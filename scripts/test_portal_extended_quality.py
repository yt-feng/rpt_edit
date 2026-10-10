"""Quality debt remains visible after render dedup and publication ACKs."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from build_portal_extended_locales import build
from portal_extended_continuation import acknowledge_published, partition_stopped_locales, pending, queue, register
from portal_extended_handoff import next_registered_batch, pending_batch, read_handoff, save_handoff
from portal_extended_incremental import prepare, read_state, remember_candidate, remember_checkpoint, write_state
from portal_extended_locales import ExpansionError, digest, make_corpus, stable_bytes
from portal_extended_quality import (candidate_quality, debt_rows, handoff_quality, proof_key, quality_fields,
                                     quality_summary, record_quality, verify_quality)
from portal_extended_r2 import R2NotFound, R2Store
from test_portal_extended_incremental import DAY, URL, daily_doc, raw_page
from test_portal_extended_locales import FakeTranslator
from test_portal_extended_r2 import FakeR2
from test_repair_portal_french_source_fallback import OriginalRejected

PRODUCER = {'run_id': '1', 'attempt': '1', 'sha': 'a' * 40}
BODY = '<h1>Public research</h1><p>Revenue USD10m.</p><p>Profit USD2m.</p>'


class Accepted(FakeTranslator):
    def translate(self, text, target, source=None, *, markdown=True):
        if 'USD' in text:
            self.calls += 1
            return text.replace('Revenue', 'Chiffre d’affaires').replace('Profit', 'Bénéfice')
        return super().translate(text, target, source, markdown=markdown)


class QualityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store = R2Store(FakeR2(), 'private', '_extended-locales/staging/quality')
        self.corpus = make_corpus([daily_doc(body=BODY), daily_doc(URL.replace('new', 'second'), body=BODY)])
        self.generation = self.corpus['documents_sha256']
        self.store.put_source(self.corpus)
        self.active = [{'generation': 'a' * 64, 'candidates': {'fr': 'b' * 64, 'pt': 'c' * 64}}]
        self.number = 0

    def candidate(self, locale='fr', *, rejected=True, registered=False):
        self.number += 1
        if registered:
            register(self.store, self.corpus, (locale,), PRODUCER)
        work = self.root / str(self.number)
        translator = OriginalRejected() if rejected else Accepted()
        manifest = build(self.corpus, locale, work/'candidate', work/'memo.json', translator,
                         allow_source_fallback=True)
        remember_checkpoint(self.store, locale, self.generation, work/'memo.json')
        result = remember_candidate(self.store, locale, self.corpus, work/'candidate')
        return result, manifest, translator, work

    def test_two_pages_two_fallbacks_stay_done_for_inference_but_not_publication(self):
        result, manifest, translator, work = self.candidate(registered=True)
        self.assertTrue(result['ready']); self.assertFalse(result['translation_ready'])
        self.assertEqual((manifest['completed_page_count'], manifest['source_fallback_unit_count']), (2, 2))
        self.assertEqual(len(manifest['source_fallback_unit_sha256']), 2)
        before = translator.calls
        report = prepare(self.store, self.corpus['documents'], ('fr',), DAY, self.root/'unused.json')
        self.assertFalse(report['has_work']); self.assertEqual(report['pending_page_count'], 0)
        self.assertEqual(report['quality_debt_source_fallback_units'], 2)
        self.assertEqual(report['quality_debt_automatic_retries'], 0)
        self.assertIsNone(pending(self.store, ('fr',), self.root/'never.json'))
        self.assertEqual(queue(self.store, 'fr')[self.generation]['status'], 'complete')
        selected = pending_batch(self.store, self.corpus, 'fr', 'fr', self.active, self.root/'handoff')
        self.assertEqual(selected['candidates'], {})
        self.assertIsNone(next_registered_batch(self.store, 'fr', 'fr', self.active, self.root/'registered'))
        self.assertEqual(translator.calls, before)
        # Re-rendering uses the same durable rejected units, never another call.
        replay = OriginalRejected()
        rebuilt = build(self.corpus, 'fr', work/'replay', work/'memo.json', replay, allow_source_fallback=True)
        self.assertEqual(replay.calls, 0)
        self.assertEqual(rebuilt['files_sha256'], manifest['files_sha256'])

    def test_ready_locale_drains_without_incomplete_sibling(self):
        register(self.store, self.corpus, ('fr', 'pt'), PRODUCER)
        bad, _, _, _ = self.candidate('fr')
        good, _, _, _ = self.candidate('pt', rejected=False)
        batch, corpus = next_registered_batch(self.store, 'fr,pt', 'fr,pt', self.active, self.root/'mixed')
        self.assertEqual(batch['candidates'], {'pt': good['candidate_id']})
        receipt = read_handoff(self.store, save_handoff(self.store, batch, day=DAY, pages=2, producer=PRODUCER))
        self.assertEqual(set(handoff_quality(self.store, receipt)), {'pt'})
        self.assertEqual(corpus, self.corpus)
        self.assertEqual(quality_summary(self.store, ('fr', 'pt'))['quality_debt_locale_count'], 1)
        with self.assertRaises(ExpansionError):
            save_handoff(self.store, {'generation': self.generation, 'candidates': {'fr': bad['candidate_id']}},
                         day=DAY, pages=2, producer=PRODUCER)

    def test_legacy_active_fallback_ack_preserves_debt_and_completed_pages(self):
        result, _, _, _ = self.candidate(registered=True)
        # Model an earlier release that already activated fallback content.
        write_state(self.store, 'quality-debt', 'fr', {'generations': {}})
        completed = copy.deepcopy(read_state(self.store, 'completed', 'fr', DAY))
        active = [{'generation': self.generation, 'candidates': {'fr': result['candidate_id']}}]
        acknowledge_published(self.store, ('fr',), active)
        self.assertEqual(queue(self.store, 'fr'), {})
        self.assertEqual(read_state(self.store, 'completed', 'fr', DAY), completed)
        self.assertEqual(quality_summary(self.store, ('fr',))['quality_debt_source_fallback_units'], 2)
        self.assertEqual(active[0]['candidates']['fr'], result['candidate_id'])

    def test_prepare_backfills_old_debt_without_reopening_completed_cursor(self):
        self.candidate(registered=True)
        write_state(self.store, 'quality-debt', 'fr', {'generations': {}})
        before = copy.deepcopy(queue(self.store, 'fr'))
        eligible, stopped = partition_stopped_locales(self.store, ('fr',))
        self.assertEqual((eligible, stopped), (('fr',), []))
        self.assertEqual(queue(self.store, 'fr'), before)
        self.assertEqual(quality_summary(self.store, ('fr',))['quality_debt_source_fallback_units'], 2)

    def test_proof_and_debt_replay_write_nothing_and_leak_no_source(self):
        result, _, _, _ = self.candidate()
        before = copy.deepcopy(self.store.client.objects)
        proof = record_quality(self.store, 'fr', self.generation, result['candidate_id'])
        self.assertEqual(self.store.client.objects, before)
        text = json.dumps(proof) + json.dumps(quality_summary(self.store, ('fr',)))
        for source in ('Revenue', 'Profit', 'USD', URL): self.assertNotIn(source, text)
        self.assertEqual(len(proof['source_fallback_unit_sha256']), 2)

    def test_full_recovery_clears_only_same_generation_debt(self):
        self.candidate()
        old = copy.deepcopy(debt_rows(self.store, 'fr'))
        other = 'd' * 64
        write_state(self.store, 'quality-debt', 'fr', {'generations': {**old, other: next(iter(old.values()))}})
        ready, _, _, _ = self.candidate(rejected=False)
        self.assertTrue(ready['translation_ready'])
        self.assertEqual(set(debt_rows(self.store, 'fr')), {other})

    def test_old_seed_fallbacks_do_not_become_new_generation_quality_debt(self):
        _, _, _, old_work = self.candidate()
        fresh = make_corpus([daily_doc(URL.replace('new', 'fresh'))])
        work = self.root/'new-generation'
        manifest = build(fresh, 'fr', work/'candidate', work/'memo.json', FakeTranslator(),
                         allow_source_fallback=True, seed_checkpoint=old_work/'memo.json')
        self.assertTrue(manifest['translation_complete'])
        self.assertEqual(manifest['source_fallback_unit_sha256'], [])
        self.store.put_source(fresh)
        ready = remember_candidate(self.store, 'fr', fresh, work/'candidate')
        self.assertTrue(ready['translation_ready'])
        self.assertEqual(set(debt_rows(self.store, 'fr')), {self.generation})

    def test_legacy_missing_quality_is_unproven_not_ready(self):
        result, _, _, _ = self.candidate(rejected=False)
        key = self.store.candidate_manifest_key('fr', self.generation, result['candidate_id'])
        manifest = json.loads(self.store.client.objects[key]['body'])
        for name in ('translation_complete', 'source_fallback_unit_count', 'source_fallback_occurrences',
                     'source_fallback_codes', 'source_fallback_unit_sha256'):
            manifest.pop(name)
        self.store._put(key, stable_bytes(manifest), metadata={'kind': 'legacy-fixture'})
        proof = record_quality(self.store, 'fr', self.generation, result['candidate_id'])
        self.assertFalse(proof['translation_ready']); self.assertEqual(proof['quality_status'], 'unproven')
        self.assertEqual(quality_summary(self.store, ('fr',))['quality_debt_by_locale']['fr']['unproven_generations'], 1)

    def test_exact_manifest_source_candidate_and_proof_bindings(self):
        result, _, _, _ = self.candidate(rejected=False)
        checksum = result['quality_proof_sha256']
        verify_quality(self.store, checksum, 'fr', self.generation, result['candidate_id'])
        with self.assertRaises((ExpansionError, R2NotFound)):
            verify_quality(self.store, checksum, 'pt', self.generation, result['candidate_id'])
        key = self.store.candidate_manifest_key('fr', self.generation, result['candidate_id'])
        value = json.loads(self.store.client.objects[key]['body']); value['cache_hits'] += 1
        self.store._put(key, stable_bytes(value), metadata={'kind': 'changed-fixture'})
        with self.assertRaisesRegex(ExpansionError, 'exact translated-ready'):
            verify_quality(self.store, checksum, 'fr', self.generation, result['candidate_id'])
        with self.assertRaisesRegex(ExpansionError, 'exact registered outcome'):
            candidate_quality(self.store, 'fr', self.generation, result['candidate_id'], manifest_sha256='e' * 64)
        self.store._put(proof_key(self.store, checksum), b'{}', metadata={'kind': 'corrupt-fixture'})
        with self.assertRaisesRegex(ExpansionError, 'checksum'):
            verify_quality(self.store, checksum, 'fr', self.generation, result['candidate_id'])

    def test_conflicting_readiness_and_bad_unit_hashes_rejected(self):
        _, manifest, _, _ = self.candidate()
        for changes in ({'translation_complete': True}, {'source_fallback_unit_sha256': ['x']},
                        {'source_fallback_unit_sha256': ['a' * 64, 'a' * 64]},
                        {'source_fallback_occurrences': 1}):
            with self.subTest(changes=changes), self.assertRaises(ExpansionError):
                quality_fields({**manifest, **changes})

    def test_bounded_ledger_never_evicts_existing_debt(self):
        self.candidate()
        before = copy.deepcopy(debt_rows(self.store, 'fr'))
        with patch('portal_extended_quality.MAX_DEBT_GENERATIONS', 0), self.assertRaises(ExpansionError):
            quality_summary(self.store, ('fr',))
        self.assertEqual(debt_rows(self.store, 'fr'), before)

    def test_legacy_handoff_without_quality_cannot_be_reviewed(self):
        result, _, _, _ = self.candidate(rejected=False)
        batch = {'generation': self.generation, 'candidates': {'fr': result['candidate_id']}}
        receipt = read_handoff(self.store, save_handoff(self.store, batch, day=DAY, pages=2, producer=PRODUCER))
        del receipt['translation_quality_proofs']
        raw = stable_bytes(receipt); checksum = digest(raw)
        self.store._put(self.store.key('publication-handoffs', checksum, 'receipt.json'), raw, metadata={'kind': 'legacy'})
        with self.assertRaisesRegex(ExpansionError, 'translated-ready quality proofs'):
            read_handoff(self.store, checksum)


class ActivePublicationTests(unittest.TestCase):
    def fixture(self):
        from test_portal_extended_publication import PublicationTests
        from portal_extended_locales import file_for_url
        fixture = PublicationTests('test_authenticated_legacy_bn_candidate_replays_exact_bytes_without_calls')
        fixture.setUp(); self.addCleanup(fixture.doCleanups)
        corpus = make_corpus([daily_doc(body=BODY)])
        work = fixture.base/'fallback'
        manifest = build(corpus, 'fr', work/'candidate', work/'memo.json', OriginalRejected(), allow_source_fallback=True)
        generation = corpus['documents_sha256']
        fixture.store.put_source(corpus)
        fixture.store.put_checkpoint('fr', generation, work/'memo.json')
        saved = fixture.store.upload_candidate(work/'candidate', 'fr', generation)
        source = fixture.root/file_for_url(URL); source.parent.mkdir(parents=True, exist_ok=True)
        source.write_bytes(raw_page(body=BODY))
        return fixture, {'generation': generation, 'candidates': {'fr': saved['candidate_id']}}, source

    def test_previously_active_fallback_bytes_keep_existing_exact_binding(self):
        fixture, batch, source = self.fixture()
        chinese_before = source.read_bytes()
        result = fixture.publish_frozen(batch)
        self.assertTrue(result['ready']); self.assertEqual(result['page_counts'], {'fr': 1})
        self.assertEqual(result['replays'][0]['translation_calls'], 0)
        # Only hreflang head decoration changes Chinese; its source body remains.
        self.assertIn(BODY.encode(), source.read_bytes())
        self.assertIn(b'Revenue USD10m.', source.read_bytes())
        self.assertIn('Revenue USD10m.', (fixture.root/'fr/blog/20260925-new.html').read_text())

    def test_changed_source_still_requires_new_translation_and_never_rebinds_old(self):
        fixture, batch, source = self.fixture()
        changed = raw_page(body=BODY.replace('USD10m', 'USD11m'))
        source.write_bytes(changed)
        with self.assertRaisesRegex(ExpansionError, 'source content changed'):
            fixture.publish_frozen(batch)
        self.assertEqual(source.read_bytes(), changed)
        self.assertFalse((fixture.root/'fr').exists())


if __name__ == '__main__':
    unittest.main()
