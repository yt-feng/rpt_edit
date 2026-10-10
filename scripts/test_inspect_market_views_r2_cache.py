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
from private_market_ocr_checkpoint import checkpoint_key
from recover_durable_mineru_sources import PRODUCER, RecoveryError


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


class OCRPresenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name); self.client = FakeR2()
        self.manifest = self.root/'selected_to_process_manifest.json'
        self.rows = [{"process_local_path": f"/runner/private-title-{index}.pdf",
                      "content_sha256": str(index+1)*64,
                      "dropbox_path": f"/zip_backup/261007/private-title-{index}.pdf"} for index in range(2)]
        self.manifest.write_bytes(json_bytes(self.rows))
        self.repository = 'owner/reports'
        self.producer = {"id": 37695511597, "path": PRODUCER, "head_branch": "main", "head_sha": "a"*40,
                         "status": "completed", "event": "schedule", "repository": {"full_name": self.repository},
                         "head_repository": {"full_name": self.repository}}
        self.request = inventory.validate_ocr_request('37695511597', '261007', '2',
                                                      hashlib.sha256(self.manifest.read_bytes()).hexdigest())
        self.key = checkpoint_key(self.manifest, '261007', 2)
        self.handoff_key = '_private-workflow-handoff/market-ocr-synthesis/37695511597/261007/shard_0.tar.gz'
        self.expected_heads = [('head', self.key), ('head', self.handoff_key)]

    def inspect(self, request=None, producer=None):
        return inventory.inspect_ocr_presence(self.client, 'private-bucket', self.manifest,
            self.producer if producer is None else producer, self.request if request is None else request,
            self.repository)

    def test_present_reads_only_exact_cache_and_handoff_heads_without_download(self):
        self.client.add(self.key, b'opaque archive is deliberately never parsed')
        result = self.inspect(); row = result['ocr_checkpoint']
        self.assertTrue(result['success']); self.assertTrue(row['present'])
        self.assertTrue(row['source_binding_verified']); self.assertFalse(row['archive_bytes_verified'])
        self.assertEqual(row['object_count'], 1); self.assertGreater(row['size_bytes'], 0)
        self.assertEqual(self.client.calls, self.expected_heads)
        self.assertFalse(result['ocr_source_handoff']['present'])
        public = json.dumps(result)
        for forbidden in ('private-title', 'zip_backup', 'private-bucket', self.key, '/runner/'):
            self.assertNotIn(forbidden, public)
        for field in ('provider_posts', 'object_writes', 'object_deletions'):
            self.assertEqual(result[field], 0)

    def test_absence_is_known_only_after_exact_head_and_does_not_trigger_generation(self):
        result = self.inspect(); row = result['ocr_checkpoint']
        self.assertTrue(result['success']); self.assertFalse(row['present'])
        self.assertEqual(row['object_count'], 0); self.assertEqual(row['size_bytes'], 0)
        self.assertIsNone(row['archive_sha256']); self.assertEqual(self.client.calls, self.expected_heads)
        self.assertFalse(result['ocr_source_handoff']['present'])

    def test_reordered_manifest_uses_same_checkpoint_but_requires_its_exact_raw_hash(self):
        self.manifest.write_bytes(json_bytes(list(reversed(self.rows))))
        with self.assertRaises(inventory.InvalidObject): self.inspect()
        self.assertEqual(self.client.calls, [])
        request = {**self.request, 'manifest_sha256': hashlib.sha256(self.manifest.read_bytes()).hexdigest()}
        self.inspect(request=request)
        self.assertEqual(self.client.calls, self.expected_heads)

    def test_source_handoff_presence_is_independent_and_does_not_inspect_other_runs_or_dates(self):
        payload = b'opaque complete source handoff'
        self.client.add(self.handoff_key, payload)
        self.client.add(self.handoff_key.replace('37695511597', '999999'), b'other run')
        self.client.add(self.handoff_key.replace('261007', '261008'), b'other date')
        result = self.inspect(); handoff = result['ocr_source_handoff']
        self.assertFalse(result['ocr_checkpoint']['present']); self.assertTrue(handoff['present'])
        self.assertEqual(handoff['object_count'], 1); self.assertEqual(handoff['size_bytes'], len(payload))
        self.assertEqual(handoff['archive_sha256'], hashlib.sha256(payload).hexdigest())
        self.assertFalse(handoff['archive_bytes_verified']); self.assertEqual(self.client.calls, self.expected_heads)
        self.assertNotIn(self.handoff_key, json.dumps(result))

    def test_both_objects_can_be_present_without_claiming_archive_verification(self):
        self.client.add(self.key, b'cache'); self.client.add(self.handoff_key, b'source handoff')
        result = self.inspect()
        for name in ('ocr_checkpoint', 'ocr_source_handoff'):
            self.assertTrue(result[name]['present']); self.assertFalse(result[name]['archive_bytes_verified'])
        self.assertEqual(self.client.calls, self.expected_heads)

    def test_source_handoff_permission_or_transport_failure_cannot_be_absence(self):
        producer = self.root/'producer.json'; producer.write_bytes(json_bytes(self.producer))
        output = self.root/'receipt.json'; self.client.add(self.key, b'cache')
        head = self.client.head_object
        class Denied(Exception):
            response = {'Error': {'Code': '403'}, 'ResponseMetadata': {'HTTPStatusCode': 403}}
        for error in (Denied('private-handoff'), TimeoutError('https://private-endpoint')):
            with self.subTest(error=type(error).__name__):
                self.client.calls.clear()
                def read(**kwargs):
                    if kwargs['Key'] == self.handoff_key:
                        self.client.calls.append(('head', kwargs['Key'])); raise error
                    return head(**kwargs)
                args = ['--output', str(output), '--source-run-id', self.request['source_run_id'],
                        '--date-folder', '261007', '--expected-reports', '2',
                        '--manifest-sha256', self.request['manifest_sha256'], '--manifest', str(self.manifest),
                        '--producer-json', str(producer)]
                with patch.object(self.client, 'head_object', side_effect=read), \
                     patch.object(inventory, 'build_client', return_value=self.client), \
                     patch.dict('os.environ', {'R2_BUCKET': 'private-bucket', 'GITHUB_REPOSITORY': self.repository}), \
                     redirect_stdout(io.StringIO()):
                    self.assertEqual(inventory.main(args), 1)
                result = json.loads(output.read_bytes())
                self.assertFalse(result['success']); self.assertNotIn('ocr_source_handoff', result)
                self.assertEqual(result['category'], 'storage_read_failed')
                self.assertEqual(self.client.calls, self.expected_heads)
                self.assertNotIn('private-', output.read_text())

    def test_wrong_count_date_and_duplicate_sources_fail_before_storage(self):
        for request in ({**self.request, 'expected_reports': 3}, {**self.request, 'date_folder': '261008'}):
            with self.subTest(request=request):
                with self.assertRaises(inventory.InvalidObject): self.inspect(request=request)
        self.manifest.write_bytes(json_bytes([self.rows[0], self.rows[0]]))
        request = {**self.request, 'manifest_sha256': hashlib.sha256(self.manifest.read_bytes()).hexdigest()}
        with self.assertRaises(inventory.InvalidObject): self.inspect(request=request)
        self.assertEqual(self.client.calls, [])

    def test_unrelated_or_unfinished_run_cannot_inspect_cache(self):
        for field, value in [('id', 123), ('path', '.github/workflows/other.yml'), ('head_branch', 'feature'),
                             ('status', 'in_progress'), ('event', 'pull_request'), ('head_sha', 'x'*40),
                             ('repository', {'full_name': 'other/reports'}),
                             ('head_repository', {'full_name': 'other/reports'})]:
            with self.subTest(field=field):
                with self.assertRaises((RecoveryError, inventory.InvalidObject)):
                    self.inspect(producer={**self.producer, field: value})
        self.assertEqual(self.client.calls, [])

    def test_missing_symlink_and_oversized_manifest_cannot_read_storage(self):
        self.manifest.unlink()
        with self.assertRaises(inventory.InvalidObject): self.inspect()
        target = self.root/'real.json'; target.write_bytes(json_bytes(self.rows)); self.manifest.symlink_to(target)
        with self.assertRaises(inventory.InvalidObject): self.inspect()
        self.manifest.unlink(); self.manifest.write_bytes(b'x'*(16*1024*1024+1))
        with self.assertRaises(inventory.InvalidObject): self.inspect()
        self.assertEqual(self.client.calls, [])

    def test_archive_metadata_is_reported_only_with_valid_size_and_hash(self):
        for size, checksum in [(0, 'a'*64), (inventory.MAX_BYTES+1, 'a'*64), (1, ''), (1, 'private-text')]:
            with self.subTest(size=size, checksum=checksum):
                self.client.add(self.key, b'x', metadata={'sha256': checksum})
                self.client.objects[self.key]['ContentLength'] = size
                with self.assertRaises(inventory.InvalidObject): self.inspect()
        self.assertTrue(all(operation == 'head' for operation, key in self.client.calls))

    def test_head_permission_or_transport_failure_is_not_absence_and_is_sanitized(self):
        producer_path = self.root/'producer.json'; producer_path.write_bytes(json_bytes(self.producer))
        class Denied(Exception):
            response = {'Error': {'Code': '403'}, 'ResponseMetadata': {'HTTPStatusCode': 403}}
        for error in (Denied('private-object'), TimeoutError('https://private-endpoint')):
            with self.subTest(error=type(error).__name__):
                output = self.root/'receipt.json'
                args = ['--output', str(output), '--source-run-id', self.request['source_run_id'],
                        '--date-folder', '261007', '--expected-reports', '2',
                        '--manifest-sha256', self.request['manifest_sha256'], '--manifest', str(self.manifest),
                        '--producer-json', str(producer_path)]
                with patch.object(inventory, 'build_client', return_value=self.client), \
                     patch.object(self.client, 'head_object', side_effect=error) as head, \
                     patch.dict('os.environ', {'R2_BUCKET': 'private-bucket', 'GITHUB_REPOSITORY': self.repository}), \
                     redirect_stdout(io.StringIO()):
                    self.assertEqual(inventory.main(args), 1)
                result = json.loads(output.read_bytes())
                self.assertFalse(result['success']); self.assertNotIn('ocr_checkpoint', result)
                self.assertEqual(result['category'], 'storage_read_failed'); head.assert_called_once()
                self.assertNotIn('private-', output.read_text())

    def test_inputs_are_all_or_none_and_default_dates_are_unchanged(self):
        self.assertIsNone(inventory.validate_ocr_request())
        self.assertEqual(inventory.DATES, ('261001', '261002', '261003'))
        for args in [('37695511597', '', '', ''), ('1/2', '261007', '2', 'a'*64),
                     ('1', '261032', '2', 'a'*64), ('1', '261007', '1001', 'a'*64),
                     ('1', '261007', '02', 'a'*64), ('1', '261007', '2', 'A'*64)]:
            with self.subTest(args=args):
                with self.assertRaises((RecoveryError, inventory.InvalidObject)):
                    inventory.validate_ocr_request(*args)

    def test_cli_presence_never_falls_through_to_incident_downloads(self):
        producer = self.root/'producer.json'; producer.write_bytes(json_bytes(self.producer))
        output = self.root/'receipt.json'
        args = ['--output', str(output), '--source-run-id', self.request['source_run_id'],
                '--date-folder', '261007', '--expected-reports', '2',
                '--manifest-sha256', self.request['manifest_sha256'], '--manifest', str(self.manifest),
                '--producer-json', str(producer)]
        with patch.object(inventory, 'build_client', return_value=self.client), \
             patch.object(inventory, 'inspect_cache', side_effect=AssertionError('wrong mode')), \
             patch.dict('os.environ', {'R2_BUCKET': 'private-bucket', 'GITHUB_REPOSITORY': self.repository}), \
             redirect_stdout(io.StringIO()):
            self.assertEqual(inventory.main(args), 0)
        self.assertEqual(json.loads(output.read_bytes())['mode'], 'ocr-presence')
        self.assertEqual(self.client.calls, self.expected_heads)


if __name__ == "__main__":
    unittest.main()
