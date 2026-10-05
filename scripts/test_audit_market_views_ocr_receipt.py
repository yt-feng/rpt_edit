#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import fitz

import audit_market_views_ocr_receipt as audit
from extract_native_market_sources import extract_sources


SOURCE_SHA = "a" * 64


def numeric_page():
    records = [{"safe_literal": "4.8", "status": "corrected", "bbox": [530, 103, 541, 110]},
               {"safe_literal": "(3.1)%", "status": "verified", "bbox": [300, 115, 320, 121]},
               {"safe_literal": "[数值待核对:n0003]", "status": "unresolved", "bbox": [350, 103, 375, 110]}]
    return {"page": 1, "extraction_method": "ocr", "ocr": {"numeric_evidence": {
        "source_num_count": 3, "verified_count": 1, "corrected_count": 1, "unresolved_count": 1,
        "secondary_only_count": 2, "observed_num_count": 5, "records": records,
        "evidence_sha256": "b" * 64, "input_pixel_sha256": "c" * 64,
        "primary_text": "PRIVATE FULL REPORT https://private.invalid signed credentials"}}}


def receipt():
    return {"schema": 2, "complete": True, "manifest_sha256": "d" * 64,
            "report_count": 1, "reports": [{"content_sha256": SOURCE_SHA, "source_pdf": "PRIVATE-TITLE.pdf",
                                           "page_count": 1, "pages": [numeric_page()]}]}


def fixture(literal="4.8", box=None):
    return {"id": "first_row_pe", "source_pdf_sha256": SOURCE_SHA, "page": 1,
            "expected_literal": literal, "expected_bbox": box or [529, 102, 543, 114]}


def unresolved_percent_receipt():
    value = receipt()
    evidence = value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]
    box = [140, 246, 164, 258]
    evidence.update({
        "source_dpi": 300, "source_num_count": 1, "verified_count": 0, "corrected_count": 0,
        "unresolved_count": 1, "secondary_only_count": 0, "observed_num_count": 1,
        "second_page_fields": [{"literal": "17%", "bbox": box},
                               {"literal": "PRIVATE PROSE https://private.invalid", "bbox": [10, 10, 20, 20]}],
        "records": [{"id": "n0001", "literal": "17%", "safe_literal": "[数值待核对:n0001]",
                     "status": "unresolved", "reason": "percent_not_visible", "bbox": box,
                     "source_pixel_bbox": [550, 1000, 720, 1100],
                     "reads": [{"method": "second-page-psm-3", "dpi": 450, "literal": "17%", "bbox": box,
                                "input_pixel_sha256": "f" * 64},
                               {"method": "source-crop-psm-6", "dpi": 600, "literal": "17%", "field_count": 1},
                               {"method": "source-crop-psm-11", "dpi": 600, "literal": "17%", "field_count": 1}],
                     "pixel_punctuation": {"width": 170, "height": 100, "threshold": 160,
                                           "pixel_sha256": "f" * 64, "components": [{"bbox": [1, 2, 3, 4], "area": 4}],
                                           "decimal_marks": [], "minus_marks": [], "percent_marks": [],
                                           "parentheses_marks": []}}]})
    return value


