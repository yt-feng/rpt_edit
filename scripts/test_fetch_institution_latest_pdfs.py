#!/usr/bin/env python3
"""Regression tests for institution PDF source resolution."""

from __future__ import annotations

import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import fetch_institution_latest_pdfs as fetcher


COUNTRY_REPORT_URL = (
    "https://www.imf.org/-/media/files/publications/cr/2026/english/"
    "1zweea2026002.pdf"
)
MONGOLIA_COUNTRY_REPORT_URL = (
    "https://www.imf.org/-/media/files/publications/cr/2026/english/"
    "1mngea2026001.pdf"
)


class FakeResponse:
    def __init__(
        self,
        *,
        text: str = "",
        json_data: dict | None = None,
        status_code: int = 200,
    ) -> None:
        self.text = text
        self.content = text.encode("utf-8")
        self._json_data = json_data or {}
        self.status_code = status_code

    def json(self) -> dict:
        return self._json_data

    def raise_for_status(self) -> None:
        return None


class BISRedesignTests(unittest.TestCase):
    FIXTURES = Path(__file__).parent / "fixtures" / "institution_sources"
    REPORT_URL = "https://www.bis.org/publications/working-paper-1376-what-determines-banks-excess-demand-reserves"

    def test_modern_feed_keeps_publications_dates_and_legacy_dedup(self) -> None:
        response = FakeResponse(text=(self.FIXTURES / "bis_research_redesign.rss").read_text())
        with patch.object(fetcher, "http_get", return_value=response) as get:
            items = fetcher.collect_rss_items(fetcher.INSTITUTIONS["bis"], object(), 10)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(len(items), 7)
        self.assertEqual(items[0]["source_url"], self.REPORT_URL)
        self.assertEqual(items[0]["guid"], "https://www.bis.org/publ/work1376.htm")
        self.assertEqual(items[0]["date"], "2026-09-07T00:00:00Z")
        self.assertEqual(items[0]["pdf_candidates"], [])
        self.assertEqual(items[0]["scrape_url"], self.REPORT_URL)
        self.assertEqual(items[2]["pdf_candidates"], ["https://www.bis.org/bcbs/publ/d600.pdf"])
        self.assertEqual(items[3]["pdf_candidates"], ["https://www.bis.org/fsi/publ/insights77.pdf"])
        self.assertEqual([item["pdf_candidates"][0] for item in items[4:]], [
            "https://www.bis.org/publ/arpdf/ar2026e.pdf",
            "https://www.bis.org/publ/qtrpdf/r_qt2606.pdf",
            "https://www.bis.org/publ/bppdf/bispap172.pdf",
        ])

    def test_scoped_download_ignores_related_reports_and_attachments(self) -> None:
        page = (self.FIXTURES / "bis_work1376_download.html").read_text()
        self.assertEqual(fetcher.scrape_pdf_candidates(page, self.REPORT_URL), [self.REPORT_URL + ".pdf"])

    def test_primary_download_can_point_to_official_file_storage(self) -> None:
        page = '<div class="hero-publication__buttons"><a class="btn btn--primary" href="/content/dam/bis/papers/work1376.pdf">PDF (38 Pages)</a></div>'
        self.assertEqual(fetcher.scrape_pdf_candidates(page, self.REPORT_URL), ["https://www.bis.org/content/dam/bis/papers/work1376.pdf"])

    def test_quarterly_review_download_uses_issue_hero_not_related_pdfs(self) -> None:
        page_url = "https://www.bis.org/publications/qr-202609"
        page = '''<div class="hero-quaterly container-xxl">
          <div class="col-12 hero-quaterly__buttons"><div class="button">
          <a class="btn btn--primary btn--size-large btn--inverted"
             href="https://www.bis.org/publications/qr-202609_0.pdf"
             aria-label="PDF (90 Pages)">PDF (90 Pages)</a></div></div></div>
          <div class="related"><a class="btn btn--primary"
             href="/publications/qr-202606.pdf">Previous issue</a></div>'''
        self.assertEqual(fetcher.scrape_pdf_candidates(page, page_url), [
            "https://www.bis.org/publications/qr-202609_0.pdf",
        ])

    def test_quarterly_review_without_issue_pdf_stays_unresolved(self) -> None:
        page = '''<div class="hero-quaterly__buttons"><a class="btn btn--outline"
          href="#">Share</a></div><a class="btn btn--primary"
          href="/publications/unrelated.pdf">Related report</a>'''
        self.assertEqual(fetcher.scrape_pdf_candidates(
            page, "https://www.bis.org/publications/qr-202609"), [])

    def test_missing_main_pdf_does_not_use_related_file_or_non_bis_host(self) -> None:
        page = '<a href="/publications/unrelated.pdf">Related paper</a><div class="hero-publication__buttons"><a class="btn btn--primary" href="https://example.org/report.pdf">PDF</a></div>'
        self.assertEqual(fetcher.scrape_pdf_candidates(page, self.REPORT_URL), [])

    def test_legacy_page_pdf_and_query_compatibility(self) -> None:
        cfg = fetcher.INSTITUTIONS["bis"]
        page_url = "https://www.bis.org/publ/work1376.htm"
        self.assertEqual(fetcher._derive_pdf_candidates(cfg, page_url + "?download=1"), ["https://www.bis.org/publ/work1376.pdf?download=1"])
        page = '<a href="work1376.pdf">Full paper</a><a href="work1375.pdf">Previous paper</a>'
        self.assertEqual(fetcher.scrape_pdf_candidates(page, page_url), ["https://www.bis.org/publ/work1376.pdf"])

    def test_known_series_keep_existing_seen_state_keys(self) -> None:
        for modern, old in (
            ("working-paper-1373-settlement-liquidity", "publ/work1373.htm"),
            ("bulletin-134-supervisory-screening", "publ/bisbull134.htm"),
            ("fsi-insight-77-high-expectation", "fsi/publ/insights77.htm"),
        ):
            with self.subTest(modern=modern):
                self.assertEqual(fetcher.bis_publication_guid("https://www.bis.org/publications/" + modern), "https://www.bis.org/" + old)

    def run_bis_main(self, directory: str, items: list[dict], seen: dict | None = None) -> tuple[int, dict, dict]:
        path = Path(directory)
        state_path = path / "seen.json"
        state_path.write_text(json.dumps({"version": 1, "items": seen or {}}))
        argv = ["fetcher", "--institutions", "bis", "--output-dir", str(path / "pdfs"), "--seen-state-path", str(state_path), "--archive-path", str(path / "archive.jsonl"), "--since-days", "7"]
        with (
            patch.object(fetcher.sys, "argv", argv),
            patch.object(fetcher, "collect_rss_items", return_value=items),
            patch.object(fetcher, "http_get", return_value=FakeResponse(text='<a href="/unrelated.pdf">Related paper</a>')),
            patch.object(fetcher, "write_github_output"),
            patch.object(fetcher, "write_source_health_summary"),
        ):
            code = fetcher.main()
        return code, json.loads(state_path.read_text()), json.loads((path / "pdfs" / "institution_run_manifest.json").read_text())

    def test_main_pdf_missing_is_reported_and_remains_retryable(self) -> None:
        item = {"title": "Fixture report", "source_url": self.REPORT_URL, "guid": self.REPORT_URL, "date": fetcher.datetime.now(fetcher.timezone.utc).isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL}
        with tempfile.TemporaryDirectory() as directory:
            code, state, manifest = self.run_bis_main(directory, [item])
        self.assertEqual(code, 2)
        self.assertNotIn("bis:" + self.REPORT_URL, state["items"])
        self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 1)
        self.assertEqual(manifest["skipped"][0]["reason"], "main_pdf_missing")

    def test_existing_seen_identity_and_recency_still_skip_downloads(self) -> None:
        now = fetcher.datetime.now(fetcher.timezone.utc)
        guid = fetcher.bis_publication_guid(self.REPORT_URL)
        items = [
            {"title": "Seen report", "source_url": self.REPORT_URL, "guid": guid, "date": now.isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL},
            {"title": "Older report", "source_url": self.REPORT_URL + "-older", "guid": "older", "date": (now - fetcher.timedelta(days=8)).isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL},
        ]
        seen = {"bis:" + guid: {"status": "downloaded", "first_seen": now.date().isoformat()}}
        with tempfile.TemporaryDirectory() as directory:
            code, state, manifest = self.run_bis_main(directory, items, seen)
        self.assertEqual(code, 0)
        self.assertEqual(manifest["source_checks"][0]["eligible_item_count"], 0)
        self.assertEqual(state["items"]["bis:" + guid]["status"], "downloaded")
        self.assertEqual(state["items"]["bis:older"]["status"], "too_old")

    def test_future_and_coming_soon_reports_stay_unseen_without_resolution_failures(self) -> None:
        now = fetcher.datetime.now(fetcher.timezone.utc)
        items = [
            {"title": "Future release", "source_url": self.REPORT_URL, "guid": "future",
             "date": (now + fetcher.timedelta(days=5)).isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL},
            {"title": "Coming Soon: Global report", "source_url": self.REPORT_URL, "guid": "pending",
             "date": now.isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL},
        ]
        with tempfile.TemporaryDirectory() as directory:
            code, state, manifest = self.run_bis_main(directory, items)
            self.assertEqual(code, 0)
            self.assertEqual(state["items"], {})
            self.assertEqual(manifest["source_checks"][0]["eligible_item_count"], 0)
            self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 0)
            self.assertEqual([row["reason"] for row in manifest["skipped"]], ["publication_pending"] * 2)
            # A publication released later is re-evaluated, not lost to dedup.
            items[0]["date"] = now.isoformat()
            code, state, manifest = self.run_bis_main(directory, items)
            self.assertEqual(code, 2)
            self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 1)
            self.assertEqual(state["items"], {})


