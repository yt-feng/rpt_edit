#!/usr/bin/env python3
"""Remove clickable link annotations from cached external PDFs in R2."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

from sanitize_pdf_links import sanitize_pdf_links

DEFAULT_BUCKET = "portal-suite-pdfs"
DEFAULT_PREFIX = "reportify/"
SANITIZED_META_KEY = "portal-links-sanitized"


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


def iter_pdf_keys(client, bucket: str, prefix: str, limit: int):
    continuation = None
    emitted = 0
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if continuation:
            kwargs["ContinuationToken"] = continuation
        response = client.list_objects_v2(**kwargs)
        for item in response.get("Contents", []):
            key = str(item.get("Key") or "")
            if not key.lower().endswith(".pdf"):
                continue
            yield key
            emitted += 1
            if limit and emitted >= limit:
                return
        if not response.get("IsTruncated"):
            return
        continuation = response.get("NextContinuationToken")


def object_is_marked_clean(client, bucket: str, key: str) -> bool:
    try:
        head = client.head_object(Bucket=bucket, Key=key)
    except Exception:
        return False
    metadata = {str(k).lower(): str(v).lower() for k, v in (head.get("Metadata") or {}).items()}
    return metadata.get(SANITIZED_META_KEY) == "true"


def sanitize_one(client, bucket: str, key: str, dry_run: bool) -> tuple[str, bool]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        path = Path(tmp_dir) / "report.pdf"
        with path.open("wb") as handle:
            client.download_fileobj(bucket, key, handle)
        data = path.read_bytes()
        if not data.startswith(b"%PDF-"):
            return "not-pdf", False
        changed = sanitize_pdf_links(path)
        if dry_run:
            return ("would-update" if changed else "would-mark-clean"), changed
        with path.open("rb") as handle:
            client.upload_fileobj(
                handle,
                bucket,
                key,
                ExtraArgs={
                    "ContentType": "application/pdf",
                    "Metadata": {SANITIZED_META_KEY: "true"},
                },
            )
        return ("updated" if changed else "marked-clean"), changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanitize cached report PDFs in R2.")
    parser.add_argument("--prefix", default=DEFAULT_PREFIX, help="R2 key prefix to scan.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum PDFs to process; 0 means all.")
    parser.add_argument("--force", action="store_true", help="Reprocess objects already marked clean.")
    parser.add_argument("--dry-run", action="store_true", help="Scan and report without uploading.")
    args = parser.parse_args()

    client = build_r2_client()
    bucket = os.getenv("R2_BUCKET", "").strip() or DEFAULT_BUCKET
    scanned = skipped = updated = marked = changed = 0
    for key in iter_pdf_keys(client, bucket, args.prefix, max(args.limit, 0)):
        scanned += 1
        if not args.force and object_is_marked_clean(client, bucket, key):
            skipped += 1
            print(f"skip clean: {key}")
            continue
        status, did_change = sanitize_one(client, bucket, key, args.dry_run)
        if status in {"updated", "would-update"}:
            updated += 1
        elif status in {"marked-clean", "would-mark-clean"}:
            marked += 1
        changed += int(did_change)
        print(f"{status}: {key}")
    print(f"summary scanned={scanned} skipped={skipped} updated={updated} marked={marked} changed={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
