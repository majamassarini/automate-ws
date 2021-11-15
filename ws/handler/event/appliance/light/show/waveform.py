import home

from ws.handler.event.enum import Handler as Parent


class Handler(Parent):

    KLASS = home.event.waveform.Event
    TEMPLATE = "event/enum.html"
    LABEL = "Show waveform?"
    SINE = "Sine"
    HALF_SINE = "Sine"
    PULSE = "Pulse"
    SAW = "Saw"
    TRIANGLE = "Triangle"

    def _get_str(self, e):
        if e == home.event.waveform.Event.Sine:
            return self.SINE
        elif e == home.event.waveform.Event.HalfSine:
            return self.HALF_SINE
        elif e == home.event.waveform.Event.Pulse:
            return self.PULSE
        elif e == home.event.waveform.Event.Saw:
            return self.SAW
        elif e == home.event.waveform.Event.Triangle:
            return self.TRIANGLE
        return e

    def get_description(self, e):
        return self._get_str(e)

    def get_icon(self, e):
        if e == home.event.waveform.Event.Sine:
            return "fa-solid fa-stumbleupon"
        elif e == home.event.waveform.Event.HalfSine:
            return "fa-brands fa-stumbleupon-circle"
        elif e == home.event.waveform.Event.Pulse:
            return "fa-solid fa-heart-pulse"
        elif e == home.event.waveform.Event.Saw:
            return "fa-solid fa-stairs"
        elif e == home.event.waveform.Event.Triangle:
            return "fa-solid fa-wave-square"
        return e
