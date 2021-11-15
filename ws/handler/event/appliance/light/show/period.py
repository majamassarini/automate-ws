import home

from ws.handler.event.appliance.event.int import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.show.period.Event
    LABEL = "Period"
