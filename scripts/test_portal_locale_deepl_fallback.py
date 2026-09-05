"""DeepL is reachable only through the residual queue; all providers are mocked."""
from collections import Counter
import json
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

    def test_one_uncertain_repair_keeps_distinct_repairs_and_paid_cache(self):
        def repair(locale, _source):
            if locale == "ko":
                raise deepl.DeepLRepairError("Uncertain response; allowance retained")
            return NATIVE[locale]

        self.repair.translate.side_effect = repair
        with self.assertRaises(builder.TranslationError):
            self.run_translation(self.primary)
        self.assertEqual(self.repair.translate.call_count, 3)
        self.assertFalse(self.state.stop_reason)
        self.assertEqual(self.state.data["remaining_units_total"], 1)
        saved = builder.load_cache(self.path)
        for locale in builder.LOCALES:
            self.assertIn("0" * 64, saved["locales"][locale])
            self.assertIn("1" * 64, saved["locales"][locale])
        self.assertNotIn("2" * 64, saved["locales"]["ko"])
        for locale in ("ja", "ar"):
            self.assertIn("2" * 64, saved["locales"][locale])

    def test_terminal_repair_stop_still_stops_distinct_paid_requests(self):
        self.repair.translate.side_effect = deepl.DeepLRepairError("Authentication failed")
        self.repair.snapshot.return_value = {"provider_requests": 1, "stop_reason": "Authentication failed"}
        self.repair.snapshot.side_effect = None
        with self.assertRaises(builder.TranslationError):
            self.run_translation(self.primary)
        self.repair.translate.assert_called_once()
        self.assertTrue(self.state.stop_reason)
        self.assertTrue(self.path.is_file())

    def test_primary_auth_failure_never_reaches_deepl(self):
        with self.assertRaises(builder.TranslationError):
            self.run_translation(mock.Mock(side_effect=builder.ProviderHTTPError(402, "primary")))
        self.repair.translate.assert_not_called()

    def test_useful_warmup_never_makes_an_incomplete_full_build_publishable(self):
        self.units = {
            f"{index:064x}": builder.TranslationUnit(
                f"{index:064x}", "html:text:p", f"第{index}段金融研究报告的完整内容。"
            ) for index in range(32)
        }
        self.cache = builder.empty_cache()
        self.repair.translate.side_effect = lambda locale, source: source if locale == "ko" else NATIVE[locale]

        def primary(locale, batch):
            raise builder.PartialTranslationError("One missing row", {
                unit.key: NATIVE[locale] for unit in batch[:-1]
            })

        with self.assertRaises(builder.TranslationError):
            builder.translate_missing_units(
                self.units, self.cache, cache_path=self.path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", workers=500, timeout=1, attempts=2,
                max_batch_items=32, max_batch_chars=100000, batch_translator=primary, run_state=self.state,
            )
        self.assertTrue(self.state.data["warmup_passed"])
        self.assertEqual(self.state.data["status"], "failed")
        self.assertEqual(self.state.data["remaining_units_total"], 1)
        self.assertEqual(self.repair.translate.call_count, 3, "Never repeat the same repair to force a green run")

    def test_preflight_request_limit_is_shared_not_six_per_provider(self):
        state = builder.TranslationRun(max_requests=2)
        state.reserve()
        state.reserve_external_repair()
        self.assertEqual(state.translation_attempts(), 2)
        with self.assertRaises(builder.TranslationStopped):
            state.reserve()
        self.assertEqual(state.data["provider_requests"], 1)


