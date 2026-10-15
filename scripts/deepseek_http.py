#!/usr/bin/env python3
"""Bounded retries for transient DeepSeek HTTP failures."""
from __future__ import annotations

import os
import random
import re
import signal
import threading
import time
import uuid
from collections.abc import Callable
from contextlib import contextmanager
from typing import Any

import requests

from deepseek_usage import operation_from_stack, record_attempt, usage_enabled

DEFAULT_DEEPSEEK_MODEL = "deepseek-flash"
LEGACY_DEEPSEEK_MODEL_ALIASES = {
    "deepseek-chat": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-reasoner": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-v4-flash": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-v4-pro": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-v4.1-flash": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-v4.1-pro": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-pro": DEFAULT_DEEPSEEK_MODEL,
}
RETRYABLE_HTTP_STATUSES = {408, 409, 425, 429, 500, 502, 503, 504}
KEY_FAILOVER_HTTP_STATUSES = RETRYABLE_HTTP_STATUSES | {401, 402, 403}
MAX_COMPLETION_RESPONSE_BYTES = 16 * 1024 * 1024
TRANSIENT_REQUEST_ERRORS = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)


class DeepSeekResponseError(RuntimeError):
    """An unusable completion, described without echoing provider content."""

    def __init__(self, category: str, *, retryable: bool = True, key_failover: bool = True):
        self.category = category
        self.retryable = retryable
        self.key_failover = key_failover
        super().__init__(f"DeepSeek completion response: {category}")


def _completion_error(response: requests.Response) -> DeepSeekResponseError | None:
    """HTTP 200 can carry an error after the provider's keep-alive headers."""
    if not 200 <= response.status_code < 300:
        return None
    try:
        data = response.json()
    except (ValueError, TypeError):
        return DeepSeekResponseError("invalid_json")
    if not isinstance(data, dict):
        return DeepSeekResponseError("invalid_envelope")
    error = data.get("error")
    if error:
        # Inspect but never persist free-form provider error messages: they may
        # contain request content or credentials. Only our categories leave here.
        code = str(error.get("code", "")).lower().strip() if isinstance(error, dict) else ""
        kind = str(error.get("type", "")).lower().strip() if isinstance(error, dict) else ""
        detail = str(error.get("message", "")).lower() if isinstance(error, dict) else str(error).lower()
        categories = (
            ({"timeout", "request_timeout", "server_error", "server_overloaded", "rate_limit", "rate_limit_exceeded", "429", "500", "503"}, ("request timeout", "request timed out", "server is overloaded", "server overloaded", "temporarily unavailable"), "provider_unavailable", True, True),
            ({"insufficient_balance", "402"}, ("insufficient balance",), "insufficient_balance", False, True),
            ({"authentication_error", "invalid_api_key", "unauthorized", "401", "403"}, ("invalid api key", "authentication fails"), "authentication_failed", False, True),
            ({"invalid_request_error", "invalid_parameters", "context_length_exceeded", "invalid_model", "model_not_found", "400", "422"}, ("invalid parameter", "maximum context length"), "invalid_request", False, False),
            ({"content_filter", "content_policy_violation"}, ("content filter",), "content_filtered", False, False),
        )
        # Structured codes take precedence over quoted/free-form message text.
        for identifier in (code, kind):
            for codes, _phrases, category, retryable, failover in categories:
                if identifier in codes:
                    return DeepSeekResponseError(category, retryable=retryable, key_failover=failover)
        for _codes, phrases, category, retryable, failover in categories:
            if any(phrase in detail for phrase in phrases):
                return DeepSeekResponseError(category, retryable=retryable, key_failover=failover)
        return DeepSeekResponseError("provider_error")
    choices = data.get("choices")
    if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
        return DeepSeekResponseError("missing_choices")
    choice = choices[0]
    if choice.get("finish_reason") in ("insufficient_system_resource", "aborted"):
        return DeepSeekResponseError("generation_interrupted")
    if choice.get("finish_reason") == "content_filter":
        return DeepSeekResponseError("content_filtered", retryable=False, key_failover=False)
    message = choice.get("message")
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, str) or not content.strip():
        return DeepSeekResponseError("missing_content")
    return None


