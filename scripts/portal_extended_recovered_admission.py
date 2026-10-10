"""Admit only an exact, already accepted recovered Blog publication cohort.

This is an append-only source route, not historical discovery. Public receipts
bind the producer and live bodies; sources/proofs remain in private R2. The
ordinary latest-day queue and its replacement policy are never written here.
"""
from __future__ import annotations

import io
import json
import re
import subprocess
import threading
import zipfile

from collect_portal_extended_sources import read_public
from portal_extended_locales import (DAILY_SCOPE, INCREMENTAL_START, ORIGIN,
    ExpansionError, daily_corpus_day, daily_document, digest, document_from_html,
    make_corpus, publication_day, stable_bytes)
from portal_extended_r2 import HEX64, MAX_SOURCE_BYTES, R2NotFound
from portal_extended_source_refresh import checked_release, read_release
from watch_recovered_article_publication import (body_identity, eligible,
    validate_request)

POLICY = 'accepted-recovered-blog-cohort-v1'
WORKFLOW = '.github/workflows/recover-report-article-delivery.yml'
MAX_COHORTS = 32
MAX_ARTIFACT_BYTES = 1024 * 1024
MAX_API_BYTES = 4 * 1024 * 1024


def require(condition, code):
    if not condition:
        raise ExpansionError(code)


def request_hash(request):
    # Match the existing public watcher exactly (including its JSON spacing).
    return digest(json.dumps(request, sort_keys=True).encode())


class GitHub:
    def __init__(self, repository):
        require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'recovered_repository_invalid')
        self.repository = repository

    def raw(self, suffix, maximum=MAX_API_BYTES):
        """Bound bytes/time, never expose gh stderr or a signed download URL."""
        process = None
        timer = None
        try:
            process = subprocess.Popen(['gh', 'api', f'repos/{self.repository}/{suffix}'],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            timer = threading.Timer(60, process.kill)
            timer.daemon = True
            timer.start()
            raw = process.stdout.read(maximum + 1)
            if len(raw) > maximum:
                process.kill()
                raise ExpansionError('recovered_github_response_oversized')
            require(process.wait(timeout=2) == 0, 'recovered_github_read_failed')
            return raw
        except (OSError, subprocess.TimeoutExpired):
            raise ExpansionError('recovered_github_read_failed') from None
        finally:
            if timer is not None:
                timer.cancel()
            if process is not None:
                if process.poll() is None:
                    process.kill()
                process.wait()
                process.stdout.close()

    def api(self, suffix):
        try:
            return json.loads(self.raw(suffix))
        except (ValueError, UnicodeError):
            raise ExpansionError('recovered_github_json_invalid') from None

    def artifact(self, artifact_id, member):
        return artifact_json(self.raw(f'actions/artifacts/{artifact_id}/zip', MAX_ARTIFACT_BYTES), member)

    def contains(self, base, head):
        if base == head:
            return True
        value = self.api(f'compare/{base}...{head}')
        return value.get('status') in {'identical', 'ahead'} and value.get('merge_base_commit', {}).get('sha') == base


def artifact_json(raw, member):
    require(len(raw) <= MAX_ARTIFACT_BYTES, 'recovered_artifact_oversized')
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            names = archive.infolist()
            require(len(names) == 1 and names[0].filename == member and not names[0].is_dir()
                    and names[0].file_size <= MAX_ARTIFACT_BYTES
                    and not (names[0].flag_bits & 1), 'recovered_artifact_members_invalid')
            raw = archive.read(names[0])
        require(len(raw) <= MAX_ARTIFACT_BYTES, 'recovered_artifact_oversized')
        value = json.loads(raw)
        require(isinstance(value, dict), 'recovered_artifact_json_invalid')
        return value
    except (ValueError, UnicodeError, zipfile.BadZipFile, RuntimeError, OSError):
        raise ExpansionError('recovered_artifact_json_invalid') from None


def checked_publication(value):
    require(isinstance(value, dict) and set(value) == {'repository', 'run_id', 'attempt', 'sha',
        'release_run_id', 'release_attempt', 'release_sha', 'request', 'state'}, 'recovered_publication_fields_invalid')
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', value['repository'])
        and all(re.fullmatch(r'[1-9][0-9]*', str(value[key])) for key in
                ('run_id', 'attempt', 'release_run_id', 'release_attempt'))
        and all(re.fullmatch(r'[a-f0-9]{40}', value[key]) for key in ('sha', 'release_sha')),
        'recovered_publication_identity_invalid')
    request, state = value['request'], value['state']
    checked_request(request)
    require(bool(request['records']), 'recovered_publication_request_empty')
    require(isinstance(state, dict) and set(state) <= {'schema_version', 'request_sha256', 'status',
        'run_ids', 'release_run_id', 'article_count', 'conclusion'}
        and state.get('schema_version') == 1 and state.get('status') == 'complete'
        and state.get('request_sha256') == request_hash(request)
        and type(state.get('article_count')) is int and state['article_count'] == len(request['records'])
        and state.get('release_run_id') == int(value['release_run_id'])
        and isinstance(state.get('run_ids'), list) and 1 <= len(state['run_ids']) <= 100
        and all(type(run) is int and run > 0 for run in state['run_ids'])
        and len(set(state['run_ids'])) == len(state['run_ids'])
        and state['run_ids'][-1] == state['release_run_id'], 'recovered_publication_not_accepted')
    return value


