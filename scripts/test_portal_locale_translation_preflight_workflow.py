"""Validate the free translation CI boundary, executable entrypoints and diagnostics."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PreflightWorkflowTests(unittest.TestCase):
    def test_preflight_has_no_paid_provider_credentials_or_deployment(self):
        workflow = (ROOT / ".github/workflows/portal-locale-translation-preflight.yml").read_text()
        self.assertIn("pull_request:", workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("contents: read", workflow)
        for forbidden in ("secrets.", "contents: write", "wrangler", "run_portal_locale_backfill.py"):
            self.assertNotIn(forbidden, workflow)
        self.assertIn("scripts/smoke_hymt_translation.py", workflow)
        upload = workflow.split("Upload translation diagnostics even when preflight fails", 1)[1]
        self.assertIn("if: always()", upload)
        self.assertIn("portal-locale-preflight/", upload)

    def test_all_invoked_scripts_exist(self):
        workflow = (ROOT / ".github/workflows/portal-locale-translation-preflight.yml").read_text()
        for script in re.findall(r"python(?:3)?(?: -B)? (scripts/[A-Za-z0-9_.]+)", workflow):
            self.assertTrue((ROOT / script).is_file(), script)

    def test_setup_caches_only_public_pinned_model_files(self):
        action = (ROOT / ".github/actions/setup-offline-translation/action.yml").read_text()
        self.assertIn("hymt-official-q8-", action)
        self.assertIn("scripts/hymt_translation_model_manifest.json", action)
        cache = action.split("uses: actions/cache@v4", 1)[1].split("- name:", 1)[0]
        self.assertIn("path: ${{ runner.temp }}/hymt-model", cache)
        self.assertNotIn("translation-cache", cache)
        self.assertIn("-DGGML_NATIVE=OFF", action)
        self.assertIn("runtime-revision", action)
        self.assertIn("persist-credentials: false", action)

if __name__ == "__main__":
    unittest.main()
