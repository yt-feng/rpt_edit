"""Synthetic tests only: no credentials, network or production records."""

import copy
from io import BytesIO, StringIO
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import summarize_membership_request_snapshots as subject


START = "2026-09-27"
END = "2026-10-10"


def object_name(index):
    return f"{subject.PREFIX}{index:064x}.json"


def record(**changes):
    value = {
        "version": 1, "request_kind": "membership", "status": "sent",
        "created_at": "2026-09-28T01:00:00Z", "attempted_at": "2026-09-28T01:00:00Z",
        "sent_at": "2026-09-28T01:00:01Z", "attempt_count": 1,
        "request_id": "synthetic-private-record-id", "requester_email": "synthetic@example.invalid",
        "contact_value": "synthetic-contact-do-not-export", "note": "synthetic-private-note",
        "page_path": "/synthetic-private-page", "last_error": "synthetic-private-provider-error",
    }
    value.update(changes)
    return value


class FakeClient:
    def __init__(self, records=None, pages=None, failures=(), list_failure=False):
        self.records = records or {}
        self.pages = pages
        self.failures = set(failures)
        self.list_failure = list_failure
        self.calls = []
        self.bodies = []

    def list_objects_v2(self, **options):
        self.calls.append(("list", options))
        assert options["Prefix"] == subject.PREFIX
        assert 1 <= options["MaxKeys"] <= 1000
        if self.list_failure:
            raise RuntimeError("synthetic-private-listing-error")
        if self.pages is not None:
            index = int(options.get("ContinuationToken", "0"))
            return self.pages[index]
        names = list(self.records)
        start = int(options.get("ContinuationToken", "0"))
        stop = min(start + options["MaxKeys"], len(names))
        response = {"Contents": [{"Key": name} for name in names[start:stop]], "IsTruncated": stop < len(names)}
        if response["IsTruncated"]:
            response["NextContinuationToken"] = str(stop)
        return response

    def get_object(self, **options):
        self.calls.append(("get", options))
        name = options["Key"]
        if name in self.failures:
            raise RuntimeError("synthetic-private-read-error")
        payload = self.records[name]
        raw = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        body = BytesIO(raw)
        self.bodies.append(body)
        return {"Body": body, "ContentLength": len(raw)}


