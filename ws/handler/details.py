import aiohttp_jinja2

from ws.handler.appliance import Handler as Parent


class Handler(Parent):

    ENCODING = "utf-8"

    def get_performers(self, appliance):
        performers = list()
        for performer in self._home_resources.brain_performers:
            if performer.is_for(appliance):
                performers.append(performer)
        return performers

    def get_group_of_performers(self, appliance):
        group_of_performers_names = set()
        group_of_performers = set()
        for key, value in self._home_resources.brain_group_of_performers.items():
            for performer in value:
                if performer.is_for(appliance):
                    group_of_performers_names.add(key)
                    group_of_performers.add(performer)
        return group_of_performers_names, group_of_performers

    def get_scheduler_triggers(self, group_of_performers):
        scheduler_triggers = set()
        for (performers, triggers) in self._home_resources.brain_schedule_infos:
            if set(performers).intersection(set(group_of_performers)):
                for trigger in triggers:
                    scheduler_triggers.add(
                        "{} will notify {}".format(
                            trigger.name, [str(e) for e in trigger.events]
                        )
                    )
        return scheduler_triggers

    async def _get_response_data(self, request, appliance):
        performers = self.get_performers(appliance)
        group_of_performers_names, group_of_performers = self.get_group_of_performers(
            appliance
        )
        scheduler_triggers = self.get_scheduler_triggers(group_of_performers)
        collection = self._home_resources.appliances.collection_for(appliance)
        collection_url = request.app.router["collection"].url_for(name=collection)
        history_url = request.app.router["history"].url_for(name=appliance.name)
        user = await self.get_user(request)
        return {
            "user": user,
            "appliance": appliance,
            "id": self.get_html_id(appliance.name),
            "appliance_url": request.app.router["appliance"].url_for(
                name=appliance.name
            ),
            "collection_url": collection_url,
            "history_url": history_url,
            "collection": collection,
            "performers": performers,
            "group_of_performers": group_of_performers_names,
            "scheduler_triggers": scheduler_triggers,
        }

    @aiohttp_jinja2.template("details.html")
    async def get(self, request):
        appliance = await self.get_appliance(request)
        response_data = await self._get_response_data(request, appliance)
        return response_data
