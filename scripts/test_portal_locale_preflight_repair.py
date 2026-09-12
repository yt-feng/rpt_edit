"""Small residual batches must fit the existing shared six-call canary cap."""
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
    def run_case(self, *, bad_locale="ar", missing=2, plain_ok=True, count=16, max_items=16,
                 initial_missing=10, preflight_batches=1, repair_accepts=None):
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
                source = payload["messages"][1]["content"].split("\n\n", 1)[1]
                plain_sources.append(source)
                text = NATIVE[locale] if plain_ok else source
            else:
                rows = json.loads(payload["messages"][1]["content"].split("\n\n", 1)[1])["items"]
                if attempts[locale] > 2 and locale == bad_locale:
                    self.assertLessEqual(len(rows), 8)
                    plain_sources.extend(row["source_text"] for row in rows)
                    accepted = repair_accepts if repair_accepts is not None else len(rows) if plain_ok else 0
                    bad = len(rows) - accepted
                else:
                    bad = (initial_missing if attempts[locale] == 1 else missing) if locale == bad_locale else 0
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
                    preflight_batches_per_locale=preflight_batches, run_state=state)
            except builder.TranslationError as caught:
                error = caught
            saved = builder.load_cache(path)
        self.assertLessEqual(state.data["provider_requests"], 6)
        self.assertEqual(state.data["provider_requests"], len(calls))
        self.assertIn("f" * 64, saved["locales"]["ko"])
        return state.data, saved, calls, plain_sources, error, units

    def test_two_arabic_omissions_use_one_grouped_repair_within_six_calls(self):
        report, cache, calls, repaired, error, units = self.run_case()
        self.assertIsNone(error)
        self.assertEqual(calls, [("ko",False),("ja",False),("ar",False),("ar",False),("ar",False)])
        self.assertEqual(set(repaired), {unit.source for unit in list(units.values())[-2:]})
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed_batches"], 0)
        self.assertEqual(report["repaired_units"], 2)
        for locale in builder.LOCALES:
            self.assertTrue(set(units).issubset(cache["locales"][locale]))

    def test_first_language_repairs_before_next_language_without_extra_calls(self):
        report, _, calls, repaired, error, _ = self.run_case(bad_locale="ko")
        self.assertIsNone(error)
        self.assertEqual(calls, [("ko",False),("ko",False),("ko",False),("ja",False),("ar",False)])
        self.assertEqual(len(repaired), 2)
        self.assertEqual(report["provider_requests"], 5)

    def test_unchanged_grouped_repair_stops_before_next_language_and_keeps_cache(self):
        report, cache, calls, _, error, units = self.run_case(bad_locale="ko", plain_ok=False)
        self.assertIsNotNone(error)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["failed_batches"], 1)
        self.assertEqual(len(calls), 3)
        self.assertTrue(all(locale=="ko" for locale, _ in calls))
        self.assertEqual(len(set(units)&set(cache["locales"]["ko"])), 14)

    def test_more_than_eight_residuals_never_enter_grouped_primary_repairs(self):
        for locale in ("ko", "ar"):
            with self.subTest(locale=locale):
                report, _, calls, repaired, error, _ = self.run_case(bad_locale=locale, missing=9)
                self.assertIsNotNone(error)
                self.assertEqual(report["failed_batches"], 1)
                self.assertFalse(repaired)
                self.assertEqual(len(calls), 2 if locale=="ko" else 4)

    def test_full_inventory_outside_canary_is_not_translated_or_required(self):
        report, _, calls, repaired, error, _ = self.run_case(count=32)
        self.assertIsNone(error)
        self.assertEqual(len(calls), 5)
        self.assertEqual(len(repaired), 2)
        self.assertEqual(report["remaining_units_total"], 48)
        self.assertEqual(report["status"], "passed")

    def test_actual_arabic_27_of_32_canary_repairs_five_rows_in_one_json_request(self):
        report, cache, calls, repaired, error, units = self.run_case(
            count=32, max_items=32, initial_missing=29, missing=5,
        )
        self.assertIsNone(error)
        self.assertEqual(len(calls), 5)
        self.assertEqual(repaired, [unit.source for unit in list(units.values())[-5:]])
        self.assertEqual(report["preflight_sample_coverage"]["ar"]["translated"], 32)
        self.assertEqual(report["preflight_residual_units"], [])
        self.assertEqual(len(set(units) & set(cache["locales"]["ar"])), 32)

    def test_partial_group_repair_keeps_the_existing_ninety_percent_gate(self):
        report, _, calls, repaired, error, _ = self.run_case(
            count=32, max_items=32, initial_missing=29, missing=5, repair_accepts=2,
        )
        self.assertIsNone(error)
        self.assertEqual(len(calls), 5)
        self.assertEqual(len(repaired), 5)
        self.assertEqual(report["preflight_sample_coverage"]["ar"]["translated"], 29)
        self.assertEqual(report["preflight_residual_units_total"], 3)
        self.assertEqual(len(report["pending_repairs"]), 3)

    def test_zero_accepted_primary_batch_never_enters_grouped_repair(self):
        report, _, calls, repaired, error, _ = self.run_case(
            bad_locale="ko", count=32, max_items=32, initial_missing=32, missing=32,
        )
        self.assertIsNotNone(error)
        self.assertEqual(calls, [("ko", False), ("ko", False)])
        self.assertFalse(repaired)
        self.assertEqual(report["preflight_sample_coverage"]["ko"]["translated"], 0)

    def test_grouped_repair_does_not_steal_remaining_canary_job_slots(self):
        report, _, calls, repaired, error, units = self.run_case(
            bad_locale="ko", count=32, max_items=16, initial_missing=10, missing=5,
            preflight_batches=2,
        )
        self.assertIsNotNone(error)
        self.assertEqual(calls, [("ko", False), ("ko", False)])
        self.assertFalse(repaired)
        self.assertEqual(report["selected_batches"], 6)
        first_batch_key = report["preflight_selected_units"][0]["batch_key"]
        residual = [row for row in report["preflight_residual_units"]
                    if row["locale"] == "ko" and row["batch_key"] == first_batch_key]
        self.assertEqual(len(residual), 5, "Declined repairs still expose every exact source")

    def test_single_residual_still_uses_plain_protocol(self):
        report, _, calls, repaired, error, _ = self.run_case(missing=1)
        self.assertIsNone(error)
        self.assertEqual(calls[-1], ("ar", True))
        self.assertEqual(len(repaired), 1)
        self.assertEqual(report["provider_requests"], 5)


