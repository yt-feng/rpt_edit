#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import json
import os
import tempfile
import unittest
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import check_social_reach as monitor


NOW = datetime(2026, 8, 31, 12, 0, tzinfo=timezone.utc)


class FakeResponse:
    def __init__(self, status: int, payload) -> None:
        self.status = status
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def getcode(self) -> int:
        return self.status

    def read(self, _limit: int = -1) -> bytes:
        if isinstance(self.payload, bytes):
            return self.payload
        return json.dumps(self.payload).encode("utf-8")


def receipt_payload(
    platform: str,
    provider_id: str,
    *,
    hours_old: float = 25,
    **extra,
) -> dict:
    payload = {
        "schema_version": 1,
        "platform": platform,
        "published_at": (NOW - timedelta(hours=hours_old)).isoformat(),
    }
    payload["video_id" if platform == "youtube" else "post_id"] = provider_id
    payload.update(extra)
    return payload


def write_receipt(root: Path, name: str, payload) -> None:
    (root / name).write_text(json.dumps(payload), encoding="utf-8")


def unified_receipt(*, state: str = "partial") -> dict:
    completed_at = (NOW - timedelta(hours=25)).isoformat()
    return {
        "schema_version": 1,
        "content_id": "private-content-id",
        "state": state,
        "completed_at": completed_at,
        "results": {
            "youtube": {
                "state": "published",
                "video_id": "private-video-id",
                "url": "https://youtube.test/private-video-id",
            },
            "linkedin": {
                "state": "published",
                "post_id": "urn:li:share:private-linkedin-post",
                "url": "https://linkedin.test/private-linkedin-post",
            },
            "x": {
                "state": "failed",
                "post_id": "must-not-be-accepted",
                "url": "https://x.test/must-not-be-accepted",
            },
        },
    }


def complete_env() -> dict[str, str]:
    return {
        "YOUTUBE_API_KEY": "youtube-api-secret",
        "X_API_KEY": "x-consumer-real-id",
        "X_API_SECRET": "x-consumer-secret",
        "X_ACCESS_TOKEN": "x-access-real-account-id",
        "X_ACCESS_TOKEN_SECRET": "x-access-secret",
    }


