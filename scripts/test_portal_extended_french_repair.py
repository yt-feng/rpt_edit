"""Complete French candidate repair through real R2 state and publication contracts."""
from __future__ import annotations
import copy
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import portal_extended_french_repair as integrated
import repair_portal_french_source_fallback as helper
from build_portal_extended_locales import build
from portal_extended_continuation import register, read_origin, queue, save_queue
from portal_extended_incremental import read_state, write_state, state_key, remember_checkpoint, remember_candidate
from portal_extended_locales import ExpansionError, make_corpus, digest, stable_bytes, file_for_url
from portal_extended_r2 import R2Store, R2TransportError
from portal_extended_handoff import save_handoff, read_handoff, source_repair_proofs, source_repair_completions
from test_portal_extended_r2 import FakeR2
from test_portal_extended_incremental import DAY, URL, daily_doc, raw_page
from test_repair_portal_french_source_fallback import OriginalRejected, RepairTranslator, Precondition

ORIGINAL = {'run_id': '1', 'attempt': '1', 'sha': 'a'*40}
OWNER = {'run_id': '2', 'attempt': '1', 'sha': 'b'*40}
REPOSITORY = 'example/repo'
BODY = '<h1>Public research</h1><p>Revenue USD10m.</p><p>Profit USD2m.</p><p>Further research.</p>'
ROOT = Path(__file__).resolve().parent.parent


