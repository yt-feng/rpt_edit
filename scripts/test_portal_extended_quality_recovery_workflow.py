"""Execute real workflow shell branches with local command stubs; no model or R2."""
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


WORKFLOW = Path(__file__).resolve().parents[1] / '.github/workflows/portal-extended-locales-r2.yml'
PLAN = '1' * 64
GENERATION = '2' * 64


def condition(expression, values, *, cancelled=False):
    """Evaluate only the fixed workflow boolean grammar used by these guards."""
    expression = expression.strip().removeprefix('${{').removesuffix('}}').strip()
    expression = expression.replace('always()', 'True').replace('cancelled()', str(cancelled))
    expression = re.sub(r'\b(?:matrix|steps|needs|inputs|github)\.[a-zA-Z0-9_.]+',
                        lambda match: repr(values.get(match.group(), '')), expression)
    expression = expression.replace('&&', ' and ').replace('||', ' or ')
    expression = re.sub(r'!(?!=)', ' not ', expression)
    return bool(eval('('+expression+')', {'__builtins__': {}}, {}))


class QualityWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = yaml.safe_load(WORKFLOW.read_text())
        cls.locale = cls.workflow['jobs']['locale']
        cls.followup = cls.workflow['jobs']['continue_admitted_batches']

    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        binary = self.root / 'bin'; binary.mkdir()
        self.log = self.root / 'commands.jsonl'
        stub = self.root / 'stub.py'
        stub.write_text('''import json, os, pathlib, sys
with open(os.environ['STUB_LOG'], 'a') as out:
    out.write(json.dumps(sys.argv[1:])+'\\n')
if 'followup' in sys.argv:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as out:
        out.write('continue='+os.environ.get('STUB_CONTINUE', 'false')+'\\n')
print(json.dumps({'present': True, 'status': 'synthetic'}))
raise SystemExit(int(os.environ.get('STUB_EXIT', '0')))
''')
        command = binary / 'python3'
        command.write_text('#!/bin/sh\nexec '+shlex.quote(sys.executable)+' '+shlex.quote(str(stub))+' "$@"\n')
        command.chmod(0o755)
        self.env = {'PATH': str(binary)+os.pathsep+os.defpath, 'RUNNER_TEMP': str(self.root),
                    'GITHUB_OUTPUT': str(self.root/'output'), 'GITHUB_STEP_SUMMARY': str(self.root/'summary'),
                    'STUB_LOG': str(self.log), 'QUALITY_REPAIR': PLAN, 'SOURCE_GENERATION': GENERATION,
                    'LOCALE': 'fr', 'TRANSLATION_SECONDS': '123', 'REQUESTED_OPERATION': 'candidate',
                    'REPAIR_EVIDENCE': '', 'ALLOW_SOURCE_FALLBACK': 'true',
                    'EXTENDED_R2_PREFIX': '_extended-locales/v1'}

    def step(self, name, *, job=None):
        return next(step for step in (job or self.locale)['steps'] if step.get('name') == name)

    def execute(self, step, **environment):
        result = subprocess.run([shutil.which('bash') or '/bin/bash', '-c', step['run']],
            cwd=self.root, env={**self.env, **environment}, capture_output=True, text=True)
        calls = [json.loads(line) for line in self.log.read_text().splitlines()] if self.log.exists() else []
        return result, calls

    def assert_identity(self, call, operation):
        self.assertEqual(call[:3], ['-B', 'scripts/portal_extended_quality_recovery.py', operation])
        for flag, value in (('--plan', PLAN), ('--locale', 'fr'), ('--generation', GENERATION),
                            ('--checkpoint', str(self.root/'locale-checkpoint.json')),
                            ('--corpus', str(self.root/'extended-source-corpus.json')),
                            ('--output', str(self.root/'extended-candidate')), ('--seconds', '123')):
            self.assertEqual(call[call.index(flag)+1], value)

    def test_shared_serialization_and_two_workers_are_retained(self):
        self.assertFalse(self.workflow['concurrency']['cancel-in-progress'])
        self.assertIn("'extended-locales-r2-pipeline'", self.workflow['concurrency']['group'])
        self.assertEqual(self.locale['strategy']['max-parallel'], 2)
        self.assertEqual(self.locale['name'], 'locale (${{ matrix.locale }})')
        self.assertEqual(self.locale['strategy']['matrix']['include'],
                         '${{ fromJSON(needs.source.outputs.locale_jobs_json) }}')
        self.assertEqual(self.locale['env']['QUALITY_REPAIR'], "${{ matrix.quality_repair || '' }}")
        self.assertEqual(self.workflow['jobs']['source']['outputs']['quality_repair_plans_json'],
                         "${{ steps.source.outputs.quality_repair_plans_json || '[]' }}")

    def test_quality_restore_routes_to_exact_plan_and_does_not_restore_latest_seed(self):
        step = self.step('Restore locale checkpoint from private R2')
        result, calls = self.execute(step)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(calls), 1); self.assert_identity(calls[0], 'restore')
        self.assertEqual((self.root/'output').read_text(), 'present=true\n')
        for name in ('Restore fixed source generation', 'Restore verified incremental unit memo'):
            guard = self.step(name)['if']
            self.assertFalse(condition(guard, {'matrix.quality_repair': PLAN, 'inputs.operation': 'candidate'}))
            self.assertTrue(condition(guard, {'inputs.operation': 'candidate'}))

    def test_setup_is_skipped_for_an_exact_ledger_only_plan_and_unknown_flag(self):
        step = self.step('Set up pinned Hy-MT2 CPU model without audit artifacts')
        self.assertTrue(condition(step['if'], {}))
        self.assertTrue(condition(step['if'], {'matrix.quality_repair':PLAN,
                                              'steps.checkpoint.outputs.requires_engine':'true'}))
        for flag in ('false',''):
            self.assertFalse(condition(step['if'], {'matrix.quality_repair':PLAN,
                                                   'steps.checkpoint.outputs.requires_engine':flag}))
        result, calls = self.execute(self.step('Restore locale checkpoint from private R2'))
        self.assertEqual(result.returncode,0)
        self.assertEqual(calls[0][calls[0].index('--github-output')+1],str(self.root/'output'))

    def test_quality_build_uses_only_the_plan_builder_and_preserves_exit_status(self):
        step = self.step('Run bounded locale translation and retain timeout state')
        for code in (0, 2, 75):
            with self.subTest(code=code):
                self.log.unlink(missing_ok=True); (self.root/'output').unlink(missing_ok=True)
                result, calls = self.execute(step, STUB_EXIT=str(code))
                self.assertEqual(len(calls), 1); self.assert_identity(calls[0], 'build')
                self.assertEqual(result.returncode, code if code == 2 else 0, result.stderr)
                self.assertIn(f'exit_code={code}\n', (self.root/'output').read_text())

    def test_normal_and_english_builds_keep_their_existing_entrypoints(self):
        step = self.step('Run bounded locale translation and retain timeout state')
        for locale, operation, script in (
                ('fr', 'candidate', 'build_portal_extended_locales.py'),
                ('en', 'candidate', 'portal_english_commentary.py'),
                ('fr', 'checkpoint-repair', 'repair_portal_extended_checkpoint.py')):
            with self.subTest(locale=locale, operation=operation):
                self.log.unlink(missing_ok=True)
                result, calls = self.execute(step, QUALITY_REPAIR='', LOCALE=locale, REQUESTED_OPERATION=operation)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(len(calls), 1)
                self.assertEqual(calls[0][1], 'scripts/'+script)

    def test_quality_never_uses_generic_always_persistence_and_only_persists_success(self):
        for name in ('Persist checkpoint even when the locale budget ended',
                     'Persist complete or incomplete candidate pages privately'):
            guard = self.step(name)['if']
            for operation in ('candidate', 'checkpoint-repair', 'recovery-test'):
                self.assertFalse(condition(guard, {'matrix.quality_repair': PLAN, 'inputs.operation': operation}))
            self.assertTrue(condition(guard, {'inputs.operation': 'candidate'}))
        step = self.step('Persist only verified quality repair progress against the exact source plan')
        for code in ('', '2', '75'):
            self.assertFalse(condition(step['if'], {'matrix.quality_repair': PLAN, 'steps.build.outputs.exit_code': code}))
        self.assertFalse(condition(step['if'], {'steps.build.outputs.exit_code': '0'}))
        self.assertTrue(condition(step['if'], {'matrix.quality_repair': PLAN, 'steps.build.outputs.exit_code': '0'}))
        result, calls = self.execute(step)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(calls), 1); self.assert_identity(calls[0], 'persist')

    def test_pure_quality_followup_works_without_source_admission_and_never_on_cancellation(self):
        values = {'github.ref': 'refs/heads/main', 'needs.source.result': 'success',
                  'needs.source.outputs.has_work': 'true', 'inputs.operation': 'candidate',
                  'needs.source.outputs.quality_repair_plans_json': json.dumps([PLAN])}
        self.assertTrue(condition(self.followup['if'], values))
        self.assertTrue(condition(self.followup['if'], {**values,'needs.source.outputs.has_work':'false'}),
                        'A source-only exact prepared tail still has a durable frontier')
        self.assertFalse(condition(self.followup['if'], values, cancelled=True))
        self.assertFalse(condition(self.followup['if'], {**values, 'needs.source.result': 'failure'}))
        self.assertFalse(condition(self.followup['if'], {**values, 'needs.source.outputs.quality_repair_plans_json': '[]'}))
        step = self.step('Continue quality debt only after accepted durable repair progress', job=self.followup)
        result, calls = self.execute(step, QUALITY_REPAIR_PLANS=json.dumps([PLAN]))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls, [['-B', 'scripts/portal_extended_quality_recovery.py', 'followup',
                                 '--plans', json.dumps([PLAN]), '--github-output', str(self.root/'output')]])
        self.assertEqual((self.root/'output').read_text(), 'continue=false\n')

    def test_quality_plan_cannot_also_write_legacy_repair_when_operation_conflicts(self):
        step = self.step('Run bounded locale translation and retain timeout state')
        result, calls = self.execute(step, REQUESTED_OPERATION='checkpoint-repair')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(calls), 1); self.assert_identity(calls[0], 'build')
        legacy = self.step('Validate exact repaired units and complete candidate before original-intent adoption')
        values = {'inputs.operation': 'checkpoint-repair', 'steps.build.outputs.exit_code': '0'}
        self.assertTrue(condition(legacy['if'], values))
        self.assertFalse(condition(legacy['if'], {**values, 'matrix.quality_repair': PLAN}))

    def test_dispatch_requires_an_explicit_true_frontier_and_retains_normal_progress(self):
        guard = self.step('Dispatch the next bounded per-language cursors', job=self.followup)['if']
        for frontier in ('frontier', 'english_frontier', 'quality_frontier'):
            self.assertTrue(condition(guard, {f'steps.{frontier}.outputs.continue': 'true'}))
            self.assertFalse(condition(guard, {f'steps.{frontier}.outputs.continue': 'false'}))
        self.assertFalse(condition(guard, {}))
        step = self.step('Continue quality debt only after accepted durable repair progress', job=self.followup)
        result, _ = self.execute(step, QUALITY_REPAIR_PLANS=json.dumps([PLAN]), STUB_EXIT='2')
        self.assertEqual(result.returncode, 2, 'pipefail must prevent dispatch after an unverified frontier')


if __name__ == '__main__':
    unittest.main()
