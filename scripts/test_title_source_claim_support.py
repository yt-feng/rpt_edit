"""No provider calls: numeric boundaries and bounded source claim support."""
from dataclasses import replace
import hashlib
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import title_source_claim_support as claims
import wechat_title_optimizer as titles


class QuantityTests(unittest.TestCase):
    def test_atomic_backoff_cannot_publish_a_dangling_numeric_introducer(self):
        source='GS-AMD AI revenue-261007.pdf'
        for stem in ('收入增至','收入达到','收入约'):
            raw='高盛：AMD AI产品'+stem+'12.5%以及相关变化'
            cut=titles.clean_filename_wechat_title(raw,'高盛',max_chars=raw.index('12.5')+2)
            self.assertIn('dangling_suffix',titles.title_quality_issues(cut,'高盛',source))
            _,decision=titles.decide_filename_anchored_title([raw],source,'高盛',max_chars=raw.index('12.5')+2)
            self.assertTrue(any('dangling_suffix' in row['reasons'] for row in decision['rejected_candidates']))

    def test_cut_never_splits_number_range_unit_scale_or_currency(self):
        for atom in ('12.5%', '150bn台', '$150bn', '30–40%', '2027年', '-12.5%', '3,500台', '(12.5%)',
                '-$30bn','−$30bn','+$30bn','($30bn)','- $30bn','( $30bn)'):
            value = '公司产品收入增长' + atom + '及相关产品变化'
            start = value.index(atom)
            for end in range(start + 1, start + len(atom)):
                with self.subTest(atom=atom, end=end):
                    cut = titles.fit_filename_title(value, end)
                    self.assertTrue(claims.boundary_observation(value, cut)['preserves_quantity_atoms'])
                    self.assertNotIn(atom[:1], cut)
            self.assertIn(atom, titles.fit_filename_title(value, start + len(atom)))

    def test_raw_to_clean_cannot_create_numeric_prefix_or_drop_unit(self):
        for full, shortened in [('增长12.5%', '增长12'), ('交付150bn台', '交付15'),
                ('收入30–40%', '收入30%'), ('下降-12.5%', '下降12.5%'), ('收入3,500台', '收入3'),
                ('收入(12.5%)','收入12.5%')]:
            self.assertFalse(claims.boundary_observation(full, shortened)['preserves_quantity_atoms'])
        result = claims.boundary_observation('增长12.5%，交付30台', '增长12.5%')
        self.assertTrue(result['preserves_quantity_atoms'])
        self.assertEqual(result['removed_whole_quantity_count'], 1)
        self.assertFalse(claims.boundary_observation('增长(12.5%', '增长(12.5%')['preserves_quantity_atoms'])

    def test_repeated_currency_and_unit_ranges_are_opaque_indivisible_atoms(self):
        for atom in ('$30-$40','$30–$40','30%-40%','$30bn-$40bn','30% to 40%'):
            value='AMD AI芯片目标价格为'+atom
            first=value.index(atom)
            self.assertEqual([m.group() for m in claims.quantities(value)],[atom])
            for end in range(first+1,len(value)):
                self.assertEqual(claims.safe_prefix_end(value,end),first,(atom,end))
            self.assertFalse(claims.boundary_observation(value,value)['preserves_quantity_atoms'])
            endpoint=value[:value.index('-',first)] if '-' in atom else value[:first]+'$30'
            self.assertFalse(claims.boundary_observation(value,endpoint)['preserves_quantity_atoms'])


