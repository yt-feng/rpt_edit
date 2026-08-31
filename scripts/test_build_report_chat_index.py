#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import importlib.util
import json
import struct
import tempfile
import unittest
from io import BytesIO
from pathlib import Path


SCRIPT = Path(__file__).with_name("build_report_chat_index.py")
SPEC = importlib.util.spec_from_file_location("build_report_chat_index", SCRIPT)
assert SPEC and SPEC.loader
indexer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(indexer)


class MissingObject(Exception):
    response = {"Error": {"Code": "NoSuchKey"}}


class FakeR2:
    def __init__(self, fail_key_suffix: str = "") -> None:
        self.objects: dict[str, bytes] = {}
        self.metadata: dict[str, dict[str, str]] = {}
        self.operations: list[tuple[str, str]] = []
        self.fail_key_suffix = fail_key_suffix

    def head_object(self, *, Bucket: str, Key: str):
        del Bucket
        self.operations.append(("head", Key))
        if Key not in self.objects:
            raise MissingObject()
        return {
            "ContentLength": len(self.objects[Key]),
            "Metadata": self.metadata.get(Key, {}),
        }

    def put_object(self, *, Bucket: str, Key: str, Body: bytes, **kwargs):
        del Bucket, kwargs
        self.operations.append(("put", Key))
        if self.fail_key_suffix and Key.endswith(self.fail_key_suffix):
            raise RuntimeError("injected upload failure")
        body = bytes(Body)
        self.objects[Key] = body
        self.metadata[Key] = {"sha256": hashlib.sha256(body).hexdigest()}

    def get_object(self, *, Bucket: str, Key: str):
        del Bucket
        self.operations.append(("get", Key))
        if Key not in self.objects:
            raise MissingObject()
        return {"Body": BytesIO(self.objects[Key])}


def lookup(output: Path, descriptor: dict, key: str):
    bucket = indexer.bucket_index(key, descriptor["bucket_count"])
    table_path = output / Path(descriptor["table_key"]).name
    data_path = output / Path(descriptor["data_key"]).name
    with table_path.open("rb") as table:
        table.seek(bucket * descriptor["slot_size"])
        offset, length = struct.unpack(">QI", table.read(descriptor["slot_size"]))
    if not length:
        return None
    with data_path.open("rb") as data:
        data.seek(offset)
        entries = json.loads(data.read(length))
    return next((value for exact, value in entries if exact == key), None)


