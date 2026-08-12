#!/usr/bin/env python3
"""Build and atomically publish the private Report Chat random-access index.

The Worker reads one 12-byte table slot and one small JSON bucket per lookup.
No source paths, storage locators, filenames, or other catalog-private fields are
copied into the index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import struct
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 2
BUILD_FORMAT = b"report-chat-random-access-v2.1\0"
DEFAULT_PREFIX = "_report-chat/v2"
SLOT_SIZE = 12
QUERY_TOKEN_LIMIT = 8
CANDIDATE_LIMIT = 12
POSTING_LIMIT = 48
MAX_BUCKET_ENTRIES = 8
MAX_BUCKET_BYTES = 128 * 1024
TABLE_FILES = {
    "token_table": ("tokens.tbl", "tokens.dat"),
    "item_table": ("items.tbl", "items.dat"),
}
CATALOG_ID_RE = re.compile(r"^[a-f0-9]{24}$")
LATIN_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9.+&-]*")
CJK_RUN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+")
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]+")

INDUSTRY_RULES = (
    ("Macro / FX / Rates", re.compile(r"\b(macro|fx|foreign exchange|currency|cny|yuan|dollar|usd|rate|rates|yield|fed|ecb|boj|inflation|cpi|pmi|gdp|economy|economic|recession|treasury|bond|nominal|real rate)\b")),
    ("Equity Strategy", re.compile(r"\b(strategy|equity strategy|market strategy|asset allocation|portfolio|index|earnings revision|valuation|eps|target price)\b")),
    ("Tech / AI / Semis", re.compile(r"\b(ai|artificial intelligence|semiconductor|semis|chip|chips|memory|dram|nand|hbm|gpu|server|software|cloud|data center|datacenter|robot|robotics)\b")),
    ("Internet / Media", re.compile(r"\b(internet|media|gaming|game|music|streaming|advertising|ecommerce|e-commerce|platform|social|takeaway|food delivery|new media)\b")),
    ("Autos / EV / Batteries", re.compile(r"\b(auto|autos|automotive|vehicle|ev|bev|battery|batteries|lithium|ess|adas|mobility|tesla|byd)\b")),
    ("Energy / Utilities", re.compile(r"\b(energy|oil|gas|lng|solar|wind|power|utility|utilities|renewable|coal|electricity|grid)\b")),
    ("Metals / Mining", re.compile(r"\b(metal|metals|mining|copper|aluminum|aluminium|steel|iron ore|gold|silver|nickel|commodity|commodities)\b")),
    ("Healthcare / Biotech", re.compile(r"\b(healthcare|health care|biotech|pharma|pharmaceutical|drug|medical|hospital|medtech|vaccine|therapy)\b")),
    ("Consumer / Retail", re.compile(r"\b(consumer|retail|apparel|luxury|brand|restaurant|food|beverage|travel retail|staples|discretionary)\b")),
    ("Banks / Financials", re.compile(r"\b(bank|banks|banking|insurance|broker|brokerage|asset manager|fintech|exchange|financials|payment)\b")),
    ("Real Estate", re.compile(r"\b(real estate|property|housing|developer|reit|mortgage|homebuilder|construction)\b")),
    ("Industrials / Capex", re.compile(r"\b(industrial|industrials|machinery|automation|capex|capital goods|aerospace|defense|rail|shipping|logistics|transport)\b")),
    ("Policy / Geopolitics", re.compile(r"\b(policy|politics|geopolitic|geopolitical|tariff|trade war|election|sanction|iran|russia|taiwan|strait|security)\b")),
)

TOP_TIER_RE = re.compile(
    r"(?:^|[^a-z0-9])(?:jpm|jpmorgan|gs|goldman|ms|morgan stanley|bofa|bank of america|ubs|citi|citigroup|hsbc)(?=$|[^a-z0-9])"
    r"|摩根大通|高盛|摩根士丹利|美银|瑞银|花旗|汇丰|金杜|中伦|君合|国浩|证监会|上交所|深交所|最高人民法院"
)
SECOND_TIER_RE = re.compile(
    r"(?:^|[^a-z0-9])(?:nomura|bernstein|deutsche bank|barclays|macquarie|mckinsey|bcg|bain)(?=$|[^a-z0-9])"
    r"|野村|德银|巴克莱|麦肯锡|贝恩"
)


def compact_text(value: Any, limit: int) -> str:
    text = unicodedata.normalize("NFKC", str(value or ""))
    text = CONTROL_RE.sub(" ", text)
    return " ".join(text.split()).strip()[:limit]


def normalized_text(value: Any) -> str:
    value = unicodedata.normalize("NFKC", str(value or "")).lower()
    value = re.sub(r"[^\w\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+", " ", value)
    return " ".join(value.split())


def search_tokens(value: Any) -> set[str]:
    """Return indexable exact keys for Worker query-token lookups."""
    raw = unicodedata.normalize("NFKC", str(value or "")).lower()
    tokens = {token for token in LATIN_TOKEN_RE.findall(raw) if len(token) >= 2}
    for run in CJK_RUN_RE.findall(raw):
        if 2 <= len(run) <= 8:
            tokens.add(run)
        for width in (2, 3, 4):
            for offset in range(max(0, len(run) - width + 1)):
                tokens.add(run[offset : offset + width])
    return tokens


def report_industry(report: dict[str, Any]) -> str:
    explicit = report.get("industry") or report.get("sector") or report.get("category")
    if explicit:
        return compact_text(explicit, 80)
    text = normalized_text(" ".join(str(report.get(key) or "") for key in ("title", "title_zh", "filename")))
    for label, pattern in INDUSTRY_RULES:
        if pattern.search(text):
            return label
    return "Other"


def report_institution(report: dict[str, Any]) -> str:
    code = compact_text(report.get("bank_code"), 48)
    name = compact_text(report.get("bank_name"), 80)
    if code and name and normalized_text(code) != normalized_text(name):
        return f"{code} · {name}"
    return code or name or "Other"


def attraction_score(report: dict[str, Any]) -> int:
    text = normalized_text(" ".join(str(report.get(key) or "") for key in (
        "bank_code", "bank_name", "institution", "title", "title_zh",
    )))
    if TOP_TIER_RE.search(text):
        return 5
    if SECOND_TIER_RE.search(text):
        return 4
    return 2


def date_key(report: dict[str, Any]) -> str:
    candidates: list[Any] = [report.get("title"), report.get("filename"), report.get("date_folder"), report.get("date")]
    candidates.extend(report.get("date_folders") if isinstance(report.get("date_folders"), list) else [])
    for value in candidates:
        digits = re.sub(r"[^0-9]", "", str(value or ""))
        match = re.search(r"((?:20)?\d{6})$", digits)
        token = match.group(1) if match else digits
        if len(token) == 6:
            token = f"20{token}"
        if re.fullmatch(r"20\d{6}", token):
            return token
    return ""


def public_item(report: dict[str, Any]) -> dict[str, Any] | None:
    report_id = str(report.get("id") or "").strip().lower()
    if not CATALOG_ID_RE.fullmatch(report_id):
        return None
    title = compact_text(report.get("title_zh") or report.get("title") or "Untitled report", 500)
    title_en = compact_text(report.get("title") or report.get("title_zh") or "Untitled report", 500)
    if title_en.lower().endswith(".pdf"):
        title_en = title_en[:-4].rstrip()
    pages = report.get("page_count")
    try:
        page_count = max(0, int(float(pages or 0)))
    except (TypeError, ValueError):
        page_count = 0
    return {
        "id": report_id,
        "title": title,
        "title_en": title_en,
        "institution": report_institution(report),
        "industry": report_industry(report),
        "date_folder": compact_text(report.get("date_folder"), 16),
        "page_count": page_count,
        "available": bool(report.get("available") or report.get("r2_synced")),
        "attraction_score": attraction_score(report),
    }


def base_rank(report: dict[str, Any], item: dict[str, Any]) -> float:
    token = date_key(report)
    recency = max(0, int(token or "0") - 20250000) / 2000 if token else 0
    return item["attraction_score"] * 1.8 + recency + (2 if item["available"] else 0)


def bucket_index(key: str, bucket_count: int) -> int:
    digest = hashlib.sha256(key.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % bucket_count


def choose_bucket_count(key_count: int, requested: int | None = None) -> int:
    if requested is not None:
        if requested < 1 or requested > 1 << 24:
            raise ValueError("bucket count is outside the supported range")
        return requested
    target = max(1, math.ceil(max(1, key_count) / MAX_BUCKET_ENTRIES))
    return 1 << max(0, (target - 1).bit_length())


def write_bucket_table(
    entries: dict[str, Any],
    table_path: Path,
    data_path: Path,
    requested_bucket_count: int | None = None,
) -> dict[str, int]:
    bucket_count = choose_bucket_count(len(entries), requested_bucket_count)
    buckets: list[list[list[Any]]] = [[] for _ in range(bucket_count)]
    for key in sorted(entries):
        buckets[bucket_index(key, bucket_count)].append([key, entries[key]])

    slots = bytearray()
    payload = bytearray()
    largest_bucket = 0
    max_bucket_bytes = 0
    for bucket in buckets:
        if not bucket:
            slots.extend(struct.pack(">QI", 0, 0))
            continue
        encoded = json.dumps(bucket, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        if len(encoded) > 0xFFFFFFFF:
            raise ValueError("one random-access bucket exceeds the slot length limit")
        if len(encoded) > MAX_BUCKET_BYTES:
            raise ValueError("one random-access bucket exceeds the Worker range-read limit")
        offset = len(payload)
        payload.extend(encoded)
        slots.extend(struct.pack(">QI", offset, len(encoded)))
        largest_bucket = max(largest_bucket, len(bucket))
        max_bucket_bytes = max(max_bucket_bytes, len(encoded))

    if len(slots) != bucket_count * SLOT_SIZE:
        raise AssertionError("invalid fixed-slot table size")
    table_path.write_bytes(slots)
    data_path.write_bytes(payload)
    return {
        "bucket_count": bucket_count,
        "slot_size": SLOT_SIZE,
        "data_bytes": len(payload),
        "largest_bucket": largest_bucket,
        "max_bucket_bytes": max(16, max_bucket_bytes),
    }


def build_index(
    catalog_path: Path,
    output_dir: Path,
    prefix: str = DEFAULT_PREFIX,
    token_bucket_count: int | None = None,
    item_bucket_count: int | None = None,
) -> dict[str, Any]:
    raw_catalog = catalog_path.read_bytes()
    catalog = json.loads(raw_catalog)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("items"), list):
        raise ValueError("catalog must contain an items array")
    prefix = prefix.strip().strip("/")
    if not prefix or not re.fullmatch(r"[A-Za-z0-9_./-]+", prefix) or ".." in prefix.split("/"):
        raise ValueError("invalid private index prefix")

    output_dir.mkdir(parents=True, exist_ok=True)
    release = hashlib.sha256(BUILD_FORMAT + raw_catalog).hexdigest()[:32]
    release_prefix = f"{prefix}/releases/{release}"

    item_rows: dict[str, dict[str, Any]] = {}
    rank_rows: dict[str, tuple[float, str]] = {}
    token_members: dict[str, list[str]] = defaultdict(list)
    seen_ids: set[str] = set()
    for report in catalog["items"]:
        if not isinstance(report, dict):
            continue
        item = public_item(report)
        if item is None or item["id"] in seen_ids:
            continue
        seen_ids.add(item["id"])
        item_rows[item["id"]] = item
        rank_rows[item["id"]] = (base_rank(report, item), item["date_folder"])
        metadata = " ".join(str(report.get(key) or "") for key in (
            "title_zh", "title", "bank_code", "bank_name", "institution", "industry", "sector", "category", "date_folder",
        ))
        metadata = f"{metadata} {item['institution']} {item['industry']}"
        for token in search_tokens(metadata):
            token_members[token].append(item["id"])

    if not item_rows:
        raise ValueError("catalog produced no valid report chat items")

    def rank_key(report_id: str) -> tuple[float, int, str]:
        score, date = rank_rows[report_id]
        try:
            date_rank = int(str(date) or "0")
        except ValueError:
            date_rank = 0
        return (-score, -date_rank, report_id)

    token_rows = {
        token: sorted(set(report_ids), key=rank_key)[:POSTING_LIMIT]
        for token, report_ids in token_members.items()
    }
    default_ids = sorted(item_rows, key=rank_key)[:CANDIDATE_LIMIT]
    default_items = [item_rows[report_id] for report_id in default_ids]

    table_manifests: dict[str, dict[str, Any]] = {}
    requested_counts = {
        "token_table": token_bucket_count,
        "item_table": item_bucket_count,
    }
    source_rows = {"token_table": token_rows, "item_table": item_rows}
    for table_name, (table_filename, data_filename) in TABLE_FILES.items():
        stats = write_bucket_table(
            source_rows[table_name],
            output_dir / table_filename,
            output_dir / data_filename,
            requested_counts[table_name],
        )
        table_manifests[table_name] = {
            "table_key": f"{release_prefix}/{table_filename}",
            "data_key": f"{release_prefix}/{data_filename}",
            **stats,
        }

    manifest: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "index_kind": "report-chat-random-access",
        "release": release,
        "normalization": "nfkc-lower-alnum-cjk234-v1",
        "hash": "sha256-first8-be",
        "query_token_limit": QUERY_TOKEN_LIMIT,
        "candidate_limit": CANDIDATE_LIMIT,
        "posting_limit": POSTING_LIMIT,
        "item_count": len(item_rows),
        "token_count": len(token_rows),
        "default_items": default_items,
        **table_manifests,
    }
    manifest_bytes = json.dumps(manifest, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    (output_dir / "manifest.json").write_bytes(manifest_bytes)
    return manifest


def _not_found(error: Exception) -> bool:
    response = getattr(error, "response", None)
    if isinstance(response, dict):
        code = str((response.get("Error") or {}).get("Code") or "")
        return code in {"404", "NoSuchKey", "NotFound"}
    return False


def publish_index(client: Any, bucket: str, output_dir: Path, prefix: str = DEFAULT_PREFIX) -> dict[str, Any]:
    manifest_path = output_dir / "manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    immutable_files: list[tuple[Path, str, str]] = []
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
                raise RuntimeError("immutable Report Chat index object does not match its release")
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
                raise RuntimeError("Report Chat index object length verification failed")

    # This small mutable pointer is the commit record. Publish it only after all
    # immutable objects have been written and verified.
    manifest_key = f"{prefix.strip().strip('/')}/manifest.json"
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
        raise RuntimeError("Report Chat manifest commit verification failed")
    return manifest


def build_r2_client() -> Any:
    import boto3
    from botocore.config import Config

    account_id = os.environ["R2_ACCOUNT_ID"]
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
        region_name="auto",
        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"}),
    )


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog-path", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--r2-prefix", default=DEFAULT_PREFIX)
    parser.add_argument("--upload-r2", action="store_true")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    manifest = build_index(args.catalog_path, args.output_dir, args.r2_prefix)
    if args.upload_r2:
        bucket = os.environ["R2_BUCKET"]
        publish_index(build_r2_client(), bucket, args.output_dir, args.r2_prefix)
    token_bytes = (args.output_dir / "tokens.tbl").stat().st_size + (args.output_dir / "tokens.dat").stat().st_size
    item_bytes = (args.output_dir / "items.tbl").stat().st_size + (args.output_dir / "items.dat").stat().st_size
    print(
        f"report_chat_release={manifest['release']} items={manifest['item_count']} "
        f"tokens={manifest['token_count']} token_bytes={token_bytes} item_bytes={item_bytes} "
        f"published={str(args.upload_r2).lower()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
