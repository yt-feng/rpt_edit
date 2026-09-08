#!/usr/bin/env python3
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest

from check_portal_app_budget import check_budget


class AppBudgetTests(unittest.TestCase):
    def test_exact_raw_limit_and_raw_overflow(self):
        self.assertEqual(check_budget(b"a" * 700_000)["status"], "passed")
        self.assertEqual(check_budget(b"a" * 700_001)["violations"], ["absolute loading budget"])

    def test_gzip_overflow_is_checked_independently(self):
        source = random.Random(42).randbytes(180_000)
        report = check_budget(source)
        self.assertLess(report["candidate_bytes"], 700_000)
        self.assertGreater(report["candidate_gzip_bytes"], 150_000)
        self.assertEqual(report["status"], "failed")

    def test_delta_budget_remains_active_when_baseline_supplied(self):
        self.assertEqual(check_budget(b"a" * 25_000, b"a" * 1_000)["status"], "passed")
        self.assertIn("active-release delta budget", check_budget(b"a" * 25_001, b"a" * 1_000)["violations"])
        self.assertEqual(check_budget(b"a" * 25_001)["status"], "passed")

    def test_empty_bundle_does_not_pass(self):
        self.assertEqual(check_budget(b"")["status"], "failed")

    def test_cli_preserves_size_evidence_on_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, output = root / "app.js", root / "report.json"
            source.write_bytes(b"x" * 700_001)
            run = subprocess.run([sys.executable, str(Path(__file__).with_name("check_portal_app_budget.py")),
                                  "--candidate", str(source), "--output", str(output)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 1)
            self.assertEqual(json.loads(output.read_text())["candidate_bytes"], 700_001)
            self.assertIn("absolute loading budget", run.stdout)


if __name__ == "__main__":
    unittest.main()