class Client(FakeR2):
    def __init__(self):
        super().__init__()
        self.writes = []
        self.fail_key = None
        self.fail_after = False
    def put_object(self, *, IfNoneMatch=None, **kwargs):
        key = kwargs['Key']
        if IfNoneMatch == '*' and key in self.objects: raise Precondition()
        if key == self.fail_key and not self.fail_after: raise TimeoutError('synthetic interruption')
        super().put_object(**kwargs)
        self.writes.append(key)
        if key == self.fail_key and self.fail_after: raise TimeoutError('synthetic interrupted acknowledgement')


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        environment = patch.dict(os.environ, {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
            'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REPOSITORY': REPOSITORY,
            'GITHUB_RUN_ID': '1', 'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': ORIGINAL['sha'],
            'KC_PUBLIC_REPOSITORY': 'true',
            'GITHUB_WORKFLOW_REF': REPOSITORY+'/'+integrated.WORKFLOW+'@refs/heads/main'})
        environment.start(); self.addCleanup(environment.stop)
        self.client = Client(); self.store = R2Store(self.client, 'private', '_extended-locales/staging/fr-repair')
        self.corpus = make_corpus([daily_doc(body=BODY), daily_doc(URL.replace('new','second'), body=BODY)])
        self.generation = self.corpus['documents_sha256']
        self.store.put_source(self.corpus)
        register(self.store, self.corpus, ('fr', 'de'), ORIGINAL)
        self.old_dir, self.old_path = self.root/'old', self.root/'old.json'
        self.old_manifest = build(self.corpus, 'fr', self.old_dir, self.old_path, OriginalRejected(),
                                  allow_source_fallback=True, budget_seconds=30)
        checkpoint = remember_checkpoint(self.store, 'fr', self.generation, self.old_path)
        candidate = remember_candidate(self.store, 'fr', self.corpus, self.old_dir)
        self.old_raw = self.old_path.read_bytes(); self.old = json.loads(self.old_raw)
        self.origin = read_origin(self.store, self.generation)
        self.before = copy.deepcopy(queue(self.store, 'fr')[self.generation])
        self.request = {'policy': helper.POLICY, 'validator_revision': helper.REVISION,
            'source_sha256': digest(stable_bytes(self.corpus)), 'origin_sha256': digest(stable_bytes(self.origin)),
            'producer': ORIGINAL, 'checkpoint_sha256': checkpoint['sha256'], 'candidate_id': candidate['candidate_id'],
            'manifest_sha256': candidate['manifest_sha256'], 'units': sorted(self.old['source_fallbacks'])}
        self.run_record = {'id': 1, 'run_attempt': 1, 'head_sha': ORIGINAL['sha'], 'status': 'completed',
            'conclusion': 'failure', 'head_branch': 'main', 'event': 'workflow_dispatch', 'path': integrated.WORKFLOW,
            'repository': {'full_name': REPOSITORY, 'private': False}, 'head_repository': {'full_name': REPOSITORY}}
        self.jobs = [{'name': name, 'run_id': 1, 'head_sha': ORIGINAL['sha'], 'status': 'completed',
            'conclusion': 'success', 'started_at': DAY+'T01:00:00Z', 'completed_at': DAY+'T01:10:00Z'}
            for name in ('source', 'locale (fr)')]
        self.args = SimpleNamespace(operation='prepare', generation=self.generation, locale='fr',
            checkpoint=self.root/'checkpoint.json', corpus=self.root/'source.json', output=self.root/'candidate',
            github_output=None, seconds=30)
        self.translator = RepairTranslator(terminal='Profit')

    def api(self, path):
        self.assertTrue(path.startswith('repos/'+REPOSITORY+'/actions/runs/1/attempts/1'))
        return {'total_count': len(self.jobs), 'jobs': self.jobs} if '/jobs?' in path else self.run_record

    def operation(self, operation, *, request=None):
        self.args.operation = operation
        output = io.StringIO()
        with redirect_stdout(output), patch('offline_translation.OfflineTranslator', return_value=self.translator):
            integrated.run(self.args, request or self.request, OWNER, store=self.store, repository=REPOSITORY, api=self.api)
        return json.loads(output.getvalue())

    def build_repair(self):
        self.assertTrue(self.operation('prepare')['has_work'])
        self.operation('restore')
        self.assertEqual(self.args.checkpoint.read_bytes(), self.old_raw)
        return self.operation('build')

    def finish(self):
        self.build_repair()
        return self.operation('persist')

    def test_real_restore_build_persist_preserves_origin_other_locale_and_counters(self):
        de_before = copy.deepcopy(queue(self.store, 'de'))
        original_manifest = (self.old_dir/'candidate-manifest.json').read_bytes()
        result = self.finish()
        row = queue(self.store, 'fr')[self.generation]
        self.assertTrue(result['changed']); self.assertEqual(result['residual_fallbacks'], 1)
        self.assertEqual(read_origin(self.store, self.generation), self.origin)
        self.assertEqual(queue(self.store, 'de'), de_before)
        self.assertEqual({k:v for k,v in row.items() if k not in {'snapshot','source_repair_sha256'}},
                         {k:v for k,v in self.before.items() if k != 'snapshot'})
        self.assertEqual(row['snapshot']['completed_pages'], self.before['snapshot']['completed_pages'])
        self.assertEqual(row['snapshot']['resolved_units'], self.before['snapshot']['resolved_units'])
        self.assertNotEqual(row['snapshot']['candidate_id'], self.request['candidate_id'])
        self.assertEqual(self.store._get(self.store.candidate_manifest_key('fr', self.generation,
            self.request['candidate_id']), maximum=2**21), original_manifest)
        self.assertEqual(len(self.translator.calls), 2)
        proof = integrated.verify_proof(self.store, result['proof_sha256'], self.generation)
        self.assertEqual(proof['before_row'], self.before)
        self.assertEqual(proof['delta']['terminal_units'], [key for key in self.request['units']
            if 'Profit' in self.old['source_fallbacks'][key]['source']])

    def test_advanced_global_memo_retains_generation_unrelated_rows_and_its_checkpoint_pointer(self):
        self.build_repair()
        later = 'f'*64
        memo = copy.deepcopy(self.old); memo['source_generation'] = later
        memo['rows']['9'*64] = {'source': 'A newer independent unit.', 'language': 'en', 'text': 'Une nouvelle unité indépendante.'}
        path = self.root/'later.json'; path.write_bytes(stable_bytes(memo))
        pointer = self.store.put_checkpoint('fr', later, path)
        write_state(self.store, 'memo', 'fr', {'generation': later, 'sha256': pointer['sha256'], 'preserved_marker':'exact'})
        result = self.operation('persist')
        latest = read_state(self.store, 'memo', 'fr')
        self.assertEqual(latest['generation'], later); self.assertEqual(latest['preserved_marker'], 'exact')
        merged = json.loads(self.store._get(self.store.checkpoint_object_key('fr', later, latest['sha256']), maximum=2**23))
        self.assertEqual(merged['rows']['9'*64], memo['rows']['9'*64])
        self.assertEqual(len(merged['source_fallbacks']), 1)
        restored = self.store.restore_checkpoint('fr', later, self.root/'later-readback.json')
        self.assertEqual(restored['sha256'], pointer['sha256'])
        integrated.verify_proof(self.store, result['proof_sha256'], self.generation)

    def test_newer_selected_memo_translation_is_not_overwritten(self):
        self.build_repair()
        memo = copy.deepcopy(self.old); selected = next(k for k in self.request['units'] if 'Revenue' in self.old['source_fallbacks'][k]['source'])
        memo['rows'][selected] = {'source': self.old['source_fallbacks'][selected]['source'], 'language':'en', 'text':'Autre version USD10m.'}
        del memo['source_fallbacks'][selected]
        path=self.root/'newer.json'; path.write_bytes(stable_bytes(memo))
        pointer=self.store.put_checkpoint('fr', self.generation, path)
        write_state(self.store,'memo','fr',{'generation':self.generation,'sha256':pointer['sha256']})
        before=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'newer memo unit'): self.operation('persist')
        self.assertEqual(self.client.objects, before)

    def test_newer_completed_source_receipt_prevents_even_model_claim(self):
        pages=read_state(self.store,'completed','fr',DAY)['pages']
        pages[URL]['generation']='d'*64
        write_state(self.store,'completed','fr',{'pages':pages},DAY)
        before=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'newer completed page'): self.operation('prepare')
        self.assertEqual(self.client.objects,before); self.assertEqual(self.translator.calls,[])

    def test_manifest_written_ready_missing_can_resume_without_reopening_model(self):
        self.build_repair()
        manifest=json.loads((self.args.output/'candidate-manifest.json').read_bytes())
        ready=self.store.candidate_ready_key('fr',self.generation,manifest['files_sha256'])
        self.client.fail_key=ready
        with self.assertRaises(R2TransportError): self.operation('persist')
        self.assertNotIn(ready,self.client.objects)
        self.assertIn(self.store.candidate_manifest_key('fr',self.generation,manifest['files_sha256']),self.client.objects)
        self.assertEqual(queue(self.store,'fr')[self.generation],self.before)
        calls=list(self.translator.calls); self.client.fail_key=None
        result=self.operation('persist')
        self.assertTrue(result['changed']); self.assertIn(ready,self.client.objects)
        self.assertEqual(self.translator.calls,calls)

    def test_partial_mutable_tail_resumes_prepared_proof_without_model(self):
        self.build_repair()
        self.client.fail_key=state_key(self.store,'completed','fr',DAY)
        with self.assertRaises(R2TransportError): self.operation('persist')
        identity=integrated.prepared_proof(self.store,self.request)
        self.assertIsNotNone(identity)
        self.assertEqual(queue(self.store,'fr')[self.generation],self.before)
        calls=list(self.translator.calls); self.client.fail_key=None
        self.assertFalse(self.operation('prepare')['has_work'])
        self.assertEqual(queue(self.store,'fr')[self.generation]['source_repair_sha256'],identity)
        self.assertEqual(self.translator.calls,calls)

    def test_prepared_tail_refuses_global_memo_that_advanced_after_capture(self):
        self.build_repair(); self.client.fail_key=state_key(self.store,'completed','fr',DAY)
        with self.assertRaises(R2TransportError): self.operation('persist')
        self.client.fail_key=None
        write_state(self.store,'memo','fr',{'generation':'c'*64,'sha256':'d'*64})
        before=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError,'memo advanced'): self.operation('prepare')
        self.assertEqual(self.client.objects,before)

    def test_no_page_change_does_not_overwrite_same_candidate_or_any_mutable_state(self):
        self.translator=RepairTranslator(unchanged=True)
        self.build_repair(); before=copy.deepcopy(self.client.objects)
        result=self.operation('persist')
        self.assertFalse(result['changed'])
        self.assertEqual(queue(self.store,'fr')[self.generation],self.before)
        for name,value in before.items(): self.assertEqual(self.client.objects[name],value)
        new_names=set(self.client.objects)-set(before)
        self.assertTrue(all('/source-fallback-repair' in name for name in new_names))

    def test_inspector_lists_eligible_hashes_without_claim_model_or_write(self):
        request={k:v for k,v in self.request.items() if k not in {'origin_sha256','source_sha256'}}; request['units']=[]
        before=copy.deepcopy(self.client.objects)
        result=self.operation('inspect',request=request)
        self.assertEqual(result['inspection']['eligible_units'],self.request['units'])
        self.assertEqual(result['frozen_request']['origin_sha256'],self.request['origin_sha256'])
        self.assertEqual(result['inspection']['storage_writes'],0); self.assertEqual(result['inspection']['model_calls'],0)
        self.assertEqual(self.client.objects,before); self.assertEqual(self.translator.calls,[])

    def test_inspector_and_mutation_require_completed_original_run(self):
        self.run_record['status']='in_progress'; self.run_record['conclusion']=None
        before=copy.deepcopy(self.client.objects)
        for operation in ('inspect','prepare'):
            with self.subTest(operation=operation), self.assertRaises(ExpansionError): self.operation(operation)
        self.assertEqual(self.client.objects,before)

    def test_changed_restored_checkpoint_fails_before_model(self):
        self.operation('prepare'); self.operation('restore'); self.args.checkpoint.write_bytes(b'{}')
        before=copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError,'exact restored checkpoint'): self.operation('build')
        self.assertEqual(self.client.objects,before); self.assertEqual(self.translator.calls,[])

    def test_handoff_binds_exact_proof_and_immutable_new_candidate(self):
        self.translator = RepairTranslator()
        result=self.finish(); row=queue(self.store,'fr')[self.generation]
        batch={'generation':self.generation,'candidates':{'fr':row['snapshot']['candidate_id']}}
        identity=save_handoff(self.store,batch,day=DAY,pages=2,producer=OWNER)
        receipt=read_handoff(self.store,identity)
        self.assertEqual(receipt['source_repair_proofs'],{'fr':result['proof_sha256']})
        for change in ('candidate','checkpoint','origin','locale'):
            corrupted=copy.deepcopy(receipt)
            if change=='candidate': corrupted['batch']['candidates']['fr']='a'*64
            elif change=='checkpoint': corrupted['continuation_checkpoints']['fr']='a'*64
            elif change=='origin': corrupted['source_origin_sha256']='a'*64
            else: corrupted['source_repair_proofs']['de']=corrupted['source_repair_proofs'].pop('fr')
            raw=stable_bytes(corrupted); checksum=digest(raw)
            self.store._put(self.store.key('publication-handoffs',checksum,'receipt.json'),raw,metadata={'kind':'fixture'})
            with self.subTest(change=change), self.assertRaises(ExpansionError): read_handoff(self.store,checksum)

    def test_partial_repair_retains_debt_and_cannot_auto_publish(self):
        from portal_extended_quality import quality_summary
        result = self.finish()
        row = queue(self.store, 'fr')[self.generation]
        batch = {'generation': self.generation, 'candidates': {'fr': row['snapshot']['candidate_id']}}
        self.assertTrue(result['changed'])
        with self.assertRaisesRegex(ExpansionError, 'translated-ready'):
            save_handoff(self.store, batch, day=DAY, pages=2, producer=OWNER)
        self.assertEqual(quality_summary(self.store, ('fr',))['quality_debt_source_fallback_units'], 1)
        self.assertIn(self.generation, queue(self.store, 'fr'))

    def test_repair_producer_requires_main_manual_exact_successful_source_and_fr_jobs(self):
        result=self.finish(); proof=integrated.verify_proof(self.store,result['proof_sha256'],self.generation)
        run={**self.run_record,'id':2,'head_sha':OWNER['sha']}
        jobs=[{**job,'run_id':2,'head_sha':OWNER['sha']} for job in self.jobs]
        integrated.verify_repair_producer(proof,run,jobs,REPOSITORY)
        cases=[({'event':'workflow_run'},jobs),({'head_branch':'other'},jobs),({'id':3},jobs),
               ({'status':'in_progress'},jobs),({},[{**jobs[0],'conclusion':'failure'},jobs[1]]),
               ({},[jobs[0],{**jobs[1],'head_sha':'c'*40}]),({},jobs+[jobs[1]])]
        for changed,changed_jobs in cases:
            with self.subTest(changed=changed),self.assertRaises(ExpansionError):
                integrated.verify_repair_producer(proof,{**run,**changed},changed_jobs,REPOSITORY)

    def test_proof_cannot_change_continuation_counter(self):
        result=self.finish(); proof=integrated.verify_proof(self.store,result['proof_sha256'],self.generation)
        proof['after_row']['continuations']+=1
        identity=digest(stable_bytes(proof))
        self.store._put(integrated.proof_key(self.store,identity),stable_bytes(proof),metadata={'kind':'fixture'})
        with self.assertRaisesRegex(ExpansionError,'continuation counters'): integrated.verify_proof(self.store,identity,self.generation)

    def test_failed_persist_new_source_only_run_completes_and_passes_handoff_review(self):
        self.translator = RepairTranslator()
        self.build_repair(); self.client.fail_key=state_key(self.store,'completed','fr',DAY)
        with self.assertRaises(R2TransportError): self.operation('persist')
        identity=integrated.prepared_proof(self.store,self.request)
        original_calls=list(self.translator.calls); self.client.fail_key=None
        resumer={'run_id':'3','attempt':'1','sha':'c'*40}
        self.args.operation='prepare'
        with redirect_stdout(io.StringIO()):
            integrated.run(self.args,self.request,resumer,store=self.store,repository=REPOSITORY,api=self.api)
        row=queue(self.store,'fr')[self.generation]
        batch={'generation':self.generation,'candidates':{'fr':row['snapshot']['candidate_id']}}
        receipt=read_handoff(self.store,save_handoff(self.store,batch,day=DAY,pages=2,producer=resumer))
        proof=source_repair_proofs(self.store,receipt)['fr']
        completion=source_repair_completions(self.store,receipt,{'fr':proof})['fr']
        self.assertEqual(proof['producer'],OWNER); self.assertEqual(completion['producer'],resumer)
        self.assertEqual(completion['proof_sha256'],identity)
        run={**self.run_record,'id':3,'head_sha':resumer['sha'],'conclusion':'success'}
        jobs=[{**self.jobs[0],'run_id':3,'head_sha':resumer['sha']},
              {**self.jobs[1],'name':'locale','run_id':3,'head_sha':resumer['sha'],'conclusion':'skipped'}]
        integrated.verify_repair_producer(proof,run,jobs,REPOSITORY,completion=completion)
        with self.assertRaises(ExpansionError): integrated.verify_repair_producer(proof,run,jobs,REPOSITORY)
        for change in ({'conclusion':'failure'},{'conclusion':'success'},{'head_sha':'d'*40}):
            with self.subTest(change=change),self.assertRaises(ExpansionError):
                integrated.verify_repair_producer(proof,run,[jobs[0],{**jobs[1],**change}],REPOSITORY,completion=completion)
        before=copy.deepcopy(self.client.objects)
        with redirect_stdout(io.StringIO()):
            integrated.run(self.args,self.request,resumer,store=self.store,repository=REPOSITORY,api=self.api)
        self.assertEqual(self.client.objects,before); self.assertEqual(self.translator.calls,original_calls)

    def test_second_batch_after_resumed_first_batch_replaces_only_new_units_and_drops_old_completion(self):
        selected=next(k for k in self.request['units'] if 'Revenue' in self.old['source_fallbacks'][k]['source'])
        self.request['units']=[selected]
        self.build_repair(); self.client.fail_key=state_key(self.store,'completed','fr',DAY)
        with self.assertRaises(R2TransportError): self.operation('persist')
        self.client.fail_key=None; self.operation('prepare')
        previous=queue(self.store,'fr')[self.generation]
        self.assertIn('source_repair_completion_sha256',previous)
        first_calls=len(self.translator.calls)
        self.request={**self.request,**{key:previous['snapshot'][key]
            for key in ('candidate_id','checkpoint_sha256','manifest_sha256')},
            'units':[key for key in sorted(self.old['source_fallbacks']) if key!=selected]}
        self.old_raw=self.store._get(self.store.checkpoint_object_key('fr',self.generation,self.request['checkpoint_sha256']),maximum=2**23)
        self.args.checkpoint=self.root/'second-checkpoint.json'; self.args.output=self.root/'second-candidate'
        self.translator=RepairTranslator()
        result=self.finish(); row=queue(self.store,'fr')[self.generation]
        self.assertTrue(result['changed']); self.assertEqual(result['residual_fallbacks'],0)
        self.assertNotIn('source_repair_completion_sha256',row)
        self.assertEqual(row['continuations'],previous['continuations'])
        self.assertEqual(first_calls,1); self.assertEqual(len(self.translator.calls),1)
        batch={'generation':self.generation,'candidates':{'fr':row['snapshot']['candidate_id']}}
        receipt=read_handoff(self.store,save_handoff(self.store,batch,day=DAY,pages=2,producer=OWNER))
        self.assertNotIn('source_repair_completions',receipt)

    def test_publication_appends_new_full_candidate_without_rewriting_active_approval(self):
        from test_portal_extended_publication import PublicationTests
        from portal_extended_publication import compose
        fixture=PublicationTests(); fixture.setUp(); self.addCleanup(fixture.doCleanups)
        result=self.finish(); row=queue(self.store,'fr')[self.generation]
        old={'generation':self.generation,'candidates':{'fr':self.request['candidate_id']}}
        new={'generation':self.generation,'candidates':{'fr':row['snapshot']['candidate_id']}}
        for doc in self.corpus['documents']:
            path=fixture.root/file_for_url(doc['url']); path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(raw_page(doc['url'],body=BODY))
        work=self.root/'publication'; work.mkdir()
        with patch('portal_extended_publication.read_active_ledger',return_value={'batches':[old]}):
            assembled=compose(fixture.root,self.store,[old,new],work,active_identity={'slot':'a'})
        self.assertEqual(assembled['batches'],[old,new])
        self.assertEqual(len(assembled['replays']),1)
        self.assertEqual(assembled['replays'][0]['approved_candidate'],new['candidates']['fr'])
        self.assertEqual(assembled['replays'][0]['translation_calls'],0)
        integrated.verify_proof(self.store,result['proof_sha256'],self.generation)

    def test_cli_inspect_routes_only_reviewed_main_supported_policy(self):
        import repair_portal_extended_checkpoint as cli
        args=['repair_portal_extended_checkpoint.py','inspect','--generation',self.generation,'--locale','fr',
              '--request',json.dumps({**self.request,'units':[]})]
        with patch('sys.argv',args),patch.object(cli,'once_store',return_value=self.store), \
             patch('review_portal_extended_handoff.api',side_effect=self.api),redirect_stdout(io.StringIO()):
            self.assertEqual(cli.main(),0)
        with patch('sys.argv',args),patch.dict(os.environ,{'GITHUB_REF':'refs/heads/unreviewed'}), \
             patch.object(cli,'once_store') as store:
            with self.assertRaises(ExpansionError): cli.main()
            store.assert_not_called()

    def test_workflow_inspect_has_no_locale_or_publication_work_and_retains_two_workers(self):
        path=ROOT/'.github/workflows/portal-extended-locales-r2.yml'
        try:
            import yaml
        except ImportError:
            raw=subprocess.check_output(['/usr/bin/ruby','-ryaml','-rjson','-e','puts JSON.generate(YAML.load_file(ARGV[0]))',str(path)],text=True)
            workflow=json.loads(raw)
        else:
            workflow=yaml.safe_load(path.read_text())
        jobs=workflow['jobs']
        trigger=workflow.get('on',workflow.get(True,workflow.get('true')))
        self.assertLessEqual(len(trigger['workflow_dispatch'].get('inputs',{})),25)
        self.assertEqual(len(trigger['workflow_dispatch']['inputs']),7)
        for job in jobs.values():
            self.assertNotIn('runner.',json.dumps(job.get('env',{})))
        self.assertEqual(jobs['locale']['strategy']['max-parallel'],2)
        self.assertIn("needs.source.outputs.has_work == 'true'",jobs['locale']['if'])
        self.assertIn("inputs.operation == 'source-fallback-inspect'",jobs['source']['if'])
        self.assertNotIn('source-fallback-inspect',jobs['publication_handoff']['if'])
        source=next(step for step in jobs['source']['steps'] if step.get('id')=='source')['run']
        branch=source.split('if [ "$REQUESTED_OPERATION" = "source-fallback-inspect" ]; then')[1].split('fi',1)[0]
        self.assertIn('repair_portal_extended_checkpoint.py inspect',branch)
        self.assertIn('exit 0',branch)
        self.assertFalse(workflow['concurrency']['cancel-in-progress'])


if __name__=='__main__': unittest.main()
