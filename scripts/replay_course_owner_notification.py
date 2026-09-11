#!/usr/bin/env python3
"""Audit or replay one saved course request to the configured owner only.

No applicant session is created and the original request is never modified.
The send is reserved in private R2 before calling Brevo, without automatic
retries. A missing response remains ambiguous and must be audited, not resent.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any

REQUEST_PREFIX = "_course-material-requests/v1/items/"
REPLAY_PREFIX = "_ops/owner-notification-replay/v1/course/"
MAX_RECORDS = 200
MAX_JSON_BYTES = 2_000_000
HASH_RE = re.compile(r"^[a-f0-9]{64}$")
MATERIAL_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,79}$")
EMAIL_RE = re.compile(r"^[^\s@<>,;:\\]+@(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$")
EVENT_NAMES = frozenset({
    "requests", "request", "sent", "delivered", "deferred", "softBounces",
    "hardBounces", "soft_bounce", "hard_bounce", "blocked", "invalid",
    "error", "spam", "unsubscribed", "opened", "uniqueOpened", "clicks",
    "proxyOpen", "uniqueProxyOpen", "clicked", "loadedByProxy",
})


class ReplayError(RuntimeError):
    """Only constant, non-private text is passed to this exception."""


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value or value == "unconfigured":
        raise ReplayError(f"Required configuration is missing: {name}")
    return value


def normalized_email(value: str) -> str:
    value = str(value).strip().lower()
    if len(value) > 254 or not EMAIL_RE.fullmatch(value):
        raise ReplayError("Configured or saved email is invalid.")
    return value


def stamp(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError):
        raise ReplayError("A required timestamp is invalid.") from None


def message_key(value: str) -> str:
    return str(value).strip().strip("<>")


def json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")


def error_code(error: Exception) -> str:
    return str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))


def read_record(client: Any, bucket: str, key: str, optional: bool = False) -> dict | None:
    try:
        response = client.get_object(Bucket=bucket, Key=key)
        raw = response["Body"].read(MAX_JSON_BYTES + 1)
        if len(raw) > MAX_JSON_BYTES:
            raise ReplayError("Stored record exceeds the size limit.")
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise ReplayError("Stored record is not an object.")
        return value
    except ReplayError:
        raise
    except Exception as error:
        if optional and error_code(error) in {"NoSuchKey", "NotFound", "404"}:
            return None
        raise ReplayError("Unable to read a required private R2 record.") from None


def find_request(client: Any, bucket: str, request_id: str, material_id: str, attempted_at: str) -> dict:
    if request_id:
        if not HASH_RE.fullmatch(request_id):
            raise ReplayError("Request ID must be a 64-character lowercase hash.")
        keys = [f"{REQUEST_PREFIX}{request_id}.json"]
    else:
        if not MATERIAL_RE.fullmatch(material_id) or not attempted_at:
            raise ReplayError("Provide a request ID or material ID and exact attempted_at.")
        stamp(attempted_at)
        try:
            listed = client.list_objects_v2(Bucket=bucket, Prefix=REQUEST_PREFIX, MaxKeys=MAX_RECORDS + 1)
        except Exception:
            raise ReplayError("Unable to list private course request records.") from None
        keys = [row.get("Key", "") for row in listed.get("Contents", [])]
        if listed.get("IsTruncated") or len(keys) > MAX_RECORDS:
            raise ReplayError("Request scan limit exceeded; use an exact request ID.")
    matches = []
    for key in keys:
        suffix = key.removeprefix(REQUEST_PREFIX).removesuffix(".json")
        if key != f"{REQUEST_PREFIX}{suffix}.json" or not HASH_RE.fullmatch(suffix):
            raise ReplayError("Unexpected object in the private course request prefix.")
        row = read_record(client, bucket, key)
        if row.get("request_id") != suffix:
            raise ReplayError("Stored request identity does not match its object key.")
        if material_id and row.get("material_id") != material_id:
            continue
        if attempted_at and row.get("attempted_at") != attempted_at:
            continue
        matches.append(row)
    if len(matches) != 1:
        raise ReplayError("Selection must match exactly one saved course request.")
    row = matches[0]
    if not MATERIAL_RE.fullmatch(str(row.get("material_id", ""))):
        raise ReplayError("Saved material identity is invalid.")
    stamp(row.get("attempted_at", ""))
    normalized_email(row.get("requester_email", ""))
    original_id = str(row.get("message_id", ""))
    if not row.get("material_title") or not message_key(original_id):
        raise ReplayError("Saved request has no material title or original provider message ID.")
    if len(original_id) > 200 or any(ord(ch) < 32 for ch in original_id):
        raise ReplayError("Saved provider message ID is invalid.")
    if row.get("provider") != "brevo":
        raise ReplayError("The saved request was not sent through Brevo.")
    return row


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *_args: Any, **_kwargs: Any) -> None:
        return None


class Brevo:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.opener = urllib.request.build_opener(NoRedirect())

    def request(self, method: str, path: str, payload: dict | None = None, **query: Any) -> dict:
        url = "https://api.brevo.com/v3" + path
        if query:
            url += "?" + urllib.parse.urlencode(query)
        request = urllib.request.Request(
            url, method=method, data=json_bytes(payload) if payload is not None else None,
            headers={"api-key": self.api_key, "Accept": "application/json", "Content-Type": "application/json"},
        )
        try:
            with self.opener.open(request, timeout=25) as response:
                raw = response.read(MAX_JSON_BYTES + 1)
                if len(raw) > MAX_JSON_BYTES:
                    raise ReplayError("Brevo response exceeds the size limit.")
                result = json.loads(raw)
                if not isinstance(result, dict):
                    raise ReplayError("Brevo returned an invalid response.")
                return result
        except urllib.error.HTTPError as error:
            raise ReplayError(f"Brevo request returned HTTP {error.code}; provider response withheld.") from None
        except ReplayError:
            raise
        except Exception:
            raise ReplayError("Brevo request did not return a usable response; no send was retried.") from None

    def events(self, message_id: str = "", recipient: str = "", tag: str = "") -> list:
        query: dict[str, Any] = {"days": 90, "limit": 100, "sort": "asc"}
        if message_id:
            query["messageId"] = message_id
        if recipient:
            query["email"] = recipient
        if tag:
            query["tags"] = json.dumps([tag], separators=(",", ":"))
        result = self.request("GET", "/smtp/statistics/events", **query)
        events = result.get("events", [])
        if not isinstance(events, list) or len(events) >= 100:
            raise ReplayError("Provider event result is invalid or exceeds the audit bound.")
        filtered = []
        for event in events:
            if not isinstance(event, dict):
                raise ReplayError("Provider event is invalid.")
            if message_id and message_key(event.get("messageId", "")) != message_key(message_id):
                continue
            if recipient and str(event.get("email", "")).lower() != recipient:
                continue
            if tag and tag not in ([event.get("tag")] + (event.get("tags") if isinstance(event.get("tags"), list) else [])):
                continue
            filtered.append(event)
        return filtered

    def original_content(self, record: dict) -> dict:
        rows = self.request("GET", "/smtp/emails", messageId=record["message_id"], limit=10).get("transactionalEmails", [])
        matches = [row for row in rows if message_key(row.get("messageId", "")) == message_key(record["message_id"])]
        if len(matches) != 1:
            raise ReplayError("Original provider message must match exactly one email.")
        uuid = str(matches[0].get("uuid", ""))
        if not re.fullmatch(r"[A-Za-z0-9_-]{8,200}", uuid):
            raise ReplayError("Original provider message has an invalid content identifier.")
        content = self.request("GET", "/smtp/emails/" + uuid)
        subject, body = content.get("subject", ""), content.get("body", "")
        if not isinstance(subject, str) or not isinstance(body, str) or not subject or not body:
            raise ReplayError("Original provider content is unavailable.")
        if len(subject) > 200 or len(body) > 1_000_000:
            raise ReplayError("Original provider content exceeds the replay bound.")
        if content.get("attachmentCount", 0):
            raise ReplayError("Original message contains attachments and cannot use this notification-only replay.")
        if record["material_title"] not in html.unescape(subject) or normalized_email(record["requester_email"]) not in html.unescape(body).lower():
            raise ReplayError("Original provider content does not match the saved course request.")
        if abs((stamp(content.get("date", "")) - stamp(record["attempted_at"])).total_seconds()) > 300:
            raise ReplayError("Original provider content time does not match the saved request.")
        return {"subject": subject, "htmlContent": body}


def event_summary(events: list) -> dict:
    safe = []
    for row in events:
        name = str(row.get("event", ""))
        date = str(row.get("date", ""))
        try:
            timestamp = stamp(date).isoformat().replace("+00:00", "Z")
        except ReplayError:
            timestamp = ""
        safe.append({"event": name if name in EVENT_NAMES else "other", "date": timestamp})
    return {"event_count": len(safe), "delivered": any(row["event"] == "delivered" for row in safe), "events": safe}


def write_marker(client: Any, bucket: str, key: str, value: dict, reserve: bool = False) -> bool:
    kwargs = {"Bucket": bucket, "Key": key, "Body": json_bytes(value), "ContentType": "application/json; charset=utf-8", "CacheControl": "private, no-store"}
    if reserve:
        kwargs["IfNoneMatch"] = "*"
    try:
        client.put_object(**kwargs)
        return True
    except Exception as error:
        if reserve and error_code(error) in {"PreconditionFailed", "ConditionalRequestConflict", "412", "409"}:
            return False
        raise ReplayError("Unable to persist the private replay marker; no send was retried.") from None


def run(client: Any, bucket: str, provider: Brevo, *, mode: str, owner: str, sender: dict,
        request_id: str = "", material_id: str = "", attempted_at: str = "") -> dict:
    if mode not in {"audit", "resend"}:
        raise ReplayError("Unsupported operation.")
    owner = normalized_email(owner)
    record = find_request(client, bucket, request_id, material_id, attempted_at)
    if owner == normalized_email(record["requester_email"]):
        raise ReplayError("Owner destination must differ from the applicant address.")
    identity = hashlib.sha256((record["request_id"] + "|" + record["attempted_at"] + "|" + owner).encode()).hexdigest()
    marker_key = f"{REPLAY_PREFIX}{identity}.json"
    marker = read_record(client, bucket, marker_key, optional=True)
    known_states = {"sending", "accepted", "unknown_requires_audit"}
    marker_state = marker.get("state") if marker else None
    summary = {
        "mode": mode, "request_matched": True, "original_request_unchanged": True,
        "original_attempted_at": record["attempted_at"],
        "original_delivery": event_summary(provider.events(message_id=record["message_id"])),
        "replay_state": marker_state if marker_state in known_states else "unknown" if marker else "not_attempted",
        "send_attempted_this_run": False,
    }
    if marker:
        # Never automatically repeat an accepted, failed, or ambiguous POST.
        summary["repeat_suppressed"] = mode == "resend"
        replay_events = provider.events(
            message_id=str(marker.get("message_id", "")), recipient=owner,
            tag="" if marker.get("message_id") else f"owner-replay-{identity[:24]}",
        )
        summary["replay_delivery"] = event_summary(replay_events)
        if replay_events and marker_state in {"sending", "unknown_requires_audit"}:
            summary["replay_state"] = "accepted_recovered_from_provider_events"
        return summary
    if mode == "audit":
        return summary
    sender_email = normalized_email(sender.get("email", ""))
    sender_name = str(sender.get("name", "")).strip()
    if not sender_name or len(sender_name) > 100 or any(ord(ch) < 32 for ch in sender_name):
        raise ReplayError("Configured sender name is invalid.")
    content = provider.original_content(record)
    marker = {
        "schema_version": 1, "state": "sending", "created_at": now_text(),
        "request_id": record["request_id"], "original_attempted_at": record["attempted_at"],
        "original_message_id": record["message_id"], "recipient_hash": hashlib.sha256(owner.encode()).hexdigest(),
        "content_sha256": hashlib.sha256(json_bytes(content)).hexdigest(),
        "message_id": "",
    }
    if not write_marker(client, bucket, marker_key, marker, reserve=True):
        summary.update(replay_state="concurrent_operation_suppressed", repeat_suppressed=True)
        return summary
    summary["send_attempted_this_run"] = True
    try:
        result = provider.request("POST", "/smtp/email", {
            **content, "sender": {"email": sender_email, "name": sender_name},
            "to": [{"email": owner}],
            "tags": ["portal-course-material-request", f"owner-replay-{identity[:24]}"],
        })
        message_id = str(result.get("messageId", "")).strip()
        if not message_id or len(message_id) > 200:
            raise ReplayError("Brevo acceptance is ambiguous because no usable message ID was returned.")
    except Exception:
        marker.update(state="unknown_requires_audit", updated_at=now_text())
        write_marker(client, bucket, marker_key, marker)
        summary["replay_state"] = marker["state"]
        return summary
    marker.update(state="accepted", message_id=message_id, updated_at=now_text())
    write_marker(client, bucket, marker_key, marker)
    summary["replay_state"] = "accepted"
    summary["replay_delivery"] = event_summary(provider.events(message_id=message_id, recipient=owner))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("audit", "resend"), default="audit")
    parser.add_argument("--request-id", default="")
    parser.add_argument("--material-id", default="")
    parser.add_argument("--attempted-at", default="")
    parser.add_argument("--inventory-start", default="")
    parser.add_argument("--inventory-end", default="")
    args = parser.parse_args()
    try:
        import boto3
        from botocore.config import Config
        client = boto3.client("s3", endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                              aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
                              aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"), region_name="auto",
                              config=Config(retries={"max_attempts": 0}, connect_timeout=15, read_timeout=25))
        summary = run(client, require_env("R2_BUCKET"), Brevo(require_env("BREVO_API_KEY")), mode=args.mode,
                      owner=require_env("OWNER_NOTIFICATION_EMAIL"),
                      sender={"email": require_env("BREVO_SENDER_EMAIL"), "name": require_env("BREVO_SENDER_NAME")},
                      request_id=args.request_id, material_id=args.material_id, attempted_at=args.attempted_at)
        if args.mode == "audit":
            from audit_portal_owner_requests import audit_owner_requests
            summary["owner_request_inventory"] = audit_owner_requests(
                client, require_env("R2_BUCKET"), args.inventory_start or (datetime.now(timezone.utc) - timedelta(days=7)).isoformat(),
                args.inventory_end or now_text(), owner_email=require_env("OWNER_NOTIFICATION_EMAIL"),
            )
        rendered = json.dumps(summary, ensure_ascii=False, indent=2)
        print(rendered)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
                handle.write("```json\n" + rendered + "\n```\n")
        incomplete_inventory = summary.get("owner_request_inventory", {}).get("complete") is False
        unresolved_send = summary["replay_state"] in {"unknown_requires_audit", "sending", "unknown"}
        return 1 if incomplete_inventory or unresolved_send else 0
    except ReplayError as error:
        print(str(error), file=sys.stderr)
        return 1
    except Exception:
        print("Owner notification operation failed; private diagnostic details were withheld.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
