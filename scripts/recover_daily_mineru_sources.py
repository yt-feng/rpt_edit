#!/usr/bin/env python3
"""Resume accepted Daily MinerU tasks, retrying only terminal failed members.

This entry never admits a fresh source or changes an original source claim.
Complete source/task-bound ZIPs and recovery children survive later failures.
The complete source-only handoff feeds the normal Market Views summarizer.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys

from mineru_task_ledger import LedgerError, exact_json
from mineru_terminal_recovery import AUTOMATIC_POLICY, POLICY, TerminalRecovery
from recover_durable_mineru_sources import (
    MANIFEST, OPTIONS, PRODUCER, RecoveryError, recover_sources,
    safe_ledger_error_category, safe_figure_source_ordinal,
)


def require_daily_context(env):
    repository = env.get('GITHUB_REPOSITORY', '')
    run_id, sha = env.get('GITHUB_RUN_ID', ''), env.get('GITHUB_SHA', '')
    if (env.get('GITHUB_ACTIONS') != 'true'
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            or env.get('GITHUB_REF') != 'refs/heads/main'
            or env.get('GITHUB_EVENT_NAME') not in {'schedule', 'workflow_dispatch'}
            or env.get('GITHUB_WORKFLOW_REF') != f'{repository}/{PRODUCER}@refs/heads/main'
            or not re.fullmatch(r'[1-9][0-9]{0,19}', run_id)
            or not re.fullmatch(r'[a-f0-9]{40}', sha)
            or env.get('REPLAY_SOURCE_RUN_ID', '')
            or env.get('MINERU_FORBID_NEW_SUBMISSIONS', '0') != '0'):
        raise RecoveryError('automatic_recovery_daily_context_required')
    return run_id, sha


def terminal_for_original(ledger, root):
    """Resume the immutable original policy; never reset a recovery budget."""
    value, _ = ledger.store.get('recoveries/' + root['key'].split('/')[1])
    if value is None:
        terminal = TerminalRecovery(ledger, automatic=True, daily_retry_limit=3)
    else:
        policy = value.get('policy') if isinstance(value, dict) else None
        if (not isinstance(policy, dict)
                or set(policy) != {'name', 'max_children', 'allowed_error_codes', 'allowed_error_hashes'}
                or policy.get('name') not in {POLICY, AUTOMATIC_POLICY}
                or not isinstance(policy.get('allowed_error_codes'), list)
                or not isinstance(policy.get('allowed_error_hashes'), list)):
            raise LedgerError('Stored terminal recovery controller does not match its original task or fixed policy')
        terminal = TerminalRecovery(ledger, automatic=policy['name'] == AUTOMATIC_POLICY,
            allowed_error_codes=policy['allowed_error_codes'], allowed_error_hashes=policy['allowed_error_hashes'],
            daily_retry_limit=3)
        if not exact_json(terminal.policy, policy):
            raise LedgerError('Stored terminal recovery controller does not match its original task or fixed policy')
    # Validate every saved proof, predecessor and immutable member inventory
    # before the caller can perform a provider request or reserve another child.
    terminal._read_control(root)
    return terminal


def recover_daily(ledger, input_dir, output_dir, expected_reports, date_folder, *,
                  env=None, total_timeout=900, interval=15, **result_options):
    run_id, sha = require_daily_context(os.environ if env is None else env)
    if ledger.forbid_new_submissions:
        raise RecoveryError('automatic_recovery_replay_forbidden')
    return recover_sources(ledger, input_dir, Path(input_dir) / MANIFEST, output_dir,
        expected_reports, date_folder, source_run_id=run_id, allow_fresh=False,
        recovery_run_id=run_id, source_execution_sha=sha, recovery_execution_sha=sha,
        terminal_factory=terminal_for_original, total_timeout=total_timeout,
        timeout=total_timeout, interval=interval, queue_budget=0, continue_batches=True, **result_options)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', required=True)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--expected-reports', required=True, type=int)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--timeout', type=int, default=900)
    args = parser.parse_args(argv)
    try:
        require_daily_context(os.environ)
        # Cloud authentication is checked before importing the runtime SDKs.
        import boto3
        from botocore.config import Config
        import requests
        from mineru_task_ledger import Ledger, Provider, R2Store
        from mineru_result_cache import ResultCache
        from private_workflow_handoff import require_env
        from smoke_mineru_api import NoRedirectHTTP, credentials
        from recover_durable_mineru_sources import download_result
        client = boto3.client('s3',
            endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'),
            aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'), region_name='auto',
            config=Config(connect_timeout=20, read_timeout=30,
                          retries={'total_max_attempts': 1, 'mode': 'standard'}))
        bucket = require_env('R2_BUCKET')
        ledger = Ledger(R2Store('dropbox', client=client, bucket=bucket),
            Provider(NoRedirectHTTP(requests.request), 'https://mineru.net'), 'dropbox',
            'https://mineru.net', OPTIONS, credentials(os.environ))
        receipt = recover_daily(ledger, args.input_dir, args.output_dir,
            args.expected_reports, args.date_folder, total_timeout=args.timeout,
            result_cache=ResultCache(client, bucket), authenticated_downloader=download_result)
    except Exception as error:
        from mineru_figure_sources import FigureSourceError, ERRORS
        if isinstance(error, FigureSourceError):
            category = error.category if error.category in ERRORS else 'figure_proof_invalid'
        elif isinstance(error, LedgerError):
            category = safe_ledger_error_category(error)
        elif isinstance(error, RecoveryError):
            category = str(error)
        else:
            # No credential, result URL or report text enters public diagnostics.
            category = type(error).__name__
        value = {'status': 'incomplete', 'category': category,
                 'source_claims_preserved': True, 'new_source_submissions': 0}
        ordinal = safe_figure_source_ordinal(error, args.expected_reports)
        if ordinal is not None:
            value['source_ordinal'] = ordinal
        print(json.dumps(value, sort_keys=True))
        return 2
    print(json.dumps({'status': 'complete', 'reports': receipt['report_count'],
        'manifest_sha256': receipt['manifest_sha256'],
        'provider_posts': receipt['provider_posts'], 'new_source_submissions': 0,
        'source_claims_preserved': True}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
