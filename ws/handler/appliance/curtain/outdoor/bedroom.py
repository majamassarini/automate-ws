import home
from ws.handler.appliance.curtain.indoor.blackout import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.curtain.outdoor.bedroom.Appliance

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.curtain.outdoor.bedroom.state.opened.State.VALUE
        ):
            return self.LABEL_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.outdoor.bedroom.state.forced.opened.State.VALUE
        ):
            return self.LABEL_FORCED_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.outdoor.bedroom.state.forced.closed.State.VALUE
        ):
            return self.LABEL_FORCED_CLOSED
        else:
            return self.LABEL_CLOSED

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.curtain.outdoor.bedroom.state.opened.State.VALUE
        ):
            return self.ICON_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.outdoor.bedroom.state.forced.opened.State.VALUE
        ):
            return self.ICON_FORCED_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.outdoor.bedroom.state.forced.closed.State.VALUE
        ):
            return self.ICON_FORCED_CLOSED
        else:
            return self.ICON_CLOSED
