"""The actual 4-request canary omission must fit the existing 6-call cap."""
from collections import Counter
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_portal_locales as builder

NATIVE = {"ko": "금융 연구의 주요 내용입니다.", "ja": "金融調査の主な内容です。", "ar": "هذا هو المحتوى الرئيسي للبحث المالي."}


class PreflightRepairTests(unittest.TestCase):
    def run_case(self, *, bad_locale="ar", missing=2, plain_ok=True, count=16, max_items=16):
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", f"第{i}段金融研究正文及完整行业分析内容。") for i in range(count)}
        cache = builder.empty_cache()
        cache["locales"]["ko"]["f" * 64] = {"source": "保留历史缓存", "translation": NATIVE["ko"]}
        state = builder.TranslationRun(max_requests=6)
        calls, attempts, plain_sources = [], Counter(), []

        def respond(_url, **kwargs):
            payload = kwargs["payload"]
            locale = kwargs["label"].split()[0]
            attempts[locale] += 1
            plain = "response_format" not in payload
            calls.append((locale, plain))
            if plain:
                source = payload["messages"][1]["content"]
                plain_sources.append(source)
                text = NATIVE[locale] if plain_ok else source
            else:
                rows = json.loads(payload["messages"][1]["content"])["items"]
                bad = (10 if attempts[locale] == 1 else missing) if locale == bad_locale else 0
                text = json.dumps({"translations": [
                    {"id": row["id"], "text": row["source_text"] if index >= len(rows)-bad else NATIVE[locale]}
                    for index, row in enumerate(rows)
                ]})
            response = mock.Mock(status_code=200)
            response.json.return_value = {"choices": [{"message": {"content": text}, "finish_reason": "stop"}],
                                          "usage": {"prompt_tokens": 5, "completion_tokens": 5, "total_tokens": 10,
                                                    "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 5}}
            return response

        with tempfile.TemporaryDirectory() as directory, mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "offline-test"}, clear=True), mock.patch.dict(
            sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=mock.Mock(side_effect=respond))}
        ), mock.patch.object(builder, "log"):
            path = Path(directory)/"cache.json.gz"
            error = None
            try:
                builder.translate_missing_units(units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://provider.example.invalid", workers=500, timeout=1, attempts=2,
                    max_batch_items=max_items, max_batch_chars=100000, preflight_only=True,
                    preflight_batches_per_locale=1, run_state=state)
            except builder.TranslationError as caught:
                error = caught
            saved = builder.load_cache(path)
        self.assertLessEqual(state.data["provider_requests"], 6)
        self.assertEqual(state.data["provider_requests"], len(calls))
        self.assertIn("f" * 64, saved["locales"]["ko"])
        return state.data, saved, calls, plain_sources, error, units

    def test_actual_arabic_two_omissions_are_repaired_in_exactly_six_calls(self):
        report, cache, calls, repaired, error, units = self.run_case()
        self.assertIsNone(error)
        self.assertEqual(calls, [("ko",False),("ja",False),("ar",False),("ar",False),("ar",True),("ar",True)])
        self.assertEqual(set(repaired), {unit.source for unit in list(units.values())[-2:]})
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed_batches"], 0)
        self.assertEqual(report["repaired_units"], 2)
        for locale in builder.LOCALES:
            self.assertTrue(set(units).issubset(cache["locales"][locale]))

    def test_first_language_repairs_before_next_language_without_extra_calls(self):
        report, _, calls, repaired, error, _ = self.run_case(bad_locale="ko")
        self.assertIsNone(error)
        self.assertEqual(calls, [("ko",False),("ko",False),("ko",True),("ko",True),("ja",False),("ar",False)])
        self.assertEqual(len(repaired), 2)
        self.assertEqual(report["provider_requests"], 6)

    def test_unchanged_plain_repair_stops_before_next_language_and_keeps_cache(self):
        report, cache, calls, _, error, units = self.run_case(bad_locale="ko", plain_ok=False)
        self.assertIsNotNone(error)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["failed_batches"], 1)
        self.assertEqual(len(calls), 4)
        self.assertTrue(all(locale=="ko" for locale, _ in calls))
        self.assertEqual(len(set(units)&set(cache["locales"]["ko"])), 14)

    def test_insufficient_remaining_allowance_never_starts_plain_repairs(self):
        for locale in ("ko", "ar"):
            with self.subTest(locale=locale):
                report, _, calls, repaired, error, _ = self.run_case(bad_locale=locale, missing=3)
                self.assertIsNotNone(error)
                self.assertEqual(report["failed_batches"], 1)
                self.assertFalse(repaired)
                self.assertEqual(len(calls), 2 if locale=="ko" else 4)

    def test_full_inventory_outside_canary_is_not_translated_or_required(self):
        report, _, calls, repaired, error, _ = self.run_case(count=32)
        self.assertIsNone(error)
        self.assertEqual(len(calls), 6)
        self.assertEqual(len(repaired), 2)
        self.assertEqual(report["remaining_units_total"], 48)
        self.assertEqual(report["status"], "passed")


if __name__ == "__main__":
    unittest.main()
