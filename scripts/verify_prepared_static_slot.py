#!/usr/bin/env python3
"""Recheck an already uploaded static candidate immediately before cutover.

This performs no writes. Recovery preparation verifies the entire candidate;
this final guard rechecks its committed identity and key served objects after
the approval wait, while holding the shared production-release concurrency lock.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import PurePosixPath
import sys
from typing import Any

from publish_static_slot import (
    DEFAULT_RUNTIME_PATHS,
    RUNTIME_SCHEMA_VERSION,
    SHA256_PATTERN,
    build_r2_client,
    incomplete_key,
    manifest_key,
    read_json_object,
    remote_object_matches_descriptor,
    require_env,
    runtime_manifest_key,
    runtime_object_matches,
    runtime_release_prefix,
    slot_prefix,
    upload_error_code,
    valid_manifest,
    valid_runtime_manifest,
    validate_release,
    validate_slot,
)


REQUIRED_STATIC_PATHS = (
    "index.html",
    "robots.txt",
    "feed.xml",
    "data/catalog.json",
    "data/catalog_preview.json",
    "data/release-semantics.json",
    "assets/styles.css",
    "assets/app.js",
    "sitemap.xml",
    "sitemap-pages.xml",
    "sitemap-baidu.xml",
    "sitemap-sogou.xml",
)
REQUIRED_LOCALE_PATHS = (
    "data/i18n/manifest.json",
    "assets/locale.css",
    "assets/locale-runtime.js",
    *(f"sitemap-{locale}.xml" for locale in ("ko", "ja", "ar")),
    *(f"{locale}/index.html" for locale in ("ko", "ja", "ar")),
)


def static_tree_sha256(files: dict[str, dict[str, Any]]) -> str:
    """Match build_inventory's Path ordering, including directory/file siblings."""
    digest = hashlib.sha256()
    for relative in sorted(files, key=PurePosixPath):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(json.dumps(files[relative], sort_keys=True, separators=(",", ":")).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def require_complete_slot(client: Any, bucket: str, slot: str) -> None:
    # An existing malformed/empty marker also means incomplete; parsing it as a
    # JSON object would incorrectly treat [] or null as an absent marker.
    try:
        client.head_object(Bucket=bucket, Key=incomplete_key(slot))
    except Exception as error:
        if upload_error_code(error) in {"404", "nosuchkey", "notfound"}:
            return
        raise
    raise RuntimeError("Prepared static slot has an incomplete publication marker")


def read_prepared_manifest(
    client: Any, bucket: str, slot: str, release: str, tree: str,
) -> dict[str, Any]:
    try:
        manifest = valid_manifest(read_json_object(client, bucket, manifest_key(slot)), slot)
    except (TypeError, ValueError) as error:
        raise RuntimeError("Prepared static manifest is invalid") from error
    if manifest is None or manifest["release_id"] != release or manifest["tree_sha256"] != tree:
        raise RuntimeError("Prepared static manifest does not match the requested candidate")
    files = manifest["files"]
    if not files or static_tree_sha256(files) != tree:
        raise RuntimeError("Prepared static manifest file tree does not match its committed digest")
    if manifest.get("total_bytes") != sum(int(row["size"]) for row in files.values()):
        raise RuntimeError("Prepared static manifest total bytes do not match its file inventory")
    return manifest


def verify_object_body(
    client: Any, bucket: str, key: str, descriptor: dict[str, Any],
) -> None:
    if not remote_object_matches_descriptor(client, bucket, key, descriptor):
        raise RuntimeError(f"Prepared object metadata differs from its manifest: {key}")
    body = client.get_object(Bucket=bucket, Key=key)["Body"]
    digest = hashlib.sha256()
    size = 0
    try:
        if not hasattr(body, "read"):
            chunks = (body.encode("utf-8") if isinstance(body, str) else bytes(body),)
        else:
            chunks = iter(lambda: body.read(1024 * 1024), b"")
        for chunk in chunks:
            size += len(chunk)
            if size > int(descriptor["size"]):
                raise RuntimeError(f"Prepared object is larger than its manifest: {key}")
            digest.update(chunk)
    finally:
        if hasattr(body, "close"):
            body.close()
    if size != int(descriptor["size"]) or digest.hexdigest() != descriptor["sha256"]:
        raise RuntimeError(f"Prepared object content differs from its manifest: {key}")


def verify_prepared_static_slot(
    client: Any, bucket: str, *, slot: str, release: str, tree: str,
) -> dict[str, Any]:
    slot = validate_slot(slot)
    release = validate_release(release)
    if not SHA256_PATTERN.fullmatch(tree):
        raise ValueError("Static tree must contain exactly 64 lowercase hex characters")
    require_complete_slot(client, bucket, slot)
    manifest = read_prepared_manifest(client, bucket, slot, release, tree)
    files = manifest["files"]
    prefix = slot_prefix(slot)
    required_paths = REQUIRED_STATIC_PATHS + (
        REQUIRED_LOCALE_PATHS if "data/i18n/manifest.json" in files else ()
    )
    for relative in required_paths:
        if relative not in files or int(files[relative]["size"]) <= 0:
            raise RuntimeError(f"Prepared static manifest lacks a required object: {relative}")
        verify_object_body(client, bucket, prefix + relative, files[relative])

    runtime = valid_runtime_manifest(
        read_json_object(client, bucket, runtime_manifest_key(release)), release,
    )
    if runtime is None:
        raise RuntimeError("Prepared immutable runtime manifest is invalid")
    binding = {
        "schema_version": RUNTIME_SCHEMA_VERSION,
        "release_id": release,
        "prefix": runtime_release_prefix(release),
        "tree_sha256": runtime["tree_sha256"],
    }
    if manifest.get("runtime_data") != binding:
        raise RuntimeError("Prepared static and immutable runtime manifest identities differ")
    expected_runtime = {PurePosixPath(relative).name for relative in DEFAULT_RUNTIME_PATHS}
    if set(runtime["files"]) != expected_runtime:
        raise RuntimeError("Prepared immutable runtime manifest has an unexpected file inventory")
    for relative in DEFAULT_RUNTIME_PATHS:
        filename = PurePosixPath(relative).name
        descriptor = runtime["files"][filename]
        static_descriptor = files.get(relative) or {}
        if any(descriptor[field] != static_descriptor.get(field) for field in ("sha256", "size")):
            raise RuntimeError(f"Prepared runtime content does not match the static candidate: {filename}")
        key = runtime["prefix"] + filename
        if not runtime_object_matches(client.head_object(Bucket=bucket, Key=key), descriptor, release):
            raise RuntimeError(f"Prepared immutable runtime metadata differs: {filename}")
        verify_object_body(client, bucket, key, descriptor)

    # A publisher may have started or committed while the object checks ran.
    require_complete_slot(client, bucket, slot)
    if read_prepared_manifest(client, bucket, slot, release, tree) != manifest:
        raise RuntimeError("Prepared static manifest changed during verification")
    if read_json_object(client, bucket, runtime_manifest_key(release)) != runtime:
        raise RuntimeError("Prepared immutable runtime manifest changed during verification")
    require_complete_slot(client, bucket, slot)
    return {
        "verified": True,
        "slot": slot,
        "release_id": release,
        "tree_sha256": tree,
        "static_objects_verified": len(required_paths),
        "runtime_objects_verified": len(expected_runtime),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slot", required=True)
    parser.add_argument("--release", required=True)
    parser.add_argument("--tree", required=True)
    args = parser.parse_args()
    try:
        client, _transfer = build_r2_client()
        result = verify_prepared_static_slot(
            client, require_env("R2_BUCKET"), slot=args.slot, release=args.release, tree=args.tree,
        )
        print(json.dumps(result, sort_keys=True))
        return 0
    except Exception as error:
        print(f"Prepared static slot verification failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
