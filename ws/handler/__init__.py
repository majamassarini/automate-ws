import logging
import json

from aiohttp_security import authorized_userid, permits
from ws.authorization import Policy

appliance_mapper = dict()
event_mapper = dict()


class User:
    def __init__(self, id, view, edit, configure):
        self.id = id
        self.view = view
        self.edit = edit
        self.configure = configure


class Handler:
    def __init__(self, home_resources):
        self._home_resources = home_resources
        self._logger = logging.getLogger(__name__)

    async def get_appliance(self, request):
        name = request.match_info.get("name")
        appliance = self._home_resources.appliances.find(name)  # noqa
        return appliance

    async def get_user(self, request):
        uid = await authorized_userid(request)
        if uid:
            view = await permits(request, Policy.VIEW_PERMISSION)
            edit = await permits(request, Policy.EDIT_PERMISSION)
            configure = await permits(request, Policy.CONFIGURE_PERMISSION)
            return User(uid, view, edit, configure)

    def get_html_id(self, name):
        return name.replace(" ", "-").replace("(", "-").replace(")", "-")

    def make_websocket_msg(self, appliance):  # noqa
        msg = json.dumps(
            {
                "appliance": appliance.name,
                "state": appliance.state.compute(),
                "events": self.make_event_msgs(appliance),
            },
            cls=self._home_resources.json_encoder,
        )
        return msg

    def get_appliance_handler(self, appliance):  # noqa
        try:
            handler = appliance_mapper[appliance.__class__]
        except KeyError:
            from ws.handler.appliance.customization import (
                Handler as CustomizationHandler,
            )

            handler = CustomizationHandler
            self._logger.debug(
                "No customization for appliance {} of class {}".format(
                    appliance, appliance.__class__
                )
            )
        if handler:
            return handler(self._home_resources)

    def get_event_handler(self, appliance, event, get_class=True):  # noqa
        handler = None
        try:
            handler = event_mapper[self.get_registry_key(appliance, event, get_class)]
        except KeyError:
            try:
                handler = event_mapper[self.get_registry_key(None, event, get_class)]
            except KeyError:
                self._logger.error(
                    "No html representation for event {} of class {}".format(
                        event, event.__class__
                    )
                )
        if handler:
            if get_class:
                return handler(self._home_resources)
            else:
                return handler

    def make_event_msgs(self, appliance):  # noqa
        msgs = list()
        for num, event in enumerate(appliance.events):  # noqa
            handler = self.get_event_handler(appliance, event)
            if handler:
                msg = handler.make_msg(
                    self.get_html_id(appliance.name),
                    self.get_appliance_handler(appliance),
                    appliance,
                    num,
                    event,
                )
                msgs.append(msg)
        return msgs

    def get_appliance_bean(self, appliance):  # noqa
        handler = self.get_appliance_handler(appliance)
        bean = None
        if handler:
            bean = handler.get(appliance)
        return bean

    def get_event_beans(self, appliance):  # noqa
        beans = list()

        appliance_handler = self.get_appliance_handler(appliance)
        for num, event in enumerate(appliance.events):  # noqa
            handler = self.get_event_handler(appliance, event)
            if handler:
                bean = handler.get(event)
                appliance_id = self.get_html_id(appliance.name)
                bean.set_enabled(appliance, event)
                bean.set_id(appliance_id, num)
                bean.set_id_enabled(appliance_id, num)
                bean.set_id_icon(appliance_id, num)
                bean.set_id_label(appliance_id, num)
                bean.set_is_displayed(appliance_handler.is_displayed(appliance, event))
                beans.append(bean)

        beans.reverse()
        return beans

    @staticmethod
    def get_registry_key(appliance, event, get_class=True):  # noqa
        if appliance:
            if get_class:
                return appliance.__class__, event.__class__
            else:
                return appliance.__class__, event
        else:
            if get_class:
                return None, event.__class__
            else:
                return None, event


from ws.handler import (
    index,
    collections,
    collection,
    appliance,
    event,
    websocket,
    history,
    details,
    graphs,
    editor,
    login,
    logout,
)
