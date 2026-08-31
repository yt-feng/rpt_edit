#!/usr/bin/env python3
"""Incrementally publish a complete static site into an inactive R2 slot.

The active edge Worker reads one of two complete namespaces.  A refresh updates
only changed objects in the other namespace, verifies the resulting tree, then
the workflow deploys a Worker version that points at the prepared slot.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Iterable

from check_public_brand import check_public_brand


SCHEMA_VERSION = 1
RUNTIME_SCHEMA_VERSION = 1
RELEASE_PATTERN = re.compile(r"^[0-9a-f]{32}$")
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
SLOTS = ("a", "b")
SLOT_ROOT = "edge-static/slots"
MANIFEST_ROOT = "edge-static/slot-manifests"
INCOMPLETE_ROOT = "edge-static/slot-incomplete"
RUNTIME_ROOT = "edge-static/runtime-data"
RUNTIME_RELEASE_ROOT = f"{RUNTIME_ROOT}/releases"

DEFAULT_RUNTIME_PATHS = (
    "data/catalog.json",
    "data/search_index.json",
    "data/password_rules.json",
)

DEFAULT_REQUIRED_PATHS = (
    "reports/institutions/bernstein/index.html",
    "b7c3e9a41d8f52e604a71bc93f2d6e80.txt",
    "data/catalog_recommendations.json",
)


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Required environment value is missing: {name}")
    return value


def validate_release(value: str) -> str:
    release = str(value or "").strip().lower()
    if not RELEASE_PATTERN.fullmatch(release):
        raise ValueError("Release id must contain exactly 32 lowercase hex characters")
    return release


def validate_slot(value: str, *, allow_empty: bool = False) -> str:
    slot = str(value or "").strip().lower()
    if allow_empty and not slot:
        return ""
    if slot not in SLOTS:
        raise ValueError("Static slot must be a or b")
    return slot


def target_slot(active_slot: str) -> str:
    active = validate_slot(active_slot, allow_empty=True)
    return "b" if active == "a" else "a"


def safe_relative_path(value: str) -> str:
    relative = str(value or "")
    if (
        not relative
        or relative.startswith("/")
        or "\\" in relative
        or "\0" in relative
        or any(part in {"", ".", ".."} for part in relative.split("/"))
    ):
        raise ValueError("Static inventory contains an unsafe relative path")
    return relative


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cache_control_for(path: Path) -> str:
    if path.suffix.lower() in {".html", ".json", ".xml", ".txt"}:
        return "public, max-age=0, must-revalidate"
    return "public, max-age=3600"


def describe_file(path: Path) -> dict[str, Any]:
    content_type, content_encoding = mimetypes.guess_type(path.name)
    descriptor: dict[str, Any] = {
        "sha256": sha256_file(path),
        "size": path.stat().st_size,
        "content_type": content_type or "application/octet-stream",
        "cache_control": cache_control_for(path),
    }
    if content_encoding:
        descriptor["content_encoding"] = content_encoding
    return descriptor


def build_inventory(root: Path) -> tuple[dict[str, Path], dict[str, dict[str, Any]], str, int]:
    if not root.is_dir() or root.is_symlink():
        raise ValueError("Static site root must be a real directory")
    paths: dict[str, Path] = {}
    entries: dict[str, dict[str, Any]] = {}
    tree_digest = hashlib.sha256()
    total_bytes = 0
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("Static site must not contain symbolic links")
        if not path.is_file():
            continue
        relative = safe_relative_path(path.relative_to(root).as_posix())
        descriptor = describe_file(path)
        paths[relative] = path
        entries[relative] = descriptor
        total_bytes += int(descriptor["size"])
        tree_digest.update(relative.encode("utf-8"))
        tree_digest.update(b"\0")
        tree_digest.update(
            json.dumps(descriptor, sort_keys=True, separators=(",", ":")).encode("utf-8")
        )
        tree_digest.update(b"\n")
    if not paths:
        raise ValueError("Static site contains no files")
    return paths, entries, tree_digest.hexdigest(), total_bytes


def body_bytes(body: Any) -> bytes:
    if hasattr(body, "read"):
        payload = body.read()
    else:
        payload = body
    if isinstance(payload, str):
        return payload.encode("utf-8")
    return bytes(payload)


def read_json_object(client: Any, bucket: str, key: str) -> dict[str, Any] | None:
    try:
        response = client.get_object(Bucket=bucket, Key=key)
    except Exception as error:  # botocore is optional during local unit tests.
        response_code = str(
            getattr(error, "response", {}).get("Error", {}).get("Code", "")
        ).lower()
        if response_code in {"404", "nosuchkey", "notfound"} or isinstance(error, KeyError):
            return None
        raise
    payload = json.loads(body_bytes(response["Body"]).decode("utf-8"))
    return payload if isinstance(payload, dict) else None


def manifest_key(slot: str) -> str:
    return f"{MANIFEST_ROOT}/{validate_slot(slot)}.json"


def incomplete_key(slot: str) -> str:
    return f"{INCOMPLETE_ROOT}/{validate_slot(slot)}.json"


def slot_prefix(slot: str) -> str:
    return f"{SLOT_ROOT}/{validate_slot(slot)}/"


def runtime_release_prefix(release_id: str) -> str:
    return f"{RUNTIME_RELEASE_ROOT}/{validate_release(release_id)}/"


def runtime_manifest_key(release_id: str) -> str:
    return f"{runtime_release_prefix(release_id)}manifest.json"


def valid_manifest(payload: dict[str, Any] | None, slot: str) -> dict[str, Any] | None:
    if not isinstance(payload, dict):
        return None
    if payload.get("schema_version") != SCHEMA_VERSION or payload.get("slot") != slot:
        return None
    if not RELEASE_PATTERN.fullmatch(str(payload.get("release_id") or "")):
        return None
    if not SHA256_PATTERN.fullmatch(str(payload.get("tree_sha256") or "")):
        return None
    files = payload.get("files")
    if not isinstance(files, dict) or int(payload.get("file_count", -1)) != len(files):
        return None
    normalized: dict[str, dict[str, Any]] = {}
    try:
        for relative, descriptor in files.items():
            safe_relative_path(relative)
            if not isinstance(descriptor, dict):
                return None
            if not SHA256_PATTERN.fullmatch(str(descriptor.get("sha256") or "")):
                return None
            if int(descriptor.get("size", -1)) < 0:
                return None
            normalized[relative] = descriptor
    except (TypeError, ValueError):
        return None
    return {**payload, "files": normalized}


def list_objects(client: Any, bucket: str, prefix: str) -> dict[str, int]:
    objects: dict[str, int] = {}
    paginator = client.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for item in page.get("Contents", []):
            key = str(item.get("Key") or "")
            if key.startswith(prefix):
                objects[key] = int(item.get("Size") or 0)
    return objects


def json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def put_json(client: Any, bucket: str, key: str, payload: dict[str, Any], **kwargs: Any) -> None:
    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=json_bytes(payload),
        ContentType="application/json",
        CacheControl="no-store",
        **kwargs,
    )


def delete_keys(client: Any, bucket: str, keys: Iterable[str]) -> int:
    values = sorted(set(keys))
    deleted = 0
    for offset in range(0, len(values), 1000):
        chunk = values[offset:offset + 1000]
        response = client.delete_objects(
            Bucket=bucket,
            Delete={"Objects": [{"Key": key} for key in chunk], "Quiet": True},
        )
        if response.get("Errors"):
            raise RuntimeError("Static slot cleanup was incomplete")
        deleted += len(chunk)
    return deleted


def upload_extra_args(descriptor: dict[str, Any]) -> dict[str, Any]:
    extra: dict[str, Any] = {
        "ContentType": descriptor["content_type"],
        "CacheControl": descriptor["cache_control"],
        "Metadata": {"sha256": descriptor["sha256"]},
    }
    if descriptor.get("content_encoding"):
        extra["ContentEncoding"] = descriptor["content_encoding"]
    return extra


def required_release_paths(root: Path) -> tuple[str, ...]:
    catalog = json.loads((root / "data" / "catalog.json").read_text(encoding="utf-8"))
    report_id = next(
        (str(item.get("id") or "") for item in catalog.get("items", []) if item.get("id")),
        "",
    )
    if not report_id:
        raise ValueError("Catalog has no report id for static slot verification")
    detail_prefix = re.sub(r"[^a-z0-9]", "_", report_id.lower())[:2].ljust(2, "_")
    return (*DEFAULT_REQUIRED_PATHS, f"data/report_details/{detail_prefix}.json")


def verify_required_objects(
    client: Any,
    bucket: str,
    prefix: str,
    paths: dict[str, Path],
    entries: dict[str, dict[str, Any]],
    required: Iterable[str],
) -> int:
    verified = 0
    for relative_value in required:
        relative = safe_relative_path(relative_value)
        if relative not in paths or paths[relative].stat().st_size <= 0:
            raise RuntimeError(f"Required static release path is missing: {relative}")
        metadata = client.head_object(Bucket=bucket, Key=prefix + relative)
        if int(metadata.get("ContentLength", -1)) != int(entries[relative]["size"]):
            raise RuntimeError(f"Required static release object has the wrong size: {relative}")
        remote_sha = str((metadata.get("Metadata") or {}).get("sha256") or "")
        if remote_sha and remote_sha != entries[relative]["sha256"]:
            raise RuntimeError(f"Required static release object has the wrong digest: {relative}")
        verified += 1
    return verified


def runtime_tree_sha256(entries: dict[str, dict[str, Any]]) -> str:
    tree_digest = hashlib.sha256()
    for filename, descriptor in sorted(entries.items()):
        tree_digest.update(filename.encode("utf-8"))
        tree_digest.update(b"\0")
        tree_digest.update(
            json.dumps(descriptor, sort_keys=True, separators=(",", ":")).encode("utf-8")
        )
        tree_digest.update(b"\n")
    return tree_digest.hexdigest()


def runtime_inventory(
    root: Path,
    paths: Iterable[str] = DEFAULT_RUNTIME_PATHS,
) -> tuple[dict[str, Path], dict[str, dict[str, Any]], str]:
    runtime_paths: dict[str, Path] = {}
    entries: dict[str, dict[str, Any]] = {}
    for relative_value in paths:
        relative = safe_relative_path(relative_value)
        path = root / relative
        if not path.is_file() or path.is_symlink():
            raise RuntimeError(f"Runtime data path is missing: {relative}")
        filename = path.name
        if filename in runtime_paths:
            raise RuntimeError(f"Runtime data filenames must be unique: {filename}")
        descriptor = describe_file(path)
        descriptor["content_type"] = "application/json"
        descriptor["cache_control"] = "no-store"
        runtime_paths[filename] = path
        entries[filename] = descriptor
    if not runtime_paths:
        raise RuntimeError("Runtime data inventory is empty")
    return runtime_paths, entries, runtime_tree_sha256(entries)


def valid_runtime_manifest(
    payload: dict[str, Any] | None,
    release_id: str,
) -> dict[str, Any] | None:
    release = validate_release(release_id)
    if not isinstance(payload, dict):
        return None
    if (
        payload.get("schema_version") != RUNTIME_SCHEMA_VERSION
        or payload.get("release_id") != release
        or payload.get("prefix") != runtime_release_prefix(release)
        or not SHA256_PATTERN.fullmatch(str(payload.get("tree_sha256") or ""))
    ):
        return None
    files = payload.get("files")
    if not isinstance(files, dict) or int(payload.get("file_count", -1)) != len(files):
        return None
    normalized: dict[str, dict[str, Any]] = {}
    try:
        for filename, descriptor in files.items():
            if safe_relative_path(filename) != Path(filename).name:
                return None
            if not isinstance(descriptor, dict):
                return None
            if not SHA256_PATTERN.fullmatch(str(descriptor.get("sha256") or "")):
                return None
            if int(descriptor.get("size", -1)) < 0:
                return None
            if descriptor.get("content_type") != "application/json":
                return None
            if descriptor.get("cache_control") != "no-store":
                return None
            normalized[filename] = descriptor
    except (TypeError, ValueError):
        return None
    if runtime_tree_sha256(normalized) != payload["tree_sha256"]:
        return None
    return {**payload, "files": normalized}


def runtime_object_matches(
    metadata: dict[str, Any] | None,
    descriptor: dict[str, Any],
    release_id: str,
) -> bool:
    if not metadata:
        return False
    custom = metadata.get("Metadata") or {}
    return (
        int(metadata.get("ContentLength", -1)) == int(descriptor["size"])
        and str(custom.get("sha256") or "") == descriptor["sha256"]
        and str(custom.get("release-id") or "") == release_id
        and str(metadata.get("ContentType") or "").lower() == descriptor["content_type"]
        and str(metadata.get("CacheControl") or "").lower() == descriptor["cache_control"]
    )


def sync_runtime_data(
    client: Any,
    bucket: str,
    root: Path,
    release_id: str,
    paths: Iterable[str] = DEFAULT_RUNTIME_PATHS,
    transfer_config: Any = None,
) -> tuple[int, int, dict[str, Any]]:
    release = validate_release(release_id)
    prefix = runtime_release_prefix(release)
    runtime_paths, entries, tree_sha256 = runtime_inventory(root, paths)
    committed = valid_runtime_manifest(
        read_json_object(client, bucket, runtime_manifest_key(release)),
        release,
    )
    if committed and (
        committed["files"] != entries
        or committed["tree_sha256"] != tree_sha256
    ):
        raise RuntimeError("Runtime data release id is already committed with different content")

    uploaded = 0
    skipped = 0
    for filename, path in runtime_paths.items():
        descriptor = entries[filename]
        key = f"{prefix}{filename}"
        current = None
        try:
            current = client.head_object(Bucket=bucket, Key=key)
        except Exception as error:
            response_code = str(
                getattr(error, "response", {}).get("Error", {}).get("Code", "")
            ).lower()
            if response_code not in {"404", "nosuchkey", "notfound"} and not isinstance(error, KeyError):
                raise
        if runtime_object_matches(current, descriptor, release):
            skipped += 1
            continue
        kwargs = {
            "ExtraArgs": {
                "ContentType": descriptor["content_type"],
                "CacheControl": descriptor["cache_control"],
                "Metadata": {
                    "sha256": descriptor["sha256"],
                    "release-id": release,
                },
            }
        }
        if transfer_config is not None:
            kwargs["Config"] = transfer_config
        client.upload_file(str(path), bucket, key, **kwargs)
        verified = client.head_object(Bucket=bucket, Key=key)
        if not runtime_object_matches(verified, descriptor, release):
            raise RuntimeError(f"Runtime data verification failed: {filename}")
        uploaded += 1

    manifest = {
        "schema_version": RUNTIME_SCHEMA_VERSION,
        "release_id": release,
        "prefix": prefix,
        "tree_sha256": tree_sha256,
        "file_count": len(entries),
        "files": entries,
    }
    put_json(
        client,
        bucket,
        runtime_manifest_key(release),
        manifest,
        Metadata={"tree-sha256": tree_sha256, "release-id": release},
    )
    verified_manifest = valid_runtime_manifest(
        read_json_object(client, bucket, runtime_manifest_key(release)),
        release,
    )
    if not verified_manifest or verified_manifest != manifest:
        raise RuntimeError("Runtime data manifest verification failed")
    return uploaded, skipped, manifest


def publish_static_slot(
    client: Any,
    bucket: str,
    root: Path,
    release_id: str,
    active_slot: str = "",
    *,
    max_workers: int = 10,
    transfer_config: Any = None,
    required: Iterable[str] | None = None,
    runtime_paths: Iterable[str] = DEFAULT_RUNTIME_PATHS,
) -> dict[str, Any]:
    release = validate_release(release_id)
    active = validate_slot(active_slot, allow_empty=True)
    slot = target_slot(active)
    prefix = slot_prefix(slot)
    check_public_brand(root)
    paths, entries, tree_sha256, total_bytes = build_inventory(root)
    previous = valid_manifest(read_json_object(client, bucket, manifest_key(slot)), slot)
    incomplete = read_json_object(client, bucket, incomplete_key(slot))
    previous_release = str((previous or {}).get("release_id") or "")
    incomplete_release = str((incomplete or {}).get("release_id") or "")
    force_reupload = bool(incomplete_release and incomplete_release != previous_release)
    remote_before = list_objects(client, bucket, prefix)

    put_json(
        client,
        bucket,
        incomplete_key(slot),
        {"schema_version": SCHEMA_VERSION, "slot": slot, "release_id": release},
    )

    previous_files = (previous or {}).get("files") or {}
    upload_relatives = []
    skipped = 0
    for relative, descriptor in entries.items():
        key = prefix + relative
        if (
            not force_reupload
            and previous_files.get(relative) == descriptor
            and remote_before.get(key) == int(descriptor["size"])
        ):
            skipped += 1
        else:
            upload_relatives.append(relative)

    def upload(relative: str) -> tuple[str, int]:
        descriptor = entries[relative]
        kwargs: dict[str, Any] = {"ExtraArgs": upload_extra_args(descriptor)}
        if transfer_config is not None:
            kwargs["Config"] = transfer_config
        client.upload_file(str(paths[relative]), bucket, prefix + relative, **kwargs)
        return relative, int(descriptor["size"])

    uploaded_bytes = 0
    with ThreadPoolExecutor(max_workers=max(1, int(max_workers))) as executor:
        futures = {executor.submit(upload, relative): relative for relative in upload_relatives}
        for future in as_completed(futures):
            _relative, size = future.result()
            uploaded_bytes += size

    desired_keys = {prefix + relative for relative in entries}
    stale_keys = set(remote_before) - desired_keys
    deleted = delete_keys(client, bucket, stale_keys)

    remote_after = list_objects(client, bucket, prefix)
    expected_sizes = {prefix + relative: int(descriptor["size"]) for relative, descriptor in entries.items()}
    if remote_after != expected_sizes:
        missing = len(set(expected_sizes) - set(remote_after))
        unexpected = len(set(remote_after) - set(expected_sizes))
        wrong_size = sum(
            1 for key in set(remote_after) & set(expected_sizes) if remote_after[key] != expected_sizes[key]
        )
        raise RuntimeError(
            f"Static slot verification failed: missing={missing} unexpected={unexpected} wrong_size={wrong_size}"
        )

    verified_required = verify_required_objects(
        client,
        bucket,
        prefix,
        paths,
        entries,
        required if required is not None else required_release_paths(root),
    )
    runtime_uploaded, runtime_skipped, runtime_manifest = sync_runtime_data(
        client,
        bucket,
        root,
        release,
        paths=runtime_paths,
        transfer_config=transfer_config,
    )
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "slot": slot,
        "release_id": release,
        "tree_sha256": tree_sha256,
        "file_count": len(entries),
        "total_bytes": total_bytes,
        "files": entries,
        "runtime_data": {
            "schema_version": runtime_manifest["schema_version"],
            "release_id": runtime_manifest["release_id"],
            "prefix": runtime_manifest["prefix"],
            "tree_sha256": runtime_manifest["tree_sha256"],
        },
    }
    put_json(
        client,
        bucket,
        manifest_key(slot),
        manifest,
        Metadata={"tree-sha256": tree_sha256, "release-id": release},
    )
    delete_keys(client, bucket, (incomplete_key(slot),))

    return {
        "static_slot": slot,
        "static_prefix": prefix,
        "release_id": release,
        "tree_sha256": tree_sha256,
        "file_count": len(entries),
        "total_bytes": total_bytes,
        "uploaded_files": len(upload_relatives),
        "uploaded_bytes": uploaded_bytes,
        "skipped_files": skipped,
        "deleted_files": deleted,
        "runtime_uploaded_files": runtime_uploaded,
        "runtime_skipped_files": runtime_skipped,
        "runtime_prefix": runtime_manifest["prefix"],
        "runtime_tree_sha256": runtime_manifest["tree_sha256"],
        "verified_release_objects": verified_required,
        "recovered_incomplete_slot": force_reupload,
    }


def build_r2_client() -> tuple[Any, Any]:
    import boto3
    from boto3.s3.transfer import TransferConfig
    from botocore.config import Config

    client = boto3.client(
        "s3",
        endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
        config=Config(
            signature_version="s3v4",
            max_pool_connections=24,
            retries={"max_attempts": 8, "mode": "adaptive"},
        ),
    )
    transfer = TransferConfig(
        multipart_threshold=16 * 1024 * 1024,
        multipart_chunksize=16 * 1024 * 1024,
        max_concurrency=10,
        use_threads=True,
    )
    return client, transfer


def append_github_values(path_value: str, values: dict[str, Any]) -> None:
    if not path_value:
        return
    path = Path(path_value)
    with path.open("a", encoding="utf-8") as handle:
        for name, value in values.items():
            text = str(value)
            if "\n" in text or "\r" in text:
                raise ValueError("GitHub output values must be single-line")
            handle.write(f"{name}={text}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="_neutral_site")
    parser.add_argument("--release", default=os.environ.get("STATIC_RELEASE", ""))
    parser.add_argument("--active-slot", default=os.environ.get("ACTIVE_STATIC_SLOT", ""))
    parser.add_argument("--max-workers", type=int, default=10)
    args = parser.parse_args()

    try:
        client, transfer = build_r2_client()
        result = publish_static_slot(
            client,
            require_env("R2_BUCKET"),
            Path(args.root),
            args.release,
            args.active_slot,
            max_workers=args.max_workers,
            transfer_config=transfer,
        )
        append_github_values(
            os.environ.get("GITHUB_ENV", ""),
            {
                "STATIC_SLOT": result["static_slot"],
                "STATIC_PREFIX": result["static_prefix"],
                "STATIC_TREE_SHA256": result["tree_sha256"],
            },
        )
        append_github_values(
            os.environ.get("GITHUB_OUTPUT", ""),
            {
                key: str(value).lower() if isinstance(value, bool) else value
                for key, value in result.items()
            },
        )
        print(
            " ".join(
                f"{key}={result[key]}"
                for key in (
                    "static_slot",
                    "file_count",
                    "uploaded_files",
                    "skipped_files",
                    "deleted_files",
                    "runtime_uploaded_files",
                    "runtime_skipped_files",
                    "verified_release_objects",
                    "recovered_incomplete_slot",
                )
            )
        )
        return 0
    except Exception as error:
        print(f"Incremental static publish failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
