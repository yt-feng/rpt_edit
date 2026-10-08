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
from test_mineru_result_cache import MemoryR2
from test_mineru_terminal_recovery import Provider, ERROR


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
            path = self.root/f'IMF_report-{index}.pdf'; raw = b'%PDF-original-'+str(index).encode(); path.write_bytes(raw)
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

    def test_prepare_proves_every_original_and_does_not_poll_or_mutate_tasks(self):
        result = self.prepare()
        self.assertTrue(result['verified']); self.assertEqual(result['original_members'], 3)
        self.assertEqual(self.r2.objects, self.originals)
        self.assertEqual((len(self.provider.posts), len(self.provider.polls)), (1, 0))

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

    def test_changed_last_frozen_file_stops_before_first_retry(self):
        proof = self.prepare(); value = json.loads((self.directory/'proof.json').read_bytes())
        (self.directory/value['roots'][0]['files'][-1]['id']).write_bytes(b'%PDF-changed')
        with self.assertRaises(m.LedgerError):
            r.recover(self.ledger, self.directory, run_id='456', expected_proof=proof['proof_sha256'], verifier=lambda *args: None)
        self.assertEqual(len(self.provider.posts), 1); self.assertEqual(self.r2.objects, self.originals)

    def test_later_original_root_mismatch_stops_before_first_root_retry(self):
        path = self.root/'IMF_later.pdf'; raw = b'%PDF-later'; path.write_bytes(raw)
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
