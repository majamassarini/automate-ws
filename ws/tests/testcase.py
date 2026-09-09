import os
import copy
import datetime
import enum as python_enum
import glob
import pathlib
import aiohttp_jinja2
import jinja2
import logging
import yaml
import home
import home.scheduler.trigger.sun
import home.scheduler.trigger.sun.sunrise
import home.scheduler.trigger.sun.sunset
import home.scheduler.trigger.sun.sunhit
import home.scheduler.trigger.sun.sunleft
import home.scheduler.trigger.sun.twilight.civil.sunrise
import home.scheduler.trigger.sun.twilight.civil.sunset
import home.scheduler.trigger.sun.twilight.astronomical.sunrise
import home.scheduler.trigger.sun.twilight.astronomical.sunset
import home.scheduler.trigger.cron
import home.scheduler.trigger.interval
import home.scheduler.trigger.circadian_rhythm
import home.scheduler.trigger.state.entering
import home.scheduler.trigger.state.entering.delay
import home.scheduler.trigger.state.entering.delay.duration
import home.scheduler.trigger.state.exiting
import home.scheduler.trigger.state.exiting.delay
import home.scheduler.trigger.date.resettable
import home.scheduler.trigger.protocol
import home.scheduler.trigger.protocol.delay
import home.scheduler.trigger.protocol.enum
import home.scheduler.trigger.protocol.mean
import home.scheduler.trigger.protocol.multi
import home.scheduler.trigger.protocol.timer
import home.scheduler.trigger.crawler.osmer_fvg.will_rain.on
import home.scheduler.trigger.crawler.osmer_fvg.will_rain.off
import home.scheduler.trigger.state.entering.disable_events
import home.scheduler.trigger.state.entering.delay.enable_events
import ws
import ws.authorization

from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web
from aiohttp_security import setup as setup_security
from aiohttp_security import SessionIdentityPolicy
from aiohttp_session import setup as setup_session
from aiohttp_session import SimpleCookieStorage
from home.performer import Performer


LOGGER_NAME = "ws tests"


class _MockLabel:
    def __init__(self, label, addresses=None):
        self.label = label
        self.addresses = addresses or []


class _MockEvent:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class _MockStateEnum(python_enum.Enum):
    A = "A"
    B = "B"
    C = "C"


class _MockState:
    def __init__(self, value, duration=0):
        self.VALUE = value
        self.duration = duration


class _MockPerformerTrigger:
    """Mock protocol trigger for performer.triggers — carries the appliance's real events."""

    def __init__(self, label, addresses, events):
        self.label = label
        self.addresses = addresses
        self.events = list(events)

    def is_triggered(self, _):
        return False


class _MockProtocolTrigger:
    def __init__(self, addresses=None):
        self.label = "mock bus trigger"
        self.addresses = addresses or []
        self.events = []

    def is_triggered(self, _):
        return False


class _MockMeanProtocolTrigger(_MockProtocolTrigger):
    def get_value(self, _):
        return 0.0


class _MockCronTrigger:
    __module__ = "cron"

    def __init__(self, name, events=()):
        self._name = name
        self._events = list(events)

    @property
    def name(self):
        return self._name

    @property
    def events(self):
        return self._events


class RedisGatewayStub:
    _timestamp = 0

    def run(self, _, __):
        pass

    async def update(self, appliance):
        logging.getLogger(__name__).warning("update {}".format(appliance))

    async def save(self, appliance):
        logging.getLogger(__name__).warning("save {}".format(appliance))

    async def notify(self, appliance):
        logging.getLogger(__name__).warning("notify {}".format(appliance))

    async def get_history_range(
        self, appliance, start_ts: float, end_ts: float
    ):
        forced_events = list(appliance.forced_enum)
        history = []
        for i, ts in enumerate(
            range(int(start_ts), min(int(end_ts) + 1, int(start_ts) + 100))
        ):
            a = copy.deepcopy(appliance)
            if forced_events:
                a.notify(forced_events[i % len(forced_events)])
            history.append((str(float(ts)), a))
        return history

    async def get_history(self, appliance, num_of_events):
        forced_events = list(appliance.forced_enum)
        history = list()
        for i in range(0, num_of_events):
            a = copy.deepcopy(appliance)
            if forced_events:
                a.notify(forced_events[i % len(forced_events)])
            history.append((RedisGatewayStub._timestamp, a))
            RedisGatewayStub._timestamp += 1
        return history


