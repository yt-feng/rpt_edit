#!/usr/bin/env python3
"""Baseline the complete public catalog, then generate starters for new reports.

The initial snapshot never invokes AI. Historical dates remain excluded even if
they are first discovered after activation. R2 conditional writes reserve every
attempt before the signed Worker request; pending/unknown outcomes are terminal.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import hmac
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

PREFIX = "_report-discussions/v1/"
STATE_KEY = PREFIX + "collector/catalog.json"
ELIGIBILITY_PREFIX = PREFIX + "eligibility/"
MAX_JSON_BYTES = 64 * 1024 * 1024
MAX_ROWS = 250000
MAX_BATCH = 20
BJT = timezone(timedelta(hours=8))
ID = re.compile(r"[a-f0-9]{16,64}\Z")
TERMINAL = frozenset({"ready", "pending", "unknown", "rejected", "failed", "not_authorized", "invalid_request"})
RETRYABLE = frozenset({"source_unavailable", "not_found", "provider_unavailable"})


class DiscussionError(Exception):
    """Only fixed error codes are emitted; upstream bodies and credentials stay private."""


def encoded(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    if len(raw) > MAX_JSON_BYTES:
        raise DiscussionError("state_too_large")
    return raw


def instant(value):
    try:
        result = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if result.tzinfo is None:
            raise ValueError()
        return result.astimezone(timezone.utc)
    except (ValueError, TypeError):
        raise DiscussionError("invalid_timestamp") from None


def iso(value):
    return value.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def report_date(row):
    value = str(row.get("date_folder", ""))
    if not re.fullmatch(r"\d{6}|\d{8}", value):
        return None
    try:
        return datetime.strptime(value, "%y%m%d" if len(value) == 6 else "%Y%m%d").date()
    except ValueError:
        return None


def validate_catalog(payload, *, minimum_items=100):
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise DiscussionError("catalog_shape")
    rows, count = payload.get("items"), payload.get("item_count")
    if (not isinstance(rows, list) or type(count) is not int or count != len(rows)
            or not minimum_items <= count <= MAX_ROWS
            or payload.get("complete") is False or payload.get("truncated") is True
            or payload.get("preview") is True or payload.get("total_item_count", count) != count):
        raise DiscussionError("catalog_incomplete")
    updated = instant(payload.get("updated_at_bjt"))
    by_id = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not ID.fullmatch(row["id"]):
            raise DiscussionError("catalog_identity")
        if row["id"] in by_id:
            raise DiscussionError("catalog_duplicate_identity")
        by_id[row["id"]] = row
    return by_id, updated


def validate_state(state):
    if (not isinstance(state, dict) or state.get("version") != 1 or state.get("source") != "catalog"
            or state.get("baseline_complete") is not True
            or not isinstance(state.get("seen_ids"), list) or not isinstance(state.get("queue"), dict)):
        raise DiscussionError("collector_state_invalid")
    activation = instant(state.get("activated_at"))
    instant(state.get("catalog_updated_at"))
    ids = state["seen_ids"]
    if (len(ids) > MAX_ROWS or any(not isinstance(item, str) or not ID.fullmatch(item) for item in ids)
            or len(set(ids)) != len(ids) or type(state.get("baseline_count")) is not int
            or not 1 <= state["baseline_count"] <= len(ids)):
        raise DiscussionError("collector_state_invalid")
    for report_id, row in state["queue"].items():
        if (report_id not in ids or not isinstance(row, dict) or row.get("status") not in TERMINAL | RETRYABLE | {"queued"}
                or instant(row.get("first_seen_at")) <= activation):
            raise DiscussionError("collector_state_invalid")
        if row.get("next_attempt_at"):
            instant(row["next_attempt_at"])
    return state


def eligibility_key(report_id):
    return ELIGIBILITY_PREFIX + hashlib.sha256(f"catalog:{report_id}".encode()).hexdigest() + ".json"


def collect(store, catalog, generate, *, now=None, max_batch=MAX_BATCH, minimum_items=100, elapsed=time.monotonic, max_seconds=1200):
    """All dependencies are injectable; tests do not perform network or model calls."""
    now = now or datetime.now(timezone.utc)
    started = elapsed()
    if not 1 <= max_batch <= MAX_BATCH:
        raise DiscussionError("invalid_batch_limit")
    rows, catalog_updated = validate_catalog(catalog, minimum_items=minimum_items)
    if catalog_updated > now + timedelta(minutes=5):
        raise DiscussionError("catalog_future_timestamp")
    previous, etag = store.get(STATE_KEY)
    if previous is None:
        baseline = {
            "version": 1, "source": "catalog", "baseline_complete": True,
            "activated_at": iso(now), "baseline_count": len(rows), "seen_ids": sorted(rows),
            "catalog_updated_at": iso(catalog_updated), "updated_at": iso(now), "queue": {},
        }
        store.put(STATE_KEY, baseline, etag=None)
        return {"ok": True, "baseline_created": True, "baseline_count": len(rows), "discovered": 0, "attempted": 0, "ready": 0, "pending": 0}

    state = deepcopy(validate_state(previous))
    activated = instant(state["activated_at"])
    if now <= activated:
        raise DiscussionError("clock_not_after_activation")
    if catalog_updated < instant(state["catalog_updated_at"]):
        raise DiscussionError("catalog_snapshot_regressed")
    unseen = set(rows) - set(state["seen_ids"])
    discovered = 0
    for report_id in sorted(unseen):
        published = report_date(rows[report_id])
        if published is None or not activated.astimezone(BJT).date() <= published <= now.astimezone(BJT).date():
            continue
        state["queue"][report_id] = {"first_seen_at": iso(now), "status": "queued", "last_attempt_at": "", "attempts": 0}
        discovered += 1
    state["seen_ids"] = sorted(set(state["seen_ids"]) | set(rows))
    if len(state["seen_ids"]) > MAX_ROWS:
        raise DiscussionError("collector_capacity")
    state["catalog_updated_at"] = iso(catalog_updated)
    state["updated_at"] = iso(now)
    etag = store.put(STATE_KEY, state, etag=etag)

    attempted = 0
    candidates = sorted(state["queue"], key=lambda report_id: (
        state["queue"][report_id].get("last_attempt_at", ""), state["queue"][report_id]["first_seen_at"], report_id))
    for report_id in candidates:
        row = state["queue"][report_id]
        if row["status"] in TERMINAL or report_id not in rows:
            continue
        if row.get("next_attempt_at") and instant(row["next_attempt_at"]) > now:
            continue
        if attempted >= max_batch or elapsed() - started >= max_seconds:
            break
        marker = {"version": 1, "source": "catalog", "report_id": report_id,
                  "first_seen_at": row["first_seen_at"], "activated_at": state["activated_at"]}
        marker_key = eligibility_key(report_id)
        existing, _ = store.get(marker_key)
        if existing is None:
            store.put(marker_key, marker, etag=None)
        elif existing != marker:
            raise DiscussionError("eligibility_conflict")
        row.update(status="pending", last_attempt_at=iso(now), attempts=int(row.get("attempts", 0)) + 1)
        row.pop("next_attempt_at", None)
        etag = store.put(STATE_KEY, state, etag=etag)
        attempted += 1
        try:
            outcome = generate({"source": "catalog", "report_id": report_id})
            status = outcome.get("status") if isinstance(outcome, dict) else "unknown"
        except Exception:
            status = "unknown"
        if status == "reserved":
            status = "pending"
        if status not in TERMINAL | RETRYABLE:
            status = "unknown"
        row["status"] = status
        if status in RETRYABLE:
            row["next_attempt_at"] = iso(now + timedelta(hours=1))
        etag = store.put(STATE_KEY, state, etag=etag)

    counts = {status: sum(row["status"] == status for row in state["queue"].values()) for status in TERMINAL | RETRYABLE | {"queued"}}
    return {"ok": True, "baseline_created": False, "baseline_count": state["baseline_count"],
            "discovered": discovered, "historical_excluded": len(unseen) - discovered, "attempted": attempted,
            "ready": counts["ready"], "pending": counts["pending"], "unknown": counts["unknown"],
            "waiting_for_source": sum(counts[status] for status in RETRYABLE), "queued": counts["queued"],
            "rejected": counts["rejected"], "blocked": counts["not_authorized"] + counts["invalid_request"] + counts["failed"]}


class R2Store:
    def __init__(self, client, bucket):
        self.client, self.bucket = client, bucket

    def get(self, key):
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
        except Exception as error:
            code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
            if code in {"NoSuchKey", "404"}:
                return None, None
            raise DiscussionError("storage_read_failed") from None
        try:
            body = response["Body"]
            try:
                raw = body.read(MAX_JSON_BYTES + 1)
            finally:
                body.close()
            if len(raw) > MAX_JSON_BYTES:
                raise ValueError()
            value = json.loads(raw)
            etag = response.get("ETag")
            if not isinstance(etag, str) or not etag:
                raise ValueError()
            return value, etag
        except Exception:
            raise DiscussionError("storage_object_invalid") from None

    def put(self, key, value, *, etag):
        try:
            self.client.put_object(Bucket=self.bucket, Key=key, Body=encoded(value),
                ContentType="application/json; charset=utf-8", CacheControl="private, no-store",
                **({"IfMatch": etag} if etag else {"IfNoneMatch": "*"}))
        except Exception as error:
            code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
            if code in {"PreconditionFailed", "412", "ConditionalRequestConflict", "409"}:
                raise DiscussionError("storage_write_conflict") from None
            # An unknown PUT outcome is read back, never blindly repeated.
            verified, current_etag = self.get(key)
            if verified == value:
                return current_etag
            raise DiscussionError("storage_write_conflict_or_unconfirmed") from None
        verified, current_etag = self.get(key)
        if verified != value:
            raise DiscussionError("storage_write_unverified")
        return current_etag


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *_args, **_kwargs):
        raise DiscussionError("unexpected_http_redirect")


def https_base(value):
    parsed = urllib.parse.urlsplit(str(value or "").strip())
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise DiscussionError("invalid_https_endpoint")
    return urllib.parse.urlunsplit(parsed).rstrip("/")


def http_json(url, *, body=None, headers=None, timeout=30, opener=None, max_bytes=MAX_JSON_BYTES, missing_ok=False):
    request_headers = {"Accept": "application/json", "User-Agent": "portal-report-discussion-starters/1.0"}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, data=body, headers=request_headers, method="POST" if body is not None else "GET")
    open_request = opener or urllib.request.build_opener(NoRedirect()).open
    try:
        response = open_request(request, timeout=timeout)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        status = response.status
        raw = response.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise DiscussionError("http_response_too_large")
    if status == 404 and missing_ok:
        return status, None
    try:
        result = json.loads(raw)
    except (ValueError, UnicodeDecodeError):
        raise DiscussionError("http_response_invalid") from None
    return status, result


def worker_ready(worker_base_url, report_id, *, opener=None):
    """Do not initialize or advance discovery before the new Worker is live."""
    if not isinstance(report_id, str) or not ID.fullmatch(report_id):
        raise DiscussionError("readiness_report_invalid")
    url = https_base(worker_base_url) + "/report-discussion?" + urllib.parse.urlencode({
        "source": "catalog", "report_id": report_id,
    })
    status, result = http_json(url, opener=opener, max_bytes=2 * 1024 * 1024, missing_ok=True)
    if status == 404:
        return False
    if (status != 200 or not isinstance(result, dict) or result.get("ok") is False
            or result.get("source") != "catalog" or result.get("report_id") != report_id
            or not isinstance(result.get("comments"), list)):
        raise DiscussionError("worker_readiness_unconfirmed")
    return True


def generate_http(worker_base_url, signing_key, payload, *, opener=None, timestamp=None):
    if not signing_key:
        raise DiscussionError("signing_key_missing")
    url = https_base(worker_base_url) + "/ops/report-discussions/generate"
    body = encoded(payload)
    timestamp_text = str(int(time.time() if timestamp is None else timestamp))
    signature = hmac.new(signing_key.encode(), timestamp_text.encode() + b"." + body, hashlib.sha256).hexdigest()
    status, result = http_json(url, body=body, headers={
        "Accept": "application/json", "Content-Type": "application/json",
        "X-Portal-Timestamp": timestamp_text, "X-Portal-Signature": "sha256=" + signature,
    }, timeout=90, opener=opener, max_bytes=16384)
    if not isinstance(result, dict):
        raise DiscussionError("generation_response_invalid")
    if status != 200 and result.get("status") not in {"provider_unavailable", "not_authorized", "invalid_request"}:
        return {"status": "unknown"}
    return {"status": result.get("status", "unknown")}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-batch", type=int, default=MAX_BATCH)
    args = parser.parse_args(argv)
    try:
        required = ("PORTAL_SITE_URL", "PORTAL_WORKER_URL", "OPS_ALERT_SIGNING_KEY", "R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")
        if any(not os.environ.get(name, "").strip() for name in required):
            raise DiscussionError("configuration_missing")
        if not re.fullmatch(r"[a-fA-F0-9]{32}", os.environ["R2_ACCOUNT_ID"]):
            raise DiscussionError("configuration_invalid")
        site = https_base(os.environ["PORTAL_SITE_URL"])
        status, catalog = http_json(site + "/data/catalog.json")
        if status != 200:
            raise DiscussionError("catalog_http_status")
        rows, _ = validate_catalog(catalog)
        worker_url = os.environ["PORTAL_WORKER_URL"].strip()
        if worker_url.startswith("/"):
            worker_url = site + worker_url
        if not worker_ready(worker_url, next(iter(rows))):
            print(json.dumps({"ok": True, "waiting_for_worker": True, "attempted": 0}, sort_keys=True))
            return 0
        import boto3
        from botocore.config import Config
        client = boto3.client("s3", endpoint_url=f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
            aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"], aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
            region_name="auto", config=Config(connect_timeout=10, read_timeout=20, retries={"total_max_attempts": 1, "mode": "standard"}))
        summary = collect(R2Store(client, os.environ["R2_BUCKET"]), catalog,
            lambda payload: generate_http(worker_url, os.environ["OPS_ALERT_SIGNING_KEY"], payload), max_batch=args.max_batch)
        print(json.dumps(summary, sort_keys=True))
        return 0
    except DiscussionError as error:
        print(json.dumps({"ok": False, "code": str(error)}), file=sys.stderr)
        return 1
    except Exception:
        print(json.dumps({"ok": False, "code": "collector_unavailable"}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