class SourceClaimTests(unittest.TestCase):
    SOURCE = 'GS-Apple AI Revenue-261007.pdf'
    TITLE = '高盛：Apple AI收入增长12.5%'
    FAITHFUL = '高盛：Apple产品收入变化'

    def observe(self, text, candidate=None, context=None):
        return claims.contextual_numeric_support(candidate or self.TITLE, {'12.5'}, self.SOURCE, ['AI'],
            claims.source_context(self.SOURCE, text) if context is None else context)

    def test_source_only_complete_claim_passes_without_expanding_token_bag(self):
        text = 'Apple AI revenue grows 12.5%.'
        self.assertTrue(self.observe(text)['supported'])
        self.assertFalse(titles.filename_title_additions_are_supported(self.TITLE, self.FAITHFUL, self.SOURCE, '收入变化'))
        self.assertTrue(titles.filename_title_additions_are_supported(self.TITLE, self.FAITHFUL, self.SOURCE, '收入变化',
            source_context=claims.source_context(self.SOURCE, text), required_terms=['AI']))

    def test_same_number_wrong_entity_topic_metric_unit_state_period_does_not_pass(self):
        cases = ['Microsoft AI revenue grows 12.5%.', 'Apple GPU revenue grows 12.5%.',
            'Apple AI shipments grow 12.5%.', 'Apple AI revenue grows 12.5bp.',
            'Apple AI revenue falls 12.5%.', 'Apple AI revenue grows (12.5%).', 'Apple AI revenue does not grow 12.5%.',
            'Apple AI revenue is expected to grow 12.5%.', 'Apple AI revenue grows 12.5% in 2027年.',
            'Apple AI revenue grows 12.5%, versus 20%.',
            'Apple AI revenue changes. Microsoft AI revenue grows 12.5%.',
            'Apple says Microsoft AI revenue grows 12.5%.',
            'Apple and Samsung AI revenue grows 12.5%.',
            'Apple AI revenue. Growth of 12.5%.', 'Apple AI revenue\n增长12.5%。',
            '| Apple AI revenue | 12.5% |', 'Apple AI revenue ' + ('extra ' * 100) + 'grows 12.5%.']
        for text in cases:
            with self.subTest(text=text):
                self.assertFalse(self.observe(text)['supported'])

    def test_missing_or_forged_context_fails_closed(self):
        good = claims.source_context(self.SOURCE, 'Apple AI revenue grows 12.5%.')
        for context in ({'text':good.text}, replace(good, sha256='0'*64), replace(good, source_filename='other.pdf')):
            self.assertFalse(self.observe('', context=context)['supported'])
        self.assertIsNone(claims.source_context(self.SOURCE, good.text, expected_sha256='0'*64))
        self.assertFalse(claims.contextual_numeric_support(self.TITLE, {'12.5'}, self.SOURCE, ['AI'], None)['supported'])

    def test_bare_number_generic_topic_and_alias_cannot_self_authorize(self):
        for title in ('高盛：Apple AI收入增长12.5', '高盛：AI收入增长12.5%', '高盛：苹果AI收入增长12.5%'):
            self.assertFalse(self.observe('Apple AI revenue grows 12.5%.', candidate=title)['supported'])
        self.assertFalse(claims.contextual_numeric_support(self.TITLE, {'12.5'}, self.SOURCE, [],
            claims.source_context(self.SOURCE, 'Apple AI revenue grows 12.5%.'))['supported'])
        for candidate,source in [('Revenue AI收入增长30%','Revenue AI grows 30%.'),
                ('Product AI收入增长30%','Product AI revenue grows 30%.')]:
            filename=candidate.split(' ')[0]+' AI outlook.pdf'
            result=claims.contextual_numeric_support(candidate,{'30'},filename,['AI'],claims.source_context(filename,source))
            self.assertEqual(result['subject_anchor_count'],0)
            self.assertFalse(result['supported'])

    def test_multiclause_number_belongs_only_to_its_own_subject(self):
        filename='GS-Apple Watch AMD Instinct AI Revenue-261007.pdf'
        candidate='高盛：Apple Watch AI产品变化，AMD Instinct AI收入增长12.5%'
        for text, expected in [('AMD Instinct AI revenue grows 12.5%.',True),
                ('Apple Watch AI revenue grows 12.5%.',False)]:
            result=claims.contextual_numeric_support(candidate,{'12.5'},filename,['AI'],claims.source_context(filename,text))
            self.assertEqual(result['supported'],expected)

    def test_direct_subject_relation_rejects_lowercase_third_parties_and_attribution(self):
        filename='AMD AI revenue outlook.pdf'
        candidate='AMD AI收入增长30%'
        for source in ['AMD says apple AI revenue grows 30%.','amd says apple AI revenue grows 30%.',
                'AMD reports apple AI revenue grows 30%.','AMD competes with apple AI revenue grows 30%.',
                'AMD customer apple AI revenue grows 30%.','According to AMD apple AI revenue grows 30%.',
                'AMD AI revenue for apple grows 30%.','AMD AI revenue grows 30% for apple.']:
            result=claims.contextual_numeric_support(candidate,{'30'},filename,['AI'],claims.source_context(filename,source))
            self.assertFalse(result['supported'],source)
        for source in ['AMD AI revenue grows 30%.',"AMD's AI revenue grows 30%."]:
            self.assertTrue(claims.contextual_numeric_support(candidate,{'30'},filename,['AI'],
                claims.source_context(filename,source))['supported'],source)
        filename='AMD Apple AI revenue outlook.pdf'
        result=claims.contextual_numeric_support('AMD提到Apple AI收入增长30%',{'30'},filename,['AI'],
            claims.source_context(filename,'AMD AI revenue grows 30%.'))
        self.assertFalse(result['candidate_direct_claim'])
        self.assertFalse(result['supported'])

    def test_uncovered_number_and_other_added_hooks_are_not_authorized(self):
        context=claims.source_context(self.SOURCE, 'Apple AI revenue grows 12.5%.')
        self.assertFalse(claims.contextual_numeric_support(self.TITLE, {'12.5','900'}, self.SOURCE, ['AI'], context)['supported'])
        self.assertFalse(titles.filename_title_additions_are_supported(self.TITLE+'反而', self.FAITHFUL,
            self.SOURCE, '', source_context=context, required_terms=['AI']))

    def test_explicit_currency_scale_is_supported_but_bare_scale_is_not(self):
        for atom, expected in [('$30bn',True),('US$30bn',True),('30bn',False),('$30mn',True)]:
            result=claims.contextual_numeric_support('高盛：Apple AI收入增长'+atom, {'30'}, self.SOURCE, ['AI'],
                claims.source_context(self.SOURCE,'Apple AI revenue grows '+atom+'.'))
            self.assertEqual(result['supported'],expected,atom)
        self.assertFalse(claims.contextual_numeric_support('高盛：Apple AI收入增长$30bn', {'30'}, self.SOURCE, ['AI'],
            claims.source_context(self.SOURCE,'Apple AI revenue grows $30mn.'))['supported'])

    def test_currency_prefix_sign_is_part_of_identity_not_ignored(self):
        filename='AMD AI revenue outlook.pdf'
        for atom in ('-$30bn','−$30bn','($30bn)','- $30bn','( $30bn)'):
            candidate='AMD AI收入为'+atom
            for source_atom, expected in [('$30bn',False),(atom,True)]:
                with self.subTest(atom=atom,source=source_atom):
                    self.assertEqual(claims.contextual_numeric_support(candidate,{'30'},filename,['AI'],
                        claims.source_context(filename,'AMD AI revenue is '+source_atom+'.'))['supported'],expected)
            self.assertFalse(claims.boundary_observation(candidate,candidate.replace(atom,'$30bn'))['preserves_quantity_atoms'])
        for atom in ('-$-30bn','(+$30bn)','(-$30bn)'):
            self.assertFalse(claims.contextual_numeric_support('AMD AI收入为'+atom,{'30'},filename,['AI'],
                claims.source_context(filename,'AMD AI revenue is '+atom+'.'))['supported'])

    def test_modal_period_and_bound_fault_probes_remain_unready(self):
        filename='AMD AI revenue outlook.pdf'
        pairs=[('AMD AI收入增长30%','AMD AI revenue may grow 30%.'),
            ('AMD AI收入增长30%','AMD AI revenue could grow 30%.'),
            ('AMD AI收入增长30%',"AMD AI revenue isn't growing 30%."),
            ('AMD AI收入增长30%','AMD AI revenue would grow 30%.'),
            ('AMD AI收入增长30%','AMD AI revenue grows 30% if approved.'),
            ('AMD AI收入增长30%','AMD AI revenue growth of 30% is false.'),
            ('AMD AI收入在2027年 Q4增长30%','AMD AI revenue grows 30% in 2027年 Q3.'),
            ('AMD AI收入增长30% FY2027','AMD AI revenue grows 30% FY2026.'),
            ('AMD AI收入增长30% 1Q27','AMD AI revenue grows 30% 1Q26.'),
            ('AMD AI收入增长超过30%','AMD AI revenue grows about 30%.'),
            ('AMD AI收入增长30%','AMD AI revenue growth is below 30%.')]
        for candidate,source in pairs:
            with self.subTest(candidate=candidate,source=source):
                self.assertFalse(claims.contextual_numeric_support(candidate,{'30'},filename,['AI'],
                    claims.source_context(filename,source))['supported'])
        candidate='AMD AI收入增长30% FY2027'
        self.assertTrue(claims.contextual_numeric_support(candidate,{'30'},filename,['AI'],
            claims.source_context(filename,'AMD AI revenue grows 30% FY2027.'))['supported'])

    def test_selector_keeps_faithful_order_and_gates_with_original_source(self):
        candidates = [self.FAITHFUL, self.TITLE]
        _, before = titles.decide_filename_anchored_title(candidates, self.SOURCE, '高盛', evidence_text='收入变化')
        selected, after = titles.decide_filename_anchored_title(candidates, self.SOURCE, '高盛', evidence_text='收入变化',
            source_context=claims.source_context(self.SOURCE, 'Apple AI revenue grows 12.5%.'))
        self.assertTrue(before['needs_model_repair'])
        self.assertEqual(selected, self.TITLE)
        self.assertFalse(after['needs_model_repair'])
        self.assertEqual(after['raw_candidates'], candidates)
        self.assertEqual(after['faithful_candidate_missing_terms'], ['AI'])

    def test_future_producer_and_contract_use_same_source_helper_without_extra_request(self):
        import pdf_to_xhs_batch as producer
        import recover_report_articles as recovery
        args=SimpleNamespace(wechat_title_refine=True, checkpoint_single_request=True)
        request=lambda *a, **k: '{"titles":["'+self.FAITHFUL+'","'+self.TITLE+'"]}'
        with patch.object(producer, 'call_deepseek', side_effect=request) as call:
            selected, decision=producer.wechat_title_from_filename(self.SOURCE,'收入变化','高盛',args,
                source_text='Apple AI revenue grows 12.5%.')
        self.assertEqual(selected,self.TITLE)
        self.assertFalse(decision['repair_attempted'])
        self.assertEqual(call.call_count,1)
        self.assertIn('title_source_claim_support.py',Path(recovery.__file__).read_text())
        self.assertIn('source_text=source_text',Path(producer.__file__).read_text())


if __name__ == '__main__':
    unittest.main()
