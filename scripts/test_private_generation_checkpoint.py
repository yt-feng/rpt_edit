#!/usr/bin/env python3
"""Check cross-run reuse against real source hashes and private archive boundaries."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import private_generation_checkpoint as checkpoint
from check_completed_shard import completed_shard_reason, manifest_source_names
from select_macro_trend_pdfs import copy_selected
from private_workflow_handoff import create_archive, extract_archive

REPO = Path(__file__).resolve().parent.parent


class StorageError(RuntimeError):
    def __init__(self, code):
        self.response = {"Error": {"Code": code}}


class GenerationCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = self.root / "selected.json"
        self.row = {"process_rank": 1, "id": 0, "process_local_path": "_selected/01-report.pdf", "content_sha256": "a" * 64}
        self.manifest.write_text(json.dumps([self.row]))
        self.options = {"model": "deepseek-flash", "wechat_length": "2000"}
        self.identity = checkpoint.input_identity(self.manifest, 0, 5, self.options, REPO)
        self.key = checkpoint.checkpoint_key("260920", 0, self.identity)

    def build_complete(self, directory):
        item = directory / "0001-01-report"
        item.mkdir(parents=True)
        (item / "source_mineru.md").write_text("private original research")
        (item / "wechat_article.md").write_text("private completed article")
        (item / "zhihu_article.md").write_text("private completed Zhihu")
        (item / "zhihu_article.md.generation.json").write_text(json.dumps({"input_sha256": "b" * 64}))
        (item / "status.json").write_text(json.dumps({"source_pdf": "0001-01-report.pdf", "wechat_article": "wechat_article.md"}))
        (directory / "shard_run_summary.md").write_text("\n".join([
            "- Selected PDFs available to shards: 1", "- Shard index: 0", "- Reports per shard: 5", "- Report directories generated: 1",
        ]))
        (directory / "finalize_summary.json").write_text(json.dumps([{"item": item.name, "zhihu_article.md": "zhihu_article.md"}]))
        (directory / "sensitive_content_guard_summary.json").write_text(json.dumps([{"path": "wechat_article.md", "api_errors": [], "rewrite_error": ""}]))
        return item

    def archive_upload(self, source, key):
        create_archive(source, self.root / "checkpoint.tar.gz")

    def archive_download(self, key, destination):
        return extract_archive(self.root / "checkpoint.tar.gz", destination)

    def test_new_runner_reuses_complete_generation_and_keeps_private_payload_out_of_public_repository(self):
        first = self.root / "runner1"
        item = self.build_complete(first)
        (item / "raw.pdf").write_bytes(b"excluded raw PDF")
        (item / "video.mp4").write_bytes(b"excluded video")
        with patch.object(checkpoint, "upload_directory", side_effect=self.archive_upload) as upload:
            self.assertTrue(checkpoint.save(first, self.key, self.identity, complete=True))
        self.assertTrue(upload.call_args.args[1].startswith("_workflow-cache/report-generation/"))
        shutil.rmtree(first)
        second = self.root / "runner2"
        with patch.object(checkpoint, "download_directory", side_effect=self.archive_download):
            self.assertTrue(checkpoint.restore(second, self.key, self.identity))
        self.assertTrue(completed_shard_reason(second, self.manifest, 0, 1, 5)[0])
        self.assertEqual((second / item.name / "wechat_article.md").read_text(), "private completed article")
        self.assertFalse((second / item.name / "raw.pdf").exists())
        self.assertFalse((second / item.name / "video.mp4").exists())

    def test_same_name_new_pdf_bytes_new_parameters_or_new_prompt_cannot_hit_old_checkpoint(self):
        self.manifest.write_text(json.dumps([{**self.row, "content_sha256": "c" * 64}]))
        self.assertNotEqual(self.identity, checkpoint.input_identity(self.manifest, 0, 5, self.options, REPO))
        self.manifest.write_text(json.dumps([self.row]))
        self.assertNotEqual(self.identity, checkpoint.input_identity(self.manifest, 0, 5, {**self.options, "wechat_length": "3500"}, REPO))
        with patch.object(checkpoint, "GENERATION_FILES", (*checkpoint.GENERATION_FILES, "scripts/deepseek_usage.py")):
            self.assertNotEqual(self.identity, checkpoint.input_identity(self.manifest, 0, 5, self.options, REPO))
        self.assertEqual(self.identity, checkpoint.input_identity(self.manifest, 0, 5, {**self.options, "force_reprocess": "true"}, REPO))

    def test_source_identity_matches_lexical_batch_order_above_99_reports(self):
        rows = [{**self.row, "process_rank": rank, "process_local_path": f"_selected/{rank:02d}-report-{rank}.pdf"} for rank in (10, 11, 100)]
        self.manifest.write_text(json.dumps(rows))
        self.assertEqual(manifest_source_names(self.manifest, 0, 2), ["report10pdf", "report100pdf"])
        identity = checkpoint.input_identity(self.manifest, 0, 2, self.options, REPO)
        rows[1]["content_sha256"] = "f" * 64  # 11-... is in the next shard.
        self.manifest.write_text(json.dumps(rows))
        self.assertEqual(identity, checkpoint.input_identity(self.manifest, 0, 2, self.options, REPO))
        rows[2]["content_sha256"] = "e" * 64
        self.manifest.write_text(json.dumps(rows))
        self.assertNotEqual(identity, checkpoint.input_identity(self.manifest, 0, 2, self.options, REPO))

    def test_partial_finalization_resumes_existing_articles_without_skipping_failed_work(self):
        first = self.root / "runner1"
        item = self.build_complete(first)
        (first / "finalize_summary.json").write_text(json.dumps([{"zhihu_article.md_error": "provider failed"}]))
        with patch.object(checkpoint, "upload_directory", side_effect=self.archive_upload):
            checkpoint.save(first, self.key, self.identity, complete=True)
        self.assertFalse(json.loads((first / checkpoint.CHECKPOINT_FILE).read_text())["complete"])
        second = self.root / "runner2"
        with patch.object(checkpoint, "download_directory", side_effect=self.archive_download):
            checkpoint.restore(second, self.key, self.identity)
        self.assertFalse(completed_shard_reason(second, self.manifest, 0, 1, 5)[0])
        self.assertTrue((second / item.name / "wechat_article.md").exists())
        self.assertFalse((second / "shard_run_summary.md").exists())

    def test_failed_or_empty_report_marker_does_not_satisfy_skip_existing(self):
        first = self.root / "runner1"
        item = self.build_complete(first)
        (item / "status.json").write_text(json.dumps({"error": "generation interrupted"}))
        with patch.object(checkpoint, "upload_directory", side_effect=self.archive_upload):
            checkpoint.save(first, self.key, self.identity, complete=False)
        second = self.root / "runner2"
        with patch.object(checkpoint, "download_directory", side_effect=self.archive_download):
            checkpoint.restore(second, self.key, self.identity)
        self.assertFalse((second / item.name / "wechat_article.md").exists())
        self.assertTrue((second / item.name / "source_mineru.md").exists())

    def test_storage_failure_never_silently_restarts_paid_generation(self):
        directory = self.root / "output"
        self.build_complete(directory)
        for error in (StorageError("AccessDenied"), TimeoutError("transport")):
            with patch.object(checkpoint, "download_directory", side_effect=error):
                with self.assertRaises(type(error)):
                    checkpoint.restore(directory, self.key, self.identity)
            self.assertTrue((directory / "shard_run_summary.md").exists())
        with patch.object(checkpoint, "download_directory", side_effect=StorageError("NoSuchKey")):
            self.assertFalse(checkpoint.restore(directory, self.key, self.identity))
        self.assertEqual(list(directory.iterdir()), [])

    def test_force_generation_bypasses_restore_and_untrusted_identity_is_rejected(self):
        first = self.root / "runner1"
        self.build_complete(first)
        with patch.object(checkpoint, "download_directory") as download:
            self.assertFalse(checkpoint.restore(first, self.key, self.identity, force=True))
            download.assert_not_called()
        self.build_complete(first)
        with patch.object(checkpoint, "upload_directory", side_effect=self.archive_upload):
            checkpoint.save(first, self.key, "f" * 64, complete=True)
        with patch.object(checkpoint, "download_directory", side_effect=self.archive_download):
            with self.assertRaisesRegex(ValueError, "identity"):
                checkpoint.restore(self.root / "runner2", self.key, self.identity)

    def test_missing_hash_fails_closed_and_selector_hashes_actual_pdf_bytes(self):
        self.manifest.write_text(json.dumps([{k: v for k, v in self.row.items() if k != "content_sha256"}]))
        with self.assertRaisesRegex(ValueError, "content hash"):
            checkpoint.input_identity(self.manifest, 0, 5, self.options, REPO)
        source = self.root / "source.pdf"
        source.write_bytes(b"actual PDF payload")
        [selected] = copy_selected([{"name": "source.pdf", "local_path": str(source)}], self.root / "selected", 1)
        self.assertEqual(selected["content_sha256"], hashlib.sha256(source.read_bytes()).hexdigest())

    def test_empty_or_unusable_finalizer_cannot_make_checkpoint_complete(self):
        directory = self.root / "output"
        item = self.build_complete(directory)
        (item / "zhihu_article.md.generation.json").unlink()
        with patch.object(checkpoint, "upload_directory"):
            checkpoint.save(directory, self.key, self.identity, complete=True)
        self.assertFalse(json.loads((directory / checkpoint.CHECKPOINT_FILE).read_text())["complete"])
        with patch.object(checkpoint, "upload_directory") as upload:
            self.assertFalse(checkpoint.save(self.root / "absent", self.key, self.identity))
            upload.assert_not_called()

    def test_workflow_restores_before_paid_work_saves_on_failure_and_republishes_reused_handoff(self):
        workflow = (REPO / ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml").read_text()
        job = workflow.split("  process-shard:\n", 1)[1].split("  package-publish-ready:\n", 1)[0]
        self.assertLess(job.index("private_generation_checkpoint.py restore"), job.index("Check for a matching completed shard"))
        self.assertLess(job.index("Check for a matching completed shard"), job.index("Generate shard outputs"))
        save = job.split("      - name: Save private generation checkpoint including partial progress", 1)[1].split("      - name:", 1)[0]
        self.assertIn("always() && steps.generation_checkpoint.outcome == 'success'", save)
        handoff = job.split("      - name: Upload shard to private R2 handoff", 1)[1].split("      - name:", 1)[0]
        self.assertNotIn("steps.completed.outputs.complete != 'true'", handoff)
        self.assertIn('"$OUTPUT_DIR"', handoff)
        self.assertNotIn("_workflow-cache/report-generation", workflow.split("  cleanup-private-handoff:", 1)[1])


if __name__ == "__main__":
    unittest.main()
