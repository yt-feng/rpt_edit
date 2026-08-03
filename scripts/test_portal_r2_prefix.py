#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from portal_r2_prefix import validated_catalog_r2_prefix


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "portal_r2_prefix.py"


class R2PrefixValidatorTests(unittest.TestCase):
    def test_valid_prefix_is_normalized(self) -> None:
        self.assertEqual(
            validated_catalog_r2_prefix("/catalog/reports-v2/"),
            "catalog/reports-v2",
        )

    def test_internal_or_malformed_prefix_is_rejected(self) -> None:
        for prefix in (
            "_hot-reports/pdfs",
            "_catalog-pdf-overrides",
            "reportify",
            "reportify-status/pdfs",
            "thinktank",
            "reports/../_hot-reports",
            "reports//nested",
            "reports with spaces",
            "reports\nmalformed",
            "",
        ):
            with self.subTest(prefix=prefix), self.assertRaisesRegex(ValueError, "prefix"):
                validated_catalog_r2_prefix(prefix)

    def test_cli_prints_only_normalized_prefix(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "/reports/current/"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout, "reports/current\n")
        self.assertEqual(result.stderr, "")

    def test_cli_fails_closed(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), "_hot-reports/pdfs"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("prefix", result.stderr)

    def test_all_worker_deploy_workflows_validate_before_wrangler_config(self) -> None:
        workflows = (
            ROOT / ".github" / "workflows" / "portal-worker-emergency-deploy.yml",
        )
        command = 'python3 scripts/portal_r2_prefix.py "$R2_OBJECT_PREFIX"'
        for workflow in workflows:
            with self.subTest(workflow=workflow.name):
                text = workflow.read_text(encoding="utf-8")
                self.assertIn(command, text)
                self.assertLess(text.index(command), text.index("cat > workers/portal-suite-worker/wrangler.toml"))


if __name__ == "__main__":
    unittest.main()
