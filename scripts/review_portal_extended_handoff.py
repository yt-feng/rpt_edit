"""Apply delegated daily approval through the existing required-reviewer API.

Opt-in only, on reviewed main, after preparation succeeds. This cannot approve
first-time locales, manual candidates, recovery runs, or arbitrary deployments.
It binds the private producer receipt, active ledger, prepared artifact and
exact-version environment variables before submitting the ordinary review.
"""
from __future__ import annotations

import json
from email.utils import parsedate_to_datetime
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
RETRY_DELAYS = (5, 15, 30)


class ReviewAPIError(ExpansionError):
    def __init__(self, status=None, *, transient=False, retry_after=0):
        self.status, self.transient, self.retry_after = status, transient, retry_after
        super().__init__('Delegated review API failed: ' + (f'HTTP {status}' if status else 'transport or response'))


def retry_delay(error, attempt):
    delay = max(RETRY_DELAYS[attempt], error.retry_after)
    require(delay <= 300, 'Delegated review Retry-After exceeds the bounded recovery window')
    return delay


def response_parts(raw):
    headers = {}
    while raw.startswith(b'HTTP/'):
        separator = b'\r\n\r\n' if b'\r\n\r\n' in raw else b'\n\n'
        head, found, body = raw.partition(separator)
        require(bool(found), 'Delegated review response headers are incomplete')
        lines = head.decode(errors='replace').splitlines()
        headers = {key.strip().lower(): value.strip() for line in lines[1:] if ':' in line
                   for key, value in [line.split(':', 1)]}
        headers['status'] = lines[0].split()[1]
        raw = body
    return headers, raw


def api_once(path, payload, method):
    command = ['gh', 'api', path, '--include']
    if method:
        command += ['--method', method]
    if payload is not None:
        command += ['--input', '-']
    try:
        result = subprocess.run(command, input=stable_bytes(payload) if payload is not None else None,
                                capture_output=True, check=False, timeout=60)
    except subprocess.TimeoutExpired:
        raise ReviewAPIError(transient=True) from None
    headers, body = response_parts(result.stdout)
    if result.returncode:
        error = result.stderr.decode(errors='replace')
        match = re.search(r'HTTP (\d{3})', error)
        status = int(headers.get('status') or match[1]) if headers.get('status') or match else None
        # Inspect diagnostic text only to classify it; never emit its contents.
        forbidden = re.search(r'certificate|x509|permission denied|access denied|not logged in|sandbox', error, re.I)
        transient = not forbidden and (status in (408, 429) or status is not None and 500 <= status <= 599
            or status is None and re.search(r'timeout|timed out|error connecting|connection (?:reset|refused|aborted)|\bEOF\b|temporary failure|no such host', error, re.I))
        retry_after = 0
        if headers.get('retry-after'):
            try:
                retry_after = max(0, float(headers['retry-after']))
            except ValueError:
                try:
                    retry_after = max(0, parsedate_to_datetime(headers['retry-after']).timestamp() - time.time())
                except (ValueError, TypeError, OverflowError):
                    raise ReviewAPIError(status) from None
        raise ReviewAPIError(status, transient=bool(transient) and status not in (401, 403), retry_after=retry_after)
    try:
        return json.loads(body) if body.strip() else None
    except (ValueError, UnicodeError):
        # A successful write with an unreadable response may have been applied.
        raise ReviewAPIError(transient=payload is not None or method not in (None, 'GET')) from None


def require(condition, message):
    if not condition:
        raise ExpansionError(message)


def api(path, payload=None, method=None):
    require(path.startswith('repos/'), 'Unexpected delegated review API route')
    read_only = payload is None and method in (None, 'GET')
    for attempt in range(4):
        try:
            return api_once(path, payload, method)
        except ReviewAPIError as error:
            if not read_only or not error.transient or attempt == 3:
                raise
            delay = retry_delay(error, attempt)
            print(f'::notice::Transient delegated review read failure; retrying after {delay:g}s.')
            time.sleep(delay)


