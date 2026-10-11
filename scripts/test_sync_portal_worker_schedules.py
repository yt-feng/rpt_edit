#!/usr/bin/env python3
from __future__ import annotations
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("schedules", ROOT / "scripts/sync_portal_worker_schedules.py")
schedules = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(schedules)
OLD = ["*/30 * * * *", *schedules.NEWSFEED_PARTS]
NEW = ["*/30 * * * *", schedules.NEWSFEED_UNION, schedules.REMINDER]

class Api:
    def __init__(self, state=None, *, reads=(), puts=()):
        self.state = list(OLD if state is None else state)
        self.reads = list(reads)
        self.put_results = list(puts)
        self.calls = []
    def get(self):
        self.calls.append(("GET", None))
        value = self.reads.pop(0) if self.reads else self.state
        if isinstance(value, Exception): raise value
        return list(value)
    def put(self, values):
        self.calls.append(("PUT", list(values)))
        self.state = list(values)
        outcome = self.put_results.pop(0) if self.put_results else values
        if isinstance(outcome, Exception): raise outcome
        return outcome

def run(api):
    return schedules.sync_schedules(api, sleep=lambda _seconds: None)

def firing_minutes(cron):
    minute, hours, *_ = cron.split()
    minutes = range(0, 60, int(minute[2:]))
    included = set()
    for part in hours.split(","):
        bounds = [int(value) for value in part.split("-")]
        included.update(range(bounds[0], bounds[-1] + 1))
    return {(hour, minute) for hour in included for minute in minutes}

