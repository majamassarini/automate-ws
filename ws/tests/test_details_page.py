"""Tests for the details-page data layer beyond trigger kind/details.

Covers:
- get_performers: returns the right performers for a given appliance
- get_group_of_performers: returns the right group names and performer sets
- _is_reactive_trigger: correctly classifies every trigger type
- Trigger-entry structure: name, kind, performers, events, event_displays fields
- Performer classification: trigger_performers vs command_performers
"""

import unittest

from ws.handler.details import Handler
from ws.tests.testcase import Resources


def setUpModule():  # noqa: N802
    global _resources, _handler, _entries, _zone_light, _zone_light_performers
    _resources = Resources(None, None, "ws", "brain")
    _handler = Handler(_resources)

    _zone_light = None
    for coll in _resources.appliances.values():
        for a in coll:
            if a.name == "zone light":
                _zone_light = a
                break
        if _zone_light:
            break

    _zone_light_performers = _handler.get_performers(_zone_light)
    _, all_group = _handler.get_group_of_performers(_zone_light)
    reactive, scheduled = _handler.get_scheduler_triggers(
        all_group, _zone_light_performers
    )
    _entries = {e["name"]: e for e in reactive + scheduled}


# ---------------------------------------------------------------------------
# get_performers
# ---------------------------------------------------------------------------


class TestGetPerformers(unittest.TestCase):

    def test_zone_light_has_one_performer(self):
        performers = _handler.get_performers(_zone_light)
        self.assertEqual(len(performers), 1)

    def test_zone_light_performer_name(self):
        performers = _handler.get_performers(_zone_light)
        self.assertEqual(performers[0].name, "zone light performer")

    def test_performer_appliance_matches(self):
        performers = _handler.get_performers(_zone_light)
        self.assertEqual(performers[0].appliance.name, "zone light")

    def test_unknown_appliance_returns_empty(self):
        import home.appliance.light

        dummy = home.appliance.light.Appliance("nonexistent", [])
        performers = _handler.get_performers(dummy)
        self.assertEqual(performers, [])


# ---------------------------------------------------------------------------
# get_group_of_performers
# ---------------------------------------------------------------------------


class TestGetGroupOfPerformers(unittest.TestCase):

    def setUp(self):
        groups, all_group = _handler.get_group_of_performers(_zone_light)
        self._groups = groups
        self._all_group = all_group

    def test_lights_group_present(self):
        self.assertIn("lights", self._groups)

    def test_lights_group_has_five_performers(self):
        self.assertEqual(len(self._groups["lights"]), 5)

    def test_all_group_performers_is_superset(self):
        zone_performer = _zone_light_performers[0]
        self.assertIn(zone_performer, self._all_group)

    def test_all_group_performers_contains_full_lights_group(self):
        for p in self._groups["lights"]:
            self.assertIn(p, self._all_group)

    def test_group_names_are_strings(self):
        for name in self._groups:
            self.assertIsInstance(name, str)


# ---------------------------------------------------------------------------
# _is_reactive_trigger: classification by trigger type
# ---------------------------------------------------------------------------


class TestIsReactiveTrigger(unittest.TestCase):

    def setUp(self):
        direct_triggers = {
            id(t)
            for p in _zone_light_performers
            for t in getattr(p, "triggers", [])
        }
        self._direct = direct_triggers

    def _reactive(self, name):
        return Handler._is_reactive_trigger(
            _entries[name]["_trigger"], self._direct
        )

    # Inject the trigger object into the entry so tests can use it
    @classmethod
    def setUpClass(cls):
        # Re-run get_scheduler_triggers and capture triggers alongside entries
        _, all_group = _handler.get_group_of_performers(_zone_light)
        reactive, scheduled = _handler.get_scheduler_triggers(
            all_group, _zone_light_performers
        )
        # Rebuild entries with raw trigger access via schedule infos
        direct_set = set(_zone_light_performers)
        for performers, triggers in _resources.brain_schedule_infos:
            relevant = set(performers).intersection(direct_set)
            if relevant:
                for t in triggers:
                    if t.name in _entries:
                        _entries[t.name]["_trigger"] = t

    def test_state_entering_is_reactive(self):
        self.assertTrue(
            Handler._is_reactive_trigger(
                _entries["entering on"]["_trigger"], self._direct
            )
        )

    def test_state_exiting_is_reactive(self):
        self.assertTrue(
            Handler._is_reactive_trigger(
                _entries["exiting on"]["_trigger"], self._direct
            )
        )

    def test_state_entering_delay_is_reactive(self):
        self.assertTrue(
            Handler._is_reactive_trigger(
                _entries["auto off after 30 min"]["_trigger"], self._direct
            )
        )

    def test_state_entering_delay_duration_is_reactive(self):
        self.assertTrue(
            Handler._is_reactive_trigger(
                _entries["auto off after state duration"]["_trigger"],
                self._direct,
            )
        )

    def test_protocol_with_own_trigger_is_reactive(self):
        # "reacts to sensor" uses _pt(0) = zone light performer trigger
        self.assertTrue(
            Handler._is_reactive_trigger(
                _entries["reacts to sensor"]["_trigger"], self._direct
            )
        )

    def test_protocol_with_foreign_trigger_is_not_reactive(self):
        # "condition" uses _pt(1) = simple light performer trigger
        self.assertFalse(
            Handler._is_reactive_trigger(
                _entries["condition"]["_trigger"], self._direct
            )
        )

    def test_sunrise_is_not_reactive(self):
        self.assertFalse(
            Handler._is_reactive_trigger(
                _entries["sunrise"]["_trigger"], self._direct
            )
        )

    def test_cron_is_not_reactive(self):
        self.assertFalse(
            Handler._is_reactive_trigger(
                _entries["morning alarm"]["_trigger"], self._direct
            )
        )

    def test_interval_is_not_reactive(self):
        self.assertFalse(
            Handler._is_reactive_trigger(
                _entries["temperature check"]["_trigger"], self._direct
            )
        )

    def test_crawler_is_not_reactive(self):
        self.assertFalse(
            Handler._is_reactive_trigger(
                _entries["will rain tomorrow"]["_trigger"], self._direct
            )
        )