class Resources(home.builder.listener.Resources):
    def __init__(
        self, redis_host, redis_port, my_node_name, other_nodes_names
    ):
        from ws.tests import testcase  # noqa

        yaml_dir = os.path.join(
            pathlib.Path(testcase.__file__).resolve().parent, "project"
        )
        super(Resources, self).__init__(
            yaml_dir, redis_host, redis_port, my_node_name, other_nodes_names
        )
        self._redis_gateway = RedisGatewayStub()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.websockets = []
        self._mock_brain_performers = self._build_mock_brain_performers()
        self._mock_brain_group_of_performers = (
            self._build_mock_brain_group_of_performers(yaml_dir)
        )

    def _build_mock_brain_performers(self):
        performers = []
        for collection in self.appliances.values():
            for appliance in collection:
                performers.append(
                    Performer(
                        "{} performer".format(appliance.name),
                        appliance,
                        [
                            _MockLabel(
                                "{}: knx switch on/off".format(appliance.name),
                                ["1/0/1"],
                            )
                        ],
                        [
                            _MockPerformerTrigger(
                                "{}: knx trigger on".format(appliance.name),
                                ["1/0/2"],
                                appliance.events,
                            ),
                        ],
                    )
                )
        return performers

    @property
    def brain_performers(self):
        return self._mock_brain_performers

    def _build_mock_brain_group_of_performers(self, yaml_dir):
        performers_by_name = {
            p.appliance.name: p for p in self._mock_brain_performers
        }
        groups = {}
        for path in glob.glob(os.path.join(yaml_dir, "performers", "*.yaml")):
            with open(path) as f:
                data = yaml.safe_load(f)
            if not isinstance(data, dict):
                continue
            for group_name, appliance_names in data.items():
                group = [
                    performers_by_name[name]
                    for name in appliance_names
                    if name in performers_by_name
                ]
                if group:
                    groups[group_name] = group
        return groups

    @property
    def brain_group_of_performers(self):
        return self._mock_brain_group_of_performers

    @property
    def brain_schedule_infos(self):
        groups = self._mock_brain_group_of_performers
        infos = []
        for group_name, performers in groups.items():
            group = home.Performers(performers)
            # Use real event instances from the group's appliances so that
            # the event-source lookup in history.py can match them against
            # old_appliance.events (which are also real enum singletons).
            appliance_events = (
                list(performers[0].appliance.events) if performers else []
            )
            sunrise = home.scheduler.trigger.sun.sunrise.Trigger(
                "sunrise",
                appliance_events,
                45.20,
                13.20,
                280,
            )
            sunset = home.scheduler.trigger.sun.sunset.Trigger(
                "sunset",
                appliance_events,
                45.20,
                13.20,
                280,
            )
            cron = home.scheduler.trigger.cron.Trigger(
                "morning alarm",
                appliance_events,
                hour=7,
                minute=30,
            )
            interval = home.scheduler.trigger.interval.Trigger(
                "temperature check",
                appliance_events,
                minutes=10,
            )
            circadian = home.scheduler.trigger.circadian_rhythm.Trigger(
                "circadian rhythm",
                appliance_events,
                appliance_events or [_MockStateEnum.A],
            )
            entering = home.scheduler.trigger.state.entering.Trigger(
                "entering on",
                appliance_events,
                "On",
            )
            exiting = home.scheduler.trigger.state.exiting.Trigger(
                "exiting on",
                appliance_events,
                "On",
            )
            resettable = home.scheduler.trigger.date.resettable.Trigger(
                "scheduled event",
                appliance_events,
                run_date=datetime.datetime.now()
                + datetime.timedelta(seconds=60),
            )

            def _pt(idx):
                """Return the inner trigger of performers[idx], or a mock."""
                if idx < len(performers):
                    return performers[idx].triggers[0]
                return _MockProtocolTrigger()

            condition = home.scheduler.trigger.protocol.Trigger(
                "condition",
                appliance_events,
                _pt(1),
            )
            # Reactive protocol trigger: inner trigger is owned by this group's
            # performer so it will appear under "Reacts to this appliance"
            reactive_condition = home.scheduler.trigger.protocol.Trigger(
                "reacts to sensor",
                appliance_events,
                _pt(0),
            )
            delay = home.scheduler.trigger.protocol.delay.Trigger(
                "delayed condition",
                appliance_events,
                _pt(2),
                30.0,
            )
            enum = home.scheduler.trigger.protocol.enum.Trigger(
                "cycle mode",
                appliance_events,
                _MockStateEnum.A,
                "next",
                _pt(3),
            )
            mean_gt = home.scheduler.trigger.protocol.mean.GreaterThan(
                "temp high",
                appliance_events,
                _MockMeanProtocolTrigger(["4/0/1"]),
                10,
                25.0,
                60.0,
            )
            mean_lt = home.scheduler.trigger.protocol.mean.LesserThan(
                "temp low",
                appliance_events,
                _MockMeanProtocolTrigger(["4/0/1"]),
                10,
                18.0,
                60.0,
            )
            mean_ib = home.scheduler.trigger.protocol.mean.InBetween(
                "temp comfortable",
                appliance_events,
                _MockMeanProtocolTrigger(["4/0/1"]),
                10,
                18.0,
                25.0,
                60.0,
            )
            multi = home.scheduler.trigger.protocol.multi.Trigger(
                "and condition",
                appliance_events,
                _pt(0),
                _pt(1),
                _pt(2),
                _pt(3),
            )
            timer = home.scheduler.trigger.protocol.timer.Trigger(
                "timed off",
                appliance_events,
                _pt(4),
                120,
                appliance_events,
                [],
            )
            position = home.scheduler.trigger.sun.Position(
                bottom_altitude=10.0,
                upper_altitude=90.0,
                min_azimuth=10.0,
                max_azimuth=160.0,
            )
            sunhit = home.scheduler.trigger.sun.sunhit.Trigger(
                "sunhit south windows",
                appliance_events,
                45.20,
                13.20,
                280,
                position,
            )
            sunleft = home.scheduler.trigger.sun.sunleft.Trigger(
                "sunleft south windows",
                appliance_events,
                45.20,
                13.20,
                280,
                position,
            )
            civil_sunrise = (
                home.scheduler.trigger.sun.twilight.civil.sunrise.Trigger(
                    "civil twilight sunrise",
                    appliance_events,
                    45.20,
                    13.20,
                    280,
                )
            )
            civil_sunset = (
                home.scheduler.trigger.sun.twilight.civil.sunset.Trigger(
                    "civil twilight sunset",
                    appliance_events,
                    45.20,
                    13.20,
                    280,
                )
            )
            astro_sunrise = home.scheduler.trigger.sun.twilight.astronomical.sunrise.Trigger(
                "astronomical twilight sunrise",
                appliance_events,
                45.20,
                13.20,
                280,
            )
            astro_sunset = home.scheduler.trigger.sun.twilight.astronomical.sunset.Trigger(
                "astronomical twilight sunset",
                appliance_events,
                45.20,
                13.20,
                280,
            )
            entering_delay = (
                home.scheduler.trigger.state.entering.delay.Trigger(
                    "auto off after 30 min",
                    appliance_events,
                    "On",
                    1800.0,
                )
            )
            exiting_delay = home.scheduler.trigger.state.exiting.delay.Trigger(
                "confirm off after 5 min",
                appliance_events,
                "On",
                300.0,
            )
            will_rain_on = (
                home.scheduler.trigger.crawler.osmer_fvg.will_rain.on.Trigger(
                    "will rain tomorrow",
                    appliance_events,
                    "http://www.osmer.fvg.it/rss.php?ln=&id=7",
                    zone=4,
                    probability=60,
                )
            )
            will_rain_off = (
                home.scheduler.trigger.crawler.osmer_fvg.will_rain.off.Trigger(
                    "will not rain tomorrow",
                    appliance_events,
                    "http://www.osmer.fvg.it/rss.php?ln=&id=7",
                    zone=4,
                    probability=60,
                )
            )
            entering_delay_duration = (
                home.scheduler.trigger.state.entering.delay.duration.Trigger(
                    "auto off after state duration",
                    appliance_events,
                    "On",
                )
            )
            # Simulate a state transition so _delay.timeout is populated with
            # the state's duration (300 s), matching real sprinkler behaviour.
            entering_delay_duration.is_triggered(
                _MockState("Off"), _MockState("On", duration=300)
            )
            disable_events = (
                home.scheduler.trigger.state.entering.disable_events.Trigger(
                    "disable forced off on entry",
                    appliance_events,
                    "On",
                )
            )
            enable_events = home.scheduler.trigger.state.entering.delay.enable_events.Trigger(
                "re-enable forced off after grace",
                appliance_events,
                "On",
                5.0,
            )
            infos.append(
                (
                    group,
                    [
                        sunrise,
                        sunset,
                        cron,
                        interval,
                        circadian,
                        entering,
                        exiting,
                        resettable,
                        condition,
                        reactive_condition,
                        delay,
                        enum,
                        mean_gt,
                        mean_lt,
                        mean_ib,
                        multi,
                        timer,
                        sunhit,
                        sunleft,
                        civil_sunrise,
                        civil_sunset,
                        astro_sunrise,
                        astro_sunset,
                        entering_delay,
                        exiting_delay,
                        entering_delay_duration,
                        disable_events,
                        enable_events,
                        will_rain_on,
                        will_rain_off,
                    ],
                )
            )
        return infos