def approval_run_identity(run, repository, run_id, attempt, sha):
    require(run.get('id') == int(run_id) and run.get('run_attempt') == int(attempt)
            and run.get('head_sha') == sha and run.get('head_branch') == 'main'
            and run.get('event') == 'workflow_dispatch'
            and run.get('path') == '.github/workflows/neutral-edge-cutover.yml'
            and all((run.get(key) or {}).get('full_name') == repository for key in ('repository', 'head_repository')),
            'Delegated approval release run identity changed')


def check_live_state(previous):
    with requests.Session() as session:
        response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False)
        require(response.status_code == 200 and len(response.content) <= 65536 and response.json() == previous,
                'Live release changed before delegated review')


def accepted_approval_job(api_call, run_path, attempt, sha, approval_job):
    for check in range(4):
        jobs = api_call(run_path + f'/attempts/{attempt}/jobs?per_page=100')
        require(jobs.get('total_count', 101) <= 100, 'Delegated approval jobs exceed verification bound')
        selected = [job for job in jobs.get('jobs', []) if job.get('name') == approval_job]
        require(len(selected) == 1 and selected[0].get('run_id') == int(run_path.rsplit('/', 1)[1])
                and selected[0].get('head_sha') == sha,
                'Accepted review approval job identity differs')
        job = selected[0]
        if job.get('started_at') and (job.get('status') == 'in_progress' or job.get('status') == 'completed'
                                     and job.get('conclusion') in ('success', 'failure', 'timed_out')):
            return
        require(job.get('status') in ('queued', 'waiting', 'pending'),
                'Accepted review has no eligible approval job')
        if check < 3:
            time.sleep(RETRY_DELAYS[check])
    raise ExpansionError('Accepted review lacks an exact-attempt started approval job')


def submit_approval(repository, run_id, environment, variables, comment, *, approval_job,
                    revalidate, api_call=None):
    """Reconcile an ambiguous approval before any bounded resubmission."""
    api_call = api_call or api
    attempt, sha = os.environ['GITHUB_RUN_ATTEMPT'], os.environ['GITHUB_SHA']
    run_path = f'repos/{repository}/actions/runs/{run_id}'
    env_path = f'repos/{repository}/environments/{ENVIRONMENT}'
    pending_path = run_path + '/pending_deployments'
    marker = digest(stable_bytes({'run_id': run_id, 'attempt': attempt, 'sha': sha,
                                 'environment_id': environment['id'], 'variables': variables}))
    comment += f' Review identity: {marker}.'
    payload = {'environment_ids': [environment['id']], 'state': 'approved', 'comment': comment}
    approval_run_identity(api_call(run_path), repository, run_id, attempt, sha)
    baseline_history = api_call(run_path + '/approvals')
    require(isinstance(baseline_history, list), 'Delegated approval history is invalid')
    baseline = [stable_bytes(row) for row in baseline_history]
    for submission in range(4):
        try:
            result = api_call(pending_path, payload, 'POST')
            require(isinstance(result, list) and result, 'Delegated approval response lacks deployment records')
            return result
        except ReviewAPIError as error:
            if not error.transient:
                raise
            # Even after the final POST, reconcile once: a failed response can
            # hide a successful review. Empty pending alone proves nothing.
            print('::notice::Ambiguous delegated review write; verifying existing approval before retry.')
            if submission < 3:
                time.sleep(retry_delay(error, submission))
            approval_run_identity(api_call(run_path), repository, run_id, attempt, sha)
            current = api_call(env_path)
            keys = ('id', 'name', 'protection_rules', 'deployment_branch_policy')
            require(all(current.get(key) == environment.get(key) for key in keys),
                    'Delegated approval environment identity changed')
            saved = api_call(env_path + '/variables?per_page=100')
            require(saved.get('total_count', 101) <= 100
                    and all({row['name']: row['value'] for row in saved['variables']}.get(key) == value
                            for key, value in variables.items()), 'Delegated approval version identity changed')
            pending = api_call(pending_path)
            require(isinstance(pending, list), 'Delegated approval pending state is invalid')
            pending = [row for row in pending if row.get('environment', {}).get('id') == environment['id']]
            history = api_call(run_path + '/approvals')
            require(isinstance(history, list), 'Delegated approval history is invalid')
            approved = [row for row in history if stable_bytes(row) not in baseline
                        and row.get('state') == 'approved' and row.get('comment') == comment
                        and any(env.get('id') == environment['id'] and env.get('name') == ENVIRONMENT
                                for env in row.get('environments', []))]
            if approved:
                require(not pending, 'Delegated approval acceptance conflicts with pending state')
                accepted_approval_job(api_call, run_path, attempt, sha, approval_job)
                approval_run_identity(api_call(run_path), repository, run_id, attempt, sha)
                print('::notice::Ambiguous review response reconciled as accepted; deployment is not verified.')
                return []
            require(len(pending) == 1 and pending[0].get('current_user_can_approve') is True,
                    'Ambiguous delegated approval remains unverified; no second submission')
            require(submission < 3, 'Delegated approval transient retry budget exhausted')
            revalidate()


