"""Exact private checkpoint inspection, no provider/storage mutations or contents."""
from contextlib import ExitStack,redirect_stdout
import copy
import io
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import inspect_recovered_article_generation as inspector
import ocr_page_sources as pages
import recovered_article_delivery as delivery
import recover_report_articles as articles
import test_ocr_page_sources as page_fixture
import test_recover_report_articles as article_fixture
from market_views_source_readiness import SOURCE_KIND_GATES


def evidence():
    original={'id':int(inspector.SOURCE_RUN_ID),'path':'.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml',
        'head_branch':'main','head_sha':'a'*40,'status':'completed','event':'schedule',
        'repository':{'full_name':'owner/repo'},'head_repository':{'full_name':'owner/repo'}}
    handoff={**original,'id':int(inspector.HANDOFF_RUN_ID),'head_sha':'b'*40,'event':'workflow_dispatch',
        'path':'.github/workflows/recover-ocr-cache-sources.yml','conclusion':'failure'}
    name,gates=SOURCE_KIND_GATES[(handoff['path'],'ocr-pages')]
    def step(number,name,outcome):
        return {'number':number,'name':name,'status':'completed','conclusion':outcome}
    jobs={'total_count':2,'jobs':[
        {'id':inspector.SOURCE_JOB_ID,'run_id':handoff['id'],'head_sha':handoff['head_sha'],'name':name,'status':'completed','conclusion':'success',
         'steps':[step(i,name,'success') for i,name in enumerate(gates,1)]},
        {'id':inspector.GENERATION_JOB_ID,'run_id':handoff['id'],'head_sha':handoff['head_sha'],'name':'deliver / generate',
         'status':'completed','conclusion':'failure','steps':[
             step(4,'Authenticate original upload and restore exact recovery sources','success'),
             step(5,'Generate only missing bound report articles','failure'),
             step(6,'Save generation progress even after interruption','success')]}]}
    return original,handoff,jobs


