import home
from ws.handler.event.appliance.sound.player.volume import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.event.sleepy_volume.Event
    LABEL = "Sleepy Volume"
