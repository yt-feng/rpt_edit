import hashlib
import unittest
from collections import Counter
from decimal import Decimal

from financial_quantity_integrity import quantities, quantity_issues

COMMA_LOCALES = ('fr', 'es', 'de', 'id', 'pt', 'tr', 'ru', 'it', 'vi', 'pl', 'cs', 'nl', 'uk', 'kk')
DOT_GROUP_LOCALES = ('es', 'de', 'id', 'pt', 'tr', 'it', 'vi', 'nl')
SPACE_GROUP_LOCALES = ('fr', 'ru', 'pl', 'cs', 'uk', 'kk')
INDIAN_GROUP_LOCALES = ('hi', 'gu', 'te', 'mr', 'bn', 'ta')


class FinancialQuantityTests(unittest.TestCase):
    def test_all_33_supported_locales_match_installed_cldr_numeric_samples(self):
        from portal_extended_locales import ADDITIONAL
        # ICU 78.3 / CLDR 48.0 fixtures, using the repository's OG_LOCALES.
        samples = {
            'fr': ('0,125', '1\u202f234\u202f567,89'),
            'pt': ('0,125', '1.234.567,89'), 'es': ('0,125', '1.234.567,89'),
            'tr': ('0,125', '1.234.567,89'), 'ru': ('0,125', '1\u00a0234\u00a0567,89'),
            'th': ('0.125', '1,234,567.89'), 'it': ('0,125', '1.234.567,89'),
            'de': ('0,125', '1.234.567,89'), 'vi': ('0,125', '1.234.567,89'),
            'ms': ('0.125', '1,234,567.89'), 'id': ('0,125', '1.234.567,89'),
            'tl': ('0.125', '1,234,567.89'), 'hi': ('0.125', '12,34,567.89'),
            'zh-Hant': ('0.125', '1,234,567.89'), 'pl': ('0,125', '1\u00a0234\u00a0567,89'),
            'cs': ('0,125', '1\u00a0234\u00a0567,89'), 'nl': ('0,125', '1.234.567,89'),
            'km': ('0.125', '1,234,567.89'), 'my': ('၀.၁၂၅', '၁,၂၃၄,၅၆၇.၈၉'),
            'fa': ('۰٫۱۲۵', '۱٬۲۳۴٬۵۶۷٫۸۹'), 'gu': ('0.125', '12,34,567.89'),
            'ur': ('0.125', '1,234,567.89'), 'te': ('0.125', '12,34,567.89'),
            'mr': ('०.१२५', '१२,३४,५६७.८९'), 'he': ('0.125', '1,234,567.89'),
            'bn': ('০.১২৫', '১২,৩৪,৫৬৭.৮৯'), 'ta': ('0.125', '12,34,567.89'),
            'uk': ('0,125', '1\u00a0234\u00a0567,89'), 'bo': ('0.125', '1,234,567.89'),
            'kk': ('0,125', '1\u00a0234\u00a0567,89'), 'mn': ('0.125', '1,234,567.89'),
            'ug': ('0.125', '1,234,567.89'), 'yue': ('0.125', '1,234,567.89'),
        }
        self.assertEqual(set(samples), set(ADDITIONAL))
        for locale, (fraction, large) in samples.items():
            for source, translated in (('0.125%', fraction + '%'), ('USD1234567.89', 'USD' + large)):
                with self.subTest(locale=locale, source=source):
                    self.assertEqual(quantity_issues(source, translated, 'en', locale), [])
                    self.assertEqual(quantity_issues(translated, source, locale, 'en'), [])
            self.assertTrue(quantity_issues('125%', fraction + '%', 'en', locale))
            self.assertTrue(quantity_issues('USD1234.56789', 'USD' + large, 'en', locale))

    def test_space_group_families_do_not_merge_decimal_lists_or_source_multisets(self):
        for locale in SPACE_GROUP_LOCALES:
            for space in (' ', '\u00a0', '\u202f'):
                with self.subTest(locale=locale, space=repr(space)):
                    self.assertEqual(quantity_issues('1234.5; 6789.5', f'1{space}234,5, 6{space}789,5', 'en', locale), [])
                    self.assertEqual(quantity_issues('0.125; 1.25', '0,125 1,250', 'en', locale), [])
                    self.assertTrue(quantity_issues('1; 234', f'1{space}234', 'en', locale))
                    self.assertTrue(quantity_issues('1; 234.567', f'1{space}234,567', 'en', locale))
                    self.assertIn('invalid_numeric_format', quantity_issues('1.234; 2.345; 67', '1,234 2.345,67', 'en', locale))

    def test_indian_grouping_keeps_full_numbers_units_and_existing_western_notation(self):
        for locale in INDIAN_GROUP_LOCALES:
            for source, translated in (
                ('1234', '1,234'), ('12345', '12,345'), ('123456', '1,23,456'),
                ('1234567.8901', '12,34,567.8901'), ('123456789', '12,34,56,789'),
                ('-1234567.89%', '−12,34,567.89%'), ('USD1234567.89', 'USD12,34,567.89'),
                ('1234567.89 bp', '12,34,567.89 bp'), ('1234567.89 million', '12,34,567.89 million'),
                ('1234567.89', '1,234,567.89'), ('0.125%', '0.125%'),
            ):
                with self.subTest(locale=locale, source=source):
                    self.assertEqual(quantity_issues(source, translated, 'en', locale), [])
                    self.assertEqual(quantity_issues(translated, source, locale, 'en'), [])
            for source in ('12.34; 567.89', '1234.56789', '-1234567.89', '1234567.89; 1234567.89'):
                self.assertTrue(quantity_issues(source, '12,34,567.89', 'en', locale))
            for malformed in ('123,45,678', '1,234,56', '0,123', '1,23', '1,,234',
                              '1,23,456,789', '.1,23,456.78', '-+1,23,456.78', '1,23,456.7.8'):
                with self.subTest(locale=locale, malformed=malformed):
                    self.assertIn('invalid_numeric_format', quantity_issues(malformed, malformed, locale, locale))
            self.assertEqual(quantity_issues('1; 2; 3', '1, 2, 3', 'en', locale), [])
            self.assertTrue(quantity_issues('125%', '0,125%', 'en', locale))
            self.assertEqual(quantity_issues('USD1234567.89', 'USD１２，３４，５６７．８９', 'en', locale), [])
        # The same spelling is not a valid grouping for unrelated locales.
        for locale in ('en', 'fr', 'de', 'ur', '', 'hi-unsupported'):
            self.assertTrue(quantity_issues('1234567.89', '12,34,567.89', 'en', locale))

    def test_turkish_percent_prefix_preserves_type_sign_precision_and_multiplicity(self):
        for source, translated in (('0.125%', '%0,125'), ('-0.125%', '-%0,125'),
                                   ('1234.5%', '%1.234,5'), ('0.125%', '% 0,125'),
                                   ('-0.125%', '- %0,125'), ('-0.125%', '− %0,125'),
                                   ('5%; 0.125', '5% 0,125'), ('5%; 0.125', '5 % 0,125'),
                                   ('-5%; 0.125%', '-%5 %0,125'), ('-5%; 10%', '-%5 %10')):
            self.assertEqual(quantity_issues(source, translated, 'en', 'tr'), [])
            self.assertEqual(quantity_issues(translated, source, 'tr', 'en'), [])
        for source, translated in (('125%', '%0,125'), ('0.125', '%0,125'),
                                   ('0.125 percentage points', '%0,125'), ('-0.125%', '%0,125'),
                                   ('0.125%', '%0,125 %0,125'), ('5; 0.125%', '5% 0,125'),
                                   ('5; 0.125%', '5 % 0,125'), ('0.125%', '- %0,125'),
                                   ('5%; -0.125%', '-%5 %0,125'), ('5%; -10%', '-%5 %10')):
            self.assertTrue(quantity_issues(source, translated, 'en', 'tr'))
        self.assertIn('invalid_numeric_format', quantity_issues('0.125%', '-%-0,125', 'en', 'tr'))
        self.assertIn('invalid_numeric_format', quantity_issues('-0.125%', '--%0,125', 'en', 'tr'))
        for locale in ('en', 'fr', 'de', 'tr-unsupported'):
            self.assertTrue(quantity_issues('0.125%', '%0.125', 'en', locale))

    def test_icu_numeric_lrm_preserves_currency_sign_magnitude_and_multiset(self):
        for locale in ('fa', 'ur', 'he'):
            for source, translated in (
                ('USD-0.125', 'USD\u200e−0.125'), ('USD-0.125', 'USD−\u200e0.125'),
                ('USD-1234567.89', 'USD\u200e−۱٬۲۳۴٬۵۶۷٫۸۹'),
                ('-0.125%', '\u200e−0.125%'), ('USD12', 'USD1\u200e2'),
            ):
                with self.subTest(locale=locale, source=source):
                    self.assertEqual(quantity_issues(source, translated, 'en', locale), [])
                    self.assertEqual(quantity_issues(translated, source, locale, 'en'), [])
            for source, translated in (
                ('USD0.125', 'USD\u200e−0.125'), ('USD0.125', 'USD−\u200e0.125'),
                ('USD-125', 'USD\u200e−0.125'), ('EUR-0.125', 'USD\u200e−0.125'),
                ('-0.125', 'USD\u200e−0.125'), ('USD-0.125', 'USD\u200e−0.125 USD\u200e−0.125'),
                ('USD1; 2', 'USD1\u200e2'),
            ):
                self.assertTrue(quantity_issues(source, translated, 'en', locale))
            for translated in ('USD-\u200e-0.125', 'USD\u200e--0.125', 'USD+\u200e-0.125'):
                self.assertIn('invalid_numeric_format', quantity_issues('USD-0.125', translated, 'en', locale))
        for locale in ('en', 'fr', 'fa-unsupported'):
            self.assertTrue(quantity_issues('USD-0.125', 'USD\u200e−0.125', 'en', locale))
        # Unrelated direction marks and marks inside words are not stripped.
        self.assertTrue(quantity_issues('USD-0.125', 'USD\u200f−0.125', 'en', 'fa'))
        self.assertTrue(quantity_issues('USD12', 'US\u200eD12', 'en', 'fa'))

    def test_locale_decimal_comma_preserves_three_fractional_digits_not_thousands(self):
        for locale in COMMA_LOCALES:
            for source, translated in (
                ('0.125%', '0,125%'), ('-0.125%', '-0,125%'),
                ('USD0.125', 'USD0,125'), ('0.125USD', '0,125USD'),
                ('USD 1.234 million', 'USD 1,234 million'),
            ):
                with self.subTest(locale=locale, source=source):
                    self.assertEqual(quantity_issues(source, translated, 'en', locale), [])
                    self.assertEqual(quantity_issues(translated, source, locale, 'en'), [])
            self.assertTrue(quantity_issues('125%', '0,125%', 'en', locale))
            self.assertTrue(quantity_issues('0,125%', '125%', locale, 'en'))
            self.assertTrue(quantity_issues('USD1234', 'USD1,234', 'en', locale))

    def test_long_comma_fractions_are_indivisible_and_not_separate_numbers(self):
        for locale in COMMA_LOCALES:
            for value in ('0.000125', '1.2345', '-12.34567', '0.123456789'):
                for form in ('{}', 'USD{}', '{}EUR', '{}%', '{} bp', '{} million'):
                    source, translated = form.format(value), form.format(value.replace('.', ','))
                    with self.subTest(locale=locale, source=source):
                        self.assertEqual(quantity_issues(source, translated, 'en', locale), [])
                        self.assertEqual(quantity_issues(translated, source, locale, 'en'), [])
            self.assertTrue(quantity_issues('0; 125', '0,000125', 'en', locale))
            self.assertTrue(quantity_issues('1.234; 5', '1,2345', 'en', locale))
        for source, translated in (('0.125; 1.25', '0,125 1,250'),
                                   ('123.45; 234.56', '123,45 234,56'),
                                   ('1234.5; 2.25', '1\u202f234,5 2,25'),
                                   ('1234.5; 6789.5', '1 234,5, 6 789,5')):
            self.assertEqual(quantity_issues(source, translated, 'en', 'fr'), [])
        for malformed in ('1,234 2.345,67', '1,234, 2.345,67'):
            self.assertIn('invalid_numeric_format',
                          quantity_issues('1.234; 2.345; 67', malformed, 'en', 'fr'))

    def test_dot_grouping_and_decimal_comma_preserve_whole_magnitudes(self):
        for locale in DOT_GROUP_LOCALES:
            for source, translated in (
                ('1234', '1.234'), ('1234567', '1.234.567'),
                ('USD1234.50', 'USD1.234,50'), ('1234.50EUR', '1.234,50EUR'),
                ('-1234.567 USD', '−1.234,567 USD'),
                ('1234567.8901%', '1.234.567,8901%'),
            ):
                with self.subTest(locale=locale, source=source):
                    self.assertEqual(quantity_issues(source, translated, 'en', locale), [])
                    self.assertEqual(quantity_issues(translated, source, locale, 'en'), [])
            # Three-digit dot groups have a single locale meaning, even if
            # treating them as English decimals would match the source.
            self.assertTrue(quantity_issues('1.234', '1.234', 'en', locale))
            self.assertEqual(quantity_issues('1.234', '1,234', 'en', locale), [])
            for value in ('0.125', '12.34', '1.2345', '1234.567'):
                self.assertEqual(quantity_issues(value, value, 'en', locale), [])

    def test_explicit_locale_does_not_reinterpret_english_or_unsupported_languages(self):
        for locale in ('', 'en', 'fr-unsupported'):
            with self.subTest(locale=locale):
                self.assertEqual(quantities('1,234', language=locale),
                                 Counter({('number', Decimal(1234)): 1}))
                self.assertEqual(quantities('1.234', language=locale),
                                 Counter({('number', Decimal('1.234')): 1}))
        for locale in COMMA_LOCALES:
            self.assertEqual(quantities('1,234', language=locale),
                             Counter({('number', Decimal('1.234')): 1}))
        self.assertEqual(quantities('1.234', language='fr'),
                         Counter({('number', Decimal('1.234')): 1}))

    def test_locale_normalization_keeps_currency_rate_sign_and_multiplicity_gates(self):
        for locale in COMMA_LOCALES:
            source = 'USD 0.125; -1.25%; 2.5 percentage points; 25 bp; 3; 3.'
            valid = 'USD 0,125; -1,25%; 2,5 percentage points; 25 bp; 3; 3.'
            with self.subTest(locale=locale):
                self.assertEqual(quantity_issues(source, valid, 'en', locale), [])
                for changed in (
                    valid.replace('USD', 'EUR'), valid.replace('USD ', ''),
                    valid.replace('-1,25', '1,25'), valid.replace('0,125', '0,126'),
                    valid.replace('percentage points', '%'), valid.replace('25 bp', '25%'),
                    valid.removesuffix(' 3.'), valid + ' 3.', valid + ' 0,125%',
                ):
                    self.assertTrue(quantity_issues(source, changed, 'en', locale), changed)

    def test_malformed_localized_decimal_cannot_be_accepted_as_valid_fragments(self):
        for locale in COMMA_LOCALES:
            for malformed in ('1.23.456,78', '1,23,456', '1.234,5,6',
                              '1,234.50', '1.234.,50', '.1.234,50',
                              '..1.234,50', '-+1.234,50', '1٬234.567,89'):
                with self.subTest(locale=locale, malformed=malformed):
                    issues = quantity_issues(malformed, malformed, locale, locale)
                    self.assertIn('invalid_numeric_format', issues)
                    self.assertTrue(quantity_issues('1; 234.50', malformed, 'en', locale))
        # Comma plus a space is a list separator, not a decimal separator.
        for locale in COMMA_LOCALES:
            self.assertEqual(quantity_issues('1; 2; 3', '1, 2, 3', 'en', locale), [])
            self.assertTrue(quantity_issues('1; 2', '1, 2, 3', 'en', locale))

    def test_numeric_width_and_arabic_separators_cannot_reintroduce_thousandfold_change(self):
        for locale in COMMA_LOCALES:
            with self.subTest(locale=locale):
                self.assertEqual(quantity_issues('0.125%', '０，１２５％', 'en', locale), [])
                self.assertTrue(quantity_issues('125%', '０，１２５％', 'en', locale))
                self.assertEqual(quantity_issues('0.125%', '٠٫١٢٥٪', 'en', locale), [])
                self.assertTrue(quantity_issues('125%', '٠٫١٢٥٪', 'en', locale))
                self.assertEqual(quantity_issues('USD 1234567.50', 'USD ١٬٢٣٤٬٥٦٧٫٥٠', 'en', locale), [])
        for locale in DOT_GROUP_LOCALES:
            self.assertEqual(quantity_issues('USD1234.50', 'USD１．２３４，５０', 'en', locale), [])
        self.assertEqual(quantity_issues('USD1234.50', 'USD１\u202f２３４，５０', 'en', 'fr'), [])

    def test_registered_seo_checkpoint_accepts_numeric_prose_differences_before_handoff(self):
        from types import SimpleNamespace
        from build_portal_extended_locales import CHECKPOINT_VERSION
        from offline_translation import MODEL_ID
        from portal_extended_continuation import checkpoint_evidence
        from portal_extended_locales import digest, stable_bytes

        generation = 'a' * 64
        for locale in COMMA_LOCALES:
            for source, same_quantity in (('Rate 0.125%.', True), ('Rate 125%.', False)):
                with self.subTest(locale=locale, source=source):
                    key = digest(stable_bytes([CHECKPOINT_VERSION, MODEL_ID, locale, 'en', source]))
                    text = {'ru': 'Рост 0,125%.', 'uk': 'Ріст 0,125%.', 'kk': 'Өсім 0,125%.'}.get(locale, 'Ratio 0,125%.')
                    raw = stable_bytes({'version': CHECKPOINT_VERSION, 'model': MODEL_ID,
                        'locale': locale, 'source_generation': generation,
                        'rows': {key: {'source': source, 'language': 'en', 'text': text}}})
                    store = SimpleNamespace(checkpoint_object_key=lambda *_: 'exact-checkpoint',
                                            _get=lambda *_, **__: raw)
                    self.assertEqual(bool(quantity_issues(source, text, 'en', locale)), not same_quantity)
                    self.assertEqual(checkpoint_evidence(store, locale, generation, digest(raw)), {key})

    def test_registered_seo_checkpoint_still_rejects_broken_display_contracts(self):
        from types import SimpleNamespace
        from build_portal_extended_locales import CHECKPOINT_VERSION
        from offline_translation import MODEL_ID
        from portal_extended_continuation import checkpoint_evidence
        from portal_extended_locales import ExpansionError, digest, stable_bytes

        generation, source, locale = 'a' * 64, 'Rate 125%.', 'fr'
        key = digest(stable_bytes([CHECKPOINT_VERSION, MODEL_ID, locale, 'en', source]))
        for text, message in (('', 'Empty translated text'),
                              ('Valeur privée \ufffd.', 'Invalid Unicode translation'),
                              ('Rapport __KC_PH_001__.', 'Unrestored protected identifier'),
                              ('Ratio 0,125% | ajouté.', 'Table column boundaries changed')):
            with self.subTest(message=message):
                raw = stable_bytes({'version': CHECKPOINT_VERSION, 'model': MODEL_ID,
                    'locale': locale, 'source_generation': generation,
                    'rows': {key: {'source': source, 'language': 'en', 'text': text}}})
                store = SimpleNamespace(checkpoint_object_key=lambda *_: 'exact-checkpoint',
                                        _get=lambda *_, **__: raw)
                with self.assertRaisesRegex(ExpansionError, message):
                    checkpoint_evidence(store, locale, generation, digest(raw))

    def test_french_complete_space_grouping_preserves_numbers_currency_and_fractional_precision(self):
        for space in (' ', '\u00a0', '\u202f'):
            for source, translated in (
                ('销量为1234.5件。', f'Les ventes atteignent 1{space}234,5 unités.'),
                ('金额为1234.5美元。', f'Le montant est de 1{space}234,5 dollars.'),
                ('金额为-1234.567美元。', f'Le montant est de −1{space}234,567 dollars.'),
                ('数量为1234567。', f'Le total est de 1{space}234{space}567.'),
                ('增长1234.5%。', f'La croissance est de 1{space}234,5 %.'),
            ):
                with self.subTest(space=repr(space), source=source):
                    self.assertEqual(quantity_issues(source, translated, 'zh', 'fr'), [])
                    self.assertEqual(quantity_issues(translated, source, 'fr', 'zh'), [])
        self.assertEqual(quantities('1\u202f234,567 dollars', language='fr'),
                         Counter({('currency', 'USD', Decimal('1234.567')): 1}))

    def test_french_grouping_does_not_hide_bad_groups_changes_extra_numbers_or_units(self):
        source = '金额为1234.5美元。'
        for translated in (
            'Le montant est de 1\u202f235,5 dollars.',
            'Le montant est de 1\u202f234,5 euros.',
            'Le montant est de 1\u202f234,5.',
            'Le montant est de 1\u202f234,5 dollars, plus 2 unités.',
            'Le montant est de -1\u202f234,5 dollars.',
            'Le montant est de 1\u202f234,5 %.',
        ):
            with self.subTest(translated=translated):
                self.assertTrue(quantity_issues(source, translated, 'zh', 'fr'))
        for malformed in ('12 34,5', '1 23 4,5', '1234 567,5', '1 234 56,5',
                          '1 234,5,6', '1 234.5,6', '1\t234,5', '1\n234,5',
                          '1  234,5', '1\u2009234,5', '0 1234,5'):
            with self.subTest(malformed=malformed):
                self.assertTrue(quantity_issues('数量为1234.5。', malformed, 'zh', 'fr'))
        # A malformed prefix must not allow its otherwise valid suffix to be
        # merged, turning two distinct observed quantities into one.
        self.assertTrue(quantity_issues('数量为12和34567。', '12 34 567', 'zh', 'fr'))
        self.assertTrue(quantity_issues('数量为1和234.567。', '1\u202f234,567', 'zh', 'fr'))

    def test_explicit_french_quarters_preserve_attached_year_and_ordinal_both_directions(self):
        for number, ordinal in enumerate(('premier', 'deuxième', 'troisième', 'quatrième'), 1):
            for connector in (' de ', ' '):
                source = f'2026年第{number}季度增长5%。'
                translated = f'Au {ordinal} trimestre{connector}2026, la croissance est de 5 %.'
                with self.subTest(number=number, connector=connector):
                    self.assertEqual(quantity_issues(source, translated, 'zh', 'fr'), [])
                    self.assertEqual(quantity_issues(translated, source, 'fr', 'zh'), [])
            self.assertEqual(quantity_issues(f'第{number}季度增长5%。',
                             f'Au {ordinal} trimestre, la croissance est de 5 %.', 'zh', 'fr'), [])
        self.assertEqual(quantities('Au troisième trimestre de 2026', language='fr'),
                         Counter({('quarter', 2026, 3): 1}))

    def test_french_quarter_changes_omissions_and_unsupported_periods_still_fail(self):
        source = '2026年第三季度增长5%。'
        for translated in (
            'Au quatrième trimestre de 2026, la croissance est de 5 %.',
            'Au troisième trimestre de 2025, la croissance est de 5 %.',
            'Au troisième trimestre de 2026, la croissance est de 6 %.',
            'Au troisième trimestre, la croissance est de 5 %.',
            'En 2026, la croissance est de 5 %.',
            'Au troisième trimestre de 2026, la croissance est de 5 points de pourcentage.',
            'Au troisième trimestre de 2026, la croissance est de 5 % et de 2 %.',
            'Au troisième trimestre de 2026 et au troisième trimestre de 2026, croissance de 5 %.',
            'Au troisième semestre de 2026, la croissance est de 5 %.',
            'Au cinquième trimestre de 2026, la croissance est de 5 %.',
            'Au troisième trimestre de 26, la croissance est de 5 %.',
            'Au troisième trimestriel de 2026, la croissance est de 5 %.',
        ):
            with self.subTest(translated=translated):
                self.assertTrue(quantity_issues(source, translated, 'zh', 'fr'))
        self.assertTrue(quantity_issues('第三季度增长5%。',
                        'Au troisième trimestre de 2026, la croissance est de 5 %.', 'zh', 'fr'))

    def test_french_only_grammar_keeps_default_other_languages_and_month_recheck_contracts(self):
        source = '2026年第三季度的9月收入为1234.5美元，增长5%。'
        translated = ('En septembre du troisième trimestre de 2026, les revenus sont de '
                      '1\u202f234,5 dollars, en hausse de 5 %.')
        self.assertEqual(quantity_issues(source, translated, 'zh', 'fr'), [])
        self.assertEqual(quantity_issues(translated, source, 'fr', 'zh'), [])
        for language in ('', 'en', 'de', 'fr-unsupported'):
            with self.subTest(language=language):
                self.assertTrue(quantity_issues(source, translated, 'zh', language))
                self.assertEqual(quantities('1\u202f234,5', language=language),
                                 Counter({('number', Decimal(1)): 1, ('number', Decimal('234.5')): 1}))
        self.assertTrue(quantity_issues(source, translated.replace('septembre', 'octobre'), 'zh', 'fr'))

    def test_observed_double_eleven_title_preserves_event_and_day_count(self):
        # The exact public source and final retry input match failed run
        # 38030674044; its diagnostic reported an extra bare number 11.
        source = '高盛：中国美妆双十一周期缩短至27天，KOL、短视频与AI重塑竞争'
        self.assertEqual(hashlib.sha256(source.encode()).hexdigest(),
                         '7b2e95afc74b770dfc7b66e845d84e4b80552b965c63f46ee22271935eafa3c3')
        translated = ('Goldman Sachs: China’s beauty Double 11 cycle shortens to 27 days; '
                      'KOLs, short videos and AI reshape competition.')
        expected = Counter({('shopping_event', 'double_eleven'): 1, ('number', Decimal(27)): 1})
        self.assertEqual(quantities(source, named_events=True), expected)
        self.assertEqual(quantities(translated, named_events=True), expected)
        self.assertEqual(quantity_issues(source, translated, 'zh', 'en'), [])

    def test_double_eleven_aliases_are_counted_as_the_same_event(self):
        for source in ('双十一周期27天', '双11周期27天', '雙十一周期27天', '雙11周期27天'):
            for event in ('Double 11', 'Double11', 'Double-11', 'Double Eleven',
                          'Double-Eleven', 'Singles Day', "Singles' Day", 'Singles’ Day'):
                with self.subTest(source=source, event=event):
                    translated = f'The {event} cycle lasts 27 days.'
                    self.assertEqual(quantity_issues(source, translated, 'zh', 'en'), [])
                    self.assertEqual(quantity_issues(translated, source, 'en', 'zh'), [])

    def test_double_eleven_equivalence_rejects_changed_missing_or_extra_facts(self):
        source = '双十一周期缩短至27天'
        for translated in (
            'The cycle shortens to 27 days.',
            'The Double 12 cycle shortens to 27 days.',
            'The Double Twelve cycle shortens to 27 days.',
            '双十二周期缩短至27天',
            'The Double 11 cycle shortens to 28 days.',
            'The Double 11 cycle shortens.',
            'The Double 11 cycle shortens to 27 days and 11 hours.',
            'The Double 11 cycle shortens to 27 days and 27 days.',
            'The Double 11 / Singles’ Day cycle shortens to 27 days.',
            'The November 11 cycle shortens to 27 days.',
        ):
            with self.subTest(translated=translated):
                self.assertTrue(quantity_issues(source, translated, 'zh', 'en'))
        self.assertEqual(quantity_issues('双十一和双十一均为27天',
                         'Double 11 and Singles’ Day both last 27 days.', 'zh', 'en'), [])
        self.assertTrue(quantity_issues('双十一和双十一均为27天',
                        'Double 11 lasts 27 days.', 'zh', 'en'))

    def test_double_eleven_aliases_do_not_swallow_numbers_or_identifiers(self):
        for text in ('11', 'November 11', 'Double 110', 'Double 11.5', 'Double 11,5',
                     'Double 11%', 'Double 11 %', 'Double 11th', 'Double 11_extra',
                     'ModelDouble11', 'DoubleElevenModel', 'Singles Daylight',
                     '双十一百', '双110'):
            with self.subTest(text=text):
                self.assertNotIn(('shopping_event', 'double_eleven'), quantities(text, named_events=True))
        self.assertTrue(quantity_issues('11份订单', 'Double 11 orders', 'zh', 'en'))
        self.assertTrue(quantity_issues('十一份订单', 'Double Eleven orders', 'zh', 'en'))

    def test_named_events_are_opt_in_and_do_not_change_other_language_contracts(self):
        source = '双十一周期27天'
        french = 'La fête des célibataires dure 27 jours.'
        self.assertEqual(quantity_issues(source, french, 'zh', 'fr'), [])
        self.assertEqual(quantity_issues(french, source, 'fr', 'zh'), [])
        self.assertTrue(quantity_issues(source, french.replace('27', '28'), 'zh', 'fr'))
        self.assertTrue(quantity_issues(source, french + ' 11 jours.', 'zh', 'fr'))
        self.assertEqual(quantities(source), Counter({('number', Decimal(27)): 1}))
        self.assertEqual(quantities('Double 11 lasts 27 days.'),
                         Counter({('number', Decimal(11)): 1, ('number', Decimal(27)): 1}))
        # Language-agnostic callers retain their existing signatures and
        # checks; only explicit Chinese/English comparison opts in.
        for source_language, target_language in (('', ''), ('zh', ''), ('', 'en'), ('zh', 'fr')):
            with self.subTest(source_language=source_language, target_language=target_language):
                self.assertTrue(quantity_issues(source, 'Double 11 lasts 27 days.',
                                               source_language, target_language))
        self.assertEqual(quantity_issues(source, 'Double 11 lasts 27 days.', 'zh', 'en'), [])
        self.assertEqual(quantity_issues('Double 11 lasts 27 days.', source, 'en', 'zh'), [])

    def test_named_event_contract_survives_month_context_comparison(self):
        source = '9月讨论双十一周期27天'
        translated = 'In September, we discuss the Double 11 cycle lasting 27 days.'
        self.assertEqual(quantity_issues(source, translated, 'zh', 'en'), [])
        self.assertTrue(quantity_issues(source, translated.replace('Double 11', 'Double 12'), 'zh', 'en'))
        self.assertTrue(quantity_issues(source, translated.replace('September', 'October'), 'zh', 'en'))

    def test_ascii_basis_points_adjacent_to_non_latin_prose_keep_their_scale(self):
        for source in ('利差扩大171bp至2%。', '利差扩大171BPS至2%。',
                       'កើន171bpទៅ2%。', '利差扩大171 basis points至2%。'):
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, 'Spread rose 1.71 percentage points to 2%.'), [])
                for changed in ('Spread rose 1.72 percentage points to 2%.',
                                'Spread rose 171 percentage points to 2%.',
                                'Spread rose 1.71% to 2%.', 'Spread rose 170 bps to 2%.'):
                    self.assertTrue(quantity_issues(source, changed))
        self.assertEqual(quantity_issues('变化-5.25bp后', 'Changed -0.0525 percentage points.'), [])
        for suffix in ('bpm', 'bpword', 'bp2', 'bp_total', 'bpsunexpected', 'basis pointsExtra'):
            with self.subTest(suffix=suffix):
                self.assertTrue(quantity_issues('Value 171'+suffix, 'Value 1.71 percentage points.'))

    def test_reporting_periods_touching_han_keep_kind_year_and_value(self):
        for source, translated in [('本季Q1订单', 'Q1 orders'), ('本季2Q交付', '2Q deliveries'),
                                   ('本季H2订单', 'H2 orders'), ('本季1H交付', '1H deliveries'),
                                   ('预期Q3 2026交付', 'Q3 2026 deliveries'),
                                   ('预期2026 Q4交付', '2026 Q4 deliveries'),
                                   ('预期H1 2026交付', 'H1 2026 deliveries'),
                                   ('预期2026 H2交付', '2026 H2 deliveries')]:
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, translated), [])
                self.assertTrue(quantity_issues(source, translated.replace('Q', 'H') if 'Q' in translated
                                                else translated.replace('H', 'Q')))
                self.assertTrue(quantity_issues(source, 'Orders'))
        for value in ('AQ1', 'Q1X', '2QX', 'X2Q', 'AH2', 'H2X', '2HX', 'X2H'):
            with self.subTest(value=value):
                self.assertTrue(quantity_issues(value, 'Q1' if 'Q' in value else 'H2'))
        self.assertTrue(quantity_issues('预期Q1订单', 'Q2 orders'))
        self.assertTrue(quantity_issues('预期Q1 2026订单', 'Q1 2025 orders'))

    def test_singular_basis_point_abbreviation_is_exact_and_does_not_match_words(self):
        self.assertEqual(quantity_issues('收益率上升50个基点。', 'Yield rose 50 bp.'), [])
        self.assertEqual(quantity_issues('收益率上升50个基点。', 'Yield rose 50 bps.'), [])
        self.assertTrue(quantity_issues('收益率上升50个基点。', 'Yield rose 50 bpm.'))
        self.assertTrue(quantity_issues('收益率上升50个基点。', 'Yield rose 50%.' ))
        self.assertTrue(quantity_issues('收益率上升50个基点。', 'Yield rose 50 percentage points.'))

    def test_equivalent_currency_scale_and_dates(self):
        self.assertEqual(quantity_issues(
            'Cash reserves were USD 120 million and debt was USD 45 million on September 15, 2026.',
            '截至2026年9月15日，现金储备为1.2亿美元，债务为4500万美元。'), [])
        self.assertEqual(quantity_issues('截至2026年9月15日，现金储备为1.2亿美元。',
                                       'As of 15 September 2026, cash reserves were $120 million.'), [])

    def test_common_localized_currency_scales_are_equivalent(self):
        source = 'Revenue was USD 120 million.'
        for translated in (
            'Les revenus étaient de 120 millions de dollars.',
            'A receita foi de 120 milhões de USD.',
            'Los ingresos fueron de 120 millones de USD.',
            'Выручка составила 120 миллионов долларов.',
            'Die Einnahmen betrugen 120 Millionen USD.',
        ):
            with self.subTest(translated=translated):
                self.assertEqual(quantity_issues(source, translated), [])

    def test_localized_dates_percentages_and_percentage_points_are_equivalent(self):
        self.assertEqual(quantity_issues(
            'Revenue grew 12.5% on September 15, 2026.',
            'A receita cresceu 12,5 por cento em 15 de setembro de 2026.'), [])
        self.assertEqual(quantity_issues(
            'Margin rose 2.5 percentage points.',
            'La marge a augmenté de 2,5 points de pourcentage.'), [])

    def test_reject_order_of_magnitude_currency_or_missing_unit(self):
        for translated in ('现金储备为120万美元。', 'Cash reserves were $1.2 billion.',
                           'Cash reserves were EUR 120 million.', 'Cash reserves were 120 million.'):
            with self.subTest(translated=translated):
                self.assertTrue(quantity_issues('Cash reserves were USD 120 million.', translated))

    def test_rates_and_percentage_points_are_distinct(self):
        self.assertEqual(quantity_issues('Margin rose 2.5 percentage points to 18.5%.',
                                       '利润率上升2.5个百分点，达到百分之18.5。'), [])
        self.assertEqual(quantity_issues('Margin rose 2.5 percentage points.',
                                       'मार्जिन 2.5 प्रतिशत अंक बढ़ा।'), [])
        self.assertEqual(quantity_issues('Margin rose 2.5 percentage points.',
                                       'मार्जिन 2.5 प्रतिशत बिंदु बढ़ा।'), [])
        self.assertEqual(quantity_issues('Increased 25 basis points.',
                                       '25 आधार अंक बढ़ा।'), [])
        self.assertEqual(quantity_issues('Revenue was CNY 120 million.',
                                       'राजस्व 12 करोड़ युआन था।'), [])
        self.assertEqual(quantity_issues('New 15th Five-Year Plan.',
                                       'नई 15वीं पंचवर्षीय योजना।'), [])
        self.assertTrue(quantity_issues('Margin rose 2.5 percentage points to 18.5%.',
                                       '利润率上升2.5%，达到18.5%。'))
        self.assertEqual(quantity_issues('利润率为23%，收入同比下降4.7%。',
                                       'Margin was 23 per cent; revenue fell 4.7 percent year on year.'), [])

    def test_general_numbers_repetition_and_signs(self):
        self.assertTrue(quantity_issues('Revenue -5%, margin 8%.', 'Revenue 5%, margin 8%.'))
        self.assertTrue(quantity_issues('Revenue 5%, margin 8%.', 'Revenue 5%, margin 8%, growth 8%.'))
        self.assertTrue(quantity_issues('In 2026, 12 plants produced 450 cars.', 'In 2026, 11 plants produced 450 cars.'))
        self.assertEqual(quantity_issues('There were 1.2 million deliveries.', '交付120万件。'), [])

    def test_arabic_numerals_and_placeholders(self):
        self.assertEqual(quantity_issues('收入增长12.5%，利润率为8%。',
                                       'الإيرادات ارتفعت ١٢٫٥ في المائة والهامش ٨٪.'), [])
        self.assertEqual(quantity_issues('__KC_PH_001__ USD 45 million __HYMTPH_002__',
                                       '__KC_PH_001__ 4500万美元 __HYMTPH_002__'), [])

    def test_dates_reject_changed_or_invalid_date(self):
        self.assertEqual(quantity_issues('2026-09-15', '2026年9月15日'), [])
        self.assertTrue(quantity_issues('2026-09-15', '2026年9月16日'))
        self.assertTrue(quantity_issues('2026-09-15', '2026年2月30日'))

    def test_periods_and_basis_points(self):
        for source, translated in [('BIS Review September 2026', 'BIS评论2026年9月'),
                                   ('Q1 2026', '2026年第一季度'),
                                   ('fourth quarter of 2026', '2026年第4季度'),
                                   ('the first half of 2026', '2026年上半年'),
                                   ('H2 2026', '2026年下半年'),
                                   ('increased 25 basis points', '上升0.25个百分点')]:
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, translated), [])
        self.assertTrue(quantity_issues('increased 25 basis points', '上升25个百分点'))
        self.assertTrue(quantity_issues('Q1 2026', '2026年第二季度'))

    def test_finance_scale_abbreviations_and_yuan_aliases(self):
        for source, translated in [
            ('Revenue was RMB120mn.', '收入为1.2亿元。'),
            ('Revenue was USD1.2bn.', '收入为12亿美元。'),
            ('Revenue was $120mln.', '收入为1.2亿美元。'),
            ('Revenue was $1.2bln.', '收入为12亿美元。'),
            ('Revenue was 120 million Chinese yuan.', '收入为1.2亿元。'),
            ('Revenue was 120mn yuan.', '收入为1.2亿人民币元。'),
            ('Revenue was USD120million.', '收入为1.2亿美元。'),
        ]:
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, translated), [])
        # Unknown magnitude suffixes must not force a decimal to be consumed in
        # pieces, and recognized mn/bn must never be treated as equivalent.
        self.assertTrue(quantity_issues('USD1.2bn', 'USD1.2mn'))
        self.assertTrue(quantity_issues('USD1.2bn', 'USD1.2'))
        self.assertTrue(quantity_issues('RMB120mn', 'USD120mn'))

    def test_common_report_period_orderings_and_unicode_amounts(self):
        for source, translated in [
            ('2026 H1', '2026年上半年'),
            ('1H2026', '2026年上半年'),
            ('1Q2026', '2026年第一季度'),
            ('2Q 2026', '2026年第二季度'),
            ('Report for 2026-09', '2026年9月报告'),
            ('Report for 2026/09', '2026年9月报告'),
            ('USD ١٢٠٬٠٠٠٫٥٠', '120000.50美元'),
        ]:
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, translated), [])
        self.assertTrue(quantity_issues('2H2026', '2026年上半年'))
        self.assertTrue(quantity_issues('2026-09', '2026年10月'))

    def test_exact_chinese_blog_units_and_adjacent_periods(self):
        for source, translated in [('上行了50个基点', 'rose 50 basis points'),
                                   ('众议院概率超九成、参议院刚过六成', 'House probability above 90%, Senate just above 60%'),
                                   ('九成五', '95%'), ('共和党在9月才开始', 'Republicans only began in September'),
                                   ('百威亚太3Q26前瞻', 'Budweiser Asia Pacific 3Q26 preview'),
                                   ('2026年3月', 'March 2026'), ('9月', 'en septembre'),
                                   ('9月', 'im September'), ('9月', 'tháng 9')]:
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, translated), [])
        for source, translated in [('50个基点', '50 percentage points'), ('九成', '9%'),
                                   ('六成', '90%'), ('九成五', '90%'), ('9月', 'October'),
                                   ('3Q26前瞻', '4Q26 preview'), ('3Q26前瞻', '3Q27 preview')]:
            with self.subTest(source=source):
                self.assertTrue(quantity_issues(source, translated))
        self.assertEqual(quantity_issues('未来可能前进', 'It may march forward'), [])
        self.assertEqual(quantity_issues('9月可能上涨', 'It may rise in September'), [])
        self.assertEqual(quantity_issues('9月可能', 'September may'), [])
        self.assertEqual(quantity_issues('9月继续推进', 'March forward in September'), [])
        self.assertEqual(quantity_issues('5月', 'May'), [])
        self.assertEqual(quantity_issues('3月', 'in March'), [])
        self.assertEqual(quantity_issues('一成不变', 'unchanging'), [])
        self.assertEqual(quantity_issues('一成不變', 'unchanging'), [])
        self.assertTrue(quantity_issues('9月', 'en octobre'))

    def test_khmer_basis_points_preserve_exact_scale_and_unit(self):
        for source, translated in [('增加50个基点', 'កើនឡើង 50 ចំណុចមូលដ្ឋាន'),
                                   ('增加7个基点', 'កើនឡើង 7 ពិន្ទុមូលដ្ឋាន'),
                                   ('增加60个基点', 'កើនឡើង ៦០ ចំណុចមូលដ្ឋាន')]:
            with self.subTest(translated=translated):
                self.assertEqual(quantity_issues(source, translated, 'zh', 'km'), [])
        for damaged in ('កើនឡើង 50', 'កើនឡើង 5 ចំណុចមូលដ្ឋាន',
                        'កើនឡើង 50 ភាគរយ', 'កើនឡើង 50 ចំណុចភាគរយ',
                        'កើនឡើង 50 ចំណុចមូលដ្ឋាន 50 ចំណុចមូលដ្ឋាន'):
            with self.subTest(damaged=damaged):
                self.assertTrue(quantity_issues('增加50个基点', damaged, 'zh', 'km'))

    def test_natural_financial_paragraph(self):
        self.assertEqual(quantity_issues(
            'In the first half of 2026, revenue declined by 8.2% year on year, while operating profit increased by 6%. '
            'The operating margin was 18.5%, up 2.5 percentage points from a year earlier. '
            'As of September 15, 2026, cash reserves were USD 120 million and debt was USD 45 million.',
            '2026年上半年，营收同比下降8.2%，营业利润增长6%。营业利润率为18.5%，同比提高2.5个百分点。'
            '截至2026年9月15日，现金储备1.2亿美元，债务4500万美元。'), [])

    def test_abbreviated_report_periods_and_ordinal_plan_names(self):
        for source, translated in [
            ('3Q26 deliveries', '2026年第三季度交付量'),
            ('a 4Q26 catalyst', '2026年第四季度催化剂'),
            ('2Q26 recovery in 2Q', '2026年第二季度及第二季度复苏'),
            ('1H26 recurring net profit', '2026年上半年经常性净利润'),
            ("The Luxury Data Handbook: September '26", '奢侈品数据手册：2026年9月'),
            ('New 15th Five-Year Healthcare Plan', '新“十五五”医疗规划'),
            ('New _15th Five~Year” Healthcare Plan', '新“十五五”医疗规划'),
            ('the 15th Five-Year Plan', '第十五个五年规划'),
            ('Policy Tracker: Sep 18', '政策跟踪：9月18日'),
        ]:
            with self.subTest(source=source):
                self.assertEqual(quantity_issues(source, translated), [])
        for source, translated in [
            ('3Q26', '2026年第二季度'), ('4Q26', '2027年第四季度'),
            ('4Q26', '第四季度'), ('3Q', '2026年第三季度'),
            ('26 plants', '2026家工厂'), ('1H26', '2026年下半年'),
            ("September '26", '2026年10月'),
            ('15th Five-Year Plan', '“十四五”规划'),
        ]:
            with self.subTest(source=source, translated=translated):
                self.assertTrue(quantity_issues(source, translated))
        # Plan-specific support must not introduce a new quantity into existing
        # ordinary ordinal labels, whose localized words do not contain digits.
        self.assertEqual(quantity_issues('第一段研究报告', '첫 번째 연구 보고서'), [])
        self.assertEqual(quantity_issues('The first report', '第一份报告'), [])


if __name__ == '__main__':
    unittest.main()
