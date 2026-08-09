#!/usr/bin/env python3
"""Persist chart-search checkpoints, indexes, and immutable images in private R2."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


DEFAULT_PREFIX = "_chart-search/v1"
ASSET_RE = re.compile(r"^[0-9a-f]{64}\.jpg$")


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required configuration: {name}")
    return value


def validate_prefix(value: str) -> str:
    cleaned = value.strip().strip("/")
    path = PurePosixPath(cleaned)
    if not cleaned or path.is_absolute() or ".." in path.parts:
        raise RuntimeError("Unsafe chart-search object prefix")
    return cleaned


def client_and_bucket() -> tuple[Any, str]:
    try:
        import boto3  # type: ignore
        from botocore.config import Config  # type: ignore
    except ImportError as exc:  # pragma: no cover - installed in Actions
        raise RuntimeError("boto3 is required") from exc
    account_id = require_env("R2_ACCOUNT_ID")
    client = boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
        config=Config(retries={"max_attempts": 8, "mode": "adaptive"}),
    )
    return client, require_env("R2_BUCKET")


def default_document(kind: str) -> dict[str, Any]:
    if kind == "state":
        return {"schema_version": 1, "analysis_version": "chart-search-v1", "items": {}}
    return {"schema_version": 1, "report_count": 0, "item_count": 0, "reports": []}


def atomic_write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def is_not_found(error: Exception) -> bool:
    response = getattr(error, "response", {})
    code = str(((response or {}).get("Error") or {}).get("Code") or "")
    return code in {"404", "NoSuchKey", "NotFound"}


def download_json(client: Any, bucket: str, key: str, destination: Path, kind: str) -> bool:
    try:
        response = client.get_object(Bucket=bucket, Key=key)
    except Exception as exc:  # botocore is an optional runtime dependency
        if is_not_found(exc):
            atomic_write(destination, default_document(kind))
            return False
        raise RuntimeError(f"Unable to download chart-search {kind}") from exc
    try:
        value = json.loads(response["Body"].read().decode("utf-8"))
    except (KeyError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Stored chart-search {kind} is invalid") from exc
    if not isinstance(value, dict) or int(value.get("schema_version") or 0) != 1:
        raise RuntimeError(f"Stored chart-search {kind} has an unsupported schema")
    atomic_write(destination, value)
    return True


def load_publish_document(path: Path, kind: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Local chart-search {kind} is invalid") from exc
    if not isinstance(value, dict) or int(value.get("schema_version") or 0) != 1:
        raise RuntimeError(f"Local chart-search {kind} has an unsupported schema")
    return value


def put_json(client: Any, bucket: str, key: str, path: Path, *, private: bool) -> None:
    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=path.read_bytes(),
        ContentType="application/json; charset=utf-8",
        CacheControl="private, no-store" if private else "public, max-age=300",
    )


def asset_exists(client: Any, bucket: str, key: str) -> bool:
    try:
        client.head_object(Bucket=bucket, Key=key)
        return True
    except Exception as exc:
        if is_not_found(exc):
            return False
        raise RuntimeError("Unable to inspect chart-search image") from exc


def publish_assets(client: Any, bucket: str, prefix: str, asset_dir: Path) -> tuple[int, int]:
    if not asset_dir.exists():
        return 0, 0
    uploaded = 0
    reused = 0
    for asset in sorted(asset_dir.iterdir()):
        if not asset.is_file() or not ASSET_RE.fullmatch(asset.name):
            continue
        key = f"{prefix}/images/{asset.name}"
        if asset_exists(client, bucket, key):
            reused += 1
            continue
        client.upload_file(
            str(asset),
            bucket,
            key,
            ExtraArgs={
                "ContentType": "image/jpeg",
                "CacheControl": "public, max-age=31536000, immutable",
            },
        )
        uploaded += 1
    return uploaded, reused


def command_download(args: argparse.Namespace) -> int:
    client, bucket = client_and_bucket()
    prefix = validate_prefix(args.prefix)
    found: list[str] = []
    if args.state:
        if download_json(client, bucket, f"{prefix}/state.json", Path(args.state), "state"):
            found.append("state")
    if args.index:
        if download_json(client, bucket, f"{prefix}/index.json", Path(args.index), "index"):
            found.append("index")
    print(f"chart_search_download found={','.join(found) or 'none'}")
    return 0


def command_publish(args: argparse.Namespace) -> int:
    state_path = Path(args.state)
    index_path = Path(args.index)
    load_publish_document(state_path, "state")
    index = load_publish_document(index_path, "index")
    client, bucket = client_and_bucket()
    prefix = validate_prefix(args.prefix)
    uploaded, reused = publish_assets(client, bucket, prefix, Path(args.asset_dir))
    put_json(client, bucket, f"{prefix}/state.json", state_path, private=True)
    # Publish the index last, after all referenced immutable images are available.
    put_json(client, bucket, f"{prefix}/index.json", index_path, private=False)
    print(
        "chart_search_publish "
        f"reports={int(index.get('report_count') or 0)} charts={int(index.get('item_count') or 0)} "
        f"images_uploaded={uploaded} images_reused={reused}"
    )
    return 0


def command_publish_state(args: argparse.Namespace) -> int:
    state_path = Path(args.state)
    state = load_publish_document(state_path, "state")
    client, bucket = client_and_bucket()
    prefix = validate_prefix(args.prefix)
    put_json(client, bucket, f"{prefix}/state.json", state_path, private=True)
    print(f"chart_search_state_publish items={len(state.get('items') or {})}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    download = subparsers.add_parser("download")
    download.add_argument("--prefix", default=DEFAULT_PREFIX)
    download.add_argument("--state", default="")
    download.add_argument("--index", default="")
    download.set_defaults(handler=command_download)

    publish = subparsers.add_parser("publish")
    publish.add_argument("--prefix", default=DEFAULT_PREFIX)
    publish.add_argument("--state", required=True)
    publish.add_argument("--index", required=True)
    publish.add_argument("--asset-dir", required=True)
    publish.set_defaults(handler=command_publish)

    publish_state = subparsers.add_parser("publish-state")
    publish_state.add_argument("--prefix", default=DEFAULT_PREFIX)
    publish_state.add_argument("--state", required=True)
    publish_state.set_defaults(handler=command_publish_state)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "download" and not (args.state or args.index):
        raise RuntimeError("At least one download destination is required")
    return int(args.handler(args))


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
