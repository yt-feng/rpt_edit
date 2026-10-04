#!/usr/bin/env python3
"""Numeric source regressions; CI must also execute the real Tesseract scans."""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock

import fitz
from PIL import Image, ImageDraw

import ocr_numeric_evidence as numeric


REQUIRE_RUNTIME = os.environ.get("REQUIRE_MARKET_VIEWS_OCR_TESTS") == "1"


def sign_evidence(evidence):
    evidence["evidence_sha256"] = numeric._sha(numeric._canonical({k: v for k, v in evidence.items() if k != "evidence_sha256"}))


class NumericUnitTests(unittest.TestCase):
    def test_preserves_decimal_sign_percent_and_grouping(self):
        mentions = numeric.numeric_mentions("Value 4.8 -3.1% (2.7)% 12,580 $1,250.88 +7.5%")
        self.assertEqual([r["normalized"] for r in mentions], ["4.8", "-3.1%", "-2.7%", "12580", "$1250.88", "+7.5%"])

    def test_decimal_comma_is_not_assumed_to_be_thousands(self):
        self.assertEqual(numeric.normalize_number("4,8%"), "4,8%")
        self.assertNotEqual(numeric.normalize_number("4,8%"), numeric.normalize_number("4.8%"))

    def test_negative_unicode_and_parentheses_have_same_value(self):
        self.assertEqual(numeric.normalize_number("− 3.1 %"), numeric.normalize_number("(3.1)%"))

    def test_table_columns_keep_separate_positions(self):
        rows = numeric._word_mentions([(0, 0, 20, 10, "4.8", 0, 0, 0),
                                       (80, 0, 100, 10, "7.5", 0, 0, 1),
                                       (0, 30, 20, 40, "4.8", 0, 1, 0)])
        self.assertEqual([r["literal"] for r in rows], ["4.8", "7.5", "4.8"])
        self.assertEqual(numeric._at_position([0, 0, 20, 10], rows)["bbox"], [0.0, 0.0, 20.0, 10.0])
        self.assertIsNone(numeric._at_position([40, 0, 60, 10], rows))

    def test_split_minus_and_percent_remain_one_field(self):
        rows = numeric._word_mentions([(0, 0, 4, 10, "-", 0, 0, 0),
                                       (7, 0, 27, 10, "3.1", 0, 0, 1),
                                       (30, 0, 38, 10, "%", 0, 0, 2)])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["normalized"], "-3.1%")
        self.assertEqual(rows[0]["bbox"], [0, 0, 38, 10])

    def test_many_to_one_alignment_is_not_guessed(self):
        primary = numeric.numeric_mentions("4.8 7.5")
        positioned = numeric._word_mentions([(0, 0, 50, 10, "4875", 0, 0, 0)])
        self.assertEqual(numeric._align_mentions(primary, positioned), {})

    def test_source_pixel_decimal_is_independent_of_engine_confidence(self):
        image = Image.new("RGB", (90, 55), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle((10, 10, 23, 42), fill="black")
        draw.rectangle((50, 10, 63, 42), fill="black")
        draw.rectangle((34, 39, 37, 42), fill="black")
        witness = numeric.pixel_punctuation(image)
        self.assertEqual(len(witness["decimal_marks"]), 1)
        self.assertEqual(numeric._punctuation_reason("48", witness), "visible_decimal_omitted")
        self.assertIsNone(numeric._punctuation_reason("4.8", witness))

    def test_source_pixel_minus_cannot_be_silently_dropped(self):
        image = Image.new("RGB", (90, 55), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle((30, 10, 43, 42), fill="black")
        draw.rectangle((5, 25, 20, 28), fill="black")
        witness = numeric.pixel_punctuation(image)
        self.assertEqual(len(witness["minus_marks"]), 1)
        self.assertEqual(numeric._punctuation_reason("3", witness), "visible_minus_omitted")
        self.assertIsNone(numeric._punctuation_reason("-3", witness))

    def test_decimal_cannot_be_invented_without_source_mark(self):
        image = Image.new("RGB", (90, 55), "white")
        draw = ImageDraw.Draw(image)
        draw.rectangle((10, 10, 23, 42), fill="black")
        draw.rectangle((50, 10, 63, 42), fill="black")
        self.assertEqual(numeric._punctuation_reason("4.8", numeric.pixel_punctuation(image)), "decimal_not_visible")

    def _rendered_witness(self, value):
        document = fitz.open()
        page = document.new_page(width=250, height=130)
        page.insert_text((40, 55), value, fontsize=18)
        box = list(page.get_text("words")[0][:4])
        image = numeric._image(page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False))
        witness = numeric.pixel_punctuation(image.crop(tuple(numeric._pixel_box(box, image, [250, 130]))))
        document.close()
        return witness

    def test_actual_rendered_percent_cannot_be_omitted(self):
        witness = self._rendered_witness("3.1%")
        self.assertEqual(len(witness["percent_marks"]), 1)
        self.assertEqual(numeric._punctuation_reason("3.1", witness), "visible_percent_omitted")
        self.assertIsNone(numeric._punctuation_reason("3.1%", witness))

    def test_percent_cannot_be_invented(self):
        witness = self._rendered_witness("3.1")
        self.assertEqual(numeric._punctuation_reason("3.1%", witness), "percent_not_visible")

    def test_actual_negative_parentheses_cannot_be_omitted(self):
        witness = self._rendered_witness("(3.1)%")
        self.assertEqual(len(witness["parentheses_marks"]), 1)
        self.assertEqual(numeric._punctuation_reason("3.1%", witness), "visible_negative_parentheses_omitted")
        self.assertIsNone(numeric._punctuation_reason("(3.1)%", witness))

    def test_negative_parentheses_cannot_be_invented(self):
        witness = self._rendered_witness("3.1%")
        self.assertEqual(numeric._punctuation_reason("(3.1)%", witness), "negative_parentheses_not_visible")

    def _audit(self, primary="48", values=None):
        document = fitz.open()
        page = document.new_page(width=250, height=130)
        page.insert_text((40, 55), "4.8", fontsize=18)
        box = list(page.get_text("words")[0][:4])
        word = tuple(box + [primary, 0, 0, 0])
        reads = [{"method": "source-crop-psm-6", "dpi": 600, "literal": (values or ["4.8", "4.8"])[0],
                  "field_count": 1, "input_pixel_sha256": "b" * 64},
                 {"method": "source-crop-psm-11", "dpi": 600, "literal": (values or ["4.8", "4.8"])[1],
                  "field_count": 1, "input_pixel_sha256": "b" * 64}]
        second = [{"bbox": [v * 450 / 72 for v in box], "text": "4.8", "block": 0, "line": 0}]
        with mock.patch.object(numeric, "_read_tesseract", return_value=second), \
             mock.patch.object(numeric, "_crop_reads", return_value={0: reads}):
            result = numeric.audit_numeric_evidence(page, primary, primary_words=[word], language="eng", tesseract_command="unused")
        image = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        document.close()
        return result, image

    def test_actual_rendered_decimal_corrects_48_to_4_8(self):
        result, _ = self._audit()
        self.assertEqual(result["safe_text"], "4.8")
        self.assertEqual(result["evidence"]["corrected_count"], 1)
        self.assertEqual(result["evidence"]["unresolved_count"], 0)

    def test_disagreement_marks_only_the_specific_field(self):
        result, _ = self._audit(primary="4.8", values=["4.8", "48"])
        self.assertEqual(result["safe_text"], "[数值待核对:n0001]")
        self.assertEqual(result["evidence"]["unresolved_count"], 1)
        self.assertEqual(result["evidence"]["primary_text"], "4.8")

    def test_transcript_change_rejected(self):
        result, _ = self._audit()
        with self.assertRaises(numeric.NumericEvidenceError):
            numeric.validate_numeric_evidence("48", result["evidence"], result["evidence"]["input_pixel_sha256"])

    def test_deleted_evidence_field_rejected_even_with_new_digest(self):
        result, _ = self._audit()
        evidence = result["evidence"]
        evidence["records"] = []
        sign_evidence(evidence)
        with self.assertRaises(numeric.NumericEvidenceError):
            numeric.validate_numeric_evidence(result["safe_text"], evidence, evidence["input_pixel_sha256"])

    def test_wrong_page_hash_rejected(self):
        result, _ = self._audit()
        with self.assertRaises(numeric.NumericEvidenceError):
            numeric.validate_numeric_evidence(result["safe_text"], result["evidence"], "d" * 64)

    def test_corrupt_pixels_rejected(self):
        result, image = self._audit()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.png"
            image.save(str(path))
            numeric.validate_numeric_evidence(result["safe_text"], result["evidence"], result["evidence"]["input_pixel_sha256"], image_path=path)
            with Image.open(path) as raw:
                changed = raw.convert("RGB")
            changed.putpixel((1, 1), (0, 0, 0))
            changed.save(path)
            with self.assertRaises(numeric.NumericEvidenceError):
                numeric.validate_numeric_evidence(result["safe_text"], result["evidence"], result["evidence"]["input_pixel_sha256"], image_path=path)

    def test_fabricated_punctuation_rejected_from_real_image(self):
        result, image = self._audit()
        evidence = result["evidence"]
        evidence["records"][0]["pixel_punctuation"]["threshold"] = 200
        sign_evidence(evidence)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.png"
            image.save(str(path))
            with self.assertRaises(numeric.NumericEvidenceError):
                numeric.validate_numeric_evidence(result["safe_text"], evidence, evidence["input_pixel_sha256"], image_path=path)

    def test_read_from_different_column_rejected(self):
        result, _ = self._audit()
        evidence = result["evidence"]
        evidence["records"][0]["reads"][0]["bbox"] = [170, 30, 200, 60]
        sign_evidence(evidence)
        with self.assertRaises(numeric.NumericEvidenceError):
            numeric.validate_numeric_evidence(result["safe_text"], evidence, evidence["input_pixel_sha256"])

    def test_missing_runtime_blocks_numeric_approval(self):
        document = fitz.open()
        page = document.new_page(width=200, height=100)
        with mock.patch.object(numeric.shutil, "which", return_value=None):
            with self.assertRaises(numeric.NumericEvidenceError):
                numeric.audit_numeric_evidence(page, "4.8")
        document.close()

    def test_no_numeric_page_retains_all_text_without_cli(self):
        document = fitz.open()
        page = document.new_page(width=200, height=100)
        result = numeric.audit_numeric_evidence(page, "The company reported stronger demand.")
        self.assertEqual(result["evidence"]["source_num_count"], 0)
        self.assertEqual(result["safe_text"], "The company reported stronger demand.")
        document.close()

    def test_secondary_only_number_is_explicit_and_bound_to_position(self):
        document = fitz.open()
        page = document.new_page(width=250, height=130)
        page.insert_text((40, 55), "4.8", fontsize=18)
        page.insert_text((160, 55), "7.5", fontsize=18)
        words = page.get_text("words")
        second = [{"bbox": [v * 450 / 72 for v in word[:4]], "text": word[4], "block": 0, "line": 0} for word in words]
        reads = [{"method": "source-crop-psm-6", "dpi": 600, "literal": "4.8", "field_count": 1, "input_pixel_sha256": "b" * 64},
                 {"method": "source-crop-psm-11", "dpi": 600, "literal": "4.8", "field_count": 1, "input_pixel_sha256": "b" * 64}]
        with mock.patch.object(numeric, "_read_tesseract", return_value=second), \
             mock.patch.object(numeric, "_crop_reads", return_value={0: reads}):
            result = numeric.audit_numeric_evidence(page, "4.8", primary_words=words[:1], language="eng", tesseract_command="unused")
        self.assertEqual(result["evidence"]["verified_count"], 1)
        self.assertEqual(result["evidence"]["secondary_only_count"], 1)
        self.assertEqual(result["evidence"]["observed_num_count"], 2)
        self.assertIn("[漏识数值待核对:s0001]", result["safe_text"])
        self.assertNotIn("7.5", result["safe_text"])
        evidence = result["evidence"]
        evidence["secondary_only_fields"] = []
        evidence["secondary_only_count"] = 0
        evidence["observed_num_count"] = 1
        sign_evidence(evidence)
        with self.assertRaises(numeric.NumericEvidenceError):
            numeric.validate_numeric_evidence(result["safe_text"], evidence, evidence["input_pixel_sha256"])
        document.close()

    def test_zero_numeric_first_read_still_inspects_original_scan(self):
        document = fitz.open()
        page = document.new_page(width=250, height=130)
        page.insert_text((40, 55), "4.8", fontsize=18)
        word = page.get_text("words")[0]
        second = [{"bbox": [v * 450 / 72 for v in word[:4]], "text": word[4], "block": 0, "line": 0}]
        with mock.patch.object(numeric, "_read_tesseract", return_value=second) as engine, \
             mock.patch.object(numeric, "_crop_reads", return_value={}):
            result = numeric.audit_numeric_evidence(page, "Financial table values were omitted", primary_words=[], language="eng", tesseract_command="unused")
        engine.assert_called_once()
        self.assertEqual(engine.call_args.kwargs["dpi"], 450)
        self.assertEqual(result["evidence"]["source_num_count"], 0)
        self.assertEqual(result["evidence"]["secondary_only_count"], 1)
        self.assertEqual(result["evidence"]["observed_num_count"], 1)
        self.assertIn("[漏识数值待核对:s0001]", result["safe_text"])
        document.close()


def financial_scan():
    """An actual raster-only PDF with known table cells, without private data."""
    vector = fitz.open()
    page = vector.new_page(width=440, height=250)
    page.insert_text((20, 26), "Financial table: exact original source values", fontsize=12)
    columns = [20, 145, 250, 350]
    rows = [("Company", "Growth", "EPS", "PE"),
            ("Alpha", "-3.1%", "1,250.88", "4.8"),
            ("Beta", "(2.7)%", "1,687.17", "7.5"),
            ("Gamma", "+9.8%", "2,635.81", "25.9"),
            ("Delta", "12.6%", "12,580", "33.0")]
    expected = []
    for row_index, row in enumerate(rows):
        y = 56 + row_index * 27
        for column_index, value in enumerate(row):
            page.insert_text((columns[column_index], y), value, fontsize=10)
            if column_index and row_index:
                expected.append({"literal": value, "row": row_index, "column": column_index,
                                 "position": [columns[column_index], y]})
    png = page.get_pixmap(dpi=200, colorspace=fitz.csRGB, alpha=False).tobytes("png")
    scan = fitz.open()
    scanned_page = scan.new_page(width=440, height=250)
    scanned_page.insert_image(scanned_page.rect, stream=png)
    vector.close()
    return scan, expected


class NumericRealScanTests(unittest.TestCase):
    def setUp(self):
        if not shutil.which("tesseract"):
            if REQUIRE_RUNTIME:
                self.fail("Cloud numeric acceptance requires the real Tesseract CLI")
            self.skipTest("Local Tesseract CLI unavailable; cloud sets REQUIRE_MARKET_VIEWS_OCR_TESTS=1")
        try:
            self.tessdata = fitz.get_tessdata()
            if not (Path(self.tessdata) / "eng.traineddata").is_file():
                raise ValueError("eng model missing")
        except Exception as exc:
            if REQUIRE_RUNTIME:
                self.fail(f"Cloud numeric acceptance requires the real trained model: {type(exc).__name__}")
            self.skipTest("Local trained model unavailable; mandatory in cloud")

    def _first_read(self, page):
        textpage = page.get_textpage_ocr(language="eng", dpi=300, full=True, tessdata=self.tessdata)
        return page.get_text("text", textpage=textpage, sort=True).strip(), page.get_text("words", textpage=textpage, sort=True)

    def test_scanned_financial_table_preserves_values_and_positions(self):
        document, expected = financial_scan()
        page = document[0]
        self.assertEqual(page.get_text("text"), "")
        text, words = self._first_read(page)
        result = numeric.audit_numeric_evidence(page, text, primary_words=words, language="eng", tessdata=self.tessdata)
        records = result["evidence"]["records"]
        admitted = [record for record in records if record["status"] != "unresolved"]
        expected_values = {numeric.normalize_number(row["literal"]) for row in expected}
        self.assertTrue(all(numeric.normalize_number(record["safe_literal"]) in expected_values for record in admitted))
        self.assertGreaterEqual(len(admitted), 10, "The backup must retain meaningful numeric table coverage")
        self.assertIn("4.8", result["safe_text"])
        self.assertIn("-3.1%", [numeric.normalize_number(record["safe_literal"]) for record in admitted])
        for original in expected:
            matched = [record for record in admitted if numeric.normalize_number(record["safe_literal"]) == numeric.normalize_number(original["literal"])]
            if matched:
                self.assertEqual(len(matched), 1)
                box = matched[0]["bbox"]
                self.assertLess(abs(box[0] - original["position"][0]), 6)
                self.assertLess(abs(box[3] - original["position"][1]), 6)
        document.close()

    def test_real_scanned_pixels_correct_injected_decimal_omission(self):
        document, _ = financial_scan()
        page = document[0]
        text, words = self._first_read(page)
        self.assertIn("4.8", text)
        corrupted = text.replace("4.8", "48", 1)
        corrupted_words = [tuple(list(word[:4]) + [word[4].replace("4.8", "48", 1)] + list(word[5:])) if word[4] == "4.8" else word for word in words]
        result = numeric.audit_numeric_evidence(page, corrupted, primary_words=corrupted_words, language="eng", tessdata=self.tessdata)
        corrected = [record for record in result["evidence"]["records"] if record["status"] == "corrected"]
        self.assertTrue(any(record["literal"] == "48" and record["safe_literal"] == "4.8" for record in corrected))
        self.assertIn("4.8", result["safe_text"])
        document.close()

    def test_zero_numeric_transcript_cannot_hide_a_real_scanned_table(self):
        document, expected = financial_scan()
        page = document[0]
        result = numeric.audit_numeric_evidence(page, "Financial table values omitted in the first read", primary_words=[], language="eng", tessdata=self.tessdata)
        self.assertEqual(result["evidence"]["source_num_count"], 0)
        self.assertGreaterEqual(result["evidence"]["secondary_only_count"], 10)
        self.assertEqual(result["evidence"]["observed_num_count"], result["evidence"]["secondary_only_count"])
        self.assertTrue(any(numeric.normalize_number(field["literal"]) == "4.8" for field in result["evidence"]["secondary_only_fields"]))
        self.assertIn("[漏识数值待核对:s0001]", result["safe_text"])
        document.close()


if __name__ == "__main__":
    unittest.main()
