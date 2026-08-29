#!/usr/bin/env python3
"""Plan or restore Dropbox PDFs deleted by the catalog cleanup workflow.

The tool is deliberately fail closed:

* it only considers catalog rows explicitly marked ``pdf_object_deleted``;
* it resolves deleted Dropbox paths back to catalog IDs through a restorable
  revision's Dropbox ``content_hash``;
* both the catalog target count and the fully resolved plan must equal the
  operator-supplied expected count before the first restore request; and
* restore mode is opt-in. The default is a read-only dry run.

Logs contain counts and public catalog report IDs only. Dropbox access tokens,
revision IDs, filenames, and complete Dropbox paths are never printed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

from build_bank_report_catalog import (
    DROPBOX_API,
    dropbox_post_with_retry,
)

DEFAULT_CATALOG_PATH = "portal_suite/data/catalog.json"
DEFAULT_DROPBOX_ROOT = "/zip_backup"
DATE_FOLDER_RE = re.compile(r"^[0-9]{6,8}$")
REPORT_ID_RE = re.compile(r"^[0-9a-f]{24}$")
REVISION_PAGE_SIZE = 100
MAX_REVISION_PAGES = 100
REQUIRED_RESTORE_SCOPE = "files.content.write"
REQUIRED_READ_SCOPE = "files.metadata.read"


class RestoreContractError(RuntimeError):
    """A safe-to-log precondition or Dropbox contract failure."""


DropboxApiCall = Callable[[str, str, dict[str, Any]], dict[str, Any]]


@dataclass(frozen=True)
class RestoreCandidate:
    report_id: str
    source_hash: str
    path: str
    rev: str


@dataclass(frozen=True)
class RestoreResult:
    target_count: int
    deleted_path_count: int
    matched_count: int
    already_restored_count: int
    pending_restore_count: int
    restored_count: int
    report_ids: tuple[str, ...]


def write_github_output(key: str, value: str | int) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as output:
        output.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


def source_hash_for_content_hash(content_hash: str) -> str:
    clean_hash = str(content_hash or "").strip().lower()
    if not clean_hash:
        raise RestoreContractError("Dropbox revision is missing content_hash")
    return hashlib.sha256(f"dropbox-content:{clean_hash}".encode("utf-8")).hexdigest()


def report_id_for_content_hash(content_hash: str) -> str:
    return source_hash_for_content_hash(content_hash)[:24]


def load_catalog(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RestoreContractError(
            f"Unable to read catalog ({type(exc).__name__}); details suppressed"
        ) from exc
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise RestoreContractError("Catalog must contain an items array")
    return data


def deleted_catalog_targets(catalog: dict[str, Any], date_folder: str) -> dict[str, str]:
    if not DATE_FOLDER_RE.fullmatch(date_folder):
        raise RestoreContractError("date_folder must contain 6 or 8 digits")

    targets: dict[str, str] = {}
    for item in catalog.get("items", []):
        if not isinstance(item, dict):
            continue
        if str(item.get("date_folder") or "") != date_folder:
            continue
        if item.get("pdf_object_deleted") is not True:
            continue
        report_id = str(item.get("id") or "").strip().lower()
        if not REPORT_ID_RE.fullmatch(report_id):
            raise RestoreContractError("Target catalog row has an invalid report ID")
        source_hash = str(item.get("source_hash") or "").strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", source_hash):
            raise RestoreContractError(f"Target catalog row is missing source_hash: {report_id}")
        if not source_hash.startswith(report_id):
            raise RestoreContractError(f"Target catalog ID/source_hash mismatch: {report_id}")
        if report_id in targets:
            raise RestoreContractError(f"Duplicate target report ID: {report_id}")
        targets[report_id] = source_hash
    return targets


def deleted_catalog_ids(catalog: dict[str, Any], date_folder: str) -> frozenset[str]:
    return frozenset(deleted_catalog_targets(catalog, date_folder))


def validate_expected_count(expected_count: int, actual_count: int, label: str) -> None:
    if expected_count <= 0:
        raise RestoreContractError("expected_count must be greater than zero")
    if actual_count != expected_count:
        raise RestoreContractError(
            f"expected_count mismatch: expected={expected_count} {label}={actual_count}"
        )


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RestoreContractError(f"Missing required environment variable: {name}")
    return value


def parse_token_response(data: Any) -> tuple[str, frozenset[str]]:
    if not isinstance(data, dict):
        raise RestoreContractError("Dropbox token refresh returned a non-object response")
    token = str(data.get("access_token") or "").strip()
    if not token:
        raise RestoreContractError("Dropbox token refresh did not return an access token")
    raw_scope = data.get("scope")
    if isinstance(raw_scope, str):
        scopes = frozenset(value for value in raw_scope.split() if value)
    elif isinstance(raw_scope, list):
        scopes = frozenset(str(value).strip() for value in raw_scope if str(value).strip())
    else:
        scopes = frozenset()
    return token, scopes


def dropbox_access_token_with_scopes() -> tuple[str, frozenset[str]]:
    try:
        response = dropbox_post_with_retry(
            "Dropbox token refresh",
            "https://api.dropboxapi.com/oauth2/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": require_env("DROPBOX_REFRESH_TOKEN"),
            },
            auth=(require_env("DROPBOX_APP_KEY"), require_env("DROPBOX_APP_SECRET")),
            timeout=60,
        )
        try:
            data = response.json()
        finally:
            response.close()
    except RestoreContractError:
        raise
    except Exception as exc:
        raise RestoreContractError(
            f"Dropbox token refresh failed ({type(exc).__name__}); private details suppressed"
        ) from exc
    return parse_token_response(data)


def validate_restore_scope(scopes: frozenset[str], apply_restore: bool) -> None:
    has_read_scope = REQUIRED_READ_SCOPE in scopes
    has_scope = REQUIRED_RESTORE_SCOPE in scopes
    print(f"scope_files_metadata_read={str(has_read_scope).lower()}")
    print(f"scope_files_content_write={str(has_scope).lower()}")
    if not has_read_scope:
        print(f"missing_scope={REQUIRED_READ_SCOPE}")
        raise RestoreContractError(f"missing_scope={REQUIRED_READ_SCOPE}")
    if apply_restore and not has_scope:
        print(f"missing_scope={REQUIRED_RESTORE_SCOPE}")
        raise RestoreContractError(f"missing_scope={REQUIRED_RESTORE_SCOPE}")


def api_post(token: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Call one Dropbox RPC endpoint without exposing its private payload."""

    try:
        response = dropbox_post_with_retry(
            f"Dropbox API {endpoint}",
            f"{DROPBOX_API}{endpoint}",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            json=payload,
            timeout=90,
        )
        try:
            data = response.json()
        finally:
            response.close()
    except Exception as exc:
        raise RestoreContractError(
            f"Dropbox API {endpoint} failed ({type(exc).__name__}); private details suppressed"
        ) from exc

    if not isinstance(data, dict):
        raise RestoreContractError(f"Dropbox API {endpoint} returned a non-object response")
    return data


