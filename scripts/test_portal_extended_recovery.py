"""Failure-injection regressions for runner transport and durable daily builds."""
import json
import math
import re
from pathlib import Path
import tempfile
import time
import unittest
from unittest import mock

import hymt_offline_translation as h
from build_portal_extended_locales import build
from portal_extended_locales import ADDITIONAL, make_corpus
from test_portal_extended_incremental import DAY, daily_doc
from test_portal_extended_locales import FakeTranslator
from test_portal_extended_r2 import FakeR2
from portal_extended_r2 import R2Store
import portal_extended_incremental as incremental


class TransportRecoveryTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.engine = object.__new__(h._HyMTEngine)
        self.engine.port = 1
        self.translator = h.OfflineTranslator(cache_dir=self.root/'cache',
            engine_factory=lambda _s, _t: self.engine)
        self.response = {'choices': [{'finish_reason': 'stop',
                                     'message': {'content': 'Texte traduit de référence.'}}]}

    def test_request_timeout_recovers_without_exhausting_four_hour_budget(self):
        corpus = make_corpus([daily_doc()])
        with mock.patch.object(h, 'request_json', side_effect=[TimeoutError('fixture'), self.response]) as request:
            # Other unique units use the same valid response after the timeout.
            def reply(*_args, **_kwargs):
                if request.call_count == 1:
                    raise TimeoutError('fixture')
                return self.response
            request.side_effect = reply
            result = build(corpus, 'fr', self.root/'out', self.root/'checkpoint.json',
                           self.translator, budget_seconds=14400)
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertFalse(result['budget_exhausted'])
        self.assertGreater(request.call_count, 1)

    def test_repeated_request_timeouts_remain_incomplete_and_resume_exact_units(self):
        corpus = make_corpus([daily_doc()])
        with mock.patch.object(h, 'request_json', side_effect=TimeoutError('fixture')) as request:
            first = build(corpus, 'fr', self.root/'first', self.root/'checkpoint.json',
                          self.translator, budget_seconds=14400, allow_source_fallback=True)
        self.assertFalse(first['budget_exhausted'])
        self.assertEqual(first['status'], 'incomplete-candidate')
        self.assertEqual(first['source_fallback_unit_count'], 0)
        self.assertEqual(first['failures'][0]['code'], 'offline-request-timeout')
        self.assertEqual(request.call_count, 3)
        with mock.patch.object(h, 'request_json', return_value=self.response):
            resumed = build(corpus, 'fr', self.root/'resumed', self.root/'checkpoint.json', self.translator)
        self.assertEqual(resumed['status'], 'complete-candidate')
        with mock.patch.object(h, 'request_json', side_effect=AssertionError('Completed units must be reused')):
            repeated = build(corpus, 'fr', self.root/'repeated', self.root/'checkpoint.json', self.translator)
        self.assertEqual(repeated['translation_calls_this_run'], 0)

    def test_only_actual_deadline_stops_the_batch(self):
        with mock.patch.object(h.time, 'monotonic', side_effect=[100, 106]), \
             mock.patch.object(h, 'request_json', side_effect=TimeoutError('fixture')) as request:
            with self.assertRaises(h.TranslationBudgetExceeded):
                self.engine.translate('Research', 'en', 'fr', deadline=105)
        self.assertEqual(request.call_count, 1)
        self.assertEqual(request.call_args.kwargs['timeout'], 5)

    def test_retry_timeouts_are_bounded_by_remaining_budget(self):
        with mock.patch.object(h.time, 'monotonic', side_effect=[100, 110, 110]), \
             mock.patch.object(h, 'request_json', side_effect=[TimeoutError('fixture'), self.response]) as request:
            self.engine.translate('Research', 'en', 'fr', deadline=120)
        self.assertEqual([call.kwargs['timeout'] for call in request.call_args_list], [20, 10])

    def test_source_fallback_does_not_hide_http_or_runtime_failure(self):
        for status, calls in ((503, 3), (400, 1)):
            with self.subTest(status=status), mock.patch.object(h, 'request_json',
                    side_effect=h.ModelHTTPError(status)) as request:
                with self.assertRaises(h.OfflineTranslationError) as caught:
                    self.engine.translate('Research', 'en', 'fr')
                self.assertEqual(caught.exception.code, f'offline-http-{status}')
                self.assertEqual(request.call_count, calls)

    def test_recovered_request_still_rejects_damaged_quantity_and_never_caches(self):
        damaged = {'choices': [{'finish_reason': 'stop', 'message': {'content': 'Revenu EUR999m.'}}]}
        self.translator.validation_attempts = 1
        with mock.patch.object(h, 'request_json', side_effect=[TimeoutError('fixture'), damaged]):
            with self.assertRaises(h.OfflineTranslationValidationError):
                self.translator.translate('Revenue USD10m.', 'fr', 'en', markdown=False)
        self.assertFalse(list((self.root/'cache').rglob('*.json')))

    def test_generic_timeout_from_adapter_is_a_failed_unit_not_budget_exhaustion(self):
        class Timed(FakeTranslator):
            def translate(self, *args, **kwargs):
                raise TimeoutError('adapter request timeout')
        result = build(make_corpus([daily_doc()]), 'fr', self.root/'out',
                       self.root/'memo.json', Timed(), allow_source_fallback=True)
        self.assertFalse(result['budget_exhausted'])
        self.assertEqual(result['failures'][0]['code'], 'offline-request-timeout')

    def test_next_day_reuses_only_exact_validated_units_without_backfill(self):
        first = make_corpus([daily_doc()])
        build(first, 'fr', self.root/'first', self.root/'memo.json', FakeTranslator())
        tomorrow = '2026-09-26'
        second = make_corpus([daily_doc('https://kcdesk.com/blog/20260926-new.html', day=tomorrow)])
        translator = FakeTranslator()
        result = build(second, 'fr', self.root/'next', self.root/'next.json', translator,
                       seed_checkpoint=self.root/'memo.json')
        self.assertEqual(translator.calls, 0)
        self.assertEqual(result['source_document_count'], 1)
        self.assertEqual([page['source_url'] for page in result['pages']], [second['documents'][0]['url']])
        self.assertNotEqual(first['documents_sha256'], second['documents_sha256'])

    def test_historical_recovery_reads_exact_generation_without_any_r2_write(self):
        client = FakeR2()
        store = R2Store(client, 'private-bucket', '_extended-locales/staging/test')
        corpus = make_corpus([daily_doc()])
        store.put_source(corpus)
        stored = dict(client.objects)
        for operation in ('prepare', 'prepare-recovery'):
            args = ['test', operation, '--generation', corpus['documents_sha256'],
                    '--corpus', str(self.root/'source.json'), '--locales', 'fr']
            with mock.patch('sys.argv', args), mock.patch.object(incremental, 'today', return_value='2026-09-28'), \
                 mock.patch.object(incremental.R2Store, 'from_env', return_value=store), \
                 mock.patch.object(incremental, 'collect_today', side_effect=AssertionError('No collection for replay')):
                if operation == 'prepare':
                    with self.assertRaisesRegex(incremental.ExpansionError, 'historical'):
                        incremental.main()
                else:
                    self.assertEqual(incremental.main(), 0)
            self.assertEqual(client.objects, stored)

    def test_recovery_workflow_disables_both_durable_write_steps(self):
        workflow = (Path(__file__).resolve().parent.parent/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        self.assertEqual(workflow.count("if: always() && inputs.operation != 'recovery-test'"), 2)
        self.assertIn("extended-locales-r2-recovery-{0}", workflow)
        self.assertIn("'r2_writes': 0", workflow)

    def test_full_locale_matrix_execution_capacity_fits_a_daily_window(self):
        workflow = (Path(__file__).resolve().parent.parent/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        locale_job = workflow.split('\n  locale:\n', 1)[1]
        timeout = int(re.search(r'timeout-minutes: (\d+)', locale_job)[1])
        workers = int(re.search(r'max-parallel:.*\|\| (\d+)', locale_job)[1])
        self.assertLess(math.ceil(len(ADDITIONAL) / workers) * timeout, 24 * 60)
        self.assertLessEqual(workers, 8)


if __name__ == '__main__':
    unittest.main()
