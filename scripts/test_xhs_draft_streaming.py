import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import push_xhs_notes_to_wechat_drafts as uploader


class XhsDraftStreamingTests(unittest.TestCase):
    def test_hard_block_checks_final_title_even_when_raw_title_is_safe(self) -> None:
        record = uploader.hard_blocked_xhs_title_record({
            "raw_title": "高盛：货币市场与相关指标观察",
            "source_report_name": "高盛-货币市场观察",
            "wechat_title": "高盛：人民币定价机制出现变化",
        })
        self.assertIsNotNone(record)
        self.assertEqual("forbidden_title_term_rmb_pricing", record["skip_reason"])
        self.assertEqual("wechat_title", record["matched_title_field"])

    def test_all_hard_blocked_titles_create_no_article_or_draft_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report_dir = root / "xhs_notes" / "dropbox" / "260822" / "shard_0" / "0001-blocked"
            report_dir.mkdir(parents=True)
            (report_dir / "wechat_article.md").write_text(
                "# 高盛：人民币定价机制出现变化\n\n这是一段完整的测试正文。",
                encoding="utf-8",
            )

            output_root = root / "wechat_drafts"
            argv = [
                "push_xhs_notes_to_wechat_drafts.py",
                "--dropbox-output-root",
                str(root / "xhs_notes" / "dropbox"),
                "--date-folder",
                "260822",
                "--output-root",
                str(output_root),
                "--trailing-image",
                "",
                "--site-url",
                "https://private.example.invalid",
                "--dry-run",
            ]
            with mock.patch.object(sys, "argv", argv), mock.patch.object(
                uploader,
                "build_article",
            ) as build_mock, mock.patch.object(
                uploader,
                "resolve_repo_asset_path",
            ) as asset_mock:
                self.assertEqual(0, uploader.main())

            build_mock.assert_not_called()
            asset_mock.assert_not_called()
            output_dir = output_root / "260822"
            self.assertEqual([], list(output_dir.glob("draft_payload_*.json")))
            summary = json.loads((output_dir / "wechat_draft_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(1, summary["input_selected_count"])
            self.assertEqual(0, summary["selected_count"])
            self.assertEqual(1, summary["skipped_title_policy_count"])
            self.assertEqual(0, summary["draft_count"])
            self.assertEqual("skipped_title_policy", summary["status"])

    def test_hard_blocked_raw_title_is_skipped_before_article_build(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date_dir = root / "xhs_notes" / "dropbox" / "260822" / "shard_0"
            date_dir.mkdir(parents=True)
            blocked_report = date_dir / "0001-blocked-report"
            allowed_report = date_dir / "0002-allowed-report"
            blocked_report.mkdir()
            allowed_report.mkdir()
            (blocked_report / "wechat_article.md").write_text(
                "# 高盛：人民币定价机制出现变化\n\n这是一段完整的测试正文。",
                encoding="utf-8",
            )
            (allowed_report / "wechat_article.md").write_text(
                "# 高盛：AI基础设施订单同比增长20%\n\n这是一段完整的测试正文。",
                encoding="utf-8",
            )

            built_reports: list[Path] = []

            def fake_build_article(
                report_dir: Path,
                _index: int,
                *_args: object,
                **_kwargs: object,
            ) -> dict[str, object]:
                built_reports.append(report_dir)
                title = "高盛：AI基础设施订单同比增长20%"
                return {
                    "title": title,
                    "wechat_title": title,
                    "raw_title": title,
                    "institution_name": "高盛",
                    "source_report_name": report_dir.name,
                    "report_dir": str(report_dir),
                    "title_decision": {},
                    "article": {
                        "article_type": "news",
                        "title": title,
                        "content": "<p>测试正文</p><p>portal.example.invalid</p>",
                        "thumb_media_id": "thumb-allowed",
                    },
                    "content_chars": 4,
                    "content_bytes": 12,
                    "visible_text_chars": 4,
                    "inline_images": [],
                    "body_image_count": 0,
                    "cover_image": "",
                }

            output_root = root / "wechat_drafts"
            argv = [
                "push_xhs_notes_to_wechat_drafts.py",
                "--dropbox-output-root",
                str(root / "xhs_notes" / "dropbox"),
                "--date-folder",
                "260822",
                "--output-root",
                str(output_root),
                "--articles-per-draft",
                "8",
                "--trailing-image",
                "",
                "--site-url",
                "https://private.example.invalid",
                "--dry-run",
            ]
            with mock.patch.object(sys, "argv", argv), mock.patch.object(
                uploader,
                "build_article",
                side_effect=fake_build_article,
            ):
                self.assertEqual(0, uploader.main())

            self.assertEqual([allowed_report], built_reports)
            output_dir = output_root / "260822"
            payload = json.loads((output_dir / "draft_payload_01.json").read_text(encoding="utf-8"))
            self.assertEqual(1, len(payload["articles"]))
            self.assertEqual("高盛：AI基础设施订单同比增长20%", payload["articles"][0]["title"])
            self.assertNotIn("人民币定价", json.dumps(payload, ensure_ascii=False))

            summary = json.loads((output_dir / "wechat_draft_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(2, summary["input_selected_count"])
            self.assertEqual(1, summary["selected_count"])
            self.assertEqual(1, summary["skipped_title_policy_count"])
            self.assertEqual(
                "forbidden_title_term_rmb_pricing",
                summary["skipped_title_policy"][0]["skip_reason"],
            )
            self.assertEqual(
                "高盛：人民币定价机制出现变化",
                summary["skipped_title_policy"][0]["blocked_title"],
            )
            self.assertEqual(1, summary["draft_count"])

            title_log = json.loads((output_dir / "wechat_title_log.json").read_text(encoding="utf-8"))
            self.assertEqual(2, title_log["article_count"])
            self.assertEqual(1, title_log["uploaded_count"])
            skipped_entries = [item for item in title_log["articles"] if not item["uploaded"]]
            self.assertEqual(1, len(skipped_entries))
            self.assertEqual(
                "forbidden_title_term_rmb_pricing",
                skipped_entries[0]["skip_reason"],
            )

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
                        "content": "<p>测试正文</p><p>portal.example.invalid</p>",
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
                "--site-url",
                "https://private.example.invalid",
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
            serialized = json.dumps(payload, ensure_ascii=False)
            self.assertIn("portal.example.invalid", serialized)
            self.assertNotIn("private.example.invalid", serialized)


if __name__ == "__main__":
    unittest.main()
