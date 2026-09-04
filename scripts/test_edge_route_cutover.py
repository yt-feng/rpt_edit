#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import edge_route_cutover as cutover


class EdgeRouteCutoverTests(unittest.TestCase):
    def _curl_result(self, command: list[str], *, status: int, body: bytes) -> subprocess.CompletedProcess[str]:
        header_path = Path(command[command.index("--dump-header") + 1])
        body_path = Path(command[command.index("--output") + 1])
        header_path.write_bytes(
            f"HTTP/2 {status}\r\nContent-Type: application/json\r\nX-Origin-Class: edge-static\r\n\r\n".encode()
        )
        body_path.write_bytes(body)
        return subprocess.CompletedProcess(command, 0, stdout=str(status), stderr="")

    def test_live_head_check_uses_curl_without_custom_headers(self) -> None:
        def run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
            return self._curl_result(command, status=200, body=b"curl may mirror HEAD headers here")

        with patch.object(cutover.subprocess, "run", side_effect=run) as curl:
            status, _headers, body = cutover.request_status("https://portal.example.invalid/")

        self.assertEqual(status, 200)
        self.assertEqual(body, b"")
        command = curl.call_args.args[0]
        self.assertEqual(command[0], "curl")
        self.assertIn("--head", command)
        self.assertNotIn("--location", command)
        self.assertNotIn("--header", command)
        self.assertNotIn("--max-filesize", command)
        self.assertEqual(command[-2:], ["--", "https://portal.example.invalid/"])
        self.assertEqual(curl.call_args.kwargs["timeout"], 35)

    def test_live_check_preserves_range_header(self) -> None:
        def run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
            return self._curl_result(command, status=206, body=b"payload")

        with patch.object(cutover.subprocess, "run", side_effect=run) as curl:
            status, headers, body = cutover.request_status(
                "https://portal.example.invalid/data/search_index.json",
                method="GET",
                headers={"Range": "bytes=0-1023"},
            )

        self.assertEqual(status, 206)
        self.assertEqual(body, b"payload")
        self.assertEqual(headers["content-type"], "application/json")
        self.assertEqual(headers["x-origin-class"], "edge-static")
        command = curl.call_args.args[0]
        range_index = command.index("--header")
        self.assertEqual(command[range_index + 1], "Range: bytes=0-1023")
        self.assertNotIn("--head", command)
        self.assertNotIn("--max-filesize", command)

    def test_curl_header_parser_uses_the_final_response_block(self) -> None:
        headers = cutover.parse_curl_headers(
            b"HTTP/1.1 200 Connection established\r\nProxy-Agent: test\r\n\r\n"
            b"HTTP/2 404\r\nContent-Type: text/html\r\nX-Origin-Class: edge-static\r\n\r\n"
        )

        self.assertEqual(
            headers,
            {
                "content-type": "text/html",
                "x-origin-class": "edge-static",
            },
        )

    def test_http_error_status_is_preserved_for_verification(self) -> None:
        def run(command: list[str], **_kwargs: object) -> subprocess.CompletedProcess[str]:
            return self._curl_result(command, status=403, body=b"Forbidden")

        with patch.object(cutover.subprocess, "run", side_effect=run) as curl:
            status, _headers, body = cutover.request_status("https://portal.example.invalid/")

        self.assertEqual(status, 403)
        self.assertEqual(body, b"")
        self.assertNotIn("--fail", curl.call_args.args[0])

    def test_curl_transport_failure_maps_to_unreachable_status(self) -> None:
        completed = subprocess.CompletedProcess([], 28, stdout="000", stderr="timeout")
        with patch.object(cutover.subprocess, "run", return_value=completed):
            self.assertEqual(
                cutover.request_status("https://portal.example.invalid/"),
                (0, {}, b""),
            )

    def test_verify_mode_uses_live_checks_without_cloud_route_permissions(self) -> None:
        with (
            patch.object(sys, "argv", ["edge_route_cutover.py", "verify"]),
            patch.dict(os.environ, {
                "SITE_HOST": "portal.example.invalid",
                "EDGE_SCRIPT_NAME": "svc-neutral",
                "EDGE_ALIAS_HOSTS": "www.portal.example.invalid",
                "EDGE_VERIFY_ATTEMPTS": "4",
                "EDGE_VERIFY_CONSECUTIVE": "2",
            }, clear=False),
            patch.object(cutover, "wait_for_public_routes", return_value=True) as wait_for_routes,
            patch.object(cutover, "find_zone_id") as find_zone_id,
        ):
            self.assertEqual(cutover.run(), 0)

        wait_for_routes.assert_called_once_with(
            "https://portal.example.invalid",
            ["www.portal.example.invalid"],
            attempts=4,
            consecutive=2,
        )
        find_zone_id.assert_not_called()

    def test_existing_route_is_never_deleted_when_verification_fails(self) -> None:
        route = {"id": "route-id", "script": "svc-neutral"}
        with (
            patch.object(cutover, "exact_route", return_value=route),
            patch.object(cutover, "wait_for_edge", return_value=False),
            patch.object(cutover, "delete_edge_route") as delete_route,
        ):
            with self.assertRaisesRegex(cutover.CutoverError, "edge_verify"):
                cutover.migrate("zone-id", "portal.example.invalid/*", "https://portal.example.invalid", "svc-neutral")

        delete_route.assert_not_called()

    def test_new_route_is_deleted_when_verification_fails(self) -> None:
        with (
            patch.object(cutover, "exact_route", return_value=None),
            patch.object(cutover, "api_json", return_value={"id": "route-id"}),
            patch.object(cutover, "wait_for_edge", side_effect=[False, True]),
            patch.object(cutover, "delete_edge_route") as delete_route,
        ):
            with self.assertRaisesRegex(cutover.CutoverError, "edge_verify"):
                cutover.migrate("zone-id", "portal.example.invalid/*", "https://portal.example.invalid", "svc-neutral")

        delete_route.assert_called_once_with("zone-id", "portal.example.invalid/*", "svc-neutral")

    def test_alias_route_verifies_all_bare_public_paths(self) -> None:
        def response(url: str, *, method: str) -> tuple[int, dict[str, str], bytes]:
            self.assertIn(method, {"GET", "HEAD"})
            path = url.removeprefix("https://www.portal.example.invalid")
            return (
                301,
                {
                    "x-origin-class": "edge-static",
                    "location": "https://portal.example.invalid" + path,
                    "cache-control": "no-store",
                    "cloudflare-cdn-cache-control": "no-store",
                    "cf-cache-status": "BYPASS",
                },
                b"",
            )

        with patch.object(cutover, "request_status", side_effect=response) as request_status:
            self.assertTrue(cutover.verify_alias(
                "https://www.portal.example.invalid",
                "https://portal.example.invalid",
            ))
        self.assertEqual(
            request_status.call_args_list,
            [
                unittest.mock.call("https://www.portal.example.invalid" + path, method=method)
                for path in cutover.ALIAS_REDIRECT_PATHS
                for method in ("GET", "HEAD")
            ],
        )

    def test_alias_route_rejects_cached_bare_200(self) -> None:
        with patch.object(
            cutover,
            "request_status",
            return_value=(200, {"x-origin-class": "edge-static"}, b""),
        ) as request_status:
            self.assertFalse(cutover.verify_alias(
                "https://www.portal.example.invalid",
                "https://portal.example.invalid",
            ))

        request_status.assert_called_once_with(
            "https://www.portal.example.invalid/",
            method="GET",
        )
        self.assertIn("status=200 expected=301", cutover.LAST_VERIFY_FAILURE)

    def test_alias_route_rejects_wrong_location(self) -> None:
        with patch.object(
            cutover,
            "request_status",
            return_value=(
                301,
                {
                    "x-origin-class": "edge-static",
                    "location": "https://portal.example.invalid/wrong",
                    "cache-control": "no-store",
                    "cloudflare-cdn-cache-control": "no-store",
                },
                b"",
            ),
        ):
            self.assertFalse(cutover.verify_alias(
                "https://www.portal.example.invalid",
                "https://portal.example.invalid",
            ))

        self.assertIn("location=", cutover.LAST_VERIFY_FAILURE)
        self.assertIn("expected='https://portal.example.invalid/'", cutover.LAST_VERIFY_FAILURE)

    def test_alias_route_rejects_cacheable_or_cached_redirects(self) -> None:
        base_headers = {
            "x-origin-class": "edge-static",
            "location": "https://portal.example.invalid/",
            "cloudflare-cdn-cache-control": "no-store",
        }
        with patch.object(
            cutover,
            "request_status",
            return_value=(301, {**base_headers, "cache-control": "public, max-age=60"}, b""),
        ):
            self.assertFalse(cutover.verify_alias(
                "https://www.portal.example.invalid",
                "https://portal.example.invalid",
            ))
        self.assertIn("redirect_not_no_store", cutover.LAST_VERIFY_FAILURE)

        with patch.object(
            cutover,
            "request_status",
            return_value=(301, {
                **base_headers,
                "cache-control": "no-store",
                "cf-cache-status": "HIT",
            }, b""),
        ):
            self.assertFalse(cutover.verify_alias(
                "https://www.portal.example.invalid",
                "https://portal.example.invalid",
            ))
        self.assertIn("unexpected_cache_status=hit", cutover.LAST_VERIFY_FAILURE)

    def test_canonical_route_rejects_shared_cache_hit_before_other_checks(self) -> None:
        with patch.object(
            cutover,
            "request_status",
            return_value=(200, {
                "content-type": "text/html",
                "x-origin-class": "edge-static",
                "cloudflare-cdn-cache-control": "no-store",
                "cf-cache-status": "HIT",
            }, b"home"),
        ) as request_status:
            self.assertFalse(cutover.verify_edge("https://portal.example.invalid"))
        request_status.assert_called_once_with("https://portal.example.invalid/", method="GET")
        self.assertIn("unexpected_cache_status=hit", cutover.LAST_VERIFY_FAILURE)

    def test_public_route_gate_requires_consecutive_cross_host_successes(self) -> None:
        request_order: list[str] = []

        def verify_edge(_origin: str) -> bool:
            request_order.append("apex")
            return True

        alias_results = iter((True, False, True, True))

        def verify_alias(_alias_origin: str, _canonical_origin: str) -> bool:
            request_order.append("alias")
            return next(alias_results)

        with (
            patch.object(cutover, "verify_edge", side_effect=verify_edge) as verify_edge_mock,
            patch.object(cutover, "verify_alias", side_effect=verify_alias) as verify_alias_mock,
            patch.object(cutover.time, "sleep"),
        ):
            self.assertTrue(cutover.wait_for_public_routes(
                "https://portal.example.invalid",
                ["www.portal.example.invalid"],
                attempts=4,
                consecutive=2,
            ))
        self.assertEqual(verify_edge_mock.call_count, 4)
        self.assertEqual(verify_alias_mock.call_count, 4)
        self.assertEqual(
            request_order,
            ["alias", "apex", "apex", "alias", "alias", "apex", "apex", "alias"],
        )

    def test_migrate_mode_manages_canonical_and_alias_routes(self) -> None:
        with (
            patch.object(sys, "argv", ["edge_route_cutover.py", "migrate"]),
            patch.dict(os.environ, {
                "SITE_HOST": "portal.example.invalid",
                "EDGE_SCRIPT_NAME": "svc-neutral",
                "EDGE_ALIAS_HOSTS": "www.portal.example.invalid",
            }, clear=False),
            patch.object(cutover, "find_zone_id", return_value="zone-id"),
            patch.object(cutover, "migrate") as migrate,
            patch.object(cutover, "migrate_alias") as migrate_alias,
        ):
            self.assertEqual(cutover.run(), 0)

        migrate.assert_called_once_with(
            "zone-id",
            "portal.example.invalid/*",
            "https://portal.example.invalid",
            "svc-neutral",
        )
        migrate_alias.assert_called_once_with(
            "zone-id",
            "www.portal.example.invalid/*",
            "https://www.portal.example.invalid",
            "https://portal.example.invalid",
            "svc-neutral",
        )

    def test_refresh_workflow_gates_on_bare_alias_verification_before_and_after_deploy(self) -> None:
        workflow = (
            Path(__file__).resolve().parent.parent
            / ".github"
            / "workflows"
            / "neutral-edge-cutover.yml"
        ).read_text(encoding="utf-8")
        deploy_name = "      - name: Deploy prepared neutral edge release\n"
        verify_name = "      - name: Accept prepared release through the live edge\n"
        preflight_name = "      - name: Gate preparation on stable live routes\n"
        upload_name = "      - name: Upload inactive static slot and immutable runtime\n"
        deploy_start = workflow.index(deploy_name)
        verify_start = workflow.index(verify_name)
        preflight_start = workflow.index(preflight_name)
        upload_start = workflow.index(upload_name)
        self.assertLess(preflight_start, upload_start)
        self.assertLess(deploy_start, verify_start)
        verify_step = workflow[verify_start:]
        self.assertIn("python3 -B scripts/edge_route_cutover.py verify", verify_step)
        self.assertIn("EDGE_VERIFY_CONSECUTIVE: \"3\"", workflow[preflight_start:upload_start])
        self.assertIn("enabled = false", workflow)
        self.assertIn("Roll back failed release or completed rehearsal", workflow)
        self.assertIn("Verify exact previous release after rollback", workflow)
        self.assertNotIn("Purge previous public edge cache", workflow)
        self.assertNotIn("edge_route_cutover.py purge", workflow)
        self.assertNotIn("inputs.operation == 'switch'", workflow)
        self.assertNotIn("edge_route_cutover.py migrate", workflow)
        self.assertNotIn("edge_route_cutover.py rollback", workflow)

    def test_static_refresh_trigger_restores_gated_schedule_and_manual_migrate(self) -> None:
        workflow = (
            Path(__file__).resolve().parent.parent
            / ".github"
            / "workflows"
            / "neutral-edge-cutover.yml"
        ).read_text(encoding="utf-8")
        trigger = workflow[: workflow.index("\npermissions:\n")]
        self.assertIn("schedule:", trigger)
        self.assertIn('cron: "30 1,5,9,13 * * *"', trigger)
        self.assertIn("workflow_run:", trigger)
        self.assertRegex(trigger, r"(?m)^\s+- migrate\s*$")
        self.assertRegex(trigger, r"(?m)^\s+- rehearse\s*$")
        self.assertRegex(trigger, r"(?m)^\s+- locale-shadow\s*$")
        self.assertNotRegex(trigger, r"(?m)^\s+- switch\s*$")
        self.assertNotRegex(trigger, r"(?m)^\s+- rollback\s*$")
        self.assertNotRegex(trigger, r"(?m)^\s+- inspect-source\s*$")
        self.assertIn("Require reviewed main operation", workflow)
        self.assertIn("vars.NEUTRAL_SCHEDULE_ENABLED == 'true'", workflow)
        self.assertIn('rehearse|locale-shadow|migrate) operation="$REQUESTED_OPERATION"', workflow)
        self.assertIn("--write-current-manifest _neutral_site/data/release-semantics.json", workflow)
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("persist-credentials: false", workflow)


if __name__ == "__main__":
    unittest.main()
