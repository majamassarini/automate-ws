import home
from ws.handler.appliance.light import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.socket.energy_guard.Appliance
    LABEL_ON = "On"
    LABEL_OFF = "Off"
    LABEL_DETACHABLE = "Detachable"
    LABEL_FORCED_ON = "Forced On"
    LABEL_FORCED_OFF = "Forced Off"
    ICON_ON = "fas fa-plug"
    ICON_OFF = "fas fa-power-off"
    ICON_FORCED_ON = "far fa-hand-point-up"
    ICON_FORCED_OFF = "far fa-hand-point-down"
    ICON_DETACHABLE = "fas exclamation-triangle"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.off.State.VALUE
        ):
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.on.State.VALUE
        ):
            return self.LABEL_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.detachable.State.VALUE
        ):
            return self.LABEL_DETACHABLE
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.forced.off.State.VALUE
        ):
            return self.LABEL_FORCED_OFF

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.off.State.VALUE
        ):
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.on.State.VALUE
        ):
            return self.ICON_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.detachable.State.VALUE
        ):
            return self.ICON_DETACHABLE
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.energy_guard.state.forced.off.State.VALUE
        ):
            return self.ICON_FORCED_OFF
