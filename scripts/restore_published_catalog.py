#!/usr/bin/env python3
"""Inherit verified published report IDs before an additive catalog refresh.

The runtime manifest binds each source catalog to an immutable release. Public
availability alone does not establish private storage state: newly inherited
PDFs require an exact R2 object-size check before they can be marked synced.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any

from build_portal_suite_site import PUBLIC_ITEM_KEYS
from portal_suite_catalog import (
    build_r2_client, catalog_r2_delete_key, catalog_size_bytes,
    validated_catalog_r2_prefix,
)
from publish_static_slot import runtime_manifest_key, runtime_release_prefix, valid_runtime_manifest

RELEASE_RE = re.compile(r"[a-f0-9]{32}")
ID_RE = re.compile(r"[a-f0-9]{24}")
HASH_RE = re.compile(r"[a-f0-9]{64}")
DATE_RE = re.compile(r"(?:\d{6}|\d{8})")
MAX_CATALOG_BYTES = 64 * 1024 * 1024
MAX_MANIFEST_BYTES = 1024 * 1024
TOMBSTONES = ("pdf_archived", "pdf_object_deleted", "pdf_delete_pending")


class CatalogInheritanceError(ValueError):
    """A fixed, public-safe error category, optionally with opaque report IDs."""

    def __init__(self, category: str, ids: list[str] | None = None):
        super().__init__(category)
        self.category = category
        self.ids = sorted(set(ids or []))


def require(condition: Any, category: str, ids: list[str] | None = None) -> None:
    if not condition:
        raise CatalogInheritanceError(category, ids)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode()


def parse_json(raw: bytes, category: str) -> dict[str, Any]:
    try:
        value = json.loads(raw)
    except (UnicodeError, ValueError):
        raise CatalogInheritanceError(category) from None
    require(isinstance(value, dict), category)
    return value


def source_dates(row: dict[str, Any]) -> set[str]:
    """Keep every observed folder; the primary date remains a display choice."""
    report_id = row.get("id")
    ids = [report_id] if isinstance(report_id, str) and ID_RE.fullmatch(report_id) else []
    values = row.get("date_folders", [])
    primary = row.get("date_folder", "")
    require(isinstance(values, list) and isinstance(primary, str), "catalog_source_dates_invalid", ids)
    require(all(isinstance(value, str) and DATE_RE.fullmatch(value) for value in values)
            and (not primary or DATE_RE.fullmatch(primary)), "catalog_source_dates_invalid", ids)
    return set(values) | ({primary} if primary else set())


def catalog_rows(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    items = catalog.get("items")
    require(isinstance(items, list) and bool(items), "catalog_items_invalid")
    require(type(catalog.get("item_count")) is int and catalog["item_count"] == len(items),
            "catalog_count_mismatch")
    rows: dict[str, dict[str, Any]] = {}
    for row in items:
        require(isinstance(row, dict), "catalog_row_invalid")
        report_id = row.get("id")
        require(isinstance(report_id, str) and ID_RE.fullmatch(report_id), "catalog_id_invalid")
        require(report_id not in rows, "catalog_duplicate_ids", [report_id])
        require(type(row.get("available")) is bool, "catalog_availability_invalid", [report_id])
        require("pdf_archived" not in row or type(row["pdf_archived"]) is bool,
                "catalog_archive_state_invalid", [report_id])
        require(not (row["available"] and row.get("pdf_archived")),
                "catalog_archive_availability_conflict", [report_id])
        if row["available"]:
            require(type(row.get("size_bytes")) is int and row["size_bytes"] > 0,
                    "catalog_pdf_size_invalid", [report_id])
        source_dates(row)
        rows[report_id] = row
    return rows


def read_object(client: Any, bucket: str, key: str, limit: int) -> bytes:
    try:
        response = client.get_object(Bucket=bucket, Key=key)
        length = response.get("ContentLength")
        require(type(length) is int and 0 < length <= limit, "runtime_object_size_invalid")
        body = response["Body"]
        try:
            raw = body.read(limit + 1)
        finally:
            close = getattr(body, "close", None)
            if close:
                close()
        require(isinstance(raw, bytes) and len(raw) == length, "runtime_object_size_mismatch")
        return raw
    except CatalogInheritanceError:
        raise
    except Exception:
        raise CatalogInheritanceError("runtime_object_read_failed") from None


def load_release_catalog(client: Any, bucket: str, release: str) -> tuple[dict[str, Any], bytes]:
    require(isinstance(release, str) and RELEASE_RE.fullmatch(release), "release_id_invalid")
    manifest_raw = read_object(client, bucket, runtime_manifest_key(release), MAX_MANIFEST_BYTES)
    manifest = parse_json(manifest_raw, "runtime_manifest_invalid")
    try:
        valid = valid_runtime_manifest(manifest, release)
    except Exception:
        valid = None
    require(valid, "runtime_manifest_invalid")
    descriptor = valid["files"].get("catalog.json")
    require(isinstance(descriptor, dict), "runtime_catalog_descriptor_missing")
    require(type(descriptor.get("size")) is int and 0 < descriptor["size"] <= MAX_CATALOG_BYTES,
            "runtime_catalog_size_invalid")
    raw = read_object(client, bucket, runtime_release_prefix(release) + "catalog.json", MAX_CATALOG_BYTES)
    require(len(raw) == descriptor["size"] and sha256(raw) == descriptor["sha256"],
            "runtime_catalog_integrity_mismatch")
    catalog = parse_json(raw, "runtime_catalog_invalid")
    catalog_rows(catalog)
    return catalog, raw


def load_sources(client: Any, bucket: str, state: dict[str, Any], public_raw: bytes,
                 recovery_release: str = "") -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    require(state.get("schema_version") == 1 and state.get("slot") in {"a", "b"}
            and isinstance(state.get("tree_sha256"), str) and HASH_RE.fullmatch(state["tree_sha256"]),
            "previous_edge_state_invalid")
    active_release = state.get("release_id")
    active, active_raw = load_release_catalog(client, bucket, active_release)
    require(active_raw == public_raw, "active_public_catalog_mismatch")
    active_rows = catalog_rows(active)
    inherited: dict[str, dict[str, Any]] = {}
    sources = []
    if recovery_release and recovery_release != active_release:
        recovery, recovery_raw = load_release_catalog(client, bucket, recovery_release)
        inherited.update(catalog_rows(recovery))
        sources.append({"release_id": recovery_release, "catalog_sha256": sha256(recovery_raw),
                        "item_count": len(inherited), "role": "recovery"})
    # Historical folders are additive evidence. The active row still owns every
    # other public field, including its primary/display date and availability.
    for report_id, row in active_rows.items():
        dates = source_dates(row) | source_dates(inherited.get(report_id, {}))
        inherited[report_id] = {**row, "date_folders": sorted(dates, reverse=True)}
    sources.append({"release_id": active_release, "catalog_sha256": sha256(active_raw),
                    "item_count": len(active_rows), "role": "active"})
    return inherited, sources


def head_pdf(client: Any, bucket: str, key: str, size: int, report_id: str) -> None:
    try:
        result = client.head_object(Bucket=bucket, Key=key)
    except Exception:
        raise CatalogInheritanceError("inherited_pdf_head_failed", [report_id]) from None
    require(isinstance(result, dict) and type(result.get("ContentLength")) is int
            and result["ContentLength"] == size and size > 0,
            "inherited_pdf_size_mismatch", [report_id])


def inherit_catalog(seed: dict[str, Any], inherited: dict[str, dict[str, Any]],
                    client: Any, bucket: str, prefix: str) -> tuple[dict[str, Any], dict[str, int]]:
    prefix = validated_catalog_r2_prefix(prefix)
    seed_rows = catalog_rows(seed)
    rows = {report_id: dict(row) for report_id, row in seed_rows.items()}
    heads = 0
    for report_id, public in sorted(inherited.items()):
        native = seed_rows.get(report_id, {})
        # Only public metadata may cross this boundary. Persisted object keys,
        # cleanup checkpoints, source hashes and private storage state stay native.
        metadata = {key: public[key] for key in PUBLIC_ITEM_KEYS if key in public}
        row = {**native, **metadata}
        row["date_folders"] = sorted(source_dates(native) | source_dates(public), reverse=True)
        private_tombstone = any(native.get(key) is True for key in TOMBSTONES)
        require(not (public["available"] and private_tombstone),
                "published_availability_conflicts_with_native_tombstone", [report_id])
        for key in TOMBSTONES:
            if native.get(key) is True:
                row[key] = True
        if public["available"]:
            try:
                key = catalog_r2_delete_key(row, prefix)
            except Exception:
                raise CatalogInheritanceError("inherited_pdf_key_invalid", [report_id]) from None
            already_verified = (native.get("r2_synced") is True and native.get("r2_key") == key
                                and native.get("size_bytes") == public["size_bytes"])
            if not already_verified:
                head_pdf(client, bucket, key, public["size_bytes"], report_id)
                heads += 1
            row["r2_key"] = key
            row["r2_synced"] = True
        else:
            # A public text-only row must never be promoted by an R2 HEAD, or by
            # a stale native synced flag. Existing cleanup markers remain intact.
            row["r2_synced"] = False
        row["present_in_latest_scan"] = False
        rows[report_id] = row
    result = {**seed, "items": sorted(rows.values(), key=lambda row: row["id"]), "item_count": len(rows)}
    result["total_size_bytes"] = catalog_size_bytes(result)
    if isinstance(result.get("storage"), dict):
        result["storage"] = {**result["storage"], "total_size_bytes": result["total_size_bytes"]}
    return result, {"inherited_count": len(inherited), "added_count": len(rows) - len(seed_rows),
                    "pdf_heads_verified": heads, "item_count": len(rows)}


def inheritance_manifest(inherited: dict[str, dict[str, Any]], sources: list[dict[str, Any]]) -> dict[str, Any]:
    required = [{"id": report_id, "available": row["available"],
                 "pdf_archived": row.get("pdf_archived") is True,
                 "date_folders": sorted(source_dates(row))}
                for report_id, row in sorted(inherited.items())]
    return {"schema_version": 1, "sources": sources, "required_count": len(required),
            "required_sha256": sha256(encoded(required)), "required": required}


def validate_inheritance(catalog: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    rows = catalog_rows(catalog)
    required = manifest.get("required")
    require(manifest.get("schema_version") == 1 and isinstance(required, list) and bool(required)
            and manifest.get("required_count") == len(required)
            and manifest.get("required_sha256") == sha256(encoded(required)), "inheritance_manifest_invalid")
    seen: set[str] = set()
    missing, unavailable, unarchived, lost_dates = [], [], [], []
    for item in required:
        require(isinstance(item, dict) and isinstance(item.get("id"), str)
                and ID_RE.fullmatch(item["id"]) and item["id"] not in seen
                and type(item.get("available")) is bool and type(item.get("pdf_archived")) is bool
                and isinstance(item.get("date_folders"), list)
                and item["date_folders"] == sorted(source_dates(item)),
                "inheritance_manifest_invalid")
        report_id = item["id"]
        seen.add(report_id)
        candidate = rows.get(report_id)
        if candidate is None:
            missing.append(report_id)
        elif item["available"] and candidate["available"] is not True:
            unavailable.append(report_id)
        elif item["pdf_archived"] and candidate.get("pdf_archived") is not True:
            unarchived.append(report_id)
        if candidate is not None and not source_dates(item) <= source_dates(candidate):
            lost_dates.append(report_id)
    require(not missing, "published_report_ids_missing", missing)
    require(not unavailable, "published_pdf_availability_regressed", unavailable)
    require(not unarchived, "published_archive_state_regressed", unarchived)
    require(not lost_dates, "published_source_dates_missing", lost_dates)
    return {"complete": True, "required_count": len(required), "item_count": len(rows),
            "required_sha256": manifest["required_sha256"]}


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    restore = commands.add_parser("restore")
    restore.add_argument("--catalog-path", required=True, type=Path)
    restore.add_argument("--previous-edge-state", required=True, type=Path)
    restore.add_argument("--previous-public-catalog", required=True, type=Path)
    restore.add_argument("--output-manifest", required=True, type=Path)
    restore.add_argument("--recovery-release", default="")
    restore.add_argument("--r2-prefix", default="reports")
    validate = commands.add_parser("validate")
    validate.add_argument("--catalog-path", required=True, type=Path)
    validate.add_argument("--manifest", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        catalog = parse_json(args.catalog_path.read_bytes(), "local_catalog_invalid")
        if args.command == "validate":
            manifest = parse_json(args.manifest.read_bytes(), "inheritance_manifest_invalid")
            result = validate_inheritance(catalog, manifest)
        else:
            # Reject local malformed inputs before issuing any object requests.
            catalog_rows(catalog)
            require(not args.recovery_release or RELEASE_RE.fullmatch(args.recovery_release), "release_id_invalid")
            prefix = validated_catalog_r2_prefix(args.r2_prefix)
            state = parse_json(args.previous_edge_state.read_bytes(), "previous_edge_state_invalid")
            public_raw = args.previous_public_catalog.read_bytes()
            bucket = os.environ.get("R2_BUCKET", "")
            require(bool(bucket), "r2_bucket_missing")
            client = build_r2_client()
            inherited, sources = load_sources(client, bucket, state, public_raw, args.recovery_release)
            restored, counts = inherit_catalog(catalog, inherited, client, bucket, prefix)
            manifest = inheritance_manifest(inherited, sources)
            validate_inheritance(restored, manifest)
            # No destination is written before all remote integrity/PDF checks pass.
            atomic_json(args.output_manifest, manifest)
            atomic_json(args.catalog_path, restored)
            result = {"complete": True, **counts, "required_sha256": manifest["required_sha256"]}
    except CatalogInheritanceError as error:
        result = {"complete": False, "error_category": error.category,
                  "affected_count": len(error.ids), "affected_ids": error.ids}
    except Exception:
        result = {"complete": False, "error_category": "catalog_inheritance_failed"}
    print(json.dumps(result, sort_keys=True))
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
