#!/usr/bin/env python3
"""Exercise every production usage path through initialization and collection.

No paid calls or GitHub access: execute the actual workflow shell blocks, with
runner temp paths containing spaces, symlinks and parent segments. The Actions
regression workflow separately uploads and downloads a synthetic fixture using
the same initializer to exercise the real artifact globber.
"""
from __future__ import annotations

import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch
import zipfile

from collect_deepseek_usage_artifacts import extract_events
from deepseek_usage import record_attempt
from summarize_deepseek_usage import summarize


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CONSUMERS = {
    ("ark-invest-feed-to-wechat.yml", "fetch-and-build"),
    ("consulting-latest-pdf-to-wechat.yml", "fetch-and-build"),
    ("institution-latest-pdf-to-wechat.yml", "fetch-and-build"),
    ("market-views-latex-pdf.yml", "build-market-views-pdf"),
    ("portal-translated-reports-test.yml", "build-portal-translated-reports"),
    ("dropbox-latest-pdf-to-xhs-sharded.yml", "select-macro-reports"),
    ("dropbox-latest-pdf-to-xhs-sharded.yml", "process-shard"),
    ("dropbox-latest-pdf-to-xhs-sharded.yml", "translate-report-shard"),
}


def usage_jobs():
    # All repository workflows use two-space job and six-space step indentation.
    # Inspect their real blocks instead of maintaining copies of shell snippets.
    for workflow in sorted((ROOT / ".github/workflows").glob("*.yml")):
        text = workflow.read_text()
        header, separator, body = text.partition("\njobs:\n")
        if not separator:
            continue
        for job in re.split(r"(?=^  [\w-]+:\n)", body, flags=re.M):
            if "name: deepseek-usage-" not in job:
                continue
            job_id = job.split(":", 1)[0].strip()
            before_steps, _, steps_text = job.partition("    steps:\n")
            steps = [s for s in re.split(r"(?=^      - )", steps_text, flags=re.M) if s.strip()]
            yield workflow.name, job_id, header + before_steps, steps


def shell(step):
    return textwrap.dedent(step.split("        run: |\n", 1)[1]).strip() + "\n"