def list_deleted_entries(
    token: str,
    root: str,
    api_call: DropboxApiCall = api_post,
) -> list[dict[str, Any]]:
    data = api_call(
        token,
        "/files/list_folder",
        {
            "path": root,
            "recursive": True,
            "include_deleted": True,
            "include_restorable_info": True,
        },
    )
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise RestoreContractError("Dropbox list_folder response is missing entries")
    result = [entry for entry in entries if isinstance(entry, dict)]
    seen_cursors: set[str] = set()

    while data.get("has_more") is True:
        cursor = str(data.get("cursor") or "")
        if not cursor or cursor in seen_cursors:
            raise RestoreContractError("Dropbox list_folder returned an invalid pagination cursor")
        seen_cursors.add(cursor)
        data = api_call(token, "/files/list_folder/continue", {"cursor": cursor})
        entries = data.get("entries")
        if not isinstance(entries, list):
            raise RestoreContractError("Dropbox list_folder continuation is missing entries")
        result.extend(entry for entry in entries if isinstance(entry, dict))

    return result


def deleted_pdf_paths(
    entries: Iterable[dict[str, Any]],
    root: str,
    date_folder: str,
) -> tuple[str, ...]:
    clean_root = "/" + str(root or "").strip().strip("/")
    folder_prefix = f"{clean_root}/{date_folder}/".lower()
    paths: set[str] = set()

    for entry in entries:
        if entry.get(".tag") != "deleted" or entry.get("is_restorable") is not True:
            continue
        # Restore the display path when Dropbox supplies it; path_lower is only
        # a fallback for entries without display metadata.
        path = str(entry.get("path_display") or entry.get("path_lower") or "").strip()
        path_lower = path.lower()
        if not path_lower.startswith(folder_prefix) or not path_lower.endswith(".pdf"):
            continue
        paths.add(path)

    return tuple(sorted(paths, key=str.lower))


def target_folder_tombstone_count(
    entries: Iterable[dict[str, Any]],
    root: str,
    date_folder: str,
) -> int:
    clean_root = "/" + str(root or "").strip().strip("/")
    target_path = f"{clean_root}/{date_folder}".lower()
    return sum(
        1
        for entry in entries
        if entry.get(".tag") == "deleted"
        and str(entry.get("path_lower") or entry.get("path_display") or "").strip().lower()
        == target_path
    )


