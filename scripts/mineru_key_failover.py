"""Bounded next-key parsing after a confirmed, stalled accepted task.

Original source claims and tasks are immutable. Alternate submissions have their
own durable reservation, credential and batch ID. A lost submission ACK blocks
further submissions; a retry reads the same attempts and selected winners.
"""
from __future__ import annotations

import copy
import math
import json
from pathlib import Path
import re
import uuid

from mineru_task_ledger import (ACTIVE, DONE, FAILED, REJECTED_STATES,
    LedgerError, digest, encoded, exact_json, schema_v1, validated_rows)
from mineru_terminal_recovery import page_limit_failure, task_identity

POLICY = 'stalled-task-next-key-v1'
MAX_ALTERNATES = 3
KEY = re.compile(r'batches/[a-f0-9]{32}')
HASH = re.compile(r'[a-f0-9]{64}')


def require(condition):
    if not condition:
        raise LedgerError('Invalid durable key failover binding')


class KeyFailover:
    def __init__(self, ledger, root, paths):
        self.ledger, self.store, self.root, self.paths = ledger, ledger.store, root, paths
        self.key = 'keyfailovers/' + root['key'].split('/')[1]
        self.bindings = {item['id']: item for item in root['files']}
        require(set(paths) == set(self.bindings))
        self.identity = task_identity(root)
        self.last_rows = {}

    def assert_original(self):
        root, _ = self.ledger._read_batch(self.root['key'])
        require(task_identity(root) == self.identity)
        for sid, item in self.bindings.items():
            raw = Path(self.paths[sid]).read_bytes()
            require(len(raw) == item['size'] and digest(raw) == item['sha256'])
            claim, _ = self.store.get('sources/' + sid)
            require(schema_v1(claim) and exact_json(claim.get('binding'), item)
                    and claim.get('batch_key') == self.root['key'])

    def read(self):
        self.assert_original()
        control, version = self.store.get(self.key)
        if control is None:
            return None, version, []
        require(schema_v1(control) and set(control) == {'schema', 'policy', 'root_key',
            'root_identity', 'attempts', 'winners', 'progress_sha256', 'last_progress_at'})
        require(control['policy'] == POLICY and control['root_key'] == self.root['key']
                and control['root_identity'] == self.identity
                and isinstance(control['attempts'], list) and len(control['attempts']) <= MAX_ALTERNATES
                and isinstance(control['winners'], dict)
                and HASH.fullmatch(str(control['progress_sha256'])) is not None
                and type(control['last_progress_at']) is int and control['last_progress_at'] >= 0)
        used_keys, used_tokens = {self.root['key']}, {self.root['token_identity']}
        children = []
        for ordinal, entry in enumerate(control['attempts'], 1):
            require(isinstance(entry, dict) and set(entry) == {'key', 'ordinal', 'token_identity', 'file_ids'}
                    and entry['ordinal'] == ordinal and type(entry['ordinal']) is int
                    and isinstance(entry['key'], str) and KEY.fullmatch(entry['key']) is not None
                    and entry['key'] not in used_keys
                    and isinstance(entry['token_identity'], str) and HASH.fullmatch(entry['token_identity']) is not None
                    and entry['token_identity'] in self.ledger.tokens
                    and entry['token_identity'] not in used_tokens
                    and isinstance(entry['file_ids'], list) and entry['file_ids']
                    and len(entry['file_ids']) == len(set(entry['file_ids']))
                    and set(entry['file_ids']) <= set(self.bindings))
            used_keys.add(entry['key']); used_tokens.add(entry['token_identity'])
            child, child_version = self.store.get(entry['key'])
            if child is not None:
                child, child_version = self.ledger._read_batch(entry['key'])
                require(child['token_identity'] == entry['token_identity']
                        and exact_json(child['files'], [self.bindings[sid] for sid in entry['file_ids']])
                        and exact_json(child.get('key_failover_parent'), {'key': self.root['key'], 'ordinal': ordinal}))
            children.append((entry, child, child_version))
        allowed = {self.root['key']: (0, set(self.bindings))}
        allowed.update({entry['key']: (entry['ordinal'], set(entry['file_ids']))
                        for entry, child, _ in children if child is not None
                        and child['state'] in {'accepted', 'uploaded', 'terminal'} and child.get('batch_id')})
        for sid, winner in control['winners'].items():
            require(sid in self.bindings and isinstance(winner, dict) and set(winner) == {'key', 'ordinal'}
                    and winner['key'] in allowed and sid in allowed[winner['key']][1]
                    and type(winner['ordinal']) is int and winner['ordinal'] == allowed[winner['key']][0])
        return control, version, children

    def inspect(self, batch, deadline):
        self.assert_original()
        remaining = self.ledger._remaining(deadline)
        rows = self.ledger.provider.poll(batch['batch_id'], self.ledger.tokens[batch['token_identity']], remaining)
        rows = validated_rows(batch, rows)
        # A partial or malformed response cannot authorize another POST.
        require(set(rows) == {item['id'] for item in batch['files']})
        self.assert_original()
        return rows

    def lineage(self, row, batch, ordinal):
        result = copy.deepcopy(row)
        result['_recovery_lineage'] = {'batch_id': batch['batch_id'], 'batch_key': batch['key'],
            'parent_batch_key': self.root['key'], 'data_id': row['data_id'], 'child_ordinal': ordinal}
        return result

    def run(self, *, timeout, interval=15, queue_budget=300, initial_waited=False, done_verifier=None):
        require(all(type(x) in {int, float} and math.isfinite(x) and x > 0 for x in (timeout, interval)))
        require(type(queue_budget) in {int, float} and math.isfinite(queue_budget) and queue_budget >= 0)
        require(type(initial_waited) is bool)
        deadline = self.ledger.clock() + timeout
        # Reserve time for every configured key instead of letting key 1 use
        # the full batch deadline. Production pools are bounded to four keys.
        stall = min(queue_budget or 300, timeout / min(4, len(self.ledger.tokens)))
        control, version, children = self.read()
        posts = 0
        verified = set()
        latest, batches = {}, {}
        unknown_submission = False
        while self.ledger.clock() < deadline:
            control, version, children = self.read()
            self.assert_original()
            observations = []
            root_rows = self.inspect(self.root, deadline)
            observations.append((self.root, 0, root_rows))
            if control is None:
                # Fully terminal originals retain the existing terminal-failure
                # policy. This policy is only admitted by observed active work.
                if not any(str(row['state']).lower() in ACTIVE for row in root_rows.values()):
                    return None
                control = {'schema': 1, 'policy': POLICY, 'root_key': self.root['key'],
                    'root_identity': self.identity, 'attempts': [], 'winners': {},
                    'progress_sha256': digest(encoded({})),
                    'last_progress_at': max(0, int(self.ledger.wallclock() - (stall if initial_waited else 0)))}
                version = self.store.put(self.key, control, version)
            unknown_submission = False
            last_attempt_rejected = False
            for entry, child, child_version in children:
                if child is None or child['state'] == 'claiming':
                    # Finish the same reservation; never allocate a replacement
                    # reservation because an earlier runner was interrupted.
                    if all(str(root_rows[sid]['state']).lower() in DONE for sid in entry['file_ids']):
                        continue
                    if self.ledger.forbid_new_submissions:
                        unknown_submission = True
                        continue
                    if child is None:
                        child = {'schema': 1, 'key': entry['key'], 'scope': self.root['scope'],
                            'endpoint': self.root['endpoint'], 'options': self.root['options'],
                            'token_identity': entry['token_identity'],
                            'files': [self.bindings[sid] for sid in entry['file_ids']],
                            'state': 'claiming', 'batch_id': None,
                            'key_failover_parent': {'key': self.root['key'], 'ordinal': entry['ordinal']}}
                        child_version = self.store.put(child['key'], child, child_version)
                    before = self.ledger.submission_posts
                    try:
                        self.ledger._submit_claimed(child, child_version, self.paths, deadline,
                                                    only_token=entry['token_identity'])
                    except LedgerError:
                        saved, _ = self.ledger._read_batch(entry['key'])
                        if saved['state'] not in REJECTED_STATES:
                            raise
                    finally:
                        posts += self.ledger.submission_posts - before
                    child, _ = self.ledger._read_batch(entry['key'])
                if child['state'] == 'submitting':
                    unknown_submission = True
                elif child['state'] in {'accepted', 'uploaded', 'terminal'}:
                    observations.append((child, entry['ordinal'], self.inspect(child, deadline)))
                elif child['state'] not in REJECTED_STATES:
                    raise LedgerError('Invalid durable key failover binding')
                if entry['ordinal'] == len(control['attempts']):
                    last_attempt_rejected = child['state'] in REJECTED_STATES
            latest, batches = {}, {}
            observed = {}
            for batch, ordinal, rows in observations:
                batches[batch['key']] = (batch, ordinal)
                observed[batch['key']] = rows
                for sid, row in rows.items():
                    winner = control['winners'].get(sid)
                    if winner is None and str(row['state']).lower() in DONE:
                        control['winners'][sid] = {'key': batch['key'], 'ordinal': ordinal}
                    if sid not in latest or str(row['state']).lower() in ACTIVE:
                        latest[sid] = row
            for sid, winner in control['winners'].items():
                require(winner['key'] in observed and sid in observed[winner['key']])
                row = observed[winner['key']][sid]
                require(str(row['state']).lower() in DONE)
                batch, ordinal = batches[winner['key']]
                latest[sid] = self.lineage(row, batch, ordinal)
            state_hash = digest(encoded({key: {sid: str(row['state']).lower() for sid, row in rows.items()}
                                         for key, rows in observed.items()}))
            if state_hash != control['progress_sha256']:
                first_observation = control['progress_sha256'] == digest(encoded({}))
                control['progress_sha256'] = state_hash
                if not (first_observation and initial_waited):
                    control['last_progress_at'] = int(self.ledger.wallclock())
            # Persist every selected winner before returning it or admitting a
            # further key; late original results cannot change that selection.
            if not self.ledger.forbid_new_submissions:
                version = self.store.put(self.key, control, version)
            for sid in control['winners']:
                if sid not in verified and done_verifier is not None:
                    done_verifier(Path(self.paths[sid]), copy.deepcopy(latest[sid]))
                verified.add(sid)
            if len(control['winners']) == len(self.bindings):
                break
            if unknown_submission:
                break
            blocked = {sid for _, _, rows in observations for sid, row in rows.items() if page_limit_failure(row)}
            pending = [sid for sid in self.bindings if sid not in control['winners'] and sid not in blocked
                       and str(latest[sid]['state']).lower() in ACTIVE]
            used = {self.root['token_identity']} | {entry['token_identity'] for entry in control['attempts']}
            # Definitively rejected original credentials need no new attempts.
            used.update(row['token_identity'] for row in self.root.get('auth_rejections', []))
            used.update(row['token_identity'] for row in self.root.get('quota_rejections', [])
                        if row['retry_after'] > self.ledger.wallclock())
            identities = list(self.ledger.tokens)
            offset = (identities.index(self.root['token_identity']) + 1) % len(identities)
            ordered = identities[offset:] + identities[:offset]
            next_token = next((identity for identity in ordered if identity not in used), None)
            stalled = (self.ledger.wallclock() - control['last_progress_at'] >= stall
                       or initial_waited and not control['attempts'])
            active = any(str(row['state']).lower() in ACTIVE for _, _, rows in observations for row in rows.values())
            if (pending and next_token is not None and len(control['attempts']) < MAX_ALTERNATES
                    and (stalled or not active or last_attempt_rejected) and not self.ledger.forbid_new_submissions):
                self.assert_original()
                entry = {'key': 'batches/' + uuid.uuid4().hex, 'ordinal': len(control['attempts']) + 1,
                         'token_identity': next_token, 'file_ids': pending}
                control['attempts'].append(entry)
                control['last_progress_at'] = int(self.ledger.wallclock())
                version = self.store.put(self.key, control, version)
                print(json.dumps({'event': 'mineru_key_failover', 'attempt': entry['ordinal'] + 1,
                    'key_index': list(self.ledger.tokens).index(next_token) + 1,
                    'pending_sources': len(pending)}, sort_keys=True), flush=True)
                control, version, children = self.read()
                continue
            remaining = deadline - self.ledger.clock()
            if remaining > 0:
                self.ledger.sleep(min(interval, remaining))
        self.assert_original()
        self.last_rows = latest
        winners = control['winners'] if control is not None else {}
        ready = len(winners) == len(self.bindings)
        failures = sum(sid not in winners and str(latest.get(sid, {}).get('state', '')).lower() in FAILED
                       for sid in self.bindings)
        outcomes = [{'data_id': sid, 'status': 'done' if sid in winners else
                     'submission_unknown' if unknown_submission else 'failed' if
                     str(latest.get(sid, {}).get('state', '')).lower() in FAILED else 'pending',
                     'retry_count': sum(sid in entry['file_ids'] for entry in control['attempts']) if control else 0}
                    for sid in self.bindings]
        summary = {'requested': len(self.bindings), 'completed': len(winners), 'failed': failures,
            'pending': len(self.bindings) - len(winners) - failures, 'missing': 0,
            'provider_posts': posts, 'ready_for_generation': ready, 'partial': not ready,
            'key_failover_attempts': len(control['attempts']) if control else 0,
            'source_outcomes': outcomes, 'batch_keys': [self.root['key']]}
        rows = [(Path(self.paths[sid]), latest[sid]) for sid in self.bindings if sid in winners]
        return rows, summary
