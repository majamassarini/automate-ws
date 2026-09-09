from ws.handler.appliance.handler import _event_class

from ws.handler.appliance import Handler as Parent


class Handler(Parent):
    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        enable = True if data["value"] == "true" else False
        k = _event_class(module, klass)
        for e in appliance.events:
            if type(e) == k:
                if enable:
                    appliance.enable(e)
                else:
                    appliance.disable(e)
        await self._home_resources.redis_gateway.save(appliance)
        await self._home_resources.redis_gateway.notify(appliance)
