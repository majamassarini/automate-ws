import home

from ws.handler.event.enum.appliance.light.indoor.dimmerable import forced


class Handler(forced.Handler):

    KLASS = home.appliance.sprinkler.event.forced.event.Event
    PARTIALLY_ON = "Partially On"
    FORCED_PARTIALLY_ON = "Forced Partially On"
    TEMPLATE = "event/forced_enum.html"
    ICON_FORCED_ON = "fas fa-play-circle"
    ICON_OFF = "far fa-play-circle"
    ICON_PARTIALLY_ON = forced.Handler.ICON_CIRCADIAN_RHYTHM

    def _get_str(self, e):
        if e == home.appliance.sprinkler.event.forced.event.Event.On:
            return self.ON
        elif e == home.appliance.sprinkler.event.forced.event.Event.Off:
            return self.OFF
        elif e == home.appliance.sprinkler.event.forced.event.Event.PartiallyOn:
            return self.PARTIALLY_ON
        elif e == home.appliance.sprinkler.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.appliance.sprinkler.event.forced.event.Event.On:
            return self.FORCED_ON
        elif e == home.appliance.sprinkler.event.forced.event.Event.Off:
            return self.FORCED_OFF
        elif e == home.appliance.sprinkler.event.forced.event.Event.PartiallyOn:
            return self.FORCED_PARTIALLY_ON
        elif e == home.appliance.sprinkler.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_icon(self, e):
        if e == home.appliance.sprinkler.event.forced.event.Event.On:
            return self.ICON_UP
        elif e == home.appliance.sprinkler.event.forced.event.Event.Off:
            return self.ICON_DOWN
        elif e == home.appliance.sprinkler.event.forced.event.Event.PartiallyOn:
            return self.ICON_PARTIALLY_ON
        elif e == home.appliance.sprinkler.event.forced.event.Event.Not:
            return self.ICON_OK
        return e
