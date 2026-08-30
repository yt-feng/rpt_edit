#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_portal_seo_live as seo_health  # noqa: E402


SITE = "https://portal.example.invalid"
KEY = "abc12345"


def result(
    status: int,
    url: str,
    body: str | bytes = "",
    *,
    content_type: str = "text/plain; charset=utf-8",
    headers: dict[str, str] | None = None,
) -> seo_health.FetchResult:
    payload = body.encode("utf-8") if isinstance(body, str) else body
    merged_headers = {"content-type": content_type}
    merged_headers.update({str(key).lower(): value for key, value in (headers or {}).items()})
    return seo_health.FetchResult(status, url, merged_headers, payload)


def urlset(*urls: str) -> str:
    rows = "".join(f"<url><loc>{url}</loc></url>" for url in urls)
    return f'<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</urlset>'


def sitemap_index(*urls: str) -> str:
    rows = "".join(f"<sitemap><loc>{url}</loc></sitemap>" for url in urls)
    return f'<?xml version="1.0"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</sitemapindex>'


def page(url: str, *, robots: str = "index,follow", canonical: str | None = None, schema: bool = True) -> str:
    canonical_url = url if canonical is None else canonical
    schema_markup = (
        '<script type="application/ld+json">'
        + json.dumps({"@context": "https://schema.org", "@type": "WebPage", "url": url})
        + "</script>"
        if schema
        else ""
    )
    icon = '<link rel="icon" href="/favicon.svg">' if url == SITE + "/" else ""
    return (
        "<!doctype html><html><head>"
        f'<meta name="robots" content="{robots}">'
        f'<link rel="canonical" href="{canonical_url}">'
        f"{icon}{schema_markup}</head><body>ok</body></html>"
    )


class FakeFetcher:
    def __init__(self, routes: dict[str, seo_health.FetchResult | Exception]) -> None:
        self.routes = routes
        self.calls: list[tuple[str, bool]] = []

    def __call__(self, url: str, *, follow_redirects: bool = True) -> seo_health.FetchResult:
        self.calls.append((url, follow_redirects))
        value = self.routes.get(url)
        if value is None:
            return result(404, url, "not found")
        if isinstance(value, Exception):
            raise value
        return value


def healthy_routes() -> dict[str, seo_health.FetchResult]:
    pages_sitemap = SITE + "/sitemap-pages.xml"
    reports_sitemap = SITE + "/sitemap-reports-1.xml"
    home = SITE + "/"
    about = SITE + "/about.html"
    report_url = SITE + "/reports/report-a.html"
    return {
        SITE + "/robots.txt": result(
            200,
            SITE + "/robots.txt",
            "User-agent: *\nAllow: /\nSitemap: https://portal.example.invalid/sitemap.xml\n",
        ),
        SITE + "/sitemap.xml": result(
            200,
            SITE + "/sitemap.xml",
            sitemap_index(pages_sitemap, reports_sitemap),
            content_type="application/xml",
        ),
        pages_sitemap: result(200, pages_sitemap, urlset(home, about), content_type="application/xml"),
        reports_sitemap: result(200, reports_sitemap, urlset(report_url), content_type="application/xml"),
        home: result(200, home, page(home), content_type="text/html"),
        about: result(200, about, page(about), content_type="text/html"),
        report_url: result(200, report_url, page(report_url), content_type="text/html"),
        SITE + f"/{KEY}.txt": result(200, SITE + f"/{KEY}.txt", KEY + "\n"),
        SITE + "/favicon.svg": result(
            200,
            SITE + "/favicon.svg",
            "<svg xmlns='http://www.w3.org/2000/svg'></svg>",
            content_type="image/svg+xml",
        ),
        "https://www.portal.example.invalid/": result(
            301,
            "https://www.portal.example.invalid/",
            headers={"Location": SITE + "/"},
        ),
    }


