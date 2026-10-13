"""Replay reviewed, completed Institution originals omitted by a later feed.

Only immutable cached PDFs and publication versions saved by the original run
are eligible. Complete original task membership remains mandatory; no provider
submission, live discovery, seen-state update or replacement PDF is allowed.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re

from mineru_task_ledger import digest, encoded, exact_json, schema_v1
from institution_original_cache import validate_payload, MAX_TOTAL
from institution_dependency_backlog import Backlog, cli_ledger
from mineru_completed_child_reuse import read_completed_batch

ROOT = Path('institution_feeds/completed_source_recovery')
RECEIPTS = Path('institution_feeds/completed_source_recovery_receipts')


def require(value, message):
    if not value:
        raise ValueError('Completed Institution recovery: '+message)


def selection(name):
    require(name == 'adb-261013', 'unreviewed selection')
    path = ROOT/(name+'.json')
    require(not path.is_symlink() and path.is_file() and path.stat().st_size <= 128*1024, 'selection file')
    raw = path.read_bytes()
    require(digest(raw) == 'bdc83ee1f68ee9253f1470e1faed639f5d1fe71483b27e11bc6544ba4ad914d2', 'reviewed selection checksum')
    value = json.loads(raw)
    require(set(value) == {'schema', 'source_run_id', 'date', 'batches', 'sources'}
            and type(value['schema']) is int and value['schema'] == 1
            and value['source_run_id'] == '38338548980' and value['date'] == '261013'
            and isinstance(value['sources'], list) and len(value['sources']) == 6
            and isinstance(value['batches'], list) and len(value['batches']) == 2
            and len(set(value['batches'])) == 2
            and all(re.fullmatch(r'batches/[a-f0-9]{32}', key) for key in value['batches']), 'selection contract')
    return value, digest(raw)


def restore(ledger, cache, backlog, value, output):
    require(ledger.scope == 'institution' and ledger.forbid_new_submissions, 'read-only accepted scope')
    require(not output.exists() or not any(output.iterdir()), 'output must be empty')
    roots = [ledger._read_batch(key)[0] for key in value['batches']]
    bindings = {item['source']: item for root in roots for item in root['files']}
    owners = {item['id']: root['key'] for root in roots for item in root['files']}
    require(len(bindings) == sum(len(root['files']) for root in roots), 'duplicate original source')
    selected, payloads, names = [], [], set()
    for row in value['sources']:
        name = row.get('local_filename'); binding = bindings.get(name)
        require(name not in names and row.get('institution') == 'adb' and binding is not None
                and row.get('sha256') == binding['sha256'] and row.get('bytes') == binding['size'], 'selected original identity')
        names.add(name)
        claim, _ = ledger.store.get('sources/'+binding['id'])
        require(schema_v1(claim) and exact_json(claim.get('binding'), binding)
                and claim.get('batch_key') == owners[binding['id']], 'accepted source claim')
        version, _ = backlog._read('versions/'+binding['id']+'.json')
        require(version is not None, 'original publication provenance missing')
        backlog.validate_versions(version, binding)
        fields = ('local_filename', 'bytes', 'sha256', 'source_page_url', 'published', 'pdf_url')
        require(any(all(exact_json(saved.get(key), row.get(key)) for key in fields)
                    for saved in version['versions'])
                and any(str(receipt.get('run_id')) == value['source_run_id']
                        for receipt in version['receipts']), 'original producer publication mismatch')
        payload = cache.get(binding)
        validate_payload(binding, payload)
        selected.append(binding); payloads.append(payload)
    require(sum(len(payload) for payload in payloads) <= MAX_TOTAL, 'original bytes bound')
    active_holds = backlog.entries()
    held_ids = {item['id'] for record in active_holds.values() for item in record['files']}
    selected_held_count = sum(binding['id'] in held_ids for binding in selected)
    # Inspect all original siblings, including the four already delivered. Their
    # complete success is required, but their PDF bytes are never materialized.
    for root in roots:
        _, counts = read_completed_batch(ledger, root)
        require(counts['all_succeeded'] and counts['completed'] == len(root['files'])
                and counts['failed'] == counts['pending'] == 0, 'original task incomplete')
    output.mkdir(parents=True, exist_ok=True)
    for binding, payload in zip(selected, payloads):
        target = output/binding['source']; target.write_bytes(payload)
        require(exact_json(ledger.bind(target, binding['source']), binding), 'materialized original mismatch')
    manifest = {'date': value['date'], 'institutions': ['adb'], 'downloaded_count': len(selected),
                'downloaded': value['sources'], 'source_checks': [],
                'recovery': {'mode': 'completed_originals', 'source_run_id': value['source_run_id'],
                             'original_members': len(bindings), 'selected_members': len(selected),
                             'selected_sources_in_existing_holds': selected_held_count,
                             'existing_hold_roots_preserved': len(active_holds),
                             'provider_posts': 0, 'fresh_feed_requests': 0}}
    (output/'institution_run_manifest.json').write_bytes(encoded(manifest))
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['restore', 'complete'])
    parser.add_argument('--selection', required=True)
    parser.add_argument('--output', type=Path, default=Path('_institution_latest_pdfs'))
    args = parser.parse_args()
    expected = os.environ.get('GITHUB_REPOSITORY', '')+'/.github/workflows/institution-latest-pdf-to-wechat.yml@refs/heads/main'
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and os.environ.get('GITHUB_WORKFLOW_REF') == expected, 'manual main producer required')
    value, checksum = selection(args.selection)
    receipt = RECEIPTS/(args.selection+'.json')
    if args.operation == 'complete':
        require(not receipt.exists(), 'selection already handed off')
        RECEIPTS.mkdir(parents=True, exist_ok=True)
        receipt.write_bytes(encoded({'schema': 1, 'selection_sha256': checksum,
            'source_run_id': value['source_run_id'], 'handoff_run_id': os.environ['GITHUB_RUN_ID'],
            'selected_sources': [row['sha256'] for row in value['sources']]}))
        return 0
    require(not receipt.exists(), 'selection already handed off; resume its existing publishing job')
    from institution_original_cache import OriginalCache
    ledger = cli_ledger(args.output)
    cache = OriginalCache.single_attempt(ledger.store.client, ledger.store.bucket)
    backlog = Backlog(ledger.store.client, ledger.store.bucket)
    manifest = restore(ledger, cache, backlog, value, args.output)
    print(json.dumps(manifest['recovery'], sort_keys=True))
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f"date_folder={value['date']}\npdf_count={len(value['sources'])}\nsource_health=accepted_source_recovery\nsource_health_required_failure_count=0\n")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
