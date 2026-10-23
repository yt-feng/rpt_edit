"""Transfer only unused source-job claims; retain original source and CPU bounds.

Used by the ordinary source job under the existing pipeline concurrency group.
Inspection is read-only. Transfers commit after all source preparation, before
matrix outputs are exposed, and preserve status, snapshot and continuation count.
"""
from __future__ import annotations

import copy
import os
import threading
import time

from portal_extended_continuation import (MAX_CONTINUATIONS, producer_identity,
    queue, read_origin, save_queue, validate_snapshot, verify_origin_run)
from portal_extended_daily_queue import batch_admission, immutable_record
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import R2NotFound

WORKFLOW = '.github/workflows/portal-extended-locales-r2.yml'
POLICY = 'unstarted-source-claim-transfer-v1'
MAX_OWNER_RUNS = 8
MAX_ORIGIN_LOOKUPS = 8
MAX_API_READS = 64
MAX_API_SECONDS = 180
MAX_JOBS = 100
MAX_RECEIPT_BYTES = 65536


class UnprovedClaim(ExpansionError):
    pass


class ScanBoundReached(UnprovedClaim):
    pass


def require(condition, code):
    if not condition:
        raise UnprovedClaim(code)


def current_owner():
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
        and os.environ.get('GITHUB_REF') == 'refs/heads/main'
        and os.environ.get('GITHUB_EVENT_NAME') in {'workflow_dispatch', 'workflow_run'}
        and os.environ.get('KC_PUBLIC_REPOSITORY') == 'true'
        and os.environ.get('GITHUB_WORKFLOW_REF') == repository+'/'+WORKFLOW+'@refs/heads/main',
        'reviewed_main_source_required')
    return producer_identity({'run_id':os.environ.get('GITHUB_RUN_ID'),
        'attempt':os.environ.get('GITHUB_RUN_ATTEMPT'), 'sha':os.environ.get('GITHUB_SHA')})


def run_identity(run, owner, repository):
    require(isinstance(run, dict)
        and run.get('id') == int(owner['run_id']) and run.get('run_attempt') == int(owner['attempt'])
        and run.get('head_sha') == owner['sha'] and run.get('status') == 'completed'
        and run.get('path') == WORKFLOW and run.get('head_branch') == 'main'
        and run.get('event') in {'workflow_dispatch', 'workflow_run'}
        and all((run.get(k) or {}).get('full_name') == repository for k in ('repository', 'head_repository'))
        and (run.get('repository') or {}).get('private') is False,
        'owner_run_unproved')
    return {key:run[key] for key in ('id','run_attempt','head_sha','status','conclusion','path','head_branch','event')}


def all_jobs(api, path, owner):
    response = api(path+'/jobs?per_page=100')
    jobs = response.get('jobs') if isinstance(response, dict) else None
    require(isinstance(jobs, list) and type(response.get('total_count')) is int
        and 0 < len(jobs) == response['total_count'] <= MAX_JOBS, 'owner_jobs_incomplete')
    require(all(isinstance(job, dict) and type(job.get('id')) is int and job['id'] > 0
        and job.get('run_id') == int(owner['run_id']) and job.get('head_sha') == owner['sha']
        and job.get('status') == 'completed' for job in jobs)
        and len({job['id'] for job in jobs}) == len(jobs), 'owner_job_identity_unproved')
    return jobs


