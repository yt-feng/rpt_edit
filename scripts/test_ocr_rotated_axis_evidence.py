"""Pure pixels/mock recognition contracts; no local OCR or network required."""
import copy
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock

import fitz
from PIL import Image, ImageDraw

import ocr_rotated_axis_evidence as axis
import ocr_numeric_evidence as numeric

MODELS = [{"language": "eng", "filename": "eng.traineddata", "sha256": "a" * 64}]


def synthetic_case(regions=1, *, reader=None, clock=None, multiline=False, repeated_axes=False, diagnostics=None):
    document = fitz.open()
    page = document.new_page(width=400, height=650)
    if multiline:
        page.insert_text((20, 30), "Reviewed market trends economic projections", fontsize=8)
        page.insert_text((20, 50), "Supply demand reliable recovery outlook remains steady", fontsize=8)
        page.insert_text((20, 75), "Revenue 25,000", fontsize=12)
        page.insert_text((20, 235), "Forecast 35,000", fontsize=12)
        page.insert_text((20, 275), "Margin -3.1%", fontsize=18)
    else:
        page.insert_text((20, 30), "Reliable revenue supply demand outlook recovery remains steady 25,000 35,000", fontsize=8)
    words = [{"bbox": list(w[:4]), "text": w[4], "block": w[5], "paragraph": 0, "line": w[6]}
             for w in page.get_text("words")]
    for i in range(regions):
        y = 120 + i * 100
        words.append({"bbox": [50, y, 190, y + 7], "text": ("A" if repeated_axes else chr(65 + i)) * 85,
                      "block": i + 10, "paragraph": 0, "line": 0})
        for x, literal in zip((70, 115, 160), ("2020/01", "2021/02", "2022/03")):
            page.insert_text((x, y + 5), literal, fontsize=6, rotate=90)
    words.sort(key=lambda w: (w["bbox"][1], w["bbox"][0]))
    if multiline:
        groups = {}
        for word in words:
            groups.setdefault((word["block"], word["line"]), []).append(word)
        text = "\n\n".join(" ".join(w["text"] for w in group) for group in groups.values())
    else:
        text = "\n".join(w["text"] for w in words)
    candidates = {key: {"text": text, "words": copy.deepcopy(words)} for key in axis.LABELS}
    candidates["full-page-psm11"]["text"] = axis._region_text(words)[0]
    calls = []
    def engine(image, **options):
        calls.append((image.size, dict(options)))
        if reader:
            return reader(image, len(calls), options)
        if len(calls) % 2 == 1:
            return [{"bbox": [3, 3, 15, 15], "text": "garbage", "block": 0, "paragraph": 0, "line": 0}]
        return date_words(image.size)
    result = axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
                tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS,
                reader=engine, clock=clock, diagnostics=diagnostics)
    return document, page, candidates, result, calls


def date_words(size, values=("2020/01", "2021/02", "2022/03")):
    return [{"bbox": [3, 30 + i * 90, min(size[0] - 3, 85), 45 + i * 90], "text": value,
             "block": 1, "paragraph": 0, "line": i + 1} for i, value in enumerate(values)]


def numeric_engine(page, result):
    """Exercise the real horizontal crop builder and three-read decision path."""
    image = numeric._image(page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False))
    context = axis.replay_rotated_axis_proof(result["proof"], result["primary_text"],
        input_pixel_sha256=axis._hash(image.tobytes()), page_size_points=[400.0, 650.0], source_image=image)
    fields = list(context["positioned"].values())
    calls = []
    def read(image, **options):
        calls.append((options["dpi"], options["psm"]))
        if options["dpi"] == 450:
            return [{"bbox": [v * 450 / 72 for v in field["bbox"]], "text": field["literal"],
                     "block": i + 1, "paragraph": 0, "line": 1} for i, field in enumerate(fields)]
        assert options["dpi"] == 600
        words, top = [], 24
        for i, field in enumerate(fields):
            clip = numeric._ocr_crop_clip(field["bbox"], [400.0, 650.0])
            crop = page.get_pixmap(dpi=600, clip=fitz.Rect(clip), colorspace=fitz.csRGB, alpha=False)
            words.append({"bbox": [24, top, 24 + crop.width, top + crop.height], "text": field["literal"],
                          "block": i + 1, "paragraph": 0, "line": 1})
            top += crop.height + 48
        return words
    return read, calls


