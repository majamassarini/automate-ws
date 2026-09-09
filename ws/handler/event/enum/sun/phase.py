import home

from ws.handler.event.enum.sun import twilight_civil


class Handler(twilight_civil.Handler):

    KLASS = home.event.sun.phase.Event

    def _get_str(self, e):
        if e == home.event.sun.phase.Event.Sunset:
            return "set"
        elif e == home.event.sun.phase.Event.Sunrise:
            return "rised"
        return e

    def get_icon(self, e):
        if e == home.event.sun.phase.Event.Sunrise:
            return "ti ti-sunrise"
        elif e == home.event.sun.phase.Event.Sunset:
            return "ti ti-sunset"
        return e
