"""Original-source and terminal-recovery regressions using real ledger state."""
import copy
from contextlib import chdir
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import recover_institution_mineru as r
import mineru_task_ledger as m
from mineru_terminal_recovery import failure_hash
from inspect_durable_mineru import failure_message_hash
from test_mineru_result_cache import MemoryR2
from test_mineru_terminal_recovery import Provider, ERROR

PROVIDER_ERROR = {'err_msg': 'parsing failed, please try again later'}
REVIEWED_ERROR_HASH = '0401d529faef13a557a665756d64dc03c646206ce7e74b41854493ec66695f4d'


def pdf_bytes(label):
    # The primary producer now inspects the physical page count before submit.
    # Bind and archive these real one-page bytes, never a PDF-looking stub.
    import fitz
    with fitz.open() as document:
        document.new_page().insert_text((72, 72), label)
        return document.tobytes(no_new_id=True)


class InstitutionRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.r2 = MemoryR2()
        self.store = m.R2Store('institution', client=self.r2, bucket='private-test')
        self.provider = Provider()
        self.ledger = m.Ledger(self.store, self.provider, 'institution', 'https://mineru.net',
                              {'model': 'vlm', 'language': 'en', 'ocr': True}, [('MINER_U', 'test-token')])
        self.inputs, self.payloads = [], {}
        for index in range(3):
            path = self.root/f'IMF_report-{index}.pdf'; raw = pdf_bytes('Original '+str(index)); path.write_bytes(raw)
            self.inputs.append((path, path.name)); self.payloads['https://www.imf.org/'+path.name] = raw
        items = [self.ledger.bind(*row) for row in self.inputs]
        self.key = self.ledger._create(items, {item['id']: path for item, (path, _) in zip(items, self.inputs)}, self.ledger.clock()+60)
        self.originals = copy.deepcopy(self.r2.objects)
        self.value = {'source_runs': ['123'], 'batches': [self.key], 'allowed_error_hashes': [failure_hash(ERROR)]}
        self.urls = {path.name: {'https://www.imf.org/'+path.name} for path, _ in self.inputs}
        self.directory = self.root/'frozen'

    def prepare(self, fetch=None):
        return r.prepare(self.ledger, self.value, self.urls, self.directory,
                         fetch=fetch or (lambda url, size: self.payloads[url]))

    def provider_error(self, error=PROVIDER_ERROR):
        def results(batch_id, items):
            plan = self.provider.plans[min(int(batch_id)-1, len(self.provider.plans)-1)]
            return [{'data_id': item['id'], 'state': state,
                     **({'full_zip_url': 'https://results.invalid/'+batch_id+'/'+item['id']}
                        if state == 'done' else copy.deepcopy(error))}
                    for item, state in zip(items, plan)]
        self.provider.on_poll = results

    def add_original(self):
        path = self.root/'IMF_later.pdf'; raw = pdf_bytes('Later report'); path.write_bytes(raw)
        binding = self.ledger.bind(path, path.name)
        key = self.ledger._create([binding], {binding['id']: path}, self.ledger.clock()+60)
        self.value['batches'].append(key)
        self.urls[path.name] = {'https://www.imf.org/'+path.name}
        self.payloads['https://www.imf.org/'+path.name] = raw
        return key

    def test_prepare_proves_every_original_and_does_not_poll_or_mutate_tasks(self):
        result = self.prepare()
        self.assertTrue(result['verified']); self.assertEqual(result['original_members'], 3)
        self.assertEqual(self.r2.objects, self.originals)
        self.assertEqual((len(self.provider.posts), len(self.provider.polls)), (1, 0))

    def test_primary_institution_cli_archives_every_original_before_provider_poll(self):
        import os, sys
        import pdf_to_xhs_batch as cli
        from institution_original_cache import OriginalCache
        cache = OriginalCache(self.r2, 'private-test')
        def inspect_archived(*_):
            for source in self.inputs:
                self.assertEqual(cache.get(self.ledger.bind(*source)), source[0].read_bytes())
        self.provider.on_poll = inspect_archived
        args = ['pdf', '--input-dir', str(self.root), '--output-dir', str(self.root/'out'), '--chart-source-only']
        with patch.object(sys, 'argv', args), patch.dict(os.environ, {'MINER_U': 'test-token'}), \
             patch.object(cli, 'from_environment', return_value=self.ledger), patch.object(cli, 'log'):
            self.assertEqual(cli.main(), 2)
        self.assertEqual(len(self.provider.posts), 1)
        self.assertTrue(self.provider.polls)

    def test_fresh_institution_submission_cannot_precede_verified_private_originals(self):
        import os, sys
        import pdf_to_xhs_batch as cli
        from institution_original_cache import OriginalCache
        self.r2.objects.clear(); self.provider.posts.clear(); self.provider.tasks.clear()
        self.provider.plans = [['done', 'done', 'done']]
        cache = OriginalCache(self.r2, 'private-test')
        def before_submission(_batch):
            for source in self.inputs:
                self.assertEqual(cache.get(self.ledger.bind(*source)), source[0].read_bytes())
        self.provider.on_submit = before_submission
        args = ['pdf', '--input-dir', str(self.root), '--output-dir', str(self.root/'out'), '--chart-source-only']
        with patch.object(sys, 'argv', args), patch.dict(os.environ, {'MINER_U': 'test-token'}), \
             patch.object(cli, 'from_environment', return_value=self.ledger), patch.object(cli, 'log'), \
             patch.object(cli, 'process_pdf', return_value={'chart_source_only': True}):
            self.assertEqual(cli.main(), 0)
        self.assertEqual(len(self.provider.posts), 1)

    def test_private_original_read_failure_stops_primary_before_any_provider_operation(self):
        import os, sys
        import pdf_to_xhs_batch as cli
        from institution_original_cache import PREFIX
        def fail_cache(key):
            if key.startswith(PREFIX): raise OSError('private read stopped')
        self.r2.before_get = fail_cache
        args = ['pdf', '--input-dir', str(self.root), '--output-dir', str(self.root/'out'), '--chart-source-only']
        with patch.object(sys, 'argv', args), patch.dict(os.environ, {'MINER_U': 'test-token'}), \
             patch.object(cli, 'from_environment', return_value=self.ledger), patch.object(cli, 'log'), \
             patch('builtins.print'):
            self.assertNotEqual(cli.main(), 0)
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.provider.polls, [])

    def test_verified_private_originals_avoid_official_url_discovery_and_fetch(self):
        originals = {self.ledger.bind(*row)['id']: row[0].read_bytes() for row in self.inputs}
        result = r.prepare(self.ledger, self.value,
            lambda *_: self.fail('Frozen originals require no GitHub log discovery'), self.directory,
            restore=lambda item: originals[item['id']], fetch=lambda *_: self.fail('No official source fetch'))
        self.assertTrue(result['verified'])
        self.assertEqual((result['restored_original_members'], result['downloaded_original_members']), (3, 0))
        self.assertEqual(self.r2.objects, self.originals)

    def test_missing_private_original_only_fetches_the_missing_exact_source(self):
        first = self.ledger.bind(*self.inputs[0]); requests = []; wanted = []
        def registry(names): wanted.append(names); return self.urls
        def restore(item): return None if item['id'] == first['id'] else self.root.joinpath(item['source']).read_bytes()
        def fetch(url, size): requests.append(url); return self.payloads[url]
        result = r.prepare(self.ledger, self.value, registry, self.directory, restore=restore, fetch=fetch)
        self.assertEqual(wanted, [{first['source']}]); self.assertEqual(len(requests), 1)
        self.assertEqual((result['restored_original_members'], result['downloaded_original_members']), (2, 1))

    def test_private_original_mismatch_or_read_error_stops_before_public_fetch(self):
        for restore in (lambda *_: b'%PDF-wrong', lambda *_: (_ for _ in ()).throw(OSError('storage unavailable'))):
            with self.subTest(restore=restore), self.assertRaises((ValueError, OSError)):
                r.prepare(self.ledger, self.value, lambda *_: self.fail('No discovery after cache error'), self.directory,
                    restore=restore, fetch=lambda *_: self.fail('No public fetch after cache error'))
        self.assertFalse(self.directory.exists()); self.assertEqual(self.r2.objects, self.originals)

    def test_missing_original_url_stops_before_any_download_or_provider_operation(self):
        self.urls.pop(self.inputs[-1][1]); calls = []
        result = self.prepare(lambda *args: calls.append(args))
        self.assertEqual((result['verified'], result['missing_url_count']), (False, 1))
        self.assertEqual(calls, []); self.assertFalse(self.directory.exists())
        self.assertEqual(self.r2.objects, self.originals)

    def test_changed_original_bytes_never_authorize_submission_or_claim_reset(self):
        self.payloads[next(iter(self.payloads))] = b'%PDF-different'
        with self.assertRaisesRegex(ValueError, 'original_source_bytes_changed'): self.prepare()
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_same_publication_filename_selects_exact_original_chapter_bytes(self):
        name = self.inputs[0][1]; original_url = next(iter(self.urls[name]))
        self.urls[name] = {'https://www.imf.org/0-earlier-chapter.pdf', original_url,
                           'https://www.imf.org/1-different-chapter.pdf', 'https://www.imf.org/z-latest-chapter.pdf'}
        original = self.payloads.pop(original_url)
        self.payloads[original_url] = original
        calls = []
        def fetch(url, size):
            calls.append(url)
            if url.endswith('0-earlier-chapter.pdf'): raise ValueError('source_length')
            if url.endswith('1-different-chapter.pdf'): return b'%PDF-modified-0'
            if url.endswith('z-latest-chapter.pdf'): return b'%PDF-new-chapter'
            return self.payloads[url]
        proof = self.prepare(fetch)
        self.assertTrue(proof['verified'])
        binding = self.ledger.bind(*self.inputs[0])
        self.assertEqual((self.directory/binding['id']).read_bytes(), original)
        self.assertIn('https://www.imf.org/0-earlier-chapter.pdf', calls)
        self.assertIn('https://www.imf.org/1-different-chapter.pdf', calls)
        self.assertNotIn('https://www.imf.org/z-latest-chapter.pdf', calls)
        self.assertEqual(self.r2.objects, self.originals); self.assertEqual(len(self.provider.posts), 1)

    def test_all_candidate_byte_mismatches_and_too_many_urls_do_not_authorize_retry(self):
        name = self.inputs[0][1]
        self.urls[name] = {'https://www.imf.org/ch1.pdf', 'https://www.imf.org/ch2.pdf'}
        with self.assertRaisesRegex(ValueError, 'original_source_bytes_changed'):
            self.prepare(lambda *_: b'%PDF-unrelated')
        self.assertEqual(self.r2.objects, self.originals); self.assertEqual(len(self.provider.posts), 1)
        self.directory.rmdir()
        self.urls[name] = {'https://www.imf.org/ch'+str(i)+'.pdf' for i in range(r.MAX_SOURCE_URLS+1)}
        result = self.prepare(lambda *_: self.fail('Unbounded candidates must stop before downloads'))
        self.assertFalse(result['verified']); self.assertEqual(result['missing_url_count'], 1)

    def test_two_original_batches_keep_distinct_bytes_under_the_same_filename(self):
        name = self.inputs[0][1]
        newer = self.root/'newer'/name; newer.parent.mkdir()
        newer_raw = pdf_bytes('Revised  0'); newer.write_bytes(newer_raw)
        self.assertEqual(len(newer_raw), len(self.inputs[0][0].read_bytes()))
        binding = self.ledger.bind(newer, name)
        key = self.ledger._create([binding], {binding['id']: newer}, self.ledger.clock()+60)
        self.value['batches'].append(key)
        url = 'https://www.imf.org/revised-chapter.pdf'
        self.urls[name].add(url); self.payloads[url] = newer_raw
        before = copy.deepcopy(self.r2.objects)
        proof = self.prepare()
        self.assertTrue(proof['verified']); self.assertEqual(proof['original_members'], 4)
        original_binding = self.ledger.bind(*self.inputs[0])
        self.assertNotEqual(original_binding['id'], binding['id'])
        self.assertEqual((self.directory/original_binding['id']).read_bytes(), self.inputs[0][0].read_bytes())
        self.assertEqual((self.directory/binding['id']).read_bytes(), newer_raw)
        self.assertEqual(self.r2.objects, before); self.assertEqual(len(self.provider.posts), 2)

    def test_alternative_candidate_does_not_hide_transport_or_status_failure(self):
        name = self.inputs[0][1]; self.urls[name].add('https://www.imf.org/other.pdf')
        calls = []
        def fetch(*args): calls.append(args); raise OSError('transport stopped')
        with self.assertRaises(OSError): self.prepare(fetch)
        self.assertEqual(len(calls), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_source_http_failure_keeps_status_and_only_bounded_identity_diagnostics(self):
        name = self.inputs[0][1]; self.urls[name].add('https://www.imf.org/other.pdf')
        calls = []
        def fetch(*args): calls.append(args); raise r.SourceHTTPError(403)
        with self.assertRaises(r.SourceHTTPError) as caught: self.prepare(fetch)
        self.assertEqual(caught.exception.status, 403)
        details = caught.exception.source_diagnostic
        self.assertEqual(details['source_name_sha256'], m.digest(name.encode()))
        self.assertEqual(details['candidate_url_sha256'], m.digest(calls[0][0].encode()))
        self.assertEqual((details['verified_original_members'], details['original_members'], details['provider_posts']), (0, 3, 0))
        self.assertNotIn(name, json.dumps(details)); self.assertNotIn('https:', json.dumps(details))
        self.assertEqual(len(calls), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_download_uses_original_producer_headers_and_preserves_http_status(self):
        from fetch_institution_latest_pdfs import source_request_headers, DEFAULT_USER_AGENT
        from unittest.mock import MagicMock
        response = MagicMock(); response.__enter__.return_value = response; response.status_code = 503
        with patch('requests.get', return_value=response) as request:
            with self.assertRaises(r.SourceHTTPError) as caught:
                r.download('https://www.imf.org/original.pdf', 15)
        self.assertEqual(caught.exception.status, 503)
        self.assertEqual(request.call_count, 1)
        kwargs = request.call_args.kwargs
        self.assertEqual(kwargs['headers'], source_request_headers())
        self.assertEqual(kwargs['headers']['User-Agent'], DEFAULT_USER_AGENT)
        self.assertEqual(source_request_headers('custom-producer-agent')['User-Agent'], 'custom-producer-agent')
        self.assertFalse(kwargs['allow_redirects']); self.assertTrue(kwargs['stream'])
        self.assertNotIn('verify', kwargs); self.assertNotIn('proxies', kwargs)
        response.iter_content.assert_not_called()

    def test_recovery_retries_only_failed_members_and_preserves_original_claims(self):
        proof = self.prepare(); verified = []
        summary = r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'],
                            verifier=lambda path, row: verified.append(row['data_id']))
        self.assertTrue(summary['ready_for_generation']); self.assertEqual(summary['completed'], 3)
        self.assertEqual(summary['provider_posts'], 2)
        original_ids = [item['id'] for item in self.provider.posts[0][0]]
        self.assertEqual([item['id'] for item in self.provider.posts[1][0]], original_ids[1:])
        self.assertEqual([item['id'] for item in self.provider.posts[2][0]], original_ids[2:])
        self.assertEqual(set(verified), set(original_ids))
        for key, value in self.originals.items(): self.assertEqual(self.r2.objects[key], value)
        # Replaying the same complete proof consumes accepted children, no POST.
        again = r.recover(self.ledger, self.directory, run_id='457', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertTrue(again['ready_for_generation']); self.assertEqual(again['provider_posts'], 0)

    def test_reviewed_six_field_provider_error_bridges_without_rewriting_proof(self):
        self.assertEqual(failure_message_hash(PROVIDER_ERROR), REVIEWED_ERROR_HASH)
        self.assertNotEqual(failure_hash(PROVIDER_ERROR), REVIEWED_ERROR_HASH)
        self.provider_error(); self.value['allowed_error_hashes'] = [REVIEWED_ERROR_HASH]
        proof = self.prepare(); frozen = (self.directory/'proof.json').read_bytes()
        self.assertEqual(self.provider.polls, [])
        result = r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'],
                           verifier=lambda *_: None)
        self.assertEqual((result['completed'], result['provider_posts']), (3, 2))
        self.assertEqual((self.directory/'proof.json').read_bytes(), frozen)
        self.assertEqual(json.loads(frozen)['allowed_error_hashes'], [REVIEWED_ERROR_HASH])
        control, _ = self.store.get('recoveries/'+self.key.split('/')[1])
        self.assertEqual(control['policy']['allowed_error_hashes'],
                         sorted([REVIEWED_ERROR_HASH, failure_hash(PROVIDER_ERROR)]))
        for entry in control['children']:
            self.assertEqual({item['error_hash'] for item in entry['proof']['value']['members']
                              if item['state'] == 'failed'}, {failure_hash(PROVIDER_ERROR)})
        before = copy.deepcopy(self.r2.objects)
        replay = r.recover(self.ledger, self.directory, run_id='457', expected_proof=proof['proof_sha256'],
                           verifier=lambda *_: None)
        self.assertTrue(replay['ready_for_generation']); self.assertEqual(replay['provider_posts'], 0)
        self.assertEqual(self.r2.objects, before)

    def test_real_provider_error_legacy_authorization_replays_byte_identical(self):
        self.provider_error(); legacy = failure_hash(PROVIDER_ERROR)
        self.value['allowed_error_hashes'] = [legacy]; proof = self.prepare()
        r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        control, _ = self.store.get('recoveries/'+self.key.split('/')[1])
        self.assertEqual(control['policy']['allowed_error_hashes'], [legacy])
        before = copy.deepcopy(self.r2.objects)
        replay = r.recover(self.ledger, self.directory, run_id='457', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        self.assertEqual(replay['provider_posts'], 0); self.assertEqual(self.r2.objects, before)

    def test_unreviewed_six_field_error_cannot_inherit_legacy_bridge(self):
        self.provider_error({**PROVIDER_ERROR, 'error_message': 'different current failure'})
        self.value['allowed_error_hashes'] = [REVIEWED_ERROR_HASH]; proof = self.prepare()
        with self.assertRaisesRegex(m.LedgerError, 'not explicitly authorized'):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_error_change_after_bridge_preflight_still_stops_before_post(self):
        self.provider_error(); original_poll = self.provider.on_poll
        def changing(batch_id, items):
            rows = original_poll(batch_id, items)
            if len(self.provider.polls) > 1:
                for row in rows:
                    if row['state'] == 'failed': row['message'] = 'unreviewed new detail'
            return rows
        self.provider.on_poll = changing
        self.value['allowed_error_hashes'] = [REVIEWED_ERROR_HASH]; proof = self.prepare()
        with self.assertRaisesRegex(m.LedgerError, 'not explicitly authorized'):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_later_unknown_reviewed_digest_stops_all_root_submissions(self):
        self.add_original(); self.provider.plans = [['failed']*3, ['failed']]
        self.provider_error(); original_poll = self.provider.on_poll
        self.value['allowed_error_hashes'] = [REVIEWED_ERROR_HASH]; proof = self.prepare()
        roots = json.loads((self.directory/'proof.json').read_bytes())['roots']
        def later_unknown(batch_id, items):
            rows = original_poll(batch_id, items)
            if batch_id == roots[-1]['batch_id']:
                for row in rows: row['message'] = 'unknown later root'
            return rows
        self.provider.on_poll = later_unknown; before = copy.deepcopy(self.r2.objects)
        with self.assertRaisesRegex(m.LedgerError, 'not explicitly authorized'):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        self.assertEqual(len(self.provider.posts), 2); self.assertEqual(self.r2.objects, before)

    def test_later_controller_policy_mismatch_stops_all_root_submissions(self):
        self.add_original(); self.provider.plans = [['failed']*3, ['failed']]
        self.provider_error(); self.value['allowed_error_hashes'] = [REVIEWED_ERROR_HASH]; proof = self.prepare()
        root = json.loads((self.directory/'proof.json').read_bytes())['roots'][-1]
        policy = r.TerminalRecovery(self.ledger, allowed_error_hashes=[failure_hash(PROVIDER_ERROR)]).policy
        self.store.put('recoveries/'+root['key'].split('/')[1], {'schema': 1, 'policy': policy,
            'root_key': root['key'], 'root_identity_sha256': r.task_identity(root), 'children': []})
        before = copy.deepcopy(self.r2.objects)
        with self.assertRaisesRegex(m.LedgerError, 'fixed policy'):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        self.assertEqual(len(self.provider.posts), 2); self.assertEqual(self.r2.objects, before)

    def test_reviewed_bridge_waits_for_all_frozen_original_roots(self):
        self.add_original(); self.provider_error(); self.value['allowed_error_hashes'] = [REVIEWED_ERROR_HASH]
        proof = self.prepare(); saved = json.loads((self.directory/'proof.json').read_bytes())
        (self.directory/saved['roots'][-1]['files'][-1]['id']).write_bytes(b'%PDF-tampered')
        before = copy.deepcopy(self.r2.objects)
        with self.assertRaises(m.LedgerError):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *_: None)
        self.assertEqual((len(self.provider.posts), len(self.provider.polls)), (2, 0))
        self.assertEqual(self.r2.objects, before)

    def test_changed_last_frozen_file_stops_before_first_retry(self):
        proof = self.prepare(); value = json.loads((self.directory/'proof.json').read_bytes())
        (self.directory/value['roots'][0]['files'][-1]['id']).write_bytes(b'%PDF-changed')
        with self.assertRaises(m.LedgerError):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_later_original_root_mismatch_stops_before_first_root_retry(self):
        path = self.root/'IMF_later.pdf'; raw = pdf_bytes('Later report'); path.write_bytes(raw)
        binding = self.ledger.bind(path, path.name)
        later_key = self.ledger._create([binding], {binding['id']: path}, self.ledger.clock()+60)
        self.value['batches'].append(later_key)
        self.urls[path.name] = {'https://www.imf.org/'+path.name}
        self.payloads['https://www.imf.org/'+path.name] = raw
        proof = self.prepare()
        saved = json.loads((self.directory/'proof.json').read_bytes())
        (self.directory/saved['roots'][-1]['files'][-1]['id']).write_bytes(b'%PDF-tampered')
        before = copy.deepcopy(self.r2.objects)
        with self.assertRaises(m.LedgerError):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertEqual(len(self.provider.posts), 2); self.assertEqual(self.r2.objects, before)

    def test_unknown_failure_hash_never_creates_child(self):
        self.value['allowed_error_hashes'] = ['f'*64]; proof = self.prepare()
        with self.assertRaisesRegex(m.LedgerError, 'not explicitly authorized'):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_original_success_result_must_verify_before_retrying_failed_members(self):
        proof = self.prepare()
        with self.assertRaises(m.LedgerError):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'],
                      verifier=lambda *args: (_ for _ in ()).throw(ValueError('bad result')))
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_retry_budget_is_two_children_even_when_provider_keeps_failing(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['failed', 'failed'], ['failed', 'failed']]
        proof = self.prepare()
        result = r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertFalse(result['ready_for_generation']); self.assertEqual((result['completed'], result['failed'], result['provider_posts']), (1, 2, 2))
        again = r.recover(self.ledger, self.directory, run_id='457', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertEqual(again['provider_posts'], 0)

    def test_private_source_freeze_requires_exact_readback_and_preserves_existing_objects(self):
        from portal_extended_r2 import R2NotFound
        result = self.prepare()
        class Store:
            def __init__(self): self.objects = {}; self.writes = 0
            def _get(self, key, **kwargs):
                if key not in self.objects: raise R2NotFound(key)
                return self.objects[key]
            def _put(self, key, raw, **kwargs): self.objects[key] = raw; self.writes += 1
        store = Store(); r.freeze_sources(store, self.directory, result['proof_sha256'])
        self.assertEqual(store.writes, 4)
        r.freeze_sources(store, self.directory, result['proof_sha256']); self.assertEqual(store.writes, 4)
        store.objects[next(iter(store.objects))] = b'changed'
        with self.assertRaisesRegex(ValueError, 'private_source_conflict'):
            r.freeze_sources(store, self.directory, result['proof_sha256'])

    def test_registry_ignores_unrelated_historical_urls_before_validation(self):
        archive = self.root/'institution_feeds/institution_pdf_archive.jsonl'; archive.parent.mkdir()
        archive.write_text(json.dumps({'local_filename': 'unrelated.pdf', 'pdf_url': 'https://web-assets.bcg.com/a.pdf'})+'\n')
        metadata = {'id': 123, 'path': r.PRODUCER, 'head_branch': 'main', 'event': 'schedule', 'status': 'completed',
                    'head_sha': 'a'*40, 'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'}}
        logs = ' saved unrelated.pdf (1 KB) <- https://www.rand.org/old.pdf\n'
        logs += '\n'.join(' saved '+path.name+' (1 KB) <- https://www.imf.org/'+path.name for path, _ in self.inputs)
        with chdir(self.root), patch.object(r, 'gh', side_effect=lambda *args: json.dumps(metadata) if args[0]=='api' else logs):
            self.assertEqual(r.registry(self.value, 'owner/repo', set(self.urls)), self.urls)

    def test_official_url_and_producer_identity_reject_changed_authority(self):
        for url in ('http://www.imf.org/a.pdf', 'https://imf.org.attacker.invalid/a.pdf',
                    'https://user:pass@www.imf.org/a.pdf', 'https://127.0.0.1/a.pdf', 'https://www.imf.org:4430/a.pdf'):
            with self.subTest(url=url), self.assertRaises(ValueError): r.official_url(url)
        with self.assertRaisesRegex(ValueError, 'source_producer'):
            r.producer({'id': 123, 'path': r.PRODUCER, 'head_branch': 'fork'}, '123', 'owner/repo')

    def test_request_rejects_duplicate_roots_and_unbounded_discovery(self):
        self.assertEqual(r.request(self.value), self.value)
        for broken in ({**self.value, 'batches': [self.key, self.key]}, {**self.value, 'source_runs': [str(i) for i in range(1, 8)]},
                       {**self.value, 'allowed_error_hashes': []}):
            with self.assertRaises(ValueError): r.request(broken)


if __name__ == '__main__': unittest.main()
