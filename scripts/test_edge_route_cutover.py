#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import unittest
from unittest.mock import patch

import edge_route_cutover as cutover


class MigrateRouteCleanupTests(unittest.TestCase):
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
