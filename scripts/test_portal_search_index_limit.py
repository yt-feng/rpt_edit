#!/usr/bin/env python3
"""Regression checks for Portal Suite's GitHub-safe public search index."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "build_portal_suite_site.py"
SPEC = importlib.util.spec_from_file_location("portal_site_builder", MODULE_PATH)
assert SPEC and SPEC.loader
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)

GITHUB_MAX_FILE_BYTES = 100 * 1024 * 1024
default_limit = int(BUILDER.DEFAULT_SEARCH_INDEX_LIMIT_GIB * 1024 * 1024 * 1024)
assert default_limit < GITHUB_MAX_FILE_BYTES
assert GITHUB_MAX_FILE_BYTES - default_limit >= 7 * 1024 * 1024

items = [
    {"id": f"old-{index:03d}", "text": f"old report {index:03d}"}
    for index in range(80)
] + [
    {"id": f"new-{index:03d}", "text": f"new report {index:03d}"}
    for index in range(80)
]
catalog = {
    "items": [
        {
            "id": item["id"],
            "date_folder": (
                "250101"
                if item["id"].startswith("old-")
                else ("20260101" if item["id"] == "new-000" else "260101")
            ),
        }
        for item in items
    ],
}
index = {
    "schema_version": 1,
    "updated_at_bjt": "2026-07-26 12:00:00",
    "item_count": len(items),
    "sources": {},
    "items": items,
}

# This threshold deliberately fits compact JSON but not the indented file that
# write_json() commits. A compact-size estimator would therefore fail the test.
compact_size = len(json.dumps(index, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
written_size = len((json.dumps(index, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
assert compact_size < written_size
limit_bytes = compact_size + max(1, (written_size - compact_size) // 2)

limited = BUILDER.limit_search_index_by_size(index, catalog, limit_bytes)
assert limited["text_pruned_dates"] == ["250101"]
assert limited["item_count"] == 80
assert all(item["id"].startswith("new-") for item in limited["items"])
assert BUILDER.search_index_size_bytes(limited) <= limit_bytes
assert limited["text_storage_size_bytes"] == BUILDER.search_index_size_bytes(limited)

unlimited = BUILDER.limit_search_index_by_size(index, catalog, 0)
assert unlimited["item_count"] == len(items)
assert unlimited["text_pruned_dates"] == []
assert unlimited["text_storage_size_bytes"] == BUILDER.search_index_size_bytes(unlimited)
assert BUILDER.search_index_month("260722") == "2607"
assert BUILDER.search_index_month("20260722") == "2607"
assert BUILDER.search_index_month("2026-07-22") == "2607"
assert BUILDER.search_index_date("260722") == "260722"
assert BUILDER.search_index_date("20260722") == "260722"
assert BUILDER.search_index_date("2026-07-22") == "260722"

with tempfile.TemporaryDirectory() as temporary_directory:
    shard_root = Path(temporary_directory) / "search_index_current"
    manifest = BUILDER.write_search_index_shards(
        index=index,
        catalog=catalog,
        output_dir=shard_root,
        partition="day",
    )
    assert manifest["partition"] == "day"
    assert {row["date"] for row in manifest["shards"]} == {"250101", "260101"}
    assert manifest["item_count"] == len(items)
    for row in manifest["shards"]:
        shard = json.loads((shard_root / row["file"]).read_text(encoding="utf-8"))
        assert shard["items"]
        assert all(item["id"].startswith("old-") for item in shard["items"]) == (row["date"] == "250101")

print("Portal Suite search-index size limit checks passed.")
