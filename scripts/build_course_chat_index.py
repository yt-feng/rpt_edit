#!/usr/bin/env python3
"""Build private, bounded Course Chat retrieval artifacts.

The source must already be the publisher's sanitized, flat directory payload.
Version 1 is retained as a rollback object.  Version 2 converts that same
allow-listed subset into two direct-hash indexes so a Worker request reads only
small R2 ranges instead of parsing the complete JSON file on a cold start.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import struct
import unicodedata
from dataclasses import dataclass
from typing import Any, Iterable


SCHEMA_VERSION = 1
LOOKUP_SCHEMA_VERSION = 2
LOOKUP_FORMAT = "course-chat-direct-bucket-v2"
LOOKUP_PREFIX = "_course-directory/v2/chat-lookup"
LOOKUP_NORMALIZATION = "nfkc-lower-cjk234-v1"
SLOT_SIZE = 12
POSTING_LIMIT = 48
MAX_QUERY_TOKENS = 8
MAX_CANDIDATES = 12
MAX_TOKENS_PER_ITEM = 96
MAX_LOOKUP_TOKENS = 200_000
MAX_BUCKET_BYTES = 64 * 1024
MAX_LOOKUP_DATA_BYTES = 32 * 1024 * 1024
MAX_LOOKUP_MANIFEST_BYTES = 32 * 1024
TARGET_KEYS_PER_BUCKET = 2
REPRESENTATIVES_PER_COURSE = 30
MAX_CHAT_INDEX_ITEMS = 5_000
MAX_CHAT_INDEX_BYTES = 2 * 1024 * 1024

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

ROW_FIELDS = frozenset({
    "id", "course_id", "name", "folders", "extension", "size_label", "date", "entities",
})

DOMAIN_HINTS = (
    "摩根大通", "高盛", "摩根士丹利", "美银", "瑞银", "花旗", "汇丰", "野村", "德银", "巴克莱",
    "金杜", "中伦", "君合", "国浩", "证监会", "上交所", "深交所", "最高人民法院",
    "投行", "并购", "估值", "建模", "面试", "行业研究", "科技", "医药", "消费", "宏观", "利率", "外汇",
    "ipo", "dcf", "lbo", "m&a", "financial modeling", "interview",
)
CJK_STOP_PHRASES = re.compile(
    r"(?:帮我|请问|希望|我想|我要|我准备|给我|推荐|值得看|最值得|最近|半年|相关|顶级|一些|一个|一下|"
    r"哪些|什么|怎么|寻找|查找|报告|研报|资料|课程|文件|方面|可以|需要|关于|的|和|与|或|是|了)"
)
LATIN_TOKEN = re.compile(r"[a-z0-9][a-z0-9.+&-]*")
HAN_RUN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]{2,}")
TOP_TIER = re.compile(
    r"(?:^|[^a-z0-9])(?:jpm|jpmorgan|goldman|morgan stanley|bofa|bank of america|ubs|citi|citigroup|hsbc)"
    r"(?=$|[^a-z0-9])|摩根大通|高盛|摩根士丹利|美银|瑞银|花旗|汇丰|金杜|中伦|君合|国浩|"
    r"证监会|上交所|深交所|最高人民法院"
)
SECOND_TIER = re.compile(
    r"(?:^|[^a-z0-9])(?:nomura|bernstein|deutsche bank|barclays|macquarie|mckinsey|bcg|bain)"
    r"(?=$|[^a-z0-9])|野村|德银|巴克莱|麦肯锡|贝恩"
)


class CourseChatIndexError(ValueError):
    """Raised when a safe directory cannot produce a bounded chat index."""


@dataclass(frozen=True)
class DirectIndex:
    """The table and data objects for one exact-key direct-hash index."""

    table: bytes
    data: bytes
    bucket_count: int
    key_count: int


@dataclass(frozen=True)
class CourseChatLookup:
    """All immutable objects plus the stable manifest for one release."""

    revision: str
    objects: dict[str, bytes]
    manifest: dict[str, Any]


def _compact_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def serialize_course_chat_index(payload: dict[str, Any]) -> bytes:
    """Serialize the rollback index and enforce the legacy Worker ceiling."""

    output = _compact_json(payload)
    if len(output) > MAX_CHAT_INDEX_BYTES:
        raise CourseChatIndexError("Course Chat index exceeds the byte limit")
    return output


def build_course_chat_index(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a deterministic, bounded allow-list subset of the directory."""

    if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA_VERSION:
        raise CourseChatIndexError("Course Chat source schema is invalid")
    rows = payload.get("items")
    if not isinstance(rows, list) or not rows:
        raise CourseChatIndexError("Course Chat source items are invalid")

    seen_ids: set[str] = set()
    source_courses: set[str] = set()
    mandatory_indexes: set[int] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != ROW_FIELDS:
            raise CourseChatIndexError("Course Chat source row is not allow-listed")
        opaque_id = row.get("id")
        course_id = row.get("course_id")
        entities = row.get("entities")
        if not isinstance(opaque_id, str) or not opaque_id or opaque_id in seen_ids:
            raise CourseChatIndexError("Course Chat source identifier is invalid")
        if course_id not in ALLOWED_COURSE_IDS:
            raise CourseChatIndexError("Course Chat source course is invalid")
        if not isinstance(entities, list) or any(not isinstance(value, str) for value in entities):
            raise CourseChatIndexError("Course Chat source entities are invalid")
        seen_ids.add(opaque_id)
        source_courses.add(course_id)
        if entities:
            mandatory_indexes.add(index)

    if source_courses != ALLOWED_COURSE_IDS:
        raise CourseChatIndexError("Course Chat source does not cover every course")
    if len(mandatory_indexes) > MAX_CHAT_INDEX_ITEMS:
        raise CourseChatIndexError("Entity-bearing Course Chat rows exceed the item limit")

    selected_indexes = set(mandatory_indexes)
    neutral_counts = {course_id: 0 for course_id in ALLOWED_COURSE_IDS}
    for index, row in enumerate(rows):
        if index in mandatory_indexes:
            continue
        course_id = row["course_id"]
        if neutral_counts[course_id] >= REPRESENTATIVES_PER_COURSE:
            continue
        selected_indexes.add(index)
        neutral_counts[course_id] += 1

    if len(selected_indexes) > MAX_CHAT_INDEX_ITEMS:
        raise CourseChatIndexError("Course Chat index exceeds the item limit")

    selected_rows = [row for index, row in enumerate(rows) if index in selected_indexes]
    if {row["course_id"] for row in selected_rows} != ALLOWED_COURSE_IDS:
        raise CourseChatIndexError("Course Chat index does not cover every course")

    result = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": payload.get("generated_at", ""),
        "items": selected_rows,
    }
    serialize_course_chat_index(result)
    return result


