import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.elapsed.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Elapsed"
    ICON_ELAPSED = "fas fa-stop-circle"
    ICON_NOT_ELAPSED = "far fa-stop-circle"

    def _get_str(self, e):
        if e == home.event.elapsed.Event.On:
            return self.YES
        elif e == home.event.elapsed.Event.Off:
            return self.NO
        return e

    def get_icon(self, e):
        if e == home.event.elapsed.Event.On:
            return self.ICON_ELAPSED
        elif e == home.event.elapsed.Event.Off:
            return self.ICON_NOT_ELAPSED
        return e
