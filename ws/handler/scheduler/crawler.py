from ws.handler.scheduler.handler import Handler as Parent


try:
    import home.scheduler.trigger.crawler.osmer_fvg.will_rain.on

    class RainOnHandler(Parent):
        KLASS = home.scheduler.trigger.crawler.osmer_fvg.will_rain.on.Trigger
        KIND = "Rain On"

        def get_details(self, trigger):
            details = []
            try:
                details.append({"label": "Zone", "value": str(trigger._zone)})
            except AttributeError:
                pass
            try:
                details.append(
                    {
                        "label": "Probability",
                        "value": f">= {trigger._probability}%",
                    }
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.crawler.osmer_fvg.will_rain.off

    class RainOffHandler(Parent):
        KLASS = home.scheduler.trigger.crawler.osmer_fvg.will_rain.off.Trigger
        KIND = "Rain Off"

        def get_details(self, trigger):
            details = []
            try:
                details.append({"label": "Zone", "value": str(trigger._zone)})
            except AttributeError:
                pass
            try:
                details.append(
                    {
                        "label": "Probability",
                        "value": f"< {trigger._probability}%",
                    }
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass
