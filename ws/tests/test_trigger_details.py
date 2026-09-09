"""Unit tests for scheduler-trigger detail entries shown in the details page.

Each test class covers one trigger type, verifying both the ``kind`` label
and every ``detail`` entry that the corresponding handler produces.

The test uses the "zone light" appliance because its group ("lights") has
five performers, so every ``_pt(idx)`` call in the mock data resolves to a
real performer trigger and the performer-name lookup is fully exercised.
"""

import unittest

from ws.handler.details import Handler
from ws.tests.testcase import Resources


# ---------------------------------------------------------------------------
# Shared fixture — built once for the whole module
# ---------------------------------------------------------------------------


def setUpModule():  # noqa: N802
    global _entries, _handler
    resources = Resources(None, None, "ws", "brain")
    _handler = Handler(resources)

    zone_light = None
    for coll in resources.appliances.values():
        for a in coll:
            if a.name == "zone light":
                zone_light = a
                break
        if zone_light:
            break

    performers = _handler.get_performers(zone_light)
    _, all_group = _handler.get_group_of_performers(zone_light)
    reactive, scheduled = _handler.get_scheduler_triggers(
        all_group, performers
    )
    _entries = {e["name"]: e for e in reactive + scheduled}


# ---------------------------------------------------------------------------
# Base helper
# ---------------------------------------------------------------------------


class _Base(unittest.TestCase):

    def _entry(self, name):
        self.assertIn(name, _entries, f"trigger '{name}' not found in entries")
        return _entries[name]

    def _detail(self, trigger_name, label):
        """Return the value for *label* in *trigger_name*'s details list."""
        entry = self._entry(trigger_name)
        for d in entry["details"]:
            if d["label"] == label:
                return d["value"]
        labels = [d["label"] for d in entry["details"]]
        self.fail(
            f"label '{label}' not found in '{trigger_name}' details; "
            f"present labels: {labels}"
        )

    def _assert_kind(self, trigger_name, expected_kind):
        entry = self._entry(trigger_name)
        self.assertEqual(entry["kind"], expected_kind)

    def _assert_detail(self, trigger_name, label, expected_value):
        self.assertEqual(self._detail(trigger_name, label), expected_value)

    def _assert_label_present(self, trigger_name, label):
        entry = self._entry(trigger_name)
        labels = [d["label"] for d in entry["details"]]
        self.assertIn(label, labels)


# ---------------------------------------------------------------------------
# Sun triggers
# ---------------------------------------------------------------------------

_LAT = "45:12:00.0"
_LON = "13:12:00.0"
_ELEV = "280.0 m"
_ALT = "10.0° – 90.0°"
_AZ = "10.0° – 160.0°"


