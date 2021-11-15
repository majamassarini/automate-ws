import importlib

from ws.handler.appliance import Handler as Parent


class Handler(Parent):
    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        m = importlib.import_module(module)
        k = getattr(m, klass)

        event = None
        for event in appliance.events:
            if type(event) == k:
                break

        collection = self._home_resources.appliances.collection_for(appliance)
        for other in self._home_resources.appliances[collection]:
            if other.__class__ == appliance.__class__:
                other.notify(event)
                await self._home_resources.redis_gateway.save(other)
                await self._home_resources.redis_gateway.notify(other)
