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
from portal_english_ui import PUBLIC_ASSET_NAMES, detail, homepage
from verify_prepared_static_slot import static_tree_sha256


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
                       'ko/report.html': b'<body>Unchanged locale shell</body>', 'data/i18n/manifest.json': b'{"translation":"retained"}',
                       'robots.txt': b'User-agent: *\nAllow: /\n', 'sitemap-en.xml': b'<urlset>retained sitemap</urlset>'})
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


if __name__ == '__main__': unittest.main()
