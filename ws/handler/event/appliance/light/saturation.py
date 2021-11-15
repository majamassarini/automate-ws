import home

from ws.handler.event.appliance.event.int import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.saturation.Event
    TEMPLATE = "event/saturation.html"
    LABEL = "Saturation"
