#!/usr/bin/env python3
"""Regression tests for MinerU figures in Market Views inputs."""

from __future__ import annotations

import tempfile
import hashlib
import json
import unittest
from pathlib import Path

from PIL import Image

from build_market_views_pdf import copy_figures, extract_exhibit_figures, handoff_source_images


def make_image(path: Path, color: tuple[int, int, int] = (20, 80, 140)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (900, 520), color).save(path)


class MarketViewsFigureTests(unittest.TestCase):
    def test_native_original_chart_caption_and_page_survive_receipt_transfer(self) -> None:
        import fitz
        from extract_native_market_sources import extract_sources
        from test_extract_native_market_sources import make_pdf
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            originals = root / "originals"
            originals.mkdir()
            pdf = originals / "bank-report.pdf"
            make_pdf(pdf, chart=True)
            # Chart captions were previously extracted then mislabeled as
            # MinerU images because they did not match the exhibit regex.
            with fitz.open(pdf) as document:
                page = document[1]
                page.add_redact_annot(fitz.Rect(40, 30, 550, 60))
                page.apply_redactions()
                page.insert_text((45, 50), "Chart 1: Revenue and margin trends", fontsize=12)
                document.saveIncr()
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps([{"process_local_path": str(pdf),
                                             "content_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest()}]))
            sources = root / "sources"
            receipt = extract_sources(originals, manifest, sources, 1)
            report = sources / receipt["reports"][0]["directory"]
            figures = extract_exhibit_figures(report, "R001", "Revenue outlook", 5)
            self.assertEqual(len(figures), 1)
            self.assertEqual(figures[0]["context"], "Chart 1: Revenue and margin trends")
            self.assertEqual(figures[0]["source_page"], 2)
            self.assertEqual(figures[0]["selection_source"], "native_pdf_page")
            self.assertNotIn("MinerU", figures[0]["label"])
            copied = copy_figures(figures, root / "figures", 0)
            self.assertEqual(len(copied), 1)
            self.assertTrue((root / copied[0]["latex_path"]).is_file())

    def test_recovers_selected_mineru_images_from_private_handoff_assets(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir) / "report"
            report.mkdir()
            (report / "source_mineru.md").write_text(
                "## Figure 1: Revenue growth\n![](images/original-hash.jpg)\n",
                encoding="utf-8",
            )
            make_image(report / "assets" / "source_image_02.jpg", (40, 90, 150))
            make_image(report / "assets" / "source_image_01.jpg", (20, 70, 130))

            assets = handoff_source_images(report)
            figures = extract_exhibit_figures(report, "R001", "JPM：Revenue outlook", 5)

            self.assertEqual([path.name for path in assets], ["source_image_01.jpg", "source_image_02.jpg"])
            self.assertEqual(len(figures), 2)
            self.assertTrue(all(item["selection_source"] == "private_handoff_source_image" for item in figures))
            self.assertEqual([item["label"] for item in figures], ["MinerU 图表 1", "MinerU 图表 2"])
            self.assertTrue(all("/" not in item["context"] for item in figures))

    def test_deduplicates_original_mineru_image_and_handoff_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir) / "report"
            original = report / "mineru_raw" / "images" / "chart.jpg"
            copied = report / "assets" / "source_image_01.jpg"
            make_image(original)
            copied.parent.mkdir(parents=True, exist_ok=True)
            copied.write_bytes(original.read_bytes())
            (report / "source_mineru.md").write_text(
                "## Figure 1: Revenue growth across regions\n![](images/chart.jpg)\n",
                encoding="utf-8",
            )

            figures = extract_exhibit_figures(report, "R001", "Revenue outlook", 5)

            self.assertEqual(len(figures), 1)
            self.assertEqual(figures[0]["label"], "Figure 1")

    def test_handoff_recovery_honors_per_report_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir) / "report"
            report.mkdir()
            (report / "source_mineru.md").write_text("# Parsed report\n", encoding="utf-8")
            for index in range(1, 5):
                make_image(report / "assets" / f"source_image_{index:02d}.png", (index * 20, 80, 120))

            figures = extract_exhibit_figures(report, "R001", "Market outlook", 2)

            self.assertEqual(len(figures), 2)

    def test_copy_figures_converts_bmp_to_pdf_safe_png(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source_image_01.bmp"
            make_image(source)
            copied = copy_figures(
                [{
                    "report_id": "R001",
                    "source_path": str(source),
                    "label": "MinerU 图表 1",
                    "context": "Market outlook",
                    "figure_type": "source_exhibit",
                }],
                root / "figures",
                0,
            )

            self.assertEqual(len(copied), 1)
            self.assertTrue(copied[0]["latex_path"].endswith(".png"))
            self.assertTrue((root / copied[0]["latex_path"]).is_file())


if __name__ == "__main__":
    unittest.main()
