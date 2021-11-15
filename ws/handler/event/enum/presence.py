import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.presence.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Is someone at home?"
    LABEL1 = "Someone is in home"
    LABEL2 = "No one is in home"

    def _get_str(self, e):
        if e == home.event.presence.Event.On:
            return self.YES
        elif e == home.event.presence.Event.Off:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.event.presence.Event.On:
            return self.LABEL1
        elif e == home.event.presence.Event.Off:
            return self.LABEL2

    def get_icon(self, e):
        if e == home.event.presence.Event.On:
            return "fas fa-house-user"
        elif e == home.event.presence.Event.Off:
            return "fas fa-house-damage"
        return e
