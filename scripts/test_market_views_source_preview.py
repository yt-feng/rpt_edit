"""Real raster-only source failure and bounded, labelled PDF recovery."""
import copy
import contextlib
import io
import os
import shutil
import subprocess
import sys
import textwrap
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, Mock

import fitz

import market_views_source_preview as preview
from extract_native_market_sources import extract_sources, SourceValidationError
from prepare_public_market_view_pdf import prepare_public_copy
from daily_market_source_status import evaluate, require_preview_producer, require_provider_only_failure


CTX = {"date": "261005", "run_id": "1234", "sha": "a" * 40}


class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.originals = self.root / "originals"
        self.originals.mkdir()
        self.manifest = self.root / "selected.json"
        self.source = self.root / "preview"
        self.rows = []

    def tearDown(self):
        self.temp.cleanup()

    def pdf(self, name="source.pdf", *, scanned=True, pages=4, blank=False):
        path = self.originals / name
        with fitz.open() as original:
            for number in range(pages):
                page = original.new_page()
                if blank:
                    continue
                with fitz.open() as content:
                    source = content.new_page()
                    source.insert_text((42, 65), f"Market outlook: original rate 171bp - page {number + 1}", fontsize=16)
                    source.insert_textbox(fitz.Rect(42, 110, 550, 350),
                        "Original research: markets, investment, inflation and bond valuation. " * 15, fontsize=12)
                    source.draw_rect(fitz.Rect(70, 420, 190, 670), fill=(.1, .3, .6))
                    source.draw_rect(fitz.Rect(235, 475, 355, 670), fill=(.7, .3, .1))
                    if scanned:
                        page.insert_image(page.rect, pixmap=source.get_pixmap())
                    else:
                        page.show_pdf_page(page.rect, content, 0)
            original.save(path)
        self.rows.append({"process_local_path": f"/runner/original/{name}", "content_sha256": preview.digest(path)})
        self.manifest.write_text(json.dumps(self.rows))
        return path

    def prepare(self):
        with patch("socket.create_connection", side_effect=AssertionError("No provider request allowed")):
            return preview.prepare(self.originals, self.manifest, self.source, len(self.rows), **CTX)

    def test_scanned_source_rejected_by_strict_path_produces_real_public_degraded_pdf(self):
        self.pdf()
        with self.assertRaises(SourceValidationError):
            extract_sources(self.originals, self.manifest, self.root / "strict", 1, enable_ocr=False)
        receipt = self.prepare()
        self.assertEqual(receipt["selected_page_count"], 2)
        private = self.root / "private.pdf"
        public = self.root / "public.pdf"
        with patch("socket.create_connection", side_effect=AssertionError("No model or provider allowed")):
            result = preview.render(self.source, private, 1, **CTX)
            prepare_public_copy(private, public)
        self.assertEqual(result["status"], "degraded")
        self.assertGreater(public.stat().st_size, 1024)
        self.assertTrue(preview.degraded_pdf(public))
        self.assertTrue(preview.readable_pdf(public))
        preview.verify_pdf(public, 2)
        with fitz.open(public) as document:
            self.assertEqual(len(document), 4)
            text = "\n".join(page.get_text() for page in document)
            self.assertIn("备用来源版", text)
            self.assertIn(self.rows[0]["content_sha256"], text)
            self.assertNotIn("171bp", text, "No numeric OCR/model claim may be introduced")
            self.assertEqual(sum(bool(p.get_images()) for p in document), 2)

    def test_real_degraded_pdf_upload_and_final_receipt_bind_exact_private_bytes(self):
        from test_upload_market_view_to_r2 import FakeR2Client
        from upload_market_view_to_r2 import upload_market_view, private_publication_complete
        self.pdf()
        self.prepare()
        private = self.root / 'edition.pdf'
        preview.render(self.source, private, 1, **CTX)
        client = FakeR2Client()
        item = upload_market_view(private, CTX['date'], client=client, bucket='test', edition='source-pages')
        self.assertEqual(item['quality_status'], 'degraded')
        self.assertIn('备用来源版', item['title'])
        self.assertTrue(private_publication_complete(CTX['date'], client=client, bucket='test', expected_sha256=preview.digest(private)))
        self.assertFalse(private_publication_complete(CTX['date'], client=client, bucket='test', expected_sha256='a' * 64))
        with self.assertRaisesRegex(RuntimeError, 'editions disagree'):
            private_publication_complete(CTX['date'], client=client, bucket='test', expected_edition='standard')

    def test_private_and_public_labels_embed_the_bundled_cjk_font(self):
        self.pdf()
        self.prepare()
        private, public = self.root / 'private.pdf', self.root / 'public.pdf'
        preview.render(self.source, private, 1, **CTX)
        prepare_public_copy(private, public)
        for path in (private, public):
            with self.subTest(path=path.name), fitz.open(path) as document:
                for page in document:
                    fonts = [font for font in page.get_fonts() if font[4] == preview.TEXT_FONT_NAME]
                    self.assertEqual(len(fonts), 1)
                    _, extension, _, font_bytes = document.extract_font(fonts[0][0])
                    self.assertEqual(extension, 'ttf')
                    self.assertTrue(font_bytes)
                    self.assertLess(len(font_bytes), len(preview._text_font_buffer()))
                self.assertIn('备用来源版', document[0].get_text())
            preview.verify_pdf(path, 2)

    def test_verifier_rejects_original_unembedded_china_s_regression(self):
        self.pdf()
        self.prepare()
        def legacy_text(page, rect, text, size=11, color=(.12, .16, .22)):
            page.insert_textbox(fitz.Rect(rect), text, fontname='china-s', fontsize=size, color=color)
        with patch.object(preview, '_text', legacy_text), \
                self.assertRaisesRegex(ValueError, 'portable label font'):
            preview.render(self.source, self.root / 'legacy.pdf', 1, **CTX)

    @unittest.skipUnless(shutil.which('pdftoppm'), 'Poppler is needed for cross-renderer verification')
    def test_poppler_renders_cover_directory_and_source_labels_without_cjk_pack(self):
        self.pdf()
        self.prepare()
        private, public = self.root / 'private.pdf', self.root / 'public.pdf'
        preview.render(self.source, private, 1, **CTX)
        prepare_public_copy(private, public)
        result = subprocess.run(['pdftoppm', '-scale-to', '1000', '-png', str(public), str(self.root / 'poppler')],
                                check=True, capture_output=True, text=True, timeout=60)
        self.assertNotIn('Syntax Error', result.stderr)
        images = sorted(self.root.glob('poppler-*.png'))
        self.assertEqual(len(images), 4)
        for index, image in enumerate(images):
            pixmap = fitz.Pixmap(str(image))
            gray = fitz.Pixmap(fitz.csGRAY, pixmap)
            self.assertGreater(sum(value < 245 for value in gray.samples), 1000,
                               f'Page {index + 1} must not be blank')
            if index >= 2:
                # Source images cannot make a missing degradation label pass.
                for top, bottom in ((14, 53), (783, 831)):
                    start = round(top / 842 * gray.height) * gray.width
                    end = round(bottom / 842 * gray.height) * gray.width
                    self.assertGreater(sum(value < 245 for value in gray.samples[start:end]), 100)

    def test_acceptance_private_roundtrip_does_not_write_any_production_object(self):
        from test_upload_market_view_to_r2 import FakeR2Client
        from upload_market_view_to_r2 import upload_market_view
        from accept_market_source_preview import accept
        self.pdf()
        (self.originals / 'selected_to_process_manifest.json').write_bytes(self.manifest.read_bytes())
        client = FakeR2Client()
        # A real original PDF represents an already published normal issue.
        upload_market_view(self.originals / 'source.pdf', CTX['date'], client=client, bucket='test')
        before = copy.deepcopy(client.objects)
        client.calls.clear()
        deleted = []
        def delete(**kwargs):
            deleted.append(kwargs['Key'])
            del client.objects[kwargs['Key']]
        with patch.object(client, 'delete_object', side_effect=delete, create=True), \
                patch('socket.create_connection', side_effect=AssertionError('No provider request')):
            result = accept(self.originals, self.root / 'acceptance', CTX['date'], CTX['run_id'], CTX['sha'],
                            '9876', '1', client=client, bucket='test')
        self.assertEqual(client.objects, before)
        self.assertEqual(deleted, ['_private-workflow-handoff/market-preview-acceptance/9876/1/preview.pdf'])
        self.assertEqual([key for op, key in client.calls if op == 'put'], deleted)
        self.assertTrue(result['production_unchanged'])
        self.assertEqual(result['provider_posts'], 0)

    def test_actual_workflow_reuses_primary_without_degraded_label_or_exception_email(self):
        import daily_market_source_status as daily
        import upload_market_view_to_r2 as uploader
        workflow = Path(__file__).resolve().parents[1] / '.github/workflows/market-views-latex-pdf.yml'
        step = workflow.read_text().split('- name: Verify and render the exact bounded original-page edition', 1)[1].split('\n      - name:', 1)[0]
        program = textwrap.dedent(step.split('        run: |\n', 1)[1]).split("python - <<'PY'\n", 1)[1].rsplit('\nPY', 1)[0]
        source = self.pdf(scanned=False)
        pdf = self.root / 'market_view_summaries' / CTX['date'] / f"market_views_{CTX['date']}.pdf"
        pdf.parent.mkdir(parents=True)
        pdf.write_bytes(source.read_bytes())
        environment = {'GITHUB_REPOSITORY': 'owner/repo', 'SOURCE_RUN_ID': CTX['run_id'],
            'SOURCE_DATE': CTX['date'], 'EXPECTED_ARTICLES': '1', 'GITHUB_ENV': str(self.root / 'env')}
        with contextlib.chdir(self.root), patch.dict(os.environ, environment, clear=True), \
                patch('subprocess.check_output', return_value='{}'), \
                patch.object(daily, 'require_preview_producer', return_value=CTX['sha']), \
                patch.object(preview, 'validate'), patch.object(preview, 'render') as render, \
                patch.object(uploader, 'private_publication_complete', return_value=True):
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(program, str(workflow), 'exec'), {'__name__': '__main__'})
        render.assert_not_called()
        values = dict(line.split('=', 1) for line in (self.root / 'env').read_text().splitlines())
        self.assertEqual(values['SHOULD_BUILD'], 'false')
        self.assertEqual(values['MARKET_EDITION'], 'standard')
        self.assertEqual(values['BACKUP_NOTICE'], '')

    def test_blank_or_missing_sources_cannot_create_successful_placeholder(self):
        self.pdf(blank=True)
        with self.assertRaisesRegex(ValueError, "No readable original pages"):
            self.prepare()
        self.assertFalse(self.source.exists())
        self.originals.joinpath("source.pdf").unlink()
        with self.assertRaisesRegex(ValueError, "inventory"):
            self.prepare()

    def test_source_hash_mismatch_and_receipt_page_tampering_rejected(self):
        original = self.pdf()
        original.write_bytes(original.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self.prepare()
        self.rows[0]["content_sha256"] = preview.digest(original)
        self.manifest.write_text(json.dumps(self.rows))
        self.prepare()
        receipt_path = self.source / "source_preview_receipt.json"
        receipt = json.loads(receipt_path.read_text())
        receipt["reports"][0]["pages"][0]["page"] = 999
        receipt_path.write_text(json.dumps(receipt))
        with self.assertRaisesRegex(ValueError, "position"):
            preview.validate(self.source, 1, **CTX)

    def test_transferred_preview_rejects_changed_image_and_wrong_producer(self):
        self.pdf()
        receipt = self.prepare()
        with self.assertRaisesRegex(ValueError, "provenance"):
            preview.validate(self.source, 1, **{**CTX, "sha": "b" * 40})
        image = self.source / receipt["reports"][0]["pages"][0]["image"]
        image.write_bytes(image.read_bytes() + b"modified")
        with self.assertRaisesRegex(ValueError, "integrity"):
            preview.validate(self.source, 1, **CTX)

    def test_limits_keep_all_manifest_bindings_and_explicitly_record_coverage(self):
        self.pdf("first.pdf", pages=5)
        self.pdf("second.pdf", pages=5)
        self.pdf("third.pdf", pages=5)
        with patch.object(preview, "MAX_PAGES", 2):
            receipt = self.prepare()
        self.assertEqual(receipt["report_count"], 3)
        self.assertEqual(receipt["selected_page_count"], 2)
        self.assertEqual(receipt["reports"][-1]["status"], "page_budget")
        self.assertEqual(len(receipt["reports"][-1]["pages"]), 0)

    def test_budget_exhaustion_with_no_images_is_not_success(self):
        self.pdf()
        with patch.object(preview, "MAX_BYTES", 1), self.assertRaisesRegex(ValueError, "No readable"):
            self.prepare()


class DailyOutcomeTests(unittest.TestCase):
    def jobs(self):
        return {"total_count": 2, "jobs": [
            {"name": f"process-shard ({i})", "run_id": 1234, "head_sha": "a" * 40,
             "status": "completed", "conclusion": "success", "steps": [
                 {"name": "Generate shard outputs", "conclusion": "success"},
                 {"name": "Upload shard to private R2 handoff", "conclusion": "success"}]} for i in range(2)]}

    def test_continue_on_error_cannot_admit_failed_or_unpublished_shards(self):
        data = self.jobs()
        self.assertTrue(evaluate(data, 2, "1234", "a" * 40)["primary_ready"])
        data["jobs"][0]["steps"][0]["conclusion"] = "failure"
        result = evaluate(data, 2, "1234", "a" * 40)
        self.assertFalse(result["primary_ready"])
        self.assertEqual(result["degraded_shards"], 1)
        data["jobs"][0]["steps"][0]["conclusion"] = "success"
        data["jobs"][0]["steps"][1]["conclusion"] = "skipped"
        self.assertFalse(evaluate(data, 2, "1234", "a" * 40)["primary_ready"])

    def test_incomplete_duplicate_foreign_or_running_jobs_fail_closed(self):
        for field, value in (("head_sha", "b" * 40), ("run_id", 999), ("status", "in_progress"), ("name", "process-shard (1)")):
            data = self.jobs()
            data["jobs"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                evaluate(data, 2, "1234", "a" * 40)
        with self.assertRaises(ValueError):
            evaluate({"jobs": [], "total_count": 2}, 2, "1234", "a" * 40)

    def test_empty_selection_is_explicit_noop_without_handoff_or_pdf_claim(self):
        data = {'total_count': 1, 'jobs': [{'name': 'select-macro-reports'}]}
        result = evaluate(data, 0, '1234', 'a' * 40, selected_count=0)
        self.assertTrue(result['no_work'])
        self.assertFalse(result['primary_ready'])
        data = self.jobs()
        for job in data['jobs']:
            job['steps'] = [{'name': 'Gate shard', 'conclusion': 'success'},
                            {'name': 'Generate shard outputs', 'conclusion': 'skipped'}]
        self.assertTrue(evaluate(data, 2, '1234', 'a' * 40, 0)['no_work'])
        data['jobs'][0]['steps'][0]['conclusion'] = 'failure'
        with self.assertRaises(ValueError):
            evaluate(data, 2, '1234', 'a' * 40, 0)

    def test_provider_proof_never_masks_install_upload_checkpoint_or_code_failure(self):
        data = self.jobs()
        bad = data['jobs'][0]
        bad['steps'][0]['conclusion'] = 'failure'
        bad['steps'][1]['conclusion'] = 'skipped'
        bad['steps'].append({'name': 'Confirm provider-only source degradation', 'conclusion': 'success'})
        self.assertTrue(evaluate(data, 2, '1234', 'a' * 40)['provider_only'])
        for name in ('Checkout repository', 'Install dependencies', 'Upload shard to private R2 handoff',
                     'Save private generation checkpoint including partial progress', 'Confirm provider-only source degradation'):
            changed = copy.deepcopy(data)
            changed['jobs'][0]['steps'].append({'name': name, 'conclusion': 'failure'})
            self.assertFalse(evaluate(changed, 2, '1234', 'a' * 40)['provider_only'])
        batch = {'returncode': 2, 'status': 'failed', 'provider_failure_category': 'mineru_unavailable'}
        self.assertEqual(require_provider_only_failure({'failures': 1, 'batches': [batch]}), 1)
        for bad in ({**batch, 'provider_failure_category': ''}, {'returncode': 99, 'status': 'failed'}):
            with self.assertRaises(ValueError):
                require_provider_only_failure({'failures': 2, 'batches': [batch, bad]})

    def test_cloud_acceptance_requires_exact_completed_daily_and_selection_upload(self):
        from accept_market_source_preview import verify_frozen_daily
        producer = {'id': 1234, 'head_sha': CTX['sha'], 'head_branch': 'main', 'event': 'schedule',
            'path': '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml', 'status': 'completed',
            'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'}}
        job = {'name': 'select-macro-reports', 'run_id': 1234, 'head_sha': CTX['sha'],
               'status': 'completed', 'conclusion': 'success', 'steps': [
                   {'name': 'Upload selected macro PDFs artifact', 'conclusion': 'success'}]}
        page = {'total_count': 1, 'jobs': [job]}
        self.assertEqual(verify_frozen_daily(producer, page, '1234', 'owner/repo'), CTX['sha'])
        job['steps'][0]['conclusion'] = 'failure'
        with self.assertRaises(ValueError):
            verify_frozen_daily(producer, page, '1234', 'owner/repo')

    def test_consumer_requires_exact_original_page_recovery_gates(self):
        producer = {"id": 1234, "head_sha": "a" * 40, "head_branch": "main", "event": "schedule",
            "path": ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml",
            "repository": {"full_name": "owner/repo"}, "head_repository": {"full_name": "owner/repo"}}
        job = {"name": "recover-market-sources", "run_id": 1234, "head_sha": "a" * 40, "steps": [
            {"name": name, "status": "completed", "conclusion": "success"} for name in (
                "Prepare bounded original-page edition", "Save bounded original-page edition to private R2")]}
        page = {"total_count": 1, "jobs": [job]}
        self.assertEqual(require_preview_producer(producer, page, "1234", "owner/repo"), "a" * 40)
        for index in range(2):
            broken = copy.deepcopy(page)
            broken["jobs"][0]["steps"][index]["conclusion"] = "failure"
            with self.assertRaises(ValueError):
                require_preview_producer(producer, broken, "1234", "owner/repo")


class ProviderClassificationTests(unittest.TestCase):
    def test_actual_batch_cli_keeps_mixed_editorial_and_provider_failure_fatal(self):
        import pdf_to_xhs_batch as batch
        from consume_legacy_mineru import NetworkStop
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            sources = [root / 'a.pdf', root / 'b.pdf']
            for source in sources:
                source.write_bytes(b'%PDF-synthetic')
            marker = root / 'provider.json'
            argv = ['batch', '--input-dir', str(root), '--output-dir', str(root / 'out'), '--provider-outcome-path', str(marker)]
            ledger = Mock()
            ledger.run.return_value = ([(source, {'state': 'done'}) for source in sources],
                {'ready_for_generation': True, 'pending': 0, 'failed': 0})
            for first, expects_marker in ((RuntimeError('editorial quality failure'), False),
                                           ({'wechat_article': 'wechat_article.md'}, True)):
                with patch.object(sys, 'argv', argv), patch.object(batch, 'mineru_tokens_from_env', return_value=[('MINER_U', 'test')]), \
                        patch.object(batch, 'from_environment', return_value=ledger), \
                        patch.object(batch, 'find_pdfs', return_value=sources), patch.object(batch, 'input_sources'), \
                        patch.object(batch, 'result_cache_contexts', return_value=(object(), {})), \
                        patch.object(batch, 'process_pdf', side_effect=[first, NetworkStop('network_stop')]), \
                        patch.object(batch, 'log'), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(batch.main(), 2)
                self.assertEqual(marker.exists(), expects_marker)
                marker.unlink(missing_ok=True)

    def test_code_cache_identity_and_r2_failures_are_not_provider_outcomes(self):
        import pdf_to_xhs_batch as batch
        from mineru_task_ledger import LedgerError, DefinitiveAuthRejection
        from consume_legacy_mineru import NetworkStop
        for error in (RuntimeError('bug'), LedgerError('Cache receipt SHA mismatch'),
                      LedgerError('R2 authorization failed'), LedgerError('Original source binding differs')):
            self.assertFalse(batch.recoverable_provider_error(error))
        for error in (DefinitiveAuthRejection('HTTP401', 401), NetworkStop('tls_certificate_expired'),
                      LedgerError('MinerU request rejected or malformed: HTTP 429')):
            self.assertTrue(batch.recoverable_provider_error(error))


if __name__ == "__main__":
    unittest.main()
