#!/usr/bin/env python3

from __future__ import annotations

import io
import json
import os
import tempfile
import threading
import unittest
from pathlib import Path

import publish_static_slot as publisher


class MissingObject(KeyError):
    response = {"Error": {"Code": "NoSuchKey"}}


class FakePaginator:
    def __init__(self, client: "FakeR2", page_size: int = 3):
        self.client = client
        self.page_size = page_size

    def paginate(self, *, Bucket: str, Prefix: str):
        del Bucket
        with self.client.lock:
            rows = [
                {"Key": key, "Size": len(value["body"])}
                for key, value in sorted(self.client.objects.items())
                if key.startswith(Prefix)
            ]
        for offset in range(0, len(rows), self.page_size):
            yield {"Contents": rows[offset:offset + self.page_size]}


class FakeR2:
    def __init__(self):
        self.objects: dict[str, dict] = {}
        self.operations: list[tuple[str, str]] = []
        self.fail_upload_suffix = ""
        self.lock = threading.Lock()

    def get_paginator(self, name: str):
        if name != "list_objects_v2":
            raise ValueError(name)
        return FakePaginator(self)

    def get_object(self, *, Bucket: str, Key: str):
        del Bucket
        with self.lock:
            self.operations.append(("get", Key))
            if Key not in self.objects:
                raise MissingObject(Key)
            return {"Body": io.BytesIO(self.objects[Key]["body"])}

    def head_object(self, *, Bucket: str, Key: str):
        del Bucket
        with self.lock:
            self.operations.append(("head", Key))
            if Key not in self.objects:
                raise MissingObject(Key)
            row = self.objects[Key]
            return {
                "ContentLength": len(row["body"]),
                "Metadata": dict(row.get("metadata") or {}),
            }

    def put_object(self, *, Bucket: str, Key: str, Body, Metadata=None, **kwargs):
        del Bucket, kwargs
        body = Body.read() if hasattr(Body, "read") else Body
        if isinstance(body, str):
            body = body.encode("utf-8")
        with self.lock:
            self.operations.append(("put", Key))
            self.objects[Key] = {"body": bytes(body), "metadata": dict(Metadata or {})}
        return {}

    def upload_file(self, filename: str, bucket: str, key: str, **kwargs):
        del bucket
        if self.fail_upload_suffix and key.endswith(self.fail_upload_suffix):
            raise RuntimeError("injected upload failure")
        extra = kwargs.get("ExtraArgs") or {}
        with self.lock:
            self.operations.append(("upload", key))
            self.objects[key] = {
                "body": Path(filename).read_bytes(),
                "metadata": dict(extra.get("Metadata") or {}),
            }

    def delete_objects(self, *, Bucket: str, Delete: dict):
        del Bucket
        with self.lock:
            for item in Delete.get("Objects") or []:
                key = item["Key"]
                self.operations.append(("delete", key))
                self.objects.pop(key, None)
        return {}


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def build_site(root: Path) -> None:
    write(root / "index.html", "home")
    write(root / "404.html", "missing")
    write(root / "assets/app.js", "console.log('v1')")
    write(root / "reports/institutions/bernstein/index.html", "bernstein")
    write(root / "b7c3e9a41d8f52e604a71bc93f2d6e80.txt", "key")
    write(root / "data/catalog.json", json.dumps({"items": [{"id": "ab-report"}]}))
    write(root / "data/search_index.json", "{}")
    write(root / "data/password_rules.json", "{}")
    write(root / "data/catalog_recommendations.json", "{}")
    write(root / "data/report_details/ab.json", json.dumps({"reports": {"ab-report": {}}}))


def release(number: int) -> str:
    return f"{number:032x}"