class GroupedDeepLPreflightTests(unittest.TestCase):
    def run_case(self, *, accepted=2, repair_echo=False, repair_echo_count=1, repair_xml_error=False, http_status=200,
                 transport_failure=False, preflight_only=True, retry_succeeds=False):
        units = {
            f"{index:064x}": builder.TranslationUnit(
                f"{index:064x}", "html:text:p", f"第{index}段金融研究报告的完整内容及行业分析。",
            ) for index in range(32)
        }
        cache = builder.empty_cache()
        history_key = "f" * 64
        for locale in builder.LOCALES:
            cache["locales"][locale][history_key] = {
                "source": "应保留的历史译文", "translation": NATIVE[locale],
            }
        state = builder.TranslationRun(max_requests=6)
        calls, primary_sources, repair_sources = [], [], []
        attempts = Counter()
        repair = mock.Mock()

        def primary(_url, **kwargs):
            payload = kwargs["payload"]
            self.assertIn("response_format", payload, "grouped canaries must not spend on per-row DeepSeek plain retries")
            message = json.loads(payload["messages"][1]["content"])
            locale, rows = message["locale"], message["items"]
            sources = [row["source_text"] for row in rows]
            primary_sources.append((locale, sources))
            calls.append(("deepseek", locale, len(rows)))
            attempts[locale] += 1
            if transport_failure:
                raise OSError("offline transport unavailable")
            content = json.dumps({"translations": [
                {"id": row["id"], "text": NATIVE[locale]
                 if index < accepted or (retry_succeeds and attempts[locale] > 1)
                 else row["source_text"]}
                for index, row in enumerate(rows)
            ]})
            response = mock.Mock(status_code=http_status)
            response.json.return_value = {
                "choices": [{"message": {"content": content}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 5, "completion_tokens": 7, "total_tokens": 12,
                          "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 5},
            }
            return response

        def grouped_repair(locale, sources):
            self.assertGreater(len(sources), 1)
            self.assertLessEqual(len(sources), 50)
            repair_sources.append((locale, list(sources)))
            calls.append(("deepl", locale, len(sources)))
            if repair_xml_error:
                raise deepl.DeepLRepairError("Invalid repair XML", partial_translations={
                    index: NATIVE[locale] for index in range(1, len(sources))
                })
            return [source if repair_echo and index < repair_echo_count else NATIVE[locale]
                    for index, source in enumerate(sources)]

        repair.translate_many.side_effect = grouped_repair
        repair.translate.side_effect = AssertionError("A grouped residual must not be split into paid singleton requests")
        repair.snapshot.side_effect = lambda: {
            "provider_requests": len(repair_sources),
            "balance_requests": int(bool(repair_sources)),
            "billed_characters": sum(len(source) for _locale, sources in repair_sources for source in sources),
            "remaining_character_budget": 490000,
            "unobserved_requests": 0, "stop_reason": "",
        }
        provider = mock.Mock(side_effect=primary)
        with tempfile.TemporaryDirectory() as directory, \
                mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "offline-primary", "DEEPL_API_KEY": "offline-repair"}, clear=True), \
                mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}), \
                mock.patch.object(deepl, "DeepLRepair", return_value=repair), mock.patch.object(builder, "log"):
            path = Path(directory) / "cache.json.gz"
            error = None
            try:
                builder.translate_missing_units(
                    units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", workers=500 if preflight_only else 1,
                    timeout=1, attempts=2, max_batch_items=32, max_batch_chars=100000,
                    preflight_only=preflight_only, preflight_batches_per_locale=1, run_state=state,
                )
            except builder.TranslationError as caught:
                error = caught
            saved = builder.load_cache(path)
        self.assertEqual(state.data["provider_requests"], provider.call_count)
        self.assertEqual(state.translation_attempts(), len(calls))
        self.assertEqual(state.data["translation_requests_total"], len(calls))
        self.assertLessEqual(len(calls), 6)
        repair.translate.assert_not_called()
        if preflight_only:
            for locale in builder.LOCALES:
                self.assertIn(history_key, saved["locales"][locale])
        return state.data, saved, calls, primary_sources, repair_sources, error, units

    def test_all_locales_with_thirty_echoes_use_exactly_six_shared_posts(self):
        report, cache, calls, primary, repaired, error, units = self.run_case()
        self.assertIsNone(error)
        self.assertEqual(calls, [
            (provider, locale, count)
            for locale in builder.LOCALES
            for provider, count in (("deepseek", 32), ("deepl", 30))
        ])
        expected_sources = [unit.source for unit in units.values()]
        for locale, sources in primary:
            self.assertEqual(sources, expected_sources)
        for locale, sources in repaired:
            self.assertEqual(sources, expected_sources[2:])
            self.assertTrue(set(expected_sources[:2]).isdisjoint(sources), "paid successes must never reach DeepL")
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed_batches"], 0)
        self.assertEqual(report["remaining_units_total"], 0)
        self.assertEqual(report["repaired_units"], 90)
        self.assertEqual(report["provider_requests"], 3)
        self.assertEqual(report["external_repair_attempts"], 3)
        self.assertEqual(report["deepl_repair"]["provider_requests"], 3)
        self.assertEqual(report["usage_totals"]["total_tokens"], 36, "DeepL characters must not enter DeepSeek token usage")
        self.assertEqual(report["pending_repairs"], [])
        for locale in builder.LOCALES:
            self.assertTrue(set(units).issubset(cache["locales"][locale]))

    def test_all_locales_with_zero_accepted_rows_still_fit_six_posts(self):
        report, cache, calls, _primary, repaired, error, units = self.run_case(accepted=0)
        self.assertIsNone(error)
        self.assertEqual(calls, [
            (provider, locale, 32) for locale in builder.LOCALES for provider in ("deepseek", "deepl")
        ])
        for _locale, sources in repaired:
            self.assertEqual(sources, [unit.source for unit in units.values()])
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["repaired_units"], 96)
        for locale in builder.LOCALES:
            self.assertTrue(set(units).issubset(cache["locales"][locale]))

    def test_one_deepl_echo_keeps_gap_but_passes_useful_all_language_canary(self):
        report, cache, calls, _primary, repaired, error, units = self.run_case(repair_echo=True)
        self.assertIsNone(error)
        self.assertEqual(len(calls), 6)
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["repaired_units"], 87)
        missing_key = list(units)[2]
        for locale in builder.LOCALES:
            self.assertEqual(set(cache["locales"][locale]) & set(units), set(units) - {missing_key})
            self.assertEqual(report["preflight_sample_coverage"][locale]["pending"], 1)
            self.assertTrue(report["preflight_sample_coverage"][locale]["passed"])
        self.assertEqual(len(repaired), 3)
        self.assertTrue(all(row["repair_attempts"] == 1 for row in report["pending_repairs"]))

    def test_http_failure_never_enters_grouped_fallback(self):
        for status in (401, 402, 403, 429, 500):
            with self.subTest(status=status):
                report, _cache, calls, _primary, repaired, error, _units = self.run_case(http_status=status)
                self.assertIsNotNone(error)
                self.assertEqual(calls, [("deepseek", "ko", 32)])
                self.assertFalse(repaired)
                self.assertEqual(report["status"], "failed")

    def test_canary_with_too_many_untranslated_rows_still_fails(self):
        report, _cache, calls, _primary, _repaired, error, _units = self.run_case(
            repair_echo=True, repair_echo_count=4,
        )
        self.assertIsNotNone(error)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(len(calls), 2, "Stop before buying other languages after an unusable sample")
        self.assertTrue(all(not row["passed"] for row in report["preflight_sample_coverage"].values()))

    def test_adapter_partial_xml_error_preserves_every_other_paid_row(self):
        report, cache, calls, _primary, _repaired, error, units = self.run_case(repair_xml_error=True)
        self.assertIsNone(error)
        self.assertEqual(len(calls), 6)
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["repaired_units"], 87)
        for locale in builder.LOCALES:
            self.assertEqual(set(cache["locales"][locale]) & set(units), set(units) - {list(units)[2]})

    def test_transport_failure_never_enters_grouped_fallback(self):
        report, _cache, calls, _primary, repaired, error, _units = self.run_case(transport_failure=True)
        self.assertIsNotNone(error)
        self.assertEqual(calls, [("deepseek", "ko", 32)])
        self.assertFalse(repaired)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["unobserved_provider_requests"], 1)

    def test_normal_full_build_keeps_two_primary_attempts_before_deepl(self):
        report, _cache, calls, primary, repaired, error, units = self.run_case(
            preflight_only=False, retry_succeeds=True,
        )
        self.assertIsNone(error)
        self.assertFalse(repaired)
        self.assertEqual(calls, [
            ("deepseek", locale, count) for locale in builder.LOCALES for count in (32, 30)
        ])
        for _locale, sources in primary[1::2]:
            self.assertEqual(sources, [unit.source for unit in units.values()][2:])
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["provider_requests"], 6)

    def test_large_residual_queue_drains_without_restarting_primary_batches(self):
        units = {f"{index:064x}": builder.TranslationUnit(
            f"{index:064x}", "html:text:p", f"第{index}段短句区间，远低于去年水平。",
        ) for index in range(1600)}
        cache = builder.empty_cache()
        for locale in ("ja", "ar"):
            cache["locales"][locale] = {
                key: builder._translation_cache_row(unit, NATIVE[locale]) for key, unit in units.items()
            }
        primary_batches, repaired_sources = [], []
        def primary(locale, batch):
            self.assertEqual(locale, "ko")
            primary_batches.append([unit.key for unit in batch])
            raise builder.PartialTranslationError("unchanged short fragments", {})
        def grouped(locale, sources):
            self.assertEqual(locale, "ko")
            repaired_sources.extend(sources)
            return [NATIVE[locale]] * len(sources)
        repair = mock.Mock()
        repair.translate_many.side_effect = grouped
        repair.translate.side_effect = lambda locale, source: grouped(locale, [source])[0]
        repair.snapshot.return_value = {"provider_requests": 0, "stop_reason": ""}
        state = builder.TranslationRun()
        with tempfile.TemporaryDirectory() as directory, \
                mock.patch.dict("os.environ", {"DEEPL_API_KEY": "offline-repair"}, clear=True), \
                mock.patch.object(deepl, "DeepLRepair", return_value=repair), mock.patch.object(builder, "log"):
            builder.translate_missing_units(
                units, cache, cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://provider.example.invalid",
                workers=500, timeout=1, attempts=2, batch_translator=primary, run_state=state,
            )
        self.assertEqual(state.data["status"], "passed")
        self.assertTrue(state.data["warmup_passed"])
        self.assertEqual(state.data["repair_workers"], 1)
        self.assertEqual(state.data["remaining_units_total"], 0)
        self.assertEqual(state.data["repaired_units"], 1600)
        self.assertCountEqual([key for batch in primary_batches for key in batch], units)
        self.assertEqual(len(primary_batches), 50)
        self.assertCountEqual(repaired_sources, [unit.source for unit in units.values()])


if __name__ == "__main__":
    unittest.main()
