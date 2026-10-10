"""Source fallback contracts: synthetic responses only, no local model calls."""
import json
import copy
from contextlib import redirect_stdout
import hashlib
import io
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

import build_portal_extended_locales as builder
from build_portal_extended_locales import Memo, build, translate_document, public_translation_diagnostics
from hymt_offline_translation import OfflineTranslationError, OfflineTranslationValidationError
from hymt_offline_translation import quantity_failure_diagnostics
from portal_extended_locales import PublicParser, document_from_html, make_corpus
from assemble_portal_extended_locales import assemble, verified_candidate
import test_portal_extended_locales as fixtures
from test_portal_extended_locales import FakeTranslator, HOME, BLOG, html
from portal_extended_r2 import checkpoint_is_valid


class RejectedQuantity(FakeTranslator):
    def translate(self, text, target, source=None, *, markdown=True):
        if 'USD10m' in text:
            self.calls += 1
            # Simulates a completed response rejected by the inner model gate.
            raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed')
        return super().translate(text, target, source, markdown=markdown)


class DiagnosticRejectedQuantity(RejectedQuantity):
    def __init__(self):
        super().__init__()
        self.failure_diagnostics = []
        self.validation_failure_count = 0

    def translate(self, text, target, source=None, *, markdown=True):
        if 'USD10m' in text:
            self.validation_failure_count += 1
            self.failure_diagnostics.append({
                'source_sha256': hashlib.sha256(text.encode()).hexdigest(),
                'response_sha256': hashlib.sha256(b'PRIVATE_RESPONSE_USD11m').hexdigest(),
                'target_language': target,
                'quantities': quantity_failure_diagnostics(text, 'PRIVATE_RESPONSE USD11m.'),
                'raw_translation': 'PRIVATE_RESPONSE USD11m.', 'model_input': 'PRIVATE_INPUT',
            })
        return super().translate(text, target, source, markdown=markdown)


class SourceFallbackTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.corpus = make_corpus([
            document_from_html(url, html(url, body='<h1>Public research</h1><p>Revenue USD10m.</p><p>Further research.</p>'))
            for url in (HOME, BLOG)
        ])

    def run_build(self, translator, *, fallback=True, output='out', budget=30):
        return build(self.corpus, 'fr', self.root/output, self.root/'memo.json', translator,
                     allow_source_fallback=fallback, budget_seconds=budget)

    def test_bad_unit_keeps_exact_source_and_later_fields_and_pages_finish(self):
        result = self.run_build(RejectedQuantity())
        self.assertEqual(result['completed_page_count'], 2)
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertFalse(result['translation_complete'])
        self.assertEqual(result['source_fallback_unit_count'], 1)
        self.assertEqual(result['source_fallback_occurrences'], 2)
        self.assertEqual(result['failures'], [])
        page = (self.root/'out/fr/index.html').read_text()
        self.assertIn('Revenue USD10m.', page)
        self.assertIn('Texte traduit de référence.', page)
        self.assertIn('noindex,follow', page)
        verified_candidate(self.root/'out', self.corpus)
        checkpoint = json.loads((self.root/'memo.json').read_text())
        self.assertNotIn('Revenue USD10m.', [row['source'] for row in checkpoint['rows'].values()])
        self.assertEqual(len(checkpoint['source_fallbacks']), 1)
        checkpoint_is_valid(checkpoint, 'fr', self.corpus['documents_sha256'])

    def test_resume_reuses_source_fallback_without_new_inference(self):
        self.run_build(RejectedQuantity())
        translator = RejectedQuantity()
        result = self.run_build(translator, output='resumed')
        self.assertEqual(translator.calls, 0)
        self.assertEqual(result['completed_page_count'], 2)
        self.assertEqual(result['source_fallback_unit_count'], 1)

    def test_strict_mode_does_not_accept_a_source_fallback_checkpoint(self):
        self.run_build(RejectedQuantity())
        translator = RejectedQuantity()
        result = self.run_build(translator, fallback=False, output='strict')
        self.assertEqual(result['completed_page_count'], 0)
        # Shared rejected units are attempted once per run, not once per page.
        self.assertEqual(translator.calls, 1)

    def test_outer_quantity_rejection_never_renders_damaged_model_output(self):
        class Damaged(FakeTranslator):
            def translate(self, text, target, source=None, *, markdown=True):
                return text.replace('USD10m', 'EUR999m')
        result = self.run_build(Damaged())
        self.assertEqual(result['completed_page_count'], 2)
        self.assertNotIn('EUR999m', (self.root/'out/fr/index.html').read_text())
        self.assertNotIn('EUR999m', (self.root/'memo.json').read_text())

    def test_runtime_failure_and_budget_are_not_content_fallbacks(self):
        class RuntimeFailure(FakeTranslator):
            def translate(self, *args, **kwargs):
                raise OfflineTranslationError('Pinned runtime unavailable')
        result = self.run_build(RuntimeFailure())
        self.assertEqual(result['status'], 'incomplete-candidate')
        self.assertEqual(result['source_fallback_unit_count'], 0)
        result = self.run_build(RejectedQuantity(), output='timed', budget=-1)
        self.assertTrue(result['budget_exhausted'])
        self.assertEqual(result['completed_page_count'], 0)
        self.assertEqual(result['source_fallback_unit_count'], 0)

    def test_financial_sentence_is_not_split_at_commas(self):
        calls = []
        class Capture(FakeTranslator):
            def translate(self, text, target, source=None, *, markdown=True):
                calls.append(text)
                return text
        sentence = '收入为USD10m，同比增长5%，利润率8%。'
        document = document_from_html(HOME, html(body=f'<h1>Research</h1><p>{sentence}</p>'))
        memo = Memo(self.root/'memo.json', 'fr', Capture(), time.monotonic()+30, allow_source_fallback=True)
        translate_document(document, memo)
        self.assertIn(sentence, calls)
        self.assertNotIn('同比增长5%', calls)

    def test_cli_emits_only_bounded_hash_diagnostics_without_changing_fallback_or_candidate(self):
        source = self.root / 'corpus.json'; source.write_text(json.dumps(self.corpus))
        translator = DiagnosticRejectedQuantity()
        argv = ['builder', '--corpus', str(source), '--locale', 'fr',
                '--output', str(self.root / 'out'), '--checkpoint', str(self.root / 'memo.json'),
                '--allow-source-fallback']
        with patch('sys.argv', argv), patch.object(builder, 'require_actions'), \
             patch.dict(builder.os.environ, {'KC_PUBLIC_REPOSITORY': 'true'}), \
             patch.object(builder, 'OfflineTranslator', return_value=translator) as factory, \
             redirect_stdout(io.StringIO()) as output:
            self.assertEqual(builder.main(), 0)
        factory.assert_called_once_with(validation_attempts=1)
        summary = json.loads(output.getvalue())
        self.assertEqual(summary['source_fallback_unit_count'], 1)
        self.assertEqual(summary['source_fallback_occurrences'], 2)
        self.assertEqual(summary['completed_page_count'], 2)
        self.assertEqual(summary['terminal_validation_failure_count'], 1)
        self.assertFalse(summary['translation_diagnostics_truncated'])
        entry = summary['terminal_translation_diagnostics'][0]
        self.assertEqual(entry['failure_type'], 'offline-quantity-validation')
        self.assertEqual(entry['quantities']['missing']['type_counts'], {'currency': 1})
        self.assertEqual(entry['quantities']['extra']['type_counts'], {'currency': 1})
        self.assertNotEqual(entry['quantities']['source']['signature_sha256'],
                            entry['quantities']['response']['signature_sha256'])
        for forbidden in ('PRIVATE_', 'USD', '10000000', '11000000', 'Revenue', 'values'):
            self.assertNotIn(forbidden, output.getvalue())
        manifest = json.loads((self.root / 'out' / 'candidate-manifest.json').read_bytes())
        self.assertNotIn('terminal_translation_diagnostics', manifest)
        verified_candidate(self.root / 'out', self.corpus)
        # Reading public diagnostics causes no additional translations. Resume
        # retains the established source-fallback policy and also makes no calls.
        before = translator.calls
        public_translation_diagnostics(translator, 'fr')
        self.assertEqual(translator.calls, before)
        resumed = DiagnosticRejectedQuantity()
        self.run_build(resumed, output='resumed')
        self.assertEqual(resumed.calls, 0)
        self.assertEqual(public_translation_diagnostics(resumed, 'fr')['terminal_translation_diagnostics'], [])

    def test_public_diagnostics_cap_and_no_untrusted_type_or_failure_text(self):
        translator = DiagnosticRejectedQuantity(); self.run_build(translator)
        row = translator.failure_diagnostics[0]
        translator.failure_diagnostics = [copy.deepcopy(row) for _ in range(25)]
        translator.validation_failure_count = 100
        result = public_translation_diagnostics(translator, 'fr')
        self.assertEqual(len(result['terminal_translation_diagnostics']), 20)
        self.assertEqual(result['terminal_validation_failure_count'], 100)
        self.assertTrue(result['translation_diagnostics_truncated'])
        translator.failure_diagnostics = [copy.deepcopy(row)]
        item = translator.failure_diagnostics[0]
        item['failure_code'] = 'PRIVATE_ERROR'
        item['quantities']['source']['rows'][0]['kind'] = 'PRIVATE_UNIT'
        result = public_translation_diagnostics(translator, 'fr')
        entry = result['terminal_translation_diagnostics'][0]
        self.assertEqual(entry['failure_type'], 'offline-validation')
        self.assertIsNone(entry['quantities']['source'])
        self.assertNotIn('PRIVATE', json.dumps(result))
        item['quantities']['source']['rows'][0]['kind'] = []
        self.assertIsNone(public_translation_diagnostics(translator, 'fr')
                          ['terminal_translation_diagnostics'][0]['quantities']['source'])

    def test_diagnostic_hash_binds_numeric_values_without_printing_them(self):
        first = quantity_failure_diagnostics('USD 1234.5', 'USD 1235.5')['source']
        second = quantity_failure_diagnostics('USD 1235.5', 'USD 1235.5')['source']
        a, b = builder.public_quantity_signature(first), builder.public_quantity_signature(second)
        self.assertEqual(a['type_counts'], b['type_counts'])
        self.assertNotEqual(a['signature_sha256'], b['signature_sha256'])
        self.assertNotIn('1234', json.dumps(a))
        self.assertNotIn('USD', json.dumps(a))

    def test_invalid_hash_and_other_locale_are_not_reflected(self):
        translator = DiagnosticRejectedQuantity(); self.run_build(translator)
        row = translator.failure_diagnostics[0]
        for field, value in [('source_sha256', 'PRIVATE_SOURCE'), ('response_sha256', 'PRIVATE_RESPONSE'),
                             ('target_language', 'PRIVATE_LANGUAGE')]:
            translator.failure_diagnostics = [{**row, field: value}]
            result = public_translation_diagnostics(translator, 'fr')
            self.assertEqual(result['terminal_translation_diagnostics'], [])
            self.assertNotIn('PRIVATE', json.dumps(result))


class ExistingMirrorAssemblyTests(unittest.TestCase):
    def test_existing_mirrors_are_verified_without_additional_locale_url_helper(self):
        fixture = fixtures.AssemblyTests('test_dry_run_writes_nothing')
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        fixture.runbuild()
        root, _ = fixture.staging()
        (root/'ko').mkdir()
        (root/'ja').mkdir()
        (root/'ko/index.html').write_bytes(html(HOME+'ko/').replace(b'lang="en"', b'lang="ko"'))
        (root/'ja/index.html').write_bytes(html(HOME+'ja/', extra='<meta name="robots" content="noindex,follow">').replace(b'lang="en"', b'lang="ja"'))
        assemble(root, fixture.c, [fixture.base/'candidate'], ('fr',), apply=True, existing_locales=('ko', 'ja', 'ar'))
        parser = PublicParser(); parser.feed((root/'fr/index.html').read_text()); parser.close()
        self.assertEqual(parser.alternates['ko'], HOME+'ko/')
        self.assertNotIn('ja', parser.alternates)
        self.assertNotIn('ar', parser.alternates)


if __name__ == '__main__':
    unittest.main()
