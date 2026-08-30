#!/usr/bin/env python3
"""Notify IndexNow about canonical Portal Suite pages changed by a deployment."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


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


def url_identity(value: str) -> tuple[str, str, str] | None:
    """Return the origin and decoded path used for canonical comparisons."""
    parsed = urlsplit(str(value or "").strip())
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.query:
        return None
    try:
        port = f":{parsed.port}" if parsed.port else ""
    except ValueError:
        return None
    path = unquote(parsed.path or "/")
    return parsed.scheme.lower(), f"{parsed.hostname.lower()}{port}", path


def load_sitemap(path: Path | None) -> dict[str, str]:
    """Load canonical URL/lastmod pairs from a local urlset or sitemap index.

    Sitemap indexes are followed only through sibling files already present on
    disk. The release workflow deliberately supplies the flat public sitemap so
    this function never needs to fetch arbitrary URLs.
    """
    if not path or not path.is_file():
        return {}

    entries: dict[str, str] = {}
    visited: set[Path] = set()

    def visit(current: Path) -> None:
        resolved = current.resolve()
        if resolved in visited or not current.is_file():
            return
        visited.add(resolved)
        try:
            root = ET.parse(current).getroot()
        except (OSError, ET.ParseError):
            return
        kind = root.tag.rsplit("}", 1)[-1]
        if kind == "urlset":
            for row in root.findall("./{*}url"):
                loc = compact_xml_text(row.find("./{*}loc"))
                identity = url_identity(loc)
                if not identity:
                    continue
                entries[loc] = compact_xml_text(row.find("./{*}lastmod"))
            return
        if kind != "sitemapindex":
            return
        for row in root.findall("./{*}sitemap"):
            loc = compact_xml_text(row.find("./{*}loc"))
            filename = Path(urlsplit(loc).path).name
            if filename:
                visit(current.parent / filename)

    visit(path)
    return entries


def compact_xml_text(node: ET.Element | None) -> str:
    return " ".join(str(node.text or "").split()) if node is not None else ""


class _DiscoveryHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []
        self.robots: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {str(key).lower(): str(value or "") for key, value in attrs}
        if tag.lower() == "link" and "canonical" in values.get("rel", "").lower().split():
            if values.get("href"):
                self.canonicals.append(values["href"].strip())
        if tag.lower() == "meta" and values.get("name", "").lower() in {"robots", "googlebot", "bingbot"}:
            self.robots.append(values.get("content", ""))


def site_path_for_url(site_dir: Path, url: str, base_url: str) -> Path | None:
    identity = url_identity(url)
    base_identity = url_identity(base_url.rstrip("/") + "/")
    if not identity or not base_identity or identity[:2] != base_identity[:2]:
        return None
    decoded_path = identity[2]
    parts = [part for part in decoded_path.split("/") if part]
    if any(part in {".", ".."} for part in parts):
        return None
    if decoded_path.endswith("/"):
        relative = Path(*parts, "index.html") if parts else Path("index.html")
    else:
        relative = Path(*parts) if parts else Path("index.html")
    candidate = site_dir / relative
    if not candidate.is_file() and not candidate.suffix:
        html_candidate = candidate.with_suffix(".html")
        if html_candidate.is_file():
            candidate = html_candidate
    return candidate


def is_indexable_self_canonical(site_dir: Path, url: str, base_url: str) -> bool:
    path = site_path_for_url(site_dir, url, base_url)
    if not path or not path.is_file() or path.suffix.lower() != ".html":
        return False
    try:
        parser = _DiscoveryHtmlParser()
        parser.feed(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError):
        return False
    if any("noindex" in {token.strip().lower() for token in re.split(r"[,\s]+", value)} for value in parser.robots):
        return False
    expected = url_identity(url)
    return bool(expected and any(url_identity(value) == expected for value in parser.canonicals))


def is_planned_retirement(site_dir: Path, url: str, base_url: str) -> bool:
    """A missing release file will resolve as 404 after the static slot switch.

    Existing noindex/meta-refresh compatibility files are intentionally not
    treated as retired URLs because they still return HTTP 200.
    """
    path = site_path_for_url(site_dir, url, base_url)
    return bool(path is not None and not path.exists())


@dataclass
class SubmissionPlan:
    reasons_by_url: dict[str, set[str]] = field(default_factory=dict)
    skipped_reason_counts: Counter[str] = field(default_factory=Counter)

    def add(self, url: str, reason: str) -> None:
        self.reasons_by_url.setdefault(url, set()).add(reason)

    @property
    def urls(self) -> list[str]:
        return sorted(self.reasons_by_url)

    @property
    def reason_counts(self) -> dict[str, int]:
        counts = Counter(
            reason
            for reasons in self.reasons_by_url.values()
            for reason in reasons
        )
        return dict(sorted(counts.items()))


def is_blog_article_url(url: str, base_url: str) -> bool:
    identity = url_identity(url)
    base_identity = url_identity(base_url.rstrip("/") + "/")
    if not identity or not base_identity or identity[:2] != base_identity[:2]:
        return False
    return bool(re.fullmatch(r"/blog/(?!page-\d+\.html$)[^/]+\.html", identity[2]))


def is_bernstein_item(item: dict[str, Any] | None) -> bool:
    if not item:
        return False
    haystack = " ".join(
        str(item.get(key) or "")
        for key in ("bank_code", "bank_name", "institution", "title", "title_zh", "filename")
    ).lower()
    return any(value in haystack for value in ("bernstein", "sanford c. bernstein", "伯恩斯坦"))


def build_submission_plan(
    catalog: dict[str, Any],
    previous_catalog: dict[str, Any],
    current_sitemap: dict[str, str],
    previous_sitemap: dict[str, str],
    site_dir: Path,
    base_url: str,
    lookback_days: int,
) -> SubmissionPlan:
    """Build a deployment delta containing only canonical, indexable URLs."""
    plan = SubmissionPlan()
    base = base_url.rstrip("/")
    current = item_map(catalog)
    previous = item_map(previous_catalog)

    if previous:
        added_reports = set(current) - set(previous)
        catalog_updated_reports = {
            report_id
            for report_id in set(current) & set(previous)
            if item_fingerprint(current[report_id]) != item_fingerprint(previous[report_id])
        }
        retired_reports = set(previous) - set(current)
    else:
        as_of = parse_date(str(catalog.get("updated_at_bjt") or "")) or datetime.now(timezone.utc)
        cutoff = as_of - timedelta(days=max(0, lookback_days))
        added_reports = {
            report_id
            for report_id, item in current.items()
            if (item_effective_date(item) or datetime.min.replace(tzinfo=timezone.utc)) >= cutoff
        }
        catalog_updated_reports = set()
        retired_reports = set()

    # A material report-page template release can change canonical HTML while
    # leaving the public catalog item untouched.  The sitemap lastmod is the
    # stable page-level revision signal for that case; it must not be discarded
    # merely because report URLs have their own catalog-delta path.
    sitemap_updated_reports = {
        report_id
        for report_id in set(current) & set(previous)
        if (
            (url := report_url(base, report_id)) in current_sitemap
            and url in previous_sitemap
            and current_sitemap[url]
            and current_sitemap[url] != previous_sitemap[url]
        )
    }
    updated_reports = catalog_updated_reports | sitemap_updated_reports

    def add_current(url: str, reason: str) -> None:
        if url not in current_sitemap:
            plan.skipped_reason_counts["current_not_in_canonical_sitemap"] += 1
            return
        if not is_indexable_self_canonical(site_dir, url, base_url):
            plan.skipped_reason_counts["current_not_indexable_self_canonical"] += 1
            return
        plan.add(url, reason)

    def add_retired(url: str, reason: str) -> None:
        if url not in previous_sitemap:
            plan.skipped_reason_counts["retired_not_in_previous_sitemap"] += 1
            return
        if url in current_sitemap:
            plan.skipped_reason_counts["retired_still_in_current_sitemap"] += 1
            return
        if not is_planned_retirement(site_dir, url, base_url):
            plan.skipped_reason_counts["retired_not_301_404_410"] += 1
            return
        plan.add(url, reason)

    for report_id in sorted(added_reports):
        add_current(report_url(base, report_id), "report_added")
    for report_id in sorted(catalog_updated_reports):
        add_current(report_url(base, report_id), "report_updated")
    for report_id in sorted(sitemap_updated_reports - catalog_updated_reports):
        add_current(report_url(base, report_id), "report_page_updated")
    for report_id in sorted(retired_reports):
        add_retired(report_url(base, report_id), "report_retired")

    current_blog = {url: lastmod for url, lastmod in current_sitemap.items() if is_blog_article_url(url, base)}
    previous_blog = {url: lastmod for url, lastmod in previous_sitemap.items() if is_blog_article_url(url, base)}
    if previous_sitemap:
        added_blog = set(current_blog) - set(previous_blog)
        updated_blog = {
            url
            for url in set(current_blog) & set(previous_blog)
            if current_blog[url] and current_blog[url] != previous_blog[url]
        }
        retired_blog = set(previous_blog) - set(current_blog)
    else:
        as_of = parse_date(str(catalog.get("updated_at_bjt") or "")) or datetime.now(timezone.utc)
        cutoff = as_of - timedelta(days=max(0, lookback_days))
        added_blog = {
            url
            for url, lastmod in current_blog.items()
            if (parse_date(lastmod) or datetime.min.replace(tzinfo=timezone.utc)) >= cutoff
        }
        updated_blog = set()
        retired_blog = set()

    for url in sorted(added_blog):
        add_current(url, "blog_added")
    for url in sorted(updated_blog):
        add_current(url, "blog_updated")
    for url in sorted(retired_blog):
        add_retired(url, "blog_retired")

    report_detail_urls = {
        report_url(base, report_id)
        for report_id in set(current) | set(previous)
    }
    blog_article_urls = {
        url
        for url in set(current_sitemap) | set(previous_sitemap)
        if is_blog_article_url(url, base)
    }

    def other_public_pages(sitemap: dict[str, str]) -> dict[str, str]:
        base_identity = url_identity(f"{base}/")
        return {
            url: lastmod
            for url, lastmod in sitemap.items()
            if (identity := url_identity(url))
            and base_identity
            and identity[:2] == base_identity[:2]
            and url not in report_detail_urls
            and url not in blog_article_urls
        }

    current_pages = other_public_pages(current_sitemap)
    previous_pages = other_public_pages(previous_sitemap)
    added_pages = set(current_pages) - set(previous_pages)
    updated_pages = {
        url
        for url in set(current_pages) & set(previous_pages)
        if current_pages[url] and current_pages[url] != previous_pages[url]
    }
    retired_pages = set(previous_pages) - set(current_pages)
    for url in sorted(added_pages):
        add_current(url, "page_added")
    for url in sorted(updated_pages):
        add_current(url, "page_updated")
    for url in sorted(retired_pages):
        add_retired(url, "page_retired")

    report_delta = bool(added_reports or updated_reports or retired_reports)
    blog_delta = bool(added_blog or updated_blog or retired_blog)
    if report_delta or blog_delta:
        add_current(f"{base}/", "aggregate_home")
    if report_delta:
        add_current(f"{base}/reports/", "aggregate_reports")
        add_current(f"{base}/reports/topics.html", "aggregate_topics")
    bernstein_delta = any(
        is_bernstein_item(current.get(report_id) or previous.get(report_id))
        for report_id in added_reports | updated_reports | retired_reports
    )
    if bernstein_delta or blog_delta:
        add_current(f"{base}/reports/institutions/bernstein/", "aggregate_institution")
    if blog_delta:
        add_current(f"{base}/blog/", "aggregate_blog")
    return plan


def discover_public_site_urls(site_dir: Path | None, base_url: str) -> list[str]:
    """Legacy helper retained for callers; deployment submission does not use it."""
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
    """Legacy catalog-only helper; deployment submission uses a sitemap-backed plan."""
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
    parser.add_argument("--sitemap", default="")
    parser.add_argument("--previous-sitemap", default="")
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
    missing_previous = [str(path) for path in previous_paths if not path.is_file()]
    if missing_previous:
        raise SystemExit(f"Previous public catalog is missing: {', '.join(missing_previous)}")
    previous = merge_catalogs(previous_paths) if previous_paths else {"items": []}
    site_dir = Path(args.site_dir) if args.site_dir else Path("__missing_static_release__")
    sitemap_path = Path(args.sitemap) if args.sitemap else site_dir / "sitemap-baidu.xml"
    previous_sitemap_path = Path(args.previous_sitemap) if args.previous_sitemap else None
    current_sitemap = load_sitemap(sitemap_path)
    previous_sitemap = load_sitemap(previous_sitemap_path)
    if args.sitemap and not current_sitemap:
        raise SystemExit(f"Current canonical sitemap is missing or empty: {sitemap_path}")
    if args.previous_sitemap and not previous_sitemap:
        raise SystemExit(f"Previous canonical sitemap is missing or empty: {previous_sitemap_path}")
    plan = build_submission_plan(
        catalog,
        previous,
        current_sitemap,
        previous_sitemap,
        site_dir,
        args.base_url,
        args.lookback_days,
    )
    urls = plan.urls
    key_location = f"{args.base_url.rstrip('/')}/{args.key}.txt"
    summary = {
        "url_count": len(urls),
        "reason_counts": plan.reason_counts,
        "skipped_reason_counts": dict(sorted(plan.skipped_reason_counts.items())),
        "key_location": key_location,
        "sample": urls[:10],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.dry_run or not urls:
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
