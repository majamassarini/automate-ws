import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.rain.in_the_past.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Has it rained?"
    HAS_RAINED = "Has rained"
    HAS_NOT_RAINED = "Has not rained"

    def _get_str(self, e):
        if e == home.event.rain.in_the_past.Event.Off:
            return self.NO
        else:
            return self.YES

    def get_description(self, e):
        if e == home.event.rain.in_the_past.Event.Off:
            return self.HAS_NOT_RAINED
        else:
            return self.HAS_RAINED

    def get_icon(self, e):
        if e == home.event.rain.in_the_past.Event.Off:
            return "fas fa-tint-slash"
        else:
            return "fas fa-tint"
