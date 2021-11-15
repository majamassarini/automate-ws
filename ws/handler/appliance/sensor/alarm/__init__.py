import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sensor.alarm.Appliance
    LABEL_UNARMED = "Unarmed"
    LABEL_ARMED = "Armed"
    LABEL_TRIGGERED = "Triggered"
    ICON_UNARMED = "far fa-bell"
    ICON_ARMED = "fas fa-bell"
    ICON_TRIGGERED = "fas fa-exclamation"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.alarm.state.unarmed.State.VALUE
        ):
            return self.LABEL_UNARMED
        elif (
            appliance.state.VALUE == home.appliance.sensor.alarm.state.armed.State.VALUE
        ):
            return self.LABEL_ARMED
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.alarm.state.triggered.State.VALUE
        ):
            return self.LABEL_TRIGGERED

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.alarm.state.unarmed.State.VALUE
        ):
            return self.ICON_UNARMED
        elif (
            appliance.state.VALUE == home.appliance.sensor.alarm.state.armed.State.VALUE
        ):
            return self.ICON_ARMED
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.alarm.state.triggered.State.VALUE
        ):
            return self.ICON_TRIGGERED
