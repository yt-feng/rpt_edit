"""Real-PDF pages-only recovery and article contracts; all services synthetic."""
from contextlib import ExitStack, redirect_stdout
import copy
import io
import json
from pathlib import Path
import tempfile
import tarfile
import unittest
from unittest.mock import patch

import fitz
import ocr_page_sources as pages
import recover_ocr_cache_sources as recovery
import recover_report_articles as articles
import recovered_article_delivery as delivery
import build_market_views_ocr_fallback as fallback
from private_market_ocr_checkpoint import checkpoint_key
from private_workflow_handoff import create_archive, upload_directory
from report_extraction_source import resolve_extraction_source
from test_build_market_views_ocr_fallback import page_record
from test_recover_ocr_cache_sources import MemoryR2


class OCRPagesTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name); self.input=self.root/'originals'; self.input.mkdir()
        self.cache=self.root/'cache'; (self.cache/'pages').mkdir(parents=True)
        self.workspace=self.root/'workspace'; self.workspace.mkdir()
        self.client=MemoryR2()
        self.env={'GITHUB_ACTIONS':'true','GITHUB_EVENT_NAME':'workflow_dispatch','GITHUB_REF':'refs/heads/main',
            'GITHUB_REPOSITORY':'owner/repo','GITHUB_WORKFLOW_REF':f'owner/repo/{recovery.WORKFLOW}@refs/heads/main',
            'GITHUB_RUN_ID':'999','GITHUB_SHA':'b'*40,'SOURCE_MODE':'pages'}
        self.producer={'id':123,'path':'.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml',
            'head_branch':'main','head_sha':'a'*40,'status':'completed','event':'schedule',
            'repository':{'full_name':'owner/repo'},'head_repository':{'full_name':'owner/repo'}}

    def seed(self,count=2):
        rows=[]
        for number in range(count):
            path=self.input/f'report-{number:03}.pdf'
            with fitz.open() as doc:
                for p in range(2): doc.new_page().insert_text((40,60),f'Report {number}, page {p+1}.')
                doc.save(path)
            sha=pages.digest(path.read_bytes())
            rows.append({'process_local_path':'/original/'+path.name,'name':path.name,'content_sha256':sha,
                         'dropbox_path':'/zip_backup/261007/'+path.name})
            content=[page_record(p,f'{path.name} 研究需求增长与盈利改善3.4%。'*12) for p in (1,2)]
            (self.cache/'pages'/(pages.extraction_key(sha)+'.json')).write_bytes(pages.encode({'pages':content}))
        self.manifest=self.input/'selected_to_process_manifest.json'; self.manifest.write_text(json.dumps(rows))
        self.request={'source_run_id':'123','date_folder':'261007','expected_reports':count,
                      'manifest_sha256':pages.digest(self.manifest.read_bytes())}
        # These intentionally unusable pending/model values are not consulted.
        (self.cache/'model').mkdir(); (self.cache/'model/old.pending.json').write_bytes(b'PRIVATE unknown summary')
        (self.cache/'final_synthesis').mkdir(); (self.cache/'final_synthesis/old.pending.json').write_bytes(b'PRIVATE unknown final')
        self.publish_cache()

    def publish_cache(self):
        archive=self.root/'cache.tar.gz'; create_archive(self.cache,archive); raw=archive.read_bytes()
        self.cache_key=checkpoint_key(self.manifest,'261007',self.request['expected_reports'])
        self.request.update(archive_sha256=pages.digest(raw),archive_size_bytes=len(raw))
        self.client.objects[self.cache_key]=(raw,{'sha256':pages.digest(raw)})

    def forbidden(self):
        stack=ExitStack()
        for name in ('build','cached_model','extract_pages','call_model','request_with_retry'):
            stack.enter_context(patch.object(fallback,name,side_effect=AssertionError('synthesis/OCR/provider forbidden')))
        stack.enter_context(patch.object(fallback.subprocess,'run',side_effect=AssertionError('no OCR executables')))
        stack.enter_context(patch('requests.Session.request',side_effect=AssertionError('no network')))
        stack.enter_context(redirect_stdout(io.StringIO()))
        return stack

    def recover(self):
        with self.forbidden():
            return recovery.recover(self.input,self.producer,self.request,self.workspace,self.env,self.client,'private')

    def archive(self):
        with self.forbidden():
            return recovery.archive(self.input,self.producer,self.request,self.workspace,self.env,self.client,'private')

    def validate(self,root=None,**kwargs):
        args={'date_folder':'261007','expected_reports':self.request['expected_reports'],'source_run_id':'123',
              'execution_sha':'a'*40,'recovery_run_id':'999','recovery_execution_sha':'b'*40,**kwargs}
        return pages.validate_pages_receipt(root or self.workspace/'source',**args)

    def reseal(self,root=None,mutate=None):
        root=root or self.workspace/'source'; value=json.loads((root/pages.RECEIPT).read_bytes())
        if mutate: mutate(value)
        value['files']=pages.inventory(root); (root/pages.RECEIPT).write_bytes(pages.encode(value))

    def test_44_original_pdfs_and_all_pages_with_summary_pending_zero_provider_calls(self):
        self.seed(44); before=self.client.objects[self.cache_key]
        self.assertEqual(self.recover(),{'reused':False,'reports':44})
        receipt=self.validate()
        self.assertEqual((receipt['source_kind'],receipt['report_count'],receipt['total_pages']),('ocr-pages',44,88))
        self.assertNotIn('summarized_reports',receipt); self.assertNotIn('model',receipt)
        self.assertEqual(receipt['cache_recovery']['archive_sha256'],self.request['archive_sha256'])
        self.assertEqual(len(receipt['files']),133)
        self.archive(); self.assertEqual(self.client.uploads,[f'{pages.PREFIX}/999/261007/shard_0.tar.gz'])
        self.assertEqual(before,self.client.objects[self.cache_key])
        for name in ('market_views_structured.json','figure_candidates.json',recovery.RECEIPT):
            self.assertFalse((self.workspace/'source'/name).exists())

    def test_same_run_retry_reuses_exact_receipt_even_original_archive_missing(self):
        self.seed(); self.recover(); self.archive()
        raw=(self.workspace/'source'/pages.RECEIPT).read_bytes(); del self.client.objects[self.cache_key]
        self.workspace=self.root/'retry'; self.workspace.mkdir()
        with patch.object(pages,'build_pages',side_effect=AssertionError('no rebuild')):
            self.assertTrue(self.recover()['reused'])
        self.archive(); self.assertEqual((self.workspace/'source'/pages.RECEIPT).read_bytes(),raw)
        self.assertEqual(len(self.client.uploads),1)

    def test_private_pdf_exception_is_opt_in_validated_exact_and_namespace_bound(self):
        self.seed(); self.recover(); source=self.workspace/'source'
        default=self.root/'default.tar.gz'; create_archive(source,default)
        with tarfile.open(default) as archive:
            self.assertFalse(any(name.endswith('.pdf') for name in archive.getnames()))
        explicit=self.root/'explicit.tar.gz'; create_archive(source,explicit,include_ocr_page_originals=True)
        with tarfile.open(explicit) as archive:
            self.assertEqual(sorted(name for name in archive.getnames() if name.endswith('.pdf')),
                             ['originals/R001.pdf','originals/R002.pdf'])
        with self.assertRaisesRegex(ValueError,'archive_namespace_invalid'):
            upload_directory(source,f'{recovery.PREFIX}/999/261007/shard_0.tar.gz',client=self.client,
                             bucket='private',include_ocr_page_originals=True)
        self.assertEqual(self.client.uploads,[])
        extra=source/'originals/unrelated.pdf'; extra.write_bytes((source/'originals/R001.pdf').read_bytes())
        self.reseal()
        with self.assertRaisesRegex(pages.OCRPagesError,'unexpected_files'):
            create_archive(source,explicit,include_ocr_page_originals=True)

    def test_same_run_cannot_replace_accepted_receipt_bytes(self):
        self.seed(); self.recover(); self.archive()
        receipt=self.workspace/'source'/pages.RECEIPT
        receipt.write_bytes(receipt.read_bytes()+b'\n')
        with self.assertRaisesRegex(ValueError,'existing_handoff_receipt_changed'): self.archive()
        self.assertEqual(len(self.client.uploads),1)

    def test_pages_mode_does_not_accept_a_synthesis_handoff_namespace(self):
        self.seed()
        self.client.objects[f'{recovery.PREFIX}/999/261007/shard_0.tar.gz']=(b'not a pages source',{'sha256':'0'*64})
        self.assertFalse(self.recover()['reused'])
        self.assertEqual(self.validate()['source_kind'],'ocr-pages')

    def test_missing_last_page_cache_fails_before_any_handoff_write(self):
        self.seed(44); next((self.cache/'pages').glob('*.json')).unlink(); self.publish_cache()
        with self.assertRaisesRegex(pages.OCRPagesError,'file_missing'): self.recover()
        self.assertFalse((self.workspace/'source').exists()); self.assertFalse((self.workspace/'built/261007').exists())
        self.assertEqual(self.client.uploads,[])

    def test_all_page_order_hash_method_empty_flags_and_nonempty_source_are_required(self):
        self.seed()
        file=next((self.cache/'pages').glob('*.json')); original=file.read_bytes()
        cases=[lambda p:p.pop(), lambda p:p.reverse(), lambda p:p[0].update(text_sha256='0'*64),
               lambda p:p[0].update(method='summary'),lambda p:p[0].update(empty_text=True),
               lambda p:[row.update(text='',text_sha256=pages.digest(b''),empty_text=True) for row in p]]
        for mutate in cases:
            payload=json.loads(original); mutate(payload['pages']); file.write_bytes(pages.encode(payload)); self.publish_cache()
            self.workspace=self.root/('case-'+str(cases.index(mutate))); self.workspace.mkdir()
            with self.subTest(case=cases.index(mutate)),self.assertRaises(pages.OCRPagesError): self.recover()
            self.assertFalse((self.workspace/'built/261007').exists())

    def test_cache_key_group_swap_and_original_pdf_change_fail(self):
        self.seed(); files=list((self.cache/'pages').glob('*.json'))
        # A cache key cannot be replaced by an arbitrary group/other identity.
        files[0].rename(files[0].with_name('0'*64+'.json')); self.publish_cache()
        with self.assertRaises(pages.OCRPagesError): self.recover()
        self.assertFalse((self.workspace/'source').exists())
        next(self.input.glob('*.pdf')).write_bytes(b'%PDF-changed')
        with self.assertRaises(ValueError): self.recover()

    def test_pinned_archive_hash_size_and_manifest_identity_remain_mandatory(self):
        self.seed()
        for key in ('archive_sha256','archive_size_bytes','manifest_sha256'):
            original=self.request[key]; self.request[key]=('0'*64 if isinstance(original,str) else original+1)
            with self.subTest(key=key),self.assertRaises(ValueError): self.recover()
            self.assertFalse((self.workspace/'source').exists()); self.request[key]=original

    def test_receipt_original_recovery_and_checkpoint_identity_are_exact(self):
        self.seed(); self.recover()
        for changes in ({'source_run_id':'999'},{'recovery_run_id':'123'},{'recovery_run_id':'998'},
                        {'execution_sha':'c'*40},{'recovery_execution_sha':'c'*40},{'expected_reports':1}):
            with self.subTest(changes=changes),self.assertRaises(ValueError): self.validate(**changes)
        self.reseal(mutate=lambda r:r['cache_recovery'].update(checkpoint_identity='0'*64))
        with self.assertRaises(ValueError): self.validate()

    def test_resealed_pdf_page_or_manifest_swap_cannot_pass(self):
        self.seed(); self.recover()
        source=self.workspace/'source'; pdf=source/'originals/R001.pdf'; original=pdf.read_bytes()
        pdf.write_bytes((source/'originals/R002.pdf').read_bytes()); self.reseal()
        with self.assertRaisesRegex(pages.OCRPagesError,'original_pdf_changed'): self.validate()
        pdf.write_bytes(original); self.reseal()
        page=source/'ocr_sources/R001/pages.json'; page.write_bytes((source/'ocr_sources/R002/pages.json').read_bytes()); self.reseal()
        with self.assertRaisesRegex(pages.OCRPagesError,'extracted_text_changed'): self.validate()

    def test_extra_files_wrong_kind_or_synthesis_claim_are_rejected(self):
        self.seed(); self.recover(); source=self.workspace/'source'
        original=(source/pages.RECEIPT).read_bytes()
        for extra in ({'source_kind':'ocr-synthesis'},{'summarized_reports':2},{'total_pages':999}):
            value=json.loads(original); value.update(extra); (source/pages.RECEIPT).write_bytes(pages.encode(value))
            with self.subTest(extra=extra),self.assertRaises(ValueError): self.validate()
        (source/pages.RECEIPT).write_bytes(original)
        (source/'summary.pending.json').write_bytes(b'{}'); self.reseal()
        with self.assertRaisesRegex(pages.OCRPagesError,'unexpected_files'): self.validate()

    def test_pages_cannot_be_consumed_as_synthesis_or_published_as_synthesized_pdf(self):
        self.seed(); self.recover()
        with self.assertRaises(Exception):
            articles.load_sources(self.workspace/'source','ocr-synthesis',2,'261007',source_run_id='123',
                source_execution_sha='a'*40,source_handoff_run_id='999',source_handoff_execution_sha='b'*40)
        from market_views_publication import publication_plan
        with self.assertRaisesRegex(ValueError,'unsupported_publication_source_kind'):
            publication_plan(Path('/unused.pdf'),'261007',source_kind='ocr-pages')

    def test_44_articles_use_full_pages_and_resume_without_regeneration_or_fabricated_charts(self):
        from test_recover_report_articles import ArticleRecoveryTests
        self.seed(44); self.recover()
        harness=ArticleRecoveryTests(); harness.setUp(); self.addCleanup(harness.doCleanups)
        output=self.root/'articles'
        args=(self.workspace/'source','ocr-pages',output,44,'261007',harness.args)
        kwargs={'source_run_id':'123','source_execution_sha':'a'*40,
                'source_handoff_run_id':'999','source_handoff_execution_sha':'b'*40}
        with harness.paid():
            receipt=articles.recover_articles(*args,**kwargs)
            before=articles.inventory(output)
            replay=articles.recover_articles(*args,**kwargs)
        self.assertEqual(len(harness.calls),44); self.assertEqual(receipt,replay)
        self.assertEqual(articles.inventory(output),before)
        self.assertFalse(list(output.rglob('*.pdf')))
        self.assertEqual(receipt['source_kind'],'ocr-pages')
        for report in receipt['reports']:
            directory=output/report['directory']; status=articles.read_json(directory/'status.json')
            self.assertEqual((status['images'],status['ocr_figures'],status['image_source_kind']),([],[],'ocr_pages_text_only'))
            self.assertEqual(resolve_extraction_source(directory).method,'ocr')
            self.assertIn('Original page 2',(directory/'source_ocr.md').read_text())
        self.assertEqual(articles.validate_articles(output,44,'261007'),receipt)

    def test_bad_last_source_blocks_all_article_calls(self):
        from test_recover_report_articles import ArticleRecoveryTests
        self.seed(); self.recover(); source=self.workspace/'source'
        (source/'ocr_sources/R002/pages.json').write_bytes(b'[]')
        harness=ArticleRecoveryTests(); harness.setUp(); self.addCleanup(harness.doCleanups)
        with harness.paid(),self.assertRaises(ValueError):
            articles.recover_articles(source,'ocr-pages',self.root/'articles',2,'261007',harness.args,
                source_run_id='123',source_execution_sha='a'*40,source_handoff_run_id='999',source_handoff_execution_sha='b'*40)
        self.assertEqual(harness.calls,[])

    def test_workflow_default_and_disjoint_successful_source_gates(self):
        import yaml
        from market_views_source_readiness import SOURCE_KIND_GATES,require_source_readiness
        from test_market_views_source_readiness import ReadinessTests
        workflow=yaml.safe_load((Path(__file__).resolve().parents[1]/recovery.WORKFLOW).read_text())
        on=workflow.get('on',workflow.get(True)); mode=on['workflow_dispatch']['inputs']['source_mode']
        self.assertEqual((mode['default'],mode['options']),('synthesis',['synthesis','pages']))
        steps={s.get('name'):s for s in workflow['jobs']['recover']['steps']}
        for kind,mode in [('ocr-pages','pages'),('ocr-synthesis','synthesis')]:
            gates=SOURCE_KIND_GATES[(recovery.WORKFLOW,kind)][1]
            for gate in gates:
                self.assertEqual(steps[gate]['if'],f"inputs.source_mode == '{mode}'")
                self.assertEqual(steps[gate]['env']['R2_ACCESS_KEY_ID'],'${{ secrets.R2_ACCESS_KEY_ID }}')
                self.assertEqual(steps[gate]['env']['R2_SECRET_ACCESS_KEY'],'${{ secrets.R2_SECRET_ACCESS_KEY }}')
                self.assertEqual(steps[gate]['env']['R2_ACCOUNT_ID'],'${{ secrets.R2_ACCOUNT_ID || vars.R2_ACCOUNT_ID }}')
                self.assertEqual(steps[gate]['env']['R2_BUCKET'],'${{ secrets.R2_BUCKET || vars.R2_BUCKET }}')
            producer,jobs=ReadinessTests().kind_evidence(recovery.WORKFLOW,kind)
            self.assertTrue(require_source_readiness(producer,jobs,source_kind=kind)['ready'])
            other='ocr-synthesis' if kind=='ocr-pages' else 'ocr-pages'
            with self.assertRaises(ValueError): require_source_readiness(producer,jobs,source_kind=other)
            for step in jobs['jobs'][0]['steps']:
                step['conclusion']='skipped'
                with self.assertRaises(ValueError): require_source_readiness(producer,jobs,source_kind=kind)
                step['conclusion']='success'
        self.assertIn("'ocr-pages'",workflow['jobs']['deliver']['with']['source_kind'])
        self.assertNotIn('${{ runner.',str(workflow['jobs']['recover'].get('env',{})))

    def test_real_delivery_prepare_uses_pages_namespace_and_all_attempt_skip_gate(self):
        from test_recovered_article_delivery import Store, original_fixture
        from market_views_source_readiness import SOURCE_KIND_GATES
        self.seed(); self.recover(); source=self.workspace/'source'
        store=Store()
        with redirect_stdout(io.StringIO()): upload_directory(source,f'{pages.PREFIX}/999/261007/shard_0.tar.gz',client=store,bucket='private',include_ocr_page_originals=True)
        config=delivery.inputs({'SOURCE_RUN_ID':'123','SOURCE_HANDOFF_RUN_ID':'999','SOURCE_KIND':'ocr-pages',
                                'DATE_FOLDER':'261007','EXPECTED_ARTICLES':'2'})
        original,attempts=original_fixture(2); original['id']=123
        for attempt in attempts:
            for job in attempt['jobs']: job['run_id']=123
        handoff={**self.producer,'id':999,'head_sha':'b'*40,'path':recovery.WORKFLOW,'event':'workflow_dispatch'}
        name,gates=SOURCE_KIND_GATES[(recovery.WORKFLOW,'ocr-pages')]
        jobs={'total_count':1,'jobs':[{'id':100,'run_id':999,'head_sha':'b'*40,'name':name,'status':'completed',
            'steps':[{'number':i,'name':name,'status':'completed','conclusion':'success'} for i,name in enumerate(gates,1)]}]}
        def job_pages(repo,run,attempt=None): return attempts[attempt-1] if run=='123' else jobs
        with patch.object(delivery,'api',side_effect=lambda repo,run: original if run=='123' else handoff), \
             patch.object(delivery,'jobs',side_effect=job_pages),redirect_stdout(io.StringIO()):
            context=delivery.prepare(self.root/'delivery',config,self.env,store,'private')
            self.assertEqual(context['source_kind'],'ocr-pages')
            self.assertEqual(context['source_receipt_sha256'],pages.digest((source/pages.RECEIPT).read_bytes()))
            attempts[0]['jobs'][1]['conclusion']='success'
            with patch('private_workflow_handoff.download_directory') as download,self.assertRaises(ValueError):
                delivery.prepare(self.root/'blocked',config,self.env,store,'private')
            download.assert_not_called()


if __name__=='__main__': unittest.main()
