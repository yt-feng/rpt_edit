from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
import os
import threading
import traceback
import unittest
from unittest import mock

import requests

from deepl_locale_repair import (
    API_ROOT, MAX_REPAIR_BODY_BYTES, DeepLQuotaExhausted, DeepLRepair, DeepLRepairError,
    _payload_size, _translation_payload, pack_repair_indexes,
)


class Response:
    def __init__(self, payload=None, status=200):
        self.status_code = status
        self.payload = payload

    def json(self):
        if isinstance(self.payload, Exception):
            raise self.payload
        return self.payload


class Transport:
    def __init__(self, *, count=288, limit=500000, response=None):
        self.usage = Response({"character_count": count, "character_limit": limit})
        self.response = response
        self.gets = []
        self.posts = []

    def get(self, url, **kwargs):
        self.gets.append((url, kwargs))
        if isinstance(self.usage, Exception):
            raise self.usage
        return self.usage

    def post(self, url, **kwargs):
        self.posts.append((url, kwargs))
        if isinstance(self.response, Exception):
            raise self.response
        if callable(self.response):
            return self.response(url, **kwargs)
        return self.response or Response({"translations": [{
            "text": kwargs["json"]["text"][0], "billed_characters": 1,
        }]})


class DeepLRepairTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ, {"DEEPL_API_KEY": "test-only-deepl-key"})
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_all_locales_one_usage_lookup_and_one_text_per_post(self):
        transport = Transport()
        repair = DeepLRepair(transport=transport)
        for locale, expected in (("ko", "KO"), ("ja", "JA"), ("ar", "AR")):
            self.assertEqual(repair.translate(locale, "待补译文字"), "待补译文字")
            url, args = transport.posts[-1]
            self.assertEqual(url, API_ROOT + "/translate")
            self.assertEqual(len(args["json"]["text"]), 1)
            self.assertEqual(args["json"]["target_lang"], expected)
            self.assertTrue(args["json"]["show_billed_characters"])
            self.assertEqual(args["json"]["tag_handling"], "xml")
            self.assertEqual(args["json"]["ignore_tags"], ["x"])
        self.assertEqual(len(transport.gets), 1)
        self.assertEqual(transport.gets[0][0], API_ROOT + "/usage")
        for _, kwargs in transport.gets + transport.posts:
            self.assertFalse(kwargs["allow_redirects"])
            self.assertLessEqual(kwargs["timeout"], 30)
            self.assertEqual(kwargs["headers"]["Authorization"], "DeepL-Auth-Key test-only-deepl-key")
        stats = repair.snapshot()
        self.assertEqual(stats["provider_requests"], 3)
        self.assertEqual(stats["balance_requests"], 1)
        self.assertEqual(stats["billed_characters"], 3)
        self.assertEqual(stats["reserved_characters"], 0)
        self.assertEqual(stats["remaining_character_budget"], 499709)
        self.assertNotIn("test-only-deepl-key", json.dumps(stats))
        self.assertNotIn("待补译文字", json.dumps(stats))

    def test_escapes_source_and_preserves_every_placeholder_occurrence(self):
        source = 'A & B < 9 "quoted" __KC_PH_000__ __KC_PH_000__ __KC_PH_23__'
        transport = Transport()
        repair = DeepLRepair(transport=transport)
        self.assertEqual(repair.translate("ja", source), source)
        sent = transport.posts[0][1]["json"]["text"][0]
        self.assertIn("A &amp; B &lt; 9", sent)
        self.assertIn('<x id="0">__KC_PH_000__</x>', sent)
        self.assertIn('<x id="1">__KC_PH_000__</x>', sent)
        self.assertIn('<x id="2">__KC_PH_23__</x>', sent)

    def test_placeholder_order_can_follow_target_language(self):
        transport = Transport(response=Response({"translations": [{
            "text": '<t>일본어 <x id="1">__KC_PH_001__</x> 다음 <x id="0">__KC_PH_000__</x></t>',
            "billed_characters": 10,
        }]}))
        self.assertEqual(
            DeepLRepair(transport=transport).translate("ko", "内容 __KC_PH_000__ __KC_PH_001__"),
            "일본어 __KC_PH_001__ 다음 __KC_PH_000__",
        )

    def test_rejects_malformed_or_changed_xml_but_accounts_billed_usage(self):
        invalid = [
            "not XML", "<t>missing end", "<other>text</other>", '<t changed="yes">text</t>',
            "<!DOCTYPE t [<!ENTITY leaked 'value'>]><t>&leaked;</t>",
            "<?xml version='1.0'?><t>text</t>", "<t><!-- discarded -->text</t>",
            '<t><x id="0">__KC_PH_001__</x></t>',
            '<t><x id="0" extra="yes">__KC_PH_000__</x></t>',
            '<t><x id="0"><b>__KC_PH_000__</b></x></t>',
            '<t><y id="0">__KC_PH_000__</y></t>',
            '<t><x id="0">__KC_PH_000__</x><x id="0">__KC_PH_000__</x></t>',
            '<t><x id="8">__KC_PH_000__</x></t>',
            "<t>missing protected marker</t>",
            '<t><x id="0">__KC_PH_000__</x> __KC_PH_777__</t>',
            '<t><x id="0">__KC_PH_000__</x> __KC_PH_000__</t>',
        ]
        for text in invalid:
            with self.subTest(text=text):
                transport = Transport(response=Response({"translations": [{"text": text, "billed_characters": 5}]}))
                repair = DeepLRepair(transport=transport)
                with self.assertRaises(DeepLRepairError):
                    repair.translate("ar", "原文 __KC_PH_000__")
                self.assertEqual(len(transport.posts), 1)
                self.assertEqual(repair.snapshot()["billed_characters"], 5)
                self.assertEqual(repair.snapshot()["reserved_characters"], 0)

    def test_rejects_empty_translation(self):
        transport = Transport(response=Response({"translations": [{"text": "<t> </t>", "billed_characters": 1}]}))
        with self.assertRaises(DeepLRepairError):
            DeepLRepair(transport=transport).translate("ko", "文字")

    def test_request_cap_has_no_hidden_post_or_usage_after_exhaustion(self):
        transport = Transport()
        repair = DeepLRepair(max_requests=1, transport=transport)
        repair.translate("ja", "文字")
        for _ in range(3):
            with self.assertRaises(DeepLQuotaExhausted):
                repair.translate("ja", "下一条")
        self.assertEqual(len(transport.posts), 1)
        self.assertEqual(len(transport.gets), 1)

    def test_zero_request_allowance_does_not_even_fetch_usage(self):
        transport = Transport()
        with self.assertRaises(DeepLQuotaExhausted):
            DeepLRepair(max_requests=0, transport=transport).translate("ja", "文字")
        self.assertEqual(transport.gets, [])
        self.assertEqual(transport.posts, [])

    def test_character_reservation_uses_utf8_and_preserves_1000_character_margin(self):
        transport = Transport(count=0, limit=1005)
        repair = DeepLRepair(transport=transport)
        for _ in range(2):
            with self.assertRaises(DeepLQuotaExhausted):
                repair.translate("ja", "文字")  # 2 codepoints, 6 UTF-8 bytes.
        self.assertEqual(len(transport.gets), 1)
        self.assertEqual(transport.posts, [])

    def test_unknown_billing_keeps_reservation_and_text_without_blocking_distinct_work(self):
        for billed in (None, "1", True, -1):
            with self.subTest(billed=billed):
                transport = Transport(response=Response({"translations": [{"text": "<t>翻訳</t>", "billed_characters": billed}]}))
                repair = DeepLRepair(transport=transport)
                self.assertEqual(repair.translate("ja", "文字"), "翻訳")
                retained = _payload_size(transport.posts[0][1]["json"])
                with self.assertRaises(DeepLRepairError):
                    repair.translate("ja", "文字")
                transport.response = Response({"translations": [{"text": "<t>次</t>", "billed_characters": 1}]})
                self.assertEqual(repair.translate("ja", "另一个"), "次")
                stats = repair.snapshot()
                self.assertEqual(stats["reserved_characters"], retained)
                self.assertEqual(stats["unobserved_requests"], 1)
                self.assertEqual(stats["billed_characters"], 1)
                self.assertEqual(stats["stop_reason"], "")
                self.assertEqual(stats["consecutive_uncertain_responses"], 0)
                self.assertEqual(len(transport.posts), 2)

    def test_numeric_bill_over_reserved_amount_is_charged_and_stops_future_posts(self):
        transport = Transport(response=Response({"translations": [{"text": "<t>翻訳</t>", "billed_characters": 100000}]}))
        repair = DeepLRepair(transport=transport)
        self.assertEqual(repair.translate("ja", "文字"), "翻訳")
        with self.assertRaisesRegex(DeepLRepairError, "exceeded reservation"):
            repair.translate("ja", "其他文字")
        stats = repair.snapshot()
        self.assertEqual(stats["reserved_characters"], 0)
        self.assertEqual(stats["billed_characters"], 100000)
        self.assertEqual(stats["remaining_character_budget"], 399712)
        self.assertEqual(stats["billing_over_reservation_responses"], 1)
        self.assertEqual(len(transport.posts), 1)

    def test_xml_markup_bill_above_old_source_only_bound_is_pre_reserved(self):
        transport = Transport(response=Response({"translations": [{"text": "<t>翻訳</t>", "billed_characters": 15}]}))
        repair = DeepLRepair(transport=transport)
        self.assertEqual(repair.translate("ja", "a"), "翻訳")
        self.assertEqual(repair.snapshot()["billed_characters"], 15)
        self.assertEqual(repair.snapshot()["stop_reason"], "")
        self.assertEqual(repair.snapshot()["unobserved_requests"], 0)

    def test_three_consecutive_uncertain_responses_preserve_text_then_stop(self):
        transport = Transport(response=Response({"translations": [{"text": "<t>翻訳</t>"}]}))
        repair = DeepLRepair(transport=transport)
        for source in ("first", "second", "third"):
            self.assertEqual(repair.translate("ja", source), "翻訳")
        with self.assertRaisesRegex(DeepLRepairError, "repeated uncertain"):
            repair.translate("ja", "fourth")
        stats = repair.snapshot()
        self.assertEqual(stats["unobserved_requests"], 3)
        self.assertEqual(stats["consecutive_uncertain_responses"], 3)
        self.assertEqual(stats["uncertainty_reasons"], {"billing_missing": 3})
        self.assertEqual(stats["reserved_characters"], sum(_payload_size(kwargs["json"]) for _, kwargs in transport.posts))
        self.assertEqual(len(transport.posts), 3)
        self.assertEqual(len(transport.gets), 1)

    def test_unknown_billing_cannot_spend_retained_reservations_again(self):
        reservation = _payload_size(_translation_payload("ja", ["<t>a</t>"]))
        transport = Transport(count=0, limit=1000 + 2 * reservation,
                              response=Response({"translations": [{"text": "<t>翻訳</t>"}]}))
        repair = DeepLRepair(transport=transport)
        self.assertEqual(repair.translate("ja", "a"), "翻訳")
        self.assertEqual(repair.translate("ja", "b"), "翻訳")
        with self.assertRaises(DeepLQuotaExhausted):
            repair.translate("ja", "c")
        stats = repair.snapshot()
        self.assertEqual(stats["remaining_character_budget"], 1000)
        self.assertEqual(stats["reserved_characters"], 2 * reservation)
        self.assertEqual(stats["billed_characters"], 0)
        self.assertEqual(stats["provider_requests"], 2)
        self.assertEqual(stats["unobserved_requests"], 2)

    def test_temporary_failure_allows_distinct_work_not_a_blind_source_replay(self):
        failures = (
            requests.Timeout("test-only-deepl-key"),
            Response({}, status=429), Response({}, status=503),
            Response({"translations": []}),
        )
        for failure in failures:
            with self.subTest(failure_type=type(failure).__name__):
                transport = Transport(response=failure)
                repair = DeepLRepair(transport=transport)
                with self.assertRaises(DeepLRepairError):
                    repair.translate("ko", "first")
                retained = repair.snapshot()["reserved_characters"]
                self.assertGreater(retained, 0)
                self.assertEqual(repair.snapshot()["stop_reason"], "")
                transport.response = Response({"translations": [{"text": "<t>한국어</t>", "billed_characters": 3}]})
                with self.assertRaisesRegex(DeepLRepairError, "already submitted"):
                    repair.translate("ko", "first")
                self.assertEqual(repair.translate("ko", "second"), "한국어")
                stats = repair.snapshot()
                self.assertEqual(stats["reserved_characters"], retained)
                self.assertEqual(stats["billed_characters"], 3)
                self.assertEqual(stats["consecutive_uncertain_responses"], 0)
                self.assertEqual(len(transport.posts), 2)
                self.assertNotIn("test-only-deepl-key", json.dumps(stats))

    def test_http_errors_never_retry_or_fall_back(self):
        for status in (301, 400, 401, 403, 429, 456, 500, 503):
            with self.subTest(status=status):
                transport = Transport(response=Response({"error": "test-only-deepl-key"}, status=status))
                repair = DeepLRepair(transport=transport)
                error = DeepLQuotaExhausted if status == 456 else DeepLRepairError
                for _ in range(2):
                    with self.assertRaises(error) as caught:
                        repair.translate("ja", "文字")
                    self.assertNotIn("test-only-deepl-key", str(caught.exception))
                self.assertEqual(len(transport.posts), 1)
                self.assertEqual(repair.snapshot()["reserved_characters"], _payload_size(transport.posts[0][1]["json"]))

    def test_transport_failure_retains_reservation_and_sanitizes_exception(self):
        transport = Transport(response=requests.ConnectionError("Authorization test-only-deepl-key"))
        repair = DeepLRepair(transport=transport)
        for _ in range(2):
            with self.assertRaises(DeepLRepairError) as caught:
                repair.translate("ar", "文字")
            self.assertNotIn("test-only-deepl-key", str(caught.exception))
        self.assertEqual(len(transport.posts), 1)
        self.assertEqual(repair.snapshot()["reserved_characters"], _payload_size(transport.posts[0][1]["json"]))
        self.assertEqual(repair.snapshot()["unobserved_requests"], 1)

    def test_missing_or_invalid_result_stops_without_losing_reservation(self):
        for payload in (None, [], {}, {"translations": []}, {"translations": [{}, {}]}, ValueError("sensitive body")):
            with self.subTest(payload=payload):
                transport = Transport(response=Response(payload))
                repair = DeepLRepair(transport=transport)
                for _ in range(2):
                    with self.assertRaises(DeepLRepairError):
                        repair.translate("ko", "文字")
                self.assertEqual(len(transport.posts), 1)
                self.assertEqual(repair.snapshot()["reserved_characters"], _payload_size(transport.posts[0][1]["json"]))

    def test_missing_key_blocks_all_network(self):
        with mock.patch.dict(os.environ, {"DEEPL_API_KEY": ""}):
            transport = Transport()
            repair = DeepLRepair(transport=transport)
            with self.assertRaises(DeepLRepairError):
                repair.translate("ko", "文字")
            self.assertEqual(transport.gets, [])
            self.assertEqual(transport.posts, [])

    def test_bad_usage_response_is_not_retried(self):
        for usage in (
            Response({}, status=403), Response({"character_count": "0", "character_limit": 500000}),
            Response({"character_count": False, "character_limit": 500000}),
            Response({"character_count": 0, "character_limit": -1}), Response(ValueError("secret body")),
            requests.Timeout("test-only-deepl-key"),
        ):
            with self.subTest(usage=type(usage).__name__):
                transport = Transport()
                transport.usage = usage
                repair = DeepLRepair(transport=transport)
                for _ in range(2):
                    with self.assertRaises(DeepLRepairError) as caught:
                        repair.translate("ja", "文字")
                    self.assertNotIn("test-only-deepl-key", str(caught.exception))
                self.assertEqual(len(transport.gets), 1)
                self.assertEqual(transport.posts, [])

    def test_usage_transport_failure_sanitizes_full_traceback(self):
        marker = "test-only-deepl-key"
        for error_type in (requests.Timeout, requests.ConnectionError):
            with self.subTest(error_type=error_type.__name__):
                transport = Transport()
                transport.usage = error_type("Authorization: DeepL-Auth-Key " + marker)
                repair = DeepLRepair(transport=transport)
                for _ in range(2):
                    try:
                        repair.translate("ja", "文字")
                    except DeepLRepairError:
                        full_traceback = traceback.format_exc()
                        self.assertIn("DeepL usage request failed; no automatic retry", full_traceback)
                        self.assertNotIn(marker, full_traceback)
                        self.assertNotIn("Authorization:", full_traceback)
                    else:
                        self.fail("Usage transport failure must stop repair")
                self.assertEqual(len(transport.gets), 1)
                self.assertEqual(transport.posts, [])

    def test_concurrent_calls_share_single_usage_lookup_and_request_cap(self):
        transport = Transport()
        repair = DeepLRepair(max_requests=6, transport=transport)

        def attempt(_):
            try:
                return repair.translate("ja", "文字")
            except DeepLQuotaExhausted:
                return None

        with ThreadPoolExecutor(max_workers=12) as pool:
            results = list(pool.map(attempt, range(50)))
        self.assertEqual(sum(result is not None for result in results), 6)
        self.assertEqual(len(transport.posts), 6)
        self.assertEqual(len(transport.gets), 1)
        self.assertEqual(repair.snapshot()["billed_characters"], 6)
        self.assertEqual(repair.snapshot()["reserved_characters"], 0)

    def test_inflight_reservations_prevent_concurrent_quota_overspend(self):
        entered = threading.Barrier(3)
        release = threading.Event()

        def pending_response(url, **kwargs):
            entered.wait(timeout=5)
            if not release.wait(timeout=5):
                raise AssertionError("test release timed out")
            return Response({"translations": [{"text": "<t>訳</t>", "billed_characters": 20}]})

        reservation = _payload_size(_translation_payload("ja", ["<t>" + "中" * 20 + "</t>"]))
        transport = Transport(count=0, limit=1000 + 2 * reservation, response=pending_response)
        repair = DeepLRepair(transport=transport)
        with ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(repair.translate, "ja", "中" * 20)
            second = pool.submit(repair.translate, "ja", "中" * 20)
            try:
                entered.wait(timeout=5)
                self.assertEqual(repair.snapshot()["reserved_characters"], 2 * reservation)
                with self.assertRaises(DeepLQuotaExhausted):
                    repair.translate("ja", "第三条")
            finally:
                release.set()
            self.assertEqual(first.result(), "訳")
            self.assertEqual(second.result(), "訳")
        self.assertEqual(len(transport.posts), 2)
        self.assertEqual(repair.snapshot()["billed_characters"], 40)
        self.assertEqual(repair.snapshot()["reserved_characters"], 0)

    def test_invalid_local_input_has_no_requests(self):
        transport = Transport()
        repair = DeepLRepair(transport=transport)
        for locale, source in (
            ("en", "text"), ("ja", ""), ("ar", "  "), ("ko", None),
            ("ja", "invalid\x00source"), ("ko", "invalid\ud800source"),
        ):
            with self.assertRaises(DeepLRepairError):
                repair.translate(locale, source)
        self.assertEqual(transport.posts, [])
        self.assertEqual(transport.gets, [])
        for maximum in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                DeepLRepair(max_requests=maximum, transport=transport)

    def test_batch_preserves_order_and_per_item_placeholder_namespaces(self):
        sources = ['甲 __KC_PH_000__ __KC_PH_000__', '乙 __KC_PH_000__ __KC_PH_001__', '丙 & <正文>']
        transport = Transport(response=Response({"translations": [
            {"text": '<t>الأول <x id="0">__KC_PH_000__</x> <x id="1">__KC_PH_000__</x></t>', "billed_characters": 3},
            {"text": '<t>الثاني <x id="1">__KC_PH_001__</x> <x id="0">__KC_PH_000__</x></t>', "billed_characters": 4},
            {"text": '<t>الثالث &amp; &lt;نص&gt;</t>', "billed_characters": 5},
        ]}))
        repair = DeepLRepair(transport=transport)
        self.assertEqual(repair.translate_many('ar', sources), [
            'الأول __KC_PH_000__ __KC_PH_000__', 'الثاني __KC_PH_001__ __KC_PH_000__', 'الثالث & <نص>',
        ])
        self.assertEqual(len(transport.gets), 1)
        self.assertEqual(len(transport.posts), 1)
        url, kwargs = transport.posts[0]
        self.assertEqual(url, API_ROOT + '/translate')
        self.assertEqual(kwargs['json']['target_lang'], 'AR')
        self.assertEqual(len(kwargs['json']['text']), 3)
        self.assertIn('<x id="0">__KC_PH_000__</x>', kwargs['json']['text'][0])
        self.assertIn('<x id="0">__KC_PH_000__</x>', kwargs['json']['text'][1])
        stats = repair.snapshot()
        self.assertEqual(stats['provider_requests'], 1)
        self.assertEqual(stats['billed_characters'], 12)
        self.assertEqual(stats['reserved_characters'], 0)
        self.assertEqual(stats['remaining_character_budget'], 500000 - 288 - 12)
        self.assertNotIn('test-only-deepl-key', json.dumps(stats))

    def test_fifty_texts_count_as_one_request_and_fifty_one_never_calls_provider(self):
        def echo(_url, **kwargs):
            return Response({'translations': [{'text': text, 'billed_characters': 1} for text in kwargs['json']['text']]})
        transport = Transport(response=echo)
        repair = DeepLRepair(max_requests=1, transport=transport)
        sources = [f'第{index}项' for index in range(50)]
        self.assertEqual(repair.translate_many('ja', sources), sources)
        with self.assertRaises(DeepLQuotaExhausted):
            repair.translate_many('ja', ['后续'])
        self.assertEqual(len(transport.posts), 1)
        self.assertEqual(repair.snapshot()['billed_characters'], 50)
        for invalid in ([], sources + ['第51项'], 'not-a-list', ['文字', ''], ['文字', None], ['文字', 'invalid\x00source']):
            with self.subTest(invalid_type=type(invalid).__name__):
                unused = Transport()
                with self.assertRaises(DeepLRepairError):
                    DeepLRepair(transport=unused).translate_many('ja', invalid)
                self.assertEqual(unused.gets, [])
                self.assertEqual(unused.posts, [])

    def test_batch_quota_reserves_sum_before_any_translation_post(self):
        transport = Transport(count=0, limit=1007)
        repair = DeepLRepair(transport=transport)
        with self.assertRaises(DeepLQuotaExhausted):
            repair.translate_many('ja', ['文字', '文字'])  # 12 bytes plus the 1000-character margin.
        self.assertEqual(len(transport.gets), 1)
        self.assertEqual(transport.posts, [])
        self.assertEqual(repair.snapshot()['reserved_characters'], 0)

    def test_batch_billing_requires_each_row_not_only_a_plausible_total(self):
        for billed in (None, True, -1):
            with self.subTest(billed=billed):
                transport = Transport(response=Response({'translations': [
                    {'text': '<t>第一</t>', 'billed_characters': 0},
                    {'text': '<t>第二</t>', 'billed_characters': billed},
                ]}))
                repair = DeepLRepair(transport=transport)
                self.assertEqual(repair.translate_many('ja', ['aa', 'b']), ['第一', '第二'])
                with self.assertRaises(DeepLRepairError):
                    repair.translate_many('ja', ['b'])
                self.assertEqual(repair.snapshot()['billed_characters'], 0)
                self.assertEqual(repair.snapshot()['reserved_characters'], _payload_size(transport.posts[0][1]['json']))
                self.assertEqual(repair.snapshot()['unobserved_requests'], 1)
                self.assertEqual(len(transport.posts), 1)
                self.assertEqual(repair.snapshot()['stop_reason'], '')

    def test_wrong_response_count_never_guesses_partial_mapping_or_retries(self):
        for count in (0, 1, 3):
            with self.subTest(count=count):
                transport = Transport(response=Response({'translations': [
                    {'text': '<t>翻訳</t>', 'billed_characters': 1} for _ in range(count)
                ]}))
                repair = DeepLRepair(transport=transport)
                with self.assertRaises(DeepLRepairError) as caught:
                    repair.translate_many('ja', ['甲', '乙'])
                self.assertEqual(caught.exception.partial_translations, {})
                with self.assertRaises(DeepLRepairError):
                    repair.translate_many('ja', ['甲', '乙'])
                self.assertEqual(len(transport.posts), 1)
                self.assertEqual(repair.snapshot()['billed_characters'], 0)
                self.assertEqual(repair.snapshot()['reserved_characters'], _payload_size(transport.posts[0][1]['json']))

    def test_aligned_partial_xml_error_retains_valid_rows_and_all_billed_usage(self):
        transport = Transport(response=Response({'translations': [
            {'text': '<t>第一 <x id="0">__KC_PH_000__</x></t>', 'billed_characters': 2},
            {'text': '<t>missing placeholder</t>', 'billed_characters': 3},
            {'text': '<t>第三</t>', 'billed_characters': 1},
        ]}))
        repair = DeepLRepair(transport=transport)
        with self.assertRaises(DeepLRepairError) as caught:
            repair.translate_many('ja', ['甲 __KC_PH_000__', '乙 __KC_PH_001__', '丙'])
        self.assertEqual(caught.exception.partial_translations, {0: '第一 __KC_PH_000__', 2: '第三'})
        self.assertEqual(repair.snapshot()['billed_characters'], 6)
        self.assertEqual(repair.snapshot()['reserved_characters'], 0)
        self.assertEqual(len(transport.posts), 1)

    def test_aligned_missing_row_preserves_other_text_but_retains_unknown_reservation(self):
        transport = Transport(response=Response({'translations': [
            {'text': '<t>第一</t>', 'billed_characters': 1}, None,
        ]}))
        repair = DeepLRepair(transport=transport)
        with self.assertRaises(DeepLRepairError) as caught:
            repair.translate_many('ja', ['甲', '乙'])
        self.assertEqual(caught.exception.partial_translations, {0: '第一'})
        retained = _payload_size(transport.posts[0][1]['json'])
        self.assertEqual(repair.snapshot()['reserved_characters'], retained)
        self.assertEqual(repair.snapshot()['billed_characters'], 0)
        self.assertEqual(repair.snapshot()['unobserved_requests'], 1)
        with self.assertRaises(DeepLRepairError):
            repair.translate_many('ja', ['乙'])
        self.assertEqual(len(transport.posts), 1)
        transport.response = Response({'translations': [{'text': '<t>次</t>', 'billed_characters': 1}]})
        self.assertEqual(repair.translate_many('ja', ['后续']), ['次'])
        self.assertEqual(repair.snapshot()['reserved_characters'], retained)
        self.assertEqual(len(transport.posts), 2)

    def test_batch_transport_exception_full_traceback_is_sanitized(self):
        marker = 'test-only-deepl-key'
        transport = Transport(response=requests.Timeout('Authorization: ' + marker))
        repair = DeepLRepair(transport=transport)
        try:
            repair.translate_many('ar', ['甲', '乙'])
        except DeepLRepairError:
            output = traceback.format_exc()
            self.assertNotIn(marker, output)
            self.assertNotIn('Authorization:', output)
        else:
            self.fail('Transport failure must fail the batch')
        self.assertEqual(repair.snapshot()['reserved_characters'], _payload_size(transport.posts[0][1]['json']))
        self.assertEqual(repair.snapshot()['unobserved_requests'], 1)
        with self.assertRaises(DeepLRepairError):
            repair.translate_many('ar', ['甲', '乙'])
        self.assertEqual(len(transport.posts), 1)

    def test_packed_long_han_and_placeholder_heavy_sources_have_bounded_actual_requests(self):
        fixtures = [
            [f'{index}' + '中' * 3500 for index in range(50)],
            [f'{index}' + '&<>' * 100 + ' __KC_PH_000__' * 200 for index in range(50)],
        ]
        for sources in fixtures:
            with self.subTest(source_length=len(sources[0])):
                groups = pack_repair_indexes(sources)
                self.assertGreater(len(groups), 1)
                self.assertEqual([index for group in groups for index in group], list(range(len(sources))))
                self.assertTrue(all(1 <= len(group) <= 50 for group in groups))
                observed = []

                def echo(url, **kwargs):
                    prepared = requests.Request('POST', url, json=kwargs['json']).prepare()
                    observed.append(len(prepared.body))
                    self.assertEqual(len(prepared.body), _payload_size(kwargs['json']))
                    self.assertLessEqual(len(prepared.body), MAX_REPAIR_BODY_BYTES)
                    return Response({'translations': [
                        {'text': text, 'billed_characters': 1} for text in kwargs['json']['text']
                    ]})

                transport = Transport(response=echo)
                repair = DeepLRepair(transport=transport)
                restored = []
                for group in groups:
                    restored.extend(repair.translate_many('ar', [sources[index] for index in group]))
                self.assertEqual(restored, sources)
                self.assertEqual(len(observed), len(groups))
                self.assertEqual(len(transport.gets), 1)
                self.assertEqual(repair.snapshot()['provider_requests'], len(groups))
                self.assertEqual(pack_repair_indexes(sources), groups)

    def test_packing_preserves_coverage_and_fifty_item_cap_for_short_sources(self):
        self.assertEqual(pack_repair_indexes([]), [])
        groups = pack_repair_indexes(['短文'] * 101)
        self.assertEqual([len(group) for group in groups], [50, 50, 1])
        self.assertEqual([index for group in groups for index in group], list(range(101)))

    def test_oversized_ascii_encoded_or_xml_expanded_batch_is_blocked_before_any_request(self):
        for sources in (['中' * 3500] * 50, ['&' * 30000], ['中' * 20000]):
            with self.subTest(source_count=len(sources)):
                transport = Transport()
                repair = DeepLRepair(transport=transport)
                with self.assertRaisesRegex(DeepLRepairError, 'request body limit'):
                    repair.translate_many('ja', sources)
                self.assertEqual(transport.gets, [])
                self.assertEqual(transport.posts, [])
                self.assertEqual(repair.snapshot()['reserved_characters'], 0)
        for source in ('&' * 30000, '中' * 20000):
            with self.assertRaisesRegex(DeepLRepairError, 'request body limit'):
                pack_repair_indexes([source])

    def test_exact_body_limit_is_accepted_and_one_more_byte_is_rejected(self):
        overhead = _payload_size(_translation_payload('ko', ['<t></t>']))
        source = 'a' * (MAX_REPAIR_BODY_BYTES - overhead)
        self.assertEqual(pack_repair_indexes([source]), [[0]])
        transport = Transport()
        repair = DeepLRepair(transport=transport)
        self.assertEqual(repair.translate_many('ko', [source]), [source])
        self.assertEqual(_payload_size(transport.posts[0][1]['json']), MAX_REPAIR_BODY_BYTES)
        unused = Transport()
        with self.assertRaisesRegex(DeepLRepairError, 'request body limit'):
            DeepLRepair(transport=unused).translate_many('ko', [source + 'a'])
        self.assertEqual(unused.gets, [])
        self.assertEqual(unused.posts, [])


if __name__ == "__main__":
    unittest.main()
