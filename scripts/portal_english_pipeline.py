"""Private English daily cursor/candidate pipeline; no independent publication.

The English job joins the existing two-runner translation matrix. Every source
is a same-fetch KC-comment projection admitted by the reviewed capture workflow.
Ready receipts mean translation/storage completion, never publication approval.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import tempfile

from build_portal_extended_locales import (MAX_CHECKPOINT_BYTES, extended_source_language,
                                          reject_symlinks, validate_text)
from offline_translation import MODEL_ID, PROVIDER
from portal_english_commentary import (ID, POLICY, PREFIX, SCOPE, TEXT_TAGS, exact, make_source,
                                      preview_text, put_source, read_source, require, text, validate_source)
from portal_extended_locales import digest, publication_day, stable_bytes
from portal_extended_r2 import (DEFAULT_PREFIX, HEX64, R2IntegrityError, R2NotFound, R2Store,
                               checkpoint_is_valid, require_staging_prefix, safe_relative)

MAX_BODY = 512 * 1024
MAX_MANIFEST = 2 * 1024 * 1024


def hash_value(value):
    require(isinstance(value, str) and HEX64.fullmatch(value), 'English hash identity differs')
    return value


def checked_cpu_producer(value):
    exact(value, ['run_id', 'attempt', 'sha', 'repository', 'workflow'])
    require(value['workflow'] == '.github/workflows/portal-extended-locales-r2.yml'
            and isinstance(value['sha'], str) and re.fullmatch(r'[0-9a-f]{40}', value['sha'])
            and isinstance(value['repository'], str) and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', value['repository'])
            and all(re.fullmatch(r'[1-9][0-9]*', str(value[key])) for key in ('run_id', 'attempt')),
            'English CPU producer identity differs')
    return value


def content_key(doc):
    # CSS/navigation/hreflang updates do not trigger new English inference.
    return digest(stable_bytes({'policy': POLICY, **{key: doc[key] for key in
                                 ('id', 'datePublished', 'title', 'blocks')}}))


def read_json(store, key, maximum=65536):
    try:
        return json.loads(store._get(key, maximum=maximum))
    except (UnicodeError, ValueError):
        raise R2IntegrityError('English private JSON is invalid') from None


def put_verified(store, key, value, kind, *, immutable=False, maximum=65536):
    raw = stable_bytes(value); require(len(raw) <= maximum, 'English private record exceeds bound')
    if immutable:
        try:
            previous = store._get(key, maximum=maximum)
        except R2NotFound:
            previous = None
        require(previous is None or previous == raw, 'Immutable English record differs')
        if previous is not None:
            return
    store._put(key, raw, metadata={'kind': kind})
    require(store._get(key, maximum=maximum) == raw, 'English private readback differs')


def read_queue(store):
    try:
        value = read_json(store, store.key('admitted-source-days', 'queue.json'))
    except R2NotFound:
        return []
    exact(value, ['schema_version', 'policy', 'entries'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY and isinstance(value['entries'], list)
            and len(value['entries']) <= 32, 'English admitted-day queue differs')
    seen = set()
    for entry in value['entries']:
        exact(entry, ['day', 'receipt'])
        require(publication_day(entry['day']) == entry['day'] and entry['day'] not in seen,
                'Invalid/duplicate English admitted day')
        hash_value(entry['receipt']); seen.add(entry['day'])
    return value['entries']


def read_admission(store, identity, source_store):
    from portal_extended_daily_queue import checked_producer, inventory, read_admission as original_admission
    hash_value(identity)
    key = store.key('source-admissions', identity, 'receipt.json')
    raw = store._get(key, maximum=65536)
    require(digest(raw) == identity, 'English source receipt checksum differs')
    value = json.loads(raw)
    exact(value, ['schema_version', 'policy', 'scope', 'day', 'generation', 'pages', 'source_admission', 'producer'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY and value['scope'] == SCOPE
            and publication_day(value['day']) == value['day'] and type(value['pages']) is int
            and 1 <= value['pages'] <= 500, 'English admission policy/count differs')
    checked_producer(value['producer']); hash_value(value['generation']); hash_value(value['source_admission'])
    original = original_admission(source_store, value['source_admission'])
    require(original['day'] == value['day'] and original['producer'] == value['producer'],
            'English capture producer/day differs from original source admission')
    _, source_corpus = inventory(source_store, {'day': value['day'], 'admission': value['source_admission']})
    corpus = read_source(store, value['generation'])
    require(corpus['day'] == value['day'] and len(corpus['documents']) == value['pages'])
    by_url = {doc['url']: doc for doc in source_corpus['documents']}
    for doc in corpus['documents']:
        original_doc = by_url.get(doc['source_url'])
        require(original_doc is not None and original_doc['source_html_sha256'] == doc['source_html_sha256'],
                'English editorial projection does not match the same captured source bytes')
    return value, corpus


def read_completed(store, day):
    require(publication_day(day) == day)
    try:
        value = read_json(store, store.key('completed', day, 'state.json'), MAX_MANIFEST)
    except R2NotFound:
        return {}
    exact(value, ['schema_version', 'policy', 'day', 'pages'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY and value['day'] == day
            and isinstance(value['pages'], dict) and len(value['pages']) <= 500, 'English completion receipts differ')
    for identifier, row in value['pages'].items():
        require(isinstance(identifier, str) and ID.fullmatch(identifier) and identifier[:8] == day.replace('-', ''))
        exact(row, ['content_key', 'generation', 'candidate_id'])
        for value_hash in row.values(): hash_value(value_hash)
    return value['pages']


def read_ready_queue(store):
    """Ready candidates awaiting the separate protected publication flow."""
    try:
        value = read_json(store, store.key('pending-publications', 'queue.json'), MAX_MANIFEST)
    except R2NotFound:
        return []
    exact(value, ['schema_version', 'policy', 'entries'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY and isinstance(value['entries'], list)
            and len(value['entries']) <= 500, 'English pending-publication queue differs')
    seen = set()
    for row in value['entries']:
        exact(row, ['day', 'generation', 'candidate_id'])
        require(publication_day(row['day']) == row['day']); hash_value(row['generation']); hash_value(row['candidate_id'])
        identity = row['generation'], row['candidate_id']
        require(identity not in seen, 'Duplicate English ready candidate'); seen.add(identity)
    return value['entries']


def queue_ready_candidate(store, source, candidate):
    entries = read_ready_queue(store)
    row = {'day': source['day'], 'generation': source['generation'], 'candidate_id': candidate}
    if row not in entries:
        require(len(entries) < 500, 'Unpublished English candidates exceed bound; nothing discarded')
        entries.append(row)
        put_verified(store, store.key('pending-publications', 'queue.json'),
                     {'schema_version': 1, 'policy': POLICY, 'entries': entries},
                     'english-pending-publications', maximum=MAX_MANIFEST)


def completed_day_is_durable(store, entry):
    """Prune only a translation cursor, never its unpublished candidate/source.

    Finished days have a second durable publication queue. Admission snapshots,
    checkpoint objects and ready candidates are not deleted. A publisher still
    needs the protected exact-source/version approval; this is NOT an approval.
    """
    raw = store._get(store.key('source-admissions', hash_value(entry['receipt']), 'receipt.json'), maximum=65536)
    require(digest(raw) == entry['receipt'], 'English completed admission checksum differs')
    receipt = json.loads(raw)
    exact(receipt, ['schema_version', 'policy', 'scope', 'day', 'generation', 'pages', 'source_admission', 'producer'])
    require(receipt['schema_version'] == 1 and receipt['policy'] == POLICY and receipt['scope'] == SCOPE
            and receipt['day'] == entry['day'])
    source = read_source(store, receipt['generation']); require(len(source['documents']) == receipt['pages'])
    completed = read_completed(store, entry['day'])
    if any(completed.get(doc['id'], {}).get('content_key') != content_key(doc) for doc in source['documents']):
        return False
    queued = {(row['generation'], row['candidate_id']) for row in read_ready_queue(store)}
    verified = {}
    for doc in source['documents']:
        row = completed[doc['id']]; identity = row['generation'], row['candidate_id']
        require(identity in queued, 'Completed English day has no durable publication queue entry')
        if identity not in verified:
            base = store.key('candidates', *identity)
            ready = read_json(store, base+'/candidate-ready.json', MAX_MANIFEST)
            require(ready.get('policy') == POLICY and ready.get('ready') is True and ready.get('indexable') is False
                    and ready.get('generation') == row['generation'] and ready.get('candidate_id') == row['candidate_id'])
            checked_cpu_producer(ready['producer'])
            batch = read_source(store, row['generation'])
            manifest_raw = store._get(base+'/candidate-manifest.json', maximum=MAX_MANIFEST)
            require(digest(manifest_raw) == row['candidate_id'], 'English queued candidate identity differs')
            manifest = verify_manifest(json.loads(manifest_raw), batch)
            require(manifest['status'] == 'complete-candidate')
            verified[identity] = {item['id']: content_key(item) for item in batch['documents']}
        require(verified[identity].get(doc['id']) == content_key(doc), 'English completed candidate content differs')
    return True


def pending_docs(store, corpus):
    rows = read_completed(store, corpus['day'])
    return [doc for doc in corpus['documents'] if rows.get(doc['id'], {}).get('content_key') != content_key(doc)]


def prepare_queued(store, source_store, *, limit=24):
    require(type(limit) is int and 1 <= limit <= 24, 'English batch limit must be 1..24')
    for entry in sorted(read_queue(store), key=lambda row: row['day'], reverse=True):
        receipt, corpus = read_admission(store, entry['receipt'], source_store)
        require(entry['day'] == corpus['day'], 'English queue day differs')
        pending = pending_docs(store, corpus)
        if not pending:
            continue
        batch = make_source(sorted(pending, key=lambda doc: doc['id'])[:limit], corpus['day'])
        put_source(store, batch)
        proof = {'schema_version': 1, 'policy': POLICY, 'admission': entry['receipt'],
                 'inventory_generation': corpus['generation'], 'generation': batch['generation'],
                 'day': corpus['day']}
        key = store.key('batch-admissions', batch['generation'], 'receipt.json')
        try:
            existing = read_json(store, key)
        except R2NotFound:
            existing = None
        if existing is None:
            put_verified(store, key, proof, 'english-batch-admission', immutable=True)
        else:
            # Preserve the first immutable capture when content and generation
            # recur. Verify it independently, not by replacing its provenance.
            batch_admission(store, source_store, batch['generation'])
        return {'job': {'locale': 'en', 'generation': batch['generation'], 'day': corpus['day']},
                'admission': entry['receipt'], 'pending_count': len(pending), 'selected_pages': len(batch['documents'])}
    return {'job': None, 'admission': '', 'pending_count': 0, 'selected_pages': 0}


def prepare_exact(store, source_store, generation):
    """Read-only recovery of one already admitted English batch, with no recapture."""
    proof, admitted, source = batch_admission(store, source_store, generation)
    return {'has_work': True, 'generation': generation, 'day': source['day'],
            'locales_json': '["en"]', 'requested_locales': '', 'stopped_locales_json': '[]',
            'locale_jobs_json': json.dumps([{'locale': 'en', 'generation': generation, 'day': source['day']}]),
            'source_admission': '', 'english_admission': proof['admission'],
            'english_pending_count': str(len(pending_docs(store, read_source(store, admitted['generation'])))),
            'selected_page_count': len(source['documents']), 'recovery_exact_batch': True,
            'source_writes': 0, 'paid_provider_requests': 0}


def batch_admission(store, source_store, generation):
    hash_value(generation)
    proof = read_json(store, store.key('batch-admissions', generation, 'receipt.json'))
    exact(proof, ['schema_version', 'policy', 'admission', 'inventory_generation', 'generation', 'day'])
    require(proof['schema_version'] == 1 and proof['policy'] == POLICY and proof['generation'] == generation)
    admitted, corpus = read_admission(store, proof['admission'], source_store)
    require(admitted['generation'] == proof['inventory_generation'] and admitted['day'] == proof['day'])
    subset = read_source(store, generation)
    by_id = {doc['id']: doc for doc in corpus['documents']}
    require(subset['day'] == corpus['day'] and 1 <= len(subset['documents']) <= 24
            and all(by_id.get(doc['id']) == doc for doc in subset['documents']), 'English candidate is outside its admitted inventory')
    return proof, admitted, subset


def followup_needed(store, source_store, admission, before):
    require(type(before) is int and before > 0, 'English previous frontier is invalid')
    _, corpus = read_admission(store, admission, source_store)
    after = len(pending_docs(store, corpus))
    return {'continue': after > 0 and after < before, 'before': before, 'after': after,
            'durable_page_progress': after < before}


def verify_manifest(value, source):
    docs = validate_source(source)
    version = value.get('schema_version') if isinstance(value, dict) else None
    require(type(version) is int and version in {1, 2}, 'English candidate schema differs')
    exact(value, ['schema_version', 'policy', 'locale', 'scope', 'day', 'provider', 'model', 'paid_provider_requests',
                  'generation', 'source_document_count', 'completed_page_count', 'items', 'failures', 'budget_exhausted',
                  'translation_calls', 'cache_hits', 'indexable', 'status']
                 + (['public_files_sha256'] if version == 2 else []))
    if version == 2: hash_value(value['public_files_sha256'])
    require(value['policy'] == POLICY and value['locale'] == 'en'
            and value['scope'] == SCOPE and value['day'] == source['day'] and value['generation'] == source['generation']
            and value['model'] == MODEL_ID and value['provider'] == PROVIDER and value['paid_provider_requests'] == 0
            and value['indexable'] is False, 'English candidate provenance differs')
    require(1 <= len(docs) <= 24 and type(value['source_document_count']) is int and value['source_document_count'] == len(docs))
    require(type(value['completed_page_count']) is int and isinstance(value['items'], list)
            and value['completed_page_count'] == len(value['items']) <= len(docs))
    require(isinstance(value['failures'], list) and len(value['failures']) <= len(docs)
            and type(value['budget_exhausted']) is bool)
    require(all(type(value[key]) is int and value[key] >= 0 for key in ('translation_calls', 'cache_hits')))
    require(value['status'] in {'complete-candidate', 'incomplete-candidate'})
    complete = len(value['items']) == len(docs) and not value['failures'] and not value['budget_exhausted']
    require((value['status'] == 'complete-candidate') == complete, 'English candidate completion differs')
    by_id = {doc['id']: doc for doc in docs}; seen = set()
    for item in value['items']:
        exact(item, ['id', 'title', 'preview', 'datePublished', 'editorial_sha256', 'body_sha256'])
        require(item['id'] in by_id and item['id'] not in seen, 'English candidate ID differs'); seen.add(item['id'])
        doc = by_id[item['id']]
        require(item['datePublished'] == doc['datePublished'] and item['editorial_sha256'] == doc['editorial_sha256'])
        hash_value(item['body_sha256']); text(item['title'], 500, english=True); text(item['preview'], 640, english=True)
    for failure in value['failures']:
        exact(failure, ['id', 'code'])
        require(failure['id'] in by_id and failure['id'] not in seen and isinstance(failure['code'], str)
                and re.fullmatch(r'[a-z][a-z0-9-]{0,80}', failure['code']))
    return value


def verify_body(raw, item, doc):
    require(0 < len(raw) <= MAX_BODY and digest(raw) == item['body_sha256'], 'English body checksum differs')
    body = json.loads(raw)
    exact(body, ['schema_version', 'policy', 'locale', 'content_kind', 'id', 'title', 'preview', 'datePublished', 'editorial_sha256', 'blocks'])
    require(body['schema_version'] == 1 and body['policy'] == POLICY and body['locale'] == 'en'
            and body['content_kind'] == 'secondary-commentary', 'English body policy differs')
    require(all(body[key] == item[key] for key in ('id', 'title', 'preview', 'datePublished', 'editorial_sha256')))
    require(isinstance(body['blocks'], list) and len(body['blocks']) == len(doc['blocks']))
    # Current English SEO policy also applies to immutable legacy candidates;
    # validate their stored bytes without rewriting their manifest or body.
    validate_text(doc['title'], text(body['title'], 500, english=True), 'en', extended_source_language(doc['title']),
                  quantity_policy='advisory')
    for translated, original in zip(body['blocks'], doc['blocks'], strict=True):
        exact(translated, ['tag', 'text'])
        require(translated['tag'] == original['tag'] and translated['tag'] in TEXT_TAGS)
        validate_text(original['text'], text(translated['text'], english=True), 'en', extended_source_language(original['text']),
                      quantity_policy='advisory')
    require(body['preview'] == preview_text(body['blocks']), 'English preview is not our secondary interpretation')
    return body


def candidate_files(directory, manifest, source, *, check_current_ui=True):
    from portal_english_ui import detail, homepage
    reject_symlinks(directory)
    by_id = {doc['id']: doc for doc in source['documents']}
    expected = {'candidate-manifest.json': stable_bytes(manifest)}
    for item in manifest['items']:
        relative = f'private/bodies/{item["body_sha256"]}.json'
        path = directory/relative
        require(path.is_file() and path.stat().st_size <= MAX_BODY, 'English private body is missing')
        raw = path.read_bytes(); verify_body(raw, item, by_id[item['id']]); expected[relative] = raw
        relative = f'public/en/blog/{item["id"]}.html'
        expected[relative] = detail(item) if check_current_ui else (directory/relative).read_bytes()
    if manifest['items']:
        expected['public/en/index.html'] = homepage(manifest['items']) if check_current_ui else (directory/'public/en/index.html').read_bytes()
    actual = {path.relative_to(directory).as_posix() for path in directory.rglob('*') if path.is_file()}
    require(actual == set(expected), 'Unexpected/missing English candidate file')
    files = {}
    for relative, raw in expected.items():
        require(0 < len(raw) <= MAX_MANIFEST and (directory/relative).read_bytes() == raw, 'English public/private candidate bytes differ')
        files[relative] = {'sha256': digest(raw), 'bytes': len(raw)}
    if manifest['schema_version'] == 2:
        public_files = {relative: descriptor for relative, descriptor in files.items() if relative.startswith('public/')}
        require(manifest['public_files_sha256'] == digest(stable_bytes(public_files)),
                'English candidate preview identity differs')
    return files


def persist_candidate(store, source_store, source, directory, producer):
    checked_cpu_producer(producer)
    proof, _, stored_source = batch_admission(store, source_store, source['generation'])
    require(stored_source == source, 'English persisted source differs')
    path = directory/'candidate-manifest.json'; require(path.stat().st_size <= MAX_MANIFEST)
    manifest = verify_manifest(json.loads(path.read_bytes()), source)
    files = candidate_files(directory, manifest, source)
    candidate = digest(stable_bytes(manifest)); generation = source['generation']
    base = store.key('candidates', generation, candidate)
    for relative, descriptor in files.items():
        raw = (directory/relative).read_bytes(); key = base+'/'+safe_relative(relative)
        try:
            previous = store._get(key, maximum=MAX_MANIFEST)
        except R2NotFound:
            previous = None
        require(previous is None or previous == raw, 'Immutable English candidate bytes differ')
        if previous is None:
            store._put(key, raw, metadata={'kind': 'english-candidate-file', 'generation': generation, 'candidate': candidate})
        require(digest(store._get(key, maximum=MAX_MANIFEST)) == descriptor['sha256'], 'English candidate R2 readback differs')
    ready = manifest['status'] == 'complete-candidate'
    if ready:
        value = {'schema_version': 1, 'policy': POLICY, 'locale': 'en', 'generation': generation, 'candidate_id': candidate,
                 'files': files, 'files_sha256': digest(stable_bytes(files)), 'producer': producer,
                 'admission': proof['admission'], 'indexable': False, 'ready': True}
        key = base+'/candidate-ready.json'
        try:
            previous = read_json(store, key, MAX_MANIFEST)
        except R2NotFound:
            previous = None
        if previous is None:
            put_verified(store, key, value, 'english-candidate-ready', immutable=True, maximum=MAX_MANIFEST)
        else:
            require({k:v for k,v in previous.items() if k != 'producer'} == {k:v for k,v in value.items() if k != 'producer'},
                    'English existing ready receipt differs')
        # Durably retain publication work BEFORE retiring any translation work.
        # Completed cursors must not erase a batch awaiting versioned approval.
        queue_ready_candidate(store, source, candidate)
        rows = read_completed(store, source['day'])
        for doc in source['documents']:
            rows[doc['id']] = {'content_key': content_key(doc), 'generation': generation, 'candidate_id': candidate}
        put_verified(store, store.key('completed', source['day'], 'state.json'),
                     {'schema_version': 1, 'policy': POLICY, 'day': source['day'], 'pages': rows},
                     'english-completed-pages', maximum=MAX_MANIFEST)
    return {'ready': ready, 'candidate_id': candidate, 'generation': generation,
            'completed_page_count': len(manifest['items']), 'indexable': False, 'deployed': False}


def restore_candidate(store, source_store, generation, candidate, directory):
    hash_value(generation); hash_value(candidate); reject_symlinks(directory)
    require(not directory.exists() or not any(directory.iterdir()), 'English restore target must be empty')
    base = store.key('candidates', generation, candidate)
    ready = read_json(store, base+'/candidate-ready.json', MAX_MANIFEST)
    exact(ready, ['schema_version', 'policy', 'locale', 'generation', 'candidate_id', 'files', 'files_sha256', 'producer',
                  'admission', 'indexable', 'ready'])
    checked_cpu_producer(ready['producer'])
    require(ready['schema_version'] == 1 and ready['policy'] == POLICY and ready['locale'] == 'en'
            and ready['generation'] == generation and ready['candidate_id'] == candidate
            and ready['ready'] is True and ready['indexable'] is False)
    require(isinstance(ready['files'], dict) and 1 <= len(ready['files']) <= 50
            and ready['files_sha256'] == digest(stable_bytes(ready['files'])), 'English file inventory differs')
    proof, _, source = batch_admission(store, source_store, generation)
    require(ready['admission'] == proof['admission'], 'English ready admission differs')
    for relative, descriptor in ready['files'].items():
        safe_relative(relative); exact(descriptor, ['sha256', 'bytes']); hash_value(descriptor['sha256'])
        require(type(descriptor['bytes']) is int and 0 < descriptor['bytes'] <= MAX_MANIFEST)
        raw = store._get(base+'/'+relative, maximum=MAX_MANIFEST)
        require(len(raw) == descriptor['bytes'] and digest(raw) == descriptor['sha256'], 'English restored file checksum differs')
        path = directory/relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
    manifest_path = directory/'candidate-manifest.json'
    require(manifest_path.is_file() and digest(manifest_path.read_bytes()) == candidate, 'English restored manifest differs')
    manifest = verify_manifest(json.loads(manifest_path.read_bytes()), source)
    require(manifest['status'] == 'complete-candidate', 'English incomplete candidate cannot restore for publication')
    require(candidate_files(directory, manifest, source, check_current_ui=False) == ready['files'], 'English restored file inventory differs')
    return ready, manifest, source


def remember_checkpoint(store, generation, checkpoint):
    # Validate generation through its admitted corpus before updating any memo.
    read_source(store, generation)
    reject_symlinks(checkpoint); require(checkpoint.stat().st_size <= MAX_CHECKPOINT_BYTES)
    result = store.put_checkpoint('en', generation, checkpoint)
    put_verified(store, store.key('checkpoints', 'unit-memo', 'latest.json'),
                 {'schema_version': 1, 'policy': POLICY, 'generation': generation, 'sha256': result['sha256']}, 'english-unit-memo')
    return result


def restore_seed(store, destination):
    try:
        value = read_json(store, store.key('checkpoints', 'unit-memo', 'latest.json'))
    except R2NotFound:
        return {'present': False}
    exact(value, ['schema_version', 'policy', 'generation', 'sha256'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY)
    hash_value(value['generation']); hash_value(value['sha256'])
    # A failed persist may advance the per-generation latest pointer without
    # advancing this cross-generation memo. Restore its immutable snapshot,
    # exactly like the established non-English incremental checkpoint path.
    reject_symlinks(destination)
    key = store.checkpoint_object_key('en', value['generation'], value['sha256'])
    raw = store._get(key, maximum=MAX_CHECKPOINT_BYTES)
    require(digest(raw) == value['sha256'], 'English incremental memo checksum differs')
    checkpoint_is_valid(json.loads(raw), 'en', value['generation'])
    destination.parent.mkdir(parents=True, exist_ok=True); destination.write_bytes(raw)
    return {'present': True, 'locale': 'en', 'generation': value['generation'],
            'sha256': value['sha256'], 'bytes': len(raw)}


def staging_probe(store):
    """Private real R2 I/O, synthetic source, empty memo; no model/publication."""
    from build_portal_extended_locales import Memo
    from portal_english_commentary import extract_editorial, freeze_editorial
    from portal_extended_daily_queue import WORKFLOW, admit
    from portal_extended_incremental import today
    from portal_extended_locales import DAILY_SCOPE, ORIGIN, document_from_html
    import time
    require_staging_prefix(store.prefix)
    original_store = R2Store(store.client, store.bucket, store.prefix+'/original-source')
    day = today(); identifier = day.replace('-', '')+'-0000000000000001'
    url = f'{ORIGIN}/blog/{identifier}.html'
    schema = {'@type': 'BlogPosting', 'url': url, 'datePublished': day,
              'inLanguage': 'zh-Hans', 'author': {'@type': 'Organization', 'name': 'KC桌面'}}
    raw = ('<html lang="zh-Hans"><head><link rel="canonical" href="'+url+'">'
           '<script type="application/ld+json">'+json.dumps(schema)+'</script></head><body>'
           '<article class="blog-article"><header class="blog-article-header"><h1>合成存储测试</h1></header>'
           '<div class="blog-article-content"><p>原始材料不能进入英文。</p>'
           '<section><strong>KC评论：</strong>这是隔离的合成存储评论，不是生产内容。</section>'
           '</div></article></body></html>').encode()
    original = document_from_html(url, raw, exclude_related=True)
    original.update(selection_scope=DAILY_SCOPE, selection_day=day)
    original['content_sha256'] = digest(stable_bytes({k:v for k,v in original.items() if k != 'content_sha256'}))
    producer = {'run_id': '1', 'attempt': '1', 'sha': '0'*40,
                'repository': 'synthetic/staging', 'workflow': WORKFLOW}
    original_receipt = admit(original_store, [original], day, producer)
    english = freeze_editorial(store, [extract_editorial(url, raw, day)], day, producer, original_receipt['admission'])
    prepared = prepare_queued(store, original_store)
    _, _, source = batch_admission(store, original_store, prepared['job']['generation'])
    with tempfile.TemporaryDirectory(prefix='english-private-pipeline-') as temporary:
        root = Path(temporary); checkpoint = root/'checkpoint.json'
        Memo(checkpoint, 'en', None, time.monotonic(), source_generation=source['generation']).save()
        written = remember_checkpoint(store, source['generation'], checkpoint)
        restored = restore_seed(store, root/'restored.json')
        require(restored['sha256'] == written['sha256'] and (root/'restored.json').read_bytes() == checkpoint.read_bytes())
        # Simulate the stored result of a timeout BEFORE the first model call.
        # Never seed fake translations or produce a synthetic ready candidate.
        candidate_dir = root/'incomplete'; candidate_dir.mkdir()
        manifest = {'schema_version': 1, 'policy': POLICY, 'locale': 'en', 'scope': SCOPE, 'day': day,
                    'provider': PROVIDER, 'model': MODEL_ID, 'paid_provider_requests': 0,
                    'generation': source['generation'], 'source_document_count': 1, 'completed_page_count': 0,
                    'items': [], 'failures': [], 'budget_exhausted': True, 'translation_calls': 0,
                    'cache_hits': 0, 'indexable': False, 'status': 'incomplete-candidate'}
        (candidate_dir/'candidate-manifest.json').write_bytes(stable_bytes(manifest))
        cpu = {**producer, 'workflow': '.github/workflows/portal-extended-locales-r2.yml'}
        saved = persist_candidate(store, original_store, source, candidate_dir, cpu)
        require(not saved['ready'] and read_completed(store, day) == {}, 'Incomplete English candidate advanced the cursor')
        key = store.key('candidates', source['generation'], saved['candidate_id'])+'/candidate-manifest.json'
        require(store._get(key, maximum=MAX_MANIFEST) == stable_bytes(manifest), 'English incomplete candidate readback differs')
        try:
            restore_candidate(store, original_store, source['generation'], saved['candidate_id'], root/'forbidden')
        except R2NotFound:
            pass
        else:
            raise R2IntegrityError('Incomplete English candidate restored for publication')
        resumed = prepare_queued(store, original_store)
        require(resumed['job'] == prepared['job'] and resumed['pending_count'] == 1
                and not followup_needed(store, original_store, english['receipt'], 1)['continue'],
                'English timeout lost its admitted source or created an automatic retry loop')
    return {'staging_only': True, 'english_same_capture_restore': 'passed',
            'english_immutable_checkpoint_restore': 'passed', 'english_timeout_cursor_restore': 'passed',
            'incomplete_candidate_not_publishable': 'passed', 'generation': source['generation'],
            'checkpoint_sha256': written['sha256'], 'candidate_id': saved['candidate_id'],
            'ready_candidates': 0, 'translation_calls': 0, 'paid_provider_requests': 0, 'deployed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['prepare', 'prepare-exact', 'restore-source', 'restore-seed', 'checkpoint', 'candidate', 'followup', 'staging-probe'])
    parser.add_argument('--prefix', default=PREFIX); parser.add_argument('--source-prefix', default=DEFAULT_PREFIX)
    parser.add_argument('--generation'); parser.add_argument('--corpus', type=Path); parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--directory', type=Path); parser.add_argument('--admission'); parser.add_argument('--before', type=int)
    parser.add_argument('--github-output', type=Path)
    args = parser.parse_args()
    if args.operation == 'staging-probe':
        require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('KC_PUBLIC_REPOSITORY') == 'true',
                'English staging probe requires public Actions')
        require_staging_prefix(args.prefix)
        print(json.dumps(staging_probe(R2Store.from_env(args.prefix)), sort_keys=True)); return
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('KC_PUBLIC_REPOSITORY') == 'true', 'English production pipeline requires reviewed main public Actions')
    require(args.prefix == PREFIX and args.source_prefix == DEFAULT_PREFIX, 'English production namespaces differ')
    store = R2Store.from_env(args.prefix)
    source_store = R2Store(store.client, store.bucket, args.source_prefix)
    if args.operation == 'prepare':
        result = prepare_queued(store, source_store)
    elif args.operation == 'prepare-exact':
        require(os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
                and os.environ.get('GITHUB_WORKFLOW_REF') == os.environ.get('GITHUB_REPOSITORY', '') +
                    '/.github/workflows/portal-extended-locales-r2.yml@refs/heads/main',
                'Exact English recovery requires the serialized reviewed CPU workflow')
        require(args.generation is not None)
        result = prepare_exact(store, source_store, args.generation)
        if args.github_output:
            with args.github_output.open('a') as stream:
                for key, value in result.items():
                    stream.write(key+'='+str(value).lower()+'\n' if isinstance(value, bool) else key+'='+str(value)+'\n')
    elif args.operation == 'restore-source':
        _, _, source = batch_admission(store, source_store, args.generation)
        require(args.corpus is not None); reject_symlinks(args.corpus)
        args.corpus.parent.mkdir(parents=True, exist_ok=True); args.corpus.write_bytes(stable_bytes(source))
        result = {'generation': source['generation'], 'source_restore': 'passed'}
    elif args.operation == 'restore-seed':
        require(args.checkpoint is not None); reject_symlinks(args.checkpoint)
        result = restore_seed(store, args.checkpoint)
    elif args.operation == 'checkpoint':
        require(args.checkpoint is not None); result = remember_checkpoint(store, args.generation, args.checkpoint)
    elif args.operation == 'candidate':
        require(args.corpus is not None and args.directory is not None)
        require(args.corpus.stat().st_size <= 32 * 1024 * 1024)
        source = json.loads(args.corpus.read_bytes()); require(source['generation'] == args.generation)
        producer = {'run_id': os.environ['GITHUB_RUN_ID'], 'attempt': os.environ['GITHUB_RUN_ATTEMPT'],
                    'sha': os.environ['GITHUB_SHA'], 'repository': os.environ['GITHUB_REPOSITORY'],
                    'workflow': '.github/workflows/portal-extended-locales-r2.yml'}
        result = persist_candidate(store, source_store, source, args.directory, producer)
    else:
        result = followup_needed(store, source_store, args.admission, args.before)
        if args.github_output:
            with args.github_output.open('a') as stream: stream.write('continue='+str(result['continue']).lower()+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__': main()