def chart_boundary_case(*, real_size=False):
    """Source pixels contain a baseline/zero above complete vertical dates."""
    document = fitz.open()
    page = document.new_page(width=400, height=650)
    page.insert_text((20, 30), "Reliable revenue supply demand outlook recovery remains steady 25,000 35,000", fontsize=8)
    words = [{"bbox": list(w[:4]), "text": w[4], "block": w[5], "paragraph": 0, "line": w[6]}
             for w in page.get_text("words")]
    y, font, xs, box = ((158, 10, (70, 150, 230), [60, 150, 270, 160]) if real_size
                        else (125, 6, (70, 115, 160), [50, 120, 190, 127]))
    # The larger fixture's expanded axis band starts at 120 pt. Keep the
    # baseline inside that band so the cloud test actually exercises source
    # pixel separation, with a white gap before the dates starting at 122 pt.
    baseline = 120 if real_size else 100
    page.draw_line((box[0], baseline), (box[2], baseline), color=(.85, .85, .85), width=.5)
    page.insert_text((box[0] - 2, baseline), "0", fontsize=7)
    for x, literal in zip(xs, ("2010/01", "2018/07", "2026/07")):
        page.insert_text((x, y), literal, fontsize=font, rotate=90)
    words.append({"bbox": [box[0] - 2, baseline - 6, box[0] + 2, baseline + .2], "text": "0",
                  "block": 9, "paragraph": 0, "line": 0})
    words.append({"bbox": box, "text": "A" * 85, "block": 10, "paragraph": 0, "line": 0})
    words.sort(key=lambda w: (w["bbox"][1], w["bbox"][0]))
    candidates = {label: {"text": "\n".join(w["text"] for w in words), "words": copy.deepcopy(words)}
                  for label in axis.LABELS}
    candidates["full-page-psm11"]["text"] = axis._region_text(words)[0]
    return document, page, candidates


class RotatedAxisTests(unittest.TestCase):
    def replay(self, page, result, proof=None, text=None):
        pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        return axis.replay_rotated_axis_proof(proof or result["proof"], text or result["primary_text"],
            input_pixel_sha256=axis._hash(image.tobytes()), page_size_points=[400.0, 650.0],
            source_image=image, language="eng", traineddata=MODELS)

    def test_complete_original_candidates_pixels_words_and_unchanged_horizontal_fields(self):
        doc, page, candidates, result, calls = synthetic_case()
        self.addCleanup(doc.close)
        self.assertIsNotNone(result)
        self.assertEqual(result["proof"]["candidates"], candidates)
        self.assertEqual(len(calls), 2)
        self.assertTrue(all(call[1]["psm"] == 6 and call[1]["dpi"] == 300 and call[1]["timeout_seconds"] <= 30 for call in calls))
        derived = self.replay(page, result)
        self.assertEqual([row["literal"] for row in derived["positioned"].values()], ["25,000", "35,000"])
        self.assertEqual(len(derived["rotated_mentions"]), 6)
        self.assertFalse(set(derived["positioned"]) & set(derived["rotated_mentions"]))
        self.assertTrue(all(len(row["source_quad"]) == 4 for row in derived["rotated_mentions"].values()))
        self.assertIn("2020/01\n2021/02\n2022/03", result["primary_text"])
        for retained in result["proof"]["ledger"]["retained"]:
            old = candidates["source-flow"]["text"][retained["old_begin"]:retained["old_end"]]
            self.assertEqual(old, result["primary_text"][retained["new_begin"]:retained["new_end"]])

    def test_rejected_recovery_exposes_only_bounded_stage_geometry_and_counts(self):
        diagnostics = {}
        doc, _, _, result, calls = synthetic_case(diagnostics=diagnostics,
            reader=lambda image, call, options: date_words(image.size, ("private", "source", "prose")))
        self.addCleanup(doc.close)
        self.assertIsNone(result)
        self.assertEqual(len(calls), 2)
        self.assertEqual(diagnostics["stage"], "region_recognition")
        self.assertEqual(diagnostics["reason"], "no_valid_direction")
        self.assertEqual(diagnostics["reads"], [
            {"angle": angle, "words": 3, "date_words": 0, "accepted": False} for angle in (90, 270)])
        self.assertEqual(axis.safe_rotated_axis_diagnostics({**diagnostics, "url": "PRIVATE"}), diagnostics)
        self.assertNotIn("private", str(diagnostics))
        for key, value in (("stage", []), ("reason", "PRIVATE"), ("region", True),
                           ("planned_region_count", 5), ("source_pixel_box", [1, 2, 1, 4]), ("reads", [])):
            with self.subTest(key=key):
                self.assertIsNone(axis.safe_rotated_axis_diagnostics({**diagnostics, key: value}))
        doc, page, candidates, _, _ = synthetic_case()
        self.addCleanup(doc.close)
        candidates.pop("geometric-sorted")
        reader = mock.Mock(side_effect=AssertionError("No recognition"))
        self.assertIsNone(axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
            tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS,
            reader=reader, diagnostics=diagnostics))
        self.assertEqual(diagnostics, {"schema": 1, "stage": "candidate_validation", "reason": "invalid_candidate_evidence"})
        reader.assert_not_called()

    def test_planning_rejection_reports_exact_guard_and_conflicting_geometry_without_words(self):
        document, page, candidates, _, _ = synthetic_case()
        self.addCleanup(document.close)
        body = {"bbox": [70, 110, 80, 117], "text": "PrivateBody", "block": 99, "paragraph": 0, "line": 0}
        for candidate in candidates.values():
            candidate["words"].append(copy.deepcopy(body))
            candidate["text"] += "\n" + body["text"]
        candidates["full-page-psm11"]["text"] = axis._region_text(candidates["full-page-psm11"]["words"])[0]
        diagnostics, reader = {}, mock.Mock(side_effect=AssertionError("No recognition"))
        self.assertIsNone(axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
            tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS,
            reader=reader, diagnostics=diagnostics))
        self.assertEqual(diagnostics["stage"], "region_planning")
        self.assertEqual(diagnostics["reason"], "horizontal_word_intersection")
        self.assertEqual(diagnostics["source_word_box"], body["bbox"])
        self.assertEqual(len(diagnostics["source_pixel_box"]), 4)
        self.assertNotIn("PrivateBody", str(diagnostics))
        reader.assert_not_called()
        candidates["source-flow"]["words"][0]["bbox"] = [-1, 0, 20, 30]
        self.assertIsNone(axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
            tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS,
            reader=reader, diagnostics=diagnostics))
        self.assertEqual(diagnostics["reason"], "source-flow_words")

    def test_max_four_regions_eight_reads_and_shared_remaining_subprocess_budget(self):
        doc, page, _, result, calls = synthetic_case(4)
        self.addCleanup(doc.close)
        self.assertEqual(len(result["proof"]["regions"]), 4)
        self.assertEqual(len(calls), 8)
        self.replay(page, result)
        clock = iter((0, 0, 175, 175, 177, 178)).__next__
        doc2, _, _, result2, calls2 = synthetic_case(clock=clock)
        self.addCleanup(doc2.close)
        self.assertIsNotNone(result2)
        self.assertEqual([c[1]["timeout_seconds"] for c in calls2], [30, 5])
        clock = iter((0, 0, 180)).__next__
        with self.assertRaisesRegex(axis.RotatedAxisError, '^rotated_axis_time_budget_exhausted$'):
            synthetic_case(clock=clock)

    def test_multiline_global_spans_after_header_and_axis_keep_exact_horizontal_boxes(self):
        doc, page, candidates, result, _ = synthetic_case(multiline=True)
        self.addCleanup(doc.close)
        self.assertIsNotNone(result)
        derived = self.replay(page, result)
        original = numeric._align_mentions(numeric.numeric_mentions(candidates["source-flow"]["text"]),
                                          numeric._word_mentions(candidates["source-flow"]["words"]))
        horizontal = list(derived["positioned"].values())
        self.assertEqual([r["literal"] for r in horizontal], ["25,000", "35,000", "-3.1%"])
        self.assertEqual([r["bbox"] for r in horizontal], [r["bbox"] for r in original.values()])
        self.assertGreater(horizontal[1]["begin"], horizontal[0]["end"] + 21)
        engine, calls = numeric_engine(page, result)
        with mock.patch.object(numeric, "_read_tesseract", side_effect=engine):
            audit = numeric.audit_numeric_evidence(page, result["primary_text"], language="eng",
                tesseract_command="unused", rotated_axis_proof=result["proof"])
        records = [r for r in audit["evidence"]["records"] if "rotated_axis" not in r]
        self.assertEqual([r["bbox"] for r in records], [r["bbox"] for r in horizontal])
        self.assertTrue(all(len(r["reads"]) == 3 for r in records))
        self.assertEqual(calls, [(450, 3), (600, 6), (600, 11)])

    def test_short_garbage_illegal_month_clipping_single_date_and_ambiguous_rotations_refused(self):
        for values in (("bad", "short", "noise"), ("2020/13", "2021/02", "2022/03"),
                       ("2020/01",), ("2020/01", "2020/01", "2020/01")):
            def reader(image, call, options):
                return date_words(image.size, values)
            doc, _, _, result, _ = synthetic_case(reader=reader)
            doc.close(); self.assertIsNone(result)
        def clipped(image, call, options):
            words = date_words(image.size); words[0]["bbox"][0] = 0
            return words
        doc, _, _, result, _ = synthetic_case(reader=clipped)
        doc.close(); self.assertIsNone(result)

    def test_split_date_words_are_refused_before_selection_and_repeated_years_keep_quads(self):
        for separator in ("/", "-"):
            def split(image, call, options):
                words = []
                for i, month in enumerate(("01", "02", "03")):
                    for j, text in enumerate(("2020", separator, month)):
                        words.append({"bbox": [3 + j * 25, 30 + i * 90, 22 + j * 25, 45 + i * 90],
                            "text": text, "block": 1, "paragraph": 0, "line": i + 1})
                return words
            doc, _, _, result, _ = synthetic_case(reader=split)
            doc.close(); self.assertIsNone(result)
        def repeated_year(image, call, options):
            return date_words(image.size, ("2020/01", "2020/02", "2020/03")) if call % 2 == 0 else date_words(
                image.size, ("bad", "bad", "bad"))
        doc, page, _, result, _ = synthetic_case(reader=repeated_year)
        self.addCleanup(doc.close)
        derived = self.replay(page, result)
        years = [metadata["source_quad"] for index, metadata in derived["rotated_mentions"].items()
                 if numeric.numeric_mentions(result["primary_text"])[index]["literal"] == "2020"]
        self.assertEqual(len(years), 3)
        self.assertEqual(len({axis._canonical(quad) for quad in years}), 3)
        doc, _, _, result, _ = synthetic_case(reader=lambda image, call, options: date_words(image.size))
        doc.close(); self.assertIsNone(result)

    def test_affine_corner_roundtrips_both_angles_are_exact_lossless_pixels(self):
        box = [11, 17, 83, 53]
        for angle in (90, 270):
            matrix, inverse = axis._transform(box, angle)
            for point in ([0, 0], [36, 0], [36, 72], [0, 72], [5.5, 12.25]):
                self.assertEqual(axis._point(axis._point(point, matrix), inverse), point)
        doc, page, _, result, _ = synthetic_case()
        self.addCleanup(doc.close)
        region = result["proof"]["regions"][0]
        self.assertEqual([read["angle"] for read in region["reads"]], [90, 270])
        self.replay(page, result)

    def test_tampering_any_geometry_pixels_ledger_words_selection_and_runtime_is_rejected(self):
        doc, page, _, result, _ = synthetic_case()
        self.addCleanup(doc.close)
        mutations = (
            lambda p: p["regions"][0]["reads"][0]["affine"].__setitem__(2, 1),
            lambda p: p["regions"][0]["reads"][1]["inverse_affine"].__setitem__(0, True),
            lambda p: p["regions"][0]["reads"][1]["affine"].__setitem__(1, True),
            lambda p: p["regions"][0].__setitem__("id", True),
            lambda p: p["regions"][0].__setitem__("source_crop_sha256", "b" * 64),
            lambda p: p["regions"][0]["reads"][0].__setitem__("input_pixel_sha256", "b" * 64),
            lambda p: p["regions"][0]["reads"][1]["words"][0]["bbox"].__setitem__(0, True),
            lambda p: p["ledger"]["retained"][0].__setitem__("old_end", 1),
            lambda p: p["regions"][0].__setitem__("selected_angle", 90),
            lambda p: p["runtime"].__setitem__("budget_seconds", 999),
            lambda p: p["runtime"]["traineddata"][0].__setitem__("sha256", "c" * 64),
            lambda p: p["candidates"]["geometric-sorted"]["words"][0].__setitem__("text", "changed"),
            lambda p: p["candidates"]["full-page-psm11"]["words"][0].__setitem__("text", "changed"),
            lambda p: p["candidates"]["full-page-psm11"].__setitem__("text", p["candidates"]["full-page-psm11"]["text"].replace(" ", "")),
            lambda p: p["regions"][0]["ink_profile"]["dark_counts"].__setitem__(0, 1),
            lambda p: p["regions"][0]["top_separation"].__setitem__("selected_top", True),
            lambda p: p["regions"][0]["top_separation"].__setitem__("threshold", 220),
            lambda p: p["candidates"]["geometric-sorted"]["words"].__setitem__(0,
                [*p["candidates"]["geometric-sorted"]["words"][0]["bbox"],
                 p["candidates"]["geometric-sorted"]["words"][0]["text"], 0, 0, {"covert": "extra"}]),
            lambda p: p.__setitem__("private_extra", "must not pass"),
        )
        for mutation in mutations:
            proof = copy.deepcopy(result["proof"]); mutation(proof)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                self.replay(page, result, proof)

    def test_wrong_word_order_body_and_edges_are_not_eligible(self):
        doc, page, candidates, result, _ = synthetic_case()
        self.addCleanup(doc.close)
        for kind in ("order", "body", "edge"):
            changed = copy.deepcopy(candidates)
            for value in changed.values():
                if kind == "order": value["words"].reverse()
                if kind == "body":
                    word = {"bbox": [80, 110, 120, 117], "text": "Body", "block": 99, "paragraph": 0, "line": 0}
                    value["words"].append(word); value["text"] += "\nBody"
                if kind == "edge": value["words"][-1]["bbox"] = [0, 120, 140, 127]
            reader = mock.Mock(side_effect=AssertionError("Recognition must not start"))
            with self.subTest(kind=kind):
                actual = axis.recover_rotated_axes(page, changed, language="eng", tessdata=None,
                    tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS, reader=reader)
                self.assertIsNone(actual); reader.assert_not_called()

    def test_repeated_axis_noise_has_exact_global_positions_and_swapped_indices_are_rejected(self):
        document, page, candidates, result, _ = synthetic_case(2, repeated_axes=True)
        self.addCleanup(document.close)
        self.assertIsNotNone(result)
        self.assertEqual(len(result["proof"]["regions"]), 2)
        runs = list(axis.LONG.finditer(candidates["source-flow"]["text"]))
        self.assertEqual(runs[0].group(), runs[1].group())
        self.assertNotEqual(runs[0].span(), runs[1].span())
        self.replay(page, result)
        changed = copy.deepcopy(result["proof"])
        a, b = changed["regions"]
        a["source_word_indices"], b["source_word_indices"] = b["source_word_indices"], a["source_word_indices"]
        with self.assertRaises(ValueError):
            self.replay(page, result, changed)
        changed = copy.deepcopy(result["proof"])
        changed["ledger"]["edits"][0]["word_index"] = result["proof"]["regions"][1]["source_word_indices"][0]
        with self.assertRaises(ValueError):
            self.replay(page, result, changed)

    def test_glued_glyph_identical_words_are_rejected_without_guessing_boundaries(self):
        text = "Abcd" * 30
        words = [{"text": text[:60], "bbox": [20, 20, 80, 26], "block": 1, "paragraph": 0, "line": 0},
                 {"text": text[60:], "bbox": [90, 20, 150, 26], "block": 1, "paragraph": 0, "line": 0}]
        with self.assertRaises(ValueError):
            axis._spans(text, words)

    def test_bounded_upward_expansion_and_adjacent_tall_axis_words_include_full_band(self):
        doc, _, candidates, _, _ = synthetic_case()
        self.addCleanup(doc.close)
        for value in candidates.values():
            value["words"][-1]["bbox"] = [74.64, 419.52, 234.4371, 428.1686]
            for index, x in enumerate((240, 251, 262)):
                word = {"bbox": [x, 407, x + 5, 428], "text": "2024/01", "block": 30 + index, "paragraph": 0, "line": 0}
                value["words"].append(word); value["text"] += "\n" + word["text"]
        plans = axis._select_regions(candidates, [400, 650], [1667, 2709])
        self.assertLess(plans[0]["source_pixel_box"][1] * 650 / 2709, 407)
        self.assertGreaterEqual(plans[0]["source_pixel_box"][2] * 400 / 1667, 267)
        self.assertEqual(len(plans[0]["source_word_indices"]), 4)

    def test_dark_columns_expand_to_omitted_axis_pixels_but_stop_before_separate_chart(self):
        doc, page, candidates, _, _ = synthetic_case()
        self.addCleanup(doc.close)
        for x in (201, 212, 223, 320):
            page.insert_text((x, 125), "2023/04", fontsize=6, rotate=90)
        pixmap = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
        regions = axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)
        right = regions[0]["source_pixel_box"][2] * 400 / image.width
        self.assertGreater(right, 220)
        self.assertLess(right, 300)
        self.assertGreater(regions[0]["source_pixel_box"][2], regions[0]["seed_pixel_box"][2])
        self.assertTrue(any(regions[0]["ink_profile"]["dark_counts"]))
        horizontal = {"bbox": [200, 115, 220, 122], "text": "0", "block": 30, "paragraph": 0, "line": 0}
        for value in candidates.values():
            value["words"].append(horizontal); value["text"] += "\n0"
        with self.assertRaisesRegex(axis.RotatedAxisError, '^rotated_axis_not_eligible$'):
            axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)

    def test_chart_baseline_zero_stays_in_original_transcript_and_three_read_numeric_path(self):
        document, page, candidates = chart_boundary_case()
        self.addCleanup(document.close)
        page.insert_text((95, 99), "Caption", fontsize=3)
        caption = {"bbox": [95, 96, 109, 100.2], "text": "Caption", "block": 8, "paragraph": 0, "line": 0}
        for value in candidates.values():
            value["words"].append(copy.deepcopy(caption))
            value["words"].sort(key=lambda w: (w["bbox"][1], w["bbox"][0]))
            value["text"] = "\n".join(w["text"] for w in value["words"])
        candidates["full-page-psm11"]["text"] = axis._region_text(candidates["full-page-psm11"]["words"])[0]
        calls = []
        def reader(image, **options):
            calls.append(options)
            return date_words(image.size) if len(calls) == 2 else [{"bbox": [3, 3, 15, 15], "text": "garbage",
                "block": 0, "paragraph": 0, "line": 0}]
        recovery = axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
            tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS, reader=reader)
        self.assertIsNotNone(recovery)
        region = recovery["proof"]["regions"][0]
        separated = region["top_separation"]
        self.assertGreater(separated["selected_top"], region["seed_pixel_box"][1])
        self.assertIsNotNone(separated["white_gap"])
        zero_index = next(i for i, w in enumerate(candidates["source-flow"]["words"]) if w["text"] == "0")
        self.assertNotIn(zero_index, region["source_word_indices"])
        self.assertNotIn(zero_index, [edit["word_index"] for edit in recovery["proof"]["ledger"]["edits"]])
        self.assertEqual(recovery["primary_text"].split().count("0"), 1)
        caption_index = next(i for i, w in enumerate(candidates["source-flow"]["words"]) if w["text"] == "Caption")
        self.assertNotIn(caption_index, region["source_word_indices"])
        self.assertEqual(recovery["primary_text"].split().count("Caption"), 1)
        engine, numeric_calls = numeric_engine(page, recovery)
        with mock.patch.object(numeric, "_read_tesseract", side_effect=engine):
            audited = numeric.audit_numeric_evidence(page, recovery["primary_text"], language="eng",
                tesseract_command="unused", rotated_axis_proof=recovery["proof"])
        zero = next(r for r in audited["evidence"]["records"] if r["literal"] == "0")
        self.assertEqual(zero["bbox"], candidates["source-flow"]["words"][zero_index]["bbox"])
        self.assertEqual(zero["status"], "verified")
        self.assertEqual(len(zero["reads"]), 3)
        self.assertEqual(numeric_calls, [(450, 3), (600, 6), (600, 11)])
        self.assertTrue(all(r["status"] == "unresolved" and r["bbox"] is None for r in
            audited["evidence"]["records"] if "rotated_axis" in r))
        for field, value in (("row_dark_counts", 1), ("selected_top", True), ("minimum_gap", True)):
            proof = copy.deepcopy(recovery["proof"])
            if isinstance(proof["regions"][0]["top_separation"][field], list):
                proof["regions"][0]["top_separation"][field][0] = value
            else:
                proof["regions"][0]["top_separation"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.replay(page, recovery, proof)

    def test_real_engine_fixture_contains_baseline_gap_and_complete_dates_before_ocr(self):
        """Keep the actual-engine fixture's pixel geometry testable without OCR."""
        document, page, candidates = chart_boundary_case(real_size=True)
        self.addCleanup(document.close)
        pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        region, = axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)
        separation = region["top_separation"]
        self.assertIsNotNone(separation["separator_row"])
        self.assertIsNotNone(separation["white_gap"])
        self.assertGreaterEqual(separation["separator_row"], region["seed_pixel_box"][1])
        self.assertLess(separation["separator_row"], separation["white_gap"][0])
        self.assertLess(separation["white_gap"][0], separation["selected_top"])
        self.assertLess(separation["selected_top"], separation["white_gap"][1])
        zero_index = next(i for i, word in enumerate(candidates["source-flow"]["words"]) if word["text"] == "0")
        self.assertNotIn(zero_index, region["source_word_indices"])
        dates = [word for word in page.get_text("words") if axis.DATE.fullmatch(word[4])]
        self.assertEqual({word[4] for word in dates}, {"2010/01", "2018/07", "2026/07"})
        left, top, right, bottom = region["source_pixel_box"]
        for word in dates:
            with self.subTest(date=word[4]):
                self.assertLess(left, word[0] * image.width / page.rect.width)
                self.assertLess(top, word[1] * image.height / page.rect.height)
                self.assertGreater(right, word[2] * image.width / page.rect.width)
                self.assertGreater(bottom, word[3] * image.height / page.rect.height)

    def test_fractional_horizontal_word_edge_aligns_one_blank_pixel_and_preserves_zero(self):
        document, page, candidates = chart_boundary_case()
        self.addCleanup(document.close)
        pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        original, = axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)
        top = original["source_pixel_box"][1]
        for candidate in candidates.values():
            next(word for word in candidate["words"] if word["text"] == "0")["bbox"][3] = (top + .1373) * 650 / image.height
        calls = []
        def reader(image, **options):
            calls.append(options)
            return date_words(image.size, ("bad", "bad", "bad")) if len(calls) == 1 else date_words(image.size)
        recovery = axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
            tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS, reader=reader)
        self.assertIsNotNone(recovery)
        region = recovery["proof"]["regions"][0]
        self.assertEqual(region["source_pixel_box"][1], top + 1)
        self.assertEqual(region["top_separation"]["selected_top"], top + 1)
        self.assertGreaterEqual(region["top_separation"]["white_gap"][1] - top - 1, 2)
        zero_index = next(i for i, word in enumerate(candidates["source-flow"]["words"]) if word["text"] == "0")
        self.assertNotIn(zero_index, region["source_word_indices"])
        self.assertNotIn(zero_index, [edit["word_index"] for edit in recovery["proof"]["ledger"]["edits"]])
        self.assertEqual(recovery["primary_text"].split().count("0"), 1)
        self.assertEqual(region["source_crop_sha256"], axis._hash(image.crop(tuple(region["source_pixel_box"])).tobytes()))
        engine, numeric_calls = numeric_engine(page, recovery)
        with mock.patch.object(numeric, "_read_tesseract", side_effect=engine):
            audited = numeric.audit_numeric_evidence(page, recovery["primary_text"], language="eng",
                tesseract_command="unused", rotated_axis_proof=recovery["proof"])
        zero = next(row for row in audited["evidence"]["records"] if row["literal"] == "0")
        self.assertEqual(zero["bbox"], [round(value, 4) for value in candidates["source-flow"]["words"][zero_index]["bbox"]])
        self.assertEqual(len(zero["reads"]), 3)
        self.assertEqual(zero["status"], "verified")
        self.assertEqual(numeric_calls, [(450, 3), (600, 6), (600, 11)])
        self.replay(page, recovery)
        changed = copy.deepcopy(recovery["proof"])
        changed["regions"][0]["top_separation"]["selected_top"] -= 1
        with self.assertRaises(ValueError):
            self.replay(page, recovery, changed)
        ink = image.copy()
        ink.putpixel((original["seed_pixel_box"][0] + 10, top), (235, 235, 235))
        with self.assertRaisesRegex(axis.RotatedAxisError, '^rotated_axis_not_eligible$'):
            axis._select_regions(candidates, [400, 650], list(ink.size), source_image=ink)
        for candidate in candidates.values():
            next(word for word in candidate["words"] if word["text"] == "0")["bbox"][3] = (top + 1.01) * 650 / image.height
        with self.assertRaisesRegex(axis.RotatedAxisError, '^rotated_axis_not_eligible$'):
            axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)

    def test_gray_baseline_sparse_antialias_and_unclear_gap_or_axis_crossing(self):
        image = Image.new("RGB", (240, 160), "white")
        draw = ImageDraw.Draw(image)
        draw.line((10, 22, 209, 22), fill=(235, 235, 235))
        draw.rectangle((10, 21, 14, 27), fill="black")
        for x in (40, 90, 140):
            draw.rectangle((x, 38, x + 5, 110), fill="black")
        image.putpixel((80, 32), (235, 235, 235))
        box, proof = axis._separate_chart_top(image, [10, 20, 210, 140], 70, 30)
        self.assertEqual(proof["white_gap"], [28, 38])
        self.assertEqual(box[1], 33)
        self.assertGreaterEqual(38 - box[1], 2)
        crossing, record = axis._separate_chart_top(image, [10, 20, 210, 140], 30, 30)
        self.assertEqual(crossing, [10, 20, 210, 140])
        self.assertIsNone(record["white_gap"])
        short_gap = image.copy()
        for x in (40, 90, 140):
            ImageDraw.Draw(short_gap).rectangle((x, 32, x + 5, 110), fill="black")
        unchanged, record = axis._separate_chart_top(short_gap, [10, 20, 210, 140], 70, 30)
        self.assertEqual(unchanged, [10, 20, 210, 140])
        self.assertIsNone(record["white_gap"])
        no_line = Image.new("RGB", image.size, "white")
        ImageDraw.Draw(no_line).rectangle((40, 27, 45, 110), fill="black")
        unchanged, record = axis._separate_chart_top(no_line, [10, 20, 210, 140], 70, 30)
        self.assertEqual(unchanged, [10, 20, 210, 140])
        self.assertIsNone(record["white_gap"])
        for kind in ("axis-crosses", "body-below", "zero-below"):
            document, page, candidates = chart_boundary_case()
            try:
                word = {"bbox": [100, 99, 104, 120], "text": "2020/01", "block": 30, "paragraph": 0, "line": 0}
                if kind == "body-below": word.update(bbox=[90, 107, 120, 112], text="Body")
                if kind == "zero-below": word.update(bbox=[90, 107, 96, 112], text="0")
                for value in candidates.values():
                    value["words"].append(copy.deepcopy(word)); value["text"] += "\n" + word["text"]
                pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
                image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                with self.subTest(kind=kind), self.assertRaisesRegex(axis.RotatedAxisError, '^rotated_axis_not_eligible$'):
                    axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)
            finally:
                document.close()
        document, page, candidates = chart_boundary_case()
        try:
            pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
            image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            ImageDraw.Draw(image).rectangle((195, 415, 805, 460), fill=(235, 235, 235))
            with self.assertRaisesRegex(axis.RotatedAxisError, '^rotated_axis_not_eligible$'):
                axis._select_regions(candidates, [400, 650], list(image.size), source_image=image)
        finally:
            document.close()

    def test_long_run_seed_planning_bound_precedes_any_recognition(self):
        doc, page, candidates, _, _ = synthetic_case()
        self.addCleanup(doc.close)
        for value in candidates.values():
            for i in range(axis.MAX_SEEDS):
                word = {"bbox": [50, 300, 190, 307], "text": "Z" * 30 + str(i),
                        "block": 100 + i, "paragraph": 0, "line": 0}
                value["words"].append(word)
            value["text"] = "\n".join(w["text"] for w in value["words"])
        candidates["full-page-psm11"]["text"] = axis._region_text(candidates["full-page-psm11"]["words"])[0]
        reader = mock.Mock(side_effect=AssertionError("No recognition"))
        self.assertIsNone(axis.recover_rotated_axes(page, candidates, language="eng", tessdata=None,
            tesseract_command="unused", tesseract_version="5.3.0", traineddata=MODELS, reader=reader))
        reader.assert_not_called()

    def test_image_file_replay_requires_original_hash_and_rejects_missing_proof_members(self):
        doc, page, _, result, _ = synthetic_case()
        self.addCleanup(doc.close)
        pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "original.png"; pix.save(str(path))
            axis.replay_rotated_axis_proof(result["proof"], result["primary_text"],
                input_pixel_sha256=result["proof"]["input_pixel_sha256"], page_size_points=[400.0, 650.0], image_path=path)
            Image.new("RGB", (pix.width, pix.height), "white").save(path)
            with self.assertRaises(ValueError):
                axis.replay_rotated_axis_proof(result["proof"], result["primary_text"],
                    input_pixel_sha256=result["proof"]["input_pixel_sha256"], page_size_points=[400.0, 650.0], image_path=path)
        for key in result["proof"]:
            proof = copy.deepcopy(result["proof"]); proof.pop(key)
            with self.subTest(missing=key), self.assertRaises(ValueError):
                self.replay(page, result, proof)
        with self.assertRaises(ValueError):
            axis.replay_rotated_axis_proof(result["proof"], result["primary_text"],
                input_pixel_sha256=result["proof"]["input_pixel_sha256"], page_size_points=[400.0, 650.0])


