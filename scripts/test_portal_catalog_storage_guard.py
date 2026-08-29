#!/usr/bin/env python3

from __future__ import annotations

import os
import re
import sys
import types
import unittest
from pathlib import Path
from unittest import mock

# Keep this focused unit test runnable in the lightweight local Python used by
# contributors; the guarded helpers do not make HTTP requests.
try:
    import requests  # noqa: F401
except ModuleNotFoundError:  # pragma: no cover - depends on local environment
    sys.modules["requests"] = types.ModuleType("requests")

# The deletion guard has no Dropbox or text-generation dependency. Stub those
# heavy sibling modules so the regression test stays self-contained.
build_catalog_stub = types.ModuleType("build_bank_report_catalog")
build_catalog_stub.DATE_FOLDER_RE = re.compile(r"^\d{6,8}$")
build_catalog_stub.DROPBOX_REQUEST_MAX_ATTEMPTS = 5
build_catalog_stub.TRANSIENT_DROPBOX_ERRORS = (ConnectionError, TimeoutError)
build_catalog_stub.detect_bank = lambda value: ("", "")
build_catalog_stub.dropbox_access_token = lambda: ""
build_catalog_stub.dropbox_post_with_retry = lambda *args, **kwargs: None
build_catalog_stub.dropbox_retry_delay = lambda attempt: 0.0
build_catalog_stub.latest_date_folders = lambda entries, days: []
build_catalog_stub.list_folder = lambda token, path, recursive=False: []
build_catalog_stub.sanitize_report_name = lambda value: value
sys.modules.setdefault("build_bank_report_catalog", build_catalog_stub)

finalize_outputs_stub = types.ModuleType("finalize_outputs")
finalize_outputs_stub.sanitize_text = lambda value: value
sys.modules.setdefault("finalize_outputs", finalize_outputs_stub)

import portal_suite_catalog as catalog


class FakeR2Client:
    def __init__(self, responses: list[dict] | None = None) -> None:
        self.calls: list[dict] = []
        self.responses = list(responses or [])

    def delete_objects(self, **kwargs: object) -> dict:
        self.calls.append(kwargs)
        return self.responses.pop(0) if self.responses else {}


