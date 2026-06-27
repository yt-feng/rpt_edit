#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload a grabbed Reportify PDF to the KC Desk Notes R2 bucket.

The ``reportify-grab`` workflow runs ``reportify_pdf_grabber.py`` to fetch a gated
report's PDF, then calls this script to mirror it to R2 under ``reportify/<id>.pdf``.
The Worker's ``GET /reportify/pdf?id=<id>`` then serves that object on the next request.

This reuses the same R2 credentials as ``kc_desk_notes_catalog.py`` (the
``R2_ACCOUNT_ID / R2_ACCESS_KEY_ID / R2_SECRET_ACCESS_KEY / R2_BUCKET`` env vars).

Run:
    python scripts/upload_reportify_pdf_to_r2.py --id 1264649995240476672 --pdf /tmp/1264649995240476672.pdf
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPORTIFY_R2_PREFIX = "reportify"
DEFAULT_BUCKET = "kc-desk-notes-pdfs"


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
    args = parser.parse_args()

    report_id = args.id.strip()
    if not re.fullmatch(r"[0-9]{6,25}", report_id):
        raise SystemExit(f"Invalid report id: {report_id!r}")

    pdf_path = Path(args.pdf).expanduser()
    data = pdf_path.read_bytes() if pdf_path.exists() else b""
    if not data.startswith(b"%PDF-"):
        raise SystemExit(f"Not a valid PDF (missing %PDF- header): {pdf_path}")

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
                "Metadata": {"source": "reportify"},
            },
        )
    print(f"Uploaded {pdf_path} ({len(data) // 1024} KB) -> r2://{bucket}/{key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
