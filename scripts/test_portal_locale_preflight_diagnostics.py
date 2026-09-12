"""Offline checks for complete, bounded preflight source diagnostics."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_portal_locales as builder


NATIVE = {
    "ko": "금융 연구의 주요 내용입니다.",
    "ja": "金融調査の主な内容です。",
    "ar": "هذا هو المحتوى الرئيسي للبحث المالي.",
}
DIAGNOSTIC_FIELDS = {
    "preflight_selected_units", "preflight_residual_units",
    "preflight_selected_units_total", "preflight_residual_units_total",
    "preflight_selected_units_truncated", "preflight_residual_units_truncated",
    "preflight_diagnostic_unit_limit", "preflight_diagnostic_source_limit",
}
ROW_FIELDS = {"locale", "batch_key", "key", "context", "source", "source_length", "source_complete", "data_placeholders"}
SECRET = "OFFLINE_CREDENTIAL_MUST_NOT_ENTER_DIAGNOSTICS"


def fixture_units(count: int) -> dict[str, builder.TranslationUnit]:
    return {
        f"{index:064x}": builder.TranslationUnit(
            f"{index:064x}", "html:text:p", f"第{index}段金融研究正文及完整行业分析内容。",
        )
        for index in range(count)
    }


class PreflightDiagnosticsTests(unittest.TestCase):
    def run_translation(self, units, provider, *, preflight=True, cache=None):
        cache = builder.empty_cache() if cache is None else cache
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json.gz"
            diagnostics = Path(directory) / "diagnostics.json"
            state = builder.TranslationRun(diagnostics, max_requests=6 if preflight else None)
            with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": SECRET}, clear=True), mock.patch.object(
                builder, "deepseek_translate_batch", side_effect=AssertionError("No real provider calls in diagnostics tests"),
            ), mock.patch.object(builder, "log"):
                error = None
                try:
                    builder.translate_missing_units(
                        units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                        base_url="https://provider.example.invalid", workers=1, timeout=1,
                        attempts=2, max_batch_items=max(1, len(units)), max_batch_chars=1_000_000,
                        batch_translator=provider, preflight_only=preflight,
                        preflight_batches_per_locale=1, run_state=state,
                    )
                except builder.TranslationError as caught:
                    error = caught
            serialized = diagnostics.read_text(encoding="utf-8")
            report = json.loads(serialized)
            self.assertEqual(report, state.data, "Persist the final diagnostic state even on failure")
            self.assertNotIn(SECRET, serialized)
            self.assertNotIn("Authorization", serialized)
            self.assertNotIn("raw_response", serialized)
            return report, builder.load_cache(path), error

    def assert_inventory(self, report, name, expected):
        rows = report[f"preflight_{name}_units"]
        self.assertEqual(report["preflight_diagnostic_unit_limit"], 192)
        self.assertEqual(report["preflight_diagnostic_source_limit"], 16384)
        self.assertEqual(report[f"preflight_{name}_units_total"], len(expected))
        self.assertEqual(report[f"preflight_{name}_units_truncated"], len(expected) > 192)
        self.assertEqual(len(rows), min(192, len(expected)))
        for row in rows:
            self.assertEqual(set(row), ROW_FIELDS)
            unit, batch_key = expected[(row["locale"], row["key"])]
            self.assertEqual(row["batch_key"], batch_key)
            self.assertEqual(row["context"], unit.context)
            self.assertEqual(row["source"], unit.source[:16384])
            self.assertEqual(row["source_length"], len(unit.source))
            self.assertIs(row["source_complete"], len(unit.source) <= 16384)
            self.assertEqual(row["data_placeholders"], list(unit.data_placeholders))
        identities = {(row["locale"], row["key"]) for row in rows}
        self.assertEqual(len(identities), len(rows), "Do not duplicate diagnostics rows")
        if len(expected) <= 192:
            self.assertEqual(identities, set(expected))

    def partial_ar_provider(self, count, *, repair_succeeds=False):
        calls = []

        def provider(locale, batch):
            calls.append((locale, len(batch)))
            translated = {unit.key: NATIVE[locale] for unit in batch}
            if locale != "ar":
                return translated
            if len(batch) == count:
                accepted = {unit.key: translated[unit.key] for unit in batch[:-5]}
                raise builder.PartialTranslationError("Five Arabic source rows remain untranslated", accepted)
            if repair_succeeds:
                return translated
            raise builder.PartialTranslationError("Grouped repair declined all five rows", {})

        return provider, calls

    def test_full_96_selected_and_five_exact_arabic_residuals_survive_declined_repair(self):
        units = fixture_units(32)
        provider, calls = self.partial_ar_provider(32)
        report, cache, error = self.run_translation(units, provider)
        self.assertIsNotNone(error)
        self.assertEqual(calls, [("ko", 32), ("ja", 32), ("ar", 32), ("ar", 5)])
        batch_key = next(iter(units))
        self.assert_inventory(report, "selected", {
            (locale, unit.key): (unit, batch_key) for locale in builder.LOCALES for unit in units.values()
        })
        self.assert_inventory(report, "residual", {
            ("ar", unit.key): (unit, batch_key) for unit in list(units.values())[-5:]
        })
        self.assertEqual({locale: len(cache["locales"][locale]) for locale in builder.LOCALES},
                         {"ko": 32, "ja": 32, "ar": 27})

    def test_residual_inventory_has_its_own_cap_so_late_arabic_rows_are_not_lost(self):
        units = fixture_units(80)
        provider, calls = self.partial_ar_provider(80)
        report, cache, _error = self.run_translation(units, provider)
        self.assertEqual(calls, [("ko", 80), ("ja", 80), ("ar", 80), ("ar", 5)])
        batch_key = next(iter(units))
        self.assert_inventory(report, "selected", {
            (locale, unit.key): (unit, batch_key) for locale in builder.LOCALES for unit in units.values()
        })
        residual = {("ar", unit.key): (unit, batch_key) for unit in list(units.values())[-5:]}
        self.assert_inventory(report, "residual", residual)
        selected_ids = {(row["locale"], row["key"]) for row in report["preflight_selected_units"]}
        self.assertTrue(set(residual).isdisjoint(selected_ids), "Fixture residuals must be beyond the selected diagnostic cap")
        self.assertEqual(len(cache["locales"]["ar"]), 75)

    def test_failure_before_later_locales_preserves_authoritative_totals_and_truncation(self):
        units = fixture_units(80)
        failure = builder.ProviderHTTPError(403, "Offline denied request")
        failure.headers = {"Authorization": SECRET}
        failure.raw_response = SECRET
        provider = mock.Mock(side_effect=failure)
        report, cache, error = self.run_translation(units, provider)
        self.assertIsNotNone(error)
        provider.assert_called_once()
        batch_key = next(iter(units))
        expected = {(locale, unit.key): (unit, batch_key) for locale in builder.LOCALES for unit in units.values()}
        self.assert_inventory(report, "selected", expected)
        self.assert_inventory(report, "residual", expected)
        self.assertEqual(report["status"], "failed")
        self.assertTrue(all(not cache["locales"][locale] for locale in builder.LOCALES))

    def test_oversized_source_retains_length_and_marks_incomplete_diagnostic_text(self):
        unit = builder.TranslationUnit(
            "a" * 64, "html:text:p", "金融研究正文" * 2800 + " __KC_PH_000__ __KC_PH_017__",
            data_placeholders=("__KC_PH_000__", "__KC_PH_017__"),
        )
        report, _cache, error = self.run_translation(
            {unit.key: unit}, mock.Mock(side_effect=builder.ProviderHTTPError(403, "Offline denied request")),
        )
        self.assertIsNotNone(error)
        self.assertGreater(len(unit.source), 16384)
        expected = {(locale, unit.key): (unit, unit.key) for locale in builder.LOCALES}
        self.assert_inventory(report, "selected", expected)
        self.assert_inventory(report, "residual", expected)
        self.assertTrue(all(not row["source_complete"] for row in report["preflight_residual_units"]))
        self.assertTrue(all(row["data_placeholders"] == ["__KC_PH_000__", "__KC_PH_017__"]
                            for row in report["preflight_residual_units"]))

    def test_successful_grouped_repair_refreshes_residuals_from_final_validated_cache(self):
        units = fixture_units(32)
        provider, calls = self.partial_ar_provider(32, repair_succeeds=True)
        report, cache, error = self.run_translation(units, provider)
        self.assertIsNone(error)
        self.assertEqual(calls[-1], ("ar", 5))
        self.assertEqual(report["preflight_selected_units_total"], 96)
        self.assert_inventory(report, "residual", {})
        self.assertEqual(report["status"], "passed")
        self.assertTrue(all(set(units) == set(cache["locales"][locale]) for locale in builder.LOCALES))

    def test_complete_cache_has_explicit_empty_preflight_inventories(self):
        units = fixture_units(2)
        cache = builder.empty_cache()
        for locale in builder.LOCALES:
            for unit in units.values():
                cache["locales"][locale][unit.key] = builder._translation_cache_row(unit, NATIVE[locale])
        provider = mock.Mock(side_effect=AssertionError("Complete cache must not call a provider"))
        report, _cache, error = self.run_translation(units, provider, cache=cache)
        self.assertIsNone(error)
        provider.assert_not_called()
        self.assert_inventory(report, "selected", {})
        self.assert_inventory(report, "residual", {})

    def test_full_translation_mode_does_not_emit_preflight_source_inventories(self):
        units = fixture_units(2)
        provider = lambda locale, batch: {unit.key: NATIVE[locale] for unit in batch}
        report, cache, error = self.run_translation(units, provider, preflight=False)
        self.assertIsNone(error)
        self.assertTrue(DIAGNOSTIC_FIELDS.isdisjoint(report))
        self.assertEqual(report["status"], "passed")
        self.assertTrue(all(set(units) == set(cache["locales"][locale]) for locale in builder.LOCALES))


if __name__ == "__main__":
    unittest.main()