def admission_is_valid(admitted, run, jobs, repository):
    """Verify the original fast capture, not the day a slow consumer starts."""
    from portal_extended_daily_queue import checked_producer
    producer = checked_producer(admitted['producer'])
    require(producer['repository'] == repository and run.get('id') == int(producer['run_id'])
            and run.get('run_attempt') == int(producer['attempt']) and run.get('head_sha') == producer['sha'],
            'Source-admission run identity mismatch')
    require(run.get('status') == 'completed' and run.get('conclusion') == 'success'
            and run.get('head_branch') == 'main' and run.get('path') == producer['workflow']
            and run.get('event') in ('workflow_run', 'workflow_dispatch'),
            'Source admission is not a completed reviewed-main capture')
    require(all((run.get(key) or {}).get('full_name') == repository for key in ('repository', 'head_repository'))
            and (run.get('repository') or {}).get('private') is False, 'Source-admission repository differs')
    selected = [job for job in jobs if job.get('name') == 'source_snapshot']
    require(len(selected) == 1 and selected[0].get('status') == 'completed' and selected[0].get('conclusion') == 'success',
            'Source-day capture did not complete')
    capture_day = admitted['day']
    if admitted.get('schema_version') == 2:
        from portal_extended_source_refresh import POLICY as REFRESH_POLICY
        require(admitted.get('policy') == REFRESH_POLICY
                and re.fullmatch(r'[a-f0-9]{64}', admitted.get('refresh', '')) is not None
                and publication_day(admitted.get('capture_day', '')) == admitted.get('capture_day')
                and admitted['day'] <= admitted['capture_day'], 'Source refresh proof identity differs')
        # read_admission already verifies the private immutable live inventory,
        # latest source day, captured release and exact corpus; the GitHub job
        # must still match its real capture day, repository, attempt and SHA.
        capture_day = admitted['capture_day']
    elif admitted.get('schema_version') == 3:
        from portal_extended_recovered_admission import POLICY as RECOVERED_POLICY
        require(admitted.get('policy') == RECOVERED_POLICY
                and re.fullmatch(r'[a-f0-9]{64}', admitted.get('recovery', '')) is not None
                and publication_day(admitted.get('capture_day', '')) == admitted.get('capture_day')
                and admitted['day'] <= admitted['capture_day'], 'Recovered publication proof identity differs')
        # read_admission validates the immutable exact publication request,
        # successful acceptance, stable public source bytes and corpus binding.
        capture_day = admitted['capture_day']
    require(capture_day in {publication_day(selected[0].get(key, '')) for key in ('started_at', 'completed_at')},
            'Admission cannot discover historical source pages')
    return admitted


