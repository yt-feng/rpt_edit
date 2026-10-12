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

from fetch_institution_latest_pdfs import DEFAULT_PUBLIC_INSTITUTION_KEYS, INSTITUTIONS


class InvalidSourceHealth(ValueError):
    pass


def require(condition: bool) -> None:
    if not condition:
        raise InvalidSourceHealth("source_health_contract_invalid")


def count(value: object) -> int:
    require(type(value) is int and 0 <= value <= 1_000_000)
    return value


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
    for check in checks:
        require(isinstance(check, dict) and set(check) == {
            "institution", "institution_en", "status", "item_count", "new_pdf_count",
            "eligible_item_count", "resolution_failure_count", "deferred_retry_count", "discovery_error", "required_for_clean_zero", "error"})
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
        deferred = count(check["deferred_retry_count"])
        require(deferred <= total and (key == "imf" or deferred == 0))
        discovery_error = check["discovery_error"]
        require(type(discovery_error) is bool)
        status = check["status"]
        require(status in {"ok", "empty", "error", "degraded"})
        if status == "ok":
            require(total > 0 and failures == deferred == 0 and not discovery_error)
        elif status == "empty":
            require(total == eligible == new == failures == deferred == 0 and not discovery_error)
        elif status == "degraded":
            require((0 < failures < eligible) or (deferred > 0 and (new > 0 or failures < eligible))
                    or (discovery_error and new > 0))
        else:
            require((total == eligible == new == failures == 0)
                    or (0 < eligible == failures and new == 0)
                    or (deferred > 0 and eligible == failures == new == 0)
                    or (discovery_error and new == 0))
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
