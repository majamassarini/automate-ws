import home

from ws.handler.event.appliance.light.temperature import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.circadian_rhythm.temperature.Event
