import aiohttp_jinja2
from aiohttp_security import check_permission

from ws.authorization import Policy
from ws.handler.appliance import Handler as Parent
from ws.handler.appliance.handler import _event_class


class Handler(Parent):
    async def get(self, request):
        await check_permission(request, Policy.EDIT_PERMISSION)
        appliance = await self.get_appliance(request)
        await self._home_resources.redis_gateway.update(appliance)

        module = request.rel_url.query.get("module")
        klass = request.rel_url.query.get("klass")
        k = _event_class(module, klass)

        event = None
        event_num = 0
        for num, e in enumerate(appliance.events):
            if type(e) == k:
                event = e
                event_num = num
                break

        event_handler = self.get_event_handler(appliance, event)
        bean = event_handler.get(event)
        appliance_id = self.get_html_id(appliance.name)
        bean.set_enabled(appliance, event)
        bean.set_id(appliance_id, event_num)
        bean.set_id_enabled(appliance_id, event_num)
        bean.set_id_icon(appliance_id, event_num)
        bean.set_id_label(appliance_id, event_num)

        similar = []
        for collection in self._home_resources.appliances:
            for other in self._home_resources.appliances[collection]:
                if (
                    other.__class__ == appliance.__class__
                    and other is not appliance
                ):
                    await self._home_resources.redis_gateway.update(other)
                    similar.append(other)

        send_to_selected_url = request.app.router["send_to_selected"].url_for(
            name=appliance.name
        )
        user = await self.get_user(request)

        ctx = self.localize_context(
            request,
            {
                "user": user,
                "appliance": appliance,
                "bean": bean,
                "module": module,
                "klass": klass,
                "similar": similar,
                "send_to_selected_url": send_to_selected_url,
                "id": appliance_id,
            },
        )
        return aiohttp_jinja2.render_template(
            "event/send_modal_body.html",
            request,
            ctx,
        )
