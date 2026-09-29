"""Credential-free delegated approval boundary tests; never submit real reviews."""
import copy
from pathlib import Path
import unittest

from offline_translation import MODEL_ID, PROVIDER
from portal_extended_locales import ExpansionError
from review_portal_extended_handoff import producer_is_valid, review_identity


class DailyReviewTests(unittest.TestCase):
    def setUp(self):
        self.active = [{'generation': 'a'*64, 'candidates': {'fr':'b'*64, 'pt':'c'*64}}]
        self.batch = {'generation':'d'*64, 'candidates':{'fr':'e'*64}}
        self.receipt = {'producer':{'run_id':'123', 'attempt':'1', 'sha':'f'*40},
                        'batch':self.batch, 'source_day':'2026-09-25', 'pages_per_locale':1}
        self.assembly = {'schema_version':2, 'status':'assembled', 'detail_only':True,
                         'batches':self.active+[self.batch], 'locales':['fr','pt'],
                         'page_counts':{'fr':2, 'pt':1}, 'paid_provider_requests':0}
        ids = {'fr':'e'*64, 'pt':'c'*64}
        self.expected = {'commit_sha':'1'*40, 'static_tree_sha256':'2'*64, 'locales':'fr,pt',
                         'candidate_ids':ids, 'pages_per_locale':'1',
                         'candidate_specs':','.join(k+'='+v for k,v in ids.items())}
        self.identity = {'schema_version':1, 'operation':'migrate', 'commit_sha':'1'*40,
                         'static_tree_sha256':'2'*64, 'source_generation':'d'*64,
                         'locales':['fr','pt'], 'candidate_ids':ids, 'pages_per_locale':1,
                         'model':MODEL_ID, 'provider':PROVIDER, 'paid_provider_requests':0}
        self.run = {'id':123, 'run_attempt':1, 'head_sha':'f'*40, 'status':'completed',
                    'conclusion':'success', 'head_branch':'main', 'event':'workflow_run',
                    'path':'.github/workflows/portal-extended-locales-r2.yml',
                    'repository':{'full_name':'example/repo', 'private':False},
                    'head_repository':{'full_name':'example/repo'}}
        self.jobs = [{'name':'source', 'status':'completed', 'conclusion':'success',
                      'started_at':'2026-09-25T01:00:00Z', 'completed_at':'2026-09-25T01:10:00Z'},
                     {'name':'publication_handoff', 'status':'completed', 'conclusion':'success'}]

    def review(self, enabled='fr'):
        return review_identity(self.receipt, self.identity, self.assembly, self.active, enabled, self.expected)

    def test_exact_daily_candidate_preserves_other_approved_locales(self):
        variables = self.review()
        self.assertEqual(variables['PORTAL_EXTENDED_APPROVED_LOCALES'], 'fr,pt')
        self.assertEqual(variables['PORTAL_EXTENDED_APPROVED_CANDIDATE_IDS'], self.expected['candidate_specs'])
        self.assertEqual(variables['PORTAL_EXTENDED_APPROVED_STATIC_TREE'], '2'*64)
        self.assertEqual(variables['PORTAL_EXTENDED_LOCALES_ACTIVATION_APPROVED'], 'true')

    def test_first_time_locale_and_disabled_policy_cannot_be_approved(self):
        for enabled in ('', 'pt'):
            with self.subTest(enabled=enabled), self.assertRaises(ExpansionError): self.review(enabled)
        self.active = []
        with self.assertRaises(ExpansionError): self.review()

    def test_each_prepared_identity_field_is_exact(self):
        original = copy.deepcopy(self.identity)
        for field, value in {'schema_version':2, 'operation':'rehearse', 'commit_sha':'3'*40,
            'static_tree_sha256':'4'*64, 'source_generation':'5'*64, 'locales':['fr'],
            'candidate_ids':{'fr':'e'*64}, 'pages_per_locale':2, 'provider':'other',
            'model':'other', 'paid_provider_requests':1}.items():
            self.identity = {**original, field:value}
            with self.subTest(field=field), self.assertRaises(ExpansionError): self.review()

    def test_extra_missing_or_changed_approved_batches_are_rejected(self):
        original = copy.deepcopy(self.assembly)
        for batches in ([self.batch], self.active, self.active+[self.batch, {'generation':'6'*64,'candidates':{'de':'7'*64}}]):
            self.assembly = {**original, 'batches':batches}
            with self.assertRaises(ExpansionError): self.review()

    def test_incomplete_assembly_counts_and_candidate_spec_mismatch_are_rejected(self):
        original = copy.deepcopy(self.assembly)
        for change in ({'status':'incomplete'}, {'detail_only':False}, {'paid_provider_requests':1},
                       {'page_counts':{'fr':0,'pt':1}}, {'page_counts':{'fr':2}},
                       {'page_counts':{'fr':True,'pt':1}}, {'locales':['fr']}):
            self.assembly = {**original, **change}
            with self.subTest(change=change), self.assertRaises(ExpansionError): self.review()
        self.assembly = original
        self.expected['candidate_specs'] = 'fr='+'f'*64+',pt='+'c'*64
        with self.assertRaises(ExpansionError): self.review()

    def test_real_main_producer_can_finish_after_its_frozen_source_day(self):
        producer_is_valid(self.receipt, self.run, self.jobs, 'example/repo')
        # A slow locale may fail while other complete candidates are publishable.
        self.run['conclusion'] = 'failure'
        producer_is_valid(self.receipt, self.run, self.jobs, 'example/repo')

    def test_wrong_producer_attempt_branch_repository_or_cancelled_run_is_rejected(self):
        original = copy.deepcopy(self.run)
        for change in ({'id':124}, {'run_attempt':2}, {'head_sha':'8'*40}, {'status':'in_progress'},
                       {'conclusion':'cancelled'}, {'head_branch':'feature'}, {'event':'pull_request'},
                       {'path':'.github/workflows/other.yml'}, {'repository':{'full_name':'example/repo','private':True}},
                       {'head_repository':{'full_name':'other/repo'}}):
            with self.subTest(change=change), self.assertRaises(ExpansionError):
                producer_is_valid(self.receipt, {**original, **change}, self.jobs, 'example/repo')

    def test_historical_or_unfinished_handoff_cannot_be_automatically_reviewed(self):
        for index in (0,1):
            jobs = copy.deepcopy(self.jobs)
            jobs[index]['conclusion'] = 'skipped'
            with self.assertRaises(ExpansionError): producer_is_valid(self.receipt,self.run,jobs,'example/repo')
        self.receipt['source_day'] = '2026-09-24'
        with self.assertRaises(ExpansionError): producer_is_valid(self.receipt,self.run,self.jobs,'example/repo')

    def test_workflow_uses_normal_reviewer_gate_and_excludes_recovery(self):
        root = Path(__file__).resolve().parents[1]
        source = (root/'.github/workflows/neutral-edge-cutover.yml').read_text()
        review = source.split('  extended_daily_review:',1)[1].split('  extended_locales_approval:',1)[0]
        for text in ("inputs.extended_handoff != ''", "vars.PORTAL_EXTENDED_AUTO_REVIEW == 'true'",
                     "inputs.operation == 'migrate'", "inputs.translation_scope == 'incremental'",
                     'secrets.GH_DISPATCH_TOKEN', 'github.sha'):
            self.assertIn(text, review)
        approval = source.split('  extended_locales_approval:',1)[1].split('  cutover:',1)[0]
        self.assertIn('name: portal-extended-locales-production', approval)
        self.assertIn('Extended locale approval identity mismatch', approval)
        self.assertNotIn('extended_daily_review:', (root/'.github/workflows/neutral-locale-resume.yml').read_text())


if __name__ == '__main__':
    unittest.main()