def unused_owner(api, owner, repository):
    """Latest and exact attempts must agree before and after the full job read."""
    owner = producer_identity(owner)
    latest = f'repos/{repository}/actions/runs/{owner["run_id"]}'
    path = latest+'/attempts/'+owner['attempt']
    before = run_identity(api(latest), owner, repository)
    exact = run_identity(api(path), owner, repository)
    require(before == exact and exact['conclusion'] in {'failure','cancelled','timed_out'}, 'owner_outcome_unproved')
    jobs = all_jobs(api, path, owner)
    sources = [job for job in jobs if job.get('name') == 'source']
    require(len(sources) == 1 and sources[0].get('conclusion') in {'failure','cancelled','timed_out'},
            'owner_source_not_failed')
    # A skipped, unexpanded matrix has a populated started_at on GitHub. Only
    # skipped + no runner + no steps is accepted, never timestamps alone.
    workers = [job for job in jobs if str(job.get('name', '')).startswith('locale (')]
    require(bool(workers), 'owner_locale_inventory_missing')
    require(all(job.get('conclusion') == 'skipped' and job.get('runner_id') is None
        and job.get('runner_name') is None and job.get('steps') == []
        for job in jobs if job is not sources[0]), 'owner_worker_may_have_started')
    after = run_identity(api(latest), owner, repository)
    require(after == before, 'owner_attempt_changed')
    return {'owner':owner, 'run':exact, 'source_job_id':sources[0]['id'],
            'skipped_job_ids':sorted(job['id'] for job in jobs if job is not sources[0])}


