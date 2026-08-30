#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/manual-cloudflare-url-cache-purge.yml"


class ManualCloudflareUrlCachePurgeWorkflowContractTests(unittest.TestCase):
    def workflow(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_is_manual_only_and_defaults_to_dry_run(self) -> None:
        workflow = self.workflow()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotRegex(workflow, r"(?m)^\s+(?:schedule|push|pull_request|workflow_run):")
        self.assertRegex(workflow, r"mode:[\s\S]*?default:\s*dry-run")
        self.assertRegex(workflow, r"options:[\s\S]*?- dry-run[\s\S]*?- apply")

    def test_apply_is_the_only_step_that_receives_token_and_posts(self) -> None:
        workflow = self.workflow()
        self.assertEqual(workflow.count("secrets.CLOUDFLARE_API_TOKEN"), 1)
        self.assertEqual(workflow.count("secrets.PORTAL_SITE_URL"), 1)
        self.assertIn('echo "::add-mask::$PORTAL_SITE_URL"', workflow)
        self.assertIn("if: ${{ inputs.mode == 'apply' }}", workflow)
        self.assertEqual(workflow.count("--mode apply"), 1)
        self.assertNotIn("wrangler", workflow.casefold())
        self.assertNotRegex(workflow, r"(?i)edge_route|cutover|deploy|r2|purge_everything")

    def test_workflow_runs_unit_and_contract_tests_before_apply(self) -> None:
        workflow = self.workflow()
        unit = workflow.index("python3 -B scripts/test_manual_cloudflare_url_cache_purge.py")
        contract = workflow.index("python3 -B scripts/test_manual_cloudflare_url_cache_purge_workflow.py")
        apply = workflow.index("python3 -B scripts/manual_cloudflare_url_cache_purge.py --mode apply")
        self.assertLess(unit, apply)
        self.assertLess(contract, apply)
        self.assertIn("persist-credentials: false", workflow)
        self.assertEqual(workflow.count("\npermissions:\n"), 1)
        self.assertIn("contents: read", workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
