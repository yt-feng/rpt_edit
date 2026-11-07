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


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import social_publish_control as control


NOW = datetime(2026, 8, 31, 1, 0, tzinfo=timezone.utc)


def valid_manifest():
    return {
        "schema_version": 1,
        "content_id": "2026-08-31-market-brief",
        "approved": True,
        "not_before": "2026-08-31T08:00:00+08:00",
        "source_url": "https://example.invalid/research/market-brief",
        "source": {
            "run_id": "123456",
            "artifact_name": "bilingual-podcast-videos-123456",
        },
        "platforms": {
            "youtube": {
                "enabled": True,
                "media_path": "videos/brief.mp4",
                "media_sha256": "0cab1c9617404faf2b24e221e189ca5945813e14d3f766345b09ca13bbe28ffc",
                "title": "What changed in global markets this week",
                "description": (
                    "A source-grounded review of the week's market changes, the mechanism behind them, "
                    "and the next variable worth watching. Full source notes: "
                    "https://example.invalid/research/market-brief"
                ),
                "category_id": "27",
                "privacy_status": "private",
                "publish_at": "2026-09-01T12:00:00+08:00",
                "made_for_kids": False,
                "contains_synthetic_media": True,
                "notify_subscribers": False,
                "tags": ["markets", "research"],
            },
            "linkedin": {
                "enabled": True,
                "text": (
                    "Three market changes looked unrelated this week. They share one transmission "
                    "mechanism, and the source data points to a specific variable to watch next. "
                    "The full evidence and video are here: {{YOUTUBE_URL}} #Markets #Research"
                ),
            },
            "x": {
                "enabled": True,
                "text": (
                    "Three market moves, one shared mechanism. The useful signal is not the headline; "
                    "it is the next variable in the chain. Evidence and video: {{YOUTUBE_URL}} #Markets"
                ),
            },
        },
    }