class BCGDiscoveryEvidenceTests(unittest.TestCase):
    # URLs below are present in the committed consulting archive. HTML fragments
    # are synthetic link fixtures, not claims of a captured BCG page template.
    OLD_PAGE = "https://www.bcg.com/publications/2021/sustainable-investing-leadership-blueprint"
    CURRENT_PAGE = "https://www.bcg.com/publications/2026/asia-pacific-retail-leaders-growth-ai"
    OFFICIAL_PDF = "https://web-assets.bcg.com/pdf-src/prod-live/every-drop-counts-pathways-to-restore-germanys-water-balance.pdf"
    SEA_PDF = "https://cdn.sea.com/investor/4Q2025/JcKns4LaJC8bxcQdJwXz/2026.03.03%20Sea%20Fourth%20Quarter%20and%20Full%20Year%202025%20Results%20Deck.pdf"

    class Clock(fetcher.datetime):
        @classmethod
        def now(cls, tz=None):
            value = cls(2026, 10, 11, 12, tzinfo=fetcher.timezone.utc)
            return value.astimezone(tz) if tz else value.replace(tzinfo=None)

    def item(self, page=None, **changes):
        page = page or self.CURRENT_PAGE
        return dict({"title": "Current report citing research from 2014", "source_url": page,
                     "guid": page, "date": "2026-10-10T02:00:00Z", "pdf_candidates": [],
                     "scrape_url": page}, **changes)

    def run_bcg_main(self, directory, item, html_text="", *, since_days=7, redirect_url=None):
        root = Path(directory)
        response = FakeResponse(text=html_text)
        if redirect_url:
            response.url = redirect_url
        def download(session, candidates, destination, *args, **kwargs):
            destination.write_bytes(b"%PDF-1.7 synthetic report fixture")
            return candidates[0], "ok"
        argv = ["fetch", "--output-dir", str(root / "pdfs"), "--date", "261011", "--institutions", "bcg",
                "--archive-path", str(root / "archive.jsonl"), "--seen-state-path", str(root / "seen.json"),
                "--since-days", str(since_days)]
        with (patch.object(fetcher, "datetime", self.Clock), patch("sys.argv", argv),
              patch.dict("os.environ", {"PROXY_SUBSCRIPTION_URL": ""}),
              patch.object(fetcher, "collect_sitemap_items", return_value=[item]),
              patch.object(fetcher, "http_get", return_value=response) as get,
              patch.object(fetcher, "download_pdf", side_effect=download) as fetch_pdf,
              patch.object(fetcher, "write_github_output"), patch.object(fetcher, "write_source_health_summary")):
            code = fetcher.main()
        manifest = json.loads((root / "pdfs/institution_run_manifest.json").read_text())
        seen = json.loads((root / "seen.json").read_text())["items"]
        return code, manifest, seen, get.call_args_list, fetch_pdf.call_args_list

    def test_explicit_older_publication_year_ignores_fresh_sitemap_lastmod_and_stays_unseen(self):
        for page in (self.OLD_PAGE, "https://www.bcg.com/publications/2025/new-zealand-growing-our-advantage-in-agritech"):
            with self.subTest(page=page), tempfile.TemporaryDirectory() as directory:
                code, manifest, seen, gets, downloads = self.run_bcg_main(directory, self.item(page))
                self.assertEqual((code, gets, downloads, seen), (0, [], [], {}))
                self.assertEqual(manifest["skipped"][0]["reason"], "publication_year_before_window")
                self.assertEqual(manifest["source_checks"][0]["eligible_item_count"], 0)
                self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 0)

    def test_current_year_report_quoting_old_years_and_unknown_year_page_are_not_guessed_old(self):
        for page in (self.CURRENT_PAGE, "https://www.bcg.com/publications/a-report-without-a-year"):
            with self.subTest(page=page), tempfile.TemporaryDirectory() as directory:
                code, manifest, seen, gets, downloads = self.run_bcg_main(
                    directory, self.item(page), f'<p>Research since 2014</p><a href="{self.OFFICIAL_PDF}">Download</a>')
                self.assertEqual((code, manifest["downloaded_count"], len(gets), len(downloads)), (0, 1, 1, 1))
                self.assertEqual(seen["bcg:" + page]["status"], "downloaded")

    def test_since_window_crossing_years_does_not_discard_that_year(self):
        page = "https://www.bcg.com/publications/2025/new-zealand-growing-our-advantage-in-agritech"
        with tempfile.TemporaryDirectory() as directory:
            code, manifest, _seen, _gets, downloads = self.run_bcg_main(
                directory, self.item(page), f'<a href="{self.OFFICIAL_PDF}">Download</a>', since_days=500)
        self.assertEqual((code, manifest["downloaded_count"], len(downloads)), (0, 1, 1))

    def test_year_guard_requires_explicit_publisher_path_not_title_query_or_other_host(self):
        self.assertEqual(fetcher.bcg_publication_year(self.OLD_PAGE), 2021)
        for url in ("https://www.bcg.com/publications/research-from-2014?date=2014",
                    "https://www.bcg.com/publications/2026/study-since-2014",
                    "https://other.example/publications/2014/report",
                    "https://www.bcg.com.evil.test/publications/2014/report"):
            with self.subTest(url=url):
                self.assertIn(fetcher.bcg_publication_year(url), (None, 2026))

    def test_external_only_citation_is_missing_main_report_and_not_marked_seen(self):
        for direct in (False, True):
            item = self.item(pdf_candidates=[self.SEA_PDF] if direct else [])
            with self.subTest(direct=direct), tempfile.TemporaryDirectory() as directory:
                code, manifest, seen, _gets, downloads = self.run_bcg_main(
                    directory, item, f'<a href="{self.SEA_PDF}">Referenced company filing</a>')
            self.assertEqual((code, seen, downloads), (2, {}, []))
            self.assertEqual(manifest["skipped"][0]["reason"], "main_pdf_missing")
            self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 1)

    def test_ordinary_bcg_article_without_any_pdf_keeps_existing_no_pdf_behavior(self):
        with tempfile.TemporaryDirectory() as directory:
            code, manifest, seen, _gets, downloads = self.run_bcg_main(
                directory, self.item(), '<p>A normal web article with no PDF attachment.</p>')
        self.assertEqual((code, downloads), (0, []))
        self.assertEqual(manifest["skipped"][0]["reason"], "no_pdf")
        self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 0)
        self.assertEqual(seen["bcg:" + self.CURRENT_PAGE]["status"], "no_pdf")

    def test_external_citation_before_official_report_cannot_win_generic_link_order(self):
        page = f'<a href="{self.SEA_PDF}">Citation</a><a href="{self.OFFICIAL_PDF}">Report</a>'
        with tempfile.TemporaryDirectory() as directory:
            code, manifest, _seen, _gets, downloads = self.run_bcg_main(directory, self.item(), page)
        self.assertEqual(code, 0)
        self.assertEqual(downloads[0].args[1], [self.OFFICIAL_PDF])
        self.assertEqual(manifest["downloaded"][0]["pdf_url"], self.OFFICIAL_PDF)

    def test_redirected_landing_cannot_remove_bcg_source_host_restriction(self):
        with tempfile.TemporaryDirectory() as directory:
            code, manifest, seen, _gets, downloads = self.run_bcg_main(
                directory, self.item(), f'<a href="{self.SEA_PDF}">Company filing</a>',
                redirect_url="https://external.example/reference-page")
        self.assertEqual((code, seen, downloads), (2, {}, []))
        self.assertEqual(manifest["skipped"][0]["reason"], "main_pdf_missing")

    def test_archived_bcg_owned_hosts_remain_allowed_and_other_institutions_unchanged(self):
        owned = [self.OFFICIAL_PDF, "https://media-publications.bcg.com/report.pdf", "https://www.bcg.com/report.pdf"]
        unrelated = [self.SEA_PDF, "https://www.hbs.edu/report.pdf",
                     "https://web-assets.bcg.com.evil.test/report.pdf", "https://web-assets.bcg.com@evil.test/report.pdf"]
        self.assertEqual(fetcher.filter_institution_pdf_candidates("bcg", owned + unrelated), owned)
        for institution in ("imf", "worldbank", "bis", "mckinsey", "bain"):
            self.assertEqual(fetcher.filter_institution_pdf_candidates(institution, unrelated), unrelated)


