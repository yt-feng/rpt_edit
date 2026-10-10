#!/usr/bin/env python3
"""Bounded, exact old fallback recovery in the existing serialized locale matrix."""
from __future__ import annotations
import argparse
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import time

from portal_extended_locales import ExpansionError, digest, stable_bytes, select_locales, daily_corpus_day
from portal_extended_repair_contract import QUALITY_POLICY, quality_contract
from portal_extended_french_repair import RepairPipeline
from portal_extended_r2 import R2Store, DEFAULT_PREFIX, R2NotFound, HEX64, MAX_SOURCE_BYTES
from portal_extended_continuation import (queue, save_queue, read_origin, origin_allows_locale,
    producer_identity, checkpoint_evidence, MAX_CONTINUATIONS)
from portal_extended_incremental import read_state, write_state, content_key
from portal_extended_daily_queue import immutable_record
from portal_extended_quality import (debt_rows, candidate_quality, proof_key, MAX_PROOF_BYTES,
                                     publication_ready, record_quality)
from build_portal_extended_locales import NUMERIC_FALLBACK_CODES

MAX_GENERATIONS_PER_SCAN = 4
MAX_UNITS_PER_SCAN = 60

MAX_SCAN_SECONDS = 300
MAX_SCAN_R2_READS = 1200
MAX_SCAN_API_READS = 16


class ScanBudgetStop(BaseException):
    # R2Store translates Exception into transport failures; this local control
    # signal must preserve its identity across that adapter without retrying I/O.
    pass


class ScanBudget:
    def __init__(self, *, seconds=MAX_SCAN_SECONDS, reads=MAX_SCAN_R2_READS, api_reads=MAX_SCAN_API_READS, clock=time.monotonic):
        self.clock, self.deadline = clock, clock()+seconds
        self.read_limit, self.api_limit = reads, api_reads
        self.reads = self.api_reads = 0
        self.stopped = False

    def consume(self, kind):
        count, limit = (self.reads,self.read_limit) if kind == 'r2' else (self.api_reads,self.api_limit)
        if self.clock() >= self.deadline or count >= limit:
            self.stopped = True
            raise ScanBudgetStop()
        if kind == 'r2': self.reads += 1
        else: self.api_reads += 1

    def storage(self, store):
        budget = self
        class Client:
            def __getattr__(self, name):
                operation = getattr(store.client,name)
                if name not in {'head_object','get_object'}: return operation
                def read(**kwargs):
                    budget.consume('r2')
                    return operation(**kwargs)
                return read
        return R2Store(Client(),store.bucket,store.prefix)

    def snapshot(self):
        return {'budget_stopped':self.stopped,'r2_reads':self.reads,'api_reads':self.api_reads,
                'max_seconds':MAX_SCAN_SECONDS,'max_r2_reads':self.read_limit,'max_api_reads':self.api_limit}


def ordered_locales(store, locales):
    key=store.key('incremental','quality-recovery-scheduler','cursor.json')
    try: value=json.loads(store._get(key,maximum=4096))
    except R2NotFound: return tuple(locales)
    require(isinstance(value,dict) and set(value)=={'schema_version','next_locale'} and value['schema_version']==1
            and select_locales(value['next_locale'])==(value['next_locale'],),'scheduler_cursor_invalid')
    all_locales=list(select_locales('all-supported'))
    start=all_locales.index(value['next_locale'])
    ordered=all_locales[start:]+all_locales[:start]
    return tuple(locale for locale in ordered if locale in locales)


def scheduler_cursor(store, locale):
    # Constant-size control metadata uses the original store so exhausted scan
    # reads cannot prevent recording where to resume. It grants no inference.
    store._put(store.key('incremental','quality-recovery-scheduler','cursor.json'),
        stable_bytes({'schema_version':1,'next_locale':locale}),metadata={'kind':'quality-recovery-cursor'})



class Blocked(ExpansionError):
    pass


def require(ok, code):
    if not ok: raise Blocked(code)


def plan_key(store, identity):
    require(isinstance(identity, str) and HEX64.fullmatch(identity), 'plan_identity_invalid')
    return store.key('incremental', 'quality-recovery-plans', identity, 'request.json')


