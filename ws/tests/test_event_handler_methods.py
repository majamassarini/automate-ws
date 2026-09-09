"""Tests for event-handler methods that are not exercised by the HTTP-level
tests because the relevant appliance types or event values are absent from
the test fixture.

Covers: motion, scene, power-production-duration, clima-season handlers
(_get_str, get_icon, get_description) and the int/float/str appliance-event
handler post() and utility methods.
"""

import asyncio
import unittest

import home

from ws.handler.event.enum.motion import Handler as MotionHandler
from ws.handler.event.enum.scene import Handler as SceneHandler
from ws.handler.event.enum.power.production.duration import (
    Handler as PowerProductionDurationHandler,
)
from ws.handler.event.enum.clima.season import Handler as SeasonHandler
from ws.handler.event import int as int_handler
from ws.handler.event.appliance.event import int as appliance_int_handler
from ws.handler.event.appliance.event import float as appliance_float_handler
from ws.handler.event.appliance.event import str as appliance_str_handler
from ws.authorization import Policy, check_credentials


# ---------------------------------------------------------------------------
# Handlers that need no meaningful resources for the tested methods
# ---------------------------------------------------------------------------

_H = None  # dummy resources — not used by the methods under test


# ---------------------------------------------------------------------------
# Motion handler
# ---------------------------------------------------------------------------


class TestMotionHandler(unittest.TestCase):

    def setUp(self):
        self.h = MotionHandler(_H)

    def test_get_str_spotted(self):
        self.assertEqual(
            self.h._get_str(home.event.motion.Event.Spotted), self.h.YES
        )

    def test_get_str_missed(self):
        self.assertEqual(
            self.h._get_str(home.event.motion.Event.Missed), self.h.NO
        )

    def test_get_description_spotted(self):
        self.assertEqual(
            self.h.get_description(home.event.motion.Event.Spotted),
            self.h.MOTION,
        )

    def test_get_description_missed(self):
        self.assertEqual(
            self.h.get_description(home.event.motion.Event.Missed),
            self.h.NOMOTION,
        )

    def test_get_icon_spotted(self):
        self.assertEqual(
            self.h.get_icon(home.event.motion.Event.Spotted), "ti ti-run"
        )

    def test_get_icon_missed(self):
        self.assertEqual(
            self.h.get_icon(home.event.motion.Event.Missed), "ti ti-eye-off"
        )

    def test_get_icon_unknown_returns_event(self):
        sentinel = object()
        self.assertIs(self.h.get_icon(sentinel), sentinel)


# ---------------------------------------------------------------------------
# Scene handler
# ---------------------------------------------------------------------------


class TestSceneHandler(unittest.TestCase):

    def setUp(self):
        self.h = SceneHandler(_H)

    def test_get_str_triggered(self):
        self.assertEqual(
            self.h._get_str(home.event.scene.Event.Triggered), "playing"
        )

    def test_get_str_untriggered(self):
        self.assertEqual(
            self.h._get_str(home.event.scene.Event.Untriggered), "stopped"
        )

    def test_get_str_unknown_returns_event(self):
        sentinel = object()
        self.assertIs(self.h._get_str(sentinel), sentinel)

    def test_get_icon_triggered(self):
        self.assertEqual(
            self.h.get_icon(home.event.scene.Event.Triggered),
            "ti ti-player-play",
        )

    def test_get_icon_untriggered(self):
        self.assertEqual(
            self.h.get_icon(home.event.scene.Event.Untriggered),
            "ti ti-player-stop",
        )

    def test_get_icon_unknown_returns_event(self):
        sentinel = object()
        self.assertIs(self.h.get_icon(sentinel), sentinel)


# ---------------------------------------------------------------------------
# Power production duration handler
# ---------------------------------------------------------------------------


