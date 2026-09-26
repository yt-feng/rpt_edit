#!/usr/bin/env python3
"""Fetch one release asset with bounded retries and atomic validation.

curl handles compressed transfer framing; Python controls the retry and acceptance
boundary. Diagnostics deliberately omit URLs, response bodies and curl stderr.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
from contextlib import ExitStack
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Callable
from urllib.parse import urlsplit


# https://curl.se/docs/manpage.html#EXIT-CODES
# Local IO, configuration and certificate failures are deliberately excluded.
TRANSIENT_CURL_CODES = {5, 6, 7, 8, 16, 18, 28, 35, 52, 55, 56, 92, 95, 96}


class FetchError(RuntimeError):
    def __init__(self, message: str, *, http_status: int = 0) -> None:
        super().__init__(message)
        self.http_status = http_status


@dataclass(frozen=True)
class FetchResult:
    http_status: int
    bytes_written: int
    attempts: int


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _retry_after(path: Path) -> float:
    """Use only the final header block, ignoring proxy/100 response headers."""
    value = ""
    for line in path.read_text(encoding="iso-8859-1").splitlines():
        if line.startswith("HTTP/"):
            value = ""
        elif line.lower().startswith("retry-after:"):
            value = line.partition(":")[2].strip()
    if re.fullmatch(r"[0-9]+", value):
        return float(value)
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return max(0.0, (parsed - datetime.now(timezone.utc)).total_seconds())
    except (ValueError, TypeError, OverflowError):
        return 0.0


def _reject_json_constant(value: str) -> None:
    raise ValueError("nonstandard JSON constant")


def _validation_error(
    path: Path, *, validate_json: bool, expected_bytes: int | None,
    expect_sha256: str | None, max_bytes: int | None,
) -> str | None:
    size = path.stat().st_size
    if max_bytes is not None and size > max_bytes:
        return "body exceeds maximum size"
    if size == 0:
        return "empty body"
    if expected_bytes is not None and size != expected_bytes:
        return "byte count mismatch"
    if expect_sha256 is not None and _sha256(path) != expect_sha256:
        return "SHA256 mismatch"
    if validate_json:
        try:
            with path.open("r", encoding="utf-8-sig") as stream:
                json.load(stream, parse_constant=_reject_json_constant)
        except (ValueError, UnicodeError, RecursionError):
            return "invalid JSON"
    return None


def fetch_release_asset(
    url: str, output: Path | str, *, label: str = "release asset",
    validate_json: bool = False, expected_file: Path | str | None = None,
    expect_sha256: str | None = None, expected_bytes: int | None = None,
    dump_header: Path | str | None = None, retry_404: bool = False,
    allow_missing: bool = False, max_bytes: int | None = None,
    attempts: int = 3, max_time: float = 120, connect_timeout: float = 30,
    max_total_time: float | None = None, retry_delay: float = 3,
    max_retry_delay: float = 30, logger: Callable[[str], None] | None = None,
) -> FetchResult:
    """Install a complete validated HTTP 200 response or leave output untouched.

    max_time applies to each attempt. max_total_time optionally limits the whole
    operation, including backoff. expected_file compares decoded body bytes with
    the local release artifact. Mismatches can be temporary during propagation,
    so retry them without ever accepting them or weakening validation.
    """
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _.:-]{0,95}", label):
        raise FetchError("invalid diagnostic label")
    try:
        parsed = urlsplit(url)
        valid_url = parsed.scheme in {"https", "http"} and bool(parsed.hostname)
    except ValueError:
        valid_url = False
    if not valid_url or any(character in url for character in "\r\n\0"):
        raise FetchError(f"{label}: expected an HTTP(S) URL")
    if not isinstance(attempts, int) or attempts < 1:
        raise FetchError(f"{label}: attempts must be a positive integer")
    for name, value in (("max-time", max_time), ("connect-timeout", connect_timeout)):
        if not math.isfinite(value) or value <= 0:
            raise FetchError(f"{label}: {name} must be positive and finite")
    for name, value in (("retry-delay", retry_delay), ("max-retry-delay", max_retry_delay)):
        if not math.isfinite(value) or value < 0:
            raise FetchError(f"{label}: {name} must be nonnegative and finite")
    if max_total_time is not None and (not math.isfinite(max_total_time) or max_total_time <= 0):
        raise FetchError(f"{label}: max-total-time must be positive and finite")
    if expected_bytes is not None and expected_bytes < 0:
        raise FetchError(f"{label}: expected-bytes must be nonnegative")
    if max_bytes is not None and max_bytes <= 0:
        raise FetchError(f"{label}: max-bytes must be positive")
    if expect_sha256 is not None:
        if not re.fullmatch(r"[0-9a-fA-F]{64}", expect_sha256):
            raise FetchError(f"{label}: expected SHA256 must contain 64 hex digits")
        expect_sha256 = expect_sha256.lower()
    if expected_file is not None:
        if expect_sha256 is not None or expected_bytes is not None:
            raise FetchError(f"{label}: expected-file cannot be combined with explicit digest or size")
        try:
            expected_bytes = Path(expected_file).stat().st_size
            expect_sha256 = _sha256(Path(expected_file))
        except OSError:
            raise FetchError(f"{label}: cannot read expected file") from None
    output = Path(output)
    header_output = Path(dump_header) if dump_header is not None else None
    if header_output is not None and output.resolve() == header_output.resolve():
        raise FetchError(f"{label}: output and header destination must differ")
    emit = logger or (lambda message: print(message, file=sys.stderr, flush=True))
    deadline = time.monotonic() + max_total_time if max_total_time is not None else None
    status = 0
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with ExitStack() as stack:
            body_dir = Path(stack.enter_context(tempfile.TemporaryDirectory(prefix=".fetch-", dir=output.parent)))
            body = body_dir / "body"
            headers = body_dir / "headers"
            if header_output is not None:
                header_output.parent.mkdir(parents=True, exist_ok=True)
                header_dir = Path(stack.enter_context(tempfile.TemporaryDirectory(prefix=".fetch-", dir=header_output.parent)))
                headers = header_dir / "headers"
            for attempt in range(1, attempts + 1):
                remaining = deadline - time.monotonic() if deadline is not None else math.inf
                if remaining <= 0:
                    raise FetchError(f"{label}: total time budget exhausted", http_status=status)
                attempt_time = min(max_time, remaining)
                # Reset each attempt; never resume a partial/stale object.
                body.write_bytes(b"")
                headers.write_bytes(b"")
                command = [
                    "curl", "--disable", "--silent", "--compressed", "--globoff",
                    "--proto", "=http,https", "--max-redirs", "0",
                    "--header", "Cache-Control: no-cache",
                    "--connect-timeout", str(min(connect_timeout, attempt_time)),
                    "--max-time", str(attempt_time), "--output", str(body),
                    "--dump-header", str(headers), "--write-out", "%{http_code}",
                    "--url", url,
                ]
                if max_bytes is not None:
                    command.extend(["--max-filesize", str(max_bytes)])
                emit(f"{label}: attempt {attempt}/{attempts} (timeout {attempt_time:g}s)")
                try:
                    process = subprocess.run(
                        command, capture_output=True, text=True,
                        timeout=min(attempt_time + 5, remaining), check=False,
                    )
                    status = int(process.stdout.strip()) if re.fullmatch(r"[0-9]{3}", process.stdout.strip()) else 0
                    curl_code = process.returncode
                except subprocess.TimeoutExpired:
                    status, curl_code = 0, 28
                if status == 404 and curl_code == 0 and allow_missing and (not retry_404 or attempt == attempts):
                    emit(f"{label}: optional asset absent (HTTP 404), attempt {attempt}/{attempts}")
                    return FetchResult(status, 0, attempt)
                # HTTP authorization failures remain permanent even if curl also
                # reports an interrupted transfer of the error response body.
                if status in {401, 403}:
                    retryable, reason = False, f"HTTP {status}"
                elif curl_code:
                    retryable = curl_code in TRANSIENT_CURL_CODES
                    reason = f"curl exit {curl_code}" + (f" (HTTP {status})" if status else "")
                elif status != 200:
                    retryable = status in {408, 425, 429} or 500 <= status <= 599 or (retry_404 and status == 404)
                    reason = f"HTTP {status:03d}"
                else:
                    error = _validation_error(
                        body, validate_json=validate_json, expected_bytes=expected_bytes,
                        expect_sha256=expect_sha256, max_bytes=max_bytes,
                    )
                    if error is None:
                        size = body.stat().st_size
                        os.replace(body, output)
                        if header_output is not None:
                            os.replace(headers, header_output)
                        emit(f"{label}: accepted HTTP 200, {size} bytes, attempt {attempt}/{attempts}")
                        return FetchResult(status, size, attempt)
                    retryable, reason = error != "body exceeds maximum size", error
                if not retryable or attempt == attempts:
                    raise FetchError(f"{label}: {reason}; failed after {attempt}/{attempts} attempts", http_status=status)
                delay = min(max_retry_delay, max(retry_delay * (2 ** (attempt - 1)), _retry_after(headers)))
                remaining = deadline - time.monotonic() if deadline is not None else math.inf
                if remaining <= delay:
                    raise FetchError(f"{label}: {reason}; total time budget exhausted", http_status=status)
                emit(f"{label}: {reason}; retrying in {delay:g}s")
                if delay:
                    time.sleep(delay)
    except OSError:
        raise FetchError(f"{label}: local file or curl execution error", http_status=status) from None
    raise AssertionError("unreachable")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--label", default="release asset")
    parser.add_argument("--json", dest="validate_json", action="store_true")
    parser.add_argument("--expected-file")
    parser.add_argument("--expect-sha256")
    parser.add_argument("--expected-bytes", type=int)
    parser.add_argument("--dump-header")
    parser.add_argument("--retry-404", action="store_true")
    parser.add_argument("--allow-missing", action="store_true", help="Allow a terminal HTTP 404 without changing output or headers")
    parser.add_argument("--max-bytes", type=int)
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--max-time", type=float, default=120)
    parser.add_argument("--connect-timeout", type=float, default=30)
    parser.add_argument("--max-total-time", type=float)
    parser.add_argument("--retry-delay", type=float, default=3)
    parser.add_argument("--max-retry-delay", type=float, default=30)
    parser.add_argument("--write-out-http-code", action="store_true")
    args = vars(parser.parse_args(argv))
    write_status = args.pop("write_out_http_code")
    try:
        result = fetch_release_asset(**args)
    except FetchError as exc:
        print(str(exc), file=sys.stderr)
        if write_status:
            print(f"{exc.http_status:03d}")
        return 1
    if write_status:
        print(f"{result.http_status:03d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
