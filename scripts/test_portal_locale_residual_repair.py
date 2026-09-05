"""Offline full-inventory repair checks; no provider requests leave the process."""

from collections import Counter
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_portal_locales as builder


NATIVE = {"ko": "공개 연구 보고서의 전체 내용입니다.", "ja": "公開調査レポートの全文です。", "ar": "هذا هو المحتوى الكامل للتقرير البحثي العام."}


class ResidualRepairTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "cache.json.gz"
        self.state = builder.TranslationRun()
        self.addCleanup(mock.patch.stopall)
        mock.patch.object(builder, "log").start()
        # An accidental call to the lazy HTTP dependency must fail offline.
        self.http = mock.Mock(side_effect=AssertionError("Unexpected provider request"))
        mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=self.http)}).start()

    @staticmethod
    def inventory(count):
        return {f"{i:064x}": builder.TranslationUnit(
            f"{i:064x}", "html:text:p", f"公开研究报告第{i}部分的完整内容及其行业分析。",
        ) for i in range(count)}

    @staticmethod
    def cache_for(units, *, missing_locales=("ko",)):
        cache = builder.empty_cache()
        for locale in builder.LOCALES:
            if locale not in missing_locales:
                cache["locales"][locale] = {
                    unit.key: builder._translation_cache_row(unit, NATIVE[locale])
                    for unit in units.values()
                }
        return cache

    def translate(self, units, cache, translator=None, **kwargs):
        options = dict(cache_path=self.path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                       base_url="https://provider.example.invalid", workers=1,
                       timeout=1, attempts=1, max_batch_items=32,
                       batch_translator=translator, run_state=self.state)
        options.update(kwargs)
        return builder.translate_missing_units(units, cache, **options)

    def assert_complete(self, units, cache):
        self.assertEqual(self.state.data["status"], "passed")
        self.assertEqual(self.state.data["failed_batches"], 0)
        self.assertEqual(self.state.data["remaining_units_total"], 0)
        self.assertEqual(self.state.data["pending_repairs"], [])
        saved = builder.load_cache(self.path)
        for locale in builder.LOCALES:
            self.assertEqual(set(saved["locales"][locale]), set(units))
            self.assertEqual(saved["locales"][locale], cache["locales"][locale])

    def test_zero_saved_singleton_gets_one_plain_repair_and_preserves_history(self):
        units = self.inventory(1)
        cache = self.cache_for(units)
        calls = []

        def provider(_url, **kwargs):
            payload = kwargs["payload"]
            calls.append(payload)
            if len(calls) == 1:
                content = json.dumps({"translations": []})
            else:
                self.assertNotIn("response_format", payload)
                self.assertEqual(payload["messages"][1]["content"], next(iter(units.values())).source)
                content = NATIVE["ko"]
            response = mock.Mock(status_code=200)
            response.json.return_value = {"choices": [{"message": {"content": content}}]}
            return response

        self.http.side_effect = provider
        with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "offline-test"}, clear=True):
            self.translate(units, cache)
        self.assertEqual(len(calls), 2)
        self.assertEqual(self.state.data["request_modes"], {"batch_json": 1, "single_plain": 1})
        self.assertEqual(self.state.data["original_failed_batches"], 1)
        self.assertIn("omitted translation rows", self.state.data["original_batch_errors"][0])
        self.assert_complete(units, cache)

    def test_whole_invalid_json_batch_larger_than_four_repairs_only_missing_rows(self):
        units = self.inventory(7)
        cache = self.cache_for(units)
        paid = next(iter(units.values()))
        cache["locales"]["ko"][paid.key] = builder._translation_cache_row(paid, NATIVE["ko"])
        calls = []

        def provider(_url, **kwargs):
            payload = kwargs["payload"]
            if "response_format" in payload:
                sources = [row["source_text"] for row in json.loads(payload["messages"][1]["content"])["items"]]
                self.assertEqual(len(sources), 6)
                content = '{"translations":['
            else:
                sources = [payload["messages"][1]["content"]]
                content = NATIVE["ko"]
            calls.append(sources)
            self.assertNotIn(paid.source, sources)
            response = mock.Mock(status_code=200)
            response.json.return_value = {"choices": [{"message": {"content": content}}]}
            return response

        self.http.side_effect = provider
        with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "offline-test"}, clear=True):
            self.translate(units, cache)
        self.assertEqual(len(calls), 7)
        self.assertEqual(Counter(source for call in calls[1:] for source in call),
                         Counter(unit.source for unit in units.values() if unit.key != paid.key))
        self.assertEqual(self.state.data["repaired_units"], 6)
        self.assertEqual(self.state.data["original_failed_batches"], 1)
        self.assert_complete(units, cache)

    def test_sparse_omission_and_historical_whole_batch_error_both_repair(self):
        units = self.inventory(6)
        cache = self.cache_for(units, missing_locales=builder.LOCALES)
        calls = []

        def translator(locale, batch):
            calls.append((locale, tuple(unit.key for unit in batch)))
            if len(batch) == 2 and batch[0].key == f"{0:064x}":
                if locale == "ko":
                    raise builder.PartialTranslationError("one omitted row", {batch[0].key: NATIVE[locale]})
                if locale == "ja":
                    raise builder.PartialTranslationError("invalid translation JSON", {})
            return {unit.key: NATIVE[locale] for unit in batch}

        self.translate(units, cache, translator, max_batch_items=2)
        self.assertEqual(self.state.data["deferred_batches"], 1)
        self.assertEqual(self.state.data["original_failed_batches"], 1)
        self.assertEqual(Counter(calls[9:]), Counter([
            ("ko", (f"{1:064x}",)), ("ja", (f"{0:064x}",)), ("ja", (f"{1:064x}",)),
        ]))
        self.assert_complete(units, cache)

    def test_unchanged_long_paragraph_stays_incomplete_after_single_repair(self):
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "行业研究需要检查完整正文及其增长假设。" * 20)
        units = {unit.key: unit}
        cache = self.cache_for(units)
        calls = []

        def translator(locale, batch):
            calls.append(batch)
            if len(calls) == 1:
                raise builder.PartialTranslationError("missing translation", {})
            return {unit.key: unit.source}

        with self.assertRaisesRegex(builder.TranslationError, "1 unresolved source"):
            self.translate(units, cache, translator)
        self.assertEqual(len(calls), 2)
        self.assertEqual(self.state.data["status"], "failed")
        self.assertEqual(self.state.data["remaining_units_total"], 1)
        self.assertEqual(self.state.data["pending_repairs"][0]["repair_attempts"], 1)
        self.assertNotIn(unit.key, builder.load_cache(self.path)["locales"]["ko"])

    def test_shared_cost_budget_stops_tail_and_resume_uses_only_remaining_cache_gaps(self):
        units = self.inventory(4)
        cache = self.cache_for(units)
        self.state = builder.TranslationRun(max_cost_cny="0.05")
        calls = []
        payload = {"model": builder.DEFAULT_DEEPSEEK_MODEL, "thinking": {"type": "disabled"}, "max_tokens": 1000}

        def translator(locale, batch):
            self.state.reserve(payload)
            calls.append(tuple(unit.key for unit in batch))
            if len(batch) > 1:
                raise builder.PartialTranslationError("invalid translation JSON", {})
            return {unit.key: NATIVE[locale] for unit in batch}

        with self.assertRaises(builder.TranslationStopped):
            self.translate(units, cache, translator)
        self.assertEqual(self.state.data["stop_category"], "budget")
        self.assertEqual(self.state.data["provider_requests"], 2)
        self.assertEqual(len(calls), 2)
        self.assertEqual(self.state.data["repaired_units"], 1)
        cached = builder.load_cache(self.path)
        paid_keys = set(cached["locales"]["ko"])
        self.assertEqual(len(paid_keys), 1)
        resumed_calls = []

        def resumed(locale, batch):
            resumed_calls.extend(unit.key for unit in batch)
            self.assertTrue(paid_keys.isdisjoint(resumed_calls))
            return {unit.key: NATIVE[locale] for unit in batch}

        self.state = builder.TranslationRun()
        self.translate(units, cached, resumed)
        self.assertEqual(set(resumed_calls), set(units) - paid_keys)
        self.assert_complete(units, cached)

    def test_more_than_1024_residual_units_are_chunked_without_repeating_repairs(self):
        units = self.inventory(1025)
        cache = self.cache_for(units)
        repairs = Counter()
        observed_queues = []
        checkpoints = []
        real_write = builder.write_cache

        def translator(locale, batch):
            if len(batch) > 1:
                raise builder.PartialTranslationError("invalid translation JSON", {})
            observed_queues.append(self.state.data["pending_repair_count"])
            repairs[batch[0].key] += 1
            return {unit.key: NATIVE[locale] for unit in batch}

        def checkpoint(path, current):
            checkpoints.append(len(current["locales"]["ko"]))
            real_write(path, current)

        with mock.patch.object(builder, "write_cache", side_effect=checkpoint):
            self.translate(units, cache, translator, workers=8, max_batch_items=2000, max_batch_chars=1_000_000)
        self.assertEqual(repairs, Counter({key: 1 for key in units}))
        self.assertEqual(self.state.data["tail_repair_chunks"], 2)
        self.assertEqual(self.state.data["repair_workers"], 8)
        self.assertLessEqual(max(observed_queues), 1024)
        self.assertIn(1024, checkpoints)
        self.assert_complete(units, cache)

    def test_900_second_tail_deadline_is_shared_across_chunks(self):
        units = self.inventory(1025)
        cache = self.cache_for(units)
        clock = [0.0]
        repaired = []

        def translator(locale, batch):
            if len(batch) > 1:
                raise builder.PartialTranslationError("invalid translation JSON", {})
            repaired.append(batch[0].key)
            if len(repaired) == 1024:
                clock[0] = 901.0
            return {unit.key: NATIVE[locale] for unit in batch}

        with mock.patch.object(builder.time, "monotonic", side_effect=lambda: clock[0]):
            with self.assertRaises(builder.TranslationStopped):
                self.translate(units, cache, translator, max_batch_items=2000, max_batch_chars=1_000_000)
        self.assertEqual(len(repaired), 1024)
        self.assertEqual(self.state.data["stop_category"], "repair_limit")
        self.assertEqual(self.state.data["remaining_units_total"], 1)
        self.assertEqual(self.state.data["pending_repairs"][0]["repair_attempts"], 0)
        self.assertEqual(len(builder.load_cache(self.path)["locales"]["ko"]), 1024)

    def test_three_consecutive_unusable_batches_still_stop_before_tail(self):
        units = self.inventory(10)
        cache = self.cache_for(units)
        translator = mock.Mock(side_effect=builder.PartialTranslationError("invalid translation JSON", {}))
        with self.assertRaisesRegex(builder.TranslationError, "invalid translation JSON"):
            self.translate(units, cache, translator, max_batch_items=1)
        self.assertEqual(translator.call_count, 3)
        self.assertIn("Systemic", self.state.stop_reason)
        self.assertNotIn("tail_repair_units", self.state.data)
        self.assertEqual(self.state.data["repaired_units"], 0)

    def test_http_and_transport_failures_stop_immediately_and_keep_paid_rows(self):
        units = self.inventory(6)
        for failure in (401, 402, 403, "transport"):
            with self.subTest(failure=failure):
                self.state = builder.TranslationRun()
                cache = self.cache_for(units)
                calls = []

                def translator(locale, batch):
                    calls.append(batch)
                    paid = {batch[0].key: NATIVE[locale]}
                    if failure == "transport":
                        raise builder.PartialTranslationError("provider transport failed (OSError)", paid) from OSError("offline")
                    error = builder.ProviderHTTPError(failure, "offline fixture")
                    error.partial_translations = paid
                    raise error

                with self.assertRaises(builder.TranslationError):
                    self.translate(units, cache, translator, max_batch_items=2)
                self.assertEqual(len(calls), 1)
                self.assertEqual(self.state.data["repaired_units"], 0)
                self.assertNotIn("tail_repair_units", self.state.data)
                self.assertEqual(len(builder.load_cache(self.path)["locales"]["ko"]), 1)

    def test_budget_stop_with_historical_failure_never_dispatches_unstarted_inventory(self):
        units = self.inventory(10)
        cache = self.cache_for(units)
        calls = []

        def translator(locale, batch):
            calls.append(batch[0].key)
            if len(calls) == 1:
                raise builder.PartialTranslationError("invalid translation JSON", {})
            self.state.stop("Fixture balance checkpoint", category="budget")
            raise builder.TranslationStopped(self.state.stop_reason)

        with self.assertRaises(builder.TranslationStopped):
            self.translate(units, cache, translator, max_batch_items=1)
        self.assertEqual(len(calls), 2)
        self.assertEqual(self.state.data["stop_category"], "budget")
        self.assertNotIn("tail_repair_units", self.state.data)
        self.assertEqual(self.state.data["remaining_units_total"], 10)


if __name__ == "__main__":
    unittest.main()
