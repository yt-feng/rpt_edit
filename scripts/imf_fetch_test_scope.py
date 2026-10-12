"""Fetch-only live acceptance of the 17 IMF sources admitted on 2026-10-12.

The reviewed manifest supplies source identities, not its reviewed download URL,
cached bytes or golden PDF hashes. Ordinary discovery, fresh previews and normal
source candidates remain responsible for finding and validating each original.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys

from institution_pending_intake import PendingIntake

SEED = Path('scripts/fixtures/institution_sources/imf_pending_acceptance_20261012.json')
SEED_SHA = 'e0674b735b429c35515319cd6b959f8da1923dc076038ac897e020459d965a5f'
REVIEWED = Path('institution_feeds/reviewed_originals/imf-20261012-reviewed.json')
REVIEWED_SHA = '250557000edbc46f0629393a7a43a139b37926cb54c58535ea498866ccd77e67'
PROTECTED = ('institution_feeds/pending_intake/imf.json', 'institution_feeds/seen_state.json',
             'institution_feeds/institution_pdf_archive.jsonl')
OUT = Path('_fetch_test')


class ScopeError(ValueError):
    pass


def require(value, category):
    if not value:
        raise ScopeError(category)


def digest(path):
    require(path.is_file() and not path.is_symlink(), 'regular_file_required')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def targets(root):
    require(digest(root / SEED) == SEED_SHA and digest(root / REVIEWED) == REVIEWED_SHA,
            'frozen_metadata_changed')
    seed = json.loads((root / SEED).read_text())
    rows = json.loads((root / REVIEWED).read_text())['records']
    PendingIntake(root / SEED, {}, now=datetime.now(timezone.utc), retry_limit=17)
    items = {row['item']['guid']: row['item'] for row in rows}
    require(len(rows) == len(items) == len(seed['items']) == 17, 'target_count_changed')
    require({key: row['item'] for key, row in seed['items'].items()} ==
            {'imf:' + guid: item for guid, item in items.items()}, 'target_identity_changed')
    return items


def fetch(root, date, producer):
    expected = targets(root)
    output = root / OUT
    require(not output.exists(), 'test_output_must_be_fresh')
    before = {path: digest(root / path) for path in PROTECTED}
    output.mkdir()
    shutil.copyfile(root / SEED, output / 'imf-pending-intake.json')
    (output / 'scope-before.json').write_text(json.dumps(before, sort_keys=True))
    original_intake, original_argv = producer.PendingIntake, sys.argv

    class ScopedIntake(original_intake):
        def merge(self, discovered):
            require({row['item']['guid']: row['item'] for row in self.items.values()} == expected,
                    'isolated_intake_identity_changed')
            # The producer has already performed real discovery and classified
            # an empty/error response. Filter only afterwards, preserving raw
            # metadata retained by that call and never synthesizing discovery.
            merged = super().merge(discovered)
            scoped = [item for item in merged if item['guid'] in expected]
            require(len(scoped) == 17 and {item['guid'] for item in scoped} == set(expected),
                    'isolated_scope_changed')
            (output / 'scope-discovery.json').write_text(json.dumps({
                'target_count': 17, 'discovered_count': len(discovered),
                'excluded_fresh_count': len(merged) - len(scoped),
                'target_guids': sorted(expected)}, sort_keys=True))
            return scoped

    producer.PendingIntake = ScopedIntake
    sys.argv = ['fetch', '--output-dir', str(output), '--date', date, '--institutions', 'imf',
                '--since-days', '7', '--max-per-institution', '17', '--max-total', '17',
                '--imf-pending-retries', '17', '--force-reprocess', 'false',
                '--pending-intake-path', str(output / 'imf-pending-intake.json'),
                '--archive-path', str(output / 'test_archive.jsonl'),
                '--seen-state-path', str(output / 'test_seen.json')]
    try:
        return producer.main()
    finally:
        producer.PendingIntake, sys.argv = original_intake, original_argv


def verify(root, date, producer_code):
    import institution_source_health as health
    from pypdf import PdfReader
    expected = targets(root)
    output = root / OUT
    result = {'schema': 1, 'scope': 'imf-reviewed-20261012', 'accepted': False,
              'expected_count': 17, 'producer_exit_code': producer_code, 'reports': []}
    try:
        require(producer_code == 0, 'producer_failed')
        before = json.loads((output / 'scope-before.json').read_text())
        require(before == {path: digest(root / path) for path in PROTECTED}, 'production_state_changed')
        pending = json.loads((output / 'imf-pending-intake.json').read_text())['items']
        original = json.loads((root / SEED).read_text())['items']
        require(set(pending) == set(original), 'pending_scope_changed')
        require(all(all(pending[key][field] == original[key][field]
                        for field in ('item', 'admitted_at', 'since_days')) for key in original),
                'pending_admission_changed')
        manifest = json.loads((output / 'institution_run_manifest.json').read_text())
        classified = health.classify(manifest, producer_exit_code=producer_code, log_exit_code=0,
                                     date_folder=date, institutions='imf')
        require(classified['source_health'] == 'healthy', 'source_health_not_healthy')
        discovery = json.loads((output / 'scope-discovery.json').read_text())
        require(discovery['target_count'] == 17 and discovery['target_guids'] == sorted(expected)
                and type(discovery['discovered_count']) is int and discovery['discovered_count'] > 0,
                'live_discovery_not_proven')
        rows = manifest['downloaded']
        require(len(rows) == 17 and manifest['downloaded_count'] == 17 and manifest['skipped'] == [],
                'exact_count_or_skip_mismatch')
        require(manifest['force_reprocess'] is False and manifest['since_days'] == 7,
                'producer_options_changed')
        by_url = {item['source_url']: item for item in expected.values()}
        require(len({row['source_page_url'] for row in rows}) == 17 and
                {row['source_page_url'] for row in rows} == set(by_url), 'exact_source_set_mismatch')
        filenames = set()
        for row in rows:
            item = by_url[row['source_page_url']]
            require(row['title'] == item['title'] and row['published'] == item['date'],
                    'source_identity_mismatch')
            # classify validates each complete live receipt. Cached originals
            # and ordinary unproven candidate downloads cannot pass this scope.
            proofs = [row[key] for key in ('imf_live_download', 'imf_official_followup') if key in row]
            require(len(proofs) == 1 and proofs[0]['source_guid'] == item['guid'], 'live_proof_missing')
            (health.validate_live_download if 'imf_live_download' in row else health.validate_followup_download)(row)
            proof = proofs[0]
            name = row['local_filename']
            require(Path(name).name == name and name not in filenames, 'pdf_filename_invalid')
            filenames.add(name)
            path = output / name
            require(digest(path) == row['sha256'] and path.stat().st_size == row['bytes'], 'pdf_bytes_mismatch')
            reader = PdfReader(path)
            require(not reader.is_encrypted and len(reader.pages) == proof['pages'] and len(reader.pages) > 0,
                    'pdf_page_count_mismatch')
            result['reports'].append({'source_guid': item['guid'], 'source_url': item['source_url'],
                                      'sha256': row['sha256'], 'bytes': row['bytes'], 'pages': len(reader.pages)})
        require(filenames == {p.name for p in output.glob('*.pdf')}, 'extra_pdf_files')
        archived = [json.loads(line) for line in (output / 'test_archive.jsonl').read_text().splitlines() if line]
        require(archived == rows, 'archive_mismatch')
        result.update(accepted=True, source_health='healthy', verified_count=17,
                      production_state_unchanged=True, bytes=sum(row['bytes'] for row in result['reports']),
                      pages=sum(row['pages'] for row in result['reports']))
    except Exception as error:
        result['error'] = str(error) if type(error) is ScopeError else type(error).__name__
    (output / 'exact-scope-acceptance.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', required=True)
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and sys.platform == 'linux', 'cloud_execution_required')
    import fetch_institution_latest_pdfs as producer
    code = 255
    root = Path.cwd()
    try:
        code = fetch(root, args.date, producer)
    except Exception as error:
        print('Exact IMF fetch failed:', type(error).__name__)
    if not (root / OUT).is_dir():
        return 1
    return 0 if verify(root, args.date, code)['accepted'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
