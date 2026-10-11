#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import check_social_credentials as monitor


NOW = datetime(2026, 8, 31, 0, 0, tzinfo=timezone.utc)


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


def complete_env() -> dict[str, str]:
    return {
        "BUFFER_API_KEY": "buffer-secret-value",
        "BUFFER_ACCOUNT_ID": "account-real-id",
        "BUFFER_LINKEDIN_CHANNEL_ID": "linkedin-real-id",
        "BUFFER_X_CHANNEL_ID": "x-real-id",
        "BUFFER_YOUTUBE_CHANNEL_ID": "buffer-youtube-real-id",
        "LINKEDIN_CLIENT_ID": "linkedin-client-real-id",
        "LINKEDIN_CLIENT_SECRET": "linkedin-client-secret-value",
        "LINKEDIN_ACCESS_TOKEN": "linkedin-access-secret-value",
        "LINKEDIN_REQUIRED_SCOPES": "w_member_social",
        "X_API_KEY": "x-api-key-value",
        "X_API_SECRET": "x-api-secret-value",
        "X_ACCESS_TOKEN": "x-access-token-value",
        "X_ACCESS_TOKEN_SECRET": "x-access-token-secret-value",
        "X_USER_ID": "x-user-real-id",
        "X_OAUTH1_SCOPES": "read write",
        "YOUTUBE_CLIENT_ID": "youtube-client-real-id",
        "YOUTUBE_CLIENT_SECRET": "youtube-client-secret-value",
        "YOUTUBE_REFRESH_TOKEN": "youtube-refresh-secret-value",
        "YOUTUBE_CHANNEL_ID": "youtube-direct-real-id",
    }


def healthy_buffer_probe(_env, **_kwargs) -> dict[str, monitor.ProbeResult]:
    return {
        "BUFFER_ACCOUNT": monitor.ProbeResult("healthy", "authenticated", 200),
        "BUFFER_LINKEDIN": monitor.ProbeResult("healthy", "authenticated", 200),
        "BUFFER_X": monitor.ProbeResult("healthy", "authenticated", 200),
        "BUFFER_YOUTUBE": monitor.ProbeResult("healthy", "authenticated", 200),
    }


def healthy_youtube_probe(_env, **_kwargs) -> monitor.ProbeResult:
    return monitor.ProbeResult("healthy", "authenticated", 200)


def healthy_linkedin_probe(_env, **_kwargs) -> monitor.ProbeResult:
    return monitor.ProbeResult("healthy", "authenticated", 200)


def healthy_x_probe(_env, **_kwargs) -> monitor.ProbeResult:
    return monitor.ProbeResult("healthy", "authenticated", 200)


def buffer_router(env: dict[str, str], *, overrides: dict[str, dict] | None = None):
    overrides = overrides or {}
    calls = []
    channel_payloads = {
        env["BUFFER_LINKEDIN_CHANNEL_ID"]: {
            "id": env["BUFFER_LINKEDIN_CHANNEL_ID"],
            "service": "linkedin",
            "isDisconnected": False,
            "isLocked": False,
            "isQueuePaused": False,
        },
        env["BUFFER_X_CHANNEL_ID"]: {
            "id": env["BUFFER_X_CHANNEL_ID"],
            "service": "twitter",
            "isDisconnected": False,
            "isLocked": False,
            "isQueuePaused": False,
        },
        env["BUFFER_YOUTUBE_CHANNEL_ID"]: {
            "id": env["BUFFER_YOUTUBE_CHANNEL_ID"],
            "service": "youtube",
            "isDisconnected": False,
            "isLocked": False,
            "isQueuePaused": False,
        },
    }
    channel_payloads.update(overrides)

    def opener(request, **kwargs):
        calls.append((request, kwargs))
        body = json.loads(request.data.decode("utf-8"))
        if "SocialCredentialAccount" in body["query"]:
            return FakeResponse(
                200,
                {
                    "data": {"account": {"id": env["BUFFER_ACCOUNT_ID"]}},
                    "privateProviderMarker": "provider-body-must-not-leak",
                },
            )
        channel_id = body["variables"]["channelId"]
        return FakeResponse(
            200,
            {
                "data": {"channel": channel_payloads[channel_id]},
                "privateProviderMarker": "provider-body-must-not-leak",
            },
        )

    return opener, calls


