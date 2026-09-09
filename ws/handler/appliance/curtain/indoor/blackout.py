import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.curtain.indoor.blackout.Appliance
    LABEL_OPENED = "Opened"
    LABEL_FORCED_OPENED = "Forced Opened"
    LABEL_FORCED_CLOSED = "Forced Closed"
    LABEL_CLOSED = "Closed"
    ICON_OPENED = "ti ti-fence"
    ICON_CLOSED = "ti ti-fence-off"
    ICON_FORCED_OPENED = "ti ti-arrow-big-up"
    ICON_FORCED_CLOSED = "ti ti-arrow-big-down"

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
