#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_kc_desk_notes_site as builder  # noqa: E402
import submit_kcdesk_indexnow as indexnow  # noqa: E402


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
            self.assertIn("https://kcdesk.com/reports/report-a.html", baidu_text)
            self.assertNotIn("report.html?", baidu_text)
            self.assertNotIn("password=", baidu_text)

            robots = (output / "robots.txt").read_text(encoding="utf-8")
            self.assertIn("User-agent: OAI-SearchBot", robots)
            self.assertIn("User-agent: PerplexityBot", robots)
            self.assertIn("Sitemap: https://kcdesk.com/sitemap-baidu.xml", robots)
            self.assertIn("Sitemap: https://kcdesk.com/sitemap-sogou.xml", robots)
            self.assertNotIn("newsfeed.html", baidu_text)

            key_file = output / f"{builder.INDEXNOW_KEY}.txt"
            self.assertEqual(key_file.read_text(encoding="utf-8").strip(), builder.INDEXNOW_KEY)

            feed = ET.parse(output / "feed.xml").getroot()
            self.assertEqual(len(feed.findall("./channel/item")), 3)
            self.assertTrue((output / "llms-full.txt").exists())

    def test_static_report_has_canonical_schema_and_related_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            builder.build_seo_outputs(output, self.catalog)
            page = (output / "reports" / "report-a.html").read_text(encoding="utf-8")
            self.assertIn('<html lang="zh-CN">', page)
            self.assertIn('<link rel="canonical" href="https://kcdesk.com/reports/report-a.html">', page)
            self.assertIn('"@type":"Report"', page)
            self.assertIn('"@type":"BreadcrumbList"', page)
            self.assertIn("研究摘要", page)
            self.assertIn("相关报告", page)
            self.assertNotIn("password=", page)

    def test_dynamic_private_pages_are_noindex(self) -> None:
        for name in ("report.html", "doc.html", "delivery.html", "newsfeed.html"):
            page = (ROOT / "kc_desk_notes" / "site_src" / name).read_text(encoding="utf-8")
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
        urls = indexnow.changed_urls(current, previous, "https://kcdesk.com", 3)
        self.assertIn("https://kcdesk.com/reports/report-b.html", urls)
        self.assertIn("https://kcdesk.com/reports/report-c.html", urls)
        self.assertNotIn("https://kcdesk.com/reports/report-a.html", urls)
        self.assertTrue(all("password=" not in url and "source=" not in url for url in urls))

    def test_indexnow_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "catalog.json"
            catalog_path.write_text(json.dumps({"items": []}), encoding="utf-8")
            old_argv = sys.argv
            try:
                sys.argv = ["submit_kcdesk_indexnow.py", "--catalog", str(catalog_path), "--dry-run"]
                self.assertEqual(indexnow.main(), 0)
            finally:
                sys.argv = old_argv


if __name__ == "__main__":
    unittest.main()
