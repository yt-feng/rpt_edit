#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/neutral-edge-cutover.yml"


class NeutralEdgeCutoverWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_schedule_and_content_triggers_are_gated_and_reviewed(self) -> None:
        trigger = self.workflow[: self.workflow.index("\npermissions:\n")]
        self.assertIn('cron: "30 1,5,9,13 * * *"', trigger)
        self.assertIn("workflow_run:", trigger)
        for producer in (
            "Bank report catalog",
            "Final PDF to XHS notes",
            "Institution latest PDF to WeChat",
            "Consulting latest PDF to WeChat",
            "ARK Invest feed to WeChat",
            "Upload XHS notes to WeChat drafts",
            "Portal chart search index",
        ):
            self.assertIn(f"- {producer}", trigger)
        self.assertNotIn("Portal Search Mirror", trigger)
        self.assertIn("types: [completed]", trigger)
        self.assertIn("branches: [main]", trigger)
        self.assertRegex(trigger, r"(?m)^\s+- rehearse\s*$")
        self.assertRegex(trigger, r"(?m)^\s+- migrate\s*$")
        self.assertNotIn("switch", trigger)
        self.assertIn("default: rehearse", trigger)
        self.assertIn("vars.NEUTRAL_SCHEDULE_ENABLED == 'true'", self.workflow)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", self.workflow)
        self.assertIn("github.event.workflow_run.head_branch == github.event.repository.default_branch", self.workflow)
        self.assertIn("github.event.workflow_run.head_repository.full_name == github.repository", self.workflow)
        self.assertIn('case "$GITHUB_EVENT_NAME" in', self.workflow)
        self.assertIn('rehearse|migrate) operation="$REQUESTED_OPERATION"', self.workflow)
        self.assertIn('schedule|workflow_run)', self.workflow)

    def test_prepare_and_cutover_are_separate_bounded_jobs(self) -> None:
        self.assertIn("  prepare_release:\n", self.workflow)
        self.assertIn("  cutover:\n", self.workflow)
        self.assertIn("needs: prepare_release", self.workflow)
        prepare = self.workflow.index("  prepare_release:\n")
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")
        cutover = self.workflow.index("  cutover:\n")
        deploy = self.workflow.index("Deploy prepared neutral edge release")
        self.assertLess(prepare, upload)
        self.assertLess(upload, cutover)
        self.assertLess(cutover, deploy)
        self.assertIn("timeout-minutes: 150", self.workflow[prepare:cutover])
        self.assertIn("timeout-minutes: 65", self.workflow[cutover:])
        self.assertEqual(self.workflow.count("ref: ${{ github.sha }}"), 2)
        self.assertNotIn("ref: main", self.workflow)
        self.assertNotIn('echo "::add-mask::$release_id"', self.workflow)

    def test_transaction_has_exact_state_and_operation_aware_rollback(self) -> None:
        self.assertIn("previous-edge-state.json", self.workflow)
        self.assertIn("previous_release", self.workflow)
        self.assertIn("previous_tree", self.workflow)
        self.assertIn("Prove live release is unchanged before cutover", self.workflow)
        self.assertIn("cmp _release_validation/previous/edge-state.json", self.workflow)
        self.assertIn("Capture exact edge rollback target", self.workflow)
        self.assertIn("steps.release_acceptance.outcome != 'success' || needs.prepare_release.outputs.operation == 'rehearse'", self.workflow)
        self.assertIn("rollback ${{ env.EDGE_PREVIOUS_VERSION_ID }}", self.workflow)
        self.assertIn("--expect-version \"$EDGE_PREVIOUS_VERSION_ID\"", self.workflow)
        self.assertIn("Verify exact previous release after rollback", self.workflow)
        self.assertIn("Enforce transactional outcome", self.workflow)

    def test_semantic_manifest_prevents_unchanged_automatic_cutovers(self) -> None:
        compare = self.workflow.index("Detect meaningful public release changes")
        upload = self.workflow.index("Upload inactive static slot and immutable runtime")
        deploy = self.workflow.index("Deploy prepared neutral edge release")
        self.assertLess(compare, upload)
        self.assertLess(upload, deploy)
        self.assertIn("previous-release-semantics.json", self.workflow)
        self.assertIn('PYTHONPATH=scripts PREVIOUS_MANIFEST="$output" python3', self.workflow)
        self.assertIn("--write-current-manifest _neutral_site/data/release-semantics.json", self.workflow)
        for component in (
            "--current-catalog",
            "--current-search-index",
            "--current-chart-search-index",
            "--current-password-rules",
            "--current-runtime-config",
            "--blog-archive-root",
            "--site-source-root",
            "--public-root",
        ):
            self.assertIn(component, self.workflow)
        self.assertIn('if [ "$GITHUB_EVENT_NAME" = "workflow_dispatch" ]', self.workflow)
        self.assertEqual(self.workflow.count("--force"), 1)
        self.assertIn("if: steps.release_delta.outputs.changed == 'true'", self.workflow)
        self.assertIn("if: needs.prepare_release.outputs.changed == 'true'", self.workflow)
        self.assertIn("release-semantics-after.json", self.workflow)

    def test_cutover_proves_portal_runtime_and_canonical_routes(self) -> None:
        cutover = self.workflow[self.workflow.index("  cutover:\n"):]
        route_context = cutover.index("Prepare masked live route context")
        route_verify = cutover.index("Prove live release is unchanged before cutover")
        self.assertLess(route_context, route_verify)
        self.assertIn("printf 'SITE_HOST=%s\\n'", cutover)
        self.assertIn("printf 'EDGE_ALIAS_HOSTS=%s\\n'", cutover)
        self.assertIn("printf 'LIVE_ORIGIN=%s\\n'", cutover)
        self.assertIn("python3 -B scripts/edge_route_cutover.py verify", cutover)
        self.assertGreaterEqual(cutover.count("api/health?runtime-data=1"), 2)
        self.assertIn('runtime.get("release_id") != os.environ["STATIC_RELEASE"]', cutover)
        self.assertIn('runtime.get("catalog_versioned") is not True', cutover)
        self.assertIn('runtime.get("rules_versioned") is not True', cutover)
        self.assertIn('runtime.get("release_id") != os.environ["PREVIOUS_STATIC_RELEASE"]', cutover)

    def test_destructive_and_nontransactional_tail_actions_are_absent(self) -> None:
        self.assertIn('CATALOG_PDF_CLEANUP_ENABLED: "false"', self.workflow)
        for forbidden in (
            "--enable-pdf-cleanup",
            "api/hot-reports",
            "build_report_chat_index.py",
            "build_report_research_index.py",
            "submit_portal_indexnow.py",
            "commit_output_dir.sh",
            "Prune obsolete legacy static releases",
            "edge_route_cutover.py migrate",
            "edge_route_cutover.py rollback",
            "cache_purge",
        ):
            self.assertNotIn(forbidden, self.workflow)

    def test_all_production_mutators_share_one_non_cancelling_lock(self) -> None:
        workflows = (
            WORKFLOW,
            ROOT / ".github/workflows/portal-worker-emergency-deploy.yml",
            ROOT / ".github/workflows/manual-edge-canonical-redirect-hotfix.yml",
            ROOT / ".github/workflows/manual-cloudflare-url-cache-purge.yml",
        )
        for path in workflows:
            body = path.read_text(encoding="utf-8")
            self.assertIn("group: portal-production-release", body, path.name)
            self.assertIn("cancel-in-progress: false", body, path.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
