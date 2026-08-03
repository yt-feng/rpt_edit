#!/usr/bin/env python3
"""Fetch new ARK Invest RSS items into the daily report pipeline.

ARK's item pages are Cloudflare-challenged, but the RSS feed is public and carries
stable metadata. This script writes feed items as source_mineru.md-style folders so
the existing Portal translated -> WeChat -> market views pipeline can reuse them.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any


DEFAULT_FEED_URL = "https://www.ark-invest.com/feed"
DEFAULT_TYPES = "Articles,Newsletters,White Papers,Crypto Reports"
DATE_DIR_RE = re.compile(r"^\d{6,8}$")
HTML_TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.I | re.S)
KEEP_HTML_BREAK_RE = re.compile(r"</?(?:p|div|section|article|br|li|ul|ol|h[1-6])[^>]*>", re.I)
ARK_INSTITUTION_NAME = "木头姐ARK"


def log(message: str) -> None:
    print(message, flush=True)


def shanghai_today() -> str:
    return (datetime.now(timezone.utc) + timedelta(hours=8)).strftime("%y%m%d")


def parse_date(value: str) -> datetime | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        return parsedate_to_datetime(text).astimezone(timezone.utc)
    except Exception:
        pass
    try:
        normalized = text.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized).astimezone(timezone.utc)
    except Exception:
        return None


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text or "")).strip()


def slug(value: str, max_len: int = 88) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return (value or "ark-item")[:max_len]


def item_key(link: str, guid: str, title: str) -> str:
    raw = normalize_space(guid or link or title)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def fetch_text(url: str, timeout: int) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 PortalSuiteARKFeed/1.0",
            "Accept": "application/rss+xml,application/xml,text/xml,text/html;q=0.8,*/*;q=0.5",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace").lstrip("\ufeff")


def html_to_markdownish(value: str) -> str:
    text = html.unescape(value or "")
    text = SCRIPT_STYLE_RE.sub(" ", text)
    text = KEEP_HTML_BREAK_RE.sub("\n", text)
    text = HTML_TAG_RE.sub(" ", text)
    lines = [normalize_space(line) for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n\n".join(lines).strip()


def first_text(item: ET.Element, names: list[str], namespaces: dict[str, str]) -> str:
    for name in names:
        if ":" in name:
            value = item.findtext(name, namespaces=namespaces)
        else:
            value = item.findtext(name)
        if value:
            return value
    return ""


def parse_feed(xml_text: str) -> list[dict[str, Any]]:
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
        "content": "http://purl.org/rss/1.0/modules/content/",
    }
    root = ET.fromstring(xml_text)
    channel = root.find("channel")
    if channel is None:
        return []
    items: list[dict[str, Any]] = []
    for item in channel.findall("item"):
        title = normalize_space(item.findtext("title") or "")
        link = normalize_space(item.findtext("link") or "")
        guid = normalize_space(item.findtext("guid") or link)
        item_type = normalize_space(item.findtext("type") or item.findtext("category") or "")
        category = normalize_space(item.findtext("category") or item_type)
        description = html_to_markdownish(item.findtext("description") or "")
        content = html_to_markdownish(first_text(item, ["content:encoded"], namespaces))
        pub_date = normalize_space(item.findtext("pubDate") or "")
        updated = normalize_space(first_text(item, ["atom:updated"], namespaces))
        pub_dt = parse_date(pub_date)
        updated_dt = parse_date(updated)
        event_dt = max([dt for dt in [pub_dt, updated_dt] if dt], default=None)
        if not title or not link:
            continue
        items.append(
            {
                "key": item_key(link, guid, title),
                "title": title,
                "link": link,
                "guid": guid,
                "type": item_type,
                "category": category,
                "description": description,
                "content": content,
                "pub_date": pub_date,
                "updated": updated,
                "pub_datetime": pub_dt.isoformat() if pub_dt else "",
                "updated_datetime": updated_dt.isoformat() if updated_dt else "",
                "event_datetime": event_dt.isoformat() if event_dt else "",
            }
        )
    return items


def should_select(
    item: dict[str, Any],
    allowed_types: set[str],
    cutoff: datetime,
    max_pub_age_cutoff: datetime,
    seen: dict[str, Any],
) -> bool:
    item_type = str(item.get("type") or "").strip().lower()
    if allowed_types and item_type not in allowed_types:
        return False
    if item["key"] in seen:
        return False
    pub_dt = parse_date(str(item.get("pub_datetime") or ""))
    updated_dt = parse_date(str(item.get("updated_datetime") or ""))
    if pub_dt and pub_dt >= cutoff:
        return True
    if updated_dt and updated_dt >= cutoff:
        # ARK occasionally rebuilds old pages, making many stale items look updated.
        # Keep updated items only when the original publication is still recent.
        return pub_dt is None or pub_dt >= max_pub_age_cutoff
    return False


def source_markdown(item: dict[str, Any]) -> str:
    body = item.get("content") or item.get("description") or ""
    if not body:
        body = "ARK Invest RSS feed did not include a body for this item."
    title = normalize_space(str(item.get("title") or "ARK Invest update"))
    lines = [
        f"# {ARK_INSTITUTION_NAME}：{title}",
        "",
        f"Source: ARK Invest RSS feed",
        f"Type: {item.get('type') or item.get('category') or 'Feed item'}",
        f"Published: {item.get('pub_date') or item.get('pub_datetime') or ''}",
        f"Updated: {item.get('updated') or item.get('updated_datetime') or ''}",
        f"URL: {item.get('link') or ''}",
        "",
        "## Feed摘要",
        "",
        str(item.get("description") or "").strip(),
        "",
        "## 原始材料",
        "",
        body.strip(),
    ]
    return "\n".join(line for line in lines if line is not None).strip() + "\n"


def note_markdown(item: dict[str, Any]) -> str:
    title = normalize_space(str(item.get("title") or "ARK Invest update"))
    desc = normalize_space(str(item.get("description") or ""))
    return (
        f"# {ARK_INSTITUTION_NAME}：{title}\n\n"
        f"{desc}\n\n"
        f"来源：{item.get('link') or ''}\n"
    )


def write_item(item: dict[str, Any], output_date_dir: Path, index: int) -> dict[str, Any]:
    safe_title = slug(str(item.get("title") or "ark-item"), 72)
    item_dir = output_date_dir / f"{index:04d}-ARK_{safe_title}_{item['key']}"
    item_dir.mkdir(parents=True, exist_ok=True)
    (item_dir / "source_mineru.md").write_text(source_markdown(item), encoding="utf-8")
    (item_dir / "note.md").write_text(note_markdown(item), encoding="utf-8")
    status = {
        "source": "ark_invest_feed",
        "institution_name": ARK_INSTITUTION_NAME,
        "title": item.get("title"),
        "type": item.get("type"),
        "category": item.get("category"),
        "source_url": item.get("link"),
        "guid": item.get("guid"),
        "pub_date": item.get("pub_date"),
        "updated": item.get("updated"),
        "event_datetime": item.get("event_datetime"),
        "feed_key": item.get("key"),
        "source_mineru": "source_mineru.md",
        "note": "note.md",
    }
    write_json(item_dir / "status.json", status)
    return {**status, "output_dir": str(item_dir)}


def set_github_output(date_folder: str, article_count: int) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as handle:
        handle.write(f"date_folder={date_folder}\n")
        handle.write(f"article_count={article_count}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch new ARK Invest RSS items into xhs_notes/ark.")
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--output-root", default="xhs_notes/ark")
    parser.add_argument("--date", default=shanghai_today())
    parser.add_argument("--since-days", type=int, default=1)
    parser.add_argument("--max-pub-age-days", type=int, default=120,
                        help="For updated-but-not-new items, require pubDate within this many days.")
    parser.add_argument("--max-items", default="5", help="Positive integer or all")
    parser.add_argument("--include-types", default=DEFAULT_TYPES)
    parser.add_argument("--seen-state-path", default="ark_invest_feed/seen_state.json")
    parser.add_argument("--archive-path", default="ark_invest_feed/archive.jsonl")
    parser.add_argument("--manifest-path", default="ark_invest_feed/ark_feed_run_manifest.json")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    if not DATE_DIR_RE.match(args.date):
        raise ValueError("--date must be YYMMDD or YYYYMMDD style digits")
    allowed_types = {item.strip().lower() for item in args.include_types.split(",") if item.strip()}
    max_items = None if str(args.max_items).strip().lower() in {"all", "*", "0"} else int(args.max_items)
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=max(0, args.since_days))
    max_pub_age_cutoff = now - timedelta(days=max(0, args.max_pub_age_days))

    state_path = Path(args.seen_state_path)
    state = load_json(state_path)
    seen = state.setdefault("seen", {})
    if not isinstance(seen, dict):
        seen = {}
        state["seen"] = seen

    feed_xml = fetch_text(args.feed_url, args.timeout)
    items = parse_feed(feed_xml)
    selected = [item for item in items if should_select(item, allowed_types, cutoff, max_pub_age_cutoff, seen)]
    selected.sort(key=lambda item: item.get("pub_datetime") or item.get("event_datetime") or "", reverse=True)
    if max_items is not None:
        selected = selected[:max_items]

    output_date_dir = Path(args.output_root) / args.date
    output_date_dir.mkdir(parents=True, exist_ok=True)
    written = [write_item(item, output_date_dir, idx) for idx, item in enumerate(selected, 1)]

    processed_at = datetime.now(timezone.utc).isoformat()
    if written:
        for item, record in zip(selected, written):
            seen[item["key"]] = {
                "title": item.get("title"),
                "link": item.get("link"),
                "type": item.get("type"),
                "event_datetime": item.get("event_datetime"),
                "processed_at": processed_at,
                "output_dir": record.get("output_dir"),
            }
        state["updated_at"] = processed_at
        state["feed_url"] = args.feed_url
        write_json(state_path, state)
        append_jsonl(Path(args.archive_path), written)

    manifest = {
        "feed_url": args.feed_url,
        "date_folder": args.date,
        "since_days": args.since_days,
        "max_pub_age_days": args.max_pub_age_days,
        "include_types": sorted(allowed_types),
        "feed_item_count": len(items),
        "selected_count": len(selected),
        "written": written,
        "status": "ok",
    }
    write_json(Path(args.manifest_path), manifest)
    set_github_output(args.date, len(written))
    log(f"Fetched ARK feed items={len(items)} selected={len(written)} output={output_date_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
