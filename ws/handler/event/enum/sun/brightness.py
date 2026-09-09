import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.sun.brightness.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Sun brightness is"

    def _get_str(self, e):
        if e == home.event.sun.brightness.Event.Bright:
            return "high"
        elif e == home.event.sun.brightness.Event.Dark:
            return "low"
        elif e == home.event.sun.brightness.Event.DeepDark:
            return "very low"
        return e

    def get_icon(self, e):
        if e == home.event.sun.brightness.Event.Bright:
            return "ti ti-sun-high"
        elif e == home.event.sun.brightness.Event.Dark:
            return "ti ti-cloud"
        elif e == home.event.sun.brightness.Event.DeepDark:
            return "ti ti-cloud"
        return e
