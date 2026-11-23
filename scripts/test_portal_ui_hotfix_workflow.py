"""Deployment ordering and rollback boundaries for the bounded UI-only route."""
from pathlib import Path
import json
import os
import re
import shlex
import subprocess
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]

class Workflow(unittest.TestCase):
    def setUp(self):
        self.raw = (ROOT/'.github/workflows/portal-ui-hotfix.yml').read_text()
        self.workflow = yaml.safe_load(self.raw)
        self.steps = self.workflow['jobs']['hotfix']['steps']
    def test_ui_validation_references_existing_regression_tests(self):
        commands = next(step['run'] for step in self.steps if step.get('name') == 'Validate UI hotfix before private configuration')
        paths = [token for line in commands.splitlines() if line.strip().startswith('node --test ')
                 for token in shlex.split(line)[2:] if token.endswith('.test.mjs')]
        self.assertIn('portal_suite/tests/download-password-context.test.mjs', paths)
        self.assertIn('portal_suite/tests/report-monthly-access-frontend.test.mjs', paths)
        for path in paths:
            self.assertTrue((ROOT / path).is_file(), path)
    def test_prod_lock_main_origin_guards_and_no_content_generation(self):
        self.assertEqual(self.workflow['concurrency'], {'group': 'portal-production-release', 'cancel-in-progress': False, 'queue': 'max'})
        commands = '\n'.join(step.get('run','') for step in self.steps)
        self.assertIn('"$GITHUB_REF" != "refs/heads/main"', commands)
        self.assertIn('release != os.environ["EXPECTED_RELEASE"]', commands)
        self.assertNotRegex(commands, r'build_portal_locales|--approved-ledger|--enable-pdf-cleanup|delete_objects.*active')
        for step in self.steps:
            if 'run' not in step: continue
            result = subprocess.run(['bash', '-n'], input=step['run'], text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
    def test_verify_then_capture_recheck_deploy_accept_and_exact_rollback(self):
        names = [step.get('name','') for step in self.steps]
        prepare = names.index('Prepare verified inactive UI candidate from the active release')
        capture = names.index('Capture exact edge rollback target')
        guard = names.index('Recheck the active release immediately before deployment')
        deploy = next(i for i, step in enumerate(self.steps) if step.get('id') == 'edge_deploy')
        accept = next(i for i, step in enumerate(self.steps) if step.get('id') == 'edge_routes_verify')
        rollback = next(i for i, step in enumerate(self.steps) if step.get('id') == 'edge_rollback')
        self.assertEqual(sorted([prepare,capture,guard,deploy,accept,rollback]), [prepare,capture,guard,deploy,accept,rollback])
        self.assertIn('verify_prepared_static_slot.py', self.steps[prepare]['run'])
        self.assertIn('--locale-origin', self.steps[prepare]['run'])
        self.assertIn('--expect-previous', self.steps[guard]['run'])
        self.assertIn("steps.edge_routes_verify.outcome != 'success'", self.steps[rollback]['if'])
        self.assertIn('EDGE_PREVIOUS_VERSION_ID', self.steps[rollback]['with']['command'])
        rollback_readback = next(step['run'] for step in self.steps if step.get('name') == 'Verify rollback restored service availability')
        self.assertIn('live-edge-state.json', rollback_readback)
        self.assertIn('--expect-version "$EDGE_PREVIOUS_VERSION_ID"', rollback_readback)

    def test_latest_captures_validated_state_inside_lock_but_exact_release_still_guards(self):
        step = next(step for step in self.steps if step.get('name') == 'Read and validate current live edge state')
        code = step['run'].split('STATE_PATH="$RUNNER_TEMP/live-edge-state.json" python3 - <<\'PY\'\n', 1)[1].rsplit('\nPY', 1)[0]
        state = {'schema_version': 1, 'slot': 'a', 'release_id': 'a' * 32, 'tree_sha256': 'b' * 64}
        with tempfile.TemporaryDirectory() as directory:
            state_path = Path(directory) / 'state.json'
            output_path = Path(directory) / 'env'
            state_path.write_text(json.dumps(state))
            for expected, success in [('latest', True), ('a' * 32, True), ('c' * 32, False), ('', False)]:
                output_path.write_text('')
                result = subprocess.run(['python3', '-c', code], env={**os.environ,
                    'STATE_PATH': str(state_path), 'GITHUB_ENV': str(output_path), 'EXPECTED_RELEASE': expected},
                    text=True, capture_output=True)
                self.assertEqual(result.returncode == 0, success, result.stderr)
                if success:
                    self.assertIn('STATIC_RELEASE=' + 'a' * 32, output_path.read_text())
                else:
                    self.assertEqual(output_path.read_text(), '')
            state['release_id'] = 'invalid'
            state_path.write_text(json.dumps(state))
            result = subprocess.run(['python3', '-c', code], env={**os.environ,
                'STATE_PATH': str(state_path), 'GITHUB_ENV': str(output_path), 'EXPECTED_RELEASE': 'latest'},
                text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)

if __name__ == '__main__': unittest.main()
