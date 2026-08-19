#!/usr/bin/env python3
"""Notify IndexNow about canonical Portal Suite pages changed by a deployment."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://portal.example.invalid"
DEFAULT_ENDPOINT = "https://api.indexnow.org/indexnow"
DEFAULT_KEY = "b7c3e9a41d8f52e604a71bc93f2d6e80"
MAX_URLS_PER_REQUEST = 10_000
FINGERPRINT_KEYS = (
    "title",
    "title_zh",
    "filename",
    "date_folder",
    "bank_code",
    "bank_name",
    "industry",
    "sector",
    "category",
    "page_count",
    "available",
    "pdf_archived",
    "server_modified",
)


def load_catalog(path: Path | None) -> dict[str, Any]:
    if not path or not path.exists():
        return {"items": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"items": []}


def merge_catalogs(paths: list[Path]) -> dict[str, Any]:
    merged: dict[str, dict[str, Any]] = {}
    for path in paths:
        merged.update(item_map(load_catalog(path)))
    return {"items": list(merged.values())}


def item_map(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(item.get("id")): item
        for item in catalog.get("items", [])
        if isinstance(item, dict) and item.get("id")
    }


def item_fingerprint(item: dict[str, Any]) -> str:
    values = {key: item.get(key) for key in FINGERPRINT_KEYS}
    return json.dumps(values, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def parse_date(value: str) -> datetime | None:
    match = re.search(r"(20\d{2})[-/]?(\d{2})[-/]?(\d{2})", str(value or ""))
    if not match:
        return None
    try:
        return datetime(
            int(match.group(1)),
            int(match.group(2)),
            int(match.group(3)),
            tzinfo=timezone.utc,
        )
    except ValueError:
        return None


def item_effective_date(item: dict[str, Any]) -> datetime | None:
    for key in ("server_modified", "first_seen_at_bjt", "date_folder", "last_seen_at_bjt"):
        parsed = parse_date(str(item.get(key) or ""))
        if parsed:
            return parsed
    return None


def report_url(base_url: str, report_id: str) -> str:
    return f"{base_url.rstrip('/')}/reports/{quote(report_id, safe='')}.html"


def discover_public_site_urls(site_dir: Path | None, base_url: str) -> list[str]:
    if not site_dir or not site_dir.is_dir():
        return []
    base = base_url.rstrip("/")
    urls: list[str] = []
    fixed = {
        "blog/index.html": f"{base}/blog/",
        "reports/topics.html": f"{base}/reports/topics.html",
        "about.html": f"{base}/about.html",
        "charts.html": f"{base}/charts",
    }
    for relative, url in fixed.items():
        if site_dir.joinpath(*relative.split("/")).is_file():
            urls.append(url)
    blog_dir = site_dir / "blog"
    if blog_dir.is_dir():
        for path in sorted(blog_dir.glob("*.html")):
            relative = path.relative_to(site_dir).as_posix()
            if relative == "blog/index.html":
                continue
            urls.append(f"{base}/{quote(relative, safe='/.-_~')}")
    return list(dict.fromkeys(urls))


def changed_urls(
    catalog: dict[str, Any],
    previous_catalog: dict[str, Any],
    base_url: str,
    lookback_days: int,
) -> list[str]:
    current = item_map(catalog)
    previous = item_map(previous_catalog)

    if previous:
        changed_ids = {
            report_id
            for report_id, item in current.items()
            if report_id not in previous or item_fingerprint(item) != item_fingerprint(previous[report_id])
        }
        changed_ids.update(set(previous) - set(current))
    else:
        as_of = parse_date(str(catalog.get("updated_at_bjt") or "")) or datetime.now(timezone.utc)
        cutoff = as_of - timedelta(days=max(0, lookback_days))
        changed_ids = {
            report_id
            for report_id, item in current.items()
            if (item_effective_date(item) or datetime.min.replace(tzinfo=timezone.utc)) >= cutoff
        }

    base = base_url.rstrip("/")
    urls = [
        f"{base}/",
        f"{base}/reports/",
        f"{base}/reports/topics.html",
        f"{base}/reports/institutions/bernstein/",
        f"{base}/blog/",
        f"{base}/feed.xml",
    ]
    urls.extend(report_url(base, report_id) for report_id in sorted(changed_ids))
    return list(dict.fromkeys(urls))


def verify_key_file(key_location: str, key: str, attempts: int = 6) -> None:
    last_error = ""
    for attempt in range(attempts):
        try:
            request = Request(key_location, headers={"User-Agent": "PortalSuite-IndexNow/1.0"})
            with urlopen(request, timeout=20) as response:
                body = response.read().decode("utf-8", errors="replace").strip()
                if response.status == 200 and body == key:
                    return
                last_error = f"HTTP {response.status}"
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
        if attempt + 1 < attempts:
            time.sleep(min(30, 5 * (attempt + 1)))
    raise RuntimeError(f"IndexNow key file is not live at {key_location}: {last_error}")


def submit_chunk(
    endpoint: str,
    host: str,
    key: str,
    key_location: str,
    urls: list[str],
) -> None:
    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    last_error = ""
    for attempt in range(4):
        try:
            request = Request(
                endpoint,
                data=body,
                headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "PortalSuite-IndexNow/1.0"},
                method="POST",
            )
            with urlopen(request, timeout=30) as response:
                if response.status in {200, 202}:
                    return
                last_error = f"HTTP {response.status}: {response.read(300).decode('utf-8', errors='replace')}"
        except HTTPError as exc:
            response_text = exc.read(300).decode("utf-8", errors="replace")
            last_error = f"HTTP {exc.code}: {response_text}"
            if exc.code not in {429, 500, 502, 503, 504}:
                break
        except (URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
        if attempt < 3:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"IndexNow submission failed: {last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", default="portal_suite/data/catalog.json")
    parser.add_argument("--previous-catalog", action="append", default=[])
    parser.add_argument("--site-dir", default="")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--key", default=os.environ.get("INDEXNOW_KEY") or DEFAULT_KEY)
    parser.add_argument("--lookback-days", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-key-check", action="store_true")
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Fa-f0-9]{8,128}", args.key):
        raise SystemExit("INDEXNOW_KEY must be 8-128 hexadecimal characters")

    catalog = load_catalog(Path(args.catalog))
    previous_paths = [Path(value) for value in args.previous_catalog if value]
    previous = merge_catalogs(previous_paths) if previous_paths else {"items": []}
    urls = changed_urls(catalog, previous, args.base_url, args.lookback_days)
    urls = list(dict.fromkeys([
        *urls,
        *discover_public_site_urls(Path(args.site_dir) if args.site_dir else None, args.base_url),
    ]))
    key_location = f"{args.base_url.rstrip('/')}/{args.key}.txt"
    summary = {
        "url_count": len(urls),
        "key_location": key_location,
        "sample": urls[:10],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.dry_run:
        return 0

    if not args.skip_key_check:
        verify_key_file(key_location, args.key)

    host = args.base_url.removeprefix("https://").removeprefix("http://").split("/", 1)[0]
    for start in range(0, len(urls), MAX_URLS_PER_REQUEST):
        chunk = urls[start:start + MAX_URLS_PER_REQUEST]
        submit_chunk(args.endpoint, host, args.key, key_location, chunk)
        print(f"Submitted {len(chunk)} URLs to IndexNow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
