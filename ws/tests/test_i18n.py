"""Unit tests for ws/i18n.py.

Covers locale detection, translation, timestamp formatting, and the
end-to-end template rendering of translated strings via HTTP.
"""

import datetime
import unittest
from unittest.mock import MagicMock

from ws.i18n import (
    get_locale,
    make_translate,
    make_format_ts,
    make_format_ts_short,
    i18n_context,
)
from ws.tests.testcase import MyHomeTestCase


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fake_request(accept_language: str = ""):
    req = MagicMock()
    req.headers = {"Accept-Language": accept_language}
    return req


# ---------------------------------------------------------------------------
# Locale detection
# ---------------------------------------------------------------------------


class TestGetLocale(unittest.TestCase):

    def test_italian_exact(self):
        self.assertEqual(get_locale(_fake_request("it")), "it")

    def test_italian_with_region(self):
        self.assertEqual(get_locale(_fake_request("it-IT")), "it")

    def test_italian_with_quality(self):
        self.assertEqual(
            get_locale(_fake_request("it-IT,it;q=0.9,en;q=0.8")), "it"
        )

    def test_english_explicit(self):
        self.assertEqual(get_locale(_fake_request("en-US,en;q=0.9")), "en")

    def test_empty_header_defaults_to_english(self):
        self.assertEqual(get_locale(_fake_request("")), "en")

    def test_no_supported_language_defaults_to_english(self):
        self.assertEqual(get_locale(_fake_request("fr,de;q=0.8")), "en")

    def test_english_before_italian_returns_english(self):
        self.assertEqual(get_locale(_fake_request("en,it;q=0.5")), "en")

    def test_italian_before_english_returns_italian(self):
        self.assertEqual(get_locale(_fake_request("it,en;q=0.5")), "it")


# ---------------------------------------------------------------------------
# Translation
# ---------------------------------------------------------------------------


class TestMakeTranslate(unittest.TestCase):

    def setUp(self):
        self._en = make_translate("en")
        self._it = make_translate("it")

    def test_english_returns_key_unchanged(self):
        self.assertEqual(self._en("Collections"), "Collections")
        self.assertEqual(self._en("Load more"), "Load more")

    def test_italian_known_key(self):
        self.assertEqual(self._it("Collections"), "Collezioni")
        self.assertEqual(self._it("Today"), "Oggi")
        self.assertEqual(self._it("Yesterday"), "Ieri")
        self.assertEqual(self._it("Load more"), "Carica altro")
        self.assertEqual(self._it("Outputs"), "Uscite")
        self.assertEqual(self._it("Inputs"), "Ingressi")
        self.assertEqual(self._it("Send"), "Invia")
        self.assertEqual(self._it("All"), "Tutti")
        self.assertEqual(self._it("None"), "Nessuno")

    def test_italian_unknown_key_returns_key(self):
        self.assertEqual(self._it("Unknown string XYZ"), "Unknown string XYZ")

    def test_italian_detail_labels(self):
        self.assertEqual(
            self._it("Triggered by performer"), "Attivato dall'esecutore"
        )
        self.assertEqual(self._it("Condition A"), "Condizione A")
        self.assertEqual(self._it("Address"), "Indirizzo")
        self.assertEqual(self._it("Timeout"), "Scadenza")

    def test_italian_trigger_kinds(self):
        self.assertEqual(self._it("Sunrise"), "Alba")
        self.assertEqual(self._it("Sunset"), "Tramonto")
        self.assertEqual(self._it("Cron"), "Pianificato")
        self.assertEqual(self._it("Entering State"), "Ingresso stato")


# ---------------------------------------------------------------------------
# Timestamp formatting
# ---------------------------------------------------------------------------


class TestMakeFormatTs(unittest.TestCase):

    # Use a fixed timestamp for deterministic output.
    # datetime(2025, 3, 10, 14, 32, 1) = Monday 10 March 2025 14:32:01
    _TS = datetime.datetime(2025, 3, 10, 14, 32, 1).timestamp()

    def test_english_returns_ctime_style(self):
        fmt = make_format_ts("en")
        result = fmt(self._TS)
        # time.ctime() includes weekday abbreviation and month abbreviation
        self.assertIn("Mar", result)
        self.assertIn("2025", result)
        self.assertIn("14:32:01", result)

    def test_italian_includes_italian_month(self):
        fmt = make_format_ts("it")
        result = fmt(self._TS)
        self.assertIn("mar", result)  # Italian weekday abbrev for Monday
        self.assertIn("10", result)
        self.assertIn("2025", result)
        self.assertIn("14:32:01", result)
        # Must NOT contain English month name
        self.assertNotIn("Mar", result)

    def test_invalid_timestamp_returns_empty_string(self):
        fmt_en = make_format_ts("en")
        fmt_it = make_format_ts("it")
        self.assertEqual(fmt_en(float("inf")), "")
        self.assertEqual(fmt_it(float("inf")), "")


