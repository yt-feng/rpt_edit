#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from materialize_shard_artifacts import materialize


class MaterializeShardArtifactsTests(unittest.TestCase):
    def test_materializes_and_validates_downloaded_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifacts = root / "artifacts"
            (artifacts / "unrelated-directory").mkdir(parents=True)
            for shard in range(2):
                for report in range(2):
                    report_dir = artifacts / f"final-dropbox-macro-shard-260801-{shard}" / f"report-{shard}-{report}"
                    report_dir.mkdir(parents=True)
                    (report_dir / "wechat_article.md").write_text("article", encoding="utf-8")

            destination = root / "xhs_notes" / "dropbox" / "260801"
            shard_count, report_count = materialize(artifacts, destination, 2, 4)

            self.assertEqual(2, shard_count)
            self.assertEqual(4, report_count)
            self.assertTrue((destination / "shard_0" / "report-0-0" / "wechat_article.md").exists())
            self.assertTrue((destination / "shard_1" / "report-1-1" / "wechat_article.md").exists())

    def test_rejects_unexpected_report_count(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            report_dir = root / "artifacts" / "shard-0" / "report"
            report_dir.mkdir(parents=True)
            (report_dir / "note.md").write_text("note", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "Expected 2 reports"):
                materialize(root / "artifacts", root / "destination", 1, 2)


if __name__ == "__main__":
    unittest.main()