class CatalogStorageGuardTests(unittest.TestCase):
    REPORT_A = "0123456789abcdef01234567"
    REPORT_B = "abcdef0123456789abcdef01"

    def test_storage_cleanup_is_disabled_without_explicit_opt_in(self) -> None:
        cleanup_limit = catalog.storage_cleanup_limit_bytes(7, False)
        self.assertEqual(cleanup_limit, 0)
        self.assertEqual(
            catalog.storage_cleanup_limit_bytes(7, True),
            7 * catalog.BYTES_PER_GIB,
        )
        active_catalog = {
            "items": [{
                "id": self.REPORT_A,
                "available": True,
                "r2_synced": True,
                "present_in_latest_scan": True,
                "date_folder": "260101",
                "size_bytes": 100,
            }],
        }
        archived, _before, after = catalog.apply_storage_limit(
            active_catalog,
            cleanup_limit,
            "2026-08-29 00:00:00 +0800",
        )
        self.assertEqual(archived, [])
        self.assertEqual(after, 100)
        self.assertTrue(active_catalog["items"][0]["available"])

    def test_negative_storage_limit_is_rejected_even_when_cleanup_is_disabled(self) -> None:
        with self.assertRaisesRegex(ValueError, "0 or greater"):
            catalog.storage_cleanup_limit_bytes(-1, False)

    def test_catalog_workflow_enables_cleanup_only_at_one_hundred_gib(self) -> None:
        workflow = (
            Path(__file__).resolve().parents[1]
            / ".github"
            / "workflows"
            / "neutral-edge-cutover.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("CATALOG_PDF_CLEANUP_ENABLED: ${{ vars.CATALOG_PDF_CLEANUP_ENABLED || 'true' }}", workflow)
        self.assertIn('true) cleanup_args=(--enable-pdf-cleanup) ;;', workflow)
        self.assertIn("--storage-limit-gb 100", workflow)
        self.assertIn('"${cleanup_args[@]}"', workflow)

    def test_prune_uses_safe_persisted_key_across_prefix_migration(self) -> None:
        client = FakeR2Client()
        items = [{
            "id": self.REPORT_A,
            "r2_key": f"reports-old/{self.REPORT_A}.pdf",
        }]

        with mock.patch.dict(os.environ, {"R2_BUCKET": "test-bucket"}, clear=False), mock.patch.object(
            catalog, "build_r2_client", return_value=client
        ):
            result = catalog.prune_r2_objects_for_items(items, "reports-new")

        self.assertEqual(result.deleted_count, 1)
        self.assertEqual(
            client.calls[0]["Delete"]["Objects"],
            [{"Key": f"reports-old/{self.REPORT_A}.pdf"}],
        )

    def test_unsafe_persisted_key_aborts_before_opening_r2_client(self) -> None:
        for stored_key in (
            f"_hot-reports/pdfs/{self.REPORT_A}.pdf",
            f"reports/{self.REPORT_B}.pdf",
            f"reports/{self.REPORT_A}.pdf/extra",
            f"/reports/{self.REPORT_A}.pdf",
        ):
            with self.subTest(stored_key=stored_key), mock.patch.object(
                catalog, "build_r2_client"
            ) as build_client:
                with self.assertRaisesRegex(ValueError, "Unsafe|persisted|reserved"):
                    catalog.prune_r2_objects_for_items(
                        [{"id": self.REPORT_A, "r2_key": stored_key}],
                        "reports",
                    )
                build_client.assert_not_called()

    def test_prune_supports_a_valid_configured_catalog_prefix(self) -> None:
        client = FakeR2Client()
        items = [{"id": self.REPORT_B}]

        with mock.patch.dict(os.environ, {"R2_BUCKET": "test-bucket"}, clear=False), mock.patch.object(
            catalog, "build_r2_client", return_value=client
        ):
            catalog.prune_r2_objects_for_items(items, "/catalog/reports-v2/")

        self.assertEqual(
            client.calls[0]["Delete"]["Objects"],
            [{"Key": f"catalog/reports-v2/{self.REPORT_B}.pdf"}],
        )

    def test_invalid_report_id_aborts_before_opening_r2_client(self) -> None:
        with mock.patch.object(catalog, "build_r2_client") as build_client:
            with self.assertRaisesRegex(ValueError, "invalid catalog report id"):
                catalog.prune_r2_objects_for_items(
                    [{"id": "../_hot-reports/pdfs/valuable", "r2_key": "reports/ok.pdf"}],
                    "reports",
                )
        build_client.assert_not_called()

    def test_reserved_or_ambiguous_prefix_is_rejected(self) -> None:
        for prefix in (
            "_hot-reports",
            "/_catalog-pdf-overrides/items",
            "_market-views",
            "",
            "reports/../_hot-reports",
        ):
            with self.subTest(prefix=prefix), self.assertRaisesRegex(ValueError, "prefix"):
                catalog.prune_r2_objects_for_items(
                    [{"id": "0123456789abcdef01234567"}],
                    prefix,
                )

    def test_batch_delete_records_partial_success_without_raising(self) -> None:
        client = FakeR2Client([{
            "Errors": [{
                "Key": f"reports/{self.REPORT_B}.pdf",
                "Code": "AccessDenied",
                "Message": "denied",
            }],
        }])

        result = catalog.delete_r2_objects(
            client,
            "test-bucket",
            [f"reports/{self.REPORT_A}.pdf", f"reports/{self.REPORT_B}.pdf"],
        )

        self.assertEqual(result.deleted_keys, frozenset({f"reports/{self.REPORT_A}.pdf"}))
        self.assertEqual(result.failed_keys, {f"reports/{self.REPORT_B}.pdf": "AccessDenied (denied)"})

    def test_batch_delete_exception_is_retryable_and_not_reported_as_success(self) -> None:
        client = FakeR2Client()
        client.delete_objects = mock.Mock(side_effect=TimeoutError("timed out"))

        result = catalog.delete_r2_objects(
            client,
            "test-bucket",
            [f"reports/{self.REPORT_A}.pdf"],
        )

        self.assertEqual(result.deleted_keys, frozenset())
        self.assertIn("TimeoutError", result.failed_keys[f"reports/{self.REPORT_A}.pdf"])

    def test_duplicate_ids_are_deleted_once(self) -> None:
        client = FakeR2Client()
        item = {"id": "0123456789abcdef01234567"}

        with mock.patch.dict(os.environ, {"R2_BUCKET": "test-bucket"}, clear=False), mock.patch.object(
            catalog, "build_r2_client", return_value=client
        ):
            result = catalog.prune_r2_objects_for_items([item, dict(item)], "reports")

        self.assertEqual(result.deleted_count, 1)
        self.assertEqual(len(client.calls), 1)

    def test_newly_archived_pdf_is_not_physically_deleted_in_same_run(self) -> None:
        old_catalog = {
            "items": [{
                "id": self.REPORT_A,
                "r2_key": f"reports/{self.REPORT_A}.pdf",
                "available": True,
                "r2_synced": True,
                "size_bytes": 100,
            }],
        }
        next_catalog = {
            "items": [{
                **old_catalog["items"][0],
                "present_in_latest_scan": True,
                "date_folder": "260101",
            }],
        }
        archived, size_before, size_after = catalog.apply_storage_limit(
            next_catalog,
            1,
            "2026-08-02 00:00:00 +0800",
        )

        self.assertEqual(len(archived), 1)
        self.assertEqual(size_before, 100)
        self.assertEqual(size_after, 0)
        self.assertFalse(next_catalog["items"][0]["available"])
        self.assertEqual(catalog.previously_archived_prune_candidates(old_catalog, next_catalog, {self.REPORT_A}), [])

    def test_inconsistent_old_archive_waits_for_unavailable_catalog_to_persist(self) -> None:
        old_item = {
            "id": self.REPORT_A,
            "r2_key": f"reports/{self.REPORT_A}.pdf",
            "available": True,
            "r2_synced": True,
            "pdf_archived": True,
        }
        normalized_item = {
            **old_item,
            "available": False,
            "r2_synced": False,
        }

        self.assertEqual(
            catalog.previously_archived_prune_candidates(
                {"items": [old_item]},
                {"items": [normalized_item]},
                {self.REPORT_A},
            ),
            [],
        )

    def test_previous_archive_is_retryable_after_partial_delete(self) -> None:
        old_catalog = {
            "items": [
                {
                    "id": self.REPORT_A,
                    "r2_key": f"reports-old/{self.REPORT_A}.pdf",
                    "available": False,
                    "r2_synced": False,
                    "pdf_archived": True,
                    "pdf_delete_pending": True,
                },
                {
                    "id": self.REPORT_B,
                    "r2_key": f"reports-old/{self.REPORT_B}.pdf",
                    "available": False,
                    "r2_synced": False,
                    "pdf_archived": True,
                    "pdf_delete_pending": True,
                },
            ],
        }
        next_catalog = {"items": [dict(item) for item in old_catalog["items"]]}
        candidates = catalog.previously_archived_prune_candidates(
            old_catalog,
            next_catalog,
            {self.REPORT_A, self.REPORT_B},
        )
        client = FakeR2Client([{
            "Errors": [{"Key": f"reports-old/{self.REPORT_B}.pdf", "Code": "InternalError"}],
        }])

        with mock.patch.dict(os.environ, {"R2_BUCKET": "test-bucket"}, clear=False), mock.patch.object(
            catalog, "build_r2_client", return_value=client
        ):
            result = catalog.prune_r2_objects_for_items(candidates, "reports-new")

        self.assertEqual(result.deleted_keys, frozenset({f"reports-old/{self.REPORT_A}.pdf"}))
        self.assertIn(f"reports-old/{self.REPORT_B}.pdf", result.failed_keys)
        # Both entries remain unavailable in the catalog regardless of which
        # physical deletion succeeded. Persisting success makes only the failed
        # object eligible for the next run's idempotent retry.
        next_catalog["items"][0]["pdf_object_deleted"] = True
        self.assertTrue(all(not item["available"] for item in next_catalog["items"]))
        self.assertEqual(
            {
                item["id"]
                for item in catalog.previously_archived_prune_candidates(
                    next_catalog,
                    next_catalog,
                    {self.REPORT_A, self.REPORT_B},
                )
            },
            {self.REPORT_B},
        )

    def test_raised_limit_reactivates_legacy_deferred_object(self) -> None:
        old_item = {
            "id": self.REPORT_A,
            "r2_key": f"reports/{self.REPORT_A}.pdf",
            "available": False,
            "r2_synced": False,
            "pdf_archived": True,
            "page_count": 12,
            "size_bytes": 100,
            "date_folder": "260101",
            "present_in_latest_scan": False,
        }
        next_catalog = {"items": [dict(old_item)]}

        archived, size_before, size_after = catalog.apply_storage_limit(
            next_catalog,
            1_000,
            "2026-08-29 00:00:00 +0800",
        )

        restored = next_catalog["items"][0]
        self.assertEqual(archived, [])
        self.assertEqual((size_before, size_after), (100, 100))
        self.assertTrue(restored["available"])
        self.assertTrue(restored["r2_synced"])
        self.assertNotIn("pdf_archived", restored)
        self.assertEqual(
            catalog.previously_archived_prune_candidates(
                {"items": [old_item]},
                next_catalog,
                set(),
            ),
            [],
        )

    def test_deferred_object_is_deleted_only_when_current_limit_reselects_it(self) -> None:
        old_item = {
            "id": self.REPORT_A,
            "r2_key": f"reports/{self.REPORT_A}.pdf",
            "available": False,
            "r2_synced": False,
            "pdf_archived": True,
            "page_count": 12,
            "size_bytes": 100,
            "date_folder": "260101",
            "present_in_latest_scan": False,
        }
        next_catalog = {"items": [dict(old_item)]}

        archived, _size_before, _size_after = catalog.apply_storage_limit(
            next_catalog,
            1,
            "2026-08-29 00:00:00 +0800",
        )
        active_ids = {str(item["id"]) for item in archived}

        self.assertEqual(active_ids, {self.REPORT_A})
        self.assertEqual(
            [item["id"] for item in catalog.previously_archived_prune_candidates(
                {"items": [old_item]},
                next_catalog,
                active_ids,
            )],
            [self.REPORT_A],
        )
        self.assertEqual(
            catalog.previously_archived_prune_candidates(
                {"items": [old_item]},
                next_catalog,
                set(),
            ),
            [],
        )

    def test_merge_preserves_existing_object_key_during_prefix_migration(self) -> None:
        old_catalog = {"items": [{
            "id": self.REPORT_A,
            "r2_key": f"reports-old/{self.REPORT_A}.pdf",
            "r2_synced": True,
            "available": True,
        }]}
        current = {self.REPORT_A: {
            "id": self.REPORT_A,
            "r2_key": f"reports-new/{self.REPORT_A}.pdf",
            "r2_synced": False,
            "available": False,
            "date_folders": ["260802"],
        }}

        merged = catalog.merge_catalog(old_catalog, current, "/zip_backup", "now")

        self.assertEqual(merged["items"][0]["r2_key"], f"reports-old/{self.REPORT_A}.pdf")

    def test_key_builder_rejects_reserved_prefix_even_without_pruning(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unsafe|reserved"):
            catalog.r2_key_for_id(self.REPORT_A, "_hot-reports/pdfs")

    def test_main_rejects_reserved_prefix_before_dropbox_or_upload(self) -> None:
        argv = [
            "portal_suite_catalog.py",
            "--r2-prefix", "_hot-reports/pdfs",
            "--storage-limit-gb", "100",
            "--sync-r2",
        ]
        with mock.patch.object(sys, "argv", argv), mock.patch.object(
            catalog, "dropbox_access_token"
        ) as token, mock.patch.object(catalog, "build_r2_client") as build_client:
            exit_code = catalog.main()

        self.assertEqual(exit_code, 2)
        token.assert_not_called()
        build_client.assert_not_called()


if __name__ == "__main__":
    unittest.main()