class NumericAuditTests(unittest.TestCase):
    def summarize(self, value=None, checks=None):
        return audit.summarize_verified_receipt(value or receipt(), "e" * 64, checks or [])

    def test_sanitized_counts_and_private_fields_do_not_escape(self):
        result = self.summarize(checks=[fixture()])
        raw = json.dumps(result)
        self.assertNotIn("PRIVATE", raw)
        self.assertNotIn("private.invalid", raw)
        self.assertNotIn("credentials", raw)
        self.assertNotIn("source_pdf\"", raw)
        self.assertEqual(result["numeric_totals"]["unconfirmed_num_count"], 3)
        self.assertEqual(result["numeric_totals"]["observed_num_count"], 5)
        self.assertEqual(result["fixture_passed_count"], 1)
        self.assertEqual(result["pages"][0]["page"], 1)

    def test_fixture_requires_value_and_position(self):
        good = self.summarize(checks=[fixture()])
        wrong_value = self.summarize(checks=[fixture("48")])
        wrong_position = self.summarize(checks=[fixture(box=[10, 10, 20, 20])])
        self.assertTrue(good["success"])
        self.assertFalse(wrong_value["success"])
        self.assertEqual(wrong_value["fixtures"][0]["category"], "value_mismatch")
        self.assertEqual(wrong_position["fixtures"][0]["category"], "position_missing")

    def test_fixture_preserves_negative_parentheses_and_percent(self):
        result = self.summarize(checks=[fixture("-3.1%", [298, 114, 322, 127])])
        self.assertTrue(result["success"])
        positive = self.summarize(checks=[fixture("3.1%", [298, 114, 322, 127])])
        missing_percent = self.summarize(checks=[fixture("-3.1", [298, 114, 322, 127])])
        self.assertFalse(positive["success"])
        self.assertFalse(missing_percent["success"])

    def test_unresolved_field_never_passes_fixture(self):
        result = self.summarize(checks=[fixture("1250.88", [349, 102, 376, 114])])
        self.assertEqual(result["fixtures"][0]["category"], "field_unresolved")
        self.assertFalse(result["success"])

    def test_failed_percent_fixture_reports_numeric_evidence_without_admitting_it(self):
        result = self.summarize(unresolved_percent_receipt(), [fixture("17%", [139, 245, 165, 259])])
        check = result["fixtures"][0]
        self.assertFalse(result["success"])
        self.assertEqual(check["category"], "field_unresolved")
        diagnostic = check["numeric_diagnostics"]
        self.assertEqual(diagnostic["source_dpi"], 300)
        self.assertEqual(diagnostic["positional_record_count"], 1)
        row = diagnostic["records"][0]
        self.assertEqual(row["primary_literal"], "17%")
        self.assertEqual(row["reason"], "percent_not_visible")
        self.assertNotIn("admitted_literal", row)
        self.assertEqual([read["literal"] for read in row["reads"]], ["17%"] * 3)
        self.assertEqual(row["pixel_punctuation"]["percent_marks"], {"present": False, "count": 0})
        self.assertEqual(row["pixel_punctuation"]["component_count"], 1)
        self.assertEqual(row["source_pixel_bbox"], [550, 1000, 720, 1100])
        self.assertEqual(row["second_page_at_record"]["candidate_count"], 1)
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertNotIn("数值待核对", json.dumps(result))

    def test_positioned_read_conflict_reports_null_and_multiple_candidates(self):
        value = unresolved_percent_receipt()
        evidence = value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]
        row = evidence["records"][0]
        row["reason"] = "positioned_reads_disagree"
        row["reads"][0]["literal"] = None
        row["reads"][1].update({"literal": None, "field_count": 2})
        evidence["second_page_fields"].append({"literal": "7%", "bbox": [142, 246, 164, 258]})
        result = self.summarize(value, [fixture("17%", [139, 245, 165, 259])])
        diagnostic = result["fixtures"][0]["numeric_diagnostics"]["records"][0]
        self.assertEqual(diagnostic["reason"], "positioned_reads_disagree")
        self.assertIsNone(diagnostic["reads"][0]["literal"])
        self.assertEqual(diagnostic["reads"][1]["field_count"], 2)
        self.assertEqual(diagnostic["second_page_at_record"]["candidate_count"], 2)
        self.assertEqual([row["literal"] for row in diagnostic["second_page_at_record"]["candidates"]], ["17%", "7%"])
        self.assertFalse(result["success"])

    def test_new_crop_geometry_is_sanitized_without_changing_unresolved_acceptance(self):
        value = unresolved_percent_receipt()
        row = value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]["records"][0]
        metadata = {"crop_policy": audit.OCR_CROP_POLICY,
                    "source_clip_bbox": [140.4, 249.4, 160.7, 260.0], "crop_pixel_size": [170, 89]}
        for read in row["reads"][1:]:
            read.update(copy.deepcopy(metadata))
        before = copy.deepcopy(value)
        result = self.summarize(value, [fixture("17%", [139, 245, 165, 259])])
        diagnostic = result["fixtures"][0]["numeric_diagnostics"]["records"][0]
        self.assertFalse(result["success"])
        self.assertEqual(result["fixtures"][0]["category"], "field_unresolved")
        self.assertNotIn("crop_policy", diagnostic["reads"][0])
        for read in diagnostic["reads"][1:]:
            for key, expected in metadata.items():
                self.assertEqual(read[key], expected)
        self.assertEqual(value, before)
        self.assertNotIn("PRIVATE", json.dumps(result))

    def test_crop_diagnostic_metadata_is_all_or_nothing_and_rejects_unbounded_or_private_values(self):
        base = {"method": "source-crop-psm-6", "dpi": 600, "literal": "17%", "field_count": 1,
                "crop_policy": audit.OCR_CROP_POLICY, "source_clip_bbox": [140, 249, 161, 260],
                "crop_pixel_size": [175, 93]}
        cases = [{"crop_policy": "PRIVATE https://private.invalid"}, {"crop_policy": []},
                 {"source_clip_bbox": [0, 0, float("nan"), 10]}, {"source_clip_bbox": [0, 0, 100001, 10]},
                 {"source_clip_bbox": None}, {"crop_pixel_size": [True, 90]}, {"crop_pixel_size": [0, 90]},
                 {"crop_pixel_size": [-1, 90]}, {"crop_pixel_size": [100000, 100000]},
                 {"crop_pixel_size": ["PRIVATE", 90]}, {"crop_pixel_size": None},
                 {"method": "second-page-psm-3"}]
        for mutation in cases:
            read = copy.deepcopy(base)
            read.update(mutation)
            projected = audit._diagnostic_read(read)
            with self.subTest(mutation=mutation):
                for key in ("crop_policy", "source_clip_bbox", "crop_pixel_size"):
                    self.assertNotIn(key, projected)
                self.assertNotIn("PRIVATE", json.dumps(projected, allow_nan=False))

    def test_second_page_lookup_uses_record_position_independently_of_fixture_box(self):
        value = unresolved_percent_receipt()
        evidence = value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]
        evidence["second_page_fields"].append({"literal": "25", "bbox": [166, 246, 175, 258]})
        result = self.summarize(value, [fixture("17%", [139, 245, 180, 259])])
        diagnostic = result["fixtures"][0]["numeric_diagnostics"]
        self.assertEqual(diagnostic["second_page_at_fixture"]["candidate_count"], 2)
        self.assertEqual(diagnostic["records"][0]["second_page_at_record"]["candidate_count"], 1)

    def test_successful_fixture_has_no_failure_diagnostics(self):
        result = self.summarize(checks=[fixture()])
        self.assertNotIn("numeric_diagnostics", result["fixtures"][0])

    def test_mismatch_reports_only_already_admitted_numeric_literal(self):
        result = self.summarize(checks=[fixture("48")])
        row = result["fixtures"][0]["numeric_diagnostics"]["records"][0]
        self.assertEqual(row["status"], "corrected")
        self.assertEqual(row["admitted_literal"], "4.8")
        self.assertFalse(result["success"])

    def test_diagnostic_projection_discards_prose_urls_unknown_fields_and_invalid_scalars(self):
        value = unresolved_percent_receipt()
        evidence = value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]
        private = "PRIVATE REPORT https://private.invalid signed credentials"
        evidence["runtime"] = {"language": private}
        row = evidence["records"][0]
        row.update({"id": private, "reason": private, "literal": private, "safe_literal": private,
                    "source_pixel_bbox": [0, 0, float("inf"), 10], "unknown": private})
        row["reads"] = [{"method": "second-page-psm-3", "dpi": True, "literal": private,
                         "bbox": [0, 0, float("nan"), 10], "field_count": -1,
                         "input_pixel_sha256": private, "raw_text": private},
                        {"method": {"private": private}, "literal": "17%"},
                        {"method": private, "literal": "17%"}]
        row["pixel_punctuation"].update({"width": True, "height": -1, "threshold": 1000,
                                         "pixel_sha256": private, "percent_marks": [[private]],
                                         "components": [{"raw_text": private}], "unknown": private})
        evidence["second_page_fields"] = [{"literal": private, "bbox": row["bbox"], "raw_text": private},
                                           {"literal": "17%", "bbox": [0, 0, 10 ** 400, 10]}]
        result = self.summarize(value, [fixture("17%", [139, 245, 165, 259])])
        diagnostic = result["fixtures"][0]["numeric_diagnostics"]["records"][0]
        for key in ("id", "reason", "source_pixel_bbox", "admitted_literal"):
            self.assertNotIn(key, diagnostic)
        self.assertIsNone(diagnostic["primary_literal"])
        self.assertEqual(diagnostic["reads"], [{"method": "second-page-psm-3", "literal": None}])
        self.assertNotIn("percent_marks", diagnostic["pixel_punctuation"])
        self.assertNotIn("PRIVATE", json.dumps(result, allow_nan=False))
        self.assertNotIn("credentials", json.dumps(result))
        self.assertFalse(result["success"])

    def test_numeric_diagnostic_literals_have_strict_bounded_grammar(self):
        for literal in ("17%", "(3.1)%", "-4.8", "−4.8", "$ 1,250.88", "25 bps", "12x"):
            self.assertEqual(audit._diagnostic_number(literal), literal)
        for literal in (None, 17, "17% PRIVATE", "https://private.invalid", "[数值待核对:n0001]",
                        "1" * 65, "17\n%", "17\t%", "17\x00%"):
            self.assertIsNone(audit._diagnostic_number(literal))

    def test_unhashable_read_methods_are_discarded_without_an_exception(self):
        for method in ([], ["second-page-psm-3"], {}, {"private": "PRIVATE REPORT"}):
            self.assertIsNone(audit._diagnostic_read({"method": method, "literal": "17%", "dpi": 450}))

    def test_failure_diagnostics_leave_the_private_receipt_unchanged(self):
        value = unresolved_percent_receipt()
        before = json.dumps(value, sort_keys=True)
        self.summarize(value, [fixture("17%", [139, 245, 165, 259])])
        self.assertEqual(json.dumps(value, sort_keys=True), before)

    def test_secondary_page_candidate_never_promotes_a_missing_primary_position(self):
        result = self.summarize(unresolved_percent_receipt(), [fixture("17%", [10, 10, 20, 20])])
        row = result["fixtures"][0]
        self.assertEqual(row["category"], "position_missing")
        self.assertEqual(row["numeric_diagnostics"]["positional_record_count"], 0)
        self.assertEqual(row["numeric_diagnostics"]["second_page_at_fixture"]["candidate_count"], 1)
        self.assertIsNone(row["numeric_diagnostics"]["second_page_at_fixture"]["candidates"][0]["literal"])
        self.assertFalse(result["success"])

    def test_failed_fixture_cli_writes_diagnostics_but_logs_counts_only_and_keeps_exit_three(self):
        summary = self.summarize(unresolved_percent_receipt(), [fixture("17%", [139, 245, 165, 259])])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "sources"
            source.mkdir()
            destination = root / "summary.json"
            stdout = io.StringIO()
            with mock.patch.object(sys, "argv", ["audit", "--source-dir", str(source), "--expected-reports", "1",
                                                "--summary", str(destination)]), \
                    mock.patch.object(audit, "audit_sources", return_value=summary) as audited, \
                    mock.patch.object(sys, "stdout", stdout):
                code = audit.main()
            self.assertEqual(code, 3)
            audited.assert_called_once()
            stored = json.loads(destination.read_text())
            self.assertEqual(stored["fixtures"][0]["numeric_diagnostics"]["records"][0]["reason"], "percent_not_visible")
            self.assertNotIn("percent_not_visible", stdout.getvalue())
            self.assertNotIn("17%", stdout.getvalue())
            self.assertNotIn("PRIVATE", destination.read_text())
            self.assertEqual(list(source.iterdir()), [])

    def test_diagnostics_are_bounded_and_explicitly_mark_truncation(self):
        value = unresolved_percent_receipt()
        evidence = value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]
        row = evidence["records"][0]
        row["reads"] *= 4
        row["pixel_punctuation"]["percent_marks"] = [[1, 2, 3, 4]] * (audit.DIAGNOSTIC_MARK_LIMIT + 1)
        evidence["records"] = [copy.deepcopy(row) for _ in range(audit.DIAGNOSTIC_RECORD_LIMIT + 1)]
        evidence.update({"source_num_count": len(evidence["records"]), "unresolved_count": len(evidence["records"]),
                         "observed_num_count": len(evidence["records"])})
        evidence["second_page_fields"] = [{"literal": "17%", "bbox": row["bbox"]}] * (audit.DIAGNOSTIC_SCAN_LIMIT + 1)
        result = self.summarize(value, [fixture("17%", [139, 245, 165, 259])])
        diagnostic = result["fixtures"][0]["numeric_diagnostics"]
        self.assertEqual(len(diagnostic["records"]), audit.DIAGNOSTIC_RECORD_LIMIT)
        self.assertTrue(diagnostic["records_truncated"])
        self.assertTrue(diagnostic["records"][0]["reads_truncated"])
        self.assertEqual(len(diagnostic["records"][0]["reads"]), audit.DIAGNOSTIC_READ_LIMIT)
        self.assertNotIn("percent_marks", diagnostic["records"][0]["pixel_punctuation"])
        self.assertTrue(diagnostic["second_page_at_fixture"]["scan_truncated"])
        self.assertTrue(diagnostic["second_page_at_fixture"]["candidates_truncated"])
        self.assertEqual(len(diagnostic["second_page_at_fixture"]["candidates"]), audit.DIAGNOSTIC_RECORD_LIMIT)
        self.assertLessEqual(len(json.dumps(diagnostic, ensure_ascii=False).encode()), audit.DIAGNOSTIC_BYTE_LIMIT)
        self.assertFalse(result["success"])

    def test_source_hash_must_match(self):
        check = fixture()
        check["source_pdf_sha256"] = "f" * 64
        self.assertEqual(self.summarize(checks=[check])["fixtures"][0]["category"], "source_missing")

    def test_missing_page_never_passes(self):
        check = fixture()
        check["page"] = 2
        self.assertEqual(self.summarize(checks=[check])["fixtures"][0]["category"], "page_missing")

    def test_duplicate_alias_retains_coverage_without_multiplying_fixture(self):
        value = receipt()
        value["reports"].append(copy.deepcopy(value["reports"][0]))
        value["report_count"] = 2
        result = self.summarize(value, [fixture()])
        self.assertTrue(result["success"])
        self.assertEqual(result["page_count"], 2)
        self.assertEqual(result["unique_content_count"], 1)
        self.assertEqual(result["numeric_totals"]["observed_num_count"], 10)
        self.assertEqual(result["unique_content_numeric_totals"]["observed_num_count"], 5)
        self.assertTrue(result["pages"][1]["duplicate_content"])

    def test_ambiguous_same_value_position_is_rejected(self):
        value = receipt()
        value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]["records"].append(
            {"safe_literal": "4.8", "status": "verified", "bbox": [530, 103, 541, 110]})
        result = self.summarize(value, [fixture()])
        self.assertEqual(result["fixtures"][0]["category"], "ambiguous_match")
        self.assertFalse(result["success"])

    def test_invalid_numeric_totals_rejected(self):
        value = receipt()
        value["reports"][0]["pages"][0]["ocr"]["numeric_evidence"]["verified_count"] = 9
        with self.assertRaises(audit.AuditError):
            self.summarize(value)

    def test_native_pages_have_zero_ocr_numeric_counts(self):
        value = receipt()
        value["reports"][0]["pages"] = [{"page": 1, "extraction_method": "native", "native_text": "PRIVATE SOURCE 4.8"}]
        result = self.summarize(value)
        self.assertEqual(result["page_methods"]["native"], 1)
        self.assertEqual(result["numeric_totals"]["observed_num_count"], 0)
        self.assertNotIn("PRIVATE SOURCE", json.dumps(result))

    def test_invalid_fixture_payload_and_prose_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixtures.json"
            for check in [dict(fixture(), expected_literal="PRIVATE REPORT"), dict(fixture(), url="https://private.invalid"),
                          dict(fixture(), id="PRIVATE-TITLE.pdf"), dict(fixture(), expected_bbox=[0, 1, 0, 2]),
                          dict(fixture(), page=True), dict(fixture(), min_overlap=float("nan"))]:
                path.write_text(json.dumps({"schema": 1, "checks": [check]}))
                with self.assertRaises(audit.AuditError):
                    audit.read_fixtures(path)

    def test_duplicate_fixture_identifiers_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixtures.json"
            path.write_text(json.dumps({"schema": 1, "checks": [fixture(), fixture()]}))
            with self.assertRaises(audit.AuditError):
                audit.read_fixtures(path)

    def test_valid_fixture_is_read_without_source_content(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixtures.json"
            path.write_text(json.dumps({"schema": 1, "checks": [fixture()]}))
            self.assertEqual(audit.read_fixtures(path), [fixture()])

    def test_summary_cannot_modify_verified_source_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "sources"
            source.mkdir()
            with self.assertRaises(audit.AuditError):
                audit.write_summary(source / "public-summary.json", self.summarize(), source_dir=source)

    def test_summary_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "sources"
            source.mkdir()
            destination = root / "target"
            destination.write_text("preserve")
            link = root / "summary"
            link.symlink_to(destination)
            with self.assertRaises(audit.AuditError):
                audit.write_summary(link, self.summarize(), source_dir=source)
            self.assertEqual(destination.read_text(), "preserve")


class FullSourceAuditTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        originals = self.root / "originals"
        originals.mkdir()
        pdf = originals / "PRIVATE-TITLE.pdf"
        document = fitz.open()
        page = document.new_page(width=600, height=800)
        for index in range(18):
            page.insert_text((30, 45 + index * 28), "The company reported stronger demand, improved margins and steady investment.", fontsize=10)
        document.save(pdf)
        document.close()
        self.manifest = self.root / "manifest.json"
        self.manifest.write_text(json.dumps([{"process_local_path": str(pdf), "content_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()}]))
        self.sources = self.root / "sources"
        extract_sources(originals, self.manifest, self.sources, 1)

    def test_real_native_source_contract_validated_and_sanitized(self):
        result = audit.audit_sources(self.sources, 1)
        self.assertTrue(result["source_contract_verified"])
        self.assertEqual(result["report_count"], 1)
        self.assertEqual(result["page_count"], 1)
        self.assertEqual(result["page_methods"], {"native": 1, "ocr": 0, "blank": 0})
        self.assertNotIn("PRIVATE-TITLE", json.dumps(result))

    def test_receipt_audit_does_not_use_fixture_json_size_limit_or_extra_json_parse(self):
        receipt_path = self.sources / audit.RECEIPT_NAME
        expected = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
        # Real native validation still runs. The removed receipt-only size gate
        # and discarded full JSON copy must never be used by this path.
        with mock.patch.object(audit, "_read_json", side_effect=AssertionError("receipt parsed twice")):
            result = audit.audit_sources(self.sources, 1)
        self.assertEqual(result["receipt_sha256"], expected)

    def test_streamed_receipt_identity_hashes_a_real_file_above_legacy_limit(self):
        path = self.root / "large-receipt.json"
        block = b"x" * (1024 * 1024)
        with path.open("wb") as stream:
            for _ in range(245):
                stream.write(block)
        self.assertGreater(path.stat().st_size, 256_000_000)
        # Hashing a genuinely over-limit regular file does not parse or retain
        # source bytes. Full schema validation is independently exercised above.
        digest = hashlib.sha256()
        for _ in range(245):
            digest.update(block)
        identity = audit.receipt_identity(path)
        self.assertEqual(identity, {"sha256": digest.hexdigest(), "bytes": 245 * len(block)})

    def test_receipt_changed_during_full_validation_is_rejected(self):
        original = audit.validate_sources
        def validate_then_mutate(*args, **kwargs):
            receipt = original(*args, **kwargs)
            with (self.sources / audit.RECEIPT_NAME).open("ab") as output:
                output.write(b"\n")
            return receipt
        with mock.patch.object(audit, "validate_sources", side_effect=validate_then_mutate):
            with self.assertRaisesRegex(audit.AuditError, "receipt_changed_during_audit"):
                audit.audit_sources(self.sources, 1)

    def test_receipt_symlink_and_directory_rejected(self):
        link = self.root / "receipt-link"
        link.symlink_to(self.sources / audit.RECEIPT_NAME)
        for path in (link, self.sources):
            with self.subTest(path=path.name), self.assertRaisesRegex(audit.AuditError, "invalid_receipt_file"):
                audit.receipt_identity(path)

    def test_tampered_source_file_is_rejected_before_summary(self):
        raw = self.sources / next(self.sources.glob("report_*" )).name / "source_native_pdf.md"
        raw.write_text(raw.read_text() + "\nTampering")
        with self.assertRaises(ValueError):
            audit.audit_sources(self.sources, 1)

    def test_cli_writes_only_sanitized_summary(self):
        destination = self.root / "summary.json"
        result = subprocess.run([sys.executable, str(Path(audit.__file__)), "--source-dir", str(self.sources),
                                 "--expected-reports", "1", "--summary", str(destination)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("PRIVATE-TITLE", result.stdout)
        self.assertNotIn("PRIVATE-TITLE", destination.read_text())
        self.assertTrue(json.loads(destination.read_text())["source_contract_verified"])

    def test_cli_contract_failure_does_not_expose_private_filename(self):
        destination = self.root / "summary.json"
        result = subprocess.run([sys.executable, str(Path(audit.__file__)), "--source-dir", str(self.sources),
                                 "--expected-reports", "2", "--summary", str(destination)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("PRIVATE-TITLE", result.stderr)
        self.assertFalse(destination.exists())

    def test_cli_failed_fixture_writes_evidence_and_exits_nonzero(self):
        destination = self.root / "summary.json"
        fixtures = self.root / "fixtures.json"
        fixtures.write_text(json.dumps({"schema": 1, "checks": [fixture()]}))
        result = subprocess.run([sys.executable, str(Path(audit.__file__)), "--source-dir", str(self.sources),
                                 "--expected-reports", "1", "--summary", str(destination), "--fixtures", str(fixtures)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 3)
        summary = json.loads(destination.read_text())
        self.assertTrue(summary["source_contract_verified"])
        self.assertFalse(summary["success"])
        self.assertEqual(summary["fixture_passed_count"], 0)


if __name__ == "__main__":
    unittest.main()
