#!/usr/bin/env python3
"""Completed source failures must not starve independently accepted originals."""
from contextlib import redirect_stdout, redirect_stderr
import copy
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import fetch_institution_latest_pdfs as fetcher
import institution_source_health as health


DATE = "261011"


def source_check(key="imf", status="error", new=0):
    return dict(institution=key, institution_en=fetcher.INSTITUTIONS[key]["name_en"],
                status=status, item_count=2, new_pdf_count=new, eligible_item_count=2,
                resolution_failure_count=2 if status == "error" else 1 if status == "degraded" else 0,
                deferred_retry_count=0, discovery_error=False,
                required_for_clean_zero=bool(fetcher.INSTITUTIONS[key].get("required_for_clean_zero")),
                error="private diagnostic material must not enter continuation outputs")


def manifest():
    return dict(date=DATE, generated_at="2026-10-11T02:00:00+00:00", since_days=7,
                institutions=["imf"], downloaded_count=0, dependency_held_count=0,
                skipped_count=0, source_checks=[source_check()], force_reprocess=False,
                downloaded=[], skipped=[])


class SourceHealthTests(unittest.TestCase):
    def classify(self, data=None, **kwargs):
        params = dict(producer_exit_code=2, log_exit_code=0, date_folder=DATE, institutions="imf")
        params.update(kwargs)
        return health.classify(data if data is not None else manifest(), **params)

    def test_exact_completed_source_failure_can_resume_but_stays_degraded(self):
        with patch.object(fetcher.requests, "Session", side_effect=AssertionError("no source HTTP")):
            result = self.classify()
        self.assertEqual(result, dict(source_health="degraded", source_health_required_failure_count="1",
                                     source_health_failed_institutions="imf", source_health_backlog_only="true"))
        self.assertNotIn("private", json.dumps(result))

    def test_healthy_zero_and_optional_source_failure_keep_producer_contract(self):
        data = manifest(); data["source_checks"] = [source_check(status="ok")]
        self.assertEqual(self.classify(data, producer_exit_code=0)["source_health"], "healthy")
        data["institutions"] = ["wto"]; data["source_checks"] = [source_check("wto")]
        self.assertEqual(self.classify(data, producer_exit_code=0, institutions="wto")["source_health"], "healthy")

    def test_required_empty_feed_can_resume_without_claiming_clean_zero(self):
        data = manifest(); check = data["source_checks"][0]
        check.update(status="empty", item_count=0, eligible_item_count=0, resolution_failure_count=0)
        self.assertEqual(self.classify(data)["source_health"], "degraded")

    def test_partial_downloads_keep_source_health_visible(self):
        data = manifest(); data["source_checks"] = [source_check(status="degraded", new=1)]
        data["downloaded"] = [dict(institution="imf")]; data["downloaded_count"] = 1
        result = self.classify(data, producer_exit_code=0)
        self.assertEqual((result["source_health"], result["source_health_backlog_only"]), ("degraded", "false"))

    def test_max_total_can_limit_successful_coverage_but_never_zero_coverage(self):
        data = manifest(); data["institutions"] = ["imf", "bis"]
        with self.assertRaises(health.InvalidSourceHealth):
            self.classify(data, institutions="imf,bis")
        data["source_checks"] = [source_check(status="ok", new=1)]
        data["downloaded"] = [dict(institution="imf")]; data["downloaded_count"] = 1
        self.assertEqual(self.classify(data, producer_exit_code=0, institutions="imf,bis")["source_health"], "healthy")

    def test_unknown_exit_or_failed_log_stops_even_with_known_manifest(self):
        for code in (1, 3, 75, 124, 130, 137, -1):
            with self.subTest(code=code), self.assertRaises(health.InvalidSourceHealth):
                self.classify(producer_exit_code=code)
        with self.assertRaises(health.InvalidSourceHealth):
            self.classify(log_exit_code=1)

    def test_exit_two_cannot_hide_success_or_wrong_failure_class(self):
        for status in ("ok", "empty"):
            data = manifest(); data["source_checks"] = [source_check("wto", status)]
            data["institutions"] = ["wto"]
            if status == "empty":
                data["source_checks"][0].update(item_count=0, eligible_item_count=0, resolution_failure_count=0)
            with self.subTest(status=status), self.assertRaises(health.InvalidSourceHealth):
                self.classify(data, institutions="wto")
        with self.assertRaises(health.InvalidSourceHealth):
            self.classify(producer_exit_code=0)

    def test_incomplete_inconsistent_or_modified_contract_stops(self):
        changes = (
            lambda x: x.pop("generated_at"),
            lambda x: x.update(date="261010"),
            lambda x: x.update(downloaded_count=1),
            lambda x: x.update(skipped_count=1),
            lambda x: x.update(dependency_held_count=1),
            lambda x: x.update(source_checks=[]),
            lambda x: x["source_checks"].append(copy.deepcopy(x["source_checks"][0])),
            lambda x: x["source_checks"][0].update(required_for_clean_zero=False),
            lambda x: x["source_checks"][0].update(required_for_clean_zero=1),
            lambda x: x["source_checks"][0].update(status="unknown"),
            lambda x: x["source_checks"][0].update(resolution_failure_count=3),
            lambda x: x["source_checks"][0].update(new_pdf_count=1),
            lambda x: x.update(generated_at="2026-10-11T02:00:00"),
            lambda x: x.update(institutions=["bis"]),
        )
        for i, change in enumerate(changes):
            data = manifest(); change(data)
            with self.subTest(case=i), self.assertRaises(health.InvalidSourceHealth):
                self.classify(data)

    def test_real_fetcher_released_pdf_403_manifest_has_known_health_exit(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            args = ["fetch", "--output-dir", str(root / "pdfs"), "--date", DATE,
                    "--institutions", "imf", "--seen-state-path", str(root / "seen.json"),
                    "--archive-path", str(root / "archive.jsonl")]
            item = dict(title="Released report", guid="released", source_url="https://example.org/released",
                        date=datetime.now(timezone.utc).isoformat(), pdf_candidates=["https://example.org/released.pdf"])
            with (patch.object(sys, "argv", args), patch.dict("os.environ", {"PROXY_SUBSCRIPTION_URL": "", "GITHUB_OUTPUT": "", "GITHUB_STEP_SUMMARY": ""}),
                  patch.object(fetcher, "collect_coveo_items", return_value=[item]),
                  patch.object(fetcher, "download_pdf", return_value=(None, "http_403")) as download,
                  redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO())):
                code = fetcher.main()
            self.assertEqual((code, download.call_count), (2, 1))
            data = json.loads((root / "pdfs/institution_run_manifest.json").read_text())
            with patch.object(fetcher, "download_pdf", side_effect=AssertionError("must not retry source")):
                self.assertEqual(self.classify(data, producer_exit_code=code)["source_health_backlog_only"], "true")
            self.assertNotIn("imf:released", json.loads((root / "seen.json").read_text())["items"])

    def test_pipeline_preserves_both_exit_codes_and_only_known_failure_continues(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); source = root / "manifest.json"; source.write_text(json.dumps(manifest()))
            output = root / "output.txt"
            args = [sys.executable, str(Path(health.__file__).resolve()), "--manifest", str(source),
                    "--date-folder", DATE, "--institutions", "imf", "--github-output", str(output)]
            for producer_code, tee_code, expected in ((2, 0, 0), (1, 0, 1), (2, 7, 1)):
                output.unlink(missing_ok=True)
                script = f'''set -e -o pipefail
set +e
(exit {producer_code}) | (cat >/dev/null; exit {tee_code})
institution_fetch_status=("${{PIPESTATUS[@]}}")
set -e
{shlex.join(args)} --producer-exit-code "${{institution_fetch_status[0]}}" --log-exit-code "${{institution_fetch_status[1]}}"
'''
                result = subprocess.run(["bash", "-c", script], capture_output=True, text=True)
                with self.subTest(producer=producer_code, log=tee_code):
                    self.assertEqual(result.returncode, expected, result.stderr)
                    self.assertEqual(output.exists(), expected == 0)
                    self.assertNotIn("private diagnostic", result.stdout + result.stderr)

    def test_missing_corrupt_or_symlinked_manifest_stops_without_outputs(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); source = root / "manifest.json"; output = root / "output"
            args = ["--manifest", str(source), "--producer-exit-code", "2", "--log-exit-code", "0",
                    "--date-folder", DATE, "--institutions", "imf", "--github-output", str(output)]
            for kind in ("missing", "corrupt", "symlink"):
                if kind == "corrupt": source.write_text("private truncated manifest {")
                if kind == "symlink":
                    source.unlink(); target = root / "target.json"; target.write_text(json.dumps(manifest())); source.symlink_to(target)
                with self.subTest(kind=kind), redirect_stderr(io.StringIO()) as stderr:
                    self.assertEqual(health.main(args), 1)
                self.assertFalse(output.exists()); self.assertNotIn("private", stderr.getvalue())

    def test_source_health_job_is_visible_but_not_an_upload_dependency(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/institution-latest-pdf-to-wechat.yml").read_text()
        source_job = workflow.split("\n  source-health:\n", 1)[1].split("\n  upload-wechat-drafts:\n", 1)[0]
        upload_job = workflow.split("\n  upload-wechat-drafts:\n", 1)[1].split("\n  cleanup-private-handoff:\n", 1)[0]
        notification = workflow.split("\n  notify-failure:\n", 1)[1]
        self.assertIn("source_health == 'degraded'", source_job)
        self.assertIn("exit 1", source_job)
        self.assertIn("needs: fetch-and-build\n", upload_job)
        self.assertNotIn("source-health", upload_job)
        self.assertIn("needs: [fetch-and-build, source-health, upload-wechat-drafts, cleanup-private-handoff]", notification)
        self.assertIn('institution_fetch_status=("${PIPESTATUS[@]}")\n          set -e', workflow)
        self.assertNotIn("continue-on-error", workflow.split("      - name: Fetch latest institution PDFs\n", 1)[1].split("      - name: Extract MinerU", 1)[0])


if __name__ == "__main__":
    unittest.main()
