#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch the latest public PDF reports from major economic / policy institutions.

This is a standalone *source* module, sitting next to ``download_dropbox_latest_pdfs.py``.
Instead of reading PDFs from Dropbox, it pulls the newest publications from:

- IMF        国际货币基金组织   (Coveo search API)
- World Bank 世界银行           (Documents & Reports JSON API)
- BIS        国际清算银行       (research / BCBS / CGFS RSS feeds)
- OECD       经合组织           (publications listing, Firefox fingerprint)
- ADB        亚洲开发银行       (publications RSS feed, includes ADBI)
- WEF        世界经济论坛       (publications listing, Chrome fingerprint)
- UNCTAD     联合国贸发会议     (publications listing)
- WTO        世界贸易组织       (news RSS feed; report launches carry PDFs)
- Bruegel    布鲁盖尔研究所     (publications RSS feed)

RAND and Brookings remain configured for explicit --institutions runs but are
excluded from the default set (topics too politically sensitive for WeChat).

Design goals
------------
- The downloaded PDFs are *transient*: they are only an input for the existing
  ``run_pdf_to_xhs_in_batches.py`` -> ``build_portal_translated_reports.py`` ->
  ``push_portal_translated_to_wechat_drafts.py`` pipeline. They are NOT meant to be
  committed or kept long term (write them under a git-ignored output dir).
- The *original PDF link* is archived permanently to a JSONL file in the repo so we
  always have a record of where each report came from, even after the PDF is deleted.
- A seen-state file is used to deduplicate, so the same report is never processed
  twice across daily runs. Recency (``--since-days``) only decides what is *fresh*;
  the seen-state is what guarantees *no reprocessing*.

Each institution is isolated: a failure fetching one source never aborts the others.

Output written to ``--output-dir``:
    <token>_<title>.pdf            transient PDFs for the downstream pipeline
    institution_run_manifest.json  per-run summary (downloaded + skipped + errors)

Persistent state (committed by the workflow, NOT the PDFs):
    institution_feeds/institution_pdf_archive.jsonl   long-term link archive
    institution_feeds/seen_state.json                 dedup state

Run:
    python scripts/fetch_institution_latest_pdfs.py \
        --output-dir _institution_latest_pdfs \
        --date 260625 \
        --since-days 1
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from collections.abc import Callable
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.entities import name2codepoint
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urljoin, urlsplit

import requests

try:  # Optional: impersonate a real Chrome TLS/HTTP2 fingerprint to pass WAFs (IMF).
    from curl_cffi import requests as cffi_requests  # type: ignore
    _HAS_CFFI = True
except Exception:  # noqa: BLE001
    cffi_requests = None  # type: ignore
    _HAS_CFFI = False

# curl_cffi impersonation target; "chrome" maps to a recent Chrome fingerprint.
CFFI_IMPERSONATE = "chrome"

# A browser-like User-Agent. Several of these sites (notably RAND and Brookings)
# reject the default python-requests UA with HTTP 403.
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
HTTP_RETRYABLE_STATUSES = {408, 425, 429, 500, 502, 503, 504}
HTTP_MAX_ATTEMPTS = 3
HTTP_RETRY_BASE_SECONDS = 2.0
HTTP_RETRY_MAX_SECONDS = 15.0
DDG_ROUTE_TIMEOUT_SECONDS = 25
DDG_SEARCH_ENDPOINTS = (
    ("html", "https://html.duckduckgo.com/html/"),
)
IMF_PROXY_TEST_URL = "https://www.imf.org/en/Publications"
DETERMINISTIC_SKIP_STATUSES = {"too_large"}

# Anchor hrefs that look like a downloadable document.
PDF_HREF_RE = re.compile(r'(?:href|data-href|content)=["\']([^"\']+?\.(?:pdf|ashx)[^"\']*)["\']', re.I)


