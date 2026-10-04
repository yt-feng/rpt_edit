"""Offline full-original, zero-POST, partial-cache and immutable-provenance checks."""
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
import uuid
import zipfile

import mineru_task_ledger as ledger_module
import mineru_pinned_result_transport as pinned
import seed_mineru_result_cache as seed
from mineru_terminal_recovery import TerminalRecovery, failure_hash, task_identity
from mineru_result_cache import ResultCache
from test_mineru_result_cache import MemoryR2, result_zip
from test_mineru_pinned_result_transport import authentication


class SeedTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.originals = self.root / 'originals'
        self.originals.mkdir()
        self.manifest = self.originals / seed.MANIFEST
        self.store = ledger_module.FileStore(self.root / 'ledger')
        self.responses, self.gets = {}, []
        self.provider = seed.SingleGetProvider(self.getter)
        self.ledger = ledger_module.Ledger(seed.ReadOnlyStore(self.store), self.provider, 'dropbox',
                                            'https://mineru.net', seed.OPTIONS,
                                            [('MINER_U', 'PRIVATE-TOKEN')], sleep=seed.stop_polling)
        self.bindings, rows = [], []
        for number in range(3):
            path = self.originals / f'PRIVATE-{number}.pdf'
            path.write_bytes(b'%PDF-1.7\noriginal frozen bytes ' + str(number).encode())
            binding = self.ledger.bind(path, path.name)
            self.bindings.append(binding)
            rows.append({'process_local_path': '/selected/' + path.name, 'content_sha256': binding['sha256'],
                         'dropbox_path': '/zip_backup/261003/' + path.name})
        self.manifest.write_text(json.dumps(rows))
        self.rows = rows
        for index, bindings in enumerate((self.bindings[:2], self.bindings[2:]), 1):
            batch_id = str(uuid.UUID(f'00000000-0000-4000-8000-{index:012d}'))
            key = 'batches/' + str(index) * 32
            batch = {'schema': 1, 'key': key, 'scope': 'dropbox', 'endpoint': 'https://mineru.net',
                     'options': seed.OPTIONS, 'token_identity': ledger_module.token_fingerprint('PRIVATE-TOKEN'),
                     'files': bindings, 'state': 'accepted', 'batch_id': batch_id}
            self.store.put(key, batch)
            for binding in bindings:
                self.store.put('sources/' + binding['id'], {'schema': 1, 'binding': binding, 'batch_key': key})
            response_rows = [{'data_id': binding['id'], 'state': 'failed' if binding is self.bindings[1] else 'done',
                              'err_msg': 'PRIVATE report parsing failure',
                              'full_zip_url': 'https://' + pinned.HOST + '/PRIVATE.zip?signature=PRIVATE'}
                             for binding in bindings]
            self.responses[batch_id] = {'code': 0, 'data': {'batch_id': batch_id, 'extract_result': response_rows}}
        self.r2 = MemoryR2()
        self.cache = ResultCache(self.r2, 'PRIVATE-BUCKET')
        self.transport = Mock()
        self.transport.authentication = authentication()
        self.transport.result_gets = 0
        self.payload = result_zip()

        def download(url):
            self.transport.result_gets += 1
            return self.payload

        self.transport.side_effect = download
        self.factory = Mock(return_value=self.transport)

    def getter(self, url, token, timeout):
        self.gets.append((url, token, timeout))
        self.assertEqual(token, 'PRIVATE-TOKEN')
        return 200, ledger_module.encoded(self.responses[url.removeprefix(seed.ENDPOINT)])

    def run_seed(self, **kwargs):
        with patch('socket.create_connection', side_effect=AssertionError('No network in offline tests')), \
                patch.object(ledger_module.Ledger, 'run', side_effect=AssertionError('No submission path')):
            return seed.seed_results(self.ledger, self.originals, self.manifest, 3, '261003', '12345', self.cache,
                                     transport_factory=self.factory, cutoff_check=lambda: None, **kwargs)

    def child_fixture(self, *, ordinal_two=False, prior_run_id='67890'):
        root = self.store.get('batches/' + '1' * 32)[0]
        root_rows = {row['data_id']: row for row in self.responses[root['batch_id']]['data']['extract_result']}
        error_hash = failure_hash(root_rows[self.bindings[1]['id']])
        terminal = TerminalRecovery(self.ledger, allowed_error_hashes=[error_hash])
        manifest_sha = ledger_module.digest(self.manifest.read_bytes())
        control_key = 'recoveries/' + '1' * 32
        entries = []
        predecessor, rows = root, root_rows
        for ordinal in range(1, 3 if ordinal_two else 2):
            key = 'batches/' + str(ordinal + 2) * 32
            entry = {'key': key, 'ordinal': ordinal, 'file_ids': [self.bindings[1]['id']],
                     'initial_token_identity': root['token_identity'], 'proof': terminal._proof(predecessor, rows),
                     'authorization': {'run_id': prior_run_id if ordinal == 1 else '67890',
                                       'manifest_sha256': manifest_sha}}
            entries.append(entry)
            child = terminal._child_row(root, control_key, entry)
            child.update(state='accepted', batch_id=str(uuid.UUID(f'00000000-0000-4000-8000-{ordinal + 2:012d}')))
            self.store.put(key, child)
            state = 'failed' if ordinal_two and ordinal == 1 else 'done'
            child_rows = [{'data_id': self.bindings[1]['id'], 'state': state,
                           'err_msg': root_rows[self.bindings[1]['id']]['err_msg'],
                           'full_zip_url': 'https://' + pinned.HOST + '/PRIVATE-child.zip?signature=PRIVATE'}]
            self.responses[child['batch_id']] = {'code': 0, 'data': {'batch_id': child['batch_id'],
                                                                   'extract_result': child_rows}}
            predecessor, rows = child, {row['data_id']: row for row in child_rows}
        control = {'schema': 1, 'policy': terminal.policy, 'root_key': root['key'],
                   'root_identity_sha256': task_identity(root), 'children': entries}
        self.store.put(control_key, control)
        return {'recovery_run_id': '67890', 'allowed_error_hashes': [error_hash],
                'expected_manifest_sha256': manifest_sha}, control_key, entries[-1]['key']

    def test_canary_checks_all_original_batches_before_one_result_and_preserves_failed_sources(self):
        def create():
            self.assertEqual(len(self.gets), 2)
            return self.transport
        self.factory.side_effect = create
        summary = self.run_seed()
        self.assertEqual(summary['original_members_verified'], 3)
        self.assertEqual(summary['completed_members'], 2)
        self.assertEqual(summary['failed_members'], 1)
        self.assertEqual(summary['cached_results'], 1)
        self.assertEqual(self.transport.call_count, 1)
        self.assertEqual(summary['provider_posts'], 0)
        self.assertFalse(summary['all_done_results_cached'])
        self.assertFalse(summary['pipeline_restored'])
        self.assertFalse(summary['complete_source_handoff'])
        self.assertFalse(summary['production_acceptance'])
        for forbidden in ('PRIVATE', 'full_zip_url', 'https://', 'source.pdf'):
            self.assertNotIn(forbidden, json.dumps(summary))

    def test_all_done_results_are_immutable_source_bound_cache_objects_and_separate_auth_receipts(self):
        summary = self.run_seed(max_results=0)
        self.assertEqual(summary['cached_results'], 2)
        self.assertTrue(summary['all_done_results_cached'])
        self.assertFalse(summary['pipeline_restored'])
        self.assertEqual(len(self.r2.objects), 6)
        auth = [value for key, value in self.r2.objects.items() if key.startswith(seed.AUTH_PREFIX)]
        self.assertEqual(len(auth), 2)
        for item in auth:
            receipt = json.loads(item['Body'])
            self.assertEqual(receipt['zip_sha256'], ledger_module.digest(self.payload))
            self.assertEqual(receipt['authentication']['auth_mode'], pinned.AUTH_MODE)
            self.assertFalse(receipt['authentication']['pki_verified_now'])
            self.assertTrue(receipt['authentication']['historical_chain_verified'])
            self.assertIn('source_binding', receipt)
            self.assertEqual(receipt['lineage']['child_ordinal'], 0)
        self.assertTrue(all(call['IfNoneMatch'] == '*' for call in self.r2.puts))

    def test_existing_cache_hit_needs_no_tls_connection_or_new_cache_write_but_still_fresh_provider_gets(self):
        self.run_seed()
        before = copy.deepcopy(self.r2.objects)
        self.gets.clear()
        self.provider.seen.clear()
        self.factory.reset_mock()
        self.transport.reset_mock()
        summary = self.run_seed()
        self.factory.assert_not_called()
        self.transport.assert_not_called()
        self.assertEqual(summary['existing_cache_hits'], 1)
        self.assertEqual(summary['provider_gets'], 2)
        self.assertEqual(self.r2.objects, before)

    def test_wrong_count_hash_date_extra_or_missing_original_is_rejected_before_api_or_tls(self):
        self.rows[2]['content_sha256'] = 'a' * 64
        self.manifest.write_text(json.dumps(self.rows))
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(self.gets, [])
        self.factory.assert_not_called()
        self.rows[2]['content_sha256'] = self.bindings[2]['sha256']
        self.rows[2]['dropbox_path'] = '/zip_backup/261002/261003/PRIVATE.pdf'
        self.manifest.write_text(json.dumps(self.rows))
        with self.assertRaises(seed.SeedError):
            self.run_seed()
        self.assertEqual(self.gets, [])

    def test_missing_duplicate_unknown_or_pending_last_batch_blocks_all_result_downloads(self):
        key = list(self.responses)[1]
        good = copy.deepcopy(self.responses[key])
        for rows in ([], good['data']['extract_result'] * 2,
                     [{'data_id': 'a' * 64, 'state': 'done', 'full_zip_url': 'https://' + pinned.HOST + '/x'}],
                     [{**good['data']['extract_result'][0], 'state': 'pending'}]):
            self.responses[key]['data']['extract_result'] = rows
            self.provider.seen.clear()
            with self.subTest(rows=len(rows)), self.assertRaises((ValueError, ledger_module.LedgerError)):
                self.run_seed()
            self.factory.assert_not_called()
            self.assertEqual(self.r2.puts, [])

    def test_foreign_result_origin_in_unselected_done_member_blocks_preflight(self):
        self.responses[list(self.responses)[1]]['data']['extract_result'][0]['full_zip_url'] = 'https://PRIVATE.invalid/x'
        with self.assertRaises(pinned.PinnedTransportError):
            self.run_seed()
        self.factory.assert_not_called()
        self.assertEqual(self.r2.puts, [])

    def test_absent_claim_or_recovery_child_is_never_admitted_as_an_original(self):
        key = 'sources/' + self.bindings[2]['id']
        claim = self.store.get(key)[0]
        self.store._path(key).unlink()
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(self.gets, [])
        self.factory.assert_not_called()
        self.store.put(key, claim)
        batch_key = claim['batch_key']
        batch, etag = self.store.get(batch_key)
        batch['recovery_parent'] = 'batches/' + 'a' * 32
        self.store.put(batch_key, batch, etag)
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(self.gets, [])
        self.factory.assert_not_called()

    def test_unlisted_or_missing_original_and_count_mismatch_stop_before_task_reads(self):
        extra = self.originals / 'PRIVATE-extra.pdf'
        extra.write_bytes(b'%PDF-extra')
        with self.assertRaises(ValueError):
            self.run_seed()
        extra.unlink()
        original = self.originals / 'PRIVATE-2.pdf'
        payload = original.read_bytes()
        original.unlink()
        with self.assertRaises(ValueError):
            self.run_seed()
        original.write_bytes(payload)
        self.manifest.write_text(json.dumps(self.rows[:2]))
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(self.gets, [])
        self.factory.assert_not_called()
        self.assertEqual(self.r2.puts, [])

    def test_cutoff_failure_precedes_source_task_tls_and_cache_work(self):
        check = Mock(side_effect=pinned.PinnedTransportError('pinned_auth_window_closed'))
        with self.assertRaises(pinned.PinnedTransportError):
            seed.seed_results(self.ledger, self.originals, self.manifest, 3, '261003', '12345', self.cache,
                              transport_factory=self.factory, cutoff_check=check)
        self.assertEqual(self.gets, [])
        self.factory.assert_not_called()
        self.assertEqual(self.r2.puts, [])

    def test_invalid_authentication_receipt_cannot_trigger_download_or_cache_write(self):
        self.transport.authentication['url'] = 'https://PRIVATE.invalid/report'
        with self.assertRaises(pinned.PinnedTransportError):
            self.run_seed()
        self.transport.assert_not_called()
        self.assertEqual(self.r2.puts, [])

    def test_local_entrypoint_writes_only_fixed_failure_category_without_task_or_cache_access(self):
        output = self.root / 'summary.json'
        args = ['--input-dir', str(self.originals), '--producer-json', str(self.root / 'PRIVATE-producer.json'),
                '--source-run-id', '12345', '--date-folder', '261003', '--expected-reports', '3',
                '--summary', str(output)]
        with patch.dict('os.environ', {}, clear=True), patch('builtins.print') as printed, \
                patch.object(seed, 'seed_results', side_effect=AssertionError('Must not access tasks or cache')) as called, \
                patch('socket.create_connection', side_effect=AssertionError('No offline network')):
            self.assertEqual(seed.main(args), 2)
        called.assert_not_called()
        summary = json.loads(output.read_text())
        self.assertEqual(summary['category'], 'reviewed_manual_cloud_required')
        self.assertEqual(summary['provider_posts'], 0)
        self.assertFalse(summary['pipeline_restored'])
        self.assertNotIn('PRIVATE', output.read_text())
        self.assertNotIn('PRIVATE', str(printed.call_args_list))

    def test_provider_and_canonical_ledger_writes_are_explicitly_blocked(self):
        for call in (self.provider.submit, self.provider.upload, self.ledger.store.put):
            with self.assertRaises(seed.SeedError):
                call('PRIVATE')
        self.assertEqual(self.gets, [])

    def test_provider_reads_are_single_attempt_and_batch_and_complete_membership_bound(self):
        batch = list(self.responses)[0]
        self.provider.poll(batch, 'PRIVATE-TOKEN', 20)
        with self.assertRaises(seed.SeedError):
            self.provider.poll(batch, 'PRIVATE-TOKEN', 20)
        self.assertEqual(len(self.gets), 1)
        self.responses[batch]['data']['batch_id'] = list(self.responses)[1]
        self.provider.seen.clear()
        with self.assertRaises(seed.SeedError):
            self.provider.poll(batch, 'PRIVATE-TOKEN', 20)

    def test_invalid_or_unsafe_zip_is_rejected_before_any_cache_or_auth_write(self):
        for payload in (b'not a ZIP',):
            self.payload = payload
            with self.assertRaises(ValueError):
                self.run_seed()
            self.assertEqual(self.r2.puts, [])
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as archive:
            archive.writestr('../full.md', 'PRIVATE')
        self.payload = buffer.getvalue()
        self.provider.seen.clear()
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(self.r2.puts, [])

    def test_original_changes_during_download_block_auth_and_cache_publication(self):
        def mutate(url):
            (self.originals / 'PRIVATE-2.pdf').write_bytes(b'%PDF-changed')
            return self.payload
        self.transport.side_effect = mutate
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(self.r2.puts, [])

    def test_each_cache_write_rechecks_fixed_cutoff_without_changing_existing_client(self):
        check = Mock(side_effect=pinned.PinnedTransportError('pinned_auth_window_closed'))
        client = seed.CutoffCacheClient(self.r2, check)
        with self.assertRaises(pinned.PinnedTransportError):
            client.put_object(Key='PRIVATE')
        self.assertEqual(self.r2.puts, [])

    def test_private_receipt_conflict_does_not_overwrite_authentication_or_publish_zip(self):
        self.run_seed()
        keys = [key for key in self.r2.objects if not key.startswith(seed.AUTH_PREFIX)]
        for key in keys:
            del self.r2.objects[key]
        auth_key = next(iter(self.r2.objects))
        wrong = self.r2.objects[auth_key]
        wrong['Body'] = b'changed authentication'
        wrong['Metadata']['sha256'] = ledger_module.digest(wrong['Body'])
        self.provider.seen.clear()
        with self.assertRaises(ValueError):
            self.run_seed()
        self.assertEqual(len(self.r2.objects), 1)

    def test_accepted_child_canary_checks_all_parents_and_child_without_any_task_state_write(self):
        kwargs, _, child_key = self.child_fixture()
        before = {path.name: path.read_bytes() for path in self.store.root.rglob('*.json')}
        with patch.object(TerminalRecovery, 'run', side_effect=AssertionError('No recovery submission')):
            summary = self.run_seed(**kwargs)
        self.assertEqual(len(self.gets), 3)
        self.assertEqual(self.transport.call_count, 1)
        self.assertEqual(summary['selection_mode'], 'accepted_children')
        self.assertEqual(summary['authorized_child_done'], 1)
        self.assertEqual(summary['completed_members'], 2)
        self.assertFalse(summary['all_done_results_cached'])
        self.assertTrue(summary['all_authorized_child_done_results_cached'])
        self.assertFalse(summary['complete_source_handoff'])
        receipts = [json.loads(value['Body']) for key, value in self.r2.objects.items()
                    if key.startswith(seed.AUTH_PREFIX)]
        self.assertEqual(receipts[0]['lineage']['batch_key'], child_key)
        self.assertEqual(receipts[0]['lineage']['child_ordinal'], 1)
        self.assertEqual(receipts[0]['lineage']['parent_batch_key'], 'batches/' + '1' * 32)
        self.assertEqual(before, {path.name: path.read_bytes() for path in self.store.root.rglob('*.json')})
        self.assertNotIn('PRIVATE', json.dumps(summary))

    def test_second_child_proves_prior_child_from_an_earlier_authorized_manifest_run(self):
        kwargs, _, child_key = self.child_fixture(ordinal_two=True, prior_run_id='67889')
        summary = self.run_seed(max_results=0, **kwargs)
        self.assertEqual(len(self.gets), 4)
        self.assertEqual(summary['authorized_child_members'], 1)
        self.assertEqual(summary['authorized_child_done'], 1)
        receipts = [json.loads(value['Body']) for key, value in self.r2.objects.items()
                    if key.startswith(seed.AUTH_PREFIX)]
        self.assertEqual(receipts[0]['lineage']['child_ordinal'], 2)
        self.assertEqual(receipts[0]['lineage']['batch_key'], child_key)

    def test_child_mode_manifest_and_failure_hash_are_distinct_and_checked_before_any_zip(self):
        kwargs, _, _ = self.child_fixture()
        kwargs['expected_manifest_sha256'] = kwargs['allowed_error_hashes'][0]
        with self.assertRaisesRegex(seed.SeedError, 'expected_manifest_mismatch'):
            self.run_seed(**kwargs)
        self.assertEqual(self.gets, [])
        self.factory.assert_not_called()

    def test_child_auth_options_reject_partial_wrong_typed_or_duplicate_hashes(self):
        for values in (('67890', [], 'a' * 64), ('', ['b' * 64], ''),
                       ('67890', ['b' * 64] * 2, 'a' * 64), ('67890', ['PRIVATE'], 'a' * 64),
                       ('67890', {}, 'a' * 64), ('0', ['b' * 64], 'a' * 64)):
            with self.subTest(values=values), self.assertRaises(seed.SeedError):
                seed.child_authorization(*values)

    def test_wrong_policy_root_proof_or_child_parent_prevents_any_result_request(self):
        kwargs, control_key, child_key = self.child_fixture()
        original_control, _ = self.store.get(control_key)
        original_child, _ = self.store.get(child_key)
        mutations = [
            lambda control, child: control['policy']['allowed_error_hashes'].append('a' * 64),
            lambda control, child: control.update(root_identity_sha256='a' * 64),
            lambda control, child: control['children'][0]['proof']['value'].update(task_identity_sha256='a' * 64),
            lambda control, child: child['recovery_parent'].update(proof_sha256='a' * 64),
            lambda control, child: child.update(state='submitting'),
            lambda control, child: control['children'][0]['authorization'].update(manifest_sha256='a' * 64),
            lambda control, child: control['children'][0]['authorization'].update(run_id='99999'),
        ]
        for mutation in mutations:
            control, child = copy.deepcopy(original_control), copy.deepcopy(original_child)
            mutation(control, child)
            # Keep the mutated proof internally hashed; the fresh identity check
            # must still detect it independently of the self-hash.
            control['children'][0]['proof']['sha256'] = ledger_module.digest(
                ledger_module.encoded(control['children'][0]['proof']['value']))
            for key, value in ((control_key, control), (child_key, child)):
                _, etag = self.store.get(key)
                self.store.put(key, value, etag)
            self.provider.seen.clear()
            with self.subTest(mutation=mutation), self.assertRaises((ValueError, ledger_module.LedgerError)):
                self.run_seed(**kwargs)
            self.factory.assert_not_called()
            self.assertEqual(self.r2.puts, [])

    def test_child_truncated_or_pending_rows_never_trigger_zip_or_terminal_write(self):
        kwargs, _, child_key = self.child_fixture()
        child = self.store.get(child_key)[0]
        for rows in ([], [{'data_id': self.bindings[1]['id'], 'state': 'pending'}]):
            self.responses[child['batch_id']]['data']['extract_result'] = rows
            self.provider.seen.clear()
            with self.assertRaises((ValueError, ledger_module.LedgerError)):
                self.run_seed(**kwargs)
            self.factory.assert_not_called()
            self.assertEqual(self.r2.puts, [])

    def test_changed_fresh_failure_or_child_snapshot_blocks_cache_publication(self):
        kwargs, control_key, _ = self.child_fixture()
        root_batch = list(self.responses)[0]
        failed_row = self.responses[root_batch]['data']['extract_result'][1]
        original_error = failed_row['err_msg']
        failed_row['err_msg'] = 'PRIVATE changed fresh error'
        with self.assertRaises((ValueError, ledger_module.LedgerError)):
            self.run_seed(**kwargs)
        self.factory.assert_not_called()
        failed_row['err_msg'] = original_error
        self.provider.seen.clear()
        def mutate_controller(url):
            control, etag = self.store.get(control_key)
            control['children'][0]['authorization']['run_id'] = '99999'
            self.store.put(control_key, control, etag)
            return self.payload
        self.transport.side_effect = mutate_controller
        with self.assertRaisesRegex(seed.SeedError, 'accepted_child_snapshot_changed'):
            self.run_seed(**kwargs)
        self.assertEqual(self.r2.puts, [])

    def test_existing_child_cache_is_reused_without_new_zip_or_auth_receipt(self):
        kwargs, _, _ = self.child_fixture()
        self.run_seed(**kwargs)
        before = copy.deepcopy(self.r2.objects)
        self.provider.seen.clear()
        self.transport.reset_mock()
        self.factory.reset_mock()
        summary = self.run_seed(**kwargs)
        self.assertEqual(summary['existing_cache_hits'], 1)
        self.transport.assert_not_called()
        self.factory.assert_not_called()
        self.assertEqual(self.r2.objects, before)

    def test_authenticated_child_producer_is_exact_manual_main_workflow_even_if_later_failed(self):
        # GitHub's actual run API returns the expanded run-name in name.
        producer = {'id': 67890, 'path': seed.RECOVERY_WORKFLOW, 'name': 'Recover MinerU Market Views 261003', 'event': 'workflow_dispatch',
                    'head_branch': 'main', 'head_sha': 'a' * 40, 'repository': {'full_name': 'owner/repo'},
                    'status': 'completed', 'conclusion': 'failure'}
        self.assertEqual(seed.check_recovery_producer(producer, '67890', 'owner/repo', '261003'), 'a' * 40)
        for change in ({'id': 67891}, {'path': 'PRIVATE.yml'}, {'name': 'Other recovery'}, {'event': 'push'}, {'head_branch': 'PRIVATE'},
                       {'head_sha': 'short'}, {'status': 'in_progress'}, {'conclusion': 'cancelled'},
                       {'name': 'Recover Market Views from exact MinerU tasks'},
                       {'name': 'Recover MinerU Market Views 261004'}):
            with self.subTest(change=change), self.assertRaises(seed.SeedError):
                seed.check_recovery_producer({**producer, **change}, '67890', 'owner/repo', '261003')
        with self.assertRaises(seed.SeedError):
            seed.check_recovery_producer(producer, '67890', 'owner/repo', '261004')