def checked_request(request):
    try:
        validate_request(request)
    except (ValueError, TypeError, KeyError):
        raise ExpansionError('recovered_publication_request_invalid') from None
    require(set(request) == {'schema_version', 'archive_commit', 'origin', 'records'}
        and request['origin'] == ORIGIN and len(request['records']) <= 500
        and all(set(row) == {'fingerprint', 'slug', 'body_sha256', 'title_sha256'} for row in request['records']),
        'recovered_publication_request_invalid')
    return request


def authenticate(github, run_id):
    require(re.fullmatch(r'[1-9][0-9]*', str(run_id)), 'recovered_run_invalid')
    run = github.api(f'actions/runs/{run_id}')
    require(run.get('id') == int(run_id) and type(run.get('run_attempt')) is int and 1 <= run['run_attempt'] <= 10
        and run.get('path') == WORKFLOW and run.get('head_branch') == 'main'
        and run.get('event') == 'workflow_dispatch' and run.get('status') == 'completed'
        and run.get('conclusion') == 'success' and re.fullmatch(r'[a-f0-9]{40}', str(run.get('head_sha', '')))
        and all((run.get(key) or {}).get('full_name') == github.repository for key in ('repository', 'head_repository'))
        and (run.get('repository') or {}).get('private') is False, 'recovered_run_not_verified')
    attempt = run['run_attempt']
    latest_jobs = {}
    for number in range(1, attempt + 1):
        jobs = github.api(f'actions/runs/{run_id}/attempts/{number}/jobs?per_page=100')
        rows = jobs.get('jobs', [])
        require(type(jobs.get('total_count')) is int and jobs['total_count'] == len(rows) <= 100,
                'recovered_jobs_incomplete')
        for name in ('generate', 'deliver', 'publish'):
            selected = [row for row in rows if row.get('name') == name]
            require(len(selected) <= 1, 'recovered_jobs_ambiguous')
            if selected:
                latest_jobs[name] = selected[0]
    # A publish-only rerun must not force new generation or new WeChat POSTs.
    # Authenticate each stage's latest actual execution across exact attempts.
    for name in ('generate', 'deliver', 'publish'):
        selected = latest_jobs.get(name, {})
        require(selected.get('status') == 'completed' and selected.get('conclusion') == 'success'
            and selected.get('run_id') == int(run_id) and selected.get('head_sha') == run['head_sha'],
            'recovered_job_not_verified')
    artifacts = github.api(f'actions/runs/{run_id}/artifacts?per_page=100')
    rows = artifacts.get('artifacts', [])
    require(type(artifacts.get('total_count')) is int and artifacts['total_count'] == len(rows) <= 100,
            'recovered_artifacts_incomplete')
    values = {}
    for kind, member in (('request', 'recovered-publication-request.json'), ('state', 'publication-state.json')):
        selected = [row for row in rows if row.get('name') == f'recovered-publication-{kind}-{run_id}']
        require(len(selected) == 1 and selected[0].get('expired') is False
            and type(selected[0].get('id')) is int and selected[0]['id'] > 0
            and type(selected[0].get('size_in_bytes')) is int
            and 0 < selected[0]['size_in_bytes'] <= MAX_ARTIFACT_BYTES,
            'recovered_artifact_not_verified')
        values[kind] = github.artifact(selected[0]['id'], member)
    request, state = values['request'], values['state']
    checked_request(request)
    require(isinstance(state, dict) and state.get('schema_version') == 1 and state.get('status') == 'complete'
            and type(state.get('article_count')) is int and state['article_count'] == len(request['records'])
            and state.get('request_sha256') == request_hash(request), 'recovered_publication_not_accepted')
    # A cohort with no published articles creates no translation work.
    if request.get('records') == []:
        require(request.get('origin') == ORIGIN and state.get('status') == 'complete'
                and state.get('article_count') == 0 and state.get('request_sha256') == request_hash(request),
                'recovered_empty_publication_invalid')
        return None
    release_id = state.get('release_run_id')
    require(type(release_id) is int and release_id > 0, 'recovered_release_missing')
    release = github.api(f'actions/runs/{release_id}')
    require(release.get('id') == release_id and release.get('status') == 'completed'
        and release.get('conclusion') == 'success' and type(release.get('run_attempt')) is int
        and release['run_attempt'] > 0
        and eligible(release, github.repository, request.get('archive_commit', ''), github.contains),
        'recovered_release_not_verified')
    value = {'repository': github.repository, 'run_id': str(run_id), 'attempt': str(attempt), 'sha': run['head_sha'],
        'release_run_id': str(release_id), 'release_attempt': str(release['run_attempt']),
        'release_sha': release['head_sha'], 'request': request, 'state': state}
    return checked_publication(value)


