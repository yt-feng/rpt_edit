#!/usr/bin/env python3
"""Aggregate content-free HTTP usage artifacts without counting copied events twice."""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import re
from typing import Any
from zoneinfo import ZoneInfo

from deepseek_usage import SCHEMA_VERSION, TOKEN_FIELDS, _identifier, _integer

GROUP_FIELDS = ("day", "workflow", "job", "run_id", "run_attempt", "stage", "operation", "model")
PRICE_FIELDS = ("input_cache_hit", "input_cache_miss", "output")
COVERAGE_NOTE = (
    "Observed instrumented HTTP attempts only; this is not a DeepSeek invoice or "
    "an account-wide total. Missing usage and transport failures can include billed "
    "tokens that the client did not receive. Offline translation has zero paid API "
    "calls and does not appear in these token totals. Worker/runtime calls outside "
    "these artifacts are not included."
)


def load_prices(path: Path | None) -> dict[str, dict[str, Decimal]]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Price configuration must map model names to CNY per million token rates")
    prices: dict[str, dict[str, Decimal]] = {}
    for model, row in data.items():
        if not isinstance(row, dict):
            raise ValueError("Each model must contain input_cache_hit, input_cache_miss and output rates")
        parsed = {}
        for name in PRICE_FIELDS:
            try:
                rate = Decimal(str(row[name]))
            except (InvalidOperation, KeyError) as exc:
                raise ValueError("Missing or invalid rate in price configuration") from exc
            if not rate.is_finite() or rate < 0:
                raise ValueError("Rates must be finite nonnegative CNY per million tokens")
            parsed[name] = rate
        prices[model] = parsed
    return prices


def _empty() -> dict[str, Any]:
    return {
        "http_attempts": 0, "successes": 0, "http_errors": 0, "transport_errors": 0,
        "usage_reported_attempts": 0, "usage_missing_attempts": 0,
        "retry_attempts": 0, "key_failover_attempts": 0,
        **{name: 0 for name in TOKEN_FIELDS},
        "missing_token_fields": {name: 0 for name in TOKEN_FIELDS},
        "estimated_cost_cny": Decimal(0), "priced_usage_attempts": 0,
        "unpriced_usage_attempts": 0,
    }


def _count(row: dict[str, Any], event: dict[str, Any], prices: dict[str, dict[str, Decimal]]) -> None:
    row["http_attempts"] += 1
    outcome = _identifier(event.get("outcome"))
    row[{"success": "successes", "http_error": "http_errors"}.get(outcome, "transport_errors")] += 1
    if (_integer(event.get("attempt")) or 1) > 1:
        row["retry_attempts"] += 1
    if (_integer(event.get("key_index")) or 1) > 1:
        row["key_failover_attempts"] += 1
    usage = event.get("usage") if isinstance(event.get("usage"), dict) else {}
    values = {name: _integer(usage.get(name)) for name in TOKEN_FIELDS}
    reported = any(value is not None for value in values.values())
    row["usage_reported_attempts" if reported else "usage_missing_attempts"] += 1
    for name, value in values.items():
        if value is None:
            row["missing_token_fields"][name] += 1
        else:
            row[name] += value
    if reported:
        rates = prices.get(_identifier(event.get("model")), {})
        hit, miss, output = (values[k] for k in ("prompt_cache_hit_tokens", "prompt_cache_miss_tokens", "completion_tokens"))
        if rates and hit is not None and miss is not None and output is not None:
            row["estimated_cost_cny"] += (
                Decimal(hit) * rates["input_cache_hit"]
                + Decimal(miss) * rates["input_cache_miss"]
                + Decimal(output) * rates["output"]
            ) / Decimal(1_000_000)
            row["priced_usage_attempts"] += 1
        else:
            row["unpriced_usage_attempts"] += 1


