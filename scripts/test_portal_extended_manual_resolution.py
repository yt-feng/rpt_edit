"""Append-only manual resolution contracts with synthetic R2, GitHub, and model."""
from __future__ import annotations

import copy
import json
import unittest
from unittest.mock import patch

import portal_extended_manual_resolution as resolution
from offline_translation import OfflineTranslationValidationError
from portal_extended_french_repair import RepairPipeline
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import R2Store, R2TransportError
from portal_extended_repair_contract import MANUAL_STRICT_RETRY, quality_contract
from repair_portal_french_source_fallback import RepairEngine
from test_repair_portal_french_source_fallback import AtomicR2


REPOSITORY = 'example/repo'
ORIGINAL = {'run_id': '1', 'attempt': '1', 'sha': 'a' * 40}
PARENT = {'run_id': '2', 'attempt': '1', 'sha': 'b' * 40}
CHILD = {'run_id': '3', 'attempt': '1', 'sha': 'c' * 40}
OTHER = {'run_id': '4', 'attempt': '1', 'sha': 'd' * 40}
TRANSLATION = 'ဝင်ငွေ USD10m။'


class Translator:
    def __init__(self, *, cached=None, error=None):
        self.cached = cached
        self.error = error
        self.cache_calls = []
        self.calls = []
        self.deadlines = []

    def set_deadline(self, deadline):
        self.deadlines.append(deadline)

    def cached_translation(self, text, target, source, *, markdown):
        self.cache_calls.append((text, target, source, markdown))
        return self.cached

    def translate(self, text, target, source, *, markdown):
        self.calls.append((text, target, source, markdown))
        if self.error is not None:
            raise self.error
        return TRANSLATION


class ManualResolutionTests(unittest.TestCase):
    def setUp(self):
        self.engine = RepairEngine(quality_contract('my'))
        self.client = AtomicR2()
        self.store = R2Store(self.client, 'private-bucket', '_extended-locales/staging/test')
        self.source = {'source': 'Revenue USD10m.', 'language': 'en', 'markdown': False}
        self.unit = self.engine.unit_key(self.source['source'], 'en', False)
        self.parent_key = self.engine.ledger_key(self.store, self.unit, 'started.json')
        self.outcome_key = self.engine.ledger_key(self.store, self.unit, 'outcome.json')
        self.claim = {**self.engine.claim_contract(self.unit, self.source), 'producer': PARENT}
        self.engine.create_record(self.store, self.parent_key, self.claim)
        self.parent_bytes = self.client.objects[self.parent_key]['body']
        self.parent_id = digest(self.parent_bytes)
        self.repair = {
            'policy': self.engine.policy, 'validator_revision': self.engine.revision,
            'locale': 'my', 'source_sha256': '1' * 64, 'origin_sha256': '2' * 64,
            'producer': ORIGINAL, 'checkpoint_sha256': '3' * 64,
            'candidate_id': '4' * 64, 'manifest_sha256': '5' * 64,
            'units': [self.unit], 'unit_modes': {self.unit: 'fresh-authorized'},
            'retry_policy': MANUAL_STRICT_RETRY,
            'resolution_evidence': {
                'policy': resolution.POLICY, 'claim_sha256': self.parent_id,
                'producer': PARENT, 'source_job_id': 21, 'locale_job_id': 22,
            },
        }
        self.runs, self.job_rows = {}, {}
        for owner, failed in ((PARENT, True), (CHILD, False), (OTHER, False)):
            run_id = int(owner['run_id'])
            self.runs[run_id] = {
                'id': run_id, 'run_attempt': 1, 'head_sha': owner['sha'],
                'status': 'completed', 'conclusion': 'failure' if failed else 'success',
                'path': resolution.WORKFLOW, 'head_branch': 'main', 'event': 'workflow_dispatch',
                'repository': {'full_name': REPOSITORY, 'private': False},
                'head_repository': {'full_name': REPOSITORY},
            }
            self.job_rows[run_id] = [
                {'id': run_id * 10 + index, 'name': name, 'run_id': run_id,
                 'head_sha': owner['sha'], 'status': 'completed',
                 'conclusion': 'failure' if failed and index == 2 else 'success'}
                for index, name in ((1, 'source'), (2, 'locale (my)'))
            ]

    def api(self, path):
        for owner in (PARENT, CHILD, OTHER):
            base = f'repos/{REPOSITORY}/actions/runs/{owner["run_id"]}/attempts/1'
            run_id = int(owner['run_id'])
            if path == base:
                return copy.deepcopy(self.runs[run_id])
            if path == base + '/jobs?per_page=100':
                rows = self.job_rows[run_id]
                return {'total_count': len(rows), 'jobs': copy.deepcopy(rows)}
        raise AssertionError('Unexpected synthetic GitHub request')

    def child_key(self, name):
        return resolution.key(self.store, self.parent_id, name)

    def stage(self, translator=None, *, owner=CHILD, seconds=900):
        return resolution.stage(self.store, self.engine, self.repair, self.source,
                                owner, translator or Translator(), seconds)

    def preflight(self):
        return resolution.preflight(self.store, self.engine, self.repair, self.source,
                                    REPOSITORY, self.api)

    def assert_original_unresolved(self):
        self.assertEqual(self.client.objects[self.parent_key]['body'], self.parent_bytes)
        self.assertNotIn(self.outcome_key, self.client.objects)
        claim, outcome = self.engine.ledger_outcome(self.store, self.unit, self.source)
        self.assertEqual(claim, self.claim)
        self.assertIsNone(outcome)

    def assert_rejected_before_translation(self):
        before = copy.deepcopy(self.client.objects)
        translator = Translator()
        with self.assertRaises((ExpansionError, R2TransportError)):
            if self.preflight():
                self.stage(translator)
        self.assertEqual(translator.calls, [])
        self.assertEqual(translator.cache_calls, [])
        self.assertEqual(self.client.objects, before)

    def replace_record(self, key, value):
        raw = stable_bytes(value)
        self.client.objects[key].update(body=raw, ContentLength=len(raw), Metadata={'sha256': digest(raw)})

    def source_claim(self, owner=CHILD):
        pipeline = RepairPipeline(self.engine.contract)
        request = resolution.normalized(self.repair)
        value = {'request': request, 'producer': owner,
                 'before_row': {'status': 'complete', 'snapshot': {
                     name: self.repair[name] for name in
                     ('checkpoint_sha256', 'candidate_id', 'manifest_sha256')}}}
        name = pipeline.claim_key(self.store, request, owner)
        resolution.immutable(self.store, name, value)
        return name

    def completed(self):
        accepted = self.stage()
        self.source_claim()
        identity = resolution.complete(self.store, self.engine, self.repair, self.source, CHILD)
        self.repair['resolution_evidence']['completion_sha256'] = identity
        return accepted, identity

    def adopt(self):
        return resolution.adopt(self.store, self.engine, self.repair, self.source, REPOSITORY, self.api)

    def test_parent_preflight_is_read_only_and_preserves_model_contract(self):
        before = copy.deepcopy(self.client.objects)
        self.assertTrue(self.preflight())
        self.assertEqual(self.client.objects, before)
        self.assertEqual(self.engine.request(self.repair), self.repair)
        self.assert_original_unresolved()

    def test_parent_claim_hash_owner_or_unit_mismatch_cannot_infer(self):
        original = copy.deepcopy(self.repair)
        for field, value in (('claim_sha256', 'f' * 64), ('producer', OTHER)):
            with self.subTest(field=field):
                self.repair = copy.deepcopy(original)
                self.repair['resolution_evidence'][field] = value
                self.assert_rejected_before_translation()
        self.repair = original
        self.source = {**self.source, 'source': 'Different source USD10m.'}
        self.assert_rejected_before_translation()

    def test_parent_running_wrong_sha_repository_workflow_or_event_cannot_infer(self):
        original = copy.deepcopy(self.runs[2])
        changes = [('status', 'in_progress'), ('conclusion', 'success'), ('head_sha', 'f' * 40),
                   ('path', '.github/workflows/other.yml'), ('event', 'schedule'),
                   ('head_branch', 'feature'), ('run_attempt', 2),
                   ('repository', {'full_name': 'other/repo', 'private': False})]
        for field, value in changes:
            with self.subTest(field=field):
                self.runs[2] = {**original, field: value}
                self.assert_rejected_before_translation()
        self.runs[2] = original

    def test_parent_wrong_job_identity_status_or_duplicate_cannot_infer(self):
        original = copy.deepcopy(self.job_rows[2])
        for field, value in (('id', 99), ('head_sha', 'f' * 40), ('run_id', 9),
                             ('status', 'in_progress'), ('conclusion', 'success')):
            with self.subTest(field=field):
                self.job_rows[2] = copy.deepcopy(original)
                self.job_rows[2][1][field] = value
                self.assert_rejected_before_translation()
        self.job_rows[2] = [*original, copy.deepcopy(original[1])]
        self.assert_rejected_before_translation()

    def test_parent_existing_outcome_or_read_error_cannot_infer(self):
        self.engine.create_record(self.store, self.outcome_key, {'status': 'terminal'})
        self.assert_rejected_before_translation()
        del self.client.objects[self.outcome_key]
        with patch.object(self.store, '_get', side_effect=R2TransportError('synthetic read stop')):
            self.assert_rejected_before_translation()

    def test_single_child_budget_and_competing_claim_do_not_infer(self):
        for seconds in (0, 901):
            with self.subTest(seconds=seconds):
                translator = Translator()
                with self.assertRaisesRegex(ExpansionError, 'budget_invalid'):
                    self.stage(translator, seconds=seconds)
                self.assertEqual(translator.calls, [])
                self.assertEqual(translator.cache_calls, [])
        translator = Translator()
        self.client.race = True
        with self.assertRaisesRegex(ExpansionError, 'already_claimed'):
            self.stage(translator)
        self.assertEqual(translator.calls, [])
        self.assertEqual(translator.cache_calls, [])
        self.assert_original_unresolved()

    def test_unknown_child_result_cannot_replay_under_another_owner(self):
        first = Translator(error=TimeoutError('synthetic unknown response'))
        with self.assertRaises(TimeoutError):
            self.stage(first)
        before = copy.deepcopy(self.client.objects)
        second = Translator(cached=TRANSLATION)
        with self.assertRaisesRegex(ExpansionError, 'started_unresolved'):
            self.stage(second, owner=OTHER)
        self.assertEqual(len(first.calls), 1)
        self.assertEqual(second.calls, [])
        self.assertEqual(second.cache_calls, [])
        self.assertEqual(self.client.objects, before)
        self.assert_original_unresolved()

    def test_terminal_child_is_durable_and_cannot_replay(self):
        translator = Translator(error=OfflineTranslationValidationError('Hy-MT2 placeholder validation failed'))
        with self.assertRaises(OfflineTranslationValidationError):
            self.stage(translator)
        self.assertIn(self.child_key('terminal.json'), self.client.objects)
        self.assertNotIn(self.child_key('accepted.json'), self.client.objects)
        self.assert_rejected_before_translation()
        self.assert_original_unresolved()

    def test_terminal_and_accepted_cannot_coexist_or_use_wrong_claim(self):
        accepted=self.stage()
        marker={'schema_version':1,'policy':resolution.POLICY,
                'child_claim_sha256':accepted['child_claim_sha256'],'failure_code':'offline-token-limit'}
        resolution.immutable(self.store,self.child_key('terminal.json'),marker)
        with self.assertRaisesRegex(ExpansionError,'terminal_result_conflict'): self.stage()
        marker['child_claim_sha256']='f'*64
        self.replace_record(self.child_key('terminal.json'),marker)
        with self.assertRaisesRegex(ExpansionError,'terminal_binding_invalid'): self.stage()
        self.assert_original_unresolved()

    def test_parent_outcome_rechecked_at_locked_child_claim_boundary(self):
        self.assertTrue(self.preflight())
        self.engine.create_record(self.store,self.outcome_key,{'status':'terminal'})
        before=copy.deepcopy(self.client.objects)
        translator=Translator()
        with self.assertRaisesRegex(ExpansionError,'parent_already_resolved'): self.stage(translator)
        self.assertEqual(translator.calls,[]); self.assertEqual(translator.cache_calls,[])
        self.assertEqual(self.client.objects,before)

    def test_existing_null_outcome_is_not_a_typed_missing_object(self):
        self.engine.create_record(self.store,self.outcome_key,None)
        self.assert_rejected_before_translation()

    def test_valid_private_result_precedes_parent_outcome_and_reuses_without_inference(self):
        translator = Translator()
        accepted = self.stage(translator)
        self.assertEqual(len(translator.calls), 1)
        self.assertEqual(len(translator.deadlines), 1)
        self.assertEqual(accepted['row']['text'], TRANSLATION)
        self.assertEqual(accepted['row_sha256'], digest(stable_bytes(accepted['row'])))
        self.assert_original_unresolved()
        before = copy.deepcopy(self.client.objects)
        second = Translator(error=AssertionError('repeated inference'))
        self.assertEqual(self.stage(second, owner=OTHER), accepted)
        self.assertFalse(self.preflight())
        self.assertEqual(second.calls, [])
        self.assertEqual(second.cache_calls, [])
        self.assertEqual(self.client.objects, before)

    def test_valid_cache_is_validated_and_durable_without_model(self):
        translator = Translator(cached=TRANSLATION)
        self.stage(translator)
        self.assertEqual(len(translator.cache_calls), 1)
        self.assertEqual(translator.calls, [])
        self.assert_original_unresolved()

    def test_durable_result_from_failed_tail_resumes_under_successful_reader_without_inference(self):
        accepted=self.stage()
        self.source_claim(CHILD)
        self.runs[3]['conclusion']='failure';self.job_rows[3][1]['conclusion']='failure'
        unused=Translator(error=AssertionError('no repeated inference'))
        self.assertEqual(self.stage(unused,owner=OTHER),accepted)
        self.source_claim(OTHER)
        identity=resolution.complete(self.store,self.engine,self.repair,self.source,OTHER)
        self.repair['resolution_evidence']['completion_sha256']=identity
        _,outcome=self.adopt()
        self.assertEqual(outcome['row'],accepted['row'])
        self.assertEqual(unused.calls,[]);self.assertEqual(unused.cache_calls,[])
        self.assertEqual(self.client.objects[self.parent_key]['body'],self.parent_bytes)

    def test_lost_accepted_ack_reads_back_identical_bytes_without_second_inference(self):
        self.client.lose_ack = 'accepted.json'
        translator = Translator()
        accepted = self.stage(translator)
        self.assertEqual(len(translator.calls), 1)
        self.assertEqual(self.client.writes, 3)  # parent, child claim, private result
        self.assertEqual(self.client.objects[self.child_key('accepted.json')]['body'], stable_bytes(accepted))
        self.assert_original_unresolved()

    def test_malformed_exception_response_after_put_still_verifies_exact_result(self):
        class LostAck(Exception):
            response = None
        original = self.client.put_object
        def put(**kwargs):
            result = original(**kwargs)
            if kwargs['Key'] == self.child_key('accepted.json'):
                raise LostAck('synthetic malformed error metadata')
            return result
        translator = Translator()
        with patch.object(self.client, 'put_object', side_effect=put):
            accepted = self.stage(translator)
        self.assertEqual(len(translator.calls), 1)
        self.assertEqual(self.client.writes, 3)
        self.assertEqual(self.client.objects[self.child_key('accepted.json')]['body'], stable_bytes(accepted))
        self.assert_original_unresolved()

    def test_missing_after_failed_put_retries_only_identical_private_bytes(self):
        original = self.client.put_object
        bodies = []
        def put(**kwargs):
            if kwargs['Key'] == self.child_key('accepted.json'):
                bodies.append(bytes(kwargs['Body']))
                if len(bodies) == 1:
                    raise TimeoutError('synthetic missing write')
            return original(**kwargs)
        translator = Translator()
        with patch.object(self.client, 'put_object', side_effect=put):
            self.stage(translator)
        self.assertEqual(len(bodies), 2)
        self.assertEqual(bodies[0], bodies[1])
        self.assertEqual(len(translator.calls), 1)
        self.assert_original_unresolved()

    def test_accepted_write_read_error_keeps_unknown_and_never_reinfers(self):
        original = self.store._get
        def get(name, **kwargs):
            if name == self.child_key('accepted.json') and name in self.client.objects:
                raise R2TransportError('synthetic accepted read interruption')
            return original(name, **kwargs)
        translator = Translator()
        with patch.object(self.store, '_get', side_effect=get):
            with self.assertRaises(R2TransportError):
                self.stage(translator)
        self.assertEqual(len(translator.calls), 1)
        second = Translator(error=AssertionError('repeated inference'))
        self.stage(second)
        self.assertEqual(second.calls, [])
        self.assert_original_unresolved()

    def test_malformed_persisted_result_cannot_adopt_or_reinfer(self):
        accepted = self.stage()
        name = self.child_key('accepted.json')
        for change in ('hash', 'source', 'language', 'text', 'producer'):
            with self.subTest(change=change):
                bad = copy.deepcopy(accepted)
                if change == 'hash':
                    bad['row_sha256'] = 'f' * 64
                elif change == 'producer':
                    bad['producer'] = OTHER
                else:
                    bad['row'][change] = {'source': 'Different source', 'language': 'zh', 'text': ''}[change]
                    bad['row_sha256'] = digest(stable_bytes(bad['row']))
                self.replace_record(name, bad)
                self.assert_rejected_before_translation()
                self.assert_original_unresolved()
        self.replace_record(name, accepted)

    def test_changed_acknowledged_bytes_are_rejected_before_parent_outcome(self):
        original = self.client.put_object
        def put(**kwargs):
            result = original(**kwargs)
            if kwargs['Key'] == self.child_key('accepted.json'):
                changed = json.loads(kwargs['Body'])
                changed['row']['text'] = 'တခြား USD10m။'
                self.replace_record(kwargs['Key'], changed)
                raise TimeoutError('synthetic changed acknowledgement')
            return result
        translator = Translator()
        with patch.object(self.client, 'put_object', side_effect=put):
            with self.assertRaisesRegex(ExpansionError, 'immutable_conflict'):
                self.stage(translator)
        self.assertEqual(len(translator.calls), 1)
        self.assert_original_unresolved()

    def test_completion_without_matching_source_claim_cannot_adopt(self):
        self.stage()
        identity = resolution.complete(self.store, self.engine, self.repair, self.source, CHILD)
        self.repair['resolution_evidence']['completion_sha256'] = identity
        with self.assertRaisesRegex(ExpansionError, 'source_claim_missing'):
            self.adopt()
        self.assert_original_unresolved()

    def test_completion_before_actual_source_and_locale_success_cannot_adopt(self):
        self.completed()
        run = copy.deepcopy(self.runs[3])
        jobs = copy.deepcopy(self.job_rows[3])
        for variant in ('run-running', 'source-failed', 'locale-failed', 'locale-running'):
            with self.subTest(variant=variant):
                self.runs[3] = copy.deepcopy(run)
                self.job_rows[3] = copy.deepcopy(jobs)
                if variant == 'run-running': self.runs[3]['status'] = 'in_progress'
                if variant == 'source-failed': self.job_rows[3][0]['conclusion'] = 'failure'
                if variant == 'locale-failed': self.job_rows[3][1]['conclusion'] = 'failure'
                if variant == 'locale-running': self.job_rows[3][1]['status'] = 'in_progress'
                before = copy.deepcopy(self.client.objects)
                with self.assertRaises(ExpansionError): self.adopt()
                self.assertEqual(self.client.objects, before)
                self.assert_original_unresolved()

    def test_success_admission_preserves_original_claim_and_only_appends_accepted_outcome(self):
        accepted, _ = self.completed()
        before = copy.deepcopy(self.client.objects)
        claim, outcome = self.adopt()
        self.assertEqual(claim, self.claim)
        for name, value in before.items(): self.assertEqual(self.client.objects[name], value)
        self.assertEqual(self.client.objects[self.parent_key]['body'], self.parent_bytes)
        self.assertEqual(outcome['status'], 'accepted')
        self.assertEqual(outcome['mode'], 'accepted-ledger')
        self.assertEqual(outcome['claim_sha256'], self.parent_id)
        self.assertEqual(outcome['row'], accepted['row'])
        self.assertEqual(outcome['validator_revision'], self.engine.revision)
        added = set(self.client.objects) - set(before)
        self.assertEqual(len(added), 2)
        self.assertIn(self.outcome_key, added)
        self.assertIn(resolution.key(self.store, self.parent_id, 'admissions',
                                    outcome['manual_resolution_sha256'] + '.json'), added)
        unused = Translator(error=AssertionError('accepted ledger inferred'))
        self.assertEqual(self.engine.attempt_unit(self.store, self.unit, self.source, OTHER, unused),
                         (claim, outcome))
        self.assertEqual(unused.calls, [])
        self.assertEqual(unused.cache_calls, [])
        self.assertEqual(self.adopt(), (claim, outcome))

    def test_imported_outcome_requires_immutable_admission_and_exact_row(self):
        self.completed()
        _, outcome = self.adopt()
        original = copy.deepcopy(self.client.objects[self.outcome_key])
        for change in ('missing-admission', 'changed-row'):
            with self.subTest(change=change):
                bad = copy.deepcopy(outcome)
                if change == 'missing-admission':
                    bad['manual_resolution_sha256'] = 'f' * 64
                else:
                    bad['row']['text'] = 'တခြား USD10m။'
                self.replace_record(self.outcome_key, bad)
                translator = Translator(error=AssertionError('invalid admission inferred'))
                before = copy.deepcopy(self.client.objects)
                with self.assertRaises(ExpansionError):
                    self.engine.attempt_unit(self.store, self.unit, self.source, OTHER, translator)
                self.assertEqual(translator.calls, [])
                self.assertEqual(translator.cache_calls, [])
                self.assertEqual(self.client.objects, before)
        self.client.objects[self.outcome_key] = original


if __name__ == '__main__':
    unittest.main()
