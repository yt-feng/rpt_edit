#!/usr/bin/env python3
"""Exercise stored candidates against public sources in an unserved R2 namespace.

No model, production-slot write, activation, or Actions content artifact is used.
This is preparation evidence, not production acceptance or approval.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import tempfile

import requests

from portal_extended_incremental import content_key, read_state
from portal_extended_locales import (ORIGIN, ExpansionError, daily_corpus_day, public_url,
                                     select_locales, validate_corpus)
from portal_extended_publication import checked_batches, compose
from portal_extended_r2 import HEX64, R2Store, safe_part


class StagingReplayStore:
    def __init__(self, source, staging):
        if not staging.prefix.startswith('_extended-locales/staging/publication-') or source.prefix == staging.prefix:
            raise ExpansionError('Publication check writes require an isolated staging namespace')
        self.restore_source = source.restore_source
        self.restore_checkpoint = source.restore_checkpoint
        self.restore_candidate = source.restore_candidate
        self.put_source = staging.put_source
        self.put_checkpoint = staging.put_checkpoint
        self.upload_candidate = staging.upload_candidate


def completed_candidates(store, corpus, locales):
    day = daily_corpus_day(corpus)
    docs = validate_corpus(corpus)
    if not day or not 1 <= len(docs) <= 24:
        raise ExpansionError('Publication check requires a bounded stored daily batch')
    candidates = {}
    for locale in locales:
        pages = read_state(store, 'completed', locale, day).get('pages', {})
        ids = set()
        for doc in docs:
            row = pages.get(doc['url'], {})
            if row.get('generation') != corpus['documents_sha256'] or row.get('content_key') != content_key(doc):
                raise ExpansionError(f'Complete matching candidate receipt is absent: {locale}')
            ids.add(safe_part(row.get('candidate_id'), label='candidate id', pattern=HEX64))
        if len(ids) != 1:
            raise ExpansionError(f'Candidate receipt identities differ within batch: {locale}')
        candidates[locale] = ids.pop()
    return checked_batches([{'generation': corpus['documents_sha256'], 'candidates': candidates}])[0]


def snapshot_public(session, root, corpus):
    # No discovery, PDFs, protected APIs or arbitrary origins: exact stored URLs
    # plus the already-established mirrors and public discovery files only.
    requested = {'/': False, '/robots.txt': False, '/sitemap.xml': False}
    for doc in corpus['documents']:
        public_url(doc['url'])
        relative = doc['url'].removeprefix(ORIGIN)
        if not relative.startswith('/') or relative.startswith('//'):
            raise ExpansionError('Unexpected stored public origin')
        requested[relative] = False
        for locale in ('ko', 'ja', 'ar'):
            requested['/'+locale+relative] = True
    count = 0
    for path, optional in requested.items():
        url = ORIGIN + path
        with session.get(url, timeout=(10, 30), stream=True, allow_redirects=False,
                         headers={'User-Agent':'KCDesk-publication-check/1.0'}) as response:
            if optional and response.status_code == 404:
                continue
            if response.status_code != 200:
                raise ExpansionError(f'Publication snapshot HTTP {response.status_code}: {path}')
            maximum = 8*1024*1024 if path.endswith('.xml') else 4*1024*1024
            size, chunks = 0, []
            for chunk in response.iter_content(65536):
                size += len(chunk)
                if size > maximum:
                    raise ExpansionError('Public publication snapshot exceeds byte bound')
                chunks.append(chunk)
        target = root/('index.html' if path == '/' else path.lstrip('/'))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b''.join(chunks))
        count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generation', required=True)
    parser.add_argument('--locales', required=True)
    parser.add_argument('--run-id', required=True)
    args = parser.parse_args()
    generation = safe_part(args.generation, label='source generation', pattern=HEX64)
    if re.fullmatch(r'[0-9]+-[0-9]+', args.run_id) is None:
        raise ExpansionError('Expected exact Actions run/attempt identity')
    locales = select_locales(args.locales)
    source = R2Store.from_env('_extended-locales/v1')
    staging = R2Store(source.client, source.bucket, '_extended-locales/staging/publication-'+args.run_id)
    with tempfile.TemporaryDirectory(prefix='publication-check-') as temporary:
        base = Path(temporary)
        source.restore_source(generation, base/'corpus.json')
        corpus = json.loads((base/'corpus.json').read_text())
        batch = completed_candidates(source, corpus, locales)
        root, work = base/'site', base/'work'
        root.mkdir(); work.mkdir()
        with requests.Session() as session:
            snapshot_count = snapshot_public(session, root, corpus)
        result = compose(root, StagingReplayStore(source, staging), [batch], work)
        print(json.dumps({'status':'passed', 'deployed':False, 'production_writes':0,
            'translation_calls':0, 'paid_provider_requests':0, 'source_generation':generation,
            'candidate_ids':batch['candidates'], 'page_counts':result['page_counts'],
            'public_snapshot_files':snapshot_count, 'staging_prefix':staging.prefix,
            'checkpoint_restores':result['replays']}, sort_keys=True))


if __name__ == '__main__':
    main()
