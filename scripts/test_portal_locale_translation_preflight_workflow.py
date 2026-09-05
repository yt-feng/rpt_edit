#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_public_identity as identity

WORKFLOW = ROOT / ".github/workflows/portal-locale-translation-preflight.yml"


class PreflightWorkflowTests(unittest.TestCase):
    def test_manual_main_only_without_deployment_or_full_build(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", workflow)
        self.assertNotRegex(workflow, r"(?m)^\s+(?:schedule|push|pull_request|workflow_run):")
        self.assertIn("contents: read", workflow)
        self.assertNotIn("contents: write", workflow)
        for forbidden in ("wrangler", "publish_static_slot.py", "build_portal_suite_site.py", "cancel-in-progress: true"):
            self.assertNotIn(forbidden, workflow)
        self.assertIn("python3 -m pip install requests", workflow)

    def test_uses_existing_private_configuration_and_uploads_failure_diagnostics(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("LIVE_ORIGIN: ${{ secrets.PORTAL_SITE_URL || vars.PORTAL_SITE_URL }}", workflow)
        for secret in ("DEEPSEEK_API_KEY", "DEEPSEEK_API_KEY_BACKUP", "DEEPSEEK_API_KEY_2", "DEEPSEEK_API_KEYS"):
            self.assertIn(f"{secret}: ${{{{ secrets.{secret} }}}}", workflow)
        upload = workflow[workflow.index("Upload translation diagnostics even when preflight fails"):]
        self.assertIn("if: always()", upload)
        self.assertIn("actions/upload-artifact@v4", upload)
        self.assertIn("portal-locale-preflight/diagnostics.json", upload)
        self.assertNotIn("cache-v1.json.gz", upload)

    def test_public_identity_guard_accepts_every_new_source(self) -> None:
        paths = (WORKFLOW, ROOT / "scripts/preflight_portal_locale_translation.py",
                 ROOT / "scripts/test_preflight_portal_locale_translation.py", Path(__file__))
        for path in paths:
            skeleton = identity.confusable_skeleton(path.read_text(encoding="utf-8"))
            with self.subTest(path=path.name):
                self.assertFalse(any(marker.casefold() in skeleton for marker in identity.private_markers()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
