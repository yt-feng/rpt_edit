#!/usr/bin/env python3
"""Exact published source and allowed-only discovery normalization contracts."""
import copy
from collections import Counter
from contextlib import chdir
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import publish_static_slot as publisher
import restore_published_chinese_source as source
import verify_portal_chinese_parity as parity
from test_publish_static_slot import FakeR2

ORIGIN = 'https://portal.example.invalid'


class PublishedChineseSourceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(); self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        current = chdir(self.base); current.__enter__(); self.addCleanup(current.__exit__, None, None, None)
        self.root = self.base/'_neutral_site'; self.root.mkdir()
        (self.root/'fresh-but-stale.txt').write_bytes(b'not the published source')
        self.raw = {relative: b'published bytes\n' for relative in parity.REQUIRED_PROTECTED_PATHS}
        links = ''.join(f'<link rel="alternate" hreflang="{code}" href="{ORIGIN}/{code}/">'
                        for code in parity.LOCALES)
        self.raw['index.html'] = (
            f'<html lang="zh-Hans"><head><link rel="canonical" href="{ORIGIN}/">'
            f'<link rel="alternate" hreflang="zh-Hans" href="{ORIGIN}/">'
            f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}/">'
            f'<link rel="alternate" hreflang="de" href="{ORIGIN}/de/">{links}'
            '</head><body>最新中文正文<a data-english-commentary-link href="/en/">English</a></body></html>'
        ).encode()
        self.raw['blog/latest.html'] = b'<html><head><title>Published</title></head><body>Exact latest body</body></html>'
        self.raw['assets/app.js'] = b'latest Chinese app'
        self.raw['assets/newsfeed-app.js'] = b'latest lazy app'
        self.raw['data/catalog.json'] = b'{"published":"latest"}'
        self.raw['downloads/archive.bin'] = b'\x00\x01\xff'
        self.raw['google0123456789abcdef.html'] = b'google-site-verification: google0123456789abcdef.html\n'
        maps = ['sitemap-pages.xml', *(f'sitemap-{code}.xml' for code in parity.LOCALES),
                'sitemap-extended-de.xml', 'sitemap-en.xml']
        self.raw['sitemap.xml'] = (
            '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + ''.join(f'<sitemap><loc>{ORIGIN}/{name}</loc></sitemap>\n' for name in maps)
            + '</sitemapindex>\n').encode()
        self.raw['robots.txt'] = ('User-agent: GPTBot\nDisallow: /\nUser-agent: *\nAllow: /\n'
                                 + ''.join(f'Sitemap: {ORIGIN}/{name}\n' for name in maps)).encode()
        self.excluded = {'ko/index.html', 'ja/index.html', 'ar/index.html', 'de/index.html', 'en/index.html',
                         'data/i18n/manifest.json', 'data/i18n/cache-v1.json.gz',
                         'data/extended-locales/assembly.json', 'data/english-commentary/assembly.json',
                         *parity.LOCALE_ASSET_PATHS, *(f'sitemap-{code}.xml' for code in parity.LOCALES),
                         'sitemap-extended.xml', 'sitemap-extended-de.xml', 'sitemap-en.xml',
                         'assets/extended-locales.js', 'assets/extended-locales.css',
                         'assets/english-commentary.js', 'assets/english-commentary.css'}
        self.raw.update(dict.fromkeys(self.excluded, b'previous translated feature'))
        self.locale = {'schema_version': 1, 'quality_gate_version': 3, 'coverage': dict.fromkeys(parity.LOCALES, 1.0),
                       'html_page_count': 1, 'translation_scope': 'incremental', 'index_policy': {
                           'mode': 'incremental-publication-cutoff', 'default': 'new-content-and-core-hubs',
                           'index_start_date': '2026-10-01', 'allowlist_count': 0, 'history_release_count': 0}}
        self.raw[source.CORE_MANIFEST] = publisher.json_bytes(self.locale)
        for code in parity.LOCALES:
            self.raw[f'sitemap-{code}.xml'] = f'<urlset><url><loc>{ORIGIN}/{code}/</loc></url></urlset>'.encode()
        self.publish_manifest()

    def publish_manifest(self):
        active = self.base/'active'; active.mkdir(exist_ok=True)
        for relative, body in self.raw.items():
            path = active/relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(body)
        paths, files, tree, total = publisher.build_inventory(active)
        self.state = {'schema_version': 1, 'slot': 'a', 'release_id': 'a'*32, 'tree_sha256': tree}
        self.manifest = {**self.state, 'files': files, 'file_count': len(files), 'total_bytes': total}
        self.client = FakeR2()
        for relative, path in paths.items():
            self.client.upload_file(str(path), 'bucket', publisher.slot_prefix('a')+relative,
                                    ExtraArgs=publisher.upload_extra_args(files[relative]))
        publisher.put_json(self.client, 'bucket', publisher.manifest_key('a'), self.manifest)
        self.client.operations.clear()

    def history_source(self, scope='release'):
        from portal_locale_history import plan_history_release
        canonical = ORIGIN + '/blog/historical.html'
        ledger = plan_history_release({canonical: '2026-09-01'}, history_start_date='2026-08-05',
                                      launch_date='2026-10-01', today='2026-10-02', previous=None, daily_limit=1)
        self.locale.update(translation_scope=scope, html_page_count=2, index_policy={
            'mode': 'fixed-publication-cutoff', 'default': 'hubs-only', 'index_start_date': '2026-10-01',
            'allowlist_count': 0, 'history_release': {'history_start_date': '2026-08-05', 'daily_limit': 1,
                'released_count': 1, 'selected_today_count': 1, 'paused': False, 'pending_count': 0}})
        self.raw[source.CORE_MANIFEST] = publisher.json_bytes(self.locale)
        self.raw[source.HISTORY_LEDGER] = publisher.json_bytes(ledger)
        self.raw['blog/historical.html'] = (
            f'<html><head><link rel="canonical" href="{canonical}"></head><body>Admitted history</body></html>').encode()
        for code in parity.LOCALES:
            self.raw[f'{code}/blog/historical.html'] = b'<html><head></head><body>Published history</body></html>'
            self.raw[f'sitemap-{code}.xml'] = (
                f'<urlset><url><loc>{ORIGIN}/{code}/</loc></url>'
                f'<url><loc>{ORIGIN}/{code}/blog/historical.html</loc></url></urlset>').encode()
        self.publish_manifest()
        return ledger

    def receipt(self):
        value = self.restore(); path = self.base/'source.json'
        path.write_bytes(publisher.json_bytes(value))
        return path, value

    def configuration(self, path, **overrides):
        return source.followup_configuration(path, **{'index_start_date': '2026-10-01',
                                                      'history_start_date': '2026-08-05', **overrides})

    def populate_followup(self, *, paused_history=None):
        for name, body in self.raw.items():
            if name.startswith(tuple(code+'/' for code in parity.LOCALES)) or name.startswith('data/i18n/') or name in {f'sitemap-{code}.xml' for code in parity.LOCALES}:
                path = self.root/name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(body)
        if paused_history is not None:
            manifest = copy.deepcopy(self.locale); manifest['translation_scope'] = 'release'
            manifest['index_policy']['history_release']['paused'] = True
            (self.root/source.CORE_MANIFEST).write_bytes(publisher.json_bytes(manifest))
            (self.root/source.HISTORY_LEDGER).write_bytes(publisher.json_bytes(paused_history))

    def restore(self):
        return source.restore(client=self.client, bucket='bucket', active_state=self.state,
                              active_manifest=self.manifest, root=self.root, site_url=ORIGIN)

    def test_restore_uses_latest_exact_chinese_and_receipt_is_a_valid_parity_baseline(self):
        original_manifest = copy.deepcopy(self.manifest)
        result = self.restore()
        self.assertEqual(self.manifest, original_manifest)
        self.assertEqual(result['source_state'], self.state)
        self.assertEqual(result['remote_mutations'], 0); self.assertEqual(result['provider_requests'], 0)
        self.assertEqual(set(result['files']), set(self.raw)-self.excluded)
        self.assertEqual(set(result['normalized_files']), {'index.html', 'robots.txt', 'sitemap.xml'})
        self.assertFalse((self.root/'fresh-but-stale.txt').exists())
        for relative in set(self.raw)-self.excluded-set(result['normalized_files']):
            self.assertEqual((self.root/relative).read_bytes(), self.raw[relative], relative)
        for relative in result['normalized_files']:
            self.assertEqual(source.descriptor(self.root/relative),
                             {key: result['files'][relative][key] for key in ('size', 'sha256')})
        html = (self.root/'index.html').read_bytes()
        self.assertEqual(parity._body(html, relative='index.html'), parity._body(self.raw['index.html'], relative='index.html'))
        self.assertIn(b'hreflang="de"', html); self.assertIn(b'data-english-commentary-link', html)
        receipt = self.base/'source-receipt.json'; receipt.write_bytes(publisher.json_bytes(result))
        snapshot = parity.create_snapshot(root=self.root, site_origin=ORIGIN, active_manifest=receipt)
        self.assertTrue(snapshot['active_manifest']['checked'])
        operations = Counter(self.client.operations)
        for relative in result['files']:
            self.assertEqual(operations['get', publisher.slot_prefix('a')+relative], 1, relative)
        self.assertEqual(operations['get', publisher.manifest_key('a')], 2)
        self.assertEqual(operations['head', publisher.incomplete_key('a')], 3)
        self.assertTrue(all(kind in {'get', 'head'} for kind, _key in self.client.operations))

    def test_corrupt_source_leaves_generated_tree_untouched(self):
        key = publisher.slot_prefix('a')+'assets/app.js'
        self.client.objects[key]['body'] = b'x'*len(self.raw['assets/app.js'])
        with self.assertRaisesRegex(RuntimeError, 'differs from manifest'):
            self.restore()
        self.assertEqual((self.root/'fresh-but-stale.txt').read_bytes(), b'not the published source')
        self.assertEqual(list(self.base.glob('published-chinese-*')), [])

    def test_changed_remote_identity_cannot_replace_generated_tree(self):
        original_get = self.client.get_object
        calls = 0
        def get(**kwargs):
            nonlocal calls
            if kwargs['Key'] == publisher.manifest_key('a'):
                calls += 1
                if calls == 2:
                    return {'Body': io.BytesIO(publisher.json_bytes({**self.manifest, 'release_id': 'b'*32}))}
            return original_get(**kwargs)
        with patch.object(self.client, 'get_object', side_effect=get):
            with self.assertRaisesRegex(RuntimeError, 'differs from active release'):
                self.restore()
        self.assertTrue((self.root/'fresh-but-stale.txt').exists())

    def test_incomplete_marker_and_forged_manifest_stop_before_object_download(self):
        publisher.put_json(self.client, 'bucket', publisher.incomplete_key('a'), {})
        self.client.operations.clear()
        with self.assertRaisesRegex(RuntimeError, 'incomplete publication marker'):
            self.restore()
        self.assertFalse(any(kind == 'get' for kind, _ in self.client.operations))
        del self.client.objects[publisher.incomplete_key('a')]
        self.manifest['files']['assets/app.js']['sha256'] = '0'*64
        with self.assertRaisesRegex(RuntimeError, 'tree is invalid'):
            self.restore()
        self.assertTrue((self.root/'fresh-but-stale.txt').exists())

    def test_publication_marker_created_during_restore_prevents_promotion(self):
        original_get = self.client.get_object
        def get(**kwargs):
            value = original_get(**kwargs)
            if kwargs['Key'] == publisher.slot_prefix('a')+'assets/app.js':
                publisher.put_json(self.client, 'bucket', publisher.incomplete_key('a'), {})
            return value
        with patch.object(self.client, 'get_object', side_effect=get):
            with self.assertRaisesRegex(RuntimeError, 'incomplete publication marker'):
                self.restore()
        self.assertTrue((self.root/'fresh-but-stale.txt').exists())

    def test_cli_writes_private_source_receipt_outside_public_tree(self):
        state_path, manifest_path = self.base/'state.json', self.base/'manifest.json'
        state_path.write_bytes(publisher.json_bytes(self.state))
        manifest_path.write_bytes(publisher.json_bytes(self.manifest))
        output = self.base/'proof'/'source.json'
        with patch('chart_search_r2.client_and_bucket', return_value=(self.client, 'bucket')), \
             patch('sys.argv', ['restore_published_chinese_source.py', '--root', '_neutral_site',
                                '--active-state', str(state_path), '--active-manifest', str(manifest_path),
                                '--site-url', ORIGIN, '--output', str(output)]), \
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            self.assertEqual(source.main(), 0)
        receipt = json.loads(output.read_bytes())
        self.assertEqual(receipt['source_state'], self.state)
        self.assertEqual(output.stat().st_mode & 0o777, 0o600)
        self.assertTrue(parity.create_snapshot(root=self.root, site_origin=ORIGIN, active_manifest=output)['active_manifest']['checked'])
        self.assertEqual(json.loads(stdout.getvalue().splitlines()[0])['restored_files'], receipt['file_count'])
        self.assertIn('chinese_locale_source_sha256=' + source.hashlib.sha256(output.read_bytes()).hexdigest(), stdout.getvalue())

    def test_incremental_source_uses_same_policy_and_rejects_configuration_changes(self):
        path, receipt = self.receipt(); config = self.configuration(path)
        self.assertEqual(config['translation_scope'], 'incremental')
        self.assertEqual(config['history_state_in'], ''); self.assertFalse(config['history_paused'])
        with self.assertRaisesRegex(source.SourceRestoreError, 'index start differs'):
            self.configuration(path, index_start_date='2026-10-02')
        self.populate_followup(); source.validate_followup(self.root, path)
        (self.root/'ko/index.html').unlink()
        with self.assertRaisesRegex(source.SourceRestoreError, 'dropped a published page'):
            source.validate_followup(self.root, path)

    def test_release_and_month_history_are_preserved_without_opening_a_new_day(self):
        from portal_locale_history import plan_history_release
        for scope in ('release', 'month'):
            with self.subTest(scope=scope):
                ledger = self.history_source(scope); path, receipt = self.receipt(); config = self.configuration(path)
                self.assertEqual(config['translation_scope'], 'release'); self.assertTrue(config['history_paused'])
                self.assertEqual(config['history_daily_limit'], 1)
                self.assertEqual(Path(config['history_state_in']).read_bytes(), self.raw[source.HISTORY_LEDGER])
                self.assertFalse(Path(config['history_state_in']).is_relative_to(self.root))
                paused = plan_history_release({ledger['released'][0]: '2026-09-01', ORIGIN+'/blog/next.html': '2026-09-02'},
                    history_start_date=config['history_start_date'], launch_date=config['index_start_date'],
                    today='2026-11-17', previous=json.loads(Path(config['history_state_in']).read_bytes()),
                    daily_limit=config['history_daily_limit'], paused=config['history_paused'])
                self.assertEqual(paused['released'], ledger['released'])
                self.assertEqual(paused['last_release_date'], ledger['last_release_date'])
                self.assertEqual(paused['selected_today'], [])
                self.populate_followup(paused_history=paused); source.validate_followup(self.root, path)
                paused['released'].append(ORIGIN+'/blog/next.html')
                (self.root/source.HISTORY_LEDGER).write_bytes(publisher.json_bytes(paused))
                with self.assertRaisesRegex(source.SourceRestoreError, 'admitted history set'):
                    source.validate_followup(self.root, path)

    def test_history_configuration_and_old_discovery_cannot_be_changed(self):
        self.history_source(); path, receipt = self.receipt()
        with self.assertRaisesRegex(source.SourceRestoreError, 'history start differs'):
            self.configuration(path, history_start_date='2026-08-06')
        self.populate_followup()
        (self.root/'sitemap-ko.xml').write_bytes(f'<urlset><url><loc>{ORIGIN}/ko/</loc></url></urlset>'.encode())
        with self.assertRaisesRegex(source.SourceRestoreError, 'removed published discovery'):
            source.validate_followup(self.root, path)

    def test_existing_allowlist_requires_same_count_and_already_published_urls(self):
        self.locale.update(translation_scope='release', index_policy={
            'mode': 'fixed-publication-cutoff', 'default': 'hubs-only', 'index_start_date': '2026-10-01', 'allowlist_count': 1})
        self.raw[source.CORE_MANIFEST] = publisher.json_bytes(self.locale); self.publish_manifest()
        path, _ = self.receipt(); allowlist = self.base/'allowlist.txt'; allowlist.write_text(ORIGIN+'/\n')
        self.assertEqual(self.configuration(path, allowlist_path=allowlist.name)['translation_scope'], 'release')
        with self.assertRaisesRegex(source.SourceRestoreError, 'allowlist changes'):
            self.configuration(path)
        allowlist.write_text(ORIGIN+'/newly-approved-history.html\n')
        with self.assertRaisesRegex(source.SourceRestoreError, 'allowlist changes'):
            self.configuration(path, allowlist_path=allowlist.name)

    def test_arbitrary_root_or_symlink_cannot_be_replaced(self):
        other = self.base/'other'; other.mkdir()
        with self.assertRaisesRegex(source.SourceRestoreError, 'only the task'):
            source.restore(client=self.client, bucket='bucket', active_state=self.state,
                           active_manifest=self.manifest, root=other, site_url=ORIGIN)
        (self.root/'escape').symlink_to(other, target_is_directory=True)
        with self.assertRaisesRegex(source.SourceRestoreError, 'contains a symlink'):
            self.restore()
        self.assertEqual(self.client.operations, [])

    def test_failed_directory_promotion_restores_previous_generated_tree(self):
        original_rename = Path.rename
        def rename(path, target):
            if path.name == 'source':
                raise OSError('promotion failed')
            return original_rename(path, target)
        with patch.object(Path, 'rename', rename):
            with self.assertRaisesRegex(OSError, 'promotion failed'):
                self.restore()
        self.assertTrue((self.root/'fresh-but-stale.txt').exists())
        self.assertEqual(list(self.base.glob('published-chinese-*')), [])

    def test_head_normalization_rejects_modified_body_or_unapproved_discovery(self):
        raw = self.raw['index.html']
        malformed = raw.replace(f'{ORIGIN}/ko/'.encode(), b'https://other.example/ko/')
        with self.assertRaisesRegex(parity.ParityError, 'incorrect ko hreflang'):
            source.normalize_discovery('index.html', malformed, ORIGIN)
        with patch.object(source, 'remove_existing_locale_discovery', side_effect=lambda head, **_: head.replace('canonical', 'changed')):
            with self.assertRaises((parity.ParityError, source.SourceRestoreError)):
                source.normalize_discovery('index.html', raw, ORIGIN)


if __name__ == '__main__':
    unittest.main()
