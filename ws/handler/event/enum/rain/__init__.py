import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.rain.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Is it raining?"
    LABEL1 = "No rain"
    LABEL2 = "It is raining"

    def _get_str(self, e):
        if e == home.event.rain.Event.No:
            return self.NO
        elif e == home.event.rain.Event.Mist:
            return "mist"
        elif e == home.event.rain.Event.Gentle:
            return self.YES
        elif e == home.event.rain.Event.Heavy:
            return "heavy raining"
        elif e == home.event.rain.Event.Storm:
            return "storm raining"
        return e

    def get_description(self, e):
        if e == home.event.rain.Event.No:
            return self.LABEL1
        elif e == home.event.rain.Event.Gentle:
            return self.LABEL2

    def get_icon(self, e):
        if e == home.event.rain.Event.No:
            return "fas fa-tint-slash"
        elif e == home.event.rain.Event.Gentle:
            return "fas fa-tint"
        return e


from ws.handler.event.enum.rain import forecast, in_the_past
