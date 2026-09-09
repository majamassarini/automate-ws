import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.sun.twilight.civil.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Sun is"

    def _get_str(self, e):
        if e == home.event.sun.twilight.civil.Event.Sunset:
            return "set (civil twilight)"
        elif e == home.event.sun.twilight.civil.Event.Sunrise:
            return "rised (civil twilight)"
        return e

    def get_icon(self, e):
        if e == home.event.sun.twilight.civil.Event.Sunrise:
            return "ti ti-sun-low"
        elif e == home.event.sun.twilight.civil.Event.Sunset:
            return "ti ti-moon-stars"
        return e
