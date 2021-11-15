import aiohttp
import aiohttp_jinja2
import importlib

from urllib.parse import parse_qsl
from multidict import MultiDict

from ws.handler import Handler as Parent

templates_dir = {
    "home.appliance.x.y.z": "a directory under event",
}


class Handler(Parent):

    ENCODING = "utf-8"

    def get_templates(self, appliance):
        key = appliance.__module__ + "." + appliance.__class__.__name__
        if key in templates_dir:
            return templates_dir[key]
        else:
            return ""

    async def _get_response_data(self, request, appliance):
        templates = self.get_templates(appliance)
        collection = self._home_resources.appliances.collection_for(appliance)
        collection_url = request.app.router["collection"].url_for(name=collection)
        history_url = request.app.router["history"].url_for(name=appliance.name)
        graphs_url = request.app.router["graphs"].url_for(name=appliance.name)
        details_url = request.app.router["details"].url_for(name=appliance.name)
        user = await self.get_user(request)

        return {
            "user": user,
            "appliance": appliance,
            "id": self.get_html_id(appliance.name),
            "bean": self.get_appliance_bean(appliance),
            "templates_dir": templates,
            "appliance_url": request.app.router["appliance"].url_for(
                name=appliance.name
            ),
            "enable_event_url": request.app.router["event_enable"].url_for(
                name=appliance.name
            ),
            "apply_to_collection_url": request.app.router[
                "apply_to_collection"
            ].url_for(name=appliance.name),
            "apply_to_others_url": request.app.router["apply_to_others"].url_for(
                name=appliance.name
            ),
            "send_to_collection_url": request.app.router["send_to_collection"].url_for(
                name=appliance.name
            ),
            "send_to_others_url": request.app.router["send_to_others"].url_for(
                name=appliance.name
            ),
            "event_beans": self.get_event_beans(appliance),
            "collection_url": collection_url,
            "history_url": history_url,
            "graphs_url": graphs_url,
            "details_url": details_url,
            "collection": collection,
        }

    @aiohttp_jinja2.template("appliance.html")
    async def get(self, request):
        appliance = await self.get_appliance(request)
        context = await self._get_response_data(request, appliance)
        response = aiohttp_jinja2.render_template(
            context["bean"].template, request, context
        )
        return response

    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        m = importlib.import_module(module)
        k = getattr(m, klass)
        handler = self.get_event_handler(appliance, k, False)
        event = handler(self._home_resources).post(data)
        _, new_state = appliance.notify(event)
        await self._home_resources.redis_gateway.save(appliance)
        await self._home_resources.redis_gateway.notify(appliance)

    @aiohttp_jinja2.template("appliance.html")
    async def old_post(self, request):
        appliance = await self.get_appliance(request)

        request_data = await request.post()

        await self._post(request_data, appliance)

        response_data = await self._get_response_data(request, appliance)
        return response_data

    async def post(self, request):
        appliance = await self.get_appliance(request)

        request_data = await request.content.read()
        request_data = MultiDict(parse_qsl(request_data.decode(self.ENCODING)))

        await self._post(request_data, appliance)

        msg = self.make_websocket_msg(appliance)
        return aiohttp.web.Response(
            body=msg.encode(self.ENCODING), content_type="application/json"
        )
