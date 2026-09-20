#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from private_workflow_handoff import create_archive, download_shards, extract_archive, validate_key, validate_prefix


class PrivateWorkflowHandoffTests(unittest.TestCase):
    def test_missing_shard_is_rejected_before_materialization(self) -> None:
        prefix = "private/run/260914"
        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir) / "bank"
            with patch("private_workflow_handoff.list_keys", return_value=[
                f"{prefix}/shard_{i}.tar.gz" for i in range(12)
            ]), patch("private_workflow_handoff.download_directory") as download:
                with self.assertRaisesRegex(RuntimeError, "Expected 13 shard handoffs.*found 12"):
                    download_shards(prefix, destination, 13, client=Mock(), bucket="test")
                download.assert_not_called()
                self.assertFalse(destination.exists())

    def test_complete_shards_are_all_materialized(self) -> None:
        prefix = "private/run/260914"
        with tempfile.TemporaryDirectory() as temp_dir:
            destination = Path(temp_dir) / "bank"
            with patch("private_workflow_handoff.list_keys", return_value=[
                f"{prefix}/shard_{i}.tar.gz" for i in reversed(range(13))
            ]), patch("private_workflow_handoff.download_directory") as download:
                self.assertEqual(13, download_shards(prefix, destination, 13, client=Mock(), bucket="test"))
                self.assertEqual(13, download.call_count)
                self.assertEqual(
                    [destination / f"shard_{i}" for i in range(13)],
                    [call.args[1] for call in download.call_args_list],
                )

    def test_archive_excludes_raw_pdfs_and_media(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source"
            (source / "report" / "assets").mkdir(parents=True)
            (source / "report" / "mineru_raw").mkdir()
            (source / "report" / "wechat_article.md").write_text("article", encoding="utf-8")
            (source / "report" / "source_mineru.md").write_text("source", encoding="utf-8")
            (source / "report" / "assets" / "chart.png").write_bytes(b"image")
            (source / "report" / "mineru_raw" / "origin.pdf").write_bytes(b"private-pdf")
            (source / "report" / "rendered.pdf").write_bytes(b"rendered-pdf")
            (source / "report" / "audio.mp3").write_bytes(b"audio")

            archive = root / "payload.tar.gz"
            count, _size, digest = create_archive(source, archive)
            destination = root / "destination"
            extracted_count = extract_archive(archive, destination)

            self.assertEqual(3, count)
            self.assertEqual(3, extracted_count)
            self.assertEqual(64, len(digest))
            self.assertTrue((destination / "report" / "wechat_article.md").exists())
            self.assertTrue((destination / "report" / "source_mineru.md").exists())
            self.assertTrue((destination / "report" / "assets" / "chart.png").exists())
            self.assertFalse((destination / "report" / "mineru_raw").exists())
            self.assertFalse((destination / "report" / "rendered.pdf").exists())
            self.assertFalse((destination / "report" / "audio.mp3").exists())

    def test_key_and_prefix_validation(self) -> None:
        self.assertEqual("private/run/shard_0.tar.gz", validate_key("/private/run/shard_0.tar.gz"))
        self.assertEqual("private/run/", validate_prefix("/private/run/"))
        for value in ("", "../escape.tar.gz", "private/not-an-archive"):
            with self.assertRaises(ValueError):
                validate_key(value)
        for value in ("", "../escape"):
            with self.assertRaises(ValueError):
                validate_prefix(value)

    def test_explicit_translated_pdf_whitelist_preserves_raw_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = root / "source" / "01-report"
            report.mkdir(parents=True)
            (report / "translation_status.json").write_text('{}')
            (report / "portal_translated_report_01.pdf").write_bytes(b'translated')
            (report / "original.pdf").write_bytes(b'original')
            (report / "portal_translated_report_01.pdf.zip").write_bytes(b'zip')
            raw = report / "mineru_raw"
            raw.mkdir()
            (raw / "translation_status.json").write_text('{}')
            (raw / "portal_translated_report_01.pdf").write_bytes(b'raw')
            unmarked = root / "source" / "02-unmarked"
            unmarked.mkdir()
            (unmarked / "portal_translated_report_02.pdf").write_bytes(b'no-status')
            archive = root / "payload.tar.gz"
            create_archive(root / "source", archive, include_translated_pdfs=True)
            extract_archive(archive, root / "restored")
            files = {path.relative_to(root / "restored").as_posix() for path in (root / "restored").rglob('*') if path.is_file()}
            self.assertEqual(files, {'01-report/translation_status.json', '01-report/portal_translated_report_01.pdf'})


if __name__ == "__main__":
    unittest.main()
