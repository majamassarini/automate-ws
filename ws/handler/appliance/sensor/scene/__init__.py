import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sensor.scene.Appliance
    LABEL_TRIGGERED = "Is running"
    LABEL_UNTRIGGERED = "Is stopped"
    ICON_TRIGGERED = "fas fa-play"
    ICON_UNTRIGGERED = "fas fa-stop"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.scene.state.triggered.State.VALUE
        ):
            return self.LABEL_TRIGGERED
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.scene.state.untriggered.State.VALUE
        ):
            return self.LABEL_UNTRIGGERED

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.scene.state.triggered.State.VALUE
        ):
            return self.ICON_TRIGGERED
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.scene.state.untriggered.State.VALUE
        ):
            return self.ICON_UNTRIGGERED
