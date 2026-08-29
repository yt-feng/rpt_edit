#!/usr/bin/env python3
"""Send one signed operations alert through the Portal Suite Newsfeed mail worker."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_WORKER_BASE_URL = "https://portal.example.invalid/api"
ALERT_PATH = "/ops/alerts/email"
DEFAULT_DEDUPE_HOURS = 24
MIN_DEDUPE_HOURS = 1
MAX_DEDUPE_HOURS = 720


def normalize_worker_url(value: str) -> str:
    base = (value or "").strip() or DEFAULT_WORKER_BASE_URL
    if base.startswith("/"):
        base = f"https://portal.example.invalid{base}"
    parsed = urllib.parse.urlparse(base)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Portal Suite Worker URL must be an absolute HTTP(S) URL or a /api path")
    return f"{base.rstrip('/')}{ALERT_PATH}"


def dedupe_hours_value(value: int | str) -> int:
    hours = int(value)
    if not MIN_DEDUPE_HOURS <= hours <= MAX_DEDUPE_HOURS:
        raise ValueError(
            f"dedupe hours must be between {MIN_DEDUPE_HOURS} and {MAX_DEDUPE_HOURS}"
        )
    return hours


def payload_bytes(
    subject: str,
    text: str,
    dedupe_key: str,
    severity: str,
    dedupe_hours: int = DEFAULT_DEDUPE_HOURS,
) -> bytes:
    payload = {
        "subject": subject.strip(),
        "text": text.strip(),
        "dedupe_key": dedupe_key.strip(),
        "dedupe_window_hours": dedupe_hours_value(dedupe_hours),
        "severity": severity.strip().lower(),
    }
    if not payload["subject"] or not payload["text"] or not payload["dedupe_key"]:
        raise ValueError("subject, text, and dedupe_key are required")
    return json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def signed_headers(signing_key: str, body: bytes, timestamp: int) -> dict[str, str]:
    if not signing_key:
        raise ValueError("OPS_ALERT_SIGNING_KEY is not configured")
    timestamp_text = str(int(timestamp))
    message = timestamp_text.encode("ascii") + b"." + body
    signature = hmac.new(signing_key.encode("utf-8"), message, hashlib.sha256).hexdigest()
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "rpt-edit-ops-alert/1.0",
        "X-Portal-Timestamp": timestamp_text,
        "X-Portal-Signature": f"sha256={signature}",
    }


def send_alert(
    *,
    worker_base_url: str,
    signing_key: str,
    subject: str,
    text: str,
    dedupe_key: str,
    severity: str = "warning",
    dedupe_hours: int = DEFAULT_DEDUPE_HOURS,
    attempts: int = 3,
    timeout: float = 20,
) -> dict[str, Any]:
    url = normalize_worker_url(worker_base_url)
    body = payload_bytes(subject, text, dedupe_key, severity, dedupe_hours)
    last_error: Exception | None = None
    for attempt in range(1, max(1, attempts) + 1):
        request = urllib.request.Request(
            url,
            data=body,
            headers=signed_headers(signing_key, body, int(time.time())),
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                response_body = response.read().decode("utf-8", errors="replace")
                result = json.loads(response_body or "{}")
                if not result.get("sent"):
                    raise RuntimeError(result.get("detail") or "Portal Suite Worker did not confirm the alert")
                return result
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")[:500]
            last_error = RuntimeError(f"Portal Suite Worker returned HTTP {error.code}: {detail}")
            if error.code not in {408, 425, 429} and error.code < 500:
                break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as error:
            last_error = error
        if attempt < max(1, attempts):
            time.sleep(min(2 ** (attempt - 1), 4))
    raise RuntimeError(f"Could not send Portal Suite operations alert: {last_error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--worker-base-url",
        default=os.environ.get("PORTAL_WORKER_URL", DEFAULT_WORKER_BASE_URL),
    )
    parser.add_argument("--subject", required=True)
    parser.add_argument("--text")
    parser.add_argument("--text-file", type=Path)
    parser.add_argument("--dedupe-key", required=True)
    parser.add_argument(
        "--dedupe-hours",
        type=dedupe_hours_value,
        default=DEFAULT_DEDUPE_HOURS,
        metavar="HOURS",
        help=(
            f"Suppress repeats for {MIN_DEDUPE_HOURS}-{MAX_DEDUPE_HOURS} hours "
            "(default: %(default)s)."
        ),
    )
    parser.add_argument("--severity", choices=("info", "warning", "critical"), default="warning")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.text or ""
    if args.text_file:
        text = args.text_file.read_text(encoding="utf-8")
    signing_key = os.environ.get("OPS_ALERT_SIGNING_KEY", "").strip()
    result = send_alert(
        worker_base_url=args.worker_base_url,
        signing_key=signing_key,
        subject=args.subject,
        text=text,
        dedupe_key=args.dedupe_key,
        severity=args.severity,
        dedupe_hours=args.dedupe_hours,
        attempts=args.attempts,
        timeout=args.timeout,
    )
    status = "deduplicated" if result.get("deduplicated") else "sent"
    print(f"Portal Suite operations alert {status} via {result.get('provider') or 'configured provider'}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - keep workflow error concise.
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
