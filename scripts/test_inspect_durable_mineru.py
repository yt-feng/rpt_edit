import copy
import io
import zipfile
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import uuid

import inspect_durable_mineru as m
from mineru_task_ledger import FileStore, Ledger, LedgerError, encoded, token_fingerprint
from inspect_legacy_mineru import ENDPOINT
from test_mineru_completed_child_reuse import no_mutations, recovered_fixture
from test_mineru_terminal_recovery import Provider


class UUIDProvider(Provider):
    """Exercise the real controller fixture with the diagnostic UUID contract."""
    def __init__(self):
        super().__init__()
        self.aliases = {}

    def submit(self, *args):
        original_id, urls = super().submit(*args)
        task_id = str(uuid.uuid4())
        self.aliases[task_id] = original_id
        return task_id, urls

    def poll(self, batch_id, *args):
        return super().poll(self.aliases[batch_id], *args)


class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = FileStore(self.root / 'ledger')
        self.credentials = {'MINER_U': 'first', 'MINER_U_2': 'second'}
        self.ledger = Ledger(self.store, None, 'dropbox', 'https://mineru.net',
                             {'model': 'vlm', 'language': 'en', 'ocr': True}, list(self.credentials.items()))
        path = self.root / 'source.pdf'; path.write_bytes(b'%PDF-exact')
        self.item = self.ledger.bind(path, 'source.pdf')
        self.key = 'batches/' + 'a' * 32
        self.batch = {'schema': 1, 'key': self.key, 'scope': 'dropbox', 'endpoint': 'https://mineru.net',
                      'options': self.ledger.options, 'token_identity': token_fingerprint('second'),
                      'state': 'terminal', 'batch_id': str(uuid.uuid4()), 'files': [self.item]}
        self.store.put(self.key, self.batch)
        self.request = {'scope': 'dropbox', 'run_id': '123', 'batches': [{'key': self.key, 'job_id': '456'}]}
        self.calls = []

    def getter(self, endpoint, token, timeout):
        self.calls.append((endpoint, token, timeout))
        return 200, encoded({'code': 0, 'data': {'batch_id': self.batch['batch_id'], 'extract_result': [
            {'data_id': self.item['id'], 'state': 'failed', 'err_msg': 'PDF page limit exceeded SECRET-REPORT'}]}})

    def test_exact_original_token_one_get_no_ledger_write_no_error_text(self):
        before = {str(p): p.read_bytes() for p in self.root.rglob('*.json')}
        with patch.object(self.store, 'put', side_effect=AssertionError('must not write')):
            public, private, diag = m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(len(self.calls), 1); self.assertEqual(self.calls[0][1], 'second')
        self.assertEqual(public['provider_posts'], 0); self.assertTrue(public['batches'][0]['membership_proven'])
        self.assertEqual(diag['failure_categories'], {'page_limit': 1})
        self.assertEqual(diag['failure_reasons'][0]['error_message_safe'], 'pdf page limit exceeded [redacted]')
        self.assertEqual(diag['failure_reasons'][0]['count'], 1)
        self.assertNotIn('SECRET-REPORT', json.dumps(public | diag))
        self.assertIn('SECRET-REPORT', json.dumps(private))
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*.json')})

    def enable_original_probe(self):
        self.request['scope'] = self.batch['scope'] = 'institution'
        self.ledger.scope = 'institution'
        self.item = self.ledger.bind(self.root/'source.pdf', 'source.pdf')
        self.batch['files'] = [self.item]
        (self.root/'ledger'/(self.key+'.json')).write_bytes(encoded(self.batch))
        self.store.put('sources/'+self.item['id'], {'schema': 1, 'batch_key': self.key, 'binding': self.item})
        self.request['original_pdf_probe_sha256'] = m.sha256(b'source.pdf')

    def result_getter(self, state='done', **changes):
        def get(*args):
            self.calls.append(args)
            row = {'data_id': self.item['id'], 'state': state,
                   'full_zip_url': 'https://results.invalid/PRIVATE-SIGNED-RESULT'}
            row.update(changes)
            return 200, encoded({'code': 0, 'data': {'batch_id': self.batch['batch_id'], 'extract_result': [row]}})
        return get

    @staticmethod
    def original_result_zip(pdf=b'%PDF-exact', name='payload/report_origin.pdf'):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w') as archive:
            archive.writestr('payload/full.md', 'PRIVATE REPORT BODY')
            archive.writestr(name, pdf)
        return stream.getvalue()

    def test_selected_completed_result_proves_only_exact_original_bytes_without_writes(self):
        self.enable_original_probe(); calls = []
        before = {str(p): p.read_bytes() for p in self.root.rglob('*.json')}
        def download(url): calls.append(url); return self.original_result_zip()
        with patch.object(self.store, 'put', side_effect=AssertionError('must not write')):
            public, private, diag = m.inspect(self.request, self.store, self.credentials,
                getter=self.result_getter(), result_downloader=download)
        result = diag['original_pdf_probe']
        self.assertTrue(result['selected_original_bytes_proven'])
        self.assertFalse(result['source_bytes_proven'])
        self.assertEqual((result['pdf_member_count'], result['matching_original_pdf_count'], result['result_gets']), (1, 1, 1))
        self.assertEqual((public['provider_posts'], result['canonical_ledger_writes']), (0, 0))
        self.assertEqual((len(self.calls), len(calls)), (1, 1))
        for secret in ('source.pdf', 'PRIVATE', 'origin.pdf', 'https:'):
            self.assertNotIn(secret, json.dumps(result))
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*.json')})

    def test_failed_or_incomplete_member_never_downloads_a_result(self):
        self.enable_original_probe()
        for getter, status in ((self.result_getter('failed'), 'original_result_unavailable'),
                               (self.result_getter(data_id='unknown'), 'original_membership_incomplete')):
            with self.subTest(status=status):
                _, _, diag = m.inspect(self.request, self.store, self.credentials, getter=getter,
                    result_downloader=lambda *_: self.fail('No result GET permitted'))
                self.assertEqual(diag['original_pdf_probe']['status'], status)
                self.assertEqual(diag['original_pdf_probe']['result_gets'], 0)

    def test_origin_filename_is_not_source_byte_proof(self):
        self.enable_original_probe()
        _, _, diag = m.inspect(self.request, self.store, self.credentials, getter=self.result_getter(),
            result_downloader=lambda *_: self.original_result_zip(b'%PDF-other'))
        self.assertFalse(diag['original_pdf_probe']['selected_original_bytes_proven'])
        self.assertEqual(diag['original_pdf_probe']['matching_original_pdf_count'], 0)

    def test_result_inventory_keeps_existing_path_crc_and_size_gates(self):
        self.enable_original_probe()
        for payload in (self.original_result_zip(name='../escape.pdf'), b'not a zip'):
            _, _, diag = m.inspect(self.request, self.store, self.credentials, getter=self.result_getter(),
                result_downloader=lambda *_: payload)
            self.assertEqual(diag['original_pdf_probe']['status'], 'result_inventory_stopped')
            self.assertFalse(diag['original_pdf_probe']['selected_original_bytes_proven'])
        self.assertFalse((self.root/'escape.pdf').exists())

    def test_selected_result_transport_stops_after_one_attempt_without_fallback(self):
        from consume_legacy_mineru import NetworkStop, ResultHTTPError
        self.enable_original_probe()
        for error in (NetworkStop('tls_certificate_expired'), ResultHTTPError(403)):
            calls = []
            def download(*args): calls.append(args); raise error
            _, _, diag = m.inspect(self.request, self.store, self.credentials, getter=self.result_getter(),
                result_downloader=download)
            result = diag['original_pdf_probe']
            self.assertEqual(result['status'], 'result_inventory_stopped')
            self.assertEqual(len(calls), 1)
            if isinstance(error, ResultHTTPError): self.assertEqual(result['http_status'], 403)
            else: self.assertTrue(result['network_stop'])

    def test_changed_source_claim_stops_before_result_get(self):
        self.enable_original_probe()
        path = self.root/'ledger'/('sources/'+self.item['id']+'.json')
        claim = json.loads(path.read_bytes()); claim['batch_key'] = 'batches/'+'b'*32
        path.write_bytes(encoded(claim))
        with self.assertRaisesRegex(ValueError, 'original_probe_source_claim'):
            m.inspect(self.request, self.store, self.credentials, getter=self.result_getter(),
                result_downloader=lambda *_: self.fail('Mismatched claim must stop'))

    def test_ambiguous_same_filename_roots_never_select_a_result(self):
        self.enable_original_probe()
        path = self.root/'changed.pdf'; path.write_bytes(b'%PDF-other')
        other = self.ledger.bind(path, 'source.pdf')
        second = dict(self.batch, key='batches/'+'b'*32, files=[other], batch_id=str(uuid.uuid4()))
        self.store.put(second['key'], second)
        self.request['batches'].append({'key': second['key'], 'job_id': '457'})
        with self.assertRaisesRegex(ValueError, 'original_probe_ambiguous'):
            m.inspect(self.request, self.store, self.credentials, getter=self.result_getter(),
                result_downloader=lambda *_: self.fail('Ambiguous original cannot be selected'))

    def test_changed_root_after_download_never_returns_verified_probe(self):
        self.enable_original_probe()
        def download(*args):
            changed = dict(self.batch, state='uploaded')
            (self.root/'ledger'/(self.key+'.json')).write_bytes(encoded(changed))
            return self.original_result_zip()
        with self.assertRaisesRegex(LedgerError, 'stored binding changed'):
            m.inspect(self.request, self.store, self.credentials, getter=self.result_getter(), result_downloader=download)

    def test_result_failure_stops_before_private_receipt_writes(self):
        import os
        from types import SimpleNamespace
        environment = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
            'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REPOSITORY': 'example/repo',
            'GITHUB_WORKFLOW_REF': 'example/repo/.github/workflows/mineru-durable-inspect.yml@refs/heads/main',
            'RUNNER_TEMP': str(self.root), 'INSPECTION_REQUEST': json.dumps(self.request)}
        report = {'status': 'result_inventory_stopped', 'category': 'tls_certificate_expired', 'network_stop': True}
        with patch.dict(os.environ, environment, clear=True), \
             patch.object(m, 'single_attempt_store', return_value=SimpleNamespace(client=None, bucket='private')), \
             patch.object(m, 'R2Store'), \
             patch.object(m, 'inspect', return_value=({'network_stop': False, 'provider_gets': 1}, {}, {'original_pdf_probe': report})), \
             patch.object(m, 'persist') as persist, patch('builtins.print'):
            self.assertEqual(m.main(), 2)
        persist.assert_not_called()
        result = json.loads((self.root/'mineru-durable-summary.json').read_bytes())
        self.assertEqual(result['original_pdf_probe'], report)
        self.assertEqual(result['provider_posts'], 0)

    def test_original_probe_is_exact_hash_and_institution_only(self):
        for bad in ('source.pdf', 'A'*64, None):
            value = dict(self.request, original_pdf_probe_sha256=bad)
            with self.assertRaises(ValueError): m.validate_request(value)
        with self.assertRaises(ValueError):
            m.validate_request(dict(self.request, original_pdf_probe_sha256='a'*64))

    def test_corrupt_source_binding_fails_before_get(self):
        self.batch['files'][0]['sha256'] = '0' * 64
        (self.root / 'ledger' / (self.key + '.json')).write_bytes(encoded(self.batch))
        with self.assertRaises(LedgerError):
            m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(self.calls, [])

    def test_missing_later_task_validated_before_first_get(self):
        self.request['batches'].append({'key': 'batches/' + 'b' * 32, 'job_id': '457'})
        with self.assertRaises(ValueError):
            m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(self.calls, [])

    def test_input_cannot_select_arbitrary_objects_or_duplicate_tasks(self):
        for bad in ['../secret', 'sources/' + 'a' * 64, self.key + '/x']:
            request = copy.deepcopy(self.request); request['batches'][0]['key'] = bad
            with self.assertRaises(ValueError): m.validate_request(request)
        self.request['batches'] *= 2
        with self.assertRaises(ValueError): m.validate_request(self.request)

    def test_rotated_away_original_token_stops_before_get(self):
        with self.assertRaises(LedgerError):
            m.inspect(self.request, self.store, {'MINER_U': 'new-token'}, getter=self.getter)
        self.assertEqual(self.calls, [])

    def test_error_classification_is_fixed_vocabulary(self):
        for raw, category in [('password protected PDF', 'encrypted_pdf'), ('Insufficient quota', 'quota'),
                               ('download failed', 'file_download'), ('arbitrary-private-url', 'other_provider_failure')]:
            self.assertEqual(m.error_category({'err_msg': raw}), category)

    def test_failure_reason_never_copies_unknown_words_numbers_urls_or_names(self):
        row = {'err_msg': ('Unable to parse PRIVATE_RESEARCH.pdf data_id a1b2c3d4 '
                          'https://example.invalid/private.zip?token=SIGNEDSECRET '
                          'at /private/folder/report.pdf AccessToken timeout'),
               'err_code': 'A0301', 'data_id': 'a1b2c3d4', 'file_name': 'PRIVATE_RESEARCH.pdf'}
        result = m.safe_failure_reason(row, ['AccessToken'])
        public = json.dumps(result)
        for private in ('PRIVATE_RESEARCH', 'a1b2c3d4', 'example.invalid', 'SIGNEDSECRET',
                        'private/folder', 'AccessToken', 'https://', '.pdf'):
            self.assertNotIn(private, public)
        self.assertIn('unable to parse', result['error_message_safe'])
        self.assertIn('timeout', result['error_message_safe'])
        self.assertEqual(result['error_codes'], ['A0301'])
        self.assertTrue(result['message_redacted'])

    def test_codes_are_bounded_and_never_freeform_identifiers_or_credentials(self):
        for value in ['token_PRIVATE', 'E-123456789', 'a' * 64, True, 1000000, {'code':'A0301'}]:
            with self.subTest(value=value):
                self.assertEqual(m.safe_failure_reason({'err_code':value})['error_codes'], [])
        self.assertEqual(m.safe_failure_reason({'err_code':'A0202'}, ['A0202'])['error_codes'], [])
        self.assertEqual(m.safe_failure_reason({'err_code':123}, ['123'])['error_codes'], [])
        self.assertEqual(m.safe_failure_reason({'err_code':-500,'error_code':'A0202'})['error_codes'], ['-500','A0202'])

    def test_unknown_failure_retains_safe_operation_words_and_original_hash(self):
        row = {'err_msg':'Failed to extract PDF: exception RETRY-PRIVATE-IDENTIFIER', 'err_code':None}
        result = m.safe_failure_reason(row)
        self.assertEqual(result['category'], 'document_processing')
        self.assertIn('failed to extract', result['error_message_safe'])
        self.assertNotIn('PRIVATE', json.dumps(result))
        self.assertEqual(result['failure_message_sha256'], m.sha256(m.canonical({k:row.get(k) for k in m.ERROR_FIELDS})))

    def test_nested_and_chinese_errors_have_fixed_categories_without_copying_report_text(self):
        for row, expected in [
            ({'error':{'message':'CUDA out of memory PRIVATE_REPORT'}}, 'provider_memory'),
            ({'error_message':'文件转换失败 私有公司报告'}, 'document_processing'),
            ({'message':'任务执行失败 私有文件'}, 'provider_worker'),
            ({'err_msg':'未知错误 私有文件'}, 'provider_unknown'),
        ]:
            with self.subTest(row=row):
                result = m.safe_failure_reason(row)
                self.assertEqual(result['category'], expected)
                self.assertNotIn('私有', json.dumps(result, ensure_ascii=False))
                self.assertNotIn('PRIVATE_REPORT', json.dumps(result))

    def test_multiple_failed_members_are_aggregated_with_zero_provider_writes(self):
        second = self.ledger.bind(self.root/'source.pdf', 'other.pdf')
        self.batch['files'].append(second)
        (self.root/'ledger'/(self.key+'.json')).write_bytes(encoded(self.batch))
        def getter(endpoint, token, timeout):
            self.calls.append(endpoint)
            return 200, encoded({'code':0,'data':{'batch_id':self.batch['batch_id'],'extract_result':[
                {'data_id':item['id'],'state':'failed','err_msg':'PDF parsing failed','err_code':'A0301'}
                for item in self.batch['files']]}})
        with patch.object(self.store, 'put', side_effect=AssertionError('must not write')):
            public, private, diag=m.inspect(self.request,self.store,self.credentials,getter=getter)
        self.assertEqual(len(self.calls),1)
        self.assertEqual(public['provider_posts'],0)
        self.assertEqual(diag['failure_reasons'][0]['count'],2)
        self.assertEqual(diag['failure_reasons'][0]['error_codes'],['A0301'])
        self.assertEqual(public['batches'][0]['state_counts'],{'failed':2})

    def completed_fixture(self, *, third=False):
        (self.root / 'completed').mkdir()
        with patch('test_mineru_completed_child_reuse.Provider', UUIDProvider):
            fixture = recovered_fixture(self.root / 'completed', third=third)
        self.credentials = {'MINER_U': 'test-private-token'}
        self.request = {'scope': 'dropbox', 'run_id': '123',
                        'batches': [{'key': fixture.root['key'], 'job_id': '456'}],
                        'include_completed_children': True}
        self.calls = []
        def getter(endpoint, token, timeout):
            self.calls.append((endpoint, token, timeout))
            batch_id = endpoint.removeprefix(ENDPOINT)
            return 200, encoded({'code': 0, 'data': {'batch_id': batch_id,
                'extract_result': fixture.provider.poll(batch_id, token, timeout)}})
        self.child_getter = getter
        return fixture

    def inspect_fixture(self, fixture):
        before = copy.deepcopy(fixture.r2.objects)
        with no_mutations(fixture):
            result = m.inspect(self.request, fixture.store, self.credentials, getter=self.child_getter)
        self.assertEqual(before, fixture.r2.objects)
        self.assertEqual(len(self.calls), len(set(endpoint for endpoint, _, _ in self.calls)))
        return result

    def test_optional_flag_is_strict_bool_and_false_keeps_original_receipt(self):
        for bad in (None, 0, 1, 'true', [], {}):
            with self.subTest(bad=bad):
                request = dict(self.request, include_completed_children=bad)
                with self.assertRaisesRegex(ValueError, 'completed_children_flag'):
                    m.inspect(request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(self.calls, [])
        baseline = m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        explicit_false = m.inspect(dict(self.request, include_completed_children=False),
                                   self.store, self.credentials, getter=self.getter)
        self.assertEqual(baseline, explicit_false)
        self.assertEqual(len(self.calls), 2)
        self.assertNotIn('completed_child_inspection', baseline[2])

    def test_completed_children_add_effective_counts_without_changing_original_receipt(self):
        fixture = self.completed_fixture(third=True)
        original_request = {key: value for key, value in self.request.items() if key != 'include_completed_children'}
        with no_mutations(fixture):
            baseline = m.inspect(original_request, fixture.store, self.credentials, getter=self.child_getter)
        self.calls.clear()
        public, private, diagnostics = self.inspect_fixture(fixture)
        self.assertEqual(public, baseline[0]); self.assertEqual(private, baseline[1])
        self.assertEqual({key: value for key, value in diagnostics.items()
                          if key != 'completed_child_inspection'}, baseline[2])
        extra = diagnostics['completed_child_inspection']
        self.assertEqual(public['provider_gets'], 1)
        self.assertEqual(public['batches'][0]['state_counts'], {'done': 1, 'failed': 2})
        self.assertEqual(extra['effective_counts'], {'admitted': 3, 'completed': 3, 'failed': 0,
                                                    'pending': 0, 'reused_sources': 2})
        self.assertEqual((extra['original_provider_gets'], extra['additional_provider_gets'],
                          extra['total_provider_gets']), (1, 3, 4))
        self.assertTrue(extra['all_succeeded']); self.assertFalse(extra['source_bytes_proven'])
        self.assertFalse(extra['canonical_task_admission'])
        self.assertEqual(extra['provider_posts'], 0); self.assertEqual(extra['canonical_ledger_writes'], 0)
        self.assertEqual(extra['batches'][0]['completed_lineage_counts'], {'0': 1, '1': 1, '3': 1})
        self.assertEqual(len(extra['batches'][0]['checked_child_bindings']), 3)
        self.assertEqual(extra['batches'][0]['controller_binding_sha256'], m.sha256(m.canonical(fixture.control)))
        serialized = json.dumps(public | diagnostics)
        for secret in ('test-private-token', 'original-0.pdf', 'results.invalid', 'upload.invalid'):
            self.assertNotIn(secret, serialized)

    def test_pending_child_is_one_get_and_does_not_claim_full_coverage(self):
        fixture = self.completed_fixture()
        key = fixture.control['children'][0]['key']
        child, version = fixture.store.get(key)
        child['state'] = 'uploaded'; fixture.store.put(key, child, version)
        fixture.provider.plans[1] = ['done', 'running']
        _, _, diagnostics = self.inspect_fixture(fixture)
        extra = diagnostics['completed_child_inspection']
        self.assertEqual(extra['total_provider_gets'], 2)
        self.assertEqual(extra['effective_counts'], {'admitted': 3, 'completed': 2, 'failed': 0,
                                                    'pending': 1, 'reused_sources': 1})
        self.assertFalse(extra['all_succeeded'])

    def test_tampered_child_lineage_fails_closed_without_provider_writes(self):
        fixture = self.completed_fixture()
        key = fixture.control['children'][0]['key']
        child, version = fixture.store.get(key)
        child['recovery_parent']['root_key'] = 'batches/' + 'f' * 32
        fixture.store.put(key, child, version)
        with self.assertRaisesRegex(LedgerError, 'parent reservation'):
            self.inspect_fixture(fixture)
        self.assertEqual(len(self.calls), 1)

    def test_changed_accepted_binding_during_inspection_fails_closed(self):
        fixture = self.completed_fixture()
        real_get = fixture.store.get
        changed = False
        def get(key):
            nonlocal changed
            value, version = real_get(key)
            if key == fixture.root['key'] and self.calls and not changed:
                changed = True
                value['state'] = 'uploaded'
            return value, version
        with patch.object(fixture.store, 'get', side_effect=get), self.assertRaisesRegex(
                LedgerError, 'Inspection stored binding changed'):
            self.inspect_fixture(fixture)


if __name__ == '__main__': unittest.main()
