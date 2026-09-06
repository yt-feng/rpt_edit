#!/usr/bin/env python3
"""Offline checks for the read-only final candidate identity guard."""

from __future__ import annotations

import copy
from pathlib import Path
import tempfile
import unittest

import publish_static_slot as publisher
import verify_prepared_static_slot as guard
from test_publish_static_slot import FakeR2, release, write


class PreparedStaticSlotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.client = FakeR2()
        self.slot = "b"
        self.release = release(17)

    def prepare(self, *, multilingual: bool = True, omit: str = "") -> dict:
        paths = set(guard.REQUIRED_STATIC_PATHS) | set(publisher.DEFAULT_RUNTIME_PATHS)
        if multilingual:
            paths.update(guard.REQUIRED_LOCALE_PATHS)
        # Path sorting differs from string sorting for these two siblings.
        paths.update(("alpha.txt", "alpha/z.txt"))
        for relative in sorted(paths - {omit}):
            write(self.root / relative, "fixture: " + relative)
        paths_by_relative, files, tree, total = publisher.build_inventory(self.root)
        for relative, path in paths_by_relative.items():
            self.client.upload_file(
                str(path), "bucket", publisher.slot_prefix(self.slot) + relative,
                ExtraArgs=publisher.upload_extra_args(files[relative]),
            )
        _runtime_paths, runtime_files, runtime_tree = publisher.runtime_inventory(self.root)
        runtime = {
            "schema_version": publisher.RUNTIME_SCHEMA_VERSION,
            "release_id": self.release,
            "prefix": publisher.runtime_release_prefix(self.release),
            "tree_sha256": runtime_tree,
            "file_count": len(runtime_files),
            "files": runtime_files,
        }
        for filename, descriptor in runtime_files.items():
            self.client.put_object(
                Bucket="bucket", Key=runtime["prefix"] + filename,
                Body=(self.root / "data" / filename).read_bytes(),
                Metadata={"sha256": descriptor["sha256"], "release-id": self.release},
                ContentType=descriptor["content_type"], CacheControl=descriptor["cache_control"],
            )
        publisher.put_json(self.client, "bucket", publisher.runtime_manifest_key(self.release), runtime)
        self.manifest = {
            "schema_version": publisher.SCHEMA_VERSION,
            "slot": self.slot,
            "release_id": self.release,
            "tree_sha256": tree,
            "file_count": len(files),
            "total_bytes": total,
            "files": files,
            "runtime_data": {key: runtime[key] for key in ("schema_version", "release_id", "prefix", "tree_sha256")},
        }
        publisher.put_json(self.client, "bucket", publisher.manifest_key(self.slot), self.manifest)
        self.client.operations.clear()
        return self.manifest

    def verify(self, **overrides):
        return guard.verify_prepared_static_slot(
            self.client, "bucket", **{
                "slot": self.slot, "release": self.release, "tree": self.manifest["tree_sha256"],
                **overrides,
            },
        )

    def replace_manifest(self, changes: dict) -> None:
        payload = {**self.manifest, **changes}
        publisher.put_json(self.client, "bucket", publisher.manifest_key(self.slot), payload)

    def test_multilingual_candidate_passes_without_writes_or_full_inventory_reads(self) -> None:
        manifest = self.prepare()
        result = self.verify()
        self.assertTrue(result["verified"])
        self.assertEqual(result["static_objects_verified"], len(guard.REQUIRED_STATIC_PATHS) + len(guard.REQUIRED_LOCALE_PATHS))
        self.assertEqual(result["runtime_objects_verified"], 3)
        self.assertEqual(guard.static_tree_sha256(manifest["files"]), manifest["tree_sha256"])
        self.assertNotEqual(publisher.runtime_tree_sha256(manifest["files"]), manifest["tree_sha256"])
        self.assertTrue(all(operation in {"head", "get"} for operation, _key in self.client.operations))
        self.assertFalse(any(key.endswith("alpha/z.txt") for _operation, key in self.client.operations))

    def test_plain_chinese_candidate_does_not_require_locale_objects(self) -> None:
        self.prepare(multilingual=False)
        result = self.verify()
        self.assertTrue(result["verified"])
        self.assertEqual(result["static_objects_verified"], len(guard.REQUIRED_STATIC_PATHS))

    def test_multilingual_manifest_requires_all_three_locale_homes(self) -> None:
        self.prepare(omit="ar/index.html")
        with self.assertRaisesRegex(RuntimeError, "required object: ar/index.html"):
            self.verify()

    def test_requested_identity_cannot_follow_a_reused_slot(self) -> None:
        self.prepare()
        self.replace_manifest({"release_id": release(18)})
        with self.assertRaisesRegex(RuntimeError, "requested candidate"):
            self.verify()

    def test_manifest_tree_is_recomputed_instead_of_trusting_its_header(self) -> None:
        self.prepare()
        changed = copy.deepcopy(self.manifest["files"])
        changed["alpha.txt"]["sha256"] = "0" * 64
        self.replace_manifest({"files": changed})
        with self.assertRaisesRegex(RuntimeError, "file tree"):
            self.verify()

    def test_incomplete_marker_is_rejected_even_when_not_a_json_object(self) -> None:
        self.prepare()
        self.client.put_object(Bucket="bucket", Key=publisher.incomplete_key(self.slot), Body=b"[]")
        with self.assertRaisesRegex(RuntimeError, "incomplete publication marker"):
            self.verify()

    def test_same_length_corruption_is_rejected_even_with_unchanged_digest_metadata(self) -> None:
        self.prepare()
        key = publisher.slot_prefix(self.slot) + "index.html"
        self.client.objects[key]["body"] = b"x" * len(self.client.objects[key]["body"])
        with self.assertRaisesRegex(RuntimeError, "content differs"):
            self.verify()

    def test_wrong_metadata_is_rejected_even_with_correct_object_bytes(self) -> None:
        self.prepare()
        key = publisher.slot_prefix(self.slot) + "index.html"
        self.client.objects[key]["metadata"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(RuntimeError, "metadata differs"):
            self.verify()

    def test_runtime_binding_and_release_metadata_are_both_checked(self) -> None:
        self.prepare()
        self.replace_manifest({"runtime_data": {**self.manifest["runtime_data"], "tree_sha256": "0" * 64}})
        with self.assertRaisesRegex(RuntimeError, "runtime manifest identities differ"):
            self.verify()
        self.replace_manifest({})
        key = publisher.runtime_release_prefix(self.release) + "catalog.json"
        self.client.objects[key]["metadata"]["release-id"] = release(18)
        with self.assertRaisesRegex(RuntimeError, "runtime metadata differs"):
            self.verify()

    def test_runtime_bytes_and_static_source_must_match(self) -> None:
        self.prepare()
        key = publisher.runtime_release_prefix(self.release) + "catalog.json"
        self.client.objects[key]["body"] = b"x" * len(self.client.objects[key]["body"])
        with self.assertRaisesRegex(RuntimeError, "content differs"):
            self.verify()

    def test_publication_started_during_checks_is_detected_before_return(self) -> None:
        self.prepare()
        get_object = self.client.get_object
        def begin_new_publication(*, Bucket, Key):
            if Key.endswith("/password_rules.json"):
                self.client.put_object(Bucket=Bucket, Key=publisher.incomplete_key(self.slot), Body=b"{}")
            return get_object(Bucket=Bucket, Key=Key)
        self.client.get_object = begin_new_publication
        with self.assertRaisesRegex(RuntimeError, "incomplete publication marker"):
            self.verify()

    def test_manifest_replaced_during_checks_is_detected_before_return(self) -> None:
        self.prepare()
        get_object = self.client.get_object
        def replace_on_runtime_read(*, Bucket, Key):
            if Key.endswith("/password_rules.json"):
                self.replace_manifest({"release_id": release(18)})
            return get_object(Bucket=Bucket, Key=Key)
        self.client.get_object = replace_on_runtime_read
        with self.assertRaisesRegex(RuntimeError, "requested candidate"):
            self.verify()

    def test_publication_started_during_final_manifest_read_is_detected(self) -> None:
        self.prepare()
        get_object = self.client.get_object
        reads = 0
        def begin_on_second_manifest_read(*, Bucket, Key):
            nonlocal reads
            if Key == publisher.manifest_key(self.slot):
                reads += 1
                if reads == 2:
                    self.client.put_object(Bucket=Bucket, Key=publisher.incomplete_key(self.slot), Body=b"{}")
            return get_object(Bucket=Bucket, Key=Key)
        self.client.get_object = begin_on_second_manifest_read
        with self.assertRaisesRegex(RuntimeError, "incomplete publication marker"):
            self.verify()


if __name__ == "__main__":
    unittest.main()
