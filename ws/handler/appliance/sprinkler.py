import home
from ws.handler.appliance.light import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sprinkler.Appliance
    LABEL_PARTIALLY_ON = "Partially On"
    LABEL_FORCED_PARTIALLY_ON = "Forced Partially On"
    ICON_ON = "fas fa-water"
    ICON_OFF = "fas fa-faucet"
    ICON_PARTIALLY_ON = "fas fa-hand-holding-water"
    ICON_FORCED_PARTIALLY_ON = "far fa-hand-point-right"

    def get_label(self, appliance):
        if appliance.state.VALUE == home.appliance.sprinkler.state.on.State.VALUE:
            return self.LABEL_ON
        elif appliance.state.VALUE == home.appliance.sprinkler.state.off.State.VALUE:
            return self.LABEL_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.partially_on.State.VALUE
        ):
            return self.LABEL_PARTIALLY_ON
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.off.State.VALUE
        ):
            return self.LABEL_FORCED_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.partially_on.State.VALUE
        ):
            return self.LABEL_FORCED_PARTIALLY_ON

    def get_icon(self, appliance):
        if appliance.state.VALUE == home.appliance.sprinkler.state.on.State.VALUE:
            return self.ICON_ON
        elif appliance.state.VALUE == home.appliance.sprinkler.state.off.State.VALUE:
            return self.ICON_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.partially_on.State.VALUE
        ):
            return self.ICON_PARTIALLY_ON
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.off.State.VALUE
        ):
            return self.ICON_FORCED_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.partially_on.State.VALUE
        ):
            return self.ICON_FORCED_PARTIALLY_ON

    def is_displayed(self, appliance, event):
        result = True
        if (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.on.State.VALUE
            or appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.off.State.VALUE
            or appliance.state.VALUE == home.appliance.sprinkler.state.on.State.VALUE
            or appliance.state.VALUE == home.appliance.sprinkler.state.off.State.VALUE
        ) and isinstance(
            event, home.appliance.sprinkler.event.partially_on.duration.Event
        ):
            result = False
        elif (
            appliance.state.VALUE
            == home.appliance.sprinkler.state.forced.partially_on.State.VALUE
            or appliance.state.VALUE
            == home.appliance.sprinkler.state.partially_on.State.VALUE
        ) and (
            isinstance(event, home.appliance.sprinkler.event.duration.Event)
            and not isinstance(
                event, home.appliance.sprinkler.event.partially_on.duration.Event
            )
        ):
            result = False
        return result