class TestPowerProductionDurationHandler(unittest.TestCase):

    def setUp(self):
        self.h = PowerProductionDurationHandler(_H)
        self.Short = home.event.power.production.duration.Event.Short
        self.Long = home.event.power.production.duration.Event.Long

    def test_get_str_short(self):
        self.assertEqual(self.h._get_str(self.Short), "since short time")

    def test_get_str_long(self):
        self.assertEqual(self.h._get_str(self.Long), "since long time")

    def test_get_str_unknown(self):
        sentinel = object()
        self.assertIs(self.h._get_str(sentinel), sentinel)

    def test_get_icon_short(self):
        self.assertEqual(self.h.get_icon(self.Short), "ti ti-hourglass-low")

    def test_get_icon_long(self):
        self.assertEqual(self.h.get_icon(self.Long), "ti ti-hourglass-high")

    def test_get_icon_unknown(self):
        sentinel = object()
        self.assertIs(self.h.get_icon(sentinel), sentinel)


# ---------------------------------------------------------------------------
# Clima season handler
# ---------------------------------------------------------------------------


class TestSeasonHandler(unittest.TestCase):

    def setUp(self):
        self.h = SeasonHandler(_H)
        E = home.event.clima.season.Event
        self.Winter = E.Winter
        self.Summer = E.Summer
        self.Spring = E.Spring
        self.Fall = E.Fall

    def test_get_str_winter(self):
        self.assertEqual(self.h._get_str(self.Winter), "winter")

    def test_get_str_summer(self):
        self.assertEqual(self.h._get_str(self.Summer), "summer")

    def test_get_str_spring(self):
        self.assertEqual(self.h._get_str(self.Spring), "sprint")

    def test_get_str_fall(self):
        self.assertEqual(self.h._get_str(self.Fall), "fall")

    def test_get_str_unknown(self):
        sentinel = object()
        self.assertIs(self.h._get_str(sentinel), sentinel)

    def test_get_icon_winter(self):
        self.assertEqual(self.h.get_icon(self.Winter), "ti ti-snowflake")

    def test_get_icon_summer(self):
        self.assertEqual(self.h.get_icon(self.Summer), "ti ti-sun-wind")

    def test_get_icon_spring(self):
        self.assertEqual(self.h.get_icon(self.Spring), "ti ti-plant")

    def test_get_icon_fall(self):
        self.assertEqual(self.h.get_icon(self.Fall), "ti ti-leaf")

    def test_get_icon_unknown(self):
        sentinel = object()
        self.assertIs(self.h.get_icon(sentinel), sentinel)


# ---------------------------------------------------------------------------
# int.Handler (ws/handler/event/int.py)
#
# Sentinel KLASS types are used so that the global event-handler registry is
# not polluted with entries that conflict with real handlers registered
# under (None, int) / (None, float) / (None, str).
# ---------------------------------------------------------------------------


class _SentinelInt(int):
    """Unique subclass used as KLASS so it never collides in the registry."""


class _SentinelFloat(float):
    """Unique subclass used as KLASS for float handler tests."""


class _SentinelStr(str):
    """Unique subclass used as KLASS for str handler tests."""


class _ConcreteIntHandler(int_handler.Handler):
    """Minimal concrete subclass of the base int.Handler."""

    KLASS = _SentinelInt
    TEMPLATE = "event/int.html"
    LABEL = "Value:"

    def get(self, event):
        return int_handler.Bean(
            self.LABEL,
            self.get_module_str(),
            self.get_class_str(),
            self.TEMPLATE,
            self.get_icon(event),
            event,
        )

    def post(self, request_data):
        return self.KLASS(request_data["value"])


class TestIntHandler(unittest.TestCase):

    def setUp(self):
        self.h = _ConcreteIntHandler(_H)

    def test_get_returns_bean_with_value(self):
        bean = self.h.get(42)
        self.assertEqual(bean.value, 42)

    def test_get_description(self):
        self.assertEqual(self.h.get_description(7), "7")

    def test_get_description_for_index(self):
        self.assertEqual(self.h.get_description_for_index(3), "3")

    def test_get_icon_returns_empty_string(self):
        self.assertEqual(self.h.get_icon(0), "")

    def test_post(self):
        result = self.h.post({"value": 5})
        self.assertEqual(result, 5)


# ---------------------------------------------------------------------------
# appliance event int/float/str post() methods
# ---------------------------------------------------------------------------


class _ConcreteApplianceIntHandler(appliance_int_handler.Handler):
    KLASS = _SentinelInt
    TEMPLATE = "event/int.html"
    LABEL = "Value:"


