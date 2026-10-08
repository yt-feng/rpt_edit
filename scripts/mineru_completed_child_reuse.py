"""Consume existing terminal recovery results without authorizing any new work.

Original claims and controllers remain immutable. This module only reads stored
bindings and accepted tasks; it never reserves, submits, uploads or extends a
recovery. A pending GET is observed once and left for the recovery producer.
"""
from __future__ import annotations

import copy
from pathlib import Path

from mineru_task_ledger import DONE, FAILED, LedgerError, R2Store, encoded, exact_json, schema_v1
from mineru_terminal_recovery import AUTOMATIC_POLICY, POLICY, TerminalRecovery, task_identity
from mineru_result_cache import OPTIONS, SUPPORTED_SCOPES, identity


def _controller(ledger, root):
    key = 'recoveries/' + root['key'].split('/')[1]
    stored, _ = ledger.store.get(key)
    if stored is None:
        return None, key, None
    policy = stored.get('policy') if isinstance(stored, dict) else None
    if (not isinstance(policy, dict)
            or set(policy) != {'name', 'max_children', 'allowed_error_codes', 'allowed_error_hashes'}
            or policy.get('name') not in {POLICY, AUTOMATIC_POLICY}
            or not isinstance(policy.get('allowed_error_codes'), list)
            or not isinstance(policy.get('allowed_error_hashes'), list)):
        raise LedgerError('Stored completed-child policy is invalid')
    # No daily_retry_limit: this reader cannot grant a new retry authorization.
    terminal = TerminalRecovery(ledger, automatic=policy['name'] == AUTOMATIC_POLICY,
        allowed_error_codes=policy['allowed_error_codes'], allowed_error_hashes=policy['allowed_error_hashes'])
    key, control, _ = terminal._read_control(root)
    return terminal, key, control


def _read_once(ledger, batch):
    """Use Ledger's complete result validation with no sleep or state writes."""
    reader = copy.copy(ledger)
    deadline = ledger.clock() + 60
    stopped = False
    def clock():
        return deadline if stopped else ledger.clock()
    def stop(_seconds):
        nonlocal stopped
        stopped = True
    reader.clock, reader.sleep = clock, stop
    return reader._poll(batch['key'], batch['files'], deadline, 1, 0, persist_terminal=False)


