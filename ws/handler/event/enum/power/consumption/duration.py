import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.power.consumption.duration.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Power consumption"

    def _get_str(self, e):
        if e == home.event.power.consumption.duration.Event.Short:
            return "since short time"
        elif e == home.event.power.consumption.duration.Event.Long:
            return "since long time"
        return e

    def get_icon(self, e):
        if e == home.event.power.consumption.duration.Event.Short:
            return "fas fa-hourglass-start"
        elif e == home.event.power.consumption.duration.Event.Long:
            return "fas fa-hourglass-end"
        return e
