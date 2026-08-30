#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/manual-edge-canonical-redirect-hotfix.yml"


class ManualEdgeCanonicalRedirectHotfixWorkflowContractTests(unittest.TestCase):
    def workflow(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_is_manual_only_and_has_read_only_repository_permission(self) -> None:
        workflow = self.workflow()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotRegex(workflow, r"(?m)^\s+(?:schedule|push|pull_request|workflow_run):")
        self.assertEqual(workflow.count("\npermissions:\n"), 1)
        self.assertIn("contents: read", workflow)
        self.assertIn("persist-credentials: false", workflow)

    def test_live_state_is_cache_busted_strictly_validated_and_reused(self) -> None:
        workflow = self.workflow()
        self.assertIn("/.well-known/edge-state?hotfix=${nonce}", workflow)
        self.assertIn('slot not in {"a", "b"}', workflow)
        self.assertIn('re.fullmatch(r"[0-9a-f]{32}", release)', workflow)
        self.assertIn('re.fullmatch(r"[0-9a-f]{64}", tree)', workflow)
        self.assertIn("STATIC_PREFIX=edge-static/slots/{slot}/", workflow)
        self.assertIn('STATIC_PREFIX = "$STATIC_PREFIX"', workflow)
        self.assertIn('STATIC_RELEASE = "$STATIC_RELEASE"', workflow)
        self.assertIn('STATIC_TREE_SHA256 = "$STATIC_TREE_SHA256"', workflow)

    def test_runtime_matches_neutral_edge_bindings_without_route_or_static_mutation(self) -> None:
        workflow = self.workflow()
        self.assertIn('name = "svc-04df8d213b73"', workflow)
        self.assertIn("[cache]\n          enabled = true", workflow)
        self.assertIn('CANONICAL_HOST = "kcdesk.com"', workflow)
        self.assertIn('binding = "STATIC_BUCKET"', workflow)
        self.assertIn('bucket_name = "$R2_BUCKET"', workflow)
        self.assertIn('binding = "API"', workflow)
        self.assertIn('service = "portal-suite-worker"', workflow)
        self.assertIn("cloudflare/wrangler-action@v3", workflow)
        self.assertIn("workingDirectory: .edge_canonical_hotfix", workflow)
        self.assertIn('wranglerVersion: "4.69.0"', workflow)
        blocked = (
            "publish_static_slot",
            "edge_route_cutover",
            "purge_cache",
            "purge_everything",
            "r2 object put",
            "wrangler r2",
            "build_portal_suite_site",
        )
        for value in blocked:
            self.assertNotIn(value, workflow.casefold())

    def test_edge_tests_precede_deploy_and_live_checks_use_fixed_no_query_urls(self) -> None:
        workflow = self.workflow()
        edge_test = workflow.index("node --test workers/edge-static-host/test/index.test.mjs")
        deploy = workflow.index("cloudflare/wrangler-action@v3")
        verify = workflow.index("Verify fixed no-query canonical URLs and API")
        self.assertLess(edge_test, deploy)
        self.assertLess(deploy, verify)
        for url in (
            "https://kcdesk.com/",
            "https://kcdesk.com/reports/",
            "https://kcdesk.com/blog/",
            "https://kcdesk.com/reports/institutions/bernstein/",
        ):
            self.assertIn(f'"{url}"', workflow)
            self.assertNotIn(f'"{url}?', workflow)
        self.assertIn('"https://kcdesk.com/api/health"', workflow)
        self.assertIn('[ "$status" != "200" ] || [ -n "$location" ]', workflow)
        self.assertIn('[ "$api_status" != "200" ]', workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
