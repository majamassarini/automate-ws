import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.scene.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Scene is"

    def _get_str(self, e):
        if e == home.event.scene.Event.Triggered:
            return "playing"
        elif e == home.event.scene.Event.Untriggered:
            return "stopped"
        return e

    def get_icon(self, e):
        if e == home.event.scene.Event.Triggered:
            return "ti ti-player-play"
        elif e == home.event.scene.Event.Untriggered:
            return "ti ti-player-stop"
        return e
