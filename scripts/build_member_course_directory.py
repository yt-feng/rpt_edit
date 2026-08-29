#!/usr/bin/env python3
"""Build a gated, privacy-clean course resource directory.

The source index and mapping configuration are private inputs.  The mapping
configuration owns every source-specific value: path prefixes, redaction terms,
keyword rules, notable-entity aliases, and the HMAC secret.  This public script
contains no source/provider names and never exports an original path.

Output is the compact flat contract consumed by the gated Worker:
``{schema_version, generated_at, items}``.  Every item contains only an opaque
ID, neutral course ID, clean display name, clean folder labels, file metadata,
and allowlisted notable-entity names.  The Worker can enforce its membership
gate, paginate/search the safe fields, and reconstruct the folder tree from the
``folders`` list.  The builder deliberately fails closed when any record is
unmapped or an emitted string still contains a configured private term or
contact marker.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Sequence


SCHEMA_VERSION = 1
MAX_COMPACT_JSON_BYTES = 16 * 1024 * 1024
MAX_DIRECTORY_ITEMS = 45_000
ALLOWED_COURSE_IDS = frozenset({
    "fin-01", "fin-02", "fin-03", "fin-04", "fin-05", "fin-06",
    "cap-01", "cap-02", "cap-03", "cap-04", "cap-05", "cap-06", "cap-07",
    "inv-01", "inv-02", "inv-03", "inv-04",
    "res-01", "res-02", "res-03", "res-04", "res-05",
    "law-01", "law-02", "law-03", "law-04", "law-05", "law-06",
    "lit-01", "lit-02", "lit-03", "lit-04",
    "lib-01", "lib-02", "lib-03", "lib-04", "lib-05",
    "career-01", "career-02", "career-03",
    "alt-01", "alt-02", "alt-03", "str-01",
})
INDEX_LINE_RE = re.compile(
    r"^- `(?P<path>.+)` — (?P<size>[0-9]+(?:\.[0-9]+)?(?:B|KB|MB|GB|TB)) — "
    r"(?P<date>\d{4}-\d{2}-\d{2})$"
)
SIZE_RE = re.compile(r"^(?P<number>[0-9]+(?:\.[0-9]+)?)(?P<unit>B|KB|MB|GB|TB)$")
EXTENSION_RE = re.compile(r"\.([A-Za-z0-9]{1,12})$")
ASCII_WORD_RE = re.compile(r"^[A-Za-z0-9]+$")
GENERIC_TITLE_RE = re.compile(
    r"^(?:(?:lesson|unit|chapter|part|section|module|video|audio|file|document|"
    r"course|class|lecture|page|session|episode|track)[\s._-]*)?\d{1,5}(?:[._-]\d{1,4})?$",
    re.IGNORECASE,
)
CONTACT_PATTERNS = (
    re.compile(r"(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9.-])"),
    re.compile(r"(?i)(?:https?|ftp)\s*:\s*/\s*/\S*"),
    re.compile(r"(?i)www\s*\.\s*\S*"),
    re.compile(r"(?i)(?<![A-Z0-9-])(?:[A-Z0-9-]+\.)+(?:com|cn|net|org|io|co|edu|gov|info|biz|me)"
               r"(?:\.[A-Z]{2,})?(?:/\S*)?(?![A-Z0-9-])"),
    re.compile(r"(?<!\d)(?:\+?86[-\s]?)?1[3-9]\d{9}(?!\d)"),
    re.compile(r"(?i)(?:we\s*chat|wechat|vx|qq|telegram)[\s:：_-]*[A-Z0-9_-]{3,}"),
    re.compile(r"(?:微信|微\s*信|公众号|联系(?:方式)?|群号|群聊|加群|提取码|网盘密码|"
               r"解压密码)[\s:：_-]*[A-Za-z0-9_-]{2,}"),
)
SPACE_RE = re.compile(r"\s+")
LEADING_SEPARATOR_RE = re.compile(r"^[\s._\-—:：|丨·/\\]+")
TRAILING_SEPARATOR_RE = re.compile(r"[\s._\-—:：|丨·/\\]+$")
REPEATED_SEPARATOR_RE = re.compile(r"(?:\s*[|丨·]\s*){2,}")


class BuildError(RuntimeError):
    """The private input cannot be converted without exposing source data."""


COURSE_MATERIAL_COURSE = {
    "id": "str-01",
    "category": "战略咨询",
    "title": "麦府学堂｜战略与商业分析方法论",
}
COURSE_MATERIAL_DATE = "2026-08-29"
COURSE_MATERIAL_FOLDER = "战略咨询方法论"
COURSE_MATERIAL_FIELDS = frozenset({
    "id", "source_filename", "title", "topic", "summary", "pages", "bytes",
    "sha256", "cover", "featured", "entities",
})
COURSE_MATERIAL_ID_RE = re.compile(r"maifu-(?:0[1-9]|1[0-9]|20)\Z")


def _course_material_text(value: Any, field: str, limit: int) -> str:
    if not isinstance(value, str):
        raise BuildError(f"Course material {field} must be text.")
    text = unicodedata.normalize("NFKC", value)
    if any(ord(character) < 32 or ord(character) == 127 for character in text):
        raise BuildError(f"Course material {field} contains a control character.")
    text = SPACE_RE.sub(" ", text).strip()
    if not text or len(text) > limit:
        raise BuildError(f"Course material {field} has an invalid length.")
    return text


def _course_material_size_label(byte_count: int) -> str:
    value = float(byte_count)
    unit = "B"
    for candidate in ("KB", "MB", "GB", "TB"):
        if value < 1024:
            break
        value /= 1024
        unit = candidate
    precision = 0 if unit == "B" else 1
    return f"{value:.{precision}f} {unit}"


def merge_course_material_manifest(payload: Mapping[str, Any], manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Append the fixed public material manifest to an established private directory.

    The static manifest is treated only as untrusted release data. Source names,
    digests, cover paths, and other publishing fields are validated but never
    copied into the member directory. The private publisher performs its usual
    redaction/contact pass over the returned rows before any R2 mutation.
    """

    if not isinstance(payload, Mapping) or int(payload.get("schema_version") or 0) != SCHEMA_VERSION:
        raise BuildError("Directory payload schema is invalid.")
    existing = payload.get("items")
    if not isinstance(existing, list) or not existing:
        raise BuildError("Directory payload item count is invalid.")
    if not isinstance(manifest, Mapping) or int(manifest.get("schema_version") or 0) != 1:
        raise BuildError("Course material manifest schema is invalid.")
    if manifest.get("course") != COURSE_MATERIAL_COURSE:
        raise BuildError("Course material manifest course metadata is invalid.")
    items = manifest.get("items")
    if not isinstance(items, list) or len(items) != 20:
        raise BuildError("Course material manifest must contain exactly 20 items.")

    expected_ids = {f"maifu-{number:02d}" for number in range(1, 21)}
    material_ids: set[str] = set()
    material_rows: list[dict[str, Any]] = []
    for position, item in enumerate(items, 1):
        if not isinstance(item, Mapping) or set(item) != COURSE_MATERIAL_FIELDS:
            raise BuildError(f"Course material item {position} has an invalid schema.")
        material_id = str(item.get("id") or "").strip().lower()
        if not COURSE_MATERIAL_ID_RE.fullmatch(material_id) or material_id in material_ids:
            raise BuildError(f"Course material item {position} has an invalid identifier.")
        if material_id != f"maifu-{position:02d}":
            raise BuildError("Course material manifest order is invalid.")
        source_filename = _course_material_text(item.get("source_filename"), "source filename", 240)
        if "/" in source_filename or "\\" in source_filename or not source_filename.lower().endswith(".pdf"):
            raise BuildError(f"Course material item {position} has an invalid source filename.")
        title = _course_material_text(item.get("title"), "title", 240)
        _course_material_text(item.get("topic"), "topic", 100)
        _course_material_text(item.get("summary"), "summary", 500)
        page_count = item.get("pages")
        byte_count = item.get("bytes")
        if isinstance(page_count, bool) or not isinstance(page_count, int) or not 1 <= page_count <= 5000:
            raise BuildError(f"Course material item {position} has an invalid page count.")
        if isinstance(byte_count, bool) or not isinstance(byte_count, int) or not 1 <= byte_count <= 128 * 1024 * 1024:
            raise BuildError(f"Course material item {position} has an invalid byte count.")
        digest = str(item.get("sha256") or "").strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise BuildError(f"Course material item {position} has an invalid digest.")
        cover = _course_material_text(item.get("cover"), "cover", 160)
        if cover != f"assets/course-covers/{material_id}.webp":
            raise BuildError(f"Course material item {position} has an invalid cover path.")
        if not isinstance(item.get("featured"), bool):
            raise BuildError(f"Course material item {position} has an invalid featured flag.")
        raw_entities = item.get("entities")
        if not isinstance(raw_entities, list):
            raise BuildError(f"Course material item {position} has invalid entities.")
        entities: list[str] = []
        for raw_entity in raw_entities[:8]:
            entity = _course_material_text(raw_entity, "entity", 80)
            entity = SPACE_RE.sub(" ", entity.replace("/", " · ").replace("\\", " · ")).strip()
            if entity not in entities:
                entities.append(entity)
        material_rows.append({
            "id": material_id,
            "course_id": COURSE_MATERIAL_COURSE["id"],
            "name": title,
            "folders": [COURSE_MATERIAL_FOLDER],
            "extension": "pdf",
            "size_label": _course_material_size_label(byte_count),
            "date": COURSE_MATERIAL_DATE,
            "entities": entities,
        })
        material_ids.add(material_id)

    if material_ids != expected_ids:
        raise BuildError("Course material manifest identifiers are incomplete.")
    merged = [
        row for row in existing
        if not isinstance(row, Mapping) or str(row.get("id") or "").strip().lower() not in material_ids
    ]
    merged.extend(material_rows)
    if len(merged) > MAX_DIRECTORY_ITEMS:
        raise BuildError("Merged directory payload item count is invalid.")
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": payload.get("generated_at", ""),
        "items": merged,
    }


