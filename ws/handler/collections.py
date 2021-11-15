import aiohttp_jinja2

from ws.handler import Handler as Parent


class Handler(Parent):
    @aiohttp_jinja2.template("collections.html")
    async def get(self, request):
        collections_urls = {}
        collections = list()
        for collection in self._home_resources.appliances:
            collections_urls[collection] = request.app.router["collection"].url_for(
                name=collection
            )
            appliance_beans = [
                self.get_appliance_bean(appliance)
                for appliance in self._home_resources.appliances[collection]
            ]
            collections.append((collection, appliance_beans))

        user = await self.get_user(request)
        return {
            "user": user,
            "collections": collections,
            "collections_urls": collections_urls,
        }
