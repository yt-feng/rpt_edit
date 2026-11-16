#!/usr/bin/env python3
"""Exercise every production usage path through initialization and collection.

No paid calls or GitHub access: execute the actual workflow shell blocks, with
runner temp paths containing spaces, symlinks and parent segments. The Actions
regression workflow separately uploads and downloads a synthetic fixture using
the same initializer to exercise the real artifact globber.
"""
from __future__ import annotations

import io
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import MagicMock, patch
import zipfile

from collect_deepseek_usage_artifacts import extract_events
from deepseek_usage import record_attempt
from summarize_deepseek_usage import summarize
from verify_uploaded_usage_fixture import verify
import verify_uploaded_usage_fixture as uploaded_fixture


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
        self.assertNotIn("actions/download-artifact@v4", workflow)
        self.assertIn("steps.fixture_upload.outputs.artifact-id", workflow)
        self.assertIn("steps.fixture_upload.outputs.artifact-digest", workflow)
        self.assertIn("if-no-files-found: error", workflow)
        self.assertNotIn("name: deepseek-usage-", workflow)
        self.assertIn('python scripts/verify_uploaded_usage_fixture.py', workflow)

    def test_exact_uploaded_archive_rejects_different_bytes_or_fixture(self):
        fixture = b'{"kind":"artifact-path-smoke"}\n'
        raw = io.BytesIO()
        with zipfile.ZipFile(raw, 'w') as archive:
            archive.writestr('fixture/path-check.json', fixture)
            archive.writestr('../../unrelated', b'never extracted')
        payload = raw.getvalue()
        checksum = hashlib.sha256(payload).hexdigest()
        verify(payload, checksum, fixture)
        with self.assertRaisesRegex(ValueError, 'checksum mismatch'):
            verify(payload + b'changed', checksum, fixture)
        with self.assertRaisesRegex(ValueError, 'contents changed'):
            verify(payload, checksum, b'wrong fixture')

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


class UploadedFixtureReadTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        self.fixture = b'{"kind":"artifact-path-smoke"}\n'
        path = directory / uploaded_fixture.MEMBER
        path.parent.mkdir(); path.write_bytes(self.fixture)
        archive = io.BytesIO()
        with zipfile.ZipFile(archive, 'w') as writer:
            writer.writestr(uploaded_fixture.MEMBER, self.fixture)
        self.payload = archive.getvalue()
        self.session = MagicMock()
        self.session.__enter__.return_value = self.session
        self.clock = 0
        self.sleep = MagicMock(side_effect=self.advance)
        self.stderr = io.StringIO()
        for mocked in (
            patch.object(uploaded_fixture.requests, 'Session', return_value=self.session),
            patch.object(uploaded_fixture.time, 'monotonic', side_effect=lambda: self.clock),
            patch.object(uploaded_fixture.time, 'sleep', self.sleep),
            patch('sys.stderr', self.stderr),
            patch('sys.stdout', io.StringIO()),
            patch.dict(os.environ, {'GITHUB_REPOSITORY': 'owner/repo', 'UPLOADED_ARTIFACT_ID': '123',
                                    'GH_TOKEN': 'private-token', 'DEEPSEEK_USAGE_DIR': str(directory),
                                    'UPLOADED_ARTIFACT_SHA256': hashlib.sha256(self.payload).hexdigest()}),
        ):
            mocked.start(); self.addCleanup(mocked.stop)

    def advance(self, seconds):
        self.clock += seconds

    def response(self, status=200, *, chunks=None, headers=None):
        result = MagicMock(status_code=status, headers=headers or {})
        result.__enter__.return_value = result
        result.raw.read1.side_effect = [self.payload, b''] if chunks is None else chunks
        return result

    def test_just_uploaded_404_and_transient_service_error_retry_only_the_exact_id(self):
        responses = [self.response(404), self.response(503), self.response()]
        self.session.get.side_effect = responses
        self.assertEqual(uploaded_fixture.main(), 0)
        self.assertEqual([call.args[0] for call in self.session.get.call_args_list],
                         ['https://api.github.com/repos/owner/repo/actions/artifacts/123/zip'] * 3)
        self.assertEqual([call.args[0] for call in self.sleep.call_args_list], [1, 2])
        self.assertEqual(self.session.max_redirects, 3)
        self.assertTrue(all(response.__exit__.call_count == 1 for response in responses))
        self.assertNotIn('private-token', self.stderr.getvalue())

    def test_transient_connection_and_interrupted_body_restart_before_exact_hash_check(self):
        self.session.get.side_effect = [
            uploaded_fixture.requests.exceptions.ConnectTimeout('https://signed.invalid/?secret=private-token'),
            self.response(chunks=[b'partial', uploaded_fixture.ProtocolError('private-token')]),
            self.response(),
        ]
        self.assertEqual(uploaded_fixture.main(), 0)
        self.assertEqual(self.session.get.call_count, 3)
        self.assertEqual(self.sleep.call_count, 2)
        self.assertNotIn('private-token', self.stderr.getvalue())
        self.assertNotIn('https://', self.stderr.getvalue())

    def test_permanent_status_certificate_oversize_and_integrity_fail_without_retry(self):
        outcomes = [*(self.response(code) for code in (400, 401, 403, 422)),
                    uploaded_fixture.requests.exceptions.SSLError('https://signed.invalid/?secret=private-token'),
                    self.response(headers={'Content-Length': str(uploaded_fixture.MAX_ARCHIVE + 1)}),
                    self.response(chunks=[b'x' * (uploaded_fixture.MAX_ARCHIVE + 1)]),
                    self.response(chunks=[b'wrong bytes', b''])]
        for outcome in outcomes:
            with self.subTest(outcome=type(outcome).__name__):
                self.session.get.reset_mock(); self.sleep.reset_mock()
                self.session.get.side_effect = [outcome]
                with self.assertRaises(ValueError) as raised:
                    uploaded_fixture.main()
                self.assertEqual(self.session.get.call_count, 1)
                self.sleep.assert_not_called()
                self.assertNotIn('private-token', str(raised.exception))
                self.assertNotIn('https://', str(raised.exception))

    def test_unavailable_exact_id_exhausts_five_attempts_without_unbounded_polling(self):
        self.session.get.side_effect = [self.response(404) for _ in range(5)]
        with self.assertRaisesRegex(RuntimeError, 'failed after 5 attempts: HTTP 404'):
            uploaded_fixture.main()
        self.assertEqual(self.session.get.call_count, 5)
        self.assertEqual([call.args[0] for call in self.sleep.call_args_list], [1, 2, 4, 8])
        self.assertLess(self.clock, 55)

    def test_remaining_budget_reduces_request_timeouts_and_prevents_another_retry(self):
        def request(*args, **kwargs):
            self.advance(30 if self.session.get.call_count == 1 else 14)
            return self.response(429)
        self.session.get.side_effect = request
        with self.assertRaisesRegex(RuntimeError, 'elapsed budget'):
            uploaded_fixture.main()
        self.assertEqual(self.session.get.call_count, 2)
        self.assertEqual(self.session.get.call_args_list[1].kwargs['timeout'], (1.75, 1.75))
        self.assertEqual([call.args[0] for call in self.sleep.call_args_list], [1])
        self.assertEqual(self.clock, 45)

    def test_slow_body_obeys_elapsed_budget_between_available_chunks(self):
        response = self.response()
        def read(*args, **kwargs):
            self.advance(1)
            return b'x'
        response.raw.read1.side_effect = read
        self.session.get.side_effect = [response]
        with self.assertRaisesRegex(RuntimeError, 'elapsed budget'):
            uploaded_fixture.main()
        self.assertEqual(self.clock, 45)
        self.assertEqual(self.session.get.call_count, 1)
        self.sleep.assert_not_called()

    def test_invalid_identity_or_checksum_cannot_make_a_request(self):
        for variable, value in (('UPLOADED_ARTIFACT_ID', '../123'), ('UPLOADED_ARTIFACT_SHA256', 'bad')):
            with self.subTest(variable=variable), patch.dict(os.environ, {variable: value}):
                with self.assertRaises(ValueError):
                    uploaded_fixture.main()
        self.session.get.assert_not_called()

    def test_older_urllib3_stream_without_read1_keeps_a_bounded_read(self):
        response = self.response()
        response.raw.read1 = None
        response.raw.read.side_effect = [self.payload[index:index + 1] for index in range(len(self.payload))] + [b'']
        self.session.get.side_effect = [response]
        self.assertEqual(uploaded_fixture.main(), 0)
        self.assertTrue(all(call.args == (1,) for call in response.raw.read.call_args_list))
        self.sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
