import home

from ws.handler.event.enum import rain


class Handler(rain.Handler):

    LABEL = None
    KLASS = home.event.rain.Event
    APPLIANCE_KLASS = home.appliance.sensor.rainmeter.Appliance

    def get_icon(self, e):
        return None

    def get_description(self, e):
        return None
