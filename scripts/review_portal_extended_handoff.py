"""Apply delegated daily approval through the existing required-reviewer API.

Opt-in only, on reviewed main, after preparation succeeds. This cannot approve
first-time locales, manual candidates, recovery runs, or arbitrary deployments.
It binds the private producer receipt, active ledger, prepared artifact and
exact-version environment variables before submitting the ordinary review.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

import requests

from offline_translation import MODEL_ID, PROVIDER
from portal_extended_handoff import read_handoff
from portal_extended_locales import (ORIGIN, ExpansionError, daily_corpus_day, digest,
                                     publication_day, select_locales, stable_bytes, validate_corpus)
from portal_extended_publication import checked_batches, read_active_batches
from portal_extended_r2 import DEFAULT_PREFIX, R2Store

ENVIRONMENT = 'portal-extended-locales-production'


def require(condition, message):
    if not condition:
        raise ExpansionError(message)


def api(path, payload=None, method=None):
    require(path.startswith('repos/'), 'Unexpected delegated review API route')
    command = ['gh', 'api', path]
    if method:
        command += ['--method', method]
    if payload is not None:
        command += ['--input', '-']
    result = subprocess.run(command, input=stable_bytes(payload) if payload is not None else None,
                            capture_output=True, check=False)
    if result.returncode:
        # Do not print credentials, signed redirects or arbitrary API bodies.
        status = re.search(r'HTTP \d{3}', result.stderr.decode(errors='replace'))
        raise ExpansionError(f'Delegated review API failed: {path} ({status[0] if status else result.returncode})')
    return json.loads(result.stdout) if result.stdout.strip() else None


def producer_is_valid(receipt, run, jobs, repository, *, origin=None, original_run=None, original_jobs=None):
    producer = receipt['producer']
    if receipt.get('source_origin_sha256'):
        from portal_extended_continuation import verify_origin_run
        require(isinstance(origin, dict) and digest(stable_bytes(origin)) == receipt['source_origin_sha256']
                and origin['generation'] == receipt['batch']['generation']
                and origin['source_day'] == receipt['source_day']
                and set(receipt['batch']['candidates']) <= set(origin['locales']),
                'Historical continuation lacks its exact original source receipt')
        require(isinstance(receipt.get('continuation_checkpoints'), dict)
                and set(receipt['continuation_checkpoints']) == set(receipt['batch']['candidates'])
                and all(re.fullmatch(r'[0-9a-f]{64}', str(value)) for value in receipt['continuation_checkpoints'].values()),
                'Continuation checkpoint inventory is invalid')
        verify_origin_run(origin, original_run or {}, original_jobs or [], repository)
    require(run.get('id') == int(producer['run_id']) and run.get('run_attempt') == int(producer['attempt'])
            and run.get('head_sha') == producer['sha'], 'Producer run identity mismatch')
    require(run.get('status') == 'completed' and run.get('conclusion') in ('success', 'failure')
            and run.get('path') == '.github/workflows/portal-extended-locales-r2.yml'
            and run.get('head_branch') == 'main'
            and run.get('event') in ('workflow_run', 'workflow_dispatch'), 'Producer is not a completed main daily pipeline')
    require(all((run.get(key) or {}).get('full_name') == repository for key in ('repository', 'head_repository')),
            'Producer repository mismatch')
    require((run.get('repository') or {}).get('private') is False, 'Producer must use the public repository')
    for name in ('source', 'publication_handoff'):
        selected = [row for row in jobs if row.get('name') == name]
        require(len(selected) == 1 and selected[0].get('conclusion') == 'success'
                and selected[0].get('status') == 'completed', f'Producer {name} did not complete')
        if name == 'source' and not receipt.get('source_origin_sha256'):
            require(receipt['source_day'] in {publication_day(selected[0].get(key, ''))
                    for key in ('started_at', 'completed_at')}, 'Historical source cannot receive automatic daily approval')


def review_identity(receipt, identity, assembly, active, enabled, expected):
    from restore_assemble_portal_extended_r2 import parse_candidate_specs
    _locales, parsed_ids = parse_candidate_specs(expected['candidate_specs'], expected['locales'])
    require(parsed_ids == expected['candidate_ids'], 'Candidate specs differ from the prepared map')
    batch = checked_batches([receipt['batch']])[0]
    live = {locale for row in checked_batches(active) for locale in row['candidates']}
    allowed = set(select_locales(enabled)) if enabled else set()
    require(set(batch['candidates']) <= live & allowed, 'Automatic review cannot introduce an unapproved locale')
    require(checked_batches(assembly.get('batches')) == checked_batches(active + [batch]),
            'Prepared batch ledger differs from active approvals and exact handoff')
    require(assembly.get('schema_version') == 2 and assembly.get('status') == 'assembled'
            and assembly.get('paid_provider_requests') == 0 and assembly.get('detail_only') is True
            and assembly.get('locale_homepages') is True,
            'Prepared assembly is not complete detail-only offline output with locale homepages')
    actual = {'schema_version': 1, 'operation': 'migrate', 'commit_sha': expected['commit_sha'],
              'static_tree_sha256': expected['static_tree_sha256'], 'source_generation': batch['generation'],
              'pages_per_locale': int(expected['pages_per_locale']),
              'locales': expected['locales'].split(','), 'candidate_ids': expected['candidate_ids'],
              'model': MODEL_ID, 'provider': PROVIDER, 'paid_provider_requests': 0}
    require(identity == actual, 'Prepared artifact does not match exact release outputs')
    require(re.fullmatch(r'[0-9a-f]{40}', actual['commit_sha']) is not None
            and re.fullmatch(r'[0-9a-f]{64}', actual['static_tree_sha256']) is not None,
            'Invalid prepared version identity')
    derived = {}
    for row in checked_batches(active + [batch]):
        derived.update(row['candidates'])
    counts = assembly.get('page_counts', {})
    require(derived == actual['candidate_ids'] and set(counts) == set(derived)
            and assembly.get('locales') == actual['locales']
            and set(actual['locales']) == set(derived), 'Prepared locale inventory differs from approvals')
    require(all(type(count) is int and 0 < count <= 20000 for count in counts.values())
            and sum(counts.values()) <= 20000
            and min(counts.values()) == actual['pages_per_locale'], 'Prepared page counts are invalid')
    return {
        'PORTAL_EXTENDED_APPROVED_COMMIT_SHA': actual['commit_sha'],
        'PORTAL_EXTENDED_APPROVED_STATIC_TREE': actual['static_tree_sha256'],
        'PORTAL_EXTENDED_APPROVED_SOURCE_GENERATION': batch['generation'],
        'PORTAL_EXTENDED_APPROVED_LOCALES': expected['locales'],
        'PORTAL_EXTENDED_APPROVED_CANDIDATE_IDS': expected['candidate_specs'],
        'PORTAL_EXTENDED_APPROVED_PAGES_PER_LOCALE': expected['pages_per_locale'],
        'PORTAL_EXTENDED_LOCALES_ACTIVATION_APPROVED': 'true',
    }


def main():
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch', 'Daily reviewer runs only on main Actions dispatch')
    repository = os.environ['GITHUB_REPOSITORY']
    require(bool(os.environ.get('GH_TOKEN')), 'Existing GH_DISPATCH_TOKEN credential is required for delegated review')
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) is not None, 'Invalid repository')
    run_id = os.environ['GITHUB_RUN_ID']
    require(run_id.isdigit(), 'Invalid release run')
    store = R2Store.from_env(DEFAULT_PREFIX)
    receipt_id = os.environ['EXTENDED_HANDOFF']
    receipt = read_handoff(store, receipt_id)
    producer = receipt['producer']
    require(all(re.fullmatch(r'[1-9][0-9]*', str(producer[key])) for key in ('run_id', 'attempt')),
            'Invalid producer run identity')
    producer_path = f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
    jobs = api(producer_path+'/jobs?per_page=100')
    require(jobs.get('total_count', 101) <= 100, 'Producer jobs exceed verification bound')
    origin = original_run = original_jobs = None
    if receipt.get('source_origin_sha256'):
        from portal_extended_continuation import checkpoint_evidence, read_origin
        origin = read_origin(store, receipt['batch']['generation'])
        require(origin is not None, 'Continuation source origin is missing')
        original = origin['producer']
        original_path = f'repos/{repository}/actions/runs/{original["run_id"]}/attempts/{original["attempt"]}'
        original_response = api(original_path+'/jobs?per_page=100')
        require(original_response.get('total_count', 101) <= 100
                and len(original_response.get('jobs', [])) == original_response['total_count'],
                'Original producer job inventory is incomplete')
        original_jobs, original_run = original_response['jobs'], api(original_path)
    producer_is_valid(receipt, api(producer_path), jobs['jobs'], repository,
                      origin=origin, original_run=original_run, original_jobs=original_jobs)
    for locale, checksum in receipt.get('continuation_checkpoints', {}).items():
        require(bool(checkpoint_evidence(store, locale, receipt['batch']['generation'], checksum)),
                'Continuation checkpoint has no resolved units')
    with tempfile.TemporaryDirectory(prefix='daily-review-') as temporary:
        corpus_path = Path(temporary)/'source.json'
        store.restore_source(receipt['batch']['generation'], corpus_path)
        corpus = json.loads(corpus_path.read_text())
        docs = validate_corpus(corpus)
        require(daily_corpus_day(corpus) == receipt['source_day']
                and len(docs) == receipt['pages_per_locale'] and 1 <= len(docs) <= 24,
                'Handoff source scope or page count differs')
    root = Path('_release_validation')
    previous = json.loads((root/'previous/edge-state.json').read_text())
    with requests.Session() as session:
        response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False)
        require(response.status_code == 200 and len(response.content) <= 65536 and response.json() == previous,
                'Live release changed before delegated review')
    active = read_active_batches(store, previous)
    identity = json.loads((root/'candidate/extended-locale-review-identity.json').read_text())
    assembly = json.loads((root/'candidate/extended-assembly.json').read_text())
    specs = os.environ['CANDIDATE_IDS']
    from restore_assemble_portal_extended_r2 import parse_candidate_specs
    _locales, candidates = parse_candidate_specs(specs, os.environ['CANDIDATE_LOCALES'])
    expected = {'commit_sha': os.environ['GITHUB_SHA'], 'static_tree_sha256': os.environ['CANDIDATE_STATIC_TREE'],
                'pages_per_locale': os.environ['CANDIDATE_PAGES_PER_LOCALE'], 'candidate_ids': candidates,
                'candidate_specs': specs, 'locales': os.environ['CANDIDATE_LOCALES']}
    variables = review_identity(receipt, identity, assembly, active, os.environ['ENABLED_LOCALES'], expected)
    env_path = f'repos/{repository}/environments/{ENVIRONMENT}'
    environment = api(env_path)
    require(environment.get('name') == ENVIRONMENT and any(row.get('type') == 'required_reviewers' and row.get('reviewers')
                for row in environment.get('protection_rules', [])), 'Required reviewers must remain configured')
    pending_path = f'repos/{repository}/actions/runs/{run_id}/pending_deployments'
    pending = []
    for attempt in range(12):
        pending = [row for row in api(pending_path) if row.get('environment', {}).get('id') == environment['id']]
        if pending:
            break
        if attempt < 11:
            time.sleep(5)
    require(len(pending) == 1 and pending[0].get('current_user_can_approve') is True,
            'Configured credential cannot submit this required-reviewer approval')
    existing = api(env_path+'/variables?per_page=100')
    require(existing.get('total_count', 101) <= 100, 'Environment variables exceed bound')
    existing_names = {row['name'] for row in existing['variables']}
    for name, value in variables.items():
        payload = {'name': name, 'value': value}
        api(env_path+'/variables'+('/'+name if name in existing_names else ''), payload,
            'PATCH' if name in existing_names else 'POST')
    saved = {row['name']: row['value'] for row in api(env_path+'/variables?per_page=100')['variables']}
    require(all(saved.get(key) == value for key, value in variables.items()), 'Exact-version variables did not persist')
    record = stable_bytes({'schema_version': 1, 'release_run_id': run_id, 'handoff': receipt_id,
                           'identity': identity, 'decision': 'approved-for-required-reviewer-submission'})
    record_key = store.key('publication-approvals', digest(record), 'receipt.json')
    store._put(record_key, record, metadata={'kind': 'delegated-publication-approval'})
    require(store._get(record_key, maximum=65536) == record, 'Private approval record did not persist')
    result = api(pending_path, {'environment_ids': [environment['id']], 'state': 'approved',
        'comment': f'Operator-delegated daily review: exact private handoff {receipt_id}, prepared tree {identity["static_tree_sha256"]}; existing locale scope, source day, producer, active ledger and full preparation verified. Normal cutover acceptance and rollback remain required.'}, 'POST')
    print(json.dumps({'review_submitted': True, 'deployed': False, 'release_run_id': run_id,
                      'handoff': receipt_id, 'deployment_ids': [row['id'] for row in result]}))


if __name__ == '__main__':
    main()