class DependencyHoldFetchTests(unittest.TestCase):
    def item(self, identity, title="Fixture report", *, landing=False):
        url = "https://www.bis.org/publ/" + identity + ".htm"
        return {"title": title, "source_url": url, "guid": url,
                "date": fetcher.datetime.now(fetcher.timezone.utc).isoformat(),
                "pdf_candidates": [] if landing else [url.removesuffix(".htm") + ".pdf"],
                "scrape_url": url if landing else ""}

    def held_name(self, item):
        key = "bis:" + item["guid"]
        return f"{fetcher.INSTITUTIONS['bis']['token']}_{fetcher.slug(item['title'])}_{fetcher.short_hash(key)}.pdf"

    def hold(self, item):
        return {'source': self.held_name(item), 'sha256': fetcher.hashlib.sha256(b'%PDF-1.7 fixture original').hexdigest(),
                'size': len(b'%PDF-1.7 fixture original')}

    def archive(self, path, item, **changes):
        record = dict(local_filename=self.held_name(item), source_page_url=item['source_url'], published=item['date'],
            pdf_url=item['source_url'].removesuffix('.htm')+'.pdf', bytes=self.hold(item)['size'],
            sha256=self.hold(item)['sha256'], feed_pdf_candidates=item['pdf_candidates'])
        record.update(changes)
        fetcher.append_archive(path/'archive.jsonl', record)
        return record

    def run_fetch(self, path, items, holds, *, force=False):
        hold_path = path / "holds.json"
        hold_path.write_text(json.dumps(holds))
        state_path = path / "seen.json"
        argv = ["fetcher", "--institutions", "bis", "--output-dir", str(path / "pdfs"),
                "--seen-state-path", str(state_path), "--archive-path", str(path / "archive.jsonl"),
                "--dependency-holds", str(hold_path), "--force-reprocess", str(force).lower()]
        def download(session, candidates, destination, *args, **kwargs):
            destination.write_bytes(b"%PDF-1.7 fixture original")
            return candidates[0], "ok"
        with (patch.object(fetcher.sys, "argv", argv),
              patch.object(fetcher, "collect_rss_items", return_value=items) as collect,
              patch.object(fetcher, "download_pdf", side_effect=download) as get_pdf,
              patch.object(fetcher, "http_get", side_effect=lambda session, url, *a, **kw: FakeResponse(text='<a href="'+url.removesuffix(".htm")+'.pdf">Report</a>')) as get_page,
              patch.object(fetcher, "collect_coveo_preview_candidates", side_effect=AssertionError("No preview request")),
              patch.object(fetcher, "write_github_output") as output,
              patch.object(fetcher, "write_source_health_summary"),
              patch.object(fetcher, "log")):
            code = fetcher.main()
        return (code, json.loads(state_path.read_text()),
                json.loads((path / "pdfs" / "institution_run_manifest.json").read_text()),
                get_pdf.call_args_list, get_page.call_args_list, output.call_args_list)

    def test_known_hold_checks_landing_without_pdf_and_new_identity_still_downloads(self):
        held = self.item("work-held", landing=True)
        fresh = self.item("work-new")  # Same title, different exact source identity.
        holds = {"schema": 1, "sources": [self.hold(held)]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            self.archive(path, held)
            code, state, manifest, pdf_calls, page_calls, outputs = self.run_fetch(path, [held, fresh], holds)
            self.assertEqual(code, 0)
            self.assertEqual(manifest["dependency_held_count"], 1)
            self.assertEqual(manifest["downloaded_count"], 1)
            self.assertEqual(manifest["source_checks"][0]["status"], "ok")
            self.assertEqual(manifest["source_checks"][0]["eligible_item_count"], 2)
            self.assertEqual(len(pdf_calls), 1)
            self.assertEqual(pdf_calls[0].args[1], fresh["pdf_candidates"])
            self.assertEqual(len(page_calls), 1)
            self.assertNotIn("bis:" + held["guid"], state["items"])
            self.assertEqual(state["items"]["bis:" + fresh["guid"]]["status"], "downloaded")
            archived = (path / "archive.jsonl").read_text()
            self.assertEqual(archived.count(held["source_url"]), 1)
            self.assertIn(fresh["source_url"], archived)
            # The next schedule must still classify the hold, not silently mark
            # it completed; the unrelated successful download is seen normally.
            again = self.run_fetch(path, [held, fresh], holds)
            self.assertEqual(again[2]["dependency_held_count"], 1)
            self.assertEqual(again[2]["downloaded_count"], 0)
            self.assertEqual(again[3], [])
            self.assertNotIn("bis:" + held["guid"], again[1]["items"])

    def test_hold_is_not_overridden_by_force_reprocess(self):
        item = self.item("work-held", landing=True)
        with tempfile.TemporaryDirectory() as directory:
            self.archive(Path(directory), item)
            result = self.run_fetch(Path(directory), [item],
                                    {"schema": 1, "sources": [self.hold(item)]}, force=True)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1]["items"], {})
        self.assertEqual(result[2]["dependency_held_count"], 1)
        self.assertEqual(result[2]["downloaded_count"], 0)
        self.assertEqual(result[3], [])
        self.assertEqual(len(result[4]), 1)

    def test_malformed_export_is_rejected_before_source_requests(self):
        source = self.hold(self.item('held'))
        for holds in ({'schema': True, 'sources': []}, {'schema': 2, 'sources': []},
                      {'schema': 1, 'sources': [dict(source, source='../report.pdf')]},
                      {'schema': 1, 'sources': [dict(source, source='bad\\name.pdf')]},
                      {'schema': 1, 'sources': [dict(source, source='bad\x00name.pdf')]},
                      {'schema': 1, 'sources': [dict(source, size=True)]},
                      {'schema': 1, 'sources': 'report.pdf'}, {'schema': 1, 'sources': [], 'extra': True}):
            with self.subTest(holds=holds), tempfile.TemporaryDirectory() as directory:
                with patch.object(fetcher, "collect_rss_items", side_effect=AssertionError("No source request")):
                    with self.assertRaisesRegex(ValueError, "dependency export invalid"):
                        self.run_fetch(Path(directory), [], holds)

    def test_same_guid_and_title_changed_date_or_direct_pdf_bypasses_hold(self):
        original = self.item('unchanged-guid')
        for changes in ({'date': (fetcher.datetime.now(fetcher.timezone.utc) - fetcher.timedelta(hours=1)).isoformat()},
                        {'pdf_candidates': ['https://www.bis.org/publ/revised.pdf']}):
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as directory:
                path = Path(directory); self.archive(path, original)
                changed = dict(original, **changes)
                result = self.run_fetch(path, [changed], {'schema': 1, 'sources': [self.hold(original)]})
                self.assertEqual(result[2]['dependency_held_count'], 0)
                self.assertEqual(result[2]['downloaded_count'], 1)
                self.assertEqual(len(result[3]), 1)
                row = result[2]['downloaded'][0]
                self.assertEqual(row['sha256'], self.hold(original)['sha256'])
                self.assertEqual(row['feed_pdf_candidates'], changed['pdf_candidates'])

    def test_coming_soon_filename_collision_never_suppresses_new_report(self):
        original = self.item('same-guid', title='Coming Soon')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            self.archive(path, original, pdf_url='https://www.imf.org/gfsr-oct2026.pdf')
            self.archive(path, original, pdf_url='https://www.imf.org/weo-oct2021.pdf')
            result = self.run_fetch(path, [original], {'schema': 1, 'sources': [self.hold(original)]})
            self.assertEqual(result[2]['dependency_held_count'], 0)
            self.assertEqual(result[2]['downloaded_count'], 1)

    def test_missing_wrong_size_or_wrong_sha_archive_never_suppresses(self):
        original = self.item('held')
        for changes in (None, {'bytes': 1}, {'sha256': '0'*64}, {'published': ''}):
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as directory:
                path = Path(directory)
                if changes is not None: self.archive(path, original, **changes)
                result = self.run_fetch(path, [original], {'schema': 1, 'sources': [self.hold(original)]})
                self.assertEqual(result[2]['dependency_held_count'], 0)
                self.assertEqual(result[2]['downloaded_count'], 1)

    def test_legacy_unique_url_page_date_size_requires_matching_current_direct_pdf(self):
        original = self.item('held')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory); record = self.archive(path, original)
            del record['sha256']; del record['feed_pdf_candidates']
            (path/'archive.jsonl').write_text(json.dumps(record)+'\n')
            result = self.run_fetch(path, [original], {'schema': 1, 'sources': [self.hold(original)]})
            self.assertEqual(result[2]['dependency_held_count'], 1)
            versions = fetcher.dependency_hold_versions(path/'archive.jsonl', [self.hold(original)])
            self.assertFalse(fetcher.matches_dependency_hold(versions, self.held_name(original), dict(original, pdf_candidates=[])))

    def test_legacy_imf_working_paper_uses_only_exact_producer_candidate_pair(self):
        name = 'IMF_Does-Foreign-Borrowing-Lift-Growth_8aaa5d8a.pdf'
        primary = 'https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026216-source-pdf.pdf'
        page = 'https://www.imf.org/en/publications/wp/issues/2026/10/03/does-foreign-borrowing-lift-growth-580148'
        date = '2026-10-02T04:00:00+00:00'
        candidates = fetcher.derive_imf_pdf_candidates({'imfseries': 'Working Papers', 'seriesvolumeno': '2026/216'})
        source = {'source': name, 'sha256': 'fc791b9b2374eadd7820527ea99e160a5d7802ac17fc5e1df658f2b6c876975b', 'size': 17202708}
        row = dict(local_filename=name, source_page_url=page, published=date, pdf_url=primary, bytes=source['size'])
        item = dict(source_url=page, date=date, pdf_candidates=candidates)
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / 'archive.jsonl'
            versions = fetcher.dependency_hold_versions(archive, [source], [row])
            self.assertEqual(candidates, [primary, primary.replace('-source-pdf', '')])
            self.assertTrue(fetcher.matches_dependency_hold(versions, name, item))
            for changes in ({'pdf_candidates': list(reversed(candidates))},
                            {'pdf_candidates': candidates + ['https://www.imf.org/other.pdf']},
                            {'pdf_candidates': [primary, 'https://www.imf.org/other.pdf']},
                            {'pdf_candidates': [value.replace('2026216', '2026217') for value in candidates]},
                            {'date': '2026-10-03T04:00:00+00:00'},
                            {'source_url': page + '-revised'}):
                with self.subTest(changes=changes):
                    self.assertFalse(fetcher.matches_dependency_hold(versions, name, dict(item, **changes)))
            # A legacy archive using the alternate URL cannot prove that the
            # currently preferred PDF is unchanged.
            alternate = fetcher.dependency_hold_versions(archive, [source], [dict(row, pdf_url=candidates[1])])
            self.assertFalse(fetcher.matches_dependency_hold(alternate, name, item))
            wrong_size = fetcher.dependency_hold_versions(archive, [source], [dict(row, bytes=1)])
            self.assertFalse(fetcher.matches_dependency_hold(wrong_size, name, item))
            # Modern records retain exact ordered feed-candidate matching.
            modern = fetcher.dependency_hold_versions(archive, [source], [dict(row, feed_pdf_candidates=candidates)])
            self.assertTrue(fetcher.matches_dependency_hold(modern, name, item))
            self.assertFalse(fetcher.matches_dependency_hold(modern, name, dict(item, pdf_candidates=[primary])))

    def test_private_manifest_supplement_enables_missing_archive_but_conflicts_fail_open(self):
        item = self.item('held')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory); row = self.archive(path, item)
            (path/'archive.jsonl').unlink()
            holds = {'schema': 1, 'sources': [self.hold(item)], 'versions': [row]}
            result = self.run_fetch(path, [item], holds)
            self.assertEqual(result[2]['dependency_held_count'], 1)
            self.archive(path, item, pdf_url='https://www.bis.org/different.pdf')
            result = self.run_fetch(path, [item], holds)
            self.assertEqual(result[2]['dependency_held_count'], 0)
            self.assertEqual(result[2]['downloaded_count'], 1)

    def test_empty_candidate_lists_require_landing_resolution_and_changed_link_bypasses_hold(self):
        item = self.item('held', landing=True)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory); self.archive(path, item)
            versions = fetcher.dependency_hold_versions(path/'archive.jsonl', [self.hold(item)])
            self.assertFalse(fetcher.matches_dependency_hold(versions, self.held_name(item), item))
            self.assertFalse(fetcher.matches_dependency_hold(versions, self.held_name(item), item,
                             ['https://www.bis.org/new.pdf']))
            self.assertTrue(fetcher.matches_dependency_hold(versions, self.held_name(item), item,
                            [item['source_url'].removesuffix('.htm')+'.pdf']))


