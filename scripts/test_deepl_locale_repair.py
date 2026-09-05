from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
import os
import threading
import traceback
import unittest
from unittest import mock

import requests

from scripts.deepl_locale_repair import (
    API_ROOT, DeepLQuotaExhausted, DeepLRepair, DeepLRepairError,
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

    def test_unknown_or_over_reserved_billing_preserves_translation_and_stops_new_calls(self):
        for billed in (None, "1", True, -1, 100000):
            with self.subTest(billed=billed):
                transport = Transport(response=Response({"translations": [{"text": "<t>翻訳</t>", "billed_characters": billed}]}))
                repair = DeepLRepair(transport=transport)
                self.assertEqual(repair.translate("ja", "文字"), "翻訳")
                with self.assertRaises(DeepLRepairError):
                    repair.translate("ja", "另一个")
                stats = repair.snapshot()
                self.assertEqual(stats["reserved_characters"], 6)
                self.assertEqual(stats["unobserved_requests"], 1)
                self.assertEqual(stats["billed_characters"], 0)
                self.assertEqual(len(transport.posts), 1)

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
                self.assertEqual(repair.snapshot()["reserved_characters"], 6)

    def test_transport_failure_retains_reservation_and_sanitizes_exception(self):
        transport = Transport(response=requests.ConnectionError("Authorization test-only-deepl-key"))
        repair = DeepLRepair(transport=transport)
        for _ in range(2):
            with self.assertRaises(DeepLRepairError) as caught:
                repair.translate("ar", "文字")
            self.assertNotIn("test-only-deepl-key", str(caught.exception))
        self.assertEqual(len(transport.posts), 1)
        self.assertEqual(repair.snapshot()["reserved_characters"], 6)
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
                self.assertEqual(repair.snapshot()["reserved_characters"], 6)

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

        transport = Transport(count=0, limit=1120, response=pending_response)
        repair = DeepLRepair(transport=transport)
        with ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(repair.translate, "ja", "中" * 20)
            second = pool.submit(repair.translate, "ja", "中" * 20)
            try:
                entered.wait(timeout=5)
                self.assertEqual(repair.snapshot()["reserved_characters"], 120)
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


if __name__ == "__main__":
    unittest.main()
