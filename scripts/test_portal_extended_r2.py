#!/usr/bin/env python3
"""Local contract tests for the private extended-locale R2 persistence layer."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

from portal_extended_r2 import (
    R2IntegrityError,
    R2NotFound,
    R2PermissionError,
    R2Store,
    R2StoreError,
    classify,
    fake_permission_check,
    require_staging_prefix,
)
from test_portal_extended_locales import FakeTranslator, corpus
from build_portal_extended_locales import MODEL_ID, build


class Missing(Exception):
    response = {"Error": {"Code": "NoSuchKey"}, "ResponseMetadata": {"HTTPStatusCode": 404}}


class Denied(Exception):
    response = {"Error": {"Code": "AccessDenied"}, "ResponseMetadata": {"HTTPStatusCode": 403}}


class FakeBody:
    def __init__(self, body: bytes):
        self.body = body

    def read(self, maximum: int = -1) -> bytes:
        return self.body[:maximum] if maximum >= 0 else self.body


class FakeR2:
    def __init__(self):
        self.objects: dict[str, dict] = {}
        self.deny = False

    def put_object(self, *, Bucket, Key, Body, ContentType, CacheControl, Metadata):
        if self.deny:
            raise Denied()
        self.objects[Key] = {"body": bytes(Body), "ContentLength": len(Body), "Metadata": dict(Metadata),
                             "ContentType": ContentType, "CacheControl": CacheControl}

    def head_object(self, *, Bucket, Key):
        if self.deny:
            raise Denied()
        if Key not in self.objects:
            raise Missing()
        value = self.objects[Key]
        return {"ContentLength": value["ContentLength"], "Metadata": value["Metadata"]}

    def get_object(self, *, Bucket, Key):
        if self.deny:
            raise Denied()
        if Key not in self.objects:
            raise Missing()
        return {"Body": FakeBody(self.objects[Key]["body"])}


class R2Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.client = FakeR2()
        self.store = R2Store(self.client, "private-bucket", "_extended-locales/staging/test")
        self.corpus = corpus()
        self.generation = self.corpus["documents_sha256"]

    def tearDown(self):
        self.tmp.cleanup()

    def test_staging_prefix_is_required_for_roundtrip(self):
        self.assertEqual(require_staging_prefix("_extended-locales/staging/run"), "_extended-locales/staging/run")
        for value in ["_extended-locales/v1", "public", "../staging/x"]:
            with self.subTest(value=value), self.assertRaises(R2StoreError):
                require_staging_prefix(value)

    def test_source_put_is_idempotent_and_rejects_changed_generation(self):
        first = self.store.put_source(self.corpus)
        second = self.store.put_source(copy.deepcopy(self.corpus))
        self.assertFalse(first["reused"])
        self.assertTrue(second["reused"])
        changed = copy.deepcopy(self.corpus)
        changed["documents"][0]["title"] = "tampered"
        with self.assertRaises(R2StoreError):
            self.store.put_source(changed)

    def test_checkpoint_round_trip_is_checksum_and_generation_bound(self):
        checkpoint = self.root / "checkpoint.json"
        checkpoint.write_text(json.dumps({
            "model": MODEL_ID,
            "locale": "fr",
            "version": "extended-static-v2",
            "source_generation": self.generation,
            "rows": {"row": {"source": "x", "language": "fr", "text": "x"}},
        }), encoding="utf-8")
        saved = self.store.put_checkpoint("fr", self.generation, checkpoint)
        restored = self.root / "restored.json"
        result = self.store.restore_checkpoint("fr", self.generation, restored)
        self.assertTrue(result["present"])
        self.assertEqual(saved["sha256"], result["sha256"])
        self.assertEqual(checkpoint.read_bytes(), restored.read_bytes())
        missing = self.store.restore_checkpoint("pt", self.generation, self.root / "missing.json")
        self.assertFalse(missing["present"])

    def test_incomplete_candidate_has_no_ready_receipt_and_cannot_restore(self):
        candidate = self.root / "candidate"
        result = build(self.corpus, "fr", candidate, self.root / "memo.json", FakeTranslator(fail="Source based"))
        self.assertEqual(result["status"], "incomplete-candidate")
        uploaded = self.store.upload_candidate(candidate, "fr", self.generation)
        self.assertFalse(uploaded["ready"])
        with self.assertRaises(R2NotFound):
            self.store.restore_candidate("fr", self.generation, uploaded["candidate_id"], self.root / "restored")

    def test_complete_candidate_restore_matches_pages(self):
        candidate = self.root / "candidate"
        build(self.corpus, "fr", candidate, self.root / "memo.json", FakeTranslator())
        uploaded = self.store.upload_candidate(candidate, "fr", self.generation)
        self.assertTrue(uploaded["ready"])
        restored = self.root / "restored"
        result = self.store.restore_candidate("fr", self.generation, uploaded["candidate_id"], restored)
        self.assertEqual(result["completed_page_count"], 2)
        self.assertEqual((candidate / "fr/index.html").read_bytes(), (restored / "fr/index.html").read_bytes())

    def test_permission_and_integrity_fail_closed(self):
        self.assertEqual(fake_permission_check()["permission_failure"], "R2PermissionError")
        self.assertIsInstance(classify(Denied(), "read"), R2PermissionError)
        self.assertIsInstance(classify(Missing(), "read"), R2NotFound)
        self.client.put_source = None
        with self.assertRaises(R2IntegrityError):
            self.store._verify_head({"ContentLength": 1, "Metadata": {"sha256": "0" * 64}}, "x", 2, "1" * 64)


if __name__ == "__main__":
    unittest.main(verbosity=2)
