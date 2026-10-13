"""Exact successful continuation provenance; no network or model."""
import copy
import json
import unittest
from unittest.mock import patch

import portal_extended_completion as completion
import portal_extended_quality_recovery as recovery
import test_portal_extended_quality_recovery as fixtures
from portal_extended_continuation import queue, save_queue, record_result, acknowledge_published
from portal_extended_incremental import read_state, state_key
from portal_extended_quality import debt_rows
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_quality_recovery import exact_result


class CompletionTests(unittest.TestCase):
    setUpBase=fixtures.RecoveryTests.setUp
    quality=fixtures.RecoveryTests.quality
    finish=fixtures.RecoveryTests.finish
    numeric_fallback=False

    def setUp(self):
        self.setUpBase()
        self.f.jobs[1]['conclusion']='failure'
        self.owner=fixtures.fixtures.OWNER
        self.repository=fixtures.fixtures.REPOSITORY
        row=copy.deepcopy(queue(self.store,self.locale)[self.generation])
        row.pop('completion_sha256',None)
        self.row=row;self.snapshot=row['snapshot']
        self.save_row(row)
        self.jobs=[{**job,'id':21+index,'run_id':2,'head_sha':self.owner['sha'],'conclusion':'success'}
                   for index,job in enumerate(self.f.jobs)]
        self.run={**self.f.run_record,'id':2,'head_sha':self.owner['sha']}
        source=[{'continuation':True,'generation':self.generation,'day':self.f.origin['source_day'],
                 'locales_json':json.dumps([self.locale])}]
        translated=[{'generation':self.generation,'sha256':self.f.origin['source_sha256']},
            {'generation':self.generation,'locale':self.locale,'present':True,'sha256':self.snapshot['checkpoint_sha256']},
            {'generation':self.generation,'locale':self.locale,'sha256':self.snapshot['checkpoint_sha256'],'pointer_key':'private'},
            {'source_generation':self.generation,'locale':self.locale,'candidate_id':self.snapshot['candidate_id'],
             'manifest_sha256':self.snapshot['manifest_sha256'],'status':'complete-candidate','ready':True,
             'completed_page_count':self.f.origin['pages']}]
        self.logs={21:self.log(source),22:self.log(translated)}
        self.evidence={'producer':self.owner,'source_job_id':21,'locale_job_id':22,
            'source_log_sha256':digest(self.logs[21]),'locale_log_sha256':digest(self.logs[22]),
            'previous_checkpoint_sha256':self.snapshot['checkpoint_sha256']}

    def log(self, values):
        return ''.join('2026-10-12T01:00:00.000Z '+json.dumps(v)+'\n' for v in values).encode()

    def save_row(self,row):
        rows=queue(self.store,self.locale);rows[self.generation]=row;save_queue(self.store,self.locale,rows)
        raw=stable_bytes(row)
        self.store._put(self.store.key('incremental','continuation-results',self.generation,self.locale,digest(raw)+'.json'),
                        raw,metadata={'kind':'continuation-result'})

    def api(self,path):
        if '/compare/' in path:return {'status':'ahead','merge_base_commit':{'sha':self.f.origin['producer']['sha']}}
        if '/runs/1/' in path:return self.f.api(path)
        return {'total_count':len(self.jobs),'jobs':self.jobs} if '/jobs?' in path else self.run

    def raw(self,path,maximum):return self.logs[int(path.split('/')[-2])]

    def authenticate(self, *, evidence=None, capture=True, api=None, **kwargs):
        return completion.authenticate(self.store,self.f.origin,self.locale,self.repository,api or self.api,
            adoption=evidence or self.evidence,capture=capture,raw=self.raw,expected_snapshot=self.snapshot,**kwargs)

    def test_original_source_stays_required_and_exact_failed_run_jobs_can_prove_completion(self):
        with patch('portal_extended_recovered_admission.GitHub.raw',side_effect=self.raw):
            self.pipeline.authenticate_original(self.store,self.f.origin,self.repository,self.api,
                completion_evidence=self.evidence,capture=True,snapshot=self.snapshot)
        identity=self.authenticate()
        receipt=completion.optional(self.store,completion.receipt_key(self.store,identity))
        self.assertEqual(receipt['producer'],self.owner)
        self.assertEqual(receipt['snapshot'],self.snapshot)
        self.assertEqual(receipt['evidence']['source_log_sha256'],digest(self.logs[21]))
        self.assertEqual(self.run['conclusion'],'failure')
        self.f.jobs[0]['conclusion']='failure'
        with self.assertRaises(ExpansionError):
            self.pipeline.authenticate_original(self.store,self.f.origin,self.repository,self.api)

    def test_wrong_run_attempt_branch_job_and_hash_never_write(self):
        cases=[('run_attempt',2),('head_sha','f'*40),('head_branch','feature'),('status','in_progress')]
        for field,value in cases:
            with self.subTest(field=field):
                changed={**self.run,field:value};before=copy.deepcopy(self.client.objects)
                def api(path):return changed if '/runs/2/' in path and '/jobs?' not in path else self.api(path)
                with self.assertRaises(ExpansionError):self.authenticate(api=api)
                self.assertEqual(self.client.objects,before)
        for index in (0,1):
            saved=self.jobs[index]['conclusion'];self.jobs[index]['conclusion']='failure'
            before=copy.deepcopy(self.client.objects)
            with self.assertRaises(ExpansionError):self.authenticate()
            self.assertEqual(self.client.objects,before);self.jobs[index]['conclusion']=saved
        for field in ('source_log_sha256','locale_log_sha256','previous_checkpoint_sha256'):
            before=copy.deepcopy(self.client.objects)
            with self.assertRaises(ExpansionError):self.authenticate(evidence={**self.evidence,field:'f'*64})
            self.assertEqual(self.client.objects,before)

    def test_wrong_generation_and_each_render_identity_in_authenticated_logs_rejected(self):
        original=self.logs[22]
        for field in ('generation','source_generation','candidate_id','manifest_sha256','sha256'):
            with self.subTest(field=field):
                records=completion.log_records(original)
                for record in records:
                    if field in record:record[field]='e'*64
                self.logs[22]=self.log(records)
                evidence={**self.evidence,'locale_log_sha256':digest(self.logs[22])}
                before=copy.deepcopy(self.client.objects)
                with self.assertRaises(ExpansionError):self.authenticate(evidence=evidence)
                self.assertEqual(self.client.objects,before)
        self.logs[22]=original
        before=copy.deepcopy(self.client.objects)
        with self.assertRaises(ExpansionError):
            completion.authenticate(self.store,self.f.origin,self.locale,self.repository,self.api,
                adoption=self.evidence,capture=True,raw=self.raw,expected_snapshot={**self.snapshot,'candidate_id':'e'*64})
        self.assertEqual(self.client.objects,before)

    def test_readonly_does_not_capture_and_acknowledged_exact_row_retains_provenance(self):
        before=copy.deepcopy(self.client.objects)
        self.assertIsNone(self.authenticate(capture=False));self.assertEqual(self.client.objects,before)
        identity=self.authenticate()
        rows=queue(self.store,self.locale);del rows[self.generation];save_queue(self.store,self.locale,rows)
        self.assertEqual(self.authenticate(completed_row=self.row),identity)
        self.assertEqual(exact_result(self.store,self.locale,self.generation,self.row),self.row)

    def test_readonly_inspection_reports_exact_receipt_without_writes(self):
        from inspect_portal_extended_continuation import inspect
        identity=self.authenticate()
        before=copy.deepcopy(self.client.objects)
        value=inspect(self.store,self.generation,self.locale,self.snapshot['checkpoint_sha256'],
            self.snapshot['candidate_id'],self.f.root/'inspection')
        self.assertEqual(value['current_continuation']['completion_receipt_sha256'],identity)
        self.assertEqual(value['production_writes'],0)
        self.assertEqual(before,self.client.objects)

    def test_native_completion_preserves_actual_continuation_owner(self):
        active={**self.row,'status':'claimed','owner':self.owner}
        self.save_row(active)
        record_result(self.store,self.locale,self.f.corpus,
            {key:self.snapshot[key] for key in ('candidate_id','manifest_sha256')},
            checkpoint_sha=self.snapshot['checkpoint_sha256'],owner=self.owner)
        row=queue(self.store,self.locale)[self.generation]
        receipt=completion.optional(self.store,completion.receipt_key(self.store,row['completion_sha256']))
        self.assertEqual(receipt['producer'],self.owner)
        self.assertEqual(receipt['evidence'],{'kind':'native-result'})
        self.pipeline.authenticate_original(self.store,self.f.origin,self.repository,self.api)

    def test_unrelated_snapshot_cannot_borrow_receipt(self):
        identity=self.authenticate()
        receipt=completion.optional(self.store,completion.receipt_key(self.store,identity))
        # Keep every source identity but substitute a different snapshot. Its
        # content-addressed receipt has no verified chain to the current row.
        receipt['snapshot']={**receipt['snapshot'],'resolved_units':999}
        new_id=digest(stable_bytes(receipt))
        completion.immutable(self.store,completion.receipt_key(self.store,new_id),receipt)
        row={**self.row,'completion_sha256':new_id};self.save_row(row)
        with self.assertRaisesRegex(ExpansionError,'lineage_missing'):self.authenticate()

    def test_two_partial_repairs_retain_verified_exact_completion_chain(self):
        identity=self.authenticate()
        snapshots=[copy.deepcopy(self.snapshot)]
        root=self.f.root
        for index in range(2):
            with patch.object(recovery,'MAX_UNITS_PER_SCAN',1):
                jobs,blocked=recovery.prepare(self.store,(self.locale,),self.owner,self.repository,self.api)
            self.assertEqual(blocked,[]);self.assertEqual(len(jobs),1)
            self.f.root=root/str(index);self.f.root.mkdir()
            self.finish(jobs[0],fixtures.fixtures.RepairTranslator())
            snapshots.append(copy.deepcopy(queue(self.store,self.locale)[self.generation]['snapshot']))
            self.assertEqual(self.authenticate(),identity)
        self.assertEqual(len({v['candidate_id'] for v in snapshots}),3)
        self.assertEqual(debt_rows(self.store,self.locale),{})
        for snapshot in snapshots:
            self.assertEqual(completion.authenticate(self.store,self.f.origin,self.locale,self.repository,self.api,
                expected_snapshot=snapshot),identity)
        with self.assertRaisesRegex(ExpansionError,'requested_snapshot_differs'):
            completion.authenticate(self.store,self.f.origin,self.locale,self.repository,self.api,
                expected_snapshot={**snapshots[1],'resolved_units':999})
        row=copy.deepcopy(queue(self.store,self.locale)[self.generation])
        row['source_repair_sha256']='f'*64;self.save_row(row)
        with self.assertRaises(ExpansionError):self.authenticate()

    def test_ack_after_accepted_adoption_clears_tail_using_immutable_input(self):
        self.authenticate()
        jobs,blocked=recovery.prepare(self.store,(self.locale,),self.owner,self.repository,self.api)
        self.assertEqual(blocked,[])
        self.finish(jobs[0],fixtures.fixtures.RepairTranslator())
        self.assertEqual(debt_rows(self.store,self.locale),{})
        row=queue(self.store,self.locale)[self.generation]
        acknowledge_published(self.store,(self.locale,),[{'generation':self.generation,
            'candidates':{self.locale:row['snapshot']['candidate_id']}}])
        self.assertEqual(queue(self.store,self.locale),{})
        self.assertTrue(recovery.pending_tail_locales(self.store,(self.locale,)))
        before=copy.deepcopy(self.client.objects)
        resumed=recovery.resume_prepared(self.store,(self.locale,),{**self.owner,'run_id':'3'},self.repository,self.api)
        self.assertEqual(resumed,[])
        self.assertEqual(read_state(self.store,'quality-recovery-active',self.locale)['plan'],'')
        self.assertEqual(recovery.pending_tail_locales(self.store,(self.locale,)),())
        self.assertEqual(queue(self.store,self.locale),{})
        self.assertEqual(debt_rows(self.store,self.locale),{})
        permitted=state_key(self.store,'quality-recovery-active',self.locale)
        self.assertEqual({k:v for k,v in self.client.objects.items() if k!=permitted},
                         {k:v for k,v in before.items() if k!=permitted})


if __name__=='__main__':unittest.main()
