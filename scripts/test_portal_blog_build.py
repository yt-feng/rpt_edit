#!/usr/bin/env python3
"""Regression checks for the Portal Suite static Blog build."""

from __future__ import annotations

from datetime import date
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts" / "build_portal_suite_site.py"
SPEC = importlib.util.spec_from_file_location("portal_site_builder", BUILD_SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {BUILD_SCRIPT}")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


def write_payload(root: Path, source: str, date_folder: str, name: str, articles: list[dict]) -> Path:
    folder = root / source / date_folder if source else root / date_folder
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    path.write_text(json.dumps({"articles": articles}, ensure_ascii=False), encoding="utf-8")
    return path


class BlogSanitizerTests(unittest.TestCase):
    def test_sanitizer_preserves_wechat_layout_and_removes_active_content(self) -> None:
        raw = """
          <section style="margin:10px 0;background:#F7F3E8;color:#142033;position:fixed;background-image:url(javascript:alert(1))">
            <script><script>alert(1)</script>blocked script text</script>
            <iframe><iframe>nested frame</iframe>blocked frame text</iframe>
            <p onclick="alert(2)" style="line-height:1.78;behavior:url(test.htc)">
              保留正文<span style="font-weight:700;color:#2457A7">与排版</span>
            </p>
            <a href="java&#x73;cript:alert(3)" onmouseover="alert(4)">坏链接</a>
            <a href="https://example.com/research?q=1&amp;x=2">安全链接</a>
            <img src="http://mmbiz.qpic.cn/example/0?from=appmsg" onerror="alert(5)" alt="研报原图" style="max-width:100%;height:auto">
            <svg onload="alert(6)"><text>blocked svg text</text></svg>
          </section>
        """
        cleaned = builder.sanitize_blog_html(raw)

        self.assertIn("<section", cleaned)
        self.assertIn("margin:10px 0", cleaned)
        self.assertIn("background:#F7F3E8", cleaned)
        self.assertIn("color:#142033", cleaned)
        self.assertIn("line-height:1.78", cleaned)
        self.assertIn("font-weight:700", cleaned)
        self.assertIn("保留正文", cleaned)
        self.assertIn("与排版", cleaned)
        self.assertNotIn("position", cleaned)
        self.assertNotIn("background-image", cleaned)
        self.assertNotIn("behavior", cleaned)
        self.assertNotIn("javascript", cleaned.lower())
        self.assertNotIn("onclick", cleaned.lower())
        self.assertNotIn("onerror", cleaned.lower())
        self.assertNotIn("onmouseover", cleaned.lower())
        self.assertNotIn("script text", cleaned)
        self.assertNotIn("nested frame", cleaned)
        self.assertNotIn("blocked frame", cleaned)
        self.assertNotIn("blocked svg", cleaned)
        self.assertNotIn("<script", cleaned.lower())
        self.assertNotIn("<iframe", cleaned.lower())
        self.assertNotIn("<svg", cleaned.lower())
        self.assertIn('href="https://example.com/research?q=1&amp;x=2"', cleaned)
        self.assertIn('rel="noopener noreferrer nofollow"', cleaned)
        self.assertNotRegex(cleaned, r"<a[^>]+>坏链接")
        self.assertIn('src="https://mmbiz.qpic.cn/example/0?from=appmsg"', cleaned)
        self.assertIn('loading="lazy"', cleaned)
        self.assertIn('decoding="async"', cleaned)

    def test_protocol_relative_images_and_entity_obfuscation_are_handled(self) -> None:
        cleaned = builder.sanitize_blog_html(
            '<img data-src="//mmbiz.qpic.cn/a.jpg"><a href="jav&#x09;ascript:alert(1)">x</a>'
        )
        self.assertIn('src="https://mmbiz.qpic.cn/a.jpg"', cleaned)
        self.assertNotIn("javascript", cleaned.lower())
        self.assertEqual("", builder.sanitize_blog_url("data:text/html,boom", image=True))
        self.assertEqual("", builder.sanitize_blog_url("/relative/path", image=True))

    def test_json_ld_cannot_be_terminated_by_draft_metadata(self) -> None:
        rendered = builder.render_json_ld({"headline": "</script><img src=x onerror=alert(1)>"})
        self.assertNotIn("</script>", rendered.lower())
        self.assertNotIn("<img", rendered.lower())
        self.assertIn("\\u003c/script\\u003e", rendered)


class BlogBuildTests(unittest.TestCase):
    def test_blog_placeholder_is_materialized_only_in_built_article(self) -> None:
        article = {
            "slug": "20260810-0123456789abcdef",
            "title": "站点地址测试",
            "digest": "检查公开归档与部署产物的边界。",
            "author": "Portal Suite",
            "content": "<p>访问 portal.example.invalid 查看全文。</p>",
            "date": "2026-08-10",
            "last_date": "2026-08-10",
            "origins": [{"source": "legacy", "source_label": "历史稿件", "date": "2026-08-10"}],
        }

        rendered = builder.render_blog_article(article, "https://published.example.test")

        self.assertIn("published.example.test 查看全文", rendered)
        self.assertNotIn("portal.example.invalid 查看全文", rendered)
        self.assertIn("portal.example.invalid", article["content"])

    def test_blog_placeholder_survives_source_materialization_until_archive_render(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            materialized_path = Path(temporary) / "materialized_builder.py"
            materialized_source = BUILD_SCRIPT.read_text(encoding="utf-8").replace(
                    "portal.example.invalid",
                    "published.example.test",
                ).replace('"portal"', '"published-service"')
            materialized_path.write_text(
                materialized_source,
                encoding="utf-8",
            )
            spec = importlib.util.spec_from_file_location("materialized_portal_site_builder", materialized_path)
            self.assertIsNotNone(spec)
            self.assertIsNotNone(spec.loader if spec else None)
            materialized = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(materialized)

            article = {
                "slug": "20260810-fedcba9876543210",
                "title": "部署后归档地址测试",
                "digest": "模拟私有部署值已经写入构建脚本。",
                "author": "Portal Suite",
                "content": "<p>访问 portal.example.invalid 查看全文。</p>",
                "date": "2026-08-10",
                "last_date": "2026-08-10",
                "origins": [],
            }
            rendered = materialized.render_blog_article(article, "https://published.example.test")

            self.assertIn("published.example.test 查看全文", rendered)
            self.assertNotIn("portal.example.invalid 查看全文", rendered)

    def test_public_blog_title_suffix_is_exact_idempotent_and_identity_stable(self) -> None:
        raw = "数据中心的供应瓶颈"
        expected = f"{raw} | KC桌面"

        self.assertEqual(expected, builder.blog_public_title(raw))
        self.assertEqual(expected, builder.blog_public_title(expected))
        self.assertEqual(expected, builder.blog_public_title(f"{expected} | KC桌面"))
        self.assertEqual(
            builder.blog_article_fingerprint(raw, "<p>正文</p>"),
            builder.blog_article_fingerprint(expected, "<p>正文</p>"),
        )

    def test_public_catalog_omits_internal_storage_and_ingestion_metadata(self) -> None:
        catalog = {
            "schema_version": 1,
            "updated_at_bjt": "2026-08-02 10:00:00 +0800",
            "dropbox_root": "/zip_backup",
            "total_size_bytes": 123456,
            "storage_limit_bytes": 8589934592,
            "storage": {
                "limit_bytes": 8589934592,
                "total_size_bytes": 123456,
                "last_pruned_at_bjt": "2026-08-02 09:00:00 +0800",
                "pdf_pruned_this_run_dates": ["260601"],
            },
            "items": [{
                "id": "report-1",
                "title": "Public report",
                "size_bytes": 42,
                "present_in_latest_scan": True,
                "pdf_archived_at_bjt": "2026-08-02 09:00:00 +0800",
                "archive_reason": "pdf_storage_limit",
            }],
        }

        public = builder.public_catalog(catalog)

        self.assertEqual(1, public["item_count"])
        self.assertEqual("report-1", public["items"][0]["id"])
        for internal_key in ("dropbox_root", "total_size_bytes", "storage_limit_bytes", "storage"):
            self.assertNotIn(internal_key, public)
        for internal_key in ("present_in_latest_scan", "pdf_archived_at_bjt", "archive_reason"):
            self.assertNotIn(internal_key, public["items"][0])

    def test_current_search_index_daily_shards_are_generated(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "data" / "search_index_current"
            catalog = {
                "items": [
                    {"id": "current-six", "date_folder": "260722"},
                    {"id": "current-eight", "date_folder": "20260723"},
                ],
            }
            index = {
                "schema_version": 1,
                "updated_at_bjt": "2026-07-26 12:00:00",
                "item_count": 2,
                "items": [
                    {"id": "current-six", "text": "first extracted report body"},
                    {"id": "current-eight", "text": "second extracted report body"},
                ],
            }

            manifest = builder.write_search_index_shards(
                index=index,
                catalog=catalog,
                output_dir=output,
                partition="day",
            )
            self.assertTrue((output / "manifest.json").is_file())
            self.assertEqual(
                ["shard_260723.json", "shard_260722.json"],
                [row["file"] for row in manifest["shards"]],
            )
            first = json.loads((output / "shard_260722.json").read_text(encoding="utf-8"))
            second = json.loads((output / "shard_260723.json").read_text(encoding="utf-8"))
            self.assertEqual(["current-six"], [row["id"] for row in first["items"]])
            self.assertEqual(["current-eight"], [row["id"] for row in second["items"]])

    def test_wechat_image_reupload_urls_do_not_duplicate_an_article(self) -> None:
        first = builder.sanitize_blog_html(
            '<section><p>同一正文</p><img src="https://mmbiz.qpic.cn/old-token" alt="图表"></section>'
        )
        retried = builder.sanitize_blog_html(
            '<section><p>同一正文</p><img src="https://mmbiz.qpic.cn/new-token" alt="图表"></section>'
        )
        changed_text = builder.sanitize_blog_html(
            '<section><p>不同正文</p><img src="https://mmbiz.qpic.cn/new-token" alt="图表"></section>'
        )
        changed_alt = builder.sanitize_blog_html(
            '<section><p>同一正文</p><img src="https://mmbiz.qpic.cn/new-token" alt="另一张图"></section>'
        )

        first_id = builder.blog_article_fingerprint("重复上传", first)
        self.assertEqual(first_id, builder.blog_article_fingerprint("重复上传", retried))
        self.assertNotEqual(first_id, builder.blog_article_fingerprint("重复上传", changed_text))
        self.assertNotEqual(first_id, builder.blog_article_fingerprint("重复上传", changed_alt))

    def test_all_sources_cutoff_deduplication_and_static_pages(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            drafts = temp / "wechat_drafts"
            output = temp / "site"
            shared_content = (
                '<section style="padding:18px;background:#F7F3E8">'
                '<p>跨目录重复正文</p>'
                '<img src="http://mmbiz.qpic.cn/shared.jpg" alt="原图">'
                '</section>'
            )
            write_payload(drafts, "xhs_notes", "260725", "draft_payload_01.json", [
                {"title": "起始日前文章", "content": "<p>不应发布</p>"},
            ])
            write_payload(drafts, "xhs_notes", "260726", "draft_payload_01.json", [
                {"title": "重复文章", "author": "Portal Suite", "digest": "摘要 A", "content": shared_content},
                {"title": "同一 payload 的第二篇", "content": "<p>第二篇完整正文</p>"},
            ])
            write_payload(drafts, "", "260725", "draft_payload_01.json", [
                {"title": "根目录起始日前文章", "content": "<p>不应发布</p>"},
            ])
            write_payload(drafts, "", "260726", "draft_payload_01.json", [
                {"title": "根目录首日文章", "content": "<p>应在首日发布</p>"},
            ])
            write_payload(drafts, "institutions", "260728", "draft_payload_01.json", [
                {"title": "重复文章", "author": "Portal Suite", "digest": "摘要 A", "content": f"\n{shared_content}\n"},
                {"title": "机构文章", "content": "<p>机构正文</p>"},
            ])
            write_payload(drafts, "consulting", "260728", "draft_payload_02.json", [
                {"title": "咨询文章", "content": "<p>咨询正文</p>"},
            ])
            write_payload(drafts, "ark", "260729", "draft_payload_01.json", [
                {"title": "ARK文章", "content": "<p>ARK正文</p>"},
            ])
            write_payload(drafts, "institutions_bis_repair", "260729", "draft_payload_02.json", [
                {"title": "机构修复文章", "content": "<p>修复正文</p>"},
            ])
            write_payload(drafts, "", "260729", "draft_payload_01.json", [
                {"title": "根目录历史文章", "content": "<p>根目录正文</p>"},
            ])
            write_payload(drafts, "legacy", "260731", "draft_payload_01.json", [
                {"title": "legacy 子目录文章", "content": "<p>legacy正文</p>"},
            ])

            articles = builder.build_blog(output, drafts, "https://portal.example.invalid", date(2026, 7, 27))
            self.assertEqual(9, len(articles), "every articles[] entry after the cutoff is retained, with one duplicate removed")
            self.assertNotIn("起始日前文章", {row["title"] for row in articles})
            self.assertNotIn("根目录起始日前文章", {row["title"] for row in articles})
            self.assertEqual(
                {
                    "重复文章", "同一 payload 的第二篇", "机构文章", "咨询文章", "ARK文章",
                    "机构修复文章", "根目录首日文章", "根目录历史文章", "legacy 子目录文章",
                },
                {row["title"] for row in articles},
            )

            root_first_day = next(row for row in articles if row["title"] == "根目录首日文章")
            self.assertEqual("2026-07-27", root_first_day["date"])
            self.assertRegex(root_first_day["slug"], r"^20260727-[0-9a-f]{16}$")

            duplicate = next(row for row in articles if row["title"] == "重复文章")
            self.assertEqual("2026-07-27", duplicate["date"])
            self.assertRegex(duplicate["slug"], r"^20260727-[0-9a-f]{16}$")
            self.assertEqual(2, len(duplicate["origins"]))
            self.assertEqual({"xhs_notes", "institutions"}, {row["source"] for row in duplicate["origins"]})
            self.assertIn("https://mmbiz.qpic.cn/shared.jpg", duplicate["content"])

            index_html = (output / "blog/index.html").read_text(encoding="utf-8")
            self.assertIn("ARK文章", index_html)
            self.assertIn("根目录历史文章", index_html)
            self.assertIn("legacy 子目录文章", index_html)
            self.assertIn("ARK Invest", index_html)
            self.assertIn("综合研报", index_html)
            self.assertIn("历史稿件", index_html)
            self.assertIn('<time datetime="2026-07-27">2026-07-27</time>', index_html)
            self.assertIn("2026-07-30", index_html)
            self.assertIn("Content-Security-Policy", index_html)
            self.assertIn('data-page="blog"', index_html)
            self.assertIn('id="blogMarketViews"', index_html)
            self.assertIn("每日 Market Views", index_html)
            self.assertIn('src="../assets/app.js"', index_html)
            self.assertIn('src="../assets/site-runtime.js"', index_html)
            self.assertIn("<title>KC桌面 Blog | 每日研报与研究文章</title>", index_html)
            self.assertIn('<meta property="og:site_name" content="KC桌面">', index_html)
            self.assertIn("重复文章 | KC桌面", index_html)

            pages = sorted((output / "blog").glob("*.html"))
            self.assertGreater(len(pages), len(articles), "legacy source-bearing URLs remain as redirects")
            duplicate_page = (output / "blog" / f'{duplicate["slug"]}.html').read_text(encoding="utf-8")
            public_title = "重复文章 | KC桌面"
            self.assertIn(f"<title>{public_title}</title>", duplicate_page)
            self.assertIn(f'<meta property="og:title" content="{public_title}">', duplicate_page)
            self.assertIn(f'<meta name="twitter:title" content="{public_title}">', duplicate_page)
            self.assertIn(f"<h1>{public_title}</h1>", duplicate_page)
            self.assertIn('src="../assets/site-runtime.js"', duplicate_page)
            self.assertNotIn(f"{public_title} | KC桌面", duplicate_page)
            json_ld_match = re.search(
                r'<script type="application/ld\+json">(.*?)</script>',
                duplicate_page,
                flags=re.S,
            )
            self.assertIsNotNone(json_ld_match)
            article_schema = json.loads(json_ld_match.group(1))
            self.assertEqual(public_title, article_schema["headline"])
            self.assertEqual(["KC桌面"], article_schema["keywords"])
            self.assertIn("跨目录重复正文", duplicate_page)
            self.assertIn("2026-07-27 · 外资研报", duplicate_page)
            self.assertIn("2026-07-28 · 研究机构", duplicate_page)
            self.assertNotIn("外资研报（xhs_notes）", duplicate_page)
            self.assertNotIn("研究机构（institutions）", duplicate_page)
            self.assertNotIn('title="xhs_notes"', duplicate_page)
            self.assertNotIn("xhs_notes", index_html)
            for internal_name in ("xhs_notes", "wechat_drafts", "draft_payload", "source_mineru", "shard_"):
                self.assertNotIn(internal_name, duplicate_page)
                self.assertNotIn(internal_name, index_html)
            self.assertNotIn("http://mmbiz.qpic.cn", duplicate_page)

            catalog = {"items": [], "item_count": 0, "updated_at_bjt": "2026-07-31 12:00:00"}
            builder.build_seo_outputs(output, catalog, "https://portal.example.invalid", articles)
            sitemap_index = (output / "sitemap.xml").read_text(encoding="utf-8")
            sitemap_blog = (output / "sitemap-blog-1.xml").read_text(encoding="utf-8")
            sitemap_baidu = (output / "sitemap-baidu.xml").read_text(encoding="utf-8")
            self.assertIn("sitemap-blog-1.xml", sitemap_index)
            self.assertIn(f'blog/{duplicate["slug"]}.html', sitemap_blog)
            self.assertIn("https://portal.example.invalid/blog/", sitemap_baidu)

    def test_empty_source_still_builds_blog_landing_page(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            output = temp / "site"
            articles = builder.build_blog(output, temp / "missing", "https://portal.example.invalid", date(2026, 7, 27))
            self.assertEqual([], articles)
            index_html = (output / "blog/index.html").read_text(encoding="utf-8")
            self.assertIn("内容将从 2026-07-27 起发布", index_html)

    def test_sharded_archive_retains_pruned_days_and_rejects_corruption(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            drafts = temp / "wechat_drafts"
            archive = temp / "data/blog_archive"
            first_output = temp / "site-day-1"
            second_output = temp / "site-day-2"
            write_payload(drafts, "xhs_notes", "260726", "draft_payload_01.json", [
                {
                    "title": "Day 1",
                    "content": '<p>第一天正文</p><img src="https://mmbiz.qpic.cn/day-one-old" alt="日图">',
                },
            ])

            first_articles = builder.build_blog(
                first_output,
                drafts,
                "https://portal.example.invalid",
                date(2026, 7, 27),
                archive,
            )
            self.assertEqual(["Day 1"], [row["title"] for row in first_articles])
            self.assertEqual("2026-07-27", first_articles[0]["date"])
            self.assertRegex(first_articles[0]["slug"], r"^20260727-[0-9a-f]{16}$")
            first_shards = list((archive / "20260727").glob("*.json"))
            self.assertEqual(1, len(first_shards))
            self.assertTrue((archive / "manifest.json").is_file())

            shutil.rmtree(drafts / "xhs_notes" / "260726")
            write_payload(drafts, "xhs_notes", "260727", "draft_payload_01.json", [
                {
                    "title": "Day 1",
                    "content": '<p>第一天正文</p><img src="https://mmbiz.qpic.cn/day-one-new" alt="日图">',
                },
            ])
            write_payload(drafts, "ark", "260728", "draft_payload_01.json", [
                {"title": "Day 2", "content": "<p>第二天正文</p>"},
            ])
            second_articles = builder.build_blog(
                second_output,
                drafts,
                "https://portal.example.invalid",
                date(2026, 7, 27),
                archive,
            )
            self.assertEqual({"Day 1", "Day 2"}, {row["title"] for row in second_articles})
            self.assertIn("Day 1", (second_output / "blog/index.html").read_text(encoding="utf-8"))
            day_one = next(row for row in second_articles if row["title"] == "Day 1")
            self.assertEqual("2026-07-27", day_one["date"])
            self.assertEqual("2026-07-28", day_one["last_date"])
            self.assertIn("day-one-new", day_one["content"])
            self.assertNotIn("day-one-old", day_one["content"])
            self.assertTrue((second_output / "blog" / f'{day_one["slug"]}.html').is_file())
            self.assertEqual(1, len(list((archive / "20260727").glob("*.json"))))
            self.assertEqual(1, len(list((archive / "20260728").glob("*.json"))))

            first_shards[0].write_text("{broken", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Invalid Blog archive shard"):
                builder.build_blog(
                    temp / "site-corrupt",
                    drafts,
                    "https://portal.example.invalid",
                    date(2026, 7, 27),
                    archive,
                )


if __name__ == "__main__":
    unittest.main()
