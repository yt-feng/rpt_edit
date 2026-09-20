import unittest

from financial_quantity_integrity import quantity_issues


class FinancialQuantityTests(unittest.TestCase):
    def test_equivalent_currency_scale_and_dates(self):
        self.assertEqual(quantity_issues(
            'Cash reserves were USD 120 million and debt was USD 45 million on September 15, 2026.',
            '截至2026年9月15日，现金储备为1.2亿美元，债务为4500万美元。'), [])
        self.assertEqual(quantity_issues('截至2026年9月15日，现金储备为1.2亿美元。',
                                       'As of 15 September 2026, cash reserves were $120 million.'), [])

    def test_reject_order_of_magnitude_currency_or_missing_unit(self):
        for translated in ('现金储备为120万美元。', 'Cash reserves were $1.2 billion.',
                           'Cash reserves were EUR 120 million.', 'Cash reserves were 120 million.'):
            with self.subTest(translated=translated):
                self.assertTrue(quantity_issues('Cash reserves were USD 120 million.', translated))

    def test_rates_and_percentage_points_are_distinct(self):
        self.assertEqual(quantity_issues('Margin rose 2.5 percentage points to 18.5%.',
                                       '利润率上升2.5个百分点，达到百分之18.5。'), [])
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

    def test_natural_financial_paragraph(self):
        self.assertEqual(quantity_issues(
            'In the first half of 2026, revenue declined by 8.2% year on year, while operating profit increased by 6%. '
            'The operating margin was 18.5%, up 2.5 percentage points from a year earlier. '
            'As of September 15, 2026, cash reserves were USD 120 million and debt was USD 45 million.',
            '2026年上半年，营收同比下降8.2%，营业利润增长6%。营业利润率为18.5%，同比提高2.5个百分点。'
            '截至2026年9月15日，现金储备1.2亿美元，债务4500万美元。'), [])


if __name__ == '__main__':
    unittest.main()
