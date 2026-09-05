"""DeepL is reachable only through the residual queue; all providers are mocked."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_portal_locales as builder
import deepl_locale_repair as deepl

NATIVE = {"ko": "금융 연구의 전체 내용", "ja": "金融調査の全文です", "ar": "المحتوى الكامل للبحث المالي"}


class DeepLFallbackTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name)/"cache.json.gz"
        self.state = builder.TranslationRun()
        self.units = {str(i)*64: builder.TranslationUnit(str(i)*64, "html:text:p", f"第{i}段金融研究报告的完整内容。") for i in range(3)}
        self.cache = builder.empty_cache()
        for locale in builder.LOCALES:
            self.cache["locales"][locale]["0"*64] = builder._translation_cache_row(self.units["0"*64], NATIVE[locale])
        self.repair = mock.Mock()
        self.repair.translate.side_effect = lambda locale, source: NATIVE[locale]
        self.repair.snapshot.side_effect = lambda: {"provider_requests": self.repair.translate.call_count, "billed_characters": 60, "remaining_character_budget": 499000, "stop_reason": ""}
        self.addCleanup(mock.patch.stopall)
        mock.patch.dict("os.environ", {"DEEPL_API_KEY": "offline-test"}, clear=True).start()
        self.constructor = mock.patch.object(deepl, "DeepLRepair", return_value=self.repair).start()
        mock.patch.object(builder, "log").start()

    def run_translation(self, translator):
        return builder.translate_missing_units(self.units, self.cache, cache_path=self.path, model=builder.DEFAULT_DEEPSEEK_MODEL,
            base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2, batch_translator=translator, run_state=self.state)

    def primary(self, locale, batch):
        self.assertEqual({unit.key for unit in batch}, {"1"*64, "2"*64})
        raise builder.PartialTranslationError("one missing row", {"1"*64: NATIVE[locale]})

    def test_only_failed_rows_reach_deepl_and_every_paid_row_is_reused(self):
        primary = mock.Mock(side_effect=self.primary)
        self.run_translation(primary)
        self.assertEqual(primary.call_count, 3)
        self.assertEqual(self.repair.translate.call_count, 3)
        self.assertTrue(all(call.args[1] == self.units["2"*64].source for call in self.repair.translate.call_args_list))
        self.assertEqual(self.state.data["status"], "passed")
        self.assertEqual(self.state.data["repair_provider"], "deepl")
        self.assertEqual(self.state.data["translation_requests_total"], 3)
        self.cache = builder.load_cache(self.path)
        self.state = builder.TranslationRun()
        self.run_translation(mock.Mock(side_effect=AssertionError("No retranslation allowed")))
        self.assertEqual(self.repair.translate.call_count, 3)

    def test_successful_primary_never_calls_deepl_or_balance(self):
        self.run_translation(lambda locale, batch: {unit.key: NATIVE[locale] for unit in batch})
        self.repair.translate.assert_not_called()

    def test_quota_exhaustion_saves_progress_and_never_falls_back_to_another_paid_call(self):
        self.repair.translate.side_effect = deepl.DeepLQuotaExhausted("limit")
        with self.assertRaises(builder.TranslationStopped):
            self.run_translation(self.primary)
        self.assertEqual(self.state.data["stop_category"], "deepl_quota")
        self.repair.translate.assert_called_once()
        saved = builder.load_cache(self.path)
        for locale in builder.LOCALES:
            self.assertIn("1"*64, saved["locales"][locale])
            self.assertNotIn("2"*64, saved["locales"][locale])

    def test_untranslated_deepl_output_is_not_written_as_a_complete_locale(self):
        self.repair.translate.side_effect = lambda locale, source: source
        with self.assertRaises(builder.TranslationError):
            self.run_translation(self.primary)
        self.assertEqual(self.state.data["status"], "failed")
        self.assertEqual(self.state.data["remaining_units_total"], 3)

    def test_primary_auth_failure_never_reaches_deepl(self):
        with self.assertRaises(builder.TranslationError):
            self.run_translation(mock.Mock(side_effect=builder.ProviderHTTPError(402, "primary")))
        self.repair.translate.assert_not_called()

    def test_preflight_request_limit_is_shared_not_six_per_provider(self):
        state = builder.TranslationRun(max_requests=2)
        state.reserve()
        state.reserve_external_repair()
        self.assertEqual(state.translation_attempts(), 2)
        with self.assertRaises(builder.TranslationStopped):
            state.reserve()
        self.assertEqual(state.data["provider_requests"], 1)


if __name__ == "__main__":
    unittest.main()
