"""Offline checks that paid translations survive missing rows and retries."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_portal_locales as builder


class SeoPracticalChecks(unittest.TestCase):
    def test_real_numeric_marker_hallucination_keeps_usable_japanese_prose(self):
        unit = builder.TranslationUnit("0", "html:text:p", "，但OEM厂商已通过提高PC售价来覆盖内存成本，导致出货量预计环比下降超过")
        output = "だが、OEMメーカーはPC販売価格を引き上げてメモリコストを賄っており、出荷台数は前期比で__KC_PH_000__%以上減少すると予想される"
        result = builder.parse_translation_batch(json.dumps({"translations": [{"id": "0", "text": output}]}), [unit], "ja")
        self.assertEqual(result["0"], output.replace("__KC_PH_000__", ""))

    def test_missing_structural_marker_and_javascript_markers_remain_checked(self):
        for context, source, translated in (
            ("html:text:p", "详情见__KC_PH_000__", "자세한 내용은 __KC_PH_001__을 참조하세요"),
            ("javascript:ui", "查看详情", "자세히 __KC_PH_000__"),
        ):
            with self.subTest(context=context):
                unit = builder.TranslationUnit("0", context, source)
                with self.assertRaisesRegex(builder.TranslationError, "placeholder"):
                    builder.parse_translation_batch(json.dumps({"translations": [{"id": "0", "text": translated}]}), [unit], "ko")

    def test_translated_quotation_does_not_count_as_a_missing_translation(self):
        unit = builder.TranslationUnit("0", "html:text:p", "Global investment outlook")
        builder.validate_translation_quality("ko", unit, "글로벌 투자 전망 — 원제: 「Global investment outlook」")
        with self.assertRaisesRegex(builder.TranslationError, "unchanged source"):
            builder.validate_translation_quality("ko", unit, unit.source)
        with self.assertRaisesRegex(builder.TranslationError, "retains complete source"):
            builder.validate_translation_quality("ko", unit, "번역 " + unit.source)

    def test_indexable_units_run_first_and_all_languages_share_the_queue(self):
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究报告内容") for i in range(5)}
        priority = frozenset(list(units)[-2:])
        calls = []
        native = {"ko": "공개 연구 보고서입니다", "ja": "公開調査レポートです", "ar": "هذا تقرير بحثي عام"}
        def translator(locale, batch):
            calls.append((locale, batch[0].key))
            return {unit.key: native[locale] for unit in batch}
        with tempfile.TemporaryDirectory() as directory:
            state = builder.TranslationRun()
            builder.translate_missing_units(units, builder.empty_cache(),
                cache_path=Path(directory) / "cache.json.gz", model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=1,
                max_batch_items=1, batch_translator=translator, priority_keys=priority, run_state=state)
        self.assertEqual([locale for locale, key in calls[:6]], list(builder.LOCALES) * 2)
        self.assertTrue(all(key in priority for locale, key in calls[:6]))
        self.assertTrue(all(key not in priority for locale, key in calls[6:]))
        self.assertEqual(len(calls), 15)
        self.assertEqual(state.data["status"], "passed")


class PlainRepairTests(unittest.TestCase):
    def test_real_failed_fragment_changes_protocol_and_reuses_31_paid_rows(self):
        units = [builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究报告内容") for i in range(32)]
        fragment = "，比去年同期提升__KC_PH_000__个百分点。"
        units[19] = builder.TranslationUnit(units[19].key, "html:text:p", fragment)
        seen = []

        def provider(_url, **kwargs):
            payload = kwargs["payload"]
            seen.append(payload)
            self.assertEqual(kwargs["max_attempts"], 1)
            self.assertFalse(kwargs["allow_model_fallback"])
            if len(seen) == 1:
                content = json.dumps({"translations": [
                    {"id": str(i), "text": fragment if i == 19 else "공개 연구 보고서 내용"}
                    for i in range(32)
                ]})
            else:
                self.assertNotIn("response_format", payload)
                self.assertEqual(payload["messages"][1]["content"], fragment)
                content = "전년 동기 대비 __KC_PH_000__퍼센트포인트 상승했다."
            response = mock.Mock(status_code=200)
            response.json.return_value = {
                "choices": [{"message": {"content": content}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150},
            }
            return response

        state = builder.TranslationRun(max_requests=2, max_cost_cny="1")
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}):
            result = builder.deepseek_translate_batch(
                "ko", units, model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                timeout=1, attempts=2, run_state=state,
            )
        self.assertEqual(len(result), 32)
        self.assertEqual(len(seen), 2)
        self.assertEqual(result[units[19].key], "전년 동기 대비 __KC_PH_000__퍼센트포인트 상승했다.")
        self.assertEqual(state.data["request_modes"], {"batch_json": 1, "single_plain": 1})
        self.assertEqual(state.data["usage_totals"]["total_tokens"], 300)
        self.assertEqual(state.data["cost_guard"]["settled_peak_estimate_micro_cny"], 1500)
        self.assertFalse(state.cost_reservations)

    def test_plain_repair_keeps_omission_and_structural_checks_and_has_no_hidden_retry(self):
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "，比去年同期提升__KC_PH_000__个百分点。")
        for content, expected in (
            (unit.source, "unchanged source"),
            ("전년 동기 대비 상승했다.", "placeholder"),
            ("ارتفعت __KC_PH_000__ نقطة مئوية.", "Hangul"),
        ):
            with self.subTest(content=content):
                response = mock.Mock(status_code=200)
                response.json.return_value = {"choices": [{"message": {"content": content}}]}
                provider = mock.Mock(return_value=response)
                with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}):
                    with self.assertRaisesRegex(builder.PartialTranslationError, expected):
                        builder.deepseek_translate_batch(
                            "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                            timeout=1, attempts=1, single_item_plain=True,
                        )
                self.assertEqual(provider.call_count, 1)

    def test_plain_repair_shares_budget_and_propagates_provider_errors(self):
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        for ending in ("request_limit", "cost_limit", "402", "transport"):
            with self.subTest(ending=ending):
                state = builder.TranslationRun(max_requests=1, max_cost_cny="0.000001" if ending == "cost_limit" else "1")
                if ending == "request_limit":
                    state.reserve({"model": builder.DEFAULT_DEEPSEEK_MODEL, "thinking": {"type": "disabled"}, "max_tokens": 1000})
                response = mock.Mock(status_code=402)
                response.json.return_value = {"error": {"message": "Insufficient Balance"}}
                provider = mock.Mock(side_effect=OSError("transport details") if ending == "transport" else None, return_value=response)
                with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}):
                    with self.assertRaises(builder.TranslationError):
                        builder.deepseek_translate_batch(
                            "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                            timeout=1, attempts=2, single_item_plain=True, run_state=state,
                        )
                self.assertEqual(provider.call_count, 0 if ending.endswith("limit") else 1)
                if ending == "transport":
                    self.assertEqual(state.data["unobserved_provider_requests"], 1)
                    self.assertGreater(state.data["cost_guard"]["retained_reservations_micro_cny"], 0)


class PartialBatchTests(unittest.TestCase):
    def test_structured_entity_aliases_are_identity_not_untranslated_prose(self):
        alias = "Bank of America Merrill Lynch"
        node = {"@type": "Organization", "name": "Bank of America", "alternateName": [alias]}
        inventory = {}
        builder.json_ld_walk(node, units=inventory)
        _protected, old_unit = builder.unit_for_text(alias, "jsonld:alternateName")
        current = inventory[old_unit.key]
        self.assertEqual(current.source, old_unit.source)
        self.assertEqual(current.context, "jsonld:entity:alternateName")
        cache = builder.empty_cache()
        for locale in builder.LOCALES:
            for unit in inventory.values():
                builder.validate_translation_quality(locale, unit, unit.source)
                cache["locales"][locale][unit.key] = {"source": unit.source, "translation": unit.source}
            self.assertEqual(builder.json_ld_walk(node, locale=locale, cache=cache), node)
        for schema_type in ("Person", "Brand", ["Thing", "Organization"], "https://schema.org/Organization"):
            units = {}
            builder.json_ld_walk({"@type": schema_type, "alternateName": alias}, units=units)
            builder.validate_translation_quality("ko", units[old_unit.key], alias)

    def test_structured_entity_rule_does_not_exempt_body_or_page_headlines(self):
        source = "Global markets remain strong while interest rates continue rising"
        for node in (
            {"@type": "Organization", "description": source},
            {"@type": "WebPage", "name": source},
            {"@type": "Article", "alternateName": source},
        ):
            units = {}
            builder.json_ld_walk(node, units=units)
            for unit in units.values():
                with self.assertRaisesRegex(builder.TranslationError, "unchanged source"):
                    builder.validate_translation_quality("ko", unit, source)

    def test_entity_identity_merges_both_collection_orders_without_changing_key(self):
        alias = "Bank of America Merrill Lynch"
        _protected, old_unit = builder.unit_for_text(alias, "jsonld:alternateName")
        for entity_first in (False, True):
            with self.subTest(entity_first=entity_first):
                units = {}
                collectors = [
                    lambda: builder.collect_text_units(alias, "html:text:span", units),
                    lambda: builder.json_ld_walk({"@type": "Organization", "alternateName": alias}, units=units),
                ]
                for collect in reversed(collectors) if entity_first else collectors:
                    collect()
                self.assertEqual(set(units), {old_unit.key})
                self.assertIn(units[old_unit.key].context, builder.STRUCTURED_NAME_CONTEXTS)
                for locale in builder.LOCALES:
                    builder.validate_translation_quality(locale, units[old_unit.key], alias)

    def test_old_entity_cache_is_annotated_without_requests_and_renders_other_fields(self):
        alias = "Bank of America Merrill Lynch"
        units = {}
        builder.collect_text_units(alias, "html:text:span", units)
        builder.json_ld_walk({"@type": "Organization", "alternateName": alias}, units=units)
        unit = next(iter(units.values()))
        for preflight in (False, True):
            with self.subTest(preflight=preflight), tempfile.TemporaryDirectory() as directory:
                cache = builder.empty_cache()
                for locale in builder.LOCALES:
                    cache["locales"][locale][unit.key] = {"source": alias, "translation": alias}
                translator = mock.Mock(side_effect=AssertionError("Existing paid translation must be reused"))
                path = Path(directory) / "cache.json.gz"
                builder.translate_missing_units(
                    units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2,
                    preflight_only=preflight, batch_translator=translator,
                )
                translator.assert_not_called()
                stored = builder.load_cache(path, builder.DEFAULT_DEEPSEEK_MODEL)
                for locale in builder.LOCALES:
                    self.assertTrue(stored["locales"][locale][unit.key]["entity_name"])
                    rendered = builder.render_localized_html(
                        f"<html><body><span>{alias}</span></body></html>",
                        locale=locale, cache=stored, site_url="https://portal.example.invalid", discovery_markup="",
                    )
                    self.assertIn(f"<span>{alias}</span>", rendered)
                    sentence = f"{alias} expects global markets to remain strong while interest rates rise."
                    _protected, prose = builder.unit_for_text(sentence, "html:text:p")
                    self.assertNotEqual(prose.key, unit.key)
                    stored["locales"][locale][prose.key] = {"source": prose.source, "translation": prose.source}
                    with self.assertRaisesRegex(builder.TranslationError, "unchanged source"):
                        builder.translated_text(sentence, "html:text:p", locale, stored)

    def test_success_and_partial_cache_rows_retain_entity_identity(self):
        alias = "Bank of America Merrill Lynch"
        units = {}
        builder.json_ld_walk({"@type": "Organization", "alternateName": alias}, units=units)
        entity = next(iter(units.values()))
        for partial in (False, True):
            with self.subTest(partial=partial), tempfile.TemporaryDirectory() as directory:
                inventory = dict(units)
                if partial:
                    builder.collect_text_units("Ordinary market outlook remains unchanged", "html:text:p", inventory)

                def translator(locale, batch):
                    if partial:
                        raise builder.PartialTranslationError("Only entity row completed", {entity.key: alias})
                    return {unit.key: alias for unit in batch}

                path = Path(directory) / "cache.json.gz"
                kwargs = dict(
                    cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2,
                    preflight_only=True, batch_translator=translator,
                )
                if partial:
                    with self.assertRaises(builder.TranslationError):
                        builder.translate_missing_units(inventory, builder.empty_cache(), **kwargs)
                else:
                    builder.translate_missing_units(inventory, builder.empty_cache(), **kwargs)
                stored = builder.load_cache(path, builder.DEFAULT_DEEPSEEK_MODEL)
                self.assertTrue(stored["locales"]["ko"][entity.key]["entity_name"])
                self.assertEqual(builder.translated_text(alias, "html:text:span", "ko", stored), alias)

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
        self.assertNotIn("response_format", seen[1])
        self.assertEqual(seen[1]["messages"][1]["content"], self.units[1].source)
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
                            # Exhaust the stated cap in the empty-response case;
                            # available canary calls now repair sparse omissions.
                            max_provider_requests={"request_limit": 1, "empty": 2, "http402": 6}[ending],
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

    @staticmethod
    def queue_inventory(count):
        return {f"{i:064x}": builder.TranslationUnit(
            f"{i:064x}", "html:text:p", f"公开研究报告第{i}部分的完整内容。",
        ) for i in range(count)}

    def test_warmup_repairs_small_gap_before_enabling_full_concurrency(self):
        units = self.queue_inventory(20)
        state, calls = builder.TranslationRun(), []
        native = {"ko": "공개 연구 보고서입니다", "ja": "公開調査レポートです", "ar": "هذا تقرير بحثي عام"}

        def translator(locale, batch):
            with state.lock:
                calls.append((locale, tuple(unit.key for unit in batch), state.data.get("warmup_passed", False)))
            if locale == "ko" and len(batch) == 2 and batch[0].key == f"{0:064x}":
                raise builder.PartialTranslationError("isolated missing row", {batch[0].key: native[locale]})
            return {unit.key: native[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory:
            builder.translate_missing_units(
                units, builder.empty_cache(), cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=500, timeout=1, attempts=2, max_batch_items=2,
                batch_translator=translator, run_state=state,
            )
        repair = [call for call in calls if len(call[1]) == 1]
        self.assertEqual(repair, [("ko", (f"{1:064x}",), False)])
        self.assertEqual(len([call for call in calls if not call[2]]), 13)
        self.assertEqual(len(calls), 31)
        self.assertTrue(state.data["warmup_passed"])
        self.assertEqual(state.data["repaired_units"], 1)
        self.assertEqual(state.data["pending_repair_count"], 0)
        self.assertEqual(state.data["status"], "passed")

    def test_tail_repairs_only_gap_after_healthy_batches_and_reuses_complete_cache(self):
        units = self.queue_inventory(6)
        state, calls = builder.TranslationRun(), []
        native = {"ko": "공개 연구 보고서입니다", "ja": "公開調査レポートです", "ar": "هذا تقرير بحثي عام"}

        def translator(locale, batch):
            calls.append((locale, tuple(unit.key for unit in batch)))
            if locale == "ko" and len(batch) == 2 and batch[0].key == f"{0:064x}":
                raise builder.PartialTranslationError("isolated missing row", {batch[0].key: native[locale]})
            return {unit.key: native[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json.gz"
            kwargs = dict(cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                          base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2, max_batch_items=2)
            builder.translate_missing_units(units, builder.empty_cache(), batch_translator=translator, run_state=state, **kwargs)
            self.assertEqual(len(calls), 10)
            self.assertEqual(calls[-1], ("ko", (f"{1:064x}",)))
            self.assertTrue(all(len(keys) == 2 for _locale, keys in calls[:-1]))
            cached = builder.load_cache(path)
            no_more_requests = mock.Mock(side_effect=AssertionError("Completed cache must be reused"))
            builder.translate_missing_units(units, cached, batch_translator=no_more_requests, **kwargs)
            no_more_requests.assert_not_called()
        self.assertEqual(state.data["pending_repairs"], [])
        self.assertEqual(state.data["failed_batches"], 0)

    def test_unresolved_warmup_repair_never_enables_full_concurrency(self):
        units = self.queue_inventory(20)
        state, calls = builder.TranslationRun(), []
        native = {"ko": "공개 연구 보고서입니다", "ja": "公開調査レポートです", "ar": "هذا تقرير بحثي عام"}

        def translator(locale, batch):
            calls.append((locale, len(batch), state.data.get("warmup_passed", False)))
            if locale == "ko" and len(batch) == 2 and batch[0].key == f"{0:064x}":
                raise builder.PartialTranslationError("isolated missing row", {batch[0].key: native[locale]})
            return {unit.key: unit.source if len(batch) == 1 else native[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory, self.assertRaises(builder.TranslationStopped):
            builder.translate_missing_units(
                units, builder.empty_cache(), cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=500, timeout=1, attempts=2, max_batch_items=2,
                batch_translator=translator, run_state=state,
            )
        self.assertEqual(len(calls), 13)
        self.assertFalse(any(passed for _locale, _size, passed in calls))
        self.assertEqual(state.data["pending_repair_count"], 1)
        self.assertEqual(state.data["status"], "failed")

    def test_more_than_four_missing_rows_are_not_deferred(self):
        units = self.queue_inventory(6)
        state = builder.TranslationRun()
        translator = mock.Mock(side_effect=builder.PartialTranslationError(
            "five missing rows", {f"{0:064x}": "공개 연구 보고서입니다"},
        ))
        with tempfile.TemporaryDirectory() as directory, self.assertRaises(builder.TranslationError):
            builder.translate_missing_units(
                units, builder.empty_cache(), cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=500, timeout=1, attempts=2, max_batch_items=6,
                batch_translator=translator, run_state=state,
            )
        self.assertEqual(state.data["deferred_units_total"], 0)
        self.assertEqual(state.data["repaired_units"], 0)

    def test_unresolved_tail_stays_failed_and_next_run_translates_only_pending_source(self):
        units = self.queue_inventory(6)
        state = builder.TranslationRun()
        native = {"ko": "공개 연구 보고서입니다", "ja": "公開調査レポートです", "ar": "هذا تقرير بحثي عام"}

        def translator(locale, batch):
            if locale == "ko" and len(batch) == 2 and batch[0].key == f"{0:064x}":
                raise builder.PartialTranslationError("isolated missing row", {batch[0].key: native[locale]})
            return {unit.key: unit.source if len(batch) == 1 else native[locale] for unit in batch}

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json.gz"
            kwargs = dict(cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                          base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2, max_batch_items=2)
            with self.assertRaisesRegex(builder.TranslationError, "unresolved source"):
                builder.translate_missing_units(units, builder.empty_cache(), batch_translator=translator, run_state=state, **kwargs)
            self.assertEqual(state.data["status"], "failed")
            self.assertEqual(state.data["pending_repair_count"], 1)
            self.assertEqual(state.data["pending_repairs"][0]["repair_attempts"], 1)
            self.assertEqual(state.data["pending_repairs"][0]["key"], f"{1:064x}")
            cached = builder.load_cache(path)
            repaired = mock.Mock(return_value={f"{1:064x}": native["ko"]})
            builder.translate_missing_units(units, cached, batch_translator=repaired, **kwargs)
            repaired.assert_called_once_with("ko", [units[f"{1:064x}"]])

    def test_repair_uses_same_request_budget_and_plain_single_attempt(self):
        units = self.queue_inventory(2)
        for request_limit in (1, 2):
            with self.subTest(request_limit=request_limit), tempfile.TemporaryDirectory() as directory:
                state = builder.TranslationRun(max_requests=request_limit)
                cache = builder.empty_cache()
                for locale, text in (("ja", "公開調査レポートです"), ("ar", "هذا تقرير بحثي عام")):
                    cache["locales"][locale] = {key: {"source": unit.source, "translation": text} for key, unit in units.items()}
                observed = []

                def translate(locale, batch, **kwargs):
                    observed.append(kwargs)
                    self.assertIs(kwargs["run_state"], state)
                    state.reserve()
                    if not kwargs["single_item_plain"]:
                        raise builder.PartialTranslationError("isolated missing row", {batch[0].key: "공개 연구 보고서입니다"})
                    self.assertEqual(kwargs["attempts"], 1)
                    self.assertEqual([unit.key for unit in batch], [f"{1:064x}"])
                    return {batch[0].key: "공개 연구 보고서입니다"}

                with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "test-key"}, clear=True), mock.patch.object(
                    builder, "deepseek_translate_batch", side_effect=translate,
                ):
                    kwargs = dict(cache_path=Path(directory) / "cache.json.gz", model=builder.DEFAULT_DEEPSEEK_MODEL,
                                  base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2, run_state=state)
                    if request_limit == 1:
                        with self.assertRaises(builder.TranslationStopped):
                            builder.translate_missing_units(units, cache, **kwargs)
                        self.assertEqual(state.data["status"], "failed")
                    else:
                        builder.translate_missing_units(units, cache, **kwargs)
                        self.assertEqual(state.data["status"], "passed")
                self.assertEqual([row["single_item_plain"] for row in observed], [False, True])
                self.assertEqual(state.data["provider_requests"], request_limit)

    def test_http_and_transport_failures_never_enter_repair_queue(self):
        units = self.queue_inventory(2)
        for failure in (401, 402, 403, "transport"):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as directory:
                state = builder.TranslationRun()
                cache = builder.empty_cache()
                for locale, text in (("ja", "公開調査レポートです"), ("ar", "هذا تقرير بحثي عام")):
                    cache["locales"][locale] = {key: {"source": unit.source, "translation": text} for key, unit in units.items()}

                def translator(locale, batch):
                    paid = {batch[0].key: "공개 연구 보고서입니다"}
                    if failure == "transport":
                        raise builder.PartialTranslationError("provider transport failed (OSError)", paid) from OSError("offline")
                    error = builder.ProviderHTTPError(failure, "test")
                    error.partial_translations = paid
                    raise error

                translator = mock.Mock(side_effect=translator)
                with self.assertRaises(builder.TranslationError):
                    builder.translate_missing_units(
                        units, cache, cache_path=Path(directory) / "cache.json.gz", model=builder.DEFAULT_DEEPSEEK_MODEL,
                        base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2,
                        batch_translator=translator, run_state=state,
                    )
                self.assertEqual(translator.call_count, 1)
                self.assertEqual(state.data["deferred_units_total"], 0)
                self.assertEqual(state.data["pending_repairs"], [])

    def test_consecutive_small_omissions_are_repaired_not_misclassified_as_systemic(self):
        units = self.queue_inventory(6)
        state = builder.TranslationRun()
        calls = []
        native = {"ko": "공개 연구 보고서입니다", "ja": "公開調査レポートです", "ar": "هذا تقرير بحثي عام"}

        def translator(locale, batch):
            calls.append(len(batch))
            if len(batch) == 2:
                raise builder.PartialTranslationError("isolated missing row", {batch[0].key: native[locale]})
            return {batch[0].key: native[locale]}

        with tempfile.TemporaryDirectory() as directory:
            builder.translate_missing_units(
                units, builder.empty_cache(), cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=1, timeout=1, attempts=2, max_batch_items=2,
                batch_translator=translator, run_state=state,
            )
        self.assertEqual(calls, [2] * 9 + [1] * 9)
        self.assertFalse(state.stop_reason)
        self.assertEqual(state.data["pending_repair_count"], 0)
        self.assertEqual(state.data["repaired_units"], 9)
        self.assertEqual(state.data["status"], "passed")

    def test_pending_queue_stops_at_1024_rows_without_dispatching_repairs(self):
        units = self.queue_inventory(2560)
        state, calls = builder.TranslationRun(), []
        cache = builder.empty_cache()
        for locale, text in (("ja", "公開調査レポートです"), ("ar", "هذا تقرير بحثي عام")):
            cache["locales"][locale] = {key: {"source": unit.source, "translation": text} for key, unit in units.items()}

        def translator(locale, batch):
            calls.append(len(batch))
            if int(batch[0].key, 16) // 5 % 2 == 0:
                raise builder.PartialTranslationError("isolated four missing rows", {batch[0].key: "공개 연구 보고서입니다"})
            return {unit.key: "공개 연구 보고서입니다" for unit in batch}

        with tempfile.TemporaryDirectory() as directory, self.assertRaises(builder.TranslationStopped):
            builder.translate_missing_units(
                units, cache, cache_path=Path(directory) / "cache.json.gz", model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2,
                max_batch_items=5, batch_translator=translator, run_state=state,
            )
        self.assertEqual(len(calls), 511)
        self.assertTrue(all(size == 5 for size in calls))
        self.assertEqual(state.data["pending_repair_count"], 1024)
        self.assertIn("queue limit", state.stop_reason)


class RepairQueueSchedulingTests(unittest.TestCase):
    @staticmethod
    def inventory_and_cache(count):
        units = PartialBatchTests.queue_inventory(count)
        cache = builder.empty_cache()
        for locale, text in (("ja", "公開調査レポートです"), ("ar", "هذا تقرير بحثي عام")):
            cache["locales"][locale] = {key: {"source": unit.source, "translation": text} for key, unit in units.items()}
        return units, cache

    def test_repair_concurrency_is_bounded_and_cache_updates_stay_on_coordinator(self):
        import threading

        for workers in (1, 3, 8, 16):
            with self.subTest(workers=workers), tempfile.TemporaryDirectory() as directory:
                units, cache = self.inventory_and_cache(36)
                state = builder.TranslationRun()
                width = min(8, workers)
                barrier, lock = threading.Barrier(width), threading.Lock()
                active = peak = repairs = 0
                coordinator = threading.get_ident()
                mutations = []
                original_row = builder._translation_cache_row

                def cache_row(unit, text):
                    mutations.append(threading.get_ident())
                    return original_row(unit, text)

                def translator(locale, batch):
                    nonlocal active, peak, repairs
                    if len(batch) > 1:
                        raise builder.PartialTranslationError("small gap", {batch[0].key: "공개 연구 보고서입니다"})
                    with lock:
                        active += 1
                        peak = max(peak, active)
                        repairs += 1
                    try:
                        barrier.wait(timeout=5)
                        return {batch[0].key: "공개 연구 보고서입니다"}
                    finally:
                        with lock:
                            active -= 1

                with mock.patch.object(builder, "_translation_cache_row", side_effect=cache_row):
                    builder.translate_missing_units(
                        units, cache, cache_path=Path(directory) / "cache.json.gz",
                        model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                        workers=workers, timeout=1, attempts=2, max_batch_items=3,
                        batch_translator=translator, run_state=state,
                    )
                self.assertEqual(peak, width)
                self.assertEqual(repairs, 24)
                self.assertEqual(set(mutations), {coordinator})
                self.assertEqual(state.data["repair_workers"], width)
                self.assertEqual(state.data["pending_repair_count"], 0)

    def test_fifteen_minute_dispatch_deadline_saves_unattempted_queue(self):
        units, cache = self.inventory_and_cache(10)
        state, clock = builder.TranslationRun(), [0.0]
        repaired = []

        def translator(locale, batch):
            if len(batch) > 1:
                raise builder.PartialTranslationError("small gap", {batch[0].key: "공개 연구 보고서입니다"})
            repaired.append(batch[0].key)
            clock[0] = 901.0
            return {batch[0].key: "공개 연구 보고서입니다"}

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cache.json.gz"
            with mock.patch.object(builder.time, "monotonic", side_effect=lambda: clock[0]), self.assertRaisesRegex(
                builder.TranslationStopped, "dispatch time limit",
            ):
                builder.translate_missing_units(
                    units, cache, cache_path=path, model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", workers=1, timeout=1, attempts=2,
                    max_batch_items=2, batch_translator=translator, run_state=state,
                )
            self.assertEqual(len(repaired), 1)
            stored = builder.load_cache(path)
            self.assertEqual(len(stored["locales"]["ko"]), 6)
        self.assertTrue(state.data["repair_dispatch_limit_reached"])
        self.assertEqual(state.data["repair_dispatch_limit_seconds"], 900)
        self.assertEqual(state.data["pending_repair_count"], 4)
        self.assertTrue(all(row["repair_attempts"] == 0 for row in state.data["pending_repairs"]))
        self.assertEqual(state.data["status"], "failed")

    def test_repair_checkpoints_after_sixty_seconds_even_without_completed_response(self):
        import threading

        units, cache = self.inventory_and_cache(2)
        state, clock = builder.TranslationRun(), [0.0]
        release = threading.Event()
        actual_wait = builder.concurrent.futures.wait
        actual_write = builder.write_cache
        checkpointed = []

        def translator(locale, batch):
            if len(batch) > 1:
                raise builder.PartialTranslationError("small gap", {batch[0].key: "공개 연구 보고서입니다"})
            self.assertTrue(release.wait(timeout=5))
            return {batch[0].key: "공개 연구 보고서입니다"}

        def wait(futures, **kwargs):
            if "repair_workers" in state.data and clock[0] == 0:
                clock[0] = 65.0
                self.assertEqual(kwargs["timeout"], 60)
                return set(), set(futures)
            return actual_wait(futures, **kwargs)

        def write(path, value):
            actual_write(path, value)
            if clock[0] == 65 and state.data["repaired_units"] == 0:
                checkpointed.append(len(value["locales"]["ko"]))
                release.set()

        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            builder.time, "monotonic", side_effect=lambda: clock[0],
        ), mock.patch.object(builder.concurrent.futures, "wait", side_effect=wait), mock.patch.object(
            builder, "write_cache", side_effect=write,
        ):
            builder.translate_missing_units(
                units, cache, cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=1, timeout=1, attempts=2, max_batch_items=2,
                batch_translator=translator, run_state=state,
            )
        self.assertEqual(checkpointed, [1])
        self.assertEqual(state.data["status"], "passed")

    def test_parallel_repairs_cannot_exceed_shared_request_budget(self):
        units, cache = self.inventory_and_cache(24)
        state = builder.TranslationRun(max_requests=3)
        real_calls = []

        def translator(locale, batch):
            if len(batch) > 1:
                raise builder.PartialTranslationError("small gap", {batch[0].key: "공개 연구 보고서입니다"})
            state.reserve()
            real_calls.append(batch[0].key)
            return {batch[0].key: "공개 연구 보고서입니다"}

        with tempfile.TemporaryDirectory() as directory, self.assertRaises(builder.TranslationStopped):
            builder.translate_missing_units(
                units, cache, cache_path=Path(directory) / "cache.json.gz",
                model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                workers=8, timeout=1, attempts=2, max_batch_items=2,
                batch_translator=translator, run_state=state,
            )
        self.assertEqual(state.data["provider_requests"], 3)
        self.assertEqual(len(real_calls), 3)
        self.assertEqual(state.data["repaired_units"], 3)
        self.assertEqual(state.data["pending_repair_count"], 9)


if __name__ == "__main__":
    unittest.main()
