"""Retained title-only failure and durable article resumption, all providers synthetic."""
from contextlib import ExitStack,redirect_stdout
import copy
import io
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch

import article_generation_progress as progress
import legacy_article_title_resume as legacy
import inspect_recovered_article_generation as inspector
import pdf_to_xhs_batch as producer
import recover_report_articles as articles
import recovered_article_delivery as delivery
import test_ocr_page_sources as pages_fixture
import test_recover_report_articles as article_fixture


def valid_decision():
    return {'needs_model_repair':False,'selected_quality_issues':[],'raw_candidates':[article_fixture.TITLE],
            'selection_reason':'faithful_filename_anchor'}


def emergency_decision():
    return {'needs_model_repair':True,'selected_quality_issues':[], 'repair_attempted':True,
            'selection_reason':'evidence_or_emergency_fallback','raw_candidates':[],
            'rejected_candidates':[], 'repair_candidates':[]}


class ResumeTests(unittest.TestCase):
    def fixture(self,count=3):
        f=pages_fixture.OCRPagesTests();f.setUp();self.addCleanup(f.doCleanups)
        f.seed(count);f.producer['id']=int(inspector.SOURCE_RUN_ID)
        f.request['source_run_id']=inspector.SOURCE_RUN_ID;f.env['GITHUB_RUN_ID']=inspector.HANDOFF_RUN_ID
        f.recover()
        h=article_fixture.ArticleRecoveryTests();h.setUp();self.addCleanup(h.doCleanups)
        checkpoint=f.root/'delivery/checkpoint';output=checkpoint/'articles';output.mkdir(parents=True)
        context=delivery.validate_source(f.workspace/'source',{'SOURCE_RUN_ID':inspector.SOURCE_RUN_ID,
            'SOURCE_HANDOFF_RUN_ID':inspector.HANDOFF_RUN_ID,'SOURCE_KIND':'ocr-pages','DATE_FOLDER':'261007',
            'EXPECTED_ARTICLES':count},'a'*40,'b'*40)
        (checkpoint/'context.json').write_bytes(delivery.encode(context))
        self.f,self.h,self.output,self.context,self.count=f,h,output,context,count
        self.calls=[];self.persisted=[]
        return f,h

    def recover(self,staged=True):
        return articles.recover_articles(self.f.workspace/'source','ocr-pages',self.output,self.count,'261007',self.h.args,
            source_run_id=inspector.SOURCE_RUN_ID,source_execution_sha='a'*40,
            source_handoff_run_id=inspector.HANDOFF_RUN_ID,source_handoff_execution_sha='b'*40,
            checkpoint_progress=staged, persist_progress=lambda:self.persisted.append(True),delivery_context=self.context)

    def model(self,prompt,args,label,**kwargs):
        self.calls.append(label)
        return article_fixture.BODY if label=='WeChat article' else json.dumps({'titles':[article_fixture.TITLE]})

    def private(self):
        stack=ExitStack()
        stack.enter_context(patch('requests.Session.request',side_effect=AssertionError('external requests forbidden')))
        stack.enter_context(redirect_stdout(io.StringIO()))
        return stack

    def test_real44_27_accepted_28_legacy_body_title_only_remaining16_and_zero_call_replay(self):
        f,h=self.fixture(44)
        def initial_title(*args,**kwargs):
            return article_fixture.TITLE, emergency_decision() if len(h.calls)==28 else valid_decision()
        with h.paid(),patch.object(producer,'wechat_title_from_filename',side_effect=initial_title),self.private():
            with self.assertRaisesRegex(ValueError,'generated_article_unbound'):self.recover(False)
        metadata=articles.read_json(self.output/'source_provenance.json')
        accepted={s['directory']:articles.inventory(self.output/s['directory']) for s in metadata['sources'][:27]}
        failed=self.output/metadata['sources'][27]['directory']
        status=articles.read_json(failed/'status.json');status['article_recovery']['generation_contract_sha256']=legacy.OLD_CONTRACT
        articles.write_json(failed/'status.json',status)
        original_body=(failed/'wechat_article.md').read_bytes()
        diagnostics=self.output.parent/'private-diagnostics';diagnostics.mkdir()
        (diagnostics/'private-generation.log').write_text('Report article recovery stopped: generated_article_unbound source_ordinal=28\n')
        context_sha=legacy.digest(legacy.encode(self.context))
        with patch.object(legacy,'CONTEXT_SHA',context_sha),patch.object(inspector,'MANIFEST_SHA256',f.request['manifest_sha256']), \
                patch.object(legacy,'BODY_SHA',legacy.digest(original_body)),patch.object(legacy,'BODY_BYTES',len(original_body)), \
                patch.object(legacy,'PROMPT_SHA',legacy.digest((failed/'prompt_for_wechat.md').read_bytes())), \
                patch.object(legacy,'SOURCE_SHA',legacy.digest((failed/'source_ocr.md').read_bytes())):
            for head in ({'ContentLength':legacy.ARCHIVE_BYTES+1,'Metadata':{'sha256':legacy.ARCHIVE_SHA}},
                         {'ContentLength':legacy.ARCHIVE_BYTES,'Metadata':{'sha256':'0'*64}}):
                with self.assertRaisesRegex(ValueError,'legacy_title_archive_mismatch'):
                    legacy.authorize(self.output.parent,self.context,head)
            saved_status=(failed/'status.json').read_bytes()
            status['article_recovery']['generation_contract_sha256']='0'*64
            articles.write_json(failed/'status.json',status)
            with self.assertRaisesRegex(ValueError,'legacy_title_state_mismatch'):
                legacy.authorize(self.output.parent,self.context,{'ContentLength':legacy.ARCHIVE_BYTES,'Metadata':{'sha256':legacy.ARCHIVE_SHA}})
            (failed/'status.json').write_bytes(saved_status)
            legacy.authorize(self.output.parent,self.context,{'ContentLength':legacy.ARCHIVE_BYTES,'Metadata':{'sha256':legacy.ARCHIVE_SHA}})
            titles=[]
            def repaired(*args,**kwargs):
                titles.append(kwargs.get('previous_decision'))
                return article_fixture.TITLE,valid_decision()
            with patch.object(producer,'call_deepseek',side_effect=self.model),patch.object(producer,'wechat_title_from_filename',side_effect=repaired),self.private():
                receipt=self.recover()
            self.assertEqual(len(self.calls),16);self.assertTrue(all(x=='WeChat article' for x in self.calls))
            self.assertEqual(len(titles),17);self.assertEqual(titles[0]['selection_reason'],'evidence_or_emergency_fallback')
            self.assertEqual((failed/'wechat_article.md').read_bytes(),original_body)
            self.assertEqual(receipt['report_count'],44)
            for directory,inventory in accepted.items():self.assertEqual(articles.inventory(self.output/directory),inventory)
            with patch.object(producer,'call_deepseek',side_effect=AssertionError('no paid replay')),patch.object(producer,'wechat_title_from_filename',side_effect=AssertionError('no title replay')),self.private():
                self.assertEqual(self.recover(),receipt)
        self.assertTrue(self.persisted)
        self.assertTrue((self.output.parent/'generation-progress').is_dir())
        self.assertFalse(list(self.output.rglob('article_generation_progress.json')))
        self.assertFalse(any('article_generation_response' in row['path'] or 'legacy_title_resume' in row['path'] for row in receipt['files']))

    def test_unknown_title_request_retains_body_and_finishes_other_reports_without_delivery(self):
        self.fixture()
        calls=[]
        def request(prompt,args,label,**kwargs):
            calls.append(label)
            if label.startswith('WeChat filename title:') and len([v for v in calls if v=='WeChat article'])==1:
                raise TimeoutError('PRIVATE unknown title response')
            return article_fixture.BODY if label=='WeChat article' else json.dumps({'titles':[article_fixture.TITLE]})
        with patch.object(producer,'call_deepseek',side_effect=request),patch.object(producer,'decide_filename_anchored_title',return_value=(article_fixture.TITLE,valid_decision())),self.private():
            with self.assertRaisesRegex(ValueError,'article_progress_request_pending'):self.recover()
        self.assertEqual(calls.count('WeChat article'),3)
        self.assertFalse((self.output/articles.RECEIPT).exists())
        metadata=articles.read_json(self.output/'source_provenance.json')
        self.assertEqual(sum(articles.usable_article(self.output/s['directory']) is not None for s in metadata['sources']),2)
        with patch.object(producer,'call_deepseek',side_effect=AssertionError('pending must not replay')),patch.object(producer,'decide_filename_anchored_title',return_value=(article_fixture.TITLE,valid_decision())),self.private():
            with self.assertRaisesRegex(ValueError,'article_progress_pending'):self.recover()
        self.assertEqual(calls.count('WeChat article'),3)

    def test_semantic_emergency_with_empty_issues_remains_unbound_and_title_budget_is_finite(self):
        self.fixture(1)
        with patch.object(producer,'call_deepseek',side_effect=self.model),patch.object(producer,'decide_filename_anchored_title',side_effect=lambda *a,**k:(article_fixture.TITLE,emergency_decision())),self.private():
            with self.assertRaisesRegex(ValueError,'generated_article_unbound'):self.recover()
            self.assertEqual(self.calls.count('WeChat article'),1);self.assertEqual(len(self.calls),5)
            with self.assertRaisesRegex(ValueError,'generated_article_unbound'):self.recover()
            self.assertEqual(len(self.calls),5)
        self.assertFalse((self.output/articles.RECEIPT).exists())

    def test_unbound_body_without_pinned_legacy_proof_is_not_regenerated_or_adopted(self):
        self.fixture(1)
        with self.h.paid(),patch.object(producer,'wechat_title_from_filename',return_value=(article_fixture.TITLE,emergency_decision())),self.private():
            with self.assertRaises(ValueError):self.recover(False)
        with patch.object(producer,'call_deepseek',side_effect=AssertionError('no unproven body replay')),self.private():
            with self.assertRaisesRegex(ValueError,'unresolved_legacy_generation'):self.recover()

    def test_changed_saved_body_or_source_identity_rejected_before_request(self):
        self.fixture(1)
        with patch.object(producer,'call_deepseek',side_effect=self.model),patch.object(producer,'wechat_title_from_filename',return_value=(article_fixture.TITLE,emergency_decision())),self.private():
            with self.assertRaises(ValueError):self.recover()
        result=next((self.output.parent/'generation-progress').rglob('article_generation_response_*.txt'))
        result.write_text('changed')
        with patch.object(producer,'call_deepseek',side_effect=AssertionError('no corrupted body replay')),self.private():
            with self.assertRaisesRegex(ValueError,'article_progress_response_changed'):self.recover()

    def test_cli_wires_prepared_private_workspace_to_durable_progress(self):
        import sys
        self.fixture(1)
        workspace=self.output.parent.parent
        (workspace/'context.json').write_bytes(delivery.encode(self.context))
        import shutil
        shutil.copytree(self.f.workspace/'source',workspace/'source')
        argv=['recover_report_articles.py','--source-dir',str(workspace/'source'),'--source-kind','ocr-pages',
            '--output-dir',str(self.output),'--expected-reports','1','--date-folder','261007',
            '--source-run-id',inspector.SOURCE_RUN_ID,'--source-execution-sha','a'*40,
            '--source-handoff-run-id',inspector.HANDOFF_RUN_ID,'--source-handoff-execution-sha','b'*40,
            '--checkpoint-workspace',str(workspace)]
        with patch.object(sys,'argv',argv),patch('private_workflow_handoff.build_r2_client',return_value=self.f.client), \
                patch('private_workflow_handoff.r2_bucket',return_value='private'), \
                patch.object(producer,'call_deepseek',side_effect=self.model), \
                patch.object(producer,'wechat_title_from_filename',return_value=(article_fixture.TITLE,valid_decision())),self.private():
            self.assertEqual(articles.main(),0)
        self.assertEqual(self.calls,['WeChat article'])
        self.assertEqual(len(self.f.client.uploads),2)
        import tarfile
        data,_meta=self.f.client.objects[delivery.context_prefix(self.context)+'/generation.tar.gz']
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as archive:
            self.assertTrue(any(name.startswith('generation-progress/') for name in archive.getnames()))
        # The complete-generation upload carries only articles, never stage data.
        with self.private():delivery.save_generation(workspace,self.f.client,'private',complete=True)
        data,_meta=self.f.client.objects[delivery.context_prefix(self.context)+'/articles/shard_0.tar.gz']
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as archive:
            self.assertFalse(any('generation-progress' in name or 'article_generation_response_' in name or legacy.PROOF in name for name in archive.getnames()))

    def test_checkpoint_mode_requires_durable_callback_before_provider(self):
        self.fixture(1)
        with patch.object(producer,'call_deepseek',side_effect=AssertionError('no nondurable call')):
            with self.assertRaisesRegex(ValueError,'progress_durable_callback_required'):
                articles.recover_articles(self.f.workspace/'source','ocr-pages',self.output,1,'261007',self.h.args,
                    checkpoint_progress=True)

    def test_private_upload_verifies_checksum_before_continuing(self):
        from private_workflow_handoff import upload_directory
        self.fixture(1)
        (self.output/'synthetic.txt').write_text('private checkpoint')
        original=self.f.client.head_object
        def stale(**kwargs):
            result=original(**kwargs);result['Metadata']={'sha256':'0'*64};return result
        with patch.object(self.f.client,'head_object',side_effect=stale),self.private():
            with self.assertRaisesRegex(RuntimeError,'checksum metadata'):
                upload_directory(self.output,'_private-workflow-handoff/test/generation.tar.gz',client=self.f.client,bucket='private')


