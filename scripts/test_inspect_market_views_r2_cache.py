#!/usr/bin/env python3
"""Real gzip private checkpoint fixtures with injected read-only R2 clients."""
from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import inspect_market_views_r2_cache as inventory


def json_bytes(value):
    return json.dumps(value, sort_keys=True).encode()


def archive_bytes(files):
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode="w:gz") as archive:
        for name, data in files.items():
            member = tarfile.TarInfo(name)
            member.size = len(data)
            archive.addfile(member, io.BytesIO(data))
    return output.getvalue()


class FakeR2:
    def __init__(self):
        self.objects, self.calls = {}, []

    def add(self, key, payload, content_type="application/gzip", metadata=None):
        self.objects[key] = {"Body": payload, "ContentLength": len(payload), "ContentType": content_type,
                             "Metadata": metadata if metadata is not None else {"sha256": hashlib.sha256(payload).hexdigest()}}

    def head_object(self, **kwargs):
        key = kwargs["Key"]
        self.calls.append(("head", key))
        return {k: v for k, v in self.objects[key].items() if k != "Body"}

    def get_object(self, **kwargs):
        key = kwargs["Key"]
        self.calls.append(("get", key))
        return {"Body": io.BytesIO(self.objects[key]["Body"])}

    def list_objects_v2(self, **kwargs):
        self.calls.append(("list", kwargs["Prefix"]))
        keys = sorted(key for key in self.objects if key.startswith(kwargs["Prefix"]))
        offset = int(kwargs.get("ContinuationToken", "0"))
        selected = keys[offset:offset + kwargs["MaxKeys"]]
        truncated = offset + len(selected) < len(keys)
        return {"Contents": [{"Key": key} for key in selected], "IsTruncated": truncated,
                "NextContinuationToken": str(offset + len(selected)) if truncated else None}


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeR2()
        self.identity = "a" * 64
        self.key = f"_workflow-cache/report-generation/v1/261003/shard_2/{self.identity}.tar.gz"
        self.files = {
            "_generation_checkpoint.json": json_bytes({"version": 1, "identity": self.identity, "complete": False}),
            "private-title/source_mineru.md": b"# Original private report source\n",
            "private-title/status.json": json_bytes({"source_pdf": "secret-title.pdf", "original_pdf_sha256": "b" * 64}),
            "private-title/assets/chart.png": b"synthetic-chart-bytes",
        }
        self.add_archive()

    def add_archive(self, files=None, key=None):
        self.client.add(key or self.key, archive_bytes(files or self.files))

    def inspect(self):
        with redirect_stdout(io.StringIO()):
            return inventory.inspect_cache(self.client, "private-bucket")

    def row(self, result=None):
        return (result or self.inspect())["dates"][2]["archives"][0]

    def add_pdf_pair(self):
        payload = b"%PDF-1.7\n" + b"x" * 1500
        digest = hashlib.sha256(payload).hexdigest()
        self.client.add("_market-views/pdfs/261003.pdf", payload, "application/pdf",
                        {"date-key": "261003", "sha256": digest})
        self.client.add("_market-views/items/261003.json", json_bytes({
            "schema_version": 1, "id": "market-view:261003", "date_key": "261003", "date": "2026-10-03",
            "filename": "market_views_261003.pdf", "pdf_key": "_market-views/pdfs/261003.pdf",
            "size_bytes": len(payload), "sha256": digest, "content_type": "application/pdf",
        }), "application/json")

    def test_verified_real_gzip_counts_without_assuming_current_source_binding(self):
        row = self.row()
        self.assertTrue(row["verified"])
        self.assertEqual(row["stored_checkpoint_identity"], self.identity)
        self.assertEqual(row["shard_index"], 2)
        for field in ("source_count", "nonempty_source_count", "status_count", "report_binding_count",
                      "pdf_hash_binding_count", "asset_file_count"):
            self.assertEqual(row[field], 1)
        self.assertFalse(row["checkpoint_complete"])
        self.assertFalse(row["current_source_binding_verified"])
        self.assertFalse(row["frozen_source_manifest_present"])

    def test_public_output_contains_no_titles_keys_bucket_or_source_text(self):
        result = self.inspect()
        serialized = json.dumps(result)
        for private in ("private-title", "secret-title", "private-bucket", "Original private", self.key, "https://"):
            self.assertNotIn(private, serialized)
        self.assertEqual(result["provider_posts"], 0)
        self.assertEqual(result["object_writes"], 0)
        self.assertEqual(result["object_deletions"], 0)
        self.assertTrue(all(call[0] in {"get", "head", "list"} for call in self.client.calls))

    def test_existing_final_pdf_and_item_match_production_validator(self):
        self.add_pdf_pair()
        result = self.inspect()["dates"][2]["final_pdf"]
        self.assertTrue(result["pdf_bytes_verified"])
        self.assertTrue(result["pair_verified"])
        self.assertEqual(result["size_bytes"], 1509)

    def test_absent_pdf_does_not_claim_recovery(self):
        result = self.inspect()["dates"][0]["final_pdf"]
        self.assertFalse(result["pdf_present"])
        self.assertFalse(result["pdf_bytes_verified"])
        self.assertFalse(result["pair_verified"])

    def test_pdf_with_corrupted_bytes_is_not_verified(self):
        self.add_pdf_pair()
        self.client.objects["_market-views/pdfs/261003.pdf"]["Body"] = b"broken" + b"x" * 1503
        result = self.inspect()["dates"][2]["final_pdf"]
        self.assertFalse(result["pdf_bytes_verified"])
        self.assertFalse(result["pair_verified"])
        self.assertEqual(result["category"], "final_pdf_verification")

    def test_archive_checksum_tamper_fails_before_extract(self):
        self.client.objects[self.key]["Metadata"]["sha256"] = "c" * 64
        self.assertEqual(self.row()["category"], "archive_hash_mismatch")

    def test_missing_archive_sha_skips_download(self):
        self.client.objects[self.key]["Metadata"] = {}
        self.assertEqual(self.row()["category"], "archive_hash_missing")
        self.assertNotIn(("get", self.key), self.client.calls)

    def test_oversized_checkpoint_is_not_downloaded(self):
        self.client.objects[self.key]["ContentLength"] = inventory.MAX_BYTES + 1
        self.assertEqual(self.row()["category"], "object_size_limit")
        self.assertNotIn(("get", self.key), self.client.calls)

    def test_tar_traversal_is_rejected(self):
        self.add_archive({**self.files, "../outside.txt": b"do not extract"})
        self.assertEqual(self.row()["category"], "archive_path")

    def test_tar_symlink_is_rejected(self):
        output = io.BytesIO()
        with tarfile.open(fileobj=output, mode="w:gz") as archive:
            member = tarfile.TarInfo("link")
            member.type, member.linkname = tarfile.SYMTYPE, "/tmp/secret"
            archive.addfile(member)
        self.client.add(self.key, output.getvalue())
        self.assertEqual(self.row()["category"], "archive_member_limit")

    def test_duplicate_tar_member_is_rejected(self):
        output = io.BytesIO()
        with tarfile.open(fileobj=output, mode="w:gz") as archive:
            for _ in range(2):
                member = tarfile.TarInfo("same.txt")
                member.size = 1
                archive.addfile(member, io.BytesIO(b"a"))
        self.client.add(self.key, output.getvalue())
        self.assertEqual(self.row()["category"], "archive_duplicate_member")

    def test_final_pdf_read_remains_bounded_if_head_is_false(self):
        self.add_pdf_pair()
        with patch.object(inventory, "MAX_BYTES", 2000):
            self.client.objects["_market-views/pdfs/261003.pdf"]["Body"] = b"%PDF-1.7\n" + b"x" * 2000
            row = self.inspect()["dates"][2]["final_pdf"]
        self.assertFalse(row["pair_verified"])
        self.assertEqual(row["category"], "object_size_limit")

    def test_checkpoint_identity_mismatch_is_not_verified(self):
        self.add_archive({**self.files, "_generation_checkpoint.json": json_bytes({"version": 1, "identity": "d" * 64, "complete": True})})
        row = self.row()
        self.assertFalse(row["verified"])
        self.assertEqual(row["category"], "checkpoint_identity_mismatch")

    def test_manifest_presence_is_reported_without_reuse_authorization(self):
        self.add_archive({**self.files, "selected_to_process_manifest.json": json_bytes([{"content_sha256": "b" * 64}])})
        row = self.row()
        self.assertTrue(row["frozen_source_manifest_present"])
        self.assertFalse(row["current_source_binding_verified"])

    def test_only_exact_known_handoff_run_is_read(self):
        prefix = "_private-workflow-handoff/xhs/37159099752/261003/"
        self.add_archive(self.files, prefix + "shard_0.tar.gz")
        self.add_archive(self.files, "_private-workflow-handoff/xhs/999999/261003/shard_0.tar.gz")
        rows = self.inspect()["dates"][2]["archives"]
        self.assertEqual(len(rows), 2)
        self.assertEqual(sum(row["kind"] == "handoff" for row in rows), 1)
        self.assertFalse(any("999999" in key for _, key in self.client.calls))

    def test_irrelevant_objects_are_not_downloaded(self):
        key = "_workflow-cache/report-generation/v1/261003/unrelated.zip"
        self.client.add(key, b"never download")
        row = self.inspect()["dates"][2]
        self.assertEqual(row["ignored_object_count"], 1)
        self.assertNotIn(("get", key), self.client.calls)

    def test_listing_caps_at_100_and_reports_incomplete(self):
        prefix = "_workflow-cache/report-generation/v1/261001/"
        for index in range(101):
            self.client.add(prefix + f"irrelevant{index:03d}", b"ignored")
        row = self.inspect()["dates"][0]
        self.assertEqual(row["listed_object_count"], 100)
        self.assertFalse(row["listing_complete"])
        self.assertEqual(row["archives"], [])

    def test_failure_always_writes_sanitized_artifact(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "inventory.json"
            with patch.object(inventory, "build_client", side_effect=RuntimeError("https://private-account/private-key")):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(inventory.main(["--output", str(output)]), 1)
            result = json.loads(output.read_text())
            self.assertFalse(result["success"])
            self.assertEqual(result["category"], "storage_read_failed")
            self.assertNotIn("private-account", output.read_text())


if __name__ == "__main__":
    unittest.main()
