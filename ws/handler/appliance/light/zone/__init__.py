import home
from ws.handler.appliance.light import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.zone.Appliance
    LABEL_ALARMED_ON = "Alarmed On"
    LABEL_ALARMED_OFF = "Alarmed Off"
    ICON_ALARMED_ON = "fas fa-bell"
    ICON_ALARMED_OFF = "fa fa-bell"

    def get_label(self, appliance):
        if appliance.state.VALUE == home.appliance.light.zone.state.on.State.VALUE:
            return self.LABEL_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.alarmed.off.State.VALUE
        ):
            return self.LABEL_ALARMED_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.alarmed.on.State.VALUE
        ):
            return self.LABEL_ALARMED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.forced.on.State.VALUE
        ):
            return self.LABEL_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.forced.off.State.VALUE
        ):
            return self.LABEL_FORCED_OFF
        else:
            return self.LABEL_OFF

    def get_icon(self, appliance):
        if appliance.state.VALUE == home.appliance.light.zone.state.on.State.VALUE:
            return self.ICON_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.alarmed.off.State.VALUE
        ):
            return self.ICON_ALARMED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.alarmed.on.State.VALUE
        ):
            return self.ICON_ALARMED_OFF
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.forced.on.State.VALUE
        ):
            return self.ICON_FORCED_ON
        elif (
            appliance.state.VALUE
            == home.appliance.light.zone.state.forced.off.State.VALUE
        ):
            return self.ICON_FORCED_OFF
        else:
            return self.ICON_OFF


from ws.handler.appliance.light.zone import home_event_presence
