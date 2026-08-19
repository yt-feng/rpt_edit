#!/usr/bin/env python3
"""Regression tests for the local Nutstore Ops cleanup."""

from __future__ import annotations

import tempfile
import unittest
from datetime import date, datetime
from pathlib import Path
from unittest.mock import patch

import cleanup_local_nutstore_ops as cleanup


class CleanupPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        # macOS exposes /var through /private/var; normalize the temporary root
        # so the production path-resolution guard remains exercised in tests.
        self.root = Path(self.temp_dir.name).resolve()
        self.kcdesk = self.root / "Nutstore" / "KCdesk" / "Ops"
        self.portal = self.root / "Nutstore" / "Portal Suite" / "Ops"
        self.trash = self.root / ".Trash"
        self.kcdesk.mkdir(parents=True)
        self.portal.mkdir(parents=True)
        self.trash.mkdir()

    def test_plan_keeps_today_and_previous_two_calendar_days(self) -> None:
        for name in (
            "2026-04-20",
            "2026-08-16",
            "2026-08-17",
            "2026-08-18",
            "2026-08-19",
            "2026-08-20",
            "notes",
        ):
            (self.kcdesk / name).mkdir()

        plan = cleanup.build_plan(
            self.kcdesk,
            self.portal,
            date(2026, 8, 19),
        )

        self.assertEqual(
            [path.name for path in plan.expired_dates],
            ["2026-04-20", "2026-08-16"],
        )
        self.assertEqual(plan.wrong_portal_ops, self.portal)

    def test_link_targets_are_skipped(self) -> None:
        expired = self.kcdesk / "2026-08-16"
        expired.mkdir()
        (expired / "linked").symlink_to(self.root, target_is_directory=True)
        (self.portal / "linked").symlink_to(self.root, target_is_directory=True)

        plan = cleanup.build_plan(
            self.kcdesk,
            self.portal,
            date(2026, 8, 19),
        )

        self.assertEqual(plan.expired_dates, ())
        self.assertIsNone(plan.wrong_portal_ops)
        self.assertEqual(len(plan.skipped), 2)

    def test_apply_moves_only_planned_directories_to_trash(self) -> None:
        expired = self.kcdesk / "2026-08-16"
        kept = self.kcdesk / "2026-08-17"
        expired.mkdir()
        kept.mkdir()
        (expired / "old.mp4").write_bytes(b"old")
        (self.portal / "wrong.mp4").write_bytes(b"wrong")
        plan = cleanup.build_plan(
            self.kcdesk,
            self.portal,
            date(2026, 8, 19),
        )

        with patch.object(cleanup, "KCDESK_OPS", self.kcdesk):
            moved = cleanup.apply_plan(
                plan,
                self.trash,
                datetime(2026, 8, 19, 12, 0, 0),
            )

        self.assertEqual(len(moved), 2)
        self.assertFalse(expired.exists())
        self.assertTrue(kept.is_dir())
        self.assertFalse(self.portal.exists())
        self.assertTrue((moved[0] / "old.mp4").is_file())
        self.assertTrue((moved[1] / "wrong.mp4").is_file())


if __name__ == "__main__":
    unittest.main()
