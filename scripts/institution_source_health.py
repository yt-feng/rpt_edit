#!/usr/bin/env python3
"""Separate verified source-health failures from accepted-source recovery.

The fetcher reserves exit 2 for a completed zero-download run with an unhealthy
required source. Only that exact result may continue to the existing private
backlog consumer. No source request, state repair or seen-state write occurs here.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re
import sys

from fetch_institution_latest_pdfs import DEFAULT_PUBLIC_INSTITUTION_KEYS, INSTITUTIONS, short_hash, slug
from imf_elibrary_resolver import ResolutionError, source_url, title_key, validate_official_pair, validate_publication_url
from institution_verified_originals import RECOVERY_FIELDS, official_url


LIVE_DOWNLOAD_FIELDS = {"schema", "source_guid", "source_url", "landing_url", "pdf_url", "doi", "title",
                        "identity_sha256", "crossref_sha256", "sha256", "bytes", "pages",
                        "landing_status", "pdf_status", "source_identity_verified", "transport"}
PREVIEW_DOWNLOAD_FIELDS = (LIVE_DOWNLOAD_FIELDS - {"crossref_sha256"}) | {"metadata"}


class InvalidSourceHealth(ValueError):
    pass


def require(condition: bool) -> None:
    if not condition:
        raise InvalidSourceHealth("source_health_contract_invalid")


def count(value: object) -> int:
    require(type(value) is int and 0 <= value <= 1_000_000)
    return value


def validate_live_download(row: dict) -> None:
    """Verify the browser's complete receipt against the producer's exact row.

    Identity/Crossref hashes retain upstream provenance. Their complete inputs
    are not in this manifest, so this classifier does not claim to rehash them.
    """
    proof = row["imf_live_download"]
    require(row["institution"] == "imf" and isinstance(proof, dict))
    require(type(proof.get("schema")) is int and proof["schema"] in {1, 2})
    if proof["schema"] == 1:
        require(set(proof) == LIVE_DOWNLOAD_FIELDS)
        provenance_hash = proof["crossref_sha256"]
    else:
        require(set(proof) == PREVIEW_DOWNLOAD_FIELDS)
        metadata = proof["metadata"]
        require(isinstance(metadata, dict) and set(metadata) == {"method", "preview_sha256"}
                and metadata["method"] == "official_source_preview")
        provenance_hash = metadata["preview_sha256"]
    require(isinstance(provenance_hash, str) and bool(re.fullmatch(r"[a-f0-9]{64}", provenance_hash)))
    require(proof["source_identity_verified"] is True
            and proof["transport"] == "existing_subscription_vless_browser")
    for field in ("landing_status", "pdf_status"):
        require(type(proof[field]) is int and proof[field] == 200)
    require(type(proof["pages"]) is int and 1 <= proof["pages"] <= 5000
            and type(proof["bytes"]) is int and 1 <= proof["bytes"] <= 128 * 1024 * 1024)
    for field in ("identity_sha256", "sha256"):
        require(isinstance(proof[field], str) and bool(re.fullmatch(r"[a-f0-9]{64}", proof[field])))
    for field in ("source_guid", "title"):
        require(isinstance(proof[field], str) and 0 < len(proof[field]) <= 4096
                and not re.search(r"[\x00-\x1f\x7f\ud800-\udfff]", proof[field]))
    require(isinstance(row.get("title"), str) and 0 < len(row["title"]) <= 4096
            and bool(title_key(proof["title"])) and title_key(proof["title"]) == title_key(row["title"]))
    require(proof["source_url"] == row.get("source_page_url")
            and proof["pdf_url"] == row.get("pdf_url")
            and proof["sha256"] == row.get("sha256")
            and type(row.get("bytes")) is int and proof["bytes"] == row["bytes"])
    require(row.get("local_filename") == f"IMF_{slug(row['title'])}_{short_hash('imf:' + proof['source_guid'])}.pdf")
    try:
        source_url(proof["source_url"])
        validate_official_pair(proof["landing_url"], proof["pdf_url"], proof["doi"])
        if proof["schema"] == 2:
            locator = validate_publication_url(proof["landing_url"])
            require(locator["kind"] == "journal" and locator["language"] == "en")
    except ResolutionError:
        raise InvalidSourceHealth("source_health_contract_invalid") from None


def enabled_sources(value: str) -> list[str]:
    value = value.strip().lower()
    if value in {"all", "*", ""}:
        result = list(DEFAULT_PUBLIC_INSTITUTION_KEYS)
    elif value in {"everything", "all-including-consulting"}:
        result = list(INSTITUTIONS)
    else:
        result = [part.strip() for part in value.split(",") if part.strip()]
    require(bool(result) and len(result) == len(set(result))
            and all(key in INSTITUTIONS for key in result))
    return result


def classify(manifest: object, *, producer_exit_code: int, log_exit_code: int,
             date_folder: str, institutions: str) -> dict[str, str]:
    require(log_exit_code == 0 and producer_exit_code in {0, 2})
    require(bool(re.fullmatch(r"[0-9]{6}", date_folder)))
    try:
        datetime.strptime(date_folder, "%y%m%d")
    except ValueError:
        raise InvalidSourceHealth("source_health_contract_invalid") from None
    require(isinstance(manifest, dict))
    required_fields = {"date", "generated_at", "since_days", "institutions", "downloaded_count",
                       "dependency_held_count", "skipped_count", "source_checks",
                       "force_reprocess", "downloaded", "skipped"}
    require(set(manifest) == required_fields and manifest["date"] == date_folder)
    try:
        generated = datetime.fromisoformat(manifest["generated_at"])
    except (TypeError, ValueError):
        raise InvalidSourceHealth("source_health_contract_invalid") from None
    require(generated.tzinfo is not None and type(manifest["force_reprocess"]) is bool)
    count(manifest["since_days"])
    enabled = enabled_sources(institutions)
    require(manifest["institutions"] == enabled)
    downloaded, skipped, checks = (manifest[key] for key in ("downloaded", "skipped", "source_checks"))
    require(all(isinstance(rows, list) for rows in (downloaded, skipped, checks)))
    require(count(manifest["downloaded_count"]) == len(downloaded)
            and count(manifest["skipped_count"]) == len(skipped))
    require(all(isinstance(row, dict) and row.get("institution") in enabled for row in downloaded + skipped))
    require(count(manifest["dependency_held_count"]) == sum(row.get("reason") == "dependency_hold" for row in skipped))
    require(0 < len(checks) <= len(enabled))
    checked = []
    blocked = []
    actual_downloads = Counter(row["institution"] for row in downloaded)
    recovered = Counter()
    recovery_manifests = {}
    for row in downloaded:
        recovery_fields = {field for field in row if field == "acquisition_method"
                           or (isinstance(field, str) and field.startswith("verified_original_"))}
        live_fields = {field for field in row if isinstance(field, str) and field.startswith("imf_live_download")}
        if live_fields:
            require(live_fields == {"imf_live_download"} and not recovery_fields)
            validate_live_download(row)
        if not recovery_fields:
            continue
        require(recovery_fields == RECOVERY_FIELDS)
        require(row["acquisition_method"] == "verified_original_cache" and row["institution"] == "imf")
        for field in ("verified_original_manifest_sha256", "verified_original_binding_id", "verified_original_receipt_sha256"):
            require(isinstance(row.get(field), str) and bool(re.fullmatch(r"[a-f0-9]{64}", row[field])))
        require(0 < count(row.get("verified_original_pages")) <= 5000)
        require(official_url(row.get("verified_original_landing_url"), pdf=False)
                and official_url(row.get("pdf_url"), pdf=True))
        key = row["institution"]
        require(key not in recovery_manifests or recovery_manifests[key] == row["verified_original_manifest_sha256"])
        recovered[key] += 1
        recovery_manifests[key] = row["verified_original_manifest_sha256"]
    for check in checks:
        fields = {
            "institution", "institution_en", "status", "item_count", "new_pdf_count",
            "eligible_item_count", "resolution_failure_count", "deferred_retry_count", "discovery_error", "required_for_clean_zero", "error"}
        recovery_fields = {"verified_original_recovery_count", "verified_original_manifest_sha256"}
        require(isinstance(check, dict) and set(check) in (fields, fields | recovery_fields))
        key = check["institution"]
        require(isinstance(key, str) and key in enabled and key not in checked)
        checked.append(key)
        cfg = INSTITUTIONS[key]
        require(check["institution_en"] == cfg["name_en"]
                and type(check["required_for_clean_zero"]) is bool
                and check["required_for_clean_zero"] == bool(cfg.get("required_for_clean_zero"))
                and isinstance(check["error"], str))
        total, new, eligible, failures = (count(check[name]) for name in (
            "item_count", "new_pdf_count", "eligible_item_count", "resolution_failure_count"))
        require(total >= eligible >= new + failures and new == actual_downloads[key])
        recovery_count = count(check.get("verified_original_recovery_count", 0))
        require(recovery_count == recovered[key] and recovery_count <= new)
        if recovery_fields <= set(check):
            require(key == "imf" and isinstance(check["verified_original_manifest_sha256"], str)
                    and bool(re.fullmatch(r"[a-f0-9]{64}", check["verified_original_manifest_sha256"]))
                    and (not recovery_count or check["verified_original_manifest_sha256"] == recovery_manifests[key]))
        deferred = count(check["deferred_retry_count"])
        require(deferred <= total and (key == "imf" or deferred == 0))
        discovery_error = check["discovery_error"]
        require(type(discovery_error) is bool)
        status = check["status"]
        require(status in {"ok", "empty", "error", "degraded"})
        if discovery_error and new == recovery_count:
            require(status == "error")
        if status == "ok":
            require(total > 0 and failures == deferred == recovery_count == 0 and not discovery_error)
        elif status == "empty":
            require(total == eligible == new == failures == deferred == 0 and not discovery_error)
        elif status == "degraded":
            require((0 < failures < eligible) or (deferred > 0 and (new > 0 or failures < eligible))
                    or (discovery_error and new > 0) or recovery_count > 0)
        else:
            require((total == eligible == new == failures == 0)
                    or (0 < eligible == failures and new == 0)
                    or (deferred > 0 and eligible == failures == new == 0)
                    or (discovery_error and new == recovery_count))
        if check["required_for_clean_zero"] and status != "ok":
            blocked.append(key)
    # A max-total cap may end a successful run early, but never a zero-PDF run.
    require(checked == enabled[:len(checked)] and all(key in checked for key in actual_downloads))
    if not downloaded:
        require(checked == enabled)
    known_health_exit = not downloaded and bool(blocked)
    require((producer_exit_code == 2) == known_health_exit)
    return {
        "source_health": "degraded" if blocked else "healthy",
        "source_health_required_failure_count": str(len(blocked)),
        "source_health_failed_institutions": ",".join(blocked),
        "source_health_backlog_only": "true" if known_health_exit else "false",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--producer-exit-code", required=True, type=int)
    parser.add_argument("--log-exit-code", required=True, type=int)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--institutions", required=True)
    parser.add_argument("--github-output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        require(not args.manifest.is_symlink() and args.manifest.stat().st_size <= 8 * 1024 * 1024)
        result = classify(json.loads(args.manifest.read_text(encoding="utf-8")),
                          producer_exit_code=args.producer_exit_code, log_exit_code=args.log_exit_code,
                          date_folder=args.date_folder, institutions=args.institutions)
        with args.github_output.open("a", encoding="utf-8") as output:
            for key, value in result.items():
                output.write(f"{key}={value}\n")
    except (InvalidSourceHealth, OSError, ValueError, TypeError, KeyError):
        print("::error::Institution fetch did not satisfy the source-health continuation contract.", file=sys.stderr)
        return 1
    if result["source_health"] == "degraded":
        print("::warning::Required institution source health remains degraded; accepted-source recovery can continue independently.")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