class FakeResponse:
    def __init__(self, status, payload, headers=None):
        self.status = status
        self.payload = payload
        self.headers = headers or {}

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def getcode(self):
        return self.status

    def read(self, _limit=-1):
        return json.dumps(self.payload).encode("utf-8")


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "videos").mkdir()
        (self.root / "videos" / "brief.mp4").write_bytes(b"video")
        self.manifest_path = self.root / "manifest.json"

    def tearDown(self):
        self.temporary.cleanup()

    def write(self, payload):
        self.manifest_path.write_text(json.dumps(payload), encoding="utf-8")
        return control.load_manifest(
            self.manifest_path,
            asset_root=self.root,
            require_media=True,
        )

    def test_valid_manifest_produces_sanitized_preview(self):
        plan = self.write(valid_manifest())
        preview = control.sanitized_preview(plan)
        self.assertEqual(plan.platforms, ("youtube", "linkedin", "x"))
        rendered = json.dumps(preview)
        self.assertNotIn("Three market", rendered)
        self.assertNotIn("example.invalid/research", rendered)
        self.assertIn("contains_synthetic_media", rendered)

    def test_manifest_digest_ignores_json_formatting(self):
        payload = valid_manifest()
        first = self.write(payload).digest
        self.manifest_path.write_text(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=4),
            encoding="utf-8",
        )
        second = control.load_manifest(self.manifest_path, asset_root=self.root).digest
        self.assertEqual(first, second)

    def test_cookie_browser_and_engagement_fields_are_rejected(self):
        for field in ("cookie", "browser", "reply_to", "auto_like", "repost"):
            payload = valid_manifest()
            payload["platforms"]["x"][field] = True
            with self.subTest(field=field), self.assertRaisesRegex(
                control.ManifestError,
                "unsupported fields",
            ):
                self.write(payload)

    def test_media_path_must_stay_inside_artifact(self):
        payload = valid_manifest()
        payload["platforms"]["youtube"]["media_path"] = "../secret.mp4"
        with self.assertRaisesRegex(control.ManifestError, "stay inside"):
            self.write(payload)

    def test_media_digest_binds_the_approved_artifact(self):
        payload = valid_manifest()
        payload["platforms"]["youtube"]["media_sha256"] = "f" * 64
        with self.assertRaisesRegex(control.ManifestError, "does not match media_sha256"):
            self.write(payload)

    def test_youtube_disclosure_fields_are_mandatory_booleans(self):
        for field in ("made_for_kids", "contains_synthetic_media", "notify_subscribers"):
            payload = valid_manifest()
            del payload["platforms"]["youtube"][field]
            with self.subTest(field=field), self.assertRaisesRegex(
                control.ManifestError,
                "must be true or false",
            ):
                self.write(payload)

    def test_scheduled_youtube_requires_private(self):
        payload = valid_manifest()
        payload["platforms"]["youtube"]["privacy_status"] = "public"
        with self.assertRaisesRegex(control.ManifestError, "requires privacy_status=private"):
            self.write(payload)

    def test_linkedin_and_x_copy_must_be_distinct(self):
        payload = valid_manifest()
        payload["platforms"]["linkedin"]["text"] = payload["platforms"]["x"]["text"]
        with self.assertRaisesRegex(control.ManifestError, "platform-specific copy"):
            self.write(payload)

    def test_automated_mentions_and_shorteners_are_rejected(self):
        payload = valid_manifest()
        payload["platforms"]["x"]["text"] = (
            "@someone This is a sufficiently long automated mention with evidence at "
            "https://bit.ly/example and extra context."
        )
        with self.assertRaises(control.ManifestError):
            self.write(payload)

    def test_only_supported_template_placeholders_are_allowed(self):
        payload = valid_manifest()
        payload["platforms"]["linkedin"]["text"] += " {{COOKIE}}"
        with self.assertRaisesRegex(control.ManifestError, "unsupported placeholders"):
            self.write(payload)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "videos").mkdir()
        (self.root / "videos" / "brief.mp4").write_bytes(b"video")
        self.manifest_path = self.root / "manifest.json"
        self.manifest_path.write_text(json.dumps(valid_manifest()), encoding="utf-8")
        self.plan = control.load_manifest(self.manifest_path, asset_root=self.root)
        self.ledger = self.root / "receipts"

    def tearDown(self):
        self.temporary.cleanup()

    def test_reservation_is_fail_closed_and_contains_no_post_copy(self):
        path, receipt = control.reserve(
            self.plan,
            ledger_dir=self.ledger,
            run_id="9001",
            run_url="https://github.com/example/project/actions/runs/9001",
            now=NOW,
            env={},
        )
        rendered = path.read_text(encoding="utf-8")
        self.assertEqual(receipt["state"], "reserved")
        self.assertNotIn("Three market", rendered)
        with self.assertRaisesRegex(control.ManifestError, "unresolved receipt"):
            control.enforce_ledger_guards(
                self.plan,
                ledger_dir=self.ledger,
                now=NOW,
                env={},
            )

    def test_reviewed_no_write_resolution_is_required_before_manual_continue(self):
        path, _receipt = control.reserve(
            self.plan,
            ledger_dir=self.ledger,
            run_id="9001",
            run_url="https://github.com/example/project/actions/runs/9001",
            now=NOW,
            env={},
        )
        payload = valid_manifest()
        payload["content_id"] = "2026-09-02-different-brief"
        payload["platforms"]["youtube"]["title"] = "A different market mechanism to watch next week"
        payload["platforms"]["youtube"]["description"] += " Additional distinct source context."
        payload["platforms"]["linkedin"]["text"] += " A different supporting observation."
        payload["platforms"]["x"]["text"] = (
            "A different market mechanism now matters more than the headline. "
            "Here is the evidence chain and the next variable: {{YOUTUBE_URL}} #Research"
        )
        other = self.root / "other.json"
        other.write_text(json.dumps(payload), encoding="utf-8")
        plan = control.load_manifest(other, asset_root=self.root)
        with self.assertRaisesRegex(control.ManifestError, "unresolved receipt"):
            control.enforce_ledger_guards(plan, ledger_dir=self.ledger, now=NOW, env={})

        stored = json.loads(path.read_text(encoding="utf-8"))
        stored["state"] = "resolved_not_published"
        stored["resolution"] = {
            "decision": "confirmed_no_provider_write",
            "reviewed_by": "release-reviewer",
            "reviewed_at": control.iso_utc(NOW + timedelta(hours=1)),
        }
        path.write_text(json.dumps(stored), encoding="utf-8")
        control.enforce_ledger_guards(plan, ledger_dir=self.ledger, now=NOW + timedelta(hours=2), env={})

    def test_exact_and_near_duplicates_are_rejected_across_content_ids(self):
        path, stored = control.reserve(
            self.plan,
            ledger_dir=self.ledger,
            run_id="9001",
            run_url="https://github.com/example/project/actions/runs/9001",
            now=NOW,
            env={},
        )
        stored["state"] = "published"
        stored["completed_at"] = control.iso_utc(NOW)
        stored["results"] = {
            platform: {"state": "published"} for platform in self.plan.platforms
        }
        path.write_text(json.dumps(stored), encoding="utf-8")
        payload = valid_manifest()
        payload["content_id"] = "2026-09-02-market-brief"
        payload["not_before"] = "2026-09-02T08:00:00+08:00"
        other = self.root / "other.json"
        other.write_text(json.dumps(payload), encoding="utf-8")
        plan = control.load_manifest(other, asset_root=self.root)
        with self.assertRaisesRegex(control.ManifestError, "duplicates|too similar"):
            control.enforce_ledger_guards(
                plan,
                ledger_dir=self.ledger,
                now=NOW + timedelta(days=3),
                env={},
            )

    def test_minimum_interval_is_enforced_for_successful_platforms(self):
        receipt = {
            "schema_version": 1,
            "content_id": "older-item",
            "manifest_sha256": "0" * 64,
            "state": "published",
            "completed_at": control.iso_utc(NOW - timedelta(hours=8)),
            "fingerprints": {},
            "simhashes": {},
            "results": {"x": {"state": "published"}},
        }
        self.ledger.mkdir()
        (self.ledger / "older-item.json").write_text(json.dumps(receipt), encoding="utf-8")
        with self.assertRaisesRegex(control.ManifestError, "minimum publication interval"):
            control.enforce_ledger_guards(
                self.plan,
                ledger_dir=self.ledger,
                now=NOW,
                env={"SOCIAL_MIN_INTERVAL_HOURS": "20"},
            )

    def test_durable_reach_pause_blocks_reservation(self):
        (self.root / "PAUSED.json").write_text(
            json.dumps({"schema_version": 1, "reason": "consecutive_zero_reach"}),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(control.ManifestError, "reach monitor"):
            control.reserve(
                self.plan,
                ledger_dir=self.ledger,
                run_id="9001",
                run_url="https://github.com/example/project/actions/runs/9001",
                now=NOW,
                env={},
            )

    def test_matching_reservation_requires_same_run_and_digest(self):
        control.reserve(
            self.plan,
            ledger_dir=self.ledger,
            run_id="9001",
            run_url="https://github.com/example/project/actions/runs/9001",
            now=NOW,
            env={},
        )
        with self.assertRaisesRegex(control.ManifestError, "does not match"):
            control.load_matching_reservation(
                self.plan,
                ledger_dir=self.ledger,
                run_id="9002",
            )


class ProviderTests(unittest.TestCase):
    def test_linkedin_forces_public_main_feed_payload(self):
        captured = []

        def opener(request, **kwargs):
            captured.append((request, kwargs))
            return FakeResponse(
                201,
                {},
                {"x-restli-id": "urn:li:share:123456789"},
            )

        result = control.publish_linkedin(
            "A" * 140,
            env={
                "LINKEDIN_ACCESS_TOKEN": "linkedin-super-secret",
                "LINKEDIN_AUTHOR_URN": "urn:li:person:abc123",
            },
            opener=opener,
        )
        request, kwargs = captured[0]
        payload = json.loads(request.data)
        self.assertEqual(payload["visibility"], "PUBLIC")
        self.assertEqual(payload["distribution"]["feedDistribution"], "MAIN_FEED")
        self.assertEqual(payload["lifecycleState"], "PUBLISHED")
        self.assertNotIn("linkedin-super-secret", request.data.decode())
        self.assertEqual(kwargs["timeout"], 30)
        self.assertEqual(result["post_id"], "urn:li:share:123456789")

    def test_x_uses_oauth1_and_minimal_top_level_post_payload(self):
        captured = []

        def opener(request, **kwargs):
            captured.append((request, kwargs))
            return FakeResponse(201, {"data": {"id": "1234567890", "text": "posted"}})

        env = {
            "X_API_KEY": "consumer-key",
            "X_API_SECRET": "consumer-secret",
            "X_ACCESS_TOKEN": "access-token",
            "X_ACCESS_TOKEN_SECRET": "access-secret",
        }
        result = control.publish_x(
            "A useful, source-grounded market update with a distinct takeaway.",
            env=env,
            opener=opener,
            timestamp=1234567890,
            nonce="fixed-nonce",
        )
        request, _kwargs = captured[0]
        self.assertEqual(json.loads(request.data), {"text": "A useful, source-grounded market update with a distinct takeaway."})
        authorization = request.get_header("Authorization")
        self.assertTrue(authorization.startswith("OAuth "))
        self.assertIn("oauth_signature=", authorization)
        self.assertNotIn("consumer-secret", authorization)
        self.assertNotIn("access-secret", authorization)
        self.assertEqual(result["url"], "https://x.com/i/web/status/1234567890")

    def test_provider_error_never_includes_response_body_or_secret(self):
        secret = "linkedin-super-secret"
        error = urllib.error.HTTPError(
            "https://api.linkedin.com/rest/posts",
            401,
            "unauthorized",
            {},
            io.BytesIO(f'{{"message":"token={secret}"}}'.encode()),
        )

        def opener(_request, **_kwargs):
            raise error

        with self.assertRaises(control.ProviderError) as raised:
            control.publish_linkedin(
                "A" * 140,
                env={
                    "LINKEDIN_ACCESS_TOKEN": secret,
                    "LINKEDIN_AUTHOR_URN": "urn:li:person:abc123",
                },
                opener=opener,
            )
        self.assertEqual(raised.exception.code, "invalid_credential")
        self.assertNotIn(secret, str(raised.exception))

    def test_oauth_signature_is_deterministic_for_fixed_inputs(self):
        first = control.oauth1_header(
            "POST",
            "https://api.x.com/2/tweets",
            consumer_key="key",
            consumer_secret="secret",
            access_token="token",
            access_token_secret="token-secret",
            timestamp=1234567890,
            nonce="nonce",
        )
        second = control.oauth1_header(
            "POST",
            "https://api.x.com/2/tweets",
            consumer_key="key",
            consumer_secret="secret",
            access_token="token",
            access_token_secret="token-secret",
            timestamp=1234567890,
            nonce="nonce",
        )
        self.assertEqual(first, second)


class PublishFlowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "videos").mkdir()
        (self.root / "videos" / "brief.mp4").write_bytes(b"video")
        self.manifest_path = self.root / "manifest.json"
        self.manifest_path.write_text(json.dumps(valid_manifest()), encoding="utf-8")
        self.plan = control.load_manifest(self.manifest_path, asset_root=self.root)
        self.ledger = self.root / "receipts"
        control.reserve(
            self.plan,
            ledger_dir=self.ledger,
            run_id="9001",
            run_url="https://github.com/example/project/actions/runs/9001",
            now=NOW,
            env={},
        )

    def tearDown(self):
        self.temporary.cleanup()

    @mock.patch("social_publish_control.publish_x")
    @mock.patch("social_publish_control.publish_linkedin")
    @mock.patch("social_publish_control._publish_youtube")
    def test_publish_order_and_youtube_url_template(self, youtube, linkedin, x):
        youtube.return_value = {
            "state": "published",
            "video_id": "video123",
            "url": "https://youtu.be/video123",
            "privacy_status": "private",
            "processing_status": "succeeded",
            "publish_at": "2026-09-01T04:00:00Z",
        }
        linkedin.return_value = {
            "state": "published",
            "post_id": "urn:li:share:1",
            "url": "https://www.linkedin.com/feed/update/urn:li:share:1/",
            "distribution": "MAIN_FEED",
        }
        x.return_value = {
            "state": "published",
            "post_id": "2",
            "url": "https://x.com/i/web/status/2",
        }
        private_path = self.root / "private-receipt.json"
        _path, receipt = control.publish_reserved(
            self.plan,
            asset_root=self.root,
            ledger_dir=self.ledger,
            run_id="9001",
            env={},
            now=NOW + timedelta(minutes=2),
            private_receipt_path=private_path,
        )
        self.assertEqual(receipt["state"], "published")
        self.assertIn("https://youtu.be/video123", linkedin.call_args.args[0])
        self.assertIn("https://youtu.be/video123", x.call_args.args[0])
        public_text = json.dumps(receipt)
        self.assertNotIn("video123", public_text)
        self.assertNotIn("urn:li:share:1", public_text)
        self.assertNotIn("x.com/i/web/status", public_text)
        private_receipt = json.loads(private_path.read_text(encoding="utf-8"))
        self.assertEqual(private_receipt["results"]["youtube"]["video_id"], "video123")
        self.assertEqual(private_receipt["results"]["linkedin"]["post_id"], "urn:li:share:1")
        self.assertEqual(private_receipt["results"]["x"]["post_id"], "2")

    @mock.patch("social_publish_control.publish_linkedin")
    @mock.patch("social_publish_control._publish_youtube")
    def test_partial_failure_is_persisted_and_not_retried_automatically(self, youtube, linkedin):
        youtube.return_value = {
            "state": "published",
            "video_id": "video123",
            "url": "https://youtu.be/video123",
        }
        linkedin.side_effect = control.ProviderError(
            "linkedin",
            "invalid_credential",
            "LinkedIn API returned invalid_credential",
        )
        with self.assertRaises(control.ProviderError):
            control.publish_reserved(
                self.plan,
                asset_root=self.root,
                ledger_dir=self.ledger,
                run_id="9001",
                env={},
                now=NOW + timedelta(minutes=2),
            )
        receipt = json.loads((self.ledger / f"{self.plan.content_id}.json").read_text())
        self.assertEqual(receipt["state"], "partial")
        self.assertEqual(receipt["failure"], {"platform": "linkedin", "code": "invalid_credential"})
        with self.assertRaisesRegex(control.ManifestError, "does not match"):
            control.load_matching_reservation(
                self.plan,
                ledger_dir=self.ledger,
                run_id="9001",
            )

    @mock.patch("social_publish_control._publish_youtube")
    def test_youtube_locator_survives_processing_failure(self, youtube):
        def uploaded_then_failed(_config, *, locator_callback, **_kwargs):
            locator_callback({
                "video_id": "Video_early_123",
                "publish_at": "2026-09-01T04:00:00Z",
            })
            raise control.ProviderError(
                "youtube",
                "processing_timeout",
                "YouTube API returned processing_timeout",
            )

        youtube.side_effect = uploaded_then_failed
        private_path = self.root / "private-receipt.json"
        with self.assertRaises(control.ProviderError):
            control.publish_reserved(
                self.plan,
                asset_root=self.root,
                ledger_dir=self.ledger,
                run_id="9001",
                env={},
                now=NOW + timedelta(minutes=2),
                private_receipt_path=private_path,
            )
        private_receipt = json.loads(private_path.read_text(encoding="utf-8"))
        self.assertEqual(private_receipt["state"], "partial")
        self.assertEqual(
            private_receipt["results"]["youtube"]["video_id"],
            "Video_early_123",
        )
        public_receipt = json.loads(
            (self.ledger / f"{self.plan.content_id}.json").read_text(encoding="utf-8")
        )
        self.assertEqual(public_receipt["state"], "failed")
        self.assertEqual(public_receipt["results"], {})


