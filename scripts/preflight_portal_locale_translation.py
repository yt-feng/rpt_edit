#!/usr/bin/env python3
"""Diagnose translation of a small public metadata sample without building a site."""

from __future__ import annotations

import argparse
from collections import Counter, deque
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Callable
from urllib.parse import urljoin, urlsplit, urlunsplit

import build_portal_locales as builder


MAX_DOCUMENT_BYTES = 3 * 1024 * 1024
MAX_FIELD_CHARS = 600
MAX_SAMPLE_UNITS = 16
MAX_PROVIDER_REQUESTS = 6


class PreflightError(RuntimeError):
    pass


def normalize_origin(value: str) -> str:
    parsed = urlsplit(value.strip())
    if (
        parsed.scheme != "https" or not parsed.hostname
        or parsed.username or parsed.password or parsed.port is not None
        or parsed.path not in {"", "/"} or parsed.query or parsed.fragment
    ):
        raise PreflightError("LIVE_ORIGIN must be a bare HTTPS origin")
    return urlunsplit(("https", parsed.netloc.lower(), "", "", ""))


def fetch_public(url: str) -> bytes:
    import requests

    try:
        with requests.get(url, timeout=(10, 30), allow_redirects=False, stream=True) as response:
            if response.status_code != 200:
                raise PreflightError(f"Public metadata request returned HTTP {response.status_code}")
            data = bytearray()
            for chunk in response.iter_content(chunk_size=64 * 1024):
                data.extend(chunk)
                if len(data) > MAX_DOCUMENT_BYTES:
                    raise PreflightError("Public metadata document exceeds the size limit")
            return bytes(data)
    except requests.RequestException as error:
        # Requests exceptions may contain URL or request details. Report only
        # the transport error class; no credentials or request headers persist.
        raise PreflightError(f"Public metadata transport failed: {type(error).__name__}") from None


