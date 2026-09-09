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
            return "ti ti-bolt-off"
        elif e == home.event.power.consumption.Event.Low:
            return "ti ti-bolt"
        elif e == home.event.power.consumption.Event.High:
            return "ti ti-bolt"
        return e


from ws.handler.event.enum.power.consumption import duration
