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
        self.assertIn("'scripts/extract_native_market_sources.py', 'validate'", block)
        self.assertIn("'--expected-reports', expected", block)
        self.assertIn("'--producer-run-id', source_run", block)
        self.assertIn("'--execution-sha', producer['head_sha']", block)
        self.assertIn('/jobs?filter=latest&per_page=100', block)
        self.assertIn('require_source_readiness(producer, json.loads(jobs_result.stdout))', block)
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
        self.assertIn("ENABLE_OCR: ${{ vars.MARKET_VIEWS_OCR_BACKUP_ENABLED || 'false' }}", daily)
        self.assertIn("OCR_ARGS+=(--enable-ocr)", daily)
        self.assertIn('"${OCR_ARGS[@]}"', daily)
        self.assertIn('--producer-run-id "$GITHUB_RUN_ID"', daily)
        self.assertIn('--original-source-run-id "$GITHUB_RUN_ID"', daily)
        for workflow in (daily, recovery, (WORKFLOWS / "wechat-pipeline-regression.yml").read_text()):
            self.assertIn("tesseract-ocr-eng tesseract-ocr-chi-sim", workflow)
            self.assertIn('test -f "$TESSDATA_DIR/eng.traineddata"', workflow)
            self.assertIn('test -f "$TESSDATA_DIR/chi_sim.traineddata"', workflow)
        regression = (WORKFLOWS / "wechat-pipeline-regression.yml").read_text()
        self.assertIn('REQUIRE_MARKET_VIEWS_OCR_TESTS: "1"', regression)
        self.assertIn('python scripts/test_ocr_numeric_evidence.py', regression)
        self.assertIn('python scripts/test_audit_market_views_ocr_receipt.py', regression)
        self.assertIn('PyMuPDF Pillow', daily)
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
            (binaries / "python").symlink_to(sys.executable)
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
            environment = {**os.environ, "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
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
            (binaries / "python").symlink_to(sys.executable)
            runtime = root / "runtime"
            runtime.mkdir()
            environment = {**os.environ, "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
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

    def test_native_archive_is_released_only_after_its_pdf_consumer_succeeds(self):
        cleanup = job(UPSTREAM, "cleanup-market-source-recovery")
        self.assertTrue(gate(cleanup, {"recover-market-sources": "success", "trigger-market-views": "success"}))
        for consumer in ("failure", "cancelled", "skipped"):
            self.assertFalse(gate(cleanup, {"recover-market-sources": "success", "trigger-market-views": consumer}))
        self.assertFalse(gate(cleanup, {"recover-market-sources": "success", "trigger-market-views": "success"}, cancelled=True))
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
        block = market[receipt:resolve]
        self.assertIn("recover_durable_mineru_sources.py validate", block)
        self.assertIn('--expected-reports "$EXPECTED_ARTICLES"', block)
        self.assertIn('--date-folder "$EXPECTED_BANK_DATE"', block)
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
