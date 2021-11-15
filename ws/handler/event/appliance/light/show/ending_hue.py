import home

from ws.handler.event.appliance.light.hue import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.light.event.show.ending_hue.Event
    LABEL = "Ending hue"
