import home
from ws.handler.appliance.socket.presence import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.socket.presence.christmas.Appliance

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.off.State.VALUE
        ):
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.on.State.VALUE
        ):
            return self.LABEL_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.forced.off.State.VALUE
        ):
            return self.LABEL_FORCED_OFF

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.off.State.VALUE
        ):
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.on.State.VALUE
        ):
            return self.ICON_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.socket.presence.christmas.state.forced.off.State.VALUE
        ):
            return self.ICON_FORCED_OFF
