import logging
import aiohttp_jinja2
from datetime import datetime

from ws.handler.event import registry
from ws.handler import Handler as Parent
from ws.i18n import get_locale, make_format_ts_short, make_translator

HISTORY_STEP = 10
HISTORY_MAX_DEPTH = 52


class Handler(Parent):
    async def get_changes(self, request, history, new_appliance, translator):
        old_old_appliance = None
        last_timestamp = None
        appliance = None
        changed = False
        appliance_url = ""
        event_details = list()
        actual_events = list()

        for idx, (timestamp, old_appliance) in enumerate(history):
            if not last_timestamp:
                last_timestamp = timestamp
                appliance = old_appliance

            try:
                old_old_appliance = history[idx + 1][1]
                events = old_appliance - old_old_appliance
                changed = bool(events)
                appliance_url = request.app.router["appliance"].url_for(
                    name=appliance.name
                )
            except IndexError as e:
                events = set()
                self._logger.debug(
                    "Appliance {} exception in index handler {}".format(
                        old_appliance, e
                    )
                )
            except TypeError as e:
                events = set()
                self._logger.debug(
                    "Appliance {} exception in index handler {}".format(
                        old_appliance, e
                    )
                )
            except AttributeError as e:
                events = set()
                self._logger.debug(
                    "Old appliance %s, old old appliance %s, exception %s",
                    old_appliance,
                    old_old_appliance,
                    e,
                )

            for event in events:
                try:
                    handler = registry.mapper[
                        self.get_registry_key(appliance, event)
                    ]
                except KeyError:
                    handler = registry.mapper[
                        self.get_registry_key(None, event)
                    ]
                except KeyError as e:
                    handler = None
                    logging.getLogger(__name__).error("{}".format(e))

                if handler:
                    h = handler.with_translator(
                        self._home_resources, translator
                    )
                    event_icon = h.get_icon(event)
                    event_description = h.get_description_for_index(event)
                    event_details.append((event_icon, event_description))

            actual_events = self.get_event_beans(new_appliance)

        return (
            changed,
            last_timestamp,
            appliance_url,
            appliance,
            event_details,
            actual_events,
        )

    async def get_history(self, request, depth=2):
        locale = get_locale(request)
        format_ts_short = make_format_ts_short(locale)
        translator = make_translator(locale)
        history = []
        for collection in self._home_resources.appliances.values():
            for appliance in collection:
                _history = (
                    await self._home_resources.redis_gateway.get_history(
                        appliance, depth
                    )
                )
                for i in range(len(_history) - 1):
                    pair = [_history[i], _history[i + 1]]
                    (
                        changed,
                        timestamp,
                        appliance_url,
                        old_appliance,
                        event_details,
                        actual_events,
                    ) = await self.get_changes(
                        request, pair, appliance, translator
                    )
                    if changed and timestamp:
                        try:
                            ts = float(timestamp)
                            dt = datetime.fromtimestamp(ts)
                            now = datetime.now()
                            ts_str = format_ts_short(dt, now)
                        except (TypeError, ValueError, OSError):
                            ts = 0.0
                            ts_str = ""
                        history.append(
                            (
                                ts,
                                (
                                    appliance_url,
                                    old_appliance,
                                    self.get_appliance_bean(old_appliance),
                                    event_details,
                                    actual_events,
                                    ts_str,
                                ),
                            )
                        )
        history.sort(key=lambda x: x[0], reverse=True)
        return [v for _, v in history]

    async def _get_response_data(self, request, depth=2):
        history = await self.get_history(request, depth)
        user = await self.get_user(request)
        return self.localize_context(
            request,
            {
                "history": history,
                "user": user,
                "next_depth": min(depth + HISTORY_STEP, HISTORY_MAX_DEPTH),
                "has_more": depth < HISTORY_MAX_DEPTH,
            },
        )

    @aiohttp_jinja2.template("index.html")
    async def get(self, request):
        return await self._get_response_data(request)

    async def get_more(self, request):
        try:
            depth = int(request.rel_url.query.get("depth", "2"))
        except ValueError:
            depth = 2
        depth = min(max(depth, 2), HISTORY_MAX_DEPTH)
        context = await self._get_response_data(request, depth)
        return aiohttp_jinja2.render_template(
            "index_history.html", request, context
        )
