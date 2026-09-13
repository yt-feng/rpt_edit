#!/usr/bin/env python3
"""Move generated workflow directories through a private Cloudflare R2 prefix.

The public repository contains only source code. Generated report text and images are
packed into short-lived ``.tar.gz`` objects in a private R2 bucket, then materialized
by downstream jobs. Raw PDFs, ZIPs, media files, and MinerU raw directories are never
included in the handoff archive.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


EXCLUDED_DIR_NAMES = {".git", "__pycache__", "mineru_raw"}
EXCLUDED_SUFFIXES = {".pdf", ".zip", ".mp3", ".wav", ".m4a", ".mp4", ".mov"}
SHARD_KEY_RE = re.compile(r"(?:^|/)shard_(\d+)\.tar\.gz$")
RUN_ID_RE = re.compile(r"^\d+$")


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is required")
    return value


def build_r2_client() -> Any:
    try:
        import boto3  # type: ignore
    except ImportError as exc:  # pragma: no cover - exercised in Actions
        raise RuntimeError("boto3 is required; install it with: python -m pip install boto3") from exc

    account_id = require_env("R2_ACCOUNT_ID")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
    )


def r2_bucket() -> str:
    return require_env("R2_BUCKET")


def validate_key(key: str) -> str:
    cleaned = key.strip().lstrip("/")
    path = PurePosixPath(cleaned)
    if not cleaned or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe R2 object key: {key!r}")
    if not cleaned.endswith(".tar.gz"):
        raise ValueError(f"Handoff key must end with .tar.gz: {cleaned}")
    return cleaned


def validate_prefix(prefix: str) -> str:
    cleaned = prefix.strip().strip("/")
    path = PurePosixPath(cleaned)
    if not cleaned or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe R2 prefix: {prefix!r}")
    return cleaned + "/"


def is_private_handoff_file(path: Path, source: Path) -> bool:
    relative = path.relative_to(source)
    if any(part in EXCLUDED_DIR_NAMES for part in relative.parts[:-1]):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    return path.is_file() and not path.is_symlink()


def iter_handoff_files(source: Path) -> Iterable[Path]:
    for path in sorted(source.rglob("*")):
        if is_private_handoff_file(path, source):
            yield path


def create_archive(source: Path, archive_path: Path) -> tuple[int, int, str]:
    source = source.resolve()
    if not source.is_dir():
        raise RuntimeError(f"Handoff source directory does not exist: {source}")

    file_count = 0
    with tarfile.open(archive_path, "w:gz", format=tarfile.PAX_FORMAT) as archive:
        for path in iter_handoff_files(source):
            archive.add(path, arcname=path.relative_to(source).as_posix(), recursive=False)
            file_count += 1

    if file_count == 0:
        raise RuntimeError(f"No private handoff files found under {source}")
    size = archive_path.stat().st_size
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    return file_count, size, digest


def _safe_members(archive: tarfile.TarFile, destination: Path) -> list[tarfile.TarInfo]:
    destination = destination.resolve()
    safe: list[tarfile.TarInfo] = []
    for member in archive.getmembers():
        member_path = PurePosixPath(member.name)
        if member_path.is_absolute() or ".." in member_path.parts:
            raise RuntimeError(f"Unsafe archive member: {member.name}")
        if member.issym() or member.islnk() or member.isdev():
            raise RuntimeError(f"Unsupported archive member: {member.name}")
        resolved = (destination / Path(*member_path.parts)).resolve()
        if resolved != destination and destination not in resolved.parents:
            raise RuntimeError(f"Archive member escapes destination: {member.name}")
        safe.append(member)
    return safe


def extract_archive(archive_path: Path, destination: Path, *, replace: bool = True) -> int:
    if replace and destination.is_symlink():
        destination.unlink()
    elif replace and destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive_path, "r:gz") as archive:
        members = _safe_members(archive, destination)
        archive.extractall(destination, members=members)
    return sum(1 for path in destination.rglob("*") if path.is_file())


def upload_directory(source: Path, key: str, *, client: Any | None = None, bucket: str | None = None) -> None:
    key = validate_key(key)
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    with tempfile.TemporaryDirectory(prefix="private-handoff-") as temp_dir:
        archive_path = Path(temp_dir) / "payload.tar.gz"
        file_count, size, digest = create_archive(source, archive_path)
        resolved_client.upload_file(
            str(archive_path),
            resolved_bucket,
            key,
            ExtraArgs={
                "ContentType": "application/gzip",
                "Metadata": {
                    "sha256": digest,
                    "file-count": str(file_count),
                },
            },
        )
        head = resolved_client.head_object(Bucket=resolved_bucket, Key=key)
        stored_size = int(head.get("ContentLength") or 0)
        if stored_size != size:
            raise RuntimeError(f"R2 size verification failed for {key}: local={size}, remote={stored_size}")
        print(f"Uploaded private handoff: key={key}, files={file_count}, bytes={size}")


def download_directory(
    key: str,
    destination: Path,
    *,
    client: Any | None = None,
    bucket: str | None = None,
) -> int:
    key = validate_key(key)
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    with tempfile.TemporaryDirectory(prefix="private-handoff-") as temp_dir:
        archive_path = Path(temp_dir) / "payload.tar.gz"
        resolved_client.download_file(resolved_bucket, key, str(archive_path))
        head = resolved_client.head_object(Bucket=resolved_bucket, Key=key)
        expected_digest = str((head.get("Metadata") or {}).get("sha256") or "").strip()
        if expected_digest:
            actual_digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
            if actual_digest != expected_digest:
                raise RuntimeError(f"R2 checksum verification failed for {key}")
        count = extract_archive(archive_path, destination)
    if count == 0:
        raise RuntimeError(f"Private handoff extracted no files: {key}")
    print(f"Downloaded private handoff: key={key}, files={count}, destination={destination}")
    return count


def list_keys(prefix: str, *, client: Any | None = None, bucket: str | None = None) -> list[str]:
    prefix = validate_prefix(prefix)
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    keys: list[str] = []
    token: str | None = None
    while True:
        kwargs: dict[str, Any] = {"Bucket": resolved_bucket, "Prefix": prefix}
        if token:
            kwargs["ContinuationToken"] = token
        response = resolved_client.list_objects_v2(**kwargs)
        keys.extend(
            str(item.get("Key"))
            for item in response.get("Contents", [])
            if item.get("Key")
        )
        if not response.get("IsTruncated"):
            break
        token = str(response.get("NextContinuationToken") or "")
        if not token:
            raise RuntimeError(f"R2 listing for {prefix} was truncated without a continuation token")
    return sorted(keys)


def download_shards(
    prefix: str,
    destination: Path,
    expected_count: int = 0,
    *,
    client: Any | None = None,
    bucket: str | None = None,
) -> int:
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    shard_keys: list[tuple[int, str]] = []
    for key in list_keys(prefix, client=resolved_client, bucket=resolved_bucket):
        match = SHARD_KEY_RE.search(key)
        if match:
            shard_keys.append((int(match.group(1)), key))
    shard_keys.sort()
    if not shard_keys:
        raise RuntimeError(f"No shard handoffs found under {validate_prefix(prefix)}")
    indices = [index for index, _key in shard_keys]
    if len(set(indices)) != len(indices):
        raise RuntimeError(f"Duplicate shard indices under {prefix}: {indices}")
    if expected_count and len(indices) != expected_count:
        raise RuntimeError(
            f"Expected {expected_count} shard handoffs under {prefix}, found {len(indices)}: {indices}"
        )
    destination.mkdir(parents=True, exist_ok=True)
    for index, key in shard_keys:
        download_directory(
            key,
            destination / f"shard_{index}",
            client=resolved_client,
            bucket=resolved_bucket,
        )
    print(f"Materialized private shard handoffs: count={len(shard_keys)}, indices={indices}")
    return len(shard_keys)


def _relative_key_parts(root: str, key: str) -> tuple[str, ...] | None:
    root_parts = PurePosixPath(validate_prefix(root).rstrip("/")).parts
    key_parts = PurePosixPath(key.strip().lstrip("/")).parts
    if len(key_parts) <= len(root_parts) or key_parts[: len(root_parts)] != root_parts:
        return None
    return tuple(key_parts[len(root_parts):])


def latest_run_with_shards(
    root: str,
    date: str,
    *,
    client: Any | None = None,
    bucket: str | None = None,
) -> str | None:
    root = validate_prefix(root).rstrip("/")
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    run_ids: set[str] = set()
    for key in list_keys(root, client=resolved_client, bucket=resolved_bucket):
        parts = _relative_key_parts(root, key)
        if len(parts or ()) != 3:
            continue
        run_id, key_date, filename = parts or ("", "", "")
        if key_date == date and RUN_ID_RE.match(run_id) and SHARD_KEY_RE.match(filename):
            run_ids.add(run_id)
    if not run_ids:
        return None
    return max(run_ids, key=int)


def latest_run_with_archive(
    root: str,
    date: str,
    archive_name: str,
    *,
    client: Any | None = None,
    bucket: str | None = None,
) -> str | None:
    root = validate_prefix(root).rstrip("/")
    validate_key(archive_name)
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    run_ids: set[str] = set()
    for key in list_keys(root, client=resolved_client, bucket=resolved_bucket):
        parts = _relative_key_parts(root, key)
        if len(parts or ()) != 3:
            continue
        run_id, key_date, filename = parts or ("", "", "")
        if key_date == date and filename == archive_name and RUN_ID_RE.match(run_id):
            run_ids.add(run_id)
    if not run_ids:
        return None
    return max(run_ids, key=int)


def download_latest_shards(
    root: str,
    date: str,
    destination: Path,
    expected_count: int = 0,
    *,
    optional: bool = False,
    client: Any | None = None,
    bucket: str | None = None,
) -> int:
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    run_id = latest_run_with_shards(root, date, client=resolved_client, bucket=resolved_bucket)
    if not run_id:
        message = f"No dated shard handoff found under {validate_prefix(root)} for {date}"
        if optional:
            print(f"Optional private handoff missing: {message}")
            return 0
        raise RuntimeError(message)
    print(f"Selected latest shard handoff: root={validate_prefix(root)}, date={date}, run_id={run_id}")
    return download_shards(
        f"{validate_prefix(root).rstrip('/')}/{run_id}/{date}",
        destination,
        max(0, expected_count),
        client=resolved_client,
        bucket=resolved_bucket,
    )


def download_latest_directory(
    root: str,
    date: str,
    archive_name: str,
    destination: Path,
    *,
    optional: bool = False,
    client: Any | None = None,
    bucket: str | None = None,
) -> int:
    archive_name = validate_key(archive_name)
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    run_id = latest_run_with_archive(root, date, archive_name, client=resolved_client, bucket=resolved_bucket)
    if not run_id:
        message = f"No dated archive handoff found under {validate_prefix(root)} for {date}/{archive_name}"
        if optional:
            print(f"Optional private handoff missing: {message}")
            return 0
        raise RuntimeError(message)
    print(f"Selected latest archive handoff: root={validate_prefix(root)}, date={date}, run_id={run_id}")
    return download_directory(
        f"{validate_prefix(root).rstrip('/')}/{run_id}/{date}/{archive_name}",
        destination,
        client=resolved_client,
        bucket=resolved_bucket,
    )


def delete_prefix(prefix: str, *, client: Any | None = None, bucket: str | None = None) -> int:
    resolved_client = client or build_r2_client()
    resolved_bucket = bucket or r2_bucket()
    keys = list_keys(prefix, client=resolved_client, bucket=resolved_bucket)
    for offset in range(0, len(keys), 1000):
        chunk = keys[offset : offset + 1000]
        resolved_client.delete_objects(
            Bucket=resolved_bucket,
            Delete={"Objects": [{"Key": key} for key in chunk], "Quiet": True},
        )
    print(f"Deleted private handoff prefix: prefix={validate_prefix(prefix)}, objects={len(keys)}")
    return len(keys)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    upload = subparsers.add_parser("upload-dir")
    upload.add_argument("--source", required=True)
    upload.add_argument("--key", required=True)

    download = subparsers.add_parser("download-dir")
    download.add_argument("--key", required=True)
    download.add_argument("--destination", required=True)

    shards = subparsers.add_parser("download-shards")
    shards.add_argument("--prefix", required=True)
    shards.add_argument("--destination", required=True)
    shards.add_argument("--expected-count", type=int, default=0)

    latest_shards = subparsers.add_parser("download-latest-shards")
    latest_shards.add_argument("--root", required=True)
    latest_shards.add_argument("--date", required=True)
    latest_shards.add_argument("--destination", required=True)
    latest_shards.add_argument("--expected-count", type=int, default=0)
    latest_shards.add_argument("--optional", action="store_true")

    latest_dir = subparsers.add_parser("download-latest-dir")
    latest_dir.add_argument("--root", required=True)
    latest_dir.add_argument("--date", required=True)
    latest_dir.add_argument("--archive-name", required=True)
    latest_dir.add_argument("--destination", required=True)
    latest_dir.add_argument("--optional", action="store_true")

    cleanup = subparsers.add_parser("delete-prefix")
    cleanup.add_argument("--prefix", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "upload-dir":
        upload_directory(Path(args.source), args.key)
    elif args.command == "download-dir":
        download_directory(args.key, Path(args.destination))
    elif args.command == "download-shards":
        download_shards(args.prefix, Path(args.destination), max(0, args.expected_count))
    elif args.command == "download-latest-shards":
        download_latest_shards(
            args.root,
            args.date,
            Path(args.destination),
            max(0, args.expected_count),
            optional=bool(args.optional),
        )
    elif args.command == "download-latest-dir":
        download_latest_directory(
            args.root,
            args.date,
            args.archive_name,
            Path(args.destination),
            optional=bool(args.optional),
        )
    elif args.command == "delete-prefix":
        delete_prefix(args.prefix)
    else:  # pragma: no cover
        raise RuntimeError(f"Unsupported command: {args.command}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
