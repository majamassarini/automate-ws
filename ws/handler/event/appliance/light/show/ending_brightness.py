import home

from ws.handler.event.appliance.light.brightness import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.show.ending_brightness.Event
    LABEL = "Ending brightness"
