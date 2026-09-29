#!/usr/bin/env python3
"""Read a private chart checkpoint and emit only bounded structural diagnostics."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import build_chart_search_index as chart
import chart_search_r2 as r2


RUN_ID_RE = re.compile(r"[1-9][0-9]{0,19}")
ATTEMPT_RE = re.compile(r"([1-9][0-9]{0,19})(?::([1-9][0-9]{0,9})(?::recovery-([1-9][0-9]{0,9}))?)?")
HASH_RE = re.compile(r"[0-9a-f]{64}")
STATUSES = ("ok", "error", "quarantined", "unknown")
MAX_ERROR_RECORDS = 100


def bounded_count(value: Any) -> int | None:
    return value if type(value) is int and 0 <= value <= 100_000_000 else None


def report_checkpoint(state: Any, run_id: str) -> dict:
    if not isinstance(run_id, str) or not RUN_ID_RE.fullmatch(run_id):
        raise ValueError("A numeric workflow run ID is required")
    if (not isinstance(state, dict) or type(state.get("schema_version")) is not int
            or state["schema_version"] != 1 or not isinstance(state.get("items"), dict)):
        raise ValueError("Unsupported checkpoint schema")
    totals = Counter({status: 0 for status in STATUSES})
    selected = Counter({status: 0 for status in STATUSES})
    reusable = 0
    selected_reusable = 0
    unknown_attempts = 0
    invalid_records = 0
    errors = []
    for image_hash, record in sorted(state["items"].items()):
        if not isinstance(image_hash, str) or not HASH_RE.fullmatch(image_hash) or not isinstance(record, dict):
            invalid_records += 1
            continue
        status = record.get("status")
        status = status if isinstance(status, str) and status in STATUSES else "unknown"
        totals[status] += 1
        is_reusable = chart.state_is_reusable(record)
        reusable += int(is_reusable)
        last_attempt = record.get("last_attempt_run_id")
        match = ATTEMPT_RE.fullmatch(last_attempt) if isinstance(last_attempt, str) else None
        if match is None:
            unknown_attempts += 1
            continue
        if match[1] != run_id:
            continue
        selected[status] += 1
        selected_reusable += int(is_reusable)
        # Successful hashes are counted but their private analysis is never copied.
        if status not in ("error", "quarantined"):
            continue
        reason = record.get("failure_reason")
        failure_class = record.get("failure_class")
        item = {
            "image_sha256": image_hash,
            "status": status,
            "attempts": bounded_count(record.get("attempts")),
            "stable_attempt_runs": bounded_count(record.get("stable_attempt_runs")),
            "run_attempt": int(match[2]) if match[2] else None,
            "recovery_round": int(match[3]) if match[3] else None,
            "analysis_version_matches": record.get("analysis_version") == chart.ANALYSIS_VERSION,
            "reusable": is_reusable,
            "failure_class": failure_class if isinstance(failure_class, str) and failure_class in ("transient", "stable_image") else "unknown",
            "failure_reason": reason if isinstance(reason, str) and reason in chart.RETRYABLE_REASON_CODES | {"stable_image"} else "unknown",
            "failure_diagnostic": chart.safe_model_diagnostic(record.get("failure_diagnostic")),
        }
        item["diagnostic_available"] = bool(item["failure_diagnostic"])
        errors.append(item)
    return {
        "schema_version": 1,
        "read_status": "available",
        "requested_run_id": run_id,
        "expected_analysis_version": chart.ANALYSIS_VERSION,
        "checkpoint_analysis_version_matches": state.get("analysis_version") == chart.ANALYSIS_VERSION,
        "checkpoint_status_counts": dict(totals),
        "checkpoint_reusable_count": reusable,
        "invalid_record_count": invalid_records,
        "unrecognized_last_attempt_count": unknown_attempts,
        "selection": {
            "basis": "exact_last_attempt_run_id_or_numeric_attempt_and_recovery_suffix",
            "matched_status_counts": dict(selected),
            "matched_reusable_count": selected_reusable,
            "matched_error_count": len(errors),
            "reported_error_count": min(len(errors), MAX_ERROR_RECORDS),
            "error_details_truncated": len(errors) > MAX_ERROR_RECORDS,
            "no_latest_attempt_match": sum(selected.values()) == 0,
        },
        "candidate_coverage": {
            "status": "unavailable",
            "reason": "checkpoint_has_no_run_candidate_manifest_or_full_attempt_history",
            "cache_hits_update_last_attempt": False,
            "candidate_count": None,
            "reusable_count": None,
            "nonreusable_count": None,
        },
        "related_errors": errors[:MAX_ERROR_RECORDS],
    }


def read_report(run_id: str) -> tuple[dict, int]:
    """Use the normal read helper, suppressing raw SDK errors and private data."""
    if not RUN_ID_RE.fullmatch(run_id):
        return {"schema_version": 1, "read_status": "invalid_run_id"}, 1
    base = {"schema_version": 1, "requested_run_id": run_id}
    try:
        client, bucket = r2.client_and_bucket()
        state, found = r2.read_json_object(client, bucket, f"{r2.DEFAULT_PREFIX}/state.json", "state")
    except Exception:
        return {**base, "read_status": "read_failed"}, 1
    if not found:
        return {**base, "read_status": "missing"}, 1
    try:
        return report_checkpoint(state, run_id), 0
    except (TypeError, ValueError):
        return {**base, "read_status": "invalid_schema"}, 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report, status = read_report(args.run_id)
    # Only this newly constructed allowlisted report ever reaches disk/artifacts.
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print("chart_checkpoint_diagnostic status=" + report["read_status"])
    return status


if __name__ == "__main__":
    raise SystemExit(main())