def read_plan(store, identity):
    raw = store._get(plan_key(store, identity), maximum=65536)
    require(digest(raw) == identity, 'plan_checksum_invalid')
    plan = json.loads(raw)
    require(set(plan) == {'schema_version', 'policy', 'locale', 'generation', 'day', 'owner', 'request',
                         'quality_proof_sha256', 'selection', 'mode', 'requires_engine'} and plan['schema_version'] == 1
            and plan['policy'] == QUALITY_POLICY and plan['mode'] in {'repair','prepared-tail'}, 'plan_contract_invalid')
    pipeline = RepairPipeline(quality_contract(plan['locale']))
    pipeline.units.request(plan['request'])
    producer_identity(plan['owner'])
    selection = plan['selection']
    require(isinstance(selection, dict) and set(selection) == {'accepted_ledger_units','fresh_authorized_units',
        'terminal_units','unresolved_units'} and all(type(v) is int and 0 <= v <= MAX_UNITS_PER_SCAN for v in selection.values())
        and selection['accepted_ledger_units'] == sum(mode == 'accepted-ledger' for mode in plan['request']['unit_modes'].values())
        and selection['fresh_authorized_units'] == sum(mode == 'fresh-authorized' for mode in plan['request']['unit_modes'].values())
        and type(plan['requires_engine']) is bool and plan['requires_engine'] == (selection['fresh_authorized_units'] > 0),
        'plan_selection_invalid')
    require(HEX64.fullmatch(plan['generation']) and HEX64.fullmatch(plan['quality_proof_sha256']),
            'plan_source_identity_invalid')
    return plan


def verify_debt(store, locale, generation, debt):
    raw = store._get(proof_key(store, debt['proof_sha256']), maximum=MAX_PROOF_BYTES)
    require(digest(raw) == debt['proof_sha256'], 'debt_proof_checksum_invalid')
    proof = json.loads(raw)
    expected = candidate_quality(store, locale, generation, debt['candidate_id'])
    require(proof == expected and proof['render_complete'] and not proof['translation_ready']
            and proof['quality_status'] == 'source-fallback'
            and all(proof[k] == debt[k] for k in ('candidate_id','source_fallback_unit_count','quality_status')),
            'debt_proof_binding_invalid')
    return proof


def anchor_key(store, quality_sha):
    require(isinstance(quality_sha,str) and HEX64.fullmatch(quality_sha),'anchor_identity_invalid')
    return store.key('incremental','quality-recovery-anchors',quality_sha,'receipt.json')


def exact_result(store, locale, generation, row):
    raw=stable_bytes(row)
    key=store.key('incremental','continuation-results',generation,locale,digest(raw)+'.json')
    require(store._get(key,maximum=65536) == raw,'historical_result_checksum_invalid')
    require(row.get('status') == 'complete' and type(row.get('continuations')) is int
            and 0 <= row['continuations'] <= MAX_CONTINUATIONS
            and set(row) <= {'status','continuations','snapshot','source_repair_sha256','source_repair_completion_sha256'},
            'historical_result_contract_invalid')
    return row


def save_ack_anchor(store, locale, generation, row, quality):
    """Keep the full immutable outcome, including repair proofs, before ACK."""
    if quality['translation_ready']: return
    exact_result(store,locale,generation,row)
    require(row['snapshot']['candidate_id'] == quality['candidate_id']
            and row['snapshot']['manifest_sha256'] == quality['manifest_sha256'],'anchor_quality_mismatch')
    value={'schema_version':1,'locale':locale,'generation':generation,
           'quality_proof_sha256':quality['proof_sha256'],'row':row}
    immutable_record(store,anchor_key(store,quality['proof_sha256']),value,kind='quality-recovery-anchor')


def verify_previous_repair(store, locale, generation, row, repository, api):
    if 'source_repair_sha256' not in row:
        require('source_repair_completion_sha256' not in row,'orphan_repair_completion')
        return
    from portal_extended_french_repair import read_repair_pipeline
    identity=row['source_repair_sha256']
    pipeline=read_repair_pipeline(store,identity)
    require(pipeline.locale == locale,'anchor_repair_locale_mismatch')
    proof=pipeline.verify_proof(store,identity,generation,row['snapshot']['candidate_id'],row['snapshot']['checkpoint_sha256'])
    completion_id=row.get('source_repair_completion_sha256')
    completion=pipeline.verify_completion(store,completion_id,proof,identity) if completion_id else None
    expected={**proof['after_row'],'source_repair_sha256':identity}
    if completion_id: expected['source_repair_completion_sha256']=completion_id
    require(row == expected,'anchor_repair_full_row_mismatch')
    owner=(completion or proof)['producer']
    path=f'repos/{repository}/actions/runs/{owner["run_id"]}/attempts/{owner["attempt"]}'
    response=api(path+'/jobs?per_page=100')
    require(type(response.get('total_count')) is int and 0 < response['total_count'] <= 100
        and len(response.get('jobs',[])) == response['total_count'],'repair_job_inventory_incomplete')
    pipeline.verify_repair_producer(proof,api(path),response['jobs'],repository,completion=completion)


