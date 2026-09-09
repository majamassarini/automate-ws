from ws.handler.scheduler.handler import Handler as Parent


try:
    import home.scheduler.trigger.interval

    class Handler(Parent):
        KLASS = home.scheduler.trigger.interval.Trigger
        KIND = "Interval"

        def get_details(self, trigger):
            try:
                return [{"label": "Interval", "value": str(trigger.interval)}]
            except AttributeError:
                pass
            s = str(trigger)
            start = s.find("[")
            if start >= 0:
                s = s[start + 1 :].rstrip("]")
            if s:
                return [{"label": "Interval", "value": s}]
            return []

except ImportError:
    pass
