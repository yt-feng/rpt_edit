#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import summarize_portal_growth_range as growth
import summarize_portal_member_cohort as cohort


def account(index: int, **changes: object) -> dict:
    return {"id": f"secret-account-{index}", "email": f"secret-{index}@example.test", "role": "user", "disabled": False,
            "created_at": "2026-10-25T01:00:00Z", "last_login_at": "2026-11-02T01:00:00Z",
            "effective_access": {"active": True, "access_mode": "all", "download_limit": 0, "source": "stored"}, **changes}


def snapshot(*accounts: dict) -> dict:
    return {"schema": cohort.SNAPSHOT_SCHEMA, "complete": True, "generated_at": "2026-11-23T08:00:00Z",
            "source_mode": "supabase", "user_count": len(accounts), "users": list(accounts)}


def event(key: str, session: str, second: int, *, user: dict | None = None, kind: str = "page_view", **changes: object) -> dict:
    return {"id": key, "type": kind, "ts": f"2026-11-02T01:00:{second:02d}Z", "date": "2026-11-02",
            "client_ts": f"2026-11-02T01:00:{second:02d}Z", "session_id": session,
            "session_started_at": "2026-11-02T01:00:00Z", "visitor_id": "secret-device", "user": user,
            "landing_path": "/reports/public-report.html", "path": "/reports/public-report.html",
            "report_id": "public-report", "report_title": "secret-client-supplied-title",
            "referrer_host": "www.google.com", "device_type": "desktop", **changes}


CATALOG = {"items": [{"id": "public-report", "title": "Public research title"}]}


