#!/usr/bin/env python3
"""Exercise the actual local-PDF fallback and its transferred source contract."""
from __future__ import annotations

import copy
import hashlib
import json
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
            # Distinct metadata prevents identical report contents from being
            # silently counted as separate originals in multi-report fixtures.
            with fitz.open(path) as document:
                document.set_metadata({"title": name})
                document.saveIncr()
            rows.append({"process_local_path": f"/runner/selected/{name}",
                         "content_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        self.manifest.write_text(json.dumps(rows), encoding="utf-8")
        return rows

    def extract(self, expected: int = 1) -> dict:
        # A network attempt would fail this realistic extraction fixture.
        with patch("socket.create_connection", side_effect=AssertionError("No network permitted")):
            return native.extract_sources(self.input, self.manifest, self.output, expected)

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

    def test_manifest_requires_verified_unique_complete_bindings(self) -> None:
        original = self.select("one.pdf")
        for mutation in ("missing_hash", "bad_hash", "duplicate_name", "duplicate_bytes", "count"):
            rows = copy.deepcopy(original)
            if mutation == "missing_hash":
                rows[0].pop("content_sha256")
            elif mutation == "bad_hash":
                rows[0]["content_sha256"] = "invalid"
            elif mutation == "duplicate_name":
                rows.append(copy.deepcopy(rows[0]))
            elif mutation == "duplicate_bytes":
                rows.append({**rows[0], "process_local_path": "/selected/other.pdf"})
            self.manifest.write_text(json.dumps(rows), encoding="utf-8")
            expected = 2 if mutation in {"duplicate_name", "duplicate_bytes", "count"} else 1
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
                with self.assertRaises(native.SourceValidationError):
                    self.extract(2)
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
                report["pages"][0]["native_text_sha256"] = "a" * 64
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
