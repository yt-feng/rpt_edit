#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import copy
from datetime import timedelta
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock

import fitz

import ocr_numeric_evidence as numeric
import probe_market_views_ocr_fields as probe


try:
    TESSDATA = Path(os.environ.get("TESSDATA_PREFIX") or fitz.get_tessdata())
except RuntimeError:
    TESSDATA = Path("/tmp/market-views-probe-tessdata")
HAS_OCR = shutil.which("tesseract") is not None and all(
    (TESSDATA / f"{language}.traineddata").is_file() for language in probe.native.OCR_LANGUAGES.split("+"))


def setUpModule():
    if os.getenv("REQUIRE_MARKET_VIEWS_OCR_TESTS") == "1" and not HAS_OCR:
        raise RuntimeError("Cloud field-probe acceptance requires the actual Tesseract CLI and eng+chi_sim models")


class FieldProbeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.originals = self.root / "originals"
        self.originals.mkdir()
        self.manifest = self.originals / probe.native.MANIFEST_NAME
        self.fixtures = self.root / "fixtures.json"
        self.metadata = self.root / "producer.json"
        self.summary = self.root / "public-diagnostic.json"
        self.metadata.write_text(json.dumps({"id": 12345, "path": probe.DAILY_WORKFLOW, "status": "completed",
                                             "conclusion": "failure", "head_branch": "main", "head_sha": "a" * 40,
                                             "html_url": "https://private.invalid/producer"}))
        self.make_source()

    def tearDown(self):
        self.temporary.cleanup()

    def make_source(self, *, pages=1):
        path = self.originals / "PRIVATE-REPORT-TITLE.pdf"
        with fitz.open() as document:
            for _ in range(pages):
                page = document.new_page(width=595, height=842)
                page.insert_textbox(fitz.Rect(45, 45, 550, 120),
                                    "Private research report examines revenue margins and economic conditions. "
                                    "The original source includes assumptions and private supporting observations.", fontsize=12)
                page.insert_text((100, 200), "48", fontsize=24)
            document.save(path)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        self.rows = [{"process_local_path": f"/selected/{path.name}", "content_sha256": sha,
                      "dropbox_path": f"/zip_backup/261004/{path.name}"}]
        self.manifest.write_text(json.dumps(self.rows))
        with fitz.open(path) as document:
            word = next(word for word in document[0].get_text("words") if word[4] == "48")
        box = [word[0] - 3, word[1] - 3, word[2] + 3, word[3] + 3]
        self.checks = [{"id": "reported_value", "source_pdf_sha256": sha, "page": 1,
                        "expected_literal": "48", "expected_bbox": box}]
        self.fixtures.write_text(json.dumps({"schema": 1, "checks": self.checks}))

    def call(self, expected=1):
        with mock.patch("socket.create_connection", side_effect=AssertionError("No network")):
            return probe.probe_fields(self.originals, self.manifest, self.fixtures, self.metadata,
                                      date_folder="261004", source_run_id="12345", expected_articles=expected)

    def ocr_fixture(self, page, name, number):
        self.assertEqual(name, "field-probe")
        primary = page.get_text("text", sort=True).strip()
        words = page.get_text("words", sort=True)
        second = [{"bbox": [value * 450 / 72 for value in word[:4]], "text": word[4],
                   "block": word[5], "paragraph": 0, "line": word[6]} for word in words]
        crops = {index: [{"method": f"source-crop-psm-{psm}", "dpi": 600,
                          "literal": mention["literal"], "field_count": 1,
                          "input_pixel_sha256": "b" * 64} for psm in (6, 11)]
                 for index, mention in enumerate(numeric.numeric_mentions(primary))}
        with mock.patch.object(numeric, "_read_tesseract", return_value=second), mock.patch.object(numeric, "_crop_reads", return_value=crops):
            result = numeric.audit_numeric_evidence(page, primary, primary_words=words, tesseract_command="fixture-engine")
        return result["safe_text"], {"numeric_evidence": result["evidence"]}

    def assert_rejected_before_ocr(self, category, expected=1):
        with mock.patch.object(probe.native, "_ocr_page", side_effect=AssertionError("Must validate all sources first")) as ocr:
            with self.assertRaisesRegex(probe.ProbeError, category):
                self.call(expected)
        self.assertEqual(ocr.call_count, 0)

    def cli(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return probe.main(["--input-dir", str(self.originals), "--manifest", str(self.manifest),
                               "--fixtures", str(self.fixtures), "--producer-metadata", str(self.metadata),
                               "--source-run-id", "12345", "--date-folder", "261004", "--expected-articles", "1",
                               "--summary", str(self.summary)])

    def assert_single_page_probe_contract(self, result):
        self.assertTrue(result["original_batch_verified"])
        self.assertEqual(result["original_file_count"], 1)
        self.assertEqual(result["probed_page_count"], 1)
        self.assertEqual(result["fixture_count"], 1)
        self.assertTrue(result["page_probe_only"])
        self.assertFalse(result["complete_source_handoff"])
        self.assertFalse(result["production_acceptance"])
        for key in ("model_call_count", "provider_post_count", "pdf_count", "r2_source_admission_count"):
            self.assertEqual(result[key], 0)
        self.assertFalse((self.originals / probe.native.RECEIPT_NAME).exists())
        check = result["fixtures"][0]
        self.assertIs(type(check["matched"]), bool)
        self.assertEqual(result["success"], check["matched"])
        self.assertEqual(result["fixture_passed_count"], int(check["matched"]))
        self.assertEqual(result["fixture_acceptance"], "passed" if check["matched"] else "failed")
        self.assertEqual(result["category"], "passed" if check["matched"] else "numeric_fixture_failed")
        if check["matched"]:
            self.assertEqual(check["category"], "passed")
        else:
            self.assertIn(check["category"], {"position_missing", "field_unresolved", "value_mismatch", "ambiguous_match"})
            # A failed primary read must still produce the real secondary
            # numeric witness safely, without promoting it to acceptance.
            secondary = check["numeric_diagnostics"]["second_page_at_fixture"]
            self.assertGreater(len(secondary["candidates"]), 0)
            self.assertGreaterEqual(secondary["candidate_count"], len(secondary["candidates"]))
            for candidate in secondary["candidates"]:
                self.assertIsNotNone(probe.audit._diagnostic_bbox(candidate["bbox"]))
                self.assertIsNotNone(probe.audit._diagnostic_number(candidate["literal"]))
        raw = json.dumps(result, allow_nan=False)
        for private in ("PRIVATE", "Private research", "private.invalid", "primary_text", "source_pdf\"",
                        "https://", "http://", "pages/", "原报告", "数值待核对"):
            self.assertNotIn(private, raw)

    def test_real_pixels_numeric_receipt_and_production_matching_are_reused(self):
        with mock.patch.object(probe.native, "_ocr_page", side_effect=self.ocr_fixture) as ocr:
            result = self.call()
        self.assertEqual(ocr.call_count, 1)
        self.assertTrue(result["success"])
        self.assertTrue(result["original_batch_verified"])
        self.assertEqual(result["fixtures"][0]["category"], "passed")
        self.assertEqual(result["fixture_passed_count"], 1)
        self.assertTrue(result["page_probe_only"])
        self.assertFalse(result["complete_source_handoff"])
        self.assertFalse(result["production_acceptance"])
        self.assert_single_page_probe_contract(result)
        self.assertNotIn("reports", result)
        self.assertNotIn("complete", result)
        self.assertEqual(result["model_call_count"], 0)
        self.assertEqual(result["r2_source_admission_count"], 0)

    def test_known_page_numeric_failure_preserves_only_fixed_category(self):
        error = probe.native.SourceValidationError("PRIVATE source and engine details", category="numeric_crop_geometry_mismatch")
        with mock.patch.object(probe.native, "_ocr_page", side_effect=error):
            self.assertEqual(self.cli(), 2)
        summary = json.loads(self.summary.read_text())
        self.assertEqual(summary["category"], "numeric_crop_geometry_mismatch")
        self.assertNotIn("PRIVATE", json.dumps(summary))

    def test_unknown_page_error_category_cannot_enter_public_diagnostic(self):
        error = probe.native.SourceValidationError("PRIVATE details", category="PRIVATE source URL")
        with mock.patch.object(probe.native, "_ocr_page", side_effect=error):
            self.assertEqual(self.cli(), 2)
        summary = json.loads(self.summary.read_text())
        self.assertEqual(summary["category"], "page_ocr_or_numeric_validation_failed")
        self.assertNotIn("PRIVATE", json.dumps(summary))

    def test_geometry_failure_forwards_only_bounded_position_diagnostics(self):
        diagnostic = {"schema": 1, "record_id": "n0001", "psm": 6,
                      "size_matches": False,
                      "expected_pixel_size": [120, 40], "actual_pixel_size": [121, 40],
                      "private_source_name": "PRIVATE", "url": "https://PRIVATE.invalid"}
        error = probe.native.SourceValidationError("PRIVATE source", category="numeric_crop_geometry_mismatch",
                                                   geometry_diagnostics=diagnostic)
        with mock.patch.object(probe.native, "_ocr_page", side_effect=error):
            self.assertEqual(self.cli(), 2)
        summary = json.loads(self.summary.read_text())
        self.assertEqual(summary["geometry_diagnostics"]["actual_pixel_size"], [121, 40])
        self.assertNotIn("PRIVATE", json.dumps(summary))

    def test_other_failure_categories_cannot_smuggle_geometry_payload(self):
        result = probe.failure_summary("ocr_engine_failed", {"schema": 1, "psm": 6})
        self.assertNotIn("geometry_diagnostics", result)

    def test_wrong_date_and_count_are_rejected_before_any_ocr(self):
        self.assert_rejected_before_ocr("manifest_count_or_binding_invalid", expected=2)
        self.rows[0]["dropbox_path"] = "/zip_backup/261003/261004/PRIVATE-REPORT-TITLE.pdf"
        self.manifest.write_text(json.dumps(self.rows))
        self.assert_rejected_before_ocr("manifest_date_mismatch")

    def test_every_source_hash_is_checked_even_when_only_one_page_is_requested(self):
        alias = self.originals / "PRIVATE-UNPROBED-ALIAS.pdf"
        original = self.originals / "PRIVATE-REPORT-TITLE.pdf"
        shutil.copyfile(original, alias)
        self.rows.append({**self.rows[0], "process_local_path": f"/selected/{alias.name}"})
        self.manifest.write_text(json.dumps(self.rows))
        alias.write_bytes(alias.read_bytes() + b"changed after manifest")
        self.assert_rejected_before_ocr("original_hash_mismatch", expected=2)
        alias.write_bytes(original.read_bytes())
        self.rows[1]["dropbox_path"] = "/zip_backup/261003/PRIVATE-UNPROBED-ALIAS.pdf"
        self.manifest.write_text(json.dumps(self.rows))
        self.assert_rejected_before_ocr("manifest_date_mismatch", expected=2)

    def test_missing_extra_and_symlinked_originals_are_rejected_before_ocr(self):
        path = self.originals / "PRIVATE-REPORT-TITLE.pdf"
        original = path.read_bytes()
        path.unlink()
        self.assert_rejected_before_ocr("original_inventory_mismatch")
        path.write_bytes(original)
        extra = self.originals / "PRIVATE-EXTRA.pdf"
        extra.write_bytes(original)
        self.assert_rejected_before_ocr("original_inventory_mismatch")
        extra.unlink()
        link = self.originals / "unsafe-metadata.json"
        link.symlink_to(self.metadata)
        self.assert_rejected_before_ocr("original_symlink_rejected")

    def test_damaged_and_encrypted_originals_reject_before_ocr(self):
        path = self.originals / "PRIVATE-REPORT-TITLE.pdf"
        healthy = path.read_bytes()
        path.write_bytes(b"%PDF-1.7\nnot a complete document")
        self.rows[0]["content_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(self.rows))
        self.assert_rejected_before_ocr("damaged_original_pdf|unsupported_original_pdf")
        encrypted = self.root / "encrypted.pdf"
        with fitz.open(stream=healthy, filetype="pdf") as document:
            document.save(encrypted, encryption=fitz.PDF_ENCRYPT_AES_256, owner_pw="fixture", user_pw="fixture")
        path.write_bytes(encrypted.read_bytes())
        self.rows[0]["content_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(self.rows))
        self.assert_rejected_before_ocr("unsupported_original_pdf")

    def test_all_fixture_hashes_pages_and_boxes_are_checked_before_ocr(self):
        for category, field, value in (("fixture_source_missing", "source_pdf_sha256", "f" * 64),
                                       ("fixture_page_out_of_bounds", "page", 2),
                                       ("fixture_bbox_out_of_bounds", "expected_bbox", [10, 10, 700, 800])):
            checks = copy.deepcopy(self.checks)
            checks.append({**checks[0], "id": "invalid_later_field", field: value})
            self.fixtures.write_text(json.dumps({"schema": 1, "checks": checks}))
            with self.subTest(category=category):
                self.assert_rejected_before_ocr(category)

    def test_duplicate_aliases_and_same_page_fixtures_run_only_one_ocr(self):
        alias = self.originals / "PRIVATE-ALIAS.pdf"
        shutil.copyfile(self.originals / "PRIVATE-REPORT-TITLE.pdf", alias)
        self.rows.append({**self.rows[0], "process_local_path": f"/selected/{alias.name}"})
        self.manifest.write_text(json.dumps(self.rows))
        self.fixtures.write_text(json.dumps({"schema": 1, "checks": self.checks + [{**self.checks[0], "id": "same_field_again"}]}))
        with mock.patch.object(probe.native, "_ocr_page", side_effect=self.ocr_fixture) as ocr:
            result = self.call(expected=2)
        self.assertEqual(ocr.call_count, 1)
        self.assertEqual(result["original_file_count"], 2)
        self.assertEqual(result["unique_original_content_count"], 1)
        self.assertEqual(result["probed_page_count"], 1)
        self.assertEqual(result["fixture_passed_count"], 2)

    def test_partial_page_lookup_is_not_a_complete_source_receipt(self):
        (self.originals / "PRIVATE-REPORT-TITLE.pdf").unlink()
        self.make_source(pages=3)
        self.checks[0]["page"] = 3
        self.fixtures.write_text(json.dumps({"schema": 1, "checks": self.checks}))
        with mock.patch.object(probe.native, "_ocr_page", side_effect=self.ocr_fixture) as ocr:
            result = self.call()
        self.assertEqual(ocr.call_count, 1)
        self.assertEqual(result["probed_page_count"], 1)
        self.assertEqual(result["fixtures"][0]["page"], 3)
        self.assertFalse(result["complete_source_handoff"])
        self.assertNotIn("page_count", result)
        self.assertFalse((self.originals / probe.native.RECEIPT_NAME).exists())

    def test_failed_fixture_exits_three_and_preserves_only_sanitized_numeric_evidence(self):
        self.checks[0]["expected_literal"] = "49"
        self.fixtures.write_text(json.dumps({"schema": 1, "checks": self.checks}))
        with mock.patch.object(probe.native, "_ocr_page", side_effect=self.ocr_fixture):
            self.assertEqual(self.cli(), 3)
        result = json.loads(self.summary.read_text())
        self.assertFalse(result["success"])
        self.assertEqual(result["fixtures"][0]["category"], "value_mismatch")
        self.assertIn("numeric_diagnostics", result["fixtures"][0])
        raw = self.summary.read_text()
        for private in ("PRIVATE", "private.invalid", "source_pdf\"", "primary_text", "pages/", "原报告", "数值待核对"):
            self.assertNotIn(private, raw)
        self.assertFalse(result["production_acceptance"])
        self.assert_single_page_probe_contract(result)

    def test_preflight_error_and_engine_error_exit_two_without_private_exception_text(self):
        self.rows[0]["content_sha256"] = "e" * 64
        self.manifest.write_text(json.dumps(self.rows))
        self.assertEqual(self.cli(), 2)
        self.assertEqual(json.loads(self.summary.read_text())["category"], "original_hash_mismatch")
        self.rows[0]["content_sha256"] = self.checks[0]["source_pdf_sha256"]
        self.manifest.write_text(json.dumps(self.rows))
        with mock.patch.object(probe.native, "_ocr_page", side_effect=RuntimeError("PRIVATE https://private.invalid secret")):
            self.assertEqual(self.cli(), 2)
        self.assertEqual(json.loads(self.summary.read_text())["category"], "page_ocr_or_numeric_validation_failed")
        self.assertNotIn("PRIVATE", self.summary.read_text())
        self.assertNotIn("private.invalid", self.summary.read_text())

    def test_original_and_manifest_mutations_during_probe_are_detected(self):
        original_manifest = self.manifest.read_bytes()
        for target in ("manifest", "original"):
            self.manifest.write_bytes(original_manifest)
            path = self.originals / "PRIVATE-REPORT-TITLE.pdf"
            original_pdf = path.read_bytes()

            def mutate(page, name, number):
                result = self.ocr_fixture(page, name, number)
                if target == "manifest":
                    self.manifest.write_bytes(original_manifest + b" ")
                else:
                    path.write_bytes(original_pdf + b" changed")
                return result

            with self.subTest(target=target), mock.patch.object(probe.native, "_ocr_page", side_effect=mutate):
                with self.assertRaisesRegex(probe.ProbeError, "manifest_changed|original_hash_mismatch"):
                    self.call()
            path.write_bytes(original_pdf)

    def test_fixture_and_producer_inputs_cannot_change_during_probe(self):
        for path in (self.fixtures, self.metadata):
            original = path.read_bytes()

            def mutate(page, name, number):
                result = self.ocr_fixture(page, name, number)
                path.write_bytes(original + b" ")
                return result

            with self.subTest(input=path.name), mock.patch.object(probe.native, "_ocr_page", side_effect=mutate):
                with self.assertRaisesRegex(probe.ProbeError, "probe_inputs_changed"):
                    self.call()
            path.write_bytes(original)

    def test_oversized_page_cannot_be_rendered_before_the_numeric_pixel_bound(self):
        path = self.originals / "PRIVATE-REPORT-TITLE.pdf"
        path.unlink()
        with fitz.open() as document:
            page = document.new_page(width=5000, height=5000)
            page.insert_text((100, 200), "48", fontsize=24)
            document.save(path)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        self.rows[0]["content_sha256"] = sha
        self.checks[0]["source_pdf_sha256"] = sha
        self.manifest.write_text(json.dumps(self.rows))
        self.fixtures.write_text(json.dumps({"schema": 1, "checks": self.checks}))
        self.assert_rejected_before_ocr("fixture_page_render_bound_exceeded")

    def test_producer_must_be_the_exact_completed_daily_run_on_main(self):
        good = json.loads(self.metadata.read_text())
        for field, value in (("id", 54321), ("path", ".github/workflows/other.yml"), ("head_branch", "feature"),
                             ("status", "in_progress"), ("conclusion", "cancelled"), ("head_sha", "bad")):
            self.metadata.write_text(json.dumps({**good, field: value}))
            with self.subTest(field=field):
                self.assert_rejected_before_ocr("original_daily_producer_not_verified")

    def test_fixture_format_rejects_prose_duplicate_keys_nan_and_oversized_input(self):
        invalid = []
        for change in ({"expected_literal": "48 SECRET"}, {"unknown": "private"}, {"page": True},
                       {"expected_bbox": [0, 0, float("nan"), 100]}, {"expected_literal": "48\n%"}):
            invalid.append(json.dumps({"schema": 1, "checks": [{**self.checks[0], **change}]}))
        invalid.extend(('{"schema":0,"schema":1,"checks":[]}', "x" * (probe.FIXTURE_BYTE_LIMIT + 1)))
        for raw in invalid:
            self.fixtures.write_text(raw)
            with self.subTest(kind=len(raw)), mock.patch.object(probe.native, "_ocr_page") as ocr:
                with self.assertRaises(probe.ProbeError):
                    self.call()
                self.assertEqual(ocr.call_count, 0)

    def make_archive_context(self):
        import archive_market_views_originals as archive
        from mineru_task_ledger import encoded, digest
        self.metadata.write_text(json.dumps({"id": 12345, "path": archive.WORKFLOW, "status": "completed",
            "conclusion": "success", "event": "workflow_dispatch", "head_branch": "main", "head_sha": "a" * 40,
            "repository": {"full_name": "owner/repo"}, "html_url": "https://PRIVATE.invalid"}))
        raw, bindings, _ = archive.checked_inputs(self.originals, len(self.rows), "261004")
        created = archive.now_utc()
        self.archive_receipt = self.originals / archive.RECEIPT
        self.archive_receipt.write_bytes(encoded({"schema_version": 1, "kind": archive.KIND, "source_ready": False,
            "source_context": archive.context("12345", "261004", "a" * 40), "report_count": len(self.rows),
            "manifest_sha256": digest(raw), "original_inventory": bindings, "archive_sha256": "c" * 64,
            "archive_bytes": 100, "created_at_utc": created.isoformat(),
            "expires_at_utc": (created + timedelta(days=7)).isoformat(),
            "expiry_policy": "restore-disabled-after-7-days", "physical_deletion_guaranteed": False}))
        self.page_checks = self.root / "page-checks.json"
        self.page_checks.write_text(json.dumps({"schema": 1, "pages": [{"source_ordinal": 1, "page": 1}]}))

    def call_pages(self):
        with mock.patch("socket.create_connection", side_effect=AssertionError("No network")):
            return probe.probe_pages(self.originals, self.manifest, self.page_checks, self.metadata,
                date_folder="261004", source_run_id="12345", expected_articles=len(self.rows),
                source_kind="original-archive", repository="owner/repo")

    def raw_fixture(self, page):
        primary = page.get_text("text", sort=True).strip()
        return primary, page.get_text("words", sort=True), "fixture-models", {
            "selection": "geometric-sorted", "sorted_readability": probe._readability_projection(primary, allow_sparse_ocr=True)}

    def test_archive_producer_requires_exact_completed_manual_main_repository(self):
        self.make_archive_context()
        good = json.loads(self.metadata.read_text())
        self.assertEqual(probe.verify_producer(self.metadata, "12345", source_kind="original-archive",
                                              repository="owner/repo"), "a" * 40)
        with self.assertRaisesRegex(probe.ProbeError, "original_daily_producer_not_verified"):
            probe.verify_producer(self.metadata, "12345")
        for change in ({"event": "push"}, {"status": "in_progress"}, {"conclusion": "cancelled"},
                       {"repository": {"full_name": "other/repo"}}, {"head_branch": "other"}, {"id": 9}):
            self.metadata.write_text(json.dumps({**good, **change}))
            with self.subTest(change=change), self.assertRaises(probe.ProbeError):
                self.call_pages()

    def test_archive_numeric_fixtures_keep_the_production_expected_value_gate(self):
        self.make_archive_context()
        with mock.patch.object(probe.native, "_ocr_page", side_effect=self.ocr_fixture):
            result = probe.probe_fields(self.originals, self.manifest, self.fixtures, self.metadata,
                date_folder="261004", source_run_id="12345", expected_articles=1,
                source_kind="original-archive", repository="owner/repo")
        self.assertTrue(result["success"])
        self.assertEqual(result["source_kind"], "original-archive")
        self.checks[0]["expected_literal"] = "49"
        self.fixtures.write_text(json.dumps({"schema": 1, "checks": self.checks}))
        with mock.patch.object(probe.native, "_ocr_page", side_effect=self.ocr_fixture):
            result = probe.probe_fields(self.originals, self.manifest, self.fixtures, self.metadata,
                date_folder="261004", source_run_id="12345", expected_articles=1,
                source_kind="original-archive", repository="owner/repo")
        self.assertFalse(result["success"])
        self.assertEqual(result["fixtures"][0]["category"], "value_mismatch")

    def test_page_selectors_are_bounded_and_cannot_carry_golden_values_or_prose(self):
        self.make_archive_context()
        for request in ({"schema": 1, "pages": [{"source_ordinal": True, "page": 1}]},
                        {"schema": 1, "pages": [{"source_ordinal": 1, "page": 0}]},
                        {"schema": 1, "pages": [{"source_ordinal": 1, "page": 1, "expected_literal": "48"}]},
                        {"schema": 1, "pages": [{"source_ordinal": 1, "page": 1}] * 2},
                        {"schema": 1, "pages": [{"source_ordinal": 1, "page": n} for n in range(1, 10)]}):
            self.page_checks.write_text(json.dumps(request))
            with self.subTest(request=request), mock.patch.object(probe, "_raw_page_ocr") as engine:
                with self.assertRaises(probe.ProbeError):
                    self.call_pages()
                engine.assert_not_called()

    def test_archive_receipt_date_count_hash_source_and_expiry_checked_before_ocr(self):
        self.make_archive_context()
        good = json.loads(self.archive_receipt.read_text())
        for change in ({"source_ready": True}, {"report_count": 2}, {"manifest_sha256": "f" * 64},
                       {"source_context": {**good["source_context"], "original_source_run_id": "888"}},
                       {"source_context": {**good["source_context"], "date_folder": "261003"}},
                       {"expires_at_utc": good["created_at_utc"]}):
            self.archive_receipt.write_text(json.dumps({**good, **change}))
            with self.subTest(change=change), mock.patch.object(probe, "_raw_page_ocr") as engine:
                with self.assertRaisesRegex(probe.ProbeError, "original_archive_receipt_not_verified"):
                    self.call_pages()
                engine.assert_not_called()

    def test_all_originals_checked_before_an_ordinal_page_probe(self):
        alias = self.originals / "PRIVATE-UNPROBED.pdf"
        shutil.copyfile(self.originals / "PRIVATE-REPORT-TITLE.pdf", alias)
        self.rows.append({**self.rows[0], "process_local_path": f"/selected/{alias.name}"})
        self.manifest.write_text(json.dumps(self.rows))
        self.make_archive_context()
        alias.write_bytes(alias.read_bytes() + b" changed")
        with mock.patch.object(probe, "_raw_page_ocr") as engine:
            with self.assertRaisesRegex(probe.ProbeError, "original_hash_mismatch"):
                self.call_pages()
            engine.assert_not_called()

    def test_invalid_ordinal_and_page_reject_before_ocr(self):
        self.make_archive_context()
        for ordinal, page in ((2, 1), (1, 2)):
            self.page_checks.write_text(json.dumps({"schema": 1, "pages": [{"source_ordinal": ordinal, "page": page}]}))
            with self.subTest(ordinal=ordinal, page=page), mock.patch.object(probe, "_raw_page_ocr") as engine:
                with self.assertRaises(probe.ProbeError):
                    self.call_pages()
                engine.assert_not_called()

    def test_unreadable_raw_ocr_has_real_counts_and_reason_without_private_text(self):
        self.make_archive_context()
        opaque = "A" * 120 + "\nPRIVATE"
        with mock.patch.object(probe, "_raw_page_ocr", return_value=(opaque, [], "private-models", {
            "selection": "rejected", "sorted_readability": probe._readability_projection(opaque, allow_sparse_ocr=True)})), \
             mock.patch.object(probe, "audit_numeric_evidence") as numeric_audit:
            result = self.call_pages()
        numeric_audit.assert_not_called()
        page = result["pages"][0]
        self.assertEqual(page["ocr_readability"]["reason"], "opaque_ascii_runs")
        self.assertEqual(page["ocr_readability"]["long_ascii_characters"], 120)
        self.assertFalse(page["ocr_readability"]["accepted"])
        self.assertEqual(page["category"], "ocr_readability_rejected")
        self.assertFalse(result["success"])
        self.assertTrue(result["diagnostic_complete"])
        self.assertEqual(result["fixture_acceptance"], "not_requested")
        for private in ("PRIVATE", "private-models", opaque, "https://", "primary_text"):
            self.assertNotIn(private, json.dumps(result))
        for key in ("model_call_count", "provider_post_count", "pdf_count", "r2_source_admission_count"):
            self.assertEqual(result[key], 0)
        self.assertFalse(result["production_acceptance"])
        self.assertFalse(result["complete_source_handoff"])

    def test_raw_probe_reuses_production_layout_and_same_textpage_words_once(self):
        source_flow = "Research market outlook shows economic conditions with growth analysis"
        joined = source_flow.replace(" ", "")
        class Page:
            def __init__(self):
                self.textpage = object()
                self.ocr_count = 0
                self.word_sorts = []
            def get_textpage_ocr(self, **options):
                self.ocr_count += 1
                return self.textpage
            def get_text(self, kind, *, textpage, sort):
                if textpage is not self.textpage:
                    raise AssertionError("Different OCR result")
                if kind == "words":
                    self.word_sorts.append(sort)
                    return []
                return joined if sort else source_flow
        page = Page()
        models = self.root / "models"
        models.mkdir()
        for language in probe.native.OCR_LANGUAGES.split("+"):
            (models / f"{language}.traineddata").write_bytes(b"fixture")
        with mock.patch.object(probe.fitz, "get_tessdata", return_value=str(models)):
            primary, _, _, diagnostic = probe._raw_page_ocr(page)
        self.assertEqual(primary, source_flow)
        self.assertEqual(page.ocr_count, 1)
        self.assertEqual(page.word_sorts, [False])
        self.assertEqual(diagnostic["selection"], "source-flow")
        self.assertEqual(diagnostic["sorted_readability"]["reason"], "opaque_ascii_runs")
        self.assertNotIn(source_flow, json.dumps(diagnostic))
        self.assertNotIn(joined, json.dumps(diagnostic))

    def test_real_textpage_glued_rotated_labels_map_to_all_covering_source_words(self):
        with fitz.open() as document:
            page = document.new_page(width=612, height=792)
            page.insert_text((50, 50), "Robot shipment value by destination research monthly trade statistics", fontsize=11)
            for index in range(30):
                page.insert_text((80 + index * 9, 240), str(201001 + index), fontsize=10, rotate=90)
            textpage = page.get_textpage()
            text = page.get_text("text", textpage=textpage, sort=True).strip()
            words = page.get_text("words", textpage=textpage, sort=True)
            result = probe._opaque_run_positions(text, words, page.rect)
            source_boxes = [word[:4] for word in words if word[4].isdigit()]
            self.assertEqual(result["status"], "mapped")
            self.assertEqual(result["long_ascii_characters"], 180)
            self.assertEqual(result["mapped_run_count"], 1)
            self.assertEqual(result["runs"][0]["source_word_count"], 30)
            expected = [min(box[0] for box in source_boxes), min(box[1] for box in source_boxes),
                        max(box[2] for box in source_boxes), max(box[3] for box in source_boxes)]
            self.assertEqual(result["runs"][0]["bbox"], [round(value, 4) for value in expected])
            flow = page.get_text("text", textpage=textpage, sort=False).strip()
            self.assertEqual(probe._opaque_run_positions(flow, page.get_text("words", textpage=textpage, sort=False), page.rect)["run_count"], 0)
        self.assertNotIn("201001", json.dumps(result))
        self.assertNotIn("Robot", json.dumps(result))

    def test_duplicate_long_runs_use_character_offsets_and_never_collapse_source_positions(self):
        text = "Q" * 30 + "\n" + "Q" * 30
        words = [(10, 10, 90, 20, "Q" * 30), (10, 60, 90, 70, "Q" * 30)]
        result = probe._opaque_run_positions(text, words, [0, 0, 200, 200])
        self.assertEqual(result["run_count"], 2)
        self.assertEqual(result["mapped_run_count"], 2)
        self.assertEqual([row["bbox"] for row in result["runs"]], [[10, 10, 90, 20], [10, 60, 90, 70]])
        self.assertEqual([row["characters"] for row in result["runs"]], [30, 30])
        self.assertNotIn("Q" * 30, json.dumps(result))

    def test_wrong_character_order_or_ambiguous_duplicate_boundaries_cannot_guess_a_box(self):
        cases = [("A" * 25 + " " + "B" * 25,
                  [(10, 10, 90, 20, "B" * 25), (10, 60, 90, 70, "A" * 25)], "text_order_mismatch"),
                 ("A" * 30 + " " + "A" * 31,
                  [(10, 10, 90, 20, "A" * 31), (10, 60, 90, 70, "A" * 30)], "word_boundary_mismatch")]
        for text, words, reason in cases:
            with self.subTest(reason=reason):
                result = probe._opaque_run_positions(text, words, [0, 0, 200, 200])
                self.assertEqual(result["status"], reason)
                self.assertEqual(result["mapped_run_count"], 0)
                self.assertTrue(all(row["bbox"] is None for row in result["runs"]))
                self.assertEqual(result["returned_run_count"], 2)
                self.assertIsNotNone(probe._safe_opaque_positions(result, [0, 0, 200, 200]))

    def test_opaque_position_geometry_is_bounded_typed_and_cannot_be_clamped_into_a_fake_page(self):
        text = "A" * 30
        for box in ([True, 10, 90, 20], [-1, 10, 90, 20], [10, 10, 201, 20],
                    [10, float("nan"), 90, 20], [90, 10, 10, 20], [10, 10, 90, float("inf")],
                    [10, 10, 10 ** 1000, 20]):
            with self.subTest(box=box):
                result = probe._opaque_run_positions(text, [{"bbox": box, "text": text, "secret": "PRIVATE"}], [0, 0, 200, 200])
                self.assertEqual(result["status"], "word_geometry_invalid")
                self.assertIsNone(result["runs"][0]["bbox"])
                self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertIsNone(probe._page_bounds([0, 0, 10 ** 1000, 200]))
        rect = [0, 0, 200.123456, 300.654321]
        result = probe._opaque_run_positions(text, [(0, 10, rect[2], 20, text)], rect)
        self.assertIsNotNone(probe._safe_opaque_positions(result, rect), "Rounded edge coordinates must remain inside the real page")

    def test_opaque_position_limits_report_truncation_and_missing_counts_explicitly(self):
        count = probe.MAX_OPAQUE_RUNS + 3
        text = "\n".join("A" * 25 for _ in range(count))
        words = [(10, index * 2 + 1, 90, index * 2 + 2, "A" * 25) for index in range(count)]
        result = probe._opaque_run_positions(text, words, [0, 0, 100, count * 2 + 10])
        self.assertEqual(result["run_count"], count)
        self.assertEqual(result["long_ascii_characters"], count * 25)
        self.assertEqual(len(result["runs"]), probe.MAX_OPAQUE_RUNS)
        self.assertTrue(result["truncated"])
        self.assertEqual(result["mapped_run_count"], probe.MAX_OPAQUE_RUNS)
        self.assertIsNotNone(probe._safe_opaque_positions(result, [0, 0, 100, count * 2 + 10]))
        result = probe._opaque_run_positions("A" * 25, [words[0]] * (probe.MAX_POSITION_WORDS + 1), [0, 0, 100, 100])
        self.assertEqual(result["status"], "word_bound_exceeded")
        self.assertIsNone(result["runs"][0]["bbox"])
        result = probe._opaque_run_positions("A" * (probe.MAX_POSITION_TEXT_BYTES + 1), [], [0, 0, 100, 100])
        self.assertEqual(result["status"], "input_bound_exceeded")
        self.assertFalse(result["counts_available"])
        self.assertEqual(result["runs"], [])
        self.assertIsNotNone(probe._safe_opaque_positions(result, [0, 0, 100, 100]))

    def test_all_rejected_recognition_candidates_get_positions_from_one_default_textpage(self):
        class Page:
            rect = fitz.Rect(0, 0, 200, 200)
            def __init__(self):
                self.textpage, self.ocr_count, self.word_sorts = object(), 0, []
            def get_textpage_ocr(self, **options):
                self.ocr_count += 1
                return self.textpage
            def get_text(self, kind, *, textpage, sort):
                self.assert_same(textpage)
                text = "A" * 30 if sort else "B" * 35
                if kind == "words":
                    self.word_sorts.append(sort)
                    y = 10 if sort else 60
                    return [(10, y, 90, y + 10, text)]
                return text
            def assert_same(self, textpage):
                if textpage is not self.textpage: raise AssertionError("A new OCR TextPage was used")
        page = Page()
        primary = "C" * 40
        def recognize(observed, *args, **options):
            textpage = observed.get_textpage_ocr()
            sorted_text = observed.get_text("text", textpage=textpage, sort=True)
            flow = observed.get_text("text", textpage=textpage, sort=False)
            return primary, [{"bbox": [10, 120, 90, 130], "text": primary}], "private-models", {}, {
                "selection": "rejected", "recognition_attempted": True,
                "sorted_readability": probe._readability_projection(sorted_text),
                "source_flow_readability": probe._readability_projection(flow),
                "alternate_readability": probe._readability_projection(primary)}
        with mock.patch.object(probe.native, "_recognize_ocr_page", side_effect=recognize):
            _, _, _, layout = probe._raw_page_ocr(page)
        self.assertEqual(page.ocr_count, 1)
        self.assertEqual(page.word_sorts, [True, False])
        self.assertEqual(set(layout["opaque_runs"]), probe.OPAQUE_CANDIDATES)
        self.assertEqual([layout["opaque_runs"][key]["runs"][0]["characters"]
                          for key in ("geometric-sorted", "source-flow", "full-page-psm11")], [30, 35, 40])
        self.assertNotIn(primary, json.dumps(layout))
        self.assertNotIn("private-models", json.dumps(layout))

    def test_opaque_public_projection_rejects_bad_types_duplicate_indices_and_private_keys(self):
        self.make_archive_context()
        primary = "A" * 30
        rect = [0, 0, 612, 792]
        positions = probe._opaque_run_positions(primary, [(10, 10, 90, 20, primary)], rect)
        for change in ("count_bool", "box_bool", "nan", "ordinal", "oversize", "status", "status_list",
                       "status_dict", "huge_coordinate", "mapped"):
            invalid = copy.deepcopy(positions)
            if change == "count_bool": invalid["run_count"] = True
            elif change == "box_bool": invalid["runs"][0]["bbox"][0] = False
            elif change == "nan": invalid["runs"][0]["bbox"][0] = float("nan")
            elif change == "ordinal": invalid["runs"][0]["run"] = 2
            elif change == "oversize": invalid["runs"] *= probe.MAX_OPAQUE_RUNS + 1
            elif change == "status": invalid["status"] = "PRIVATE"
            elif change == "status_list": invalid["status"] = ["mapped"]
            elif change == "status_dict": invalid["status"] = {"private": "PRIVATE"}
            elif change == "huge_coordinate": invalid["runs"][0]["bbox"][0] = 10 ** 1000
            else: invalid["mapped_run_count"] = 0
            with self.subTest(change=change):
                self.assertIsNone(probe._safe_opaque_positions(invalid, rect))
        positions["raw"] = primary
        positions["runs"][0]["text"] = "PRIVATE"
        layout = {"selection": "rejected", "sorted_readability": probe._readability_projection(primary),
                  "opaque_runs": {"geometric-sorted": positions, "PRIVATE_SOURCE": positions}}
        with mock.patch.object(probe, "_raw_page_ocr", return_value=(primary, [], "PRIVATE-models", layout)), \
                mock.patch.object(probe, "audit_numeric_evidence") as audit:
            result = self.call_pages()
        projected = result["pages"][0]["ocr_layout"]["opaque_runs"]
        self.assertEqual(set(projected), {"geometric-sorted"})
        self.assertEqual(projected["geometric-sorted"]["runs"][0]["characters"], 30)
        self.assertEqual(result["pages"][0]["category"], "ocr_readability_rejected")
        self.assertFalse(result["success"])
        self.assertFalse(result["production_acceptance"])
        self.assertFalse(result["complete_source_handoff"])
        audit.assert_not_called()
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn(primary, json.dumps(result))

    def test_raw_probe_uses_the_shared_primary_recognition_before_the_numeric_stage(self):
        primary = "Research market outlook shows economic conditions with growth analysis"
        words = [{"bbox": [2, 3, 10, 14], "text": "Research", "block": 0, "paragraph": 0, "line": 0}]
        diagnostic = {"selection": "full-page-psm11", "recognition_attempted": True,
                      "sorted_readability": probe._readability_projection("A" * 120),
                      "source_flow_readability": probe._readability_projection("A" * 120),
                      "source_flow_same_glyphs": True,
                      "alternate_readability": probe._readability_projection(primary)}
        with mock.patch.object(probe.native, "_recognize_ocr_page",
                               return_value=(primary, words, "private-models", {"recognition": {"raw": "PRIVATE"}}, diagnostic)) as recognize, \
                mock.patch.object(probe, "audit_numeric_evidence") as audit:
            result = probe._raw_page_ocr(object())
        self.assertEqual(result, (primary, words, "private-models", diagnostic))
        self.assertEqual(recognize.call_count, 1)
        self.assertTrue(recognize.call_args.kwargs["allow_rejected"])
        audit.assert_not_called()

    def test_rejected_source_flow_and_alternate_counts_are_independent_without_private_payloads(self):
        self.make_archive_context()
        primary = "A" * 120
        flow = "B" * 150
        layout = {"selection": "rejected", "recognition_attempted": True, "source_flow_same_glyphs": False,
                  "sorted_readability": {**probe._readability_projection(primary), "raw": "PRIVATE"},
                  "source_flow_readability": {**probe._readability_projection(flow), "words": "PRIVATE"},
                  "alternate_readability": {**probe._readability_projection(primary), "image": "PRIVATE"},
                  "recognition": {"primary_words": ["PRIVATE"]}, "private_text": "PRIVATE"}
        with mock.patch.object(probe, "_raw_page_ocr", return_value=(primary, [], "private-models", layout)), \
                mock.patch.object(probe, "audit_numeric_evidence") as audit:
            result = self.call_pages()
        counts = result["pages"][0]["ocr_layout"]
        self.assertEqual(counts["sorted_readability"]["long_ascii_characters"], 120)
        self.assertEqual(counts["source_flow_readability"]["long_ascii_characters"], 150)
        self.assertEqual(counts["alternate_readability"]["long_ascii_characters"], 120)
        self.assertTrue(counts["recognition_attempted"])
        self.assertFalse(counts["source_flow_same_glyphs"])
        self.assertEqual(result["pages"][0]["category"], "ocr_readability_rejected")
        audit.assert_not_called()
        self.assertFalse(result["success"])
        self.assertFalse(result["production_acceptance"])
        for value in ("PRIVATE", "private-models", primary, flow, "primary_words", "https://"):
            self.assertNotIn(value, json.dumps(result))

    def test_alternate_readable_probe_still_uses_numeric_consumer_and_no_acceptance_shortcut(self):
        self.make_archive_context()
        primary = "Research market outlook shows economic conditions with growth analysis"
        layout = {"selection": "full-page-psm11", "recognition_attempted": True,
                  "sorted_readability": probe._readability_projection("A" * 120),
                  "source_flow_readability": probe._readability_projection("B" * 150),
                  "alternate_readability": probe._readability_projection(primary)}
        evidence = {"source_num_count": 0, "verified_count": 0, "corrected_count": 0,
                    "unresolved_count": 0, "secondary_only_count": 0, "observed_num_count": 0}
        with mock.patch.object(probe, "_raw_page_ocr", return_value=(primary, [], "models", layout)), \
                mock.patch.object(probe, "audit_numeric_evidence", return_value={"safe_text": primary, "evidence": evidence}) as audit, \
                mock.patch.object(probe, "validate_numeric_evidence") as validate:
            result = self.call_pages()
        self.assertEqual(audit.call_count, 1)
        self.assertEqual(validate.call_count, 1)
        self.assertEqual(result["pages"][0]["ocr_layout"]["selection"], "full-page-psm11")
        self.assertEqual(result["pages"][0]["category"], "page_checks_completed")
        self.assertTrue(result["success"])
        self.assertFalse(result["production_acceptance"])
        self.assertFalse(result["complete_source_handoff"])
        self.assertEqual(result["fixture_acceptance"], "not_requested")

    def test_page_layout_projection_has_both_counts_without_copying_private_keys(self):
        self.make_archive_context()
        primary = "Research market outlook shows economic conditions with growth analysis"
        sorted_counts = probe._readability_projection(primary.replace(" ", ""), allow_sparse_ocr=True)
        layout = {"selection": "source-flow", "sorted_readability": {**sorted_counts, "raw": "PRIVATE"},
                  "private_text": primary}
        error = numeric.NumericEvidenceError("Numeric crop geometry differs from its positioned source field")
        with mock.patch.object(probe, "_raw_page_ocr", return_value=(primary, [], "models", layout)), \
             mock.patch.object(probe, "audit_numeric_evidence", side_effect=error):
            result = self.call_pages()
        projected = result["pages"][0]["ocr_layout"]
        self.assertEqual(projected["selection"], "source-flow")
        self.assertFalse(projected["sorted_readability"]["accepted"])
        self.assertTrue(projected["selected_readability"]["accepted"])
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn(primary, json.dumps(result))

    def test_page_numeric_failure_preserves_only_category_and_safe_geometry(self):
        self.make_archive_context()
        error = numeric.NumericEvidenceError("Numeric crop geometry differs from its positioned source field",
            diagnostics={"schema": 1, "size_matches": False, "actual_pixel_size": [12, 8], "private": "PRIVATE"})
        with mock.patch.object(probe, "_raw_page_ocr", side_effect=self.raw_fixture), \
             mock.patch.object(probe, "audit_numeric_evidence", side_effect=error):
            result = self.call_pages()
        page = result["pages"][0]
        self.assertEqual(page["category"], "numeric_crop_geometry_mismatch")
        self.assertEqual(page["geometry_diagnostics"]["actual_pixel_size"], [12, 8])
        self.assertNotIn("PRIVATE", json.dumps(result))

    def test_readable_page_reuses_numeric_consumer_and_publishes_only_totals(self):
        self.make_archive_context()
        def numerical(page, primary, **kwargs):
            safe, ocr = self.ocr_fixture(page, "field-probe", 1)
            return {"safe_text": safe, "evidence": ocr["numeric_evidence"]}
        with mock.patch.object(probe, "_raw_page_ocr", side_effect=self.raw_fixture), \
             mock.patch.object(probe, "audit_numeric_evidence", side_effect=numerical):
            result = self.call_pages()
        self.assertTrue(result["success"])
        self.assertEqual(result["pages"][0]["category"], "page_checks_completed")
        self.assertEqual(result["pages"][0]["numeric_counts"]["source_num_count"], 1)
        self.assertEqual(result["pages"][0]["numeric_counts"]["verified_count"], 1)
        for private in ("PRIVATE", '"literal"', "primary_text", "https://", "safe_text"):
            self.assertNotIn(private, json.dumps(result))
        self.assertEqual(result["fixture_acceptance"], "not_requested")

    def test_page_cli_preserves_diagnostic_failures_without_claiming_acceptance(self):
        self.make_archive_context()
        common = ["--input-dir", str(self.originals), "--manifest", str(self.manifest),
                  "--page-checks", str(self.page_checks), "--producer-metadata", str(self.metadata),
                  "--source-run-id", "12345", "--date-folder", "261004", "--expected-articles", "1",
                  "--summary", str(self.summary), "--source-kind", "original-archive", "--repository", "owner/repo"]
        with mock.patch.object(probe, "_raw_page_ocr", side_effect=probe.ProbeError("ocr_engine_failed")), \
             contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(probe.main(common), 3)
        result = json.loads(self.summary.read_text())
        self.assertTrue(result["diagnostic_complete"])
        self.assertFalse(result["success"])
        self.assertEqual(result["pages"][0]["category"], "ocr_engine_failed")
        self.assertFalse(result["production_acceptance"])
        with mock.patch.object(probe, "_raw_page_ocr") as engine, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(probe.main(common + ["--fixtures", str(self.fixtures)]), 2)
            engine.assert_not_called()
        self.assertEqual(json.loads(self.summary.read_text())["category"], "exactly_one_probe_request_required")

    def test_page_probe_rechecks_archive_receipt_and_every_input_after_engine(self):
        self.make_archive_context()
        original = self.archive_receipt.read_bytes()
        def changed(page, image):
            self.archive_receipt.write_bytes(original + b" ")
            return {"category": "page_checks_completed"}
        with mock.patch.object(probe, "_diagnose_page", side_effect=changed), self.assertRaisesRegex(probe.ProbeError, "probe_inputs_changed"):
            self.call_pages()

    def test_page_selector_cannot_bypass_daily_golden_requirement(self):
        self.make_archive_context()
        with self.assertRaisesRegex(probe.ProbeError, "page_diagnostics_require_original_archive"):
            probe.probe_pages(self.originals, self.manifest, self.page_checks, self.metadata,
                date_folder="261004", source_run_id="12345", expected_articles=1, source_kind="daily", repository="owner/repo")

    @unittest.skipUnless(HAS_OCR, "Actual Tesseract CLI and eng+chi_sim models unavailable")
    def test_actual_cloud_archive_page_probe_publishes_counts_only(self):
        self.make_archive_context()
        with mock.patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            result = self.call_pages()
        self.assertTrue(result["diagnostic_complete"])
        self.assertIn("ocr_readability", result["pages"][0])
        self.assertEqual(result["fixture_acceptance"], "not_requested")
        self.assertFalse(result["production_acceptance"])
        self.assertNotIn("PRIVATE", json.dumps(result))

    @unittest.skipUnless(HAS_OCR, "Actual Tesseract CLI and eng+chi_sim models unavailable")
    def test_actual_cloud_ocr_field_probe_without_full_source_or_model_calls(self):
        with mock.patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            result = self.call()
        # This smoke exercises the instrument, not universal numeric accuracy.
        # Real/manual fixtures and numeric-engine tests retain strict acceptance;
        # an uncertain synthetic field must remain an explicit failed fixture.
        self.assert_single_page_probe_contract(result)


class FieldProbeWorkflowTests(unittest.TestCase):
    def test_workflow_only_reads_original_daily_artifact_and_archives_sanitized_json(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / ".github/workflows/market-views-ocr-field-probe.yml").read_text()
        self.assertIn("actions: read", text)
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", text)
        self.assertIn("tesseract-ocr-eng tesseract-ocr-chi-sim", text)
        self.assertIn("eng.traineddata", text)
        self.assertIn("chi_sim.traineddata", text)
        self.assertIn("probe.verify_producer", text)
        self.assertIn("probe.FIXTURE_BYTE_LIMIT", text)
        self.assertIn("FIXTURE_JSON: ${{ inputs.fixture_json }}", text)
        self.assertNotIn("${{ inputs.fixture_json }}", text.split("run: |")[-1])
        self.assertIn("selected-macro-pdfs-${{ inputs.source_run_id }}", text)
        self.assertIn("if: ${{ always() }}", text)
        self.assertIn("path: ${{ runner.temp }}/market-views-ocr-field-probe.json", text)
        for forbidden in ("private_workflow_handoff", "MINERU", "build_market_views", "upload-dir", "workflow run"):
            self.assertNotIn(forbidden, text)
        regression = (root / ".github/workflows/wechat-pipeline-regression.yml").read_text()
        self.assertIn("python scripts/test_probe_market_views_ocr_fields.py", regression)
        self.assertEqual(regression.count('      - ".github/workflows/market-views-ocr-field-probe.yml"'), 2)

    def test_archive_opt_in_reads_only_restores_private_originals_and_never_admits_sources(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / ".github/workflows/market-views-ocr-field-probe.yml").read_text()
        self.assertIn("default: daily", text)
        self.assertIn("if: ${{ inputs.source_kind == 'daily' }}", text)
        self.assertIn("if: ${{ inputs.source_kind == 'original-archive' }}", text)
        self.assertIn("scripts/archive_market_views_originals.py restore", text)
        self.assertIn('--destination "$RUNNER_TEMP/market-views-originals"', text)
        self.assertIn("probe.read_page_checks", text)
        self.assertIn('REQUEST_ARGS=(--page-checks', text)
        self.assertNotIn("archive_market_views_originals.py upload", text)
        self.assertNotIn("put_object", text)
        self.assertNotIn("delete_object", text)
        self.assertEqual(text.count("actions/upload-artifact@v4"), 1)
        self.assertIn("path: ${{ runner.temp }}/market-views-ocr-field-probe.json", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