def complete_snapshot(store, pipeline, generation, proof, workspace):
    """A pointer supplies a hash; an immutable result proves its old ownership."""
    locale = pipeline.locale
    rows = queue(store, locale)
    existing = rows.get(generation)
    if existing is not None:
        require(existing['status'] == 'complete' and existing['snapshot']['candidate_id'] == proof['candidate_id']
                and existing['snapshot']['manifest_sha256'] == proof['manifest_sha256'], 'registered_outcome_advanced')
        return existing, False
    checksum=digest(stable_bytes(proof))
    try: raw=store._get(anchor_key(store,checksum),maximum=65536)
    except R2NotFound: raw=None
    if raw is not None:
        anchor=json.loads(raw)
        require(isinstance(anchor,dict) and set(anchor) == {'schema_version','locale','generation','quality_proof_sha256','row'}
                and anchor['schema_version'] == 1 and anchor['locale'] == locale and anchor['generation'] == generation
                and anchor['quality_proof_sha256'] == checksum and raw == stable_bytes(anchor),'historical_anchor_invalid')
        row=exact_result(store,locale,generation,anchor['row'])
        require(row['snapshot']['candidate_id'] == proof['candidate_id']
                and row['snapshot']['manifest_sha256'] == proof['manifest_sha256'],'anchor_quality_mismatch')
        return row, True
    path = workspace/'old-checkpoint.json'
    pointer = store.restore_checkpoint(locale, generation, path)
    require(pointer.get('present'), 'historical_checkpoint_missing')
    snapshot = {'checkpoint_sha256': pointer['sha256'], 'candidate_id': proof['candidate_id'],
                'manifest_sha256': proof['manifest_sha256'], 'completed_pages': proof['completed_page_count'],
                'resolved_units': len(checkpoint_evidence(store, locale, generation, pointer['sha256']))}
    matches = []
    for count in range(MAX_CONTINUATIONS+1):
        row = {'status':'complete', 'continuations':count, 'snapshot':snapshot}
        raw = stable_bytes(row)
        key = store.key('incremental','continuation-results',generation,locale,digest(raw)+'.json')
        try: found = store._get(key, maximum=65536)
        except R2NotFound: continue
        require(found == raw, 'historical_result_checksum_invalid')
        matches.append(row)
    require(len(matches) == 1, 'historical_result_not_unique')
    return matches[0], True


def normal_work(store, locale):
    if any(row['status'] != 'complete' for row in queue(store, locale).values()): return True
    from portal_extended_daily_queue import all_queued, inventory, pending_docs
    for item in all_queued(store):
        # all_queued returns authenticated queue entries, never fresh public data.
        _, corpus = inventory(store, item)
        if pending_docs(store, corpus['documents'], locale, item['day']): return True
    return False


def status(store, locale, generation, code, **counts):
    values = read_state(store, 'quality-recovery-status', locale).get('generations', {})
    require(isinstance(values, dict) and len(values) <= 500, 'recovery_status_invalid')
    values[generation] = {'code':code, **counts}
    require(len(values) <= 500, 'recovery_status_full')
    write_state(store, 'quality-recovery-status', locale, {'generations':values})