class UnstartedClaims:
    def __init__(self, store, repository, owner, api):
        self.store, self.repository, self.owner, self.api = store, repository, producer_identity(owner), api
        self.lock = threading.Lock()
        self.owners, self.origins, self.proofs, self.reasons, self.transfers = {}, {}, {}, {}, {}
        self.interrupted = {}
        self.api_reads, self.api_seconds, self.clock = 0, 0, time.monotonic

    def read(self, path):
        # Count API time only: ordinary source/quality audits between staging
        # and commit must not consume this separate recovery inspection budget.
        # The injected GitHub client also bounds each in-flight request/retry.
        if self.api_reads >= MAX_API_READS or self.api_seconds >= MAX_API_SECONDS:
            raise ScanBoundReached('recovery_api_scan_bound_reached')
        self.api_reads += 1
        started = self.clock()
        try:
            return self.api(path)
        finally:
            self.api_seconds += max(0, self.clock()-started)

    def original_source(self, origin):
        identity = digest(stable_bytes(origin))
        if identity not in self.origins:
            require(len(self.origins) < MAX_ORIGIN_LOOKUPS, 'original_source_scan_bound_reached')
            owner = producer_identity(origin['producer'])
            path = f'repos/{self.repository}/actions/runs/{owner["run_id"]}/attempts/{owner["attempt"]}'
            try:
                run = self.read(path)
                jobs = all_jobs(self.read, path, owner)
                admitted = batch_admission(self.store, origin['generation']) if origin.get('source_admission') else None
                verify_origin_run(origin, run, jobs, self.repository, admitted=admitted)
            except ScanBoundReached:
                raise
            except Exception:
                # Preserve the strict default. A canceled original source
                # requires independent admission and explicit unused-run proof.
                try:
                    from portal_extended_interrupted_origin import prove
                    self.interrupted[identity] = prove(self.store, origin, self.repository, self.read)
                except ScanBoundReached:
                    raise
                except Exception:
                    self.origins[identity] = False
                else:
                    self.origins[identity] = True
            else:
                self.origins[identity] = True
        require(self.origins[identity], 'original_source_unproved')

    def eligible(self, locale, generation, row, origin):
        key = (locale, generation)
        with self.lock:
            try:
                owner = producer_identity(row.get('owner'))
                require(owner != self.owner, 'current_owner_still_active')
                require((row['status'] == 'started' and row['continuations'] == 0 and 'snapshot' not in row)
                    or (row['status'] == 'claimed' and 1 <= row['continuations'] <= MAX_CONTINUATIONS),
                    'unused_claim_shape_unproved')
                self.original_source(origin)
                owner_key = digest(stable_bytes(owner))
                if owner_key not in self.owners:
                    require(len(self.owners) < MAX_OWNER_RUNS, 'owner_scan_bound_reached')
                    try:
                        self.owners[owner_key] = unused_owner(self.read, owner, self.repository)
                    except UnprovedClaim as error:
                        self.owners[owner_key] = str(error)
                    except Exception:
                        self.owners[owner_key] = 'owner_api_unavailable'
                proof = self.owners[owner_key]
                require(isinstance(proof, dict), proof if isinstance(proof, str) else 'owner_run_unproved')
                self.proofs[key] = {'before':copy.deepcopy(row), 'origin_sha256':digest(stable_bytes(origin)),
                                    'proof':proof}
                return True
            except UnprovedClaim as error:
                self.reasons[key] = str(error)
                return False

    def stage(self, locale, generation, row):
        key = (locale, generation)
        proof = self.proofs.get(key)
        require(proof is not None and proof['before'] == row, 'unused_claim_changed_after_scan')
        self.transfers[key] = proof

    def commit(self):
        if not self.transfers:
            return 0
        require(current_owner() == self.owner, 'transfer_owner_changed')
        checked = []
        refreshed = {}
        interrupted = {}
        # Verify every selected row and every owner before the first write.
        for (locale, generation), saved in self.transfers.items():
            before = saved['before']
            after = {**before, 'owner':self.owner}
            origin = read_origin(self.store, generation)
            require(origin is not None and digest(stable_bytes(origin)) == saved['origin_sha256'], 'transfer_origin_changed')
            origin_id = saved['origin_sha256']
            if origin_id in self.interrupted and origin_id not in interrupted:
                from portal_extended_interrupted_origin import prove
                proof = prove(self.store, origin, self.repository, self.read)
                require(proof == self.interrupted[origin_id], 'transfer_origin_evidence_changed')
                interrupted[origin_id] = (origin, proof)
            if before['status'] == 'claimed':
                validate_snapshot(self.store, locale, generation, before)
            owner_key = digest(stable_bytes(before['owner']))
            if owner_key not in refreshed:
                refreshed[owner_key] = unused_owner(self.read, before['owner'], self.repository)
            require(refreshed[owner_key] == saved['proof'], 'transfer_owner_evidence_changed')
            receipt = {'schema_version':1, 'policy':POLICY, 'repository':self.repository,
                'locale':locale, 'generation':generation, 'origin_sha256':saved['origin_sha256'],
                'before':before, 'after':after, 'evidence':saved['proof'], 'paid_provider_requests':0}
            if origin_id in interrupted:
                receipt['interrupted_origin_sha256'] = digest(stable_bytes(interrupted[origin_id][1]))
            raw = stable_bytes(receipt)
            require(len(raw) <= MAX_RECEIPT_BYTES, 'transfer_receipt_too_large')
            key = self.store.key('incremental', 'unstarted-claim-transfers', generation, locale, digest(raw)+'.json')
            current = queue(self.store, locale).get(generation)
            require(current in (before, after), 'transfer_current_row_changed')
            if current == after:
                try:
                    previous = self.store._get(key, maximum=MAX_RECEIPT_BYTES)
                except R2NotFound:
                    raise UnprovedClaim('transfer_receipt_missing') from None
                require(previous == raw, 'transfer_receipt_changed')
            checked.append((locale, generation, before, after, key, receipt))
        # The proof depends only on independent capture and the original run,
        # so a replacement failure cannot strand an immutable proof pointer.
        from portal_extended_interrupted_origin import record
        for origin, proof in interrupted.values():
            record(self.store, origin, proof)
        for locale, generation, before, after, key, receipt in checked:
            immutable_record(self.store, key, receipt, kind='unstarted-claim-transfer')
            rows = queue(self.store, locale)
            require(rows.get(generation) in (before, after), 'transfer_current_row_changed')
            if rows[generation] != after:
                rows[generation] = after
                save_queue(self.store, locale, rows)
            require(queue(self.store, locale).get(generation) == after, 'transfer_write_not_persisted')
        return len(checked)


def for_source(store, repository, owner, api):
    try:
        require(current_owner() == producer_identity(owner), 'transfer_owner_changed')
    except UnprovedClaim:
        return None
    return UnstartedClaims(store, repository, owner, api)
