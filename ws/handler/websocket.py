from aiohttp import web

from ws.handler import Handler as Parent
from ws.handler.appliance import registry as appliance_registry
from ws.handler.event import registry as event_registry


class Handler(Parent):
    async def get(self, request):
        websocket = web.WebSocketResponse()

        await websocket.prepare(request)
        self._home_resources.websockets.append(websocket)
        try:
            while True:
                await websocket.receive()
        except RuntimeError as e:
            self._logger.debug(e)
        finally:
            self._home_resources.websockets.remove(websocket)

        return websocket

    async def on_appliance_update(self, new_appliance):
        appliance = self._home_resources.appliances.find(new_appliance.name)
        old_state, new_state = appliance.update(new_appliance)
        if old_state != new_state:
            for websocket in self._home_resources.websockets:
                msg = self.make_websocket_msg(appliance)
                await websocket.send_str(msg)
                appliance_handler = appliance_registry.mapper[appliance.__class__]
                for num, event in enumerate(appliance.events):
                    try:
                        try:
                            handler = event_registry.mapper[
                                self.get_registry_key(appliance, event)
                            ]
                        except KeyError:
                            handler = event_registry.mapper[
                                self.get_registry_key(None, event)
                            ]
                        msg = handler(self._home_resources).make_websocket_msg(
                            self.get_html_id(appliance.name),
                            appliance_handler(self._home_resources),
                            appliance,
                            num,
                            event,
                        )
                        await websocket.send_str(msg)
                    except KeyError:
                        self._logger.error(
                            "No websocket msg representation for event {} of class {}".format(
                                event, event.__class__
                            )
                        )

                self._logger.info("Appliance updated: {}".format(appliance))

    async def on_shutdown(self, app):
        for websocket in self._home_resources.websockets:
            await websocket.close(code=999, message="Server shutdown")
