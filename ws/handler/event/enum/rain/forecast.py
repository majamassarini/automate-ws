import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.rain.forecast.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Will it rain?"
    WILL_RAIN = "Will rain"
    WILL_NOT_RAIN = "Will not rain"

    def _get_str(self, e):
        if e == home.event.rain.forecast.Event.Off:
            return self.NO
        else:
            return self.YES

    def get_description(self, e):
        if e == home.event.rain.forecast.Event.Off:
            return self.WILL_NOT_RAIN
        else:
            return self.WILL_RAIN

    def get_icon(self, e):
        if e == home.event.rain.forecast.Event.Off:
            return "fas fa-tint-slash"
        else:
            return "fas fa-tint"
