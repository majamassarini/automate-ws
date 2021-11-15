import logging
import collections
import aiohttp_jinja2

from ws.handler.event import registry
from ws.handler import Handler as Parent


class Handler(Parent):
    async def get_changes(self, request, history, new_appliance):
        old_old_appliance = None
        last_timestamp = None
        appliance = None
        changed = False
        appliance_url = ""
        event_details = list()
        actual_events = list()

        for idx, (timestamp, old_appliance) in enumerate(history):
            if not last_timestamp:
                last_timestamp = timestamp
                appliance = old_appliance

            try:
                old_old_appliance = history[idx + 1][1]
                events = old_appliance - old_old_appliance
                changed = (
                    old_old_appliance.state.compute() != old_appliance.state.compute()
                    or old_appliance.state.is_forced()
                )
                appliance_url = request.app.router["appliance"].url_for(
                    name=appliance.name
                )
            except IndexError as e:
                events = set()
                self._logger.debug(
                    "Appliance {} exception in index handler {}".format(
                        old_appliance, e
                    )
                )
            except TypeError as e:
                events = set()
                self._logger.debug(
                    "Appliance {} exception in index handler {}".format(
                        old_appliance, e
                    )
                )
            except AttributeError as e:
                events = set()
                self._logger.debug(
                    "Old appliance {}, old old appliance {}, exception {}".format(
                        old_appliance, old_old_appliance, e
                    )
                )

            for event in events:
                try:
                    handler = registry.mapper[self.get_registry_key(appliance, event)]
                except KeyError:
                    handler = registry.mapper[self.get_registry_key(None, event)]
                except KeyError as e:
                    handler = None
                    logging.getLogger(__name__).error("{}".format(e))

                if handler:
                    event_icon = handler(self._home_resources).get_icon(event)
                    event_description = handler(
                        self._home_resources
                    ).get_description_for_index(event)
                    event_details.append((event_icon, event_description))

            actual_events = self.get_event_beans(new_appliance)

        return (
            changed,
            last_timestamp,
            appliance_url,
            appliance,
            event_details,
            actual_events,
        )

    async def get_history(self, request):
        history = dict()
        for collection in self._home_resources.appliances.values():
            for appliance in collection:
                _history = await self._home_resources.redis_gateway.get_history(
                    appliance, 2
                )
                if _history:
                    (
                        changed,
                        timestamp,
                        appliance_url,
                        old_appliance,
                        event_details,
                        actual_events,
                    ) = await self.get_changes(request, _history, appliance)
                    if changed:
                        history[timestamp] = (
                            appliance_url,
                            old_appliance,
                            self.get_appliance_bean(old_appliance),
                            event_details,
                            actual_events,
                        )
        sorted_history = collections.OrderedDict(sorted(history.items(), reverse=True))
        return sorted_history.values()

    async def _get_response_data(self, request):
        history = await self.get_history(request)
        user = await self.get_user(request)
        return {
            "history": history,
            "user": user,
        }

    @aiohttp_jinja2.template("index.html")
    async def get(self, request):
        response_data = await self._get_response_data(request)
        return response_data
