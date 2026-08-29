#!/usr/bin/env python3
"""Regression tests for the manual chart-only historical backfill."""

from __future__ import annotations

import argparse
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import fitz
from PIL import Image, ImageDraw

import pdf_to_xhs_batch as pdf_batch
import validate_chart_historical_backfill as validator


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/portal-chart-historical-backfill.yml"


def make_pdf(path: Path, label: str) -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), label)
    document.save(path)
    document.close()


def make_chart(path: Path) -> None:
    image = Image.new("RGB", (800, 500), "white")
    draw = ImageDraw.Draw(image)
    for x in range(0, 800, 20):
        draw.line((x, 0, 800 - x, 500), fill=(0, 50 + x % 180, 180), width=3)
    for y in range(0, 500, 25):
        draw.line((0, y, 800, 500 - y), fill=(180, y % 180, 20), width=2)
    image.save(path)


class SourceValidationTests(unittest.TestCase):
    def build_source(self, root: Path) -> None:
        names = ["01-Alpha outlook.pdf", "02-Beta forecast.pdf"]
        manifest = []
        for rank, name in enumerate(names, 1):
            make_pdf(root / name, name)
            manifest.append(
                {
                    "name": name,
                    "dropbox_path": f"/zip_backup/260810/{name}",
                    "process_rank": rank,
                    "process_local_path": f"/runner/_selected_macro_pdfs/{name}",
                }
            )
        (root / "selected_to_process_manifest.json").write_text(
            json.dumps(manifest),
            encoding="utf-8",
        )

    def test_source_validation_is_exact_and_emits_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_source(root)
            inventory = validator.source_inventory(
                root,
                date_folder="260810",
                expected_pdf_count=2,
                reports_per_shard=1,
            )

        self.assertEqual(inventory["pdf_count"], 2)
        self.assertEqual(inventory["effective_shard_count"], 2)
        self.assertEqual(inventory["shard_indices"], [0, 1])
        self.assertTrue(all(row["page_count"] == 1 for row in inventory["pdfs"]))
        self.assertTrue(all(len(row["sha256"]) == 64 for row in inventory["pdfs"]))

    def test_source_validation_rejects_wrong_date_or_count(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_source(root)
            with self.assertRaises(validator.ValidationError):
                validator.source_inventory(
                    root,
                    date_folder="260811",
                    expected_pdf_count=2,
                    reports_per_shard=5,
                )
            with self.assertRaises(validator.ValidationError):
                validator.source_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=3,
                    reports_per_shard=5,
                )


class ChartOnlyParserTests(unittest.TestCase):
    def test_mineru_download_extracts_without_persisting_archive(self) -> None:
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, "w") as archive:
            archive.writestr("nested/full.md", "# Historical report")

        class Response:
            content = payload.getvalue()

            @staticmethod
            def raise_for_status() -> None:
                return None

        with tempfile.TemporaryDirectory() as temp:
            item_dir = Path(temp) / "report"
            raw_dir = item_dir / "mineru_raw"
            with patch.object(pdf_batch.requests, "get", return_value=Response()):
                pdf_batch.download_and_unzip("https://example.invalid/result.zip", raw_dir)

            self.assertTrue((raw_dir / "nested/full.md").is_file())
            self.assertFalse((item_dir / "mineru_result.zip").exists())

    def test_chart_source_only_skips_generated_articles_and_removes_raw(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / "output"
            source_pdf = root / "Alpha forecast.pdf"
            source_pdf.write_bytes(b"placeholder")

            def fake_download(_url: str, raw_dir: Path) -> None:
                raw_dir.mkdir(parents=True)
                (raw_dir / "report.md").write_text("# Alpha forecast\nData and outlook.", encoding="utf-8")
                make_chart(raw_dir / "chart_forecast.png")

            args = argparse.Namespace(chart_source_only=True, max_images=8)
            with patch.object(pdf_batch, "download_and_unzip", side_effect=fake_download), patch.object(
                pdf_batch,
                "safe_generate_text",
                side_effect=AssertionError("text generation must not run in chart-only mode"),
            ):
                status = pdf_batch.process_pdf(
                    source_pdf,
                    {"state": "done", "full_zip_url": "https://example.invalid/result.zip"},
                    output,
                    args,
                )

            report_dir = output / "Alpha-forecast"
            self.assertTrue(status["chart_source_only"])
            self.assertEqual(status["source_pdf"], "Alpha forecast.pdf")
            self.assertEqual(status["chart_source_image_count"], 1)
            self.assertTrue((report_dir / "source_mineru.md").is_file())
            self.assertTrue((report_dir / "assets/source_image_01.png").is_file())
            self.assertFalse((report_dir / "mineru_raw").exists())
            self.assertFalse((report_dir / "note.md").exists())
            self.assertFalse((report_dir / "wechat_article.md").exists())


class ShardValidationTests(unittest.TestCase):
    def build_shard(self, root: Path) -> None:
        (root / "batch_run_summary.json").write_text(
            json.dumps(
                {
                    "total_pdf_count_before_shard": 2,
                    "pdf_count_before_skip": 2,
                    "pdf_count": 2,
                    "generated_report_count": 2,
                    "failures": 0,
                    "shard_index": 0,
                    "shard_count": 1,
                    "chart_source_only": True,
                }
            ),
            encoding="utf-8",
        )
        for index in (1, 2):
            report = root / f"report-{index}"
            assets = report / "assets"
            assets.mkdir(parents=True)
            (report / "source_mineru.md").write_text(f"# Report {index}", encoding="utf-8")
            make_chart(assets / "source_image_01.png")
            (report / "status.json").write_text(
                json.dumps(
                    {
                        "source_pdf": f"Report {index}.pdf",
                        "chart_source_only": True,
                        "chart_source_image_count": 1,
                    }
                ),
                encoding="utf-8",
            )

    def test_shard_validation_accepts_only_complete_chart_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_shard(root)
            inventory = validator.shard_inventory(
                root,
                date_folder="260810",
                expected_pdf_count=2,
                reports_per_shard=5,
                shard_index=0,
            )
        self.assertEqual(inventory["report_count"], 2)
        self.assertEqual(inventory["chart_count"], 2)

    def test_shard_validation_rejects_generated_wechat_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.build_shard(root)
            (root / "report-1/wechat_article.md").write_text("not allowed", encoding="utf-8")
            with self.assertRaises(validator.ValidationError):
                validator.shard_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=2,
                    reports_per_shard=5,
                    shard_index=0,
                )


