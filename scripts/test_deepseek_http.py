#!/usr/bin/env python3
from __future__ import annotations

import os
import unittest
from unittest.mock import Mock, patch

import requests

from deepseek_http import (
    deepseek_api_keys_from_env,
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
            "logger": Mock(),
        }
        options.update(overrides)
        return request_with_retry("https://api.deepseek.com/chat/completions", **options)

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
        bad_request = Mock(status_code=400, headers={})
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


if __name__ == "__main__":
    unittest.main()
