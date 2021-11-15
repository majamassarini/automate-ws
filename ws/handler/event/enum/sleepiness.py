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
            return "fas fa-bed"
        elif e == home.event.sleepiness.Event.Awake:
            return "fas fa-business-time"
        elif e == home.event.sleepiness.Event.Sleepy:
            return "fas fa-couch"
        return e
