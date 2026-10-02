"""Exact English approval via the existing configured required-reviewer API.

No environment protection is removed or skipped. This opt-in reviewer checks
real main/public capture and CPU job evidence, candidate objects, the pinned
previous state and the exact uploaded static tree before normal approval.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
import tempfile
import time

import requests
from portal_english_commentary import PREFIX, POLICY, require, exact
from portal_english_handoff import verify_handoff
from portal_english_publication import checked_assembly, read_active, verify_prepared_ledger, RELEASE
from portal_english_pipeline import hash_value, put_verified
from portal_extended_locales import ORIGIN, digest, stable_bytes
from portal_extended_r2 import DEFAULT_PREFIX, R2Store
from review_portal_extended_handoff import ENVIRONMENT, api, admission_is_valid


def producer_is_valid(receipt, run, jobs, repository):
    producer = receipt['producer']
    require(producer['repository'] == repository and run.get('id') == int(producer['run_id'])
            and run.get('run_attempt') == int(producer['attempt']) and run.get('head_sha') == producer['sha']
            and run.get('path') == producer['workflow'], 'English CPU producer identity differs')
    require(run.get('head_branch') == 'main' and run.get('status') == 'completed'
            and run.get('conclusion') in {'success', 'failure'} and run.get('event') in {'workflow_run', 'workflow_dispatch'}
            and (run.get('repository') or {}).get('private') is False
            and all((run.get(key) or {}).get('full_name') == repository for key in ('repository', 'head_repository')),
            'English CPU is not completed reviewed main/public Actions')
    for name in ('source', 'locale (en)'):
        selected = [job for job in jobs if job.get('name') == name]
        require(len(selected) == 1 and selected[0].get('status') == 'completed' and selected[0].get('conclusion') == 'success',
                'English source/CPU candidate job did not complete')


def review_identity(identity, assembly, previous, handoff, *, commit, tree, release):
    exact(identity, ['schema_version', 'policy', 'operation', 'commit_sha', 'static_tree_sha256',
                     'site_release', 'ledger_sha256', 'page_count', 'handoff'])
    checked_assembly(assembly); hash_value(tree); hash_value(identity['ledger_sha256']); hash_value(identity['handoff'])
    require(re.fullmatch(r'[0-9a-f]{40}', commit) and RELEASE.fullmatch(release))
    require(identity == {'schema_version': 1, 'policy': POLICY, 'operation': 'migrate', 'commit_sha': commit,
                         'static_tree_sha256': tree, 'site_release': release, 'ledger_sha256': assembly['ledger_sha256'],
                         'page_count': assembly['page_count'], 'handoff': identity['handoff']},
            'English prepared identity differs from exact release outputs')
    expected_batches = list(previous['batches']) if previous else []
    if handoff['batch'] not in expected_batches: expected_batches.append(handoff['batch'])
    require(assembly['batches'] == expected_batches and assembly['page_count'] >= handoff['page_count'],
            'English approved batch carry-forward differs from exact handoff')
    return {'PORTAL_ENGLISH_APPROVED_COMMIT_SHA': commit, 'PORTAL_ENGLISH_APPROVED_STATIC_TREE': tree,
            'PORTAL_ENGLISH_APPROVED_SITE_RELEASE': release, 'PORTAL_ENGLISH_APPROVED_LEDGER': assembly['ledger_sha256'],
            'PORTAL_ENGLISH_APPROVED_HANDOFF': identity['handoff'], 'PORTAL_ENGLISH_COMMENTARY_ACTIVATION_APPROVED': 'true'}


def approval_is_valid(identity, expected, variables):
    exact(identity, ['schema_version', 'policy', 'operation', 'commit_sha', 'static_tree_sha256',
                     'site_release', 'ledger_sha256', 'page_count', 'handoff'])
    require(identity['schema_version'] == 1 and identity['policy'] == POLICY and identity['operation'] == 'migrate'
            and isinstance(identity['commit_sha'], str) and re.fullmatch(r'[0-9a-f]{40}', identity['commit_sha'])
            and isinstance(identity['site_release'], str) and RELEASE.fullmatch(identity['site_release'])
            and type(identity['page_count']) is int and 1 <= identity['page_count'] <= 5000,
            'English approval identity schema differs')
    for field in ('static_tree_sha256', 'ledger_sha256', 'handoff'): hash_value(identity[field])
    require(identity == expected, 'English approval artifact differs from the prepared identity')
    require(variables.get('PORTAL_ENGLISH_COMMENTARY_ACTIVATION_APPROVED') == 'true', 'English exact-version approval flag is not true')
    for key, field in {'COMMIT_SHA': 'commit_sha', 'STATIC_TREE': 'static_tree_sha256', 'SITE_RELEASE': 'site_release',
                       'LEDGER': 'ledger_sha256', 'HANDOFF': 'handoff'}.items():
        require(variables.get('PORTAL_ENGLISH_APPROVED_'+key) == identity[field], 'English exact-version approval identity differs')


def main():
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and os.environ.get('KC_ENGLISH_AUTO_REVIEW') == 'true', 'English delegated review requires opted-in reviewed main dispatch')
    repository = os.environ['GITHUB_REPOSITORY']; run_id = os.environ['GITHUB_RUN_ID']
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) and run_id.isdigit()
            and bool(os.environ.get('GH_TOKEN')), 'Configured English reviewer identity is unavailable')
    store = R2Store.from_env(PREFIX); original = R2Store(store.client, store.bucket, DEFAULT_PREFIX)
    handoff_id = os.environ['ENGLISH_HANDOFF']
    with tempfile.TemporaryDirectory(prefix='english-exact-review-') as temporary:
        receipt, admission = verify_handoff(store, original, handoff_id, Path(temporary)/'candidate')
    for producer, verifier, value in [(admission['producer'], admission_is_valid, admission),
                                      (receipt['producer'], producer_is_valid, receipt)]:
        path = f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
        jobs = api(path+'/jobs?per_page=100'); require(jobs.get('total_count', 101) <= 100, 'English producer jobs exceed bound')
        verifier(value, api(path), jobs['jobs'], repository)
    root = Path('_release_validation')
    previous_identity = json.loads((root/'previous/edge-state.json').read_bytes())
    with requests.Session() as session:
        response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False)
        require(response.status_code == 200 and len(response.content) <= 65536 and response.json() == previous_identity,
                'Live version changed before English delegated review')
    active = read_active(store, previous_identity)
    identity = json.loads((root/'candidate/english-review-identity.json').read_bytes())
    require(identity['handoff'] == handoff_id)
    candidate_identity = {'slot': os.environ['CANDIDATE_SLOT'], 'release_id': os.environ['CANDIDATE_RELEASE'],
                          'tree_sha256': os.environ['CANDIDATE_STATIC_TREE']}
    with tempfile.TemporaryDirectory(prefix='english-prepared-review-') as temporary:
        assembly = verify_prepared_ledger(store, original, candidate_identity, Path(temporary))
    variables = review_identity(identity, assembly, active, receipt, commit=os.environ['GITHUB_SHA'],
                                tree=candidate_identity['tree_sha256'], release=candidate_identity['release_id'])
    environment_path = f'repos/{repository}/environments/{ENVIRONMENT}'
    environment = api(environment_path)
    require(environment.get('name') == ENVIRONMENT and any(row.get('type') == 'required_reviewers' and row.get('reviewers')
            for row in environment.get('protection_rules', [])), 'English required reviewers must stay configured')
    pending_path = f'repos/{repository}/actions/runs/{run_id}/pending_deployments'
    pending = []
    for attempt in range(12):
        pending = [row for row in api(pending_path) if row.get('environment', {}).get('id') == environment['id']]
        if pending: break
        if attempt < 11: time.sleep(5)
    require(len(pending) == 1 and pending[0].get('current_user_can_approve') is True,
            'Configured English reviewer cannot submit the required approval')
    existing = api(environment_path+'/variables?per_page=100')
    require(existing.get('total_count', 101) <= 100, 'English environment variables exceed bound')
    names = {row['name'] for row in existing['variables']}
    for name, value in variables.items():
        api(environment_path+'/variables'+('/'+name if name in names else ''), {'name': name, 'value': value},
            'PATCH' if name in names else 'POST')
    saved = {row['name']: row['value'] for row in api(environment_path+'/variables?per_page=100')['variables']}
    approval_is_valid(identity, identity, saved)
    record = {'schema_version': 1, 'policy': POLICY, 'release_run_id': run_id, 'identity': identity,
              'decision': 'approved-for-required-reviewer-submission'}
    put_verified(store, store.key('publication-approvals', digest(stable_bytes(record)), 'receipt.json'), record,
                 'english-exact-publication-approval', immutable=True)
    api(pending_path, {'environment_ids': [environment['id']], 'state': 'approved',
                      'comment': 'Operator-delegated English secondary-commentary review; exact source, CPU, preview-only static tree, private ledger, active baseline and versioned rollback verified. Normal cutover gates remain required.'}, 'POST')
    print(json.dumps({'review_submitted': True, 'release_run_id': run_id, 'deployed': False}))


if __name__ == '__main__': main()
