import home

from ws.handler.event.enum import motion


class Handler(motion.Handler):

    LABEL = None
    KLASS = home.event.motion.Event
    APPLIANCE_KLASS = home.appliance.sensor.motion.Appliance

    def get_icon(self, e):
        return None

    def get_description(self, e):
        return None
