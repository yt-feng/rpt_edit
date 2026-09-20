#!/usr/bin/env python3
"""Pure adapter tests for the Actions-provisioned M2M100 route."""
from __future__ import annotations

import tempfile
import types
import unittest

from m2m100_offline_translation import M2M100OfflineTranslator, M2M100TranslationError, MANIFEST, MODEL_ID, REVISION


class M2M100OfflineTests(unittest.TestCase):
    def test_manifest_is_pinned_and_model_card_license_is_explicit(self):
        self.assertEqual(MANIFEST["model_id"], "facebook/m2m100_418M")
        self.assertEqual(REVISION, "55c2e61bbf05dfb8d7abccdc3fae6fc8512fd636")
        self.assertEqual(MANIFEST["model_license"], "MIT")
        self.assertEqual(MANIFEST["quantization"], "int8")
        self.assertIn("ko", {code for route in MANIFEST["routes"] for code in route})

    def test_batch_engine_receives_context_and_preserves_financial_amount(self):
        calls: list[tuple[str, str, list[str]]] = []

        class Engine:
            def translate_batch(self, texts, source, target):
                calls.append((source, target, list(texts)))
                return ["收入为" if text == "Revenue was" else "净利润下降3%。" for text in texts]

        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(
                cache_dir=directory,
                engine_factory=lambda *_args: Engine(),
                batch_size=8,
            )
            output = translator.translate("Revenue was USD 120 million and net profit declined by 3%.", "zh", "en")
        self.assertIn("USD 120 million", output)
        self.assertIn("3%", output)
        self.assertEqual(calls, [("en", "zh", ["Revenue was", "and net profit declined by 3%."])])

    def test_duplicates_in_one_batch_and_across_runs_reuse_exact_source(self):
        calls = []
        engine = types.SimpleNamespace(translate_batch=lambda texts, source, target:
            (calls.append(list(texts)) or ["收入增长" for _ in texts]))
        with tempfile.TemporaryDirectory() as directory:
            first = M2M100OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: engine)
            self.assertEqual(first.translate_many(["Revenue rose."] * 3, "zh", "en"), ["收入增长"] * 3)
            second = M2M100OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: engine)
            self.assertEqual(second.translate("Revenue rose.", "zh", "en"), "收入增长")
        self.assertEqual(calls, [["Revenue rose."]])

    def test_three_digit_decimal_cannot_become_integer(self):
        from m2m100_offline_translation import _verify_numbers
        for source, translated in (("0.125", "125"), ("1.250", "1250")):
            with self.assertRaises(M2M100TranslationError):
                _verify_numbers(source, translated)
        self.assertEqual(_verify_numbers("1,250 12.5%", "1250 12,5%"), "1,250 12.5%")

    def test_chinese_currency_scales_use_exact_arithmetic_outside_model(self):
        from m2m100_offline_translation import _protected_literal
        examples = {"1.2亿美元": "USD 120 million", "2.5万亿人民币": "CNY 2.5 trillion",
                    "350万欧元": "EUR 3.5 million", "-1.25千万港元": "HKD -12.5 million"}
        for source, expected in examples.items():
            self.assertEqual(_protected_literal(source, "zh_amount", "en"), expected)
        calls = []
        engine = types.SimpleNamespace(translate_batch=lambda texts, source, target:
            (calls.extend(texts) or ["Cash reserves were" for _ in texts]))
        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: engine)
            result = translator.translate("现金储备为1.2亿美元。", "en", "zh")
        self.assertIn("USD 120 million", result)
        self.assertNotIn("1.2", " ".join(calls))

    def test_dates_and_percentage_points_keep_units_without_neural_conversion(self):
        from m2m100_offline_translation import _protected_literal
        self.assertEqual(_protected_literal("2026年9月15日", "zh_date", "en"), "2026-09-15")
        self.assertEqual(_protected_literal("September 15, 2026", "en_date", "zh"), "2026年9月15日")
        self.assertEqual(_protected_literal("2.5 percentage points", "points", "zh"), "2.5个百分点")
        self.assertEqual(_protected_literal("2.5个百分点", "points", "en"), "2.5 percentage points")
        with self.assertRaises(M2M100TranslationError):
            _protected_literal("2026年2月30日", "zh_date", "en")

    def test_english_sentence_with_chinese_institution_is_not_skipped(self):
        calls = []
        engine = types.SimpleNamespace(translate_batch=lambda texts, source, target:
            (calls.extend(texts) or ["中国银行报告预计2026年收入增长。" for _ in texts]))
        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: engine)
            result = translator.translate("The report from 中国银行 forecasts revenue growth in 2026.", "zh")
            self.assertNotIn("The report", result)
        self.assertEqual(len(calls), 1)

    def test_numeric_changes_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(
                cache_dir=directory,
                engine_factory=lambda *_args: types.SimpleNamespace(
                    translate_batch=lambda texts, source, target: ["增长16%" for _text in texts]
                ),
            )
            with self.assertRaisesRegex(M2M100TranslationError, "numeric value"):
                translator.translate("Cash flow rose by 15% in 2026.", "zh", "en")

    def test_markdown_keeps_links_fences_and_tables(self):
        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(
                cache_dir=directory,
                engine_factory=lambda *_args: types.SimpleNamespace(
                    translate_batch=lambda texts, source, target: ["译文" for _text in texts]
                ),
            )
            source = "# Report\n\n| Metric | Value |\n| --- | --- |\n| Revenue | 42 |\n\n[Read](https://example.org/a)\n\n```python\nprint('keep')\n```\n"
            output = translator.translate_markdown(source, "zh", "en")
        self.assertIn("| --- | --- |", output)
        self.assertIn("[译文](https://example.org/a)", output)
        self.assertIn("```python\nprint('keep')\n```", output)
        self.assertIn("译文", output)

    def test_model_namespace_changes_with_manifest(self):
        self.assertIn("facebook/m2m100_418M@" + REVISION, MODEL_ID)
        self.assertIn("ct2-int8", MODEL_ID)

    def test_translate_many_groups_units_and_keeps_literal_rows(self):
        batches: list[list[str]] = []

        class Engine:
            def translate_batch(self, texts, source, target):
                batches.append(list(texts))
                return ["译" + text for text in texts]

        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(cache_dir=directory, engine_factory=lambda *_args: Engine())
            output = translator.translate_many(["Revenue rose.", "https://example.org", "Profit fell."], "zh", "en")
        self.assertEqual(output[1], "https://example.org")
        self.assertEqual(output[0], "译Revenue rose.")
        self.assertEqual(output[2], "译Profit fell.")
        self.assertEqual(batches, [["Revenue rose.", "Profit fell."]])

    def test_reviewed_operating_cash_flow_sentence_keeps_financial_semantics(self):
        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(
                cache_dir=directory,
                engine_factory=lambda *_args: types.SimpleNamespace(
                    translate_batch=lambda texts, source, target: ["任意模型输出15% 2026" for _text in texts]
                ),
            )
            self.assertEqual(
                translator.translate("Operating cash flow rose by 15% in 2026.", "ko", "en"),
                "2026년 영업 현금 흐름은 15% 증가했습니다.",
            )
            self.assertEqual(
                translator.translate("Operating cash flow rose by 15% in 2026.", "ja", "en"),
                "2026年、営業キャッシュフローは15%増加しました。",
            )

    def test_reviewed_sentence_accepts_portal_numeric_placeholders(self):
        with tempfile.TemporaryDirectory() as directory:
            translator = M2M100OfflineTranslator(
                cache_dir=directory,
                engine_factory=lambda *_args: types.SimpleNamespace(
                    translate_batch=lambda texts, source, target: [
                        "任意模型输出9370101 9370102" for _text in texts
                    ]
                ),
            )
            result = translator.translate(
                "Operating cash flow rose by __KC_PH_000__ in __KC_PH_001__", "ko", "en"
            )
        self.assertEqual(result, "__KC_PH_001__년 영업 현금 흐름은 __KC_PH_000__ 증가했습니다.")


if __name__ == "__main__":
    unittest.main()
