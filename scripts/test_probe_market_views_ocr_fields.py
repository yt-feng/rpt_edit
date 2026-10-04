#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import copy
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
        for forbidden in ("private_workflow_handoff", "R2_ACCESS", "MINERU", "build_market_views", "upload-dir", "workflow run"):
            self.assertNotIn(forbidden, text)
        regression = (root / ".github/workflows/wechat-pipeline-regression.yml").read_text()
        self.assertIn("python scripts/test_probe_market_views_ocr_fields.py", regression)
        self.assertEqual(regression.count('      - ".github/workflows/market-views-ocr-field-probe.yml"'), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
