from abc import abstractmethod
from typing import ClassVar, Optional
import json

from ws.handler.event.registry import Registry
from ws.i18n import Translator


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

    KLASS: ClassVar[Optional[type]] = None
    APPLIANCE_KLASS: ClassVar[Optional[type]] = None
    TEMPLATE: ClassVar[Optional[str]] = None
    LABEL: ClassVar[Optional[str]] = None

    def __init__(self, home_resources):
        self._home_resources = home_resources
        self._translator = Translator()

    @classmethod
    def with_translator(cls, home_resources, translator):
        h = cls(home_resources)
        h._translator = translator
        return h

    def get_module_str(self):
        # Mirror the normalisation applied by
        # home.event.enumeration.register_class so that bean.module matches
        # the key used in home.event.registry.
        return self.KLASS.__module__.replace(".definition", "").replace(
            "forced.event", "forced"
        )

    def get_class_str(self):
        return self.KLASS.__name__

    @abstractmethod
    def get(self, event): ...

    @abstractmethod
    def post(self, request_data): ...

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
            self.make_msg(
                appliance_id, appliance_handler, appliance, num, event
            ),
            cls=self._home_resources.json_encoder,
        )
        return msg

    def get_description(self, event):
        return "{} {}".format(self.LABEL, event)

    def get_description_for_index(self, event):
        return self._translator(self.get_description(event))

    def get_description_for_history(self, event):
        return self._translator(self.get_description(event))

    def get_icon(self, event):
        return "ti ti-circle-x"