def result_lineage(ledger, binding, root, row):
    """Validate a result's cache context against its immutable stored ancestry."""
    original = {'batch_id': root['batch_id'], 'batch_key': root['key'],
                'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}
    lineage = row.get('_recovery_lineage', original)
    identity(binding, lineage)
    if lineage['child_ordinal'] == 0:
        if not exact_json(lineage, original):
            raise LedgerError('Completed result original lineage mismatch')
        return original
    terminal, key, control = _controller(ledger, root)
    if control is None or lineage['child_ordinal'] > len(control['children']):
        raise LedgerError('Completed result recovery lineage is absent')
    entry = control['children'][lineage['child_ordinal'] - 1]
    child, _ = terminal._child(root, key, entry, create=False)
    if (child is None or child['state'] not in {'accepted', 'uploaded', 'terminal'}
            or not child.get('batch_id') or binding['id'] not in entry['file_ids']):
        raise LedgerError('Completed result recovery task is not accepted')
    expected = TerminalRecovery._lineage(row, child, root, entry['ordinal'])['_recovery_lineage']
    if not exact_json(lineage, expected):
        raise LedgerError('Completed result recovery lineage mismatch')
    return copy.deepcopy(lineage)


def read_completed_batch(ledger, root):
    """GET-only effective coverage for one exact accepted original batch.

    This also serves diagnostics without admitting local sources: its evidence
    is the stored content binding, not a new verification of local PDF bytes.
    """
    current, _ = ledger._read_batch(root['key'])
    if (not exact_json(current, root) or 'recovery_parent' in root
            or root['state'] not in {'accepted', 'uploaded', 'terminal'} or not root.get('batch_id')):
        raise LedgerError('Completed-child original task mismatch')
    snapshots = {root['key']: encoded(root)}
    for binding in root['files']:
        claim_key = 'sources/' + binding['id']
        claim, _ = ledger.store.get(claim_key)
        if (not schema_v1(claim) or not exact_json(claim.get('binding'), binding)
                or claim.get('batch_key') != root['key']):
            raise LedgerError('Completed-child source claim mismatch')
        snapshots[claim_key] = encoded(claim)
    terminal, key, control = _controller(ledger, root)
    if control is not None:
        snapshots[key] = encoded(control)
    task_keys, batch_ids, gets = {root['key']}, {root['batch_id']}, 0
    rows, _ = _read_once(ledger, root); gets += 1
    effective = {sid: TerminalRecovery._lineage(row, root, root, 0) for sid, row in rows.items()}
    predecessor = root
    for entry in (control or {}).get('children', []):
        if not terminal._terminal(rows, predecessor['files']):
            break
        if (entry['proof']['value']['task_identity_sha256'] != task_identity(predecessor)
                or not exact_json(terminal._proof_for_entry(predecessor, rows, control, entry), entry['proof'])):
            raise LedgerError('Completed-child fresh failure proof mismatch')
        child, _ = terminal._child(root, key, entry, create=False)
        if child is None:
            break  # Reservation without an accepted task is never resumed here.
        snapshots[child['key']] = encoded(child)
        if child['state'] not in {'accepted', 'uploaded', 'terminal'} or not child.get('batch_id'):
            break  # Includes ambiguous submitting; no second POST or upload.
        if child['key'] in task_keys or child['batch_id'] in batch_ids:
            raise LedgerError('Completed-child task identity is duplicated')
        task_keys.add(child['key']); batch_ids.add(child['batch_id'])
        rows, _ = _read_once(ledger, child); gets += 1
        for binding in child['files']:
            sid = binding['id']
            if sid in effective and str(effective[sid]['state']).lower() in DONE:
                raise LedgerError('Completed-child overwrites an already completed source')
            effective.pop(sid, None)
            if sid in rows:
                effective[sid] = TerminalRecovery._lineage(rows[sid], child, root, entry['ordinal'])
        predecessor = child
    completed = sum(str(row['state']).lower() in DONE for row in effective.values())
    failed = sum(str(row['state']).lower() in FAILED for row in effective.values())
    counts = {'key': root['key'], 'admitted': len(root['files']),
        'completed': completed, 'failed': failed, 'pending': len(root['files']) - completed - failed,
        'all_succeeded': completed == len(root['files'])}
    for key, expected in snapshots.items():
        current, _ = ledger.store.get(key)
        if current is None or encoded(current) != expected:
            raise LedgerError('Completed-child accepted snapshot changed')
    counts.update(provider_gets=gets, provider_posts=0,
        reused_sources=sum(str(row['state']).lower() in DONE and row['_recovery_lineage']['child_ordinal'] > 0
                           for row in effective.values()))
    return effective, counts


def reuse_completed_children(ledger, sources, results, summary):
    """Return effective full-batch results while retaining original diagnostics."""
    if (not isinstance(ledger.store, R2Store) or ledger.scope not in SUPPORTED_SCOPES
            or (ledger.scope == 'institution' and not exact_json(ledger.options, OPTIONS))):
        return results, summary
    if summary.get('ready_for_generation') is True:
        # This reserved metadata is ours, never an assertion from provider JSON.
        return [(path, {key: value for key, value in row.items() if key != '_recovery_lineage'})
                for path, row in results], summary
    groups, snapshots, selected = {}, {}, {}
    for path, source in sources:
        binding = ledger.bind(path, source)
        claim_key = 'sources/' + binding['id']
        claim, _ = ledger.store.get(claim_key)
        if (not schema_v1(claim) or not exact_json(claim.get('binding'), binding)
                or not isinstance(claim.get('batch_key'), str)):
            raise LedgerError('Completed-child source claim mismatch')
        snapshots[claim_key] = encoded(claim)
        root, _ = ledger._read_batch(claim['batch_key'])
        if ('recovery_parent' in root or root['state'] not in {'accepted', 'uploaded', 'terminal'}
                or not root.get('batch_id') or sum(exact_json(item, binding) for item in root['files']) != 1):
            raise LedgerError('Completed-child original task mismatch')
        if binding['id'] in selected:
            raise LedgerError('Completed-child duplicate selected source')
        selected[binding['id']] = (Path(path), source, binding)
        if root['key'] not in groups:
            terminal, key, control = _controller(ledger, root)
            groups[root['key']] = (root, terminal, key, control)
            snapshots[root['key']] = encoded(root)
            if control is not None:
                snapshots[key] = encoded(control)
    if not any(control and control['children'] for _, _, _, control in groups.values()):
        return results, summary
    if set(groups) != set(summary.get('batch_keys', [])):
        raise LedgerError('Completed-child original summary mismatch')
    resolved, effective_batches, gets = {}, [], 0
    for root, _, _, _ in groups.values():
        effective, counts = read_completed_batch(ledger, root)
        gets += counts.pop('provider_gets')
        counts.pop('provider_posts'); counts.pop('reused_sources')
        effective_batches.append(counts)
        resolved.update(effective)
    # Abort if another writer changed a checked proof or any source changed.
    for key, expected in snapshots.items():
        current, _ = ledger.store.get(key)
        if current is None or encoded(current) != expected:
            raise LedgerError('Completed-child accepted snapshot changed')
    for path, source, binding in selected.values():
        if not exact_json(ledger.bind(path, source), binding):
            raise LedgerError('Completed-child source bytes changed')
    successes = [(path, resolved[sid]) for sid, (path, _, _) in selected.items()
                 if sid in resolved and str(resolved[sid]['state']).lower() in DONE]
    failed = sum(sid in resolved and str(resolved[sid]['state']).lower() in FAILED for sid in selected)
    pending = len(selected) - len(successes) - failed
    reused = sum(row['_recovery_lineage']['child_ordinal'] > 0 for _, row in successes)
    updated = copy.deepcopy(summary)
    updated['original_outcomes'] = {key: summary[key] for key in ('completed', 'failed', 'pending')}
    updated.update(completed=len(successes), failed=failed, pending=pending,
        ready_for_generation=not failed and not pending and all(row['all_succeeded'] for row in effective_batches),
        effective_batches=effective_batches,
        completed_child_reuse={'schema': 1, 'provider_posts': 0, 'provider_gets': gets, 'reused_sources': reused})
    return (successes if updated['ready_for_generation'] else []), updated
