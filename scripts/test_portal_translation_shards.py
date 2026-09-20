#!/usr/bin/env python3
"""Verify full report coverage, private checkpoint isolation and merge contracts."""
from __future__ import annotations

import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest import mock

import build_portal_translated_reports as reports
import portal_translation_shards as shards
from private_workflow_handoff import SHARD_KEY_RE


class TranslationShardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.date = self.root / 'sources' / '260919'
        self.date.mkdir(parents=True)

    def tearDown(self):
        self.temp.cleanup()

    def sources(self, count):
        for index in range(count):
            # Same report basename in different raw shards must still produce
            # different globally indexed output directories and PDF filenames.
            directory = self.date / f'shard_{index // 5}' / f'report-{index % 5}'
            directory.mkdir(parents=True)
            (directory / 'source_mineru.md').write_text(f'Public fixture {index}. Revenue was 10%.')

    def save_plan(self, plan):
        path = self.root / 'plan.json'
        shards.write_json(path, plan)
        return path

    def outputs(self, plan):
        source_root = self.root / 'outputs'
        for shard_index in range(plan['shard_count']):
            worker = source_root / f'shard_{shard_index}'
            date_root = worker / 'portal_translated_reports' / plan['date_folder']
            items = []
            for record in shards.shard_records(plan, shard_index):
                index = record['global_index']
                name = f'{index:02d}-report'
                directory = date_root / name
                directory.mkdir(parents=True)
                pdf_name = f'portal_translated_report_{index:02d}.pdf'
                (directory / pdf_name).write_bytes(b'%PDF-' + b'0' * 1100)
                (directory / 'translated.md').write_text('公开测试译文')
                (directory / 'assets').mkdir()
                image = directory / 'assets/fig_001.png'
                image.write_bytes(b'public-image-fixture')
                (directory / 'figure_manifest.json').write_text(json.dumps([
                    {'token': '[[PORTAL_IMAGE_001]]', 'relative_path': image.name, 'path': str(image)},
                ]))
                status = {'global_index': index, 'source_report_dir': str(self.date / record['relative_dir']), 'pdf': pdf_name}
                shards.write_json(directory / 'translation_status.json', status)
                items.append({**status, 'output_dir': str(directory), 'pdf_path': str(directory / pdf_name)})
            shards.write_json(date_root / f'translation_shard_{shard_index}.json', {
                'plan_sha256': plan['plan_sha256'], 'successful_count': len(items), 'reports': items, 'failures': [],
            })
            logs = worker / 'translation_shard_logs'
            logs.mkdir()
            (logs / f'shard_{shard_index}.log').write_text(f'private log {shard_index}\n')
        return source_root

    def test_78_reports_have_complete_disjoint_stable_global_coverage(self):
        self.sources(78)
        plan = shards.create_plan(self.date)
        self.assertEqual(plan['shard_count'], 16)
        loaded = shards.load_plan(self.save_plan(plan))
        indices = []
        for shard_index in range(16):
            records = shards.shard_records(loaded, shard_index)
            self.assertLessEqual(len(records), 5)
            indices.extend(index for index, _ in shards.selected_reports(loaded, shard_index, self.date))
        self.assertEqual(indices, list(range(1, 79)))
        self.assertEqual(plan, shards.create_plan(self.date))

    def test_global_limit_applies_before_partition(self):
        self.sources(12)
        plan = shards.create_plan(self.date, '7')
        self.assertEqual(plan['source_count'], 12)
        self.assertEqual(plan['selected_count'], 7)
        self.assertEqual([len(shards.shard_records(plan, index)) for index in range(2)], [5, 2])

    def test_source_change_after_plan_is_rejected(self):
        self.sources(6)
        plan = shards.create_plan(self.date)
        source = self.date / plan['reports'][0]['relative_dir'] / 'source_mineru.md'
        source.write_text('changed after plan')
        with self.assertRaisesRegex(ValueError, 'Source changed'):
            shards.selected_reports(plan, 0, self.date)

    def test_private_scopes_are_stable_across_runs_but_worker_specific(self):
        self.sources(6)
        plan = shards.create_plan(self.date)
        self.assertEqual(shards.checkpoint_scope(plan, 0), 'dropbox-p5-n2-i0')
        self.assertNotEqual(shards.checkpoint_scope(plan, 0), shards.checkpoint_scope(plan, 1))
        self.assertEqual(shards.checkpoint_scope(plan, 1), shards.checkpoint_scope(shards.create_plan(self.date), 1))

    def test_worker_downloads_only_required_raw_source_shards(self):
        self.sources(12)
        plan = shards.create_plan(self.date)
        with mock.patch('private_workflow_handoff.download_directory') as download:
            shards.materialize(plan, 1, 'private/run/date', self.date)
        self.assertEqual(download.call_count, 1)
        self.assertEqual(download.call_args.args[0], 'private/run/date/shard_1.tar.gz')

    def test_results_do_not_pollute_existing_raw_shard_inventory(self):
        self.sources(6)
        plan = shards.create_plan(self.date)
        with mock.patch('private_workflow_handoff.download_directory') as download:
            shards.download_results(plan, 'private/run/date', self.root / 'results')
        for call in download.call_args_list:
            self.assertIsNone(SHARD_KEY_RE.search(call.args[0]))

    def test_exact_merge_preserves_every_pdf_and_single_legacy_summary(self):
        self.sources(12)
        plan = shards.create_plan(self.date)
        output = self.root / 'merged'
        summary = shards.merge_shards(plan, self.outputs(plan), output)
        self.assertEqual(summary['successful_count'], 12)
        date_root = output / 'portal_translated_reports' / '260919'
        self.assertEqual(len(list(date_root.rglob('portal_translated_report_*.pdf'))), 12)
        self.assertEqual(len(list(date_root.glob('translation*.json'))), 1)
        self.assertEqual([row['global_index'] for row in summary['reports']], list(range(1, 13)))
        from push_portal_translated_to_wechat_drafts import load_figure_paths
        for item in summary['reports']:
            directory = output / item['output_dir']
            self.assertEqual(load_figure_paths(directory)['[[PORTAL_IMAGE_001]]'], directory / 'assets/fig_001.png')
        progress = (output / 'portal_translated_reports_progress.log').read_text()
        for index in range(3):
            self.assertEqual(progress.count(f'private log {index}'), 1)

    def test_missing_or_incomplete_shard_never_publishes_partial_union(self):
        self.sources(6)
        plan = shards.create_plan(self.date)
        source_root = self.outputs(plan)
        summary_path = source_root / 'shard_1/portal_translated_reports/260919/translation_shard_1.json'
        summary = json.loads(summary_path.read_text())
        summary['reports'][0]['global_index'] = 1
        summary_path.write_text(json.dumps(summary))
        output = self.root / 'merged'
        with self.assertRaisesRegex(ValueError, 'incomplete or mismatches'):
            shards.merge_shards(plan, source_root, output)
        self.assertFalse(output.exists())

    def test_builder_uses_planned_global_index_and_shard_summary(self):
        self.sources(6)
        plan_path = self.save_plan(shards.create_plan(self.date))
        output = self.root / 'rendered'
        argv = ['build', '--dropbox-output-root', str(self.date.parent), '--date-folder', '260919',
                '--output-root', str(output), '--max-reports', 'all', '--report-plan', str(plan_path),
                '--translation-shard-index', '1']
        with mock.patch('sys.argv', argv), mock.patch.object(reports, 'process_report', return_value={'global_index': 6}) as process:
            self.assertEqual(reports.main(), 0)
        self.assertEqual(process.call_args.args[2], 6)
        summary = json.loads((output / '260919/translation_shard_1.json').read_text())
        self.assertEqual(summary['successful_count'], 1)
        self.assertFalse((output / '260919/translation_summary.json').exists())

    def test_soft_deadline_exits_with_retained_completed_report_summary(self):
        self.sources(5)
        plan_path = self.save_plan(shards.create_plan(self.date))
        output = self.root / 'rendered'
        handlers = []

        def register(_signum, handler):
            handlers.append(handler)

        def process(_report, _out, index, _args):
            if index == 2:
                handlers[0](None, None)
            return {'global_index': index}

        argv = ['build', '--dropbox-output-root', str(self.date.parent), '--date-folder', '260919',
                '--output-root', str(output), '--max-reports', 'all', '--report-plan', str(plan_path),
                '--translation-shard-index', '0', '--max-seconds', '1']
        with mock.patch('sys.argv', argv), mock.patch.object(reports, 'process_report', side_effect=process), \
             mock.patch.object(reports.signal, 'signal', side_effect=register), mock.patch.object(reports.signal, 'setitimer'):
            self.assertEqual(reports.main(), 1)
        summary = json.loads((output / '260919/translation_shard_0.json').read_text())
        self.assertEqual(summary['successful_count'], 1)
        self.assertEqual(summary['failures'][0]['error'], 'translation_time_budget_exhausted')

    def test_workflow_has_bounded_workers_private_handoff_and_legacy_final_artifact(self):
        workflow = (Path(__file__).parents[1] / '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml').read_text()
        worker = re.search(r'(?ms)^  translate-report-shard:\n(.*?)(?=^  [\w-]+:\n)', workflow).group(1)
        self.assertIn('max-parallel: 8', worker)
        self.assertIn('fail-fast: false', worker)
        self.assertIn('--max-seconds 16500', worker)
        self.assertIn('--include-translated-pdfs', worker)
        self.assertIn('always() && steps.translation_checkpoint.outcome', worker)
        self.assertIn('audit-suffix: -shard-${{ matrix.translation_shard_index }}', worker)
        self.assertNotIn('name: portal-translated-reports-', worker)
        self.assertIn('name: portal-translated-reports-${{ needs.select-macro-reports.outputs.latest_folder }}-${{ github.run_id }}', workflow)


if __name__ == '__main__':
    unittest.main()
