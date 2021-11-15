import home
from ws.handler.event.float import Handler as Parent


class Handler(Parent):

    LABEL = None
    APPLIANCE_KLASS = home.appliance.sensor.powermeter.Appliance

    def get_icon(self, event):
        return None

    def get_description(self, e):
        return None