def prepare_one(store, locale, generation, debt, owner, repository, api):
    pipeline = RepairPipeline(quality_contract(locale))
    proof = verify_debt(store, locale, generation, debt)
    if publication_ready(proof):
        # Reuse the existing bounded, cursor-based scan to migrate old numeric
        # debt. The exact immutable proof/source/manifest was authenticated
        # above; remove only its queue row, never its honest fallback evidence.
        record_quality(store, locale, generation, proof['candidate_id'],
                       manifest_sha256=proof['manifest_sha256'])
        status(store, locale, generation, 'numeric_advisory_no_repair',
               skipped_numeric_units=proof['source_fallback_unit_count'], fresh_authorized_units=0)
        return None
    origin = read_origin(store, generation)
    require(origin is not None and origin_allows_locale(origin, locale)
            and origin['source_sha256'] == proof['source_sha256'], 'historical_origin_unproven')
    with tempfile.TemporaryDirectory(prefix='quality-recovery-') as temporary:
        workspace = Path(temporary)
        row, restore = complete_snapshot(store, pipeline, generation, proof, workspace)
        verify_previous_repair(store,locale,generation,row,repository,api)
        request = {'policy':pipeline.policy, 'validator_revision':pipeline.revision, 'locale':locale,
            'source_sha256':proof['source_sha256'], 'origin_sha256':digest(stable_bytes(origin)),
            'producer':origin['producer'], **{k:row['snapshot'][k] for k in
                ('checkpoint_sha256','candidate_id','manifest_sha256')}, 'units':[], 'unit_modes':{}}
        corpus, old, candidate, _, snapshot, inspection = pipeline.frozen(store, generation, request, workspace)
        pipeline.authenticate_original(store, origin, repository, api)
        require(snapshot == row['snapshot'], 'historical_snapshot_changed')
        # Never write an ACK restoration until every original page receipt and
        # the full immutable source/checkpoint/render binding has been verified.
        pages = read_state(store, 'completed', locale, daily_corpus_day(corpus)).get('pages', {})
        require(isinstance(pages, dict) and all(isinstance(pages.get(doc['url']), dict)
                and pages[doc['url']].get('content_key') == content_key(doc)
                and pages[doc['url']].get('generation') == generation
                and pages[doc['url']].get('candidate_id') == proof['candidate_id'] for doc in corpus['documents']),
                'completed_page_receipt_advanced')
        required = pipeline.units.required_units(corpus)
        eligible = inspection['eligible_units']
        selection = {'accepted_ledger_units':0, 'fresh_authorized_units':0, 'terminal_units':0, 'unresolved_units':0}
        cursor = read_state(store, 'quality-recovery-cursor', locale).get('offsets', {})
        require(isinstance(cursor, dict) and len(cursor) <= 500, 'recovery_cursor_invalid')
        offset = cursor.get(generation, 0)
        require(type(offset) is int and offset >= 0, 'recovery_cursor_invalid')
        ordered = eligible[offset % len(eligible):] + eligible[:offset % len(eligible)] if eligible else []
        scanned = 0
        skipped_numeric_units = 0
        old_fallbacks = json.loads(old).get('source_fallbacks', {})
        for unit in ordered[:MAX_UNITS_PER_SCAN]:
            scanned += 1
            claim, outcome, legacy = pipeline.units.prior_outcome(store, unit, required[unit])
            if (old_fallbacks.get(unit, {}).get('code') in NUMERIC_FALLBACK_CODES
                    and (outcome is None or outcome['status'] != 'accepted')):
                # Keep the exact source fallback and its honest untranslated
                # count. Numeric prose quality alone no longer authorizes a
                # provider call, including after an old terminal attempt.
                skipped_numeric_units += 1
                continue
            if claim is not None and outcome is None:
                selection['unresolved_units'] += 1
            elif outcome is not None and outcome['status'] == 'terminal':
                selection['terminal_units'] += 1
            else:
                request['units'].append(unit)
                request['unit_modes'][unit] = 'accepted-ledger' if outcome else 'fresh-authorized'
                selection['accepted_ledger_units' if outcome else 'fresh_authorized_units'] += 1
            if len(request['units']) == 20: break
        cursor[generation] = (offset+scanned) % len(eligible) if eligible else 0
        write_state(store, 'quality-recovery-cursor', locale, {'offsets':cursor})
        request['units'].sort()
        if not request['units']:
            status(store, locale, generation, 'no_retryable_units', **selection,
                   skipped_numeric_units=skipped_numeric_units)
            return None
        pipeline.units.request(request)
        if restore:
            rows = queue(store, locale)
            require(generation not in rows, 'registered_outcome_advanced')
            rows[generation] = row
            save_queue(store, locale, rows)
        before, _ = pipeline.guard_current(store, corpus, snapshot)
        immutable_record(store, pipeline.claim_key(store, request, owner),
            {'request':request, 'producer':producer_identity(owner), 'before_row':before}, kind='quality-repair-claim')
        plan = {'schema_version':1, 'policy':QUALITY_POLICY, 'locale':locale, 'generation':generation,
            'day':daily_corpus_day(corpus), 'owner':producer_identity(owner), 'request':request,
            'quality_proof_sha256':debt['proof_sha256'], 'selection':selection, 'mode':'repair',
            'requires_engine':selection['fresh_authorized_units'] > 0}
        identity = digest(stable_bytes(plan))
        immutable_record(store, plan_key(store, identity), plan, kind='quality-recovery-plan')
        # Save the exact plan before launch so an interrupted prepared tail can be
        # retried without selecting new units or introducing a new source.
        write_state(store, 'quality-recovery-active', locale, {'plan':identity})
        status(store, locale, generation, 'selected', **selection,
               skipped_numeric_units=skipped_numeric_units)
        return {'locale':locale, 'generation':generation, 'day':plan['day'], 'quality_repair':identity}


