#!/usr/bin/env python3
"""Persist chart-search checkpoints, indexes, and immutable images in private R2."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any


DEFAULT_PREFIX = "_chart-search/v1"
DEFAULT_STORAGE_BUDGET_BYTES = 100 * 1024 * 1024 * 1024
PUBLIC_ANALYSIS_VERSION = "chart-search-v2"
ASSET_RE = re.compile(r"^[0-9a-f]{64}\.jpg$")
IMAGE_ID_RE = re.compile(r"^[0-9a-f]{64}$")
REPORT_REF_ALIAS_RE = re.compile(r"^[0-9a-f]{24}$")
MAX_REPORT_REF_ALIASES = 32


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
    temporary.write_bytes(json_document_bytes(value))
    os.replace(temporary, path)


def json_document_bytes(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def is_not_found(error: Exception) -> bool:
    response = getattr(error, "response", {})
    code = str(((response or {}).get("Error") or {}).get("Code") or "")
    return code in {"404", "NoSuchKey", "NotFound"}


def read_json_object(client: Any, bucket: str, key: str, kind: str) -> tuple[dict[str, Any], bool]:
    try:
        response = client.get_object(Bucket=bucket, Key=key)
    except Exception as exc:  # botocore is an optional runtime dependency
        if is_not_found(exc):
            return default_document(kind), False
        raise RuntimeError(f"Unable to download chart-search {kind}") from exc
    try:
        value = json.loads(response["Body"].read().decode("utf-8"))
    except (KeyError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Stored chart-search {kind} is invalid") from exc
    if not isinstance(value, dict) or int(value.get("schema_version") or 0) != 1:
        raise RuntimeError(f"Stored chart-search {kind} has an unsupported schema")
    return value, True


def download_json(client: Any, bucket: str, key: str, destination: Path, kind: str) -> bool:
    value, found = read_json_object(client, bucket, key, kind)
    atomic_write(destination, value)
    return found


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


def put_index_snapshot(client: Any, bucket: str, prefix: str, path: Path) -> str:
    body = path.read_bytes()
    digest = hashlib.sha256(body).hexdigest()
    key = index_snapshot_key(prefix, body)
    client.put_object(
        Bucket=bucket,
        Key=key,
        Body=body,
        ContentType="application/json; charset=utf-8",
        CacheControl="private, max-age=31536000, immutable",
        Metadata={"sha256": digest},
    )
    return key


def index_snapshot_key(prefix: str, body: bytes) -> str:
    return f"{prefix}/index-snapshots/sha256-{hashlib.sha256(body).hexdigest()}.json"


def asset_exists(client: Any, bucket: str, key: str) -> bool:
    try:
        client.head_object(Bucket=bucket, Key=key)
        return True
    except Exception as exc:
        if is_not_found(exc):
            return False
        raise RuntimeError("Unable to inspect chart-search image") from exc


def publish_assets(
    client: Any,
    bucket: str,
    prefix: str,
    asset_dir: Path,
    referenced_image_ids: set[str] | None = None,
) -> tuple[int, int]:
    if not asset_dir.exists():
        return 0, 0
    uploaded = 0
    reused = 0
    for asset in sorted(asset_dir.iterdir()):
        if not asset.is_file() or not ASSET_RE.fullmatch(asset.name):
            continue
        if referenced_image_ids is not None and asset.stem not in referenced_image_ids:
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


def index_item_count(index: dict[str, Any]) -> int:
    actual = sum(
        len([chart for chart in report.get("charts", []) if isinstance(chart, dict)])
        for report in index.get("reports", [])
        if isinstance(report, dict)
    )
    try:
        declared = max(0, int(index.get("item_count") or 0))
    except (TypeError, ValueError):
        declared = 0
    return max(actual, declared)


def oldest_index_source_date(index: dict[str, Any]) -> tuple[int, str]:
    dated: list[tuple[int, str]] = []
    undated_records = 0
    for report in index.get("reports", []):
        if not isinstance(report, dict):
            continue
        charts = [chart for chart in report.get("charts", []) if isinstance(chart, dict)]
        if not charts:
            continue
        value = str(report.get("date_folder") or "")
        rank = report_date_rank(value)
        if not rank:
            undated_records += len(charts)
            continue
        dated.append((rank, value))
    if undated_records:
        raise RuntimeError(
            f"Chart index contains {undated_records} record(s) without a valid source date"
        )
    return min(dated) if dated else (0, "")


def validate_publish_coverage(
    previous: dict[str, Any],
    candidate: dict[str, Any],
    *,
    allow_index_removal_migration: bool,
) -> dict[str, Any]:
    sanitized_previous = copy.deepcopy(previous)
    previous_schema_records_removed = filter_index_images(
        sanitized_previous,
        set(referenced_image_recency(sanitized_previous)),
    )
    previous_count = index_item_count(sanitized_previous)
    candidate_count = index_item_count(candidate)
    previous_oldest_rank, previous_oldest = oldest_index_source_date(sanitized_previous)
    candidate_oldest_rank, candidate_oldest = oldest_index_source_date(candidate)
    previous_image_counts = referenced_v2_image_counts(sanitized_previous)
    candidate_image_counts = referenced_v2_image_counts(candidate)
    previous_occurrences, previous_missing_identities, _previous_invalid_aliases = (
        report_image_occurrences(sanitized_previous, candidate_aliases=False)
    )
    candidate_occurrences, candidate_missing_identities, candidate_invalid_aliases = (
        report_image_occurrences(candidate, candidate_aliases=True)
    )
    if candidate_invalid_aliases:
        raise RuntimeError(
            f"candidate_report_ref_aliases_invalid={candidate_invalid_aliases}"
        )
    underrepresented_image_ids = {
        image_id
        for image_id, count in previous_image_counts.items()
        if candidate_image_counts[image_id] < count
    }
    missing_image_occurrences = sum(
        previous_image_counts[image_id] - candidate_image_counts[image_id]
        for image_id in underrepresented_image_ids
    )
    previous_association_count = sum(len(rows) for rows in previous_occurrences.values())
    candidate_association_count = sum(len(rows) for rows in candidate_occurrences.values())
    association_matches = 0
    dated_association_matches = 0
    for image_id, previous_rows in previous_occurrences.items():
        candidate_rows = candidate_occurrences.get(image_id, [])
        association_matches += maximum_occurrence_matches(
            previous_rows,
            candidate_rows,
            require_date_floor=False,
        )
        dated_association_matches += maximum_occurrence_matches(
            previous_rows,
            candidate_rows,
            require_date_floor=True,
        )
    missing_association_occurrences = previous_association_count - association_matches
    later_association_date_occurrences = association_matches - dated_association_matches
    violations: list[str] = []
    if previous_schema_records_removed:
        violations.append(f"previous_live_schema_records={previous_schema_records_removed}")
    if candidate_count < previous_count:
        violations.append(f"item_count {previous_count}->{candidate_count}")
    if previous_oldest_rank and (
        not candidate_oldest_rank or candidate_oldest_rank > previous_oldest_rank
    ):
        violations.append(
            f"oldest_source_date {previous_oldest or 'missing'}->{candidate_oldest or 'missing'}"
        )
    if underrepresented_image_ids:
        violations.append(
            f"previous_v2_image_ids_missing={len(underrepresented_image_ids)} "
            f"occurrences_missing={missing_image_occurrences}"
        )
    if previous_missing_identities:
        violations.append(f"previous_report_identity_missing={previous_missing_identities}")
    if candidate_missing_identities:
        violations.append(f"candidate_report_identity_missing={candidate_missing_identities}")
    if missing_association_occurrences:
        violations.append(
            f"previous_report_image_associations_missing={missing_association_occurrences}"
        )
    if later_association_date_occurrences:
        violations.append(
            "report_image_association_dates_moved_later="
            f"{later_association_date_occurrences}"
        )
    if violations and not allow_index_removal_migration:
        raise RuntimeError(
            "Chart index coverage regression; rerun only an intentional one-time migration "
            f"with --allow-index-removal-migration: {', '.join(violations)}"
        )
    return {
        "previous_item_count": previous_count,
        "candidate_item_count": candidate_count,
        "previous_oldest_source_date": previous_oldest or "none",
        "candidate_oldest_source_date": candidate_oldest or "none",
        "previous_v2_image_count": len(previous_image_counts),
        "candidate_v2_image_count": len(candidate_image_counts),
        "previous_report_image_association_count": previous_association_count,
        "candidate_report_image_association_count": candidate_association_count,
        "previous_live_schema_records": previous_schema_records_removed,
        "coverage_regression_allowed": bool(violations and allow_index_removal_migration),
    }


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


def referenced_v2_image_counts(index: dict[str, Any]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for report in index.get("reports", []):
        if not isinstance(report, dict):
            continue
        for chart in report.get("charts", []):
            image_id = str(chart.get("image_id") or "") if isinstance(chart, dict) else ""
            if (
                isinstance(chart, dict)
                and str(chart.get("analysis_version") or "") == PUBLIC_ANALYSIS_VERSION
                and IMAGE_ID_RE.fullmatch(image_id)
            ):
                counts[image_id] += 1
    return counts


def stable_report_identity(report: dict[str, Any]) -> str:
    report_id = str(report.get("report_id") or "").strip()
    if report_id:
        return f"report_id:{report_id}"
    report_ref = str(report.get("report_ref") or "").strip()
    return f"report_ref:{report_ref}" if report_ref else ""


def candidate_report_identities(report: dict[str, Any]) -> tuple[frozenset[str], bool]:
    identities: set[str] = set()
    report_id = str(report.get("report_id") or "").strip()
    report_ref = str(report.get("report_ref") or "").strip()
    if report_id:
        identities.add(f"report_id:{report_id}")
    if report_ref:
        identities.add(f"report_ref:{report_ref}")

    raw_aliases = report.get("report_ref_aliases")
    if raw_aliases is None:
        return frozenset(identities), False
    if not isinstance(raw_aliases, list) or len(raw_aliases) > MAX_REPORT_REF_ALIASES:
        return frozenset(identities), True
    invalid = False
    for raw_alias in raw_aliases:
        if not isinstance(raw_alias, str) or not REPORT_REF_ALIAS_RE.fullmatch(raw_alias):
            invalid = True
            continue
        identities.add(f"report_ref:{raw_alias}")
    return frozenset(identities), invalid


def report_image_occurrences(
    index: dict[str, Any],
    *,
    candidate_aliases: bool,
) -> tuple[dict[str, list[tuple[frozenset[str], int]]], int, int]:
    occurrences: dict[str, list[tuple[frozenset[str], int]]] = {}
    missing_identity_records = 0
    invalid_alias_reports = 0
    for report in index.get("reports", []):
        if not isinstance(report, dict):
            continue
        if candidate_aliases:
            identities, invalid_aliases = candidate_report_identities(report)
            invalid_alias_reports += int(invalid_aliases)
            primary_identity = stable_report_identity(report)
        else:
            primary_identity = stable_report_identity(report)
            identities = frozenset({primary_identity}) if primary_identity else frozenset()
        date_rank = report_date_rank(report.get("date_folder"))
        for chart in report.get("charts", []):
            image_id = str(chart.get("image_id") or "") if isinstance(chart, dict) else ""
            if (
                not isinstance(chart, dict)
                or str(chart.get("analysis_version") or "") != PUBLIC_ANALYSIS_VERSION
                or not IMAGE_ID_RE.fullmatch(image_id)
            ):
                continue
            if not primary_identity:
                missing_identity_records += 1
                continue
            occurrences.setdefault(image_id, []).append((identities, date_rank))
    for rows in occurrences.values():
        rows.sort(key=lambda row: (row[1], sorted(row[0])))
    return occurrences, missing_identity_records, invalid_alias_reports


def maximum_occurrence_matches(
    previous_rows: list[tuple[frozenset[str], int]],
    candidate_rows: list[tuple[frozenset[str], int]],
    *,
    require_date_floor: bool,
) -> int:
    edges: list[list[int]] = []
    for previous_identities, previous_date in previous_rows:
        matches = [
            offset
            for offset, (candidate_identities, candidate_date) in enumerate(candidate_rows)
            if previous_identities & candidate_identities
            and (not require_date_floor or candidate_date <= previous_date)
        ]
        edges.append(matches)

    candidate_matches: dict[int, int] = {}

    def augment(previous_offset: int, seen: set[int]) -> bool:
        for candidate_offset in edges[previous_offset]:
            if candidate_offset in seen:
                continue
            seen.add(candidate_offset)
            matched_previous = candidate_matches.get(candidate_offset)
            if matched_previous is None or augment(matched_previous, seen):
                candidate_matches[candidate_offset] = previous_offset
                return True
        return False

    matched = 0
    for previous_offset in sorted(range(len(previous_rows)), key=lambda offset: len(edges[offset])):
        matched += int(augment(previous_offset, set()))
    return matched


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
    return len(json_document_bytes(value))


def plan_storage_budget(
    client: Any,
    bucket: str,
    prefix: str,
    index: dict[str, Any],
    *,
    budget_bytes: int,
    asset_dir: Path | None = None,
    state_path: Path | None = None,
) -> dict[str, Any]:
    """Plan retention without mutating R2; callers commit live before deleting objects."""
    budget_bytes = int(budget_bytes)
    if budget_bytes <= 0:
        raise RuntimeError("Chart storage budget must be positive")

    base_index = copy.deepcopy(index)
    recency = referenced_image_recency(base_index)
    objects = list_prefix_objects(client, bucket, prefix)
    image_prefix = f"{prefix}/images/"
    index_key = f"{prefix}/index.json"
    state_key = f"{prefix}/state.json"
    object_keys = {str(row.get("Key") or "") for row in objects}
    images: dict[str, dict[str, Any]] = {}
    fixed_existing_bytes = 0
    existing_state_bytes = 0
    for row in objects:
        key = str(row.get("Key") or "")
        size = max(0, int(row.get("Size") or 0))
        name = key[len(image_prefix) :] if key.startswith(image_prefix) else ""
        if name and "/" not in name and ASSET_RE.fullmatch(name):
            images[name[:-4]] = {
                **row,
                "Key": key,
                "Size": size,
                "image_id": name[:-4],
                "remote": True,
            }
        elif key == state_key:
            existing_state_bytes = size
        elif key != index_key:
            # Includes every prior immutable index snapshot. None is a cleanup target.
            fixed_existing_bytes += size

    if asset_dir is not None and asset_dir.exists():
        for asset in sorted(asset_dir.iterdir()):
            if (
                not asset.is_file()
                or not ASSET_RE.fullmatch(asset.name)
                or asset.stem not in recency
            ):
                continue
            key = f"{image_prefix}{asset.name}"
            if key not in object_keys:
                images[asset.stem] = {
                    "Key": key,
                    "Size": max(0, int(asset.stat().st_size)),
                    "LastModified": None,
                    "image_id": asset.stem,
                    "remote": False,
                }

    state_bytes = (
        max(0, int(state_path.stat().st_size))
        if state_path is not None
        else existing_state_bytes
    )
    candidates = [row for image_id, row in images.items() if image_id in recency]
    candidates.sort(
        key=lambda row: (
            recency.get(str(row["image_id"]), 0),
            object_age_rank(row.get("LastModified")),
            str(row.get("Key") or ""),
        )
    )
    retained: set[str] = {str(row["image_id"]) for row in candidates}
    cursor = 0
    while True:
        planned_index = copy.deepcopy(base_index)
        removed_records = filter_index_images(planned_index, retained)
        index_body = json_document_bytes(planned_index)
        snapshot_key = index_snapshot_key(prefix, index_body)
        snapshot_bytes = 0 if snapshot_key in object_keys else len(index_body)
        fixed_bytes = fixed_existing_bytes + state_bytes + len(index_body) + snapshot_bytes
        retained_image_bytes = sum(
            int(row.get("Size") or 0)
            for row in candidates
            if str(row["image_id"]) in retained
        )
        if fixed_bytes + retained_image_bytes <= budget_bytes:
            break
        if cursor >= len(candidates):
            raise RuntimeError("Chart metadata exceeds the configured storage budget")
        retained.discard(str(candidates[cursor]["image_id"]))
        cursor += 1

    evicted_keys = [
        str(row["Key"])
        for row in images.values()
        if bool(row.get("remote")) and str(row["image_id"]) not in retained
    ]
    index.clear()
    index.update(planned_index)
    return {
        "budget_bytes": budget_bytes,
        "fixed_bytes": fixed_bytes,
        "image_bytes": retained_image_bytes,
        "images_retained": len(retained),
        "images_evicted": len(evicted_keys),
        "records_removed": removed_records,
        "evicted_keys": evicted_keys,
        "snapshot_key": snapshot_key,
    }


def enforce_storage_budget(
    client: Any,
    bucket: str,
    prefix: str,
    index: dict[str, Any],
    *,
    budget_bytes: int,
) -> dict[str, Any]:
    """Compatibility wrapper for explicit cleanup callers outside the publish transaction."""
    plan = plan_storage_budget(
        client,
        bucket,
        prefix,
        index,
        budget_bytes=budget_bytes,
    )
    delete_object_keys(client, bucket, list(plan["evicted_keys"]))
    return plan


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
    index = copy.deepcopy(load_publish_document(index_path, "index"))
    prefix = validate_prefix(args.prefix)
    cleanup_enabled = bool(getattr(args, "cleanup", False))
    allow_migration = bool(getattr(args, "allow_index_removal_migration", False))
    schema_image_ids = set(referenced_image_recency(index))
    schema_records_removed = filter_index_images(index, schema_image_ids)
    if schema_records_removed and not allow_migration:
        raise RuntimeError(
            "Chart schema hygiene would remove "
            f"{schema_records_removed} record(s); rerun only an intentional one-time migration "
            "with --allow-index-removal-migration"
        )

    previous_index_path = str(getattr(args, "previous_index", "") or "").strip()
    previous_index = (
        load_publish_document(Path(previous_index_path), "previous index")
        if previous_index_path
        else None
    )
    if previous_index is not None:
        coverage = validate_publish_coverage(
            previous_index,
            index,
            allow_index_removal_migration=allow_migration,
        )

    client, bucket = client_and_bucket()
    if previous_index is None:
        previous_index, _found = read_json_object(
            client,
            bucket,
            f"{prefix}/index.json",
            "previous index",
        )
        coverage = validate_publish_coverage(
            previous_index,
            index,
            allow_index_removal_migration=allow_migration,
        )

    asset_dir = Path(args.asset_dir)
    retention = {
        "images_evicted": 0,
        "records_removed": schema_records_removed,
    }
    evicted_keys: list[str] = []
    storage_summary = "stored_bytes=not_checked budget_bytes=not_enforced"
    if cleanup_enabled:
        storage_budget_bytes = int(getattr(args, "max_storage_bytes", DEFAULT_STORAGE_BUDGET_BYTES))
        cleanup_retention = plan_storage_budget(
            client,
            bucket,
            prefix,
            index,
            budget_bytes=storage_budget_bytes,
            asset_dir=asset_dir,
            state_path=state_path,
        )
        # Storage planning is read-only. Guard the final, post-retention candidate
        # before the first R2 upload, put, or delete.
        coverage = validate_publish_coverage(
            previous_index,
            index,
            allow_index_removal_migration=allow_migration,
        )
        evicted_keys = list(cleanup_retention["evicted_keys"])
        retention = {
            **cleanup_retention,
            "records_removed": schema_records_removed + cleanup_retention["records_removed"],
        }

    # Materialize the exact guarded candidate before any remote mutation. The
    # snapshot and live object will both use these same bytes.
    atomic_write(index_path, index)
    referenced_image_ids = set(referenced_image_recency(index))
    uploaded, reused = publish_assets(
        client,
        bucket,
        prefix,
        asset_dir,
        referenced_image_ids,
    )
    put_json(client, bucket, f"{prefix}/state.json", state_path, private=True)
    snapshot_key = put_index_snapshot(client, bucket, prefix, index_path)
    # Commit the live index only after its immutable versioned snapshot and all
    # referenced immutable images are available.
    put_json(client, bucket, f"{prefix}/index.json", index_path, private=False)
    if cleanup_enabled:
        # The live index no longer references planned evictions. Old immutable
        # snapshots are never present in this image-only deletion list.
        delete_object_keys(client, bucket, evicted_keys)
        total_bytes = prefix_size_bytes(client, bucket, prefix)
        if total_bytes > storage_budget_bytes:
            raise RuntimeError("Chart storage budget verification failed")
        storage_summary = f"stored_bytes={total_bytes} budget_bytes={storage_budget_bytes}"
    print(
        "chart_search_publish "
        f"reports={int(index.get('report_count') or 0)} charts={int(index.get('item_count') or 0)} "
        f"images_uploaded={uploaded} images_reused={reused} "
        f"images_evicted={retention['images_evicted']} records_removed={retention['records_removed']} "
        f"cleanup_enabled={str(cleanup_enabled).lower()} "
        f"migration_enabled={str(allow_migration).lower()} "
        f"previous_charts={coverage['previous_item_count']} "
        f"oldest_source_date={coverage['candidate_oldest_source_date']} "
        f"snapshot_key={snapshot_key} {storage_summary}"
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
    publish.add_argument(
        "--previous-index",
        default="",
        help="Optional downloaded live-index baseline. Without it, the publisher reads the live R2 index.",
    )
    publish.add_argument("--asset-dir", required=True)
    publish.add_argument(
        "--allow-index-removal-migration",
        action="store_true",
        help="One-run opt-in for intentional schema removals or index coverage regression.",
    )
    publish.add_argument(
        "--cleanup",
        action="store_true",
        help="Opt in to deleting unreferenced images and enforcing the storage budget.",
    )
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
