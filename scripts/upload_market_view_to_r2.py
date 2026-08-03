#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Archive one daily Market Views PDF and its public-safe metadata in private R2.

The PDF is written and verified with ``head_object`` before its metadata item is
published.  Consumers can therefore list ``_market-views/items/`` without ever
discovering an incomplete PDF upload.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_BUCKET = "portal-suite-pdfs"
MARKET_VIEWS_PREFIX = "_market-views"
LEGACY_VARIANTS_PREFIX = f"{MARKET_VIEWS_PREFIX}/legacy-variants"
PDF_CONTENT_TYPE = "application/pdf"
METADATA_CONTENT_TYPE = "application/json; charset=utf-8"
MIN_PDF_BYTES = 1024


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def parse_issue_date(value: str) -> tuple[date, str]:
    """Return the real issue date and its canonical YYMMDD object-key segment."""
    if not re.fullmatch(r"(?:[0-9]{6}|[0-9]{8})", value):
        raise ValueError("Market Views date must be exactly YYMMDD or YYYYMMDD")
    expanded = f"20{value}" if len(value) == 6 else value
    try:
        issue_date = datetime.strptime(expanded, "%Y%m%d").date()
    except ValueError as exc:
        raise ValueError(f"Invalid Market Views calendar date: {value}") from exc
    return issue_date, issue_date.strftime("%y%m%d")


def read_valid_pdf(path: Path) -> bytes:
    if not path.is_file():
        raise FileNotFoundError(f"Market Views PDF does not exist: {path}")
    size = path.stat().st_size
    if size <= MIN_PDF_BYTES:
        raise ValueError(
            f"Market Views PDF must be larger than {MIN_PDF_BYTES} bytes: {path} ({size} bytes)"
        )
    data = path.read_bytes()
    if len(data) <= MIN_PDF_BYTES:
        raise ValueError(f"Market Views PDF became too small while reading: {path}")
    if not data.startswith(b"%PDF-"):
        raise ValueError(f"Market Views file is missing the PDF magic header: {path}")
    return data


def build_r2_client():
    try:
        import boto3  # type: ignore
    except Exception as exc:  # pragma: no cover - exercised in Actions
        raise RuntimeError("boto3 is required. Install it with: pip install boto3") from exc

    account_id = require_env("R2_ACCOUNT_ID")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
    )


def _utc_timestamp(value: str | None = None) -> str:
    if value is not None:
        return value
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def r2_object_exists(client: Any, bucket: str, key: str) -> tuple[bool, dict[str, Any]]:
    try:
        return True, dict(client.head_object(Bucket=bucket, Key=key) or {})
    except (FileNotFoundError, KeyError):
        return False, {}
    except Exception as exc:
        response = getattr(exc, "response", {})
        error = response.get("Error", {}) if isinstance(response, dict) else {}
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode") if isinstance(response, dict) else None
        code = str(error.get("Code") or "")
        if status == 404 or code in {"404", "NoSuchKey", "NotFound"}:
            return False, {}
        raise


def _read_r2_body(response: dict[str, Any], key: str) -> bytes:
    body = response.get("Body")
    if body is None:
        raise RuntimeError(f"R2 get_object returned no body for {key}")
    try:
        data = body.read() if hasattr(body, "read") else body
    finally:
        close = getattr(body, "close", None)
        if callable(close):
            close()
    if not isinstance(data, (bytes, bytearray)):
        raise RuntimeError(f"R2 get_object returned an invalid body for {key}")
    return bytes(data)


def validate_existing_pdf_object(
    client: Any,
    bucket: str,
    *,
    key: str,
    head: dict[str, Any],
    date_key: str,
    expected_sha256: str | None = None,
) -> dict[str, Any]:
    """Read an existing private object in full and verify its bytes and metadata."""
    try:
        stored_size = int(head.get("ContentLength", -1))
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"Existing R2 PDF has invalid ContentLength: {key}") from exc
    if stored_size <= MIN_PDF_BYTES:
        raise RuntimeError(f"Existing R2 PDF is too small: {key} ({stored_size} bytes)")

    stored_type = str(head.get("ContentType") or "").split(";", 1)[0].strip().lower()
    if stored_type != PDF_CONTENT_TYPE:
        raise RuntimeError(
            f"Existing R2 PDF has invalid content-type: {key} ({stored_type or 'missing'})"
        )
    stored_metadata = {
        str(metadata_key).lower(): str(value)
        for metadata_key, value in dict(head.get("Metadata") or {}).items()
    }
    metadata_sha256 = stored_metadata.get("sha256", "").lower()
    if not re.fullmatch(r"[0-9a-f]{64}", metadata_sha256):
        raise RuntimeError(f"Existing R2 PDF is missing valid SHA-256 metadata: {key}")
    if stored_metadata.get("date-key") != date_key:
        raise RuntimeError(f"Existing R2 PDF has mismatched date metadata: {key}")

    stored_data = _read_r2_body(client.get_object(Bucket=bucket, Key=key), key)
    if len(stored_data) != stored_size:
        raise RuntimeError(
            f"Existing R2 PDF body length disagrees with ContentLength: {key} "
            f"({len(stored_data)} != {stored_size})"
        )
    if not stored_data.startswith(b"%PDF-"):
        raise RuntimeError(f"Existing R2 object is missing the PDF magic header: {key}")
    actual_sha256 = hashlib.sha256(stored_data).hexdigest()
    if actual_sha256 != metadata_sha256:
        raise RuntimeError(f"Existing R2 PDF bytes disagree with SHA-256 metadata: {key}")
    if expected_sha256 is not None and actual_sha256 != expected_sha256:
        raise RuntimeError(f"Existing R2 PDF has unexpected SHA-256 content: {key}")
    return {"size_bytes": stored_size, "sha256": actual_sha256}


