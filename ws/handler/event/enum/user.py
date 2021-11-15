import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.user.Event
    TEMPLATE = "event/enum.html"
    LABEL = "User"
    LABEL_A = "A"
    LABEL_B = "B"
    LABEL_C = "C"

    def _get_str(self, e):
        if e == home.event.user.Event.A:
            return "A"
        elif e == home.event.user.Event.B:
            return "B"
        elif e == home.event.user.Event.C:
            return "C"
        return e

    def get_icon(self, e):
        return e
