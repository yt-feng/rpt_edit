#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch the latest public PDF reports from major economic / policy institutions.

This is a standalone *source* module, sitting next to ``download_dropbox_latest_pdfs.py``.
Instead of reading PDFs from Dropbox, it pulls the newest publications from:

- IMF        国际货币基金组织   (publications RSS feeds)
- BIS        国际清算银行       (working papers RSS feed)
- World Bank 世界银行           (Documents & Reports JSON API)
- RAND       兰德公司           (latest publications Atom feed)
- Brookings  布鲁金斯学会       (WordPress research feed)

Design goals
------------
- The downloaded PDFs are *transient*: they are only an input for the existing
  ``run_pdf_to_xhs_in_batches.py`` -> ``build_kc_translated_reports.py`` ->
  ``push_kc_translated_to_wechat_drafts.py`` pipeline. They are NOT meant to be
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
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.entities import name2codepoint
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote, unquote, urljoin, urlsplit

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
        # which is a separate, non-WAF host we can query directly. Then we fetch each
        # landing page's PDF on imf.org via curl_cffi Chrome impersonation.
        "impersonate": True,
        "kind": "coveo_api",
        "pdf": "scrape",
        "coveo_url": "https://imfproduction561s308u.org.coveo.com/rest/search/v2?organizationId=imfproduction561s308u",
        # Public, browser-exposed Coveo search key. Static/long-lived; if IMF ever
        # rotates it, override via the IMF_COVEO_TOKEN env var (no code change needed).
        "coveo_token": "xx742a6c66-f427-4f5a-ae1e-770dc7264e8a",
        # Advanced query: English publications only. "PUBS" covers working papers,
        # country reports, selected issues, FSAPs, Article IV, etc. To narrow (e.g.
        # only working papers) tighten this @imfcontenttype filter.
        "coveo_aq": '(@imflanguage=="ENG") AND (@syslanguage=="ENGLISH") AND (@imfcontenttype=="PUBS")',
    },
    "bis": {
        "name_en": "BIS",
        "name_cn": "国际清算银行",
        "token": "BIS",
        "kind": "rss",
        "pdf": "swap_htm_pdf",
        "feeds": [
            "https://www.bis.org/doclist/wppubls.rss",
        ],
        # Only keep /publ/ documents (working papers, bulletins), skip speeches etc.
        "include": r"bis\.org/publ/",
    },
    "worldbank": {
        "name_en": "World Bank",
        "name_cn": "世界银行",
        "token": "WorldBank",
        "kind": "worldbank_api",
        "pdf": "direct",
        "api_base": "https://search.worldbank.org/api/v2/wds",
        # WDS docdt lags real publication by many months, so a recency window would
        # always be empty. Take the newest available by docdt and rely on seen-dedup.
        "recency_filter": False,
        "params": {
            "format": "json",
            "srt": "docdt",
            "order": "desc",
            "fl": "docdt,display_title,docna,pdfurl,url,docty,guid",
            # Substantive research reports, not loan / project agreements.
            "docty_exact": "Policy Research Working Paper",
        },
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
        "recency_filter": False,
        "query": "site:mckinsey.com filetype:pdf",
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
        "kind": "ddg_search",
        "pdf": "direct",
        "impersonate": True,
        "recency_filter": False,
        "query": "site:bcg.com filetype:pdf",
    },
}


def log(message: str) -> None:
    print(message, flush=True)


def warn(message: str) -> None:
    print(f"[WARN] {message}", flush=True)


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

def http_get(session: requests.Session, url: str, timeout: int, impersonate: bool = False, stream: bool = False):
    """GET via curl_cffi (Chrome fingerprint) when impersonate is requested and the
    library is installed; otherwise via the shared requests session. The returned
    object exposes .status_code/.headers/.content/.text/.raise_for_status like requests.
    """
    if impersonate and _HAS_CFFI:
        return cffi_requests.get(url, timeout=timeout, impersonate=CFFI_IMPERSONATE, allow_redirects=True, stream=stream)
    return session.get(url, timeout=timeout, allow_redirects=True, stream=stream)


