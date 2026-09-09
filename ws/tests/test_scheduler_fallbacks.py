"""Tests for the AttributeError fallback paths in scheduler handler
get_details() methods, and edge-cases in _protocol_trigger_addresses.

All handlers are called with mock trigger objects that intentionally lack
the expected attributes so that the except/fallback branches are exercised.
"""

import unittest

import home.scheduler.trigger.protocol
import home.scheduler.trigger.protocol.delay
import home.scheduler.trigger.protocol.enum
import home.scheduler.trigger.protocol.mean
import home.scheduler.trigger.protocol.multi
import home.scheduler.trigger.protocol.timer
import home.scheduler.trigger.state.entering
import home.scheduler.trigger.state.entering.delay
import home.scheduler.trigger.state.entering.delay.duration
import home.scheduler.trigger.state.entering.delay.enable_events
import home.scheduler.trigger.state.entering.disable_events
import home.scheduler.trigger.state.exiting
import home.scheduler.trigger.state.exiting.delay
import home.scheduler.trigger.interval
import home.scheduler.trigger.cron

from ws.handler.scheduler import registry as scheduler_registry
from ws.handler.scheduler.protocol import _protocol_trigger_addresses


# ---------------------------------------------------------------------------
# Minimal mock objects whose attributes raise AttributeError on demand
# ---------------------------------------------------------------------------


class _Bare:
    """A trigger stub with no domain attributes at all."""

    name = "bare"


class _WithStr:
    """Stub whose __str__ contains a bracketed value."""

    name = "with-str"

    def __init__(self, s):
        self._s = s

    def __str__(self):
        return self._s


class _TupleState:
    """Stub where _state is a tuple (tests tuple-unwrap branch)."""

    name = "tuple-state"
    _state = ("On",)
    _timeout = 60.0


class _EmptyTupleState:
    """Stub where _state is an empty tuple."""

    name = "empty-tuple-state"
    _state = ()
    _timeout = 5.0


class _MockDelay:
    def __init__(self, timeout):
        self.timeout = timeout


class _ZeroTimeout:
    """Stub where _delay.timeout is 0 — triggers 'from state duration'."""

    name = "zero-timeout"
    _state = "On"
    _delay = _MockDelay(0)


class _StateOnly:
    """Stub with _state but no _timeout — tests partial attribute presence."""

    name = "state-only"
    _state = "Closed"


class _NoAddressesPt:
    """Protocol trigger stub that has no .addresses attribute."""

    pass


class _EmptyAddressesPt:
    """Protocol trigger stub with an empty addresses list."""

    addresses: list[str] = []


class _TypeErrorAddressesPt:
    """Protocol trigger stub whose addresses is not iterable."""

    addresses = None


# ---------------------------------------------------------------------------
# Helper: retrieve a handler from the registry by trigger KLASS
# ---------------------------------------------------------------------------


def _handler(klass):
    return scheduler_registry.mapper[klass]()


# ---------------------------------------------------------------------------
# Interval handler — AttributeError fallback path
# ---------------------------------------------------------------------------


class TestIntervalFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(home.scheduler.trigger.interval.Trigger)

    def test_fallback_parses_str_with_bracket(self):
        t = _WithStr("Interval [0:10:00]")
        details = self.h.get_details(t)
        self.assertEqual(details, [{"label": "Interval", "value": "0:10:00"}])

    def test_fallback_uses_full_str_when_no_bracket(self):
        t = _WithStr("Interval 0:10:00")
        details = self.h.get_details(t)
        self.assertEqual(
            details, [{"label": "Interval", "value": "Interval 0:10:00"}]
        )

    def test_fallback_returns_empty_when_str_empty(self):
        t = _WithStr("")
        details = self.h.get_details(t)
        self.assertEqual(details, [])


# ---------------------------------------------------------------------------
# Cron handler — AttributeError fallback path
# ---------------------------------------------------------------------------


class TestCronFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(home.scheduler.trigger.cron.Trigger)

    def test_fallback_parses_str_with_bracket(self):
        t = _WithStr("cron[*/5 * * * *]")
        details = self.h.get_details(t)
        self.assertEqual(
            details, [{"label": "Schedule", "value": "*/5 * * * *"}]
        )

    def test_fallback_uses_full_str_when_no_bracket(self):
        t = _WithStr("no bracket here")
        details = self.h.get_details(t)
        self.assertEqual(
            details, [{"label": "Schedule", "value": "no bracket here"}]
        )


# ---------------------------------------------------------------------------
# State — Entering handler
# ---------------------------------------------------------------------------


class TestEnteringStateFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(home.scheduler.trigger.state.entering.Trigger)

    def test_missing_state_returns_empty(self):
        details = self.h.get_details(_Bare())
        self.assertEqual(details, [])


# ---------------------------------------------------------------------------
# State — Exiting handler
# ---------------------------------------------------------------------------


class TestExitingStateFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(home.scheduler.trigger.state.exiting.Trigger)

    def test_missing_state_returns_empty(self):
        details = self.h.get_details(_Bare())
        self.assertEqual(details, [])


# ---------------------------------------------------------------------------
# State — Entering Delay handler
# ---------------------------------------------------------------------------


class TestEnteringDelayFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(home.scheduler.trigger.state.entering.delay.Trigger)

    def test_missing_both_returns_empty(self):
        details = self.h.get_details(_Bare())
        self.assertEqual(details, [])

    def test_state_only_no_timeout(self):
        details = self.h.get_details(_StateOnly())
        self.assertEqual(len(details), 1)
        self.assertEqual(details[0]["label"], "State")
        self.assertEqual(details[0]["value"], "Closed")


# ---------------------------------------------------------------------------
# State — Exiting Delay handler
# ---------------------------------------------------------------------------


class TestExitingDelayFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(home.scheduler.trigger.state.exiting.delay.Trigger)

    def test_missing_both_returns_empty(self):
        details = self.h.get_details(_Bare())
        self.assertEqual(details, [])

    def test_state_only(self):
        details = self.h.get_details(_StateOnly())
        labels = [d["label"] for d in details]
        self.assertIn("State", labels)
        self.assertNotIn("Timeout", labels)


# ---------------------------------------------------------------------------
# State — Entering Disable Events handler
# ---------------------------------------------------------------------------


class TestEnteringDisableEventsFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(
            home.scheduler.trigger.state.entering.disable_events.Trigger
        )

    def test_missing_state_returns_empty(self):
        details = self.h.get_details(_Bare())
        self.assertEqual(details, [])


# ---------------------------------------------------------------------------
# State — Entering Delay Enable Events handler
# ---------------------------------------------------------------------------


class TestEnteringDelayEnableEventsFallback(unittest.TestCase):

    def setUp(self):
        self.h = _handler(
            home.scheduler.trigger.state.entering.delay.enable_events.Trigger
        )

    def test_missing_both_returns_empty(self):
        details = self.h.get_details(_Bare())
        self.assertEqual(details, [])


# ---------------------------------------------------------------------------
# State — Entering Delay Duration handler (several branches)
# ---------------------------------------------------------------------------


class TestEnteringDelayDurationBranches(unittest.TestCase):

    def setUp(self):
        self.h = _handler(
            home.scheduler.trigger.state.entering.delay.duration.Trigger
        )

    def test_tuple_state_uses_first_element(self):
        details = self.h.get_details(_TupleState())
        state_detail = next(d for d in details if d["label"] == "State")
        self.assertEqual(state_detail["value"], "On")

    def test_empty_tuple_state_uses_empty_string(self):
        details = self.h.get_details(_EmptyTupleState())
        state_detail = next(d for d in details if d["label"] == "State")
        self.assertEqual(state_detail["value"], "")

    def test_zero_timeout_yields_from_state_duration(self):
        details = self.h.get_details(_ZeroTimeout())
        timeout_detail = next(d for d in details if d["label"] == "Timeout")
        self.assertEqual(timeout_detail["value"], "from state duration")

    def test_missing_delay_yields_from_state_duration(self):
        details = self.h.get_details(_StateOnly())
        timeout_detail = next(d for d in details if d["label"] == "Timeout")
        self.assertEqual(timeout_detail["value"], "from state duration")

    def test_missing_state_still_returns_timeout(self):
        details = self.h.get_details(_Bare())
        labels = [d["label"] for d in details]
        self.assertIn("Timeout", labels)

    def test_missing_state_with_bare_trigger(self):
        details = self.h.get_details(_Bare())
        timeout_detail = next(d for d in details if d["label"] == "Timeout")
        self.assertEqual(timeout_detail["value"], "from state duration")


# ---------------------------------------------------------------------------
# _protocol_trigger_addresses — address-absent and empty-address paths
# ---------------------------------------------------------------------------


class TestProtocolTriggerAddresses(unittest.TestCase):

    def test_no_addresses_attribute_returns_empty(self):
        details = _protocol_trigger_addresses(_NoAddressesPt())
        self.assertEqual(details, [])

    def test_empty_addresses_returns_empty(self):
        details = _protocol_trigger_addresses(_EmptyAddressesPt())
        self.assertEqual(details, [])

    def test_none_addresses_returns_empty(self):
        details = _protocol_trigger_addresses(_TypeErrorAddressesPt())
        self.assertEqual(details, [])

    def test_valid_addresses_returned(self):
        class Pt:
            addresses = ["1/0/1", "1/0/2"]

        details = _protocol_trigger_addresses(Pt())
        self.assertEqual(
            details, [{"label": "Address", "value": "1/0/1, 1/0/2"}]
        )


if __name__ == "__main__":
    unittest.main()
