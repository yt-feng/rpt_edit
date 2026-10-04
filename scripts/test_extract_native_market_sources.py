#!/usr/bin/env python3
"""Exercise the actual local-PDF fallback and its transferred source contract."""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import fitz

import extract_native_market_sources as native


REPORT_TEXT = (
    "Investment research examines revenue, margins, financing costs and market demand. "
    "The base case assumes steady industrial production, while a slower recovery changes earnings. "
    "The source data covers companies and regions, with explicit dates and assumptions. "
    "Portfolio observations compare valuation and cash flow trends across reporting periods. "
    "This paragraph is native selectable report text and retains the original evidence. "
) * 3
try:
    DEFAULT_TESSDATA = fitz.get_tessdata()
except RuntimeError:
    DEFAULT_TESSDATA = "/tmp/market-views-tessdata"
TESSDATA = Path(os.getenv("TESSDATA_PREFIX", DEFAULT_TESSDATA))
HAS_OCR_DATA = all((TESSDATA / f"{language}.traineddata").is_file()
                   for language in native.OCR_LANGUAGES.split("+"))


def setUpModule() -> None:
    # A developer without local language data may run native contract checks.
    # The cloud release job must prove the real OCR fixtures ran, not turn a
    # missing dependency into a successful job with skipped acceptance tests.
    if os.getenv("REQUIRE_MARKET_VIEWS_OCR_TESTS") == "1" and (not HAS_OCR_DATA or not shutil.which("tesseract")):
        raise RuntimeError("Cloud OCR acceptance requires Tesseract plus eng and chi_sim language data")


def make_pdf(path: Path, *, chart: bool = False, scanned_page: bool = False, short: bool = False) -> None:
    with fitz.open() as document:
        page = document.new_page(width=595, height=842)
        page.insert_textbox(fitz.Rect(45, 50, 550, 750),
                            "Too little text" if short else REPORT_TEXT, fontsize=10)
        if chart:
            page = document.new_page(width=595, height=842)
            page.insert_text((45, 50), "Exhibit 1: Revenue and margin trends", fontsize=12)
            page.insert_textbox(fitz.Rect(45, 70, 550, 300), REPORT_TEXT, fontsize=10)
            page.draw_rect(fitz.Rect(70, 400, 140, 650), color=(0, 0, 1), fill=(0, 0, 1))
            page.draw_rect(fitz.Rect(180, 450, 250, 650), color=(1, 0, 0), fill=(1, 0, 0))
        if scanned_page:
            page = document.new_page(width=595, height=842)
            # A real raster-only report page can look fully readable to a
            # person while providing no native text to the fallback.
            with fitz.open() as scanned:
                raster_page = scanned.new_page(width=595, height=842)
                raster_page.insert_textbox(fitz.Rect(45, 50, 550, 750), REPORT_TEXT, fontsize=10)
                image = raster_page.get_pixmap()
                page.insert_image(page.rect, pixmap=image)
        document.save(path)


class NativeMarketSourcesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.input = self.root / "originals"
        self.input.mkdir()
        self.manifest = self.root / "manifest.json"
        self.output = self.root / "sources"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def select(self, *names: str, chart: bool = False) -> list[dict[str, str]]:
        rows = []
        for index, name in enumerate(names):
            path = self.input / name
            make_pdf(path, chart=chart and index == 0)
            # Most fixtures represent distinct sources; duplicate byte aliases
            # have separate tests proving that every original binding remains.
            with fitz.open(path) as document:
                document.set_metadata({"title": name})
                document.saveIncr()
            rows.append({"process_local_path": f"/runner/selected/{name}",
                         "content_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        self.manifest.write_text(json.dumps(rows), encoding="utf-8")
        return rows

    def extract(self, expected: int = 1, *, enable_ocr: bool = False, source_context: dict | None = None) -> dict:
        # A network attempt would fail this realistic extraction fixture.
        with patch("socket.create_connection", side_effect=AssertionError("No network permitted")):
            return native.extract_sources(self.input, self.manifest, self.output, expected,
                                          enable_ocr=enable_ocr, source_context=source_context)

    def append_sparse_page(self, name: str, text: str, *, chinese: bool = False) -> None:
        path = self.input / name
        changed = self.root / "with-sparse-page.pdf"
        with fitz.open(path) as document:
            page = document.new_page(width=792, height=612)
            page.insert_textbox(fitz.Rect(150, 230, 650, 450), text, fontsize=26,
                                fontname="china-s" if chinese else "helv", align=1)
            document.save(changed)
        path.write_bytes(changed.read_bytes())
        self.update_hash(name)

    def audited_sparse_fixture(self, page, source_name, number):
        """Mock engine reads only; bind actual PDF geometry, pixels and receipt."""
        import ocr_numeric_evidence as numeric
        primary = page.get_text("text", sort=True).strip()
        words = page.get_text("words", sort=True)
        second = [{"bbox": [value * 450 / 72 for value in word[:4]], "text": word[4],
                   "block": word[5], "line": word[6]} for word in words]
        crops = {index: [{"method": f"source-crop-psm-{psm}", "dpi": 600,
                          "literal": mention["literal"], "field_count": 1,
                          "input_pixel_sha256": "b" * 64} for psm in (6, 11)]
                 for index, mention in enumerate(numeric.numeric_mentions(primary))}
        with patch.object(numeric, "_read_tesseract", return_value=second), patch.object(numeric, "_crop_reads", return_value=crops):
            audit = numeric.audit_numeric_evidence(page, primary, primary_words=words,
                                                  language=native.OCR_LANGUAGES, tesseract_command="fixture-engine")
        return audit["safe_text"], {"engine": "tesseract-via-pymupdf", "pymupdf_version": fitz.VersionBind,
                                    "languages": native.OCR_LANGUAGES, "dpi": native.PAGE_DPI, "full_page": True,
                                    "traineddata": [{"language": language, "filename": f"{language}.traineddata", "sha256": "a" * 64}
                                                    for language in native.OCR_LANGUAGES.split("+")],
                                    "numeric_evidence": audit["evidence"]}

    def test_readability_rejects_opaque_native_streams_even_above_the_old_threshold(self) -> None:
        opaque = "f6BvX2LkZ9QwR4N8jH3PsY7MdW5GtV1C0UaEoIiSxAzTnRpK9mH6L4zBq"
        self.assertGreater(native.meaningful_characters(opaque), native.MIN_PAGE_CHARACTERS)
        cases = (opaque, opaque + "\n" + opaque, "1234567890" * 10,
                 "qzxv qzxv qzxv qzxv qzxv qzxv qzxv qzxv qzxv qzxv")
        for text in cases:
            with self.subTest(shape=native.page_readability(text)), self.assertRaisesRegex(native.SourceValidationError, "unreadable"):
                native.require_readable_page(text, "encoded.pdf", 1)
        self.assertEqual(native.page_readability(opaque)["reason"], "opaque_ascii_runs")

    def test_readability_accepts_real_prose_chinese_and_short_financial_table_labels(self) -> None:
        examples = {
            "English": REPORT_TEXT,
            "Chinese": "市场观点：本月收入增长，利润率有所改善。未来仍需关注需求变化及融资成本。" * 3,
            "Table": "Revenue EBITDA Margin\n2024 2025 2026\n4.8 5.2 6.4\n18.5 19.3 20.1\n11.2 12.3 14.5",
            "Acronyms": "EPS ROE EBITDA FY2024 FY2025 FY2026\n4.8 5.2 6.4 18.5 19.3 20.1 11.2 12.3 14.5",
            "Macro table": "GDP CPI PMI\n4.8 5.2 6.4\n18.5 19.3 20.1\n11.2 12.3 14.5 3.5",
            "Chinese table": "收入 利润\n4.8 5.2 6.4\n18.5 19.3 20.1\n11.2 12.3 14.5 3.5",
            "URL footer": REPORT_TEXT + "\nhttps://research.example/" + "a" * 100,
        }
        for kind, text in examples.items():
            with self.subTest(kind=kind):
                self.assertTrue(native.page_readability(text)["accepted"])
                self.assertEqual(native.require_readable_page(text, "readable.pdf", 1), native.meaningful_characters(text))

    def test_pending_markers_cannot_fabricate_recognized_language(self) -> None:
        text = " ".join(f"[数值待核对:n{index:04d}]" for index in range(1, 20))
        self.assertGreater(native.meaningful_characters(text), 100)
        self.assertEqual(native.page_readability(text)["characters"], 0)
        with self.assertRaisesRegex(native.SourceValidationError, "insufficient readable"):
            native.require_readable_page(text, "unreadable.pdf", 1)

    def test_sparse_structural_ocr_is_explicit_and_preserves_regular_readability(self) -> None:
        for text, structure in (("Disclosure Appendix\nResearch\n49", "sparse_ocr_english"),
                                ("Research\nJordan Evans", "sparse_ocr_english"),
                                ("Section\nTaylor Morgan", "sparse_ocr_english"),
                                ("信息披露附录\n二零二六年十月", "sparse_ocr_chinese"),
                                ("风险披露\n20261004", "sparse_ocr_chinese")):
            with self.subTest(text=text):
                self.assertFalse(native.page_readability(text)["accepted"])
                with self.assertRaises(native.SourceValidationError):
                    native.require_readable_page(text, "divider.pdf", 1)
                evidence = native.page_readability(text, allow_sparse_ocr=True)
                self.assertTrue(evidence["accepted"])
                self.assertEqual(evidence["subtype"], native.SPARSE_OCR_SUBTYPE)
                self.assertEqual(evidence["structure"], structure)
        self.assertEqual(native.page_readability(REPORT_TEXT),
                         native.page_readability(REPORT_TEXT, allow_sparse_ocr=True),
                         "Previously accepted native/OCR receipts must retain exact evidence")

    def test_sparse_ocr_rejects_noise_empty_opaque_and_annotation_only_pages(self) -> None:
        cases = ("", "Disclosure", "Disclosure Appendix", "qxzv rtyk jhgf 0123",
                 "的" * 12, "甲" * 12, "甲乙" * 6, "的的的的的的的的的的甲乙",
                 "1234 5678 9012 3456", "Disclosure Appendix Research\ufffd",
                 "Disclosure Appendix Research\ue000",
                 "f6BvX2LkZ9QwR4N8jH3PsY7MdW5GtV1C0UaEoIiSxAzTnRpK9mH6L4zBq",
                 "[数值待核对:n0001] [漏识数值待核对:s0001]",
                 "Appendix Research [数值待核对:n0001] [数值待核对:n0002]")
        for text in cases:
            with self.subTest(text=text), self.assertRaises(native.SourceValidationError):
                native.require_readable_page(text, "noise.pdf", 1, allow_sparse_ocr=True)
        self.assertEqual(native.page_readability("风险披露 [数值待核对:n0001]", allow_sparse_ocr=True)["characters"], 4)

    def test_sparse_native_divider_still_requires_ocr_and_transferred_consumer_rechecks_subtype(self) -> None:
        self.select("divider.pdf")
        self.append_sparse_page("divider.pdf", "Disclosure Appendix\nResearch\n49")
        with patch.object(native, "_ocr_page", side_effect=AssertionError("Disabled OCR must not be called")):
            with self.assertRaisesRegex(native.SourceValidationError, "OCR is disabled"):
                self.extract()
        with patch.object(native, "_ocr_page", side_effect=self.audited_sparse_fixture) as ocr:
            receipt = self.extract(enable_ocr=True)
        self.assertEqual(ocr.call_count, 1)
        report = receipt["reports"][0]
        page = report["pages"][1]
        self.assertEqual(page["extraction_method"], "ocr")
        self.assertFalse(page["native_readability"]["accepted"])
        self.assertFalse(page["text_readability"]["accepted"])
        self.assertEqual(page["recognized_readability"]["subtype"], native.SPARSE_OCR_SUBTYPE)
        self.assertEqual(page["ocr"]["numeric_evidence"]["source_num_count"], 1)
        with fitz.open(self.input / "divider.pdf") as source:
            expected = source[1].get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
            self.assertEqual(page["original_page"]["pixel_sha256"], hashlib.sha256(expected.samples).hexdigest())
        shutil.rmtree(self.input)
        with patch.object(native, "_ocr_page", side_effect=AssertionError("Consumer must not rerun OCR")):
            self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)
        receipt_path = self.output / native.RECEIPT_NAME
        for mutation in ("subtype", "minimum", "native", "numeric_missing"):
            tampered = copy.deepcopy(receipt)
            page = tampered["reports"][0]["pages"][1]
            if mutation == "subtype":
                page["recognized_readability"].pop("subtype")
            elif mutation == "minimum":
                page["recognized_readability"]["minimum_characters"] = 1
            elif mutation == "native":
                page["extraction_method"] = "native"
                page["ocr"] = None
            else:
                page["ocr"].pop("numeric_evidence")
            receipt_path.write_text(json.dumps(tampered))
            with self.subTest(mutation=mutation), self.assertRaises(native.SourceValidationError):
                native.validate_sources(self.output, self.manifest, 1)

    def test_sparse_structural_ocr_does_not_relax_the_complete_report_floor(self) -> None:
        self.select("short-report.pdf")
        path = self.input / "short-report.pdf"
        path.unlink()
        with fitz.open() as document:
            page = document.new_page()
            page.insert_text((45, 50), "Disclosure Appendix Research", fontsize=20)
            document.save(path)
        self.update_hash("short-report.pdf")
        with patch.object(native, "_ocr_page", side_effect=self.audited_sparse_fixture):
            with self.assertRaisesRegex(native.SourceValidationError, "insufficient text for a report summary"):
                self.extract(enable_ocr=True)
        self.assertFalse(self.output.exists())

    def test_ocr_readability_rejection_is_not_relabelled_as_missing_language_models(self) -> None:
        models = self.root / "fixture-tessdata"
        models.mkdir()
        for language in native.OCR_LANGUAGES.split("+"):
            (models / f"{language}.traineddata").write_bytes(b"fixture model identity")
        with fitz.open() as document:
            page = document.new_page()
            page.insert_text((45, 50), "Too short", fontsize=20)
            with patch.object(fitz, "get_tessdata", return_value=str(models)), \
                    patch.object(fitz.Page, "get_textpage_ocr", return_value=page.get_textpage()):
                with self.assertRaisesRegex(native.SourceValidationError, "insufficient readable page text") as failure:
                    native._ocr_page(page, "unreadable.pdf", 1)
                self.assertNotIn("Tesseract data", str(failure.exception))
            with patch.object(fitz, "get_tessdata", return_value=str(models)), \
                    patch.object(fitz.Page, "get_textpage_ocr", side_effect=RuntimeError("engine failed")):
                with self.assertRaisesRegex(native.SourceValidationError, "Runner OCR failed") as failure:
                    native._ocr_page(page, "unreadable.pdf", 1)
                self.assertIsInstance(failure.exception.__cause__, RuntimeError)
            readable = document.new_page()
            readable.insert_text((45, 50), "Disclosure Appendix Research", fontsize=20)
            with patch.object(fitz, "get_tessdata", return_value=str(models)), \
                    patch.object(fitz.Page, "get_textpage_ocr", return_value=readable.get_textpage()), \
                    patch("ocr_numeric_evidence.audit_numeric_evidence",
                          side_effect=native.SourceValidationError("source numeric positions differ")):
                with self.assertRaisesRegex(native.SourceValidationError, "source numeric positions differ") as failure:
                    native._ocr_page(readable, "unreadable.pdf", 2)
                self.assertNotIn("Tesseract data", str(failure.exception))

    def test_sparse_scanned_table_keeps_complete_source_when_one_numeric_field_is_masked(self) -> None:
        import ocr_numeric_evidence as numeric
        self.select("sparse-table.pdf")
        path = self.input / "sparse-table.pdf"
        replacement = self.root / "sparse-table-with-scan.pdf"
        with fitz.open() as vector:
            table = vector.new_page(width=320, height=130)
            table.insert_text((15, 25), "GDP CPI PMI", fontsize=12)
            for row, values in enumerate((("4.8", "5.2", "6.4", "18.5"), ("19.3", "20.1", "11.2", "12.3"))):
                for column, value in enumerate(values):
                    table.insert_text((15 + 70 * column, 55 + 30 * row), value, fontsize=12)
            primary = table.get_text("text", sort=True).strip()
            words = table.get_text("words", sort=True)
            image = table.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
        with fitz.open(path) as document:
            page = document.new_page(width=320, height=130)
            page.insert_image(page.rect, pixmap=image)
            document.save(replacement)
        path.write_bytes(replacement.read_bytes())
        self.update_hash("sparse-table.pdf")
        self.assertTrue(native.page_readability(primary)["accepted"])

        def audit_fixture(page, source_name, number):
            second = [{"bbox": [value * 450 / 72 for value in word[:4]], "text": word[4],
                       "block": word[5], "line": word[6]} for word in words]
            mentions = numeric.numeric_mentions(primary)
            crops = {}
            for index, mention in enumerate(mentions):
                crops[index] = [{"method": f"source-crop-psm-{psm}", "dpi": 600,
                                 "literal": "48" if index == 0 and psm == 11 else mention["literal"],
                                 "field_count": 1, "input_pixel_sha256": "b" * 64} for psm in (6, 11)]
            with patch.object(numeric, "_read_tesseract", return_value=second), patch.object(numeric, "_crop_reads", return_value=crops):
                audit = numeric.audit_numeric_evidence(page, primary, primary_words=words, language=native.OCR_LANGUAGES,
                                                      tesseract_command="fixture-engine")
            return audit["safe_text"], {"engine": "tesseract-via-pymupdf", "pymupdf_version": fitz.VersionBind,
                                        "languages": native.OCR_LANGUAGES, "dpi": native.PAGE_DPI, "full_page": True,
                                        "traineddata": [{"language": language, "filename": f"{language}.traineddata", "sha256": "a" * 64}
                                                        for language in native.OCR_LANGUAGES.split("+")],
                                        "numeric_evidence": audit["evidence"]}

        with patch.object(native, "_ocr_page", side_effect=audit_fixture):
            receipt = self.extract(enable_ocr=True)
        page = receipt["reports"][0]["pages"][1]
        self.assertEqual(page["ocr"]["numeric_evidence"]["unresolved_count"], 1)
        self.assertTrue(page["recognized_readability"]["accepted"])
        self.assertFalse(page["text_readability"]["accepted"], "Masking must not need to invent new page language")
        self.assertEqual(page["recognized_text_characters"], 30)
        self.assertEqual(receipt["reports"][0]["pages_covered"], [1, 2])
        shutil.rmtree(self.input)
        with patch.object(native, "_ocr_page", side_effect=AssertionError("Transferred consumer must not perform OCR")):
            self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)

    def test_masked_ocr_figure_index_retains_the_source_image_through_consumer_and_asset_selection(self) -> None:
        import ocr_numeric_evidence as numeric
        from build_market_views_pdf import extract_exhibit_figures
        self.select("masked-figure.pdf")
        path = self.input / "masked-figure.pdf"
        replacement = self.root / "masked-figure-with-scan.pdf"
        with fitz.open() as vector:
            figure = vector.new_page(width=595, height=842)
            figure.insert_text((45, 45), "Figure 1: Revenue and margin trends", fontsize=12)
            figure.insert_textbox(fitz.Rect(45, 70, 550, 300), REPORT_TEXT, fontsize=10)
            figure.draw_rect(fitz.Rect(70, 400, 140, 650), color=(0, 0, 1), fill=(0, 0, 1))
            figure.draw_rect(fitz.Rect(180, 450, 250, 650), color=(1, 0, 0), fill=(1, 0, 0))
            primary = figure.get_text("text", sort=True).strip()
            words = figure.get_text("words", sort=True)
            image = figure.get_pixmap(dpi=150, colorspace=fitz.csRGB, alpha=False)
        with fitz.open(path) as document:
            page = document.new_page(width=595, height=842)
            page.insert_image(page.rect, pixmap=image)
            document.save(replacement)
        path.write_bytes(replacement.read_bytes())
        self.update_hash("masked-figure.pdf")

        def audit_fixture(page, source_name, number):
            second = [{"bbox": [value * 450 / 72 for value in word[:4]], "text": word[4],
                       "block": word[5], "line": word[6]} for word in words]
            crops = {0: [{"method": f"source-crop-psm-{psm}", "dpi": 600,
                          "literal": None if psm == 11 else "1", "field_count": 0 if psm == 11 else 1,
                          "input_pixel_sha256": "b" * 64} for psm in (6, 11)]}
            with patch.object(numeric, "_read_tesseract", return_value=second), patch.object(numeric, "_crop_reads", return_value=crops):
                audit = numeric.audit_numeric_evidence(page, primary, primary_words=words, language=native.OCR_LANGUAGES,
                                                      tesseract_command="fixture-engine")
            return audit["safe_text"], {"engine": "tesseract-via-pymupdf", "pymupdf_version": fitz.VersionBind,
                                        "languages": native.OCR_LANGUAGES, "dpi": native.PAGE_DPI, "full_page": True,
                                        "traineddata": [{"language": language, "filename": f"{language}.traineddata", "sha256": "a" * 64}
                                                        for language in native.OCR_LANGUAGES.split("+")],
                                        "numeric_evidence": audit["evidence"]}

        with patch.object(native, "_ocr_page", side_effect=audit_fixture):
            receipt = self.extract(enable_ocr=True)
        report = receipt["reports"][0]
        page = report["pages"][1]
        self.assertEqual(page["ocr"]["numeric_evidence"]["unresolved_count"], 1)
        self.assertEqual(len(report["assets"]), 1)
        self.assertEqual(report["assets"][0]["description"], "Figure [数值待核对:n0001]: Revenue and margin trends")
        with fitz.open(path) as original:
            expected_pixels = original[1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
            expected_pixel_sha = hashlib.sha256(expected_pixels.samples).hexdigest()
        shutil.rmtree(self.input)
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)
        selected = extract_exhibit_figures(self.output / report["directory"], "report", "Source", 0)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["source_page"], 2)
        self.assertEqual(Path(selected[0]["source_path"]).read_bytes(), (self.output / report["assets"][0]["path"]).read_bytes())
        pixmap = fitz.Pixmap(selected[0]["source_path"])
        self.assertEqual(hashlib.sha256(pixmap.samples).hexdigest(), expected_pixel_sha)
        self.assertGreater(len(set(pixmap.samples)), 2, "The retained plot must contain the actual original color bars")

    def test_masked_caption_indices_accept_only_the_numeric_audit_marker_format(self) -> None:
        for caption in ("Figure [数值待核对:n0001]: Revenue trends", "Figure [数值待核对:n0001]A: Revenue trends",
                        "Chart [漏识数值待核对:s0001]: Margin trends",
                        "图[数值待核对:n0002] 收入变化"):
            self.assertIsNotNone(native.EXHIBIT_CAPTION.fullmatch(caption))
        for caption in ("Figure [pending1]: Revenue trends", "Figure [数值待核对:z0001]: Revenue trends",
                        "Figure [数值待核对:n1]: Revenue trends"):
            self.assertIsNone(native.EXHIBIT_CAPTION.fullmatch(caption))

    def test_unreadable_native_page_requires_explicit_ocr_and_preserves_prior_output(self) -> None:
        self.select("encoded.pdf")
        path = self.input / "encoded.pdf"
        replacement = self.root / "encoded-replacement.pdf"
        with fitz.open(path) as document:
            page = document.new_page()
            page.insert_textbox(fitz.Rect(40, 40, 550, 750), "K4mN8rW2yP6vT9hB1jZ5sQ7dL3xA0cEoUfIgVkRzMnBqYwPsJtHkC9G6")
            document.save(replacement)
        path.write_bytes(replacement.read_bytes())
        self.update_hash("encoded.pdf")
        with patch.object(native, "_ocr_page", side_effect=AssertionError("Default must not invoke OCR")):
            with self.assertRaisesRegex(native.SourceValidationError, "OCR is disabled"):
                self.extract()
        self.assertFalse(self.output.exists())
        self.assertEqual(list(self.root.glob(".sources-native-*")), [])

    def test_cloud_context_matches_exact_date_producer_commit_and_original_run(self) -> None:
        self.select("one.pdf")
        context = {"date_folder": "261003", "producer_run_id": "37214015946",
                   "execution_sha": "a" * 40, "original_source_run_id": "37159099752"}
        receipt = self.extract(source_context=context)
        self.assertEqual(receipt["source_context"], context)
        shutil.rmtree(self.input)
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1,
                                                expected_source_context=context), receipt)
        for field, value in (("date_folder", "261002"), ("producer_run_id", "37214015947"),
                             ("execution_sha", "b" * 40), ("original_source_run_id", "37159099753")):
            with self.subTest(field=field), self.assertRaisesRegex(native.SourceValidationError, "execution context"):
                native.validate_sources(self.output, self.manifest, 1,
                                        expected_source_context={**context, field: value})

    def test_cloud_context_is_optional_for_local_contracts_but_not_a_required_cloud_consumer(self) -> None:
        self.select("one.pdf")
        self.extract()
        context = {"date_folder": "261003", "producer_run_id": "37214015946",
                   "execution_sha": "a" * 40, "original_source_run_id": ""}
        with self.assertRaisesRegex(native.SourceValidationError, "execution context"):
            native.validate_sources(self.output, self.manifest, 1, expected_source_context=context)
        receipt_path = self.output / native.RECEIPT_NAME
        receipt = json.loads(receipt_path.read_bytes())
        for bad in ({**context, "date_folder": "261032"}, {**context, "producer_run_id": "0"},
                    {**context, "execution_sha": "a" * 39}, {**context, "extra": "not-authorized"}):
            receipt["source_context"] = bad
            receipt_path.write_text(json.dumps(receipt))
            with self.subTest(context=bad), self.assertRaises(native.SourceValidationError):
                native.validate_sources(self.output, self.manifest, 1)

    def test_page_readability_provenance_is_rechecked_by_transferred_consumer(self) -> None:
        self.select("one.pdf")
        receipt = self.extract()
        receipt["reports"][0]["pages"][0]["native_readability"]["accepted"] = False
        (self.output / native.RECEIPT_NAME).write_text(json.dumps(receipt))
        with self.assertRaisesRegex(native.SourceValidationError, "readability evidence"):
            native.validate_sources(self.output, self.manifest, 1)

    def test_cli_source_context_is_all_or_nothing_and_direct_dropbox_source_is_explicit(self) -> None:
        self.select("one.pdf")
        arguments = ["native", "extract", "--input-dir", str(self.input), "--manifest", str(self.manifest),
                     "--output-dir", str(self.output), "--expected-reports", "1"]
        with patch.object(sys, "argv", [*arguments, "--date-folder", "261003"]):
            with self.assertRaises(SystemExit) as stopped:
                native.main()
        self.assertEqual(stopped.exception.code, 2)
        self.assertFalse(self.output.exists())
        with patch.object(sys, "argv", [*arguments, "--date-folder", "261003", "--producer-run-id", "37214015946",
                                       "--execution-sha", "a" * 40, "--original-source-run-id", ""]):
            self.assertEqual(native.main(), 0)
        receipt = native.validate_sources(self.output, self.manifest, 1)
        self.assertEqual(receipt["source_context"]["original_source_run_id"], "")
        self.assertEqual(receipt["source_context"]["date_folder"], "261003")

    def test_string_ocr_flag_cannot_be_used_as_an_implicit_truthy_activation(self) -> None:
        self.select("one.pdf")
        with self.assertRaisesRegex(native.SourceValidationError, "explicit boolean"):
            self.extract(enable_ocr="false")
        self.assertFalse(self.output.exists())

    def test_complete_batch_retains_every_page_and_only_original_exhibit_pages(self) -> None:
        self.select("bank-a.pdf", "bank-b.pdf", chart=True)
        receipt = self.extract(2)
        self.assertEqual(receipt["report_count"], 2)
        self.assertEqual([row["page_count"] for row in receipt["reports"]], [2, 1])
        first = receipt["reports"][0]
        self.assertEqual(first["pages_covered"], [1, 2])
        self.assertEqual(len(first["assets"]), 1)
        asset = first["assets"][0]
        self.assertEqual(asset["source_page"], 2)
        self.assertEqual(asset["description"], "Exhibit 1: Revenue and margin trends")
        pixmap = fitz.Pixmap(str(self.output / asset["path"]))
        self.assertGreater(pixmap.width, 500)
        text = (self.output / first["markdown"]["path"]).read_text(encoding="utf-8")
        self.assertIn("## 原报告第 1 页", text)
        self.assertIn("## 原报告第 2 页", text)
        self.assertIn("Investment research examines", text)
        self.assertIn("assets/source_image_1.png", text)
        self.assertEqual(receipt["reports"][1]["assets"], [])
        self.assertEqual(receipt["source_method"], "original-pdf")
        self.assertEqual(receipt["schema"], 2)
        self.assertIsNone(first["duplicate_of"])
        self.assertEqual(first["pages"][0]["extraction_method"], "native")
        self.assertNotIn("original_page", first["pages"][0])
        self.assertIn("original_page", first["pages"][1])
        with patch.object(native, "_ocr_page", side_effect=AssertionError("Native pages need no OCR")):
            native.validate_sources(self.output, self.manifest, 2)

    def test_transferred_batch_validates_without_original_pdfs(self) -> None:
        self.select("one.pdf", chart=True)
        receipt = self.extract()
        shutil.rmtree(self.input)
        self.manifest.unlink()
        self.assertEqual(native.validate_sources(self.output, self.output / native.MANIFEST_NAME, 1), receipt)
        with patch.object(sys, "argv", ["native", "validate", "--output-dir", str(self.output),
                                       "--manifest", str(self.output / native.MANIFEST_NAME), "--expected-reports", "1"]):
            self.assertEqual(native.main(), 0)

    def test_missing_extra_duplicate_and_hash_changed_originals_are_rejected(self) -> None:
        for case in ("missing", "extra", "duplicate", "hash"):
            with self.subTest(case=case):
                if self.input.exists():
                    shutil.rmtree(self.input)
                self.input.mkdir()
                self.select("one.pdf")
                if case == "missing":
                    (self.input / "one.pdf").unlink()
                elif case == "extra":
                    make_pdf(self.input / "extra.pdf")
                elif case == "duplicate":
                    nested = self.input / "nested"
                    nested.mkdir()
                    shutil.copyfile(self.input / "one.pdf", nested / "one.pdf")
                else:
                    (self.input / "one.pdf").write_bytes((self.input / "one.pdf").read_bytes() + b"changed")
                with self.assertRaises(native.SourceValidationError):
                    self.extract()
                self.assertFalse(self.output.exists())

    def test_manifest_requires_verified_unique_names_and_complete_bindings(self) -> None:
        original = self.select("one.pdf")
        for mutation in ("missing_hash", "bad_hash", "duplicate_name", "count"):
            rows = copy.deepcopy(original)
            if mutation == "missing_hash":
                rows[0].pop("content_sha256")
            elif mutation == "bad_hash":
                rows[0]["content_sha256"] = "invalid"
            elif mutation == "duplicate_name":
                rows.append(copy.deepcopy(rows[0]))
            self.manifest.write_text(json.dumps(rows), encoding="utf-8")
            expected = 2 if mutation in {"duplicate_name", "count"} else 1
            with self.subTest(mutation=mutation), self.assertRaises(native.SourceValidationError):
                self.extract(expected)
            self.assertFalse(self.output.exists())

    def test_scanned_page_corruption_and_short_text_reject_whole_batch(self) -> None:
        for case in ("scan", "damaged", "short"):
            with self.subTest(case=case):
                self.select("readable.pdf", "unsupported.pdf")
                path = self.input / "unsupported.pdf"
                if case == "damaged":
                    path.write_bytes(b"%PDF-1.7\nbroken original")
                else:
                    path.unlink()
                    make_pdf(path, scanned_page=case == "scan", short=case == "short")
                rows = json.loads(self.manifest.read_text())
                rows[1]["content_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
                self.manifest.write_text(json.dumps(rows), encoding="utf-8")
                with patch.object(native, "_ocr_page", side_effect=native.SourceValidationError("OCR cannot read this page")) as ocr:
                    with self.assertRaises(native.SourceValidationError):
                        self.extract(2, enable_ocr=True)
                    self.assertEqual(ocr.call_count, 0 if case == "damaged" else 1)
                self.assertFalse(self.output.exists(), "Even the earlier readable report must not become a published batch")
                self.assertEqual(list(self.root.glob(".sources-native-*")), [])

    def test_readable_but_summary_too_short_and_garbled_pages_are_rejected(self) -> None:
        self.select("one.pdf")
        path = self.input / "one.pdf"
        path.unlink()
        with fitz.open() as document:
            page = document.new_page()
            page.insert_textbox(fitz.Rect(40, 40, 550, 750), "Native words present but less than six hundred characters. " * 3)
            document.save(path)
        rows = json.loads(self.manifest.read_text())
        rows[0]["content_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(rows), encoding="utf-8")
        with self.assertRaisesRegex(native.SourceValidationError, "insufficient text for a report summary"):
            self.extract()
        with self.assertRaisesRegex(native.SourceValidationError, "unreadable"):
            native.require_readable_page("readable words " * 20 + "\ufffd" * 30, "one.pdf", 1)

    def test_encrypted_original_is_rejected_without_password_or_network(self) -> None:
        self.select("one.pdf")
        path = self.input / "one.pdf"
        encrypted = self.root / "encrypted.pdf"
        with fitz.open(path) as document:
            document.save(encrypted, encryption=fitz.PDF_ENCRYPT_AES_256,
                          owner_pw="owner", user_pw="reader")
        path.write_bytes(encrypted.read_bytes())
        rows = json.loads(self.manifest.read_text())
        rows[0]["content_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(rows), encoding="utf-8")
        with self.assertRaisesRegex(native.SourceValidationError, "Encrypted"):
            self.extract()
        self.assertFalse(self.output.exists())

    def test_receipt_rejects_transferred_corruption_missing_pages_and_wrong_manifest(self) -> None:
        self.select("one.pdf", chart=True)
        self.extract()
        receipt_path = self.output / native.RECEIPT_NAME
        original_receipt = receipt_path.read_bytes()
        receipt = json.loads(original_receipt)
        markdown_path = self.output / receipt["reports"][0]["markdown"]["path"]
        original_markdown = markdown_path.read_bytes()
        markdown_path.write_bytes(original_markdown + b"tampered")
        with self.assertRaisesRegex(native.SourceValidationError, "checksum mismatch"):
            native.validate_sources(self.output, self.manifest, 1)
        markdown_path.write_bytes(original_markdown)
        receipt["reports"][0]["pages_covered"] = [1]
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        with self.assertRaisesRegex(native.SourceValidationError, "page coverage"):
            native.validate_sources(self.output, self.manifest, 1)
        receipt_path.write_bytes(original_receipt)
        rows = json.loads(self.manifest.read_text())
        rows[0]["content_sha256"] = "a" * 64
        self.manifest.write_text(json.dumps(rows), encoding="utf-8")
        with self.assertRaisesRegex(native.SourceValidationError, "selected manifest"):
            native.validate_sources(self.output, self.manifest, 1)

    def test_validation_checks_exact_original_text_hashes_and_asset_page_bindings(self) -> None:
        self.select("one.pdf", chart=True)
        self.extract()
        receipt_path = self.output / native.RECEIPT_NAME
        original = receipt_path.read_bytes()
        for mutation in ("page_text", "asset_page", "asset_missing"):
            receipt = json.loads(original)
            report = receipt["reports"][0]
            if mutation == "page_text":
                report["pages"][0]["text_sha256"] = "a" * 64
            elif mutation == "asset_page":
                report["assets"][0]["source_page"] = 1
            else:
                (self.output / report["assets"][0]["path"]).unlink()
            receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
            with self.subTest(mutation=mutation), self.assertRaises(native.SourceValidationError):
                native.validate_sources(self.output, self.manifest, 1)

    def test_unreceipted_files_symlinks_and_unsafe_paths_cannot_enter_consumer(self) -> None:
        self.select("one.pdf")
        self.extract()
        extra = self.output / "unexpected.md"
        extra.write_text("unreceipted report")
        with self.assertRaisesRegex(native.SourceValidationError, "inventory"):
            native.validate_sources(self.output, self.manifest, 1)
        extra.unlink()
        extra.symlink_to(self.manifest)
        with self.assertRaisesRegex(native.SourceValidationError, "symbolic"):
            native.validate_sources(self.output, self.manifest, 1)
        extra.unlink()
        receipt_path = self.output / native.RECEIPT_NAME
        receipt = json.loads(receipt_path.read_text())
        receipt["reports"][0]["markdown"]["path"] = "../manifest.json"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        with self.assertRaisesRegex(native.SourceValidationError, "unsafe"):
            native.validate_sources(self.output, self.manifest, 1)

    def test_existing_output_is_preserved_and_no_complete_receipt_is_fabricated(self) -> None:
        self.select("one.pdf")
        self.output.mkdir()
        old = self.output / "keep.txt"
        old.write_text("existing output")
        with self.assertRaisesRegex(native.SourceValidationError, "already exists"):
            self.extract()
        self.assertEqual(old.read_text(), "existing output")
        self.assertFalse((self.output / native.RECEIPT_NAME).exists())

    def test_source_changes_after_one_report_are_detected_before_batch_receipt(self) -> None:
        self.select("first.pdf", "second.pdf")
        original_extract = native._extract_report

        def mutate_after_materialization(*args, **kwargs):
            report = original_extract(*args, **kwargs)
            if report["source_pdf"] == "second.pdf":
                first = self.input / "first.pdf"
                first.write_bytes(first.read_bytes() + b"source changed after first report")
            return report

        with patch.object(native, "_extract_report", side_effect=mutate_after_materialization):
            with self.assertRaisesRegex(native.SourceValidationError, "batch bytes changed"):
                self.extract(2)
        self.assertFalse(self.output.exists())

    def update_hash(self, name: str) -> None:
        rows = json.loads(self.manifest.read_text())
        for row in rows:
            if Path(row["process_local_path"]).name == name:
                row["content_sha256"] = hashlib.sha256((self.input / name).read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(rows), encoding="utf-8")

    @unittest.skipUnless(HAS_OCR_DATA, "Local eng and chi_sim Tesseract language data are unavailable")
    def test_actual_cloud_ocr_short_english_divider_retains_full_page_and_numeric_proof(self) -> None:
        self.select("short-divider.pdf")
        self.append_sparse_page("short-divider.pdf", "Disclosure Appendix\nResearch\n49")
        with patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            receipt = self.extract(enable_ocr=True)
        report = receipt["reports"][0]
        page = report["pages"][1]
        self.assertEqual(page["extraction_method"], "ocr")
        self.assertEqual(page["recognized_readability"]["subtype"], native.SPARSE_OCR_SUBTYPE)
        self.assertEqual(page["recognized_readability"]["structure"], "sparse_ocr_english")
        self.assertLess(page["recognized_text_characters"], native.MIN_PAGE_CHARACTERS)
        self.assertIn("Disclosure", page["ocr"]["numeric_evidence"]["primary_text"])
        self.assertEqual(page["ocr"]["input_pixel_sha256"], page["original_page"]["pixel_sha256"])
        self.assertEqual(page["original_page"]["dpi"], 300)
        self.assertGreaterEqual(page["ocr"]["numeric_evidence"]["source_num_count"], 1)
        self.assertGreaterEqual(report["recognized_text_characters"], native.MIN_REPORT_CHARACTERS)
        shutil.rmtree(self.input)
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)

    @unittest.skipUnless(HAS_OCR_DATA, "Local eng and chi_sim Tesseract language data are unavailable")
    def test_actual_cloud_ocr_short_chinese_divider_retains_recognized_language(self) -> None:
        self.select("short-chinese-divider.pdf")
        self.append_sparse_page("short-chinese-divider.pdf", "信息披露附录\n二零二六年十月", chinese=True)
        with patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            receipt = self.extract(enable_ocr=True)
        page = receipt["reports"][0]["pages"][1]
        self.assertEqual(page["extraction_method"], "ocr")
        self.assertEqual(page["recognized_readability"]["subtype"], native.SPARSE_OCR_SUBTYPE)
        self.assertEqual(page["recognized_readability"]["structure"], "sparse_ocr_chinese")
        self.assertGreaterEqual(page["recognized_readability"]["han_characters"], 4)
        self.assertLess(page["recognized_text_characters"], native.MIN_PAGE_CHARACTERS)
        shutil.rmtree(self.input)
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)

    @unittest.skipUnless(HAS_OCR_DATA, "Local eng and chi_sim Tesseract language data are unavailable")
    def test_actual_full_page_ocr_retains_image_provenance_and_validates_without_originals(self) -> None:
        self.select("scanned.pdf")
        path = self.input / "scanned.pdf"
        path.unlink()
        make_pdf(path, scanned_page=True)
        self.update_hash("scanned.pdf")
        with patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            receipt = self.extract(enable_ocr=True)
        report = receipt["reports"][0]
        page = report["pages"][1]
        self.assertEqual(page["extraction_method"], "ocr")
        self.assertEqual(page["native_text"], "")
        self.assertEqual(page["native_text_characters"], 0)
        self.assertGreater(page["text_characters"], 600)
        self.assertEqual(report["ocr_page_count"], 1)
        self.assertEqual(page["ocr"]["languages"], "eng+chi_sim")
        self.assertTrue(page["ocr"]["full_page"])
        self.assertEqual(page["ocr"]["input_pixel_sha256"], page["original_page"]["pixel_sha256"])
        self.assertEqual(report["assets"], [], "A scanned text page is not a chart")
        markdown = (self.output / report["markdown"]["path"]).read_text()
        self.assertIn("Investment research examines", markdown)
        self.assertIn("pages/source_page_0002.png", markdown)
        shutil.rmtree(self.input)
        with patch.object(native, "_ocr_page", side_effect=AssertionError("Consumer must not rerun OCR")):
            self.assertEqual(native.validate_sources(self.output, self.output / native.MANIFEST_NAME, 1), receipt)

    @unittest.skipUnless(HAS_OCR_DATA, "Local eng and chi_sim Tesseract language data are unavailable")
    def test_actual_ocr_replaces_an_opaque_hidden_text_layer_with_visible_report_prose(self) -> None:
        self.select("hidden-layer.pdf")
        path = self.input / "hidden-layer.pdf"
        changed = self.root / "hidden-layer-replacement.pdf"
        opaque = "K4mN8rW2yP6vT9hB1jZ5sQ7dL3xA0cEoUfIgVkRzMnBqYwPsJtHkC9G6"
        with fitz.open(path) as document, fitz.open() as scanned:
            raster_page = scanned.new_page(width=595, height=842)
            raster_page.insert_textbox(fitz.Rect(45, 50, 550, 750), REPORT_TEXT, fontsize=10)
            page = document.new_page(width=595, height=842)
            page.insert_image(page.rect, pixmap=raster_page.get_pixmap(dpi=150))
            page.insert_text((45, 40), opaque, fontsize=8, render_mode=3)
            document.save(changed)
        path.write_bytes(changed.read_bytes())
        self.update_hash("hidden-layer.pdf")
        with patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            receipt = self.extract(enable_ocr=True)
        page = receipt["reports"][0]["pages"][1]
        self.assertEqual(page["native_text"], opaque)
        self.assertEqual(page["native_readability"]["reason"], "opaque_ascii_runs")
        self.assertEqual(page["extraction_method"], "ocr")
        markdown = (self.output / receipt["reports"][0]["markdown"]["path"]).read_text()
        self.assertIn("Investment research examines", markdown)
        self.assertNotIn(opaque, markdown)
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)

    def test_provably_white_page_is_preserved_without_fabricated_text_or_ocr(self) -> None:
        self.select("blank.pdf")
        path = self.input / "blank.pdf"
        changed = self.root / "with-blank.pdf"
        with fitz.open(path) as document:
            document.new_page()
            document.save(changed)
        path.write_bytes(changed.read_bytes())
        self.update_hash("blank.pdf")
        with patch.object(native, "_ocr_page", side_effect=AssertionError("White pixels do not need OCR")):
            receipt = self.extract()
        report = receipt["reports"][0]
        page = report["pages"][1]
        self.assertEqual(page["extraction_method"], "blank")
        self.assertEqual(page["text_characters"], 0)
        self.assertEqual(page["markdown_text_begin"], page["markdown_text_end"])
        self.assertEqual(page["text_sha256"], hashlib.sha256(b"").hexdigest())
        self.assertEqual(page["original_page"]["white_sample_count"], page["original_page"]["sample_count"])
        self.assertEqual(report["blank_page_count"], 1)
        self.assertEqual(report["assets"], [])
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)

    def test_nonwhite_page_with_failed_or_empty_ocr_cannot_claim_blank(self) -> None:
        self.select("unreadable.pdf")
        path = self.input / "unreadable.pdf"
        changed = self.root / "nonwhite.pdf"
        with fitz.open(path) as document:
            page = document.new_page()
            page.draw_rect(fitz.Rect(60, 100, 300, 400), fill=(0, 0, 0))
            document.save(changed)
        path.write_bytes(changed.read_bytes())
        self.update_hash("unreadable.pdf")
        for effect in (native.SourceValidationError("OCR failed"), ("", {}), ("Too short", {})):
            kwargs = {"side_effect": effect} if isinstance(effect, Exception) else {"return_value": effect}
            with self.subTest(effect=str(effect)), patch.object(native, "_ocr_page", **kwargs) as ocr:
                with self.assertRaises(native.SourceValidationError):
                    self.extract(enable_ocr=True)
                self.assertEqual(ocr.call_count, 1)
                self.assertFalse(self.output.exists())

    def test_duplicate_aliases_keep_all_originals_and_canonical_extraction(self) -> None:
        rows = self.select("canonical.pdf", chart=True)
        shutil.copyfile(self.input / "canonical.pdf", self.input / "alias.pdf")
        rows.append({**rows[0], "process_local_path": "/selected/alias.pdf"})
        self.manifest.write_text(json.dumps(rows))
        with patch.object(native, "_extract_report", wraps=native._extract_report) as extraction:
            receipt = self.extract(2)
        self.assertEqual(extraction.call_count, 1)
        self.assertEqual(receipt["report_count"], 2)
        self.assertEqual(receipt["unique_content_count"], 1)
        first, alias = receipt["reports"]
        self.assertEqual(alias["duplicate_of"], first["directory"])
        self.assertEqual(alias["source_pdf"], "alias.pdf")
        self.assertEqual(alias["markdown"]["sha256"], first["markdown"]["sha256"])
        self.assertTrue((self.output / alias["markdown"]["path"]).is_file())
        self.assertEqual(native.validate_sources(self.output, self.manifest, 2), receipt)

    def test_duplicate_alias_missing_original_or_wrong_bytes_rejects_complete_batch(self) -> None:
        rows = self.select("canonical.pdf")
        rows.append({**rows[0], "process_local_path": "/selected/alias.pdf"})
        self.manifest.write_text(json.dumps(rows))
        with self.assertRaisesRegex(native.SourceValidationError, "inventory"):
            self.extract(2)
        make_pdf(self.input / "alias.pdf", short=True)
        with self.assertRaisesRegex(native.SourceValidationError, "hash mismatch"):
            self.extract(2)
        self.assertFalse(self.output.exists())

    def test_receipt_rejects_wrong_duplicate_target_count_and_missing_alias(self) -> None:
        rows = self.select("canonical.pdf")
        shutil.copyfile(self.input / "canonical.pdf", self.input / "alias.pdf")
        rows.append({**rows[0], "process_local_path": "/selected/alias.pdf"})
        self.manifest.write_text(json.dumps(rows))
        self.extract(2)
        receipt_path = self.output / native.RECEIPT_NAME
        original = receipt_path.read_bytes()
        for mutation in ("target", "count", "alias"):
            receipt = json.loads(original)
            if mutation == "target":
                receipt["reports"][1]["duplicate_of"] = None
            elif mutation == "count":
                receipt["unique_content_count"] = 2
            else:
                receipt["reports"].pop()
            receipt_path.write_text(json.dumps(receipt))
            with self.subTest(mutation=mutation), self.assertRaises(native.SourceValidationError):
                native.validate_sources(self.output, self.manifest, 2)

    @unittest.skipUnless(HAS_OCR_DATA, "Local eng and chi_sim Tesseract language data are unavailable")
    def test_ocr_provenance_pixels_text_and_language_models_cannot_be_forged(self) -> None:
        self.select("scanned.pdf")
        path = self.input / "scanned.pdf"
        path.unlink()
        make_pdf(path, scanned_page=True)
        self.update_hash("scanned.pdf")
        with patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}):
            self.extract(enable_ocr=True)
        receipt_path = self.output / native.RECEIPT_NAME
        original = receipt_path.read_bytes()
        for mutation in ("engine", "pixels", "model", "text", "method", "numeric_missing", "numeric_pixels"):
            receipt = json.loads(original)
            page = receipt["reports"][0]["pages"][1]
            if mutation == "engine":
                page["ocr"]["engine"] = "unknown"
            elif mutation == "pixels":
                page["original_page"]["pixel_sha256"] = "a" * 64
            elif mutation == "model":
                page["ocr"]["traineddata"] = []
            elif mutation == "text":
                page["text_sha256"] = "a" * 64
            elif mutation == "method":
                page["extraction_method"] = "native"
            elif mutation == "numeric_missing":
                page["ocr"].pop("numeric_evidence")
            else:
                page["ocr"]["numeric_evidence"]["input_pixel_sha256"] = "a" * 64
            receipt_path.write_text(json.dumps(receipt))
            with self.subTest(mutation=mutation), self.assertRaises(native.SourceValidationError):
                native.validate_sources(self.output, self.manifest, 1)

    def test_schema_one_existing_native_receipt_remains_valid(self) -> None:
        self.select("native.pdf")
        receipt = self.extract()
        receipt = {key: receipt[key] for key in ("schema", "source_method", "complete", "expected_reports", "report_count", "manifest_sha256", "manifest_file", "reports")}
        receipt.update(schema=1, source_method="native-pdf")
        report = receipt["reports"][0]
        report = {key: report[key] for key in ("source_pdf", "content_sha256", "directory", "source_method", "page_count", "pages_covered", "native_text_characters", "pages", "markdown", "status", "assets")}
        receipt["reports"][0] = report
        report["source_method"] = "native-pdf"
        report["pages"] = [{key: page[key] for key in ("page", "native_text_characters", "native_text_sha256", "markdown_text_begin", "markdown_text_end")}
                           for page in report["pages"]]
        status_path = self.output / report["status"]["path"]
        status = json.loads(status_path.read_bytes())
        status = {key: status[key] for key in ("source_method", "source_pdf", "content_sha256", "source_markdown", "page_count", "pages_covered", "native_text_characters", "images")}
        status["source_method"] = "native-pdf"
        status_path.write_text(json.dumps(status))
        report["status"] = native.file_record(status_path, self.output)
        (self.output / native.RECEIPT_NAME).write_text(json.dumps(receipt))
        self.assertEqual(native.validate_sources(self.output, self.manifest, 1), receipt)

    def test_blank_image_pixel_evidence_and_whole_blank_report_are_rejected(self) -> None:
        self.select("blank.pdf")
        path = self.input / "blank.pdf"
        changed = self.root / "white-pages.pdf"
        with fitz.open(path) as document:
            document.new_page()
            document.save(changed)
        path.write_bytes(changed.read_bytes())
        self.update_hash("blank.pdf")
        receipt = self.extract()
        page = receipt["reports"][0]["pages"][1]
        image_path = self.output / page["original_page"]["path"]
        with fitz.open() as document:
            original = document.new_page()
            original.draw_rect(original.rect, fill=(0, 0, 0))
            pixmap = original.get_pixmap(dpi=native.PAGE_DPI, colorspace=fitz.csRGB, alpha=False)
            pixmap.save(str(image_path))
            page["original_page"].update({**native.file_record(image_path, self.output), **native._pixel_record(pixmap)})
        (self.output / native.RECEIPT_NAME).write_text(json.dumps(receipt))
        with self.assertRaisesRegex(native.SourceValidationError, "provably white"):
            native.validate_sources(self.output, self.manifest, 1)
        shutil.rmtree(self.output)
        with fitz.open() as document:
            document.new_page()
            document.save(path)
        self.update_hash("blank.pdf")
        with self.assertRaisesRegex(native.SourceValidationError, "insufficient text for a report summary"):
            self.extract()
        self.assertFalse(self.output.exists())

    @unittest.skipUnless(HAS_OCR_DATA, "Local eng and chi_sim Tesseract language data are unavailable")
    def test_duplicate_scanned_alias_reuses_one_ocr_and_requires_both_originals(self) -> None:
        self.select("canonical.pdf")
        path = self.input / "canonical.pdf"
        path.unlink()
        make_pdf(path, scanned_page=True)
        self.update_hash("canonical.pdf")
        rows = json.loads(self.manifest.read_text())
        shutil.copyfile(path, self.input / "alias.pdf")
        rows.append({**rows[0], "process_local_path": "/selected/alias.pdf"})
        self.manifest.write_text(json.dumps(rows))
        with patch.dict(os.environ, {"TESSDATA_PREFIX": str(TESSDATA)}), patch.object(native, "_ocr_page", wraps=native._ocr_page) as ocr:
            receipt = self.extract(2, enable_ocr=True)
        self.assertEqual(ocr.call_count, 1)
        self.assertEqual(receipt["unique_content_count"], 1)
        self.assertEqual([report["ocr_page_count"] for report in receipt["reports"]], [1, 1])
        self.assertEqual(native.validate_sources(self.output, self.manifest, 2), receipt)

    def test_schema_one_cannot_reinterpret_duplicate_bytes_without_alias_contract(self) -> None:
        rows = self.select("canonical.pdf")
        shutil.copyfile(self.input / "canonical.pdf", self.input / "alias.pdf")
        rows.append({**rows[0], "process_local_path": "/selected/alias.pdf"})
        self.manifest.write_text(json.dumps(rows))
        receipt = self.extract(2)
        receipt.update(schema=1, source_method="native-pdf")
        (self.output / native.RECEIPT_NAME).write_text(json.dumps(receipt))
        with self.assertRaisesRegex(native.SourceValidationError, "Schema 1 cannot represent duplicate PDF contents"):
            native.validate_sources(self.output, self.manifest, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
