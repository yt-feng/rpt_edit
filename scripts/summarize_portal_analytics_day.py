#!/usr/bin/env python3
"""Build a privacy-preserving daily portal analytics summary from private R2 events.

The output intentionally excludes visitor IDs, IP hashes, full referrer URLs, user
email addresses, and raw user-agent strings. It is suitable for a short-lived,
authenticated Actions artifact or the private admin dashboard.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit


PRIMARY_PREFIX = "_analytics/events"
BACKUP_PREFIX = "_analytics_backup/events"
BOT_RE = re.compile(
    r"(?:bot|spider|crawler|headless|python|curl|wget|scrapy|httpclient|preview|monitor)",
    re.IGNORECASE,
)


def clean_text(value: Any, limit: int = 240) -> str:
    return re.sub(r"[\x00-\x1f\x7f]+", "", str(value or "")).strip()[:limit]


def path_only(value: Any) -> str:
    text = clean_text(value, 1000)
    if not text:
        return "/"
    try:
        parsed = urlsplit(text)
        path = parsed.path or "/"
    except ValueError:
        path = text.split("?", 1)[0].split("#", 1)[0] or "/"
    return path[:300]


def referrer_host(value: Any) -> str:
    text = clean_text(value, 1000)
    if not text:
        return "(direct)"
    try:
        host = (urlsplit(text).hostname or "").lower().rstrip(".")
    except ValueError:
        host = ""
    return host[:160] or "(direct)"


def user_agent_groups(value: Any) -> tuple[str, str, bool]:
    ua = clean_text(value, 1000)
    is_bot = bool(BOT_RE.search(ua))
    if is_bot:
        browser = "Bot/automation"
    elif re.search(r"Edg(?:e|A|iOS)?/", ua):
        browser = "Edge"
    elif re.search(r"(?:Chrome|CriOS)/", ua):
        browser = "Chrome"
    elif "Firefox/" in ua or "FxiOS/" in ua:
        browser = "Firefox"
    elif "Safari/" in ua:
        browser = "Safari"
    else:
        browser = "Other/unknown"
    if is_bot:
        device = "Bot/automation"
    elif re.search(r"Mobile|Android|iPhone|iPad|iPod", ua, re.IGNORECASE):
        device = "Mobile/tablet"
    else:
        device = "Desktop/unknown"
    return browser, device, is_bot


def hour_bucket(value: Any) -> str:
    text = clean_text(value, 40)
    if not text:
        return "unknown"
    try:
        instant = datetime.fromisoformat(text.replace("Z", "+00:00"))
        hour = (instant.hour + 8) % 24
        return f"{hour:02d}:00"
    except ValueError:
        return "unknown"


def top_rows(counter: Counter[str], limit: int = 20) -> list[dict[str, Any]]:
    return [{"value": key, "count": count} for key, count in counter.most_common(limit)]


def build_summary(events: Iterable[dict[str, Any]], date: str) -> dict[str, Any]:
    rows = [event for event in events if isinstance(event, dict)]
    event_types: Counter[str] = Counter()
    paths: Counter[str] = Counter()
    referrers: Counter[str] = Counter()
    countries: Counter[str] = Counter()
    browsers: Counter[str] = Counter()
    devices: Counter[str] = Counter()
    hours: Counter[str] = Counter()
    unique_keys: set[str] = set()
    bot_unique_keys: set[str] = set()
    first_page_by_visitor: dict[str, tuple[str, str]] = {}
    timestamps: list[str] = []

    for event in rows:
        event_type = clean_text(event.get("type"), 80) or "unknown"
        event_types[event_type] += 1
        timestamp = clean_text(event.get("ts"), 40)
        if timestamp:
            timestamps.append(timestamp)
        identity = clean_text(event.get("visitor_id"), 120) or clean_text(event.get("ip_hash"), 120)
        if identity:
            unique_keys.add(identity)
        browser, device, is_bot = user_agent_groups(event.get("user_agent"))
        browsers[browser] += 1
        devices[device] += 1
        if is_bot and identity:
            bot_unique_keys.add(identity)
        country = clean_text(event.get("country"), 8).upper() or "unknown"
        countries[country] += 1
        hours[hour_bucket(timestamp)] += 1

        if event_type == "page_view":
            path = path_only(event.get("path"))
            paths[path] += 1
            referrers[referrer_host(event.get("referrer"))] += 1
            if identity:
                current = first_page_by_visitor.get(identity)
                if current is None or (timestamp and timestamp < current[0]):
                    first_page_by_visitor[identity] = (timestamp, path)

    landing_paths: Counter[str] = Counter(value[1] for value in first_page_by_visitor.values())
    return {
        "schema": "portal-analytics-day-summary-v1",
        "date": date,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "totals": {
            "events": len(rows),
            "page_views": event_types.get("page_view", 0),
            "unique_visitors": len(unique_keys),
            "bot_hint_unique_visitors": len(bot_unique_keys),
            "first_event_at": min(timestamps) if timestamps else "",
            "last_event_at": max(timestamps) if timestamps else "",
        },
        "event_types": top_rows(event_types),
        "top_paths": top_rows(paths),
        "top_landing_paths": top_rows(landing_paths),
        "top_referrer_hosts": top_rows(referrers),
        "top_countries": top_rows(countries),
        "browsers": top_rows(browsers),
        "devices": top_rows(devices),
        "events_by_beijing_hour": top_rows(hours, 24),
        "privacy": {
            "raw_visitor_ids_included": False,
            "ip_hashes_included": False,
            "raw_user_agents_included": False,
            "full_referrer_urls_included": False,
        },
    }


def list_keys(client: Any, bucket: str, prefix: str) -> list[str]:
    keys: list[str] = []
    continuation = ""
    while True:
        kwargs: dict[str, Any] = {"Bucket": bucket, "Prefix": prefix, "MaxKeys": 1000}
        if continuation:
            kwargs["ContinuationToken"] = continuation
        response = client.list_objects_v2(**kwargs)
        keys.extend(str(item["Key"]) for item in response.get("Contents", []) if item.get("Key"))
        if not response.get("IsTruncated"):
            break
        continuation = clean_text(response.get("NextContinuationToken"), 4000)
        if not continuation:
            raise RuntimeError("R2 listing was truncated without a continuation token.")
    return keys


def read_event(client: Any, bucket: str, candidates: list[str]) -> dict[str, Any] | None:
    for key in candidates:
        try:
            response = client.get_object(Bucket=bucket, Key=key)
            value = json.loads(response["Body"].read().decode("utf-8"))
            if isinstance(value, dict):
                return value
        except Exception:  # Try the mirrored object before dropping a damaged row.
            continue
    return None


def load_r2_events(date: str) -> list[dict[str, Any]]:
    try:
        import boto3
        from botocore.config import Config
    except ImportError as error:  # pragma: no cover - exercised in Actions.
        raise RuntimeError("boto3 is required to read the private analytics archive.") from error

    account_id = clean_text(os.environ.get("R2_ACCOUNT_ID"), 200)
    access_key = clean_text(os.environ.get("R2_ACCESS_KEY_ID"), 300)
    secret_key = clean_text(os.environ.get("R2_SECRET_ACCESS_KEY"), 500)
    bucket = clean_text(os.environ.get("R2_BUCKET"), 240)
    if not all([account_id, access_key, secret_key, bucket]):
        raise RuntimeError("Missing private R2 configuration.")
    client = boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"}),
    )

    roots = [PRIMARY_PREFIX, BACKUP_PREFIX]
    suffix_candidates: dict[str, list[str]] = {}
    for root in roots:
        prefix = f"{root}/{date}/"
        for key in list_keys(client, bucket, prefix):
            suffix = key[len(prefix):]
            if suffix:
                suffix_candidates.setdefault(suffix, []).append(key)
    if not suffix_candidates:
        raise RuntimeError(f"No analytics events found for {date}.")
    with ThreadPoolExecutor(max_workers=24) as pool:
        events = list(pool.map(lambda item: read_event(client, bucket, item), suffix_candidates.values()))
    return [event for event in events if event is not None]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="Beijing date in YYYY-MM-DD format")
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        raise SystemExit("--date must use YYYY-MM-DD")
    events = load_r2_events(args.date)
    summary = build_summary(events, args.date)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Private daily analytics summary generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
