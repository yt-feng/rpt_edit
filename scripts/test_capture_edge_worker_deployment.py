#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/capture_edge_worker_deployment.py"
SPEC = importlib.util.spec_from_file_location("capture_edge_worker_deployment", SCRIPT)
assert SPEC and SPEC.loader
capture = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = capture
SPEC.loader.exec_module(capture)


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self, _limit: int = -1) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


class CaptureEdgeWorkerDeploymentTests(unittest.TestCase):
    def deployment(self, deployment_id: str, version_id: str, created_on: str) -> dict:
        return {
            "id": deployment_id,
            "created_on": created_on,
            "versions": [{"version_id": version_id, "percentage": 100}],
        }

    def test_selects_latest_single_version_deployment(self) -> None:
        older = self.deployment(
            "11111111-1111-4111-8111-111111111111",
            "22222222-2222-4222-8222-222222222222",
            "2026-08-29T00:00:00Z",
        )
        current = self.deployment(
            "33333333-3333-4333-8333-333333333333",
            "44444444-4444-4444-8444-444444444444",
            "2026-08-30T00:00:00Z",
        )
        self.assertEqual(
            capture.active_rollback_target([current, older]),
            (current["id"], current["versions"][0]["version_id"]),
        )

    def test_active_target_follows_api_order_not_timestamp_sorting(self) -> None:
        active = self.deployment(
            "33333333-3333-4333-8333-333333333333",
            "44444444-4444-4444-8444-444444444444",
            "2026-08-29T00:00:00Z",
        )
        newer_but_not_active = self.deployment(
            "55555555-5555-4555-8555-555555555555",
            "66666666-6666-4666-8666-666666666666",
            "2026-08-30T00:00:00Z",
        )
        self.assertEqual(
            capture.active_rollback_target([active, newer_but_not_active]),
            (active["id"], active["versions"][0]["version_id"]),
        )

    def test_rejects_gradual_or_malformed_deployment(self) -> None:
        with self.assertRaisesRegex(capture.CaptureError, "deployment_not_single_version"):
            capture.active_rollback_target([{
                "id": "33333333-3333-4333-8333-333333333333",
                "created_on": "2026-08-30T00:00:00Z",
                "versions": [
                    {"version_id": "44444444-4444-4444-8444-444444444444", "percentage": 50},
                    {"version_id": "55555555-5555-4555-8555-555555555555", "percentage": 50},
                ],
            }])

    def test_main_writes_only_opaque_rollback_ids(self) -> None:
        deployment = self.deployment(
            "33333333-3333-4333-8333-333333333333",
            "44444444-4444-4444-8444-444444444444",
            "2026-08-30T00:00:00Z",
        )

        def fake_urlopen(request, timeout):
            self.assertEqual(timeout, 30)
            self.assertIn("/workers/scripts/svc-neutral/deployments", request.full_url)
            self.assertEqual(request.headers["Authorization"], "Bearer secret-token")
            return FakeResponse({"success": True, "result": {"deployments": [deployment]}})

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "github-env"
            with (
                patch.dict(os.environ, {
                    "CLOUDFLARE_ACCOUNT_ID": "account-id",
                    "CLOUDFLARE_API_TOKEN": "secret-token",
                }, clear=True),
                patch.object(capture.urllib.request, "urlopen", side_effect=fake_urlopen),
            ):
                self.assertEqual(capture.main([
                    "--script-name", "svc-neutral",
                    "--output-env", str(output),
                ]), 0)
            self.assertEqual(
                output.read_text(encoding="utf-8"),
                "EDGE_PREVIOUS_DEPLOYMENT_ID=33333333-3333-4333-8333-333333333333\n"
                "EDGE_PREVIOUS_VERSION_ID=44444444-4444-4444-8444-444444444444\n",
            )

    def test_missing_credentials_fail_before_network(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            patch.dict(os.environ, {}, clear=True),
            patch.object(capture.urllib.request, "urlopen") as urlopen,
        ):
            self.assertEqual(capture.main([
                "--script-name", "svc-neutral",
                "--output-env", str(Path(directory) / "github-env"),
            ]), 2)
        urlopen.assert_not_called()

    def test_rejects_legacy_flat_result_shape(self) -> None:
        deployment = self.deployment(
            "33333333-3333-4333-8333-333333333333",
            "44444444-4444-4444-8444-444444444444",
            "2026-08-30T00:00:00Z",
        )
        with patch.object(
            capture.urllib.request,
            "urlopen",
            return_value=FakeResponse({"success": True, "result": [deployment]}),
        ):
            with self.assertRaisesRegex(capture.CaptureError, "deployment_shape"):
                capture.request_deployments("account-id", "svc-neutral", "secret-token")

    def test_expect_version_requires_the_active_version_to_match(self) -> None:
        deployment = self.deployment(
            "33333333-3333-4333-8333-333333333333",
            "44444444-4444-4444-8444-444444444444",
            "2026-08-30T00:00:00Z",
        )
        with (
            patch.dict(os.environ, {
                "CLOUDFLARE_ACCOUNT_ID": "account-id",
                "CLOUDFLARE_API_TOKEN": "secret-token",
            }, clear=True),
            patch.object(capture, "request_deployments", return_value=[deployment]),
        ):
            self.assertEqual(capture.main([
                "--script-name", "svc-neutral",
                "--expect-version", "44444444-4444-4444-8444-444444444444",
            ]), 0)
            self.assertEqual(capture.main([
                "--script-name", "svc-neutral",
                "--expect-version", "55555555-5555-4555-8555-555555555555",
            ]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
