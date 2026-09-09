import asyncio
from ws.handler.appliance.handler import _event_class

from ws.handler.appliance import Handler as Parent


class Handler(Parent):
    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        enable = True if data["value"] == "true" else False
        k = _event_class(module, klass)

        event = None
        for event in appliance.events:
            if type(event) == k:
                break

        for collection in self._home_resources.appliances:
            for other in self._home_resources.appliances[collection]:
                if other.__class__ == appliance.__class__:
                    if enable:
                        other.enable(event)
                    else:
                        other.disable(event)
                    await self._home_resources.redis_gateway.save(other)
                    await self._home_resources.redis_gateway.notify(other)
                    await asyncio.sleep(0.1)
