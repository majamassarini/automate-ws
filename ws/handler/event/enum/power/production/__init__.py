import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.power.production.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Power production is"

    def _get_str(self, e):
        if e == home.event.power.production.Event.No:
            return "off"
        elif e == home.event.power.production.Event.Low:
            return "low"
        elif e == home.event.power.production.Event.High:
            return "high"
        return e

    def get_icon(self, e):
        if e == home.event.power.production.Event.No:
            return "fas fa-battery-empty"
        elif e == home.event.power.production.Event.Low:
            return "fas fa-battery-quarter"
        elif e == home.event.power.production.Event.High:
            return "fas fa-battery-full"
        return e


from ws.handler.event.enum.power.production import duration
