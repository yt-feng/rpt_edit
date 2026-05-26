#!/usr/bin/env python3
"""Build the persistent KC Desk Notes catalog and mirror current PDFs to R2.

The catalog intentionally stores sanitized titles and opaque report ids only.
Dropbox paths are used in memory during the current scan, but are not written to
the repo-facing JSON.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

from build_bank_report_catalog import (
    DATE_FOLDER_RE,
    detect_bank,
    dropbox_access_token,
    latest_date_folders,
    list_folder,
    sanitize_report_name,
)
from finalize_outputs import sanitize_text

DROPBOX_CONTENT = "https://content.dropboxapi.com/2"
DEFAULT_R2_PREFIX = "reports"


def log(message: str) -> None:
    print(message, flush=True)


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def bjt_now() -> str:
    return datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")


def load_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def report_id_for_entry(entry: dict[str, Any]) -> str:
    content_hash = str(entry.get("content_hash") or "").strip().lower()
    if content_hash:
        seed = f"dropbox-content:{content_hash}"
    else:
        path_seed = str(entry.get("path_lower") or entry.get("path_display") or entry.get("name") or "")
        seed = f"dropbox-path:{path_seed.lower()}"
    return sha256_hex(seed)[:24]


def source_hash_for_entry(entry: dict[str, Any]) -> str:
    content_hash = str(entry.get("content_hash") or "").strip().lower()
    if content_hash:
        return sha256_hex(f"dropbox-content:{content_hash}")
    path_seed = str(entry.get("path_lower") or entry.get("path_display") or entry.get("name") or "")
    return sha256_hex(f"dropbox-path:{path_seed.lower()}")


def clean_title(name: str) -> str:
    title = sanitize_text(sanitize_report_name(name))
    title = re.sub(r"\.pdf$", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+", " ", title).strip(" -_\t\r\n")
    if not title:
        title = Path(name).stem or "Untitled report"
    return title


def choose_date_folders(token: str, root: str, days: int) -> list[dict[str, Any]]:
    entries = list_folder(token, root, recursive=False)
    folders = [e for e in entries if e.get(".tag") == "folder" and DATE_FOLDER_RE.match(str(e.get("name", "")))]
    if not folders:
        names = ", ".join(str(e.get("name")) for e in entries[:20])
        raise RuntimeError(f"No date-named child folders found under {root}. First entries: {names}")
    folders = sorted(folders, key=lambda e: int(e["name"]), reverse=True)
    if days > 0:
        return latest_date_folders(entries, days)
    return folders


def load_password_rules(path: Path) -> dict[str, Any]:
    data = load_json(path, {"default_group": "default", "groups": [], "assignment_rules": []})
    groups = {str(group.get("id")) for group in data.get("groups", []) if group.get("id")}
    default_group = str(data.get("default_group") or "default")
    if default_group not in groups:
        raise RuntimeError(f"Password default_group is not declared in groups: {default_group}")
    return data


def matches_rule(value: str, pattern: str) -> bool:
    pattern = pattern or "*"
    return fnmatch.fnmatchcase(value.lower(), pattern.lower())


def assign_password_group(title: str, date_folder: str, bank_code: str, rules: dict[str, Any]) -> str:
    default_group = str(rules.get("default_group") or "default")
    for rule in rules.get("assignment_rules", []):
        rule_date = str(rule.get("date_folder") or "*")
        rule_bank = str(rule.get("bank_code") or "*")
        title_contains = str(rule.get("title_contains") or "").strip().lower()
        if not matches_rule(date_folder, rule_date):
            continue
        if not matches_rule(bank_code, rule_bank):
            continue
        if title_contains and title_contains not in title.lower():
            continue
        return str(rule.get("password_group") or default_group)
    return default_group


def r2_key_for_id(report_id: str, prefix: str) -> str:
    clean_prefix = prefix.strip("/")
    return f"{clean_prefix}/{report_id}.pdf" if clean_prefix else f"{report_id}.pdf"


def download_dropbox_file(token: str, dropbox_path: str, local_path: Path) -> None:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.post(
        f"{DROPBOX_CONTENT}/files/download",
        headers={
            "Authorization": f"Bearer {token}",
            "Dropbox-API-Arg": json.dumps({"path": dropbox_path}),
        },
        timeout=300,
        stream=True,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"Dropbox download failed for {dropbox_path}: HTTP {response.status_code}, {response.text[:500]}")
    with local_path.open("wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)


def build_r2_client() -> Any:
    try:
        import boto3  # type: ignore
    except Exception as exc:  # pragma: no cover - exercised in Actions
        raise RuntimeError("boto3 is required for --sync-r2. Install it with: pip install boto3") from exc

    account_id = require_env("R2_ACCOUNT_ID")
    access_key = require_env("R2_ACCESS_KEY_ID")
    secret_key = require_env("R2_SECRET_ACCESS_KEY")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
    )


def upload_pdf_to_r2(client: Any, bucket: str, key: str, local_path: Path) -> None:
    with local_path.open("rb") as f:
        client.upload_fileobj(
            f,
            bucket,
            key,
            ExtraArgs={
                "ContentType": "application/pdf",
                "Metadata": {"source": "kc-desk-notes"},
            },
        )


def collect_current_reports(
    token: str,
    root: str,
    folders: list[dict[str, Any]],
    rules: dict[str, Any],
    r2_prefix: str,
) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    current: dict[str, dict[str, Any]] = {}
    download_paths: dict[str, str] = {}

    for folder in folders:
        date_folder = str(folder["name"])
        folder_path = str(folder.get("path_display") or folder.get("path_lower") or f"{root.rstrip('/')}/{date_folder}")
        log(f"Listing PDFs under {folder_path}")
        entries = list_folder(token, folder_path, recursive=True)
        pdfs = [e for e in entries if e.get(".tag") == "file" and str(e.get("name", "")).lower().endswith(".pdf")]
        log(f"  {date_folder}: {len(pdfs)} PDFs")

        for entry in pdfs:
            dropbox_path = str(entry.get("path_display") or entry.get("path_lower") or "")
            if not dropbox_path:
                continue
            name = str(entry.get("name") or "report.pdf")
            report_id = report_id_for_entry(entry)
            title = clean_title(name)
            bank_code, bank_name = detect_bank(f"{name} {dropbox_path}")
            password_group = assign_password_group(title, date_folder, bank_code, rules)
            seen_dates = set(current.get(report_id, {}).get("date_folders", []))
            seen_dates.add(date_folder)

            current[report_id] = {
                "id": report_id,
                "title": title,
                "filename": f"{title}.pdf",
                "date_folder": max(seen_dates),
                "date_folders": sorted(seen_dates, reverse=True),
                "bank_code": bank_code,
                "bank_name": bank_name,
                "password_group": password_group,
                "size_bytes": int(entry.get("size") or 0),
                "client_modified": str(entry.get("client_modified") or ""),
                "server_modified": str(entry.get("server_modified") or ""),
                "source_hash": source_hash_for_entry(entry),
                "r2_key": r2_key_for_id(report_id, r2_prefix),
                "r2_synced": False,
                "available": False,
                "present_in_latest_scan": True,
            }
            download_paths[report_id] = dropbox_path

    return current, download_paths


def merge_catalog(
    old_catalog: dict[str, Any],
    current: dict[str, dict[str, Any]],
    dropbox_root: str,
    now_bjt: str,
) -> dict[str, Any]:
    old_by_id = {str(item.get("id")): item for item in old_catalog.get("items", []) if item.get("id")}
    merged: dict[str, dict[str, Any]] = {}

    for report_id, old_item in old_by_id.items():
        item = dict(old_item)
        item["present_in_latest_scan"] = False
        item.setdefault("available", bool(item.get("r2_synced")))
        merged[report_id] = item

    for report_id, current_item in current.items():
        old_item = merged.get(report_id, {})
        item = {**old_item, **current_item}
        old_dates = set(old_item.get("date_folders", []))
        new_dates = set(current_item.get("date_folders", []))
        item["date_folders"] = sorted(old_dates | new_dates, reverse=True)
        item["first_seen_at_bjt"] = old_item.get("first_seen_at_bjt") or now_bjt
        item["last_seen_at_bjt"] = now_bjt
        item["r2_synced"] = bool(old_item.get("r2_synced")) or bool(current_item.get("r2_synced"))
        item["available"] = bool(old_item.get("available")) or bool(current_item.get("available"))
        merged[report_id] = item

    items = sorted(
        merged.values(),
        key=lambda item: (str(item.get("date_folder", "")), str(item.get("title", "")).lower()),
        reverse=True,
    )
    return {
        "schema_version": 1,
        "updated_at_bjt": now_bjt,
        "dropbox_root": dropbox_root,
        "item_count": len(items),
        "items": items,
    }


def sync_current_reports_to_r2(
    catalog: dict[str, Any],
    current_ids: set[str],
    download_paths: dict[str, str],
    token: str,
    force_upload: bool,
) -> int:
    bucket = require_env("R2_BUCKET")
    client = build_r2_client()
    by_id = {str(item.get("id")): item for item in catalog.get("items", []) if item.get("id")}
    uploaded = 0

    with tempfile.TemporaryDirectory(prefix="kc-desk-notes-") as tmpdir:
        tmp_root = Path(tmpdir)
        for report_id in sorted(current_ids):
            item = by_id.get(report_id)
            dropbox_path = download_paths.get(report_id)
            if not item or not dropbox_path:
                continue
            if item.get("r2_synced") and not force_upload:
                item["available"] = True
                continue

            key = str(item.get("r2_key") or r2_key_for_id(report_id, DEFAULT_R2_PREFIX))
            local_path = tmp_root / f"{report_id}.pdf"
            log(f"Mirroring to R2: {report_id} -> {key}")
            download_dropbox_file(token, dropbox_path, local_path)
            upload_pdf_to_r2(client, bucket, key, local_path)
            item["r2_synced"] = True
            item["available"] = True
            uploaded += 1

    catalog["items"] = sorted(
        by_id.values(),
        key=lambda item: (str(item.get("date_folder", "")), str(item.get("title", "")).lower()),
        reverse=True,
    )
    catalog["item_count"] = len(catalog["items"])
    return uploaded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dropbox-root", default="/zip_backup")
    parser.add_argument("--days", type=int, default=0, help="Latest date folders to scan. 0 scans all current date folders.")
    parser.add_argument("--catalog-path", default="kc_desk_notes/data/catalog.json")
    parser.add_argument("--password-rules", default="kc_desk_notes/password_rules.json")
    parser.add_argument("--r2-prefix", default=os.getenv("R2_OBJECT_PREFIX", DEFAULT_R2_PREFIX))
    parser.add_argument("--sync-r2", action="store_true")
    parser.add_argument("--force-upload", action="store_true")
    args = parser.parse_args()

    try:
        if args.days < 0:
            raise ValueError("--days must be 0 or greater")

        root = args.dropbox_root.rstrip("/") or ""
        catalog_path = Path(args.catalog_path)
        password_rules = load_password_rules(Path(args.password_rules))
        old_catalog = load_json(catalog_path, {"schema_version": 1, "items": []})
        now = bjt_now()

        token = dropbox_access_token()
        folders = choose_date_folders(token, root, args.days)
        folder_names = ", ".join(str(folder.get("name")) for folder in folders)
        log(f"Scanning Dropbox date folders: {folder_names}")

        current, download_paths = collect_current_reports(token, root, folders, password_rules, args.r2_prefix)
        catalog = merge_catalog(old_catalog, current, root, now)

        uploaded = 0
        if args.sync_r2:
            uploaded = sync_current_reports_to_r2(
                catalog=catalog,
                current_ids=set(current.keys()),
                download_paths=download_paths,
                token=token,
                force_upload=args.force_upload,
            )

        write_json(catalog_path, catalog)
        write_github_output("catalog_path", str(catalog_path))
        write_github_output("item_count", str(catalog.get("item_count", 0)))
        write_github_output("seen_count", str(len(current)))
        write_github_output("uploaded_count", str(uploaded))
        log(f"Wrote {catalog_path}: {catalog.get('item_count', 0)} total reports, {len(current)} seen, {uploaded} uploaded")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
