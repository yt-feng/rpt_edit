#!/usr/bin/env python3
from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

import requests

from deepseek_http import request_with_retry


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


if __name__ == "__main__":
    unittest.main()
