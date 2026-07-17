#!/usr/bin/env python3
"""Build the static KC Desk Notes Pages artifact."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from email.utils import format_datetime
import gzip
import hashlib
from html import escape as html_escape
import json
import os
import re
import shutil
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import quote


PUBLIC_ITEM_KEYS = [
    "id",
    "title",
    "title_zh",
    "filename",
    "date_folder",
    "date_folders",
    "bank_code",
    "bank_name",
    "password_group",
    "size_bytes",
    "client_modified",
    "server_modified",
    "first_seen_at_bjt",
    "last_seen_at_bjt",
    "available",
    "present_in_latest_scan",
    "industry",
    "sector",
    "category",
    "pdf_archived",
    "pdf_archived_at_bjt",
    "archive_reason",
    "page_count",
    "first_page_width",
    "first_page_height",
    "first_page_orientation",
    "first_page_landscape",
]

BANK_ALIASES = [
    "goldman sachs",
    "j p morgan",
    "jp morgan",
    "jpmorgan",
    "morgan stanley",
    "deutsche bank",
    "bank of america",
    "bofa",
    "barclays",
    "bernstein",
    "jefferies",
    "nomura",
    "citi",
    "citigroup",
    "ubs",
    "hsbc",
    "gs",
    "jpm",
    "ms",
    "db",
    "barc",
    "jef",
    "nom",
]

SITE_BASE_URL = "https://kcdesk.com"
SITEMAP_REPORT_CHUNK_SIZE = 5000
INDEXNOW_KEY = "201eca2fc32f348cb7280e22b4999524"
RSS_ITEM_LIMIT = 100
LLMS_REPORT_LIMIT = 200


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_json_default(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    try:
        return load_json(path)
    except (OSError, json.JSONDecodeError):
        return default


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_search_text(value: str) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).lower()
    chars: list[str] = []
    previous_space = True
    for char in text:
        category = unicodedata.category(char)
        if category[0] in {"L", "N"}:
            chars.append(char)
            previous_space = False
        elif not previous_space:
            chars.append(" ")
            previous_space = True
    return "".join(chars).strip()


def strip_leading_sequence(value: str) -> str:
    text = str(value or "")
    return re.sub(r"^(?:\d{1,4}[-_]){1,3}", "", text).strip()


def strip_extension(value: str) -> str:
    text = str(value or "").strip()
    if text.lower().endswith(".pdf"):
        return text[:-4]
    return text


def strip_trailing_date(value: str) -> str:
    return re.sub(r"[-_\s~]+(?:20)?\d{6,8}$", "", value).strip()


def compact_space(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def strip_leading_bank_alias(value: str) -> str:
    text = normalize_search_text(value)
    for alias in sorted(BANK_ALIASES, key=len, reverse=True):
        normalized_alias = normalize_search_text(alias)
        if text == normalized_alias:
            return ""
        prefix = f"{normalized_alias} "
        if text.startswith(prefix):
            return text[len(prefix):].strip()
    return text


def title_keys(value: str) -> set[str]:
    base = strip_extension(Path(str(value or "")).name)
    variants = {
        base,
        strip_leading_sequence(base),
    }
    variants |= {strip_trailing_date(item) for item in list(variants)}

    keys: set[str] = set()
    for variant in variants:
        normalized = normalize_search_text(variant)
        if normalized:
            keys.add(normalized)
            without_bank = strip_leading_bank_alias(normalized)
            if without_bank:
                keys.add(without_bank)
    return keys


def append_unique_text(target: list[str], value: str) -> None:
    text = normalize_search_text(value)
    if text and text not in target:
        target.append(text)


def build_title_lookup(items: list[dict[str, Any]]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    collisions: set[str] = set()
    for item in items:
        report_id = str(item.get("id") or "")
        if not report_id:
            continue
        values = [
            str(item.get("title") or ""),
            str(item.get("filename") or ""),
        ]
        for value in values:
            for key in title_keys(value):
                existing = lookup.get(key)
                if existing and existing != report_id:
                    collisions.add(key)
                    continue
                lookup[key] = report_id
    for key in collisions:
        lookup.pop(key, None)
    return lookup


def match_report_id(value: str, lookup: dict[str, str]) -> str:
    for key in title_keys(value):
        report_id = lookup.get(key)
        if report_id:
            return report_id
    return ""


def iter_bank_catalog_titles(root: Path) -> list[tuple[str, str]]:
    if not root.exists():
        return []
    titles: list[tuple[str, str]] = []
    for path in sorted(root.glob("*/*.txt")):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line in text.splitlines():
            stripped = line.strip()
            match = re.fullmatch(r"【(.+)】", stripped)
            if match:
                titles.append((match.group(1).strip(), str(path)))
    return titles


def trailing_date_from_title(value: str) -> str:
    text = strip_extension(str(value or "")).strip()
    match = re.search(r"[-_\s~]+(?:20)?(\d{6}|\d{8})$", text)
    if not match:
        return ""
    date = match.group(1)
    if len(date) == 8 and date.startswith("20"):
        return date[2:]
    return date


def source_date_from_path(source_path: str) -> str:
    for part in Path(source_path).parts:
        if re.fullmatch(r"\d{6}", part):
            return part
    return ""


def archive_item_id(title: str, bank_code: str) -> str:
    key = normalize_search_text(f"{bank_code} {strip_extension(title)}")
    return hashlib.sha256(f"kcdesk-archive-title:{key}".encode("utf-8")).hexdigest()[:24]


def normalize_archive_item(item: dict[str, Any], updated_at_bjt: str) -> dict[str, Any]:
    title = str(item.get("title") or item.get("filename") or "").strip()
    filename = str(item.get("filename") or f"{title}.pdf").strip()
    bank_code = str(item.get("bank_code") or item.get("bank_name") or "Archive").strip() or "Archive"
    date_folder = str(item.get("date_folder") or trailing_date_from_title(title) or "").strip()
    date_folders = item.get("date_folders") if isinstance(item.get("date_folders"), list) else []
    date_folders = sorted({str(value) for value in date_folders if str(value or "").strip()}, key=sort_date_value)
    if date_folder and date_folder not in date_folders:
        date_folders.append(date_folder)
        date_folders = sorted(set(date_folders), key=sort_date_value)
    report_id = str(item.get("id") or archive_item_id(title, bank_code)).strip()
    return {
        "id": report_id,
        "title": title,
        "title_zh": str(item.get("title_zh") or "").strip(),
        "filename": filename,
        "date_folder": date_folder,
        "date_folders": date_folders,
        "bank_code": bank_code,
        "bank_name": str(item.get("bank_name") or bank_code).strip(),
        "password_group": str(item.get("password_group") or "default").strip(),
        "size_bytes": int(item.get("size_bytes") or 0),
        "first_seen_at_bjt": str(item.get("first_seen_at_bjt") or updated_at_bjt or "").strip(),
        "last_seen_at_bjt": str(item.get("last_seen_at_bjt") or updated_at_bjt or "").strip(),
        "available": False,
        "present_in_latest_scan": False,
        "industry": str(item.get("industry") or "").strip(),
        "sector": str(item.get("sector") or "").strip(),
        "category": str(item.get("category") or "").strip(),
        "pdf_archived": True,
        "pdf_archived_at_bjt": str(item.get("pdf_archived_at_bjt") or updated_at_bjt or "").strip(),
        "archive_reason": str(item.get("archive_reason") or "text_only_archive").strip(),
        "page_count": item.get("page_count") or None,
    }


def archive_sort_key(item: dict[str, Any]) -> tuple[int, int, str, str]:
    rank, date_num, date_text = sort_date_value(str(item.get("date_folder") or ""))
    valid_rank = 0 if rank == 0 else 1
    return (valid_rank, -date_num, date_text, normalize_search_text(str(item.get("title") or "")))


def build_archive_catalog(
    live_catalog: dict[str, Any],
    previous_archive: dict[str, Any],
    bank_catalog_root: Path,
) -> dict[str, Any]:
    updated_at_bjt = str(live_catalog.get("updated_at_bjt") or "")
    live_items = [item for item in live_catalog.get("items", []) if item.get("id")]
    live_lookup = build_title_lookup(live_items)
    archive_by_id: dict[str, dict[str, Any]] = {}

    for item in previous_archive.get("items", []):
        if not isinstance(item, dict):
            continue
        normalized = normalize_archive_item(item, updated_at_bjt)
        if not normalized["id"] or match_report_id(normalized["title"], live_lookup):
            continue
        archive_by_id[normalized["id"]] = normalized

    archive_lookup = build_title_lookup(live_items + list(archive_by_id.values()))
    source_counts = {
        "previous_archive_items": len(archive_by_id),
        "bank_catalog_titles": 0,
        "archive_items_added": 0,
        "archive_items_updated": 0,
        "live_matches_skipped": 0,
    }

    for title, source_path in iter_bank_catalog_titles(bank_catalog_root):
        source_counts["bank_catalog_titles"] += 1
        if match_report_id(title, live_lookup):
            source_counts["live_matches_skipped"] += 1
            continue

        bank_code = Path(source_path).stem or "Archive"
        report_id = match_report_id(title, archive_lookup) or archive_item_id(title, bank_code)
        source_date = source_date_from_path(source_path)
        title_date = trailing_date_from_title(title)
        date_folder = title_date or source_date
        existing = archive_by_id.get(report_id)
        if existing:
            folders = set(existing.get("date_folders") or [])
            if source_date:
                folders.add(source_date)
            if title_date:
                folders.add(title_date)
            existing["date_folders"] = sorted(folders, key=sort_date_value)
            if date_folder:
                existing["date_folder"] = date_folder
            existing["last_seen_at_bjt"] = updated_at_bjt
            source_counts["archive_items_updated"] += 1
            continue

        archive_item = normalize_archive_item({
            "id": report_id,
            "title": title,
            "filename": f"{title}.pdf",
            "date_folder": date_folder,
            "date_folders": [value for value in (source_date, title_date) if value],
            "bank_code": bank_code,
            "bank_name": bank_code,
        }, updated_at_bjt)
        archive_by_id[report_id] = archive_item
        for key in title_keys(title):
            archive_lookup.setdefault(key, report_id)
        source_counts["archive_items_added"] += 1

    archive_items = sorted(archive_by_id.values(), key=archive_sort_key)
    return {
        "schema_version": 1,
        "updated_at_bjt": updated_at_bjt,
        "item_count": len(archive_items),
        "sources": source_counts,
        "items": archive_items,
    }


def catalog_with_archive_items(catalog: dict[str, Any], archive_catalog: dict[str, Any]) -> dict[str, Any]:
    live_items = [item for item in catalog.get("items", []) if item.get("id")]
    live_ids = {str(item.get("id")) for item in live_items}
    live_lookup = build_title_lookup(live_items)
    archive_items: list[dict[str, Any]] = []
    for item in archive_catalog.get("items", []):
        if not isinstance(item, dict):
            continue
        report_id = str(item.get("id") or "")
        if not report_id or report_id in live_ids:
            continue
        if match_report_id(str(item.get("title") or item.get("filename") or ""), live_lookup):
            continue
        archive_items.append({key: item.get(key) for key in PUBLIC_ITEM_KEYS if key in item})
    merged = dict(catalog)
    merged["items"] = live_items + archive_items
    merged["item_count"] = len(merged["items"])
    merged["archive_item_count"] = len(archive_items)
    return merged


def mineru_source_title(item_dir: Path) -> str:
    status_path = item_dir / "status.json"
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
            source_pdf = str(status.get("source_pdf") or "")
            if source_pdf:
                return strip_leading_sequence(strip_extension(Path(source_pdf).name))
        except (OSError, json.JSONDecodeError):
            pass

    markdown_path = item_dir / "source_mineru.md"
    try:
        for line in markdown_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                return stripped.lstrip("#").strip()
            if stripped:
                return stripped[:200]
    except OSError:
        return ""
    return item_dir.name


def iter_mineru_sources(root: Path) -> list[tuple[str, str, str]]:
    if not root.exists():
        return []
    sources: list[tuple[str, str, str]] = []
    for markdown_path in sorted(root.glob("*/shard_*/*/source_mineru.md")):
        item_dir = markdown_path.parent
        title = mineru_source_title(item_dir)
        try:
            text = markdown_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if title and text:
            sources.append((title, text, str(markdown_path)))
    return sources


def build_search_index(
    catalog: dict[str, Any],
    bank_catalog_root: Path,
    mineru_root: Path,
    text_limit: int,
) -> dict[str, Any]:
    items = [item for item in catalog.get("items", []) if item.get("id")]
    lookup = build_title_lookup(items)
    index_text: dict[str, list[str]] = {str(item["id"]): [] for item in items}
    source_counts = {
        "bank_catalog_titles": 0,
        "bank_catalog_matched": 0,
        "mineru_sources": 0,
        "mineru_matched": 0,
    }

    for title, _source_path in iter_bank_catalog_titles(bank_catalog_root):
        source_counts["bank_catalog_titles"] += 1
        report_id = match_report_id(title, lookup)
        if not report_id:
            continue
        source_counts["bank_catalog_matched"] += 1
        append_unique_text(index_text[report_id], title)

    for title, text, _source_path in iter_mineru_sources(mineru_root):
        source_counts["mineru_sources"] += 1
        report_id = match_report_id(title, lookup)
        if not report_id:
            continue
        source_counts["mineru_matched"] += 1
        append_unique_text(index_text[report_id], title)
        append_unique_text(index_text[report_id], text)

    public_items: list[dict[str, str]] = []
    for report_id, chunks in sorted(index_text.items()):
        text = " ".join(chunks).strip()
        if not text:
            continue
        if text_limit > 0 and len(text) > text_limit:
            text = text[:text_limit]
        public_items.append({"id": report_id, "text": text})

    return {
        "schema_version": 1,
        "updated_at_bjt": catalog.get("updated_at_bjt", ""),
        "item_count": len(public_items),
        "sources": source_counts,
        "items": public_items,
    }


def merge_search_indexes(
    previous_index: dict[str, Any],
    current_index: dict[str, Any],
    catalog: dict[str, Any],
) -> dict[str, Any]:
    catalog_ids = {str(item.get("id")) for item in catalog.get("items", []) if item.get("id")}
    previous_by_id = {
        str(item.get("id")): str(item.get("text") or "")
        for item in previous_index.get("items", [])
        if isinstance(item, dict) and item.get("id")
    }
    current_by_id = {
        str(item.get("id")): str(item.get("text") or "")
        for item in current_index.get("items", [])
        if isinstance(item, dict) and item.get("id")
    }

    merged_items: list[dict[str, str]] = []
    for report_id in sorted(catalog_ids):
        chunks: list[str] = []
        append_unique_text(chunks, previous_by_id.get(report_id, ""))
        append_unique_text(chunks, current_by_id.get(report_id, ""))
        text = " ".join(chunks).strip()
        if text:
            merged_items.append({"id": report_id, "text": text})

    sources = dict(current_index.get("sources") or {})
    sources["previous_search_entries"] = len(previous_by_id)
    sources["previous_search_entries_kept"] = sum(1 for report_id in previous_by_id if report_id in catalog_ids)
    return {
        "schema_version": 1,
        "updated_at_bjt": current_index.get("updated_at_bjt") or catalog.get("updated_at_bjt", ""),
        "item_count": len(merged_items),
        "sources": sources,
        "items": merged_items,
    }


def search_index_size_bytes(index: dict[str, Any]) -> int:
    return len(json.dumps(index, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def limit_search_index_by_size(
    index: dict[str, Any],
    catalog: dict[str, Any],
    limit_bytes: int,
) -> dict[str, Any]:
    if limit_bytes <= 0:
        index["text_storage_limit_bytes"] = 0
        index["text_storage_size_bytes"] = search_index_size_bytes(index)
        index["text_pruned_dates"] = []
        return index

    id_to_date = {
        str(item.get("id")): str(item.get("date_folder") or "")
        for item in catalog.get("items", [])
        if item.get("id")
    }
    items = list(index.get("items", []))
    pruned_dates: list[str] = []

    candidate_index = dict(index)
    candidate_index["items"] = items
    while items and search_index_size_bytes(candidate_index) > limit_bytes:
        dates = sorted({id_to_date.get(str(item.get("id")), "") for item in items}, key=sort_date_value)
        oldest = dates[0]
        pruned_dates.append(oldest)
        items = [item for item in items if id_to_date.get(str(item.get("id")), "") != oldest]
        candidate_index = dict(index)
        candidate_index["items"] = items
        candidate_index["item_count"] = len(items)
        candidate_index["text_pruned_dates"] = pruned_dates

    candidate_index["item_count"] = len(items)
    candidate_index["text_storage_limit_bytes"] = limit_bytes
    candidate_index["text_storage_size_bytes"] = search_index_size_bytes(candidate_index)
    candidate_index["text_pruned_dates"] = pruned_dates
    return candidate_index


def sort_date_value(value: str) -> tuple[int, int, str]:
    text = str(value or "")
    match = re.fullmatch(r"\d{6}", text)
    if match:
        return 0, int(f"20{text}"), text
    match = re.fullmatch(r"\d{8}", text)
    if match:
        return 0, int(text), text
    return 1, 0, text


def merge_history_catalog(
    catalog: dict[str, Any],
    history_catalog_path: Path,
    history_text_dir: Path,
) -> tuple[dict[str, Any], dict[str, str], dict[str, int]]:
    """Merge the one-time ib_rpt_history import into the public catalog.

    History reports that title-match a live Dropbox report are dropped from the
    catalog (the live record wins, it may still have a PDF) and their search
    text is re-attached to the live report id instead. Runs before the archive
    catalog merge so archive title records duplicating history are also skipped.
    """
    stats = {"history_total": 0, "history_deduped": 0, "history_added": 0, "history_texts": 0}
    if not history_catalog_path.exists():
        return catalog, {}, stats

    history = load_json_default(history_catalog_path, {"items": []})
    live_items = [item for item in catalog.get("items", []) if item.get("id")]
    history_items = [item for item in history.get("items", []) if item.get("id")]
    stats["history_total"] = len(history_items)

    lookup = build_title_lookup(live_items)
    id_remap: dict[str, str] = {}
    added_items: list[dict[str, Any]] = []
    for item in history_items:
        live_id = match_report_id(str(item.get("title") or ""), lookup)
        if live_id:
            id_remap[str(item["id"])] = live_id
        else:
            added_items.append({key: item.get(key) for key in PUBLIC_ITEM_KEYS if key in item})
    stats["history_deduped"] = len(id_remap)
    stats["history_added"] = len(added_items)

    merged = dict(catalog)
    merged_items = live_items + added_items
    merged_items.sort(
        key=lambda item: (str(item.get("date_folder") or ""), str(item.get("title") or "").lower()),
        reverse=True,
    )
    merged["items"] = merged_items
    merged["item_count"] = len(merged_items)

    texts: dict[str, str] = {}
    if history_text_dir.exists():
        for shard_path in sorted(history_text_dir.glob("shard_*.json.gz")):
            mapping = json.loads(gzip.decompress(shard_path.read_bytes()).decode("utf-8"))
            for history_id, text in mapping.items():
                if not text:
                    continue
                target = id_remap.get(str(history_id), str(history_id))
                existing = texts.get(target)
                if existing:
                    if text not in existing:
                        texts[target] = f"{existing} {text}"
                else:
                    texts[target] = text
    stats["history_texts"] = len(texts)
    return merged, texts, stats


def build_history_search_index(
    catalog: dict[str, Any],
    texts: dict[str, str],
    limit_bytes: int,
) -> dict[str, Any]:
    index = {
        "schema_version": 1,
        "updated_at_bjt": catalog.get("updated_at_bjt", ""),
        "item_count": len(texts),
        "items": [{"id": report_id, "text": text} for report_id, text in sorted(texts.items())],
    }
    return limit_search_index_by_size(index=index, catalog=catalog, limit_bytes=limit_bytes)


def write_history_search_shards(
    history_index: dict[str, Any],
    catalog: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    """Split the size-capped history text index into per-month shard files.

    The browser loads the manifest lazily and then streams shards newest-first,
    so the initial page load never downloads the history text at all. The
    Worker keeps loading only the small search_index.json.
    """
    id_to_month: dict[str, str] = {}
    for item in catalog.get("items", []):
        report_id = str(item.get("id") or "")
        if report_id:
            id_to_month[report_id] = str(item.get("date_folder") or "")[:4] or "0000"

    groups: dict[str, list[dict[str, str]]] = {}
    for entry in history_index.get("items", []):
        month = id_to_month.get(str(entry.get("id")), "0000")
        groups.setdefault(month, []).append(entry)

    output_dir.mkdir(parents=True, exist_ok=True)
    shards: list[dict[str, Any]] = []
    for month in sorted(groups, reverse=True):
        filename = f"shard_{month}.json"
        payload = json.dumps({"items": groups[month]}, ensure_ascii=False, separators=(",", ":"))
        shard_path = output_dir / filename
        shard_path.write_text(payload, encoding="utf-8")
        shards.append({
            "file": filename,
            "month": month,
            "item_count": len(groups[month]),
            "bytes": len(payload.encode("utf-8")),
        })

    manifest = {
        "schema_version": 1,
        "updated_at_bjt": history_index.get("updated_at_bjt", ""),
        "item_count": history_index.get("item_count", 0),
        "text_storage_limit_bytes": history_index.get("text_storage_limit_bytes", 0),
        "text_storage_size_bytes": history_index.get("text_storage_size_bytes", 0),
        "text_pruned_dates": history_index.get("text_pruned_dates", []),
        "total_bytes": sum(shard["bytes"] for shard in shards),
        "shards": shards,
    }
    write_json(output_dir / "manifest.json", manifest)
    return manifest


def public_catalog(catalog: dict[str, Any]) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    for item in catalog.get("items", []):
        public_item = {key: item.get(key) for key in PUBLIC_ITEM_KEYS if key in item}
        items.append(public_item)
    total_size_bytes = catalog.get("total_size_bytes")
    if not total_size_bytes:
        total_size_bytes = sum(int(item.get("size_bytes") or 0) for item in items)
    public = {
        "schema_version": catalog.get("schema_version", 1),
        "updated_at_bjt": catalog.get("updated_at_bjt", ""),
        "dropbox_root": catalog.get("dropbox_root", ""),
        "item_count": len(items),
        "total_size_bytes": total_size_bytes,
        "storage_limit_bytes": catalog.get("storage_limit_bytes", 0),
        "items": items,
    }
    storage = catalog.get("storage")
    if isinstance(storage, dict):
        public["storage"] = {
            "limit_bytes": storage.get("limit_bytes", 0),
            "total_size_bytes": storage.get("total_size_bytes", public["total_size_bytes"]),
            "last_pruned_at_bjt": storage.get("last_pruned_at_bjt", ""),
            "pdf_pruned_this_run_count": storage.get("pdf_pruned_this_run_count", storage.get("pruned_this_run_count", 0)),
            "pdf_pruned_this_run_size_bytes": storage.get("pdf_pruned_this_run_size_bytes", storage.get("pruned_this_run_size_bytes", 0)),
            "pdf_pruned_this_run_dates": storage.get("pdf_pruned_this_run_dates", storage.get("pruned_this_run_dates", [])),
        }
    return public


def public_password_rules(rules: dict[str, Any]) -> dict[str, Any]:
    groups = []
    for group in rules.get("groups", []):
        password_hash = group.get("password_sha256")
        if password_hash == "REPLACE_WITH_SHA256_HASH":
            password_secret = os.getenv("PASSWORD_SECRET", "")
            download_password = os.getenv("KC_DESK_DOWNLOAD_PASSWORD", "")
            if password_secret and download_password:
                password_hash = hashlib.sha256(f"{password_secret}:{download_password}".encode("utf-8")).hexdigest()
        groups.append({
            "id": group.get("id"),
            "label": group.get("label"),
            "password_sha256": password_hash,
            "active": bool(group.get("active", True)),
        })
    return {
        "schema_version": rules.get("schema_version", 1),
        "hash_rule": rules.get("hash_rule", "sha256(PASSWORD_SECRET + ':' + plain_password)"),
        "default_group": rules.get("default_group", "default"),
        "groups": groups,
    }


def date_folder_to_iso(value: str) -> str:
    text = str(value or "").strip()
    if re.fullmatch(r"\d{6}", text):
        return f"20{text[:2]}-{text[2:4]}-{text[4:6]}"
    if re.fullmatch(r"20\d{6}", text):
        return f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", text):
        return text
    return ""


def bjt_timestamp_to_date(value: str) -> str:
    match = re.search(r"(20\d{2})-(\d{2})-(\d{2})", str(value or ""))
    return f"{match.group(1)}-{match.group(2)}-{match.group(3)}" if match else ""


def item_lastmod(item: dict[str, Any], fallback: str = "") -> str:
    return (
        bjt_timestamp_to_date(str(item.get("server_modified") or ""))
        or date_folder_to_iso(str(item.get("date_folder") or ""))
        or bjt_timestamp_to_date(str(item.get("first_seen_at_bjt") or ""))
        or bjt_timestamp_to_date(str(item.get("last_seen_at_bjt") or ""))
        or fallback
    )


def xml_escape(value: str) -> str:
    return html_escape(str(value or ""), quote=True)


def url_join(base_url: str, path: str) -> str:
    base = base_url.rstrip("/") or SITE_BASE_URL
    clean = "/" + str(path or "").lstrip("/")
    return f"{base}{clean}"


def report_seo_path(report_id: str) -> str:
    return f"reports/{quote(str(report_id), safe='')}.html"


def item_display_title(item: dict[str, Any]) -> str:
    return compact_space(str(item.get("title_zh") or item.get("title") or item.get("filename") or "研究报告"))


def item_source_title(item: dict[str, Any]) -> str:
    title = compact_space(str(item.get("title") or item.get("filename") or ""))
    return strip_extension(title)


def item_institution(item: dict[str, Any]) -> str:
    bank_code = compact_space(str(item.get("bank_code") or ""))
    bank_name = compact_space(str(item.get("bank_name") or ""))
    if bank_code and bank_name and normalize_search_text(bank_code) != normalize_search_text(bank_name):
        return f"{bank_code} · {bank_name}"
    return bank_name or bank_code or "研究机构"


def item_industry(item: dict[str, Any]) -> str:
    return compact_space(str(item.get("industry") or item.get("sector") or item.get("category") or "综合研究"))


def item_page_label(item: dict[str, Any]) -> str:
    page_count = item.get("page_count")
    try:
        count = int(page_count)
    except (TypeError, ValueError):
        return "页数待识别"
    return f"{count}页"


def item_availability_label(item: dict[str, Any]) -> str:
    if item.get("available") and not item.get("pdf_archived"):
        return "PDF可用"
    return "文字索引可检索，原文请联系 MacroGate"


def item_meta_description(item: dict[str, Any]) -> str:
    title = item_display_title(item)
    institution = item_institution(item)
    industry = item_industry(item)
    report_date = date_folder_to_iso(str(item.get("date_folder") or "")) or str(item.get("date_folder") or "")
    return compact_space(
        f"{institution}报告《{title}》，研究主题为{industry}，发布日期为{report_date}，"
        f"{item_page_label(item)}。{item_availability_label(item)}。"
        "KC Desk Notes 提供中文标题、英文标题、报告信息和相关研究索引。"
    )[:280]


def item_summary(item: dict[str, Any]) -> str:
    report_date = date_folder_to_iso(str(item.get("date_folder") or "")) or str(item.get("date_folder") or "")
    return compact_space(
        f"本报告由{item_institution(item)}发布，聚焦{item_industry(item)}，"
        f"发布日期为{report_date}，{item_page_label(item)}。"
        "本页整理中英文标题、研究机构、主题分类、页数和可用状态，便于中文检索及相关研究发现。"
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def render_json_ld(data: dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def report_keywords(item: dict[str, Any]) -> str:
    values = [
        item_institution(item),
        item_industry(item),
        str(item.get("bank_code") or ""),
        str(item.get("bank_name") or ""),
        str(item.get("title_zh") or ""),
        str(item.get("title") or ""),
        "金融研报",
        "宏观策略",
        "行业研究",
        "公司研究",
    ]
    seen: set[str] = set()
    keywords: list[str] = []
    for value in values:
        clean = compact_space(value)
        key = normalize_search_text(clean)
        if clean and key and key not in seen:
            keywords.append(clean)
            seen.add(key)
    return ", ".join(keywords[:12])


def render_report_seo_page(
    item: dict[str, Any],
    base_url: str,
    generated_date: str,
    related_items: list[dict[str, Any]] | None = None,
) -> str:
    report_id = str(item.get("id") or "")
    title = item_display_title(item)
    source_title = item_source_title(item)
    canonical = url_join(base_url, report_seo_path(report_id))
    detail_href = f"../report.html?id={quote(report_id, safe='')}"
    search_href = f"../?q={quote(title[:80])}"
    description = item_meta_description(item)
    date_iso = date_folder_to_iso(str(item.get("date_folder") or ""))
    lastmod = item_lastmod(item, generated_date)
    institution = item_institution(item)
    industry = item_industry(item)
    report_json_ld = {
        "@type": "Report",
        "@id": f"{canonical}#report",
        "name": title,
        "headline": title,
        "alternateName": source_title,
        "description": description,
        "url": canonical,
        "mainEntityOfPage": canonical,
        "identifier": report_id,
        "datePublished": date_iso or lastmod,
        "dateModified": lastmod,
        "inLanguage": ["zh-CN", "en"],
        "genre": "金融研究报告",
        "keywords": report_keywords(item),
        "publisher": {
            "@type": "Organization",
            "name": "KC Desk Notes",
            "url": url_join(base_url, "/"),
        },
        "about": [industry, institution],
        "isAccessibleForFree": False,
    }
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            report_json_ld,
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "首页", "item": url_join(base_url, "/")},
                    {"@type": "ListItem", "position": 2, "name": "报告索引", "item": url_join(base_url, "reports/")},
                    {"@type": "ListItem", "position": 3, "name": title, "item": canonical},
                ],
            },
        ],
    }
    if source_title and source_title != title:
        source_block = f"""
          <h2>英文标题</h2>
          <p>{html_escape(source_title)}</p>"""
    else:
        source_block = ""
    related_rows = []
    for related in related_items or []:
        related_id = str(related.get("id") or "")
        if not related_id:
            continue
        related_rows.append(
            "<li>"
            f"<a href=\"{html_escape(quote(related_id, safe='') + '.html')}\">{html_escape(item_display_title(related))}</a>"
            f"<span>{html_escape(item_institution(related))} · {html_escape(item_lastmod(related))}</span>"
            "</li>"
        )
    related_block = ""
    if related_rows:
        related_block = (
            "<h2>相关报告</h2>"
            '<ul class="seo-report-index seo-related-reports">'
            + "".join(related_rows)
            + "</ul>"
        )
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html_escape(title)} | KC Desk Notes</title>
    <meta name="description" content="{html_escape(description)}">
    <meta name="keywords" content="{html_escape(report_keywords(item))}">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
    <link rel="canonical" href="{html_escape(canonical)}">
    <link rel="alternate" hreflang="zh-CN" href="{html_escape(canonical)}">
    <link rel="alternate" hreflang="x-default" href="{html_escape(canonical)}">
    <link rel="alternate" type="application/rss+xml" title="KC Desk Notes 最近报告" href="../feed.xml">
    <meta property="og:type" content="article">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="KC Desk Notes">
    <meta property="og:title" content="{html_escape(title)}">
    <meta property="og:description" content="{html_escape(description)}">
    <meta property="og:url" content="{html_escape(canonical)}">
    <link rel="stylesheet" href="../assets/styles.css">
    <script type="application/ld+json">{render_json_ld(json_ld)}</script>
  </head>
  <body>
    <header class="topbar">
      <a class="back-link" href="../index.html">返回首页</a>
      <a class="brand compact" href="../index.html" aria-label="KC Desk Notes home">
        <img src="../assets/kc-mark.svg" alt="" width="30" height="30">
        <span>KC Desk Notes</span>
      </a>
    </header>
    <main class="shell legal-shell">
      <article class="legal-panel">
        <h1>{html_escape(title)}</h1>
        <p class="subtle">{html_escape(description)}</p>
        <h2>研究摘要</h2>
        <p>{html_escape(item_summary(item))}</p>
        <h2>报告信息</h2>
        <p>机构：{html_escape(institution)}</p>
        <p>行业：{html_escape(industry)}</p>
        <p>日期：{html_escape(date_iso or str(item.get("date_folder") or ""))}</p>
        <p>页数：{html_escape(item_page_label(item))}</p>
        <p>状态：{html_escape(item_availability_label(item))}</p>{source_block}
        <p>
          <a class="primary-link" href="{html_escape(detail_href)}">打开报告详情</a>
          <a class="secondary-button" href="{html_escape(search_href)}">检索相关报告</a>
        </p>{related_block}
      </article>
    </main>
    <footer class="legal-footer">
      <a href="../reports/index.html">报告索引</a>
      <a href="../terms.html">Terms of Service</a>
      <a href="../privacy.html">Privacy Policy</a>
      <span>Contact: MacroGate</span>
    </footer>
  </body>
</html>
"""