class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.f=page_fixture.OCRPagesTests();self.f.setUp();self.addCleanup(self.f.doCleanups)
        self.f.seed(44)
        self.original,self.handoff,self.jobs=evidence()
        self.f.producer=self.original
        self.f.env.update(GITHUB_RUN_ID=inspector.HANDOFF_RUN_ID)
        self.f.request['source_run_id']=inspector.SOURCE_RUN_ID
        self.addCleanup(patch.stopall)
        patch.object(inspector,'MANIFEST_SHA256',self.f.request['manifest_sha256']).start()
        self.f.recover()
        self.workspace=self.f.root/'generation';self.workspace.mkdir()
        config={'SOURCE_RUN_ID':inspector.SOURCE_RUN_ID,'SOURCE_HANDOFF_RUN_ID':inspector.HANDOFF_RUN_ID,
                'SOURCE_KIND':'ocr-pages','DATE_FOLDER':inspector.DATE_FOLDER,'EXPECTED_ARTICLES':44}
        self.context=delivery.validate_source(self.f.workspace/'source',config,'a'*40,'b'*40)
        checkpoint=self.workspace/'checkpoint';(checkpoint/'articles').mkdir(parents=True)
        for path in (self.workspace/'context.json',checkpoint/'context.json'):
            path.write_bytes(delivery.encode(self.context))
        self.harness=article_fixture.ArticleRecoveryTests();self.harness.setUp();self.addCleanup(self.harness.doCleanups)
        with self.harness.paid(fail_at=3),redirect_stdout(io.StringIO()),self.assertRaises(articles.ArticleRecoveryError):
            articles.recover_articles(self.f.workspace/'source','ocr-pages',checkpoint/'articles',44,'261007',self.harness.args,
                source_run_id=inspector.SOURCE_RUN_ID,source_execution_sha='a'*40,
                source_handoff_run_id=inspector.HANDOFF_RUN_ID,source_handoff_execution_sha='b'*40)
        self.log='''RECOVERED_ARTICLE ordinal=1 reused=false
RECOVERED_ARTICLE ordinal=2 reused=false
Traceback (most recent call last):
  File "/PRIVATE/scripts/pdf_to_xhs_batch.py", line 804, in call_deepseek
requests.exceptions.ReadTimeout: PRIVATE url=https://secret.invalid/?key=SECRET body=PRIVATE_TEXT
RuntimeError: DeepSeek generation failed for WeChat article: PRIVATE request
ArticleRecoveryError: article_generation_failed
Report article recovery stopped: article_generation_failed source_ordinal=3
'''
        (self.workspace/'private-generation.log').write_text(self.log)
        patch.object(inspector,'KEY',delivery.context_prefix(self.context)+'/generation.tar.gz').start()
        with redirect_stdout(io.StringIO()):delivery.save_generation(self.workspace,self.f.client,'private')
        self.f.client.uploads.clear()
        self.before=copy.deepcopy(self.f.client.objects)

    def inspect(self):
        destination=self.f.root/'inspect';destination.mkdir(exist_ok=True)
        with self.f.forbidden():
            return inspector.inspect(self.f.client,'private',self.original,self.handoff,self.jobs,'owner/repo',destination)

    def test_real_44_source_checkpoint_two_bound_articles_private_typed_timeout_no_writes(self):
        result=self.inspect()
        self.assertEqual(result['completed_article_count'],2)
        self.assertEqual((result['terminal_category'],result['failed_source_ordinal'],result['phase']),
                         ('article_generation_failed',3,'body_generation'))
        self.assertEqual(result['typed_causes'],['model_timeout'])
        self.assertEqual(result['exception_types'],['ArticleRecoveryError','ReadTimeout','RuntimeError'])
        self.assertFalse(result['provider_outcome_resolved'])
        self.assertEqual(result['inspection_provider_posts'],0)
        self.assertEqual(self.f.client.objects,self.before);self.assertFalse(self.f.client.uploads)
        for forbidden in ('PRIVATE','SECRET','secret.invalid','Revenue','研究','report-000','/scripts/'):
            self.assertNotIn(forbidden,json.dumps(result,ensure_ascii=False))

    def test_wrong_original_handoff_generation_job_or_save_gate_blocks_before_r2(self):
        mutations=(lambda o,h,j:o.update(id=123),lambda o,h,j:h.update(id=999),
            lambda o,h,j:j['jobs'][0].update(id=99),
            lambda o,h,j:j['jobs'][1].update(head_sha='c'*40),
            lambda o,h,j:j['jobs'][1]['steps'][-1].update(conclusion='failure'),
            lambda o,h,j:j['jobs'][0]['steps'][0].update(conclusion='skipped'))
        for mutation in mutations:
            o,h,j=copy.deepcopy((self.original,self.handoff,self.jobs));mutation(o,h,j)
            with patch.object(self.f.client,'head_object') as read,self.assertRaises(ValueError):
                inspector.inspect(self.f.client,'private',o,h,j,'owner/repo',self.f.root/'blocked')
            read.assert_not_called()

    def test_archive_hash_change_stops_without_mutation(self):
        key=inspector.KEY;data,metadata=self.f.client.objects[key]
        self.f.client.objects[key]=(data+b'changed',metadata)
        with self.assertRaises(ValueError):self.inspect()
        self.assertFalse(self.f.client.uploads)

    def test_context_swap_is_rejected(self):
        path=self.workspace/'checkpoint/context.json';value=json.loads(path.read_bytes())
        for field,value_new in (('source_run_id','123'),('source_handoff_run_id','999'),('handoff_execution_sha','c'*40),
                                ('manifest_sha256','d'*64),('expected_articles',43),('source_kind','ocr-synthesis')):
            changed={**value,field:value_new};path.write_bytes(delivery.encode(changed))
            with self.assertRaisesRegex(ValueError,'context_mismatch'):
                inspector.inspect_checkpoint(self.workspace/'checkpoint','a'*40,'b'*40)
        path.write_bytes(delivery.encode(value))

    def test_unbound_status_file_does_not_count_as_completed_article(self):
        root=self.workspace/'checkpoint';metadata=json.loads((root/'articles/source_provenance.json').read_bytes())
        path=root/'articles'/metadata['sources'][1]['directory']/'status.json';value=json.loads(path.read_bytes())
        value.pop('wechat_editorial_binding');path.write_text(json.dumps(value))
        self.assertEqual(inspector.inspect_checkpoint(root,'a'*40,'b'*40)['completed_article_count'],1)

    def test_missing_log_and_oversized_log_are_failures_not_empty_success(self):
        path=self.workspace/'checkpoint/private-diagnostics/private-generation.log'
        path.unlink()
        with self.assertRaisesRegex(ValueError,'invalid_private_file'):
            inspector.inspect_checkpoint(self.workspace/'checkpoint','a'*40,'b'*40)
        path.write_bytes(b'x'*(inspector.MAX_LOG_BYTES+1))
        with self.assertRaisesRegex(ValueError,'invalid_private_file'):
            inspector.inspect_checkpoint(self.workspace/'checkpoint','a'*40,'b'*40)

    def test_provenance_receipt_and_bound_source_changes_are_rejected(self):
        root=self.workspace/'checkpoint';path=root/'articles/source_provenance.json';raw=path.read_bytes()
        value=json.loads(raw);value['source_receipt_json']+='PRIVATE'
        path.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError,'provenance_mismatch'):
            inspector.inspect_checkpoint(root,'a'*40,'b'*40)
        path.write_bytes(raw);value=json.loads(raw)
        value['sources'][0]['source_markdown_sha256']='0'*64;path.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError,'binding_mismatch'):
            inspector.inspect_checkpoint(root,'a'*40,'b'*40)

    def test_receipt_policy_file_inventory_and_source_identity_are_verified(self):
        root=self.workspace/'checkpoint';path=root/'articles/source_provenance.json'
        baseline=path.read_bytes();context_path=root/'context.json';context_raw=context_path.read_bytes()
        mutations=(lambda r:r.update(policy='synthesis-only'), lambda r:r.update(complete=False),
                   lambda r:r.update(report_count=43), lambda r:r['files'].__setitem__(0,r['files'][1]),
                   lambda r:r['files'][0].update(bytes=True), lambda r:r['reports'][0].update(id='R044'),
                   lambda r:r['reports'][0].update(page_count=True),
                   lambda r:r.update(source_inventory_sha256='0'*64),
                   lambda r:r['extraction'].update(ocr_all_pages=False))
        for mutation in mutations:
            metadata=json.loads(baseline);receipt=json.loads(metadata['source_receipt_json']);mutation(receipt)
            metadata['source_receipt_json']=pages.encode(receipt).decode()
            digest=pages.digest(metadata['source_receipt_json'].encode())
            metadata['source_receipt_sha256']=digest
            for source in metadata['sources']:source['provenance']['source_receipt_sha256']=digest
            context={**json.loads(context_raw),'source_receipt_sha256':digest}
            path.write_bytes(pages.encode(metadata));context_path.write_bytes(pages.encode(context))
            with self.assertRaises(ValueError):inspector.inspect_checkpoint(root,'a'*40,'b'*40)
        path.write_bytes(baseline);context_path.write_bytes(context_raw)
        metadata=json.loads(baseline);metadata['sources'][0]['provenance']['source_report_id']='R002'
        path.write_bytes(pages.encode(metadata))
        with self.assertRaisesRegex(ValueError,'source_inventory_mismatch'):
            inspector.inspect_checkpoint(root,'a'*40,'b'*40)

    def test_completed_article_original_pages_and_policy_are_required(self):
        root=self.workspace/'checkpoint';metadata=json.loads((root/'articles/source_provenance.json').read_bytes())
        directory=root/'articles'/metadata['sources'][0]['directory']
        page_path=directory/'source_ocr_pages.json';raw=page_path.read_bytes()
        page_path.write_bytes(raw+b' ')
        status_path=directory/'status.json';old_status=status_path.read_bytes();status=json.loads(old_status)
        status['wechat_source_provenance']['source_pages_sha256']=pages.digest(page_path.read_bytes())
        from wechat_editorial_binding import bind_generated_article
        self.assertTrue(bind_generated_article(directory,status))
        status_path.write_bytes(pages.encode(status))
        with self.assertRaisesRegex(ValueError,'article_page_binding_mismatch'):
            inspector.inspect_checkpoint(root,'a'*40,'b'*40)
        page_path.write_bytes(raw);status=json.loads(old_status)
        status['article_recovery']['policy']='wrong'
        status_path.write_bytes(pages.encode(status))
        with self.assertRaisesRegex(ValueError,'article_policy_mismatch'):
            inspector.inspect_checkpoint(root,'a'*40,'b'*40)

    def test_pregeneration_failure_without_metadata_is_inspectable_and_pending_stays_unknown(self):
        import shutil
        root=self.workspace/'checkpoint';shutil.rmtree(root/'articles');(root/'articles').mkdir()
        (root/'articles/unresolved.pending.json').write_text('PRIVATE unknown outcome')
        (root/'private-diagnostics/private-generation.log').write_text(
            'FileNotFoundError: PRIVATE prompt file missing\nReport article recovery stopped: article_generation_failed\n')
        result=inspector.inspect_checkpoint(root,'a'*40,'b'*40)
        self.assertFalse(result['source_provenance_present']);self.assertEqual(result['completed_article_count'],0)
        self.assertEqual(result['pending_marker_count'],1);self.assertFalse(result['provider_outcome_resolved'])
        self.assertEqual((root/'articles/unresolved.pending.json').read_text(),'PRIVATE unknown outcome')

    def test_archive_traversal_symlink_expansion_and_size_limits_are_read_only(self):
        import tarfile
        from inspect_market_views_r2_cache import MAX_BYTES
        for kind in ('traversal','symlink','expanded'):
            blob=io.BytesIO()
            with tarfile.open(fileobj=blob,mode='w:gz') as archive:
                entry=tarfile.TarInfo('../PRIVATE' if kind=='traversal' else 'PRIVATE')
                if kind=='symlink':entry.type=tarfile.SYMTYPE;entry.linkname='/PRIVATE'
                entry.size=4096 if kind=='expanded' else 0
                archive.addfile(entry,io.BytesIO(b'\0'*entry.size) if entry.size else None)
            raw=blob.getvalue();self.f.client.objects[inspector.KEY]=(raw,{'sha256':pages.digest(raw)})
            with patch('inspect_market_views_r2_cache.MAX_BYTES',1024 if kind=='expanded' else MAX_BYTES):
                expected={'traversal':'archive_path','symlink':'archive_member_limit','expanded':'archive_expansion_limit'}[kind]
                with self.assertRaisesRegex(ValueError,expected):self.inspect()
            self.assertFalse(self.f.client.uploads)
        with patch.object(self.f.client,'head_object',return_value={'ContentLength':MAX_BYTES+1,'Metadata':{'sha256':'a'*64}}), \
                patch.object(self.f.client,'get_object') as get:
            with self.assertRaises(ValueError):self.inspect()
            get.assert_not_called()


