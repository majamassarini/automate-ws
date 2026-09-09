import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.alarm.armed.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Is alarm armed?"
    ARMED = "Alarm is armed"
    UNARMED = "Alarm is not armed"

    def _get_str(self, e):
        if e == home.event.alarm.armed.Event.On:
            return self.YES
        elif e == home.event.alarm.armed.Event.Off:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.event.alarm.armed.Event.On:
            return self.ARMED
        elif e == home.event.alarm.armed.Event.Off:
            return self.UNARMED

    def get_icon(self, e):
        if e == home.event.alarm.armed.Event.On:
            return "ti ti-bell-ringing"
        elif e == home.event.alarm.armed.Event.Off:
            return "ti ti-bell-off"
        return e