@contextmanager
def _main_thread_deadline(seconds: float):
    """Interrupt blocked I/O without overriding another owner's active timer."""
    supported = hasattr(signal, "setitimer") and threading.current_thread() is threading.main_thread()
    if not supported or signal.getitimer(signal.ITIMER_REAL)[0]:
        yield
        return
    previous = signal.getsignal(signal.SIGALRM)
    def expired(_signum, _frame):
        raise requests.exceptions.Timeout("DeepSeek response deadline exceeded")
    signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def _post_with_deadline(url: str, *, headers: dict[str, str], payload: dict[str, Any], timeout: float) -> requests.Response:
    """Consume a nonstream completion while bounding keep-alive waiting.

    requests' timeout is a socket idle timeout, not a response deadline. Read
    one byte at a time so periodic whitespace cannot hide a 15-minute queue.
    The caller's socket tolerance is preserved. On the main thread (the article
    pipelines), a timer also bounds silent I/O; in worker threads a final socket
    read can extend the deadline by at most one caller timeout. The API request
    itself remains nonstreaming.
    """
    budget = max(0.001, float(timeout))
    deadline = time.monotonic() + budget
    with _main_thread_deadline(budget):
        response = requests.post(url, headers=headers, json=payload, timeout=budget, stream=True)
        try:
            body = bytearray()
            for chunk in response.iter_content(chunk_size=1):
                if time.monotonic() >= deadline:
                    raise requests.exceptions.Timeout("DeepSeek response deadline exceeded")
                if len(body) + len(chunk) > MAX_COMPLETION_RESPONSE_BYTES:
                    raise DeepSeekResponseError("response_too_large", retryable=False, key_failover=False)
                body.extend(chunk)
            if time.monotonic() >= deadline:
                raise requests.exceptions.Timeout("DeepSeek response deadline exceeded")
            response._content = bytes(body)
            response._content_consumed = True
            return response
        finally:
            response.close()


def normalize_deepseek_model_name(value: str | None) -> str:
    """Route legacy and Pro model aliases to current Flash before API calls."""
    model = str(value or "").strip() or DEFAULT_DEEPSEEK_MODEL
    if re.fullmatch(r"deepseek-v4(?:\.1)?-pro-[a-z0-9][a-z0-9._-]*", model, re.IGNORECASE):
        return DEFAULT_DEEPSEEK_MODEL
    return LEGACY_DEEPSEEK_MODEL_ALIASES.get(model.lower(), model)