def youtube_router(env: dict[str, str]):
    calls = []

    def opener(request, **kwargs):
        calls.append((request, kwargs))
        if request.full_url == monitor.DEFAULT_YOUTUBE_TOKEN_URL:
            return FakeResponse(
                200,
                {
                    "access_token": "short-lived-youtube-access-token",
                    "scope": "https://www.googleapis.com/auth/youtube.upload",
                    "privateProviderMarker": "provider-body-must-not-leak",
                },
            )
        return FakeResponse(
            200,
            {
                "items": [{"id": env["YOUTUBE_CHANNEL_ID"], "title": "private-title"}],
                "privateProviderMarker": "provider-body-must-not-leak",
            },
        )

    return opener, calls


class ExpiryTests(unittest.TestCase):
    def test_date_only_expiry_is_beijing_end_of_day(self) -> None:
        parsed = monitor.parse_explicit_expiry("2026-08-31")
        self.assertEqual(parsed.isoformat(), "2026-08-31T23:59:59+08:00")

    def test_threshold_boundaries_are_inclusive(self) -> None:
        cases = (
            (NOW, "invalid"),
            (NOW + timedelta(days=3), "expiring_3d"),
            (NOW + timedelta(days=3, seconds=1), "expiring_14d"),
            (NOW + timedelta(days=14), "expiring_14d"),
            (NOW + timedelta(days=14, seconds=1), "healthy"),
        )
        for expiry, expected in cases:
            with self.subTest(expiry=expiry):
                status, parsed, _days, _reason = monitor.evaluate_expiry(
                    expiry.isoformat(),
                    now=NOW,
                )
                self.assertEqual(status, expected)
                self.assertEqual(parsed, expiry)

    def test_absent_expiry_is_optional_and_malformed_expiry_is_invalid(self) -> None:
        self.assertEqual(
            monitor.evaluate_expiry("", now=NOW),
            (None, None, None, None),
        )
        status, expiry, days, reason = monitor.evaluate_expiry("not-a-date", now=NOW)
        self.assertEqual(status, "invalid")
        self.assertIsNone(expiry)
        self.assertIsNone(days)
        self.assertEqual(reason, "expiry_variable_invalid")


