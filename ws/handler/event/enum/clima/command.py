import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.clima.command.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Command"

    def _get_str(self, e):
        if e == home.event.clima.command.Event.On:
            return "on"
        elif e == home.event.clima.command.Event.Off:
            return "off"
        elif e == home.event.clima.command.Event.Keep:
            return "keep"
        return e

    def get_icon(self, e):
        if e == home.event.clima.command.Event.On:
            return "fas fa-toggle-on"
        elif e == home.event.clima.command.Event.Off:
            return "fas fa-toggle-off"
        elif e == home.event.clima.command.Event.Keep:
            return "fas fa-circle"
        return e
