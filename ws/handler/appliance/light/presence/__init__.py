import home
from ws.handler.appliance.light import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.presence.Appliance
    LABEL_ALARMED = "Alarmed"
    ICON_ALARMED = "fas fa-bell"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.light.presence.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        else:
            return self.LABEL_OFF

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.light.presence.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        else:
            return self.ICON_OFF
