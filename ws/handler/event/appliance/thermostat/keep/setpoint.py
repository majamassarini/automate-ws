import home

from ws.handler.event.appliance.thermostat.setpoint import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.thermostat.presence.event.keep.setpoint.Event
    LABEL = "Setpoint maintenance"
