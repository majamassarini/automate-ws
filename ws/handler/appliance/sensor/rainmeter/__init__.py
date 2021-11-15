import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sensor.rainmeter.Appliance
    LABEL_NO = "No rain"
    LABEL_GENTLE = "Gentle raining"
    ICON_NO = "fas fa-tint-slash"
    ICON_GENTLE = "fas fa-tint"

    def get_label(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.rainmeter.state.no.State.VALUE
        ):
            return self.LABEL_NO
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.rainmeter.state.gentle.State.VALUE
        ):
            return self.LABEL_GENTLE

    def get_icon(self, appliance):
        if (
            appliance.state.VALUE
            == home.appliance.sensor.rainmeter.state.no.State.VALUE
        ):
            return self.ICON_NO
        elif (
            appliance.state.VALUE
            == home.appliance.sensor.rainmeter.state.gentle.State.VALUE
        ):
            return self.ICON_GENTLE


from ws.handler.appliance.sensor.rainmeter import home_event_rain
