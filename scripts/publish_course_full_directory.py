#!/usr/bin/env python3
"""Validate and publish the private original-name catalog; never print its rows."""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import re
from datetime import datetime

MAX_BYTES = 32 * 1024 * 1024
MAX_ITEMS = 100000
FORMAT = "course-full-directory-aes-256-gcm-v1"
AAD = b"course-full-directory-v1"
KEY = "_course-directory/full-v1/directory.json"
FIELDS = {"id", "name", "folders", "extension", "size_label", "date"}


def display_text(value, limit):
    if (not isinstance(value, str) or not value.strip() or len(value) > limit
            or any(ord(c) < 32 or ord(c) == 127 for c in value) or "/" in value or "\\" in value):
        raise ValueError("invalid_display_text")
    return value


def validate(payload):
    if (not isinstance(payload, dict) or set(payload) != {"schema_version", "variant", "complete", "item_count", "generated_at", "items"}
            or type(payload.get("schema_version")) is not int or payload.get("schema_version") != 1
            or payload.get("variant") != "original_names" or payload.get("complete") is not True
            or not isinstance(payload.get("items"), list)
            or type(payload.get("item_count")) is not int
            or payload["item_count"] != len(payload["items"])
            or not 1 <= payload["item_count"] <= MAX_ITEMS):
        raise ValueError("invalid_complete_catalog")
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:.]+Z", str(payload.get("generated_at", ""))):
        raise ValueError("invalid_generation")
    datetime.fromisoformat(payload["generated_at"].replace("Z", "+00:00"))
    seen = set()
    for row in payload["items"]:
        if not isinstance(row, dict) or set(row) != FIELDS:
            raise ValueError("invalid_row_fields")
        if not isinstance(row["id"], str) or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{7,79}", row["id"]) or row["id"] in seen:
            raise ValueError("invalid_row_identity")
        seen.add(row["id"])
        display_text(row["name"], 500)
        if not isinstance(row["folders"], list) or len(row["folders"]) > 32:
            raise ValueError("invalid_folders")
        for folder in row["folders"]:
            display_text(folder, 500)
        if not isinstance(row["extension"], str) or not re.fullmatch(r"[a-z0-9]{0,12}", row["extension"]):
            raise ValueError("invalid_extension")
        if not isinstance(row["size_label"], str) or row["size_label"] and not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?\s*(?:B|KB|MB|GB|TB)", row["size_label"]):
            raise ValueError("invalid_size")
        if not isinstance(row["date"], str) or row["date"] and not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", row["date"]):
            raise ValueError("invalid_date")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode()
    if len(encoded) > MAX_BYTES:
        raise ValueError("catalog_too_large")
    return encoded


def decrypt(path, key):
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    envelope = json.loads(Path(path).read_text())
    if envelope.get("format") != FORMAT or len(key) != 32:
        raise ValueError("invalid_envelope")
    nonce = base64.b64decode(envelope["nonce"], validate=True)
    if len(nonce) != 12:
        raise ValueError("invalid_nonce")
    compressed = AESGCM(key).decrypt(nonce, base64.b64decode(envelope["ciphertext"], validate=True), AAD)
    with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("catalog_too_large")
    return validate(json.loads(raw))


def publish(client, bucket, body):
    digest = hashlib.sha256(body).hexdigest()
    revision = f"_course-directory/full-v1/revisions/{digest}.json"
    previous = None
    try:
        previous = client.head_object(Bucket=bucket, Key=KEY).get("ETag")
    except Exception as error:
        if str(getattr(error, "response", {}).get("Error", {}).get("Code", "")) not in {"404", "NoSuchKey", "NotFound"}:
            raise ValueError("previous_version_unavailable") from None
    for key in [revision, KEY]:
        kwargs = {} if key == revision else ({"IfMatch": previous} if previous else {"IfNoneMatch": "*"})
        client.put_object(Bucket=bucket, Key=key, Body=body, ContentType="application/json; charset=utf-8",
                          CacheControl="private, no-store", Metadata={"sha256": digest}, **kwargs)
        response = client.get_object(Bucket=bucket, Key=key)
        try:
            saved = response["Body"].read(MAX_BYTES + 1)
        finally:
            response["Body"].close()
        if hashlib.sha256(saved).hexdigest() != digest:
            raise ValueError("publish_unverified")
    return {"ok": True, "item_count": json.loads(body)["item_count"], "bytes": len(body), "sha256": digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", required=True, type=Path)
    args = parser.parse_args()
    try:
        import boto3
        from botocore.config import Config
        key = base64.b64decode(os.environ["COURSE_FULL_DIRECTORY_BUNDLE_KEY_B64"], validate=True)
        body = decrypt(args.bundle, key)
        client = boto3.client("s3", endpoint_url=f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
                              aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"], aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
                              region_name="auto", config=Config(connect_timeout=10, read_timeout=30, retries={"total_max_attempts": 1}))
        print(json.dumps(publish(client, os.environ["R2_BUCKET"], body)))
    except Exception:
        raise SystemExit("Original-name directory could not be verified or published; no source rows are logged.") from None


if __name__ == "__main__":
    main()
