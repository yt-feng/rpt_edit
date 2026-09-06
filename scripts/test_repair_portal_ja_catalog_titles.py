"""Offline regression coverage for reviewed JA title cache repairs."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import build_portal_locales as builder
from repair_portal_ja_catalog_titles import apply_ja_catalog_title_repairs, load_repairs


class JapaneseTitleRepairTests(unittest.TestCase):
    def setUp(self):
        self.repairs = load_repairs()
        self.row = self.repairs[0]
        self.units = {
            row["unit_key"]: builder.unit_for_text(row["source_title"], "catalog:title")[1]
            for row in self.repairs
        }
        self.cache = builder.empty_cache()

    def test_reviewed_inventory_matches_current_builder_keys_and_placeholders(self):
        self.assertEqual(len(self.repairs), 14)
        self.assertEqual(len({row["report_id"] for row in self.repairs}), 13)
        for row in self.repairs:
            with self.subTest(report=row["report_id"], source=row["source_title"]):
                protected, unit = builder.unit_for_text(row["source_title"], "catalog:title")
                self.assertEqual(unit.key, row["unit_key"])
                self.assertEqual(unit.source, row["source"])
                builder.validate_translation_quality("ja", unit, row["translation"])
                self.assertEqual(protected.restore(row["translation"]), row["translation_title"])
                self.assertRegex(row["translation_title"], r"[\u3040-\u30ff]")

    def test_observed_errors_match_both_protected_and_literal_provider_numbers(self):
        for row in self.repairs:
            protected, unit = builder.unit_for_text(row["source_title"], "catalog:title")
            for observed in row["observed_translations"]:
                with self.subTest(report=row["report_id"], observed=observed):
                    self.assertEqual(protected.restore(observed), row["observed_title"])
                    self.cache["locales"]["ja"][unit.key] = {"source": unit.source, "translation": observed}
                    result = apply_ja_catalog_title_repairs(self.cache, self.units, repairs=[row])
                    self.assertEqual(result["replaced"], 1)
                    self.assertEqual(self.cache["locales"]["ja"][unit.key]["translation"], row["translation"])

    def test_replaces_only_reviewed_error_and_preserves_cache_provenance(self):
        row = self.row
        self.cache["locales"]["ja"][row["unit_key"]] = {
            "source": row["source"], "translation": row["observed_translations"][0],
            "provenance": "existing paid cache",
        }
        result = apply_ja_catalog_title_repairs(self.cache, self.units, repairs=[row])
        self.assertEqual(result, {"replaced": 1, "seeded": 0, "preserved": 0, "unmatched": 0})
        fixed = self.cache["locales"]["ja"][row["unit_key"]]
        self.assertEqual(fixed["translation"], row["translation"])
        self.assertEqual(fixed["provenance"], "existing paid cache")

    def test_missing_rows_are_seeded_and_repeat_application_is_idempotent(self):
        result = apply_ja_catalog_title_repairs(self.cache, self.units)
        self.assertEqual(result["seeded"], 14)
        snapshot = copy.deepcopy(self.cache)
        result = apply_ja_catalog_title_repairs(self.cache, self.units)
        self.assertEqual(result["preserved"], 14)
        self.assertEqual(self.cache, snapshot)

    def test_unknown_or_improved_japanese_is_not_overwritten(self):
        for value in ("既に確認済みの別の日本語訳", self.row["translation"], "未確認の既存訳"):
            with self.subTest(value=value):
                previous = {"source": self.row["source"], "translation": value}
                self.cache["locales"]["ja"][self.row["unit_key"]] = previous
                result = apply_ja_catalog_title_repairs(self.cache, self.units, repairs=[self.row])
                self.assertEqual(result["preserved"], 1)
                self.assertIs(self.cache["locales"]["ja"][self.row["unit_key"]], previous)

    def test_unrelated_paid_cache_other_locales_and_source_inventory_are_unchanged(self):
        for locale in self.cache["locales"]:
            self.cache["locales"][locale]["f" * 64] = {"source": "unused historical source", "translation": "paid value"}
        before = copy.deepcopy(self.cache)
        units_before = copy.deepcopy(self.units)
        apply_ja_catalog_title_repairs(self.cache, self.units)
        for locale in ("ko", "ar"):
            self.assertEqual(self.cache["locales"][locale], before["locales"][locale])
        self.assertEqual(self.cache["locales"]["ja"]["f" * 64], before["locales"]["ja"]["f" * 64])
        self.assertEqual(self.units, units_before)

    def test_only_current_source_and_key_pairs_can_be_repaired(self):
        key = self.row["unit_key"]
        for units in ({}, {key: SimpleNamespace(key=key, source="changed source")},
                      {key: SimpleNamespace(key="0" * 64, source=self.row["source"])},
                      {"0" * 64: SimpleNamespace(key="0" * 64, source=self.row["source"])}):
            with self.subTest(units=units):
                result = apply_ja_catalog_title_repairs(self.cache, units, repairs=[self.row])
                self.assertEqual(result["unmatched"], 1)
                self.assertEqual(self.cache["locales"]["ja"], {})

    def test_corrupt_existing_source_is_not_silently_replaced(self):
        self.cache["locales"]["ja"][self.row["unit_key"]] = {
            "source": "another source", "translation": self.row["observed_translations"][0],
        }
        before = copy.deepcopy(self.cache)
        result = apply_ja_catalog_title_repairs(self.cache, self.units, repairs=[self.row])
        self.assertEqual(result["preserved"], 1)
        self.assertEqual(self.cache, before)

    def test_no_script_detection_overrides_valid_kanji_title(self):
        source = "JPM-China Logistics, Express Parcel and Ecommerce-260903"
        _, unit = builder.unit_for_text(source, "catalog:title")
        row = {"source": unit.source, "translation": "JPM-中国物流、宅配便、電子商取引-__KC_PH_000__"}
        self.cache["locales"]["ja"][unit.key] = row
        apply_ja_catalog_title_repairs(self.cache, {unit.key: unit})
        self.assertIs(self.cache["locales"]["ja"][unit.key], row)

    def test_fixed_rows_render_for_catalog_html_and_reused_numeric_tokens_without_apis(self):
        apply_ja_catalog_title_repairs(self.cache, self.units)
        for row in self.repairs:
            with self.subTest(source=row["source_title"]):
                for context in ("catalog:title", "html:text:h1", "jsonld:headline"):
                    self.assertEqual(builder.translated_text(row["source_title"], context, "ja", self.cache), row["translation_title"])
        next_date = self.row["source_title"].replace("260902", "260906")
        self.assertEqual(builder.translated_text(next_date, "catalog:title", "ja", self.cache),
                         self.row["translation_title"].replace("260902", "260906"))

    def test_hsbc_catalog_and_chinese_source_detail_have_same_japanese_title(self):
        rows = [row for row in self.repairs if row["report_id"] == "69a8d73da74f01a2f1756ac3"]
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["translation_title"], rows[1]["translation_title"])
        self.assertNotEqual(rows[0]["unit_key"], rows[1]["unit_key"])

    def test_invalid_repair_data_is_rejected(self):
        for change in ("schema", "duplicate", "placeholder", "same_translation"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temp:
                payload = {"schema_version": 1, "locale": "ja", "repairs": [copy.deepcopy(self.row)]}
                if change == "schema":
                    payload["locale"] = "ko"
                elif change == "duplicate":
                    payload["repairs"].append(copy.deepcopy(self.row))
                elif change == "placeholder":
                    payload["repairs"][0]["translation"] = "別の日本語"
                else:
                    payload["repairs"][0]["observed_translations"] = [self.row["translation"]]
                path = Path(temp) / "repairs.json"
                path.write_text(json.dumps(payload), encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_repairs(path)


if __name__ == "__main__":
    unittest.main()
