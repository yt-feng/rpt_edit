#!/usr/bin/env python3
"""Build the static KC Desk Notes Pages artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import unicodedata
from pathlib import Path
from typing import Any


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
    for html_path in output.glob("*.html"):
        text = html_path.read_text(encoding="utf-8")
        for rel, digest in versions.items():
            pattern = re.compile(rf'(["\']){re.escape(rel)}(?:\?v=[^"\']*)?\1')
            text = pattern.sub(lambda match: f"{match.group(1)}{rel}?v={digest}{match.group(1)}", text)
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
    args = parser.parse_args()

    site_src = Path(args.site_src)
    output_dir = Path(args.output_dir)
    copy_site(site_src, output_dir)

    catalog = public_catalog(load_json(Path(args.catalog_path)))
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
    rules = public_password_rules(load_json(Path(args.password_rules)))
    write_json(output_dir / "data" / "catalog.json", catalog)
    write_json(output_dir / "data" / "search_index.json", search_index)
    write_json(output_dir / "data" / "password_rules.json", rules)
    write_json(output_dir / "data" / "config.json", {"worker_base_url": args.worker_base_url.rstrip("/")})
    write_json(archive_catalog_path, archive_catalog)
    write_json(search_index_path, search_index)
    version_assets(output_dir)
    print(
        f"Built {output_dir} with {catalog['item_count']} catalog items "
        f"and {search_index['item_count']} full-text search entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
