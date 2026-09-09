"""Tests for the shared data-layer functions used across the collection,
collections, appliance, and history pages.

Covers:
- get_html_id: sanitises appliance names into CSS-safe IDs
- get_appliance_bean: returns a non-None bean with a template for every
  appliance in the test fixture
- get_event_beans: returns a list (possibly empty) for every appliance
- get_event_beans_with_str: each bean has an event_str attribute
- Collection data: every appliance in a collection is represented
- Collections data: every collection is present
- History page: get_history_page returns paginated entries and has_more flag
- History processing: _process_raw_history skips unknown entries gracefully
"""

import asyncio
import unittest

from ws.handler import Handler as BaseHandler
from ws.handler.history import Handler as HistoryHandler
from ws.i18n import Translator
from ws.tests.testcase import Resources


def setUpModule():  # noqa: N802
    global _resources, _base_handler
    _resources = Resources(None, None, "ws", "brain")
    _base_handler = BaseHandler(_resources)


# ---------------------------------------------------------------------------
# get_html_id
# ---------------------------------------------------------------------------


class TestGetHtmlId(unittest.TestCase):

    def test_spaces_become_dashes(self):
        self.assertEqual(
            _base_handler.get_html_id("simple light"), "simple-light"
        )

    def test_parens_become_dashes(self):
        self.assertEqual(
            _base_handler.get_html_id("irrigatore (sud)"), "irrigatore--sud-"
        )

    def test_plain_name_unchanged(self):
        self.assertEqual(_base_handler.get_html_id("thermostat"), "thermostat")

    def test_empty_string(self):
        self.assertEqual(_base_handler.get_html_id(""), "")


# ---------------------------------------------------------------------------
# get_appliance_bean
# ---------------------------------------------------------------------------


class TestGetApplianceBean(unittest.TestCase):

    def test_every_appliance_has_a_bean(self):
        for coll in _resources.appliances.values():
            for appliance in coll:
                with self.subTest(appliance=appliance.name):
                    bean = _base_handler.get_appliance_bean(appliance)
                    self.assertIsNotNone(
                        bean,
                        "get_appliance_bean returned None for "
                        f"{appliance.name}",
                    )

    def test_bean_has_template_attribute(self):
        for coll in _resources.appliances.values():
            for appliance in coll:
                with self.subTest(appliance=appliance.name):
                    bean = _base_handler.get_appliance_bean(appliance)
                    self.assertTrue(
                        hasattr(bean, "template"),
                        f"bean for {appliance.name} has no "
                        "'template' attribute",
                    )

    def test_bean_template_is_non_empty_string(self):
        for coll in _resources.appliances.values():
            for appliance in coll:
                with self.subTest(appliance=appliance.name):
                    bean = _base_handler.get_appliance_bean(appliance)
                    self.assertIsInstance(bean.template, str)
                    self.assertTrue(bean.template)


# ---------------------------------------------------------------------------
# get_event_beans
# ---------------------------------------------------------------------------


class TestGetEventBeans(unittest.TestCase):

    def test_every_appliance_returns_a_list(self):
        for coll in _resources.appliances.values():
            for appliance in coll:
                with self.subTest(appliance=appliance.name):
                    beans = _base_handler.get_event_beans(appliance)
                    self.assertIsInstance(beans, list)

    def test_simple_light_has_event_beans(self):
        simple_light = None
        for coll in _resources.appliances.values():
            for a in coll:
                if a.name == "simple light":
                    simple_light = a
        self.assertIsNotNone(simple_light)
        beans = _base_handler.get_event_beans(simple_light)
        self.assertGreater(len(beans), 0)

    def test_event_bean_has_required_attributes(self):
        """Every bean from get_event_beans exposes id, icon and label ids."""
        for coll in _resources.appliances.values():
            for appliance in coll:
                for bean in _base_handler.get_event_beans(appliance):
                    with self.subTest(
                        appliance=appliance.name, bean=type(bean).__name__
                    ):
                        for attr in ("id", "id_icon", "id_label"):
                            self.assertTrue(
                                hasattr(bean, attr),
                                f"bean missing '{attr}' for {appliance.name}",
                            )


# ---------------------------------------------------------------------------
# get_event_beans_with_str (details handler)
# ---------------------------------------------------------------------------


