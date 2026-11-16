#!/usr/bin/env python3
"""Recovery must reuse release gates without rebuilding or paid provider access."""
import ast
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

from build_portal_locale_resume_workflow import SOURCE, TARGET, generate


class ResumeWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.source = SOURCE.read_text()
        self.recovery = TARGET.read_text()

    def test_generated_workflow_is_current(self):
        self.assertEqual(self.recovery, generate(self.source))

    def test_complete_provenance_bundle_is_preserved_and_checked_in_both_workflows(self):
        for workflow in (self.source, self.recovery):
            self.assertIn('copy_locale_manifest_bundle', workflow)
            self.assertIn('scripts/verify_portal_locale_manifest_bundle.py', workflow)
            self.assertIn('--release "$STATIC_RELEASE" --tree "$STATIC_TREE_SHA256"', workflow)
            self.assertNotIn('required_paths+=(data/i18n/source-fallbacks', workflow)

    def test_deployment_and_rollback_jobs_are_identical(self):
        def jobs(text):
            return dict(re.findall(r'^  ([a-z_]+):\n(.*?)(?=^  [a-z_]+:\n|\Z)',
                                   text.split('\njobs:\n', 1)[1], re.M | re.S))
        source, recovery = jobs(self.source), jobs(self.recovery)
        shared = {'shadow_review_hold', 'multilingual_approval', 'extended_locales_approval',
                  'english_approval', 'cutover', 'cleanup_multilingual_shadow'}
        self.assertEqual(set(source), shared | {'prepare_release', 'extended_daily_review', 'english_daily_review',
                                              'reject_failed_daily_review', 'schedule_locale_followup'})
        self.assertEqual(set(recovery), shared | {'prepare_release'})
        for job in shared:
            expected = source[job]
            if job in ('extended_locales_approval', 'english_approval'):
                reviewer = 'extended_daily_review' if job == 'extended_locales_approval' else 'english_daily_review'
                expected = expected.replace(f'needs: [prepare_release, {reviewer}]', 'needs: [prepare_release]')
                expected = expected.replace(
                    f"        (needs.{reviewer}.result == 'success' || needs.{reviewer}.result == 'skipped') &&\n", '')
            if job == 'cutover':
                # Manual recovery has no delegated reviewers. Only remove
                # their scheduling dependencies; retain all protected approvals
                # and every deployment, acceptance and rollback byte.
                expected = expected.replace(', extended_daily_review, english_daily_review]', ']')
                for reviewer in ('extended_daily_review', 'english_daily_review'):
                    expected = expected.replace(
                        f"        (needs.{reviewer}.result == 'success' || needs.{reviewer}.result == 'skipped') &&\n", '')
            self.assertEqual(expected, recovery[job], job)

    def test_manual_recovery_cannot_inherit_daily_review_cancellation_or_dangling_dependencies(self):
        for forbidden in ('extended_daily_review', 'english_daily_review', 'reject_failed_daily_review',
                          'schedule_locale_followup', 'actions: write', "api(path + '/cancel'", 'GH_DISPATCH_TOKEN'):
            self.assertNotIn(forbidden, self.recovery)
        for job in ('multilingual_approval', 'extended_locales_approval', 'english_approval'):
            self.assertIn(f"needs.{job}.result == 'success'", self.recovery)
        # A future new daily-only condition needs a deliberate adapter; never
        # silently delete or leave a reference to a job that recovery omits.
        changed = self.source.replace("        always() &&\n        needs.prepare_release.result == 'success' &&",
                                      "        always() &&\n        needs.english_daily_review.outputs.extra == 'true' &&\n"
                                      "        needs.prepare_release.result == 'success' &&")
        with self.assertRaisesRegex(ValueError, 'Unexpected daily-only dependency'):
            generate(changed)

    def test_no_rebuild_translation_upload_or_schedule(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        for forbidden in ('DEEPSEEK', 'DEEPL', 'build_portal_locales.py', 'build_portal.py',
                          'publish_static_slot.py', 'run_portal_locale_backfill.py', 'workflow_run:', 'cron:'):
            self.assertNotIn(forbidden, preparation)
        self.assertIn('group: portal-production-release', preparation)
        self.assertIn('test "$GITHUB_REF" = "refs/heads/main"', preparation)
        self.assertIn('    timeout-minutes: 120', preparation)

    def test_source_identity_is_not_replaced_by_recovery_commit(self):
        self.assertIn('candidate_commit: ${{ steps.static_upload.outputs.commit_sha }}', self.recovery)
        self.assertIn('CANDIDATE_COMMIT_SHA: ${{ steps.static_upload.outputs.commit_sha }}', self.recovery)
        self.assertIn('static_release: ${{ steps.static_upload.outputs.static_release }}', self.recovery)
        self.assertLess(self.recovery.index('Verify committed candidate immediately before cutover'),
                        self.recovery.index('      - name: Deploy prepared neutral edge release'))

    def test_recovery_preserves_production_activation_state(self):
        expression = "PORTAL_MULTILINGUAL_LIVE_CONFIGURED: ${{ vars.PORTAL_MULTILINGUAL_LIVE || 'false' }}"
        self.assertIn(expression, self.source)
        self.assertIn(expression, self.recovery)
        operation = self.recovery.split('      - name: Require reviewed main operation\n', 1)[1]
        operation = operation.split('      - name: ', 1)[0]
        shell = '\n'.join(line[10:] if line.startswith('          ') else line
                          for line in operation.split('        run: |\n', 1)[1].splitlines()) + '\n'
        for live in ('true', 'false', 'invalid'):
            with self.subTest(live=live), tempfile.TemporaryDirectory() as temporary:
                env_file, output_file = Path(temporary) / 'env', Path(temporary) / 'output'
                env = {
                    'PATH': os.environ['PATH'], 'GITHUB_REF': 'refs/heads/main',
                    'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_SHA': 'a' * 40,
                    'GITHUB_ENV': str(env_file), 'GITHUB_OUTPUT': str(output_file),
                    'REQUESTED_OPERATION': 'migrate', 'REQUESTED_TRANSLATION_SCOPE': 'incremental',
                    'PORTAL_MULTILINGUAL_CONFIGURED': 'true',
                    'PORTAL_MULTILINGUAL_LIVE_CONFIGURED': live,
                    'PORTAL_MULTILINGUAL_INDEX_START_DATE': '2026-01-01',
                    'EXTENDED_LOCALES_REQUESTED': '', 'EXTENDED_SOURCE_GENERATION': '',
                    'EXTENDED_CANDIDATE_IDS': '', 'EXTENDED_HANDOFF': '', 'ENGLISH_HANDOFF': '',
                }
                result = subprocess.run(['bash', '-c', shell], env=env, text=True, capture_output=True)
                if live == 'invalid':
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(output_file.exists())
                    continue
                self.assertEqual(result.returncode, 0, result.stderr)
                output = dict(line.split('=', 1) for line in output_file.read_text().splitlines())
                exported = dict(line.split('=', 1) for line in env_file.read_text().splitlines())
                self.assertEqual(output['multilingual_live'], live)
                self.assertEqual(exported['PORTAL_MULTILINGUAL_LIVE'], live)
                self.assertEqual(output['multilingual_enabled'], 'true')

    def test_fresh_shadow_validation_does_not_change_first_activation_approval(self):
        shadow = self.recovery.split('      - name: Prepare isolated multilingual shadow worker\n', 1)[1]
        condition = shadow.split('        if: >-\n', 1)[1].split('        env:\n', 1)[0]
        for prerequisite in ("steps.release_delta.outputs.changed == 'true'",
                             "steps.locale_build.outputs.ready == 'true'",
                             "steps.operation.outputs.multilingual_enabled == 'true'"):
            self.assertIn(prerequisite, condition)
        self.assertNotIn('multilingual_live', condition)
        approval = self.recovery.split('\n  multilingual_approval:\n', 1)[1]
        approval = approval.split('\n  extended_locales_approval:\n', 1)[0]
        self.assertIn("needs.prepare_release.outputs.multilingual_live != 'true'", approval)
        self.assertIn('if approved != actual:', approval)
        cutover = self.recovery.split('\n  cutover:\n', 1)[1]
        self.assertIn("needs.prepare_release.outputs.multilingual_live == 'true' ||\n"
                      "          needs.multilingual_approval.result == 'success'", cutover)
        changed = self.source.replace("              steps.operation.outputs.multilingual_live != 'true'",
                                      "              steps.operation.outputs.multilingual_live == 'false'")
        with self.assertRaisesRegex(ValueError, 'Unexpected production shadow activation condition'):
            generate(changed)

    def test_extended_recovery_preserves_bytes_and_requires_fresh_approval(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        self.assertNotIn('restore_assemble_portal_extended_r2.py', preparation)
        self.assertIn("restored_identity(Path('_neutral_site'))", preparation)
        self.assertIn('extended_requested: ${{ steps.extended_assembly.outputs.ready }}', preparation)
        self.assertIn('Remove required reviewers for automatic deployment', preparation)
        self.assertIn('name: Publish extended locale review identity', preparation)

    def test_restored_candidate_passes_local_route_gate_before_shadow_or_cutover(self):
        self.assertIn('python3 -B scripts/test_verify_portal_locale_routes.py', self.recovery)
        restored = self.recovery.index('Restore verified uploaded candidate without rebuilding or translating')
        verified = self.recovery.index('Validate locale application routes before upload')
        policy = self.recovery.index('Compute multilingual index policy identity')
        self.assertLess(restored, verified)
        self.assertLess(verified, policy)

    def test_english_recovery_keeps_exact_uploaded_bytes_and_protected_approval(self):
        preparation = self.recovery.split('\n  shadow_review_hold:\n')[0]
        self.assertIn('scripts/portal_english_publication.py recover', preparation)
        self.assertNotIn('scripts/portal_english_publication.py assemble', preparation)
        self.assertIn('english_requested: ${{ steps.english_assembly.outputs.requested }}', preparation)
        self.assertIn('english_ready: ${{ steps.english_assembly.outputs.ready }}', preparation)
        self.assertIn('CANDIDATE_COMMIT_SHA: ${{ steps.static_upload.outputs.commit_sha }}', preparation)
        self.assertIn('ENGLISH_HANDOFF: ${{ steps.english_assembly.outputs.handoff }}', preparation)
        self.assertIn('Remove required reviewers for automatic deployment', preparation)
        self.assertNotIn('english_daily_review:', self.recovery)
        self.assertIn('needs.english_approval.result == \'success\'', self.recovery)

    def test_retained_english_still_binds_and_only_new_content_requests_approval(self):
        review = self.recovery.split('      - name: Publish metadata-only English exact-version review identity\n', 1)[1]
        review = review.split('      - name: ', 1)[0]
        self.assertIn("steps.english_assembly.outputs.requested == 'true'", review)
        self.assertIn("steps.english_assembly.outputs.ready == 'true'", review)
        artifact = self.recovery.split('      - name: Build public validation artifact\n', 1)[1]
        artifact = artifact.split('      - name: ', 1)[0]
        self.assertIn("ENGLISH_REQUESTED: ${{ steps.english_assembly.outputs.requested || 'false' }}", artifact)
        self.assertIn('if [ "$ENGLISH_REQUESTED" = "true" ]; then', artifact)
        bind = self.recovery.split('      - name: Bind the exact prepared English version after protected approval\n', 1)[1]
        bind = bind.split('      - name: ', 1)[0]
        self.assertIn("if: needs.prepare_release.outputs.english_ready == 'true'", bind)
        shell = '\n'.join(line[10:] if line.startswith('          ') else line
                          for line in bind.split('        run: |\n', 1)[1].splitlines()) + '\n'
        # macOS Bash 3 treats an empty array as unset under nounset; this
        # recorder tests argument selection, while production uses Ubuntu Bash.
        shell = shell.replace('set -euo pipefail', 'set -eo pipefail', 1)
        for requested in ('false', 'true'):
            with self.subTest(requested=requested), tempfile.TemporaryDirectory() as temporary:
                command_log = Path(temporary) / 'commands'
                env = {'PATH': os.environ['PATH'], 'COMMAND_LOG': str(command_log),
                       'ENGLISH_REQUESTED': requested, 'ENGLISH_LEDGER': 'a' * 64,
                       'STATIC_SLOT': 'b', 'STATIC_RELEASE': 'b' * 32, 'STATIC_TREE_SHA256': 'c' * 64}
                # Execute the actual binding shell with a recorder in place of
                # its Python entry point; no publication/network code runs.
                result = subprocess.run(['bash', '-c',
                                         'python3() { printf "%s\\n" "$*" >> "$COMMAND_LOG"; }\n' + shell],
                                        env=env, text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                commands = command_log.read_text().splitlines()
                self.assertEqual(len(commands), 2)
                self.assertIn('portal_english_publication.py preflight ', commands[0])
                self.assertIn('portal_english_publication.py bind ', commands[1])
                self.assertEqual('--approved-ledger ' in commands[1], requested == 'true')

    def test_fresh_loading_budget_evidence_is_preserved_before_artifact_upload(self):
        preserve = self.recovery.split('      - name: Preserve uploaded candidate provenance\n', 1)[1]
        preserve = preserve.split('      - name: Upload release validation artifact\n', 1)[0]
        self.assertIn('"$RUNNER_TEMP/chinese-recovery-performance.json"', preserve)
        self.assertIn('_release_validation/candidate/chinese-recovery-performance.json', preserve)
        self.assertIn('_release_validation/candidate/locale-resume-identity.json', preserve)

    def test_retained_recovery_forwards_verified_proof_and_never_queues_another_build(self):
        self.assertIn("RETAINED_CORE_LOCALES: ${{ steps.static_upload.outputs.retained || 'false' }}", self.recovery)
        self.assertIn('echo "retained=$RETAINED_CORE_LOCALES" >> "$GITHUB_OUTPUT"', self.recovery)
        self.assertIn('_release_validation/candidate/locale-retention.json', self.recovery)
        self.assertIn('_release_validation/candidate/locale-retention-active-manifest.json', self.recovery)
        self.assertIn('REQUESTED_PUBLICATION_MODE: "locales"', self.recovery)
        self.assertNotIn('schedule_locale_followup:', self.recovery)
        self.assertNotIn('dispatch_neutral_locale_followup.py', self.recovery)

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
