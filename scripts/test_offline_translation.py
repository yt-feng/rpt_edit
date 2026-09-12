#!/usr/bin/env python3
"""Structural and offline-boundary tests, requiring no installed neural models."""
import importlib.metadata
import json
from pathlib import Path
import re
import tempfile
import types
import unittest
from unittest.mock import patch
import zipfile

from offline_translation import OfflineTranslator, OfflineTranslationError, _ArgosEngine, split_text
from install_offline_translation_models import inspect_archive, install_one, selected_models


class FakeEngine:
    def __init__(self, calls, pair):
        self.calls, self.pair = calls, pair

    def translate(self, text):
        self.calls.append((*self.pair, text))
        return "译{" + text.lower() + "}"


class OfflineTranslationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.calls = []
        self.translator = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda source, target: FakeEngine(self.calls, (source, target)))

    def test_structure_is_protected_but_quantities_keep_context(self):
        text = 'Growth __KC_PH_000__ for $AAPL is $1,234.50 (+12.5%) [[PORTAL_IMAGE_001]] <b data-x="42">forecast</b> https://example.com/a?q=2'
        output = self.translator.translate(text, "zh", "en")
        for value in ["__KC_PH_000__", "$AAPL", "[[PORTAL_IMAGE_001]]", '<b data-x="42">', "</b>", "https://example.com/a?q=2"]:
            self.assertIn(value, output)
            self.assertFalse(any(value in call[2] for call in self.calls), value)
        for amount in ["$1,234.50", "+12.5%"]:
            self.assertIn(amount, output)
            self.assertTrue(any(amount in call[2] for call in self.calls))
        self.assertIn("growth", output)

    def test_cash_flow_sentence_reaches_model_with_percent_and_year(self):
        sentence = "Operating cash flow rose by 15% in 2026."
        translated = "2026年经营现金流增长了15%。"

        def contextual(text):
            self.assertEqual(text, sentence, "Translation lost the sentence context around quantities")
            return translated

        engine = types.SimpleNamespace(translate=contextual)
        translator = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda *_args: engine)
        self.assertEqual(translator.translate(sentence, "zh", "en"), translated)

    def test_placeholders_keep_sentence_context_and_can_reorder(self):
        sentence = "Revenue rose by __KC_PH_000__ in __KC_PH_001__."

        def contextual(text):
            self.assertRegex(text, r"^Revenue rose by \d+ in \d+\.$")
            first, second = re.findall(r"\d+", text)
            return f"{second}年营收增长{first}。"

        translator = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda *_args: types.SimpleNamespace(translate=contextual))
        self.assertEqual(translator.translate(sentence, "zh", "en"), "__KC_PH_001__年营收增长__KC_PH_000__。")

    def test_changed_missing_or_repeated_numeric_values_are_rejected(self):
        for altered in ["2026年现金流增加。", "2026年现金流增长16%。", "2026年2026年现金流增长15%。"]:
            with self.subTest(altered=altered):
                translator = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda *_args: types.SimpleNamespace(translate=lambda _text: altered))
                with self.assertRaisesRegex(OfflineTranslationError, "numeric value"):
                    translator.translate("Cash flow rose by 15% in 2026.", "zh", "en")

    def test_identical_language_preserves_original_and_skips_engine(self):
        text = "现金流 __KC_PH_000__ 和 12.5%\n<tag>  字符串  </tag>"
        self.assertEqual(self.translator.translate(text, "zh-CN", "zh"), text)
        self.assertEqual(self.calls, [])

    def test_numeric_spellings_restored_after_safe_grouping_changes(self):
        engine = types.SimpleNamespace(translate=lambda _text: "增长 ١٢.٥ %，达到1234.50。")
        translator = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda *_args: engine)
        self.assertEqual(translator.translate("Growth of 12.5% to 1,234.50.", "zh", "en"), "增长 12.5%，达到1,234.50。")

    def test_arabic_percent_and_separators_restore_exact_source_spelling(self):
        engine = types.SimpleNamespace(translate=lambda _text: "نمو ١٢٫٥٪ إلى ١٬٢٣٤٫٥٠.")
        translator = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda *_args: engine)
        self.assertEqual(translator.translate("Growth of 12.5% to 1,234.50.", "ar", "en"), "نمو 12.5% إلى 1,234.50.")

    def test_m2m100_backend_keeps_full_currency_scale_opaque(self):
        calls = []

        def contextual(text):
            calls.append(text)
            return "收入为 " if text == "Revenue was" else "净利润下降3%。"

        translator = OfflineTranslator(
            cache_dir=self.temp.name,
            backend="m2m100",
            engine_factory=lambda *_args: types.SimpleNamespace(translate=contextual),
        )
        output = translator.translate("Revenue was USD 120 million and net profit declined by 3%.", "zh", "en")
        self.assertIn("USD 120 million", output)
        self.assertEqual(calls, ["Revenue was", "and net profit declined by 3%."])
        self.assertEqual(translator.model_id.split(":", 1)[0].split("-")[0], "m2m100")

    def test_allcaps_prose_is_translated_and_explicit_codes_preserved(self):
        output = self.translator.translate("REVENUE / OPERATING CASH FLOW in USD for NASDAQ:AAPL and BRK.B", "zh", "en")
        self.assertIn("译{revenue / operating cash flow in}", output)
        for code in ["USD", "NASDAQ:AAPL", "BRK.B"]:
            self.assertIn(code, output)
            self.assertFalse(any(code in call[2] for call in self.calls))

    def test_markdown_preserves_structure_and_code(self):
        markdown = '# Report\n\n| Metric | Value |\n| :--- | ---: |\n| Sales | 42 |\n\n- [Read report](https://example.com/a_(b))\n![Chart](images/chart.png)\nFormula $x^2 + y^2$ and ``keep ` backtick``\n\n```python\nprint("DO NOT translate", 42)\n```\n<script>\nconst hello = "unchanged";\n</script>\n    code = "unchanged"\n'
        output = self.translator.translate_markdown(markdown)
        self.assertEqual(output.count("\n"), markdown.count("\n"))
        self.assertEqual(output.count("|"), markdown.count("|"))
        for literal in ['# ', '| :--- | ---: |', '](https://example.com/a_(b))', '![Chart](images/chart.png)', '$x^2 + y^2$', '``keep ` backtick``', '```python\nprint("DO NOT translate", 42)\n```', '<script>\nconst hello = "unchanged";\n</script>', '    code = "unchanged"']:
            self.assertIn(literal, output)
        self.assertIn("译{read report}", output)

    def test_split_is_lossless_for_oversize_unbroken_text(self):
        text = "报告研究" * 800 + ". final sentence with spaces. " * 30
        chunks = split_text(text)
        self.assertEqual("".join(chunks), text)
        self.assertTrue(all(len(chunk) <= 240 for chunk in chunks))
        unique_text = "".join(chr(0x4E00 + index) for index in range(1700)) + "终"
        self.translator.translate(unique_text, "en", "zh")
        self.assertEqual("".join(call[2] for call in self.calls), unique_text)

    def test_token_limit_rechunks_without_truncation(self):
        engine = _ArgosEngine.__new__(_ArgosEngine)
        engine.package = types.SimpleNamespace(target_prefix="", tokenizer=types.SimpleNamespace(encode=list, decode=lambda tokens: "".join(tokens)))
        received = []

        def translate_batch(batches, **kwargs):
            self.assertEqual(kwargs["max_input_length"], 0)
            self.assertLessEqual(len(batches[0]), 192)
            received.extend(batches[0])
            return [types.SimpleNamespace(hypotheses=[batches[0]])]

        engine.model = types.SimpleNamespace(translate_batch=translate_batch)
        text = "研" * 900 + "终"
        self.assertEqual(engine.translate(text), text)
        self.assertEqual("".join(received), text)

    def test_decoder_output_limit_fails_instead_of_returning_truncation(self):
        engine = _ArgosEngine.__new__(_ArgosEngine)
        engine.package = types.SimpleNamespace(target_prefix="", tokenizer=types.SimpleNamespace(encode=list, decode=lambda tokens: "".join(tokens)))
        engine.model = types.SimpleNamespace(translate_batch=lambda *args, **kwargs: [types.SimpleNamespace(hypotheses=[["x"] * 1024])])
        with self.assertRaisesRegex(OfflineTranslationError, "output limit"):
            engine.translate("hello")

    def test_persistent_exact_cache_and_language_separation(self):
        expected = self.translator.translate("Growth forecast", "zh", "en")
        replay = OfflineTranslator(cache_dir=self.temp.name, engine_factory=lambda *args: self.fail("Engine must not load on a cache hit"))
        self.assertEqual(replay.translate("Growth forecast", "zh", "en"), expected)
        self.assertEqual(replay.stats["cache_hits"], 1)
        self.translator.translate("Growth forecast", "ja", "en")
        self.translator.translate("Growth Forecast", "zh", "en")
        self.assertEqual(len(self.calls), 3)
        entries = list(Path(self.temp.name).rglob("*.json"))
        self.assertEqual(len(entries), 3)
        audit = json.loads(entries[0].read_text())
        self.assertEqual(audit["provider"], "argos-offline")
        self.assertEqual(len(audit["source_sha256"]), 64)
        self.assertIn("model", audit)

    def test_invalid_cache_is_recomputed(self):
        self.translator.translate("Report", "zh", "en")
        path = next(Path(self.temp.name).rglob("*.json"))
        path.write_text('{"translation":"tampered"}')
        self.assertEqual(self.translator.translate("Report", "zh", "en"), "译{report}")
        self.assertEqual(len(self.calls), 2)

    def test_blank_cache_entry_is_recomputed(self):
        self.translator.translate("Report", "zh", "en")
        path = next(Path(self.temp.name).rglob("*.json"))
        audit = json.loads(path.read_text())
        audit["translation"] = "   "
        path.write_text(json.dumps(audit))
        self.assertEqual(self.translator.translate("Report", "zh", "en"), "译{report}")
        self.assertEqual(len(self.calls), 2)

    def test_mixed_source_routes_english_and_chinese_separately(self):
        output = self.translator.translate("研究 Growth outlook", "zh")
        self.assertIn("研究", output)
        self.assertEqual(self.calls, [("en", "zh", "Growth outlook")])
        self.calls.clear()
        self.translator.translate("研究 New outlook", "ja")
        pairs = [(source, target) for source, target, _ in self.calls]
        self.assertIn(("zh", "en"), pairs)
        self.assertIn(("en", "ja"), pairs)

    def test_missing_runtime_has_no_network_or_paid_fallback(self):
        translator = OfflineTranslator(cache_dir=self.temp.name)
        with patch("importlib.metadata.version", side_effect=importlib.metadata.PackageNotFoundError("argostranslate")), patch("urllib.request.urlopen") as network, patch.dict("os.environ", {"DEEPSEEK_API_KEY": "must-not-use", "ARGOS_MODEL_PROVIDER": "OPENAI"}):
            with self.assertRaisesRegex(OfflineTranslationError, "offline runtime"):
                translator.translate("Forecast", "ar", "en")
            network.assert_not_called()

    def test_unknown_source_route_fails_without_fallback(self):
        with self.assertRaisesRegex(OfflineTranslationError, "No pinned offline route"):
            self.translator.translate("sample", "zh", "ar")
        self.assertEqual(self.calls, [])

    def test_installer_targets_and_archive_metadata(self):
        self.assertEqual({(model["source"], model["target"]) for model in selected_models("zh,en")}, {("zh", "en"), ("en", "zh")})
        model = selected_models("en")[0]
        archive_path = Path(self.temp.name) / "test.argosmodel"
        with zipfile.ZipFile(archive_path, "w") as archive:
            archive.writestr("translate-zh_en/metadata.json", json.dumps({"from_code": "zh", "to_code": "en", "package_version": "1.9"}))
            archive.writestr("translate-zh_en/model/model.bin", "fake")
            archive.writestr("translate-zh_en/LICENSE", "Example license")
        evidence, root = inspect_archive(archive_path, model)
        self.assertEqual(root, "translate-zh_en")
        self.assertEqual(evidence["license_status"], "bundled_license_text_available")
        with self.assertRaisesRegex(OfflineTranslationError, "metadata mismatch"):
            inspect_archive(archive_path, {**model, "version": "1.0"})

    def test_installer_cache_does_not_bypass_new_digest_pin(self):
        model = {**selected_models("en")[0], "sha256": "new-digest"}
        with self.assertRaisesRegex(OfflineTranslationError, "SHA-256 does not match"):
            install_one(model, Path(self.temp.name), {**model, "sha256": "old-digest"})


if __name__ == "__main__":
    unittest.main()
