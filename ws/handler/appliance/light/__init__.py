import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.Appliance
    LABEL_ON = "On"
    LABEL_FORCED_ON = "Forced On"
    LABEL_OFF = "Off"
    LABEL_FORCED_OFF = "Forced Off"
    ICON_ON = "fas fa-lightbulb"
    ICON_OFF = "far fa-lightbulb"
    ICON_FORCED_ON = "far fa-hand-point-up"
    ICON_FORCED_OFF = "far fa-hand-point-down"

    def get_label(self, appliance):
        if appliance.state.VALUE == home.appliance.light.state.on.State.VALUE:
            return self.LABEL_ON
        elif appliance.state.VALUE == home.appliance.light.state.forced.on.State.VALUE:
            return self.LABEL_FORCED_ON
        elif appliance.state.VALUE == home.appliance.light.state.forced.off.State.VALUE:
            return self.LABEL_FORCED_OFF
        else:
            return self.LABEL_OFF

    def get_icon(self, appliance):
        if appliance.state.VALUE == home.appliance.light.state.on.State.VALUE:
            return self.ICON_ON
        elif appliance.state.VALUE == home.appliance.light.state.forced.on.State.VALUE:
            return self.ICON_FORCED_ON
        elif appliance.state.VALUE == home.appliance.light.state.forced.off.State.VALUE:
            return self.ICON_FORCED_OFF
        else:
            return self.ICON_OFF


from ws.handler.appliance.light import zone, presence, indoor