def prepare(store, locales, owner, repository, api, *, budget=None):
    budget = budget or ScanBudget()
    control_store = store
    locales = ordered_locales(control_store,locales)
    store = budget.storage(store)
    jobs, blocked = [], []
    # Cache exact original run/job reads within this source job, not across runs.
    responses = {}
    def cached_api(path):
        if path not in responses:
            budget.consume('api')
            responses[path] = api(path)
        return responses[path]
    for locale_index, locale in enumerate(locales):
        try:
            rows = queue(store, locale)
            # Original incomplete page generation keeps its existing priority/claim.
            if any(row['status'] != 'complete' for row in rows.values()): continue
            turn = read_state(store, 'quality-recovery-turn', locale).get('last', 'ordinary')
            require(turn in {'ordinary','quality'}, 'recovery_turn_invalid')
            if turn == 'quality' and normal_work(store, locale): continue
            entries = sorted(debt_rows(store, locale).items())
            if not entries: continue
            authorize()
            scan = read_state(store, 'quality-recovery-scan', locale).get('offset', 0)
            require(type(scan) is int and scan >= 0, 'recovery_scan_invalid')
            entries = entries[scan % len(entries):] + entries[:scan % len(entries)]
            for index, (generation, debt) in enumerate(entries[:MAX_GENERATIONS_PER_SCAN], 1):
                write_state(store, 'quality-recovery-scan', locale, {'offset':(scan+index) % len(entries)})
                try:
                    job = prepare_one(store, locale, generation, debt, owner, repository, cached_api)
                except ScanBudgetStop:
                    write_state(control_store,'quality-recovery-scan',locale,{'offset':(scan+index-1) % len(entries)})
                    raise
                except (ExpansionError, R2NotFound, ValueError, KeyError, TypeError) as error:
                    code = str(error) if isinstance(error, Blocked) else 'historical_evidence_unverifiable'
                    status(store, locale, generation, code)
                    blocked.append({'locale':locale,'generation':generation,'code':code})
                    continue
                if job:
                    jobs.append(job)
                    write_state(store, 'quality-recovery-turn', locale, {'last':'quality'})
                    break
        except ScanBudgetStop:
            scheduler_cursor(control_store,locale)
            blocked.append({'locale':locale,'code':'scan_budget_exhausted'})
            break
        finally:
            if not budget.stopped:
                scheduler_cursor(control_store,locales[(locale_index+1) % len(locales)])
    return jobs, blocked


