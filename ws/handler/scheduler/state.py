from ws.handler.scheduler.handler import Handler as Parent


try:
    import home.scheduler.trigger.state.entering

    class EnteringHandler(Parent):
        KLASS = home.scheduler.trigger.state.entering.Trigger
        KIND = "Entering State"

        def get_details(self, trigger):
            try:
                return [{"label": "State", "value": str(trigger._state)}]
            except AttributeError:
                return []

except ImportError:
    pass


try:
    import home.scheduler.trigger.state.exiting

    class ExitingHandler(Parent):
        KLASS = home.scheduler.trigger.state.exiting.Trigger
        KIND = "Exiting State"

        def get_details(self, trigger):
            try:
                return [{"label": "State", "value": str(trigger._state)}]
            except AttributeError:
                return []

except ImportError:
    pass


try:
    import home.scheduler.trigger.state.entering.delay

    class EnteringDelayHandler(Parent):
        KLASS = home.scheduler.trigger.state.entering.delay.Trigger
        KIND = "Entering State (delayed)"

        def get_details(self, trigger):
            details = []
            try:
                details.append(
                    {"label": "State", "value": str(trigger._state)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Timeout", "value": f"{trigger._timeout} s"}
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.state.exiting.delay

    class ExitingDelayHandler(Parent):
        KLASS = home.scheduler.trigger.state.exiting.delay.Trigger
        KIND = "Exiting State (delayed)"

        def get_details(self, trigger):
            details = []
            try:
                details.append(
                    {"label": "State", "value": str(trigger._state)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Timeout", "value": f"{trigger._timeout} s"}
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.state.entering.disable_events

    class EnteringDisableEventsHandler(Parent):
        KLASS = home.scheduler.trigger.state.entering.disable_events.Trigger
        KIND = "Entering State (disable events)"

        def get_details(self, trigger):
            try:
                return [{"label": "State", "value": str(trigger._state)}]
            except AttributeError:
                return []

except ImportError:
    pass


try:
    import home.scheduler.trigger.state.entering.delay.enable_events

    class EnteringDelayEnableEventsHandler(Parent):
        KLASS = (
            home.scheduler.trigger.state.entering.delay.enable_events.Trigger
        )
        KIND = "Entering State (re-enable events, delayed)"

        def get_details(self, trigger):
            details = []
            try:
                details.append(
                    {"label": "State", "value": str(trigger._state)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Timeout", "value": f"{trigger._timeout} s"}
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.state.entering.delay.duration

    class EnteringDelayDurationHandler(Parent):
        KLASS = home.scheduler.trigger.state.entering.delay.duration.Trigger
        KIND = "Entering State (delayed by state duration)"

        def get_details(self, trigger):
            details = []
            try:
                state = trigger._state
                if isinstance(state, (tuple, list)):
                    state = state[0] if state else ""
                details.append({"label": "State", "value": str(state)})
            except AttributeError:
                pass
            try:
                timeout = trigger._delay.timeout
                if timeout:
                    details.append(
                        {"label": "Timeout", "value": f"{timeout} s"}
                    )
                else:
                    details.append(
                        {"label": "Timeout", "value": "from state duration"}
                    )
            except AttributeError:
                details.append(
                    {"label": "Timeout", "value": "from state duration"}
                )
            return details

except ImportError:
    pass