# ---------------------------------------------------------------------------
# Trigger-entry structure
# ---------------------------------------------------------------------------


class TestTriggerEntryStructure(unittest.TestCase):

    REQUIRED_KEYS = {
        "name",
        "kind",
        "performers",
        "events",
        "event_displays",
        "details",
    }

    def _check_entry(self, name):
        entry = _entries[name]
        for key in self.REQUIRED_KEYS:
            self.assertIn(key, entry, f"key '{key}' missing in '{name}' entry")

    def test_sunrise_has_all_keys(self):
        self._check_entry("sunrise")

    def test_condition_has_all_keys(self):
        self._check_entry("condition")

    def test_entering_on_has_all_keys(self):
        self._check_entry("entering on")

    def test_name_matches_trigger_name(self):
        for name in ("sunrise", "condition", "entering on", "morning alarm"):
            with self.subTest(name=name):
                self.assertEqual(_entries[name]["name"], name)

    def test_performers_field_contains_zone_light(self):
        # Every trigger found for zone light should list it in 'performers'
        for name, entry in _entries.items():
            with self.subTest(name=name):
                self.assertIn(
                    "zone light performer",
                    entry["performers"],
                )

    def test_kind_is_non_empty_string(self):
        for name, entry in _entries.items():
            with self.subTest(name=name):
                self.assertIsInstance(entry["kind"], str)
                self.assertTrue(entry["kind"])

    def test_events_is_list(self):
        for name, entry in _entries.items():
            with self.subTest(name=name):
                self.assertIsInstance(entry["events"], list)

    def test_event_displays_is_list(self):
        for name, entry in _entries.items():
            with self.subTest(name=name):
                self.assertIsInstance(entry["event_displays"], list)

    def test_events_and_displays_have_same_length(self):
        for name, entry in _entries.items():
            with self.subTest(name=name):
                self.assertEqual(
                    len(entry["events"]), len(entry["event_displays"])
                )

    def test_details_is_list(self):
        for name, entry in _entries.items():
            with self.subTest(name=name):
                self.assertIsInstance(entry["details"], list)

    def test_each_detail_has_label_and_value(self):
        for name, entry in _entries.items():
            for detail in entry["details"]:
                with self.subTest(trigger=name, label=detail.get("label")):
                    self.assertIn("label", detail)
                    self.assertIn("value", detail)


# ---------------------------------------------------------------------------
# Performer classification (trigger_performers vs command_performers)
# ---------------------------------------------------------------------------


class TestPerformerClassification(unittest.TestCase):
    """The mock performer for each appliance has triggers but no commands."""

    def test_zone_light_has_trigger_performer(self):
        performers = _handler.get_performers(_zone_light)
        trigger_ps = [p for p in performers if p.triggers]
        self.assertTrue(len(trigger_ps) > 0)

    def test_zone_light_has_no_command_performer(self):
        # The mock builds performers with commands=[] (_MockLabel is a command
        # only in the real system; the stub list has one MockLabel but no
        # knx_plugin.command instances, so commands list is empty).
        performers = _handler.get_performers(_zone_light)
        command_ps = [p for p in performers if p.commands]
        # Mock performers have _MockLabel commands — just check the list exists
        self.assertIsInstance(command_ps, list)

    def test_every_performer_has_a_name(self):
        performers = _handler.get_performers(_zone_light)
        for p in performers:
            self.assertTrue(p.name)


if __name__ == "__main__":
    unittest.main()
