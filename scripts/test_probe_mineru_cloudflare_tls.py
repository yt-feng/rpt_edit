#!/usr/bin/env python3
"""Offline lifecycle mocks and real Worker-handler calls with mocked fetch."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import unittest
from unittest.mock import patch

import requests

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("probe_mineru_cloudflare_tls", ROOT / "scripts/probe_mineru_cloudflare_tls.py")
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)
ENV = {
    "GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": "workflow_dispatch",
    "GITHUB_REF": "refs/heads/main", "GITHUB_REPOSITORY": "example/research",
    "GITHUB_WORKFLOW_REF": "example/research/.github/workflows/mineru-cloudflare-tls-probe.yml@refs/heads/main",
    "GITHUB_RUN_ID": "123456", "GITHUB_RUN_ATTEMPT": "1", "GITHUB_SHA": "c" * 40,
    "CLOUDFLARE_ACCOUNT_ID": "a" * 32, "CLOUDFLARE_API_TOKEN": "never-print-this-api-token",
}
BODY = {
    "schema_version": 1, "provider_host": "cdn-mineru.openxlab.org.cn",
    "request_method": "HEAD", "request_count": 1, "redirects_followed": 0,
    "zip_downloads": 0, "provider_posts": 0, "category": "https_response_received",
    "upstream_http_status": 403, "colo": "CDG", "elapsed_ms": 12,
}


class Response:
    def __init__(self, status=200, body=None, raw=None):
        self.status_code = status
        self.data = raw if raw is not None else json.dumps(body).encode()
        self.closed = False

    def iter_content(self, chunk_size):
        for start in range(0, len(self.data), chunk_size):
            yield self.data[start:start + chunk_size]

    def close(self):
        self.closed = True


def ok(result=None):
    return Response(body={"success": True, "result": result if result is not None else {}})


def absent():
    return Response(404, {"success": False, "errors": [{"code": 10007, "message": "No such script"}]})


def sequence(body=None):
    return [ok({"subdomain": "existing-account"}), absent(), ok(), ok(), Response(body=body or BODY), ok()]


class Session:
    def __init__(self, results):
        self.results = list(results)
        self.calls = []

    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        result = self.results.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


class LifecycleTests(unittest.TestCase):
    def run_with(self, results, env=None):
        session = Session(results)
        with patch.object(probe.secrets, "token_hex", side_effect=["0123abcd", "e" * 64]):
            result = probe.run_probe(env or dict(ENV), session)
        return result, session

    def test_complete_probe_deletes_only_created_worker(self):
        result, session = self.run_with(sequence())
        self.assertEqual(result["category"], "https_response_received")
        self.assertTrue(result["worker_deleted"])
        self.assertEqual(result["cloudflare_api_calls"], 5)
        self.assertEqual(result["worker_calls"], 1)
        self.assertEqual([call[0] for call in session.calls], ["GET", "GET", "PUT", "POST", "GET", "DELETE"])
        script = "/workers/scripts/mineru-result-tls-probe-123456-1-0123abcd"
        self.assertTrue(session.calls[-1][1].endswith(script))
        self.assertNotIn("preserved_worker_name_sha256", result)

    def test_all_transports_strict_no_redirect_no_retry(self):
        _, session = self.run_with(sequence())
        for _, url, options in session.calls:
            self.assertTrue(url.startswith("https://"))
            self.assertIs(options["verify"], True)
            self.assertIs(options["allow_redirects"], False)
            self.assertEqual(options["timeout"], (5, 20))
        self.assertEqual(len(session.calls), 6)

    def test_upload_is_module_with_only_one_ephemeral_secret(self):
        result, session = self.run_with(sequence())
        metadata = json.loads(session.calls[2][2]["files"]["metadata"][1])
        self.assertEqual(metadata["main_module"], "index.js")
        self.assertEqual(metadata["bindings"], [{"type": "secret_text", "name": "PROBE_TOKEN", "text": "e" * 64}])
        self.assertIn("no_cots_on_external_fetch", metadata["compatibility_flags"])
        self.assertIn("global_fetch_strictly_public", metadata["compatibility_flags"])
        self.assertFalse(metadata["observability"]["enabled"])
        self.assertEqual(session.calls[3][2]["json"], {"enabled": True, "previews_enabled": False})
        encoded = json.dumps(result)
        self.assertNotIn(ENV["CLOUDFLARE_API_TOKEN"], encoded)
        self.assertNotIn("e" * 64, encoded)
        self.assertNotIn("existing-account", encoded)

    def test_main_manual_only_is_runtime_enforced(self):
        for key, value in [("GITHUB_ACTIONS", "false"), ("GITHUB_EVENT_NAME", "pull_request"),
                           ("GITHUB_REF", "refs/heads/test"), ("GITHUB_REPOSITORY", "other/repo"),
                           ("GITHUB_WORKFLOW_REF", "example/research/.github/workflows/other.yml@refs/heads/main"),
                           ("GITHUB_WORKFLOW_REF", "")]:
            with self.subTest(key=key):
                env = {**ENV, key: value}
                result, session = self.run_with([], env)
                self.assertEqual(result["category"], "main_manual_action_required")
                self.assertEqual(session.calls, [])

    def test_invalid_config_never_calls_api(self):
        for key, value in [("CLOUDFLARE_ACCOUNT_ID", "bad/path"), ("CLOUDFLARE_API_TOKEN", ""),
                           ("GITHUB_RUN_ID", "../../production"), ("GITHUB_RUN_ATTEMPT", ""), ("GITHUB_SHA", "short")]:
            with self.subTest(key=key):
                result, session = self.run_with([], {**ENV, key: value})
                self.assertEqual(result["category"], "invalid_action_configuration")
                self.assertEqual(session.calls, [])

    def test_missing_account_subdomain_never_creates_one(self):
        result, session = self.run_with([ok({})])
        self.assertEqual(result["category"], "existing_subdomain_required")
        self.assertEqual(len(session.calls), 1)
        self.assertFalse(result["worker_created"])

    def test_existing_script_never_updated_or_deleted(self):
        result, session = self.run_with([ok({"subdomain": "existing-account"}), ok()])
        self.assertEqual(result["category"], "new_worker_absence_unconfirmed")
        self.assertEqual([call[0] for call in session.calls], ["GET", "GET"])

    def test_generic_404_does_not_authorize_create(self):
        result, session = self.run_with([ok({"subdomain": "existing-account"}), Response(404, {"success": False, "errors": [{"code": 999}]})])
        self.assertEqual(result["category"], "new_worker_absence_unconfirmed")
        self.assertEqual(len(session.calls), 2)

    def test_upload_unknown_ack_not_retried_or_deleted(self):
        result, session = self.run_with([ok({"subdomain": "existing-account"}), absent(), requests.Timeout("secret-url")])
        self.assertEqual(result["category"], "request_timeout")
        self.assertEqual(result["cleanup_category"], "creation_not_acknowledged")
        self.assertEqual(len(session.calls), 3)
        self.assertEqual(len(result["preserved_worker_name_sha256"]), 64)
        self.assertNotIn("secret-url", json.dumps(result))

    def test_subdomain_enable_failure_still_cleans_up(self):
        rows = sequence()
        rows[3] = Response(403, {"success": False, "errors": [{"code": 10000, "message": "secret account data"}]})
        result, session = self.run_with(rows[:4] + [ok()])
        self.assertEqual(result["category"], "cloudflare_api_rejected")
        self.assertEqual(result["cloudflare_error_codes"], [10000])
        self.assertEqual(result["stage"], "enable_temporary_worker")
        self.assertTrue(result["worker_deleted"])
        self.assertNotIn("secret account data", json.dumps(result))
        self.assertEqual(session.calls[-1][0], "DELETE")

    def test_526_summary_is_not_reported_as_download_success(self):
        result, _ = self.run_with(sequence({**BODY, "upstream_http_status": 526, "category": "tls_invalid_certificate"}))
        self.assertEqual(result["category"], "tls_invalid_certificate")
        self.assertEqual(result["zip_downloads"], 0)
        self.assertEqual(result["r2_writes"], 0)
        self.assertTrue(result["worker_deleted"])

    def test_fetch_exception_is_indeterminate_and_cleans_up(self):
        result, _ = self.run_with(sequence({**BODY, "upstream_http_status": None, "category": "fetch_failed"}))
        self.assertEqual(result["category"], "fetch_failed")
        self.assertTrue(result["worker_deleted"])

    def test_edge_5xx_not_misclassified_as_origin_https_success(self):
        result, _ = self.run_with(sequence({**BODY, "upstream_http_status": 530, "category": "upstream_http_error"}))
        self.assertEqual(result["category"], "upstream_http_error")
        self.assertTrue(result["worker_deleted"])

    def test_probe_endpoint_tls_error_is_sanitized_and_cleans_up(self):
        rows = sequence()
        rows[4] = requests.exceptions.SSLError("secret-url-token")
        result, _ = self.run_with(rows)
        self.assertEqual(result["category"], "tls_verification_failed")
        self.assertTrue(result["worker_deleted"])
        self.assertNotIn("secret-url-token", json.dumps(result))

    def test_worker_http_error_cleans_up(self):
        rows = sequence()
        rows[4] = Response(404, {"secret": "upstream URL"})
        result, _ = self.run_with(rows)
        self.assertEqual(result["category"], "worker_http_rejected")
        self.assertTrue(result["worker_deleted"])
        self.assertNotIn("upstream URL", json.dumps(result))

    def test_cleanup_failure_preserves_only_name_hash(self):
        rows = sequence()
        rows[-1] = requests.ConnectionError("private API URL")
        result, session = self.run_with(rows)
        self.assertEqual(result["category"], "https_response_received")
        self.assertFalse(result["worker_deleted"])
        self.assertEqual(result["cleanup_category"], "request_failed")
        self.assertEqual(len(result["preserved_worker_name_sha256"]), 64)
        self.assertEqual(len(session.calls), 6)
        self.assertNotIn("private API URL", json.dumps(result))
        self.assertNotIn("mineru-result-tls-probe-123456", json.dumps(result))

    def test_invalid_probe_or_extra_fields_never_escape(self):
        for body in [{**BODY, "request_count": 2}, {**BODY, "upstream_http_status": 526},
                     {**BODY, "schema_version": True}, {**BODY, "colo": "secret-string"},
                     {**BODY, "elapsed_ms": -1}]:
            with self.subTest(body=body):
                result, _ = self.run_with(sequence(body))
                self.assertEqual(result["category"], "invalid_probe_summary")
                self.assertTrue(result["worker_deleted"])
        result, _ = self.run_with(sequence({**BODY, "private_url": "secret"}))
        self.assertNotIn("private_url", json.dumps(result))
        self.assertNotIn("secret", json.dumps(result))

    def test_response_limit_still_cleans_up(self):
        rows = sequence()
        rows[4] = Response(raw=b"x" * (probe.MAX_RESPONSE_BYTES + 1))
        result, _ = self.run_with(rows)
        self.assertEqual(result["category"], "response_too_large")
        self.assertTrue(result["worker_deleted"])

    def test_invalid_json_still_cleans_up(self):
        rows = sequence()
        rows[4] = Response(raw=b"not JSON secret")
        result, _ = self.run_with(rows)
        self.assertEqual(result["category"], "invalid_response")
        self.assertTrue(result["worker_deleted"])

    def test_workflow_has_no_production_r2_or_schedule_and_tests_before_probe(self):
        workflow = (ROOT / ".github/workflows/mineru-cloudflare-tls-probe.yml").read_text()
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", workflow)
        self.assertIn("needs: offline-tests", workflow)
        self.assertIn("if: always()", workflow)
        self.assertNotIn("schedule:", workflow)
        self.assertNotIn("R2_BUCKET_NAME", workflow)
        self.assertNotIn("R2_SECRET_ACCESS_KEY", workflow)


class WorkerHandlerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = shutil.which("node")
        if not cls.node:
            raise unittest.SkipTest("Node runtime unavailable for real Worker handler tests")

    def call_worker(self, *, method="GET", path="/probe", token="a" * 64,
                    env_token="a" * 64, upstream_status=403, throws=False):
        fixture = {"method": method, "path": path, "token": token, "env_token": env_token,
                   "upstream_status": upstream_status, "throws": throws}
        code = """
