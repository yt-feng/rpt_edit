"""Execute the production selector and argument boundary without network or cache IO."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / '.github/workflows/institution-latest-pdf-to-wechat.yml').read_text()
SELECTIONS = {
    'imf-20261012-reviewed': '250557000edbc46f0629393a7a43a139b37926cb54c58535ea498866ccd77e67',
    'imf-20261015-reviewed': 'c880842e7f022145eaca780dd52017934444ab7c7f1be7208a9cc7f74b81196b',
}


def manifest_path(selection):
    return Path('institution_feeds/reviewed_originals') / (selection + '.json')


def step(name):
    return WORKFLOW.split('      - name: ' + name + '\n', 1)[1].split('\n      - name:', 1)[0]


def run_block(section):
    return textwrap.dedent(section.split('        run: |\n', 1)[1]).rstrip() + '\n'


SELECT = run_block(step('Select reviewed institution originals'))
FETCH = run_block(step('Fetch latest institution PDFs'))


class ReviewedIntakeTests(unittest.TestCase):
    def selector(self, root, *, selection='none', event='workflow_dispatch', manifest=True):
        if manifest:
            source = root / manifest_path(selection)
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_bytes((ROOT / manifest_path(selection)).read_bytes())
        (root / 'scripts').symlink_to(ROOT / 'scripts')
        binaries = root / 'bin'; binaries.mkdir()
        (binaries / 'python').symlink_to(sys.executable)
        runtime = root / 'runner temp'; runtime.mkdir()
        output = root / 'output'
        env = dict(os.environ, REVIEWED_ORIGINALS=selection, EVENT_NAME=event,
                   RUNNER_TEMP=str(runtime), GITHUB_OUTPUT=str(output),
                   PATH=str(binaries)+os.pathsep+os.environ['PATH'])
        result = subprocess.run(['bash', '-c', SELECT], cwd=root, env=env, text=True, capture_output=True, timeout=20)
        return result, output, runtime

    def test_none_does_not_read_manifest_on_schedule_or_dispatch(self):
        for event in ('schedule', 'workflow_dispatch'):
            with self.subTest(event=event), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                result, output, runtime = self.selector(root, event=event, manifest=False)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(output.read_text(), 'manifest_path=\n')
                self.assertEqual(list(runtime.iterdir()), [])
                self.assertFalse((root / 'institution_feeds').exists())

    def test_unknown_and_nonmanual_selection_fail_without_shell_execution(self):
        for selection, event in (('unknown', 'workflow_dispatch'), ('$(touch INJECTED)', 'workflow_dispatch'),
                                 ('none; touch INJECTED', 'workflow_dispatch'),
                                 *((choice, 'schedule') for choice in SELECTIONS)):
            with self.subTest(selection=selection, event=event), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                result, output, runtime = self.selector(root, selection=selection, event=event, manifest=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(output.exists())
                self.assertFalse((root / 'INJECTED').exists())
                self.assertEqual(list(runtime.iterdir()), [])
                self.assertNotIn(selection, result.stdout + result.stderr)

    def test_selected_manifest_is_immutable_validated_temp_copy(self):
        for selection, expected in SELECTIONS.items():
            with self.subTest(selection=selection), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                result, output, runtime = self.selector(root, selection=selection)
                self.assertEqual(result.returncode, 0, result.stderr)
                copied = Path(output.read_text().strip().removeprefix('manifest_path='))
                self.assertEqual(copied.parent, runtime)
                self.assertEqual(copied.read_bytes(), (ROOT / manifest_path(selection)).read_bytes())
                self.assertEqual(hashlib.sha256(copied.read_bytes()).hexdigest(), expected)
                (root / manifest_path(selection)).write_text('changed after selection')
                self.assertEqual(hashlib.sha256(copied.read_bytes()).hexdigest(), expected)
                self.assertEqual(copied.stat().st_mode & 0o777, 0o600)

    def test_missing_changed_or_symlink_manifest_is_rejected_before_fetch(self):
        for selection in SELECTIONS:
            for mode in ('missing', 'changed', 'symlink'):
                with self.subTest(selection=selection, mode=mode), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    source = root / manifest_path(selection); source.parent.mkdir(parents=True)
                    if mode == 'changed':
                        source.write_bytes((ROOT / manifest_path(selection)).read_bytes() + b'\n')
                    elif mode == 'symlink':
                        source.symlink_to(ROOT / manifest_path(selection))
                    result, output, runtime = self.selector(root, selection=selection, manifest=False)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(output.exists())
                    self.assertEqual(list(runtime.iterdir()), [])

    def test_fetch_argument_is_optional_and_never_split_or_interpolated(self):
        script = re.sub(r"\$\{\{ github\.event\.inputs\.[a-z_]+ \|\| '([^']*)' \}\}", lambda m: m[1], FETCH)
        self.assertNotIn('${{', script)
        for manifest in ('', '/synthetic runner/path with spaces/reviewed.json'):
            with self.subTest(manifest=manifest), tempfile.TemporaryDirectory() as directory:
                root = Path(directory); binaries = root / 'bin'; binaries.mkdir()
                python = binaries / 'python'
                python.write_text('#!' + sys.executable + '\nimport json, os, sys\n'
                                  'with open(os.environ["ARGUMENT_LOG"], "a") as f: f.write(json.dumps(sys.argv[1:])+"\\n")\n')
                python.chmod(0o700)
                log = root / 'arguments.jsonl'
                env = dict(os.environ, PATH=str(binaries)+os.pathsep+os.environ['PATH'], ARGUMENT_LOG=str(log),
                           GITHUB_OUTPUT=str(root/'output'), RUNNER_TEMP=str(root), IMF_PENDING_RETRIES='17',
                           REVIEWED_ORIGINALS_MANIFEST=manifest)
                result = subprocess.run(['bash', '-c', script], cwd=root, env=env, text=True, capture_output=True, timeout=20)
                self.assertEqual(result.returncode, 0, result.stderr)
                calls = [json.loads(line) for line in log.read_text().splitlines()]
                self.assertEqual(len(calls), 2)
                fetch, health = calls
                self.assertEqual(fetch[0], 'scripts/fetch_institution_latest_pdfs.py')
                self.assertEqual(fetch[fetch.index('--imf-pending-retries')+1], '17')
                if manifest:
                    self.assertEqual(fetch[fetch.index('--verified-originals-manifest')+1], manifest)
                    self.assertEqual(fetch.count('--verified-originals-manifest'), 1)
                else:
                    self.assertNotIn('--verified-originals-manifest', fetch)
                self.assertEqual(health[0], 'scripts/institution_source_health.py')
                self.assertEqual(health[health.index('--producer-exit-code')+1], '0')

    def test_production_wiring_is_default_off_post_reset_and_private_cache_only(self):
        inputs = WORKFLOW.split('      reviewed_originals:\n', 1)[1].split('      force_reprocess:', 1)[0]
        self.assertIn('type: choice\n', inputs)
        self.assertIn('default: none\n', inputs)
        self.assertEqual(re.findall(r'^          - (.+)$', inputs, re.M), ['none', *SELECTIONS])
        selection = step('Select reviewed institution originals')
        self.assertIn("REVIEWED_ORIGINALS: ${{ github.event.inputs.reviewed_originals || 'none' }}", selection)
        self.assertNotIn('${{', SELECT)
        self.assertLess(WORKFLOW.index('git reset --hard origin/main'), WORKFLOW.index('name: Select reviewed institution originals'))
        self.assertLess(WORKFLOW.index('name: Select reviewed institution originals'), WORKFLOW.index('name: Fetch latest institution PDFs'))
        fetch = step('Fetch latest institution PDFs')
        for setting in ('R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID || vars.R2_ACCOUNT_ID }}',
                        'R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}',
                        'R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}',
                        'R2_BUCKET: ${{ secrets.R2_BUCKET || vars.R2_BUCKET }}'):
            self.assertIn(setting, fetch)
        self.assertIn('REVIEWED_ORIGINALS_MANIFEST: ${{ steps.reviewed_originals.outputs.manifest_path }}', fetch)
        self.assertNotIn('continue-on-error', fetch)
        self.assertIn("needs.fetch-and-build.outputs.source_health == 'degraded'", WORKFLOW)

    def test_all_workflow_run_blocks_have_valid_bash_syntax(self):
        blocks = re.findall(r'^([ ]+)run: \|\n((?:(?:\1  .*|[ ]*)\n)*)', WORKFLOW, re.M)
        self.assertGreater(len(blocks), 20)
        for _, block in blocks:
            result = subprocess.run(['bash', '-n'], input=textwrap.dedent(block), text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