class CohortTest(unittest.TestCase):
    def build(self, rows: list[dict], users: dict | None = None, **kwargs: object) -> dict:
        return cohort.build_member_cohort(rows, users or snapshot(account(1)), "2026-10-24", "2026-11-22",
                                          catalog=CATALOG, site_host="example.test", **kwargs)

    def test_same_session_anonymous_registration_and_download_and_no_private_output(self) -> None:
        rows = []
        for index in (1, 2):
            user, session = account(index), f"secret-session-{index}"
            rows.extend([
                event(f"secret-landing-{index}", session, 1),
                event(f"secret-open-{index}", session, 2, kind="report_open"),
                event(f"secret-register-{index}", session, 3, user=user, kind="account_auth", action="register", status="success"),
                event(f"secret-attempt-{index}", session, 4, user=user, kind="download_attempt"),
                event(f"secret-success-{index}", session, 5, user=user, kind="download_success"),
            ])
        report = self.build(list(reversed(rows)) + [rows[0]], snapshot(account(1), account(2)))
        primary = report["cohorts"][cohort.COHORTS[0]]
        self.assertEqual(primary["observed_accounts"], 2)
        self.assertEqual(primary["authenticated_intentional_active_accounts"], 2)
        self.assertEqual(primary["session_metrics"]["registration_sessions"], 2)
        self.assertEqual(primary["earliest_observed_window_entry"]["channels"], [{"channel": "organic_search", "accounts": 2}])
        activity = primary["report_activity"][0]
        self.assertEqual(activity["ordered_attempt_then_success_sessions"], 2)
        self.assertEqual(activity["report_open_before_registration_sessions"], 2)
        self.assertEqual(activity["title"], "Public research title")
        self.assertEqual(report["join_coverage"]["duplicate_events_removed"], 1)
        self.assertEqual(report["join_coverage"]["anonymous_events_linked_in_same_session"], 4)
        serialized = json.dumps(report) + cohort.markdown_summary(report)
        for private in ("secret-", "@example.test", "secret-client-supplied-title"):
            self.assertNotIn(private, serialized)
        growth.validate_aggregate_review(report)

    def test_current_access_not_paid_excludes_trial_scoped_disabled_and_roles(self) -> None:
        users = snapshot(account(1), account(2, effective_access={"active": True, "access_mode": "all", "download_limit": 3, "source": "stored"}),
                         account(3, effective_access={"active": True, "access_mode": "filters", "download_limit": 0, "source": "stored"}),
                         account(4, effective_access={"active": True, "access_mode": "all", "download_limit": 0, "source": "vid2ppt_trial"}),
                         account(5, disabled=True), account(6, role="super"),
                         account(7, effective_access={"active": False, "access_mode": "all", "download_limit": 0, "source": "stored"}),
                         account(8, effective_access={"active": True, "access_mode": "all", "download_limit": 0, "source": "entitlement+vid2ppt_trial"}))
        report = self.build([], users)
        self.assertEqual([report["cohorts"][name]["current_accounts"] for name in cohort.COHORTS], [2, 3, 2])
        self.assertEqual(report["snapshot_counts"]["privileged_accounts_excluded"], 1)
        self.assertEqual(report["snapshot_counts"]["disabled_normal_accounts"], 1)
        self.assertIn("does not mean paid", report["notes"][0])

    def test_ambiguous_unknown_and_privileged_sessions_are_not_joined(self) -> None:
        users = snapshot(account(1), account(2), account(3, role="operator"))
        rows = [event("a", "shared", 1), event("b", "shared", 2, user=account(1)), event("c", "shared", 3, user=account(2)),
                event("d", "unknown", 1, user=account(99)), event("e", "unknown", 2, user=account(1)),
                event("f", "staff", 1), event("g", "staff", 2, user=account(3, role="operator")),
                event("h", "mismatch", 1, user={"id": account(1)["id"], "email": account(2)["email"]}),
                event("i", "anonymous", 1), event("j", "", 1, user=account(1))]
        result = self.build(rows, users)
        coverage = result["join_coverage"]
        self.assertEqual(coverage["multi_account_sessions_excluded"], 1)
        self.assertEqual(coverage["unknown_authenticated_sessions_excluded"], 2)
        self.assertEqual(coverage["privileged_sessions_excluded"], 1)
        self.assertEqual(coverage["anonymous_only_sessions"], 1)
        self.assertEqual(coverage["events_without_explicit_session"], 1)
        self.assertEqual(result["cohorts"][cohort.COHORTS[0]]["observed_accounts"], 0)

    def test_no_cross_session_or_device_join_and_server_confirmation_stays_unattributed(self) -> None:
        user = account(1)
        rows = [event("anonymous", "anonymous", 1), event("login", "login", 2, user=user, kind="account_auth", action="login", status="success", referrer_host="", landing_path="/"),
                event("confirmation", "anonymous", 3, user=user, kind="form_confirmation", action="provider_result", request_kind="registration", status="provider_accepted"),
                event("bot", "bot", 4, user=user, verified_bot=True), event("admin", "admin", 5, user=user, kind="admin_user_update")]
        result = self.build(rows, min_count=1)
        primary = result["cohorts"][cohort.COHORTS[0]]
        self.assertEqual(primary["session_metrics"]["sessions"], 1)
        self.assertEqual(primary["earliest_observed_window_entry"]["channels"], [{"channel": "direct_or_unknown", "accounts": 1}])
        self.assertEqual(primary["session_metrics"]["registration_sessions"], 0)
        self.assertEqual(result["unattributed_server_form_confirmations"][0]["events"], 1)
        self.assertIsNone(result["unattributed_server_form_confirmations"][0]["client_sessions"])

    def test_window_start_and_earliest_entry_do_not_become_lifetime_acquisition(self) -> None:
        user = account(1)
        rows = [event("old", "old", 1, user=user, ts="2026-10-23T00:00:00Z", session_started_at="2026-10-23T00:00:00Z"),
                event("first", "first", 1, user=user, ts="2026-10-24T00:00:01Z", session_started_at="2026-10-24T00:00:00Z", referrer_host="chatgpt.com"),
                event("later", "later", 1, user=user, referrer_host="www.google.com"),
                event("future", "future", 1, user=user, ts="2026-11-23T00:00:00Z")]
        result = self.build(rows)
        primary = result["cohorts"][cohort.COHORTS[0]]
        self.assertEqual(primary["earliest_observed_window_entry"]["channels"], [{"channel": "ai_referral", "accounts": 1}])
        self.assertEqual(result["join_coverage"]["outside_window_events"], 2)
        self.assertEqual(primary["earliest_observed_window_entry"]["landing_pages"], [])
        self.assertEqual(primary["report_activity"], [])

    def test_missing_and_tied_session_start_remain_unknown(self) -> None:
        rows = [event("one", "one", 1, user=account(1)), event("two", "two", 2, user=account(1)),
                event("three", "three", 1, user=account(2), session_started_at="")]
        result = self.build(rows, snapshot(account(1), account(2)))
        entry = result["cohorts"][cohort.COHORTS[0]]["earliest_observed_window_entry"]
        self.assertEqual(entry["channels"], [{"channel": "unknown", "accounts": 2}])
        self.assertEqual(entry["coverage"]["accounts_without_unambiguous_window_entry"], 2)

    def test_order_requires_same_report_and_client_time_and_no_passive_activity(self) -> None:
        rows = [event("landing", "session", 1, user=account(1)),
                event("loading", "session", 2, user=account(1), kind="report_open", action="detail_load_ready"),
                event("attempt", "session", 5, user=account(1), kind="download_attempt"),
                event("success", "session", 4, user=account(1), kind="download_success"),
                event("other", "session", 6, user=account(1), kind="download_success", report_id="secret-unpublished-report"),
                event("register", "session", 7, user=account(1), kind="account_auth", action="register", status="error")]
        primary = self.build(rows, min_count=1)["cohorts"][cohort.COHORTS[0]]
        self.assertEqual(primary["report_activity"][0]["ordered_attempt_then_success_sessions"], 0)
        self.assertEqual(primary["report_activity"][0]["report_open_sessions"], 0)
        self.assertEqual(primary["session_metrics"]["registration_sessions"], 0)
        self.assertNotIn("secret-unpublished-report", json.dumps(primary))
        passive = self.build(rows[:2])["cohorts"][cohort.COHORTS[0]]
        self.assertEqual(passive["authenticated_intentional_active_accounts"], 0)

    def test_snapshot_integrity_fails_closed(self) -> None:
        variants = [snapshot(account(1), account(1)), {**snapshot(account(1)), "complete": False},
                    {**snapshot(account(1)), "user_count": 2}, {**snapshot(account(1)), "generated_at": "invalid"},
                    snapshot(account(1, effective_access={"active": True, "access_mode": "all", "download_limit": False, "source": "stored"})),
                    snapshot(account(1, effective_access={"active": True, "access_mode": "all", "download_limit": 0, "source": "error"}))]
        for variant in variants:
            with self.subTest(variant=variant.get("user_count")), self.assertRaises(ValueError):
                self.build([], variant)

    def test_redacted_duplicate_emails_keep_exact_ids_without_email_only_cross_join(self) -> None:
        users = snapshot(account(1, email="redacted@users.example.invalid"), account(2, email="redacted@users.example.invalid"))
        rows = [event("id-one", "one", 1, user=account(1)), event("id-two", "two", 1, user=account(2)),
                event("email-only", "unknown", 1, user={"email": "redacted@users.example.invalid"})]
        report = self.build(rows, users)
        self.assertEqual(report["cohorts"][cohort.COHORTS[0]]["current_accounts"], 2)
        self.assertEqual(report["cohorts"][cohort.COHORTS[0]]["observed_accounts"], 2)
        self.assertEqual(report["join_coverage"]["unknown_authenticated_sessions_excluded"], 1)
        duplicates = snapshot(account(1, email="shared@example.test"), account(2, email="shared@example.test"))
        email_only = self.build([event("shared", "shared", 1, user={"email": "shared@example.test"})], duplicates)
        self.assertEqual(email_only["join_coverage"]["unknown_authenticated_sessions_excluded"], 1)

    def test_missing_client_time_does_not_report_measured_zero_ordered_downloads(self) -> None:
        rows = [event("a", "one", 1, user=account(1), kind="download_attempt", client_ts=""),
                event("b", "one", 2, user=account(1), kind="download_success", client_ts="")]
        row = self.build(rows, min_count=1)["cohorts"][cohort.COHORTS[0]]["report_activity"][0]
        self.assertIsNone(row["ordered_attempt_then_success_sessions"])
        self.assertEqual(row["download_pairs_without_usable_client_time_sessions"], 1)

    def test_authentication_only_and_automatic_newsfeed_load_are_not_product_activity(self) -> None:
        rows = [event("login", "one", 1, user=account(1), kind="account_auth", action="login", status="success"),
                event("load", "one", 2, user=account(1), kind="newsfeed_interaction", action="feed_load", outcome="success"),
                event("article", "two", 1, user=account(2), kind="newsfeed_interaction", action="article_open")]
        primary = self.build(rows, snapshot(account(1), account(2)))["cohorts"][cohort.COHORTS[0]]
        self.assertEqual(primary["authenticated_intentional_active_accounts"], 2)
        self.assertEqual(primary["authenticated_product_active_accounts"], 1)

    def test_unknown_path_query_and_event_title_never_enter_report(self) -> None:
        rows = [event("a", "one", 1, user=account(1), kind="search", query="secret-personal-query",
                      path="/secret-person/email@example.test", landing_path="/secret-person/email@example.test?token=private")]
        report = self.build(rows, min_count=1)
        serialized = json.dumps(report)
        for value in ("secret-person", "email@example.test", "private", "secret-personal-query", "secret-client-supplied-title"):
            self.assertNotIn(value, serialized)