def prepare_deepseek_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a request payload with a current model and legacy chat semantics."""
    prepared = dict(payload)
    requested_model = str(prepared.get("model") or "").strip().lower()
    prepared["model"] = normalize_deepseek_model_name(requested_model)
    supports_thinking = prepared["model"] == DEFAULT_DEEPSEEK_MODEL or prepared["model"].startswith("deepseek-v4-")
    if supports_thinking and "thinking" not in prepared:
        prepared["thinking"] = {
            "type": "enabled" if requested_model == "deepseek-reasoner" else "disabled"
        }
    return prepared


def _model_replacement_from_response(
    response: requests.Response,
    current_model: str,
) -> str | None:
    if response.status_code != 400:
        return None
    try:
        text = response.text
    except Exception:
        return None
    if not isinstance(text, str):
        return None
    lowered = text.lower()
    if "model" not in lowered or not any(
        marker in lowered
        for marker in ("supported", "unsupported", "not support", "invalid model")
    ):
        return None
    suggested = list(
        dict.fromkeys(
            normalize_deepseek_model_name(name)
            for name in re.findall(r"\bdeepseek-[a-z0-9][a-z0-9._-]*\b", lowered)
        )
    )
    configured = normalize_deepseek_model_name(
        os.getenv("DEEPSEEK_MODEL_FALLBACK", DEFAULT_DEEPSEEK_MODEL)
    )
    if configured != current_model and (not suggested or configured in suggested):
        return configured
    for candidate in suggested:
        if candidate != current_model:
            return candidate
    return None


def deepseek_api_keys_from_env() -> list[tuple[str, str]]:
    """Return distinct DeepSeek keys in primary-to-backup order."""
    keys: list[tuple[str, str]] = []
    seen: set[str] = set()
    for env_name in (
        "DEEPSEEK_API_KEY",
        "DEEPSEEK_API_KEY_BACKUP",
        "DEEPSEEK_API_KEY_2",
        "DEEPSEEK_API_KEYS",
    ):
        raw_value = os.getenv(env_name, "")
        values = [part.strip() for part in re.split(r"[\n,;]+", raw_value) if part.strip()]
        for index, api_key in enumerate(values, 1):
            if api_key in seen:
                continue
            seen.add(api_key)
            label = env_name if len(values) == 1 else f"{env_name}_{index}"
            keys.append((label, api_key))
    return keys


def _retry_delay(
    attempt: int,
    base_seconds: float,
    max_seconds: float,
    response: requests.Response | None = None,
    jitter_ratio: float = 0.25,
) -> float:
    delay = max(0.0, base_seconds) * (2 ** max(0, attempt - 1))
    if response is not None:
        retry_after = response.headers.get("Retry-After", "").strip()
        try:
            delay = max(delay, float(retry_after))
        except (TypeError, ValueError):
            pass
    maximum = max(0.0, max_seconds)
    bounded = min(maximum, delay)
    jitter_room = min(
        max(0.0, maximum - bounded),
        bounded * min(1.0, max(0.0, jitter_ratio)),
    )
    return bounded + (random.uniform(0.0, jitter_room) if jitter_room else 0.0)


def request_with_retry(
    url: str,
    *,
    headers: dict[str, str],
    payload: dict[str, Any],
    label: str,
    timeout: float = 180,
    max_attempts: int = 4,
    retry_base_seconds: float = 4,
    retry_max_seconds: float = 45,
    retry_jitter_ratio: float = 0.25,
    allow_model_fallback: bool = True,
    validate_completion: bool = True,
    logger: Callable[[str], None] = print,
    usage_operation: str | None = None,
    _usage_request_id: str | None = None,
    _usage_key_index: int = 1,
) -> requests.Response:
    """Retry transient transport/envelope failures within the caller's budget.

    Metered callers with their own envelope validation may disable the latter;
    semantic failures are still recorded in the usage ledger before returning.
    """
    attempts = max(1, int(max_attempts))
    request_payload = prepare_deepseek_payload(payload)
    attempt = 1
    model_switches = 0
    physical_attempt = 0
    request_id = _usage_request_id or uuid.uuid4().hex
    operation = usage_operation or (operation_from_stack() if usage_enabled() else "unknown")
    while attempt <= attempts:
        physical_attempt += 1
        started = time.monotonic()
        thinking = request_payload.get("thinking")
        thinking_mode = thinking.get("type") if isinstance(thinking, dict) else "unknown"
        try:
            response = _post_with_deadline(
                url,
                headers=headers,
                payload=request_payload,
                timeout=timeout,
            )
        except DeepSeekResponseError as exc:
            record_attempt(
                request_id=request_id, operation=operation,
                model=str(request_payload.get("model") or ""),
                attempt=physical_attempt, retry_attempt=attempt,
                model_switches=model_switches, key_index=_usage_key_index,
                elapsed_ms=int((time.monotonic() - started) * 1000),
                response_error=exc.category, thinking_mode=thinking_mode,
            )
            raise
        except TRANSIENT_REQUEST_ERRORS as exc:
            record_attempt(
                request_id=request_id, operation=operation,
                model=str(request_payload.get("model") or ""),
                attempt=physical_attempt, retry_attempt=attempt,
                model_switches=model_switches, key_index=_usage_key_index,
                elapsed_ms=int((time.monotonic() - started) * 1000),
                transport_error=True, thinking_mode=thinking_mode,
            )
            if attempt >= attempts:
                raise
            delay = _retry_delay(
                attempt,
                retry_base_seconds,
                retry_max_seconds,
                jitter_ratio=retry_jitter_ratio,
            )
            logger(
                f"DeepSeek {label}: transient {type(exc).__name__} on attempt "
                f"{attempt}/{attempts}; retrying in {delay:g}s."
            )
            time.sleep(delay)
            attempt += 1
            continue

        completion_error = _completion_error(response)
        record_attempt(
            request_id=request_id, operation=operation,
            model=str(request_payload.get("model") or ""),
            attempt=physical_attempt, retry_attempt=attempt,
            model_switches=model_switches, key_index=_usage_key_index,
            elapsed_ms=int((time.monotonic() - started) * 1000),
            response=response, thinking_mode=thinking_mode,
            response_error=completion_error.category if completion_error else None,
        )
        if completion_error and validate_completion:
            if not completion_error.retryable or attempt >= attempts:
                raise completion_error
            delay = _retry_delay(attempt, retry_base_seconds, retry_max_seconds,
                                 response=response, jitter_ratio=retry_jitter_ratio)
            logger(f"DeepSeek {label}: HTTP {response.status_code} {completion_error.category} "
                   f"on attempt {attempt}/{attempts}; retrying in {delay:g}s.")
            time.sleep(delay)
            attempt += 1
            continue
        replacement = (
            _model_replacement_from_response(
                response,
                str(request_payload.get("model") or ""),
            )
            if allow_model_fallback
            else None
        )
        if replacement and model_switches < 2:
            previous = str(request_payload.get("model") or "")
            request_payload = prepare_deepseek_payload(
                {**request_payload, "model": replacement}
            )
            model_switches += 1
            logger(
                f"DeepSeek {label}: model {previous} is unsupported; "
                f"retrying with {replacement}."
            )
            continue

        if response.status_code not in RETRYABLE_HTTP_STATUSES or attempt >= attempts:
            return response

        delay = _retry_delay(
            attempt,
            retry_base_seconds,
            retry_max_seconds,
            response=response,
            jitter_ratio=retry_jitter_ratio,
        )
        logger(
            f"DeepSeek {label}: retryable HTTP {response.status_code} on attempt "
            f"{attempt}/{attempts}; retrying in {delay:g}s."
        )
        time.sleep(delay)
        attempt += 1

    raise RuntimeError(f"DeepSeek {label}: retry loop ended unexpectedly")


def request_with_key_fallback(
    url: str,
    *,
    headers: dict[str, str],
    payload: dict[str, Any],
    label: str,
    api_keys: list[tuple[str, str]] | None = None,
    timeout: float = 180,
    max_attempts: int = 4,
    retry_base_seconds: float = 4,
    retry_max_seconds: float = 45,
    retry_jitter_ratio: float = 0.25,
    allow_model_fallback: bool = True,
    validate_completion: bool = True,
    logger: Callable[[str], None] = print,
    usage_operation: str | None = None,
) -> requests.Response:
    """Retry each key and switch only after a key-specific failure is exhausted."""
    candidates = api_keys if api_keys is not None else deepseek_api_keys_from_env()
    if not candidates:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

    request_id = uuid.uuid4().hex
    operation = usage_operation or (operation_from_stack() if usage_enabled() else "unknown")
    last_response: requests.Response | None = None
    last_exception: Exception | None = None
    for index, (key_label, api_key) in enumerate(candidates):
        request_headers = dict(headers)
        request_headers["Authorization"] = f"Bearer {api_key}"
        has_backup = index + 1 < len(candidates)
        try:
            response = request_with_retry(
                url,
                headers=request_headers,
                payload=payload,
                label=label,
                timeout=timeout,
                max_attempts=max_attempts,
                retry_base_seconds=retry_base_seconds,
                retry_max_seconds=retry_max_seconds,
                retry_jitter_ratio=retry_jitter_ratio,
                allow_model_fallback=allow_model_fallback,
                validate_completion=validate_completion,
                logger=logger,
                usage_operation=operation,
                _usage_request_id=request_id,
                _usage_key_index=index + 1,
            )
        except DeepSeekResponseError as exc:
            last_exception = exc
            if not has_backup or not exc.key_failover:
                raise
            logger(f"DeepSeek {label}: {key_label} exhausted {exc.category} retries; "
                   "switching to the next configured key.")
            continue
        except TRANSIENT_REQUEST_ERRORS as exc:
            last_exception = exc
            if not has_backup:
                raise
            logger(
                f"DeepSeek {label}: {key_label} exhausted transient retries; "
                "switching to the next configured key."
            )
            continue

        last_response = response
        if response.status_code not in KEY_FAILOVER_HTTP_STATUSES or not has_backup:
            return response
        logger(
            f"DeepSeek {label}: {key_label} returned HTTP {response.status_code}; "
            "switching to the next configured key."
        )

    if last_response is not None:
        return last_response
    if last_exception is not None:
        raise last_exception
    raise RuntimeError(f"DeepSeek {label}: no API key attempt was made")
