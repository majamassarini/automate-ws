import home

from ws.handler.event.appliance.light.brightness import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.lux_balancing.brightness.Event