class TitleContractTests(unittest.TestCase):
    def test_production_provenance_pins_are_complete_sha256_values(self):
        for name in ('ARCHIVE_SHA','CONTEXT_SHA','OLD_CONTRACT','BODY_SHA','PROMPT_SHA','SOURCE_SHA'):
            with self.subTest(pin=name):self.assertRegex(getattr(legacy,name),r'^[a-f0-9]{64}$')
        self.assertEqual((legacy.ARCHIVE_BYTES,legacy.BODY_BYTES),(2072910,4763))

    def test_legacy_context_pin_matches_exact_delivery_encoding(self):
        context={'schema_version':1,'source_run_id':'123','date_folder':'261007'}
        self.assertEqual(legacy.encode(context),delivery.encode(context))
        with patch.object(legacy,'CONTEXT_SHA',delivery.digest(delivery.encode(context))):
            self.assertTrue(legacy.incident(context))
            self.assertFalse(legacy.incident({**context,'source_run_id':'456'}))

    def test_real_optimizer_requires_new_model_candidate_for_semantic_emergency(self):
        from wechat_title_optimizer import decide_filename_anchored_title
        source='MS-Memory semiconductor supply and demand changes-261007.pdf'
        body='半导体供需出现变化。研究记录了半导体企业产出和交付。'
        title,previous=decide_filename_anchored_title([],source,'摩根士丹利',evidence_text=body)
        self.assertEqual(previous['selection_reason'],'evidence_or_emergency_fallback')
        self.assertTrue(previous['needs_model_repair']);self.assertEqual(previous['selected_quality_issues'],[])
        args=producer.build_arg_parser().parse_args([]);args.checkpoint_single_request=True
        no_candidates=[]
        def empty(*a,**k):no_candidates.append(a);return '{"titles":[]}'
        _,unready=producer.wechat_title_from_filename(source,body,'摩根士丹利',args,request=empty,previous_decision=previous)
        self.assertTrue(unready['needs_model_repair']);self.assertEqual(len(no_candidates),3)
        returned=iter(['{"titles":[]}',json.dumps({'titles':[title]})]);submissions=[]
        def proposed(*a,**k):submissions.append(a);return next(returned)
        final,ready=producer.wechat_title_from_filename(source,body,'摩根士丹利',args,request=proposed,previous_decision=previous)
        self.assertEqual(final,title);self.assertFalse(ready['needs_model_repair'])
        self.assertEqual(ready['selected_quality_issues'],[]);self.assertEqual(len(submissions),2)
        self.assertIn(title,ready['repair_candidates'])

    def test_real_long_english_company_candidates_get_targeted_repair_and_keep_semantic_gates(self):
        from wechat_title_optimizer import decide_filename_anchored_title
        source='MS-Salesforce Revenue Growth Accelerates-261007.pdf'
        body='赛富时（Salesforce）的营收增长加快。该公司产品交付数量增加。'
        english='摩根士丹利：Salesforce营收增长加快'
        chinese='摩根士丹利：赛富时营收增长加快'
        _,previous=decide_filename_anchored_title([english]*6,source,'摩根士丹利',evidence_text=body)
        self.assertTrue(previous['needs_model_repair'])
        self.assertTrue(any('long_untranslated_english' in row['reasons'] for row in previous['rejected_candidates']))
        args=producer.build_arg_parser().parse_args([]);args.checkpoint_single_request=True
        replies=iter([json.dumps({'titles':[english]*3}),json.dumps({'titles':[chinese]})]);prompts=[]
        def call(prompt,*a,**k):prompts.append(prompt);return next(replies)
        title,decision=producer.wechat_title_from_filename(source,body,'摩根士丹利',args,request=call,previous_decision=previous)
        self.assertEqual(title,chinese);self.assertFalse(decision['needs_model_repair'])
        self.assertEqual(decision['selected_quality_issues'],[]);self.assertEqual(len(prompts),2)
        self.assertTrue(all('不要原样复制完整英文名' in prompt for prompt in prompts))
        self.assertTrue(all('正文证据明确出现的中文名称' in prompt for prompt in prompts))
        self.assertIn(chinese,decision['repair_candidates'])

    def test_prior_selected_emergency_is_never_promoted_as_actual_model_candidate(self):
        args=producer.build_arg_parser().parse_args([]);args.checkpoint_single_request=True
        previous={**emergency_decision(),'selected_title':'FACTUAL EMERGENCY','final_title_after_wording_guard':'FACTUAL EMERGENCY'}
        seen=[]
        def choose(candidates,*a,**k):
            seen.append(list(candidates));return article_fixture.TITLE,emergency_decision()
        requests=[]
        def request(*a,**k):requests.append(a);return '{"titles":[]}'
        with patch.object(producer,'decide_filename_anchored_title',side_effect=choose):
            _,decision=producer.wechat_title_from_filename('BIS-source.pdf',article_fixture.BODY,'国际清算银行',args,request=request,previous_decision=previous)
        self.assertTrue(decision['needs_model_repair']);self.assertEqual(decision['selected_quality_issues'],[])
        self.assertEqual(len(requests),3)
        self.assertTrue(all('FACTUAL EMERGENCY' not in rows for rows in seen))

    def test_checkpoint_call_uses_one_key_one_post_no_hidden_model_fallback(self):
        args=producer.build_arg_parser().parse_args([]);args.checkpoint_single_request=True
        response=type('Response',(),{'status_code':200,'json':lambda self:{'choices':[{'message':{'content':'completed'}}]}})()
        with patch.object(producer,'deepseek_api_keys_from_env',return_value=[('primary','x'),('backup','y')]),patch.object(producer,'request_with_key_fallback',return_value=response) as call:
            self.assertEqual(producer.call_deepseek('prompt',args,'title'),'completed\n')
        self.assertEqual(call.call_args.kwargs['api_keys'],[('primary','x')])
        self.assertEqual(call.call_args.kwargs['max_attempts'],1);self.assertFalse(call.call_args.kwargs['allow_model_fallback'])

    def test_workflow_requires_durable_workspace_and_deliver_only_after_generation_success(self):
        import yaml
        workflow=Path(__file__).resolve().parents[1]/'.github/workflows/recover-report-article-delivery.yml'
        data=yaml.safe_load(workflow.read_text());steps=data['jobs']['generate']['steps']
        generate=next(step for step in steps if step.get('name')=='Generate only missing bound report articles')
        self.assertIn('--checkpoint-workspace "$DELIVERY_WORKSPACE"',generate['run'])
        self.assertIn("needs.generate.result == 'success'",data['jobs']['deliver']['if'])


if __name__=='__main__':unittest.main()
