#!/usr/bin/env python3
from __future__ import annotations

from copy import deepcopy
import contextlib
from datetime import datetime, timedelta, timezone
import hashlib
import hmac
import io
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import collect_report_discussion_starters as collector

NOW = datetime(2030, 1, 10, 2, 0, tzinfo=timezone.utc)


def report_id(number):
    return f"{number:024x}"


def catalog(*numbers, date="300110", now=NOW):
    return {"schema_version": 1, "updated_at_bjt": collector.iso(now), "item_count": len(numbers),
            "items": [{"id": report_id(number), "date_folder": date, "title": "Synthetic report"} for number in numbers]}


class Store:
    def __init__(self):
        self.rows, self.version, self.writes = {}, 0, []
        self.fail_final = False

    def get(self, key):
        row = self.rows.get(key)
        return (deepcopy(row[0]), row[1]) if row else (None, None)

    def put(self, key, value, *, etag):
        current = self.rows.get(key)
        if (current[1] if current else None) != etag:
            raise collector.DiscussionError("fixture_conflict")
        if self.fail_final and key == collector.STATE_KEY and any(row["status"] == "ready" for row in value.get("queue", {}).values()):
            raise collector.DiscussionError("fixture_write_interrupted")
        self.version += 1
        self.rows[key] = (deepcopy(value), str(self.version))
        self.writes.append((key, deepcopy(value)))
        return str(self.version)


def run(store, payload, calls=None, *, now=NOW, outcome="ready", max_batch=20, **kwargs):
    if calls is None:
        calls = []

    def generate(request):
        calls.append(request)
        state, _ = store.get(collector.STATE_KEY)
        row = state["queue"][request["report_id"]]
        assert row["status"] == "pending", "reserve before any paid request"
        marker, _ = store.get(collector.eligibility_key(request["report_id"]))
        assert marker["report_id"] == request["report_id"]
        if isinstance(outcome, Exception):
            raise outcome
        return {"status": outcome}

    return collector.collect(store, payload, generate, now=now, max_batch=max_batch, minimum_items=1, **kwargs)


