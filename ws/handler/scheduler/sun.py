from ws.handler.scheduler.handler import Handler as Parent


def _observer_details(trigger):
    details = []
    try:
        obs = trigger._observer
        details.append({"label": "Latitude", "value": str(obs.lat)})
        details.append({"label": "Longitude", "value": str(obs.lon)})
        if obs.elev:
            details.append({"label": "Elevation", "value": f"{obs.elev} m"})
    except AttributeError:
        pass
    return details


try:
    import home.scheduler.trigger.sun.sunrise

    class SunriseHandler(Parent):
        KLASS = home.scheduler.trigger.sun.sunrise.Trigger
        KIND = "Sunrise"

        def get_details(self, trigger):
            return _observer_details(trigger)

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.sunset

    class SunsetHandler(Parent):
        KLASS = home.scheduler.trigger.sun.sunset.Trigger
        KIND = "Sunset"

        def get_details(self, trigger):
            return _observer_details(trigger)

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.sunhit

    class SunhitHandler(Parent):
        KLASS = home.scheduler.trigger.sun.sunhit.Trigger
        KIND = "Sunhit"

        def get_details(self, trigger):
            details = _observer_details(trigger)
            try:
                pos = trigger._position
                details.append(
                    {
                        "label": "Altitude",
                        "value": f"{pos.bottom_altitude}° – {pos.upper_altitude}°",
                    }
                )
                details.append(
                    {
                        "label": "Azimuth",
                        "value": f"{pos.min_azimuth}° – {pos.max_azimuth}°",
                    }
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.sunleft

    class SunleftHandler(Parent):
        KLASS = home.scheduler.trigger.sun.sunleft.Trigger
        KIND = "Sun Left"

        def get_details(self, trigger):
            details = _observer_details(trigger)
            try:
                pos = trigger._position
                details.append(
                    {
                        "label": "Altitude",
                        "value": f"{pos.bottom_altitude}° – {pos.upper_altitude}°",
                    }
                )
                details.append(
                    {
                        "label": "Azimuth",
                        "value": f"{pos.min_azimuth}° – {pos.max_azimuth}°",
                    }
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.twilight.civil.sunrise

    class CivilSunriseHandler(Parent):
        KLASS = home.scheduler.trigger.sun.twilight.civil.sunrise.Trigger
        KIND = "Civil Sunrise"

        def get_details(self, trigger):
            return _observer_details(trigger)

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.twilight.civil.sunset

    class CivilSunsetHandler(Parent):
        KLASS = home.scheduler.trigger.sun.twilight.civil.sunset.Trigger
        KIND = "Civil Sunset"

        def get_details(self, trigger):
            return _observer_details(trigger)

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.twilight.astronomical.sunrise

    class AstronomicalSunriseHandler(Parent):
        KLASS = (
            home.scheduler.trigger.sun.twilight.astronomical.sunrise.Trigger
        )
        KIND = "Astronomical Sunrise"

        def get_details(self, trigger):
            return _observer_details(trigger)

except ImportError:
    pass


try:
    import home.scheduler.trigger.sun.twilight.astronomical.sunset

    class AstronomicalSunsetHandler(Parent):
        KLASS = home.scheduler.trigger.sun.twilight.astronomical.sunset.Trigger
        KIND = "Astronomical Sunset"

        def get_details(self, trigger):
            return _observer_details(trigger)

except ImportError:
    pass
