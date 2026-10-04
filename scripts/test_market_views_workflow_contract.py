#!/usr/bin/env python3
"""Guard dependency isolation and input lifetime for every Dropbox R2 consumer."""

import re
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


WORKFLOWS = Path(__file__).resolve().parents[1] / ".github/workflows"
UPSTREAM = WORKFLOWS / "dropbox-latest-pdf-to-xhs-sharded.yml"
MARKET = WORKFLOWS / "market-views-latex-pdf.yml"


def job(path, name):
    text = path.read_text(encoding="utf-8")
    return re.search(
        rf"(?ms)^  {re.escape(name)}:\n(.*?)(?=^  [\w-]+:\n|\Z)", text
    ).group(1)


def gate(block, results, *, selected="64", cancelled=False, plan=None):
    expression = re.search(r"(?s)\bif:.*?\$\{\{(.*?)\}\}", block).group(1)
    expression = expression.replace("needs.*.result", repr(list(results.values())))
    expression = re.sub(
        r"needs\.([\w-]+)\.result", lambda m: repr(results.get(m[1], "skipped")), expression
    )
    expression = expression.replace(
        "needs.select-macro-reports.outputs.selected_count", repr(selected)
    )
    options = {
        "wechat_draft_upload": "true", "wechat_draft_source": "xhs_notes",
        "translated_report_count": "3",
        **(plan or {}),
    }
    expression = re.sub(
        r"needs\.resolve-inputs\.outputs\.(\w+)",
        lambda m: repr(options[m[1]]), expression,
    )
    expression = expression.replace("vars.CHART_SEARCH_ENABLED", repr("true"))
    expression = expression.replace("always()", "True")
    expression = expression.replace("cancelled()", repr(cancelled))
    expression = expression.replace("&&", " and ").replace("||", " or ")
    expression = re.sub(r"!(?!=)", " not ", expression)
    return eval(" ".join(expression.split()), {"__builtins__": {}}, {
        "contains": lambda values, value: value in values,
    })


