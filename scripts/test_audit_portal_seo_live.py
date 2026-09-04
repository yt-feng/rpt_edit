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


def locale_page(
    url: str,
    *,
    language: str,
    direction: str | None = None,
    canonical: str | None = None,
    in_language: str | None = None,
    omitted_hreflangs: set[str] | None = None,
    hreflang_overrides: dict[str, str] | None = None,
) -> str:
    canonical_url = url if canonical is None else canonical
    omitted = {value.lower() for value in (omitted_hreflangs or set())}
    targets = {
        "zh-Hans": SITE + "/",
        "ko": SITE + "/ko/",
        "ja": SITE + "/ja/",
        "ar": SITE + "/ar/",
        "x-default": SITE + "/",
    }
    targets.update(hreflang_overrides or {})
    alternates = "".join(
        f'<link rel="alternate" hreflang="{code}" href="{target}">'
        for code, target in targets.items()
        if code.lower() not in omitted
    )
    schema_markup = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "url": url,
            "inLanguage": language if in_language is None else in_language,
        }
    )
    icon = '<link rel="icon" href="/favicon.svg">' if url == SITE + "/" else ""
    direction_attr = f' dir="{direction}"' if direction else ""
    return (
        f'<!doctype html><html lang="{language}"{direction_attr}><head>'
        '<meta name="robots" content="index,follow">'
        f'<link rel="canonical" href="{canonical_url}">'
        f'{alternates}{icon}<script type="application/ld+json">{schema_markup}</script>'
        "</head><body>ok</body></html>"
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


def healthy_locale_routes() -> dict[str, seo_health.FetchResult]:
    routes = healthy_routes()
    pages_sitemap = SITE + "/sitemap-pages.xml"
    reports_sitemap = SITE + "/sitemap-reports-1.xml"
    locale_sitemaps = [SITE + f"/sitemap-{locale}.xml" for locale in ("ko", "ja", "ar")]
    routes[SITE + "/sitemap.xml"] = result(
        200,
        SITE + "/sitemap.xml",
        sitemap_index(pages_sitemap, reports_sitemap, *locale_sitemaps),
        content_type="application/xml",
    )
    routes[SITE + "/"] = result(
        200,
        SITE + "/",
        locale_page(SITE + "/", language="zh-Hans"),
        content_type="text/html",
    )
    for locale in ("ko", "ja", "ar"):
        locale_home = SITE + f"/{locale}/"
        locale_sitemap = SITE + f"/sitemap-{locale}.xml"
        routes[locale_sitemap] = result(
            200,
            locale_sitemap,
            urlset(locale_home),
            content_type="application/xml",
        )
        routes[locale_home] = result(
            200,
            locale_home,
            locale_page(
                locale_home,
                language=locale,
                direction="rtl" if locale == "ar" else "ltr",
            ),
            content_type="text/html",
        )
    return routes


def cloudflare_managed_robots(*, search: str = "yes", wildcard_rule: str = "Allow: /") -> str:
    return (
        "# BEGIN Cloudflare Managed content\n\n"
        "User-agent: *\n"
        f"Content-Signal: search={search},ai-train=no,use=reference\n"
        f"{wildcard_rule}\n\n"
        "User-agent: GPTBot\n"
        "Disallow: /\n\n"
        "# END Cloudflare Managed Content\n"
    )


class LiveSeoAuditTests(unittest.TestCase):
    def test_default_indexnow_key_is_the_public_deployment_proof(self) -> None:
        self.assertEqual("b7c3e9a41d8f52e604a71bc93f2d6e80", seo_health.DEFAULT_INDEXNOW_KEY)
        workflow = (
            Path(__file__).resolve().parents[1] / ".github/workflows/portal-seo-health.yml"
        ).read_text(encoding="utf-8")
        self.assertNotIn("secrets.PORTAL_INDEXNOW_KEY", workflow)
        self.assertNotIn('--indexnow-key "$PORTAL_INDEXNOW_KEY"', workflow)

    def test_healthy_site_passes_with_aggregate_metrics(self) -> None:
        fetcher = FakeFetcher(healthy_routes())

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=fetcher)

        self.assertTrue(report["ok"])
        self.assertEqual(2, report["metrics"]["sitemap"]["declared_shards"])
        self.assertEqual(3, report["metrics"]["sitemap"]["total_urls"])
        self.assertEqual(3, report["metrics"]["samples"]["self_canonical"])
        self.assertEqual(
            {
                "enabled": False,
                "declared_sitemaps": [],
                "requested": 0,
                "http_200": 0,
                "html_lang": 0,
                "arabic_rtl": 0,
                "self_canonical": 0,
                "reciprocal_hreflang": 0,
                "json_ld_in_language": 0,
            },
            report["metrics"]["locales"],
        )
        self.assertTrue(report["metrics"]["indexnow"]["key_file_verified"])
        self.assertTrue(report["metrics"]["favicon"]["verified"])
        self.assertEqual(301, report["metrics"]["www_alias"]["status"])
        self.assertFalse(report["site"]["production_identity_included"])
        self.assertNotIn("portal.example.invalid", json.dumps(report))
        self.assertIn(("https://www.portal.example.invalid/", False), fetcher.calls)
        self.assertNotIn((SITE + "/favicon.ico", True), fetcher.calls)
        for locale in ("ko", "ja", "ar"):
            self.assertNotIn((SITE + f"/{locale}/", True), fetcher.calls)
        self.assertNotIn("多语言 SEO", seo_health.render_markdown(report))

    def test_declared_locale_sitemaps_enable_reciprocal_locale_audit(self) -> None:
        fetcher = FakeFetcher(healthy_locale_routes())

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=fetcher)

        self.assertTrue(report["ok"])
        self.assertTrue(report["checks"]["locales"]["ok"])
        self.assertEqual(5, report["metrics"]["sitemap"]["declared_shards"])
        self.assertEqual(
            {
                "enabled": True,
                "declared_sitemaps": ["ko", "ja", "ar"],
                "requested": 3,
                "http_200": 3,
                "html_lang": 3,
                "arabic_rtl": 1,
                "self_canonical": 3,
                "reciprocal_hreflang": 4,
                "json_ld_in_language": 3,
            },
            report["metrics"]["locales"],
        )
        for locale in ("ko", "ja", "ar"):
            self.assertIn((SITE + f"/{locale}/", True), fetcher.calls)
        self.assertIn("多语言 SEO", seo_health.render_markdown(report))

    def test_locale_sitemaps_must_be_declared_all_or_none(self) -> None:
        routes = healthy_locale_routes()
        pages_sitemap = SITE + "/sitemap-pages.xml"
        reports_sitemap = SITE + "/sitemap-reports-1.xml"
        routes[SITE + "/sitemap.xml"] = result(
            200,
            SITE + "/sitemap.xml",
            sitemap_index(pages_sitemap, reports_sitemap, SITE + "/sitemap-ko.xml"),
            content_type="application/xml",
        )
        fetcher = FakeFetcher(routes)

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=fetcher)

        self.assertFalse(report["ok"])
        self.assertFalse(report["checks"]["locales"]["ok"])
        self.assertFalse(report["metrics"]["locales"]["enabled"])
        self.assertEqual(["ko"], report["metrics"]["locales"]["declared_sitemaps"])
        self.assertEqual(0, report["metrics"]["locales"]["requested"])
        failures = [item for item in report["failures"] if item["category"] == "locale"]
        self.assertEqual(["sitemap_set_incomplete"], [item["code"] for item in failures])
        self.assertIn("missing ja, ar", failures[0]["message"])

    def test_enabled_locale_contract_failures_are_classified(self) -> None:
        routes = healthy_locale_routes()
        ko_url = SITE + "/ko/"
        ja_url = SITE + "/ja/"
        ar_url = SITE + "/ar/"
        routes[ko_url] = result(503, ko_url, "unavailable", content_type="text/html")
        routes[ja_url] = result(
            200,
            ja_url,
            locale_page(
                ja_url,
                language="ko",
                direction="ltr",
                canonical=SITE + "/wrong.html",
                in_language="ko",
                omitted_hreflangs={"x-default"},
            ),
            content_type="text/html",
        )
        routes[ar_url] = result(
            200,
            ar_url,
            locale_page(ar_url, language="ar", direction="ltr"),
            content_type="text/html",
        )

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=FakeFetcher(routes))

        self.assertFalse(report["ok"])
        self.assertFalse(report["checks"]["locales"]["ok"])
        codes = {item["code"] for item in report["failures"] if item["category"] == "locale"}
        self.assertTrue(
            {
                "http_status",
                "html_lang_mismatch",
                "arabic_not_rtl",
                "canonical_not_self",
                "json_ld_in_language_missing",
                "hreflang_count",
            }
            <= codes
        )

    def test_cloudflare_managed_search_yes_without_sitemap_is_warning_only(self) -> None:
        routes = healthy_routes()
        routes[SITE + "/robots.txt"] = result(200, SITE + "/robots.txt", cloudflare_managed_robots())

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=FakeFetcher(routes))

        self.assertTrue(report["ok"])
        self.assertTrue(report["checks"]["robots"]["ok"])
        self.assertEqual(2, report["metrics"]["sitemap"]["validated_shards"])
        self.assertEqual(
            {
                "http_ok": True,
                "advertised_discovery_files": 0,
                "managed_by_cloudflare": True,
                "search_content_signal": "yes",
                "canonical_sitemap_advertised": False,
                "managed_sitemap_warning": True,
            },
            report["metrics"]["robots"],
        )
        self.assertEqual(["managed_sitemap_not_advertised"], [item["code"] for item in report["warnings"]])
        self.assertNotIn("sitemap_missing", {item["code"] for item in report["failures"]})

    def test_cloudflare_managed_search_no_fails_even_when_sitemap_is_healthy(self) -> None:
        routes = healthy_routes()
        routes[SITE + "/robots.txt"] = result(
            200,
            SITE + "/robots.txt",
            cloudflare_managed_robots(search="no") + f"Sitemap: {SITE}/sitemap.xml\n",
        )

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=FakeFetcher(routes))

        self.assertFalse(report["ok"])
        self.assertIn("managed_search_disabled", {item["code"] for item in report["failures"]})
        self.assertEqual(2, report["metrics"]["sitemap"]["validated_shards"])

    def test_cloudflare_managed_wildcard_root_block_still_fails(self) -> None:
        routes = healthy_routes()
        routes[SITE + "/robots.txt"] = result(
            200,
            SITE + "/robots.txt",
            cloudflare_managed_robots(wildcard_rule="Disallow: /") + f"Sitemap: {SITE}/sitemap.xml\n",
        )

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=FakeFetcher(routes))

        self.assertFalse(report["ok"])
        self.assertIn("wildcard_root_blocked", {item["code"] for item in report["failures"]})

    def test_self_managed_robots_without_sitemap_still_fails(self) -> None:
        routes = healthy_routes()
        routes[SITE + "/robots.txt"] = result(200, SITE + "/robots.txt", "User-agent: *\nAllow: /\n")

        report = seo_health.audit_site(SITE, indexnow_key=KEY, sample_size=10, fetcher=FakeFetcher(routes))

        self.assertFalse(report["ok"])
        self.assertFalse(report["metrics"]["robots"]["managed_by_cloudflare"])
        self.assertTrue(
            {"sitemap_missing", "canonical_sitemap_missing"}
            <= {item["code"] for item in report["failures"]}
        )

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
