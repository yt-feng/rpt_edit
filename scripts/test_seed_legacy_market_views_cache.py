"""Offline original-artifact, accepted legacy membership and private cache tests."""
import base64
import copy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
import zipfile
import mineru_pinned_result_transport as pinned

import seed_legacy_market_views_cache as seed
import inspect_legacy_mineru as inspect
from test_mineru_result_cache import MemoryR2, result_zip
from test_mineru_pinned_result_transport import authentication


def archive_bytes(rows):
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w') as archive:
        for name, data in rows:
            archive.writestr(name, data)
    return out.getvalue()


class LegacyTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.repository = 'example/report-repository'
        self.run = '12345'; self.sha = 'a' * 40
        self.api_calls = []; self.gets = []
        self.base = f'repos/{self.repository}/'
        self.code = {name: ('reviewed ' + name).encode() for name in seed.ORIGINAL_CODE}
        self.hashes = {name: seed.digest(raw) for name, raw in self.code.items()}
        self.names = [f'private-source-{index}.pdf' for index in range(6)]
        self.sources = {name: b'%PDF-1.7\nexact original ' + str(index).encode() for index, name in enumerate(self.names)}
        self.rows = [{'process_local_path': name, 'name': name, 'content_sha256': seed.digest(raw),
                      'dropbox_path': '/zip_backup/261001/' + name} for name, raw in self.sources.items()]
        self.manifest = seed.canonical(self.rows)
        self.archive = archive_bytes(list(self.sources.items()) + [(seed.MANIFEST, self.manifest)])
        self.responses = {}
        self.run_meta = {'id': int(self.run), 'path': seed.PRODUCER, 'head_branch': 'main', 'status': 'completed',
                         'conclusion': 'failure', 'event': 'schedule', 'head_sha': self.sha,
                         'repository': {'full_name': self.repository}, 'head_repository': {'full_name': self.repository}}
        self.artifact = {'id': 777, 'name': 'selected-macro-pdfs-' + self.run, 'expired': False,
                         'workflow_run': {'id': int(self.run)}, 'size_in_bytes': len(self.archive),
                         'digest': 'sha256:' + seed.digest(self.archive)}
        self.jobs = []
        self.logs = {}
        for shard in range(2):
            names = self.names[shard * 5:(shard + 1) * 5]
            job = {'id': 900 + shard, 'name': f'process-shard ({shard})', 'run_id': int(self.run),
                   'head_sha': self.sha, 'status': 'completed', 'conclusion': 'success'}
            self.jobs.append(job)
            lines = ['[command]/usr/bin/git log -1 --format=%H', self.sha,
                     f'Found 6 total PDFs; shard {shard}/40 has {len(names)} PDFs, skips 0 already converted, will process {len(names)} PDFs with batch_size=5.',
                     f'Running batch 1: {len(names)} PDFs']
            copied = [{'source': '/work/_selected_macro_pdfs/' + name, 'batch_file': '/tmp/exact/pdfs/' + seed.consumer.copied_name(name, index),
                       'stable_index': str(index)} for index, name in enumerate(names, 1)]
            ids = [seed.consumer.data_id(Path(row['batch_file']).name) for row in copied]
            for attempt, slot in enumerate(('MINER_U', 'MINER_U_2', 'MINER_U_3', 'MINER_U_4'), 1):
                batch_id = f'00000000-0000-4000-8000-{shard * 4 + attempt:012d}'
                lines.append(f'MinerU attempt {attempt}/4 using {slot}: submitting {len(names)} PDF(s).')
                lines.extend('Uploading PDF to MinerU: ' + row['batch_file'] for row in copied)
                lines.append(f'MinerU attempt {attempt} using {slot} batch_id={batch_id}')
                self.responses[batch_id] = {'code': 0, 'data': {'batch_id': batch_id, 'extract_result': [
                    {'data_id': identity, 'state': 'done', 'full_zip_url': 'https://' + pinned.HOST + '/PRIVATE.zip?secret=PRIVATE'}
                    for identity in ids]}}
            lines.append('Batch 1 failed: ' + repr({'batch_index': 1, 'pdf_count': len(names), 'files': copied, 'returncode': 2, 'status': 'failed'}))
            self.logs[str(job['id'])] = '\n'.join('2026-10-01T00:00:00Z ' + line for line in lines).encode()
        self.api = Mock()
        self.api.get.side_effect = self.api_get
        self.api.raw.side_effect = self.api_raw
        self.r2 = MemoryR2(); self.cache = seed.LegacyResultCache(self.r2, 'private-bucket')
        self.transport = Mock(); self.transport.authentication = authentication(); self.transport.result_gets = 0
        self.payload = result_zip()
        def download(url):
            self.assertEqual(len(self.gets), 8)
            self.assertTrue(any(key.startswith(seed.PROOF_PREFIX) for key in self.r2.objects))
            self.transport.result_gets += 1
            return self.payload
        self.transport.side_effect = download

    def api_get(self, endpoint):
        self.api_calls.append(endpoint)
        if endpoint == self.base + f'actions/runs/{self.run}': return copy.deepcopy(self.run_meta)
        if '/contents/' in endpoint:
            name = endpoint.split('/contents/')[1].split('?ref=')[0]
            return {'path': name, 'encoding': 'base64', 'content': base64.b64encode(self.code[name]).decode()}
        if endpoint.endswith('/artifacts?per_page=100'): return {'total_count': 1, 'artifacts': [copy.deepcopy(self.artifact)]}
        if endpoint.endswith('/artifacts/777'): return copy.deepcopy(self.artifact)
        if endpoint.endswith('/jobs?filter=latest&per_page=100'): return {'total_count': len(self.jobs), 'jobs': copy.deepcopy(self.jobs)}
        raise AssertionError(endpoint)

    def api_raw(self, endpoint, maximum, redirect=False):
        self.api_calls.append(endpoint)
        if endpoint.endswith('/artifacts/777/zip'): return self.archive
        if endpoint.endswith('/logs'): return self.logs[endpoint.split('/jobs/')[1].split('/')[0]]
        raise AssertionError(endpoint)

    def authenticate(self):
        with patch.object(seed, 'ORIGINAL_CODE', self.hashes), patch('socket.create_connection', side_effect=AssertionError('No network')):
            return seed.authenticate(self.api, self.run, self.repository, self.root / 'originals', 6, '261001')

    def getter(self, url, token, timeout):
        self.gets.append(url)
        return 200, seed.canonical(self.responses[url.removeprefix(inspect.ENDPOINT)])

    def seed(self, authority, manifest, *, maximum=1):
        with patch.object(seed, 'ORIGINAL_CODE', self.hashes), patch('socket.create_connection', side_effect=AssertionError('No network')):
            return seed.seed_results(authority, manifest, manifest.parent,
                {slot: 'PRIVATE-TOKEN' for slot in inspect.SLOTS}, self.cache,
                getter=self.getter, transport_factory=lambda: self.transport, cutoff_check=lambda: None, max_results=maximum)

    def test_whole_original_artifact_jobs_checkout_and_acceptance_are_verified(self):
        authority, manifest, _ = self.authenticate()
        self.assertEqual(authority['expected_reports'], 6)
        self.assertEqual(len(authority['groups']), 2)
        self.assertEqual(sum(len(group['accepted']) for group in authority['groups']), 8)
        self.assertEqual(manifest.read_bytes(), self.manifest)
        self.assertEqual([path.read_bytes() for path in sorted(manifest.parent.glob('*.pdf'))], list(self.sources.values()))

    def test_one_canary_checks_all_original_retries_before_one_result_get(self):
        authority, manifest, _ = self.authenticate()
        summary, _ = self.seed(authority, manifest)
        self.assertEqual(summary['provider_gets'], 8)
        self.assertEqual(summary['result_gets'], 1)
        self.assertEqual(summary['cached_results'], 1)
        self.assertFalse(summary['all_original_results_cached'])
        self.assertFalse(summary['complete_source_handoff'])
        self.assertFalse(summary['canonical_task_admission'])
        self.assertEqual(summary['provider_posts'], 0)
        self.assertTrue(all(put['Key'].startswith((seed.PREFIX, seed.PROOF_PREFIX)) for put in self.r2.puts))
        result_keys = [put['Key'] for put in self.r2.puts if put['Key'].startswith(seed.PREFIX)]
        self.assertIn('/auth-', result_keys[0]); self.assertTrue(result_keys[-1].endswith('/receipt.json'))
        public = json.dumps(summary)
        for private in ('PRIVATE', 'private-source', 'https://', 'credential_slot', 'MINER_U'):
            self.assertNotIn(private, public)

    def test_all_then_rerun_uses_real_legacy_id_and_no_more_zip_get(self):
        authority, manifest, _ = self.authenticate()
        summary, _ = self.seed(authority, manifest, maximum=0)
        self.assertEqual(summary['cached_results'], 6)
        self.assertTrue(summary['all_original_results_cached'])
        self.gets.clear(); self.transport.reset_mock()
        summary, _ = self.seed(authority, manifest, maximum=0)
        self.assertEqual(summary['existing_cache_hits'], 6); self.transport.assert_not_called()
        receipts = [json.loads(value['Body']) for key, value in self.r2.objects.items() if key.endswith('/receipt.json')]
        self.assertTrue(all(receipt['binding']['data_id'].startswith('000') for receipt in receipts))
        self.assertTrue(all(receipt['binding']['data_id'] != receipt['binding']['content_sha256'] for receipt in receipts))

    def test_signed_url_refresh_does_not_change_cache_identity(self):
        authority, manifest, _ = self.authenticate(); self.seed(authority, manifest)
        for response in self.responses.values():
            for row in response['data']['extract_result']: row['full_zip_url'] += '&new-signature=NEW'
        self.gets.clear(); self.transport.reset_mock()
        summary, _ = self.seed(authority, manifest)
        self.assertEqual(summary['existing_cache_hits'], 1); self.transport.assert_not_called()

    def test_pending_failed_membership_and_unknown_rows_block_all_zip_and_puts(self):
        authority, manifest, _ = self.authenticate()
        for change in ('pending', 'missing', 'duplicate', 'unknown', 'bad-url'):
            original = copy.deepcopy(self.responses)
            rows = next(iter(self.responses.values()))['data']['extract_result']
            if change == 'pending': rows[0]['state'] = 'pending'
            if change == 'missing': rows.pop()
            if change == 'duplicate': rows.append(copy.deepcopy(rows[0]))
            if change == 'unknown': rows[0]['data_id'] = 'unknown'
            if change == 'bad-url': rows[0]['full_zip_url'] = 'https://private.example/zip'
            with self.subTest(change=change), self.assertRaises(ValueError): self.seed(authority, manifest)
            self.assertEqual(self.r2.puts, []); self.transport.assert_not_called()
            self.responses = original; self.gets.clear()

    def test_all_failed_group_is_not_combined_or_resubmitted(self):
        authority, manifest, _ = self.authenticate()
        for response in list(self.responses.values())[:4]:
            for row in response['data']['extract_result']: row['state'] = 'failed'
        summary, _ = self.seed(authority, manifest, maximum=0)
        self.assertEqual(summary['cached_results'], 1)
        self.assertEqual(summary['unresolved_original_groups'], 1)
        self.assertFalse(summary['all_original_results_cached'])

    def test_mixed_success_retries_never_union_into_a_whole_original_group(self):
        authority, manifest, _ = self.authenticate()
        for index, response in enumerate(list(self.responses.values())[:4]):
            response['data']['extract_result'][index]['state'] = 'failed'
        summary, _ = self.seed(authority, manifest, maximum=0)
        self.assertEqual(summary['recoverable_original_members'], 1)
        self.assertEqual(summary['unresolved_original_groups'], 1)

    def test_source_change_before_provider_stops_without_any_get(self):
        authority, manifest, _ = self.authenticate()
        next(manifest.parent.glob('*.pdf')).write_bytes(b'%PDF-1.7 changed')
        with self.assertRaises(ValueError): self.seed(authority, manifest)
        self.assertEqual(self.gets, []); self.assertEqual(self.r2.puts, [])

    def test_source_change_during_provider_checks_precedes_zip_and_put(self):
        authority, manifest, _ = self.authenticate()
        normal = self.getter
        def getter(*args):
            result = normal(*args)
            if len(self.gets) == 8: next(manifest.parent.glob('*.pdf')).write_bytes(b'%PDF-1.7 changed')
            return result
        with patch.object(self, 'getter', getter), self.assertRaises(ValueError): self.seed(authority, manifest)
        self.assertEqual(self.r2.puts, []); self.transport.assert_not_called()

    def test_unknown_code_other_checkout_and_wrong_jobs_fail_pre_provider(self):
        cases = [('code', lambda: self.code.update({next(iter(self.code)): b'unknown'})),
                 ('checkout', lambda: self.logs.update({'900': self.logs['900'].replace(self.sha.encode(), b'b' * 40)})),
                 ('jobrun', lambda: self.jobs[0].update(run_id=888)),
                 ('ambiguousjob', lambda: self.jobs.append(copy.deepcopy(self.jobs[0]))),
                 ('cancelledjob', lambda: self.jobs[0].update(conclusion='cancelled'))]
        for name, change in cases:
            old_code, old_logs, old_jobs = copy.deepcopy(self.code), copy.deepcopy(self.logs), copy.deepcopy(self.jobs)
            change()
            with self.subTest(name=name), self.assertRaises(ValueError): self.authenticate()
            self.assertEqual(self.gets, []); self.assertEqual(self.r2.puts, [])
            self.code, self.logs, self.jobs = old_code, old_logs, old_jobs
            import shutil
            shutil.rmtree(self.root / 'originals', ignore_errors=True)

    def test_artifact_digest_and_origin_are_hard_gates(self):
        for change in ({'digest': 'sha256:' + 'f' * 64}, {'expired': True}, {'workflow_run': {'id': 999}},
                       {'name': 'other-originals'}, {'size_in_bytes': seed.MAX_ARTIFACT + 1}):
            old = copy.deepcopy(self.artifact); self.artifact.update(change)
            with self.subTest(change=change), self.assertRaises(ValueError): self.authenticate()
            self.assertEqual(self.gets, []); self.artifact = old

    def test_path_symlink_crc_and_expansion_rejected(self):
        symlink = zipfile.ZipInfo('link.pdf'); symlink.external_attr = 0o120777 << 16
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as archive: archive.writestr(symlink, 'target')
        for raw in (archive_bytes([('../' + seed.MANIFEST, self.manifest)]), buffer.getvalue(), b'badzip'):
            with self.assertRaises(ValueError): seed.unpack_original_artifact(raw, self.root / 'invalid')
        with patch.object(seed, 'MAX_ARTIFACT', 8), self.assertRaises(ValueError):
            seed.unpack_original_artifact(self.archive, self.root / 'too-big')

    def test_missing_or_corrupted_auth_proof_prevents_cache_reuse(self):
        authority, manifest, _ = self.authenticate(); self.seed(authority, manifest)
        proof = next(key for key in self.r2.objects if key.startswith(seed.PROOF_PREFIX))
        self.r2.objects[proof]['Body'] = b'changed'
        self.gets.clear()
        with self.assertRaises(ValueError): self.seed(authority, manifest)
        self.assertEqual(self.transport.result_gets, 1)

    def test_invalid_zip_has_no_result_receipt(self):
        authority, manifest, _ = self.authenticate(); self.transport.side_effect = lambda _: b'badzip'
        with self.assertRaises(ValueError): self.seed(authority, manifest)
        self.assertFalse(any(key.startswith(seed.PREFIX) for key in self.r2.objects))

    def test_legacy_cache_binding_rejects_canonical_id_and_bad_types(self):
        authority, _, _ = self.authenticate()
        with patch.object(seed, 'ORIGINAL_CODE', self.hashes):
            results, _, _ = seed.complete_results(authority, {slot: 'TOKEN' for slot in inspect.SLOTS}, getter=self.getter)
        binding = results[0][0]
        for change in ({'data_id': binding['content_sha256']}, {'original_pdf_bytes': True}, {'batch_id': 'unknown'}, {'job_id': 2}):
            with self.subTest(change=change), self.assertRaises(ValueError): seed.binding_identity({**binding, **change})

    def test_first_complete_original_retry_is_chosen_without_credential_rotation(self):
        authority, manifest, _ = self.authenticate()
        for row in next(iter(self.responses.values()))['data']['extract_result']: row['state'] = 'failed'
        summary, _ = self.seed(authority, manifest)
        self.assertEqual(summary['cached_results'], 1)
        receipt = next(json.loads(value['Body']) for key, value in self.r2.objects.items() if key.endswith('/receipt.json'))
        self.assertTrue(receipt['binding']['batch_id'].endswith('000000000002'))
        self.assertEqual(receipt['binding']['credential_slot'], 'MINER_U_2')

    def test_zero_done_records_have_zero_result_gets_puts_and_no_false_success(self):
        authority, manifest, _ = self.authenticate()
        for response in self.responses.values():
            for row in response['data']['extract_result']: row['state'] = 'failed'
        summary, _ = self.seed(authority, manifest, maximum=0)
        self.assertFalse(summary['success']); self.assertEqual(summary['result_gets'], 0)
        self.assertEqual(summary['category'], 'legacy_no_complete_result_batch')
        self.assertEqual(summary['accepted_retry_member_state_counts'], {'failed': 24})
        self.assertEqual(self.r2.puts, []); self.transport.assert_not_called()

    def test_bad_producer_states_and_workflow_stop_before_artifact(self):
        for change in ({'head_branch': 'feature'}, {'path': seed.consumer.WORKFLOW}, {'status': 'in_progress'},
                       {'conclusion': 'cancelled'}, {'event': 'pull_request'}, {'head_repository': {'full_name': 'fork/repo'}}):
            original = copy.deepcopy(self.run_meta); self.run_meta.update(change)
            self.api_calls.clear()
            with self.subTest(change=change), self.assertRaises(ValueError): self.authenticate()
            self.assertEqual(len(self.api_calls), 1); self.run_meta = original

    def test_private_response_error_cannot_be_public_cli_text(self):
        for error in (seed.LegacyError('original_code PRIVATE-report https://secret.invalid'), ValueError('PRIVATE-TOKEN')):
            output = io.StringIO(); summary = self.root / 'summary.json'
            with patch.object(seed, 'require_cloud_manual', side_effect=error), redirect_stdout(output):
                code = seed.main(['--source-run-id', self.run, '--date-folder', '261001', '--expected-reports', '6', '--summary', str(summary)])
            self.assertEqual(code, 2); self.assertNotIn('PRIVATE', output.getvalue())
            self.assertEqual(json.loads(summary.read_text())['category'], 'seed_failed')

    def test_copy_map_attempt_upload_coverage_and_duplicates_are_required(self):
        authority, _, _ = self.authenticate()
        log = self.logs['900']
        cases = [log.replace(b'submitting 5 PDF(s).', b'submitting 4 PDF(s).', 1),
                 log.replace(b'0001-private-source-0.pdf', b'0009-private-source-0.pdf', 1),
                 log.replace(b"'stable_index': '1'", b"'stable_index': '9'", 1),
                 log + b'\n' + next(line for line in log.splitlines() if b' batch_id=' in line)]
        for raw in cases:
            with self.assertRaises(ValueError):
                seed.original_group(raw, self.names[:5], shard=0, total=6, job_id='900', run_id=self.run)


