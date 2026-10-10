"""Saved title diagnosis reports gate causes without emitting source content."""
import copy
import json
import re
import unittest
from unittest.mock import patch

import saved_article_title_diagnostics as diagnostics
import wechat_title_optimizer as titles


SOURCE = 'UBS-AI product comparison-261007.pdf'
STATUS = {'original_filename': SOURCE, 'institution_name': '瑞银'}
FAITHFUL = '瑞银：产品交付节奏与市场需求变化'
NUMBERED = '瑞银：AI产品交付数量增长30%'


def observe(batches, body='', source_markdown='', status=None):
    status = status or STATUS
    candidates = [value for batch in reversed(batches) for value in batch]
    _, decision = titles.decide_filename_anchored_title(candidates, status['original_filename'],
        status['institution_name'], evidence_text=diagnostics.title_excerpt(body))
    before = copy.deepcopy((batches, decision))
    result = diagnostics.observe_saved_title_gates(status, body, source_markdown, batches, decision)
    assert (batches, decision) == before
    return result, decision


class SavedTitleDiagnosticTests(unittest.TestCase):
    def test_excerpt_is_byte_identical_to_previous_selector_preparation(self):
        body = '# private [marked](content)\n\n\nA  B *value*\ttext\n' + '正文段落。'*600
        original = re.sub(r'[ \t]+', ' ', re.sub(r'[#>*`!\\[\\]()]+', ' ', body))
        original = re.sub(r'\n{2,}', '\n', original).strip()[:2200]
        self.assertEqual(diagnostics.title_excerpt(body), original)

    def test_only_base_valid_anchor_has_number_outside_excerpt_without_authorizing_it(self):
        body = '产品交付节奏与市场需求出现变化。'*180 + 'AI产品交付数量增长30%。'
        result, decision = observe([[FAITHFUL, NUMBERED]], body, body)
        self.assertEqual(result['base_valid_unique_candidate_count'], 1)
        self.assertEqual(result['base_valid_hook_rejected_unique_count'], 1)
        self.assertEqual(result['hook_rejection_cleared_by_complete_article_count'], 1)
        self.assertEqual(result['hook_rejection_cleared_by_verified_source_count'], 1)
        self.assertEqual(result['anchor_origin'], 'saved_candidate')
        self.assertTrue(decision['needs_model_repair'])
        anchor = result['candidates'][1]
        self.assertTrue(anchor['is_selected_anchor']); self.assertTrue(anchor['meets_existing_anchor_coverage'])
        self.assertEqual(anchor['hook_support']['selector_excerpt']['numbers']['unsupported_count'], 1)
        self.assertEqual(anchor['hook_support']['complete_article']['numbers']['unsupported_count'], 0)
        self.assertFalse(anchor['hook_support']['selector_excerpt']['passes_existing_hook_gate'])
        self.assertEqual((result['provider_posts'], result['object_writes']), (0, 0))

    def test_source_only_support_and_truly_unsupported_claims_remain_observations(self):
        for source, expected in (('AI产品交付数量增长30%。', 1), ('AI产品交付数量保持稳定。', 0)):
            with self.subTest(source_support=expected):
                result, decision = observe([[FAITHFUL, NUMBERED]], '公司产品交付数量保持稳定。', source)
                self.assertEqual(result['hook_rejection_cleared_by_complete_article_count'], 0)
                self.assertEqual(result['hook_rejection_cleared_by_verified_source_count'], expected)
                self.assertTrue(decision['needs_model_repair'])

    def test_each_hook_kind_uses_existing_rules_including_indirect_contrast_evidence(self):
        candidate = '瑞银：AI麦肯锡交付数据反而增长30%'
        faithful = '瑞银：AI产品交付数量变化'
        for evidence, supported in (('', False), ('麦肯锡：交付增长30%，但产品需求仍有变化。', True)):
            result = diagnostics.hook_support(candidate, faithful, SOURCE, evidence)
            for kind in ('numbers', 'big_names', 'contrarian'):
                self.assertEqual(result[kind]['added_count'], 1)
                self.assertEqual(result[kind]['supported_count'], int(supported))
            self.assertEqual(result['passes_existing_hook_gate'],
                             titles.filename_title_additions_are_supported(candidate, faithful, SOURCE, evidence))
            self.assertEqual(result['passes_existing_hook_gate'], supported)

    def test_filename_support_is_separate_from_any_article_evidence(self):
        result = diagnostics.hook_support(NUMBERED, FAITHFUL, 'UBS-AI growth 30 percent-261007.pdf', '')
        self.assertEqual(result['numbers']['supported_count'], 1)
        self.assertTrue(result['passes_existing_hook_gate'])

    def test_required_terms_and_numbers_removed_by_length_are_distinguished(self):
        raw = '瑞银：'+ '产品交付需求结构与运营情况'*4+'AI增长30%'
        result, _ = observe([[raw]])
        row = result['candidates'][0]
        self.assertTrue(row['length_limit_changed_candidate'])
        self.assertEqual(row['raw_missing_required_count'], 0)
        self.assertEqual(row['full_clean_missing_required_count'], 0)
        self.assertEqual(row['clean_missing_required_count'], 1)
        self.assertEqual(row['normalization_removed_required_count'], 0)
        self.assertEqual(row['length_limit_removed_required_count'], 1)
        self.assertEqual(row['length_limit_removed_numeric_token_count'], 1)
        self.assertEqual(row['raw_to_clean_removed_numeric_token_count'], 1)

    def test_normalization_loss_is_not_misattributed_to_title_length(self):
        result, _ = observe([['瑞银：AI产品交付30%/产品需求与交付结构变化']])
        row = result['candidates'][0]
        self.assertEqual(row['normalization_removed_required_count'], 1)
        self.assertEqual(row['normalization_removed_numeric_token_count'], 1)
        self.assertEqual(row['length_limit_removed_required_count'], 0)

    def test_raw_missing_required_term_and_english_ratio_remain_identified(self):
        result, _ = observe([[FAITHFUL, '瑞银：Alpha Beta Gamma AI产出变化']])
        self.assertEqual(result['candidates'][0]['raw_missing_required_count'], 1)
        self.assertEqual(result['candidates'][0]['normalization_removed_required_count'], 0)
        self.assertIn('english_heavy_fragment', result['candidates'][1]['raw_quality']['codes'])

    def test_saved_order_and_short_fallback_origin_are_never_fabricated_as_model_evidence(self):
        result, _ = observe([[NUMBERED], [FAITHFUL]])
        self.assertEqual([(row['response_ordinal'], row['candidate_ordinal']) for row in result['candidates']], [(2, 1), (1, 1)])
        result, _ = observe([['AI']], status={'original_filename': 'UBS-产品交付数量与需求变化-261007.pdf', 'institution_name': '瑞银'})
        self.assertTrue(result['candidates'][0]['short_candidate_replaced_by_fallback'])
        self.assertEqual(result['anchor_origin'], 'filename_fallback')
        self.assertEqual(result['base_valid_saved_candidate_count'], 0)
        self.assertEqual(result['base_valid_fallback_substitution_count'], 1)

    def test_output_strings_are_strictly_allowlisted_even_for_unknown_quality_text(self):
        with patch.object(titles, 'title_quality_issues', return_value=['PRIVATE_ERROR_VALUE']):
            result, _ = observe([['PRIVATE_CANDIDATE_MARKER']], 'PRIVATE_BODY_MARKER', 'PRIVATE_SOURCE_MARKER')
        allowed = diagnostics.TITLE_REJECTION_REASONS | {
            diagnostics.POLICY, 'saved_candidate', 'filename_fallback', 'evidence_fallback'}
        def check(value):
            if isinstance(value, dict):
                for item in value.values(): check(item)
            elif isinstance(value, list):
                for item in value: check(item)
            elif isinstance(value, str): self.assertIn(value, allowed)
            else: self.assertIn(type(value), (int, bool))
        check(result)
        self.assertNotIn('PRIVATE', json.dumps(result))
        self.assertEqual(result['candidates'][0]['raw_quality']['unknown_code_count'], 1)

    def test_bounds_and_decision_binding_fail_with_fixed_codes(self):
        for batches in ([[]]*5, [['PRIVATE'*200]], [[str(index) for index in range(13)]]):
            with self.assertRaisesRegex(ValueError, '^saved_title_diagnostic_input_invalid$'):
                diagnostics.observe_saved_title_gates(STATUS, '', '', batches, {})
        with self.assertRaisesRegex(ValueError, '^saved_title_diagnostic_decision_invalid$'):
            diagnostics.observe_saved_title_gates(STATUS, '', '', [[FAITHFUL]], {})


if __name__ == '__main__':
    unittest.main()
