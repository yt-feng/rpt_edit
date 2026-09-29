import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from build_portal_extended_locales import build
from portal_extended_locales import ORIGIN, ExpansionError, file_for_url, make_corpus, PublicParser, select_locales
from portal_extended_publication import compose, checked_batches, read_active_batches
from restore_assemble_portal_extended_r2 import restored_identity
from check_portal_extended_publication import StagingReplayStore, completed_candidates, snapshot_public
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
        build(corpus, locale, work/'candidate', work/'checkpoint.json', FakeTranslator(), allow_source_fallback=True)
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

    def test_all_33_namespaces_compose_without_english_or_fabricated_homepages(self):
        locales = select_locales('all-supported')
        result = self.publish([self.candidate(locale) for locale in locales])
        self.assertEqual(len(result['locales']), 33)
        self.assertEqual(result['page_counts'], dict.fromkeys(locales, 1))
        self.assertTrue(all(row['translation_calls'] == 0 for row in result['replays']))
        self.assertFalse((self.root/'en').exists())
        for locale in locales:
            parser = PublicParser()
            parser.feed((self.root/locale/file_for_url(URL)).read_text()); parser.close()
            self.assertEqual(parser.content_lang, locale)
            self.assertNotIn('noindex', parser.metadata.get('robots', ''))
            self.assertFalse((self.root/locale/'index.html').exists())

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

    def test_restored_uploaded_release_preserves_identity_without_writes(self):
        batches = [self.candidate(), self.candidate('pt')]
        original = self.publish(batches)
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        recovered = restored_identity(self.root)
        for key in ('locales', 'candidate_ids', 'source_generation', 'page_counts', 'pages_per_locale'):
            self.assertEqual(recovered[key], original[key])
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_restored_identity_rejects_incomplete_or_mismatched_ledger(self):
        self.assertFalse(restored_identity(self.root)['ready'])
        self.publish([self.candidate()])
        path = self.root/'data/extended-locales/assembly.json'
        valid = json.loads(path.read_text())
        for changes in ({'status':'incomplete'}, {'locales':['en']}, {'page_counts':{'fr':0}}):
            path.write_text(json.dumps({**valid, **changes}))
            with self.assertRaises(ExpansionError):
                restored_identity(self.root)

    def test_committed_extended_paths_are_validated_as_locale_plus_public_source(self):
        from test_publish_static_slot import FakeR2 as SlotClient
        from publish_static_slot import build_inventory, upload_extra_args
        from verify_prepared_static_slot import verify_extended_static_tree
        self.publish([self.candidate(), self.candidate(url=ORIGIN+'/blog/20260925-other.html'),
                      self.candidate(url=ORIGIN+'/blog/20260925-z-final.html')])
        paths, files, _tree, _size = build_inventory(self.root)
        client = SlotClient()
        for name, path in paths.items():
            client.upload_file(str(path), 'bucket', 'slot/'+name, ExtraArgs=upload_extra_args(files[name]))
        from concurrent.futures import ThreadPoolExecutor
        with mock.patch('verify_prepared_static_slot.ThreadPoolExecutor', wraps=ThreadPoolExecutor) as executor:
            result = verify_extended_static_tree(client, 'bucket', 'slot/', files, origin=ORIGIN)
            executor.assert_called_once_with(max_workers=4)
        self.assertEqual(result['locales'], ['fr'])
        for name in ('new', 'other', 'z-final'):
            self.assertIn(('get', f'slot/fr/blog/20260925-{name}.html'), client.operations)
        # A corrupt middle page must fail too, even when both endpoint samples
        # are valid. Full pre-cutover verification is never reduced to samples.
        entry = client.objects['slot/fr/blog/20260925-other.html']
        entry['body'] = b'x' * len(entry['body'])
        with self.assertRaisesRegex(RuntimeError, 'content differs'):
            verify_extended_static_tree(client, 'bucket', 'slot/', files, origin=ORIGIN)

    def test_publication_check_writes_only_staging_and_requires_complete_receipts(self):
        from portal_extended_incremental import remember_candidate
        batch = self.candidate()
        corpus = make_corpus([daily_doc()])
        with self.assertRaisesRegex(ExpansionError, 'receipt is absent'):
            completed_candidates(self.store, corpus, ('fr',))
        remember_candidate(self.store, 'fr', corpus, self.base/'1/candidate')
        self.assertEqual(completed_candidates(self.store, corpus, ('fr',)), batch)
        original = copy.deepcopy(self.store.client.objects)
        staging = R2Store(self.store.client, self.store.bucket, '_extended-locales/staging/publication-123-1')
        work = self.base/'staging-check'; work.mkdir()
        result = compose(self.root, StagingReplayStore(self.store, staging), [batch], work)
        self.assertEqual(result['replays'][0]['translation_calls'], 0)
        for key, value in original.items():
            self.assertEqual(self.store.client.objects[key], value)
        self.assertTrue(all(key.startswith(staging.prefix+'/') for key in self.store.client.objects.keys()-original.keys()))
        with self.assertRaises(ExpansionError):
            StagingReplayStore(self.store, self.store)

    def test_publication_snapshot_is_bounded_to_exact_source_and_legacy_routes(self):
        corpus = make_corpus([daily_doc()])
        seen = []
        def response(url, **kwargs):
            seen.append(url)
            self.assertFalse(kwargs['allow_redirects'])
            result = mock.MagicMock()
            result.status_code = 404 if '/ko/' in url else 200
            result.iter_content.return_value = iter([b'public snapshot'])
            result.__enter__.return_value = result
            return result
        session = mock.Mock(); session.get.side_effect = response
        count = snapshot_public(session, self.root, corpus)
        self.assertEqual(count, 6)
        self.assertEqual(len(seen), 7)
        self.assertEqual((self.root/'robots.txt').read_bytes(), b'public snapshot')
        self.assertFalse((self.root/'ko/blog/20260925-new.html').exists())
        self.assertTrue((self.root/'ja/blog/20260925-new.html').exists())

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
