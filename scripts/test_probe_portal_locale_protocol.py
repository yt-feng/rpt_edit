#!/usr/bin/env python3
"""Offline protocol controls: every transport call is mocked."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe_portal_locale_protocol as probe

SECRET = "FAKE_PROTOCOL_PRIMARY_CREDENTIAL"
KOREAN = "상반기 실적은 예상에 미치지 못했습니다."
ARABIC = "جاءت نتائج النصف الأول دون التوقعات."


def response(payload, *, status=200, echo=False, usage=True):
    text = probe.SOURCE_TEXT if echo else ARABIC if "阿拉伯" in payload["messages"][0]["content"] else KOREAN
    if "response_format" in payload:
        text = json.dumps({"translations": [{"id": "0", "text": text}]}, ensure_ascii=False)
    body = {"model": "returned-" + payload["model"],
            "choices": [{"finish_reason": "stop", "message": {"content": text}}]}
    if usage:
        body["usage"] = {"prompt_tokens": 20, "completion_tokens": 10, "total_tokens": 30}
    result = Mock(status_code=status, headers={"Authorization": SECRET})
    result.json.return_value = body
    return result


class ProtocolProbeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary.name) / "diagnostics.json"
        self.environment = patch.dict("os.environ", {"DEEPSEEK_API_KEY": SECRET,
                                      "DEEPSEEK_API_KEY_BACKUP": "FAKE_BACKUP"}, clear=True)
        self.environment.start()

    def tearDown(self):
        self.environment.stop()
        self.temporary.cleanup()

    def test_four_successful_controls_share_fixed_budget_and_preserve_actual_model(self):
        transport = Mock(side_effect=lambda _url, **kwargs: response(kwargs["payload"]))
        result = probe.run_probe(diagnostics_out=self.path, transport=transport)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(transport.call_count, 4)
        self.assertEqual(result["provider_requests"], 4)
        self.assertEqual(result["usage_totals"]["total_tokens"], 120)
        payloads = [call.kwargs["payload"] for call in transport.call_args_list]
        self.assertEqual({**payloads[0], "model": "deepseek-v4-pro"}, payloads[3])
        for call, row in zip(transport.call_args_list, result["cases"]):
            self.assertEqual(call.kwargs["api_keys"], [("configured", SECRET)])
            self.assertEqual(call.kwargs["max_attempts"], 1)
            self.assertFalse(call.kwargs["allow_model_fallback"])
            self.assertEqual(call.kwargs["payload"]["max_tokens"], 1000)
            self.assertEqual(call.kwargs["payload"]["thinking"], {"type": "disabled"})
            self.assertEqual(row["returned_model"], "returned-" + row["requested_model"])
        self.assertNotIn(SECRET, self.path.read_text())
        self.assertNotIn("Authorization", self.path.read_text())

    def test_echo_quality_failures_continue_through_all_four_controls(self):
        transport = Mock(side_effect=lambda _url, **kwargs: response(kwargs["payload"], echo=True))
        result = probe.run_probe(diagnostics_out=self.path, transport=transport)
        self.assertEqual(transport.call_count, 4)
        self.assertTrue(all("unchanged source" in row["error"] for row in result["cases"]))
        self.assertEqual(result["status"], "failed")

    def test_auth_or_billing_failure_stops_remaining_controls(self):
        for status in (401, 402, 403):
            with self.subTest(status=status):
                transport = Mock(side_effect=lambda _url, **kwargs: response(kwargs["payload"], status=status))
                result = probe.run_probe(diagnostics_out=self.path, transport=transport)
                self.assertEqual(transport.call_count, 1)
                self.assertEqual(result["provider_requests"], 1)
                self.assertIn(str(status), result["stop_reason"])

    def test_transport_failure_stops_without_exposing_exception_details(self):
        transport = Mock(side_effect=RuntimeError("Authorization: Bearer " + SECRET))
        result = probe.run_probe(diagnostics_out=self.path, transport=transport)
        self.assertEqual(transport.call_count, 1)
        self.assertEqual(result["unobserved_provider_requests"], 1)
        self.assertNotIn(SECRET, self.path.read_text())
        self.assertNotIn("Authorization", self.path.read_text())
        self.assertIn("RuntimeError", result["cases"][0]["error"])

    def test_shared_budget_blocks_accidental_fifth_control(self):
        transport = Mock(side_effect=lambda _url, **kwargs: response(kwargs["payload"]))
        with patch.object(probe, "controls", return_value=probe.controls() + (probe.controls()[0],)):
            result = probe.run_probe(diagnostics_out=self.path, transport=transport)
        self.assertEqual(transport.call_count, 4)
        self.assertEqual(result["provider_requests"], 4)
        self.assertIn("limit", result["stop_reason"])

    def test_diagnostics_scrub_credentials_bound_text_and_mark_unknown_usage(self):
        def transport(_url, **kwargs):
            result = response(kwargs["payload"], usage=False)
            body = result.json.return_value
            body["model"] = SECRET + "x" * 150
            body["choices"][0]["finish_reason"] = SECRET
            body["choices"][0]["message"]["content"] = SECRET + KOREAN * 200
            return result
        result = probe.run_probe(diagnostics_out=self.path, transport=transport)
        self.assertNotIn(SECRET, self.path.read_text())
        self.assertEqual(result["usage_unknown_responses"], 4)
        self.assertEqual(result["usage_totals"], {})
        self.assertTrue(all(len(row["translation"]) <= 1200 and len(row["returned_model"]) <= 96 for row in result["cases"]))

    def test_invalid_base_url_never_calls_provider(self):
        transport = Mock()
        result = probe.run_probe(diagnostics_out=self.path, base_url="https://unapproved.example", transport=transport)
        transport.assert_not_called()
        self.assertEqual(result["provider_requests"], 0)
        self.assertEqual(result["status"], "failed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
