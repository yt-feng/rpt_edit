#!/usr/bin/env python3
"""Focused tests for bounded Portal search-mirror recovery behavior."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import portal_search_mirror as mirror


class PortalSearchMirrorTests(unittest.TestCase):
    def test_external_public_metadata_removes_aggregator_brand_and_channel_fallback(self) -> None:
        item = mirror.slim_external({
            "report_id": "external-1",
            "title": "Reportify | AI Infrastructure",
            "title_cn": "NashAI：人工智能基础设施",
            "institution_name": "Nash AI",
            "channel_name": "Reportify",
            "summary": "From reportify.cn · independent research summary",
        })
        self.assertIsNotNone(item)
        assert item is not None
        self.assertEqual(item["title"], "AI Infrastructure")
        self.assertEqual(item["title_cn"], "人工智能基础设施")
        self.assertEqual(item["institution"], "")
        self.assertEqual(item["summary"], "independent research summary")

        channel_only = mirror.slim_external({
            "report_id": "external-2",
            "title": "Valid title",
            "channel_name": "Legacy aggregator",
        })
        self.assertIsNotNone(channel_only)
        assert channel_only is not None
        self.assertEqual(channel_only["institution"], "")

    def test_authority_public_metadata_removes_aggregator_brand(self) -> None:
        item = mirror.slim_authority("foreign", {
            "id": "authority-1",
            "title": "NashAI - Global AI Outlook",
            "securities": "Nash AI",
            "companyName": "NashAI",
            "author": "MacroGate",
        })
        self.assertIsNotNone(item)
        assert item is not None
        self.assertEqual(item["title"], "Global AI Outlook")
        self.assertEqual(item["institution"], "")
        self.assertEqual(item["author"], "")

    def test_public_metadata_normalizes_confusable_and_zero_width_brand(self) -> None:
        self.assertEqual(mirror.public_brand_text("Ｎａｓｈ\u200bＡＩ：Outlook"), "Outlook")

    def test_expired_budget_avoids_request(self) -> None:
        method = Mock()
        with patch.object(mirror.time, "monotonic", return_value=10.0):
            with self.assertRaises(mirror.TimeBudgetExceeded):
                mirror.request_json_with_retries(
                    method,
                    "fixture",
                    retries=4,
                    retry_backoff=1.5,
                    deadline=9.0,
                    timeout=30.0,
                )
        method.assert_not_called()

    def test_request_timeout_is_bounded_by_remaining_budget(self) -> None:
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {"ok": True}
        method = Mock(return_value=response)
        with patch.object(mirror.time, "monotonic", return_value=10.0):
            result = mirror.request_json_with_retries(
                method,
                "fixture",
                retries=1,
                retry_backoff=1.5,
                deadline=12.5,
                timeout=30.0,
            )
        self.assertEqual(result, {"ok": True})
        self.assertEqual(method.call_args.kwargs["timeout"], 2.5)

    def test_previous_snapshot_freshness_uses_generated_timestamp(self) -> None:
        client = Mock()
        now = datetime(2026, 8, 16, 7, 0, tzinfo=timezone.utc)
        payload = {"generated_at": "2026-08-15T08:00:00Z"}
        client.get_object.side_effect = lambda **_kwargs: {
            "Body": io.BytesIO(json.dumps(payload).encode("utf-8"))
        }
        with patch.dict(mirror.os.environ, {"R2_BUCKET": "fixture-bucket"}):
            self.assertTrue(
                mirror.previous_mirror_is_fresh("external", 24, now=now, client=client)
            )
            self.assertFalse(
                mirror.previous_mirror_is_fresh("external", 22, now=now, client=client)
            )
        client.get_object.assert_called_with(
            Bucket="fixture-bucket",
            Key="_search-mirror/external/latest.json",
        )

    def test_malformed_previous_snapshot_is_not_fresh(self) -> None:
        client = Mock()
        client.get_object.return_value = {"Body": io.BytesIO(b"private invalid body")}
        with patch.dict(mirror.os.environ, {"R2_BUCKET": "fixture-bucket"}):
            with redirect_stderr(io.StringIO()):
                self.assertFalse(mirror.previous_mirror_is_fresh("authority", 24, client=client))

    def test_incomplete_refresh_is_healthy_with_fresh_previous_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            args = [
                "portal_search_mirror.py",
                "--output-dir",
                str(Path(temp) / "output"),
                "--upload-r2",
            ]
            with (
                patch.object(mirror.sys, "argv", args),
                patch.object(mirror, "fetch_external_pages", return_value=([], False)),
                patch.object(mirror, "fetch_authority_pages", return_value=([], True)),
                patch.object(mirror, "previous_mirror_is_fresh", return_value=True),
                patch.object(mirror, "upload_r2") as upload,
                redirect_stdout(io.StringIO()),
                redirect_stderr(io.StringIO()),
            ):
                self.assertEqual(mirror.main(), 0)
        upload.assert_called_once()
        self.assertEqual(upload.call_args.args[0], "authority")

    def test_incomplete_refresh_fails_after_grace_window(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            args = [
                "portal_search_mirror.py",
                "--output-dir",
                str(Path(temp) / "output"),
                "--upload-r2",
            ]
            with (
                patch.object(mirror.sys, "argv", args),
                patch.object(mirror, "fetch_external_pages", return_value=([], False)),
                patch.object(mirror, "fetch_authority_pages", return_value=([], True)),
                patch.object(mirror, "previous_mirror_is_fresh", return_value=False),
                patch.object(mirror, "upload_r2"),
                redirect_stdout(io.StringIO()),
                redirect_stderr(io.StringIO()),
            ):
                self.assertEqual(mirror.main(), 1)


if __name__ == "__main__":
    unittest.main()