class LiveSeoAuditTests(unittest.TestCase):
    def test_healthy_site_passes_with_aggregate_metrics(self) -> None:
        fetcher = FakeFetcher(healthy_routes())

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=fetcher)

        self.assertTrue(report["ok"])
        self.assertEqual(2, report["metrics"]["sitemap"]["declared_shards"])
        self.assertEqual(3, report["metrics"]["sitemap"]["total_urls"])
        self.assertEqual(3, report["metrics"]["samples"]["self_canonical"])
        self.assertTrue(report["metrics"]["indexnow"]["key_file_verified"])
        self.assertTrue(report["metrics"]["favicon"]["verified"])
        self.assertEqual(301, report["metrics"]["www_alias"]["status"])
        self.assertFalse(report["site"]["production_identity_included"])
        self.assertNotIn("portal.example.invalid", json.dumps(report))
        self.assertIn(("https://www.portal.example.invalid/", False), fetcher.calls)
        self.assertNotIn((SITE + "/favicon.ico", True), fetcher.calls)

    def test_failures_are_classified_without_following_alias(self) -> None:
        routes = healthy_routes()
        bad_page = SITE + "/reports/report-a.html"
        routes[bad_page] = result(
            200,
            bad_page,
            page(bad_page, robots="noindex", canonical=SITE + "/wrong.html", schema=False),
            content_type="text/html",
        )
        routes[SITE + f"/{KEY}.txt"] = result(200, SITE + f"/{KEY}.txt", "wrong")
        routes[SITE + "/favicon.svg"] = result(200, SITE + "/favicon.svg", "not an image")
        routes["https://www.portal.example.invalid/"] = result(200, "https://www.portal.example.invalid/")
        fetcher = FakeFetcher(routes)

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=fetcher)

        self.assertFalse(report["ok"])
        categories = {failure["category"] for failure in report["failures"]}
        self.assertTrue({"noindex", "canonical", "structured_data", "indexnow", "favicon", "alias"} <= categories)
        codes = {failure["code"] for failure in report["failures"]}
        self.assertIn("not_permanent_redirect", codes)
        self.assertIn(("https://www.portal.example.invalid/", False), fetcher.calls)

    def test_transport_and_malformed_sitemap_are_visible(self) -> None:
        routes = healthy_routes()
        routes[SITE + "/robots.txt"] = OSError("offline")
        routes[SITE + "/sitemap.xml"] = result(
            200,
            SITE + "/sitemap.xml",
            "<sitemapindex>",
            content_type="application/xml",
        )

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=3, fetcher=FakeFetcher(routes))

        self.assertFalse(report["ok"])
        self.assertEqual(1, report["failure_counts"]["transport"])
        self.assertEqual("root_invalid_xml", next(item["code"] for item in report["failures"] if item["category"] == "sitemap"))
        self.assertNotIn("offline", json.dumps(report))

    def test_off_origin_sitemap_url_is_reported_but_never_fetched(self) -> None:
        routes = healthy_routes()
        report_sitemap = SITE + "/sitemap-reports-1.xml"
        external = "https://other.example/report.html"
        routes[report_sitemap] = result(
            200,
            report_sitemap,
            urlset(external),
            content_type="application/xml",
        )
        fetcher = FakeFetcher(routes)

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=fetcher)

        self.assertFalse(report["ok"])
        self.assertIn("off_origin_url", {item["code"] for item in report["failures"]})
        self.assertFalse(any(url == external for url, _follow in fetcher.calls))

    def test_cli_writes_failure_json_and_markdown_for_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "health.json"
            markdown = Path(directory) / "health.md"

            exit_code = seo_health.main(
                [
                    "--site-url",
                    "http://portal.example.invalid/path",
                    "--output",
                    str(output),
                    "--markdown-output",
                    str(markdown),
                ]
            )

            self.assertEqual(1, exit_code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("input", payload["failures"][0]["category"])
            self.assertIn("未通过", markdown.read_text(encoding="utf-8"))

    def test_site_url_validation_rejects_www_and_query(self) -> None:
        for value in (
            "https://www.portal.example.invalid",
            "https://portal.example.invalid/?preview=1",
            "http://portal.example.invalid",
        ):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    seo_health.normalize_site_url(value)


if __name__ == "__main__":
    unittest.main()
