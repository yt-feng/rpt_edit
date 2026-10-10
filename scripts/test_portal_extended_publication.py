import copy
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest import mock

from build_portal_extended_locales import build
from portal_approved_quantity_contract import CONTRACT_ID, PARSER_SHA256, quantity_issues as frozen_quantity_issues
from portal_extended_locales import ORIGIN, ExpansionError, file_for_url, make_corpus, PublicParser, select_locales, digest
from portal_extended_publication import compose, checked_batches, read_active_batches, restore_active_checkpoint
from restore_assemble_portal_extended_r2 import restored_identity
from check_portal_extended_publication import StagingReplayStore, completed_candidates, snapshot_public
from audit_portal_extended_live import audit
from portal_extended_r2 import R2Store, R2IntegrityError, R2NotFound
from test_portal_extended_r2 import FakeR2
from test_portal_extended_locales import FakeTranslator
from test_portal_extended_incremental import daily_doc, raw_page, URL, DAY


class PublicationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.store = R2Store(FakeR2(), 'private-bucket', '_extended-locales/staging/publication')
        self.root = self.base/'site'; self.root.mkdir()
        assets = self.root/'assets'; assets.mkdir()
        # A production tree carries these established shared assets before
        # extended composition. Model that contract instead of an HTML-only tree.
        repository = Path(__file__).resolve().parent.parent
        for name in ('styles.css', 'blog.css', 'app.js', 'contact.js'):
            (assets/name).write_bytes((repository/'portal_suite/site_src/assets'/name).read_bytes())
        (assets/'locale.css').write_bytes((repository/'portal_suite/locale_assets/locale.css').read_bytes())
        # Exact source main/controls used by the established locale mirrors.
        homepage = (repository/'portal_suite/site_src/index.html').read_text()
        homepage = homepage.replace('<body data-page="index" data-analytics-auto="manual">', '<body>')
        (self.root/'index.html').write_text(homepage)
        (self.root/'robots.txt').write_text('User-agent: GPTBot\nDisallow: /\n')
        (self.root/'sitemap.xml').write_text('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc>'+ORIGIN+'/sitemap-pages.xml</loc></sitemap></sitemapindex>')
        self.number = 0
        self.approved_seeds = {}

    def candidate(self, locale='fr', url=URL):
        self.number += 1
        corpus = make_corpus([daily_doc(url)])
        work = self.base/str(self.number); work.mkdir()
        build(corpus, locale, work/'candidate', work/'checkpoint.json', FakeTranslator(), allow_source_fallback=True)
        generation = corpus['documents_sha256']
        self.store.put_source(corpus)
        seed = self.store.put_checkpoint(locale, generation, work/'checkpoint.json')
        saved = self.store.upload_candidate(work/'candidate', locale, generation)
        self.approved_seeds[generation, locale, saved['candidate_id']] = seed['sha256']
        target = self.root/file_for_url(url); target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw_page(url))
        return {'generation': generation, 'candidates': {locale: saved['candidate_id']}}

    def publish(self, batches):
        workspace = Path(tempfile.mkdtemp(dir=self.base))
        return compose(self.root, self.store, batches, workspace)

    def legacy_bn_candidate(self, *, current_rule=False):
        body = '<h1>Research</h1><p>政策利率上升'+('九成' if current_rule else '25个基点')+'。</p>'
        corpus = make_corpus([daily_doc(body=body)])
        self.number += 1
        work = self.base/str(self.number); work.mkdir()
        class Bengali:
            def translate(self, text, *args, **kwargs):
                return ('নীতিগত হার ৯০% বৃদ্ধি।' if '九成' in text else
                        'নীতিগত সুদের হার ২৫ বেসিস পয়েন্ট বেড়েছে।' if '25个基点' in text else 'গবেষণা তথ্য ও বিশ্লেষণ।')
        result = build(corpus, 'bn', work/'candidate', work/'checkpoint.json', Bengali(),
                       allow_source_fallback=True, quantity_validator=None if current_rule else frozen_quantity_issues)
        self.assertEqual(result['status'], 'complete-candidate')
        generation = corpus['documents_sha256']
        self.store.put_source(corpus); seed = self.store.put_checkpoint('bn', generation, work/'checkpoint.json')
        saved = self.store.upload_candidate(work/'candidate', 'bn', generation)
        self.approved_seeds[generation, 'bn', saved['candidate_id']] = seed['sha256']
        target = self.root/file_for_url(URL); target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw_page(body=body))
        return {'generation': generation, 'candidates': {'bn': saved['candidate_id']}}

    def active_ledger(self, batches):
        return {'schema_version':2, 'status':'assembled', 'batches': batches,
                'replays': [{'approved_generation': batch['generation'], 'locale': locale,
                             'approved_candidate': candidate,
                             'checkpoint_sha256': self.approved_seeds[batch['generation'], locale, candidate]}
                            for batch in batches for locale, candidate in batch['candidates'].items()]}

    def publish_frozen(self, batch, *, ledger=None):
        identity = {'slot': 'a', 'release_id': 'a'*32, 'tree_sha256': 'b'*64}
        workspace = Path(tempfile.mkdtemp(dir=self.base))
        with mock.patch('portal_extended_publication.read_active_ledger', return_value=ledger or self.active_ledger([batch])) as reader:
            result = compose(self.root, self.store, [batch], workspace, active_identity=identity)
        reader.assert_called_once_with(self.store, identity)
        return result

    def test_authenticated_legacy_bn_candidate_replays_exact_bytes_without_calls(self):
        batch = self.legacy_bn_candidate()
        result = self.publish_frozen(batch)
        self.assertTrue(result['ready']); self.assertEqual(result['page_counts'], {'bn': 1})
        self.assertEqual(result['replays'][0]['translation_calls'], 0)
        self.assertEqual(result['replays'][0]['quantity_contract'], CONTRACT_ID)
        self.assertEqual(result['replays'][0]['quantity_parser_sha256'], PARSER_SHA256)
        self.assertIn('২৫ বেসিস পয়েন্ট', (self.root/'bn'/file_for_url(URL)).read_text())

    def test_active_approval_ignores_changed_latest_and_reuses_original_seed(self):
        batch = self.candidate(); ledger = self.active_ledger([batch])
        original_sha = ledger['replays'][0]['checkpoint_sha256']
        latest = self.base/'changed-latest.json'
        self.store.restore_checkpoint('fr', batch['generation'], latest)
        value = json.loads(latest.read_bytes())
        next(iter(value['rows'].values()))['text'] = 'Autre traduction valide et privée.'
        latest.write_text(json.dumps(value)); self.store.put_checkpoint('fr', batch['generation'], latest)
        with mock.patch.object(self.store, 'restore_checkpoint', side_effect=AssertionError('Active must not follow latest')):
            result = self.publish_frozen(batch, ledger=ledger)
        replay = result['replays'][0]
        self.assertEqual(replay['checkpoint_sha256'], original_sha)
        self.assertEqual(replay['checkpoint_binding'], 'authenticated-active-ledger')
        self.assertEqual(replay['translation_calls'], 0)
        self.assertNotIn('Autre traduction', (self.root/'fr'/file_for_url(URL)).read_text())

    def test_active_checkpoint_receipt_is_unique_and_exact_not_replay_output_identity(self):
        batch = self.candidate(); original = self.active_ledger([batch])
        wrong = copy.deepcopy(original)
        wrong['replays'][0]['source_generation'] = batch['generation']
        wrong['replays'][0]['candidate_id'] = batch['candidates']['fr']
        wrong['replays'][0]['approved_generation'] = 'e'*64
        cases = [dict(batches=[batch]), {**original, 'replays':[]},
                 {**original, 'replays':original['replays']*2}, wrong]
        for field, value in (('locale','de'), ('approved_candidate','f'*64), ('checkpoint_sha256',None),
                             ('checkpoint_sha256','../bad'), ('checkpoint_sha256',int('1'*64))):
            changed = copy.deepcopy(original); changed['replays'][0][field] = value; cases.append(changed)
        for index, ledger in enumerate(cases):
            with self.subTest(index=index), mock.patch.object(self.store, '_get') as get:
                with self.assertRaises(ExpansionError):
                    restore_active_checkpoint(self.store, ledger, 'fr', batch['generation'],
                                              batch['candidates']['fr'], self.base/f'invalid-{index}.json')
            get.assert_not_called()

    def test_pinned_checkpoint_missing_cannot_fall_back_to_valid_latest(self):
        batch = self.candidate(); ledger = self.active_ledger([batch])
        ledger['replays'][0]['checkpoint_sha256'] = 'f'*64
        with mock.patch.object(self.store, 'restore_checkpoint', side_effect=AssertionError('No latest fallback')):
            with self.assertRaises(R2NotFound): self.publish_frozen(batch, ledger=ledger)
        self.assertFalse((self.root/'fr').exists())

    def test_pinned_checkpoint_hash_not_storage_metadata_is_authority(self):
        batch = self.candidate(); ledger = self.active_ledger([batch]); row = ledger['replays'][0]
        key = self.store.checkpoint_object_key('fr', batch['generation'], row['checkpoint_sha256'])
        value = self.store.client.objects[key]; changed = value['body'] + b' '
        value.update(body=changed, ContentLength=len(changed), Metadata={'sha256':digest(changed)})
        with self.assertRaisesRegex(ExpansionError, 'checkpoint checksum differs'):
            self.publish_frozen(batch, ledger=ledger)
        self.assertFalse((self.root/'fr').exists())

    def test_pinned_checkpoint_identity_is_checked_even_with_matching_content_hash(self):
        batch = self.candidate(); ledger = self.active_ledger([batch]); row = ledger['replays'][0]
        key = self.store.checkpoint_object_key('fr', batch['generation'], row['checkpoint_sha256'])
        original = json.loads(self.store.client.objects[key]['body'])
        for field, wrong in (('locale','de'), ('model','different'), ('version','different'),
                             ('source_generation','f'*64)):
            with self.subTest(field=field):
                changed = {**original, field:wrong}; raw = json.dumps(changed).encode(); checksum = digest(raw)
                self.store._put(self.store.checkpoint_object_key('fr',batch['generation'],checksum),raw,metadata={'kind':'test'})
                altered = copy.deepcopy(ledger); altered['replays'][0]['checkpoint_sha256'] = checksum
                with self.assertRaises(R2IntegrityError): self.publish_frozen(batch,ledger=altered)
        self.assertFalse((self.root/'fr').exists())

    def test_exact_active_pin_survives_second_publication_generation(self):
        batch = self.candidate(); ledger = self.active_ledger([batch])
        first = self.publish_frozen(batch, ledger=ledger)
        (self.root/'data/extended-locales/assembly.json').unlink()
        second = self.publish_frozen(batch, ledger=first)
        for result in (first, second):
            row = result['replays'][0]
            self.assertEqual(row['approved_generation'], batch['generation'])
            self.assertEqual(row['approved_candidate'], batch['candidates']['fr'])
            self.assertEqual(row['checkpoint_sha256'], ledger['replays'][0]['checkpoint_sha256'])
            self.assertEqual(result['batches'], [batch])
            self.assertEqual(result['page_counts'], {'fr':1})

    def test_fully_superseded_active_tuple_does_not_require_unused_seed(self):
        old = self.candidate(); new = self.candidate()
        # Same source+candidate can deduplicate; use a current-code new candidate
        # with a distinct valid translation to exercise the owner override.
        from test_portal_extended_locales import FakeTranslator
        class Different(FakeTranslator):
            def translate(self, *args, **kwargs): return super().translate(*args, **kwargs)+' nouveau'
        corpus = make_corpus([daily_doc()]); work=self.base/'replacement'; work.mkdir()
        build(corpus,'fr',work/'candidate',work/'checkpoint.json',Different(),allow_source_fallback=True)
        self.store.put_checkpoint('fr',corpus['documents_sha256'],work/'checkpoint.json')
        saved=self.store.upload_candidate(work/'candidate','fr',corpus['documents_sha256'])
        new={'generation':corpus['documents_sha256'],'candidates':{'fr':saved['candidate_id']}}
        with mock.patch('portal_extended_publication.read_active_ledger',return_value={'batches':[old]}):
            result=compose(self.root,self.store,[old,new],Path(tempfile.mkdtemp(dir=self.base)),active_identity={'slot':'a'})
        self.assertEqual(result['batches'],[old,new]); self.assertEqual(len(result['replays']),1)
        self.assertEqual(result['replays'][0]['approved_candidate'],new['candidates']['fr'])
        self.assertEqual(result['replays'][0]['checkpoint_binding'],'incoming-exact-byte-replay')

    def test_partially_superseded_active_tuple_still_requires_exact_seed_receipt(self):
        other = ORIGIN+'/blog/20260925-other.html'
        corpus = make_corpus([daily_doc(), daily_doc(other)])
        work = self.base/'two-approved'; work.mkdir()
        build(corpus,'fr',work/'candidate',work/'checkpoint.json',FakeTranslator(),allow_source_fallback=True)
        generation = corpus['documents_sha256']; self.store.put_source(corpus)
        self.store.put_checkpoint('fr',generation,work/'checkpoint.json')
        candidate = self.store.upload_candidate(work/'candidate','fr',generation)['candidate_id']
        old = {'generation':generation,'candidates':{'fr':candidate}}
        path = self.root/file_for_url(other); path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(raw_page(other))
        incoming = self.candidate()
        before = {p.relative_to(self.root):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        with mock.patch('portal_extended_publication.read_active_ledger',return_value={'batches':[old],'replays':[]}):
            with self.assertRaisesRegex(ExpansionError, 'one exact checkpoint receipt'):
                compose(self.root,self.store,[old,incoming],Path(tempfile.mkdtemp(dir=self.base)),active_identity={'slot':'a'})
        self.assertEqual(before,{p.relative_to(self.root):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_current_rule_approved_candidate_stays_publishable_after_becoming_active(self):
        batch = self.legacy_bn_candidate(current_rule=True)
        result = self.publish_frozen(batch)
        self.assertTrue(result['ready'])
        self.assertEqual(result['replays'][0]['quantity_contract'], 'current')
        self.assertEqual(result['replays'][0]['translation_calls'], 0)
        self.assertIn('৯০%', (self.root/'bn'/file_for_url(URL)).read_text())

    def test_unapproved_incoming_candidate_keeps_current_numeric_gate(self):
        batch = self.legacy_bn_candidate()
        with self.assertRaisesRegex(ExpansionError, 'approved candidate bytes'): self.publish([batch])
        self.assertFalse((self.root/'bn').exists())

    def test_incoming_cannot_forge_an_active_approval_quantity_contract(self):
        active = self.candidate('fr', url=ORIGIN+'/blog/20260925-active.html')
        incoming = self.legacy_bn_candidate()
        incoming['quantity_contract'] = CONTRACT_ID
        incoming['checkpoint_sha256'] = self.active_ledger([active])['replays'][0]['checkpoint_sha256']
        identity = {'slot': 'a', 'release_id': 'a'*32, 'tree_sha256': 'b'*64}
        with mock.patch('portal_extended_publication.read_active_ledger', return_value=self.active_ledger([active])):
            with self.assertRaisesRegex(ExpansionError, 'approved candidate bytes'):
                compose(self.root, self.store, [active, incoming], Path(tempfile.mkdtemp(dir=self.base)), active_identity=identity)
        self.assertFalse((self.root/'bn').exists())

    def test_candidate_integrity_failure_is_not_a_parser_fallback(self):
        batch = self.legacy_bn_candidate()
        with mock.patch.object(self.store, 'restore_candidate', side_effect=R2IntegrityError('Candidate bytes differ')), \
             mock.patch('portal_extended_publication.prove_approved_baseline') as proof:
            with self.assertRaisesRegex(R2IntegrityError, 'Candidate bytes differ'): self.publish_frozen(batch)
            proof.assert_not_called()

    def test_frozen_approval_rejects_changed_real_number_and_changed_words(self):
        for text in ('নীতিগত সুদের হার ২৬ বেসিস পয়েন্ট বেড়েছে।', 'ভিন্ন অনুমোদন ২৫ বেসিস পয়েন্ট।'):
            with self.subTest(text=text):
                batch = self.legacy_bn_candidate()
                path = self.base/'poisoned.json'; self.store.restore_checkpoint('bn', batch['generation'], path)
                seed = json.loads(path.read_bytes())
                row = next(row for row in seed['rows'].values() if '25个基点' in row['source']); row['text'] = text
                path.write_text(json.dumps(seed)); changed = self.store.put_checkpoint('bn', batch['generation'], path)
                ledger = self.active_ledger([batch]); ledger['replays'][0]['checkpoint_sha256'] = changed['sha256']
                with self.assertRaisesRegex(ExpansionError, 'approved candidate bytes'): self.publish_frozen(batch, ledger=ledger)
                self.assertFalse((self.root/'bn').exists())

    def test_current_replay_seed_contains_only_units_proved_against_approved_html(self):
        batch = self.legacy_bn_candidate()
        path = self.base/'extra.json'; self.store.restore_checkpoint('bn', batch['generation'], path)
        seed = json.loads(path.read_bytes())
        seed['rows']['f'*64] = {'source': 'Unapproved extra source.', 'language': 'en', 'text': 'নতুন অগ্রহণযোগ্য লেখা।'}
        seed.setdefault('source_fallbacks', {})['e'*64] = {'source': 'Unapproved fallback.', 'language': 'en',
            'policy': 'exact-source-v1', 'code': 'financial-quantity-validation'}
        path.write_text(json.dumps(seed)); saved = self.store.put_checkpoint('bn', batch['generation'], path)
        ledger = self.active_ledger([batch]); ledger['replays'][0]['checkpoint_sha256'] = saved['sha256']
        with mock.patch('portal_extended_publication.build', wraps=build) as builder:
            self.publish_frozen(batch, ledger=ledger)
        used_seed = json.loads(next(call for call in builder.call_args_list if call.args[2].name == 'current').kwargs['seed_checkpoint'].read_bytes())
        self.assertNotIn('f'*64, used_seed['rows'])
        self.assertNotIn('e'*64, used_seed.get('source_fallbacks', {}))
        self.assertTrue(all('Unapproved extra' not in row['source'] for row in used_seed['rows'].values()))

    def test_frozen_content_change_is_rejected_even_with_extra_latest_units(self):
        batch = self.legacy_bn_candidate()
        checkpoint = self.base/'changed-extra.json'
        self.store.restore_checkpoint('bn', batch['generation'], checkpoint)
        seed = json.loads(checkpoint.read_bytes())
        seed['rows']['f'*64] = {'source': '政策利率上升26个基点。', 'language': 'zh',
                               'text': 'নীতিগত সুদের হার ২৬ বেসিস পয়েন্ট বেড়েছে।'}
        checkpoint.write_text(json.dumps(seed)); self.store.put_checkpoint('bn', batch['generation'], checkpoint)
        path = self.root/file_for_url(URL); path.write_bytes(path.read_bytes().replace('25个基点'.encode(), '26个基点'.encode()))
        with self.assertRaisesRegex(ExpansionError, 'source content changed'): self.publish_frozen(batch)
        self.assertFalse((self.root/'bn').exists())

    def test_frozen_contract_requires_authenticated_active_ledger_and_exact_prefix(self):
        batch = self.legacy_bn_candidate()
        with mock.patch('portal_extended_publication.read_active_ledger', side_effect=RuntimeError('Pinned identity differs')):
            with self.assertRaisesRegex(RuntimeError, 'Pinned identity'): compose(self.root,self.store,[batch],self.base/'missing',active_identity={'slot':'a'})
        other = {'generation': 'c'*64, 'candidates': {'bn': 'd'*64}}
        with mock.patch('portal_extended_publication.read_active_ledger', return_value={'batches':[other]}):
            with self.assertRaisesRegex(ExpansionError, 'retained exactly'): compose(self.root,self.store,[batch],self.base/'missing',active_identity={'slot':'a'})

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
        self.assertTrue((self.root/'fr/index.html').is_file())
        homepage = (self.root/'fr/index.html').read_text()
        self.assertIn('lang="fr"', homepage)
        self.assertIn('/fr/blog/20260925-new.html', homepage)
        self.assertNotIn('noindex', homepage)
        self.assertIn('Disallow: /', (self.root/'robots.txt').read_text())
        self.assertNotIn('sitemap-extended.xml', (self.root/'sitemap.xml').read_text())
        self.assertIn('sitemap-extended-fr.xml', (self.root/'sitemap.xml').read_text())
        self.assertIn('sitemap-pages.xml', (self.root/'sitemap.xml').read_text())
        page = (self.root/'fr'/file_for_url(URL)).read_text()
        self.assertIn('index,follow', page)
        self.assertNotIn('noindex', page)

    def test_all_33_namespaces_compose_without_english_and_with_real_homepages(self):
        locales = select_locales('all-supported')
        result = self.publish([self.candidate(locale) for locale in locales])
        self.assertEqual(len(result['locales']), 33)
        self.assertEqual(result['page_counts'], dict.fromkeys(locales, 1))
        self.assertTrue(all(row['translation_calls'] == 0 for row in result['replays']))
        self.assertFalse((self.root/'en').exists())
        sitemap = ET.fromstring((self.root/'sitemap.xml').read_bytes())
        locations = [node.text for node in sitemap.findall('{*}sitemap/{*}loc')]
        self.assertEqual(len(locations), len(set(locations)))
        self.assertEqual(set(locations), {ORIGIN+'/sitemap-pages.xml'} | {
            ORIGIN+f'/sitemap-extended-{locale}.xml' for locale in locales})
        for locale in locales:
            shard = ET.fromstring((self.root/f'sitemap-extended-{locale}.xml').read_bytes())
            self.assertEqual(shard.tag.rsplit('}', 1)[-1], 'urlset')
        for locale in locales:
            parser = PublicParser()
            parser.feed((self.root/locale/file_for_url(URL)).read_text()); parser.close()
            self.assertEqual(parser.content_lang, locale)
            self.assertNotIn('noindex', parser.metadata.get('robots', ''))
            homepage = self.root/locale/'index.html'
            self.assertTrue(homepage.is_file())
            self.assertIn(f'lang="{locale}"', homepage.read_text())
        self.assertNotIn('/en/', '\n'.join(str(path) for path in self.root.rglob('*')))

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

    def test_legacy_nested_sitemap_is_repaired_without_losing_base_metadata(self):
        batch = self.candidate()
        path = self.root/'sitemap.xml'
        path.write_text(path.read_text().replace('</sitemapindex>',
            '<sitemap><loc>'+ORIGIN+'/sitemap-extended.xml</loc></sitemap>'
            '<sitemap><loc>'+ORIGIN+'/sitemap-extended-fr.xml</loc></sitemap>'
            '<sitemap><loc>'+ORIGIN+'/sitemap-extended-fr.xml</loc></sitemap>'
            '<sitemap><loc>'+ORIGIN+'/sitemap-extended-pt.xml</loc></sitemap>'
            '</sitemapindex>').replace('sitemap-pages.xml</loc>',
            'sitemap-pages.xml</loc><lastmod>2026-09-30</lastmod>'))
        self.publish([batch])
        root = ET.fromstring(path.read_bytes())
        self.assertEqual([node.text for node in root.findall('{*}sitemap/{*}loc')],
            [ORIGIN+'/sitemap-pages.xml', ORIGIN+'/sitemap-extended-fr.xml'])
        self.assertEqual(root.find('{*}sitemap/{*}lastmod').text, '2026-09-30')
        # Robots can advertise an independent index; root indexes stay flat.
        self.assertIn('Sitemap: '+ORIGIN+'/sitemap-extended.xml',
            (self.root/'robots.txt').read_text())

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
        without_ui = {name: item for name, item in files.items() if name != 'assets/extended-locales.css'}
        with self.assertRaisesRegex(RuntimeError, 'UI asset is missing'):
            verify_extended_static_tree(client, 'bucket', 'slot/', without_ui, origin=ORIGIN)
        asset = client.objects['slot/assets/extended-locales.js']
        original = asset['body']
        asset['body'] = b'x' * len(original)
        with self.assertRaisesRegex(RuntimeError, 'content differs'):
            verify_extended_static_tree(client, 'bucket', 'slot/', files, origin=ORIGIN)
        asset['body'] = original
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

    def test_live_audit_checks_real_homepage_and_detail_urls(self):
        self.publish([self.candidate()])
        seen = []
        def response(url, **kwargs):
            seen.append(url)
            relative = url.removeprefix(ORIGIN+'/')
            if relative.endswith('/'):
                relative += 'index.html'
            page = self.root/relative
            return mock.Mock(status_code=200 if page.is_file() else 404,
                headers={'Content-Language':'fr', 'X-Robots-Tag':'', 'Content-Type':'text/css' if relative.endswith('.css') else 'text/html'}, content=page.read_bytes() if page.is_file() else b'')
        with mock.patch('requests.Session') as session:
            session.return_value.get.side_effect = response
            report = audit(ORIGIN, 'fr', require_standard_ui=True)
            self.assertEqual(report['status'], 'passed')
            self.assertEqual(report['reports'][0]['pages'], 1)
            self.assertIn(ORIGIN+'/fr/', seen)
            self.assertIn(ORIGIN+'/assets/extended-locales.css', seen)
            (self.root/'assets/extended-locales.css').unlink()
            with self.assertRaisesRegex(ExpansionError, 'HTTP 404'):
                audit(ORIGIN, 'fr', require_standard_ui=True)

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
