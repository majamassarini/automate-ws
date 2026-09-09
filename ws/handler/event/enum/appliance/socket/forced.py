import home

from ws.handler.event.enum.appliance.light import forced


class Handler(forced.Handler):

    KLASS = home.appliance.socket.event.forced.Event
    TEMPLATE = "event/forced_enum.html"

    def _get_str(self, e):
        if e == home.appliance.socket.event.forced.event.Event.On:
            return self.ON
        elif e == home.appliance.socket.event.forced.event.Event.Off:
            return self.OFF
        elif e == home.appliance.socket.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.appliance.socket.event.forced.event.Event.On:
            return self.FORCED_ON
        elif e == home.appliance.socket.event.forced.event.Event.Off:
            return self.FORCED_OFF
        elif e == home.appliance.socket.event.forced.event.Event.Not:
            return self.FORCED_NOT
        return e

    def get_icon(self, e):
        if e == home.appliance.socket.event.forced.event.Event.On:
            return "ti ti-plug-connected"
        elif e == home.appliance.socket.event.forced.event.Event.Off:
            return "ti ti-plug-x"
        elif e == home.appliance.socket.event.forced.event.Event.Not:
            return self.ICON_OK
        return e