# ------------------------------------------------------------------
# Per-institution configuration.
#
# kind:
#   "rss"           -> fetch the feed(s), then resolve each item's PDF.
#   "worldbank_api" -> query the WDS JSON API (gives a direct pdfurl).
# pdf:
#   "scrape"        -> open the item's landing page and look for a PDF link.
#   "swap_htm_pdf"  -> derive the PDF by swapping the .htm(l) suffix for .pdf.
#   "direct"        -> the item already carries a direct PDF url.
#
# To enable/disable a source or add a feed, edit this dict. ``include`` is an
# optional regex the item link must match (used to keep only real reports).
# ------------------------------------------------------------------
INSTITUTIONS: dict[str, dict[str, Any]] = {
    "imf": {
        "name_en": "IMF",
        "name_cn": "国际货币基金组织",
        "token": "IMF",
        # IMF's site is a JS app behind Akamai (RSS is gone; the WAF blocks plain
        # requests by TLS fingerprint). Its publications search is powered by Coveo,
        # which is a separate, non-WAF host we can query directly. Resolve PDFs from
        # Coveo's cached HTML preview first; use the IMF landing page only as fallback.
        "impersonate": True,
        "kind": "coveo_api",
        "pdf": "scrape",
        "coveo_url": "https://imfproduction561s308u.org.coveo.com/rest/search/v2?organizationId=imfproduction561s308u",
        "coveo_organization_id": "imfproduction561s308u",
        # Public, browser-exposed Coveo search key. Static/long-lived; if IMF ever
        # rotates it, override via the IMF_COVEO_TOKEN env var (no code change needed).
        "coveo_token": "xx742a6c66-f427-4f5a-ae1e-770dc7264e8a",
        # Advanced query: English publications only. "PUBS" covers working papers,
        # country reports, selected issues, FSAPs, Article IV, etc. To narrow (e.g.
        # only working papers) tighten this @imfcontenttype filter.
        "coveo_aq": '(@imflanguage=="ENG") AND (@syslanguage=="ENGLISH") AND (@imfcontenttype=="PUBS")',
        # GitHub-hosted runner IPs can fetch Coveo but IMF's Akamai landing and
        # media endpoints often return 403; route both resolution and download
        # requests through a proxy validated against the IMF origin.
        "use_proxy": True,
        "proxy_test_url": IMF_PROXY_TEST_URL,
        # A zero-output run is only trustworthy when this source is healthy.
        "required_for_clean_zero": True,
    },
    "bis": {
        "name_en": "BIS",
        "name_cn": "国际清算银行",
        "token": "BIS",
        "kind": "rss",
        "pdf": "swap_htm_pdf",
        "feeds": [
            # BIS' public RSS page labels this broader feed "Research papers"; it
            # includes the Annual Economic Report, BIS Bulletins, FSI papers and
            # working papers. The old wppubls feed only covered working papers.
            "https://www.bis.org/doclist/bis_fsi_publs.rss",
            "https://www.bis.org/doclist/wppubls.rss",
            # Basel Committee (bis.org/bcbs/publ/dNNN.htm) and Committee on the
            # Global Financial System (bis.org/publ/cgfsNN.htm) publications.
            "https://www.bis.org/doclist/bcbspubls.rss",
            "https://www.bis.org/doclist/cgfs_publs.rss",
        ],
        # Only keep substantive publication pages, skip speeches / central-bank
        # reviews. Publication paths vary by committee: /publ/, /bcbs/publ/,
        # /fsi/publ/ all carry the swap-htm-for-pdf convention.
        "include": r"bis\.org/(?:\w+/)?publ/",
        "required_for_clean_zero": True,
    },
    "worldbank": {
        "name_en": "World Bank",
        "name_cn": "世界银行",
        "token": "WorldBank",
        "kind": "worldbank_api",
        "pdf": "direct",
        "api_base": "https://search.worldbank.org/api/v3/wds",
        # WDS v3 returns current publication dates, so the normal freshness window
        # applies. The retired v2 endpoint had gone stale at March 2025.
        "recency_filter": True,
        "params": {
            "format": "json",
            "sort": "docdt",
            "order": "desc",
            "fl": "docdt,display_title,docna,pdfurl,url,docty,guid",
            # Substantive research reports, not loan / project agreements.
            "docty_exact": "Policy Research Working Paper",
        },
        "required_for_clean_zero": True,
    },
    "oecd": {
        "name_en": "OECD",
        "name_cn": "经合组织",
        "token": "OECD",
        # oecd.org is behind Akamai and 403s both plain requests and the Chrome
        # curl_cffi fingerprint, but accepts the Firefox one. The publications
        # landing page is server-rendered with the newest reports; each report
        # page links its PDF under /content/dam/.
        "kind": "html_listing",
        "pdf": "scrape",
        "impersonate": True,
        "impersonate_profile": "firefox135",
        # GitHub runner IPs get 403s from Akamai intermittently; route through
        # the VPS proxy when PROXY_SUBSCRIPTION_URL is configured.
        "use_proxy": True,
        "recency_filter": False,
        "listing_urls": [
            "https://www.oecd.org/en/publications.html",
        ],
        # Real publications look like /en/publications/<slug>_<id>-en.html; the
        # trailing _<id> distinguishes them from nav pages.
        "item_link_pattern": r"oecd\.org/en/publications/[a-z0-9][a-z0-9-]*_[a-z0-9-]+\.html",
    },
    "adb": {
        "name_en": "ADB",
        "name_cn": "亚洲开发银行",
        "token": "ADB",
        # The feed also carries ADBI (ADB Institute) papers. adb.org's WAF blocks
        # Chrome-family TLS fingerprints (and GitHub runner IPs on plain requests)
        # but accepts Firefox/Safari fingerprints.
        "kind": "rss",
        "pdf": "scrape",
        "impersonate": True,
        "impersonate_profile": "firefox135",
        "feeds": [
            "https://www.adb.org/rss/publications",
        ],
        "include": r"adb\.org/(?:adbi/)?publications/",
    },
    "wef": {
        "name_en": "World Economic Forum",
        "name_cn": "世界经济论坛",
        "token": "WEF",
        # weforum.org 403s plain requests but accepts the Chrome fingerprint. The
        # publications listing is server-rendered; report pages link PDFs on
        # reports.weforum.org/docs/.
        "kind": "html_listing",
        "pdf": "scrape",
        "impersonate": True,
        "recency_filter": False,
        "listing_urls": [
            "https://www.weforum.org/publications/",
        ],
        "item_link_pattern": r"weforum\.org/publications/(?!series\b)[a-z0-9-]+/?$",
    },
    "unctad": {
        "name_en": "UNCTAD",
        "name_cn": "联合国贸发会议",
        "token": "UNCTAD",
        # Server-rendered Drupal listing; publication pages link PDFs under
        # unctad.org/system/files/.
        "kind": "html_listing",
        "pdf": "scrape",
        "impersonate": True,
        "use_proxy": True,
        "recency_filter": False,
        "listing_urls": [
            "https://unctad.org/publications",
        ],
        "item_link_pattern": r"unctad\.org/publication/[a-z0-9-]+$",
        # Every UNCTAD page links the generic "UNCTAD at a glance" brochure;
        # never mistake it for the publication's own PDF.
        "pdf_exclude": r"at-a-glance",
    },
    "wto": {
        "name_en": "WTO",
        "name_cn": "世界贸易组织",
        "token": "WTO",
        # The WTO has no publications feed (library/rss/latest_pubs_e.xml is a
        # dead HTML page), so use the news feed: report launches carry a PDF on
        # the news page, plain announcements are skipped as no_pdf.
        "kind": "rss",
        "pdf": "scrape",
        "feeds": [
            "https://www.wto.org/library/rss/latest_news_e.xml",
        ],
        "include": r"wto\.org/english/news_e/",
    },
    "bruegel": {
        "name_en": "Bruegel",
        "name_cn": "布鲁盖尔研究所",
        "token": "Bruegel",
        # Cloudflare blocks GitHub-hosted runner IPs outright (every fingerprint
        # 403s), so this source needs the VPS proxy on CI; fingerprint alone is
        # enough from residential IPs.
        "kind": "rss",
        "pdf": "scrape",
        "impersonate": True,
        "impersonate_profile": "firefox135",
        "use_proxy": True,
        "feeds": [
            "https://www.bruegel.org/feed/publications-feed.xml",
        ],
        # Keep report-style pieces (which carry PDFs); datasets / events / web
        # commentary are skipped.
        "include": r"bruegel\.org/(?:working-paper|policy-brief|blueprint|essay|report)",
    },
    "rand": {
        "name_en": "RAND",
        "name_cn": "兰德公司",
        "token": "RAND",
        "kind": "rss",
        "pdf": "scrape",
        "feeds": [
            "https://www.rand.org/pubs/new.xml",
        ],
        # RAND research_reports / perspectives carry a free PDF; external_publications
        # usually point to paywalled journals, so skip those.
        "include": r"rand\.org/pubs/(?:research_reports|perspectives|commentary|tools)/",
    },
    "brookings": {
        "name_en": "Brookings",
        "name_cn": "布鲁金斯学会",
        "token": "Brookings",
        # Brookings has disabled its RSS feed (/feed/ returns the HTML homepage), so
        # scrape the research listing page for article links, then resolve each PDF.
        # Most articles are web-only commentary; those without a PDF are skipped, so
        # this naturally keeps only the report-style posts.
        "kind": "html_listing",
        "pdf": "scrape",
        # Listing pages carry no reliable per-item dates; rely on seen-dedup instead.
        "recency_filter": False,
        "listing_urls": [
            "https://www.brookings.edu/research/",
        ],
        "item_link_pattern": r"https://www\.brookings\.edu/articles/[a-z0-9-]+/",
    },
    # MBB strategy consultancies. Their sites are JS apps behind Akamai/Cloudflare
    # (Bain is fully Cloudflare-challenged), so we don't scrape them directly. Instead
    # we discover their published PDFs via DuckDuckGo (site:<domain> filetype:pdf) and
    # download from the asset/CDN hosts, which are not bot-walled. df=m biases toward
    # recent; seen-dedup guarantees no report is processed twice.
    "mckinsey": {
        "name_en": "McKinsey",
        "name_cn": "麦肯锡",
        "token": "McKinsey",
        "kind": "ddg_search",
        "pdf": "direct",
        "impersonate": True,
        # DDG results have no date and therefore bypass the normal cutoff; the
        # official fallback does provide dates, so this prevents an outage from
        # backfilling months-old store reports as today's discoveries.
        "recency_filter": True,
        "query": "site:mckinsey.com filetype:pdf",
        # Independent fallback when DuckDuckGo is unavailable or challenges the
        # runner. This official page exposes direct report downloads and dates.
        "fallback_pdf_listing_urls": [
            "https://www.mckinsey.com/featured-insights/insights-store",
        ],
        # DDG is relevance-ranked; keep only reports whose URL/title mentions the
        # current or previous year so old evergreen reports are excluded.
        "recent_years": 2,
        "required_for_clean_zero": True,
    },
    "bain": {
        "name_en": "Bain",
        "name_cn": "贝恩",
        "token": "Bain",
        "kind": "ddg_search",
        "pdf": "direct",
        "impersonate": True,
        "recency_filter": False,
        "query": "site:bain.com filetype:pdf",
    },
    "bcg": {
        "name_en": "BCG",
        "name_cn": "波士顿咨询",
        "token": "BCG",
        # BCG's publication list is JS-rendered and DuckDuckGo discovery is flaky, but
        # its sitemap exposes every publication URL and the pages link to downloadable
        # PDFs (web-assets / media-publications hosts). Sort by <lastmod> for recency.
        "kind": "sitemap",
        "pdf": "scrape",
        "impersonate": True,
        "recency_filter": False,
        "sitemap_urls": ["https://www.bcg.com/sitemap.xml"],
        "child_filter": r"content|latest",
        "include": r"bcg\.com/publications/",
        "sitemap_scan_limit": 40,
        # Only publications modified within this window, so we skip old reports.
        "sitemap_max_age_days": 120,
        "required_for_clean_zero": True,
    },
}
# Sources the scheduled WeChat run pulls by default. Ordered by priority: when
# --max-total binds, earlier sources keep their quota. RAND and Brookings are
# deliberately NOT here (topics too politically sensitive for the WeChat
# account); they remain in INSTITUTIONS for explicit --institutions runs.
DEFAULT_PUBLIC_INSTITUTION_KEYS = [
    "imf", "worldbank", "bis", "oecd", "adb", "wef", "unctad", "wto", "bruegel",
]


def log(message: str) -> None:
    print(message, flush=True)


def warn(message: str) -> None:
    print(f"[WARN] {message}", flush=True)


def github_warning(message: str) -> None:
    """Add a visible Actions annotation without aborting the other sources."""
    warn(message)
    if os.getenv("GITHUB_ACTIONS", "").lower() == "true":
        escaped = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::warning::{escaped}", flush=True)


def write_source_health_summary(source_checks: list[dict[str, Any]]) -> None:
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    status_label = {"ok": "OK", "degraded": "DEGRADED", "empty": "EMPTY", "error": "ERROR"}
    lines = [
        "## Institution source health",
        "",
        "| Source | Status | Items checked | New PDFs | Detail |",
        "|---|---:|---:|---:|---|",
    ]
    for check in source_checks:
        detail = str(check.get("error", "")).replace("|", "\\|").replace("\n", " ")[:240]
        lines.append(
            f"| {check['institution']} | {status_label.get(check['status'], check['status'])} "
            f"| {check.get('item_count', 0)} | {check.get('new_pdf_count', 0)} | {detail} |"
        )
    with open(summary_path, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


# ------------------------------------------------------------------
# Small helpers
# ------------------------------------------------------------------

def slug(value: str, limit: int = 60) -> str:
    value = re.sub(r"\.(pdf|ashx|html?)$", "", value.strip(), flags=re.IGNORECASE)
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:limit] or "report"


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


def local_tag(tag: str) -> str:
    """Strip the XML namespace so RSS / RDF / Atom can share one parser."""
    return tag.rsplit("}", 1)[-1].lower() if "}" in tag else tag.lower()


