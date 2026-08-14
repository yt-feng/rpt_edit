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
        size_index = command.index("--max-filesize")
        self.assertEqual(command[size_index + 1], "65536")

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
            patch.dict(os.environ, {"SITE_HOST": "portal.example.invalid", "EDGE_SCRIPT_NAME": "svc-neutral"}, clear=False),
            patch.object(cutover, "wait_for_edge", return_value=True) as wait_for_edge,
            patch.object(cutover, "find_zone_id") as find_zone_id,
        ):
            self.assertEqual(cutover.run(), 0)

        wait_for_edge.assert_called_once_with("https://portal.example.invalid", expected=True)
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


if __name__ == "__main__":
    unittest.main()
