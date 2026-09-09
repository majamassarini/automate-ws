"""Regression tests for _event_class() and the action endpoints.

Before commit a5efa1e, the toggle (enable/disable) and send-modal
buttons were broken for every non-Enum event type (brightness, volume,
duration, setpoint …) because home.event.registry only contains
Enum subclasses.  These tests ensure that both lookup paths keep
working after any future refactoring.
"""

import unittest

from aiohttp import web

from ws.handler.appliance.handler import _event_class
from ws.tests.testcase import AuthenticatedTestCase, Resources
from ws.handler import Handler as BaseHandler


# ---------------------------------------------------------------------------
# _event_class unit tests (no HTTP, no server)
# ---------------------------------------------------------------------------


class TestEventClassLookup(unittest.TestCase):

    # --- Enum-based events (in home.event.registry) ---

    def test_enum_forced_light(self):
        cls = _event_class("home.appliance.light.event.forced", "Event")
        import home.appliance.light.event.forced.event as m

        self.assertIs(cls, m.Event)

    def test_enum_forced_curtain(self):
        cls = _event_class("home.appliance.curtain.event.forced", "Event")
        import home.appliance.curtain.event.forced.event as m

        self.assertIs(cls, m.Event)

    def test_enum_forced_socket(self):
        cls = _event_class("home.appliance.socket.event.forced", "Event")
        import home.appliance.socket.event.forced.event as m

        self.assertIs(cls, m.Event)

    def test_enum_enable_event(self):
        cls = _event_class("home.event.enable", "Event")
        import home.event.enable as m

        self.assertIs(cls, m.Event)

    def test_enum_sun_brightness(self):
        cls = _event_class("home.event.sun.brightness", "Event")
        import home.event.sun.brightness as m

        self.assertIs(cls, m.Event)

    # --- Non-Enum events (importlib fallback) ---

    def test_float_brightness(self):
        cls = _event_class("home.appliance.light.event.brightness", "Event")
        import home.appliance.light.event.brightness as m

        self.assertIs(cls, m.Event)

    def test_float_thermostat_setpoint(self):
        cls = _event_class(
            "home.appliance.thermostat.presence.event.setpoint", "Event"
        )
        import home.appliance.thermostat.presence.event.setpoint as m

        self.assertIs(cls, m.Event)

    def test_float_sprinkler_duration(self):
        cls = _event_class("home.appliance.sprinkler.event.duration", "Event")
        import home.appliance.sprinkler.event.duration as m

        self.assertIs(cls, m.Event)

    def test_float_sound_player_volume(self):
        cls = _event_class("home.appliance.sound.player.event.volume", "Event")
        import home.appliance.sound.player.event.volume as m

        self.assertIs(cls, m.Event)

    def test_float_sound_player_sleepy_volume(self):
        cls = _event_class(
            "home.appliance.sound.player.event.sleepy_volume", "Event"
        )
        import home.appliance.sound.player.event.sleepy_volume as m

        self.assertIs(cls, m.Event)

    # --- Security: non-home modules are rejected ---

    def test_rejects_os_module(self):
        with self.assertRaises(web.HTTPBadRequest):
            _event_class("os", "system")

    def test_rejects_subprocess_module(self):
        with self.assertRaises(web.HTTPBadRequest):
            _event_class("subprocess", "Popen")

    def test_allows_builtins_float(self):
        # Some event handlers use KLASS = float/int (Python builtins).
        self.assertIs(_event_class("builtins", "float"), float)

    def test_allows_builtins_int(self):
        self.assertIs(_event_class("builtins", "int"), int)

    def test_rejects_unknown_builtin(self):
        with self.assertRaises(web.HTTPBadRequest):
            _event_class("builtins", "NonExistentClass")

    def test_rejects_unknown_home_module(self):
        with self.assertRaises(web.HTTPBadRequest):
            _event_class("home.nonexistent.module.path", "Event")


# ---------------------------------------------------------------------------
# HTTP integration: every field-test appliance with a label has a
# working toggle endpoint (enable=false then enable=true).
# ---------------------------------------------------------------------------


class TestEnableEndpointAllBeans(AuthenticatedTestCase):
    """Ensure no event bean produces HTTP 400 from the enable endpoint."""

    @classmethod
    def setUpClass(cls):
        resources = Resources(None, None, "ws", "brain")
        handler = BaseHandler(resources)
        cls._cases = []
        for coll in resources.appliances.values():
            for appliance in coll:
                for bean in handler.get_event_beans(appliance):
                    if bean.label:
                        cls._cases.append(
                            (appliance.name, bean.module, bean.klass)
                        )

    async def test_enable_endpoint_for_all_beans(self):
        for appliance_name, module, klass in self._cases:
            with self.subTest(appliance=appliance_name, module=module):
                url = "/appliance/{}/enable".format(
                    appliance_name.replace(" ", "%20")
                )
                r = await self.client.request(
                    "POST",
                    url,
                    data={"module": module, "klass": klass, "value": "false"},
                )
                self.assertEqual(
                    r.status,
                    200,
                    f"enable POST returned {r.status} for "
                    f"{appliance_name!r} module={module!r}",
                )


# ---------------------------------------------------------------------------
# HTTP integration: send_modal GET for representative Enum and non-Enum beans
# ---------------------------------------------------------------------------


class TestSendModalEndpoint(AuthenticatedTestCase):

    async def _get_modal(self, appliance_name, module, klass):
        url = "/appliance/{}/send_modal".format(
            appliance_name.replace(" ", "%20")
        )
        return await self.client.request(
            "GET", url, params={"module": module, "klass": klass}
        )

    async def test_send_modal_enum_forced_light(self):
        r = await self._get_modal(
            "simple light",
            "home.appliance.light.event.forced",
            "Event",
        )
        self.assertEqual(r.status, 200)

    async def test_send_modal_non_enum_brightness(self):
        r = await self._get_modal(
            "hue light",
            "home.appliance.light.event.brightness",
            "Event",
        )
        self.assertEqual(r.status, 200)

    async def test_send_modal_non_enum_sprinkler_duration(self):
        r = await self._get_modal(
            "sprinkler for grass",
            "home.appliance.sprinkler.event.duration",
            "Event",
        )
        self.assertEqual(r.status, 200)


if __name__ == "__main__":
    unittest.main()