class RotatedAxisCloudTests(unittest.TestCase):
    def setUp(self):
        # This actual-engine contract runs on Linux CI only. macOS checks use
        # pure source pixels/mocks and never invoke the user's local OCR.
        required = os.environ.get("REQUIRE_MARKET_VIEWS_OCR_TESTS") == "1"
        if not sys.platform.startswith("linux"):
            if required:
                self.fail("Required rotated-axis OCR acceptance must run in Linux CI")
            self.skipTest("Real rotated-axis OCR is cloud-only")
        self.command = shutil.which("tesseract")
        try:
            self.tessdata = str(Path(os.environ.get("TESSDATA_PREFIX") or fitz.get_tessdata()))
            self.models = [{"language": language, "filename": language + ".traineddata",
                "sha256": hashlib.sha256((Path(self.tessdata) / (language + ".traineddata")).read_bytes()).hexdigest()}
                for language in ("eng", "chi_sim")]
            if not self.command:
                raise ValueError("missing CLI")
        except Exception:
            if required:
                self.fail("Cloud rotated-axis acceptance requires Tesseract plus eng and chi_sim models")
            self.skipTest("Real cloud OCR dependencies unavailable")

    def test_real_tesseract_vertical_year_month_baseline_zero_and_unresolved_axes(self):
        import extract_native_market_sources as native
        document, page, candidates = chart_boundary_case(real_size=True)
        self.addCleanup(document.close)
        recovery = axis.recover_rotated_axes(page, candidates, language="eng+chi_sim", tessdata=self.tessdata,
            tesseract_command=self.command, tesseract_version=native._tesseract_version(self.command, 1),
            traineddata=self.models)
        self.assertIsNotNone(recovery, "The real engine must recover complete date-axis labels")
        selected = recovery["proof"]["regions"][0]
        read = next(r for r in selected["reads"] if r["angle"] == selected["selected_angle"])
        labels = axis._region_text(read["words"])[0].splitlines()
        self.assertGreaterEqual(len(labels), 3)
        self.assertTrue(all(axis.DATE.fullmatch(label) for label in labels))
        self.assertEqual(set(labels), {"2010/01", "2018/07", "2026/07"})
        self.assertIsNotNone(selected["top_separation"]["white_gap"])
        self.assertEqual(recovery["primary_text"].split().count("0"), 1)
        audited = numeric.audit_numeric_evidence(page, recovery["primary_text"], primary_words=recovery["primary_words"],
            language="eng+chi_sim", tessdata=self.tessdata, tesseract_command=self.command,
            rotated_axis_proof=recovery["proof"])
        zero = next(r for r in audited["evidence"]["records"] if r["literal"] == "0")
        self.assertEqual(zero["bbox"], next(w["bbox"] for w in candidates["source-flow"]["words"] if w["text"] == "0"))
        self.assertEqual(len(zero["reads"]), 3)
        axes = [r for r in audited["evidence"]["records"] if "rotated_axis" in r]
        self.assertGreaterEqual(len(axes), 6)
        self.assertTrue(all(r["status"] == "unresolved" and r["bbox"] is None and r["reads"] == [] for r in axes))
        pix = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        numeric.validate_numeric_evidence(audited["safe_text"], audited["evidence"], axis._hash(image.tobytes()),
            source_image=image, rotated_axis_proof=recovery["proof"])


if __name__ == "__main__":
    unittest.main()
