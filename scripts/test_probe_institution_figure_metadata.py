import copy
import unittest
import fitz
from unittest.mock import Mock, patch

import probe_institution_figure_metadata as p
from mineru_task_ledger import digest, encoded


class ProbeTests(unittest.TestCase):
    def test_pinned_inventory_is_complete_and_binds_exact_originals(self):
        value = p.selection()
        self.assertEqual(value['source_job_id'], '116174580136')
        bindings = [p.binding_for(row) for row in value['sources']]
        self.assertEqual(len({row['id'] for row in bindings}), 4)
        for row, binding in zip(value['sources'], bindings):
            self.assertEqual(binding['sha256'], row['sha256'])
            self.assertEqual(binding['size'], row['bytes'])

    def test_only_exact_claim_and_completed_cached_result_are_read(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger, cache = Mock(), Mock()
        ledger.store.get.return_value = ({'binding': binding, 'batch_key': 'batches/test'}, None)
        ledger._read_batch.return_value = ({'files': [binding]}, None)
        lineage = {'exact': True}
        with patch.object(p, 'read_completed_batch', return_value=(
                {binding['id']: {'_recovery_lineage': lineage}}, {'all_succeeded': True})):
            self.assertEqual(p.cached_payload(ledger, cache, binding), cache.get.return_value)
        cache.get.assert_called_once_with(binding, lineage)
        ledger.store.put.assert_not_called()
        cache.put.assert_not_called()
        ledger.provider.submit.assert_not_called()
        changed = copy.deepcopy(binding); changed['sha256'] = 'f' * 64
        ledger.store.get.return_value = ({'binding': changed, 'batch_key': 'batches/test'}, None)
        cache.reset_mock()
        with self.assertRaisesRegex(p.ProbeError, 'source_claim_missing'):
            p.cached_payload(ledger, cache, binding)
        cache.get.assert_not_called()

    def test_missing_cache_never_downloads_or_submits(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger, cache = Mock(), Mock()
        ledger.store.get.return_value = ({'binding': binding, 'batch_key': 'batches/test'}, None)
        ledger._read_batch.return_value = ({'files': [binding]}, None)
        cache.get.return_value = None
        with patch.object(p, 'read_completed_batch', return_value=(
                {binding['id']: {'_recovery_lineage': {}}}, {'all_succeeded': True})):
            with self.assertRaisesRegex(p.ProbeError, 'source_result_cache_missing'):
                p.cached_payload(ledger, cache, binding)
        ledger.provider.submit.assert_not_called()
        cache.put.assert_not_called()

    def test_write_capable_ledger_rejected_before_any_read(self):
        ledger = Mock(scope='institution', forbid_new_submissions=False)
        with self.assertRaisesRegex(p.ProbeError, 'read_only_scope'):
            p.probe(ledger, Mock(), 'private')
        ledger.store.get.assert_not_called()

    def test_invalid_binding_is_rejected(self):
        row = dict(p.selection()['sources'][0], local_filename='../outside.pdf')
        with self.assertRaises(ValueError): p.binding_for(row)

    def test_valid_segment_merge_exercises_production_consumer_on_exact_original(self):
        original = b'%PDF-fixture-original'
        row = dict(p.selection()['sources'][2], sha256=digest(original), bytes=len(original))
        binding = p.binding_for(row)
        ledger = Mock(); ledger.clock.return_value = 0
        plan = {'segments': [{'binding': {'part': 1}, 'page_start': 1, 'page_end': 200},
                             {'binding': {'part': 2}, 'page_start': 201, 'page_end': 214}]}
        proof = {'status': 'verified', 'production_consumer_verified': True,
                 'private_handoff_replay_verified': True, 'production_acceptance': False,
                 'complete_source_handoff': False, 'image_count': 8}
        def verify(path, payload, original_sha, budget):
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(payload, b'merged-result')
            self.assertEqual(original_sha, binding['sha256'])
            budget()
            return proof
        with patch.object(p, 'OriginalCache') as originals, \
                patch.object(p, 'read_segment_plan', return_value=plan), \
                patch.object(p, 'cached_payload', side_effect=[b'first', b'second']) as cached, \
                patch.object(p, 'merge_segments', return_value=b'merged-result') as merged, \
                patch.object(p, 'inspect_payload', return_value={'status': 'valid'}), \
                patch.object(p, 'verify_production_figures', side_effect=verify) as verifier, \
                patch.object(p, 'compare_cached_pdf', return_value={'pages': []}):
            originals.return_value.get.return_value = original
            result = p.inspect_source(ledger, Mock(), 'private', binding)
        self.assertEqual(cached.call_count, 2)
        self.assertEqual(merged.call_args.args[:2], (plan, [b'first', b'second']))
        self.assertEqual(verifier.call_count, 1)
        self.assertEqual(result['production_figure_consumer'], proof)
        self.assertEqual(result['merge']['status'], 'valid')
        self.assertFalse(result['production_figure_consumer']['production_acceptance'])
        ledger.provider.submit.assert_not_called()
        ledger.store.put.assert_not_called()

    def test_rejected_metadata_never_calls_production_consumer(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger = Mock(); ledger.clock.return_value = 0
        with patch.object(p, 'OriginalCache') as originals, \
                patch.object(p, 'read_segment_plan', return_value=None), \
                patch.object(p, 'cached_payload', return_value=b'result'), \
                patch.object(p, 'inspect_payload', return_value={'status': 'rejected'}), \
                patch.object(p, 'verify_production_figures') as verifier:
            originals.return_value.get.return_value = b'%PDF-fixture'
            result = p.inspect_source(ledger, Mock(), 'private', binding)
        verifier.assert_not_called()
        self.assertEqual(result['metadata']['status'], 'rejected')
        self.assertNotIn('production_figure_consumer', result)

    def test_rejected_consumer_diagnostic_uses_exact_eight_image_limit(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger = Mock(); ledger.clock.return_value = 0
        proof = {'status': 'rejected', 'category': 'figure_source_pixels_mismatch',
                 'production_consumer_verified': False}
        with patch.object(p, 'OriginalCache') as originals, \
                patch.object(p, 'read_segment_plan', return_value=None), \
                patch.object(p, 'cached_payload', return_value=b'result'), \
                patch.object(p, 'inspect_payload', return_value={'status': 'valid'}), \
                patch.object(p, 'verify_production_figures', return_value=proof), \
                patch.object(p, 'compare_cached_pdf', return_value={'pages': []}) as compare:
            originals.return_value.get.return_value = b'%PDF-fixture'
            result = p.inspect_source(ledger, Mock(), 'private', binding)
        self.assertEqual(compare.call_args.kwargs['max_images'], 8)
        self.assertEqual(compare.call_args.kwargs['deadline'], 480)
        self.assertEqual(compare.call_args.kwargs['original_sha256'], binding['sha256'])
        self.assertIs(result['production_figure_consumer'], proof)
        self.assertFalse(proof['production_consumer_verified'])

    def test_segment_diagnostic_identifies_split_catalog_loss_without_acceptance(self):
        with fitz.open() as document:
            group = document.add_ocg('PRIVATE GROUP', on=False)
            document.new_page(width=30, height=30)
            page = document.new_page(width=30, height=30)
            page.draw_rect(fitz.Rect(5, 5, 25, 25), fill=(1, 0, 0), oc=group)
            original = document.tobytes(no_new_id=True)
        with fitz.open(stream=original, filetype='pdf') as document, fitz.open() as split, fitz.open() as merged:
            split.insert_pdf(document, from_page=1, to_page=1)
            physical = split.tobytes(garbage=4, deflate=True, no_new_id=True)
            merged.insert_pdf(document)
            merged_raw = merged.tobytes(garbage=4, deflate=True, no_new_id=True)
        binding, segment_binding = {'id': 'original'}, {'id': 'segment'}
        archive = Mock(); archive.get.return_value = physical
        plan = {'segments': [{'binding': segment_binding, 'page_start': 2, 'page_end': 2}]}
        with patch.object(p, 'embedded_pdf', side_effect=[physical, merged_raw]):
            result = p.segment_pixel_diagnostics(original, b'merged', plan, [b'provider'],
                                                 binding, archive, 1, lambda: None)
        archive.get.assert_called_once_with(binding, segment_binding)
        self.assertEqual(result['segment_page_index'], 0)
        docs = result['documents']
        self.assertEqual(docs['original']['catalog']['OCProperties'], 'dict')
        self.assertEqual(docs['physical_segment']['catalog']['OCProperties'], 'null')
        boundaries = result['boundaries']
        self.assertGreater(boundaries['original_to_physical_segment']['pixels']['diff_pixel_count'], 0)
        self.assertEqual(boundaries['physical_segment_to_provider_segment']['pixels']['diff_pixel_count'], 0)
        self.assertEqual(boundaries['provider_segment_to_merged_provider']['pixels']['diff_pixel_count'], 0)
        self.assertFalse(result['production_acceptance'])
        self.assertNotIn('PRIVATE', str(result))

    def test_embedded_pdf_reads_real_zip_into_private_child_directory(self):
        import io, json, zipfile
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, 'w') as archive:
            archive.writestr('full.md', 'fixture')
            archive.writestr('content_list.json', '[]')
            archive.writestr('middle.json', json.dumps({'pdf_info': []}))
            archive.writestr('source.pdf', b'%PDF-fixture')
        self.assertEqual(p.embedded_pdf(payload.getvalue()), b'%PDF-fixture')

    def test_cache_miss_download_is_exact_done_lineage_read_only_and_counted(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger, cache, download = Mock(), Mock(), Mock(return_value=b'result')
        lineage = {'batch_id': 'job', 'batch_key': 'batches/'+'a'*32,
            'parent_batch_key': 'batches/'+'a'*32, 'data_id': binding['id'], 'child_ordinal': 0}
        ledger.store.get.return_value = ({'binding': binding, 'batch_key': lineage['batch_key']}, None)
        root = {'files': [binding], 'key': lineage['batch_key'], 'batch_id': 'job'}
        ledger._read_batch.return_value = root, None
        cache.get.return_value = None
        row = {'state': 'done', '_recovery_lineage': lineage, 'full_zip_url': 'https://PRIVATE.invalid/result'}
        downloads = []
        with patch.object(p, 'read_completed_batch', return_value=(
                {binding['id']: row}, {'all_succeeded': True})), patch.object(p, 'validate_zip') as validate:
            self.assertEqual(p.cached_payload(ledger, cache, binding, download=download, downloads=downloads), b'result')
        download.assert_called_once_with(row['full_zip_url'])
        validate.assert_called_once_with(b'result')
        self.assertEqual(downloads[0]['status'], 'validated')
        self.assertEqual(downloads[0]['source_binding_sha256'], binding['id'])
        self.assertNotIn('PRIVATE', str(downloads))
        cache.put.assert_not_called(); ledger.store.put.assert_not_called(); ledger.provider.submit.assert_not_called()
        download.reset_mock(); cache.get.side_effect = ValueError('invalid cache receipt')
        with patch.object(p, 'read_completed_batch', return_value=(
                {binding['id']: row}, {'all_succeeded': True})), self.assertRaisesRegex(ValueError, 'invalid cache'):
            p.cached_payload(ledger, cache, binding, download=download, downloads=[])
        download.assert_not_called()


if __name__ == '__main__': unittest.main()
