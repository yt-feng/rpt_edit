"""Offline complete legacy source, alias, archive and producer admission tests."""
import copy
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import textwrap
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import recover_legacy_market_views_sources as source
import seed_legacy_market_views_cache as legacy
import test_seed_legacy_market_views_cache as seed_fixture
from test_consume_legacy_mineru import fake_asset_writer


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.fixture = seed_fixture.LegacyTests(methodName='test_whole_original_artifact_jobs_checkout_and_acceptance_are_verified')
        self.fixture.setUp(); self.addCleanup(self.fixture.doCleanups)
        patcher = patch.object(legacy, 'ORIGINAL_CODE', self.fixture.hashes)
        patcher.start(); self.addCleanup(patcher.stop)
        self.authority, self.manifest, _ = self.fixture.authenticate()
        self.fixture.seed(self.authority, self.manifest, maximum=0)
        self.fixture.gets.clear()
        self.results, self.counts, self.private = legacy.complete_results(self.authority,
            {slot: 'PRIVATE-TOKEN' for slot in legacy.inspect.SLOTS}, getter=self.fixture.getter)
        self.context = source.source_context('77777', 'c' * 40, self.fixture.run, self.fixture.sha, '261001')
        self.destination = self.fixture.root / 'sources'

    def recover(self):
        with patch('socket.create_connection', side_effect=AssertionError('No network')), \
                patch.object(legacy, 'PinnedResultTransport', side_effect=AssertionError('No result downloads')):
            return source.materialize(self.authority, self.manifest, self.manifest.parent, self.results,
                self.private, self.fixture.cache, self.destination, self.context, asset_writer=fake_asset_writer)

    def rewrite(self, change, *, files=False):
        path = self.destination / source.RECEIPT
        receipt = json.loads(path.read_text()); change(receipt)
        if files: receipt['files'] = source.file_inventory(self.destination)
        path.write_bytes(legacy.canonical(receipt))

    def test_all_sources_are_read_from_cache_with_full_receipt_and_no_result_or_api_write(self):
        puts = len(self.fixture.r2.puts)
        receipt = self.recover()
        self.assertEqual(len(self.fixture.r2.puts), puts)
        self.assertEqual(receipt['report_count'], 6)
        self.assertEqual(len(receipt['reports']), 6)
        self.assertEqual(len(receipt['terminal_tasks']), 8)
        self.assertFalse(receipt['canonical_task_admission']); self.assertFalse(receipt['original_provider_bytes_proven'])
        self.assertEqual(source.validate_sources(self.destination, 6, '261001', expected_producer_run_id='77777',
                         expected_execution_sha='c' * 40), receipt)
        self.assertEqual(len(list(self.destination.glob('report_*/source_mineru.md'))), 6)
        self.assertFalse(list(self.destination.rglob('*.zip'))); self.assertFalse(list(self.destination.rglob('*.pdf')))

    def test_complete_alias_inventory_survives_real_renderer_dedup(self):
        first, duplicate = self.fixture.names[0], self.fixture.names[1]
        original = next(row for row in self.authority['original_inventory'] if row['source_pdf'] == first)
        second = next(row for row in self.authority['original_inventory'] if row['source_pdf'] == duplicate)
        payload = (self.manifest.parent / first).read_bytes()
        (self.manifest.parent / duplicate).write_bytes(payload)
        second['content_sha256'] = original['content_sha256']
        self.authority['original_sizes'][duplicate] = len(payload)
        rows = json.loads(self.manifest.read_bytes())
        next(row for row in rows if row['process_local_path'] == duplicate)['content_sha256'] = original['content_sha256']
        self.manifest.write_bytes(legacy.canonical(rows)); self.authority['manifest_sha256'] = legacy.digest(self.manifest.read_bytes())
        self.authority['authority_sha256'] = legacy.digest(legacy.canonical({key: value for key, value in self.authority.items() if key != 'authority_sha256'}))
        self.fixture.gets.clear(); self.fixture.seed(self.authority, self.manifest, maximum=0)
        self.fixture.gets.clear()
        self.results, _, self.private = legacy.complete_results(self.authority,
            {slot: 'PRIVATE-TOKEN' for slot in legacy.inspect.SLOTS}, getter=self.fixture.getter)
        receipt = self.recover()
        self.assertEqual(receipt['report_count'], 6); self.assertEqual(receipt['unique_content_count'], 5)
        import build_market_views_pdf as renderer
        directories = [self.destination / row['directory'] for row in receipt['reports']]
        unique, aliases = renderer.unique_original_report_dirs(directories)
        self.assertEqual(len(unique), 5); self.assertEqual(sum(map(len, aliases.values())), 1)
        self.assertEqual(next(iter(aliases.values()))[0]['source_pdf'], duplicate)
        # Neither aliases nor an ordinary unique source may be omitted before
        # the complete receipt gate, even when the subset itself has no alias.
        for subset in (directories[::2], directories[1:]):
            with self.assertRaises(RuntimeError): renderer.unique_original_report_dirs(subset)

    def test_source_subset_and_missing_cache_never_create_partial_handoff(self):
        with self.assertRaisesRegex(source.LegacySourceError, 'source_incomplete'):
            source.materialize(self.authority, self.manifest, self.manifest.parent, self.results[:-1], self.private,
                self.fixture.cache, self.destination, self.context, asset_writer=fake_asset_writer)
        self.assertFalse(self.destination.exists())
        with patch.object(self.fixture.cache, 'get', side_effect=[self.fixture.payload, None]), self.assertRaises(ValueError):
            self.recover()
        self.assertFalse(self.destination.exists())
        self.assertFalse(list(self.destination.parent.glob('.legacy-market-source-*')))

    def test_modified_text_extra_file_symlink_and_receipt_hashes_are_rejected(self):
        receipt = self.recover()
        text = self.destination / receipt['reports'][0]['directory'] / 'source_mineru.md'
        original = text.read_bytes(); text.write_bytes(b'changed')
        with self.assertRaises(ValueError): source.validate_sources(self.destination, 6, '261001')
        text.write_bytes(original)
        extra = self.destination / 'unexpected.txt'; extra.write_bytes(b'private')
        with self.assertRaises(ValueError): source.validate_sources(self.destination, 6, '261001')
        extra.unlink()
        link = self.destination / 'alias-link'; link.symlink_to(text)
        with self.assertRaises(ValueError): source.validate_sources(self.destination, 6, '261001')

    def test_producer_date_count_and_sha_are_exact(self):
        self.recover()
        for count, date, run, sha in ((5, '261001', '77777', 'c'*40), (6, '261002', '77777', 'c'*40),
                                    (6, '261001', '88888', 'c'*40), (6, '261001', '77777', 'd'*40)):
            with self.subTest(count=count, date=date), self.assertRaises(ValueError):
                source.validate_sources(self.destination, count, date, expected_producer_run_id=run, expected_execution_sha=sha)

    def test_terminal_proof_cannot_omit_retry_or_accept_pending_or_union(self):
        receipt = self.recover(); original = legacy.canonical(receipt)
        cases = [lambda r: r['terminal_tasks'].pop(),
                 lambda r: r['terminal_tasks'][0]['members'][0].update(state='pending'),
                 lambda r: r['terminal_tasks'][0]['members'].pop(),
                 lambda r: r['terminal_tasks'][0]['members'][0].update(state='failed'),
                 lambda r: r['reports'][0]['binding'].update(data_id=r['reports'][0]['content_sha256'])]
        for change in cases:
            self.rewrite(change)
            with self.assertRaises(ValueError): source.validate_sources(self.destination, 6, '261001')
            (self.destination / source.RECEIPT).write_bytes(original)

    def test_recomputed_authority_hash_cannot_shrink_or_regroup_original_inventory(self):
        receipt = self.recover(); original = legacy.canonical(receipt)
        for change in (lambda a: a['groups'].pop(), lambda a: a['groups'][0]['members'].pop(),
                       lambda a: a['groups'][0].update(shard=2), lambda a: a['groups'][0]['batches'][0].update(job_id='99999')):
            def mutate(value):
                authority = value['original_authority']; change(authority)
                authority['authority_sha256'] = legacy.digest(legacy.canonical({key: item for key, item in authority.items() if key != 'authority_sha256'}))
            self.rewrite(mutate)
            with self.assertRaises(ValueError): source.validate_sources(self.destination, 6, '261001')
            (self.destination / source.RECEIPT).write_bytes(original)

    def test_status_task_and_images_still_require_consistent_complete_binding(self):
        receipt = self.recover()
        status_path = self.destination / receipt['reports'][0]['directory'] / 'status.json'
        original_status = status_path.read_bytes(); original_receipt = legacy.canonical(receipt)
        for change in (lambda s: s['mineru_legacy'].update(batch_id='00000000-0000-4000-8000-000000000008'),
                       lambda s: s.update(canonical_task_admission=True), lambda s: s.update(images=['assets/missing.png']),
                       lambda s: s.update(duplicate_of=receipt['reports'][1]['directory'])):
            status = json.loads(original_status); change(status); status_path.write_bytes(legacy.canonical(status))
            self.rewrite(lambda _: None, files=True)
            with self.assertRaises(ValueError): source.validate_sources(self.destination, 6, '261001')
            status_path.write_bytes(original_status); (self.destination / source.RECEIPT).write_bytes(original_receipt)

    def test_default_writer_receives_each_authenticated_frozen_original(self):
        calls = []
        def create(raw_dir, assets_dir, maximum, **kwargs):
            calls.append(kwargs)
            return fake_asset_writer(raw_dir, assets_dir, maximum)
        with patch('pdf_to_xhs_batch.create_chart_source_assets', side_effect=create):
            source.materialize(self.authority, self.manifest, self.manifest.parent, self.results,
                self.private, self.fixture.cache, self.destination, self.context)
        self.assertEqual(len(calls), 6)
        for original, call in zip(self.authority['original_inventory'], calls):
            self.assertEqual(call['auth_original_pdf'], self.manifest.parent / original['source_pdf'])
            self.assertEqual(call['original_pdf_sha256'], original['content_sha256'])
            self.assertEqual(source.digest(call['auth_original_pdf'].read_bytes()), original['content_sha256'])
            self.assertRegex(call['markdown_sha256'], r'^[a-f0-9]{64}$')
        source.validate_sources(self.destination, 6, '261001')

    def test_rehashed_invalid_figure_sidecar_is_rejected(self):
        receipt = self.recover()
        directory = self.destination / receipt['reports'][0]['directory']
        (directory / 'source_figure_map.json').write_bytes(b'[]')
        self.rewrite(lambda _: None, files=True)
        with self.assertRaisesRegex(source.LegacySourceError, 'source_images'):
            source.validate_sources(self.destination, 6, '261001')

    def test_declared_figure_sidecar_cannot_disappear_or_be_null(self):
        receipt = self.recover()
        path = self.destination / receipt['reports'][0]['directory'] / 'status.json'
        status = json.loads(path.read_bytes())
        for name, sha in [('source_figure_map.json', 'a' * 64), (None, None)]:
            status.update(source_figure_map=name, source_figure_map_sha256=sha)
            path.write_bytes(legacy.canonical(status)); self.rewrite(lambda _: None, files=True)
            with self.subTest(name=name), self.assertRaisesRegex(source.LegacySourceError, 'source_images'):
                source.validate_sources(self.destination, 6, '261001')

    def test_real_private_handoff_archive_roundtrip_retains_the_complete_receipt(self):
        self.recover()
        import private_workflow_handoff as handoff
        archive = self.fixture.root / 'sources.tar.gz'
        handoff.create_archive(self.destination, archive)
        restored = self.fixture.root / 'restored'
        handoff.extract_archive(archive, restored)
        receipt = source.validate_sources(restored, 6, '261001', expected_producer_run_id='77777', expected_execution_sha='c'*40)
        self.assertEqual(receipt['report_count'], 6)

    def test_unknown_private_cli_failure_is_not_reflected(self):
        output = io.StringIO()
        with patch.object(source, 'validate_sources', side_effect=ValueError('PRIVATE-TOKEN report https://private.invalid')), redirect_stdout(output):
            code = source.main(['validate', '--output-dir', str(self.destination), '--date-folder', '261001', '--expected-reports', '6'])
        self.assertEqual(code, 2); self.assertNotIn('PRIVATE', output.getvalue())
        self.assertEqual(json.loads(output.getvalue())['category'], 'source_failed')

    def test_real_pdf_workflow_step_accepts_exact_receipt_and_blocks_failed_readback_before_validation(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / '.github/workflows/market-views-latex-pdf.yml').read_text()
        block = workflow.split('- name: Verify complete accepted legacy Daily source receipt', 1)[1].split('\n      - name:', 1)[0]
        code = textwrap.dedent(block.split("python - <<'PY'\n", 1)[1].rsplit('\n          PY', 1)[0])
        self.destination = self.fixture.root / 'xhs_notes/dropbox/261001/shard_0'
        self.recover()
        import market_views_source_readiness as readiness
        _, names = readiness.SOURCE_GATES[source.WORKFLOW]
        producer = {'id': 77777, 'path': source.WORKFLOW, 'event': 'workflow_dispatch', 'head_branch': 'main',
                    'head_sha': 'c' * 40, 'status': 'in_progress', 'repository': {'full_name': self.fixture.repository},
                    'head_repository': {'full_name': self.fixture.repository}}
        jobs = {'total_count': 1, 'jobs': [{'id': 981, 'run_id': 77777, 'head_sha': 'c' * 40, 'name': 'recover',
                'status': 'in_progress', 'steps': [{'number': index, 'name': name, 'status': 'completed', 'conclusion': 'success'}
                for index, name in enumerate(names, 5)]}]}
        def run(args, **kwargs):
            endpoint = args[-1]
            if endpoint.endswith('actions/runs/77777'): value = producer
            elif endpoint.endswith('actions/runs/77777/jobs?filter=latest&per_page=100'): value = jobs
            elif endpoint.endswith('actions/runs/' + self.fixture.run): value = self.fixture.run_meta
            else: raise AssertionError(endpoint)
            return SimpleNamespace(returncode=0, stdout=json.dumps(value))
        env = {'GITHUB_REPOSITORY': self.fixture.repository, 'SOURCE_HANDOFF_RUN_ID': '77777',
               'EXPECTED_BANK_DATE': '261001', 'EXPECTED_ARTICLES': '6'}
        previous = Path.cwd()
        try:
            os.chdir(self.fixture.root)
            with patch.dict(os.environ, env), patch('subprocess.run', side_effect=run), redirect_stdout(io.StringIO()):
                exec(compile(code, '<actual-legacy-consumer-workflow>', 'exec'), {})
            jobs['jobs'][0]['steps'][-1]['conclusion'] = 'failure'
            with patch.dict(os.environ, env), patch('subprocess.run', side_effect=run), \
                    patch.object(source, 'validate_sources', side_effect=AssertionError('Must reject failed readback first')), \
                    self.assertRaises(readiness.SourceReadinessError):
                exec(compile(code, '<actual-legacy-consumer-workflow>', 'exec'), {})
        finally:
            os.chdir(previous)


