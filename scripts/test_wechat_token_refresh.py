#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

import push_kc_translated_to_wechat_drafts as wechat


class _FakeResponse:
    def __init__(self, payload: dict[str, Any], status_code: int = 200) -> None:
        self.payload = payload
        self.status_code = status_code
        self.headers: dict[str, str] = {}
        self.text = json.dumps(payload, ensure_ascii=False)

    def json(self) -> dict[str, Any]:
        return self.payload


class _RecordingSession:
    def __init__(self, *responses: _FakeResponse) -> None:
        self.responses = list(responses)
        self.calls: list[dict[str, Any]] = []
        self.upload_handles: list[Any] = []
        self.upload_positions: list[int] = []
        self.upload_payloads: list[bytes] = []

    def post(self, url: str, **kwargs: Any) -> _FakeResponse:
        if not self.responses:
            raise AssertionError(f"Unexpected POST: {url}")
        call = {"url": url, **kwargs}
        self.calls.append(call)

        files = kwargs.get("files")
        if files:
            handle = files["media"][1]
            self.upload_handles.append(handle)
            self.upload_positions.append(handle.tell())
            self.upload_payloads.append(handle.read())
            handle.seek(0)

        return self.responses.pop(0)


def _response(**payload: Any) -> _FakeResponse:
    return _FakeResponse(payload)


def _manager(session: _RecordingSession) -> wechat.WeChatAccessTokenManager:
    return wechat.WeChatAccessTokenManager(
        session,  # type: ignore[arg-type]
        "test-appid",
        "test-secret",
        timeout=10,
    )


def _stable_token_force_flags(session: _RecordingSession) -> list[bool]:
    flags: list[bool] = []
    for call in session.calls:
        if call["url"].endswith("/stable_token"):
            payload = json.loads(call["data"].decode("utf-8"))
            flags.append(payload["force_refresh"])
    return flags


def _urls_containing(session: _RecordingSession, fragment: str) -> list[str]:
    return [call["url"] for call in session.calls if fragment in call["url"]]


class WeChatTokenRefreshTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sleep_patcher = patch.object(wechat.time, "sleep")
        self.monotonic_patcher = patch.object(wechat.time, "monotonic", return_value=100.0)
        self.sleep = self.sleep_patcher.start()
        self.monotonic = self.monotonic_patcher.start()
        self.addCleanup(self.monotonic_patcher.stop)
        self.addCleanup(self.sleep_patcher.stop)

    def test_initial_token_fetch_does_not_force_refresh(self) -> None:
        session = _RecordingSession(_response(access_token="initial-token", expires_in=7200))
        manager = _manager(session)

        self.assertEqual("initial-token", manager.current())

        self.assertEqual([False], _stable_token_force_flags(session))
        self.assertEqual([], session.responses)

    def test_token_refreshes_proactively_at_expires_in_boundary(self) -> None:
        session = _RecordingSession(
            _response(access_token="initial-token", expires_in=100),
            _response(access_token="refreshed-token", expires_in=100),
        )
        manager = _manager(session)
        self.monotonic.side_effect = [100.0, 189.999, 190.0, 190.0]

        self.assertEqual("initial-token", manager.current())
        self.assertEqual("initial-token", manager.current())
        self.assertEqual("refreshed-token", manager.current())

        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual([], session.responses)

    def test_add_draft_refreshes_after_42001_and_uses_new_url(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(access_token="new-token", expires_in=7200),
            _response(media_id="draft-media-id"),
        )
        manager = _manager(session)

        media_id = wechat.add_draft(session, manager, [{"title": "测试文章"}], timeout=10)  # type: ignore[arg-type]

        self.assertEqual("draft-media-id", media_id)
        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual(
            [
                "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=old-token",
                "https://api.weixin.qq.com/cgi-bin/draft/add?access_token=new-token",
            ],
            _urls_containing(session, "/draft/add?"),
        )
        self.assertEqual("new-token", manager.current())
        self.sleep.assert_not_called()

    def test_second_42001_after_refresh_is_raised_without_another_refresh(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(access_token="new-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired again"),
        )
        manager = _manager(session)

        with self.assertRaises(wechat.WeChatError) as raised:
            wechat.add_draft(session, manager, [{"title": "测试文章"}], timeout=10)  # type: ignore[arg-type]

        self.assertEqual(42001, raised.exception.errcode)
        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual(2, len(_urls_containing(session, "/draft/add?")))
        self.assertEqual([], session.responses)
        self.sleep.assert_not_called()

    def test_article_size_error_does_not_refresh_token(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=45008, errmsg="article size out of limit"),
        )
        manager = _manager(session)

        with self.assertRaises(wechat.WeChatError) as raised:
            wechat.add_draft(session, manager, [{"title": "测试文章"}], timeout=10)  # type: ignore[arg-type]

        self.assertEqual(45008, raised.exception.errcode)
        self.assertEqual([False], _stable_token_force_flags(session))
        self.assertEqual(1, len(_urls_containing(session, "/draft/add?")))
        self.sleep.assert_not_called()

    def test_find_recent_draft_with_raw_token_does_not_swallow_42001(self) -> None:
        session = _RecordingSession(
            _response(errcode=42001, errmsg="access_token expired"),
        )

        with self.assertRaises(wechat.WeChatError) as raised:
            wechat.find_recent_draft_by_titles(
                session,  # type: ignore[arg-type]
                "expired-token",
                ["测试文章"],
                timeout=10,
            )

        self.assertEqual(42001, raised.exception.errcode)
        self.assertEqual(
            ["https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token=expired-token"],
            _urls_containing(session, "/draft/batchget?"),
        )

    def test_verify_draft_get_refreshes_and_returns_success_summary(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(access_token="new-token", expires_in=7200),
            _response(news_item=[{"title": "测试文章"}], create_time=1, update_time=2),
        )
        manager = _manager(session)

        summary = wechat.verify_draft_get(
            session,  # type: ignore[arg-type]
            manager,
            "draft-media-id",
            timeout=10,
            expected_article_count=1,
        )

        self.assertTrue(summary["ok"])
        self.assertEqual(1, summary["article_count"])
        self.assertTrue(summary["matches_expected_article_count"])
        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual(
            [
                "https://api.weixin.qq.com/cgi-bin/draft/get?access_token=old-token",
                "https://api.weixin.qq.com/cgi-bin/draft/get?access_token=new-token",
            ],
            _urls_containing(session, "/draft/get?"),
        )

    def test_submit_publish_refreshes_after_42001(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(access_token="new-token", expires_in=7200),
            _response(publish_id="publish-id"),
        )
        manager = _manager(session)

        publish_id = wechat.submit_publish(
            session,  # type: ignore[arg-type]
            manager,
            "draft-media-id",
            timeout=10,
        )

        self.assertEqual("publish-id", publish_id)
        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual(
            [
                "https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token=old-token",
                "https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token=new-token",
            ],
            _urls_containing(session, "/freepublish/submit?"),
        )

    def test_upload_article_image_reopens_file_and_uses_refreshed_token(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(access_token="new-token", expires_in=7200),
            _response(url="https://mmbiz.qpic.cn/test-image"),
        )
        manager = _manager(session)

        with tempfile.TemporaryDirectory() as tmp:
            image_path = Path(tmp) / "article.png"
            image_bytes = b"test-image-bytes"
            image_path.write_bytes(image_bytes)

            image_url = wechat.upload_article_image(
                session,  # type: ignore[arg-type]
                manager,
                image_path,
                timeout=10,
            )

        self.assertEqual("https://mmbiz.qpic.cn/test-image", image_url)
        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual(
            [
                "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=old-token",
                "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=new-token",
            ],
            _urls_containing(session, "/media/uploadimg?"),
        )
        self.assertEqual([0, 0], session.upload_positions)
        self.assertEqual([image_bytes, image_bytes], session.upload_payloads)
        self.assertEqual(2, len(session.upload_handles))
        self.assertIsNot(session.upload_handles[0], session.upload_handles[1])
        self.assertTrue(all(handle.closed for handle in session.upload_handles))
        self.sleep.assert_not_called()

    def test_rejected_cached_token_escalates_to_one_forced_refresh(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(access_token="old-token", expires_in=7200),
            _response(access_token="new-token", expires_in=7200),
            _response(media_id="draft-media-id"),
        )
        manager = _manager(session)

        media_id = wechat.add_draft(
            session,  # type: ignore[arg-type]
            manager,
            [{"title": "测试文章"}],
            timeout=10,
        )

        self.assertEqual("draft-media-id", media_id)
        self.assertEqual([False, False, True], _stable_token_force_flags(session))
        self.assertEqual(2, len(_urls_containing(session, "/draft/add?")))

    def test_refresh_failure_is_not_swallowed_by_draft_lookup(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=7200),
            _response(errcode=42001, errmsg="access_token expired"),
            _response(errcode=40164, errmsg="stable_token unavailable"),
        )
        manager = _manager(session)

        with self.assertRaises(wechat.WeChatAccessTokenRefreshError):
            wechat.find_recent_draft_by_titles(
                session,  # type: ignore[arg-type]
                manager,
                ["测试文章"],
                timeout=10,
            )

        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual(1, len(_urls_containing(session, "/draft/batchget?")))

    def test_proactive_refresh_failure_is_not_softened_by_verification(self) -> None:
        session = _RecordingSession(
            _response(access_token="old-token", expires_in=100),
            _response(errcode=40164, errmsg="stable_token unavailable"),
        )
        manager = _manager(session)
        self.monotonic.side_effect = [100.0, 190.0]
        self.assertEqual("old-token", manager.current())

        with self.assertRaises(wechat.WeChatAccessTokenRefreshError):
            wechat.verify_draft_get(
                session,  # type: ignore[arg-type]
                manager,
                "draft-media-id",
                timeout=10,
                expected_article_count=1,
            )

        self.assertEqual([False, False], _stable_token_force_flags(session))
        self.assertEqual([], _urls_containing(session, "/draft/get?"))

    def test_request_errors_redact_access_token_query_values(self) -> None:
        rendered = wechat.safe_wechat_error(
            RuntimeError(
                "POST https://api.weixin.qq.com/cgi-bin/draft/add"
                "?access_token=super-secret-token&debug=1 failed"
            )
        )

        self.assertNotIn("super-secret-token", rendered)
        self.assertIn("access_token=***&debug=1", rendered)


if __name__ == "__main__":
    unittest.main()
