from ws.handler.scheduler.handler import Handler as Parent


try:
    import home.scheduler.trigger.cron

    class Handler(Parent):
        KLASS = home.scheduler.trigger.cron.Trigger
        KIND = "Cron"

        def get_details(self, trigger):
            details = []
            try:
                for field in trigger.fields:
                    if not field.is_default:
                        details.append(
                            {"label": field.name, "value": str(field)}
                        )
            except AttributeError:
                s = str(trigger)
                start = s.find("[")
                if start >= 0:
                    s = s[start + 1 :].rstrip("]")
                if s:
                    details.append({"label": "Schedule", "value": s})
            return details

except ImportError:
    pass