class AggregateValidationTests(unittest.TestCase):
    def write_inventory(
        self,
        root: Path,
        artifact_name: str,
        shard_index: int,
        reports: list[tuple[str, int]],
    ) -> None:
        artifact = root / artifact_name
        artifact.mkdir(parents=True)
        rows = [
            {
                "report_dir": f"report-{shard_index}-{offset}",
                "source_pdf": source_pdf,
                "source_markdown_bytes": 100,
                "chart_count": chart_count,
                "charts": [
                    {"ordinal": ordinal, "sha256": f"{shard_index:02x}{offset:02x}{ordinal:060x}"[-64:]}
                    for ordinal in range(1, chart_count + 1)
                ],
            }
            for offset, (source_pdf, chart_count) in enumerate(reports, 1)
        ]
        (artifact / "validated_chart_shard_inventory.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "date_folder": "260810",
                    "shard_index": shard_index,
                    "expected_report_count": len(rows),
                    "report_count": len(rows),
                    "chart_count": sum(row["chart_count"] for row in rows),
                    "reports": rows,
                }
            ),
            encoding="utf-8",
        )

    def test_aggregate_allows_zero_chart_report_when_global_minimum_is_met(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_inventory(root, "artifact-0", 0, [("Report 1.pdf", 0)])
            self.write_inventory(root, "artifact-1", 1, [("Report 2.pdf", 2)])
            inventory = validator.aggregate_inventory(
                root,
                date_folder="260810",
                expected_pdf_count=2,
                expected_shards=2,
            )
        self.assertEqual(inventory["report_count"], 2)
        self.assertEqual(inventory["chart_count"], 2)
        self.assertEqual(inventory["minimum_chart_count"], 2)

    def test_aggregate_rejects_all_zero_chart_false_green(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_inventory(root, "artifact-0", 0, [("Report 1.pdf", 0)])
            self.write_inventory(root, "artifact-1", 1, [("Report 2.pdf", 0)])
            with self.assertRaisesRegex(validator.ValidationError, "below minimum"):
                validator.aggregate_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=2,
                    expected_shards=2,
                )

    def test_aggregate_rejects_nonzero_but_severely_shrunken_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_inventory(root, "artifact-0", 0, [("Report 1.pdf", 1)])
            self.write_inventory(root, "artifact-1", 1, [("Report 2.pdf", 0)])
            with self.assertRaisesRegex(validator.ValidationError, "expected at least 2, found 1"):
                validator.aggregate_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=2,
                    expected_shards=2,
                )

    def test_aggregate_rejects_missing_shard_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_inventory(root, "artifact-0", 0, [("Report 1.pdf", 1)])
            with self.assertRaisesRegex(validator.ValidationError, "Expected exactly 2"):
                validator.aggregate_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=2,
                    expected_shards=2,
                )

    def test_aggregate_rejects_duplicate_shard_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_inventory(root, "artifact-a", 0, [("Report 1.pdf", 1)])
            self.write_inventory(root, "artifact-b", 0, [("Report 2.pdf", 1)])
            with self.assertRaisesRegex(validator.ValidationError, "Duplicate shard"):
                validator.aggregate_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=2,
                    expected_shards=2,
                )

    def test_aggregate_rejects_duplicate_report_across_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_inventory(root, "artifact-0", 0, [("Same report.pdf", 1)])
            self.write_inventory(root, "artifact-1", 1, [("Same report.pdf", 1)])
            with self.assertRaisesRegex(validator.ValidationError, "Duplicate source PDF"):
                validator.aggregate_inventory(
                    root,
                    date_folder="260810",
                    expected_pdf_count=2,
                    expected_shards=2,
                )


