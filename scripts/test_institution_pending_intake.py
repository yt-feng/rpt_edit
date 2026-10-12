"""Known failed sources survive recency windows and failed downstream handoffs."""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import fetch_institution_latest_pdfs as fetcher
import institution_source_health as health
from institution_pending_intake import PendingIntake


NOW = datetime(2026, 10, 12, 1, tzinfo=timezone.utc)


def item(number=1, *, days=0):
    return dict(title=f"Observed report {number}", guid=f"coveo-{number}",
                date=(NOW - timedelta(days=days)).isoformat(),
                source_url=f"https://www.imf.org/en/publications/wp/issues/2026/10/12/report-{number}",
                scrape_url="", coveo_unique_id="",
                pdf_candidates=[f"https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026{number:03d}.pdf"])


class IntakeTests(unittest.TestCase):
    def run_fetch(self, path, sources, *, now=NOW, success=False, retries=10, discovery_error=None, held=False):
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None): return now
        argv = ["fetcher", "--institutions", "imf", "--output-dir", str(path / "pdfs"),
                "--seen-state-path", str(path / "seen.json"), "--archive-path", str(path / "archive.jsonl"),
                "--pending-intake-path", str(path / "pending/imf.json"),
                "--imf-pending-retries", str(retries), "--since-days", "7"]
        calls = []
        def download(session, candidates, destination, *args, **kwargs):
            calls.append(candidates)
            if not success: return None, "http_403"
            destination.write_bytes(b"%PDF-1.7 observed original")
            return candidates[0], "ok"
        with (patch.object(fetcher.sys, "argv", argv), patch.object(fetcher, "datetime", Clock),
              patch.dict(fetcher.os.environ, {"PROXY_SUBSCRIPTION_URL": ""}),
              patch.object(fetcher, "collect_coveo_items", return_value=copy.deepcopy(sources), side_effect=discovery_error),
              patch.object(fetcher, "matches_dependency_hold", side_effect=lambda versions, name, record, *args: held and record["guid"] == "coveo-1"),
              patch.object(fetcher, "download_pdf", side_effect=download),
              patch.object(fetcher, "http_get", side_effect=AssertionError("unexpected live request")),
              patch.object(fetcher, "write_github_output"), patch.object(fetcher, "write_source_health_summary")):
            code = fetcher.main()
        manifest = json.loads((path / "pdfs/institution_run_manifest.json").read_text())
        classified = health.classify(manifest, producer_exit_code=code, log_exit_code=0,
                                    date_folder=now.strftime("%y%m%d"), institutions="imf")
        return code, calls, manifest, classified

    def test_aged_source_retries_without_feed_and_retires_only_after_durable_seen(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            code, calls, _, classified = self.run_fetch(path, [item()])
            self.assertEqual((code, len(calls), classified["source_health"]), (2, 1, "degraded"))
            durable_seen = (path / "seen.json").read_text()
            queued = json.loads((path / "pending/imf.json").read_text())
            self.assertEqual(queued["items"]["imf:coveo-1"]["item"], item())
            code, calls, manifest, _ = self.run_fetch(path, [], now=NOW + timedelta(days=10), success=True)
            self.assertEqual((code, len(calls), manifest["downloaded_count"]), (0, 1, 1))
            self.assertEqual(manifest["downloaded"][0]["published"], item()["date"])
            # Translation/handoff fails: its provisional seen-state is not durable.
            (path / "seen.json").write_text(durable_seen)
            code, calls, _, _ = self.run_fetch(path, [], now=NOW + timedelta(days=11), success=True)
            self.assertEqual((code, len(calls)), (0, 1))
            # Now handoff and ordinary seen-state commit succeed. The next run
            # retires the queue and cannot download the source a second time.
            code, calls, _, _ = self.run_fetch(path, [item()], now=NOW + timedelta(days=12), success=True)
            self.assertEqual((code, calls), (0, []))
            self.assertEqual(json.loads((path / "pending/imf.json").read_text())["items"], {})
            self.assertEqual(json.loads((path / "seen.json").read_text())["items"]["imf:coveo-1"]["status"], "downloaded")

    def test_unobserved_historical_source_is_not_backfilled(self):
        with tempfile.TemporaryDirectory() as directory:
            code, calls, manifest, _ = self.run_fetch(Path(directory), [item(days=8)])
            self.assertEqual((code, calls, manifest["downloaded_count"]), (0, [], 0))
            self.assertEqual(json.loads((Path(directory) / "pending/imf.json").read_text())["items"], {})

    def test_bound_rotates_failed_retries_and_preserves_original_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            self.run_fetch(path, [item(1), item(2), item(3)])
            changed = item(1); changed["title"] = "Changed title"; changed["date"] = (NOW + timedelta(days=9)).isoformat()
            _, calls, manifest, classified = self.run_fetch(path, [changed, item(2), item(3)],
                                                           now=NOW + timedelta(days=10), retries=1)
            self.assertEqual(calls, [item(1)["pdf_candidates"]])
            self.assertEqual(manifest["source_checks"][0]["deferred_retry_count"], 2)
            self.assertEqual(classified["source_health"], "degraded")
            self.assertEqual(json.loads((path / "pending/imf.json").read_text())["items"]["imf:coveo-1"]["item"], item(1))
            _, calls, _, _ = self.run_fetch(path, [], now=NOW + timedelta(days=11), retries=1)
            self.assertEqual(calls, [item(2)["pdf_candidates"]])

    def test_successful_bounded_batch_cannot_hide_deferred_intake(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory); self.run_fetch(path, [item(1), item(2)])
            code, calls, manifest, classified = self.run_fetch(path, [], now=NOW + timedelta(days=10), retries=1, success=True)
            self.assertEqual((code, len(calls), classified["source_health"]), (0, 1, "degraded"))
            check = manifest["source_checks"][0]
            self.assertEqual((check["resolution_failure_count"], check["deferred_retry_count"]), (0, 1))

    def test_official_direct_pdf_is_supported_but_unknown_date_is_visible_failure(self):
        direct = item(); direct["source_url"] = direct["pdf_candidates"][0]
        with tempfile.TemporaryDirectory() as directory:
            code, calls, _, _ = self.run_fetch(Path(directory), [direct], success=True)
            self.assertEqual((code, len(calls)), (0, 1))
        unknown = item(); unknown["date"] = ""
        with tempfile.TemporaryDirectory() as directory:
            code, calls, manifest, _ = self.run_fetch(Path(directory), [unknown])
            self.assertEqual((code, calls), (2, []))
            self.assertEqual(manifest["skipped"][0]["reason"], "invalid_intake_metadata")

    def test_feed_outage_still_retries_known_sources_without_claiming_healthy_intake(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory); self.run_fetch(path, [item()])
            code, calls, manifest, classified = self.run_fetch(path, [], now=NOW + timedelta(days=10),
                                                              success=True, discovery_error=RuntimeError("offline"))
            self.assertEqual((code, len(calls), classified["source_health"]), (0, 1, "degraded"))
            self.assertTrue(manifest["source_checks"][0]["discovery_error"])

    def test_held_oldest_item_rotates_without_starving_unresolved_sibling(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory); self.run_fetch(path, [item(1), item(2)])
            code, calls, manifest, _ = self.run_fetch(path, [], now=NOW + timedelta(days=10), retries=1, held=True)
            self.assertEqual(calls, [])
            self.assertEqual(manifest["source_checks"][0]["deferred_retry_count"], 1)
            _, calls, _, _ = self.run_fetch(path, [], now=NOW + timedelta(days=11), retries=1, held=True)
            self.assertEqual(calls, [item(2)["pdf_candidates"]])
            self.assertIn("imf:coveo-1", json.loads((path / "pending/imf.json").read_text())["items"])

    def test_checkpoint_rejects_unknown_types_paths_and_historical_admission(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "queue.json"
            pending = PendingIntake(path, {}, now=NOW); pending.admit(item(), 7)
            valid = json.loads(path.read_text())
            mutations = [
                lambda data: data.update(institution="bis"),
                lambda data: data["items"]["imf:coveo-1"]["item"].update(source_url="https://www.imf.org/en/publications/weo"),
                lambda data: data["items"]["imf:coveo-1"]["item"].update(source_url="https://evil.example/en/publications/report"),
                lambda data: data["items"]["imf:coveo-1"]["item"].update(source_url="https://www.imf.org/private/report"),
                lambda data: data["items"]["imf:coveo-1"]["item"].update(pdf_candidates=["https://www.imf.org@evil.example/report.pdf"]),
                lambda data: data["items"]["imf:coveo-1"]["item"].update(date=(NOW-timedelta(days=8)).isoformat()),
                lambda data: data["items"]["imf:coveo-1"].update(attempts=True),
            ]
            for mutate in mutations:
                data = copy.deepcopy(valid); mutate(data); path.write_text(json.dumps(data))
                with self.assertRaises(ValueError): PendingIntake(path, {}, now=NOW)

    def test_weo_collection_is_excluded_but_dated_future_issue_stays_pending(self):
        future = item(); future["title"] = "World Economic Outlook October 2026"
        future["date"] = (NOW + timedelta(days=1)).isoformat()
        future["source_url"] = "https://www.imf.org/en/publications/weo/issues/2026/10/13/world-economic-outlook-october-2026"
        with tempfile.TemporaryDirectory() as directory:
            code, calls, manifest, _ = self.run_fetch(Path(directory), [future])
            self.assertEqual((code, calls, manifest["skipped"][0]["reason"]), (0, [], "publication_pending"))
            self.assertEqual(json.loads((Path(directory) / "pending/imf.json").read_text())["items"], {})
        class Response:
            def raise_for_status(self): pass
            def json(self):
                urls = ["https://www.imf.org/en/publications/weo", "https://www.imf.org/en/Publications/WEO/",
                        "https://www.imf.org/en/publications/weo/?year=2026", future["source_url"]]
                return {"results": [{"title": "WEO", "raw": {"clickableuri": url, "permanentid": url}}
                                    for url in urls]}
        with patch.object(fetcher, "http_post", return_value=Response()):
            discovered = fetcher.collect_coveo_items(fetcher.INSTITUTIONS["imf"], object(), 10, 60)
        self.assertEqual([record["source_url"] for record in discovered], [future["source_url"]])

    def test_discovery_is_saved_before_download_exception(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pending.json"
            PendingIntake(path, {}, now=NOW).admit(item(), 7)
            # A process/downstream exception needs no later save to retain it.
            self.assertIn("imf:coveo-1", PendingIntake(path, {}, now=NOW).items)

    def test_workflow_checkpoints_only_pending_before_translation_and_requires_push(self):
        workflow = (Path(__file__).parents[1] / ".github/workflows/institution-latest-pdf-to-wechat.yml").read_text()
        start = workflow.index("      - name: Persist pending IMF intake")
        end = workflow.index("      - name: Extract MinerU", start)
        step = workflow[start:end]
        self.assertIn('"institution_feeds/pending_intake/imf.json" "Checkpoint unresolved IMF intake" 8 true', step)
        self.assertNotIn('"institution_feeds"', step)
        self.assertIn("always()", step)
        self.assertLess(end, workflow.index("      - name: Build Portal translated report PDFs"))
        self.assertIn('"Update institution PDF link archive" 8 true', workflow)


if __name__ == "__main__": unittest.main()
