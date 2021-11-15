import home

from ws.handler.event.appliance.event.int import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.brightness.Event
    TEMPLATE = "event/zero_hundred.html"
    LABEL = "Brightness"
