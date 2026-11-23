"""Frozen-code admission and exact replay evidence, with no network or cloud writes."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import admit_neutral_release_source as gate


class SourceAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.git('init', '-q')
        for path in gate.REQUIRED_CODE:
            self.write(path, 'initial code\n')
        self.initial = self.commit()

    def git(self, *args):
        return subprocess.check_output(['git', '-c', 'user.name=Source admission test',
            '-c', 'user.email=admission@example.invalid', *args], cwd=self.root,
            stderr=subprocess.PIPE).decode().strip()

    def write(self, path, body):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def admit(self, head, *, event_name='workflow_dispatch', inputs=None):
        return gate.admit(self.root, source_sha=self.initial, main_sha=head,
            event_name=event_name, event={'inputs': inputs or {}}, repository='example/repo',
            run_id=123, run_attempt=2)

    def test_catalog_report_archive_locale_data_and_documentation_changes_are_allowed(self):
        for name in ('portal_suite/data/catalog.json', 'portal_suite/data/blog_archive/day.json',
                     'portal_suite/data/i18n/cache-v1.json', 'portal_suite/site_src/data/course-materials.json',
                     'reports/latest.pdf', 'docs/publishing.md', 'scripts/test_builder.py'):
            self.write(name, 'new report data')
        result = self.admit(self.commit())
        self.assertEqual(result['state'], 'ready')
        self.assertEqual(result['changed_code_paths'], [])
        self.assertFalse(result['replay_required'])
        self.assertNotEqual(result['source']['head_sha'], result['observed_main_sha'])

    def test_app_change_supersedes_without_mutation_or_checkout_change(self):
        self.write('portal_suite/site_src/assets/app.js', 'new admin API')
        head = self.commit()
        result = self.admit(head)
        self.assertEqual(result['state'], 'superseded')
        self.assertEqual(result['changed_code_paths'], ['portal_suite/site_src/assets/app.js'])
        self.assertFalse(result['publication_attempted'])
        self.assertFalse(result['automatic_dispatch_attempted'])
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.git('status', '--porcelain'), '')

    def test_ui_templates_locale_assets_edge_and_indirect_build_helpers_are_covered(self):
        for name in ('portal_suite/site_src/newsfeed.html', 'portal_suite/locale_assets/locale.css',
                     'workers/edge-static-host/src/index.js', 'scripts/portal_indirect_builder.py',
                     'scripts/materialize_private_assets.sh', gate.WORKFLOW,
                     'requirements-neutral-release-constraints.txt'):
            with self.subTest(path=name):
                self.write(name, 'changed executable source')
                result = self.admit(self.commit())
                self.assertEqual(result['state'], 'superseded')
                self.assertIn(name, result['changed_code_paths'])

    def test_unknown_or_incomplete_main_is_a_real_failure(self):
        with self.assertRaises(gate.AdmissionError):
            self.admit('f' * 40)
        self.git('rm', 'portal_suite/site_src/assets/app.js')
        with self.assertRaisesRegex(gate.AdmissionError, 'incomplete_source_code'):
            self.admit(self.commit())

    def test_exact_all_manual_inputs_and_original_provenance_survive(self):
        values = {'operation': 'migrate', 'translation_scope': 'month', 'publication_mode': 'locales',
            'locale_followup_source': '456:3', 'catalog_recovery_release': 'b'*32,
            'extended_locales': 'fr,zh-Hant', 'extended_source_generation': 'c'*64,
            'extended_candidate_ids': 'fr='+'d'*64+',zh-Hant='+'e'*64,
            'extended_handoff': 'a'*64, 'english_handoff': 'f'*64}
        self.write('portal_suite/site_src/assets/app.js', 'changed')
        result = self.admit(self.commit(), inputs=values)
        self.assertEqual(result['replay']['inputs'], values)
        self.assertEqual(result['original_manual_inputs'], values)
        self.assertEqual(result['input_mode'], 'exact_manual_inputs')
        self.assertEqual(result['replay']['ref'], 'main')
        self.assertEqual(result['source'], {'repository': 'example/repo', 'event': 'workflow_dispatch',
            'run_id': 123, 'run_attempt': 2, 'head_sha': self.initial})

    def test_automatic_replay_is_explicitly_reconstructed_and_has_no_private_event_payload(self):
        result = self.admit(self.initial, event_name='workflow_run')
        self.assertEqual(result['input_mode'], 'reconstructed_automatic_defaults')
        self.assertIsNone(result['original_manual_inputs'])
        self.assertEqual(result['replay']['inputs'], {**gate.DEFAULT_INPUTS, 'operation': 'migrate'})
        with self.assertRaises(gate.AdmissionError):
            gate.replay_inputs('repository_dispatch', {'action': 'unrelated'})
        mode, values = gate.replay_inputs('repository_dispatch', {
            'action': 'portal-dropbox-report-refresh', 'client_payload': {'private': 'never export'}})
        self.assertNotIn('private', json.dumps(values))

    def test_unexpected_or_secret_bearing_manual_fields_are_not_exported(self):
        for values in ({'credential': 'never export'}, {'extended_handoff': 'https://private.invalid/token'},
                       {'operation': 'migrate\nsecret'}, {'extended_locales': 'person@example.invalid'}):
            with self.subTest(values=values), self.assertRaises(gate.AdmissionError):
                self.admit(self.initial, inputs=values)

    def test_main_lookup_fetches_exact_observed_object_without_switching_checkout(self):
        calls = []
        def fake(args, **kwargs):
            calls.append(args)
            return ('a'*40+'\n').encode() if args[0] == 'gh' else b''
        with patch.object(gate, 'run_read', side_effect=fake):
            self.assertEqual(gate.resolve_main(self.root, 'example/repo'), 'a'*40)
        self.assertEqual(calls[1], ['git', 'fetch', '--quiet', '--no-tags', '--depth=1', '--filter=blob:none', 'origin', 'a'*40])
        self.assertFalse(any('checkout' in call or 'reset' in call for call in calls))
        with patch.object(gate, 'run_read', return_value=b'null\n'), self.assertRaises(gate.AdmissionError):
            gate.resolve_main(self.root, 'example/repo')

    def test_lookup_failure_never_writes_success_output_or_replay_manifest(self):
        event = self.root / 'event.json'
        event.write_text('{"inputs": {}}')
        output = self.root / 'result.json'
        env = {'GITHUB_REF': 'refs/heads/main', 'GITHUB_SHA': self.initial,
            'GITHUB_EVENT_PATH': str(event), 'GITHUB_REPOSITORY': 'example/repo',
            'GITHUB_OUTPUT': str(self.root / 'output'), 'GITHUB_STEP_SUMMARY': str(self.root / 'summary')}
        with patch.dict(os.environ, env), patch('sys.argv', ['gate', '--output', str(output)]), \
                patch.object(gate, 'run_read', return_value=self.initial.encode()), \
                patch.object(gate, 'resolve_main', side_effect=gate.AdmissionError('unavailable')), \
                contextlib.redirect_stderr(io.StringIO()) as errors:
            self.assertEqual(gate.main(), 1)
        self.assertFalse(output.exists())
        self.assertFalse((self.root / 'output').exists())
        self.assertIn('no publication was admitted', errors.getvalue())


class WorkflowGateTests(unittest.TestCase):
    def test_admission_holds_existing_lock_and_every_publication_path_needs_prepare(self):
        source = (Path(__file__).resolve().parents[1] / gate.WORKFLOW).read_text()
        admission = source.split('\n  source_admission:\n')[1].split('\n  prepare_release:\n')[0]
        prepare = source.split('\n  prepare_release:\n')[1].split('\n  shadow_review_hold:\n')[0]
        self.assertIn("&& 'portal-production-release'", source.split('\njobs:')[0])
        self.assertIn('cancel-in-progress: false', source.split('\njobs:')[0])
        self.assertIn('ref: ${{ github.sha }}', admission)
        self.assertIn('contents: read', admission)
        self.assertIn('persist-credentials: true', admission)
        self.assertIn('needs: source_admission', prepare)
        self.assertIn("needs.source_admission.result == 'success' && needs.source_admission.outputs.ready == 'true'", prepare)
        self.assertEqual(source.count('scripts/admit_neutral_release_source.py'), 1)
        for forbidden in ('secrets.', 'actions: write', 'wrangler', 'publish_static_slot', 'dispatches'):
            self.assertNotIn(forbidden, admission)
        for name in ('cutover', 'schedule_locale_followup', 'reject_failed_daily_review'):
            block = source.split('\n  '+name+':\n')[1].split('\n    runs-on:')[0]
            self.assertIn("needs.prepare_release.result == 'success'", block)
        self.assertIn('candidate_commit: ${{ steps.operation.outputs.commit_sha }}', prepare)
        self.assertIn('"$GITHUB_SHA"', prepare)


if __name__ == '__main__':
    unittest.main()
