"""Primary CLI and wrapper boundaries for explicit Institution dependency holds."""
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import institution_dependency_backlog as backlog
import mineru_task_ledger as m
from inspect_durable_mineru import failure_message_hash
import pdf_to_xhs_batch as primary
import run_pdf_to_xhs_in_batches as wrapper
from test_mineru_result_cache import MemoryR2, result_zip, S3Error

ERROR = {'err_code': 'FIXTURE_PARSE_FAILURE', 'err_msg': 'fixture terminal parse failure'}


class WithHeadR2(MemoryR2):
    def head_object(self, **kwargs):
        if kwargs['Key'] not in self.objects:
            raise S3Error('NoSuchKey', 404)
        value = copy.deepcopy(self.objects[kwargs['Key']])
        raw = value.pop('Body')
        return dict(value, ContentLength=len(raw))


class RecordingLedger(m.Ledger):
    def run(self, *args, **kwargs):
        self.run_modes.append(self.forbid_new_submissions)
        return super().run(*args, **kwargs)


class Provider:
    def __init__(self, items, *, unknown=False):
        self.items, self.unknown = items, unknown
        self.polls, self.posts, self.uploads = {}, 0, 0

    def submit(self, *args):
        self.posts += 1
        raise AssertionError('Accepted originals must never be resubmitted')

    def upload(self, *args):
        self.uploads += 1
        raise AssertionError('Accepted originals must never be uploaded')

    def poll(self, batch_id, token, timeout):
        self.polls[batch_id] = self.polls.get(batch_id, 0) + 1
        item = self.items[batch_id]
        # Pre-filter sees two complete tasks; the main pass observes a newly
        # reported terminal failure in the second root, while the first stays good.
        if batch_id == 'bad' and self.polls[batch_id] >= 2:
            error = dict(ERROR, err_msg='unknown new failure') if self.unknown else ERROR
            return [{'data_id': item['id'], 'state': 'failed', **error}]
        return [{'data_id': item['id'], 'state': 'done', 'full_zip_url': 'https://results.invalid/' + batch_id}]


class BacklogPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.inputs = self.root/'pdfs'; self.inputs.mkdir()
        self.output = self.root/'out'; self.outcome = self.root/'outcome.json'
        self.r2 = WithHeadR2(); self.store = m.R2Store('institution', client=self.r2, bucket='private-test')
        self.ledger = RecordingLedger(self.store, None, 'institution', 'https://mineru.net',
                                     {'model': 'vlm', 'language': 'en', 'ocr': True}, [('MINER_U', 'test-token')])
        self.ledger.run_modes = []
        items = {}
        self.sources = []
        for index, name in enumerate(('good', 'bad')):
            path = self.inputs/(name+'.pdf'); path.write_bytes(b'%PDF-fixture-' + name.encode())
            binding = self.ledger.bind(path, path.name); items[name] = binding
            key = 'batches/' + ('a' if name == 'good' else 'b') * 32
            row = {'schema': 1, 'key': key, 'scope': 'institution', 'endpoint': 'https://mineru.net',
                   'options': self.ledger.options, 'token_identity': next(iter(self.ledger.tokens)),
                   'files': [binding], 'state': 'terminal', 'batch_id': name}
            self.store.put(key, row)
            self.store.put('sources/'+binding['id'], {'schema': 1, 'binding': binding, 'batch_key': key})
            self.sources.append((path.resolve(), path.name))
        self.provider = Provider(items); self.ledger.provider = self.provider

    def run_primary(self):
        argv = ['primary', '--input-dir', str(self.inputs), '--output-dir', str(self.output),
                '--chart-source-only', '--provider-outcome-path', str(self.outcome)]
        with (patch.object(sys, 'argv', argv),
              patch.dict(os.environ, {'MINER_U': 'test-token', 'INSTITUTION_DEPENDENCY_BACKLOG': '1'}),
              patch.object(backlog, 'ALLOWED', frozenset({failure_message_hash(ERROR)})),
              patch.object(primary, 'from_environment', return_value=self.ledger),
              patch.object(primary, 'download_once', return_value=result_zip()) as download,
              patch.object(primary, 'download_and_unzip', side_effect=AssertionError('Use source-bound result cache')),
              patch.object(primary, 'create_chart_source_assets', return_value=[]),
              patch.object(primary, 'safe_generate_text', side_effect=AssertionError('No paid copy in source extraction')),
              patch.object(primary, 'log'), patch('sys.stderr', new_callable=io.StringIO)):
            code = primary.main()
            holds = backlog.configured(self.ledger)[1].entries()
        return code, download.call_count, holds

    def test_new_known_failure_defers_one_root_and_releases_complete_sibling(self):
        code, downloads, holds = self.run_primary()
        self.assertEqual(code, 0)
        self.assertEqual(self.ledger.run_modes, [False, True])
        self.assertEqual((self.provider.posts, self.provider.uploads), (0, 0))
        self.assertEqual(downloads, 1)
        self.assertEqual(len(list(self.output.rglob('source_mineru.md'))), 1)
        report = json.loads((self.output/'summary.json').read_text())
        self.assertEqual(len(report), 1)
        self.assertIn('good.pdf', str(report[0]))
        self.assertEqual(json.loads(self.outcome.read_text()),
                         {'schema': 1, 'category': 'institution_dependencies_deferred', 'deferred_sources': 1})
        self.assertEqual(list(holds), ['batches/' + 'b' * 32])
        self.assertEqual(holds['batches/' + 'b' * 32]['status'], 'dependency_hold')
        summary = json.loads((self.output/'mineru_attempts_summary.json').read_text())
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(summary['before_dependency_holds']['failed'], 1)
        self.assertEqual(summary['provider_posts'], 0)

    def test_unknown_terminal_failure_remains_hard_failure_without_partial_release(self):
        self.provider.unknown = True
        code, downloads, holds = self.run_primary()
        self.assertEqual(code, 2)
        self.assertEqual(self.ledger.run_modes, [False])
        self.assertEqual((self.provider.posts, self.provider.uploads, downloads), (0, 0, 0))
        self.assertEqual(holds, {})
        self.assertFalse(list(self.output.rglob('source_mineru.md')))
        if self.outcome.exists():
            self.assertNotEqual(json.loads(self.outcome.read_text()).get('category'), 'institution_dependencies_deferred')

    def test_subset_knobs_reject_before_backlog_access_or_resume_acknowledgements(self):
        for option in (['--shard-index', '1'], ['--shard-count', '2'],
                       ['--max-reports-per-shard', '1'], ['--max-total-reports', '1'], ['--skip-existing', 'true']):
            argv = ['wrapper', '--input-dir', str(self.inputs), '--output-dir', str(self.output),
                    '--skip-existing', 'false', *option]
            with (self.subTest(option=option), patch.object(sys, 'argv', argv),
                  patch.dict(os.environ, {'INSTITUTION_DEPENDENCY_BACKLOG': '1'}),
                  patch.object(backlog, 'cli_ledger') as configure,
                  patch.object(backlog, 'resume') as resume,
                  self.assertRaisesRegex(ValueError, 'complete unsharded')):
                wrapper.main()
            configure.assert_not_called(); resume.assert_not_called()
            self.assertFalse((self.output/'institution-resume-context.json').exists())


if __name__ == '__main__':
    unittest.main()
