#!/usr/bin/env python3
import contextlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml
import progressive_wechat_workflow as publisher

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    return yaml.safe_load((ROOT / '.github/workflows' / name).read_text())


class ProgressiveWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.env = {'GITHUB_RUN_ID': '123', 'SOURCE_RUN_ID': '123', 'GITHUB_SHA': 'a' * 40,
                    'SOURCE_SHA': 'a' * 40, 'GITHUB_REPOSITORY': 'owner/reports', 'DATE_FOLDER': '261116',
                    'SHARD_COUNT': '6', 'SELECTED_COUNT': '30'}
        self.options = dict(translated_report_count='0', wechat_draft_articles_per_draft='3',
                            wechat_draft_max_body_chars='18000', wechat_draft_min_inline_images='2',
                            wechat_draft_max_inline_images='8', reports_per_shard='5',
                            wechat_freepublish='false', wechat_draft_upload='true', wechat_draft_source='xhs_notes')

    def config(self, **options):
        with tempfile.TemporaryDirectory() as directory, contextlib.chdir(directory):
            publisher.freeze({**self.env, 'PUBLISHING_OPTIONS_JSON': json.dumps({**self.options, **options})})
            return json.loads(Path('_progressive_wechat_config.json').read_text())

    def test_frozen_options_produce_typed_once_and_plan_commands_without_shell(self):
        config = self.config()
        for plan_only, mode in ((False, '--once'), (True, '--plan-only')):
            command = publisher.once_command(config, self.env, 'manifest.json', plan_only=plan_only)
            self.assertIn(mode, command)
            for flag, value in (('--source-run-id', '123'), ('--source-sha', 'a' * 40),
                                ('--date-folder', '261116'), ('--max-articles', 'all'),
                                ('--articles-per-draft', '3'), ('--shard-count', '6'),
                                ('--reports-per-shard', '5'), ('--expected-source-count', '30')):
                self.assertEqual(command[command.index(flag) + 1], value)
            self.assertIn('_private-workflow-handoff/xhs/123/261116', command)

    def test_disabled_translated_and_freepublish_modes_keep_original_delivery_authority(self):
        for options in ({'wechat_draft_upload': 'false'}, {'wechat_draft_source': 'portal_translated'}, {'wechat_freepublish': 'true'}):
            self.assertIsNone(publisher.once_command(self.config(**options), self.env, 'manifest.json'))

    def test_default_all_articles_and_explicit_numeric_limits_are_retained(self):
        for value, expected in (('all', 'all'), ('0', 'all'), ('12', '12')):
            command = publisher.once_command(self.config(translated_report_count=value), self.env, 'manifest.json')
            self.assertEqual(command[command.index('--max-articles') + 1], expected)

    def test_producer_identity_and_options_cannot_be_overridden_by_child_inputs(self):
        for field, value in (('source_run_id', '124'), ('source_sha', 'b' * 40),
                             ('date_folder', '261117'), ('repository', 'attacker/reports')):
            config = self.config()
            config[field] = value
            with self.assertRaisesRegex(ValueError, 'identity_mismatch'):
                publisher.once_command(config, self.env, 'manifest.json')
        config = self.config()
        config['options']['wechat_draft_articles_per_draft'] = '3; unexpected_command'
        with self.assertRaisesRegex(ValueError, 'invalid_publishing_options'):
            publisher.once_command(config, self.env, 'manifest.json')

    def test_shard_signal_does_not_fail_generation_or_dispatch_before_handoff(self):
        daily = workflow('dropbox-latest-pdf-to-xhs-sharded.yml')
        events = daily.get('on', daily.get(True))
        self.assertEqual(events['workflow_dispatch']['inputs']['wechat_draft_articles_per_draft']['default'], '8')
        jobs = daily['jobs']
        self.assertIn("wechat_draft_articles_per_draft || '8'", jobs['resolve-inputs']['steps'][0]['run'])
        steps = jobs['process-shard']['steps']
        upload = next(step for step in steps if step.get('id') == 'upload_shard')
        signal = next(step for step in steps if step.get('name') == 'Wake short progressive WeChat publisher')
        self.assertGreater(steps.index(signal), steps.index(upload))
        self.assertTrue(signal['continue-on-error'])
        self.assertIn("steps.upload_shard.outcome == 'success'", signal['if'])
        self.assertIn("wechat_freepublish != 'true'", signal['if'])
        self.assertEqual(signal['with']['retries'], 0)
        self.assertNotIn('upload_options_json', signal['with']['script'])
        names = [step.get('name') for step in jobs['select-macro-reports']['steps']]
        self.assertIn('Retain progressive WeChat publisher options', names)

    def test_short_and_final_and_recovery_publishers_share_non_cancelling_mutex(self):
        early = workflow('progressive-wechat-delivery.yml')
        final = workflow('dropbox-latest-pdf-to-xhs-sharded.yml')['jobs']['push-xhs-notes-wechat-drafts']
        recovery = workflow('recover-report-article-delivery.yml')['jobs']['deliver']
        self.assertNotEqual(early['concurrency']['group'], early['jobs']['publish-ready']['concurrency']['group'])
        for job in (early['jobs']['publish-ready'], final, recovery):
            self.assertTrue(job['concurrency']['group'].startswith('daily-wechat-publisher-'))
            self.assertFalse(job['concurrency']['cancel-in-progress'])
            self.assertEqual(job['concurrency']['queue'], 'max')
        for job, step_name in ((early['jobs']['publish-ready'], 'Upload currently ready fixed groups'),
                               (final, 'Upload generated xhs notes to WeChat drafts'),
                               (recovery, 'Upload drafts and require exact article readback')):
            upload = next(step for step in job['steps'] if step.get('name') == step_name)
            self.assertEqual(upload['env']['GH_TOKEN'], '${{ github.token }}')
        self.assertIn('process-shard', final['needs'])
        self.assertIn('source-outcome', final['needs'])
        self.assertTrue(final['continue-on-error'])
        steps = final['steps']
        plan = next(step for step in steps if step.get('name') == 'Initialize progressive WeChat delivery plan')
        upload = next(step for step in steps if step.get('id') == 'upload_xhs_wechat')
        self.assertLess(steps.index(plan), steps.index(upload))
        self.assertIn('progressive_wechat_workflow.py plan', plan['run'])
        self.assertIn('--complete-final', upload['run'])
        self.assertIn('UPLOADER=(python scripts/push_xhs_notes_to_wechat_drafts.py)', upload['run'])
        self.assertIn('PUBLISH_ARGS+=(--publish)', upload['run'])
        self.assertEqual(final['timeout-minutes'], 180)

    def test_final_full_delivery_gate_and_partial_receipts_are_preserved(self):
        final = workflow('dropbox-latest-pdf-to-xhs-sharded.yml')['jobs']['push-xhs-notes-wechat-drafts']
        verification = next(step for step in final['steps'] if step.get('id') == 'delivery')
        self.assertIn("steps.upload_xhs_wechat.outcome == 'success'", verification['if'])
        self.assertIn('--expected-count "${{ needs.select-macro-reports.outputs.selected_count }}"', verification['run'])
        archive = next(step for step in final['steps'] if step.get('id') == 'archive_wechat_receipts')
        self.assertIn('always()', archive['if'])
        self.assertEqual(archive['with']['required'], 'true')

    def test_admission_executes_actual_javascript_for_trusted_new_old_and_cancelled_producers(self):
        step = workflow('progressive-wechat-delivery.yml')['jobs']['admit']['steps'][0]
        source = step['with']['script']
        run = {'id': 123, 'path': '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml',
               'head_branch': 'main', 'head_sha': 'a' * 40, 'head_repository': {'full_name': 'owner/reports'},
               'repository': {'full_name': 'owner/reports'}, 'event': 'workflow_dispatch', 'conclusion': None}
        artifact = {'name': 'progressive-wechat-config-123', 'expired': False}
        for changes, artifacts, expected in (({}, [artifact], 'true'), ({}, [], 'false'),
                                             ({'conclusion': 'cancelled'}, [artifact], 'false'),
                                             ({'head_branch': 'feature'}, [artifact], 'error'),
                                             ({'head_repository': {'full_name': 'attacker/reports'}}, [artifact], 'error')):
            program = '''
const run = RUN, artifacts = ARTIFACTS, outputs = {};
const core = {setOutput: (key,value) => outputs[key]=value, info: () => {}};
const context = {repo:{owner:'owner',repo:'reports'}};
const github = {rest:{actions:{getWorkflowRun:async()=>({data:run}),listWorkflowRunArtifacts:async()=>({data:{total_count:artifacts.length,artifacts}})}}};
try { await (new Function('github','context','core','return (async()=>{'+SOURCE+'})()'))(github,context,core); console.log(outputs.eligible); }
catch { console.log('error'); }
'''.replace('RUN', json.dumps({**run, **changes})).replace('ARTIFACTS', json.dumps(artifacts)).replace('SOURCE', json.dumps(source))
            result = subprocess.run(['node', '--input-type=module', '-e', program],
                                    env={**os.environ, 'SOURCE_RUN_ID': '123', 'DATE_FOLDER': '261116'},
                                    text=True, capture_output=True, check=True)
            self.assertEqual(result.stdout.strip(), expected)


if __name__ == '__main__':
    unittest.main()
