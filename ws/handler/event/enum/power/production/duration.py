import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.power.production.duration.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Power production"

    def _get_str(self, e):
        if e == home.event.power.production.duration.Event.Short:
            return "since short time"
        elif e == home.event.power.production.duration.Event.Long:
            return "since long time"
        return e

    def get_icon(self, e):
        if e == home.event.power.production.duration.Event.Short:
            return "ti ti-hourglass-low"
        elif e == home.event.power.production.duration.Event.Long:
            return "ti ti-hourglass-high"
        return e
