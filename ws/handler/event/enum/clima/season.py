import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.clima.season.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Season is"

    def _get_str(self, e):
        if e == home.event.clima.season.Event.Winter:
            return "winter"
        elif e == home.event.clima.season.Event.Summer:
            return "summer"
        elif e == home.event.clima.season.Event.Spring:
            return "sprint"
        elif e == home.event.clima.season.Event.Fall:
            return "fall"
        return e

    def get_icon(self, e):
        if e == home.event.clima.season.Event.Winter:
            return "fas fa-snowflake"
        elif e == home.event.clima.season.Event.Summer:
            return "fas fa-umbrella-beach"
        elif e == home.event.clima.season.Event.Spring:
            return "fas fa-seeding"
        elif e == home.event.clima.season.Event.Fall:
            return "fas fa-leaf"
        return e
