#!/usr/bin/env python3
"""Cloud-only, read-only backlog metadata gate for the reviewed IMF originals."""
from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

REPOSITORY = 'yt-feng/rpt_edit'
WORKFLOW = '.github/workflows/institution-fetch-test.yml'
BRANCH = 'codex/imf-reviewed-cache-import-20261012'
HELPER_TREE = 'fa269a40dfe9c433b9473c6d6800c1bafe70ee4c'
MANIFEST_SHA = '250557000edbc46f0629393a7a43a139b37926cb54c58535ea498866ccd77e67'
MANIFEST_PATH = 'institution_feeds/reviewed_originals/imf-20261012-reviewed.json'
MAX_SECONDS = 120


class PreflightError(ValueError):
    pass


def require(condition, code):
    if not condition:
        raise PreflightError(code)


def cloud_guard():
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
            and os.environ.get('GITHUB_REF') == 'refs/heads/' + BRANCH
            and os.environ.get('GITHUB_WORKFLOW_REF') == REPOSITORY + '/' + WORKFLOW + '@refs/heads/' + BRANCH,
            'cloud_readonly_workflow_required')


def load_helpers(repo, manifest=None):
    repo = Path(repo).resolve()
    tree = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD^{tree}'], text=True).strip()
    clean = subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain', '--untracked-files=no',
                                     '--', 'scripts', 'institution_feeds'], text=True)
    require(tree == HELPER_TREE and not clean, 'helper_revision')
    sys.path.insert(0, str(repo / 'scripts'))
    import institution_dependency_backlog as backlog
    import institution_verified_originals as verified
    import fetch_institution_latest_pdfs as fetch
    manifest = Path(manifest) if manifest is not None else repo / MANIFEST_PATH
    require(manifest.is_file() and not manifest.is_symlink() and manifest.stat().st_size <= 512 * 1024,
            'manifest_file')
    require(hashlib.sha256(manifest.read_bytes()).hexdigest() == MANIFEST_SHA, 'manifest_hash')
    selection = verified.VerifiedOriginals(manifest, cache_factory=lambda: None)
    rows = list(selection.records.values())
    require(len(rows) == 17, 'manifest_count')
    return repo, backlog, fetch, rows


class MetadataReader:
    """Expose only the existing export's bounded backlog metadata GETs."""
    def __init__(self, client, bucket, prefix, *, clock=time.monotonic):
        self._client, self._bucket, self._prefix = client, bucket, prefix
        self._clock, self._deadline, self.calls = clock, clock() + MAX_SECONDS, 0

    def get_object(self, **kwargs):
        require(set(kwargs) == {'Bucket', 'Key'} and kwargs['Bucket'] == self._bucket
                and isinstance(kwargs['Key'], str) and kwargs['Key'].startswith(self._prefix), 'metadata_target')
        suffix = kwargs['Key'][len(self._prefix):]
        require(suffix == 'active.json' or re.fullmatch(r'(?:records|versions)/[a-f0-9]{64}\.json', suffix),
                'metadata_key')
        require(self._clock() < self._deadline and self.calls < 1201, 'metadata_read_bound')
        self.calls += 1
        return self._client.get_object(**kwargs)

    def __getattr__(self, name):
        raise PreflightError('metadata_operation_forbidden')


def summarize(backlog, rows, fetch, archive, *, resume_function):
    # Same validated immutable index/record/version reads as the production export.
    records = backlog.entries()
    bindings, memberships = {}, {}
    for root in records.values():
        for binding in root['files']:
            identity = binding['id']
            require(identity not in bindings or bindings[identity] == binding, 'conflicting_binding')
            bindings[identity] = binding
            memberships.setdefault(identity, set()).add(root['status'])
    versions = backlog.versions(list(bindings.values()))
    sources = [{key: binding[key] for key in ('source', 'sha256', 'size')} for binding in bindings.values()]
    held_versions = fetch.dependency_hold_versions(Path(archive), sources, versions)
    approved = {row['binding']['id']: row for row in rows}
    matched = {}
    for identity, row in approved.items():
        if identity in bindings:
            require(bindings[identity] == row['binding'], 'approved_binding_mismatch')
            matched['imf:' + row['item']['guid']] = sorted(memberships[identity])
    fetch_holds = sorted('imf:' + row['item']['guid'] for row in rows
                         if fetch.matches_dependency_hold(held_versions, row['binding']['source'], row['item']))
    outside = sorted(identity for identity in bindings if identity not in approved)
    parameters = tuple(inspect.signature(resume_function).parameters)
    require(parameters == ('ledger', 'directory'), 'resume_contract_changed')
    # No resume/dependency/provider/cache-payload calls: eligibility is deliberately unknown.
    return {
        'status': 'backlog_metadata_verified', 'manifest_sha256': MANIFEST_SHA,
        'approved_count': len(rows), 'total_active_roots': len(records),
        'dependency_hold_roots': sum(row['status'] == 'dependency_hold' for row in records.values()),
        'resuming_roots': sum(row['status'] == 'resuming' for row in records.values()),
        'total_active_sources': len(bindings),
        'approved_exact_binding_match_count': len(matched),
        'approved_exact_binding_matches': matched,
        'approved_fetch_hold_match_count': len(fetch_holds),
        'approved_fetch_hold_source_keys': fetch_holds,
        'outside_approved_source_count': len(outside),
        'outside_approved_binding_ids': outside,
        'resume_selected_source_filter_supported': False,
        'resume_eligibility_checked': False,
        'no_backlog_scope_expansion': not bindings,
        'provider_requests': 0, 'pdf_reads': 0, 'writes': 0,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--manifest', type=Path)
    args = parser.parse_args(argv)
    cloud_guard()  # Before loading any storage configuration or client.
    repo, module, fetch, rows = load_helpers(args.repo, args.manifest)
    from persist_legacy_mineru_inspection import single_attempt_store
    store = single_attempt_store()
    reader = MetadataReader(store.client, store.bucket, module.PREFIX)
    backlog = module.Backlog(reader, store.bucket)
    result = summarize(backlog, rows, fetch, repo / 'institution_feeds/institution_pdf_archive.jsonl',
                       resume_function=module.resume)
    result['metadata_gets'] = reader.calls
    return result


if __name__ == '__main__':
    try:
        print(json.dumps(main(), sort_keys=True))
    except Exception as error:
        code = str(error) if type(error) is PreflightError else 'preflight_read_failed'
        print(json.dumps({'status': 'stopped', 'code': code}), file=sys.stderr)
        raise SystemExit(1) from None
