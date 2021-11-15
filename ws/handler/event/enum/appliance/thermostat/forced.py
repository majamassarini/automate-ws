import home

from ws.handler.event.enum.appliance.light import forced


class Handler(forced.Handler):

    KLASS = home.appliance.thermostat.presence.event.forced.event.Event
    TEMPLATE = "event/forced_enum.html"
    KEEPING = "keeping"
    FORCED_KEEPING = "Forced keeping"
    ICON_KEEPING = "fas fa-sort"

    def _get_str(self, e):
        if e == home.appliance.thermostat.presence.event.forced.event.Event.On:
            return self.ON
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Off:
            return self.OFF
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Keep:
            return self.KEEPING
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.appliance.thermostat.presence.event.forced.event.Event.On:
            return self.FORCED_ON
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Off:
            return self.FORCED_OFF
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Keep:
            return self.FORCED_KEEPING
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Not:
            return self.FORCED_NOT
        return e

    def get_icon(self, e):
        if e == home.appliance.thermostat.presence.event.forced.event.Event.On:
            return self.ICON_UP
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Off:
            return self.ICON_DOWN
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Keep:
            return self.ICON_KEEPING
        elif e == home.appliance.thermostat.presence.event.forced.event.Event.Not:
            return self.ICON_OK
        return e
