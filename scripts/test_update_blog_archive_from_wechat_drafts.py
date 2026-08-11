#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "update_blog_archive_from_wechat_drafts.py"
PUBLIC_SITE_HOST = "".join(("kc", "desk", ".com"))
PUBLIC_SITE_HOST_PLACEHOLDER = "portal.example.invalid"


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
                {
                    "title": "Day Two",
                    "content": f"<p>第二天正文</p><p>更新信息参见{PUBLIC_SITE_HOST_PLACEHOLDER}</p>",
                },
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
            self.assertIn(PUBLIC_SITE_HOST_PLACEHOLDER, serialized)
            self.assertNotIn(PUBLIC_SITE_HOST, serialized)

    def test_rejects_private_identity_before_persisting_archive_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            drafts = temp / "wechat_drafts"
            archive = temp / "portal_suite" / "data" / "blog_archive"
            write_payload(drafts, "consulting", "260811", "draft_payload_01.json", [
                {
                    "title": "Private footer regression",
                    "content": f"<p>更新信息参见{PUBLIC_SITE_HOST}</p>",
                },
            ])

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--wechat-drafts-root",
                    str(drafts),
                    "--blog-archive-root",
                    str(archive),
                ],
                check=False,
                text=True,
                capture_output=True,
            )

            self.assertNotEqual(0, result.returncode)
            self.assertIn("Private identity marker", result.stderr)
            self.assertEqual([], list(archive.glob("*/*.json")))

    def test_title_only_and_content_only_records_round_trip_without_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            drafts = temp / "wechat_drafts"
            archive = temp / "portal_suite" / "data" / "blog_archive"
            write_payload(drafts, "consulting", "260811", "draft_payload_01.json", [
                {"title": "Title only", "content": ""},
                {"title": "", "content": "<p>只有正文也应稳定归档。</p>"},
            ])

            command = [
                sys.executable,
                str(SCRIPT),
                "--wechat-drafts-root",
                str(drafts),
                "--blog-archive-root",
                str(archive),
            ]
            first = subprocess.run(command, check=True, text=True, capture_output=True)
            second = subprocess.run(command, check=True, text=True, capture_output=True)

            self.assertIn("new_articles=2", first.stdout)
            self.assertIn("archived_after=2", second.stdout)
            self.assertIn("new_articles=0", second.stdout)
            self.assertEqual(2, len(list(archive.glob("*/*.json"))))


if __name__ == "__main__":
    unittest.main()
