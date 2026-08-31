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

    def test_first_phase_is_manual_rehearsal_without_cron(self) -> None:
        trigger = self.workflow[: self.workflow.index("\npermissions:\n")]
        self.assertNotIn("schedule:", trigger)
        self.assertNotIn("workflow_run:", trigger)
        self.assertRegex(trigger, r"(?m)^\s+- rehearse\s*$")
        self.assertNotIn("migrate", trigger)
        self.assertNotIn("switch", trigger)
        self.assertIn("default: rehearse", trigger)
        self.assertIn('test "${{ inputs.operation }}" = "rehearse"', self.workflow)

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

    def test_transaction_has_exact_state_and_forced_rehearsal_rollback(self) -> None:
        self.assertIn("previous-edge-state.json", self.workflow)
        self.assertIn("previous_release", self.workflow)
        self.assertIn("previous_tree", self.workflow)
        self.assertIn("Prove live release is unchanged before cutover", self.workflow)
        self.assertIn("cmp _release_validation/previous/edge-state.json", self.workflow)
        self.assertIn("Capture exact edge rollback target", self.workflow)
        self.assertIn("steps.release_acceptance.outcome != 'success' || inputs.operation == 'rehearse'", self.workflow)
        self.assertIn("rollback ${{ env.EDGE_PREVIOUS_VERSION_ID }}", self.workflow)
        self.assertIn("--expect-version \"$EDGE_PREVIOUS_VERSION_ID\"", self.workflow)
        self.assertIn("Verify exact previous release after rollback", self.workflow)
        self.assertIn("Enforce transactional outcome", self.workflow)

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
