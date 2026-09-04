#!/usr/bin/env python3
from __future__ import annotations

import os
import unittest
from unittest.mock import Mock, patch

import requests

from deepseek_http import (
    DEFAULT_DEEPSEEK_MODEL,
    deepseek_api_keys_from_env,
    prepare_deepseek_payload,
    request_with_key_fallback,
    request_with_retry,
)


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

    def test_maps_retired_chat_alias_to_v4_flash(self) -> None:
        payload = prepare_deepseek_payload({"model": "deepseek-chat", "messages": []})

        self.assertEqual(payload["model"], DEFAULT_DEEPSEEK_MODEL)
        self.assertEqual(payload["thinking"], {"type": "disabled"})

    def test_preserves_legacy_reasoner_thinking_mode(self) -> None:
        payload = prepare_deepseek_payload({"model": "deepseek-reasoner", "messages": []})

        self.assertEqual(payload["model"], DEFAULT_DEEPSEEK_MODEL)
        self.assertEqual(payload["thinking"], {"type": "enabled"})

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_retries_connection_reset_then_returns_success(self, post: Mock, sleep: Mock) -> None:
        success = Mock(status_code=200, headers={})
        post.side_effect = [requests.exceptions.ConnectionError("connection reset"), success]

        response = self.request()

        self.assertIs(response, success)
        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(2)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_retries_retryable_status_and_honors_retry_after(self, post: Mock, sleep: Mock) -> None:
        busy = Mock(status_code=429, headers={"Retry-After": "7"})
        success = Mock(status_code=200, headers={})
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
        busy = Mock(status_code=429, headers={"Retry-After": "7"})
        success = Mock(status_code=200, headers={})
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
        busy = Mock(status_code=503, headers={"Retry-After": "120"})
        success = Mock(status_code=200, headers={})
        post.side_effect = [busy, success]

        response = self.request(retry_jitter_ratio=0.25)

        self.assertIs(response, success)
        uniform.assert_not_called()
        sleep.assert_called_once_with(20)

    @patch("deepseek_http.time.sleep")
    @patch("deepseek_http.requests.post")
    def test_does_not_retry_permanent_http_error(self, post: Mock, sleep: Mock) -> None:
        unauthorized = Mock(status_code=401, headers={})
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
        balance_error = Mock(status_code=402, headers={})
        success = Mock(status_code=200, headers={})
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
        bad_request = Mock(status_code=400, headers={}, text='{"error":"bad input"}')
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
        retired = Mock(
            status_code=400,
            headers={},
            text=(
                '{"error":{"message":"The supported API model names are '
                'deepseek-v4-pro or deepseek-v4-flash, but you passed retired-model."}}'
            ),
        )
        success = Mock(status_code=200, headers={}, text="{}")
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
        rejected = Mock(
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
