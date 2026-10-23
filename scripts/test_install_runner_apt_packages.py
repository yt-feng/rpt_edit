#!/usr/bin/env python3
"""Exercise dependency failures without invoking sudo or the real package manager."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/install_runner_apt_packages.sh"
WORKFLOWS = ROOT / ".github/workflows"
FONT_WORKFLOWS = (
    "institution-latest-pdf-to-wechat.yml",
    "consulting-latest-pdf-to-wechat.yml",
    "ark-invest-feed-to-wechat.yml",
    "portal-translated-reports-test.yml",
    "replay-report-translation-shards.yml",
    "dropbox-latest-pdf-to-xhs-sharded.yml",
)


class RunnerAptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.log = self.directory / "calls.jsonl"
        # Replace sudo itself: tests never elevate privileges, install packages,
        # inspect the host's package state, or make network requests.
        sudo = self.directory / "sudo"
        sudo.write_text(
            f"#!{sys.executable}\n"
            "import json, os, sys\n"
            "with open(os.environ['APT_TEST_LOG'], 'a') as log:\n"
            "    log.write(json.dumps(sys.argv[1:]) + '\\n')\n"
            "phase = 'update' if sys.argv[-1] == 'update' else 'install'\n"
            "sys.exit(int(os.environ.get('APT_TEST_' + phase.upper() + '_STATUS', '0')))\n"
        )
        sudo.chmod(0o755)

    def run_setup(self, *packages, **changes):
        env = dict(os.environ, PATH=f"{self.directory}{os.pathsep}{os.environ['PATH']}",
                   GITHUB_ACTIONS="true", RUNNER_OS="Linux", APT_TEST_LOG=str(self.log))
        env.update(changes)
        result = subprocess.run(["bash", str(SCRIPT), *packages], env=env,
                                capture_output=True, text=True, timeout=5)
        calls = [json.loads(line) for line in self.log.read_text().splitlines()] if self.log.exists() else []
        return result, calls

    def test_root_timeout_contains_both_apt_process_groups_and_bounded_retries(self):
        result, calls = self.run_setup("tesseract-ocr", "tesseract-ocr-eng", "tesseract-ocr-chi-sim")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(len(calls), 2)
        for call, budget in zip(calls, ("120s", "240s")):
            self.assertEqual(call[:7], ["timeout", "--signal=TERM", "--kill-after=15s", budget,
                                       "env", "DEBIAN_FRONTEND=noninteractive", "apt-get"])
            self.assertNotIn("--foreground", call)
            for option in ("DPkg::Lock::Timeout=60", "Acquire::Retries=2",
                           "Acquire::http::Timeout=30", "Acquire::https::Timeout=30"):
                self.assertIn(option, call)
        self.assertEqual(calls[0][-3:], ["-o", "APT::Update::Error-Mode=any", "update"])
        self.assertEqual(calls[1][-6:], ["install", "-y", "--no-install-recommends",
                                      "tesseract-ocr", "tesseract-ocr-eng", "tesseract-ocr-chi-sim"])

    def test_failed_or_timed_out_update_never_starts_install(self):
        for status in (100, 124, 137):
            with self.subTest(status=status):
                self.log.unlink(missing_ok=True)
                result, calls = self.run_setup("fonts-noto-cjk", APT_TEST_UPDATE_STATUS=str(status))
                self.assertEqual(result.returncode, status)
                self.assertEqual(len(calls), 1)
                self.assertIn(f"exit {status}", result.stdout)

    def test_install_failure_is_not_hidden_or_retried(self):
        result, calls = self.run_setup("tesseract-ocr", APT_TEST_INSTALL_STATUS="100")
        self.assertEqual(result.returncode, 100)
        self.assertEqual(len(calls), 2)

    def test_local_host_and_invalid_packages_are_rejected_before_sudo(self):
        for packages, changes in ((["fonts-noto-cjk"], {"RUNNER_OS": "macOS"}),
                                  (["fonts-noto-cjk"], {"GITHUB_ACTIONS": "false"}),
                                  ([], {}), (["--assume-yes"], {}), (["foo;bar"], {})):
            with self.subTest(packages=packages, changes=changes):
                result, calls = self.run_setup(*packages, **changes)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(calls, [])

    def test_optional_fonts_cannot_outlive_their_workflow_steps(self):
        count = 0
        for name in FONT_WORKFLOWS:
            text = (WORKFLOWS / name).read_text()
            for block in text.split("      - name: ")[1:]:
                if not block.startswith("Install Chinese fonts"):
                    continue
                count += 1
                self.assertIn("timeout-minutes: 8", block, name)
                self.assertIn("continue-on-error: true", block, name)
                self.assertIn("bash scripts/install_runner_apt_packages.sh fonts-noto-cjk", block, name)
                self.assertNotIn("sudo apt-get", block, name)
        self.assertEqual(count, 7)

    def test_institution_required_ocr_finishes_before_optional_fonts(self):
        text = (WORKFLOWS / FONT_WORKFLOWS[0]).read_text()
        ocr = text.index("- name: Install required institution OCR fallback tools")
        font = text.index("- name: Install Chinese fonts")
        self.assertLess(ocr, font)
        block = text[ocr:font]
        self.assertNotIn("continue-on-error", block)
        self.assertIn("timeout-minutes: 8", block)
        self.assertIn("bash scripts/install_runner_apt_packages.sh tesseract-ocr tesseract-ocr-eng tesseract-ocr-chi-sim", block)
        self.assertIn("tesseract --list-langs", block)
        self.assertIn("inputs.completed_source_recovery == 'none'", block)

    def test_cloud_regression_checks_failure_cases_before_actual_install(self):
        text = (WORKFLOWS / "wechat-pipeline-regression.yml").read_text()
        self.assertEqual(text.count('"scripts/*runner_apt_packages*"'), 2)
        test = text.index("python scripts/test_install_runner_apt_packages.py")
        install = text.index("- name: Install real cloud OCR regression dependencies")
        self.assertLess(test, install)
        block = text[install:].split("\n      - name:", 1)[0]
        self.assertIn("timeout-minutes: 8", block)
        self.assertIn("bash scripts/install_runner_apt_packages.sh", block)
        self.assertNotIn("fonts-noto-cjk", block)
        self.assertIn('test -f "$TESSDATA_DIR/eng.traineddata"', block)
        self.assertIn('test -f "$TESSDATA_DIR/chi_sim.traineddata"', block)
        self.assertNotIn("continue-on-error", block)
        optional = text.index("- name: Exercise optional Chinese font setup")
        verify = text.index("- name: Verify required OCR and released package locks after optional fonts")
        self.assertLess(install, optional)
        self.assertLess(optional, verify)
        self.assertIn("continue-on-error: true", text[optional:verify])
        self.assertIn("timeout-minutes: 8", text[optional:verify])
        block = text[verify:].split("\n      - name:", 1)[0]
        self.assertNotIn("continue-on-error", block)
        self.assertIn("LOCK_EX | fcntl.LOCK_NB", block)
        for path in ("/var/lib/dpkg/lock-frontend", "/var/lib/dpkg/lock",
                     "/var/lib/apt/lists/lock", "/var/cache/apt/archives/lock"):
            self.assertIn(path, block)
        self.assertIn("python scripts/test_pdf_to_xhs_fonts.py", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
