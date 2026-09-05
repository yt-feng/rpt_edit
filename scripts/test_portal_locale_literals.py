#!/usr/bin/env python3
"""Asset references do not require translation or paid repair requests."""
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import build_portal_locales as builder
from portal_locale_literals import is_latin_name_literal, is_machine_asset_reference


class AssetReferenceTests(unittest.TestCase):
    def test_real_failure_and_asset_variants_are_not_prose(self):
        for value in (
            "assets/source_image_02.jpg", "source_image_02.JPG", "../images/figure-2.webp",
            "/assets/chart.svg#plot", "./report_2026.pdf?download=1", "data/table.xlsx",
            " figure_01.png ", "assets/a%20b.avif", "archive/report.pptx",
        ):
            with self.subTest(value=value):
                self.assertTrue(is_machine_asset_reference(value))
                units = {}
                builder.collect_text_units(value, "html:attribute:alt", units)
                self.assertEqual(units, {})
                for locale in ("ko", "ja", "ar"):
                    cache = {"locales": {locale: {}}}
                    self.assertEqual(builder.translated_text(value, "html:attribute:alt", locale, cache), value)

    def test_prose_and_unknown_identifiers_are_not_exempt(self):
        for value in (
            "Learn about source.jpg", "图表 source.jpg", "source.jpg illustrates growth",
            "Bank of America Merrill Lynch", "From", "经济研究报告", "Revenue.pdf increased",
            "Report PDF", "some.unknown", "image.png\nprose", None, "", "photo.jpg;ignore",
        ):
            with self.subTest(value=value):
                self.assertFalse(is_machine_asset_reference(value))
        for value in ("Learn about source.jpg", "图表 source.jpg", "From"):
            self.assertIsNotNone(builder.unit_for_text(value, "html:attribute:alt")[1])


