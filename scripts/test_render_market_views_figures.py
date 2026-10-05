#!/usr/bin/env python3
"""Regression tests for writing selected MinerU figures into the PDF body."""

from __future__ import annotations

import json
import hashlib
import re
import tempfile
import unittest
from pathlib import Path

from PIL import Image
import fitz

from render_market_views_reportlab_pdf import build_pdf, clean_text


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def make_image(path: Path, color: tuple[int, int, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (900, 520), color).save(path)


class RenderMarketViewsFigureTests(unittest.TestCase):
    def make_summary(self, root: Path, *, broken_figure: bool = False) -> tuple[Path, Path]:
        summary_dir = root / "market_view_summaries" / "260812"
        summary_dir.mkdir(parents=True)
        make_image(root / "prompts" / "zsxq_img.jpg", (10, 30, 60))
        figure_path = summary_dir / "figures" / "fig_001.png"
        figure_path.parent.mkdir()
        if broken_figure:
            figure_path.write_text("not an image", encoding="utf-8")
        else:
            make_image(figure_path, (30, 90, 150))
        write_json(summary_dir / "report_inputs.json", [{
            "id": "R001",
            "title": "JPM：Revenue outlook",
            "source_group": "bank_research",
            "source_label": "投行/券商",
            "institution_name": "JPM",
            "digest": "Revenue growth accelerated.",
            "extract": "Revenue growth accelerated.",
        }])
        write_json(summary_dir / "figure_candidates.json", [{
            "figure_id": "F001",
            "report_id": "R001",
            "report_title": "JPM：Revenue outlook",
            "label": "MinerU 图表 1",
            "context": "JPM：Revenue outlook｜原始报告图表",
            "figure_type": "source_exhibit",
            "latex_path": "figures/fig_001.png",
        }])
        write_json(summary_dir / "market_views_structured.json", {
            "title": "Market Views",
            "subtitle": "Daily roundup",
            "executive_summary": ["Revenue growth accelerated."],
            "bank_roundup": {
                "title": "全球投行叙事汇编",
                "summary": "One report.",
                "sections": [{
                    "heading": "Technology",
                    "thesis": "Revenue growth accelerated.",
                    "consensus": ["Growth accelerated."],
                    "divergences": [],
                    "bank_views": [{
                        "bank": "JPM",
                        "view": "Revenue growth accelerated.",
                        "data_points": [],
                        "marginal_change": "",
                        "report_ids": ["R001"],
                    }],
                    "data_points": [],
                    "figure_ids": ["F001"],
                    "references": ["R001"],
                }],
            },
            "supporting_roundups": [],
            "closing": "",
        })
        return summary_dir, summary_dir / "market_views_260812.pdf"

    def test_writes_render_stats_for_mineru_figure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            summary_dir, output = self.make_summary(Path(temp_dir))

            build_pdf(summary_dir, output)

            stats = json.loads((summary_dir / "market_views_render_stats.json").read_text(encoding="utf-8"))
            self.assertEqual(stats["figure_candidate_count"], 1)
            self.assertEqual(stats["selected_figure_count"], 1)
            self.assertEqual(stats["rendered_figure_count"], 1)
            self.assertEqual(stats["rendered_figure_ids"], ["F001"])
            self.assertGreater(output.stat().st_size, 1024)

    def test_rendered_pdf_retains_original_file_coverage_without_duplicate_summaries(self) -> None:
        from pypdf import PdfReader
        with tempfile.TemporaryDirectory() as temp_dir:
            summary_dir, output = self.make_summary(Path(temp_dir))
            inputs = json.loads((summary_dir / "report_inputs.json").read_text())
            inputs[0]["source_aliases"] = [
                {"source_pdf": "alias-a.pdf", "content_sha256": "a" * 64, "path": "source/alias-a"},
                {"source_pdf": "alias-b.pdf", "content_sha256": "a" * 64, "path": "source/alias-b"},
            ]
            write_json(summary_dir / "report_inputs.json", inputs)
            build_pdf(summary_dir, output)
            text = "\n".join(page.extract_text() for page in PdfReader(output).pages)
            self.assertIn("原文件共 3 份", text)
            self.assertIn("覆盖 1 份独立研究内容", text)
            self.assertIn("2 份同内容原文件保留来源绑定", text)
            stats = json.loads((summary_dir / "market_views_render_stats.json").read_text())
            self.assertEqual(stats["rendered_figure_count"], 1)

    def test_rejects_selected_figure_that_cannot_be_rendered(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            summary_dir, output = self.make_summary(Path(temp_dir), broken_figure=True)

            with self.assertRaisesRegex(RuntimeError, "not rendered"):
                build_pdf(summary_dir, output)

    def test_pending_number_display_accepts_only_complete_producer_markers(self) -> None:
        from build_market_views_pdf import latex_escape
        # :04d is a minimum width, including supplemental IDs above 9999.
        known = ("[数值待核对:n0001]", "[漏识数值待核对:s0001]", "[漏识数值待核对:s10000]")
        for escape in (clean_text, latex_escape):
            for marker in known:
                with self.subTest(escape=escape.__name__, marker=marker):
                    self.assertEqual(escape("12" + marker + "34"), "12（该数值待核对）34")
            for unknown in ("[数值待核对:n12]", "[数值待核对:p2n3]", "[数值待核对:arbitrary]",
                            "[数值待核对:s0001]", "[漏识数值待核对:n0001]", "[数值待核对:n0001",
                            "[数值待核对:n0001 trailing]", "n0001", "[数值待核对:n０００１]"):
                with self.subTest(escape=escape.__name__, unknown=unknown):
                    self.assertEqual(escape(unknown), unknown)

    def test_pdf_and_latex_show_pending_numbers_without_internal_ids_or_evidence_mutation(self) -> None:
        from build_market_views_pdf import render_latex
        with tempfile.TemporaryDirectory() as temp_dir:
            summary_dir, output = self.make_summary(Path(temp_dir))
            summary_path = summary_dir / "market_views_structured.json"
            figure_path = summary_dir / "figure_candidates.json"
            inputs_path = summary_dir / "report_inputs.json"
            summary = json.loads(summary_path.read_text())
            summary["title"] = "Market Views [数值待核对:n0001]"
            section = summary["bank_roundup"]["sections"][0]
            section["bank_views"][0]["view"] = "字段[数值待核对:n0002]尚待核对；已确认数值222%、203.46。"
            section["bank_views"][0]["data_points"] = ["日期2026-09-28；补充字段[漏识数值待核对:s0001]。"]
            figures = json.loads(figure_path.read_text())
            figures[0]["context"] = "Exhibit [数值待核对:n0003]；原页数字保留。"
            inputs = json.loads(inputs_path.read_text())
            inputs[0]["digest"] = "Input evidence [数值待核对:n0002]"
            inputs[0]["has_pending_numeric_values"] = True
            write_json(summary_path, summary)
            write_json(figure_path, figures)
            write_json(inputs_path, inputs)
            preserved = [summary_path, figure_path, inputs_path, summary_dir / "figures/fig_001.png"]
            hashes = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in preserved}
            latex = render_latex(summary, {row["id"]: row for row in inputs},
                                 {row["figure_id"]: row for row in figures}, "261002")
            build_pdf(summary_dir, output)
            with fitz.open(output) as document:
                text = re.sub(r"\s+", "", "\n".join(page.get_text() for page in document))
                self.assertEqual(sum(len(page.get_image_info()) for page in document), 2)
            for label, value in (("pdf", text), ("latex", latex)):
                with self.subTest(output=label):
                    self.assertIn("该数值待核对", value)
                    for internal in ("n0001", "n0002", "n0003", "s0001", "[数值待核对:", "[漏识数值待核对:"):
                        self.assertNotIn(internal, value)
                    for confirmed in ("222", "203.46", "2026-09-28"):
                        self.assertIn(confirmed, value)
            self.assertIn("222%", text)
            self.assertIn(r"222\%", latex)
            self.assertEqual(hashes, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in preserved})
            stats = json.loads((summary_dir / "market_views_render_stats.json").read_text())
            self.assertEqual(stats["rendered_figure_ids"], ["F001"])

    def test_portrait_original_pages_keep_wrapped_captions_on_the_same_page(self) -> None:
        """Three 1224x1584 originals can fit while the last caption cannot."""
        with tempfile.TemporaryDirectory() as temp_dir:
            summary_dir, output = self.make_summary(Path(temp_dir))
            figures = []
            for index in range(1, 5):
                relative = f"figures/portrait_{index}.png"
                Image.new("RGB", (1224, 1584), (index * 40, 70, 110)).save(summary_dir / relative)
                figures.append({
                    "figure_id": f"F{index:03d}", "report_id": "R001", "figure_type": "source_exhibit",
                    "label": f"Source-page-{index}", "latex_path": relative,
                    "context": ("Original report evidence" if index != 3 else
                                "MHCV industry is on an upcycle since H2FY26, with demand holding intact; "
                                "CV operators are passing through price hikes relatively faster; "
                                "original tables and source footnotes remain available for review."),
                })
            write_json(summary_dir / "figure_candidates.json", figures)
            summary = json.loads((summary_dir / "market_views_structured.json").read_text())
            section = summary["bank_roundup"]["sections"][0]
            section["figure_ids"] = [row["figure_id"] for row in figures]
            section["bank_views"][0]["view"] = (
                "Revenue margins and financing conditions change across the cycle. " * 44
            )
            write_json(summary_dir / "market_views_structured.json", summary)
            build_pdf(summary_dir, output)
            with fitz.open(output) as document:
                seen = []
                image_count = 0
                for page in document:
                    images = page.get_image_info()
                    image_count += len(images)
                    for block in page.get_text("blocks"):
                        if block[6] != 0 or "Source-page-" not in block[4]:
                            continue
                        label = next(row["label"] for row in figures if row["label"] in block[4])
                        seen.append(label)
                        preceding = [fitz.Rect(row["bbox"]) for row in images
                                     if 0 <= block[1] - row["bbox"][3] < 8]
                        self.assertEqual(len(preceding), 1, f"{label} must immediately follow its full image on the same page")
                        self.assertTrue(page.rect.contains(preceding[0]))
                        self.assertTrue(page.rect.contains(fitz.Rect(block[:4])))
                        self.assertLess(block[3], page.rect.height - 42,
                                        "Caption must not overlap the footer")
                        if label == "Source-page-3":
                            tail = page.search_for("original tables and source footnotes remain available for review.")
                            self.assertTrue(tail, "The complete wrapped caption stays with its original page image")
                            self.assertGreater(tail[-1].y1, block[3], "Exercise a caption that wraps beyond its first line")
                self.assertEqual(sorted(seen), sorted(row["label"] for row in figures))
                self.assertEqual(image_count, 5, "All four originals and the existing ending image remain")
            stats = json.loads((summary_dir / "market_views_render_stats.json").read_text())
            self.assertEqual(stats["rendered_figure_ids"], ["F001", "F002", "F003", "F004"])


if __name__ == "__main__":
    unittest.main()
