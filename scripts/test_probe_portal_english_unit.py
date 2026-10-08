"""Source-bound one-unit CPU diagnostics never alter production objects."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
from hymt_offline_translation import OfflineTranslationValidationError, _restore_terms
from financial_quantity_integrity import quantities
from portal_extended_locales import ExpansionError, digest
from portal_english_commentary import build
from portal_english_pipeline import batch_admission, persist_candidate, prepare_queued, remember_checkpoint
import test_portal_english_pipeline as fixture_module
from test_portal_english_pipeline import CPU_PRODUCER
from test_portal_english_commentary import COMMENT, TITLE, SyntheticTranslator
from probe_portal_english_unit import input_forms, probe

PRIVATE = '我的独家判断是欧洲投资达到150亿欧元，企业仍需改善长期回报。'


class ProbeTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture_module.EnglishPipelineTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        f = self.fixture
        f.admit(content=f'<section><strong>KC评论：</strong><p>{COMMENT}</p><p>{PRIVATE}</p></section>')
        prepared = prepare_queued(f.store, f.original)
        _, _, self.source = batch_admission(f.store, f.original, prepared['job']['generation'])
        directory = f.root/'failed'; checkpoint = f.root/'checkpoint.json'
        translator = SyntheticTranslator(); original = translator.translate
        def translate(value, *args, **kwargs):
            if value == PRIVATE: raise OfflineTranslationValidationError('Private rejected prose')
            return original(value, *args, **kwargs)
        translator.translate = translate
        manifest = build(self.source, directory, checkpoint, translator)
        self.assertEqual(manifest['status'], 'incomplete-candidate')
        self.checkpoint = remember_checkpoint(f.store, self.source['generation'], checkpoint)
        self.candidate = persist_candidate(f.store, f.original, self.source, directory, CPU_PRODUCER)
        self.before = copy.deepcopy(f.client.objects)
        self.calls = []
        outer = self
        class Engine:
            def translate(self, value, source, target, **kwargs):
                outer.calls.append((value, source, target, kwargs))
                return outer.responses.pop(0)
            def close(self): outer.closed = True
        self.engine = Engine()
        self.factory = mock.Mock(return_value=self.engine)
        self.responses = ['European investment is EUR 16 billion.', 'European investment is EUR 15 billion.',
                          'European investment is EUR 15 billion and EUR 15 billion.']
        self.closed = False

    def run_probe(self, **changes):
        values = dict(generation=self.source['generation'], checkpoint_sha=self.checkpoint['sha256'],
            candidate_id=self.candidate['candidate_id'], unit_sha=digest(PRIVATE.encode()),
            output=self.fixture.root/'numeric-result.json', engine_factory=self.factory)
        values.update(changes)
        return probe(self.fixture.store, self.fixture.original, **values)

    def test_three_equivalent_inputs_full_source_gates_and_no_writes(self):
        result = self.run_probe()
        self.assertEqual(self.fixture.client.objects, self.before)
        self.assertEqual([row['accepted'] for row in result['results']], [False, True, False])
        self.assertEqual((result['model_calls'], result['production_writes'], result['paid_provider_requests']), (3,0,0))
        self.assertTrue(self.closed)
        self.assertEqual(len({call[3]['deadline'] for call in self.calls}), 1)
        for value, source, target, kwargs in self.calls:
            self.assertEqual(quantities(value), quantities(PRIVATE))
            self.assertEqual((source,target,kwargs['quality_retry']), ('zh','en',2))
        public = json.dumps(result, ensure_ascii=False)
        for private in (PRIVATE, COMMENT, TITLE, 'European investment', 'Private rejected prose'):
            self.assertNotIn(private, public)
        self.assertEqual(len(result['results'][0]['missing_quantities']['rows']), 1)
        self.assertEqual(result['results'][2]['extra_quantities']['rows'][0]['count'], 1)
        self.assertFalse(list(self.fixture.root.glob('**/*translation*.json')))

    def test_production_sequence_matches_actual_inputs_and_retry_indices(self):
        self.responses = ['Investment is EUR 15 billion and 30%.',
                          'Investment is EUR 15 billion and 30%.', 'Investment is EUR 15 billion.']
        result = self.run_probe(mode='production-sequence')
        self.assertEqual([call[3]['quality_retry'] for call in self.calls], [0,1,2])
        self.assertEqual([call[0] for call in self.calls[:2]], [PRIVATE, PRIVATE])
        self.assertIn('EUR 15,000,000,000', self.calls[2][0])
        self.assertEqual([row['accepted'] for row in result['results']], [False,False,True])
        self.assertEqual(self.fixture.client.objects, self.before)

    def test_production_sequence_stops_when_adapter_accepts_or_runtime_fails(self):
        self.responses = ['Investment is EUR 15 billion.']
        result = self.run_probe(mode='production-sequence')
        self.assertEqual(result['model_calls'], 1)
        self.assertTrue(result['results'][0]['accepted'])
        (self.fixture.root/'numeric-result.json').unlink()
        from hymt_offline_translation import OfflineTranslationError
        self.engine.translate = mock.Mock(side_effect=OfflineTranslationError('private failure'))
        result = self.run_probe(mode='production-sequence')
        self.assertEqual(result['model_calls'], 1)
        self.assertNotIn('private failure', json.dumps(result))
        self.assertEqual(self.fixture.client.objects, self.before)

    def test_wrong_source_or_cached_unit_rejected_before_model(self):
        for sha in ('f'*64, digest(TITLE.encode())):
            with self.assertRaises(ExpansionError): self.run_probe(unit_sha=sha)
        self.factory.assert_not_called()
        self.assertEqual(self.fixture.client.objects, self.before)

    def test_tampered_checkpoint_or_candidate_rejected_before_model(self):
        for key in (self.fixture.store.checkpoint_object_key('en', self.source['generation'], self.checkpoint['sha256']),
                    self.fixture.store.key('candidates', self.source['generation'], self.candidate['candidate_id'], 'candidate-manifest.json')):
            original = self.fixture.client.objects[key]
            self.fixture.client.objects[key] = b'{}'
            with self.assertRaises(Exception): self.run_probe()
            self.fixture.client.objects[key] = original
        self.factory.assert_not_called()
        self.assertEqual(self.fixture.client.objects, self.before)

    def test_all_input_forms_proved_before_engine_creation(self):
        with mock.patch('probe_portal_english_unit.input_forms', side_effect=ExpansionError('unsupported')):
            with self.assertRaises(ExpansionError): self.run_probe()
        self.factory.assert_not_called()

    def test_unknown_engine_error_is_not_masked_as_translation_rejection(self):
        self.engine.translate = mock.Mock(side_effect=RuntimeError('private raw body'))
        with self.assertRaises(RuntimeError): self.run_probe()
        self.assertTrue(self.closed)
        public = (self.fixture.root/'numeric-result.json').read_text()
        self.assertNotIn('private raw body', public)
        self.assertEqual(self.fixture.client.objects, self.before)

    def test_known_engine_error_has_only_fixed_category(self):
        self.engine.translate = mock.Mock(side_effect=OfflineTranslationValidationError('private raw body'))
        result = self.run_probe()
        self.assertEqual(result['model_calls'], 3)
        self.assertNotIn('private raw body', json.dumps(result))
        self.assertFalse(any(row['accepted'] for row in result['results']))

    def test_input_form_scope_and_exact_decimal(self):
        forms = input_forms(PRIVATE)
        self.assertEqual([row[0] for row in forms], ['production','absolute','scaled'])
        self.assertIn('EUR 15,000,000,000', forms[0][1])
        self.assertIn('EUR 15000000000', forms[1][1])
        self.assertIn('EUR 15 billion', forms[2][1])
        for unsupported in ('没有金额。', '金额150亿欧元及100亿美元。', '金额150亿欧元，增长10%。'):
            with self.assertRaises(ExpansionError): input_forms(unsupported)
        for form in input_forms('金额15.25亿欧元。'):
            self.assertEqual(quantities(form[1]), quantities('金额15.25亿欧元。'))

    def test_workflow_only_uploads_numeric_receipt(self):
        path = Path(__file__).resolve().parents[1]/'.github/workflows/portal-english-unit-probe.yml'
        value = path.read_text()
        self.assertIn('contents: read', value)
        self.assertIn('runs-on: ubuntu-22.04', value)
        self.assertIn('default: production-sequence', value)
        self.assertNotIn('contents: write', value)
        self.assertIn('persist-audit: \'false\'', value)
        self.assertIn('path: ${{ runner.temp }}/english-unit-probe.json', value)
        self.assertNotIn('actions/cache', value)


if __name__ == '__main__': unittest.main()
