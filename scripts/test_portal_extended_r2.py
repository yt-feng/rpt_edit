#!/usr/bin/env python3
"""Local contract tests for the private extended-locale R2 persistence layer."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, call, patch

from portal_extended_r2 import (
    R2IntegrityError,
    R2NotFound,
    R2PermissionError,
    R2Store,
    R2StoreError,
    R2TransportError,
    READ_RETRY_DELAYS,
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


class HttpError(Exception):
    def __init__(self, code: str, status: int, retries: int | None = 0):
        self.response = {"Error": {"Code": code}, "ResponseMetadata": {"HTTPStatusCode": status}}
        if retries is not None:
            self.response["ResponseMetadata"]["RetryAttempts"] = retries


class FakeBody:
    def __init__(self, body: bytes):
        self.body = body
        self.closed = False

    def read(self, maximum: int = -1) -> bytes:
        return self.body[:maximum] if maximum >= 0 else self.body

    def close(self) -> None:
        self.closed = True


class FakeR2:
    def __init__(self):
        self.objects: dict[str, dict] = {}
        self.deny = False
        self.bodies: list[FakeBody] = []

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
        return {name: copy.deepcopy(value[name]) for name in
                ("ContentLength", "Metadata", "ContentType", "CacheControl")}

    def get_object(self, *, Bucket, Key):
        if self.deny:
            raise Denied()
        if Key not in self.objects:
            raise Missing()
        body = FakeBody(self.objects[Key]["body"])
        self.bodies.append(body)
        return {"Body": body, "ResponseMetadata": {"RetryAttempts": 0}}


class R2Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.client = FakeR2()
        self.store = R2Store(self.client, "private-bucket", "_extended-locales/staging/test")
        self.corpus = corpus()
        self.generation = self.corpus["documents_sha256"]
        sleep_patch = patch("portal_extended_r2.time.sleep")
        self.sleep = sleep_patch.start()
        self.addCleanup(sleep_patch.stop)
        jitter_patch = patch("portal_extended_r2.random.uniform", return_value=0.25)
        jitter_patch.start()
        self.addCleanup(jitter_patch.stop)

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

    def test_identical_candidate_replay_avoids_all_duplicate_puts(self):
        candidate = self.root / "candidate"
        build(self.corpus, "fr", candidate, self.root / "memo.json", FakeTranslator())
        first = self.store.upload_candidate(candidate, "fr", self.generation)
        self.client.put_object = Mock(wraps=self.client.put_object)
        second = self.store.upload_candidate(candidate, "fr", self.generation)
        self.assertEqual(first, second)
        self.client.put_object.assert_not_called()
        self.store.restore_candidate("fr", self.generation, second["candidate_id"], self.root / "restored")

    def test_interrupted_candidate_upload_resumes_without_rewriting_verified_pages(self):
        candidate = self.root / "candidate"
        manifest = build(self.corpus, "fr", candidate, self.root / "memo.json", FakeTranslator())
        candidate_id = manifest["files_sha256"]
        first_key = self.store.candidate_key("fr", self.generation, candidate_id, manifest["pages"][0]["path"])
        failed_key = self.store.candidate_key("fr", self.generation, candidate_id, manifest["pages"][1]["path"])
        ready_key = self.store.candidate_ready_key("fr", self.generation, candidate_id)
        write = self.client.put_object

        def interrupt_second_page(**kwargs):
            if kwargs["Key"] == failed_key:
                raise HttpError("ServiceUnavailable", 429, retries=8)
            return write(**kwargs)

        self.client.put_object = Mock(side_effect=interrupt_second_page)
        with self.assertRaises(R2TransportError):
            self.store.upload_candidate(candidate, "fr", self.generation)
        self.assertIn(first_key, self.client.objects)
        self.assertNotIn(ready_key, self.client.objects)
        self.client.put_object = Mock(wraps=write)
        result = self.store.upload_candidate(candidate, "fr", self.generation)
        self.assertTrue(result["ready"])
        self.assertEqual([entry.kwargs["Key"] for entry in self.client.put_object.call_args_list],
                         [failed_key, result["manifest_key"], ready_key])

    def test_changed_candidate_diagnostics_update_manifest_and_receipt_only(self):
        candidate = self.root / "candidate"
        build(self.corpus, "fr", candidate, self.root / "memo.json", FakeTranslator())
        first = self.store.upload_candidate(candidate, "fr", self.generation)
        path = candidate / "candidate-manifest.json"
        manifest = json.loads(path.read_bytes())
        manifest["translation_calls_this_run"] = 0
        manifest["cache_hits"] = 123
        path.write_text(json.dumps(manifest), encoding="utf-8")
        self.client.put_object = Mock(wraps=self.client.put_object)
        second = self.store.upload_candidate(candidate, "fr", self.generation)
        self.assertEqual(first["candidate_id"], second["candidate_id"])
        self.assertNotEqual(first["manifest_sha256"], second["manifest_sha256"])
        self.assertEqual([entry.kwargs["Key"] for entry in self.client.put_object.call_args_list],
                         [second["manifest_key"], second["ready_key"]])
        self.store.restore_candidate("fr", self.generation, second["candidate_id"], self.root / "restored")

    def test_checkpoint_replay_reuses_object_and_pointer_but_updates_new_content(self):
        checkpoint = self.root / "checkpoint.json"
        value = {"model": MODEL_ID, "locale": "fr", "version": "extended-static-v2",
                 "source_generation": self.generation, "rows": {}}
        checkpoint.write_text(json.dumps(value), encoding="utf-8")
        first = self.store.put_checkpoint("fr", self.generation, checkpoint)
        self.client.put_object = Mock(wraps=self.client.put_object)
        self.assertEqual(first, self.store.put_checkpoint("fr", self.generation, checkpoint))
        self.client.put_object.assert_not_called()
        value["rows"]["new"] = {"source": "source", "language": "fr", "text": "texte"}
        checkpoint.write_text(json.dumps(value), encoding="utf-8")
        second = self.store.put_checkpoint("fr", self.generation, checkpoint)
        self.assertNotEqual(first["object_key"], second["object_key"])
        self.assertEqual([entry.kwargs["Key"] for entry in self.client.put_object.call_args_list],
                         [second["object_key"], second["pointer_key"]])

    def test_reuse_requires_matching_bytes_metadata_and_delivery_attributes(self):
        changes = {
            "length": lambda value: value.update(ContentLength=1),
            "checksum": lambda value: value["Metadata"].update(sha256="0" * 64),
            "identity": lambda value: value["Metadata"].update(kind="other"),
            "content_type": lambda value: value.update(ContentType="text/plain"),
            "cache_control": lambda value: value.update(CacheControl="public"),
        }
        for label, change in changes.items():
            with self.subTest(change=label):
                self.client = FakeR2()
                self.store.client = self.client
                self.store._put("object", b"abc", metadata={"kind": "test"})
                change(self.client.objects["object"])
                self.client.put_object = Mock(wraps=self.client.put_object)
                self.store._put("object", b"abc", metadata={"kind": "test"}, reuse_identical=True)
                self.client.put_object.assert_called_once()

    def test_preflight_failure_never_writes(self):
        for error, expected in ((Denied(), R2PermissionError), (HttpError("429", 429), R2TransportError)):
            with self.subTest(error=error):
                self.client.head_object = Mock(side_effect=error)
                self.client.put_object = Mock()
                with self.assertRaises(expected):
                    self.store._put("object", b"abc", metadata={}, reuse_identical=True)
                self.client.put_object.assert_not_called()

    def test_permission_and_integrity_fail_closed(self):
        self.assertEqual(fake_permission_check()["permission_failure"], "R2PermissionError")
        self.assertIsInstance(classify(Denied(), "read"), R2PermissionError)
        self.assertIsInstance(classify(Missing(), "read"), R2NotFound)
        self.client.put_source = None
        with self.assertRaises(R2IntegrityError):
            self.store._verify_head({"ContentLength": 1, "Metadata": {"sha256": "0" * 64}}, "x", 2, "1" * 64)

    def seed_read(self) -> tuple[str, bytes, dict]:
        self.client = FakeR2()
        self.store.client = self.client
        key, body = "read-test", b"complete source or candidate page"
        self.store._put(key, body, metadata={})
        return key, body, self.client.head_object(Bucket="private-bucket", Key=key)

    def test_head_failure_does_not_start_another_sdk_retry_chain(self):
        key, _body, _head = self.seed_read()
        self.client.head_object = Mock(side_effect=HttpError("429", 429))
        self.client.get_object = Mock(wraps=self.client.get_object)
        with self.assertRaises(R2TransportError):
            self.store._get(key, maximum=1024)
        self.assertEqual(self.client.head_object.call_count, 1)
        self.client.get_object.assert_not_called()
        self.sleep.assert_not_called()

    def test_throttling_exhaustion_is_not_missing_checkpoint(self):
        self.client.head_object = Mock(side_effect=HttpError("429", 429))
        self.client.get_object = Mock(wraps=self.client.get_object)
        destination = self.root / "checkpoint.json"
        with self.assertRaises(R2TransportError):
            self.store.restore_checkpoint("fr", self.generation, destination)
        self.assertEqual(self.client.head_object.call_count, 1)
        self.sleep.assert_not_called()
        self.client.get_object.assert_not_called()
        self.assertFalse(destination.exists())

    def test_get_request_failure_does_not_start_another_sdk_retry_chain(self):
        for error in (HttpError("429", 429), HttpError("ServiceUnavailable", 503)):
            with self.subTest(error=error.response):
                key, _body, head = self.seed_read()
                self.client.head_object = Mock(return_value=head)
                self.client.get_object = Mock(side_effect=error)
                with self.assertRaises(R2TransportError):
                    self.store._get(key, maximum=1024)
                self.assertEqual(self.client.head_object.call_count, 1)
                self.assertEqual(self.client.get_object.call_count, 1)
        self.sleep.assert_not_called()

    def test_request_failures_without_retry_authority_fail_once(self):
        errors = [
            (HttpError("AccessDenied", 403), R2PermissionError),
            (HttpError("", 404), R2NotFound),
            (HttpError("NoSuchKey", 404), R2NotFound),
            (HttpError("UnknownError", 400), R2TransportError),
            (HttpError("InternalError", 500, retries=None), R2TransportError),
            (HttpError("429", 429, retries=8), R2TransportError),
            (TimeoutError("SDK retry metadata absent"), R2TransportError),
            (OSError("unclassified transport error"), R2TransportError),
        ]
        for error, expected in errors:
            with self.subTest(error=error), self.assertRaises(expected):
                self.client.head_object = Mock(side_effect=error)
                self.store._get("object", maximum=1024)
            self.assertEqual(self.client.head_object.call_count, 1)
        self.sleep.assert_not_called()

    def test_post_put_head_failure_does_not_replay_put(self):
        key, body, _head = self.seed_read()
        self.client.put_object = Mock(wraps=self.client.put_object)
        self.client.head_object = Mock(side_effect=HttpError("429", 429))
        with self.assertRaises(R2TransportError):
            self.store._put(key, body, metadata={})
        self.assertEqual(self.client.put_object.call_count, 1)
        self.assertEqual(self.client.head_object.call_count, 1)
        self.sleep.assert_not_called()

    def test_put_failure_is_not_replayed_by_read_retry(self):
        self.client.put_object = Mock(side_effect=HttpError("429", 429))
        self.client.head_object = Mock(wraps=self.client.head_object)
        with self.assertRaises(R2TransportError):
            self.store._put("object", b"body", metadata={})
        self.assertEqual(self.client.put_object.call_count, 1)
        self.client.head_object.assert_called_once()
        self.sleep.assert_not_called()

    def test_transient_put_response_is_reconciled_without_replaying_the_write(self):
        for error in (HttpError("ServiceUnavailable", 503, retries=8),
                      HttpError("ServiceUnavailable", 429), TimeoutError("response lost")):
            with self.subTest(error=error):
                self.client = FakeR2()
                self.store.client = self.client
                write = self.client.put_object

                def committed_without_response(**kwargs):
                    write(**kwargs)
                    raise error

                self.client.put_object = Mock(side_effect=committed_without_response)
                self.client.head_object = Mock(wraps=self.client.head_object)
                result = self.store._put("object", b"abc", metadata={"kind": "test"})
                self.assertEqual(result["bytes"], 3)
                self.client.put_object.assert_called_once()
                self.client.head_object.assert_called_once()
        self.sleep.assert_not_called()

    def test_reconciliation_cannot_accept_different_object_attributes(self):
        changes = {
            "length": lambda value: value.update(ContentLength=1),
            "checksum": lambda value: value["Metadata"].update(sha256="0" * 64),
            "identity": lambda value: value["Metadata"].update(kind="other"),
            "content_type": lambda value: value.update(ContentType="text/plain"),
            "cache_control": lambda value: value.update(CacheControl="public"),
        }
        for label, change in changes.items():
            with self.subTest(change=label):
                self.client = FakeR2()
                self.store.client = self.client
                self.store._put("object", b"abc", metadata={"kind": "test"})
                change(self.client.objects["object"])
                self.client.put_object = Mock(side_effect=HttpError("ServiceUnavailable", 503, retries=8))
                self.client.head_object = Mock(wraps=self.client.head_object)
                with self.assertRaises(R2TransportError):
                    self.store._put("object", b"abc", metadata={"kind": "test"})
                self.client.put_object.assert_called_once()
                self.client.head_object.assert_called_once()
        self.sleep.assert_not_called()

    def test_permission_and_unknown_put_errors_do_not_reconcile_or_replay(self):
        for error, expected in ((Denied(), R2PermissionError),
                                (HttpError("UnknownError", 400), R2TransportError),
                                (OSError("unknown"), R2TransportError)):
            with self.subTest(error=error):
                self.client.put_object = Mock(side_effect=error)
                self.client.head_object = Mock()
                with self.assertRaises(expected):
                    self.store._put("object", b"abc", metadata={})
                self.client.put_object.assert_called_once()
                self.client.head_object.assert_not_called()
        self.sleep.assert_not_called()

    def test_failed_reconciliation_never_replays_put(self):
        self.client.put_object = Mock(side_effect=HttpError("ServiceUnavailable", 503, retries=8))
        self.client.head_object = Mock(side_effect=HttpError("429", 429, retries=8))
        with self.assertRaises(R2TransportError):
            self.store._put("object", b"abc", metadata={})
        self.client.put_object.assert_called_once()
        self.client.head_object.assert_called_once()
        self.sleep.assert_not_called()

    def test_stream_timeout_closes_and_restarts_only_get(self):
        key, body, head = self.seed_read()
        self.client.head_object = Mock(return_value=head)
        broken, complete = FakeBody(b"partial"), FakeBody(body)
        broken.read = Mock(side_effect=TimeoutError("interrupted stream"))
        self.client.get_object = Mock(side_effect=[{"Body": broken}, {"Body": complete}])
        self.assertEqual(self.store._get(key, maximum=1024), body)
        self.assertEqual(self.client.head_object.call_count, 1)
        self.assertEqual(self.client.get_object.call_count, 2)
        self.assertTrue(broken.closed)
        self.assertTrue(complete.closed)
        self.sleep.assert_called_once_with(2.25)

    def test_stream_retry_exhaustion_closes_every_body(self):
        key, body, head = self.seed_read()
        self.client.head_object = Mock(return_value=head)
        bodies = [FakeBody(body) for _ in range(len(READ_RETRY_DELAYS) + 1)]
        for stream in bodies:
            stream.read = Mock(side_effect=TimeoutError("interrupted stream"))
        self.client.get_object = Mock(side_effect=[{"Body": stream} for stream in bodies])
        with self.assertRaises(R2TransportError):
            self.store._get(key, maximum=1024)
        self.assertEqual(self.client.head_object.call_count, 1)
        self.assertEqual(self.client.get_object.call_count, len(bodies))
        self.assertTrue(all(stream.closed for stream in bodies))
        self.assertEqual(self.sleep.call_args_list, [call(delay + 0.25) for delay in READ_RETRY_DELAYS])

    def test_stream_does_not_multiply_sdk_retries_or_retry_unknown_errors(self):
        for error, retries in [(TimeoutError("interrupted stream"), 8), (OSError("unknown"), 0)]:
            with self.subTest(error=error, retries=retries):
                key, body, head = self.seed_read()
                self.client.head_object = Mock(return_value=head)
                broken = FakeBody(body)
                broken.read = Mock(side_effect=error)
                self.client.get_object = Mock(return_value={"Body": broken, "ResponseMetadata": {"RetryAttempts": retries}})
                with self.assertRaises(R2TransportError):
                    self.store._get(key, maximum=1024)
                self.assertEqual(self.client.get_object.call_count, 1)
                self.assertTrue(broken.closed)
        self.sleep.assert_not_called()

    def test_checksum_and_length_validation_never_retry(self):
        for change in ("checksum", "length", "maximum"):
            with self.subTest(change=change):
                key, body, head = self.seed_read()
                if change == "checksum":
                    head["Metadata"]["sha256"] = "0" * 64
                elif change == "length":
                    head["ContentLength"] += 1
                self.client.head_object = Mock(return_value=head)
                stream = FakeBody(body)
                self.client.get_object = Mock(return_value={"Body": stream})
                with self.assertRaises(R2IntegrityError):
                    self.store._get(key, maximum=1 if change == "maximum" else 1024)
                self.assertEqual(self.client.head_object.call_count, 1)
                self.assertEqual(self.client.get_object.call_count, 0 if change == "maximum" else 1)
                self.assertEqual(stream.closed, change != "maximum")
        self.sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
