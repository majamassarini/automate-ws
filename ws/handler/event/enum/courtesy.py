import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.courtesy.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Is coming someone?"
    COMING = "Someone is coming"
    GOING = "No one is coming"

    def _get_str(self, e):
        if e == home.event.courtesy.Event.On:
            return self.YES
        elif e == home.event.courtesy.Event.Off:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.event.courtesy.Event.On:
            return self.COMING
        elif e == home.event.courtesy.Event.Off:
            return self.GOING

    def get_icon(self, e):
        if e == home.event.courtesy.Event.On:
            return "fas fa-walking"
        elif e == home.event.courtesy.Event.Off:
            return "fas fa-shoe-prints"
        return e
