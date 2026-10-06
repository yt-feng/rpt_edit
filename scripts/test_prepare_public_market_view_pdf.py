#!/usr/bin/env python3
"""Regression tests for the public Market Views PDF export."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import IndirectObject
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

    def test_preserves_toc_destinations_and_bookmarks_without_private_ending_objects(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rendered, source, output = (root / name for name in ("rendered.pdf", "private.pdf", "public.pdf"))
            private_identity = "".join(("kc", "desk", ".com"))
            private_sentinel = "PRIVATE_ENDING_ONLY_42"
            document = canvas.Canvas(str(rendered))
            document.bookmarkPage("toc")
            document.addOutlineEntry("Contents", "toc", level=0)
            document.drawString(72, 760, "Contents: research on page 2")
            document.linkRect("Research TOC link", "research", (72, 700, 300, 720), relative=0)
            document.linkRect("Private ending link", "private-ending", (72, 660, 300, 680), relative=0)
            document.showPage()
            document.bookmarkPage("research")
            document.addOutlineEntry("Cross-report research", "research", level=0)
            document.bookmarkPage("macro")
            document.addOutlineEntry("Macro versus Equity", "macro", level=1)
            document.drawString(72, 760, "Research compares macro demand and equity earnings.")
            document.showPage()
            document.bookmarkPage("private-ending")
            document.addOutlineEntry(private_identity + " private ending", "private-ending", level=0)
            document.drawString(72, 760, ENDING_PAGE_MARKER)
            document.drawString(72, 730, private_identity + " " + private_sentinel)
            document.showPage()
            document.save()

            # Include named destinations as well as ReportLab's direct TOC
            # destinations: both must be filtered to selected public pages.
            original = PdfWriter()
            original.append(rendered)
            original.add_named_destination("research-body", 1)
            original.add_named_destination(private_identity + "-ending", 2)
            original.write(source)

            prepare_public_copy(source, output)

            public = PdfReader(output)
            self.assertEqual(len(public.pages), 2)
            outline = public.outline
            self.assertEqual([item.title for item in outline if not isinstance(item, list)],
                             ["Contents", "Cross-report research"])
            self.assertEqual(outline[2][0].title, "Macro versus Equity")
            self.assertEqual(public.get_destination_page_number(outline[1]), 1)
            self.assertEqual(public.get_destination_page_number(outline[2][0]), 1)
            self.assertEqual(set(public.named_destinations), {"research-body"})
            self.assertEqual(public.get_destination_page_number(public.named_destinations["research-body"]), 1)
            links = [reference.get_object() for reference in public.pages[0]["/Annots"]]
            self.assertEqual(len(links), 1)
            self.assertEqual(links[0]["/Dest"][0], public.pages[1].indirect_reference)
            self.assertEqual(links[0]["/Contents"], "Research TOC link")

            # Check every serialized object, including decoded content streams,
            # so a detached private page cannot survive outside the page tree.
            serialized = [output.read_bytes()]
            page_objects = 0
            for generation, objects in public.xref.items():
                if generation == 65535:
                    continue
                for number in objects:
                    if number == 0:
                        continue
                    value = public.get_object(IndirectObject(number, generation, public))
                    serialized.append(str(value).encode())
                    if hasattr(value, "get_data"):
                        serialized.append(value.get_data())
                    if hasattr(value, "get") and value.get("/Type") == "/Page":
                        page_objects += 1
            self.assertEqual(page_objects, 2)
            for marker in (private_identity, private_sentinel, ENDING_PAGE_MARKER):
                self.assertNotIn(marker.encode(), b"\n".join(serialized))

    def test_rejects_private_identity_in_imported_public_navigation(self) -> None:
        for navigation_kind in ("outline", "named_destination"):
            with self.subTest(navigation_kind=navigation_kind), tempfile.TemporaryDirectory() as temp_dir:
                root = Path(temp_dir)
                rendered, source, output = (root / name for name in ("rendered.pdf", "private.pdf", "public.pdf"))
                self.make_pdf(rendered, ["Public research body", ENDING_PAGE_MARKER])
                writer = PdfWriter()
                writer.append(rendered)
                private_identity = "".join(("kc", "desk", ".com"))
                if navigation_kind == "outline":
                    writer.add_outline_item(private_identity, 0)
                else:
                    writer.add_named_destination(private_identity, 0)
                writer.write(source)
                with self.assertRaisesRegex(ValueError, "Private identity remains.*navigation"):
                    prepare_public_copy(source, output)
                self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
