from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    LABEL = "Is it forced?"
    FORCED_NOT = "Unforced"
    ON = "on"
    OFF = "off"
    OPENED = "opened"
    CLOSED = "closed"

    ICON_UP = "ti ti-arrow-big-up"
    ICON_DOWN = "ti ti-arrow-big-down"
    ICON_OK = "ti ti-circle-check"
