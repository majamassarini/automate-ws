import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sensor.motion.Appliance
    LABEL_SPOTTED = "Motion detected"
    LABEL_MISSED = "No motion"
    ICON_SPOTTED = "fas fa-eye"
    ICON_MISSED = "far fa-eye"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.motion.state.spotted.State.VALUE
        ):
            return self.LABEL_SPOTTED
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.motion.state.missed.State.VALUE
        ):
            return self.LABEL_MISSED

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.motion.state.spotted.State.VALUE
        ):
            return self.ICON_SPOTTED
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.motion.state.missed.State.VALUE
        ):
            return self.ICON_MISSED


from ws.handler.appliance.sensor.motion import home_event_motion
