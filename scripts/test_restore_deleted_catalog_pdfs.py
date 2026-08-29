#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import io
import sys
import types
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from typing import Any

# Keep the pure contract tests runnable in the repository's lightweight local
# Python. Network calls are injected below, so only the exception classes used
# by the shared Dropbox retry helper need to exist when requests is unavailable.
try:
    import requests  # noqa: F401
except ModuleNotFoundError:  # pragma: no cover - environment dependent
    requests_stub = types.ModuleType("requests")
    requests_stub.exceptions = types.SimpleNamespace(
        ConnectionError=ConnectionError,
        Timeout=TimeoutError,
        ChunkedEncodingError=ConnectionError,
    )
    requests_stub.post = lambda *args, **kwargs: None
    sys.modules["requests"] = requests_stub

import restore_deleted_catalog_pdfs as restore


class FakeDropboxApi:
    def __init__(self, responses: dict[str, list[dict[str, Any]]]) -> None:
        self.responses = {endpoint: list(values) for endpoint, values in responses.items()}
        self.calls: list[tuple[str, str, dict[str, Any]]] = []

    def __call__(self, token: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        self.calls.append((token, endpoint, payload))
        values = self.responses.get(endpoint, [])
        if not values:
            raise AssertionError(f"Unexpected Dropbox endpoint: {endpoint}")
        return values.pop(0)


class RestoreDeletedCatalogPdfsTests(unittest.TestCase):
    CONTENT_A = "a" * 64
    CONTENT_B = "b" * 64
    PATH_A = "/zip_backup/260724/private-a.pdf"
    PATH_B = "/zip_backup/260724/nested/private-b.pdf"
    TOKEN = "private-token-must-not-appear"

    @staticmethod
    def report_id(content_hash: str) -> str:
        return hashlib.sha256(f"dropbox-content:{content_hash}".encode()).hexdigest()[:24]

    def catalog(self, *content_hashes: str) -> dict[str, Any]:
        return {
            "items": [
                {
                    "id": self.report_id(content_hash),
                    "source_hash": restore.source_hash_for_content_hash(content_hash),
                    "date_folder": "260724",
                    "pdf_object_deleted": True,
                }
                for content_hash in content_hashes
            ]
        }

    def test_report_id_matches_portal_catalog_content_hash_contract(self) -> None:
        self.assertEqual(
            restore.report_id_for_content_hash(self.CONTENT_A),
            self.report_id(self.CONTENT_A),
        )

    def test_token_scope_is_parsed_without_exposing_token(self) -> None:
        token, scopes = restore.parse_token_response({
            "access_token": self.TOKEN,
            "scope": "files.metadata.read files.content.write",
        })
        self.assertEqual(token, self.TOKEN)
        self.assertIn("files.content.write", scopes)

        output = io.StringIO()
        with redirect_stdout(output):
            restore.validate_restore_scope(scopes, True)
        self.assertEqual(
            output.getvalue(),
            "scope_claim_present=true\n"
            "scope_files_metadata_read=true\n"
            "scope_files_content_write=true\n",
        )
        self.assertNotIn(self.TOKEN, output.getvalue())

    def test_missing_write_scope_fails_closed_with_scope_name_only(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output), self.assertRaisesRegex(
            restore.RestoreContractError,
            "missing_scope=files.content.write",
        ):
            restore.validate_restore_scope(frozenset({"files.metadata.read"}), True)

        self.assertEqual(
            output.getvalue(),
            "scope_claim_present=true\n"
            "scope_files_metadata_read=true\n"
            "scope_files_content_write=false\n"
            "missing_scope=files.content.write\n",
        )
        self.assertNotIn(self.TOKEN, output.getvalue())

    def test_read_only_scope_allows_dry_run(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            restore.validate_restore_scope(frozenset({"files.metadata.read"}), False)
        self.assertEqual(
            output.getvalue(),
            "scope_claim_present=true\n"
            "scope_files_metadata_read=true\n"
            "scope_files_content_write=false\n",
        )

    def test_omitted_scope_claim_allows_read_only_preflight(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            restore.validate_restore_scope(frozenset(), False)
        self.assertEqual(
            output.getvalue(),
            "scope_claim_present=false\n"
            "scope_files_metadata_read=false\n"
            "scope_files_content_write=false\n",
        )

    def test_list_folder_is_recursive_and_requests_deleted_restorable_metadata(self) -> None:
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [{".tag": "deleted", "path_lower": self.PATH_A}],
                "has_more": True,
                "cursor": "opaque-cursor",
            }],
            "/files/list_folder/continue": [{
                "entries": [{".tag": "deleted", "path_lower": self.PATH_B}],
                "has_more": False,
            }],
        })

        entries = restore.list_deleted_entries(self.TOKEN, "/zip_backup", api)

        self.assertEqual(len(entries), 2)
        self.assertEqual(api.calls[0][1], "/files/list_folder")
        self.assertEqual(
            api.calls[0][2],
            {
                "path": "/zip_backup",
                "recursive": True,
                "include_deleted": True,
                "include_restorable_info": True,
            },
        )
        self.assertEqual(
            api.calls[1][2],
            {"cursor": "opaque-cursor"},
        )

    def test_expected_catalog_count_mismatch_makes_no_dropbox_call(self) -> None:
        api = FakeDropboxApi({})

        with self.assertRaisesRegex(restore.RestoreContractError, "catalog_count=1"):
            restore.run_restore(
                catalog=self.catalog(self.CONTENT_A),
                token=self.TOKEN,
                root="/zip_backup",
                date_folder="260724",
                expected_count=2,
                apply_restore=True,
                api_call=api,
            )

        self.assertEqual(api.calls, [])

    def test_revision_pagination_follows_has_more_even_for_a_short_page(self) -> None:
        api = FakeDropboxApi({
            "/files/list_revisions": [
                {
                    "entries": [{"rev": "rev-new"}],
                    "has_more": True,
                },
                {
                    "entries": [{"rev": "rev-old"}],
                    "has_more": False,
                },
            ],
        })

        entries = restore.list_revisions(self.TOKEN, self.PATH_A, api)

        self.assertEqual([entry["rev"] for entry in entries], ["rev-new", "rev-old"])
        revision_calls = [call for call in api.calls if call[1] == "/files/list_revisions"]
        self.assertEqual(len(revision_calls), 2)
        self.assertEqual(revision_calls[1][2]["before_rev"], "rev-new")

    def test_revision_page_with_exact_limit_and_no_more_stops(self) -> None:
        page = [{"rev": f"rev-{index:03d}"} for index in range(restore.REVISION_PAGE_SIZE)]
        api = FakeDropboxApi({
            "/files/list_revisions": [{"entries": page, "has_more": False}],
        })

        entries = restore.list_revisions(self.TOKEN, self.PATH_A, api)

        self.assertEqual(len(entries), restore.REVISION_PAGE_SIZE)
        self.assertEqual(
            len([call for call in api.calls if call[1] == "/files/list_revisions"]),
            1,
        )

    def test_dry_run_resolves_exact_ids_without_restore_calls(self) -> None:
        report_a = self.report_id(self.CONTENT_A)
        report_b = self.report_id(self.CONTENT_B)
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [
                    {
                        ".tag": "deleted",
                        "path_lower": self.PATH_A,
                        "is_restorable": True,
                    },
                    {
                        ".tag": "deleted",
                        "path_lower": self.PATH_B,
                        "is_restorable": True,
                    },
                    {
                        ".tag": "deleted",
                        "path_lower": "/zip_backup/260725/not-target.pdf",
                        "is_restorable": True,
                    },
                ],
                "has_more": False,
            }],
            "/files/list_revisions": [
                {
                    "has_more": False,
                    "entries": [{
                        ".tag": "file",
                        "rev": "rev-a",
                        "content_hash": self.CONTENT_A,
                        "is_restorable": True,
                    }],
                },
                {
                    "has_more": False,
                    "entries": [{
                        ".tag": "file",
                        "rev": "rev-b",
                        "content_hash": self.CONTENT_B,
                        "is_restorable": True,
                    }],
                },
            ],
        })

        result = restore.run_restore(
            catalog=self.catalog(self.CONTENT_A, self.CONTENT_B),
            token=self.TOKEN,
            root="/zip_backup",
            date_folder="260724",
            expected_count=2,
            apply_restore=False,
            api_call=api,
        )

        self.assertEqual(result.report_ids, tuple(sorted((report_a, report_b))))
        self.assertEqual(result.already_restored_count, 0)
        self.assertEqual(result.pending_restore_count, 2)
        self.assertEqual(result.restored_count, 0)
        self.assertNotIn("/files/restore", [endpoint for _token, endpoint, _payload in api.calls])
        revision_payloads = [payload for _token, endpoint, payload in api.calls if endpoint == "/files/list_revisions"]
        self.assertTrue(revision_payloads)
        self.assertTrue(all(payload["mode"] == "path" for payload in revision_payloads))
        self.assertTrue(all(payload["include_restorable_info"] is True for payload in revision_payloads))

    def test_unresolved_expected_count_stops_before_first_restore(self) -> None:
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [{
                    ".tag": "deleted",
                    "path_lower": self.PATH_A,
                    "is_restorable": True,
                }],
                "has_more": False,
            }],
            "/files/list_revisions": [{
                "has_more": False,
                "entries": [{
                    "rev": "rev-a",
                    "content_hash": self.CONTENT_A,
                    "is_restorable": True,
                }],
            }],
        })

        with self.assertRaisesRegex(restore.RestoreContractError, "resolved_count=1"):
            restore.run_restore(
                catalog=self.catalog(self.CONTENT_A, self.CONTENT_B),
                token=self.TOKEN,
                root="/zip_backup",
                date_folder="260724",
                expected_count=2,
                apply_restore=True,
                api_call=api,
            )

        self.assertNotIn("/files/restore", [endpoint for _token, endpoint, _payload in api.calls])

    def test_active_file_is_already_restored_and_not_written_again(self) -> None:
        report_a = self.report_id(self.CONTENT_A)
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [{
                    ".tag": "file",
                    "path_display": "/zip_backup/260724/Private-A.pdf",
                    "path_lower": self.PATH_A,
                    "content_hash": self.CONTENT_A,
                }],
                "has_more": False,
            }],
        })

        result = restore.run_restore(
            catalog=self.catalog(self.CONTENT_A),
            token=self.TOKEN,
            root="/zip_backup",
            date_folder="260724",
            expected_count=1,
            apply_restore=True,
            api_call=api,
        )

        self.assertEqual(result.report_ids, (report_a,))
        self.assertEqual(result.already_restored_count, 1)
        self.assertEqual(result.pending_restore_count, 0)
        self.assertEqual(result.restored_count, 0)
        self.assertNotIn("/files/list_revisions", [endpoint for _token, endpoint, _payload in api.calls])
        self.assertNotIn("/files/restore", [endpoint for _token, endpoint, _payload in api.calls])

    def test_partial_rerun_restores_only_pending_target(self) -> None:
        report_b = self.report_id(self.CONTENT_B)
        display_b = "/zip_backup/260724/Nested/Private-B.pdf"
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [
                    {
                        ".tag": "file",
                        "path_display": "/zip_backup/260724/Private-A.pdf",
                        "content_hash": self.CONTENT_A,
                    },
                    {
                        ".tag": "deleted",
                        "path_display": display_b,
                        "path_lower": self.PATH_B,
                        "is_restorable": True,
                    },
                ],
                "has_more": False,
            }],
            "/files/list_revisions": [{
                "has_more": False,
                "entries": [{
                    "rev": "rev-b",
                    "content_hash": self.CONTENT_B,
                    "is_restorable": True,
                }],
            }],
            "/files/restore": [{"content_hash": self.CONTENT_B}],
        })

        result = restore.run_restore(
            catalog=self.catalog(self.CONTENT_A, self.CONTENT_B),
            token=self.TOKEN,
            root="/zip_backup",
            date_folder="260724",
            expected_count=2,
            apply_restore=True,
            api_call=api,
        )

        restore_calls = [call for call in api.calls if call[1] == "/files/restore"]
        self.assertEqual(len(restore_calls), 1)
        self.assertEqual(restore_calls[0][2], {"path": display_b, "rev": "rev-b"})
        self.assertEqual(result.already_restored_count, 1)
        self.assertEqual(result.pending_restore_count, 1)
        self.assertEqual(result.restored_count, 1)
        self.assertIn(report_b, result.report_ids)

    def test_folder_tombstone_without_child_paths_has_explicit_diagnostic(self) -> None:
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [{
                    ".tag": "deleted",
                    "path_lower": "/zip_backup/260724",
                    "is_restorable": True,
                }],
                "has_more": False,
            }],
        })

        with self.assertRaisesRegex(
            restore.RestoreContractError,
            "target_folder_tombstone_only=true.*child_deleted_pdf_paths=0",
        ):
            restore.run_restore(
                catalog=self.catalog(self.CONTENT_A),
                token=self.TOKEN,
                root="/zip_backup",
                date_folder="260724",
                expected_count=1,
                apply_restore=True,
                api_call=api,
            )

        self.assertNotIn("/files/restore", [endpoint for _token, endpoint, _payload in api.calls])

    def test_apply_uses_files_restore_and_logs_only_counts_and_ids(self) -> None:
        report_a = self.report_id(self.CONTENT_A)
        api = FakeDropboxApi({
            "/files/list_folder": [{
                "entries": [{
                    ".tag": "deleted",
                    "path_lower": self.PATH_A,
                    "is_restorable": True,
                }],
                "has_more": False,
            }],
            "/files/list_revisions": [{
                "has_more": False,
                "entries": [
                    {
                        "rev": "private-revision",
                        "content_hash": self.CONTENT_A,
                        "is_restorable": True,
                    },
                    {
                        "rev": "unrelated-revision",
                        "content_hash": self.CONTENT_B,
                        "is_restorable": True,
                    },
                ],
            }],
            "/files/restore": [{
                ".tag": "file",
                "content_hash": self.CONTENT_A,
            }],
        })

        result = restore.run_restore(
            catalog=self.catalog(self.CONTENT_A),
            token=self.TOKEN,
            root="/zip_backup",
            date_folder="260724",
            expected_count=1,
            apply_restore=True,
            api_call=api,
        )
        output = io.StringIO()
        with redirect_stdout(output):
            restore.emit_result(result, True)

        restore_calls = [call for call in api.calls if call[1] == "/files/restore"]
        self.assertEqual(len(restore_calls), 1)
        self.assertEqual(
            restore_calls[0][2],
            {"path": self.PATH_A, "rev": "private-revision"},
        )
        self.assertIn(f"report_id={report_a}", output.getvalue())
        self.assertNotIn(self.PATH_A, output.getvalue())
        self.assertNotIn("private-revision", output.getvalue())
        self.assertNotIn(self.TOKEN, output.getvalue())

    def test_one_deleted_path_cannot_restore_two_catalog_ids(self) -> None:
        api = FakeDropboxApi({
            "/files/list_revisions": [{
                "has_more": False,
                "entries": [
                    {
                        "rev": "rev-a",
                        "content_hash": self.CONTENT_A,
                        "is_restorable": True,
                    },
                    {
                        "rev": "rev-b",
                        "content_hash": self.CONTENT_B,
                        "is_restorable": True,
                    },
                ],
            }],
        })

        with self.assertRaisesRegex(restore.RestoreContractError, "multiple target"):
            restore.build_restore_plan(
                self.TOKEN,
                {
                    self.report_id(self.CONTENT_A): restore.source_hash_for_content_hash(self.CONTENT_A),
                    self.report_id(self.CONTENT_B): restore.source_hash_for_content_hash(self.CONTENT_B),
                },
                (self.PATH_A,),
                api,
            )

    def test_matching_report_id_prefix_with_wrong_full_source_hash_fails(self) -> None:
        source_hash = restore.source_hash_for_content_hash(self.CONTENT_A)
        report_id = source_hash[:24]
        api = FakeDropboxApi({
            "/files/list_revisions": [{
                "has_more": False,
                "entries": [{
                    "rev": "rev-a",
                    "content_hash": self.CONTENT_A,
                    "is_restorable": True,
                }],
            }],
        })

        with self.assertRaisesRegex(restore.RestoreContractError, "source_hash mismatch"):
            restore.build_restore_plan(
                self.TOKEN,
                {report_id: source_hash[:-1] + ("0" if source_hash[-1] != "0" else "1")},
                (self.PATH_A,),
                api,
            )

    def test_workflow_is_manual_and_dry_run_by_default(self) -> None:
        workflow_path = (
            Path(__file__).resolve().parents[1]
            / ".github"
            / "workflows"
            / "restore-deleted-catalog-pdfs.yml"
        )
        workflow = workflow_path.read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("schedule:", workflow)
        self.assertIn("date_folder:", workflow)
        self.assertIn("expected_count:", workflow)
        self.assertIn("apply_restore:", workflow)
        self.assertIn("default: false", workflow)
        self.assertIn("DROPBOX_REFRESH_TOKEN: ${{ secrets.DROPBOX_REFRESH_TOKEN }}", workflow)
        self.assertIn('true) restore_args=(--apply-restore) ;;', workflow)


if __name__ == "__main__":
    unittest.main()
