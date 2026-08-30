#!/usr/bin/env python3

from __future__ import annotations

from datetime import date
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_portal_suite_site as builder  # noqa: E402
import submit_portal_indexnow as indexnow  # noqa: E402


def sample_item(report_id: str, title_zh: str, report_date: str, institution: str = "GS") -> dict:
    return {
        "id": report_id,
        "title": f"English title {report_id}",
        "title_zh": title_zh,
        "date_folder": report_date,
        "bank_code": institution,
        "bank_name": "高盛" if institution == "GS" else "摩根士丹利",
        "industry": "Macro / FX / Rates",
        "page_count": 18,
        "available": True,
        "pdf_archived": False,
        "server_modified": f"{report_date}T08:00:00Z",
    }


def first_json_ld(page: str) -> dict:
    match = re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', page, flags=re.S)
    if not match:
        raise AssertionError("page does not contain JSON-LD")
    return json.loads(match.group(1))


def graph_node(schema: dict, schema_type: str) -> dict:
    for node in schema.get("@graph", []):
        if node.get("@type") == schema_type:
            return node
    raise AssertionError(f"JSON-LD graph does not contain {schema_type}")


def sitemap_lastmods(path: Path) -> dict[str, str]:
    root = ET.parse(path).getroot()
    return {
        str(row.findtext("./{*}loc") or ""): str(row.findtext("./{*}lastmod") or "")
        for row in root.findall("./{*}url")
    }


class SeoOutputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = {
            "updated_at_bjt": "2026-07-17 09:30:00 +0800",
            "items": [
                sample_item("report-a", "全球利率与汇率展望", "2026-07-17"),
                sample_item("report-b", "亚洲宏观策略周报", "2026-07-16"),
                sample_item("report-c", "全球资产配置观察", "2026-07-15", "MS"),
            ],
        }

    def test_generates_engine_specific_discovery_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, self.catalog)

            sitemap_index = ET.parse(output / "sitemap.xml").getroot()
            self.assertTrue(sitemap_index.tag.endswith("sitemapindex"))

            baidu = ET.parse(output / "sitemap-baidu.xml").getroot()
            self.assertTrue(baidu.tag.endswith("urlset"))
            baidu_text = (output / "sitemap-baidu.xml").read_text(encoding="utf-8")
            self.assertIn("https://portal.example.invalid/reports/report-a.html", baidu_text)
            self.assertNotIn("report.html?", baidu_text)
            self.assertNotIn("password=", baidu_text)

            robots = (output / "robots.txt").read_text(encoding="utf-8")
            self.assertIn("User-agent: OAI-SearchBot", robots)
            self.assertIn("User-agent: PerplexityBot", robots)
            self.assertIn("User-agent: ChatGPT-User", robots)
            self.assertIn("User-agent: Claude-SearchBot", robots)
            self.assertIn("User-agent: Claude-User", robots)
            self.assertIn("User-agent: GPTBot\nDisallow: /", robots)
            self.assertIn("User-agent: Google-Extended\nDisallow: /", robots)
            self.assertIn("Sitemap: https://portal.example.invalid/sitemap-baidu.xml", robots)
            self.assertIn("Sitemap: https://portal.example.invalid/sitemap-sogou.xml", robots)
            self.assertNotIn("newsfeed.html", baidu_text)

            key_file = output / f"{builder.INDEXNOW_KEY}.txt"
            self.assertEqual(key_file.read_text(encoding="utf-8").strip(), builder.INDEXNOW_KEY)

            feed = ET.parse(output / "feed.xml").getroot()
            self.assertEqual(len(feed.findall("./channel/item")), 3)
            self.assertTrue((output / "llms-full.txt").exists())

    def test_builds_bernstein_entity_hub_and_lightweight_detail_shards(self) -> None:
        bernstein = sample_item("be-report", "人工智能行业展望", "2026-07-18", "Bernstein")
        bernstein["bank_name"] = "伯恩斯坦"
        catalog = {
            "updated_at_bjt": "2026-07-18 09:30:00 +0800",
            "items": [bernstein, *self.catalog["items"]],
        }
        article = {
            "slug": "bernstein-ai-view",
            "title": "伯恩斯坦人工智能观点",
            "digest": "研究观点摘要",
            "content": "<p>Bernstein Research 行业观察。</p>",
            "date": "2026-07-18",
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, catalog, blog_articles=[article])

            hub = (output / "reports" / "institutions" / "bernstein" / "index.html").read_text(encoding="utf-8")
            self.assertIn("伯恩斯坦研报（Bernstein Research）", hub)
            self.assertIn('rel="canonical" href="https://portal.example.invalid/reports/institutions/bernstein/"', hub)
            self.assertIn("Sanford C. Bernstein", hub)
            self.assertIn("当前共 1 篇", hub)
            self.assertIn("bernstein-ai-view.html", hub)
            collection = graph_node(first_json_ld(hub), "CollectionPage")
            self.assertEqual("Bernstein Research", collection["about"]["name"])

            report = (output / "reports" / "be-report.html").read_text(encoding="utf-8")
            self.assertIn('href="institutions/bernstein/"', report)
            self.assertIn("<title>伯恩斯坦研报：人工智能行业展望 | KC桌面</title>", report)

            shard = json.loads((output / "data" / "report_details" / "be.json").read_text(encoding="utf-8"))
            self.assertEqual("be-report", shard["reports"]["be-report"]["item"]["id"])
            self.assertTrue(shard["reports"]["be-report"]["related"])
            self.assertLessEqual(set(shard["reports"]["be-report"]["item"]), set(builder.PUBLIC_ITEM_KEYS))

            sitemap_pages = (output / "sitemap-pages.xml").read_text(encoding="utf-8")
            self.assertIn("/reports/institutions/bernstein/", sitemap_pages)
            self.assertIn("/reports/institutions/bernstein/", (output / "llms.txt").read_text(encoding="utf-8"))
            self.assertIn("伯恩斯坦研报（Bernstein Research）", (output / "llms-full.txt").read_text(encoding="utf-8"))

    def test_builds_normalized_institution_and_topic_hubs_without_empty_pages(self) -> None:
        for definition in builder.INSTITUTION_HUBS:
            for alias in definition["aliases"]:
                matched = builder.institution_hub_for_values(str(alias))
                self.assertIsNotNone(matched, alias)
                self.assertEqual(definition["slug"], matched["slug"], alias)

        goldman_items = []
        for index in range(105):
            item = sample_item(f"gs-{index:03d}", f"人工智能与半导体 {index:03d}", "2026-07-20", "GS")
            item["bank_name"] = "高盛"
            item["industry"] = "Tech / AI / Semis"
            item["server_modified"] = "2026-07-29T08:00:00Z" if index == 104 else "2026-07-20T08:00:00Z"
            goldman_items.append(item)

        institution_items = []
        for index, definition in enumerate(
            item for item in builder.INSTITUTION_HUBS
            if item["slug"] not in {"goldman-sachs", "hsbc"}
        ):
            item = sample_item(
                f"institution-{index:02d}",
                f"{definition['name_zh']}宏观研究",
                "2026-07-21",
                str(definition["aliases"][-1]),
            )
            item["bank_name"] = definition["name_zh"]
            institution_items.append(item)

        topic_items = []
        for index, definition in enumerate(
            item for item in builder.TOPIC_HUBS
            if item["label"] not in {"Macro / FX / Rates", "Tech / AI / Semis"}
        ):
            item = sample_item(f"topic-{index:02d}", f"{definition['name_zh']}行业展望", "2026-07-22", "MS")
            item["bank_name"] = "摩根士丹利"
            item["industry"] = definition["label"]
            topic_items.append(item)

        unknown = sample_item("unknown-other", "跨学科专题观察", "2026-07-23", "XYZ")
        unknown["bank_name"] = "Arc Research"
        unknown["industry"] = "Other"
        catalog = {
            "updated_at_bjt": "2026-07-30 09:30:00 +0800",
            "items": [*goldman_items, *institution_items, *topic_items, unknown],
        }
        article = {
            "slug": "goldman-ai-view",
            "title": "高盛人工智能行业观察",
            "digest": "Goldman Sachs 对半导体产业链的研究摘要。",
            "content": "<p>AI and semiconductor research.</p>",
            "date": "2026-07-30",
        }

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, catalog, blog_articles=[article])

            goldman_hub = (
                output / "reports" / "institutions" / "goldman-sachs" / "index.html"
            ).read_text(encoding="utf-8")
            self.assertIn("高盛研报（Goldman Sachs）", goldman_hub)
            self.assertIn("当前共 105 篇", goldman_hub)
            self.assertIn("goldman-ai-view.html", goldman_hub)
            self.assertIn('<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">', goldman_hub)
            self.assertIn('<link rel="alternate" hreflang="zh-Hans"', goldman_hub)
            self.assertIn("仅汇总机构字段命中Goldman Sachs及其别名的公开报告", goldman_hub)
            self.assertIn('<link rel="icon" href="/favicon.svg" type="image/svg+xml">', goldman_hub)
            goldman_schema = first_json_ld(goldman_hub)
            self.assertEqual("2026-08-30", graph_node(goldman_schema, "CollectionPage")["dateModified"])
            self.assertEqual(100, graph_node(goldman_schema, "ItemList")["numberOfItems"])
            graph_node(goldman_schema, "BreadcrumbList")

            tech_hub = (
                output / "reports" / "topics" / "tech-ai-semis" / "index.html"
            ).read_text(encoding="utf-8")
            self.assertIn("科技、人工智能与半导体研报（Tech / AI / Semis）", tech_hub)
            self.assertIn("goldman-ai-view.html", tech_hub)
            self.assertIn('<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">', tech_hub)
            self.assertIn('<link rel="alternate" hreflang="x-default"', tech_hub)
            self.assertIn("本页仅索引被归类为 Tech / AI / Semis 的公开报告", tech_hub)
            tech_schema = first_json_ld(tech_hub)
            self.assertEqual(100, graph_node(tech_schema, "ItemList")["numberOfItems"])
            graph_node(tech_schema, "BreadcrumbList")

            known_report = (output / "reports" / "gs-104.html").read_text(encoding="utf-8")
            self.assertIn('href="institutions/goldman-sachs/"', known_report)
            self.assertIn('href="topics/tech-ai-semis/"', known_report)
            unknown_report = (output / "reports" / "unknown-other.html").read_text(encoding="utf-8")
            self.assertIn('href="topics.html#institution-', unknown_report)
            self.assertIn('href="topics.html#topic-', unknown_report)

            navigation = (output / "reports" / "topics.html").read_text(encoding="utf-8")
            self.assertIn('href="institutions/goldman-sachs/"', navigation)
            self.assertIn('href="topics/tech-ai-semis/"', navigation)
            for item in institution_items:
                definition = builder.institution_hub_for_item(item)
                self.assertTrue(
                    (output / "reports" / "institutions" / definition["slug"] / "index.html").is_file(),
                    definition["slug"],
                )
            for item in topic_items:
                definition = builder.topic_hub_for_label(item["industry"])
                self.assertTrue(
                    (output / "reports" / "topics" / definition["slug"] / "index.html").is_file(),
                    definition["slug"],
                )
            self.assertFalse((output / "reports" / "institutions" / "hsbc").exists())
            self.assertFalse((output / "reports" / "topics" / "other").exists())

            sitemap_pages = (output / "sitemap-pages.xml").read_text(encoding="utf-8")
            self.assertIn(
                "<loc>https://portal.example.invalid/reports/institutions/goldman-sachs/</loc>\n"
                "    <lastmod>2026-08-30</lastmod>",
                sitemap_pages,
            )
            self.assertIn("/reports/topics/tech-ai-semis/", sitemap_pages)
            llms = (output / "llms.txt").read_text(encoding="utf-8")
            llms_full = (output / "llms-full.txt").read_text(encoding="utf-8")
            self.assertIn("/reports/institutions/goldman-sachs/", llms)
            self.assertIn("/reports/topics/tech-ai-semis/", llms)
            self.assertIn("高盛研报（Goldman Sachs）", llms_full)
            self.assertIn("科技、人工智能与半导体研报（Tech / AI / Semis）", llms_full)

    def test_indexable_templates_use_favicon_and_policy_sitemap_dates_are_truthful(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, self.catalog)
            generated_pages = [
                output / "reports" / "report-a.html",
                output / "reports" / "index.html",
                output / "reports" / "institutions" / "goldman-sachs" / "index.html",
                output / "reports" / "topics" / "macro-fx-rates" / "index.html",
                output / "reports" / "topics.html",
                output / "about.html",
            ]
            for path in generated_pages:
                self.assertIn(
                    '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
                    path.read_text(encoding="utf-8"),
                    path.as_posix(),
                )

            sitemap_pages = (output / "sitemap-pages.xml").read_text(encoding="utf-8")
            self.assertIn(
                "<loc>https://portal.example.invalid/terms.html</loc>\n"
                "    <lastmod>2026-08-27</lastmod>",
                sitemap_pages,
            )
            self.assertIn(
                "<loc>https://portal.example.invalid/privacy.html</loc>\n"
                "    <lastmod>2026-08-30</lastmod>",
                sitemap_pages,
            )

        article = {
            "slug": "sample-article",
            "title": "中文研究文章",
            "digest": "摘要",
            "content": "<p>正文</p>",
            "date": "2026-07-30",
            "last_date": "2026-07-30",
            "keywords": [],
        }
        blog_index = builder.render_blog_index([article], "https://portal.example.invalid", date(2026, 7, 27))
        blog_article = builder.render_blog_article(article, "https://portal.example.invalid")
        for page in (blog_index, blog_article):
            self.assertIn('<link rel="icon" href="/favicon.svg" type="image/svg+xml">', page)

    def test_canonical_page_lastmods_share_a_stable_template_floor(self) -> None:
        old_report = sample_item("old-report", "高盛全球利率展望", "2026-07-17")
        old_article = {
            "slug": "goldman-ai-old",
            "legacy_slugs": ["goldman-ai-old-legacy"],
            "title": "高盛人工智能行业观察",
            "digest": "研究观点摘要。",
            "content": "<p>Goldman Sachs AI research.</p>",
            "date": "2026-07-30",
            "last_date": "2026-07-30",
            "keywords": [],
        }
        self.assertEqual("2026-07-17", builder.item_lastmod(old_report))
        self.assertEqual("2026-08-30", builder.report_page_lastmod(old_report))
        self.assertEqual("2026-08-30", builder.blog_page_lastmod(old_article))
        self.assertEqual("2026-08-30", builder.hub_page_lastmod([old_report], [old_article]))

        future_report = dict(old_report, server_modified="2026-09-02T08:00:00Z")
        future_article = dict(old_article, last_date="2026-09-03")
        self.assertEqual("2026-09-02", builder.report_page_lastmod(future_report))
        self.assertEqual("2026-09-03", builder.blog_page_lastmod(future_article))
        self.assertEqual("2026-09-03", builder.hub_page_lastmod([future_report], [future_article]))

        report_page = builder.render_report_seo_page(
            old_report,
            "https://portal.example.invalid",
            "2027-01-15",
        )
        report_schema = first_json_ld(report_page)
        self.assertEqual("2026-08-30", graph_node(report_schema, "Report")["dateModified"])
        self.assertEqual("2026-08-30", graph_node(report_schema, "WebPage")["dateModified"])

        blog_page = builder.render_blog_article(old_article, "https://portal.example.invalid")
        blog_schema = first_json_ld(blog_page)
        self.assertEqual("2026-08-30", graph_node(blog_schema, "BlogPosting")["dateModified"])
        self.assertEqual("2026-08-30", graph_node(blog_schema, "WebPage")["dateModified"])

        catalog = {
            "updated_at_bjt": "2027-01-15 09:30:00 +0800",
            "items": [old_report],
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, catalog, blog_articles=[old_article])
            report_url = "https://portal.example.invalid/reports/old-report.html"
            blog_url = "https://portal.example.invalid/blog/goldman-ai-old.html"
            institution_url = "https://portal.example.invalid/reports/institutions/goldman-sachs/"

            report_sitemap = sitemap_lastmods(output / "sitemap-reports-1.xml")
            blog_sitemap = sitemap_lastmods(output / "sitemap-blog-1.xml")
            page_sitemap = sitemap_lastmods(output / "sitemap-pages.xml")
            baidu_sitemap = sitemap_lastmods(output / "sitemap-baidu.xml")
            self.assertEqual("2026-08-30", report_sitemap[report_url])
            self.assertEqual("2026-08-30", blog_sitemap[blog_url])
            self.assertEqual("2026-08-30", page_sitemap[institution_url])
            self.assertEqual("2026-08-30", baidu_sitemap[report_url])
            self.assertEqual("2026-08-30", baidu_sitemap[blog_url])

            hub_schema = first_json_ld(
                (output / "reports" / "institutions" / "goldman-sachs" / "index.html").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual("2026-08-30", graph_node(hub_schema, "CollectionPage")["dateModified"])
            for sitemap in (report_sitemap, blog_sitemap, baidu_sitemap):
                self.assertFalse(any("goldman-ai-old-legacy" in url for url in sitemap))

    def test_blog_articles_link_only_to_controlled_related_hubs(self) -> None:
        goldman_article = {
            "slug": "goldman-ai-view",
            "title": "高盛解读新一轮产业投资",
            "digest": "Goldman Sachs 对资本开支的最新判断。",
            "content": "<p>人工智能、半导体与数据中心仍是重要线索。</p>",
            "date": "2026-07-30",
            "last_date": "2026-07-30",
            "keywords": [],
        }
        goldman_page = builder.render_blog_article(goldman_article, "https://portal.example.invalid")
        self.assertIn(
            '<a href="../reports/institutions/goldman-sachs/">高盛研报（Goldman Sachs）</a>',
            goldman_page,
        )
        self.assertIn(
            '<a href="../reports/topics/tech-ai-semis/">科技、人工智能与半导体研报（Tech / AI / Semis）</a>',
            goldman_page,
        )
        goldman_about = graph_node(first_json_ld(goldman_page), "BlogPosting")["about"]
        self.assertIsInstance(goldman_about, list)
        self.assertEqual(
            {
                "https://portal.example.invalid/reports/institutions/goldman-sachs/#organization",
                "https://portal.example.invalid/reports/topics/tech-ai-semis/#topic",
                "https://portal.example.invalid/reports/topics/industrials-capex/#topic",
            },
            {entity["@id"] for entity in goldman_about},
        )

        short_code_article = {
            "slug": "short-codes-are-not-entities",
            "title": "MS 与 DB 字段迁移记录",
            "digest": "GS 只是样例缩写，不代表机构来源。",
            "content": "<p>排查 MS、DB、GS、JPM 和 UBS 的字段兼容。</p>",
            "date": "2026-07-30",
            "last_date": "2026-07-30",
            "keywords": [],
        }
        short_code_page = builder.render_blog_article(short_code_article, "https://portal.example.invalid")
        self.assertNotIn("../reports/institutions/", short_code_page)
        short_code_schema = graph_node(first_json_ld(short_code_page), "BlogPosting")
        self.assertNotIn("about", short_code_schema)

        bernstein_article = {
            "slug": "bernstein-view",
            "title": "伯恩斯坦专题观察",
            "digest": "研究观点摘要。",
            "content": "<p>Bernstein Research 行业观察。</p>",
            "date": "2026-07-30",
            "last_date": "2026-07-30",
            "keywords": [],
        }
        bernstein_page = builder.render_blog_article(bernstein_article, "https://portal.example.invalid")
        self.assertIn(
            '<a href="../reports/institutions/bernstein/">伯恩斯坦研报（Bernstein Research）</a>',
            bernstein_page,
        )
        self.assertEqual(
            {
                "@type": "Organization",
                "@id": "https://portal.example.invalid/reports/institutions/bernstein/#organization",
                "name": "Bernstein Research",
                "alternateName": ["伯恩斯坦", "Sanford C. Bernstein"],
            },
            graph_node(first_json_ld(bernstein_page), "BlogPosting")["about"],
        )

    def test_homepage_establishes_the_public_editorial_keyword(self) -> None:
        page = (ROOT / "portal_suite" / "site_src" / "index.html").read_text(encoding="utf-8")
        self.assertIn("<title>KC桌面 | 中文金融研报检索与报告索引</title>", page)
        self.assertIn('<meta name="keywords" content="KC桌面,', page)
        self.assertIn('<meta property="og:site_name" content="KC桌面">', page)
        self.assertIn('"name": "KC桌面"', page)

    def test_landing_pages_get_public_entity_and_language_signals(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            shutil.copytree(ROOT / "portal_suite" / "site_src", output, dirs_exist_ok=True)
            builder.build_seo_outputs(output, self.catalog)

            home = (output / "index.html").read_text(encoding="utf-8")
            home_schema = first_json_ld(home)
            website = graph_node(home_schema, "WebSite")
            organization = graph_node(home_schema, "Organization")
            self.assertEqual("zh-Hans", website["inLanguage"])
            self.assertNotIn("alternateName", website)
            self.assertEqual("KC桌面", organization["name"])
            self.assertIn('<html lang="zh-Hans">', home)
            self.assertIn('<span>KC桌面</span>', home)
            self.assertNotIn('<span>Portal Suite</span>', home)
            self.assertIn('href="about.html"', home)

            charts = (output / "charts.html").read_text(encoding="utf-8")
            self.assertIn('<html lang="zh-Hans">', charts)
            self.assertIn('hreflang="zh-Hans"', charts)
            self.assertIn('<meta property="og:site_name" content="KC桌面">', charts)
            self.assertIn('<span>KC桌面</span>', charts)
            self.assertNotIn('<span>Portal Suite</span>', charts)
            self.assertEqual("CollectionPage", graph_node(first_json_ld(charts), "CollectionPage")["@type"])
            graph_node(first_json_ld(charts), "BreadcrumbList")
            self.assertIn('href="about.html"', charts)

            builder.version_assets(output)
            versioned_home = (output / "index.html").read_text(encoding="utf-8")
            self.assertRegex(versioned_home, r'assets/app\.js\?v=[0-9a-f]{8}')
            self.assertRegex(versioned_home, r'assets/report-chat\.js\?v=[0-9a-f]{8}')
            self.assertRegex(versioned_home, r'assets/styles\.css\?v=[0-9a-f]{8}')
            versioned_institution = (
                output / "reports" / "institutions" / "goldman-sachs" / "index.html"
            ).read_text(encoding="utf-8")
            self.assertRegex(versioned_institution, r'\.\./\.\./\.\./assets/styles\.css\?v=[0-9a-f]{8}')
            self.assertRegex(versioned_institution, r'\.\./\.\./\.\./assets/analytics\.js\?v=[0-9a-f]{8}')

    def test_public_contact_alias_is_materialized_after_private_profile_stage(self) -> None:
        public_email = "".join(("info", "@", "kc", "desk", ".com"))
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            shutil.copytree(ROOT / "portal_suite" / "site_src", output, dirs_exist_ok=True)
            builder.build_seo_outputs(output, self.catalog)

            changed = builder.materialize_public_contact(output)

            self.assertGreater(changed, 0)
            index = (output / "index.html").read_text(encoding="utf-8")
            about = (output / "about.html").read_text(encoding="utf-8")
            llms = (output / "llms.txt").read_text(encoding="utf-8")
            self.assertIn(public_email, index)
            self.assertIn(public_email, about)
            self.assertIn(public_email, llms)
            for path in output.rglob("*"):
                if not path.is_file() or path.suffix.lower() not in {".html", ".js", ".json", ".txt", ".xml"}:
                    continue
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                self.assertNotIn(builder.PUBLIC_CONTACT_EMAIL_PLACEHOLDER, text, path.as_posix())

    def test_static_report_has_canonical_schema_and_related_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, self.catalog)
            page = (output / "reports" / "report-a.html").read_text(encoding="utf-8")
            self.assertIn('<html lang="zh-Hans">', page)
            self.assertIn('<link rel="canonical" href="https://portal.example.invalid/reports/report-a.html">', page)
            schema = first_json_ld(page)
            report = graph_node(schema, "Report")
            webpage = graph_node(schema, "WebPage")
            graph_node(schema, "BreadcrumbList")
            self.assertEqual("Goldman Sachs", report["publisher"]["name"])
            self.assertIn("高盛", report["publisher"]["alternateName"])
            self.assertIn("GS", report["publisher"]["alternateName"])
            self.assertEqual("KC桌面", report["sdPublisher"]["name"])
            self.assertEqual("1-18", report["pagination"])
            self.assertNotIn("author", report)
            self.assertNotIn("copyrightHolder", report)
            self.assertNotIn("datePublished", report)
            self.assertEqual("2026-08-30", report["dateModified"])
            self.assertTrue(webpage["isAccessibleForFree"])
            self.assertFalse(report["isAccessibleForFree"])
            self.assertIn(f">{report['abstract']}</p>", page)
            self.assertIn("核心信息（可引用）", page)
            self.assertIn("相关报告", page)
            self.assertIn("不是底层报告的作者或出版方", page)
            self.assertIn("收录日期：2026-07-17", page)
            self.assertNotIn("发布日期", page)
            self.assertNotIn("发布了《", page)
            self.assertIn('../assets/contact.js', page)
            self.assertIn('data-portal-non-chinese-only', page)
            self.assertNotIn("password=", page)

    def test_text_only_static_report_links_to_a_complete_prefilled_home_search(self) -> None:
        long_title = "A" * 90 + "END"
        item = sample_item("text-only-report", long_title, "2026-07-17")
        item["available"] = False
        item["pdf_archived"] = True
        page = builder.render_report_seo_page(
            item,
            "https://portal.example.invalid",
            "2026-07-18",
        )

        self.assertIn('class="text-only-search-guidance"', page)
        self.assertIn("约 90%", page)
        self.assertIn("完整标题", page)
        self.assertIn("“其他报告”等板块", page)
        self.assertIn("在首页搜索同名报告", page)
        self.assertIn(f'href="../?q={long_title}"', page)
        self.assertNotIn(">检索相关报告</a>", page)

        available_page = builder.render_report_seo_page(
            sample_item("available-report", "可下载报告", "2026-07-17"),
            "https://portal.example.invalid",
            "2026-07-18",
        )
        self.assertNotIn('class="text-only-search-guidance"', available_page)
        self.assertIn(">检索相关报告</a>", available_page)

    def test_report_schema_only_uses_explicit_published_at(self) -> None:
        item = sample_item("verified-date", "明确出版日期的报告", "2026-07-17")
        item["published_at"] = "2026-07-12T16:30:00+08:00"
        page = builder.render_report_seo_page(item, "https://portal.example.invalid", "2026-07-18")
        report = graph_node(first_json_ld(page), "Report")
        self.assertEqual("2026-07-12", report["datePublished"])
        self.assertEqual("2026-08-30", report["dateModified"])
        self.assertIn("收录日期：2026-07-17", page)

        item["published_at"] = "2026-99-42"
        invalid_report = graph_node(
            first_json_ld(builder.render_report_seo_page(item, "https://portal.example.invalid", "2026-07-18")),
            "Report",
        )
        self.assertNotIn("datePublished", invalid_report)

    def test_infers_all_browser_industries_from_chinese_titles(self) -> None:
        cases = [
            ("Macro / FX / Rates", "全球宏观与汇率展望"),
            ("Equity Strategy", "中国股票策略与估值展望"),
            ("Tech / AI / Semis", "人工智能与半导体产业链"),
            ("Internet / Media", "互联网媒体与电商趋势"),
            ("Autos / EV / Batteries", "新能源汽车与锂电池"),
            ("Energy / Utilities", "原油与公用事业展望"),
            ("Metals / Mining", "铜与铁矿石供需"),
            ("Healthcare / Biotech", "生物科技与医疗器械"),
            ("Consumer / Retail", "奢侈品零售趋势"),
            ("Banks / Financials", "银行与保险业观察"),
            ("Real Estate", "房地产与住房市场"),
            ("Industrials / Capex", "航空航天与资本开支"),
            ("Policy / Geopolitics", "地缘政治与关税政策"),
            ("ESG / Climate", "气候与碳中和路线图"),
        ]
        inferred_items = []
        for index, (expected, title_zh) in enumerate(cases):
            item = sample_item(f"inferred-{index:02d}", title_zh, "2026-07-17")
            item.pop("industry")
            self.assertEqual(expected, builder.item_industry(item))
            inferred_items.append(item)

        fallback = sample_item("inferred-other", "跨学科专题观察", "2026-07-17")
        fallback.pop("industry")
        self.assertEqual("Other", builder.item_industry(fallback))
        inferred_items.append(fallback)

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(
                output,
                {"updated_at_bjt": "2026-07-17 09:30:00 +0800", "items": inferred_items},
            )
            topic_hub = (output / "reports" / "topics.html").read_text(encoding="utf-8")
            for expected, _ in cases:
                self.assertIn(builder.stable_section_anchor("topic", expected), topic_hub)
            tech_page = (output / "reports" / "inferred-02.html").read_text(encoding="utf-8")
            self.assertIn(">Tech / AI / Semis</a>", tech_page)

    def test_report_collection_is_paginated_with_self_canonicals_and_sitemap_urls(self) -> None:
        catalog = {
            "updated_at_bjt": "2026-07-17 09:30:00 +0800",
            "items": [
                sample_item(f"report-{index:03d}", f"全球研究 {index:03d}", "2026-07-17")
                for index in range(405)
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, catalog)

            pages = [
                (output / "reports" / "index.html").read_text(encoding="utf-8"),
                (output / "reports" / "page-2.html").read_text(encoding="utf-8"),
                (output / "reports" / "page-3.html").read_text(encoding="utf-8"),
            ]
            expected_canonicals = [
                "https://portal.example.invalid/reports/",
                "https://portal.example.invalid/reports/page-2.html",
                "https://portal.example.invalid/reports/page-3.html",
            ]
            expected_counts = [200, 200, 5]
            for page, canonical, expected_count in zip(pages, expected_canonicals, expected_counts):
                self.assertIn(f'<link rel="canonical" href="{canonical}">', page)
                self.assertIn('<link rel="icon" href="/favicon.svg" type="image/svg+xml">', page)
                report_list = re.search(r'<ul class="seo-report-index">(.*?)</ul>', page, flags=re.S)
                self.assertIsNotNone(report_list)
                self.assertEqual(expected_count, report_list.group(1).count("<li>"))
            self.assertIn('href="page-2.html" rel="next"', pages[0])
            self.assertIn('href="./" rel="prev"', pages[1])
            self.assertIn('href="page-3.html" rel="next"', pages[1])
            self.assertIn('href="page-2.html" rel="prev"', pages[2])

            sitemap_pages = (output / "sitemap-pages.xml").read_text(encoding="utf-8")
            for canonical in expected_canonicals:
                self.assertIn(canonical, sitemap_pages)
            topic_hub = (output / "reports" / "topics.html").read_text(encoding="utf-8")
            self.assertIn(builder.stable_section_anchor("institution", "Goldman Sachs · 高盛"), topic_hub)
            self.assertTrue((output / "about.html").is_file())

    def test_report_schema_does_not_invent_an_unknown_publisher(self) -> None:
        item = sample_item("unknown-source", "来源待核验的报告", "2026-07-17")
        item.pop("bank_code")
        item.pop("bank_name")
        page = builder.render_report_seo_page(item, "https://portal.example.invalid", "2026-07-17")
        report = graph_node(first_json_ld(page), "Report")
        self.assertNotIn("publisher", report)
        self.assertEqual([{"@type": "Thing", "name": "Macro / FX / Rates"}], report["about"])

    def test_catalog_preview_is_newest_40_and_uses_only_public_fields(self) -> None:
        items = []
        for index in range(45):
            item = sample_item(f"report-{index:02d}", f"报告 {index:02d}", "2026-07-17")
            item["server_modified"] = f"2026-07-17T08:{index:02d}:00Z"
            item["archive_reason"] = "internal-only"
            items.append(item)
        preview = builder.public_catalog_preview({
            "schema_version": 7,
            "updated_at_bjt": "2026-07-17 09:30:00 +0800",
            "items": items,
            "storage": {"private": True},
        })

        self.assertEqual(1, preview["schema_version"])
        self.assertEqual(40, preview["item_count"])
        self.assertEqual(45, preview["total_item_count"])
        self.assertEqual("report-44", preview["items"][0]["id"])
        self.assertEqual("report-05", preview["items"][-1]["id"])
        self.assertNotIn("storage", preview)
        for item in preview["items"]:
            self.assertLessEqual(set(item), set(builder.PUBLIC_ITEM_KEYS))
            self.assertNotIn("archive_reason", item)

    def test_dynamic_private_pages_are_noindex(self) -> None:
        for name in ("report.html", "doc.html", "delivery.html", "newsfeed.html"):
            page = (ROOT / "portal_suite" / "site_src" / name).read_text(encoding="utf-8")
            self.assertIn('content="noindex,', page)


class IndexNowTests(unittest.TestCase):
    def test_changed_urls_only_include_canonical_public_pages(self) -> None:
        previous = {
            "items": [
                sample_item("report-a", "全球利率与汇率展望", "2026-07-17"),
                sample_item("report-b", "旧标题", "2026-07-16"),
            ]
        }
        current = {
            "updated_at_bjt": "2026-07-17 09:30:00 +0800",
            "items": [
                sample_item("report-a", "全球利率与汇率展望", "2026-07-17"),
                sample_item("report-b", "新标题", "2026-07-16"),
                sample_item("report-c", "新增报告", "2026-07-17"),
            ],
        }
        urls = indexnow.changed_urls(current, previous, "https://portal.example.invalid", 3)
        self.assertIn("https://portal.example.invalid/reports/report-b.html", urls)
        self.assertIn("https://portal.example.invalid/reports/report-c.html", urls)
        self.assertIn("https://portal.example.invalid/reports/institutions/bernstein/", urls)
        self.assertIn("https://portal.example.invalid/blog/", urls)
        self.assertNotIn("https://portal.example.invalid/reports/report-a.html", urls)
        self.assertTrue(all("password=" not in url and "source=" not in url for url in urls))

    def test_public_site_urls_include_blog_articles_and_aggregates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "blog").mkdir()
            (root / "reports").mkdir()
            (root / "blog" / "index.html").write_text("blog", encoding="utf-8")
            (root / "blog" / "page-2.html").write_text("page", encoding="utf-8")
            (root / "blog" / "伯恩斯坦观察.html").write_text("article", encoding="utf-8")
            (root / "reports" / "topics.html").write_text("topics", encoding="utf-8")
            urls = indexnow.discover_public_site_urls(root, "https://portal.example.invalid")
        self.assertIn("https://portal.example.invalid/blog/", urls)
        self.assertIn("https://portal.example.invalid/blog/page-2.html", urls)
        self.assertIn(
            "https://portal.example.invalid/blog/%E4%BC%AF%E6%81%A9%E6%96%AF%E5%9D%A6%E8%A7%82%E5%AF%9F.html",
            urls,
        )
        self.assertIn("https://portal.example.invalid/reports/topics.html", urls)

    def test_previous_catalogs_are_merged_before_diffing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "live.json"
            second = root / "archive.json"
            first.write_text(json.dumps({"items": [sample_item("live", "Live", "2026-07-17")]}), encoding="utf-8")
            second.write_text(json.dumps({"items": [sample_item("archive", "Archive", "2026-07-16")]}), encoding="utf-8")
            merged = indexnow.merge_catalogs([first, second])
        self.assertEqual({"live", "archive"}, set(indexnow.item_map(merged)))

    def test_indexnow_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "catalog.json"
            catalog_path.write_text(json.dumps({"items": []}), encoding="utf-8")
            old_argv = sys.argv
            try:
                sys.argv = ["submit_portal_indexnow.py", "--catalog", str(catalog_path), "--dry-run"]
                self.assertEqual(indexnow.main(), 0)
            finally:
                sys.argv = old_argv


if __name__ == "__main__":
    unittest.main()
