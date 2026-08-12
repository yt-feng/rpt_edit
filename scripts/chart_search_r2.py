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
DEFAULT_STORAGE_BUDGET_BYTES = 1024 * 1024 * 1024
PUBLIC_ANALYSIS_VERSION = "chart-search-v2"
ASSET_RE = re.compile(r"^[0-9a-f]{64}\.jpg$")
IMAGE_ID_RE = re.compile(r"^[0-9a-f]{64}$")


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
        return {"schema_version": 1, "analysis_version": "chart-search-v2", "items": {}}
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


def list_prefix_objects(client: Any, bucket: str, prefix: str) -> list[dict[str, Any]]:
    objects: list[dict[str, Any]] = []
    continuation = ""
    while True:
        kwargs: dict[str, Any] = {"Bucket": bucket, "Prefix": f"{prefix}/"}
        if continuation:
            kwargs["ContinuationToken"] = continuation
        response = client.list_objects_v2(**kwargs)
        objects.extend(row for row in response.get("Contents", []) if isinstance(row, dict))
        if not response.get("IsTruncated"):
            return objects
        continuation = str(response.get("NextContinuationToken") or "")
        if not continuation:
            raise RuntimeError("Chart object listing was truncated without a continuation token")


def object_age_rank(value: Any) -> float:
    if hasattr(value, "timestamp"):
        try:
            return float(value.timestamp())
        except (OSError, OverflowError, ValueError):
            return 0.0
    return 0.0


def report_date_rank(value: Any) -> int:
    digits = re.sub(r"\D", "", str(value or ""))
    if len(digits) == 6:
        return 20_000_000 + int(digits)
    if len(digits) == 8:
        return int(digits)
    return 0


def referenced_image_recency(index: dict[str, Any]) -> dict[str, int]:
    recency: dict[str, int] = {}
    for report in index.get("reports", []):
        if not isinstance(report, dict):
            continue
        rank = report_date_rank(report.get("date_folder"))
        for chart in report.get("charts", []):
            image_id = str(chart.get("image_id") or "") if isinstance(chart, dict) else ""
            if (
                isinstance(chart, dict)
                and str(chart.get("analysis_version") or "") == PUBLIC_ANALYSIS_VERSION
                and IMAGE_ID_RE.fullmatch(image_id)
            ):
                recency[image_id] = max(recency.get(image_id, 0), rank)
    return recency


def bounded_chart_search_text(report: dict[str, Any]) -> str:
    chunks: list[str] = [" ".join(str(report.get("title") or "").split())[:300]]
    for chart in report.get("charts", []):
        if not isinstance(chart, dict):
            continue
        for field in (
            "analysis_version", "title", "content_kind", "chart_type", "description", "trend_summary",
            "metrics", "entities", "periods", "geographies", "units", "keywords",
        ):
            value = chart.get(field)
            if isinstance(value, list):
                chunks.extend(" ".join(str(item or "").split())[:160] for item in value)
            else:
                chunks.append(" ".join(str(value or "").split())[:900])
    return " ".join(chunk for chunk in chunks if chunk)[:12_000]


def filter_index_images(index: dict[str, Any], retained: set[str]) -> int:
    removed = 0
    reports: list[dict[str, Any]] = []
    for report in index.get("reports", []):
        if not isinstance(report, dict):
            continue
        charts = [
            chart
            for chart in report.get("charts", [])
            if (
                isinstance(chart, dict)
                and str(chart.get("analysis_version") or "") == PUBLIC_ANALYSIS_VERSION
                and str(chart.get("image_id") or "") in retained
            )
        ]
        removed += len([chart for chart in report.get("charts", []) if isinstance(chart, dict)]) - len(charts)
        if not charts:
            continue
        report["charts"] = charts
        report["chart_count"] = len(charts)
        report["search_text"] = bounded_chart_search_text(report)
        reports.append(report)
    index["reports"] = reports
    index["report_count"] = len(reports)
    index["item_count"] = sum(int(report.get("chart_count") or 0) for report in reports)
    return removed


def delete_object_keys(client: Any, bucket: str, keys: list[str]) -> None:
    for offset in range(0, len(keys), 1000):
        batch = keys[offset : offset + 1000]
        if batch:
            client.delete_objects(
                Bucket=bucket,
                Delete={"Objects": [{"Key": key} for key in batch], "Quiet": True},
            )