class BufferProbeTests(unittest.TestCase):
    def test_account_and_three_channels_use_queries_only_and_return_healthy(self) -> None:
        env = complete_env()
        opener, calls = buffer_router(env)
        results = monitor.probe_buffer_credentials(env, opener=opener)

        self.assertEqual(set(results), {
            "BUFFER_ACCOUNT",
            "BUFFER_LINKEDIN",
            "BUFFER_X",
            "BUFFER_YOUTUBE",
        })
        self.assertTrue(all(result.status == "healthy" for result in results.values()))
        self.assertEqual(len(calls), 4)
        for request, kwargs in calls:
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.full_url, monitor.DEFAULT_BUFFER_API_URL)
            self.assertEqual(
                request.get_header("Authorization"),
                f"Bearer {env['BUFFER_API_KEY']}",
            )
            payload = json.loads(request.data.decode("utf-8"))
            self.assertIn("query", payload)
            self.assertNotIn("mutation", payload["query"].casefold())
            self.assertNotIn(env["BUFFER_API_KEY"], request.full_url)
            self.assertNotIn(env["BUFFER_API_KEY"], request.data.decode("utf-8"))
            self.assertEqual(kwargs["timeout"], 20)

    def test_missing_buffer_configuration_does_not_call_network(self) -> None:
        calls = []

        def opener(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("network should not be called")

        results = monitor.probe_buffer_credentials(
            {"BUFFER_LINKEDIN_CHANNEL_ID": "configured-but-no-account"},
            opener=opener,
        )
        self.assertEqual(calls, [])
        self.assertTrue(all(result.status == "missing" for result in results.values()))

    def test_graphql_auth_and_permission_errors_are_normalized(self) -> None:
        env = complete_env()

        def unauthorized(_request, **_kwargs):
            return FakeResponse(
                200,
                {"errors": [{"message": "secret provider prose", "extensions": {"code": "UNAUTHORIZED"}}]},
            )

        invalid = monitor.probe_buffer_credentials(env, opener=unauthorized)
        self.assertTrue(all(result.status == "invalid" for result in invalid.values()))
        self.assertTrue(all(result.reason == "credential_invalid" for result in invalid.values()))

        def forbidden(_request, **_kwargs):
            return FakeResponse(403, {"private": "body"})

        denied = monitor.probe_buffer_credentials(env, opener=forbidden)
        self.assertTrue(all(result.status == "permission_denied" for result in denied.values()))

    def test_network_error_is_transient_without_exception_text(self) -> None:
        env = complete_env()

        def unavailable(_request, **_kwargs):
            raise urllib.error.URLError("token=must-not-leak")

        results = monitor.probe_buffer_credentials(env, opener=unavailable)
        self.assertTrue(all(result.status == "transient" for result in results.values()))
        self.assertTrue(all(result.reason == "transient_response" for result in results.values()))

    def test_account_mismatch_stops_channel_queries(self) -> None:
        env = complete_env()
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(200, {"data": {"account": {"id": "different-account"}}})

        results = monitor.probe_buffer_credentials(env, opener=opener)
        self.assertEqual(len(calls), 1)
        self.assertTrue(all(result.status == "permission_denied" for result in results.values()))
        self.assertTrue(all(result.reason == "account_mismatch" for result in results.values()))

    def test_channel_flags_and_service_mismatch_are_actionable(self) -> None:
        base = {
            "id": "channel-id",
            "service": "linkedin",
            "isDisconnected": False,
            "isLocked": False,
            "isQueuePaused": False,
        }
        cases = (
            ({"isDisconnected": True}, "invalid", "channel_disconnected"),
            ({"isLocked": True}, "permission_denied", "channel_locked"),
            ({"isQueuePaused": True}, "permission_denied", "queue_paused"),
            ({"service": "twitter"}, "permission_denied", "service_mismatch"),
            ({"isLocked": None}, "transient", "provider_response_invalid"),
            ({"id": "other-id"}, "invalid", "channel_not_available"),
        )
        for update, status, reason in cases:
            with self.subTest(update=update):
                channel = dict(base)
                channel.update(update)
                result = monitor.classify_buffer_channel(
                    channel,
                    expected_id="channel-id",
                    expected_services=frozenset({"linkedin"}),
                )
                self.assertEqual(result.status, status)
                self.assertEqual(result.reason, reason)

    def test_channel_not_found_graphql_error_is_invalid(self) -> None:
        env = complete_env()
        calls = 0

        def opener(request, **_kwargs):
            nonlocal calls
            calls += 1
            payload = json.loads(request.data.decode("utf-8"))
            if "SocialCredentialAccount" in payload["query"]:
                return FakeResponse(200, {"data": {"account": {"id": env["BUFFER_ACCOUNT_ID"]}}})
            return FakeResponse(
                200,
                {"errors": [{"extensions": {"code": "CHANNEL_NOT_FOUND"}}]},
            )

        results = monitor.probe_buffer_credentials(env, opener=opener)
        self.assertEqual(calls, 4)
        self.assertEqual(results["BUFFER_ACCOUNT"].status, "healthy")
        for slot in ("BUFFER_LINKEDIN", "BUFFER_X", "BUFFER_YOUTUBE"):
            self.assertEqual(results[slot].status, "invalid")
            self.assertEqual(results[slot].reason, "channel_not_available")


class LinkedInProbeTests(unittest.TestCase):
    def test_introspection_validates_active_expiry_and_scope_without_identifier_output(self) -> None:
        env = complete_env()
        calls = []
        expiry = NOW + timedelta(days=10)

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(
                200,
                {
                    "active": True,
                    "status": "active",
                    "client_id": env["LINKEDIN_CLIENT_ID"],
                    "expires_at": int(expiry.timestamp()),
                    "scope": "r_liteprofile,w_member_social",
                    "privateProviderMarker": "linkedin-provider-body-must-not-leak",
                },
            )

        result = monitor.probe_direct_linkedin(env, opener=opener)
        self.assertEqual(result.status, "healthy")
        self.assertEqual(result.expires_at, expiry)
        self.assertEqual(len(calls), 1)
        request, kwargs = calls[0]
        self.assertEqual(request.method, "POST")
        self.assertEqual(request.full_url, monitor.DEFAULT_LINKEDIN_INTROSPECTION_URL)
        form = urllib_parse(request.data.decode("utf-8"))
        self.assertEqual(form["client_id"], [env["LINKEDIN_CLIENT_ID"]])
        self.assertEqual(form["client_secret"], [env["LINKEDIN_CLIENT_SECRET"]])
        self.assertEqual(form["token"], [env["LINKEDIN_ACCESS_TOKEN"]])
        self.assertNotIn(env["LINKEDIN_CLIENT_SECRET"], request.full_url)
        self.assertNotIn(env["LINKEDIN_ACCESS_TOKEN"], request.full_url)
        self.assertEqual(kwargs["timeout"], 20)

        check = monitor.combine_probe_and_expiry(
            monitor.SLOT_SPEC_BY_NAME["LINKEDIN_DIRECT"],
            result,
            env,
            now=NOW,
        )
        self.assertEqual(check.status, "expiring_14d")
        self.assertEqual(check.expires_at, expiry.isoformat().replace("+00:00", "Z"))

    def test_inactive_token_invalid_credentials_and_missing_scope_are_normalized(self) -> None:
        env = complete_env()

        def inactive(_request, **_kwargs):
            return FakeResponse(
                200,
                {"active": False, "status": "revoked", "scope": "w_member_social"},
            )

        inactive_result = monitor.probe_direct_linkedin(env, opener=inactive)
        self.assertEqual(inactive_result.status, "invalid")
        self.assertEqual(inactive_result.reason, "linkedin_token_inactive")

        def invalid(_request, **_kwargs):
            return FakeResponse(400, {"error": "private invalid detail"})

        invalid_result = monitor.probe_direct_linkedin(env, opener=invalid)
        self.assertEqual(invalid_result.status, "invalid")
        self.assertEqual(invalid_result.reason, "credential_invalid")

        def missing_scope(_request, **_kwargs):
            return FakeResponse(
                200,
                {
                    "active": True,
                    "status": "active",
                    "client_id": env["LINKEDIN_CLIENT_ID"],
                    "scope": "r_liteprofile",
                },
            )

        scope_result = monitor.probe_direct_linkedin(env, opener=missing_scope)
        self.assertEqual(scope_result.status, "permission_denied")
        self.assertEqual(scope_result.reason, "scope_missing")

    def test_missing_and_transient_linkedin_checks_do_not_leak_exception(self) -> None:
        calls = []

        def unexpected(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("should not call network")

        missing = monitor.probe_direct_linkedin(
            {"LINKEDIN_CLIENT_ID": "only-client"},
            opener=unexpected,
        )
        self.assertEqual(missing.status, "missing")
        self.assertEqual(calls, [])

        def unavailable(_request, **_kwargs):
            raise urllib.error.URLError("linkedin token secret detail")

        transient = monitor.probe_direct_linkedin(complete_env(), opener=unavailable)
        self.assertEqual(transient.status, "transient")
        self.assertEqual(transient.reason, "transient_response")


class XProbeTests(unittest.TestCase):
    def test_oauth1_signs_only_a_read_only_users_me_request(self) -> None:
        env = complete_env()
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(
                200,
                {
                    "data": {"id": env["X_USER_ID"], "username": "private-name"},
                    "privateProviderMarker": "x-provider-body-must-not-leak",
                },
            )

        result = monitor.probe_direct_x(
            env,
            opener=opener,
            nonce_func=lambda: "fixed-nonce",
            timestamp_func=lambda: 1234567890,
        )
        self.assertEqual(result.status, "healthy")
        self.assertEqual(len(calls), 1)
        request, kwargs = calls[0]
        self.assertEqual(request.method, "GET")
        self.assertIsNone(request.data)
        self.assertEqual(request.full_url, monitor.DEFAULT_X_USERS_ME_URL)
        authorization = request.get_header("Authorization")
        self.assertTrue(authorization.startswith("OAuth "))
        self.assertIn('oauth_nonce="fixed-nonce"', authorization)
        self.assertIn('oauth_signature_method="HMAC-SHA1"', authorization)
        self.assertNotIn(env["X_API_SECRET"], authorization)
        self.assertNotIn(env["X_ACCESS_TOKEN_SECRET"], authorization)
        self.assertNotIn(env["X_API_SECRET"], request.full_url)
        self.assertNotIn(env["X_ACCESS_TOKEN_SECRET"], request.full_url)
        self.assertEqual(kwargs["timeout"], 20)

        second_header = monitor.oauth1_authorization_header(
            "GET",
            monitor.DEFAULT_X_USERS_ME_URL,
            consumer_key=env["X_API_KEY"],
            consumer_secret=env["X_API_SECRET"],
            access_token=env["X_ACCESS_TOKEN"],
            access_token_secret=env["X_ACCESS_TOKEN_SECRET"],
            nonce="fixed-nonce",
            timestamp=1234567890,
        )
        self.assertEqual(authorization, second_header)

    def test_x_invalid_permission_identity_and_declared_scope_are_normalized(self) -> None:
        env = complete_env()

        def unauthorized(_request, **_kwargs):
            return FakeResponse(401, {"detail": "private"})

        invalid = monitor.probe_direct_x(env, opener=unauthorized)
        self.assertEqual(invalid.status, "invalid")

        def forbidden(_request, **_kwargs):
            return FakeResponse(403, {"detail": "private"})

        denied = monitor.probe_direct_x(env, opener=forbidden)
        self.assertEqual(denied.status, "permission_denied")

        def wrong_identity(_request, **_kwargs):
            return FakeResponse(200, {"data": {"id": "different-user"}})

        mismatch = monitor.probe_direct_x(env, opener=wrong_identity)
        self.assertEqual(mismatch.status, "permission_denied")
        self.assertEqual(mismatch.reason, "identity_mismatch")

        read_only = dict(env)
        read_only["X_OAUTH1_SCOPES"] = "read"
        calls = []

        def should_not_call(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("scope gate should run first")

        scope = monitor.probe_direct_x(read_only, opener=should_not_call)
        self.assertEqual(scope.status, "permission_denied")
        self.assertEqual(scope.reason, "scope_missing")
        self.assertEqual(calls, [])

        undeclared = dict(env)
        undeclared.pop("X_OAUTH1_SCOPES")
        missing_declaration = monitor.probe_direct_x(undeclared, opener=should_not_call)
        self.assertEqual(missing_declaration.status, "missing")
        self.assertEqual(missing_declaration.reason, "missing_configuration")
        self.assertEqual(calls, [])

        read_write = dict(env)
        read_write["X_OAUTH1_SCOPES"] = "read-write"
        compatible = monitor.probe_direct_x(
            read_write,
            opener=lambda _request, **_kwargs: FakeResponse(
                200,
                {"data": {"id": env["X_USER_ID"]}},
            ),
            nonce_func=lambda: "fixed-nonce",
            timestamp_func=lambda: 1234567890,
        )
        self.assertEqual(compatible.status, "healthy")

    def test_missing_and_transient_x_checks_are_normalized(self) -> None:
        missing = monitor.probe_direct_x({"X_API_KEY": "only-key"})
        self.assertEqual(missing.status, "missing")

        def unavailable(_request, **_kwargs):
            raise urllib.error.URLError("x credential secret detail")

        transient = monitor.probe_direct_x(complete_env(), opener=unavailable)
        self.assertEqual(transient.status, "transient")
        self.assertEqual(transient.reason, "transient_response")


class YouTubeProbeTests(unittest.TestCase):
    def test_refresh_then_channels_list_is_read_only_and_healthy(self) -> None:
        env = complete_env()
        opener, calls = youtube_router(env)
        result = monitor.probe_direct_youtube(env, opener=opener)

        self.assertEqual(result.status, "healthy")
        self.assertEqual(len(calls), 2)
        refresh, refresh_kwargs = calls[0]
        self.assertEqual(refresh.method, "POST")
        self.assertEqual(refresh.full_url, monitor.DEFAULT_YOUTUBE_TOKEN_URL)
        refresh_form = urllib_parse(refresh.data.decode("ascii"))
        self.assertEqual(refresh_form["grant_type"], ["refresh_token"])
        self.assertEqual(refresh_form["client_secret"], [env["YOUTUBE_CLIENT_SECRET"]])
        self.assertEqual(refresh_form["refresh_token"], [env["YOUTUBE_REFRESH_TOKEN"]])
        self.assertNotIn(env["YOUTUBE_CLIENT_SECRET"], refresh.full_url)
        self.assertNotIn(env["YOUTUBE_REFRESH_TOKEN"], refresh.full_url)
        self.assertEqual(refresh_kwargs["timeout"], 20)

        channels, channels_kwargs = calls[1]
        self.assertEqual(channels.method, "GET")
        self.assertIsNone(channels.data)
        self.assertIn("part=id", channels.full_url)
        self.assertIn("mine=true", channels.full_url)
        self.assertNotIn(env["YOUTUBE_CHANNEL_ID"], channels.full_url)
        self.assertEqual(
            channels.get_header("Authorization"),
            "Bearer short-lived-youtube-access-token",
        )
        self.assertEqual(channels_kwargs["timeout"], 20)

    def test_missing_oauth_configuration_does_not_call_network(self) -> None:
        calls = []

        def opener(*args, **kwargs):
            calls.append((args, kwargs))
            raise AssertionError("network should not be called")

        result = monitor.probe_direct_youtube(
            {"YOUTUBE_CLIENT_ID": "only-one-value"},
            opener=opener,
        )
        self.assertEqual(result.status, "missing")
        self.assertEqual(calls, [])

    def test_invalid_refresh_is_normalized_and_stops_before_channels_list(self) -> None:
        env = complete_env()
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(400, {"error": "invalid_grant", "description": env["YOUTUBE_REFRESH_TOKEN"]})

        result = monitor.probe_direct_youtube(env, opener=opener)
        self.assertEqual(result.status, "invalid")
        self.assertEqual(result.reason, "oauth_refresh_invalid")
        self.assertEqual(len(calls), 1)

    def test_permission_and_channel_mismatch_are_normalized(self) -> None:
        env = complete_env()

        def forbidden(request, **_kwargs):
            if request.full_url == monitor.DEFAULT_YOUTUBE_TOKEN_URL:
                return FakeResponse(200, {
                    "access_token": "access",
                    "scope": "https://www.googleapis.com/auth/youtube.upload",
                })
            return FakeResponse(403, {"error": {"message": "private"}})

        denied = monitor.probe_direct_youtube(env, opener=forbidden)
        self.assertEqual(denied.status, "permission_denied")

        def wrong_channel(request, **_kwargs):
            if request.full_url == monitor.DEFAULT_YOUTUBE_TOKEN_URL:
                return FakeResponse(200, {
                    "access_token": "access",
                    "scope": "https://www.googleapis.com/auth/youtube.upload",
                })
            return FakeResponse(200, {"items": [{"id": "different-channel"}]})

        mismatch = monitor.probe_direct_youtube(env, opener=wrong_channel)
        self.assertEqual(mismatch.status, "permission_denied")
        self.assertEqual(mismatch.reason, "youtube_channel_mismatch")

    def test_refresh_without_upload_scope_is_permission_denied(self) -> None:
        env = complete_env()
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(200, {
                "access_token": "access",
                "scope": "https://www.googleapis.com/auth/youtube.readonly",
            })

        result = monitor.probe_direct_youtube(env, opener=opener)
        self.assertEqual(result.status, "permission_denied")
        self.assertEqual(result.reason, "scope_missing")
        self.assertEqual(len(calls), 1)

    def test_network_error_is_transient(self) -> None:
        env = complete_env()

        def unavailable(_request, **_kwargs):
            raise urllib.error.URLError("secret response detail")

        result = monitor.probe_direct_youtube(env, opener=unavailable)
        self.assertEqual(result.status, "transient")
        self.assertEqual(result.reason, "transient_response")


def urllib_parse(value: str) -> dict[str, list[str]]:
    import urllib.parse

    return urllib.parse.parse_qs(value)


class MonitorReportTests(unittest.TestCase):
    def test_all_supported_statuses_have_priority_severity_and_text(self) -> None:
        self.assertEqual(monitor.VALID_STATUSES, {
            "healthy",
            "expiring_14d",
            "expiring_3d",
            "invalid",
            "permission_denied",
            "transient",
            "missing",
        })
        for status in monitor.VALID_STATUSES:
            with self.subTest(status=status):
                self.assertIn(status, monitor.STATUS_PRIORITY)
                self.assertIn(status, monitor.STATUS_SEVERITY)
                self.assertIn(status, monitor.STATUS_TEXT)
                self.assertEqual(monitor.ProbeResult(status, "reason").status, status)

    def test_buffer_is_optional_and_not_probed_when_unconfigured(self) -> None:
        env = {
            key: value
            for key, value in complete_env().items()
            if not key.startswith("BUFFER_")
        }

        def buffer_should_not_run(*_args, **_kwargs):
            raise AssertionError("optional Buffer monitor should stay disabled")

        report = monitor.run_monitor(
            env,
            now=NOW,
            force_email=True,
            buffer_probe_func=buffer_should_not_run,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        self.assertEqual(report.check_count, 3)
        self.assertEqual(
            [row.slot for row in report.checks],
            ["LINKEDIN_DIRECT", "X_DIRECT", "YOUTUBE_DIRECT"],
        )
        self.assertEqual(report.issue_count, 0)

    def test_force_email_sends_healthy_report_without_inventing_a_new_status(self) -> None:
        report = monitor.run_monitor(
            complete_env(),
            now=NOW,
            force_email=True,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        self.assertTrue(report.should_alert)
        self.assertEqual(report.alert_stage, "healthy")
        self.assertEqual(report.issue_count, 0)
        self.assertEqual(report.severity, "info")
        self.assertIn("测试", report.subject)

    def test_expiry_warnings_apply_to_matching_slots(self) -> None:
        env = complete_env()
        env.update(
            {
                "BUFFER_LINKEDIN_CREDENTIAL_EXPIRES_AT": (NOW + timedelta(days=14)).isoformat(),
                "BUFFER_X_CREDENTIAL_EXPIRES_AT": (NOW + timedelta(days=3)).isoformat(),
                "YOUTUBE_CREDENTIAL_EXPIRES_AT": (NOW - timedelta(seconds=1)).isoformat(),
            }
        )
        report = monitor.run_monitor(
            env,
            now=NOW,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        by_slot = {row.slot: row for row in report.checks}
        self.assertEqual(by_slot["BUFFER_LINKEDIN"].status, "expiring_14d")
        self.assertEqual(by_slot["BUFFER_X"].status, "expiring_3d")
        self.assertEqual(by_slot["YOUTUBE_DIRECT"].status, "invalid")
        self.assertEqual(by_slot["YOUTUBE_DIRECT"].reason, "credential_expired")
        self.assertEqual(report.alert_stage, "invalid")
        self.assertEqual(report.issue_count, 3)

    def test_probe_failure_and_expiry_choose_the_more_actionable_status(self) -> None:
        spec = monitor.SLOT_SPEC_BY_NAME["BUFFER_LINKEDIN"]
        env = {
            "BUFFER_LINKEDIN_CREDENTIAL_EXPIRES_AT": (NOW + timedelta(days=2)).isoformat()
        }
        transient = monitor.combine_probe_and_expiry(
            spec,
            monitor.ProbeResult("transient", "transient_response"),
            env,
            now=NOW,
        )
        self.assertEqual(transient.status, "expiring_3d")
        denied = monitor.combine_probe_and_expiry(
            spec,
            monitor.ProbeResult("permission_denied", "channel_locked"),
            env,
            now=NOW,
        )
        self.assertEqual(denied.status, "permission_denied")

    def test_dedupe_key_is_stable_and_changes_with_stage_or_version(self) -> None:
        env = complete_env()
        env["LINKEDIN_CREDENTIAL_VERSION"] = "7"
        first = monitor.run_monitor(
            env,
            now=NOW,
            force_email=True,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        later = monitor.run_monitor(
            env,
            now=NOW + timedelta(hours=6),
            force_email=True,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        self.assertEqual(first.dedupe_key, later.dedupe_key)

        replacement = dict(env)
        replacement["LINKEDIN_CREDENTIAL_VERSION"] = "8"
        replaced = monitor.run_monitor(
            replacement,
            now=NOW,
            force_email=True,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        self.assertNotEqual(first.dedupe_key, replaced.dedupe_key)

        expiring = dict(env)
        expiring["LINKEDIN_CREDENTIAL_EXPIRES_AT"] = (NOW + timedelta(days=10)).isoformat()
        warning = monitor.run_monitor(
            expiring,
            now=NOW,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        self.assertNotEqual(first.dedupe_key, warning.dedupe_key)

    def test_json_email_and_github_output_never_contain_secrets_ids_or_raw_body(self) -> None:
        env = complete_env()
        env.update(
            {
                "GITHUB_SERVER_URL": "https://github.com",
                "GITHUB_REPOSITORY": "owner/repository",
                "GITHUB_RUN_ID": "1234",
            }
        )
        buffer_opener, _buffer_calls = buffer_router(env)
        youtube_opener, _youtube_calls = youtube_router(env)
        buffer_results = monitor.probe_buffer_credentials(env, opener=buffer_opener)
        youtube_result = monitor.probe_direct_youtube(env, opener=youtube_opener)

        def linkedin_opener(_request, **_kwargs):
            return FakeResponse(
                200,
                {
                    "active": True,
                    "status": "active",
                    "client_id": env["LINKEDIN_CLIENT_ID"],
                    "scope": "w_member_social",
                    "privateProviderMarker": "linkedin-provider-body-must-not-leak",
                },
            )

        def x_opener(_request, **_kwargs):
            return FakeResponse(
                200,
                {
                    "data": {"id": env["X_USER_ID"]},
                    "privateProviderMarker": "x-provider-body-must-not-leak",
                },
            )

        linkedin_result = monitor.probe_direct_linkedin(env, opener=linkedin_opener)
        x_result = monitor.probe_direct_x(
            env,
            opener=x_opener,
            nonce_func=lambda: "redaction-nonce",
            timestamp_func=lambda: 1234567890,
        )

        report = monitor.run_monitor(
            env,
            now=NOW,
            force_email=True,
            buffer_probe_func=lambda _env, **_kwargs: buffer_results,
            linkedin_probe_func=lambda _env, **_kwargs: linkedin_result,
            x_probe_func=lambda _env, **_kwargs: x_result,
            youtube_probe_func=lambda _env, **_kwargs: youtube_result,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            email_path = root / "email.txt"
            json_path = root / "report.json"
            output_path = root / "github-output.txt"
            email = monitor.render_email(report, env)
            payload = json.dumps(monitor.report_payload(report), ensure_ascii=False)
            email_path.write_text(email, encoding="utf-8")
            json_path.write_text(payload, encoding="utf-8")
            monitor.write_github_output(output_path, report, email_path, json_path)
            combined = email + payload + output_path.read_text(encoding="utf-8")

        forbidden = tuple(complete_env().values()) + (
            "short-lived-youtube-access-token",
            "provider-body-must-not-leak",
            "linkedin-provider-body-must-not-leak",
            "x-provider-body-must-not-leak",
            "private-title",
        )
        for value in forbidden:
            with self.subTest(value=value):
                self.assertNotIn(value, combined)
        self.assertIn("BUFFER_LINKEDIN", combined)
        self.assertNotIn("privateProviderMarker", combined)
        self.assertNotIn("raw", json.dumps(monitor.report_payload(report)).casefold())

    def test_github_output_has_stable_single_line_contract(self) -> None:
        report = monitor.run_monitor(
            complete_env(),
            now=NOW,
            force_email=True,
            buffer_probe_func=healthy_buffer_probe,
            linkedin_probe_func=healthy_linkedin_probe,
            x_probe_func=healthy_x_probe,
            youtube_probe_func=healthy_youtube_probe,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "github-output.txt"
            email = root / "email.txt"
            report_json = root / "report.json"
            monitor.write_github_output(output, report, email, report_json)
            values = dict(
                line.split("=", 1)
                for line in output.read_text(encoding="utf-8").splitlines()
            )
        self.assertEqual(
            set(values),
            {
                "should_alert",
                "alert_stage",
                "severity",
                "subject",
                "dedupe_key",
                "check_count",
                "configured_count",
                "issue_count",
                "email_file",
                "json_file",
            },
        )
        self.assertEqual(values["should_alert"], "true")
        self.assertEqual(values["alert_stage"], "healthy")
        self.assertEqual(values["email_file"], str(email))
        self.assertEqual(values["json_file"], str(report_json))

    def test_cli_writes_workflow_files_and_stdout_is_sanitized(self) -> None:
        env = complete_env()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            json_path = root / "social.json"
            email_path = root / "social.txt"
            output_path = root / "github-output.txt"
            argv = [
                "check_social_credentials.py",
                "--force-email",
                "--now",
                NOW.isoformat(),
                "--json-output",
                str(json_path),
                "--email-output",
                str(email_path),
                "--github-output",
                str(output_path),
            ]
            stdout = io.StringIO()
            with (
                mock.patch.dict(os.environ, env, clear=True),
                mock.patch.object(sys, "argv", argv),
                mock.patch.object(monitor, "probe_buffer_credentials", healthy_buffer_probe),
                mock.patch.object(monitor, "probe_direct_linkedin", healthy_linkedin_probe),
                mock.patch.object(monitor, "probe_direct_x", healthy_x_probe),
                mock.patch.object(monitor, "probe_direct_youtube", healthy_youtube_probe),
                contextlib.redirect_stdout(stdout),
            ):
                self.assertEqual(monitor.main(), 0)

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            email = email_path.read_text(encoding="utf-8")
            outputs = output_path.read_text(encoding="utf-8")
        self.assertEqual(payload["alert_stage"], "healthy")
        self.assertEqual(len(payload["checks"]), 7)
        self.assertIn("BUFFER_ACCOUNT", email)
        self.assertIn("should_alert=true", outputs)
        combined = stdout.getvalue() + json.dumps(payload) + email + outputs
        for value in complete_env().values():
            self.assertNotIn(value, combined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
