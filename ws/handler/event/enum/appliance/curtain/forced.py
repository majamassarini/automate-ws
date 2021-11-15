import home

from ws.handler.event.enum import forced


class Handler(forced.Handler):

    KLASS = home.appliance.curtain.event.forced.event.Event
    TEMPLATE = "event/forced_enum.html"
    FORCED_OPENED = "Forced opened"
    FORCED_CLOSED = "Forced closed"

    def _get_str(self, e):
        if e == home.appliance.curtain.event.forced.event.Event.Opened:
            return self.OPENED
        elif e == home.appliance.curtain.event.forced.event.Event.Closed:
            return self.CLOSED
        elif e == home.appliance.curtain.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.appliance.curtain.event.forced.event.Event.Opened:
            return self.FORCED_OPENED
        elif e == home.appliance.curtain.event.forced.event.Event.Closed:
            return self.FORCED_CLOSED
        elif e == home.appliance.curtain.event.forced.event.Event.Not:
            return self.FORCED_NOT
        return e

    def get_icon(self, e):
        if e == home.appliance.curtain.event.forced.event.Event.Opened:
            return self.ICON_UP
        elif e == home.appliance.curtain.event.forced.event.Event.Closed:
            return self.ICON_DOWN
        elif e == home.appliance.curtain.event.forced.event.Event.Not:
            return self.ICON_OK
        return e
