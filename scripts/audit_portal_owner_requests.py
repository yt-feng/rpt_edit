#!/usr/bin/env python3
"""Read private request snapshots and emit only a bounded, non-identifying inventory.

The interval is start-inclusive and end-exclusive. Dates in count summaries use
Asia/Shanghai. Request records retain their latest attempt, so this inventory is
not a history of every form submission or delivery attempt. No R2 writes occur.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import json
import os
import re
import sys
from typing import Any

REQUEST_PREFIXES = {
    "course_material_request": "_course-material-requests/v1/items/",
    "report_chat_request": "_report-chat-requests/v1/items/",
    "newsfeed_topic_request": "_newsfeed/topic-requests/v1/items/",
    "membership_request": "_membership-requests/v1/items/",
    "report_request": "_report-requests/v1/items/",
}
SHANGHAI = timezone(timedelta(hours=8))
MAX_RECORD_BYTES = 128_000
MAX_SCAN_KEYS = 50_000
STATUSES = frozenset({"pending", "sent", "failed", "fulfilled"})
PROVIDERS = frozenset({"brevo", "cloudflare"})
HASH_PATTERN = re.compile(r"^[a-f0-9]{64}$")
MATERIAL_PATTERN = re.compile(r"^maifu-(?:0[1-9]|1[0-9]|20)$")
EMAIL_PATTERN = re.compile(r"^[^\s@<>,;:\\]+@(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$")


class AuditError(RuntimeError):
    """Only constant configuration messages may be passed to this exception."""


@dataclass(repr=False)
class AuditCollection:
    summary: dict[str, Any]
    # Available for a provider audit in-process only; never serialize this object.
    provider_requests: list[dict[str, str]] = field(repr=False)

    def __repr__(self) -> str:
        return f"AuditCollection(summary={self.summary!r}, provider_requests=<withheld>)"


def parse_timestamp(value: Any) -> datetime:
    if not isinstance(value, str) or len(value) > 64:
        raise AuditError("A required audit timestamp is invalid.")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        raise AuditError("A required audit timestamp is invalid.") from None


def utc_text(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def normalized_email(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    email = value.strip().lower()
    return email if len(email) <= 254 and EMAIL_PATTERN.fullmatch(email) else ""


def read_record(client: Any, bucket: str, key: str) -> dict[str, Any]:
    body = None
    try:
        response = client.get_object(Bucket=bucket, Key=key)
        body = response["Body"]
        raw = body.read(MAX_RECORD_BYTES + 1)
        if len(raw) > MAX_RECORD_BYTES:
            raise ValueError
        record = json.loads(raw)
        if not isinstance(record, dict):
            raise ValueError
        return record
    except Exception:
        raise AuditError("A private request record could not be read.") from None
    finally:
        if body is not None and callable(getattr(body, "close", None)):
            try:
                body.close()
            except Exception:
                pass


def collect_owner_requests(
    s3_client: Any,
    bucket_name: str,
    start_iso: str,
    end_iso: str,
    owner_email: str = "",
    max_keys: int = 5000,
) -> AuditCollection:
    """Return safe summary plus private provider identifiers, without logging.

    max_keys bounds the total listing entries across all five request prefixes.
    A partial scan returns complete=False and constant reason codes, never an
    exception containing SDK responses, object keys, email addresses or records.
    """
    start, end = parse_timestamp(start_iso), parse_timestamp(end_iso)
    if start >= end:
        raise AuditError("Audit start must be earlier than audit end.")
    if isinstance(max_keys, bool) or not isinstance(max_keys, int) or not 1 <= max_keys <= MAX_SCAN_KEYS:
        raise AuditError("Audit key limit must be between 1 and 50000.")
    if not isinstance(bucket_name, str) or not bucket_name.strip():
        raise AuditError("Private R2 bucket configuration is missing.")
    owner = normalized_email(owner_email)
    if owner_email and not owner:
        raise AuditError("Configured owner mailbox is invalid.")

    issues: Counter[str] = Counter()
    type_complete: dict[str, bool] = {}
    rows: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    listed_count = read_count = duplicate_count = outside_count = 0
    for request_type, prefix in REQUEST_PREFIXES.items():
        complete = False
        continuation = ""
        seen_tokens: set[str] = set()
        while True:
            remaining = max_keys - listed_count
            if remaining <= 0:
                issues["scan_limit_reached"] += 1
                break
            options: dict[str, Any] = {"Bucket": bucket_name, "Prefix": prefix, "MaxKeys": min(1000, remaining)}
            if continuation:
                options["ContinuationToken"] = continuation
            try:
                response = s3_client.list_objects_v2(**options)
                entries = response.get("Contents", [])
                if not isinstance(entries, list) or len(entries) > options["MaxKeys"]:
                    raise ValueError
            except Exception:
                issues["listing_failed"] += 1
                break
            listed_count += len(entries)
            for entry in entries:
                key = entry.get("Key") if isinstance(entry, dict) else None
                suffix = key[len(prefix):-5] if isinstance(key, str) and key.startswith(prefix) and key.endswith(".json") else ""
                if not HASH_PATTERN.fullmatch(suffix) or key != f"{prefix}{suffix}.json":
                    issues["invalid_object_key"] += 1
                    continue
                if key in seen_keys:
                    duplicate_count += 1
                    continue
                seen_keys.add(key)
                try:
                    record = read_record(s3_client, bucket_name, key)
                    read_count += 1
                    if record.get("request_id") not in (None, "", suffix):
                        raise AuditError("Stored request identity is invalid.")
                    attempted = parse_timestamp(record.get("attempted_at"))
                except AuditError:
                    issues["unreadable_or_invalid_record"] += 1
                    continue
                if not start <= attempted < end:
                    outside_count += 1
                    continue
                sent_at = ""
                if record.get("sent_at"):
                    try:
                        sent_at = utc_text(parse_timestamp(record["sent_at"]))
                    except AuditError:
                        issues["invalid_sent_timestamp"] += 1
                raw_status = record.get("status")
                status = raw_status if isinstance(raw_status, str) and raw_status in STATUSES else "unknown"
                stored = normalized_email(record.get("notification_recipient"))
                recipient_state = (
                    "not_recorded" if not record.get("notification_recipient") else
                    "invalid" if not stored else
                    "owner_not_configured" if not owner else
                    "matches_owner" if stored == owner else "different_recipient"
                )
                safe: dict[str, Any] = {
                    "type": request_type,
                    "status": status,
                    "attempted_at": utc_text(attempted),
                    "sent_at": sent_at,
                    "stored_recipient_matches_owner": stored == owner if stored and owner else None,
                    "stored_recipient_state": recipient_state,
                }
                material = record.get("material_id")
                if request_type == "course_material_request" and isinstance(material, str) and MATERIAL_PATTERN.fullmatch(material):
                    safe["material_id"] = material
                provider = record.get("provider")
                provider = provider if isinstance(provider, str) and provider in PROVIDERS else "unknown"
                message_id = record.get("message_id")
                message_id = message_id if isinstance(message_id, str) and len(message_id) <= 500 else ""
                rows.append({"key": key, "attempted": attempted, "safe": safe, "provider": provider,
                             "message_id": message_id, "recipient": stored})
            if not response.get("IsTruncated"):
                complete = True
                break
            token = response.get("NextContinuationToken")
            if not isinstance(token, str) or not token or token in seen_tokens or not entries:
                issues["invalid_pagination"] += 1
                break
            seen_tokens.add(token)
            continuation = token
        type_complete[request_type] = complete

    rows.sort(key=lambda row: (row["attempted"], row["safe"]["type"], row["key"]))
    by_type = {name: {"total": 0, "by_status": {}} for name in REQUEST_PREFIXES}
    by_status: Counter[str] = Counter()
    by_day: dict[str, dict[str, Any]] = {}
    requests: list[dict[str, Any]] = []
    provider_requests: list[dict[str, str]] = []
    for index, row in enumerate(rows, 1):
        safe = {"alias": f"request-{index:04d}", **row["safe"]}
        requests.append(safe)
        request_type, status = safe["type"], safe["status"]
        by_type[request_type]["total"] += 1
        status_counts = by_type[request_type]["by_status"]
        status_counts[status] = status_counts.get(status, 0) + 1
        by_status[status] += 1
        day = row["attempted"].astimezone(SHANGHAI).date().isoformat()
        day_counts = by_day.setdefault(day, {"total": 0, "by_type": {}, "by_status": {}})
        day_counts["total"] += 1
        for category, value in (("by_type", request_type), ("by_status", status)):
            day_counts[category][value] = day_counts[category].get(value, 0) + 1
        if row["message_id"]:
            provider_requests.append({"alias": safe["alias"], "type": request_type, "provider": row["provider"],
                                      "message_id": row["message_id"], "notification_recipient": row["recipient"]})
    summary = {
        "schema_version": 1,
        "window": {"start_inclusive": utc_text(start), "end_exclusive": utc_text(end), "day_timezone": "Asia/Shanghai"},
        "count_basis": "unique_persisted_request_latest_attempt",
        "historical_attempts_available": False,
        "complete": all(type_complete.values()) and not issues,
        "scan": {"max_keys": max_keys, "listed_entries": listed_count, "unique_keys": len(seen_keys),
                 "records_read": read_count, "duplicate_entries": duplicate_count, "outside_window": outside_count,
                 "prefixes_complete": type_complete, "issues": dict(sorted(issues.items()))},
        "total_requests": len(requests),
        "by_type": by_type,
        "by_status": dict(sorted(by_status.items())),
        "by_day": dict(sorted(by_day.items())),
        "requests": requests,
    }
    return AuditCollection(summary, provider_requests)


def audit_owner_requests(
    s3_client: Any, bucket_name: str, start_iso: str, end_iso: str,
    owner_email: str = "", max_keys: int = 5000,
) -> dict[str, Any]:
    return collect_owner_requests(s3_client, bucket_name, start_iso, end_iso, owner_email, max_keys).summary


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value or value == "unconfigured":
        raise AuditError("Required private R2 configuration is missing.")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default="")
    parser.add_argument("--end", default=utc_text(datetime.now(timezone.utc)))
    parser.add_argument("--max-keys", type=int, default=5000)
    args = parser.parse_args()
    try:
        import boto3
        from botocore.config import Config
        client = boto3.client("s3", endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                              aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
                              aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"), region_name="auto",
                              config=Config(retries={"max_attempts": 0}, connect_timeout=15, read_timeout=25))
        start = args.start or utc_text(parse_timestamp(args.end) - timedelta(days=7))
        summary = audit_owner_requests(client, require_env("R2_BUCKET"), start, args.end,
                                       os.environ.get("OWNER_NOTIFICATION_EMAIL", ""), args.max_keys)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if summary["complete"] else 2
    except AuditError as error:
        print(str(error), file=sys.stderr)
        return 1
    except Exception:
        print("Owner request audit failed; private diagnostic details were withheld.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
