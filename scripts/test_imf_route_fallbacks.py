"""Missing DOI registration and official IEO receipts keep distinct evidence."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import fetch_institution_latest_pdfs as fetcher
import imf_elibrary_resolver as resolver
import institution_source_health as health
import test_imf_ieo_followup as ieo_fixture
from test_imf_ieo_followup import IDENTITY
from test_institution_source_health import manifest, source_check


class RouteFallbackTests(unittest.TestCase):
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
