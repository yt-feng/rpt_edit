#!/usr/bin/env python3
"""Reject legacy public brands in a materialized website artifact."""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Sequence
from urllib.parse import unquote


REQUIRED_PUBLIC_BRAND = "KC桌面"
READ_CHUNK_SIZE = 1024 * 1024
CHUNK_OVERLAP = 256
FORBIDDEN_PUBLIC_PATHS = {"assets/contact-card.jpg"}
REQUIRED_APP_MARK_PATH = "assets/app-mark.svg"
REQUIRED_APP_MARK_LABELS = frozenset({"KC", "KC桌面"})
HTML_TAG_PATTERN = re.compile(r'''<(?:(?:"[^"]*"|'[^']*'|[^'">]))*>''')
JS_CODE_POINT_ESCAPE_PATTERN = re.compile(r"\\u\{([0-9a-fA-F]{1,6})\}")
JS_UNICODE_ESCAPE_PATTERN = re.compile(r"\\u([0-9a-fA-F]{4})")
JS_HEX_ESCAPE_PATTERN = re.compile(r"\\x([0-9a-fA-F]{2})")
CSS_HEX_ESCAPE_PATTERN = re.compile(r"\\([0-9a-fA-F]{1,6})(?:[ \t\r\n\f])?")
JS_CONCAT_GAP = r"(?:\s|/\*[\s\S]{0,512}?\*/|//[^\r\n]*(?:\r?\n|$))*"
JS_STRING_CONCAT_PATTERN = re.compile(
    r'''(?P<q1>["'])(?P<left>[^"'\\\r\n]{0,256})(?P=q1)'''
    + JS_CONCAT_GAP
    + r'''\+'''
    + JS_CONCAT_GAP
    + r'''(?P<q2>["'])(?P<right>[^"'\\\r\n]{0,256})(?P=q2)'''
)
HTML_NON_RENDERED_TAGS = frozenset({"script", "style", "template"})


@dataclass(frozen=True, order=True)
class BrandViolation:
    path: str
    marker: str


class PublicBrandError(ValueError):
    """Raised when a public artifact violates the brand contract."""