def render_reports_index(catalog: dict[str, Any], base_url: str, generated_date: str) -> str:
    items = [item for item in catalog.get("items", []) if item.get("id")]
    sorted_items = sorted(
        items,
        key=lambda row: (
            sort_date_value(str(row.get("date_folder") or "")),
            normalize_search_text(item_display_title(row)),
        ),
        reverse=True,
    )
    rows = []
    for item in sorted_items:
        href = f"{quote(str(item.get('id')), safe='')}.html"
        date_iso = date_folder_to_iso(str(item.get("date_folder") or ""))
        rows.append(
            "<li>"
            f"<a href=\"{html_escape(href)}\">{html_escape(item_display_title(item))}</a>"
            f"<span>{html_escape(item_institution(item))} · {html_escape(date_iso or str(item.get('date_folder') or ''))} · {html_escape(item_industry(item))}</span>"
            "</li>"
        )
    description = "KC Desk Notes 中文金融研报索引，覆盖宏观策略、行业分析、公司研究、财报、招股书和国际智库报告线索。"
    collection_json_ld = {
        "@type": "CollectionPage",
        "@id": f"{url_join(base_url, 'reports/')}#collection",
        "name": "KC Desk Notes 报告索引",
        "description": description,
        "url": url_join(base_url, "reports/"),
        "dateModified": generated_date,
        "inLanguage": "zh-CN",
    }
    item_list = {
        "@type": "ItemList",
        "name": "最新金融研报",
        "numberOfItems": len(items),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": item_display_title(item),
                "url": url_join(base_url, report_seo_path(str(item.get("id")))),
            }
            for index, item in enumerate(sorted_items[:50], start=1)
        ],
    }
    json_ld = {"@context": "https://schema.org", "@graph": [collection_json_ld, item_list]}
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>金融研报索引 | KC Desk Notes</title>
    <meta name="description" content="{html_escape(description)}">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
    <link rel="canonical" href="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="alternate" hreflang="zh-CN" href="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="alternate" hreflang="x-default" href="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="alternate" type="application/rss+xml" title="KC Desk Notes 最近报告" href="../feed.xml">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="KC Desk Notes">
    <meta property="og:title" content="金融研报索引 | KC Desk Notes">
    <meta property="og:description" content="{html_escape(description)}">
    <meta property="og:url" content="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="stylesheet" href="../assets/styles.css">
    <script type="application/ld+json">{render_json_ld(json_ld)}</script>
  </head>
  <body>
    <header class="topbar">
      <a class="back-link" href="../index.html">返回首页</a>
      <a class="brand compact" href="../index.html" aria-label="KC Desk Notes home">
        <img src="../assets/kc-mark.svg" alt="" width="30" height="30">
        <span>KC Desk Notes</span>
      </a>
    </header>
    <main class="shell legal-shell">
      <section class="legal-panel">
        <h1>金融研报索引</h1>
        <p class="subtle">{html_escape(description)}</p>
        <p class="subtle">已更新：{html_escape(generated_date)} · 共 {len(items)} 篇</p>
        <ul class="seo-report-index">
          {"".join(rows)}
        </ul>
      </section>
    </main>
    <footer class="legal-footer">
      <a href="../index.html">首页检索</a>
      <a href="../feed.xml">最近报告 RSS</a>
      <a href="../terms.html">Terms of Service</a>
      <a href="../privacy.html">Privacy Policy</a>
      <span>Contact: MacroGate</span>
    </footer>
  </body>