class StaticSlotPublisherTests(unittest.TestCase):
    def publish(self, client: FakeR2, root: Path, number: int, active: str = ""):
        return publisher.publish_static_slot(
            client,
            "bucket",
            root,
            release(number),
            active,
            max_workers=4,
        )

    def test_two_complete_slots_then_zero_and_single_file_content_uploads(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()

            first = self.publish(client, root, 1)
            self.assertEqual(first["static_slot"], "a")
            self.assertEqual(first["uploaded_files"], first["file_count"])
            self.assertEqual(first["skipped_files"], 0)

            second = self.publish(client, root, 2, "a")
            self.assertEqual(second["static_slot"], "b")
            self.assertEqual(second["uploaded_files"], second["file_count"])

            third = self.publish(client, root, 3, "b")
            self.assertEqual(third["static_slot"], "a")
            self.assertEqual(third["uploaded_files"], 0)
            self.assertEqual(third["skipped_files"], third["file_count"])
            self.assertEqual(third["runtime_uploaded_files"], 0)
            self.assertEqual(third["runtime_skipped_files"], 3)

            write(root / "assets/app.js", "console.log('v2')")
            fourth = self.publish(client, root, 4, "a")
            self.assertEqual(fourth["static_slot"], "b")
            self.assertEqual(fourth["uploaded_files"], 1)
            self.assertEqual(fourth["skipped_files"], fourth["file_count"] - 1)

    def test_removed_object_is_deleted_from_inactive_slot(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            write(root / "obsolete.txt", "remove me")
            client = FakeR2()
            self.publish(client, root, 1)
            self.publish(client, root, 2, "a")

            (root / "obsolete.txt").unlink()
            result = self.publish(client, root, 3, "b")
            self.assertEqual(result["deleted_files"], 1)
            self.assertNotIn(publisher.slot_prefix("a") + "obsolete.txt", client.objects)
            self.assertIn(publisher.slot_prefix("b") + "obsolete.txt", client.objects)

    def test_failed_upload_keeps_previous_manifest_and_forces_clean_recovery(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            self.publish(client, root, 1)
            self.publish(client, root, 2, "a")
            manifest_key = publisher.manifest_key("a")
            previous_manifest = client.objects[manifest_key]["body"]

            write(root / "assets/app.js", "console.log('broken run')")
            client.fail_upload_suffix = "assets/app.js"
            with self.assertRaisesRegex(RuntimeError, "injected upload failure"):
                self.publish(client, root, 3, "b")
            self.assertEqual(client.objects[manifest_key]["body"], previous_manifest)
            self.assertIn(publisher.incomplete_key("a"), client.objects)

            client.fail_upload_suffix = ""
            recovered = self.publish(client, root, 4, "b")
            self.assertTrue(recovered["recovered_incomplete_slot"])
            self.assertEqual(recovered["uploaded_files"], recovered["file_count"])
            self.assertNotIn(publisher.incomplete_key("a"), client.objects)

    def test_manifest_is_committed_after_all_slot_content_uploads(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            self.publish(client, root, 1)
            manifest_operation = client.operations.index(("put", publisher.manifest_key("a")))
            content_operations = [
                index
                for index, operation in enumerate(client.operations)
                if operation[0] == "upload" and operation[1].startswith(publisher.slot_prefix("a"))
            ]
            self.assertTrue(content_operations)
            self.assertGreater(manifest_operation, max(content_operations))

    def test_tree_verification_uses_every_paginated_object(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            for index in range(11):
                write(root / "many" / f"{index:02d}.txt", str(index))
            client = FakeR2()
            result = self.publish(client, root, 1)
            slot_objects = [key for key in client.objects if key.startswith(publisher.slot_prefix("a"))]
            self.assertEqual(len(slot_objects), result["file_count"])

    def test_tree_digest_ignores_mtime_and_changes_with_served_content(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            _paths, _entries, first_digest, _total = publisher.build_inventory(root)
            app_path = root / "assets/app.js"
            os.utime(app_path, (2_000_000_000, 2_000_000_000))
            _paths, _entries, touched_digest, _total = publisher.build_inventory(root)
            self.assertEqual(touched_digest, first_digest)
            write(app_path, "console.log('changed')")
            _paths, _entries, changed_digest, _total = publisher.build_inventory(root)
            self.assertNotEqual(changed_digest, first_digest)

    def test_invalid_release_and_symlink_are_rejected_before_upload(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            with self.assertRaisesRegex(ValueError, "Release id"):
                publisher.publish_static_slot(client, "bucket", root, "latest")
            (root / "linked.html").symlink_to(root / "index.html")
            with self.assertRaisesRegex(ValueError, "symbolic links"):
                self.publish(client, root, 1)
            self.assertFalse(any(operation[0] in {"put", "upload"} for operation in client.operations))


if __name__ == "__main__":
    unittest.main()
