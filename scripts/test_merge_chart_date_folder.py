#!/usr/bin/env python3
"""Regression tests for Chart source dates versus catalog report dates."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import merge_chart_search_index as merge


class MergeChartDateFolderTests(unittest.TestCase):
    def test_catalog_date_never_overwrites_chart_source_date(self) -> None:
        charts = {
            "schema_version": 1,
            "reports": [{
                "report_id": "report-alpha",
                "title": "Alpha forecast",
                "date_folder": "260826",
                "charts": [],
            }],
        }
        catalog = {
            "items": [{
                "id": "report-alpha",
                "title": "Alpha forecast",
                "date_folder": "260605",
            }],
        }

        self.assertEqual(merge.reconcile_report_ids(charts, catalog), 0)
        report = charts["reports"][0]
        self.assertEqual(report["date_folder"], "260826")
        self.assertEqual(report["catalog_date_folder"], "260605")

    def test_catalog_date_is_added_after_title_reconciliation(self) -> None:
        charts = {
            "schema_version": 1,
            "reports": [{
                "report_id": "",
                "title": "Alpha MLCC Outlook",
                "date_folder": "260826",
                "charts": [],
            }],
        }
        catalog = {
            "items": [{
                "id": "report-alpha",
                "title": "Alpha-MLCC_Outlook.pdf",
                "date_folder": "260605",
            }],
        }

        self.assertEqual(merge.reconcile_report_ids(charts, catalog), 1)
        report = charts["reports"][0]
        self.assertEqual(report["report_id"], "report-alpha")
        self.assertEqual(report["date_folder"], "260826")
        self.assertEqual(report["catalog_date_folder"], "260605")

    def test_stale_catalog_date_is_removed_without_touching_source_date(self) -> None:
        charts = {
            "schema_version": 1,
            "reports": [{
                "report_id": "not-in-catalog",
                "title": "Historical chart",
                "date_folder": "260826",
                "catalog_date_folder": "260605",
                "charts": [],
            }],
        }

        self.assertEqual(merge.reconcile_report_ids(charts, {"items": []}), 0)
        report = charts["reports"][0]
        self.assertEqual(report["date_folder"], "260826")
        self.assertNotIn("catalog_date_folder", report)

    def test_merge_command_publishes_both_dates_without_mutating_source(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            search_path = root / "search.json"
            chart_path = root / "charts.json"
            catalog_path = root / "catalog.json"
            output_path = root / "published.json"
            search_path.write_text(
                json.dumps({"items": [{"id": "report-alpha", "text": "base"}]}),
                encoding="utf-8",
            )
            chart_path.write_text(
                json.dumps({
                    "schema_version": 1,
                    "reports": [{
                        "report_id": "report-alpha",
                        "title": "Alpha forecast",
                        "date_folder": "260826",
                        "chart_count": 0,
                        "charts": [],
                    }],
                }),
                encoding="utf-8",
            )
            catalog_path.write_text(
                json.dumps({
                    "items": [{
                        "id": "report-alpha",
                        "title": "Alpha forecast",
                        "date_folder": "260605",
                    }],
                }),
                encoding="utf-8",
            )
            argv = [
                "merge_chart_search_index.py",
                "--search-index", str(search_path),
                "--chart-index", str(chart_path),
                "--catalog", str(catalog_path),
                "--chart-output", str(output_path),
            ]
            with patch.object(sys, "argv", argv):
                self.assertEqual(merge.main(), 0)

            published = json.loads(output_path.read_text(encoding="utf-8"))
            report = published["reports"][0]
            self.assertEqual(report["date_folder"], "260826")
            self.assertEqual(report["catalog_date_folder"], "260605")


if __name__ == "__main__":
    unittest.main(verbosity=2)
