import home
from ws.handler.event.appliance.sound.player.volume import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.event.volume_scale.Event
    LABEL = "Sleepy Volume Scale"
