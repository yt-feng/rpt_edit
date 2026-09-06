#!/usr/bin/env python3
"""Recovery must reuse release gates without rebuilding or paid provider access."""
import ast
from pathlib import Path
import re
import subprocess
import unittest

from build_portal_locale_resume_workflow import SOURCE, TARGET, generate


class ResumeWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.source = SOURCE.read_text()
        self.recovery = TARGET.read_text()

    def test_generated_workflow_is_current(self):
        self.assertEqual(self.recovery, generate(self.source))

    def test_deployment_and_rollback_jobs_are_identical(self):
        separator = '\n  shadow_review_hold:\n'
        self.assertEqual(self.source.split(separator)[1], self.recovery.split(separator)[1])

    def test_no_rebuild_translation_upload_or_schedule(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        for forbidden in ('DEEPSEEK', 'DEEPL', 'build_portal_locales.py', 'build_portal.py',
                          'publish_static_slot.py', 'run_portal_locale_backfill.py', 'workflow_run:', 'cron:'):
            self.assertNotIn(forbidden, preparation)
        self.assertIn('group: portal-production-release', preparation)
        self.assertIn('test "$GITHUB_REF" = "refs/heads/main"', preparation)
        self.assertIn('timeout-minutes: 20', preparation)

    def test_source_identity_is_not_replaced_by_recovery_commit(self):
        self.assertIn('candidate_commit: ${{ steps.static_upload.outputs.commit_sha }}', self.recovery)
        self.assertIn('CANDIDATE_COMMIT_SHA: ${{ steps.static_upload.outputs.commit_sha }}', self.recovery)
        self.assertIn('static_release: ${{ steps.static_upload.outputs.static_release }}', self.recovery)
        self.assertIn('PORTAL_MULTILINGUAL_LIVE_CONFIGURED: "false"', self.recovery)
        self.assertLess(self.recovery.index('Verify committed candidate immediately before cutover'),
                        self.recovery.index('      - name: Deploy prepared neutral edge release'))

    def test_embedded_python_and_shell_parse(self):
        for block in re.split(r'(?=^      - name: )', self.recovery, flags=re.M)[1:]:
            if '        run: |\n' not in block:
                continue
            raw = block.split('        run: |\n', 1)[1]
            lines = []
            for line in raw.splitlines():
                if line.strip() and not line.startswith('          '):
                    break
                lines.append(line[10:] if line.startswith('          ') else line)
            shell = '\n'.join(lines) + '\n'
            shell = re.sub(r'\$\{\{.*?\}\}', 'test-value', shell)
            checked = subprocess.run(['bash', '-n'], input=shell, text=True, capture_output=True)
            self.assertEqual(checked.returncode, 0, block.splitlines()[0] + checked.stderr)
            for python in re.findall(r"<<'PY'[^\n]*\n(.*?)\nPY(?:\n|$)", shell, re.S):
                ast.parse(python)


if __name__ == '__main__':
    unittest.main()
