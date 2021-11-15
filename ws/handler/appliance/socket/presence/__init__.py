import home
from ws.handler.appliance.socket.energy_guard import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.socket.presence.Appliance

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.socket.presence.state.off.State.VALUE
        ):
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.socket.presence.state.off.State.VALUE
        ):
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON


from ws.handler.appliance.socket.presence import christmas