class ReceiptTests(unittest.TestCase):
    def test_unified_receipt_yields_only_published_provider_results(self) -> None:
        receipts = monitor.parse_receipts(unified_receipt())
        self.assertEqual([row.platform for row in receipts], ["youtube", "linkedin"])
        self.assertTrue(all(row.published_at == NOW - timedelta(hours=25) for row in receipts))
        self.assertTrue(all(row.receipt_ref.startswith("receipt-") for row in receipts))
        self.assertTrue(all("private" not in row.receipt_ref for row in receipts))
        self.assertTrue(all(row.provider_id != "must-not-be-accepted" for row in receipts))

    def test_unified_failed_or_reserved_receipt_is_rejected(self) -> None:
        self.assertEqual(monitor.parse_receipts(unified_receipt(state="failed")), ())
        self.assertEqual(monitor.parse_receipts(unified_receipt(state="reserved")), ())

    def test_youtube_scheduled_publish_at_overrides_receipt_completion_time(self) -> None:
        payload = unified_receipt(state="published")
        scheduled = NOW + timedelta(hours=3)
        payload["results"]["youtube"]["publish_at"] = scheduled.isoformat()
        receipts = monitor.parse_receipts(payload)
        youtube = next(row for row in receipts if row.platform == "youtube")
        linkedin = next(row for row in receipts if row.platform == "linkedin")
        self.assertEqual(youtube.published_at, scheduled)
        self.assertEqual(linkedin.published_at, NOW - timedelta(hours=25))

    def test_only_schema_v1_success_receipts_with_required_fields_are_accepted(self) -> None:
        cases = (
            (receipt_payload("youtube", "video-good"), True),
            (receipt_payload("twitter", "tweet-good", status="published"), True),
            (receipt_payload("linkedin", "urn:li:share:good", success=True), True),
            (receipt_payload("x", "state-good", state="published"), True),
            ({**receipt_payload("x", "bad-schema"), "schema_version": 2}, False),
            ({**receipt_payload("x", "float-schema"), "schema_version": 1.0}, False),
            ({**receipt_payload("x", "string-schema"), "schema_version": "1"}, False),
            (receipt_payload("x", "failed", status="failed"), False),
            (receipt_payload("x", "failed-state", state="failed"), False),
            (receipt_payload("x", "failed-bool", success=False), False),
            ({**receipt_payload("x", "missing-time"), "published_at": ""}, False),
            ({**receipt_payload("x", "missing-id"), "post_id": ""}, False),
            (receipt_payload("unknown", "unknown-id"), False),
        )
        for payload, expected in cases:
            with self.subTest(payload=payload):
                self.assertEqual(monitor.parse_receipt(payload) is not None, expected)

    def test_load_is_bounded_deduplicated_and_does_not_expose_filenames(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_receipt(root, "real-account-id.json", receipt_payload("x", "post-one"))
            write_receipt(root, "duplicate.json", receipt_payload("x", "post-one", hours_old=26))
            write_receipt(root, "invalid.json", {"schema_version": 7})
            loaded = monitor.load_receipts(root)
        self.assertEqual(loaded.seen_count, 3)
        self.assertEqual(loaded.invalid_count, 1)
        self.assertEqual(loaded.duplicate_count, 1)
        self.assertEqual(len(loaded.receipts), 1)
        self.assertNotIn("real-account-id", loaded.receipts[0].receipt_ref)
        self.assertNotIn("post-one", loaded.receipts[0].receipt_ref)


class ProviderProbeTests(unittest.TestCase):
    def test_youtube_calls_videos_list_statistics_and_status_via_env_url(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("youtube", "private-video-id"))
        self.assertIsNotNone(receipt)
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(
                200,
                {
                    "items": [
                        {
                            "statistics": {"viewCount": "0", "private": "discard"},
                            "status": {"uploadStatus": "processed", "privacyStatus": "public"},
                            "accountId": "real-account-must-not-leak",
                        }
                    ],
                    "rawPrivate": "provider-body-must-not-leak",
                },
            )

        env = {
            "YOUTUBE_API_KEY": "youtube-secret",
            "YOUTUBE_VIDEOS_URL": "https://mock.youtube.test/custom/videos?mock=1",
        }
        result = monitor.probe_youtube(receipt, env, opener=opener)
        self.assertEqual(result.status, "checked")
        self.assertEqual(result.metric_value, 0)
        self.assertEqual(result.content_status["upload_status"], "processed")
        request, kwargs = calls[0]
        query = urllib.parse.parse_qs(urllib.parse.urlsplit(request.full_url).query)
        self.assertEqual(urllib.parse.urlsplit(request.full_url).netloc, "mock.youtube.test")
        self.assertEqual(query["part"], ["statistics,status"])
        self.assertEqual(query["id"], ["private-video-id"])
        self.assertEqual(query["key"], ["youtube-secret"])
        self.assertEqual(kwargs["timeout"], monitor.DEFAULT_TIMEOUT)

    def test_youtube_can_refresh_existing_oauth_credentials_before_videos_list(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("youtube", "private-video-id"))
        self.assertIsNotNone(receipt)
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            if request.method == "POST":
                return FakeResponse(
                    200,
                    {
                        "access_token": "short-lived-token-must-not-leak",
                        "private": "raw-refresh-body-must-not-leak",
                    },
                )
            return FakeResponse(
                200,
                {"items": [{"statistics": {"viewCount": "3"}, "status": {}}]},
            )

        env = {
            "YOUTUBE_CLIENT_ID": "youtube-client-id",
            "YOUTUBE_CLIENT_SECRET": "youtube-client-secret",
            "YOUTUBE_REFRESH_TOKEN": "youtube-refresh-secret",
            "YOUTUBE_TOKEN_URL": "https://mock.oauth.test/token",
            "YOUTUBE_VIDEOS_LIST_URL": "https://mock.youtube.test/videos",
        }
        result = monitor.probe_youtube(receipt, env, opener=opener)
        self.assertEqual(result.status, "checked")
        self.assertEqual(result.metric_value, 3)
        self.assertEqual(len(calls), 2)
        refresh, refresh_kwargs = calls[0]
        self.assertEqual(refresh.method, "POST")
        form = urllib.parse.parse_qs(refresh.data.decode("ascii"))
        self.assertEqual(form["grant_type"], ["refresh_token"])
        self.assertEqual(form["client_secret"], [env["YOUTUBE_CLIENT_SECRET"]])
        self.assertEqual(form["refresh_token"], [env["YOUTUBE_REFRESH_TOKEN"]])
        self.assertNotIn(env["YOUTUBE_CLIENT_SECRET"], refresh.full_url)
        self.assertEqual(refresh_kwargs["timeout"], monitor.DEFAULT_TIMEOUT)
        videos, videos_kwargs = calls[1]
        self.assertEqual(videos.method, "GET")
        self.assertEqual(
            videos.get_header("Authorization"),
            "Bearer short-lived-token-must-not-leak",
        )
        self.assertEqual(videos_kwargs["timeout"], monitor.DEFAULT_TIMEOUT)
        rendered = json.dumps(monitor.asdict(result))
        self.assertNotIn("short-lived-token-must-not-leak", rendered)
        self.assertNotIn("raw-refresh-body-must-not-leak", rendered)

    def test_youtube_private_or_unprocessed_zero_is_not_a_reach_zero(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("youtube", "private-video-id"))
        self.assertIsNotNone(receipt)
        cases = (
            (
                {"uploadStatus": "processed", "privacyStatus": "private"},
                "unsupported",
                "youtube_not_public",
            ),
            (
                {"uploadStatus": "uploaded", "privacyStatus": "public"},
                "unavailable",
                "youtube_processing_incomplete",
            ),
            ({}, "unsupported", "youtube_status_unavailable"),
        )
        for status_payload, expected_status, expected_reason in cases:
            with self.subTest(status_payload=status_payload):
                def opener(_request, **_kwargs):
                    return FakeResponse(
                        200,
                        {
                            "items": [
                                {
                                    "statistics": {"viewCount": 0},
                                    "status": status_payload,
                                }
                            ]
                        },
                    )

                result = monitor.probe_youtube(
                    receipt,
                    {"YOUTUBE_API_KEY": "secret"},
                    opener=opener,
                )
                self.assertEqual(result.status, expected_status)
                self.assertEqual(result.reason, expected_reason)
                self.assertEqual(result.metric_value, 0)

    def test_youtube_partial_oauth_config_does_not_call_network(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("youtube", "private-video-id"))
        self.assertIsNotNone(receipt)
        calls = []

        def opener(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("network should not be called")

        result = monitor.probe_youtube(
            receipt,
            {"YOUTUBE_CLIENT_ID": "only-client-id"},
            opener=opener,
        )
        self.assertEqual(result.status, "unavailable")
        self.assertEqual(result.reason, "missing_configuration")
        self.assertEqual(calls, [])

    def test_youtube_refresh_token_is_reused_only_inside_one_monitor_run(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_receipt(root, "one.json", receipt_payload("youtube", "video-one"))
            write_receipt(root, "two.json", receipt_payload("youtube", "video-two", hours_old=26))
            methods = []

            def opener(request, **_kwargs):
                methods.append(request.method)
                if request.method == "POST":
                    return FakeResponse(200, {"access_token": "ephemeral-access-token"})
                return FakeResponse(
                    200,
                    {"items": [{"statistics": {"viewCount": 4}, "status": {}}]},
                )

            report = monitor.run_monitor(
                root,
                {
                    "YOUTUBE_CLIENT_ID": "client-id",
                    "YOUTUBE_CLIENT_SECRET": "client-secret",
                    "YOUTUBE_REFRESH_TOKEN": "refresh-token",
                },
                checkpoint_hours=24,
                now=NOW,
                opener=opener,
            )
        self.assertEqual(report.due_count, 2)
        self.assertEqual(methods.count("POST"), 1)
        self.assertEqual(methods.count("GET"), 2)

    def test_x_get_uses_oauth1_and_reads_allowlisted_public_metrics(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("x", "private-tweet-id"))
        self.assertIsNotNone(receipt)
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(
                200,
                {
                    "data": {
                        "id": "private-tweet-id",
                        "author_id": "real-account-must-not-leak",
                        "text": "raw body must not leak",
                        "public_metrics": {
                            "impression_count": 0,
                            "like_count": 2,
                            "reply_count": 1,
                            "retweet_count": 3,
                        },
                    }
                },
            )

        env = complete_env()
        env["X_TWEET_LOOKUP_URL_TEMPLATE"] = "https://mock.x.test/custom/{post_id}"
        result = monitor.probe_x(
            receipt,
            env,
            opener=opener,
            nonce="fixed-nonce",
            timestamp=1_789_000_000,
        )
        self.assertEqual(result.status, "checked")
        self.assertEqual(result.metric_value, 0)
        self.assertEqual(result.metrics, {
            "impressions": 0,
            "likes": 2,
            "replies": 1,
            "reposts": 3,
        })
        request, kwargs = calls[0]
        self.assertEqual(request.method, "GET")
        self.assertEqual(urllib.parse.urlsplit(request.full_url).netloc, "mock.x.test")
        self.assertEqual(
            urllib.parse.parse_qs(urllib.parse.urlsplit(request.full_url).query)["tweet.fields"],
            ["public_metrics"],
        )
        authorization = request.get_header("Authorization")
        self.assertTrue(authorization.startswith("OAuth "))
        self.assertIn('oauth_signature_method="HMAC-SHA1"', authorization)
        self.assertIn('oauth_nonce="fixed-nonce"', authorization)
        self.assertNotIn(env["X_API_SECRET"], authorization)
        self.assertNotIn(env["X_ACCESS_TOKEN_SECRET"], authorization)
        self.assertEqual(kwargs["timeout"], monitor.DEFAULT_TIMEOUT)

    def test_x_missing_impressions_is_unsupported_not_zero(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("x", "tweet-no-impressions"))
        self.assertIsNotNone(receipt)

        def opener(_request, **_kwargs):
            return FakeResponse(200, {"data": {"public_metrics": {"like_count": 8}}})

        result = monitor.probe_x(receipt, complete_env(), opener=opener)
        self.assertEqual(result.status, "unsupported")
        self.assertIsNone(result.metric_value)
        self.assertEqual(result.metrics, {"likes": 8})

    def test_x_zero_public_metric_is_not_zero_if_another_available_metric_is_positive(self) -> None:
        receipt = monitor.parse_receipt(receipt_payload("x", "tweet-mixed-metrics"))
        self.assertIsNotNone(receipt)

        def opener(_request, **_kwargs):
            return FakeResponse(
                200,
                {
                    "data": {
                        "public_metrics": {"impression_count": 0},
                        "organic_metrics": {"impression_count": 9},
                    }
                },
            )

        result = monitor.probe_x(receipt, complete_env(), opener=opener)
        self.assertEqual(result.status, "checked")
        self.assertEqual(result.metric_value, 9)
        self.assertEqual(result.metrics["impressions"], 9)

    def test_linkedin_without_explicit_analytics_config_is_unsupported_without_network(self) -> None:
        receipt = monitor.parse_receipt(
            receipt_payload("linkedin", "urn:li:share:private-post")
        )
        self.assertIsNotNone(receipt)
        calls = []

        def opener(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("LinkedIn must not be queried")

        result = monitor.probe_linkedin(
            receipt,
            {"LINKEDIN_ACCESS_TOKEN": "token-without-analytics-config"},
            opener=opener,
        )
        self.assertEqual(result.status, "unsupported")
        self.assertEqual(result.reason, "linkedin_analytics_not_configured")
        self.assertEqual(calls, [])

    def test_linkedin_configured_endpoint_permission_and_metric_path_are_mockable(self) -> None:
        receipt = monitor.parse_receipt(
            receipt_payload("linkedin", "urn:li:share:private-post")
        )
        self.assertIsNotNone(receipt)
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(
                200,
                {
                    "elements": [{"custom": {"count": "0"}}],
                    "account": "real-account-must-not-leak",
                },
            )

        env = {
            "LINKEDIN_ACCESS_TOKEN": "linkedin-secret-token",
            "LINKEDIN_ANALYTICS_PERMISSION": "r_member_postAnalytics",
            "LINKEDIN_ANALYTICS_URL_TEMPLATE": "https://mock.linkedin.test/stats/{post_id}",
            "LINKEDIN_ANALYTICS_METRIC_PATH": "elements.0.custom.count",
        }
        result = monitor.probe_linkedin(receipt, env, opener=opener)
        self.assertEqual(result.status, "checked")
        self.assertEqual(result.metric_value, 0)
        request, kwargs = calls[0]
        self.assertEqual(urllib.parse.urlsplit(request.full_url).netloc, "mock.linkedin.test")
        self.assertNotIn("urn:li:share:", request.full_url)
        self.assertEqual(
            request.get_header("Authorization"),
            "Bearer linkedin-secret-token",
        )
        self.assertEqual(request.get_header("Linkedin-version"), "202608")
        self.assertEqual(kwargs["timeout"], monitor.DEFAULT_TIMEOUT)

    def test_linkedin_default_parser_never_treats_only_first_bucket_as_total(self) -> None:
        receipt = monitor.parse_receipt(
            receipt_payload("linkedin", "urn:li:share:private-post")
        )
        self.assertIsNotNone(receipt)

        def opener(_request, **_kwargs):
            return FakeResponse(
                200,
                {"elements": [{"impressionCount": 0}, {"impressionCount": 7}]},
            )

        result = monitor.probe_linkedin(
            receipt,
            {
                "LINKEDIN_ACCESS_TOKEN": "linkedin-secret-token",
                "LINKEDIN_ANALYTICS_PERMISSION_GRANTED": "true",
                "LINKEDIN_ANALYTICS_URL": "https://mock.linkedin.test/stats",
            },
            opener=opener,
        )
        self.assertEqual(result.status, "checked")
        self.assertEqual(result.metric_value, 7)


class MonitorTests(unittest.TestCase):
    def test_checkpoint_windows_are_half_open_and_do_not_scan_history(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ages = (0.99, 1, 23.99, 24, 47.99, 48)
            for index, age in enumerate(ages):
                write_receipt(
                    root,
                    f"receipt-{index}.json",
                    receipt_payload("youtube", f"video-{index}", hours_old=age),
                )

            def opener(_request, **_kwargs):
                return FakeResponse(
                    200,
                    {"items": [{"statistics": {"viewCount": 5}, "status": {}}]},
                )

            one_hour = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=1,
                now=NOW,
                opener=opener,
            )
            twenty_four_hour = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=24,
                now=NOW,
                opener=opener,
            )
        self.assertEqual(one_hour.checkpoint_window_end_hours, 24)
        self.assertEqual(one_hour.window_match_count, 2)
        self.assertEqual(one_hour.due_count, 2)
        self.assertEqual(
            {row.age_hours for row in one_hour.results},
            {1.0, 23.99},
        )
        self.assertEqual(twenty_four_hour.checkpoint_window_end_hours, 48)
        self.assertEqual(twenty_four_hour.window_match_count, 2)
        self.assertEqual(twenty_four_hour.due_count, 2)
        self.assertEqual(
            {row.age_hours for row in twenty_four_hour.results},
            {24.0, 47.99},
        )

    def test_max_receipts_bounds_network_calls_and_prioritizes_window_expiry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for age in (25, 30, 35):
                write_receipt(
                    root,
                    f"receipt-{age}.json",
                    receipt_payload("youtube", f"video-{age}", hours_old=age),
                )
            requested_ids = []

            def opener(request, **_kwargs):
                requested_ids.append(
                    urllib.parse.parse_qs(
                        urllib.parse.urlsplit(request.full_url).query
                    )["id"][0]
                )
                return FakeResponse(
                    200,
                    {"items": [{"statistics": {"viewCount": 5}, "status": {}}]},
                )

            report = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=24,
                now=NOW,
                max_receipts=2,
                opener=opener,
            )
        self.assertEqual(report.window_match_count, 3)
        self.assertEqual(report.due_count, 2)
        self.assertEqual(report.truncated_count, 1)
        self.assertEqual(set(requested_ids), {"video-30", "video-35"})

    def test_one_hour_zero_is_report_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_receipt(root, "youtube.json", receipt_payload("youtube", "video-one", hours_old=2))

            def opener(_request, **_kwargs):
                return FakeResponse(
                    200,
                    {
                        "items": [
                            {
                                "statistics": {"viewCount": "0"},
                                "status": {"uploadStatus": "processed", "privacyStatus": "public"},
                            }
                        ]
                    },
                )

            report = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=1,
                now=NOW,
                opener=opener,
            )
        self.assertEqual(report.results[0].metric_value, 0)
        self.assertFalse(report.results[0].should_alert)
        self.assertEqual(report.zero_reach_count, 1)
        self.assertFalse(report.should_alert)
        self.assertFalse(report.pause_signal)

    def test_24h_explicit_zero_alerts_but_unavailable_and_not_due_do_not(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_receipt(root, "youtube.json", receipt_payload("youtube", "video-zero", hours_old=25))
            write_receipt(root, "linkedin.json", receipt_payload("linkedin", "post-unsupported", hours_old=25))
            write_receipt(root, "future.json", receipt_payload("x", "not-due", hours_old=23))

            def opener(_request, **_kwargs):
                return FakeResponse(
                    200,
                    {
                        "items": [
                            {
                                "statistics": {"viewCount": "0"},
                                "status": {"uploadStatus": "processed", "privacyStatus": "public"},
                            }
                        ]
                    },
                )

            report = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=24,
                now=NOW,
                opener=opener,
            )
        self.assertEqual(report.receipts_accepted, 3)
        self.assertEqual(report.due_count, 2)
        self.assertEqual(report.zero_reach_count, 1)
        self.assertEqual(report.unsupported_count, 1)
        self.assertTrue(report.should_alert)
        linkedin = next(row for row in report.results if row.platform == "linkedin")
        self.assertEqual(linkedin.status, "unsupported")
        self.assertFalse(linkedin.should_alert)

    def test_consecutive_recent_24h_zeros_emit_pause_signal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_receipt(root, "newer.json", receipt_payload("youtube", "video-newer", hours_old=25))
            write_receipt(root, "older.json", receipt_payload("youtube", "video-older", hours_old=45))

            def opener(_request, **_kwargs):
                return FakeResponse(
                    200,
                    {
                        "items": [
                            {
                                "statistics": {"viewCount": 0},
                                "status": {"uploadStatus": "processed", "privacyStatus": "public"},
                            }
                        ]
                    },
                )

            report = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=24,
                now=NOW,
                pause_after_consecutive=2,
                opener=opener,
            )
        self.assertEqual(report.consecutive_zero_by_platform["youtube"], 2)
        self.assertEqual(report.max_consecutive_zero, 2)
        self.assertTrue(report.pause_signal)

    def test_recent_positive_breaks_consecutive_pause_signal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_receipt(root, "newer.json", receipt_payload("youtube", "video-newer", hours_old=25))
            write_receipt(root, "older.json", receipt_payload("youtube", "video-older", hours_old=45))

            def opener(request, **_kwargs):
                video_id = urllib.parse.parse_qs(urllib.parse.urlsplit(request.full_url).query)["id"][0]
                count = 7 if video_id == "video-newer" else 0
                return FakeResponse(
                    200,
                    {
                        "items": [
                            {
                                "statistics": {"viewCount": count},
                                "status": {"uploadStatus": "processed", "privacyStatus": "public"},
                            }
                        ]
                    },
                )

            report = monitor.run_monitor(
                root,
                {"YOUTUBE_API_KEY": "secret"},
                checkpoint_hours=24,
                now=NOW,
                opener=opener,
            )
        self.assertEqual(report.zero_reach_count, 1)
        self.assertEqual(report.consecutive_zero_by_platform["youtube"], 0)
        self.assertTrue(report.should_alert)
        self.assertFalse(report.pause_signal)

    def test_json_email_github_output_and_stdout_are_sanitized(self) -> None:
        secret_values = complete_env() | {
            "YOUTUBE_API_KEY": "youtube-secret-must-not-leak",
            "GITHUB_SERVER_URL": "https://github.com",
            "GITHUB_REPOSITORY": "owner/repository",
            "GITHUB_RUN_ID": "12345",
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            receipts = root / "receipts"
            receipts.mkdir()
            write_receipt(
                receipts,
                "real-account-id-in-filename.json",
                {
                    **unified_receipt(state="published"),
                    "content_id": "private-content-id-must-not-leak",
                    "results": {
                        **unified_receipt(state="published")["results"],
                        "x": {
                            "state": "published",
                            "post_id": "999999999999999999",
                            "url": "https://x.test/real-account/999999999999999999",
                        },
                    },
                },
            )
            json_path = root / "reach.json"
            email_path = root / "reach-email.txt"
            github_output = root / "github-output.txt"

            def opener(request, **_kwargs):
                if urllib.parse.urlsplit(request.full_url).netloc == "api.x.com":
                    return FakeResponse(
                        200,
                        {
                            "data": {
                                "id": "999999999999999999",
                                "author_id": "real-x-account-id-in-body",
                                "text": "raw x body must not leak",
                                "public_metrics": {"impression_count": 0},
                            }
                        },
                    )
                return FakeResponse(
                    200,
                    {
                        "items": [
                            {
                                "id": "private-video-id",
                                "account_id": "real-account-id-in-body",
                                "statistics": {"viewCount": 0},
                                "status": {"uploadStatus": "processed", "privacyStatus": "public"},
                            }
                        ],
                        "private": "raw-provider-body-must-not-leak",
                    },
                )

            argv = [
                "--receipts-dir",
                str(receipts),
                "--age-hours",
                "24",
                "--now",
                NOW.isoformat(),
                "--json-output",
                str(json_path),
                "--email-output",
                str(email_path),
                "--github-output",
                str(github_output),
            ]
            stdout = io.StringIO()
            with (
                mock.patch.dict(os.environ, secret_values, clear=True),
                mock.patch.object(monitor, "request_json", wraps=monitor.request_json),
                mock.patch.object(monitor.urllib.request, "urlopen", opener),
                contextlib.redirect_stdout(stdout),
            ):
                self.assertEqual(monitor.main(argv), 0)
            combined = "\n".join(
                (
                    stdout.getvalue(),
                    json_path.read_text(encoding="utf-8"),
                    email_path.read_text(encoding="utf-8"),
                    github_output.read_text(encoding="utf-8"),
                )
            )
            payload = json.loads(json_path.read_text(encoding="utf-8"))

        forbidden = (
            "youtube-secret-must-not-leak",
            complete_env()["X_API_KEY"],
            complete_env()["X_API_SECRET"],
            complete_env()["X_ACCESS_TOKEN"],
            complete_env()["X_ACCESS_TOKEN_SECRET"],
            "private-content-id-must-not-leak",
            "private-video-id",
            "private-linkedin-post",
            "999999999999999999",
            "real-account-id-in-filename",
            "real-account-id-in-body",
            "real-x-account-id-in-body",
            "raw-provider-body-must-not-leak",
        )
        for value in forbidden:
            with self.subTest(value=value):
                self.assertNotIn(value, combined)
        self.assertIn("should_alert=true", combined)
        self.assertIn("pause_signal=false", combined)
        self.assertNotIn("raw", json.dumps(payload).casefold())

    def test_github_output_has_stable_pause_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = monitor.run_monitor(
                root / "missing-receipts",
                {},
                checkpoint_hours=24,
                now=NOW,
            )
            output = root / "github-output.txt"
            email = root / "email.txt"
            payload = root / "report.json"
            monitor.write_github_output(output, report, email, payload)
            values = dict(
                line.split("=", 1)
                for line in output.read_text(encoding="utf-8").splitlines()
            )
        self.assertEqual(
            set(values),
            {
                "should_alert",
                "pause_signal",
                "pause_platforms",
                "max_consecutive_zero",
                "zero_reach_count",
                "due_count",
                "truncated_count",
                "unsupported_count",
                "unavailable_count",
                "subject",
                "alert_key",
                "email_file",
                "json_file",
            },
        )
        self.assertEqual(values["should_alert"], "false")
        self.assertEqual(values["pause_signal"], "false")


if __name__ == "__main__":
    unittest.main(verbosity=2)
