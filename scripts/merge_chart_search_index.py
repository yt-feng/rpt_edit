#!/usr/bin/env python3
"""Merge chart descriptions into the report full-text index and publish chart data."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any


MARKER = "\n[[CHART_SEARCH_V1]]\n"
BANK_ALIASES = (
    "goldman sachs", "j p morgan", "jp morgan", "jpmorgan", "morgan stanley",
    "deutsche bank", "bank of america", "bofa", "barclays", "bernstein",
    "jefferies", "nomura", "citi", "citigroup", "ubs", "hsbc", "gs", "jpm",
    "ms", "db", "barc", "jef", "nom",
)
REPORT_PREVIEW_FIELDS = (
    "title_zh", "filename", "bank_code", "bank_name",
    "size_bytes", "available", "industry", "sector", "category",
    "pdf_archived", "page_count",
)
CATALOG_DATE_FOLDER_FIELD = "catalog_date_folder"


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Invalid JSON input: {path.name}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected a JSON object: {path.name}")
    return value


def atomic_write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def clean_text(value: Any, limit: int) -> str:
    return " ".join(str(value or "").split())[:limit]


def normalize_title(value: Any) -> str:
    text = unicodedata.normalize("NFKC", clean_text(value, 500)).casefold()
    text = re.sub(r"\.pdf$", "", text, flags=re.IGNORECASE)
    return "".join(character for character in text if character.isalnum())


def normalize_title_words(value: Any) -> str:
    text = unicodedata.normalize("NFKC", clean_text(value, 500)).casefold()
    words: list[str] = []
    current: list[str] = []
    for character in text:
        if character.isalnum():
            current.append(character)
        elif current:
            words.append("".join(current))
            current = []
    if current:
        words.append("".join(current))
    return " ".join(words)


def title_keys(value: Any) -> set[str]:
    base = re.sub(r"\.pdf$", "", Path(str(value or "")).name, flags=re.IGNORECASE)
    stripped = re.sub(r"^(?:\d{1,4}[-_]){1,3}", "", base).strip()
    variants = {base, stripped}
    variants |= {re.sub(r"[-_\s~]+(?:20)?\d{6,8}$", "", item).strip() for item in list(variants)}
    aliases = sorted((normalize_title_words(alias) for alias in BANK_ALIASES), key=len, reverse=True)
    keys: set[str] = set()
    for variant in variants:
        words = normalize_title_words(variant)
        compact = normalize_title(words)
        if compact:
            keys.add(compact)
        for alias in aliases:
            if words.startswith(alias + " "):
                without_bank = normalize_title(words[len(alias) + 1 :])
                if without_bank:
                    keys.add(without_bank)
                break
    return keys


def reconcile_report_ids(chart_index: dict[str, Any], catalog: dict[str, Any]) -> int:
    lookup: dict[str, set[str]] = {}
    catalog_by_id: dict[str, dict[str, Any]] = {}
    for item in catalog.get("items", []):
        if not isinstance(item, dict) or not item.get("id"):
            continue
        report_id = clean_text(item.get("id"), 64)
        catalog_by_id[report_id] = item
        for candidate in (item.get("title"), item.get("filename"), item.get("title_zh")):
            for normalized in title_keys(candidate):
                lookup.setdefault(normalized, set()).add(report_id)
    reconciled = 0
    for report in chart_index.get("reports", []):
        if not isinstance(report, dict):
            continue
        report_id = clean_text(report.get("report_id"), 64)
        if not report_id:
            matches = {
                candidate_id
                for key in title_keys(report.get("title"))
                for candidate_id in lookup.get(key, set())
            }
            if len(matches) == 1:
                report_id = next(iter(matches))
                report["report_id"] = report_id
                reconciled += 1
        catalog_item = catalog_by_id.get(report_id)
        if not catalog_item:
            # A chart record outside the current catalog has no trustworthy PDF state.
            report.pop(CATALOG_DATE_FOLDER_FIELD, None)
            report.pop("available", None)
            report.pop("pdf_archived", None)
            continue
        canonical_title = clean_text(catalog_item.get("title") or catalog_item.get("filename"), 300)
        if canonical_title:
            report["title"] = canonical_title
        # date_folder is the immutable chart acquisition/source date.  Catalog
        # metadata can point at an older canonical report date, so publish it
        # separately instead of rewriting the chart timeline.
        catalog_date_folder = clean_text(catalog_item.get("date_folder"), 16)
        if catalog_date_folder:
            report[CATALOG_DATE_FOLDER_FIELD] = catalog_date_folder
        else:
            report.pop(CATALOG_DATE_FOLDER_FIELD, None)
        for key in REPORT_PREVIEW_FIELDS:
            value = catalog_item.get(key)
            if key in {"available", "pdf_archived"} and not isinstance(value, bool):
                report.pop(key, None)
                continue
            if value is None or value == "":
                continue
            report[key] = value
    return reconciled


def merge_indexes(search_index: dict[str, Any], chart_index: dict[str, Any]) -> dict[str, int]:
    items = [item for item in search_index.get("items", []) if isinstance(item, dict) and item.get("id")]
    by_id = {str(item["id"]): item for item in items}
    chart_reports = 0
    chart_matched = 0
    chart_items = 0
    for report in chart_index.get("reports", []):
        if not isinstance(report, dict):
            continue
        chart_reports += 1
        chart_items += int(report.get("chart_count") or 0)
        report_id = clean_text(report.get("report_id"), 64)
        chart_text = clean_text(report.get("search_text"), 12_000)
        if not report_id or not chart_text or report_id not in by_id:
            continue
        item = by_id[report_id]
        base = str(item.get("text") or "").split(MARKER, 1)[0].rstrip()
        item["text"] = (base + MARKER + chart_text).strip()
        chart_matched += 1
    search_index["items"] = items
    search_index["item_count"] = len(items)
    sources = search_index.setdefault("sources", {})
    if not isinstance(sources, dict):
        sources = {}
        search_index["sources"] = sources
    sources.update({
        "chart_reports": chart_reports,
        "chart_matched": chart_matched,
        "chart_items": chart_items,
    })
    return {
        "chart_reports": chart_reports,
        "chart_matched": chart_matched,
        "chart_items": chart_items,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--search-index", required=True)
    parser.add_argument("--chart-index", required=True)
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--chart-output", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    search_path = Path(args.search_index)
    chart_path = Path(args.chart_index)
    chart_output = Path(args.chart_output)
    search_index = load_json(search_path)
    chart_index = load_json(chart_path)
    catalog = load_json(Path(args.catalog))
    if int(chart_index.get("schema_version") or 0) != 1:
        raise RuntimeError("Unsupported chart-search index schema")
    reconciled = reconcile_report_ids(chart_index, catalog)
    counts = merge_indexes(search_index, chart_index)
    atomic_write(search_path, search_index)
    atomic_write(chart_output, chart_index)
    print(
        "chart_search_merge "
        f"reports={counts['chart_reports']} matched={counts['chart_matched']} "
        f"charts={counts['chart_items']} reconciled={reconciled}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
