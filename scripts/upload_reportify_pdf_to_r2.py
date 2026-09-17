#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload a grabbed Reportify PDF to the Portal Suite R2 bucket.

The ``reportify-grab`` workflow runs ``reportify_pdf_grabber.py`` to fetch a gated
report's PDF, then calls this script to mirror it to R2 under ``reportify/<id>.pdf``.
The Worker's ``GET /reportify/pdf?id=<id>`` then serves that object on the next request.

This reuses the same R2 credentials as ``portal_suite_catalog.py`` (the
``R2_ACCOUNT_ID / R2_ACCESS_KEY_ID / R2_SECRET_ACCESS_KEY / R2_BUCKET`` env vars).

Run:
    python scripts/upload_reportify_pdf_to_r2.py --id 1264649995240476672 --pdf /tmp/1264649995240476672.pdf
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

from sanitize_pdf_links import sanitize_pdf_links
from reportify_pdf_grabber import validate_pdf
from reportify_result import read_result, ready_metadata

REPORTIFY_R2_PREFIX = "reportify"
DEFAULT_BUCKET = "portal-suite-pdfs"


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def build_r2_client():
    try:
        import boto3  # type: ignore
    except Exception as exc:  # pragma: no cover - exercised in Actions
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
    parser = argparse.ArgumentParser(description="Upload a Reportify PDF to R2.")
    parser.add_argument("--id", required=True, help="Numeric reportify report id.")
    parser.add_argument("--pdf", required=True, help="Path to the grabbed PDF.")
    parser.add_argument("--result-json", type=Path, help="Verified grabber result (default: PDF path + .result.json)")
    args = parser.parse_args()

    report_id = args.id.strip()
    if not re.fullmatch(r"[0-9]{6,25}", report_id):
        raise SystemExit(f"Invalid report id: {report_id!r}")

    pdf_path = Path(args.pdf).expanduser()
    data = pdf_path.read_bytes() if pdf_path.exists() else b""
    if not data.startswith(b"%PDF-"):
        raise SystemExit(f"Not a valid PDF (missing %PDF- header): {pdf_path}")
    result_path = args.result_json or pdf_path.with_name(pdf_path.name + ".result.json")
    result = read_result(result_path, report_id)
    metadata = ready_metadata(result, data)
    try:
        if sanitize_pdf_links(pdf_path):
            data = pdf_path.read_bytes()
    except Exception:
        print("warning: could not sanitize PDF links", file=sys.stderr)
    data = pdf_path.read_bytes()
    # Sanitization must preserve the verified page count as well.
    validate_pdf(data, result["expected_page_count"])
    metadata["sha256"] = hashlib.sha256(data).hexdigest()

    bucket = os.getenv("R2_BUCKET", "").strip() or DEFAULT_BUCKET
    key = f"{REPORTIFY_R2_PREFIX}/{report_id}.pdf"
    client = build_r2_client()
    with pdf_path.open("rb") as f:
        client.upload_fileobj(
            f,
            bucket,
            key,
            ExtraArgs={
                "ContentType": "application/pdf",
                "Metadata": metadata,
            },
        )
    head = client.head_object(Bucket=bucket, Key=key)
    if (head.get("ContentLength") != len(data)
            or any(head.get("Metadata", {}).get(name) != value for name, value in metadata.items())):
        raise RuntimeError("Uploaded report PDF metadata or size failed readback verification")
    print(f"Uploaded {pdf_path} ({len(data) // 1024} KB) -> r2://{bucket}/{key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