def pretty_json_size(value: dict[str, Any]) -> int:
    return len((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def enforce_storage_budget(
    client: Any,
    bucket: str,
    prefix: str,
    index: dict[str, Any],
    *,
    budget_bytes: int,
) -> dict[str, int]:
    """Keep the newest referenced images and evict unreferenced/oldest objects first."""
    budget_bytes = int(budget_bytes)
    if budget_bytes <= 0:
        raise RuntimeError("Chart storage budget must be positive")
    v2_recency = referenced_image_recency(index)
    removed_records = filter_index_images(index, set(v2_recency))
    objects = list_prefix_objects(client, bucket, prefix)
    image_prefix = f"{prefix}/images/"
    index_key = f"{prefix}/index.json"
    images: list[dict[str, Any]] = []
    fixed_bytes = pretty_json_size(index)
    for row in objects:
        key = str(row.get("Key") or "")
        size = max(0, int(row.get("Size") or 0))
        name = key[len(image_prefix) :] if key.startswith(image_prefix) else ""
        if name and "/" not in name and ASSET_RE.fullmatch(name):
            images.append({**row, "Key": key, "Size": size, "image_id": name[:-4]})
        elif key != index_key:
            fixed_bytes += size
    if fixed_bytes > budget_bytes:
        raise RuntimeError("Chart metadata exceeds the configured storage budget")

    recency = referenced_image_recency(index)
    available = budget_bytes - fixed_bytes
    candidates = [row for row in images if row["image_id"] in recency]
    candidates.sort(
        key=lambda row: (
            recency.get(str(row["image_id"]), 0),
            object_age_rank(row.get("LastModified")),
            str(row.get("Key") or ""),
        )
    )
    retained: set[str] = {str(row["image_id"]) for row in candidates}
    retained_image_bytes = sum(int(row.get("Size") or 0) for row in candidates)
    for row in candidates:
        if retained_image_bytes <= available:
            break
        retained.discard(str(row["image_id"]))
        retained_image_bytes -= int(row.get("Size") or 0)

    evicted_keys = [
        str(row["Key"])
        for row in images
        if str(row["image_id"]) not in retained
    ]
    delete_object_keys(client, bucket, evicted_keys)
    removed_records += filter_index_images(index, retained)
    return {
        "budget_bytes": budget_bytes,
        "fixed_bytes": fixed_bytes,
        "image_bytes": retained_image_bytes,
        "images_retained": len(retained),
        "images_evicted": len(evicted_keys),
        "records_removed": removed_records,
    }


def prefix_size_bytes(client: Any, bucket: str, prefix: str) -> int:
    return sum(max(0, int(row.get("Size") or 0)) for row in list_prefix_objects(client, bucket, prefix))


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
    storage_budget_bytes = int(getattr(args, "max_storage_bytes", DEFAULT_STORAGE_BUDGET_BYTES))
    uploaded, reused = publish_assets(client, bucket, prefix, Path(args.asset_dir))
    put_json(client, bucket, f"{prefix}/state.json", state_path, private=True)
    retention = enforce_storage_budget(
        client,
        bucket,
        prefix,
        index,
        budget_bytes=storage_budget_bytes,
    )
    atomic_write(index_path, index)
    # Publish the index last, after all referenced immutable images are available.
    put_json(client, bucket, f"{prefix}/index.json", index_path, private=False)
    total_bytes = prefix_size_bytes(client, bucket, prefix)
    if total_bytes > storage_budget_bytes:
        raise RuntimeError("Chart storage budget verification failed")
    print(
        "chart_search_publish "
        f"reports={int(index.get('report_count') or 0)} charts={int(index.get('item_count') or 0)} "
        f"images_uploaded={uploaded} images_reused={reused} "
        f"images_evicted={retention['images_evicted']} records_removed={retention['records_removed']} "
        f"stored_bytes={total_bytes} budget_bytes={storage_budget_bytes}"
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
    publish.add_argument("--max-storage-bytes", type=int, default=DEFAULT_STORAGE_BUDGET_BYTES)
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
