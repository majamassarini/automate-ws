import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.sun.hit.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Sun is"

    def _get_str(self, e):
        if e == home.event.sun.hit.Event.Sunleft:
            return "gone"
        elif e == home.event.sun.hit.Event.Sunhit:
            return "over"
        return e

    def get_icon(self, e):
        if e == home.event.sun.hit.Event.Sunhit:
            return "fas fa-square"
        elif e == home.event.sun.hit.Event.Sunleft:
            return "far fa-square"
        return e
