"""Offline observed-metadata tests; never start HTTP clients or browsers."""
from copy import deepcopy
import html
import json
from pathlib import Path
import unittest

import imf_elibrary_resolver as r

FIXTURE = Path(__file__).parent / "fixtures/imf_elibrary/estonia_observed_metadata.json"


class ResolverTests(unittest.TestCase):
    def setUp(self):
        self.observed = json.loads(FIXTURE.read_text())
        self.item, self.raw = self.observed["item"], self.observed["raw"]
        self.crossref = self.observed["crossref"]
        self.landing = self.observed["landing_observed"]
        # This is deliberately labelled reconstructed markup. The field values
        # are real captured metadata, not an invented raw-page snapshot.
        self.preview = (f'<link rel="canonical" href="{self.item["source_url"]}">'
                        f'<h1>{html.escape(self.item["title"])}</h1>'
                        f'<p>DOI: {self.landing["doi"]}</p>'
                        f'<meta name="citation_isbn" content="{self.landing["isbn"]}">')
        self.identity = r.bind_source(self.item, self.raw, self.preview, self.item["source_url"])
        self.publication = r.resolve_crossref(self.identity, self.crossref)
        self.metadata = {"citation_doi": [self.landing["doi"]], "citation_title": [self.landing["title"]],
                         "citation_isbn": [self.landing["isbn"]], "citation_pdf_url": [self.landing["pdf_href"]]}

    def parse_landing(self, **changes):
        args = dict(final_url=self.landing["url"], metadata=self.metadata,
                    h1s=[self.landing["title"]], download_hrefs=[self.landing["pdf_href"]])
        args.update(changes)
        return r.validate_landing_metadata(self.publication, **args)

    def test_observed_source_crossref_and_catalog_identity(self):
        self.assertEqual(self.identity.doi, "10.5089/9798229063937.019")
        self.assertEqual(self.identity.isbn, "9798229063937")
        self.assertEqual(self.identity.issue, "082")
        self.assertEqual(self.publication["title"], "Republic of Estonia")
        self.assertEqual(self.publication["full_title"], self.item["title"])
        self.assertEqual(self.publication["pdf_url_candidates"], [])
        self.assertFalse(self.publication["pdf_verified"])
        self.assertEqual(self.parse_landing(), self.landing["pdf_href"])

    def test_pending_item_without_raw_metadata(self):
        identity = r.bind_source(self.item, {}, self.preview, self.item["source_url"])
        self.assertIsNone(identity.issue)
        self.assertEqual(r.resolve_crossref(identity, self.crossref)["landing_url"], self.publication["landing_url"])

    def test_verbatim_official_preview_excerpt_with_and_without_raw(self):
        text = (FIXTURE.parent / "estonia_preview_excerpt.html").read_text()
        identities = [r.bind_source(self.item, raw, text, self.item["source_url"]) for raw in (self.raw, {})]
        self.assertEqual(identities[0].source_binding_sha256, identities[1].source_binding_sha256)
        for identity in identities:
            self.assertEqual((identity.year, identity.issue, identity.series), ("2026", "082", ("Technical Assistance Reports",)))
            self.assertEqual(r.resolve_crossref(identity, self.crossref)["landing_url"], self.publication["landing_url"])

    def test_verbatim_preview_visible_isbn_and_issue_disagreements_rejected(self):
        text = (FIXTURE.parent / "estonia_preview_excerpt.html").read_text()
        for changed in (text.replace('>9798229063937</p>', '>9798229063074</p>'),
                        text.replace('>082</p>', '>081</p>')):
            self.assertNotEqual(changed, text)
            with self.assertRaises(r.ResolutionError):
                r.bind_source(self.item, self.raw, changed, self.item["source_url"])

    def test_cache_binding_changes_with_source_version_and_preview(self):
        item = {**self.item, "date": "2026-10-10T21:30:00+00:00"}
        other = r.bind_source(item, self.raw, self.preview, item["source_url"])
        self.assertNotEqual(other.source_binding_sha256, self.identity.source_binding_sha256)
        another = r.bind_source(self.item, self.raw, self.preview + " ", self.item["source_url"])
        self.assertNotEqual(another.preview_sha256, self.identity.preview_sha256)
        self.assertEqual(another.source_binding_sha256, self.identity.source_binding_sha256)

    def test_reject_source_guid_title_url_and_preview_mismatch(self):
        for key, value in [("permanentid", "other-guid"), ("title", "Other Report"),
                           ("clickableuri", self.item["source_url"] + "-other")]:
            with self.subTest(key=key), self.assertRaises(r.ResolutionError):
                r.bind_source(self.item, {**self.raw, key: value}, self.preview, self.item["source_url"])
        with self.assertRaises(r.ResolutionError):
            r.bind_source(self.item, self.raw, self.preview, self.item["source_url"] + "-other")
        with self.assertRaisesRegex(r.ResolutionError, "preview_title_mismatch"):
            r.bind_source(self.item, self.raw, self.preview.replace(self.item["title"], "Other report"), self.item["source_url"])

    def test_no_doi_guess_from_isbn_series_or_filename(self):
        preview = self.preview.replace(self.identity.doi, "")
        with self.assertRaisesRegex(r.ResolutionError, "explicit_doi_missing_or_ambiguous"):
            r.bind_source(self.item, self.raw, preview, self.item["source_url"])

    def test_ambiguous_doi_and_conflicting_isbn_are_rejected(self):
        for suffix in ('<a href="https://doi.org/10.5089/9798229063074.029">Other DOI</a>',
                       '<meta name="citation_isbn" content="9798229063074">'):
            with self.assertRaises(r.ResolutionError):
                r.bind_source(self.item, self.raw, self.preview + suffix, self.item["source_url"])

    def test_explicit_raw_doi_can_be_used_but_cannot_conflict_with_preview(self):
        no_doi = self.preview.replace(self.identity.doi, "")
        identity = r.bind_source(self.item, {**self.raw, "doi": self.identity.doi}, no_doi, self.item["source_url"])
        self.assertEqual(identity.doi, self.identity.doi)
        with self.assertRaises(r.ResolutionError):
            r.bind_source(self.item, {**self.raw, "doi": "10.5089/9798229063074.029"}, self.preview, self.item["source_url"])

    def test_crossref_complete_title_and_subtitle_required(self):
        changed = deepcopy(self.crossref)
        changed["message"].pop("subtitle")
        with self.assertRaisesRegex(r.ResolutionError, "crossref_title_mismatch"):
            r.resolve_crossref(self.identity, changed)

    def test_crossref_rejects_every_conflicting_identity_field(self):
        wrong = {"DOI": "10.5089/9798229063074.029", "publisher": "Other Publisher",
                 "title": ["Another Country"], "subtitle": ["Another Study"], "volume": "2025",
                 "issue": "081", "container-title": ["Working Papers"], "language": "es",
                 "ISBN": ["9798229063074"]}
        for key, value in wrong.items():
            with self.subTest(key=key):
                changed = deepcopy(self.crossref); changed["message"][key] = value
                with self.assertRaises(r.ResolutionError):
                    r.resolve_crossref(self.identity, changed)

    def test_resource_must_be_real_official_matching_issue_and_language(self):
        for url in (self.publication["landing_url"].replace("elibrary.imf.org", "evil.invalid"),
                    self.publication["landing_url"].replace("/082/", "/081/").replace("issue-082", "issue-081"),
                    self.publication["landing_url"].replace("-en.xml", "-es.xml")):
            changed = deepcopy(self.crossref); changed["message"]["resource"]["primary"]["URL"] = url
            with self.assertRaises(r.ResolutionError):
                r.resolve_crossref(self.identity, changed)

    def test_observed_crossref_pdf_link_is_retained_without_generation(self):
        changed = deepcopy(self.crossref)
        changed["message"]["link"] = [{"URL": self.landing["pdf_href"], "content-type": "application/pdf"}]
        result = r.resolve_crossref(self.identity, changed)
        self.assertEqual(result["pdf_url_candidates"], [self.landing["pdf_href"]])
        changed["message"]["link"][0]["URL"] = self.landing["pdf_href"].replace("-en.pdf", "-es.pdf")
        with self.assertRaises(r.ResolutionError):
            r.resolve_crossref(self.identity, changed)

    def test_www_and_nonwww_are_only_allowed_same_document_aliases(self):
        self.assertEqual(self.parse_landing(final_url=self.publication["landing_url"]), self.landing["pdf_href"])
        with self.assertRaises(r.ResolutionError):
            self.parse_landing(final_url=self.landing["url"].replace("issue-082", "article-A001"))

    def test_browser_title_country_alone_is_not_sufficient_heading(self):
        with self.assertRaisesRegex(r.ResolutionError, "landing_heading_mismatch"):
            self.parse_landing(h1s=["Republic of Estonia"])
        metadata = {**self.metadata, "citation_title": ["Republic of Estonia"]}
        self.assertEqual(self.parse_landing(metadata=metadata), self.landing["pdf_href"])

    def test_conflicting_empty_or_case_duplicated_doi_rejected(self):
        for metadata in ({**self.metadata, "citation_doi": []},
                         {**self.metadata, "citation_doi": [""]},
                         {**self.metadata, "citation_doi": ["10.5089/9798229063074.029"]},
                         {**self.metadata, "CITATION_DOI": ["10.5089/9798229063074.029"]}):
            with self.assertRaises(r.ResolutionError):
                self.parse_landing(metadata=metadata)

    def test_missing_pdf_never_becomes_a_constructed_url(self):
        with self.assertRaisesRegex(r.ResolutionError, "official_pdf_missing_or_ambiguous"):
            self.parse_landing(metadata={k: v for k, v in self.metadata.items() if k != "citation_pdf_url"}, download_hrefs=[])

    def test_contradictory_citation_pdf_and_foreign_pdf_rejected(self):
        for pdf in (self.landing["pdf_href"].replace("issue-082", "article-A001"),
                    self.landing["pdf_href"].replace("www.elibrary.imf.org", "evil.invalid")):
            with self.assertRaises(r.ResolutionError):
                self.parse_landing(metadata={**self.metadata, "citation_pdf_url": [pdf]})

    def test_invalid_url_authorities_encoding_and_queries_rejected(self):
        url = self.landing["pdf_href"]
        for bad in (url.replace("https://", "http://"), url.replace("https://", "https://@"),
                    url.replace("https://", "https://user:pass@"), url + "?token=not-permitted",
                    url + "#x", url.replace("/view/", "/%76iew/"), url.replace("/view/", "/../view/"),
                    url.replace(".org/", ".org.evil.invalid/"), url.replace(".org/", ".org:bad/")):
            with self.subTest(url=bad), self.assertRaises(r.ResolutionError):
                r.validate_publication_url(bad, pdf=True)
        with self.assertRaises(r.ResolutionError):
            r.source_url(self.item["source_url"].replace("https://", "https://@"))

    def test_book_pair_uses_only_observed_isbn_paths(self):
        landing = "https://www.elibrary.imf.org/display/book/9798229056298/9798229056298.xml"
        pdf = "https://www.elibrary.imf.org/downloadpdf/display/book/9798229056298/9798229056298.pdf"
        self.assertEqual(r.validate_official_pair(landing, pdf, "10.5089/9798229056298.089")["kind"], "book")
        with self.assertRaises(r.ResolutionError):
            r.validate_official_pair(landing, pdf, self.identity.doi)

    def test_html_adapter_ignores_navigation_and_never_executes_scripts(self):
        markup = '<script>throw new Error("do not execute")</script>' + ''.join(f'<a href="/section/{i}">Menu</a>' for i in range(100))
        markup += f'<h1>{html.escape(self.landing["title"])}</h1>'
        for key, values in self.metadata.items():
            for value in values:
                markup += f'<meta name="{key}" content="{html.escape(value)}">'
        markup += f'<a href="{self.landing["pdf_href"]}">Download PDF</a>'
        self.assertEqual(r.resolve_landing(self.publication, markup, self.landing["url"]), self.landing["pdf_href"])

    def test_malformed_data_returns_content_free_errors(self):
        for bad in ({"message": None}, {"message": {"DOI": self.identity.doi, "publisher": ["SECRET"]}}, None):
            with self.assertRaises(r.ResolutionError) as caught:
                r.resolve_crossref(self.identity, bad)
            self.assertNotIn("SECRET", str(caught.exception))
        with self.assertRaises(r.ResolutionError):
            r.validate_landing_metadata({}, final_url="SECRET", metadata={}, h1s=[], download_hrefs=[])


