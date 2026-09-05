"""Offline checks that paid translations survive missing rows and retries."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_portal_locales as builder


class PartialBatchTests(unittest.TestCase):
    def setUp(self):
        self.units = [
            builder.TranslationUnit("a" * 64, "html:text:p", "第一段公开研究报告的完整内容。"),
            builder.TranslationUnit("b" * 64, "html:text:p", "第二段公开研究报告的完整内容。"),
        ]
        self.good = {"id": "0", "text": "첫 번째 공개 연구 보고서의 전체 내용입니다."}
        self.other = {"id": "1", "text": "두 번째 공개 연구 보고서의 전체 내용입니다."}

    @staticmethod
    def response(rows, status=200):
        response = mock.Mock(status_code=status)
        response.json.return_value = {
            "choices": [{"message": {"content": json.dumps({"translations": rows})}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150},
        }
        return response

    def translate(self, provider, **kwargs):
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}):
            return builder.deepseek_translate_batch(
                "ko", self.units, model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", timeout=1, attempts=2, **kwargs,
            )

    def test_retry_sends_only_missing_rows(self):
        seen = []

        def provider(_url, **kwargs):
            seen.append(json.loads(json.dumps(kwargs["payload"])))
            return self.response([self.good] if len(seen) == 1 else [self.other])

        result = self.translate(provider)
        self.assertEqual(result, {self.units[0].key: self.good["text"], self.units[1].key: self.other["text"]})
        self.assertEqual([row["id"] for row in json.loads(seen[0]["messages"][1]["content"])["items"]], ["0", "1"])
        self.assertEqual([row["id"] for row in json.loads(seen[1]["messages"][1]["content"])["items"]], ["1"])
        self.assertNotIn(self.units[0].source, seen[1]["messages"][1]["content"])

    def test_valid_rows_after_bad_row_are_not_lost(self):
        wire = [builder.TranslationUnit(str(i), unit.context, unit.source) for i, unit in enumerate(self.units)]
        with self.assertRaises(builder.PartialTranslationError) as caught:
            builder.parse_translation_batch(json.dumps({"translations": [
                {"id": "0", "text": ""}, self.other,
            ]}), wire, "ko")
        self.assertEqual(caught.exception.partial_translations, {"1": self.other["text"]})

    def test_duplicate_and_extra_rows_do_not_force_paid_retry(self):
        provider = mock.Mock(return_value=self.response([self.good, self.other, self.good, {"id": "extra", "text": ""}]))
        result = self.translate(provider)
        self.assertEqual(len(result), 2)
        self.assertEqual(provider.call_count, 1)

    def test_numeric_policy_keeps_cache_key_and_required_shared_url_slots(self):
        numeric, unit = builder.unit_for_text("查看 2026", "html:text:p")
        previous_key = builder.hashlib.sha256(
            f"{builder.PROMPT_VERSION}\0copy\0{numeric.canonical}".encode("utf-8")
        ).hexdigest()
        self.assertEqual(unit.key, previous_key)
        self.assertEqual(unit.data_placeholders, ("__KC_PH_000__",))
        builder.validate_translation_quality("ko", unit, "확인하세요")
        inventory = {}
        builder.collect_text_units("查看 2026", "html:text:p", inventory)
        builder.collect_text_units("查看 https://example.com", "html:text:p", inventory)
        self.assertEqual(len(inventory), 1)
        self.assertEqual(inventory[unit.key].data_placeholders, ())
        with self.assertRaisesRegex(builder.TranslationError, "placeholder"):
            builder.validate_translation_quality("ko", inventory[unit.key], "확인하세요")

    def test_stopped_retries_save_paid_rows_to_resumable_cache(self):
        for ending in ("empty", "http402", "request_limit"):
            with self.subTest(ending=ending), tempfile.TemporaryDirectory() as directory:
                provider = mock.Mock(side_effect=[self.response([self.good]), self.response([], 402 if ending == "http402" else 200)])
                cache = builder.empty_cache()
                path = Path(directory) / "cache.json.gz"
                with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "test-key"}, clear=True), mock.patch.dict(
                    sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}
                ):
                    with self.assertRaises(builder.TranslationError):
                        builder.translate_missing_units(
                            {unit.key: unit for unit in self.units}, cache,
                            cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                            base_url="https://api.deepseek.com", workers=500, timeout=1,
                            attempts=2, preflight_only=True, preflight_batches_per_locale=1,
                            max_provider_requests=1 if ending == "request_limit" else 6,
                        )
                saved = builder.load_cache(path, builder.DEFAULT_DEEPSEEK_MODEL)
                self.assertEqual(saved["locales"]["ko"][self.units[0].key]["translation"], self.good["text"])
                self.assertNotIn(self.units[1].key, saved["locales"]["ko"])
                self.assertEqual(provider.call_count, 1 if ending == "request_limit" else 2)

    def test_full_concurrency_waits_for_all_language_warmup_and_reuses_its_rows(self):
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究报告内容") for i in range(10)}
        state = builder.TranslationRun()
        calls = []
        native = {"ko": "공개 연구 보고서", "ja": "公開調査レポート", "ar": "تقرير بحثي عام"}

        def translator(locale, batch):
            with state.lock:
                calls.append((locale, batch[0].key, state.data.get("warmup_passed", False)))
            return {unit.key: native[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory:
            cache = builder.empty_cache()
            builder.translate_missing_units(
                units, cache, cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=500, timeout=1, attempts=1, max_batch_items=1,
                batch_translator=translator, run_state=state,
            )
        self.assertEqual(len(calls), 30)
        self.assertEqual(len({(locale, key) for locale, key, _ in calls}), 30)
        self.assertEqual({locale for locale, _, _ in calls[:12]}, set(builder.LOCALES))
        self.assertTrue(all(not passed for _, _, passed in calls[:12]))
        self.assertTrue(all(passed for _, _, passed in calls[12:]))
        self.assertTrue(state.data["warmup_passed"])

    def test_incomplete_warmup_never_dispatches_high_concurrency(self):
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究报告内容") for i in range(100)}
        calls = []

        def translator(locale, batch):
            calls.append((locale, batch[0].key))
            raise builder.PartialTranslationError("missing row", {})

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(builder.TranslationError):
                builder.translate_missing_units(
                    units, builder.empty_cache(), cache_path=Path(directory) / "cache.json.gz",
                    model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                    workers=500, timeout=1, attempts=1, max_batch_items=1,
                    batch_translator=translator,
                )
        self.assertLessEqual(len(calls), 8)


if __name__ == "__main__":
    unittest.main()
