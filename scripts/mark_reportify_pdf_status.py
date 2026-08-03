#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write background external-report preparation status to R2."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone

DEFAULT_BUCKET = "portal-suite-pdfs"
STATUS_PREFIX = "reportify-status"


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def build_r2_client():
    try:
        import boto3  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise SystemExit("boto3 is required. Install it with: pip install boto3") from exc

    account_id = require_env("R2_ACCOUNT_ID")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Mark external report PDF preparation status.")
    parser.add_argument("--id", required=True, help="Numeric report id.")
    parser.add_argument("--status", required=True, choices=["running", "ready", "failed"])
    parser.add_argument("--message", default="")
    args = parser.parse_args()

    report_id = args.id.strip()
    if not re.fullmatch(r"[0-9]{6,25}", report_id):
        raise SystemExit(f"Invalid report id: {report_id!r}")

    payload = {
        "id": report_id,
        "status": args.status,
        "message": args.message.strip()[:500],
        "updated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    bucket = os.getenv("R2_BUCKET", "").strip() or DEFAULT_BUCKET
    key = f"{STATUS_PREFIX}/{report_id}.json"
    build_r2_client().put_object(
        Bucket=bucket,
        Key=key,
        Body=body,
        ContentType="application/json; charset=utf-8",
        CacheControl="no-store",
    )
    print(f"Marked {args.status} -> r2://{bucket}/{key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
