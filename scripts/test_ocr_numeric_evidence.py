#!/usr/bin/env python3
"""Numeric source regressions; CI must also execute the real Tesseract scans."""
from __future__ import annotations

import copy
import base64
import binascii
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
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

    def _parse_real_tsv_shape(self, rows):
        header = "level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext\n"
        output = (header + "".join("\t".join(str(value) for value in row) + "\n" for row in rows)).encode()
        with mock.patch.object(numeric.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, output, b"")):
            return numeric._read_tesseract(Image.new("RGB", (140, 110), "white"),
                                           language="eng", tessdata=None, command="unused", psm=3, dpi=300)

    def test_tsv_paragraphs_with_same_line_number_never_merge(self):
        words = self._parse_real_tsv_shape([
            [5, 1, 1, 1, 1, 1, 10, 10, 5, 10, 90, "-"],
            [5, 1, 1, 1, 1, 2, 18, 10, 20, 10, 90, "3.1"],
            [5, 1, 1, 2, 1, 1, 14, 60, 20, 10, 90, "8.4"],
        ])
        self.assertEqual([word["paragraph"] for word in words], [1, 1, 2])
        mentions = numeric._word_mentions(words)
        self.assertEqual([row["normalized"] for row in mentions], ["-3.1", "8.4"])
        self.assertEqual([row["bbox"] for row in mentions], [[10, 10, 38, 20], [14, 60, 34, 70]])

    def test_tsv_negative_percent_and_adjacent_columns_keep_rows(self):
        words = self._parse_real_tsv_shape([
            [5, 1, 1, 1, 1, 1, 10, 10, 5, 10, 90, "-"],
            [5, 1, 1, 1, 1, 2, 18, 10, 20, 10, 90, "3.1"],
            [5, 1, 1, 1, 1, 3, 41, 10, 8, 10, 90, "%"],
            [5, 1, 1, 1, 1, 4, 80, 10, 20, 10, 90, "8.4"],
            [5, 1, 1, 2, 1, 1, 10, 60, 5, 10, 90, "-"],
            [5, 1, 1, 2, 1, 2, 18, 60, 20, 10, 90, "2.7"],
            [5, 1, 1, 2, 1, 3, 41, 60, 8, 10, 90, "%"],
            [5, 1, 1, 2, 1, 4, 80, 60, 20, 10, 90, "4.8"],
        ])
        mentions = numeric._word_mentions(words)
        self.assertEqual([row["normalized"] for row in mentions], ["-3.1%", "8.4", "-2.7%", "4.8"])
        self.assertEqual([row["bbox"] for row in mentions], [[10, 10, 49, 20], [80, 10, 100, 20],
                                                             [10, 60, 49, 70], [80, 60, 100, 70]])

    def test_many_to_one_alignment_is_not_guessed(self):
        primary = numeric.numeric_mentions("4.8 7.5")
        positioned = numeric._word_mentions([(0, 0, 50, 10, "4875", 0, 0, 0)])
        self.assertEqual(numeric._align_mentions(primary, positioned), {})

    def test_tight_crop_keeps_field_pixels_and_excludes_adjacent_prose_ink(self):
        with fitz.open() as document:
            page = document.new_page(width=250, height=130)
            box = [100.0, 60.0, 120.0, 70.0]
            for ink in ([100, 60, 112, 70], [95, 60, 98, 70], [100, 55, 120, 57]):
                page.draw_rect(fitz.Rect(ink), color=None, fill=(0, 0, 0))
            clip = numeric._ocr_crop_clip(box, [250.0, 130.0])
            tight = numeric._image(page.get_pixmap(dpi=600, clip=fitz.Rect(clip), colorspace=fitz.csRGB, alpha=False))
            pad = numeric._field_padding(box)
            wide = numeric._image(page.get_pixmap(dpi=600, clip=fitz.Rect(box) + (-pad, -pad, pad, pad),
                                                  colorspace=fitz.csRGB, alpha=False))
            self.assertEqual(len(numeric.pixel_punctuation(tight)["components"]), 1)
            self.assertEqual(len(numeric.pixel_punctuation(wide)["components"]), 3)
            self.assertEqual(list(tight.size), numeric._ocr_crop_pixel_size(clip))
            self.assertGreater(clip[0], 98)
            self.assertGreater(clip[1], 57)
            self.assertLessEqual(clip[0], box[0])
            self.assertGreaterEqual(clip[2], box[2])
            # This is the existing consumer witness, not the OCR crop policy.
            source = numeric._image(page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False))
            self.assertEqual(numeric._pixel_box(box, source, [250, 130]), [389, 223, 528, 319])

    def test_tight_crop_clips_at_page_edges_and_rejects_invalid_geometry(self):
        clip = numeric._ocr_crop_clip([0, 0, 2, 3], [10, 10])
        self.assertEqual(clip[:2], [0, 0])
        clip = numeric._ocr_crop_clip([8, 8, 10, 10], [10, 10])
        self.assertEqual(clip[2:], [10, 10])
        for box in ([2, 2, 1, 3], [float("nan"), 0, 2, 3], [20, 20, 22, 23], [True, 0, 2, 3]):
            with self.subTest(box=box), self.assertRaises(numeric.NumericEvidenceError):
                numeric._ocr_crop_clip(box, [10, 10])

    def test_crop_reads_record_the_actual_source_clip_and_same_pixels_for_both_modes(self):
        with fitz.open() as document:
            page = document.new_page(width=250, height=130)
            page.insert_text((40, 55), "4.8", fontsize=18)
            box = list(page.get_text("words")[0][:4])
            clip = numeric._ocr_crop_clip(box, [250.0, 130.0])
            expected = numeric._image(page.get_pixmap(dpi=600, clip=fitz.Rect(clip), colorspace=fitz.csRGB, alpha=False))

            def engine(mosaic, **options):
                self.assertEqual(options["dpi"], 600)
                self.assertEqual(mosaic.crop((24, 24, 24 + expected.width, 24 + expected.height)).tobytes(), expected.tobytes())
                return [{"bbox": [24, 24, 24 + expected.width, 24 + expected.height], "text": "4.8", "block": 1, "line": 1}]

            with mock.patch.object(numeric, "_read_tesseract", side_effect=engine) as engine_mock:
                reads = numeric._crop_reads(page, {0: {"bbox": box}}, language="eng", tessdata=None, command="unused")[0]
            self.assertEqual(engine_mock.call_count, 2)
            for read in reads:
                self.assertEqual(read["literal"], "4.8")
                self.assertEqual(read["field_count"], 1)
                self.assertEqual(read["crop_policy"], numeric.OCR_CROP_POLICY)
                self.assertEqual(read["source_clip_bbox"], clip)
                self.assertEqual(read["crop_pixel_size"], list(expected.size))
                self.assertEqual(read["input_pixel_sha256"], numeric._sha(expected.tobytes()))

            def page_and_crop_engine(image, **options):
                if options["dpi"] == 450:
                    return [{"bbox": [value * 450 / 72 for value in box], "text": "4.8", "block": 1, "line": 1}]
                return engine(image, **options)

            with mock.patch.object(numeric, "_read_tesseract", side_effect=page_and_crop_engine):
                result = numeric.audit_numeric_evidence(page, "4.8", primary_words=page.get_text("words"),
                                                       language="eng", tesseract_command="unused")
            self.assertEqual(result["evidence"]["verified_count"], 1)
            with tempfile.TemporaryDirectory() as directory:
                image_path = Path(directory) / "source.png"
                page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False).save(str(image_path))
                numeric.validate_numeric_evidence(result["safe_text"], result["evidence"],
                                                  result["evidence"]["input_pixel_sha256"], image_path=image_path)

    def test_spanning_mosaic_word_cannot_borrow_numbers_from_other_crop_rows(self):
        with fitz.open() as document:
            page = document.new_page(width=250, height=160)
            page.insert_text((40, 55), "4.8", fontsize=18)
            page.insert_text((40, 110), "7.5", fontsize=18)
            words = page.get_text("words")
            positioned = {index: {"bbox": list(word[:4])} for index, word in enumerate(words)}
            def giant_candidate(image, **options):
                return [{"bbox": [0, 0, image.width, image.height], "text": "4.8", "block": 1, "line": 1}]
            with mock.patch.object(numeric, "_read_tesseract", side_effect=giant_candidate) as engine:
                reads = numeric._crop_reads(page, positioned, language="eng", tessdata=None, command="unused")
            self.assertEqual(engine.call_count, 2)
            for field in reads.values():
                self.assertTrue(all(read["literal"] is None and read["field_count"] == 0 for read in field))
                self.assertTrue(all("crop_read_recovery" not in read for read in field))
        tiny, giant = [24, 24, 102, 152], [0, 0, 126, 1000]
        self.assertEqual(numeric._overlap(tiny, giant), 1)
        self.assertEqual(numeric._source_crop_hits([{"bbox": giant, "literal": "0"}], tiny), ([], False))

    def overflow_fixture(self, *, isolated_literals=("4.8",), persistent_overflow=False):
        with fitz.open() as document:
            page = document.new_page(width=250, height=130)
            page.insert_text((40, 55), "4.8", fontsize=18)
            words = page.get_text("words")
            box = list(words[0][:4])
            clip = numeric._ocr_crop_clip(box, [250.0, 130.0])
            crop = numeric._image(page.get_pixmap(dpi=600, clip=fitz.Rect(clip), colorspace=fitz.csRGB, alpha=False))
            isolated_height = crop.height + 2 * numeric.ISOLATED_PADDING
            def engine(image, **options):
                if options["dpi"] == 450:
                    return [{"bbox": [value * 450 / 72 for value in box], "text": "4.8", "block": 1, "line": 1}]
                self.assertEqual(options["dpi"], 600)
                self.assertEqual(image.crop((24, 24, crop.width + 24, crop.height + 24)).tobytes(), crop.tobytes())
                if options["psm"] == 11 and (image.height != isolated_height or persistent_overflow):
                    return [{"bbox": [24, 24, crop.width + 24, crop.height + 24],
                             "text": "4.8", "block": index + 1, "line": 1}
                            for index in range(numeric.MAX_FIELDS + 1)]
                literals = isolated_literals if options["psm"] == 11 else ("4.8",)
                return [{"bbox": [24, 24, crop.width + 24, crop.height + 24],
                         "text": literal, "block": index + 1, "line": 1}
                        for index, literal in enumerate(literals)]
            with mock.patch.object(numeric, "_read_tesseract", side_effect=engine) as calls:
                result = numeric.audit_numeric_evidence(page, "4.8", primary_words=words,
                                                       language="eng", tesseract_command="unused")
            image = numeric._image(page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False))
        return result, image, calls.call_args_list

    def test_overflow_recovers_once_with_same_psm_pixels_and_three_independent_reads(self):
        result, source_image, calls = self.overflow_fixture()
        record = result["evidence"]["records"][0]
        self.assertEqual([call.kwargs["psm"] for call in calls], [3, 6, 11, 11])
        self.assertEqual([call.kwargs["dpi"] for call in calls], [450, 600, 600, 600])
        self.assertEqual(result["safe_text"], "4.8")
        self.assertEqual(result["evidence"]["verified_count"], 1)
        self.assertEqual(len(record["reads"]), 3)
        self.assertNotIn("crop_read_recovery", record["reads"][1])
        recovered = record["reads"][2]
        metadata = json.loads(recovered["crop_read_recovery"])
        self.assertEqual(recovered["field_count"], 1)
        self.assertEqual(metadata["mosaic_field_count_lower_bound"], numeric.MAX_FIELDS + 1)
        self.assertEqual(metadata["crop_pixel_sha256"], record["reads"][1]["input_pixel_sha256"])
        self.assertEqual(metadata["padding_pixels"], 24)
        self.assertEqual(metadata["isolated_canvas_size"], [value + 48 for value in recovered["crop_pixel_size"]])
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "source.png"
            source_image.save(image_path)
            numeric.validate_numeric_evidence(result["safe_text"], result["evidence"],
                                              result["evidence"]["input_pixel_sha256"], image_path=image_path)
        import audit_market_views_ocr_receipt as public_audit
        projected = json.dumps(public_audit._diagnostic_read(recovered))
        self.assertNotIn("crop_read_recovery", projected)
        self.assertNotIn(metadata["crop_png_base64"], projected)

    def test_isolated_overflow_still_exits_at_the_unchanged_field_bound(self):
        with self.assertRaisesRegex(numeric.NumericEvidenceError, "exceeds the field bound"):
            self.overflow_fixture(persistent_overflow=True)
        self.assertEqual(numeric.MAX_FIELDS, 2500)

    def test_recovered_empty_ambiguous_or_conflicting_read_stays_unresolved(self):
        for literals, count in (((), 0), (("4.8", "7.5"), 2), (("7.5",), 1)):
            with self.subTest(count=count, literals=literals):
                result, _, calls = self.overflow_fixture(isolated_literals=literals)
                record = result["evidence"]["records"][0]
                self.assertEqual(len(calls), 4)
                self.assertEqual(record["reads"][2]["field_count"], count)
                if count != 1:
                    self.assertIsNone(record["reads"][2]["literal"])
                self.assertEqual(record["status"], "unresolved")
                self.assertEqual(result["safe_text"], "[数值待核对:n0001]")
                numeric.validate_numeric_evidence(result["safe_text"], result["evidence"], result["evidence"]["input_pixel_sha256"])

    def test_one_overflowing_crop_does_not_reread_its_unaffected_neighbour(self):
        with fitz.open() as document:
            page = document.new_page(width=250, height=160)
            page.insert_text((40, 55), "4.8", fontsize=18)
            page.insert_text((40, 110), "7.5", fontsize=18)
            boxes = [list(word[:4]) for word in page.get_text("words")]
            crops = [numeric._image(page.get_pixmap(dpi=600, clip=fitz.Rect(numeric._ocr_crop_clip(box, [250, 160])),
                                                  colorspace=fitz.csRGB, alpha=False)) for box in boxes]
            def engine(image, **options):
                isolated = image.height == crops[0].height + 48
                first = {"bbox": [24, 24, crops[0].width + 24, crops[0].height + 24], "text": "4.8", "block": 1, "line": 1}
                if isolated:
                    self.assertEqual(options["psm"], 11)
                    return [first]
                top = 24 + crops[0].height + 48
                second = {"bbox": [24, top, crops[1].width + 24, top + crops[1].height], "text": "7.5", "block": 9999, "line": 1}
                if options["psm"] == 6:
                    return [first, second]
                return [{**first, "block": index + 1} for index in range(numeric.MAX_FIELDS + 1)] + [second]
            with mock.patch.object(numeric, "_read_tesseract", side_effect=engine) as calls:
                reads = numeric._crop_reads(page, {index: {"bbox": box} for index, box in enumerate(boxes)},
                                            language="eng", tessdata=None, command="unused")
        self.assertEqual(calls.call_count, 3)
        self.assertIn("crop_read_recovery", reads[0][1])
        self.assertNotIn("crop_read_recovery", reads[1][1])
        self.assertEqual([read["literal"] for read in reads[1]], ["7.5", "7.5"])

    def test_actual_incident_tiny_crop_geometry_is_preserved_during_isolation(self):
        with fitz.open() as document:
            page = document.new_page(width=612, height=776.5689697265625)
            box = [424.08, 116.16, 430.3044, 129.8537]
            page.draw_rect(fitz.Rect(box), color=None, fill=(0, 0, 0))
            def engine(image, **options):
                field = {"bbox": [24, 24, 102, 152], "text": "0", "block": 1, "line": 1}
                if options["psm"] == 11 and image.height != 176:
                    return [{**field, "block": index + 1} for index in range(numeric.MAX_FIELDS + 1)]
                self.assertEqual(image.crop((24, 24, 102, 152)).size, (78, 128))
                return [field]
            with mock.patch.object(numeric, "_read_tesseract", side_effect=engine):
                reads = numeric._crop_reads(page, {0: {"bbox": box}}, language="eng", tessdata=None, command="unused")[0]
        for read in reads:
            self.assertEqual(read["crop_pixel_size"], [78, 128])
        metadata = json.loads(reads[1]["crop_read_recovery"])
        self.assertEqual(metadata["isolated_canvas_size"], [126, 176])
        numeric._validate_overflow_recovery(reads[1], [78, 128])

    def test_recovery_receipt_rejects_typed_metadata_duplicate_keys_hashes_and_covert_fields(self):
        result, _, _ = self.overflow_fixture()
        for change in ("duplicate", "extra", "boolean", "crop_hash", "canvas_hash", "size", "padding", "lower_bound", "bad_png", "bound"):
            evidence = copy.deepcopy(result["evidence"])
            read = evidence["records"][0]["reads"][2]
            value = json.loads(read["crop_read_recovery"])
            if change == "duplicate":
                read["crop_read_recovery"] = read["crop_read_recovery"].replace('"schema":1', '"schema":1,"schema":1')
            else:
                if change == "extra": value["PRIVATE"] = "PRIVATE"
                elif change == "boolean": value["schema"] = True
                elif change == "crop_hash": value["crop_pixel_sha256"] = "0" * 64
                elif change == "canvas_hash": value["isolated_canvas_pixel_sha256"] = "0" * 64
                elif change == "size": value["isolated_canvas_size"][0] += 1
                elif change == "padding": value["padding_pixels"] = 25
                elif change == "lower_bound": value["mosaic_field_count_lower_bound"] = 2500
                elif change == "bad_png": value["crop_png_base64"] = base64.b64encode(b"PRIVATE").decode()
                elif change == "bound": read["field_count"] = numeric.MAX_FIELDS + 1
                read["crop_read_recovery"] = numeric._canonical(value).decode()
            sign_evidence(evidence)
            with self.subTest(change=change), self.assertRaises(numeric.NumericEvidenceError):
                numeric.validate_numeric_evidence(result["safe_text"], evidence, evidence["input_pixel_sha256"])

    def test_recovery_png_dimensions_pixels_and_chunks_are_checked_before_expansion(self):
        result, _, _ = self.overflow_fixture()
        original = result["evidence"]["records"][0]["reads"][2]
        value = json.loads(original["crop_read_recovery"])
        raw = base64.b64decode(value["crop_png_base64"])
        for change in ("header", "ancillary", "trailing", "crc"):
            mutated = bytearray(raw)
            if change == "header":
                mutated[16:24] = (100_000).to_bytes(4, "big") * 2
                mutated[29:33] = (binascii.crc32(mutated[12:29]) & 0xffffffff).to_bytes(4, "big")
            elif change == "ancillary":
                payload = b"PRIVATE"
                chunk = len(payload).to_bytes(4, "big") + b"tEXt" + payload + (binascii.crc32(b"tEXt" + payload) & 0xffffffff).to_bytes(4, "big")
                mutated[33:33] = chunk
            elif change == "trailing": mutated += b"PRIVATE"
            else: mutated[29] ^= 1
            read = copy.deepcopy(original)
            metadata = dict(value, crop_png_base64=base64.b64encode(mutated).decode())
            read["crop_read_recovery"] = numeric._canonical(metadata).decode()
            with self.subTest(change=change), mock.patch.object(numeric.Image, "open", side_effect=AssertionError("Malformed PNG must be rejected before decompression")), \
                    self.assertRaises(numeric.NumericEvidenceError):
                numeric._validate_overflow_recovery(read, read["crop_pixel_size"])
        with mock.patch.object(numeric, "MAX_IMAGE_PIXELS", 1), \
                mock.patch.object(numeric.Image, "open", side_effect=AssertionError("Pixel bound must be checked before decompression")), \
                self.assertRaises(numeric.NumericEvidenceError):
            numeric._validate_overflow_recovery(original, original["crop_pixel_size"])

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

    def test_tight_crop_metadata_is_rechecked_without_breaking_legacy_receipts(self):
        result, image = self._audit()
        legacy = copy.deepcopy(result["evidence"])
        numeric.validate_numeric_evidence(result["safe_text"], legacy, legacy["input_pixel_sha256"])
        evidence = copy.deepcopy(legacy)
        record = evidence["records"][0]
        clip = numeric._ocr_crop_clip(record["bbox"], evidence["page_size_points"])
        for read in record["reads"][1:]:
            read.update(crop_policy=numeric.OCR_CROP_POLICY, source_clip_bbox=clip,
                        crop_pixel_size=numeric._ocr_crop_pixel_size(clip))
        sign_evidence(evidence)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "original.png"
            image.save(str(path))
            numeric.validate_numeric_evidence(result["safe_text"], evidence, evidence["input_pixel_sha256"], image_path=path)
            for mutation in ("clip", "size", "policy", "different_pixels", "partial", "multiple_fields"):
                changed = copy.deepcopy(evidence)
                read = changed["records"][0]["reads"][1]
                if mutation == "clip":
                    read["source_clip_bbox"][0] -= 1
                elif mutation == "size":
                    read["crop_pixel_size"][0] += 1
                elif mutation == "policy":
                    read["crop_policy"] = "other-crop"
                elif mutation == "different_pixels":
                    read["input_pixel_sha256"] = "c" * 64
                elif mutation == "partial":
                    changed["records"][0]["reads"][2].pop("source_clip_bbox")
                else:
                    read["field_count"] = 2
                sign_evidence(changed)
                with self.subTest(mutation=mutation), self.assertRaises(numeric.NumericEvidenceError) as failure:
                    numeric.validate_numeric_evidence(result["safe_text"], changed, changed["input_pixel_sha256"], image_path=path)
                if mutation in {"clip", "size", "policy", "partial"}:
                    diagnostic = failure.exception.diagnostics
                    self.assertEqual(diagnostic["record_id"], "n0001")
                    self.assertEqual(diagnostic["expected_clip_bbox"], clip)
                    self.assertEqual(diagnostic["expected_pixel_size"], numeric._ocr_crop_pixel_size(clip))
                    key = {"clip": "clip_matches", "size": "size_matches", "policy": "policy_matches", "partial": "clip_valid"}[mutation]
                    self.assertIs(diagnostic[key], False)

    def test_crop_failure_diagnostics_are_a_pure_bounded_geometry_whitelist(self):
        private = "PRIVATE https://private.invalid signed token source words"
        source = {"schema": 1, "record_id": "n0008", "psm": 6, "field_bbox": [10.1, 20.2, 30.3, 40.4],
                  "page_bounds": [0, 0, 612, 776.5689697], "expected_clip_bbox": [9, 19, 31, 41],
                  "actual_clip_bbox": [9, 19, 31, 41], "expected_pixel_size": [185, 185],
                  "actual_pixel_size": [184, 185], "size_matches": False, "dpi": 600, "field_count": 1,
                  "pymupdf_version": "1.28.2",
                  "source_name": private, "literal": private, "url": private, "unknown": private}
        before = copy.deepcopy(source)
        error = numeric.NumericEvidenceError("Numeric crop geometry differs from its positioned source field", diagnostics=source)
        self.assertEqual(source, before)
        self.assertEqual(error.diagnostics["actual_pixel_size"], [184, 185])
        self.assertIs(error.diagnostics["size_matches"], False)
        self.assertEqual(error.diagnostics["pymupdf_version"], "1.28.2")
        self.assertEqual(numeric.safe_geometry_diagnostics(error), error.diagnostics)
        forwarded = ValueError(private)
        forwarded.geometry_diagnostics = error.diagnostics
        self.assertEqual(numeric.safe_geometry_diagnostics(forwarded), error.diagnostics)
        self.assertEqual(numeric.safe_geometry_diagnostics(error.diagnostics), error.diagnostics)
        self.assertNotIn("PRIVATE", json.dumps(error.diagnostics, allow_nan=False))
        error.diagnostics["field_bbox"][0] = 12
        self.assertEqual(source, before)
        malformed = {"schema": 1, "record_id": private, "psm": True, "size_matches": private,
                     "field_bbox": [0, 0, float("inf"), 10], "actual_clip_bbox": [0, 0, 100001, 10],
                     "actual_pixel_size": [True, 10], "expected_pixel_size": [10, 100001],
                     "dpi": private, "field_count": 2501, "pymupdf_version": private, "private": private,
                     "field_count_kind": {"PRIVATE": private}, "field_count_above_bound": private,
                     "field_count_capped_count": 2501}
        self.assertEqual(numeric.safe_numeric_geometry_diagnostics(malformed), {"schema": 1})
        for value in (None, private, [], {"schema": True}, {"schema": 2}):
            self.assertIsNone(numeric.safe_numeric_geometry_diagnostics(value))
        self.assertIsNone(numeric.safe_geometry_diagnostics(ValueError(private)))

    def test_invalid_crop_field_count_diagnostic_distinguishes_type_and_bound_without_raw_value(self):
        result, _ = self._audit()
        evidence = copy.deepcopy(result["evidence"])
        record = evidence["records"][0]
        clip = numeric._ocr_crop_clip(record["bbox"], evidence["page_size_points"])
        for read in record["reads"][1:]:
            read.update(crop_policy=numeric.OCR_CROP_POLICY, source_clip_bbox=clip,
                        crop_pixel_size=numeric._ocr_crop_pixel_size(clip))
        for value, kind, cap, above in ((None, "null", None, False), (True, "boolean", None, False),
                                      ("PRIVATE 9000", "other", None, False), (-1, "integer", 0, False),
                                      (2501, "integer", 2500, True), (10 ** 100, "integer", 2500, True),
                                      ("missing", "missing", None, False)):
            changed = copy.deepcopy(evidence)
            read = changed["records"][0]["reads"][2]
            if value == "missing":
                read.pop("field_count")
            else:
                read["field_count"] = value
            sign_evidence(changed)
            with self.subTest(kind=kind, cap=cap), self.assertRaises(numeric.NumericEvidenceError) as failure:
                numeric.validate_numeric_evidence(result["safe_text"], changed, changed["input_pixel_sha256"])
            diagnostic = numeric.safe_geometry_diagnostics(failure.exception)
            self.assertEqual(diagnostic["field_count_kind"], kind)
            self.assertIs(diagnostic["field_count_above_bound"], above)
            self.assertFalse(diagnostic["field_count_valid"])
            self.assertTrue(diagnostic["clip_matches"])
            self.assertTrue(diagnostic["size_matches"])
            self.assertNotIn("field_count", diagnostic)
            if cap is None:
                self.assertNotIn("field_count_capped_count", diagnostic)
            else:
                self.assertEqual(diagnostic["field_count_capped_count"], cap)
            self.assertNotIn("PRIVATE", json.dumps(diagnostic))
            self.assertEqual(numeric.safe_geometry_diagnostics(diagnostic), diagnostic)

    def test_tight_reads_cannot_overrule_wide_witness_for_an_omitted_minus_or_percent(self):
        for original, primary in (("-3%", "3%"), ("3%", "3")):
            with self.subTest(original=original), fitz.open() as document:
                page = document.new_page(width=250, height=130)
                page.insert_text((100, 55), original, fontsize=10)
                box = list(page.get_text("words")[0][:4])
                if original.startswith("-"):
                    box[0] += fitz.get_text_length("-", fontsize=10)
                else:
                    box[2] -= fitz.get_text_length("%", fontsize=10)
                box = [round(value, 4) for value in box]
                clip = numeric._ocr_crop_clip(box, [250.0, 130.0])
                reads = [{"method": f"source-crop-psm-{psm}", "dpi": 600, "literal": primary, "field_count": 1,
                          "input_pixel_sha256": "b" * 64, "crop_policy": numeric.OCR_CROP_POLICY,
                          "source_clip_bbox": clip, "crop_pixel_size": numeric._ocr_crop_pixel_size(clip)} for psm in (6, 11)]
                second = [{"bbox": [value * 450 / 72 for value in box], "text": primary, "block": 1, "line": 1}]
                word = tuple(box + [primary, 0, 0, 0])
                with mock.patch.object(numeric, "_read_tesseract", return_value=second), \
                        mock.patch.object(numeric, "_crop_reads", return_value={0: reads}):
                    result = numeric.audit_numeric_evidence(page, primary, primary_words=[word], language="eng", tesseract_command="unused")
                self.assertEqual(result["evidence"]["verified_count"], 0)
                self.assertEqual(result["evidence"]["unresolved_count"], 1)
                self.assertEqual(result["evidence"]["records"][0]["reason"],
                                 "visible_minus_omitted" if original.startswith("-") else "visible_percent_omitted")
                self.assertEqual(result["safe_text"], "[数值待核对:n0001]")

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

    def test_dense_scanned_prose_numeric_crop_excludes_neighboring_words(self):
        with fitz.open() as vector:
            page = vector.new_page(width=360, height=130)
            for y, text in ((58, "BROAD SOURCE CONTEXT FOR THE REPORT"),
                            (70, "Operating 17% leverage improved"),
                            (82, "CURRENT QUARTERLY OPERATING VALUES")):
                page.insert_text((20, y), text, fontsize=10)
            raster = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False).tobytes("png")
        with fitz.open() as document:
            page = document.new_page(width=360, height=130)
            page.insert_image(page.rect, stream=raster)
            self.assertEqual(page.get_text("text"), "")
            text, words = self._first_read(page)
            self.assertIn("17%", text, "The regression requires a correct positioned first read")
            result = numeric.audit_numeric_evidence(page, text, primary_words=words, language="eng", tessdata=self.tessdata)
            fields = [record for record in result["evidence"]["records"] if record["literal"] == "17%"]
            self.assertEqual(len(fields), 1)
            field = fields[0]
            self.assertEqual(field["status"], "verified")
            self.assertEqual([numeric.normalize_number(read["literal"]) for read in field["reads"]], ["17%"] * 3)
            self.assertTrue(field["pixel_punctuation"]["percent_marks"])
            self.assertEqual([read["crop_policy"] for read in field["reads"][1:]], [numeric.OCR_CROP_POLICY] * 2)
            self.assertLess(field["reads"][1]["source_clip_bbox"][3] - field["reads"][1]["source_clip_bbox"][1],
                            (field["bbox"][3] - field["bbox"][1]) + 2 * numeric._field_padding(field["bbox"]))


if __name__ == "__main__":
    unittest.main()