def collect(session, publication, capture_day):
    checked_publication(publication)
    require(publication_day(capture_day) == capture_day, 'recovered_capture_day_invalid')
    request = publication['request']
    # publication_day accepts ISO dates, not compact slugs.
    days = {publication_day(row['slug'][:4]+'-'+row['slug'][4:6]+'-'+row['slug'][6:8]) for row in request['records']}
    require(len(days) == 1, 'recovered_cohort_mixed_dates')
    day = days.pop()
    require(INCREMENTAL_START <= day <= capture_day, 'recovered_cohort_day_invalid')
    before = read_release(session)
    docs = []
    source_bytes = 0
    for row in request['records']:
        url = ORIGIN + '/blog/' + row['slug'] + '.html'
        raw = read_public(session, url)
        try:
            body, canonicals = body_identity(raw.decode('utf-8'), row['title_sha256'])
        except (ValueError, UnicodeError):
            raise ExpansionError('recovered_live_body_invalid') from None
        require(body == row['body_sha256'] and canonicals == [url], 'recovered_live_body_changed')
        doc = document_from_html(url, raw, exclude_related=True)
        require(daily_document(doc, day), 'recovered_live_date_changed')
        source_bytes += len(stable_bytes(doc))
        require(source_bytes <= MAX_SOURCE_BYTES, 'recovered_corpus_oversized')
        docs.append(doc)
    require(read_release(session) == before, 'recovered_live_release_changed')
    urls = {doc['url'] for doc in docs}
    for doc in docs:
        doc['links'] = [row for row in doc['links'] if row['url'] in urls]
        doc.update(selection_scope=DAILY_SCOPE, selection_day=day)
        doc['content_sha256'] = digest(stable_bytes({k: v for k, v in doc.items() if k != 'content_sha256'}))
    corpus = make_corpus(sorted(docs, key=lambda doc: doc['url']))
    proof = {'schema_version': 1, 'policy': POLICY, 'capture_day': capture_day, 'day': day,
        'release': before, 'publication': publication, 'generation': corpus['documents_sha256'],
        'sources': {doc['url']: {'html_sha256': doc['source_html_sha256'], 'document_sha256': doc['content_sha256']}
                    for doc in corpus['documents']}}
    return corpus, validate_proof(proof, corpus)


def validate_proof(value, corpus):
    require(isinstance(value, dict) and set(value) == {'schema_version', 'policy', 'capture_day', 'day',
        'release', 'publication', 'generation', 'sources'} and value['schema_version'] == 1
        and value['policy'] == POLICY, 'recovered_source_proof_invalid')
    checked_release(value['release'])
    checked_publication(value['publication'])
    require(value['generation'] == corpus['documents_sha256'] and daily_corpus_day(corpus) == value['day']
        and publication_day(value['capture_day']) == value['capture_day']
        and INCREMENTAL_START <= value['day'] <= value['capture_day'], 'recovered_source_proof_identity_changed')
    expected = {ORIGIN+'/blog/'+row['slug']+'.html' for row in value['publication']['request']['records']}
    require(expected == {doc['url'] for doc in corpus['documents']} == set(value['sources']),
            'recovered_source_inventory_changed')
    for doc in corpus['documents']:
        row = value['sources'][doc['url']]
        require(isinstance(row, dict) and set(row) == {'html_sha256', 'document_sha256'}
            and row['html_sha256'] == doc['source_html_sha256'] and HEX64.fullmatch(row['html_sha256'])
            and row['document_sha256'] == doc['content_sha256'], 'recovered_source_bytes_changed')
    return value


def read_proof(store, identity, corpus):
    require(isinstance(identity, str) and HEX64.fullmatch(identity), 'recovered_proof_identity_invalid')
    raw = store._get(store.key('recovered-publications', identity, 'proof.json'), maximum=MAX_SOURCE_BYTES)
    require(digest(raw) == identity, 'recovered_proof_checksum_changed')
    return validate_proof(json.loads(raw), corpus)