class UsageWorkflowTests(unittest.TestCase):
    def test_all_instrumented_jobs_initialize_before_work_and_preserve_failure_ledgers(self):
        found = set()
        for filename, job_id, header, steps in usage_jobs():
            found.add((filename, job_id))
            with self.subTest(workflow=filename, job=job_id):
                # runner context is unavailable at both workflow and job env.
                self.assertNotRegex(header, r"DEEPSEEK_USAGE_DIR\s*:")
                self.assertIn("name: Initialize DeepSeek usage ledger", steps[0])
                self.assertIn("shell: bash", steps[0])
                summaries = [s for s in steps if "scripts/summarize_deepseek_usage.py \\" in s]
                uploads = [s for s in steps if "name: deepseek-usage-" in s]
                self.assertEqual(len(summaries), 1)
                self.assertEqual(len(uploads), 1)
                self.assertIn("always()", summaries[0])
                self.assertIn("always()", uploads[0])
                self.assertNotIn("continue-on-error", uploads[0])
                self.assertIn("uses: ./.github/actions/resilient-diagnostic-artifact", uploads[0])
                self.assertIn("hashFiles('.github/actions/resilient-diagnostic-artifact/action.yml')", uploads[0])
                self.assertIn("path: ${{ env.DEEPSEEK_USAGE_DIR }}", uploads[0])
                self.assertIn("${{ github.run_id }}", uploads[0])
                self.assertIn("${{ github.run_attempt }}", uploads[0])
                self.assertIn("retention-days: 30", uploads[0])
                self.assertIn("if-no-files-found: error", uploads[0])
                matrix = re.search(r"^      matrix:\n((?:        .*\n)+)", header, flags=re.M)
                if matrix:
                    for matrix_key in re.findall(r"^        ([\w_]+):", matrix[1], flags=re.M):
                        self.assertIn("${{ matrix." + matrix_key + " }}", uploads[0])
                for checkout in (s for s in steps if "uses: actions/checkout@" in s):
                    if "sparse-checkout:" in checkout:
                        self.assertRegex(checkout, r"(?m)^            \.github(?:/actions)?$")
        self.assertTrue(EXPECTED_CONSUMERS <= found, EXPECTED_CONSUMERS - found)

    def test_canonical_unique_paths_survive_checkout_cleanup_and_collect_real_events(self):
        for filename, job_id, _, steps in usage_jobs():
            with self.subTest(workflow=filename, job=job_id), tempfile.TemporaryDirectory() as temp:
                root = Path(temp).resolve()
                checkout = root / "checkout"
                checkout.mkdir()
                subprocess.run(["git", "init", "-q", str(checkout)], check=True)
                (checkout / "generated.txt").write_text("checkout reset removes this")
                runner_temp = root / "runner temp"
                (runner_temp / "child").mkdir(parents=True)
                (root / "temp-link").symlink_to(runner_temp, target_is_directory=True)
                env_file = root / "github-env"
                # setup-python provides `python` in Actions; use this interpreter
                # for the same shell command on systems with only `python3`.
                binaries = root / "bin"
                binaries.mkdir()
                (binaries / "python").symlink_to(sys.executable)
                environment = {
                    **os.environ,
                    "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
                    "RUNNER_TEMP": str(root / "temp-link" / "child") + "/..",
                    "GITHUB_ENV": str(env_file),
                    "GITHUB_STEP_SUMMARY": str(root / "step-summary"),
                }
                for _ in range(2):
                    subprocess.run(["bash", "-e", "-o", "pipefail", "-c", shell(steps[0])],
                                   env=environment, cwd=checkout, check=True)
                directories = [line.split("=", 1)[1] for line in env_file.read_text().splitlines()]
                self.assertEqual(len(directories), 2)
                self.assertNotEqual(*directories)
                for value in directories:
                    self.assertTrue(Path(value).is_dir())
                    self.assertEqual(value, str(Path(value).resolve()))
                    self.assertFalse({".", ".."} & set(value.split("/")))
                    self.assertEqual(Path(value).parent, runner_temp)
                ledger = Path(directories[0])
                environment["DEEPSEEK_USAGE_DIR"] = str(ledger)
                with patch.dict(os.environ, environment):
                    record_attempt(request_id="fixture", operation="test.workflow", model="test",
                                   attempt=1, retry_attempt=1, model_switches=0, key_index=1,
                                   elapsed_ms=0, transport_error=True)
                subprocess.run(["git", "clean", "-fdx"], cwd=checkout, check=True, capture_output=True)
                self.assertFalse((checkout / "generated.txt").exists())
                summary_step = next(s for s in steps if "scripts/summarize_deepseek_usage.py \\" in s)
                subprocess.run(["bash", "-e", "-o", "pipefail", "-c", shell(summary_step)],
                               env=environment, cwd=ROOT, check=True, capture_output=True)
                self.assertEqual(json.loads((ledger / "summary.json").read_text())["totals"]["http_attempts"], 1)
                self.assertTrue((ledger / "summary.md").is_file())
                payload = io.BytesIO()
                with zipfile.ZipFile(payload, "w") as archive:
                    for source in ledger.rglob("*"):
                        if source.is_file():
                            archive.write(source, source.relative_to(ledger))
                collected = root / "collected"
                collected.mkdir()
                self.assertEqual(extract_events(payload.getvalue(), collected), 1)
                self.assertEqual(summarize([collected])["totals"]["http_attempts"], 1)

    def test_regression_covers_workflow_edits_and_real_artifact_roundtrip(self):
        workflow = (ROOT / ".github/workflows/deepseek-usage-regression.yml").read_text()
        self.assertEqual(workflow.count("- '.github/workflows/*.yml'"), 2)
        self.assertIn("python scripts/test_deepseek_usage_workflows.py", workflow)
        self.assertIn("actions/upload-artifact@v4", workflow)
        self.assertIn("actions/download-artifact@v4", workflow)
        self.assertIn("if-no-files-found: error", workflow)
        self.assertNotIn("name: deepseek-usage-", workflow)
        self.assertIn('cmp "$DEEPSEEK_USAGE_DIR/fixture/path-check.json"', workflow)

    def test_exhausted_upload_retry_warns_without_blocking_article_delivery(self):
        action = (ROOT / ".github/actions/resilient-diagnostic-artifact/action.yml").read_text()
        self.assertEqual(action.count("uses: actions/upload-artifact@v4"), 2)
        self.assertIn("steps.primary.outcome == 'failure'", action)
        self.assertEqual(action.count("continue-on-error: true"), 2)
        result_script = textwrap.dedent(action.rsplit("      run: |\n", 1)[1])
        for primary, retry, uploaded in (("success", "skipped", True),
                                         ("failure", "success", True),
                                         ("failure", "failure", False)):
            with self.subTest(primary=primary, retry=retry), tempfile.TemporaryDirectory() as temp:
                output = Path(temp) / "output"
                result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", result_script],
                                        env={**os.environ, "PRIMARY_OUTCOME": primary,
                                             "RETRY_OUTCOME": retry, "ARTIFACT_NAME": "ledger",
                                             "GITHUB_OUTPUT": str(output)},
                                        check=True, capture_output=True, text=True)
                self.assertEqual(output.read_text().strip(), f"uploaded={str(uploaded).lower()}")
                self.assertEqual("::warning::" in result.stdout, not uploaded)


if __name__ == "__main__":
    unittest.main()
