import home


class OnRedisMsg(home.builder.listener.OnRedisMsg):
    def __init__(self, websocket_handler, home_resources):
        self._home_resources = home_resources
        self._websocket_handler = websocket_handler

    async def on_appliance_updated(self, new_appliance):
        await self._websocket_handler.on_appliance_update(new_appliance)

    async def on_performer_updated(self, performer, old_state, new_state):
        msgs = performer.execute(old_state, new_state)  # noqa
