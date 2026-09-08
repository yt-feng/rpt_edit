#!/usr/bin/env python3
"""Read production index coverage; emit counts only, never text, IDs or object keys."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path

from summarize_portal_growth_range import r2_client


def coverage_summary(catalog: dict, research: dict, charts: dict) -> dict:
    if research.get("index_kind") != "report-research-random-access":
        raise ValueError("Unexpected research manifest kind")
    catalog_ids = {str(row.get("id")) for row in catalog.get("items", []) if row.get("id")}
    reports = [row for row in charts.get("reports", []) if isinstance(row, dict)]
    linked = [row for row in reports if row.get("report_id")]
    image_rows = [chart for row in reports for chart in row.get("charts", []) if isinstance(chart, dict)]
    return {
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "catalog_reports": len(catalog_ids),
        "research": {
            "reports": research.get("item_count"),
            "full_text_reports": research.get("full_text_item_count"),
            "partial_excerpt_reports": research.get("partial_excerpt_item_count"),
            "evidence_chunks": research.get("chunk_count"),
            "min_full_text_chars": research.get("chunking", {}).get("min_full_text_chars"),
            "per_query_report_limit": research.get("report_limit"),
        },
        "charts": {
            "updated_at": charts.get("updated_at_bjt"),
            "declared_reports": charts.get("report_count"),
            "declared_images": charts.get("item_count"),
            "measured_reports": len(reports),
            "measured_images": len(image_rows),
            "reports_with_report_id": len(linked),
            "reports_matching_catalog": sum(str(row.get("report_id")) in catalog_ids for row in reports),
            "reports_missing_report_id": len(reports) - len(linked),
            "images_with_id": sum(bool(row.get("id")) for row in image_rows),
        },
        "scope_note": "Catalog, research text corpus and chart corpus are separate inventories; counts do not establish full-text or chart coverage for every source.",
    }


def read_json(client, bucket, key, max_bytes):
    response = client.get_object(Bucket=bucket, Key=key)
    with response["Body"] as body:
        data = body.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError("Coverage input exceeds bounded read size")
    return json.loads(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    client = r2_client()
    bucket = os.environ["R2_BUCKET"]
    result = coverage_summary(
        json.loads(args.catalog.read_text()),
        read_json(client, bucket, "_report-research/v1/manifest.json", 1024 * 1024),
        read_json(client, bucket, "_chart-search/v1/index.json", 64 * 1024 * 1024),
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
