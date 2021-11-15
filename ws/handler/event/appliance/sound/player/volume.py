import home
from ws.handler.event.appliance.event.int import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.event.volume.Event
    TEMPLATE = "event/zero_hundred.html"
    LABEL = "Volume"
