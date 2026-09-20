#!/usr/bin/env python3
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import hymt_offline_translation as h

class Engine:
    def __init__(self, responder):
        self.responder = responder
        self.calls = []
    def translate(self, text, source, target):
        self.calls.append((text, source, target))
        return self.responder(text)

class HyMTTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
    def translator(self, responder):
        self.engine = Engine(responder)
        return h.OfflineTranslator(cache_dir=self.directory.name, engine_factory=lambda s,t: self.engine)
    def test_quantities_and_predicates_remain_in_complete_sentence(self):
        original = 'The operating margin increased by 2.5 percentage points to 18.5%.'
        translator = self.translator(lambda text: '营业利润率上升2.5个百分点，达到18.5%。')
        self.assertIn('18.5%', translator.translate(original, 'zh', 'en'))
        self.assertEqual(self.engine.calls, [(original, 'en', 'zh')])
    def test_equivalent_money_and_date_accepted(self):
        source = 'Cash reserves were USD 120 million on September 15, 2026.'
        translator = self.translator(lambda _: '2026年9月15日，现金储备为1.2亿美元。')
        translator.translate(source, 'zh', 'en')
        self.assertEqual(len(self.engine.calls), 1)
    def test_numeric_damage_is_not_cached(self):
        translator = self.translator(lambda _: '现金储备为120万美元。')
        with self.assertRaises(h.OfflineTranslationError):
            translator.translate('Cash reserves were USD 120 million.', 'zh', 'en')
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))
    def test_cache_is_exact_source_target_and_model(self):
        translator = self.translator(lambda _: '收入下降8.2%。')
        source = 'Revenue fell by 8.2%.'
        self.assertEqual(translator.translate(source, 'zh'), translator.translate(source, 'zh'))
        self.assertEqual(len(self.engine.calls), 1)
        self.assertEqual(translator.stats['cache_hits'], 1)
    def test_protected_links_code_and_placeholder_keep_sentence_context(self):
        source = 'See [the report](https://example.org/r.pdf) and `USD` for __KC_PH_000__.'
        translator = self.translator(lambda text: text.replace('See', '查看').replace('the report', '报告').replace('and', '和').replace('for', '对应'))
        result = translator.translate(source, 'zh', 'en')
        self.assertIn('[报告](https://example.org/r.pdf)', result)
        self.assertIn('`USD`', result)
        self.assertIn('__KC_PH_000__', result)
        self.assertEqual(len(self.engine.calls), 1)
    def test_placeholder_damage_rejected(self):
        translator = self.translator(lambda _: '收入增长。')
        with self.assertRaisesRegex(h.OfflineTranslationError, 'placeholder'):
            translator.translate('Revenue grew __KC_PH_000__.', 'zh', 'en')
    def test_markdown_fences_and_prefixes(self):
        translator = self.translator(lambda text: text.replace('Revenue', '收入'))
        source = '# Revenue\n\n```python\nrevenue = 12\n```\n\n| Revenue | 12 |\n| --- | --- |\n'
        output = translator.translate_markdown(source, 'zh', 'en')
        self.assertEqual(output, source.replace('# Revenue', '# 收入').replace('| Revenue', '| 收入'))
    def test_source_language_mixed_name(self):
        self.assertEqual(h._detect_source('The report from 中国银行 forecasts revenue growth in 2026.'), 'en')
    def test_no_local_inference(self):
        with mock.patch.dict(os.environ, {'GITHUB_ACTIONS': 'false'}):
            with self.assertRaisesRegex(h.OfflineTranslationError, 'restricted'):
                h._HyMTEngine(Path(self.directory.name))
    def test_long_sentence_rejected_not_split_inside_claim(self):
        with self.assertRaisesRegex(h.OfflineTranslationError, 'sentence'):
            h.split_sentences('word ' * 500)
        self.assertEqual(''.join(h.split_sentences(('A full sentence. ' * 200))), 'A full sentence. ' * 200)

if __name__ == '__main__':
    unittest.main()