class WorkflowContractTests(unittest.TestCase):
    def test_legacy_opt_in_remains_exact_manual_main_separate_from_durable_jobs(self):
        path = Path(__file__).resolve().parents[1] / '.github/workflows/mineru-result-cache-seed.yml'
        text = path.read_text()
        self.assertIn("options: ['durable', 'legacy-daily', 'original-archive']", text)
        self.assertIn('default: durable', text)
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", text)
        self.assertEqual(text.count("if: ${{ inputs.source_kind == 'durable' }}"), 3)
        self.assertEqual(text.count("if: ${{ inputs.source_kind == 'legacy-daily' }}"), 1)
        self.assertIn("if: github.event_name == 'pull_request'", text)
        self.assertIn('python3 -B scripts/test_seed_legacy_market_views_cache.py', text)
        self.assertIn('python3 -B scripts/test_seed_mineru_result_cache.py', text)
        self.assertIn('path: ${{ runner.temp }}/mineru-result-cache-seed-summary.json', text)
        self.assertNotIn('allow_fresh', text)
        self.assertIn('Legacy tasks cannot mix durable child authorization.', text)
        self.assertIn('Durable tasks cannot use a legacy artifact override.', text)
        source = (path.parents[2] / 'scripts/seed_legacy_market_views_cache.py').read_text()
        self.assertNotIn('Ledger.run', source); self.assertNotIn('TerminalRecovery.run', source)
        self.assertNotIn('requests.post', source); self.assertNotIn('persist_terminal=True', source)


if __name__ == '__main__':
    unittest.main()
