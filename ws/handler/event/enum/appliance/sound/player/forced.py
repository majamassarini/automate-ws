import home

from ws.handler.event.enum.appliance.light.indoor.dimmerable import forced


class Handler(forced.Handler):

    KLASS = home.appliance.sound.player.event.forced.event.Event
    TEMPLATE = "event/forced_enum.html"
    ICON_FORCED_ON = "fas fa-play-circle"
    ICON_OFF = "far fa-play-circle"

    def _get_str(self, e):
        if e == home.appliance.sound.player.event.forced.event.Event.On:
            return self.ON
        elif e == home.appliance.sound.player.event.forced.event.Event.Off:
            return self.OFF
        elif e == home.appliance.sound.player.event.forced.event.Event.CircadianRhythm:
            return self.CIRCADIAN_RHYTHM
        elif e == home.appliance.sound.player.event.forced.event.Event.Not:
            return self.NO
        return e

    def get_description(self, e):
        if e == home.appliance.sound.player.event.forced.event.Event.On:
            return self.FORCED_ON
        elif e == home.appliance.sound.player.event.forced.event.Event.Off:
            return self.FORCED_OFF
        elif e == home.appliance.sound.player.event.forced.event.Event.CircadianRhythm:
            return self.FORCED_CIRCADIAN_RHYTHM
        elif e == home.appliance.sound.player.event.forced.event.Event.Not:
            return self.NO
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
            return self.CIRCADIAN_RHYTHM
        elif e == home.appliance.light.indoor.dimmerable.event.forced.event.Event.Not:
            return self.ICON_OK
        return e