def parse_date(value: str) -> datetime | None:
    value = (value or "").strip()
    if not value:
        return None
    # RFC 822 (RSS pubDate), e.g. "Tue, 24 Jun 2026 09:00:00 GMT"
    try:
        dt = parsedate_to_datetime(value)
        if dt is not None:
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        pass
    # ISO 8601 (Atom / dc:date / World Bank docdt), tolerate a trailing Z.
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    for fmt in ("%Y-%m-%d", "%d %b %Y", "%d %B %Y", "%Y/%m/%d", "%b %d, %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def is_pdf_bytes(data: bytes) -> bool:
    # Some servers emit a small BOM / whitespace before the signature.
    return b"%PDF-" in data[:1024]


# ------------------------------------------------------------------
# Optional VPS proxy for sources whose WAF blocks GitHub runner IPs.
#
# Same subscription format as bbg-show: PROXY_SUBSCRIPTION_URL points at a
# (possibly base64-wrapped) node list; only curl-compatible nodes are used
# (https:// entries whose payload base64-decodes to user:pass@host:port,
# plain http://, and socks5:// which curl needs as socks5h://). Sources opt
# in with "use_proxy": True; everything else keeps fetching directly.
# ------------------------------------------------------------------

PROXY_TEST_URL = "https://www.gstatic.com/generate_204"


def _b64_text(value: str) -> str | None:
    import base64
    stripped = value.strip()
    try:
        return base64.b64decode(stripped + "=" * (-len(stripped) % 4)).decode("utf-8")
    except Exception:  # noqa: BLE001
        return None


def _normalize_proxy_node(node: str) -> str | None:
    node = node.split("#", 1)[0].strip()  # drop display label
    if node.startswith("https://"):
        decoded = _b64_text(node[len("https://"):])
        if decoded and "@" in decoded:
            return "https://" + decoded.split("/", 1)[0]
        return node
    if node.startswith("socks5://"):
        return "socks5h://" + node[len("socks5://"):]
    if node.startswith(("http://", "socks5h://")):
        return node
    return None  # vmess/anytls/... not curl-compatible


def mask_proxy(proxy: str) -> str:
    return re.sub(r"//[^@/]+@", "//***@", proxy)


def _fetch_subscription(url: str, timeout: int) -> str | None:
    """The subscription host is picky about clients; try several fetch methods."""
    try:
        resp = requests.get(url, timeout=timeout, headers={"User-Agent": DEFAULT_USER_AGENT})
        resp.raise_for_status()
        return resp.text.strip()
    except Exception as exc:  # noqa: BLE001
        warn(f"subscription via requests failed: {exc}")
    try:  # plain curl CLI is what bbg-show uses successfully
        out = subprocess.run(
            ["curl", "--location", "--fail", "--silent", "--show-error", url],
            capture_output=True, text=True, timeout=90,
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
        warn(f"subscription via curl failed: rc={out.returncode} {out.stderr.strip()[:120]}")
    except Exception as exc:  # noqa: BLE001
        warn(f"subscription via curl failed: {exc}")
    if _HAS_CFFI:
        try:
            resp = cffi_requests.get(url, timeout=timeout, impersonate=CFFI_IMPERSONATE)
            if resp.status_code < 400 and resp.text.strip():
                return resp.text.strip()
            warn(f"subscription via curl_cffi failed: http_{resp.status_code}")
        except Exception as exc:  # noqa: BLE001
            warn(f"subscription via curl_cffi failed: {exc}")
    return None


def resolve_working_proxy(
    subscription_url: str,
    timeout: int,
    test_url: str = PROXY_TEST_URL,
) -> str | None:
    """Return the first proxy node that reaches the source-specific test URL.

    Validating the actual WAF-protected origin rotates past nodes that have
    general connectivity but are still blocked by that origin.
    """
    body = _fetch_subscription(subscription_url, timeout)
    if not body:
        return None
    if "://" not in body.splitlines()[0]:
        body = _b64_text(body) or body
    candidates = [p for p in (_normalize_proxy_node(l) for l in body.splitlines() if l.strip()) if p]
    log(f"proxy subscription: {len(candidates)} curl-compatible node(s)")
    # Bound the health check so a subscription full of dead nodes cannot stall
    # the whole run: at most 10 nodes, 10s each.
    for proxy in candidates[:10]:
        if not _HAS_CFFI:
            break
        try:
            resp = cffi_requests.get(
                test_url, timeout=min(max(timeout, 1), 10), impersonate=CFFI_IMPERSONATE,
                proxies={"http": proxy, "https": proxy},
            )
            if 200 <= resp.status_code < 400:
                return proxy
        except Exception:  # noqa: BLE001
            continue
    warn("no working proxy node found in subscription")
    return None


# ------------------------------------------------------------------
# Feed parsing (RSS 2.0, RSS 1.0/RDF, Atom)
# ------------------------------------------------------------------

def _sanitize_xml_entities(content: bytes) -> bytes:
    """Neutralize undefined named HTML entities so strict XML parsing succeeds.

    Real-world feeds (notably the Brookings WordPress feed) break strict XML in a
    few ways: undefined named entities like ``&nbsp;``, bare ``&`` that do not start
    a valid entity, and stray control characters. Fix all three: strip illegal
    control chars, escape bare ampersands, then convert known named entities to
    numeric refs (dropping unknown ones) while leaving the five XML built-ins alone.
    """
    text = content.decode("utf-8", errors="replace")
    # Drop control characters that are illegal in XML 1.0 (keep tab/newline/CR).
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    # Escape bare ampersands that do not begin a valid entity reference.
    text = re.sub(r"&(?!#[0-9]+;|#x[0-9a-fA-F]+;|[A-Za-z][A-Za-z0-9]*;)", "&amp;", text)

    def repl(match: "re.Match[str]") -> str:
        name = match.group(1)
        if name in ("amp", "lt", "gt", "quot", "apos"):
            return match.group(0)
        codepoint = name2codepoint.get(name)
        return f"&#{codepoint};" if codepoint is not None else ""

    return re.sub(r"&([A-Za-z][A-Za-z0-9]*);", repl, text).encode("utf-8")


def _first_tag_text(body: str, tag: str) -> str:
    """Pull the inner text of the first <tag>...</tag> (any namespace) from a blob."""
    match = re.search(rf"<(?:\w+:)?{tag}\b[^>]*>(.*?)</(?:\w+:)?{tag}>", body, re.I | re.S)
    if not match:
        return ""
    value = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", match.group(1), flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)  # strip any nested HTML tags
    return html.unescape(value).strip()


def _regex_extract_items(content: bytes) -> list[dict[str, str]]:
    """Last-resort parser for feeds that are not well-formed XML at all.

    Some feeds embed raw, unbalanced HTML (mismatched tags) that no amount of
    entity fixing will make XML-valid. We do not need the full document tree, only
    each item's title/link/guid/date, so extract those by pattern from each
    <item>/<entry> block. This is lenient by design.
    """
    text = content.decode("utf-8", errors="replace")
    results: list[dict[str, str]] = []
    for tag, body in re.findall(r"<(item|entry)\b[^>]*>(.*?)</\1>", text, re.I | re.S):
        link = _first_tag_text(body, "link")
        if not link:
            href = re.search(r"<link\b[^>]*\bhref=[\"']([^\"']+)[\"']", body, re.I)
            link = html.unescape(href.group(1)) if href else ""
        date = (
            _first_tag_text(body, "pubDate")
            or _first_tag_text(body, "date")
            or _first_tag_text(body, "published")
            or _first_tag_text(body, "updated")
        )
        results.append({
            "title": _first_tag_text(body, "title"),
            "link": link,
            "guid": _first_tag_text(body, "guid") or _first_tag_text(body, "id") or link,
            "date": date,
        })
    return results


def parse_feed(content: bytes) -> list[dict[str, str]]:
    """Return a list of {title, link, guid, date} from any RSS/RDF/Atom feed."""
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        try:
            root = ET.fromstring(_sanitize_xml_entities(content))
        except ET.ParseError:
            return _regex_extract_items(content)
    entries = [el for el in root.iter() if local_tag(el.tag) in {"item", "entry"}]
    results: list[dict[str, str]] = []
    for entry in entries:
        title = ""
        link = ""
        guid = ""
        date = ""
        atom_links: list[tuple[str, str, str]] = []
        for child in entry:
            tag = local_tag(child.tag)
            text = (child.text or "").strip()
            if tag == "title" and not title:
                title = html.unescape(text)
            elif tag == "link":
                href = child.get("href")
                if href:  # Atom: link is an element with attributes
                    rel = (child.get("rel") or "alternate").lower()
                    typ = (child.get("type") or "").lower()
                    atom_links.append((rel, typ, href))
                elif text and not link:  # RSS / RDF: link is plain text
                    link = text
            elif tag in {"guid", "id"} and not guid:
                guid = text
            elif tag in {"pubdate", "date", "published", "updated"} and not date:
                date = text
        if not link and atom_links:
            link = next(
                (h for rel, typ, h in atom_links if rel == "alternate" and ("html" in typ or not typ)),
                atom_links[0][2],
            )
        results.append({
            "title": title,
            "link": link,
            "guid": guid or link,
            "date": date,
        })
    return results


# ------------------------------------------------------------------
# Item collection per institution
# ------------------------------------------------------------------

def _http_retry_delay(attempt: int, response: Any | None = None) -> float:
    delay = HTTP_RETRY_BASE_SECONDS * (2 ** max(0, attempt - 1))
    if response is not None:
        retry_after = str(getattr(response, "headers", {}).get("Retry-After", "")).strip()
        try:
            delay = max(delay, float(retry_after))
        except (TypeError, ValueError):
            pass
    return min(HTTP_RETRY_MAX_SECONDS, delay)


def _is_transient_get_error(exc: Exception) -> bool:
    if isinstance(
        exc,
        (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.ChunkedEncodingError,
        ),
    ):
        return True
    return type(exc).__module__.startswith("curl_cffi")


def _request_with_retry(
    url: str,
    request_call: Callable[[], Any],
    max_attempts: int,
) -> Any:
    attempts = max(1, int(max_attempts))
    for attempt in range(1, attempts + 1):
        try:
            response = request_call()
        except Exception as exc:  # noqa: BLE001 - curl_cffi uses its own exception classes
            if not _is_transient_get_error(exc) or attempt >= attempts:
                raise
            delay = _http_retry_delay(attempt)
            warn(
                f"transient HTTP error for {url} on attempt {attempt}/{attempts} "
                f"({type(exc).__name__}); retrying in {delay:g}s"
            )
            time.sleep(delay)
            continue

        status_code = int(getattr(response, "status_code", 200))
        if status_code not in HTTP_RETRYABLE_STATUSES or attempt >= attempts:
            return response
        delay = _http_retry_delay(attempt, response)
        warn(
            f"retryable HTTP {status_code} for {url} on attempt {attempt}/{attempts}; "
            f"retrying in {delay:g}s"
        )
        close = getattr(response, "close", None)
        if callable(close):
            close()
        time.sleep(delay)
    raise RuntimeError(f"HTTP retry loop ended unexpectedly: {url}")


def http_get(
    session: requests.Session,
    url: str,
    timeout: int,
    impersonate: bool = False,
    stream: bool = False,
    profile: str | None = None,
    proxy: str | None = None,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    max_attempts: int = HTTP_MAX_ATTEMPTS,
):
    """GET via curl_cffi (browser fingerprint) when impersonate is requested and the
    library is installed; otherwise via the shared requests session. The returned
    object exposes .status_code/.headers/.content/.text/.raise_for_status like requests.
    ``profile`` overrides the default Chrome fingerprint (e.g. OECD only accepts
    Firefox); ``proxy`` routes the impersonated request through a VPS node.
    """
    def request_call() -> Any:
        if impersonate and _HAS_CFFI:
            return cffi_requests.get(
                url,
                timeout=timeout,
                impersonate=profile or CFFI_IMPERSONATE,
                allow_redirects=True,
                stream=stream,
                proxies={"http": proxy, "https": proxy} if proxy else None,
                params=params,
                headers=headers,
            )
        return session.get(
            url,
            timeout=timeout,
            allow_redirects=True,
            stream=stream,
            params=params,
            headers=headers,
        )

    return _request_with_retry(url, request_call, max_attempts)


def http_post(
    session: requests.Session,
    url: str,
    timeout: int,
    *,
    headers: dict[str, str] | None = None,
    json_payload: dict[str, Any] | None = None,
    max_attempts: int = HTTP_MAX_ATTEMPTS,
) -> Any:
    return _request_with_retry(
        url,
        lambda: session.post(url, headers=headers, json=json_payload, timeout=timeout),
        max_attempts,
    )


def collect_rss_items(cfg: dict[str, Any], session: requests.Session, timeout: int) -> list[dict[str, Any]]:
    include = re.compile(cfg["include"], re.I) if cfg.get("include") else None
    items: list[dict[str, Any]] = []
    for feed_url in cfg["feeds"]:
        try:
            resp = http_get(session, feed_url, timeout, cfg.get("impersonate", False), profile=cfg.get("impersonate_profile"), proxy=cfg.get("_proxy"))
            resp.raise_for_status()
            parsed = parse_feed(resp.content)
        except Exception as exc:  # noqa: BLE001 - isolate feed failures
            warn(f"feed failed: {feed_url}: {exc}")
            continue
        log(f"  feed {feed_url} -> {len(parsed)} items")
        if not parsed:
            try:
                content_type = resp.headers.get("content-type", "")
            except Exception:  # noqa: BLE001
                content_type = ""
            snippet = resp.content[:200].decode("utf-8", "replace").replace("\n", " ").strip()
            log(f"    [debug] 0 items; content-type={content_type!r}; starts: {snippet!r}")
        for entry in parsed:
            link = entry["link"]
            if not link:
                continue
            if include and not include.search(link):
                continue
            items.append({
                "title": entry["title"],
                "source_url": link,
                "guid": entry["guid"],
                "date": entry["date"],
                "pdf_candidates": _derive_pdf_candidates(cfg, link),
                "scrape_url": link if cfg.get("pdf") == "scrape" else "",
            })
    return items


def _derive_pdf_candidates(cfg: dict[str, Any], link: str) -> list[str]:
    if cfg.get("pdf") == "swap_htm_pdf":
        return [re.sub(r"\.html?(\?|#|$)", r".pdf\1", link, flags=re.IGNORECASE)]
    if cfg.get("pdf") == "direct":
        return [link]
    return []


def collect_worldbank_items(cfg: dict[str, Any], session: requests.Session, timeout: int, rows: int) -> list[dict[str, Any]]:
    params = dict(cfg["params"])
    params["rows"] = rows
    resp = http_get(session, cfg["api_base"], timeout, params=params)
    resp.raise_for_status()
    data = resp.json()
    documents = data.get("documents", {})
    items: list[dict[str, Any]] = []
    for key, doc in documents.items():
        if not isinstance(doc, dict):
            continue  # e.g. the "facets" entry
        pdf_url = doc.get("pdfurl")
        if not pdf_url:
            continue
        items.append({
            "title": doc.get("display_title") or doc.get("docna") or key,
            "source_url": doc.get("url") or pdf_url,
            "guid": doc.get("guid") or key,
            "date": doc.get("docdt") or "",
            "pdf_candidates": [pdf_url],
            "scrape_url": "",
        })
    log(f"  worldbank api -> {len(items)} docs with pdf")
    return items


# ------------------------------------------------------------------
# PDF resolution + download
# ------------------------------------------------------------------

def _title_from_url_slug(url: str) -> str:
    """Fallback title: the last path segment of the landing URL, dashes as spaces."""
    segments = [s for s in urlsplit(url).path.split("/") if s]
    if not segments:
        return ""
    return unquote(segments[-1]).replace("-", " ").replace("_", " ").strip()


def _extract_html_title(html_text: str) -> str:
    """Best-effort article title from an HTML page (og:title, then <title>)."""
    match = re.search(
        r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']',
        html_text, re.I,
    )
    if not match:
        match = re.search(r"<title>(.*?)</title>", html_text, re.I | re.S)
    if not match:
        return ""
    title = html.unescape(re.sub(r"\s+", " ", match.group(1))).strip()
    return re.sub(r"\s*[|–-]\s*Brookings.*$", "", title).strip()


# Marketing / recruiting / boilerplate PDFs that are not research reports.
NON_REPORT_RE = re.compile(
    r"brochure|fact[\s_-]?sheet|recruit|career|\bmba\b|code[\s_-]?of[\s_-]?conduct|"
    r"modern[\s_-]?slavery|gender[\s_-]?pay|privacy|cookie|terms[\s_-]?of[\s_-]?use|"
    r"who[\s_-]?we[\s_-]?are|media[\s_-]?kit|press[\s_-]?kit",
    re.I,
)


def _parse_ddg_pdfs(text: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(target: str, title: str) -> None:
        if not re.search(r"\.pdf(\?|$)", target, re.I) or target in seen:
            return
        seen.add(target)
        if not title:
            title = unquote(Path(urlsplit(target).path).name) or target
        items.append({
            "title": title,
            "source_url": target,
            "guid": target,
            "date": "",
            "pdf_candidates": [target],
            "scrape_url": "",
        })

    # Primary: any anchor whose target (via the uddg= redirect or a direct href)
    # resolves to a PDF. Not tied to DuckDuckGo's CSS class names.
    for match in re.finditer(r'<a\b[^>]*\bhref="([^"]+)"[^>]*>(.*?)</a>', text, re.S | re.I):
        redirect = re.search(r"[?&]uddg=([^&]+)", match.group(1))
        target = unquote(redirect.group(1)) if redirect else html.unescape(match.group(1))
        target = target.split("&rut=")[0]
        add(target, html.unescape(re.sub(r"<[^>]+>", "", match.group(2))).strip())

    # Fallback: bare PDF URLs in the page (handles markup changes), title from filename.
    if not items:
        for raw in re.findall(r'https?(?:%3a%2f%2f|%3A%2F%2F|://)[^\s"\'<>()]+?\.pdf', text, re.I):
            add(unquote(raw), "")
    return items


def _parse_official_download_listing(text: str, base_url: str) -> list[dict[str, Any]]:
    """Parse McKinsey's ``#/download/<encoded PDF>`` report cards."""
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    pattern = re.compile(
        r'<a\b[^>]*\bhref=["\']([^"\']*#/download/[^"\']+)["\'][^>]*>',
        re.I,
    )
    for match in pattern.finditer(text):
        encoded_target = html.unescape(match.group(1)).split("#/download/", 1)[1]
        target = unquote(encoded_target).strip()
        if target.startswith("//"):
            target = "https:" + target
        else:
            target = urljoin(base_url, target)
        target = requests.utils.requote_uri(target)
        if not re.search(r"\.pdf(?:\?|$)", target, re.I) or target in seen:
            continue
        seen.add(target)

        # Title and publication time precede the download link in each report card.
        card_prefix = text[max(0, match.start() - 5000):match.start()]
        headings = re.findall(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", card_prefix, re.I | re.S)
        title = ""
        if headings:
            title = html.unescape(re.sub(r"<[^>]+>", " ", headings[-1]))
            title = re.sub(r"\s+", " ", title).strip()
        if not title:
            title = unquote(Path(urlsplit(target).path).stem).replace("-", " ").strip()
        dates = re.findall(r'<time\b[^>]*\bdatetime=["\']([^"\']+)', card_prefix, re.I)
        published = dates[-1] if dates else ""
        items.append({
            "title": title,
            "source_url": target,
            "guid": target,
            "date": published,
            "pdf_candidates": [target],
            "scrape_url": "",
        })
    return items


def _is_ddg_challenge_response(response: Any) -> bool:
    status_code = int(getattr(response, "status_code", 200))
    body = str(getattr(response, "text", "")).lower()
    return (
        status_code == 202
        or "challenge-form" in body
        or "bots use duckduckgo too" in body
    )


def collect_ddg_items(cfg: dict[str, Any], session: requests.Session, timeout: int, df: str) -> list[dict[str, Any]]:
    """Discover PDFs via DuckDuckGo HTML search (site:<domain> filetype:pdf).

    Bypasses the consultancies' bot walls: we only hit DuckDuckGo and the PDF CDN
    hosts. DDG can time out or return a challenge page, so try independent browser
    and plain transports, then the official report store, before declaring the source
    degraded. Obvious non-reports are filtered out, and seen-dedup keeps each report
    one-time.
    """
    params = {"q": str(cfg["query"])}
    if df:
        params["df"] = df
    headers = {"Referer": "https://duckduckgo.com/", "Accept-Language": "en-US,en;q=0.9"}
    items: list[dict[str, Any]] = []
    route_timeout = max(1, min(int(timeout), DDG_ROUTE_TIMEOUT_SECONDS))
    routes: list[tuple[str, str, bool]] = []
    for endpoint_name, endpoint_url in DDG_SEARCH_ENDPOINTS:
        if _HAS_CFFI:
            routes.append((f"{endpoint_name}/browser", endpoint_url, True))
        routes.append((f"{endpoint_name}/requests", endpoint_url, False))

    def request_route(
        endpoint_url: str,
        use_cffi: bool,
        request_params: dict[str, str] | None,
        request_headers: dict[str, str],
    ) -> Any:
        if use_cffi:
            return cffi_requests.get(
                endpoint_url,
                params=request_params,
                impersonate=CFFI_IMPERSONATE,
                timeout=route_timeout,
                headers=request_headers,
                allow_redirects=True,
            )
        return session.get(
            endpoint_url,
            params=request_params,
            timeout=route_timeout,
            headers=request_headers,
            allow_redirects=True,
        )

    failed_routes: list[str] = []
    empty_routes = 0
    for route_name, endpoint_url, use_cffi in routes:
        try:
            resp = request_route(endpoint_url, use_cffi, params, headers)
            resp.raise_for_status()
            if _is_ddg_challenge_response(resp):
                raise RuntimeError("DuckDuckGo challenge response")
            items = _parse_ddg_pdfs(resp.text)
        except Exception as exc:  # noqa: BLE001 - independent route fallback
            failed_routes.append(f"{route_name}:{type(exc).__name__}")
            warn(f"  ddg route {route_name} failed ({type(exc).__name__}); trying fallback")
            continue
        if items:
            log(f"  ddg discovery route: {route_name}")
            break
        empty_routes += 1
        warn(f"  ddg route {route_name} returned no PDF results; trying fallback")

    if not items:
        listing_headers = {"Accept-Language": "en-US,en;q=0.9"}
        for listing_url in cfg.get("fallback_pdf_listing_urls", []):
            listing_routes = [True, False] if _HAS_CFFI else [False]
            for use_cffi in listing_routes:
                route_name = f"official/{'browser' if use_cffi else 'requests'}"
                try:
                    resp = request_route(listing_url, use_cffi, None, listing_headers)
                    resp.raise_for_status()
                    items = _parse_official_download_listing(resp.text, listing_url)
                except Exception as exc:  # noqa: BLE001 - independent source fallback
                    failed_routes.append(f"{route_name}:{type(exc).__name__}")
                    warn(
                        f"  report discovery route {route_name} failed "
                        f"({type(exc).__name__}); trying fallback"
                    )
                    continue
                if items:
                    log(f"  report discovery route: {route_name}")
                    break
                empty_routes += 1
                warn(f"  report discovery route {route_name} returned no PDF results")
            if items:
                break

    if not items and failed_routes:
        failures = ", ".join(failed_routes)
        raise RuntimeError(f"Report discovery unavailable across all routes ({failures})")

    kept = [it for it in items if not NON_REPORT_RE.search(it["source_url"]) and not NON_REPORT_RE.search(it["title"])]
    # DuckDuckGo ranks by relevance, not date, so without this it would surface old
    # evergreen reports. Keep only items whose URL or title mentions a recent year.
    recent_years = int(cfg.get("recent_years", 0))
    if recent_years:
        years = {str(datetime.now(timezone.utc).year - offset) for offset in range(recent_years)}
        before = len(kept)
        kept = [
            it for it in kept
            if any(
                y in it["source_url"]
                or y in it["title"]
                or str(it.get("date", "")).startswith(y)
                for y in years
            )
        ]
        log(f"  recent-year filter ({'/'.join(sorted(years, reverse=True))}): {before} -> {len(kept)}")
    log(f"  report discovery '{cfg['query']}' -> {len(items)} pdf results, kept {len(kept)}")
    return kept


def collect_sitemap_items(cfg: dict[str, Any], session: requests.Session, timeout: int) -> list[dict[str, Any]]:
    """Collect publication page URLs from a sitemap (following a sitemap index),
    newest first by <lastmod>; each page's PDF is resolved later by the scrape step.

    Used for BCG, whose listing is JS-rendered but whose sitemap exposes every
    publication URL and whose pages link to downloadable PDFs on asset hosts.
    """
    include = re.compile(cfg["include"], re.I) if cfg.get("include") else None
    child_filter = re.compile(cfg["child_filter"], re.I) if cfg.get("child_filter") else None
    impersonate = cfg.get("impersonate", False)
    profile = cfg.get("impersonate_profile")
    proxy = cfg.get("_proxy")
    to_fetch = list(cfg["sitemap_urls"])
    fetched = 0
    entries: list[tuple[str, str]] = []  # (lastmod, loc)
    seen_sm: set[str] = set()
    while to_fetch and fetched < cfg.get("max_sitemaps", 8):
        sm = to_fetch.pop(0)
        if sm in seen_sm:
            continue
        seen_sm.add(sm)
        fetched += 1
        try:
            resp = http_get(session, sm, timeout, impersonate, profile=profile, proxy=proxy)
            resp.raise_for_status()
            text = resp.text
        except Exception as exc:  # noqa: BLE001 - isolate sitemap failures
            warn(f"  sitemap failed {sm}: {exc}")
            continue
        if "<sitemapindex" in text[:1000].lower():
            for loc in re.findall(r"<loc>([^<]+)</loc>", text):
                if not child_filter or child_filter.search(loc):
                    to_fetch.append(html.unescape(loc.strip()))
            continue
        for block in re.findall(r"<url>(.*?)</url>", text, re.S):
            loc_m = re.search(r"<loc>([^<]+)</loc>", block)
            if not loc_m:
                continue
            loc = html.unescape(loc_m.group(1).strip())
            if include and not include.search(loc):
                continue
            lm = re.search(r"<lastmod>([^<]+)</lastmod>", block)
            entries.append((lm.group(1).strip() if lm else "", loc))
    entries.sort(key=lambda e: e[0], reverse=True)  # newest <lastmod> first
    # Keep only recently-modified publications so we don't pull in old reports.
    max_age = int(cfg.get("sitemap_max_age_days", 0))
    if max_age:
        cutoff = datetime.now(timezone.utc) - timedelta(days=max_age)
        before = len(entries)
        fresh: list[tuple[str, str]] = []
        for lastmod, loc in entries:
            dt = parse_date(lastmod)
            if dt is not None and dt >= cutoff:
                fresh.append((lastmod, loc))
        entries = fresh
        log(f"  sitemap age filter (<= {max_age}d): {before} -> {len(entries)} recent urls")
    limit = cfg.get("sitemap_scan_limit", 40)
    items = [
        {"title": "", "source_url": loc, "guid": loc, "date": lastmod, "pdf_candidates": [], "scrape_url": loc}
        for lastmod, loc in entries[:limit]
    ]
    log(f"  sitemap -> scanning newest {len(items)} urls")
    return items


def collect_html_listing_items(cfg: dict[str, Any], session: requests.Session, timeout: int) -> list[dict[str, Any]]:
    """Scrape a listing page for article links; each is resolved to a PDF later."""
    pattern = re.compile(cfg["item_link_pattern"], re.I)
    items: list[dict[str, Any]] = []
    seen_links: set[str] = set()
    for url in cfg["listing_urls"]:
        try:
            resp = http_get(session, url, timeout, cfg.get("impersonate", False), profile=cfg.get("impersonate_profile"), proxy=cfg.get("_proxy"))
            resp.raise_for_status()
        except Exception as exc:  # noqa: BLE001 - isolate listing failures
            warn(f"listing failed: {url}: {exc}")
            continue
        links: list[str] = []
        for match in re.finditer(r'href=["\']([^"\']+)["\']', resp.text):
            full = urljoin(url, html.unescape(match.group(1))).split("#")[0]
            if pattern.search(full) and full not in seen_links:
                seen_links.add(full)
                links.append(full)
        log(f"  listing {url} -> {len(links)} article links")
        for link in links:
            items.append({
                "title": "",
                "source_url": link,
                "guid": link,
                "date": "",
                "pdf_candidates": [],
                "scrape_url": link,
            })
    return items


def _normalize_imf_host(url: str) -> str:
    """Rewrite IMF origin/staging hosts to the public www host."""
    return re.sub(r"https?://(?:origin-www|prd-sitecore[\w.-]*|stg-www)\.imf\.org",
                  "https://www.imf.org", url, flags=re.I)


IMF_SERIES_PDF_RULES: tuple[tuple[re.Pattern[str], str, str], ...] = (
    (re.compile(r"high level summary technical assistance", re.I), "hls", "hlsea"),
    (re.compile(r"selected issues paper", re.I), "selected-issues-papers", "sipea"),
    (re.compile(r"technical notes? and manuals?", re.I), "tnm", "tnmea"),
    (re.compile(r"staff discussion notes?", re.I), "sdn", "sdnea"),
    (re.compile(r"(?:imf )?how[- ]to notes?", re.I), "howtonotes", "htnea"),
    (re.compile(r"imf notes?", re.I), "imf-notes", "insea"),
    (re.compile(r"policy papers?", re.I), "pp", "ppea"),
    (re.compile(r"working papers?", re.I), "wp", "wpiea"),
    (re.compile(r"technical assistance reports?", re.I), "tar", "tarea"),
)


def derive_imf_pdf_candidates(raw: dict[str, Any]) -> list[str]:
    """Build official IMF media URLs from the series number in Coveo metadata.

    IMF's Akamai landing pages can return 403 even though the public PDF media
    host remains reachable. Coveo exposes stable series identifiers such as
    ``Working Paper No. 2026/153``; most IMF publication families use a
    deterministic media filename derived from that identifier.
    """
    volume = str(raw.get("seriesvolumeno") or "")
    series_value = raw.get("imfseries") or ""
    if isinstance(series_value, (list, tuple)):
        series = " ".join(str(value) for value in series_value)
    else:
        series = str(series_value)
    identity = f"{series} {volume}".strip()
    number_match = re.search(r"\b(20\d{2})\s*/\s*(\d{1,4})\b", volume)
    if not identity or not number_match:
        return []

    year = number_match.group(1)
    number = f"{int(number_match.group(2)):03d}"
    for pattern, path_token, filename_token in IMF_SERIES_PDF_RULES:
        if not pattern.search(identity):
            continue
        stem = (
            "https://www.imf.org/-/media/files/publications/"
            f"{path_token}/{year}/english/{filename_token}{year}{number}"
        )
        # Newly released working papers often use -source-pdf while other IMF
        # families generally use the plain filename. Try both, in likely order.
        if path_token == "wp":
            return [f"{stem}-source-pdf.pdf", f"{stem}.pdf"]
        return [f"{stem}.pdf", f"{stem}-source-pdf.pdf"]
    return []


def collect_coveo_items(cfg: dict[str, Any], session: requests.Session, timeout: int, rows: int) -> list[dict[str, Any]]:
    """Query the IMF Coveo search API for the latest publications (newest first)."""
    token = os.getenv("IMF_COVEO_TOKEN") or cfg["coveo_token"]
    body = {
        "aq": cfg["coveo_aq"],
        "q": "",
        "searchHub": "Search",
        "enableQuerySyntax": False,
        "sortCriteria": "@imfdate descending",
        "numberOfResults": rows,
        "fieldsToInclude": [
            "title", "clickableuri", "imfdate", "imfcontenttype", "permanentid",
            "urihash", "imfseries", "seriesvolumeno",
        ],
    }
    resp = http_post(
        session,
        cfg["coveo_url"],
        timeout,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Origin": "https://www.imf.org",
            "Referer": "https://www.imf.org/",
        },
        json_payload=body,
    )
    resp.raise_for_status()
    data = resp.json()
    items: list[dict[str, Any]] = []
    for result in data.get("results", []):
        raw = result.get("raw", {})
        landing = raw.get("clickableuri") or result.get("clickUri") or result.get("uri") or ""
        if not landing:
            continue
        landing = _normalize_imf_host(landing)
        # Search results can include Special Features roll-up pages, which are
        # collections rather than individual publications with one report PDF.
        if "/publications/sprolls/" in urlsplit(landing).path.lower():
            continue
        epoch_ms = raw.get("imfdate")
        date_iso = ""
        if isinstance(epoch_ms, (int, float)):
            try:
                date_iso = datetime.fromtimestamp(epoch_ms / 1000, tz=timezone.utc).isoformat()
            except (ValueError, OSError):
                date_iso = ""
        is_file = bool(re.search(r"\.(pdf|ashx)(\?|$)", landing, re.I))
        pdf_candidates = [landing] if is_file else derive_imf_pdf_candidates(raw)
        items.append({
            "title": result.get("title") or raw.get("title") or landing,
            "source_url": landing,
            "guid": raw.get("permanentid") or raw.get("urihash") or landing,
            "date": date_iso,
            "pdf_candidates": pdf_candidates,
            "scrape_url": "" if is_file else landing,
            "coveo_unique_id": result.get("uniqueId") or result.get("UniqueId") or "",
        })
    log(f"  coveo -> {len(items)} publications (total {data.get('totalCount')})")
    return items


def scrape_pdf_candidates(html_text: str, base_url: str) -> list[str]:
    host = urlsplit(base_url).netloc
    candidates: list[str] = []
    seen: set[str] = set()
    for match in PDF_HREF_RE.finditer(html_text):
        href = html.unescape(match.group(1).strip())
        full = urljoin(base_url, href)
        if full in seen:
            continue
        seen.add(full)
        candidates.append(full)

    # Also catch bare PDF/.ashx URLs embedded in JSON/JS (e.g. IMF Next.js props),
    # not just href/data-href/content attributes.
    for match in re.finditer(r'https?://[^\s"\'<>()\\]+?\.(?:pdf|ashx)(?:\?[^\s"\'<>()\\]*)?', html_text, re.I):
        full = html.unescape(match.group(0))
        if full not in seen:
            seen.add(full)
            candidates.append(full)

    def score(url: str) -> int:
        low = url.lower()
        value = 0
        if low.split("?")[0].endswith(".pdf"):
            value += 5
        if "pdf" in low:
            value += 2
        if host and host in low:
            value += 2
        if any(bad in low for bad in ("/thumb", "icon", "logo", "cover-", "-cover", "summary-")):
            value -= 3
        return value

    return sorted(candidates, key=score, reverse=True)


def scrape_imf_preview_candidates(html_text: str, base_url: str) -> list[str]:
    """Extract IMF PDF links, including Country Report stock-number URLs."""

    candidates = scrape_pdf_candidates(html_text, base_url)
    if "/publications/cr/" not in urlsplit(base_url).path.lower():
        return candidates

    # Some freshly indexed Country Report previews contain metadata before their
    # Download PDF button is rendered. The stock number is the exact media
    # filename, so it remains a reliable resolver for these cached pages.
    plain_text = html.unescape(re.sub(r"<[^>]+>", " ", html_text))
    for match in re.finditer(
        r"\bStock\s+No\.?\s*:?\s*([A-Z0-9][A-Z0-9._-]{5,31})\b",
        plain_text,
        re.I,
    ):
        stock_no = match.group(1).rstrip(".").lower()
        year_match = re.search(r"20\d{2}", stock_no)
        if not year_match:
            continue
        stem = (
            "https://www.imf.org/-/media/files/publications/cr/"
            f"{year_match.group(0)}/english/{stock_no}"
        )
        for candidate in (f"{stem}.pdf", f"{stem}-source-pdf.pdf"):
            if candidate not in candidates:
                candidates.append(candidate)
    return candidates


def collect_coveo_preview_candidates(
    cfg: dict[str, Any],
    session: requests.Session,
    unique_id: str,
    base_url: str,
    timeout: int,
) -> list[str]:
    """Resolve official PDF links from Coveo's cached HTML preview."""

    unique_id = str(unique_id or "").strip()
    if not unique_id:
        return []

    parsed = urlsplit(cfg["coveo_url"])
    preview_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path.rstrip('/')}/html"
    token = os.getenv("IMF_COVEO_TOKEN") or cfg["coveo_token"]
    response = http_get(
        session,
        preview_url,
        timeout,
        params={
            "organizationId": cfg["coveo_organization_id"],
            "uniqueId": unique_id,
        },
        headers={
            "Authorization": f"Bearer {token}",
            "Origin": "https://www.imf.org",
            "Referer": "https://www.imf.org/",
        },
    )
    response.raise_for_status()
    return scrape_imf_preview_candidates(response.text, base_url)


def download_pdf(session: requests.Session, urls: Iterable[str], dest: Path, timeout: int, max_bytes: int, impersonate: bool = False, profile: str | None = None, proxy: str | None = None) -> tuple[str | None, str]:
    """Try each candidate URL; save the first that is a real PDF. Returns (used_url, status)."""
    last_status = "no_candidate"
    for url in urls:
        if not url:
            continue
        try:
            if impersonate and _HAS_CFFI:
                # curl_cffi: read fully (bounded below), no chunked streaming API needed.
                resp = http_get(
                    session,
                    url,
                    timeout,
                    impersonate=True,
                    profile=profile,
                    proxy=proxy,
                )
                if resp.status_code >= 400:
                    last_status = f"http_{resp.status_code}"
                    continue
                data = resp.content
                if len(data) > max_bytes:
                    last_status = "too_large"
                    continue
            else:
                with http_get(session, url, timeout, stream=True) as resp:
                    if resp.status_code >= 400:
                        last_status = f"http_{resp.status_code}"
                        continue
                    buffer = bytearray()
                    too_large = False
                    for chunk in resp.iter_content(8192):
                        if not chunk:
                            continue
                        buffer.extend(chunk)
                        if len(buffer) > max_bytes:
                            too_large = True
                            break
                if too_large:
                    last_status = "too_large"
                    continue
                data = bytes(buffer)
            # Require the %PDF signature even when the server claims a PDF content-type,
            # so we never save an HTML error / login page that lies about its type.
            if not is_pdf_bytes(data):
                last_status = "not_pdf"
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            return url, "ok"
        except Exception as exc:  # noqa: BLE001 - try the next candidate
            last_status = f"error:{exc}"
            continue
    return None, last_status


# ------------------------------------------------------------------
# Seen-state and archive
# ------------------------------------------------------------------

def load_seen_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "items": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        data.setdefault("items", {})
        return data
    except Exception as exc:  # noqa: BLE001
        warn(f"could not read seen state {path}: {exc}; starting fresh")
        return {"version": 1, "items": {}}


def prune_seen_state(state: dict[str, Any], retention_days: int) -> None:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=retention_days)).date().isoformat()
    items = state.get("items", {})
    for key in [k for k, v in items.items() if str(v.get("first_seen", "")) < cutoff]:
        del items[key]