class StorageAndWorkflowTest(unittest.TestCase):
    def test_controlled_download_failures_remain_distinct_without_error_text(self) -> None:
        self.assertEqual(growth.download_error_category({"status": "network", "error": "secret-address"}), "network_failure")
        self.assertEqual(growth.download_error_category({"status": "body", "error": "secret-address"}), "body_read_failure")
        self.assertEqual(growth.download_error_category({"status": "secret-address"}), "other")

    def test_per_day_single_read_primary_backup_and_count_only_progress(self) -> None:
        reads = []
        class Client:
            def list_objects_v2(self, **kwargs: object) -> dict:
                prefix = str(kwargs["Prefix"])
                return {"Contents": [{"Key": prefix + "event.json"}], "IsTruncated": False}
            def get_object(self, *, Bucket: str, Key: str) -> dict:
                reads.append(Key)
                return {"Body": io.BytesIO(json.dumps(event(Key, "private-session", 1)).encode())}
        progress = []
        with patch.object(growth, "r2_client", return_value=Client()), patch.dict(os.environ, {"R2_BUCKET": "private-bucket"}):
            rows, dates = growth.load_r2_range_events(date(2026, 11, 2), date(2026, 11, 2), progress=progress.append)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(reads), 1, "primary/backup logical events are read only once")
        self.assertEqual(dates, ["2026-11-02"])
        self.assertEqual(progress[-1], {"date": "2026-11-02", "phase": "complete", "read": 1, "total_read": 1})
        self.assertNotIn("private", json.dumps(progress))

    def test_failed_day_or_unreadable_both_mirrors_cannot_return_complete_data(self) -> None:
        class Client:
            def list_objects_v2(self, **kwargs: object) -> dict:
                return {"Contents": [{"Key": str(kwargs["Prefix"]) + "private.json"}], "IsTruncated": False}
            def get_object(self, **kwargs: object) -> dict:
                raise RuntimeError("private-key-and-credentials")
        for fail_listing in (False, True):
            client = Client()
            if fail_listing:
                client.list_objects_v2 = lambda **kwargs: (_ for _ in ()).throw(RuntimeError("private-key"))
            with patch.object(growth, "r2_client", return_value=client), patch.dict(os.environ, {"R2_BUCKET": "private-bucket"}):
                with self.assertRaises(RuntimeError) as error:
                    growth.load_r2_range_events(date(2026, 11, 2), date(2026, 11, 2))
                self.assertNotIn("private", str(error.exception))

    def test_repeated_storage_cursor_is_bounded(self) -> None:
        class Client:
            def list_objects_v2(self, **kwargs: object) -> dict:
                return {"Contents": [], "IsTruncated": True, "NextContinuationToken": "same"}
        with self.assertRaises(RuntimeError):
            growth.list_keys(Client(), "private", "private-prefix")

    def test_event_stream_is_bounded_closed_and_corruption_uses_mirror(self) -> None:
        for bad in (b"{truncated", b"x" * (512 * 1024 + 2), b"{}"):
            streams = {"primary": io.BytesIO(bad), "backup": io.BytesIO(b'{"id":"valid","type":"page_view"}')}
            class Client:
                def get_object(self, *, Bucket: str, Key: str) -> dict:
                    return {"Body": streams[Key]}
            self.assertEqual(growth.read_event(Client(), "bucket", ["primary", "backup"])["id"], "valid")
            self.assertTrue(all(stream.closed for stream in streams.values()))

    def test_truncated_listing_without_continuation_fails(self) -> None:
        class Client:
            def list_objects_v2(self, **kwargs: object) -> dict:
                return {"Contents": [], "IsTruncated": True}
        with self.assertRaises(RuntimeError):
            growth.list_keys(Client(), "bucket", "prefix")

    def test_archive_context_only_reads_at_most_four_aggregate_objects(self) -> None:
        reads = []
        streams = []
        archive = growth.build_growth_review([], "2026-10-01", "2026-10-02")
        class Client:
            def list_objects_v2(self, **kwargs: object) -> dict:
                self.assert_prefix = kwargs["Prefix"]
                return {"Contents": [{"Key": f"_analytics/reviews/weekly/2026-10-0{index}_2026-10-1{index}/growth-review.json"} for index in range(1, 7)]}
            def get_object(self, *, Bucket: str, Key: str) -> dict:
                reads.append(Key)
                stream = io.BytesIO(json.dumps(archive).encode())
                streams.append(stream)
                return {"Body": stream}
        client = Client()
        with patch.object(growth, "r2_client", return_value=client), patch.dict(os.environ, {"R2_BUCKET": "private-bucket"}):
            report = growth.read_previous_aggregate_reviews()
        self.assertEqual(report["review_count"], 4)
        self.assertEqual(len(reads), 4)
        self.assertTrue(all(stream.closed for stream in streams))
        self.assertTrue(all("/reviews/weekly/" in key for key in reads))
        self.assertEqual(client.assert_prefix, "_analytics/reviews/weekly/")
        growth.validate_aggregate_review(report)
        with self.assertRaises(ValueError):
            growth.validate_aggregate_review({"privacy": {"raw": False}, "nested": [{"email": "hidden"}]})

    def test_growth_and_cohort_share_one_read_and_failed_read_creates_no_report(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            users = root / "users.json"
            users.write_text(json.dumps(snapshot(account(1))))
            arguments = ["analysis", "--start-date", "2026-10-24", "--end-date", "2026-11-22", "--output", str(root / "growth.json"),
                         "--users-snapshot", str(users), "--cohort-output", str(root / "cohort.json")]
            with patch.object(sys, "argv", arguments), patch.object(growth, "load_r2_range_events", return_value=([event("x", "s", 1, user=account(1))], ["2026-11-02"])) as reader, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(growth.main(), 0)
                reader.assert_called_once()
            self.assertTrue(json.loads((root / "growth.json").read_text())["data_quality"]["storage_read_complete"])
            (root / "growth.json").unlink()
            (root / "cohort.json").unlink()
            with patch.object(sys, "argv", arguments), patch.object(growth, "load_r2_range_events", side_effect=RuntimeError("read failed")), self.assertRaises(RuntimeError):
                growth.main()
            self.assertFalse((root / "growth.json").exists())
            self.assertFalse((root / "cohort.json").exists())

    def test_workflow_uses_canonical_profile_and_never_uploads_snapshot(self) -> None:
        source = (Path(__file__).parents[1] / ".github/workflows/portal-growth-review.yml").read_text()
        self.assertIn("timeout-minutes: 300", source)
        self.assertIn("ACCOUNT_STORE_MODE: supabase", source)
        self.assertIn("PORTAL_PRIVATE_CONFIG_B64", source)
        self.assertLess(source.index("name: Materialize canonical"), source.index("name: Read complete current"))
        self.assertLess(source.index("name: Read complete current"), source.index("name: Build aggregate"))
        self.assertIn("--skip-generated-files", source)
        self.assertIn("umask 077", source)
        self.assertIn("--archive-context-only --archive-context-limit 4", source)
        uploaded = source[source.index("name: Upload short-lived aggregate review"):]
        self.assertNotIn("private-input", uploaded)
        self.assertNotIn("current-users", uploaded)
        self.assertNotIn("workers/", uploaded)
        self.assertIn("retention-days: 1", uploaded)


if __name__ == "__main__":
    unittest.main()
