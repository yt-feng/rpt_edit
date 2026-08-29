#!/usr/bin/env python3
"""Regression tests for append-only Chart acquisition dates in the builder."""

from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

import build_chart_search_index as chart
import chart_search_r2 as r2


REPORT_ID = "report-alpha"


def write_image(path: Path, color: str) -> str:
    image = Image.new("RGB", (640, 360), "white")
    draw = ImageDraw.Draw(image)
    draw.line((20, 320, 180, 180, 340, 260, 610, 60), fill=color, width=10)
    image.save(path)
    return chart.sha256_file(path)


def analysis(title: str) -> dict:
    return chart.normalize_analysis({
        "is_chart": True,
        "content_kind": "chart",
        "quality_score": 92,
        "has_data_evidence": True,
        "invalid_reason": "none",
        "title": title,
        "chart_type": "line",
        "description": f"{title} shows a visible trend.",
        "trend_summary": "up",
        "metrics": ["shipments"],
        "entities": ["Alpha"],
        "periods": ["2026"],
        "geographies": ["Global"],
        "units": ["units"],
        "keywords": ["forecast"],
    })


def cached_state(rows: dict[str, dict]) -> dict:
    return {
        "schema_version": 1,
        "analysis_version": chart.ANALYSIS_VERSION,
        "items": {
            image_id: {
                "status": "ok",
                "analysis_version": chart.ANALYSIS_VERSION,
                "analysis": payload,
            }
            for image_id, payload in rows.items()
        },
    }


def candidate(path: Path, image_id: str, date_folder: str, *, report_ref: str | None = None) -> chart.ChartCandidate:
    return chart.ChartCandidate(
        image_path=path,
        image_sha256=image_id,
        report_ref=report_ref or chart.canonical_report_ref(REPORT_ID),
        report_id=REPORT_ID,
        report_title="Alpha forecast",
        date_folder=date_folder,
        ordinal=1,
    )


def build(
    root: Path,
    candidates: list[chart.ChartCandidate],
    state: dict,
    previous_index: dict,
    *,
    catalog_lookup: dict | None = None,
) -> dict:
    state_path = root / "state.json"
    state_path.write_text("{}", encoding="utf-8")
    index, _summary = chart.build_index(
        candidates,
        state=state,
        previous_index=previous_index,
        state_path=state_path,
        asset_output_dir=root / "assets",
        analyze=lambda _path: (_ for _ in ()).throw(AssertionError("cache should be reused")),
        max_model_calls=0,
        catalog_lookup=catalog_lookup,
        attempt_run_id="source-date-test",
    )
    return index


class ChartBuilderSourceDateTests(unittest.TestCase):
    def test_later_run_keeps_earliest_report_date_and_all_charts(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            old_path = root / "old.png"
            new_path = root / "new.png"
            old_id = write_image(old_path, "blue")
            new_id = write_image(new_path, "red")
            state = cached_state({old_id: analysis("Old chart"), new_id: analysis("New chart")})
            empty = {"schema_version": 1, "reports": []}

            first = build(root, [candidate(old_path, old_id, "260811")], state, empty)
            self.assertEqual(first["reports"][0]["date_folder"], "260811")
            second = build(root, [candidate(new_path, new_id, "260828")], state, first)

        self.assertEqual(second["report_count"], 1)
        report = second["reports"][0]
        self.assertEqual(report["report_id"], REPORT_ID)
        self.assertEqual(report["date_folder"], "260811")
        self.assertEqual(report["chart_count"], 2)
        self.assertEqual({row["image_id"] for row in report["charts"]}, {old_id, new_id})

    def test_unresolved_to_resolved_merge_uses_earliest_valid_date(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            old_path = root / "old.png"
            new_path = root / "new.png"
            old_id = write_image(old_path, "blue")
            new_id = write_image(new_path, "red")
            legacy_ref = "a" * 24
            old_candidate = candidate(old_path, old_id, "260811", report_ref=legacy_ref)
            old_record = chart.chart_record(old_candidate, analysis("Old chart"))
            previous = {
                "schema_version": 1,
                "report_count": 1,
                "item_count": 1,
                "reports": [{
                    "report_ref": legacy_ref,
                    "report_id": "",
                    "title": "Alpha MLCC Outlook",
                    "date_folder": "260811",
                    "chart_count": 1,
                    "charts": [old_record],
                }],
            }
            state = cached_state({new_id: analysis("New chart")})
            lookup = {
                key: [(REPORT_ID, "Alpha MLCC Outlook")]
                for key in chart.title_keys("Alpha MLCC Outlook")
            }
            resolved = build(
                root,
                [candidate(new_path, new_id, "260828")],
                state,
                copy.deepcopy(previous),
                catalog_lookup=lookup,
            )
            coverage = r2.validate_publish_coverage(
                previous,
                resolved,
                allow_index_removal_migration=False,
            )
            self.assertFalse(coverage["coverage_regression_allowed"])

        self.assertEqual(resolved["report_count"], 1)
        report = resolved["reports"][0]
        self.assertEqual(report["report_ref"], chart.canonical_report_ref(REPORT_ID))
        self.assertEqual(report["report_ref_aliases"], [legacy_ref])
        self.assertEqual(report["date_folder"], "260811")
        self.assertEqual(report["chart_count"], 2)
        self.assertEqual({row["image_id"] for row in report["charts"]}, {old_id, new_id})

        with tempfile.TemporaryDirectory() as next_temp:
            next_root = Path(next_temp)
            next_path = next_root / "third.png"
            third_image_id = write_image(next_path, "green")
            next_state = cached_state({third_image_id: analysis("Third chart")})
            next_index = build(
                next_root,
                [candidate(next_path, third_image_id, "260829")],
                next_state,
                resolved,
            )
            next_coverage = r2.validate_publish_coverage(
                resolved,
                next_index,
                allow_index_removal_migration=False,
            )
            self.assertFalse(next_coverage["coverage_regression_allowed"])
        next_report = next_index["reports"][0]
        self.assertEqual(next_report["report_ref_aliases"], [legacy_ref])
        self.assertEqual(next_report["date_folder"], "260811")
        self.assertEqual(next_report["chart_count"], 3)

    def test_report_ref_aliases_are_opaque_deduplicated_and_bounded(self) -> None:
        canonical = chart.canonical_report_ref(REPORT_ID)
        raw_aliases = [f"{number:024x}" for number in range(1, 40)]
        reports = [{
            "report_ref": canonical,
            "report_id": REPORT_ID,
            "report_ref_aliases": [
                raw_aliases[0],
                raw_aliases[0],
                "not-an-opaque-ref",
                canonical,
                *raw_aliases[1:],
            ],
            "title": "Alpha forecast",
            "date_folder": "260811",
            "charts": [],
        }]

        merged = chart.merge_reports_by_report_id(reports)[0]
        aliases = merged["report_ref_aliases"]
        self.assertEqual(len(aliases), chart.MAX_REPORT_REF_ALIASES)
        self.assertEqual(len(aliases), len(set(aliases)))
        self.assertNotIn(canonical, aliases)
        self.assertTrue(all(chart.REPORT_REF_RE.fullmatch(value) for value in aliases))

    def test_invalid_dates_do_not_replace_valid_history(self) -> None:
        self.assertEqual(chart.earliest_source_date("260811", "260828"), "260811")
        self.assertEqual(chart.earliest_source_date("20260811", "260828"), "20260811")
        self.assertEqual(chart.earliest_source_date("260811", "269999", "latest"), "260811")
        self.assertEqual(chart.earliest_source_date("269999", "2026811", "latest"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
