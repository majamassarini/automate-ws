import asyncio
from ws.handler.appliance.handler import _event_class
from aiohttp_security import check_permission
from multidict import MultiDict
from urllib.parse import parse_qsl

from ws.authorization import Policy
from ws.handler.appliance import Handler as Parent


class Handler(Parent):
    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        send_enabled = data.get("send_type") == "send_enabled"
        send_value = data.get("send_type") == "send_value"
        selected_names = set(data.getall("appliance_name", []))

        k = _event_class(module, klass)

        event = None
        for e in appliance.events:
            if type(e) == k:
                event = e
                break

        enabled = appliance.is_enabled(event)

        for collection in self._home_resources.appliances:
            for other in self._home_resources.appliances[collection]:
                if other.name in selected_names:
                    other_event = None
                    for e in other.events:
                        if type(e) == k:
                            other_event = e
                            break

                    if send_enabled:
                        if enabled:
                            other.enable(other_event)
                        else:
                            other.disable(other_event)

                    if send_value:
                        other.notify(event)

                    await self._home_resources.redis_gateway.save(other)
                    await self._home_resources.redis_gateway.notify(other)
                    await asyncio.sleep(0.1)

    async def post(self, request):
        await check_permission(request, Policy.EDIT_PERMISSION)
        appliance = await self.get_appliance(request)
        request_data = await request.content.read()
        request_data = MultiDict(parse_qsl(request_data.decode(self.ENCODING)))
        await self._post(request_data, appliance)
        context = await self._get_response_data(request, appliance)
        return self._render_partial(request, context)
