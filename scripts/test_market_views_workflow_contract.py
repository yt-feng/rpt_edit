#!/usr/bin/env python3
"""Guard dependency isolation and input lifetime for every Dropbox R2 consumer."""

import ast
import contextlib
import io
import json
import re
import shlex
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock


WORKFLOWS = Path(__file__).resolve().parents[1] / ".github/workflows"
UPSTREAM = WORKFLOWS / "dropbox-latest-pdf-to-xhs-sharded.yml"
MARKET = WORKFLOWS / "market-views-latex-pdf.yml"
NOTICE_RECOVERY = WORKFLOWS / "market-views-notice-recovery.yml"



def test_python_environment(binaries):
    """Keep the parent interpreter and resolved dependencies in nested CLIs."""
    wrapper = binaries / "python"
    # A symlink outside a venv can lose its pyvenv.cfg. Exec the original path
    # instead, and preserve dependency paths added by a test runtime launcher.
    wrapper.write_text("#!/bin/sh\nexec " + shlex.quote(sys.executable) + ' "$@"\n')
    wrapper.chmod(0o755)
    return {
        "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
        "PYTHONPATH": os.pathsep.join(str(Path(entry).resolve()) for entry in sys.path if entry),
    }


def make_readable_pdf(path, label="Actual generated research summary"):
    """Use a real multi-page PDF for the resolver's render/readability gate."""
    import fitz
    with fitz.open() as document:
        for number in range(1, 3):
            page = document.new_page()
            page.insert_text((40, 50), f"{label} - page {number}\nSource analysis and observations.")
            page.draw_rect(fitz.Rect(40, 90, 500, 180), color=(0.2, 0.3, 0.7))
        document.save(path)
    return path.read_bytes()


def run_actual_market_resolver(root, environment, client):
    """Run the actual workflow Python, replacing only the external R2 client."""
    import upload_market_view_to_r2 as uploader
    step = MARKET.read_text().split("- name: Resolve and validate primary bank source", 1)[1].split("\n      - name:", 1)[0]
    command = textwrap.dedent(step.split("        run: |\n", 1)[1])
    program = command.split("python - <<'PYTHON'\n", 1)[1].rsplit("\nPYTHON", 1)[0]
    stdout, stderr = io.StringIO(), io.StringIO()
    previous_path = list(sys.path)
    returncode = 0
    try:
        with contextlib.chdir(root), mock.patch.dict(os.environ, environment, clear=True), \
                mock.patch.object(uploader, "build_r2_client", return_value=client), \
                contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                exec(compile(program, str(MARKET), "exec"), {"__name__": "__main__"})
            except (Exception, SystemExit) as exc:
                returncode = 1
                print(str(exc), file=stderr)
    finally:
        sys.path[:] = previous_path
    return subprocess.CompletedProcess(["actual-workflow-resolver"], returncode, stdout.getvalue(), stderr.getvalue())


def job(path, name):
    text = path.read_text(encoding="utf-8")
    return re.search(
        rf"(?ms)^  {re.escape(name)}:\n(.*?)(?=^  [\w-]+:\n|\Z)", text
    ).group(1)


def gate(block, results, *, selected="64", cancelled=False, plan=None, primary_ready=None, provider_only="false",
         steps=None, prior_steps_success=True, chart_enabled="true", recovery_kind="mineru-recovery",
         recovery_outputs=None):
    expression = re.search(r"(?s)\bif:.*?\$\{\{(.*?)\}\}", block).group(1)
    # GitHub adds success() when an expression has no explicit status function.
    # A continue-on-error step has failure outcome but successful conclusion;
    # callers model that distinction with steps and prior_steps_success.
    if not re.search(r'\b(?:always|cancelled|failure|success)\s*\(', expression):
        if cancelled or not prior_steps_success:
            return False
    expression = expression.replace("needs.*.result", repr(list(results.values())))
    expression = re.sub(
        r"needs\.([\w-]+)\.result", lambda m: repr(results.get(m[1], "skipped")), expression
    )
    expression = expression.replace(
        "needs.select-macro-reports.outputs.selected_count", repr(selected)
    )
    if primary_ready is None:
        primary_ready = {"success": "true", "failure": "false"}.get(results.get("process-shard"), "")
    expression = expression.replace("needs.source-outcome.outputs.primary_ready", repr(primary_ready))
    expression = expression.replace("needs.source-outcome.outputs.provider_only", repr(provider_only))
    expression = expression.replace("needs.recover-market-sources.outputs.source_kind", repr(recovery_kind))
    expression = re.sub(r"needs\.recover-market-sources\.outputs\.(\w+)",
                        lambda m: repr((recovery_outputs or {}).get(m[1], '')), expression)
    options = {
        "wechat_draft_upload": "true", "wechat_draft_source": "xhs_notes",
        "translated_report_count": "3", "replay_source_run_id": "",
        **(plan or {}),
    }
    expression = re.sub(
        r"needs\.resolve-inputs\.outputs\.(\w+)",
        lambda m: repr(options[m[1]]), expression,
    )
    expression = re.sub(r"steps\.([\w-]+)\.outcome",
                        lambda m: repr((steps or {}).get(m[1], "skipped")), expression)
    expression = expression.replace("vars.CHART_SEARCH_ENABLED", repr(chart_enabled))
    expression = expression.replace("always()", "True")
    expression = expression.replace("cancelled()", repr(cancelled))
    expression = expression.replace("&&", " and ").replace("||", " or ")
    expression = re.sub(r"!(?!=)", " not ", expression)
    return eval(" ".join(expression.split()), {"__builtins__": {}}, {
        "contains": lambda values, value: value in values,
    })