class TestMakeFormatTsShort(unittest.TestCase):

    def _now_and_today(self):
        now = datetime.datetime.now()
        return now, now.replace(hour=10, minute=5, second=0)

    def test_english_today_shows_time_only(self):
        fmt = make_format_ts_short("en")
        now = datetime.datetime.now()
        today_dt = now.replace(hour=9, minute=15, second=0)
        result = fmt(today_dt, now)
        self.assertEqual(result, "09:15")

    def test_english_other_day_shows_month_and_day(self):
        fmt = make_format_ts_short("en")
        now = datetime.datetime.now()
        other = now - datetime.timedelta(days=3)
        result = fmt(other, now)
        self.assertIn(other.strftime("%b"), result)

    def test_italian_today_shows_time_only(self):
        fmt = make_format_ts_short("it")
        now = datetime.datetime.now()
        today_dt = now.replace(hour=9, minute=15, second=0)
        result = fmt(today_dt, now)
        self.assertEqual(result, "09:15")

    def test_italian_other_day_shows_italian_month(self):
        fmt = make_format_ts_short("it")
        now = datetime.datetime.now()
        # Use March (3) explicitly so we know the abbreviation
        other = datetime.datetime(now.year - 1, 3, 5, 14, 0)
        result = fmt(other, now)
        self.assertIn("mar", result)  # "mar" = March abbreviation in Italian
        self.assertIn("5", result)


# ---------------------------------------------------------------------------
# i18n_context helper
# ---------------------------------------------------------------------------


class TestI18nContext(unittest.TestCase):

    def test_english_request_returns_english_translate(self):
        req = _fake_request("en")
        ctx = i18n_context(req)
        self.assertIn("_", ctx)
        self.assertIn("format_ts", ctx)
        self.assertIn("locale", ctx)
        self.assertEqual(ctx["locale"], "en")
        self.assertEqual(ctx["_"]("Collections"), "Collections")

    def test_italian_request_returns_italian_translate(self):
        req = _fake_request("it-IT,it;q=0.9")
        ctx = i18n_context(req)
        self.assertEqual(ctx["locale"], "it")
        self.assertEqual(ctx["_"]("Collections"), "Collezioni")
        self.assertEqual(ctx["_"]("Today"), "Oggi")

    def test_format_ts_callable(self):
        req = _fake_request("en")
        ctx = i18n_context(req)
        ts = datetime.datetime(2025, 6, 1, 12, 0, 0).timestamp()
        result = ctx["format_ts"](ts)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


# ---------------------------------------------------------------------------
# HTTP integration — translated strings appear in rendered pages
# ---------------------------------------------------------------------------


class TestTranslatedPages(MyHomeTestCase):
    """Smoke-test that translated strings appear when Accept-Language is set."""

    async def _get(self, path, lang="en"):
        return await self.client.request(
            "GET", path, headers={"Accept-Language": lang}
        )

    # -- Collections page --

    async def test_collections_english(self):
        r = await self._get("/collections", "en")
        self.assertEqual(r.status, 200)
        text = await r.text()
        self.assertIn("Collections", text)

    async def test_collections_italian(self):
        r = await self._get("/collections", "it")
        self.assertEqual(r.status, 200)
        text = await r.text()
        self.assertIn("Collezioni", text)
        self.assertNotIn(">Collections<", text)  # heading translated

    # -- Collection page --

    async def test_collection_italian(self):
        first_coll = next(iter(self.app.resources.appliances))
        r = await self._get(
            f"/collection/{first_coll.replace(' ', '%20')}", "it"
        )
        self.assertEqual(r.status, 200)
        text = await r.text()
        self.assertIn("Collezioni", text)  # breadcrumb

    # -- History page --

    async def test_history_english(self):
        r = await self._get("/appliance/simple%20light/history", "en")
        self.assertEqual(r.status, 200)
        text = await r.text()
        self.assertIn("Today", text)
        self.assertIn("Yesterday", text)

    async def test_history_italian(self):
        r = await self._get("/appliance/simple%20light/history", "it")
        self.assertEqual(r.status, 200)
        text = await r.text()
        self.assertIn("Oggi", text)
        self.assertIn("Ieri", text)

    # -- lang attribute on <html> --

    async def test_html_lang_english(self):
        r = await self._get("/collections", "en")
        text = await r.text()
        self.assertIn('lang="en"', text)

    async def test_html_lang_italian(self):
        r = await self._get("/collections", "it")
        text = await r.text()
        self.assertIn('lang="it"', text)


if __name__ == "__main__":
    unittest.main()
