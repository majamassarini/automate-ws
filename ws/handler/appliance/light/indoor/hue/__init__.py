import home
from ws.handler.appliance.light.indoor.dimmerable import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.indoor.hue.Appliance

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.on.State.VALUE
        ):
            return self.LABEL_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.off.State.VALUE
        ):
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.show.State.VALUE
        ):
            return self.LABEL_FORCED_SHOW
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.circadian_rhythm.State.VALUE
        ):
            return self.LABEL_FORCED_CIRCADIAN_RHYTHM
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.lux_balance.State.VALUE
        ):
            return self.LABEL_FORCED_LUX_BALANCING

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.on.State.VALUE
        ):
            return self.ICON_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.off.State.VALUE
        ):
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.show.State.VALUE
        ):
            return self.ICON_FORCED_SHOW
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.circadian_rhythm.State.VALUE
        ):
            return self.ICON_FORCED_CIRCADIAN_RHYTHM
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.lux_balance.State.VALUE
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
            == home.appliance.light.indoor.hue.state.forced.on.State.VALUE
            and isinstance(event, home.appliance.light.event.brightness.Event)
        ):
            result = True
        elif (
            appliance.state.VALUE
            == home.appliance.light.indoor.hue.state.forced.show.State.VALUE
            and isinstance(
                event,
                (
                    home.event.waveform.Event,
                    home.appliance.light.event.show.period.Event,
                    home.appliance.light.event.show.cycles.Event,
                    home.appliance.light.event.show.ending_brightness.Event,
                    home.appliance.light.event.show.ending_hue.Event,
                    home.appliance.light.event.show.starting_brightness.Event,
                    home.appliance.light.event.show.starting_hue.Event,
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
        elif appliance.state.VALUE == home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm.State.VALUE and isinstance(
            event,
            (
                home.appliance.light.event.circadian_rhythm.brightness.Event,
                home.appliance.light.event.circadian_rhythm.hue.Event,
                home.appliance.light.event.circadian_rhythm.temperature.Event,
                home.appliance.light.event.circadian_rhythm.saturation.Event,
            ),
        ):
            result = True
        return result
