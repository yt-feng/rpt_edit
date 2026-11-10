#!/usr/bin/env python3
"""Wait on an accepted child run despite temporary GitHub read visibility loss."""
from __future__ import annotations

import argparse
import math
import re
import sys
import time

from recover_neutral_runner_loss import GitHub, RecoveryError

ACTIVE = {'queued', 'requested', 'waiting', 'pending', 'in_progress'}


def watch(github, run_id, workflow, *, timeout=4800, read_grace=120, poll=15,
          clock=time.monotonic, sleep=time.sleep):
    if (not re.fullmatch(r'[1-9][0-9]*', str(run_id))
            or not re.fullmatch(r'\.github/workflows/[A-Za-z0-9_.-]+\.ya?ml', workflow)
            or any(not math.isfinite(value) or value <= 0 for value in (timeout, read_grace, poll))
            or timeout > 21600 or read_grace > 300 or poll > 60):
        raise ValueError('invalid_child_watch_request')
    deadline, unreadable_since, previous = clock() + timeout, None, None
    while clock() < deadline:
        try:
            run = github.api('actions/runs/' + str(run_id))
        except RecoveryError as error:
            # Dispatch returned this exact ID. GitHub can briefly return 404
            # before its run read endpoint catches up. Permissions stay fatal;
            # no failed read ever causes another dispatch.
            if str(error) not in {'github_http_404', 'github_read_failed'}:
                raise
            if unreadable_since is None:
                unreadable_since = clock()
            if clock() - unreadable_since >= read_grace:
                raise RecoveryError('accepted_child_read_unavailable') from None
            remaining = deadline - clock()
            if remaining <= 0:
                break
            sleep(min(5, remaining))
            continue
        if (not isinstance(run, dict) or run.get('id') != int(run_id)
                or run.get('path') != workflow or run.get('event') != 'workflow_dispatch'
                or run.get('head_branch') != 'main'
                or any((run.get(key) or {}).get('full_name') != github.repository
                       for key in ('repository', 'head_repository'))
                or run.get('status') not in ACTIVE | {'completed'}):
            raise ValueError('accepted_child_identity_invalid')
        unreadable_since = None
        state = (run['status'], run.get('conclusion'))
        if state != previous:
            print(f'Accepted child {run_id}: status={state[0]} conclusion={state[1]}', flush=True)
            previous = state
        if state[0] == 'completed':
            if state[1] != 'success':
                raise RecoveryError('accepted_child_did_not_succeed')
            return int(run_id)
        remaining = deadline - clock()
        if remaining <= 0:
            break
        sleep(min(poll, remaining))
    raise TimeoutError('accepted_child_wait_deadline_reached')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--run-id', required=True)
    parser.add_argument('--workflow', required=True)
    parser.add_argument('--timeout', type=float, default=4800)
    args = parser.parse_args(argv)
    try:
        watch(GitHub(args.repo), args.run_id, args.workflow, timeout=args.timeout)
    except (RecoveryError, ValueError, TimeoutError) as error:
        print('Child workflow wait failed: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
