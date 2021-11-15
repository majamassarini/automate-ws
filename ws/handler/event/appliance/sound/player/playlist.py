import home
from ws.handler.event.appliance.event.str import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.event.playlist.Event
    TEMPLATE = "event/str.html"
    LABEL = "Playlist"
