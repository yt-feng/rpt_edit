#!/usr/bin/env python3

from __future__ import annotations

import io
import json
import tempfile
import unittest
import urllib.error
import urllib.parse
from pathlib import Path
from typing import Any

try:
    from scripts.social_publish_youtube import (
        YouTubeAuditBlockerError,
        YouTubeAuthenticationError,
        YouTubeProcessingError,
        YouTubeTransientError,
        publish_youtube,
    )
except ModuleNotFoundError:
    from social_publish_youtube import (  # type: ignore[no-redef]
        YouTubeAuditBlockerError,
        YouTubeAuthenticationError,
        YouTubeProcessingError,
        YouTubeTransientError,
        publish_youtube,
    )


class _FakeResponse:
    def __init__(
        self,
        status: int,
        body: bytes = b"",
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status = status
        self._body = body
        self.headers = headers or {}

    def read(self, limit: int = -1) -> bytes:
        return self._body if limit < 0 else self._body[:limit]

    def getcode(self) -> int:
        return self.status

    def close(self) -> None:
        return None


class _ScriptedOpener:
    def __init__(self, actions: list[dict[str, Any]]) -> None:
        self.actions = list(actions)
        self.requests: list[dict[str, Any]] = []

    def __call__(self, request: Any, timeout: float | None = None) -> _FakeResponse:
        data = request.data
        if data is None:
            captured_data = None
        elif isinstance(data, bytes):
            captured_data = data
        else:
            captured_data = b"".join(data)
        self.requests.append(
            {
                "method": request.get_method(),
                "url": request.full_url,
                "headers": {key.lower(): value for key, value in request.header_items()},
                "data": captured_data,
                "timeout": timeout,
            }
        )
        if not self.actions:
            raise AssertionError("unexpected network request")
        action = self.actions.pop(0)
        if "raise" in action:
            raise action["raise"]
        status = int(action.get("status", 200))
        body = action.get("body", b"")
        headers = action.get("headers", {})
        if status >= 400:
            raise urllib.error.HTTPError(
                request.full_url,
                status,
                "provider detail must not escape",
                headers,
                io.BytesIO(body),
            )
        return _FakeResponse(status, body, headers)


class YouTubePublisherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.asset_root = Path(self.temp_dir.name)
        self.media = self.asset_root / "episode.mp4"
        self.media_bytes = b"fake-video-payload"
        self.media.write_bytes(self.media_bytes)
        self.env = {
            "YOUTUBE_CLIENT_ID": "client-secret-id",
            "YOUTUBE_CLIENT_SECRET": "client-super-secret",
            "YOUTUBE_REFRESH_TOKEN": "refresh-super-secret",
            "YOUTUBE_TOKEN_URL": "https://oauth.test/token",
            "YOUTUBE_VIDEOS_INSERT_URL": "https://youtube.test/upload/videos",
            "YOUTUBE_VIDEOS_LIST_URL": "https://youtube.test/api/videos",
            "YOUTUBE_WATCH_URL_TEMPLATE": "https://watch.test/{video_id}",
            "YOUTUBE_HTTP_RETRY_BASE_SECONDS": "1",
            "YOUTUBE_HTTP_RETRY_MAX_SECONDS": "8",
            "YOUTUBE_PROCESSING_POLL_SECONDS": "0",
            "YOUTUBE_PROCESSING_MAX_POLLS": "3",
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def config(self, **updates: Any) -> dict[str, Any]:
        config: dict[str, Any] = {
            "media_path": self.media.name,
            "title": "Original episode title",
            "description": "Original, human-reviewed description.",
            "category_id": "22",
            "privacy_status": "private",
            "publish_at": "2030-02-03T04:05:06Z",
            "made_for_kids": False,
            "contains_synthetic_media": True,
            "notify_subscribers": False,
            "tags": ["markets", "research"],
        }
        config.update(updates)
        return config

    @staticmethod
    def json_body(payload: Any) -> bytes:
        return json.dumps(payload).encode("utf-8")

    def success_actions(
        self,
        *,
        privacy: str = "private",
        processing_sequence: tuple[str, ...] = ("succeeded",),
    ) -> list[dict[str, Any]]:
        actions: list[dict[str, Any]] = [
            {
                "status": 200,
                "body": self.json_body(
                    {"access_token": "short-lived-access-secret", "expires_in": 3600}
                ),
            },
            {
                "status": 200,
                "headers": {"Location": "https://upload-session.test/secret-session"},
            },
            {"status": 200, "body": self.json_body({"id": "Video_123"})},
        ]
        for processing in processing_sequence:
            actions.append(
                {
                    "status": 200,
                    "body": self.json_body(
                        {
                            "items": [
                                {
                                    "id": "Video_123",
                                    "status": {
                                        "privacyStatus": privacy,
                                        "uploadStatus": (
                                            "processed" if processing == "succeeded" else "uploaded"
                                        ),
                                    },
                                    "processingDetails": {
                                        "processingStatus": processing,
                                    },
                                }
                            ]
                        }
                    ),
                }
            )
        return actions

    def test_success_uses_official_metadata_and_returns_sanitized_receipt(self) -> None:
        opener = _ScriptedOpener(
            self.success_actions(processing_sequence=("processing", "succeeded"))
        )
        sleeps: list[float] = []

        receipt = publish_youtube(
            self.config(),
            asset_root=self.asset_root,
            env=self.env,
            opener=opener,
            sleep_func=sleeps.append,
        )

        self.assertEqual(
            receipt,
            {
                "state": "published",
                "video_id": "Video_123",
                "url": "https://watch.test/Video_123",
                "privacy_status": "private",
                "processing_status": "succeeded",
                "publish_at": "2030-02-03T04:05:06Z",
            },
        )
        self.assertEqual(set(receipt), {
            "state", "video_id", "url", "privacy_status", "processing_status", "publish_at"
        })
        self.assertNotIn("short-lived-access-secret", json.dumps(receipt))

        token_request, metadata_request, media_request = opener.requests[:3]
        token_form = urllib.parse.parse_qs(token_request["data"].decode("ascii"))
        self.assertEqual(token_form["grant_type"], ["refresh_token"])
        self.assertEqual(token_form["refresh_token"], ["refresh-super-secret"])

        query = urllib.parse.parse_qs(urllib.parse.urlsplit(metadata_request["url"]).query)
        self.assertEqual(query["uploadType"], ["resumable"])
        self.assertEqual(query["part"], ["snippet,status"])
        self.assertEqual(query["notifySubscribers"], ["false"])
        self.assertEqual(
            json.loads(metadata_request["data"].decode("utf-8")),
            {
                "snippet": {
                    "title": "Original episode title",
                    "description": "Original, human-reviewed description.",
                    "categoryId": "22",
                    "tags": ["markets", "research"],
                },
                "status": {
                    "privacyStatus": "private",
                    "publishAt": "2030-02-03T04:05:06Z",
                    "selfDeclaredMadeForKids": False,
                    "containsSyntheticMedia": True,
                },
            },
        )
        self.assertEqual(media_request["method"], "PUT")
        self.assertEqual(media_request["data"], self.media_bytes)
        self.assertEqual(sleeps, [0.0])

    def test_5xx_and_429_are_retried_with_bounded_exponential_backoff(self) -> None:
        actions = [
            {"status": 503, "body": b'provider raw body: refresh-super-secret'},
            {
                "status": 200,
                "body": self.json_body({"access_token": "short-lived-access-secret"}),
            },
            {
                "status": 200,
                "headers": {"Location": "https://upload-session.test/session"},
            },
            {"status": 200, "body": self.json_body({"id": "Video_123"})},
            {
                "status": 429,
                "headers": {"Retry-After": "2"},
                "body": b'provider raw body: client-super-secret',
            },
            *self.success_actions()[3:],
        ]
        opener = _ScriptedOpener(actions)
        sleeps: list[float] = []

        receipt = publish_youtube(
            self.config(),
            asset_root=self.asset_root,
            env=self.env,
            opener=opener,
            sleep_func=sleeps.append,
        )

        self.assertEqual(receipt["video_id"], "Video_123")
        self.assertEqual(sleeps, [1.0, 2.0])
        self.assertEqual(len(opener.requests), 6)

    def test_retry_budget_is_bounded_and_error_is_sanitized(self) -> None:
        raw_secret = "refresh-super-secret"
        env = {**self.env, "YOUTUBE_HTTP_MAX_ATTEMPTS": "3"}
        opener = _ScriptedOpener(
            [
                {"status": 503, "body": f"raw-{raw_secret}-{index}".encode()}
                for index in range(3)
            ]
        )
        sleeps: list[float] = []

        with self.assertRaises(YouTubeTransientError) as caught:
            publish_youtube(
                self.config(),
                asset_root=self.asset_root,
                env=env,
                opener=opener,
                sleep_func=sleeps.append,
            )

        self.assertEqual(caught.exception.code, "provider_unavailable")
        self.assertEqual(len(opener.requests), 3)
        self.assertEqual(sleeps, [1.0, 2.0])
        self.assertNotIn(raw_secret, str(caught.exception))
        self.assertNotIn(raw_secret, repr(caught.exception))

    def test_session_init_ambiguous_response_fails_closed_without_repost(self) -> None:
        ambiguous_actions = (
            {"raise": RuntimeError("transport-secret-refresh-super-secret")},
            {
                "status": 429,
                "headers": {"Retry-After": "5"},
                "body": b"rate-limit-provider-secret",
            },
            {"status": 503, "body": b"provider-unavailable-secret"},
        )
        for ambiguous_action in ambiguous_actions:
            with self.subTest(action=sorted(ambiguous_action)):
                opener = _ScriptedOpener(
                    [
                        {
                            "status": 200,
                            "body": self.json_body(
                                {"access_token": "short-lived-access-secret"}
                            ),
                        },
                        ambiguous_action,
                    ]
                )
                sleeps: list[float] = []

                with self.assertRaises(YouTubeTransientError) as caught:
                    publish_youtube(
                        self.config(),
                        asset_root=self.asset_root,
                        env=self.env,
                        opener=opener,
                        sleep_func=sleeps.append,
                    )

                self.assertEqual(caught.exception.code, "upload_session_ambiguous")
                self.assertEqual(len(opener.requests), 2)
                self.assertEqual(opener.requests[1]["method"], "POST")
                self.assertEqual(sleeps, [])
                sanitized = json.dumps(caught.exception.as_dict())
                for secret in (
                    "refresh-super-secret",
                    "rate-limit-provider-secret",
                    "provider-unavailable-secret",
                ):
                    self.assertNotIn(secret, sanitized)

    def test_final_put_response_lost_queries_same_session_and_recovers_receipt(self) -> None:
        session_url = "https://upload-session.test/final-response-lost"
        opener = _ScriptedOpener(
            [
                {
                    "status": 200,
                    "body": self.json_body({"access_token": "short-lived-access-secret"}),
                },
                {"status": 200, "headers": {"Location": session_url}},
                {"raise": RuntimeError("lost-final-response-provider-secret")},
                {
                    "status": 308,
                    "headers": {"Range": f"bytes=0-{len(self.media_bytes) - 1}"},
                },
                {"status": 200, "body": self.json_body({"id": "Video_123"})},
                *self.success_actions()[3:],
            ]
        )

        receipt = publish_youtube(
            self.config(),
            asset_root=self.asset_root,
            env=self.env,
            opener=opener,
            sleep_func=lambda _: None,
        )

        self.assertEqual(receipt["video_id"], "Video_123")
        media_put = opener.requests[2]
        status_query = opener.requests[3]
        completion_query = opener.requests[4]
        self.assertEqual(media_put["url"], session_url)
        self.assertEqual(status_query["url"], session_url)
        self.assertEqual(status_query["method"], "PUT")
        self.assertEqual(status_query["data"], b"")
        self.assertEqual(
            status_query["headers"]["content-range"],
            f"bytes */{len(self.media_bytes)}",
        )
        self.assertEqual(completion_query["url"], session_url)
        self.assertEqual(completion_query["data"], b"")
        self.assertEqual(
            completion_query["headers"]["content-range"],
            f"bytes */{len(self.media_bytes)}",
        )
        self.assertNotIn("lost-final-response-provider-secret", json.dumps(receipt))

    def test_chunk_429_and_5xx_query_status_before_any_media_retry(self) -> None:
        for status in (429, 503):
            with self.subTest(status=status):
                session_url = f"https://upload-session.test/ambiguous-{status}"
                opener = _ScriptedOpener(
                    [
                        {
                            "status": 200,
                            "body": self.json_body(
                                {"access_token": "short-lived-access-secret"}
                            ),
                        },
                        {"status": 200, "headers": {"Location": session_url}},
                        {
                            "status": status,
                            "headers": {"Retry-After": "1"},
                            "body": b"ambiguous-write-provider-secret",
                        },
                        {"status": 200, "body": self.json_body({"id": "Video_123"})},
                        *self.success_actions()[3:],
                    ]
                )

                receipt = publish_youtube(
                    self.config(),
                    asset_root=self.asset_root,
                    env=self.env,
                    opener=opener,
                    sleep_func=lambda _: None,
                )

                self.assertEqual(receipt["video_id"], "Video_123")
                media_put, status_query = opener.requests[2:4]
                self.assertEqual(media_put["data"], self.media_bytes)
                self.assertEqual(status_query["data"], b"")
                self.assertEqual(status_query["url"], session_url)
                self.assertEqual(
                    status_query["headers"]["content-range"],
                    f"bytes */{len(self.media_bytes)}",
                )

    def test_partial_chunk_received_is_queried_then_resumed_from_confirmed_offset(self) -> None:
        self.media_bytes = b"abcdefghij"
        self.media.write_bytes(self.media_bytes)
        session_url = "https://upload-session.test/partial"
        opener = _ScriptedOpener(
            [
                {
                    "status": 200,
                    "body": self.json_body({"access_token": "short-lived-access-secret"}),
                },
                {"status": 200, "headers": {"Location": session_url}},
                {"raise": RuntimeError("partial-response-provider-secret")},
                {"status": 308, "headers": {"Range": "bytes=0-3"}},
                {"status": 200, "body": self.json_body({"id": "Video_123"})},
                *self.success_actions()[3:],
            ]
        )

        receipt = publish_youtube(
            self.config(),
            asset_root=self.asset_root,
            env=self.env,
            opener=opener,
            sleep_func=lambda _: None,
        )

        self.assertEqual(receipt["video_id"], "Video_123")
        first_put, status_query, resumed_put = opener.requests[2:5]
        self.assertEqual(first_put["headers"]["content-range"], "bytes 0-9/10")
        self.assertEqual(first_put["data"], b"abcdefghij")
        self.assertEqual(status_query["headers"]["content-range"], "bytes */10")
        self.assertEqual(status_query["data"], b"")
        self.assertEqual(resumed_put["headers"]["content-range"], "bytes 4-9/10")
        self.assertEqual(resumed_put["data"], b"efghij")

    def test_resumable_308_continues_from_acknowledged_offset(self) -> None:
        chunk_size = 256 * 1024
        self.media_bytes = b"a" * chunk_size + b"tail"
        self.media.write_bytes(self.media_bytes)
        env = {**self.env, "YOUTUBE_UPLOAD_CHUNK_BYTES": str(chunk_size)}
        opener = _ScriptedOpener(
            [
                {
                    "status": 200,
                    "body": self.json_body({"access_token": "short-lived-access-secret"}),
                },
                {
                    "status": 200,
                    "headers": {"Location": "https://upload-session.test/session"},
                },
                {
                    "status": 308,
                    "headers": {"Range": f"bytes=0-{chunk_size - 1}"},
                },
                {"status": 200, "body": self.json_body({"id": "Video_123"})},
                *self.success_actions()[3:],
            ]
        )

        receipt = publish_youtube(
            self.config(),
            asset_root=self.asset_root,
            env=env,
            opener=opener,
            sleep_func=lambda _: None,
        )

        self.assertEqual(receipt["video_id"], "Video_123")
        first_chunk, final_chunk = opener.requests[2:4]
        self.assertEqual(
            first_chunk["headers"]["content-range"],
            f"bytes 0-{chunk_size - 1}/{len(self.media_bytes)}",
        )
        self.assertEqual(first_chunk["data"], b"a" * chunk_size)
        self.assertEqual(
            final_chunk["headers"]["content-range"],
            f"bytes {chunk_size}-{len(self.media_bytes) - 1}/{len(self.media_bytes)}",
        )
        self.assertEqual(final_chunk["data"], b"tail")

    def test_public_request_returned_private_is_audit_blocker(self) -> None:
        opener = _ScriptedOpener(self.success_actions(privacy="private"))

        with self.assertRaises(YouTubeAuditBlockerError) as caught:
            publish_youtube(
                self.config(privacy_status="public", publish_at=None),
                asset_root=self.asset_root,
                env=self.env,
                opener=opener,
                sleep_func=lambda _: None,
            )

        self.assertEqual(caught.exception.code, "youtube_api_audit_required")
        self.assertEqual(caught.exception.http_status, 200)
        self.assertNotIn("short-lived-access-secret", str(caught.exception))
        self.assertNotIn("secret-session", str(caught.exception))

    def test_video_locator_callback_runs_before_processing_failure(self) -> None:
        opener = _ScriptedOpener(
            self.success_actions(processing_sequence=("failed",))
        )
        locators = []
        with self.assertRaises(YouTubeProcessingError):
            publish_youtube(
                self.config(),
                asset_root=self.asset_root,
                env=self.env,
                opener=opener,
                sleep_func=lambda _: None,
                receipt_callback=locators.append,
            )
        self.assertEqual(locators, [{
            "video_id": "Video_123",
            "publish_at": "2030-02-03T04:05:06Z",
        }])

    def test_oauth_error_body_and_credentials_are_never_exposed(self) -> None:
        raw_body_secret = "provider-error-description-secret"
        opener = _ScriptedOpener(
            [
                {
                    "status": 400,
                    "body": self.json_body(
                        {
                            "error": "invalid_grant",
                            "error_description": raw_body_secret,
                            "echo": "refresh-super-secret client-super-secret",
                        }
                    ),
                }
            ]
        )

        with self.assertRaises(YouTubeAuthenticationError) as caught:
            publish_youtube(
                self.config(),
                asset_root=self.asset_root,
                env=self.env,
                opener=opener,
                sleep_func=lambda _: None,
            )

        self.assertEqual(caught.exception.code, "oauth_refresh_invalid")
        serialized = json.dumps(caught.exception.as_dict())
        for secret in (
            raw_body_secret,
            "refresh-super-secret",
            "client-super-secret",
            "client-secret-id",
        ):
            self.assertNotIn(secret, str(caught.exception))
            self.assertNotIn(secret, repr(caught.exception))
            self.assertNotIn(secret, serialized)


if __name__ == "__main__":
    unittest.main()
