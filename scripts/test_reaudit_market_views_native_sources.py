from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest import mock

import fitz

import audit_market_views_ocr_receipt as audit
from extract_native_market_sources import extract_sources
import market_views_source_readiness as readiness
import ocr_numeric_evidence
import reaudit_market_views_native_sources as reaudit

REPOSITORY = "example/reports"
SOURCE_ID, REVIEW_ID = "100", "200"
DATE = "261002"


def run(run_id=SOURCE_ID, *, reviewer=False):
    return {"id": int(run_id), "head_sha": ("b" if reviewer else "a") * 40,
            "head_branch": "main", "event": "workflow_dispatch", "run_attempt": 1,
            "path": reaudit.WORKFLOW if reviewer else reaudit.SOURCE_WORKFLOW,
            "repository": {"full_name": REPOSITORY}, "head_repository": {"full_name": REPOSITORY}, "status": "completed",
            "conclusion": "success" if reviewer else "failure"}


def jobs(producer, *, reviewer=False):
    names = (reaudit.AUDIT_STEP,) if reviewer else reaudit.SOURCE_STEPS
    conclusions = ("success",) if reviewer else ("success", "success", "failure")
    return {"total_count": 1, "jobs": [{"id": 300, "run_id": producer["id"],
             "head_sha": producer["head_sha"], "run_attempt": producer["run_attempt"],
             "name": "reaudit" if reviewer else "recover", "status": "completed",
             "steps": [{"name": name, "number": number, "status": "completed", "conclusion": conclusion}
                       for number, (name, conclusion) in enumerate(zip(names, conclusions), 1)]}]}


class FakeR2:
    def __init__(self):
        self.objects = {}
        self.puts = []

    def put_object(self, **kwargs):
        if kwargs["Key"] in self.objects:
            raise AssertionError("Attestation must be immutable")
        self.puts.append(kwargs)
        self.objects[kwargs["Key"]] = (kwargs["Body"], kwargs["Metadata"])

    def get_object(self, **kwargs):
        raw, metadata = self.objects[kwargs["Key"]]
        return {"ContentLength": len(raw), "Metadata": metadata, "Body": io.BytesIO(raw)}


class MetadataTests(unittest.TestCase):
    def test_only_complete_extraction_and_archive_with_failed_old_audit_are_eligible(self):
        source = run()
        baseline = jobs(source)
        reaudit.verify_retained_source(source, baseline, SOURCE_ID, REPOSITORY)
        for index, conclusion in ((0, "failure"), (1, "failure"), (2, "success"), (2, "skipped")):
            changed = copy.deepcopy(baseline)
            changed["jobs"][0]["steps"][index]["conclusion"] = conclusion
            with self.subTest(index=index, conclusion=conclusion), self.assertRaises(reaudit.ReauditError):
                reaudit.verify_retained_source(source, changed, SOURCE_ID, REPOSITORY)
        # Existing everyday consumers remain strict and do not accept this run.
        with self.assertRaisesRegex(readiness.SourceReadinessError, "source_gate_not_successful"):
            readiness.require_source_readiness(source, baseline)

    def test_branch_workflow_repository_sha_and_attempt_are_bound(self):
        source = run()
        for key, value in (("head_branch", "feature"), ("path", ".github/workflows/other.yml"),
                           ("head_sha", "invalid"), ("run_attempt", True),
                           ("repository", {"full_name": "other/reports"}),
                           ("head_repository", {"full_name": "other/reports"}), ("event", "push")):
            changed = {**source, key: value}
            with self.subTest(key=key), self.assertRaises(reaudit.ReauditError):
                reaudit.verify_retained_source(changed, jobs(source), SOURCE_ID, REPOSITORY)
        for key, value in (("head_sha", "c" * 40), ("run_id", 999), ("run_attempt", 2)):
            changed = jobs(source)
            changed["jobs"][0][key] = value
            with self.subTest(job_key=key), self.assertRaises(reaudit.ReauditError):
                reaudit.verify_retained_source(source, changed, SOURCE_ID, REPOSITORY)

    def test_partial_ambiguous_or_reordered_jobs_rejected(self):
        source = run()
        changes = []
        changed = jobs(source); changed["total_count"] = 2; changes.append(changed)
        changed = jobs(source); changed["jobs"] *= 2; changed["total_count"] = 2; changes.append(changed)
        changed = jobs(source); changed["jobs"][0]["steps"][0]["number"] = 4; changes.append(changed)
        changed = jobs(source); changed["jobs"][0]["steps"].pop(); changes.append(changed)
        for changed in changes:
            with self.assertRaises(reaudit.ReauditError):
                reaudit.verify_retained_source(source, changed, SOURCE_ID, REPOSITORY)

    def test_reaudit_requires_successful_exact_main_workflow_and_gate(self):
        reviewer = run(REVIEW_ID, reviewer=True)
        reaudit.verify_reaudit_producer(reviewer, jobs(reviewer, reviewer=True), REVIEW_ID, REPOSITORY)
        for conclusion in ("failure", "cancelled", "skipped", None):
            with self.subTest(conclusion=conclusion), self.assertRaises(reaudit.ReauditError):
                reaudit.verify_reaudit_producer({**reviewer, "conclusion": conclusion},
                                               jobs(reviewer, reviewer=True), REVIEW_ID, REPOSITORY)
        changed = jobs(reviewer, reviewer=True)
        changed["jobs"][0]["steps"][0]["conclusion"] = "skipped"
        with self.assertRaises(reaudit.ReauditError):
            reaudit.verify_reaudit_producer(reviewer, changed, REVIEW_ID, REPOSITORY)


class RetainedSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        originals = self.root / "originals"
        originals.mkdir()
        pdf = originals / "PRIVATE-SOURCE.pdf"
        with fitz.open() as document:
            page = document.new_page()
            for number in range(18):
                page.insert_text((30, 45 + number * 28),
                                 "The company reported stronger demand and steady investment.")
            document.save(pdf)
        manifest = self.root / "manifest.json"
        manifest.write_text(json.dumps([{"process_local_path": str(pdf),
                                         "content_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()}]))
        self.source, self.reviewer = run(), run(REVIEW_ID, reviewer=True)
        self.context = {"date_folder": DATE, "producer_run_id": SOURCE_ID,
                        "execution_sha": self.source["head_sha"], "original_source_run_id": ""}
        self.saved = self.root / "saved"
        extract_sources(originals, manifest, self.saved, 1, source_context=self.context)
        self.restored = self.root / "restored"
        self.client = FakeR2()

    def create(self, **kwargs):
        def restore(key, destination, **options):
            self.assertEqual(key, f"_private-workflow-handoff/market-sources/{SOURCE_ID}/{DATE}/shard_0.tar.gz")
            shutil.copytree(self.saved, destination)
        self.output = io.StringIO()
        with mock.patch("private_workflow_handoff.download_directory", side_effect=restore), \
                mock.patch.object(ocr_numeric_evidence, "_read_tesseract", side_effect=AssertionError("OCR forbidden")), \
                contextlib.redirect_stdout(self.output):
            return reaudit.reaudit_retained(self.restored, self.source, jobs(self.source), self.reviewer,
                REPOSITORY, DATE, 1, "", client=self.client, bucket="private", **kwargs)

    def metadata(self, repository, suffix):
        self.assertEqual(repository, REPOSITORY)
        if suffix == REVIEW_ID:
            return self.reviewer
        self.assertEqual(suffix, f"{REVIEW_ID}/jobs?filter=latest&per_page=100")
        return jobs(self.reviewer, reviewer=True)

    def test_real_native_evidence_is_reaudited_without_rebinding_or_source_upload(self):
        before = (self.saved / audit.RECEIPT_NAME).read_bytes()
        value = self.create()
        self.assertEqual(before, (self.restored / audit.RECEIPT_NAME).read_bytes())
        self.assertEqual(value["source_context"], self.context)
        self.assertEqual(value["receipt_sha256"], hashlib.sha256(before).hexdigest())
        self.assertEqual(value["receipt_bytes"], len(before))
        self.assertEqual(len(self.client.puts), 1)
        put = self.client.puts[0]
        self.assertEqual(put["IfNoneMatch"], "*")
        self.assertLess(len(put["Body"]), reaudit.MAX_ATTESTATION)
        self.assertNotIn("PRIVATE", put["Body"].decode())
        self.assertNotIn("PRIVATE", self.output.getvalue())
        self.assertEqual(set(value), reaudit.FIELDS)
        context = reaudit.consume_attestation(self.restored, self.source, jobs(self.source), REVIEW_ID,
            REPOSITORY, DATE, 1, client=self.client, bucket="private", get_metadata=self.metadata)
        self.assertEqual(context, self.context)
        # The consumer must retain its original full validation after the new gate.
        result = audit.audit_sources(self.restored, 1, expected_source_context=context)
        self.assertTrue(result["source_contract_verified"])

    def test_changed_receipt_cannot_use_old_successful_attestation(self):
        self.create()
        with (self.restored / audit.RECEIPT_NAME).open("ab") as output:
            output.write(b"\n")
        with self.assertRaisesRegex(reaudit.ReauditError, "attestation_receipt_mismatch"):
            reaudit.consume_attestation(self.restored, self.source, jobs(self.source), REVIEW_ID,
                REPOSITORY, DATE, 1, client=self.client, bucket="private", get_metadata=self.metadata)

    def test_actual_pdf_consumer_executes_reattest_then_original_complete_validation(self):
        self.create()
        repository_root = Path(__file__).resolve().parents[1]
        workflow = (repository_root / ".github/workflows/market-views-latex-pdf.yml").read_text()
        block = workflow.split("      - name: Verify complete native PDF source receipt\n", 1)[1].split("      - name:", 1)[0]
        command = textwrap.dedent(block.split("        run: |\n", 1)[1])
        code = command.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        (self.root / "scripts").symlink_to(repository_root / "scripts", target_is_directory=True)
        target = self.root / "xhs_notes/dropbox" / DATE / "shard_0"
        target.parent.mkdir(parents=True)
        shutil.copytree(self.restored, target)
        runtime = self.root / "runtime"
        runtime.mkdir()
        environment = {"GITHUB_REPOSITORY": REPOSITORY, "SOURCE_HANDOFF_RUN_ID": SOURCE_ID,
            "EXPECTED_BANK_DATE": DATE, "EXPECTED_ARTICLES": "1", "NATIVE_REAUDIT_RUN_ID": REVIEW_ID,
            "NATIVE_QUALITY_FIXTURE_JSON": "", "RUNNER_TEMP": str(runtime)}
        real_run = subprocess.run
        validation_commands = []
        def runner(arguments, **kwargs):
            if arguments[0] == "gh":
                suffix = arguments[-1].split("/actions/runs/", 1)[1]
                values = {SOURCE_ID: self.source, f"{SOURCE_ID}/jobs?filter=latest&per_page=100": jobs(self.source),
                          REVIEW_ID: self.reviewer, f"{REVIEW_ID}/jobs?filter=latest&per_page=100": jobs(self.reviewer, reviewer=True)}
                result = json.dumps(values[suffix])
                return subprocess.CompletedProcess(arguments, 0, result if kwargs.get("text") else result.encode(), "")
            validation_commands.append(arguments)
            return real_run(arguments, **{**kwargs, "capture_output": True})
        def execute():
            with contextlib.chdir(self.root), mock.patch.dict(os.environ, environment), \
                    mock.patch("private_workflow_handoff.build_r2_client", return_value=self.client), \
                    mock.patch("private_workflow_handoff.r2_bucket", return_value="private"), \
                    mock.patch.object(subprocess, "run", side_effect=runner):
                exec(compile(code, "<native-consumer-workflow>", "exec"), {})
        execute()
        self.assertEqual([command[1:3] for command in validation_commands], [
            ["scripts/extract_native_market_sources.py", "validate"],
            ["scripts/audit_market_views_ocr_receipt.py", "--source-dir"]])
        self.assertTrue(json.loads((runtime / "market-views-native-source-audit.json").read_text())["source_contract_verified"])
        validation_commands.clear()
        self.reviewer["conclusion"] = "failure"
        with self.assertRaisesRegex(reaudit.ReauditError, "successful_reaudit_required"):
            execute()
        self.assertEqual(validation_commands, [])

    def test_altered_context_counts_sha_or_reviewer_rejected(self):
        value = self.create()
        identity = audit.receipt_identity(self.restored / audit.RECEIPT_NAME)
        changes = [("report_count", 2), ("report_count", True), ("receipt_sha256", "0" * 64),
                   ("source_run_attempt", 2), ("reaudit_run_attempt", 2), ("reaudit_run_id", "201"),
                   ("reaudit_execution_sha", "c" * 40), ("ocr_call_count", 1), ("extra", "PRIVATE")]
        for key, item in changes:
            with self.subTest(key=key), self.assertRaises(reaudit.ReauditError):
                reaudit.verify_attestation({**value, key: item}, self.source, self.reviewer,
                                          REPOSITORY, DATE, 1, identity)
        for key, item in (("date_folder", "261003"), ("producer_run_id", "101"), ("execution_sha", "c" * 40)):
            changed = copy.deepcopy(value)
            changed["source_context"][key] = item
            with self.subTest(context_key=key), self.assertRaises(reaudit.ReauditError):
                reaudit.verify_attestation(changed, self.source, self.reviewer, REPOSITORY, DATE, 1, identity)

    def test_rejected_source_and_numeric_fixture_never_write_attestation(self):
        (self.saved / audit.RECEIPT_NAME).write_text("{}")
        with self.assertRaises(ValueError):
            self.create()
        self.assertEqual(self.client.puts, [])

    def test_failed_numeric_fixture_never_writes_attestation(self):
        fixture = self.root / "fixtures.json"
        fixture.write_text(json.dumps({"schema": 1, "checks": [{"id": "absent_value", "source_pdf_sha256": "d" * 64,
            "page": 1, "expected_literal": "31%", "expected_bbox": [10, 10, 30, 30]}]}))
        with self.assertRaisesRegex(reaudit.ReauditError, "reaudit_fixture_rejected"):
            self.create(fixtures=fixture)
        self.assertEqual(self.client.puts, [])

    def test_attestation_integrity_and_duplicate_fields_rejected(self):
        self.create()
        key = self.client.puts[0]["Key"]
        raw, metadata = self.client.objects[key]
        self.client.objects[key] = (raw + b" ", metadata)
        with self.assertRaisesRegex(reaudit.ReauditError, "invalid_attestation_integrity"):
            reaudit.read_attestation(self.client, "private", key)
        raw = b'{"schema":1,"schema":1}'
        self.client.objects[key] = (raw, {"kind": reaudit.KIND, "sha256": hashlib.sha256(raw).hexdigest()})
        with self.assertRaisesRegex(reaudit.ReauditError, "duplicate_attestation_field"):
            reaudit.read_attestation(self.client, "private", key)


class WorkflowTests(unittest.TestCase):
    def test_workflow_only_restores_and_audits_in_main_with_no_ocr_install(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / reaudit.WORKFLOW).read_text()
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("scripts/reaudit_market_views_native_sources.py", workflow)
        self.assertIn(f"- name: {reaudit.AUDIT_STEP}", workflow)
        for forbidden in ("tesseract", "--enable-ocr", "extract_native_market_sources.py", "actions/upload-artifact", "upload-dir"):
            self.assertNotIn(forbidden, workflow)
        market = (root / ".github/workflows/market-views-latex-pdf.yml").read_text()
        block = market.split("      - name: Verify complete native PDF source receipt\n", 1)[1].split("      - name:", 1)[0]
        self.assertIn("if reaudit_run:", block)
        self.assertIn("context = consume_attestation(", block)
        self.assertIn("require_source_readiness(producer, source_jobs)", block)
        self.assertIn("scripts/extract_native_market_sources.py', 'validate'", block)
        self.assertIn("scripts/audit_market_views_ocr_receipt.py", block)
        regression = (root / ".github/workflows/wechat-pipeline-regression.yml").read_text()
        self.assertEqual(regression.count('".github/workflows/market-views-native-reaudit.yml"'), 2)
        self.assertIn("python scripts/test_reaudit_market_views_native_sources.py", regression)


if __name__ == "__main__":
    unittest.main()