class IdentityCheckpointTests(unittest.TestCase):
    def translate(self, units, cache, path, provider, *, preflight=False):
        state = builder.TranslationRun(max_requests=6 if preflight else None)
        with mock.patch.dict("os.environ", {}, clear=True), mock.patch.object(builder, "log"):
            builder.translate_missing_units(
                units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://provider.example.invalid", workers=500, timeout=1,
                attempts=2, batch_translator=provider, run_state=state,
                preflight_only=preflight, preflight_batches_per_locale=1,
            )
        return state.data, builder.load_cache(path)

    def test_fresh_legal_names_are_cached_without_paid_echo_and_reused_on_resume(self):
        sources = ("Arm Holdings plc", "Example Networks ltd", "Example Semiconductor co ltd")
        units = {}
        for source in sources:
            # The same cache key must work regardless of collection order.
            builder.collect_text_units(source, "html:text:p", units)
            builder.collect_text_units(source, "chart:keywords", units)
        provider = mock.Mock(side_effect=AssertionError("Literal names must not reach a provider"))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json.gz"
            report, cache = self.translate(units, builder.empty_cache(), path, provider, preflight=True)
            self.assertEqual(report["identity_seeded_units"], {locale: 3 for locale in builder.LOCALES})
            for locale in builder.LOCALES:
                for source in sources:
                    self.assertEqual(builder.translated_text(source, "html:text:p", locale, cache), source)
            report, cache = self.translate(units, cache, path, provider)
        self.assertEqual(report["identity_seeded_units"], {locale: 0 for locale in builder.LOCALES})
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["provider_requests"], 0)
        provider.assert_not_called()

    def test_incident_tail_preserves_paid_rows_and_sends_only_prose_to_provider(self):
        units = {}
        company = "Arm Holdings plc"
        geography = "EU/JN/UK/AU/CA/SZ"
        index = "S&P 500指数"
        prose = "这些公司的收入预计将在下一年度继续增长。"
        for source, context in ((company, "chart:keywords"), (geography, "chart:geographies"),
                                (index, "chart:keywords"), (prose, "html:text:p")):
            builder.collect_text_units(source, context, units)
        self.assertEqual(len(units), 3, "Geography codes must never enter the paid inventory")
        company_unit = builder.unit_for_text(company, "chart:keywords")[1]
        index_unit = builder.unit_for_text(index, "chart:keywords")[1]
        self.assertEqual(company_unit.key[:12], "2781e7cd017b", "Keep the incident cache key stable")
        self.assertEqual(index_unit.source, "S&P __KC_PH_000__指数")
        cache = builder.empty_cache()
        for locale in ("ja", "ar"):
            cache["locales"][locale][company_unit.key] = builder._translation_cache_row(company_unit, NATIVE[locale])
        for locale in ("ko", "ar"):
            cache["locales"][locale][index_unit.key] = builder._translation_cache_row(index_unit, NATIVE[locale])
        calls = []

        def provider(locale, batch):
            calls.extend(unit.source for unit in batch)
            return {unit.key: NATIVE[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json.gz"
            report, saved = self.translate(units, cache, path, provider, preflight=True)
            self.assertEqual(report["status"], "passed")
            self.assertEqual(report["identity_seeded_units"], {"ko": 1, "ja": 1, "ar": 0})
            self.assertEqual(calls, [prose] * 3)
            self.assertEqual(builder.translated_text(index, "html:meta:keyword", "ja", saved), index)
            for locale in ("ja", "ar"):
                self.assertEqual(saved["locales"][locale][company_unit.key]["translation"], NATIVE[locale])
            for locale in builder.LOCALES:
                self.assertEqual(builder.translated_text(geography, "chart:geographies", locale, saved), geography)
            report, _ = self.translate(units, saved, path, mock.Mock(side_effect=AssertionError("No replay")))
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["remaining_units_total"] if "remaining_units_total" in report else 0, 0)

    def test_identity_seeding_does_not_complete_untranslated_prose(self):
        for source in ("Arm Holdings plc expects revenue to grow.",
                       "这是需要完整翻译的中文研究正文。", "EU/UNKNOWN/UK outlook improves"):
            for preflight in (True, False):
                with self.subTest(source=source, preflight=preflight), tempfile.TemporaryDirectory() as directory:
                    unit = builder.unit_for_text(source, "chart:keywords")[1]
                    cache = builder.empty_cache()
                    provider = mock.Mock(side_effect=lambda locale, batch: {row.key: row.source for row in batch})
                    with self.assertRaises(builder.TranslationError):
                        self.translate({unit.key: unit}, cache, Path(directory) / "cache.json.gz", provider,
                                       preflight=preflight)
                    self.assertTrue(provider.called)
                    for locale in builder.LOCALES:
                        self.assertNotIn(unit.key, cache["locales"][locale])

    def test_title_case_keywords_still_reach_translation_provider(self):
        units = {}
        for source in ("Operating Cash Flow", "Net Income Growth", "Annual Revenue Outlook",
                       "Total Shareholder Return", "Palo Alto Networks"):
            builder.collect_text_units(source, "chart:keywords", units)
        calls = []

        def provider(locale, batch):
            calls.extend((locale, unit.source) for unit in batch)
            return {unit.key: NATIVE[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory:
            report, _ = self.translate(units, builder.empty_cache(), Path(directory) / "cache.json.gz", provider)
        self.assertEqual(set(calls), {(locale, unit.source) for locale in builder.LOCALES for unit in units.values()})
        self.assertEqual(report["identity_seeded_units"], {locale: 0 for locale in builder.LOCALES})


if __name__ == "__main__":
    unittest.main()
