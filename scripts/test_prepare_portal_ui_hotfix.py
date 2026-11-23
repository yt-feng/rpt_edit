"""Offline immutable-source, narrow-patch and commit-order contracts."""
import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import prepare_portal_ui_hotfix as hotfix
import publish_static_slot as publish
import portal_english_publication as english
import portal_locale_manifest as locale_manifest
import verify_prepared_static_slot as prepared_slot
from portal_english_ui import PUBLIC_ASSET_NAMES, detail, homepage
from verify_prepared_static_slot import static_tree_sha256, verify_candidate_locale_routes


class S3Error(Exception):
    def __init__(self, code):
        self.response = {'Error': {'Code': code}}
        super().__init__(code)


class MemoryR2:
    def __init__(self):
        self.objects = {}; self.trace = []; self.reject_source = ''; self.copy_failures = []; self.copy_response_error = ''
    def put_object(self, **args):
        body = bytes(args['Body']); key = args['Key']; self.trace.append(('put', key))
        self.objects[key] = {'Body': body, 'ContentLength': len(body), 'ContentType': args.get('ContentType', ''),
                             'CacheControl': args.get('CacheControl', ''), 'Metadata': copy.deepcopy(args.get('Metadata', {})),
                             'ContentEncoding': args.get('ContentEncoding', ''), 'ETag': '"' + hashlib.md5(body).hexdigest() + '"'}
        return {'ETag': self.objects[key]['ETag']}
    def head_object(self, **args):
        if args['Key'] not in self.objects: raise S3Error('NoSuchKey')
        return {key: copy.deepcopy(value) for key, value in self.objects[args['Key']].items() if key != 'Body'}
    def get_object(self, **args):
        return {**self.head_object(**args), 'Body': io.BytesIO(self.objects[args['Key']]['Body'])}
    def copy_object(self, **args):
        source = args['CopySource']['Key']; self.trace.append(('copy', args['Key'], source, args['CopySourceIfMatch']))
        if self.copy_failures: raise S3Error(self.copy_failures.pop(0))
        if source == self.reject_source or args['CopySourceIfMatch'] != self.objects[source]['ETag']:
            raise S3Error('PreconditionFailed')
        original = self.objects[source]
        extra = ({key: original[key] for key in ('ContentType', 'CacheControl', 'ContentEncoding', 'Metadata')}
                 if args['MetadataDirective'] == 'COPY' else {key: args[key] for key in ('ContentType', 'CacheControl', 'Metadata')})
        self.put_object(Bucket=args['Bucket'], Key=args['Key'], Body=original['Body'], **extra)
        if self.copy_response_error: raise S3Error(self.copy_response_error)
        return {'CopyObjectResult': {'ETag': self.objects[args['Key']]['ETag']}}
    def get_paginator(self, _name):
        client = self
        class Pages:
            def paginate(self, **args):
                yield {'Contents': [{'Key': key, 'Size': row['ContentLength']} for key, row in client.objects.items() if key.startswith(args['Prefix'])]}
        return Pages()
    def delete_objects(self, **args):
        for row in args['Delete']['Objects']:
            self.trace.append(('delete', row['Key'])); self.objects.pop(row['Key'], None)
        return {}


class HotfixTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.source = self.root/'site'; self.locale = self.root/'locale'
        (self.source/'assets').mkdir(parents=True); self.locale.mkdir()
        self.client = MemoryR2(); self.bucket = 'test-bucket'; self.old_release = 'a'*32; self.new_release = 'b'*32
        self.source_prefix = publish.slot_prefix('a'); self.target_prefix = publish.slot_prefix('b')
        bodies = {f'assets/{name}': f'// previous {name}\n'.encode() for name in hotfix.ASSETS | set(PUBLIC_ASSET_NAMES)}
        bodies.update({'assets/site-feedback.css': b'.feedback{}', 'assets/newsfeed-app.js': b'// retained module',
                       'report.html': b'<body data-page="report">Keep body<script src="assets/app.js?v=old"></script><script src="assets/analytics.js"></script></body>',
                       'index.html': b'<body>Keep home<script src="/assets/app.js?v=old"></script></body>',
                       'blog/article.html': b'<body>Unchanged original article<script src="/assets/app.js?v=old"></script></body>',
                       'ko/report.html': b'<body>Unchanged locale shell</body>',
                       'data/i18n/manifest.json': b'{"schema_version":1,"coverage":{"ko":1,"ja":1,"ar":1},"translation":"retained"}',
                       'robots.txt': b'User-agent: *\nAllow: /\n', 'sitemap-en.xml': b'<urlset>retained sitemap</urlset>'})
        site_source = Path(__file__).resolve().parents[1] / 'portal_suite/site_src'
        developer = (site_source / 'developer-api.html').read_bytes()
        bodies['developer-api.html'] = developer.replace(b'<body data-page="developer-api">', b'<body data-page="developer-api" data-analytics-auto="manual">')
        activity = (site_source / 'activity.html').read_bytes()
        self.assertIn(hotfix.ACTIVITY_OPTIONS_AFTER.encode(), activity)
        bodies['activity.html'] = activity.replace(hotfix.ACTIVITY_OPTIONS_AFTER.encode(), hotfix.ACTIVITY_OPTIONS_BEFORE.encode())
        bodies.update({path: ('{"retained":' + str(index) + '}').encode() for index, path in enumerate(publish.DEFAULT_RUNTIME_PATHS)})
        for name in hotfix.ASSETS:
            (self.locale/name if name == 'english-commentary.js' else self.source/'assets'/name).write_bytes(f'// replacement {name}\n'.encode())
        (self.source/'assets/app.js').write_text('const AUTH_SESSION_KEY = "deployment_auth_session"; const feedback="/assets/site-feedback.js?v=feedback-v1"; const news="assets/newsfeed-app.js?v=old";')
        (self.locale/'english-commentary.js').write_text('const SESSION = "portal_auth_session";')
        private_body = {'schema_version': 1, 'policy': english.POLICY, 'locale': 'en', 'content_kind': 'secondary-commentary',
                        'id': '20261024-'+'c'*16, 'title': 'Approved interpretation', 'preview': 'A short approved preview.',
                        'datePublished': '2026-10-24', 'editorial_sha256': 'd'*64, 'blocks': [{'tag': 'p', 'text': 'PRIVATE_AUTHORIZED_BODY_ONLY'}]}
        private_raw = english.stable_bytes(private_body)
        self.item = {key: private_body[key] for key in ('id', 'title', 'preview', 'datePublished', 'editorial_sha256')}
        self.item['body_sha256'] = hashlib.sha256(private_raw).hexdigest()
        items = [self.item]
        ledger = {'schema_version': 1, 'policy': english.POLICY, 'locale': 'en', 'status': 'approved', 'release_id': hashlib.sha256(english.stable_bytes(items)).hexdigest(), 'items': items}
        ledger_raw = english.stable_bytes(ledger); self.ledger_hash = hashlib.sha256(ledger_raw).hexdigest()
        self.store_private(english.PREFIX+'/ledgers/'+self.ledger_hash+'.json', ledger_raw)
        self.store_private(english.PREFIX+'/bodies/'+self.item['body_sha256']+'.json', private_raw)
        self.store_private(english.PREFIX+'/releases/'+self.old_release+'/manifest.json', english.stable_bytes({'schema_version': 1, 'policy': english.POLICY, 'status': 'approved', 'site_release': self.old_release, 'ledger_sha256': self.ledger_hash}))
        hashes = {name: hashlib.sha256(bodies['assets/'+name]).hexdigest() for name in PUBLIC_ASSET_NAMES}
        bodies['en/index.html'] = homepage(items, approved=True, asset_hashes=hashes)
        bodies[f'en/blog/{self.item["id"]}.html'] = detail(self.item, approved=True, asset_hashes=hashes)
        previews = {path: {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)} for path, raw in bodies.items() if path.startswith('en/') or path == 'sitemap-en.xml'}
        bodies[english.ASSEMBLY] = english.stable_bytes({'schema_version': 1, 'policy': english.POLICY, 'status': 'assembled', 'batches': [{'generation': 'e'*64, 'candidate_id': 'f'*64}], 'ledger_sha256': self.ledger_hash, 'page_count': 1, 'public_files': previews})
        files = {}
        for relative, body in bodies.items():
            row = {'sha256': hashlib.sha256(body).hexdigest(), 'size': len(body), 'content_type': 'text/html' if relative.endswith('.html') else 'application/json' if relative.endswith('.json') else 'text/plain', 'cache_control': publish.cache_control_for(Path(relative))}
            files[relative] = row
            self.client.put_object(Bucket=self.bucket, Key=self.source_prefix+relative, Body=body, **publish.upload_extra_args(row))
        runtime_files = {Path(path).name: {**files[path], 'content_type': 'application/json', 'cache_control': 'no-store'} for path in publish.DEFAULT_RUNTIME_PATHS}
        runtime = {'schema_version': 1, 'release_id': self.old_release, 'prefix': publish.runtime_release_prefix(self.old_release), 'tree_sha256': publish.runtime_tree_sha256(runtime_files), 'file_count': len(runtime_files), 'files': runtime_files}
        for path in publish.DEFAULT_RUNTIME_PATHS:
            row = runtime_files[Path(path).name]; extra = publish.upload_extra_args(row); extra['Metadata']['release-id'] = self.old_release
            self.client.put_object(Bucket=self.bucket, Key=runtime['prefix']+Path(path).name, Body=bodies[path], **extra)
        publish.put_json(self.client, self.bucket, publish.runtime_manifest_key(self.old_release), runtime)
        self.manifest = {'schema_version': 1, 'slot': 'a', 'release_id': self.old_release, 'tree_sha256': static_tree_sha256(files), 'file_count': len(files), 'total_bytes': sum(row['size'] for row in files.values()), 'files': files, 'runtime_data': {key: runtime[key] for key in ('schema_version', 'release_id', 'prefix', 'tree_sha256')}}
        publish.put_json(self.client, self.bucket, publish.manifest_key('a'), self.manifest)
        self.active = {key: self.manifest[key] for key in ('slot', 'release_id', 'tree_sha256')}
        self.client.trace.clear(); self.guard_calls = 0
    def store_private(self, key, body):
        self.client.put_object(Bucket=self.bucket, Key=key, Body=body, ContentType='application/json', CacheControl='private, no-store', Metadata={'sha256': hashlib.sha256(body).hexdigest()})
    def guard(self): self.guard_calls += 1
    def run_prepare(self, guard=None):
        return hotfix.prepare(self.client, self.bucket, active_state=self.active, release=self.new_release, source_root=self.source, locale_assets=self.locale, assert_active=guard or self.guard)

    def replace_source_bodies(self, bodies):
        for relative, body in bodies.items():
            row = hotfix.descriptor_with_body(self.manifest['files'].get(relative, {
                'content_type': 'text/html' if relative.endswith('.html') else 'application/json',
                'cache_control': publish.cache_control_for(Path(relative)),
            }), body)
            if relative.endswith('.js'): row['content_type'] = 'application/javascript'
            self.manifest['files'][relative] = row
            self.client.put_object(Bucket=self.bucket, Key=self.source_prefix + relative, Body=body, **publish.upload_extra_args(row))
        self.manifest.update(file_count=len(self.manifest['files']),
                             total_bytes=sum(row['size'] for row in self.manifest['files'].values()),
                             tree_sha256=static_tree_sha256(self.manifest['files']))
        self.active['tree_sha256'] = self.manifest['tree_sha256']
        publish.put_json(self.client, self.bucket, publish.manifest_key('a'), self.manifest)
        self.client.trace.clear()

    def locale_fixture(self, *, sharded=False):
        bodies = {}; value = {'schema_version': 1, 'coverage': dict.fromkeys(hotfix.locale_routes.LOCALES, 1.0),
                              'application_routes': {}, 'lazy_javascript_assets': {}}
        def describe(relative, body):
            bodies[relative] = body
            return {'path': relative, 'byte_size': len(body), 'sha256': hashlib.sha256(body).hexdigest()}
        for locale, direction in hotfix.locale_routes.LOCALES.items():
            value['application_routes'][locale] = {}
            for filename, page in hotfix.locale_routes.APPLICATION_PAGES.items():
                body = (f'<html lang="{locale}" dir="{direction}"><head><meta name="robots" content="noindex,follow"></head>'
                        f'<body data-page="{page}"><aside data-kc-locale-help>'
                        f'<a data-kc-chinese-entry data-kc-chinese-equivalent hreflang="zh-Hans" href="https://portal.example.invalid/{filename}">中文</a>'
                        '<a data-kc-chinese-entry hreflang="zh-Hans" href="https://portal.example.invalid/">Chinese home</a>'
                        '<span data-kc-public-account-contact><a href="mailto:info@kcdesk.com" dir="ltr">info@kcdesk.com</a></span>'
                        '<p data-kc-locale-error hidden></p></aside><main>Retained translation</main></body></html>').encode()
                value['application_routes'][locale][filename] = describe(f'{locale}/{filename}', body)
        value['recovery_asset'] = describe('assets/locale-recovery.js', b'/* retained recovery */')
        value['detail_asset'] = describe('assets/locale-detail.js', b'/* retained detail */')
        for locale, prefix in [('zh-Hans', ''), *((locale, f'{locale}/') for locale in hotfix.locale_routes.LOCALES)]:
            relative = prefix + 'assets/newsfeed-app.js'
            raw = self.client.objects[self.source_prefix + relative]['Body'] if not prefix else f'/* retained {locale} newsfeed */'.encode()
            value['lazy_javascript_assets'][locale] = describe(relative, raw)
        # Additional covered descriptors must follow their actual candidate too;
        # a Newsfeed-only replacement would miss app, analytics and CSS bindings.
        value['shared_assets'] = {name: {**describe('assets/' + name, self.client.objects[self.source_prefix + 'assets/' + name]['Body']), 'owner': 'retained'}
                                  for name in ('app.js', 'admin-users.js', 'analytics.js', 'styles.css')}
        if sharded:
            source = 'Retained source text'; prompt = 'test-locale-v1'
            key = hashlib.sha256(f'{prompt}\0copy\0{source}'.encode()).hexdigest()
            row = {'source': source, 'context': 'html:p', 'reason': 'translation_time_budget', 'translation_class': 'copy',
                   'source_sha256': hashlib.sha256(source.encode()).hexdigest()}
            units = {'ko': {key: row}, 'ja': {}, 'ar': {}}
            shard, body = locale_manifest._encode_fallback_shard(units, key[0], prompt)
            bodies[shard['path']] = body
            value.update(prompt_version=prompt, source_unit_count=1,
                         translation_entry_count={'ko': 0, 'ja': 1, 'ar': 1}, coverage={'ko': 0, 'ja': 1, 'ar': 1},
                         resolved_entry_count=dict.fromkeys(units, 1), resolved_coverage=dict.fromkeys(units, 1),
                         source_fallbacks={'schema_version': 5, 'counts': {'ko': 1, 'ja': 0, 'ar': 0}, 'shards': [shard]})
        for relative in (*prepared_slot.REQUIRED_STATIC_PATHS, *prepared_slot.REQUIRED_LOCALE_PATHS):
            if relative not in self.manifest['files'] and relative not in bodies:
                bodies[relative] = ('Retained fixture: ' + relative).encode()
        bodies['data/i18n/manifest.json'] = json.dumps(value, ensure_ascii=False).encode()
        self.replace_source_bodies(bodies)
        return value

    def test_locale_asset_graph_rebinds_actual_candidate_and_passes_the_unchanged_route_guard(self):
        original = self.locale_fixture()
        before = copy.deepcopy(self.client.objects)
        result = self.run_prepare()
        candidate = json.loads(self.client.objects[publish.manifest_key('b')]['Body'])
        raw = self.client.objects[self.target_prefix + 'data/i18n/manifest.json']['Body']
        updated = locale_manifest.parse_locale_manifest(raw)
        for descriptor in [updated['lazy_javascript_assets']['zh-Hans'], *updated['shared_assets'].values()]:
            row = candidate['files'][descriptor['path']]
            self.assertEqual((descriptor['byte_size'], descriptor['sha256']), (row['size'], row['sha256']))
        self.assertEqual(updated['application_routes'], original['application_routes'])
        self.assertEqual(updated['coverage'], original['coverage'])
        for locale in hotfix.locale_routes.LOCALES:
            self.assertEqual(updated['lazy_javascript_assets'][locale], original['lazy_javascript_assets'][locale])
        self.assertTrue(all(row['owner'] == 'retained' for row in updated['shared_assets'].values()))
        expected = copy.deepcopy(original)
        expected['lazy_javascript_assets']['zh-Hans'] = updated['lazy_javascript_assets']['zh-Hans']
        expected['shared_assets'] = updated['shared_assets']
        self.assertEqual(updated, expected, 'only asset descriptor hashes and sizes may change')
        self.assertEqual(candidate['files']['data/i18n/manifest.json']['sha256'], hashlib.sha256(raw).hexdigest())
        self.assertIn('data/i18n/manifest.json', result['changed_files'])
        for key, value in before.items(): self.assertEqual(self.client.objects[key], value, key)
        report = verify_candidate_locale_routes(self.client, self.bucket, self.target_prefix, candidate['files'], updated, 'https://portal.example.invalid')
        self.assertEqual(report['status'], 'passed')
        self.assertEqual(report['request_count'], 24)
        stale = copy.deepcopy(updated); stale['lazy_javascript_assets']['zh-Hans'] = original['lazy_javascript_assets']['zh-Hans']
        with self.assertRaisesRegex(RuntimeError, 'Locale route descriptor differs'):
            verify_candidate_locale_routes(self.client, self.bucket, self.target_prefix, candidate['files'], stale, 'https://portal.example.invalid')

    def test_sharded_locale_provenance_is_revalidated_but_never_reencoded_or_replaced(self):
        original = self.locale_fixture(sharded=True)
        shard = original['source_fallbacks']['shards'][0]
        before = copy.deepcopy(self.client.objects[self.source_prefix + shard['path']])
        result = self.run_prepare()
        raw = self.client.objects[self.target_prefix + 'data/i18n/manifest.json']['Body']
        updated = json.loads(raw)
        for key in ('source_fallbacks', 'source_unit_count', 'prompt_version', 'coverage', 'translation_entry_count', 'resolved_entry_count', 'resolved_coverage'):
            self.assertEqual(updated[key], original[key], key)
        self.assertEqual(self.client.objects[self.target_prefix + shard['path']], before)
        self.assertNotIn(shard['path'], result['changed_files'])
        verified = locale_manifest.parse_locale_manifest(raw, shard_resolver=lambda row: self.client.objects[self.target_prefix + row['path']]['Body'])
        locale_manifest.validate_translation_resolution(verified, hotfix.locale_routes.LOCALES)
        self.assertEqual(verified['source_fallbacks']['schema_version'], 5)
        report = prepared_slot.verify_prepared_static_slot(
            self.client, self.bucket, slot=result['slot'], release=result['release_id'], tree=result['tree_sha256'],
            locale_origin='https://portal.example.invalid',
        )
        self.assertTrue(report['verified'])
        self.assertEqual(report['locale_routes_status'], 'passed')
        self.assertEqual(report['locale_objects_verified'], 24)
        self.assertEqual(report['locale_source_shards_verified'], 1)

    def test_old_locale_descriptor_mismatches_fail_before_any_candidate_write(self):
        original = self.locale_fixture()
        for section, key in [('lazy_javascript_assets', 'zh-Hans'), ('shared_assets', 'analytics.js'), ('application_routes', 'ko')]:
            value = copy.deepcopy(original)
            row = value[section][key]['report.html'] if section == 'application_routes' else value[section][key]
            row['sha256'] = '0' * 64
            self.replace_source_bodies({'data/i18n/manifest.json': json.dumps(value).encode()})
            with self.subTest(section=section), self.assertRaisesRegex(RuntimeError, 'descriptor differs from pinned static manifest'):
                self.run_prepare()
            self.assertEqual(self.client.trace, [])

    def test_legacy_compressed_provenance_keeps_its_original_encoding(self):
        original = self.locale_fixture(sharded=True)
        shard = original['source_fallbacks']['shards'][0]
        original['source_fallbacks'] = json.loads(self.client.objects[self.source_prefix + shard['path']]['Body'])['source_fallbacks']
        self.client.objects.pop(self.source_prefix + shard['path'])
        self.manifest['files'].pop(shard['path'])
        self.replace_source_bodies({'data/i18n/manifest.json': json.dumps(original).encode()})
        result = self.run_prepare()
        raw = self.client.objects[self.target_prefix + 'data/i18n/manifest.json']['Body']
        self.assertEqual(json.loads(raw)['source_fallbacks'], original['source_fallbacks'])
        self.assertEqual(json.loads(raw)['source_fallbacks']['schema_version'], 4)
        locale_manifest.validate_translation_resolution(locale_manifest.parse_locale_manifest(raw), hotfix.locale_routes.LOCALES)
        self.assertNotIn(shard['path'], result['changed_files'])

    def test_missing_corrupt_or_extra_locale_shards_fail_before_candidate_copy(self):
        original = self.locale_fixture(sharded=True)
        shard = original['source_fallbacks']['shards'][0]
        baseline = copy.deepcopy(self.client.objects)
        inventory = copy.deepcopy(self.manifest)
        for failure in ('missing', 'corrupt', 'extra', 'descriptor'):
            self.client.objects = copy.deepcopy(baseline); self.manifest = copy.deepcopy(inventory)
            self.active['tree_sha256'] = inventory['tree_sha256']; self.client.trace.clear()
            if failure == 'missing': self.client.objects.pop(self.source_prefix + shard['path'])
            elif failure == 'corrupt': self.client.objects[self.source_prefix + shard['path']]['Body'] = b'x' * shard['byte_size']
            elif failure == 'extra': self.replace_source_bodies({hotfix.FALLBACK_SHARD_DIRECTORY + '/undeclared.json': b'{}'})
            else:
                value = copy.deepcopy(original); value['source_fallbacks']['shards'][0]['byte_size'] += 1
                self.replace_source_bodies({'data/i18n/manifest.json': json.dumps(value).encode()})
            with self.subTest(failure=failure), self.assertRaises((RuntimeError, S3Error)):
                self.run_prepare()
            self.assertEqual(self.client.trace, [])

    def test_full_clone_preserves_source_content_and_approved_ledger_with_manifest_last(self):
        before = copy.deepcopy(self.client.objects)
        retained = 'ko/report.html'; self.client.objects[self.target_prefix+retained] = copy.deepcopy(before[self.source_prefix+retained])
        self.client.put_object(Bucket=self.bucket, Key=self.target_prefix+'unlisted-secret.html', Body=b'old')
        self.client.trace.clear()
        result = self.run_prepare()
        for key, value in before.items(): self.assertEqual(self.client.objects[key], value, key)
        self.assertEqual(result['previous'], {'schema_version': 1, **self.active}); self.assertFalse(result['content_changed']); self.assertFalse(result['deployed'])
        self.assertGreaterEqual(result['reused_files'], 1); self.assertEqual(result['deleted_files'], 1)
        self.assertEqual(result['english_ledger_sha256'], self.ledger_hash)
        self.assertEqual(self.guard_calls, 4)
        self.assertNotIn(publish.incomplete_key('b'), self.client.objects)
        for path in ('blog/article.html', 'ko/report.html', 'data/i18n/manifest.json', 'sitemap-en.xml', *publish.DEFAULT_RUNTIME_PATHS):
            self.assertEqual(self.client.objects[self.target_prefix+path]['Body'], before[self.source_prefix+path]['Body'])
            self.assertNotIn(path, result['changed_files'])
        root = self.client.objects[self.target_prefix+'report.html']['Body']
        self.assertIn(b'Keep body', root); self.assertNotIn(b'?v=old', root)
        for relative in ('developer-api.html', 'activity.html'):
            old_html = before[self.source_prefix + relative]['Body']
            patched_html = hotfix.root_html_analytics_patch(relative, old_html)
            self.assertNotEqual(old_html, patched_html)
            self.assertEqual(self.client.objects[self.target_prefix + relative]['Body'],
                             hotfix.root_html_versions(patched_html, result['changed_files']))
            self.assertIn(relative, result['changed_files'])
        app = self.client.objects[self.target_prefix+'assets/app.js']['Body']
        self.assertEqual(self.client.objects[self.target_prefix+'assets/english-commentary.js']['Body'],
                         b'const SESSION = "deployment_auth_session";')
        leaf_hash = result['changed_files']['assets/site-feedback.js']['sha256'][:12].encode()
        self.assertIn(b'/assets/site-feedback.js?v='+leaf_hash, app)
        candidate = json.loads(self.client.objects[publish.manifest_key('b')]['Body'])
        for path in candidate['files']:
            if path.startswith('en/'):
                self.assertNotIn(b'PRIVATE_AUTHORIZED_BODY_ONLY', self.client.objects[self.target_prefix+path]['Body'])
        binding = json.loads(self.client.objects[english.PREFIX+'/releases/'+self.new_release+'/manifest.json']['Body'])
        self.assertEqual(binding['ledger_sha256'], self.ledger_hash)
        for filename in ('catalog.json', 'search_index.json', 'password_rules.json'):
            row = self.client.objects[publish.runtime_release_prefix(self.new_release)+filename]
            self.assertEqual(row['Body'], before[publish.runtime_release_prefix(self.old_release)+filename]['Body'])
            self.assertEqual(row['Metadata']['release-id'], self.new_release)
            self.assertEqual(row['CacheControl'], 'no-store')
        self.assertEqual(self.client.trace[0], ('put', publish.incomplete_key('b')))
        commit = self.client.trace.index(('put', publish.manifest_key('b')))
        self.assertFalse(any(row[0] in {'copy', 'put'} and row[1].startswith(self.target_prefix) for row in self.client.trace[commit+1:]))
        copies = [row for row in self.client.trace if row[0] == 'copy']
        self.assertTrue(all(row[3] == before[row[2]]['ETag'] for row in copies))
        self.assertFalse(any(row[0] == 'copy' and row[1] == self.target_prefix+retained for row in self.client.trace))

    def test_first_report_refresh_module_is_added_and_versioned_without_touching_reports(self):
        relative = 'assets/admin-report-refresh.js'
        self.client.objects.pop(self.source_prefix + relative)
        self.manifest['files'].pop(relative)
        self.manifest['file_count'] = len(self.manifest['files'])
        self.manifest['total_bytes'] = sum(row['size'] for row in self.manifest['files'].values())
        self.manifest['tree_sha256'] = static_tree_sha256(self.manifest['files'])
        self.active['tree_sha256'] = self.manifest['tree_sha256']
        publish.put_json(self.client, self.bucket, publish.manifest_key('a'), self.manifest)
        app = self.source/'assets/app.js'
        app.write_text(app.read_text() + ' import("/assets/admin-report-refresh.js?v=initial");')
        self.client.trace.clear()
        result = self.run_prepare()
        self.assertIn(relative, result['changed_files'])
        module = self.client.objects[self.target_prefix + relative]
        self.assertIn(module['ContentType'], ('text/javascript', 'application/javascript'))
        digest = hashlib.sha256(module['Body']).hexdigest()[:12].encode()
        self.assertIn(b'/assets/admin-report-refresh.js?v=' + digest,
                      self.client.objects[self.target_prefix + 'assets/app.js']['Body'])
        self.assertFalse(result['content_changed'])
        self.assertEqual(self.client.objects[self.target_prefix + 'data/catalog.json']['Body'],
                         self.client.objects[self.source_prefix + 'data/catalog.json']['Body'])

    def test_unapproved_added_asset_is_rejected_before_writes(self):
        with patch.object(hotfix, 'ASSETS', hotfix.ASSETS | {'extra-tool.js'}):
            with self.assertRaisesRegex(RuntimeError, 'unapproved asset'):
                self.run_prepare()
        self.assertEqual(self.client.trace, [])

    def test_new_admin_module_is_published_with_its_actual_loader_hash(self):
        relative = 'assets/admin-users.js'
        self.client.objects.pop(self.source_prefix + relative)
        self.manifest['files'].pop(relative)
        self.manifest['file_count'] = len(self.manifest['files'])
        self.manifest['total_bytes'] = sum(row['size'] for row in self.manifest['files'].values())
        self.manifest['tree_sha256'] = static_tree_sha256(self.manifest['files'])
        self.active['tree_sha256'] = self.manifest['tree_sha256']
        publish.put_json(self.client, self.bucket, publish.manifest_key('a'), self.manifest)
        app = self.source / 'assets/app.js'
        app.write_text(app.read_text() + ' import(new URL("assets/admin-users.js?v=initial", document.baseURI));')
        self.client.trace.clear()
        result = self.run_prepare()
        for asset in ('admin-users.js', 'account-services.js', 'newsfeed-app.js', 'styles.css'):
            self.assertIn('assets/' + asset, result['changed_files'])
        module = self.client.objects[self.target_prefix + relative]
        digest = hashlib.sha256(module['Body']).hexdigest()[:12].encode()
        self.assertIn(b'assets/admin-users.js?v=' + digest,
                      self.client.objects[self.target_prefix + 'assets/app.js']['Body'])
        self.assertFalse(result['content_changed'])

    def test_changed_active_before_commit_aborts_with_incomplete_target(self):
        def guard():
            self.guard_calls += 1
            if self.guard_calls == 3: raise RuntimeError('active changed')
        with self.assertRaisesRegex(RuntimeError, 'active changed'): self.run_prepare(guard)
        self.assertIn(publish.incomplete_key('b'), self.client.objects)
        self.assertNotIn(publish.manifest_key('b'), self.client.objects)
        self.assertNotIn(english.PREFIX+'/releases/'+self.new_release+'/manifest.json', self.client.objects)

    def test_source_precondition_failure_never_commits_candidate(self):
        self.client.reject_source = self.source_prefix+'data/catalog.json'
        with self.assertRaisesRegex(S3Error, 'PreconditionFailed'): self.run_prepare()
        self.assertIn(publish.incomplete_key('b'), self.client.objects)
        self.assertNotIn(publish.manifest_key('b'), self.client.objects)

    def test_missing_source_digest_is_not_treated_as_reusable(self):
        key = self.source_prefix+'ko/report.html'; self.client.objects[key]['Metadata'].pop('sha256')
        with self.assertRaisesRegex(RuntimeError, 'source object metadata differs'): self.run_prepare()
        self.assertNotIn(publish.manifest_key('b'), self.client.objects)

    def test_unknown_runtime_objects_rejected_before_any_mutation(self):
        self.client.put_object(Bucket=self.bucket, Key=publish.runtime_release_prefix(self.new_release)+'unexpected.json', Body=b'{}')
        self.client.trace.clear()
        with self.assertRaisesRegex(RuntimeError, 'unexpected objects'): self.run_prepare()
        self.assertEqual(self.client.trace, [])

    def test_retry_is_bounded_and_keeps_source_precondition(self):
        path = 'ko/report.html'; self.client.copy_failures = ['SlowDown', '503']; delays = []
        result = hotfix.copy_verified(self.client, self.bucket, self.source_prefix+path, self.target_prefix+path, self.manifest['files'][path], retry_sleep=delays.append)
        self.assertEqual(result, 'copied'); self.assertEqual(delays, [5, 10])
        copies = [row for row in self.client.trace if row[0] == 'copy']
        self.assertEqual(len(copies), 3); self.assertEqual(len({row[3] for row in copies}), 1)

    def test_ambiguous_successful_copy_is_read_back_before_retry(self):
        path = 'ko/report.html'; self.client.copy_response_error = 'SlowDown'; delays = []
        result = hotfix.copy_verified(self.client, self.bucket, self.source_prefix+path, self.target_prefix+path, self.manifest['files'][path], retry_sleep=delays.append)
        self.assertEqual(result, 'copied'); self.assertEqual(delays, [])
        self.assertEqual(sum(row[0] == 'copy' for row in self.client.trace), 1)

    def test_same_size_target_with_wrong_metadata_is_not_reused(self):
        path = 'ko/report.html'; self.client.objects[self.target_prefix+path] = copy.deepcopy(self.client.objects[self.source_prefix+path])
        self.client.objects[self.target_prefix+path]['ContentType'] = 'application/json'
        result = hotfix.copy_verified(self.client, self.bucket, self.source_prefix+path, self.target_prefix+path, self.manifest['files'][path])
        self.assertEqual(result, 'copied')
        self.assertEqual(self.client.objects[self.target_prefix+path]['ContentType'], 'text/html')

    def test_exact_destination_reuse_needs_one_head_and_no_source_read(self):
        path = 'ko/report.html'; source = self.source_prefix+path; target = self.target_prefix+path
        self.client.objects[target] = copy.deepcopy(self.client.objects[source])
        self.client.objects.pop(source)
        with patch.object(self.client, 'head_object', wraps=self.client.head_object) as head:
            self.assertEqual(hotfix.copy_verified(self.client, self.bucket, source, target,
                                                 self.manifest['files'][path]), 'reused')
        self.assertEqual(head.call_count, 1)
        self.assertEqual(head.call_args.kwargs['Key'], target)
        self.assertEqual(self.client.trace, [])

    def test_immutable_destination_reuse_requires_exact_release_and_never_overwrites(self):
        path = 'ko/report.html'; source = self.source_prefix+path; target = self.target_prefix+path
        self.client.objects[target] = copy.deepcopy(self.client.objects[source])
        self.client.objects[target]['Metadata']['release-id'] = self.new_release
        self.assertEqual(hotfix.copy_verified(self.client, self.bucket, source, target,
                                             self.manifest['files'][path], target_release=self.new_release), 'reused')
        self.client.objects[target]['Metadata']['release-id'] = self.old_release
        before = copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(RuntimeError, 'Immutable runtime object already exists'):
            hotfix.copy_verified(self.client, self.bucket, source, target,
                                 self.manifest['files'][path], target_release=self.new_release)
        self.assertEqual(self.client.objects, before)
        self.assertEqual(self.client.trace, [])

    def test_asset_symlink_is_rejected_before_mutation(self):
        path = self.source/'assets/course-full.js'; raw = path.read_bytes(); path.unlink()
        target = self.root/'outside.js'; target.write_bytes(raw); path.symlink_to(target)
        with self.assertRaisesRegex(RuntimeError, 'linked or oversized'): self.run_prepare()
        self.assertEqual(self.client.trace, [])

    def test_script_version_edit_preserves_comments_inline_text_and_other_attributes(self):
        raw = b'''<!-- <script src="assets/app.js?v=comment"></script> --><p>keep</p>
<script title=" src='assets/app.js?v=title'" data-src="assets/app.js?v=data" src='assets/app.js?v=real'></script>
<script>const text='<script src="assets/app.js?v=inline">';</script>'''
        changed = hotfix.root_html_versions(raw, self.manifest['files'])
        expected = raw.replace(b"src='assets/app.js?v=real'", b"src='assets/app.js?v="+self.manifest['files']['assets/app.js']['sha256'][:12].encode()+b"'")
        self.assertEqual(changed, expected)

    def test_stylesheet_version_changes_only_real_stylesheet_href(self):
        raw = b'''<!-- <link rel="stylesheet" href="assets/styles.css?v=comment"> -->
<link rel="canonical" href="assets/styles.css?v=canonical">
<link rel="stylesheet" data-href="assets/styles.css?v=data" href="assets/styles.css?v=old">
<p>assets/styles.css?v=body</p>'''
        changed = hotfix.root_html_versions(raw, self.manifest['files'])
        expected = raw.replace(b'href="assets/styles.css?v=old"',
            b'href="assets/styles.css?v=' + self.manifest['files']['assets/styles.css']['sha256'][:12].encode() + b'"')
        self.assertEqual(changed, expected)

    def test_developer_analytics_patch_changes_only_the_actual_body_flag_and_is_idempotent(self):
        raw = b'''<!doctype html><html><head><title>Published SEO title</title>
<link rel="canonical" href="https://public.example/developer-api.html"><meta name="robots" content="index,follow">
<!-- <body data-page="developer-api" data-analytics-auto="manual"> -->
<script>const sample='<body data-page="developer-api" data-analytics-auto="manual">';</script></head>
<body class='published' data-page='developer-api' data-analytics-auto='manual' data-extra="keep">
<h1>Published heading</h1><p>Keep published prose &amp; spacing.</p></body></html>'''
        expected = raw.replace(b" data-analytics-auto='manual'", b'')
        changed = hotfix.root_html_analytics_patch('developer-api.html', raw)
        self.assertEqual(changed, expected)
        self.assertEqual(hotfix.root_html_analytics_patch('developer-api.html', changed), changed)
        self.assertEqual(hotfix.root_html_analytics_patch('report.html', raw), raw)
        self.assertEqual(hotfix.root_html_analytics_patch('ko/developer-api.html', raw), raw)

    def test_activity_patch_changes_only_approved_event_options_and_is_idempotent(self):
        prefix = '''<!doctype html><html><head><title>Live private activity title</title>
<link rel="canonical" href="https://public.example/activity.html"><meta name="robots" content="noindex,nofollow">
<!-- <select id="analyticsHistoryType">Do not touch</select> -->
<script>const sample='<select id="analyticsHistoryType">Do not touch</select>';</script></head>
<body data-page="activity"><h1>Live heading</h1><select id="unrelated"><option>keep</option></select>
<select class="published" id='analyticsHistoryType' aria-label="Keep label">'''
        suffix = '</select><p>Live counts and body remain unchanged.</p></body></html>'
        raw = (prefix + hotfix.ACTIVITY_OPTIONS_BEFORE + suffix).encode()
        expected = (prefix + hotfix.ACTIVITY_OPTIONS_AFTER + suffix).encode()
        changed = hotfix.root_html_analytics_patch('activity.html', raw)
        self.assertEqual(changed, expected)
        self.assertEqual(hotfix.root_html_analytics_patch('activity.html', changed), changed)
        for event in ('report_text_view', 'membership_request', 'report_request', 'newsfeed_interaction',
                      'newsfeed_topic_request', 'journey_interaction', 'form_confirmation', 'reward_checkin', 'reward_claim'):
            self.assertEqual(changed.count(f'<option value="{event}">'.encode()), 1)

    def test_analytics_html_patch_rejects_missing_ambiguous_or_unexpected_markup(self):
        developer_cases = [
            '<div data-page="developer-api"></div>',
            '<body data-page="report" data-analytics-auto="manual">',
            '<body data-page="developer-api" data-page="developer-api">',
            '<body data-page="developer-api" data-analytics-auto="off">',
            '<body data-page="developer-api" data-analytics-auto="manual" data-analytics-auto="manual">',
            '<body data-page="developer-api" data-analytics-auto="&#109;anual">',
            '<body data-page="developer-api"></body><body data-page="developer-api">',
            '<body data-page="developer-api" />',
        ]
        for raw in developer_cases:
            with self.subTest(page='developer-api.html', html=raw), self.assertRaises(RuntimeError):
                hotfix.root_html_analytics_patch('developer-api.html', raw.encode())
        original = '<body data-page="activity"><select id="analyticsHistoryType">' + hotfix.ACTIVITY_OPTIONS_BEFORE + '</select></body>'
        activity_cases = [
            original.replace('id="analyticsHistoryType"', 'id="other"'),
            original.replace('id="analyticsHistoryType"', 'id="analyticsHistoryType" id="analyticsHistoryType"'),
            original.replace('</select>', ''),
            original.replace('</select>', '</select><select id="analyticsHistoryType"></select>'),
            original.replace('打开报告', 'Unreviewed changed label'),
            original.replace('<option value="search">搜索</option>', '<option value="custom">Custom event</option>'),
            original.replace('</select>', '<select></select></select>'),
        ]
        for raw in activity_cases:
            with self.subTest(page='activity.html', html=raw[:100]), self.assertRaises(RuntimeError):
                hotfix.root_html_analytics_patch('activity.html', raw.encode())

    def test_unexpected_live_analytics_options_fail_before_any_target_write(self):
        relative = 'activity.html'; key = self.source_prefix + relative
        raw = self.client.objects[key]['Body'].replace('打开报告'.encode(), b'Unknown live option')
        row = hotfix.descriptor_with_body(self.manifest['files'][relative], raw)
        self.manifest['files'][relative] = row
        self.manifest['tree_sha256'] = static_tree_sha256(self.manifest['files'])
        self.manifest['total_bytes'] = sum(item['size'] for item in self.manifest['files'].values())
        self.active['tree_sha256'] = self.manifest['tree_sha256']
        self.client.put_object(Bucket=self.bucket, Key=key, Body=raw, **publish.upload_extra_args(row))
        publish.put_json(self.client, self.bucket, publish.manifest_key('a'), self.manifest)
        self.client.trace.clear()
        with self.assertRaisesRegex(RuntimeError, 'Unexpected analytics event options'):
            self.run_prepare()
        self.assertEqual(self.client.trace, [])

    def test_missing_live_analytics_page_fails_before_any_target_write(self):
        self.manifest['files'].pop('developer-api.html')
        with self.assertRaisesRegex(RuntimeError, 'Required analytics root HTML is missing'):
            hotfix.build_patch(self.client, self.bucket, self.active, self.manifest, self.source, self.locale, None)
        self.assertEqual(self.client.trace, [])


if __name__ == '__main__': unittest.main()
