import aiohttp_jinja2
from aiohttp import web

from aiohttp_security import remember
from aiohttp_session import get_session
from ws.authorization import check_credentials
from ws.handler.index import Handler as Parent

REMEMBER_ME_MAX_AGE = 30 * 24 * 3600  # 30 days


class Handler(Parent):
    @aiohttp_jinja2.template("index.html")
    async def post(self, request):
        response = web.HTTPFound("/")
        form = await request.post()
        username = form.get("username")
        password = form.get("password")
        remember_me = form.get("remember_me") == "1"

        verified = await check_credentials(
            request.app["credentials"], username, password
        )
        if verified:
            if remember_me:
                session = await get_session(request)
                session.max_age = REMEMBER_ME_MAX_AGE
            await remember(request, response, username)
            return response

        return web.HTTPUnauthorized(
            body="Invalid username / password combination"
        )
