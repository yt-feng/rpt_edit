#!/usr/bin/env python3
"""Content-free, atomic accounting for observed DeepSeek HTTP attempts.

One immutable event per physical HTTP attempt makes writes safe across threads and
processes. Copied artifacts can be deduplicated by event_id without hiding paid
reruns. Provider usage is observed, never inferred from prompt length.
"""
from __future__ import annotations

import inspect
import json
import os
from pathlib import Path
import re
import tempfile
from datetime import datetime, timezone
from typing import Any
import uuid

SCHEMA_VERSION = 1
TOKEN_FIELDS = (
    "prompt_tokens", "completion_tokens", "total_tokens",
    "prompt_cache_hit_tokens", "prompt_cache_miss_tokens",
)
_WARNING_PRINTED = False


def _identifier(value: Any, default: str = "unknown") -> str:
    if not isinstance(value, str) or not value or len(value) > 180:
        return default
    # Metadata comes from source code/GitHub, never request labels or bodies.
    if not re.fullmatch(r"[A-Za-z0-9_ .:/()\[\]-]+", value) or "sk-" in value.lower():
        return default
    return value


def operation_from_stack() -> str:
    """Use a source call site, never a label containing a report title/path."""
    frame = inspect.currentframe()
    fallback = "unknown"
    try:
        frame = frame.f_back if frame else None
        while frame is not None:
            name = Path(frame.f_code.co_filename).stem
            function = frame.f_code.co_name
            if name not in {"deepseek_http", "deepseek_usage"}:
                operation = _identifier(f"{name}.{function}:L{frame.f_lineno}")
                if fallback == "unknown":
                    fallback = operation
                if function not in {"call_deepseek", "safe_generate_text"}:
                    return operation
            frame = frame.f_back
        return fallback
    finally:
        del frame


def usage_enabled() -> bool:
    return bool(os.getenv("DEEPSEEK_USAGE_DIR", "").strip())


def _integer(value: Any) -> int | None:
    return value if type(value) is int and value >= 0 else None


def record_attempt(
    *, request_id: str, operation: str, model: str, attempt: int,
    retry_attempt: int, model_switches: int, key_index: int,
    elapsed_ms: int, response: Any = None, transport_error: bool = False,
) -> None:
    """Record allowlisted metadata; accounting failures never retry a paid call."""
    directory = os.getenv("DEEPSEEK_USAGE_DIR", "").strip()
    if not directory:
        return
    temporary: str | None = None
    try:
        usage: dict[str, Any] = {}
        if response is not None:
            try:
                body = response.json()
                if isinstance(body, dict) and isinstance(body.get("usage"), dict):
                    usage = body["usage"]
            except Exception:
                pass
        counters = {name: _integer(usage.get(name)) for name in TOKEN_FIELDS}
        now = datetime.now(timezone.utc)
        event_id = uuid.uuid4().hex
        status = _integer(getattr(response, "status_code", None))
        event = {
            "schema_version": SCHEMA_VERSION,
            "kind": "deepseek_http_attempt",
            "event_id": event_id,
            "request_id": request_id,
            "occurred_at": now.isoformat(),
            "workflow": _identifier(os.getenv("GITHUB_WORKFLOW", "local")),
            "job": _identifier(os.getenv("GITHUB_JOB", "local")),
            "run_id": _identifier(os.getenv("GITHUB_RUN_ID", "local")),
            "run_attempt": _identifier(os.getenv("GITHUB_RUN_ATTEMPT", "1")),
            "stage": _identifier(os.getenv("DEEPSEEK_USAGE_STAGE", "unspecified")),
            "operation": _identifier(operation),
            "model": _identifier(model),
            "attempt": attempt,
            "retry_attempt": retry_attempt,
            "model_switches": model_switches,
            "key_index": key_index,
            "elapsed_ms": max(0, elapsed_ms),
            "http_status": status,
            "outcome": "transport_error" if transport_error else (
                "success" if status is not None and 200 <= status < 300 else "http_error"
            ),
            "usage_reported": any(value is not None for value in counters.values()),
            "usage": counters,
        }
        target = Path(directory) / now.strftime("%Y-%m-%d")
        target.mkdir(parents=True, exist_ok=True)
        # Readers only see completed JSON files. Unique files avoid lost updates
        # and interleaved append records when multiple processes run in a shard.
        fd, temporary = tempfile.mkstemp(prefix=".usage-", suffix=".tmp", dir=target)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(event, handle, ensure_ascii=True, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, target / f"{event_id}.json")
        temporary = None
    except Exception:
        global _WARNING_PRINTED
        if not _WARNING_PRINTED:
            print("::warning::DeepSeek usage accounting could not persist an event; totals may be incomplete.")
            _WARNING_PRINTED = True
    finally:
        if temporary:
            try:
                os.unlink(temporary)
            except OSError:
                pass