class CoveoPreviewTests(unittest.TestCase):
    def test_cached_html_exposes_country_report_pdf(self) -> None:
        cached_html = (
            '<html><a href="/-/media/files/publications/cr/2026/english/'
            '1zweea2026002.pdf">Download PDF</a></html>'
        )

        candidates = fetcher.scrape_pdf_candidates(
            cached_html,
            "https://www.imf.org/en/Publications/CR/Issues/2026/08/07/zimbabwe",
        )

        self.assertEqual(candidates[0], COUNTRY_REPORT_URL)

    def test_cached_stock_number_resolves_fresh_country_report(self) -> None:
        cached_html = (
            '<li><p>Stock No<!-- -->:</p>'
            '<p role="presentation">1MNGEA2026001</p></li>'
        )

        candidates = fetcher.scrape_imf_preview_candidates(
            cached_html,
            (
                "https://www.imf.org/en/publications/cr/issues/2026/08/05/"
                "mongolia-2026-article-iv-consultation-discussions"
            ),
        )

        self.assertEqual(candidates[0], MONGOLIA_COUNTRY_REPORT_URL)
        self.assertEqual(
            candidates[1],
            MONGOLIA_COUNTRY_REPORT_URL.removesuffix(".pdf") + "-source-pdf.pdf",
        )

    def test_coveo_items_keep_preview_id_and_filter_rollups(self) -> None:
        payload = {
            "totalCount": 2,
            "results": [
                {
                    "title": "Zimbabwe: Staff Report",
                    "uniqueId": "country-report-cache-id",
                    "raw": {
                        "clickableuri": (
                            "https://www.imf.org/en/Publications/CR/Issues/2026/08/07/"
                            "zimbabwe-staff-report"
                        ),
                        "permanentid": "country-report",
                        "imfseries": "IMF Staff Country Reports",
                        "seriesvolumeno": "2026/212",
                    },
                },
                {
                    "title": "Commodity Special Feature",
                    "uniqueId": "rollup-cache-id",
                    "raw": {
                        "clickableuri": (
                            "https://www.imf.org/en/Publications/SPROLLs/"
                            "commodity-special-feature"
                        ),
                        "permanentid": "rollup",
                    },
                },
            ],
        }
        cfg = dict(fetcher.INSTITUTIONS["imf"])

        with patch.object(fetcher, "http_post", return_value=FakeResponse(json_data=payload)):
            items = fetcher.collect_coveo_items(cfg, object(), timeout=10, rows=25)

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["guid"], "country-report")
        self.assertEqual(items[0]["coveo_unique_id"], "country-report-cache-id")

    def test_preview_helper_calls_coveo_html_endpoint(self) -> None:
        captured: dict = {}
        cached_html = f'<a href="{COUNTRY_REPORT_URL}">PDF</a>'

        def fake_http_get(session, url, timeout, **kwargs):
            captured.update({"url": url, "timeout": timeout, **kwargs})
            return FakeResponse(text=cached_html)

        cfg = dict(fetcher.INSTITUTIONS["imf"])
        with patch.object(fetcher, "http_get", side_effect=fake_http_get):
            candidates = fetcher.collect_coveo_preview_candidates(
                cfg,
                object(),
                "country-report-cache-id",
                "https://www.imf.org/en/Publications/CR/Issues/2026/08/07/zimbabwe",
                12,
            )

        self.assertEqual(candidates[0], COUNTRY_REPORT_URL)
        self.assertTrue(captured["url"].endswith("/rest/search/v2/html"))
        self.assertEqual(
            captured["params"],
            {
                "organizationId": "imfproduction561s308u",
                "uniqueId": "country-report-cache-id",
            },
        )
        self.assertTrue(captured["headers"]["Authorization"].startswith("Bearer "))


