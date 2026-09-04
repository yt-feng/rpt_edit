#!/usr/bin/env python3
"""Run a read-only SEO health audit against a deployed Portal site."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from typing import Any, Callable
from urllib.error import HTTPError
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener, urlopen
import xml.etree.ElementTree as ET


DEFAULT_SITE_URL = "https://portal.example.invalid"
DEFAULT_INDEXNOW_KEY = "b7c3e9a41d8f52e604a71bc93f2d6e80"
DEFAULT_SAMPLE_SIZE = 18
DEFAULT_TIMEOUT_SECONDS = 20.0
MAX_DOCUMENT_BYTES = 12 * 1024 * 1024
MAX_SITEMAP_SHARDS = 1_000
MAX_URLS_PER_SITEMAP = 50_000
PORTAL_LOCALES = ("ko", "ja", "ar")
REQUIRED_HREFLANGS = ("zh-Hans", "ko", "ja", "ar", "x-default")


@dataclass(frozen=True)
class FetchResult:
    status: int
    final_url: str
    headers: dict[str, str]
    body: bytes
    truncated: bool = False


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(
        self,
        request: Request,
        file_pointer: Any,
        code: int,
        message: str,
        headers: Any,
        new_url: str,
    ) -> None:
        return None


class HttpFetcher:
    def __init__(self, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> None:
        self.timeout = timeout
        self.no_redirect_opener = build_opener(_NoRedirect)

    def __call__(self, url: str, *, follow_redirects: bool = True) -> FetchResult:
        request = Request(
            url,
            headers={
                "Accept": "text/html,application/xml,text/xml,image/*;q=0.8,*/*;q=0.5",
                "User-Agent": "portal-seo-health/1.0",
            },
        )
        try:
            if follow_redirects:
                response = urlopen(request, timeout=self.timeout)
            else:
                response = self.no_redirect_opener.open(request, timeout=self.timeout)
            with response:
                body = response.read(MAX_DOCUMENT_BYTES + 1)
                return FetchResult(
                    status=int(response.status),
                    final_url=str(response.geturl()),
                    headers={str(key).lower(): str(value) for key, value in response.headers.items()},
                    body=body[:MAX_DOCUMENT_BYTES],
                    truncated=len(body) > MAX_DOCUMENT_BYTES,
                )
        except HTTPError as error:
            body = error.read(MAX_DOCUMENT_BYTES + 1)
            return FetchResult(
                status=int(error.code),
                final_url=str(error.geturl()),
                headers={str(key).lower(): str(value) for key, value in error.headers.items()},
                body=body[:MAX_DOCUMENT_BYTES],
                truncated=len(body) > MAX_DOCUMENT_BYTES,
            )


class SeoHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []
        self.robots: list[str] = []
        self.icons: list[str] = []
        self.hreflangs: list[tuple[str, str]] = []
        self.html_lang = ""
        self.html_dir = ""
        self.json_ld_blocks: list[str] = []
        self._json_ld_buffer: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {str(key).lower(): str(value or "").strip() for key, value in attrs}
        lowered_tag = tag.lower()
        if lowered_tag == "html":
            self.html_lang = values.get("lang", "")
            self.html_dir = values.get("dir", "")
        elif lowered_tag == "link":
            rel_tokens = {token.lower() for token in re.split(r"\s+", values.get("rel", "")) if token}
            href = values.get("href", "")
            if "canonical" in rel_tokens and href:
                self.canonicals.append(href)
            if "alternate" in rel_tokens and href and values.get("hreflang"):
                self.hreflangs.append((values["hreflang"], href))
            if "icon" in rel_tokens and href:
                self.icons.append(href)
        elif lowered_tag == "meta" and values.get("name", "").lower() in {
            "robots",
            "googlebot",
            "bingbot",
        }:
            self.robots.append(values.get("content", ""))
        elif lowered_tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self._json_ld_buffer = []

    def handle_data(self, data: str) -> None:
        if self._json_ld_buffer is not None:
            self._json_ld_buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._json_ld_buffer is not None:
            self.json_ld_blocks.append("".join(self._json_ld_buffer).strip())
            self._json_ld_buffer = None


def normalize_site_url(value: str) -> str:
    parsed = urlsplit(str(value or "").strip())
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("site_url_must_be_clean_https_origin")
    if parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
        raise ValueError("site_url_must_not_include_path_query_or_fragment")
    if parsed.hostname.lower().startswith("www."):
        raise ValueError("site_url_must_use_canonical_non_www_host")
    return urlunsplit(("https", parsed.netloc.lower(), "", "", "")).rstrip("/")


def canonical_identity(value: str) -> tuple[str, str, int | None, str, str] | None:
    parsed = urlsplit(str(value or "").strip())
    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.hostname
        or parsed.username
        or parsed.password
        or parsed.fragment
    ):
        return None
    try:
        port = parsed.port
    except ValueError:
        return None
    if port == 443 and parsed.scheme == "https":
        port = None
    if port == 80 and parsed.scheme == "http":
        port = None
    return (
        parsed.scheme.lower(),
        parsed.hostname.lower(),
        port,
        unquote(parsed.path or "/"),
        parsed.query,
    )


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def xml_text(node: ET.Element | None) -> str:
    return " ".join(str(node.text or "").split()) if node is not None else ""


def parse_xml_discovery(body: bytes) -> tuple[str, list[str]]:
    root = ET.fromstring(body)
    kind = local_name(root.tag)
    if kind == "sitemapindex":
        values = [xml_text(row.find("./{*}loc")) for row in root.findall("./{*}sitemap")]
    elif kind == "urlset":
        values = [xml_text(row.find("./{*}loc")) for row in root.findall("./{*}url")]
    elif kind == "rss":
        values = [xml_text(row.find("./link")) for row in root.findall("./channel/item")]
    elif kind == "feed":
        values = [str(row.get("href") or "").strip() for row in root.findall("./{*}entry/{*}link")]
    else:
        values = []
    return kind, [value for value in values if value]


def target_path(url: str, fallback: str = "request") -> str:
    parsed = urlsplit(str(url or ""))
    if not parsed.path:
        return "/"
    return parsed.path if len(parsed.path) <= 240 else fallback


def is_same_origin(url: str, site_url: str) -> bool:
    candidate = canonical_identity(url)
    origin = canonical_identity(site_url + "/")
    return bool(candidate and origin and candidate[:3] == origin[:3])


def robots_directives(text: str) -> tuple[list[str], bool]:
    sitemap_urls: list[str] = []
    active_agents: set[str] = set()
    wildcard_disallows_root = False
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        name, value = (part.strip() for part in line.split(":", 1))
        lowered = name.lower()
        if lowered == "user-agent":
            active_agents = {value.lower()}
        elif lowered == "disallow" and "*" in active_agents and value == "/":
            wildcard_disallows_root = True
        elif lowered == "sitemap" and value:
            sitemap_urls.append(value)
    return sitemap_urls, wildcard_disallows_root


def cloudflare_managed_robots_search_signal(text: str) -> tuple[bool, str]:
    """Return whether Cloudflare owns the robots block and its wildcard search signal."""
    managed = bool(
        re.search(r"(?im)^\s*#\s*BEGIN\s+Cloudflare\s+Managed\s+content\s*$", text)
        and re.search(r"(?im)^\s*#\s*END\s+Cloudflare\s+Managed\s+Content\s*$", text)
    )
    if not managed:
        return False, ""

    active_agents: set[str] = set()
    search_signal = ""
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        name, value = (part.strip() for part in line.split(":", 1))
        lowered = name.lower()
        if lowered == "user-agent":
            active_agents = {value.lower()}
        elif lowered == "content-signal" and "*" in active_agents:
            for token in value.split(","):
                key, separator, signal_value = token.partition("=")
                if separator and key.strip().lower() == "search":
                    search_signal = signal_value.strip().lower()
    return True, search_signal


def robots_has_noindex(values: list[str], header_value: str = "") -> bool:
    tokens: set[str] = set()
    for value in [*values, header_value]:
        tokens.update(token.lower() for token in re.split(r"[,\s]+", value) if token)
    return "noindex" in tokens or "none" in tokens


def valid_json_ld(block: str) -> bool:
    try:
        payload = json.loads(block)
    except (TypeError, json.JSONDecodeError):
        return False

    def has_schema_node(value: Any) -> bool:
        if isinstance(value, dict):
            if "@type" in value or str(value.get("@context") or "").startswith("https://schema.org"):
                return True
            return any(has_schema_node(child) for child in value.values())
        if isinstance(value, list):
            return any(has_schema_node(child) for child in value)
        return False

    return has_schema_node(payload)


def json_ld_has_in_language(block: str, language: str) -> bool:
    try:
        payload = json.loads(block)
    except (TypeError, json.JSONDecodeError):
        return False
    expected = str(language or "").strip().lower()

    def contains(value: Any) -> bool:
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "inLanguage":
                    candidates = child if isinstance(child, list) else [child]
                    if any(str(candidate or "").strip().lower() == expected for candidate in candidates):
                        return True
                if contains(child):
                    return True
        elif isinstance(value, list):
            return any(contains(child) for child in value)
        return False

    return contains(payload)


class AuditState:
    def __init__(self, site_url: str, fetcher: Callable[..., FetchResult]) -> None:
        self.site_url = site_url
        self.fetcher = fetcher
        self.failures: list[dict[str, str]] = []
        self.warnings: list[dict[str, str]] = []
        self.request_count = 0

    def fail(self, category: str, code: str, message: str, target: str) -> None:
        self.failures.append(
            {
                "category": category,
                "code": code,
                "message": message,
                "target": target,
            }
        )

    def warn(self, category: str, code: str, message: str, target: str) -> None:
        self.warnings.append(
            {
                "category": category,
                "code": code,
                "message": message,
                "target": target,
            }
        )

    def fetch(self, url: str, *, follow_redirects: bool = True, target: str | None = None) -> FetchResult | None:
        self.request_count += 1
        try:
            return self.fetcher(url, follow_redirects=follow_redirects)
        except Exception as error:  # Network failures are represented, never hidden.
            self.fail(
                "transport",
                "request_failed",
                f"HTTP request failed ({type(error).__name__})",
                target or target_path(url),
            )
            return None


def sample_urls_by_shard(shards: list[tuple[str, list[str]]], sample_size: int) -> list[str]:
    if sample_size <= 0:
        return []
    selected: list[str] = []
    seen: set[str] = set()
    for _path, urls in shards:
        if urls and urls[0] not in seen:
            seen.add(urls[0])
            selected.append(urls[0])
            if len(selected) >= sample_size:
                return selected
    remaining = sorted(
        {url for _path, urls in shards for url in urls if url not in seen},
        key=lambda url: sha256(url.encode("utf-8")).hexdigest(),
    )
    selected.extend(remaining[: max(0, sample_size - len(selected))])
    return selected


def audit_site(
    site_url: str = DEFAULT_SITE_URL,
    *,
    indexnow_key: str = "",
    sample_size: int = DEFAULT_SAMPLE_SIZE,
    fetcher: Callable[..., FetchResult] | None = None,
) -> dict[str, Any]:
    canonical_site = normalize_site_url(site_url)
    state = AuditState(canonical_site, fetcher or HttpFetcher())
    canonical_root = canonical_site + "/"
    root_identity = canonical_identity(canonical_root)

    robots_url = urljoin(canonical_root, "robots.txt")
    robots_response = state.fetch(robots_url)
    advertised_sitemaps: list[str] = []
    robots_ok = False
    robots_managed_by_cloudflare = False
    robots_search_signal = ""
    robots_sitemap_warning = False
    if robots_response is None:
        pass
    elif robots_response.status != 200:
        state.fail("robots", "http_status", "robots.txt did not return HTTP 200", "/robots.txt")
    elif robots_response.truncated:
        state.fail("robots", "document_too_large", "robots.txt exceeded the audit size limit", "/robots.txt")
    else:
        robots_text = robots_response.body.decode("utf-8", errors="replace")
        advertised_sitemaps, wildcard_block = robots_directives(robots_text)
        robots_managed_by_cloudflare, robots_search_signal = cloudflare_managed_robots_search_signal(robots_text)
        robots_ok = True
        if wildcard_block:
            state.fail("robots", "wildcard_root_blocked", "The wildcard crawler group disallows the site root", "/robots.txt")
        if robots_managed_by_cloudflare and robots_search_signal == "no":
            state.fail(
                "robots",
                "managed_search_disabled",
                "Cloudflare Managed robots explicitly disables search indexing",
                "/robots.txt",
            )
        managed_search_enabled = robots_managed_by_cloudflare and robots_search_signal == "yes"
        if not advertised_sitemaps and managed_search_enabled:
            robots_sitemap_warning = True
            state.warn(
                "robots",
                "managed_sitemap_not_advertised",
                "Cloudflare Managed robots permits search but does not advertise /sitemap.xml; the discovery file is audited independently",
                "/robots.txt",
            )
        else:
            if not advertised_sitemaps:
                state.fail("robots", "sitemap_missing", "robots.txt does not advertise a discovery file", "/robots.txt")
            if not any(canonical_identity(url) == canonical_identity(urljoin(canonical_root, "sitemap.xml")) for url in advertised_sitemaps):
                state.fail("robots", "canonical_sitemap_missing", "robots.txt does not advertise /sitemap.xml", "/robots.txt")
        for advertised in advertised_sitemaps:
            if not is_same_origin(advertised, canonical_site):
                state.fail("robots", "off_origin_sitemap", "robots.txt advertises an off-origin discovery file", "/robots.txt")

    sitemap_url = urljoin(canonical_root, "sitemap.xml")
    sitemap_response = state.fetch(sitemap_url)
    root_sitemap_kind = "unavailable"
    root_values: list[str] = []
    shards: list[tuple[str, list[str]]] = []
    declared_shard_count = 0
    if sitemap_response is None:
        pass
    elif sitemap_response.status != 200:
        state.fail("sitemap", "root_http_status", "/sitemap.xml did not return HTTP 200", "/sitemap.xml")
    elif sitemap_response.truncated:
        state.fail("sitemap", "root_too_large", "/sitemap.xml exceeded the audit size limit", "/sitemap.xml")
    else:
        try:
            root_sitemap_kind, root_values = parse_xml_discovery(sitemap_response.body)
        except ET.ParseError:
            state.fail("sitemap", "root_invalid_xml", "/sitemap.xml is not valid XML", "/sitemap.xml")
            root_values = []
        if root_sitemap_kind == "urlset":
            shards.append(("/sitemap.xml", root_values))
            declared_shard_count = 1
        elif root_sitemap_kind == "sitemapindex":
            declared_shard_count = len(root_values)
            if not root_values:
                state.fail("sitemap", "index_empty", "The sitemap index contains no shards", "/sitemap.xml")
            if len(root_values) > MAX_SITEMAP_SHARDS:
                state.fail("sitemap", "too_many_shards", "The sitemap index exceeds the audit shard limit", "/sitemap.xml")
                root_values = root_values[:MAX_SITEMAP_SHARDS]
            for shard_url in root_values:
                shard_target = target_path(shard_url, "sitemap_shard")
                if not is_same_origin(shard_url, canonical_site):
                    state.fail("sitemap", "off_origin_shard", "A sitemap shard is off-origin", shard_target)
                    continue
                shard_response = state.fetch(shard_url, target=shard_target)
                if shard_response is None:
                    continue
                if shard_response.status != 200:
                    state.fail("sitemap", "shard_http_status", "A sitemap shard did not return HTTP 200", shard_target)
                    continue
                if shard_response.truncated:
                    state.fail("sitemap", "shard_too_large", "A sitemap shard exceeded the audit size limit", shard_target)
                    continue
                try:
                    shard_kind, shard_values = parse_xml_discovery(shard_response.body)
                except ET.ParseError:
                    state.fail("sitemap", "shard_invalid_xml", "A sitemap shard is not valid XML", shard_target)
                    continue
                if shard_kind != "urlset":
                    state.fail("sitemap", "shard_wrong_root", "A sitemap shard is not a urlset", shard_target)
                    continue
                shards.append((shard_target, shard_values))
        elif root_sitemap_kind != "unavailable":
            state.fail("sitemap", "root_wrong_type", "/sitemap.xml is neither a sitemap index nor a urlset", "/sitemap.xml")

    locale_sitemaps: dict[str, str] = {}
    if root_sitemap_kind == "sitemapindex":
        for locale in PORTAL_LOCALES:
            expected = canonical_identity(urljoin(canonical_root, f"sitemap-{locale}.xml"))
            matches = [value for value in root_values if canonical_identity(value) == expected]
            if matches:
                locale_sitemaps[locale] = matches[0]

    all_urls = [url for _path, urls in shards for url in urls]
    same_origin_urls: list[str] = []
    for shard_path, urls in shards:
        if not urls:
            state.fail("sitemap", "shard_empty", "A sitemap shard contains no URLs", shard_path)
        if len(urls) > MAX_URLS_PER_SITEMAP:
            state.fail("sitemap", "shard_url_limit", "A sitemap shard exceeds 50,000 URLs", shard_path)
        for url in urls:
            if not is_same_origin(url, canonical_site):
                state.fail("sitemap", "off_origin_url", "A sitemap URL is off-origin", shard_path)
            else:
                same_origin_urls.append(url)
    duplicate_count = len(same_origin_urls) - len(set(same_origin_urls))
    if duplicate_count:
        state.fail("sitemap", "duplicate_urls", "The sitemap index contains duplicate canonical URLs", "/sitemap.xml")
    if not same_origin_urls:
        state.fail("sitemap", "no_canonical_urls", "No same-origin canonical URLs were found", "/sitemap.xml")

    sample_shards = [
        (path, [url for url in urls if is_same_origin(url, canonical_site)])
        for path, urls in shards
    ]
    sampled_urls = sample_urls_by_shard(sample_shards, sample_size)
    if canonical_root not in sampled_urls:
        sampled_urls = ([canonical_root] + sampled_urls)[: max(1, sample_size)]
    sample_metrics = {
        "requested": len(sampled_urls),
        "http_200": 0,
        "indexable": 0,
        "self_canonical": 0,
        "structured_data": 0,
    }
    homepage_parser: SeoHtmlParser | None = None
    for page_url in sampled_urls:
        page_target = target_path(page_url, "sample_page")
        page_response = state.fetch(page_url, target=page_target)
        if page_response is None:
            continue
        if page_response.status != 200:
            state.fail("sample_http", "http_status", "A sampled sitemap URL did not return HTTP 200", page_target)
            continue
        if page_response.truncated:
            state.fail("sample_http", "document_too_large", "A sampled page exceeded the audit size limit", page_target)
            continue
        sample_metrics["http_200"] += 1
        parser = SeoHtmlParser()
        parser.feed(page_response.body.decode("utf-8", errors="replace"))
        if canonical_identity(page_url) == root_identity:
            homepage_parser = parser
        if robots_has_noindex(parser.robots, page_response.headers.get("x-robots-tag", "")):
            state.fail("noindex", "sample_noindex", "A sitemap sample declares noindex", page_target)
        else:
            sample_metrics["indexable"] += 1
        resolved_canonicals = [urljoin(page_url, value) for value in parser.canonicals]
        if not resolved_canonicals:
            state.fail("canonical", "missing", "A sitemap sample has no canonical link", page_target)
        elif len(resolved_canonicals) != 1:
            state.fail("canonical", "multiple", "A sitemap sample has multiple canonical links", page_target)
        elif canonical_identity(resolved_canonicals[0]) != canonical_identity(page_url):
            state.fail("canonical", "not_self", "A sitemap sample canonical does not point to itself", page_target)
        else:
            sample_metrics["self_canonical"] += 1
        if not parser.json_ld_blocks:
            state.fail("structured_data", "missing", "A sitemap sample has no JSON-LD", page_target)
        elif not any(valid_json_ld(block) for block in parser.json_ld_blocks):
            state.fail("structured_data", "invalid", "A sitemap sample has no valid schema node", page_target)
        else:
            sample_metrics["structured_data"] += 1

    indexnow_configured = bool(indexnow_key)
    indexnow_verified = False
    if not indexnow_key:
        state.fail("indexnow", "key_not_configured", "No IndexNow key was supplied to the audit", "indexnow_key")
    elif not re.fullmatch(r"[A-Za-z0-9-]{8,128}", indexnow_key):
        state.fail("indexnow", "key_invalid", "The supplied IndexNow key format is invalid", "indexnow_key")
    else:
        key_response = state.fetch(urljoin(canonical_root, f"{indexnow_key}.txt"), target="indexnow_key")
        if key_response is None:
            pass
        elif key_response.status != 200:
            state.fail("indexnow", "key_http_status", "The IndexNow key file did not return HTTP 200", "indexnow_key")
        elif key_response.body.decode("utf-8", errors="replace").strip() != indexnow_key:
            state.fail("indexnow", "key_content_mismatch", "The IndexNow key file content does not match", "indexnow_key")
        else:
            indexnow_verified = True

    if homepage_parser is None:
        homepage_response = state.fetch(canonical_root, target="/")
        if homepage_response is not None and homepage_response.status == 200:
            homepage_parser = SeoHtmlParser()
            homepage_parser.feed(homepage_response.body.decode("utf-8", errors="replace"))

    declared_locales = [locale for locale in PORTAL_LOCALES if locale in locale_sitemaps]
    locale_bundle_enabled = len(declared_locales) == len(PORTAL_LOCALES)
    if declared_locales and not locale_bundle_enabled:
        missing_locales = [locale for locale in PORTAL_LOCALES if locale not in locale_sitemaps]
        state.fail(
            "locale",
            "sitemap_set_incomplete",
            "Localized sitemaps must be declared as one ko/ja/ar set; missing " + ", ".join(missing_locales),
            "/sitemap.xml",
        )
    enabled_locales = list(PORTAL_LOCALES) if locale_bundle_enabled else []
    locale_metrics: dict[str, Any] = {
        "enabled": locale_bundle_enabled,
        "declared_sitemaps": declared_locales,
        "requested": 0,
        "http_200": 0,
        "html_lang": 0,
        "arabic_rtl": 0,
        "self_canonical": 0,
        "reciprocal_hreflang": 0,
        "json_ld_in_language": 0,
    }
    if enabled_locales:
        locale_pages: dict[str, tuple[str, SeoHtmlParser]] = {}
        for locale in enabled_locales:
            page_url = urljoin(canonical_root, f"{locale}/")
            page_target = f"/{locale}/"
            locale_metrics["requested"] += 1
            page_response = state.fetch(page_url, target=page_target)
            if page_response is None:
                state.fail("locale", "request_failed", "A localized homepage request failed", page_target)
                continue
            if page_response.status != 200:
                state.fail("locale", "http_status", "A localized homepage did not return HTTP 200", page_target)
                continue
            if page_response.truncated:
                state.fail("locale", "document_too_large", "A localized homepage exceeded the audit size limit", page_target)
                continue
            locale_metrics["http_200"] += 1
            parser = SeoHtmlParser()
            parser.feed(page_response.body.decode("utf-8", errors="replace"))
            locale_pages[locale] = (page_url, parser)

            if parser.html_lang.strip().lower() != locale:
                state.fail("locale", "html_lang_mismatch", "A localized homepage has the wrong html lang", page_target)
            else:
                locale_metrics["html_lang"] += 1
            if locale == "ar":
                if parser.html_dir.strip().lower() != "rtl":
                    state.fail("locale", "arabic_not_rtl", "The Arabic homepage is not marked dir=rtl", page_target)
                else:
                    locale_metrics["arabic_rtl"] += 1

            resolved_canonicals = [urljoin(page_url, value) for value in parser.canonicals]
            if len(resolved_canonicals) != 1:
                state.fail("locale", "canonical_count", "A localized homepage must have one canonical", page_target)
            elif canonical_identity(resolved_canonicals[0]) != canonical_identity(page_url):
                state.fail("locale", "canonical_not_self", "A localized homepage canonical is not self-referential", page_target)
            else:
                locale_metrics["self_canonical"] += 1

            if not any(json_ld_has_in_language(block, locale) for block in parser.json_ld_blocks):
                state.fail(
                    "locale",
                    "json_ld_in_language_missing",
                    "A localized homepage JSON-LD does not declare its inLanguage",
                    page_target,
                )
            else:
                locale_metrics["json_ld_in_language"] += 1

        expected_hreflangs = {
            "zh-hans": canonical_root,
            "ko": urljoin(canonical_root, "ko/"),
            "ja": urljoin(canonical_root, "ja/"),
            "ar": urljoin(canonical_root, "ar/"),
            "x-default": canonical_root,
        }
        cluster_pages: list[tuple[str, str, SeoHtmlParser | None]] = [
            ("zh-Hans", canonical_root, homepage_parser)
        ]
        cluster_pages.extend(
            (locale, page_url, parser)
            for locale, (page_url, parser) in locale_pages.items()
        )
        for page_language, page_url, parser in cluster_pages:
            page_target = "/" if page_language == "zh-Hans" else f"/{page_language}/"
            if parser is None:
                state.fail("locale", "hreflang_page_unavailable", "A hreflang cluster page is unavailable", page_target)
                continue
            grouped: dict[str, list[str]] = {}
            for language, href in parser.hreflangs:
                grouped.setdefault(language.strip().lower(), []).append(urljoin(page_url, href))
            page_ok = True
            for language in REQUIRED_HREFLANGS:
                key = language.lower()
                values = grouped.get(key, [])
                if len(values) != 1:
                    state.fail(
                        "locale",
                        "hreflang_count",
                        f"A locale cluster page must have one {language} hreflang",
                        page_target,
                    )
                    page_ok = False
                elif canonical_identity(values[0]) != canonical_identity(expected_hreflangs[key]):
                    state.fail(
                        "locale",
                        "hreflang_target_mismatch",
                        f"A locale cluster page has the wrong {language} hreflang target",
                        page_target,
                    )
                    page_ok = False
            if page_ok:
                locale_metrics["reciprocal_hreflang"] += 1

    icon_candidates = [] if homepage_parser is None else [urljoin(canonical_root, value) for value in homepage_parser.icons]
    unique_icon_candidates = list(dict.fromkeys(icon_candidates))
    favicon_verified = False
    if not unique_icon_candidates:
        state.fail("favicon", "declaration_missing", "The homepage has no rel=icon declaration", "favicon")
    for icon_url in unique_icon_candidates:
        if not is_same_origin(icon_url, canonical_site):
            state.fail("favicon", "off_origin", "The declared homepage icon is off-origin", "favicon")
            continue
        icon_response = state.fetch(icon_url, target="favicon")
        if icon_response is None:
            continue
        content_type = icon_response.headers.get("content-type", "").lower()
        if icon_response.status == 200 and icon_response.body and content_type.startswith("image/"):
            favicon_verified = True
            break
    if not favicon_verified:
        state.fail("favicon", "unavailable", "No declared same-origin homepage icon returned a usable image", "favicon")

    parsed_site = urlsplit(canonical_root)
    alias_netloc = f"www.{parsed_site.hostname}"
    if parsed_site.port:
        alias_netloc += f":{parsed_site.port}"
    alias_url = urlunsplit((parsed_site.scheme, alias_netloc, "/", "", ""))
    alias_response = state.fetch(alias_url, follow_redirects=False, target="www_alias_root")
    alias_status = None if alias_response is None else alias_response.status
    alias_location_matches = False
    if alias_response is not None:
        location = alias_response.headers.get("location", "")
        alias_location_matches = canonical_identity(urljoin(alias_url, location)) == root_identity
        if alias_response.status != 301:
            state.fail("alias", "not_permanent_redirect", "The bare www alias root did not return HTTP 301", "www_alias_root")
        elif not alias_location_matches:
            state.fail("alias", "location_mismatch", "The www alias Location does not equal the canonical root", "www_alias_root")

    category_counts = Counter(item["category"] for item in state.failures)
    warning_counts = Counter(item["category"] for item in state.warnings)
    category_groups = {
        "robots": {"robots", "transport"},
        "sitemap": {"sitemap", "transport"},
        "sample_pages": {"sample_http", "canonical", "noindex", "structured_data", "transport"},
        "indexnow": {"indexnow", "transport"},
        "favicon": {"favicon", "transport"},
        "www_alias": {"alias", "transport"},
        "locales": {"locale"},
    }
    report: dict[str, Any] = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "ok": not state.failures,
        "site": {
            "https": True,
            "canonical_host_kind": "non_www",
            "production_identity_included": False,
        },
        "checks": {
            name: {"ok": not any(category_counts.get(category, 0) for category in categories)}
            for name, categories in category_groups.items()
        },
        "metrics": {
            "http_requests": state.request_count,
            "robots": {
                "http_ok": robots_ok,
                "advertised_discovery_files": len(advertised_sitemaps),
                "managed_by_cloudflare": robots_managed_by_cloudflare,
                "search_content_signal": robots_search_signal or "unspecified",
                "canonical_sitemap_advertised": any(
                    canonical_identity(url) == canonical_identity(urljoin(canonical_root, "sitemap.xml"))
                    for url in advertised_sitemaps
                ),
                "managed_sitemap_warning": robots_sitemap_warning,
            },
            "sitemap": {
                "root_type": root_sitemap_kind,
                "declared_shards": declared_shard_count,
                "validated_shards": len(shards),
                "total_urls": len(all_urls),
                "unique_same_origin_urls": len(set(same_origin_urls)),
                "duplicate_urls": duplicate_count,
                "shards": [{"path": path, "url_count": len(urls)} for path, urls in shards],
            },
            "samples": sample_metrics,
            "locales": locale_metrics,
            "indexnow": {"configured": indexnow_configured, "key_file_verified": indexnow_verified},
            "favicon": {"verified": favicon_verified},
            "www_alias": {
                "status": alias_status,
                "location_matches_canonical": alias_location_matches,
            },
        },
        "failure_counts": dict(sorted(category_counts.items())),
        "failures": state.failures[:100],
        "warning_counts": dict(sorted(warning_counts.items())),
        "warnings": state.warnings[:100],
    }
    return report


def render_markdown(report: dict[str, Any]) -> str:
    metrics = report.get("metrics", {})
    sitemap = metrics.get("sitemap", {})
    samples = metrics.get("samples", {})
    result = "通过" if report.get("ok") else "未通过"
    lines = [
        "# Portal SEO 健康检查",
        "",
        f"- 结果：**{result}**",
        f"- Sitemap：{sitemap.get('validated_shards', 0)}/{sitemap.get('declared_shards', 0)} 个分片通过，共 {sitemap.get('unique_same_origin_urls', 0)} 个唯一站内 URL",
        f"- 页面抽样：{samples.get('self_canonical', 0)}/{samples.get('requested', 0)} self-canonical，{samples.get('indexable', 0)}/{samples.get('requested', 0)} 可索引，{samples.get('structured_data', 0)}/{samples.get('requested', 0)} 含有效结构化数据",
        f"- IndexNow key：{'通过' if metrics.get('indexnow', {}).get('key_file_verified') else '未通过'}",
        f"- Favicon/品牌图标：{'通过' if metrics.get('favicon', {}).get('verified') else '未通过'}",
        f"- www 裸域 301：{'通过' if metrics.get('www_alias', {}).get('status') == 301 and metrics.get('www_alias', {}).get('location_matches_canonical') else '未通过'}",
    ]
    locales = metrics.get("locales", {})
    if locales.get("enabled"):
        requested = int(locales.get("requested", 0))
        cluster_pages = requested + 1
        lines.append(
            f"- 多语言 SEO：{locales.get('http_200', 0)}/{requested} 个 locale 首页返回 200，"
            f"{locales.get('reciprocal_hreflang', 0)}/{cluster_pages} 个页面 hreflang 互惠通过"
        )
    robots = metrics.get("robots", {})
    if robots.get("managed_by_cloudflare"):
        lines.append(
            f"- Robots 管理层：Cloudflare Managed（search={robots.get('search_content_signal', 'unspecified')}；"
            f"Sitemap 声明：{'有' if robots.get('canonical_sitemap_advertised') else '无，已独立校验 /sitemap.xml'}）"
        )
    failures = report.get("failures", [])
    if failures:
        lines.extend(["", "## 故障分类", "", "| 分类 | 代码 | 目标 |", "|---|---|---|"])
        for item in failures:
            lines.append(f"| {item.get('category', '')} | {item.get('code', '')} | {item.get('target', '')} |")
    warnings = report.get("warnings", [])
    if warnings:
        lines.extend(["", "## 警告", "", "| 分类 | 代码 | 目标 |", "|---|---|---|"])
        for item in warnings:
            lines.append(f"| {item.get('category', '')} | {item.get('code', '')} | {item.get('target', '')} |")
    return "\n".join(lines) + "\n"


def write_text_output(path_value: str, content: str) -> None:
    if path_value == "-":
        print(content, end="")
        return
    path = Path(path_value)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def invalid_input_report(code: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "ok": False,
        "site": {"production_identity_included": False},
        "checks": {},
        "metrics": {},
        "failure_counts": {"input": 1},
        "failures": [
            {
                "category": "input",
                "code": code,
                "message": "The site URL configuration is invalid",
                "target": "site_url",
            }
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL, help="Canonical HTTPS site origin")
    parser.add_argument(
        "--indexnow-key",
        default=os.environ.get("PORTAL_INDEXNOW_KEY", "") or DEFAULT_INDEXNOW_KEY,
        help="Public IndexNow key deployed at the site root",
    )
    parser.add_argument("--sample-size", type=int, default=DEFAULT_SAMPLE_SIZE)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--output", default="-", help="Aggregate JSON output path, or - for stdout")
    parser.add_argument("--markdown-output", help="Optional Markdown summary output path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.sample_size < 1 or args.sample_size > 200:
        report = invalid_input_report("sample_size_out_of_range")
    elif args.timeout <= 0 or args.timeout > 120:
        report = invalid_input_report("timeout_out_of_range")
    else:
        try:
            report = audit_site(
                args.site_url,
                indexnow_key=args.indexnow_key,
                sample_size=args.sample_size,
                fetcher=HttpFetcher(args.timeout),
            )
        except ValueError as error:
            report = invalid_input_report(str(error))
    write_text_output(args.output, json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    if args.markdown_output:
        write_text_output(args.markdown_output, render_markdown(report))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
