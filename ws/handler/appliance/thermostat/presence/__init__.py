import home
from ws.handler.appliance.light import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.thermostat.presence.Appliance
    LABEL_KEEP = "Keeping"
    LABEL_FORCED_KEEP = "Forced keeping"
    ICON_ON = "fas fa-burn"
    ICON_OFF = "fas fa-power-off"
    ICON_KEEP = "fas fa-water"
    ICON_FORCED_KEEP = "far fa-hand-point-right"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.on.State.VALUE
        ):
            return self.LABEL_ON
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.off.State.VALUE
        ):
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.keep.State.VALUE
        ):
            return self.LABEL_KEEP
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.forced.off.State.VALUE
        ):
            return self.LABEL_FORCED_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.forced.keep.State.VALUE
        ):
            return self.LABEL_FORCED_KEEP

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.on.State.VALUE
        ):
            return self.ICON_ON
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.off.State.VALUE
        ):
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.keep.State.VALUE
        ):
            return self.ICON_KEEP
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.forced.off.State.VALUE
        ):
            return self.ICON_FORCED_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.thermostat.presence.state.forced.keep.State.VALUE
        ):
            return self.ICON_FORCED_KEEP
