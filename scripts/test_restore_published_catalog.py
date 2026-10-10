#!/usr/bin/env python3
"""Published catalog inheritance, immutable source binding and history regressions."""
from __future__ import annotations

import contextlib
import copy
import gzip
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import restore_published_catalog as restore
from build_portal_suite_site import merge_history_catalog
from publish_static_slot import runtime_manifest_key, runtime_release_prefix, runtime_tree_sha256

A, B, C = "a" * 24, "b" * 24, "c" * 24
ACTIVE, RECOVERY = "1" * 32, "2" * 32


def item(report_id=A, *, available=True, **fields):
    return {"id": report_id, "title": "Private source title", "filename": "Private source title.pdf",
            "date_folder": "261009", "date_folders": ["261009"],
            "available": available, "size_bytes": 123 if available else 0, **fields}


def catalog(*items):
    return {"schema_version": 1, "updated_at_bjt": "2026-10-10 12:00:00 +0800",
            "item_count": len(items), "items": list(items)}


def state():
    return {"schema_version": 1, "release_id": ACTIVE, "slot": "a", "tree_sha256": "3" * 64}


class FakeR2:
    def __init__(self):
        self.objects = {}
        self.heads = {}
        self.head_calls = []
        self.get_calls = []

    def add_release(self, release, value):
        raw = restore.encoded(value)
        files = {"catalog.json": {"sha256": restore.sha256(raw), "size": len(raw),
                                  "content_type": "application/json", "cache_control": "no-store"}}
        manifest = {"schema_version": 1, "release_id": release, "prefix": runtime_release_prefix(release),
                    "files": files, "file_count": len(files), "tree_sha256": runtime_tree_sha256(files)}
        self.objects[runtime_manifest_key(release)] = restore.encoded(manifest)
        self.objects[runtime_release_prefix(release) + "catalog.json"] = raw
        return raw

    def get_object(self, *, Bucket, Key):
        self.get_calls.append(Key)
        raw = self.objects[Key]
        return {"ContentLength": len(raw), "Body": io.BytesIO(raw)}

    def head_object(self, *, Bucket, Key):
        self.head_calls.append(Key)
        value = self.heads[Key]
        if isinstance(value, Exception):
            raise value
        return {"ContentLength": value}


