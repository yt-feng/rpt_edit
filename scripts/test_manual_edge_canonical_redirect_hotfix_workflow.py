#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/manual-edge-canonical-redirect-hotfix.yml"
ROUTE_AUDITOR = ROOT / "scripts/edge_route_cutover.py"


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
        self.assertIn(".github/workflows/neutral-edge-cutover.yml", workflow)
        self.assertIn("scripts/capture_edge_worker_deployment.py", workflow)
        self.assertIn("group: edge-static-hosting-production", workflow)
        self.assertIn("Require audited main branch", workflow)
        self.assertIn('if [ "$GITHUB_REF" != "refs/heads/main" ]', workflow)

    def test_live_state_is_cache_busted_strictly_validated_and_reused(self) -> None:
        workflow = self.workflow()
        self.assertIn("LIVE_ORIGIN: ${{ secrets.PORTAL_SITE_URL }}", workflow)
        self.assertIn("Configured site URL is not a bare HTTPS origin", workflow)
        self.assertIn("printf 'SITE_HOST=%s\\n'", workflow)
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
        self.assertIn("[cache]\n          enabled = false", workflow)
        self.assertIn('CANONICAL_HOST = "$SITE_HOST"', workflow)
        self.assertIn('binding = "STATIC_BUCKET"', workflow)
        self.assertIn('bucket_name = "$R2_BUCKET"', workflow)
        self.assertIn('binding = "API"', workflow)
        self.assertIn('service = "portal-suite-worker"', workflow)
        self.assertIn("cloudflare/wrangler-action@v3", workflow)
        self.assertIn("workingDirectory: .edge_canonical_hotfix", workflow)
        self.assertIn('wranglerVersion: "4.69.0"', workflow)
        blocked = (
            "publish_static_slot",
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
        auditor = ROUTE_AUDITOR.read_text(encoding="utf-8")
        edge_test = workflow.index("node --test workers/edge-static-host/test/index.test.mjs")
        route_test = workflow.index("python3 -B scripts/test_edge_route_cutover.py")
        capture = workflow.index("Capture exact edge rollback target")
        deploy = workflow.index("cloudflare/wrangler-action@v3")
        verify = workflow.index("Verify fixed no-query canonical URLs and API")
        self.assertLess(edge_test, deploy)
        self.assertLess(route_test, deploy)
        self.assertLess(capture, deploy)
        self.assertLess(deploy, verify)
        for path in (
            "/",
            "/reports/",
            "/blog/",
            "/reports/institutions/bernstein/",
        ):
            self.assertIn(f'"{path}"', auditor)
        self.assertIn("python3 -B scripts/edge_route_cutover.py verify", workflow)
        self.assertIn('EDGE_VERIFY_CONSECUTIVE: "3"', workflow)
        self.assertIn("Roll back failed edge hotfix", workflow)
        self.assertIn("EDGE_PREVIOUS_VERSION_ID", workflow)
        self.assertIn('command: rollback ${{ env.EDGE_PREVIOUS_VERSION_ID }} --message "Automated rollback', workflow)
        self.assertIn("Verify rollback restored service availability", workflow)
        self.assertIn("timeout-minutes: 35", workflow)
        self.assertIn("timeout-minutes: 8", workflow)
        self.assertIn("/.well-known/edge-state?rollback=", workflow)
        self.assertIn('"slot": os.environ["STATIC_SLOT"]', workflow)
        self.assertIn('"release_id": os.environ["STATIC_RELEASE"]', workflow)
        self.assertIn('"tree_sha256": os.environ["STATIC_TREE_SHA256"]', workflow)
        self.assertIn('--expect-version "$EDGE_PREVIOUS_VERSION_ID"', workflow)
        self.assertIn("edge_hotfix_rollback=exact_version_and_state_restored", workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
