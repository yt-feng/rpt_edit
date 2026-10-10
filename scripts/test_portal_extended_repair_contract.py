"""Bounded debt repair: exact durable identities and zero-inference cache reuse."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import portal_extended_repair_contract as contract
from portal_extended_repair_cache import CacheFirstTranslator
from repair_portal_french_source_fallback import RepairEngine
from offline_translation import OfflineTranslator, OfflineTranslationError
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import R2Store, R2TransportError
import test_repair_portal_french_source_fallback as legacy


class ProbeTranslator(legacy.RepairTranslator):
    def __init__(self, cached=None):
        super().__init__()
        self.cached = cached
        self.cache_calls = []

    def cached_translation(self, text, target, source, *, markdown):
        self.cache_calls.append((text, target, source, markdown))
        return self.cached


class DurableContractTests(unittest.TestCase):
    def setUp(self):
        self.engine = RepairEngine(contract.quality_contract('fr'))
        self.legacy = RepairEngine(contract.LEGACY_FRENCH)
        self.client = legacy.AtomicR2()
        self.store = R2Store(self.client, 'private-bucket', '_extended-locales/staging/test')
        self.source = {'source': 'Revenue USD10m.', 'language': 'en', 'markdown': False}
        self.unit = self.engine.unit_key(self.source['source'], 'en', False)

    def started(self, engine):
        value = {**engine.claim_contract(self.unit, self.source), 'producer': legacy.OWNER}
        engine.create_record(self.store, engine.ledger_key(self.store, self.unit, 'started.json'), value)

    def attempt(self, translator, engine=None):
        return (engine or self.engine).attempt_unit(self.store, self.unit, self.source,
                                                   legacy.OTHER_OWNER, translator)

    def assert_unused(self, translator):
        self.assertEqual(translator.calls, [])
        self.assertEqual(translator.cache_calls, [])

    def test_current_or_legacy_unknown_blocks_cache_model_and_new_writes(self):
        for engine in (self.engine, self.legacy):
            with self.subTest(policy=engine.policy):
                self.client.objects.clear()
                self.started(engine)
                before = copy.deepcopy(self.client.objects)
                translator = ProbeTranslator('Chiffre d’affaires USD10m.')
                with self.assertRaisesRegex(ExpansionError, 'started_unresolved'):
                    self.attempt(translator)
                self.assert_unused(translator)
                self.assertEqual(self.client.objects, before)

    def test_legacy_accepted_migrates_only_after_current_validation(self):
        self.attempt(legacy.RepairTranslator(), self.legacy)
        before = copy.deepcopy(self.client.objects)
        translator = ProbeTranslator()
        _, outcome = self.attempt(translator)
        self.assert_unused(translator)
        self.assertEqual((outcome['status'], outcome['mode']), ('accepted', 'accepted-ledger'))
        for key, value in before.items():
            self.assertEqual(self.client.objects[key], value)

    def test_legacy_terminal_is_not_reopened_by_new_revision(self):
        self.attempt(legacy.RepairTranslator(terminal='Revenue'), self.legacy)
        before = copy.deepcopy(self.client.objects)
        translator = ProbeTranslator('Chiffre d’affaires USD10m.')
        with self.assertRaisesRegex(ExpansionError, 'legacy_terminal'):
            self.attempt(translator)
        self.assert_unused(translator)
        self.assertEqual(self.client.objects, before)

    def test_accepted_ledger_is_current_validated_even_with_valid_object_hash(self):
        for engine in (self.engine, self.legacy):
            with self.subTest(policy=engine.policy):
                self.client.objects.clear()
                self.attempt(legacy.RepairTranslator(), engine)
                key = engine.ledger_key(self.store, self.unit, 'outcome.json')
                value = json.loads(self.client.objects[key]['body'])
                value['row']['text'] = ''
                raw = stable_bytes(value)
                self.client.objects[key].update(body=raw, ContentLength=len(raw), Metadata={'sha256': digest(raw)})
                before = copy.deepcopy(self.client.objects)
                translator = ProbeTranslator('Chiffre d’affaires USD10m.')
                with self.assertRaises((ExpansionError, OfflineTranslationError)):
                    self.attempt(translator)
                self.assert_unused(translator)
                self.assertEqual(self.client.objects, before)

    def test_future_validator_revision_uses_same_key_and_cannot_reopen_unknown(self):
        self.started(self.engine)
        with patch.object(contract, 'QUALITY_REVISION', 'future-review-only'):
            future = RepairEngine(contract.quality_contract('fr'))
            self.assertEqual(future.ledger_key(self.store, self.unit, 'started.json'),
                             self.engine.ledger_key(self.store, self.unit, 'started.json'))
            before = copy.deepcopy(self.client.objects)
            translator = ProbeTranslator()
            with self.assertRaisesRegex(ExpansionError, 'ledger_claim_invalid'):
                self.attempt(translator, future)
            self.assert_unused(translator)
            self.assertEqual(self.client.objects, before)

    def test_lost_started_ack_never_calls_cache_or_model(self):
        self.client.lose_ack = 'started.json'
        translator = ProbeTranslator('Chiffre d’affaires USD10m.')
        with self.assertRaises(R2TransportError):
            self.attempt(translator)
        self.assert_unused(translator)
        self.client.lose_ack = None
        with self.assertRaisesRegex(ExpansionError, 'started_unresolved'):
            self.attempt(translator)
        self.assert_unused(translator)

    def test_locales_and_markdown_have_separate_logical_unit_keys(self):
        identities = set()
        for locale in ('fr', 'de', 'hi', 'tr'):
            engine = RepairEngine(contract.quality_contract(locale))
            for markdown in (False, True):
                unit = engine.unit_key(self.source['source'], 'en', markdown)
                identities.add(engine.ledger_key(self.store, unit, 'started.json'))
        self.assertEqual(len(identities), 8)

    def test_explicit_cache_miss_allows_one_fresh_attempt_and_durable_reuse(self):
        translator = ProbeTranslator()
        _, outcome = self.attempt(translator)
        self.assertEqual((outcome['status'], outcome['mode']), ('accepted', 'fresh-inference'))
        self.assertEqual((len(translator.cache_calls), len(translator.calls)), (1, 1))
        retry = ProbeTranslator()
        self.attempt(retry)
        self.assert_unused(retry)

    def test_accepted_cache_only_records_mode_without_calling_fresh(self):
        translator = ProbeTranslator('Chiffre d’affaires USD10m.')
        _, outcome = self.attempt(translator)
        self.assertEqual(outcome['mode'], 'cache-only')
        self.assertEqual(len(translator.cache_calls), 1)
        self.assertEqual(translator.calls, [])


class FrozenBatchTests(unittest.TestCase):
    def setUp(self):
        self.fixture = legacy.RepairTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.engine = RepairEngine(contract.quality_contract('fr'))
        self.request = {**self.fixture.request, 'locale': 'fr', 'policy': self.engine.policy,
                        'validator_revision': self.engine.revision,
                        'unit_modes': {unit:'fresh-authorized' for unit in self.fixture.units}}

    def rebuild(self, translator):
        f = self.fixture
        return self.engine.rebuild(f.store, f.corpus, f.oldraw, f.oldcandidate,
            f.root/'generic', f.root/'generic.json', self.request, legacy.OTHER_OWNER,
            translator, seconds=30)

    def test_last_selected_legacy_unknown_or_terminal_stops_all_earlier_work(self):
        f = self.fixture
        old_engine = RepairEngine(contract.LEGACY_FRENCH)
        unit = f.units[-1]
        source = old_engine.required_units(f.corpus)[unit]
        for terminal in (False, True):
            with self.subTest(terminal=terminal):
                f.client.objects.clear()
                if terminal:
                    old_engine.attempt_unit(f.store, unit, source, legacy.OWNER,
                                            legacy.RepairTranslator(terminal=source['source']))
                else:
                    old_engine.create_record(f.store, old_engine.ledger_key(f.store, unit, 'started.json'),
                        {**old_engine.claim_contract(unit, source), 'producer': legacy.OWNER})
                before = copy.deepcopy(f.client.objects)
                translator = ProbeTranslator()
                with self.assertRaises(ExpansionError):
                    self.rebuild(translator)
                self.assertEqual((translator.calls, translator.cache_calls), ([], []))
                self.assertEqual(f.client.objects, before)
                self.assertFalse((f.root/'generic').exists())
                self.assertFalse((f.root/'generic.json').exists())

    def test_all_legacy_accepted_rebuilds_without_cache_or_inference(self):
        f = self.fixture
        old_engine = RepairEngine(contract.LEGACY_FRENCH)
        sources = old_engine.required_units(f.corpus)
        for unit in f.units:
            old_engine.attempt_unit(f.store, unit, sources[unit], legacy.OWNER, legacy.RepairTranslator())
        self.request['unit_modes'] = {unit:'accepted-ledger' for unit in f.units}
        translator = ProbeTranslator()
        proof = self.rebuild(translator)
        self.assertEqual((translator.calls, translator.cache_calls), ([], []))
        self.assertEqual(proof['unit_attempt_modes'],
                         {'accepted-ledger': 2, 'cache-only': 0, 'fresh-inference': 0})
        self.assertEqual(proof['fallbacks_after'], 0)
        self.assertEqual(f.oldcheckpoint.read_bytes(), f.oldraw)


class CacheProbeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.factory_calls = []
        def forbidden(*args):
            self.factory_calls.append(args)
            raise AssertionError('real inference engine must not be constructed')
        self.fresh = OfflineTranslator(cache_dir=self.root/'cache', model_dir=self.root/'model',
                                        engine_factory=forbidden, validation_attempts=1)
        self.probe = CacheFirstTranslator(self.fresh)
        self.source = 'Revenue was 0.125%.'

    def cached(self, text, translation, **overrides):
        identity, path = self.probe.cached._memo_identity(text, 'fr', 'en', markdown=False)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({**identity, 'translation': translation, **overrides}), encoding='utf-8')
        return path

    def translate(self, text=None):
        return self.probe.cached_translation(text or self.source, 'fr', 'en', markdown=False)

    def assert_no_inference(self):
        self.assertEqual(self.factory_calls, [])
        for adapter in (self.fresh, self.probe.cached):
            self.assertEqual(adapter.stats['batch_requests'], 0)
            self.assertEqual(adapter.stats['translated_fragments'], 0)

    def test_current_valid_cache_reused_without_engine_or_file_writes(self):
        path = self.cached(self.source, 'Le revenu était de 0,125 %.')
        raw, modified = path.read_bytes(), path.stat().st_mtime_ns
        self.assertEqual(self.translate(), 'Le revenu était de 0,125 %.')
        self.assertEqual((path.read_bytes(), path.stat().st_mtime_ns), (raw, modified))
        self.assert_no_inference()

    def test_numeric_cache_difference_is_reused_without_inference_or_writes(self):
        path = self.cached(self.source, 'Le revenu était de 125 %.')
        raw, modified = path.read_bytes(), path.stat().st_mtime_ns
        self.assertEqual(self.translate(), 'Le revenu était de 125 %.')
        self.assertEqual((path.read_bytes(), path.stat().st_mtime_ns), (raw, modified))
        self.assert_no_inference()

    def test_cache_identity_or_json_corruption_is_not_missing(self):
        path = self.cached(self.source, 'Le revenu était de 0,125 %.', target_language='de')
        with self.assertRaises(OfflineTranslationError):
            self.translate()
        path.write_text('{broken', encoding='utf-8')
        with self.assertRaises((ValueError, OfflineTranslationError)):
            self.translate()
        self.assert_no_inference()

    def test_existing_structurally_invalid_cache_is_not_an_explicit_miss(self):
        source = 'Revenue was 0.125% at https://example.com/report.'
        path = self.cached(source, 'Le revenu était de 0,125 %.')
        raw = path.read_bytes()
        with self.assertRaises((ExpansionError, OfflineTranslationError)):
            self.translate(source)
        self.assertEqual(path.read_bytes(), raw)
        self.assert_no_inference()

    def test_explicit_missing_cache_returns_none_without_inference_or_cache_creation(self):
        self.assertIsNone(self.translate())
        self.assertFalse((self.root/'cache').exists())
        self.assert_no_inference()


if __name__ == '__main__':
    unittest.main()
