"""Validate recovered chart input without indexing or exposing report contents."""
import copy
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch

import chart_recovered_handoff as handoff


WORKFLOW = Path(__file__).resolve().parents[1] / '.github/workflows/portal-chart-search-index.yml'
DAILY_WORKFLOW = WORKFLOW.with_name('dropbox-latest-pdf-to-xhs-sharded.yml')


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

    def test_daily_dispatch_inputs_pass_actual_chart_source_validation(self):
        daily = DAILY_WORKFLOW.read_text()
        step = re.split(r'(?m)^  [\w-]+:[ \t]*$',
                        daily.split('      - name: Dispatch daily incremental chart index\n', 1)[1], maxsplit=1)[0]
        dispatch_program = textwrap.dedent(step.split('        run: |\n', 1)[1])
        count_variable = re.search(r'^\s+(\w+): \$\{\{ needs\.select-macro-reports\.outputs\.selected_count \}\}$',
                                   step, flags=re.MULTILINE).group(1)
        chart_step = WORKFLOW.read_text().split('      - name: Validate source selection\n', 1)[1].split('      - name:', 1)[0]
        validation_program = textwrap.dedent(chart_step.split('        run: |\n', 1)[1])
        with tempfile.TemporaryDirectory() as temp:
            fake_gh = Path(temp) / 'gh'
            fake_gh.write_text(
                '#!' + sys.executable + '\n'
                'import json, os, sys\n'
                'with open(os.environ["GH_CALLS"], "a") as stream:\n'
                '    stream.write(json.dumps(sys.argv[1:]) + "\\n")\n'
                'if sys.argv[1:3] == ["workflow", "run"]:\n'
                '    print("https://github.com/example/reports/actions/runs/456")\n'
            )
            fake_gh.chmod(0o755)
            calls_path = Path(temp) / 'calls.jsonl'
            base = {**os.environ, 'PATH': temp + os.pathsep + os.environ['PATH'],
                    'GH_CALLS': str(calls_path), 'GITHUB_REPOSITORY': 'example/reports',
                    'DATE_FOLDER': '261009', 'SOURCE_RUN_ID': '123', 'EXPECTED_SHARDS': '16',
                    'MAX_IMAGES': '0', count_variable: '79'}
            for recovered in (False, True):
                with self.subTest(recovered=recovered):
                    calls_path.unlink(missing_ok=True)
                    manifest = 'a' * 64 if recovered else ''
                    result = subprocess.run(['bash', '-c', dispatch_program],
                                            env={**base, 'RECOVERED_RESULT': 'success' if recovered else 'skipped',
                                                 'RECOVERED_MANIFEST': manifest}, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    calls = [json.loads(line) for line in calls_path.read_text().splitlines()]
                    self.assertEqual(len(calls), 2)
                    self.assertEqual(calls[0][:3], ['workflow', 'run', 'portal-chart-search-index.yml'])
                    self.assertEqual(calls[1][:3], ['run', 'watch', '456'])
                    inputs = dict(calls[0][i + 1].split('=', 1)
                                  for i, item in enumerate(calls[0]) if item == '-f')
                    self.assertEqual(inputs['expected_shards'], '1' if recovered else '16')
                    self.assertEqual(inputs['expected_articles'], '79' if recovered else '0')
                    self.assertEqual(inputs['source_handoff_manifest_sha256'], manifest)
                    selected = {**os.environ, 'DATE_FOLDER': inputs['date_folder'],
                                'HANDOFF_RUN_ID': inputs['source_handoff_run_id'], 'ARTIFACT_RUN_ID': '',
                                'HANDOFF_MANIFEST_SHA256': inputs['source_handoff_manifest_sha256'],
                                'EXPECTED_SHARDS': inputs['expected_shards'],
                                'EXPECTED_ARTICLES': inputs['expected_articles'],
                                'MAX_IMAGES': inputs['max_images'], 'RETRY_ERRORS_NOW': 'false'}
                    validation = subprocess.run(['bash', '-c', validation_program], env=selected,
                                                capture_output=True, text=True)
                    self.assertEqual(validation.returncode, 0, validation.stderr)
                    # Keep the receiver strict: neither normal input with a recovered
                    # count nor a recovered manifest without its count is admissible.
                    invalid = subprocess.run(['bash', '-c', validation_program],
                                             env={**selected, 'EXPECTED_ARTICLES': '0' if recovered else '79'},
                                             capture_output=True, text=True)
                    self.assertNotEqual(invalid.returncode, 0)

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

    def test_actual_sparse_checkout_runs_real_recovered_chart_contract(self):
        checkout_step = WORKFLOW.read_text().split('      - name: Checkout public source\n', 1)[1].split('      - uses:', 1)[0]
        patterns = textwrap.dedent(checkout_step.split('          sparse-checkout: |\n', 1)[1]).strip()
        root = WORKFLOW.parents[2]
        with tempfile.TemporaryDirectory() as temp:
            checkout = Path(temp) / 'checkout'
            checkout.mkdir()

            def git(*args, **kwargs):
                result = subprocess.run(['git', '-C', str(checkout), *args],
                                        capture_output=True, text=True, timeout=60, **kwargs)
                self.assertEqual(result.returncode, 0, result.stderr)

            # Actions can expose a partial/promisor repository whose other blobs
            # are unavailable offline. Build a small independent Git fixture from
            # the actual checked-out dependencies; never clone its object store.
            shutil.copytree(root / 'scripts', checkout / 'scripts',
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            for relative in (WORKFLOW.relative_to(root), DAILY_WORKFLOW.relative_to(root),
                             Path('prompts/wechat_report_article_prompt.md')):
                target = checkout / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(root / relative, target)
            git('init', '--quiet')
            git('add', '--all')
            git('-c', 'user.name=Chart fixture', '-c', 'user.email=chart-fixture@example.invalid',
                '-c', 'commit.gpgsign=false', 'commit', '--quiet', '-m', 'Checked-out chart dependencies')
            # Applying the real workflow patterns still catches a missing prompt
            # declaration even when the developer checkout contains that file.
            git('sparse-checkout', 'set', '--no-cone', '--stdin', input=patterns + '\n')
            git('checkout', '--detach', '--quiet', 'HEAD')
            fixture_test = Path(__file__).relative_to(root)
            self.assertTrue((checkout / fixture_test).is_file())
            selected = [
                'RecoveredChartTests.test_real_complete_source_receipt_and_images_survive_materialization',
                'RecoveredChartTests.test_real_receipt_wrong_manifest_run_date_or_missing_receipt_are_rejected',
            ]
            result = subprocess.run([sys.executable, str(fixture_test), *selected], cwd=checkout,
                                    capture_output=True, text=True, timeout=90)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            # The fixture must still bind the actual prompt; a missing checkout
            # input must never pass through a mocked or synthetic replacement.
            (checkout / 'prompts/wechat_report_article_prompt.md').unlink()
            missing = subprocess.run([sys.executable, str(fixture_test), selected[0]], cwd=checkout,
                                     capture_output=True, text=True, timeout=90)
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn('FileNotFoundError', missing.stderr)
            self.assertIn('wechat_report_article_prompt.md', missing.stderr)

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
