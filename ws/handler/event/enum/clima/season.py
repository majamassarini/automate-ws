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
            return "ti ti-snowflake"
        elif e == home.event.clima.season.Event.Summer:
            return "ti ti-sun-wind"
        elif e == home.event.clima.season.Event.Spring:
            return "ti ti-plant"
        elif e == home.event.clima.season.Event.Fall:
            return "ti ti-leaf"
        return e
