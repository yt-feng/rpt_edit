#!/usr/bin/env python3
"""Derive the bounded private Course Chat retrieval index.

The input to this module must already be the publisher's sanitized, flat
directory payload.  The derived index is only a deterministic subset of those
allow-listed rows: every row with a public notable entity is retained, then up
to thirty neutral rows per course are retained in source order.
"""

from __future__ import annotations

import json
from typing import Any


SCHEMA_VERSION = 1
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
    "alt-01", "alt-02", "alt-03",
})

ROW_FIELDS = frozenset({
    "id",
    "course_id",
    "name",
    "folders",
    "extension",
    "size_label",
    "date",
    "entities",
})


class CourseChatIndexError(ValueError):
    """Raised when a safe directory cannot produce a bounded chat index."""


def serialize_course_chat_index(payload: dict[str, Any]) -> bytes:
    """Serialize a derived index and enforce the Worker byte ceiling."""

    output = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    if len(output) > MAX_CHAT_INDEX_BYTES:
        raise CourseChatIndexError("Course Chat index exceeds the byte limit")
    return output


def build_course_chat_index(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a stable, bounded subset of a sanitized course directory.

    Entity-bearing rows are mandatory.  For discovery breadth, the first
    thirty entity-free rows for every course are also selected.  Selection and
    output both follow the original row order, making repeated builds from the
    same input byte-for-byte deterministic.
    """

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