class ObservedLandingTests(unittest.TestCase):
    def cases(self):
        for name in ("estonia_cpi", "guidance"):
            yield json.loads((FIXTURE.parent / (name + "_landing_observation.json")).read_text())

    def validate(self, case, **changes):
        args = {key: case["page"][key] for key in ("final_url", "metadata", "h1s", "download_hrefs")}
        args.update(changes)
        return r.validate_landing_metadata(case["publication"], **args)

    def test_real_cloud_pages_without_citation_tags_keep_full_resource_and_heading_binding(self):
        for case in self.cases():
            self.assertEqual(case["page"]["landing_status"], 200)
            self.assertEqual(set(case["page"]["metadata"]), {"canonical_url"})
            self.assertEqual(self.validate(case), case["page"]["download_hrefs"][0])

    def test_present_doi_title_isbn_or_canonical_conflicts_are_never_ignored(self):
        for case in self.cases():
            publication, metadata = case["publication"], case["page"]["metadata"]
            changes = [(key, ["10.5089/9798229063074.029"]) for key in ("citation_doi", "dc.identifier.doi", "prism.doi")]
            changes += [(key, ["Different Report"]) for key in ("citation_title", "dc.title")]
            changes += [("citation_isbn", ["9798229063074"]), ("canonical_url", ["https://evil.invalid/report"])]
            changes += [(key, []) for key in ("citation_doi", "dc.identifier.doi", "prism.doi", "citation_title", "dc.title")]
            for key, value in changes:
                with self.subTest(key=key, value=value), self.assertRaises(r.ResolutionError):
                    self.validate(case, metadata={**metadata, key: value})
            for extra in ({"dc.title": ["Different Report"]}, {"DC.TITLE": ["Different Report"]}):
                with self.assertRaisesRegex(r.ResolutionError, "landing_title_mismatch"):
                    self.validate(case, metadata={**metadata, "citation_title": [publication["full_title"]], **extra})

    def test_missing_redundant_tags_never_allow_partial_duplicate_or_wrong_heading(self):
        for case in self.cases():
            for headings in ([], ["Different Report"], [case["publication"]["full_title"]] * 2,
                             [case["publication"]["full_title"].split(":")[0].split(" ")[0]]):
                with self.subTest(headings=headings), self.assertRaisesRegex(r.ResolutionError, "landing_heading_mismatch"):
                    self.validate(case, h1s=headings)

    def test_missing_tags_never_authorize_unobserved_or_different_edition_pdf(self):
        for case in self.cases():
            page = case["page"]
            wrong = page["download_hrefs"][0].replace("-en.pdf", "-es.pdf")
            for hrefs in ([], [wrong], ["https://evil.invalid/other.pdf"]):
                with self.assertRaises(r.ResolutionError):
                    self.validate(case, download_hrefs=hrefs)
            with self.assertRaisesRegex(r.ResolutionError, "landing_url_identity_mismatch"):
                self.validate(case, final_url=page["final_url"].replace("-en.xml", "-es.xml"))