def validate_existing_private_pair(
    client: Any,
    bucket: str,
    *,
    pdf_key: str,
    item_key: str,
    pdf_head: dict[str, Any],
    item_head: dict[str, Any],
    issue_date: date,
    date_key: str,
    filename: str,
) -> dict[str, Any]:
    """Fail closed unless an existing PDF and its index item are internally consistent."""
    verified_pdf = validate_existing_pdf_object(
        client,
        bucket,
        key=pdf_key,
        head=pdf_head,
        date_key=date_key,
    )
    stored_size = int(verified_pdf["size_bytes"])
    stored_sha256 = str(verified_pdf["sha256"])

    item_type = str(item_head.get("ContentType") or "").split(";", 1)[0].strip().lower()
    if item_type != "application/json":
        raise RuntimeError(
            f"Existing R2 Market Views item has invalid content-type: {item_key} "
            f"({item_type or 'missing'})"
        )

    item_body = _read_r2_body(client.get_object(Bucket=bucket, Key=item_key), item_key)
    try:
        item = json.loads(item_body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Existing R2 Market Views item is invalid JSON: {item_key}") from exc
    expected = {
        "schema_version": 1,
        "id": f"market-view:{date_key}",
        "date_key": date_key,
        "date": issue_date.isoformat(),
        "filename": filename,
        "pdf_key": pdf_key,
        "size_bytes": stored_size,
        "sha256": stored_sha256,
        "content_type": PDF_CONTENT_TYPE,
    }
    if not isinstance(item, dict):
        raise RuntimeError(f"Existing R2 Market Views item is not an object: {item_key}")
    mismatches = [key for key, value in expected.items() if item.get(key) != value]
    if mismatches:
        raise RuntimeError(
            f"Existing R2 Market Views item disagrees with its PDF for {item_key}: "
            + ", ".join(mismatches)
        )
    return item


def archive_private_variant(
    client: Any,
    bucket: str,
    *,
    data: bytes,
    date_key: str,
    filename: str,
    sha256: str,
) -> str:
    """Preserve a noncanonical same-date version without exposing it in the public index."""
    key = f"{LEGACY_VARIANTS_PREFIX}/{date_key}/{sha256}.pdf"
    exists, head = r2_object_exists(client, bucket, key)
    if exists:
        validate_existing_pdf_object(
            client,
            bucket,
            key=key,
            head=head,
            date_key=date_key,
            expected_sha256=sha256,
        )
        return key

    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType=PDF_CONTENT_TYPE,
        ContentDisposition=f'attachment; filename="{filename}"',
        CacheControl="private, max-age=86400",
        Metadata={
            "date-key": date_key,
            "sha256": sha256,
            "canonical-filename": filename,
        },
    )
    variant_head = client.head_object(Bucket=bucket, Key=key)
    validate_existing_pdf_object(
        client,
        bucket,
        key=key,
        head=variant_head,
        date_key=date_key,
        expected_sha256=sha256,
    )
    return key


