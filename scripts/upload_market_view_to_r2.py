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


DEFAULT_BUCKET = "kc-desk-notes-pdfs"
MARKET_VIEWS_PREFIX = "_market-views"
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
    if if_absent:
        pdf_exists, pdf_head = r2_object_exists(resolved_client, resolved_bucket, pdf_key)
        item_exists, _item_head = r2_object_exists(resolved_client, resolved_bucket, item_key)
        if pdf_exists and item_exists:
            return {
                "schema_version": 1,
                "id": f"market-view:{date_key}",
                "date_key": date_key,
                "date": issue_date.isoformat(),
                "title": f"Market Views · {issue_date.isoformat()}",
                "filename": filename,
                "pdf_key": pdf_key,
                "size_bytes": int(pdf_head.get("ContentLength") or 0),
                "skipped_existing": True,
            }

    data = read_valid_pdf(path)
    size_bytes = len(data)
    sha256 = hashlib.sha256(data).hexdigest()
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
    try:
        stored_size = int(head.get("ContentLength", -1))
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"R2 PDF head returned an invalid ContentLength for {pdf_key}") from exc
    if stored_size != size_bytes:
        raise RuntimeError(
            f"R2 PDF size verification failed for {pdf_key}: expected {size_bytes}, got {stored_size}"
        )
    stored_type = str(head.get("ContentType") or "").split(";", 1)[0].strip().lower()
    if stored_type != PDF_CONTENT_TYPE:
        raise RuntimeError(
            f"R2 PDF content-type verification failed for {pdf_key}: {stored_type or 'missing'}"
        )
    stored_metadata = {
        str(key).lower(): str(value) for key, value in dict(head.get("Metadata") or {}).items()
    }
    if stored_metadata.get("sha256") != sha256:
        raise RuntimeError(f"R2 PDF SHA-256 verification failed for {pdf_key}")
    if stored_metadata.get("date-key") != date_key:
        raise RuntimeError(f"R2 PDF date metadata verification failed for {pdf_key}")

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
        help="Keep an already verified private PDF+metadata pair instead of overwriting it.",
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

    action = "Kept existing private" if item.get("skipped_existing") else "Archived"
    print(
        f"{action} {item['filename']} ({item['size_bytes']} bytes) -> "
        f"{item['pdf_key']} + {MARKET_VIEWS_PREFIX}/items/{item['date_key']}.json"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
