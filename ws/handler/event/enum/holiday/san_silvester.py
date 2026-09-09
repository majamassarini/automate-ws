import home

from ws.handler.event.enum.holiday import christmas as definition


class Handler(definition.Handler):

    KLASS = home.event.holiday.san_silvester.Event
    TEMPLATE = "event/enum.html"
    LABEL = "San Silvester"

    def _get_str(self, e):
        if e == home.event.holiday.san_silvester.Event.Day:
            return self.DAY
        elif e == home.event.holiday.san_silvester.Event.Eve:
            return self.EVE
        elif e == home.event.holiday.san_silvester.Event.Over:
            return self.OVER
        return e

    def get_icon(self, e):
        if e == home.event.holiday.san_silvester.Event.Day:
            return "ti ti-balloons"
        elif e == home.event.holiday.san_silvester.Event.Eve:
            return "ti ti-glass-champagne"
        elif e == home.event.holiday.san_silvester.Event.Over:
            return "ti ti-calendar-x"
        return e
