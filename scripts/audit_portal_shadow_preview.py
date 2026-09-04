#!/usr/bin/env python3
"""Build and verify a bounded review plan for an isolated locale preview."""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
from xml.etree import ElementTree as ET


LOCALES = {"ko": "ltr", "ja": "ltr", "ar": "rtl"}
SHADOW_ROBOTS = b"User-agent: *\nDisallow: /\n"
SHADOW_ROBOTS_HEADER = "noindex, nofollow, noarchive"
RELEASE_RE = re.compile(r"^[0-9a-f]{32}$")
TREE_RE = re.compile(r"^[0-9a-f]{64}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
WORKERS_DEV_LABEL_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$")
INVALID_PERCENT_RE = re.compile(r"%(?![0-9a-fA-F]{2})")
DOUBLE_ENCODED_RE = re.compile(r"%[0-9a-fA-F]{2}")
MAX_PLAN_BYTES = 1024 * 1024
MAX_MANIFEST_PATHS = 8192
MAX_RESPONSE_BYTES = 16 * 1024 * 1024
REQUIRED_SAMPLE_KINDS = (
    "home",
    "blog",
    "blog-detail",
    "reports",
    "report-detail",
    "charts",
)
OPTIONAL_SAMPLE_KINDS = {"blog-zsxq-clean"}
MANIFEST_MAP_GROUPS = (
    "catalog_overlays",
    "catalog_detail_overlays",
    "locale_data_files",
)
MANIFEST_ROW_GROUPS = ("chart_overlays", "hot_report_overlays")


class AuditError(RuntimeError):
    """Raised when the isolated preview does not match its candidate."""


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001, ANN201
        return None


class AssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.assets: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {str(key).lower(): str(value or "") for key, value in attrs}
        candidate = values.get("src") if tag.lower() == "script" else values.get("href")
        if not candidate:
            return
        parsed = urlsplit(candidate)
        if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
            return
        if parsed.path.lower().endswith((".css", ".js", ".mjs")):
            self.assets.add(parsed.path + (("?" + parsed.query) if parsed.query else ""))


def safe_output(path: Path) -> Path:
    target = Path(path)
    if target.exists() and (target.is_symlink() or not target.is_file()):
        raise AuditError(f"Output is not a regular file: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def validate_workers_dev_origin(base_url: str) -> str:
    try:
        parsed = urlsplit(base_url)
        port = parsed.port
    except ValueError as error:
        raise AuditError("Shadow preview URL must be a bare workers.dev HTTPS origin") from error
    hostname = parsed.hostname or ""
    labels = hostname.split(".")
    if (
        parsed.scheme != "https"
        or len(labels) < 3
        or labels[-2:] != ["workers", "dev"]
        or any(WORKERS_DEV_LABEL_RE.fullmatch(label) is None for label in labels[:-2])
        or parsed.username is not None
        or parsed.password is not None
        or port is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise AuditError("Shadow preview URL must be a bare workers.dev HTTPS origin")
    return base_url.rstrip("/")


def validate_public_origin(value: str) -> str:
    try:
        parsed = urlsplit(value)
        port = parsed.port
    except ValueError as error:
        raise AuditError("Public site URL must be a bare HTTPS origin") from error
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or port is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise AuditError("Public site URL must be a bare HTTPS origin")
    return f"https://{parsed.hostname.lower()}"


def validate_preview_path(relative: str, *, allow_query: bool) -> None:
    if not isinstance(relative, str) or not relative or len(relative) > 8192:
        raise AuditError(f"Unsafe preview path: {relative}")
    if any(ord(character) < 0x20 or ord(character) == 0x7F for character in relative):
        raise AuditError(f"Unsafe preview path: {relative}")
    parsed = urlsplit(relative)
    if (
        parsed.scheme
        or parsed.netloc
        or not parsed.path.startswith("/")
        or parsed.path.startswith("//")
        or "\\" in parsed.path
        or parsed.fragment
        or (parsed.query and not allow_query)
        or INVALID_PERCENT_RE.search(parsed.path)
    ):
        raise AuditError(f"Unsafe preview path: {relative}")
    try:
        decoded = unquote(parsed.path, errors="strict")
    except UnicodeDecodeError as error:
        raise AuditError(f"Unsafe preview path: {relative}") from error
    if (
        "\\" in decoded
        or "//" in decoded
        or any(ord(character) < 0x20 or ord(character) == 0x7F for character in decoded)
        or any(part in {".", ".."} for part in decoded.split("/"))
        or DOUBLE_ENCODED_RE.search(decoded)
    ):
        raise AuditError(f"Unsafe preview path: {relative}")
    if parsed.query and (
        len(parsed.query) > 2048
        or "\\" in parsed.query
        or any(ord(character) < 0x20 or ord(character) == 0x7F for character in parsed.query)
    ):
        raise AuditError(f"Unsafe preview path: {relative}")


def read_json_object(path: Path, label: str, *, max_bytes: int = MAX_PLAN_BYTES) -> dict[str, Any]:
    source = Path(path)
    if source.is_symlink() or not source.is_file():
        raise AuditError(f"{label} is unavailable")
    body = source.read_bytes()
    if not body or len(body) > max_bytes:
        raise AuditError(f"{label} has an invalid size")
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is invalid JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} is invalid")
    return payload


def route_for_html(locale: str, locale_root: Path, page: Path) -> str:
    relative = page.relative_to(locale_root).as_posix()
    if relative == "index.html":
        route = f"/{locale}/"
    elif relative.endswith("/index.html"):
        route = f"/{locale}/{relative[:-len('index.html')]}"
    else:
        route = f"/{locale}/{relative}"
    return quote(route, safe="/-._~")


def require_page(path: Path, label: str, *, root: Path | None = None) -> Path:
    if path.is_symlink() or not path.is_file() or path.stat().st_size <= 0:
        raise AuditError(f"Shadow review sample is missing: {label}")
    if root is not None:
        try:
            resolved = path.resolve(strict=True)
            resolved.relative_to(root.resolve(strict=True))
        except (OSError, ValueError) as error:
            raise AuditError(f"Shadow review sample escapes its locale root: {label}") from error
        if resolved != path.absolute():
            raise AuditError(f"Shadow review sample uses a symbolic path: {label}")
    return path


def first_detail(root: Path, section: str) -> Path:
    section_root = root / section
    if section_root.is_symlink() or not section_root.is_dir():
        raise AuditError(f"Shadow review has no {section} detail page")
    candidates = [
        require_page(path, f"{section} detail", root=root)
        for path in sorted(section_root.rglob("*.html"))
        if path.is_file() and not path.is_symlink() and path != section_root / "index.html"
    ]
    if not candidates:
        raise AuditError(f"Shadow review has no {section} detail page")
    return next((path for path in candidates if path.name.lower() != "index.html"), candidates[0])


def build_plan(root: Path) -> dict[str, Any]:
    root = Path(root).resolve()
    if not root.is_dir():
        raise AuditError("Static root is unavailable")
    samples: list[dict[str, Any]] = []
    zsxq_sources = [
        path
        for path in sorted(root.joinpath("blog").rglob("*.html"))
        if path.is_file() and not path.is_symlink() and b"zsxq.img" in path.read_bytes().lower()
    ]
    zsxq_relative = zsxq_sources[0].relative_to(root) if zsxq_sources else None

    for locale, direction in LOCALES.items():
        locale_root = root / locale
        if not locale_root.is_dir() or locale_root.is_symlink():
            raise AuditError(f"Locale root is missing: {locale}")
        selected = [
            ("home", require_page(locale_root / "index.html", f"{locale} home", root=locale_root), False),
            ("blog", require_page(locale_root / "blog" / "index.html", f"{locale} blog", root=locale_root), True),
            ("blog-detail", first_detail(locale_root, "blog"), True),
            (
                "reports",
                require_page(
                    locale_root / "reports" / "index.html",
                    f"{locale} reports",
                    root=locale_root,
                ),
                False,
            ),
            ("report-detail", first_detail(locale_root, "reports"), False),
            ("charts", require_page(locale_root / "charts.html", f"{locale} charts", root=locale_root), False),
        ]
        if zsxq_relative is not None:
            localized_zsxq = require_page(
                locale_root / zsxq_relative,
                f"{locale} zsxq-clean blog",
                root=locale_root,
            )
            selected.append(("blog-zsxq-clean", localized_zsxq, True))
        seen: set[str] = set()
        for kind, page, forbid_zsxq in selected:
            route = route_for_html(locale, locale_root, page)
            if route in seen:
                continue
            seen.add(route)
            samples.append({
                "kind": kind,
                "locale": locale,
                "direction": direction,
                "path": route,
                "forbid_zsxq": forbid_zsxq,
            })

    if len(samples) < 18:
        raise AuditError("Shadow review plan is incomplete")
    return {"schema_version": 1, "samples": samples}


def expected_sample_path(locale: str, kind: str, path: str) -> bool:
    exact = {
        "home": f"/{locale}/",
        "blog": f"/{locale}/blog/",
        "reports": f"/{locale}/reports/",
        "charts": f"/{locale}/charts.html",
    }
    if kind in exact:
        return path == exact[kind]
    if kind in {"blog-detail", "blog-zsxq-clean"}:
        return path.startswith(f"/{locale}/blog/") and path != f"/{locale}/blog/"
    if kind == "report-detail":
        return path.startswith(f"/{locale}/reports/") and path != f"/{locale}/reports/"
    return False


def validate_samples(plan: dict[str, Any]) -> list[dict[str, Any]]:
    samples = plan.get("samples")
    if (
        plan.get("schema_version") != 1
        or not isinstance(samples, list)
        or not (len(LOCALES) * len(REQUIRED_SAMPLE_KINDS) <= len(samples) <= len(LOCALES) * 7)
    ):
        raise AuditError("Shadow review plan is invalid")
    required_seen: set[tuple[str, str]] = set()
    optional_seen: set[tuple[str, str]] = set()
    paths_seen: set[str] = set()
    for sample in samples:
        if not isinstance(sample, dict):
            raise AuditError("Shadow sample is invalid")
        locale = sample.get("locale")
        direction = sample.get("direction")
        kind = sample.get("kind")
        path = sample.get("path")
        forbid_zsxq = sample.get("forbid_zsxq")
        if not all(isinstance(value, str) for value in (locale, direction, kind, path)):
            raise AuditError("Shadow sample is invalid")
        validate_preview_path(path, allow_query=False)
        expected_forbid_zsxq = kind.startswith("blog")
        if (
            LOCALES.get(locale) != direction
            or kind not in set(REQUIRED_SAMPLE_KINDS) | OPTIONAL_SAMPLE_KINDS
            or not expected_sample_path(locale, kind, path)
            or forbid_zsxq is not expected_forbid_zsxq
            or path in paths_seen
        ):
            raise AuditError(f"Shadow sample identity is invalid: {path}")
        identity = (locale, kind)
        seen = optional_seen if kind in OPTIONAL_SAMPLE_KINDS else required_seen
        if identity in seen:
            raise AuditError(f"Shadow sample identity is duplicated: {path}")
        seen.add(identity)
        paths_seen.add(path)
    expected = {(locale, kind) for locale in LOCALES for kind in REQUIRED_SAMPLE_KINDS}
    if required_seen != expected:
        raise AuditError("Shadow review plan is incomplete")
    return samples


def write_json(path: Path, payload: dict[str, Any]) -> None:
    target = safe_output(path)
    target.write_text(
        json.dumps(payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def fetch(opener: Any, base_url: str, relative: str, *, attempts: int = 6) -> tuple[bytes, Any, float]:
    validate_preview_path(relative, allow_query=True)
    base = validate_workers_dev_origin(base_url)
    target = urljoin(base + "/", relative)
    target_url = urlsplit(target)
    base_url_parts = urlsplit(base)
    if (
        target_url.scheme != base_url_parts.scheme
        or target_url.hostname != base_url_parts.hostname
        or target_url.port != base_url_parts.port
        or target_url.username is not None
        or target_url.password is not None
    ):
        raise AuditError(f"Unsafe preview path: {relative}")
    if not isinstance(attempts, int) or isinstance(attempts, bool) or not 1 <= attempts <= 10:
        raise AuditError("Preview retry count is invalid")
    last_error: BaseException | None = None
    for attempt in range(1, attempts + 1):
        started = time.monotonic()
        try:
            response = opener.open(
                Request(target, headers={"Cache-Control": "no-cache", "User-Agent": "Portal-Shadow-Audit/1.0"}),
                timeout=30,
            )
            body = response.read(MAX_RESPONSE_BYTES + 1)
            elapsed = time.monotonic() - started
            if response.status != 200:
                raise AuditError(f"Preview returned HTTP {response.status}: {relative}")
            if len(body) > MAX_RESPONSE_BYTES:
                raise AuditError(f"Preview response is oversized: {relative}")
            return body, response.headers, elapsed
        except (HTTPError, URLError, TimeoutError, AuditError) as error:
            last_error = error
            if attempt < attempts:
                time.sleep(2)
    raise AuditError(f"Preview fetch failed after retries: {relative}") from last_error


def require_shadow_header(headers: Any, path: str) -> None:
    value = str(headers.get("X-Robots-Tag") or "").strip().lower()
    if value != SHADOW_ROBOTS_HEADER:
        raise AuditError(f"Preview indexing header is missing: {path}")


def json_object(body: bytes, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is invalid JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} is invalid")
    return payload


def xml_document(body: bytes, label: str) -> ET.Element:
    try:
        return ET.fromstring(body)
    except ET.ParseError as error:
        raise AuditError(f"{label} is invalid XML") from error


def xml_local_name(tag: Any) -> str:
    return str(tag).rsplit("}", 1)[-1].lower()


def require_public_locale_url(value: str, locale: str, label: str, public_origin: str) -> None:
    try:
        parsed = urlsplit(value.strip())
        port = parsed.port
    except ValueError as error:
        raise AuditError(f"{label} has an invalid locale URL") from error
    if (
        parsed.scheme != "https"
        or parsed.hostname != urlsplit(public_origin).hostname
        or parsed.username is not None
        or parsed.password is not None
        or port is not None
        or not parsed.path.startswith(f"/{locale}/")
        or parsed.query
        or parsed.fragment
    ):
        raise AuditError(f"{label} has an invalid locale URL")


def validate_locale_sitemap(body: bytes, locale: str, public_origin: str) -> None:
    root = xml_document(body, f"Shadow {locale} sitemap")
    if xml_local_name(root.tag) != "urlset":
        raise AuditError(f"Shadow {locale} sitemap has the wrong document type")
    locations = [
        str(element.text or "").strip()
        for element in root.iter()
        if xml_local_name(element.tag) == "loc"
    ]
    if not locations:
        raise AuditError(f"Shadow {locale} sitemap is empty")
    for value in locations:
        require_public_locale_url(value, locale, f"Shadow {locale} sitemap", public_origin)


def validate_locale_feed(body: bytes, locale: str, public_origin: str) -> None:
    root = xml_document(body, f"Shadow {locale} feed")
    if xml_local_name(root.tag) != "rss":
        raise AuditError(f"Shadow {locale} feed has the wrong document type")
    languages = [
        str(element.text or "").strip().lower()
        for element in root.iter()
        if xml_local_name(element.tag) == "language"
    ]
    if languages != [locale]:
        raise AuditError(f"Shadow {locale} feed has the wrong language")
    links = [
        str(element.text or "").strip()
        for element in root.iter()
        if xml_local_name(element.tag) in {"link", "guid"} and str(element.text or "").strip()
    ]
    if not links:
        raise AuditError(f"Shadow {locale} feed has no links")
    for value in links:
        require_public_locale_url(value, locale, f"Shadow {locale} feed", public_origin)


def validate_manifest_row(row: Any, locale: str, label: str) -> tuple[str, int, str]:
    if not isinstance(row, dict):
        raise AuditError(f"Shadow multilingual manifest has an invalid {label} row")
    relative = row.get("path")
    byte_size = row.get("byte_size")
    sha256 = row.get("sha256")
    if (
        not isinstance(relative, str)
        or not relative
        or relative.startswith("/")
        or not isinstance(byte_size, int)
        or isinstance(byte_size, bool)
        or byte_size <= 0
        or not isinstance(sha256, str)
        or SHA256_RE.fullmatch(sha256) is None
    ):
        raise AuditError(f"Shadow multilingual manifest has invalid {label} metadata")
    path = "/" + relative
    validate_preview_path(path, allow_query=False)
    if not (
        relative.startswith(f"data/i18n/{locale}/")
        or relative.startswith(f"{locale}/data/")
    ):
        raise AuditError(f"Shadow multilingual manifest crosses locale boundaries: {relative}")
    return path, byte_size, sha256


def manifest_files(manifest: dict[str, Any]) -> dict[str, tuple[str, int, str]]:
    locales = manifest.get("locales")
    coverage = manifest.get("coverage")
    if (
        manifest.get("schema_version") != 1
        or manifest.get("quality_gate_version") != 2
        or not isinstance(locales, list)
        or len(locales) != len(LOCALES)
        or set(locales) != set(LOCALES)
        or not isinstance(coverage, dict)
        or set(coverage) != set(LOCALES)
        or any(
            not isinstance(coverage.get(locale), (int, float))
            or isinstance(coverage.get(locale), bool)
            or float(coverage[locale]) != 1.0
            for locale in LOCALES
        )
    ):
        raise AuditError("Shadow multilingual manifest is incomplete")

    rows: dict[str, tuple[str, int, str]] = {}

    def add_row(row: Any, locale: str, label: str) -> None:
        path, byte_size, sha256 = validate_manifest_row(row, locale, label)
        if path in rows:
            raise AuditError(f"Shadow multilingual manifest repeats a path: {path}")
        rows[path] = (locale, byte_size, sha256)

    for group_name in MANIFEST_MAP_GROUPS:
        group = manifest.get(group_name)
        if not isinstance(group, dict) or set(group) != set(LOCALES):
            raise AuditError(f"Shadow multilingual manifest is missing {group_name}")
        for locale in LOCALES:
            locale_rows = group.get(locale)
            if not isinstance(locale_rows, dict):
                raise AuditError(f"Shadow multilingual manifest is missing {group_name}.{locale}")
            if group_name == "catalog_overlays" and not locale_rows:
                raise AuditError(f"Shadow multilingual manifest is missing {group_name}.{locale}")
            for row_name, row in locale_rows.items():
                add_row(row, locale, f"{group_name}.{locale}.{row_name}")

    for group_name in MANIFEST_ROW_GROUPS:
        group = manifest.get(group_name)
        if not isinstance(group, dict) or set(group) != set(LOCALES):
            raise AuditError(f"Shadow multilingual manifest is missing {group_name}")
        for locale in LOCALES:
            add_row(group.get(locale), locale, f"{group_name}.{locale}")

    required_paths = manifest.get("required_paths")
    expected = sorted(path.removeprefix("/") for path in rows)
    if (
        not isinstance(required_paths, list)
        or not required_paths
        or len(required_paths) > MAX_MANIFEST_PATHS
        or required_paths != expected
    ):
        raise AuditError("Shadow multilingual manifest required_paths is invalid")
    return rows


def audit_preview(
    base_url: str,
    public_origin: str,
    samples_path: Path,
    expected_release: str,
    expected_tree: str,
) -> dict[str, Any]:
    base_url = validate_workers_dev_origin(base_url)
    public_origin = validate_public_origin(public_origin)
    if not RELEASE_RE.fullmatch(expected_release) or not TREE_RE.fullmatch(expected_tree):
        raise AuditError("Expected shadow release identity is invalid")
    plan = read_json_object(samples_path, "Shadow review plan")
    samples = validate_samples(plan)

    opener = build_opener(NoRedirect())
    rows: list[dict[str, Any]] = []
    state_body, state_headers, elapsed = fetch(opener, base_url, "/.well-known/edge-state")
    require_shadow_header(state_headers, "/.well-known/edge-state")
    state = json_object(state_body, "Shadow Edge state")
    if (
        state.get("schema_version") != 1
        or state.get("release_id") != expected_release
        or state.get("tree_sha256") != expected_tree
        or state.get("slot") not in {"a", "b"}
    ):
        raise AuditError("Shadow Edge state does not match the uploaded candidate")
    rows.append({"path": "/.well-known/edge-state", "bytes": len(state_body), "milliseconds": round(elapsed * 1000)})

    robots, robots_headers, elapsed = fetch(opener, base_url, "/robots.txt")
    require_shadow_header(robots_headers, "/robots.txt")
    if robots != SHADOW_ROBOTS:
        raise AuditError("Shadow robots.txt does not disallow the preview")
    rows.append({"path": "/robots.txt", "bytes": len(robots), "milliseconds": round(elapsed * 1000)})

    assets: set[str] = {"/assets/locale.css", "/assets/locale-runtime.js"}
    for sample in samples:
        locale = str(sample.get("locale") or "")
        direction = str(sample.get("direction") or "")
        path = str(sample.get("path") or "")
        body, headers, elapsed = fetch(opener, base_url, path)
        require_shadow_header(headers, path)
        if str(headers.get("Content-Language") or "").strip().lower() != locale:
            raise AuditError(f"Shadow locale response has the wrong Content-Language: {path}")
        try:
            text = body.decode("utf-8")
        except UnicodeDecodeError as error:
            raise AuditError(f"Shadow locale page is not UTF-8: {path}") from error
        html_match = re.search(r"<html\b([^>]*)>", text[:16_384], flags=re.I)
        if html_match is None:
            raise AuditError(f"Shadow locale page has no html element: {path}")
        attrs = {
            key.lower(): value.strip().lower()
            for key, _quote, value in re.findall(
                r"\b(lang|dir)\s*=\s*(['\"])(.*?)\2", html_match.group(1), flags=re.I
            )
        }
        if attrs.get("lang") != locale or attrs.get("dir") != direction:
            raise AuditError(f"Shadow locale direction is invalid: {path}")
        if "/assets/locale.css" not in text or "/assets/locale-runtime.js" not in text:
            raise AuditError(f"Shadow locale runtime is missing: {path}")
        if sample.get("forbid_zsxq") is True and "zsxq.img" in text.lower():
            raise AuditError(f"Localized Blog still contains zsxq.img: {path}")
        parser = AssetParser()
        parser.feed(text)
        assets.update(parser.assets)
        rows.append({
            "path": path,
            "locale": locale,
            "bytes": len(body),
            "milliseconds": round(elapsed * 1000),
        })

    manifest_body, manifest_headers, elapsed = fetch(opener, base_url, "/data/i18n/manifest.json")
    require_shadow_header(manifest_headers, "/data/i18n/manifest.json")
    manifest = json_object(manifest_body, "Shadow multilingual manifest")
    required_files = manifest_files(manifest)
    rows.append({
        "path": "/data/i18n/manifest.json",
        "bytes": len(manifest_body),
        "milliseconds": round(elapsed * 1000),
    })

    for locale in LOCALES:
        sitemap_path = f"/sitemap-{locale}.xml"
        body, headers, elapsed = fetch(opener, base_url, sitemap_path)
        require_shadow_header(headers, sitemap_path)
        if str(headers.get("Content-Language") or "").strip().lower() != locale:
            raise AuditError(f"Shadow sitemap has the wrong Content-Language: {sitemap_path}")
        validate_locale_sitemap(body, locale, public_origin)
        rows.append({
            "path": sitemap_path,
            "locale": locale,
            "bytes": len(body),
            "milliseconds": round(elapsed * 1000),
        })

        feed_path = f"/{locale}/feed.xml"
        body, headers, elapsed = fetch(opener, base_url, feed_path)
        require_shadow_header(headers, feed_path)
        if str(headers.get("Content-Language") or "").strip().lower() != locale:
            raise AuditError(f"Shadow feed has the wrong Content-Language: {feed_path}")
        validate_locale_feed(body, locale, public_origin)
        rows.append({"path": feed_path, "locale": locale, "bytes": len(body), "milliseconds": round(elapsed * 1000)})

    for asset in sorted(assets):
        body, headers, elapsed = fetch(opener, base_url, asset)
        require_shadow_header(headers, asset)
        if not body:
            raise AuditError(f"Shadow locale asset is empty: {asset}")
        rows.append({"path": asset, "bytes": len(body), "milliseconds": round(elapsed * 1000)})

    for path, (locale, expected_bytes, expected_sha256) in sorted(required_files.items()):
        body, headers, elapsed = fetch(opener, base_url, path)
        require_shadow_header(headers, path)
        if str(headers.get("Content-Language") or "").strip().lower() != locale:
            raise AuditError(f"Shadow locale data has the wrong Content-Language: {path}")
        if len(body) != expected_bytes or hashlib.sha256(body).hexdigest() != expected_sha256:
            raise AuditError(f"Shadow locale data does not match its manifest: {path}")
        rows.append({"path": path, "locale": locale, "bytes": len(body), "milliseconds": round(elapsed * 1000)})

    return {
        "schema_version": 1,
        "base_url": base_url,
        "release_id": expected_release,
        "tree_sha256": expected_tree,
        "sample_count": len(samples),
        "asset_count": len(assets),
        "checks": rows,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    plan = subparsers.add_parser("plan")
    plan.add_argument("--root", type=Path, required=True)
    plan.add_argument("--output", type=Path, required=True)
    audit = subparsers.add_parser("audit")
    audit.add_argument("--base-url", required=True)
    audit.add_argument("--public-origin", required=True)
    audit.add_argument("--samples", type=Path, required=True)
    audit.add_argument("--expected-release", required=True)
    audit.add_argument("--expected-tree", required=True)
    audit.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "plan":
        payload = build_plan(args.root)
    else:
        payload = audit_preview(
            args.base_url,
            args.public_origin,
            args.samples,
            args.expected_release,
            args.expected_tree,
        )
    write_json(args.output, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
