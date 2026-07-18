#!/usr/bin/env python3
"""Bounded retries for transient DeepSeek HTTP failures."""
from __future__ import annotations

import time
from collections.abc import Callable
from typing import Any

import requests

RETRYABLE_HTTP_STATUSES = {408, 409, 425, 429, 500, 502, 503, 504}
TRANSIENT_REQUEST_ERRORS = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)


def _retry_delay(
    attempt: int,
    base_seconds: float,
    max_seconds: float,
    response: requests.Response | None = None,
) -> float:
    delay = max(0.0, base_seconds) * (2 ** max(0, attempt - 1))
    if response is not None:
        retry_after = response.headers.get("Retry-After", "").strip()
        try:
            delay = max(delay, float(retry_after))
        except (TypeError, ValueError):
            pass
    return min(max(0.0, max_seconds), delay)


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
    logger: Callable[[str], None] = print,
) -> requests.Response:
    """POST once for permanent failures and retry bounded transient failures."""
    attempts = max(1, int(max_attempts))
    for attempt in range(1, attempts + 1):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=timeout,
            )
        except TRANSIENT_REQUEST_ERRORS as exc:
            if attempt >= attempts:
                raise
            delay = _retry_delay(attempt, retry_base_seconds, retry_max_seconds)
            logger(
                f"DeepSeek {label}: transient {type(exc).__name__} on attempt "
                f"{attempt}/{attempts}; retrying in {delay:g}s."
            )
            time.sleep(delay)
            continue

        if response.status_code not in RETRYABLE_HTTP_STATUSES or attempt >= attempts:
            return response

        delay = _retry_delay(
            attempt,
            retry_base_seconds,
            retry_max_seconds,
            response=response,
        )
        logger(
            f"DeepSeek {label}: retryable HTTP {response.status_code} on attempt "
            f"{attempt}/{attempts}; retrying in {delay:g}s."
        )
        time.sleep(delay)

    raise RuntimeError(f"DeepSeek {label}: retry loop ended unexpectedly")
