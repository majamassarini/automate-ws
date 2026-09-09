from ws.handler.scheduler.handler import Handler as Parent


try:
    import home.scheduler.trigger.date.resettable

    class ResettableHandler(Parent):
        KLASS = home.scheduler.trigger.date.resettable.Trigger
        KIND = "Date"

        def get_details(self, trigger):
            details = []
            try:
                details.append(
                    {"label": "Run date", "value": str(trigger.run_date)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Enabled", "value": str(trigger.is_enabled)}
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass
