#!/usr/bin/env python3
from __future__ import annotations

import ast
import contextlib
import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import inspect_portal_handoff_replay as inspector


ROOT = Path(__file__).resolve().parents[1]


def receipt(**updates):
    value = {
        "schema_version": 1, "paid_provider_requests": 0,
        "batch": {"generation": "a" * 64, "candidates": {"pt": "c" * 64, "fr": "b" * 64}},
        "producer": {"run_id": "12345", "attempt": "1", "sha": "d" * 40},
        "private_note": "never-export@example.invalid",
        "private_source": "private original text",
    }
    value.update(updates)
    raw = json.dumps(value, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest(), raw


class InspectorTests(unittest.TestCase):
    def test_input_is_bounded_strict_and_deduplicates_exact_receipts(self):
        values = [f"{index:064x}" for index in range(20)]
        self.assertEqual(inspector.receipt_hashes(",\n".join(values)), values)
        self.assertEqual(inspector.receipt_hashes(values[0] + ",\n" + values[0]), [values[0]])
        for invalid in ("", " ,\n", "A" * 64, "a" * 63, "../" + "a" * 64,
                        "https://example.invalid/" + "a" * 64, "a" * 64 + " " + "b" * 64,
                        ",".join(values + ["f" * 64]), " " * 2000):
            with self.subTest(invalid=invalid[:24]), self.assertRaises(inspector.InspectionError):
                inspector.receipt_hashes(invalid)

    def test_exact_checksum_and_projection_preserve_only_replay_metadata(self):
        identity, raw = receipt()
        result = inspector.replay_identity(identity, raw)
        self.assertEqual(result, {
            "handoff_sha256": identity,
            "generation": "a" * 64,
            "candidates": {"fr": "b" * 64, "pt": "c" * 64},
            "producer": {"run_id": "12345", "attempt": "1", "sha": "d" * 40},
        })
        self.assertNotIn("private", json.dumps(result))
        self.assertNotIn("@", json.dumps(result))
        with self.assertRaisesRegex(inspector.InspectionError, "checksum"):
            inspector.replay_identity("f" * 64, raw)
        for invalid in (b"", b"x" * 65537, "not bytes"):
            with self.assertRaises(inspector.InspectionError):
                inspector.replay_identity(identity, invalid)

    def test_authenticated_but_malformed_shapes_fail_closed(self):
        _, raw = receipt()
        original = json.loads(raw)
        edits = [
            ("schema_version", True), ("schema_version", 2), ("paid_provider_requests", 1),
            ("producer", {"run_id": "0", "attempt": "1", "sha": "d" * 40}),
            ("producer", {"run_id": "123", "attempt": "1", "sha": "D" * 40}),
            ("producer", {"run_id": "123", "attempt": "1", "sha": "d" * 40, "email": "private"}),
            ("batch", {"generation": "a" * 64, "candidates": {}}),
            ("batch", {"generation": "a" * 64, "candidates": {"en": "b" * 64}}),
            ("batch", {"generation": "a" * 64, "candidates": {"fr": "bad"}}),
            ("batch", {"generation": "a" * 64, "candidates": {"fr": "b" * 64}, "extra": "private"}),
        ]
        for field, change in edits:
            value = copy.deepcopy(original)
            value[field] = change
            encoded = json.dumps(value).encode()
            with self.subTest(field=field, change=change), self.assertRaises(inspector.InspectionError):
                inspector.replay_identity(hashlib.sha256(encoded).hexdigest(), encoded)
        duplicate = b'{"schema_version":1,"schema_version":1}'
        with self.assertRaisesRegex(inspector.InspectionError, "duplicate"):
            inspector.replay_identity(hashlib.sha256(duplicate).hexdigest(), duplicate)

    def test_each_requested_receipt_is_read_once_and_failure_returns_no_partial_report(self):
        first, raw_first = receipt()
        second, raw_second = receipt(producer={"run_id": "6789", "attempt": "2", "sha": "e" * 40})
        calls = []
        def read(identity):
            calls.append(identity)
            return {first: raw_first, second: raw_second}[identity]
        report = inspector.inspect(read, f"{first},{second},{first}")
        self.assertEqual(calls, [first, second])
        self.assertEqual(report["receipt_count"], 2)
        self.assertEqual([row["producer"]["run_id"] for row in report["receipts"]], ["12345", "6789"])
        with self.assertRaises(KeyError):
            inspector.inspect(read, f"{first},{'f' * 64}")

    def test_cli_reads_only_requested_receipt_keys_and_writes_projected_artifact(self):
        identity, raw = receipt()
        calls = []
        class ReadOnlyStore:
            def key(self, *parts):
                self.parts = parts
                return "/".join(parts)
            def _get(self, key, *, maximum):
                calls.append((key, maximum))
                return raw
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output.json"
            with patch.object(inspector.R2Store, "from_env", return_value=ReadOnlyStore()) as factory:
                with contextlib.redirect_stdout(io.StringIO()) as stdout:
                    status = inspector.main(["--receipt-hashes", identity, "--output", str(output)])
            self.assertEqual(status, 0)
            factory.assert_called_once_with(inspector.DEFAULT_PREFIX)
            self.assertEqual(calls, [(f"publication-handoffs/{identity}/receipt.json", 65536)])
            self.assertEqual(output.stat().st_mode & 0o777, 0o600)
            self.assertEqual(json.loads(output.read_text())["receipt_count"], 1)
            self.assertNotIn("private", output.read_text())
            self.assertEqual(json.loads(stdout.getvalue()), {"ok": True, "receipt_count": 1})

    def test_cli_validates_before_credentials_and_redacts_provider_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output.json"
            with patch.object(inspector.R2Store, "from_env") as factory:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(inspector.main(["--receipt-hashes", "invalid", "--output", str(output)]), 1)
                factory.assert_not_called()
            with patch.object(inspector.R2Store, "from_env", side_effect=RuntimeError("credential-private-url")):
                with contextlib.redirect_stdout(io.StringIO()) as stdout:
                    self.assertEqual(inspector.main(["--receipt-hashes", "a" * 64, "--output", str(output)]), 1)
                self.assertNotIn("credential", stdout.getvalue())
                self.assertEqual(json.loads(stdout.getvalue())["error"], "handoff_receipt_inspection_failed")
            self.assertFalse(output.exists())

    def test_inspector_and_workflow_cannot_dispatch_or_modify_cloud_state(self):
        source = Path(inspector.__file__).read_text()
        tree = ast.parse(source)
        calls = {node.func.attr for node in ast.walk(tree)
                 if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)}
        self.assertFalse(calls & {"_put", "put_object", "delete_object", "delete_objects", "list_objects_v2",
                                  "dispatch", "post", "put", "delete", "run", "Popen"})
        workflow = (ROOT / ".github/workflows/portal-handoff-replay-inspect.yml").read_text()
        self.assertIn("contents: read", workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("github.actor == github.repository_owner", workflow)
        self.assertIn("github.triggering_actor == github.repository_owner", workflow)
        self.assertIn("ref: ${{ github.sha }}", workflow)
        self.assertIn("needs: test", workflow)
        self.assertIn("python3 -B scripts/test_inspect_portal_handoff_replay.py", workflow)
        self.assertIn("HANDOFF_SHA256S: ${{ inputs.receipt_hashes }}", workflow)
        self.assertEqual(workflow.count("inputs.receipt_hashes"), 1, "input must only enter the fixed environment field")
        self.assertIn("path: ${{ runner.temp }}/handoff-replay-identities.json", workflow)
        self.assertIn("retention-days: 1", workflow)
        self.assertNotIn("secrets.", workflow.split("  inspect:")[0])
        for forbidden in ("portal-production-release", "actions: write", "contents: write", "gh workflow",
                          "publish_static_slot", "versions deploy", "force-cancel"):
            self.assertNotIn(forbidden, workflow)


if __name__ == "__main__":
    unittest.main()
