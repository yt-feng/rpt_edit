"""Synthetic private/public release, approval and rollback contracts."""
import copy
from contextlib import chdir
import io
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
from unittest import mock

from portal_english_commentary import POLICY, build
from portal_english_handoff import next_ready, read_handoff, verify_handoff
from portal_english_publication import (ASSEMBLY, NS, bind_release, checked_assembly, checked_batches, audit_live, preflight_api,
                                       compose, read_active, read_ledger, read_static_assembly, recover_prepared, verify_prepared_ledger)
from portal_extended_locales import ExpansionError, ORIGIN, digest, stable_bytes
from portal_extended_r2 import R2NotFound, R2PermissionError
from publish_static_slot import manifest_key, slot_prefix
from verify_prepared_static_slot import static_tree_sha256
from review_portal_english_handoff import approval_is_valid, producer_is_valid, review_identity
import test_portal_english_pipeline as fixtures
from test_portal_english_pipeline import CPU_PRODUCER, SOURCE_PRODUCER
from test_portal_english_commentary import DAY, SyntheticTranslator, page


class EnglishPublicationTests(unittest.TestCase):
    def setUp(self):
        self.engine = fixtures.EnglishPipelineTests(); self.engine.setUp(); self.addCleanup(self.engine.tearDown)
        original_get = self.engine.client.get_object
        def streaming_get(**kwargs):
            value = original_get(**kwargs)
            return {**value, 'Body': io.BytesIO(value['Body'].body)}
        stream_patch = mock.patch.object(self.engine.client, 'get_object', side_effect=streaming_get)
        stream_patch.start(); self.addCleanup(stream_patch.stop)
        self.base = self.engine.root; self.store = self.engine.store; self.original = self.engine.original
        self.counter = 0; self.root = self.fresh_tree()

    def fresh_tree(self):
        self.counter += 1; root = self.base/f'site-{self.counter}'; root.mkdir()
        (root/'index.html').write_text('<html><head></head><body><nav class="topbar-actions">中文原首页</nav></body></html>')
        (root/'robots.txt').write_text('User-agent: GPTBot\nDisallow: /\nUser-agent: *\nAllow: /\n')
        (root/'sitemap.xml').write_text(f'<sitemapindex xmlns="{NS}"><sitemap><loc>{ORIGIN}/sitemap-pages.xml</loc></sitemap>'
                                       f'<sitemap><loc>{ORIGIN}/sitemap-extended-fr.xml</loc></sitemap></sitemapindex>')
        assets = root/'assets'; assets.mkdir()
        source = Path(__file__).resolve().parents[1]/'portal_suite/site_src/assets'
        for name in ('styles.css', 'blog.css', 'app.js'):
            (assets/name).write_bytes((source/name).read_bytes())
        return root

    def candidate(self, day=DAY):
        self.engine.admit(1, day); prepared, source, directory, _, _ = self.engine.build_candidate()
        from portal_english_pipeline import persist_candidate
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        doc = source['documents'][0]; path = self.root/'blog'/f'{doc["id"]}.html'
        path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(page(url=doc['source_url'], day=source['day']))
        return {'generation': source['generation'], 'candidate_id': saved['candidate_id']}

    def assemble(self, batches, active=None):
        return compose(self.root, self.store, self.original, active, batches, self.base/f'work-{self.counter}')

    def pin(self, slot='a', release='a'*32):
        files = {}
        for path in self.root.rglob('*'):
            if not path.is_file(): continue
            relative = path.relative_to(self.root).as_posix(); raw = path.read_bytes()
            files[relative] = {'sha256': digest(raw), 'size': len(raw)}
            self.store._put(slot_prefix(slot)+relative, raw, metadata={'kind': 'synthetic-static'})
        tree = static_tree_sha256(files)
        manifest = {'schema_version': 1, 'slot': slot, 'release_id': release, 'tree_sha256': tree,
                    'files': files, 'file_count': len(files), 'total_bytes': sum(row['size'] for row in files.values())}
        self.store._put(manifest_key(slot), stable_bytes(manifest), metadata={'kind': 'synthetic-manifest'})
        return {'slot': slot, 'release_id': release, 'tree_sha256': tree}

    def first_live(self):
        batch = self.candidate(); result = self.assemble([batch]); identity = self.pin()
        bind_release(self.store, identity, None, approved_ledger=result['ledger_sha256'])
        return batch, identity, read_active(self.store, identity)

    def test_publication_is_preview_only_and_preserves_root_languages_and_training_policy(self):
        batch = self.candidate(); robots = (self.root/'robots.txt').read_bytes()
        result = self.assemble([batch]); self.assertTrue(result['ready']); self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['page_count'], 1); self.assertFalse(result['deployed'])
        self.assertEqual((self.root/'robots.txt').read_bytes(), robots)
        for path in (self.root/'en').rglob('*'):
            if not path.is_file(): continue
            raw = path.read_text()
            self.assertIn('index,follow', raw); self.assertNotIn('noindex', raw)
            for prohibited in ['SECRET', 'Next, watch actual deliveries.', 'body_sha256', '原始', '<img', '<table', 'articleBody']:
                self.assertNotIn(prohibited, raw)
        self.assertFalse((self.root/'en/reports').exists()); self.assertFalse((self.root/'en/charts.html').exists())
        self.assertFalse((self.root/'private').exists())
        sitemap = ET.fromstring((self.root/'sitemap.xml').read_bytes())
        self.assertEqual({node.text for node in sitemap.findall(f'.//{{{NS}}}loc')},
                         {ORIGIN+'/sitemap-pages.xml', ORIGIN+'/sitemap-extended-fr.xml', ORIGIN+'/sitemap-en.xml'})
        self.assertIn('中文原首页', (self.root/'index.html').read_text())
        self.assertIn('data-english-commentary-link', (self.root/'index.html').read_text())
        self.assertFalse(any('/releases/' in key for key in self.engine.client.objects))

    def test_current_homepage_div_navigation_accepts_approved_english(self):
        batch = self.candidate()
        homepage = (Path(__file__).resolve().parents[1]/'portal_suite/site_src/index.html').read_text()
        self.assertIn('<div class="topbar-actions">', homepage)
        (self.root/'index.html').write_text(homepage)
        result = self.assemble([batch])
        self.assertTrue(result['ready'])
        updated = (self.root/'index.html').read_text()
        anchor = '<a class="topbar-link" data-english-commentary-link href="/en/">English commentary</a>'
        self.assertEqual(updated.count(anchor), 1)
        self.assertEqual(updated.replace(anchor, ''), homepage)

    def test_navigation_class_tokens_quotes_and_ambiguous_boundaries(self):
        batch = self.candidate()
        source = next((self.root/'blog').glob('*.html'))
        source_name, source_bytes = source.name, source.read_bytes()
        def fresh_source_tree():
            self.root = self.fresh_tree(); (self.root/'blog').mkdir()
            (self.root/'blog'/source_name).write_bytes(source_bytes)
        for boundary in ("<div class='wide topbar-actions compact'>", '<nav class="compact topbar-actions">'):
            with self.subTest(boundary=boundary):
                fresh_source_tree()
                (self.root/'index.html').write_text(boundary+'Existing navigation</'+('div' if boundary.startswith('<div') else 'nav')+'>')
                self.assertTrue(self.assemble([batch])['ready'])
                self.assertIn(boundary+'<a class="topbar-link" data-english-commentary-link', (self.root/'index.html').read_text())
        for boundary in ('<div class="topbar-actions-copy"></div>', '<div>Missing</div>',
                         '<div data-class="topbar-actions"></div>',
                         '<div aria-class="topbar-actions"></div>',
                         '''<div title=" class='topbar-actions'"></div>''',
                         '<div class="topbar-actions" class="other"></div>',
                         '<div class="other" class="topbar-actions"></div>',
                         '<nav class="topbar-actions"></nav><div class="topbar-actions"></div>'):
            with self.subTest(boundary=boundary):
                fresh_source_tree()
                (self.root/'index.html').write_text(boundary)
                stored = copy.deepcopy(self.engine.client.objects)
                with self.assertRaisesRegex(ExpansionError, 'navigation boundary'):
                    self.assemble([batch])
                self.assertEqual(self.engine.client.objects, stored)
                self.assertEqual((self.root/'index.html').read_text(), boundary)
                self.assertFalse((self.root/'en').exists())

    def test_prepared_english_has_no_read_authority_until_exact_protected_version_binding(self):
        batch = self.candidate(); result = self.assemble([batch]); identity = self.pin()
        self.assertEqual(read_static_assembly(self.store, identity)['page_count'], 1)
        with self.assertRaises(R2NotFound): read_active(self.store, identity)
        with self.assertRaises(ExpansionError): bind_release(self.store, identity, None)
        with self.assertRaises(ExpansionError): bind_release(self.store, identity, None, approved_ledger='f'*64)
        bind_release(self.store, identity, None, approved_ledger=result['ledger_sha256'])
        self.assertEqual(read_active(self.store, identity)['ledger_sha256'], result['ledger_sha256'])

    def test_new_batch_preserves_approved_old_pages_and_rolls_back_the_whole_english_version(self):
        old, previous_identity, active = self.first_live()
        old_ledger = read_ledger(self.store, active['ledger_sha256'])
        self.root = self.fresh_tree(); new = self.candidate('2026-10-02'); result = self.assemble([old, new], active)
        self.assertEqual(result['page_count'], 2)
        identity = self.pin('b', 'b'*32)
        with self.assertRaises(ExpansionError): bind_release(self.store, identity, previous_identity)
        bind_release(self.store, identity, previous_identity, approved_ledger=result['ledger_sha256'])
        self.assertEqual(read_active(self.store, identity)['page_count'], 2)
        restored = read_active(self.store, previous_identity)
        self.assertEqual(restored, active); self.assertEqual(read_ledger(self.store, restored['ledger_sha256']), old_ledger)
        self.assertTrue(all((self.root/'en/blog'/f'{item["id"]}.html').is_file()
                            for item in read_ledger(self.store, result['ledger_sha256'])['items']))

    def test_normal_refresh_carries_approved_english_without_new_inference_or_approval(self):
        batch, previous_identity, active = self.first_live()
        self.root = self.fresh_tree(); result = self.assemble([batch], active)
        self.assertEqual(result['ledger_sha256'], active['ledger_sha256'])
        identity = self.pin('b', 'b'*32); bind_release(self.store, identity, previous_identity)
        self.assertEqual(read_active(self.store, identity)['batches'], [batch])

    def test_new_source_comment_change_rejects_candidate_but_navigation_changes_do_not(self):
        batch = self.candidate(); original = next((self.root/'blog').glob('*.html'))
        original.write_bytes(original.read_bytes().replace(b'</head>', b'<meta name="build" content="changed"></head>'))
        self.assertTrue(self.assemble([batch])['ready'])
        self.root = self.fresh_tree()
        path = self.root/'blog'/original.name; path.parent.mkdir(); path.write_bytes(original.read_bytes().replace('下一步应关注实际交付。'.encode(), '我的判断已经变化。'.encode()))
        with self.assertRaises(ExpansionError): self.assemble([batch])
        self.assertFalse((self.root/'en').exists())

    def test_public_namespace_symlink_and_missing_navigation_are_not_overwritten(self):
        batch = self.candidate(); (self.root/'en').mkdir(); (self.root/'en/keep').write_text('user content')
        with self.assertRaises(ExpansionError): self.assemble([batch])
        self.assertEqual((self.root/'en/keep').read_text(), 'user content')
        self.root = self.fresh_tree(); (self.root/'en').symlink_to(self.base, target_is_directory=True)
        with self.assertRaises(ExpansionError): self.assemble([batch])

    def test_missing_private_body_or_storage_permissions_cannot_bind_or_activate(self):
        batch = self.candidate(); result = self.assemble([batch]); identity = self.pin()
        item = read_ledger(self.store, result['ledger_sha256'])['items'][0]
        key = self.store.key('bodies', item['body_sha256']+'.json'); saved = self.engine.client.objects.pop(key)
        with self.assertRaises(R2NotFound): bind_release(self.store, identity, None, approved_ledger=result['ledger_sha256'])
        self.engine.client.objects[key] = saved; self.engine.client.deny = True
        with self.assertRaises(Exception): bind_release(self.store, identity, None, approved_ledger=result['ledger_sha256'])
        self.assertFalse(any('/releases/' in key for key in self.engine.client.objects))

    def test_pinned_manifest_and_all_english_route_descriptors_are_checked(self):
        batch = self.candidate(); self.assemble([batch])
        identity = self.pin(); modified = {**identity, 'tree_sha256': 'f'*64}
        with self.assertRaises(Exception): read_static_assembly(self.store, modified)
        key = slot_prefix('a')+'en/index.html'; self.engine.client.objects[key]['body'] += b'bad'
        with self.assertRaises(Exception): read_static_assembly(self.store, identity)

    def test_prepared_verification_reproduces_admitted_private_bodies_and_preview_bytes(self):
        batch = self.candidate(); result = self.assemble([batch]); identity = self.pin()
        verified = verify_prepared_ledger(self.store, self.original, identity, self.base/'verified')
        self.assertEqual(verified['ledger_sha256'], result['ledger_sha256'])
        item = read_ledger(self.store, result['ledger_sha256'])['items'][0]
        target = self.root/'en/blog'/f'{item["id"]}.html'
        target.write_bytes(target.read_bytes().replace(b'</main>', b'<div hidden>SECRET FULL TEXT</div></main>'))
        metadata = json.loads((self.root/ASSEMBLY).read_bytes())
        metadata['public_files'][f'en/blog/{item["id"]}.html'] = {'sha256': digest(target.read_bytes()), 'bytes': target.stat().st_size}
        (self.root/ASSEMBLY).write_bytes(stable_bytes(metadata)); repinned = self.pin('b', 'b'*32)
        with self.assertRaises(ExpansionError): verify_prepared_ledger(self.store, self.original, repinned, self.base/'bad-verified')

    def test_deployment_materialized_assets_survive_clean_reviewer_checkout(self):
        import portal_english_ui as ui
        batch = self.candidate()
        app = self.root/'assets/app.js'
        app.write_bytes(app.read_bytes()+b'\n/* deployment profile fixture */\n')
        result = self.assemble([batch]); identity = self.pin()
        self.assertIn(f'/assets/app.js?v={digest(app.read_bytes())[:12]}'.encode(),
                      (self.root/'en/index.html').read_bytes())
        # A reviewer must need no materialized local assets at all. All seven
        # version tokens come from the checksum-bound uploaded static tree.
        with mock.patch.object(ui, 'ROOT', self.base/'absent-review-checkout'), \
             mock.patch.object(ui, 'ASSETS', self.base/'absent-review-assets'):
            verified = verify_prepared_ledger(self.store, self.original, identity, self.base/'clean-review')
        self.assertEqual(verified['ledger_sha256'], result['ledger_sha256'])

    def test_shared_asset_change_after_rendering_does_not_revalidate_old_preview(self):
        batch = self.candidate(); self.assemble([batch])
        app = self.root/'assets/app.js'
        app.write_bytes(app.read_bytes()+b'\n/* unexpected later mutation */\n')
        identity = self.pin()
        with self.assertRaisesRegex(ExpansionError, 'preview-only projection'):
            verify_prepared_ledger(self.store, self.original, identity, self.base/'wrong-asset-review')

    def test_missing_shared_asset_prevents_prepared_review(self):
        batch = self.candidate(); self.assemble([batch])
        (self.root/'assets/app.js').unlink()
        identity = self.pin()
        with self.assertRaisesRegex(ExpansionError, 'public asset is missing'):
            verify_prepared_ledger(self.store, self.original, identity, self.base/'missing-asset-review')

    def test_batch_and_metadata_bounds_reject_original_or_unknown_routes(self):
        batch = self.candidate(); self.assemble([batch]); assembly = json.loads((self.root/ASSEMBLY).read_bytes())
        for rows in ([batch, batch], [{**batch, 'original': 'secret'}], [batch]*501):
            with self.assertRaises(ExpansionError): checked_batches(rows)
        broken = copy.deepcopy(assembly); original = broken['public_files'].pop('en/index.html')
        broken['public_files']['en/original-report.html'] = original
        with self.assertRaises(ExpansionError): checked_assembly(broken)

    def test_uploaded_english_recovery_preserves_static_bytes_and_requires_a_new_version_approval(self):
        batch = self.candidate(); original = self.assemble([batch]); identity = self.pin()
        before = {key: dict(value) for key, value in self.engine.client.objects.items() if key.startswith(slot_prefix('a'))}
        result = recover_prepared(self.store, self.original, identity, self.base/'prepared-recovery')
        self.assertEqual(result['ledger_sha256'], original['ledger_sha256'])
        self.assertEqual(read_handoff(self.store, result['handoff'])['batch'], batch)
        self.assertEqual(result['translation_calls'], 0); self.assertFalse(result['deployed'])
        self.assertEqual(before, {key: value for key, value in self.engine.client.objects.items() if key.startswith(slot_prefix('a'))})
        with self.assertRaises(ExpansionError): bind_release(self.store, identity, None)
        with self.assertRaises(R2NotFound): read_active(self.store, identity)
        self.root = self.fresh_tree(); empty = self.pin('b', 'b'*32)
        self.assertFalse(recover_prepared(self.store, self.original, empty, self.base/'no-english')['ready'])

    def test_empty_source_does_not_make_a_fake_english_home_or_navigation(self):
        self.assertFalse(self.assemble([])['ready']); self.assertFalse((self.root/'en').exists())
        self.assertNotIn('data-english-commentary-link', (self.root/'index.html').read_text())

    def test_english_ready_handoff_recovers_only_complete_unpublished_batches(self):
        self.assertIsNone(next_ready(self.store, self.original, None, self.base/'empty'))
        batch = self.candidate(); identity = next_ready(self.store, self.original, None, self.base/'handoff')
        value = read_handoff(self.store, identity); self.assertEqual(value['batch'], batch)
        verified, admission = verify_handoff(self.store, self.original, identity, self.base/'verify-handoff')
        self.assertEqual(verified, value); self.assertEqual(admission['day'], DAY)
        self.assertIsNone(next_ready(self.store, self.original, {'batches': [batch]}, self.base/'already'))

    def test_live_audit_checks_same_site_release_preview_hashes_and_denies_anonymous_full_text(self):
        _, identity, active = self.first_live(); ledger = read_ledger(self.store, active['ledger_sha256'])
        def reply(status=200, value=None, raw=None, headers=None):
            return mock.Mock(status_code=status, content=raw if raw is not None else stable_bytes(value),
                             headers=headers or {}, json=lambda: value)
        def get(url, **kwargs):
            if url.endswith('/.well-known/edge-state'): return reply(value=identity)
            if '/api/english/commentary' in url:
                from portal_english_ui import preview_item
                return reply(value={'policy': POLICY, 'total': 1, 'items': [preview_item(item) for item in ledger['items']]})
            relative = 'en/index.html' if url.endswith('/en/') else url[len(ORIGIN)+1:]
            return reply(raw=(self.root/relative).read_bytes(), headers={'Content-Language': 'en'})
        session = mock.Mock(); session.get.side_effect = get
        session.post.return_value = reply(401, {'error': 'login_required'}, headers={'Cache-Control': 'private, no-store', 'X-Robots-Tag': 'noindex'})
        proof = audit_live(self.store, identity, session)
        self.assertEqual(proof['status'], 'passed'); self.assertEqual(proof['anonymous_full_read'], 'denied')
        session.post.return_value = reply(200, {'blocks': [{'tag': 'p', 'text': 'SECRET FULL BODY'}]})
        with self.assertRaises(ExpansionError): audit_live(self.store, identity, session)
        wrong_version = {**identity, 'release_id': 'f'*32}
        with self.assertRaises(ExpansionError): audit_live(self.store, wrong_version, session)

    def test_api_preflight_cannot_treat_a_missing_route_as_a_published_access_boundary(self):
        session = mock.Mock()
        session.get.return_value = mock.Mock(status_code=404, content=b'{}', json=lambda: {'error': 'not_found'})
        with self.assertRaises(ExpansionError): preflight_api(session)
        session.get.return_value = mock.Mock(status_code=404, content=b'{}', json=lambda: {'error': 'commentary_not_published'})
        preflight_api(session)

    def test_rollback_without_english_requires_both_public_pages_and_api_ledger_absent(self):
        identity = self.pin()
        def reply(status, value):
            return mock.Mock(status_code=status, content=stable_bytes(value), json=lambda: value)
        def get(url, **kwargs):
            if url.endswith('/.well-known/edge-state'): return reply(200, identity)
            if url.endswith('/en/'): return reply(404, {})
            return reply(404, {'error': 'commentary_not_published'})
        session = mock.Mock(); session.get.side_effect = get
        self.assertTrue(audit_live(self.store, identity, session)['english_absent'])
        for surviving_route in ('/en/', '/api/english/commentary'):
            def unsafe_get(url, **kwargs):
                return reply(200, {}) if url.endswith(surviving_route) else get(url, **kwargs)
            session.get.side_effect = unsafe_get
            with self.subTest(route=surviving_route), self.assertRaises(ExpansionError):
                audit_live(self.store, identity, session)

    def review_orchestration(self, *, can_approve=True, bad_capture=False, bad_readback=False):
        import review_portal_english_handoff as reviewer
        batch = self.candidate(); previous = self.pin(); self.assemble([batch]); candidate = self.pin('b', 'b'*32)
        handoff_id = next_ready(self.store, self.original, None, self.base/'review-handoff')
        assembly = json.loads((self.root/ASSEMBLY).read_bytes())
        identity = {'schema_version': 1, 'policy': POLICY, 'operation': 'migrate', 'commit_sha': 'a'*40,
                    'static_tree_sha256': candidate['tree_sha256'], 'site_release': candidate['release_id'],
                    'ledger_sha256': assembly['ledger_sha256'], 'page_count': 1, 'handoff': handoff_id}
        artifact = self.base/'_release_validation'
        (artifact/'previous').mkdir(parents=True); (artifact/'candidate').mkdir()
        (artifact/'previous/edge-state.json').write_bytes(stable_bytes(previous))
        (artifact/'candidate/english-review-identity.json').write_bytes(stable_bytes(identity))
        variables, submitted = {}, []
        capture = {'id': 123, 'run_attempt': 1, 'head_sha': 'b'*40, 'status': 'completed', 'conclusion': 'success',
                   'path': SOURCE_PRODUCER['workflow'], 'event': 'workflow_dispatch',
                   'head_branch': 'feature' if bad_capture else 'main', 'repository': {'full_name': 'example/repo', 'private': False},
                   'head_repository': {'full_name': 'example/repo'}}
        cpu = {**capture, 'id': 456, 'head_sha': 'c'*40, 'head_branch': 'main', 'path': CPU_PRODUCER['workflow'], 'conclusion': 'failure'}
        def api(path, payload=None, method=None):
            if path.endswith('/runs/900'):
                return {**cpu, 'id': 900, 'head_sha': 'a'*40,
                        'path': '.github/workflows/neutral-edge-cutover.yml'}
            if path.endswith('/runs/900/approvals'): return []
            if '/runs/123/attempts/1/jobs' in path:
                return {'total_count': 1, 'jobs': [{'name': 'source_snapshot', 'status': 'completed', 'conclusion': 'success',
                         'started_at': DAY+'T01:00:00Z', 'completed_at': DAY+'T01:10:00Z'}]}
            if path.endswith('/runs/123/attempts/1'): return capture
            if '/runs/456/attempts/1/jobs' in path:
                return {'total_count': 2, 'jobs': [{'name': name, 'status': 'completed', 'conclusion': 'success'} for name in ('source', 'locale (en)')]}
            if path.endswith('/runs/456/attempts/1'): return cpu
            if path.endswith('/environments/portal-extended-locales-production'):
                return {'id': 42, 'name': 'portal-extended-locales-production',
                        'protection_rules': [{'type': 'required_reviewers', 'reviewers': [{'type': 'User'}]}]}
            if '/pending_deployments' in path:
                if payload is not None: submitted.append(payload); return [{'id': 999}]
                return [{'environment': {'id': 42}, 'current_user_can_approve': can_approve}]
            if '/variables' in path:
                if payload is not None: variables[payload['name']] = payload['value']; return None
                rows = [{'name': name, 'value': 'wrong' if bad_readback else value} for name, value in variables.items()]
                return {'total_count': len(rows), 'variables': rows}
            raise AssertionError('unexpected reviewer API route: '+path)
        environment = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
                       'KC_ENGLISH_AUTO_REVIEW': 'true', 'GITHUB_REPOSITORY': 'example/repo', 'GITHUB_RUN_ID': '900',
                       'GITHUB_RUN_ATTEMPT': '1',
                       'GITHUB_SHA': 'a'*40, 'GH_TOKEN': 'synthetic', 'ENGLISH_HANDOFF': handoff_id,
                       'CANDIDATE_SLOT': 'b', 'CANDIDATE_RELEASE': 'b'*32, 'CANDIDATE_STATIC_TREE': candidate['tree_sha256']}
        session = mock.Mock(); session.get.return_value = mock.Mock(status_code=200, content=stable_bytes(previous), json=lambda: previous)
        session.__enter__ = lambda value: value; session.__exit__ = lambda *args: None
        with chdir(self.base), mock.patch.dict('os.environ', environment, clear=True), mock.patch.object(reviewer, 'api', side_effect=api), \
             mock.patch.object(reviewer, 'R2Store') as storage, mock.patch.object(reviewer.requests, 'Session', return_value=session), \
             mock.patch('builtins.print'):
            storage.from_env.return_value = self.store; storage.return_value = self.original
            if not can_approve or bad_capture or bad_readback:
                with self.assertRaises(ExpansionError): reviewer.main()
            else: reviewer.main()
        return variables, submitted

    def test_delegated_review_uses_configured_required_reviewer_and_exact_persisted_version_values(self):
        variables, submitted = self.review_orchestration()
        self.assertEqual(len(submitted), 1); self.assertEqual(submitted[0]['environment_ids'], [42])
        self.assertEqual(submitted[0]['state'], 'approved')
        self.assertEqual(variables['PORTAL_ENGLISH_APPROVED_COMMIT_SHA'], 'a'*40)
        self.assertTrue(any('/publication-approvals/' in key for key in self.engine.client.objects))

    def test_missing_review_authority_bad_capture_or_failed_version_readback_never_submits_approval(self):
        for arguments in [{'can_approve': False}, {'bad_capture': True}, {'bad_readback': True}]:
            # Each case has its own independent synthetic release/storage.
            fixture = EnglishPublicationTests(); fixture.setUp()
            try:
                _, submitted = fixture.review_orchestration(**arguments)
                self.assertEqual(submitted, [])
            finally: fixture.doCleanups()

    def test_workflows_keep_required_approval_shared_lock_and_transactional_english_rollback(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/'.github/workflows/neutral-edge-cutover.yml').read_text()
        approval = workflow.split('  english_approval:', 1)[1].split('  cutover:', 1)[0]
        for required in ('name: portal-extended-locales-production', 'PORTAL_ENGLISH_APPROVED_STATIC_TREE',
                         'PORTAL_ENGLISH_APPROVED_LEDGER', 'PORTAL_ENGLISH_APPROVED_SITE_RELEASE',
                         'PORTAL_ENGLISH_APPROVED_HANDOFF', 'scripts/portal_english_publication.py approve'):
            self.assertIn(required, approval)
        cutover = workflow.split('  cutover:', 1)[1]
        self.assertIn("needs.english_approval.result == 'success'", cutover)
        self.assertLess(cutover.index('Bind the exact prepared English version'), cutover.index('Deploy prepared neutral edge release'))
        self.assertIn('steps.english_acceptance.outcome', cutover)
        self.assertIn('steps.english_rollback_acceptance.outcome', cutover)
        artifact = workflow.split('Build public validation artifact', 1)[1].split('Upload release validation artifact', 1)[0]
        self.assertIn('english-review-identity.json', artifact)
        self.assertNotIn('_neutral_site/en/', artifact)
        self.assertNotIn('private/bodies', artifact)
        pipeline = (root/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        handoff = pipeline.split('  english_publication_handoff:', 1)[1].split('  continue_admitted_batches:', 1)[0]
        self.assertIn("vars.PORTAL_ENGLISH_AUTO_PUBLISH == 'true'", handoff)
        self.assertIn('scripts/portal_english_handoff.py', handoff)
        self.assertNotIn('approved-ledger', handoff)


class EnglishReviewTests(unittest.TestCase):
    def setUp(self):
        self.identity = {'schema_version': 1, 'policy': POLICY, 'operation': 'migrate', 'commit_sha': 'a'*40,
                         'static_tree_sha256': 'b'*64, 'site_release': 'c'*32, 'ledger_sha256': 'd'*64,
                         'page_count': 1, 'handoff': 'e'*64}
        self.batch = {'generation': 'f'*64, 'candidate_id': '1'*64}
        self.assembly = {'schema_version': 1, 'policy': POLICY, 'status': 'assembled', 'batches': [self.batch],
                         'ledger_sha256': 'd'*64, 'page_count': 1, 'public_files': {name: {'sha256': 'a'*64, 'bytes': 10}
                           for name in ['en/index.html', 'sitemap-en.xml', 'en/blog/20261001-0000000000000001.html']}}
        self.handoff = {'batch': self.batch, 'page_count': 1}

    def review(self, identity=None):
        return review_identity(identity or self.identity, self.assembly, None, self.handoff,
                               commit='a'*40, tree='b'*64, release='c'*32)

    def test_each_exact_version_field_is_required_by_protected_approval(self):
        variables = self.review(); approval_is_valid(self.identity, self.identity, variables)
        for field in ('commit_sha', 'static_tree_sha256', 'site_release', 'ledger_sha256', 'operation', 'policy', 'page_count'):
            identity = {**self.identity, field: 'invalid'}
            with self.subTest(field=field), self.assertRaises(ExpansionError): self.review(identity)
        for name in variables:
            with self.subTest(variable=name), self.assertRaises(ExpansionError):
                approval_is_valid(self.identity, self.identity, {**variables, name: 'wrong'})

    def test_matching_artifact_and_environment_cannot_approve_a_malformed_identity(self):
        variables = self.review()
        for field, invalid in [('commit_sha', 'invalid'), ('site_release', 'invalid'), ('static_tree_sha256', 'invalid'),
                               ('ledger_sha256', 'invalid'), ('handoff', 'invalid'), ('page_count', True),
                               ('page_count', 0), ('page_count', 5001), ('policy', 'unknown'), ('operation', 'restore')]:
            identity = {**self.identity, field: invalid}
            matched = dict(variables)
            for suffix, key in [('COMMIT_SHA', 'commit_sha'), ('STATIC_TREE', 'static_tree_sha256'),
                                ('SITE_RELEASE', 'site_release'), ('LEDGER', 'ledger_sha256'), ('HANDOFF', 'handoff')]:
                matched['PORTAL_ENGLISH_APPROVED_'+suffix] = identity[key]
            with self.subTest(field=field, invalid=invalid), self.assertRaises(ExpansionError):
                approval_is_valid(identity, identity, matched)

    def test_wrong_batch_and_omitted_old_approvals_are_rejected(self):
        self.handoff['batch'] = {**self.batch, 'candidate_id': '2'*64}
        with self.assertRaises(ExpansionError): self.review()
        self.handoff['batch'] = self.batch
        with self.assertRaises(ExpansionError):
            review_identity(self.identity, self.assembly, {'batches': [{'generation': '3'*64, 'candidate_id': '4'*64}]},
                            self.handoff, commit='a'*40, tree='b'*64, release='c'*32)

    def test_real_main_public_english_cpu_job_must_succeed_even_if_another_locale_failed(self):
        producer = {**CPU_PRODUCER, 'repository': 'example/repo'}
        receipt = {'producer': producer}
        run = {'id': 456, 'run_attempt': 1, 'head_sha': 'c'*40, 'path': producer['workflow'], 'head_branch': 'main',
               'status': 'completed', 'conclusion': 'failure', 'event': 'workflow_run',
               'repository': {'full_name': 'example/repo', 'private': False}, 'head_repository': {'full_name': 'example/repo'}}
        jobs = [{'name': name, 'status': 'completed', 'conclusion': 'success'} for name in ('source', 'locale (en)')]
        producer_is_valid(receipt, run, jobs, 'example/repo')
        for change in ({'head_branch': 'feature'}, {'head_sha': 'f'*40}, {'run_attempt': 2}, {'status': 'in_progress'},
                       {'conclusion': 'cancelled'}, {'event': 'pull_request'}, {'path': 'wrong'}):
            with self.subTest(change=change), self.assertRaises(ExpansionError):
                producer_is_valid(receipt, {**run, **change}, jobs, 'example/repo')
        jobs[-1]['conclusion'] = 'failure'
        with self.assertRaises(ExpansionError): producer_is_valid(receipt, run, jobs, 'example/repo')


if __name__ == '__main__': unittest.main()
