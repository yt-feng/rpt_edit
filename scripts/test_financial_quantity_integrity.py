import unittest

from financial_quantity_integrity import quantity_issues


class FinancialQuantityTests(unittest.TestCase):
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