def collect_rss_items(cfg: dict[str, Any], session: requests.Session, timeout: int) -> list[dict[str, Any]]:
    include = re.compile(cfg["include"], re.I) if cfg.get("include") else None
    items: list[dict[str, Any]] = []
    for feed_url in cfg["feeds"]:
        try:
            resp = http_get(session, feed_url, timeout, cfg.get("impersonate", False))
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
    resp = session.get(cfg["api_base"], params=params, timeout=timeout)
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


def collect_ddg_items(cfg: dict[str, Any], session: requests.Session, timeout: int, df: str) -> list[dict[str, Any]]:
    """Discover PDFs via DuckDuckGo HTML search (site:<domain> filetype:pdf).

    Bypasses the consultancies' bot walls: we only hit DuckDuckGo and the PDF CDN
    hosts. DDG can return an empty page when queried rapidly, so retry with backoff;
    obvious non-reports (brochures, fact sheets, recruiting) are filtered out, and
    seen-dedup keeps each report one-time.
    """
    url = "https://html.duckduckgo.com/html/?q=" + quote(cfg["query"])
    if df:
        url += "&df=" + df
    headers = {"Referer": "https://duckduckgo.com/", "Accept-Language": "en-US,en;q=0.9"}
    items: list[dict[str, Any]] = []
    for attempt in range(3):
        time.sleep(2 + 2 * attempt)  # space queries so DDG doesn't return an empty page
        try:
            if _HAS_CFFI:
                resp = cffi_requests.get(url, impersonate=CFFI_IMPERSONATE, timeout=timeout, headers=headers, allow_redirects=True)
            else:
                resp = session.get(url, timeout=timeout, headers=headers, allow_redirects=True)
            resp.raise_for_status()
            items = _parse_ddg_pdfs(resp.text)
        except Exception as exc:  # noqa: BLE001 - retry
            warn(f"  ddg attempt {attempt + 1} failed: {exc}")
            items = []
        if items:
            break

    kept = [it for it in items if not NON_REPORT_RE.search(it["source_url"]) and not NON_REPORT_RE.search(it["title"])]
    log(f"  ddg '{cfg['query']}' -> {len(items)} pdf results, kept {len(kept)} after non-report filter")
    return kept