class CollectionTests(unittest.TestCase):
    def test_first_complete_baseline_marks_every_current_id_old_and_never_generates(self):
        store, calls = Store(), []
        result = run(store, catalog(1, 2, 3), calls)
        self.assertTrue(result["baseline_created"])
        self.assertEqual(result["baseline_count"], 3)
        self.assertEqual(calls, [])
        self.assertEqual(len(store.rows), 1)
        state, _ = store.get(collector.STATE_KEY)
        self.assertEqual(state["seen_ids"], [report_id(1), report_id(2), report_id(3)])
        run(store, catalog(1, 2, 3), calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(calls, [])

    def test_partial_or_malformed_first_catalog_never_creates_a_baseline(self):
        samples = []
        for field, value in [("item_count", 2), ("complete", False), ("truncated", True), ("preview", True), ("total_item_count", 100), ("updated_at_bjt", "invalid")]:
            payload = catalog(1)
            payload[field] = value
            samples.append(payload)
        samples += [catalog(), {**catalog(1, 2), "items": [catalog(1)["items"][0]] * 2}, {**catalog(1), "schema_version": 2}]
        for payload in samples:
            with self.subTest(payload=payload):
                store, calls = Store(), []
                with self.assertRaises(collector.DiscussionError):
                    run(store, payload, calls)
                self.assertEqual(store.rows, {})
                self.assertEqual(calls, [])
        with self.assertRaises(collector.DiscussionError):
            collector.validate_catalog(catalog(1))

    def test_only_new_current_report_gets_eligibility_and_ai_no_historical_backfill(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        payload = catalog(1, 2, 3, 4, 5)
        payload["items"][2]["date_folder"] = "290101"
        payload["items"][3].pop("date_folder")
        payload["items"][4]["date_folder"] = "301231"
        result = run(store, payload, calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(result["discovered"], 1)
        self.assertEqual(result["historical_excluded"], 3)
        self.assertEqual(calls, [{"source": "catalog", "report_id": report_id(2)}])
        marker, _ = store.get(collector.eligibility_key(report_id(2)))
        self.assertEqual(marker, {"version": 1, "source": "catalog", "report_id": report_id(2),
                                 "activated_at": collector.iso(NOW), "first_seen_at": collector.iso(NOW + timedelta(minutes=30))})
        self.assertEqual(len(store.get(collector.STATE_KEY)[0]["seen_ids"]), 5)
        # Reappearing historical reports stay excluded even after metadata changes.
        payload["items"][2]["date_folder"] = "300110"
        run(store, payload, calls, now=NOW + timedelta(hours=1))
        self.assertEqual(len(calls), 1)

    def test_partial_later_catalog_preserves_queue_and_never_generates(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        before = deepcopy(store.rows)
        payload = catalog(1, 2)
        payload["item_count"] = 3
        with self.assertRaises(collector.DiscussionError):
            run(store, payload, calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(store.rows, before)
        self.assertEqual(calls, [])

    def test_new_report_attempt_cap_and_fair_queue_resume(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        payload = catalog(*range(1, 27))
        first = run(store, payload, calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(first["attempted"], 20)
        self.assertEqual(first["queued"], 5)
        second = run(store, payload, calls, now=NOW + timedelta(hours=1))
        self.assertEqual(second["attempted"], 5)
        self.assertEqual(second["ready"], 25)
        self.assertEqual(len({row["report_id"] for row in calls}), 25)

    def test_every_terminal_state_is_preserved_without_automatic_retry(self):
        for outcome in ["ready", "pending", "reserved", "unknown", "rejected", "failed", "not_authorized", "invalid_request", "unexpected", TimeoutError("private response")]:
            with self.subTest(outcome=outcome):
                store, calls = Store(), []
                run(store, catalog(1), calls)
                run(store, catalog(1, 2), calls, now=NOW + timedelta(minutes=30), outcome=outcome)
                run(store, catalog(1, 2), calls, now=NOW + timedelta(hours=2))
                self.assertEqual(len(calls), 1)

    def test_source_unavailable_retries_later_without_starving_first_attempts(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        run(store, catalog(1, 2), calls, now=NOW + timedelta(minutes=30), outcome="source_unavailable")
        run(store, catalog(1, 2), calls, now=NOW + timedelta(minutes=40))
        self.assertEqual(len(calls), 1)
        run(store, catalog(1, 2, 3), calls, now=NOW + timedelta(hours=2), max_batch=1)
        self.assertEqual(calls[-1]["report_id"], report_id(3))
        run(store, catalog(1, 2, 3), calls, now=NOW + timedelta(hours=3))
        self.assertEqual(calls[-1]["report_id"], report_id(2))

    def test_unknown_final_write_leaves_pending_reservation_and_never_replays(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        store.fail_final = True
        with self.assertRaises(collector.DiscussionError):
            run(store, catalog(1, 2), calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(store.get(collector.STATE_KEY)[0]["queue"][report_id(2)]["status"], "pending")
        store.fail_final = False
        run(store, catalog(1, 2), calls, now=NOW + timedelta(hours=1))
        self.assertEqual(len(calls), 1)

    def test_conflicting_marker_fails_before_provider_and_preserves_other_owner_state(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        marker = {"version": 1, "source": "catalog", "report_id": report_id(2), "activated_at": "other-cycle"}
        store.put(collector.eligibility_key(report_id(2)), marker, etag=None)
        with self.assertRaisesRegex(collector.DiscussionError, "eligibility_conflict"):
            run(store, catalog(1, 2), calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(calls, [])
        self.assertEqual(store.get(collector.eligibility_key(report_id(2)))[0], marker)

    def test_regressed_snapshot_and_bad_state_fail_before_new_eligibility(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        with self.assertRaisesRegex(collector.DiscussionError, "snapshot_regressed"):
            run(store, catalog(1, 2, now=NOW - timedelta(days=1)), calls, now=NOW + timedelta(minutes=30))
        state, etag = store.get(collector.STATE_KEY)
        state["baseline_complete"] = False
        store.put(collector.STATE_KEY, state, etag=etag)
        with self.assertRaises(collector.DiscussionError):
            run(store, catalog(1, 2), calls, now=NOW + timedelta(minutes=30))
        self.assertEqual(calls, [])

    def test_elapsed_budget_stops_before_next_generation(self):
        store, calls = Store(), []
        run(store, catalog(1), calls)
        ticks = iter([0, 0, 1201])
        result = run(store, catalog(1, 2, 3), calls, now=NOW + timedelta(minutes=30), elapsed=lambda: next(ticks))
        self.assertEqual(result["attempted"], 1)
        self.assertEqual(result["queued"], 1)


class Response(io.BytesIO):
    def __init__(self, body, status=200):
        super().__init__(json.dumps(body).encode())
        self.status = status


class TransportTests(unittest.TestCase):
    def test_catalog_request_identifies_the_operations_client(self):
        def opener(request, timeout):
            self.assertEqual(request.get_header("User-agent"), "portal-report-discussion-starters/1.0")
            self.assertEqual(request.get_header("Accept"), "application/json")
            return Response({"items": []})
        self.assertEqual(collector.http_json("https://portal.example.invalid/data/catalog.json", opener=opener), (200, {"items": []}))

    def test_readiness_checks_the_exact_catalog_report_without_authorization_or_mutation(self):
        calls = []
        def opener(request, timeout):
            calls.append(request)
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.full_url, f"https://portal.example.invalid/api/report-discussion?source=catalog&report_id={report_id(1)}")
            self.assertIsNone(request.data)
            self.assertIsNone(request.get_header("X-portal-signature"))
            self.assertEqual(request.get_header("User-agent"), "portal-report-discussion-starters/1.0")
            self.assertEqual(timeout, 30)
            return Response({"source": "catalog", "report_id": report_id(1), "starter": None, "starter_status": "none", "comments": []})
        self.assertTrue(collector.worker_ready("https://portal.example.invalid/api", report_id(1), opener=opener))
        self.assertEqual(len(calls), 1)

    def test_old_worker_plain_text_404_waits_but_other_invalid_responses_fail_closed(self):
        def missing(*_args, **_kwargs):
            response = io.BytesIO(b"Not found")
            response.status = 404
            return response
        self.assertFalse(collector.worker_ready("https://portal.example.invalid/api", report_id(1), opener=missing))
        valid = {"source": "catalog", "report_id": report_id(1), "starter": None, "starter_status": "none", "comments": []}
        samples = [(200, {**valid, "source": "hot"}), (200, {**valid, "report_id": report_id(2)}),
                   (200, {**valid, "comments": {}}), (200, {**valid, "ok": False}), (503, valid)]
        for status, result in samples:
            with self.subTest(status=status, result=result):
                with self.assertRaises(collector.DiscussionError):
                    collector.worker_ready("https://portal.example.invalid/api", report_id(1),
                        opener=lambda *_args, **_kwargs: Response(result, status))

    def test_main_does_not_construct_storage_or_touch_baseline_when_worker_not_ready(self):
        environment = {name: "fixture" for name in ("OPS_ALERT_SIGNING_KEY", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")}
        environment.update(PORTAL_SITE_URL="https://portal.example.invalid", PORTAL_WORKER_URL="/api", R2_ACCOUNT_ID="a" * 32)
        for readiness, exit_code in [(False, 0), (collector.DiscussionError("worker_readiness_unconfirmed"), 1)]:
            stdout, stderr = io.StringIO(), io.StringIO()
            with self.subTest(readiness=readiness), patch.dict(collector.os.environ, environment), \
                    patch.object(collector, "http_json", return_value=(200, catalog(*range(100)))), \
                    patch.object(collector, "worker_ready", side_effect=readiness if isinstance(readiness, Exception) else None, return_value=readiness) as ready, \
                    patch.object(collector, "R2Store") as storage, patch.object(collector, "collect") as collect, \
                    contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                self.assertEqual(collector.main([]), exit_code)
                ready.assert_called_once_with("https://portal.example.invalid/api", report_id(0))
                storage.assert_not_called()
                collect.assert_not_called()
                if exit_code == 0:
                    self.assertEqual(json.loads(stdout.getvalue()), {"ok": True, "waiting_for_worker": True, "attempted": 0})
                else:
                    self.assertEqual(json.loads(stderr.getvalue())["code"], "worker_readiness_unconfirmed")

    def test_main_rejects_partial_catalog_before_readiness_or_storage(self):
        environment = {name: "fixture" for name in ("OPS_ALERT_SIGNING_KEY", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")}
        environment.update(PORTAL_SITE_URL="https://portal.example.invalid", PORTAL_WORKER_URL="/api", R2_ACCOUNT_ID="a" * 32)
        partial = catalog(*range(100))
        partial["item_count"] = 101
        with patch.dict(collector.os.environ, environment), patch.object(collector, "http_json", return_value=(200, partial)), \
                patch.object(collector, "worker_ready") as ready, patch.object(collector, "R2Store") as storage, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(collector.main([]), 1)
            ready.assert_not_called()
            storage.assert_not_called()

    def test_main_creates_storage_only_after_valid_readiness_response(self):
        environment = {name: "fixture" for name in ("OPS_ALERT_SIGNING_KEY", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")}
        environment.update(PORTAL_SITE_URL="https://portal.example.invalid", PORTAL_WORKER_URL="/api", R2_ACCOUNT_ID="a" * 32)
        payload = catalog(*range(100))
        responses = [(200, payload), (200, {"source": "catalog", "report_id": report_id(0), "starter": None, "starter_status": "none", "comments": []})]
        client = Mock()
        modules = {"boto3": SimpleNamespace(client=client), "botocore": SimpleNamespace(),
                   "botocore.config": SimpleNamespace(Config=lambda **kwargs: kwargs)}
        def make_client(*_args, **_kwargs):
            self.assertEqual(http.call_count, 2, "readiness must finish before any storage client exists")
            return object()
        client.side_effect = make_client
        with patch.dict(collector.os.environ, environment), patch.dict(collector.sys.modules, modules), \
                patch.object(collector, "http_json", side_effect=responses) as http, patch.object(collector, "R2Store") as storage, \
                patch.object(collector, "collect", return_value={"ok": True, "baseline_created": True, "attempted": 0}) as collect, \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(collector.main([]), 0)
            client.assert_called_once()
            storage.assert_called_once()
            self.assertIs(collect.call_args.args[0], storage.return_value)
            self.assertEqual(collect.call_args.args[1], payload)

    def test_signed_generation_body_and_exact_endpoint_are_bound_and_called_once(self):
        calls = []
        payload = {"source": "catalog", "report_id": report_id(2)}
        def opener(request, timeout):
            calls.append(request)
            self.assertEqual(request.full_url, "https://portal.example.invalid/api/ops/report-discussions/generate")
            self.assertEqual(json.loads(request.data), payload)
            expected = hmac.new(b"fixture-secret", b"1234567." + request.data, hashlib.sha256).hexdigest()
            self.assertEqual(request.get_header("X-portal-signature"), "sha256=" + expected)
            self.assertEqual(request.get_header("User-agent"), "portal-report-discussion-starters/1.0")
            self.assertEqual(timeout, 90)
            return Response({"ok": True, "generated": True, "status": "ready"})
        self.assertEqual(collector.generate_http("https://portal.example.invalid/api", "fixture-secret", payload, opener=opener, timestamp=1234567), {"status": "ready"})
        self.assertEqual(len(calls), 1)

    def test_known_pre_generation_unavailability_can_retry_but_ambiguous_http_does_not(self):
        for status, expected in [("provider_unavailable", "provider_unavailable"), ("unavailable", "unknown")]:
            result = collector.generate_http("https://portal.example.invalid/api", "fixture", {}, opener=lambda *_args, **_kwargs: Response({"status": status}, 503))
            self.assertEqual(result["status"], expected)
        for url in ["http://portal.example.invalid", "https://user:pass@portal.example.invalid", "https://portal.example.invalid?secret=1"]:
            with self.assertRaises(collector.DiscussionError):
                collector.https_base(url)

    def test_r2_conditional_put_unknown_ack_is_read_back_without_replaying(self):
        class Client:
            puts = 0
            value = None
            def put_object(self, **kwargs):
                self.puts += 1
                self.value = kwargs["Body"]
                self.args = kwargs
                raise TimeoutError("private upstream body")
            def get_object(self, **_kwargs):
                return {"Body": io.BytesIO(self.value), "ETag": "new-etag"}
        client = Client()
        store = collector.R2Store(client, "fixture-bucket")
        self.assertEqual(store.put("fixture-key", {"x": 1}, etag=None), "new-etag")
        self.assertEqual(client.puts, 1)
        self.assertEqual(client.args["IfNoneMatch"], "*")
        self.assertEqual(client.args["CacheControl"], "private, no-store")

    def test_r2_cas_conflict_is_not_mistaken_for_own_reservation(self):
        class Conflict(Exception):
            response = {"Error": {"Code": "PreconditionFailed"}}
        class Client:
            def put_object(self, **_kwargs):
                raise Conflict()
            def get_object(self, **_kwargs):
                raise AssertionError("known CAS conflict cannot acquire the winner's reservation")
        with self.assertRaisesRegex(collector.DiscussionError, "storage_write_conflict"):
            collector.R2Store(Client(), "fixture").put("key", {}, etag="old-etag")

    def test_workflow_runs_only_main_in_cloud_with_serial_execution_and_existing_secrets(self):
        text = (Path(__file__).resolve().parents[1] / ".github/workflows/report-discussion-starters.yml").read_text()
        for expected in ["13,43 * * * *", "github.ref == 'refs/heads/main'", "vars.PORTAL_AUTOMATION_ENABLED == 'true'", "cancel-in-progress: false", "--max-batch 20", "secrets.OPS_ALERT_SIGNING_KEY || secrets.PASSWORD_SECRET", "persist-credentials: false"]:
            self.assertIn(expected, text)
        self.assertNotIn("force", text)
        self.assertNotIn("backfill", text)


if __name__ == "__main__":
    unittest.main()