def active_restored_ids(
    entries: Iterable[dict[str, Any]],
    root: str,
    date_folder: str,
    targets: Mapping[str, str],
) -> frozenset[str]:
    clean_root = "/" + str(root or "").strip().strip("/")
    folder_prefix = f"{clean_root}/{date_folder}/".lower()
    matched_paths: dict[str, str] = {}

    for entry in entries:
        if entry.get(".tag") != "file":
            continue
        path = str(entry.get("path_display") or entry.get("path_lower") or "").strip()
        path_lower = path.lower()
        if not path_lower.startswith(folder_prefix) or not path_lower.endswith(".pdf"):
            continue
        content_hash = str(entry.get("content_hash") or "").strip()
        if not content_hash:
            continue
        source_hash = source_hash_for_content_hash(content_hash)
        report_id = source_hash[:24]
        expected_source_hash = targets.get(report_id)
        if expected_source_hash is None:
            continue
        if source_hash != expected_source_hash:
            raise RestoreContractError(
                f"Active Dropbox file ID/source_hash mismatch: {report_id}"
            )
        if report_id in matched_paths:
            raise RestoreContractError(
                f"Multiple active Dropbox paths map to report ID: {report_id}"
            )
        matched_paths[report_id] = path

    return frozenset(matched_paths)


