#!/usr/bin/env python3
"""Regression tests for MinerU figures in Market Views inputs."""

from __future__ import annotations

import tempfile
import hashlib
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

from build_market_views_pdf import (copy_figures, extract_exhibit_figures, handoff_source_images,
                                   resolve_image_path, select_section_figures, source_figure_display_exclusion)


def make_image(path: Path, color: tuple[int, int, int] = (20, 80, 140)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (900, 520), color).save(path)


class MarketViewsFigureTests(unittest.TestCase):
    def test_display_filter_rejects_actual_rating_history_in_each_owned_text_field(self) -> None:
        for field in ("body_text", "content_captions", "content_footnotes", "captions", "footnotes"):
            with self.subTest(field=field):
                title = "Goldman Sachs rating and stock price target history"
                value = title if field == "body_text" else ([{"text": title}] if field in ("captions", "footnotes") else [title])
                self.assertEqual(source_figure_display_exclusion({"kind": "chart", field: value}),
                                 "exclude_broker_rating_history")
        for text in ("Stock Rating History: 6/6/23 O/H; 8/14/24 O/H",
                     "Goldman Sachs rating and stock price history",
                     "Budweiser Rating History for Bernstein as of 10/02/2026",
                     "The price targets shown should be considered in the context of all prior published Goldman Sachs research.",
                     "Covered by Neil Mehta; Price target removal; Not covered by current analyst",
                     "股票评级与目标价历史"):
            with self.subTest(text=text):
                self.assertEqual(source_figure_display_exclusion({"kind": "chart", "body_text": text}),
                                 "exclude_broker_rating_history")

    def test_display_filter_rejects_actual_p28_analyst_coverage_table(self) -> None:
        record = {"kind": "table", "body_text": "<table><tr><td>Justin M Lang</td></tr><tr><td>Gogo Inc. (GOGO.O)</td><td>E (08/14/2025)</td><td>$2.11</td></tr><tr><td>Iridium (IRDM.O)</td><td>E (01/16/2026)</td><td>$48.96</td></tr><tr><td>Kristine T Liwag</td></tr></table>",
                  "content_footnotes": ["Stock Ratings are subject to change. Please see latest research for each company."]}
        self.assertEqual(source_figure_display_exclusion(record), "exclude_analyst_coverage_table")
        self.assertEqual(source_figure_display_exclusion({"kind": "table", "body_text": "Company Ticker Rating Price Target",
                         "captions": [{"text": "Analyst Coverage"}]}), "exclude_analyst_coverage_table")
        # Names and company coverage by themselves are not editorial evidence.
        record["content_footnotes"] = []
        self.assertIsNone(source_figure_display_exclusion(record))
        self.assertIsNone(source_figure_display_exclusion({"kind": "table",
            "body_text": "Revenue FY24 100 FY25 120 EBITDA margin15% 18%",
            "content_captions": ["Figure3: Revenue and operating margin forecast"],
            "footnotes": [{"text": "Stock ratings are subject to change. Please see the latest research for each company."}]}))

    def test_display_filter_rejects_short_explicit_disclosure_but_not_normal_source_notes(self) -> None:
        self.assertEqual(source_figure_display_exclusion({"kind": "table", "body_text": "Analyst Certification. Analysts' compensation. All rights reserved."}),
                         "exclude_publication_disclosure")
        self.assertEqual(source_figure_display_exclusion({"kind": "chart", "content_captions": ["Ratings Distribution"],
                         "footnotes": [{"text": "Investment banking clients."}]}), "exclude_publication_disclosure")
        for body in ("Income statement. Revenue grew15%. Compensation expenses increased2%.",
                     "Copyright licensing revenue is expected to grow15%.",
                     "Regulatory reform could alter bank capital and industry competition."):
            with self.subTest(body=body):
                self.assertIsNone(source_figure_display_exclusion({"kind": "table", "body_text": body,
                    "content_captions": ["Figure1: Revenue outlook"],
                    "footnotes": [{"text": "Source: Goldman Sachs. Disclaimer: not an offer. All rights reserved."}]}))

    def test_display_filter_keeps_valuation_credit_rating_and_company_coverage_research(self) -> None:
        for text in ("Exhibit 1: What's in the Price at $150/share? Space & Connectivity EV / EBITDA (2028 MSe)",
                     "Valuation sensitivity: target price $150; revenue growth20%, WACC8%.",
                     "Credit rating history and sovereign rating transition estimates",
                     "Credit rating and bond price history",
                     "Company coverage research: price targets and valuation upside",
                     "Rating agencies' historical default rates by credit rating",
                     "Source: Morgan Stanley Research. Covered by our global company coverage research."):
            with self.subTest(text=text):
                self.assertIsNone(source_figure_display_exclusion({"kind": "table", "body_text": text}))
        self.assertIsNone(source_figure_display_exclusion({"kind": "image", "body_text": ""}))
        for caption in ("Ratings Distribution of the corporate bond portfolio", "企业债信用评级分布", "评级分布：公司债组合"):
            with self.subTest(caption=caption):
                self.assertIsNone(source_figure_display_exclusion({"kind": "chart", "body_text": "AAA15%; AA25%; A35%; BBB25%",
                    "content_captions": [caption], "content_footnotes": ["Source: Moody's. All rights reserved."]}))

    def test_verified_display_filter_preserves_source_proof_and_cannot_be_refilled(self) -> None:
        from test_mineru_figure_sources import Fixture, visual
        from mineru_figure_sources import FigureSourceError
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            fixture = Fixture(root, visuals=[
                visual(0, [30, 80, 350, 180], kind="chart", page_idx=0,
                       captions=[([30, 60, 350, 79], "Goldman Sachs rating and stock price history")]),
                visual(1, [30, 80, 350, 180], kind="table", page_idx=1,
                       body="<table><tr><td>Justin M Lang</td><td>SpaceX (SPCX.O)</td><td>O (07/07/2026)</td></tr><tr><td>Kristine T Liwag</td><td>Gogo (GOGO.O)</td><td>E (08/14/2025)</td></tr></table>",
                       footnotes=[([30, 182, 350, 200], "Stock Ratings are subject to change. Please see latest research for each company.")]),
                visual(2, [30, 80, 350, 180], kind="table", page_idx=2,
                       body="<table><tr><td>EV/EBITDA</td><td>10x</td><td>15x</td></tr></table>",
                       captions=[([30, 60, 350, 79], "Exhibit1: What's in the Price at $150/share?")]),
            ], pages=3)
            fixture.create(); fixture.status()
            (fixture.report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": fixture.md_sha,
                "images": fixture.selection["reference_images"],
            }))
            before = {str(p.relative_to(fixture.report)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in fixture.report.rglob('*') if p.is_file()}
            self.assertEqual(len(fixture.validate()), 3, "all source evidence remains admitted")
            with patch('pdf_to_xhs_batch.chart_image_score', return_value=(10, 'test-ranked')):
                selected = extract_exhibit_figures(fixture.report, 'R001', 'Space and energy', 1)
            self.assertEqual([row['source_page'] for row in selected], [3], "filter before truncating the report budget")
            self.assertEqual(len(fixture.validate()), 3)
            after = {str(p.relative_to(fixture.report)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in fixture.report.rglob('*') if p.is_file()}
            self.assertEqual(before, after, "display filtering must not rewrite proofs, maps or source pixels")
            figures = copy_figures(selected, root / 'public-figures', 0)
            self.assertEqual(len(figures), 1)
            for requested in ([], ['excluded-history', 'excluded-coverage']):
                self.assertEqual(select_section_figures(requested, ['R001'], figures, 4), [figures[0]['figure_id']])
            # Invalid metadata may not be hidden by an exclusion decision.
            fixture.mutate(lambda proof: proof['metadata']['records'][0].update(body_text='Stock Rating History'), reseal=False)
            with self.assertRaises(FigureSourceError):
                extract_exhibit_figures(fixture.report, 'R001', 'Research', 4)

    def test_verified_figures_keep_original_priority_and_reject_swapped_aliases(self) -> None:
        import shutil
        from test_mineru_figure_sources import Fixture, visual
        from pdf_to_xhs_batch import create_chart_source_assets
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = Fixture(Path(temp_dir), visuals=[
                visual(0, [20, 80, 145, 200], kind="chart", ref="images/profile.jpg"),
                visual(1, [200, 90, 380, 220], kind="chart", ref="images/chart.jpg"),
            ])
            images = create_chart_source_assets(
                fixture.raw, fixture.assets, 100, original_pdf_sha256=fixture.original_sha,
                auth_original_pdf=fixture.original, markdown_sha256=fixture.md_sha,
            )
            fixture.selection = {"images": images}
            fixture.admitted = True
            fixture.status()
            shutil.rmtree(fixture.raw)
            selected = extract_exhibit_figures(fixture.report, "R001", "Research", 1)
            self.assertEqual(Path(selected[0]["source_path"]).name, "source_image_02.png")
            self.assertEqual(selected[0]["selection_source"], "mineru_source_figure")
            all_figures = extract_exhibit_figures(fixture.report, "R001", "Research", 0)
            self.assertEqual(len(all_figures), 2, "Valid lower-ranked figures remain eligible")
            self.assertEqual(all_figures[0]["source_page"], 1)
            mapping_path = fixture.report / "source_image_map.json"
            mapping = json.loads(mapping_path.read_bytes())
            swaps = {images[0]: images[1], images[1]: images[0]}
            mapping["images"] = {ref: swaps[target] for ref, target in mapping["images"].items()}
            mapping_path.write_text(json.dumps(mapping))
            with self.assertRaisesRegex(RuntimeError, "complete image map"):
                extract_exhibit_figures(fixture.report, "R001", "Research", 1)

    def test_private_handoff_map_restores_exact_markdown_image_and_caption(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir) / "report"
            report.mkdir()
            md = report / "source_mineru.md"
            md.write_text("## Figure 9: Revenue growth across regions\n![](images/provider-hash.jpg)\n")
            image = report / "assets" / "source_image_01.png"
            make_image(image)
            (report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": hashlib.sha256(md.read_bytes()).hexdigest(),
                "images": {"images/provider-hash.jpg": "assets/source_image_01.png"},
            }))
            figures = extract_exhibit_figures(report, "R001", "Revenue outlook", 4)
            self.assertEqual(len(figures), 1)
            self.assertEqual(figures[0]["label"], "Figure 9")
            self.assertIn("Revenue growth across regions", figures[0]["context"])
            self.assertEqual(Path(figures[0]["source_path"]), image)

    def test_excluded_provider_reference_cannot_reappear_from_raw_basename(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("![](images/disclosures.jpg)\n")
            make_image(report / "mineru_raw" / "images" / "disclosures.jpg")
            (report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": hashlib.sha256(md.read_bytes()).hexdigest(), "images": {},
            }))
            self.assertIsNone(resolve_image_path(md, "images/disclosures.jpg"))

    def test_invalid_map_cannot_fall_back_to_an_unbound_raw_image(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("![](images/chart.jpg)\n")
            make_image(report / "mineru_raw" / "images" / "chart.jpg")
            (report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": "0" * 64, "images": {},
            }))
            with self.assertRaisesRegex(RuntimeError, "image map is invalid"):
                resolve_image_path(md, "images/chart.jpg")

    def test_invalid_map_cannot_bypass_validation_when_markdown_has_no_exhibit(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("# Parsed report\n")
            make_image(report / "assets" / "source_image_01.png")
            mapping = report / "source_image_map.json"
            mapping.write_text(json.dumps({"version": 1, "source_sha256": "0" * 64, "images": {}}))
            with self.assertRaisesRegex(RuntimeError, "image map is invalid"):
                extract_exhibit_figures(report, "R001", "Market outlook", 4)
            mapping.unlink()
            mapping.symlink_to("missing-map.json")
            with self.assertRaisesRegex(RuntimeError, "image map is invalid"):
                extract_exhibit_figures(report, "R001", "Market outlook", 4)

    def test_empty_admitted_map_does_not_resurrect_leftover_handoff_asset(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("# Parsed report\n")
            make_image(report / "assets" / "source_image_01.png")
            (report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": hashlib.sha256(md.read_bytes()).hexdigest(), "images": {},
            }))
            self.assertEqual(extract_exhibit_figures(report, "R001", "Market outlook", 4), [])

    def test_invalid_figure_proof_cannot_bypass_validation_without_markdown_exhibits(self) -> None:
        from mineru_figure_sources import FigureSourceError
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("# Parsed report\n")
            make_image(report / "assets" / "source_image_01.png")
            image = "assets/source_image_01.png"
            (report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": hashlib.sha256(md.read_bytes()).hexdigest(),
                "images": {"images/provider.jpg": image},
            }))
            (report / "status.json").write_text(json.dumps({"images": [image], "original_pdf_sha256": None}))
            (report / "source_figure_map.json").write_text("[]")
            with self.assertRaises(FigureSourceError):
                extract_exhibit_figures(report, "R001", "Market outlook", 4)

    def test_deleted_declared_figure_proof_cannot_downgrade_to_map_fallback(self) -> None:
        from mineru_figure_sources import FigureSourceError
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("# Parsed report\n")
            make_image(report / "assets" / "source_image_01.png")
            image = "assets/source_image_01.png"
            (report / "source_image_map.json").write_text(json.dumps({
                "version": 1, "source_sha256": hashlib.sha256(md.read_bytes()).hexdigest(),
                "images": {"images/provider.jpg": image},
            }))
            (report / "status.json").write_text(json.dumps({
                "images": [image], "original_pdf_sha256": "a" * 64,
                "source_figure_map": "source_figure_map.json", "source_figure_map_sha256": "b" * 64,
            }))
            with self.assertRaises(FigureSourceError):
                extract_exhibit_figures(report, "R001", "Market outlook", 4)

    def test_map_rejects_duplicate_alias_and_asset_path_escape(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir)
            md = report / "source_mineru.md"
            md.write_text("![](images/chart.jpg)\n")
            image = report / "assets" / "source_image_01.png"
            make_image(image)
            source_sha = hashlib.sha256(md.read_bytes()).hexdigest()
            mapping = report / "source_image_map.json"
            mapping.write_text('{"version":1,"source_sha256":"' + source_sha +
                               '","images":{"images/chart.jpg":"assets/source_image_01.png",' +
                               '"images/chart.jpg":"assets/source_image_01.png"}}')
            with self.assertRaises(RuntimeError):
                resolve_image_path(md, "images/chart.jpg")
            mapping.write_text(json.dumps({"version": 1, "source_sha256": source_sha,
                                           "images": {"images/chart.jpg": "../assets/source_image_01.png"}}))
            with self.assertRaises(RuntimeError):
                resolve_image_path(md, "images/chart.jpg")

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
