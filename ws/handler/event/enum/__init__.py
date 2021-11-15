from ws.handler.event import handler


class Bean(handler.Bean):
    def __init__(self, label, module, klass, template, icon, value, choices):
        super(Bean, self).__init__(label, module, klass, template, icon)
        self.value = value
        self.choices = choices


class Handler(handler.Handler):

    YES = "yes"
    NO = "no"

    def get(self, event):
        return Bean(
            self.LABEL,
            self.get_module_str(),
            self.get_class_str(),
            self.TEMPLATE,
            self.get_icon(event),
            self._get_str(event),
            [(e, self._get_str(e)) for e in event.__class__],
        )

    def _get_str(self, e):
        return e

    def _make_msg_label(self, event):
        return self._get_str(event)

    def post(self, request_data):
        value = request_data["value"]
        event = self.KLASS(value)
        return event

    def make_websocket_msg(self, appliance_id, appliance_handler, appliance, id, event):
        return super(Handler, self).make_websocket_msg(
            appliance_id, appliance_handler, appliance, id, event
        )

    def get_description(self, event):
        return "{} {}".format(self.LABEL, self._get_str(event))


from ws.handler.event.enum import (
    appliance,
    clima,
    alarm,
    power,
    holiday,
    sun,
    courtesy,
    sleepiness,
    motion,
    wind,
    rain,
    scene,
    enable,
    presence,
    user,
    elapsed,
    toggle,
)
