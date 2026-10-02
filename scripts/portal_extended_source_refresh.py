"""Select the newest published source batch, independent of runner midnight.

Only one newest source day is discovered. Older days are never walked to fill
a batch. The immutable inventory and stable live release are private R2 proof;
page-owned publication dates remain mandatory and are never rewritten.
"""
from __future__ import annotations

import json
import re
from urllib.parse import urlsplit

from collect_portal_extended_sources import inventory_entries
from portal_extended_locales import (ORIGIN, INCREMENTAL_START, ExpansionError,
    daily_corpus_day, digest, publication_day, public_url, stable_bytes)
from portal_extended_r2 import HEX64, MAX_SOURCE_BYTES, R2IntegrityError, R2NotFound

POLICY = 'latest-published-source-refresh-v1'


def require(value, message):
    if not value:
        raise ExpansionError(message)


def checked_inventory(entries):
    require(isinstance(entries, dict) and len(entries) <= 100000, 'Source inventory exceeds bound')
    for url, modified in entries.items():
        require(isinstance(url, str) and public_url(url) == url
                and isinstance(modified, str) and len(modified) <= 64, 'Invalid source inventory row')
    return entries


def latest_day(entries, capture_day):
    require(publication_day(capture_day) == capture_day and capture_day >= INCREMENTAL_START,
            'Invalid source capture date')
    hints = []
    for url, modified in checked_inventory(entries).items():
        path = urlsplit(url).path
        blog = re.fullmatch(r'/blog/(\d{4})(\d{2})(\d{2})-[A-Za-z0-9_.-]+\.html', path)
        if blog:
            day = publication_day('-'.join(blog.groups()))
        elif re.fullmatch(r'/reports/[A-Za-z0-9_-]+\.html', path) and path not in {
                '/reports/index.html', '/reports/topics.html'}:
            day = publication_day(modified)
        else:
            continue
        if INCREMENTAL_START <= day <= capture_day:
            hints.append(day)
    return max(hints, default='')


def checked_release(value):
    require(isinstance(value, dict) and set(value) == {'slot', 'release_id', 'tree_sha256'},
            'Source release fields differ')
    require(value['slot'] in ('a', 'b') and isinstance(value['release_id'], str)
            and re.fullmatch(r'[a-f0-9]{32}', value['release_id'])
            and isinstance(value['tree_sha256'], str) and HEX64.fullmatch(value['tree_sha256']),
            'Source release identity differs')
    return value


def read_release(session):
    response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False,
                           headers={'Cache-Control': 'no-cache'})
    require(response.status_code == 200 and len(response.content) <= 65536, 'Cannot pin source release')
    value = response.json()
    require(isinstance(value, dict) and value.get('schema_version') == 1, 'Invalid live source release')
    return checked_release({key: value.get(key) for key in ('slot', 'release_id', 'tree_sha256')})


def collect_refresh(session, capture_day, *, on_source=None):
    from portal_extended_incremental import collect_today
    before = read_release(session)
    entries = inventory_entries(session)
    day = latest_day(entries, capture_day)
    docs = collect_today(session, day, entries=entries, on_source=on_source) if day else []
    require(read_release(session) == before, 'Source release changed during capture; retry the current release')
    proof = {'schema_version': 1, 'policy': POLICY, 'capture_day': capture_day,
             'day': day, 'release': before, 'inventory': entries}
    return day, docs, proof


def validate_proof(value, corpus):
    from portal_extended_incremental import eligible_url
    require(isinstance(value, dict) and set(value) == {
        'schema_version', 'policy', 'capture_day', 'day', 'release', 'inventory', 'generation'},
        'Source refresh proof fields differ')
    require(value['schema_version'] == 1 and value['policy'] == POLICY, 'Source refresh policy differs')
    checked_release(value['release'])
    day = latest_day(value['inventory'], value['capture_day'])
    require(day and value['day'] == day == daily_corpus_day(corpus)
            and value['generation'] == corpus['documents_sha256'], 'Source refresh batch identity differs')
    require(all(doc['url'] in value['inventory'] and eligible_url(doc['url'], value['inventory'][doc['url']], day)
                for doc in corpus['documents']), 'Source batch is outside its newest published inventory')
    return value


def save_proof(store, proof, corpus):
    value = validate_proof({**proof, 'generation': corpus['documents_sha256']}, corpus)
    raw = stable_bytes(value)
    require(len(raw) <= MAX_SOURCE_BYTES, 'Source refresh proof exceeds bound')
    identity = digest(raw)
    key = store.key('source-refreshes', identity, 'inventory.json')
    try:
        previous = store._get(key, maximum=MAX_SOURCE_BYTES)
    except R2NotFound:
        previous = None
    if previous is None:
        store._put(key, raw, metadata={'kind': 'source-refresh-proof'})
    if store._get(key, maximum=MAX_SOURCE_BYTES) != raw:
        raise R2IntegrityError('Immutable source refresh proof differs')
    return identity


def read_proof(store, identity, corpus):
    require(isinstance(identity, str) and HEX64.fullmatch(identity), 'Invalid source refresh proof identity')
    raw = store._get(store.key('source-refreshes', identity, 'inventory.json'), maximum=MAX_SOURCE_BYTES)
    if digest(raw) != identity:
        raise R2IntegrityError('Source refresh proof checksum differs')
    return validate_proof(json.loads(raw), corpus)
