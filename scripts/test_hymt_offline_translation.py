#!/usr/bin/env python3
import os
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest import mock
import hymt_offline_translation as h

COMMA_LOCALES = ('fr', 'es', 'de', 'id', 'pt', 'tr', 'ru', 'it', 'vi', 'pl', 'cs', 'nl', 'uk', 'kk')
SPACE_GROUP_LOCALES = {'fr', 'ru', 'pl', 'cs', 'uk', 'kk'}

def comma_response(locale):
    return {'ru': 'Рост 0,125%.', 'uk': 'Ріст 0,125%.', 'kk': 'Өсім 0,125%.'}.get(locale, 'Ratio 0,125%.')

class Engine:
    def __init__(self, responder):
        self.responder = responder
        self.calls = []
    def translate(self, text, source, target):
        self.calls.append((text, source, target))
        return self.responder(text)


class RetryingEngine(h._HyMTEngine):
    def __init__(self, responder):
        self.responder = responder
        self.calls = []

    def translate(self, text, source, target, *, quality_retry=0):
        self.calls.append((text, source, target, quality_retry))
        return self.responder(text, quality_retry)

class HyMTTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
    def translator(self, responder):
        self.engine = Engine(responder)
        return h.OfflineTranslator(cache_dir=self.directory.name, engine_factory=lambda s,t: self.engine)

    def retrying_translator(self, responder):
        self.engine = RetryingEngine(responder)
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

    def test_advisory_numeric_difference_is_cached_without_retry_or_fallback(self):
        engine = RetryingEngine(lambda _text, _attempt: 'Le revenu augmente de 125%.')
        translator = h.OfflineTranslator(cache_dir=self.directory.name,
            engine_factory=lambda *_: engine, quantity_policy='advisory')
        source = 'Revenue grew 12.5%.'
        for _ in range(2):
            self.assertEqual(translator.translate(source, 'fr', 'en'), 'Le revenu augmente de 125%.')
        self.assertEqual(len(engine.calls), 1)
        self.assertEqual(translator.stats['cache_hits'], 1)
        self.assertEqual(translator.validation_failure_count, 0)
        self.assertEqual(translator.failure_diagnostics, [])
        self.assertEqual(translator.quantity_warning_count, 2)
        warnings = translator.quantity_warning_diagnostics
        self.assertEqual(warnings[0]['codes'], ['financial_quantity_changed_missing_or_added'])
        self.assertEqual(set(warnings[0]), {'source_sha256', 'target_language', 'codes'})
        self.assertNotIn('125', json.dumps(warnings))
        row = json.loads(next(Path(self.directory.name).rglob('*.json')).read_text())
        self.assertEqual(row['quantity_policy'], 'advisory')

    def test_advisory_reuses_existing_strict_cache_without_inference(self):
        strict = self.translator(lambda _: 'Le revenu augmente de 12,5%.')
        source = 'Revenue grew 12.5%.'
        expected = strict.translate(source, 'fr', 'en')
        # Legacy cache rows did not persist a quantity_policy field.
        path = next(Path(self.directory.name).rglob('*.json'))
        row = json.loads(path.read_text()); row.pop('quantity_policy')
        path.write_text(json.dumps(row))
        original = path.read_bytes()
        advisory = h.OfflineTranslator(cache_dir=self.directory.name, quantity_policy='advisory',
            engine_factory=mock.Mock(side_effect=AssertionError('Existing cache must avoid inference')))
        self.assertEqual(advisory.translate(source, 'fr', 'en'), expected)
        self.assertEqual(advisory.quantity_warning_count, 0)
        self.assertEqual(path.read_bytes(), original)

    def test_advisory_cache_does_not_bypass_strict_report_validation(self):
        advisory = h.OfflineTranslator(cache_dir=self.directory.name, quantity_policy='advisory',
            engine_factory=lambda *_: Engine(lambda _: 'Le revenu augmente de 125%.'))
        source = 'Revenue grew 12.5%.'
        advisory.translate(source, 'fr', 'en')
        path = next(Path(self.directory.name).rglob('*.json'))
        original = path.read_bytes()
        strict = h.OfflineTranslator(cache_dir=self.directory.name,
            engine_factory=mock.Mock(side_effect=AssertionError('Strict cache validation must not call model')))
        with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'quantity'):
            strict.translate(source, 'fr', 'en')
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(strict.quantity_warning_count, 0)

    def test_advisory_preserves_structural_unicode_and_language_checks(self):
        for source, response, reason, markdown in (
            ('Read __KC_PH_000__ at 12.5%.', 'Lire 125%.', 'placeholder', True),
            ('Read [report](../report.pdf) at 12.5%.', 'Lire [rapport]__HYMTPH_0000__ à 125%.', 'destination boundary', True),
            ('Read **report** at 12.5%.', 'Lire rapport à 125%.', 'Markdown structure', True),
            ('Revenue | 12.5%', 'Revenu 125%', 'Markdown structure', False),
            ('Revenue grew 12.5%.', 'Revenu \ufffd 125%.', 'Unicode', True),
            ('Revenue grew 12.5%.', '', 'Empty', True),
            ('Revenue grew 12.5%.', '收入125%。', 'target script', True),
        ):
            with self.subTest(reason=reason), tempfile.TemporaryDirectory() as directory:
                engine = RetryingEngine(lambda _text, _attempt: response)
                translator = h.OfflineTranslator(cache_dir=directory, quantity_policy='advisory',
                    engine_factory=lambda *_: engine)
                with self.assertRaisesRegex(h.OfflineTranslationValidationError, reason):
                    translator.translate(source, 'fr', 'en', markdown=markdown)
                self.assertEqual(len(engine.calls), 3)
                self.assertFalse(list(Path(directory).rglob('*.json')))
                self.assertEqual(translator.quantity_warning_count, 0)

    def test_advisory_diagnostics_are_bounded_and_parser_errors_do_not_retry(self):
        engine = RetryingEngine(lambda _text, _attempt: 'Le revenu augmente de 125%.')
        translator = h.OfflineTranslator(cache_dir=self.directory.name, quantity_policy='advisory',
            engine_factory=lambda *_: engine)
        diagnostic_errors = [ValueError, ArithmeticError, TypeError, RuntimeError, OSError]
        with mock.patch.object(h, 'quantity_issues',
                               side_effect=[diagnostic_errors[index % len(diagnostic_errors)]('private quantity contents')
                                            for index in range(25)]):
            for _ in range(25):
                self.assertEqual(translator.translate('Revenue grew 12.5%.', 'fr', 'en'),
                                 'Le revenu augmente de 125%.')
        self.assertEqual(len(engine.calls), 1)
        self.assertEqual(translator.quantity_warning_count, 25)
        self.assertEqual(len(translator.quantity_warning_diagnostics), 20)
        self.assertEqual(translator.quantity_warning_diagnostics[0]['codes'], ['quantity_diagnostic_unavailable'])
        self.assertNotIn('private', json.dumps(translator.quantity_warning_diagnostics))

    def test_quantity_policy_requires_explicit_supported_value(self):
        for policy in ('ignore', '', None, 1):
            with self.subTest(policy=policy), self.assertRaises(ValueError):
                h.OfflineTranslator(cache_dir=self.directory.name, quantity_policy=policy)

    def test_advisory_site_numeric_tokens_may_be_omitted_but_resources_remain_exact(self):
        source = 'Read __KC_PH_000__ at __KC_PH_001__.'
        engine = RetryingEngine(lambda _text, _attempt: 'Lire __KC_PH_000__.')
        translator = h.OfflineTranslator(cache_dir=self.directory.name, quantity_policy='advisory',
            engine_factory=lambda *_: engine)
        for _ in range(2):
            self.assertEqual(translator.translate_site_text(source, 'fr', data_placeholders=('__KC_PH_001__',)),
                             'Lire __KC_PH_000__.')
        self.assertEqual(len(engine.calls), 1)
        self.assertEqual(translator.quantity_warning_count, 2)
        self.assertIn('numeric_data_placeholder_changed', translator.quantity_warning_diagnostics[0]['codes'])
        # The same cache row cannot excuse an omitted resource for another caller.
        with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'placeholder'):
            translator.translate_site_text(source, 'fr')
        self.assertEqual(len(engine.calls), 4)  # Existing bounded structural retry remains.
        strict = h.OfflineTranslator(cache_dir=self.directory.name)
        with self.assertRaisesRegex(ValueError, 'advisory'):
            strict.translate_site_text(source, 'fr', data_placeholders=('__KC_PH_001__',))

    def test_advisory_optional_numbers_do_not_allow_new_tokens_or_missing_resources(self):
        for response in ('Lire __KC_PH_001__.', 'Lire __KC_PH_000__ __KC_PH_999__.' ):
            with self.subTest(response=response), tempfile.TemporaryDirectory() as directory:
                translator = h.OfflineTranslator(cache_dir=directory, quantity_policy='advisory',
                    engine_factory=lambda *_: Engine(lambda _: response))
                with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'placeholder'):
                    translator.translate_site_text('Read __KC_PH_000__ at __KC_PH_001__.', 'fr',
                                                   data_placeholders=('__KC_PH_001__',))
                self.assertFalse(list(Path(directory).rglob('*.json')))

    def test_advisory_numeric_token_allowlist_cannot_skip_resource_destination_shape(self):
        translator = h.OfflineTranslator(cache_dir=self.directory.name, quantity_policy='advisory',
            engine_factory=lambda *_: Engine(lambda _: 'Lire [rapport]().'))
        with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'placeholder|destination boundary'):
            translator.translate_site_text('Read [report](__KC_PH_000__).', 'fr',
                                           data_placeholders=('__KC_PH_000__',))
        for placeholders in (('__HYMTPH_0000__',), ('__KC_PH_999__',), ['__KC_PH_000__']):
            with self.subTest(placeholders=placeholders), self.assertRaises(ValueError):
                translator.translate_site_text('Read __KC_PH_000__.', 'fr', data_placeholders=placeholders)

    def test_locale_decimal_validation_precedes_cache_and_preserves_equivalent_result(self):
        for locale in COMMA_LOCALES:
            for source, accepted in (('Rate 0.125%.', True), ('Rate 125%.', False)):
                with self.subTest(locale=locale, source=source), tempfile.TemporaryDirectory() as cache:
                    engine = Engine(lambda _: comma_response(locale))
                    translator = h.OfflineTranslator(cache_dir=cache, engine_factory=lambda *_: engine)
                    if accepted:
                        self.assertEqual(translator.translate(source, locale, 'en'), comma_response(locale))
                        self.assertEqual(translator.translate(source, locale, 'en'), comma_response(locale))
                        self.assertTrue(list(Path(cache).rglob('*.json')))
                    else:
                        with self.assertRaises(h.OfflineTranslationValidationError):
                            translator.translate(source, locale, 'en')
                        self.assertFalse(list(Path(cache).rglob('*.json')))
                        facts = translator.failure_diagnostics[0]['quantities']
                        self.assertEqual(facts['missing']['rows'],
                                         [{'kind': 'percent', 'values': ['125'], 'count': 1}])
                        self.assertEqual(facts['extra']['rows'],
                                         [{'kind': 'percent', 'values': ['0.125'], 'count': 1}])
                    self.assertEqual(len(engine.calls), 1)

    def test_locale_quantity_diagnostic_matches_grouping_and_malformed_gate(self):
        for locale in COMMA_LOCALES:
            response = 'USD 1\u202f234,567' if locale in SPACE_GROUP_LOCALES else 'USD 1.234,567'
            facts = h.quantity_failure_diagnostics('USD 1234.567', response, 'en', locale)
            self.assertEqual(facts['missing']['rows'], [])
            self.assertEqual(facts['extra']['rows'], [])
            malformed = 'USD 1.234,5,6'
            with self.assertRaises(h.OfflineTranslationValidationError):
                h.validate_result('USD 1234.56', malformed, 'en', locale)
            facts = h.quantity_failure_diagnostics('USD 1234.56', malformed, 'en', locale)
            self.assertEqual(facts['extra']['rows'],
                             [{'kind': 'invalid_number', 'values': [], 'count': 1}])

    def test_existing_same_model_cache_cannot_bypass_new_locale_quantity_gate(self):
        for locale in COMMA_LOCALES:
            for source, accepted in (('Rate 0.125%.', True), ('Rate 125%.', False)):
                with self.subTest(locale=locale, source=source), tempfile.TemporaryDirectory() as cache:
                    engine_factory = mock.Mock(side_effect=AssertionError('Cached validation must not call a model'))
                    translator = h.OfflineTranslator(cache_dir=cache, engine_factory=engine_factory)
                    identity, path = translator._memo_identity(source, locale, 'en', markdown=True)
                    path.parent.mkdir(parents=True)
                    h.atomic_json(path, {**identity, 'translation': comma_response(locale)})
                    before = path.read_bytes()
                    if accepted:
                        self.assertEqual(translator.translate(source, locale, 'en'), comma_response(locale))
                    else:
                        with self.assertRaises(h.OfflineTranslationValidationError):
                            translator.translate(source, locale, 'en')
                    engine_factory.assert_not_called()
                    self.assertEqual(path.read_bytes(), before)

    def test_indian_grouping_cache_revalidates_whole_values_without_inference(self):
        for locale, word in {'hi':'आय', 'gu':'આવક', 'te':'ఆదాయం',
                             'mr':'उत्पन्न', 'bn':'আয়', 'ta':'வருவாய்'}.items():
            for source, accepted in (('Value 1234567.89.', True), ('Value 12.34; 567.89.', False)):
                with self.subTest(locale=locale, source=source), tempfile.TemporaryDirectory() as cache:
                    engine_factory = mock.Mock(side_effect=AssertionError('Cached validation must not call a model'))
                    translator = h.OfflineTranslator(cache_dir=cache, engine_factory=engine_factory)
                    identity, path = translator._memo_identity(source, locale, 'en', markdown=True)
                    path.parent.mkdir(parents=True)
                    translated = word + ' 12,34,567.89.'
                    h.atomic_json(path, {**identity, 'translation': translated})
                    before = path.read_bytes()
                    if accepted:
                        self.assertEqual(translator.translate(source, locale, 'en'), translated)
                    else:
                        with self.assertRaises(h.OfflineTranslationValidationError):
                            translator.translate(source, locale, 'en')
                    engine_factory.assert_not_called()
                    self.assertEqual(path.read_bytes(), before)

    def test_pinned_engine_retries_target_script_and_materialized_quantities(self):
        source = 'Margin rose 2.5 percentage points.'

        def respond(text, retry):
            if retry < 2:
                return 'The margin rose 2.5 percentage points.'
            self.assertIn('__HYMTPH_0000__', text)
            return 'मार्जिन __HYMTPH_0000__ बढ़ा।'

        translator = self.retrying_translator(respond)
        self.assertEqual(translator.translate(source, 'hi', 'en'), 'मार्जिन 2.5 percentage points बढ़ा।')
        self.assertEqual([row[3] for row in self.engine.calls], [0, 1, 2])

    def test_terminal_placeholder_failure_reports_only_bounded_counts_and_hashes(self):
        source = '私有源文`a`与`b`。'
        def respond(value, attempt):
            if attempt < 2: return 'Private rejected response with changed quantities.'
            return 'Private rejected response __HYMTPH_0000__ __HYMTPH_0000__.'
        translator = self.retrying_translator(respond)
        with self.assertRaises(h.OfflineTranslationValidationError):
            translator.translate(source, 'en', 'zh')
        self.assertEqual(len(self.engine.calls), 3)
        self.assertEqual(translator.validation_failure_count, 1)
        self.assertEqual(len(translator.failure_diagnostics), 1)
        row = translator.failure_diagnostics[0]
        self.assertEqual(row['source_sha256'], h.hashlib.sha256(source.encode()).hexdigest())
        self.assertEqual(row['quality_retry'], 2)
        self.assertEqual(row['placeholders']['expected'], 2)
        self.assertEqual(row['placeholders']['canonical'],
                         {'found': 2, 'missing': 1, 'extra': 1, 'duplicate_expected': 1})
        self.assertEqual(len(row['placeholders']['missing_token_sha256']), 1)
        rendered = json.dumps(row, ensure_ascii=False)
        for private in (source, 'Private rejected response', '__HYMTPH_0000__', '__HYMTPH_0001__'):
            self.assertNotIn(private, rendered)
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))
        for number in range(21):
            with self.assertRaises(h.OfflineTranslationValidationError):
                translator.translate(source + str(number), 'en', 'zh')
        self.assertEqual(translator.validation_failure_count, 22)
        self.assertEqual(len(translator.failure_diagnostics), 20)
        self.assertEqual(len(self.engine.calls), 66)

    def test_final_english_prompt_names_actual_complete_facts_without_template_tokens(self):
        engine = object.__new__(h._HyMTEngine); engine.port = 12345
        source = '投资 __HYMTPH_0000__，参见 __KC_PH_0001__ 与 __KC_PH_0001__。'
        response = {'choices': [{'finish_reason': 'stop', 'message': {'content': 'translation'}}]}
        with mock.patch.object(h, 'request_json', return_value=response) as request:
            engine.translate(source, 'zh', 'en', quality_retry=2)
        payload = request.call_args.args[2]; prompt = payload['messages'][0]['content']
        self.assertEqual(engine.last_request_sha256, h.hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest())
        instruction, actual = prompt.rsplit('\n', 1)
        self.assertEqual(actual, source)
        self.assertIn('__HYMTPH_0000__: 1 occurrence(s)', instruction)
        self.assertIn('__KC_PH_0001__: 2 occurrence(s)', instruction)
        self.assertIn('complete financial quantity', instruction)
        self.assertNotIn('__HYMTPH_...__', instruction)
        self.assertNotIn('__KC_PH_...__', instruction)
        self.assertNotIn('previous draft', instruction)
        self.assertEqual(payload['seed'], int(h.MANIFEST['sampling'].get('seed', 0)) + 2)
        self.assertEqual(payload['grammar'], h.UNICODE_TEXT_GRAMMAR)
        self.assertEqual(request.call_count, 1)
        for target, retry, text in [('en', 0, source), ('en', 1, source), ('ar', 2, source),
                                    ('en', 2, '普通标题')]:
            with self.subTest(target=target, retry=retry), mock.patch.object(h, 'request_json', return_value=response) as request:
                engine.translate(text, 'zh', target, quality_retry=retry)
                prompt = request.call_args.args[2]['messages'][0]['content']
                self.assertNotIn('These exact tokens must appear', prompt)
                self.assertTrue(prompt.endswith(text))
                if target == 'en' and retry == 2:
                    self.assertNotIn('HYMTPH', prompt)
                    self.assertNotIn('KC_PH', prompt)

    def test_placeholder_diagnostics_describe_format_damage_without_repairing_it(self):
        original = '__HYMTPH_0000__ and __HYMTPH_0001__'
        raw = r'__ HYMTPH_0000 __ and \_\_HYMTPH\_0001\_\_'
        result = h.placeholder_diagnostics(original, raw)
        self.assertEqual(result['canonical']['missing'], 2)
        self.assertEqual(result['no_whitespace']['missing'], 1)
        self.assertEqual(result['markdown_unescaped'],
                         {'found': 2, 'missing': 0, 'extra': 0, 'duplicate_expected': 0})
        with self.assertRaises(h.OfflineTranslationValidationError):
            h.validate_result(original, raw, 'zh', 'en')
        self.assertEqual(h.placeholder_diagnostics(original, None),
                         {'expected': 2, 'response_available': False})
        many = h.placeholder_diagnostics(' '.join(f'__KC_PH_{n:04d}__' for n in range(30)), '')
        self.assertEqual(len(many['missing_token_sha256']), 20)
        self.assertTrue(many['missing_tokens_truncated'])

    def test_english_final_retry_materializes_complete_source_facts_without_han(self):
        cases = [
            ('第三季度订单观察', 'Q3'),
            ('一季度增长8%，四季度增长2%。', 'Q1|8%|Q4|2%'),
            ('预期Q1增长三成。', 'Q1|30%'),
            ('投资金额为150亿欧元。', 'EUR 15,000,000,000'),
            ('预期2Q增长10%。', 'Q2|10%'),
            ('2026年下半年投资1.2亿美元。', 'H2 2026|USD 120,000,000'),
        ]
        from financial_quantity_integrity import quantity_issues
        from portal_english_commentary import text as english_text
        for source, expected in cases:
            with self.subTest(source=source):
                masked, facts = h._mask_quantity_facts(source, 0, target='en')
                self.assertEqual(list(facts.values()), expected.split('|'))
                self.assertFalse(h.quantities(masked))
                self.assertEqual(quantity_issues(source, ' and '.join(facts.values())), [])
                def respond(value, attempt):
                    if attempt < 2: return 'The outlook is unchanged.'
                    self.assertFalse(h._PLACEHOLDERS.findall(value))
                    self.assertEqual(quantity_issues(source, value), [])
                    for fact in expected.split('|'): self.assertIn(fact, value)
                    return 'Outlook: ' + ' and '.join(expected.split('|')) + '.'
                translator = self.retrying_translator(respond)
                translated = translator.translate(source, 'en', 'zh')
                self.assertEqual(quantity_issues(source, translated), [])
                english_text(translated, 12000, english=True)
                self.assertEqual(len(self.engine.calls), 3)
                self.assertEqual(self.engine.calls[0][0], source)
                self.assertEqual(self.engine.calls[1][0], source)
                self.assertEqual(translator.translate(source, 'en', 'zh'), translated)
                self.assertEqual(len(self.engine.calls), 3)

    def test_english_currency_grouping_preserves_decimal_sign_and_fraction(self):
        for source, expected in (
            ('150亿欧元', 'EUR 15,000,000,000'),
            ('EUR -12345.67', 'EUR -12,345.67'),
            ('USD 1000.00001', 'USD 1,000.00001'),
            ('GBP 1234567.8900', 'GBP 1,234,567.89'),
            ('USD 0.125', 'USD 0.125'),
        ):
            with self.subTest(source=source):
                self.assertEqual(h._english_quantity_fact(source), expected)
                self.assertEqual(h.quantities(source), h.quantities(expected))
        self.assertEqual(h._english_quantity_fact('三成'), '30%')
        self.assertEqual(h._english_quantity_fact('第三季度'), 'Q3')

    def test_grouped_currency_retry_still_rejects_observed_invented_percent(self):
        source = '企业投资150亿欧元，并重视长期回报。'
        def respond(value, attempt):
            if attempt == 2:
                self.assertIn('EUR 15,000,000,000', value)
            return 'The company invests EUR 15 billion with a return of 30%.'
        translator = self.retrying_translator(respond)
        with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'quantity'):
            translator.translate(source, 'en', 'zh', markdown=False)
        self.assertEqual(len(self.engine.calls), 3)
        self.assertEqual(self.engine.calls[0][0], source)
        self.assertEqual(self.engine.calls[1][0], source)
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))
        self.assertEqual(translator.failure_diagnostics[0]['quantities']['extra']['rows'],
                         [{'kind': 'percent', 'values': ['30'], 'count': 1}])

    def test_terminal_numeric_signatures_are_bounded_and_exclude_prose(self):
        source = 'PRIVATE_SOURCE amount EUR 15000000000.'
        response = 'PRIVATE_RESPONSE amount EUR 15000000000 and 30%.'
        result = h.quantity_failure_diagnostics(source, response)
        self.assertEqual(result['extra']['rows'], [{'kind': 'percent', 'values': ['30'], 'count': 1}])
        self.assertEqual(result['missing']['rows'], [])
        self.assertNotIn('PRIVATE', json.dumps(result))
        many = h.quantity_failure_diagnostics('', ' '.join(f'{n}%' for n in range(40)))
        self.assertEqual(len(many['response']['rows']), 20)
        self.assertTrue(many['response']['truncated'])
        self.assertFalse(h.quantity_failure_diagnostics(source, None)['response_available'])

    def test_quantity_diagnostics_match_french_grouping_quarter_and_month_gate(self):
        source = '2026年第三季度的9月收入为1234.5美元，增长5%。'
        response = ('En septembre du troisième trimestre de 2026, les revenus sont de '
                    '1\u202f234,5 dollars, en hausse de 5 %.')
        for original, translated, source_language, target_language in (
            (source, response, 'zh', 'fr'), (response, source, 'fr', 'zh')):
            with self.subTest(target=target_language):
                self.assertEqual(h.quantity_issues(original, translated, source_language, target_language), [])
                facts = h.quantity_failure_diagnostics(original, translated, source_language, target_language)
                self.assertEqual(facts['missing']['rows'], [])
                self.assertEqual(facts['extra']['rows'], [])
        facts = h.quantity_failure_diagnostics(source, response.replace('5 %', '6 %'), 'zh', 'fr')
        self.assertEqual(facts['missing']['rows'], [{'kind': 'percent', 'values': ['5'], 'count': 1}])
        self.assertEqual(facts['extra']['rows'], [{'kind': 'percent', 'values': ['6'], 'count': 1}])

    def test_quantity_diagnostics_named_event_scope_and_default_are_compatible(self):
        source = '9月双十一周期27天'
        response = 'In September, the Double 11 cycle lasts 27 days.'
        for original, translated, source_language, target_language in (
            (source, response, 'zh', 'en'), (response, source, 'en', 'zh')):
            with self.subTest(target=target_language):
                facts = h.quantity_failure_diagnostics(original, translated, source_language, target_language)
                self.assertEqual(facts['missing']['rows'], [])
                self.assertEqual(facts['extra']['rows'], [])
        legacy = h.quantity_failure_diagnostics('双十一周期27天', 'Double 11 lasts 27 days.')
        self.assertEqual(legacy['extra']['rows'], [{'kind': 'number', 'values': ['11'], 'count': 1}])
        french = h.quantity_failure_diagnostics('双十一周期27天',
                    'La fête des célibataires dure 27 jours.', 'zh', 'fr')
        self.assertEqual(french['extra']['rows'], [])
        self.assertEqual(french['missing']['rows'], [])

    def test_real_terminal_diagnostics_receive_detected_and_target_language(self):
        cases = [
            ('2026年第三季度的9月收入为1234.5美元，增长5%。',
             'En septembre du troisième trimestre de 2026, le revenu est de 1\u202f234,5 dollars, en hausse de 6 %.',
             'fr', 'percent', '5', '6'),
            ('9月双十一周期27天', 'In September, the Double 11 cycle lasts 28 days.',
             'en', 'number', '27', '28'),
        ]
        for source, response, target, kind, before, after in cases:
            with self.subTest(target=target):
                translator = self.translator(lambda _, result=response: result)
                with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'quantity'):
                    translator.translate(source, target, markdown=False)
                self.assertEqual(self.engine.calls[0][1:3], ('zh', target))
                facts = translator.failure_diagnostics[0]['quantities']
                self.assertEqual(facts['missing']['rows'], [{'kind': kind, 'values': [before], 'count': 1}])
                self.assertEqual(facts['extra']['rows'], [{'kind': kind, 'values': [after], 'count': 1}])
                self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_terminal_quantity_diagnostics_restore_protected_facts_before_comparison(self):
        source = '私有变化为150bps。'
        def respond(value, attempt):
            amount = ' '.join(h._PLACEHOLDERS.findall(value)) if attempt == 2 else '150 bps'
            return 'The change is ' + amount + ' and 30%.'
        translator = self.retrying_translator(respond)
        with self.assertRaises(h.OfflineTranslationValidationError):
            translator.translate(source, 'en', 'zh', markdown=False)
        facts = translator.failure_diagnostics[0]['quantities']
        self.assertEqual(facts['missing']['rows'], [])
        self.assertEqual(facts['extra']['rows'], [{'kind': 'percent', 'values': ['30'], 'count': 1}])
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_visible_english_retry_preserves_resources_identifiers_and_rejects_changed_facts(self):
        source = '按`原始资料`及CO2在第三季度150亿欧元投资。'
        masked, resources, terms = h._mask(source, 'en')
        model_input, protected, visible = h._quantity_retry_input(masked, len(resources) + len(terms), target='en')
        self.assertEqual(set(visible.values()), {'Q3', 'EUR 15,000,000,000'})
        self.assertEqual(list(protected.values()), ['CO2'])
        self.assertIn('__HYMTPH_0000__', model_input)
        self.assertIn(' Q3  EUR 15,000,000,000 ', model_input)
        self.assertEqual(h._quantity_retry_input(masked, 1, target='km')[:2], h._mask_quantity_facts(masked, 1, target='km'))
        with mock.patch.object(h, '_english_quantity_fact', return_value='USD 1'):
            with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'canonicalization'):
                h._quantity_retry_input('投资150亿欧元。', 0, target='en')
        def respond(value, attempt):
            if attempt < 2: return 'An investment changed.'
            return 'An investment of EUR 15 billion in Q3 follows ' + ' and '.join(h._PLACEHOLDERS.findall(value)) + '.'
        translator = self.retrying_translator(respond)
        translated = translator.translate(source, 'en', 'zh')
        self.assertIn('`原始资料`', translated)
        self.assertIn('CO2', translated)
        self.assertEqual(h.quantities(source), h.quantities(translated))
        for changed in ('EUR 1500000000', 'USD 15000000000', 'EUR 15000000000 and EUR 15000000000',
                        'an investment', 'EUR 15000000000 and 1%'):
            with self.subTest(changed=changed), tempfile.TemporaryDirectory() as directory:
                engine = RetryingEngine(lambda value, attempt: 'The investment is ' + changed + '.')
                translator = h.OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: engine)
                with self.assertRaises(h.OfflineTranslationValidationError):
                    translator.translate('投资150亿欧元。', 'en', 'zh')
                self.assertEqual(len(engine.calls), 3)
                self.assertFalse(list(Path(directory).rglob('*.json')))

    def test_english_retry_keeps_identifier_opaque_and_other_locale_contracts(self):
        source = '__HYMTPH_0001__ 私有第三季度150亿欧元订单三成。'
        masked, facts = h._mask_quantity_facts(source, 1, target='en')
        self.assertEqual(list(facts.values()), ['Q3', 'EUR 15,000,000,000', '30%'])
        self.assertNotIn('__HYMTPH_0001__', facts)
        self.assertEqual(masked.count('__HYMTPH_0001__'), 1)
        _, identifiers = h._mask_quantity_facts('CO2 ModelX1 171bpm', 0, target='en')
        self.assertEqual(list(identifiers.values()), ['CO2', 'ModelX1'])
        self.assertEqual(h._mask_quantity_facts('第三季度150亿欧元三成', 0, target='km'),
                         h._mask_quantity_facts('第三季度150亿欧元三成', 0))
        for bad in ('Outlook: __HYMTPH_0000__ and USD 1.',
                    'Outlook: __HYMTPH_0000__ __HYMTPH_0000__.', 'Outlook unchanged.'):
            with self.subTest(bad=bad):
                translator = self.retrying_translator(lambda _value, _attempt: bad)
                with self.assertRaises(h.OfflineTranslationValidationError):
                    translator.translate('本期150亿欧元投资。', 'en', 'zh')

    def test_quantity_retry_masks_complete_basis_points_touching_non_ascii_prose(self):
        for quantity, following in (
            ('171bp', '至'), ('171BP', 'ទៅ'), ('171bps', '至'),
            ('-17.1BP', '至'), ('−17.1 bps', 'ទៅ'),
            ('-0.25 basis points', '至'), ('-17.1个基点', '至'),
            ('-17.1基點', 'ទៅ'),
        ):
            with self.subTest(quantity=quantity, following=following):
                source = f'收益率变化{quantity}{following}2%。'
                masked, replacements = h._mask_quantity_facts(source, 0)
                self.assertEqual(list(replacements.values()), [quantity, '2%'])
                self.assertEqual(masked, f'收益率变化__HYMTPH_0000__{following}__HYMTPH_0001__。')
                self.assertEqual(h._restore_terms(masked, replacements), source)

    def test_quantity_retry_does_not_treat_ascii_identifiers_as_basis_points(self):
        for value in ('171bpm', '171bpword', '171bp2', '171bp_total'):
            with self.subTest(value=value):
                masked, replacements = h._mask_quantity_facts(value, 0)
                self.assertEqual(masked, value)
                self.assertEqual(replacements, {})

    def test_basis_point_retry_preserves_caller_and_opaque_token_identity_and_cache(self):
        source = '收益率按__HYMTPH_0001__和`USD`上升171bp至2%。'

        def respond(text, retry):
            self.assertIn('__HYMTPH_0001__', text)
            self.assertIn('__HYMTPH_0000__', text)
            if retry < 2:
                self.assertIn('171bp至2%', text)
                return 'អត្រាតាម __HYMTPH_0001__ និង __HYMTPH_0000__ កើន 171% ដល់ 2%។'
            self.assertEqual(text, '收益率按__HYMTPH_0001__和__HYMTPH_0000__上升__HYMTPH_0002__至__HYMTPH_0003__。')
            return 'អត្រាតាម __HYMTPH_0001__ និង __HYMTPH_0000__ កើន __HYMTPH_0002__ ដល់ __HYMTPH_0003__។'

        translator = self.retrying_translator(respond)
        expected = 'អត្រាតាម __HYMTPH_0001__ និង `USD` កើន 171bp ដល់ 2%។'
        self.assertEqual(translator.translate(source, 'km', 'zh'), expected)
        self.assertEqual(translator.translate(source, 'km', 'zh'), expected)
        self.assertEqual([row[3] for row in self.engine.calls], [0, 1, 2])
        self.assertEqual(translator.stats['cache_hits'], 1)

    def test_basis_point_retry_rejects_missing_or_duplicated_quantity_tokens_without_caching(self):
        for damaged in ('អត្រាកើន ដល់ __HYMTPH_0001__។',
                        'អត្រាកើន __HYMTPH_0000__ __HYMTPH_0000__ ដល់ __HYMTPH_0001__។'):
            with self.subTest(damaged=damaged):
                translator = self.retrying_translator(
                    lambda _text, retry: 'អត្រាកើន 171% ដល់ 2%។' if retry < 2 else damaged)
                with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'placeholder'):
                    translator.translate('收益率上升171bp至2%。', 'km', 'zh')
                self.assertEqual([row[3] for row in self.engine.calls], [0, 1, 2])
                self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_basis_point_equivalence_keeps_percentage_points_distinct_from_percent(self):
        source = '收益率上升171bp至2%。'
        h.validate_result(source, 'អត្រាកើន 1.71 percentage points ដល់ 2%។', 'zh', 'km')
        for changed in ('1.71%', '171 percentage points', '170bp'):
            with self.subTest(changed=changed):
                with self.assertRaisesRegex(h.OfflineTranslationValidationError, 'quantity'):
                    h.validate_result(source, f'អត្រាកើន {changed} ដល់ 2%។', 'zh', 'km')

    def test_pinned_engine_retries_short_heading_with_target_script(self):
        source = 'Market Outlook'

        def respond(_text, retry):
            return 'Market Outlook' if retry < 2 else 'बाज़ार परिदृश्य'

        translator = self.retrying_translator(respond)
        self.assertEqual(translator.translate(source, 'hi', 'en'), 'बाज़ार परिदृश्य')
        self.assertEqual([row[3] for row in self.engine.calls], [0, 1, 2])

    def test_source_fallback_caller_can_bound_validation_to_one_attempt(self):
        translator = self.retrying_translator(lambda _text, _retry: '错误金额 USD99m')
        translator.validation_attempts = 1
        with self.assertRaises(h.OfflineTranslationValidationError):
            translator.translate('Revenue USD10m.', 'zh', 'en')
        self.assertEqual(len(self.engine.calls), 1)

    def test_plain_title_cannot_cache_an_invented_table_pipe(self):
        translator = self.retrying_translator(lambda _text, retry: '研究 | 摘要' if retry == 0 else '研究摘要')
        self.assertEqual(translator.translate('Research summary', 'zh', 'en', markdown=False), '研究摘要')
        self.assertEqual(len(self.engine.calls), 2)

    def test_deadline_is_preserved_as_timeout_for_checkpointing(self):
        translator = self.translator(lambda _text: self.fail('No model call after deadline'))
        translator.set_deadline(time.monotonic() - 1)
        with self.assertRaises(TimeoutError):
            translator.translate('Research summary', 'zh', 'en')
        self.assertEqual(self.engine.calls, [])

    def test_model_request_is_bounded_by_remaining_run_budget(self):
        engine = object.__new__(h._HyMTEngine)
        engine.port = 1
        response = {'choices': [{'finish_reason': 'stop', 'message': {'content': '研究摘要'}}]}
        with mock.patch.object(h, 'request_json', return_value=response) as request:
            engine.translate('Research summary', 'en', 'zh', deadline=time.monotonic()+5)
        self.assertGreater(request.call_args.kwargs['timeout'], 0)
        self.assertLessEqual(request.call_args.kwargs['timeout'], 5)
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
        translator = self.translator(lambda _: '__HYMTPH_0000__ (영업이익률)은 31%입니다.')
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
        translator = self.translator(lambda _: '__HYMTPH_0000__은 31%를 유지했으며 __HYMTPH_0001__은 7% 증가했습니다.')
        output = translator.translate(source, 'ko', 'en')
        self.assertIn('매출총이익률', output)
        self.assertIn('영업이익', output)
        self.assertEqual(self.engine.calls[0][0], '__HYMTPH_0000__ remained at 31%, while __HYMTPH_0001__ increased by 7%.')
        self.assertEqual(len(self.engine.calls), 1)

    def test_public_diagnostic_opt_in_retains_rejected_raw_without_caching(self):
        captured = []
        engine = Engine(lambda _: '잘못된 출력 100%')
        translator = h.OfflineTranslator(cache_dir=self.directory.name,
            engine_factory=lambda s,t: engine, diagnostic_callback=captured.append)
        with self.assertRaises(h.OfflineTranslationError):
            translator.translate('Gross margin was 31%.', 'ko', 'en')
        self.assertEqual(captured[0]['raw_translation'], '잘못된 출력 100%')
        self.assertEqual(captured[0]['model_input'], '__HYMTPH_0000__ was 31%.')
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
        translator = self.translator(lambda _: '现金储备 | 1.2亿美元')
        source = '| Cash reserves | USD 120 million |'
        self.assertEqual(translator.translate_markdown(source, 'zh', 'en'), '|现金储备 | 1.2亿美元|')
        self.assertEqual(self.engine.calls[0][0], source)

    def test_table_interior_separator_loss_or_added_column_is_rejected(self):
        for output in ('现金储备 1.2亿美元', '现金储备 | 新增 | 1.2亿美元'):
            with self.subTest(output=output):
                translator = self.translator(lambda _, output=output: output)
                with self.assertRaisesRegex(h.OfflineTranslationError, 'Markdown structure'):
                    translator.translate_markdown('| Cash reserves | USD 120 million |', 'zh', 'en')

    def test_table_edges_do_not_hide_quantity_damage(self):
        translator = self.translator(lambda _: '现金储备 | 120万美元')
        with self.assertRaisesRegex(h.OfflineTranslationError, 'quantity'):
            translator.translate_markdown('| Cash reserves | USD 120 million |', 'zh', 'en')

    def test_plain_filename_punctuation_is_not_markdown_but_claims_remain_checked(self):
        translator = self.translator(lambda _: '短期增长12.5%')
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

    def test_planning_term_ordinal_is_source_derived_and_numeric_claims_are_unmasked(self):
        source = 'The 16th Five-Year Plan forecasts revenue growth of 12.5% and USD 120 million investment.'
        masked, _resources, terms = h._mask(source, 'zh')
        self.assertEqual(terms, {'__HYMTPH_0000__': '第16个五年'})
        self.assertIn('12.5%', masked)
        self.assertIn('USD 120 million', masked)
        for output, error in [
            ('第15个五年计划预计收入增长12.5%，投资1.2亿美元。', 'placeholder'),
            ('__HYMTPH_0000__计划预计收入增长125%，投资1.2亿美元。', 'quantity'),
            ('__HYMTPH_0000__计划预计收入增长12.5%，投资120万美元。', 'quantity'),
        ]:
            with self.subTest(output=output):
                translator = self.translator(lambda _, output=output: output)
                with self.assertRaisesRegex(h.OfflineTranslationError, error):
                    translator.translate(source, 'zh', 'en', markdown=False)
        self.assertFalse(list(Path(self.directory.name).rglob('*.json')))

    def test_controlled_period_next_to_markdown_underscores_keeps_emphasis(self):
        translator = self.translator(lambda _: '___HYMTPH_0000___规划')
        self.assertEqual(translator.translate('_15th Five-Year_ plan', 'zh', 'en'), '_第15个五年_规划')

    def test_opted_in_markdown_fallback_preserves_bad_units_and_translates_neighbors(self):
        cash = '- Cash reserves were USD 120 million; see [source](../2026/report.pdf).\r\n'
        figure = '> See [[PORTAL_IMAGE_001]] for the chart.\r\n'
        source = '# Revenue\r\n\r\n' + cash + figure + 'Revenue grew 12.5%.\r\n'
        def respond(text):
            if text.startswith('Cash reserves'):
                return text.replace('Cash reserves were USD 120 million', '现金储备为120万美元')
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
        translator = self.translator(lambda _: '收入增长125%。')
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
