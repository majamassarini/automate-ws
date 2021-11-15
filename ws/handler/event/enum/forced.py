from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    LABEL = "Is it forced?"
    FORCED_NOT = "Unforced"
    ON = "on"
    OFF = "off"
    OPENED = "opened"
    CLOSED = "closed"

    ICON_UP = "far fa-hand-point-up"
    ICON_DOWN = "far fa-hand-point-down"
    ICON_OK = "far fa-thumbs-up"
