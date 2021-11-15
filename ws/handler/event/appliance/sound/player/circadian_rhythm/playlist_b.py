import home

from ws.handler.event.appliance.sound.player.playlist import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event
    LABEL = "Playlist user B"
