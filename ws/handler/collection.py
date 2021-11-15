import aiohttp_jinja2

from ws.handler import Handler as Parent


class Handler(Parent):
    @aiohttp_jinja2.template("collection.html")
    async def get(self, request):
        collection = request.match_info.get("name")
        appliances_urls = dict()
        appliances = list()
        for appliance in self._home_resources.appliances[collection]:
            await self._home_resources.redis_gateway.update(appliance)
            appliances_urls[appliance.name] = request.app.router["appliance"].url_for(
                name=appliance.name
            )
            appliances.append(
                (
                    appliance,
                    self.get_appliance_bean(appliance),
                    self.get_event_beans(appliance),
                )
            )
        user = await self.get_user(request)
        return {
            "user": user,
            "collection": collection,
            "appliances": appliances,
            "appliances_urls": appliances_urls,
        }
