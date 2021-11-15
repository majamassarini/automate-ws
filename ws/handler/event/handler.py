from abc import abstractmethod
import json

from ws.handler.event.registry import Registry


class Bean:
    def __init__(self, label, module, klass, template, icon):
        self.label = label
        self.module = module
        self.klass = klass
        self.displayed = True
        self.template = template
        self.icon = icon
        self.enabled = True
        self.id = None
        self.id_icon = None
        self.id_enabled = None
        self.id_label = None

    def set_id(self, appliance_id, num):
        self.id = "{}-{}".format(appliance_id, num)

    def set_id_enabled(self, appliance_id, num):
        self.id_enabled = "{}-{}-enabled".format(appliance_id, num)

    def set_id_icon(self, appliance_id, num):
        self.id_icon = "{}-{}-icon".format(appliance_id, num)

    def set_id_label(self, appliance_id, num):
        self.id_label = "{}-{}-label".format(appliance_id, num)

    def set_enabled(self, appliance, event):
        self.enabled = appliance.is_enabled(event)

    def set_is_displayed(self, value):
        self.displayed = value


class Handler(metaclass=Registry):

    KLASS = None
    APPLIANCE_KLASS = None
    TEMPLATE = None
    LABEL = None

    def __init__(self, home_resources):
        self._home_resources = home_resources

    def get_module_str(self):
        return self.KLASS.__module__

    def get_class_str(self):
        return self.KLASS.__name__

    @abstractmethod
    def get(self, event):
        ...

    @abstractmethod
    def post(self, request_data):
        ...

    def _make_msg_label(self, event):
        return event

    def make_msg(self, appliance_id, appliance_handler, appliance, num, event):
        return {
            "id": "{}-{}".format(appliance_id, num),
            "id_enabled": "{}-{}-enabled".format(appliance_id, num),
            "id_icon": "{}-{}-icon".format(appliance_id, num),
            "id_label": "{}-{}-label".format(appliance_id, num),
            "value": event,
            "description": self.get_description(event),
            "label": self._make_msg_label(event),
            "enabled": appliance.is_enabled(event),
            "displayed": appliance_handler.is_displayed(appliance, event),
            "icon": self.get_icon(event),
        }

    def make_websocket_msg(
        self, appliance_id, appliance_handler, appliance, num, event
    ):
        msg = json.dumps(
            self.make_msg(appliance_id, appliance_handler, appliance, num, event),
            cls=self._home_resources.json_encoder,
        )
        return msg

    def get_description(self, event):
        return "{} {}".format(self.LABEL, event)

    def get_description_for_index(self, event):
        return self.get_description(event)

    def get_description_for_history(self, event):
        return self.get_description(event)

    def get_icon(self, event):
        return "fas fa-times-circle"
