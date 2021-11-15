import home

from ws.handler.event.appliance.light.saturation import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.circadian_rhythm.saturation.Event