def read_queue(store):
    try:
        value = json.loads(store._get(store.key('incremental', 'recovered-source-cohorts', 'queue.json'), maximum=65536))
    except R2NotFound:
        return []
    require(isinstance(value, dict) and set(value) == {'schema_version', 'policy', 'entries'}
        and value['schema_version'] == 1 and value['policy'] == POLICY
        and isinstance(value['entries'], list) and len(value['entries']) <= MAX_COHORTS,
        'recovered_queue_invalid')
    from portal_extended_daily_queue import checked_entry
    rows = [checked_entry(row) for row in value['entries']]
    require(len({row['admission'] for row in rows}) == len(rows), 'recovered_queue_duplicate')
    return rows


def admit(store, corpus, proof, producer):
    from portal_extended_daily_queue import (checked_producer, immutable_record, inventory,
        pending_docs, read_admission, read_corpus, write_verified)
    from portal_extended_locales import ADDITIONAL
    checked_producer(producer)
    validate_proof(proof, corpus)
    request_id = request_hash(proof['publication']['request'])
    claim_key = store.key('recovered-publication-claims', request_id, 'receipt.json')
    try:
        prior = json.loads(store._get(claim_key, maximum=65536))
    except R2NotFound:
        prior = None
    if prior is not None:
        require(set(prior) == {'request_sha256', 'admission'} and prior['request_sha256'] == request_id,
                'recovered_claim_invalid')
        receipt = read_admission(store, prior['admission'])
        old = read_proof(store, receipt['recovery'], read_corpus(store, receipt['generation']))
        require(request_hash(old['publication']['request']) == request_id, 'recovered_claim_changed')
        return {'admitted': False, 'reused': True, 'admission': prior['admission'], 'day': receipt['day'],
                'pages': receipt['pages'], 'generation': receipt['generation'], 'paid_provider_requests': 0}
    queued = read_queue(store)
    # The queue write precedes the final immutable claim. Recover an interrupted
    # last write without appending the same exact publication a second time.
    for entry in queued:
        previous_receipt, previous = inventory(store, entry)
        previous_proof = read_proof(store, previous_receipt['recovery'], previous)
        if request_hash(previous_proof['publication']['request']) == request_id:
            immutable_record(store, claim_key, {'request_sha256': request_id, 'admission': entry['admission']},
                             kind='recovered-source-claim')
            return {'admitted': False, 'reused': True, 'admission': entry['admission'], 'day': entry['day'],
                'pages': previous_receipt['pages'], 'generation': previous_receipt['generation'], 'paid_provider_requests': 0}
    retained = []
    for entry in queued:
        _, previous = inventory(store, entry)
        if any(pending_docs(store, previous['documents'], locale, entry['day']) for locale in ADDITIONAL):
            retained.append(entry)
    require(len(retained) < MAX_COHORTS, 'recovered_queue_full')
    raw = stable_bytes(proof)
    require(len(raw) <= MAX_SOURCE_BYTES, 'recovered_proof_oversized')
    identity = digest(raw)
    key = store.key('recovered-publications', identity, 'proof.json')
    try:
        old = store._get(key, maximum=MAX_SOURCE_BYTES)
    except R2NotFound:
        old = None
    require(old in (None, raw), 'recovered_immutable_proof_changed')
    store.put_source(corpus)
    if old is None:
        store._put(key, raw, metadata={'kind': 'recovered-source-proof'})
    require(store._get(key, maximum=MAX_SOURCE_BYTES) == raw, 'recovered_proof_readback_changed')
    receipt = {'schema_version': 3, 'policy': POLICY, 'scope': DAILY_SCOPE, 'day': proof['day'],
        'capture_day': proof['capture_day'], 'generation': corpus['documents_sha256'],
        'pages': len(corpus['documents']), 'producer': producer, 'recovery': identity}
    admission = digest(stable_bytes(receipt))
    immutable_record(store, store.key('source-admissions', admission, 'receipt.json'), receipt, kind='source-admission')
    retained.append({'day': proof['day'], 'admission': admission})
    write_verified(store, store.key('incremental', 'recovered-source-cohorts', 'queue.json'),
        {'schema_version': 1, 'policy': POLICY, 'entries': retained}, kind='recovered-source-queue')
    immutable_record(store, claim_key, {'request_sha256': request_id, 'admission': admission}, kind='recovered-source-claim')
    return {'admitted': True, 'reused': False, 'admission': admission, 'day': proof['day'],
        'pages': len(corpus['documents']), 'generation': corpus['documents_sha256'], 'paid_provider_requests': 0}
