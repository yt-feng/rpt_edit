"""Real 40-source delivery, old provider failures and complete segment receipts."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from mineru_task_ledger import FileStore, Ledger, LedgerError, digest, encoded
from mineru_terminal_recovery import TerminalRecovery
from mineru_result_cache import ResultCache
from test_mineru_result_cache import MemoryR2
from test_mineru_page_segments import pdf, result_zip
from test_recover_durable_mineru_sources import assets, result_zip as plain_zip
import mineru_page_segments as segments
import recover_durable_mineru_sources as recovery
import pdf_to_xhs_batch as primary


class Provider:
    def __init__(self):
        self.tasks, self.states, self.uploads = {}, {}, {}
        self.posts, self.polls, self.downloads = [], [], []
        self.events = []
    def submit(self, items, options, token, timeout):
        bid = 'derived-' + str(len(self.posts) + 1)
        self.posts.append(copy.deepcopy(items)); self.events.append('post')
        self.tasks[bid] = copy.deepcopy(items)
        return bid, ['https://upload.invalid/'+bid+'/'+item['id'] for item in items]
    def upload(self, url, raw, timeout):
        self.uploads[url.rsplit('/', 1)[-1]] = raw
    def poll(self, bid, token, timeout):
        self.polls.append(bid); self.events.append('get')
        result = []
        for item in self.tasks[bid]:
            state = self.states.get(item['id'], 'done')
            result.append({'data_id': item['id'], 'state': state,
                **({'full_zip_url': 'https://results.invalid/'+item['id']} if state == 'done'
                   else {'err_code': 'TEST_FAILURE', 'err_msg': 'The number of pages exceeds the limit.'
                         if item['source'] == 'R037.pdf' else 'fixed historical failure'})})
        return result
    def download(self, url):
        sid = url.rsplit('/', 1)[-1]
        self.downloads.append(sid); self.events.append('zip')
        return result_zip(self.uploads[sid]) if sid in self.uploads else plain_zip()


class SegmentedDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.inputs = self.root/'inputs'; self.inputs.mkdir()
        self.output = self.root/'output'
        self.provider = Provider(); self.store = FileStore(self.root/'ledger')
        self.ledger = Ledger(self.store, self.provider, 'dropbox', 'https://mineru.net', recovery.OPTIONS,
                             [('MINER_U', 'test-secret')], sleep=lambda _: None)
        self.cache = ResultCache(MemoryR2(), 'private')
        self.pairs, manifest = [], []
        for i in range(40):
            path = self.inputs/f'R{i+1:03d}.pdf'; pdf(path, 202 if i == 36 else 1)
            self.pairs.append((path, path.name))
            manifest.append({'process_local_path': path.name, 'content_sha256': digest(path.read_bytes()),
                'dropbox_path': '/zip_backup/261009/'+path.name, 'name': path.name})
        self.manifest = self.inputs/recovery.MANIFEST; self.manifest.write_bytes(encoded(manifest))
        self.originals = []
        for i in range(0, 40, 5):
            items = [self.ledger.bind(*pair) for pair in self.pairs[i:i+5]]
            key = 'batches/'+f'{i+1:032x}'; bid = 'root-'+str(i)
            batch = {'schema': 1, 'key': key, 'scope': 'dropbox', 'endpoint': 'https://mineru.net',
                'options': recovery.OPTIONS, 'token_identity': next(iter(self.ledger.tokens)),
                'files': items, 'state': 'accepted', 'batch_id': bid}
            self.store.put(key, batch); self.originals.append(batch); self.provider.tasks[bid] = items
            for item in items:
                self.store.put('sources/'+item['id'], {'schema': 1, 'binding': item, 'batch_key': key})
                if item['source'] != 'R037.pdf':
                    lineage = {'batch_key': key, 'batch_id': bid, 'parent_batch_key': key,
                        'data_id': item['id'], 'child_ordinal': 0}
                    self.cache.put(item, lineage, plain_zip())
        self.long = self.ledger.bind(*self.pairs[36]); self.provider.states[self.long['id']] = 'failed'
    def recover(self, **kwargs):
        options = dict(source_run_id='123', recovery_run_id='456', source_execution_sha='a'*40,
            result_cache=self.cache, downloader=self.provider.download, asset_writer=assets, timeout=30, interval=1)
        options.update(kwargs)
        return recovery.recover_sources(self.ledger, self.inputs, self.manifest, self.output, 40, '261009', **options)
    def original_snapshot(self):
        return {str(path.relative_to(self.store.root)): path.read_bytes() for path in self.store.root.rglob('*.json')}
    def test_39_cached_results_plus_two_segments_produce_40_sources_and_replay_zero_posts(self):
        before = self.original_snapshot()
        receipt = self.recover()
        self.assertEqual((receipt['schema_version'], receipt['report_count'], receipt['provider_posts']), (2, 40, 2))
        self.assertEqual(len(self.provider.downloads), 2)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertTrue(all(len(items) == 1 and items[0]['source'].startswith('_mineru-page-segments/')
                            for items in self.provider.posts))
        for name, raw in before.items(): self.assertEqual((self.store.root/name).read_bytes(), raw)
        checked = recovery.validate_sources(self.output, 40, '261009')
        row = checked['reports'][36]
        self.assertEqual(row['delivery']['kind'], 'page_segments')
        self.assertEqual(row['delivery']['original_provider_state'], 'failed')
        self.assertEqual(row['task']['batch_id'], 'root-35')
        status = json.loads((self.output/row['directory']/'status.json').read_bytes())
        self.assertEqual(status['mineru_state'], 'segmented_complete')
        self.assertEqual([x['page_start'] for x in row['delivery']['receipt']['segments']], [1, 201])
        shutil.rmtree(self.output)
        def no_download(_): self.fail('All complete ZIPs should be cached')
        self.assertEqual(self.recover(downloader=no_download)['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 2)
    def test_three_exhausted_historical_children_remain_byte_identical(self):
        terminal = TerminalRecovery(self.ledger, automatic=True, daily_retry_limit=3)
        with patch('mineru_terminal_recovery.page_limit_failure', return_value=False):
            terminal.run(self.pairs[35:40], authorization={'run_id':'456', 'manifest_sha256':digest(self.manifest.read_bytes())},
                timeout=20, interval=1, queue_budget=0, partial=True)
        self.assertEqual(len(self.provider.posts), 3)
        before = self.original_snapshot()
        receipt = self.recover()
        self.assertEqual((receipt['provider_posts'], len(self.provider.posts)), (2, 5))
        self.assertEqual(receipt['reports'][36]['task']['child_ordinal'], 3)
        for name, raw in before.items(): self.assertEqual((self.store.root/name).read_bytes(), raw)
    def test_unrelated_missing_claim_or_corrupt_controller_blocks_before_any_post(self):
        first = self.ledger.bind(*self.pairs[0])
        claim = self.store.root/('sources/'+first['id']+'.json'); raw = claim.read_bytes(); claim.unlink()
        with self.assertRaisesRegex(recovery.RecoveryError, 'missing_original_claim'): self.recover()
        self.assertEqual((self.provider.posts, self.provider.polls), ([], []))
        claim.write_bytes(raw)
        self.store.put('recoveries/'+self.originals[0]['key'].split('/')[1], {'schema':1,'policy':'bad'})
        with self.assertRaises(LedgerError): self.recover()
        self.assertEqual((self.provider.posts, self.provider.polls), ([], []))
    def test_ambiguous_legacy_child_cannot_authorize_new_physical_segment_tasks(self):
        terminal = TerminalRecovery(self.ledger, automatic=True, daily_retry_limit=3)
        with patch('mineru_terminal_recovery.page_limit_failure', return_value=False):
            terminal.run(self.pairs[35:40], authorization={'run_id':'456', 'manifest_sha256':digest(self.manifest.read_bytes())},
                timeout=20, interval=1, queue_budget=0, partial=True)
        controller, _ = self.store.get('recoveries/'+self.originals[7]['key'].split('/')[1])
        key = controller['children'][0]['key']
        child, version = self.store.get(key)
        child.update(state='submitting', batch_id=None)
        self.store.put(key,child,version)
        posts, polls = len(self.provider.posts),len(self.provider.polls)
        with self.assertRaisesRegex(recovery.RecoveryError,'saved_submission_ambiguous'): self.recover()
        self.assertEqual((len(self.provider.posts),len(self.provider.polls)),(posts,polls))
        self.assertFalse(self.output.exists())

    def test_unrelated_pending_or_failed_member_never_admits_segments_or_handoff(self):
        first = self.ledger.bind(*self.pairs[0])
        for state in ('running', 'failed'):
            self.provider.states[first['id']] = state
            with self.subTest(state=state), self.assertRaises((recovery.RecoveryError,LedgerError)):
                self.recover()
            self.assertEqual(self.provider.posts, [])
            self.assertFalse(self.output.exists())
    def test_independent_short_failure_keeps_daily_bounded_recovery_with_long_pdf(self):
        import recover_daily_mineru_sources as daily
        first = self.ledger.bind(*self.pairs[0]); self.provider.states[first['id']] = 'failed'
        original_poll = self.provider.poll
        def poll(bid, token, timeout):
            rows = original_poll(bid,token,timeout)
            if bid.startswith('derived-'):
                for row in rows:
                    if row['data_id'] == first['id']:
                        row.clear(); row.update(data_id=first['id'],state='done',full_zip_url='https://results.invalid/'+first['id'])
            return rows
        self.provider.poll = poll
        # A normal recovery child has a PDF upload but uses the ordinary result fixture.
        original_download = self.provider.download
        def download(url):
            return plain_zip() if url.endswith('/'+first['id']) else original_download(url)
        receipt = self.recover(terminal_factory=daily.terminal_for_original,continue_batches=True,downloader=download)
        self.assertEqual((receipt['report_count'],receipt['provider_posts']),(40,3))
        self.assertEqual(receipt['reports'][0]['task']['child_ordinal'],1)
        self.assertEqual(receipt['reports'][36]['delivery']['kind'],'page_segments')

    def test_segment_failure_preserves_completed_segment_and_never_hands_off_partial_source(self):
        plan = segments.prepare_segments(self.ledger, *self.pairs[36], self.root/'parts')
        self.provider.states[plan['segments'][1]['binding']['id']] = 'failed'
        for _ in range(2):
            with self.assertRaisesRegex(LedgerError, 'segment parsing incomplete'): self.recover()
            self.assertFalse(self.output.exists())
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(self.provider.downloads), 1)
    def test_receipt_page_gap_provider_success_forgery_and_missing_report_rejected(self):
        receipt = self.recover(); receipt_path = self.output/recovery.RECEIPT
        for edit in (
            lambda x: x['reports'][36]['delivery']['receipt']['segments'][1].update(page_start=200),
            lambda x: x['reports'][36]['delivery'].update(original_provider_state='done'),
            lambda x: x['reports'].pop(),
            lambda x: x['segmented_originals'].append(self.long['id'])):
            changed = copy.deepcopy(receipt); edit(changed); receipt_path.write_bytes(encoded(changed))
            with self.assertRaises((LedgerError, recovery.RecoveryError)):
                recovery.validate_sources(self.output, 40, '261009')
        receipt_path.write_bytes(encoded(receipt))
    def test_current_original_bytes_changed_rejects_before_provider_calls(self):
        self.pairs[36][0].write_bytes(b'%PDF changed')
        with self.assertRaisesRegex(recovery.RecoveryError, 'input_pdf_hash'): self.recover()
        self.assertEqual((self.provider.posts, self.provider.polls), ([], []))
    def test_primary_reuses_completed_segments_of_failed_original_with_zero_new_posts(self):
        self.recover()
        posts = len(self.provider.posts)
        with patch.object(primary,'download_result',side_effect=AssertionError('Complete segment ZIPs must be cached')):
            rows, summary = primary.run_source_batch(self.ledger,self.pairs[35:40],timeout=20,result_cache=self.cache)
        self.assertEqual((summary['completed'],summary['failed'],summary['provider_posts']),(5,0,0))
        self.assertEqual(summary['original_outcomes']['failed'],1)
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(dict(rows)[self.pairs[36][0]]['state'],'segmented_complete')
        self.assertEqual(len(self.provider.posts),posts)

    def test_existing_long_replay_can_share_producer_batch_with_fresh_short_source(self):
        self.recover()
        path = self.root/'fresh-short.pdf'; pdf(path,1)
        posts = len(self.provider.posts)
        selected = self.pairs[35:39]+[(path,path.name)]
        with patch.object(primary,'download_result',side_effect=AssertionError('Segment ZIPs already cached')):
            rows, summary = primary.run_source_batch(self.ledger,selected,timeout=20,result_cache=self.cache)
        self.assertEqual((summary['completed'],summary['provider_posts']),(5,1))
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(set(dict(rows)),{value[0] for value in selected})
        self.assertEqual(len(self.provider.posts)-posts,1)
        self.assertEqual(self.provider.posts[-1][0]['source'],'fresh-short.pdf')

    def test_new_producer_splits_before_submission_and_reuses_accepted_segments(self):
        new_path = self.root/'new.pdf'; pdf(new_path, 202)
        before = len(self.provider.posts)
        with patch.object(primary, 'download_result', side_effect=lambda url, **_: (self.provider.download(url), None)):
            rows, summary = primary.run_source_batch(self.ledger, [(new_path,new_path.name)], timeout=20,
                                                    result_cache=self.cache)
            self.assertTrue(summary['ready_for_generation'])
            self.assertEqual((summary['completed'], summary['provider_posts']), (1,2))
            self.assertEqual(rows[0][1]['state'], 'segmented_complete')
            binding = self.ledger.bind(new_path,new_path.name)
            self.assertIsNone(self.store.get('sources/'+binding['id'])[0])
            self.assertEqual(len(self.provider.posts)-before,2)
            rows, summary = primary.run_source_batch(self.ledger, [(new_path,new_path.name)], timeout=20,
                                                    result_cache=self.cache)
            self.assertEqual(summary['provider_posts'],0)
    def test_segmented_process_pdf_replaces_validated_raw_directory_on_repeat(self):
        self.recover()
        with patch.object(primary,'download_result',side_effect=AssertionError('Cache required')):
            rows, _ = primary.run_source_batch(self.ledger,self.pairs[35:40],timeout=20,result_cache=self.cache)
        source, _ = self.pairs[36]; row = dict(rows)[source]
        output = self.root/'primary-output'
        args = primary.build_arg_parser().parse_args(['--input-dir',str(self.inputs),'--output-dir',str(output),
                                                       '--chart-source-only','--keep-mineru-raw'])
        with patch.object(primary,'create_chart_source_assets',return_value=[]):
            first = primary.process_pdf(source,row,output,args)
            raw = output/primary.slug(source.name)/'mineru_raw'
            (raw/'stale.txt').write_text('must disappear')
            second = primary.process_pdf(source,row,output,args)
        self.assertEqual((first['mineru_state'],second['mineru_state']),('segmented_complete','segmented_complete'))
        self.assertFalse((raw/'stale.txt').exists())
        self.assertEqual(first['source_delivery'],second['source_delivery'])

    def test_existing_frozen_standalone_plan_resumes_only_missing_second_segment(self):
        path,source = self.pairs[36]
        standalone_dir = self.root/'partial'; standalone_dir.mkdir()
        standalone_pdf = standalone_dir/source; shutil.copy2(path,standalone_pdf)
        manifest = json.loads(self.manifest.read_bytes())[36:37]
        standalone_manifest = standalone_dir/recovery.MANIFEST; standalone_manifest.write_bytes(encoded(manifest))
        ledger = Ledger(FileStore(self.root/'partial-ledger'),self.provider,'dropbox','https://mineru.net',
                        recovery.OPTIONS,[('MINER_U','test-secret')])
        directory = self.root/'partial-parts'
        plan = segments.prepare_segments(ledger,standalone_pdf,source,directory)
        first = plan['segments'][0]
        ledger.run([(directory/Path(first['binding']['source']).name,first['binding']['source'])],timeout=20,interval=1)
        self.assertEqual(len(self.provider.posts),1)
        output = self.root/'partial-output'
        arguments = dict(source_run_id='123',recovery_run_id='456',source_execution_sha='a'*40,result_cache=self.cache,
            downloader=self.provider.download,asset_writer=assets,timeout=20,interval=1)
        ledger.forbid_new_submissions=True
        before = len(self.provider.polls)
        with self.assertRaisesRegex(LedgerError,'segment claim missing'):
            recovery.recover_sources(ledger,standalone_dir,standalone_manifest,output,1,'261009',**arguments)
        self.assertEqual(len(self.provider.polls),before)
        ledger.forbid_new_submissions=False
        receipt = recovery.recover_sources(ledger,standalone_dir,standalone_manifest,output,1,'261009',**arguments)
        self.assertEqual((receipt['report_count'],receipt['provider_posts'],len(self.provider.posts)),(1,1,2))
        self.assertIsNone(ledger.store.get('sources/'+self.long['id'])[0])

    def test_all_long_sources_validate_without_any_original_provider_root(self):
        path, source = self.pairs[36]
        standalone_dir = self.root/'standalone'; standalone_dir.mkdir()
        standalone_pdf = standalone_dir/source; shutil.copy2(path,standalone_pdf)
        manifest = json.loads(self.manifest.read_bytes())[36:37]
        standalone_manifest = standalone_dir/recovery.MANIFEST; standalone_manifest.write_bytes(encoded(manifest))
        # A distinct ledger models a new producer which has never submitted the original.
        ledger = Ledger(FileStore(self.root/'standalone-ledger'),self.provider,'dropbox','https://mineru.net',
                        recovery.OPTIONS,[('MINER_U','test-secret')])
        segments.run_segments(ledger,standalone_pdf,source,self.root/'standalone-parts',result_cache=self.cache,
                              downloader=self.provider.download,timeout=20,interval=1)
        output = self.root/'standalone-output'
        receipt = recovery.recover_sources(ledger,standalone_dir,standalone_manifest,output,1,'261009',
            source_run_id='123',recovery_run_id='456',source_execution_sha='a'*40,result_cache=self.cache,
            downloader=self.provider.download,asset_writer=assets,timeout=20,interval=1)
        self.assertEqual(receipt['original_tasks'],[])
        self.assertEqual(receipt['segmented_originals'],[self.long['id']])
        self.assertEqual(recovery.validate_sources(output,1,'261009')['report_count'],1)

    def test_future_standalone_segment_plan_replays_without_original_provider_claim(self):
        # Rebuild original root membership to the four actual provider sources,
        # representing a producer which split the long PDF before submission.
        root = self.originals[7]; updated = copy.deepcopy(root)
        updated['files'] = [item for item in root['files'] if item['id'] != self.long['id']]
        _, version = self.store.get(root['key']); self.store.put(root['key'],updated,version)
        self.provider.tasks[root['batch_id']] = updated['files']
        (self.store.root/('sources/'+self.long['id']+'.json')).unlink()
        with self.assertRaisesRegex(recovery.RecoveryError, 'missing_original_claim'): self.recover()
        segments.run_segments(self.ledger, *self.pairs[36], self.root/'parts', result_cache=self.cache,
                              downloader=self.provider.download, timeout=20, interval=1)
        result = self.recover()
        self.assertEqual(result['segmented_originals'],[self.long['id']])
        self.assertIsNone(result['reports'][36]['task'])
        self.assertIsNone(result['reports'][36]['delivery']['original_provider_state'])
        self.assertEqual(result['provider_posts'],0)


if __name__ == '__main__': unittest.main(verbosity=2)
