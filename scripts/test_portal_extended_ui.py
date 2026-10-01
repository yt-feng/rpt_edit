"""Presentation regressions; synthetic text is not a translation assessment."""
import re
import unittest
from pathlib import Path

from portal_extended_locales import COPY, ORIGIN, ExpansionError, render_document, select_locales
from portal_extended_ui import UI_VERSION, page_parts, standard_detail, standard_homepage, ui_assets
from audit_portal_extended_live import check_page

URL = ORIGIN + '/blog/20260930-layout.html'


def fixture(locale='fr', title='Layout & markup <test>'):
    doc = {'url': URL, 'source_language': 'zh-Hans', 'links': [], 'datePublished': '2026-09-30'}
    translated = {'title': title, 'description': 'A public summary, 22% and $100.', 'copy': COPY,
                  'blocks': [{'tag': 'h2', 'text': 'Section'}, {'tag': 'p', 'text': 'Exact accepted text: 22%, $100, 2026-09-30.'},
                             {'tag': 'tr', 'text': 'A | 100 | 22%'}, {'tag': 'li', 'text': '<script>alert(1)</script>'}], 'links': []}
    return render_document(doc, translated, locale, {URL}).replace('noindex,follow', 'index,follow').encode()


class SharedUITests(unittest.TestCase):
    def test_full_home_reuses_actual_source_search_and_source_data_routes(self):
        source = (Path(__file__).resolve().parent.parent/'portal_suite/site_src/index.html').read_text()
        for locale in select_locales('all-supported'):
            home = standard_homepage(locale, [(URL, fixture(locale))], portal_home=source)
            text = home.decode()
            for field in ('searchInput', 'bankFilter', 'industryFilter', 'scopeFilter', 'availabilityFilter', 'pageSize', 'externalDateFilter', 'authorityInstitutionFilter'):
                self.assertIn('id="'+field+'"', text)
            self.assertIn('data-page="index" data-extended-portal="full"', text)
            self.assertIn('<base href="'+ORIGIN+'/">', text)
            self.assertEqual(text.count('id="searchInput"'), 1)
            self.assertEqual(text.count('id="results"'), 1)
            self.assertNotIn('/'+locale+'/data/', text)
            self.assertNotIn('/'+locale+'/research.html', text)
            check_page(home, ORIGIN+'/'+locale+'/', locale, require_standard_ui=True)
        with self.assertRaises(ExpansionError):
            standard_homepage('fr', [(URL, fixture())], portal_home='<main>not a portal</main>')
    def test_all_33_share_main_styles_navigation_search_and_article_format(self):
        for locale in select_locales('all-supported'):
            with self.subTest(locale=locale):
                raw = fixture(locale)
                alts = {'zh-Hans': ORIGIN+'/', locale: ORIGIN+'/'+locale+'/'}
                home = standard_homepage(locale, [(URL, raw)], alternates=alts)
                detail = standard_detail(raw, locale, URL, alternates=alts)
                for body in (home, detail):
                    text = body.decode()
                    self.assertIn('class="topbar blog-topbar"', text)
                    self.assertIn('class="legal-footer blog-footer"', text)
                    for asset in ('styles.css', 'blog.css', 'locale.css', 'extended-locales.css'):
                        self.assertIn('/assets/'+asset+'?v=', text)
                    self.assertIn('id="accountGate"', text)
                    self.assertIn('data-auth-open="register"', text)
                    self.assertIn('data-extended-ui="'+UI_VERSION+'"', text)
                    self.assertNotIn('/en/', text)
                    self.assertNotIn('<style>', text)
                self.assertIn('class="search-panel"', home.decode())
                self.assertIn('class="blog-card extended-result"', home.decode())
                for control in ('Search', 'Type', 'From', 'To', 'Sort', 'Prev', 'Next', 'Clear'):
                    self.assertIn('id="extended'+control+'"', home.decode())
                self.assertIn('class="blog-article-content"', detail.decode())
                # Collection-only preview is not sufficient for production parity.
                check_page(home, ORIGIN+'/'+locale+'/', locale)
                check_page(detail, ORIGIN+'/'+locale+URL[len(ORIGIN):], locale, require_standard_ui=True)

    def test_live_gate_rejects_200_minimal_page_or_missing_asset_link(self):
        raw = fixture()
        with self.assertRaises(ExpansionError):
            check_page(standard_homepage('fr', [(URL, raw)]), ORIGIN+'/fr/', 'fr', require_standard_ui=True)
        url = ORIGIN+'/fr'+URL[len(ORIGIN):]
        with self.assertRaises(ExpansionError):
            check_page(raw, url, 'fr', require_standard_ui=True)
        detail = standard_detail(raw, 'fr', URL, alternates={})
        with self.assertRaises(ExpansionError):
            check_page(detail.replace(b'/assets/blog.css', b'/missing.css'), url, 'fr', require_standard_ui=True)

    def test_content_and_schema_are_byte_preserved_after_approval(self):
        raw = fixture()
        parts = page_parts(raw, 'fr', URL)
        detail = standard_detail(raw, 'fr', URL, alternates={}).decode()
        self.assertIn(parts['content'], detail)
        self.assertIn(parts['notice'], detail)
        schema = re.search(r'<script type="application/ld\+json">.*?</script>', raw.decode()).group()
        self.assertIn(schema, detail)
        self.assertIn('2026-09-30', detail)
        self.assertIn('&lt;script&gt;', detail)
        self.assertNotIn('<script>alert', detail)

    def test_unpublished_unknown_and_english_candidates_cannot_be_restyled(self):
        for raw, locale in ((fixture().replace(b'index,follow', b'noindex,follow'), 'fr'),
                            (fixture('fr'), 'en'), (fixture().replace(b'<main>', b'<article>'), 'fr')):
            with self.assertRaises(ExpansionError):
                standard_homepage(locale, [(URL, raw)])

    def test_homes_only_link_the_approved_collection_and_real_source_functions(self):
        home = standard_homepage('fr', [(URL, fixture())], alternates={'fr': ORIGIN+'/fr/', 'de': ORIGIN+'/de/'}).decode()
        self.assertIn('/fr/blog/20260930-layout.html', home)
        self.assertNotIn('/fr/research.html', home)
        self.assertNotIn('/fr/charts', home)
        self.assertNotIn('/fr/courses.html', home)
        self.assertNotIn('/pt/', home)
        self.assertIn(ORIGIN+'/research.html', home)
        self.assertIn(ORIGIN+'/de/', home)
        self.assertIn('"numberOfItems": 1', home)

    def test_existing_candidate_renderer_stays_minimal_for_checkpoint_replay(self):
        raw = fixture().decode()
        self.assertIn('<body><header><nav>', raw)
        self.assertNotIn(UI_VERSION, raw)
        self.assertEqual(set(ui_assets()), {'assets/extended-locales.css', 'assets/extended-locales.js'})

    def test_shared_script_urls_are_content_versioned(self):
        from portal_extended_locales import digest
        from portal_extended_ui import SITE_ASSETS
        text = standard_homepage('fr', [(URL, fixture())]).decode()
        for name in ('app.js', 'contact.js'):
            self.assertIn('/assets/'+name+'?v='+digest((SITE_ASSETS/name).read_bytes())[:12], text)


if __name__ == '__main__':
    unittest.main()
