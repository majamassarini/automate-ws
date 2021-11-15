import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.power.consumption.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Power consumption is"

    def _get_str(self, e):
        if e == home.event.power.consumption.Event.No:
            return "off"
        elif e == home.event.power.consumption.Event.Low:
            return "low"
        elif e == home.event.power.consumption.Event.High:
            return "high"
        return e

    def get_icon(self, e):
        if e == home.event.power.consumption.Event.No:
            return "fas fa-battery-full"
        elif e == home.event.power.consumption.Event.Low:
            return "fas fa-battery-three-quarters"
        elif e == home.event.power.consumption.Event.High:
            return "fas fa-battery-empty"
        return e


from ws.handler.event.enum.power.consumption import duration