def resume_prepared(store, locales, owner, repository, api, *, budget=None):
    """Keep a tail recoverable until its actual source/locale jobs succeeded."""
    budget = budget or ScanBudget()
    control_store = store
    locales = ordered_locales(control_store,locales)
    store = budget.storage(store)
    resumed, responses = [], {}
    def cached_api(path):
        if path not in responses:
            budget.consume('api')
            responses[path] = api(path)
        return responses[path]
    for locale in locales:
        try:
            identity = read_state(store, 'quality-recovery-active', locale).get('plan')
            if not identity: continue
            plan = read_plan(store, identity)
            require(plan['locale'] == locale, 'active_plan_locale_mismatch')
            pipeline = RepairPipeline(quality_contract(locale))
            proof_id = pipeline.prepared_proof(store, plan['request'])
            if proof_id is None: continue
            authorize()
            pipeline.authenticate_original(store, read_origin(store, plan['generation']), repository, cached_api)
            proof = pipeline.verify_proof(store, proof_id, plan['generation'])
            if not proof['delta']['changed']:
                write_state(store, 'quality-recovery-active', locale, {'plan':''})
                continue
            current = queue(store, locale).get(plan['generation'], {})
            expected = {**proof['after_row'], 'source_repair_sha256':proof_id}
            if not current and plan['generation'] not in debt_rows(store, locale):
                write_state(store, 'quality-recovery-active', locale, {'plan':''})
                continue
            if {k:v for k,v in current.items() if k != 'source_repair_completion_sha256'} == expected:
                completion_id = current.get('source_repair_completion_sha256')
                completion = pipeline.verify_completion(store, completion_id, proof, proof_id) if completion_id else None
                producer = (completion or proof)['producer']
                path = f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
                response = cached_api(path+'/jobs?per_page=100')
                require(type(response.get('total_count')) is int and 0 < response['total_count'] <= 100
                    and len(response.get('jobs',[])) == response['total_count'], 'repair_job_inventory_incomplete')
                try:
                    pipeline.verify_repair_producer(proof, cached_api(path), response['jobs'], repository, completion=completion)
                except ExpansionError:
                    # A committed candidate whose original job failed still needs
                    # a successful, authenticated source-only completion receipt.
                    pass
                else:
                    # Refresh quality first: queue-after alone does not prove the
                    # final quality receipt persisted before a lost acknowledgement.
                    from portal_extended_quality import record_quality
                    record_quality(store, locale, plan['generation'], proof['delta']['new']['candidate_id'],
                                   manifest_sha256=proof['delta']['new']['manifest_sha256'])
                    write_state(store, 'quality-recovery-active', locale, {'plan':''})
                    continue
            pipeline.commit_prepared(store, proof_id)
            pipeline.record_completion(store, proof_id, proof, owner)
            newplan = {**plan, 'owner':producer_identity(owner), 'mode':'prepared-tail'}
            new_id = digest(stable_bytes(newplan))
            immutable_record(store, plan_key(store,new_id), newplan, kind='quality-recovery-tail')
            # Do not clear before this source job has actually succeeded. A later
            # source step may fail; the following serialized run can rebind tail.
            write_state(store, 'quality-recovery-active', locale, {'plan':new_id})
            resumed.append(new_id)
        except ScanBudgetStop:
            scheduler_cursor(control_store,locale)
            break
        except (ExpansionError, R2NotFound, ValueError, KeyError, TypeError):
            write_state(control_store, 'quality-recovery-tail-status', locale, {'code':'prepared_tail_evidence_blocked'})
    return resumed


def pending_tail_locales(store, locales, *, completed=()):
    """Read only bounded control records before allowing ordinary memo writes.

    This inventory is independent of the exhausted deep-scan budget: at most
    three small objects per configured locale, never sources, pages or ledgers.
    A model-unit started without a sealed prepared proof does not reserve a lane.
    """
    reserved=[]
    for locale in locales:
        if locale in completed: continue
        identity=read_state(store,'quality-recovery-active',locale).get('plan')
        if not identity: continue
        plan=read_plan(store,identity)
        require(plan['locale']==locale,'active_plan_locale_mismatch')
        pipeline=RepairPipeline(quality_contract(locale))
        if pipeline.prepared_proof(store,plan['request']) is not None:
            reserved.append(locale)
    return tuple(reserved)


def mark_ordinary(store, jobs):
    for job in jobs:
        if job['locale'] != 'en' and not job.get('quality_repair'):
            write_state(store, 'quality-recovery-turn', job['locale'], {'last':'ordinary'})


