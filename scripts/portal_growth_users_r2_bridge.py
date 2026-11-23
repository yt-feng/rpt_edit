#!/usr/bin/env python3
"""Private stdio bridge for canonical account reads; never a cloud write API."""
from __future__ import annotations

import base64
from concurrent.futures import ThreadPoolExecutor
import json
import os
import re
import sys
from threading import Lock, Semaphore

MAX_BYTES = 512 * 1024
MAX_CALLS = 40000
READ_PREFIXES = (
    "_account/users/id/", "_account/entitlements/", "_account/access/",
    "_account/user-state/email/", "_account/user-state/id/", "_account/newsfeed-access/",
)
LIST_PREFIXES = {"_account/users/id/", "_account/entitlements/"}


def request_shape(value):
    if not isinstance(value, dict) or type(value.get("id")) is not int or not 1 <= value["id"] <= MAX_CALLS:
        raise ValueError("invalid read request")
    operation = value.get("op")
    if operation not in {"get", "head", "list"}:
        raise ValueError("only reads are supported")
    if operation == "list":
        if set(value) - {"id", "op", "prefix", "limit", "cursor"}:
            raise ValueError("invalid list fields")
        if value.get("prefix") not in LIST_PREFIXES:
            raise ValueError("listing outside canonical account sources")
        limit = value.get("limit", 1000)
        cursor = value.get("cursor", "")
        if type(limit) is not int or not 1 <= limit <= 1000 or not isinstance(cursor, str) or len(cursor) > 8192:
            raise ValueError("invalid listing bound")
    else:
        key = value.get("key")
        if (set(value) != {"id", "op", "key"} or not isinstance(key, str) or len(key) > 2048
                or not any(key.startswith(prefix) and len(key) > len(prefix) and "/" not in key[len(prefix):]
                           for prefix in READ_PREFIXES)
                or any(part in {".", "..", ""} for part in key.split("/"))
                or any(ord(char) < 32 for char in key)):
            raise ValueError("reading outside canonical account sources")
    return value


def read_request(client, bucket, value):
    value = request_shape(value)
    operation = value["op"]
    if operation == "list":
        params = {"Bucket": bucket, "Prefix": value["prefix"], "MaxKeys": value.get("limit", 1000)}
        if value.get("cursor"):
            params["ContinuationToken"] = value["cursor"]
        result = client.list_objects_v2(**params)
        return {"objects": [{"key": row["Key"]} for row in result.get("Contents", [])],
                "truncated": bool(result.get("IsTruncated")), "cursor": result.get("NextContinuationToken", "")}
    try:
        if operation == "head":
            response = client.head_object(Bucket=bucket, Key=value["key"])
            return {"etag": str(response.get("ETag", "")).strip('"'), "size": response.get("ContentLength", 0)}
        response = client.get_object(Bucket=bucket, Key=value["key"])
    except Exception as error:
        metadata = getattr(error, "response", {})
        if metadata.get("Error", {}).get("Code") in {"NoSuchKey", "NotFound", "404"}:
            return None
        raise
    body = response["Body"]
    try:
        raw = body.read(MAX_BYTES + 1)
        if len(raw) > MAX_BYTES:
            raise ValueError("account object exceeds read bound")
    finally:
        body.close()
    return {"etag": str(response.get("ETag", "")).strip('"'),
            "body_b64": base64.b64encode(raw).decode("ascii")}


def client_from_env():
    import boto3
    from botocore.config import Config
    account = os.environ.get("R2_ACCOUNT_ID", "")
    bucket = os.environ.get("R2_BUCKET", "")
    key = os.environ.get("R2_ACCESS_KEY_ID", "")
    secret = os.environ.get("R2_SECRET_ACCESS_KEY", "")
    if not re.fullmatch(r"[a-f0-9]{32}", account) or not all((bucket, key, secret)):
        raise ValueError("storage configuration incomplete")
    client = boto3.client("s3", endpoint_url=f"https://{account}.r2.cloudflarestorage.com",
                          aws_access_key_id=key, aws_secret_access_key=secret, region_name="auto",
                          config=Config(signature_version="s3v4", retries={"total_max_attempts": 3, "mode": "standard"},
                                        max_pool_connections=8, connect_timeout=10, read_timeout=20))
    return client, bucket


def main():
    client, bucket = client_from_env()
    lock, pending = Lock(), Semaphore(64)
    seen = set()
    def process(value):
        try:
            result = {"id": value["id"], "ok": True, "result": read_request(client, bucket, value)}
        except Exception:
            result = {"id": value["id"], "ok": False, "error": "canonical_account_read_failed"}
        with lock:
            print(json.dumps(result, separators=(",", ":")), flush=True)
        pending.release()
    with ThreadPoolExecutor(max_workers=8) as pool:
        while True:
            line = sys.stdin.readline(16385)
            if not line:
                break
            if len(line) > 16384 or not line.endswith("\n"):
                raise ValueError("read request exceeds bound")
            value = request_shape(json.loads(line))
            if value["id"] in seen or len(seen) >= MAX_CALLS:
                raise ValueError("read request repeated or exceeds bound")
            seen.add(value["id"])
            pending.acquire()
            pool.submit(process, value)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # The parent logs only a generic failure; provider exceptions stay private.
        raise SystemExit(1) from None
