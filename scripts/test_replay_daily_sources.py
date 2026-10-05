"""Frozen source provenance and the real Daily replay switch; no provider calls."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import textwrap
import unittest

from replay_daily_sources import validate_selection, verify_origin

WORKFLOW = Path(__file__).resolve().parents[1] / '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'


class FrozenSourcesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.pdf = self.root / '01-report.pdf'
        self.pdf.write_bytes(b'%PDF-frozen-original-bytes')
        self.row = {'process_local_path': '/old/runner/01-report.pdf',
                    'dropbox_path': '/zip_backup/261004/report.pdf',
                    'content_sha256': hashlib.sha256(self.pdf.read_bytes()).hexdigest()}
        self.manifest = self.root / 'selected_to_process_manifest.json'
        self.manifest.write_text(json.dumps([self.row]))

    def validate(self, date='261004'):
        return validate_selection(self.root, date, '/zip_backup', '123', 'a'*40, '456', 'b'*40)

    def test_replay_keeps_exact_original_manifest_and_binds_new_upload_context(self):
        raw = self.manifest.read_bytes()
        value = self.validate()
        self.assertEqual(self.manifest.read_bytes(), raw)
        self.assertEqual(value['original_manifest_sha256'], hashlib.sha256(raw).hexdigest())
        self.assertEqual((value['source_run_id'], value['replay_run_id']), ('123', '456'))
        self.assertEqual(value['provider_submission_policy'], 'existing-accepted-only')

    def test_wrong_day_changed_bytes_missing_or_extra_pdf_cannot_replay(self):
        with self.assertRaisesRegex(ValueError, 'context'):
            self.validate('2610041')
        with self.assertRaisesRegex(ValueError, 'date/root'):
            self.validate('261005')
        self.pdf.write_bytes(b'%PDF-changed')
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            self.validate()
        self.pdf.unlink()
        with self.assertRaisesRegex(ValueError, 'inventory'):
            self.validate()
        self.pdf.write_bytes(b'%PDF-frozen-original-bytes')
        (self.root/'additional.pdf').write_bytes(b'%PDF-other')
        with self.assertRaisesRegex(ValueError, 'inventory'):
            self.validate()

    def test_untrusted_or_unfinished_producer_never_reaches_artifact_consumption(self):
        called = []
        def get(path):
            called.append(path)
            return {'id': 123, 'head_branch': 'feature', 'head_sha': 'a'*40}
        with self.assertRaisesRegex(ValueError, 'completed main Daily'):
            verify_origin('123', '261004', 'owner/repo', get=get)
        self.assertEqual(len(called), 2)
        called.clear()
        with self.assertRaisesRegex(ValueError, 'Invalid frozen'):
            verify_origin('123/../../different', '261004', 'owner/repo', get=get)
        self.assertEqual(called, [])


class ReplayWorkflowTests(unittest.TestCase):
    def test_real_input_gate_requires_manual_main_no_force_no_wechat_no_translation(self):
        block = WORKFLOW.read_text().split('- name: Resolve workflow inputs', 1)[1].split('      - name:', 1)[0]
        program = textwrap.dedent(block.split('        run: |\n', 1)[1]).split('echo "dropbox_root=', 1)[0]
        env = {'REPLAY_SOURCE_RUN_ID': '123', 'REPLAY_DATE': '261004', 'REPLAY_FORCE': 'false',
               'REPLAY_WECHAT': 'false', 'REPLAY_TRANSLATIONS': '0', 'REPLAY_LIMIT': '0',
               'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main'}
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'output'
            for changed, success in [({}, True), ({'REPLAY_SOURCE_RUN_ID': '', 'GITHUB_EVENT_NAME': 'schedule'}, True),
                 ({'GITHUB_EVENT_NAME': 'schedule'}, False), ({'GITHUB_REF': 'refs/heads/feature'}, False),
                 ({'REPLAY_FORCE': 'true'}, False), ({'REPLAY_WECHAT': 'true'}, False),
                 ({'REPLAY_TRANSLATIONS': 'all'}, False), ({'REPLAY_LIMIT': '4'}, False),
                 ({'REPLAY_DATE': ''}, False), ({'REPLAY_DATE': '26104'}, False), ({'REPLAY_DATE': '26100x'}, False), ({'REPLAY_SOURCE_RUN_ID': '123;false'}, False)]:
                output.write_text('')
                result = subprocess.run(['bash', '-e', '-c', program],
                    env={**os.environ, **env, **changed, 'GITHUB_OUTPUT': str(output)}, capture_output=True, text=True)
                self.assertEqual(result.returncode == 0, success, (changed, result.stderr))
                if success:
                    expected = '0' if changed.get('REPLAY_SOURCE_RUN_ID') == '' else '1'
                    self.assertIn('forbid_new_submissions=' + expected, output.read_text())

    def test_replay_uses_the_same_current_run_artifact_and_real_downstream_jobs(self):
        workflow = WORKFLOW.read_text()
        self.assertEqual(len(re.findall(r'^      [a-z_]+:$', workflow.split('\npermissions:', 1)[0], re.M)), 25)
        for name in ('Download PDFs from latest Dropbox date folder', 'Select reports with DeepSeek'):
            step = workflow.split('- name: ' + name, 1)[1].split('\n      - name:', 1)[0]
            self.assertIn("needs.resolve-inputs.outputs.replay_source_run_id == ''", step)
        verify = workflow.index('- name: Verify every frozen original byte and replay provenance')
        upload = workflow.index('- name: Upload selected macro PDFs artifact')
        self.assertLess(verify, upload)
        self.assertIn('name: selected-macro-pdfs-${{ github.run_id }}', workflow[upload:])
        self.assertIn('MINERU_FORBID_NEW_SUBMISSIONS: ${{ needs.resolve-inputs.outputs.forbid_new_submissions }}', workflow)
        for name in ('source-outcome', 'recover-market-sources', 'trigger-market-views', 'validate-market-delivery'):
            self.assertIn('\n  ' + name + ':', workflow)
        self.assertNotIn('force_provider_failure', workflow)


if __name__ == '__main__':
    unittest.main()
