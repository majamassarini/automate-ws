import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.alarm.triggered.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Is alarm triggered?"
    TRIGGERED = "Alarm is triggered"
    UNTRIGGERED = "Alarm is not triggered"

    def _get_str(self, e):
        if e == home.event.alarm.triggered.Event.On:
            return self.YES
        elif e == home.event.alarm.triggered.Event.Off:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.event.alarm.triggered.Event.On:
            return self.TRIGGERED
        elif e == home.event.alarm.triggered.Event.Off:
            return self.UNTRIGGERED

    def get_icon(self, e):
        if e == home.event.alarm.triggered.Event.On:
            return "fas fa-eye"
        elif e == home.event.alarm.triggered.Event.Off:
            return "far fa-eye"
        return e
