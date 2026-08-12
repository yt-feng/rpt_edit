#!/usr/bin/env python3
"""Regression tests for writing selected MinerU figures into the PDF body."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from render_market_views_reportlab_pdf import build_pdf


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

    def test_rejects_selected_figure_that_cannot_be_rendered(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            summary_dir, output = self.make_summary(Path(temp_dir), broken_figure=True)

            with self.assertRaisesRegex(RuntimeError, "not rendered"):
                build_pdf(summary_dir, output)


if __name__ == "__main__":
    unittest.main()
