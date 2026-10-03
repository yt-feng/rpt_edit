import copy
import json
import os
import unittest
from unittest.mock import patch

import repair_portal_extended_checkpoint as repair
import portal_extended_recovery_intent as intent
from portal_extended_continuation import register, queue, read_origin
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import R2IntegrityError
import test_portal_extended_recovery_intent as fixtures
from test_portal_extended_continuation import PRODUCER
from offline_translation import MODEL_ID
from build_portal_extended_locales import CHECKPOINT_VERSION
import test_portal_extended_continuation as continuation_fixtures
from build_portal_extended_locales import build
from test_portal_extended_incremental import daily_doc
from portal_extended_locales import make_corpus
from test_portal_extended_locales import ORIGIN,FakeTranslator
from portal_extended_continuation import save_queue


class RepairTests(unittest.TestCase):
    setUp=fixtures.IntentTests.setUp
    api=fixtures.IntentTests.api
    partial=fixtures.IntentTests.partial

    def original(self):
        evidence={'producer':PRODUCER,'locales':{'fr':self.partial(registered=False)}}
        identity=intent.register_intent(self.store,self.gen,evidence,'example/repo',self.api)
        return identity,evidence

    def checkpoint(self, source='收益率上升50个基点。', target='Le rendement monte de 50.'):
        row={'source':source,'language':'zh','text':target}
        identity=repair.unit_key('fr',row)
        good={'source':'中文研究','language':'zh','text':'Une analyse financière.'}
        return identity,{'model':MODEL_ID,'version':CHECKPOINT_VERSION,'locale':'fr','source_generation':self.gen,
                         'rows':{identity:row,repair.unit_key('fr',good):good}}

    def test_only_current_quantity_failures_with_exact_source_keys_are_selected(self):
        identity,value=self.checkpoint()
        self.assertEqual(repair.validate_units(value,'fr',self.gen),[identity])
        value['rows'][identity]['text']='Le rendement monte de 50 bp.'
        self.assertEqual(repair.validate_units(value,'fr',self.gen),[])
        value['rows'][identity]['source']='收益率上升60个基点。'
        with self.assertRaisesRegex(ExpansionError,'exact source'):repair.validate_units(value,'fr',self.gen)

    def test_nonquantity_failures_cannot_enter_targeted_repair(self):
        identity,value=self.checkpoint(target='')
        with self.assertRaisesRegex(ExpansionError,'only replace'):repair.validate_units(value,'fr',self.gen)
        identity,value=self.checkpoint(source='收入增长50%。')
        with self.assertRaisesRegex(ExpansionError,'only replace'):repair.validate_units(value,'fr',self.gen)

    def test_protected_basis_point_translation_keeps_scale_and_original_quality_gate(self):
        source='收益率上升50个基点，利润率为9%。'
        calls=[]
        class Base:
            def translate(self,text,**kw):
                calls.append(text);return 'Le taux monte de __HYMTPH_9000__, marge 9%.'
        output=repair.ProtectedBasisPointTranslator(Base(),{source}).translate(source,target='fr',source='zh')
        self.assertEqual(output,'Le taux monte de 50 bps, marge 9%.')
        self.assertNotIn('50',calls[0]);self.assertIn('9%',calls[0])
        class Wrong:
            def translate(self,text,**kw):return 'Le taux monte de __HYMTPH_9000__, marge 10%.'
        with self.assertRaisesRegex(repair.TargetedRepairError,'original quality'):
            repair.ProtectedBasisPointTranslator(Wrong(),{source}).translate(source,target='fr',source='zh')

    def test_placeholder_loss_or_duplication_does_not_become_a_repair(self):
        for value in ('Le taux augmente.', 'Le taux __HYMTPH_9000__ et __HYMTPH_9000__.'):
            class Base:
                def translate(self,*a,**kw):return value
            with self.subTest(value=value),self.assertRaisesRegex(repair.TargetedRepairError,'original quality'):
                repair.ProtectedBasisPointTranslator(Base(),{'50个基点'}).translate('50个基点',target='fr',source='zh')

    def test_fixed_failure_diagnostic_keeps_gate_and_unit_without_source_or_error_text(self):
        source='私人报告内容：收益率上升50个基点。'
        class Base:
            def translate(self,*a,**kw):
                raise repair.OfflineTranslationValidationError('Hy-MT2 quantity validation failed: private secret 999')
        protected=repair.ProtectedBasisPointTranslator(Base(),{source})
        with self.assertRaises(repair.TargetedRepairError) as caught:
            protected.translate(source,target='fr',source='zh',markdown=False)
        diagnostic=caught.exception.diagnostic
        self.assertEqual(diagnostic['gate_code'],'offline-quantity-validation')
        self.assertEqual(diagnostic['stage'],'model-validation')
        self.assertEqual(diagnostic['unit_sha256'],repair.unit_key('fr',{'source':source,'language':'zh'}))
        self.assertNotIn('私人报告',json.dumps(diagnostic,ensure_ascii=False))
        self.assertNotIn('private secret',json.dumps(diagnostic))
        self.assertIsNone(protected.current)

    def test_model_signals_are_bounded_and_do_not_contain_private_model_text(self):
        source='收益率上升50个基点，利润率9%。'
        class Base:
            def translate(self,text,**kw):
                for n in range(10):
                    protected.observe_model({'model_input':text,'raw_translation':'Private model draft 10%',
                                             'quality_retry':n%3})
                return 'Le taux a augmenté sans unité.'
        protected=repair.ProtectedBasisPointTranslator(Base(),{source})
        with self.assertRaises(repair.TargetedRepairError):
            protected.translate(source,target='fr',source='zh')
        row=protected.failures[0]
        self.assertEqual(row['gate_code'],'placeholder-validation')
        self.assertEqual((len(row['model_attempts']),row['model_signals_total'],row['model_signals_truncated']),(3,10,True))
        self.assertEqual(row['model_attempts'][0]['missing_basis_point_placeholders'],1)
        self.assertNotIn('Private model draft',json.dumps(row))
        self.assertNotIn(source,json.dumps(row,ensure_ascii=False))

    def test_preserved_rows_and_fallbacks_are_byte_bound_and_new_source_cannot_be_swapped(self):
        identity,old=self.checkpoint();new=copy.deepcopy(old)
        new['rows'][identity]['text']='Le rendement monte de 50 bps.'
        result=repair.preserve(old,new,'fr',self.gen,[identity])
        self.assertEqual(result['unchanged_translation_rows'],1)
        self.assertEqual(result['repaired_units'][0]['source_sha256'],digest(old['rows'][identity]['source'].encode()))
        changed=copy.deepcopy(new);other=next(k for k in old['rows'] if k!=identity)
        changed['rows'][other]['text']='Une autre recherche.'
        with self.assertRaisesRegex(ExpansionError,'preserved cache'):repair.preserve(old,changed,'fr',self.gen,[identity])
        changed=copy.deepcopy(new);del changed['rows'][identity]
        with self.assertRaisesRegex(ExpansionError,'source fallback'):repair.preserve(old,changed,'fr',self.gen,[identity])

    def test_no_registration_claim_or_ack_before_all_original_evidence_is_checked(self):
        identity,evidence=self.original();requested={'intent':identity,'units':['0'*64]}
        before=copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError,'current rejected'):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,PRODUCER)
        self.assertEqual(self.store.client.objects,before);self.assertIsNone(read_origin(self.store,self.gen))
        self.assertFalse(intent.acknowledged(self.store,identity))

    def test_registered_generation_cannot_be_reset_by_repair_entry(self):
        identity,evidence=self.original();requested={'intent':identity,'units':['0'*64]}
        value=intent.read_receipt(self.store,{'intent':identity,'generation':self.gen})
        register(self.store,self.corpus,('fr',),PRODUCER);before=copy.deepcopy(self.store.client.objects)
        with patch.object(repair,'load',return_value=(value,self.corpus,{})),self.assertRaisesRegex(ExpansionError,'cannot reset'):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,PRODUCER)
        self.assertEqual(self.store.client.objects,before);self.assertEqual(queue(self.store,'fr')[self.gen]['continuations'],0)

    def test_exact_serialized_claim_never_allows_another_attempt(self):
        identity,evidence=self.original();requested={'intent':identity,'units':['0'*64]}
        value=intent.read_receipt(self.store,{'intent':identity,'generation':self.gen})
        with patch.object(repair,'load',return_value=(value,self.corpus,{})):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,PRODUCER)
        repair.check_claim(self.store,self.gen,'fr',requested,PRODUCER)
        another={**PRODUCER,'attempt':'2'}
        with self.assertRaisesRegex(ExpansionError,'exact serialized'):repair.check_claim(self.store,self.gen,'fr',requested,another)
        with patch.object(repair,'load',return_value=(value,self.corpus,{})),self.assertRaises(ExpansionError):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,another)

    def financial_original(self):
        source='收益率上升50个基点。'
        self.corpus=make_corpus([daily_doc(body='<h1>Research note</h1><p>'+source+'</p>'),
            daily_doc(ORIGIN+'/blog/20260925-second.html',body='<h1>Second page</h1><p>Second unique unfinished unit.</p>')])
        self.gen=self.corpus['documents_sha256'];self.store.put_source(self.corpus)
        class Legacy(continuation_fixtures.StopAtLastUnit):
            def translate(self,text,**kw):
                if text==source:return 'Le rendement monte de 50.'
                return super().translate(text,**kw)
        with patch.object(continuation_fixtures,'StopAtLastUnit',Legacy),patch('build_portal_extended_locales.quantity_issues',return_value=[]):
            evidence={'producer':PRODUCER,'locales':{'fr':self.partial(registered=False)}}
            identity=intent.register_intent(self.store,self.gen,evidence,'example/repo',self.api)
        proof=evidence['locales']['fr'];old=json.loads(self.store._get(self.store.checkpoint_object_key('fr',self.gen,proof['checkpoint_sha256']),maximum=8*1024*1024))
        units=repair.validate_units(old,'fr',self.gen)
        self.assertEqual(len(units),1)
        return {'intent':identity,'units':units},old

    def prepared_fixture(self):
        requested,old=self.financial_original()
        repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,PRODUCER)
        value,corpus,verified_old=repair.load(self.store,self.gen,'fr',requested,'example/repo',self.api)
        self.assertEqual(old,verified_old)
        checkpoint=self.root/'fixed.json';clone=copy.deepcopy(old)
        for unit in requested['units']:del clone['rows'][unit]
        checkpoint.write_bytes(stable_bytes(clone))
        class Base(FakeTranslator):
            def translate(self,text,**kw):
                if '__HYMTPH_9000__' in text:return 'Le rendement monte de __HYMTPH_9000__.'
                return super().translate(text,**kw)
        base=Base();protected=repair.ProtectedBasisPointTranslator(base,{old['rows'][k]['source'] for k in requested['units']})
        translator=repair.PrivateUnitTranslator(protected,self.store,requested,self.gen,'fr',PRODUCER)
        output=self.root/'repaired';manifest=build(corpus,'fr',output,checkpoint,translator,allow_source_fallback=True)
        self.assertEqual(manifest['status'],'complete-candidate')
        evidence=repair.preserve(old,json.loads(checkpoint.read_bytes()),'fr',self.gen,requested['units'])
        saved=self.store.put_checkpoint('fr',self.gen,checkpoint);candidate=self.store.upload_candidate(output,'fr',self.gen)
        prepared={'schema_version':1,'policy':repair.POLICY,'generation':self.gen,'locale':'fr','request':requested,
            'producer':PRODUCER,'original_producer':PRODUCER,'source_sha256':value['source_sha256'],
            'checkpoint_sha256':saved['sha256'],'candidate_id':candidate['candidate_id'],
            'manifest_sha256':candidate['manifest_sha256'],**evidence}
        intent.immutable_record(self.store,repair.repair_key(self.store,requested,'prepared.json'),prepared,kind='test')
        return requested,old,value,prepared

    def test_real_frozen_source_is_repaired_once_and_resume_uses_private_validated_units(self):
        requested,old,value,prepared=self.prepared_fixture()
        class NoModel:
            def translate(self,*a,**kw):raise AssertionError('resumed validated private unit caused a CPU call')
        cached=repair.PrivateUnitTranslator(NoModel(),self.store,requested,self.gen,'fr',PRODUCER)
        source=old['rows'][requested['units'][0]]['source']
        self.assertEqual(cached.translate(source,target='fr',source='zh',markdown=False),'Le rendement monte de 50 bps.')
        self.assertEqual(cached.cache_hits,1)
        repair.resume_prepared(self.store,value,self.corpus,old,requested,'fr',prepared)
        self.assertTrue(intent.acknowledged(self.store,requested['intent']))
        self.assertEqual((queue(self.store,'fr')[self.gen]['status'],queue(self.store,'fr')[self.gen]['continuations']),('complete',0))
        result=repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,{**PRODUCER,'run_id':'987'})
        self.assertFalse(result['has_work']);self.assertTrue(result['resumed_prepared_without_cpu'])

    def test_fault_at_every_canonical_commit_write_resumes_without_cpu_or_counter_reset(self):
        requested,old,value,prepared=self.prepared_fixture()
        baseline=copy.deepcopy(self.store.client.objects);writes=[];put=self.store._put
        def record(key,*a,**kw):writes.append(key);return put(key,*a,**kw)
        with patch.object(self.store,'_put',record):repair.resume_prepared(self.store,value,self.corpus,old,requested,'fr',prepared)
        self.assertGreaterEqual(len(writes),6)
        for stop in range(len(writes)):
            self.store.client.objects=copy.deepcopy(baseline);count=[0]
            def crash(key,*a,**kw):
                if count[0]==stop:raise RuntimeError('synthetic interrupted commit')
                count[0]+=1;return put(key,*a,**kw)
            with self.subTest(write=stop):
                with patch.object(self.store,'_put',crash),self.assertRaises(RuntimeError):
                    repair.resume_prepared(self.store,value,self.corpus,old,requested,'fr',prepared)
                repair.resume_prepared(self.store,value,self.corpus,old,requested,'fr',prepared)
                self.assertTrue(intent.acknowledged(self.store,requested['intent']))
                self.assertEqual(queue(self.store,'fr')[self.gen]['continuations'],0)

    def test_prepared_resume_cannot_reset_a_real_advanced_or_different_snapshot(self):
        requested,old,value,prepared=self.prepared_fixture()
        repair.resume_prepared(self.store,value,self.corpus,old,requested,'fr',prepared)
        row=queue(self.store,'fr')[self.gen];row['continuations']=1;save_queue(self.store,'fr',{self.gen:row})
        before=copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError,'advanced continuation'):
            repair.resume_prepared(self.store,value,self.corpus,old,requested,'fr',prepared)
        self.assertEqual(before,self.store.client.objects)

    def test_partial_repair_reuses_validated_private_units_across_bounded_attempts(self):
        requested,old=self.financial_original();owner={'run_id':'456','attempt':'1','sha':'b'*40}
        def api(path):
            if '/runs/456/' not in path:return self.api(path)
            return {'id':456,'run_attempt':int(path.rsplit('/',1)[-1]),'head_sha':'b'*40,
                'status':'completed','conclusion':'failure','path':repair.WORKFLOW,'head_branch':'main',
                'event':'workflow_dispatch','repository':{'full_name':'example/repo'},'head_repository':{'full_name':'example/repo'}}
        repair.prepare(self.store,self.gen,'fr',requested,'example/repo',api,owner)
        source=old['rows'][requested['units'][0]]['source']
        class Once:
            calls=0
            def translate(self,*a,**kw):self.calls+=1;return 'Le rendement monte de 50 bps.'
        model=Once();translator=repair.PrivateUnitTranslator(model,self.store,requested,self.gen,'fr',owner)
        translator.translate(source,target='fr',source='zh',markdown=False)
        next_owner={**owner,'attempt':'2'}
        repair.prepare(self.store,self.gen,'fr',requested,'example/repo',api,next_owner)
        resumed=repair.PrivateUnitTranslator(model,self.store,requested,self.gen,'fr',next_owner)
        resumed.translate(source,target='fr',source='zh',markdown=False)
        self.assertEqual(model.calls,1);self.assertEqual(resumed.cache_hits,1)
        repair.prepare(self.store,self.gen,'fr',requested,'example/repo',api,{**owner,'attempt':'3'})
        before=copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError,'attempt bound'):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',api,{**owner,'attempt':'4'})
        self.assertEqual(before,self.store.client.objects);self.assertIsNone(read_origin(self.store,self.gen))

    def test_seven_exact_units_resume_six_private_cache_rows_and_one_cpu_unit(self):
        sources = [f'收益率上升{n}个基点。' for n in range(10, 80, 10)]
        numbers = {text: repair.BP.search(text)[1] for text in sources}
        self.corpus = make_corpus([daily_doc(body='<h1>Research note</h1>' + ''.join('<p>'+s+'</p>' for s in sources))])
        self.gen = self.corpus['documents_sha256']
        class Good(FakeTranslator):
            def translate(base, text, **kw):
                if text in numbers: return 'Le rendement monte de '+numbers[text]+' bps.'
                return super().translate(text, **kw)
        original_checkpoint = self.root/'seven-original.json'
        initial = build(self.corpus, 'fr', self.root/'seven-original-candidate', original_checkpoint, Good(), allow_source_fallback=True)
        self.assertEqual(initial['status'], 'complete-candidate')
        old = json.loads(original_checkpoint.read_bytes())
        for row in old['rows'].values():
            if row['source'] in numbers: row['text'] = 'Le rendement monte de '+numbers[row['source']]+'.'
        units = repair.validate_units(old, 'fr', self.gen)
        self.assertEqual(len(units), 7)
        requested = {'intent':'a'*64, 'units':units}
        owner = {'run_id':'456', 'attempt':'1', 'sha':'b'*40}
        value = {'source_sha256':digest(stable_bytes(self.corpus)), 'evidence':{'producer':PRODUCER}}
        def api(path):
            return {'id':456, 'run_attempt':1, 'head_sha':owner['sha'], 'status':'completed',
                'conclusion':'failure', 'path':repair.WORKFLOW, 'head_branch':'main',
                'event':'workflow_dispatch', 'repository':{'full_name':'example/repo'},
                'head_repository':{'full_name':'example/repo'}}
        with patch.object(repair, 'load', return_value=(value,self.corpus,old)):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',api,owner)
        def restored(path):
            clone=copy.deepcopy(old)
            for identity in units: del clone['rows'][identity]
            path.write_bytes(stable_bytes(clone))
        class First(FakeTranslator):
            targeted_calls=0
            def translate(base,text,**kw):
                if '__HYMTPH_9000__' in text:
                    base.targeted_calls+=1
                    if base.targeted_calls==7: return 'Le rendement omet son nombre.'
                    return 'Le rendement monte de __HYMTPH_9000__.'
                raise AssertionError('an unaffected original unit invoked CPU')
        first=First()
        protected=repair.ProtectedBasisPointTranslator(first,set(sources))
        wrapped=repair.PrivateUnitTranslator(protected,self.store,requested,self.gen,'fr',owner)
        first_checkpoint=self.root/'seven-first.json'; restored(first_checkpoint)
        failed=build(self.corpus,'fr',self.root/'seven-first-candidate',first_checkpoint,wrapped,allow_source_fallback=True)
        self.assertEqual(failed['status'],'incomplete-candidate')
        self.assertEqual(first.targeted_calls,7)
        partial=json.loads(first_checkpoint.read_bytes())
        successful=set(units)&set(partial['rows']); self.assertEqual(len(successful),6)
        remaining=(set(units)-successful).pop()
        self.assertNotIn(remaining,partial.get('source_fallbacks',{}))
        self.assertIsNone(repair.read_optional(self.store,repair.repair_key(self.store,requested,'units',remaining+'.json')))
        before={identity:self.store._get(repair.repair_key(self.store,requested,'units',identity+'.json'),maximum=65536) for identity in successful}
        next_owner={**owner,'attempt':'2'}
        with patch.object(repair,'load',return_value=(value,self.corpus,old)):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',api,next_owner)
        class Last(FakeTranslator):
            targeted_calls=0
            def translate(base,text,**kw):
                base.targeted_calls+=1
                if base.targeted_calls!=1 or '__HYMTPH_9000__' not in text:
                    raise AssertionError('the six validated units or preserved rows were redone')
                return 'Le rendement monte de __HYMTPH_9000__.'
        last=Last()
        resumed=repair.PrivateUnitTranslator(repair.ProtectedBasisPointTranslator(last,set(sources)),self.store,requested,self.gen,'fr',next_owner)
        final_checkpoint=self.root/'seven-final.json'; restored(final_checkpoint)
        complete=build(self.corpus,'fr',self.root/'seven-final-candidate',final_checkpoint,resumed,allow_source_fallback=True)
        self.assertEqual(complete['status'],'complete-candidate')
        self.assertEqual(last.targeted_calls,1); self.assertEqual(resumed.cache_hits,6)
        self.assertEqual(set(resumed.cache_unit_ids),successful); self.assertEqual(resumed.new_unit_ids,[remaining])
        for identity,raw in before.items():
            self.assertEqual(raw,self.store._get(repair.repair_key(self.store,requested,'units',identity+'.json'),maximum=65536))
        final=json.loads(final_checkpoint.read_bytes())
        self.assertFalse(set(units)&set(final.get('source_fallbacks',{})))
        evidence=repair.preserve(old,final,'fr',self.gen,units,allowed_new_units=repair.required_units(self.corpus,'fr'))
        untouched={k:v for k,v in old['rows'].items() if k not in units}
        self.assertEqual({k:final['rows'][k] for k in untouched},untouched)
        self.assertEqual(evidence['unchanged_rows_sha256'],digest(stable_bytes(untouched)))
        self.assertEqual(evidence['unchanged_translation_rows'],len(untouched))
        self.assertEqual(len(evidence['repaired_units']),7)

    def test_selected_translation_failure_cannot_become_an_ordinary_source_fallback(self):
        requested,old=self.financial_original();clone=copy.deepcopy(old)
        for k in requested['units']:del clone['rows'][k]
        checkpoint=self.root/'bad-repair.json';checkpoint.write_bytes(stable_bytes(clone))
        class Reject(FakeTranslator):
            def translate(self,text,**kw):
                if '__HYMTPH_9000__' in text:return 'Le rendement omet son nombre.'
                return super().translate(text,**kw)
        wrapped=repair.ProtectedBasisPointTranslator(Reject(),{old['rows'][k]['source'] for k in requested['units']})
        result=build(self.corpus,'fr',self.root/'bad-candidate',checkpoint,wrapped,allow_source_fallback=True)
        self.assertEqual(result['status'],'incomplete-candidate');self.assertTrue(result['failures'])
        new=json.loads(checkpoint.read_bytes())
        self.assertFalse(set(requested['units']) & set(new.get('source_fallbacks',{})))

    def test_changed_frozen_original_page_is_rejected_before_claim_or_cpu(self):
        requested,old=self.financial_original()
        value=intent.read_receipt(self.store,{'intent':requested['intent'],'generation':self.gen})
        proof=value['evidence']['locales']['fr']
        manifest=json.loads(self.store._get(self.store.candidate_manifest_key('fr',self.gen,proof['candidate_id']),maximum=2*1024*1024))
        row=manifest['pages'][0];name=self.store.candidate_key('fr',self.gen,proof['candidate_id'],row['path'])
        self.store._put(name,b'changed frozen page',metadata={})
        before=copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError,'frozen page bytes'):
            repair.prepare(self.store,self.gen,'fr',requested,'example/repo',self.api,PRODUCER)
        self.assertEqual(before,self.store.client.objects)


if __name__=='__main__':unittest.main()
