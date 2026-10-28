"""Deployment ordering and rollback boundaries for the bounded UI-only route."""
from pathlib import Path
import re
import shlex
import subprocess
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
        self.assertEqual(self.workflow['concurrency'], {'group': 'portal-production-release', 'cancel-in-progress': False})
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

if __name__ == '__main__': unittest.main()