@dataclass(frozen=True)
class SourceRecord:
    line_number: int
    relative_parts: tuple[str, ...]
    size_text: str
    size_bytes: int
    indexed_date: str


@dataclass(frozen=True)
class PrefixRule:
    prefix_parts: tuple[str, ...]
    folded_parts: tuple[str, ...]
    course_ids: tuple[str, ...]
    strip_components: int
    priority: int


@dataclass(frozen=True)
class KeywordRule:
    keyword_folds: tuple[str, ...]
    exclude_folds: tuple[str, ...]
    course_ids: tuple[str, ...]
    when_course_ids: frozenset[str]
    mode: str
    primary: bool
    priority: int


@dataclass(frozen=True)
class EntityRule:
    name: str
    entity_type: str
    aliases: tuple[str, ...]
    alias_folds: tuple[str, ...]


@dataclass(frozen=True)
class MappingResult:
    primary_course_id: str
    course_ids: tuple[str, ...]
    strip_components: int


def compact_fold(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return "".join(character for character in text if character.isalnum())


def display_clean(value: Any, limit: int) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).replace("\x00", " ")
    text = SPACE_RE.sub(" ", text).strip()
    return text[:limit]


def unique_strings(values: Iterable[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        key = unicodedata.normalize("NFKC", value).casefold()
        if value and key not in seen:
            seen.add(key)
            result.append(value)
    return result


def parse_size(value: str) -> int:
    match = SIZE_RE.fullmatch(value)
    if not match:
        raise BuildError("The private index contains an invalid size value.")
    multipliers = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4}
    return round(float(match.group("number")) * multipliers[match.group("unit")])


def load_private_config(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError("The private mapping configuration is unavailable or invalid.") from exc
    if not isinstance(value, dict):
        raise BuildError("The private mapping configuration must be a JSON object.")
    return value


def require_nonempty_string(value: Any, field: str) -> str:
    text = display_clean(value, 500)
    if not text:
        raise BuildError(f"Private mapping field {field!r} must be a non-empty string.")
    return text


def split_private_path(value: str) -> tuple[str, ...]:
    parts = tuple(part for part in value.replace("\\", "/").split("/") if part)
    if not parts:
        raise BuildError("A private mapping prefix is empty.")
    return parts


class CourseDirectoryBuilder:
    def __init__(self, config: Mapping[str, Any], *, hmac_secret: str | None = None) -> None:
        self.catalog_version = require_nonempty_string(config.get("catalog_version"), "catalog_version")
        self.root_prefix = split_private_path(require_nonempty_string(config.get("root_prefix"), "root_prefix"))
        secret = hmac_secret or str(config.get("hmac_secret") or "")
        if len(secret.encode("utf-8")) < 24:
            raise BuildError("The private HMAC secret must contain at least 24 UTF-8 bytes.")
        self.hmac_secret = secret.encode("utf-8")
        self.courses = self._load_courses(config.get("courses"))
        self.course_order = {course["id"]: position for position, course in enumerate(self.courses)}
        self.course_by_id = {course["id"]: course for course in self.courses}
        self.redaction_terms = self._load_redaction_terms(config.get("privacy"))
        self.redaction_patterns = self._load_redaction_patterns(config.get("privacy"))
        self.term_patterns = tuple(self._fuzzy_term_pattern(term) for term in self.redaction_terms)
        self.guard_folds = tuple(sorted({compact_fold(term) for term in self.redaction_terms}, key=len, reverse=True))
        self.prefix_rules = self._load_prefix_rules(config.get("prefix_rules"))
        self.keyword_rules = self._load_keyword_rules(config.get("keyword_rules", []))
        self.entities = self._load_entities(config.get("notable_entities", []))
        self.max_links_per_file = max(1, min(int(config.get("max_links_per_file", 8)), 20))
        self._validate_private_config()

    def _load_courses(self, raw: Any) -> list[dict[str, str]]:
        if not isinstance(raw, list) or not raw:
            raise BuildError("The private mapping must declare at least one course.")
        courses: list[dict[str, str]] = []
        ids: set[str] = set()
        for position, item in enumerate(raw):
            if not isinstance(item, dict):
                raise BuildError("Each private course entry must be a JSON object.")
            course_id = require_nonempty_string(item.get("id"), f"courses[{position}].id").casefold()
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", course_id):
                raise BuildError("Course IDs may contain only lowercase letters, numbers, and hyphens.")
            if course_id not in ALLOWED_COURSE_IDS:
                raise BuildError("The private mapping contains an unsupported course ID.")
            if course_id in ids:
                raise BuildError("The private mapping contains a duplicate course ID.")
            ids.add(course_id)
            courses.append({
                "id": course_id,
                "title": require_nonempty_string(item.get("title"), f"courses[{position}].title"),
                "category": require_nonempty_string(item.get("category"), f"courses[{position}].category"),
            })
        return courses

    def _load_redaction_terms(self, raw_privacy: Any) -> tuple[str, ...]:
        if not isinstance(raw_privacy, dict):
            raise BuildError("The private mapping must include a privacy object.")
        raw_terms = raw_privacy.get("redact_terms")
        if not isinstance(raw_terms, list) or not raw_terms:
            raise BuildError("The private mapping must include redaction terms.")
        terms = unique_strings(require_nonempty_string(value, "privacy.redact_terms") for value in raw_terms)
        if any(len(compact_fold(term)) < 2 for term in terms):
            raise BuildError("Private redaction terms must contain at least two letters or numbers.")
        return tuple(sorted(terms, key=lambda value: len(compact_fold(value)), reverse=True))

    def _load_redaction_patterns(self, raw_privacy: Any) -> tuple[re.Pattern[str], ...]:
        values = raw_privacy.get("redact_patterns", []) if isinstance(raw_privacy, dict) else []
        if not isinstance(values, list):
            raise BuildError("privacy.redact_patterns must be a JSON list.")
        patterns: list[re.Pattern[str]] = []
        for value in values:
            pattern = require_nonempty_string(value, "privacy.redact_patterns")
            try:
                patterns.append(re.compile(pattern, re.IGNORECASE))
            except re.error as exc:
                raise BuildError("A private redaction pattern is invalid.") from exc
        return tuple(patterns)

    def _load_prefix_rules(self, raw: Any) -> tuple[PrefixRule, ...]:
        if not isinstance(raw, list) or not raw:
            raise BuildError("The private mapping must include prefix rules.")
        rules: list[PrefixRule] = []
        for position, item in enumerate(raw):
            if not isinstance(item, dict):
                raise BuildError("Each prefix rule must be a JSON object.")
            prefix_parts = split_private_path(require_nonempty_string(item.get("prefix"), "prefix_rules.prefix"))
            course_ids = self._course_ids(item.get("course_ids"), f"prefix_rules[{position}]")
            strip_components = int(item.get("strip_components", len(prefix_parts)))
            if strip_components < 0 or strip_components > 32:
                raise BuildError("A prefix rule has an invalid strip_components value.")
            rules.append(PrefixRule(
                prefix_parts=prefix_parts,
                folded_parts=tuple(unicodedata.normalize("NFKC", part).casefold() for part in prefix_parts),
                course_ids=course_ids,
                strip_components=strip_components,
                priority=int(item.get("priority", 0)),
            ))
        return tuple(rules)

    def _load_keyword_rules(self, raw: Any) -> tuple[KeywordRule, ...]:
        if not isinstance(raw, list):
            raise BuildError("keyword_rules must be a JSON list.")
        rules: list[KeywordRule] = []
        for position, item in enumerate(raw):
            if not isinstance(item, dict):
                raise BuildError("Each keyword rule must be a JSON object.")
            raw_keywords = item.get("keywords")
            if not isinstance(raw_keywords, list) or not raw_keywords:
                raise BuildError("Each keyword rule must declare at least one private keyword.")
            keyword_folds = tuple(compact_fold(require_nonempty_string(value, "keyword_rules.keywords")) for value in raw_keywords)
            raw_excludes = item.get("exclude_keywords", [])
            if not isinstance(raw_excludes, list):
                raise BuildError("exclude_keywords must be a JSON list.")
            exclude_folds = tuple(compact_fold(require_nonempty_string(value, "keyword_rules.exclude_keywords")) for value in raw_excludes)
            course_ids = self._course_ids(item.get("course_ids"), f"keyword_rules[{position}]")
            when_values = item.get("when_course_ids", [])
            when_course_ids = frozenset(self._course_ids(when_values, "when_course_ids", allow_empty=True))
            mode = str(item.get("mode", "any")).casefold()
            if mode not in {"any", "all"}:
                raise BuildError("A keyword rule mode must be 'any' or 'all'.")
            rules.append(KeywordRule(
                keyword_folds=keyword_folds,
                exclude_folds=exclude_folds,
                course_ids=course_ids,
                when_course_ids=when_course_ids,
                mode=mode,
                primary=bool(item.get("primary", False)),
                priority=int(item.get("priority", 0)),
            ))
        return tuple(sorted(rules, key=lambda rule: rule.priority, reverse=True))

    def _load_entities(self, raw: Any) -> tuple[EntityRule, ...]:
        if not isinstance(raw, list):
            raise BuildError("notable_entities must be a JSON list.")
        entities: list[EntityRule] = []
        for position, item in enumerate(raw):
            if not isinstance(item, dict):
                raise BuildError("Each notable entity must be a JSON object.")
            name = require_nonempty_string(item.get("name"), f"notable_entities[{position}].name")
            entity_type = require_nonempty_string(item.get("type"), f"notable_entities[{position}].type")
            aliases_raw = item.get("aliases", [])
            if not isinstance(aliases_raw, list):
                raise BuildError("Entity aliases must be a JSON list.")
            aliases = tuple(unique_strings([name, *(require_nonempty_string(value, "entity alias") for value in aliases_raw)]))
            entities.append(EntityRule(
                name=name,
                entity_type=entity_type,
                aliases=aliases,
                alias_folds=tuple(compact_fold(alias) for alias in aliases),
            ))
        return tuple(entities)

    def _course_ids(self, raw: Any, field: str, *, allow_empty: bool = False) -> tuple[str, ...]:
        if raw is None and allow_empty:
            return ()
        if not isinstance(raw, list) or (not raw and not allow_empty):
            raise BuildError(f"{field} must contain course IDs.")
        result = tuple(unique_strings(str(value).casefold() for value in raw))
        unknown = [course_id for course_id in result if course_id not in self.course_by_id]
        if unknown:
            raise BuildError(f"{field} references an unknown course ID.")
        return result

    def _validate_private_config(self) -> None:
        for course in self.courses:
            self._guard_string(course["title"], "course title")
            self._guard_string(course["category"], "course category")
        for entity in self.entities:
            self._guard_string(entity.name, "notable entity")
            for alias_fold in entity.alias_folds:
                if any(guard in alias_fold or alias_fold in guard for guard in self.guard_folds):
                    raise BuildError("A notable entity conflicts with a private redaction term.")

    @staticmethod
    def _fuzzy_term_pattern(term: str) -> re.Pattern[str]:
        characters = [character for character in unicodedata.normalize("NFKC", term) if character.isalnum()]
        if not characters:
            raise BuildError("A private redaction term has no searchable characters.")
        joiner = r"[\s._\-—:：|丨·/\\]*"
        return re.compile(joiner.join(re.escape(character) for character in characters), re.IGNORECASE)

    def parse_index(self, path: Path) -> Iterator[SourceRecord]:
        try:
            handle = path.open(encoding="utf-8")
        except OSError as exc:
            raise BuildError("The private source index cannot be read.") from exc
        root_folded = tuple(unicodedata.normalize("NFKC", part).casefold() for part in self.root_prefix)
        with handle:
            for line_number, raw_line in enumerate(handle, 1):
                line = raw_line.rstrip("\n")
                if not line.startswith("- `"):
                    continue
                match = INDEX_LINE_RE.fullmatch(line)
                if not match:
                    raise BuildError(f"Private index line {line_number} has an unsupported format.")
                full_parts = split_private_path(match.group("path"))
                full_folded = tuple(unicodedata.normalize("NFKC", part).casefold() for part in full_parts)
                if full_folded[:len(root_folded)] != root_folded or len(full_parts) <= len(self.root_prefix):
                    raise BuildError(f"Private index line {line_number} is outside the configured root.")
                relative_parts = full_parts[len(self.root_prefix):]
                if len(relative_parts) < 2:
                    raise BuildError(f"Private index line {line_number} has no mappable file hierarchy.")
                yield SourceRecord(
                    line_number=line_number,
                    relative_parts=relative_parts,
                    size_text=match.group("size"),
                    size_bytes=parse_size(match.group("size")),
                    indexed_date=match.group("date"),
                )

    def map_record(self, record: SourceRecord) -> MappingResult:
        folded_parts = tuple(unicodedata.normalize("NFKC", part).casefold() for part in record.relative_parts)
        matches = [
            rule for rule in self.prefix_rules
            if len(folded_parts) >= len(rule.folded_parts)
            and folded_parts[:len(rule.folded_parts)] == rule.folded_parts
        ]
        if not matches:
            raise BuildError(f"Private index line {record.line_number} has no prefix mapping.")
        matches.sort(key=lambda rule: (len(rule.folded_parts), rule.priority), reverse=True)
        selected = matches[0]
        course_ids = list(selected.course_ids)
        primary_course_id = course_ids[0]
        haystack = compact_fold("/".join(record.relative_parts))
        for rule in self.keyword_rules:
            if rule.when_course_ids and primary_course_id not in rule.when_course_ids:
                continue
            if rule.exclude_folds and any(value and value in haystack for value in rule.exclude_folds):
                continue
            checks = [value in haystack for value in rule.keyword_folds if value]
            matched = all(checks) if rule.mode == "all" else any(checks)
            if not matched:
                continue
            for course_id in rule.course_ids:
                if course_id not in course_ids:
                    course_ids.append(course_id)
            if rule.primary:
                primary_course_id = rule.course_ids[0]
                course_ids = [primary_course_id, *(value for value in course_ids if value != primary_course_id)]
        return MappingResult(
            primary_course_id=primary_course_id,
            course_ids=tuple(course_ids[:self.max_links_per_file]),
            strip_components=selected.strip_components,
        )

    def _sanitize(self, value: str, *, limit: int) -> str:
        text = unicodedata.normalize("NFKC", value).replace("\x00", " ")
        for pattern in self.term_patterns:
            text = pattern.sub(" ", text)
        for pattern in self.redaction_patterns:
            text = pattern.sub(" ", text)
        for pattern in CONTACT_PATTERNS:
            text = pattern.sub(" ", text)
        text = text.replace("/", " · ").replace("\\", " · ")
        text = REPEATED_SEPARATOR_RE.sub(" ", text)
        text = LEADING_SEPARATOR_RE.sub("", text)
        text = TRAILING_SEPARATOR_RE.sub("", text)
        text = SPACE_RE.sub(" ", text).strip()
        return text[:limit]

    @staticmethod
    def _split_filename(value: str) -> tuple[str, str]:
        match = EXTENSION_RE.search(value)
        if not match:
            return value, ""
        extension = match.group(1).casefold()
        return value[:match.start()], extension

    def _safe_display_parts(
        self,
        record: SourceRecord,
        mapping: MappingResult,
    ) -> tuple[list[str], str, str]:
        retained = list(record.relative_parts[mapping.strip_components:])
        if not retained:
            retained = [record.relative_parts[-1]]
        raw_filename = retained[-1]
        raw_directories = retained[:-1]
        directories: list[str] = []
        for value in raw_directories:
            title = self._sanitize(value, limit=180)
            if not title:
                continue
            if directories and compact_fold(directories[-1]) == compact_fold(title):
                continue
            self._guard_string(title, f"directory title at line {record.line_number}")
            directories.append(title)
        raw_stem, extension = self._split_filename(raw_filename)
        title = self._sanitize(raw_stem, limit=240)
        if not title:
            title = directories[-1] if directories else self.course_by_id[mapping.primary_course_id]["title"]
        if GENERIC_TITLE_RE.fullmatch(compact_fold(title)) and directories:
            title = f"{directories[-1]} · {title}"
        title = display_clean(title, 240)
        self._guard_string(title, f"file title at line {record.line_number}")
        return directories, title, extension

    def _detect_entities(self, record: SourceRecord) -> list[str]:
        raw_haystack = unicodedata.normalize("NFKC", "/".join(record.relative_parts)).casefold()
        compact_haystack = compact_fold(raw_haystack)
        found: list[str] = []
        seen: set[tuple[str, str]] = set()
        for entity in self.entities:
            if not any(
                self._alias_matches(alias, alias_fold, raw_haystack, compact_haystack)
                for alias, alias_fold in zip(entity.aliases, entity.alias_folds)
            ):
                continue
            key = (entity.entity_type, entity.name.casefold())
            if key in seen:
                continue
            seen.add(key)
            found.append(entity.name)
        return found[:8]

    @staticmethod
    def _alias_matches(alias: str, alias_fold: str, raw_haystack: str, compact_haystack: str) -> bool:
        if not alias_fold:
            return False
        normalized_alias = unicodedata.normalize("NFKC", alias).strip().casefold()
        if ASCII_WORD_RE.fullmatch(normalized_alias) and len(alias_fold) <= 5:
            return re.search(
                rf"(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])",
                raw_haystack,
                re.IGNORECASE,
            ) is not None
        return alias_fold in compact_haystack

    def _opaque_id(self, namespace: str, *values: str) -> str:
        payload = "\x00".join([namespace, *values]).encode("utf-8")
        digest = hmac.new(self.hmac_secret, payload, hashlib.sha256).hexdigest()[:32]
        return f"{namespace[0]}_{digest}"

    def _guard_string(self, value: str, field: str) -> None:
        folded = compact_fold(value)
        if any(term and term in folded for term in self.guard_folds):
            raise BuildError(f"Privacy guard rejected {field}; no output was written.")
        if any(pattern.search(value) for pattern in CONTACT_PATTERNS):
            raise BuildError(f"Contact guard rejected {field}; no output was written.")

    def build(self, records: Iterable[SourceRecord]) -> dict[str, Any]:
        items: list[dict[str, Any]] = []
        unique_resource_ids: set[str] = set()
        source_record_count = 0
        entity_hits: Counter[str] = Counter()
        course_counts: Counter[str] = Counter()

        for record in records:
            source_record_count += 1
            mapping = self.map_record(record)
            safe_directories, title, extension = self._safe_display_parts(record, mapping)
            entities = self._detect_entities(record)
            for entity in entities:
                entity_hits[entity] += 1
            resource_id = self._opaque_id("resource", *record.relative_parts)
            unique_resource_ids.add(resource_id)
            for course_id in mapping.course_ids:
                file_id = self._opaque_id("file", course_id, *record.relative_parts)
                item = {
                    "id": file_id,
                    "course_id": course_id,
                    "name": title,
                    "folders": safe_directories[-8:],
                    "extension": extension[:10],
                    "size_label": record.size_text,
                    "date": record.indexed_date,
                    "entities": entities,
                }
                items.append(item)
                course_counts[course_id] += 1

        if source_record_count == 0:
            raise BuildError("The private source index contains no file records.")

        items.sort(key=lambda item: (
            self.course_order[item["course_id"]],
            tuple(compact_fold(value) for value in item["folders"]),
            compact_fold(item["name"]),
            item["id"],
        ))
        payload = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "items": items,
        }
        self.last_stats = {
            "catalog_version": self.catalog_version,
            "source_record_count": source_record_count,
            "unique_file_count": len(unique_resource_ids),
            "linked_file_count": len(items),
            "notable_entity_hit_count": sum(entity_hits.values()),
            "entity_counts": dict(entity_hits.most_common()),
            "course_counts": dict(course_counts),
        }
        self.validate_output(payload)
        return payload

    def validate_output(self, payload: Mapping[str, Any]) -> None:
        items = payload.get("items")
        if not isinstance(items, list) or not items or len(items) > MAX_DIRECTORY_ITEMS:
            raise BuildError("Output item count exceeds the final directory contract.")
        if len(json_bytes(payload, pretty=False)) > MAX_COMPACT_JSON_BYTES:
            raise BuildError("Compact UTF-8 output exceeds the final directory size contract.")
        forbidden_keys = {
            "raw_path", "source_path", "original_path", "storage_key", "provider",
            "source_provider", "teacher", "contact", "download_url", "resource_id",
        }

        def walk(value: Any, location: str) -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    if str(key).casefold() in forbidden_keys:
                        raise BuildError("Output schema contains a forbidden source field.")
                    if str(key).casefold() in {"id", "course_id", "generated_at", "extension", "size_label", "date"}:
                        continue
                    walk(child, f"{location}.{key}")
            elif isinstance(value, list):
                for position, child in enumerate(value):
                    walk(child, f"{location}[{position}]")
            elif isinstance(value, str):
                self._guard_string(value, location)

        walk(payload, "catalog")


def file_type(extension: str) -> str:
    value = extension.casefold()
    if value == "pdf":
        return "pdf"
    if value in {"mp4", "mov", "mkv", "avi", "wmv", "webm", "m4v"}:
        return "video"
    if value in {"mp3", "m4a", "wav", "aac", "flac", "ogg"}:
        return "audio"
    if value in {"doc", "docx", "rtf", "txt", "md"}:
        return "document"
    if value in {"ppt", "pptx", "key"}:
        return "presentation"
    if value in {"xls", "xlsx", "csv", "tsv"}:
        return "spreadsheet"
    if value in {"zip", "rar", "7z", "tar", "gz"}:
        return "archive"
    if value in {"jpg", "jpeg", "png", "gif", "webp", "svg", "bmp", "tiff"}:
        return "image"
    return "other"


def json_bytes(value: Mapping[str, Any], *, pretty: bool) -> bytes:
    if pretty:
        serialized = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    else:
        serialized = json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
    return serialized.encode("utf-8")


def atomic_write_json(path: Path, value: Mapping[str, Any], *, pretty: bool) -> None:
    serialized = json_bytes(value, pretty=pretty)
    if len(serialized) > MAX_COMPACT_JSON_BYTES:
        raise BuildError("Serialized UTF-8 output exceeds the final directory size contract.")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(serialized)
    os.replace(temporary, path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", required=True, type=Path, help="Private Markdown file index.")
    parser.add_argument("--map", required=True, dest="map_path", type=Path, help="Private JSON mapping file.")
    parser.add_argument("--output", required=True, type=Path, help="Private JSON catalog output.")
    parser.add_argument(
        "--hmac-secret-env",
        default="COURSE_DIRECTORY_HMAC_SECRET",
        help="Optional environment variable overriding the private map's HMAC secret.",
    )
    parser.add_argument("--pretty", action="store_true", help="Indent output JSON for inspection.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        config = load_private_config(args.map_path)
        secret = os.getenv(args.hmac_secret_env) or None
        builder = CourseDirectoryBuilder(config, hmac_secret=secret)
        payload = builder.build(builder.parse_index(args.index))
        atomic_write_json(args.output, payload, pretty=args.pretty)
    except BuildError as exc:
        print(f"course-directory build failed: {exc}", file=sys.stderr)
        return 2
    stats = builder.last_stats
    print(json.dumps({
        "output": args.output.name,
        "source_records": stats["source_record_count"],
        "unique_files": stats["unique_file_count"],
        "linked_files": stats["linked_file_count"],
        "notable_entity_hits": stats["notable_entity_hit_count"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