class MetadataParser(HTMLParser):
    """Select existing titles, headings, and SEO metadata, never article bodies."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.fragments: list[str] = []
        self.links: list[str] = []
        self.current_tag = ""
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(str(values["href"]))
        if tag in {"title", "h1", "h2"} and not self.current_tag:
            self.current_tag, self.text_parts = tag, []
        if tag == "meta":
            name = str(values.get("name") or values.get("property") or "").lower()
            content = str(values.get("content") or "")
            if name in builder.TRANSLATABLE_META_KEYS and 0 < len(content) <= MAX_FIELD_CHARS:
                attribute = "name" if values.get("name") else "property"
                self.fragments.append(f'<meta {attribute}="{escape(name, quote=True)}" content="{escape(content, quote=True)}">')

    def handle_data(self, data: str) -> None:
        if self.current_tag:
            self.text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != self.current_tag:
            return
        value = "".join(self.text_parts).strip()
        if 0 < len(value) <= MAX_FIELD_CHARS:
            self.fragments.append(f"<{tag}>{escape(value)}</{tag}>")
        self.current_tag, self.text_parts = "", []


def latest_blog_url(parser: MetadataParser, origin: str) -> str:
    for href in parser.links:
        candidate = urlsplit(urljoin(origin + "/blog/", href))
        if (
            candidate.scheme != "https" or candidate.netloc != urlsplit(origin).netloc
            or candidate.query or candidate.fragment
            or not re.fullmatch(r"/blog/[^/]+\.html", candidate.path)
        ):
            continue
        name = candidate.path.rsplit("/", 1)[-1]
        if name == "index.html" or re.fullmatch(r"page-\d+\.html", name):
            continue
        # The public blog index lists its most recent article first.
        return urlunsplit(candidate)
    raise PreflightError("Public blog index contains no same-origin article link")


def collect_samples(origin: str, fetcher: Callable[[str], bytes]) -> tuple[dict, dict]:
    groups: dict[str, dict] = {}
    blog_parser: MetadataParser | None = None
    for label, path in (("home", "/"), ("blog", "/blog/")):
        parser = MetadataParser()
        parser.feed(fetcher(origin + path).decode("utf-8"))
        parser.close()
        units: dict = {}
        builder.collect_html_units("\n".join(parser.fragments), units)
        groups[label] = units
        if label == "blog":
            blog_parser = parser
    assert blog_parser is not None
    parser = MetadataParser()
    parser.feed(fetcher(latest_blog_url(blog_parser, origin)).decode("utf-8"))
    parser.close()
    groups["latest-blog"] = {}
    builder.collect_html_units("\n".join(parser.fragments), groups["latest-blog"])

    catalog = json.loads(fetcher(origin + "/data/catalog_preview.json"))
    if not isinstance(catalog, dict) or not isinstance(catalog.get("items"), list):
        raise PreflightError("Public catalog preview has no items array")
    items = []
    for item in catalog["items"][:4]:
        if not isinstance(item, dict) or not item.get("id"):
            continue
        selected = {"id": str(item["id"])}
        for field in builder.CATALOG_TRANSLATABLE_FIELDS:
            value = item.get(field)
            if isinstance(value, str) and 0 < len(value) <= MAX_FIELD_CHARS:
                selected[field] = value
        items.append(selected)
    groups["catalog-preview"] = {}
    builder.collect_catalog_units({"items": items}, groups["catalog-preview"])
    if any(not units for units in groups.values()):
        raise PreflightError("A required public metadata source has no translatable sample")

    queues = {label: deque(units.values()) for label, units in groups.items()}
    selected, counts = {}, Counter()
    while len(selected) < MAX_SAMPLE_UNITS and any(queues.values()):
        for label, queue in queues.items():
            if not queue or len(selected) >= MAX_SAMPLE_UNITS:
                continue
            unit = queue.popleft()
            if unit.key not in selected and len(unit.source) <= MAX_FIELD_CHARS:
                selected[unit.key] = unit
                counts[label] += 1
    if set(counts) != set(groups):
        raise PreflightError("Public metadata sources do not provide four distinct sample groups")
    return selected, {
        "source_counts": dict(counts), "unit_count": len(selected),
        "contexts": dict(Counter(unit.context for unit in selected.values())),
        "source_characters": sum(len(unit.source) for unit in selected.values()),
    }


def run_preflight(
    *, site_url: str, diagnostics_out: Path,
    model: str = builder.DEFAULT_DEEPSEEK_MODEL,
    base_url: str = "https://api.deepseek.com",
    fetcher: Callable[[str], bytes] = fetch_public,
) -> dict:
    diagnostics_out.parent.mkdir(parents=True, exist_ok=True)
    report = {"schema_version": 1, "status": "preparing", "provider_requests": 0,
              "max_provider_requests": MAX_PROVIDER_REQUESTS, "usage_totals": {}}
    diagnostics_out.write_text(json.dumps(report) + "\n", encoding="utf-8")
    sampling: dict = {}
    failure = ""
    try:
        origin = normalize_origin(site_url)
        base_url = builder.validate_deepseek_base_url(base_url)
        units, sampling = collect_samples(origin, fetcher)
        with tempfile.TemporaryDirectory(prefix="portal-locale-preflight-") as temporary:
            builder.translate_missing_units(
                units, builder.empty_cache(model),
                cache_path=Path(temporary) / "cache-v1.json.gz",
                model=model, base_url=base_url, workers=1, timeout=120, attempts=1,
                max_batch_chars=8 * MAX_FIELD_CHARS, max_batch_items=8,
                preflight_only=True, preflight_batches_per_locale=2,
                diagnostics_out=diagnostics_out, max_provider_requests=MAX_PROVIDER_REQUESTS,
            )
    except Exception as error:
        failure = str(error)
        raise PreflightError(failure) from None
    finally:
        report = json.loads(diagnostics_out.read_text(encoding="utf-8"))
        report["sampling"] = sampling
        if failure:
            report["status"] = "failed"
            report["diagnostic_error"] = failure
        diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", default=os.getenv("LIVE_ORIGIN", ""))
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", builder.DEFAULT_DEEPSEEK_MODEL))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    args = parser.parse_args()
    try:
        report = run_preflight(site_url=args.site_url, diagnostics_out=args.diagnostics_out,
                               model=args.model, base_url=args.deepseek_base_url)
    except PreflightError as error:
        print(f"portal locale preflight failed: {error}", file=sys.stderr)
        return 1
    print(json.dumps({key: report.get(key) for key in ("status", "provider_requests", "usage_totals", "usage_unknown_responses")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