def producer_is_valid(receipt, run, jobs, repository, admitted=None, *, origin=None, original_run=None, original_jobs=None):
    producer = receipt['producer']
    if receipt.get('source_origin_sha256'):
        from portal_extended_continuation import origin_allows_locale, verify_origin_run
        require(isinstance(origin, dict) and digest(stable_bytes(origin)) == receipt['source_origin_sha256']
                and origin['generation'] == receipt['batch']['generation']
                and origin['source_day'] == receipt['source_day']
                and all(origin_allows_locale(origin, locale) for locale in receipt['batch']['candidates']),
                'Historical continuation lacks its exact original source receipt')
        require(isinstance(receipt.get('continuation_checkpoints'), dict)
                and set(receipt['continuation_checkpoints']) == set(receipt['batch']['candidates'])
                and all(re.fullmatch(r'[0-9a-f]{64}', str(value)) for value in receipt['continuation_checkpoints'].values()),
                'Continuation checkpoint inventory is invalid')
        verify_origin_run(origin, original_run or {}, original_jobs or [], repository, admitted=admitted)
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
            source_days = {publication_day(selected[0].get(key, '')) for key in ('started_at', 'completed_at')}
            frozen = (admitted is not None and admitted['day'] == receipt['source_day']
                      and admitted['admission'] == receipt.get('source_admission'))
            require(receipt['source_day'] in source_days or frozen,
                    'Historical source cannot receive automatic daily approval')


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
    admitted = None
    if receipt.get('source_admission'):
        from portal_extended_daily_queue import batch_admission
        admitted = batch_admission(store, receipt['batch']['generation'])
        require(admitted is not None and admitted['admission'] == receipt['source_admission'],
                'Handoff admission differs from its checksum-verified inventory')
        capture = admitted['producer']
        capture_path = f'repos/{repository}/actions/runs/{capture["run_id"]}/attempts/{capture["attempt"]}'
        capture_jobs = api(capture_path + '/jobs?per_page=100')
        require(capture_jobs.get('total_count', 101) <= 100, 'Source capture jobs exceed verification bound')
        admission_is_valid(admitted, api(capture_path), capture_jobs['jobs'], repository)
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
    producer_is_valid(receipt, api(producer_path), jobs['jobs'], repository, admitted,
                      origin=origin, original_run=original_run, original_jobs=original_jobs)
    from portal_extended_handoff import source_repair_proofs, source_repair_completions
    from portal_extended_french_repair import verify_repair_producer
    repairs = source_repair_proofs(store, receipt)
    completions = source_repair_completions(store, receipt, repairs)
    for locale, proof in repairs.items():
        completion = completions.get(locale)
        repaired_by = (completion or proof)['producer']
        repair_path = f'repos/{repository}/actions/runs/{repaired_by["run_id"]}/attempts/{repaired_by["attempt"]}'
        response = api(repair_path+'/jobs?per_page=100')
        require(type(response.get('total_count')) is int and 0 < response['total_count'] <= 100
                and len(response.get('jobs', [])) == response['total_count'],
                'French repair producer job inventory is incomplete')
        verify_repair_producer(proof, api(repair_path), response['jobs'], repository, completion=completion)
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
    check_live_state(previous)
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
    result = submit_approval(repository, run_id, environment, variables,
        f'Operator-delegated daily review: exact private handoff {receipt_id}, prepared tree {identity["static_tree_sha256"]}; existing locale scope, source day, producer, active ledger and full preparation verified. Normal cutover acceptance and rollback remain required.',
        approval_job='extended_locales_approval', revalidate=lambda: check_live_state(previous), api_call=api)
    print(json.dumps({'review_submitted': True, 'deployed': False, 'release_run_id': run_id,
                      'handoff': receipt_id, 'deployment_ids': [row['id'] for row in result]}))


if __name__ == '__main__':
    main()