class WorkflowContractTests(unittest.TestCase):
    def workflow(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_is_manual_and_has_fail_closed_inputs(self) -> None:
        workflow = self.workflow()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("schedule:", workflow)
        self.assertNotIn("pull_request:", workflow)
        self.assertNotIn("push:", workflow)
        for name in ("source_artifact_run_id", "date_folder", "expected_pdf_count"):
            self.assertIn(f"      {name}:", workflow)
        self.assertIn("default: \"31454655825\"", workflow)
        self.assertIn("default: \"260810\"", workflow)
        self.assertIn("default: \"36\"", workflow)

        checkout_blocks = workflow.split("uses: actions/checkout@v4")[1:]
        self.assertEqual(len(checkout_blocks), 3)
        for block in checkout_blocks:
            checkout_step = block.split("\n      - name:", 1)[0]
            self.assertNotIn("ref: main", checkout_step)

        dispatch = workflow[workflow.index("gh workflow run portal-chart-search-index.yml"):]
        self.assertIn("--ref main", dispatch)

    def test_source_artifact_is_exact_and_resealed_for_ninety_days(self) -> None:
        workflow = self.workflow()
        self.assertIn("run-id: ${{ inputs.source_artifact_run_id }}", workflow)
        self.assertIn(
            "name: selected-macro-pdfs-${{ inputs.source_artifact_run_id }}",
            workflow,
        )
        self.assertIn("name: selected-macro-pdfs-${{ github.run_id }}", workflow)
        self.assertIn("retention-days: 90", workflow)
        self.assertIn("overwrite: true", workflow)

    def test_only_chart_sources_and_existing_chart_index_are_invoked(self) -> None:
        workflow = self.workflow()
        lowered = workflow.casefold()
        self.assertIn("--chart-source-only", workflow)
        self.assertNotIn("deepseek_api_key", lowered)
        self.assertNotIn("market-views", lowered)
        self.assertNotIn("wechat", lowered)
        self.assertNotIn("translated", lowered)
        self.assertIn("gh workflow run portal-chart-search-index.yml", workflow)
        self.assertIn("-f source_handoff_run_id=\"${{ github.run_id }}\"", workflow)
        self.assertIn("-f max_images=0", workflow)
        self.assertIn("-f retry_errors_now=true", workflow)

    def test_temporary_handoff_is_deleted_only_after_index_success(self) -> None:
        workflow = self.workflow()
        aggregate = workflow.index("validate_chart_historical_backfill.py aggregate")
        dispatch = workflow.index("gh workflow run portal-chart-search-index.yml")
        watch = workflow.index("gh run watch")
        cleanup = workflow.index("private_workflow_handoff.py delete-prefix")
        self.assertLess(aggregate, dispatch)
        self.assertLess(dispatch, watch)
        self.assertLess(watch, cleanup)
        self.assertIn(
            '--expected-pdf-count "${{ inputs.expected_pdf_count }}"',
            workflow[aggregate:dispatch],
        )
        self.assertIn(
            '--expected-shards "${{ needs.validate-source.outputs.effective_shard_count }}"',
            workflow[aggregate:dispatch],
        )
        self.assertIn(
            '--prefix "$PRIVATE_HANDOFF_ROOT/${{ github.run_id }}/${{ inputs.date_folder }}"',
            workflow,
        )
        cleanup_section = workflow[cleanup:]
        self.assertNotIn("chart-search", cleanup_section)
        self.assertNotIn("--cleanup", workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