class PublishedCatalogTests(unittest.TestCase):
    def assert_category(self, category, callback):
        with self.assertRaises(restore.CatalogInheritanceError) as caught:
            callback()
        self.assertEqual(caught.exception.category, category)

    def test_runtime_manifest_binds_release_tree_bytes_and_catalog_ids(self):
        client = FakeR2()
        raw = client.add_release(ACTIVE, catalog(item()))
        loaded, loaded_raw = restore.load_release_catalog(client, "bucket", ACTIVE)
        self.assertEqual(loaded_raw, raw)
        self.assertEqual(loaded["items"][0]["id"], A)
        for field, value in [("release_id", RECOVERY), ("tree_sha256", "0" * 64),
                             ("prefix", "arbitrary/"), ("file_count", 99)]:
            with self.subTest(field=field):
                client.add_release(ACTIVE, catalog(item()))
                manifest = json.loads(client.objects[runtime_manifest_key(ACTIVE)])
                manifest[field] = value
                client.objects[runtime_manifest_key(ACTIVE)] = restore.encoded(manifest)
                self.assert_category("runtime_manifest_invalid",
                                     lambda: restore.load_release_catalog(client, "bucket", ACTIVE))
        client.add_release(ACTIVE, catalog(item()))
        key = runtime_release_prefix(ACTIVE) + "catalog.json"
        client.objects[key] = client.objects[key].replace(b"Private", b"Changed")
        self.assert_category("runtime_catalog_integrity_mismatch",
                             lambda: restore.load_release_catalog(client, "bucket", ACTIVE))
        client.objects[key] += b" "
        self.assert_category("runtime_catalog_integrity_mismatch",
                             lambda: restore.load_release_catalog(client, "bucket", ACTIVE))

    def test_invalid_release_rejected_without_remote_read(self):
        client = FakeR2()
        self.assert_category("release_id_invalid",
                             lambda: restore.load_release_catalog(client, "bucket", "../catalog.json"))
        self.assertEqual(client.get_calls, [])

    def test_active_public_bytes_must_match_immutable_snapshot(self):
        client = FakeR2()
        raw = client.add_release(ACTIVE, catalog(item()))
        self.assert_category("active_public_catalog_mismatch",
                             lambda: restore.load_sources(client, "bucket", state(), raw + b" "))

    def test_active_state_wins_over_recovery_for_same_id(self):
        client = FakeR2()
        active = catalog(item(available=False, pdf_archived=True, title="Active title"))
        raw = client.add_release(ACTIVE, active)
        client.add_release(RECOVERY, catalog(item(date_folder="260929", date_folders=["260928"]), item(B)))
        rows, sources = restore.load_sources(client, "bucket", state(), raw, RECOVERY)
        self.assertFalse(rows[A]["available"])
        self.assertTrue(rows[A]["pdf_archived"])
        self.assertTrue(rows[B]["available"])
        self.assertEqual(rows[A]["date_folder"], "261009")
        self.assertEqual(rows[A]["title"], "Active title")
        self.assertEqual(rows[A]["date_folders"], ["261009", "260929", "260928"])
        self.assertEqual(active["items"][0]["date_folders"], ["261009"])
        self.assertEqual([source["role"] for source in sources], ["recovery", "active"])

    def test_duplicate_published_ids_fail_without_silent_overwrite(self):
        client = FakeR2()
        client.add_release(ACTIVE, catalog(item(), item()))
        self.assert_category("catalog_duplicate_ids",
                             lambda: restore.load_release_catalog(client, "bucket", ACTIVE))

    def test_inherited_pdf_requires_exact_head_and_does_not_mutate_inputs(self):
        client = FakeR2()
        client.heads[f"reports/{A}.pdf"] = 123
        seed = catalog(item(B, available=False, pdf_archived=True))
        original = copy.deepcopy(seed)
        inherited = {A: item(source_hash="injected", r2_key="arbitrary/key")}
        result, counts = restore.inherit_catalog(seed, inherited, client, "bucket", "reports")
        by_id = restore.catalog_rows(result)
        self.assertTrue(by_id[A]["r2_synced"])
        self.assertEqual(by_id[A]["r2_key"], f"reports/{A}.pdf")
        self.assertNotIn("source_hash", by_id[A])
        self.assertEqual(client.head_calls, [f"reports/{A}.pdf"])
        self.assertEqual(counts["added_count"], 1)
        self.assertEqual(seed, original)

    def test_same_title_different_ids_remain_distinct(self):
        client = FakeR2()
        client.heads = {f"reports/{report_id}.pdf": 123 for report_id in [A, B]}
        seed = catalog(item(C, available=False, pdf_archived=True))
        result, _ = restore.inherit_catalog(seed, {A: item(), B: item(B)}, client, "bucket", "reports")
        self.assertEqual(set(restore.catalog_rows(result)), {A, B, C})

    def test_native_persistent_key_and_private_metadata_survive_prefix_migration(self):
        client = FakeR2()
        old_key = f"old-reports/{A}.pdf"
        seed = catalog(item(r2_key=old_key, r2_synced=True, source_hash="native",
                            title_zh="old translation", date_folder="260928", date_folders=["260928"]))
        result, counts = restore.inherit_catalog(seed, {A: item(title_zh="new translation")},
                                                client, "bucket", "reports-v2")
        actual = result["items"][0]
        self.assertEqual(actual["r2_key"], old_key)
        self.assertEqual(actual["source_hash"], "native")
        self.assertEqual(actual["title_zh"], "new translation")
        self.assertEqual(actual["date_folder"], "261009")
        self.assertEqual(actual["date_folders"], ["261009", "260928"])
        self.assertEqual(counts["pdf_heads_verified"], 0)
        self.assertEqual(client.head_calls, [])
        seed["items"][0]["r2_synced"] = False
        client.heads[old_key] = 123
        restore.inherit_catalog(seed, {A: item()}, client, "bucket", "reports-v2")
        self.assertEqual(client.head_calls, [old_key])

    def test_native_tombstone_and_text_only_rows_are_never_reactivated(self):
        client = FakeR2()
        native = item(available=False, pdf_archived=True, pdf_object_deleted=True,
                      pdf_delete_pending=True, r2_key=f"reports/{A}.pdf", r2_synced=False)
        result, counts = restore.inherit_catalog(catalog(native),
            {A: item(available=False, pdf_archived=True), B: item(B, available=False, pdf_archived=True)},
            client, "bucket", "reports")
        rows = restore.catalog_rows(result)
        self.assertTrue(rows[A]["pdf_object_deleted"])
        self.assertTrue(rows[A]["pdf_delete_pending"])
        self.assertFalse(rows[B]["r2_synced"])
        self.assertEqual(counts["pdf_heads_verified"], 0)
        self.assertEqual(client.head_calls, [])
        self.assert_category("published_availability_conflicts_with_native_tombstone",
            lambda: restore.inherit_catalog(catalog(native), {A: item()}, client, "bucket", "reports"))

    def test_archive_state_conflict_and_nonpositive_size_are_invalid(self):
        self.assert_category("catalog_archive_availability_conflict",
                             lambda: restore.catalog_rows(catalog(item(pdf_archived=True))))
        self.assert_category("catalog_pdf_size_invalid",
                             lambda: restore.catalog_rows(catalog(item(size_bytes=0))))

    def test_final_gate_requires_exact_ids_and_availability_without_fuzzy_alias(self):
        manifest = restore.inheritance_manifest({A: item()}, [])
        self.assert_category("published_report_ids_missing",
                             lambda: restore.validate_inheritance(catalog(item(B)), manifest))
        self.assert_category("published_pdf_availability_regressed",
            lambda: restore.validate_inheritance(catalog(item(available=False, pdf_archived=True)), manifest))
        self.assertTrue(restore.validate_inheritance(catalog(item(), item(B)), manifest)["complete"])
        self.assertNotIn("title", json.dumps(manifest))
        manifest["required"][0]["available"] = False
        self.assert_category("inheritance_manifest_invalid",
                             lambda: restore.validate_inheritance(catalog(item()), manifest))

    def test_final_gate_preserves_archived_state(self):
        manifest = restore.inheritance_manifest({A: item(available=False, pdf_archived=True)}, [])
        self.assert_category("published_archive_state_regressed",
                             lambda: restore.validate_inheritance(catalog(item()), manifest))

    def test_final_gate_preserves_primary_and_secondary_source_dates_with_additions_allowed(self):
        prior = item(date_folder="261009", date_folders=["260928"])
        manifest = restore.inheritance_manifest({A: prior}, [])
        self.assertEqual(manifest["required"][0]["date_folders"], ["260928", "261009"])
        self.assert_category("published_source_dates_missing",
                             lambda: restore.validate_inheritance(catalog(item()), manifest))
        # A newer display date is fine when every previous source date remains.
        candidate = item(date_folder="261010", date_folders=["261010", "261009", "260928"])
        self.assertTrue(restore.validate_inheritance(catalog(candidate), manifest)["complete"])
        manifest["required"][0].pop("date_folders")
        manifest["required_sha256"] = restore.sha256(restore.encoded(manifest["required"]))
        self.assert_category("inheritance_manifest_invalid",
                             lambda: restore.validate_inheritance(catalog(candidate), manifest))

    def test_malformed_source_date_is_rejected_without_private_value_in_error(self):
        self.assert_category("catalog_source_dates_invalid",
                             lambda: restore.catalog_rows(catalog(item(date_folders=["private source name"]))))

    def test_failed_heads_never_write_catalog_or_checkpoint_and_emit_no_private_name(self):
        for response in [122, RuntimeError("404 private object"), RuntimeError("403 private auth"),
                         RuntimeError("503 private provider")]:
            with self.subTest(response=type(response).__name__), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                native_path, public_path = root / "native.json", root / "public.json"
                state_path, manifest_path = root / "state.json", root / "inheritance.json"
                seed = restore.encoded(catalog(item(B, available=False, pdf_archived=True)))
                native_path.write_bytes(seed)
                state_path.write_bytes(restore.encoded(state()))
                client = FakeR2()
                public_path.write_bytes(client.add_release(ACTIVE, catalog(item())))
                client.heads[f"reports/{A}.pdf"] = response
                output = io.StringIO()
                with mock.patch.object(restore, "build_r2_client", return_value=client), \
                     mock.patch.dict(os.environ, {"R2_BUCKET": "bucket"}), contextlib.redirect_stdout(output):
                    code = restore.main(["restore", "--catalog-path", str(native_path),
                        "--previous-edge-state", str(state_path), "--previous-public-catalog", str(public_path),
                        "--output-manifest", str(manifest_path)])
                self.assertEqual(code, 1)
                self.assertEqual(native_path.read_bytes(), seed)
                self.assertFalse(manifest_path.exists())
                self.assertNotIn("Private source", output.getvalue())
                self.assertNotIn("private auth", output.getvalue())


