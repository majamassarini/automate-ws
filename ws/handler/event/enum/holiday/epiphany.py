import home

from ws.handler.event.enum.holiday import christmas as definition


class Handler(definition.Handler):

    KLASS = home.event.holiday.epiphany.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Epiphany"

    def _get_str(self, e):
        if e == home.event.holiday.epiphany.Event.Day:
            return self.DAY
        elif e == home.event.holiday.epiphany.Event.Eve:
            return self.EVE
        elif e == home.event.holiday.epiphany.Event.Over:
            return self.OVER
        return e

    def get_icon(self, e):
        if e == home.event.holiday.epiphany.Event.Day:
            return "fas fa-hat-wizard"
        elif e == home.event.holiday.epiphany.Event.Eve:
            return "fas fa-broom"
        elif e == home.event.holiday.epiphany.Event.Over:
            return "far fa-calendar-times"
        return e
