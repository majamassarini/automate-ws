import importlib

from ws.handler.appliance import Handler as Parent


class Handler(Parent):
    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        enable = True if data["value"] == "true" else False
        m = importlib.import_module(module)
        k = getattr(m, klass)
        for e in appliance.events:
            if type(e) == k:
                if enable:
                    appliance.enable(e)
                else:
                    appliance.disable(e)
        await self._home_resources.redis_gateway.save(appliance)
        await self._home_resources.redis_gateway.notify(appliance)
