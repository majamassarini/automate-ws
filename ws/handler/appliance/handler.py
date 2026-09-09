import aiohttp
import aiohttp_jinja2
import importlib
import home.event
from aiohttp import web
from aiohttp_security import check_permission
from urllib.parse import parse_qsl
from multidict import MultiDict

from ws.authorization import Policy
from ws.handler import Handler as Parent

templates_dir = {
    "home.appliance.x.y.z": "a directory under event",
}


def _event_class(module: str, klass: str) -> type:
    """Return the event class for *module.klass*.

    The home.event.registry only contains home.event.enumeration.Enum
    subclasses (forced states, sun phases, …).  Float/int/str-based
    appliance events (brightness, volume, duration, setpoint …) are not
    registered there, so a registry miss falls back to importlib.

    Only modules whose dotted path starts with "home." are accepted; any
    other value is rejected with HTTP 400 to keep the original security
    guarantee against arbitrary-module injection.
    """
    key = f"{module}.{klass}"
    # 1. Exact class-level key (added by our automate-home patch)
    cls = home.event.registry.get(key)
    if cls is not None:
        return cls
    # 2. Member-level prefix scan (e.g. "module.Class.On" → Class)
    prefix = key + "."
    for k, v in home.event.registry.items():
        if k.startswith(prefix):
            return v
    # 3. Importlib fallback for non-Enum event types.  "builtins" is allowed
    #    for handlers whose KLASS is a Python primitive (float, int, str);
    #    everything else must be inside the "home." package namespace.
    if not (module.startswith("home.") or module == "builtins"):
        raise web.HTTPBadRequest(reason=f"Unknown event: {key}")
    try:
        m = importlib.import_module(module)
        return vars(m)[klass]
    except (ImportError, KeyError, AttributeError):
        raise web.HTTPBadRequest(reason=f"Unknown event: {key}")


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
        collection_url = request.app.router["collection"].url_for(
            name=collection
        )
        history_url = request.app.router["history"].url_for(
            name=appliance.name
        )
        details_url = request.app.router["details"].url_for(
            name=appliance.name
        )
        user = await self.get_user(request)

        ctx = {
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
            "apply_to_others_url": request.app.router[
                "apply_to_others"
            ].url_for(name=appliance.name),
            "send_to_collection_url": request.app.router[
                "send_to_collection"
            ].url_for(name=appliance.name),
            "send_to_others_url": request.app.router["send_to_others"].url_for(
                name=appliance.name
            ),
            "send_modal_url": request.app.router["send_modal"].url_for(
                name=appliance.name
            ),
            "event_beans": self.get_event_beans(appliance),
            "collection_url": collection_url,
            "history_url": history_url,
            "details_url": details_url,
            "collection": collection,
            "oob": False,
        }
        return self.localize_context(request, ctx)

    def _render_partial(self, request, context):
        """Render the appliance partial template to an HTML string response."""
        html = aiohttp_jinja2.render_string(
            "appliance_partial.html", request, context
        )
        return aiohttp.web.Response(
            body=html.encode(self.ENCODING), content_type="text/html"
        )

    async def get(self, request):
        appliance = await self.get_appliance(request)
        context = await self._get_response_data(request, appliance)
        return aiohttp_jinja2.render_template(
            context["bean"].template, request, context
        )

    async def _post(self, data, appliance):
        module = data["module"]
        klass = data["klass"]
        k = _event_class(module, klass)
        handler = self.get_event_handler(appliance, k, False)
        event = handler(self._home_resources).post(data)
        _, new_state = appliance.notify(event)
        await self._home_resources.redis_gateway.save(appliance)
        await self._home_resources.redis_gateway.notify(appliance)

    async def post(self, request):
        await check_permission(request, Policy.EDIT_PERMISSION)
        appliance = await self.get_appliance(request)

        request_data = await request.content.read()
        request_data = MultiDict(parse_qsl(request_data.decode(self.ENCODING)))

        await self._post(request_data, appliance)

        context = await self._get_response_data(request, appliance)
        return self._render_partial(request, context)
