#!/usr/bin/env python3
"""Exercise delayed GitHub step visibility without weakening source gates."""
import contextlib
import copy
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from daily_market_source_status import JobsPending, evaluate_live, github_json


RUN_ID = "38474801707"
SHA = "a" * 40
REPOSITORY = "example/research"
LIST_PATH = f"repos/{REPOSITORY}/actions/runs/{RUN_ID}/jobs?filter=latest&per_page=100"


def step(name, conclusion="success", status="completed"):
    return {"name": name, "status": status, "conclusion": conclusion}


def shard(index=0):
    return {
        "id": 100 + index, "name": f"process-shard ({index})", "run_id": int(RUN_ID),
        "head_sha": SHA, "status": "completed", "conclusion": "success",
        "steps": [step("Gate shard"), step("Generate shard outputs"),
                  step("Confirm provider-only source degradation", "skipped"),
                  step("Upload shard to private R2 handoff")],
    }


def page(*jobs):
    return {"total_count": len(jobs), "jobs": list(jobs)}


class FakeAPI:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.elapsed = 0
        self.delays = []

    def __call__(self, endpoint, timeout):
        self.calls.append((endpoint, timeout))
        expected_path, response = self.responses.pop(0)
        if endpoint != expected_path:
            raise AssertionError(f"Unexpected request: {endpoint}")
        if isinstance(response, Exception):
            raise response
        return copy.deepcopy(response)

    def sleep(self, delay):
        self.delays.append(delay)
        self.elapsed += delay

    def run(self, **kwargs):
        with contextlib.redirect_stderr(io.StringIO()):
            return evaluate_live(REPOSITORY, kwargs.pop("expected_shards", 1), RUN_ID, SHA,
                                 kwargs.pop("selected_count", 5), api=self,
                                 monotonic=lambda: self.elapsed, sleep=self.sleep, **kwargs)


