"""Real private source/checkpoint/render/queue contracts; no model or network."""
import copy
import io
import json
import os
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import test_portal_extended_french_repair as fixtures
import portal_extended_quality_recovery as recovery
from portal_extended_french_repair import RepairPipeline
from portal_extended_repair_contract import quality_contract
from portal_extended_quality import record_quality, debt_rows
from portal_extended_continuation import queue, save_queue
from portal_extended_incremental import read_state, write_state, state_key, remember_checkpoint, remember_candidate
from portal_extended_locales import ExpansionError, stable_bytes, digest
from build_portal_extended_locales import build
from repair_portal_french_source_fallback import RepairEngine


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.IntegrationTests('test_real_restore_build_persist_preserves_origin_other_locale_and_counters')
        self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.store, self.client = self.f.store, self.f.client
        self.locale, self.generation = 'fr', self.f.generation
        self.pipeline = RepairPipeline(quality_contract('fr'))
        self.quality()

    def quality(self):
        row = queue(self.store, self.locale)[self.generation]
        return record_quality(self.store, self.locale, self.generation, row['snapshot']['candidate_id'],
                              manifest_sha256=row['snapshot']['manifest_sha256'])

    def history_api(self, path):
        if '/runs/1/' in path: return self.f.api(path)
        run_id = path.split('/runs/')[1].split('/')[0]
        run = {**self.f.run_record, 'id':int(run_id), 'head_sha':fixtures.OWNER['sha']}
        jobs = [{**item,'run_id':int(run_id),'head_sha':fixtures.OWNER['sha']} for item in self.f.jobs]
        if run_id == '2': jobs[1]['conclusion']='failure'
        return {'total_count':len(jobs),'jobs':jobs} if '/jobs?' in path else run

    def successful_history_api(self, path):
        value=self.history_api(path)
        if '/jobs?' in path:
            for job in value['jobs']:job['conclusion']='success'
        return value

    def select(self):
        return recovery.prepare(self.store, (self.locale,), fixtures.OWNER, fixtures.REPOSITORY, self.successful_history_api)

    def finish(self, job, translator=None):
        plan = recovery.read_plan(self.store, job['quality_repair'])
        args = SimpleNamespace(operation='restore', generation=self.generation, locale=self.locale,
            checkpoint=self.f.root/'quality.json', corpus=self.f.root/'corpus.json', output=self.f.root/'quality-out',
            github_output=None, seconds=30, requires_engine=plan['requires_engine'])
        def forbidden(path): raise AssertionError('No source refresh/authentication during locale job')
        with redirect_stdout(io.StringIO()):
            self.pipeline.run(args, plan['request'], fixtures.OWNER, store=self.store, repository=fixtures.REPOSITORY, api=forbidden)
        with __import__('tempfile').TemporaryDirectory() as temp:
            corpus, old, candidate, _, _, _ = self.pipeline.frozen(self.store,self.generation,plan['request'],Path(temp))
            checkpoint=Path(temp)/'new.json'
            tr=translator or fixtures.RepairTranslator(terminal='Profit')
            proof=self.pipeline.units.rebuild(self.store, corpus,old,candidate,args.output,checkpoint,
                plan['request'], fixtures.OWNER,tr,seconds=30)
            args.checkpoint.write_bytes(checkpoint.read_bytes())
            (args.output.parent/'fr-source-fallback-repair-proof.json').write_bytes(stable_bytes(proof))
        args.operation='persist'
        with redirect_stdout(io.StringIO()):
            self.pipeline.run(args,plan['request'],fixtures.OWNER,store=self.store,repository=fixtures.REPOSITORY,api=forbidden)
        return proof

    def test_two_pages_two_fallbacks_partial_success_durable_then_terminal_no_loop(self):
        jobs, blocked=self.select(); self.assertEqual(blocked,[]); self.assertEqual(len(jobs),1)
        origin=copy.deepcopy(self.f.origin); de=copy.deepcopy(queue(self.store,'de'))
        proof=self.finish(jobs[0]); self.assertEqual(proof['fallbacks_before'],2); self.assertEqual(proof['fallbacks_after'],1)
        result=recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.OWNER)
        self.assertTrue(result['continue']); self.assertEqual(result['accepted_units'],1)
        self.assertEqual(result['still_fallback_terminal_units'],1)
        self.assertEqual(result['fresh_inference_unit_attempts'],2)
        self.assertEqual(queue(self.store,'de'),de); self.assertEqual(self.f.origin,origin)
        jobs, blocked=self.select(); self.assertEqual(jobs,[])
        row=read_state(self.store,'quality-recovery-status','fr')['generations'][self.generation]
        self.assertEqual(row['code'],'no_retryable_units'); self.assertEqual(row['terminal_units'],1)
        self.assertEqual(len(debt_rows(self.store,'fr')),1)

    def test_full_recovery_removes_debt_and_no_spurious_followup(self):
        jobs,_=self.select(); self.finish(jobs[0],fixtures.RepairTranslator())
        self.assertEqual(debt_rows(self.store,'fr'),{})
        summary=recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.OWNER)
        self.assertEqual(summary['accepted_units'],2); self.assertFalse(summary['continue'])

    def test_snapshot_ack_recovered_only_from_exact_immutable_old_result(self):
        old=copy.deepcopy(queue(self.store,'fr')[self.generation]);save_queue(self.store,'fr',{})
        jobs,blocked=self.select();self.assertEqual(blocked,[]);self.assertEqual(len(jobs),1)
        self.assertEqual(queue(self.store,'fr')[self.generation],old)

    def test_ack_without_exact_result_stays_debt_no_queue_claim(self):
        save_queue(self.store,'fr',{})
        for key in list(self.client.objects):
            if '/continuation-results/' in key: del self.client.objects[key]
        jobs,blocked=self.select();self.assertEqual(jobs,[])
        self.assertEqual(blocked[0]['code'],'historical_result_not_unique')
        self.assertEqual(queue(self.store,'fr'),{});self.assertTrue(debt_rows(self.store,'fr'))

    def test_two_immutable_results_cannot_guess_old_continuation_count(self):
        row=copy.deepcopy(queue(self.store,'fr')[self.generation]);row['continuations']=1
        key=self.store.key('incremental','continuation-results',self.generation,'fr',digest(stable_bytes(row))+'.json')
        self.store._put(key,stable_bytes(row),metadata={'kind':'test'})
        save_queue(self.store,'fr',{})
        jobs,blocked=self.select();self.assertFalse(jobs);self.assertEqual(blocked[0]['code'],'historical_result_not_unique')
        self.assertEqual(queue(self.store,'fr'),{})

    def test_actual_ack_retains_full_repaired_row_for_a_later_bounded_batch(self):
        from portal_extended_continuation import acknowledge_published
        with patch.object(recovery,'MAX_UNITS_PER_SCAN',1): jobs,_=self.select()
        self.finish(jobs[0],fixtures.RepairTranslator())
        before=copy.deepcopy(queue(self.store,'fr')[self.generation])
        self.assertIn('source_repair_sha256',before)
        acknowledge_published(self.store,('fr',),[{'generation':self.generation,
            'candidates':{'fr':before['snapshot']['candidate_id']}}])
        self.assertEqual(queue(self.store,'fr'),{})
        def successful(path):
            value=self.history_api(path)
            if '/jobs?' in path:
                for job in value['jobs']:job['conclusion']='success'
            return value
        jobs,blocked=recovery.prepare(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,successful)
        self.assertEqual(blocked,[]);self.assertEqual(len(jobs),1)
        self.assertEqual(queue(self.store,'fr')[self.generation],before)
        self.assertEqual(len(recovery.read_plan(self.store,jobs[0]['quality_repair'])['request']['units']),1)

    def test_repaired_ack_anchor_does_not_accept_failed_repair_producer(self):
        from portal_extended_continuation import acknowledge_published
        with patch.object(recovery,'MAX_UNITS_PER_SCAN',1):jobs,_=self.select()
        self.finish(jobs[0],fixtures.RepairTranslator())
        row=queue(self.store,'fr')[self.generation]
        acknowledge_published(self.store,('fr',),[{'generation':self.generation,
            'candidates':{'fr':row['snapshot']['candidate_id']}}])
        jobs,blocked=recovery.prepare(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,self.history_api)
        self.assertFalse(jobs);self.assertEqual(blocked[0]['code'],'historical_evidence_unverifiable')
        self.assertEqual(queue(self.store,'fr'),{})

    def test_advanced_completed_page_never_restores_ack(self):
        save_queue(self.store,'fr',{})
        pages=read_state(self.store,'completed','fr',fixtures.DAY)['pages']
        pages[fixtures.URL]['generation']='d'*64
        write_state(self.store,'completed','fr',{'pages':pages},fixtures.DAY)
        jobs,blocked=self.select();self.assertEqual(jobs,[]);self.assertEqual(blocked[0]['code'],'completed_page_receipt_advanced')
        self.assertEqual(queue(self.store,'fr'),{})

    def test_existing_noncomplete_not_reconstructed_or_reclaimed(self):
        rows=queue(self.store,'fr');rows[self.generation]['status']='blocked';save_queue(self.store,'fr',rows)
        before=copy.deepcopy(self.client.objects);jobs,blocked=self.select()
        self.assertEqual(jobs,[])
        for key,value in before.items():self.assertEqual(self.client.objects[key],value)
        self.assertTrue(all('/quality-recovery-scheduler/' in key for key in set(self.client.objects)-set(before)))

    def test_unknown_legacy_unit_skipped_other_unit_progresses(self):
        required=self.pipeline.units.required_units(self.f.corpus)
        unit=self.f.request['units'][0]; old=RepairEngine()
        old.create_record(self.store,old.ledger_key(self.store,unit,'started.json'),
            {**old.claim_contract(unit,required[unit]),'producer':fixtures.ORIGINAL})
        jobs,_=self.select();plan=recovery.read_plan(self.store,jobs[0]['quality_repair'])
        self.assertNotIn(unit,plan['request']['units']);self.assertEqual(plan['selection']['unresolved_units'],1)
        self.finish(jobs[0],fixtures.RepairTranslator())
        self.assertEqual(self.pipeline.units.ledger_outcome(self.store,unit,required[unit]),(None,None))

    def test_cache_only_complete_candidate_rebuild_uses_no_fresh_calls(self):
        class Cached(fixtures.RepairTranslator):
            def cached_translation(self,text,target,source,*,markdown):
                return text.replace('Revenue','Chiffre d’affaires').replace('Profit','Bénéfice')
            def translate(self,*args,**kwargs): raise AssertionError('cache recovery opened inference')
        jobs,_=self.select();proof=self.finish(jobs[0],Cached())
        self.assertEqual(proof['unit_attempt_modes'],{'accepted-ledger':0,'cache-only':2,'fresh-inference':0})

    def test_no_prepared_receipt_no_followup(self):
        jobs,_=self.select();summary=recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.OWNER)
        self.assertFalse(summary['continue']);self.assertEqual(summary['blocked_plans'],1)

    def test_wrong_followup_owner_rejected(self):
        jobs,_=self.select()
        with self.assertRaisesRegex(ExpansionError,'owner_mismatch'):
            recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.ORIGINAL)

    def test_changed_debt_proof_cannot_create_unit_claim(self):
        debt=debt_rows(self.store,'fr')[self.generation]
        from portal_extended_quality import proof_key
        key=proof_key(self.store,debt['proof_sha256'])
        raw=json.loads(self.client.objects[key]['body']);raw['source_sha256']='0'*64
        self.store._put(key,stable_bytes(raw),metadata={'kind':'test'})
        jobs,blocked=self.select();self.assertEqual(jobs,[]);self.assertEqual(blocked[0]['code'],'debt_proof_checksum_invalid')
        self.assertFalse(any('/source-fallback-repair-units/' in key for key in self.client.objects))

    def test_each_locale_has_explicit_nonmutable_contract(self):
        from portal_extended_locales import select_locales
        keys={RepairEngine(quality_contract(loc)).unit_key('Revenue USD10m.','en') for loc in select_locales('all-supported')}
        self.assertEqual(len(keys),33)
        for bad in ('en','zh','ko','ja','ar','fr,de'):
            with self.assertRaises(ExpansionError): quality_contract(bad)

    def test_interrupted_prepared_tail_resumes_with_zero_inference_and_exact_completion(self):
        jobs,_=self.select()
        self.client.fail_key=state_key(self.store,'completed','fr',fixtures.DAY)
        with self.assertRaises(fixtures.R2TransportError): self.finish(jobs[0])
        self.client.fail_key=None
        owner={**fixtures.OWNER, 'run_id':'3'}
        with patch('offline_translation.OfflineTranslator', side_effect=AssertionError('tail opened inference')):
            resumed=recovery.resume_prepared(self.store,('fr',),owner,fixtures.REPOSITORY,self.history_api)
        self.assertEqual(len(resumed),1)
        summary=recovery.followup(self.store,resumed,owner)
        self.assertTrue(summary['continue']);self.assertEqual(summary['accepted_units'],1)
        self.assertEqual(summary['fresh_inference_unit_attempts'],0)
        self.assertEqual(recovery.resume_prepared(self.store,('fr',),owner,fixtures.REPOSITORY,self.history_api),[])
        self.assertEqual(len(debt_rows(self.store,'fr')),1)

    def test_queue_after_but_quality_write_missing_resumes_exact_tail(self):
        jobs,_=self.select()
        self.client.fail_key=state_key(self.store,'quality-debt','fr')
        with self.assertRaises(fixtures.R2TransportError): self.finish(jobs[0])
        self.client.fail_key=None
        self.assertIn('source_repair_sha256',queue(self.store,'fr')[self.generation])
        owner={**fixtures.OWNER,'run_id':'3'}
        resumed=recovery.resume_prepared(self.store,('fr',),owner,fixtures.REPOSITORY,self.history_api)
        self.assertEqual(len(resumed),1)
        self.assertEqual(debt_rows(self.store,'fr')[self.generation]['source_fallback_unit_count'],1)
        self.assertEqual(recovery.followup(self.store,resumed,owner)['fresh_inference_unit_attempts'],0)

    def test_failed_source_after_tail_keeps_active_for_next_source(self):
        jobs,_=self.select();self.client.fail_key=state_key(self.store,'completed','fr',fixtures.DAY)
        with self.assertRaises(fixtures.R2TransportError):self.finish(jobs[0])
        self.client.fail_key=None
        owner={**fixtures.OWNER,'run_id':'3'}
        resumed=recovery.resume_prepared(self.store,('fr',),owner,fixtures.REPOSITORY,self.history_api)
        self.assertEqual(read_state(self.store,'quality-recovery-active','fr')['plan'],resumed[0])
        def failed_source(path):
            value=self.history_api(path)
            if '/runs/3/' in path and '/jobs?' in path:
                value['jobs'][0]['conclusion']='failure'
            return value
        next_owner={**fixtures.OWNER,'run_id':'4'}
        resumed_again=recovery.resume_prepared(self.store,('fr',),next_owner,fixtures.REPOSITORY,failed_source)
        self.assertEqual(len(resumed_again),1)
        summary=recovery.followup(self.store,resumed_again,next_owner)
        self.assertTrue(summary['continue']);self.assertEqual(summary['fresh_inference_unit_attempts'],0)

    def test_accepted_ledger_plan_skips_adapter_construction_and_lost_ledger_blocks(self):
        required=self.pipeline.units.required_units(self.f.corpus)
        for unit in self.f.request['units']:
            self.pipeline.units.attempt_unit(self.store,unit,required[unit],fixtures.ORIGINAL,fixtures.RepairTranslator())
        jobs,_=self.select();plan=recovery.read_plan(self.store,jobs[0]['quality_repair'])
        self.assertFalse(plan['requires_engine'])
        args=SimpleNamespace(operation='restore',generation=self.generation,locale='fr',requires_engine=False,
            checkpoint=self.f.root/'ledger.json',corpus=self.f.root/'corpus.json',output=self.f.root/'ledger-out',
            github_output=self.f.root/'outputs.txt',seconds=30)
        with patch('offline_translation.OfflineTranslator',side_effect=AssertionError('cache-only instantiated model')):
            with redirect_stdout(io.StringIO()):
                self.pipeline.run(args,plan['request'],fixtures.OWNER,store=self.store,repository=fixtures.REPOSITORY,api=self.f.api)
                self.assertIn('requires_engine=false',args.github_output.read_text())
                args.operation='build'
                self.pipeline.run(args,plan['request'],fixtures.OWNER,store=self.store,repository=fixtures.REPOSITORY,api=self.f.api)
        proof=json.loads((args.output.parent/'fr-source-fallback-repair-proof.json').read_text())
        self.assertEqual(proof['unit_attempt_modes'],{'accepted-ledger':2,'cache-only':0,'fresh-inference':0})
        unit=plan['request']['units'][-1]
        for name in ('started.json','outcome.json'):
            del self.client.objects[self.pipeline.units.ledger_key(self.store,unit,name)]
        args.output=self.f.root/'lost-ledger-output'
        args.checkpoint.write_bytes(self.f.old_raw)
        before=copy.deepcopy(self.client.objects)
        with patch('offline_translation.OfflineTranslator',side_effect=AssertionError('lost ledger instantiated model')):
            with self.assertRaisesRegex(ExpansionError,'planned_ledger_missing'):
                self.pipeline.run(args,plan['request'],fixtures.OWNER,store=self.store,repository=fixtures.REPOSITORY,api=self.f.api)
        self.assertEqual(self.client.objects,before);self.assertFalse(args.output.exists())

    def test_completed_generation_yields_to_another_debt_or_ordinary_work(self):
        jobs,_=self.select();self.finish(jobs[0],fixtures.RepairTranslator())
        with patch.object(recovery,'normal_work',return_value=True):
            self.assertTrue(recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.OWNER)['continue'])
        real=recovery.debt_rows
        with patch.object(recovery,'debt_rows',side_effect=lambda store,locale: {'other':{}} if not real(store,locale) else real(store,locale)):
            self.assertTrue(recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.OWNER)['continue'])

    def test_bounded_generation_scan_rotates_past_blocked_first_four(self):
        seen=[]; entries={str(i)*64:{} for i in range(1,6)}
        def rejected(store,locale,generation,*args):seen.append(generation[0]);return None
        with patch.object(recovery,'debt_rows',return_value=entries),patch.object(recovery,'prepare_one',side_effect=rejected):
            for _ in range(3):self.select()
        self.assertEqual(''.join(seen),'123451234512')

    def test_nonfrench_repair_full_handoff_is_bound_to_its_own_locale(self):
        # Same English fixture source, German contract; no language globals change.
        self.locale='de'; self.pipeline=RepairPipeline(quality_contract('de'))
        self.f.jobs[1]['name']='locale (de)'
        old_dir=self.f.root/'de-old'; old_path=self.f.root/'de-old.json'
        build(self.f.corpus,'de',old_dir,old_path,fixtures.OriginalRejected(),allow_source_fallback=True,budget_seconds=30)
        remember_checkpoint(self.store,'de',self.generation,old_path)
        remember_candidate(self.store,'de',self.f.corpus,old_dir)
        self.quality();jobs,blocked=self.select();self.assertFalse(blocked)
        self.finish(jobs[0],fixtures.RepairTranslator())
        row=queue(self.store,'de')[self.generation]
        identity=fixtures.save_handoff(self.store,{'generation':self.generation,'candidates':{'de':row['snapshot']['candidate_id']}},
            producer=fixtures.OWNER,day=fixtures.DAY,pages=2)
        receipt=fixtures.read_handoff(self.store,identity)
        proofs=fixtures.source_repair_proofs(self.store,receipt)
        self.assertEqual(set(proofs),{'de'})
        self.assertEqual(proofs['de']['locale'],'de')

    def test_quality_turn_yields_only_when_actual_normal_work_exists(self):
        jobs,_=self.select();self.assertTrue(jobs)
        with patch.object(recovery,'normal_work',return_value=True):
            more,_=self.select();self.assertFalse(more)
        recovery.mark_ordinary(self.store,[{'locale':'fr','generation':'e'*64,'day':fixtures.DAY}])
        with patch.object(recovery,'normal_work',return_value=True):
            more,_=self.select();self.assertTrue(more)

    def test_last_ordinary_page_progress_releases_a_single_debt_scan(self):
        import portal_extended_daily_queue as daily
        admitted={'generation':self.generation,'day':fixtures.DAY,'pages':2}
        with patch.object(daily,'read_admission',return_value=admitted),             patch.object(daily,'read_corpus',return_value=self.f.corpus),             patch.object(daily,'pending_docs',return_value=[]),             patch.object(daily,'all_queued',return_value=[]):
            self.assertTrue(daily.followup_needed(self.store,'a'*64,('fr',),{'fr':2})['continue'])
            self.assertFalse(daily.followup_needed(self.store,'a'*64,('fr',),{'fr':0})['continue'])

    def test_every_tail_write_boundary_budget_stop_reserves_only_affected_locale(self):
        jobs,_=self.select();self.client.fail_key=state_key(self.store,'completed','fr',fixtures.DAY)
        with self.assertRaises(fixtures.R2TransportError):self.finish(jobs[0])
        self.client.fail_key=None
        snapshot=copy.deepcopy(self.client.objects)
        owner={**fixtures.OWNER,'run_id':'3'}
        reads=[0];boundaries=[]
        head,get,put=self.client.head_object,self.client.get_object,self.client.put_object
        def counted_head(**kw):reads[0]+=1;return head(**kw)
        def counted_get(**kw):reads[0]+=1;return get(**kw)
        def marked_put(**kw):boundaries.append(reads[0]);return put(**kw)
        with patch.object(self.client,'head_object',side_effect=counted_head),             patch.object(self.client,'get_object',side_effect=counted_get),             patch.object(self.client,'put_object',side_effect=marked_put):
            completed=recovery.resume_prepared(self.store,('fr',),owner,fixtures.REPOSITORY,self.history_api)
        self.assertEqual(len(completed),1);self.assertGreater(len(boundaries),5)
        # Scheduler control reads are outside the deep scan. Include each write's
        # adjacent budgets and all queue-after / completion / marker boundaries.
        limits=sorted({max(0,n+delta) for n in boundaries for delta in (-2,-1,0,1)})
        for limit in limits:
            with self.subTest(read_budget=limit):
                self.client.objects=copy.deepcopy(snapshot)
                budget=recovery.ScanBudget(reads=limit)
                resumed=recovery.resume_prepared(self.store,('fr',),owner,fixtures.REPOSITORY,self.history_api,budget=budget)
                complete_locales={recovery.read_plan(self.store,identity)['locale'] for identity in resumed}
                reserved=recovery.pending_tail_locales(self.store,('fr','de'),completed=complete_locales)
                self.assertNotIn('de',reserved)
                if not resumed:
                    self.assertIn('fr',reserved)
                    # The source matrix filters this locale; ordinary work must
                    # not overwrite its exact pending-tail Memo before resumption.
                    self.assertEqual(tuple(loc for loc in ('fr','de') if loc not in reserved),('de',))
                    memo=copy.deepcopy(read_state(self.store,'memo','fr'))
                    with patch('offline_translation.OfflineTranslator',side_effect=AssertionError('tail inference')):
                        next_done=recovery.resume_prepared(self.store,('fr',),{**owner,'run_id':'4'},
                            fixtures.REPOSITORY,lambda path:self._failed_repair_history(path))
                    self.assertEqual(len(next_done),1)
                    self.assertEqual(recovery.followup(self.store,next_done,{**owner,'run_id':'4'})['fresh_inference_unit_attempts'],0)
                else:
                    self.assertNotIn('fr',reserved)

    def _failed_repair_history(self,path):
        value=self.history_api(path)
        if '/runs/3/' in path and '/jobs?' in path:value['jobs'][0]['conclusion']='failure'
        return value

    def test_unknown_unit_without_prepared_proof_does_not_reserve_ordinary_lane(self):
        jobs,_=self.select()
        self.assertEqual(recovery.pending_tail_locales(self.store,('fr','de')),())

    def test_scan_read_budget_stops_before_inference_and_next_source_resumes(self):
        before=copy.deepcopy(queue(self.store,'fr'))
        budget=recovery.ScanBudget(reads=6)
        jobs,blocked=recovery.prepare(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,self.f.api,budget=budget)
        self.assertEqual(jobs,[]);self.assertEqual(blocked[-1]['code'],'scan_budget_exhausted')
        self.assertEqual(budget.reads,6);self.assertTrue(budget.stopped)
        self.assertEqual(queue(self.store,'fr'),before)
        self.assertFalse(any('/source-fallback-repair-units/' in key for key in self.client.objects))
        self.assertFalse(recovery.followup(self.store,[],fixtures.OWNER)['continue'])
        jobs,blocked=self.select();self.assertTrue(jobs);self.assertEqual(blocked,[])

    def test_scan_deadline_and_api_budget_preserve_original_snapshot(self):
        before=copy.deepcopy(queue(self.store,'fr'))
        for budget in (recovery.ScanBudget(seconds=0,clock=lambda:1), recovery.ScanBudget(api_reads=0)):
            with self.subTest(reads=budget.api_limit):
                jobs,blocked=recovery.prepare(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,self.f.api,budget=budget)
                self.assertEqual(jobs,[]);self.assertTrue(budget.stopped)
                self.assertEqual(queue(self.store,'fr'),before)
                self.assertEqual(budget.api_reads,0)
                self.assertFalse(recovery.followup(self.store,[],fixtures.OWNER)['continue'])
        jobs,_=self.select();self.assertTrue(jobs)

    def test_budget_keeps_already_selected_plan_and_next_locale_cursor(self):
        before=copy.deepcopy(self.client.objects)
        probe=recovery.ScanBudget()
        jobs,_=recovery.prepare(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,self.f.api,budget=probe)
        self.assertEqual(len(jobs),1)
        self.client.objects=before
        budget=recovery.ScanBudget(reads=probe.reads)
        jobs,blocked=recovery.prepare(self.store,('fr','de'),fixtures.OWNER,fixtures.REPOSITORY,self.f.api,budget=budget)
        self.assertEqual(len(jobs),1);self.assertEqual(jobs[0]['locale'],'fr')
        self.assertEqual(recovery.read_plan(self.store,jobs[0]['quality_repair'])['locale'],'fr')
        self.assertEqual(blocked[-1],{'locale':'de','code':'scan_budget_exhausted'})
        self.assertEqual(recovery.ordered_locales(self.store,('fr','de')),('de','fr'))
        self.assertFalse(recovery.followup(self.store,[jobs[0]['quality_repair']],fixtures.OWNER)['continue'])

    def test_tail_and_selection_share_one_source_scan_budget(self):
        budget=recovery.ScanBudget(reads=2)
        self.assertEqual(recovery.resume_prepared(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,self.f.api,budget=budget),[])
        jobs,blocked=recovery.prepare(self.store,('fr',),fixtures.OWNER,fixtures.REPOSITORY,self.f.api,budget=budget)
        self.assertEqual(jobs,[]);self.assertTrue(budget.stopped);self.assertLessEqual(budget.reads,2)
        self.assertFalse(recovery.followup(self.store,[],fixtures.OWNER)['continue'])

    def test_empty_ordinary_turn_does_not_stall_debt(self):
        write_state(self.store,'quality-recovery-turn','fr',{'last':'quality'})
        with patch.object(recovery,'normal_work',return_value=False):
            jobs,_=self.select();self.assertTrue(jobs)


if __name__=='__main__':unittest.main()
