#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from private_workflow_handoff import (
    create_archive,
    download_latest_directory,
    download_latest_shards,
    extract_archive,
    latest_run_with_archive,
    latest_run_with_shards,
    validate_key,
    validate_prefix,
)


class PrivateWorkflowHandoffTests(unittest.TestCase):
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

    def test_latest_run_selection_for_dated_market_views_handoffs(self) -> None:
        keys = [
            "_private-workflow-handoff/market-views/dropbox/100/260804/shard_0.tar.gz",
            "_private-workflow-handoff/market-views/dropbox/101/260803/shard_0.tar.gz",
            "_private-workflow-handoff/market-views/dropbox/102/260804/shard_0.tar.gz",
            "_private-workflow-handoff/market-views/dropbox/102/260804/shard_1.tar.gz",
            "_private-workflow-handoff/market-views/institutions/99/260804/xhs_notes.tar.gz",
            "_private-workflow-handoff/market-views/institutions/103/260804/xhs_notes.tar.gz",
        ]

        class FakeClient:
            def list_objects_v2(self, **_kwargs):  # type: ignore[no-untyped-def]
                return {"Contents": [{"Key": key} for key in keys]}

        client = FakeClient()
        self.assertEqual(
            "102",
            latest_run_with_shards(
                "_private-workflow-handoff/market-views/dropbox",
                "260804",
                client=client,
                bucket="bucket",
            ),
        )
        self.assertEqual(
            "103",
            latest_run_with_archive(
                "_private-workflow-handoff/market-views/institutions",
                "260804",
                "xhs_notes.tar.gz",
                client=client,
                bucket="bucket",
            ),
        )
        self.assertIsNone(
            latest_run_with_archive(
                "_private-workflow-handoff/market-views/consulting",
                "260804",
                "xhs_notes.tar.gz",
                client=client,
                bucket="bucket",
            )
        )

    def test_optional_latest_downloads_can_be_absent(self) -> None:
        class EmptyClient:
            def list_objects_v2(self, **_kwargs):  # type: ignore[no-untyped-def]
                return {}

        client = EmptyClient()
        self.assertEqual(
            0,
            download_latest_shards(
                "_private-workflow-handoff/market-views/dropbox",
                "260804",
                Path("unused"),
                optional=True,
                client=client,
                bucket="bucket",
            ),
        )
        self.assertEqual(
            0,
            download_latest_directory(
                "_private-workflow-handoff/market-views/institutions",
                "260804",
                "xhs_notes.tar.gz",
                Path("unused"),
                optional=True,
                client=client,
                bucket="bucket",
            ),
        )


if __name__ == "__main__":
    unittest.main()
