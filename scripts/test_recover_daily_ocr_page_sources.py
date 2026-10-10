"""Daily fallback control flow and real-PDF page/archive/consumer regressions."""
from contextlib import redirect_stdout
import copy
import io
import itertools
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import ocr_page_sources as pages
import recover_daily_ocr_page_sources as daily
import recover_report_articles as articles
import recovered_article_delivery as delivery
from market_views_source_readiness import SOURCE_KIND_GATES, require_source_readiness
import test_ocr_page_sources as pages_fixture
from test_market_views_workflow_contract import gate, job, UPSTREAM


PRIOR_STEPS = (
    ('Recover existing MinerU tasks for daily Market Views', 'success'),
    ('Save complete recovered MinerU sources to private R2', 'skipped'),
    ('Build complete OCR summaries and charts for Market Views', 'failure'),
    ('Save private OCR synthesis cache even after interruption', 'success'),
    ('Save complete OCR synthesis to private R2', 'skipped'),
    ('Capture Daily OCR page fallback eligibility', 'success'),
)


def source_jobs(run_id=123, sha='a'*40):
    name, names = SOURCE_KIND_GATES[(pages.DAILY_WORKFLOW, 'ocr-pages')]
    def record(number, name, conclusion):
        return {'number':number,'name':name,'status':'completed','conclusion':conclusion}
    return {'total_count':2,'jobs':[
        {'id':11,'run_id':run_id,'head_sha':sha,'name':'recover-market-sources',
         'status':'completed','conclusion':'failure',
         'steps':[record(i,name,conclusion) for i,(name,conclusion) in enumerate(PRIOR_STEPS,1)]},
        {'id':12,'run_id':run_id,'head_sha':sha,'name':name,'status':'completed','conclusion':'success',
         'steps':[record(i,name,'success') for i,name in enumerate(names,1)]},
    ]}


