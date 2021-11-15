import json
import home
from ws.handler import Handler as Parent
from ws.handler.appliance.registry import Registry


class Bean:

    ID = "{}"
    ID_ICON = "{}-icon"
    ID_LABEL = "{}-label"

    def __init__(self, module, klass, template, label, icon):
        self.module = module
        self.klass = klass
        self.template = template
        self.label = label
        self.icon = icon
        self.id = None
        self.id_icon = None
        self.id_label = None

    def set_id(self, appliance_id):
        self.id = self.ID.format(appliance_id)

    def set_id_icon(self, appliance_id):
        self.id_icon = self.ID_ICON.format(appliance_id)

    def set_id_label(self, appliance_id):
        self.id_label = self.ID_LABEL.format(appliance_id)


class Handler(Parent, metaclass=Registry):

    KLASS = home.appliance.Appliance
    TEMPLATE = "appliance.html"

    def __init__(self, home_resources):
        self._home_resources = home_resources

    def get_module_str(self):
        return self.KLASS.__module__

    def get_class_str(self):
        return self.KLASS.__name__

    def get(self, appliance):
        id = self.get_html_id(appliance.name)
        bean = Bean(
            self.get_module_str(),
            self.get_class_str(),
            self.get_template(appliance),
            self.get_label(appliance),
            self.get_icon(appliance),
        )
        bean.set_id(id)
        bean.set_id_icon(id)
        bean.set_id_label(id)
        return bean

    def make_msg(self, appliance):
        id = self.get_html_id(appliance.name)
        return {
            "id": Bean.ID.format(id),
            "id_icon": Bean.ID_ICON.format(id),
            "id_label": Bean.ID_LABEL.format(id),
            "label": self.get_label(appliance),
            "icon": self.get_icon(appliance),
        }

    def make_websocket_msg(self, appliance):
        msg = json.dumps(
            self.make_msg(appliance), cls=self._home_resources.json_encoder
        )
        return msg

    def get_template(self, appliance):
        return self.TEMPLATE

    def get_label(self, appliance):
        return appliance.state.compute()

    def get_icon(self, appliance):
        return "fas fa-times-circle"

    def is_displayed(self, appliance, event):
        return True