class SelectionAndCliTests(unittest.TestCase):
    def test_select_picks_one_due_approved_manifest(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outbox = root / "outbox"
            outbox.mkdir()
            ledger = root / "receipts"
            payload = valid_manifest()
            payload["platforms"]["youtube"]["enabled"] = False
            payload["platforms"]["linkedin"]["text"] = payload["platforms"]["linkedin"]["text"].replace(
                "{{YOUTUBE_URL}}",
                "{{SOURCE_URL}}",
            )
            payload["platforms"]["x"]["text"] = payload["platforms"]["x"]["text"].replace(
                "{{YOUTUBE_URL}}",
                "{{SOURCE_URL}}",
            )
            path = outbox / "one.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            selected = control.select_manifest(outbox, ledger_dir=ledger, now=NOW)
            self.assertEqual(selected, path)

    def test_unresolved_receipt_pauses_the_automatic_queue(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outbox = root / "outbox"
            outbox.mkdir()
            ledger = root / "receipts"
            ledger.mkdir()
            (ledger / "uncertain.json").write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "content_id": "uncertain-item",
                        "state": "partial",
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(control.ManifestError, "queue is paused"):
                control.select_manifest(outbox, ledger_dir=ledger, now=NOW)

    def test_reach_pause_file_pauses_the_automatic_queue(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outbox = root / "outbox"
            outbox.mkdir()
            ledger = root / "receipts"
            (root / "PAUSED.json").write_text("{}\n", encoding="utf-8")
            with self.assertRaisesRegex(control.ManifestError, "PAUSED.json"):
                control.select_manifest(outbox, ledger_dir=ledger, now=NOW)

    def test_cli_github_output_is_single_line_and_sanitized(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "videos").mkdir()
            (root / "videos" / "brief.mp4").write_bytes(b"video")
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps(valid_manifest()), encoding="utf-8")
            output = root / "github-output"
            json_output = root / "preview.json"
            result = control.run(
                [
                    "validate",
                    "--manifest",
                    str(manifest),
                    "--asset-root",
                    str(root),
                    "--require-media",
                    "--github-output",
                    str(output),
                    "--json-output",
                    str(json_output),
                ],
                env={"SECRET": "must-not-appear"},
            )
            self.assertEqual(result, 0)
            rendered = output.read_text() + json_output.read_text()
            self.assertNotIn("must-not-appear", rendered)
            self.assertNotIn("Three market", rendered)


if __name__ == "__main__":
    unittest.main()
