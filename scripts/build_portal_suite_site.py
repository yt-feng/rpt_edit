#!/usr/bin/env python3
"""Build the static Portal Suite Pages artifact."""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime
import gzip
import hashlib
from html import escape as html_escape, unescape as html_unescape
from html.parser import HTMLParser
import json
import os
import re
import shutil
import tempfile
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit


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
    "industry",
    "sector",
    "category",
    "pdf_archived",
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

SITE_BASE_URL = "https://portal.example.invalid"
SITEMAP_REPORT_CHUNK_SIZE = 5000
INDEXNOW_KEY = "portal-index-key"
RSS_ITEM_LIMIT = 100
LLMS_REPORT_LIMIT = 200
BLOG_START_DATE = "2026-07-27"
DEFAULT_SEARCH_INDEX_LIMIT_GIB = 0.09
BLOG_ARCHIVE_SCHEMA_VERSION = 1
BLOG_SOURCE_LABELS = {
    "xhs_notes": "外资研报",
    "institutions": "研究机构",
    "consulting": "咨询公司",
    "ark": "ARK Invest",
    "institutions_bis_repair": "研究机构",
    "root": "综合研报",
    "legacy": "历史稿件",
}
BLOG_SOURCE_ORDER = {name: index for index, name in enumerate(BLOG_SOURCE_LABELS)}
BLOG_SOURCE_PUBLICATION_DAY_OFFSETS = {"xhs_notes": 1, "root": 1}
BLOG_MAX_PAYLOAD_BYTES = 20 * 1024 * 1024
BLOG_MAX_ARTICLE_HTML_CHARS = 2_000_000
BLOG_ALLOWED_TAGS = {
    "a", "b", "blockquote", "br", "caption", "code", "div", "em", "figcaption",
    "figure", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "i", "img", "li",
    "ol", "p", "pre", "s", "section", "small", "span", "strong", "sub", "sup",
    "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul",
}
BLOG_DROP_CONTENT_TAGS = {"embed", "iframe", "math", "object", "script", "style", "svg", "template"}
BLOG_VOID_TAGS = {"br", "hr", "img"}
BLOG_STYLE_PROPERTIES = {
    "background", "background-color", "border", "border-bottom", "border-bottom-color",
    "border-bottom-style", "border-bottom-width", "border-color", "border-left",
    "border-left-color", "border-left-style", "border-left-width", "border-radius",
    "border-right", "border-right-color", "border-right-style", "border-right-width",
    "border-style", "border-top", "border-top-color", "border-top-style", "border-top-width",
    "border-width", "box-sizing", "color", "display", "font-family", "font-size",
    "font-style", "font-weight", "height", "letter-spacing", "line-height", "list-style",
    "list-style-position", "list-style-type", "margin", "margin-bottom", "margin-left",
    "margin-right", "margin-top", "max-height", "max-width", "min-height", "min-width",
    "overflow-wrap", "padding", "padding-bottom", "padding-left", "padding-right",
    "padding-top", "text-align", "text-decoration", "vertical-align", "white-space", "width",
    "word-break",
}


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
    return hashlib.sha256(f"portal-archive-title:{key}".encode("utf-8")).hexdigest()[:24]


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
    # Keep this byte-for-byte aligned with write_json(). GitHub evaluates the
    # committed file, not a compact in-memory representation.
    return len((json.dumps(index, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def search_index_with_size_metadata(
    index: dict[str, Any],
    items: list[dict[str, Any]],
    limit_bytes: int,
    pruned_dates: list[str],
) -> dict[str, Any]:
    candidate = dict(index)
    candidate["items"] = items
    candidate["item_count"] = len(items)
    candidate["text_storage_limit_bytes"] = limit_bytes
    candidate["text_pruned_dates"] = list(pruned_dates)
    candidate["text_storage_size_bytes"] = 0
    # The recorded byte count is itself part of the JSON. Iterate until its
    # digit width and the serialized file size agree.
    for _attempt in range(8):
        measured = search_index_size_bytes(candidate)
        if candidate["text_storage_size_bytes"] == measured:
            break
        candidate["text_storage_size_bytes"] = measured
    return candidate


def limit_search_index_by_size(
    index: dict[str, Any],
    catalog: dict[str, Any],
    limit_bytes: int,
) -> dict[str, Any]:
    if limit_bytes <= 0:
        return search_index_with_size_metadata(index, list(index.get("items", [])), 0, [])

    id_to_date = {
        str(item.get("id")): str(item.get("date_folder") or "")
        for item in catalog.get("items", [])
        if item.get("id")
    }
    items = list(index.get("items", []))
    pruned_dates: list[str] = []

    candidate_index = search_index_with_size_metadata(index, items, limit_bytes, pruned_dates)
    while items and candidate_index["text_storage_size_bytes"] > limit_bytes:
        dates = sorted({id_to_date.get(str(item.get("id")), "") for item in items}, key=sort_date_value)
        oldest = dates[0]
        pruned_dates.append(oldest)
        items = [item for item in items if id_to_date.get(str(item.get("id")), "") != oldest]
        candidate_index = search_index_with_size_metadata(index, items, limit_bytes, pruned_dates)
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


def search_index_month(value: Any) -> str:
    compact = re.sub(r"[^0-9]", "", str(value or ""))
    if re.fullmatch(r"\d{6}", compact):
        return compact[:4]
    if re.fullmatch(r"\d{8}", compact):
        return compact[2:6]
    return "0000"


def search_index_date(value: Any) -> str:
    compact = re.sub(r"[^0-9]", "", str(value or ""))
    if re.fullmatch(r"\d{6}", compact):
        return compact
    if re.fullmatch(r"\d{8}", compact):
        return compact[2:]
    return "000000"


def write_search_index_shards(
    index: dict[str, Any],
    catalog: dict[str, Any],
    output_dir: Path,
    partition: str = "month",
) -> dict[str, Any]:
    """Split a size-capped text index into bounded monthly or daily files."""
    if partition not in {"month", "day"}:
        raise ValueError("Search-index shard partition must be month or day")
    id_to_partition: dict[str, str] = {}
    for item in catalog.get("items", []):
        report_id = str(item.get("id") or "")
        if report_id:
            id_to_partition[report_id] = (
                search_index_date(item.get("date_folder"))
                if partition == "day"
                else search_index_month(item.get("date_folder"))
            )

    groups: dict[str, list[dict[str, str]]] = {}
    for entry in index.get("items", []):
        partition_key = id_to_partition.get(str(entry.get("id")), "000000" if partition == "day" else "0000")
        groups.setdefault(partition_key, []).append(entry)

    output_dir.mkdir(parents=True, exist_ok=True)
    shards: list[dict[str, Any]] = []
    for partition_key in sorted(groups, reverse=True):
        filename = f"shard_{partition_key}.json"
        payload = json.dumps({"items": groups[partition_key]}, ensure_ascii=False, separators=(",", ":"))
        shard_path = output_dir / filename
        shard_path.write_text(payload, encoding="utf-8")
        shard_row = {
            "file": filename,
            "item_count": len(groups[partition_key]),
            "bytes": len(payload.encode("utf-8")),
        }
        shard_row["date" if partition == "day" else "month"] = partition_key
        shards.append(shard_row)

    manifest = {
        "schema_version": 1,
        "updated_at_bjt": index.get("updated_at_bjt", ""),
        "item_count": index.get("item_count", 0),
        "text_storage_limit_bytes": index.get("text_storage_limit_bytes", 0),
        "text_storage_size_bytes": index.get("text_storage_size_bytes", 0),
        "text_pruned_dates": index.get("text_pruned_dates", []),
        "partition": partition,
        "total_bytes": sum(shard["bytes"] for shard in shards),
        "shards": shards,
    }
    write_json(output_dir / "manifest.json", manifest)
    return manifest


def write_history_search_shards(
    history_index: dict[str, Any],
    catalog: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    """Keep the public helper name used by the browser-history build/tests."""
    return write_search_index_shards(
        index=history_index,
        catalog=catalog,
        output_dir=output_dir,
    )


def public_catalog(catalog: dict[str, Any]) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    for item in catalog.get("items", []):
        public_item = {key: item.get(key) for key in PUBLIC_ITEM_KEYS if key in item}
        items.append(public_item)
    # Storage quotas, aggregate usage and pruning details are operational
    # metadata.  They are served to the exact admin-a account by the Worker
    # and must never be embedded in the public Pages catalog.
    return {
        "schema_version": catalog.get("schema_version", 1),
        "updated_at_bjt": catalog.get("updated_at_bjt", ""),
        "item_count": len(items),
        "items": items,
    }


def public_password_rules(rules: dict[str, Any]) -> dict[str, Any]:
    groups = []
    for group in rules.get("groups", []):
        password_hash = group.get("password_sha256")
        if password_hash == "REPLACE_WITH_SHA256_HASH":
            password_secret = os.getenv("PASSWORD_SECRET", "")
            download_password = os.getenv("PORTAL_DOWNLOAD_PASSWORD", "")
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
    return "文字索引可检索，PDF状态以报告详情页实时核验为准"


def item_meta_description(item: dict[str, Any]) -> str:
    title = item_display_title(item)
    institution = item_institution(item)
    industry = item_industry(item)
    report_date = date_folder_to_iso(str(item.get("date_folder") or "")) or str(item.get("date_folder") or "")
    return compact_space(
        f"{institution}报告《{title}》，研究主题为{industry}，发布日期为{report_date}，"
        f"{item_page_label(item)}。{item_availability_label(item)}。"
        "Portal Suite 提供中文标题、英文标题、报告信息和相关研究索引。"
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
    # JSON-LD lives in an HTML raw-text element. Escape markup-significant
    # characters so draft metadata can never terminate the script element.
    return (
        json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


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
            "name": "Portal Suite",
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
    <title>{html_escape(title)} | Portal Suite</title>
    <meta name="description" content="{html_escape(description)}">
    <meta name="keywords" content="{html_escape(report_keywords(item))}">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
    <link rel="canonical" href="{html_escape(canonical)}">
    <link rel="alternate" hreflang="zh-CN" href="{html_escape(canonical)}">
    <link rel="alternate" hreflang="x-default" href="{html_escape(canonical)}">
    <link rel="alternate" type="application/rss+xml" title="Portal Suite 最近报告" href="../feed.xml">
    <meta property="og:type" content="article">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="Portal Suite">
    <meta property="og:title" content="{html_escape(title)}">
    <meta property="og:description" content="{html_escape(description)}">
    <meta property="og:url" content="{html_escape(canonical)}">
    <link rel="stylesheet" href="../assets/styles.css">
    <script type="application/ld+json">{render_json_ld(json_ld)}</script>
  </head>
  <body>
    <header class="topbar">
      <a class="back-link" href="../index.html">返回首页</a>
      <div class="topbar-actions">
        <a class="topbar-link" href="../blog/">Blog</a>
        <a class="brand compact" href="../index.html" aria-label="Portal Suite home">
          <img src="../assets/app-mark.svg" alt="" width="30" height="30">
          <span>Portal Suite</span>
        </a>
      </div>
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
      <a href="../blog/">Blog</a>
      <a href="../reports/index.html">报告索引</a>
      <a href="../terms.html">Terms of Service</a>
      <a href="../privacy.html">Privacy Policy</a>
      <span data-portal-chinese-only hidden>Contact WeChat: Support Contact</span>
      <a href="mailto:support@portal.example.invalid" data-portal-non-chinese-only hidden>Email: support@portal.example.invalid</a>
    </footer>
    <script src="../assets/contact.js"></script>
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
    description = "Portal Suite 中文金融研报索引，覆盖宏观策略、行业分析、公司研究、财报、招股书和国际智库报告线索。"
    collection_json_ld = {
        "@type": "CollectionPage",
        "@id": f"{url_join(base_url, 'reports/')}#collection",
        "name": "Portal Suite 报告索引",
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
    <title>金融研报索引 | Portal Suite</title>
    <meta name="description" content="{html_escape(description)}">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
    <link rel="canonical" href="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="alternate" hreflang="zh-CN" href="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="alternate" hreflang="x-default" href="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="alternate" type="application/rss+xml" title="Portal Suite 最近报告" href="../feed.xml">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="Portal Suite">
    <meta property="og:title" content="金融研报索引 | Portal Suite">
    <meta property="og:description" content="{html_escape(description)}">
    <meta property="og:url" content="{html_escape(url_join(base_url, 'reports/'))}">
    <link rel="stylesheet" href="../assets/styles.css">
    <script type="application/ld+json">{render_json_ld(json_ld)}</script>
  </head>
  <body>
    <header class="topbar">
      <a class="back-link" href="../index.html">返回首页</a>
      <div class="topbar-actions">
        <a class="topbar-link" href="../blog/">Blog</a>
        <a class="brand compact" href="../index.html" aria-label="Portal Suite home">
          <img src="../assets/app-mark.svg" alt="" width="30" height="30">
          <span>Portal Suite</span>
        </a>
      </div>
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
      <a href="../blog/">Blog</a>
      <a href="../feed.xml">最近报告 RSS</a>
      <a href="../terms.html">Terms of Service</a>
      <a href="../privacy.html">Privacy Policy</a>
      <span data-portal-chinese-only hidden>Contact WeChat: Support Contact</span>
      <a href="mailto:support@portal.example.invalid" data-portal-non-chinese-only hidden>Email: support@portal.example.invalid</a>
    </footer>
    <script src="../assets/contact.js"></script>
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
        "    <title>Portal Suite 最近报告</title>\n"
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
        "# Portal Suite 公开报告索引",
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


def parse_blog_date(value: str) -> date | None:
    text = str(value or "")
    if not re.fullmatch(r"\d{6}", text):
        return None
    try:
        year = 2000 + int(text[:2])
        return datetime(year, int(text[2:4]), int(text[4:6])).date()
    except ValueError:
        return None


def parse_blog_start_date(value: str) -> date:
    try:
        return datetime.strptime(str(value or ""), "%Y-%m-%d").date()
    except ValueError as error:
        raise ValueError("--blog-start-date must use YYYY-MM-DD") from error


def blog_publication_date(source: str, folder_date: date) -> date:
    """Convert a source folder date to the article's actual publication date."""
    return folder_date + timedelta(days=BLOG_SOURCE_PUBLICATION_DAY_OFFSETS.get(source, 0))


def blog_public_slug(date_value: date | str, fingerprint: str) -> str:
    published = date_value if isinstance(date_value, date) else datetime.strptime(str(date_value), "%Y-%m-%d").date()
    return f"{published.strftime('%Y%m%d')}-{fingerprint[:16]}"


def blog_legacy_slug(date_value: date | str, source: str, fingerprint: str) -> str:
    published = date_value if isinstance(date_value, date) else datetime.strptime(str(date_value), "%Y-%m-%d").date()
    return f"{published.strftime('%Y%m%d')}-{source}-{fingerprint[:16]}"


def sanitize_blog_style(value: str) -> str:
    safe: list[str] = []
    for declaration in str(value or "").split(";"):
        if ":" not in declaration:
            continue
        property_name, property_value = declaration.split(":", 1)
        property_name = property_name.strip().lower()
        property_value = re.sub(r"\s+", " ", property_value).strip()
        lowered = html_unescape(property_value).lower()
        if property_name not in BLOG_STYLE_PROPERTIES or not property_value or len(property_value) > 300:
            continue
        if re.search(r"(?:url\s*\(|expression\s*\(|javascript:|vbscript:|data:|@import|-moz-binding|behavior\s*:|var\s*\()", lowered):
            continue
        if "\\" in property_value or any(ord(char) < 0x20 and char not in "\t\n\r" for char in property_value):
            continue
        numeric_source = re.sub(r"#[0-9a-fA-F]{3,8}\b", "", property_value)
        numeric_values = [float(number) for number in re.findall(r"-?\d+(?:\.\d+)?", numeric_source)]
        if numeric_values and max(abs(number) for number in numeric_values) > 2000:
            continue
        if property_name.startswith(("margin", "padding")) and any(number < 0 for number in numeric_values):
            continue
        if property_name == "font-size" and numeric_values and numeric_values[0] > 96:
            continue
        safe.append(f"{property_name}:{property_value}")
    return ";".join(safe)


def sanitize_blog_url(value: str, *, image: bool = False) -> str:
    text = re.sub(r"[\x00-\x20\x7f]+", "", html_unescape(str(value or ""))).strip()
    if not text:
        return ""
    if text.startswith("//"):
        text = f"https:{text}"
    if not image and text.startswith("#"):
        return text[:500]
    try:
        parsed = urlsplit(text)
    except ValueError:
        return ""
    scheme = parsed.scheme.lower()
    allowed = {"http", "https"} if image else {"http", "https", "mailto"}
    if scheme not in allowed:
        return ""
    if scheme in {"http", "https"} and not parsed.netloc:
        return ""
    if scheme == "http":
        parsed = parsed._replace(scheme="https")
    cleaned = urlunsplit(parsed)
    return cleaned[:3000]


class BlogHTMLSanitizer(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.output: list[str] = []
        self.open_tags: list[str] = []
        self.blocked_tag = ""
        self.blocked_depth = 0

    def _safe_attributes(self, tag: str, attrs: list[tuple[str, str | None]]) -> list[tuple[str, str]]:
        values: dict[str, str] = {}
        for raw_name, raw_value in attrs:
            name = str(raw_name or "").lower()
            if not name or name in values or name.startswith("on"):
                continue
            value = str(raw_value or "")
            if name == "style":
                style = sanitize_blog_style(value)
                if style:
                    values[name] = style
            elif name in {"title", "alt"} and tag in {"a", "img"}:
                values[name] = compact_space(value)[:500]
            elif name == "href" and tag == "a":
                href = sanitize_blog_url(value)
                if href:
                    values[name] = href
            elif name in {"src", "data-src", "data-original", "data-actualsrc"} and tag == "img":
                src = sanitize_blog_url(value, image=True)
                if src and ("src" not in values or name == "src"):
                    values["src"] = src
            elif name in {"colspan", "rowspan"} and tag in {"td", "th"}:
                if value.isdigit() and 1 <= int(value) <= 100:
                    values[name] = value
            elif name in {"width", "height"} and tag == "img":
                if re.fullmatch(r"\d{1,4}(?:\.\d+)?%?", value.strip()):
                    values[name] = value.strip()

        if tag == "img":
            if "src" not in values:
                return []
            values["loading"] = "lazy"
            values["decoding"] = "async"
            values["referrerpolicy"] = "no-referrer"
        elif tag == "a" and values.get("href", "").startswith(("http://", "https://")):
            values["target"] = "_blank"
            values["rel"] = "noopener noreferrer nofollow"
        return list(values.items())

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = str(tag or "").lower()
        if self.blocked_tag:
            if tag == self.blocked_tag:
                self.blocked_depth += 1
            return
        if tag in BLOG_DROP_CONTENT_TAGS:
            self.blocked_tag = tag
            self.blocked_depth = 1
            return
        if tag not in BLOG_ALLOWED_TAGS:
            return
        safe_attrs = self._safe_attributes(tag, attrs)
        if tag == "img" and not safe_attrs:
            return
        attributes = "".join(
            f' {html_escape(name, quote=True)}="{html_escape(value, quote=True)}"'
            for name, value in safe_attrs
        )
        self.output.append(f"<{tag}{attributes}>")
        if tag not in BLOG_VOID_TAGS:
            self.open_tags.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized = str(tag or "").lower()
        self.handle_starttag(normalized, attrs)
        if normalized not in BLOG_VOID_TAGS:
            self.handle_endtag(normalized)

    def handle_endtag(self, tag: str) -> None:
        tag = str(tag or "").lower()
        if self.blocked_tag:
            if tag == self.blocked_tag:
                self.blocked_depth -= 1
                if self.blocked_depth <= 0:
                    self.blocked_tag = ""
                    self.blocked_depth = 0
            return
        if tag not in BLOG_ALLOWED_TAGS or tag in BLOG_VOID_TAGS or tag not in self.open_tags:
            return
        while self.open_tags:
            current = self.open_tags.pop()
            self.output.append(f"</{current}>")
            if current == tag:
                break

    def handle_data(self, data: str) -> None:
        if self.blocked_tag:
            # HTMLParser treats script/style bodies as raw text, so account for a
            # nested opening token before accepting the first closing tag.
            nested_pattern = rf"<\s*{re.escape(self.blocked_tag)}(?:\s|/?>)"
            self.blocked_depth += len(re.findall(nested_pattern, data, flags=re.IGNORECASE))
            return
        if data:
            self.output.append(html_escape(data, quote=False))

    def get_html(self) -> str:
        while self.open_tags:
            self.output.append(f"</{self.open_tags.pop()}>")
        return "".join(self.output).strip()


class BlogTextExtractor(HTMLParser):
    BLOCK_TAGS = {"blockquote", "br", "div", "figcaption", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "li", "p", "section", "tr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, _attrs: list[tuple[str, str | None]]) -> None:
        if str(tag or "").lower() in self.BLOCK_TAGS:
            self.parts.append(" ")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def sanitize_blog_html(value: str) -> str:
    sanitizer = BlogHTMLSanitizer()
    sanitizer.feed(str(value or ""))
    sanitizer.close()
    return sanitizer.get_html()


def blog_html_text(value: str) -> str:
    extractor = BlogTextExtractor()
    extractor.feed(str(value or ""))
    extractor.close()
    return compact_space("".join(extractor.parts))


def blog_article_fingerprint(title: str, sanitized_content: str) -> str:
    normalized_title = compact_space(unicodedata.normalize("NFKC", str(title or ""))).casefold()
    # WeChat re-uploads inline images on a retry and therefore rewrites their
    # CDN URLs even when the article is otherwise identical. Ignore only the
    # volatile image src value; retain the tag structure, alt text, styles,
    # links and visible text so genuinely different articles remain distinct.
    stable_content = re.sub(
        r'(<img\b[^>]*?\s)src="[^"]*"',
        r'\1src="[wechat-image]"',
        str(sanitized_content or ""),
        flags=re.IGNORECASE,
    )
    normalized_content = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", stable_content)).strip()
    return hashlib.sha256(f"{normalized_title}\0{normalized_content}".encode("utf-8")).hexdigest()


def discover_blog_payloads(drafts_root: Path, start_date: date) -> list[tuple[date, str, Path]]:
    payloads: list[tuple[date, str, Path]] = []
    for source in BLOG_SOURCE_LABELS:
        source_dir = drafts_root / source
        if not source_dir.is_dir() or source_dir.is_symlink():
            continue
        for date_dir in source_dir.iterdir():
            folder_date = parse_blog_date(date_dir.name)
            if folder_date is None or not date_dir.is_dir() or date_dir.is_symlink():
                continue
            date_value = blog_publication_date(source, folder_date)
            if date_value < start_date:
                continue
            for payload_path in date_dir.glob("draft_payload_*.json"):
                if payload_path.is_file() and not payload_path.is_symlink():
                    payloads.append((date_value, source, payload_path))
    if drafts_root.is_dir() and not drafts_root.is_symlink():
        for date_dir in drafts_root.iterdir():
            folder_date = parse_blog_date(date_dir.name)
            if folder_date is None or not date_dir.is_dir() or date_dir.is_symlink():
                continue
            date_value = blog_publication_date("root", folder_date)
            if date_value < start_date:
                continue
            for payload_path in date_dir.glob("draft_payload_*.json"):
                if payload_path.is_file() and not payload_path.is_symlink():
                    payloads.append((date_value, "root", payload_path))
    return sorted(payloads, key=lambda row: (row[0], BLOG_SOURCE_ORDER[row[1]], row[2].name))


def load_blog_draft_articles(drafts_root: Path, start_date: date) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for date_value, source, payload_path in discover_blog_payloads(drafts_root, start_date):
        if payload_path.stat().st_size > BLOG_MAX_PAYLOAD_BYTES:
            raise ValueError(f"Blog payload is too large: {payload_path}")
        try:
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError(f"Invalid blog payload: {payload_path}") from error
        articles = payload.get("articles") if isinstance(payload, dict) else None
        if not isinstance(articles, list):
            raise ValueError(f"Blog payload must contain an articles list: {payload_path}")
        try:
            relative_payload = payload_path.relative_to(drafts_root).as_posix()
        except ValueError:
            relative_payload = payload_path.name

        for article_index, raw_article in enumerate(articles, start=1):
            if not isinstance(raw_article, dict):
                raise ValueError(f"Blog article {article_index} must be an object: {payload_path}")
            title = compact_space(str(raw_article.get("title") or ""))[:300]
            raw_content_value = raw_article.get("content")
            if raw_content_value is not None and not isinstance(raw_content_value, str):
                raise ValueError(f"Blog article {article_index} content must be text: {payload_path}")
            raw_content = str(raw_content_value or "")
            if len(raw_content) > BLOG_MAX_ARTICLE_HTML_CHARS:
                raise ValueError(f"Blog article {article_index} is too large: {payload_path}")
            if not title and not raw_content.strip():
                continue
            sanitized_content = sanitize_blog_html(raw_content)
            fingerprint = blog_article_fingerprint(title, sanitized_content)
            origin = {
                "source": source,
                "source_label": BLOG_SOURCE_LABELS[source],
                "date": date_value.isoformat(),
                "payload": relative_payload,
                "article_index": article_index,
            }
            existing = unique.get(fingerprint)
            if existing is not None:
                previous_last_date = str(existing.get("last_date") or existing.get("date") or "")
                origin_key = (source, date_value.isoformat(), relative_payload, article_index)
                known_origins = {
                    (row["source"], row["date"], row["payload"], row["article_index"])
                    for row in existing["origins"]
                }
                if origin_key not in known_origins:
                    existing["origins"].append(origin)
                    existing["last_date"] = max(existing["last_date"], date_value.isoformat())
                if date_value.isoformat() >= previous_last_date and sanitized_content:
                    existing["content"] = sanitized_content
                continue

            digest = compact_space(str(raw_article.get("digest") or ""))[:300]
            if not digest:
                digest = blog_html_text(sanitized_content)[:220]
            display_title = title or digest[:80] or "未命名文章"
            slug = blog_public_slug(date_value, fingerprint)
            unique[fingerprint] = {
                "fingerprint": fingerprint,
                "slug": slug,
                "legacy_slugs": [blog_legacy_slug(date_value, source, fingerprint)],
                "title": display_title,
                "author": compact_space(str(raw_article.get("author") or "Portal Suite"))[:100],
                "digest": digest,
                "content": sanitized_content or "<p>正文暂不可用。</p>",
                "date": date_value.isoformat(),
                "last_date": date_value.isoformat(),
                "source": source,
                "source_label": BLOG_SOURCE_LABELS[source],
                "source_order": BLOG_SOURCE_ORDER[source],
                "payload": relative_payload,
                "article_index": article_index,
                "origins": [origin],
            }

    rows = list(unique.values())
    rows.sort(key=lambda row: (row["source_order"], row["payload"], row["article_index"], row["title"]))
    rows.sort(key=lambda row: row["date"], reverse=True)
    return rows


def blog_source_label(source: str) -> str:
    return BLOG_SOURCE_LABELS.get(str(source or ""), "其他来源")


def normalize_blog_origins(origins: list[dict[str, Any]]) -> list[dict[str, str]]:
    unique: dict[tuple[str, str], dict[str, str]] = {}
    for origin in origins:
        if not isinstance(origin, dict):
            continue
        source = compact_space(str(origin.get("source") or ""))
        date_value = compact_space(str(origin.get("date") or ""))
        if not re.fullmatch(r"[a-z0-9_][a-z0-9_-]{0,80}", source):
            continue
        try:
            datetime.strptime(date_value, "%Y-%m-%d")
        except ValueError:
            continue
        unique[(source, date_value)] = {
            "source": source,
            "source_label": blog_source_label(source),
            "date": date_value,
        }
    return sorted(
        unique.values(),
        key=lambda row: (row["date"], BLOG_SOURCE_ORDER.get(row["source"], 999), row["source"]),
    )


def atomic_write_blog_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        try:
            if path.read_text(encoding="utf-8") == serialized:
                return
        except (OSError, UnicodeDecodeError):
            pass
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(serialized)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def blog_archive_manifest(start_date: date) -> dict[str, Any]:
    return {
        "schema_version": BLOG_ARCHIVE_SCHEMA_VERSION,
        "start_date": start_date.isoformat(),
        "layout": "YYYYMMDD/<fingerprint>.json",
    }


def ensure_blog_archive_manifest(archive_root: Path, start_date: date) -> None:
    if archive_root.is_symlink() or (archive_root.exists() and not archive_root.is_dir()):
        raise ValueError(f"Blog archive root must be a regular directory: {archive_root}")
    manifest_path = archive_root / "manifest.json"
    expected = blog_archive_manifest(start_date)
    if not manifest_path.exists():
        existing_shards = list(archive_root.glob("*/*.json")) if archive_root.exists() else []
        if existing_shards:
            raise ValueError(f"Blog archive manifest is missing: {manifest_path}")
        atomic_write_blog_json(manifest_path, expected)
        return
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError(f"Blog archive manifest must be a regular file: {manifest_path}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"Invalid Blog archive manifest: {manifest_path}") from error
    if manifest != expected:
        raise ValueError(
            f"Unsupported Blog archive manifest in {manifest_path}; "
            f"expected schema {BLOG_ARCHIVE_SCHEMA_VERSION} from {start_date.isoformat()}"
        )


def blog_archive_record(article: dict[str, Any]) -> dict[str, Any]:
    origins = normalize_blog_origins(list(article.get("origins") or []))
    return {
        "schema_version": BLOG_ARCHIVE_SCHEMA_VERSION,
        "fingerprint": str(article.get("fingerprint") or ""),
        "slug": str(article.get("slug") or ""),
        "legacy_slugs": sorted({
            str(value)
            for value in article.get("legacy_slugs", [])
            if re.fullmatch(r"[a-z0-9_-]{8,160}", str(value))
            and str(value) != str(article.get("slug") or "")
        }),
        "title": str(article.get("title") or ""),
        "author": str(article.get("author") or "Portal Suite"),
        "digest": str(article.get("digest") or ""),
        "content": str(article.get("content") or "<p>正文暂不可用。</p>"),
        "date": str(article.get("date") or ""),
        "last_date": str(article.get("last_date") or article.get("date") or ""),
        "source": str(article.get("source") or "legacy"),
        "origins": [
            {"source": origin["source"], "date": origin["date"]}
            for origin in origins
        ],
    }


def validate_blog_archive_record(data: Any, path: Path, start_date: date) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("schema_version") != BLOG_ARCHIVE_SCHEMA_VERSION:
        raise ValueError(f"Invalid Blog archive schema: {path}")
    fingerprint = str(data.get("fingerprint") or "")
    if not re.fullmatch(r"[0-9a-f]{64}", fingerprint) or path.stem != fingerprint:
        raise ValueError(f"Invalid Blog archive fingerprint: {path}")
    title = compact_space(str(data.get("title") or ""))[:300]
    slug = str(data.get("slug") or "")
    source = compact_space(str(data.get("source") or ""))
    date_value = str(data.get("date") or "")
    last_date = str(data.get("last_date") or date_value)
    if not title or not re.fullmatch(r"[a-z0-9_-]{8,160}", slug):
        raise ValueError(f"Invalid Blog archive title or slug: {path}")
    if not re.fullmatch(r"[a-z0-9_][a-z0-9_-]{0,80}", source):
        raise ValueError(f"Invalid Blog archive source: {path}")
    try:
        published = datetime.strptime(date_value, "%Y-%m-%d").date()
        modified = datetime.strptime(last_date, "%Y-%m-%d").date()
    except ValueError as error:
        raise ValueError(f"Invalid Blog archive date: {path}") from error
    if published < start_date or modified < published or path.parent.name != published.strftime("%Y%m%d"):
        raise ValueError(f"Blog archive path/date mismatch: {path}")
    expected_slug = blog_public_slug(published, fingerprint)
    legacy_slug = blog_legacy_slug(published, source, fingerprint)
    if slug not in {expected_slug, legacy_slug}:
        raise ValueError(f"Blog archive slug does not match its identity: {path}")
    legacy_slugs = {
        str(value)
        for value in data.get("legacy_slugs", [])
        if re.fullmatch(r"[a-z0-9_-]{8,160}", str(value))
    }
    if slug != expected_slug:
        legacy_slugs.add(slug)
    legacy_slugs.discard(expected_slug)
    content = str(data.get("content") or "")
    if not content or len(content) > BLOG_MAX_ARTICLE_HTML_CHARS or sanitize_blog_html(content) != content:
        raise ValueError(f"Blog archive contains unsanitized or invalid HTML: {path}")
    raw_origins = data.get("origins")
    if not isinstance(raw_origins, list):
        raise ValueError(f"Blog archive origins must be a list: {path}")
    origins = normalize_blog_origins(raw_origins)
    if (
        not origins
        or len(origins) != len(raw_origins)
        or any(origin["date"] < date_value or origin["date"] > last_date for origin in origins)
        or max(origin["date"] for origin in origins) != last_date
        or not any(origin["source"] == source and origin["date"] == date_value for origin in origins)
    ):
        raise ValueError(f"Blog archive origins are incomplete: {path}")
    return {
        "fingerprint": fingerprint,
        "slug": expected_slug,
        "legacy_slugs": sorted(legacy_slugs),
        "title": title,
        "author": compact_space(str(data.get("author") or "Portal Suite"))[:100],
        "digest": compact_space(str(data.get("digest") or ""))[:300],
        "content": content,
        "date": date_value,
        "last_date": last_date,
        "source": source,
        "source_label": blog_source_label(source),
        "source_order": BLOG_SOURCE_ORDER.get(source, 999),
        "payload": "",
        "article_index": 0,
        "origins": origins,
    }


def load_blog_archive(archive_root: Path, start_date: date) -> list[dict[str, Any]]:
    ensure_blog_archive_manifest(archive_root, start_date)
    rows: list[dict[str, Any]] = []
    fingerprints: set[str] = set()
    shard_paths: list[Path] = []
    for entry in archive_root.iterdir():
        if entry.name == "manifest.json":
            continue
        if entry.is_symlink() or not entry.is_dir() or not re.fullmatch(r"\d{8}", entry.name):
            raise ValueError(f"Unexpected entry in Blog archive: {entry}")
        for path in entry.iterdir():
            if path.is_symlink() or not path.is_file() or path.suffix != ".json":
                raise ValueError(f"Unexpected Blog archive shard entry: {path}")
            shard_paths.append(path)
    for path in sorted(shard_paths):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValueError(f"Invalid Blog archive shard: {path}") from error
        row = validate_blog_archive_record(raw, path, start_date)
        if row["fingerprint"] in fingerprints:
            raise ValueError(f"Duplicate Blog archive fingerprint: {path}")
        fingerprints.add(row["fingerprint"])
        rows.append(row)
    return rows


def merge_blog_articles(
    archived_articles: list[dict[str, Any]],
    draft_articles: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    merged = {str(article.get("fingerprint") or ""): dict(article) for article in archived_articles}
    for draft in draft_articles:
        fingerprint = str(draft.get("fingerprint") or "")
        existing = merged.get(fingerprint)
        if existing is None:
            merged[fingerprint] = dict(draft)
            continue
        existing["legacy_slugs"] = sorted({
            *[str(value) for value in existing.get("legacy_slugs", []) if value],
            *[str(value) for value in draft.get("legacy_slugs", []) if value],
        })
        origins = normalize_blog_origins(list(existing.get("origins") or []) + list(draft.get("origins") or []))
        existing["origins"] = origins
        existing["last_date"] = max(
            str(existing.get("last_date") or existing.get("date") or ""),
            str(draft.get("last_date") or draft.get("date") or ""),
        )
        if draft.get("content"):
            existing["content"] = draft["content"]
        if not existing.get("digest") and draft.get("digest"):
            existing["digest"] = draft["digest"]
        if not existing.get("author") and draft.get("author"):
            existing["author"] = draft["author"]
    rows = [article for fingerprint, article in merged.items() if fingerprint]
    rows.sort(key=lambda row: (row.get("source_order", 999), row.get("payload", ""), row.get("article_index", 0), row.get("title", "")))
    rows.sort(key=lambda row: str(row.get("date") or ""), reverse=True)
    return rows


def persist_blog_archive(archive_root: Path, articles: list[dict[str, Any]], start_date: date) -> None:
    ensure_blog_archive_manifest(archive_root, start_date)
    for article in articles:
        record = blog_archive_record(article)
        date_folder = str(record["date"]).replace("-", "")
        path = archive_root / date_folder / f'{record["fingerprint"]}.json'
        atomic_write_blog_json(path, record)


def blog_source_badges(article: dict[str, Any]) -> str:
    seen: set[str] = set()
    badges: list[str] = []
    origins = sorted(
        article.get("origins", []),
        key=lambda row: (row.get("date", ""), BLOG_SOURCE_ORDER.get(str(row.get("source") or ""), 999)),
    )
    for origin in origins:
        source = str(origin.get("source") or "")
        label = str(origin.get("source_label") or BLOG_SOURCE_LABELS.get(source) or "其他来源")
        if not source or label in seen:
            continue
        seen.add(label)
        # `source` is an internal ingestion key (for example xhs_notes).  The
        # public Blog should only expose the editorial label, including in
        # hover text and accessibility output.
        badges.append(f'<span class="blog-source-badge">{html_escape(label)}</span>')
    return "".join(badges)


def blog_origin_details(article: dict[str, Any]) -> str:
    rows: list[str] = []
    origins = sorted(
        article.get("origins", []),
        key=lambda row: (row.get("date", ""), BLOG_SOURCE_ORDER.get(str(row.get("source") or ""), 999)),
    )
    seen: set[tuple[str, str]] = set()
    for origin in origins:
        source = str(origin.get("source") or "")
        date_value = str(origin.get("date") or "")
        key = (source, date_value)
        if key in seen:
            continue
        seen.add(key)
        label = str(origin.get("source_label") or BLOG_SOURCE_LABELS.get(source) or "其他来源")
        rows.append(f"{html_escape(date_value)} · {html_escape(label)}")
    return "；".join(rows)


def blog_csp_meta() -> str:
    return (
        '<meta http-equiv="Content-Security-Policy" '
        'content="default-src &#39;none&#39;; style-src &#39;self&#39; &#39;unsafe-inline&#39;; '
        'script-src &#39;self&#39;; connect-src &#39;self&#39;; '
        'img-src &#39;self&#39; https: data:; font-src &#39;self&#39; data:; base-uri &#39;none&#39;; '
        'form-action &#39;none&#39;; frame-ancestors &#39;none&#39;">'
    )


def render_blog_index(articles: list[dict[str, Any]], base_url: str, start_date: date) -> str:
    canonical = url_join(base_url, "blog/")
    grouped: dict[str, list[dict[str, Any]]] = {}
    for article in articles:
        grouped.setdefault(str(article.get("date") or ""), []).append(article)
    sections: list[str] = []
    for date_value, date_articles in grouped.items():
        cards = []
        for article in date_articles:
            cards.append(
                '<article class="blog-card">'
                '<div class="blog-card-meta">'
                f'<time datetime="{html_escape(date_value, quote=True)}">{html_escape(date_value)}</time>'
                f'{blog_source_badges(article)}'
                '</div>'
                f'<h2><a href="{html_escape(article["slug"], quote=True)}.html">{html_escape(article["title"])}</a></h2>'
                f'<p>{html_escape(article.get("digest") or "")}</p>'
                f'<a class="blog-read-more" href="{html_escape(article["slug"], quote=True)}.html">阅读全文</a>'
                '</article>'
            )
        sections.append(
            '<section class="blog-day">'
            f'<h2 class="blog-day-title"><time datetime="{html_escape(date_value, quote=True)}">{html_escape(date_value)}</time></h2>'
            f'<div class="blog-card-grid">{"".join(cards)}</div>'
            '</section>'
        )
    if not sections:
        sections.append(
            '<section class="blog-empty">'
            f'<h2>内容将从 {html_escape(start_date.isoformat())} 起发布</h2>'
            '<p>公众号正文进入每日草稿后，会在这里自动生成可长期访问的静态文章。</p>'
            '</section>'
        )
    json_ld = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "name": "Portal Suite Blog",
        "description": "Portal Suite 每日研究文章与公众号正文存档。",
        "url": canonical,
        "blogPost": [
            {
                "@type": "BlogPosting",
                "headline": article["title"],
                "datePublished": article["date"],
                "url": url_join(base_url, f'blog/{article["slug"]}.html'),
            }
            for article in articles
        ],
    }
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Blog | Portal Suite</title>
    <meta name="description" content="Portal Suite 每日研究文章与公众号正文存档，覆盖外资研报、研究机构与咨询公司内容。">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
    <link rel="canonical" href="{html_escape(canonical, quote=True)}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="Portal Suite">
    <meta property="og:title" content="Blog | Portal Suite">
    <meta property="og:description" content="Portal Suite 每日研究文章与公众号正文存档。">
    <meta property="og:url" content="{html_escape(canonical, quote=True)}">
    {blog_csp_meta()}
    <link rel="stylesheet" href="../assets/styles.css">
    <link rel="stylesheet" href="../assets/blog.css">
    <script defer src="../assets/contact.js"></script>
    <script defer src="../assets/app.js"></script>
    <script type="application/ld+json">{render_json_ld(json_ld)}</script>
  </head>
  <body class="blog-page" data-page="blog">
    <header class="topbar blog-topbar">
      <a class="brand compact" href="../index.html" aria-label="Portal Suite home">
        <img src="../assets/app-mark.svg" alt="" width="30" height="30">
        <span>Portal Suite</span>
      </a>
      <nav class="topbar-actions" aria-label="站点导航">
        <a class="topbar-link" href="../index.html">首页</a>
        <a class="topbar-link is-active" href="index.html" aria-current="page">Blog</a>
        <a class="topbar-link" href="../newsfeed.html">Newsfeed</a>
        <a class="topbar-link" href="../reports/index.html">报告索引</a>
        <button id="accountGate" class="account-button" type="button">登录</button>
      </nav>
    </header>
    <main class="blog-shell">
      <header class="blog-hero">
        <p class="blog-kicker">PORTAL SUITE · DAILY RESEARCH</p>
        <h1>Blog</h1>
        <p>从 {html_escape(start_date.isoformat())} 起，完整保存每日公众号文章，按首次入库日期倒序展示。</p>
        <div class="blog-summary"><strong>{len(articles)}</strong> 篇文章</div>
      </header>
      <section class="blog-market-views" id="blogMarketViews" aria-labelledby="blogMarketViewsTitle">
        <div class="blog-market-views-heading">
          <div>
            <p class="blog-kicker">DAILY MARKET VIEWS</p>
            <h2 id="blogMarketViewsTitle">每日 Market Views</h2>
          </div>
          <p>开通时长至少 1 个月的会员可下载 PDF。</p>
        </div>
        <div id="blogMarketViewsAccess" class="status-line" aria-live="polite"></div>
        <div id="blogMarketViewsList" class="blog-market-views-list">
          <div class="loading-state"><span class="loading-spinner" aria-hidden="true"></span><span>正在读取每日 PDF…</span></div>
        </div>
      </section>
      {"".join(sections)}
    </main>
    <footer class="legal-footer blog-footer">
      <a href="../index.html">首页检索</a>
      <a href="../reports/index.html">报告索引</a>
      <a href="../terms.html">Terms of Service</a>
      <a href="mailto:support@portal.example.invalid">Email: support@portal.example.invalid</a>
    </footer>
  </body>
</html>
"""


def render_blog_article(article: dict[str, Any], base_url: str) -> str:
    canonical = url_join(base_url, f'blog/{article["slug"]}.html')
    title = str(article.get("title") or "未命名文章")
    digest = str(article.get("digest") or "")
    author = str(article.get("author") or "Portal Suite")
    image_match = re.search(r'<img\b[^>]*\bsrc="([^"]+)"', str(article.get("content") or ""), re.IGNORECASE)
    image_url = html_unescape(image_match.group(1)) if image_match else ""
    json_ld: dict[str, Any] = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": digest,
        "datePublished": article["date"],
        "dateModified": article.get("last_date") or article["date"],
        "mainEntityOfPage": canonical,
        "author": {"@type": "Organization", "name": author},
        "publisher": {"@type": "Organization", "name": "Portal Suite", "url": url_join(base_url, "/")},
    }
    if image_url:
        json_ld["image"] = [image_url]
    og_image = f'<meta property="og:image" content="{html_escape(image_url, quote=True)}">' if image_url else ""
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html_escape(title)} | Portal Suite Blog</title>
    <meta name="description" content="{html_escape(digest, quote=True)}">
    <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
    <link rel="canonical" href="{html_escape(canonical, quote=True)}">
    <meta property="og:type" content="article">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="Portal Suite">
    <meta property="og:title" content="{html_escape(title, quote=True)}">
    <meta property="og:description" content="{html_escape(digest, quote=True)}">
    <meta property="og:url" content="{html_escape(canonical, quote=True)}">
    {og_image}
    {blog_csp_meta()}
    <link rel="stylesheet" href="../assets/styles.css">
    <link rel="stylesheet" href="../assets/blog.css">
    <script type="application/ld+json">{render_json_ld(json_ld)}</script>
  </head>
  <body class="blog-page blog-article-page">
    <header class="topbar blog-topbar">
      <a class="brand compact" href="../index.html" aria-label="Portal Suite home">
        <img src="../assets/app-mark.svg" alt="" width="30" height="30">
        <span>Portal Suite</span>
      </a>
      <nav class="topbar-actions" aria-label="站点导航">
        <a class="topbar-link" href="../index.html">首页</a>
        <a class="topbar-link is-active" href="index.html">Blog</a>
        <a class="topbar-link" href="../reports/index.html">报告索引</a>
      </nav>
    </header>
    <main class="blog-article-shell">
      <a class="blog-back" href="index.html">← 返回 Blog</a>
      <article class="blog-article">
        <header class="blog-article-header">
          <div class="blog-card-meta">
            <time datetime="{html_escape(article["date"], quote=True)}">{html_escape(article["date"])}</time>
            {blog_source_badges(article)}
          </div>
          <h1>{html_escape(title)}</h1>
          {f'<p class="blog-digest">{html_escape(digest)}</p>' if digest else ''}
          <p class="blog-byline">作者：{html_escape(author)} · 来源：{blog_origin_details(article)}</p>
        </header>
        <div class="blog-article-content">
          {article["content"]}
        </div>
      </article>
    </main>
    <footer class="legal-footer blog-footer">
      <a href="index.html">Blog</a>
      <a href="../index.html">首页检索</a>
      <a href="../reports/index.html">报告索引</a>
      <a href="mailto:support@portal.example.invalid">Email: support@portal.example.invalid</a>
    </footer>
  </body>
</html>
"""


def render_blog_legacy_redirect(article: dict[str, Any], base_url: str) -> str:
    target = f'{article["slug"]}.html'
    canonical = url_join(base_url, f"blog/{target}")
    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex,follow">
    <meta http-equiv="refresh" content="0; url={html_escape(target, quote=True)}">
    <link rel="canonical" href="{html_escape(canonical, quote=True)}">
    <title>文章地址已更新 | Portal Suite Blog</title>
  </head>
  <body>
    <p>文章地址已更新，<a href="{html_escape(target, quote=True)}">点击继续阅读</a>。</p>
  </body>
</html>
"""


def build_blog(
    output: Path,
    drafts_root: Path,
    base_url: str,
    start_date: date,
    archive_root: Path | None = None,
) -> list[dict[str, Any]]:
    draft_articles = load_blog_draft_articles(drafts_root, start_date)
    if archive_root is None:
        articles = draft_articles
    else:
        archived_articles = load_blog_archive(archive_root, start_date)
        articles = merge_blog_articles(archived_articles, draft_articles)
        persist_blog_archive(archive_root, articles, start_date)
    blog_dir = output / "blog"
    blog_dir.mkdir(parents=True, exist_ok=True)
    write_text(blog_dir / "index.html", render_blog_index(articles, base_url, start_date))
    for article in articles:
        write_text(blog_dir / f'{article["slug"]}.html', render_blog_article(article, base_url))
        for legacy_slug in article.get("legacy_slugs", []):
            if legacy_slug and legacy_slug != article["slug"]:
                write_text(blog_dir / f"{legacy_slug}.html", render_blog_legacy_redirect(article, base_url))
    return articles


def build_seo_outputs(
    output: Path,
    catalog: dict[str, Any],
    base_url: str = SITE_BASE_URL,
    blog_articles: list[dict[str, Any]] | None = None,
) -> None:
    base_url = base_url.rstrip("/") or SITE_BASE_URL
    blog_articles = list(blog_articles or [])
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
        sitemap_url(
            url_join(base_url, "blog/"),
            max((str(article.get("last_date") or article.get("date") or "") for article in blog_articles), default=generated_date),
            "0.8",
        ),
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

    for index in range(0, len(blog_articles), SITEMAP_REPORT_CHUNK_SIZE):
        chunk = blog_articles[index:index + SITEMAP_REPORT_CHUNK_SIZE]
        sitemap_name = f"sitemap-blog-{index // SITEMAP_REPORT_CHUNK_SIZE + 1}.xml"
        sitemap_names.append(sitemap_name)
        rows = [
            sitemap_url(
                url_join(base_url, f'blog/{article["slug"]}.html'),
                str(article.get("last_date") or article.get("date") or generated_date),
                "0.7",
            )
            for article in chunk
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
    cn_rows.extend(
        sitemap_url(
            url_join(base_url, f'blog/{article["slug"]}.html'),
            str(article.get("last_date") or article.get("date") or generated_date),
            "0.7",
        )
        for article in blog_articles
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
            "# Portal Suite",
            "",
            "Portal Suite 是中文金融研究报告检索与索引站点，覆盖宏观策略、行业分析、公司研究、财报、招股书、国际智库和市场观点。",
            "",
            "## Primary URLs",
            f"- Home/Search: {url_join(base_url, '/')}",
            f"- Report index: {url_join(base_url, 'reports/')}",
            f"- Blog: {url_join(base_url, 'blog/')}",
            f"- Sitemap index: {url_join(base_url, 'sitemap.xml')}",
            f"- Recent reports RSS: {url_join(base_url, 'feed.xml')}",
            f"- Expanded public report metadata: {url_join(base_url, 'llms-full.txt')}",
            f"- Public catalog JSON: {url_join(base_url, 'data/catalog.json')}",
            "",
            "## Content Notes",
            "- Preferred language for summaries: zh-CN.",
            "- Report pages expose titles, translated titles, institution, industry, date, page count, and availability status.",
            "- PDF download access may require an approved account. For source files or unavailable PDFs, email support@portal.example.invalid.",
            "",
        ]),
    )
    write_text(output / "llms-full.txt", render_llms_full(catalog, base_url))


def copy_site(src: Path, output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(src, output)


def version_assets(output: Path) -> None:
    """Append a content-hash query to JavaScript / stylesheet links in every HTML file.

    portal.example.invalid is fronted by Cloudflare, which caches these assets for hours, so an
    unversioned `assets/app.js` keeps serving stale JS after a deploy. Hashing the
    URL (`assets/app.js?v=<hash>`) makes each change a new cache key, so deploys take
    effect immediately. Only busts when the file content actually changes.
    """
    versions: dict[str, str] = {}
    for rel in ("assets/app.js", "assets/contact.js", "assets/styles.css", "assets/blog.css"):
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
    parser.add_argument("--site-src", default="portal_suite/site_src")
    parser.add_argument("--output-dir", default="_portal_suite_pages")
    parser.add_argument("--wechat-drafts-root", default="wechat_drafts")
    parser.add_argument("--blog-start-date", default=BLOG_START_DATE)
    parser.add_argument("--blog-archive-root", default="portal_suite/data/blog_archive")
    parser.add_argument("--catalog-path", default="portal_suite/data/catalog.json")
    parser.add_argument("--archive-catalog-path", default="portal_suite/data/archive_catalog.json")
    parser.add_argument("--search-index-path", default="portal_suite/data/search_index.json")
    parser.add_argument("--password-rules", default="portal_suite/password_rules.json")
    parser.add_argument("--worker-base-url", default="")
    parser.add_argument("--bank-catalog-root", default="bank_report_catalogs")
    parser.add_argument("--mineru-root", default="xhs_notes/dropbox")
    parser.add_argument("--search-text-limit", type=int, default=0, help="Per-report normalized search text cap. 0 keeps all matched text.")
    parser.add_argument(
        "--search-index-limit-gb",
        type=float,
        default=DEFAULT_SEARCH_INDEX_LIMIT_GIB,
        help=(
            "Maximum public text index size in GiB. The default stays below GitHub's 100 MiB"
            " per-file limit; oldest date folders are removed first. 0 disables."
        ),
    )
    parser.add_argument("--history-catalog", default="portal_suite/data/history_catalog.json")
    parser.add_argument("--history-text-dir", default="portal_suite/data/history_text")
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
    current_manifest = write_search_index_shards(
        index=search_index,
        catalog=catalog,
        output_dir=output_dir / "data" / "search_index_current",
        partition="day",
    )
    history_manifest = write_history_search_shards(
        history_index=history_index,
        catalog=catalog,
        output_dir=output_dir / "data" / "search_index_history",
    )
    rules = public_password_rules(load_json(Path(args.password_rules)))
    write_json(output_dir / "data" / "catalog.json", public_catalog(catalog))
    write_json(output_dir / "data" / "search_index.json", search_index)
    write_json(output_dir / "data" / "password_rules.json", rules)
    write_json(output_dir / "data" / "config.json", {"worker_base_url": args.worker_base_url.rstrip("/")})
    write_json(archive_catalog_path, archive_catalog)
    write_json(search_index_path, search_index)
    blog_articles = build_blog(
        output=output_dir,
        drafts_root=Path(args.wechat_drafts_root),
        base_url=SITE_BASE_URL,
        start_date=parse_blog_start_date(args.blog_start_date),
        archive_root=Path(args.blog_archive_root),
    )
    build_seo_outputs(output_dir, catalog, SITE_BASE_URL, blog_articles)
    version_assets(output_dir)
    print(
        f"Built {output_dir} with {catalog['item_count']} catalog items "
        f"({history_stats['history_added']} history-only, {history_stats['history_deduped']} history deduped) "
        f"and {search_index['item_count']} full-text search entries, "
        f"{len(blog_articles)} blog articles, "
        f"{search_index['item_count']} current text entries in {len(current_manifest['shards'])} daily shards, "
        f"{history_index['item_count']} history text entries in {len(history_manifest['shards'])} lazy shards "
        f"({history_manifest['total_bytes'] / 1e6:.1f} MB)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
