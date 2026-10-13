import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import restore_completed_institution_sources as recovery
from institution_dependency_backlog import Backlog
from institution_original_cache import OPTIONS
from mineru_task_ledger import digest, encoded


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.output = Path(self.temporary.name)/'out'
        self.value, _ = recovery.selection('adb-261013')
        self.ledger = Mock(scope='institution', forbid_new_submissions=True)
        self.payloads = {}; self.bindings = []; self.versions = {}; self.claims = {}
        for i, row in enumerate(self.value['sources']):
            payload = f'%PDF-original-{i}'.encode()
            row.update(sha256=digest(payload), bytes=len(payload))
            binding = self.binding(row['local_filename'], payload)
            self.bindings.append(binding); self.payloads[binding['id']] = payload
            self.versions[binding['id']] = {'schema': 1, 'binding': binding,
                'versions': [dict({key: row[key] for key in ('local_filename', 'bytes', 'sha256', 'source_page_url', 'published', 'pdf_url')}, binding_id=binding['id'])],
                'receipts': [{'run_id': self.value['source_run_id'], 'manifest_sha256': 'a'*64}]}
        siblings = [self.binding(f'sibling-{i}.pdf', f'%PDF-sibling-{i}'.encode()) for i in range(4)]
        self.roots = [dict(key=self.value['batches'][0], files=self.bindings[:5]),
                      dict(key=self.value['batches'][1], files=self.bindings[5:]+siblings)]
        for root in self.roots:
            for binding in root['files']:
                self.claims[binding['id']] = {'schema': 1, 'binding': binding, 'batch_key': root['key']}
        self.ledger._read_batch.side_effect = lambda key: (next(row for row in self.roots if row['key'] == key), None)
        self.ledger.store.get.side_effect = lambda key: (self.claims[key.split('/')[1]], None)
        self.ledger.bind.side_effect = lambda path, name: self.binding(name, path.read_bytes())
        self.cache = Mock(); self.cache.get.side_effect = lambda binding: self.payloads[binding['id']]
        self.backlog = Mock(); self.backlog.validate_versions.side_effect = Backlog.validate_versions
        self.backlog._read.side_effect = lambda key: (self.versions[key.split('/')[1][:-5]], None)

    @staticmethod
    def binding(name, raw):
        value = dict(source=name, sha256=digest(raw), size=len(raw), scope='institution', endpoint='https://mineru.net', options=OPTIONS)
        return dict(value, id=digest(encoded(value)))

    def run_restore(self, counts=None):
        if counts is None:
            counts = {'all_succeeded': True, 'completed': 5, 'failed': 0, 'pending': 0}
        with patch.object(recovery, 'read_completed_batch', return_value=({}, counts)) as read:
            result = recovery.restore(self.ledger, self.cache, self.backlog, self.value, self.output)
        return result, read

    def test_only_six_originals_restored_but_all_ten_members_checked(self):
        result, read = self.run_restore()
        self.assertEqual(len(list(self.output.glob('*.pdf'))), 6)
        self.assertEqual(sum(len(call.args[1]['files']) for call in read.call_args_list), 10)
        self.assertEqual(result['recovery']['provider_posts'], 0)
        self.assertEqual(result['downloaded'], self.value['sources'])
        self.ledger.provider.submit.assert_not_called()
        self.ledger.store.put.assert_not_called()

    def test_foreign_producer_or_publication_version_stops_before_provider(self):
        for mutation in ('producer', 'publication', 'claim', 'missing'):
            with self.subTest(mutation=mutation):
                versions, claims = copy.deepcopy(self.versions), copy.deepcopy(self.claims)
                first = self.bindings[0]['id']
                if mutation == 'producer': self.versions[first]['receipts'][0]['run_id'] = 'other'
                if mutation == 'publication': self.versions[first]['versions'][0]['pdf_url'] += '?other'
                if mutation == 'claim': self.claims[first]['batch_key'] = self.value['batches'][1]
                if mutation == 'missing': self.versions[first] = None
                with patch.object(recovery, 'read_completed_batch') as read, self.assertRaises(ValueError):
                    recovery.restore(self.ledger, self.cache, self.backlog, self.value, self.output)
                read.assert_not_called(); self.assertFalse(self.output.exists())
                self.versions, self.claims = versions, claims

    def test_corrupt_original_bytes_stop_before_provider_or_output(self):
        self.payloads[self.bindings[0]['id']] = b'%PDF-changed'
        with patch.object(recovery, 'read_completed_batch') as read, self.assertRaises(ValueError):
            recovery.restore(self.ledger, self.cache, self.backlog, self.value, self.output)
        read.assert_not_called(); self.assertFalse(self.output.exists())

    def test_one_incomplete_original_sibling_blocks_all_selected_outputs(self):
        with self.assertRaisesRegex(ValueError, 'original task incomplete'):
            self.run_restore({'all_succeeded': False, 'completed': 4, 'failed': 0, 'pending': 1})
        self.assertFalse(self.output.exists())

    def test_replay_requires_forbid_new_submissions(self):
        self.ledger.forbid_new_submissions = False
        with self.assertRaisesRegex(ValueError, 'accepted scope'): self.run_restore()
        self.ledger._read_batch.assert_not_called()

    def test_selection_cannot_expand_to_unreviewed_sources(self):
        with self.assertRaisesRegex(ValueError, 'unreviewed'): recovery.selection('anything')
        self.value['sources'].append(copy.deepcopy(self.value['sources'][0]))
        with self.assertRaisesRegex(ValueError, 'selected original identity'): self.run_restore()
        self.assertFalse(self.output.exists())

    def test_workflow_replay_cannot_discover_new_sources_or_resume_other_holds(self):
        text = Path('.github/workflows/institution-latest-pdf-to-wechat.yml').read_text()
        self.assertIn('export MINERU_FORBID_NEW_SUBMISSIONS=1', text)
        self.assertIn('export INSTITUTION_DEPENDENCY_BACKLOG=0', text)
        self.assertIn('restore --selection "$COMPLETED_SOURCE_RECOVERY"\n            exit 0', text)
        self.assertIn('Complete resumed dependencies after private translated handoff', text)
        for name in ['Commit PDF link archive and seen state', 'Set up official IMF download route']:
            block = text.split('- name: '+name, 1)[1].split('- name:', 1)[0]
            self.assertIn("inputs.completed_source_recovery == 'none'", block)


if __name__ == '__main__': unittest.main()
