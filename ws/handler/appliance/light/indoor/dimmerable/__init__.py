import home
from ws.handler.appliance.light import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.indoor.dimmerable.Appliance
    LABEL_FORCED_SHOW = "In a show"
    LABEL_FORCED_CIRCADIAN_RHYTHM = "Following circadian rhythm"
    LABEL_FORCED_LUX_BALANCING = "Lux balancing"
    ICON_FORCED_SHOW = "fas fa-magic"
    ICON_FORCED_CIRCADIAN_RHYTHM = "fas fa-sync"
    ICON_FORCED_LUX_BALANCING = "fas fa-adjust"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.on.State.VALUE
        ):
            return self.LABEL_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.off.State.VALUE
        ):
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.show.State.VALUE
        ):
            return self.LABEL_FORCED_SHOW
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm.State.VALUE
        ):
            return self.LABEL_FORCED_CIRCADIAN_RHYTHM
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.lux_balance.State.VALUE
        ):
            return self.LABEL_FORCED_LUX_BALANCING

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.on.State.VALUE
        ):
            return self.ICON_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.off.State.VALUE
        ):
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.show.State.VALUE
        ):
            return self.ICON_FORCED_SHOW
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm.State.VALUE
        ):
            return self.ICON_FORCED_CIRCADIAN_RHYTHM
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.lux_balance.State.VALUE
        ):
            return self.ICON_FORCED_LUX_BALANCING

    def is_displayed(self, appliance, event):
        result = False
        if isinstance(
            event,
            (
                home.event.presence.Event,
                home.event.sun.brightness.Event,
                appliance.forced_enum,
            ),
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.on.State.VALUE
            and isinstance(event, home.appliance.light.event.brightness.Event)
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.show.State.VALUE
            and isinstance(
                event,
                (
                    home.event.waveform.Event,
                    home.appliance.light.event.show.period.Event,
                    home.appliance.light.event.show.cycles.Event,
                    home.appliance.light.event.show.ending_brightness.Event,
                    home.appliance.light.event.show.starting_brightness.Event,
                ),
            )
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.lux_balance.State.VALUE
            and isinstance(
                event, home.appliance.light.event.lux_balancing.brightness.Event
            )
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm.State.VALUE
            and isinstance(
                event, home.appliance.light.event.circadian_rhythm.brightness.Event
            )
        ):
            result = True
        return result
