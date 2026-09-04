#!/usr/bin/env python3
"""Fail-closed parity gate for the Simplified-Chinese static release.

``snapshot`` records the Chinese candidate before locale generation. ``verify``
then proves that locale generation changed only the explicitly controlled
discovery markup and locale discovery files.  The locale trees themselves are
intentionally outside this gate and have separate release validation.
"""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit
import xml.etree.ElementTree as ET


SCHEMA_VERSION = 1
SNAPSHOT_KIND = "portal-chinese-parity-snapshot"
VERIFY_KIND = "portal-chinese-parity-verification"
DEFAULT_SITE_ORIGIN = "https://portal.example.invalid"
LOCALES = ("ko", "ja", "ar")
LOCALE_DIRS = frozenset(LOCALES)
LOCALE_ASSET_PATHS = frozenset(("assets/locale.css", "assets/locale-runtime.js"))
LOCALE_SITEMAPS = frozenset(f"sitemap-{locale}.xml" for locale in LOCALES)
REQUIRED_PROTECTED_PATHS = frozenset(
    (
        "robots.txt",
        "feed.xml",
        "llms.txt",
        "llms-full.txt",
        "sitemap-baidu.xml",
        "sitemap-sogou.xml",
        "sitemap-pages.xml",
        "assets/styles.css",
    )
)

