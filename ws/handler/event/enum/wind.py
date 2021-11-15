import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.wind.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Wind is"

    def _get_str(self, e):
        if e == home.event.wind.Event.Strong:
            return "strong"
        elif e == home.event.wind.Event.Weak:
            return "weak"
        return e

    def get_icon(self, e):
        if e == home.event.wind.Event.Strong:
            return "fas fa-wind"
        elif e == home.event.wind.Event.Weak:
            return "fas fa-window-minimize"
        return e