class LiveSourceStatusTests(unittest.TestCase):
    def test_complete_list_needs_no_extra_api_calls(self):
        api = FakeAPI([(LIST_PATH, page(shard()))])
        self.assertTrue(api.run()["primary_ready"])
        self.assertEqual(len(api.calls), 1)
        self.assertFalse(api.delays)

    def test_missing_list_steps_are_hydrated_from_exact_job(self):
        listed = shard()
        listed.pop("steps")
        api = FakeAPI([(LIST_PATH, page(listed)),
                       (f"repos/{REPOSITORY}/actions/jobs/100", shard())])
        self.assertEqual(api.run(), {"primary_ready": True, "degraded_shards": 0,
                                     "provider_only": False, "no_work": False})
        self.assertFalse(api.delays)

    def test_empty_detail_retries_until_steps_are_visible(self):
        listed = shard()
        listed["steps"] = []
        api = FakeAPI([(LIST_PATH, page(listed)),
                       (f"repos/{REPOSITORY}/actions/jobs/100", listed),
                       (LIST_PATH, page(shard()))])
        self.assertTrue(api.run()["primary_ready"])
        self.assertEqual(api.delays, [5])

    def test_pending_step_is_hydrated_before_acceptance(self):
        listed = shard()
        listed["steps"][-1]["status"] = "in_progress"
        api = FakeAPI([(LIST_PATH, page(listed)),
                       (f"repos/{REPOSITORY}/actions/jobs/100", shard())])
        self.assertTrue(api.run()["primary_ready"])
        self.assertEqual(len(api.calls), 2)

    def test_missing_shard_inventory_retries(self):
        api = FakeAPI([(LIST_PATH, page(shard())),
                       (LIST_PATH, page(shard(), shard(1)))])
        self.assertTrue(api.run(expected_shards=2)["primary_ready"])
        self.assertEqual(api.delays, [5])

    def test_persistent_missing_steps_hits_deadline_and_never_accepts(self):
        listed = shard()
        listed["steps"] = []
        responses = [(LIST_PATH, page(listed)),
                     (f"repos/{REPOSITORY}/actions/jobs/100", listed)] * 2
        api = FakeAPI(responses)
        with self.assertRaisesRegex(TimeoutError, "evidence unavailable after 12s"):
            api.run(timeout=12)
        self.assertEqual(api.delays, [5, 7])
        self.assertEqual(api.elapsed, 12)
        self.assertEqual([timeout for _, timeout in api.calls], [12, 12, 7, 7])

    def test_wrong_run_sha_or_job_identity_cannot_be_retried_into_success(self):
        for key, wrong in (("id", 101), ("run_id", int(RUN_ID) + 1),
                           ("head_sha", "b" * 40), ("name", "process-shard (1)")):
            with self.subTest(key=key):
                listed, detail = shard(), shard()
                listed["steps"] = []
                detail[key] = wrong
                api = FakeAPI([(LIST_PATH, page(listed)),
                               (f"repos/{REPOSITORY}/actions/jobs/100", detail)])
                with self.assertRaisesRegex(ValueError, "detail identity differs"):
                    api.run()
                self.assertFalse(api.delays)

    def test_duplicate_or_foreign_shards_fail_without_polling(self):
        foreign = shard()
        foreign["run_id"] += 1
        for jobs in (page(shard(), shard()), page(foreign), page(shard(1))):
            with self.subTest(jobs=jobs):
                api = FakeAPI([(LIST_PATH, jobs)])
                with self.assertRaisesRegex(ValueError, "shard identity differs"):
                    api.run()
                self.assertFalse(api.delays)

    def test_successful_job_with_failed_generation_remains_degraded(self):
        failed = shard()
        failed["steps"][1]["conclusion"] = "failure"
        failed["steps"][-1]["conclusion"] = "skipped"
        api = FakeAPI([(LIST_PATH, page(failed))])
        self.assertEqual(api.run(), {"primary_ready": False, "degraded_shards": 1,
                                     "provider_only": False, "no_work": False})

    def test_provider_only_recovery_requires_exact_proof(self):
        failed = shard()
        failed["steps"][1]["conclusion"] = "failure"
        failed["steps"][2]["conclusion"] = "success"
        failed["steps"][-1]["conclusion"] = "skipped"
        api = FakeAPI([(LIST_PATH, page(failed))])
        self.assertEqual(api.run(), {"primary_ready": False, "degraded_shards": 1,
                                     "provider_only": True, "no_work": False})

    def test_no_work_still_requires_clean_gate_and_skipped_generation(self):
        empty = shard()
        empty["steps"][1]["conclusion"] = "skipped"
        empty["steps"][-1]["conclusion"] = "skipped"
        api = FakeAPI([(LIST_PATH, page(empty))])
        self.assertTrue(api.run(selected_count=0)["no_work"])
        api = FakeAPI([(LIST_PATH, page(shard()))])
        with self.assertRaisesRegex(ValueError, "clean no-op"):
            api.run(selected_count=0)

    def test_temporary_api_failure_is_retried_with_bounded_requests(self):
        api = FakeAPI([(LIST_PATH, JobsPending("temporary timeout")),
                       (LIST_PATH, page(shard()))])
        self.assertTrue(api.run()["primary_ready"])
        self.assertEqual(api.delays, [5])
        self.assertTrue(all(timeout <= 20 for _, timeout in api.calls))

    def test_authentication_failure_is_not_retried(self):
        api = FakeAPI([(LIST_PATH, ValueError("GitHub jobs request was denied or not found"))])
        with self.assertRaisesRegex(ValueError, "denied"):
            api.run()
        self.assertFalse(api.delays)

    def test_offline_cli_keeps_exact_github_output_format(self):
        with tempfile.TemporaryDirectory() as directory:
            saved = Path(directory) / "jobs.json"
            saved.write_text(json.dumps(page(shard())), encoding="utf-8")
            result = subprocess.run([sys.executable, str(Path(__file__).with_name("daily_market_source_status.py")),
                                     "--jobs", str(saved), "--expected-shards", "1", "--selected-count", "5",
                                     "--run-id", RUN_ID, "--execution-sha", SHA],
                                    check=True, capture_output=True, text=True)
        self.assertEqual(result.stdout, "primary_ready=true\ndegraded_shards=0\nprovider_only=false\nno_work=false\n")
        self.assertEqual(result.stderr, "")

    def test_workflow_uses_live_evidence_with_deadline_inside_job_timeout(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml").read_text()
        block = workflow.split("  source-outcome:\n", 1)[1].split("  package-publish-ready:\n", 1)[0]
        self.assertIn("timeout-minutes: 5", block)
        self.assertIn('--repository "$GITHUB_REPOSITORY" --timeout 180 --poll-interval 5', block)
        self.assertNotIn('gh api "repos/', block)


class GitHubRequestTests(unittest.TestCase):
    def test_timeout_is_retryable_without_command_output(self):
        with patch("daily_market_source_status.subprocess.run", side_effect=subprocess.TimeoutExpired("gh", 3)):
            with self.assertRaisesRegex(JobsPending, "timed out"):
                github_json(LIST_PATH, 3)

    def test_permissions_are_terminal_but_5xx_is_retryable(self):
        for code, expected in ((403, ValueError), (503, JobsPending)):
            response = subprocess.CompletedProcess([], 1, "", f"gh: request failed (HTTP {code})")
            with self.subTest(code=code), patch("daily_market_source_status.subprocess.run", return_value=response):
                with self.assertRaises(expected):
                    github_json(LIST_PATH, 3)

    def test_403_rate_limits_retry_without_exposing_response(self):
        for message in ("API rate limit exceeded", "secondary rate limit", "abuse detection mechanism"):
            response = subprocess.CompletedProcess([], 1, "", f"gh: {message}: private detail (HTTP 403)")
            with self.subTest(message=message), patch("daily_market_source_status.subprocess.run", return_value=response):
                with self.assertRaisesRegex(JobsPending, "rate limited") as error:
                    github_json(LIST_PATH, 3)
                self.assertNotIn("private detail", str(error.exception))


if __name__ == "__main__":
    unittest.main()
