"""Shared bounded S3 transport for R2 release readers and publishers.

The SDK owns request retries. Only a successful GET whose response stream is
interrupted may start a fresh GET, and never after an SDK-retried request.
"""
from __future__ import annotations

import random
import time
from typing import Any

READ_RETRY_DELAYS = (2, 4, 8)
READ_RETRY_JITTER = 1
READ_CHUNK_BYTES = 1024 * 1024
_OBJECT_OPERATIONS = frozenset({
    "HeadObject", "GetObject", "PutObject", "CopyObject", "ListObjectsV2",
    "DeleteObject", "DeleteObjects", "CreateMultipartUpload", "UploadPart",
    "CompleteMultipartUpload", "AbortMultipartUpload",
})
_THROTTLE_MESSAGES = (
    "reduce your concurrent request rate for the same object",
    "reduce your rate of simultaneous reads on the same object",
)


class R2BodyError(RuntimeError):
    def __init__(self, category: str):
        self.category = category
        super().__init__(f"R2 response body {category}")


def normalize_r2_throttling(response: Any = None, operation: Any = None, **_kwargs: Any) -> None:
    """Let standard/adaptive SDK handlers recognize R2's throttle variants."""
    if getattr(operation, "name", None) not in _OBJECT_OPERATIONS:
        return
    if not isinstance(response, tuple) or len(response) != 2:
        return
    http_response, parsed = response
    if not isinstance(parsed, dict):
        return
    details = parsed.get("Error")
    if details is None:
        details = {}
    if not isinstance(details, dict):
        return
    status = getattr(http_response, "status_code", None)
    code = str(details.get("Code") or "").strip().lower()
    message = str(details.get("Message") or "").lower()
    if not (
        (status == 429 and code in {"", "429", "serviceunavailable"})
        or (status == 503 and code == "serviceunavailable"
            and any(text in message for text in _THROTTLE_MESSAGES))
    ):
        return
    # Named permission and validation errors are intentionally unchanged.
    details["Code"] = "SlowDown"
    parsed["Error"] = details


def install_r2_retry_handler(client: Any) -> Any:
    client.meta.events.register_first("needs-retry.s3", normalize_r2_throttling,
                                      unique_id="r2-object-throttling")
    client._r2_native_retry_policy = True
    return client


def native_retry_handler_installed(client: Any) -> bool:
    return getattr(client, "_r2_native_retry_policy", False) is True


def sdk_retry_count(response: Any) -> int | None:
    """None means absent, -1 means unreadable; neither proves a zero budget."""
    if not isinstance(response, dict):
        return None
    metadata = response.get("ResponseMetadata") or {}
    if not isinstance(metadata, dict):
        return -1
    if "RetryAttempts" not in metadata:
        return None
    value = metadata["RetryAttempts"]
    return value if type(value) is int and value >= 0 else -1


def request_retry_count(error: BaseException) -> int | None:
    """Find SDK authority even inside boto3's S3UploadFailedError wrapper."""
    pending, seen = [error], set()
    counts = []
    while pending:
        current = pending.pop()
        if id(current) in seen:
            continue
        seen.add(id(current))
        count = sdk_retry_count(getattr(current, "response", None))
        if count is not None:
            counts.append(count)
        pending.extend(item for item in (current.__cause__, current.__context__)
                       if isinstance(item, BaseException))
    if -1 in counts:
        return -1
    return max(counts) if counts else None


def retryable_stream_error(error: BaseException) -> bool:
    transport_errors: tuple[type[BaseException], ...] = (TimeoutError, ConnectionError)
    try:
        from botocore.exceptions import (
            ConnectionClosedError, ConnectTimeoutError, EndpointConnectionError,
            IncompleteReadError, ReadTimeoutError, ResponseStreamingError,
        )
    except ImportError:
        pass
    else:
        transport_errors += (ConnectionClosedError, ConnectTimeoutError, EndpointConnectionError,
                             IncompleteReadError, ReadTimeoutError, ResponseStreamingError)
    return isinstance(error, transport_errors)


def transient_request_error(error: BaseException) -> bool:
    """Identify a readback-worthy write outcome, including transfer wrappers."""
    pending, seen = [error], set()
    while pending:
        current = pending.pop()
        if id(current) in seen:
            continue
        seen.add(id(current))
        response = getattr(current, "response", None)
        if isinstance(response, dict):
            details, metadata = response.get("Error") or {}, response.get("ResponseMetadata") or {}
            code = str(details.get("Code") or "").lower() if isinstance(details, dict) else ""
            status = str(metadata.get("HTTPStatusCode") or "") if isinstance(metadata, dict) else ""
            if code in {"accessdenied", "invalidaccesskeyid", "signaturedoesnotmatch", "forbidden",
                        "404", "nosuchkey", "notfound", "nosuchbucket"} or status in {"401", "403", "404"}:
                return False
            if code in {"408", "429", "500", "502", "503", "504", "slowdown", "throttling",
                        "requestlimitexceeded", "serviceunavailable", "internalerror", "requesttimeout"} or status in {
                        "408", "429", "500", "502", "503", "504"}:
                return True
        if retryable_stream_error(current):
            return True
        pending.extend(item for item in (current.__cause__, current.__context__)
                       if isinstance(item, BaseException))
    return False


def read_r2_bytes(client: Any, bucket: str, key: str, *, maximum: int,
                  require_content_length: bool = False, **get_kwargs: Any) -> bytes:
    if type(maximum) is not int or maximum <= 0:
        raise ValueError("R2 response bound must be a positive integer")
    for attempt in range(len(READ_RETRY_DELAYS) + 1):
        response = None
        stream_started = False
        try:
            response = client.get_object(Bucket=bucket, Key=key, **get_kwargs)
            stream = response["Body"]
            try:
                declared = response.get("ContentLength")
                if (declared is None and require_content_length) or (
                    declared is not None and (type(declared) is not int or declared < 0
                                              or declared > maximum
                                              or (require_content_length and declared == 0))
                ):
                    raise R2BodyError("size_invalid")
                chunks, size = [], 0
                while True:
                    stream_started = True
                    chunk = stream.read(min(READ_CHUNK_BYTES, maximum - size + 1))
                    if not isinstance(chunk, bytes):
                        raise R2BodyError("size_invalid")
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > maximum:
                        raise R2BodyError("size_invalid")
                    chunks.append(chunk)
                if declared is not None and size != declared:
                    raise R2BodyError("size_mismatch")
                return b"".join(chunks)
            finally:
                close = getattr(stream, "close", None)
                if close is not None:
                    close()
        except Exception as error:
            if (attempt == len(READ_RETRY_DELAYS) or not stream_started
                or not retryable_stream_error(error)
                or request_retry_count(error) not in {None, 0}
                or sdk_retry_count(response) not in {None, 0}):
                raise
            time.sleep(READ_RETRY_DELAYS[attempt] + random.uniform(0, READ_RETRY_JITTER))
    raise AssertionError("Unreachable R2 read retry state")
