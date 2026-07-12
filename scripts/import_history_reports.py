#!/usr/bin/env python3
"""Import the ib_rpt_history text-only report archive into KC Desk Notes data files.

Reads the locally extracted `research_reports_full.json` (one record per PDF with
filename-derived metadata plus extracted text) and writes:

- `kc_desk_notes/data/history_catalog.json`: catalog-shaped metadata for every
  historical report. These records are text-only (`available=false`,
  `pdf_archived=true`), never uploaded to R2, and never touched by the daily
  Dropbox catalog merge.
- `kc_desk_notes/data/history_text/shard_<YYMM>.json.gz`: normalized, per-report
  capped search text keyed by report id. The site build merges these into
  `search_index_history.json`, which only the browser loads (the Worker keeps
  loading the smaller `search_index.json`).

This is a one-time import; rerunning it is idempotent because report ids derive
from the archive-relative file path.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from build_bank_report_catalog import detect_bank, sanitize_report_name
from finalize_outputs import sanitize_text

DEFAULT_SOURCE_JSON = "/Users/ytfeng/Downloads/ib_rpt_history/research_reports_full.json"
DEFAULT_TEXT_CHAR_CAP = 10000

# 文件夹名 -> 日期缺失时的兜底 date_folder（YYMM + "01"）
FOLDER_MONTH_PATTERNS = [
    (re.compile(r"^12月份"), "2512"),
    (re.compile(r"^1月份"), "2601"),
    (re.compile(r"^26年(\d{1,2})月"), None),
]


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


def clean_title(name: str) -> str:
    title = sanitize_text(sanitize_report_name(name))
    title = re.sub(r"\.pdf$", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+", " ", title).strip(" -_\t\r\n")
    if not title:
        title = Path(name).stem or "Untitled report"
    return title


def history_report_id(rel_path: str) -> str:
    return hashlib.sha256(f"ib-rpt-history:{rel_path}".encode("utf-8")).hexdigest()[:24]


def date_folder_for(record: dict) -> str:
    date_iso = record.get("date")
    if date_iso:
        return f"{date_iso[2:4]}{date_iso[5:7]}{date_iso[8:10]}"
    folder = str(record.get("folder") or "")
    for pattern, yymm in FOLDER_MONTH_PATTERNS:
        match = pattern.match(folder)
        if match:
            if yymm is None:
                yymm = f"26{int(match.group(1)):02d}"
            return f"{yymm}01"
    return "260101"


def bjt_now() -> str:
    return datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-json", default=DEFAULT_SOURCE_JSON)
    parser.add_argument("--archive-root", default="/Users/ytfeng/Downloads/ib_rpt_history",
                        help="Original PDF folder, used only to record size_bytes.")
    parser.add_argument("--catalog-out", default="kc_desk_notes/data/history_catalog.json")
    parser.add_argument("--text-dir-out", default="kc_desk_notes/data/history_text")
    parser.add_argument("--text-char-cap", type=int, default=DEFAULT_TEXT_CHAR_CAP,
                        help="Per-report normalized search text cap in characters. 0 keeps all text.")
    args = parser.parse_args()

    now = bjt_now()
    data = json.loads(Path(args.source_json).read_text(encoding="utf-8"))
    records = data["reports"] if isinstance(data, dict) else data
    archive_root = Path(args.archive_root)

    items = []
    shards: dict[str, dict[str, str]] = defaultdict(dict)
    text_count = 0
    for record in records:
        rel = str(record["file"])
        report_id = history_report_id(rel)
        original_name = Path(rel).name
        title = clean_title(original_name)
        bank_code, bank_name = detect_bank(original_name)
        date_folder = date_folder_for(record)
        size_bytes = 0
        pdf_path = archive_root / rel
        if pdf_path.exists():
            size_bytes = pdf_path.stat().st_size

        item = {
            "id": report_id,
            "title": title,
            "filename": f"{title}.pdf",
            "date_folder": date_folder,
            "date_folders": [date_folder],
            "bank_code": bank_code,
            "bank_name": bank_name,
            "password_group": "default",
            "size_bytes": size_bytes,
            "source": "ib_rpt_history",
            "r2_synced": False,
            "available": False,
            "pdf_archived": True,
            "archive_reason": "history_text_only",
            "present_in_latest_scan": False,
            "first_seen_at_bjt": now,
            "last_seen_at_bjt": now,
        }
        page_count = record.get("pages")
        if page_count:
            item["page_count"] = int(page_count)
        items.append(item)

        text = normalize_search_text(record.get("text") or "")
        if text:
            if args.text_char_cap > 0:
                text = text[: args.text_char_cap]
            shards[date_folder[:4]][report_id] = text
            text_count += 1

    items.sort(key=lambda i: (i["date_folder"], i["title"].lower()), reverse=True)
    catalog_out = Path(args.catalog_out)
    catalog_out.parent.mkdir(parents=True, exist_ok=True)
    catalog_out.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "source": "ib_rpt_history",
                "imported_at_bjt": now,
                "item_count": len(items),
                "text_item_count": text_count,
                "text_char_cap": args.text_char_cap,
                "items": items,
            },
            ensure_ascii=False,
            indent=1,
        )
        + "\n",
        encoding="utf-8",
    )

    text_dir = Path(args.text_dir_out)
    text_dir.mkdir(parents=True, exist_ok=True)
    for old_shard in text_dir.glob("shard_*.json.gz"):
        old_shard.unlink()
    total_gz = 0
    for yymm, mapping in sorted(shards.items()):
        shard_path = text_dir / f"shard_{yymm}.json.gz"
        payload = json.dumps(mapping, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        shard_path.write_bytes(gzip.compress(payload, compresslevel=9))
        total_gz += shard_path.stat().st_size
        print(f"{shard_path}: {len(mapping)} texts, {shard_path.stat().st_size / 1e6:.1f} MB gz")

    print(f"Wrote {catalog_out}: {len(items)} items ({text_count} with text), shards total {total_gz / 1e6:.1f} MB gz")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
