"""Real private ledger holds: unchanged no-poll, exact child reuse and handoff."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import institution_dependency_backlog as b
from institution_original_cache import OriginalCache, preserve_sources
import mineru_task_ledger as m
from mineru_completed_child_reuse import reuse_completed_children
from mineru_terminal_recovery import TerminalRecovery, failure_hash
from test_mineru_result_cache import MemoryR2, S3Error
from test_mineru_terminal_recovery import Provider, ERROR, AUTH, OPTIONS


class HeadR2(MemoryR2):
    def __init__(self):
        super().__init__(); self.heads = []
    def head_object(self, **kwargs):
        self.heads.append(kwargs['Key'])
        if kwargs['Key'] not in self.objects: raise S3Error('NoSuchKey', 404)
        value = copy.deepcopy(self.objects[kwargs['Key']]); body = value.pop('Body')
        return dict(value, ContentLength=len(body), ETag=m.digest(body))


class BacklogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name); self.client = HeadR2()
        self.store = m.R2Store('institution', client=self.client, bucket='private-test')
        self.provider = Provider(); self.now = 0
        self.ledger = m.Ledger(self.store, self.provider, 'institution', 'https://mineru.net', OPTIONS,
                              [('MINER_U', 'test-private-token')], clock=lambda: self.now, sleep=self.sleep)
        self.inputs = []
        for i in range(3):
            path = self.folder / f'report-{i}.pdf'; path.write_bytes(b'%PDF-original-' + str(i).encode())
            self.inputs.append((path, path.name))
        self.root_key = self.create_root(self.inputs)
        self.cache = OriginalCache(self.client, 'private-test')
        self.backlog = b.Backlog(self.client, 'private-test')
        allowed = patch.object(b, 'ALLOWED', frozenset({failure_hash(ERROR)})); allowed.start(); self.addCleanup(allowed.stop)

    def sleep(self, seconds): self.now += seconds
    def create_root(self, sources):
        items = [self.ledger.bind(*source) for source in sources]
        return self.ledger._create(items, {item['id']: path for item, (path, _) in zip(items, sources)}, self.now+60)
    def root(self): return self.ledger._read_batch(self.root_key)[0]
    def hold(self):
        eligible, deferred = b.filter_sources(self.ledger, self.inputs)
        self.assertEqual((eligible, deferred), ([], 3))
        return self.backlog.entries()[self.root_key]
    def originals(self): preserve_sources(self.ledger, self.inputs)
    def recover(self):
        return TerminalRecovery(self.ledger, allowed_error_hashes=[failure_hash(ERROR)]).run(
            self.inputs, authorization=AUTH, timeout=60)

    def test_first_hold_is_full_root_and_unchanged_schedule_has_zero_provider_requests(self):
        self.originals(); row = self.hold()
        self.assertEqual(row['counts'], dict(admitted=3, completed=1, failed=2, pending=0))
        self.provider.polls.clear(); self.client.gets.clear(); before_posts = len(self.provider.posts)
        self.assertEqual(b.filter_sources(self.ledger, self.inputs), ([], 3))
        self.assertEqual(b.resume(self.ledger, self.folder/'restored'), ({}, {}, 3))
        self.assertEqual(self.provider.polls, [])
        self.assertEqual(len(self.provider.posts), before_posts)
        self.assertFalse(any(key.endswith('.pdf') for key in self.client.gets))
        self.assertEqual(len(self.backlog.entries()), 1)

    def test_unrelated_new_source_remains_eligible_beside_held_root(self):
        self.hold(); path = self.folder/'fresh.pdf'; path.write_bytes(b'%PDF-fresh')
        self.provider.polls.clear()
        self.assertEqual(b.filter_sources(self.ledger, self.inputs+[(path, 'fresh.pdf')]), ([(path, 'fresh.pdf')], 3))
        self.assertEqual(self.provider.polls, [])

    def test_unknown_error_or_pending_or_truncated_full_inventory_never_becomes_hold(self):
        for plan in (['done','pending','failed'], ['done'], ['done','failed','failed']):
            with self.subTest(plan=plan):
                self.provider.plans[0] = plan
                allow = frozenset() if len(plan) == 3 and 'pending' not in plan else b.ALLOWED
                with patch.object(b, 'ALLOWED', allow):
                    self.assertEqual(b.filter_sources(self.ledger, self.inputs), (self.inputs, 0))
                    self.assertFalse(b.hold_terminal_failure(self.ledger, self.inputs))
                self.assertEqual(self.backlog.entries(), {})

    def test_old_seed_missing_originals_is_visible_and_does_not_fetch_or_submit(self):
        posts = len(self.provider.posts)
        result = b.seed(self.ledger, [self.root_key])
        self.assertEqual(result, dict(status='dependencies_deferred', original_members=3, held_roots=1,
            deferred_sources=3, failed_originals=2, provider_posts=0, source_bytes_proven=False))
        self.provider.polls.clear()
        self.assertEqual(b.resume(self.ledger, self.folder/'restored'), ({}, {}, 3))
        self.assertEqual(self.provider.polls, []); self.assertEqual(len(self.provider.posts), posts)

    def test_new_exact_original_availability_changes_dependency_but_still_failed_root_reholds(self):
        self.hold(); self.originals()
        names, ack, deferred = b.resume(self.ledger, self.folder/'restored')
        self.assertEqual((len(names), len(ack), deferred), (3, 1, 0))
        sources = [(Path(path), source) for path, source in names.items()]
        self.assertEqual(b.filter_sources(self.ledger, sources), ([], 3))
        b.handoff_complete(self.ledger, ack)
        self.assertEqual(self.backlog.entries()[self.root_key]['status'], 'dependency_hold')

    def test_completed_children_resume_exact_originals_generate_then_handoff_clears_only_acknowledged(self):
        self.originals(); self.hold(); self.recover()
        posts = len(self.provider.posts)
        names, ack, deferred = b.resume(self.ledger, self.folder/'restored')
        sources = [(Path(path), source) for path, source in names.items()]
        self.assertEqual((len(sources), deferred), (3, 0))
        for path, source in sources:
            original = next(p for p, name in self.inputs if name == source)
            self.assertEqual(path.read_bytes(), original.read_bytes())
        eligible, held = b.filter_sources(self.ledger, sources)
        self.assertEqual((eligible, held), (sources, 0))
        rows, summary = self.ledger.run(eligible, timeout=60)
        rows, summary = reuse_completed_children(self.ledger, eligible, rows, summary)
        self.assertTrue(summary['ready_for_generation']); self.assertEqual(len(rows), 3)
        self.assertEqual(summary['completed_child_reuse']['reused_sources'], 2)
        self.assertEqual(len(self.provider.posts), posts)
        self.assertIn(self.root_key, self.backlog.entries())  # not done until translated private handoff
        b.handoff_complete(self.ledger, ack)
        self.assertEqual(self.backlog.entries(), {})
        self.assertTrue(any(key.startswith(b.PREFIX+'records/') for key in self.client.objects))

    def test_mixed_complete_and_known_failed_roots_hold_only_failed_root(self):
        self.provider.plans[0] = ['done'] * 3
        path = self.folder/'other.pdf'; path.write_bytes(b'%PDF-other')
        other = [(path, path.name)]; key = self.create_root(other)
        self.provider.plans[1] = ['failed']
        self.assertTrue(b.hold_terminal_failure(self.ledger, self.inputs+other))
        self.assertEqual(set(self.backlog.entries()), {key})
        self.assertEqual(b.filter_sources(self.ledger, self.inputs+other), (self.inputs, 1))

    def test_mixed_known_and_pending_roots_do_not_write_partial_holds(self):
        path = self.folder/'pending.pdf'; path.write_bytes(b'%PDF-pending')
        other = [(path, path.name)]; self.create_root(other); self.provider.plans[1] = ['pending']
        self.assertFalse(b.hold_terminal_failure(self.ledger, self.inputs+other))
        self.assertEqual(self.backlog.entries(), {})

    def test_source_claim_mismatch_stops_before_provider_poll(self):
        binding = self.ledger.bind(*self.inputs[0]); key = 'sources/'+binding['id']
        claim, version = self.store.get(key); claim['binding']['sha256'] = '0'*64; self.store.put(key, claim, version)
        with self.assertRaises(m.LedgerError): self.hold()
        self.assertEqual(self.provider.polls, [])

    def test_bad_original_metadata_stops_resume_without_provider_poll(self):
        self.hold(); self.originals(); binding = self.ledger.bind(*self.inputs[0])
        self.client.objects[self.cache.key(binding)]['Metadata']['kind'] = 'wrong'
        self.provider.polls.clear()
        with self.assertRaisesRegex(m.LedgerError, 'availability mismatch'): b.resume(self.ledger, self.folder/'restored')
        self.assertEqual(self.provider.polls, [])

    def test_handoff_cannot_clear_a_hold_or_a_changed_resuming_record(self):
        row = self.hold(); checksum = m.digest(m.encoded(row))
        with self.assertRaisesRegex(m.LedgerError, 'not resumed'):
            b.handoff_complete(self.ledger, {self.root_key: checksum})
        self.originals(); self.recover()
        _, ack, _ = b.resume(self.ledger, self.folder/'restored')
        current = self.backlog.entries()[self.root_key]
        changed = dict(current, dependency_sha256='f'*64); self.backlog.save(changed)
        b.handoff_complete(self.ledger, ack)
        self.assertEqual(self.backlog.entries()[self.root_key], changed)

    def test_record_contract_rejects_wrong_counts_unknown_hash_duplicate_and_bool_schema(self):
        row = self.hold()
        variants = [dict(row, schema=True), dict(row, failure_hashes=['0'*64]),
                    dict(row, counts=dict(row['counts'], admitted=True)),
                    dict(row, counts=dict(row['counts'], pending=1)), dict(row, files=[row['files'][0]]*3)]
        before = len(self.client.puts)
        for value in variants:
            with self.subTest(value=value), self.assertRaises(m.LedgerError): self.backlog.save(value)
        self.assertEqual(len(self.client.puts), before)

    def test_ambiguous_backlog_write_stops_without_readback_or_retry(self):
        row = b.known_hold(self.ledger, self.root(), self.cache)
        before = len(self.client.puts)
        def fail(key, request): raise TimeoutError('private-url')
        self.client.after_put = fail
        with self.assertRaises(TimeoutError): self.backlog.save(row)
        self.assertEqual(len(self.client.puts), before+1)
        self.assertNotIn(b.PREFIX+'active.json', self.client.objects)
        self.assertEqual(self.client.gets[-1], b.PREFIX+'records/'+m.digest(m.encoded(row))+'.json')

    def test_conditional_index_conflict_keeps_previous_hold_visible(self):
        row = self.hold(); changed = dict(row, dependency_sha256='f'*64)
        actual = self.client.put_object
        def conflict(**request):
            if request['Key'] == b.PREFIX+'active.json': raise S3Error('PreconditionFailed', 412)
            return actual(**request)
        with patch.object(self.client, 'put_object', side_effect=conflict), self.assertRaises(S3Error):
            self.backlog.save(changed)
        self.assertEqual(self.backlog.entries()[self.root_key], row)

    def test_resume_count_bound_never_selects_partial_root_or_acknowledges_it(self):
        self.hold(); self.originals()
        with patch.object(b, 'MAX_RESUME_SOURCES', 2):
            self.assertEqual(b.resume(self.ledger, self.folder/'restored'), ({}, {}, 3))
        self.assertEqual(self.backlog.entries()[self.root_key]['status'], 'dependency_hold')

    def test_publication_versions_are_bound_durable_and_collision_history_retained(self):
        binding = self.ledger.bind(*self.inputs[0])
        row = dict(binding_id=binding['id'], local_filename=binding['source'], bytes=binding['size'],
                   sha256=binding['sha256'], published='2026-10-08', source_page_url='https://www.imf.org/report',
                   pdf_url='https://www.imf.org/report.pdf', feed_pdf_candidates=['https://www.imf.org/report.pdf'])
        self.backlog.save_versions([binding], [row], [{'run_id': '123', 'manifest_sha256': 'a'*64}])
        puts = len(self.client.puts)
        self.backlog.save_versions([binding], [row], [{'run_id': '123', 'manifest_sha256': 'a'*64}])
        self.assertEqual(len(self.client.puts), puts)
        for index in range(40):
            self.backlog.save_versions([binding], [row], [{'run_id': str(1000+index), 'manifest_sha256': 'b'*64}])
        self.assertEqual(len(self.client.puts), puts)
        stored, _ = self.backlog._read('versions/'+binding['id']+'.json')
        self.assertEqual(len(stored['receipts']), 1)
        newer = dict(row, pdf_url='https://www.imf.org/new.pdf')
        self.backlog.save_versions([binding], [newer], [])
        self.assertEqual(self.backlog.versions([binding]), [row, newer])
        with self.assertRaises(m.LedgerError):
            self.backlog.save_versions([binding], [dict(row, bytes=1)], [])

    def test_new_source_requires_exact_manifest_before_provider_admission(self):
        path = self.folder/'new.pdf'; path.write_bytes(b'%PDF-new')
        sources = [(path, path.name)]
        with patch.dict(b.os.environ, {}, clear=True):
            with self.assertRaisesRegex(m.LedgerError, 'lacks publication provenance'):
                b.preserve_manifest_versions(self.ledger, sources)
        binding = self.ledger.bind(*sources[0]); manifest = self.folder/'manifest.json'
        row = dict(local_filename=path.name, sha256=binding['sha256'], bytes=binding['size'],
                   published='2026-10-08', source_page_url='https://www.imf.org/report',
                   pdf_url='https://www.imf.org/report.pdf', feed_pdf_candidates=[])
        manifest.write_text(json.dumps({'downloaded': [row]}))
        with patch.dict(b.os.environ, {'INSTITUTION_SOURCE_MANIFEST': str(manifest)}):
            b.preserve_manifest_versions(self.ledger, sources)
        self.assertEqual(self.backlog.versions([binding])[0]['sha256'], binding['sha256'])
        self.assertEqual(len(self.provider.posts), 1)

    def test_translated_handoff_requires_every_generated_source_not_a_capped_subset(self):
        extracted = self.folder/'extracted'; translated = self.folder/'translated'; translated.mkdir()
        reports = []
        for i in range(2):
            source = extracted/str(i); source.mkdir(parents=True); (source/'source_mineru.md').write_text('source')
            output = translated/str(i); output.mkdir(); pdf = output/'report.pdf'; pdf.write_bytes(b'%PDF-valid')
            reports.append(dict(source_report_dir=str(source), output_dir=str(output), pdf_path=str(pdf)))
        payload = dict(selected_count=2, successful_count=2, failures=[], reports=reports)
        path = translated/'translation_summary.json'; path.write_text(json.dumps(payload))
        self.assertEqual(b.verify_handoff(extracted, translated), 2)
        for value in (dict(payload, selected_count=1, successful_count=1, reports=reports[:1]),
                      dict(payload, reports=[reports[0], reports[0]]), dict(payload, failures=[{}])):
            path.write_text(json.dumps(value))
            with self.assertRaises(m.LedgerError): b.verify_handoff(extracted, translated)


if __name__ == '__main__': unittest.main()
