import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.presence.Event
    APPLIANCE_KLASS = home.appliance.light.zone.Appliance
    TEMPLATE = "event/enum.html"
    LABEL = "Is someone in here?"
    LABEL1 = "Someone is in here"
    LABEL2 = "No one is in here"

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
            return "fas fa-sign-in-alt"
        elif e == home.event.presence.Event.Off:
            return "fas fa-sign-out-alt"
        return e