class WorkflowContractTests(unittest.TestCase):
    def test_manual_main_only_no_post_scope_and_dependency_contract(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / '.github/workflows/mineru-result-cache-seed.yml').read_text()
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", text)
        self.assertIn('actions: read', text)
        self.assertIn('source_run_id:', text)
        self.assertIn('max_results:', text)
        self.assertIn("default: '1'", text)
        self.assertIn('selected-macro-pdfs-${{ inputs.source_run_id }}', text)
        self.assertIn("'urllib3>=2.2,<3'", text)
        self.assertIn('scripts/seed_mineru_result_cache.py', text)
        self.assertIn('mineru-result-cache-seed-summary.json', text)
        self.assertIn('if: ${{ always() }}', text)
        self.assertIn('recovery_run_id:', text)
        self.assertIn('allowed_error_hashes:', text)
        self.assertIn('expected_manifest_sha256:', text)
        self.assertIn('decode(os.environ[\'ALLOWED_ERROR_HASHES\'].encode())', text)
        self.assertIn('--allowed-error-hashes "$ALLOWED_ERROR_HASHES"', text)
        for forbidden in ('allow_fresh', 'allowed_error_codes:', 'TerminalRecovery', 'ledger.run', 'build_market_views',
                          'workflow run', 'verify=False', 'DROPBOX_REFRESH_TOKEN'):
            self.assertNotIn(forbidden, text)
        ci = (root / '.github/workflows/market-views-mineru-recovery.yml').read_text()
        self.assertIn('- scripts/seed_mineru_result_cache.py', ci)
        self.assertIn('python3 -B scripts/test_seed_mineru_result_cache.py', ci)
        self.assertIn('python3 -B scripts/test_mineru_pinned_result_transport.py', ci)
        self.assertNotIn('test_seed_mineru_result_cache.py', ci.split('  recover:')[1])


if __name__ == '__main__':
    unittest.main()
