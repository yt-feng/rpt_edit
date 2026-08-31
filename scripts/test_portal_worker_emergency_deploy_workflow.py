#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/portal-worker-emergency-deploy.yml"


class PortalWorkerEmergencyDeployWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_release_is_version_only_and_does_not_touch_edge_or_static_data(self) -> None:
        self.assertIn("versions upload --keep-vars", self.workflow)
        self.assertIn("versions deploy", self.workflow)
        self.assertIn('compatibility_flags = ["global_fetch_strictly_public"]', self.workflow)
        self.assertIn("cancel-in-progress: false", self.workflow)
        for forbidden in (
            "publish_static_slot.py",
            "edge_route_cutover.py",
            "cache_purge",
            "neutral-edge-cutover.yml",
            "api/hot-reports",
            "bootstrap=1",
        ):
            self.assertNotIn(forbidden, self.workflow)

    def test_exact_rollback_target_is_captured_before_deploy(self) -> None:
        resolve_name = self.workflow.index("Resolve private Portal Worker name")
        capture = self.workflow.index("Capture exact Portal Worker rollback target")
        upload = self.workflow.index("Upload Cloudflare Worker version")
        deploy = self.workflow.index("Deploy Cloudflare Worker version at 100 percent")
        self.assertLess(resolve_name, capture)
        self.assertLess(capture, upload)
        self.assertLess(upload, deploy)
        self.assertIn("name_matches = []", self.workflow)
        self.assertIn("len(name_matches) != 1", self.workflow)
        self.assertNotIn("import tomllib", self.workflow)
        self.assertIn('worker_name == "portal-suite-worker"', self.workflow)
        self.assertEqual(
            self.workflow.count('--script-name "$PORTAL_WORKER_SCRIPT_NAME"'),
            2,
        )
        self.assertIn("--output-env \"$GITHUB_ENV\"", self.workflow)

    def test_failed_deploy_or_smoke_rolls_back_and_verifies_exact_version(self) -> None:
        self.assertIn("id: deploy-worker-version", self.workflow)
        self.assertIn("id: portal_smoke", self.workflow)
        self.assertIn("id: portal_rollback", self.workflow)
        self.assertIn("steps.deploy-worker-version.outcome != 'skipped'", self.workflow)
        self.assertIn("steps.portal_smoke.outcome != 'success'", self.workflow)
        self.assertIn("rollback ${{ env.EDGE_PREVIOUS_VERSION_ID }}", self.workflow)
        self.assertIn("--expect-version \"$EDGE_PREVIOUS_VERSION_ID\"", self.workflow)
        self.assertIn("$origin/api/health", self.workflow)

    def test_job_and_steps_reserve_time_for_rollback(self) -> None:
        self.assertIn("timeout-minutes: 35", self.workflow)
        self.assertGreaterEqual(self.workflow.count("timeout-minutes: 5"), 4)
        self.assertIn("timeout-minutes: 8", self.workflow)

    def test_portal_suite_uses_stable_isolated_node_runner(self) -> None:
        self.assertIn("for test_file in portal_suite/tests/*.test.mjs; do", self.workflow)
        self.assertIn('node --test --test-isolation=none "$test_file"', self.workflow)
        self.assertNotIn("node --test portal_suite/tests/*.test.mjs", self.workflow)
        self.assertNotIn("--test-concurrency", self.workflow)

    def test_materialized_public_site_is_brand_checked_before_worker_upload(self) -> None:
        self.assertIn("scripts/check_public_brand.py", self.workflow)
        self.assertIn("scripts/test_check_public_brand.py", self.workflow)
        self.assertIn("python3 -B scripts/test_check_public_brand.py", self.workflow)
        materialize = self.workflow.index("Materialize private deployment values")
        brand_check = self.workflow.index("Validate materialized public brand")
        upload = self.workflow.index("Upload Cloudflare Worker version")
        self.assertLess(materialize, brand_check)
        self.assertLess(brand_check, upload)
        self.assertIn(
            "python3 -B scripts/check_public_brand.py portal_suite/site_src",
            self.workflow,
        )
        self.assertNotIn(
            "check_public_brand.py workers/portal-suite-worker/src",
            self.workflow,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
