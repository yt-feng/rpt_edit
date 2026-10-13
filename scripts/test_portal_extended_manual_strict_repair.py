"""Bounded manual staging and subsequent serialized accepted-ledger adoption."""
import copy
import io
import json
from contextlib import redirect_stdout
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import test_portal_extended_quality_recovery as fixtures
from portal_extended_repair_contract import MANUAL_STRICT_RETRY
from portal_extended_locales import ExpansionError, stable_bytes, digest
from portal_extended_continuation import queue
from portal_extended_incremental import read_state, write_state
from portal_extended_quality import debt_rows


class ManualStrictTests(unittest.TestCase):
    def setUp(self):
        # One blocked structural unit, matching the production replay target.
        from test_portal_extended_locales import FakeTranslator
        class OneRejected(FakeTranslator):
            def translate(self, text, target, source=None, *, markdown=True):
                if 'Revenue' in text:
                    from offline_translation import OfflineTranslationValidationError
                    raise OfflineTranslationValidationError('Hy-MT2 placeholder validation failed')
                return super().translate(text,target,source,markdown=markdown)
        with patch.object(fixtures,'StructuralRejected',OneRejected):
            fixtures.RecoveryTests.setUp(self)
    quality = fixtures.RecoveryTests.quality
    numeric_fallback = False
    history_api = fixtures.RecoveryTests.history_api
    successful_history_api = fixtures.RecoveryTests.successful_history_api
    select = fixtures.RecoveryTests.select
    finish = fixtures.RecoveryTests.finish

    def request(self):
        unit = sorted(self.f.old['source_fallbacks'])[0]
        return {**self.f.request, 'policy':self.pipeline.policy,
                'validator_revision':self.pipeline.revision, 'locale':self.locale,
                'retry_policy':MANUAL_STRICT_RETRY, 'units':[unit],
                'unit_modes':{unit:'fresh-authorized'}}

    def operation(self, operation, request=None, *, translator=None, stage=True, seconds=900):
        args = SimpleNamespace(operation=operation, generation=self.generation, locale=self.locale,
            checkpoint=self.f.root/'manual.json', corpus=self.f.root/'manual-source.json',
            output=self.f.root/'manual-out', github_output=None, seconds=seconds, stage_only=stage)
        output=io.StringIO()
        with redirect_stdout(output), patch('offline_translation.OfflineTranslator',
                return_value=translator or fixtures.fixtures.RepairTranslator()) as factory, \
             patch('portal_extended_repair_cache.CacheFirstTranslator',side_effect=lambda translator:translator):
            self.pipeline.run(args, request or self.request(), fixtures.fixtures.OWNER,
                store=self.store, repository=fixtures.fixtures.REPOSITORY, api=self.f.api, manual_strict=True)
        return json.loads(output.getvalue()),factory

    def test_stage_changes_only_immutable_evidence_then_auto_adopts_latest_memo(self):
        request=self.request(); selected=request['units'][0]
        before_queue=copy.deepcopy(queue(self.store,self.locale))
        before_memo=copy.deepcopy(read_state(self.store,'memo',self.locale))
        before_debt=copy.deepcopy(debt_rows(self.store,self.locale))
        before_completed=copy.deepcopy(read_state(self.store,'completed',self.locale,fixtures.fixtures.DAY))
        self.operation('prepare'); self.operation('restore')
        result,factory=self.operation('build')
        factory.assert_called_once_with(validation_attempts=3,quantity_policy='advisory')
        self.assertEqual(result['accepted_units'],1)
        result,_=self.operation('persist')
        self.assertTrue(result['prepared_only']); self.assertEqual(result['mutable_production_writes'],0)
        self.assertEqual(queue(self.store,self.locale),before_queue)
        self.assertEqual(read_state(self.store,'memo',self.locale),before_memo)
        self.assertEqual(debt_rows(self.store,self.locale),before_debt)
        self.assertEqual(read_state(self.store,'completed',self.locale,fixtures.fixtures.DAY),before_completed)
        proof=self.pipeline.verify_proof(self.store,result['proof_sha256'],self.generation)
        self.assertEqual(proof['delta']['accepted_units'],[selected])
        # A distinct later-generation memo must survive adoption unchanged
        # except for this one validated target. The staged memo is now stale.
        advanced=copy.deepcopy(self.f.old)
        later_generation='f'*64
        advanced['source_generation']=later_generation
        unrelated=self.pipeline.units.unit_key('Unrelated detail','en',False)
        advanced['rows'][unrelated]={'source':'Unrelated detail','language':'en','text':'Détail indépendant'}
        raw=stable_bytes(advanced); checksum=digest(raw)
        self.store._put(self.store.checkpoint_object_key(self.locale,later_generation,checksum),raw,
                        metadata={'kind':'translation-checkpoint'})
        write_state(self.store,'memo',self.locale,{'generation':later_generation,'sha256':checksum})
        current=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError,'latest memo advanced'):
            self.pipeline.commit_prepared(self.store,result['proof_sha256'])
        self.assertEqual(self.client.objects,current)
        jobs,blocked=self.select();self.assertFalse(blocked)
        plan=fixtures.recovery.read_plan(self.store,jobs[0]['quality_repair'])
        self.assertNotIn('retry_policy',plan['request'])
        self.assertEqual(plan['request']['unit_modes'][selected],'accepted-ledger')
        self.assertFalse(plan['requires_engine'])
        self.assertNotEqual(self.pipeline.repair_key(self.store,request),
                            self.pipeline.repair_key(self.store,plan['request']))
        args=SimpleNamespace(operation='restore',generation=self.generation,locale=self.locale,
            checkpoint=self.f.root/'adopt.json',corpus=self.f.root/'adopt-source.json',
            output=self.f.root/'adopt-out',github_output=None,seconds=30,requires_engine=False)
        with patch('offline_translation.OfflineTranslator',side_effect=AssertionError('adoption inferred')):
            for operation in ('restore','build','persist'):
                args.operation=operation
                with redirect_stdout(io.StringIO()):
                    self.pipeline.run(args,plan['request'],fixtures.fixtures.OWNER,store=self.store,
                        repository=fixtures.fixtures.REPOSITORY,api=self.f.api)
        self.assertEqual(debt_rows(self.store,self.locale),{})
        memo=read_state(self.store,'memo',self.locale)
        self.assertEqual(memo['generation'],later_generation)
        merged=json.loads(self.store._get(self.store.checkpoint_object_key(self.locale,later_generation,memo['sha256']),maximum=2**23))
        self.assertEqual(merged['rows'][unrelated],advanced['rows'][unrelated])
        self.assertIn(selected,merged['rows']);self.assertNotIn(selected,merged.get('source_fallbacks',{}))
        row=queue(self.store,self.locale)[self.generation]
        self.assertNotEqual(row['snapshot']['candidate_id'],request['candidate_id'])

    def test_overbudget_and_extra_units_reject_without_write(self):
        before=copy.deepcopy(self.client.objects)
        with self.assertRaises(ExpansionError):self.operation('prepare',seconds=901)
        request=self.request();request['units']=sorted([*self.f.old['source_fallbacks'],'f'*64])
        request['unit_modes']={unit:'fresh-authorized' for unit in request['units']}
        with self.assertRaises(ExpansionError):self.operation('prepare',request)
        self.assertEqual(self.client.objects,before)

    def test_terminal_and_unknown_ledger_cannot_be_reopened(self):
        request=self.request();unit=request['units'][0]
        required=self.pipeline.units.required_units(self.f.corpus)
        self.pipeline.units.attempt_unit(self.store,unit,required[unit],fixtures.fixtures.ORIGINAL,
            fixtures.fixtures.RepairTranslator(terminal=required[unit]['source']))
        before=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError,'terminal or unknown'):self.operation('prepare')
        self.assertEqual(self.client.objects,before)
        del self.client.objects[self.pipeline.units.ledger_key(self.store,unit,'outcome.json')]
        before=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError,'terminal or unknown'):self.operation('prepare')
        self.assertEqual(self.client.objects,before)

    def test_failed_selected_translation_does_not_stage_or_mutate_candidate(self):
        self.operation('prepare');self.operation('restore')
        source=self.f.old['source_fallbacks'][self.request()['units'][0]]['source']
        with self.assertRaisesRegex(ExpansionError,'not accepted'):
            self.operation('build',translator=fixtures.fixtures.RepairTranslator(terminal=source))
        self.assertIsNone(self.pipeline.prepared_proof(self.store,self.request()))
        self.assertEqual(queue(self.store,self.locale)[self.generation],self.f.before)

    def test_automatic_caller_cannot_activate_manual_retry_policy(self):
        with self.assertRaisesRegex(ExpansionError,'explicit reviewed dispatcher'):
            self.pipeline.run(self.f.args,self.request(),fixtures.fixtures.OWNER,
                store=self.store,repository=fixtures.fixtures.REPOSITORY,api=self.f.api)


if __name__=='__main__':unittest.main()
