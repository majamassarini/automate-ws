import home
from ws.handler.event.appliance.event.int import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sprinkler.event.duration.Event
    TEMPLATE = "event/int.html"
    LABEL = "Sprinkling time duration"
