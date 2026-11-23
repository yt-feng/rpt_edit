#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/portal-worker-emergency-deploy.yml"


class PortalWorkerEmergencyDeployWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_manual_deployment_override_is_explicit_main_only_and_defaults_off(self) -> None:
        trigger = self.workflow.split("permissions:", 1)[0]
        self.assertIn("workflow_dispatch:", trigger)
        self.assertIn("allow_manual_deploy:", trigger)
        self.assertIn("type: boolean", trigger)
        self.assertIn("default: false", trigger)
        self.assertNotIn("schedule:", trigger)
        self.assertIn("vars.PORTAL_AUTOMATION_ENABLED == 'true' || (github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main' && inputs.allow_manual_deploy == true)", self.workflow)

    def test_worker_ui_and_ci_pin_the_same_python_before_any_python_command(self) -> None:
        sparse = self.workflow.split("sparse-checkout: |", 1)[1].split("\n      - name:", 1)[0]
        paths = {line.strip() for line in sparse.splitlines() if line.strip()}
        workflows = (
            ".github/workflows/portal-worker-emergency-deploy.yml",
            ".github/workflows/portal-ui-hotfix.yml",
            ".github/workflows/public-identity-guard.yml",
        )
        versions = []
        for path in workflows:
            with self.subTest(workflow=path):
                self.assertIn(path, paths, "The sparse deployment must include every inspected contract")
                source = (ROOT / path).read_text(encoding="utf-8")
                setups = list(re.finditer(r"uses: actions/setup-python@v5\n", source))
                self.assertEqual(len(setups), 1)
                setup = source[setups[0].start():].split("\n      - ", 1)[0]
                version = re.search(r"python-version: ['\"]([^'\"]+)['\"]", setup)
                self.assertIsNotNone(version)
                versions.append(version[1])
                first_python = re.search(r"(?m)^\s*(?:run: )?python3(?:\s|$)", source)
                self.assertIsNotNone(first_python)
                self.assertLess(setups[0].start(), first_python.start(),
                                "Install the pinned interpreter before validation or dependency installation")
        self.assertEqual(versions, ["3.11", "3.11", "3.11"])

    def test_release_does_not_touch_routes_or_static_data(self) -> None:
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
        self.assertIn("steps.portal_schedules.outcome != 'success'", self.workflow)
        self.assertIn("rollback ${{ env.EDGE_PREVIOUS_VERSION_ID }}", self.workflow)
        self.assertIn("--expect-version \"$EDGE_PREVIOUS_VERSION_ID\"", self.workflow)
        self.assertIn("$origin/api/health", self.workflow)

    def test_cron_sync_runs_after_smoke_and_is_checked_in_sparse_and_pr_ci(self) -> None:
        smoke = self.workflow.index("- name: Smoke deployed API through the live edge")
        sync = self.workflow.index("- name: Synchronize Portal Worker cron triggers")
        rollback = self.workflow.index("- name: Roll back failed Portal Worker deployment")
        self.assertLess(smoke, sync)
        self.assertLess(sync, rollback)
        step = self.workflow[sync:rollback]
        self.assertIn("id: portal_schedules", step)
        self.assertIn("timeout-minutes: 4", step)
        self.assertIn("CLOUDFLARE_API_TOKEN:", step)
        self.assertIn("CLOUDFLARE_ACCOUNT_ID:", step)
        self.assertNotIn("continue-on-error", step)
        self.assertIn("python3 -B scripts/sync_portal_worker_schedules.py", step)
        sparse = self.workflow.split("sparse-checkout: |", 1)[1].split("\n      - name:", 1)[0]
        for filename in ("sync_portal_worker_schedules.py", "test_sync_portal_worker_schedules.py"):
            self.assertIn("scripts/" + filename, sparse)
        public_ci = (ROOT / ".github/workflows/public-identity-guard.yml").read_text(encoding="utf-8")
        self.assertIn("python3 -B scripts/test_sync_portal_worker_schedules.py", self.workflow)
        self.assertIn("python3 -B scripts/test_sync_portal_worker_schedules.py", public_ci)

    def test_rendered_crons_fit_five_trigger_limit_with_all_day_newsfeed(self) -> None:
        import ast
        config = self.workflow.split("[triggers]", 1)[1].split("[[r2_buckets]]", 1)[0]
        crons = ast.literal_eval(config.split("crons =", 1)[1].strip())
        self.assertEqual(set(crons), {"*/30 * * * *", "*/10 * * * *", "* 2-3 * * *"})
        self.assertEqual(len(crons), 3)

    def test_job_and_steps_reserve_time_for_rollback(self) -> None:
        self.assertIn("timeout-minutes: 35", self.workflow)
        self.assertGreaterEqual(self.workflow.count("timeout-minutes: 5"), 4)
        self.assertIn("timeout-minutes: 8", self.workflow)

    def test_locale_module_is_shipped_with_bounded_opt_in_and_zero_cost_smoke(self) -> None:
        self.assertIn("            workers/portal-suite-worker/src\n", self.workflow)
        self.assertIn("node scripts/test_portal_locale_detail_server.js", self.workflow)
        self.assertIn("< workers/portal-suite-worker/src/locale-report-detail.js", self.workflow)
        for name, default in (("LOCALE_DETAIL_TRANSLATION_ENABLED", "false"),
                              ("LOCALE_DETAIL_DAILY_MAX_REQUESTS", "100"),
                              ("LOCALE_DETAIL_DAILY_MAX_CHARS", "100000")):
            self.assertIn("vars." + name + " || '" + default + "'", self.workflow)
            self.assertIn(name + ' = "$' + name + '"', self.workflow)
        smoke = self.workflow.split("- name: Smoke deployed API through the live edge", 1)[1].split("- name: Roll back", 1)[0]
        self.assertIn('payload.get("locale_detail_translation_v1")', smoke)
        self.assertIn('"locale":"zh-Hans"', smoke)
        self.assertNotIn('"locale":"ja"', smoke)
        self.assertIn('test "$code" = 400', smoke)
        self.assertIn('test "$code" = 503', smoke)

    def test_only_expensive_read_smokes_use_bounded_get_helper_and_keep_json_gate(self) -> None:
        sparse = self.workflow.split('sparse-checkout: |', 1)[1].split('\n      - name:', 1)[0]
        for name in ('portal_smoke_get.py', 'test_portal_smoke_get.py'):
            self.assertIn('scripts/' + name, sparse)
        self.assertIn('.github/workflows/public-identity-guard.yml', sparse)
        self.assertIn('python3 -B scripts/test_portal_smoke_get.py', self.workflow)
        smoke = self.workflow.split('- name: Smoke deployed API through the live edge', 1)[1].split('- name: Roll back', 1)[0]
        self.assertEqual(smoke.count('scripts/portal_smoke_get.py --endpoint '), 2)
        self.assertIn('--endpoint runtime-data', smoke)
        self.assertIn('--endpoint market-views', smoke)
        self.assertIn('"$RUNNER_TEMP/api-runtime-health.json"', smoke)
        self.assertIn('"$RUNNER_TEMP/api-market-views.json"', smoke)
        self.assertIn('health.get("ok") is not True or not runtime.get("rules_loaded")', smoke)
        self.assertIn('int(runtime.get("catalog_item_count") or 0) < 1', smoke)
        self.assertIn('not isinstance(views.get("items"), list) or not views["items"]', smoke)
        self.assertNotIn('continue-on-error:', smoke)
        self.assertIn('steps.portal_smoke.outcome != \'success\'', self.workflow)

    def test_smoke_transport_regressions_run_on_pull_requests(self) -> None:
        workflow = (ROOT / '.github/workflows/public-identity-guard.yml').read_text(encoding='utf-8')
        self.assertIn('  pull_request:', workflow.split('permissions:', 1)[0])
        self.assertIn('python3 -B scripts/test_portal_smoke_get.py', workflow)

    def test_portal_suite_uses_stable_isolated_node_runner(self) -> None:
        self.assertIn("portal_suite/locale_assets", self.workflow)
        self.assertIn("for test_file in portal_suite/tests/*.test.mjs; do", self.workflow)
        self.assertIn('node "$test_file"', self.workflow)
        self.assertNotIn("node --test portal_suite/tests/*.test.mjs", self.workflow)
        self.assertNotIn("--test-isolation", self.workflow)

    def test_reportify_acquisition_contract_dependencies_are_in_sparse_checkout(self) -> None:
        sparse = self.workflow.split("sparse-checkout: |", 1)[1].split("\n      - name:", 1)[0]
        paths = {line.strip() for line in sparse.splitlines() if line.strip()}
        # The API acquisition tests read the workflow contract and import the
        # uploader/status helpers. Full-checkout PR tests cannot catch an
        # omitted runtime dependency in the emergency deployment checkout.
        for path in (
            ".github/workflows/reportify-grab.yml",
            "scripts/test_reportify_api_grab.py",
            "scripts/reportify_pdf_grabber.py",
            "scripts/reportify_result.py",
            "scripts/upload_reportify_pdf_to_r2.py",
            "scripts/mark_reportify_pdf_status.py",
            "scripts/sanitize_pdf_links.py",
        ):
            with self.subTest(path=path):
                self.assertIn(path, paths)
        self.assertIn("python3 -B scripts/test_reportify_api_grab.py", self.workflow)

    def test_validation_fixtures_and_their_transitive_imports_are_in_sparse_checkout(self) -> None:
        sparse = self.workflow.split("sparse-checkout: |", 1)[1].split("\n      - name:", 1)[0]
        paths = {line.strip() for line in sparse.splitlines() if line.strip()}
        # daily-source-wakeup.test.mjs imports the independent clock, while
        # customer-content's real export/readback fixture imports the completed
        # source and editorial validation helpers. These are validation inputs,
        # not additional Workers or publishing commands to deploy.
        required = {"workers/daily-source-wakeup/src"}
        required.update("scripts/" + name + ".py" for name in (
            "test_publish_customer_content", "test_reuse_completed_progressive_sources",
            "test_progressive_wechat_delivery", "progressive_wechat_delivery",
            "reuse_completed_progressive_sources", "recovered_article_delivery",
            "market_views_partial_sources", "report_extraction_source", "portal_translation_shards",
            "run_pdf_to_xhs_in_batches", "private_workflow_handoff", "publish_customer_content",
            "push_xhs_notes_to_wechat_drafts", "push_portal_translated_to_wechat_drafts",
            "portal_discovery_quality", "deepseek_http", "deepseek_usage", "free_editorial_images",
            "institution_names", "sensitive_content_guard", "title_source_claim_support",
            "verify_existing_wechat_drafts", "wechat_account_routing", "wechat_accounts",
            "wechat_article_quality", "wechat_draft_grouping", "wechat_editorial_binding",
            "wechat_image_quality", "wechat_title_optimizer",
        ))
        self.assertEqual(required - paths, set())
        for path in required:
            self.assertTrue((ROOT / path).exists(), path)
        validation = self.workflow.split("- name: Validate legacy access compatibility", 1)[1].split(
            "- name: Materialize private deployment values", 1)[0]
        self.assertIn('"requests>=2.31,<3"', validation)
        self.assertIn('python3 -B scripts/test_publish_customer_content.py', validation)
        self.assertEqual(self.workflow.count('workers/daily-source-wakeup/src'), 1)
        deployment = self.workflow.split('- name: Materialize private deployment values', 1)[1]
        self.assertNotIn('daily-source-wakeup', deployment)
        self.assertNotIn('push_xhs_notes_to_wechat_drafts.py', deployment)

    def test_materialized_public_site_is_brand_checked_before_worker_upload(self) -> None:
        self.assertIn("scripts/check_public_brand.py", self.workflow)
        self.assertIn("scripts/test_check_public_brand.py", self.workflow)
        self.assertIn("scripts/test_render_private_config.py", self.workflow)
        self.assertIn("python3 -B scripts/test_render_private_config.py", self.workflow)
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
        materialized_section = self.workflow[materialize:brand_check]
        self.assertIn("--forbid-profile-private-for admin-a", materialized_section)
        self.assertIn(
            "--forbid-profile-private-for admin-a@users.portal.example.invalid",
            materialized_section,
        )
        self.assertNotIn(
            "check_public_brand.py workers/portal-suite-worker/src",
            self.workflow,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
