#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import sys
import types
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_portal_owner_requests as audit

START = "2026-09-03T16:00:00Z"
END = "2026-09-11T04:00:00Z"
OWNER = "owner-direct@example.invalid"


class MemoryClient:
    def __init__(self, page_size=1000):
        self.objects = {}
        self.calls = []
        self.page_size = page_size
        self.fail_list = set()
        self.fail_get = set()

    def seed(self, kind, number, **updates):
        key = audit.REQUEST_PREFIXES[kind] + f"{number:064x}.json"
        row = {
            "request_id": f"{number:064x}", "attempted_at": "2026-09-10T18:29:00Z",
            "created_at": "2026-01-01T00:00:00Z", "sent_at": "2026-09-10T18:29:01Z", "status": "sent",
            "provider": "brevo", "message_id": f"<original-provider-{number}@example.invalid>",
            "requester_email": "reader-private@example.invalid", "requester_username": "PRIVATE-NAME",
            "material_title": "PRIVATE-TITLE", "note": "PRIVATE-NOTE",
            **updates,
        }
        self.objects[key] = json.dumps(row).encode()
        return key

    def list_objects_v2(self, **kwargs):
        self.calls.append(("list", kwargs))
        if kwargs["Prefix"] in self.fail_list:
            raise RuntimeError("PRIVATE-NAME reader-private@example.invalid PRIVATE-TOKEN")
        keys = sorted(key for key in self.objects if key.startswith(kwargs["Prefix"]))
        start = int(kwargs.get("ContinuationToken", "0"))
        size = min(kwargs["MaxKeys"], self.page_size)
        selected = keys[start:start + size]
        truncated = start + size < len(keys)
        return {"Contents": [{"Key": key} for key in selected], "IsTruncated": truncated,
                **({"NextContinuationToken": str(start + size)} if truncated else {})}

    def get_object(self, **kwargs):
        self.calls.append(("get", kwargs))
        if kwargs["Key"] in self.fail_get:
            raise RuntimeError("PRIVATE-TOKEN reader-private@example.invalid")
        return {"Body": io.BytesIO(self.objects[kwargs["Key"]])}


