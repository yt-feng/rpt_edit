#!/usr/bin/env python3
from __future__ import annotations

import os
import json
import unittest
from unittest.mock import Mock, patch

import requests

from deepseek_http import (
    DEFAULT_DEEPSEEK_MODEL,
    DeepSeekResponseError,
    _main_thread_deadline,
    _post_with_deadline,
    deepseek_api_keys_from_env,
    prepare_deepseek_payload,
    request_with_key_fallback,
    request_with_retry,
)


def http_response(status_code=200, headers=None, text=None, body=None):
    result = requests.Response()
    result.status_code = status_code
    result.headers.update(headers or {})
    result._content = (text if text is not None else json.dumps(
        body if body is not None else {"choices": [{"message": {"content": "complete article"}}]}
    )).encode()
    result._content_consumed = True
    return result


class DeepSeekHttpTests(unittest.TestCase):
    def request(self, **overrides):
        options = {
            "headers": {"Authorization": "Bearer test"},
            "payload": {"model": "deepseek-chat"},
            "label": "test article",
            "max_attempts": 4,
            "retry_base_seconds": 2,
            "retry_max_seconds": 20,
            "retry_jitter_ratio": 0,
            "logger": Mock(),
        }
        options.update(overrides)
        return request_with_retry("https://api.deepseek.com/chat/completions", **options)

    def test_maps_retired_chat_alias_to_canonical_flash(self) -> None:
        payload = prepare_deepseek_payload({"model": "deepseek-chat", "messages": []})

        self.assertEqual(payload["model"], DEFAULT_DEEPSEEK_MODEL)
        self.assertEqual(payload["thinking"], {"type": "disabled"})

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_http_200_provider_timeout_is_retried_before_caller_parses_choices(self, post, sleep):
        failed = http_response(body={"error": {"code": "server_error", "message": "private request timed out"}})
        success = http_response()
        post.side_effect = [failed, success]
        logger = Mock()
        self.assertIs(self.request(logger=logger), success)
        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(2)
        self.assertIn("provider_unavailable", str(logger.call_args))
        self.assertNotIn("private", str(logger.call_args))

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_malformed_successes_exhaust_bounded_retries_without_keyerror(self, post, sleep):
        for body, category in (
            ({}, "missing_choices"),
            ({"choices": []}, "missing_choices"),
            ({"choices": [None]}, "missing_choices"),
            ({"choices": [{"message": {"content": " "}}]}, "missing_content"),
            ({"choices": [{"message": {"content": None}}]}, "missing_content"),
            (["unexpected"], "invalid_envelope"),
            ({"choices": [{"finish_reason": "aborted", "message": {"content": "partial text"}}]}, "generation_interrupted"),
        ):
            with self.subTest(category=category, body=body):
                post.reset_mock()
                post.return_value = http_response(body=body)
                with self.assertRaisesRegex(DeepSeekResponseError, category):
                    self.request(max_attempts=2)
                self.assertEqual(post.call_count, 2)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_non_json_200_can_recover(self, post, sleep):
        post.side_effect = [http_response(text="upstream unavailable"), http_response()]
        self.assertEqual(self.request().json()["choices"][0]["message"]["content"], "complete article")
        self.assertEqual(post.call_count, 2)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_permanent_200_error_does_not_retry_or_switch_keys(self, post, sleep):
        post.return_value = http_response(body={"error": {"code": "invalid_request_error", "message": "private input"}})
        with self.assertRaisesRegex(DeepSeekResponseError, "invalid_request"):
            request_with_key_fallback("https://api.deepseek.com/chat/completions", headers={},
                payload={}, label="test", api_keys=[("primary", "private"), ("backup", "private2")])
        post.assert_called_once()
        sleep.assert_not_called()

    @patch("deepseek_http.requests.post")
    def test_http_200_balance_error_switches_to_configured_backup(self, post):
        success = http_response()
        post.side_effect = [http_response(body={"error": {"code": "insufficient_balance"}}), success]
        result = request_with_key_fallback("https://api.deepseek.com/chat/completions", headers={},
            payload={}, label="test", api_keys=[("primary", "private"), ("backup", "private2")], logger=Mock())
        self.assertIs(result, success)
        self.assertEqual(post.call_count, 2)

    @patch("deepseek_http.time.monotonic")
    @patch("deepseek_http.requests.post")
    def test_keepalive_whitespace_cannot_extend_response_deadline(self, post, monotonic):
        result = Mock()
        result.iter_content.return_value = iter([b"\n", b"\n", b"\n"])
        post.return_value = result
        monotonic.side_effect = [0, 5, 20, 31]
        with self.assertRaisesRegex(requests.exceptions.Timeout, "deadline"):
            _post_with_deadline("https://api.deepseek.com/chat/completions", headers={}, payload={}, timeout=30)
        result.close.assert_called_once()
        result.iter_content.assert_called_once_with(chunk_size=1)
        self.assertEqual(post.call_args.kwargs["timeout"], 30)
        self.assertTrue(post.call_args.kwargs["stream"])

    @patch("deepseek_http.requests.post")
    def test_leading_keepalive_lines_preserve_completed_json(self, post):
        body = {"choices": [{"message": {"content": "中文完整文章"}}]}
        result = http_response(text="\n \n" + json.dumps(body))
        post.return_value = result
        self.assertEqual(self.request().json(), body)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_single_attempt_contract_preserved_for_semantic_failure(self, post, sleep):
        post.return_value = http_response(body={"error": "Request timeout"})
        with self.assertRaises(DeepSeekResponseError):
            self.request(max_attempts=1)
        post.assert_called_once()
        sleep.assert_not_called()

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_metered_self_validating_caller_can_receive_original_envelope(self, post, sleep):
        failed = http_response(body={"error": "Request timeout"})
        post.return_value = failed
        result = request_with_key_fallback("https://api.deepseek.com/chat/completions", headers={},
            payload={}, label="test", api_keys=[("configured", "private")], max_attempts=1,
            allow_model_fallback=False, validate_completion=False, logger=Mock())
        self.assertIs(result, failed)
        post.assert_called_once()
        sleep.assert_not_called()

    @patch("deepseek_http.requests.post")
    def test_unrecognized_error_numbers_do_not_change_error_classification(self, post):
        post.return_value = http_response(body={"error": {"message": "private report 400 and 503"}})
        with self.assertRaisesRegex(DeepSeekResponseError, "provider_error"):
            self.request(max_attempts=1)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_permanent_code_takes_precedence_over_transient_message_phrase(self, post, sleep):
        post.return_value = http_response(body={"error": {"code": "context_length_exceeded", "message": "input includes request timeout"}})
        with self.assertRaisesRegex(DeepSeekResponseError, "invalid_request"):
            self.request(max_attempts=3)
        post.assert_called_once()
        sleep.assert_not_called()

    @patch("deepseek_http.requests.post")
    def test_response_size_limit_closes_stream_without_retry(self, post):
        result = Mock()
        result.iter_content.return_value = iter([b"123", b"456"])
        post.return_value = result
        with patch("deepseek_http.MAX_COMPLETION_RESPONSE_BYTES", 5):
            with self.assertRaisesRegex(DeepSeekResponseError, "response_too_large"):
                self.request()
        post.assert_called_once()
        result.close.assert_called_once()

    @patch("deepseek_http.signal.getitimer", return_value=(0, 0))
    @patch("deepseek_http.signal.getsignal", return_value="previous_handler")
    @patch("deepseek_http.signal.signal")
    @patch("deepseek_http.signal.setitimer")
    def test_main_thread_deadline_interrupts_silent_io_and_restores_handler(self, timer, handler, getsignal, gettimer):
        with self.assertRaisesRegex(requests.exceptions.Timeout, "deadline"):
            with _main_thread_deadline(300):
                expired = handler.call_args.args[1]
                expired(None, None)
        self.assertEqual([call.args[1] for call in timer.call_args_list], [300, 0])
        self.assertEqual(handler.call_args.args[1], "previous_handler")

    @patch("deepseek_http.signal.getitimer", return_value=(20, 0))
    @patch("deepseek_http.signal.signal")
    @patch("deepseek_http.signal.setitimer")
    def test_existing_alarm_is_never_overwritten(self, timer, handler, gettimer):
        with _main_thread_deadline(300):
            pass
        handler.assert_not_called()
        timer.assert_not_called()

    @patch("deepseek_http.threading.current_thread", return_value=object())
    @patch("deepseek_http.signal.signal")
    @patch("deepseek_http.signal.setitimer")
    def test_worker_threads_use_cooperative_deadline_without_signal_mutation(self, timer, handler, current):
        with _main_thread_deadline(300):
            pass
        handler.assert_not_called()
        timer.assert_not_called()

    def test_preserves_legacy_reasoner_thinking_mode(self) -> None:
        payload = prepare_deepseek_payload({"model": "deepseek-reasoner", "messages": []})

        self.assertEqual(payload["model"], DEFAULT_DEEPSEEK_MODEL)
        self.assertEqual(payload["thinking"], {"type": "enabled"})

    def test_legacy_pro_and_flash_overrides_use_canonical_flash_with_thinking_support(self) -> None:
        for alias in ("deepseek-v4-pro", "deepseek-pro", "deepseek-v4-flash", "deepseek-v4.1-flash", "deepseek-flash"):
            with self.subTest(alias=alias):
                payload = prepare_deepseek_payload({"model": alias, "messages": []})
                self.assertEqual(payload["model"], "deepseek-flash")
                self.assertEqual(payload["thinking"], {"type": "disabled"})
        explicit = prepare_deepseek_payload({"model": "deepseek-v4-pro", "thinking": {"type": "enabled"}})
        self.assertEqual(explicit["thinking"], {"type": "enabled"})

    @patch("deepseek_http.requests.post")
    def test_dated_pro_overrides_are_normalized_at_request_boundary(self, post: Mock) -> None:
        post.return_value = http_response(status_code=200, headers={})
        for model, expected in (
            ("deepseek-v4-pro-0813", "deepseek-flash"),
            ("deepseek-v4.1-pro-20260919", "deepseek-flash"),
            ("other-provider-pro-0813", "other-provider-pro-0813"),
        ):
            with self.subTest(model=model):
                self.request(payload={"model": model})
                self.assertEqual(post.call_args.kwargs["json"]["model"], expected)

    @patch("deepseek_http.requests.post")
    def test_rejected_flash_never_escalates_to_pro_from_provider_or_environment(self, post: Mock) -> None:
        rejected = http_response(status_code=400, headers={}, text="Unsupported model. Supported model: deepseek-v4-pro-0813")
        post.return_value = rejected
        with patch.dict("os.environ", {"DEEPSEEK_MODEL_FALLBACK": "deepseek-v4.1-pro-20260919"}):
            response = self.request(payload={"model": "deepseek-flash"})
        self.assertIs(response, rejected)
        post.assert_called_once()
        self.assertEqual(post.call_args.kwargs["json"]["model"], "deepseek-flash")

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_retries_connection_reset_then_returns_success(self, post: Mock, sleep: Mock) -> None:
        success = http_response(status_code=200, headers={})
        post.side_effect = [requests.exceptions.ConnectionError("connection reset"), success]

        response = self.request()

        self.assertIs(response, success)
        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(2)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_retries_retryable_status_and_honors_retry_after(self, post: Mock, sleep: Mock) -> None:
        busy = http_response(status_code=429, headers={"Retry-After": "7"})
        success = http_response(status_code=200, headers={})
        post.side_effect = [busy, success]

        response = self.request()

        self.assertIs(response, success)
        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(7)

    @patch("deepseek_http.random.uniform", return_value=1.25)
    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_retry_after_adds_bounded_jitter(
        self,
        post: Mock,
        sleep: Mock,
        uniform: Mock,
    ) -> None:
        busy = http_response(status_code=429, headers={"Retry-After": "7"})
        success = http_response(status_code=200, headers={})
        post.side_effect = [busy, success]

        response = self.request(retry_jitter_ratio=0.25)

        self.assertIs(response, success)
        uniform.assert_called_once_with(0.0, 1.75)
        sleep.assert_called_once_with(8.25)

    @patch("deepseek_http.random.uniform")
    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_retry_after_remains_bounded_by_maximum_delay(
        self,
        post: Mock,
        sleep: Mock,
        uniform: Mock,
    ) -> None:
        busy = http_response(status_code=503, headers={"Retry-After": "120"})
        success = http_response(status_code=200, headers={})
        post.side_effect = [busy, success]

        response = self.request(retry_jitter_ratio=0.25)

        self.assertIs(response, success)
        uniform.assert_not_called()
        sleep.assert_called_once_with(20)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_does_not_retry_permanent_http_error(self, post: Mock, sleep: Mock) -> None:
        unauthorized = http_response(status_code=401, headers={})
        post.return_value = unauthorized

        response = self.request()

        self.assertIs(response, unauthorized)
        post.assert_called_once()
        sleep.assert_not_called()

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_raises_after_attempt_limit(self, post: Mock, sleep: Mock) -> None:
        post.side_effect = requests.exceptions.Timeout("timed out")

        with self.assertRaises(requests.exceptions.Timeout):
            self.request(max_attempts=3)

        self.assertEqual(post.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [2, 4])

    @patch.dict(
        os.environ,
        {
            "DEEPSEEK_API_KEY": "primary",
            "DEEPSEEK_API_KEY_BACKUP": "backup",
            "DEEPSEEK_API_KEY_2": "backup",
        },
        clear=True,
    )
    def test_reads_primary_and_distinct_backup_keys(self) -> None:
        self.assertEqual(
            deepseek_api_keys_from_env(),
            [
                ("DEEPSEEK_API_KEY", "primary"),
                ("DEEPSEEK_API_KEY_BACKUP", "backup"),
            ],
        )

    @patch("deepseek_http.requests.post")
    def test_switches_to_backup_after_primary_balance_error(self, post: Mock) -> None:
        balance_error = http_response(status_code=402, headers={})
        success = http_response(status_code=200, headers={})
        post.side_effect = [balance_error, success]
        logger = Mock()

        response = request_with_key_fallback(
            "https://api.deepseek.com/chat/completions",
            headers={"Content-Type": "application/json"},
            payload={"model": "deepseek-chat"},
            label="test article",
            api_keys=[("primary", "secret-primary"), ("backup", "secret-backup")],
            max_attempts=1,
            logger=logger,
        )

        self.assertIs(response, success)
        self.assertEqual(post.call_count, 2)
        self.assertEqual(
            [call.kwargs["headers"]["Authorization"] for call in post.call_args_list],
            ["Bearer secret-primary", "Bearer secret-backup"],
        )
        log_text = " ".join(str(call) for call in logger.call_args_list)
        self.assertNotIn("secret-primary", log_text)
        self.assertNotIn("secret-backup", log_text)

    @patch("deepseek_http.requests.post")
    def test_does_not_switch_keys_for_bad_request(self, post: Mock) -> None:
        bad_request = http_response(status_code=400, headers={}, text='{"error":"bad input"}')
        post.return_value = bad_request

        response = request_with_key_fallback(
            "https://api.deepseek.com/chat/completions",
            headers={"Content-Type": "application/json"},
            payload={"model": "deepseek-chat"},
            label="test article",
            api_keys=[("primary", "secret-primary"), ("backup", "secret-backup")],
            max_attempts=1,
            logger=Mock(),
        )

        self.assertIs(response, bad_request)
        post.assert_called_once()

    @patch("deepseek_http.requests.post")
    def test_retries_with_supported_model_after_model_rejection(self, post: Mock) -> None:
        retired = http_response(
            status_code=400,
            headers={},
            text=(
                '{"error":{"message":"The supported API model names are '
                'deepseek-v4-pro or deepseek-v4-flash, but you passed retired-model."}}'
            ),
        )
        success = http_response(status_code=200, headers={})
        post.side_effect = [retired, success]
        logger = Mock()

        response = request_with_key_fallback(
            "https://api.deepseek.com/chat/completions",
            headers={"Content-Type": "application/json"},
            payload={"model": "retired-model"},
            label="test article",
            api_keys=[("primary", "secret-primary")],
            max_attempts=1,
            logger=logger,
        )

        self.assertIs(response, success)
        self.assertEqual(post.call_count, 2)
        self.assertEqual(
            [call.kwargs["json"]["model"] for call in post.call_args_list],
            ["retired-model", DEFAULT_DEEPSEEK_MODEL],
        )

    @patch("deepseek_http.requests.post")
    def test_can_disable_model_fallback_for_model_scoped_translation_caches(self, post: Mock) -> None:
        rejected = http_response(
            status_code=400,
            headers={},
            text=(
                '{"error":{"message":"The supported API model is '
                'deepseek-v4-flash, but you passed retired-model."}}'
            ),
        )
        post.return_value = rejected

        response = self.request(
            payload={"model": "retired-model"},
            allow_model_fallback=False,
        )

        self.assertIs(response, rejected)
        post.assert_called_once()
        self.assertEqual(post.call_args.kwargs["json"]["model"], "retired-model")


if __name__ == "__main__":
    unittest.main()
