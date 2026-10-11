"""Same-fetch provenance, independent cursors and private candidate recovery."""
import copy
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest import mock

from offline_translation import TranslationBudgetExceeded
from build_portal_extended_locales import Memo
from portal_english_commentary import (build, extract_editorial, freeze_editorial, make_source, put_source,
                                      PREFIX, POLICY)
from portal_english_pipeline import (batch_admission, content_key, followup_needed, pending_docs,
                                    persist_candidate, prepare_queued, read_admission, read_completed,
                                    remember_checkpoint, restore_candidate, restore_seed, staging_probe, main, verify_body,
                                    completed_day_is_durable, read_ready_queue)
from portal_extended_daily_queue import WORKFLOW, admit
from portal_extended_locales import (DAILY_SCOPE, ExpansionError, digest, document_from_html, stable_bytes)
from portal_extended_r2 import R2IntegrityError, R2NotFound, R2PermissionError, R2Store
from test_portal_english_commentary import DAY, COMMENT, TITLE, SyntheticTranslator, page
from test_portal_extended_r2 import FakeR2

SOURCE_PRODUCER = {'run_id': '123', 'attempt': '1', 'sha': 'b'*40, 'repository': 'example/repo', 'workflow': WORKFLOW}
CPU_PRODUCER = {'run_id': '456', 'attempt': '1', 'sha': 'c'*40, 'repository': 'example/repo',
                'workflow': '.github/workflows/portal-extended-locales-r2.yml'}


class EnglishPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(); self.root = Path(self.temporary.name)
        self.client = FakeR2(); self.store = R2Store(self.client, 'private', '_extended-locales/staging/english-pipeline')
        self.original = R2Store(self.client, 'private', '_extended-locales/staging/original')

    def tearDown(self): self.temporary.cleanup()

    def admit(self, count=1, day=DAY, *, content=None):
        docs, originals = [], []
        for number in range(count):
            identifier = day.replace('-', '')+'-'+f'{number:016x}'
            from portal_extended_locales import ORIGIN
            url = f'{ORIGIN}/blog/{identifier}.html'; raw = page(content, url=url, day=day)
            docs.append(extract_editorial(url, raw, day))
            original = document_from_html(url, raw, exclude_related=True)
            original.update(selection_scope=DAILY_SCOPE, selection_day=day)
            original['content_sha256'] = digest(stable_bytes({k:v for k,v in original.items() if k != 'content_sha256'}))
            originals.append(original)
        admitted = admit(self.original, originals, day, SOURCE_PRODUCER)
        english = freeze_editorial(self.store, docs, day, SOURCE_PRODUCER, admitted['admission'])
        return english, docs

    def build_candidate(self):
        prepared = prepare_queued(self.store, self.original)
        _, _, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        directory = self.root/source['generation']; checkpoint = self.root/(source['generation']+'.json')
        result = build(source, directory, checkpoint, SyntheticTranslator())
        return prepared, source, directory, checkpoint, result

    def test_numeric_advisory_survives_persistence_restore_and_legacy_manifest_without_rewrite(self):
        self.admit(content='<section><strong>KC评论：</strong>我的理解是增长5.3%。</section>')
        prepared = prepare_queued(self.store, self.original)
        _, _, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        for version in (1, 2):
            with self.subTest(version=version):
                directory = self.root/f'numeric-{version}'; checkpoint = self.root/f'numeric-{version}.json'
                translator = SyntheticTranslator(); original = translator.translate
                translator.translate = lambda value, **kwargs: original(value, **kwargs) if value == TITLE else 'In our view, growth is 6.3%.'
                manifest = build(source, directory, checkpoint, translator)
                if version == 1:
                    manifest['schema_version'] = 1; manifest.pop('public_files_sha256')
                    (directory/'candidate-manifest.json').write_bytes(stable_bytes(manifest))
                original_manifest = (directory/'candidate-manifest.json').read_bytes()
                saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
                self.assertTrue(saved['ready'])
                before = copy.deepcopy(self.client.objects)
                restored = self.root/f'numeric-restored-{version}'
                _, actual, _ = restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], restored)
                self.assertEqual(actual, manifest)
                self.assertEqual((restored/'candidate-manifest.json').read_bytes(), original_manifest)
                self.assertEqual(self.client.objects, before)
                item = manifest['items'][0]; doc = source['documents'][0]
                raw = (restored/'private'/'bodies'/f'{item["body_sha256"]}.json').read_bytes()
                verified = verify_body(raw, item, doc)
                self.assertIn('6.3%', verified['blocks'][0]['text'])
                # Altering content with a matching recomputed hash cannot
                # bypass the remaining English asset/language/template rules.
                for bad in ('Read https://example.invalid/chart', '<b>Growth</b>', '增长6.3%。',
                            'Growth __KC_PH_000__', 'Growth\ufffd', 'Growth | 6.3%'):
                    changed = copy.deepcopy(verified); changed['blocks'][0]['text'] = bad
                    from portal_english_commentary import preview_text
                    try:
                        changed['preview'] = preview_text(changed['blocks'])
                    except ExpansionError:
                        changed['preview'] = 'Rejected invalid content.'
                    encoded = stable_bytes(changed)
                    changed_item = {**item, 'preview':changed['preview'], 'body_sha256':digest(encoded)}
                    with self.subTest(bad=bad), self.assertRaises(ExpansionError):
                        verify_body(encoded, changed_item, doc)

    def failed_inspection_fixture(self):
        self.admit()
        prepared = prepare_queued(self.store, self.original)
        _, _, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        directory = self.root/'failed-candidate'; checkpoint = self.root/'failed-checkpoint.json'
        translator = SyntheticTranslator()
        original = translator.translate
        translator.translate = lambda value, *a, **kw: 'A' * 600 if value == TITLE else original(value, *a, **kw)
        manifest = build(source, directory, checkpoint, translator)
        self.assertEqual(manifest['status'], 'incomplete-candidate')
        # Historic producer versions saved a generic-valid title before the
        # stricter English size gate rejected it. Keep that real old storage
        # shape in the read-only inspection fixture; current build must not
        # create this poisoned row anymore.
        memo = Memo(checkpoint, 'en', translator, time.monotonic()+30, source_generation=source['generation'])
        memo.get(TITLE)
        manifest['failures'][0]['code'] = 'expansion-validation'
        (directory/'candidate-manifest.json').write_bytes(stable_bytes(manifest))
        saved_checkpoint = remember_checkpoint(self.store, source['generation'], checkpoint)
        candidate = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        return source, saved_checkpoint, candidate, manifest

    def test_exact_english_recovery_reads_original_batch_without_mutation(self):
        from portal_english_pipeline import prepare_exact
        source, checkpoint, candidate, _ = self.failed_inspection_fixture()
        before = copy.deepcopy(self.client.objects)
        result = prepare_exact(self.store, self.original, source['generation'])
        self.assertEqual(self.client.objects, before)
        self.assertEqual(result['generation'], source['generation'])
        self.assertEqual(json.loads(result['locale_jobs_json']), [{'locale': 'en',
            'generation': source['generation'], 'day': source['day']}])
        self.assertEqual(result['source_writes'], 0)
        self.assertEqual(result['source_admission'], '')
        with self.assertRaises((ExpansionError, R2NotFound)):
            prepare_exact(self.store, self.original, 'f'*64)

    def test_exact_english_recovery_keeps_existing_cpu_and_publication_bounds(self):
        workflow = (Path(__file__).resolve().parents[1]/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        self.assertIn("'extended-locales-r2-pipeline'", workflow)
        self.assertIn('max-parallel: 2', workflow)
        self.assertIn('cancel-in-progress: false', workflow)
        self.assertIn('scripts/portal_english_pipeline.py prepare-exact', workflow)
        self.assertIn("vars.PORTAL_ENGLISH_AUTO_PUBLISH == 'true'", workflow)

    def test_exact_failed_english_inspection_is_read_only_and_excludes_private_text(self):
        from inspect_portal_extended_continuation import inspect_english
        source, checkpoint, candidate, _ = self.failed_inspection_fixture()
        before = copy.deepcopy(self.client.objects)
        result = inspect_english(self.store, self.original, source['generation'], checkpoint['sha256'],
                                 candidate['candidate_id'], self.root/'inspection')
        self.assertEqual(self.client.objects, before)
        self.assertEqual(result['failure_code_counts'], {'expansion-validation': 1})
        self.assertEqual(result['failed_documents'][0]['units'][0]['validation'], 'english-text-size')
        self.assertEqual(result['failed_documents'][0]['units'][0]['cached_characters'], 600)
        self.assertEqual((result['production_writes'], result['model_calls'], result['paid_provider_requests']), (0, 0, 0))
        public = (self.root/'inspection/inspection.json').read_text()
        for private in (TITLE, COMMENT, 'A' * 600, source['documents'][0]['id'], source['documents'][0]['source_url']):
            self.assertNotIn(private, public)
        self.assertEqual([path.name for path in (self.root/'inspection').iterdir()], ['inspection.json'])

    def test_missing_quantity_translation_has_source_mask_diagnostics_without_model_or_writes(self):
        from inspect_portal_extended_continuation import inspect_english
        quantity_text = '我的理解是增长5.3%，九成订单仍未交付。'
        later_text = '尚未尝试的私有后续评论。'
        self.admit(content=f'<section><strong>KC评论：</strong><p>{COMMENT}</p>'
                           f'<p>{quantity_text}</p><p>{later_text}</p></section>')
        prepared = prepare_queued(self.store, self.original)
        _, _, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        directory = self.root/'quantity-candidate'; checkpoint = self.root/'quantity-checkpoint.json'
        translator = SyntheticTranslator(); original = translator.translate
        def translate(value, *args, **kwargs):
            if value == quantity_text:
                from hymt_offline_translation import validate_result
                rejected = 'Growth is 5.4%; 90% of orders are undelivered.'
                validate_result(value, rejected, 'zh', 'en')
                return rejected
            return original(value, *args, **kwargs)
        translator.translate = translate
        manifest = build(source, directory, checkpoint, translator)
        self.assertEqual(manifest['failures'][0]['code'], 'offline-quantity-validation')
        saved = remember_checkpoint(self.store, source['generation'], checkpoint)
        candidate = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        before = copy.deepcopy(self.client.objects)
        with mock.patch('hymt_offline_translation.HyMTOfflineTranslator._engine',
                        side_effect=AssertionError('Inspection must never start a model')):
            result = inspect_english(self.store, self.original, source['generation'], saved['sha256'],
                                     candidate['candidate_id'], self.root/'quantity-inspection')
        self.assertEqual(self.client.objects, before)
        diagnostic = result['failed_documents'][0]
        self.assertEqual(diagnostic['first_unvalidated_unit_index'], 2)
        self.assertEqual([unit['cached'] for unit in diagnostic['units']], [True, True, False, False])
        signals = diagnostic['units'][2]['quantity_signals']
        self.assertEqual(signals['source_quantities']['total_rows'], 2)
        fragment = signals['fragments'][0]
        self.assertEqual(fragment['third_visible_quantities']['rows'][0]['values'], ['5.3'])
        self.assertCountEqual(fragment['third_residual_quantities']['rows'], fragment['third_visible_quantities']['rows'])
        self.assertEqual((result['production_writes'], result['model_calls'], result['paid_provider_requests']), (0, 0, 0))
        for private in (COMMENT, quantity_text, later_text, 'Growth is 5.4%', source['documents'][0]['id']):
            self.assertNotIn(private, json.dumps(result, ensure_ascii=False))
        self.assertEqual([path.name for path in (self.root/'quantity-inspection').iterdir()], ['inspection.json'])

    def test_english_source_quantity_signals_match_retry_fragments_and_never_emit_source_facts(self):
        from inspect_portal_extended_continuation import english_source_quantity_signals
        source = r'私有标题 171bp后，九成订单，3亿元，符号\%。'
        result = english_source_quantity_signals(source)
        fragment = result['fragments'][0]
        self.assertEqual(fragment['adapter_escaped_character_count'], 1)
        self.assertEqual(fragment['third_protected_fact_count'], 1)
        self.assertEqual(fragment['third_visible_fact_count'], 2)
        self.assertEqual(fragment['third_protected_han_fact_count'], 0)
        self.assertCountEqual(fragment['third_residual_quantities']['rows'], fragment['third_visible_quantities']['rows'])
        self.assertNotIn('私有标题', json.dumps(result, ensure_ascii=False))
        self.assertNotIn('3亿元', json.dumps(result, ensure_ascii=False))
        self.assertNotIn('171bp', json.dumps(result, ensure_ascii=False))
        self.assertEqual(english_source_quantity_signals('私' * 1801)['mask_status'], 'offline-context-limit')
        many = english_source_quantity_signals(('Private sentence. ' * 110) * 25)
        self.assertGreater(many['fragment_count'], 20)
        self.assertEqual(len(many['fragments']), 20); self.assertTrue(many['fragments_truncated'])
        crowded = english_source_quantity_signals(' '.join(['9' * 500] + [str(n) for n in range(1, 80)]))
        signatures = crowded['source_quantities']
        self.assertEqual(signatures['total_rows'], 80); self.assertEqual(len(signatures['rows']), 64)
        self.assertEqual(len(signatures['rows'][0]['values'][0]), 128); self.assertTrue(signatures['truncated'])

    def test_english_inspection_rejects_unknown_error_kind_without_printing_it(self):
        from inspect_portal_extended_continuation import inspect_english
        source, checkpoint, candidate, manifest = self.failed_inspection_fixture()
        manifest['failures'][0]['code'] = 'private-commentary-disguised-as-error'
        raw = stable_bytes(manifest); candidate_id = digest(raw)
        self.store._put(self.store.key('candidates', source['generation'], candidate_id, 'candidate-manifest.json'),
                        raw, metadata={'kind': 'synthetic-contaminated-manifest'})
        before = copy.deepcopy(self.client.objects)
        with self.assertRaisesRegex(ExpansionError, '^Unrecognized English failure code$'):
            inspect_english(self.store, self.original, source['generation'], checkpoint['sha256'], candidate_id,
                            self.root/'rejected')
        self.assertFalse((self.root/'rejected').exists()); self.assertEqual(self.client.objects, before)

    def test_english_inspection_rejects_corrupt_checkpoint_candidate_and_admission(self):
        from inspect_portal_extended_continuation import inspect_english
        source, checkpoint, candidate, _ = self.failed_inspection_fixture()
        keys = [self.store.checkpoint_object_key('en', source['generation'], checkpoint['sha256']),
                self.store.key('candidates', source['generation'], candidate['candidate_id'], 'candidate-manifest.json'),
                self.store.key('batch-admissions', source['generation'], 'receipt.json')]
        for number, key in enumerate(keys):
            with self.subTest(key=number):
                original = copy.deepcopy(self.client.objects[key])
                self.client.objects[key]['body'] = b'{}'
                before = copy.deepcopy(self.client.objects)
                with self.assertRaises((ExpansionError, R2IntegrityError)):
                    inspect_english(self.store, self.original, source['generation'], checkpoint['sha256'],
                                    candidate['candidate_id'], self.root/f'corrupt-{number}')
                self.assertEqual(self.client.objects, before)
                self.assertFalse((self.root/f'corrupt-{number}').exists())
                self.client.objects[key] = original

    def test_english_inspection_cli_selects_separate_namespace_and_preserves_storage(self):
        import inspect_portal_extended_continuation as inspection
        source, checkpoint, candidate, _ = self.failed_inspection_fixture()
        args = ['inspect', '--locale', 'en', '--generation', source['generation'],
                '--checkpoint-sha', checkpoint['sha256'], '--candidate-id', candidate['candidate_id'],
                '--prefix', self.store.prefix, '--source-prefix', self.original.prefix,
                '--output', str(self.root/'cli-inspection')]
        before = copy.deepcopy(self.client.objects)
        with mock.patch('sys.argv', args), mock.patch.object(inspection.R2Store, 'from_env', return_value=self.store) as make_store, \
             mock.patch('builtins.print') as printed:
            inspection.main()
        make_store.assert_called_once_with(self.store.prefix)
        self.assertEqual(json.loads(printed.call_args.args[0])['locale'], 'en')
        self.assertEqual(self.client.objects, before)

    def test_english_failure_counts_are_enumerated_and_never_copy_unknown_text(self):
        from portal_english_commentary import failure_code_counts
        identifier = DAY.replace('-', '')+'-'+('a'*16)
        self.assertEqual(failure_code_counts([{'id': identifier, 'code': 'offline-http-503-memory'}]),
                         {'offline-http-503-memory': 1})
        for failures in ([{'id': identifier, 'code': 'PRIVATE RAW ERROR'}],
                         [{'id': identifier, 'code': 'offline-http-503-private-comment'}],
                         [{'id': identifier, 'code': 'expansion-validation', 'text': COMMENT}],
                         [{'id': identifier, 'code': 'expansion-validation'}] * 2):
            with self.subTest(case=failures), self.assertRaises(ExpansionError):
                failure_code_counts(failures)

    def test_failed_english_cli_reports_codes_and_preserves_nonzero_exit(self):
        import portal_english_commentary as english
        source, checkpoint, candidate, manifest = self.failed_inspection_fixture()
        corpus = self.root/'cli-source.json'; corpus.write_bytes(stable_bytes(source))
        args = ['english', '--corpus', str(corpus), '--output', str(self.root/'cli-candidate'),
                '--checkpoint', str(self.root/'failed-checkpoint.json')]
        environment = {'GITHUB_ACTIONS': 'true', 'RUNNER_OS': 'Linux',
                       'GITHUB_REF': 'refs/heads/main', 'KC_PUBLIC_REPOSITORY': 'true'}
        translator = SyntheticTranslator(); original = translator.translate
        translator.translate = lambda value, *a, **kw: 'A' * 600 if value == TITLE else original(value, *a, **kw)
        with mock.patch.dict('os.environ', environment), mock.patch('sys.argv', args), \
             mock.patch.object(english, 'OfflineTranslator', return_value=translator), \
             mock.patch('builtins.print') as printed:
            self.assertEqual(english.main(), 1)
        summary = json.loads(printed.call_args.args[0])
        self.assertEqual(summary['status'], 'incomplete-candidate')
        self.assertEqual(summary['failure_code_counts'], {'english-size-validation': 1})
        self.assertFalse(summary['budget_exhausted'])
        self.assertNotIn(TITLE, printed.call_args.args[0]); self.assertNotIn(COMMENT, printed.call_args.args[0])

    def test_empty_queue_never_crawls_history_or_sets_up_a_model(self):
        self.assertIsNone(prepare_queued(self.store, self.original)['job'])
        self.assertEqual(self.client.objects, {})

    def test_corpus_requires_same_capture_bytes_original_producer_and_date(self):
        admitted, docs = self.admit()
        receipt, source = read_admission(self.store, admitted['receipt'], self.original)
        self.assertEqual(source['documents'], docs); self.assertEqual(receipt['producer'], SOURCE_PRODUCER)
        bad = copy.deepcopy(docs[0]); bad['source_html_sha256'] = 'd'*64
        bad['editorial_sha256'] = digest(stable_bytes({k:v for k,v in bad.items() if k != 'editorial_sha256'}))
        frozen = freeze_editorial(self.store, [bad], DAY, SOURCE_PRODUCER, receipt['source_admission'])
        with self.assertRaises(ExpansionError): read_admission(self.store, frozen['receipt'], self.original)

    def test_latest_admitted_day_first_with_deterministic_24_page_cursor(self):
        self.admit(2, '2026-09-30'); self.admit(25)
        prepared = prepare_queued(self.store, self.original)
        self.assertEqual(prepared['job']['locale'], 'en'); self.assertEqual(prepared['job']['day'], DAY)
        self.assertEqual(prepared['selected_pages'], 24); self.assertEqual(prepared['pending_count'], 25)
        proof, receipt, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        self.assertEqual(len(source['documents']), 24); self.assertEqual(proof['admission'], prepared['admission'])
        self.assertEqual(receipt['pages'], 25)

    def test_ready_written_only_after_all_private_public_objects_and_source_verify(self):
        self.admit(); prepared, source, directory, checkpoint, result = self.build_candidate()
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertTrue(saved['ready']); self.assertFalse(saved['indexable']); self.assertFalse(saved['deployed'])
        self.assertEqual(saved['completed_page_count'], 1)
        ready, restored, restored_source = restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], self.root/'restore')
        self.assertEqual(restored, result); self.assertEqual(restored_source, source)
        self.assertEqual(ready['producer'], CPU_PRODUCER)
        self.assertEqual(read_completed(self.store, DAY)[source['documents'][0]['id']]['candidate_id'], saved['candidate_id'])
        self.assertIsNone(prepare_queued(self.store, self.original)['job'])
        for relative in ready['files']:
            self.assertEqual((self.root/'restore'/relative).read_bytes(), (directory/relative).read_bytes())
        self.assertTrue(all(obj['CacheControl'] == 'private, no-store' for obj in self.client.objects.values()))
        self.assertFalse(any(key.endswith('/active.json') for key in self.client.objects))

    def test_preview_revision_creates_new_identity_for_complete_and_incomplete_candidates(self):
        import portal_english_ui as ui
        for incomplete in (False, True):
            with self.subTest(incomplete=incomplete):
                engine = EnglishPipelineTests(); engine.setUp(); self.addCleanup(engine.tearDown)
                engine.admit(2)
                prepared = prepare_queued(engine.store, engine.original)
                _, _, source = batch_admission(engine.store, engine.original, prepared['job']['generation'])
                saved, manifests, dirs = [], [], []
                for revision in ('old', 'new'):
                    directory = engine.root/revision
                    translator = SyntheticTranslator()
                    translate = translator.translate
                    failed = False
                    def fail_once(value, *args, **kwargs):
                        nonlocal failed
                        if incomplete and not failed:
                            failed = True
                            raise RuntimeError('synthetic translation failure')
                        return translate(value, *args, **kwargs)
                    translator.translate = fail_once
                    original_head = ui.head
                    def revised_head(*args, **kwargs):
                        return original_head(*args, **kwargs).replace('</head>', f'<meta name="revision" content="{revision}"></head>')
                    with mock.patch.object(ui, 'head', side_effect=revised_head):
                        manifest = build(source, directory, engine.root/(revision+'.json'), translator)
                        result = persist_candidate(engine.store, engine.original, source, directory, CPU_PRODUCER)
                    saved.append(result); manifests.append(manifest); dirs.append(directory)
                    self.assertEqual(result['ready'], not incomplete)
                self.assertEqual(manifests[0]['items'], manifests[1]['items'])
                self.assertEqual(manifests[0]['translation_calls'], manifests[1]['translation_calls'])
                self.assertNotEqual(saved[0]['candidate_id'], saved[1]['candidate_id'])
                for result, directory in zip(saved, dirs):
                    base = engine.store.key('candidates', source['generation'], result['candidate_id'])
                    self.assertEqual(engine.store._get(base+'/public/en/index.html', maximum=2*1024*1024),
                                     (directory/'public/en/index.html').read_bytes())
                    if not incomplete:
                        restore_candidate(engine.store, engine.original, source['generation'], result['candidate_id'],
                                          engine.root/('restore-'+result['candidate_id']))
                if incomplete:
                    self.assertEqual(read_completed(engine.store, DAY), {})
                    self.assertEqual(read_ready_queue(engine.store), [])

    def test_legacy_candidate_restores_and_carries_forward_after_manifest_upgrade(self):
        self.admit(); _, source, directory, _, manifest = self.build_candidate()
        manifest['schema_version'] = 1; manifest.pop('public_files_sha256')
        (directory/'candidate-manifest.json').write_bytes(stable_bytes(manifest))
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        _, restored, _ = restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], self.root/'legacy')
        self.assertEqual(restored, manifest)
        self.admit(1, '2026-10-03')
        self.assertEqual(len(read_ready_queue(self.store)), 1)

    def test_manifest_preview_digest_rejects_edited_preview_inventory(self):
        self.admit(); _, source, directory, _, manifest = self.build_candidate()
        manifest['public_files_sha256'] = 'f'*64
        (directory/'candidate-manifest.json').write_bytes(stable_bytes(manifest))
        with self.assertRaisesRegex(ExpansionError, 'preview identity differs'):
            persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertFalse(any('/candidates/' in key for key in self.client.objects))

    def test_unchanged_comments_skip_even_after_navigation_html_changes(self):
        self.admit(); _, source, directory, _, _ = self.build_candidate()
        persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        changed = copy.deepcopy(source['documents'][0]); changed['source_html_sha256'] = 'e'*64
        changed['editorial_sha256'] = digest(stable_bytes({k:v for k,v in changed.items() if k != 'editorial_sha256'}))
        self.assertEqual(content_key(changed), content_key(source['documents'][0]))
        self.assertEqual(pending_docs(self.store, make_source([changed], DAY)), [])

    def test_after_complete_first_batch_next_cursor_selects_only_remaining_page(self):
        admitted, _ = self.admit(25); prepared, source, directory, _, _ = self.build_candidate()
        persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        next_batch = prepare_queued(self.store, self.original)
        self.assertEqual(next_batch['pending_count'], 1); self.assertEqual(next_batch['selected_pages'], 1)
        self.assertNotEqual(next_batch['job']['generation'], prepared['job']['generation'])
        _, _, remaining = batch_admission(self.store, self.original, next_batch['job']['generation'])
        self.assertEqual(remaining['documents'][0]['id'], DAY.replace('-', '')+'-'+f'{24:016x}')
        self.assertTrue(followup_needed(self.store, self.original, admitted['receipt'], 25)['continue'])
        self.assertFalse(followup_needed(self.store, self.original, admitted['receipt'], 1)['continue'])

    def test_completed_day_leaves_translation_queue_but_keeps_immutable_publication_work(self):
        admitted, _ = self.admit(1, '2026-09-30'); _, source, directory, _, _ = self.build_candidate()
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertTrue(completed_day_is_durable(self.store, {'day': '2026-09-30', 'receipt': admitted['receipt']}))
        queue = read_ready_queue(self.store)
        self.assertEqual(queue, [{'day': '2026-09-30', 'generation': source['generation'], 'candidate_id': saved['candidate_id']}])
        candidate_keys = {key for key in self.client.objects if '/candidates/' in key}
        self.admit(1, DAY)
        from portal_english_pipeline import read_queue
        self.assertEqual([row['day'] for row in read_queue(self.store)], [DAY])
        self.assertEqual(read_ready_queue(self.store), queue)
        self.assertTrue(candidate_keys <= set(self.client.objects))
        restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], self.root/'old-ready-restore')

    def test_fake_completed_day_cannot_be_pruned_without_a_real_durable_ready_candidate(self):
        admitted, _ = self.admit(1, '2026-09-30'); _, source, directory, _, _ = self.build_candidate()
        persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.store._put(self.store.key('pending-publications', 'queue.json'),
                        stable_bytes({'schema_version': 1, 'policy': POLICY, 'entries': []}), metadata={'kind': 'synthetic-test'})
        with self.assertRaises(ExpansionError): self.admit(1, DAY)
        from portal_english_pipeline import read_queue
        self.assertEqual([row['day'] for row in read_queue(self.store)], ['2026-09-30'])

    def test_ready_queue_permission_failure_cannot_mark_translation_complete(self):
        self.admit(); _, source, directory, _, _ = self.build_candidate()
        original_put = self.store._put
        def fail_publication_queue(key, body, **kwargs):
            if key.endswith('/pending-publications/queue.json'): raise R2PermissionError('forbidden')
            return original_put(key, body, **kwargs)
        with mock.patch.object(self.store, '_put', side_effect=fail_publication_queue):
            with self.assertRaises(R2PermissionError): persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertEqual(read_completed(self.store, DAY), {})
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertTrue(saved['ready']); self.assertEqual(len(read_ready_queue(self.store)), 1)
        persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertEqual(len(read_ready_queue(self.store)), 1)

    def test_no_durable_page_progress_cannot_make_an_infinite_auto_retry(self):
        admitted, _ = self.admit(25)
        self.assertFalse(followup_needed(self.store, self.original, admitted['receipt'], 25)['continue'])
        for before in (0, -1, True):
            with self.assertRaises(ExpansionError): followup_needed(self.store, self.original, admitted['receipt'], before)

    def test_timeout_saves_checkpoint_but_incomplete_candidate_never_gets_ready_or_completion(self):
        self.admit(); prepared = prepare_queued(self.store, self.original)
        _, _, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        fake = SyntheticTranslator(); fake.translate = mock.Mock(side_effect=TranslationBudgetExceeded('budget'))
        directory, checkpoint = self.root/'incomplete', self.root/'memo.json'
        result = build(source, directory, checkpoint, fake)
        self.assertTrue(result['budget_exhausted'])
        written = remember_checkpoint(self.store, source['generation'], checkpoint)
        restored = restore_seed(self.store, self.root/'seed.json')
        self.assertEqual(written['sha256'], restored['sha256']); self.assertEqual(json.loads((self.root/'seed.json').read_text())['rows'], {})
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertFalse(saved['ready']); self.assertEqual(read_completed(self.store, DAY), {})
        with self.assertRaises(R2NotFound): restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], self.root/'bad-restore')

    def test_permission_failure_and_corrupt_checkpoint_fail_without_resetting_or_spending(self):
        self.admit(); _, source, directory, checkpoint, _ = self.build_candidate()
        written = remember_checkpoint(self.store, source['generation'], checkpoint)
        self.client.deny = True
        with self.assertRaises(R2PermissionError): persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        with self.assertRaises(R2PermissionError): restore_seed(self.store, self.root/'seed.json')
        self.client.deny = False
        obj = self.client.objects[written['object_key']]; obj['body'] = b'x'+obj['body'][1:]
        with self.assertRaises(R2IntegrityError): restore_seed(self.store, self.root/'seed.json')

    def test_seed_restores_immutable_snapshot_not_a_changed_generation_pointer(self):
        self.admit(); _, source, _, checkpoint, _ = self.build_candidate()
        written = remember_checkpoint(self.store, source['generation'], checkpoint)
        original = checkpoint.read_bytes()
        value = json.loads(original); value['rows'] = {}
        checkpoint.write_bytes(stable_bytes(value))
        self.store.put_checkpoint('en', source['generation'], checkpoint)
        recovered = restore_seed(self.store, self.root/'seed.json')
        self.assertEqual(recovered['sha256'], written['sha256'])
        self.assertEqual((self.root/'seed.json').read_bytes(), original)

    def test_staging_probe_stores_only_synthetic_source_empty_memo_and_incomplete_candidate(self):
        proof = staging_probe(self.store)
        self.assertTrue(proof['staging_only']); self.assertFalse(proof['deployed'])
        self.assertEqual(proof['ready_candidates'], 0); self.assertEqual(proof['translation_calls'], 0)
        self.assertEqual(proof['english_timeout_cursor_restore'], 'passed')
        self.assertEqual(proof['incomplete_candidate_not_publishable'], 'passed')
        self.assertFalse(any(key.endswith('candidate-ready.json') for key in self.client.objects))
        self.assertTrue(all(key.startswith(self.store.prefix+'/') for key in self.client.objects))
        with self.assertRaises(Exception): staging_probe(R2Store(self.client, 'private', PREFIX))

    def test_production_cli_requires_reviewed_main_public_actions_before_storage_access(self):
        for environment in [{}, {'GITHUB_ACTIONS': 'true', 'KC_PUBLIC_REPOSITORY': 'true', 'GITHUB_REF': 'refs/heads/feature'},
                            {'GITHUB_ACTIONS': 'true', 'KC_PUBLIC_REPOSITORY': 'false', 'GITHUB_REF': 'refs/heads/main'}]:
            with self.subTest(environment=environment), mock.patch.dict('os.environ', environment, clear=True), \
                 mock.patch('sys.argv', ['pipeline', 'prepare']), mock.patch.object(R2Store, 'from_env') as connect:
                with self.assertRaises(ExpansionError): main()
                connect.assert_not_called()
        reviewed = {'GITHUB_ACTIONS': 'true', 'KC_PUBLIC_REPOSITORY': 'true', 'GITHUB_REF': 'refs/heads/main'}
        with mock.patch.dict('os.environ', reviewed, clear=True), \
             mock.patch('sys.argv', ['pipeline', 'prepare', '--prefix', self.store.prefix]), \
             mock.patch.object(R2Store, 'from_env') as connect:
            with self.assertRaises(ExpansionError): main()
            connect.assert_not_called()

    def test_staging_cli_rejects_production_prefix_before_storage_access(self):
        environment = {'GITHUB_ACTIONS': 'true', 'KC_PUBLIC_REPOSITORY': 'true', 'GITHUB_REF': 'refs/heads/feature'}
        with mock.patch.dict('os.environ', environment, clear=True), mock.patch('sys.argv', ['pipeline', 'staging-probe']), \
             mock.patch.object(R2Store, 'from_env') as connect:
            with self.assertRaises(Exception): main()
            connect.assert_not_called()

    def test_original_body_extra_file_or_fake_complete_status_cannot_be_persisted(self):
        self.admit(); _, source, directory, _, manifest = self.build_candidate()
        extra = directory/'public/en/original.html'; extra.write_text('SECRET ORIGINAL')
        with self.assertRaises(ExpansionError): persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        extra.unlink()
        target = directory/'candidate-manifest.json'
        fake = {**manifest, 'budget_exhausted': True}; target.write_bytes(stable_bytes(fake))
        with self.assertRaises(ExpansionError): persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertFalse(any(key.endswith('candidate-ready.json') for key in self.client.objects))

    def test_full_commentary_cannot_be_hidden_in_public_preview_candidate(self):
        self.admit(); _, source, directory, _, _ = self.build_candidate()
        target = next((directory/'public/en/blog').glob('*.html'))
        target.write_bytes(target.read_bytes().replace(b'</main>', b'<div hidden>SECRET FULL COMMENTARY</div></main>'))
        with self.assertRaises(ExpansionError): persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        self.assertEqual(read_completed(self.store, DAY), {})

    def test_ready_and_body_checksum_tampering_never_restores_a_candidate(self):
        self.admit(); _, source, directory, _, _ = self.build_candidate()
        saved = persist_candidate(self.store, self.original, source, directory, CPU_PRODUCER)
        base = self.store.key('candidates', source['generation'], saved['candidate_id'])
        ready = self.client.objects[base+'/candidate-ready.json']
        original = ready['body']; value = json.loads(original); value['generation'] = 'f'*64
        ready['body'] = stable_bytes(value); ready['ContentLength'] = len(ready['body']); ready['Metadata']['sha256'] = digest(ready['body'])
        with self.assertRaises(ExpansionError): restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], self.root/'tampered')
        ready['body'] = original; ready['ContentLength'] = len(original); ready['Metadata']['sha256'] = digest(original)
        body_key = next(key for key in self.client.objects if key.startswith(base+'/private/bodies/'))
        self.client.objects[body_key]['body'] = b'x'+self.client.objects[body_key]['body'][1:]
        with self.assertRaises(R2IntegrityError): restore_candidate(self.store, self.original, source['generation'], saved['candidate_id'], self.root/'corrupt')

    def test_candidate_producer_is_the_cpu_workflow_not_capture_or_arbitrary_code(self):
        self.admit(); _, source, directory, _, _ = self.build_candidate()
        for producer in [SOURCE_PRODUCER, {**CPU_PRODUCER, 'sha': 'invalid'}, {**CPU_PRODUCER, 'original': 'SECRET'}]:
            with self.assertRaises(ExpansionError): persist_candidate(self.store, self.original, source, directory, producer)

    def test_current_source_inventory_cannot_be_replaced_by_a_noninventory_subset(self):
        self.admit(); prepared = prepare_queued(self.store, self.original)
        proof, _, source = batch_admission(self.store, self.original, prepared['job']['generation'])
        broken = copy.deepcopy(source['documents'][0]); broken['title'] += '篡改'
        broken['editorial_sha256'] = digest(stable_bytes({k:v for k,v in broken.items() if k != 'editorial_sha256'}))
        subset = make_source([broken], DAY); put_source(self.store, subset)
        key = self.store.key('batch-admissions', subset['generation'], 'receipt.json')
        raw = stable_bytes({**proof, 'generation': subset['generation']})
        self.store._put(key, raw, metadata={'kind': 'synthetic-invalid-subset'})
        with self.assertRaises(ExpansionError): batch_admission(self.store, self.original, subset['generation'])


if __name__ == '__main__': unittest.main()
