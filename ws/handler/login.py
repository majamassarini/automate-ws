import aiohttp_jinja2
from aiohttp import web

from aiohttp_security import remember
from ws.authorization import check_credentials
from ws.handler.index import Handler as Parent


class Handler(Parent):
    @aiohttp_jinja2.template("index.html")
    async def post(self, request):
        response = web.HTTPFound("/")
        form = await request.post()
        username = form.get("username")
        password = form.get("password")

        verified = await check_credentials(request.app.credentials, username, password)
        if verified:
            await remember(request, response, username)
            return response

        return web.HTTPUnauthorized(body="Invalid username / password combination")
