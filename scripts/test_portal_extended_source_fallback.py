"""Source fallback contracts: synthetic responses only, no local model calls."""
import json
from pathlib import Path
import tempfile
import time
import unittest

from build_portal_extended_locales import Memo, build, translate_document
from hymt_offline_translation import OfflineTranslationError, OfflineTranslationValidationError
from portal_extended_locales import PublicParser, document_from_html, make_corpus
from assemble_portal_extended_locales import assemble, verified_candidate
import test_portal_extended_locales as fixtures
from test_portal_extended_locales import FakeTranslator, HOME, BLOG, html
from portal_extended_r2 import checkpoint_is_valid


class RejectedQuantity(FakeTranslator):
    def translate(self, text, target, source=None, *, markdown=True):
        self.calls += 1
        if 'USD10m' in text:
            # Simulates a completed response rejected by the inner model gate.
            raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed')
        return text


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
        return build(self.corpus, 'en', self.root/output, self.root/'memo.json', translator,
                     allow_source_fallback=fallback, budget_seconds=budget)

    def test_bad_unit_keeps_exact_source_and_later_fields_and_pages_finish(self):
        result = self.run_build(RejectedQuantity())
        self.assertEqual(result['completed_page_count'], 2)
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertFalse(result['translation_complete'])
        self.assertEqual(result['source_fallback_unit_count'], 1)
        self.assertEqual(result['source_fallback_occurrences'], 2)
        self.assertEqual(result['failures'], [])
        page = (self.root/'out/en/index.html').read_text()
        self.assertIn('Revenue USD10m.', page)
        self.assertIn('Further research.', page)
        self.assertIn('noindex,follow', page)
        verified_candidate(self.root/'out', self.corpus)
        checkpoint = json.loads((self.root/'memo.json').read_text())
        self.assertNotIn('Revenue USD10m.', [row['source'] for row in checkpoint['rows'].values()])
        self.assertEqual(len(checkpoint['source_fallbacks']), 1)
        checkpoint_is_valid(checkpoint, 'en', self.corpus['documents_sha256'])

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
        self.assertNotIn('EUR999m', (self.root/'out/en/index.html').read_text())
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
        memo = Memo(self.root/'memo.json', 'en', Capture(), time.monotonic()+30, allow_source_fallback=True)
        translate_document(document, memo)
        self.assertIn(sentence, calls)
        self.assertNotIn('同比增长5%', calls)


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
        assemble(root, fixture.c, [fixture.base/'candidate'], ('en',), apply=True, existing_locales=('ko', 'ja', 'ar'))
        parser = PublicParser(); parser.feed((root/'en/index.html').read_text()); parser.close()
        self.assertEqual(parser.alternates['ko'], HOME+'ko/')
        self.assertNotIn('ja', parser.alternates)
        self.assertNotIn('ar', parser.alternates)


if __name__ == '__main__':
    unittest.main()
