#!/usr/bin/env python3

from __future__ import annotations

import io
import json
import os
import tempfile
import threading
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

from PIL import Image

import publish_static_slot as publisher


class MissingObject(KeyError):
    response = {"Error": {"Code": "NoSuchKey"}}


class R2UploadError(RuntimeError):
    def __init__(self, code: str):
        super().__init__(f"injected R2 upload error: {code}")
        self.response = {"Error": {"Code": code}}


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
        self.upload_attempts: dict[str, int] = {}
        self.upload_failures: dict[str, list[BaseException]] = {}
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
                "ContentType": row.get("content_type") or "",
                "CacheControl": row.get("cache_control") or "",
            }

    def put_object(self, *, Bucket: str, Key: str, Body, Metadata=None, **kwargs):
        del Bucket
        body = Body.read() if hasattr(Body, "read") else Body
        if isinstance(body, str):
            body = body.encode("utf-8")
        with self.lock:
            self.operations.append(("put", Key))
            self.objects[Key] = {
                "body": bytes(body),
                "metadata": dict(Metadata or {}),
                "content_type": kwargs.get("ContentType") or "",
                "cache_control": kwargs.get("CacheControl") or "",
            }
        return {}

    def upload_file(self, filename: str, bucket: str, key: str, **kwargs):
        del bucket
        with self.lock:
            self.upload_attempts[key] = self.upload_attempts.get(key, 0) + 1
            failures = self.upload_failures.get(key) or []
            if failures:
                error = failures.pop(0)
                raise error
        if self.fail_upload_suffix and key.endswith(self.fail_upload_suffix):
            raise RuntimeError("injected upload failure")
        extra = kwargs.get("ExtraArgs") or {}
        with self.lock:
            self.operations.append(("upload", key))
            self.objects[key] = {
                "body": Path(filename).read_bytes(),
                "metadata": dict(extra.get("Metadata") or {}),
                "content_type": extra.get("ContentType") or "",
                "cache_control": extra.get("CacheControl") or "",
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
    write(root / "index.html", "KC桌面 home")
    write(root / "404.html", "missing")
    write(root / "assets/app-mark.svg", '<svg role="img" aria-label="KC桌面"></svg>')
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


def wrapped_upload_error(code: str) -> BaseException:
    try:
        try:
            raise R2UploadError(code)
        except R2UploadError:
            raise RuntimeError("boto3 upload wrapper")
    except RuntimeError as error:
        return error


class StaticSlotPublisherTests(unittest.TestCase):
    def member_contact_card(self) -> Path:
        handle = tempfile.NamedTemporaryFile(suffix="-member-contact-card.jpg", delete=False)
        handle.close()
        path = Path(handle.name)
        Image.effect_noise((640, 800), 32).convert("RGB").save(
            path,
            format="JPEG",
            quality=92,
            subsampling=0,
        )
        self.addCleanup(path.unlink, missing_ok=True)
        return path

    def publish(
        self,
        client: FakeR2,
        root: Path,
        number: int,
        active: str = "",
        *,
        member_contact_card: Path | None = None,
        skip_shared_private_assets: bool = False,
    ):
        return publisher.publish_static_slot(
            client,
            "bucket",
            root,
            release(number),
            active,
            member_contact_card=member_contact_card or self.member_contact_card(),
            skip_shared_private_assets=skip_shared_private_assets,
            max_workers=4,
        )

    def test_progress_is_flushed_and_bounded_by_count_or_elapsed_time(self) -> None:
        with patch.object(publisher.time, "monotonic", return_value=0.0) as clock:
            with patch("builtins.print") as output:
                progress = publisher._PublishProgress("upload_static", total=2000, workers=16)
                for completed in range(1, 1000):
                    progress.update(completed)
                self.assertEqual(output.call_count, 1)
                progress.update(1000, bytes=5000)
                progress.update(1001)
                self.assertEqual(output.call_count, 2)
                clock.return_value = 30.0
                progress.update(1002, bytes=5010)
                progress.finish(completed=1002, bytes=5010)
                self.assertEqual(output.call_count, 4)
        messages = [call.args[0] for call in output.call_args_list]
        self.assertIn("state=started elapsed_seconds=0.0 total=2000 workers=16", messages[0])
        self.assertIn("completed=1000 bytes=5000", messages[1])
        self.assertIn("state=progress elapsed_seconds=30.0", messages[2])
        self.assertIn("state=completed elapsed_seconds=30.0", messages[3])
        self.assertTrue(all(call.kwargs.get("flush") is True for call in output.call_args_list))
        self.assertTrue(all(call.kwargs.get("file") is publisher.sys.stderr for call in output.call_args_list))

    def test_progress_distinguishes_publish_phases_and_never_reports_failed_commit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            output = io.StringIO()
            with redirect_stderr(output):
                result = self.publish(client, root, 1)
            messages = output.getvalue()
            for phase in (
                "brand_validation", "local_inventory", "remote_inventory",
                "verify_unchanged", "upload_static", "cleanup_stale", "verify_tree",
                "verify_required", "shared_private_assets", "immutable_runtime", "commit_manifest",
            ):
                self.assertIn(f"phase={phase} state=started", messages)
                self.assertIn(f"phase={phase} state=completed", messages)
            self.assertIn(f"completed={result['uploaded_files']} bytes={result['uploaded_bytes']}", messages)
            self.assertNotIn("assets/app.js", messages)

            output = io.StringIO()
            client.fail_upload_suffix = "assets/app.js"
            with redirect_stderr(output):
                with self.assertRaisesRegex(RuntimeError, "injected upload failure"):
                    self.publish(client, root, 2, "a")
            self.assertIn("phase=upload_static state=started", output.getvalue())
            self.assertNotIn("phase=upload_static state=completed", output.getvalue())
            self.assertNotIn("phase=commit_manifest", output.getvalue())

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
            self.assertEqual(third["runtime_uploaded_files"], 3)
            self.assertEqual(third["runtime_skipped_files"], 0)

            write(root / "assets/app.js", "console.log('v2')")
            fourth = self.publish(client, root, 4, "a")
            self.assertEqual(fourth["static_slot"], "b")
            self.assertEqual(fourth["uploaded_files"], 1)
            self.assertEqual(fourth["skipped_files"], fourth["file_count"] - 1)

    def test_same_length_overwrite_without_digest_metadata_is_reuploaded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            self.publish(client, root, 1)
            self.publish(client, root, 2, "a")

            app_key = publisher.slot_prefix("a") + "assets/app.js"
            expected = (root / "assets/app.js").read_bytes()
            corrupted = b"x" * len(expected)
            self.assertNotEqual(corrupted, expected)
            client.put_object(Bucket="bucket", Key=app_key, Body=corrupted)

            result = self.publish(client, root, 3, "b")

            self.assertEqual(result["uploaded_files"], 1)
            self.assertEqual(result["skipped_files"], result["file_count"] - 1)
            self.assertEqual(client.objects[app_key]["body"], expected)
            self.assertEqual(
                client.objects[app_key]["metadata"].get("sha256"),
                publisher.sha256_file(root / "assets/app.js"),
            )

    def test_required_object_without_digest_metadata_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            paths, entries, _tree_sha256, _total_bytes = publisher.build_inventory(root)
            relative = publisher.DEFAULT_REQUIRED_PATHS[0]
            key = publisher.slot_prefix("a") + relative
            client.put_object(
                Bucket="bucket",
                Key=key,
                Body=paths[relative].read_bytes(),
            )

            with self.assertRaisesRegex(RuntimeError, "wrong digest"):
                publisher.verify_required_objects(
                    client,
                    "bucket",
                    publisher.slot_prefix("a"),
                    paths,
                    entries,
                    (relative,),
                )

    def test_transient_upload_errors_retry_then_succeed_with_bounded_backoff(self) -> None:
        with tempfile.NamedTemporaryFile() as handle:
            client = FakeR2()
            key = "edge-static/slots/a/retry.txt"
            client.upload_failures[key] = [
                wrapped_upload_error("ServiceUnavailable"),
                R2UploadError("SlowDown"),
            ]
            delays: list[float] = []

            publisher.upload_file_with_retry(
                client,
                handle.name,
                "bucket",
                key,
                retry_sleep=delays.append,
            )

            self.assertEqual(client.upload_attempts[key], 3)
            self.assertEqual(delays, [5.0, 10.0])
            self.assertIn(key, client.objects)

    def test_transient_upload_error_stops_after_four_total_attempts(self) -> None:
        with tempfile.NamedTemporaryFile() as handle:
            client = FakeR2()
            key = "edge-static/slots/a/exhausted.txt"
            client.upload_failures[key] = [
                R2UploadError("ServiceUnavailable") for _ in range(4)
            ]
            delays: list[float] = []

            with self.assertRaisesRegex(R2UploadError, "ServiceUnavailable"):
                publisher.upload_file_with_retry(
                    client,
                    handle.name,
                    "bucket",
                    key,
                    retry_sleep=delays.append,
                )

            self.assertEqual(client.upload_attempts[key], 4)
            self.assertEqual(delays, [5.0, 10.0, 20.0])
            self.assertNotIn(key, client.objects)

    def test_permanent_upload_error_is_not_retried(self) -> None:
        with tempfile.NamedTemporaryFile() as handle:
            client = FakeR2()
            key = "edge-static/slots/a/denied.txt"
            client.upload_failures[key] = [R2UploadError("AccessDenied")]
            delays: list[float] = []

            with self.assertRaisesRegex(R2UploadError, "AccessDenied"):
                publisher.upload_file_with_retry(
                    client,
                    handle.name,
                    "bucket",
                    key,
                    retry_sleep=delays.append,
                )

            self.assertEqual(client.upload_attempts[key], 1)
            self.assertEqual(delays, [])
            self.assertNotIn(key, client.objects)

    def test_runtime_data_is_immutable_per_release_and_never_overwrites_legacy_shared_data(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            client.objects[f"{publisher.RUNTIME_ROOT}/catalog.json"] = {
                "body": b'{"legacy":true}',
                "metadata": {"sha256": "legacy"},
            }

            first = self.publish(client, root, 1)
            first_prefix = publisher.runtime_release_prefix(release(1))
            self.assertEqual(first["runtime_prefix"], first_prefix)
            self.assertEqual(first["runtime_uploaded_files"], 3)
            self.assertIn(first_prefix + "catalog.json", client.objects)
            self.assertIn(publisher.runtime_manifest_key(release(1)), client.objects)
            self.assertEqual(
                client.objects[f"{publisher.RUNTIME_ROOT}/catalog.json"]["body"],
                b'{"legacy":true}',
            )

            write(root / "data/catalog.json", json.dumps({"items": [{"id": "ab-report"}], "revision": 2}))
            second = self.publish(client, root, 2, "a")
            second_prefix = publisher.runtime_release_prefix(release(2))
            self.assertEqual(second["runtime_prefix"], second_prefix)
            self.assertNotEqual(
                client.objects[first_prefix + "catalog.json"]["body"],
                client.objects[second_prefix + "catalog.json"]["body"],
            )
            self.assertIn(first_prefix + "catalog.json", client.objects)
            self.assertIn(second_prefix + "catalog.json", client.objects)

            first_manifest = json.loads(
                client.objects[publisher.runtime_manifest_key(release(1))]["body"]
            )
            second_manifest = json.loads(
                client.objects[publisher.runtime_manifest_key(release(2))]["body"]
            )
            self.assertEqual(first_manifest["release_id"], release(1))
            self.assertEqual(second_manifest["release_id"], release(2))
            self.assertEqual(
                json.loads(client.objects[publisher.manifest_key("b")]["body"])["runtime_data"],
                {
                    "schema_version": publisher.RUNTIME_SCHEMA_VERSION,
                    "release_id": release(2),
                    "prefix": second_prefix,
                    "tree_sha256": second["runtime_tree_sha256"],
                },
            )

    def test_retry_of_same_runtime_release_skips_verified_objects_and_rejects_content_collision(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            first = publisher.sync_runtime_data(client, "bucket", root, release(7))
            second = publisher.sync_runtime_data(client, "bucket", root, release(7))
            self.assertEqual(first[:2], (3, 0))
            self.assertEqual(second[:2], (0, 3))
            prefix = publisher.runtime_release_prefix(release(7))
            manifest = first[2]
            for filename, descriptor in manifest["files"].items():
                self.assertEqual(descriptor["content_type"], "application/json")
                self.assertEqual(descriptor["cache_control"], "no-store")
                head = client.head_object(Bucket="bucket", Key=prefix + filename)
                self.assertEqual(head["ContentType"], descriptor["content_type"])
                self.assertEqual(head["CacheControl"], descriptor["cache_control"])

            client.objects[prefix + "catalog.json"]["metadata"]["release-id"] = release(8)
            repaired = publisher.sync_runtime_data(client, "bucket", root, release(7))
            self.assertEqual(repaired[:2], (1, 2), "wrong release metadata must force re-upload")
            self.assertEqual(
                client.objects[prefix + "catalog.json"]["metadata"]["release-id"],
                release(7),
            )

            write(root / "data/search_index.json", '{"changed":true}')
            with self.assertRaisesRegex(RuntimeError, "already committed with different content"):
                publisher.sync_runtime_data(client, "bucket", root, release(7))

    def test_failed_runtime_upload_does_not_commit_static_or_runtime_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            client.fail_upload_suffix = "search_index.json"
            with self.assertRaisesRegex(RuntimeError, "injected upload failure"):
                self.publish(client, root, 9)
            self.assertNotIn(publisher.runtime_manifest_key(release(9)), client.objects)
            self.assertNotIn(publisher.manifest_key("a"), client.objects)
            self.assertIn(publisher.incomplete_key("a"), client.objects)

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

    def test_private_member_card_is_verified_outside_public_inventory_before_commit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            for key in publisher.LEGACY_PUBLIC_CONTACT_CARD_KEYS:
                client.objects[key] = {
                    "body": b"legacy-public-contact-card",
                    "metadata": {},
                }
            member_card = self.member_contact_card()
            result = self.publish(client, root, 1, member_contact_card=member_card)

            self.assertEqual(
                result["legacy_public_contact_cards_removed"],
                len(publisher.LEGACY_PUBLIC_CONTACT_CARD_KEYS),
            )
            for key in publisher.LEGACY_PUBLIC_CONTACT_CARD_KEYS:
                self.assertNotIn(key, client.objects)

            private_row = client.objects[publisher.MEMBER_CONTACT_CARD_KEY]
            self.assertEqual(private_row["content_type"], "image/jpeg")
            self.assertEqual(
                private_row["cache_control"],
                publisher.MEMBER_CONTACT_CARD_CACHE_CONTROL,
            )
            self.assertEqual(
                private_row["metadata"],
                {"sha256": result["member_contact_card_sha256"]},
            )
            self.assertEqual(len(private_row["body"]), result["member_contact_card_bytes"])

            slot_prefix = publisher.slot_prefix("a")
            manifest = json.loads(client.objects[publisher.manifest_key("a")]["body"])
            self.assertNotIn(publisher.MEMBER_CONTACT_CARD_KEY, manifest["files"])
            self.assertFalse(
                any(
                    key.startswith(slot_prefix) and "member-contact-card" in key
                    for key in client.objects
                )
            )

            private_upload = client.operations.index(("upload", publisher.MEMBER_CONTACT_CARD_KEY))
            private_head = client.operations.index(("head", publisher.MEMBER_CONTACT_CARD_KEY))
            legacy_deletes = [
                client.operations.index(("delete", key))
                for key in publisher.LEGACY_PUBLIC_CONTACT_CARD_KEYS
            ]
            legacy_absence_checks = [
                max(
                    index
                    for index, operation in enumerate(client.operations)
                    if operation == ("head", key)
                )
                for key in publisher.LEGACY_PUBLIC_CONTACT_CARD_KEYS
            ]
            static_uploads = [
                index
                for index, operation in enumerate(client.operations)
                if operation[0] == "upload" and operation[1].startswith(slot_prefix)
            ]
            required_heads = [
                index
                for index, operation in enumerate(client.operations)
                if operation[0] == "head" and operation[1].startswith(slot_prefix)
            ]
            manifest_commit = client.operations.index(("put", publisher.manifest_key("a")))
            self.assertGreater(private_upload, max(static_uploads))
            self.assertGreater(private_upload, max(required_heads))
            self.assertGreater(private_upload, max(legacy_deletes))
            self.assertGreater(private_upload, max(legacy_absence_checks))
            self.assertGreater(private_head, private_upload)
            self.assertGreater(manifest_commit, private_head)

    def test_skip_shared_private_assets_preserves_every_qr_object_without_accessing_local_card(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            original_qr_objects = {
                publisher.MEMBER_CONTACT_CARD_KEY: b"existing-private-contact-card",
                **{
                    key: f"existing-{key}".encode("utf-8")
                    for key in publisher.LEGACY_PUBLIC_CONTACT_CARD_KEYS
                },
            }
            for key, body in original_qr_objects.items():
                client.objects[key] = {"body": body, "metadata": {}}

            missing_card = root.parent / f"{root.name}-missing-member-contact.jpg"
            result = self.publish(
                client,
                root,
                1,
                member_contact_card=missing_card,
                skip_shared_private_assets=True,
            )

            self.assertFalse(result["shared_private_assets_published"])
            self.assertEqual(result["legacy_public_contact_cards_removed"], 0)
            self.assertEqual(result["member_contact_card_sha256"], "")
            self.assertEqual(result["member_contact_card_bytes"], 0)
            for key, body in original_qr_objects.items():
                self.assertEqual(client.objects[key]["body"], body)
                self.assertFalse(any(operation[1] == key for operation in client.operations))
            self.assertIn(publisher.manifest_key("a"), client.objects)

    def test_missing_or_bad_private_member_card_fails_before_remote_calls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            missing = root.parent / f"{root.name}-missing-member-contact.jpg"
            with self.assertRaisesRegex(ValueError, "real JPEG"):
                self.publish(client, root, 1, member_contact_card=missing)
            self.assertEqual(client.operations, [])

            handle = tempfile.NamedTemporaryFile(suffix="-bad-member-contact.jpg", delete=False)
            handle.write(b"\xff\xd8\xff" + b"not-a-real-jpeg" * 400 + b"\xff\xd9")
            handle.close()
            bad = Path(handle.name)
            self.addCleanup(bad.unlink, missing_ok=True)
            with self.assertRaisesRegex(ValueError, "valid JPEG"):
                self.publish(client, root, 2, member_contact_card=bad)
            self.assertEqual(client.operations, [])

            inside_public_root = root / "member-contact-card.jpg"
            inside_public_root.write_bytes(self.member_contact_card().read_bytes())
            with self.assertRaisesRegex(ValueError, "outside the public static root"):
                self.publish(client, root, 3, member_contact_card=inside_public_root)
            self.assertEqual(client.operations, [])

    def test_private_member_card_upload_failure_leaves_slot_uncommitted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            client = FakeR2()
            client.fail_upload_suffix = publisher.MEMBER_CONTACT_CARD_KEY
            with self.assertRaisesRegex(RuntimeError, "injected upload failure"):
                self.publish(client, root, 1)
            self.assertTrue(
                any(
                    operation[0] == "upload"
                    and operation[1].startswith(publisher.slot_prefix("a"))
                    for operation in client.operations
                )
            )
            self.assertNotIn(publisher.MEMBER_CONTACT_CARD_KEY, client.objects)
            self.assertNotIn(publisher.manifest_key("a"), client.objects)
            self.assertIn(publisher.incomplete_key("a"), client.objects)

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
                publisher.publish_static_slot(
                    client,
                    "bucket",
                    root,
                    "latest",
                    member_contact_card=self.member_contact_card(),
                )
            (root / "linked.html").symlink_to(root / "index.html")
            with self.assertRaisesRegex(ValueError, "symbolic links"):
                self.publish(client, root, 1)
            self.assertFalse(any(operation[0] in {"put", "upload"} for operation in client.operations))

    def test_public_brand_violation_is_rejected_before_any_remote_call(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            build_site(root)
            write(root / "assets/app.js", "showError('Reportify is unavailable')")
            client = FakeR2()
            with self.assertRaisesRegex(ValueError, "Public brand check failed"):
                self.publish(client, root, 1)
            self.assertEqual(client.operations, [])


if __name__ == "__main__":
    unittest.main()
