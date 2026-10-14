#!/usr/bin/env python3
"""Exercise actual partial-source PDF generation with no model or publication."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import fitz
import publish_daily_market_views as publisher


class DailyDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        originals = self.root / 'originals'
        originals.mkdir()
        rows = []
        for index in range(4):
            name = f'{index:02d}-Market-research.pdf'
            path = originals / name
            with fitz.open() as document:
                page = document.new_page()
                page.insert_textbox(fitz.Rect(40, 40, 550, 700),
                    f'Research institution {index}\nMarket outlook and industrial demand\n\n'
                    'Market demand remains supported by a gradual recovery in household income and investment. '
                    'Interest rates are expected to remain stable while inflation moderates over the next quarter. '
                    'Industrial earnings increased by 12 percent as export orders and operating margins improved. '
                    'The report expects energy demand to grow moderately alongside the recovery in global production.', fontsize=12)
                document.save(path)
            rows.append({'process_local_path': f'_selected_macro_pdfs/{name}',
                         'content_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
        manifest = self.root / 'selected_to_process_manifest.json'
        manifest.write_text(json.dumps(rows))
        self.context = {'date_folder': '261014', 'source_run_id': '123456',
            'source_execution_sha': 'a' * 40, 'manifest_path': str(manifest),
            'selected_manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
            'originals_dir': str(originals), 'handoff_dir': str(self.root / 'handoff'),
            'available_dir': str(self.root / 'available'), 'reports_per_shard': 0,
            'unavailable_originals': []}

    def tearDown(self):
        self.temp.cleanup()

    def test_missing_source_and_disabled_model_still_render_true_coverage(self):
        with patch('upload_market_view_to_r2.upload_market_view') as upload, \
             patch.dict('os.environ', {'DEEPSEEK_API_KEY': ''}):
            result = publisher.deliver(self.context, self.root / 'run',
                acceptance_only=True, force_fallback=True)
        upload.assert_not_called()
        self.assertEqual((3, 4, 1), tuple(result[key] for key in ('included_reports', 'expected_reports', 'skipped_reports')))
        self.assertEqual(0, result['production_writes'])
        self.assertEqual(0, result['model_calls'])
        self.assertTrue(Path(result['public_pdf']).is_file())
        output = self.root / 'run' / 'rendered' / '261014'
        stats = json.loads((output / 'market_views_render_stats.json').read_text())
        self.assertLessEqual(stats['page_count'], 70)
        self.assertLessEqual(stats['module_count'], 10)
        self.assertEqual(result['pdf_sha256'], stats['pdf_sha256'])
        summary = json.loads((output / 'market_views_structured.json').read_text())
        self.assertEqual('daily-digest', summary['source_kind'])
        self.assertEqual(3, summary['delivery_coverage']['included_reports'])
        with fitz.open(result['public_pdf']) as pdf:
            self.assertGreater(len(pdf), 1)
            self.assertTrue(any('3/4' in page.get_text().replace(' ', '') for page in pdf))

    def test_manifest_mutation_refuses_source_rebinding(self):
        manifest = Path(self.context['manifest_path'])
        manifest.write_text(manifest.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'manifest_changed'):
            publisher.assemble(self.context, self.root / 'run')

    def test_acceptance_fault_cannot_be_selected_for_production(self):
        with self.assertRaisesRegex(ValueError, 'acceptance_only'):
            publisher.deliver(self.context, self.root / 'run', force_fallback=True)

    def test_unusable_source_does_not_remove_healthy_sibling(self):
        good, bad = self.root / 'good', self.root / 'bad'
        good.mkdir()
        bad.mkdir()
        (good / 'source_mineru.md').write_text('Market earnings recovered strongly as demand increased across industrial sectors and operating margins improved.')
        (bad / 'source_mineru.md').write_text('Contact us. Legal disclosure.')
        reasons = {}
        result = publisher.usable_excerpts({'good': {'directory': good}, 'bad': {'directory': bad}}, reasons)
        self.assertEqual({'good'}, set(result))
        self.assertEqual('no_substantive_source_text', reasons['bad'])


if __name__ == '__main__':
    unittest.main()
