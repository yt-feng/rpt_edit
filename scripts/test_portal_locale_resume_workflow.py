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
        def jobs(text):
            return dict(re.findall(r'^  ([a-z_]+):\n(.*?)(?=^  [a-z_]+:\n|\Z)',
                                   text.split('\njobs:\n', 1)[1], re.M | re.S))
        source, recovery = jobs(self.source), jobs(self.recovery)
        shared = {'shadow_review_hold', 'multilingual_approval', 'extended_locales_approval',
                  'english_approval', 'cutover', 'cleanup_multilingual_shadow'}
        self.assertEqual(set(source), shared | {'prepare_release', 'extended_daily_review', 'english_daily_review'})
        self.assertEqual(set(recovery), shared | {'prepare_release'})
        for job in shared:
            self.assertEqual(source[job], recovery[job], job)

    def test_no_rebuild_translation_upload_or_schedule(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        for forbidden in ('DEEPSEEK', 'DEEPL', 'build_portal_locales.py', 'build_portal.py',
                          'publish_static_slot.py', 'run_portal_locale_backfill.py', 'workflow_run:', 'cron:'):
            self.assertNotIn(forbidden, preparation)
        self.assertIn('group: portal-production-release', preparation)
        self.assertIn('test "$GITHUB_REF" = "refs/heads/main"', preparation)
        self.assertIn('    timeout-minutes: 60', preparation)

    def test_source_identity_is_not_replaced_by_recovery_commit(self):
        self.assertIn('candidate_commit: ${{ steps.static_upload.outputs.commit_sha }}', self.recovery)
        self.assertIn('CANDIDATE_COMMIT_SHA: ${{ steps.static_upload.outputs.commit_sha }}', self.recovery)
        self.assertIn('static_release: ${{ steps.static_upload.outputs.static_release }}', self.recovery)
        self.assertIn('PORTAL_MULTILINGUAL_LIVE_CONFIGURED: "false"', self.recovery)
        self.assertLess(self.recovery.index('Verify committed candidate immediately before cutover'),
                        self.recovery.index('      - name: Deploy prepared neutral edge release'))

    def test_extended_recovery_preserves_bytes_and_requires_fresh_approval(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        self.assertNotIn('restore_assemble_portal_extended_r2.py', preparation)
        self.assertIn("restored_identity(Path('_neutral_site'))", preparation)
        self.assertIn('extended_requested: ${{ steps.extended_assembly.outputs.ready }}', preparation)
        self.assertIn('Configure required reviewers before extended activation', preparation)
        self.assertIn('name: Publish extended locale review identity', preparation)

    def test_restored_candidate_passes_local_route_gate_before_shadow_or_cutover(self):
        self.assertIn('python3 -B scripts/test_verify_portal_locale_routes.py', self.recovery)
        restored = self.recovery.index('Restore verified uploaded candidate without rebuilding or translating')
        verified = self.recovery.index('Validate locale application routes before upload')
        policy = self.recovery.index('Compute multilingual index policy identity')
        self.assertLess(restored, verified)
        self.assertLess(verified, policy)

    def test_english_recovery_keeps_exact_uploaded_bytes_and_requires_fresh_protected_approval(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        self.assertIn('scripts/portal_english_publication.py recover', preparation)
        self.assertNotIn('scripts/portal_english_publication.py assemble', preparation)
        self.assertIn('english_requested: ${{ steps.english_assembly.outputs.ready }}', preparation)
        self.assertIn('CANDIDATE_COMMIT_SHA: ${{ steps.static_upload.outputs.commit_sha }}', preparation)
        self.assertIn('ENGLISH_HANDOFF: ${{ steps.english_assembly.outputs.handoff }}', preparation)
        self.assertIn('Configure required reviewers before English recovery', preparation)
        self.assertNotIn('english_daily_review:', self.recovery)
        self.assertIn('needs.english_approval.result == \'success\'', self.recovery)

    def test_fresh_loading_budget_evidence_is_preserved_before_artifact_upload(self):
        preserve = self.recovery.split('      - name: Preserve uploaded candidate provenance\n', 1)[1]
        preserve = preserve.split('      - name: Upload release validation artifact\n', 1)[0]
        self.assertIn('"$RUNNER_TEMP/chinese-recovery-performance.json"', preserve)
        self.assertIn('_release_validation/candidate/chinese-recovery-performance.json', preserve)
        self.assertIn('_release_validation/candidate/locale-resume-identity.json', preserve)

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
