#!/usr/bin/env python3
"""Test real checkpoint/archive code with an isolated in-memory S3 transport."""
from __future__ import annotations

from contextlib import redirect_stdout, redirect_stderr
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import private_workflow_handoff as handoff
import smoke_private_checkpoints as smoke


class StorageError(RuntimeError):
    def __init__(self, code):
        super().__init__("sensitive endpoint bucket/object " + code)
        self.response = {"Error": {"Code": code}}


class FakeS3:
    def __init__(self):
        self.objects = {"unrelated-object": (b"untouched", {})}
        self.deleted = []
        self.fail_deletes = set()

    def upload_file(self, path, bucket, key, ExtraArgs):
        self.objects[key] = (Path(path).read_bytes(), ExtraArgs["Metadata"])

    def download_file(self, bucket, key, path):
        if key not in self.objects:
            raise StorageError("NoSuchKey")
        Path(path).write_bytes(self.objects[key][0])

    def head_object(self, *, Bucket, Key):
        if Key not in self.objects:
            raise StorageError("404")
        data, metadata = self.objects[Key]
        return {"ContentLength": len(data), "Metadata": metadata}

    def delete_object(self, *, Bucket, Key):
        self.deleted.append(Key)
        if Key in self.fail_deletes:
            raise StorageError("AccessDenied")
        self.objects.pop(Key, None)


class PrivateCheckpointSmokeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.diagnostics = Path(self.temp.name) / "diagnostics"
        self.client = FakeS3()
        self.keys = smoke.object_keys("1234", "2")
        for patcher in (patch.object(handoff, "build_r2_client", return_value=self.client),
                        patch.object(handoff, "r2_bucket", return_value="private-bucket-never-output"),
                        patch.dict(os.environ, {"GITHUB_RUN_ID": "1234", "GITHUB_RUN_ATTEMPT": "2"})):
            patcher.start()
            self.addCleanup(patcher.stop)
        self.output = io.StringIO()
        for context in (redirect_stdout(self.output), redirect_stderr(self.output)):
            context.__enter__()
            self.addCleanup(context.__exit__, None, None, None)

    def result(self, phase):
        return json.loads((self.diagnostics / f"{phase}.json").read_text())

    def test_two_checkpoints_restore_from_empty_tree_and_republish_complete_handoff(self):
        self.assertTrue(smoke.run_phase("save", self.diagnostics))
        self.assertEqual(set(self.client.objects), {"unrelated-object", self.keys["generation"], self.keys["translation"]})
        self.assertTrue(smoke.run_phase("verify", self.diagnostics))
        verified = self.result("verify")
        self.assertEqual(verified["objects_restored"], 3)
        self.assertEqual(verified["reuse_checks_passed"], 1)
        self.assertEqual(verified["files_verified"], 22)
        self.assertEqual(verified["fixture_sha256"], self.result("save")["fixture_sha256"])
        self.assertTrue(smoke.run_phase("cleanup", self.diagnostics))
        self.assertEqual(set(self.client.objects), {"unrelated-object"})
        self.assertEqual(set(self.client.deleted), set(self.keys.values()))
        self.assertEqual(self.result("cleanup")["objects_verified_absent"], 3)

    def test_missing_checkpoint_is_failure_and_cleanup_still_succeeds(self):
        self.assertFalse(smoke.run_phase("verify", self.diagnostics))
        self.assertFalse(self.result("verify")["success"])
        self.assertTrue(smoke.run_phase("cleanup", self.diagnostics))
        self.assertEqual(set(self.client.deleted), set(self.keys.values()))

    def test_corrupted_checksum_fails_and_never_republishes_bad_handoff(self):
        self.assertTrue(smoke.run_phase("save", self.diagnostics))
        data, _metadata = self.client.objects[self.keys["generation"]]
        self.client.objects[self.keys["generation"]] = (data, {"sha256": "f" * 64})
        self.assertFalse(smoke.run_phase("verify", self.diagnostics))
        self.assertNotIn(self.keys["handoff"], self.client.objects)
        self.assertTrue(smoke.run_phase("cleanup", self.diagnostics))

    def test_failure_does_not_expose_storage_details_or_claim_success(self):
        with patch.object(handoff, "build_r2_client", side_effect=StorageError("AccessDenied")):
            self.assertEqual(smoke.main(["save", "--diagnostics-out", str(self.diagnostics)]), 1)
        public = self.output.getvalue() + (self.diagnostics / "save.json").read_text()
        for forbidden in ("sensitive", "endpoint", "bucket", smoke.NAMESPACE, "AccessDenied", "source_mineru", "Public synthetic"):
            self.assertNotIn(forbidden, public)
        self.assertEqual(set(self.result("save")), {"schema_version", "phase", "success"})

    def test_cleanup_attempts_every_exact_object_and_fails_if_any_remains(self):
        self.assertTrue(smoke.run_phase("save", self.diagnostics))
        self.client.fail_deletes.add(self.keys["translation"])
        self.assertFalse(smoke.run_phase("cleanup", self.diagnostics))
        self.assertEqual(set(self.client.deleted), set(self.keys.values()))
        self.assertEqual(self.result("cleanup")["objects_verified_absent"], 2)
        self.assertIn(self.keys["translation"], self.client.objects)

    def test_unsafe_identity_rejected_before_any_storage_action(self):
        for invalid in ("", "../123", "0", "123/2", "1\n", "-1", "a"):
            with self.assertRaises(ValueError):
                smoke.object_keys(invalid, "1")
            with self.assertRaises(ValueError):
                smoke.object_keys("123", invalid)
        self.assertNotEqual(self.keys, smoke.object_keys("1234", "3"))
        with patch.dict(os.environ, {"GITHUB_RUN_ID": ""}):
            self.assertFalse(smoke.run_phase("cleanup", self.diagnostics))
        self.assertFalse(self.client.deleted)

    def test_workflow_storage_is_manual_opt_in_and_always_cleans_exact_objects(self):
        workflow = (smoke.REPO / ".github/workflows/portal-locale-translation-preflight.yml").read_text()
        inputs = workflow.split("workflow_dispatch:", 1)[1].split("pull_request:", 1)[0]
        self.assertIn("verify_private_checkpoint:", inputs)
        self.assertIn("default: false", inputs)
        self.assertIn("type: boolean", inputs)
        job = workflow.split("  private-checkpoint-smoke:\n", 1)[1]
        self.assertIn("github.event_name == 'workflow_dispatch' && inputs.verify_private_checkpoint == true", job)
        for phase in smoke.PHASES:
            self.assertIn(f"scripts/smoke_private_checkpoints.py {phase}", job)
        self.assertIn("if: always()", job.split("Delete only this run's synthetic objects", 1)[1].split("- name:", 1)[0])
        self.assertIn("if: always()", job.split("Upload content-free private checkpoint diagnostics", 1)[1])
        self.assertNotIn("DEEPSEEK", job)
        self.assertNotIn("delete-prefix", job)
        self.assertNotIn("setup-offline-translation", job)


if __name__ == "__main__":
    unittest.main()