def upload_market_view(
    pdf_path: Path | str,
    date_value: str,
    *,
    client: Any | None = None,
    bucket: str | None = None,
    updated_at: str | None = None,
    if_absent: bool = False,
) -> dict[str, Any]:
    """Upload and verify the PDF, then publish its metadata item."""
    issue_date, date_key = parse_issue_date(date_value)
    path = Path(pdf_path).expanduser()
    resolved_bucket = (bucket or os.getenv("R2_BUCKET", "").strip() or DEFAULT_BUCKET).strip()
    if not resolved_bucket:
        raise RuntimeError("R2 bucket name is empty")
    resolved_client = client or build_r2_client()

    pdf_key = f"{MARKET_VIEWS_PREFIX}/pdfs/{date_key}.pdf"
    item_key = f"{MARKET_VIEWS_PREFIX}/items/{date_key}.json"
    filename = f"market_views_{date_key}.pdf"
    data = read_valid_pdf(path)
    size_bytes = len(data)
    sha256 = hashlib.sha256(data).hexdigest()
    if if_absent:
        pdf_exists, pdf_head = r2_object_exists(resolved_client, resolved_bucket, pdf_key)
        item_exists, item_head = r2_object_exists(resolved_client, resolved_bucket, item_key)
        if pdf_exists != item_exists:
            raise RuntimeError(
                f"Existing private Market Views pair is incomplete for {date_key}; refusing overwrite"
            )
        if pdf_exists and item_exists:
            existing_item = validate_existing_private_pair(
                resolved_client,
                resolved_bucket,
                pdf_key=pdf_key,
                item_key=item_key,
                pdf_head=pdf_head,
                item_head=item_head,
                issue_date=issue_date,
                date_key=date_key,
                filename=filename,
            )
            if existing_item["sha256"] != sha256:
                variant_key = archive_private_variant(
                    resolved_client,
                    resolved_bucket,
                    data=data,
                    date_key=date_key,
                    filename=filename,
                    sha256=sha256,
                )
                return {
                    **existing_item,
                    "skipped_existing": True,
                    "archived_variant": True,
                    "variant_pdf_key": variant_key,
                    "source_sha256": sha256,
                }
            return {**existing_item, "skipped_existing": True}

    timestamp = _utc_timestamp(updated_at)

    resolved_client.put_object(
        Bucket=resolved_bucket,
        Key=pdf_key,
        Body=data,
        ContentType=PDF_CONTENT_TYPE,
        ContentDisposition=f'attachment; filename="{filename}"',
        CacheControl="private, max-age=86400",
        Metadata={
            "date-key": date_key,
            "sha256": sha256,
        },
    )

    head = resolved_client.head_object(Bucket=resolved_bucket, Key=pdf_key)
    verified_pdf = validate_existing_pdf_object(
        resolved_client,
        resolved_bucket,
        key=pdf_key,
        head=head,
        date_key=date_key,
        expected_sha256=sha256,
    )
    if int(verified_pdf["size_bytes"]) != size_bytes:
        raise RuntimeError(
            f"R2 PDF size verification failed for {pdf_key}: "
            f"expected {size_bytes}, got {verified_pdf['size_bytes']}"
        )

    item = {
        "schema_version": 1,
        "id": f"market-view:{date_key}",
        "date_key": date_key,
        "date": issue_date.isoformat(),
        "title": f"Market Views · {issue_date.isoformat()}",
        "filename": filename,
        "pdf_key": pdf_key,
        "size_bytes": size_bytes,
        "sha256": sha256,
        "content_type": PDF_CONTENT_TYPE,
        "updated_at": timestamp,
        "uploaded_at": timestamp,
    }
    item_body = (json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode(
        "utf-8"
    )
    resolved_client.put_object(
        Bucket=resolved_bucket,
        Key=item_key,
        Body=item_body,
        ContentType=METADATA_CONTENT_TYPE,
        CacheControl="private, max-age=300",
    )
    return item


def main() -> int:
    parser = argparse.ArgumentParser(description="Archive a daily Market Views PDF in private R2.")
    parser.add_argument("--date", required=True, help="Issue date in YYMMDD or YYYYMMDD form.")
    parser.add_argument("--pdf", required=True, help="Path to market_views_<date>.pdf.")
    parser.add_argument("--bucket", default="", help="Optional R2 bucket override.")
    parser.add_argument(
        "--if-absent",
        action="store_true",
        help=(
            "Keep an already verified private PDF+metadata pair; preserve differing same-date "
            "content as a private immutable variant."
        ),
    )
    args = parser.parse_args()

    try:
        item = upload_market_view(
            args.pdf,
            args.date,
            bucket=args.bucket or None,
            if_absent=args.if_absent,
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    if item.get("archived_variant"):
        print(
            f"Archived differing {item['filename']} privately -> {item['variant_pdf_key']}; "
            f"kept canonical {item['pdf_key']}"
        )
        return 0
    action = "Kept existing private" if item.get("skipped_existing") else "Archived"
    print(
        f"{action} {item['filename']} ({item['size_bytes']} bytes) -> "
        f"{item['pdf_key']} + {MARKET_VIEWS_PREFIX}/items/{item['date_key']}.json"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