class WorkflowTests(unittest.TestCase):
    def test_explicit_main_manual_legacy_receipt_gates_precede_generation(self):
        root = Path(__file__).resolve().parents[1]
        producer = (root / '.github/workflows/market-views-legacy-recovery.yml').read_text()
        consumer = (root / '.github/workflows/market-views-latex-pdf.yml').read_text()
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", producer)
        self.assertIn('source_handoff_kind=legacy-daily', producer)
        self.assertNotIn('delete-prefix', producer)
        self.assertNotIn('PinnedResultTransport', producer)
        self.assertIn('--expected-producer-run-id "$GITHUB_RUN_ID" --expected-execution-sha "$GITHUB_SHA"', producer)
        start = consumer.index('- name: Verify complete accepted legacy Daily source receipt')
        end = consumer.index('- name: Resolve and validate primary bank source')
        block = consumer[start:end]
        self.assertLess(block.index('require_source_readiness(producer, jobs)'), block.index('receipt = validate_sources('))
        self.assertIn("producer.get('event') != 'workflow_dispatch'", block)
        self.assertIn("original_sha != receipt['source_context']['original_execution_sha']", block)
        self.assertLess(end, consumer.index('- name: Build market views data and LaTeX source'))
        self.assertIn('PRIVATE_LEGACY_SOURCES_ROOT', consumer)
        self.assertIn('options: [xhs, native-pdf, mineru-recovery, legacy-daily]', consumer)


if __name__ == '__main__':
    unittest.main()
