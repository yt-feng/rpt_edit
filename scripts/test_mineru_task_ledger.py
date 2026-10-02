#!/usr/bin/env python3
"""Offline failure-class regressions. No provider, R2 or publication calls."""
from __future__ import annotations
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import mineru_task_ledger as m

OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}
TOKENS = [('MINER_U', 'private-test-token'), ('MINER_U_2', 'different-test-token')]
ROOT = Path(__file__).resolve().parents[1]


class Clock:
    now = 0
    def time(self): return self.now
    def sleep(self, seconds): self.now += seconds


class FakeProvider:
    def __init__(self):
        self.posts, self.uploads, self.polls, self.tasks = [], [], [], {}
        self.mode = 'pending'
        self.on_submit = None
        self.on_upload = None
        self.custom_rows = None
    def submit(self, items, options, token, timeout):
        key = str(len(self.posts) + 1)
        self.posts.append((copy.deepcopy(items), options, token, timeout))
        self.tasks[key] = copy.deepcopy(items)
        if self.on_submit: self.on_submit()
        return key, ['https://upload.invalid/' + item['id'] for item in items]
    def upload(self, url, raw, timeout):
        self.uploads.append((url, raw, timeout))
        if self.on_upload: self.on_upload()
    def poll(self, batch_id, token, timeout):
        self.polls.append((batch_id, token, timeout))
        if self.custom_rows is not None: return self.custom_rows(self.tasks[batch_id])
        return [{'data_id': item['id'], 'state': self.mode,
                 **({'full_zip_url': 'https://results.invalid/' + item['id']} if self.mode == 'done' else {})}
                for item in self.tasks[batch_id]]


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store = m.FileStore(self.root / 'ledger')
        self.provider = FakeProvider()
        self.clock = Clock()
        self.inputs = []
        for index in range(5):
            path = self.root / f'{index}.pdf'; path.write_bytes(b'%PDF-' + bytes([index]))
            self.inputs.append((path, f'source/{index}.pdf'))
    def ledger(self, **kw):
        return m.Ledger(kw.pop('store', self.store), self.provider, kw.pop('scope', 'daily'),
                        'https://mineru.net', kw.pop('options', OPTIONS), kw.pop('tokens', TOKENS),
                        clock=self.clock.time, sleep=self.clock.sleep, **kw)
    def run_task(self, inputs=None, **kw):
        return self.ledger(**kw).run(inputs or self.inputs, timeout=20, interval=2, queue_budget=4)
    def rewrite_batch(self, change):
        path = next((self.root / 'ledger/batches').glob('*.json'))
        value = json.loads(path.read_text()); change(value); path.write_bytes(m.encoded(value))
    def test_five_pdfs_one_post_and_original_token_survives_days_and_rotation(self):
        for day in range(4):
            self.clock.now += 86400
            _, summary = self.run_task(tokens=list(reversed(TOKENS)) if day else TOKENS)
            self.assertEqual(summary['pending'], 5)
        self.assertEqual(len(self.provider.posts), 1)
        self.assertEqual(len(self.provider.uploads), 5)
        self.assertTrue(all(row[1] == TOKENS[0][1] for row in self.provider.polls))
        self.provider.mode = 'done'
        rows, summary = self.run_task()
        self.assertEqual((len(rows), summary['pending'], len(self.provider.posts)), (5, 0, 1))
        self.assertLessEqual(self.clock.now % 86400, 20)
    def test_regrouped_subset_reuses_original_batch(self):
        self.run_task()
        self.provider.mode = 'done'
        rows, summary = self.run_task(self.inputs[::2])
        self.assertEqual({p for p, _ in rows}, {p for p, _ in self.inputs[::2]})
        self.assertEqual(summary['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 1)
    def test_only_new_sources_submitted_when_regrouped(self):
        self.run_task(self.inputs[:2]); self.run_task(self.inputs[1:])
        self.assertEqual([len(row[0]) for row in self.provider.posts], [2, 3])
        self.assertEqual(len({item['id'] for row in self.provider.posts for item in row[0]}), 5)
    def test_pending_never_switches_to_another_credential(self):
        self.run_task(); self.run_task()
        self.assertEqual({row[1] for row in self.provider.polls}, {TOKENS[0][1]})
        self.assertEqual(len(self.provider.posts), 1)
    def test_missing_original_token_fails_before_any_provider_call(self):
        self.run_task(); previous = len(self.provider.polls)
        with self.assertRaises(m.LedgerError): self.run_task(tokens=TOKENS[1:])
        self.assertEqual((len(self.provider.posts),len(self.provider.polls)), (1, previous))
    def test_provider_terminal_failure_retained_never_retried(self):
        self.provider.mode = 'failed'
        for _ in range(3):
            rows, summary = self.run_task()
            self.assertEqual((rows,summary['failed'],summary['pending']), ([],5,0))
        self.assertEqual(len(self.provider.posts),1)
    def test_truncated_rows_never_mean_complete(self):
        self.provider.custom_rows = lambda items: [{'data_id': items[0]['id'], 'state':'done', 'full_zip_url':'https://result.invalid'}]
        rows, summary = self.run_task()
        self.assertEqual((len(rows),summary['pending']), (1,4))
        self.assertEqual(len(self.provider.posts), 1)
    def test_terminal_batch_cannot_regress_or_truncate(self):
        self.provider.mode = 'done'; self.run_task()
        self.provider.custom_rows = lambda items: []
        with self.assertRaises(m.LedgerError): self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_malformed_unknown_duplicate_and_unsigned_result_fail_closed(self):
        cases = [lambda items: {}, lambda items: [{'data_id':'unrequested','state':'done'}],
                 lambda items: [{'data_id':items[0]['id'],'state':'surprise'}],
                 lambda items: [{'data_id':items[0]['id'],'state':'done','full_zip_url':'http://unsafe'}],
                 lambda items: [{'data_id':items[0]['id'],'state':'pending'}]*2]
        self.run_task()
        for rows in cases:
            self.provider.custom_rows = rows
            with self.assertRaises(m.LedgerError): self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_unknown_post_outcome_blocks_every_future_attempt(self):
        self.provider.on_submit = lambda: (_ for _ in ()).throw(TimeoutError('unknown'))
        with self.assertRaises(TimeoutError): self.run_task()
        self.provider.on_submit = None
        for _ in range(3):
            with self.assertRaisesRegex(m.LedgerError, 'Ambiguous'): self.run_task()
        self.assertEqual(len(self.provider.posts),1)
        self.assertEqual(len(self.provider.polls),0)
    def test_ack_is_durable_before_first_upload_and_upload_loss_never_posts_again(self):
        def interrupted():
            value=json.loads(next((self.root/'ledger/batches').glob('*.json')).read_text())
            self.assertEqual((value['state'],value['batch_id']), ('accepted','1'))
            raise TimeoutError('lost upload')
        self.provider.on_upload = interrupted
        with self.assertRaises(TimeoutError): self.run_task()
        self.provider.on_upload = None
        self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_failed_ack_persistence_leaves_ambiguous_intent(self):
        actual = self.store.put
        def write(key,value,previous=None):
            if value.get('state') == 'accepted': raise OSError('store unavailable')
            return actual(key,value,previous)
        with patch.object(self.store,'put',side_effect=write), self.assertRaises(OSError): self.run_task()
        with self.assertRaises(m.LedgerError): self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_partial_claims_fail_before_post_and_do_not_expire(self):
        actual=self.store.put; count=0
        def write(key,value,previous=None):
            nonlocal count
            if key.startswith('sources/'):
                count+=1
                if count==2: raise OSError('runner stopped')
            return actual(key,value,previous)
        with patch.object(self.store,'put',side_effect=write), self.assertRaises(OSError): self.run_task()
        self.clock.now += 7*86400
        with self.assertRaises(m.LedgerError): self.run_task()
        self.assertEqual(len(self.provider.posts),0)
    def test_concurrent_claim_conflict_does_not_submit(self):
        actual=self.store.put
        def write(key,value,previous=None):
            if key.startswith('sources/'):
                actual(key,value)
            return actual(key,value,previous)
        with patch.object(self.store,'put',side_effect=write), self.assertRaises(m.LedgerError): self.run_task()
        self.assertEqual(len(self.provider.posts),0)
    def test_tampered_binding_scope_or_batch_references_block_new_work(self):
        self.run_task(self.inputs[:2])
        path=next((self.root/'ledger/sources').glob('*.json')); original=path.read_bytes()
        for key,value in [('batch_key','batches/../../other'),('binding',{}),('schema',99)]:
            ref=json.loads(original);ref[key]=value;path.write_bytes(m.encoded(ref))
            with self.assertRaises(m.LedgerError): self.run_task()
            self.assertEqual(len(self.provider.posts),1)
        path.write_bytes(original)
        self.rewrite_batch(lambda b: b.update(scope='other'))
        with self.assertRaises(m.LedgerError): self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_bytes_changed_after_admission_never_upload_wrong_source(self):
        self.provider.on_submit=lambda:self.inputs[0][0].write_bytes(b'changed')
        with self.assertRaisesRegex(m.LedgerError,'bytes changed'): self.run_task()
        self.assertEqual(len(self.provider.uploads),0)
    def test_source_mutation_during_poll_cannot_return_other_bytes(self):
        def changed(items):
            self.inputs[0][0].write_bytes(b'changed while waiting')
            return [{'data_id':item['id'],'state':'done','full_zip_url':'https://result.invalid'} for item in items]
        self.provider.custom_rows=changed
        with self.assertRaisesRegex(m.LedgerError,'during polling'): self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_new_content_and_new_options_have_distinct_claims(self):
        self.run_task(self.inputs[:1]); self.inputs[0][0].write_bytes(b'new exact source')
        self.run_task(self.inputs[:1]); self.run_task(self.inputs[:1], options=dict(OPTIONS,ocr=False))
        self.assertEqual(len(self.provider.posts),3)
        self.assertEqual(len({row[0][0]['id'] for row in self.provider.posts}),3)
    def test_invalid_scope_endpoint_paths_and_batch_size_have_no_provider_calls(self):
        for scope in ('../escape','', 'Upper'):
            with self.assertRaises(m.LedgerError): self.ledger(scope=scope)
        for source in ('../escape.pdf','/absolute.pdf','dir\\escape.pdf'):
            with self.assertRaises(m.LedgerError): self.run_task([(self.inputs[0][0],source)])
        with self.assertRaises(m.LedgerError): self.run_task(self.inputs+self.inputs[:1])
        with self.assertRaises(m.LedgerError): self.run_task([self.inputs[0]]*2)
        self.assertEqual(len(self.provider.posts),0)
    def test_corrupt_checkpoint_does_not_look_absent(self):
        self.run_task(); next((self.root/'ledger/sources').glob('*.json')).write_bytes(b'{')
        with self.assertRaises(m.LedgerError):self.run_task()
        self.assertEqual(len(self.provider.posts),1)
    def test_checkpoint_contains_neither_tokens_nor_signed_urls_or_pdf_content(self):
        self.run_task(); raw=b'\n'.join(p.read_bytes() for p in (self.root/'ledger').rglob('*.json'))
        for secret in [t.encode() for _,t in TOKENS]+[b'https://upload.invalid',b'https://results.invalid',b'%PDF-']:
            self.assertNotIn(secret,raw)
    def test_two_independent_store_instances_share_exact_task(self):
        self.run_task(); self.run_task(store=m.FileStore(self.root/'ledger'))
        self.assertEqual(len(self.provider.posts),1)
    def test_attempt_budget_is_shared_across_regrouped_batches(self):
        self.run_task(self.inputs[:1]);self.run_task(self.inputs[1:2]);begun=self.clock.now
        self.ledger().run(self.inputs[:2],timeout=3,interval=2,queue_budget=600)
        self.assertEqual(self.clock.now-begun,3)
        self.assertTrue(all(call[2] <= 20 for call in self.provider.polls))


class ProviderContractTests(unittest.TestCase):
    def test_native_payload_and_exact_poll_identity_preserve_batching(self):
        http=unittest.mock.Mock()
        response=unittest.mock.Mock(status_code=200)
        response.json.return_value={'code':0,'data':{'batch_id':'accepted/batch', 'file_urls':['https://upload.invalid']*5}}
        http.post.return_value=response
        provider=m.Provider(http,'https://mineru.net')
        items=[{'source':f'folder/{i}.pdf','id':str(i)*64} for i in range(5)]
        batch,urls=provider.submit(items,OPTIONS,'secret-token',8)
        self.assertEqual((batch,len(urls)),('accepted/batch',5))
        sent=http.post.call_args.kwargs
        self.assertEqual(len(sent['json']['files']),5)
        self.assertEqual(sent['json']['files'][0],{'name':'0.pdf','data_id':'0'*64,'is_ocr':True})
        self.assertEqual(sent['headers']['Authorization'],'Bearer secret-token')
        self.assertEqual(sent['timeout'],8)
        http.get.return_value=response
        response.json.return_value={'code':0,'data':{'extract_result':[]}}
        self.assertEqual(provider.poll(batch,'secret-token',7),[])
        self.assertTrue(http.get.call_args.args[0].endswith('/accepted%2Fbatch'))
        self.assertEqual(http.get.call_args.kwargs['timeout'],7)
    def test_unknown_post_is_not_retried_and_error_contains_no_token(self):
        http=unittest.mock.Mock();http.post.side_effect=TimeoutError('secret-token https://signed.invalid')
        with self.assertRaises(m.LedgerError) as captured:
            m.Provider(http,'https://mineru.net').submit([{'source':'a.pdf','id':'a'*64}],OPTIONS,'secret-token',5)
        self.assertEqual(http.post.call_count,1)
        self.assertNotIn('secret-token',str(captured.exception))
        self.assertNotIn('signed.invalid',str(captured.exception))
    def test_incomplete_ack_or_rejected_upload_fail_closed(self):
        http=unittest.mock.Mock();response=unittest.mock.Mock(status_code=200)
        http.post.return_value=response
        provider=m.Provider(http,'https://mineru.net')
        for data in ({'batch_id':'accepted','file_urls':[]},{'file_urls':['https://upload.invalid']}, {'batch_id':'accepted','file_urls':['http://upload.invalid']}):
            response.json.return_value={'code':0,'data':data}
            with self.assertRaises(m.LedgerError):provider.submit([{'source':'a.pdf','id':'a'*64}],OPTIONS,'token',5)
        http.put.return_value=unittest.mock.Mock(status_code=500)
        with self.assertRaises(m.LedgerError):provider.upload('https://upload.invalid',b'bytes',4)
        self.assertEqual(http.put.call_args.kwargs['timeout'],4)


class FakeR2:
    def __init__(self):self.objects={}
    def get_object(self, **kw):
        if kw['Key'] not in self.objects:
            error=RuntimeError('missing'); error.response={'Error':{'Code':'NoSuchKey'}};raise error
        row=copy.deepcopy(self.objects[kw['Key']]);row['Body']=io.BytesIO(row['Body']);return row
    def put_object(self, **kw):
        old=self.objects.get(kw['Key'])
        if (kw.get('IfNoneMatch')=='*' and old) or ('IfMatch' in kw and (not old or old['ETag']!=kw['IfMatch'])):
            error=RuntimeError('PreconditionFailed')
            error.response={'Error':{'Code':'PreconditionFailed'},'ResponseMetadata':{'HTTPStatusCode':412}}
            raise error
        etag='"'+m.digest(kw['Body'])+'"'
        self.objects[kw['Key']]={'ETag':etag,'ContentLength':len(kw['Body']),'Metadata':kw['Metadata'],'Body':kw['Body']}
        return {'ETag':etag}


class StoreAndIntegrationTests(unittest.TestCase):
    def test_r2_conditional_create_and_update_reject_competing_writer(self):
        client=FakeR2();store=m.R2Store('daily',client=client,bucket='private');key='batches/'+'a'*32
        first=store.put(key,{'state':'claimed'})
        with self.assertRaises(m.LedgerError):store.put(key,{'state':'other'})
        second=store.put(key,{'state':'accepted'},first)
        with self.assertRaises(m.LedgerError):store.put(key,{'state':'bad'},first)
        self.assertEqual(store.get(key),({'state':'accepted'},second))
    def test_r2_corruption_missing_metadata_and_truncation_fail_closed(self):
        for mutate in [lambda o:o.update(ContentLength=999),lambda o:o.update(Metadata={}),
                       lambda o:o.update(Body=b'{'),lambda o:o.update(ETag=''),lambda o:o.update(ContentLength=10**9)]:
            client=FakeR2();store=m.R2Store('daily',client=client,bucket='private');key='sources/'+'b'*64
            store.put(key,{'state':'saved'});mutate(next(iter(client.objects.values())))
            with self.assertRaises(m.LedgerError):store.get(key)
    def test_r2_lost_write_ack_requires_exact_durable_readback_without_second_put(self):
        client=FakeR2();store=m.R2Store('daily',client=client,bucket='private');key='sources/'+'b'*64
        original=client.put_object
        calls=[]
        def lost_ack(**kwargs):
            calls.append(kwargs)
            original(**kwargs)
            raise TimeoutError('lost ACK')
        with patch.object(client,'put_object',side_effect=lost_ack):
            version=store.put(key,{'exact':'claim'})
        self.assertEqual(store.get(key),({'exact':'claim'},version))
        self.assertEqual(len(calls),1)
    def test_r2_unknown_write_without_matching_readback_blocks(self):
        client=FakeR2();store=m.R2Store('daily',client=client,bucket='private');key='sources/'+'b'*64
        with patch.object(client,'put_object',side_effect=TimeoutError('unknown')) as put:
            with self.assertRaises(m.LedgerError):store.put(key,{'exact':'claim'})
            self.assertEqual(put.call_count,1)
    def test_actual_installed_sdk_serializes_both_conditions_as_headers(self):
        try:
            import botocore.session
        except ImportError:
            if os.environ.get('GITHUB_ACTIONS') == 'true':
                self.fail('CI must install boto3 and execute SDK header validation')
            self.skipTest('CI installs the verified boto3 floor; local runtime lacks boto3')
        m.validate_s3_model(botocore.session.Session().get_service_model('s3'))
    def test_canary_exercises_actual_conditional_codepaths_and_retains_only_two_synthetic_objects(self):
        import smoke_mineru_ledger as smoke
        client=FakeR2();store=m.R2Store('synthetic-canary',client=client,bucket='private')
        receipt=smoke.canary(store,'123','1')
        self.assertTrue(receipt['conditional_create_412'])
        self.assertTrue(receipt['stale_update_412'])
        self.assertTrue(receipt['valid_cas_readback'])
        self.assertEqual((receipt['objects_retained'],receipt['deletes_performed']), (2,0))
        self.assertTrue(all(key.startswith('_workflow-smoke/mineru-cas/v1/123/1/') for key in client.objects))
        marker,_=store.get(smoke.MARKER_KEY)
        self.assertTrue(marker['complete'])
        self.assertEqual(marker['cleanup_mode'],'read_only_retained_for_review')
    def test_canary_rejects_wrong_precondition_status_or_successful_overwrite(self):
        import smoke_mineru_ledger as smoke
        client=unittest.mock.Mock()
        with self.assertRaises(RuntimeError):smoke.expected_precondition_failure(client,'private','key',{},IfNoneMatch='*')
        error=RuntimeError('secret endpoint');error.response={'ResponseMetadata':{'HTTPStatusCode':500}}
        client.put_object.side_effect=error
        with self.assertRaises(RuntimeError) as captured:smoke.expected_precondition_failure(client,'private','key',{},IfMatch='etag')
        self.assertNotIn('secret',str(captured.exception))
    def test_canary_identity_never_accepts_arbitrary_prefix_or_source(self):
        import smoke_mineru_ledger as smoke
        with patch.dict(os.environ,{'GITHUB_RUN_ID':'../private-source','GITHUB_RUN_ATTEMPT':'1'},clear=True),self.assertRaises(ValueError):smoke.identity()
    def test_github_actions_cannot_fall_back_to_ephemeral_local_store(self):
        with patch.dict(os.environ,{'GITHUB_ACTIONS':'true'},clear=True):
            with self.assertRaises(m.LedgerError):m.from_environment('/unused',None,'https://mineru.net',OPTIONS,TOKENS)
    def test_source_map_preserves_identity_across_temp_filenames_and_rejects_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);pdf=root/'0003-original.pdf';pdf.write_bytes(b'%PDF-test')
            source_map=root/'map.json';entry={'source':'original.pdf','size':9,'sha256':m.digest(pdf.read_bytes())}
            source_map.write_bytes(m.encoded({'schema':1,'files':{pdf.name:entry}}))
            self.assertEqual(m.input_sources([pdf],root,source_map),[(pdf.resolve(),'original.pdf')])
            for mutation in [('size',8),('source','../escape'),('sha256','bad')]:
                changed=dict(entry);changed[mutation[0]]=mutation[1]
                source_map.write_bytes(m.encoded({'schema':1,'files':{pdf.name:changed}}))
                with self.assertRaises(m.LedgerError):m.input_sources([pdf],root,source_map)
            source_map.write_bytes(m.encoded({'schema':1,'files':{}}))
            with self.assertRaises(m.LedgerError):m.input_sources([pdf],root,source_map)
    def test_partial_pending_cli_cannot_generate_or_publish(self):
        import pdf_to_xhs_batch as cli
        for task,code in [({'pending':1,'failed':0},75),({'pending':0,'failed':1},2)]:
            with tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);(root/'one.pdf').write_bytes(b'%PDF-source')
                fake=unittest.mock.Mock();fake.run.return_value=([],task)
                with patch.object(sys,'argv',['pdf','--input-dir',str(root),'--output-dir',str(root/'out')]),patch.dict(os.environ,{'MINER_U':'test'}),patch.object(cli,'from_environment',return_value=fake),patch.object(cli,'process_pdf') as generate:
                    self.assertEqual(cli.main(),code);generate.assert_not_called()
    def test_wrapper_cannot_green_partial_output_with_continue_enabled(self):
        import run_pdf_to_xhs_in_batches as wrapper
        for code in (75,2):
            with tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);(root/'one.pdf').write_bytes(b'%PDF-source')
                with patch.object(sys,'argv',['wrapper','--input-dir',str(root),'--output-dir',str(root/'out')]),patch.object(wrapper,'run_batch',return_value={'returncode':code}),patch.object(wrapper,'count_generated_report_dirs',return_value=1):
                    self.assertEqual(wrapper.main(),code)
    def test_existing_shard_admission_is_disjoint_for_frozen_input(self):
        import argparse
        import run_pdf_to_xhs_in_batches as wrapper
        inputs=[Path(f'{i:03}.pdf') for i in range(65)]
        seen=[]
        for index in range(13):
            args=argparse.Namespace(max_total_reports=65,shard_index=index,shard_count=13,max_reports_per_shard=5)
            shard=wrapper.apply_shard_filter(inputs,args)
            self.assertEqual(len(shard),5)
            seen.extend(shard)
        self.assertEqual(seen,inputs)
        self.assertEqual(len(set(seen)),65)
    def test_real_wrapper_maps_changed_indices_to_same_original_source(self):
        import pdf_to_xhs_batch as cli
        import run_pdf_to_xhs_in_batches as wrapper
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary).resolve();pdf=root/'original.pdf';pdf.write_bytes(b'%PDF-source')
            args=cli.build_arg_parser().parse_args(['--input-dir',str(root),'--output-dir',str(root/'out')])
            identities=[]
            def child(cmd,**kwargs):
                folder=Path(cmd[cmd.index('--input-dir')+1]);source_map=Path(cmd[cmd.index('--mineru-source-map')+1])
                sources=m.input_sources(list(folder.glob('*.pdf')),folder,source_map)
                identities.append([(source,m.digest(path.read_bytes())) for path,source in sources])
                return unittest.mock.Mock(returncode=75)
            with patch.object(wrapper.subprocess,'run',side_effect=child):
                wrapper.run_batch(1,[(1,pdf)],args)
                wrapper.run_batch(3,[(22,pdf)],args)
            self.assertEqual(identities[0],identities[1])
    def test_every_workflow_caller_has_private_durable_scope_and_bounded_serialization(self):
        callers=[]
        for path in (ROOT/'.github/workflows').glob('*.yml'):
            text=path.read_text()
            if 'python scripts/run_pdf_to_xhs_in_batches.py' in text:
                callers.append(path.name)
                self.assertIn('MINERU_LEDGER_BACKEND: r2',text)
                self.assertIn('MINERU_CHECKPOINT_SCOPE:',text)
                self.assertIn('R2_SECRET_ACCESS_KEY:',text)
                self.assertIn('boto3',text)
                self.assertIn('concurrency:',text)
                if path.name != 'daily-bilingual-podcast-videos.yml':
                    self.assertIn('cancel-in-progress: false',text)
        self.assertEqual(len(callers),5)


if __name__=='__main__':unittest.main()
