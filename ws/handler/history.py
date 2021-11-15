import logging
import time
import aiohttp_jinja2
from ws.handler.event import registry

from ws.handler import Handler as Parent


class Handler(Parent):

    DEFAULT_NUM_OF_EVENTS = 100

    async def get_history(self, appliance, num_of_events):
        history_strs = list()
        history = await self._home_resources.redis_gateway.get_history(
            appliance, num_of_events
        )
        for idx, (timestamp, old_appliance) in enumerate(history):
            if isinstance(old_appliance, dict):
                skip = True
            else:
                skip = False

            try:
                events = old_appliance - history[idx + 1][1]
            except IndexError:
                events = set()
            except TypeError as e:
                logging.getLogger(__name__).error(
                    "{} for appliance {}".format(e, appliance)
                )
                events = set()
                skip = True

            event_details = list()
            for event in events:
                try:
                    handler = registry.mapper[self.get_registry_key(appliance, event)]
                except KeyError as e:
                    handler = registry.mapper[self.get_registry_key(None, event)]
                    logging.getLogger(__name__).error("{}".format(e))

                if handler:
                    event_description = handler(
                        self._home_resources
                    ).get_description_for_history(event)
                    event_icon = handler(self._home_resources).get_icon(event)
                    event_details.append((event_description, event_icon))
                else:
                    skip = True

            if not skip:
                history_strs.append(
                    (
                        time.ctime(float(timestamp)),
                        old_appliance,
                        self.get_appliance_bean(old_appliance),
                        event_details,
                    )
                )

        return history_strs

    async def _get_response_data(self, request, appliance, num_of_events):
        history = await self.get_history(appliance, num_of_events)
        collection = self._home_resources.appliances.collection_for(appliance)
        collection_url = request.app.router["collection"].url_for(name=collection)
        history_url = request.app.router["history"].url_for(name=appliance.name)
        user = await self.get_user(request)
        return {
            "user": user,
            "appliance": appliance,
            "id": self.get_html_id(appliance.name),
            "appliance_uri": request.app.router["appliance"].url_for(
                name=appliance.name
            ),
            "history": history,
            "collection_url": collection_url,
            "collection": collection,
            "history_url": history_url,
        }

    @aiohttp_jinja2.template("history.html")
    async def get(self, request):
        appliance = await self.get_appliance(request)
        response_data = await self._get_response_data(
            request, appliance, self.DEFAULT_NUM_OF_EVENTS
        )
        return response_data

    @aiohttp_jinja2.template("history.html")
    async def post(self, request):
        request_data = await request.post()
        num_of_events = request_data["num-of-events"]
        appliance = await self.get_appliance(request)
        response_data = await self._get_response_data(
            request, appliance, int(num_of_events)
        )
        return response_data
