"""Visible Institution dependency holds; unchanged tasks never get polled again.

Only the two explicitly reviewed terminal failure classes can become holds.
Private original bindings remain the authority. New sources and changed recovery
controllers are independent of a held root; unknown failures are never deferred.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
from mineru_task_ledger import LedgerError, R2Store, encoded, digest, exact_json, schema_v1
from mineru_completed_child_reuse import _controller, read_completed_batch
from mineru_terminal_recovery import failure_hash
from mineru_result_cache import missing
from institution_original_cache import OriginalCache, MAX_TOTAL, validate_binding

PREFIX = '_workflow-cache/institution-dependencies/v1/'
MAX_ROOTS = 200
MAX_RESUME_SOURCES = 25
MAX_OBJECT = 256 * 1024
ALLOWED = frozenset({
    '0401d529faef13a557a665756d64dc03c646206ce7e74b41854493ec66695f4d',
    '584a7e9062a5fa6c811258b209f7cc1fc40b37864117dfd3bc6a5c2142463542',
})


def require(test, code):
    if not test: raise LedgerError(code)


class Backlog:
    def __init__(self, client, bucket):
        self.client, self.bucket = client, bucket

    def _read(self, key):
        try: response = self.client.get_object(Bucket=self.bucket, Key=PREFIX+key)
        except Exception as error:
            if missing(error): return None, None
            raise LedgerError('Institution backlog read failed') from None
        body = response.get('Body')
        try:
            require(type(response.get('ContentLength')) is int and 0 < response['ContentLength'] <= MAX_OBJECT
                    and body is not None and response.get('ETag'), 'Institution backlog metadata')
            raw = body.read(MAX_OBJECT+1)
            require(len(raw) == response['ContentLength'] and digest(raw) == response.get('Metadata', {}).get('sha256'),
                    'Institution backlog checksum')
            value = json.loads(raw)
            require(isinstance(value, dict), 'Institution backlog object')
            return value, response['ETag']
        finally:
            if callable(getattr(body, 'close', None)): body.close()

    def _write(self, key, value, version=None):
        raw = encoded(value); require(len(raw) <= MAX_OBJECT, 'Institution backlog size')
        condition = {'IfMatch': version} if version else {'IfNoneMatch': '*'}
        # A failed/ambiguous write stops. No write retry or lost-ACK readback.
        self.client.put_object(Bucket=self.bucket, Key=PREFIX+key, Body=raw, ContentType='application/json',
            Metadata={'sha256': digest(raw)}, CacheControl='private, no-store', **condition)
        actual, _ = self._read(key)
        require(exact_json(actual, value), 'Institution backlog readback')

    def entries(self):
        value, _ = self._read('active.json')
        if value is None: return {}
        self.validate_index(value)
        result = {}
        for key, checksum in value['roots'].items():
            require(re.fullmatch(r'batches/[a-f0-9]{32}', key) and re.fullmatch(r'[a-f0-9]{64}', checksum),
                    'Institution backlog reference')
            row, _ = self._read('records/'+checksum+'.json')
            require(row is not None and digest(encoded(row)) == checksum and row.get('root_key') == key,
                    'Institution backlog record')
            self.validate(row); result[key] = row
        return result

    @staticmethod
    def validate(row):
        require(isinstance(row, dict) and set(row) == {'schema', 'scope', 'root_key', 'files', 'dependency_sha256', 'status', 'failure_hashes', 'counts'}
                and schema_v1(row) and row['scope'] == 'institution'
                and row['status'] in {'dependency_hold', 'resuming'}
                and isinstance(row['root_key'], str) and re.fullmatch(r'batches/[a-f0-9]{32}', row['root_key'])
                and isinstance(row['dependency_sha256'], str) and re.fullmatch(r'[a-f0-9]{64}', row['dependency_sha256'])
                and isinstance(row['files'], list) and 1 <= len(row['files']) <= 5
                and isinstance(row['failure_hashes'], list)
                and all(isinstance(value, str) and value in ALLOWED for value in row['failure_hashes'])
                and bool(row['failure_hashes']) and len(set(row['failure_hashes'])) == len(row['failure_hashes']),
                'Institution backlog contract')
        for item in row['files']: validate_binding(item)
        require(len({item['id'] for item in row['files']}) == len(row['files']), 'Institution backlog duplicate source')
        counts = row['counts']
        require(isinstance(counts, dict) and set(counts) == {'admitted', 'completed', 'failed', 'pending'}
                and all(type(value) is int and value >= 0 for value in counts.values())
                and counts['admitted'] == len(row['files']) and counts['pending'] == 0
                and counts['failed'] > 0 and counts['completed'] + counts['failed'] == counts['admitted'],
                'Institution backlog counts')

    @staticmethod
    def validate_index(value):
        require(schema_v1(value) and set(value) == {'schema', 'roots'} and isinstance(value['roots'], dict)
                and len(value['roots']) <= MAX_ROOTS, 'Institution backlog index')
        for key, checksum in value['roots'].items():
            require(isinstance(key, str) and re.fullmatch(r'batches/[a-f0-9]{32}', key)
                    and isinstance(checksum, str) and re.fullmatch(r'[a-f0-9]{64}', checksum),
                    'Institution backlog reference')

    def save(self, row):
        self.validate(row)
        value, version = self._read('active.json')
        if value is not None: self.validate_index(value)
        roots = dict((value or {'roots': {}})['roots'])
        checksum = digest(encoded(row)); key = 'records/'+checksum+'.json'
        previous, _ = self._read(key)
        if previous is None: self._write(key, row)
        else: require(exact_json(previous, row), 'Institution backlog immutable conflict')
        roots[row['root_key']] = checksum
        require(len(roots) <= MAX_ROOTS, 'Institution backlog limit')
        self._write('active.json', {'schema': 1, 'roots': roots}, version)

    def save_versions(self, bindings, rows, receipts):
        """Retain publication discriminators even if later translation fails."""
        by_id = {item['id']: item for item in bindings}
        for item in by_id.values(): validate_binding(item)
        plans = []
        for sid, binding in by_id.items():
            selected = [row for row in rows if row.get('binding_id') == sid]
            if not selected: continue
            for row in selected:
                require(row.get('local_filename') == binding['source'] and row.get('bytes') == binding['size']
                        and (row.get('sha256') is None or row['sha256'] == binding['sha256']),
                        'Institution publication binding mismatch')
            key = 'versions/'+sid+'.json'; previous, version = self._read(key)
            if previous is not None:
                self.validate_versions(previous, binding)
            existing = {digest(encoded(row)): row for row in (previous or {}).get('versions', [])}
            if previous is not None and all(digest(encoded(row)) in existing for row in selected):
                continue  # Same publication needs no new per-run receipt or write.
            values = {**existing, **{digest(encoded(row)): row for row in selected}}
            proofs = {digest(encoded(row)): row for row in (previous or {}).get('receipts', []) + receipts}
            value = dict(schema=1, binding=binding, versions=list(values.values()), receipts=list(proofs.values()))
            self.validate_versions(value, binding)
            if not exact_json(previous, value): plans.append((key, value, version))
        for key, value, version in plans: self._write(key, value, version)

    @staticmethod
    def validate_versions(value, binding):
        require(schema_v1(value) and set(value) == {'schema', 'binding', 'versions', 'receipts'}
                and exact_json(value['binding'], binding) and isinstance(value['versions'], list)
                and 1 <= len(value['versions']) <= 16 and isinstance(value['receipts'], list)
                and len(value['receipts']) <= 32, 'Institution publication versions')
        for row in value['versions']:
            require(isinstance(row, dict) and row.get('binding_id') == binding['id']
                    and row.get('local_filename') == binding['source'] and type(row.get('bytes')) is int
                    and row['bytes'] == binding['size']
                    and (row.get('sha256') is None or row['sha256'] == binding['sha256'])
                    and all(isinstance(row.get(key), str) and 0 < len(row[key]) <= 2048
                            for key in ('source_page_url', 'published', 'pdf_url')),
                    'Institution publication version binding')

    def versions(self, bindings):
        rows = []
        for binding in bindings:
            value, _ = self._read('versions/'+binding['id']+'.json')
            if value is not None:
                self.validate_versions(value, binding); rows.extend(value['versions'])
        return rows

    def complete(self, keys):
        # The immutable record remains recoverable; only the active index changes.
        value, version = self._read('active.json')
        if value is None: return
        self.validate_index(value)
        self.validate_index({'schema': 1, 'roots': keys})
        roots = dict(value['roots'])
        for key, checksum in keys.items():
            # A root that returned to a hold or changed during independent work
            # remains pending; a sibling's successful handoff cannot clear it.
            if roots.get(key) != checksum: continue
            row, _ = self._read('records/'+checksum+'.json')
            require(row and digest(encoded(row)) == checksum and row.get('root_key') == key
                    and row.get('status') == 'resuming', 'Institution handoff was not resumed')
            self.validate(row)
            roots.pop(key)
        self._write('active.json', {'schema': 1, 'roots': roots}, version)


def configured(ledger):
    require(ledger.scope == 'institution' and isinstance(ledger.store, R2Store), 'Institution private backlog required')
    original = OriginalCache.single_attempt(ledger.store.client, ledger.store.bucket)
    return original, Backlog(original.client, original.bucket)


def availability(cache, binding):
    try: head = cache.client.head_object(Bucket=cache.bucket, Key=cache.key(binding))
    except Exception as error:
        if missing(error): return False
        raise LedgerError('Institution original availability failed') from None
    require(head.get('ContentLength') == binding['size'] and head.get('ContentType') == 'application/pdf'
            and head.get('Metadata') == {'sha256': binding['sha256'], 'kind': 'institution-original-proof'},
            'Institution original availability mismatch')
    return True


def dependency(ledger, root, cache):
    current, _ = ledger._read_batch(root['key'])
    require(exact_json(current, root) and 'recovery_parent' not in root and root['state'] in {'accepted', 'uploaded', 'terminal'}
            and root.get('batch_id'), 'Institution original root changed')
    values = {root['key']: root}
    for item in root['files']:
        key = 'sources/'+item['id']; claim, _ = ledger.store.get(key)
        require(schema_v1(claim) and exact_json(claim.get('binding'), item) and claim.get('batch_key') == root['key'],
                'Institution original claim changed')
        values[key] = claim
    terminal, key, control = _controller(ledger, root); values[key] = control
    for entry in (control or {}).get('children', []):
        child, _ = terminal._child(root, key, entry, create=False)
        values[entry['key']] = child
    present = {item['id']: availability(cache, item) for item in root['files']}
    return digest(encoded({'tasks': values, 'originals': present})), present


def known_hold(ledger, root, cache, observed=None):
    rows, counts = observed if observed is not None else read_completed_batch(ledger, root)
    if counts['pending'] or not counts['failed']: return None
    hashes = {failure_hash(row) for row in rows.values() if str(row['state']).lower() in {'failed', 'fail', 'error'}}
    if not hashes or not hashes <= ALLOWED: return None
    checksum, _ = dependency(ledger, root, cache)
    return {'schema': 1, 'scope': 'institution', 'root_key': root['key'], 'files': root['files'],
            'dependency_sha256': checksum, 'status': 'dependency_hold', 'failure_hashes': sorted(hashes),
            'counts': {key: counts[key] for key in ('admitted', 'completed', 'failed', 'pending')}}


def filter_sources(ledger, sources):
    """Separate held roots before they can block unrelated new provider work."""
    cache, backlog = configured(ledger); held = backlog.entries(); roots, bindings = {}, {}
    for path, source in sources:
        binding = ledger.bind(path, source); bindings[Path(path)] = binding
        claim, _ = ledger.store.get('sources/'+binding['id'])
        if claim is None: continue
        require(schema_v1(claim) and exact_json(claim.get('binding'), binding), 'Institution source claim mismatch')
        root, _ = ledger._read_batch(claim['batch_key']); roots[root['key']] = root
    blocked = set()
    for key, root in roots.items():
        checksum, _ = dependency(ledger, root, cache)
        previous = held.get(key)
        if previous and previous['status'] == 'dependency_hold' and previous['dependency_sha256'] == checksum:
            require(exact_json(previous['files'], root['files']), 'Institution held inventory changed')
            blocked.update(item['id'] for item in root['files']); continue
        observed = known_hold(ledger, root, cache)
        if observed is not None:
            backlog.save(observed); blocked.update(item['id'] for item in root['files'])
    eligible = [(path, source) for path, source in sources if bindings[Path(path)]['id'] not in blocked]
    return eligible, len(sources)-len(eligible)


def hold_terminal_failure(ledger, sources):
    cache, backlog = configured(ledger); roots = {}
    for path, source in sources:
        binding = ledger.bind(path, source); claim, _ = ledger.store.get('sources/'+binding['id'])
        require(schema_v1(claim) and exact_json(claim.get('binding'), binding), 'Institution failed source claim')
        root, _ = ledger._read_batch(claim['batch_key']); roots[root['key']] = root
    # Every incomplete root must be a recognized complete terminal failure.
    plans = []
    for root in roots.values():
        observed = read_completed_batch(ledger, root)
        if observed[1]['all_succeeded']: continue
        row = known_hold(ledger, root, cache, observed)
        if row is None: return False
        plans.append(row)
    if not plans: return False
    for row in plans: backlog.save(row)
    return True


def resume(ledger, directory):
    cache, backlog = configured(ledger); rows = backlog.entries(); names = {}; acknowledged = {}; total = 0; selected = 0
    deferred = 0
    for key, record in rows.items():
        root, _ = ledger._read_batch(key)
        require(exact_json(root['files'], record['files']), 'Institution resume inventory changed')
        checksum, available = dependency(ledger, root, cache)
        if record['status'] == 'dependency_hold' and record['dependency_sha256'] == checksum:
            deferred += len(root['files']); continue
        if not all(available.values()):
            deferred += len(root['files']); continue
        size = sum(item['size'] for item in root['files'])
        if total+size > MAX_TOTAL or selected+len(root['files']) > MAX_RESUME_SOURCES: deferred += len(root['files']); continue
        total += size; selected += len(root['files'])
        for item in root['files']:
            payload = cache.get(item); require(payload is not None, 'Institution resume original disappeared')
            target = Path(directory)/'.institution-resume'/item['id']/Path(item['source']).name
            target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(payload)
            names[str(target.resolve())] = item['source']
        updated = dict(record, status='resuming', dependency_sha256=checksum); backlog.save(updated)
        acknowledged[key] = digest(encoded(updated))
    return names, acknowledged, deferred


def preserve_manifest_versions(ledger, sources):
    manifest_path = os.environ.get('INSTITUTION_SOURCE_MANIFEST')
    if manifest_path: require(Path(manifest_path).stat().st_size <= 256*1024, 'Institution source manifest bound')
    raw = Path(manifest_path).read_bytes() if manifest_path else b''
    require(len(raw) <= 256*1024, 'Institution source manifest bound')
    manifest = json.loads(raw) if raw else {'downloaded': []}
    require(isinstance(manifest, dict) and isinstance(manifest.get('downloaded'), list), 'Institution source manifest')
    bindings, rows = [], []
    for path, name in sources:
        binding = ledger.bind(path, name); bindings.append(binding)
        matches = [row for row in manifest['downloaded'] if row.get('local_filename') == name
                   and row.get('sha256') == binding['sha256'] and row.get('bytes') == binding['size']]
        if not matches:
            claim, _ = ledger.store.get('sources/'+binding['id'])
            require(schema_v1(claim) and exact_json(claim.get('binding'), binding),
                    'Institution new original lacks publication provenance')
        for row in matches:
            fields = ('local_filename', 'bytes', 'sha256', 'source_page_url', 'published', 'pdf_url', 'feed_pdf_candidates')
            rows.append(dict({key: row[key] for key in fields if key in row}, binding_id=binding['id']))
    _, backlog = configured(ledger)
    backlog.save_versions(bindings, rows, [{'run_id': os.environ.get('GITHUB_RUN_ID', 'local'),
        'manifest_sha256': digest(raw)}] if raw else [])


def verify_handoff(extracted, translated):
    """Every extracted report must appear in the successful translated handoff."""
    extracted, translated = Path(extracted).resolve(), Path(translated).resolve()
    expected = {path.parent.resolve() for path in extracted.rglob('source_mineru.md')}
    summary = json.loads((translated/'translation_summary.json').read_bytes())
    require(bool(expected) and not summary.get('failures') and summary.get('selected_count') == len(expected)
            and summary.get('successful_count') == len(expected) and isinstance(summary.get('reports'), list)
            and len(summary['reports']) == len(expected), 'Institution translated handoff incomplete')
    actual = set()
    for row in summary['reports']:
        source = Path(row['source_report_dir']).resolve(); output = Path(row['output_dir']).resolve()
        pdf = Path(row['pdf_path']).resolve()
        require(source in expected and source not in actual and translated in output.parents
                and pdf.parent == output and pdf.is_file() and not pdf.is_symlink(),
                'Institution translated handoff binding')
        with pdf.open('rb') as stream: require(stream.read(5) == b'%PDF-', 'Institution translated PDF missing')
        actual.add(source)
    require(actual == expected, 'Institution translated source coverage')
    return len(actual)

def deferred_count(ledger, acknowledgements):
    _, backlog = configured(ledger)
    rows = backlog.entries()
    return len({item['id'] for key, row in rows.items()
                if row['status'] == 'dependency_hold' or key not in acknowledgements
                for item in row['files']})

def handoff_complete(ledger, context):
    _, backlog = configured(ledger)
    backlog.complete(context)


def cli_ledger(output):
    import requests
    from pdf_to_xhs_batch import mineru_tokens_from_env, MINERU_BASE_URL
    from mineru_task_ledger import from_environment
    return from_environment(output, requests, MINERU_BASE_URL,
        {'model': 'vlm', 'language': 'en', 'ocr': True}, mineru_tokens_from_env())


def seed(ledger, keys, version_loader=None):
    cache, backlog = configured(ledger)
    roots = [ledger._read_batch(key)[0] for key in keys]
    plans = []
    for root in roots:
        row = known_hold(ledger, root, cache)
        if row is not None: plans.append(row)
    # Verify all dependencies before recording any hold. No original PDF fetch,
    # provider submission, upload, generation or publication occurs here.
    if version_loader is not None:
        bindings = [item for root in roots for item in root['files']]
        versions, receipts = version_loader(bindings)
        backlog.save_versions(bindings, versions, receipts)
    for row in plans: backlog.save(row)
    return {'status': 'dependencies_deferred', 'original_members': sum(len(root['files']) for root in roots),
            'held_roots': len(plans), 'deferred_sources': sum(len(row['files']) for row in plans),
            'failed_originals': sum(row['counts']['failed'] for row in plans),
            'provider_posts': 0, 'source_bytes_proven': False}


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['export', 'complete', 'verify-handoff'])
    parser.add_argument('--path', type=Path)
    parser.add_argument('--extracted', type=Path)
    parser.add_argument('--translated', type=Path)
    args = parser.parse_args()
    if args.operation == 'verify-handoff':
        print(json.dumps({'translated_handoff_reports': verify_handoff(args.extracted, args.translated)})); return 0
    require(args.path is not None, 'Institution context path required')
    from persist_legacy_mineru_inspection import single_attempt_store
    private = single_attempt_store(); backlog = Backlog(private.client, private.bucket)
    if args.operation == 'export':
        records = backlog.entries()
        sources = {item['id']: {key: item[key] for key in ('source', 'sha256', 'size')}
                   for row in records.values() for item in row['files']}
        bindings = {item['id']: item for row in records.values() for item in row['files']}
        versions = backlog.versions(list(bindings.values()))
        args.path.write_text(json.dumps({'schema': 1, 'sources': list(sources.values()), 'versions': versions}))
        print(json.dumps({'dependency_roots': len(records), 'deferred_sources': len(sources), 'provider_posts': 0}))
    else:
        context = json.loads(args.path.read_text())
        require(isinstance(context, dict), 'Institution handoff context')
        backlog.complete(context)
        print(json.dumps({'translated_handoff_roots': len(context), 'provider_posts': 0}))
    return 0


if __name__ == '__main__': raise SystemExit(main())
