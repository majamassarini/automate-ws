import aiohttp_jinja2
from aiohttp import web

from aiohttp_security import forget, check_authorized
from ws.handler.index import Handler as Parent


class Handler(Parent):
    @aiohttp_jinja2.template("index.html")
    async def post(self, request):
        response = web.HTTPFound("/")
        await check_authorized(request)
        await forget(request, response)
        return response
