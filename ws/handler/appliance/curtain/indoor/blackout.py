import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.curtain.indoor.blackout.Appliance
    LABEL_OPENED = "Opened"
    LABEL_FORCED_OPENED = "Forced Opened"
    LABEL_FORCED_CLOSED = "Forced Closed"
    LABEL_CLOSED = "Closed"
    ICON_OPENED = "fas fa-door-open"
    ICON_CLOSED = "fas fa-door-closed"
    ICON_FORCED_OPENED = "far fa-hand-point-up"
    ICON_FORCED_CLOSED = "far fa-hand-point-down"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.curtain.indoor.blackout.state.opened.State.VALUE
        ):
            return self.LABEL_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.indoor.blackout.state.forced.opened.State.VALUE
        ):
            return self.LABEL_FORCED_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.indoor.blackout.state.forced.closed.State.VALUE
        ):
            return self.LABEL_FORCED_CLOSED
        else:
            return self.LABEL_CLOSED

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.curtain.indoor.blackout.state.opened.State.VALUE
        ):
            return self.ICON_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.indoor.blackout.state.forced.opened.State.VALUE
        ):
            return self.ICON_FORCED_OPENED
        elif (
            appliance.state.VALUE
            == home.appliance.curtain.indoor.blackout.state.forced.closed.State.VALUE
        ):
            return self.ICON_FORCED_CLOSED
        else:
            return self.ICON_CLOSED
