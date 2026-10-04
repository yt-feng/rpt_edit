#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
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