class MarketViewsWorkflowContractTests(unittest.TestCase):
    def test_every_r2_consumer_is_isolated_and_participates_in_cleanup(self):
        blocks = dict(re.findall(
            r"(?ms)^  ([\w-]+):\n(.*?)(?=^  [\w-]+:\n|\Z)",
            UPSTREAM.read_text(encoding="utf-8"),
        ))
        consumers = {
            name: block for name, block in blocks.items()
            if "private_workflow_handoff.py download-shards" in block
            or "-f source_handoff_run_id=" in block
        }
        self.assertTrue(consumers, "No producer handoff consumers were found")
        cleanup = blocks["cleanup-private-handoff"]
        cleanup_needs = re.search(r"(?s)needs:\n(.*?)    if:", cleanup).group(1)
        cleanup_results = dict.fromkeys(re.findall(r"(?m)^      - ([\w-]+)$", cleanup_needs), "success")
        self.assertTrue(gate(cleanup, cleanup_results))
        for name, block in consumers.items():
            with self.subTest(consumer=name):
                needs = re.search(r"needs: \[(.*?)\]", block).group(1).split(", ")
                self.assertIn("process-shard", needs)
                self.assertNotIn("package-publish-ready", needs)
                if "private_workflow_handoff.py download-shards" in block:
                    self.assertIn('--expected-count "${{ needs.select-macro-reports.outputs.effective_shard_count }}"', block)
                else:
                    self.assertIn("EXPECTED_SHARDS: ${{ needs.select-macro-reports.outputs.effective_shard_count }}", block)
                    self.assertIn('-f expected_shards="$EXPECTED_SHARDS"', block)
                self.assertIn(f"      - {name}\n", blocks["cleanup-private-handoff"])
                self.assertIn(f"      - {name}\n", blocks["notify-failure"])
                for status in ("failure", "cancelled"):
                    self.assertFalse(gate(cleanup, {**cleanup_results, name: status}))
                for package in ("success", "failure", "cancelled", "skipped"):
                    self.assertTrue(gate(block, {
                        "process-shard": "success", "package-publish-ready": package,
                    }))
                for shards in ("failure", "cancelled", "skipped"):
                    self.assertFalse(gate(block, {"process-shard": shards}))
                self.assertFalse(gate(block, {"process-shard": "success"}, cancelled=True))

    def test_optional_outputs_keep_user_selection_gates(self):
        results = {"process-shard": "success", "translate-report-shard": "success"}
        drafts = job(UPSTREAM, "push-xhs-notes-wechat-drafts")
        self.assertFalse(gate(drafts, results, plan={"wechat_draft_upload": "false"}))
        self.assertFalse(gate(drafts, results, plan={"wechat_draft_source": "portal_translated"}))
        translated = job(UPSTREAM, "build-portal-translated-reports")
        self.assertFalse(gate(translated, results, plan={"translated_report_count": "0"}))
        # This branch actually consumes translated artifacts, so it must keep
        # its dependency on their producer rather than on the raw R2 shards.
        translated_drafts = job(UPSTREAM, "push-portal-translated-wechat-drafts")
        needs = re.search(r"needs: \[(.*?)\]", translated_drafts).group(1).split(", ")
        self.assertIn("build-portal-translated-reports", needs)

    def test_zip_timeout_cannot_suppress_complete_shards(self):
        trigger = job(UPSTREAM, "trigger-market-views")
        needs = re.search(r"needs: \[(.*?)\]", trigger).group(1).split(", ")
        self.assertIn("process-shard", needs)
        self.assertNotIn("package-publish-ready", needs)
        for package in ("success", "failure", "cancelled", "skipped"):
            with self.subTest(package=package):
                self.assertTrue(gate(trigger, {
                    "process-shard": "success", "package-publish-ready": package,
                }))
        for shards in ("failure", "cancelled", "skipped"):
            self.assertFalse(gate(trigger, {"process-shard": shards}))
        self.assertFalse(gate(trigger, {"process-shard": "success"}, selected="0"))
        self.assertFalse(gate(trigger, {"process-shard": "success"}, cancelled=True))

    def test_r2_consumer_validates_producer_shard_count(self):
        trigger = job(UPSTREAM, "trigger-market-views")
        self.assertIn("EXPECTED_SHARDS: ${{ needs.select-macro-reports.outputs.effective_shard_count }}", trigger)
        self.assertIn('-f expected_shards="$EXPECTED_SHARDS"', trigger)
        market = MARKET.read_text(encoding="utf-8")
        download = market.split("- name: Download bank inputs from private R2", 1)[1].split("\n      - name:", 1)[0]
        self.assertIn("EXPECTED_SHARDS: ${{ inputs.expected_shards || '0' }}", download)
        self.assertIn('--expected-count "$EXPECTED_SHARDS"', download)
        self.assertIn('gh run watch "$MARKET_RUN_ID"', trigger)

    def test_complete_native_sources_restore_pdf_after_failed_notes_without_unblocking_drafts(self):
        recovery = job(UPSTREAM, "recover-market-sources")
        results = {"select-macro-reports": "success", "process-shard": "failure"}
        self.assertTrue(gate(recovery, results))
        for status in ("success", "cancelled", "skipped"):
            self.assertFalse(gate(recovery, {**results, "process-shard": status}))
        self.assertFalse(gate(recovery, results, cancelled=True))
        self.assertIn("--manifest _selected_macro_pdfs/selected_to_process_manifest.json", recovery)
        self.assertIn('--expected-reports "${{ needs.select-macro-reports.outputs.selected_count }}"', recovery)
        self.assertNotIn("MINER_U:", recovery)
        self.assertNotIn("DEEPSEEK_API_KEY:", recovery)
        trigger = job(UPSTREAM, "trigger-market-views")
        for status in ("failure", "cancelled", "skipped"):
            self.assertFalse(gate(trigger, {**results, "recover-market-sources": status}))
        results["recover-market-sources"] = "success"
        self.assertTrue(gate(trigger, results))
        self.assertFalse(gate(job(UPSTREAM, "push-xhs-notes-wechat-drafts"), results))
        self.assertIn('SOURCE_KIND=native-pdf', trigger)
        self.assertIn('-f source_handoff_kind="$SOURCE_KIND"', trigger)
        self.assertIn('-f expected_articles="$EXPECTED_ARTICLES"', trigger)
        self.assertIn('-f date_folder="$DATE_FOLDER"', trigger)
        self.assertNotIn('-f date_folder=latest', trigger)

    def test_native_receipt_is_checked_before_idempotency_or_paid_synthesis(self):
        market = MARKET.read_text()
        receipt = market.index("- name: Verify complete native PDF source receipt")
        resolve = market.index("- name: Resolve and validate primary bank source")
        build = market.index("- name: Build market views data and LaTeX source")
        self.assertLess(receipt, resolve)
        self.assertLess(resolve, build)
        block = market[receipt:resolve]
        self.assertIn("extract_native_market_sources.py validate", block)
        self.assertIn('--expected-reports "${{ inputs.expected_articles }}"', block)

    def test_native_archive_is_released_only_after_its_pdf_consumer_succeeds(self):
        cleanup = job(UPSTREAM, "cleanup-market-source-recovery")
        self.assertTrue(gate(cleanup, {"recover-market-sources": "success", "trigger-market-views": "success"}))
        for consumer in ("failure", "cancelled", "skipped"):
            self.assertFalse(gate(cleanup, {"recover-market-sources": "success", "trigger-market-views": consumer}))
        self.assertFalse(gate(cleanup, {"recover-market-sources": "success", "trigger-market-views": "success"}, cancelled=True))
        recovery = (WORKFLOWS / "market-views-native-recovery.yml").read_text()
        self.assertLess(recovery.index('gh run watch "$MARKET_RUN_ID"'),
                        recovery.index('name: Delete consumed native source handoff'))

    def test_actual_private_input_validation_rejects_shell_metacharacters_in_run_ids(self):
        step = MARKET.read_text().split("- name: Validate private input source", 1)[1].split("\n      - name:", 1)[0]
        command = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory() as temp:
            sentinel = Path(temp) / "should-not-exist"
            environment = {**os.environ, "SOURCE_HANDOFF_RUN_ID": f"999$(touch {sentinel})",
                           "SOURCE_ARTIFACT_RUN_ID": "", "EXPECTED_BANK_DATE": "261003",
                           "SOURCE_HANDOFF_KIND": "native-pdf", "EXPECTED_SHARDS": "1", "EXPECTED_ARTICLES": "54"}
            result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                    env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(sentinel.exists())
            self.assertIn("run ids must be positive integers", result.stderr)
            environment["SOURCE_HANDOFF_RUN_ID"] = "37159099752"
            result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                    env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_actual_resolver_cannot_skip_new_bank_batch_because_of_future_auxiliary_pdf(self):
        market = MARKET.read_text()
        step = market.split("- name: Resolve and validate primary bank source", 1)[1].split("\n      - name:", 1)[0]
        command = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "scripts").symlink_to(WORKFLOWS.parents[1] / "scripts", target_is_directory=True)
            for source, date in (("dropbox", "261003"), ("institutions", "261004")):
                report = root / "xhs_notes" / source / date / "report"
                report.mkdir(parents=True)
                (report / "source_native_pdf.md").write_text("# Exact source report")
            existing = root / "market_view_summaries/261004/market_views_261004.pdf"
            existing.parent.mkdir(parents=True)
            existing.write_bytes(b"%PDF-" + b"x" * 2048)
            binaries = root / "bin"
            binaries.mkdir()
            (binaries / "python").symlink_to(sys.executable)
            env_file = root / "env"
            environment = {**os.environ, "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
                           "GITHUB_ENV": str(env_file), "REQUESTED_DATE_FOLDER": "latest",
                           "EXPECTED_BANK_DATE": "261003", "EXPECTED_ARTICLES": "1", "FORCE_REBUILD": "false"}
            result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                    cwd=root, env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["BUILD_DATE_FOLDER"], "261003")
            self.assertEqual(values["DATE_FOLDER"], "261003")
            self.assertEqual(values["SHOULD_BUILD"], "true")
            environment["EXPECTED_ARTICLES"] = "2"
            result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                    cwd=root, env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Expected 2 bank reports, received 1", result.stderr)
            environment["EXPECTED_ARTICLES"] = "1"
            same_date = root / "market_view_summaries/261003/market_views_261003.pdf"
            same_date.parent.mkdir(parents=True)
            same_date.write_bytes(existing.read_bytes())
            env_file.write_text("")
            result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                    cwd=root, env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["SHOULD_BUILD"], "false")
            environment["FORCE_REBUILD"] = "true"
            env_file.write_text("")
            result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                    cwd=root, env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["SHOULD_BUILD"], "true")

    def test_scheduled_daily_flow_rejects_stale_dropbox_folders(self):
        workflow = UPSTREAM.read_text(encoding="utf-8")
        self.assertIn(
            "expected_dropbox_date_folder: ${{ steps.vars.outputs.expected_dropbox_date_folder }}",
            workflow,
        )
        self.assertIn('TZ=Asia/Shanghai date +%y%m%d', workflow)
        self.assertIn(
            '--expected-date-folder "$EXPECTED_DATE"',
            workflow,
        )

    def test_cleanup_retains_inputs_for_failed_or_cancelled_consumers(self):
        cleanup = job(UPSTREAM, "cleanup-private-handoff")
        results = {name: "success" for name in (
            "package-publish-ready", "trigger-market-views", "trigger-chart-search-index",
            "push-xhs-notes-wechat-drafts", "build-portal-translated-reports",
            "push-portal-translated-wechat-drafts",
        )}
        self.assertTrue(gate(cleanup, results))
        for name in results:
            for status in ("failure", "cancelled"):
                with self.subTest(name=name, status=status):
                    self.assertFalse(gate(cleanup, {**results, name: status}))
        self.assertFalse(gate(cleanup, {**results, "trigger-market-views": "skipped"}))
        for name in ("push-xhs-notes-wechat-drafts", "build-portal-translated-reports", "push-portal-translated-wechat-drafts"):
            results[name] = "skipped"
        self.assertTrue(gate(cleanup, results))

    def test_timeout_cancellation_reaches_existing_alert_policy(self):
        for workflow in (UPSTREAM, MARKET):
            notify = job(workflow, "notify-failure")
            for status in ("failure", "cancelled"):
                self.assertTrue(gate(notify, {"job": status}, cancelled=status == "cancelled"))
            for status in ("success", "skipped"):
                self.assertFalse(gate(notify, {"job": status}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
