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
            return "ti ti-solar-panel"
        elif e == home.event.power.production.Event.Low:
            return "ti ti-solar-panel"
        elif e == home.event.power.production.Event.High:
            return "ti ti-solar-panel"
        return e


from ws.handler.event.enum.power.production import duration
