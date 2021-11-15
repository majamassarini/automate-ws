from ws.handler.event.int import Handler as Parent, Bean


class Handler(Parent):
    def post(self, request_data):
        value = request_data["value"]
        event = self.KLASS(int(value))
        return event


from ws.handler.event.appliance.light import hue
from ws.handler.event.appliance.light import show
from ws.handler.event.appliance.light import brightness
from ws.handler.event.appliance.light import saturation
from ws.handler.event.appliance.light import temperature
from ws.handler.event.appliance.light import lux_balancing
from ws.handler.event.appliance.light import circadian_rhythm
