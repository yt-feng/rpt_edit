#!/usr/bin/env python3
"""Resume one static locale candidate within its observed DeepSeek balance."""

from __future__ import annotations

import argparse
from decimal import Decimal
import gzip
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Callable

from check_deepseek_balance import read_balance


MAX_ROUNDS = 3
ROUND_LIMIT_CNY = Decimal("400")
BALANCE_RESERVE_CNY = Decimal("20")
USAGE_FIELDS = (
    "prompt_tokens", "completion_tokens", "total_tokens",
    "prompt_cache_hit_tokens", "prompt_cache_miss_tokens",
)
OBSERVATION_FIELDS = (
    "usage_unknown_responses", "usage_partial_responses", "unobserved_provider_requests",
)


def _save(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _cache_rows(path: Path | None) -> int:
    if path is None or not path.exists():
        return 0
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        cache = json.load(handle)
    if not isinstance(cache, dict) or not isinstance(cache.get("locales"), dict):
        raise ValueError("Invalid cache structure")
    count = 0
    for locale in ("ko", "ja", "ar"):
        rows = cache["locales"].get(locale, {})
        if not isinstance(rows, dict):
            raise ValueError("Invalid locale cache structure")
        count += sum(
            isinstance(row, dict) and isinstance(row.get("source"), str)
            and isinstance(row.get("translation"), str) and bool(row["translation"].strip())
            for row in rows.values()
        )
    return count


def _number(raw: Any) -> Decimal:
    if not isinstance(raw, str) or not raw or len(raw) > 64:
        raise ValueError("Invalid balance number")
    value = Decimal(raw)
    if not value.is_finite() or value.adjusted() > 30 or value.as_tuple().exponent < -30:
        raise ValueError("Invalid balance number")
    return value


def _safe_balance(raw: Any) -> dict[str, Any]:
    """Never copy arbitrary provider payloads or exception text into this report."""
    if not isinstance(raw, dict) or raw.get("status") not in {"passed", "failed"}:
        raise ValueError("Invalid balance report")
    result: dict[str, Any] = {"status": raw["status"], "mode": "balance", "provider_requests": 0}
    result["balance_requests"] = 1 if raw.get("balance_requests") == 1 else 0
    if type(raw.get("http_status")) is int and 100 <= raw["http_status"] <= 599:
        result["http_status"] = raw["http_status"]
    if raw["status"] != "passed":
        return result
    if type(raw.get("is_available")) is not bool or not isinstance(raw.get("balance_infos"), list):
        raise ValueError("Invalid balance report")
    rows, currencies = [], set()
    for row in raw["balance_infos"]:
        if not isinstance(row, dict) or row.get("currency") not in {"CNY", "USD"}:
            raise ValueError("Invalid balance currency")
        if row["currency"] in currencies:
            raise ValueError("Repeated balance currency")
        currencies.add(row["currency"])
        rows.append({"currency": row["currency"], **{
            field: format(_number(row.get(field)), "f")
            for field in ("total_balance", "granted_balance", "topped_up_balance")
        }})
    result.update(is_available=raw["is_available"], balance_infos=rows)
    return result


def _summary(raw: dict[str, Any]) -> dict[str, Any]:
    status = raw.get("status")
    if status not in {"passed", "checkpointed", "failed"}:
        raise ValueError("Invalid builder status")
    result: dict[str, Any] = {"status": status, "ready": status == "passed"}
    for field in ("provider_requests", "completed_batches", "failed_batches", "remaining_units_total", *OBSERVATION_FIELDS):
        value = raw.get(field)
        if type(value) is int and value >= 0:
            result[field] = value
    usage = raw.get("usage_totals", {})
    if not isinstance(usage, dict):
        raise ValueError("Invalid builder usage")
    result["usage_totals"] = {
        field: usage[field] for field in USAGE_FIELDS
        if type(usage.get(field)) is int and usage[field] >= 0
    }
    if raw.get("stop_category") in {"budget", "repair_limit", "deepl_quota", "provider", "transport", "quality", "systemic"}:
        result["stop_category"] = raw["stop_category"]
    repair = raw.get("deepl_repair")
    if isinstance(repair, dict):
        result["deepl_repair"] = {
            key: repair[key] for key in ("provider_requests", "balance_requests", "billed_characters", "reserved_characters", "remaining_character_budget")
            if type(repair.get(key)) is int and repair[key] >= 0
        }
        result["deepl_repair"]["stopped"] = bool(repair.get("stop_reason"))
    return result


def _resumable_translation_gaps(raw: dict[str, Any]) -> bool:
    """Recognize only the completed translation phase's exact residual error."""
    remaining = raw.get("remaining_units_total")
    requests = raw.get("provider_requests")
    if (
        raw.get("status") != "failed" or raw.get("preflight_only") is not False
        or raw.get("ready") is True or type(remaining) is not int or remaining <= 0
        or raw.get("stop_reason") not in (None, "") or raw.get("stop_category") not in (None, "")
        or raw.get("build_error") != f"Locale translation has {remaining} unresolved source units; completed rows saved"
        or type(requests) is not int or requests < 0
        or type(raw.get("usage_complete_responses")) is not int
        or raw["usage_complete_responses"] != requests
        or any(type(raw.get(field)) is not int or raw[field] != 0 for field in OBSERVATION_FIELDS)
    ):
        return False
    usage = raw.get("usage_totals")
    if requests and (
        not isinstance(usage, dict)
        or any(type(usage.get(field)) is not int or usage[field] < 0
               for field in ("prompt_tokens", "completion_tokens", "total_tokens"))
        or usage["prompt_tokens"] + usage["completion_tokens"] != usage["total_tokens"]
    ):
        return False
    repair = raw.get("deepl_repair")
    if repair is not None and (
        not isinstance(repair, dict) or repair.get("stop_reason") not in (None, "")
        or any(type(repair.get(field)) is not int or repair[field] != 0
               for field in ("unobserved_requests", "reserved_characters"))
    ):
        return False
    return True


def run_backfill(
    builder_args: list[str], *, cache_out: Path, diagnostics_out: Path,
    cache_in: Path | None = None, balance_reader: Callable[..., Any] = read_balance,
    runner: Callable[..., Any] = subprocess.run,
) -> dict[str, Any]:
    report: dict[str, Any] = {
        "schema_version": 1, "mode": "backfill", "status": "running", "ready": False,
        "max_rounds": MAX_ROUNDS, "provider_requests": 0, "balance_requests": 0,
        "usage_totals": {}, "rounds": [],
        **{field: 0 for field in OBSERVATION_FIELDS},
    }
    try:
        forbidden = {"--max-provider-cost-cny", "--checkpoint-on-budget", "--preflight-only"}
        if any(arg.split("=", 1)[0] in forbidden for arg in builder_args):
            raise ValueError("Backfill owns budget and completion options")
        for index in range(1, MAX_ROUNDS + 1):
            balance_path = diagnostics_out.with_name(f"{diagnostics_out.stem}-balance-{index}.json")
            round_path = diagnostics_out.with_name(f"{diagnostics_out.stem}-round-{index}.json")
            current: dict[str, Any] = {"round": index, "status": "running", "ready": False}
            report["rounds"].append(current)
            # Exactly one read-only balance request before each builder invocation.
            balance = _safe_balance(balance_reader())
            _save(balance_path, balance)
            current["balance"] = balance
            report["balance_requests"] += balance["balance_requests"]
            if balance["status"] != "passed":
                report.update(status="failed", stop_category="balance_check")
                current["status"] = "failed"
                break
            cny = next((row for row in balance["balance_infos"] if row["currency"] == "CNY"), None)
            if not balance["is_available"]:
                report.update(status="checkpointed", stop_category="balance_unavailable")
                current["status"] = "checkpointed"
                break
            if cny is None:
                report.update(status="failed", stop_category="missing_cny_balance")
                current["status"] = "failed"
                break
            budget = min(ROUND_LIMIT_CNY, _number(cny["total_balance"]) - BALANCE_RESERVE_CNY)
            current["max_provider_cost_cny"] = format(max(Decimal(0), budget), "f")
            if budget < Decimal("0.000001"):
                report.update(status="checkpointed", stop_category="balance_reserve")
                current["status"] = "checkpointed"
                break
            before = _cache_rows(cache_in)
            current["cache_rows_before"] = before
            _save(diagnostics_out, report)
            command = [sys.executable, "-B", str(Path(__file__).with_name("build_portal_locales.py")),
                       *builder_args, "--cache-out", str(cache_out)]
            if cache_in is not None:
                command.extend(["--cache-in", str(cache_in)])
            command.extend([
                "--max-provider-cost-cny", format(budget, "f"), "--checkpoint-on-budget",
                "--diagnostics-out", str(round_path),
            ])
            # Child inherits credentials through its environment, never CLI args or diagnostics.
            completed = runner(command, check=False)
            if not round_path.is_file():
                raise ValueError("Builder diagnostics missing")
            raw = json.loads(round_path.read_text(encoding="utf-8"))
            if not isinstance(raw, dict):
                raise ValueError("Invalid builder diagnostics")
            current.update(_summary(raw))
            current["exit_code"] = completed.returncode
            for field in ("provider_requests", *OBSERVATION_FIELDS):
                report[field] += current.get(field, 0)
            for field, value in current["usage_totals"].items():
                report["usage_totals"][field] = report["usage_totals"].get(field, 0) + value
            resumable_gaps = completed.returncode == 1 and _resumable_translation_gaps(raw)
            if completed.returncode != 0 or current["status"] == "failed":
                if not resumable_gaps:
                    current.update(status="failed", ready=False)
                    report.update(status="failed", stop_category="builder_failure")
                    break
                # A failed residual-quality phase has no rendered release. Only
                # its newly saved translations may advance a bounded retry.
                current.update(status="checkpointed", ready=False, stop_category="translation_gaps")
            if not cache_out.is_file():
                raise ValueError("Builder checkpoint missing")
            current["cache_rows_after"] = _cache_rows(cache_out)
            if current["status"] == "passed":
                report.update(status="passed", ready=True)
                break
            if current.get("stop_category") == "deepl_quota" and raw.get("ready") is False:
                report.update(status="checkpointed", stop_category="deepl_quota")
                break
            if current.get("stop_category") not in {"budget", "repair_limit", "translation_gaps"} or (
                not resumable_gaps and raw.get("ready") is not False
            ):
                raise ValueError("Unrecognized builder checkpoint")
            if current.get("deepl_repair", {}).get("stopped"):
                report.update(status="checkpointed", stop_category="deepl_stopped")
                break
            if any(current.get(field) != 0 for field in OBSERVATION_FIELDS):
                current.update(status="failed", ready=False)
                report.update(status="failed", stop_category="incomplete_usage")
                break
            report.update(status="checkpointed", stop_category=current["stop_category"])
            if current["cache_rows_after"] <= before:
                report["stop_category"] = "no_progress"
                break
            if index == MAX_ROUNDS:
                report["stop_category"] = "round_limit"
                break
            # Only a bounded checkpoint with observed usage and saved progress may resume.
            cache_in = cache_out
            _save(diagnostics_out, report)
    except Exception as error:
        # Exception messages can contain provider details; use a fixed classification only.
        report.update(status="failed", ready=False, stop_category="orchestration_error",
                      error_type=type(error).__name__)
        if report["rounds"]:
            report["rounds"][-1].update(status="failed", ready=False)
    _save(diagnostics_out, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--cache-in", type=Path)
    parser.add_argument("--cache-out", type=Path, required=True)
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    args, builder_args = parser.parse_known_args()
    report = run_backfill(builder_args, cache_in=args.cache_in, cache_out=args.cache_out,
                          diagnostics_out=args.diagnostics_out)
    print(json.dumps({field: report[field] for field in ("status", "ready", "provider_requests", "balance_requests")}, sort_keys=True))
    return 0 if report["status"] in {"passed", "checkpointed"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