class ScheduleTests(unittest.TestCase):
    def test_known_union_has_identical_daily_firing_times(self):
        previous = set().union(*(firing_minutes(cron) for cron in schedules.NEWSFEED_PARTS))
        self.assertEqual(previous, firing_minutes(schedules.NEWSFEED_UNION))
        self.assertEqual(schedules.desired_schedules(OLD), NEW)

    def test_unknown_schedules_preserved_exactly_and_partial_known_union_not_expanded(self):
        previous = ["11 15 * * MON", schedules.NEWSFEED_PARTS[0], "19 3 1 * *"]
        self.assertEqual(schedules.desired_schedules(previous), previous + [schedules.REMINDER])
        previous = ["11 15 * * MON", *schedules.NEWSFEED_PARTS]
        self.assertEqual(schedules.desired_schedules(previous), [previous[0], schedules.NEWSFEED_UNION, schedules.REMINDER])

    def test_limit_failure_and_initial_read_failure_never_write(self):
        for api in [Api(["1 1 * * *", "2 2 * * *", "3 3 * * *", "4 4 * * *", "5 5 * * *"]),
                    Api(reads=[schedules.ScheduleError("transport")])]:
            with self.assertRaises(schedules.ScheduleError): run(api)
            self.assertEqual([call for call in api.calls if call[0] == "PUT"], [])
            self.assertEqual(len(api.calls), 1)

    def test_update_is_one_put_followed_by_exact_readback_and_second_run_is_noop(self):
        api = Api()
        result = run(api)
        self.assertEqual(result, {"ok": True, "changed": True, "schedule_count": 3, "rollback": "not_needed"})
        self.assertEqual([method for method, _ in api.calls], ["GET", "GET", "PUT", "GET", "GET"])
        self.assertEqual(api.state, NEW)
        api.calls.clear()
        self.assertFalse(run(api)["changed"])
        self.assertEqual(api.calls, [("GET", None)])

    def test_unknown_put_ack_is_reconciled_before_any_new_mutation(self):
        api = Api(puts=[TimeoutError("PRIVATE API BODY")])
        self.assertTrue(run(api)["ok"])
        self.assertEqual([call for call in api.calls if call[0] == "PUT"], [("PUT", NEW)])

    def test_readback_handles_one_stale_previous_list_without_replaying_put(self):
        api = Api(reads=[OLD, OLD, OLD, NEW, NEW])
        self.assertTrue(run(api)["ok"])
        self.assertEqual(sum(method == "PUT" for method, _ in api.calls), 1)

    def test_concurrent_change_before_put_is_not_overwritten(self):
        api = Api(reads=[OLD, ["1 2 * * *"]])
        with self.assertRaises(schedules.ScheduleError) as caught: run(api)
        self.assertEqual(caught.exception.code, "concurrent_change")
        self.assertFalse(any(method == "PUT" for method, _ in api.calls))

    def test_concurrent_unrecognized_post_put_state_is_not_rolled_back(self):
        api = Api(reads=[OLD, OLD, ["1 2 * * *"]])
        with self.assertRaises(schedules.ScheduleError) as caught: run(api)
        self.assertEqual(caught.exception.rollback, "conflict")
        self.assertEqual(sum(method == "PUT" for method, _ in api.calls), 1)

    def test_failed_verification_restores_exact_prior_list_and_verifies(self):
        fail = schedules.ScheduleError("transport")
        api = Api(reads=[OLD, OLD, NEW, fail, fail, NEW])
        with self.assertRaises(schedules.ScheduleError) as caught: run(api)
        self.assertEqual(caught.exception.code, "verification_failed")
        self.assertEqual(caught.exception.rollback, "verified")
        self.assertEqual([call for call in api.calls if call[0] == "PUT"], [("PUT", NEW), ("PUT", OLD)])
        self.assertEqual(api.state, OLD)
        self.assertEqual(api.calls[-2:], [("GET", None), ("GET", None)])

    def test_unknown_rollback_ack_is_reconciled_without_repeating_rollback(self):
        fail = schedules.ScheduleError("transport")
        api = Api(reads=[OLD, OLD, NEW, fail, fail, NEW], puts=[NEW, TimeoutError("PRIVATE")])
        with self.assertRaises(schedules.ScheduleError) as caught: run(api)
        self.assertEqual(caught.exception.rollback, "verified")
        self.assertEqual(sum(method == "PUT" for method, _ in api.calls), 2)

    def test_unreadable_state_after_put_does_not_blindly_restore(self):
        fail = schedules.ScheduleError("transport")
        api = Api(reads=[OLD, OLD, *([fail] * 6)])
        with self.assertRaises(schedules.ScheduleError) as caught: run(api)
        self.assertEqual(caught.exception.rollback, "unverified")
        self.assertEqual(sum(method == "PUT" for method, _ in api.calls), 1)
        self.assertEqual(len(api.calls), 9)

    def test_changed_state_immediately_before_rollback_is_not_overwritten(self):
        fail = schedules.ScheduleError("transport")
        api = Api(reads=[OLD, OLD, NEW, fail, fail, ["1 3 * * *"]])
        with self.assertRaises(schedules.ScheduleError) as caught: run(api)
        self.assertEqual(caught.exception.rollback, "conflict")
        self.assertEqual(sum(method == "PUT" for method, _ in api.calls), 1)

    def test_wrapper_shape_is_strict_but_metadata_and_server_order_are_allowed(self):
        payload = {"success": True, "result": {"schedules": [{"cron": cron, "created_on": "2030-01-01"} for cron in reversed(NEW)]}}
        self.assertTrue(schedules.same(schedules.parse_schedules(payload), NEW))
        for payload in [{"success": True, "result": []}, {"success": False, "result": {"schedules": []}},
                        {"success": True, "result": {"schedules": [{"cron": "* * * * *"}, {"cron": "* * * * *"}]}}]:
            with self.assertRaises(schedules.ScheduleError): schedules.parse_schedules(payload)

    def test_https_only_fixed_path_no_redirects_or_retries_and_no_body_leak(self):
        calls = []
        class Response:
            status = 302
            def read(self, _limit): raise AssertionError("redirect body must not be read")
            def close(self): pass
        class Connection:
            def __init__(self, host, **kwargs):
                self.assert_host = host
                calls.append((host, kwargs["context"].verify_mode))
            def request(self, method, path, **kwargs): calls.append((method, path, kwargs))
            def getresponse(self): return Response()
            def close(self): pass
        api = schedules.ScheduleApi("a" * 32, "svc-fixture", "fixture-token", connection_factory=Connection)
        with self.assertRaises(schedules.ScheduleError) as caught: api.get()
        self.assertEqual(str(caught.exception), "http_status")
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][0], "api.cloudflare.com")
        self.assertEqual(calls[1][1], "/client/v4/accounts/" + "a" * 32 + "/workers/scripts/svc-fixture/schedules")

    def test_put_body_is_schedule_array_and_official_response_envelope_is_parsed(self):
        bodies = []
        class Response:
            status = 200
            def read(self, _limit): return json.dumps({"success": True, "result": {"schedules": [{"cron": cron} for cron in NEW]}}).encode()
            def close(self): pass
        class Connection:
            def __init__(self, *_args, **_kwargs): pass
            def request(self, method, _path, **kwargs): bodies.append((method, json.loads(kwargs["body"])))
            def getresponse(self): return Response()
            def close(self): pass
        api = schedules.ScheduleApi("a" * 32, "svc-fixture", "fixture-token", connection_factory=Connection)
        self.assertEqual(api.put(NEW), NEW)
        self.assertEqual(bodies, [("PUT", [{"cron": cron} for cron in NEW])])

    def test_configuration_failure_has_no_external_call_and_stdout_is_fixed_metadata(self):
        output = io.StringIO()
        with patch.dict(os.environ, {}, clear=True), patch.object(schedules.http.client, "HTTPSConnection") as connect, contextlib.redirect_stdout(output):
            self.assertEqual(schedules.main(), 1)
            connect.assert_not_called()
        self.assertEqual(json.loads(output.getvalue()), {"ok": False, "error": "configuration", "rollback": "not_needed"})
        output = io.StringIO()
        with patch.object(schedules, "ScheduleApi", return_value=Api(reads=[ValueError("PRIVATE URL TOKEN BODY")])), contextlib.redirect_stdout(output):
            self.assertEqual(schedules.main(), 1)
        self.assertNotIn("PRIVATE", output.getvalue())

if __name__ == "__main__":
    unittest.main(verbosity=2)
