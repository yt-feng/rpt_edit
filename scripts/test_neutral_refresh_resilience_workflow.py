#!/usr/bin/env python3
"""Replay optional refresh persistence without Actions services or credentials."""
from __future__ import annotations

import gzip
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest

from build_portal_locales import empty_cache
from offline_translation import MODEL_ID, PROVIDER


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/neutral-edge-cutover.yml"
COMPOSITE = ROOT / ".github/actions/resilient-diagnostic-artifact/action.yml"


PYTHON_STUB = """import json, os, pathlib, shutil, sys
args = sys.argv[1:]
script = next((value for value in args if value.endswith('.py')), '')
if script in {'scripts/fetch_release_asset.py', 'scripts/translate_portal_titles.py'}:
    record = {'script': script, 'args': args}
    if script.endswith('fetch_release_asset.py'):
        status = os.environ.get('STUB_FETCH_STATUS', '200')
        if status == '200':
            target = pathlib.Path(args[args.index('--output') + 1])
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(os.environ['STUB_FETCH_BODY'], target)
        with open(os.environ['STUB_CALLS'], 'a') as output:
            output.write(json.dumps(record) + '\\n')
        print(status)
        sys.exit(int(os.environ.get('STUB_FETCH_EXIT', '0')))
    target = pathlib.Path(args[args.index('--cache-path') + 1])
    record['existing_cache'] = target.exists()
    with open(os.environ['STUB_CALLS'], 'a') as output:
        output.write(json.dumps(record) + '\\n')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(os.environ['STUB_TITLE_BODY'], target)
    sys.exit(0)
os.execv(os.environ['STUB_REAL_PYTHON'], [os.environ['STUB_REAL_PYTHON'], *args])
"""


def step_block(name: str, source: str | None = None) -> str:
    source = WORKFLOW.read_text(encoding="utf-8") if source is None else source
    match = re.search(rf"(?m)^( +)- name: {re.escape(name)}\s*$", source)
    if match is None:
        raise AssertionError(f"Missing step: {name}")
    rest = source[match.end():]
    boundary = re.search(rf"(?m)^ {{0,{len(match.group(1))}}}(?:- |[A-Za-z_]\w*:)", rest)
    return rest[:boundary.start()] if boundary else rest


def step_script(name: str, source: str | None = None) -> str:
    block = step_block(name, source)
    return textwrap.dedent(block.split("run: |\n", 1)[1])


class OptionalArtifactTests(unittest.TestCase):
    def test_diagnostics_use_bounded_optional_upload_but_release_identity_remains_required(self):
        for name in ("Preserve translation diagnostics even on failure",
                     "Preserve public chart acceptance evidence"):
            with self.subTest(step=name):
                block = step_block(name)
                self.assertIn("uses: ./.github/actions/resilient-diagnostic-artifact", block)
                self.assertNotIn('required: "true"', block)
                self.assertIn("if: always()", block)
        mandatory = step_block("Upload release validation artifact")
        self.assertIn("uses: actions/upload-artifact@v4", mandatory)
        self.assertIn("if-no-files-found: error", mandatory)
        self.assertNotIn("continue-on-error", mandatory)

    def test_actual_diagnostic_result_preserves_primary_result_after_two_failures(self):
        source = COMPOSITE.read_text(encoding="utf-8")
        for name in ("Upload diagnostic artifact", "Retry diagnostic artifact upload"):
            self.assertIn("continue-on-error: true", step_block(name, source))
        self.assertIn("steps.primary.outcome == 'failure'", step_block("Retry diagnostic artifact upload", source))
        script = step_script("Report diagnostic artifact result", source)
        for required, primary, retry, artifact_id, expected_success in (
            ("false", "failure", "failure", "", True),
            ("false", "failure", "success", "456", True),
            ("true", "failure", "failure", "", False),
            ("true", "failure", "success", "456", True),
        ):
            with self.subTest(required=required, primary=primary, retry=retry), tempfile.TemporaryDirectory() as temporary:
                output = Path(temporary) / "output"
                result = subprocess.run(["bash", "-euo", "pipefail", "-c", script],
                    env={**os.environ, "GITHUB_OUTPUT": str(output), "PRIMARY_OUTCOME": primary,
                         "RETRY_OUTCOME": retry, "ARTIFACT_NAME": "test-evidence", "REQUIRED": required,
                         "PRIMARY_ARTIFACT_ID": "", "RETRY_ARTIFACT_ID": artifact_id},
                    capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, expected_success, result.stderr)
                self.assertEqual(output.read_text(), "uploaded=" + ("true" if retry == "success" else "false") + "\n")
                if required == "false" and retry == "failure":
                    self.assertIn("::warning::", result.stdout)
                elif required == "true" and retry == "failure":
                    self.assertIn("::error::", result.stdout)


class CheckpointWorkflowTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "scripts").symlink_to(ROOT / "scripts", target_is_directory=True)
        self.runner = self.root / "runner"
        self.runner.mkdir()
        self.output = self.root / "output"
        self.summary = self.root / "summary"
        self.calls_path = self.root / "calls.jsonl"
        self.cache = self.runner / "portal-locale-cache/cache-v1.json.gz"
        self.built = self.root / "_neutral_site/data/i18n/cache-v1.json.gz"
        self.title = self.runner / "portal-title-cache/cache-v1.json"
        self.valid_locale = gzip.compress(json.dumps(empty_cache(MODEL_ID, provider="hymt")).encode(), mtime=0)
        self.valid_title = json.dumps({"schema_version": 1, "provider": PROVIDER, "entries": {}}).encode()
        self.fetch_body = self.root / "fetch-body"
        self.fetch_body.write_bytes(self.valid_locale)
        self.title_body = self.root / "title-body"
        self.title_body.write_bytes(self.valid_title)
        bindir = self.root / "bin"
        bindir.mkdir()
        shim = bindir / "python3"
        shim.write_text(f"#!{sys.executable}\n" + PYTHON_STUB, encoding="utf-8")
        shim.chmod(0o755)
        self.env = {**os.environ, "PATH": str(bindir) + os.pathsep + os.environ.get("PATH", ""),
                    "RUNNER_TEMP": str(self.runner), "GITHUB_OUTPUT": str(self.output),
                    "GITHUB_STEP_SUMMARY": str(self.summary), "LIVE_ORIGIN": "https://example.invalid",
                    "PREVIOUS_STATIC_RELEASE": "a" * 32, "STUB_REAL_PYTHON": sys.executable,
                    "STUB_CALLS": str(self.calls_path), "STUB_FETCH_BODY": str(self.fetch_body),
                    "STUB_TITLE_BODY": str(self.title_body)}

    @staticmethod
    def write(path: Path, body: bytes):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)

    def run_step(self, name: str):
        return subprocess.run(["bash", "-euo", "pipefail", "-c", step_script(name)],
                              cwd=self.root, env=self.env, text=True, capture_output=True)

    def calls(self):
        return [json.loads(row) for row in self.calls_path.read_text().splitlines()] if self.calls_path.exists() else []

    def test_valid_ci_checkpoint_is_reused_without_download(self):
        self.write(self.cache, self.valid_locale)
        result = self.run_step("Use active multilingual cache only without a CI checkpoint")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.cache.read_bytes(), self.valid_locale)
        self.assertEqual(self.calls(), [])

    def test_corrupt_ci_checkpoint_is_quarantined_before_active_fallback(self):
        self.write(self.cache, b"corrupt saved CI cache")
        result = self.run_step("Use active multilingual cache only without a CI checkpoint")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.cache.read_bytes(), self.valid_locale)
        self.assertEqual(self.cache.with_name("rejected-ci-cache.json.gz").read_bytes(), b"corrupt saved CI cache")
        self.assertIn("::warning::", result.stdout)
        self.assertEqual(len(self.calls()), 1)
        self.assertIn("/.well-known/edge-release/" + "a" * 32 + "/data/i18n/cache-v1.json.gz",
                      " ".join(self.calls()[0]["args"]))

    def test_invalid_active_fallback_fails_without_promoting_it(self):
        self.fetch_body.write_bytes(b"invalid active checkpoint")
        result = self.run_step("Use active multilingual cache only without a CI checkpoint")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.cache.exists())
        self.assertEqual(len(self.calls()), 1)

    def test_only_missing_active_checkpoint_can_start_empty(self):
        for status, accepted in (("404", True), ("503", False), ("403", False)):
            with self.subTest(status=status):
                self.env["STUB_FETCH_STATUS"] = status
                result = self.run_step("Use active multilingual cache only without a CI checkpoint")
                self.assertEqual(result.returncode == 0, accepted, result.stderr)
                self.assertFalse(self.cache.exists())

    def test_invalid_built_checkpoint_does_not_replace_valid_restored_progress(self):
        self.write(self.built, b"partial build cache")
        self.write(self.cache, self.valid_locale)
        result = self.run_step("Detect multilingual translation checkpoint")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_text(), "present=true\n")
        self.assertEqual(self.cache.read_bytes(), self.valid_locale)
        self.assertEqual(self.built.read_bytes(), b"partial build cache")

    def test_valid_built_checkpoint_is_promoted_to_saved_progress(self):
        self.write(self.built, self.valid_locale)
        self.write(self.cache, b"older damaged cache")
        result = self.run_step("Detect multilingual translation checkpoint")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_text(), "present=true\n")
        self.assertEqual(self.cache.read_bytes(), self.valid_locale)

    def test_invalid_checkpoints_are_never_offered_to_cache_save(self):
        self.write(self.built, b"partial build cache")
        self.write(self.cache, b"bad restored cache")
        result = self.run_step("Detect multilingual translation checkpoint")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_text(), "present=false\n")
        self.assertEqual(self.cache.read_bytes(), b"bad restored cache")
        self.assertIn("::warning::", result.stdout)

    def test_corrupt_title_checkpoint_is_quarantined_before_source_seed_translation(self):
        self.write(self.title, b"corrupt title cache")
        self.write(self.root / "portal_suite/data/catalog.json", b'{"items": []}')
        result = self.run_step("Translate missing report titles")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.title.read_bytes(), self.valid_title)
        self.assertEqual(self.title.with_name("rejected-title-cache.json").read_bytes(), b"corrupt title cache")
        self.assertEqual(len(self.calls()), 1)
        self.assertFalse(self.calls()[0]["existing_cache"])
        self.assertIn("--seed-catalog-path", self.calls()[0]["args"])
        self.assertIn("::warning::", result.stdout)

    def test_title_detection_only_saves_valid_checkpoints(self):
        for body, expected in ((b"bad title cache", "false"), (self.valid_title, "true")):
            with self.subTest(valid=expected):
                self.output.unlink(missing_ok=True)
                self.write(self.title, body)
                result = self.run_step("Detect Chinese report title checkpoint")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.output.read_text(), f"present={expected}\n")

    def test_cache_service_failures_warn_without_disabling_validation(self):
        names = ("Restore Chinese report title checkpoint", "Save Chinese report title checkpoint",
                 "Restore resumable multilingual translation checkpoint", "Save multilingual translation checkpoint")
        for name in names:
            with self.subTest(step=name):
                self.assertIn("continue-on-error: true", step_block(name))
        for name in ("Validate complete static release", "Verify catalog inheritance before publication",
                     "Verify protected Chinese release after locale build"):
            self.assertNotIn("continue-on-error", step_block(name))
        self.env.update(TITLE_RESTORE="failure", TITLE_SAVE="success", LOCALE_RESTORE="skipped", LOCALE_SAVE="failure")
        result = self.run_step("Report optional cache service failures")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("::warning::", result.stdout)
        self.assertIn("TITLE_RESTORE, LOCALE_SAVE", self.summary.read_text())
        self.assertNotIn("TITLE_SAVE", self.summary.read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