def followup(store, identities, owner):
    require(isinstance(identities, list) and len(identities) <= 33 and len(set(identities)) == len(identities),
            'followup_plan_inventory_invalid')
    accepted = terminal = cache_only = fresh = blocked = 0
    should_continue = False
    for identity in identities:
        plan = read_plan(store, identity)
        require(plan['owner'] == producer_identity(owner), 'followup_plan_owner_mismatch')
        pipeline = RepairPipeline(quality_contract(plan['locale']))
        proof_id = pipeline.prepared_proof(store, plan['request'])
        if proof_id is None:
            blocked += 1
            continue
        proof = pipeline.verify_proof(store, proof_id, plan['generation'])
        require(proof['request'] == plan['request'], 'followup_proof_owner_mismatch')
        completion_id = None
        if plan['mode'] == 'repair':
            require(proof['producer'] == plan['owner'], 'followup_proof_owner_mismatch')
        else:
            completion_id = queue(store, plan['locale']).get(plan['generation'], {}).get('source_repair_completion_sha256')
            completion = pipeline.verify_completion(store, completion_id, proof, proof_id)
            require(completion['producer'] == owner, 'followup_completion_owner_mismatch')
        delta = proof['delta']
        expected = {**proof['after_row'], 'source_repair_sha256':proof_id} if delta['changed'] else proof['before_row']
        if completion_id is not None: expected['source_repair_completion_sha256'] = completion_id
        current = queue(store, plan['locale']).get(plan['generation'])
        # A prepared object alone is not durable accepted progress. The complete
        # queue+quality proof must acknowledge its exact candidate after commit.
        if current != expected:
            blocked += 1
            continue
        quality = candidate_quality(store, plan['locale'], plan['generation'], delta['new']['candidate_id'],
                                    manifest_sha256=delta['new']['manifest_sha256'])
        progress = delta['fallbacks_before'] - delta['fallbacks_after'] if delta['changed'] else 0
        require(progress == (len(delta['accepted_units']) if delta['changed'] else 0), 'followup_progress_invalid')
        accepted += progress
        terminal += len(delta['terminal_units'])
        if plan['mode'] == 'prepared-tail':
            cache_only += progress
        else:
            cache_only += delta['unit_attempt_modes']['cache-only'] + delta['unit_attempt_modes']['accepted-ledger']
            fresh += delta['unit_attempt_modes']['fresh-inference']
        if progress > 0 and (debt_rows(store, plan['locale']) or normal_work(store, plan['locale'])):
            should_continue = True
    return {'continue':should_continue, 'accepted_units':accepted, 'still_fallback_terminal_units':terminal,
            'cache_only_units':cache_only, 'fresh_inference_unit_attempts':fresh, 'blocked_plans':blocked,
            'paid_provider_requests':0}


def authorize():
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
        and os.environ.get('KC_PUBLIC_REPOSITORY') == 'true'
        and os.environ.get('GITHUB_EVENT_NAME') in {'workflow_dispatch','workflow_run'}
        and os.environ.get('GITHUB_WORKFLOW_REF') == os.environ.get('GITHUB_REPOSITORY','')+
            '/.github/workflows/portal-extended-locales-r2.yml@refs/heads/main', 'reviewed_main_actions_required')
    return producer_identity({'run_id':os.environ['GITHUB_RUN_ID'], 'attempt':os.environ['GITHUB_RUN_ATTEMPT'],
                              'sha':os.environ['GITHUB_SHA']})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['restore','build','persist','followup'])
    for name in ('plan','locale','generation'): parser.add_argument('--'+name, default='')
    parser.add_argument('--plans', default='[]')
    parser.add_argument('--prefix', default=DEFAULT_PREFIX)
    for name in ('corpus','checkpoint','output','github-output'): parser.add_argument('--'+name, type=Path)
    parser.add_argument('--seconds', type=int, default=14400)
    args = parser.parse_args()
    owner = authorize()
    store = R2Store.from_env(args.prefix)
    if args.operation == 'followup':
        outcome = followup(store, json.loads(args.plans), owner)
        if args.github_output:
            with args.github_output.open('a') as file: file.write('continue='+str(outcome['continue']).lower()+'\n')
        print(json.dumps(outcome, sort_keys=True))
        return 0
    plan = read_plan(store, args.plan)
    require(plan['owner'] == owner and plan['locale'] == args.locale and plan['generation'] == args.generation,
            'job_plan_binding_invalid')
    args.requires_engine = plan['requires_engine']
    pipeline = RepairPipeline(quality_contract(args.locale))
    result = pipeline.run(args, plan['request'], owner, store=store, repository=os.environ['GITHUB_REPOSITORY'],
                        api=lambda path: (_ for _ in ()).throw(ExpansionError('Unexpected source authentication request')))
    return result


if __name__ == '__main__':
    try: raise SystemExit(main())
    except (ExpansionError, R2NotFound, ValueError, KeyError, TypeError):
        print(json.dumps({'status':'blocked','code':'quality_recovery_contract_rejected'}))
        raise SystemExit(1)
