#!/usr/bin/env python3
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout
from decimal import Decimal
import io
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import Mock, patch

import requests

from deepseek_http import request_with_key_fallback, request_with_retry
from deepseek_usage import record_attempt
from summarize_deepseek_usage import load_prices, markdown_report, summarize

USAGE = {
    "prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120,
    "prompt_cache_hit_tokens": 70, "prompt_cache_miss_tokens": 30,
}


def response(status: int = 200, usage=USAGE) -> Mock:
    result = Mock(status_code=status, headers={}, text="private response body")
    result.json.return_value = {
        "id": "private-id", "usage": usage,
        "choices": [{"message": {"content": "private generated report"}}],
        "error": "private original error",
    }
    return result


class DeepSeekUsageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.events = self.root / "events"
        environment = patch.dict(os.environ, {
            "DEEPSEEK_USAGE_DIR": str(self.events),
            "DEEPSEEK_USAGE_STAGE": "report-notes",
            "GITHUB_WORKFLOW": "Daily reports",
            "GITHUB_JOB": "process-shard",
            "GITHUB_RUN_ID": "123456", "GITHUB_RUN_ATTEMPT": "1",
        }, clear=True)
        environment.start()
        self.addCleanup(environment.stop)

    def request(self, **overrides):
        options = {
            "headers": {"Authorization": "Bearer private-key"},
            "payload": {"model": "deepseek-flash", "messages": [{"content": "private source"}]},
            "label": "private report title", "max_attempts": 1,
            "logger": Mock(), "retry_base_seconds": 0,
        }
        options.update(overrides)
        return request_with_retry("https://private-endpoint/chat/completions", **options)

    def read_events(self):
        return [json.loads(p.read_text()) for p in sorted(self.events.rglob("*.json"))]

    @patch("deepseek_http.requests.post")
    def test_response_usage_only_no_content_credentials_or_titles(self, post):
        post.return_value = response()
        self.request()
        [event] = self.read_events()
        self.assertEqual(event["usage"], USAGE)
        self.assertEqual(event["model"], "deepseek-flash")
        self.assertEqual(event["stage"], "report-notes")
        self.assertEqual(event["workflow"], "Daily reports")
        self.assertEqual(event["run_attempt"], "1")
        self.assertIn("test_deepseek_usage", event["operation"])
        self.assertNotIn("private", json.dumps(event))
        self.assertEqual(event["outcome"], "success")

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_every_physical_attempt_is_counted_and_missing_usage_is_explicit(self, post, sleep):
        post.side_effect = [requests.exceptions.Timeout("private connection string"), response(429, None), response()]
        self.request(max_attempts=3)
        events = sorted(self.read_events(), key=lambda row: row["attempt"])
        self.assertEqual([row["attempt"] for row in events], [1, 2, 3])
        self.assertEqual([row["outcome"] for row in events], ["transport_error", "http_error", "success"])
        self.assertEqual(len({row["request_id"] for row in events}), 1)
        summary = summarize([self.events])
        self.assertEqual(summary["totals"]["http_attempts"], 3)
        self.assertEqual(summary["totals"]["retry_attempts"], 2)
        self.assertEqual(summary["totals"]["usage_missing_attempts"], 2)
        self.assertEqual(summary["totals"]["prompt_tokens"], 100)
        self.assertIsNone(summary["totals"]["estimated_cost_cny"])
        self.assertNotIn("private", json.dumps(events))

    @patch("deepseek_http.requests.post")
    def test_key_failover_is_one_logical_request_without_key_labels(self, post):
        post.side_effect = [response(402, None), response()]
        request_with_key_fallback(
            "https://private-endpoint", headers={}, payload={"model": "deepseek-flash"},
            label="private report", api_keys=[("private primary", "private-key"), ("private fallback", "other-key")],
            logger=Mock(), max_attempts=1,
        )
        events = self.read_events()
        self.assertEqual(sorted(row["key_index"] for row in events), [1, 2])
        self.assertEqual(len({row["request_id"] for row in events}), 1)
        self.assertNotIn("private", json.dumps(events))
        self.assertEqual(summarize([self.events])["totals"]["key_failover_attempts"], 1)

    @patch("deepseek_http.requests.post")
    def test_model_fallback_attempts_are_observed_without_changing_retry_limit(self, post):
        rejected = response(400, None)
        rejected.text = "Unsupported model. Supported model: deepseek-flash"
        post.side_effect = [rejected, response()]
        self.request(payload={"model": "retired-model"})
        events = sorted(self.read_events(), key=lambda row: row["attempt"])
        self.assertEqual([row["model_switches"] for row in events], [0, 1])
        self.assertEqual([row["attempt"] for row in events], [1, 2])
        self.assertEqual(len({row["request_id"] for row in events}), 1)

    @patch("deepseek_http.requests.post")
    def test_copied_artifacts_deduplicate_but_actual_reruns_remain_billed(self, post):
        post.return_value = response()
        self.request()
        with patch.dict(os.environ, {"GITHUB_RUN_ATTEMPT": "2"}):
            self.request()
        duplicate = self.root / "downloaded-again"
        shutil.copytree(self.events, duplicate)
        summary = summarize([self.events, duplicate])
        self.assertEqual(summary["totals"]["http_attempts"], 2)
        self.assertEqual(summary["totals"]["total_tokens"], 240)
        self.assertEqual(summary["duplicate_events_ignored"], 2)
        self.assertEqual({row["run_attempt"] for row in summary["groups"]}, {"1", "2"})

    def test_atomic_concurrent_writes_are_complete_unique_events(self):
        def write(index):
            record_attempt(
                request_id=str(index), operation="test.concurrent", model="deepseek-flash",
                attempt=1, retry_attempt=1, model_switches=0, key_index=1,
                elapsed_ms=5, response=response(),
            )
        with ThreadPoolExecutor(max_workers=16) as pool:
            list(pool.map(write, range(160)))
        self.assertEqual(len(self.read_events()), 160)
        self.assertEqual(list(self.events.rglob("*.tmp")), [])
        summary = summarize([self.events])
        self.assertEqual(summary["totals"]["prompt_tokens"], 16000)
        self.assertEqual(summary["invalid_files"], 0)

    @patch("deepseek_http.requests.post")
    def test_accounting_failure_does_not_repeat_successful_paid_request(self, post):
        post.return_value = response()
        self.events.write_text("not a directory")
        with redirect_stdout(io.StringIO()) as output:
            result = self.request()
        post.assert_called_once()
        self.assertEqual(result.status_code, 200)
        self.assertIn("totals may be incomplete", output.getvalue())
        self.assertNotIn(str(self.events), output.getvalue())

    @patch("deepseek_http.requests.post")
    def test_date_filter_uses_billing_timezone_and_ignores_summary_files(self, post):
        post.return_value = response()
        self.request()
        [path] = list(self.events.rglob("*.json"))
        event = json.loads(path.read_text())
        event["occurred_at"] = "2026-09-19T17:00:00+00:00"
        path.write_text(json.dumps(event))
        (self.events / "summary.json").write_text(json.dumps({"totals": USAGE}))
        self.assertEqual(summarize([self.events], date="2026-09-20")["totals"]["http_attempts"], 1)
        self.assertEqual(summarize([self.events], date="2026-09-19")["totals"]["http_attempts"], 0)
        self.assertEqual(summarize([self.events], date="2026-09-19", timezone="UTC")["totals"]["http_attempts"], 1)

    @patch("deepseek_http.requests.post")
    def test_configured_cost_is_explicit_estimate_and_missing_usage_is_not_free(self, post):
        post.side_effect = [response(), response(200, {"prompt_tokens": 10, "completion_tokens": 2})]
        self.request()
        self.request()
        rates = {"deepseek-flash": {"input_cache_hit": Decimal("1"), "input_cache_miss": Decimal("2"), "output": Decimal("3")}}
        summary = summarize([self.events], prices=rates)
        self.assertEqual(Decimal(summary["totals"]["estimated_cost_cny"]), Decimal("0.00019"))
        self.assertEqual(summary["totals"]["unpriced_usage_attempts"], 1)
        self.assertEqual(summary["totals"]["missing_token_fields"]["prompt_cache_hit_tokens"], 1)
        self.assertIn("estimate, not provider invoice", summary["cost_basis"])
        self.assertIn("not a DeepSeek invoice", markdown_report(summary))

    def test_prices_reject_invalid_or_incomplete_rates(self):
        path = self.root / "prices.json"
        for rates in ({}, {"input_cache_hit": "NaN", "input_cache_miss": 1, "output": 1}, {"input_cache_hit": -1, "input_cache_miss": 1, "output": 1}):
            path.write_text(json.dumps({"deepseek-flash": rates}))
            with self.assertRaises(ValueError):
                load_prices(path)

    @patch("deepseek_http.requests.post")
    def test_unknown_or_malformed_provider_counters_are_not_invented(self, post):
        post.return_value = response(200, {"prompt_tokens": -1, "completion_tokens": "20", "total_tokens": True})
        self.request()
        [event] = self.read_events()
        self.assertFalse(event["usage_reported"])
        self.assertTrue(all(value is None for value in event["usage"].values()))
        self.assertEqual(summarize([self.events])["totals"]["usage_missing_attempts"], 1)


if __name__ == "__main__":
    unittest.main()