def as_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def append_archive(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch latest institution PDF reports for the WeChat pipeline.")
    parser.add_argument("--output-dir", required=True, help="Where to write transient PDFs (should be git-ignored).")
    parser.add_argument("--date", default=datetime.now(timezone.utc).strftime("%y%m%d"), help="Run date tag, YYMMDD.")
    parser.add_argument("--institutions", default="all", help="Comma list of keys to enable, or 'all'.")
    parser.add_argument("--since-days", type=int, default=1, help="Only keep items published within this many days.")
    parser.add_argument("--max-per-institution", type=int, default=0, help="Cap new PDFs per institution (0 = no cap).")
    parser.add_argument("--archive-path", default="institution_feeds/institution_pdf_archive.jsonl")
    parser.add_argument("--seen-state-path", default="institution_feeds/seen_state.json")
    parser.add_argument("--seen-retention-days", type=int, default=120)
    parser.add_argument("--max-pdf-mb", type=float, default=60.0)
    parser.add_argument("--worldbank-rows", type=int, default=30)
    parser.add_argument("--imf-rows", type=int, default=60, help="Coveo results to scan for IMF (newest first).")
    parser.add_argument("--ddg-df", default="", help="DuckDuckGo date filter for search sources: d/w/m/y or '' for none. The html endpoint returns nothing with a date filter, so default is none; recent reports still surface by relevance and seen-dedup avoids reprocessing.")
    parser.add_argument("--force-reprocess", default="false", help="Ignore seen-state dedup and redownload matching fresh PDFs.")
    parser.add_argument("--max-total", type=int, default=0, help="Cap new PDFs across ALL institutions this run (0 = no cap). Keeps the daily WeChat output bounded; earlier institutions in the list get priority.")
    parser.add_argument("--request-timeout", type=int, default=60)
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = Path(args.archive_path)
    seen_path = Path(args.seen_state_path)
    max_bytes = int(args.max_pdf_mb * 1024 * 1024)

    if args.institutions.strip().lower() in {"all", "*", ""}:
        enabled = DEFAULT_PUBLIC_INSTITUTION_KEYS
    elif args.institutions.strip().lower() in {"everything", "all-including-consulting"}:
        enabled = list(INSTITUTIONS.keys())
    else:
        enabled = [k.strip().lower() for k in args.institutions.split(",") if k.strip()]
        unknown = [k for k in enabled if k not in INSTITUTIONS]
        if unknown:
            raise SystemExit(f"Unknown institution keys: {unknown}. Known: {list(INSTITUTIONS)}")

    session = requests.Session()
    session.headers.update({
        "User-Agent": args.user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })

    state = load_seen_state(seen_path)
    seen_items = state["items"]
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.since_days)
    today = datetime.now(timezone.utc).date().isoformat()
    force_reprocess = as_bool(args.force_reprocess)
    if force_reprocess:
        log("Force reprocess enabled: ignoring seen-state dedup for matching fresh PDFs.")

    downloaded: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    source_checks: list[dict[str, Any]] = []
    used_pdf_urls: set[str] = set()

    proxy_url: str | None = None
    if any(INSTITUTIONS[k].get("use_proxy") for k in enabled):
        subscription = os.getenv("PROXY_SUBSCRIPTION_URL", "").strip()
        if subscription:
            # Prefer a source-specific WAF probe when one is configured. IMF is
            # first in the public-source set, so normal institution runs verify
            # the chosen node against IMF instead of merely checking the web.
            proxy_test_url = next(
                (
                    str(INSTITUTIONS[k]["proxy_test_url"])
                    for k in enabled
                    if INSTITUTIONS[k].get("use_proxy")
                    and INSTITUTIONS[k].get("proxy_test_url")
                ),
                PROXY_TEST_URL,
            )
            proxy_url = resolve_working_proxy(
                subscription,
                args.request_timeout,
                test_url=proxy_test_url,
            )
            if proxy_url:
                log(f"Using VPS proxy for WAF-blocked sources: {mask_proxy(proxy_url)}")
            else:
                warn("proxy unavailable; use_proxy sources will fetch directly and may 403")
        else:
            log("PROXY_SUBSCRIPTION_URL not set; use_proxy sources fetch directly.")
    for key in INSTITUTIONS:
        INSTITUTIONS[key]["_proxy"] = proxy_url if INSTITUTIONS[key].get("use_proxy") else None

    for key in enabled:
        if args.max_total and len(downloaded) >= args.max_total:
            log(f"Reached --max-total {args.max_total}; skipping remaining institutions.")
            break
        cfg = INSTITUTIONS[key]
        log(f"== {cfg['name_en']} ({cfg['name_cn']}) ==")
        try:
            if cfg["kind"] == "worldbank_api":
                items = collect_worldbank_items(cfg, session, args.request_timeout, args.worldbank_rows)
            elif cfg["kind"] == "coveo_api":
                items = collect_coveo_items(cfg, session, args.request_timeout, args.imf_rows)
            elif cfg["kind"] == "ddg_search":
                items = collect_ddg_items(cfg, session, args.request_timeout, args.ddg_df)
            elif cfg["kind"] == "sitemap":
                items = collect_sitemap_items(cfg, session, args.request_timeout)
            elif cfg["kind"] == "html_listing":
                items = collect_html_listing_items(cfg, session, args.request_timeout)
            else:
                items = collect_rss_items(cfg, session, args.request_timeout)
        except Exception as exc:  # noqa: BLE001 - never let one source kill the run
            message = f"{cfg['name_en']} source failed entirely: {exc}"
            github_warning(message)
            source_checks.append({
                "institution": key,
                "institution_en": cfg["name_en"],
                "status": "error",
                "item_count": 0,
                "new_pdf_count": 0,
                "eligible_item_count": 0,
                "resolution_failure_count": 0,
                "required_for_clean_zero": bool(cfg.get("required_for_clean_zero")),
                "error": str(exc),
            })
            continue

        source_status = "ok" if items else "empty"
        if source_status == "empty":
            github_warning(
                f"{cfg['name_en']} source returned no items; treating this as "
                "source health degradation, not confirmed zero updates"
            )

        new_count = 0
        eligible_count = 0
        resolution_failure_count = 0
        resolution_failure_samples: list[str] = []
        for item in items:
            if args.max_per_institution and new_count >= args.max_per_institution:
                break
            if args.max_total and len(downloaded) >= args.max_total:
                break

            dedup_key = f"{key}:{item['guid'] or item['source_url']}"
            if dedup_key in seen_items and not force_reprocess:
                continue

            published = parse_date(item["date"])
            if cfg.get("recency_filter", True) and published is not None and published < cutoff:
                # Old item we have simply never recorded; mark it so we do not keep
                # re-checking it every day, but do not download it.
                seen_items[dedup_key] = {"first_seen": today, "status": "too_old"}
                continue

            eligible_count += 1
            candidates = list(item["pdf_candidates"])
            landing_attempted = False
            preview_attempted = False
            if not candidates and item.get("coveo_unique_id"):
                preview_attempted = True
                try:
                    candidates = collect_coveo_preview_candidates(
                        cfg,
                        session,
                        item["coveo_unique_id"],
                        item["source_url"],
                        args.request_timeout,
                    )
                except Exception as exc:  # noqa: BLE001 - use origin fallback
                    warn(f"  Coveo preview fetch failed, will try landing page: {item['source_url']}: {exc}")
            if not candidates and item.get("scrape_url"):
                landing_attempted = True
                try:
                    page = http_get(session, item["scrape_url"], args.request_timeout, cfg.get("impersonate", False), profile=cfg.get("impersonate_profile"), proxy=cfg.get("_proxy"))
                    page.raise_for_status()
                    candidates = scrape_pdf_candidates(page.text, item["scrape_url"])
                    if not item["title"]:
                        item["title"] = _extract_html_title(page.text)
                except Exception as exc:  # noqa: BLE001 - network error: retry next run
                    warn(f"  landing fetch failed, will retry next run: {item['source_url']}: {exc}")
                    resolution_failure_count += 1
                    if len(resolution_failure_samples) < 3:
                        resolution_failure_samples.append(f"landing: {type(exc).__name__}: {exc}")
                    continue
            if cfg.get("pdf_exclude"):
                candidates = [c for c in candidates if not re.search(cfg["pdf_exclude"], c, re.I)]
            # Some sites (e.g. WEF) return the bare site name as og:title.
            if item["title"].strip().lower() in {"", cfg["name_en"].lower()}:
                item["title"] = _title_from_url_slug(item["source_url"]) or item["title"]

            if not candidates:
                # Page reachable but has no downloadable PDF (e.g. a Brookings op-ed).
                seen_items[dedup_key] = {"first_seen": today, "status": "no_pdf"}
                skipped.append({"institution": key, "title": item["title"], "reason": "no_pdf", "source_url": item["source_url"]})
                continue

            title = item["title"] or item["guid"] or item["source_url"]
            filename = f"{cfg['token']}_{slug(title)}_{short_hash(dedup_key)}.pdf"
            dest = output_dir / filename
            used_url, status = download_pdf(session, candidates[:3], dest, args.request_timeout, max_bytes, impersonate=cfg.get("impersonate", False), profile=cfg.get("impersonate_profile"), proxy=cfg.get("_proxy"))
            # A deterministic/direct candidate may have changed on the source site.
            # Try Coveo's cached HTML before touching the WAF-protected landing page.
            if (status != "ok" or used_url is None) and item.get("coveo_unique_id") and not preview_attempted:
                preview_attempted = True
                try:
                    preview_candidates = collect_coveo_preview_candidates(
                        cfg,
                        session,
                        item["coveo_unique_id"],
                        item["source_url"],
                        args.request_timeout,
                    )
                    if cfg.get("pdf_exclude"):
                        preview_candidates = [
                            candidate for candidate in preview_candidates
                            if not re.search(cfg["pdf_exclude"], candidate, re.I)
                        ]
                    preview_candidates = [candidate for candidate in preview_candidates if candidate not in candidates]
                    if preview_candidates:
                        used_url, status = download_pdf(
                            session,
                            preview_candidates[:3],
                            dest,
                            args.request_timeout,
                            max_bytes,
                            impersonate=cfg.get("impersonate", False),
                            profile=cfg.get("impersonate_profile"),
                            proxy=cfg.get("_proxy"),
                        )
                except Exception as exc:  # noqa: BLE001 - use origin fallback
                    if len(resolution_failure_samples) < 3:
                        resolution_failure_samples.append(f"Coveo preview fallback: {type(exc).__name__}: {exc}")
            # If Coveo cannot resolve the PDF, still try the landing page.
            if (status != "ok" or used_url is None) and item.get("scrape_url") and not landing_attempted:
                landing_attempted = True
                try:
                    page = http_get(session, item["scrape_url"], args.request_timeout, cfg.get("impersonate", False), profile=cfg.get("impersonate_profile"), proxy=cfg.get("_proxy"))
                    page.raise_for_status()
                    scraped_candidates = scrape_pdf_candidates(page.text, item["scrape_url"])
                    if cfg.get("pdf_exclude"):
                        scraped_candidates = [
                            candidate for candidate in scraped_candidates
                            if not re.search(cfg["pdf_exclude"], candidate, re.I)
                        ]
                    scraped_candidates = [candidate for candidate in scraped_candidates if candidate not in candidates]
                    if scraped_candidates:
                        used_url, status = download_pdf(
                            session,
                            scraped_candidates[:3],
                            dest,
                            args.request_timeout,
                            max_bytes,
                            impersonate=cfg.get("impersonate", False),
                            profile=cfg.get("impersonate_profile"),
                            proxy=cfg.get("_proxy"),
                        )
                except Exception as exc:  # noqa: BLE001 - retry the item next run
                    if len(resolution_failure_samples) < 3:
                        resolution_failure_samples.append(f"landing fallback: {type(exc).__name__}: {exc}")
            if status != "ok" or used_url is None:
                if status in DETERMINISTIC_SKIP_STATUSES:
                    seen_items[dedup_key] = {
                        "first_seen": today,
                        "status": status,
                        "max_pdf_mb": args.max_pdf_mb,
                    }
                    warn(f"  skipped ({status}): {title[:80]}")
                    skipped.append({"institution": key, "title": title, "reason": status, "source_url": item["source_url"]})
                    continue
                # Could not download; do NOT mark seen so a transient failure is retried.
                warn(f"  download failed ({status}): {title[:80]}")
                skipped.append({"institution": key, "title": title, "reason": status, "source_url": item["source_url"]})
                resolution_failure_count += 1
                if len(resolution_failure_samples) < 3:
                    resolution_failure_samples.append(f"download: {status}: {title[:80]}")
                continue

            if used_url in used_pdf_urls:
                # Two feed/listing items resolved to the same PDF (e.g. a shared
                # brochure link); keep only the first.
                dest.unlink(missing_ok=True)
                seen_items[dedup_key] = {"first_seen": today, "status": "duplicate_pdf"}
                skipped.append({"institution": key, "title": title, "reason": "duplicate_pdf", "source_url": item["source_url"]})
                continue
            used_pdf_urls.add(used_url)

            seen_items[dedup_key] = {"first_seen": today, "status": "downloaded"}
            record = {
                "archived_at": datetime.now(timezone.utc).isoformat(),
                "date": args.date,
                "institution": key,
                "institution_en": cfg["name_en"],
                "institution_cn": cfg["name_cn"],
                "title": title,
                "published": item["date"],
                "source_page_url": item["source_url"],
                "pdf_url": used_url,
                "local_filename": filename,
                "bytes": dest.stat().st_size,
                "force_reprocess": force_reprocess,
            }
            append_archive(archive_path, record)
            downloaded.append(record)
            new_count += 1
            log(f"  saved {filename} ({record['bytes'] // 1024} KB) <- {used_url}")

        health_detail = ""
        if source_status == "ok" and resolution_failure_count:
            source_status = "error" if resolution_failure_count >= eligible_count else "degraded"
            health_detail = (
                f"{resolution_failure_count}/{eligible_count} unseen recent item(s) "
                "could not be resolved or downloaded"
            )
            if resolution_failure_samples:
                health_detail += "; " + " | ".join(resolution_failure_samples)
            github_warning(f"{cfg['name_en']} source health {source_status}: {health_detail}")

        source_checks.append({
            "institution": key,
            "institution_en": cfg["name_en"],
            "status": source_status,
            "item_count": len(items),
            "new_pdf_count": new_count,
            "eligible_item_count": eligible_count,
            "resolution_failure_count": resolution_failure_count,
            "required_for_clean_zero": bool(cfg.get("required_for_clean_zero")),
            "error": health_detail,
        })
        log(f"  {cfg['name_en']}: {new_count} new PDF(s)")

    prune_seen_state(state, args.seen_retention_days)
    seen_path.parent.mkdir(parents=True, exist_ok=True)
    seen_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest = {
        "date": args.date,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "since_days": args.since_days,
        "institutions": enabled,
        "downloaded_count": len(downloaded),
        "skipped_count": len(skipped),
        "source_checks": source_checks,
        "force_reprocess": force_reprocess,
        "downloaded": downloaded,
        "skipped": skipped,
    }
    (output_dir / "institution_run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    write_github_output("pdf_count", str(len(downloaded)))
    write_github_output("source_error_count", str(sum(check["status"] == "error" for check in source_checks)))
    write_github_output("source_degraded_count", str(sum(check["status"] == "degraded" for check in source_checks)))
    write_github_output("source_empty_count", str(sum(check["status"] == "empty" for check in source_checks)))
    write_github_output("output_dir", str(output_dir))
    write_github_output("date_folder", args.date)
    write_source_health_summary(source_checks)
    log(f"Done. Downloaded {len(downloaded)} new PDF(s), skipped {len(skipped)}.")
    blocking_checks = [
        check for check in source_checks
        if check.get("required_for_clean_zero") and check["status"] != "ok"
    ]
    if not downloaded and blocking_checks:
        names = ", ".join(f"{check['institution']}={check['status']}" for check in blocking_checks)
        github_warning(
            "Zero PDFs cannot be treated as a confirmed no-update run because "
            f"required source health is degraded: {names}"
        )
        return 2
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        warn("interrupted")
        raise SystemExit(130)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
