#!/usr/bin/env python3
"""Decide whether a previously committed report shard can be reused."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any


SUMMARY_LINE_RE = re.compile(r"^-\s*([^:]+):\s*(.*?)\s*$")
LEADING_SEQUENCE_RE = re.compile(r"^\d+-")
REQUIRED_REPORT_FILES = ("source_mineru.md", "wechat_article.md", "status.json")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_markdown_summary(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = SUMMARY_LINE_RE.match(line.strip())
        if match:
            values[match.group(1).strip()] = match.group(2).strip()
    return values


def normalized_source_name(value: str) -> str:
    name = Path(value).name
    while LEADING_SEQUENCE_RE.match(name):
        name = LEADING_SEQUENCE_RE.sub("", name, count=1)
    # Batch staging replaces punctuation such as ：, ~, &, quotes and brackets
    # with hyphens. Compare the stable letters/numbers/CJK payload instead.
    return re.sub(r"[\W_]+", "", name.casefold(), flags=re.UNICODE)


def manifest_source_names(manifest_path: Path, shard_index: int, reports_per_shard: int) -> list[str]:
    payload = read_json(manifest_path)
    if not isinstance(payload, list):
        raise ValueError(f"Manifest must contain a list: {manifest_path}")
    ordered = sorted(
        (item for item in payload if isinstance(item, dict)),
        key=lambda item: (int(item.get("process_rank") or 10**9), int(item.get("id") or 10**9)),
    )
    start = shard_index * reports_per_shard
    selected = ordered[start : start + reports_per_shard]
    return [
        normalized_source_name(
            str(item.get("process_local_path") or item.get("local_path") or item.get("name") or "")
        )
        for item in selected
    ]


def report_source_names(report_dirs: list[Path]) -> list[str]:
    names: list[str] = []
    for report_dir in report_dirs:
        status = read_json(report_dir / "status.json")
        if not isinstance(status, dict):
            raise ValueError(f"Status must contain an object: {report_dir / 'status.json'}")
        names.append(normalized_source_name(str(status.get("source_pdf") or "")))
    return names


def completed_shard_reason(
    output_dir: Path,
    current_manifest: Path,
    shard_index: int,
    selected_count: int,
    reports_per_shard: int,
    force_reprocess: bool = False,
) -> tuple[bool, str]:
    if force_reprocess:
        return False, "force_reprocess=true"

    expected_count = max(0, min(reports_per_shard, selected_count - shard_index * reports_per_shard))
    if expected_count == 0:
        return False, "the shard has no expected reports"

    summary_path = output_dir / "shard_run_summary.md"
    if not summary_path.is_file():
        return False, f"missing {summary_path.name}"
    summary = parse_markdown_summary(summary_path)
    expected_summary = {
        "Selected PDFs available to shards": selected_count,
        "Shard index": shard_index,
        "Reports per shard": reports_per_shard,
        "Report directories generated": expected_count,
    }
    for key, expected in expected_summary.items():
        try:
            actual = int(summary.get(key, ""))
        except ValueError:
            return False, f"invalid summary value for {key}"
        if actual != expected:
            return False, f"summary mismatch for {key}: expected {expected}, found {actual}"

    report_dirs = sorted(
        path for path in output_dir.iterdir()
        if path.is_dir() and (path / "wechat_article.md").is_file()
    )
    if len(report_dirs) != expected_count:
        return False, f"expected {expected_count} report directories, found {len(report_dirs)}"
    for report_dir in report_dirs:
        for filename in REQUIRED_REPORT_FILES:
            path = report_dir / filename
            if not path.is_file() or path.stat().st_size == 0:
                return False, f"missing or empty {report_dir.name}/{filename}"

    try:
        expected_sources = sorted(manifest_source_names(current_manifest, shard_index, reports_per_shard))
        actual_sources = sorted(report_source_names(report_dirs))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return False, f"cannot verify source manifest: {exc}"
    if expected_sources != actual_sources:
        return False, "current selected PDF names do not match the committed shard"

    return True, f"reusing {expected_count} complete report directories"


def write_github_output(complete: bool, reason: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT", "")
    if not output_path:
        return
    with Path(output_path).open("a", encoding="utf-8") as handle:
        handle.write(f"complete={'true' if complete else 'false'}\n")
        handle.write(f"reason={reason.replace(chr(10), ' ')}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--current-manifest", type=Path, required=True)
    parser.add_argument("--shard-index", type=int, required=True)
    parser.add_argument("--selected-count", type=int, required=True)
    parser.add_argument("--reports-per-shard", type=int, required=True)
    parser.add_argument("--force-reprocess", default="false")
    args = parser.parse_args()

    complete, reason = completed_shard_reason(
        args.output_dir,
        args.current_manifest,
        args.shard_index,
        args.selected_count,
        args.reports_per_shard,
        str(args.force_reprocess).lower() in {"1", "true", "yes", "on"},
    )
    write_github_output(complete, reason)
    print(f"complete={'true' if complete else 'false'}: {reason}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