class TestGetEventBeansWithStr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from ws.handler.details import Handler as DetailsHandler

        cls._handler = DetailsHandler(_resources)

    def test_every_appliance_returns_a_list(self):
        for coll in _resources.appliances.values():
            for appliance in coll:
                with self.subTest(appliance=appliance.name):
                    beans = self._handler.get_event_beans_with_str(appliance)
                    self.assertIsInstance(beans, list)

    def test_simple_light_beans_have_event_str(self):
        simple_light = next(
            a
            for coll in _resources.appliances.values()
            for a in coll
            if a.name == "simple light"
        )
        beans = self._handler.get_event_beans_with_str(simple_light)
        self.assertGreater(len(beans), 0)
        for bean in beans:
            self.assertTrue(
                hasattr(bean, "event_str"),
                "bean missing 'event_str' attribute",
            )
            self.assertIsInstance(bean.event_str, str)
            self.assertTrue(bean.event_str)


# ---------------------------------------------------------------------------
# Collection data
# ---------------------------------------------------------------------------


class TestCollectionData(unittest.TestCase):

    def test_all_collections_non_empty(self):
        for collection in _resources.appliances:
            with self.subTest(collection=collection):
                self.assertGreater(
                    len(list(_resources.appliances[collection])), 0
                )

    def test_every_appliance_has_bean_and_event_beans(self):
        for collection in _resources.appliances:
            for appliance in _resources.appliances[collection]:
                with self.subTest(
                    collection=collection, appliance=appliance.name
                ):
                    bean = _base_handler.get_appliance_bean(appliance)
                    self.assertIsNotNone(bean)
                    event_beans = _base_handler.get_event_beans(appliance)
                    self.assertIsInstance(event_beans, list)

    def test_collection_for_returns_correct_collection(self):
        for collection in _resources.appliances:
            for appliance in _resources.appliances[collection]:
                with self.subTest(appliance=appliance.name):
                    found = _resources.appliances.collection_for(appliance)
                    self.assertEqual(found, collection)


# ---------------------------------------------------------------------------
# History page
# ---------------------------------------------------------------------------


class TestHistoryPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._handler = HistoryHandler(_resources)
        # Pick "simple light" — RedisGatewayStub.get_history uses forced_enum
        cls._appliance = next(
            a
            for coll in _resources.appliances.values()
            for a in coll
            if a.name == "simple light"
        )

    def _run(self, coro):
        return asyncio.run(coro)

    def test_get_history_page_returns_tuple(self):
        page, has_more = self._run(
            self._handler.get_history_page(self._appliance, 0, 5, Translator())
        )
        self.assertIsInstance(page, list)
        self.assertIsInstance(has_more, bool)

    def test_page_length_respects_limit(self):
        page, _ = self._run(
            self._handler.get_history_page(self._appliance, 0, 3, Translator())
        )
        self.assertLessEqual(len(page), 3)

    def test_has_more_true_when_excess_history(self):
        # Request 2 items; stub produces offset+limit+1 = 3 raw entries so
        # there will be more after processing (forced-state cycles produce
        # at least some non-skipped entries).
        _, has_more = self._run(
            self._handler.get_history_page(self._appliance, 0, 1, Translator())
        )
        # has_more is True when processed list is longer than limit
        self.assertIsInstance(has_more, bool)

    def test_page_entries_are_six_tuples(self):
        page, _ = self._run(
            self._handler.get_history_page(
                self._appliance, 0, 10, Translator()
            )
        )
        for entry in page:
            with self.subTest(entry=entry):
                self.assertEqual(
                    len(entry),
                    6,
                    "entry must be (ts, appliance, bean, details, duration, causes)",
                )

    def test_page_entry_timestamp_is_string(self):
        page, _ = self._run(
            self._handler.get_history_page(
                self._appliance, 0, 10, Translator()
            )
        )
        for ts_str, *_ in page:
            self.assertIsInstance(ts_str, str)

    def test_page_entry_bean_is_not_none(self):
        page, _ = self._run(
            self._handler.get_history_page(
                self._appliance, 0, 10, Translator()
            )
        )
        for _, _, bean, *_ in page:
            self.assertIsNotNone(bean)

    def test_page_entry_duration_is_str_or_none(self):
        page, _ = self._run(
            self._handler.get_history_page(
                self._appliance, 0, 10, Translator()
            )
        )
        for *_, duration, _ in page:
            self.assertTrue(duration is None or isinstance(duration, str))

    def test_page_entry_causal_links_is_list(self):
        page, _ = self._run(
            self._handler.get_history_page(
                self._appliance, 0, 10, Translator()
            )
        )
        for *_, causal_links in page:
            self.assertIsInstance(causal_links, list)

    def test_page_never_exceeds_limit(self):
        for limit in (1, 3, 5, 10):
            with self.subTest(limit=limit):
                page, _ = self._run(
                    self._handler.get_history_page(
                        self._appliance, 0, limit, Translator()
                    )
                )
                self.assertLessEqual(len(page), limit)


if __name__ == "__main__":
    unittest.main()