def normalize_course_chat_tokens(value: Any, *, query: bool = False) -> list[str]:
    """Tokenize with the same bounded NFKC/lower/CJK-gram contract as Worker."""

    raw = unicodedata.normalize("NFKC", str(value or "")).lower()
    tokens: list[str] = [hint for hint in DOMAIN_HINTS if hint in raw]
    tokens.extend(token for token in LATIN_TOKEN.findall(raw) if len(token) >= 2)
    for run in HAN_RUN.findall(raw):
        chunks = CJK_STOP_PHRASES.sub(" ", run).split() if query else [run]
        for chunk in (part for part in chunks if len(part) >= 2):
            if len(chunk) <= 8:
                tokens.append(chunk)
            for width in (4, 3, 2):
                if len(chunk) < width:
                    continue
                tokens.extend(chunk[offset:offset + width] for offset in range(len(chunk) - width + 1))
    unique: list[str] = []
    seen: set[str] = set()
    limit = MAX_QUERY_TOKENS if query else MAX_TOKENS_PER_ITEM
    for token in tokens:
        if token in seen:
            continue
        seen.add(token)
        unique.append(token)
        if len(unique) >= limit:
            break
    return unique


def _item_tokens(item: dict[str, Any]) -> list[str]:
    text = " ".join([
        item["course_id"], item["name"], *item["folders"], item["extension"], *item["entities"],
    ])
    return normalize_course_chat_tokens(text)


def _attraction_score(item: dict[str, Any]) -> int:
    text = unicodedata.normalize("NFKC", " ".join([
        item["name"], *item["folders"], *item["entities"],
    ])).lower()
    if TOP_TIER.search(text):
        return 5
    if SECOND_TIER.search(text):
        return 4
    return 2


def _rank_key(item: dict[str, Any]) -> tuple[Any, ...]:
    preferred_type = 1 if item["extension"] in {"pdf", "xls", "xlsx", "csv", "ppt", "pptx"} else 0
    date_key = int(str(item["date"] or "").replace("-", "") or 0)
    return (-_attraction_score(item), -preferred_type, -date_key, item["name"], item["id"])


