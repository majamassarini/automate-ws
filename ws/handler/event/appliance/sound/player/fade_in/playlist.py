import home

from ws.handler.event.appliance.sound.player.playlist import Handler as Parent


class Handler(Parent):

    KLASS = home.appliance.sound.player.event.fade_in.playlist.Event