</html>
"""


def sitemap_url(loc: str, lastmod: str = "", priority: str = "") -> str:
    pieces = ["  <url>", f"    <loc>{xml_escape(loc)}</loc>"]
    if lastmod:
        pieces.append(f"    <lastmod>{xml_escape(lastmod)}</lastmod>")
    if priority:
        pieces.append(f"    <priority>{xml_escape(priority)}</priority>")
    pieces.append("  </url>")
    return "\n".join(pieces)


def write_urlset(path: Path, rows: list[str]) -> None:
    write_text(
        path,
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        + "\n".join(rows)
        + "\n</urlset>\n",
    )


def build_related_reports(items: list[dict[str, Any]], limit: int = 6) -> dict[str, list[dict[str, Any]]]:
    sorted_items = sorted(
        items,
        key=lambda item: (item_lastmod(item), sort_date_value(str(item.get("date_folder") or ""))),
        reverse=True,
    )
    institution_buckets: dict[str, list[dict[str, Any]]] = {}
    industry_buckets: dict[str, list[dict[str, Any]]] = {}
    for item in sorted_items:
        institution_buckets.setdefault(normalize_search_text(item_institution(item)), []).append(item)
        industry_buckets.setdefault(normalize_search_text(item_industry(item)), []).append(item)

    related: dict[str, list[dict[str, Any]]] = {}
    for item in sorted_items:
        report_id = str(item.get("id") or "")
        candidates: dict[str, dict[str, Any]] = {}
        institution_key = normalize_search_text(item_institution(item))
        industry_key = normalize_search_text(item_industry(item))
        for candidate in institution_buckets.get(institution_key, [])[:40]:
            candidate_id = str(candidate.get("id") or "")
            if candidate_id and candidate_id != report_id:
                candidates[candidate_id] = candidate
        for candidate in industry_buckets.get(industry_key, [])[:40]:
            candidate_id = str(candidate.get("id") or "")
            if candidate_id and candidate_id != report_id:
                candidates[candidate_id] = candidate

        def relation_key(candidate: dict[str, Any]) -> tuple[int, int, str]:
            score = 0
            if normalize_search_text(item_institution(candidate)) == institution_key:
                score += 4
            if normalize_search_text(item_industry(candidate)) == industry_key:
                score += 3
            if candidate.get("available") and not candidate.get("pdf_archived"):
                score += 1
            return score, sort_date_value(str(candidate.get("date_folder") or "")), item_lastmod(candidate)

        related[report_id] = sorted(candidates.values(), key=relation_key, reverse=True)[:limit]
    return related


def rss_pub_date(value: str) -> str:
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        parsed = datetime.now(timezone.utc)
    return format_datetime(parsed)


def render_report_feed(catalog: dict[str, Any], base_url: str, generated_date: str) -> str:
    items = sorted(
        [item for item in catalog.get("items", []) if item.get("id")],
        key=lambda item: (item_lastmod(item, generated_date), sort_date_value(str(item.get("date_folder") or ""))),
        reverse=True,
    )[:RSS_ITEM_LIMIT]
    rows = []
    for item in items:
        canonical = url_join(base_url, report_seo_path(str(item.get("id"))))
        rows.append(
            "    <item>\n"
            f"      <title>{xml_escape(item_display_title(item))}</title>\n"
            f"      <link>{xml_escape(canonical)}</link>\n"
            f"      <guid isPermaLink=\"true\">{xml_escape(canonical)}</guid>\n"
            f"      <pubDate>{xml_escape(rss_pub_date(item_lastmod(item, generated_date)))}</pubDate>\n"
            f"      <description>{xml_escape(item_meta_description(item))}</description>\n"
            f"      <category>{xml_escape(item_institution(item))}</category>\n"
            f"      <category>{xml_escape(item_industry(item))}</category>\n"
            "    </item>"
        )
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\">\n"
        "  <channel>\n"
        "    <title>KC Desk Notes 最近报告</title>\n"
        f"    <link>{xml_escape(url_join(base_url, '/'))}</link>\n"
        "    <description>中文金融研报、宏观策略、行业研究和国际智库报告的最近更新。</description>\n"
        "    <language>zh-CN</language>\n"
        f"    <lastBuildDate>{xml_escape(rss_pub_date(generated_date))}</lastBuildDate>\n"
        f"    <atom:link href=\"{xml_escape(url_join(base_url, 'feed.xml'))}\" rel=\"self\" type=\"application/rss+xml\" />\n"
        + "\n".join(rows)
        + "\n  </channel>\n</rss>\n"
    )


def render_llms_full(catalog: dict[str, Any], base_url: str) -> str:
    items = sorted(
        [item for item in catalog.get("items", []) if item.get("id")],
        key=lambda item: (item_lastmod(item), sort_date_value(str(item.get("date_folder") or ""))),
        reverse=True,
    )[:LLMS_REPORT_LIMIT]
    lines = [
        "# KC Desk Notes 公开报告索引",
        "",
        "以下是最近更新的中文金融研究报告元数据。报告下载权限与公开索引相互独立。",
        "",
    ]
    for item in items:
        lines.extend([
            f"## {item_display_title(item)}",
            f"- URL: {url_join(base_url, report_seo_path(str(item.get('id'))))}",
            f"- 机构: {item_institution(item)}",
            f"- 主题: {item_industry(item)}",
            f"- 日期: {item_lastmod(item)}",
            f"- 摘要: {item_summary(item)}",
            "",
        ])
    return "\n".join(lines)


def build_seo_outputs(output: Path, catalog: dict[str, Any], base_url: str = SITE_BASE_URL) -> None:
    base_url = base_url.rstrip("/") or SITE_BASE_URL
    generated_date = bjt_timestamp_to_date(str(catalog.get("updated_at_bjt") or "")) or ""
    reports_dir = output / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_items = sorted(
        [item for item in catalog.get("items", []) if item.get("id")],
        key=lambda item: (item_lastmod(item, generated_date), sort_date_value(str(item.get("date_folder") or ""))),
        reverse=True,
    )
    related_reports = build_related_reports(report_items)

    for item in report_items:
        report_id = str(item.get("id") or "")
        write_text(
            reports_dir / f"{quote(report_id, safe='')}.html",
            render_report_seo_page(item, base_url, generated_date, related_reports.get(report_id, [])),
        )
    write_text(reports_dir / "index.html", render_reports_index(catalog, base_url, generated_date))

    page_rows = [
        sitemap_url(url_join(base_url, "/"), generated_date, "1.0"),
        sitemap_url(url_join(base_url, "reports/"), generated_date, "0.9"),
        sitemap_url(url_join(base_url, "terms.html"), generated_date, "0.2"),
        sitemap_url(url_join(base_url, "privacy.html"), generated_date, "0.2"),
    ]
    write_urlset(output / "sitemap-pages.xml", page_rows)

    sitemap_names = ["sitemap-pages.xml"]
    for index in range(0, len(report_items), SITEMAP_REPORT_CHUNK_SIZE):
        chunk = report_items[index:index + SITEMAP_REPORT_CHUNK_SIZE]
        sitemap_name = f"sitemap-reports-{index // SITEMAP_REPORT_CHUNK_SIZE + 1}.xml"
        sitemap_names.append(sitemap_name)
        rows = [
            sitemap_url(
                url_join(base_url, report_seo_path(str(item.get("id")))),
                item_lastmod(item, generated_date),
                "0.8" if item.get("available") else "0.6",
            )
            for item in chunk
        ]
        write_urlset(output / sitemap_name, rows)

    sitemap_index_rows = []
    for name in sitemap_names:
        sitemap_index_rows.append(
            "  <sitemap>\n"
            f"    <loc>{xml_escape(url_join(base_url, name))}</loc>\n"
            f"    <lastmod>{xml_escape(generated_date)}</lastmod>\n"
            "  </sitemap>"
        )
    write_text(
        output / "sitemap.xml",
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<sitemapindex xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        + "\n".join(sitemap_index_rows)
        + "\n</sitemapindex>\n",
    )

    # Baidu no longer accepts sitemap index files. A single flat file also works
    # well for Sogou and remains under the 50,000 URL / 10 MB limits.
    cn_rows = list(page_rows)
    cn_rows.extend(
        sitemap_url(
            url_join(base_url, report_seo_path(str(item.get("id")))),
            item_lastmod(item, generated_date),
            "0.8" if item.get("available") else "0.6",
        )
        for item in report_items
    )
    write_urlset(output / "sitemap-baidu.xml", cn_rows)
    write_urlset(output / "sitemap-sogou.xml", cn_rows)
    write_text(output / "feed.xml", render_report_feed(catalog, base_url, generated_date))

    indexnow_key = compact_space(os.environ.get("INDEXNOW_KEY") or INDEXNOW_KEY)
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", indexnow_key):
        raise ValueError("INDEXNOW_KEY must be 8-128 ASCII letters, digits, or hyphens")
    write_text(output / f"{indexnow_key}.txt", f"{indexnow_key}\n")

    restricted_rules = [
        "Disallow: /api/",
        "Disallow: /data/",
        "Allow: /data/catalog.json",
        "Disallow: /delivery.html",
        "Disallow: /newsfeed.html",
    ]
    robots_lines: list[str] = []
    for agent in ("*", "OAI-SearchBot", "PerplexityBot"):
        robots_lines.extend([f"User-agent: {agent}", "Allow: /", *restricted_rules, ""])
    robots_lines.extend([
        f"Sitemap: {url_join(base_url, 'sitemap.xml')}",
        f"Sitemap: {url_join(base_url, 'sitemap-baidu.xml')}",
        f"Sitemap: {url_join(base_url, 'sitemap-sogou.xml')}",
        f"Sitemap: {url_join(base_url, 'feed.xml')}",
        "",
    ])
    write_text(
        output / "robots.txt",
        "\n".join(robots_lines),
    )
    write_text(
        output / "llms.txt",
        "\n".join([
            "# KC Desk Notes",
            "",
            "KC Desk Notes 是中文金融研究报告检索与索引站点，覆盖宏观策略、行业分析、公司研究、财报、招股书、国际智库和市场观点。",
            "",
            "## Primary URLs",
            f"- Home/Search: {url_join(base_url, '/')}",
            f"- Report index: {url_join(base_url, 'reports/')}",
            f"- Sitemap index: {url_join(base_url, 'sitemap.xml')}",
            f"- Recent reports RSS: {url_join(base_url, 'feed.xml')}",
            f"- Expanded public report metadata: {url_join(base_url, 'llms-full.txt')}",
            f"- Public catalog JSON: {url_join(base_url, 'data/catalog.json')}",
            "",
            "## Content Notes",
            "- Preferred language for summaries: zh-CN.",
            "- Report pages expose titles, translated titles, institution, industry, date, page count, and availability status.",
            "- PDF download access may require an approved account. For source files or unavailable PDFs, contact WeChat MacroGate.",
            "",
        ]),
    )
    write_text(output / "llms-full.txt", render_llms_full(catalog, base_url))


def copy_site(src: Path, output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(src, output)


def version_assets(output: Path) -> None:
    """Append a content-hash query to app.js / styles.css links in every HTML file.

    kcdesk.com is fronted by Cloudflare, which caches these assets for hours, so an
    unversioned `assets/app.js` keeps serving stale JS after a deploy. Hashing the
    URL (`assets/app.js?v=<hash>`) makes each change a new cache key, so deploys take
    effect immediately. Only busts when the file content actually changes.
    """
    versions: dict[str, str] = {}
    for rel in ("assets/app.js", "assets/styles.css"):
        path = output / rel
        if path.exists():
            versions[rel] = hashlib.sha1(path.read_bytes()).hexdigest()[:8]
    if not versions:
        return
    for html_path in output.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        for rel, digest in versions.items():
            for prefix in ("", "../"):
                href = f"{prefix}{rel}"
                pattern = re.compile(rf'(["\']){re.escape(href)}(?:\?v=[^"\']*)?\1')
                text = pattern.sub(lambda match, href=href: f"{match.group(1)}{href}?v={digest}{match.group(1)}", text)
        html_path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-src", default="kc_desk_notes/site_src")
    parser.add_argument("--output-dir", default="_kc_desk_notes_pages")
    parser.add_argument("--catalog-path", default="kc_desk_notes/data/catalog.json")
    parser.add_argument("--archive-catalog-path", default="kc_desk_notes/data/archive_catalog.json")
    parser.add_argument("--search-index-path", default="kc_desk_notes/data/search_index.json")
    parser.add_argument("--password-rules", default="kc_desk_notes/password_rules.json")
    parser.add_argument("--worker-base-url", default="")
    parser.add_argument("--bank-catalog-root", default="bank_report_catalogs")
    parser.add_argument("--mineru-root", default="xhs_notes/dropbox")
    parser.add_argument("--search-text-limit", type=int, default=0, help="Per-report normalized search text cap. 0 keeps all matched text.")
    parser.add_argument(
        "--search-index-limit-gb",
        type=float,
        default=2,
        help="Maximum public text index size in GiB. Oldest date folders are removed from the text index if exceeded. 0 disables.",
    )
    parser.add_argument("--history-catalog", default="kc_desk_notes/data/history_catalog.json")
    parser.add_argument("--history-text-dir", default="kc_desk_notes/data/history_text")
    parser.add_argument(
        "--history-index-limit-gb",
        type=float,
        default=0.06,
        help="Maximum browser-only history text index size in GiB. Oldest date folders lose their"
        " body text first (titles stay searchable via the catalog). 0 disables.",
    )
    args = parser.parse_args()

    site_src = Path(args.site_src)
    output_dir = Path(args.output_dir)
    copy_site(site_src, output_dir)

    catalog = public_catalog(load_json(Path(args.catalog_path)))
    catalog, history_texts, history_stats = merge_history_catalog(
        catalog=catalog,
        history_catalog_path=Path(args.history_catalog),
        history_text_dir=Path(args.history_text_dir),
    )
    archive_catalog_path = Path(args.archive_catalog_path)
    archive_catalog = build_archive_catalog(
        live_catalog=catalog,
        previous_archive=load_json_default(archive_catalog_path, {"items": []}),
        bank_catalog_root=Path(args.bank_catalog_root),
    )
    catalog = catalog_with_archive_items(catalog, archive_catalog)
    current_search_index = build_search_index(
        catalog=catalog,
        bank_catalog_root=Path(args.bank_catalog_root),
        mineru_root=Path(args.mineru_root),
        text_limit=args.search_text_limit,
    )
    search_index_path = Path(args.search_index_path)
    search_index = merge_search_indexes(
        previous_index=load_json_default(search_index_path, {"items": []}),
        current_index=current_search_index,
        catalog=catalog,
    )
    search_index = limit_search_index_by_size(
        index=search_index,
        catalog=catalog,
        limit_bytes=int(args.search_index_limit_gb * 1024 * 1024 * 1024),
    )
    history_index = build_history_search_index(
        catalog=catalog,
        texts=history_texts,
        limit_bytes=int(args.history_index_limit_gb * 1024 * 1024 * 1024),
    )
    history_manifest = write_history_search_shards(
        history_index=history_index,
        catalog=catalog,
        output_dir=output_dir / "data" / "search_index_history",
    )
    rules = public_password_rules(load_json(Path(args.password_rules)))
    write_json(output_dir / "data" / "catalog.json", catalog)
    write_json(output_dir / "data" / "search_index.json", search_index)
    write_json(output_dir / "data" / "password_rules.json", rules)
    write_json(output_dir / "data" / "config.json", {"worker_base_url": args.worker_base_url.rstrip("/")})
    write_json(archive_catalog_path, archive_catalog)
    write_json(search_index_path, search_index)
    build_seo_outputs(output_dir, catalog, SITE_BASE_URL)
    version_assets(output_dir)
    print(
        f"Built {output_dir} with {catalog['item_count']} catalog items "
        f"({history_stats['history_added']} history-only, {history_stats['history_deduped']} history deduped) "
        f"and {search_index['item_count']} full-text search entries, "
        f"{history_index['item_count']} history text entries in {len(history_manifest['shards'])} lazy shards "
        f"({history_manifest['total_bytes'] / 1e6:.1f} MB)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