class _ConcreteApplianceFloatHandler(appliance_float_handler.Handler):
    KLASS = _SentinelFloat  # type: ignore[assignment]
    TEMPLATE = "event/int.html"
    LABEL = "Value:"


class _ConcreteApplianceStrHandler(appliance_str_handler.Handler):
    KLASS = _SentinelStr  # type: ignore[assignment]
    TEMPLATE = "event/int.html"
    LABEL = "Value:"


class TestApplianceEventHandlers(unittest.TestCase):

    def test_int_post_converts_to_int(self):
        h = _ConcreteApplianceIntHandler(_H)
        result = h.post({"value": "42"})
        self.assertEqual(result, 42)
        self.assertIsInstance(result, int)

    def test_float_post_converts_to_float(self):
        h = _ConcreteApplianceFloatHandler(_H)
        result = h.post({"value": "3.14"})
        self.assertAlmostEqual(result, 3.14)
        self.assertIsInstance(result, float)

    def test_str_post_returns_string(self):
        h = _ConcreteApplianceStrHandler(_H)
        result = h.post({"value": "hello"})
        self.assertEqual(result, "hello")
        self.assertIsInstance(result, str)

    def test_int_get_icon_returns_none(self):
        h = _ConcreteApplianceIntHandler(_H)
        self.assertIsNone(h.get_icon(42))

    def test_int_get_description_for_index(self):
        h = _ConcreteApplianceIntHandler(_H)
        self.assertEqual(h.get_description_for_index(7), "7")


# ---------------------------------------------------------------------------
# Authorization policy and check_credentials
# ---------------------------------------------------------------------------


class TestPolicy(unittest.TestCase):

    def setUp(self):
        self.policy = Policy()

    def _run(self, coro):
        return asyncio.run(coro)

    def test_authorized_userid_known_user(self):
        uid = self._run(self.policy.authorized_userid("admin"))
        self.assertEqual(uid, "admin")

    def test_authorized_userid_unknown_returns_none(self):
        uid = self._run(self.policy.authorized_userid("nobody"))
        self.assertIsNone(uid)

    def test_admin_has_configure_permission(self):
        result = self._run(
            self.policy.permits("admin", Policy.CONFIGURE_PERMISSION)
        )
        self.assertTrue(result)

    def test_user_has_no_configure_permission(self):
        result = self._run(
            self.policy.permits("user", Policy.CONFIGURE_PERMISSION)
        )
        self.assertFalse(result)

    def test_user_has_edit_permission(self):
        result = self._run(self.policy.permits("user", Policy.EDIT_PERMISSION))
        self.assertTrue(result)

    def test_anonymous_has_view_permission(self):
        result = self._run(
            self.policy.permits("anonymous", Policy.VIEW_PERMISSION)
        )
        self.assertTrue(result)

    def test_anonymous_has_no_edit_permission(self):
        result = self._run(
            self.policy.permits("anonymous", Policy.EDIT_PERMISSION)
        )
        self.assertFalse(result)

    def test_unknown_identity_has_no_permission(self):
        result = self._run(
            self.policy.permits("ghost", Policy.VIEW_PERMISSION)
        )
        self.assertFalse(result)

    def test_custom_credentials_accepted(self):
        p = Policy(credentials={"alice": "pass123"})
        uid = self._run(p.authorized_userid("alice"))
        self.assertEqual(uid, "alice")

    def test_custom_credentials_unknown_rejected(self):
        p = Policy(credentials={"alice": "pass123"})
        uid = self._run(p.authorized_userid("bob"))
        self.assertIsNone(uid)


class TestCheckCredentials(unittest.TestCase):

    def _run(self, coro):
        return asyncio.run(coro)

    def test_correct_credentials_accepted(self):
        creds = {"admin": "secret"}
        self.assertTrue(self._run(check_credentials(creds, "admin", "secret")))

    def test_wrong_password_rejected(self):
        creds = {"admin": "secret"}
        self.assertFalse(self._run(check_credentials(creds, "admin", "wrong")))

    def test_unknown_user_rejected(self):
        creds = {"admin": "secret"}
        self.assertFalse(self._run(check_credentials(creds, "nobody", "x")))


if __name__ == "__main__":
    unittest.main()
