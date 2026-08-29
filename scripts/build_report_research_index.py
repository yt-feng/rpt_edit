#!/usr/bin/env python3
"""Build and atomically publish KCDesk's private research-evidence index.

The index is deliberately random-access. Query tokens resolve to bounded report
postings and relevant chunk ids; report metadata and evidence chunks are then
fetched by exact key. Only public report metadata is copied into the index.
Private source paths, PDF object keys, filenames, and storage locators are never
published.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import itertools
import json
import os
import re
import sqlite3
import struct
import tempfile
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator
from urllib.parse import quote

import build_report_chat_index as chat_index


SCHEMA_VERSION = 1
BUILD_FORMAT = b"report-research-random-access-v1.2\0"
DEFAULT_PREFIX = "_report-research/v1"
CORPUS_FILENAME = "corpus.jsonl.gz"
SLOT_SIZE = 12
QUERY_TOKEN_LIMIT = 8
REPORT_LIMIT = 8
POSTING_LIMIT = 48
EVIDENCE_CHUNKS_PER_REPORT = 2
MAX_BUCKET_ENTRIES = 8
MAX_BUCKET_BYTES = 128 * 1024
DEFAULT_CHUNK_CHARS = 1800
DEFAULT_CHUNK_OVERLAP = 180
# The current search-index builder has a clean gap between title-only rows
# (<=216 chars) and extracted report text (>=1,223 chars). This guard prevents
# a catalog title from being mislabeled as full-text evidence.
DEFAULT_MIN_TEXT_CHARS = 1000
MAX_MANIFEST_BYTES = 128 * 1024
MAX_CORPUS_COMPRESSED_BYTES = 2 * 1024 * 1024 * 1024
MAX_CORPUS_UNCOMPRESSED_BYTES = 8 * 1024 * 1024 * 1024
MAX_CORPUS_LINE_BYTES = 32 * 1024 * 1024
CORPUS_ITEM_FIELDS = frozenset({
    "id",
    "title",
    "title_en",
    "institution",
    "industry",
    "date_folder",
    "page_count",
    "available",
    "attraction_score",
    "public_url",
})
TABLE_FILES = {
    "token_table": ("tokens.tbl", "tokens.dat"),
    "item_table": ("items.tbl", "items.dat"),
    "evidence_table": ("evidence.tbl", "evidence.dat"),
}
LATIN_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9.+&-]*")
CJK_RUN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+")
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]+")
BOUNDARY_RE = re.compile(r"[.!?;:\u3002\uff01\uff1f\uff1b\uff1a]\s|。|！|？|；|：")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")


class CorpusError(RuntimeError):
    """The stable private corpus could not be authenticated or decoded."""


def body_text(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or ""))
    text = CONTROL_RE.sub(" ", text)
    return " ".join(text.split()).strip()


def iter_search_tokens(value: Any) -> Iterator[str]:
    """Yield exact index tokens while preserving term frequency."""
    raw = unicodedata.normalize("NFKC", str(value or "")).lower()
    for token in LATIN_TOKEN_RE.findall(raw):
        if 2 <= len(token) <= 64:
            yield token
    for run in CJK_RUN_RE.findall(raw):
        if 2 <= len(run) <= 8:
            yield run
        for width in (2, 3, 4):
            if len(run) < width:
                continue
            for offset in range(len(run) - width + 1):
                yield run[offset : offset + width]


def split_chunks(text: str, max_chars: int, overlap_chars: int) -> list[dict[str, str]]:
    if max_chars < 64:
        raise ValueError("chunk size must be at least 64 characters")
    if overlap_chars < 0 or overlap_chars >= max_chars // 2:
        raise ValueError("chunk overlap must be non-negative and less than half the chunk size")
    clean = body_text(text)
    if not clean:
        return []

    chunks: list[dict[str, str]] = []
    start = 0
    while start < len(clean):
        hard_end = min(len(clean), start + max_chars)
        end = hard_end
        if hard_end < len(clean):
            floor = start + max_chars * 3 // 5
            candidates = [match.end() for match in BOUNDARY_RE.finditer(clean, floor, hard_end)]
            if candidates:
                end = candidates[-1]
            else:
                whitespace = clean.rfind(" ", floor, hard_end)
                if whitespace > start:
                    end = whitespace
        chunk = clean[start:end].strip()
        if chunk:
            chunks.append({"id": f"c{len(chunks):06d}", "text": chunk})
        if end >= len(clean):
            break
        next_start = max(start + 1, end - overlap_chars)
        while next_start < len(clean) and clean[next_start].isspace():
            next_start += 1
        start = next_start
    return chunks


def valid_prefix(value: str) -> str:
    prefix = str(value or "").strip().strip("/")
    if not prefix or not re.fullmatch(r"[A-Za-z0-9_./-]+", prefix) or ".." in prefix.split("/"):
        raise ValueError("invalid private index prefix")
    return prefix


def public_research_item(report: dict[str, Any], chunk_count: int) -> dict[str, Any] | None:
    item = chat_index.public_item(report)
    if item is None:
        return None
    report_id = item["id"]
    return {
        **item,
        "public_url": f"/report.html?id={quote(report_id, safe='')}",
        "chunk_count": chunk_count,
    }


def _json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def corpus_public_item(item: dict[str, Any]) -> dict[str, Any]:
    """Return the strict public-metadata allowlist persisted with full text."""
    return {key: item[key] for key in sorted(CORPUS_ITEM_FIELDS)}


def _validated_corpus_item(value: Any, expected_id: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != CORPUS_ITEM_FIELDS:
        raise CorpusError("stable research corpus item metadata is outside the public allowlist")
    report_id = str(value.get("id") or "").strip().lower()
    if report_id != expected_id or not chat_index.CATALOG_ID_RE.fullmatch(report_id):
        raise CorpusError("stable research corpus report id is invalid")
    limits = {
        "title": 500,
        "title_en": 500,
        "institution": 160,
        "industry": 160,
        "date_folder": 40,
    }
    item: dict[str, Any] = {"id": report_id}
    for key, limit in limits.items():
        raw = value.get(key)
        clean = chat_index.compact_text(raw, limit)
        if not isinstance(raw, str) or raw != clean:
            raise CorpusError(f"stable research corpus {key} is invalid")
        item[key] = clean
    page_count = value.get("page_count")
    if isinstance(page_count, bool) or not isinstance(page_count, int) or not 0 <= page_count <= 100_000:
        raise CorpusError("stable research corpus page count is invalid")
    attraction_score = value.get("attraction_score")
    if isinstance(attraction_score, bool) or not isinstance(attraction_score, int) or not 1 <= attraction_score <= 5:
        raise CorpusError("stable research corpus attraction score is invalid")
    available = value.get("available")
    if not isinstance(available, bool):
        raise CorpusError("stable research corpus availability is invalid")
    public_url = value.get("public_url")
    expected_url = f"/report.html?id={quote(report_id, safe='')}"
    if public_url != expected_url:
        raise CorpusError("stable research corpus public URL is invalid")
    item.update({
        "page_count": page_count,
        "available": available,
        "attraction_score": attraction_score,
        "public_url": expected_url,
    })
    return item


def decode_corpus(payload: bytes) -> tuple[dict[str, dict[str, Any]], int]:
    if len(payload) > MAX_CORPUS_COMPRESSED_BYTES:
        raise CorpusError("stable research corpus exceeds the compressed-size limit")
    rows: dict[str, dict[str, Any]] = {}
    uncompressed_bytes = 0
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(payload), mode="rb") as compressed:
            for line_number, raw_line in enumerate(compressed, start=1):
                uncompressed_bytes += len(raw_line)
                if uncompressed_bytes > MAX_CORPUS_UNCOMPRESSED_BYTES:
                    raise CorpusError("stable research corpus exceeds the uncompressed-size limit")
                if not raw_line or len(raw_line) > MAX_CORPUS_LINE_BYTES or not raw_line.endswith(b"\n"):
                    raise CorpusError(f"stable research corpus line {line_number} is invalid")
                try:
                    row = json.loads(raw_line)
                except (UnicodeDecodeError, json.JSONDecodeError) as error:
                    raise CorpusError(f"stable research corpus line {line_number} is not JSON") from error
                if not isinstance(row, dict) or set(row) != {"id", "item", "text"}:
                    raise CorpusError(f"stable research corpus line {line_number} has invalid fields")
                report_id = str(row.get("id") or "").strip().lower()
                if not chat_index.CATALOG_ID_RE.fullmatch(report_id) or report_id in rows:
                    raise CorpusError(f"stable research corpus line {line_number} has an invalid report id")
                text = row.get("text")
                clean_text = body_text(text)
                if not isinstance(text, str) or not clean_text or text != clean_text:
                    raise CorpusError(f"stable research corpus line {line_number} has invalid full text")
                rows[report_id] = {
                    "id": report_id,
                    "item": _validated_corpus_item(row.get("item"), report_id),
                    "text": clean_text,
                }
    except CorpusError:
        raise
    except (EOFError, OSError, gzip.BadGzipFile) as error:
        raise CorpusError("stable research corpus gzip payload is damaged") from error
    return rows, uncompressed_bytes


def read_corpus(path: Path) -> dict[str, dict[str, Any]]:
    rows, _uncompressed_bytes = decode_corpus(path.read_bytes())
    return rows


def write_corpus(rows: dict[str, dict[str, Any]], path: Path) -> dict[str, Any]:
    uncompressed_bytes = 0
    with path.open("wb") as raw_file:
        with gzip.GzipFile(filename="", mode="wb", compresslevel=9, fileobj=raw_file, mtime=0) as compressed:
            for report_id in sorted(rows):
                line = _json_bytes(rows[report_id]) + b"\n"
                if len(line) > MAX_CORPUS_LINE_BYTES:
                    raise CorpusError("research corpus contains an oversized report row")
                uncompressed_bytes += len(line)
                if uncompressed_bytes > MAX_CORPUS_UNCOMPRESSED_BYTES:
                    raise CorpusError("research corpus exceeds the uncompressed-size limit")
                compressed.write(line)
    payload = path.read_bytes()
    if not payload or len(payload) > MAX_CORPUS_COMPRESSED_BYTES:
        raise CorpusError("research corpus exceeds the compressed-size limit")
    return {
        "format": "jsonl",
        "content_encoding": "gzip",
        "bytes": len(payload),
        "uncompressed_bytes": uncompressed_bytes,
        "sha256": hashlib.sha256(payload).hexdigest(),
        "item_count": len(rows),
    }


def load_stable_corpus(
    client: Any,
    bucket: str,
    prefix: str = DEFAULT_PREFIX,
) -> dict[str, dict[str, Any]]:
    """Load the last committed corpus or fail before any new object is written."""
    prefix = valid_prefix(prefix)
    manifest_key = f"{prefix}/manifest.json"
    try:
        response = client.get_object(Bucket=bucket, Key=manifest_key)
    except Exception as error:
        if _not_found(error):
            return {}
        raise CorpusError("stable research manifest could not be read") from error
    if not response:
        return {}
    try:
        manifest_bytes = response["Body"].read()
    except Exception as error:
        raise CorpusError("stable research manifest body could not be read") from error
    if len(manifest_bytes) > MAX_MANIFEST_BYTES:
        raise CorpusError("stable research manifest exceeds the size limit")
    try:
        manifest = json.loads(manifest_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CorpusError("stable research manifest is damaged") from error
    if not isinstance(manifest, dict) or manifest.get("index_kind") != "report-research-random-access":
        raise CorpusError("stable research manifest kind is invalid")
    descriptor = manifest.get("corpus")
    # Backward-compatible first durable build: the earlier research schema had
    # no corpus at all, so there is no historical text it could preserve.
    if descriptor is None:
        if manifest.get("corpus_durability"):
            raise CorpusError("stable research manifest lost its durable corpus descriptor")
        return {}
    if not isinstance(descriptor, dict):
        raise CorpusError("stable research corpus descriptor is invalid")
    key = str(descriptor.get("key") or "")
    digest = str(descriptor.get("sha256") or "").lower()
    size = descriptor.get("bytes")
    uncompressed_size = descriptor.get("uncompressed_bytes")
    item_count = descriptor.get("item_count")
    if (
        not key.startswith(f"{prefix}/releases/")
        or not key.endswith(f"/{CORPUS_FILENAME}")
        or ".." in key.split("/")
        or descriptor.get("format") != "jsonl"
        or descriptor.get("content_encoding") != "gzip"
        or not SHA256_RE.fullmatch(digest)
        or isinstance(size, bool)
        or not isinstance(size, int)
        or not 0 < size <= MAX_CORPUS_COMPRESSED_BYTES
        or isinstance(uncompressed_size, bool)
        or not isinstance(uncompressed_size, int)
        or not 0 < uncompressed_size <= MAX_CORPUS_UNCOMPRESSED_BYTES
        or isinstance(item_count, bool)
        or not isinstance(item_count, int)
        or item_count < 1
    ):
        raise CorpusError("stable research corpus descriptor is invalid")
    try:
        corpus_response = client.get_object(Bucket=bucket, Key=key)
        payload = corpus_response["Body"].read()
    except Exception as error:
        raise CorpusError("stable research corpus object could not be read") from error
    if len(payload) != size or hashlib.sha256(payload).hexdigest() != digest:
        raise CorpusError("stable research corpus object failed integrity verification")
    rows, measured_uncompressed_bytes = decode_corpus(payload)
    if len(rows) != item_count or measured_uncompressed_bytes != uncompressed_size:
        raise CorpusError("stable research corpus counts do not match the committed manifest")
    return rows


def merge_corpus_rows(
    catalog_by_id: dict[str, dict[str, Any]],
    search_by_id: dict[str, str],
    previous_rows: dict[str, dict[str, Any]],
    min_text_chars: int,
) -> tuple[dict[str, dict[str, Any]], int, int]:
    merged: dict[str, dict[str, Any]] = {}
    for report_id in sorted(previous_rows):
        row = previous_rows[report_id]
        if not isinstance(row, dict) or set(row) != {"id", "item", "text"}:
            raise CorpusError("previous research corpus row is invalid")
        if row.get("id") != report_id:
            raise CorpusError("previous research corpus key does not match its report id")
        merged[report_id] = {
            "id": report_id,
            "item": _validated_corpus_item(row.get("item"), report_id),
            "text": body_text(row.get("text")),
        }
        if not merged[report_id]["text"]:
            raise CorpusError("previous research corpus contains empty full text")

    current_full_text_count = 0
    for report_id in sorted(catalog_by_id):
        current_item = public_research_item(catalog_by_id[report_id], 0)
        if current_item is None:
            continue
        public_item = corpus_public_item(current_item)
        current_text = search_by_id.get(report_id, "")
        if len(current_text) >= min_text_chars:
            merged[report_id] = {"id": report_id, "item": public_item, "text": current_text}
            current_full_text_count += 1
        elif report_id in merged:
            merged[report_id]["item"] = public_item
    retained_from_previous_count = len(merged) - current_full_text_count
    return merged, current_full_text_count, retained_from_previous_count


def _choose_bucket_count(key_count: int, requested: int | None) -> int:
    return chat_index.choose_bucket_count(key_count, requested)


def _bucket_index(key: str, bucket_count: int) -> int:
    return chat_index.bucket_index(key, bucket_count)


def _create_store(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA journal_mode=OFF")
    connection.execute("PRAGMA synchronous=OFF")
    connection.execute("PRAGMA temp_store=FILE")
    connection.execute(
        "CREATE TABLE postings ("
        "token TEXT NOT NULL, report_id TEXT NOT NULL, tf INTEGER NOT NULL, chunks TEXT NOT NULL, "
        "PRIMARY KEY (token, report_id)) WITHOUT ROWID"
    )
    connection.execute(
        "CREATE TABLE raw_entries ("
        "table_name TEXT NOT NULL, exact_key TEXT NOT NULL, value_json BLOB NOT NULL, "
        "PRIMARY KEY (table_name, exact_key)) WITHOUT ROWID"
    )
    connection.execute(
        "CREATE TABLE bucket_entries ("
        "table_name TEXT NOT NULL, bucket INTEGER NOT NULL, exact_key TEXT NOT NULL, value_json BLOB NOT NULL, "
        "PRIMARY KEY (table_name, bucket, exact_key)) WITHOUT ROWID"
    )
    return connection


def _store_raw_entry(connection: sqlite3.Connection, table_name: str, exact_key: str, value: Any) -> None:
    connection.execute(
        "INSERT INTO raw_entries(table_name, exact_key, value_json) VALUES (?, ?, ?)",
        (table_name, exact_key, _json_bytes(value)),
    )


def _store_report_postings(
    connection: sqlite3.Connection,
    report_id: str,
    chunks: list[dict[str, str]],
) -> None:
    stats: dict[str, list[Any]] = {}
    for chunk in chunks:
        counts = Counter(iter_search_tokens(chunk["text"]))
        for token, count in counts.items():
            current = stats.get(token)
            if current is None:
                stats[token] = [count, [(count, chunk["id"])]]
            else:
                current[0] += count
                current[1].append((count, chunk["id"]))

    rows = []
    for token in sorted(stats):
        term_frequency, chunk_scores = stats[token]
        top_chunks = [
            chunk_id
            for _count, chunk_id in sorted(chunk_scores, key=lambda row: (-row[0], row[1]))[
                :EVIDENCE_CHUNKS_PER_REPORT
            ]
        ]
        rows.append((token, report_id, min(int(term_frequency), 65535), json.dumps(top_chunks, separators=(",", ":"))))
    connection.executemany(
        "INSERT INTO postings(token, report_id, tf, chunks) VALUES (?, ?, ?, ?)",
        rows,
    )


def _populate_hashed_raw_entries(
    connection: sqlite3.Connection,
    table_name: str,
    bucket_count: int,
) -> None:
    rows = connection.execute(
        "SELECT exact_key, value_json FROM raw_entries WHERE table_name = ? ORDER BY exact_key",
        (table_name,),
    )
    connection.executemany(
        "INSERT INTO bucket_entries(table_name, bucket, exact_key, value_json) VALUES (?, ?, ?, ?)",
        (
            (table_name, _bucket_index(exact_key, bucket_count), exact_key, value_json)
            for exact_key, value_json in rows
        ),
    )


def _populate_token_entries(
    connection: sqlite3.Connection,
    bucket_count: int,
) -> int:
    cursor = connection.execute(
        "SELECT token, report_id, tf, chunks FROM postings ORDER BY token, tf DESC, report_id"
    )
    token_count = 0
    for token, group in itertools.groupby(cursor, key=lambda row: row[0]):
        postings = []
        for _token, report_id, term_frequency, chunks_json in itertools.islice(group, POSTING_LIMIT):
            postings.append({
                "id": report_id,
                "tf": int(term_frequency),
                "chunks": json.loads(chunks_json),
            })
        # islice leaves the remaining rows in this group unread. Consume them so
        # itertools.groupby can advance safely to the next exact token.
        for _unused in group:
            pass
        connection.execute(
            "INSERT INTO bucket_entries(table_name, bucket, exact_key, value_json) VALUES (?, ?, ?, ?)",
            ("token_table", _bucket_index(token, bucket_count), token, _json_bytes(postings)),
        )
        token_count += 1
    return token_count


def _encoded_bucket(entries: list[tuple[str, bytes]]) -> bytes:
    parts = []
    for exact_key, raw_value in entries:
        key_json = json.dumps(exact_key, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        parts.append(b"[" + key_json + b"," + raw_value + b"]")
    return b"[" + b",".join(parts) + b"]"


def _write_bucket_table(
    connection: sqlite3.Connection,
    table_name: str,
    bucket_count: int,
    table_path: Path,
    data_path: Path,
) -> dict[str, int]:
    cursor = connection.execute(
        "SELECT bucket, exact_key, value_json FROM bucket_entries "
        "WHERE table_name = ? ORDER BY bucket, exact_key",
        (table_name,),
    )
    next_row = next(cursor, None)
    data_offset = 0
    largest_bucket = 0
    max_bucket_bytes = 0
    with table_path.open("wb") as table_file, data_path.open("wb") as data_file:
        for bucket_number in range(bucket_count):
            bucket_entries: list[tuple[str, bytes]] = []
            while next_row is not None and int(next_row[0]) == bucket_number:
                raw_value = next_row[2]
                if isinstance(raw_value, str):
                    raw_value = raw_value.encode("utf-8")
                bucket_entries.append((str(next_row[1]), bytes(raw_value)))
                next_row = next(cursor, None)
            if not bucket_entries:
                table_file.write(struct.pack(">QI", 0, 0))
                continue
            payload = _encoded_bucket(bucket_entries)
            if len(payload) > MAX_BUCKET_BYTES:
                raise ValueError(f"one {table_name} bucket exceeds the Worker range-read limit")
            table_file.write(struct.pack(">QI", data_offset, len(payload)))
            data_file.write(payload)
            data_offset += len(payload)
            largest_bucket = max(largest_bucket, len(bucket_entries))
            max_bucket_bytes = max(max_bucket_bytes, len(payload))
    if next_row is not None:
        raise AssertionError("bucket entry is outside the configured table")
    if table_path.stat().st_size != bucket_count * SLOT_SIZE:
        raise AssertionError("invalid fixed-slot table size")
    return {
        "bucket_count": bucket_count,
        "slot_size": SLOT_SIZE,
        "data_bytes": data_offset,
        "largest_bucket": largest_bucket,
        "max_bucket_bytes": max(16, max_bucket_bytes),
    }


def build_index(
    catalog_path: Path,
    search_index_path: Path,
    output_dir: Path,
    prefix: str = DEFAULT_PREFIX,
    *,
    token_bucket_count: int | None = None,
    item_bucket_count: int | None = None,
    evidence_bucket_count: int | None = None,
    chunk_chars: int = DEFAULT_CHUNK_CHARS,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    min_text_chars: int = DEFAULT_MIN_TEXT_CHARS,
    previous_corpus: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    raw_catalog = catalog_path.read_bytes()
    raw_search_index = search_index_path.read_bytes()
    catalog = json.loads(raw_catalog)
    search_index = json.loads(raw_search_index)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("items"), list):
        raise ValueError("catalog must contain an items array")
    if not isinstance(search_index, dict) or not isinstance(search_index.get("items"), list):
        raise ValueError("search index must contain an items array")
    if min_text_chars < 1:
        raise ValueError("minimum full-text length must be positive")
    prefix = valid_prefix(prefix)
    # Validate the chunking contract before doing any material work.
    split_chunks("validation text", chunk_chars, chunk_overlap)

    catalog_by_id: dict[str, dict[str, Any]] = {}
    for report in catalog["items"]:
        if not isinstance(report, dict):
            continue
        report_id = str(report.get("id") or "").strip().lower()
        if chat_index.CATALOG_ID_RE.fullmatch(report_id) and report_id not in catalog_by_id:
            catalog_by_id[report_id] = report

    search_by_id: dict[str, str] = {}
    for row in search_index["items"]:
        if not isinstance(row, dict):
            continue
        report_id = str(row.get("id") or "").strip().lower()
        if report_id not in catalog_by_id:
            continue
        text = body_text(row.get("text"))
        current = search_by_id.get(report_id, "")
        # The longest duplicate is the most complete extraction. Lexical order
        # breaks equal-length ties so input ordering cannot change the release.
        if (len(text), text) > (len(current), current):
            search_by_id[report_id] = text

    corpus_rows, _current_full_text_count, _retained_from_previous_count = merge_corpus_rows(
        catalog_by_id,
        search_by_id,
        previous_corpus or {},
        min_text_chars,
    )
    if not corpus_rows:
        raise ValueError("search index and stable corpus produced no full-text research items")

    output_dir.mkdir(parents=True, exist_ok=True)
    # Hash only fields that can change the generated index. Catalog refresh
    # timestamps, private paths, and other operational metadata must not force
    # a second immutable 100+ MiB release when the research evidence is
    # byte-for-byte unchanged.
    release_digest = hashlib.sha256(BUILD_FORMAT + struct.pack(">III", chunk_chars, chunk_overlap, min_text_chars))
    for report_id in sorted(corpus_rows):
        value = _json_bytes(corpus_rows[report_id])
        release_digest.update(struct.pack(">Q", len(value)))
        release_digest.update(value)
    release = release_digest.hexdigest()[:32]
    release_prefix = f"{prefix}/releases/{release}"
    corpus_path = output_dir / CORPUS_FILENAME
    corpus_manifest = {
        "key": f"{release_prefix}/{CORPUS_FILENAME}",
        **write_corpus(corpus_rows, corpus_path),
    }

    temp_handle = tempfile.NamedTemporaryFile(prefix="report-research-", suffix=".sqlite3", dir=output_dir, delete=False)
    temp_handle.close()
    store_path = Path(temp_handle.name)
    connection = _create_store(store_path)
    item_count = 0
    evidence_count = 0
    try:
        for report_id in sorted(corpus_rows):
            row = corpus_rows[report_id]
            text = row["text"]
            chunks = split_chunks(text, chunk_chars, chunk_overlap)
            if not chunks:
                raise CorpusError("merged research corpus produced an empty evidence row")
            item = {**row["item"], "chunk_count": len(chunks)}
            _store_raw_entry(connection, "item_table", report_id, item)
            for chunk in chunks:
                evidence_key = f"{report_id}:{chunk['id']}"
                evidence = {
                    "id": chunk["id"],
                    "report_id": report_id,
                    "text": chunk["text"],
                    "source": {
                        "report_id": report_id,
                        "public_url": item["public_url"],
                    },
                }
                _store_raw_entry(connection, "evidence_table", evidence_key, evidence)
                evidence_count += 1
            _store_report_postings(connection, report_id, chunks)
            item_count += 1
            if item_count % 25 == 0:
                connection.commit()
        connection.commit()

        if not item_count:
            raise ValueError("search index produced no full-text research items")
        token_count = int(connection.execute("SELECT COUNT(DISTINCT token) FROM postings").fetchone()[0])
        if not token_count:
            raise ValueError("full-text research items produced no search tokens")

        bucket_counts = {
            "token_table": _choose_bucket_count(token_count, token_bucket_count),
            "item_table": _choose_bucket_count(item_count, item_bucket_count),
            "evidence_table": _choose_bucket_count(evidence_count, evidence_bucket_count),
        }
        _populate_token_entries(connection, bucket_counts["token_table"])
        _populate_hashed_raw_entries(connection, "item_table", bucket_counts["item_table"])
        _populate_hashed_raw_entries(connection, "evidence_table", bucket_counts["evidence_table"])
        connection.commit()

        table_manifests: dict[str, dict[str, Any]] = {}
        for table_name, (table_filename, data_filename) in TABLE_FILES.items():
            stats = _write_bucket_table(
                connection,
                table_name,
                bucket_counts[table_name],
                output_dir / table_filename,
                output_dir / data_filename,
            )
            table_manifests[table_name] = {
                "table_key": f"{release_prefix}/{table_filename}",
                "data_key": f"{release_prefix}/{data_filename}",
                **stats,
            }

        manifest: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "index_kind": "report-research-random-access",
            "release": release,
            "normalization": "nfkc-lower-alnum-cjk234-v1",
            "hash": "sha256-first8-be",
            "query_token_limit": QUERY_TOKEN_LIMIT,
            "report_limit": REPORT_LIMIT,
            "posting_limit": POSTING_LIMIT,
            "evidence_chunks_per_report": EVIDENCE_CHUNKS_PER_REPORT,
            "item_count": item_count,
            "chunk_count": evidence_count,
            "token_count": token_count,
            "chunking": {
                "max_chars": chunk_chars,
                "overlap_chars": chunk_overlap,
                "min_full_text_chars": min_text_chars,
            },
            "source_contract": "report-id-and-public-url-only",
            "corpus_durability": "append-only-merge-v1",
            "corpus": corpus_manifest,
            **table_manifests,
        }
        (output_dir / "manifest.json").write_bytes(_json_bytes(manifest))
        return manifest
    finally:
        connection.close()
        store_path.unlink(missing_ok=True)


def _not_found(error: Exception) -> bool:
    return chat_index._not_found(error)


def publish_index(client: Any, bucket: str, output_dir: Path, prefix: str = DEFAULT_PREFIX) -> dict[str, Any]:
    manifest_bytes = (output_dir / "manifest.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    corpus_descriptor = manifest.get("corpus") or {}
    corpus_path = output_dir / CORPUS_FILENAME
    corpus_body = corpus_path.read_bytes()
    corpus_key = str(corpus_descriptor.get("key") or "")
    expected_release_prefix = f"{valid_prefix(prefix)}/releases/{manifest.get('release')}/"
    if (
        not corpus_key.startswith(expected_release_prefix)
        or not corpus_key.endswith(f"/{CORPUS_FILENAME}")
        or ".." in corpus_key.split("/")
        or int(corpus_descriptor.get("bytes") or -1) != len(corpus_body)
        or corpus_descriptor.get("sha256") != hashlib.sha256(corpus_body).hexdigest()
    ):
        raise RuntimeError("Report Research corpus does not match its manifest descriptor")
    immutable_files: list[tuple[Path, str, str]] = [
        (corpus_path, corpus_key, "application/gzip"),
    ]
    for name in TABLE_FILES:
        descriptor = manifest[name]
        immutable_files.extend((
            (output_dir / Path(descriptor["table_key"]).name, descriptor["table_key"], "application/octet-stream"),
            (output_dir / Path(descriptor["data_key"]).name, descriptor["data_key"], "application/json"),
        ))

    for path, key, content_type in immutable_files:
        body = path.read_bytes()
        digest = hashlib.sha256(body).hexdigest()
        try:
            current = client.head_object(Bucket=bucket, Key=key)
        except Exception as error:
            if not _not_found(error):
                raise
            current = None
        if current is not None:
            metadata = current.get("Metadata") or {}
            if int(current.get("ContentLength", -1)) != len(body) or metadata.get("sha256") != digest:
                raise RuntimeError("immutable Report Research index object does not match its release")
        else:
            client.put_object(
                Bucket=bucket,
                Key=key,
                Body=body,
                ContentType=content_type,
                CacheControl="private, no-store",
                Metadata={"sha256": digest},
            )
            stored = client.head_object(Bucket=bucket, Key=key)
            if int(stored.get("ContentLength", -1)) != len(body):
                raise RuntimeError("Report Research index object length verification failed")

    manifest_key = f"{valid_prefix(prefix)}/manifest.json"
    manifest_digest = hashlib.sha256(manifest_bytes).hexdigest()
    client.put_object(
        Bucket=bucket,
        Key=manifest_key,
        Body=manifest_bytes,
        ContentType="application/json",
        CacheControl="private, no-store",
        Metadata={"sha256": manifest_digest},
    )
    committed = client.get_object(Bucket=bucket, Key=manifest_key)["Body"].read()
    if committed != manifest_bytes:
        raise RuntimeError("Report Research manifest commit verification failed")
    return manifest


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog-path", type=Path, required=True)
    parser.add_argument("--search-index-path", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--r2-prefix", default=DEFAULT_PREFIX)
    parser.add_argument(
        "--merge-r2-corpus",
        action="store_true",
        help="Merge the last atomically committed private corpus before building",
    )
    parser.add_argument("--upload-r2", action="store_true")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    client = None
    bucket = ""
    previous_corpus: dict[str, dict[str, Any]] = {}
    if args.merge_r2_corpus or args.upload_r2:
        client = chat_index.build_r2_client()
        bucket = os.environ["R2_BUCKET"]
    if args.merge_r2_corpus:
        previous_corpus = load_stable_corpus(client, bucket, args.r2_prefix)
    manifest = build_index(
        args.catalog_path,
        args.search_index_path,
        args.output_dir,
        args.r2_prefix,
        previous_corpus=previous_corpus,
    )
    if args.upload_r2:
        publish_index(
            client,
            bucket,
            args.output_dir,
            args.r2_prefix,
        )
    total_bytes = sum(
        (args.output_dir / filename).stat().st_size
        for pair in TABLE_FILES.values()
        for filename in pair
    ) + (args.output_dir / CORPUS_FILENAME).stat().st_size
    print(
        f"report_research_release={manifest['release']} items={manifest['item_count']} "
        f"chunks={manifest['chunk_count']} tokens={manifest['token_count']} bytes={total_bytes} "
        f"published={str(args.upload_r2).lower()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
