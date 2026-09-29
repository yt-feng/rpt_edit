import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from build_portal_extended_locales import build
from portal_extended_locales import ORIGIN, ExpansionError, file_for_url, make_corpus, PublicParser
from portal_extended_publication import compose, checked_batches, read_active_batches
from audit_portal_extended_live import audit
from portal_extended_r2 import R2Store, R2IntegrityError
from test_portal_extended_r2 import FakeR2
from test_portal_extended_locales import FakeTranslator
from test_portal_extended_incremental import daily_doc, raw_page, URL, DAY


class PublicationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.store = R2Store(FakeR2(), 'private-bucket', '_extended-locales/staging/publication')
        self.root = self.base/'site'; self.root.mkdir()
        (self.root/'index.html').write_text('<html><head></head><body>Home</body></html>')
        (self.root/'robots.txt').write_text('User-agent: GPTBot\nDisallow: /\n')
        (self.root/'sitemap.xml').write_text('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc>'+ORIGIN+'/sitemap-pages.xml</loc></sitemap></sitemapindex>')
        self.number = 0

    def candidate(self, locale='fr', url=URL):
        self.number += 1
        corpus = make_corpus([daily_doc(url)])
        work = self.base/str(self.number); work.mkdir()
        build(corpus, locale, work/'candidate', work/'checkpoint.json', FakeTranslator())
        generation = corpus['documents_sha256']
        self.store.put_source(corpus)
        self.store.put_checkpoint(locale, generation, work/'checkpoint.json')
        saved = self.store.upload_candidate(work/'candidate', locale, generation)
        target = self.root/file_for_url(url); target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw_page(url))
        return {'generation': generation, 'candidates': {locale: saved['candidate_id']}}

    def publish(self, batches):
        workspace = Path(tempfile.mkdtemp(dir=self.base))
        return compose(self.root, self.store, batches, workspace)

    def test_head_only_change_replays_exact_units_and_rechecks_current_html(self):
        batch = self.candidate()
        source = self.root/file_for_url(URL)
        source.write_bytes(source.read_bytes().replace(b'</head>', b'<meta name="build" content="new"></head>'))
        before = source.read_bytes().split(b'<body>')[1]
        result = self.publish([batch])
        self.assertTrue(result['ready'])
        self.assertEqual(result['page_counts'], {'fr': 1})
        self.assertEqual(result['replays'][0]['translation_calls'], 0)
        self.assertNotEqual(result['replays'][0]['source_generation'], batch['generation'])
        self.assertEqual(source.read_bytes().split(b'<body>')[1], before)
        self.assertFalse((self.root/'fr/index.html').exists())
        self.assertIn('Disallow: /', (self.root/'robots.txt').read_text())
        self.assertIn('sitemap-extended.xml', (self.root/'sitemap.xml').read_text())
        self.assertIn('sitemap-pages.xml', (self.root/'sitemap.xml').read_text())
        page = (self.root/'fr'/file_for_url(URL)).read_text()
        self.assertIn('index,follow', page)
        self.assertNotIn('noindex', page)

    def test_semantic_change_is_rejected_without_modifying_tree(self):
        batch = self.candidate()
        source = self.root/file_for_url(URL)
        source.write_bytes(raw_page(URL, body='<h1>Changed report</h1><p>New facts.</p>'))
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        with self.assertRaisesRegex(ExpansionError, 'source content changed'):
            self.publish([batch])
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_later_batch_keeps_earlier_locale_pages_and_reciprocal_alternates(self):
        french = self.candidate()
        portuguese = self.candidate('pt')
        other = self.candidate('fr', ORIGIN+'/blog/20260925-other.html')
        result = self.publish([french, portuguese, other])
        self.assertEqual(result['page_counts'], {'fr': 2, 'pt': 1})
        for locale in ('fr', 'pt'):
            parser = PublicParser(); parser.feed((self.root/locale/file_for_url(URL)).read_text()); parser.close()
            self.assertEqual(parser.alternates['fr'], ORIGIN+'/fr'+URL[len(ORIGIN):])
            self.assertEqual(parser.alternates['pt'], ORIGIN+'/pt'+URL[len(ORIGIN):])
        sitemap = (self.root/'sitemap-extended-fr.xml').read_text()
        self.assertIn('20260925-new.html', sitemap)
        self.assertIn('20260925-other.html', sitemap)

    def test_checkpoint_cannot_change_approved_translation(self):
        batch = self.candidate()
        work = self.base/'seed.json'
        self.store.restore_checkpoint('fr', batch['generation'], work)
        payload = json.loads(work.read_text())
        next(iter(payload['rows'].values()))['text'] = 'Autre traduction valide.'
        work.write_text(json.dumps(payload))
        self.store.put_checkpoint('fr', batch['generation'], work)
        with self.assertRaisesRegex(ExpansionError, 'approved candidate bytes'):
            self.publish([batch])

    def test_english_and_unapproved_or_incomplete_candidate_fail(self):
        with self.assertRaises(ExpansionError):
            checked_batches([{'generation':'a'*64, 'candidates':{'en':'b'*64}}])
        batch = self.candidate()
        batch['candidates']['fr'] = 'a'*64
        with self.assertRaises(Exception):
            self.publish([batch])
        self.assertFalse((self.root/'fr').exists())

    def test_active_ledger_is_loaded_only_from_pinned_verified_production(self):
        identity = {'slot': 'a', 'release_id': 'release', 'tree_sha256': 'a'*64}
        ledger = {'schema_version':2, 'status':'assembled', 'batches':[self.candidate()]}
        with mock.patch('resume_portal_locale_candidate.read_pinned_manifest', return_value={'files':{
             'data/extended-locales/assembly.json': {'sha256':'b'*64, 'size':1}}}) as pinned, \
             mock.patch('verify_prepared_static_slot.read_verified_candidate_body', return_value=json.dumps(ledger).encode()) as verified:
            self.assertEqual(read_active_batches(self.store, identity), ledger['batches'])
            pinned.assert_called_once_with(self.store.client, self.store.bucket, identity)
            verified.assert_called_once()
            verified.side_effect = RuntimeError('checksum mismatch')
            with self.assertRaisesRegex(RuntimeError, 'checksum'):
                read_active_batches(self.store, identity)

    def test_live_detail_only_audit_checks_real_urls_without_requesting_homepage(self):
        self.publish([self.candidate()])
        seen = []
        def response(url, **kwargs):
            seen.append(url)
            relative = url.removeprefix(ORIGIN+'/')
            page = self.root/relative
            return mock.Mock(status_code=200 if page.is_file() else 404,
                headers={'Content-Language':'fr'}, content=page.read_bytes() if page.is_file() else b'')
        with mock.patch('audit_portal_extended_live.requests.Session') as session:
            session.return_value.get.side_effect = response
            report = audit(ORIGIN, 'fr')
            self.assertEqual(report['status'], 'passed')
            self.assertEqual(report['reports'][0]['pages'], 1)
            self.assertNotIn(ORIGIN+'/fr/', seen)

    def test_release_workflow_assembles_after_legacy_parity_and_preserves_approval(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/'.github/workflows/neutral-edge-cutover.yml').read_text()
        self.assertLess(workflow.index('name: Verify protected Chinese release after locale build'),
                        workflow.index('name: Restore approved extended candidates and assemble inactive tree'))
        self.assertIn('--active-state "$RUNNER_TEMP/previous-edge-state.json"', workflow)
        self.assertIn('Configure required reviewers before extended activation', workflow)
        self.assertIn("needs.extended_locales_approval.result == 'success'", workflow)
        self.assertIn("needs.prepare_release.outputs.extended_ready == 'true' && steps.extended_acceptance.outcome != 'success'", workflow)


if __name__ == '__main__':
    unittest.main()
