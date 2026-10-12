"""Offline integration for live IMF delivery, durable intake and existing holds."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import fetch_institution_latest_pdfs as fetcher
import institution_source_health as health


NOW = datetime(2026, 10, 13, tzinfo=timezone.utc)
SOURCE = dict(title="Test publication", guid="stable-source", date=NOW.isoformat(),
              source_url="https://www.imf.org/en/publications/tar/issues/2026/10/12/test-report",
              scrape_url="", coveo_unique_id="exact-indexed-publication", pdf_candidates=[])
PDF_URL = "https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf"


class LiveIntakeTests(unittest.TestCase):
    def invoke(self, root, browser, *, resolution_error=None, held=False):
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None): return NOW
        argv = ["fetch", "--institutions", "imf", "--output-dir", str(root / "pdfs"),
                "--seen-state-path", str(root / "seen.json"), "--archive-path", str(root / "archive.jsonl"),
                "--pending-intake-path", str(root / "pending.json")]
        with (patch.object(fetcher.sys, "argv", argv), patch.object(fetcher, "datetime", Clock),
              patch.object(fetcher, "collect_coveo_items", return_value=[copy.deepcopy(SOURCE)]),
              patch.object(fetcher, "resolve_imf_browser_publication", return_value={"source_guid": SOURCE["guid"]},
                           side_effect=resolution_error) as resolve,
              patch.object(fetcher, "matches_dependency_hold", return_value=held),
              patch.object(fetcher, "collect_coveo_preview_candidates", return_value=[]),
              patch.object(fetcher, "download_pdf", side_effect=AssertionError("No ordinary PDF candidates")),
              patch.object(fetcher, "resolve_working_proxy", side_effect=AssertionError("Browser route has its own source check")),
              patch.object(fetcher, "write_github_output"), patch.object(fetcher, "write_source_health_summary")):
            code = fetcher._main(browser)
        manifest = json.loads((root / "pdfs/institution_run_manifest.json").read_text())
        return code, manifest, resolve.call_count

    def test_live_route_runs_without_legacy_candidates_and_deduplicates_after_seen(self):
        pdf = b"%PDF-fixture"
        proof = dict(schema=1, source_guid=SOURCE["guid"], source_url=SOURCE["source_url"],
                     landing_url="https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml",
                     pdf_url=PDF_URL, doi="10.5089/9780000000002.019", title=SOURCE["title"],
                     identity_sha256="1" * 64, crossref_sha256="2" * 64,
                     sha256=hashlib.sha256(pdf).hexdigest(), bytes=len(pdf), pages=14,
                     landing_status=200, pdf_status=200, source_identity_verified=True,
                     transport="existing_subscription_vless_browser")
        def download(publication, dest, max_bytes):
            self.assertEqual(publication["source_guid"], SOURCE["guid"])
            dest.write_bytes(pdf)
            return proof
        browser = SimpleNamespace(enabled=True, download=Mock(side_effect=download))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            code, manifest, calls = self.invoke(root, browser)
            self.assertEqual((code, calls, manifest["downloaded_count"]), (0, 1, 1))
            row = manifest["downloaded"][0]
            self.assertEqual(row["imf_live_download"], proof)
            self.assertEqual(row["sha256"], proof["sha256"])
            self.assertEqual(manifest["source_checks"][0]["status"], "ok")
            self.assertEqual(health.classify(manifest, producer_exit_code=code, log_exit_code=0,
                                            date_folder=manifest["date"], institutions="imf"),
                             dict(source_health="healthy", source_health_required_failure_count="0",
                                  source_health_failed_institutions="", source_health_backlog_only="false"))
            self.assertIn("imf:stable-source", json.loads((root / "pending.json").read_text())["items"])
            # The normal durable seen state, not a transient PDF, retires intake.
            code, manifest, calls = self.invoke(root, browser)
            self.assertEqual((code, calls, manifest["downloaded_count"]), (0, 0, 0))
            self.assertEqual(json.loads((root / "pending.json").read_text())["items"], {})
            browser.download.assert_called_once()

    def test_rejected_source_stays_queued_and_is_never_marked_downloaded(self):
        browser = SimpleNamespace(enabled=True, download=Mock())
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            code, manifest, calls = self.invoke(root, browser, resolution_error=ValueError("fixture mismatch"))
            self.assertEqual((code, calls, manifest["downloaded_count"]), (2, 1, 0))
            self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 1)
            self.assertEqual(json.loads((root / "seen.json").read_text())["items"], {})
            self.assertIn("imf:stable-source", json.loads((root / "pending.json").read_text())["items"])
            browser.download.assert_not_called()

    def test_existing_dependency_hold_is_checked_before_new_live_route(self):
        browser = SimpleNamespace(enabled=True, download=Mock())
        with tempfile.TemporaryDirectory() as directory:
            code, manifest, calls = self.invoke(Path(directory), browser, held=True)
            self.assertEqual((code, calls, manifest["downloaded_count"]), (0, 0, 0))
            self.assertEqual(manifest["dependency_held_count"], 1)
            browser.download.assert_not_called()


if __name__ == "__main__":
    unittest.main()
