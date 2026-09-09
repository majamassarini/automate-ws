import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.sleepiness.Event
    TEMPLATE = "event/enum.html"
    LABEL = "User is"

    def _get_str(self, e):
        if e == home.event.sleepiness.Event.Asleep:
            return "asleep"
        elif e == home.event.sleepiness.Event.Awake:
            return "awake"
        elif e == home.event.sleepiness.Event.Sleepy:
            return "sleepy"
        return e

    def get_icon(self, e):
        if e == home.event.sleepiness.Event.Asleep:
            return "ti ti-zzz"
        elif e == home.event.sleepiness.Event.Awake:
            return "ti ti-coffee"
        elif e == home.event.sleepiness.Event.Sleepy:
            return "ti ti-armchair"
        return e