class DiagnosticTests(unittest.TestCase):
    def test_title_http_failure_and_safe_status_have_specific_causes_without_text(self):
        status={'wechat_title_decision':{'needs_model_repair':True,'repair_attempted':True,
            'repair_error':'DeepSeek generate WeChat title repair: PRIVATE TITLE: HTTP 429, response=SECRET',
            'selected_quality_issues':['PRIVATE issue']}}
        result=inspector.diagnostic('Report article recovery stopped: generated_article_unbound source_ordinal=3\n',status)
        self.assertEqual(result['phase'],'title_generation')
        self.assertEqual(result['http_statuses'],[429])
        self.assertEqual(result['typed_causes'],['editorial_binding_missing','model_http_429','title_quality_rejected','title_repair_failed'])
        self.assertNotIn('PRIVATE',json.dumps(result));self.assertNotIn('SECRET',json.dumps(result))

    def test_prior_report_nonfatal_errors_are_not_current_failure_causes(self):
        log='RuntimeError: HTTP 401 PRIVATE\nRECOVERED_ARTICLE ordinal=1 reused=false\nRuntimeError: WeChat article failed deterministic editorial guard: PRIVATE\nReport article recovery stopped: article_generation_failed source_ordinal=2\n'
        result=inspector.diagnostic(log,{})
        self.assertEqual(result['typed_causes'],['editorial_guard_failed']);self.assertEqual(result['http_statuses'],[])
        self.assertEqual(result['phase'],'editorial_guard')

    def test_unknown_input_cannot_escape_allowlists_or_claim_provider_outcome(self):
        result=inspector.diagnostic('PRIVATE http://secret.example\nOtherSecretException: PRIVATE\nReport article recovery stopped: private_category source_ordinal=9999\n',{})
        self.assertEqual((result['terminal_category'],result['phase'],result['typed_causes']),('unknown','unknown',['unknown']))
        self.assertIsNone(result['failed_source_ordinal']);self.assertEqual(result['exception_types'],[])
        self.assertNotIn('secret',json.dumps(result))

    def test_fixed_body_auth_json_and_missing_file_causes(self):
        for marker,cause in [('Missing DEEPSEEK_API_KEY for WeChat article','missing_model_credential'),
                             ('Unexpected DeepSeek response: PRIVATE','model_response_invalid'),
                             ('DeepSeek generate WeChat article: HTTP 403, response=PRIVATE','model_http_403'),
                             ('FileNotFoundError: PRIVATE','generation_file_missing')]:
            result=inspector.diagnostic(marker+'\nReport article recovery stopped: article_generation_failed source_ordinal=1\n',{})
            self.assertIn(cause,result['typed_causes'])
            self.assertNotIn('PRIVATE',json.dumps(result))

    def test_main_failure_redacts_raw_exception(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temporary:
            out=Path(temporary)/'result.json'
            for error in (RuntimeError('SECRET body url'),inspector.InspectionError('SECRET body url')):
                with patch.object(inspector,'runtime_identity',side_effect=error),redirect_stdout(io.StringIO()):
                    self.assertEqual(inspector.main(['--output',str(out)]),1)
                value=json.loads(out.read_text());self.assertEqual(value['category'],'inspection_verification_failed')
                self.assertNotIn('SECRET',out.read_text())

    def test_workflow_has_fixed_scope_read_permissions_no_model_or_mutating_operations(self):
        import yaml
        path=Path(__file__).resolve().parents[1]/inspector.WORKFLOW
        value=yaml.safe_load(path.read_text());on=value.get('on',value.get(True))
        self.assertIsNone(on['workflow_dispatch'])
        self.assertEqual(value['permissions'],{'contents':'read','actions':'read'})
        text=path.read_text()
        for forbidden in ('DEEPSEEK','MINER_U','prepare --workspace','save-generation','upload-wechat','delete-prefix'):
            self.assertNotIn(forbidden,text)
        output=value['jobs']['inspect']['steps'][-1]['with']['path']
        self.assertEqual(output,'${{ runner.temp }}/recovered-article-generation-inspection.json')
        env={'GITHUB_ACTIONS':'true','GITHUB_REF':'refs/heads/main','GITHUB_EVENT_NAME':'workflow_dispatch',
             'GITHUB_REPOSITORY':'owner/repo','GITHUB_WORKFLOW_REF':f'owner/repo/{inspector.WORKFLOW}@refs/heads/main'}
        self.assertEqual(inspector.runtime_identity(env),'owner/repo')
        with self.assertRaises(ValueError):inspector.runtime_identity({**env,'GITHUB_EVENT_NAME':'pull_request'})


if __name__=='__main__':unittest.main()