def list_revisions(
    token: str,
    path: str,
    api_call: DropboxApiCall = api_post,
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    before_rev = ""
    seen_boundaries: set[str] = set()

    for _page in range(MAX_REVISION_PAGES):
        payload: dict[str, Any] = {
            "path": path,
            "mode": "path",
            "limit": REVISION_PAGE_SIZE,
            "include_restorable_info": True,
        }
        if before_rev:
            payload["before_rev"] = before_rev
        data = api_call(token, "/files/list_revisions", payload)
        entries = data.get("entries")
        if not isinstance(entries, list):
            raise RestoreContractError("Dropbox list_revisions response is missing entries")
        page = [entry for entry in entries if isinstance(entry, dict)]
        result.extend(page)
        if len(page) < REVISION_PAGE_SIZE:
            return result

        next_boundary = str(page[-1].get("rev") or "")
        if not next_boundary or next_boundary in seen_boundaries:
            raise RestoreContractError("Dropbox list_revisions pagination did not advance")
        seen_boundaries.add(next_boundary)
        before_rev = next_boundary

    raise RestoreContractError("Dropbox revision history exceeded the inspection limit")


def build_restore_plan(
    token: str,
    targets: Mapping[str, str],
    paths: Iterable[str],
    api_call: DropboxApiCall = api_post,
) -> tuple[RestoreCandidate, ...]:
    by_id: dict[str, RestoreCandidate] = {}

    for path in paths:
        matches: dict[str, str] = {}
        for revision in list_revisions(token, path, api_call):
            if revision.get("is_restorable") is not True:
                continue
            rev = str(revision.get("rev") or "").strip()
            content_hash = str(revision.get("content_hash") or "").strip()
            if not rev or not content_hash:
                continue
            source_hash = source_hash_for_content_hash(content_hash)
            report_id = source_hash[:24]
            expected_source_hash = targets.get(report_id)
            if expected_source_hash is not None and source_hash != expected_source_hash:
                raise RestoreContractError(
                    f"Dropbox revision ID/source_hash mismatch: {report_id}"
                )
            if expected_source_hash is not None:
                # list_revisions is newest-first; retain the newest matching rev
                # when several revisions have identical content.
                matches.setdefault(report_id, rev)

        if len(matches) > 1:
            raise RestoreContractError(
                "One deleted Dropbox path maps to multiple target report IDs"
            )
        if not matches:
            continue

        report_id, rev = next(iter(matches.items()))
        expected_source_hash = targets[report_id]
        if report_id in by_id:
            raise RestoreContractError(
                f"Multiple deleted Dropbox paths map to report ID: {report_id}"
            )
        by_id[report_id] = RestoreCandidate(
            report_id=report_id,
            source_hash=expected_source_hash,
            path=path,
            rev=rev,
        )

    return tuple(by_id[report_id] for report_id in sorted(by_id))


def restore_candidates(
    token: str,
    candidates: Iterable[RestoreCandidate],
    api_call: DropboxApiCall = api_post,
) -> tuple[str, ...]:
    restored_ids: list[str] = []
    for candidate in candidates:
        try:
            metadata = api_call(
                token,
                "/files/restore",
                {"path": candidate.path, "rev": candidate.rev},
            )
        except Exception as exc:
            raise RestoreContractError(
                f"Dropbox restore failed for report ID: {candidate.report_id}"
            ) from exc

        restored_hash = str(metadata.get("content_hash") or "").strip()
        if (
            not restored_hash
            or source_hash_for_content_hash(restored_hash) != candidate.source_hash
        ):
            raise RestoreContractError(
                f"Dropbox restore verification failed for report ID: {candidate.report_id}"
            )
        restored_ids.append(candidate.report_id)
    return tuple(restored_ids)


def run_restore(
    *,
    catalog: dict[str, Any],
    token: str,
    root: str,
    date_folder: str,
    expected_count: int,
    apply_restore: bool,
    api_call: DropboxApiCall = api_post,
) -> RestoreResult:
    targets = deleted_catalog_targets(catalog, date_folder)
    validate_expected_count(expected_count, len(targets), "catalog_count")

    entries = list_deleted_entries(token, root, api_call)
    already_restored_ids = active_restored_ids(entries, root, date_folder, targets)
    pending_targets = {
        report_id: source_hash
        for report_id, source_hash in targets.items()
        if report_id not in already_restored_ids
    }
    paths = deleted_pdf_paths(entries, root, date_folder)
    folder_tombstones = target_folder_tombstone_count(entries, root, date_folder)
    if pending_targets and folder_tombstones and not paths:
        raise RestoreContractError(
            "target_folder_tombstone_only=true "
            f"folder_tombstone_count={folder_tombstones} child_deleted_pdf_paths=0"
        )
    plan = build_restore_plan(token, pending_targets, paths, api_call)
    resolved_count = len(already_restored_ids) + len(plan)
    validate_expected_count(expected_count, resolved_count, "resolved_count")

    planned_ids = frozenset(candidate.report_id for candidate in plan)
    if planned_ids & already_restored_ids:
        raise RestoreContractError("Restore plan overlaps already restored catalog targets")
    if planned_ids | already_restored_ids != frozenset(targets):
        raise RestoreContractError("Resolved restore plan does not exactly match catalog targets")

    restored_ids = restore_candidates(token, plan, api_call) if apply_restore else ()
    return RestoreResult(
        target_count=len(targets),
        deleted_path_count=len(paths),
        matched_count=resolved_count,
        already_restored_count=len(already_restored_ids),
        pending_restore_count=len(plan),
        restored_count=len(restored_ids),
        report_ids=tuple(sorted(targets)),
    )


def emit_result(result: RestoreResult, apply_restore: bool) -> None:
    print(f"mode={'apply' if apply_restore else 'dry-run'}")
    print(f"target_count={result.target_count}")
    print(f"deleted_path_count={result.deleted_path_count}")
    print(f"matched_count={result.matched_count}")
    print(f"already_restored_count={result.already_restored_count}")
    print(f"pending_restore_count={result.pending_restore_count}")
    print(f"restored_count={result.restored_count}")
    for report_id in result.report_ids:
        print(f"report_id={report_id}")

    write_github_output("mode", "apply" if apply_restore else "dry-run")
    write_github_output("target_count", result.target_count)
    write_github_output("deleted_path_count", result.deleted_path_count)
    write_github_output("matched_count", result.matched_count)
    write_github_output("already_restored_count", result.already_restored_count)
    write_github_output("pending_restore_count", result.pending_restore_count)
    write_github_output("restored_count", result.restored_count)
    write_github_output("report_ids", ",".join(result.report_ids))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog-path", default=DEFAULT_CATALOG_PATH)
    parser.add_argument("--dropbox-root", default=DEFAULT_DROPBOX_ROOT)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--expected-count", required=True, type=int)
    parser.add_argument(
        "--apply-restore",
        action="store_true",
        help="Perform Dropbox files/restore calls. Default: dry-run.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        catalog = load_catalog(Path(args.catalog_path))
        # Check the operator's count before refreshing a token or making any
        # Dropbox request. run_restore repeats this check as a library contract.
        target_ids = deleted_catalog_ids(catalog, args.date_folder)
        validate_expected_count(args.expected_count, len(target_ids), "catalog_count")
        token, scopes = dropbox_access_token_with_scopes()
        validate_restore_scope(scopes, args.apply_restore)
        result = run_restore(
            catalog=catalog,
            token=token,
            root=args.dropbox_root,
            date_folder=args.date_folder,
            expected_count=args.expected_count,
            apply_restore=args.apply_restore,
        )
        emit_result(result, args.apply_restore)
        return 0
    except RestoreContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(
            f"ERROR: unexpected {type(exc).__name__}; private details suppressed",
            file=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
