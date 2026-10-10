"""Durable publication-event capture and one serialized, bounded admission writer."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import time

import requests

import portal_extended_recovered_admission as recovered
from portal_extended_daily_queue import (WORKFLOW, checked_producer, immutable_record,
    read_admission, read_corpus, write_verified)
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import (DEFAULT_PREFIX, R2IntegrityError, R2NotFound, R2Store,
    R2StoreError, classify)

POLICY = 'verified-publication-ingress-v1'
WAKE_WORKFLOW = '.github/workflows/portal-extended-source-wakeup.yml'
MAX_PENDING = 1024
MAX_EVENTS = 8
MAX_ENVELOPES = 4
MAX_ENVELOPE_BYTES = 3 * 1024 * 1024
STAGES = ('generate', 'deliver', 'publish')
EVENT_FIELDS = {'repository', 'id', 'run_attempt', 'head_sha', 'path', 'event', 'conclusion'}


def require(value, code):
    if not value:
        raise ExpansionError(code)


class BudgetClient:
    """Check one monotonic deadline around every bounded SDK operation."""
    def __init__(self, client, clock, deadline):
        self.client, self.clock, self.deadline = client, clock, deadline

    def check(self):
        require(self.clock() < self.deadline, 'ingress_budget_exhausted')

    def __getattr__(self, name):
        method = getattr(self.client, name)
        def call(*args, **kwargs):
            self.check()
            value = method(*args, **kwargs)
            self.check()
            if name == 'get_object' and isinstance(value, dict) and 'Body' in value:
                value = {**value, 'Body': BudgetBody(value['Body'], self)}
            return value
        return call


class BudgetBody:
    def __init__(self, body, budget):
        self.body, self.budget = body, budget

    def read(self, *args, **kwargs):
        self.budget.check()
        value = self.body.read(*args, **kwargs)
        self.budget.check()
        return value

    def close(self):
        if hasattr(self.body, 'close'):
            self.body.close()


def checked_event(value):
    require(isinstance(value, dict) and set(value) == EVENT_FIELDS
        and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', str(value['repository']))
        and type(value['id']) is int and value['id'] > 0
        and type(value['run_attempt']) is int and 1 <= value['run_attempt'] <= 10
        and re.fullmatch(r'[a-f0-9]{40}', str(value['head_sha'])), 'ingress_event_invalid')
    daily = value['path'] == recovered.DAILY_WORKFLOW
    require(value['path'] in {recovered.WORKFLOW, recovered.DAILY_WORKFLOW}
        and (value['event'] in {'schedule', 'workflow_dispatch'} if daily else value['event'] == 'workflow_dispatch')
        and (value['conclusion'] in {'success', 'failure', 'timed_out'} if daily else value['conclusion'] == 'success'),
        'ingress_event_ineligible')
    return value


def event_from_run(run, repository):
    require(isinstance(run, dict) and run.get('status') == 'completed' and run.get('head_branch') == 'main'
        and all((run.get(key) or {}).get('full_name') == repository for key in ('repository', 'head_repository'))
        and (run.get('repository') or {}).get('private') is False, 'ingress_run_identity_invalid')
    return checked_event({'repository': repository, **{key: run.get(key) for key in EVENT_FIELDS - {'repository'}}})


def event_id(event):
    checked_event(event)
    return digest(stable_bytes({k: event[k] for k in ('repository', 'path', 'id', 'run_attempt')}))


def key(store, *parts):
    return store.key('publication-ingress', *parts)


def read_optional(store, path, maximum=65536):
    try:
        return store._get(path, maximum=maximum)
    except R2NotFound:
        return None


def immutable_bytes(store, path, raw, kind):
    require(0 < len(raw) <= MAX_ENVELOPE_BYTES, 'ingress_envelope_oversized')
    old = read_optional(store, path, MAX_ENVELOPE_BYTES)
    require(old in (None, raw), 'ingress_immutable_changed')
    if old is None:
        store._put(path, raw, metadata={'kind': kind})
    require(store._get(path, maximum=MAX_ENVELOPE_BYTES) == raw, 'ingress_readback_changed')


def validate_no_publication(event, value):
    require(isinstance(value, dict) and set(value) == {'reason', 'attempts', 'latest_jobs', 'parent_job', 'artifact_inventory_sha256'}
        and value['reason'] in {'no_nested_stages', 'all_nested_stages_skipped'}
        and isinstance(value['attempts'], list) and len(value['attempts']) == event['run_attempt']
        and re.fullmatch(r'[a-f0-9]{64}', str(value['artifact_inventory_sha256'])), 'ingress_terminal_evidence_invalid')
    for index, row in enumerate(value['attempts'], 1):
        require(isinstance(row, dict) and set(row) == {'attempt', 'count', 'sha256'}
            and row['attempt'] == index and type(row['count']) is int and 0 <= row['count'] <= 1000
            and re.fullmatch(r'[a-f0-9]{64}', str(row['sha256'])), 'ingress_terminal_evidence_invalid')
    jobs = value['latest_jobs']
    require(isinstance(jobs, dict), 'ingress_terminal_evidence_invalid')
    if value['reason'] == 'no_nested_stages':
        row = value['parent_job']
        require(jobs == {} and isinstance(row, dict)
            and set(row) == {'id', 'attempt', 'name', 'run_id', 'head_sha', 'status', 'conclusion'}
            and type(row['id']) is int and row['id'] > 0
            and type(row['attempt']) is int and 1 <= row['attempt'] <= event['run_attempt']
            and row['name'] == recovered.DAILY_JOB_PREFIX.removesuffix(' / ')
            and row['run_id'] == event['id'] and row['head_sha'] == event['head_sha']
            and row['status'] == 'completed' and row['conclusion'] == 'skipped', 'ingress_no_work_unproven')
    else:
        require(set(jobs) == set(STAGES) and value['parent_job'] is None, 'ingress_terminal_evidence_invalid')
        ids = set()
        for stage, row in jobs.items():
            require(set(row) == {'id', 'attempt', 'name', 'run_id', 'head_sha', 'status', 'conclusion'}
                and type(row['id']) is int and row['id'] > 0 and row['id'] not in ids
                and type(row['attempt']) is int and 1 <= row['attempt'] <= event['run_attempt']
                and row['name'] == recovered.DAILY_JOB_PREFIX + stage and row['run_id'] == event['id']
                and row['head_sha'] == event['head_sha'] and row['status'] == 'completed'
                and row['conclusion'] == 'skipped', 'ingress_terminal_evidence_invalid')
            ids.add(row['id'])


def authenticate_no_publication(github, event):
    """Only a complete exact-attempt absence/skipped proof can close a hint."""
    require(event['path'] == recovered.DAILY_WORKFLOW, 'ingress_no_work_unproven')
    run = github.api(f"actions/runs/{event['id']}")
    require(event_from_run(run, github.repository) == event, 'ingress_captured_attempt_changed')
    attempts, latest, parent = [], {}, None
    for number in range(1, event['run_attempt'] + 1):
        rows = recovered.attempt_jobs(github, str(event['id']), number)
        attempts.append({'attempt': number, 'count': len(rows), 'sha256': digest(stable_bytes(rows))})
        parents = [row for row in rows if row.get('name') == recovered.DAILY_JOB_PREFIX.removesuffix(' / ')]
        require(len(parents) <= 1, 'ingress_nested_jobs_ambiguous')
        if parents:
            require(parents[0].get('status') == 'completed' and parents[0].get('conclusion') == 'skipped',
                    'ingress_prior_parent_execution_present')
            parent = {**{k: parents[0].get(k) for k in
                ('id', 'name', 'run_id', 'head_sha', 'status', 'conclusion')}, 'attempt': number}
        for stage in STAGES:
            selected = [row for row in rows if row.get('name') == recovered.DAILY_JOB_PREFIX + stage]
            require(len(selected) <= 1, 'ingress_nested_jobs_ambiguous')
            if selected:
                require(selected[0].get('status') == 'completed' and selected[0].get('conclusion') == 'skipped',
                        'ingress_prior_nested_execution_present')
                latest[stage] = {**{k: selected[0].get(k) for k in
                    ('id', 'name', 'run_id', 'head_sha', 'status', 'conclusion')}, 'attempt': number}
    artifacts = github.api(f"actions/runs/{event['id']}/artifacts?per_page=100")
    rows = artifacts.get('artifacts')
    require(isinstance(rows, list) and type(artifacts.get('total_count')) is int
        and artifacts['total_count'] == len(rows) <= 100
        and all(isinstance(row, dict) for row in rows), 'ingress_artifacts_incomplete')
    # Even expired or malformed publication artifacts keep the hint pending.
    require(not any(str(row.get('name', '')).startswith('recovered-publication-') for row in rows),
            'ingress_publication_artifact_present')
    value = {'reason': 'no_nested_stages' if not latest else 'all_nested_stages_skipped',
        'attempts': attempts, 'latest_jobs': latest, 'parent_job': None if latest else parent,
        'artifact_inventory_sha256': digest(stable_bytes(rows))}
    validate_no_publication(event, value)
    after = github.api(f"actions/runs/{event['id']}")
    require(event_from_run(after, github.repository) == event, 'ingress_captured_attempt_changed')
    return value


def validate_frozen(event, publication, evidence):
    """Validate the small authenticated snapshot after source artifacts expire."""
    checked_event(event)
    if isinstance(evidence, dict) and set(evidence) == {'no_publication'}:
        require(publication is None and event['path'] == recovered.DAILY_WORKFLOW,
                'ingress_terminal_evidence_invalid')
        validate_no_publication(event, evidence['no_publication'])
        return
    require(isinstance(evidence, dict) and set(evidence) in ({'jobs', 'artifacts'},
        {'jobs', 'artifacts', 'empty_publication'}), 'ingress_evidence_invalid')
    require(set(evidence['jobs']) == set(STAGES) and set(evidence['artifacts']) == {'request', 'state'},
            'ingress_evidence_inventory_invalid')
    prefix = recovered.DAILY_JOB_PREFIX if event['path'] == recovered.DAILY_WORKFLOW else ''
    ids = set()
    for stage, row in evidence['jobs'].items():
        require(isinstance(row, dict) and set(row) == {'id', 'attempt', 'name', 'run_id', 'head_sha', 'status', 'conclusion', 'started_at', 'completed_at'}
            and type(row['id']) is int and row['id'] > 0 and row['id'] not in ids
            and type(row['attempt']) is int and 1 <= row['attempt'] <= event['run_attempt']
            and row['name'] == prefix + stage and row['run_id'] == event['id']
            and row['head_sha'] == event['head_sha'] and row['status'] == 'completed'
            and row['conclusion'] == 'success', 'ingress_stage_identity_invalid')
        ids.add(row['id'])
        require(recovered.timestamp(row['started_at']) <= recovered.timestamp(row['completed_at']),
                'ingress_stage_time_invalid')
    if publication is None:
        empty = evidence.get('empty_publication', {})
        require(isinstance(empty, dict) and set(empty) == {'request', 'state'}, 'ingress_empty_evidence_invalid')
        request, state = empty['request'], empty['state']
        recovered.checked_request(request)
        require(request['records'] == [] and state.get('schema_version') == 1 and state.get('status') == 'complete'
            and type(state.get('article_count')) is int and state['article_count'] == 0
            and state.get('request_sha256') == recovered.request_hash(request), 'ingress_empty_evidence_invalid')
    else:
        recovered.checked_publication(publication)
        require('empty_publication' not in evidence and publication['repository'] == event['repository']
            and publication['run_id'] == str(event['id']) and publication['attempt'] == str(event['run_attempt'])
            and publication['sha'] == event['head_sha'], 'ingress_publication_identity_invalid')
        request, state = publication['request'], publication['state']
    for kind, value in (('request', request), ('state', state)):
        row = evidence['artifacts'][kind]
        require(isinstance(row, dict) and set(row) == {'id', 'name', 'bytes', 'sha256', 'created_at'}
            and type(row['id']) is int and row['id'] > 0
            and row['name'] == f"recovered-publication-{kind}-{event['id']}"
            and type(row['bytes']) is int and 0 < row['bytes'] <= recovered.MAX_ARTIFACT_BYTES
            and row['sha256'] == digest(stable_bytes(value)), 'ingress_artifact_identity_invalid')
        owner = evidence['jobs']['deliver' if kind == 'request' else 'publish']
        require(recovered.timestamp(owner['started_at']) <= recovered.timestamp(row['created_at'])
                <= recovered.timestamp(owner['completed_at']), 'ingress_artifact_attempt_changed')
    require(evidence['artifacts']['request']['id'] != evidence['artifacts']['state']['id'],
            'ingress_artifact_identity_invalid')


def checked_envelope(value):
    require(isinstance(value, dict) and set(value) == {'schema_version', 'policy', 'event', 'publication', 'evidence'}
        and value['schema_version'] == 1 and value['policy'] == POLICY, 'ingress_envelope_invalid')
    checked_event(value['event'])
    if value['evidence'] is None:
        require(value['publication'] is None, 'ingress_hint_invalid')
    else:
        validate_frozen(value['event'], value['publication'], value['evidence'])
    return value


def persist_envelope(store, event, publication=None, evidence=None):
    value = checked_envelope({'schema_version': 1, 'policy': POLICY, 'event': event,
                             'publication': publication, 'evidence': evidence})
    raw = stable_bytes(value)
    identity = digest(raw)
    path = key(store, 'pending', event_id(event), identity + '.json')
    immutable_bytes(store, path, raw, 'publication-ingress-pending')
    return path, value


def capture(store, github, event):
    require(event['repository'] == github.repository, 'ingress_repository_mismatch')
    # The first object is self-contained and discoverable even if capture stops
    # during API reads or before the richer frozen receipt can be persisted.
    persist_envelope(store, event)
    evidence = {}
    try:
        publication = recovered.authenticate(github, str(event['id']), expected=event, evidence_sink=evidence)
    except ExpansionError:
        try:
            evidence = {'no_publication': authenticate_no_publication(github, event)}
            publication = None
        except ExpansionError:
            return {'captured': True, 'frozen': False, 'event_sha256': event_id(event), 'category': 'authentication_pending'}
    persist_envelope(store, event, publication, evidence)
    return {'captured': True, 'frozen': True, 'event_sha256': event_id(event), 'category': 'captured'}


def pending_inventory(store):
    prefix = key(store, 'pending') + '/'
    result, token = {}, None
    for _ in range(11):
        arguments = {'Bucket': store.bucket, 'Prefix': prefix, 'MaxKeys': 100}
        if token:
            arguments['ContinuationToken'] = token
        try:
            page = store.client.list_objects_v2(**arguments)
        except Exception as error:
            raise classify(error, 'list publication ingress') from error
        rows = page.get('Contents', [])
        require(isinstance(rows, list) and len(rows) <= 100, 'ingress_listing_invalid')
        for row in rows:
            match = re.fullmatch(re.escape(prefix) + r'([a-f0-9]{64})/([a-f0-9]{64})\.json', str(row.get('Key', '')))
            require(match is not None and row['Key'] not in {item for items in result.values() for item in items},
                    'ingress_listing_invalid')
            result.setdefault(match[1], []).append(row['Key'])
            require(sum(map(len, result.values())) <= MAX_PENDING, 'ingress_pending_bound_exceeded')
        if page.get('IsTruncated') is False:
            return result
        next_token = page.get('NextContinuationToken')
        require(isinstance(next_token, str) and next_token and next_token != token, 'ingress_listing_incomplete')
        token = next_token
    raise ExpansionError('ingress_pending_bound_exceeded')


def load_group(store, identity, paths):
    require(0 < len(paths) <= MAX_ENVELOPES, 'ingress_event_conflict')
    values = []
    for path in paths:
        raw = store._get(path, maximum=MAX_ENVELOPE_BYTES)
        require(path.endswith('/' + digest(raw) + '.json'), 'ingress_envelope_checksum_changed')
        value = checked_envelope(json.loads(raw))
        require(event_id(value['event']) == identity, 'ingress_envelope_event_changed')
        values.append(value)
    require(all(value['event'] == values[0]['event'] for value in values), 'ingress_event_conflict')
    full = [value for value in values if value['evidence'] is not None]
    require(len(full) <= 1, 'ingress_event_conflict')
    return full[0] if full else values[0]


def verified_result(store, value, result):
    event, publication = value['event'], value['publication']
    admitted = read_admission(store, result['admission'])
    corpus = read_corpus(store, admitted['generation'])
    proof = recovered.read_proof(store, admitted['recovery'], corpus)
    request_id = recovered.request_hash(publication['request'])
    require(recovered.request_hash(proof['publication']['request']) == request_id
        and result['generation'] == admitted['generation'] and result['pages'] == admitted['pages'],
        'ingress_admission_identity_changed')
    claim = json.loads(store._get(store.key('recovered-publication-claims', request_id, 'receipt.json'), maximum=65536))
    require(claim == {'request_sha256': request_id, 'admission': result['admission']}, 'ingress_admission_claim_missing')
    return {'schema_version': 1, 'policy': POLICY, 'event_sha256': event_id(event),
            'envelope_sha256': digest(stable_bytes(value)), 'disposition': 'admitted',
            'request_sha256': request_id, 'admission': result['admission']}


def producer_outcome(github, admitted, current_producer):
    from review_portal_extended_handoff import admission_is_valid
    producer = checked_producer(admitted['producer'])
    if producer == current_producer:
        return 'pending'
    run = github.api(f"actions/runs/{producer['run_id']}/attempts/{producer['attempt']}")
    require(run.get('id') == int(producer['run_id']) and run.get('head_sha') == producer['sha']
        and run.get('head_branch') == 'main' and run.get('path') == WORKFLOW
        and run.get('event') in {'workflow_run', 'workflow_dispatch'}
        and all((run.get(k) or {}).get('full_name') == producer['repository'] for k in ('repository', 'head_repository'))
        and (run.get('repository') or {}).get('private') is False
        and type(run.get('run_attempt')) is int and run['run_attempt'] == int(producer['attempt']),
        'ingress_admission_producer_changed')
    if run.get('status') != 'completed':
        return 'pending'
    if run.get('conclusion') in {
            'failure', 'cancelled', 'timed_out', 'action_required', 'startup_failure', 'skipped', 'neutral'}:
        return 'failed'
    require(run.get('conclusion') == 'success', 'ingress_admission_producer_unknown')
    jobs = recovered.attempt_jobs(github, producer['run_id'], producer['attempt'])
    admission_is_valid(admitted, run, jobs, github.repository)
    selected = [row for row in jobs if row.get('name') == 'source_snapshot']
    require(len(selected) == 1 and selected[0].get('run_id') == run['id']
        and selected[0].get('head_sha') == producer['sha'], 'ingress_admission_job_changed')
    return 'accepted'


def acknowledgement(store, identity, github, producer):
    raw = read_optional(store, key(store, 'acks', identity + '.json'))
    if raw is None:
        return None
    ack = json.loads(raw)
    require(isinstance(ack, dict) and set(ack) == {'schema_version', 'policy', 'event_sha256',
        'envelope_sha256', 'disposition', 'request_sha256', 'admission'}
        and ack['schema_version'] == 1 and ack['policy'] == POLICY and ack['event_sha256'] == identity
        and re.fullmatch(r'[a-f0-9]{64}', str(ack['envelope_sha256'])), 'ingress_ack_invalid')
    saved = store._get(key(store, 'accepted', identity, ack['envelope_sha256'] + '.json'), maximum=MAX_ENVELOPE_BYTES)
    require(digest(saved) == ack['envelope_sha256'], 'ingress_ack_evidence_changed')
    value = checked_envelope(json.loads(saved))
    require(event_id(value['event']) == identity and value['evidence'] is not None, 'ingress_ack_event_changed')
    if value['publication'] is None:
        require(ack == no_work_ack(value), 'ingress_ack_invalid')
    else:
        admitted = read_admission(store, ack['admission'])
        require(producer_outcome(github, admitted, producer) == 'accepted', 'ingress_admission_producer_pending')
        result = {'admission': ack['admission'], 'generation': admitted['generation'], 'pages': admitted['pages']}
        require(ack == verified_result(store, value, result), 'ingress_ack_admission_changed')
    return ack, value


def no_work_ack(value):
    require(value['publication'] is None and value['evidence'] is not None, 'ingress_no_work_invalid')
    return {'schema_version': 1, 'policy': POLICY, 'event_sha256': event_id(value['event']),
        'envelope_sha256': digest(stable_bytes(value)), 'disposition': 'no_public_articles',
        'request_sha256': None, 'admission': None}


def delete_pending(store, paths):
    for path in paths:
        require(path.startswith(key(store, 'pending') + '/'), 'ingress_delete_scope_invalid')
        try:
            store.client.delete_object(Bucket=store.bucket, Key=path)
        except Exception as error:
            raise classify(error, 'delete acknowledged publication pointer') from error


def reconcile(store, github, session, producer, capture_day, *, clock=time.monotonic, seconds=1200):
    checked_producer(producer)
    require(producer['repository'] == github.repository and 0 < seconds <= 1200, 'ingress_writer_invalid')
    deadline = clock() + seconds
    github.deadline = deadline
    store = R2Store(BudgetClient(store.client, clock, deadline), store.bucket, store.prefix)
    inventory = pending_inventory(store)
    turns = {}
    for identity in inventory:
        raw = read_optional(store, key(store, 'turns', identity + '.json'))
        row = json.loads(raw) if raw else {'run_id': 0, 'attempt': 0}
        require(set(row) == {'run_id', 'attempt'} and all(type(row[k]) is int and row[k] >= 0 for k in row),
                'ingress_turn_invalid')
        turns[identity] = (row['run_id'], row['attempt'])
    summary = {'captured_events': len(inventory), 'checked_events': 0, 'admitted_events': 0, 'no_work_events': 0,
               'awaiting_producer_events': 0,
               'blocked_events': 0, 'retained_events': len(inventory), 'paid_provider_requests': 0}
    for identity in sorted(inventory, key=lambda item: (*turns[item], item))[:MAX_EVENTS]:
        if clock() >= deadline:
            break
        summary['checked_events'] += 1
        try:
            write_verified(store, key(store, 'turns', identity + '.json'),
                {'run_id': int(producer['run_id']), 'attempt': int(producer['attempt'])}, kind='publication-ingress-turn')
            value = load_group(store, identity, inventory[identity])
            event = value['event']
            require(event['repository'] == github.repository, 'ingress_repository_mismatch')
            prior = acknowledgement(store, identity, github, producer)
            if prior is not None:
                require(prior[1]['event'] == event and (value['evidence'] is None or value == prior[1]),
                        'ingress_ack_event_changed')
                delete_pending(store, inventory[identity])
                summary['retained_events'] -= 1
                continue
            if value['evidence'] is None:
                capture(store, github, event)
                paths = pending_inventory(store).get(identity, [])
                value = load_group(store, identity, paths)
                require(value['evidence'] is not None, 'ingress_authentication_pending')
                inventory[identity] = paths
            publication = value['publication']
            if publication is None:
                ack = no_work_ack(value)
            else:
                request_id = recovered.request_hash(publication['request'])
                existing = recovered.existing_admission(store, request_id)
                outcome = producer_outcome(github, existing[1], producer) if existing else None
                if outcome == 'pending':
                    summary['awaiting_producer_events'] += 1
                    continue
                if outcome == 'accepted':
                    result = {'admission': existing[0], 'generation': existing[1]['generation'], 'pages': existing[1]['pages']}
                    # Recover queue-write-before-claim interruption only after
                    # proving the queued producer actually completed.
                    claim_key = store.key('recovered-publication-claims', request_id, 'receipt.json')
                    claim = {'request_sha256': request_id, 'admission': existing[0]}
                    old_claim = read_optional(store, claim_key)
                    if old_claim != stable_bytes(claim):
                        if old_claim:
                            old_value = json.loads(old_claim)
                            old_receipt = read_admission(store, old_value['admission'])
                            old_proof = recovered.read_proof(store, old_receipt['recovery'], read_corpus(store, old_receipt['generation']))
                            require(old_value == {'request_sha256': request_id, 'admission': old_value['admission']}
                                and recovered.request_hash(old_proof['publication']['request']) == request_id,
                                'ingress_prior_claim_changed')
                        write_verified(store, claim_key, claim, kind='recovered-source-claim')
                else:
                    corpus, proof = recovered.collect(session, publication, capture_day, deadline=deadline, clock=clock)
                    require(clock() < deadline, 'ingress_budget_exhausted')
                    if outcome == 'failed':
                        result = recovered.rebind_failed_admission(store, corpus, proof, producer, existing[0])
                    else:
                        result = recovered.admit(store, corpus, proof, producer)
                    verified_result(store, value, result)
                    summary['awaiting_producer_events'] += 1
                    continue
                ack = verified_result(store, value, result)
            raw = stable_bytes(value)
            immutable_bytes(store, key(store, 'accepted', identity, digest(raw) + '.json'), raw, 'publication-ingress-evidence')
            immutable_record(store, key(store, 'acks', identity + '.json'), ack, kind='publication-ingress-ack')
            require(json.loads(store._get(key(store, 'acks', identity + '.json'), maximum=65536)) == ack,
                    'ingress_ack_readback_changed')
            delete_pending(store, inventory[identity])
            summary['admitted_events' if publication else 'no_work_events'] += 1
            summary['retained_events'] -= 1
        except (ExpansionError, R2StoreError, ValueError, TypeError, KeyError):
            # A blocked event is retained; a later event cannot erase its hint.
            summary['blocked_events'] += 1
    return summary


def dispatch_reconcile(github):
    """Exactly one call; an unknown response is never retried here."""
    try:
        result = subprocess.run(['gh', 'api', f'repos/{github.repository}/actions/workflows/'
            'portal-extended-locales-source.yml/dispatches', '--method', 'POST', '--input', '-'],
            input=stable_bytes({'ref': 'main', 'inputs': {'reconcile_only': True}}),
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60, check=False)
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def wake(store, github, hour, *, dispatch=dispatch_reconcile, clock=time.monotonic):
    require(re.fullmatch(r'\d{8}T\d{2}', hour), 'ingress_wake_hour_invalid')
    try:
        datetime.strptime(hour, '%Y%m%dT%H')
    except ValueError:
        raise ExpansionError('ingress_wake_hour_invalid') from None
    store = R2Store(BudgetClient(store.client, clock, clock()+300), store.bucket, store.prefix)
    prefix = key(store, 'pending') + '/'
    try:
        page = store.client.list_objects_v2(Bucket=store.bucket, Prefix=prefix, MaxKeys=1)
    except Exception as error:
        raise classify(error, 'read pending publication wake-up') from error
    rows = page.get('Contents', [])
    require(isinstance(rows, list) and len(rows) <= 1
        and type(page.get('IsTruncated')) is bool, 'ingress_wake_listing_invalid')
    if not rows:
        require(page['IsTruncated'] is False, 'ingress_wake_listing_incomplete')
        return {'pending': False, 'dispatches': 0, 'category': 'empty', 'paid_provider_requests': 0}
    require(isinstance(rows[0], dict) and re.fullmatch(re.escape(prefix)+r'[a-f0-9]{64}/[a-f0-9]{64}\.json',
        str(rows[0].get('Key', ''))), 'ingress_wake_listing_invalid')
    reservation = {'schema_version': 1, 'policy': POLICY, 'hour': hour, 'repository': github.repository,
        'target': WORKFLOW, 'ref': 'main', 'reconcile_only': True}
    marker = key(store, 'wake-reservations', digest(stable_bytes(reservation)) + '.json')
    previous = read_optional(store, marker)
    if previous is not None:
        require(previous == stable_bytes(reservation), 'ingress_wake_reservation_changed')
        return {'pending': True, 'dispatches': 0, 'category': 'hour_already_reserved', 'paid_provider_requests': 0}
    # The dedicated wake job is serialized. Reserve before POST so a crash or
    # an unknown dispatch outcome cannot cause immediate same-hour replay.
    immutable_record(store, marker, reservation, kind='publication-ingress-wake-reservation')
    require(store._get(marker, maximum=65536) == stable_bytes(reservation), 'ingress_wake_readback_changed')
    accepted = dispatch(github)
    return {'pending': True, 'dispatches': 1, 'category': 'dispatched' if accepted else 'dispatch_unknown',
            'paid_provider_requests': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['capture', 'reconcile', 'wake'])
    parser.add_argument('--prefix', default=DEFAULT_PREFIX)
    parser.add_argument('--run-id', default='')
    parser.add_argument('--reconcile-only', action='store_true')
    parser.add_argument('--github-output', type=Path)
    args = parser.parse_args()
    env = os.environ
    workflow = WAKE_WORKFLOW if args.operation == 'wake' else WORKFLOW
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
        and env.get('KC_PUBLIC_REPOSITORY') == 'true'
        and env.get('GITHUB_WORKFLOW_REF') == env.get('GITHUB_REPOSITORY', '') + '/' + workflow + '@refs/heads/main',
        'ingress_main_workflow_required')
    require(not args.reconcile_only or args.operation == 'capture' and not args.run_id
        and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch', 'ingress_reconcile_only_invalid')
    store = R2Store.from_env(args.prefix)
    github = recovered.GitHub(env['GITHUB_REPOSITORY'])
    github.deadline = time.monotonic() + 1200
    if args.operation == 'capture':
        if args.run_id:
            require(re.fullmatch(r'[1-9][0-9]*', args.run_id), 'ingress_run_id_invalid')
            run = github.api(f'actions/runs/{args.run_id}')
        elif env.get('GITHUB_EVENT_NAME') == 'workflow_run':
            path = Path(env['GITHUB_EVENT_PATH'])
            require(path.stat().st_size <= 2 * 1024 * 1024, 'ingress_event_oversized')
            run = json.loads(path.read_bytes())['workflow_run']
        else:
            require(env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch', 'ingress_event_ineligible')
            run = None
        latest_day = not args.reconcile_only and (run is None or run.get('path') == '.github/workflows/neutral-edge-cutover.yml')
        if run is not None and latest_day:
            require(run.get('status') == 'completed' and run.get('conclusion') == 'success'
                and run.get('head_branch') == 'main'
                and all((run.get(k) or {}).get('full_name') == github.repository for k in ('repository', 'head_repository'))
                and (run.get('repository') or {}).get('private') is False, 'ingress_neutral_event_unverified')
        result = {'captured': False, 'frozen': False}
        if run is not None and not latest_day:
            result = capture(store, github, event_from_run(run, github.repository))
        if args.github_output:
            with args.github_output.open('a') as stream:
                stream.write('latest_day=' + str(latest_day).lower() + '\n')
    elif args.operation == 'reconcile':
        from portal_extended_incremental import today
        producer = {'run_id': env['GITHUB_RUN_ID'], 'attempt': env['GITHUB_RUN_ATTEMPT'],
            'sha': env['GITHUB_SHA'], 'repository': github.repository, 'workflow': WORKFLOW}
        with requests.Session() as session:
            result = reconcile(store, github, session, producer, today())
    else:
        require(env.get('GITHUB_EVENT_NAME') in {'schedule', 'workflow_dispatch'} and not args.run_id,
                'ingress_wake_event_invalid')
        result = wake(store, github, datetime.now(timezone.utc).strftime('%Y%m%dT%H'))
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (ExpansionError, R2StoreError, ValueError, TypeError, KeyError, OSError):
        print(json.dumps({'status': 'blocked', 'category': 'publication_ingress_unavailable'}))
        raise SystemExit(1)