def direct_bucket_number(key: str, bucket_count: int) -> int:
    if not key or bucket_count < 1:
        raise CourseChatIndexError("Direct index key or bucket count is invalid")
    digest = hashlib.sha256(key.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % bucket_count


def _bucket_count(key_count: int) -> int:
    target = max(1, math.ceil(key_count / TARGET_KEYS_PER_BUCKET))
    return max(64, 1 << (target - 1).bit_length())


def build_direct_index(entries: dict[str, Any]) -> DirectIndex:
    """Build 12-byte BE slots into a compact collision-bucket data object."""

    if not entries or any(not isinstance(key, str) or not key for key in entries):
        raise CourseChatIndexError("Direct index entries are invalid")
    bucket_count = _bucket_count(len(entries))
    buckets: list[list[list[Any]]] = [[] for _ in range(bucket_count)]
    for key in sorted(entries):
        buckets[direct_bucket_number(key, bucket_count)].append([key, entries[key]])

    table = bytearray(bucket_count * SLOT_SIZE)
    data = bytearray()
    for bucket_number, bucket in enumerate(buckets):
        if not bucket:
            continue
        encoded = _compact_json(bucket)
        if len(encoded) > MAX_BUCKET_BYTES:
            raise CourseChatIndexError("Direct index collision bucket exceeds the byte limit")
        offset = len(data)
        data.extend(encoded)
        struct.pack_into(">QI", table, bucket_number * SLOT_SIZE, offset, len(encoded))
    if len(data) > MAX_LOOKUP_DATA_BYTES:
        raise CourseChatIndexError("Direct index data exceeds the byte limit")
    return DirectIndex(bytes(table), bytes(data), bucket_count, len(entries))


def direct_index_lookup(index: DirectIndex, key: str) -> Any | None:
    """Reference reader used by tests; production performs the same two ranges."""

    bucket = direct_bucket_number(key, index.bucket_count)
    offset, length = struct.unpack_from(">QI", index.table, bucket * SLOT_SIZE)
    if not length:
        return None
    entries = json.loads(index.data[offset:offset + length])
    for exact_key, value in entries:
        if exact_key == key:
            return value
    return None


def _descriptor(index: DirectIndex, table_key: str, data_key: str) -> dict[str, Any]:
    return {
        "table_key": table_key,
        "data_key": data_key,
        "bucket_count": index.bucket_count,
        "slot_size": SLOT_SIZE,
        "hash": "sha256-first64-be-mod",
        "table_bytes": len(index.table),
        "data_bytes": len(index.data),
        "max_bucket_bytes": MAX_BUCKET_BYTES,
        "table_sha256": hashlib.sha256(index.table).hexdigest(),
        "data_sha256": hashlib.sha256(index.data).hexdigest(),
    }


def build_course_chat_lookup(payload: dict[str, Any]) -> CourseChatLookup:
    """Build revisioned token/item objects and a manifest published last."""

    selected = build_course_chat_index(payload)
    items = list(selected["items"])
    items_by_id = {item["id"]: item for item in items}
    ranked = sorted(items, key=_rank_key)

    postings: dict[str, list[str]] = {}
    for item in ranked:
        for token in _item_tokens(item):
            token_postings = postings.setdefault(token, [])
            if len(token_postings) < POSTING_LIMIT:
                token_postings.append(item["id"])
    if not postings or len(postings) > MAX_LOOKUP_TOKENS:
        raise CourseChatIndexError("Course Chat lookup token count is invalid")

    token_index = build_direct_index(postings)
    item_index = build_direct_index(items_by_id)
    content_digest = hashlib.sha256(
        token_index.table + token_index.data + item_index.table + item_index.data
    ).hexdigest()
    revision = content_digest[:16]
    revision_prefix = f"{LOOKUP_PREFIX}/{revision}"
    token_table_key = f"{revision_prefix}/token-table.bin"
    token_data_key = f"{revision_prefix}/token-data.bin"
    item_table_key = f"{revision_prefix}/item-table.bin"
    item_data_key = f"{revision_prefix}/item-data.bin"
    objects = {
        token_table_key: token_index.table,
        token_data_key: token_index.data,
        item_table_key: item_index.table,
        item_data_key: item_index.data,
    }
    manifest = {
        "schema_version": LOOKUP_SCHEMA_VERSION,
        "format": LOOKUP_FORMAT,
        "generated_at": selected.get("generated_at", ""),
        "revision": revision,
        "normalization": LOOKUP_NORMALIZATION,
        "max_query_tokens": MAX_QUERY_TOKENS,
        "max_candidates": MAX_CANDIDATES,
        "posting_limit": POSTING_LIMIT,
        "item_count": len(items),
        "token_count": len(postings),
        "course_count": len({item["course_id"] for item in items}),
        "token_index": _descriptor(token_index, token_table_key, token_data_key),
        "item_index": _descriptor(item_index, item_table_key, item_data_key),
        "default_items": ranked[:MAX_CANDIDATES],
    }
    if manifest["course_count"] != len(ALLOWED_COURSE_IDS):
        raise CourseChatIndexError("Course Chat lookup does not cover every course")
    return CourseChatLookup(revision=revision, objects=objects, manifest=manifest)


def iter_course_chat_lookup_objects(lookup: CourseChatLookup) -> Iterable[tuple[str, bytes]]:
    """Yield immutable objects only; callers must publish the manifest last."""

    yield from lookup.objects.items()


def serialize_course_chat_lookup_manifest(lookup: CourseChatLookup) -> bytes:
    output = _compact_json(lookup.manifest)
    if len(output) > MAX_LOOKUP_MANIFEST_BYTES:
        raise CourseChatIndexError("Course Chat lookup manifest exceeds the byte limit")
    return output