class MarketViewsWorkflowContractTests(unittest.TestCase):
    def test_acceptance_runs_have_independent_queues_while_publications_remain_serialized(self):
        from types import SimpleNamespace
        text = MARKET.read_text(encoding="utf-8")
        block = text.split("\nconcurrency:\n", 1)[1].split("\njobs:\n", 1)[0]
        expression = re.search(r"group: \$\{\{(.*?)\}\}", block).group(1)
        expression = expression.replace("true", "True").replace("&&", " and ").replace("||", " or ")
        def group(acceptance, run_id):
            return eval(expression, {"__builtins__": {}}, {
                "inputs": SimpleNamespace(acceptance_only=acceptance),
                "github": SimpleNamespace(run_id=run_id),
                "format": lambda pattern, value: pattern.format(value),
            })
        self.assertEqual(group(False, "100"), "market-views-daily-pdf")
        self.assertEqual(group(False, "101"), group(False, "100"))
        self.assertEqual(group(None, "102"), "market-views-daily-pdf")
        self.assertNotEqual(group(True, "100"), group(True, "101"))
        self.assertNotEqual(group(True, "100"), group(False, "100"))
        self.assertIn("100", group(True, "100"))
        self.assertIn("cancel-in-progress: false", block)

    def test_acceptance_pdf_keeps_complete_build_gates_and_skips_every_publish_write(self):
        market = MARKET.read_text(encoding="utf-8")
        input_block = market.split("      acceptance_only:\n", 1)[1].split("\npermissions:", 1)[0]
        self.assertIn("type: boolean", input_block)
        self.assertIn("default: false", input_block)
        steps = dict(re.findall(r"(?ms)^      - name: ([^\n]+)\n(.*?)(?=^      - name: |^  [\w-]+:|\Z)", market))

        def enabled(name, acceptance, *, should_build="true", public_pdf="success"):
            expression = re.search(r"if: \$\{\{(.*?)\}\}", steps[name]).group(1)
            expression = expression.replace("true", "True").replace("&&", " and ").replace("||", " or ")
            expression = expression.replace("inputs.acceptance_only", repr(acceptance))
            expression = expression.replace("inputs.source_handoff_kind", repr("native-pdf"))
            expression = expression.replace("env.SHOULD_BUILD", repr(should_build))
            expression = expression.replace("steps.public_pdf.conclusion", repr(public_pdf))
            return eval(expression, {"__builtins__": {}}, {
                "always": lambda: True, "hashFiles": lambda path: "available",
            })

        writes = [name for name, block in steps.items()
                  if "scripts/upload_market_view_to_r2.py" in block or "scripts/commit_output_dir.sh" in block]
        self.assertEqual(set(writes), {"Archive exact Market Views PDF in private R2",
                                     "Commit public-safe Market Views PDF to main"})
        for name in writes:
            self.assertIn("inputs.acceptance_only != true", steps[name])
            self.assertNotIn("||", re.search(r"if:.*", steps[name]).group(0))
            self.assertFalse(enabled(name, True))
            self.assertTrue(enabled(name, False))
            self.assertFalse(enabled(name, False, should_build="false"))
        for name in ("Verify complete native PDF source receipt", "Verify complete MinerU recovery source receipt",
                     "Verify complete accepted legacy Daily source receipt", "Build market views data and LaTeX source",
                     "Render fast PDF without LaTeX install", "Verify PDF exists before upload and commit",
                     "Prepare public-safe Market Views PDF"):
            self.assertNotIn("acceptance_only", steps[name])
        prepared = steps["Prepare public-safe Market Views PDF"]
        self.assertIn("id: public_pdf", prepared)
        self.assertLess(prepared.index("scripts/prepare_public_market_view_pdf.py"),
                        prepared.index("scripts/check_public_identity.py"))

        artifact = steps["Preserve public-safe acceptance PDF"]
        self.assertTrue(enabled("Preserve public-safe acceptance PDF", True))
        self.assertFalse(enabled("Preserve public-safe acceptance PDF", False))
        for conclusion in ("failure", "cancelled", "skipped", ""):
            self.assertFalse(enabled("Preserve public-safe acceptance PDF", True, public_pdf=conclusion))
        self.assertFalse(enabled("Preserve public-safe acceptance PDF", True, should_build="false"))
        self.assertIn("uses: actions/upload-artifact@v4", artifact)
        self.assertEqual(re.search(r"(?m)^          path: (.+)$", artifact).group(1),
                         "market_view_summaries/${{ env.DATE_FOLDER }}/market_views_${{ env.DATE_FOLDER }}.pdf")
        self.assertIn("if-no-files-found: error", artifact)
        self.assertIn("retention-days: 1", artifact)
        self.assertNotIn("always()", artifact)
        for name, block in steps.items():
            if "actions/upload-artifact@" in block or "resilient-diagnostic-artifact" in block:
                if name != "Preserve public-safe acceptance PDF":
                    self.assertIn("inputs.acceptance_only != true", block)
                    self.assertFalse(enabled(name, True))
                    self.assertTrue(enabled(name, False))

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
                    if name == 'plan-portal-translated-reports':
                        self.assertIn('--expected-count "$EXPECTED_SHARDS"', block)
                        self.assertIn('EXPECTED_SHARDS=1', block)
                    else:
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

    def test_recovered_articles_feed_requested_translations_without_duplicate_primary_drafts(self):
        delivery = job(UPSTREAM, 'deliver-recovered-report-articles')
        planner = job(UPSTREAM, 'plan-portal-translated-reports')
        results = {'process-shard': 'success', 'recover-market-sources': 'success'}
        self.assertTrue(gate(delivery, results, primary_ready='false'))
        self.assertFalse(gate(delivery, results, primary_ready='true'))
        self.assertFalse(gate(delivery, results, primary_ready='false', cancelled=True))
        self.assertFalse(gate(delivery, results, primary_ready='false',
                              plan={'wechat_draft_upload': 'false', 'translated_report_count': '0'}, chart_enabled='false'))
        self.assertFalse(gate(delivery, results, primary_ready='false',
                              plan={'replay_source_run_id': '123'}))
        for outcome in ('success', 'failure', 'cancelled', 'skipped'):
            restored = {**results, 'deliver-recovered-report-articles': outcome}
            self.assertEqual(gate(planner, restored, primary_ready='false'), outcome == 'success')
            self.assertFalse(gate(job(UPSTREAM, 'push-xhs-notes-wechat-drafts'),
                                  restored, primary_ready='false'))
        self.assertIn('needs.deliver-recovered-report-articles.outputs.article_handoff_prefix', planner)
        materialize = job(UPSTREAM, 'translate-report-shard')
        self.assertIn('--prefix "${{ needs.plan-portal-translated-reports.outputs.source_prefix }}"', materialize)
        restored = {**results, 'deliver-recovered-report-articles': 'success'}
        chart = job(UPSTREAM, 'trigger-chart-search-index')
        self.assertTrue(gate(chart, restored, primary_ready='false', recovery_kind='mineru-recovery'))
        self.assertFalse(gate(chart, restored, primary_ready='false', recovery_kind='ocr-synthesis'))
        self.assertFalse(gate(chart, restored, primary_ready='false', chart_enabled='false'))
        self.assertIn('-f source_handoff_manifest_sha256="$MANIFEST_SHA"', chart)

    def test_actual_article_gate_rejects_green_pdf_with_skipped_required_outputs(self):
        block = job(UPSTREAM, 'validate-report-delivery')
        program = textwrap.dedent(block.split('        run: |\n', 1)[1])
        base = {'SELECTION_RESULT': 'success', 'SOURCE_STATUS': 'success', 'SELECTED_COUNT': '40',
                'NO_WORK': 'false', 'PRIMARY_READY': 'false', 'RECOVERED_DELIVERY': 'success',
                'WECHAT_ENABLED': 'true', 'WECHAT_SOURCE': 'xhs_notes', 'WECHAT_RESULT': 'skipped',
                'TRANSLATION_COUNT': 'all', 'TRANSLATION_RESULT': 'success',
                'TRANSLATED_WECHAT_RESULT': 'skipped'}
        cases = [({}, True), ({'RECOVERED_DELIVERY': 'skipped'}, False),
                 ({'RECOVERED_DELIVERY': 'failure'}, False),
                 ({'TRANSLATION_RESULT': 'skipped'}, False),
                 ({'TRANSLATION_RESULT': 'failure'}, False),
                 ({'WECHAT_SOURCE': 'portal_translated'}, False),
                 ({'WECHAT_SOURCE': 'portal_translated', 'TRANSLATED_WECHAT_RESULT': 'success'}, True),
                 ({'PRIMARY_READY': 'true'}, False),
                 ({'PRIMARY_READY': 'true', 'WECHAT_RESULT': 'success'}, True),
                 ({'TRANSLATION_COUNT': '0', 'TRANSLATION_RESULT': 'skipped'}, True),
                 ({'WECHAT_ENABLED': 'false', 'RECOVERED_DELIVERY': 'skipped',
                   'TRANSLATION_COUNT': '0', 'TRANSLATION_RESULT': 'skipped'}, True),
                 ({'SELECTED_COUNT': '0', 'NO_WORK': 'true'}, True),
                 ({'SELECTED_COUNT': '0'}, False)]
        for changed, succeeds in cases:
            with self.subTest(changed=changed):
                result = subprocess.run(['bash', '-e', '-c', program],
                    env={**os.environ, **base, **changed}, capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, succeeds, result.stderr)
        self.assertIn('validate-report-delivery', job(UPSTREAM, 'notify-failure'))

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

    def test_recovered_sources_need_article_generation_before_unblocking_drafts(self):
        recovery = job(UPSTREAM, "recover-market-sources")
        results = {"select-macro-reports": "success", "process-shard": "failure"}
        self.assertTrue(gate(recovery, results))
        for status in ("success", "cancelled", "skipped"):
            self.assertFalse(gate(recovery, {**results, "process-shard": status}))
        self.assertFalse(gate(recovery, results, cancelled=True))
        self.assertIn("--manifest _selected_macro_pdfs/selected_to_process_manifest.json", recovery)
        self.assertIn('EXPECTED_ARTICLES: ${{ needs.select-macro-reports.outputs.selected_count }}', recovery)
        self.assertIn('--expected-reports "$EXPECTED_ARTICLES"', recovery)
        mineru = recovery.split('- name: Recover existing MinerU tasks for daily Market Views', 1)[1].split('\n      - name:', 1)[0]
        synthesis = recovery.split('- name: Build complete OCR summaries and charts for Market Views', 1)[1].split('\n      - name:', 1)[0]
        self.assertIn('MINER_U: ${{ secrets.MINER_U }}', mineru)
        self.assertNotIn('DEEPSEEK_API_KEY:', mineru)
        self.assertIn('DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_MARKET_VIEWS_API_KEY }}', synthesis)
        self.assertNotIn('MINER_U:', synthesis)
        trigger = job(UPSTREAM, "trigger-market-views")
        for status in ("failure", "cancelled", "skipped"):
            self.assertFalse(gate(trigger, {**results, "recover-market-sources": status}))
        results["recover-market-sources"] = "success"
        self.assertTrue(gate(trigger, results))
        self.assertFalse(gate(job(UPSTREAM, "push-xhs-notes-wechat-drafts"), results))
        self.assertTrue(gate(job(UPSTREAM, "deliver-recovered-report-articles"), results))
        self.assertIn('SOURCE_KIND="$RECOVERY_KIND"', trigger)
        self.assertIn('-f source_handoff_kind="$SOURCE_KIND"', trigger)
        self.assertIn('-f expected_articles="$EXPECTED_ARTICLES"', trigger)
        self.assertIn('-f date_folder="$DATE_FOLDER"', trigger)
        self.assertNotIn('-f date_folder=latest', trigger)

    def test_continue_on_error_uses_observed_shard_outcomes_and_requires_real_delivery(self):
        self.assertIn('continue-on-error: true', job(UPSTREAM, 'process-shard'))
        recovered = {'select-macro-reports': 'success', 'process-shard': 'success'}
        self.assertTrue(gate(job(UPSTREAM, 'recover-market-sources'), recovered, primary_ready='false'))
        self.assertFalse(gate(job(UPSTREAM, 'trigger-market-views'), recovered, primary_ready='false'))
        self.assertFalse(gate(job(UPSTREAM, 'push-xhs-notes-wechat-drafts'), recovered, primary_ready='false'))
        self.assertTrue(gate(job(UPSTREAM, 'trigger-market-views'),
                             {**recovered, 'recover-market-sources': 'success'}, primary_ready='false'))
        final = job(UPSTREAM, 'validate-market-delivery')
        self.assertIn('test "$DELIVERY_RESULT" = success', final)
        self.assertIn('needs.trigger-market-views.result', final)
        self.assertIn('validate-market-delivery', job(UPSTREAM, 'notify-failure'))
        recovery = job(UPSTREAM, 'recover-market-sources')
        self.assertIn('recover_daily_mineru_sources.py', recovery)
        self.assertIn('build_market_views_ocr_fallback.py', recovery)
        self.assertIn('source_kind=mineru-recovery', recovery)
        self.assertIn('source_kind=ocr-synthesis', recovery)
        self.assertNotIn('market_views_source_preview.py', recovery)
        self.assertNotIn('source_kind=source-pages', recovery)
        self.assertNotIn('--mineru-retries', recovery)

    def test_bounded_mineru_recovery_leaves_time_for_complete_ocr_synthesis(self):
        recovery = job(UPSTREAM, 'recover-market-sources')
        self.assertIn('timeout-minutes: 180', recovery)
        names = [('Recover existing MinerU tasks for daily Market Views', 30),
                 ('Save complete recovered MinerU sources to private R2', 5),
                 ('Install complete cloud OCR synthesis dependencies', 5),
                 ('Build complete OCR summaries and charts for Market Views', 90),
                 ('Save complete OCR synthesis to private R2', 5)]
        blocks = {}
        for name, timeout in names:
            block = recovery.split('- name: ' + name, 1)[1].split('\n      - name:', 1)[0]
            blocks[name] = block
            self.assertIn(f'timeout-minutes: {timeout}', block)
            if name == names[0][0]:
                self.assertIn('continue-on-error: true', block)
            else:
                self.assertNotIn('continue-on-error:', block)
        mineru = blocks[names[0][0]]
        self.assertIn('--timeout 1740', mineru)
        self.assertIn("needs.resolve-inputs.outputs.replay_source_run_id == ''", mineru)
        self.assertNotIn('provider_only', mineru)
        self.assertIn("steps.mineru-recover.outcome == 'success'", blocks[names[1][0]])
        self.assertIn("steps.mineru-recover.outcome == 'failure'", blocks[names[3][0]])
        self.assertIn("steps.ocr-synthesis.outcome == 'success'", blocks[names[4][0]])
        self.assertIn('_private-workflow-handoff/mineru-market-sources/', blocks[names[1][0]])
        self.assertIn('_private-workflow-handoff/market-ocr-synthesis/', blocks[names[4][0]])
        self.assertLess(recovery.index(names[0][0]), recovery.index(names[1][0]))
        self.assertLess(recovery.index(names[3][0]), recovery.index(names[4][0]))

    def test_normal_recovery_precedes_ocr_for_provider_generation_and_pending_segment_failures(self):
        recovery = job(UPSTREAM, 'recover-market-sources')
        def block(name):
            return recovery.split('- name: ' + name, 1)[1].split('\n      - name:', 1)[0]
        mineru = block('Recover existing MinerU tasks for daily Market Views')
        ocr = [block(name) for name in ('Install complete cloud OCR synthesis dependencies',
               'Restore private source-bound OCR synthesis cache',
               'Build complete OCR summaries and charts for Market Views')]
        results = {'resolve-inputs': 'success', 'select-macro-reports': 'success', 'process-shard': 'success'}
        for failure, provider_only in [('provider', 'true'), ('article_generation', 'false'),
                                       ('pending_page_segment', 'false')]:
            with self.subTest(failure=failure):
                self.assertTrue(gate(recovery, results, primary_ready='false', provider_only=provider_only))
                self.assertTrue(gate(mineru, results, provider_only=provider_only))
            for outcome in ('success', 'failure', 'skipped', 'cancelled', 'timed_out', ''):
                for step in ocr:
                    with self.subTest(failure=failure, outcome=outcome):
                        self.assertEqual(gate(step, results, provider_only=provider_only,
                            steps={'mineru-recover': outcome}), outcome == 'failure')
            for step in [mineru, *ocr]:
                for stopped in ({'cancelled': True}, {'prior_steps_success': False}):
                    self.assertFalse(gate(step, results, provider_only=provider_only,
                        steps={'mineru-recover': 'failure'}, **stopped))

    def test_frozen_replay_has_separate_provider_proven_ocr_route_without_mineru_recovery(self):
        recovery = job(UPSTREAM, 'recover-market-sources')
        def block(name):
            return recovery.split('- name: ' + name, 1)[1].split('\n      - name:', 1)[0]
        mineru = block('Recover existing MinerU tasks for daily Market Views')
        ocr = [block(name) for name in ('Install complete cloud OCR synthesis dependencies',
               'Restore private source-bound OCR synthesis cache',
               'Build complete OCR summaries and charts for Market Views')]
        results = {'resolve-inputs': 'success', 'select-macro-reports': 'success', 'process-shard': 'success'}
        plan = {'replay_source_run_id': '123'}
        for proven in ('true', 'false', ''):
            self.assertFalse(gate(mineru, results, plan=plan, provider_only=proven))
            self.assertEqual(gate(recovery, results, plan=plan, primary_ready='false',
                                  provider_only=proven), proven == 'true')
            for outcome in ('success', 'failure', 'skipped', 'cancelled', 'timed_out', ''):
                for step in ocr:
                    with self.subTest(proven=proven, outcome=outcome):
                        self.assertEqual(gate(step, results, plan=plan, provider_only=proven,
                            steps={'mineru-recover': outcome}), proven == 'true' and outcome == 'skipped')
            for step in ocr:
                for stopped in ({'cancelled': True}, {'prior_steps_success': False}):
                    self.assertFalse(gate(step, results, plan=plan, provider_only=proven,
                        steps={'mineru-recover': 'skipped'}, **stopped))

    def test_frozen_replay_cannot_recover_when_accepted_task_binding_was_not_proven(self):
        results = {'resolve-inputs': 'success', 'select-macro-reports': 'success', 'process-shard': 'success'}
        recovery = job(UPSTREAM, 'recover-market-sources')
        for proven in ('false', 'true'):
            self.assertEqual(gate(recovery, results, primary_ready='false', provider_only=proven,
                                  plan={'replay_source_run_id': '123'}), proven == 'true')
        self.assertTrue(gate(recovery, results, primary_ready='false'))

    def test_actual_delivery_gate_distinguishes_provider_recovery_noop_and_real_failure(self):
        block = job(UPSTREAM, 'validate-market-delivery')
        program = textwrap.dedent(block.split('        run: |\n', 1)[1])
        base = {'SELECTION_RESULT': 'success', 'SOURCE_STATUS': 'success', 'DELIVERY_RESULT': 'success',
                'PRIMARY_READY': 'false', 'PROVIDER_ONLY': 'true', 'NO_WORK': 'false', 'SELECTED_COUNT': '4'}
        cases = [({}, 0), ({'PRIMARY_READY': 'true', 'PROVIDER_ONLY': 'false'}, 0),
                 ({'PROVIDER_ONLY': 'false'}, 0), ({'DELIVERY_RESULT': 'failure'}, 1),
                 ({'SOURCE_STATUS': 'failure'}, 1), ({'SELECTION_RESULT': 'failure'}, 1),
                 ({'NO_WORK': 'true', 'SELECTED_COUNT': '0', 'DELIVERY_RESULT': 'skipped'}, 0),
                 ({'NO_WORK': 'false', 'SELECTED_COUNT': '0', 'DELIVERY_RESULT': 'skipped'}, 1)]
        for changed, expected in cases:
            result = subprocess.run(['bash', '-e', '-c', program], env={**os.environ, **base, **changed},
                                    capture_output=True, text=True)
            self.assertEqual(bool(result.returncode), bool(expected), (changed, result.stderr))
            if changed.get('NO_WORK') == 'true':
                self.assertIn('no PDF was generated or claimed', result.stdout)
        proof = job(UPSTREAM, 'process-shard').split('- name: Confirm provider-only source degradation', 1)[1].split('\n      - name:', 1)[0]
        self.assertNotIn('continue-on-error', proof, 'REST proof conclusion must reflect a failed proof')
        generate = job(UPSTREAM, 'process-shard').split('- name: Generate shard outputs', 1)[1].split('\n      - name:', 1)[0]
        self.assertLess(generate.index('rm -f -- "$OUTPUT_DIR/batch_run_summary.json"'),
                        generate.index('python scripts/run_pdf_to_xhs_in_batches.py'))

    def test_exception_mail_follows_successful_backup_publication_and_exact_private_sha(self):
        market = MARKET.read_text()
        step = market.split('- name: Send deduplicated backup exception notice', 1)[1].split('\n      - name:', 1)[0]
        self.assertIn("env.BACKUP_NOTICE != ''", step)
        self.assertNotIn('failure()', step)
        self.assertIn('native-pdf)', step)
        self.assertIn('ocr-synthesis)', step)
        self.assertNotIn('source-pages', step)
        self.assertIn('--dedupe-hours 24', step)
        self.assertLess(market.index('- name: Verify the completed private publication receipt'),
                        market.index('- name: Send deduplicated backup exception notice'))
        self.assertIn("expected_sha256=os.environ['PRIVATE_PDF_SHA256']", market)
        self.assertLess(market.index('PRIVATE_PDF_SHA256={sha}'), market.index('- name: Prepare public-safe Market Views PDF'))

    def test_backup_notice_requires_successful_private_runtime_materialization(self):
        market = MARKET.read_text()
        materialize = market.split('- name: Materialize private backup alert runtime values', 1)[1].split('\n      - name:', 1)[0]
        send = market.split('- name: Send deduplicated backup exception notice', 1)[1].split('\n      - name:', 1)[0]
        self.assertIn('id: backup-alert-runtime', materialize)
        self.assertIn('continue-on-error: true', materialize)
        self.assertIn('PORTAL_PRIVATE_CONFIG_B64: ${{ secrets.PORTAL_PRIVATE_CONFIG_B64 }}', materialize)
        for flag in ('scripts/render_private_config.py', '--root scripts/send_portal_ops_alert.py',
                     '--github-add-mask', '--skip-generated-files'):
            self.assertIn(flag, materialize)
        for block in (materialize, send):
            expression = re.search(r'if: \$\{\{(.*?)\}\}', block).group(1)
            for notice in ('', 'ocr-synthesis', 'native-pdf'):
                for acceptance in (True, False):
                    for outcome in ('success', 'failure', 'skipped'):
                        evaluated = expression.replace('env.BACKUP_NOTICE', repr(notice))
                        evaluated = evaluated.replace('inputs.acceptance_only', repr(acceptance))
                        evaluated = evaluated.replace('steps.backup-alert-runtime.outcome', repr(outcome))
                        evaluated = evaluated.replace('true', 'True').replace('&&', ' and ')
                        expected = bool(notice) and not acceptance and (block == materialize or outcome == 'success')
                        self.assertEqual(eval(evaluated, {'__builtins__': {}}), expected)
        self.assertLess(market.index('- name: Verify the completed private publication receipt'),
                        market.index('- name: Materialize private backup alert runtime values'))
        self.assertLess(market.index('- name: Materialize private backup alert runtime values'),
                        market.index('- name: Send deduplicated backup exception notice'))

    def test_actual_alert_materialization_resolves_empty_and_relative_origins(self):
        import base64
        script_dir = Path(__file__).resolve().parent
        profile = {'version': 1, 'replacements': [
            {'public': 'portal.example.invalid', 'private': 'notify.example.test'}], 'files': []}
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / 'scripts/send_portal_ops_alert.py'
            target.parent.mkdir()
            target.write_bytes((script_dir / 'send_portal_ops_alert.py').read_bytes())
            result = subprocess.run([sys.executable, str(script_dir / 'render_private_config.py'),
                                     '--root', 'scripts/send_portal_ops_alert.py', '--github-add-mask',
                                     '--skip-generated-files'], cwd=root, capture_output=True, text=True,
                                    env={**os.environ, 'PORTAL_PRIVATE_CONFIG_B64': base64.b64encode(
                                        json.dumps(profile).encode()).decode()})
            self.assertEqual(result.returncode, 0, result.stderr)
            namespace = {'__name__': 'materialized_alert_for_test'}
            exec(compile(target.read_text(), str(target), 'exec'), namespace)
            for value in ('', '/api'):
                self.assertEqual(namespace['normalize_worker_url'](value),
                                 'https://notify.example.test/api/ops/alerts/email')

    def test_notice_recovery_only_verifies_then_sends_with_original_deduplication(self):
        recovery = NOTICE_RECOVERY.read_text()
        self.assertIn('workflow_dispatch:', recovery)
        self.assertNotIn('workflow_run:', recovery)
        self.assertNotIn('schedule:', recovery)
        self.assertIn("if: ${{ github.ref == 'refs/heads/main' }}", recovery)
        self.assertIn('contents: read', recovery)
        self.assertNotIn('contents: write', recovery)
        for forbidden in ('DEEPSEEK_API_KEY', 'MINERU_API_KEY', 'commit_output_dir.sh',
                          'build_market_views', 'upload-artifact', 'download-artifact'):
            self.assertNotIn(forbidden, recovery)
        self.assertLess(recovery.index('- name: Verify original run and exact published PDF'),
                        recovery.index('- name: Materialize private alert runtime values'))
        self.assertLess(recovery.index('- name: Materialize private alert runtime values'),
                        recovery.index('- name: Send deduplicated backup exception notice'))
        self.assertNotIn('continue-on-error', recovery)
        materialize = recovery.split('- name: Materialize private alert runtime values', 1)[1].split('\n      - name:', 1)[0]
        self.assertIn('PORTAL_PRIVATE_CONFIG_B64: ${{ secrets.PORTAL_PRIVATE_CONFIG_B64 }}', materialize)
        for flag in ('scripts/render_private_config.py', '--root scripts/send_portal_ops_alert.py',
                     '--github-add-mask', '--skip-generated-files'):
            self.assertIn(flag, materialize)
        for text in (MARKET.read_text(), recovery):
            self.assertIn('--dedupe-key "market-views-source-edition:$DATE_FOLDER" --dedupe-hours 24', text)
        self.assertIn('/actions/runs/$PUBLICATION_RUN_ID', recovery)

    def test_actual_notice_recovery_verifier_requires_successful_run_and_exact_private_pdf(self):
        import upload_market_view_to_r2 as uploader
        step = NOTICE_RECOVERY.read_text().split('- name: Verify original run and exact published PDF', 1)[1].split('\n      - name:', 1)[0]
        shell = textwrap.dedent(step.split('        run: |\n', 1)[1])
        program = shell.split("python - <<'PY'\n", 1)[1].rsplit('\nPY', 1)[0]
        base = {'DATE_FOLDER': '261005', 'PUBLICATION_RUN_ID': '37452939157',
                'PRIVATE_PDF_SHA256': 'a' * 64, 'BACKUP_NOTICE': 'ocr-synthesis',
                'GITHUB_REPOSITORY': 'example/reports'}
        original = {'id': 37452939157, 'repository': {'full_name': 'example/reports'},
                    'path': '.github/workflows/market-views-latex-pdf.yml', 'head_branch': 'main',
                    'status': 'completed', 'conclusion': 'success', 'event': 'workflow_dispatch'}

        def execute(*, environment=None, run=None, complete=True, r2_error=None):
            response = subprocess.CompletedProcess(['gh'], 0, json.dumps(run or original), '')
            previous_path = list(sys.path)
            try:
                with mock.patch.dict(os.environ, {**base, **(environment or {})}, clear=True), \
                        mock.patch('subprocess.run', return_value=response) as github, \
                        mock.patch.object(uploader, 'private_publication_complete', return_value=complete,
                                          side_effect=r2_error) as private, \
                        contextlib.redirect_stdout(io.StringIO()):
                    error = None
                    try:
                        exec(compile(program, str(NOTICE_RECOVERY), 'exec'), {'__name__': '__main__'})
                    except (Exception, SystemExit) as exc:
                        error = exc
                    return error, github, private
            finally:
                sys.path[:] = previous_path

        for notice, edition in (('ocr-synthesis', 'ocr-synthesis'), ('native-pdf', 'standard')):
            error, github, private = execute(environment={'BACKUP_NOTICE': notice})
            self.assertIsNone(error)
            github.assert_called_once_with(['gh', 'api', 'repos/example/reports/actions/runs/37452939157'],
                                           check=True, capture_output=True, text=True)
            private.assert_called_once_with('261005', expected_sha256='a' * 64, expected_edition=edition)
        for changed in ({'DATE_FOLDER': 'latest'}, {'DATE_FOLDER': '261332'},
                        {'PRIVATE_PDF_SHA256': ''}, {'PRIVATE_PDF_SHA256': 'A' * 64},
                        {'PUBLICATION_RUN_ID': '../wrong'}, {'BACKUP_NOTICE': 'source-pages'}):
            error, github, private = execute(environment=changed)
            self.assertIsNotNone(error, changed)
            github.assert_not_called()
            private.assert_not_called()
        for changed in ({'id': 1}, {'repository': {'full_name': 'other/reports'}},
                        {'path': '.github/workflows/unrelated.yml'}, {'head_branch': 'feature'},
                        {'status': 'in_progress'}, {'conclusion': 'failure'}, {'event': 'pull_request'}):
            error, _, private = execute(run={**original, **changed})
            self.assertIsNotNone(error, changed)
            private.assert_not_called()
        for arguments in ({'complete': False}, {'r2_error': RuntimeError('unavailable R2')}):
            error, _, private = execute(**arguments)
            self.assertIsNotNone(error)
            private.assert_called_once()

    def test_native_receipt_is_checked_before_idempotency_or_paid_synthesis(self):
        market = MARKET.read_text()
        receipt = market.index("- name: Verify complete native PDF source receipt")
        resolve = market.index("- name: Resolve and validate primary bank source")
        build = market.index("- name: Build market views data and LaTeX source")
        self.assertLess(receipt, resolve)
        self.assertLess(resolve, build)
        block = market[receipt:resolve]
        self.assertIn("'scripts/extract_native_market_sources.py', 'validate'", block)
        self.assertIn("'--expected-reports', expected", block)
        self.assertIn("'--producer-run-id', source_run", block)
        self.assertIn("'--execution-sha', producer['head_sha']", block)
        self.assertIn('/jobs?filter=latest&per_page=100', block)
        self.assertIn('require_source_readiness(producer, source_jobs)', block)
        self.assertIn("'scripts/audit_market_views_ocr_receipt.py'", block)

    def test_cloud_ocr_is_staged_and_source_only_review_keeps_the_private_handoff(self):
        recovery = (WORKFLOWS / "market-views-native-recovery.yml").read_text()
        self.assertRegex(recovery, r"(?s)enable_ocr:.*?default: false")
        self.assertRegex(recovery, r"(?s)generate_pdf:.*?default: true")
        for step_name in ("Generate and wait for the exact Market Views PDF",
                          "Delete consumed native source handoff after the PDF succeeds"):
            block = recovery.split(f"- name: {step_name}", 1)[1].split("\n      - name:", 1)[0]
            self.assertIn("if: ${{ inputs.generate_pdf && !inputs.archive_originals_only }}", block)
        daily = job(UPSTREAM, "recover-market-sources")
        self.assertIn('--ocr-all-pages', daily)
        self.assertNotIn('MARKET_VIEWS_OCR_BACKUP_ENABLED', daily)
        self.assertIn('--cache-dir _market_ocr_cache', daily)
        self.assertIn('--source-run-id "$GITHUB_RUN_ID"', daily)
        self.assertIn('--execution-sha "$GITHUB_SHA"', daily)
        self.assertIn('--model "$MODEL" --base-url "$BASE_URL"', daily)
        self.assertIn('MODEL: ${{ needs.resolve-inputs.outputs.model }}', daily)
        self.assertIn('BASE_URL: ${{ needs.resolve-inputs.outputs.deepseek_base_url }}', daily)
        cache_restore = daily.split('- name: Restore private source-bound OCR synthesis cache', 1)[1].split('\n      - name:', 1)[0]
        cache_save = daily.split('- name: Save private OCR synthesis cache even after interruption', 1)[1].split('\n      - name:', 1)[0]
        self.assertIn('private_market_ocr_checkpoint.py restore', cache_restore)
        self.assertIn('private_market_ocr_checkpoint.py save', cache_save)
        self.assertIn('always()', cache_save)
        self.assertIn("steps.ocr-synthesis.outcome != 'skipped'", cache_save)
        self.assertNotIn('uses: actions/upload-artifact', cache_save)
        for block in (cache_restore, cache_save):
            self.assertIn('timeout-minutes: 3', block)
            self.assertIn('continue-on-error: true', block)
            self.assertIn('--manifest _selected_macro_pdfs/selected_to_process_manifest.json', block)
            self.assertIn('--date-folder "$DATE_FOLDER" --expected-reports "$EXPECTED_ARTICLES"', block)

        for workflow in (daily, recovery, (WORKFLOWS / "wechat-pipeline-regression.yml").read_text()):
            self.assertIn("tesseract-ocr-eng tesseract-ocr-chi-sim", workflow)
            self.assertIn('test -f "$TESSDATA_DIR/eng.traineddata"', workflow)
            self.assertIn('test -f "$TESSDATA_DIR/chi_sim.traineddata"', workflow)
        regression = (WORKFLOWS / "wechat-pipeline-regression.yml").read_text()
        self.assertIn('REQUIRE_MARKET_VIEWS_OCR_TESTS: "1"', regression)
        self.assertIn('python scripts/test_ocr_numeric_evidence.py', regression)
        self.assertIn('python scripts/test_audit_market_views_ocr_receipt.py', regression)
        self.assertIn('pip install -r requirements.txt reportlab', daily)
        self.assertIn('PyMuPDF Pillow requests', recovery)
        market = MARKET.read_text()
        dependency = market.index('- name: Install private handoff dependency')
        receipt = market.index('- name: Verify complete native PDF source receipt')
        self.assertLess(dependency, receipt)
        self.assertIn('boto3 requests PyMuPDF Pillow', market[dependency:receipt])
        audit = recovery.index('- name: Audit complete cloud OCR numeric evidence')
        archive = recovery.index('- name: Archive verified native sources in private R2')
        consumer = recovery.index('- name: Generate and wait for the exact Market Views PDF')
        self.assertLess(archive, audit)
        self.assertLess(audit, consumer)
        self.assertIn('--source-dir _native_market_sources/shard_0', recovery[audit:consumer])
        self.assertIn('path: ${{ runner.temp }}/market-views-ocr-audit.json', recovery[audit:consumer])
        self.assertIn('QUALITY_FIXTURE_JSON: ${{ inputs.quality_fixture_json }}', recovery)
        self.assertIn("raw = os.environ['QUALITY_FIXTURE_JSON']", recovery[audit:consumer])
        self.assertIn('FIXTURE_ARGS+=(--fixtures "$RUNNER_TEMP/market-views-ocr-fixtures.json")', recovery[audit:consumer])
        self.assertNotIn('continue-on-error:', recovery[audit:consumer])

    def test_actual_native_consumer_accepts_failed_original_and_rejects_wrong_producer_context(self):
        import hashlib
        import json
        from extract_native_market_sources import extract_sources
        from test_extract_native_market_sources import make_pdf

        step = MARKET.read_text().split("- name: Verify complete native PDF source receipt", 1)[1].split("\n      - name:", 1)[0]
        command = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "scripts").symlink_to(WORKFLOWS.parents[1] / "scripts", target_is_directory=True)
            originals = root / "originals"
            originals.mkdir()
            pdf = originals / "source.pdf"
            make_pdf(pdf)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps([{
                "process_local_path": str(pdf), "dropbox_path": "/zip_backup/261003/source.pdf",
                "content_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            }]))
            sources = root / "xhs_notes/dropbox/261003/shard_0"
            context = {"date_folder": "261003", "producer_run_id": "37214015946",
                       "execution_sha": "c" * 40, "original_source_run_id": "37159099752"}
            extract_sources(originals, manifest, sources, 1, source_context=context)
            binaries = root / "bin"
            binaries.mkdir()
            python_environment = test_python_environment(binaries)
            gh = binaries / "gh"
            gh.write_text(f"#!{sys.executable}\n" + textwrap.dedent('''\
                import json
                import os
                import sys
                endpoint = sys.argv[-1]
                if '/jobs?' in endpoint:
                    sys.path.insert(0, 'scripts')
                    from market_views_source_readiness import SOURCE_GATES
                    path = os.environ.get('FAKE_PRODUCER_PATH', '.github/workflows/market-views-native-recovery.yml')
                    name, gates = SOURCE_GATES[path]
                    steps = [{'name': title, 'number': number, 'status': 'completed', 'conclusion': 'success'}
                             for number, title in enumerate(gates, start=3)]
                    for step in steps:
                        if step['name'].startswith('Audit complete'):
                            step['status'] = os.environ.get('FAKE_AUDIT_STATUS', 'completed')
                            step['conclusion'] = os.environ.get('FAKE_AUDIT_CONCLUSION', 'success')
                    print(json.dumps({'total_count': 1, 'jobs': [{
                        'id': 67890, 'name': name, 'run_id': int(os.environ.get('FAKE_JOB_RUN_ID', '37214015946')),
                        'head_sha': os.environ.get('FAKE_JOB_SHA', os.environ.get('FAKE_SHA', 'c' * 40)),
                        'status': os.environ.get('FAKE_PRODUCER_STATUS', 'in_progress'),
                        'conclusion': os.environ.get('FAKE_PRODUCER_CONCLUSION'), 'steps': steps,
                    }]}))
                    raise SystemExit(0)
                run_id = endpoint.split('/')[-1]
                producer = run_id == '37214015946'
                print(json.dumps({
                    'id': int(run_id), 'head_branch': os.environ.get('FAKE_BRANCH', 'main'),
                    'head_sha': os.environ.get('FAKE_SHA', 'c' * 40),
                    'path': os.environ.get('FAKE_PRODUCER_PATH', '.github/workflows/market-views-native-recovery.yml') if producer else '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml',
                    'status': os.environ.get('FAKE_PRODUCER_STATUS', 'in_progress') if producer else os.environ.get('FAKE_ORIGINAL_STATUS', 'completed'),
                    'conclusion': os.environ.get('FAKE_PRODUCER_CONCLUSION') if producer else os.environ.get('FAKE_ORIGINAL_CONCLUSION', 'failure'),
                }))
            '''))
            gh.chmod(0o755)
            runtime = root / 'runtime'
            runtime.mkdir()
            environment = {**os.environ, **python_environment,
                           "GITHUB_REPOSITORY": "example/project", "SOURCE_HANDOFF_RUN_ID": context["producer_run_id"],
                           "EXPECTED_BANK_DATE": "261003", "EXPECTED_ARTICLES": "1", "RUNNER_TEMP": str(runtime),
                           "NATIVE_QUALITY_FIXTURE_JSON": ''}
            def run(values):
                return subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command], cwd=root,
                                      env={**environment, **values}, capture_output=True, text=True)
            accepted = run({})
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            accepted = run({'FAKE_PRODUCER_STATUS': 'completed', 'FAKE_PRODUCER_CONCLUSION': 'failure'})
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            for invalid in ({"FAKE_BRANCH": "feature"}, {"FAKE_SHA": "d" * 40},
                            {"FAKE_PRODUCER_PATH": ".github/workflows/another.yml"},
                            {"FAKE_ORIGINAL_STATUS": "in_progress"}, {"FAKE_ORIGINAL_CONCLUSION": "cancelled"},
                            {"FAKE_AUDIT_CONCLUSION": "failure"}, {"FAKE_AUDIT_CONCLUSION": "skipped"},
                            {"FAKE_AUDIT_STATUS": "in_progress"}, {"FAKE_JOB_SHA": "d" * 40},
                            {"FAKE_JOB_RUN_ID": "37214015947"}):
                with self.subTest(invalid=invalid):
                    rejected = run(invalid)
                    self.assertNotEqual(rejected.returncode, 0, rejected.stdout)
            rejected = run({"FAKE_PRODUCER_PATH": ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"})
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("own selected original run", rejected.stderr)
            real_fixture = {"schema": 1, "checks": [{
                "id": "real_17pct", "source_pdf_sha256": "55519fd3388cfecc3bd12854d64bfd8368c6b683c365512fbcff49581e2c5fa5",
                "page": 1, "expected_literal": "17%", "expected_bbox": [139, 245, 165, 259],
            }]}
            encoded_fixture = json.dumps(real_fixture)
            rejected = run({'NATIVE_QUALITY_FIXTURE_JSON': encoded_fixture})
            self.assertNotEqual(rejected.returncode, 0)
            self.assertEqual((runtime / 'market-views-native-quality-fixtures.json').read_text(), encoded_fixture)
            audit = json.loads((runtime / 'market-views-native-source-audit.json').read_text())
            self.assertEqual(audit['fixture_acceptance'], 'failed')
            injection = json.dumps({"schema": 1, "checks": [{**real_fixture['checks'][0],
                "expected_literal": "$(touch SHELL_EXECUTED)"}]})
            rejected = run({'NATIVE_QUALITY_FIXTURE_JSON': injection})
            self.assertNotEqual(rejected.returncode, 0)
            self.assertFalse((root / 'SHELL_EXECUTED').exists())

    def test_actual_cloud_audit_reads_fixture_json_as_data_and_fails_unmatched_fields(self):
        import hashlib
        import json
        from extract_native_market_sources import extract_sources
        from test_extract_native_market_sources import make_pdf

        workflow = (WORKFLOWS / "market-views-native-recovery.yml").read_text()
        step = workflow.split("- name: Audit complete cloud OCR numeric evidence", 1)[1].split("\n      - name:", 1)[0]
        command = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "scripts").symlink_to(WORKFLOWS.parents[1] / "scripts", target_is_directory=True)
            originals = root / "originals"
            originals.mkdir()
            pdf = originals / "source.pdf"
            make_pdf(pdf)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps([{
                "process_local_path": str(pdf), "dropbox_path": "/zip_backup/261003/source.pdf",
                "content_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            }]))
            source_dir = root / "_native_market_sources/shard_0"
            context = {"date_folder": "261003", "producer_run_id": "37214015946",
                       "execution_sha": "c" * 40, "original_source_run_id": "37159099752"}
            extract_sources(originals, manifest, source_dir, 1, source_context=context)
            binaries = root / "bin"
            binaries.mkdir()
            python_environment = test_python_environment(binaries)
            runtime = root / "runtime"
            runtime.mkdir()
            environment = {**os.environ, **python_environment,
                           "RUNNER_TEMP": str(runtime), "EXPECTED_ARTICLES": "1", "DATE_FOLDER": "261003",
                           "GITHUB_RUN_ID": context["producer_run_id"], "GITHUB_SHA": context["execution_sha"],
                           "SOURCE_RUN_ID": context["original_source_run_id"], "QUALITY_FIXTURE_JSON": ""}
            def run(fixture):
                return subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command], cwd=root,
                                      env={**environment, "QUALITY_FIXTURE_JSON": fixture}, capture_output=True, text=True)
            accepted = run("")
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            summary_path = runtime / "market-views-ocr-audit.json"
            self.assertEqual(json.loads(summary_path.read_text())["fixture_acceptance"], "not_requested")
            check = {"id": "known_value", "source_pdf_sha256": "a" * 64, "page": 2,
                     "expected_literal": "4.8", "expected_bbox": [10, 10, 20, 20]}
            rejected = run(json.dumps({"schema": 1, "checks": [check]}))
            self.assertEqual(rejected.returncode, 3, rejected.stderr)
            self.assertEqual(json.loads(summary_path.read_text())["fixture_acceptance"], "failed")
            sentinel = root / "should-not-exist"
            rejected = run(json.dumps({"schema": 1, "checks": [{**check, "id": f"$(touch {sentinel})"}]}))
            self.assertEqual(rejected.returncode, 2)
            self.assertFalse(sentinel.exists())
            self.assertTrue((source_dir / "source_receipt.json").is_file())

    def test_recovery_archive_waits_for_pdf_and_article_consumers(self):
        cleanup = job(UPSTREAM, "cleanup-market-source-recovery")
        complete = {"recover-market-sources": "success", "trigger-market-views": "success",
                    "validate-report-delivery": "success", "publish-customer-content": "success"}
        self.assertTrue(gate(cleanup, complete))
        for name in complete:
            for outcome in ("failure", "cancelled", "skipped"):
                self.assertFalse(gate(cleanup, {**complete, name: outcome}))
        self.assertFalse(gate(cleanup, complete, cancelled=True))
        self.assertIn('mineru-recovery) SOURCE_PREFIX=mineru-market-sources', cleanup)
        self.assertIn('ocr-synthesis) SOURCE_PREFIX=market-ocr-synthesis', cleanup)
        self.assertNotIn('SOURCE_PREFIX=market-preview-sources', cleanup)
        recovery = (WORKFLOWS / "market-views-native-recovery.yml").read_text()
        self.assertLess(recovery.index('gh run watch "$MARKET_RUN_ID"'),
                        recovery.index('name: Delete consumed native source handoff'))

    def test_mineru_recovery_receipt_precedes_source_resolution_and_synthesis(self):
        market = MARKET.read_text()
        receipt = market.index("- name: Verify complete MinerU recovery source receipt")
        resolve = market.index("- name: Resolve and validate primary bank source")
        build = market.index("- name: Build market views data and LaTeX source")
        self.assertLess(receipt, resolve)
        self.assertLess(resolve, build)
        block = market[receipt:resolve].split("\n      - name:", 1)[0]
        command = textwrap.dedent(block.split("        run: |\n", 1)[1])
        program = command.split("python - <<'PYTHON'\n", 1)[1].rsplit("\nPYTHON", 1)[0]
        calls = [node for node in ast.walk(ast.parse(program))
                 if isinstance(node, ast.Call) and ast.unparse(node.func) == "subprocess.run"]
        self.assertEqual(len(calls), 1)
        call = calls[0]
        self.assertIsInstance(call.args[0], ast.List)
        argv = call.args[0].elts
        self.assertEqual(ast.unparse(argv[0]), "sys.executable")
        self.assertEqual([ast.literal_eval(value) for value in argv[1:3]],
                         ["scripts/recover_durable_mineru_sources.py", "validate"])
        options = {ast.literal_eval(argv[index]): ast.unparse(argv[index + 1])
                   for index in range(3, len(argv), 2)}
        self.assertEqual(options["--expected-reports"], "os.environ['EXPECTED_ARTICLES']")
        self.assertEqual(options["--date-folder"], "os.environ['EXPECTED_BANK_DATE']")
        self.assertEqual(options["--expected-recovery-run-id"], "run")
        self.assertEqual(options["--expected-execution-sha"], "producer['head_sha']")
        self.assertEqual({keyword.arg: ast.literal_eval(keyword.value) for keyword in call.keywords},
                         {"check": True})
        self.assertIn("require_source_readiness(producer, jobs, source_kind='mineru-recovery')", block)
        self.assertIn('PRIVATE_MINERU_SOURCES_ROOT: "_private-workflow-handoff/mineru-market-sources"', market)

    def test_mineru_recovery_input_requires_complete_explicit_handoff(self):
        step = MARKET.read_text().split("- name: Validate private input source", 1)[1].split("\n      - name:", 1)[0]
        command = textwrap.dedent(step.split("        run: |\n", 1)[1])
        environment = {**os.environ, "SOURCE_HANDOFF_RUN_ID": "37211677994",
                       "SOURCE_ARTIFACT_RUN_ID": "", "EXPECTED_BANK_DATE": "261003",
                       "SOURCE_HANDOFF_KIND": "mineru-recovery", "EXPECTED_SHARDS": "1", "EXPECTED_ARTICLES": "54"}
        valid = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                               env=environment, capture_output=True, text=True)
        self.assertEqual(valid.returncode, 0, valid.stderr)
        for missing in ({"SOURCE_HANDOFF_RUN_ID": ""}, {"EXPECTED_SHARDS": "0"}, {"EXPECTED_ARTICLES": "0"}):
            rejected = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", command],
                                      env={**environment, **missing}, capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("Source recovery requires", rejected.stderr)

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
        import upload_market_view_to_r2 as uploader
        from test_upload_market_view_to_r2 import FakeR2Client
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "scripts").symlink_to(WORKFLOWS.parents[1] / "scripts", target_is_directory=True)
            for source, date in (("dropbox", "261003"), ("institutions", "261004")):
                report = root / "xhs_notes" / source / date / "report"
                report.mkdir(parents=True)
                (report / "source_native_pdf.md").write_text("# Exact source report")
            existing = root / "market_view_summaries/261004/market_views_261004.pdf"
            existing.parent.mkdir(parents=True)
            make_readable_pdf(existing)
            binaries = root / "bin"
            binaries.mkdir()
            (binaries / "python").symlink_to(sys.executable)
            env_file = root / "env"
            environment = {**os.environ, "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
                           "GITHUB_ENV": str(env_file), "REQUESTED_DATE_FOLDER": "latest",
                           "EXPECTED_BANK_DATE": "261003", "EXPECTED_ARTICLES": "1", "FORCE_REBUILD": "false"}
            client = FakeR2Client()
            result = run_actual_market_resolver(root, environment, client)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["BUILD_DATE_FOLDER"], "261003")
            self.assertEqual(values["DATE_FOLDER"], "261003")
            self.assertEqual(values["SHOULD_BUILD"], "true")
            environment["EXPECTED_ARTICLES"] = "2"
            result = run_actual_market_resolver(root, environment, client)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Expected 2 bank reports, received 1", result.stderr)
            environment["EXPECTED_ARTICLES"] = "1"
            same_date = root / "market_view_summaries/261003/market_views_261003.pdf"
            same_date.parent.mkdir(parents=True)
            same_date.write_bytes(existing.read_bytes())
            uploader.upload_market_view(same_date, "261003", client=client, bucket="test")
            env_file.write_text("")
            result = run_actual_market_resolver(root, environment, client)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["SHOULD_BUILD"], "false")
            environment["FORCE_REBUILD"] = "true"
            environment["SOURCE_HANDOFF_KIND"] = "native-pdf"
            env_file.write_text("")
            result = run_actual_market_resolver(root, environment, client)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["SHOULD_BUILD"], "true")
            self.assertEqual(values["BACKUP_NOTICE"], "native-pdf")
            # Acceptance must rebuild an already published issue while still
            # checking the real complete source count before synthesis.
            environment["FORCE_REBUILD"] = "false"
            environment["ACCEPTANCE_ONLY"] = "true"
            env_file.write_text("")
            result = run_actual_market_resolver(root, environment, client)
            self.assertEqual(result.returncode, 0, result.stderr)
            values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
            self.assertEqual(values["SHOULD_BUILD"], "true")
            environment["EXPECTED_ARTICLES"] = "2"
            result = run_actual_market_resolver(root, environment, client)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Expected 2 bank reports, received 1", result.stderr)

    def test_existing_public_pdf_requires_complete_private_publication_to_skip(self):
        import upload_market_view_to_r2 as uploader
        from test_upload_market_view_to_r2 import FakeR2Client, R2ServiceError
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            report = root / "xhs_notes/dropbox/261003/report"
            report.mkdir(parents=True)
            (report / "source_native_pdf.md").write_text("# Exact complete source report")
            public_pdf = root / "market_view_summaries/261003/market_views_261003.pdf"
            public_pdf.parent.mkdir(parents=True)
            public_bytes = make_readable_pdf(public_pdf, "Public research analysis")
            private_pdf = root / "private-original.pdf"
            private_bytes = make_readable_pdf(private_pdf, "Complete private research analysis")
            client = FakeR2Client()
            uploader.upload_market_view(private_pdf, "261003", client=client, bucket="test")
            private_pdf.unlink()
            original_objects = dict(client.objects)
            pdf_key, item_key = "_market-views/pdfs/261003.pdf", "_market-views/items/261003.json"
            env_file = root / "env"
            environment = {**os.environ, "GITHUB_ENV": str(env_file), "REQUESTED_DATE_FOLDER": "261003",
                           "EXPECTED_BANK_DATE": "261003", "EXPECTED_ARTICLES": "1",
                           "FORCE_REBUILD": "false", "ACCEPTANCE_ONLY": "false"}

            def run(expected):
                env_file.write_text("")
                client.calls.clear()
                result = run_actual_market_resolver(root, environment, client)
                self.assertEqual(result.returncode, 0, result.stderr)
                values = dict(line.split("=", 1) for line in env_file.read_text().splitlines())
                self.assertEqual(values["SHOULD_BUILD"], expected)
                self.assertFalse(any(operation == "put" for operation, _ in client.calls))
                self.assertEqual(public_pdf.read_bytes(), public_bytes)

            # Private original and public-safe hashes intentionally differ.
            run("false")
            self.assertIn(("get", pdf_key), client.calls)
            self.assertIn(("get", item_key), client.calls)
            self.assertEqual(client.objects[pdf_key]["Body"], private_bytes)
            for missing in ((pdf_key,), (item_key,), (pdf_key, item_key)):
                client.objects = {key: value for key, value in original_objects.items() if key not in missing}
                run("true")
            client.objects = dict(original_objects)
            item = json.loads(original_objects[item_key]["Body"])
            item["sha256"] = "0" * 64
            client.objects[item_key] = {**original_objects[item_key], "Body": json.dumps(item).encode()}
            run("true")

            client.objects = dict(original_objects)
            for error in (R2ServiceError("AccessDenied", 403), TimeoutError("private read timeout")):
                env_file.write_text("")
                with mock.patch.object(client, "get_object", side_effect=error):
                    result = run_actual_market_resolver(root, environment, client)
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn("SHOULD_BUILD=", env_file.read_text())

            # Explicit force and acceptance retain their existing rebuild
            # semantics without adding a private-publication availability gate.
            for field in ("FORCE_REBUILD", "ACCEPTANCE_ONLY"):
                environment[field] = "true"
                with mock.patch.object(client, "head_object", side_effect=AssertionError("unneeded R2 probe")):
                    run("true")
                environment[field] = "false"

        market = MARKET.read_text()
        for name in ("Build market views data and LaTeX source", "Render fast PDF without LaTeX install",
                     "Archive exact Market Views PDF in private R2", "Commit public-safe Market Views PDF to main"):
            step = market.split(f"- name: {name}", 1)[1].split("\n      - name:", 1)[0]
            self.assertIn("env.SHOULD_BUILD != 'false'", step)
        self.assertLess(market.index("- name: Verify complete native PDF source receipt"),
                        market.index("- name: Resolve and validate primary bank source"))
        self.assertLess(market.index("- name: Archive exact Market Views PDF in private R2"),
                        market.index("- name: Prepare public-safe Market Views PDF"))

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
            "push-portal-translated-wechat-drafts", "publish-customer-content",
        )}
        self.assertTrue(gate(cleanup, results))
        for name in results:
            for status in ("failure", "cancelled"):
                with self.subTest(name=name, status=status):
                    self.assertFalse(gate(cleanup, {**results, name: status}))
        self.assertFalse(gate(cleanup, {**results, "trigger-market-views": "skipped"}))
        self.assertFalse(gate(cleanup, {**results, "publish-customer-content": "skipped"}))
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