def summarize(
    input_dirs: list[Path], *, date: str | None = None, timezone: str = "Asia/Shanghai",
    prices: dict[str, dict[str, Decimal]] | None = None,
) -> dict[str, Any]:
    zone = ZoneInfo(timezone)
    if date:
        datetime.strptime(date, "%Y-%m-%d")
    prices = prices or {}
    groups: dict[tuple[str, ...], dict[str, Any]] = defaultdict(_empty)
    totals = _empty()
    seen: set[str] = set()
    duplicate_events = invalid_files = conflicting_events = 0
    signatures: dict[str, str] = {}
    logical_requests: set[str] = set()
    for directory in input_dirs:
        for path in sorted(directory.rglob("*.json")):
            try:
                event = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                invalid_files += 1
                continue
            if not isinstance(event, dict) or event.get("kind") != "deepseek_http_attempt":
                continue  # summary JSON and unrelated artifacts are not events.
            if event.get("schema_version") != SCHEMA_VERSION or not re.fullmatch(r"[0-9a-f]{32}", str(event.get("event_id", ""))):
                invalid_files += 1
                continue
            try:
                timestamp = datetime.fromisoformat(event["occurred_at"])
                if timestamp.tzinfo is None:
                    raise ValueError("Timestamp must have a timezone")
                day = timestamp.astimezone(zone).date().isoformat()
            except (KeyError, TypeError, ValueError):
                invalid_files += 1
                continue
            if date and day != date:
                continue
            event_id = event["event_id"]
            signature = json.dumps(event, sort_keys=True)
            if event_id in seen:
                duplicate_events += 1
                if signatures[event_id] != signature:
                    conflicting_events += 1
                continue
            seen.add(event_id)
            signatures[event_id] = signature
            logical_requests.add(str(event.get("request_id", event_id)))
            key = (day, *(_identifier(event.get(name)) for name in GROUP_FIELDS[1:]))
            _count(groups[key], event, prices)
            _count(totals, event, prices)
    rows = []
    for key, row in sorted(groups.items()):
        row = {**dict(zip(GROUP_FIELDS, key)), **row}
        row["estimated_cost_cny"] = str(row["estimated_cost_cny"]) if prices else None
        rows.append(row)
    totals["estimated_cost_cny"] = str(totals["estimated_cost_cny"]) if prices else None
    totals["logical_requests"] = len(logical_requests)
    return {
        "schema_version": SCHEMA_VERSION, "timezone": timezone, "date_filter": date,
        "coverage": COVERAGE_NOTE,
        "cost_basis": "configured CNY rates per million tokens; estimate, not provider invoice" if prices else "not estimated: no explicit price configuration",
        "duplicate_events_ignored": duplicate_events,
        "invalid_files": invalid_files, "conflicting_duplicate_events": conflicting_events,
        "totals": totals, "groups": rows,
    }


def markdown_report(summary: dict[str, Any]) -> str:
    totals = summary["totals"]
    lines = [
        "## DeepSeek observed usage", "", summary["coverage"], "",
        f"Timezone: {summary['timezone']}; date: {summary['date_filter'] or 'all artifact dates'}.", "",
        f"HTTP attempts: **{totals['http_attempts']}**; logical requests: **{totals['logical_requests']}**; "
        f"attempts without usage: **{totals['usage_missing_attempts']}**; "
        f"duplicate events ignored: **{summary['duplicate_events_ignored']}**.", "",
        f"Cost: {summary['cost_basis']}.", "",
        "| Date | Workflow / job | Stage | Operation | Run / attempt | HTTP calls | Input | Output | Cache hit | Cache miss | Missing usage |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary["groups"]:
        lines.append(
            f"| {row['day']} | {row['workflow']} / {row['job']} | {row['stage']} | "
            f"{row['operation']} | {row['run_id']} / {row['run_attempt']} | "
            f"{row['http_attempts']} | {row['prompt_tokens']} | {row['completion_tokens']} | "
            f"{row['prompt_cache_hit_tokens']} | {row['prompt_cache_miss_tokens']} | {row['usage_missing_attempts']} |"
        )
    if not summary["groups"]:
        lines.append("| — | No instrumented events found | — | — | — | 0 | 0 | 0 | 0 | 0 | 0 |")
    lines.extend(["", "Missing provider counters contribute no known tokens; they are not evidence of zero billed tokens."])
    if totals["estimated_cost_cny"] is not None:
        lines.extend(["", f"Configured-rate estimate: CNY {totals['estimated_cost_cny']}; "
                      f"unpriced responses with usage: {totals['unpriced_usage_attempts']}."])
    if summary["invalid_files"] or summary["conflicting_duplicate_events"]:
        lines.extend(["", f"Accounting diagnostics: {summary['invalid_files']} invalid files; "
                      f"{summary['conflicting_duplicate_events']} conflicting duplicate event IDs."])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--github-summary", action="store_true")
    parser.add_argument("--timezone", default="Asia/Shanghai")
    parser.add_argument("--date", help="Include only attempts occurring on YYYY-MM-DD in --timezone")
    parser.add_argument("--prices-json", type=Path, help="Optional model rates in CNY per million; never a provider invoice")
    args = parser.parse_args()
    summary = summarize(args.input_dir, date=args.date, timezone=args.timezone, prices=load_prices(args.prices_json))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
    markdown = markdown_report(summary)
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown, encoding="utf-8")
    if args.github_summary and os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write(markdown)
    print(f"Observed DeepSeek attempts: {summary['totals']['http_attempts']}; missing usage: {summary['totals']['usage_missing_attempts']}")


if __name__ == "__main__":
    main()
