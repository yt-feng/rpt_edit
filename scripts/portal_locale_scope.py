"""Remove out-of-cohort detail references without rewriting unrelated HTML."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import html
from html.parser import HTMLParser
import json
from urllib.parse import urljoin, urlsplit, urlunsplit


_VOID = frozenset("area base br col embed hr img input link meta param source track wbr".split())
_DROP = object()


def _canonical_identity(value: object, base: str, origin: str) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        url = urlsplit(urljoin(base, value.strip()))
    except ValueError:
        return None
    if url.scheme.lower() not in {"http", "https"} or urlunsplit((url.scheme.lower(), url.netloc.lower(), "/", "", "")) != origin:
        return None
    path = url.path or "/"
    if path in {"/", "/index.html"} and url.query:
        return None  # Shared query-driven homepage/navigation is not a detail URL.
    if path.endswith("/index.html"):
        path = path[:-10]
    path = path.rstrip("/") or "/"
    return urlunsplit((url.scheme.lower(), url.netloc.lower(), path, "", ""))


@lru_cache(maxsize=8)
def _normalized_canonical_set(origin: str, values: frozenset[str]) -> frozenset[str]:
    """Normalize a cohort once per origin, never relative to an individual page."""
    return frozenset(key for value in values if (key := _canonical_identity(value, origin, origin)) is not None)


@dataclass
class _Node:
    tag: str
    attrs: dict[str, str | None]
    start: int
    open_end: int
    parent: _Node | None
    close_start: int = 0
    end: int = 0


class _Spans(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.lines = [0]
        self.lines.extend(index + 1 for index, character in enumerate(source) if character == "\n")
        self.nodes: list[_Node] = []
        self.stack: list[_Node] = []

    def source_offset(self) -> int:
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def _close(self, index: int, position: int, end: int) -> None:
        for node in self.stack[index + 1:]:
            node.close_start = node.end = position
        node = self.stack[index]
        node.close_start, node.end = position, end
        del self.stack[index:]

    def handle_starttag(self, tag, attrs):
        start = self.source_offset()
        # HTML permits omitted </li>; do not let one removal swallow its sibling.
        if tag == "li":
            for index in range(len(self.stack) - 1, -1, -1):
                if self.stack[index].tag in {"ul", "ol", "menu"}:
                    break
                if self.stack[index].tag == "li":
                    self._close(index, start, start)
                    break
        node = _Node(tag, dict(attrs), start, start + len(self.get_starttag_text()),
                     self.stack[-1] if self.stack else None)
        self.nodes.append(node)
        if tag in _VOID:
            node.close_start = node.end = node.open_end
        else:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack and self.stack[-1] is self.nodes[-1]:
            node = self.stack.pop()
            node.close_start = node.end = node.open_end

    def handle_endtag(self, tag):
        position = self.source_offset()
        end = self.source.find(">", position)
        end = len(self.source) if end < 0 else end + 1
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index].tag == tag:
                self._close(index, position, end)
                break

    def finish(self):
        self.feed(self.source)
        self.close()
        for node in self.stack:
            node.close_start = node.end = len(self.source)


def restrict_html_to_cohort(
    source: str, canonical: str, eligible_canonicals: frozenset[str],
    known_canonicals: frozenset[str],
) -> str:
    parsed = urlsplit(canonical)
    origin = urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), "/", "", ""))

    def identity(value):
        return _canonical_identity(value, canonical, origin)

    primary = identity(canonical)
    eligible = _normalized_canonical_set(origin, eligible_canonicals)
    known = _normalized_canonical_set(origin, known_canonicals)
    if not known or known is eligible:
        return source

    def excluded_identity(key):
        # No per-page full-set copy/difference: only O(1) membership checks.
        return key is not None and key != primary and key in known and key not in eligible

    def excluded_url(value):
        return excluded_identity(identity(value))

    def references(value):
        if isinstance(value, str):
            return {identity(value)}
        if isinstance(value, dict):
            return set().union(*(references(value.get(key)) for key in ("url", "@id", "item", "mainEntityOfPage")))
        return set()

    def filter_json(value):
        if isinstance(value, dict):
            refs = references(value)
            if primary not in refs and any(excluded_identity(key) for key in refs):
                return _DROP
            result = {}
            changed = False
            for key, child in value.items():
                filtered = _DROP if excluded_url(child) else filter_json(child)
                if filtered is _DROP:
                    changed = True
                else:
                    result[key] = filtered
                    changed |= filtered is not child
            if not changed:
                return value
            types = value.get("@type", [])
            types = {types} if isinstance(types, str) else set(types) if isinstance(types, list) else set()
            items = result.get("itemListElement")
            if types & {"ItemList", "BreadcrumbList"} and isinstance(items, list):
                result["itemListElement"] = [
                    {**item, "position": index} if isinstance(item, dict) and (item.get("@type") == "ListItem" or "position" in item) else item
                    for index, item in enumerate(items, 1)
                ]
                if "ItemList" in types or "numberOfItems" in result:
                    result["numberOfItems"] = len(items)
            return result
        if isinstance(value, list):
            result = []
            changed = False
            for child in value:
                filtered = _DROP if excluded_url(child) else filter_json(child)
                changed |= filtered is not child
                if filtered is not _DROP:
                    result.append(filtered)
            return result if changed else value
        return value

    parser = _Spans(source)
    parser.finish()
    removals: list[tuple[int, int]] = []
    replacements: list[tuple[int, int, str]] = []
    for node in parser.nodes:
        if node.tag == "a" and excluded_url(node.attrs.get("href")):
            target = node
            parent = node.parent
            while parent:
                labels = set((parent.attrs.get("class") or "").split()) | {parent.attrs.get("id")}
                if labels & {"legal", "legal-panel", "disclaimer", "disclaimer-panel", "main-article"} or parent.tag == "main":
                    break
                if parent.tag == "li" or (parent.tag == "article" and "blog-card" in (parent.attrs.get("class") or "").split()):
                    target = parent
                    break
                if parent.tag in {"article", "main"}:
                    break
                parent = parent.parent
            removals.append((target.start, target.end))
        elif node.tag == "script" and (node.attrs.get("type") or "").lower().split(";", 1)[0].strip() == "application/ld+json":
            try:
                payload = json.loads(source[node.open_end:node.close_start])
            except (ValueError, TypeError):
                continue
            filtered = filter_json(payload)
            if filtered is _DROP:
                removals.append((node.start, node.end))
            elif filtered is not payload:
                replacements.append((node.open_end, node.close_start,
                                     json.dumps(filtered, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")))
    if not removals and not replacements:
        return source
    merged: list[tuple[int, int]] = []
    for start, end in sorted(removals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    edits = [(start, end, "") for start, end in merged]
    edits.extend(edit for edit in replacements if not any(start <= edit[0] and edit[1] <= end for start, end in merged))
    for start, end, replacement in sorted(edits, reverse=True):
        source = source[:start] + replacement + source[end:]
    return source


def deferred_locale_source(canonical: str) -> str:
    """A complete, non-indexable source shell, with no historical title/body."""
    safe_canonical = html.escape(canonical, quote=True)
    return (
        '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,follow">'
        f'<link rel="canonical" href="{safe_canonical}">'
        '<title>内容暂未开放多语言版本</title></head><body><main>'
        '<p>此内容暂未开放多语言版本，请浏览最新文章。</p>'
        '<nav><a href="/">首页</a> <a href="/blog/">最新文章</a> '
        '<a href="/reports/">报告索引</a></nav></main></body></html>'
    )