class LatinNameLiteralTests(unittest.TestCase):
    def test_real_company_failures_are_identity_literals(self):
        for value, context in (
            ("JD.Com Inc", "chart:keywords"),
            ("JD.Com Inc", "html:text:p"),
            ("Ping An Insurance Group Co of China Ltd", "chart:keywords"),
            ("Ping An Insurance Group Co of China Ltd", "html:text:span"),
            ("Palo Alto Networks", "chart:keywords"),
        ):
            with self.subTest(value=value, context=context):
                self.assertTrue(is_latin_name_literal(value, context))
                unit = builder.TranslationUnit("a" * 64, context, value)
                for locale in ("ko", "ja", "ar"):
                    builder.validate_translation_quality(locale, unit, value)

    def test_keyword_name_heuristic_does_not_apply_to_prose_or_title_fields(self):
        for context in ("html:text:p", "html:text:title", "html:meta:title", "chart:report:title", "jsonld:headline"):
            with self.subTest(context=context):
                self.assertFalse(is_latin_name_literal("Palo Alto Networks", context))
                unit = builder.TranslationUnit("a" * 64, context, "Palo Alto Networks")
                for locale in ("ko", "ja", "ar"):
                    with self.assertRaises(builder.TranslationError):
                        builder.validate_translation_quality(locale, unit, unit.source)

    def test_sentences_chinese_and_embedded_names_are_not_identity_literals(self):
        for value in (
            "Revenue is expected to grow this year.",
            "Revenue Increased Sharply Because Demand Improved",
            "We Expect Revenue To Grow",
            "JD.Com Inc expects revenue to grow",
            "The report covers JD.Com Inc",
            "平安保险集团", "关于 JD.Com Inc 的行业研究", "", None,
        ):
            for context in ("chart:keywords", "html:text:p", "chart:report:title"):
                with self.subTest(value=value, context=context):
                    self.assertFalse(is_latin_name_literal(value, context))
        for value in (
            "Revenue is expected to grow this year.",
            "JD.Com Inc expects revenue to grow",
            "这是需要完整翻译的中文行业研究正文和未来发展前景。",
        ):
            unit = builder.TranslationUnit("a" * 64, "chart:keywords", value)
            for locale in ("ko", "ja", "ar"):
                with self.subTest(value=value, locale=locale):
                    with self.assertRaises(builder.TranslationError):
                        builder.validate_translation_quality(locale, unit, value)

    def test_name_exemption_only_accepts_the_original_identity_not_wrong_language_copy(self):
        for name in ("JD.Com Inc", "Palo Alto Networks"):
            unit = builder.TranslationUnit("a" * 64, "chart:keywords", name)
            for output in (
                "Company Details Are Discussed Below",
                "이 회사의 사업은 계속 성장하고 있습니다.",
                "这家公司的收入正在快速增长。",
            ):
                with self.subTest(name=name, output=output):
                    with self.assertRaises(builder.TranslationError):
                        builder.validate_translation_quality("ar", unit, output)

    def test_identity_cache_provenance_survives_cross_field_rendering_but_not_sentences(self):
        source = "Palo Alto Networks"
        _protected, keyword_unit = builder.unit_for_text(source, "chart:keywords")
        _protected, body_unit = builder.unit_for_text(source, "html:text:p")
        self.assertIsNotNone(keyword_unit)
        self.assertIsNotNone(body_unit)
        self.assertEqual(keyword_unit.key, body_unit.key, "the paid source string must retain its existing shared cache key")
        row = builder._translation_cache_row(keyword_unit, source)
        self.assertIs(row.get("entity_name"), True)
        for locale in ("ko", "ja", "ar"):
            with self.subTest(locale=locale):
                self.assertTrue(builder._valid_cache_row(locale, body_unit, row))
                cache = builder.empty_cache()
                cache["locales"][locale][keyword_unit.key] = row.copy()
                self.assertEqual(builder.translated_text(source, "html:text:p", locale, cache), source)
                self.assertFalse(builder._valid_cache_row(locale, body_unit, {**row, "source": source + " report"}))
                sentence = "Palo Alto Networks expects revenue to grow."
                with self.assertRaises(builder.TranslationError):
                    builder.translated_text(sentence, "html:text:p", locale, cache)

    def test_html_first_dedup_retains_later_keyword_identity_context(self):
        source = "Palo Alto Networks"
        units = {}
        builder.collect_text_units(source, "html:text:p", units)
        original = next(iter(units.values()))
        self.assertEqual(original.context, "html:text:p")
        builder.collect_text_units(source, "chart:keywords", units)
        builder.collect_text_units(source, "html:meta:title", units)
        self.assertEqual(len(units), 1)
        merged = units[original.key]
        self.assertEqual(merged.context, "chart:keywords")
        self.assertEqual(merged.source, source)
        for locale in ("ko", "ja", "ar"):
            builder.validate_translation_quality(locale, merged, source)
        self.assertIs(builder._translation_cache_row(merged, source).get("entity_name"), True)
        wrong = builder._translation_cache_row(merged, "Company Details Are Discussed Below")
        self.assertIsNot(wrong.get("entity_name"), True)
        self.assertFalse(builder._valid_cache_row("ar", merged, wrong))

    def test_existing_identity_cache_upgrades_in_prune_and_preserved_inventory_without_calls(self):
        source = "Palo Alto Networks"
        _protected, unit = builder.unit_for_text(source, "chart:keywords")
        units = {unit.key: unit}
        for mode in ("prune", "preserve_unused"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                cache = builder.empty_cache()
                for locale in builder.LOCALES:
                    cache["locales"][locale][unit.key] = {"source": source, "translation": source}
                    cache["locales"][locale]["f" * 64] = {"source": "History sentinel", "translation": "History sentinel"}
                provider = mock.Mock(side_effect=AssertionError("An already paid identity must never be translated again"))
                if mode == "prune":
                    counts = builder.prune_translation_cache(cache, units)
                    for locale in builder.LOCALES:
                        self.assertEqual(counts[locale], {"retained": 1, "stale": 1, "invalid": 0})
                else:
                    state = builder.TranslationRun()
                    path = Path(directory) / "cache.json.gz"
                    with mock.patch.dict("os.environ", {}, clear=True), mock.patch.object(builder, "log"):
                        missing = builder.translate_missing_units(
                            units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                            base_url="https://api.deepseek.com", workers=500, timeout=1, attempts=2,
                            batch_translator=provider, preserve_unused_cache=True, run_state=state,
                        )
                    self.assertEqual(missing, {locale: 0 for locale in builder.LOCALES})
                    self.assertEqual(state.data["status"], "passed")
                    self.assertEqual(state.data["provider_requests"], 0)
                    cache = builder.load_cache(path)
                    for locale in builder.LOCALES:
                        self.assertIn("f" * 64, cache["locales"][locale])
                provider.assert_not_called()
                for locale in builder.LOCALES:
                    self.assertIs(cache["locales"][locale][unit.key].get("entity_name"), True)
                    self.assertEqual(builder.translated_text(source, "html:text:p", locale, cache), source)


if __name__ == "__main__":
    unittest.main()
