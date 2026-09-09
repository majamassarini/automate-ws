from ws.handler.scheduler.handler import Handler as Parent


def _protocol_trigger_addresses(pt):
    """Try to extract address list from a wrapped protocol trigger."""
    details = []
    try:
        addrs = ", ".join(pt.addresses)
        if addrs:
            details.append({"label": "Address", "value": addrs})
    except (AttributeError, TypeError):
        pass
    return details


try:
    import home.scheduler.trigger.protocol

    class Handler(Parent):
        KLASS = home.scheduler.trigger.protocol.Trigger
        KIND = "Protocol"

        def get_details(self, trigger):
            return _protocol_trigger_addresses(trigger._protocol_trigger)

except ImportError:
    pass


try:
    import home.scheduler.trigger.protocol.delay

    class DelayHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.delay.Trigger
        KIND = "Protocol Delay"

        def get_details(self, trigger):
            details = _protocol_trigger_addresses(trigger._protocol_trigger)
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
    import home.scheduler.trigger.protocol.enum

    class EnumHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.enum.Trigger
        KIND = "Protocol Enum"

        def get_details(self, trigger):
            details = _protocol_trigger_addresses(trigger._protocol_trigger)
            try:
                details.append(
                    {"label": "Selected", "value": str(trigger._selected)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {
                        "label": "Direction",
                        "value": str(trigger._direction.name),
                    }
                )
            except AttributeError:
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.protocol.mean

    class MeanGreaterThanHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.mean.GreaterThan
        KIND = "Protocol Mean >"

        def get_details(self, trigger):
            details = _protocol_trigger_addresses(trigger._protocol_trigger)
            try:
                details.append(
                    {"label": "Threshold", "value": str(trigger._hit_value)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Samples", "value": str(trigger._samples.maxlen)}
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

    class MeanLesserThanHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.mean.LesserThan
        KIND = "Protocol Mean <"

        def get_details(self, trigger):
            details = _protocol_trigger_addresses(trigger._protocol_trigger)
            try:
                details.append(
                    {"label": "Threshold", "value": str(trigger._hit_value)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Samples", "value": str(trigger._samples.maxlen)}
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

    class MeanInBetweenHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.mean.InBetween
        KIND = "Protocol Mean ↔"

        def get_details(self, trigger):
            details = _protocol_trigger_addresses(trigger._protocol_trigger)
            try:
                details.append(
                    {"label": "Min", "value": str(trigger._min_value)}
                )
                details.append(
                    {"label": "Max", "value": str(trigger._max_value)}
                )
            except AttributeError:
                pass
            try:
                details.append(
                    {"label": "Samples", "value": str(trigger._samples.maxlen)}
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
    import home.scheduler.trigger.protocol.multi

    class MultiHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.multi.Trigger
        KIND = "Protocol Multi"

        def get_details(self, trigger):
            details = []
            try:
                addrs_a = ", ".join(trigger._positive_a.addresses)
                if addrs_a:
                    details.append({"label": "Condition A", "value": addrs_a})
            except (AttributeError, TypeError):
                pass
            try:
                addrs_b = ", ".join(trigger._positive_b.addresses)
                if addrs_b:
                    details.append({"label": "Condition B", "value": addrs_b})
            except (AttributeError, TypeError):
                pass
            return details

except ImportError:
    pass


try:
    import home.scheduler.trigger.protocol.timer

    class TimerHandler(Parent):
        KLASS = home.scheduler.trigger.protocol.timer.Trigger
        KIND = "Protocol Timer"

        def get_details(self, trigger):
            details = _protocol_trigger_addresses(trigger._protocol_trigger)
            try:
                details.append(
                    {"label": "Timeout", "value": f"{trigger._timeout} s"}
                )
            except AttributeError:
                pass
            try:
                stop = [str(p) for p in trigger._stop_timer_performers]
                if stop:
                    details.append(
                        {"label": "Stop notifies", "value": ", ".join(stop)}
                    )
            except AttributeError:
                pass
            return details

except ImportError:
    pass
