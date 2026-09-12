#!/usr/bin/env python3
"""The real-model smoke must remain free, offline and deployment-independent."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PreflightWorkflowTests(unittest.TestCase):
    def test_public_standard_runner_has_no_credentials_or_deployment(self):
        text = (ROOT / '.github/workflows/portal-locale-translation-preflight.yml').read_text()
        self.assertIn('runs-on: ubuntu-24.04', text)
        self.assertIn('contents: read', text)
        self.assertIn('pull_request:', text)
        for forbidden in ('secrets.', 'DEEPSEEK_', 'DEEPL_', 'wrangler', 'publish_static_slot', 'contents: write'):
            self.assertNotIn(forbidden, text)
        self.assertIn('scripts/smoke_offline_translation.py', text)
        self.assertIn('if: always()', text)
        self.assertIn('retention-days: 3', text)

    def test_model_cache_never_contains_report_memo(self):
        text = (ROOT / '.github/actions/setup-offline-translation/action.yml').read_text()
        cached = text.split('Restore public model files only', 1)[1].split('Install and audit', 1)[0]
        self.assertIn('argos-packages', cached)
        self.assertNotIn('offline-translation-memo', cached)
        self.assertIn('requirements-translation.txt', text)
        self.assertIn('--audit-out', text)

    def test_production_locale_step_has_no_paid_provider_path(self):
        text = (ROOT / '.github/workflows/neutral-edge-cutover.yml').read_text()
        step = text.split('Build Korean Japanese and Arabic static locales', 1)[1].split('Detect multilingual translation checkpoint', 1)[0]
        for forbidden in ('DEEPSEEK', 'DEEPL', 'run_portal_locale_backfill.py', 'max-provider-cost-cny'):
            self.assertNotIn(forbidden, step)
        self.assertIn('--provider argos', step)
        title = text.split('- name: Translate missing report titles', 1)[1].split('- name: Detect Chinese', 1)[0]
        self.assertNotIn('DEEPSEEK', title)
        self.assertIn('--fail-on-error', title)

    def test_all_report_and_subtitle_jobs_install_models(self):
        for file in (ROOT / '.github/workflows').glob('*.yml'):
            text = file.read_text()
            if ('python scripts/build_portal_translated_reports.py' in text or
                    'python scripts/generate_test_podcast_video_eleven_batch_v5.py' in text):
                with self.subTest(workflow=file.name):
                    self.assertIn('uses: ./.github/actions/setup-offline-translation', text)


if __name__ == '__main__':
    unittest.main()
