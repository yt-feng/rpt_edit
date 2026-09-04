#!/usr/bin/env python3
"""Bounded retries for transient DeepSeek HTTP failures."""
from __future__ import annotations

import os
import random
import re
import time
from collections.abc import Callable
from typing import Any

import requests

DEFAULT_DEEPSEEK_MODEL = "deepseek-v4-flash"
LEGACY_DEEPSEEK_MODEL_ALIASES = {
    "deepseek-chat": DEFAULT_DEEPSEEK_MODEL,
    "deepseek-reasoner": DEFAULT_DEEPSEEK_MODEL,
}
RETRYABLE_HTTP_STATUSES = {408, 409, 425, 429, 500, 502, 503, 504}
KEY_FAILOVER_HTTP_STATUSES = RETRYABLE_HTTP_STATUSES | {401, 402, 403}
TRANSIENT_REQUEST_ERRORS = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)


def normalize_deepseek_model_name(value: str | None) -> str:
    """Map retired official model aliases before an API request is sent."""
    model = str(value or "").strip() or DEFAULT_DEEPSEEK_MODEL
    return LEGACY_DEEPSEEK_MODEL_ALIASES.get(model.lower(), model)


def prepare_deepseek_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a request payload with a current model and legacy chat semantics."""
    prepared = dict(payload)
    requested_model = str(prepared.get("model") or "").strip().lower()
    prepared["model"] = normalize_deepseek_model_name(requested_model)
    if prepared["model"].startswith("deepseek-v4-") and "thinking" not in prepared:
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
        dict.fromkeys(re.findall(r"\bdeepseek-[a-z0-9][a-z0-9._-]*\b", lowered))
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
    logger: Callable[[str], None] = print,
) -> requests.Response:
    """POST once for permanent failures and retry bounded transient failures."""
    attempts = max(1, int(max_attempts))
    request_payload = prepare_deepseek_payload(payload)
    attempt = 1
    model_switches = 0
    while attempt <= attempts:
        try:
            response = requests.post(
                url,
                headers=headers,
                json=request_payload,
                timeout=timeout,
            )
        except TRANSIENT_REQUEST_ERRORS as exc:
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
    logger: Callable[[str], None] = print,
) -> requests.Response:
    """Retry each key and switch only after a key-specific failure is exhausted."""
    candidates = api_keys if api_keys is not None else deepseek_api_keys_from_env()
    if not candidates:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

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
                logger=logger,
            )
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
