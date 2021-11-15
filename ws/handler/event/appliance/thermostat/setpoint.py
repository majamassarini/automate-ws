import home
from ws.handler.event.appliance.event.float import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.thermostat.presence.event.setpoint.Event
    TEMPLATE = "event/float.html"
    LABEL = "Setpoint"
