import home

from ws.handler.event.appliance.sprinkler.duration import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sprinkler.event.partially_on.duration.Event
    LABEL = "Sprinkling time reduced duration"
