import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.enable.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Detach logic is"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def _get_str(self, e):
        if e == home.event.enable.Event.On:
            return self.ENABLED
        elif e == home.event.enable.Event.Off:
            return self.DISABLED
        return e

    def get_icon(self, e):
        if e == home.event.enable.Event.On:
            return "ti ti-toggle-right"
        elif e == home.event.enable.Event.Off:
            return "ti ti-toggle-left"
        return e
