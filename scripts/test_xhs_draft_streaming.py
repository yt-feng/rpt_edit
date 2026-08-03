import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import push_xhs_notes_to_wechat_drafts as uploader


class XhsDraftStreamingTests(unittest.TestCase):
    def test_completed_group_is_written_before_later_article_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date_dir = root / "xhs_notes" / "dropbox" / "260723" / "shard_0"
            date_dir.mkdir(parents=True)
            for index in range(1, 10):
                report_dir = date_dir / f"{index:04d}-report-{index}"
                report_dir.mkdir()
                (report_dir / "wechat_article.md").write_text(
                    f"# 高盛：测试主题{index}\n\n这是一段完整的测试正文。",
                    encoding="utf-8",
                )

            def fake_build_article(
                report_dir: Path,
                index: int,
                *_args: object,
                **_kwargs: object,
            ) -> dict[str, object]:
                if index == 9:
                    raise RuntimeError("later article failed")
                title = f"高盛：测试主题{index}"
                return {
                    "title": title,
                    "wechat_title": title,
                    "article": {
                        "article_type": "news",
                        "title": title,
                        "content": "<p>测试正文</p>",
                        "thumb_media_id": f"thumb-{index}",
                    },
                }

            output_root = root / "wechat_drafts"
            argv = [
                "push_xhs_notes_to_wechat_drafts.py",
                "--dropbox-output-root",
                str(root / "xhs_notes" / "dropbox"),
                "--date-folder",
                "260723",
                "--output-root",
                str(output_root),
                "--articles-per-draft",
                "8",
                "--trailing-image",
                "",
                "--dry-run",
            ]
            with mock.patch.object(sys, "argv", argv), mock.patch.object(
                uploader,
                "build_article",
                side_effect=fake_build_article,
            ):
                with self.assertRaisesRegex(RuntimeError, "later article failed"):
                    uploader.main()

            payload_path = output_root / "260723" / "draft_payload_01.json"
            self.assertTrue(payload_path.is_file())
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
            self.assertEqual(8, len(payload["articles"]))


if __name__ == "__main__":
    unittest.main()
