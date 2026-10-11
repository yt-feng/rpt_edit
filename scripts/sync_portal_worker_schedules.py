#!/usr/bin/env python3
"""Reconcile only a Worker's Cron Triggers after the deployed API passes smoke.

Versions upload/deploy do not apply triggers. Preserve unknown schedules and
merge only the complete four-entry, equivalent Newsfeed union. Never modify
routes/domains. PUT is not retried: reconcile an unknown outcome by GET first.
A failed verification restores the exact prior cron strings only while the
current list is one of the two known states. Concurrent unrecognized changes
are never overwritten. No credentials, script identifiers or API bodies log.
"""
from __future__ import annotations

from contextlib import contextmanager, suppress
import http.client
import json
import os
import re
import signal
import ssl
import time

API_HOST = "api.cloudflare.com"
REMINDER = "* 2-3 * * *"
NEWSFEED_PARTS = (
    "*/10 17-18 * * *", "*/10 23 * * *", "*/10 0-3 * * *", "*/10 5-6 * * *",
)
NEWSFEED_UNION = "*/10 0-3,5-6,17-18,23 * * *"
MAX_SCHEDULES = 5
MAX_BODY = 128 * 1024
READ_ATTEMPTS = 3
REQUEST_SECONDS = 15
ERRORS = frozenset({"configuration", "transport", "http_status", "api_shape", "schedule_limit",
    "concurrent_change", "verification_failed", "rollback_unverified", "local_failure"})


class ScheduleError(Exception):
    def __init__(self, code, *, rollback="not_needed"):
        self.code = code if code in ERRORS else "local_failure"
        self.rollback = rollback if rollback in {"not_needed", "verified", "unverified", "conflict"} else "unverified"
        super().__init__(self.code)


def validate_crons(rows):
    if not isinstance(rows, list) or len(rows) > 100:
        raise ScheduleError("api_shape")
    crons = []
    for row in rows:
        value = row.get("cron") if isinstance(row, dict) else None
        if (not isinstance(value, str) or not value or len(value) > 256
                or any(ord(char) < 32 or ord(char) > 126 for char in value)
                or len(value.split()) != 5 or value in crons):
            raise ScheduleError("api_shape")
        crons.append(value)
    return crons


def parse_schedules(payload):
    result = payload.get("result") if isinstance(payload, dict) and payload.get("success") is True else None
    return validate_crons(result.get("schedules") if isinstance(result, dict) else None)


def desired_schedules(previous):
    previous = validate_crons([{"cron": value} for value in previous])
    desired = list(previous)
    if all(value in previous for value in NEWSFEED_PARTS):
        desired = []
        for value in previous:
            if value in NEWSFEED_PARTS:
                if NEWSFEED_UNION not in desired and NEWSFEED_UNION not in previous:
                    desired.append(NEWSFEED_UNION)
            else:
                desired.append(value)
    if REMINDER not in desired:
        desired.append(REMINDER)
    if len(desired) > MAX_SCHEDULES:
        raise ScheduleError("schedule_limit")
    return desired


def same(left, right):
    # Ordering is not part of Cloudflare's schedule identity; cron strings are.
    return sorted(left) == sorted(right)


@contextmanager
def deadline():
    previous = signal.getsignal(signal.SIGALRM)
    def expired(_signum, _frame):
        raise ScheduleError("transport")
    signal.signal(signal.SIGALRM, expired)
    try:
        signal.setitimer(signal.ITIMER_REAL, REQUEST_SECONDS)
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