class InheritedHistoryTests(unittest.TestCase):
    def test_existing_history_id_wins_over_date_stripped_title_match_and_keeps_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            history_path = root / "history.json"
            history_path.write_bytes(restore.encoded(catalog(item(A, available=False,
                title="Periodic outlook - 260928", pdf_archived=True))))
            (root / "shard_0.json.gz").write_bytes(gzip.compress(restore.encoded({A: "History body"})))
            live = catalog(item(A, available=False, title="Renamed inherited title", pdf_archived=True),
                           item(B, title="Periodic outlook - 260929"))
            merged, texts, stats = merge_history_catalog(live, history_path, root)
            self.assertEqual(len(merged["items"]), 2)
            self.assertEqual(texts, {A: "History body"})
            self.assertEqual(stats["history_added"], 0)

    def test_duplicate_history_ids_are_not_appended_twice(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "history.json"
            path.write_bytes(restore.encoded(catalog(item(A, available=False), item(A, available=False))))
            live = catalog(item(B, title="Different source", filename="Different source.pdf"))
            merged, _, stats = merge_history_catalog(live, path, root)
            self.assertEqual(len(merged["items"]), 2)
            self.assertEqual(stats["history_added"], 1)
            self.assertEqual({row["id"] for row in merged["items"]}, {A, B})


if __name__ == "__main__":
    unittest.main()
