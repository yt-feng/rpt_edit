#!/usr/bin/env python3
"""Checkpoint validation uses the publication loader without mutating its input."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import copy
import gzip
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import build_portal_locales as builder
from offline_translation import MODEL_ID
from validate_portal_locale_checkpoint import CheckpointValidationError, main, validate_checkpoint
import translate_portal_titles as titles


class CheckpointValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "private-checkpoint.json.gz"
        self.cache = builder.empty_cache(MODEL_ID, provider="hymt")
        self.cache["locales"]["ko"]["a" * 64] = {
            "source": "private source text", "translation": "검증된 번역",
            "provider": "hymt", "model": MODEL_ID,
        }

    def write(self, value):
        self.path.write_bytes(gzip.compress(json.dumps(value).encode(), mtime=0))

    def test_healthy_current_cache_is_read_only_and_counts_accepted_rows(self):
        self.write(self.cache)
        before = self.path.read_bytes()
        result = validate_checkpoint(self.path)
        self.assertEqual(result, {"status": "valid", "entry_count": 1,
                                  "entries_by_locale": {"ko": 1, "ja": 0, "ar": 0}})
        self.assertEqual(self.path.read_bytes(), before)

    def test_missing_zero_byte_and_symlink_are_not_valid_checkpoints(self):
        with self.assertRaises(CheckpointValidationError):
            validate_checkpoint(self.path)
        self.path.touch()
        with self.assertRaises(CheckpointValidationError):
            validate_checkpoint(self.path)
        target = self.path.with_name("valid.json.gz")
        target.write_bytes(gzip.compress(json.dumps(self.cache).encode()))
        self.path.unlink()
        self.path.symlink_to(target)
        with self.assertRaises(CheckpointValidationError):
            validate_checkpoint(self.path)

    def test_corrupt_gzip_json_schema_and_rows_are_rejected(self):
        invalid_payloads = [b"not gzip", gzip.compress(b"{broken JSON"),
                            gzip.compress(json.dumps({**self.cache, "schema_version": 999}).encode())]
        malformed_row = copy.deepcopy(self.cache)
        malformed_row["locales"]["ko"]["a" * 64]["translation"] = ""
        invalid_payloads.append(gzip.compress(json.dumps(malformed_row).encode()))
        malformed_locales = copy.deepcopy(self.cache)
        malformed_locales["locales"] = []
        invalid_payloads.append(gzip.compress(json.dumps(malformed_locales).encode()))
        for raw in invalid_payloads:
            with self.subTest(raw_length=len(raw)):
                self.path.write_bytes(raw)
                with self.assertRaises(CheckpointValidationError):
                    validate_checkpoint(self.path)
                self.assertEqual(self.path.read_bytes(), raw)

    def test_valid_zero_translation_checkpoint_is_preserved(self):
        self.write(builder.empty_cache(MODEL_ID, provider="hymt"))
        result = validate_checkpoint(self.path)
        self.assertEqual(result["status"], "valid")
        self.assertEqual(result["entry_count"], 0)

    def test_legacy_paid_cache_migration_is_accepted(self):
        self.cache.update(provider="deepseek", model=builder.DEFAULT_DEEPSEEK_MODEL)
        self.cache["locales"]["ko"]["a" * 64].pop("provider")
        self.cache["locales"]["ko"]["a" * 64].pop("model")
        self.write(self.cache)
        before = self.path.read_bytes()
        self.assertEqual(validate_checkpoint(self.path)["entry_count"], 1)
        self.assertEqual(self.path.read_bytes(), before)

    def test_model_upgrade_retains_paid_rows_and_drops_old_offline_rows(self):
        self.cache["model"] = "old-offline-model"
        self.cache["locales"]["ko"]["b" * 64] = {
            "source": "previously paid source", "translation": "유료 번역",
            "provider": "legacy-cache", "source_cache_provider": "deepseek",
            "model": builder.DEFAULT_DEEPSEEK_MODEL,
        }
        self.write(self.cache)
        result = validate_checkpoint(self.path)
        self.assertEqual(result["entry_count"], 1)
        self.cache["locales"]["ko"].pop("b" * 64)
        self.write(self.cache)
        self.assertEqual(validate_checkpoint(self.path)["entry_count"], 0)

    def test_namespace_change_obeys_loader_empty_cache_policy(self):
        self.cache["prompt_version"] = "old-prompt"
        self.write(self.cache)
        with redirect_stderr(io.StringIO()):
            result = validate_checkpoint(self.path)
        self.assertEqual(result["status"], "valid")
        self.assertEqual(result["entry_count"], 0)

    def test_cli_reports_only_safe_status_and_counts(self):
        self.write(self.cache)
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main([str(self.path)]), 0)
        self.assertEqual(json.loads(output.getvalue())["entry_count"], 1)
        self.assertNotIn(str(self.path), output.getvalue())
        self.assertNotIn("private source", output.getvalue())
        self.path.write_bytes(b"private invalid payload")
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main([str(self.path)]), 1)
        self.assertEqual(json.loads(output.getvalue()), {"status": "invalid", "reason": "invalid_checkpoint"})

    def title_cache(self, *, legacy=False):
        model = builder.DEFAULT_DEEPSEEK_MODEL if legacy else MODEL_ID
        row = {"source": "Private research outlook", "model": model,
               "prompt_version": titles.TITLE_PROMPT_VERSION, "title_zh": "研究展望"}
        return {"schema_version": titles.TITLE_CACHE_SCHEMA_VERSION,
                "provider": "deepseek" if legacy else titles.PROVIDER,
                "entries": {titles.title_cache_key(row["source"], model): row}}

    def test_title_cache_uses_real_loader_and_preserves_legacy_migration(self):
        for legacy, count in ((False, 1), (True, 2)):
            with self.subTest(legacy=legacy):
                self.path.write_text(json.dumps(self.title_cache(legacy=legacy)), encoding="utf-8")
                before = self.path.read_bytes()
                with mock.patch("requests.sessions.Session.request", side_effect=AssertionError("No API call")):
                    result = validate_checkpoint(self.path, kind="title")
                self.assertEqual(result, {"status": "valid", "entry_count": count})
                self.assertEqual(self.path.read_bytes(), before)

    def test_title_cache_rejects_corrupt_json_schema_and_identity(self):
        malformed = self.title_cache()
        next(iter(malformed["entries"].values()))["source"] = "Changed without its identity key"
        invalid = ["{bad JSON", json.dumps({**self.title_cache(), "schema_version": 99}), json.dumps(malformed)]
        for raw in invalid:
            with self.subTest(raw=raw):
                self.path.write_text(raw, encoding="utf-8")
                with self.assertRaises(CheckpointValidationError):
                    validate_checkpoint(self.path, kind="title")

    def test_title_cli_accepts_valid_empty_cache_but_rejects_empty_file(self):
        self.path.write_text(json.dumps({"schema_version": 1, "provider": titles.PROVIDER, "entries": {}}))
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(["--kind", "title", str(self.path)]), 0)
        self.assertEqual(json.loads(output.getvalue()), {"status": "valid", "entry_count": 0})
        self.path.write_text("")
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(main(["--kind", "title", str(self.path)]), 1)
        self.assertEqual(json.loads(output.getvalue())["status"], "invalid")
        self.assertNotIn(str(self.path), output.getvalue())


if __name__ == "__main__":
    unittest.main()