import fs from 'node:fs';
import {webcrypto} from 'node:crypto';
if (!globalThis.crypto) Object.defineProperty(globalThis, 'crypto', {value: webcrypto});
const fixture = JSON.parse(fs.readFileSync(0, 'utf8'));
const source = fs.readFileSync(process.argv[1], 'utf8');
const worker = (await import('data:text/javascript;base64,' + Buffer.from(source).toString('base64'))).default;
const calls = [];
globalThis.fetch = async (url, options) => {
  calls.push({url, method: options.method, redirect: options.redirect, cache: options.cache});
  if (fixture.throws) throw new Error('private secret URL');
  return new Response(null, {status: fixture.upstream_status});
};
const headers = fixture.token === null ? {} : {Authorization: 'Bearer ' + fixture.token};
const request = new Request('https://temporary.example.workers.dev' + fixture.path, {method: fixture.method, headers});
Object.defineProperty(request, 'cf', {value: {colo: 'CDG'}});
const response = await worker.fetch(request, {PROBE_TOKEN: fixture.env_token});
process.stdout.write(JSON.stringify({status: response.status, body: await response.json(), calls}));
"""
        result = subprocess.run([self.node, "--input-type=module", "-e", code, str(probe.WORKER_SOURCE)],
                                input=json.dumps(fixture), text=True, capture_output=True, timeout=10, check=True)
        return json.loads(result.stdout)

    def test_worker_uses_one_fixed_strict_https_head(self):
        result = self.call_worker()
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["calls"], [{"url": "https://cdn-mineru.openxlab.org.cn/", "method": "HEAD",
                                             "redirect": "manual", "cache": "no-store"}])
        self.assertEqual(result["body"]["category"], "https_response_received")
        self.assertEqual(result["body"]["zip_downloads"], 0)

    def test_worker_absent_or_wrong_secret_denies_without_fetch(self):
        for overrides in [{"env_token": None}, {"token": None}, {"token": "b" * 64}, {"token": "short"}]:
            with self.subTest(overrides=overrides):
                result = self.call_worker(**overrides)
                self.assertEqual(result["status"], 401)
                self.assertEqual(result["calls"], [])

    def test_worker_rejects_parameters_methods_or_other_paths(self):
        for overrides in [{"method": "POST"}, {"path": "/probe?url=https://example.com"}, {"path": "/other"}]:
            with self.subTest(overrides=overrides):
                result = self.call_worker(**overrides)
                self.assertEqual(result["status"], 404)
                self.assertEqual(result["calls"], [])

    def test_worker_526_and_fetch_errors_sanitized(self):
        result = self.call_worker(upstream_status=526)
        self.assertEqual(result["body"]["category"], "tls_invalid_certificate")
        self.assertEqual(len(result["calls"]), 1)
        result = self.call_worker(throws=True)
        self.assertEqual(result["body"]["category"], "fetch_failed")
        self.assertEqual(result["body"]["upstream_http_status"], None)
        self.assertNotIn("private secret", json.dumps(result))

    def test_worker_does_not_follow_redirects(self):
        result = self.call_worker(upstream_status=302)
        self.assertEqual(result["body"]["category"], "https_redirect_received")
        self.assertEqual(len(result["calls"]), 1)

    def test_worker_non_tls_5xx_is_indeterminate(self):
        result = self.call_worker(upstream_status=530)
        self.assertEqual(result["body"]["category"], "upstream_http_error")


if __name__ == "__main__":
    unittest.main()