class DuckDuckGoFallbackTests(unittest.TestCase):
    RESULT_HTML = (
        '<html><a href="https://www.mckinsey.com/~/media/mckinsey/'
        'featured-insights/2026/example-report.pdf">Example report</a></html>'
    )
    STORE_HTML = (
        '<article><h5><span>Independent official report</span></h5>'
        '<time datetime="2026-08-22T12:00:00Z">August 22, 2026</time>'
        '<a href="#/download/%2F~%2Fmedia%2Fmckinsey%2Fofficial-report.pdf">'
        'Report (20 pages)</a></article>'
    )

    @staticmethod
    def config() -> dict:
        return {
            "query": "site:mckinsey.com filetype:pdf",
            "recent_years": 0,
            "fallback_pdf_listing_urls": [
                "https://www.mckinsey.com/featured-insights/insights-store",
            ],
        }

    def test_browser_timeout_falls_back_to_plain_requests(self) -> None:
        browser = Mock()
        browser.get.side_effect = fetcher.requests.Timeout("fixture timeout")
        session = Mock()
        session.get.return_value = FakeResponse(text=self.RESULT_HTML)

        with (
            patch.object(fetcher, "_HAS_CFFI", True),
            patch.object(fetcher, "cffi_requests", browser),
        ):
            items = fetcher.collect_ddg_items(self.config(), session, timeout=60, df="")

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Example report")
        self.assertEqual(browser.get.call_count, 1)
        self.assertEqual(session.get.call_count, 1)
        self.assertEqual(session.get.call_args.kwargs["timeout"], 25)

    def test_ddg_challenge_falls_back_to_official_listing(self) -> None:
        session = Mock()
        session.get.side_effect = [
            FakeResponse(
                text='<form class="challenge-form">bots use DuckDuckGo too.</form>',
                status_code=202,
            ),
            FakeResponse(text=self.STORE_HTML),
        ]

        with patch.object(fetcher, "_HAS_CFFI", False):
            items = fetcher.collect_ddg_items(self.config(), session, timeout=10, df="")

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Independent official report")
        self.assertEqual(items[0]["date"], "2026-08-22T12:00:00Z")
        self.assertEqual(
            items[0]["source_url"],
            "https://www.mckinsey.com/~/media/mckinsey/official-report.pdf",
        )
        called_urls = [call.args[0] for call in session.get.call_args_list]
        self.assertEqual(
            called_urls,
            [
                "https://html.duckduckgo.com/html/",
                "https://www.mckinsey.com/featured-insights/insights-store",
            ],
        )

    def test_official_listing_parser_uses_publication_date_for_recent_filter(self) -> None:
        year = str(fetcher.datetime.now(fetcher.timezone.utc).year)
        store_html = self.STORE_HTML.replace("2026", year)
        session = Mock()
        session.get.side_effect = [
            fetcher.requests.Timeout("fixture timeout"),
            FakeResponse(text=store_html),
        ]
        cfg = self.config()
        cfg["recent_years"] = 1

        with patch.object(fetcher, "_HAS_CFFI", False):
            items = fetcher.collect_ddg_items(cfg, session, timeout=10, df="")

        self.assertEqual(len(items), 1)
        self.assertTrue(items[0]["date"].startswith(year))

    def test_all_transport_failures_raise_source_health_error(self) -> None:
        session = Mock()
        session.get.side_effect = fetcher.requests.Timeout("fixture timeout")

        with (
            patch.object(fetcher, "_HAS_CFFI", False),
            self.assertRaisesRegex(RuntimeError, "unavailable across all routes"),
        ):
            fetcher.collect_ddg_items(self.config(), session, timeout=10, df="")

        self.assertEqual(session.get.call_count, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