class MembershipSnapshotTests(unittest.TestCase):
    def summarize(self, client, **options):
        return subject.summarize(client, "synthetic-private-bucket", START, END, **options)

    def assert_partial(self, report):
        self.assertFalse(report["complete"])
        self.assertEqual(report["coverage"], "partial")
        for metric in report["windows"].values():
            self.assertIsNone(metric["snapshot_count"])
            self.assertTrue(all(value is None for value in metric["by_request_kind"].values()))
            self.assertTrue(all(value is None for value in metric["by_latest_status"].values()))
        subject.assert_aggregate_privacy(report)

    def test_three_windows_use_first_creation_and_latest_retained_attempt_separately(self):
        client = FakeClient({
            object_name(1): record(created_at="2026-09-10T00:00:00Z", attempt_count=7),
            object_name(2): record(request_kind="access", created_at="2026-09-30T00:00:00Z",
                                   attempted_at="2026-10-11T00:00:00Z", sent_at="2026-10-11T00:00:01Z"),
            object_name(3): record(request_kind="support", status="failed", sent_at=""),
            object_name(4): record(request_kind="privacy", status="pending", sent_at=""),
            object_name(5): record(request_kind="refund"),
        })
        report = self.summarize(client)
        self.assertTrue(report["complete"])
        windows = report["windows"]
        self.assertEqual([windows[name]["snapshot_count"] for name in subject.WINDOWS], [4, 4, 2])
        self.assertEqual(windows["created_window"]["by_request_kind"]["membership"], 0)
        self.assertEqual(windows["latest_attempt_window"]["by_request_kind"]["membership"], 1)
        self.assertEqual(windows["retained_sent_window"]["by_request_kind"]["refund"], 1)
        self.assertEqual(windows["latest_attempt_window"]["by_latest_status"], {"pending": 1, "sent": 2, "failed": 1})
        self.assertTrue(all(body.closed for body in client.bodies))
        self.assertEqual({name for name, _ in client.calls}, {"get", "list"})

    def test_beijing_dates_are_inclusive_with_end_exclusive_utc(self):
        points = ("2026-09-26T15:59:59Z", "2026-09-26T16:00:00Z",
                  "2026-10-10T15:59:59Z", "2026-10-10T16:00:00Z")
        client = FakeClient({object_name(i): record(created_at=p, attempted_at=p, sent_at=p)
                             for i, p in enumerate(points)})
        report = self.summarize(client)
        self.assertEqual(report["windows"]["created_window"]["snapshot_count"], 2)
        self.assertEqual(report["scan"]["outside_all_windows"], 2)
        self.assertEqual(report["window"]["start_utc_inclusive"], "2026-09-26T16:00:00Z")
        self.assertEqual(report["window"]["end_utc_exclusive"], "2026-10-10T16:00:00Z")

    def test_complete_empty_prefix_is_zero(self):
        report = self.summarize(FakeClient())
        self.assertTrue(report["complete"])
        self.assertEqual(report["windows"]["created_window"]["snapshot_count"], 0)

    def test_object_cap_is_partial_even_after_valid_objects(self):
        report = self.summarize(FakeClient({object_name(i): record() for i in range(3)}), max_objects=2)
        self.assert_partial(report)
        self.assertEqual(report["scan"]["valid_records"], 2)
        self.assertTrue(report["scan"]["object_limit_reached"])

    def test_exact_object_cap_with_complete_listing_is_complete(self):
        report = self.summarize(FakeClient({object_name(i): record() for i in range(2)}), max_objects=2)
        self.assertTrue(report["complete"])
        self.assertFalse(report["scan"]["object_limit_reached"])

    def test_pagination_and_duplicate_detection(self):
        pages = [
            {"Contents": [{"Key": object_name(1)}], "IsTruncated": True, "NextContinuationToken": "1"},
            {"Contents": [{"Key": object_name(1)}], "IsTruncated": False},
        ]
        client = FakeClient({object_name(1): record()}, pages=pages)
        report = self.summarize(client)
        self.assert_partial(report)
        self.assertEqual(report["scan"]["duplicate_objects"], 1)
        self.assertEqual(len([call for call in client.calls if call[0] == "get"]), 1)

    def test_complete_multi_page_inventory(self):
        pages = [
            {"Contents": [{"Key": object_name(1)}], "IsTruncated": True, "NextContinuationToken": "1"},
            {"Contents": [{"Key": object_name(2)}], "IsTruncated": False},
        ]
        report = self.summarize(FakeClient({object_name(i): record() for i in (1, 2)}, pages=pages))
        self.assertTrue(report["complete"])
        self.assertEqual(report["windows"]["created_window"]["snapshot_count"], 2)

    def test_repeated_or_missing_continuation_token_stops_without_leaking_it(self):
        pages = [
            {"Contents": [{"Key": object_name(1)}], "IsTruncated": True, "NextContinuationToken": "1"},
            {"Contents": [{"Key": object_name(2)}], "IsTruncated": True, "NextContinuationToken": "1"},
        ]
        report = self.summarize(FakeClient({object_name(i): record() for i in (1, 2)}, pages=pages))
        self.assert_partial(report)
        self.assertEqual(report["scan"]["pagination_failures"], 1)
        for response in ({"Contents": [], "IsTruncated": True}, {"Contents": []}):
            with self.subTest(response=response):
                self.assert_partial(self.summarize(FakeClient(pages=[response])))

    def test_list_and_read_failures_suppress_all_metrics_and_private_messages(self):
        clients = (FakeClient(list_failure=True),
                   FakeClient({object_name(i): record() for i in (1, 2)}, failures=(object_name(2),)))
        for client in clients:
            with self.subTest(client=type(client).__name__):
                report = self.summarize(client)
                self.assert_partial(report)
                self.assertNotIn("synthetic-private", json.dumps(report))

    def test_invalid_or_oversized_records_are_partial_and_closed(self):
        cases = (
            b"not JSON synthetic-private", b"x" * (subject.MAX_RECORD_BYTES + 1), [],
            record(version=2), record(request_kind="synthetic-private-kind"),
            record(status="synthetic-private-status"), record(sent_at=""),
            record(status="failed"), record(created_at="not-a-time"),
            record(created_at="2026-09-28T01:00:00"),
            record(created_at="2026-10-01T00:00:00Z"),
            record(sent_at="2026-09-27T00:00:00Z"),
            record(status="failed", sent_at=[]), record(status="pending", sent_at=False),
            record(status="failed", sent_at=0), record(status="failed", sent_at=None),
        )
        for payload in cases:
            with self.subTest(payload_type=type(payload).__name__):
                client = FakeClient({object_name(1): payload})
                report = self.summarize(client)
                self.assert_partial(report)
                self.assertEqual(report["scan"]["invalid_records"], 1)
                self.assertTrue(all(body.closed for body in client.bodies))

    def test_read_is_bounded_even_without_content_length(self):
        body = BytesIO(b"x" * (subject.MAX_RECORD_BYTES + 200))
        sizes = []
        original_read = body.read
        body.read = lambda size: (sizes.append(size), original_read(size))[1]
        client = FakeClient({object_name(1): record()})
        client.get_object = lambda **_options: {"Body": body}
        report = self.summarize(client)
        self.assert_partial(report)
        self.assertEqual(sizes, [subject.MAX_RECORD_BYTES + 1])
        self.assertTrue(body.closed)

    def test_incomplete_or_invalid_declared_length_is_read_failure(self):
        raw = json.dumps(record()).encode()
        for declared in (len(raw) + 7, len(raw) - 7, -1, True, "128", None):
            with self.subTest(declared=declared):
                client = FakeClient({object_name(1): record()})
                body = BytesIO(raw)
                client.get_object = lambda **_options: {"Body": body, "ContentLength": declared}
                report = self.summarize(client)
                self.assert_partial(report)
                self.assertEqual(report["scan"]["read_failures"], 1)
                self.assertTrue(body.closed)

    def test_foreign_or_unexpected_object_names_are_never_read(self):
        client = FakeClient({"_other/private.json": record(), subject.PREFIX + "not-a-digest.json": record()})
        report = self.summarize(client)
        self.assert_partial(report)
        self.assertEqual(report["scan"]["invalid_objects"], 2)
        self.assertFalse(any(name == "get" for name, _ in client.calls))

    def test_output_is_aggregate_only_and_markdown_is_deterministic(self):
        private_record = record()
        report = self.summarize(FakeClient({object_name(123): private_record}))
        output = json.dumps(report) + subject.render_markdown(report)
        for secret in (object_name(123), "synthetic-private-bucket", *[
            private_record[name] for name in ("request_id", "requester_email", "contact_value", "note", "page_path", "last_error")
        ]):
            self.assertNotIn(secret, output)
        self.assertNotIn(private_record["attempted_at"], output)
        self.assertIn("provider acceptance", output)
        self.assertEqual(subject.render_markdown(report), subject.render_markdown(copy.deepcopy(report)))

    def test_recursive_privacy_validation_rejects_nested_extra_data_and_count_strings(self):
        report = self.summarize(FakeClient({object_name(1): record()}))
        for location in ((), ("scan",), ("windows", "created_window"),
                         ("windows", "created_window", "by_request_kind")):
            changed = copy.deepcopy(report)
            target = changed
            for key in location:
                target = target[key]
            target["private_extra"] = "synthetic@example.invalid"
            with self.assertRaises(subject.SafeError):
                subject.assert_aggregate_privacy(changed)
        changed = copy.deepcopy(report)
        changed["windows"]["created_window"]["by_request_kind"]["membership"] = "synthetic@example.invalid"
        with self.assertRaises(subject.SafeError):
            subject.assert_aggregate_privacy(changed)
        changed = copy.deepcopy(report)
        changed["notes"].append("synthetic-private-note")
        with self.assertRaises(subject.SafeError):
            subject.assert_aggregate_privacy(changed)

    def test_invalid_arguments_fail_before_reads(self):
        for start, end in (("2026-9-27", END), ("2026-02-30", END), (END, START), (START, "9999-12-31")):
            client = FakeClient()
            with self.assertRaises(subject.SafeError):
                subject.summarize(client, "synthetic-bucket", start, end)
            self.assertEqual(client.calls, [])
        for limit in (True, 0, -1, subject.MAX_OBJECTS + 1):
            with self.assertRaises(subject.SafeError):
                self.summarize(FakeClient(), max_objects=limit)

    def test_cli_unexpected_failure_does_not_print_exception_details(self):
        argv = ["snapshot", "--start-date", START, "--end-date", END,
                "--output", "unused.json", "--markdown-output", "unused.md"]
        with patch.object(sys, "argv", argv), patch.object(subject, "interval", side_effect=RuntimeError("synthetic-private-error")), \
                patch.object(sys, "stderr", new_callable=StringIO) as stderr:
            self.assertEqual(subject.main(), 1)
        self.assertNotIn("synthetic-private-error", stderr.getvalue())

    def test_workflow_has_only_manual_owner_read_path_and_verified_short_lived_artifact(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/portal-membership-snapshot.yml").read_text()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("schedule:", workflow)
        self.assertIn("github.actor == github.repository_owner", workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("retention-days: 1", workflow)
        self.assertIn("name: portal-membership-snapshot-counts", workflow)
        self.assertLess(workflow.index("assert_aggregate_privacy(report)"), workflow.index("uses: actions/upload-artifact@v4"))
        self.assertLess(workflow.index("uses: actions/upload-artifact@v4"), workflow.index("name: Require complete scan"))
        for unwanted in ("continue-on-error", "if: always()", "OWNER_NOTIFICATION_EMAIL", "BREVO_API_KEY", "wrangler", "archive_portal"):
            self.assertNotIn(unwanted, workflow)


if __name__ == "__main__":
    unittest.main()
