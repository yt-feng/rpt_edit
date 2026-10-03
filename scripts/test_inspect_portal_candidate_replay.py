"""Offline, real candidate/checkpoint diagnostic contracts; no provider calls."""
import contextlib
import io
import gzip
from urllib3.response import HTTPResponse
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import inspect_portal_candidate_replay as inspector
import test_portal_extended_publication as fixtures


class InspectorTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.PublicationTests('test_checkpoint_cannot_change_approved_translation')
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.batch = self.fixture.candidate()
        self.store = self.fixture.store
        self.base = self.fixture.base

    def compare(self):
        return inspector.compare(self.store, self.batch, 'fr', self.base/'inspect')

    def test_exact_candidate_replays_without_writes_or_inference(self):
        before = {key: dict(value) for key, value in self.store.client.objects.items()}
        result = self.compare()
        self.assertTrue(result['matches'])
        self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['changed_pages'], [])
        self.assertEqual(result['rejected_rows_total'], 0)
        self.assertEqual(before, self.store.client.objects)

    def mutate_checkpoint(self, text):
        seed = self.base/'mutated.json'
        self.store.restore_checkpoint('fr', self.batch['generation'], seed)
        value = json.loads(seed.read_bytes())
        next(iter(value['rows'].values()))['text'] = text
        seed.write_text(json.dumps(value))
        self.store.put_checkpoint('fr', self.batch['generation'], seed)

    def test_latest_checkpoint_drift_is_detected_with_private_text_omitted(self):
        self.mutate_checkpoint('Autre traduction valide et privée.')
        result = self.compare()
        self.assertFalse(result['matches'])
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['failure_codes'], {})
        change = result['changed_pages'][0]
        self.assertFalse(change['descriptor_only'])
        self.assertNotEqual(change['approved_shape']['visible_text_sha256'], change['replay_shape']['visible_text_sha256'])
        public = json.dumps(result)
        for secret in ('Autre traduction', fixtures.URL, 'Source based', 'Texte traduit'):
            self.assertNotIn(secret, public)

    def test_rejected_checkpoint_unit_reports_gate_and_cache_miss(self):
        self.mutate_checkpoint('Valeur privée 99999%.')
        result = self.compare()
        self.assertFalse(result['matches'])
        self.assertEqual(result['status'], 'incomplete-candidate')
        self.assertGreater(result['rejected_rows_total'], 0)
        self.assertIn('offline-approval-cache-miss', result['failure_codes'])
        self.assertEqual(result['translation_calls'], 1)
        # CacheOnly raises before invoking any translator/provider. The build's
        # attempt count documents that absent approval instead of hiding it.
        self.assertNotIn('Valeur privée', json.dumps(result))

    def test_missing_checkpoint_is_a_fixed_mismatch(self):
        key = self.store.checkpoint_pointer_key('fr', self.batch['generation'])
        del self.store.client.objects[key]
        result = self.compare()
        self.assertFalse(result['matches'])
        self.assertEqual(result['failure_codes'], {'checkpoint-absent': 1})

    def test_changed_active_identity_stops_before_private_reads(self):
        with mock.patch.object(inspector, 'read_active_batches') as reader:
            with self.assertRaisesRegex(inspector.InspectionError, 'active-release-changed'):
                inspector.inspect(self.store, self.batch, 'a'*32, {'release_id': 'b'*32})
            reader.assert_not_called()

    def test_first_carry_forward_mismatch_precedes_new_target(self):
        target = self.fixture.candidate('pt')
        self.mutate_checkpoint('Autre traduction valide.')
        with mock.patch.object(inspector, 'read_active_batches', return_value=[self.batch]):
            result = inspector.inspect(self.store, target, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'mismatch')
        self.assertEqual(len(result['results']), 1)
        self.assertEqual(result['results'][0]['locale'], 'fr')
        self.assertFalse(result['results'][0]['target_candidate'])
        self.assertEqual(result['production_writes'], 0)
        self.assertEqual(result['inference_calls'], 0)

    def test_superseded_candidate_is_skipped_like_publication_owner_order(self):
        target = {'generation': self.batch['generation'], 'candidates': {'fr': 'c'*64}}
        with mock.patch.object(inspector, 'read_active_batches', return_value=[self.batch]), \
             mock.patch.object(inspector, 'compare', return_value={'matches': True}) as compare:
            result = inspector.inspect(self.store, target, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'all-matched')
        self.assertEqual(compare.call_count, 1)
        self.assertEqual(compare.call_args.args[1], target)
        self.assertEqual(result['results'][0]['batch_index'], 1)

    def test_batch_bound_precedes_corpus_restoration(self):
        rows = [{'generation': f'{i:064x}', 'candidates': {'fr': 'c'*64}} for i in range(37)]
        with mock.patch.object(inspector, 'read_active_batches', return_value=rows), \
             mock.patch.object(self.store, 'restore_source') as restore:
            with self.assertRaisesRegex(inspector.InspectionError, 'too-many-batches'):
                inspector.inspect(self.store, self.batch, 'a'*32, {'release_id': 'a'*32})
            restore.assert_not_called()

    def test_render_only_difference_has_equal_visible_text_signature(self):
        first = self.base/'one.html'; second = self.base/'two.html'
        first.write_text('<body><p>Private report.</p><script>private token</script></body>')
        second.write_text('<body><p class="new">Private report.</p><script>other token</script></body>')
        self.assertEqual(inspector.html_shape(first), inspector.html_shape(second))
        self.assertNotIn('Private', json.dumps(inspector.html_shape(first)))

    def test_invalid_cli_input_stops_before_http_or_storage(self):
        args = ['inspect', '--generation', '../bad', '--locale', 'fr', '--candidate', 'b'*64, '--active-release', 'a'*32]
        with mock.patch('sys.argv', args), mock.patch.object(inspector, 'read_identity') as reader, \
             mock.patch.object(inspector.R2Store, 'from_env') as storage, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(inspector.main(), 1)
        reader.assert_not_called(); storage.assert_not_called()
        self.assertEqual(json.loads(output.getvalue())['status'], 'failed')
        self.assertNotIn('../bad', output.getvalue())

    def test_runtime_exception_body_never_leaks(self):
        args = ['inspect', '--generation', 'a'*64, '--locale', 'fr', '--candidate', 'b'*64, '--active-release', 'a'*32]
        with mock.patch('sys.argv', args), mock.patch.object(inspector, 'read_identity', side_effect=RuntimeError('secret https://private/?token=x')), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(inspector.main(), 1)
        self.assertEqual(json.loads(output.getvalue())['code'], 'inspection-failed')
        self.assertNotIn('secret', output.getvalue()); self.assertNotIn('https', output.getvalue())

    def test_gzip_state_is_decoded_before_bounded_json_parse(self):
        identity = {'release_id': 'a'*32, 'slot': 'a', 'tree_sha256': 'b'*64}
        response = mock.MagicMock(); response.__enter__.return_value = response
        response.raw = HTTPResponse(body=io.BytesIO(gzip.compress(json.dumps(identity).encode())),
                                    headers={'Content-Encoding': 'gzip'}, preload_content=False)
        with mock.patch.object(inspector.requests, 'get', return_value=response):
            self.assertEqual(inspector.read_identity(), identity)

    def test_phase_error_exposes_only_fixed_stage_and_exception_class(self):
        args = ['inspect', '--generation', 'a'*64, '--locale', 'fr', '--candidate', 'b'*64, '--active-release', 'a'*32]
        with mock.patch('sys.argv', args), mock.patch.object(inspector, 'read_identity', side_effect=UnicodeDecodeError('utf-8', b'private', 0, 1, 'secret')), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(inspector.main(), 1)
        result = json.loads(output.getvalue())
        self.assertEqual(result['stage'], 'active-identity-read')
        self.assertEqual(result['error_type'], 'UnicodeDecodeError')
        self.assertNotIn('secret', output.getvalue()); self.assertNotIn('private', output.getvalue())

    def test_state_read_uses_fixed_endpoint_no_redirect_and_size_bound(self):
        response = mock.MagicMock()
        response.__enter__.return_value = response
        response.raw.read.return_value = b'x'*(inspector.MAX_STATE_BYTES + 1)
        with mock.patch.object(inspector.requests, 'get', return_value=response) as get:
            with self.assertRaisesRegex(inspector.InspectionError, 'oversized-state'): inspector.read_identity()
        self.assertEqual(get.call_args.args, (inspector.ORIGIN+'/.well-known/edge-state',))
        self.assertFalse(get.call_args.kwargs['allow_redirects'])
        self.assertEqual(get.call_args.kwargs['timeout'], (10, 30))


if __name__ == '__main__':
    unittest.main()