class DailyPagesTests(unittest.TestCase):
    def setUp(self):
        self.f=pages_fixture.OCRPagesTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        self.env={**self.f.env,'GITHUB_RUN_ID':'123','GITHUB_SHA':'a'*40,'GITHUB_EVENT_NAME':'schedule',
            'GITHUB_WORKFLOW_REF':f'owner/repo/{pages.DAILY_WORKFLOW}@refs/heads/main',
            'REPLAY_SOURCE_RUN_ID':'','PRIMARY_READY':'false','MINERU_RECOVERY_FAILED':'true',
            'OCR_ATTEMPTED':'true','ARTICLE_SOURCE_READY':'false','DATE_FOLDER':'261007','EXPECTED_REPORTS':'2'}

    def seed(self,count=2):
        self.f.seed(count);self.env['EXPECTED_REPORTS']=str(count)

    def recover(self):
        with self.f.forbidden():
            return daily.recover(self.f.input,self.f.workspace,self.env,self.f.client,'private')

    def archive(self):
        with self.f.forbidden():
            return daily.archive(self.f.input,self.f.workspace,self.env,self.f.client,'private')

    def validate(self):
        return pages.validate_pages_receipt(self.f.workspace/'source',date_folder='261007',
            expected_reports=int(self.env['EXPECTED_REPORTS']),source_run_id='123',execution_sha='a'*40,
            recovery_run_id='123',recovery_execution_sha='a'*40)

    def test_actual_44_pdfs_pending_summary_complete_pages_no_provider_or_ocr(self):
        self.seed(44);before=copy.deepcopy(self.f.client.objects)
        self.assertEqual(self.recover(),{'reused':False,'reports':44})
        receipt=self.validate();self.archive()
        self.assertEqual((receipt['report_count'],receipt['total_pages']),(44,88))
        self.assertNotIn('cache_recovery',receipt)
        self.assertEqual(receipt['daily_cache_origin']['archive_sha256'],self.f.request['archive_sha256'])
        self.assertEqual(self.f.client.uploads,[f'{pages.DAILY_PREFIX}/123/261007/shard_0.tar.gz'])
        self.assertEqual(self.f.client.objects[self.f.cache_key],before[self.f.cache_key])

    def test_retry_reuses_exact_accepted_handoff_even_mutable_cache_gone(self):
        self.seed();self.recover();self.archive()
        raw=(self.f.workspace/'source'/pages.RECEIPT).read_bytes()
        del self.f.client.objects[self.f.cache_key]
        self.f.workspace=self.f.root/'retry';self.f.workspace.mkdir()
        with patch.object(daily,'build_pages',side_effect=AssertionError('no re-extraction')):
            self.assertTrue(self.recover()['reused'])
        self.archive();self.assertEqual((self.f.workspace/'source'/pages.RECEIPT).read_bytes(),raw)
        self.assertEqual(len(self.f.client.uploads),1)

    def test_receipt_cannot_be_replaced_after_acceptance(self):
        self.seed();self.recover();self.archive()
        receipt=self.f.workspace/'source'/pages.RECEIPT
        receipt.write_bytes(receipt.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError,'existing_receipt_changed'):self.archive()
        self.assertEqual(len(self.f.client.uploads),1)

    def test_daily_origin_and_manual_recovery_are_mutually_exclusive(self):
        self.seed();self.recover();receipt=self.f.workspace/'source'/pages.RECEIPT
        original=receipt.read_bytes();value=json.loads(original)
        for mutate in (
            lambda r:r.update(cache_recovery={}),
            lambda r:r.update(cache_recovery=r.pop('daily_cache_origin')),
            lambda r:r.pop('daily_cache_origin'),
            lambda r:r['daily_cache_origin'].update(source_run_id='999'),
            lambda r:r['daily_cache_origin'].update(source_execution_sha='b'*40),
            lambda r:r['daily_cache_origin'].update(checkpoint_identity='0'*64),
            lambda r:r['daily_cache_origin'].update(provider_posts=1),
            lambda r:r['daily_cache_origin'].update(ocr_calls=True),
        ):
            changed=copy.deepcopy(value);mutate(changed);receipt.write_bytes(pages.encode(changed))
            with self.assertRaises(ValueError):self.validate()
        receipt.write_bytes(original);self.validate()
        with self.assertRaises(ValueError):
            pages.validate_pages_receipt(receipt.parent,date_folder='261007',expected_reports=2,
                source_run_id='123',execution_sha='a'*40,recovery_run_id='999',recovery_execution_sha='b'*40)

    def test_daily_namespace_cannot_receive_manual_envelope_or_wrong_run(self):
        from private_workflow_handoff import upload_directory
        self.seed();self.recover()
        for prefix,run in ((pages.PREFIX,'123'),(pages.DAILY_PREFIX,'999')):
            with self.assertRaisesRegex(ValueError,'archive_namespace_invalid'):
                upload_directory(self.f.workspace/'source',f'{prefix}/{run}/261007/shard_0.tar.gz',
                    client=self.f.client,bucket='private',include_ocr_page_originals=True)
        self.assertFalse(self.f.client.uploads)

    def test_missing_last_page_archive_change_or_pdf_change_fails_before_writing(self):
        for defect in ('page','archive','pdf'):
            with self.subTest(defect=defect):
                # Separate fixtures ensure no state from an earlier rejected batch.
                case=DailyPagesTests();case.setUp();self.addCleanup(case.doCleanups);case.seed()
                if defect=='page':
                    file=sorted((case.f.cache/'pages').glob('*.json'))[-1]
                    value=json.loads(file.read_bytes());value['pages'].pop();file.write_bytes(pages.encode(value))
                    case.f.publish_cache()
                elif defect=='archive':
                    raw,metadata=case.f.client.objects[case.f.cache_key]
                    case.f.client.objects[case.f.cache_key]=(raw+b'changed',metadata)
                else:
                    next(case.f.input.glob('*.pdf')).write_bytes(b'changed')
                with self.assertRaises(Exception):case.recover()
                self.assertFalse((case.f.workspace/'source').exists())
                self.assertFalse(case.f.client.uploads)

    def test_identity_and_actual_attempt_requirements_precede_any_storage_access(self):
        self.seed()
        for key,value in (('REPLAY_SOURCE_RUN_ID','123'),('PRIMARY_READY','true'),('MINERU_RECOVERY_FAILED','false'),
                          ('OCR_ATTEMPTED','false'),('ARTICLE_SOURCE_READY','true'),('GITHUB_REF','refs/heads/dev'),
                          ('GITHUB_EVENT_NAME','pull_request'),('GITHUB_WORKFLOW_REF',self.f.env['GITHUB_WORKFLOW_REF'])):
            with self.subTest(key=key),patch.object(self.f.client,'head_object') as head:
                with self.assertRaises(ValueError):
                    daily.recover(self.f.input,self.f.workspace,{**self.env,key:value},self.f.client,'private')
                head.assert_not_called()

    def test_full_article_consumer_accepts_daily_origin_and_omits_original_pdfs(self):
        from test_recover_report_articles import ArticleRecoveryTests
        self.seed();self.recover()
        harness=ArticleRecoveryTests();harness.setUp();self.addCleanup(harness.doCleanups)
        output=self.f.root/'articles'
        with harness.paid():
            receipt=articles.recover_articles(self.f.workspace/'source','ocr-pages',output,2,'261007',harness.args,
                source_run_id='123',source_execution_sha='a'*40,source_handoff_run_id='123',source_handoff_execution_sha='a'*40)
            articles.validate_articles(output,2,'261007')
        self.assertEqual(len(harness.calls),2);self.assertEqual(receipt['source_kind'],'ocr-pages')
        self.assertFalse(list(output.rglob('*.pdf')))
        for row in receipt['reports']:
            root=output/row['directory'];status=json.loads((root/'status.json').read_bytes())
            self.assertIn('Original page 2',(root/'source_ocr.md').read_text())
            self.assertEqual(status['image_source_kind'],'ocr_pages_text_only')
            self.assertEqual(status['images'],[])

    def test_live_daily_producer_and_queued_translations_admit_exact_source(self):
        from test_recovered_article_delivery import Store,original_fixture
        from private_workflow_handoff import upload_directory
        self.seed();self.recover();store=Store()
        with redirect_stdout(io.StringIO()):
            upload_directory(self.f.workspace/'source',f'{pages.DAILY_PREFIX}/123/261007/shard_0.tar.gz',
                client=store,bucket='private',include_ocr_page_originals=True)
        config=delivery.inputs({'SOURCE_RUN_ID':'123','SOURCE_HANDOFF_RUN_ID':'123','SOURCE_KIND':'ocr-pages',
                                'DATE_FOLDER':'261007','EXPECTED_ARTICLES':'2'})
        original,attempts=original_fixture();original.update(id=123,status='in_progress',conclusion=None)
        for row in attempts[0]['jobs']:row['run_id']=123
        attempts[0]['jobs'][-1].update(status='queued',conclusion=None)
        latest=source_jobs();latest['jobs']+=copy.deepcopy(attempts[0]['jobs']);latest['total_count']=len(latest['jobs'])
        with patch.object(delivery,'api',return_value=original),\
             patch.object(delivery,'jobs',side_effect=lambda repo,run,attempt=None: attempts[attempt-1] if attempt else latest),\
             redirect_stdout(io.StringIO()):
            context=delivery.prepare(self.f.root/'delivery',config,self.env,store,'private')
        self.assertEqual(context['source_execution_sha'],context['handoff_execution_sha'])
        self.assertEqual(context['source_run_id'],context['source_handoff_run_id'])

    def test_readiness_requires_independent_prior_and_new_source_gates(self):
        producer={**self.f.producer,'status':'in_progress','conclusion':None}
        baseline=source_jobs()
        self.assertTrue(require_source_readiness(producer,baseline,source_kind='ocr-pages')['ready'])
        for job_index,step_index,field,bad in (
            (0,None,'conclusion','success'),(0,None,'head_sha','b'*40),(0,None,'status','in_progress'),
            (0,0,'conclusion','skipped'),(0,1,'conclusion','success'),(0,2,'conclusion','skipped'),
            (0,4,'conclusion','success'),(0,5,'conclusion','failure'),
            (1,0,'conclusion','failure'),(1,1,'conclusion','skipped')):
            changed=copy.deepcopy(baseline);row=changed['jobs'][job_index]
            if step_index is not None:row=row['steps'][step_index]
            row[field]=bad
            with self.subTest(job_index=job_index,step_index=step_index,field=field),self.assertRaises(ValueError):
                require_source_readiness(producer,changed,source_kind='ocr-pages')
        baseline['jobs'][0]['steps'][2]['conclusion']='success'
        baseline['jobs'][0]['steps'][4]['conclusion']='failure'
        self.assertTrue(require_source_readiness(producer,baseline,source_kind='ocr-pages')['ready'])

    def test_outcome_permutations_never_fallback_before_real_mineru_failure_and_ocr_attempt(self):
        block=job(UPSTREAM,'recover-ocr-page-sources')
        for mineru,ocr,mineru_saved,ocr_saved in itertools.product(('success','failure','skipped','cancelled'),repeat=4):
            outcomes=daily.recovery_outcomes(mineru,ocr,mineru_saved,ocr_saved)
            expected=mineru=='failure' and ocr in {'success','failure'} and not(ocr==ocr_saved=='success')
            results={'select-macro-reports':'success','source-outcome':'success','recover-market-sources':'failure'}
            with self.subTest(mineru=mineru,ocr=ocr,mineru_saved=mineru_saved,ocr_saved=ocr_saved):
                self.assertEqual(gate(block,results,primary_ready='false',recovery_outputs=outcomes),expected)
        outcomes={'mineru_recovery_failed':'true','ocr_attempted':'true','article_source_ready':'false'}
        for result in ('success','skipped','cancelled'):
            self.assertFalse(gate(block,{**results,'recover-market-sources':result},primary_ready='false',recovery_outputs=outcomes))
        for args in ({'cancelled':True},{'primary_ready':'true'},{'selected':'0'},
                     {'plan':{'replay_source_run_id':'123'}}):
            self.assertFalse(gate(block,results,recovery_outputs=outcomes,**{'primary_ready':'false',**args}))

    def test_source_routing_delivers_articles_translations_but_not_market_pdf_or_charts(self):
        results={'select-macro-reports':'success','source-outcome':'success','recover-market-sources':'failure',
                 'recover-ocr-page-sources':'success','deliver-recovered-report-articles':'success'}
        self.assertTrue(gate(job(UPSTREAM,'deliver-recovered-report-articles'),results,primary_ready='false'))
        self.assertTrue(gate(job(UPSTREAM,'plan-portal-translated-reports'),results,primary_ready='false'))
        self.assertFalse(gate(job(UPSTREAM,'trigger-market-views'),results,primary_ready='false',recovery_kind=''))
        self.assertFalse(gate(job(UPSTREAM,'trigger-chart-search-index'),results,primary_ready='false',recovery_kind=''))
        self.assertFalse(gate(job(UPSTREAM,'cleanup-market-source-recovery'),results,primary_ready='false'))
        for result in ('failure','skipped','cancelled'):
            self.assertFalse(gate(job(UPSTREAM,'deliver-recovered-report-articles'),
                {**results,'recover-ocr-page-sources':result},primary_ready='false'))

    def test_workflow_uses_same_run_artifact_only_no_ocr_or_model_credentials(self):
        import yaml
        workflow=yaml.safe_load(UPSTREAM.read_text());block=workflow['jobs']['recover-ocr-page-sources']
        text=json.dumps(block)
        for forbidden in ('DEEPSEEK_API_KEY','MINER_U','tesseract','--ocr-all-pages'):
            self.assertNotIn(forbidden,text)
        self.assertNotIn('${{ runner.',str(block['env']))
        download=next(step for step in block['steps'] if step.get('uses')=='actions/download-artifact@v4')
        self.assertEqual(download['with']['name'],'selected-macro-pdfs-${{ github.run_id }}')
        self.assertNotIn('run-id',download['with'])
        named={step.get('name'):step for step in block['steps']}
        for name in SOURCE_KIND_GATES[(pages.DAILY_WORKFLOW,'ocr-pages')][1]:
            self.assertIn('recover_daily_ocr_page_sources.py',named[name]['run'])
        recovery=workflow['jobs']['recover-market-sources'];steps={s.get('id'):s for s in recovery['steps']}
        self.assertIn('always()',steps['recovery-status']['if'])
        self.assertEqual(steps['recovery-status']['env']['MINERU_OUTCOME'],'${{ steps.mineru-recover.outcome }}')
        manual=yaml.safe_load((UPSTREAM.parent/'recover-ocr-cache-sources.yml').read_text())
        on=manual.get('on',manual.get(True))
        self.assertEqual(on['workflow_dispatch']['inputs']['source_mode']['default'],'synthesis')


if __name__=='__main__':unittest.main()
