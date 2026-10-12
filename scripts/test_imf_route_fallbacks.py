"""Missing DOI registration and official IEO receipts keep distinct evidence."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, Mock, patch

import fetch_institution_latest_pdfs as fetcher
import imf_elibrary_resolver as resolver
import institution_source_health as health
import test_imf_ieo_followup as ieo_fixture
from test_imf_ieo_followup import IDENTITY
from test_institution_source_health import manifest, source_check


class RouteFallbackTests(unittest.TestCase):
    def test_ieo_uses_isolated_https_and_only_one_cloud_retry_for_real_403(self):
        import imf_ieo_followup as followup
        item = {"title": IDENTITY.title, "source_url": IDENTITY.source_url}
        for status, enabled in ((200, True), (403, True), (403, False), (404, True), (429, True), (500, True), (None, True)):
            direct = MagicMock(); direct.__enter__.return_value = direct
            cloud = MagicMock(); cloud.__enter__.return_value = cloud
            browser = Mock(enabled=enabled); browser.http_session.return_value = cloud
            category = "ieo_followup_request_failed" if status is None else "ieo_followup_http_rejected"
            outcome = {"verified": "receipt"}
            effects = [outcome] if status == 200 else [followup.FollowupError(category, http_status=status), outcome]
            with (self.subTest(status=status, enabled=enabled),
                  patch.object(fetcher, "collect_coveo_preview_html", return_value="fresh preview"),
                  patch.object(resolver, "bind_source", return_value=IDENTITY),
                  patch.object(fetcher.requests, "Session", return_value=direct) as factory,
                  patch.object(followup, "download_followup", side_effect=effects) as download):
                if status == 200 or (status == 403 and enabled):
                    self.assertEqual(fetcher.resolve_imf_ieo_followup({}, Mock(), item, Path("unused.pdf"),
                                                                     100, 1000000, imf_browser=browser), outcome)
                else:
                    with self.assertRaises(followup.FollowupError):
                        fetcher.resolve_imf_ieo_followup({}, Mock(), item, Path("unused.pdf"),
                                                        100, 1000000, imf_browser=browser)
                factory.assert_called_once_with()
                self.assertIs(direct.trust_env, False)
                direct.__exit__.assert_called_once()
                self.assertIs(download.call_args_list[0].args[1], direct)
                self.assertEqual(browser.http_session.call_count, int(status == 403 and enabled))
                self.assertEqual(download.call_count, 1 + int(status == 403 and enabled))
                if status == 403 and enabled:
                    self.assertIs(download.call_args_list[1].args[1], cloud)
                    self.assertEqual(download.call_args_list[0].args[0], download.call_args_list[1].args[0])
                    cloud.__exit__.assert_called_once()

    def test_ieo_second_rejection_stops_without_third_attempt(self):
        import imf_ieo_followup as followup
        item = {"title": IDENTITY.title, "source_url": IDENTITY.source_url}
        direct = MagicMock(); direct.__enter__.return_value = direct
        cloud = MagicMock(); cloud.__enter__.return_value = cloud
        browser = Mock(enabled=True); browser.http_session.return_value = cloud
        with (patch.object(fetcher, "collect_coveo_preview_html", return_value="fresh preview"),
              patch.object(resolver, "bind_source", return_value=IDENTITY),
              patch.object(fetcher.requests, "Session", return_value=direct),
              patch.object(followup, "download_followup", side_effect=followup.FollowupError(
                  "ieo_followup_http_rejected", http_status=403)) as download):
            with self.assertRaises(followup.FollowupError):
                fetcher.resolve_imf_ieo_followup({}, Mock(), item, Path("unused.pdf"), 60, 1000000, imf_browser=browser)
        self.assertEqual(download.call_count, 2)
        browser.http_session.assert_called_once()
        direct.__exit__.assert_called_once()
        cloud.__exit__.assert_called_once()

    def test_crossref_stream_limits_close_on_oversize_invalid_json_and_expiry(self):
        def oversized():
            yield b"x" * 1_000_000
            yield b"x" * 1_000_001
            self.fail("Stream must stop as soon as its bound is exceeded")
        for body, category in ((oversized(), "crossref_response_too_large"),
                               ([b"not JSON"], "crossref_response_invalid")):
            response = Mock(status_code=200); response.iter_content.return_value = body
            session = Mock(); session.get.return_value = response
            with self.subTest(category=category), self.assertRaisesRegex(resolver.ResolutionError, category):
                fetcher.collect_imf_crossref_json(session, "https://api.crossref.org/works", 60)
            response.close.assert_called_once()
            self.assertIs(session.get.call_args.kwargs["stream"], True)
        response = Mock(status_code=200); response.iter_content.return_value = [b"{}"]
        session = Mock(); session.get.return_value = response
        with patch.object(fetcher.time, "monotonic", side_effect=[0, 31]):
            with self.assertRaisesRegex(resolver.ResolutionError, "crossref_response_timeout"):
                fetcher.collect_imf_crossref_json(session, "https://api.crossref.org/works", 60)
        response.close.assert_called_once()

    def test_fiscal_missing_doi_resolves_unique_current_metadata_and_caches_responses(self):
        case = json.loads((Path(__file__).parent / "fixtures/imf_elibrary/fiscal_chapter_observed.json").read_text())
        responses = [Mock(status_code=200, content=json.dumps(case[key]).encode())
                     for key in ("search_payload", "exact_payload")]
        for response, key in zip(responses, ("search_payload", "exact_payload")):
            response.json.return_value = case[key]
            response.iter_content.return_value = [response.content]
        session = Mock(); session.get.side_effect = responses; cfg = {}
        with patch.object(fetcher, "collect_coveo_preview_html", return_value=case["source_preview_html"]):
            first = fetcher.resolve_imf_browser_publication(cfg, session, case["source_item"], 60)
            second = fetcher.resolve_imf_browser_publication(cfg, session, case["source_item"], 60)
        self.assertEqual(first, second)
        self.assertEqual(first["source_title"], case["source_item"]["title"])
        self.assertIsNone(first["crossref_sha256"])
        self.assertEqual(first["metadata"]["method"], "official_fiscal_chapter")
        self.assertEqual(session.get.call_count, 2)
        search, exact = session.get.call_args_list
        self.assertEqual(search.args[0], "https://api.crossref.org/works")
        self.assertIn("prefix:10.5089,type:edited-book", search.kwargs["params"]["filter"])
        self.assertTrue(exact.args[0].endswith(first["doi"]))
        self.assertTrue(all(call.kwargs["allow_redirects"] is False and call.kwargs["timeout"] == 30
                            for call in session.get.call_args_list))
        for response in responses:
            response.close.assert_called_once()
        metadata = copy.deepcopy(first["metadata"])
        metadata["publisher_page"] = {"pages": 31, "page_sha256": "c" * 64}
        pdf = first["landing_url"].split("?", 1)[0].replace("/display/", "/downloadpdf/display/").replace(".xml", ".pdf")
        proof = dict(schema=2, source_guid=first["source_guid"], source_url=first["source_url"],
                     landing_url=first["landing_url"], pdf_url=pdf, doi=first["doi"], title=first["source_title"],
                     identity_sha256=first["identity_sha256"], metadata=metadata, sha256="a" * 64,
                     bytes=100000, pages=31, landing_status=200, pdf_status=200,
                     source_identity_verified=True, transport="existing_subscription_vless_browser")
        row = dict(institution="imf", title=proof["title"], source_page_url=proof["source_url"], pdf_url=pdf,
                   sha256=proof["sha256"], bytes=proof["bytes"],
                   local_filename=f"IMF_{fetcher.slug(proof['title'])}_{fetcher.short_hash('imf:' + proof['source_guid'])}.pdf",
                   imf_live_download=proof)
        health.validate_live_download(row)
        for change in (lambda p: p.update(pages=30), lambda p: p["metadata"].update(chapter=2),
                       lambda p: p["metadata"].update(search_total_results=101),
                       lambda p: p["metadata"].pop("publisher_page"),
                       lambda p: p["metadata"]["publisher_page"].update(page_sha256=None),
                       lambda p: p.update(crossref_sha256="b" * 64)):
            changed = copy.deepcopy(row); change(changed["imf_live_download"])
            with self.assertRaises(health.InvalidSourceHealth):
                health.validate_live_download(changed)

    def test_missing_doi_for_non_fiscal_or_incomplete_catalog_never_fetches_a_guessed_book(self):
        from imf_fiscal_chapter import FiscalChapterError
        case = json.loads((Path(__file__).parent / "fixtures/imf_elibrary/fiscal_chapter_observed.json").read_text())
        session = Mock()
        wrong = dict(case["source_item"], source_url=case["source_item"]["source_url"].replace("/fm/", "/wp/"))
        with patch.object(fetcher, "collect_coveo_preview_html", return_value=case["source_preview_html"]):
            with self.assertRaises(ValueError):
                fetcher.resolve_imf_browser_publication({}, session, wrong, 60)
        session.get.assert_not_called()
        incomplete = copy.deepcopy(case["search_payload"]); incomplete["message"]["total-results"] += 1
        response = Mock(status_code=200, content=json.dumps(incomplete).encode())
        response.iter_content.return_value = [response.content]
        response.json.return_value = incomplete; session.get.return_value = response
        with patch.object(fetcher, "collect_coveo_preview_html", return_value=case["source_preview_html"]):
            with self.assertRaises(FiscalChapterError):
                fetcher.resolve_imf_browser_publication({}, session, case["source_item"], 60)
        self.assertEqual(session.get.call_count, 1)
        response.close.assert_called_once()

    def test_observed_original_editions_keep_source_and_download_identity_distinct(self):
        from imf_original_edition import resolve_original_edition
        fixture = json.loads((Path(__file__).parent / "fixtures/imf_elibrary/spanish_editions_observed.json").read_text())
        for observed in fixture["observations"]:
            publication, page = observed["publication"], observed["page"]
            metadata = resolve_original_edition(publication, page, source_landing_status=404)
            proof = dict(schema=2, source_guid=publication["source_guid"], source_url=publication["source_url"],
                         landing_url=page["final_url"], pdf_url=page["download_hrefs"][0], doi=publication["doi"],
                         title=publication["source_title"], identity_sha256=publication["identity_sha256"],
                         metadata=metadata, sha256="a" * 64, bytes=100000,
                         pages=metadata["original_edition"]["pages"], landing_status=200, pdf_status=200,
                         source_identity_verified=True, transport="existing_subscription_vless_browser")
            row = dict(institution="imf", title=proof["title"], source_page_url=proof["source_url"],
                       pdf_url=proof["pdf_url"], sha256=proof["sha256"], bytes=proof["bytes"],
                       local_filename=f"IMF_{fetcher.slug(proof['title'])}_{fetcher.short_hash('imf:' + proof['source_guid'])}.pdf",
                       imf_live_download=proof)
            health.validate_live_download(row)
            self.assertNotEqual(proof["doi"], metadata["original_edition"]["doi"])
            changes = [lambda p: p.update(pages=p["pages"] + 1),
                       lambda p: p["metadata"].update(source_landing_status=403),
                       lambda p: p["metadata"].update(source_crossref_sha256=None),
                       lambda p: p["metadata"].update(unverified=True),
                       lambda p: p["metadata"]["original_edition"].update(title="Peru: " + p["metadata"]["original_edition"]["title"].split(":", 1)[1]),
                       lambda p: p["metadata"]["original_edition"].update(doi=p["doi"]),
                       lambda p: p.update(landing_url=p["landing_url"].replace("-es.xml", "-en.xml")),
                       lambda p: p.update(crossref_sha256="b" * 64),
                       lambda p: p.update(schema=1)]
            for index, change in enumerate(changes):
                changed = copy.deepcopy(row); change(changed["imf_live_download"])
                with self.subTest(series=publication["series"], case=index), self.assertRaises(health.InvalidSourceHealth):
                    health.validate_live_download(changed)

    def test_only_confirmed_crossref_404_uses_observed_official_preview(self):
        item = {"title": "Report", "guid": "one", "source_url": IDENTITY.source_url}
        identity = Mock(doi=IDENTITY.doi)
        for status in (200, 404, 403, 429, 503):
            response = Mock(status_code=status, content=b"{}")
            response.iter_content.return_value = [response.content]
            response.json.return_value = {"actual": "metadata"}
            with (self.subTest(status=status),
                patch.object(fetcher, "collect_coveo_preview_html", return_value="observed preview"),
                patch.object(resolver, "bind_source", return_value=identity),
                patch.object(fetcher, "_request_with_retry", return_value=response) as request,
                patch.object(resolver, "resolve_crossref", return_value="crossref") as crossref,
                patch.object(resolver, "resolve_official_preview", return_value="preview") as preview,
            ):
                if status in (200, 404):
                    result = fetcher.resolve_imf_browser_publication({}, Mock(), item, 60)
                    self.assertEqual(result, "preview" if status == 404 else "crossref")
                else:
                    with self.assertRaises(resolver.ResolutionError):
                        fetcher.resolve_imf_browser_publication({}, Mock(), item, 60)
                self.assertEqual(preview.call_count, int(status == 404))
                self.assertEqual(crossref.call_count, int(status == 200))
                self.assertEqual(request.call_args.kwargs["max_attempts"], 3)
                response.close.assert_called_once()

    def test_unrelated_report_never_requests_ieo_or_preview(self):
        session = Mock()
        with patch.object(fetcher, "collect_coveo_preview_html") as preview:
            self.assertIsNone(fetcher.resolve_imf_ieo_followup(
                {}, session, {"title": "Unrelated policy report"}, Path("unused.pdf"), 30, 1000000))
        preview.assert_not_called()
        session.get.assert_not_called()

    def test_complete_ieo_receipt_is_healthy_and_bound_to_exact_producer_row(self):
        with tempfile.TemporaryDirectory() as folder:
            proof, _, _ = ieo_fixture.FollowupTests().run_download(Path(folder))
        data = manifest()
        data["source_checks"] = [source_check(status="ok", new=1)]
        data["downloaded_count"] = 1
        row = dict(institution="imf", title=proof["title"], source_page_url=proof["source_url"],
                   published=proof["published"], pdf_url=proof["pdf_url"], sha256=proof["sha256"],
                   bytes=proof["bytes"], local_filename=f"IMF_{fetcher.slug(proof['title'])}_{fetcher.short_hash('imf:' + proof['source_guid'])}.pdf",
                   imf_official_followup=proof)
        data["downloaded"] = [row]
        def classify(value):
            return health.classify(value, producer_exit_code=0, log_exit_code=0,
                                   date_folder=value["date"], institutions="imf")
        self.assertEqual(classify(data)["source_health"], "healthy")
        changes = [lambda r: r.update(institution="bis"), lambda r: r.update(title="Different title"),
                   lambda r: r.update(published="2026-10-10T04:00:00+00:00"),
                   lambda r: r.update(source_page_url=r["source_page_url"] + "-other"),
                   lambda r: r.update(pdf_url=r["pdf_url"] + "?x=1"),
                   lambda r: r.update(sha256="a" * 64), lambda r: r.update(bytes=True),
                   lambda r: r.update(local_filename="different.pdf"),
                   lambda r: r.update(imf_live_download={}),
                   lambda r: r.update(acquisition_method="verified_original_cache"),
                   lambda r: r.update(imf_official_followup_unknown=True)]
        for missing in proof:
            changes.append(lambda r, field=missing: r["imf_official_followup"].pop(field))
        for index, change in enumerate(changes):
            changed = copy.deepcopy(data); change(changed["downloaded"][0])
            with self.subTest(case=index), self.assertRaises(health.InvalidSourceHealth):
                classify(changed)


if __name__ == "__main__":
    unittest.main()
