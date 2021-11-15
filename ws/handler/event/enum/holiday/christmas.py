import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.holiday.christmas.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Christmas"
    DAY = "day"
    EVE = "eve"
    TIME = "time"
    OVER = "is over"

    def _get_str(self, e):
        if e == home.event.holiday.christmas.Event.Day:
            return self.DAY
        elif e == home.event.holiday.christmas.Event.Eve:
            return self.EVE
        elif e == home.event.holiday.christmas.Event.Time:
            return self.TIME
        elif e == home.event.holiday.christmas.Event.Over:
            return self.OVER
        return e

    def get_icon(self, e):
        if e == home.event.holiday.christmas.Event.Day:
            return "fas fa-gifts"
        elif e == home.event.holiday.christmas.Event.Eve:
            return "fas fa-holly-berry"
        elif e == home.event.holiday.christmas.Event.Time:
            return "far fa-calendar-check"
        elif e == home.event.holiday.christmas.Event.Over:
            return "far fa-calendar-times"
        return e