class ReportChatIndexTests(unittest.TestCase):
    def catalog(self) -> dict:
        return {
            "schema_version": 1,
            "updated_at_bjt": "2026-08-12 20:00:00 +0800",
            "items": [
                {
                    "id": "a" * 24,
                    "title": "JPMorgan MLCC industry outlook 260812",
                    "title_zh": "摩根大通：MLCC 行业展望-260812",
                    "filename": "private-a.pdf",
                    "date_folder": "260812",
                    "bank_code": "JPM",
                    "bank_name": "摩根大通",
                    "size_bytes": 100,
                    "page_count": 12,
                    "available": True,
                    "r2_key": "reports/private-a.pdf",
                    "source_path": "/a/private/source",
                },
                {
                    "id": "b" * 24,
                    "title": "Battery supply chain 260811",
                    "title_zh": "电池供应链更新-260811",
                    "date_folder": "260811",
                    "bank_code": "ABC",
                    "bank_name": "中性机构",
                    "page_count": 8,
                    "r2_synced": True,
                    "r2_key": "reports/private-b.pdf",
                },
                {
                    "id": "not-an-id",
                    "title": "must be rejected",
                },
            ],
        }

    def build(self, root: Path) -> tuple[Path, dict]:
        catalog = root / "catalog.json"
        output = root / "output"
        catalog.write_text(json.dumps(self.catalog(), ensure_ascii=False), encoding="utf-8")
        manifest = indexer.build_index(
            catalog,
            output,
            token_bucket_count=8,
            item_bucket_count=4,
        )
        return output, manifest

    def test_tokenization_supports_latin_numbers_and_cjk_grams(self) -> None:
        tokens = indexer.search_tokens("MLCC 0201 电池供应链")
        self.assertIn("mlcc", tokens)
        self.assertIn("0201", tokens)
        self.assertIn("电池", tokens)
        self.assertIn("池供应", tokens)
        self.assertIn("供应链", tokens)
        self.assertIn("电池供应链", tokens)

    def test_builds_fixed_slot_random_access_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            self.assertEqual(manifest["schema_version"], 2)
            self.assertEqual(manifest["item_count"], 2)
            self.assertEqual(len(manifest["default_items"]), 2)
            for name in ("token_table", "item_table"):
                descriptor = manifest[name]
                table = output / Path(descriptor["table_key"]).name
                self.assertEqual(table.stat().st_size, descriptor["bucket_count"] * 12)
                self.assertEqual(descriptor["slot_size"], 12)

            report_ids = lookup(output, manifest["token_table"], "mlcc")
            self.assertEqual(report_ids, ["a" * 24])
            cjk_ids = lookup(output, manifest["token_table"], "供应链")
            self.assertEqual(cjk_ids, ["b" * 24])
            report = lookup(output, manifest["item_table"], "a" * 24)
            self.assertEqual(report["institution"], "JPM · 摩根大通")
            self.assertEqual(report["industry"], "Other")
            self.assertEqual(report["attraction_score"], 5)

            persisted = b"".join(path.read_bytes() for path in output.iterdir())
            self.assertNotIn(b"reports/private", persisted)
            self.assertNotIn(b"/a/private/source", persisted)
            self.assertNotIn(b"private-a.pdf", persisted)

    def test_collision_bucket_requires_exact_key(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            table = root / "table.bin"
            data = root / "data.bin"
            descriptor = indexer.write_bucket_table(
                {"alpha": ["a"], "beta": ["b"], "gamma": ["c"]},
                table,
                data,
                requested_bucket_count=1,
            )
            descriptor.update({"table_key": "table.bin", "data_key": "data.bin"})
            self.assertEqual(lookup(root, descriptor, "beta"), ["b"])
            self.assertIsNone(lookup(root, descriptor, "missing"))

    def test_postings_and_defaults_are_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            catalog = {
                "items": [
                    {
                        "id": f"{number:024x}",
                        "title": f"Semiconductor outlook {number}",
                        "date_folder": f"2608{number % 28 + 1:02d}",
                        "available": True,
                    }
                    for number in range(1, 81)
                ],
            }
            catalog_path = root / "catalog.json"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
            output = root / "output"
            manifest = indexer.build_index(catalog_path, output, token_bucket_count=16, item_bucket_count=16)
            self.assertEqual(len(lookup(output, manifest["token_table"], "semiconductor")), indexer.POSTING_LIMIT)
            self.assertEqual(len(manifest["default_items"]), indexer.CANDIDATE_LIMIT)

    def test_release_and_bytes_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_output, first_manifest = self.build(Path(first))
            second_output, second_manifest = self.build(Path(second))
            self.assertEqual(first_manifest, second_manifest)
            for filename in ("manifest.json", "tokens.tbl", "tokens.dat", "items.tbl", "items.dat"):
                self.assertEqual((first_output / filename).read_bytes(), (second_output / filename).read_bytes())

    def test_manifest_is_published_last_and_only_after_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            client = FakeR2()
            indexer.publish_index(client, "private-bucket", output)
            manifest_key = "_report-chat/v2/manifest.json"
            puts = [key for operation, key in client.operations if operation == "put"]
            self.assertEqual(puts[-1], manifest_key)
            self.assertEqual(json.loads(client.objects[manifest_key]), manifest)

            # Re-publishing a deterministic release must not rewrite immutable data.
            client.operations.clear()
            indexer.publish_index(client, "private-bucket", output)
            immutable_puts = [key for operation, key in client.operations if operation == "put" and key != manifest_key]
            self.assertEqual(immutable_puts, [])

    def test_failed_immutable_upload_never_commits_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, _manifest = self.build(Path(temporary))
            client = FakeR2(fail_key_suffix="items.dat")
            with self.assertRaisesRegex(RuntimeError, "injected"):
                indexer.publish_index(client, "private-bucket", output)
            self.assertNotIn("_report-chat/v2/manifest.json", client.objects)

    def test_neutral_edge_transaction_does_not_publish_the_shared_manifest(self) -> None:
        workflow = SCRIPT.parent.parent.joinpath(".github/workflows/neutral-edge-cutover.yml").read_text(encoding="utf-8")
        self.assertNotIn("scripts/build_report_chat_index.py", workflow)
        self.assertNotIn("_report-chat/v2/manifest.json", workflow)


if __name__ == "__main__":
    unittest.main()