class OwnerRequestAuditTests(unittest.TestCase):
    def test_all_five_prefixes_match_worker_and_count_latest_unique_requests_by_shanghai_day(self):
        worker = (Path(__file__).resolve().parents[1] / "workers/portal-suite-worker/src/index.js").read_text()
        client = MemoryClient()
        for index, kind in enumerate(audit.REQUEST_PREFIXES, 1):
            self.assertIn('"' + audit.REQUEST_PREFIXES[kind].removesuffix("/items/") + '"', worker)
            client.seed(kind, index, material_id="maifu-02", status="failed" if index == 2 else "sent",
                        notification_recipient=OWNER if index == 1 else "legacy@example.invalid")
        result = audit.audit_owner_requests(client, "private-bucket", START, END, OWNER)
        self.assertTrue(result["complete"])
        self.assertEqual(result["total_requests"], 5)
        self.assertEqual(result["by_status"], {"failed": 1, "sent": 4})
        self.assertEqual(result["by_day"]["2026-09-11"]["total"], 5)
        self.assertTrue(all(value["total"] == 1 for value in result["by_type"].values()))
        self.assertEqual([row["alias"] for row in result["requests"]], [f"request-{n:04d}" for n in range(1, 6)])
        course = next(row for row in result["requests"] if row["type"] == "course_material_request")
        self.assertEqual(course["material_id"], "maifu-02")
        self.assertTrue(course["stored_recipient_matches_owner"])
        self.assertEqual(course["stored_recipient_state"], "matches_owner")
        self.assertTrue(all("material_id" not in row for row in result["requests"] if row is not course))
        self.assertFalse(result["historical_attempts_available"])
        self.assertEqual(set(kind for kind, _ in client.calls), {"get", "list"})

    def test_interval_is_start_inclusive_end_exclusive_and_uses_latest_attempt(self):
        client = MemoryClient()
        kind = "report_request"
        client.seed(kind, 1, attempted_at="2026-09-04T00:00:00+08:00", request_id=None)
        client.seed(kind, 2, attempted_at="2026-09-03T15:59:59Z")
        client.seed(kind, 3, attempted_at=END)
        client.seed(kind, 4, attempted_at="2026-09-11T03:59:59Z", created_at="2025-01-01T00:00:00Z")
        result = audit.audit_owner_requests(client, "private-bucket", START, END)
        self.assertTrue(result["complete"])
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["scan"]["outside_window"], 2)
        self.assertEqual(list(result["by_day"]), ["2026-09-04", "2026-09-11"])
        self.assertEqual(result["requests"][0]["attempted_at"], START)
        self.assertIsNone(result["requests"][0]["stored_recipient_matches_owner"])
        self.assertEqual(result["requests"][0]["stored_recipient_state"], "not_recorded")

    def test_pagination_and_repeated_keys_count_each_persisted_request_once(self):
        client = MemoryClient(page_size=1)
        keys = [client.seed("course_material_request", number) for number in (1, 2, 3)]
        original = client.list_objects_v2
        def listing(**kwargs):
            if kwargs["Prefix"] == audit.REQUEST_PREFIXES["course_material_request"] and kwargs.get("ContinuationToken") == "1":
                client.calls.append(("list", kwargs))
                return {"Contents": [{"Key": keys[0]}, {"Key": keys[1]}], "IsTruncated": True, "NextContinuationToken": "2"}
            return original(**kwargs)
        client.list_objects_v2 = listing
        result = audit.audit_owner_requests(client, "private-bucket", START, END)
        self.assertTrue(result["complete"])
        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["scan"]["duplicate_entries"], 1)
        self.assertEqual(len([call for call in client.calls if call[0] == "get"]), 3)
        self.assertTrue(any("ContinuationToken" in args for kind, args in client.calls if kind == "list"))

    def test_global_key_limit_reports_incomplete_instead_of_claiming_empty_remaining_types(self):
        client = MemoryClient(page_size=1)
        for number in (1, 2, 3):
            client.seed("course_material_request", number)
        result = audit.audit_owner_requests(client, "private-bucket", START, END, max_keys=2)
        self.assertFalse(result["complete"])
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["scan"]["listed_entries"], 2)
        self.assertGreater(result["scan"]["issues"]["scan_limit_reached"], 0)
        self.assertFalse(any(result["scan"]["prefixes_complete"].values()))
        self.assertEqual(len([call for call in client.calls if call[0] == "get"]), 2)

    def test_invalid_pagination_and_sdk_errors_are_bounded_and_do_not_leak(self):
        client = MemoryClient()
        key = client.seed("course_material_request", 1)
        original = client.list_objects_v2
        def listing(**kwargs):
            if kwargs["Prefix"] == audit.REQUEST_PREFIXES["course_material_request"]:
                return {"Contents": [{"Key": key}], "IsTruncated": True, "NextContinuationToken": "same-private-token"}
            return original(**kwargs)
        client.list_objects_v2 = listing
        client.fail_list.add(audit.REQUEST_PREFIXES["report_request"])
        result = audit.audit_owner_requests(client, "private-bucket", START, END)
        self.assertFalse(result["complete"])
        self.assertEqual(result["scan"]["issues"], {"invalid_pagination": 1, "listing_failed": 1})
        self.assertEqual(result["total_requests"], 1)
        self.assertNotIn("private-token", json.dumps(result))
        self.assertNotIn("PRIVATE-TOKEN", json.dumps(result))

    def test_corrupt_oversized_and_mismatched_records_are_reported_without_exposing_content(self):
        client = MemoryClient()
        kind = "course_material_request"
        corrupt = client.seed(kind, 1)
        client.objects[corrupt] = b"reader-private@example.invalid"
        oversized = client.seed(kind, 2)
        client.objects[oversized] = b"x" * (audit.MAX_RECORD_BYTES + 1)
        client.seed(kind, 3, request_id="invalid-private-identifier")
        client.seed(kind, 4, attempted_at="private-invalid-date")
        client.seed(kind, 5, material_id="private-material-id", status="private-state", sent_at="private-sent-date")
        client.objects[audit.REQUEST_PREFIXES[kind] + "PRIVATE-NAME.json"] = b"{}"
        result = audit.audit_owner_requests(client, "private-bucket", START, END)
        self.assertFalse(result["complete"])
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["scan"]["issues"], {"invalid_object_key": 1, "invalid_sent_timestamp": 1, "unreadable_or_invalid_record": 4})
        self.assertEqual(result["requests"][0]["status"], "unknown")
        self.assertNotIn("material_id", result["requests"][0])
        self.assertNotIn("private-", json.dumps(result))
        self.assertNotIn("PRIVATE-NAME", json.dumps(result))

    def test_private_provider_identifiers_remain_available_only_in_process(self):
        client = MemoryClient()
        key = client.seed("course_material_request", 1, notification_recipient=OWNER)
        result = audit.collect_owner_requests(client, "private-bucket", START, END, OWNER)
        private = result.provider_requests[0]
        self.assertEqual(private["message_id"], "<original-provider-1@example.invalid>")
        self.assertEqual(private["notification_recipient"], OWNER)
        self.assertEqual(private["alias"], result.summary["requests"][0]["alias"])
        rendered = json.dumps(result.summary) + repr(result)
        for value in [key, "original-provider-1", OWNER, "reader-private@example.invalid", "PRIVATE-NAME", "PRIVATE-TITLE", "PRIVATE-NOTE", "00000000000000000000"]:
            self.assertNotIn(value, rendered)

    def test_invalid_configuration_fails_before_any_r2_access(self):
        client = MemoryClient()
        for args in [
            ("invalid-private-date", END, "", 5000),
            (START, "2026-09-11", "", 5000),
            (END, START, "", 5000),
            (START, END, "owner@example.invalid,other@example.invalid", 5000),
            (START, END, "", 0),
            (START, END, "", True),
        ]:
            with self.assertRaises(audit.AuditError) as error:
                audit.audit_owner_requests(client, "private-bucket", *args)
            self.assertNotIn("invalid-private-date", str(error.exception))
            self.assertNotIn("owner@example.invalid", str(error.exception))
        self.assertEqual(client.calls, [])

    def test_cli_prints_only_safe_summary_and_incomplete_scan_exits_nonzero(self):
        client = MemoryClient()
        client.seed("report_request", 1)
        boto3 = types.SimpleNamespace(client=lambda *_args, **_kwargs: client)
        config_module = types.SimpleNamespace(Config=lambda **kwargs: kwargs)
        environment = {"R2_ACCOUNT_ID": "private-account", "R2_ACCESS_KEY_ID": "private-key", "R2_SECRET_ACCESS_KEY": "private-secret",
                       "R2_BUCKET": "private-bucket", "OWNER_NOTIFICATION_EMAIL": OWNER}
        with mock.patch.dict(sys.modules, {"boto3": boto3, "botocore.config": config_module}), mock.patch.dict(audit.os.environ, environment), mock.patch.object(sys, "argv", ["audit", "--start", START, "--end", END]):
            with contextlib.redirect_stdout(output := io.StringIO()), contextlib.redirect_stderr(errors := io.StringIO()):
                self.assertEqual(audit.main(), 0)
            rendered = output.getvalue() + errors.getvalue()
            self.assertEqual(json.loads(output.getvalue())["total_requests"], 1)
            for value in ["private-account", "private-key", "private-secret", "private-bucket", "original-provider-1", "PRIVATE-NAME", OWNER]:
                self.assertNotIn(value, rendered)
            client.fail_list.add(audit.REQUEST_PREFIXES["report_request"])
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(audit.main(), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
