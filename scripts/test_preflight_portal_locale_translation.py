#!/usr/bin/env python3
"""All public fetches and provider calls in these tests are mocked."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import preflight_portal_locale_translation as preflight


ORIGIN = "https://portal.example.invalid"


def metadata(label: str, extra: str = "") -> bytes:
    return (
        f'<html><head><title>{label}金融研究中心</title>'
        f'<meta name="description" content="{label}的全球宏观经济研究与行业观察">'
        f'<meta property="og:title" content="{label}公开市场研究索引">'
        f'<meta property="og:description" content="{label}投资研究公开摘要">'
        f'</head><body><h1>{label}金融研究导航</h1>'
        f'<p>ARTICLE_BODY_MUST_NOT_BE_TRANSLATED</p>{extra}</body></html>'
    ).encode("utf-8")


def fixture_fetcher() -> Mock:
    routes = {
        ORIGIN + "/": metadata("首页"),
        ORIGIN + "/blog/": metadata("专栏", '<a href="page-2.html">Older</a><a href="newest.html">最新文章</a><a href="older.html">旧文章</a>'),
        ORIGIN + "/blog/newest.html": metadata("最新文章"),
        ORIGIN + "/data/catalog_preview.json": json.dumps({"items": [
            {"id": f"report-{index}", "title": f"宏观经济研究报告第{index}期", "bank_name": "研究机构",
             "industry": "金融行业", "sector": "经济发展", "category": "宏观策略",
             "content": "CATALOG_BODY_MUST_NOT_BE_TRANSLATED", "pdf_url": ORIGIN + "/private.pdf"}
            for index in range(4)
        ]}, ensure_ascii=False).encode("utf-8"),
    }
    return Mock(side_effect=lambda url: routes[url])


class PreflightTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.report_path = Path(self.temporary.name) / "diagnostics.json"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_collects_four_public_metadata_sources_without_bodies_or_pdf(self) -> None:
        fetcher = fixture_fetcher()
        units, sampling = preflight.collect_samples(ORIGIN, fetcher)
        self.assertEqual(fetcher.call_count, 4)
        self.assertEqual(set(sampling["source_counts"]), {"home", "blog", "latest-blog", "catalog-preview"})
        self.assertLessEqual(len(units), 16)
        self.assertGreater(len(units), 8)
        self.assertTrue(any(unit.context.startswith("html:") for unit in units.values()))
        self.assertTrue(any(unit.context.startswith("catalog:") for unit in units.values()))
        self.assertTrue(all(len(unit.source) <= 600 for unit in units.values()))
        self.assertNotIn("MUST_NOT_BE_TRANSLATED", repr(units))
        self.assertNotIn(".pdf", repr(fetcher.call_args_list))

    def test_passes_fixed_paid_limits_and_uses_only_a_temporary_cache(self) -> None:
        calls = []

        def translate(units, cache, **kwargs):
            calls.append(kwargs)
            self.assertEqual(kwargs["workers"], 1)
            self.assertEqual(kwargs["attempts"], 1)
            self.assertEqual(kwargs["max_provider_requests"], 6)
            self.assertTrue(kwargs["preflight_only"])
            self.assertEqual(kwargs["preflight_batches_per_locale"], 2)
            self.assertEqual(kwargs["max_batch_items"], 8)
            self.assertTrue(all(not cache["locales"][locale] for locale in preflight.builder.LOCALES))
            kwargs["cache_path"].write_bytes(b"temporary checkpoint")
            kwargs["diagnostics_out"].write_text(json.dumps({
                "status": "passed", "provider_requests": 6,
                "usage_totals": {"total_tokens": 1200}, "usage_unknown_responses": 0,
            }), encoding="utf-8")
            return {locale: len(units) for locale in preflight.builder.LOCALES}

        with patch.object(preflight.builder, "translate_missing_units", side_effect=translate):
            report = preflight.run_preflight(site_url=ORIGIN, diagnostics_out=self.report_path, fetcher=fixture_fetcher())
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["usage_totals"]["total_tokens"], 1200)
        self.assertFalse(calls[0]["cache_path"].exists())
        self.assertEqual(len(calls), 1)

    def test_bounded_sample_includes_english_terms_at_end_of_mixed_keyword_list(self) -> None:
        base = fixture_fetcher()
        keywords = "金融研报,宏观策略,行业研究,公司研究,股票研究,国际智库,市场观察,全球经济,投资研究,Chinese financial research,investment bank research"

        def fetch(url: str) -> bytes:
            if url == ORIGIN + "/":
                return metadata("首页", f'<meta name="keywords" content="{keywords}">')
            return base(url)

        units, _sampling = preflight.collect_samples(ORIGIN, fetch)
        selected = {unit.source for unit in units.values() if unit.context == "html:meta:keyword"}
        self.assertTrue({"Chinese financial research", "investment bank research"}.issubset(selected))
        self.assertLessEqual(len(units), 16)

    def test_failed_provider_response_records_usage_and_stops_after_one_request(self) -> None:
        response = Mock(status_code=402)
        response.json.return_value = {
            "error": {"message": "declined"},
            "usage": {"prompt_tokens": 7, "completion_tokens": 0, "total_tokens": 7},
        }
        secret = "FAKE_PROVIDER_CREDENTIAL_MUST_NOT_APPEAR"
        response.headers = {"Authorization": secret}
        provider = Mock(return_value=response)
        with patch.dict("os.environ", {"DEEPSEEK_API_KEY": secret}), patch.dict(
            sys.modules, {"deepseek_http": SimpleNamespace(request_with_key_fallback=provider)},
        ):
            with self.assertRaisesRegex(preflight.PreflightError, "HTTP 402"):
                preflight.run_preflight(site_url=ORIGIN, diagnostics_out=self.report_path, fetcher=fixture_fetcher())
        report = json.loads(self.report_path.read_text(encoding="utf-8"))
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(report["provider_requests"], 1)
        self.assertEqual(report["usage_totals"]["total_tokens"], 7)
        self.assertEqual(report["status"], "failed")
        self.assertNotIn(secret, self.report_path.read_text(encoding="utf-8"))
        self.assertNotIn("Authorization", self.report_path.read_text(encoding="utf-8"))

    def test_source_failure_writes_diagnostics_before_any_provider_call(self) -> None:
        with patch.object(preflight.builder, "translate_missing_units") as translate:
            with self.assertRaisesRegex(preflight.PreflightError, "no same-origin article"):
                preflight.run_preflight(site_url=ORIGIN, diagnostics_out=self.report_path,
                                        fetcher=lambda _url: metadata("索引"))
        translate.assert_not_called()
        report = json.loads(self.report_path.read_text(encoding="utf-8"))
        self.assertEqual(report["provider_requests"], 0)
        self.assertEqual(report["status"], "failed")

    def test_article_selection_rejects_external_links_and_pagination(self) -> None:
        parser = preflight.MetadataParser()
        parser.feed('<a href="https://outside.example/article.html">外部</a>'
                    '<a href="page-2.html">下一页</a><a href="index.html">目录</a>'
                    '<a href="/files/report.pdf">下载</a><a href="newest.html">最新</a>')
        self.assertEqual(preflight.latest_blog_url(parser, ORIGIN), ORIGIN + "/blog/newest.html")

    def test_origin_rejects_credentials_non_https_and_paths(self) -> None:
        for origin in ("http://portal.example.invalid", "https://user:pass@portal.example.invalid",
                       ORIGIN + "/blog/", ORIGIN + "?query=1"):
            with self.subTest(origin=origin), self.assertRaises(preflight.PreflightError):
                preflight.normalize_origin(origin)

    def test_public_http_request_cannot_follow_redirect_or_attach_auth(self) -> None:
        response = Mock(status_code=200)
        response.iter_content.return_value = [b"public metadata"]
        context = Mock()
        context.__enter__ = Mock(return_value=response)
        context.__exit__ = Mock(return_value=False)
        get = Mock(return_value=context)
        with patch.dict(sys.modules, {"requests": SimpleNamespace(get=get, RequestException=RuntimeError)}):
            self.assertEqual(preflight.fetch_public(ORIGIN + "/"), b"public metadata")
        self.assertEqual(get.call_args.kwargs, {"timeout": (10, 30), "allow_redirects": False, "stream": True})


if __name__ == "__main__":
    unittest.main(verbosity=2)
