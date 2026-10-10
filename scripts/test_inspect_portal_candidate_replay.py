"""Offline, real candidate/checkpoint diagnostic contracts; no provider calls."""
import contextlib
import io
import gzip
from urllib3.response import HTTPResponse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
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

    def test_actual_missing_call_has_exact_field_hash_and_never_repairs_a_cache(self):
        corpus = fixtures.make_corpus([fixtures.daily_doc()])
        source = corpus['documents'][0]['title']
        self.assertNotIn('|', source)
        language = inspector.extended_source_language(source)
        key = inspector.unit_key('fr', source, language, False)
        path = self.base/'missing.json'
        self.store.restore_checkpoint('fr', self.batch['generation'], path)
        seed = json.loads(path.read_bytes()); del seed['rows'][key]
        path.write_text(json.dumps(seed)); self.store.put_checkpoint('fr', self.batch['generation'], path)
        before = {k: dict(v) for k, v in self.store.client.objects.items()}
        original = inspector.publication.CacheOnly
        result = inspector.compare(self.store, self.batch, 'fr', self.base/'missing-inspect', frozen_approval=True)
        self.assertFalse(result['matches']); self.assertIs(inspector.publication.CacheOnly, original)
        self.assertEqual(before, self.store.client.objects)
        for attempt in result['baseline_attempts']:
            item = attempt['failed_unit_diagnostics']['failures'][0]
            self.assertEqual(item['field'], 'title')
            self.assertEqual(item['source_sha256'], inspector.digest(source.encode()))
            self.assertEqual(item['unit_sha256'], key)
            self.assertTrue(item['actual_call_matches_resolved_field'])
            self.assertFalse(item['exact_translation_key_present'])
            self.assertFalse(item['exact_fallback_key_present'])
            self.assertEqual(item['same_source_variants']['count'], 0)
        self.assertNotIn(source, json.dumps(result)); self.assertNotIn(fixtures.URL, json.dumps(result))

    def unit_probe(self, source='Private factual research prose.', *, seed=None, approved_keys=None,
                   field='title', parent=None, markdown=False, include_inventory=True):
        doc = {'url': fixtures.URL, 'title': parent or source, 'description': '', 'blocks': [], 'links': []}
        if field.startswith('block.'):
            doc['blocks'] = [{'tag': 'p', 'text': parent or source}]
        language = inspector.extended_source_language(source)
        approved = {'source_fallback_unit_sha256': approved_keys or []} if include_inventory else {}
        report = inspector.failed_unit_diagnostics({'documents': [doc]}, 'es', seed or {'rows': {}}, approved,
            {'failures': [{'url': fixtures.URL, 'field': field, 'code': 'offline-approval-cache-miss'}]},
            [(source, 'es', language, markdown)])
        return report, report['failures'][0]

    def test_probe_distinguishes_numeric_advisory_from_missing_approved_fallback(self):
        source = 'Private source revenue USD10m.'
        key = inspector.unit_key('es', source, 'en', False)
        seed = {'rows': {key: {'source': source, 'language': 'en', 'text': 'Ingresos USD11m.'}}}
        report, item = self.unit_probe(source, seed=seed, approved_keys=[key])
        self.assertTrue(item['exact_translation_identity_matches'])
        self.assertEqual(item['current_validation'], 'accepted')
        self.assertEqual(item['approved_quantity_validation'], 'financial-quantity-validation')
        self.assertTrue(item['approved_fallback_member'])
        self.assertEqual(report['approved_fallback_keys_absent'], 1)
        seed['source_fallbacks'] = {key: {'source': source, 'language': 'en', 'policy': 'wrong'}}
        report, item = self.unit_probe(source, seed=seed, approved_keys=[key])
        self.assertTrue(item['exact_fallback_key_present'])
        self.assertFalse(item['exact_fallback_identity_matches'])
        self.assertEqual(report['approved_fallback_keys_present'], 1)
        self.assertNotIn('USD10m', json.dumps(report)); self.assertNotIn('USD11m', json.dumps(report))

    def test_probe_separates_other_language_and_markdown_keys_without_using_them(self):
        source = 'Private factual research prose.'
        seed = {'rows': {inspector.unit_key('es', source, language, markdown):
            {'source': source, 'language': language, 'text': 'Análisis publicado.'}
            for language, markdown in (('zh', False), ('en', True))}}
        _, item = self.unit_probe(source, seed=seed)
        self.assertFalse(item['exact_translation_key_present'])
        self.assertEqual(item['same_source_variants']['count'], 2)
        self.assertEqual({(r['language'], tuple(r['key_matches_markdown']))
            for r in item['same_source_variants']['rows']}, {('zh', (False,)), ('en', (True,))})

    def test_probe_finds_whole_pipe_parent_and_preserves_part_markdown(self):
        source = 'Private part'; parent = source + '| second private part'
        key = inspector.unit_key('es', parent, 'en', True)
        seed = {'source_fallbacks': {key: {'source': parent, 'language': 'en', 'policy': inspector.SOURCE_FALLBACK_VERSION}}}
        _, item = self.unit_probe(source, parent=parent, field='block.0.p.part0', markdown=True,
            seed=seed, approved_keys=[key])
        self.assertTrue(item['actual_call_matches_resolved_field']); self.assertTrue(item['markdown'])
        self.assertEqual(item['same_source_variants']['count'], 0)
        self.assertEqual(item['whole_pipe_parent']['variants']['count'], 1)
        self.assertTrue(item['whole_pipe_parent']['variants']['rows'][0]['approved_fallback_member'])
        self.assertFalse(item['approved_fallback_member'])
        self.assertNotIn(parent, json.dumps(item)); self.assertNotIn(source, json.dumps(item))

    def test_real_pipe_split_miss_is_bound_to_the_actual_builder_call(self):
        corpus = fixtures.make_corpus([fixtures.daily_doc(body='<h1>Research</h1><p>Private left | private right</p>')])
        work = self.base/'pipe'; work.mkdir()
        fixtures.build(corpus, 'es', work/'candidate', work/'memo.json', fixtures.FakeTranslator(), allow_source_fallback=True)
        seed = json.loads((work/'memo.json').read_bytes())
        parent = corpus['documents'][0]['blocks'][1]['text']
        source = parent.split('|')[0]
        del seed['rows'][inspector.unit_key('es', source, 'en', True)]
        key = inspector.unit_key('es', parent, 'en', True)
        seed.setdefault('source_fallbacks', {})[key] = {'source': parent, 'language': 'en',
            'policy': inspector.SOURCE_FALLBACK_VERSION, 'code': 'offline-validation'}
        (work/'memo.json').write_text(json.dumps(seed))
        generation = corpus['documents_sha256']
        self.store.put_source(corpus); self.store.put_checkpoint('es', generation, work/'memo.json')
        saved = self.store.upload_candidate(work/'candidate', 'es', generation)
        result = inspector.compare(self.store, {'generation': generation, 'candidates': {'es': saved['candidate_id']}},
            'es', self.base/'pipe-inspect', frozen_approval=True)
        self.assertFalse(result['matches'])
        for attempt in result['baseline_attempts']:
            item = attempt['failed_unit_diagnostics']['failures'][0]
            self.assertEqual(item['field'], 'block.1.p.part0')
            self.assertTrue(item['actual_call_matches_resolved_field']); self.assertTrue(item['markdown'])
            self.assertEqual(item['whole_pipe_parent']['variants']['rows'][0]['unit_sha256'], key)

    def test_old_manifest_inventory_unknown_is_not_reported_as_absent_or_false(self):
        report, item = self.unit_probe(include_inventory=False)
        self.assertFalse(report['approved_fallback_inventory_present'])
        self.assertIsNone(report['approved_fallback_keys_absent'])
        self.assertIsNone(item['approved_fallback_member'])

    def test_unresolved_fields_and_trace_disagreement_are_explicit_and_redacted(self):
        for field in ('private secret', 'copy.private-secret', 'block.9.p', 'title.part0', 'link.99999', 'title.part1.part2'):
            report, item = self.unit_probe(field=field)
            self.assertEqual(item, {'code': 'unresolved-field'})
            self.assertNotIn('private secret', json.dumps(report))
        _, item = self.unit_probe(markdown=True)
        self.assertFalse(item['actual_call_matches_resolved_field'])

    def test_variant_output_is_bounded_and_exception_restores_cache_only_factory(self):
        source = 'Private factual research prose.'
        seed = {'rows': {f'{n:064x}': {'source': source, 'language': 'private-secret', 'text': 'private raw'}
                        for n in range(12)}}
        _, item = self.unit_probe(source, seed=seed)
        self.assertEqual(item['same_source_variants']['count'], 12)
        self.assertEqual(len(item['same_source_variants']['rows']), inspector.MAX_UNIT_VARIANTS)
        self.assertTrue(item['same_source_variants']['truncated'])
        self.assertNotIn('private-secret', json.dumps(item)); self.assertNotIn('private raw', json.dumps(item))
        original = inspector.publication.CacheOnly
        with self.assertRaisesRegex(ValueError, 'stop'):
            with inspector.record_cache_misses(): raise ValueError('stop')
        self.assertIs(inspector.publication.CacheOnly, original)

    def test_missing_quantity_category_is_reported_without_values(self):
        result = inspector.quantity_signature('Revenue USD120m.', 'Revenue USD999m.', 'fr')
        self.assertEqual(result['missing_kinds'], {'currency': 1})
        self.assertEqual(result['added_kinds'], {'currency': 1})
        self.assertNotIn('120', json.dumps(result)); self.assertNotIn('999', json.dumps(result))

    def test_bn_month_signature_proves_exact_calendar_equivalence_only(self):
        september = inspector.BN_MONTH_ALIASES[8][0]
        result = inspector.quantity_signature('9月研究报告', september+' গবেষণা প্রতিবেদন', 'bn')
        self.assertEqual(result['missing_kinds'], {'month': 1})
        self.assertEqual(result['added_kinds'], {})
        self.assertTrue(result['language_scoped_month_repair_matches'])
        self.assertNotIn(september, json.dumps(result))
        october = inspector.BN_MONTH_ALIASES[9][0]
        self.assertFalse(inspector.quantity_signature('9月', october, 'bn')['language_scoped_month_repair_matches'])
        self.assertFalse(inspector.quantity_signature('9月 90%', september+' 80%', 'bn')['language_scoped_month_repair_matches'])
        self.assertFalse(inspector.quantity_signature('9月', september+'ে', 'bn')['language_scoped_month_repair_matches'])

    def test_inspector_replays_both_historical_numeric_rules_under_current_seo_policy(self):
        old = self.fixture.legacy_bn_candidate()
        result = inspector.compare(self.store, old, 'bn', self.base/'legacy-inspect', frozen_approval=True)
        self.assertTrue(result['matches'])
        self.assertEqual(result['quantity_contract'], 'current')
        self.assertEqual([a['contract'] for a in result['baseline_attempts']], ['current'])
        self.assertTrue(result['baseline_attempts'][0]['matches'])
        self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['rejected_rows_total'], 0)
        new = self.fixture.legacy_bn_candidate(current_rule=True)
        result = inspector.compare(self.store, new, 'bn', self.base/'new-inspect', frozen_approval=True)
        self.assertTrue(result['matches']); self.assertEqual(result['quantity_contract'], 'current')
        self.assertEqual(len(result['baseline_attempts']), 1)
        self.assertEqual(result['translation_calls'], 0)

    def test_exact_candidate_replays_without_writes_or_inference(self):
        before = {key: dict(value) for key, value in self.store.client.objects.items()}
        result = self.compare()
        self.assertTrue(result['matches'])
        self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['changed_pages'], [])
        self.assertEqual(result['rejected_rows_total'], 0)
        self.assertEqual(before, self.store.client.objects)

    def test_active_only_uses_only_pinned_active_batches_and_stays_read_only(self):
        before = {key: dict(value) for key, value in self.store.client.objects.items()}
        with mock.patch.object(inspector, 'read_active_ledger', return_value=self.fixture.active_ledger([self.batch])):
            result = inspector.inspect(self.store, None, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'all-matched')
        self.assertEqual(result['mode'], 'active-only')
        self.assertEqual(result['active_release'], 'a'*32)
        self.assertEqual(len(result['results']), 1)
        self.assertFalse(result['results'][0]['target_candidate'])
        self.assertEqual(before, self.store.client.objects)
        self.assertEqual(result['inference_calls'], 0)
        self.assertEqual(result['production_writes'], 0)
        self.assertTrue(result['results'][0]['approved_checkpoint_replay']['reused_verified_latest_replay'])
        for private in ('Texte traduit', fixtures.URL, 'Source based'):
            self.assertNotIn(private, json.dumps(result))

    def test_empty_active_only_is_explicitly_not_a_replay_acceptance(self):
        with mock.patch.object(inspector, 'read_active_ledger', return_value={'batches':[]}), \
             mock.patch.object(inspector, 'compare') as compare:
            result = inspector.inspect(self.store, None, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'no-active-batches')
        self.assertEqual(result['results'], [])
        compare.assert_not_called()

    def test_read_only_client_forbids_mutating_operations_before_call(self):
        underlying = mock.Mock()
        client = inspector.ReadOnlyClient(underlying)
        for name in ('put_object', 'delete_object', 'copy_object', 'list_objects_v2'):
            with self.subTest(name=name), self.assertRaisesRegex(inspector.InspectionError, 'storage-operation-forbidden'):
                getattr(client, name)
        self.assertEqual(underlying.mock_calls, [])
        client.head_object(Key='safe'); client.get_object(Key='safe')
        self.assertEqual(len(underlying.mock_calls), 2)

    def test_every_baseline_attempt_reports_only_bounded_replay_counters(self):
        batch = self.fixture.legacy_bn_candidate()
        result = inspector.compare(self.store, batch, 'bn', self.base/'attempts', frozen_approval=True)
        self.assertEqual(len(result['baseline_attempts']), 1)
        for attempt in result['baseline_attempts']:
            self.assertEqual(attempt['approved_pages'], 1)
            self.assertIn('replayed_pages', attempt)
            self.assertIn('cache_hits', attempt)
            self.assertIn('failure_codes', attempt)
            self.assertNotIn('source', attempt)
        self.assertTrue(result['baseline_attempts'][-1]['matches'])

    def test_active_only_latest_mismatch_is_compared_with_exact_approved_seed(self):
        self.mutate_checkpoint('Autre traduction valide et privée.')
        with mock.patch.object(inspector, 'read_active_ledger', return_value=self.fixture.active_ledger([self.batch])):
            result = inspector.inspect(self.store, None, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'all-matched')
        self.assertEqual(len(result['results'][0]['baseline_attempts']), 2)
        self.assertFalse(result['results'][0]['matches'])
        self.assertTrue(result['results'][0]['publication_matches'])
        pin = result['results'][0]['approved_checkpoint_replay']
        self.assertTrue(pin['matches']); self.assertEqual(pin['code'], 'matched')
        self.assertEqual(pin['cache_miss_attempts'], 0)
        self.assertFalse(pin['reused_verified_latest_replay'])
        self.assertNotEqual(pin['checkpoint_sha256'], result['results'][0]['checkpoint_sha256'])
        self.assertFalse(result['results'][0]['target_candidate'])
        self.assertNotIn('Autre traduction', json.dumps(result))

    def test_active_only_preserves_first_mismatch_if_later_audit_fails(self):
        self.mutate_checkpoint('Autre traduction valide et privée.')
        ledger = self.ledger_using_latest()
        for index, error in enumerate((inspector.InspectionError('too-many-cache-audits'),
                                       RuntimeError('private https://secret/?token=hidden'))):
            with self.subTest(index=index), mock.patch.object(inspector, 'read_active_ledger', return_value=ledger), \
                 mock.patch.object(inspector, 'audit_cached_rows', side_effect=error):
                result = inspector.inspect(self.store, None, 'a'*32, {'release_id': 'a'*32})
            self.assertEqual(result['status'], 'mismatch')
            self.assertEqual(len(result['results']), 1)
            self.assertFalse(result['cache_audit_complete'])
            self.assertEqual(result['carry_forward_cache_audit'], [])
            self.assertEqual(result['cache_audit_code'], 'cache-audit-bound' if index == 0 else 'cache-audit-unavailable')
            for private in ('Autre traduction', 'private', 'secret', 'hidden'):
                self.assertNotIn(private, json.dumps(result))

    def mutate_checkpoint(self, text):
        seed = self.base/'mutated.json'
        self.store.restore_checkpoint('fr', self.batch['generation'], seed)
        value = json.loads(seed.read_bytes())
        next(iter(value['rows'].values()))['text'] = text
        seed.write_text(json.dumps(value))
        self.store.put_checkpoint('fr', self.batch['generation'], seed)

    def ledger_using_latest(self):
        ledger = self.fixture.active_ledger([self.batch])
        restored = self.store.restore_checkpoint('fr', self.batch['generation'], self.base/'latest-receipt.json')
        ledger['replays'][0]['checkpoint_sha256'] = restored['sha256']
        return ledger

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

    def test_numeric_advisory_does_not_approve_changed_candidate_html(self):
        self.mutate_checkpoint('Valeur privée 99999%.')
        result = self.compare()
        self.assertFalse(result['matches'])
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertEqual(result['rejected_rows_total'], 0)
        self.assertEqual(result['failure_codes'], {})
        self.assertEqual(result['translation_calls'], 0)
        # Numeric prose can pass the SEO validator, while different rendered
        # bytes still cannot stand in for the authenticated approved page.
        self.assertEqual(len(result['changed_pages']), 1)
        change = result['changed_pages'][0]
        self.assertFalse(change['descriptor_only'])
        self.assertNotEqual(change['approved_shape']['visible_text_sha256'],
                            change['replay_shape']['visible_text_sha256'])
        self.assertNotIn('Valeur privée', json.dumps(result))
        self.assertNotIn('99999', json.dumps(result))

    def test_missing_checkpoint_is_a_fixed_mismatch(self):
        key = self.store.checkpoint_pointer_key('fr', self.batch['generation'])
        del self.store.client.objects[key]
        result = self.compare()
        self.assertFalse(result['matches'])
        self.assertEqual(result['failure_codes'], {'checkpoint-absent': 1})

    def test_changed_active_identity_stops_before_private_reads(self):
        with mock.patch.object(inspector, 'read_active_ledger') as reader:
            with self.assertRaisesRegex(inspector.InspectionError, 'active-release-changed'):
                inspector.inspect(self.store, self.batch, 'a'*32, {'release_id': 'b'*32})
            reader.assert_not_called()

    def test_first_carry_forward_mismatch_precedes_new_target(self):
        target = self.fixture.candidate('pt')
        self.mutate_checkpoint('Autre traduction valide.')
        with mock.patch.object(inspector, 'read_active_ledger', return_value=self.ledger_using_latest()):
            result = inspector.inspect(self.store, target, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'mismatch')
        self.assertEqual(len(result['results']), 1)
        self.assertEqual(result['results'][0]['locale'], 'fr')
        self.assertFalse(result['results'][0]['target_candidate'])
        self.assertEqual(result['production_writes'], 0)
        self.assertEqual(result['inference_calls'], 0)

    def test_all_owned_active_tuple_pins_are_verified_before_all_matched(self):
        other = self.fixture.candidate('pt')
        ledger = self.fixture.active_ledger([self.batch, other])
        self.mutate_checkpoint('Autre traduction valide et privée.')
        before = {key: dict(value) for key, value in self.store.client.objects.items()}
        with mock.patch.object(inspector, 'read_active_ledger', return_value=ledger), \
             mock.patch('offline_translation.OfflineTranslator', side_effect=AssertionError('No inference adapter')):
            result = inspector.inspect(self.store, None, 'a'*32, {'release_id':'a'*32})
        self.assertEqual(result['status'], 'all-matched')
        self.assertEqual(result['checked_candidates'], result['selected_candidates'])
        self.assertEqual(result['checked_candidates'], 2)
        self.assertTrue(all(row['approved_checkpoint_replay']['matches'] for row in result['results']))
        self.assertEqual(before, self.store.client.objects)

    def test_same_exact_seed_reuses_baseline_only_after_reading_pinned_object(self):
        ledger=self.fixture.active_ledger([self.batch]); checksum=ledger['replays'][0]['checkpoint_sha256']
        key=self.store.checkpoint_object_key('fr',self.batch['generation'],checksum)
        reads=[]; original=self.store.client.get_object
        def read(**kwargs):
            reads.append(kwargs['Key']); return original(**kwargs)
        with mock.patch.object(inspector,'read_active_ledger',return_value=ledger), \
             mock.patch.object(self.store.client,'get_object',side_effect=read), \
             mock.patch.object(inspector,'prove_approved_baseline',wraps=inspector.prove_approved_baseline) as proof:
            result=inspector.inspect(self.store,None,'a'*32,{'release_id':'a'*32})
        self.assertEqual(proof.call_count,1)
        self.assertGreaterEqual(reads.count(key),2)
        self.assertTrue(result['results'][0]['approved_checkpoint_replay']['reused_verified_latest_replay'])

    def test_same_pin_digest_does_not_reuse_when_second_read_is_corrupt(self):
        ledger=self.fixture.active_ledger([self.batch]); checksum=ledger['replays'][0]['checkpoint_sha256']
        key=self.store.checkpoint_object_key('fr',self.batch['generation'],checksum)
        work=self.base/'latest-first'; latest=inspector.compare(self.store,self.batch,'fr',work,frozen_approval=True)
        self.store._put(key,b'private corrupted object',metadata={'kind':'test'})
        with mock.patch.object(inspector,'prove_approved_baseline') as proof:
            result=inspector.compare_active_checkpoint(self.store,ledger,self.batch,'fr',work,latest)
        self.assertFalse(result['matches']); proof.assert_not_called()
        self.assertEqual(result['code'],'approved-checkpoint-unavailable-or-invalid')
        self.assertNotIn('private corrupted',json.dumps(result))

    def test_missing_or_corrupt_latest_does_not_hide_valid_active_pin_evidence(self):
        key = self.store.checkpoint_pointer_key('fr', self.batch['generation'])
        original = self.store.client.objects.pop(key)
        ledger = self.fixture.active_ledger([self.batch])
        for state in ('missing', 'corrupt'):
            if state == 'corrupt':
                self.store._put(key,b'invalid private pointer',metadata={'kind':'test'})
            with self.subTest(state=state), mock.patch.object(inspector, 'read_active_ledger', return_value=ledger):
                result = inspector.inspect(self.store, None, 'a'*32, {'release_id':'a'*32})
            self.assertEqual(result['status'],'all-matched')
            self.assertFalse(result['results'][0]['matches'])
            self.assertTrue(result['results'][0]['approved_checkpoint_replay']['matches'])
            self.assertEqual(result['cache_audit_complete'], state == 'missing')
            self.assertNotIn('private pointer',json.dumps(result))
        self.store.client.objects[key] = original

    def test_missing_or_ambiguous_active_pin_is_not_excused_by_matching_latest(self):
        original = self.fixture.active_ledger([self.batch])
        for rows in ([], original['replays']*2):
            ledger = {**original,'replays':rows}
            with self.subTest(rows=len(rows)), mock.patch.object(inspector, 'read_active_ledger',return_value=ledger):
                result = inspector.inspect(self.store,None,'a'*32,{'release_id':'a'*32})
            self.assertEqual(result['status'],'mismatch')
            self.assertTrue(result['results'][0]['matches'])
            self.assertFalse(result['results'][0]['publication_matches'])
            self.assertEqual(result['results'][0]['approved_checkpoint_replay']['code'],'approved-checkpoint-receipt-invalid')

    def test_missing_active_blob_reports_pin_hash_and_keeps_latest_comparison(self):
        ledger = self.fixture.active_ledger([self.batch]); ledger['replays'][0]['checkpoint_sha256']='f'*64
        with mock.patch.object(inspector,'read_active_ledger',return_value=ledger):
            result=inspector.inspect(self.store,None,'a'*32,{'release_id':'a'*32})
        pin=result['results'][0]['approved_checkpoint_replay']
        self.assertEqual(result['status'],'mismatch')
        self.assertEqual(pin['checkpoint_sha256'],'f'*64)
        self.assertEqual(pin['code'],'approved-checkpoint-missing')
        self.assertTrue(result['results'][0]['matches'])

    def test_superseded_candidate_is_skipped_like_publication_owner_order(self):
        target = {'generation': self.batch['generation'], 'candidates': {'fr': 'c'*64}}
        with mock.patch.object(inspector, 'read_active_ledger', return_value=self.fixture.active_ledger([self.batch])), \
             mock.patch.object(inspector, 'compare', return_value={'matches': True}) as compare:
            result = inspector.inspect(self.store, target, 'a'*32, {'release_id': 'a'*32})
        self.assertEqual(result['status'], 'all-matched')
        self.assertEqual(compare.call_count, 1)
        self.assertEqual(compare.call_args.args[1], target)
        self.assertEqual(result['results'][0]['batch_index'], 1)

    def test_all_remaining_active_cache_audit_is_read_only_and_private(self):
        target = self.fixture.candidate('pt')
        self.mutate_checkpoint('Valeur privée 99999%.')
        before = {key: dict(value) for key, value in self.store.client.objects.items()}
        with mock.patch.object(inspector, 'read_active_ledger', return_value=self.fixture.active_ledger([self.batch])):
            result = inspector.inspect(self.store, target, 'a'*32, {'release_id': 'a'*32})
        audit = result['carry_forward_cache_audit']
        self.assertEqual([row['locale'] for row in audit], ['fr', 'pt'])
        self.assertEqual(audit[0]['rejected_codes'], {})
        self.assertEqual(audit[0]['quantity_signatures'], [])
        self.assertEqual(audit[1]['rejected_codes'], {})
        self.assertEqual(before, self.store.client.objects)
        self.assertNotIn('99999', json.dumps(result)); self.assertNotIn('Valeur privée', json.dumps(result))

    def test_checkpoint_audit_count_is_bounded(self):
        target = self.fixture.candidate('pt')
        self.mutate_checkpoint('Autre traduction valide.')
        with mock.patch.object(inspector, 'read_active_ledger', return_value=self.fixture.active_ledger([self.batch])), \
             mock.patch.object(inspector, 'MAX_CACHE_AUDITS', 1):
            with self.assertRaisesRegex(inspector.InspectionError, 'too-many-cache-audits'):
                inspector.inspect(self.store, target, 'a'*32, {'release_id': 'a'*32})

    def test_batch_bound_precedes_corpus_restoration(self):
        rows = [{'generation': f'{i:064x}', 'candidates': {'fr': 'c'*64}} for i in range(37)]
        with mock.patch.object(inspector, 'read_active_ledger', return_value={'batches':rows}), \
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

    def test_cli_modes_are_exclusive_and_complete_before_any_external_read(self):
        cases = [[], ['--generation', 'b'*64],
                 ['--active-only', '--locale', 'fr'],
                 ['--active-only', '--generation', 'b'*64, '--locale', 'fr', '--candidate', 'c'*64]]
        for case in cases:
            with self.subTest(case=case), mock.patch('sys.argv', ['inspect', '--active-release', 'a'*32, *case]), \
                 mock.patch.object(inspector, 'read_identity') as reader, \
                 mock.patch.object(inspector.R2Store, 'from_env') as storage, contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(inspector.main(), 1)
            reader.assert_not_called(); storage.assert_not_called()
            self.assertEqual(json.loads(output.getvalue())['code'], 'invalid-inspection-mode')

    def test_active_only_cli_checks_exact_release_before_storage(self):
        args = ['inspect', '--active-only', '--active-release', 'a'*32]
        with mock.patch('sys.argv', args), \
             mock.patch.object(inspector, 'read_identity', return_value={'release_id': 'b'*32}), \
             mock.patch.object(inspector.R2Store, 'from_env') as storage, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(inspector.main(), 1)
        storage.assert_not_called()
        self.assertEqual(json.loads(output.getvalue())['code'], 'active-release-changed')

    def test_active_only_cli_passes_no_synthetic_candidate(self):
        args = ['inspect', '--active-only', '--active-release', 'a'*32]
        identity = {'release_id': 'a'*32}
        with mock.patch('sys.argv', args), mock.patch.object(inspector, 'read_identity', return_value=identity), \
             mock.patch.object(inspector.R2Store, 'from_env', return_value=self.store), \
             mock.patch.object(inspector, 'inspect', return_value={'status':'all-matched'}) as inspect, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(inspector.main(), 0)
        inspect.assert_called_once_with(self.store, None, 'a'*32, identity)

    def test_actual_workflow_shell_forwards_modes_without_evaluating_inputs(self):
        workflow = Path(__file__).resolve().parent.parent/'.github/workflows/portal-candidate-replay-inspect.yml'
        shell = textwrap.dedent(workflow.read_text().rsplit('        run: |\n', 1)[1])
        binary = self.base/'bin'; binary.mkdir()
        fake = binary/'python3'
        fake.write_text('#!'+sys.executable+'\nimport json,os,sys\n'
                        'open(os.environ["ARGUMENT_FILE"],"w").write(json.dumps(sys.argv[1:]))\n')
        fake.chmod(0o755)
        for active in ('true', 'false'):
            output = self.base/f'arguments-{active}.json'
            candidate = '' if active == 'true' else '$(touch '+str(self.base/'unexpected')+')'
            env = dict(os.environ, PATH=str(binary)+os.pathsep+os.environ.get('PATH',''),
                       ARGUMENT_FILE=str(output), ACTIVE_ONLY=active, ACTIVE_RELEASE='a'*32,
                       EXPECTED_HEAD='', GITHUB_REF='refs/heads/main', GITHUB_SHA='b'*40,
                       GENERATION='' if active == 'true' else 'b'*64,
                       LOCALE='' if active == 'true' else 'fr', CANDIDATE=candidate)
            subprocess.run(['bash', '-c', shell], env=env, check=True, capture_output=True)
            args = json.loads(output.read_text())
            self.assertEqual('--active-only' in args, active == 'true')
            self.assertEqual(args[args.index('--candidate')+1], candidate)
            self.assertEqual(args[args.index('--active-release')+1], 'a'*32)
            self.assertFalse((self.base/'unexpected').exists())
        for expected, valid in (('b'*40, True), ('a'*40, False), ('', False), ('invalid', False)):
            output=self.base/'branch-arguments.json'
            if output.exists(): output.unlink()
            env.update(ARGUMENT_FILE=str(output),EXPECTED_HEAD=expected,GITHUB_REF='refs/heads/codex/test',
                       ACTIVE_ONLY='true',GENERATION='',LOCALE='',CANDIDATE='')
            result=subprocess.run(['bash','-c',shell],env=env,capture_output=True)
            self.assertEqual(result.returncode == 0, valid)
            self.assertEqual(output.exists(), valid)

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
