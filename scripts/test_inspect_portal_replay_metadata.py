"""Metadata-only audit boundaries against real persisted publication fixtures."""
from __future__ import annotations

import copy
import io
import json
from pathlib import Path
import unittest
from unittest import mock

import inspect_portal_handoff_replay as cli
import inspect_portal_replay_metadata as audit
from build_portal_extended_locales import build
from portal_english_handoff import save_handoff
from portal_extended_locales import make_corpus, stable_bytes, digest
import test_portal_english_publication as english_fixtures
from test_portal_extended_incremental import daily_doc, URL
from test_portal_extended_locales import FakeTranslator


class ReplayMetadataTests(unittest.TestCase):
    def setUp(self):
        self.fixture = english_fixtures.EnglishPublicationTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.english_batch, self.identity, _ = self.fixture.first_live()
        self.original, self.english = self.fixture.original, self.fixture.store
        self.counter = 0
        self.ext_batch = self.extended()
        path = self.fixture.root / audit.LEDGER
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(stable_bytes({"schema_version": 2, "status": "assembled", "batches": [self.ext_batch]}))
        self.identity = self.fixture.pin()

    def extended(self, *, url=URL, body=None):
        self.counter += 1
        doc = daily_doc(url, **({"body": body} if body else {}))
        source = make_corpus([doc])
        work = self.fixture.base / ("metadata-ext-" + str(self.counter))
        build(source, "fr", work, work.with_suffix(".json"), FakeTranslator(), allow_source_fallback=True)
        self.original.put_source(source)
        saved = self.original.upload_candidate(work, "fr", source["documents_sha256"])
        return {"generation": source["documents_sha256"], "candidates": {"fr": saved["candidate_id"]}}

    def receipt(self, batch, producer="123"):
        source = json.loads(self.original._get(self.original.source_key(batch["generation"]), maximum=10*1024*1024))
        value = {"schema_version": 1, "paid_provider_requests": 0, "batch": batch,
                 "source_day": audit.daily_corpus_day(source),
                 "producer": {"run_id": producer, "attempt": "1", "sha": "c"*40},
                 "private_note": "private@example.invalid secret source text",
                 "generated_at": "2000-01-01T00:00:00Z", "approved_at": "2001-01-01T00:00:00Z"}
        raw = stable_bytes(value); identity = digest(raw)
        self.original._put(self.original.key("publication-handoffs", identity, "receipt.json"), raw, metadata={})
        return identity

    def english_receipt(self, batch=None):
        batch = batch or self.english_batch
        base = self.english.key("candidates", batch["generation"], batch["candidate_id"])
        ready = json.loads(self.english._get(base + "/candidate-ready.json", maximum=2*1024*1024))
        manifest = json.loads(self.english._get(base + "/candidate-manifest.json", maximum=2*1024*1024))
        return save_handoff(self.english, batch, ready, manifest)

    def reader(self):
        client = audit.ReadOnlyClient(self.original.client)
        original = audit.MetadataStore(client, self.original.bucket, self.original.prefix)
        english = audit.MetadataStore(client, self.english.bucket, self.english.prefix)
        return audit.Reader(original, english, self.identity)

    def test_real_active_identity_and_english_mapping_export_only_whitelisted_fields(self):
        extended = self.receipt(self.ext_batch)
        english = self.english_receipt()
        before = copy.deepcopy(self.original.client.objects)
        result = audit.audit(self.reader(), [extended], [english])
        self.assertEqual(self.original.client.objects, before)
        self.assertEqual(result["active_extended_batches"], 1)
        self.assertEqual(result["active_english_batches"], 1)
        for group in (result["extended"][0], result["english"][0]):
            self.assertTrue(group["exact_batch_active"])
            self.assertIsNone(group["generated_at"])
            self.assertIsNone(group["approved_at"])
            self.assertEqual(set(group["receipts"][0]), {"handoff_sha256", "producer"})
            self.assertEqual(set(group["receipts"][0]["producer"]), {"run_id", "attempt", "sha"})
        page = result["extended"][0]["candidates"][0]["pages"][0]
        self.assertEqual(set(page), {"public_page", "generation", "candidate_id", "source_day",
                                   "source_content_sha256", "translation_sha256", "active_owner", "comparison"})
        self.assertEqual(page["comparison"], "same_version")
        self.assertEqual(result["english"][0]["candidate_id"], self.english_batch["candidate_id"])
        self.assertEqual(result["english"][0]["counts"]["same_version"], 1)
        text = json.dumps(result)
        for forbidden in ("private@example", "secret source text", "New market findings", "2000-01-01", "2001-01-01", "title", "preview", "blocks", "private-bucket"):
            self.assertNotIn(forbidden, text)

    def test_duplicate_candidate_receipts_group_once_without_reordering_active_owner(self):
        a, b = self.receipt(self.ext_batch), self.receipt(self.ext_batch, "456")
        reader = self.reader()
        with mock.patch.object(reader, "extended_candidate", wraps=reader.extended_candidate) as candidates:
            result = audit.audit(reader, [a, b], [])
        self.assertEqual(len(result["extended"]), 1)
        self.assertEqual(len(result["extended"][0]["receipts"]), 2)
        self.assertEqual(candidates.call_count, 2, "one target and its active comparison, regardless of receipt count")
        self.assertEqual(result["extended"][0]["candidates"][0]["counts"]["same_version"], 1)

    def test_new_source_overlap_is_not_called_newer_and_novel_page_is_distinguished(self):
        changed = self.extended(body="<h1>Changed source</h1><p>Different original findings.</p>")
        novel = self.extended(url=URL.replace("new.html", "second.html"))
        result = audit.audit(self.reader(), [self.receipt(changed), self.receipt(novel)], [])
        self.assertEqual(result["extended"][0]["candidates"][0]["counts"]["overlap_source_changed"], 1)
        self.assertEqual(result["extended"][1]["candidates"][0]["counts"]["novel"], 1)
        self.assertFalse(result["publication_authorized"])
        self.assertNotIn("newer", json.dumps(result))

    def test_same_source_different_translation_remains_unordered(self):
        page = audit.page_projection("a"*64, "b"*64, "2026-09-25", "c"*64, "d"*64)
        old = {**page, "candidate_id": "e"*64, "translation_sha256": "f"*64}
        rows, counts = audit.compare_pages({URL: page}, {URL: old})
        self.assertEqual(counts["overlap_translation_changed"], 1)
        self.assertEqual(rows[0]["active_owner"], old)

    def test_active_owner_is_latest_batch_even_when_target_is_already_in_history(self):
        later = self.extended(body="<h1>Updated source</h1><p>Revised original findings.</p>")
        path = self.fixture.root / audit.LEDGER
        path.write_bytes(stable_bytes({"schema_version": 2, "status": "assembled", "batches": [self.ext_batch, later]}))
        self.identity = self.fixture.pin()
        result = audit.audit(self.reader(), [self.receipt(self.ext_batch)], [])
        group = result["extended"][0]
        self.assertTrue(group["exact_batch_active"], "historical batch stays in its existing position")
        page = group["candidates"][0]["pages"][0]
        self.assertEqual(page["active_owner"]["generation"], later["generation"])
        self.assertEqual(page["comparison"], "overlap_source_changed")

    def test_english_unpublished_day_is_novel_and_maps_receipt_to_exact_batch(self):
        batch = self.fixture.candidate(day="2026-09-26")
        result = audit.audit(self.reader(), [], [self.english_receipt(batch)])
        row = result["english"][0]
        self.assertEqual((row["generation"], row["candidate_id"]), (batch["generation"], batch["candidate_id"]))
        self.assertEqual(row["source_day"], "2026-09-26")
        self.assertFalse(row["exact_batch_active"])
        self.assertEqual(row["counts"]["novel"], 1)
        self.assertIsNone(row["pages"][0]["active_owner"])

    def test_english_receipt_cannot_claim_a_different_producer_or_page_count(self):
        identity = self.english_receipt()
        key = self.english.key("publication-handoffs", identity, "receipt.json")
        value = json.loads(self.english._get(key, maximum=65536))
        for field, changed in (("producer", {**value["producer"], "run_id": "987"}), ("page_count", 2)):
            tampered = {**value, field: changed}; raw = stable_bytes(tampered); checksum = digest(raw)
            self.english._put(self.english.key("publication-handoffs", checksum, "receipt.json"), raw, metadata={})
            with self.subTest(field=field), self.assertRaises(ValueError):
                audit.audit(self.reader(), [], [checksum])

    def test_corrupt_candidate_manifest_and_active_binding_fail_closed(self):
        ext = self.receipt(self.ext_batch)
        key = self.original.candidate_manifest_key("fr", self.ext_batch["generation"], self.ext_batch["candidates"]["fr"])
        saved = copy.deepcopy(self.original.client.objects[key])
        self.original.client.objects[key]["body"] += b" "
        self.original.client.objects[key]["ContentLength"] += 1
        self.original.client.objects[key]["Metadata"]["sha256"] = digest(self.original.client.objects[key]["body"])
        with self.assertRaises(ValueError): audit.audit(self.reader(), [ext], [])
        self.original.client.objects[key] = saved
        key = self.english.key("releases", self.identity["release_id"], "manifest.json")
        self.english._put(key, stable_bytes({"status": "approved", "ledger_sha256": "f"*64}), metadata={})
        with self.assertRaises(ValueError): audit.audit(self.reader(), [ext], [])

    def test_english_ready_inventory_rejects_missing_extra_and_mismatched_descriptors(self):
        receipt = self.english_receipt()
        batch = self.english_batch
        key = self.english.key("candidates", batch["generation"], batch["candidate_id"]) + "/candidate-ready.json"
        original = json.loads(self.english._get(key, maximum=2*1024*1024))
        body = next(path for path in original["files"] if path.startswith("private/"))
        for mode in ("manifest-only", "extra", "body-hash", "invalid-size", "public-hash"):
            value = copy.deepcopy(original)
            if mode == "manifest-only": value["files"] = {"candidate-manifest.json": value["files"]["candidate-manifest.json"]}
            elif mode == "extra": value["files"]["private/unexpected.json"] = {"sha256": "f"*64, "bytes": 1}
            elif mode == "body-hash": value["files"][body]["sha256"] = "f"*64
            elif mode == "invalid-size": value["files"][body]["bytes"] = True
            else: value["files"]["public/en/index.html"]["sha256"] = "f"*64
            value["files_sha256"] = digest(stable_bytes(value["files"]))
            self.english._put(key, stable_bytes(value), metadata={})
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                audit.audit(self.reader(), [], [receipt])

    def test_storage_adapter_rejects_writes_listing_and_has_a_read_bound(self):
        client = mock.Mock()
        readonly = audit.ReadOnlyClient(client)
        for operation in ("put_object", "delete_object", "list_objects_v2", "copy_object", "create_multipart_upload"):
            with self.subTest(operation=operation), self.assertRaises(ValueError): getattr(readonly, operation)
        client.assert_not_called()
        with mock.patch.object(audit, "MAX_READS", 1):
            readonly.head_object(Bucket="test", Key="known")
            with self.assertRaises(ValueError): readonly.get_object(Bucket="test", Key="known")
        self.assertEqual(client.mock_calls, [mock.call.head_object(Bucket="test", Key="known")])

    def test_cli_validates_mode_before_credentials_and_redacts_metadata_failures(self):
        output = self.fixture.base / "metadata-output.json"
        with mock.patch.object(cli.R2Store, "from_env") as factory:
            for args in (["--metadata", "--receipt-hashes", "a"*64],
                         ["--english-receipt-hashes", "a"*64],
                         ["--metadata", "--active-release", "a"*32]):
                with mock.patch("sys.stdout", new_callable=io.StringIO):
                    self.assertEqual(cli.main([*args, "--output", str(output)]), 1)
            factory.assert_not_called()
        with mock.patch.object(cli.R2Store, "from_env", return_value=self.original), mock.patch.object(
                audit, "inspect_metadata", side_effect=ValueError("private credential endpoint")):
            with mock.patch("sys.stdout", new_callable=io.StringIO) as stdout:
                status = cli.main(["--metadata", "--english-receipt-hashes", "a"*64,
                                   "--active-release", "a"*32, "--output", str(output)])
        self.assertEqual(status, 1)
        self.assertNotIn("private", stdout.getvalue())
        self.assertFalse(output.exists())

    def test_active_release_must_match_before_storage_and_after_audit(self):
        ext = self.receipt(self.ext_batch)
        with mock.patch.object(audit, "read_identity", return_value=self.identity), mock.patch.object(audit, "Reader") as reader:
            with self.assertRaises(ValueError): audit.inspect_metadata(self.original, [ext], [], "f"*32)
            reader.assert_not_called()
        with mock.patch.object(audit, "DEFAULT_PREFIX", self.original.prefix), mock.patch.object(audit, "PREFIX", self.english.prefix), mock.patch.object(
                audit, "read_identity", side_effect=[self.identity, {**self.identity, "release_id": "f"*32}]):
            with self.assertRaises(ValueError): audit.inspect_metadata(self.original, [ext], [], self.identity["release_id"])


if __name__ == "__main__": unittest.main()