HEAD_RE = re.compile(rb"<head\b[^>]*>.*?</head\s*>", flags=re.I | re.S)
BODY_RE = re.compile(rb"<body\b", flags=re.I)
BOOTSTRAP_RE = re.compile(
    rb"<script\b(?=[^>]*\bdata-kc-locale-bootstrap\b)[^>]*>.*?</script\s*>",
    flags=re.I | re.S,
)
LOCALE_HREFLANG_RE = re.compile(
    rb"<link\b"
    rb"(?=[^>]*\brel\s*=\s*([\"'])[^\"']*\balternate\b[^\"']*\1)"
    rb"(?=[^>]*\bhreflang\s*=\s*([\"'])(?:ko|ja|ar)\2)"
    rb"[^>]*>",
    flags=re.I,
)
INTERTAG_SPACE_RE = re.compile(rb"(?<=>)[\t\r\n ]+(?=<)")
SITEMAP_BLOCK_RE = re.compile(
    rb"<(?:[A-Za-z_][\w.-]*:)?sitemap\b[^>]*>.*?</(?:[A-Za-z_][\w.-]*:)?sitemap\s*>",
    flags=re.I | re.S,
)
SITEMAP_LOC_RE = re.compile(
    rb"<(?:[A-Za-z_][\w.-]*:)?loc\b[^>]*>\s*([^<]+?)\s*</(?:[A-Za-z_][\w.-]*:)?loc\s*>",
    flags=re.I | re.S,
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

# This is deliberately the exact build contract, apart from the shared asset
# version. A looser substring check could accidentally move asset creation
# ahead of the Simplified-Chinese early return.
BOOTSTRAP_BODY_RE = re.compile(
    r'^\(function\(\)\{'
    r'var n=navigator,l=String\(n\.language\|\|n\.languages&&n\.languages\[0\]\|\|""\)\.toLowerCase\(\);'
    r'if\(l==="zh"\|\|/\^zh-\(\?:cn\|sg\|hans\)\(\?:-\|\$\)/\.test\(l\)\)return;'
    r'var h=document\.head,c=document\.createElement\("link"\),s=document\.createElement\("script"\);'
    r'c\.rel="stylesheet";c\.href="/assets/locale\.css\?v=([0-9a-f]{12})";'
    r's\.src="/assets/locale-runtime\.js\?v=([0-9a-f]{12})";s\.defer=true;'
    r'h\.appendChild\(c\);h\.appendChild\(s\)\}\)\(\)$'
)


class ParityError(RuntimeError):
    """A Chinese parity invariant was not satisfied."""


class _HeadLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.alternates: list[tuple[str, str]] = []
        self.canonicals: list[str] = []
        self.direct_locale_assets: list[str] = []
        self.bootstrap_bodies: list[str] = []
        self._bootstrap_depth = 0
        self._bootstrap_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {str(key).lower(): str(value or "") for key, value in attrs}
        lowered = tag.lower()
        if lowered == "link":
            rel = {token.lower() for token in values.get("rel", "").split()}
            href = values.get("href", "").strip()
            hreflang = values.get("hreflang", "").strip()
            if "alternate" in rel and hreflang:
                self.alternates.append((hreflang, href))
            if "canonical" in rel and href:
                self.canonicals.append(href)
            if _is_direct_locale_asset(href, "locale.css"):
                self.direct_locale_assets.append(href)
        elif lowered == "script":
            source = values.get("src", "").strip()
            if source and _is_direct_locale_asset(source, "locale-runtime.js"):
                self.direct_locale_assets.append(source)
            if "data-kc-locale-bootstrap" in values:
                self._bootstrap_depth += 1
                self._bootstrap_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._bootstrap_depth:
            self.bootstrap_bodies.append("".join(self._bootstrap_parts))
            self._bootstrap_depth -= 1
            self._bootstrap_parts = []

    def handle_data(self, data: str) -> None:
        if self._bootstrap_depth:
            self._bootstrap_parts.append(data)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _with_digest(value: dict[str, Any]) -> dict[str, Any]:
    result = dict(value)
    result["digest"] = _sha256(_json_bytes(result))
    return result


def _verify_digest(value: dict[str, Any], *, label: str) -> None:
    actual = value.get("digest")
    if not isinstance(actual, str) or not SHA256_RE.fullmatch(actual):
        raise ParityError(f"{label} has no valid digest")
    unsigned = dict(value)
    unsigned.pop("digest", None)
    expected = _sha256(_json_bytes(unsigned))
    if actual != expected:
        raise ParityError(f"{label} digest does not match its content")


def _normalize_origin(value: str) -> str:
    parsed = urlsplit(str(value or "").strip())
    if (
        parsed.scheme.lower() != "https"
        or not parsed.netloc
        or parsed.username is not None
        or parsed.password is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise ParityError("site origin must be an HTTPS origin without credentials, path, query, or fragment")
    return urlunsplit(("https", parsed.netloc.lower(), "", "", ""))


def _safe_root(value: str | Path) -> Path:
    root = Path(value).expanduser().resolve(strict=True)
    if not root.is_dir() or root == Path(root.anchor):
        raise ParityError(f"unsafe or invalid site root: {root}")
    return root


def _safe_input_file(value: str | Path, *, label: str) -> Path:
    path = Path(value).expanduser()
    if path.is_symlink():
        raise ParityError(f"{label} must not be a symlink")
    path = path.resolve(strict=True)
    if not path.is_file():
        raise ParityError(f"{label} is not a regular file: {path}")
    return path


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _safe_output(value: str | Path, *, root: Path) -> Path:
    path = Path(value).expanduser()
    if path.exists() and path.is_symlink():
        raise ParityError("output must not be a symlink")
    parent = path.parent.resolve(strict=True)
    resolved = parent / path.name
    if _is_within(resolved, root):
        raise ParityError("output must be outside the static site root")
    return resolved


def _valid_relative(value: str) -> str:
    if not value or "\\" in value or "\x00" in value or value.startswith("/"):
        raise ParityError(f"unsafe manifest path: {value!r}")
    path = PurePosixPath(value)
    if any(part in {"", ".", ".."} for part in path.parts) or path.as_posix() != value:
        raise ParityError(f"unsafe manifest path: {value!r}")
    return value


def _excluded(relative: str) -> bool:
    path = PurePosixPath(_valid_relative(relative))
    if path.parts[0] in LOCALE_DIRS:
        return True
    if len(path.parts) >= 2 and path.parts[:2] == ("data", "i18n"):
        return True
    return relative in LOCALE_ASSET_PATHS or relative in LOCALE_SITEMAPS


def _inventory(root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ParityError(f"static site contains a symlink: {path.relative_to(root)}")
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if not _excluded(relative):
            files[relative] = path
    if not files:
        raise ParityError("static site inventory is empty")
    return files


def _read(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as error:
        raise ParityError(f"cannot read {path}: {error}") from error


def _decode_html(data: bytes, *, relative: str) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ParityError(f"HTML is not valid UTF-8: {relative}") from error


def _head(data: bytes, *, relative: str) -> bytes:
    matches = list(HEAD_RE.finditer(data))
    if len(matches) != 1:
        raise ParityError(f"HTML must contain exactly one head element: {relative}")
    return matches[0].group(0)


def _body(data: bytes, *, relative: str) -> bytes:
    matches = list(BODY_RE.finditer(data))
    if len(matches) != 1:
        raise ParityError(f"HTML must contain exactly one body element: {relative}")
    return data[matches[0].start():]


def _neutral_head(data: bytes, *, relative: str) -> bytes:
    value = _head(data, relative=relative)
    value = BOOTSTRAP_RE.sub(b"", value)
    value = LOCALE_HREFLANG_RE.sub(b"", value)
    return INTERTAG_SPACE_RE.sub(b"", value).strip()


def _head_links(data: bytes, *, relative: str) -> _HeadLinks:
    parser = _HeadLinks()
    source = _decode_html(_head(data, relative=relative), relative=relative)
    try:
        parser.feed(source)
        parser.close()
    except Exception as error:
        raise ParityError(f"cannot parse HTML head: {relative}: {error}") from error
    return parser


def _is_direct_locale_asset(value: str, filename: str) -> bool:
    if not value:
        return False
    parsed = urlsplit(value)
    return parsed.path == f"/assets/{filename}"


def _alternate_map(parser: _HeadLinks, *, relative: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw_language, href in parser.alternates:
        language = raw_language.strip()
        identity = language.lower()
        if not language or not href:
            raise ParityError(f"empty hreflang or href: {relative}")
        if identity in result:
            raise ParityError(f"duplicate hreflang {language!r}: {relative}")
        result[identity] = href
    return result


def _localized_url(root_url: str, locale: str, *, origin: str, relative: str) -> str:
    parsed = urlsplit(root_url)
    expected_origin = urlsplit(origin)
    if (
        parsed.scheme.lower() != "https"
        or parsed.netloc.lower() != expected_origin.netloc.lower()
        or parsed.fragment
        or not parsed.path.startswith("/")
    ):
        raise ParityError(f"invalid zh-Hans hreflang URL: {relative}: {root_url!r}")
    path = parsed.path or "/"
    if re.match(r"^/(?:ko|ja|ar)(?:/|$)", path, flags=re.I):
        raise ParityError(f"zh-Hans hreflang already has a locale prefix: {relative}")
    localized_path = f"/{locale}/" if path == "/" else f"/{locale}{path}"
    return urlunsplit(("https", expected_origin.netloc, localized_path, parsed.query, ""))


def _validate_snapshot_head(data: bytes, *, relative: str) -> dict[str, Any]:
    parser = _head_links(data, relative=relative)
    if parser.bootstrap_bodies:
        raise ParityError(f"pre-locale HTML already contains locale bootstrap: {relative}")
    if parser.direct_locale_assets:
        raise ParityError(f"pre-locale HTML directly loads locale assets: {relative}")
    alternates = _alternate_map(parser, relative=relative)
    if any(locale in alternates for locale in LOCALES):
        raise ParityError(f"pre-locale HTML already contains locale hreflang links: {relative}")
    if len(parser.canonicals) > 1:
        raise ParityError(f"HTML contains duplicate canonical links: {relative}")
    return {
        "alternates": alternates,
        "canonical": parser.canonicals[0] if parser.canonicals else "",
    }


def _validate_final_head(
    data: bytes,
    *,
    relative: str,
    baseline: dict[str, Any],
    origin: str,
) -> bool:
    parser = _head_links(data, relative=relative)
    if parser.direct_locale_assets:
        raise ParityError(
            f"Chinese HTML statically loads locale assets instead of using the guarded bootstrap: {relative}"
        )
    if len(parser.bootstrap_bodies) != 1:
        raise ParityError(f"Chinese HTML must contain exactly one locale bootstrap: {relative}")
    match = BOOTSTRAP_BODY_RE.fullmatch(parser.bootstrap_bodies[0])
    if match is None or match.group(1) != match.group(2):
        raise ParityError(f"Chinese HTML locale bootstrap guard is not the approved contract: {relative}")

    final = _alternate_map(parser, relative=relative)
    before = baseline.get("alternates")
    if not isinstance(before, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in before.items()):
        raise ParityError(f"snapshot HTML alternate metadata is invalid: {relative}")
    additions_present = {locale for locale in LOCALES if locale in final}
    has_cluster_baseline = "zh-hans" in before and "x-default" in before

    if has_cluster_baseline:
        if additions_present != set(LOCALES):
            raise ParityError(f"locale hreflang cluster is incomplete: {relative}")
        if set(final) != set(before) | set(LOCALES):
            raise ParityError(f"locale hreflang language set changed unexpectedly: {relative}")
        for language, href in before.items():
            if final.get(language) != href:
                raise ParityError(f"protected hreflang {language!r} changed: {relative}")
        zh_url = before["zh-hans"]
        if before["x-default"] != zh_url:
            raise ParityError(f"x-default must remain aligned with zh-Hans: {relative}")
        if baseline.get("canonical") != zh_url:
            raise ParityError(f"zh-Hans hreflang must remain aligned with canonical: {relative}")
        for locale in LOCALES:
            expected = _localized_url(zh_url, locale, origin=origin, relative=relative)
            if final[locale] != expected:
                raise ParityError(f"incorrect {locale} hreflang URL: {relative}")
        return True

    if additions_present:
        raise ParityError(f"locale hreflang was added to a page without a protected zh-Hans cluster: {relative}")
    if final != before:
        raise ParityError(f"existing hreflang metadata changed: {relative}")
    return False


def _protected_paths(paths: Iterable[str]) -> list[str]:
    result: list[str] = []
    for relative in paths:
        name = PurePosixPath(relative).name
        if relative in REQUIRED_PROTECTED_PATHS:
            result.append(relative)
        elif PurePosixPath(relative).parent == PurePosixPath(".") and (
            (name.startswith("llms") and name.endswith(".txt"))
            or (name.startswith("sitemap-reports-") and name.endswith(".xml"))
            or (name.startswith("sitemap-blog-") and name.endswith(".xml"))
        ):
            result.append(relative)
    return sorted(set(result))


def _robot_locale_lines(data: bytes, *, relative: str) -> list[tuple[str, str]]:
    try:
        source = data.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ParityError(f"robots.txt is not valid UTF-8: {relative}") from error
    found: list[tuple[str, str]] = []
    for line in source.splitlines():
        match = re.fullmatch(r"\s*Sitemap:\s*(\S+)\s*", line, flags=re.I)
        if not match:
            continue
        value = match.group(1)
        parsed = urlsplit(value)
        locale_match = re.fullmatch(r"/sitemap-(ko|ja|ar)\.xml", parsed.path, flags=re.I)
        if locale_match:
            found.append((locale_match.group(1).lower(), line))
    return found


def _neutral_robots(data: bytes, *, relative: str) -> bytes:
    controlled = {line for _locale, line in _robot_locale_lines(data, relative=relative)}
    if not controlled:
        return data
    pieces: list[str] = []
    source = data.decode("utf-8")
    for line in source.splitlines(keepends=True):
        text = line.rstrip("\r\n")
        if text not in controlled:
            pieces.append(line)
    return "".join(pieces).encode("utf-8")


def _validate_final_robots(data: bytes, *, origin: str) -> None:
    found = _robot_locale_lines(data, relative="robots.txt")
    if len(found) != len(LOCALES):
        raise ParityError("robots.txt must contain exactly three locale sitemap declarations")
    counts: dict[str, int] = {}
    for locale, line in found:
        counts[locale] = counts.get(locale, 0) + 1
        expected = f"Sitemap: {origin}/sitemap-{locale}.xml"
        if line != expected:
            raise ParityError(f"robots.txt has a non-canonical locale sitemap declaration: {line!r}")
    if counts != {locale: 1 for locale in LOCALES}:
        raise ParityError("robots.txt locale sitemap declarations are incomplete or duplicated")


def _sitemap_locale_blocks(data: bytes, *, relative: str) -> list[tuple[str, str]]:
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise ParityError(f"invalid sitemap index XML: {relative}: {error}") from error
    if root.tag.rsplit("}", 1)[-1].lower() != "sitemapindex":
        raise ParityError(f"sitemap.xml is not a sitemap index: {relative}")
    found: list[tuple[str, str]] = []
    for child in list(root):
        if child.tag.rsplit("}", 1)[-1].lower() != "sitemap":
            continue
        locations = [
            str(node.text or "").strip()
            for node in list(child)
            if node.tag.rsplit("}", 1)[-1].lower() == "loc"
        ]
        if len(locations) != 1:
            continue
        value = locations[0]
        parsed = urlsplit(value)
        match = re.fullmatch(r"/sitemap-(ko|ja|ar)\.xml", parsed.path, flags=re.I)
        if match:
            found.append((match.group(1).lower(), value))
    return found


def _neutral_sitemap(data: bytes, *, relative: str) -> bytes:
    # Validate the whole document first, then remove precisely those sitemap
    # blocks whose loc path names one of the three controlled locale files.
    _sitemap_locale_blocks(data, relative=relative)

    def replace(match: re.Match[bytes]) -> bytes:
        block = match.group(0)
        locations = SITEMAP_LOC_RE.findall(block)
        if len(locations) != 1:
            return block
        try:
            location = locations[0].decode("utf-8").strip()
        except UnicodeDecodeError:
            return block
        parsed = urlsplit(location)
        if re.fullmatch(r"/sitemap-(?:ko|ja|ar)\.xml", parsed.path, flags=re.I):
            return b""
        return block

    return INTERTAG_SPACE_RE.sub(b"", SITEMAP_BLOCK_RE.sub(replace, data)).strip()


def _validate_final_sitemap(data: bytes, *, origin: str) -> None:
    found = _sitemap_locale_blocks(data, relative="sitemap.xml")
    if len(found) != len(LOCALES):
        raise ParityError("sitemap.xml must contain exactly three locale sitemap entries")
    counts: dict[str, int] = {}
    for locale, value in found:
        counts[locale] = counts.get(locale, 0) + 1
        if value != f"{origin}/sitemap-{locale}.xml":
            raise ParityError(f"sitemap.xml has an incorrect {locale} locale sitemap URL")
    if counts != {locale: 1 for locale in LOCALES}:
        raise ParityError("sitemap.xml locale entries are incomplete or duplicated")


def _descriptor(data: bytes) -> dict[str, Any]:
    return {"size": len(data), "sha256": _sha256(data)}


def _load_json(path: Path, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ParityError(f"cannot read {label}: {error}") from error
    if not isinstance(value, dict):
        raise ParityError(f"{label} must be a JSON object")
    return value


def _validate_active_manifest(
    manifest_path: Path,
    *,
    files: dict[str, Path],
    descriptors: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    manifest = _load_json(manifest_path, label="active static manifest")
    rows = manifest.get("files")
    if not isinstance(rows, dict):
        raise ParityError("active static manifest has no files object")
    # The candidate site builder may legitimately rotate query hashes inside
    # HTML before locale generation.  Active-slot comparison therefore covers
    # the stable Chinese discovery/CSS contract only; the much stronger
    # pre/post-locale body + neutralized-head gate below covers every HTML file.
    checked_paths = set(_protected_paths(files)) | {"sitemap.xml"}
    active: dict[str, dict[str, Any]] = {}
    for raw_relative, raw_descriptor in rows.items():
        if not isinstance(raw_relative, str):
            raise ParityError("active static manifest contains a non-string path")
        relative = _valid_relative(raw_relative)
        if _excluded(relative):
            continue
        if relative not in checked_paths:
            continue
        if not isinstance(raw_descriptor, dict):
            raise ParityError(f"active manifest descriptor is invalid: {relative}")
        size = raw_descriptor.get("size")
        sha256 = raw_descriptor.get("sha256")
        if not isinstance(size, int) or isinstance(size, bool) or size < 0:
            raise ParityError(f"active manifest size is invalid: {relative}")
        if not isinstance(sha256, str) or not SHA256_RE.fullmatch(sha256):
            raise ParityError(f"active manifest SHA-256 is invalid: {relative}")
        active[relative] = {"size": size, "sha256": sha256}
    if set(active) != checked_paths:
        missing = sorted(checked_paths - set(active))[:5]
        extra = sorted(set(active) - checked_paths)[:5]
        raise ParityError(f"active manifest protected path set differs: missing={missing} extra={extra}")
    for relative in sorted(checked_paths):
        expected = descriptors[relative]
        if active[relative] != {"size": expected["size"], "sha256": expected["sha256"]}:
            raise ParityError(f"pre-locale candidate differs from active manifest: {relative}")
    return {
        "checked": True,
        "file_count": len(active),
        "manifest_sha256": _sha256(_read(manifest_path)),
        "scope": "protected-discovery-and-styles",
        "skipped_html_reason": (
            "HTML can contain candidate asset query hashes; every Chinese HTML body and "
            "neutralized head is instead enforced by the pre/post locale gate"
        ),
    }


def create_snapshot(
    *,
    root: str | Path,
    site_origin: str = DEFAULT_SITE_ORIGIN,
    active_manifest: str | Path | None = None,
) -> dict[str, Any]:
    site = _normalize_origin(site_origin)
    site_root = _safe_root(root)
    inventory = _inventory(site_root)
    missing = sorted(REQUIRED_PROTECTED_PATHS - set(inventory))
    if missing:
        raise ParityError(f"required protected Chinese files are missing: {missing}")
    if "sitemap.xml" not in inventory:
        raise ParityError("required controlled file is missing: sitemap.xml")

    files: dict[str, dict[str, Any]] = {}
    html_count = 0
    for relative, path in inventory.items():
        data = _read(path)
        row = _descriptor(data)
        if relative.endswith(".html"):
            html_count += 1
            metadata = _validate_snapshot_head(data, relative=relative)
            row.update(
                {
                    "body_sha256": _sha256(_body(data, relative=relative)),
                    "head_neutralized_sha256": _sha256(_neutral_head(data, relative=relative)),
                    "alternates": metadata["alternates"],
                    "canonical": metadata["canonical"],
                }
            )
        files[relative] = row
    if html_count == 0:
        raise ParityError("Chinese site contains no HTML files")

    robots = _read(inventory["robots.txt"])
    if _robot_locale_lines(robots, relative="robots.txt"):
        raise ParityError("pre-locale robots.txt already declares locale sitemaps")
    sitemap = _read(inventory["sitemap.xml"])
    if _sitemap_locale_blocks(sitemap, relative="sitemap.xml"):
        raise ParityError("pre-locale sitemap.xml already contains locale sitemap entries")

    protected = {
        relative: dict(files[relative])
        for relative in _protected_paths(inventory)
    }
    controlled = {
        "robots.txt": {
            **_descriptor(robots),
            "neutral_sha256": _sha256(_neutral_robots(robots, relative="robots.txt")),
        },
        "sitemap.xml": {
            **_descriptor(sitemap),
            "neutral_sha256": _sha256(_neutral_sitemap(sitemap, relative="sitemap.xml")),
        },
    }
    active = {
        "checked": False,
        "file_count": 0,
        "manifest_sha256": "",
        "scope": "protected-discovery-and-styles",
        "skipped_html_reason": (
            "HTML can contain candidate asset query hashes; every Chinese HTML body and "
            "neutralized head is instead enforced by the pre/post locale gate"
        ),
    }
    if active_manifest is not None:
        manifest_path = _safe_input_file(active_manifest, label="active static manifest")
        active = _validate_active_manifest(
            manifest_path,
            files=inventory,
            descriptors=files,
        )

    snapshot = {
        "schema_version": SCHEMA_VERSION,
        "kind": SNAPSHOT_KIND,
        "site_origin": site,
        "counts": {
            "files": len(files),
            "html": html_count,
            "protected": len(protected),
        },
        "paths": sorted(files),
        "files": files,
        "protected_files": protected,
        "controlled_files": controlled,
        "active_manifest": active,
    }
    return _with_digest(snapshot)


def verify_snapshot(
    *,
    root: str | Path,
    snapshot_path: str | Path,
    site_origin: str | None = None,
) -> dict[str, Any]:
    site_root = _safe_root(root)
    snapshot_file = _safe_input_file(snapshot_path, label="Chinese parity snapshot")
    snapshot = _load_json(snapshot_file, label="Chinese parity snapshot")
    if snapshot.get("schema_version") != SCHEMA_VERSION or snapshot.get("kind") != SNAPSHOT_KIND:
        raise ParityError("Chinese parity snapshot schema or kind is unsupported")
    _verify_digest(snapshot, label="Chinese parity snapshot")
    saved_origin = _normalize_origin(str(snapshot.get("site_origin") or ""))
    origin = _normalize_origin(site_origin) if site_origin is not None else saved_origin
    if origin != saved_origin:
        raise ParityError("verification site origin differs from the snapshot")

    expected_paths = snapshot.get("paths")
    expected_files = snapshot.get("files")
    protected = snapshot.get("protected_files")
    controlled = snapshot.get("controlled_files")
    if (
        not isinstance(expected_paths, list)
        or not all(isinstance(item, str) for item in expected_paths)
        or not isinstance(expected_files, dict)
        or not isinstance(protected, dict)
        or not isinstance(controlled, dict)
    ):
        raise ParityError("Chinese parity snapshot structure is invalid")
    if expected_paths != sorted(set(expected_paths)) or set(expected_paths) != set(expected_files):
        raise ParityError("Chinese parity snapshot path inventory is invalid")
    for relative in expected_paths:
        _valid_relative(relative)

    inventory = _inventory(site_root)
    if set(inventory) != set(expected_paths):
        missing = sorted(set(expected_paths) - set(inventory))[:5]
        extra = sorted(set(inventory) - set(expected_paths))[:5]
        raise ParityError(f"Chinese root path set changed: missing={missing} extra={extra}")

    cluster_pages = 0
    verification_files: dict[str, dict[str, Any]] = {}
    for relative in expected_paths:
        baseline = expected_files.get(relative)
        if not isinstance(baseline, dict):
            raise ParityError(f"snapshot descriptor is invalid: {relative}")
        data = _read(inventory[relative])
        actual = _descriptor(data)
        if relative.endswith(".html"):
            body_sha = _sha256(_body(data, relative=relative))
            head_sha = _sha256(_neutral_head(data, relative=relative))
            if body_sha != baseline.get("body_sha256"):
                raise ParityError(f"Chinese body changed: {relative}")
            if _validate_final_head(
                data,
                relative=relative,
                baseline=baseline,
                origin=origin,
            ):
                cluster_pages += 1
            if head_sha != baseline.get("head_neutralized_sha256"):
                raise ParityError(f"protected Chinese head changed: {relative}")
            actual.update({"body_sha256": body_sha, "head_neutralized_sha256": head_sha})
        elif relative == "robots.txt":
            _validate_final_robots(data, origin=origin)
            saved = controlled.get(relative)
            if not isinstance(saved, dict) or _sha256(_neutral_robots(data, relative=relative)) != saved.get("neutral_sha256"):
                raise ParityError("protected Chinese robots.txt content changed")
        elif relative == "sitemap.xml":
            _validate_final_sitemap(data, origin=origin)
            saved = controlled.get(relative)
            if not isinstance(saved, dict) or _sha256(_neutral_sitemap(data, relative=relative)) != saved.get("neutral_sha256"):
                raise ParityError("protected Chinese sitemap.xml content changed")
        elif actual != {"size": baseline.get("size"), "sha256": baseline.get("sha256")}:
            raise ParityError(f"Chinese static file changed during locale build: {relative}")
        verification_files[relative] = actual

    expected_protected = set(_protected_paths(expected_paths))
    if set(protected) != expected_protected:
        raise ParityError("snapshot protected file inventory is invalid")
    for relative in expected_protected:
        baseline = protected.get(relative)
        file_baseline = expected_files.get(relative)
        if baseline != file_baseline:
            raise ParityError(f"snapshot protected descriptor is inconsistent: {relative}")
        if relative != "robots.txt":
            data = _read(inventory[relative])
            if _descriptor(data) != {"size": baseline.get("size"), "sha256": baseline.get("sha256")}:
                raise ParityError(f"protected Chinese discovery file changed: {relative}")

    report = {
        "schema_version": SCHEMA_VERSION,
        "kind": VERIFY_KIND,
        "site_origin": origin,
        "snapshot_digest": snapshot["digest"],
        "counts": {
            "files": len(expected_paths),
            "html": sum(1 for path in expected_paths if path.endswith(".html")),
            "protected": len(expected_protected),
            "hreflang_clusters": cluster_pages,
        },
        "verified_tree_digest": _sha256(_json_bytes(verification_files)),
    }
    return _with_digest(report)


def _write_json(path: Path, value: dict[str, Any]) -> None:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    temporary_name = ""
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_name = handle.name
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    finally:
        if temporary_name:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    snapshot = subparsers.add_parser("snapshot", help="record the pre-locale Chinese static tree")
    snapshot.add_argument("--root", required=True)
    snapshot.add_argument("--output", required=True)
    snapshot.add_argument("--site-url", default=DEFAULT_SITE_ORIGIN)
    snapshot.add_argument("--active-manifest")

    verify = subparsers.add_parser("verify", help="verify Chinese parity after locale generation")
    verify.add_argument("--root", required=True)
    verify.add_argument("--snapshot", required=True)
    verify.add_argument("--output", required=True)
    verify.add_argument("--site-url")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        root = _safe_root(args.root)
        output = _safe_output(args.output, root=root)
        if args.command == "snapshot":
            result = create_snapshot(
                root=root,
                site_origin=args.site_url,
                active_manifest=args.active_manifest,
            )
        else:
            result = verify_snapshot(
                root=root,
                snapshot_path=args.snapshot,
                site_origin=args.site_url,
            )
        _write_json(output, result)
    except ParityError as error:
        raise SystemExit(f"Chinese parity gate failed: {error}") from error
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