def collect_html_listing_items(cfg: dict[str, Any], session: requests.Session, timeout: int) -> list[dict[str, Any]]:
    """Scrape a listing page for article links; each is resolved to a PDF later."""
    pattern = re.compile(cfg["item_link_pattern"], re.I)
    items: list[dict[str, Any]] = []
    seen_links: set[str] = set()
    for url in cfg["listing_urls"]:
        try:
            resp = session.get(url, timeout=timeout)
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
        "fieldsToInclude": ["title", "clickableuri", "imfdate", "imfcontenttype", "permanentid", "urihash"],
    }
    resp = session.post(
        cfg["coveo_url"],
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Origin": "https://www.imf.org",
            "Referer": "https://www.imf.org/",
        },
        json=body, timeout=timeout,
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
        epoch_ms = raw.get("imfdate")
        date_iso = ""
        if isinstance(epoch_ms, (int, float)):
            try:
                date_iso = datetime.fromtimestamp(epoch_ms / 1000, tz=timezone.utc).isoformat()
            except (ValueError, OSError):
                date_iso = ""
        is_file = bool(re.search(r"\.(pdf|ashx)(\?|$)", landing, re.I))
        items.append({
            "title": result.get("title") or raw.get("title") or landing,
            "source_url": landing,
            "guid": raw.get("permanentid") or raw.get("urihash") or landing,
            "date": date_iso,
            "pdf_candidates": [landing] if is_file else [],
            "scrape_url": "" if is_file else landing,
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


def download_pdf(session: requests.Session, urls: Iterable[str], dest: Path, timeout: int, max_bytes: int, impersonate: bool = False) -> tuple[str | None, str]:
    """Try each candidate URL; save the first that is a real PDF. Returns (used_url, status)."""
    last_status = "no_candidate"
    for url in urls:
        if not url:
            continue
        try:
            if impersonate and _HAS_CFFI:
                # curl_cffi: read fully (bounded below), no chunked streaming API needed.
                resp = cffi_requests.get(url, timeout=timeout, impersonate=CFFI_IMPERSONATE, allow_redirects=True)
                if resp.status_code >= 400:
                    last_status = f"http_{resp.status_code}"
                    continue
                data = resp.content
                if len(data) > max_bytes:
                    last_status = "too_large"
                    continue
            else:
                with session.get(url, stream=True, timeout=timeout, allow_redirects=True) as resp:
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
    parser.add_argument("--request-timeout", type=int, default=60)
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = Path(args.archive_path)
    seen_path = Path(args.seen_state_path)
    max_bytes = int(args.max_pdf_mb * 1024 * 1024)

    if args.institutions.strip().lower() in {"all", "*", ""}:
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

    downloaded: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []

    for key in enabled:
        cfg = INSTITUTIONS[key]
        log(f"== {cfg['name_en']} ({cfg['name_cn']}) ==")
        try:
            if cfg["kind"] == "worldbank_api":
                items = collect_worldbank_items(cfg, session, args.request_timeout, args.worldbank_rows)
            elif cfg["kind"] == "coveo_api":
                items = collect_coveo_items(cfg, session, args.request_timeout, args.imf_rows)
            elif cfg["kind"] == "ddg_search":
                items = collect_ddg_items(cfg, session, args.request_timeout, args.ddg_df)
            elif cfg["kind"] == "html_listing":
                items = collect_html_listing_items(cfg, session, args.request_timeout)
            else:
                items = collect_rss_items(cfg, session, args.request_timeout)
        except Exception as exc:  # noqa: BLE001 - never let one source kill the run
            warn(f"{cfg['name_en']} source failed entirely: {exc}")
            continue

        new_count = 0
        for item in items:
            if args.max_per_institution and new_count >= args.max_per_institution:
                break

            dedup_key = f"{key}:{item['guid'] or item['source_url']}"
            if dedup_key in seen_items:
                continue

            published = parse_date(item["date"])
            if cfg.get("recency_filter", True) and published is not None and published < cutoff:
                # Old item we have simply never recorded; mark it so we do not keep
                # re-checking it every day, but do not download it.
                seen_items[dedup_key] = {"first_seen": today, "status": "too_old"}
                continue

            candidates = list(item["pdf_candidates"])
            if not candidates and item.get("scrape_url"):
                try:
                    page = http_get(session, item["scrape_url"], args.request_timeout, cfg.get("impersonate", False))
                    page.raise_for_status()
                    candidates = scrape_pdf_candidates(page.text, item["scrape_url"])
                    if not item["title"]:
                        item["title"] = _extract_html_title(page.text)
                except Exception as exc:  # noqa: BLE001 - network error: retry next run
                    warn(f"  landing fetch failed, will retry next run: {item['source_url']}: {exc}")
                    continue

            if not candidates:
                # Page reachable but has no downloadable PDF (e.g. a Brookings op-ed).
                seen_items[dedup_key] = {"first_seen": today, "status": "no_pdf"}
                skipped.append({"institution": key, "title": item["title"], "reason": "no_pdf", "source_url": item["source_url"]})
                continue

            title = item["title"] or item["guid"] or item["source_url"]
            filename = f"{cfg['token']}_{slug(title)}_{short_hash(dedup_key)}.pdf"
            dest = output_dir / filename
            used_url, status = download_pdf(session, candidates[:3], dest, args.request_timeout, max_bytes, impersonate=cfg.get("impersonate", False))
            if status != "ok" or used_url is None:
                # Could not download; do NOT mark seen so a transient failure is retried.
                warn(f"  download failed ({status}): {title[:80]}")
                skipped.append({"institution": key, "title": title, "reason": status, "source_url": item["source_url"]})
                continue

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
            }
            append_archive(archive_path, record)
            downloaded.append(record)
            new_count += 1
            log(f"  saved {filename} ({record['bytes'] // 1024} KB) <- {used_url}")

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
        "downloaded": downloaded,
        "skipped": skipped,
    }
    (output_dir / "institution_run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    write_github_output("pdf_count", str(len(downloaded)))
    write_github_output("output_dir", str(output_dir))
    write_github_output("date_folder", args.date)
    log(f"Done. Downloaded {len(downloaded)} new PDF(s), skipped {len(skipped)}.")
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
