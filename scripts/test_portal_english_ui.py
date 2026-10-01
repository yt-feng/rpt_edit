"""Public HTML/SEO must contain previews only, even in complete candidates."""
import json
from pathlib import Path
import re
import tempfile
import unittest

from portal_english_commentary import build, make_source, extract_editorial
from portal_english_ui import detail, homepage, preview_item, ui_assets
from portal_extended_locales import ExpansionError
from test_portal_english_commentary import DAY, IDENTIFIER, URL, COMMENT, SyntheticTranslator, page

ROOT = Path(__file__).resolve().parents[1]


def item(index=1):
    return {'id': '20261001-'+f'{index:016x}', 'title': 'A secondary interpretation',
            'preview': 'Our short editorial interpretation.', 'datePublished': DAY,
            'body_sha256': 'a'*64, 'editorial_sha256': 'b'*64,
            'blocks': [{'tag': 'p', 'text': 'SECRET FULL COMMENTARY'}],
            'original_text': 'SECRET ORIGINAL', 'charts': ['SECRET CHART'], 'source_url': 'https://example.invalid/SECRET'}


class EnglishUITests(unittest.TestCase):
    def test_public_projection_cannot_leak_full_body_or_originals_through_unknown_private_fields(self):
        self.assertEqual(set(preview_item(item())), {'id', 'title', 'preview', 'datePublished'})
        for raw in (detail(item()), homepage([item()])):
            rendered = raw.decode()
            for secret in ('SECRET', 'a'*64, 'b'*64, 'original_text', 'body_sha256', 'editorial_sha256',
                           'source_url', 'articleBody', '<img', '<iframe', '<table', '/charts', '/reports/', '/blog/bbg-'):
                self.assertNotIn(secret, rendered)
            self.assertIn('noindex,follow', rendered)
            self.assertIn('lang="en"', rendered); self.assertIn('data-page="english-commentary"', rendered)
            self.assertIn('/assets/styles.css?v=', rendered); self.assertIn('/assets/blog.css?v=', rendered)
        rendered = detail(item()).decode()
        self.assertIn('id="englishFullCommentary" class="blog-article-content" data-nosnippet hidden></div>', rendered)
        self.assertIn('data-membership-request-open="access"', rendered)
        schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', rendered, re.S)[1])
        self.assertFalse(schema['isAccessibleForFree']); self.assertEqual(schema['description'], item()['preview'])
        self.assertEqual(schema['hasPart']['cssSelector'], '#englishFullCommentary')

    def test_same_search_date_sort_pagination_granularity_without_a_report_or_chart_scope(self):
        rendered = homepage([item(index) for index in range(1, 30)]).decode()
        for control in ('Search', 'Type', 'From', 'To', 'Sort', 'Clear', 'Count', 'Results', 'Empty', 'Prev', 'Page', 'Next'):
            self.assertIn('id="extended'+control+'"', rendered)
        self.assertEqual(rendered.count('class="blog-card extended-result"'), 29)
        self.assertNotIn('value="reports"', rendered); self.assertNotIn('initIndex', rendered)
        self.assertIn('/en/blog/20261001-', rendered)

    def test_unapproved_candidates_are_noindex_and_empty_or_duplicate_collections_are_rejected(self):
        self.assertIn(b'noindex,follow', detail(item()))
        self.assertIn(b'index,follow', detail(item(), approved=True))
        self.assertNotIn(b'noindex', detail(item(), approved=True))
        for rows in ([], [item(), item()]):
            with self.assertRaises(ExpansionError): homepage(rows)

    def test_non_english_embeds_or_malformed_public_id_cannot_render(self):
        for changes in ({'title': '<script>secret</script>'}, {'preview': '原文中文'},
                        {'preview': '![chart](/private)'}, {'preview': 'https://example.invalid/original'},
                        {'id': '../../private'}, {'datePublished': '2026-09-30'}):
            with self.assertRaises(ExpansionError): detail({**item(), **changes})

    def test_complete_cpu_candidate_separates_private_full_text_and_public_previews(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            doc = extract_editorial(URL, page(), DAY)
            result = build(make_source([doc], DAY), root/'out', root/'checkpoint.json', SyntheticTranslator())
            self.assertEqual(result['status'], 'complete-candidate')
            body = json.loads(next((root/'out/private/bodies').glob('*.json')).read_text())
            self.assertIn('Next, watch actual deliveries.', body['blocks'][0]['text'])
            for path in (root/'out/public').rglob('*.html'):
                rendered = path.read_text()
                self.assertNotIn('Next, watch actual deliveries.', rendered)
                self.assertNotIn(COMMENT, rendered); self.assertNotIn('SECRET', rendered)
                self.assertNotIn('body_sha256', rendered); self.assertIn('noindex,follow', rendered)

    def test_english_boot_reuses_account_ui_without_original_catalog_or_newsfeed(self):
        app = (ROOT/'portal_suite/site_src/assets/app.js').read_text()
        start = app.index('async function initEnglishCommentaryAccount()')
        section = app[start:app.index('\n  const boot', start)]
        self.assertIn('initAccountGate("/api")', section)
        for forbidden in ('initIndex(', 'initNewsfeedNav(', 'loadCatalog(', 'initReport(', 'initBlog('):
            self.assertNotIn(forbidden, section)
        self.assertIn('page === "english-commentary"\n    ? initEnglishCommentaryAccount', app)
        assets = ui_assets(); self.assertIn('assets/english-commentary.js', assets)
        script = assets['assets/english-commentary.js'].decode()
        self.assertNotIn('innerHTML', script); self.assertNotIn('localStorage.setItem', script)
        self.assertIn('portal-auth-change', script); self.assertIn('pagehide', script)
        self.assertIn('visibilitychange', script); self.assertIn('current().token !== signedIn.token', script)
        self.assertIn('cache: "no-store"', script); self.assertIn('data', script)


if __name__ == '__main__': unittest.main()