class MyHomeTestCase(AioHTTPTestCase):
    def get_app(self):
        app = web.Application()
        resources = Resources(None, None, "ws", "brain")
        app.resources = resources
        websocket_handler = ws.handler.websocket.Handler(resources)
        app.on_shutdown.append(websocket_handler.on_shutdown)

        on_redis_msg = ws.OnRedisMsg(websocket_handler, resources)
        resources.redis_gateway.run(
            on_redis_msg.on_appliance_updated,
            on_redis_msg.on_performer_updated,
        )

        setup_session(app, SimpleCookieStorage())
        brain_policy = ws.authorization.Policy()
        setup_security(app, SessionIdentityPolicy(), brain_policy)
        app["credentials"] = brain_policy.credentials

        ws.routes.setup(app, resources, websocket_handler)
        app.add_routes(
            [
                web.static(
                    "/static",
                    os.path.join(os.path.dirname(__file__), "../static"),
                )
            ]
        )
        aiohttp_jinja2.setup(
            app,
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__), "../templates")
            ),
        )

        return app


class AuthenticatedTestCase(MyHomeTestCase):
    """Test case that logs in as admin before each test."""

    async def asyncSetUp(self):
        await super().asyncSetUp()
        await self.client.request(
            "POST",
            "/login",
            data={"username": "admin", "password": "admin"},
        )