class ScheduleApi:
    def __init__(self, account_id, script_name, token, *, connection_factory=None):
        if (not re.fullmatch(r"[a-fA-F0-9]{32}", account_id or "")
                or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", script_name or "")
                or not isinstance(token, str) or not token or any(ord(c) < 32 for c in token)):
            raise ScheduleError("configuration")
        self.path = f"/client/v4/accounts/{account_id}/workers/scripts/{script_name}/schedules"
        self.token = token
        self.factory = connection_factory or http.client.HTTPSConnection

    def request(self, method, schedules=None):
        connection = response = None
        try:
            with deadline():
                connection = self.factory(API_HOST, timeout=10, context=ssl.create_default_context())
                body = None if method == "GET" else json.dumps([{"cron": cron} for cron in schedules]).encode("utf-8")
                # HTTPSConnection does not follow redirects or retry a request.
                connection.request(method, self.path, body=body, headers={
                    "Authorization": f"Bearer {self.token}", "Accept": "application/json",
                    "Content-Type": "application/json", "Accept-Encoding": "identity",
                })
                response = connection.getresponse()
                if not 200 <= response.status < 300:
                    raise ScheduleError("http_status")
                raw = response.read(MAX_BODY + 1)
                if len(raw) > MAX_BODY:
                    raise ScheduleError("api_shape")
                return parse_schedules(json.loads(raw))
        except ScheduleError:
            raise
        except Exception:
            raise ScheduleError("transport") from None
        finally:
            if response is not None:
                with suppress(Exception): response.close()
            if connection is not None:
                with suppress(Exception): connection.close()

    def get(self):
        return self.request("GET")

    def put(self, schedules):
        return self.request("PUT", schedules)


def verify(api, expected, alternative, sleep):
    """Require two consecutive exact reads, with at most three read attempts."""
    matches = 0
    for index in range(READ_ATTEMPTS):
        try:
            current = api.get()
        except Exception:
            matches = 0
        else:
            if same(current, expected):
                matches += 1
                if matches == 2:
                    return True
            elif same(current, alternative):
                matches = 0
            else:
                raise ScheduleError("concurrent_change", rollback="conflict")
        if index < READ_ATTEMPTS - 1:
            sleep(1)
    return False


def restore_previous(api, previous, desired, sleep):
    # Fresh observation before any rollback write. Do not restore over an
    # unrecognized list or an unavailable read, even if an earlier PUT acked.
    current = None
    for index in range(READ_ATTEMPTS):
        try:
            current = api.get()
            break
        except Exception:
            if index < READ_ATTEMPTS - 1: sleep(1)
    if current is None:
        raise ScheduleError("rollback_unverified", rollback="unverified")
    if not same(current, previous) and not same(current, desired):
        raise ScheduleError("concurrent_change", rollback="conflict")
    if same(current, desired):
        try:
            api.put(previous)
        except Exception:
            # Unknown rollback acknowledgement is also reconciled by GET only.
            pass
    if not verify(api, previous, desired, sleep):
        raise ScheduleError("rollback_unverified", rollback="unverified")
    return "verified"


def sync_schedules(api, *, sleep=time.sleep):
    previous = api.get()  # A failed initial read can never lead to a PUT.
    desired = desired_schedules(previous)
    if same(previous, desired):
        return {"ok": True, "changed": False, "schedule_count": len(previous), "rollback": "not_needed"}
    # Narrow the lost-update window; the API has no documented schedule CAS.
    if not same(api.get(), previous):
        raise ScheduleError("concurrent_change", rollback="conflict")
    try:
        api.put(desired)
    except Exception:
        # No blind mutation retry, including a 4xx or lost success response.
        pass
    try:
        if verify(api, desired, previous, sleep):
            return {"ok": True, "changed": True, "schedule_count": len(desired), "rollback": "not_needed"}
    except ScheduleError as error:
        if error.code == "concurrent_change":
            raise
    except Exception:
        # Even a local verification failure after PUT must reconcile/restore.
        pass
    restored = restore_previous(api, previous, desired, sleep)
    raise ScheduleError("verification_failed", rollback=restored)


def main():
    try:
        api = ScheduleApi(os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip(),
            os.environ.get("PORTAL_WORKER_SCRIPT_NAME", "").strip(),
            os.environ.get("CLOUDFLARE_API_TOKEN", "").strip())
        result = sync_schedules(api)
        code = 0
    except ScheduleError as error:
        result = {"ok": False, "error": error.code, "rollback": error.rollback}
        code = 1
    except Exception:
        result = {"ok": False, "error": "local_failure", "rollback": "unverified"}
        code = 1
    print(json.dumps(result, sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
