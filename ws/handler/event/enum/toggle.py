import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.toggle.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Toggling"
    ENABLED = "enabled"
    DISABLED = "disabled"

    def _get_str(self, e):
        if e == home.event.toggle.Event.On:
            return self.ENABLED
        elif e == home.event.toggle.Event.Off:
            return self.DISABLED
        return e

    def get_icon(self, e):
        if e == home.event.toggle.Event.On:
            return "ti ti-toggle-right"
        elif e == home.event.toggle.Event.Off:
            return "ti ti-toggle-left"
        return e
