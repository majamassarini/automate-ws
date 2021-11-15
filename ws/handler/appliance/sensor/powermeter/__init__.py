import home
from ws.handler.appliance.customization import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sensor.powermeter.Appliance

    def get_icon(self, appliance):
        return None


from ws.handler.appliance.sensor.powermeter import float
