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
            return "fas fa-hot-tub"
        elif e == home.event.holiday.san_silvester.Event.Eve:
            return "fas fa-glass-cheers"
        elif e == home.event.holiday.san_silvester.Event.Over:
            return "far fa-calendar-times"
        return e