class _VisibleHTMLParser(HTMLParser):
    """Collect browser-visible HTML text while excluding non-rendered nodes."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        if tag.casefold() in HTML_NON_RENDERED_TAGS:
            self.hidden_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() in HTML_NON_RENDERED_TAGS and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)

    def visible_text_views(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(("".join(self.parts), " ".join(self.parts))))


def _compile(pattern: str) -> re.Pattern[str]:
    return re.compile(pattern, re.IGNORECASE)


# Match public names as words. Separators used by internal route keys and code
# identifiers are deliberately not interchangeable with display-name spaces.
FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("Reportify", _compile(r"(?<![a-z0-9])report[\s._-]*ify(?![a-z0-9])")),
    ("NashAI / Nash AI", _compile(r"(?<![a-z0-9])nash[\s._-]*ai(?![a-z0-9])")),
    ("MacroGate", _compile(r"(?<![a-z0-9])macro[\s._-]*gate(?![a-z0-9])")),
    ("Portal Suite", _compile(r"(?<![a-z0-9])portal[\s._-]+suite(?![a-z0-9])")),
    ("Portal Alternate", _compile(r"(?<![a-z0-9])portal[\s._-]+alternate(?![a-z0-9])")),
    ("Portal 娱乐", _compile(r"(?<![a-z0-9])portal[\s._-]*娱乐")),
    (
        " ".join(("KC", "Desk", "Notes")),
        _compile(r"(?<![a-z0-9])kc[\s._-]+desk[\s._-]+notes(?![a-z0-9])"),
    ),
    ("Support Contact", _compile(r"(?<![a-z0-9])support[\s._-]+contact(?![a-z0-9])")),
    ("Twotigers", _compile(r"(?<![a-z0-9])two[\s._-]*tigers(?![a-z0-9])")),
    ("麦府课堂 / 麦府学堂", re.compile(r"麦府(?:课堂|学堂)")),
    ("慧博", re.compile("慧博")),
    (
        "reportify.cn",
        _compile(r"(?<![a-z0-9.-])(?:[a-z0-9-]+\.)*reportify\.cn(?![a-z0-9.-])"),
    ),
    (
        "nash-ai.cn",
        _compile(r"(?<![a-z0-9.-])(?:[a-z0-9-]+\.)*nash-ai\.cn(?![a-z0-9.-])"),
    ),
    (
        "hibor.com.cn",
        _compile(r"(?<![a-z0-9.-])(?:[a-z0-9-]+\.)*hibor\.com\.cn(?![a-z0-9.-])"),
    ),
)


def normalize_public_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    return "".join(character for character in normalized if unicodedata.category(character) != "Cf")


def _valid_app_mark(source: str) -> bool:
    try:
        root = ET.fromstring(source)
    except ET.ParseError:
        return False
    root_name = str(root.tag or "").rsplit("}", 1)[-1].casefold()
    label = normalize_public_text(str(root.attrib.get("aria-label") or "")).strip()
    return root_name == "svg" and label in REQUIRED_APP_MARK_LABELS


def _code_point(match: re.Match[str]) -> str:
    value = int(match.group(1), 16)
    return chr(value) if value <= 0x10FFFF and not 0xD800 <= value <= 0xDFFF else match.group(0)


def _runtime_decode_once(value: str) -> str:
    decoded = value
    if "&" in decoded:
        decoded = html.unescape(decoded)
    if "\\" in decoded:
        decoded = JS_CODE_POINT_ESCAPE_PATTERN.sub(_code_point, decoded)
        decoded = JS_UNICODE_ESCAPE_PATTERN.sub(_code_point, decoded)
        decoded = JS_HEX_ESCAPE_PATTERN.sub(_code_point, decoded)
        decoded = CSS_HEX_ESCAPE_PATTERN.sub(_code_point, decoded)
    if "%" in decoded:
        decoded = unquote(decoded)
    if "+" in decoded:
        for _ in range(8):
            joined = JS_STRING_CONCAT_PATTERN.sub(
                lambda match: f'"{match.group("left")}{match.group("right")}"',
                decoded,
            )
            if joined == decoded:
                break
            decoded = joined
    return decoded


def _runtime_decoded_text(value: str) -> str:
    """Decode common browser-visible encodings before applying the brand rules."""
    decoded = value
    for _ in range(3):
        next_value = _runtime_decode_once(decoded)
        if next_value == decoded:
            break
        decoded = next_value
    return decoded


def _decoded_html_text_views(value: str) -> tuple[str, ...]:
    """Interleave markup parsing and decoding so encoded tags retain HTML semantics."""
    pending = [value]
    seen: set[str] = set()
    views: list[str] = []
    for _ in range(4):
        next_pending: list[str] = []
        for source in pending:
            normalized_source = normalize_public_text(source)
            if normalized_source not in seen:
                seen.add(normalized_source)
                views.append(normalized_source)
            visible_inputs = (source,)
            if "<" in source and ">" in source:
                parser = _VisibleHTMLParser()
                parser.feed(source)
                parser.close()
                visible_inputs = parser.visible_text_views()
            for visible in visible_inputs:
                normalized_visible = normalize_public_text(visible)
                if normalized_visible not in seen:
                    seen.add(normalized_visible)
                    views.append(normalized_visible)
                decoded = _runtime_decode_once(visible)
                if decoded != visible:
                    next_pending.append(decoded)
        if not next_pending:
            break
        pending = list(dict.fromkeys(next_pending))
    return tuple(views)


def _public_text_views(value: str, *, strip_markup: bool = False) -> tuple[str, ...]:
    decoded = _runtime_decoded_text(value)
    views = [normalize_public_text(decoded)]
    if strip_markup and "<" in decoded and ">" in decoded:
        views.append(normalize_public_text(HTML_TAG_PATTERN.sub("", decoded)))
    return tuple(dict.fromkeys(views))


def _markers_in(value: str) -> set[str]:
    return {
        label
        for normalized in _public_text_views(value)
        for label, pattern in FORBIDDEN_PATTERNS
        if pattern.search(normalized)
    }


def _scan_file(path: Path) -> tuple[set[str], bool, int]:
    markers: set[str] = set()
    required_brand_found = False
    byte_count = path.stat().st_size
    overlap = ""
    is_html = path.suffix.casefold() in {".html", ".htm"}
    html_parser = _VisibleHTMLParser() if is_html else None
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        while True:
            chunk = handle.read(READ_CHUNK_SIZE)
            if not chunk:
                break
            if html_parser is not None:
                html_parser.feed(chunk)
            combined = overlap + chunk
            for normalized in _public_text_views(combined, strip_markup=not is_html):
                if not is_html:
                    required_brand_found = required_brand_found or REQUIRED_PUBLIC_BRAND in normalized
                for label, pattern in FORBIDDEN_PATTERNS:
                    if label not in markers and pattern.search(normalized):
                        markers.add(label)
            overlap = combined[-CHUNK_OVERLAP:]
    if html_parser is not None:
        html_parser.close()
        for visible_text in html_parser.visible_text_views():
            for normalized in _decoded_html_text_views(visible_text):
                required_brand_found = required_brand_found or REQUIRED_PUBLIC_BRAND in normalized
                for label, pattern in FORBIDDEN_PATTERNS:
                    if label not in markers and pattern.search(normalized):
                        markers.add(label)
    return markers, required_brand_found, byte_count


def check_public_brand(root: Path | str) -> dict[str, int]:
    public_root = Path(root)
    if not public_root.is_dir() or public_root.is_symlink():
        raise PublicBrandError("Public artifact root must be a real directory")

    violations: set[BrandViolation] = set()
    homepage_brand_found = False
    file_count = 0
    byte_count = 0
    for path in sorted(public_root.rglob("*")):
        relative = path.relative_to(public_root).as_posix()
        if path.is_symlink():
            raise PublicBrandError("Public artifact must not contain symbolic links")
        if normalize_public_text(relative).casefold() in FORBIDDEN_PUBLIC_PATHS:
            violations.add(BrandViolation(relative, "retired public contact-card asset"))
        for marker in _markers_in(relative):
            violations.add(BrandViolation(relative, marker))
        if not path.is_file():
            continue
        file_count += 1
        markers, found, size = _scan_file(path)
        byte_count += size
        if relative == "index.html":
            homepage_brand_found = found
        for marker in markers:
            violations.add(BrandViolation(relative, marker))

    if not file_count:
        raise PublicBrandError("Public artifact contains no files")
    if not homepage_brand_found:
        violations.add(BrandViolation("index.html", f"missing required brand: {REQUIRED_PUBLIC_BRAND}"))
    app_mark = public_root / REQUIRED_APP_MARK_PATH
    if not app_mark.is_file() or app_mark.is_symlink():
        violations.add(BrandViolation(REQUIRED_APP_MARK_PATH, "missing required KC brand mark"))
    else:
        app_mark_source = app_mark.read_text(encoding="utf-8", errors="ignore")
        if not _valid_app_mark(app_mark_source):
            violations.add(BrandViolation(REQUIRED_APP_MARK_PATH, "brand mark aria-label must be KC or KC桌面"))
    if violations:
        details = "\n".join(
            f"- {violation.path}: {violation.marker}"
            for violation in sorted(violations)[:50]
        )
        remaining = len(violations) - 50
        if remaining > 0:
            details += f"\n- ... and {remaining} more violation(s)"
        raise PublicBrandError(f"Public brand check failed:\n{details}")

    return {"files": file_count, "bytes": byte_count}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a materialized public website against the public brand contract."
    )
    parser.add_argument("root", type=Path, help="Materialized public website root")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        stats = check_public_brand(args.root)
    except PublicBrandError as error:
        print(error, file=sys.stderr)
        return 1
    print(
        f"public brand check passed ({stats['files']} files, {stats['bytes']} bytes, "
        f"required brand: {REQUIRED_PUBLIC_BRAND})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
