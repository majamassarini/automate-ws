from ws.handler.scheduler.handler import Handler as Parent


try:
    import home.scheduler.trigger.circadian_rhythm

    class Handler(Parent):
        KLASS = home.scheduler.trigger.circadian_rhythm.Trigger
        KIND = "Circadian"

        def get_details(self, trigger):
            details = []
            try:
                details.append(
                    {
                        "label": "Events/day",
                        "value": str(len(trigger._events_in_a_day)),
                    }
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {
                        "label": "Interval",
                        "value": f"{trigger._interval:.0f} min",
                    }
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass
