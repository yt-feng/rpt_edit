#!/usr/bin/env python3
"""Admit a frozen Neutral source tree, without publishing or dispatching anything."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import time
from typing import Any, Callable


PROFILE = 'neutral-code-v1'
SHA = re.compile(r'[0-9a-f]{40}')
WORKFLOW = '.github/workflows/neutral-edge-cutover.yml'
DEFAULT_INPUTS = {
    'operation': 'rehearse', 'translation_scope': 'incremental', 'publication_mode': 'catalog',
    'locale_followup_source': '', 'catalog_recovery_release': '', 'extended_locales': '',
    'extended_source_generation': '', 'extended_candidate_ids': '', 'extended_handoff': '',
    'english_handoff': '',
}
REQUIRED_CODE = frozenset({WORKFLOW, 'portal_suite/site_src/index.html',
    'portal_suite/site_src/assets/app.js', 'workers/edge-static-host/src/index.js',
    'scripts/build_portal_suite_site.py', 'scripts/render_private_config.py'})
SCRIPT_SUFFIXES = frozenset({'.py', '.js', '.mjs', '.cjs', '.sh', '.ts', '.tsx', '.jsx', '.html', '.css'})


class AdmissionError(RuntimeError):
    pass


def require(condition: Any, message: str) -> None:
    if not condition:
        raise AdmissionError(message)


def code_path(path: str) -> bool:
    """Raw tracked code/assets only; never hash live/private/materialized data.

    All executable build helpers are included, even indirect Python imports. A
    helper-code change can conservatively supersede a queued run; catalog,
    reports, archives, locale checkpoints, tests and documentation cannot.
    """
    value = PurePosixPath(path)
    if path == WORKFLOW or path in {'portal_suite/discovery_editorial.json', 'portal_suite/password_rules.json',
                                  'requirements.txt', 'requirements-translation.txt',
                                  'requirements-neutral-release-constraints.txt'}:
        return True
    if path.startswith(('portal_suite/locale_assets/', 'portal_suite/private_assets/',
                        'workers/edge-static-host/src/')):
        return True
    if path.startswith('portal_suite/site_src/'):
        return not path.startswith('portal_suite/site_src/data/')
    if path.startswith('scripts/'):
        return value.suffix in SCRIPT_SUFFIXES and not any(
            part in {'tests', '__pycache__'} or part.startswith('test_') for part in value.parts)
    return False


def run_read(args: list[str], *, cwd: Path, attempts: int = 1,
             sleep: Callable[[float], None] = time.sleep) -> bytes:
    for attempt in range(attempts):
        try:
            result = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, timeout=60, check=False)
            if result.returncode == 0:
                return result.stdout
        except (OSError, subprocess.TimeoutExpired):
            pass
        if attempt + 1 < attempts:
            sleep((1, 3)[min(attempt, 1)])
    # Git/gh output may include private origins or authentication diagnostics.
    raise AdmissionError('source_read_failed')


def projection(root: Path, revision: str) -> list[tuple[str, str, str]]:
    require(SHA.fullmatch(revision), 'invalid_source_revision')
    raw = run_read(['git', 'ls-tree', '-rz', '--full-tree', revision], cwd=root)
    require(len(raw) <= 32 * 1024 * 1024, 'source_tree_exceeds_bound')
    rows = []
    for entry in raw.split(b'\0'):
        if not entry:
            continue
        try:
            descriptor, name = entry.decode('utf-8').split('\t', 1)
            mode, kind, object_sha = descriptor.split(' ')
        except (UnicodeError, ValueError):
            raise AdmissionError('invalid_source_tree') from None
        if not code_path(name):
            continue
        require(kind == 'blob' and mode in {'100644', '100755'} and SHA.fullmatch(object_sha),
                'unsupported_code_object')
        require(not any(character in name for character in '\r\n\t'), 'invalid_code_path')
        rows.append((name, mode, object_sha))
    require(REQUIRED_CODE <= {row[0] for row in rows}, 'incomplete_source_code')
    return sorted(rows)


def fingerprint(rows: list[tuple[str, str, str]]) -> str:
    return hashlib.sha256(json.dumps({'profile': PROFILE, 'files': rows},
        ensure_ascii=True, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def replay_inputs(event_name: str, event: dict[str, Any]) -> tuple[str, dict[str, str]]:
    if event_name != 'workflow_dispatch':
        require(event_name in {'schedule', 'workflow_run', 'repository_dispatch'}, 'unsupported_source_event')
        if event_name == 'repository_dispatch':
            require(event.get('action') == 'portal-dropbox-report-refresh', 'unsupported_repository_dispatch')
        return 'reconstructed_automatic_defaults', {**DEFAULT_INPUTS, 'operation': 'migrate'}
    raw = event.get('inputs')
    require(isinstance(raw, dict) and set(raw) <= set(DEFAULT_INPUTS), 'invalid_manual_input_fields')
    require(all(isinstance(value, str) for value in raw.values()), 'invalid_manual_input_type')
    inputs = {**DEFAULT_INPUTS, **raw}
    require(inputs['operation'] in {'rehearse', 'locale-shadow', 'migrate'}, 'invalid_operation')
    require(inputs['translation_scope'] in {'incremental', 'release', 'month'}, 'invalid_translation_scope')
    require(inputs['publication_mode'] in {'catalog', 'locales'}, 'invalid_publication_mode')
    patterns = {
        'locale_followup_source': r'(?:[1-9][0-9]{0,19}:[1-9][0-9]{0,9})?',
        'catalog_recovery_release': r'(?:[0-9a-f]{32})?',
        'extended_locales': r'(?:all-supported|[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})?(?:,[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})?)*)?',
        'extended_source_generation': r'(?:[0-9a-f]{64})?',
        'extended_candidate_ids': r'(?:[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})?=[0-9a-f]{64}(?:,[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})?=[0-9a-f]{64})*)?',
        'extended_handoff': r'(?:[0-9a-f]{64})?', 'english_handoff': r'(?:[0-9a-f]{64})?',
    }
    for key, pattern in patterns.items():
        require(len(inputs[key]) <= 8192 and re.fullmatch(pattern, inputs[key]), 'invalid_manual_input_value')
    return 'exact_manual_inputs', inputs


def admit(root: Path, *, source_sha: str, main_sha: str, event_name: str,
          event: dict[str, Any], repository: str, run_id: int, run_attempt: int) -> dict[str, Any]:
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'invalid_repository')
    require(type(run_id) is int and run_id > 0 and type(run_attempt) is int and run_attempt > 0,
            'invalid_run_identity')
    mode, inputs = replay_inputs(event_name, event)
    source = projection(root, source_sha)
    current = projection(root, main_sha)
    source_hash, current_hash = fingerprint(source), fingerprint(current)
    before, after = {row[0]: row[1:] for row in source}, {row[0]: row[1:] for row in current}
    changed = sorted(path for path in before.keys() | after.keys() if before.get(path) != after.get(path))
    require(len(changed) <= 10000, 'changed_code_inventory_exceeds_bound')
    return {
        'schema_version': 1, 'profile': PROFILE,
        'state': 'ready' if source_hash == current_hash else 'superseded',
        'publication_attempted': False, 'replay_required': source_hash != current_hash,
        'source': {'repository': repository, 'event': event_name, 'run_id': run_id,
                   'run_attempt': run_attempt, 'head_sha': source_sha},
        'observed_main_sha': main_sha, 'source_code_sha256': source_hash,
        'main_code_sha256': current_hash, 'changed_code_paths': changed,
        'input_mode': mode,
        'original_manual_inputs': event.get('inputs') if event_name == 'workflow_dispatch' else None,
        'replay': {'workflow': Path(WORKFLOW).name, 'ref': 'main', 'inputs': inputs},
        'automatic_dispatch_attempted': False,
    }


def resolve_main(root: Path, repository: str) -> str:
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'invalid_repository')
    value = run_read(['gh', 'api', f'repos/{repository}/git/ref/heads/main',
                      '--jq', '.object.sha'], cwd=root, attempts=3).decode('ascii', errors='replace').strip()
    require(SHA.fullmatch(value), 'unknown_main_revision')
    # Fetch only the audited object for comparison; never change HEAD, the
    # checkout, GITHUB_SHA or the candidate identity used by downstream review.
    run_read(['git', 'fetch', '--quiet', '--no-tags', '--depth=1', '--filter=blob:none', 'origin', value],
             cwd=root, attempts=3)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        require(os.environ.get('GITHUB_REF') == 'refs/heads/main', 'source_is_not_main')
        root = Path.cwd()
        source_sha = os.environ.get('GITHUB_SHA', '')
        head = run_read(['git', 'rev-parse', 'HEAD'], cwd=root).decode('ascii').strip()
        require(SHA.fullmatch(source_sha) and head == source_sha, 'checkout_identity_mismatch')
        event_path = Path(os.environ['GITHUB_EVENT_PATH'])
        require(event_path.stat().st_size <= 1024 * 1024, 'event_exceeds_bound')
        event = json.loads(event_path.read_text())
        require(isinstance(event, dict), 'invalid_event')
        repository = os.environ['GITHUB_REPOSITORY']
        result = admit(root, source_sha=source_sha, main_sha=resolve_main(root, repository),
            event_name=os.environ['GITHUB_EVENT_NAME'], event=event, repository=repository,
            run_id=int(os.environ['GITHUB_RUN_ID']), run_attempt=int(os.environ['GITHUB_RUN_ATTEMPT']))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
        ready = result['state'] == 'ready'
        with Path(os.environ['GITHUB_OUTPUT']).open('a') as output:
            output.write(f"ready={str(ready).lower()}\nstate={result['state']}\n")
        with Path(os.environ['GITHUB_STEP_SUMMARY']).open('a') as summary:
            summary.write('### Neutral source admission\n\n')
            summary.write('Source code matches the main revision observed at admission.\n' if ready else
                'Superseded: publication was skipped before cloud writes. Replay is required; no automatic dispatch was sent. '
                'Download the source-admission artifact and dispatch its `replay.inputs` on `main`.\n')
            summary.write(f"\nFrozen source: `{source_sha}`. Observed main: `{result['observed_main_sha']}`.\n")
        print(json.dumps({key: result[key] for key in ('state', 'profile', 'replay_required',
                                                      'automatic_dispatch_attempted')}, sort_keys=True))
        return 0
    except (AdmissionError, OSError, ValueError, KeyError, UnicodeError):
        print('Neutral source admission failed; no publication was admitted.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
