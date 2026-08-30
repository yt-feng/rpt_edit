#!/usr/bin/env python3
"""Archive an aggregate-only weekly growth review to private R2 storage."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


ARCHIVE_PREFIX = "_analytics/reviews/weekly"
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
LOG_PREFIX = "growth-review-archive:"


class ArchiveError(RuntimeError):
    pass


def validated_date(value: Any) -> str:
    text = str(value or "")
    if not DATE_RE.fullmatch(text):
        raise ArchiveError("invalid review window")
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError as error:
        raise ArchiveError("invalid review window") from error


def review_window(report: dict[str, Any]) -> tuple[str, str]:
    nested = report.get("review_window")
    window = nested if isinstance(nested, dict) else {}
    start = validated_date(window.get("start") or window.get("start_date") or report.get("start_date"))
    end = validated_date(window.get("end") or window.get("end_date") or report.get("end_date"))
    if date.fromisoformat(end) < date.fromisoformat(start):
        raise ArchiveError("invalid review window")
    return start, end


def archive_keys(start: str, end: str) -> dict[str, str]:
    safe_start = validated_date(start)
    safe_end = validated_date(end)
    directory = f"{ARCHIVE_PREFIX}/{safe_start}_{safe_end}"
    return {
        "json": f"{directory}/growth-review.json",
        "markdown": f"{directory}/growth-review.md",
    }


def archive_growth_review(
    client: Any,
    bucket: str,
    json_path: Path,
    markdown_path: Path,
) -> tuple[str, str, int]:
    json_bytes = json_path.read_bytes()
    markdown_bytes = markdown_path.read_bytes()
    try:
        report = json.loads(json_bytes.decode("utf-8"))
        markdown_bytes.decode("utf-8")
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ArchiveError("invalid aggregate review") from error
    if not isinstance(report, dict):
        raise ArchiveError("invalid aggregate review")
    privacy = report.get("privacy")
    if not isinstance(privacy, dict) or any(bool(value) for value in privacy.values()):
        raise ArchiveError("aggregate-only assertion missing")
    start, end = review_window(report)
    keys = archive_keys(start, end)
    uploads = (
        (keys["json"], json_bytes, "application/json; charset=utf-8"),
        (keys["markdown"], markdown_bytes, "text/markdown; charset=utf-8"),
    )
    for key, body, content_type in uploads:
        client.put_object(
            Bucket=bucket,
            Key=key,
            Body=body,
            ContentType=content_type,
            CacheControl="private, no-store",
        )
    return start, end, len(uploads)


def build_r2_client() -> tuple[Any, str]:
    account_id = os.environ.get("R2_ACCOUNT_ID", "").strip()
    access_key = os.environ.get("R2_ACCESS_KEY_ID", "").strip()
    secret_key = os.environ.get("R2_SECRET_ACCESS_KEY", "").strip()
    bucket = os.environ.get("R2_BUCKET", "").strip()
    if not all((account_id, access_key, secret_key, bucket)):
        raise ArchiveError("private storage configuration missing")
    try:
        import boto3
        from botocore.config import Config
    except ImportError as error:  # pragma: no cover - installed in Actions.
        raise ArchiveError("private storage client missing") from error
    client = boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"}),
    )
    return client, bucket


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        client, bucket = build_r2_client()
        start, end, object_count = archive_growth_review(client, bucket, args.json, args.markdown)
    except Exception:
        print(f"{LOG_PREFIX} failed", file=sys.stderr)
        return 1
    print(f"{LOG_PREFIX} {start}_{end} objects={object_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
