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
        # The separate manual-only storage smoke needs R2 credentials. PR model
        # preflight remains secret-free and cannot execute the storage job.
        preflight = workflow.split("  preflight:\n", 1)[1].split("  private-checkpoint-smoke:\n", 1)[0]
        self.assertNotIn("secrets.", preflight)
        for forbidden in ("contents: write", "wrangler", "run_portal_locale_backfill.py", "DEEPSEEK_API_KEY"):
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
        cache = action.split("uses: actions/cache/restore@v4", 1)[1].split("- name:", 1)[0]
        self.assertIn("path: ${{ runner.temp }}/hymt-model", cache)
        self.assertNotIn("translation-cache", cache)
        self.assertEqual(action.count("uses: actions/cache/save@v4"), 2)
        for block in re.split(r"uses: actions/cache/(?:restore|save)@v4", action)[1:]:
            cache_path = re.search(r"path:\s*(.+)", block.split("- name:", 1)[0]).group(1)
            self.assertIn(cache_path, ("${{ runner.temp }}/hymt-model", "${{ runner.temp }}/hymt-runtime/build"))
        self.assertIn("-DGGML_NATIVE=OFF", action)
        self.assertIn("runtime-revision", action)
        # Different Ubuntu releases have different glibc/libstdc++ ABIs even
        # when both runners report Linux/X64. Never share their native binaries.
        self.assertIn("platform.freedesktop_os_release()", action)
        runtime_keys = re.findall(r"key: (hymt-cpu-[^\n]+)", action)
        self.assertEqual(len(runtime_keys), 2)
        self.assertTrue(all("steps.configure.outputs.runner-image" in key for key in runtime_keys))
        self.assertIn("persist-credentials: false", action)

if __name__ == "__main__":
    unittest.main()
