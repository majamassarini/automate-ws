import home

from ws.handler.event.enum.appliance.light import forced


class Handler(forced.Handler):

    KLASS = home.appliance.light.indoor.dimmerable.event.forced.event.Event
    TEMPLATE = "event/forced_enum.html"
    CIRCADIAN_RHYTHM = "circadian rhythm"
    LUX_BALANCING = "lux balancing"
    SHOW = "show"
    FORCED_CIRCADIAN_RHYTHM = "Forced circadian rhytm"
    FORCED_LUX_BALANCING = "Forced lux balancing"
    FORCED_SHOW = "Forced show"
    ICON_CIRCADIAN_RHYTHM = "fas fa-sync"
    ICON_LUX_BALANCING = "fas fa-adjust"
    ICON_SHOW = "fas fa-magic"

    def _get_str(self, e):
        if e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.On:
            return self.ON
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Off:
            return self.OFF
        elif (
            e
            == home.appliance.light.indoor.dimmerable.event.forced.event.Event.CircadianRhythm
        ):
            return self.CIRCADIAN_RHYTHM
        elif (
            e
            == home.appliance.light.indoor.dimmerable.event.forced.event.Event.LuxBalance
        ):
            return self.LUX_BALANCING
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Show:
            return self.SHOW
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.On:
            return self.FORCED_ON
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Off:
            return self.FORCED_OFF
        elif (
            e
            == home.appliance.light.indoor.dimmerable.event.forced.event.Event.CircadianRhythm
        ):
            return self.FORCED_CIRCADIAN_RHYTHM
        elif (
            e
            == home.appliance.light.indoor.dimmerable.event.forced.event.Event.LuxBalance
        ):
            return self.LUX_BALANCING
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Show:
            return self.FORCED_SHOW
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Not:
            return self.FORCED_NOT
        return e

    def get_icon(self, e):
        if e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.On:
            return self.ICON_UP
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Off:
            return self.ICON_DOWN
        elif (
            e
            == home.appliance.light.indoor.dimmerable.event.forced.event.Event.CircadianRhythm
        ):
            return self.ICON_CIRCADIAN_RHYTHM
        elif (
            e
            == home.appliance.light.indoor.dimmerable.event.forced.event.Event.LuxBalance
        ):
            return self.ICON_LUX_BALANCING
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Show:
            return self.ICON_SHOW
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Not:
            return self.ICON_OK
        return e
