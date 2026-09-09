import copy
from datetime import datetime

import aiohttp_jinja2
from aiohttp import web

from ws.handler import Handler as Parent
from ws.handler.appliance.handler import Handler as ApplianceHandler
from ws.handler.event import registry
from ws.i18n import get_locale, make_translator


class Handler(Parent):
    async def get(self, request):
        websocket = web.WebSocketResponse()

        await websocket.prepare(request)
        entry = (websocket, request)
        self._home_resources.websockets.append(entry)
        self._logger.info(
            "WebSocket connected, total: %d",
            len(self._home_resources.websockets),
        )
        try:
            while True:
                await websocket.receive()
        except RuntimeError as e:
            self._logger.debug(e)
        finally:
            self._home_resources.websockets.remove(entry)
            self._logger.info(
                "WebSocket disconnected, total: %d",
                len(self._home_resources.websockets),
            )

        return websocket

    async def _render_oob_partial(self, request, appliance):
        appliance_handler = ApplianceHandler(self._home_resources)
        context = await appliance_handler._get_response_data(
            request, appliance
        )
        context["oob"] = True
        html = aiohttp_jinja2.render_string(
            "appliance_partial.html", request, context
        )
        return html

    def _render_bean_oob(self, request, appliance):
        bean = self.get_appliance_bean(appliance)
        ctx = self.localize_context(request, {"bean": bean})
        return aiohttp_jinja2.render_string("bean_oob.html", request, ctx)

    def _compute_event_details(self, appliance, old_appliance, translator):
        event_details = []
        try:
            events = appliance - old_appliance
        except Exception:
            events = set()
        for event in events:
            try:
                handler_class = registry.mapper[
                    self.get_registry_key(appliance, event)
                ]
            except KeyError:
                try:
                    handler_class = registry.mapper[
                        self.get_registry_key(None, event)
                    ]
                except KeyError:
                    handler_class = None
            if handler_class:
                h = handler_class.with_translator(
                    self._home_resources, translator
                )
                event_details.append(
                    (h.get_icon(event), h.get_description_for_index(event))
                )
        return event_details

    def _render_index_row_oob(self, request, appliance, old_appliance):
        translator = make_translator(get_locale(request))
        now = datetime.now()
        ts_str = now.strftime("%H:%M")
        appliance_url = request.app.router["appliance"].url_for(
            name=appliance.name
        )
        event_details = self._compute_event_details(
            appliance, old_appliance, translator
        )
        actual_events = self.get_event_beans(appliance)
        bean = self.get_appliance_bean(appliance)
        ctx = self.localize_context(
            request,
            {
                "appliance_url": appliance_url,
                "old_appliance": appliance,
                "old_appliance_bean": bean,
                "event_details": event_details,
                "actual_events": actual_events,
                "timestamp": ts_str,
            },
        )
        return aiohttp_jinja2.render_string("index_row_oob.html", request, ctx)

    async def on_appliance_update(self, new_appliance):
        appliance = self._home_resources.appliances.find(new_appliance.name)
        old_appliance = copy.deepcopy(appliance)
        old_state, new_state = appliance.update(new_appliance)
        self._logger.debug(
            "Appliance %s: old=%s new=%s", appliance.name, old_state, new_state
        )
        if old_state != new_state:
            self._logger.info(
                "Appliance %s state changed, pushing to %d WebSocket(s)",
                appliance.name,
                len(self._home_resources.websockets),
            )
            for websocket, request in list(self._home_resources.websockets):
                try:
                    parts = [
                        await self._render_oob_partial(request, appliance),
                        self._render_bean_oob(request, appliance),
                        self._render_index_row_oob(
                            request, appliance, old_appliance
                        ),
                    ]
                    await websocket.send_str("\n".join(parts))
                    self._logger.debug(
                        "OOB update sent for appliance %s", appliance.name
                    )
                except Exception:
                    self._logger.warning(
                        "Could not send OOB update for appliance %s",
                        appliance.name,
                        exc_info=True,
                    )

    async def on_shutdown(self, app):
        for websocket, _ in self._home_resources.websockets:
            await websocket.close(code=999, message="Server shutdown")
