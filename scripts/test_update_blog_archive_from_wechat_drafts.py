#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "update_blog_archive_from_wechat_drafts.py"


def write_payload(root: Path, source: str, date_folder: str, filename: str, articles: list[dict[str, str]]) -> None:
    output_dir = root / source / date_folder if source else root / date_folder
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / filename).write_text(json.dumps({"articles": articles}, ensure_ascii=False), encoding="utf-8")


class BlogArchiveUpdateTest(unittest.TestCase):
    def test_update_archive_from_current_drafts_and_keep_pruned_posts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            drafts = temp / "wechat_drafts"
            archive = temp / "portal_suite" / "data" / "blog_archive"

            write_payload(drafts, "xhs_notes", "260726", "draft_payload_01.json", [
                {"title": "Day One", "content": "<p>第一天正文</p>"},
            ])
            first = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--wechat-drafts-root",
                    str(drafts),
                    "--blog-archive-root",
                    str(archive),
                ],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertIn("draft_articles=1", first.stdout)
            self.assertEqual(1, len(list((archive / "20260727").glob("*.json"))))

            for path in (drafts / "xhs_notes" / "260726").glob("*"):
                path.unlink()
            (drafts / "xhs_notes" / "260726").rmdir()
            write_payload(drafts, "consulting", "260728", "draft_payload_01.json", [
                {"title": "Day Two", "content": "<p>第二天正文</p>"},
            ])
            second = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--wechat-drafts-root",
                    str(drafts),
                    "--blog-archive-root",
                    str(archive),
                ],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertIn("archived_after=2", second.stdout)
            self.assertEqual(1, len(list((archive / "20260727").glob("*.json"))))
            self.assertEqual(1, len(list((archive / "20260728").glob("*.json"))))

            shards = sorted(archive.glob("*/*.json"))
            serialized = "\n".join(path.read_text(encoding="utf-8") for path in shards)
            self.assertNotIn("wechat_drafts", serialized)
            self.assertNotIn("draft_payload", serialized)


if __name__ == "__main__":
    unittest.main()
