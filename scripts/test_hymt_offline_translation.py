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
        translator = self.translator(lambda text: '营业利润率上升__HYMTPH_0000__个百分点，达到__HYMTPH_0001__%。')
        self.assertIn('18.5%', translator.translate(original, 'zh', 'en'))
        self.assertEqual(self.engine.calls, [('The operating margin increased by __HYMTPH_0000__ percentage points to __HYMTPH_0001__%.', 'en', 'zh')])
    def test_equivalent_money_and_date_accepted(self):
        source = 'Cash reserves were USD 120 million on September 15, 2026.'
        translator = self.translator(lambda _: '__HYMTPH_0002__年9月__HYMTPH_0001__日，现金储备为__HYMTPH_0000__百万美元。')
        translator.translate(source, 'zh', 'en')
        self.assertEqual(len(self.engine.calls), 1)
    def test_numeric_damage_is_not_cached(self):
        translator = self.translator(lambda _: '现金储备为__HYMTPH_0000__万美元。')
        with self.assertRaises(h.OfflineTranslationError):
            translator.translate('Cash reserves were USD 120 million.', 'zh', 'en')
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))
    def test_cache_is_exact_source_target_and_model(self):
        translator = self.translator(lambda _: '收入下降__HYMTPH_0000__%。')
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
    def test_missing_controlled_term_placeholder_is_rejected_and_not_cached(self):
        translator = self.translator(lambda _: '영업 이익률은 23%이고 매출은 4.7% 감소했습니다.')
        with self.assertRaisesRegex(h.OfflineTranslationError, 'placeholder'):
            translator.translate('毛利率为23%，销售收入同比下降4.7%。', 'ko', 'zh')
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_masked_locale_distinguishes_gross_and_operating_margin(self):
        source = '毛利率为__KC_PH_000__，营业利润率为__KC_PH_001__。'
        translator = self.translator(lambda _: '__HYMTPH_0000__은 __KC_PH_000__, __HYMTPH_0001__은 __KC_PH_001__입니다.')
        result = translator.translate(source, 'ko', 'zh')
        self.assertIn('매출총이익률', result)
        self.assertIn('영업이익률', result)
        self.assertEqual(self.engine.calls[0][0], '__HYMTPH_0000__为__KC_PH_000__，__HYMTPH_0001__为__KC_PH_001__。')

    def test_glossary_works_for_arbitrary_english_gross_margin_sentence(self):
        source = 'Gross margin remained at 31%, while net profit margin was 7%.'
        h.validate_financial_terms(source, '매출총이익률은 31%를 유지했으며 순이익률은 7%였습니다.', 'ko')
        with self.assertRaises(h.OfflineTranslationError):
            h.validate_financial_terms(source, '영업이익률은 31%를 유지했으며 순이익률은 7%였습니다.', 'ko')

    def test_korean_wording_diagnostic_does_not_block_runtime_validation(self):
        source = 'Gross margin was 31%.'
        h.validate_result(source, '영업이익률은 31%였습니다.', 'en', 'ko')
        translator = self.translator(lambda _: '__HYMTPH_0000__ (영업이익률)은 __HYMTPH_0001__%입니다.')
        with mock.patch.object(h, 'validate_financial_terms', side_effect=AssertionError('Optional review must not block release')):
            first = translator.translate(source, 'ko', 'en')
            self.assertEqual(translator.translate(source, 'ko', 'en'), first)
        with self.assertRaisesRegex(h.OfflineTranslationError, 'quantity'):
            h.validate_result(source, '영업이익률은 32%였습니다.', 'en', 'ko')

    def test_engine_prompt_adds_concept_glossary_without_replacing_source(self):
        engine = object.__new__(h._HyMTEngine)
        engine.port = 1
        source = '毛利率为__KC_PH_000__。'
        response = {'choices': [{'finish_reason': 'stop', 'message': {'content': '매출총이익률은 __KC_PH_000__입니다.'}}]}
        with mock.patch.object(h, 'request_json', return_value=response) as request:
            engine.translate(source, 'zh', 'ko')
        prompt = request.call_args.args[2]['messages'][0]['content']
        self.assertIn('毛利率 = 매출총이익률', prompt)
        self.assertTrue(prompt.endswith(source))
        self.assertEqual(h.financial_glossary(source, 'ja'), '')

    def test_only_explicit_length_finish_is_content_failure(self):
        engine = object.__new__(h._HyMTEngine)
        engine.port = 1
        translator = h.OfflineTranslator(cache_dir=self.directory.name, engine_factory=lambda _s, _t: engine)
        for response, expected_error in (
            ({'choices': [{'finish_reason': 'length', 'message': {'content': '截断'}}]}, h.OfflineTranslationValidationError),
            ({'choices': [{'finish_reason': 'unknown', 'message': {'content': '异常'}}]}, h.OfflineTranslationError),
            ({'choices': [{'message': {'content': '异常'}}]}, h.OfflineTranslationError),
            ({'choices': []}, h.OfflineTranslationError),
        ):
            with self.subTest(response=response), mock.patch.object(h, 'request_json', return_value=response):
                with self.assertRaises(h.OfflineTranslationError) as caught:
                    translator.translate('Read the complete report.', 'zh', 'en')
                self.assertIs(type(caught.exception), expected_error)
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_controlled_nouns_leave_quantities_and_predicates_in_one_model_call(self):
        source = 'Gross margin remained at 31%, while operating profit increased by 7%.'
        translator = self.translator(lambda _: '__HYMTPH_0000__은 __HYMTPH_0002__%를 유지했으며 __HYMTPH_0001__은 __HYMTPH_0003__% 증가했습니다.')
        output = translator.translate(source, 'ko', 'en')
        self.assertIn('매출총이익률', output)
        self.assertIn('영업이익', output)
        self.assertEqual(self.engine.calls[0][0], '__HYMTPH_0000__ remained at __HYMTPH_0002__%, while __HYMTPH_0001__ increased by __HYMTPH_0003__%.')
        self.assertEqual(len(self.engine.calls), 1)

    def test_public_diagnostic_opt_in_retains_rejected_raw_without_caching(self):
        captured = []
        engine = Engine(lambda _: '잘못된 출력 100%')
        translator = h.OfflineTranslator(cache_dir=self.directory.name,
            engine_factory=lambda s,t: engine, diagnostic_callback=captured.append)
        with self.assertRaises(h.OfflineTranslationError):
            translator.translate('Gross margin was 31%.', 'ko', 'en')
        self.assertEqual(captured[0]['raw_translation'], '잘못된 출력 100%')
        self.assertEqual(captured[0]['model_input'], '__HYMTPH_0000__ was __HYMTPH_0001__%.')
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))
        self.assertIsNone(h.OfflineTranslator(cache_dir=self.directory.name)._diagnostic_callback)

    def test_report_image_marker_standalone_never_loads_model(self):
        translator = self.translator(lambda _: self.fail('Opaque-only marker must not reach the model'))
        source = '[[PORTAL_IMAGE_001]]\n'
        self.assertEqual(translator.translate_markdown(source, 'zh', 'en'), source)
        self.assertEqual(self.engine.calls, [])

    def test_report_image_marker_inline_is_protected_with_its_sentence(self):
        translator = self.translator(lambda text: text.replace('See', '参见').replace('for the chart', '中的图表'))
        source = 'See [[PORTAL_IMAGE_001]] for the chart.'
        output = translator.translate_markdown(source, 'zh', 'en')
        self.assertIn('[[PORTAL_IMAGE_001]]', output)
        self.assertEqual(self.engine.calls[0][0], 'See __HYMTPH_0000__ for the chart.')

    def test_relative_nested_and_reference_link_destinations_stay_exact(self):
        translator = self.translator(lambda text: text.replace('See', '参见').replace('report', '报告').replace('source', '来源'))
        source = 'See [report](../files/report_(v2).pdf) and [source][report-2026].'
        output = translator.translate_markdown(source, 'zh', 'en')
        self.assertIn('[报告](../files/report_(v2).pdf)', output)
        self.assertIn('[来源][report-2026]', output)
        self.assertNotIn('report_(v2)', self.engine.calls[0][0])

    def test_inline_raw_code_and_escaped_markdown_stay_exact(self):
        translator = self.translator(lambda text: text.replace('Read', '阅读').replace('and', '和'))
        source = r'Read <code>gross_margin = 23</code> and \*literal\*.'
        output = translator.translate(source, 'zh', 'en')
        self.assertIn('<code>gross_margin = 23</code>', output)
        self.assertIn(r'\*literal\*', output)
        self.assertNotIn('gross_margin', self.engine.calls[0][0])

    def test_link_delimiter_damage_is_rejected(self):
        translator = self.translator(lambda _: '参见[报告]__HYMTPH_0000__。')
        with self.assertRaisesRegex(h.OfflineTranslationError, 'destination boundary'):
            translator.translate('See [report](../report.pdf).', 'zh', 'en')

    def test_table_edge_pipes_restored_when_columns_and_money_are_intact(self):
        translator = self.translator(lambda _: '现金储备 | __HYMTPH_0000__百万美元')
        source = '| Cash reserves | USD 120 million |'
        self.assertEqual(translator.translate_markdown(source, 'zh', 'en'), '|现金储备 | 120百万美元|')
        self.assertEqual(self.engine.calls[0][0], '| Cash reserves | USD __HYMTPH_0000__ million |')

    def test_table_interior_separator_loss_or_added_column_is_rejected(self):
        for output in ('现金储备 __HYMTPH_0000__百万美元', '现金储备 | 新增 | __HYMTPH_0000__百万美元'):
            with self.subTest(output=output):
                translator = self.translator(lambda _, output=output: output)
                with self.assertRaisesRegex(h.OfflineTranslationError, 'Markdown structure'):
                    translator.translate_markdown('| Cash reserves | USD 120 million |', 'zh', 'en')

    def test_table_edges_do_not_hide_quantity_damage(self):
        translator = self.translator(lambda _: '现金储备 | __HYMTPH_0000__万美元')
        with self.assertRaisesRegex(h.OfflineTranslationError, 'quantity'):
            translator.translate_markdown('| Cash reserves | USD 120 million |', 'zh', 'en')

    def test_numeric_lock_covers_digits_adjacent_to_cjk_units(self):
        masked, replacements, _terms = h._mask('截至2024年9月，收入增长12.5%，投资1.2亿美元。', 'fr')
        self.assertEqual(masked, '截至__HYMTPH_0000__年__HYMTPH_0001__月，收入增长__HYMTPH_0002__%，投资__HYMTPH_0003__亿美元。')
        self.assertEqual(list(replacements.values()), ['2024', '9', '12.5', '1.2'])

    def test_plain_filename_punctuation_is_not_markdown_but_claims_remain_checked(self):
        translator = self.translator(lambda _: '短期增长__HYMTPH_0000__%')
        source = 'Short~term_growth 12.5%'
        self.assertEqual(translator.translate(source, 'zh', 'en', markdown=False), '短期增长12.5%')
        self.assertEqual(len(self.engine.calls), 1)
        # Plain text cache must never bypass validation for a Markdown caller.
        with self.assertRaisesRegex(h.OfflineTranslationError, 'Markdown structure'):
            translator.translate(source, 'zh', 'en')
        self.assertEqual(len(self.engine.calls), 2)
        with self.assertRaisesRegex(h.OfflineTranslationError, 'quantity'):
            h.validate_result(source, '短期增长125%', 'en', 'zh', markdown=False)
        with self.assertRaisesRegex(h.OfflineTranslationError, 'placeholder'):
            h.validate_result(source + '__KC_PH_0000__', '短期增长12.5%', 'en', 'zh', markdown=False)

    def test_real_catalog_plan_regression_keeps_ordinal_and_fic_in_one_model_request(self):
        source = ('JPM-China Healthcare New _15th Five~Year” Healthcare Industry Plan Targets Increased '
                  'FIC Innovation，AI Applications and Global Competitiveness__KC_PH_0000__')
        # This exact rejected output occurred on Ubuntu 22.04 and 24.04 in
        # production-adapter preflight 35572961434. Never accept its changed plan.
        damaged = 'JPM-中国医疗保健“十四五”规划目标：提升医疗创新、人工智能应用及全球竞争力__KC_PH_0000__'
        with self.assertRaisesRegex(h.OfflineTranslationError, 'quantity'):
            h.validate_result(source, damaged, 'en', 'zh', markdown=False)
        translator = self.translator(lambda _: 'JPM-中国医疗：新__HYMTPH_0000__行业规划旨在加强'
                                     '__HYMTPH_0001__、人工智能应用和全球竞争力__KC_PH_0000__')
        output = translator.translate(source, 'zh', 'en', markdown=False)
        self.assertIn('第15个五年', output)
        self.assertIn('FIC创新', output)
        self.assertEqual(len(self.engine.calls), 1)
        model_input = self.engine.calls[0][0]
        self.assertIn('New ___HYMTPH_0000__” Healthcare Industry Plan Targets Increased __HYMTPH_0001__', model_input)
        self.assertIn('AI Applications and Global Competitiveness', model_input)

    def test_planning_term_ordinal_and_numeric_claims_are_locked(self):
        source = 'The 16th Five-Year Plan forecasts revenue growth of 12.5% and USD 120 million investment.'
        masked, _resources, terms = h._mask(source, 'zh')
        self.assertEqual(terms, {'__HYMTPH_0000__': '第16个五年'})
        self.assertIn('__HYMTPH_0001__%', masked)
        self.assertIn('USD __HYMTPH_0002__ million', masked)
        for output, error in [
            ('第15个五年计划预计收入增长12.5%，投资1.2亿美元。', 'placeholder'),
            ('__HYMTPH_0000__计划预计收入增长__HYMTPH_0001__%，投资__HYMTPH_0002__万美元。', 'quantity'),
        ]:
            with self.subTest(output=output):
                translator = self.translator(lambda _, output=output: output)
                with self.assertRaisesRegex(h.OfflineTranslationError, error):
                    translator.translate(source, 'zh', 'en', markdown=False)
        translator = self.translator(lambda _: '__HYMTPH_0000__计划预计收入增长__HYMTPH_0001__%，投资__HYMTPH_0002__百万美元。')
        output = translator.translate(source, 'zh', 'en', markdown=False)
        self.assertIn('第16个五年', output)
        self.assertIn('12.5%', output)
        self.assertIn('120百万美元', output)
        self.assertEqual(len(list(Path(self.directory.name).rglob('*.json'))), 1)

    def test_controlled_period_next_to_markdown_underscores_keeps_emphasis(self):
        translator = self.translator(lambda _: '___HYMTPH_0000___规划')
        self.assertEqual(translator.translate('_15th Five-Year_ plan', 'zh', 'en'), '_第15个五年_规划')

    def test_opted_in_markdown_fallback_preserves_bad_units_and_translates_neighbors(self):
        cash = '- Cash reserves were USD 120 million; see [source](../2026/report.pdf).\r\n'
        figure = '> See [[PORTAL_IMAGE_001]] for the chart.\r\n'
        source = '# Revenue\r\n\r\n' + cash + figure + 'Revenue grew 12.5%.\r\n'
        def respond(text):
            if text.startswith('Cash reserves'):
                return '现金储备为__HYMTPH_0001__万美元；参见[source](__HYMTPH_0000__)。'
            if text.startswith('See '):
                return '参见图表。'
            return text.replace('Revenue grew', '收入增长').replace('Revenue', '收入')
        translator = self.translator(respond)
        events = []
        result = translator.translate_markdown(source, 'zh', 'en', source_fallback=events.append)
        self.assertIn(cash, result)
        self.assertIn(figure, result)
        self.assertIn('# 收入\r\n', result)
        self.assertIn('收入增长 12.5%.\r\n', result)
        self.assertEqual([row['line'] for row in events], [3, 4])
        self.assertEqual(events[0]['source_sha256'], h.hashlib.sha256(cash.encode()).hexdigest())
        self.assertIn('quantity', events[0]['reason'])
        self.assertIn('placeholder', events[1]['reason'])
        self.assertEqual(len(list(Path(self.directory.name).rglob('*.json'))), 2)
        self.assertEqual(len(self.engine.calls), 4)
        translator.translate_markdown(source, 'zh', 'en', source_fallback=events.append)
        self.assertEqual(len(self.engine.calls), 6)  # Only rejected units retried.
        self.assertEqual(len(list(Path(self.directory.name).rglob('*.json'))), 2)
        with self.assertRaises(h.OfflineTranslationValidationError):
            translator.translate_markdown(source, 'zh', 'en')

    def test_markdown_fallback_does_not_swallow_runtime_transport_or_programming_errors(self):
        for error in (h.OfflineTranslationError('Missing model provenance'),
                      OSError('transport failed'), TypeError('programming failure')):
            with self.subTest(error=error):
                def fail(_text, error=error):
                    raise error
                translator = self.translator(fail)
                events = []
                with self.assertRaises(h.OfflineTranslationError) as caught:
                    translator.translate_markdown('Revenue grew 12.5%.\n', 'zh', 'en', source_fallback=events.append)
                self.assertNotIsInstance(caught.exception, h.OfflineTranslationValidationError)
                self.assertEqual(events, [])
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_diagnostic_write_failure_still_stops_report_fallback(self):
        translator = self.translator(lambda _: '收入增长__HYMTPH_0000__')
        def failed_diagnostics(_event):
            raise OSError('diagnostic checkpoint write failed')
        with self.assertRaisesRegex(OSError, 'checkpoint write failed'):
            translator.translate_markdown('Revenue grew 12.5%.\n', 'zh', 'en', source_fallback=failed_diagnostics)
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

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
