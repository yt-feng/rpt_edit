"""Validate recovered chart input without indexing or exposing report contents."""
import copy
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from unittest.mock import patch

import chart_recovered_handoff as handoff


WORKFLOW = Path(__file__).resolve().parents[1] / '.github/workflows/portal-chart-search-index.yml'


class RecoveredChartTests(unittest.TestCase):
    def env(self):
        return {'DATE_FOLDER': '261003', 'HANDOFF_RUN_ID': '123', 'ARTIFACT_RUN_ID': '',
                'HANDOFF_MANIFEST_SHA256': 'a' * 64, 'EXPECTED_SHARDS': '1', 'EXPECTED_ARTICLES': '7'}

    def test_exact_prefix_and_rejected_ambiguous_or_injected_selections(self):
        config = handoff.selection(self.env())
        self.assertEqual(config['prefix'], '_private-workflow-handoff/xhs-recovery/123/261003/' + 'a' * 64 + '/articles')
        for key, value in [('DATE_FOLDER', '261032'), ('DATE_FOLDER', '261003/..'),
                           ('HANDOFF_RUN_ID', '123;touch /tmp/no'), ('HANDOFF_RUN_ID', ''),
                           ('HANDOFF_MANIFEST_SHA256', '../' + 'a' * 61), ('HANDOFF_MANIFEST_SHA256', 'b' * 63),
                           ('HANDOFF_MANIFEST_SHA256', '$(touch /tmp/no)'), ('ARTIFACT_RUN_ID', '456'),
                           ('EXPECTED_SHARDS', '0'), ('EXPECTED_SHARDS', '2'), ('EXPECTED_ARTICLES', '0'),
                           ('EXPECTED_ARTICLES', '1001')]:
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                handoff.selection({**self.env(), key: value})

    def test_actual_workflow_shell_rejects_substitution_without_executing_it(self):
        workflow = WORKFLOW.read_text()
        step = workflow.split('      - name: Validate source selection\n', 1)[1].split('      - name:', 1)[0]
        program = textwrap.dedent(step.split('        run: |\n', 1)[1])
        with tempfile.TemporaryDirectory() as temp:
            marker = Path(temp) / 'unexpected'
            base = {**os.environ, **self.env(), 'MAX_IMAGES': '0', 'RETRY_ERRORS_NOW': 'false'}
            self.assertEqual(subprocess.run(['bash', '-c', program], env=base, capture_output=True).returncode, 0)
            for key in ('HANDOFF_MANIFEST_SHA256', 'HANDOFF_RUN_ID', 'DATE_FOLDER', 'EXPECTED_ARTICLES'):
                with self.subTest(key=key):
                    result = subprocess.run(['bash', '-c', program], env={**base, key: '$(touch ' + str(marker) + ')'}, capture_output=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(marker.exists())

    def fixture(self):
        from test_recover_report_articles import ArticleRecoveryTests
        case = ArticleRecoveryTests()
        case.setUp()
        self.addCleanup(case.doCleanups)
        source = case.mineru(figures=True)
        with case.paid():
            case.recover(source)
        root = case.root / 'articles'
        metadata = json.loads((root / 'source_provenance.json').read_text())
        config = handoff.selection({**self.env(), 'HANDOFF_MANIFEST_SHA256': metadata['manifest_sha256']})
        return case, root, config

    def test_real_complete_source_receipt_and_images_survive_materialization(self):
        case, root, config = self.fixture()
        before = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}
        def download(key, destination):
            self.assertEqual(key, config['prefix'] + '/shard_0.tar.gz')
            shutil.copytree(root, destination)
        with patch('private_workflow_handoff.download_directory', side_effect=download), \
             patch('requests.Session.request', side_effect=AssertionError('No external calls')):
            result = handoff.materialize(case.root / 'chart', config)
        self.assertEqual(result, {'complete': True, 'reports': 7, 'source_kind': 'mineru-recovery', 'original_image_count': 7})
        copied = case.root / 'chart/261003/shard_0'
        self.assertEqual(before, {str(p.relative_to(copied)): p.read_bytes() for p in copied.rglob('*') if p.is_file()})

    def test_real_receipt_wrong_manifest_run_date_or_missing_receipt_are_rejected(self):
        _case, root, config = self.fixture()
        for key, value in [('HANDOFF_MANIFEST_SHA256', 'f' * 64), ('HANDOFF_RUN_ID', '456'), ('DATE_FOLDER', '261004')]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                handoff.validate_handoff(root, {**config, key: value})
        (root / 'article_recovery_receipt.json').unlink()
        with self.assertRaises(ValueError):
            handoff.validate_handoff(root, config)

    def test_ocr_kind_rejected_before_validation_or_candidate_indexing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'article_recovery_receipt.json').write_text(json.dumps({'source_kind': 'ocr-synthesis'}))
            with patch('recover_report_articles.validate_articles') as validate, \
                 patch('build_chart_search_index.discover_candidates') as candidates:
                with self.assertRaisesRegex(ValueError, '^unsupported_recovered_chart_source_kind$'):
                    handoff.validate_handoff(root, handoff.selection(self.env()))
            validate.assert_not_called()
            candidates.assert_not_called()

    def test_workflow_preserves_legacy_sources_and_admits_recovery_before_index(self):
        workflow = WORKFLOW.read_text()
        self.assertIn("if: inputs.source_handoff_run_id != '' && inputs.source_handoff_manifest_sha256 == ''", workflow)
        self.assertIn('--prefix "$PRIVATE_HANDOFF_ROOT/${{ inputs.source_handoff_run_id }}/${{ inputs.date_folder }}"', workflow)
        self.assertIn('"PyMuPDF>=1.24"', workflow)
        self.assertLess(workflow.index('Download and authenticate recovered article chart sources'),
                        workflow.index('Describe and index new chart hashes'))
        block = workflow.split('      - name: Download and authenticate recovered article chart sources\n', 1)[1].split('      - name:', 1)[0]
        self.assertNotIn('${{', block.split('        run:', 1)[1])
        self.assertIn('ARTIFACT_RUN_ID:', block)


if __name__ == '__main__':
    unittest.main()
