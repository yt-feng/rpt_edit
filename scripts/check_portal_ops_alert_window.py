#!/usr/bin/env python3
"""Gate workflow-failure email alerts on recent GitHub Actions health."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def parse_timestamp(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def workflow_dedupe_key(source_workflow: str) -> str:
    normalized = " ".join(str(source_workflow or "").split())
    if not normalized:
        raise ValueError("source_workflow is required")
    return f"workflow-failure:{normalized}"[:240]


def evaluate_recent_runs(
    runs: list[dict[str, Any]],
    *,
    current_run_id: str,
    current_started_at: Any = None,
    now: datetime | None = None,
    window_hours: float = 24,
) -> dict[str, Any]:
    if window_hours <= 0:
        raise ValueError("window_hours must be positive")
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    current_id = str(current_run_id or "").strip()
    current_started = parse_timestamp(current_started_at) or next(
        (
            parse_timestamp(run.get("startedAt")) or parse_timestamp(run.get("createdAt"))
            for run in runs
            if str(run.get("databaseId") or "").strip() == current_id
        ),
        None,
    )
    reference_time = current_started or now
    cutoff = reference_time - timedelta(hours=window_hours)
    recent: list[dict[str, Any]] = []
    for run in runs:
        if not isinstance(run, dict):
            continue
        run_id = str(run.get("databaseId") or "").strip()
        if current_id and run_id == current_id:
            continue
        started_at = parse_timestamp(run.get("startedAt")) or parse_timestamp(run.get("createdAt"))
        if started_at is None or started_at < cutoff:
            continue
        recent.append(run)

    if any(str(run.get("conclusion") or "").lower() == "success" for run in recent):
        return {
            "should_alert": False,
            "reason": "recent_success",
            "recent_count": len(recent),
        }
    return {
        "should_alert": True,
        "reason": "no_success_in_window",
        "recent_count": len(recent),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-json", type=Path, required=True)
    parser.add_argument("--source-workflow", required=True)
    parser.add_argument("--current-run-id", required=True)
    parser.add_argument("--current-started-at", required=True)
    parser.add_argument("--window-hours", type=float, default=24)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = json.loads(args.runs_json.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("runs JSON must contain a list")
    decision = evaluate_recent_runs(
        payload,
        current_run_id=args.current_run_id,
        current_started_at=args.current_started_at,
        window_hours=args.window_hours,
    )
    print(f"should_alert={'true' if decision['should_alert'] else 'false'}")
    print(f"reason={decision['reason']}")
    print(f"recent_count={decision['recent_count']}")
    print(f"dedupe_key={workflow_dedupe_key(args.source_workflow)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
