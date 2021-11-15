import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.motion.Event
    TEMPLATE = "event/enum.html"
    MOTION = "Motion detected"
    NOMOTION = "No motion"
    LABEL = "Is motion detected?"

    def _get_str(self, e):
        if e == home.event.motion.Event.Spotted:
            return self.YES
        elif e == home.event.motion.Event.Missed:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.event.motion.Event.Spotted:
            return self.MOTION
        elif e == home.event.motion.Event.Missed:
            return self.NOMOTION

    def get_icon(self, e):
        if e == home.event.motion.Event.Spotted:
            return "fas fa-eye"
        elif e == home.event.motion.Event.Missed:
            return "far fa-eye"
        return e