class DeclaredOriginalLanguageTests(unittest.TestCase):
    def cases(self):
        for name in ("chile_hls", "chile_tar"):
            yield json.loads((FIXTURE.parent / (name + "_observed_metadata.json")).read_text())

    def bind(self, case, preview=None):
        item = case["item"]
        return r.bind_source(item, {}, preview or case["preview_excerpt"], item["source_url"])

    def test_two_observed_sources_keep_english_doi_metadata_and_explicit_spanish_original(self):
        expected = {"10.5089/9798229062657.029": "071", "10.5089/9798229064521.019": "083"}
        for case in self.cases():
            identity = self.bind(case)
            publication = r.resolve_crossref(identity, case["crossref"])
            self.assertEqual(identity.original_language, "es")
            self.assertEqual(publication["original_language"], "es")
            self.assertEqual(publication["language"], "en")
            self.assertEqual(publication["full_title"], case["item"]["title"])
            self.assertEqual(publication["issue"], expected[identity.doi])
            self.assertEqual(publication["doi"], identity.doi)
            self.assertEqual(publication["isbn"], identity.isbn)
            self.assertEqual(publication["series"], case["crossref"]["message"]["container-title"])
            self.assertIn("-en.xml", publication["landing_url"])
            self.assertEqual(publication["pdf_url_candidates"], [])

    def test_unknown_quoted_or_other_location_descriptions_keep_strict_default(self):
        for case in self.cases():
            preview = case["preview_excerpt"]
            prefix = next(value for value in r.SPANISH_ORIGINAL_PREFIXES if value in preview)
            variants = [preview.replace(prefix, text) for text in (
                "[This report is only available in French]", "", "The following report says " + prefix,
                "[This report may be available in Spanish]", "[Another report is only available in Spanish]")]
            variants += [preview.replace('name="Description"', 'name="unrelated"'),
                         preview.replace(f'<meta name="Description" content="{prefix}">', f'<p>{prefix}</p>'),
                         preview + '<meta name="Description" content="This report is in English">']
            baseline = self.bind(case)
            for changed in variants:
                with self.subTest(description=changed):
                    identity = self.bind(case, changed)
                    self.assertIsNone(identity.original_language)
                    self.assertNotEqual(identity.source_binding_sha256, baseline.source_binding_sha256)
                    self.assertIsNone(r.resolve_crossref(identity, case["crossref"])["original_language"])

    def test_original_language_never_relaxes_source_title_doi_series_or_locator(self):
        for case in self.cases():
            identity = self.bind(case)
            for key, value in (("DOI", "10.5089/9798229063074.029"),
                               ("subtitle", ["Reporte sobre la misión de asistencia técnica en estadísticas de finanzas públicas"]),
                               ("container-title", ["Other Series"]), ("issue", "070")):
                changed = deepcopy(case["crossref"]); changed["message"][key] = value
                with self.subTest(key=key), self.assertRaises(r.ResolutionError):
                    r.resolve_crossref(identity, changed)
            changed = deepcopy(case["crossref"])
            changed["message"]["resource"]["primary"]["URL"] = changed["message"]["resource"]["primary"]["URL"].replace("-en.xml", "-es.xml")
            with self.assertRaises(r.ResolutionError):
                r.resolve_crossref(identity, changed)
            changed = case["preview_excerpt"].replace(html.escape(case["item"]["title"]), "Different report")
            with self.assertRaisesRegex(r.ResolutionError, "preview_title_mismatch"):
                self.bind(case, changed)

    def test_crossref_series_is_retained_when_pending_source_has_no_series_field(self):
        case = next(self.cases())
        preview = case["preview_excerpt"].replace('<meta name="Series" content="High-Level Summary Technical Assistance Reports">', '')
        identity = self.bind(case, preview)
        self.assertEqual(identity.series, ())
        self.assertEqual(r.resolve_crossref(identity, case["crossref"])["series"],
                         ["High-Level Summary Technical Assistance Reports"])


class OfficialPreviewFallbackTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads((FIXTURE.parent / "albania_observed_preview.json").read_text())
        self.item = self.case["item"]
        self.preview = self.case["preview_excerpt"]

    def resolve(self, preview=None):
        preview = self.preview if preview is None else preview
        identity = r.bind_source(self.item, {}, preview, self.item["source_url"])
        return identity, r.resolve_official_preview(identity, preview, self.item["source_url"])

    def test_observed_albania_preview_resolves_real_link_without_claiming_crossref(self):
        identity, publication = self.resolve()
        self.assertEqual(publication["landing_url"], self.case["observed_landing_url"])
        self.assertEqual(publication["doi"], "10.5089/9798229061933.029")
        self.assertEqual(publication["isbn"], "9798229061933")
        self.assertEqual((publication["year"], publication["issue"], publication["language"]), ("2026", "073", "en"))
        self.assertEqual(publication["title_variants"], [self.item["title"]])
        self.assertEqual(publication["full_title"], self.item["title"])
        self.assertEqual(publication["metadata"], {"method": "official_source_preview", "preview_sha256": identity.preview_sha256})
        self.assertIsNone(publication["crossref_sha256"])
        self.assertFalse(publication["pdf_verified"])
        self.assertEqual(publication["pdf_url_candidates"], [])

    def test_independent_language_isbn_series_volume_and_issue_are_required(self):
        for fragment in ('<meta name="Language" content="ENG">', '<p>ISBN: 9798229061933</p>',
                         '<meta name="Series" content="High-Level Summary Technical Assistance Reports">',
                         '<p>Volume: 2026</p>', '<p>Issue: 073</p>'):
            with self.subTest(missing=fragment), self.assertRaises(r.ResolutionError):
                self.resolve(self.preview.replace(fragment, ''))
        for old, new in [('content="ENG"', 'content="SPA"'), ('ISBN: 9798229061933', 'ISBN: 9798229062657'),
                         ('content="High-Level Summary Technical Assistance Reports"', 'content="Policy Papers"'),
                         ('Volume: 2026', 'Volume: 2025'), ('Issue: 073', 'Issue: 072')]:
            with self.subTest(field=old), self.assertRaises(r.ResolutionError):
                self.resolve(self.preview.replace(old, new))

    def test_actual_link_is_mandatory_no_generated_country_or_series_url(self):
        landing = self.case["observed_landing_url"]
        for changed in (self.preview.replace(landing, "https://www.elibrary.imf.org/"),
                        self.preview.replace(landing, "https://evil.invalid/view/journals/029/2026/073/029.2026.issue-073-en.xml"),
                        self.preview.replace(landing, landing.replace("/073/", "/072/").replace("issue-073", "issue-072")),
                        self.preview.replace(landing, landing.replace("-en.xml", "-es.xml")),
                        self.preview + '<a href="https://elibrary.imf.org/view/journals/029/2026/072/029.2026.issue-072-en.xml">Different report</a>'):
            with self.assertRaises(r.ResolutionError):
                self.resolve(changed)

    def test_preview_content_and_url_must_match_the_previously_bound_source(self):
        identity, _ = self.resolve()
        with self.assertRaisesRegex(r.ResolutionError, "preview_content_mismatch"):
            r.resolve_official_preview(identity, self.preview + ' ', self.item["source_url"])
        with self.assertRaisesRegex(r.ResolutionError, "preview_source_mismatch"):
            r.resolve_official_preview(identity, self.preview, self.item["source_url"] + '-other')
        with self.assertRaisesRegex(r.ResolutionError, "preview_title_mismatch"):
            self.resolve(self.preview.replace(html.escape(self.item["title"]), "Different report"))

    def test_official_preview_tracking_value_allows_observed_dot_but_no_extra_query(self):
        observed = self.case["observed_landing_url"]
        self.assertEqual(r.validate_publication_url(observed)["issue"], "073")
        for changed in (observed + '&token=unknown', observed + '&cid=other',
                        observed.replace('lk-com-dsp-imf.org', 'https://evil.invalid'), observed + '#fragment'):
            with self.assertRaises(r.ResolutionError):
                r.validate_publication_url(changed)


if __name__ == "__main__":
    unittest.main()
