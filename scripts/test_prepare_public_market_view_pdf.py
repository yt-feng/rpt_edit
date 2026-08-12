#!/usr/bin/env python3
"""Regression tests for the public Market Views PDF export."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
from reportlab.pdfgen import canvas

from prepare_public_market_view_pdf import ENDING_PAGE_MARKER, prepare_public_copy


class PreparePublicMarketViewPdfTests(unittest.TestCase):
    def make_pdf(self, path: Path, pages: list[str]) -> None:
        document = canvas.Canvas(str(path))
        for text in pages:
            document.drawString(72, 760, text)
            document.showPage()
        document.save()

    def make_pdf_with_body_image(self, path: Path, image_path: Path) -> None:
        Image.new("RGB", (900, 520), (20, 80, 140)).save(image_path)
        document = canvas.Canvas(str(path))
        document.drawString(72, 760, "Market Views body chart")
        document.drawImage(str(image_path), 72, 320, width=450, height=260)
        document.showPage()
        document.drawString(72, 760, ENDING_PAGE_MARKER)
        document.showPage()
        document.save()

    def test_removes_only_dedicated_ending_page(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "private.pdf"
            output = root / "public.pdf"
            self.make_pdf(source, ["Market Views body", "Disclaimer", ENDING_PAGE_MARKER])

            result = prepare_public_copy(source, output)

            self.assertEqual(result["page_count"], 2)
            private_document = PdfReader(source)
            self.assertEqual(len(private_document.pages), 3)
            public_document = PdfReader(output)
            self.assertEqual(len(public_document.pages), 2)
            text = "\n".join(page.extract_text() or "" for page in public_document.pages)
            self.assertNotIn("portal.example.invalid", text)

    def test_rejects_an_unexpected_final_page(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "private.pdf"
            self.make_pdf(source, ["Market Views body", "ordinary final page"])
            with self.assertRaisesRegex(ValueError, "not the expected private ending page"):
                prepare_public_copy(source, root / "public.pdf")

    def test_rejects_private_identity_outside_the_ending_page(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "private.pdf"
            private_domain = "".join(("kc", "desk", ".com"))
            self.make_pdf(source, [private_domain + " body", ENDING_PAGE_MARKER])
            with self.assertRaisesRegex(ValueError, "Private identity remains"):
                prepare_public_copy(source, root / "public.pdf")

    def test_preserves_mineru_chart_images_on_public_body_pages(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "private.pdf"
            output = root / "public.pdf"
            self.make_pdf_with_body_image(source, root / "chart.png")

            prepare_public_copy(source, output)

            public_document = PdfReader(output)
            self.assertEqual(len(public_document.pages), 1)
            self.assertGreaterEqual(len(public_document.pages[0].images), 1)


if __name__ == "__main__":
    unittest.main()