class TestSunrise(_Base):
    def test_kind(self):
        self._assert_kind("sunrise", "Sunrise")

    def test_latitude(self):
        self._assert_detail("sunrise", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("sunrise", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("sunrise", "Elevation", _ELEV)


class TestSunset(_Base):
    def test_kind(self):
        self._assert_kind("sunset", "Sunset")

    def test_latitude(self):
        self._assert_detail("sunset", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("sunset", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("sunset", "Elevation", _ELEV)


class TestSunhit(_Base):
    def test_kind(self):
        self._assert_kind("sunhit south windows", "Sunhit")

    def test_latitude(self):
        self._assert_detail("sunhit south windows", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("sunhit south windows", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("sunhit south windows", "Elevation", _ELEV)

    def test_altitude(self):
        self._assert_detail("sunhit south windows", "Altitude", _ALT)

    def test_azimuth(self):
        self._assert_detail("sunhit south windows", "Azimuth", _AZ)


class TestSunleft(_Base):
    def test_kind(self):
        self._assert_kind("sunleft south windows", "Sun Left")

    def test_latitude(self):
        self._assert_detail("sunleft south windows", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("sunleft south windows", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("sunleft south windows", "Elevation", _ELEV)

    def test_altitude(self):
        self._assert_detail("sunleft south windows", "Altitude", _ALT)

    def test_azimuth(self):
        self._assert_detail("sunleft south windows", "Azimuth", _AZ)


class TestCivilSunrise(_Base):
    def test_kind(self):
        self._assert_kind("civil twilight sunrise", "Civil Sunrise")

    def test_latitude(self):
        self._assert_detail("civil twilight sunrise", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("civil twilight sunrise", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("civil twilight sunrise", "Elevation", _ELEV)


class TestCivilSunset(_Base):
    def test_kind(self):
        self._assert_kind("civil twilight sunset", "Civil Sunset")

    def test_latitude(self):
        self._assert_detail("civil twilight sunset", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("civil twilight sunset", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("civil twilight sunset", "Elevation", _ELEV)


class TestAstronomicalSunrise(_Base):
    def test_kind(self):
        self._assert_kind(
            "astronomical twilight sunrise", "Astronomical Sunrise"
        )

    def test_latitude(self):
        self._assert_detail("astronomical twilight sunrise", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("astronomical twilight sunrise", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail(
            "astronomical twilight sunrise", "Elevation", _ELEV
        )


class TestAstronomicalSunset(_Base):
    def test_kind(self):
        self._assert_kind(
            "astronomical twilight sunset", "Astronomical Sunset"
        )

    def test_latitude(self):
        self._assert_detail("astronomical twilight sunset", "Latitude", _LAT)

    def test_longitude(self):
        self._assert_detail("astronomical twilight sunset", "Longitude", _LON)

    def test_elevation(self):
        self._assert_detail("astronomical twilight sunset", "Elevation", _ELEV)


# ---------------------------------------------------------------------------
# Time-based triggers
# ---------------------------------------------------------------------------


class TestCron(_Base):
    def test_kind(self):
        self._assert_kind("morning alarm", "Cron")

    def test_hour(self):
        self._assert_detail("morning alarm", "hour", "7")

    def test_minute(self):
        self._assert_detail("morning alarm", "minute", "30")


class TestInterval(_Base):
    def test_kind(self):
        self._assert_kind("temperature check", "Interval")

    def test_interval(self):
        self._assert_detail("temperature check", "Interval", "0:10:00")


class TestCircadian(_Base):
    def test_kind(self):
        self._assert_kind("circadian rhythm", "Circadian")

    def test_events_per_day_present(self):
        self._assert_label_present("circadian rhythm", "Events/day")

    def test_interval_present(self):
        self._assert_label_present("circadian rhythm", "Interval")


class TestDate(_Base):
    def test_kind(self):
        self._assert_kind("scheduled event", "Date")

    def test_run_date_present(self):
        self._assert_label_present("scheduled event", "Run date")

    def test_enabled(self):
        self._assert_detail("scheduled event", "Enabled", "True")


# ---------------------------------------------------------------------------
# State triggers
# ---------------------------------------------------------------------------


class TestEnteringState(_Base):
    def test_kind(self):
        self._assert_kind("entering on", "Entering State")

    def test_state(self):
        self._assert_detail("entering on", "State", "On")


class TestExitingState(_Base):
    def test_kind(self):
        self._assert_kind("exiting on", "Exiting State")

    def test_state(self):
        self._assert_detail("exiting on", "State", "On")


class TestEnteringStateDelayed(_Base):
    def test_kind(self):
        self._assert_kind("auto off after 30 min", "Entering State (delayed)")

    def test_state(self):
        self._assert_detail("auto off after 30 min", "State", "On")

    def test_timeout(self):
        self._assert_detail("auto off after 30 min", "Timeout", "1800.0 s")


class TestExitingStateDelayed(_Base):
    def test_kind(self):
        self._assert_kind("confirm off after 5 min", "Exiting State (delayed)")

    def test_state(self):
        self._assert_detail("confirm off after 5 min", "State", "On")

    def test_timeout(self):
        self._assert_detail("confirm off after 5 min", "Timeout", "300.0 s")


class TestEnteringStateDelayedByDuration(_Base):
    _NAME = "auto off after state duration"

    def test_kind(self):
        self._assert_kind(
            self._NAME, "Entering State (delayed by state duration)"
        )

    def test_state(self):
        self._assert_detail(self._NAME, "State", "On")

    def test_timeout(self):
        # Timeout is populated by the is_triggered() call in testcase.py
        # with _MockState("On", duration=300).
        self._assert_detail(self._NAME, "Timeout", "300 s")


class TestEnteringStateDisableEvents(_Base):
    _NAME = "disable forced off on entry"

    def test_kind(self):
        self._assert_kind(self._NAME, "Entering State (disable events)")

    def test_state(self):
        self._assert_detail(self._NAME, "State", "On")


class TestEnteringStateReEnableEventsDelayed(_Base):
    _NAME = "re-enable forced off after grace"

    def test_kind(self):
        self._assert_kind(
            self._NAME, "Entering State (re-enable events, delayed)"
        )

    def test_state(self):
        self._assert_detail(self._NAME, "State", "On")

    def test_timeout(self):
        self._assert_detail(self._NAME, "Timeout", "5.0 s")


# ---------------------------------------------------------------------------
# Protocol triggers
# ---------------------------------------------------------------------------


class TestProtocol(_Base):
    # "condition" uses _pt(1) = "simple light performer" trigger
    _NAME = "condition"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol")

    def test_performer_name(self):
        self._assert_detail(
            self._NAME, "Triggered by performer", "simple light performer"
        )

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "1/0/2")


class TestProtocolReactive(_Base):
    # "reacts to sensor" uses _pt(0) = "zone light performer" trigger (reactive)
    _NAME = "reacts to sensor"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol")

    def test_performer_name(self):
        self._assert_detail(
            self._NAME, "Triggered by performer", "zone light performer"
        )

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "1/0/2")


class TestProtocolDelay(_Base):
    # "delayed condition" uses _pt(2) = "presence light performer" trigger
    _NAME = "delayed condition"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Delay")

    def test_performer_name(self):
        self._assert_detail(
            self._NAME, "Triggered by performer", "presence light performer"
        )

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "1/0/2")

    def test_timeout(self):
        self._assert_detail(self._NAME, "Timeout", "30.0 s")


class TestProtocolEnum(_Base):
    # "cycle mode" uses _pt(3) = "hue light performer" trigger
    _NAME = "cycle mode"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Enum")

    def test_performer_name(self):
        self._assert_detail(
            self._NAME, "Triggered by performer", "hue light performer"
        )

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "1/0/2")

    def test_selected_present(self):
        self._assert_label_present(self._NAME, "Selected")

    def test_direction(self):
        self._assert_detail(self._NAME, "Direction", "next")


class TestProtocolMeanGreaterThan(_Base):
    _NAME = "temp high"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Mean >")

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "4/0/1")

    def test_threshold(self):
        self._assert_detail(self._NAME, "Threshold", "25.0")

    def test_samples(self):
        self._assert_detail(self._NAME, "Samples", "10")

    def test_timeout(self):
        self._assert_detail(self._NAME, "Timeout", "60.0 s")


class TestProtocolMeanLesserThan(_Base):
    _NAME = "temp low"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Mean <")

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "4/0/1")

    def test_threshold(self):
        self._assert_detail(self._NAME, "Threshold", "18.0")

    def test_samples(self):
        self._assert_detail(self._NAME, "Samples", "10")

    def test_timeout(self):
        self._assert_detail(self._NAME, "Timeout", "60.0 s")


class TestProtocolMeanInBetween(_Base):
    _NAME = "temp comfortable"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Mean ↔")

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "4/0/1")

    def test_min(self):
        self._assert_detail(self._NAME, "Min", "18.0")

    def test_max(self):
        self._assert_detail(self._NAME, "Max", "25.0")

    def test_samples(self):
        self._assert_detail(self._NAME, "Samples", "10")

    def test_timeout(self):
        self._assert_detail(self._NAME, "Timeout", "60.0 s")


class TestProtocolMulti(_Base):
    # positive_a=_pt(0), negative_a=_pt(1), positive_b=_pt(2), negative_b=_pt(3)
    _NAME = "and condition"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Multi")

    def test_triggered_by_a_positive(self):
        self._assert_detail(
            self._NAME, "Triggered by (A+)", "zone light performer"
        )

    def test_reset_by_a_negative(self):
        self._assert_detail(
            self._NAME, "Reset by (A-)", "simple light performer"
        )

    def test_triggered_by_b_positive(self):
        self._assert_detail(
            self._NAME, "Triggered by (B+)", "presence light performer"
        )

    def test_reset_by_b_negative(self):
        self._assert_detail(self._NAME, "Reset by (B-)", "hue light performer")

    def test_condition_a_address(self):
        self._assert_detail(self._NAME, "Condition A", "1/0/2")

    def test_condition_b_address(self):
        self._assert_detail(self._NAME, "Condition B", "1/0/2")


class TestProtocolTimer(_Base):
    # "timed off" uses _pt(4) = "dimmerable light performer" trigger
    _NAME = "timed off"

    def test_kind(self):
        self._assert_kind(self._NAME, "Protocol Timer")

    def test_performer_name(self):
        self._assert_detail(
            self._NAME, "Triggered by performer", "dimmerable light performer"
        )

    def test_address(self):
        self._assert_detail(self._NAME, "Address", "1/0/2")

    def test_timeout(self):
        self._assert_detail(self._NAME, "Timeout", "120 s")


# ---------------------------------------------------------------------------
# Crawler triggers
# ---------------------------------------------------------------------------


class TestRainOn(_Base):
    _NAME = "will rain tomorrow"

    def test_kind(self):
        self._assert_kind(self._NAME, "Rain On")

    def test_zone(self):
        self._assert_detail(self._NAME, "Zone", "4")

    def test_probability(self):
        self._assert_detail(self._NAME, "Probability", ">= 60%")


class TestRainOff(_Base):
    _NAME = "will not rain tomorrow"

    def test_kind(self):
        self._assert_kind(self._NAME, "Rain Off")

    def test_zone(self):
        self._assert_detail(self._NAME, "Zone", "4")

    def test_probability(self):
        self._assert_detail(self._NAME, "Probability", "< 60%")


if __name__ == "__main__":
    unittest.main()
