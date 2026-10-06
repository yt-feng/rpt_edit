"""Explicit, bounded recovery of verified terminal MinerU failures.

The normal Ledger.run() contract is unchanged. Original source claims continue
to point to their original task and credential. A private recovery controller
reserves two child tasks by default; Daily can durably extend the limit to three.
Only verified failed members can be submitted.
Accepted and ambiguous children are never submitted again.
"""
from __future__ import annotations

import copy
import math
from pathlib import Path
import re
import uuid

from mineru_task_ledger import (
    DONE, FAILED, LedgerError, digest, encoded, exact_json, schema_v1,
)

POLICY = 'terminal-failed-recovery-v1'
AUTOMATIC_POLICY = 'daily-terminal-failed-recovery-v1'
MAX_CHILDREN = 2
DAILY_MAX_CHILDREN = 3
HASH = re.compile(r'[a-f0-9]{64}')
CODE = re.compile(r'[A-Za-z0-9_.:-]{1,128}')


def failure_hash(row):
    """Matches inspect_durable_mineru's private failure-message digest."""
    return digest(encoded({key: row.get(key) for key in ('err_msg', 'error', 'err_code')}))


def error_code(row):
    value = row.get('err_code')
    if value is None:
        value = row.get('error_code')
    if type(value) is int:
        value = str(value)
    return value if isinstance(value, str) and CODE.fullmatch(value) else ''


def task_identity(batch):
    """Immutable accepted-task identity; no credentials or signed URLs."""
    fields = ('key', 'scope', 'endpoint', 'options', 'token_identity', 'files', 'batch_id')
    return digest(encoded({key: batch[key] for key in fields}))


class TerminalRecovery:
    """One exact original batch per call; no fresh sources are admitted.

    ``authorization`` is an explicit reviewed-dispatch run ID and the complete
    original manifest hash. The caller must enforce its cloud workflow origin
    and verify that manifest. Manual recovery requires an explicit allowlist;
    the separately named automatic policy permits only verified terminal failures.
    """

    def __init__(self, ledger, *, allowed_error_codes=(), allowed_error_hashes=(), automatic=False,
                 daily_retry_limit=None):
        self.ledger = ledger
        self.store = ledger.store
        if daily_retry_limit is not None and (type(daily_retry_limit) is not int or daily_retry_limit != DAILY_MAX_CHILDREN):
            raise LedgerError('Daily recovery retry limit must be exactly three')
        self.daily_retry_limit = daily_retry_limit
        codes, hashes = list(allowed_error_codes), list(allowed_error_hashes)
        if (type(automatic) is not bool
                or (automatic and (codes or hashes))
                or not all(isinstance(value, str) and CODE.fullmatch(value) for value in codes)
                or not all(isinstance(value, str) and HASH.fullmatch(value) for value in hashes)):
            raise LedgerError('Invalid explicit terminal recovery allowlist')
        self.policy = {'name': AUTOMATIC_POLICY if automatic else POLICY, 'max_children': MAX_CHILDREN,
                       'allowed_error_codes': sorted(set(codes)),
                       'allowed_error_hashes': sorted(set(hashes))}

    @staticmethod
    def _authorization(value):
        if (not isinstance(value, dict) or set(value) != {'run_id', 'manifest_sha256'}
                or not isinstance(value['run_id'], str)
                or not re.fullmatch(r'[1-9][0-9]{0,19}', value['run_id'])
                or not isinstance(value['manifest_sha256'], str)
                or not HASH.fullmatch(value['manifest_sha256'])):
            raise LedgerError('Explicit recovery run and original manifest hash required')
        return copy.deepcopy(value)

    def _allowed(self, row):
        return (self.daily_retry_limit == DAILY_MAX_CHILDREN
                or self._allowed_proof(error_code(row), failure_hash(row)))

    def _allowed_proof(self, code, message_hash):
        # Automatic recovery is authorized only by its caller's exact main
        # Daily context. _proof still requires a fresh complete terminal GET;
        # pending, missing and successful members can never become children.
        return (self.policy['name'] == AUTOMATIC_POLICY
                or code in self.policy['allowed_error_codes']
                or message_hash in self.policy['allowed_error_hashes'])

    @staticmethod
    def _assert_bytes(files, paths):
        for item in files:
            raw = Path(paths[item['id']]).read_bytes()
            if len(raw) != item['size'] or digest(raw) != item['sha256']:
                raise LedgerError('Original source bytes changed during terminal recovery')

    def _original(self, paths_and_sources):
        if not 1 <= len(paths_and_sources) <= 5:
            raise LedgerError('Terminal recovery requires one complete original batch of one to five PDFs')
        items = [self.ledger.bind(path, source) for path, source in paths_and_sources]
        if len({item['id'] for item in items}) != len(items):
            raise LedgerError('Duplicate original source identity')
        roots = set()
        for item in items:
            reference, _ = self.store.get('sources/' + item['id'])
            if (not schema_v1(reference) or not exact_json(reference.get('binding'), item)
                    or not isinstance(reference.get('batch_key'), str)):
                raise LedgerError('Terminal recovery requires an unchanged original source claim')
            roots.add(reference['batch_key'])
        if len(roots) != 1:
            raise LedgerError('Terminal recovery requires exactly one original task')
        root, _ = self.ledger._read_batch(roots.pop())
        if ('recovery_parent' in root or root['state'] not in {'accepted', 'uploaded', 'terminal'}
                or not isinstance(root.get('batch_id'), str) or not root['batch_id']):
            raise LedgerError('Only an accepted original task can be recovered')
        requested = {item['id']: item for item in items}
        if ({item['id'] for item in root['files']} != set(requested)
                or any(not exact_json(item, requested[item['id']]) for item in root['files'])):
            raise LedgerError('Terminal recovery requires its complete original source inventory')
        paths = {item['id']: path for item, (path, _) in zip(items, paths_and_sources)}
        return root, paths

    @staticmethod
    def _lineage(row, batch, root, ordinal):
        value = copy.deepcopy(row)
        value['_recovery_lineage'] = {
            'batch_id': batch['batch_id'], 'batch_key': batch['key'],
            'parent_batch_key': root['key'], 'data_id': row['data_id'],
            'child_ordinal': ordinal,
        }
        return value

    def _poll(self, batch, root, paths, deadline, interval, queue_budget, ordinal, done_verifier):
        self._assert_bytes(root['files'], paths)
        rows, summary = self.ledger._poll(batch['key'], batch['files'], deadline, interval, queue_budget,
                                        persist_terminal=ordinal != 0)
        self._assert_bytes(root['files'], paths)
        rows = {source_id: self._lineage(row, batch, root, ordinal)
                for source_id, row in rows.items()}
        if done_verifier is not None:
            for source_id, row in rows.items():
                if str(row['state']).lower() in DONE:
                    done_verifier(Path(paths[source_id]), copy.deepcopy(row))
            self._assert_bytes(root['files'], paths)
        return rows, summary

    @staticmethod
    def _terminal(rows, files):
        return (set(rows) == {item['id'] for item in files}
                and all(str(row['state']).lower() in DONE | FAILED for row in rows.values()))

    def _proof(self, predecessor, rows, *, allow_daily=False):
        if not self._terminal(rows, predecessor['files']):
            raise LedgerError('Only a complete freshly verified terminal task authorizes a recovery child')
        values = []
        for item in predecessor['files']:
            row = rows[item['id']]
            failed = str(row['state']).lower() in FAILED
            if failed and not (allow_daily or self._allowed(row)):
                raise LedgerError('Terminal failure is not explicitly authorized for recovery')
            values.append({'data_id': item['id'], 'state': 'failed' if failed else 'done',
                           'error_code': error_code(row) if failed else '',
                           'error_hash': failure_hash(row) if failed else None})
        value = {'task_key': predecessor['key'], 'task_identity_sha256': task_identity(predecessor),
                 'members': values}
        return {'value': value, 'sha256': digest(encoded(value))}

    def _extension(self, root, control):
        extension = control.get('daily_retry_extension')
        if extension is None:
            return None
        expected = {'schema', 'max_children', 'root_identity_sha256',
                    'previous_controller_sha256', 'previous_children_count', 'authorizations'}
        if (not isinstance(extension, dict) or set(extension) != expected
                or type(extension['schema']) is not int or extension['schema'] != 1
                or type(extension['max_children']) is not int or extension['max_children'] != DAILY_MAX_CHILDREN
                or extension['root_identity_sha256'] != task_identity(root)
                or type(extension['previous_children_count']) is not int
                or not 0 <= extension['previous_children_count'] <= MAX_CHILDREN
                or extension['previous_children_count'] > len(control['children'])
                or not isinstance(extension['authorizations'], list)
                or not 1 <= len(extension['authorizations']) <= 1024):
            raise LedgerError('Invalid Daily retry budget extension')
        previous = {key: copy.deepcopy(value) for key, value in control.items() if key != 'daily_retry_extension'}
        previous['children'] = previous['children'][:extension['previous_children_count']]
        if extension['previous_controller_sha256'] != digest(encoded(previous)):
            raise LedgerError('Daily retry extension does not preserve its previous controller')
        seen = set()
        for authorization in extension['authorizations']:
            self._authorization(authorization)
            identity = (authorization['run_id'], authorization['manifest_sha256'])
            if identity in seen:
                raise LedgerError('Duplicate Daily manifest authorization')
            seen.add(identity)
        return extension

    @staticmethod
    def _daily_entry_authorized(control, entry):
        extension = control.get('daily_retry_extension')
        return bool(extension and entry['ordinal'] > extension['previous_children_count']
                    and any(exact_json(entry['authorization'], auth) for auth in extension['authorizations']))

    def _proof_for_entry(self, predecessor, rows, control, entry):
        """Recheck an already validated reservation without broadening old proofs."""
        if not any(exact_json(entry, saved) for saved in control['children']):
            raise LedgerError('Recovery proof entry is absent from its controller')
        return self._proof(predecessor, rows, allow_daily=self._daily_entry_authorized(control, entry))

    def _extend_daily(self, root, paths_and_sources, authorization):
        """CAS-append explicit Daily authority while preserving every old byte binding."""
        verified, paths = self._original(paths_and_sources)
        if verified['key'] != root['key'] or task_identity(verified) != task_identity(root):
            raise LedgerError('Original task changed before Daily retry extension')
        self._assert_bytes(root['files'], paths)
        key, control, version = self._read_control(root)
        if control is None:
            control = {'schema': 1, 'policy': copy.deepcopy(self.policy), 'root_key': root['key'],
                       'root_identity_sha256': task_identity(root), 'children': []}
        extension = control.get('daily_retry_extension')
        if extension and any(exact_json(authorization, auth) for auth in extension['authorizations']):
            return
        updated = copy.deepcopy(control)
        if extension is None:
            updated['daily_retry_extension'] = {'schema': 1, 'max_children': DAILY_MAX_CHILDREN,
                'root_identity_sha256': task_identity(root),
                'previous_controller_sha256': digest(encoded(control)),
                'previous_children_count': len(control['children']), 'authorizations': []}
        updated['daily_retry_extension']['authorizations'].append(copy.deepcopy(authorization))
        self._extension(root, updated)
        self.store.put(key, updated, version)  # Conflict leaves the winning history intact; never reset.

    def _read_control(self, root):
        key = 'recoveries/' + root['key'].split('/')[1]
        control, version = self.store.get(key)
        if control is None:
            return key, None, None
        expected = {'schema', 'policy', 'root_key', 'root_identity_sha256', 'children'}
        if (not schema_v1(control) or set(control) not in (expected, expected | {'daily_retry_extension'})
                or not exact_json(control['policy'], self.policy)
                or control['root_key'] != root['key']
                or control['root_identity_sha256'] != task_identity(root)
                or not isinstance(control['children'], list) or len(control['children']) > DAILY_MAX_CHILDREN):
            raise LedgerError('Stored terminal recovery controller does not match its original task or fixed policy')
        extension = self._extension(root, control)
        if len(control['children']) > (DAILY_MAX_CHILDREN if extension else MAX_CHILDREN):
            raise LedgerError('Stored terminal recovery child count exceeds its durable budget')
        previous_files, previous_key = root['files'], root['key']
        manifest_hash = None
        keys = {root['key']}
        for ordinal, entry in enumerate(control['children'], 1):
            shape = {'key', 'ordinal', 'file_ids', 'initial_token_identity', 'proof', 'authorization'}
            if (not isinstance(entry, dict) or set(entry) != shape or type(entry['ordinal']) is not int
                    or entry['ordinal'] != ordinal or not isinstance(entry['key'], str)
                    or not re.fullmatch(r'batches/[a-f0-9]{32}', entry['key']) or entry['key'] in keys
                    or not isinstance(entry['initial_token_identity'], str)
                    or not HASH.fullmatch(entry['initial_token_identity'])):
                raise LedgerError('Stored terminal recovery child reservation is malformed')
            self._authorization(entry['authorization'])
            daily_entry = bool(extension and ordinal > extension['previous_children_count'])
            if daily_entry:
                if not self._daily_entry_authorized(control, entry):
                    raise LedgerError('Recovery child lacks its registered Daily authorization')
            elif manifest_hash is None:
                manifest_hash = entry['authorization']['manifest_sha256']
            elif entry['authorization']['manifest_sha256'] != manifest_hash:
                raise LedgerError('Stored recovery children refer to different original manifests')
            proof = entry['proof']
            if (not isinstance(proof, dict) or set(proof) != {'value', 'sha256'}
                    or not isinstance(proof['sha256'], str) or not HASH.fullmatch(proof['sha256'])
                    or not isinstance(proof['value'], dict)
                    or set(proof['value']) != {'task_key', 'task_identity_sha256', 'members'}
                    or proof['sha256'] != digest(encoded(proof['value']))
                    or proof['value']['task_key'] != previous_key
                    or not isinstance(proof['value']['task_identity_sha256'], str)
                    or not HASH.fullmatch(proof['value']['task_identity_sha256'])):
                raise LedgerError('Stored terminal recovery proof is malformed')
            members = proof['value']['members']
            ids = [item['id'] for item in previous_files]
            if not isinstance(members, list) or len(members) != len(ids):
                raise LedgerError('Stored terminal recovery proof omits original members')
            failed = []
            for source_id, member in zip(ids, members):
                if (not isinstance(member, dict) or set(member) != {'data_id', 'state', 'error_code', 'error_hash'}
                        or member['data_id'] != source_id or member['state'] not in {'done', 'failed'}):
                    raise LedgerError('Stored terminal recovery proof has invalid member bindings')
                if member['state'] == 'failed':
                    if (not isinstance(member['error_hash'], str) or not HASH.fullmatch(member['error_hash'])
                            or not isinstance(member['error_code'], str)
                            or (member['error_code'] and not CODE.fullmatch(member['error_code']))
                            or not (daily_entry or self._allowed_proof(member['error_code'], member['error_hash']))):
                        raise LedgerError('Stored failure proof is not explicitly authorized')
                    failed.append(source_id)
                elif member['error_hash'] is not None or member['error_code'] != '':
                    raise LedgerError('Stored successful member has invalid failure evidence')
            if not failed or not exact_json(entry['file_ids'], failed):
                raise LedgerError('Stored child inventory differs from its failed original members')
            previous_files = [item for item in previous_files if item['id'] in failed]
            previous_key = entry['key']
            keys.add(previous_key)
        return key, control, version

    def _child_row(self, root, controller_key, entry):
        ids = set(entry['file_ids'])
        return {'schema': 1, 'key': entry['key'], 'scope': root['scope'], 'endpoint': root['endpoint'],
                'options': root['options'], 'token_identity': entry['initial_token_identity'],
                'files': [item for item in root['files'] if item['id'] in ids],
                'state': 'claiming', 'batch_id': None,
                'recovery_parent': {'policy': self.policy['name'], 'root_key': root['key'],
                                    'controller_key': controller_key, 'ordinal': entry['ordinal'],
                                    'proof_sha256': entry['proof']['sha256']}}

    def _child(self, root, controller_key, entry, *, create=False):
        row, version = self.store.get(entry['key'])
        expected = self._child_row(root, controller_key, entry)
        if row is None:
            if not create:
                return None, None
            version = self.store.put(entry['key'], expected)
        row, version = self.ledger._read_batch(entry['key'])
        if (not exact_json(row.get('files'), expected['files'])
                or not exact_json(row.get('recovery_parent'), expected['recovery_parent'])
                or (row['state'] == 'claiming' and row['token_identity'] != entry['initial_token_identity'])):
            raise LedgerError('Recovery child does not match its durable parent reservation')
        rejections = row.get('auth_rejections', [])
        if ((rejections and rejections[0]['token_identity'] != entry['initial_token_identity'])
                or (row['token_identity'] != entry['initial_token_identity'] and not rejections)):
            raise LedgerError('Recovery child credential changed without its original definitive rejection')
        return row, version

    def _reserve(self, root, controller_key, control, version, predecessor, rows, authorization):
        proof = self._proof(predecessor, rows)
        failed = [member['data_id'] for member in proof['value']['members'] if member['state'] == 'failed']
        if not failed:
            raise LedgerError('No terminal failed member can be reserved')
        if control is None:
            control = {'schema': 1, 'policy': copy.deepcopy(self.policy), 'root_key': root['key'],
                       'root_identity_sha256': task_identity(root), 'children': []}
        if len(control['children']) >= (self.daily_retry_limit or MAX_CHILDREN):
            raise LedgerError('Terminal recovery child limit reached; saved tasks retained')
        if self.daily_retry_limit is not None and not any(exact_json(authorization, auth)
                for auth in (control.get('daily_retry_extension') or {}).get('authorizations', [])):
            raise LedgerError('Daily retry reservation requires its persisted authority')
        control = copy.deepcopy(control)
        control['children'].append({'key': 'batches/' + uuid.uuid4().hex,
            'ordinal': len(control['children']) + 1, 'file_ids': failed,
            'initial_token_identity': next(iter(self.ledger.tokens)),
            'proof': proof, 'authorization': copy.deepcopy(authorization)})
        self.store.put(controller_key, control, version)  # Before child creation or any POST.
        return control

    def run(self, paths_and_sources, *, authorization, timeout=1800, interval=15, queue_budget=300,
            done_verifier=None, partial=False):
        """Return full coverage by default; opt-in partial rows retain explicit outcomes."""
        if type(partial) is not bool:
            raise LedgerError('Partial recovery mode must be boolean')
        authorization = self._authorization(authorization)
        if (any(type(value) not in {int, float} or not math.isfinite(value)
                for value in (timeout, interval, queue_budget))
                or timeout <= 0 or interval <= 0 or queue_budget < 0):
            raise LedgerError('Terminal recovery requires positive bounded attempt timing')
        if done_verifier is not None and not callable(done_verifier):
            raise LedgerError('Completed result verifier must be callable')
        self.ledger.submission_posts = 0
        try:
            return self._run(paths_and_sources, authorization, timeout, interval, queue_budget, done_verifier, partial)
        except LedgerError:
            raise
        except Exception as error:
            # Provider/store transport text can contain credentials or signed URLs.
            raise LedgerError('Terminal recovery stopped; saved tasks retained (' + type(error).__name__ + ')') from None

    def _run(self, paths_and_sources, authorization, timeout, interval, queue_budget, done_verifier, partial):
        root, paths = self._original(paths_and_sources)
        deadline = self.ledger.clock() + timeout
        controller_key, control, _ = self._read_control(root)
        if control is not None and control['children'] and self.daily_retry_limit is None:
            manifests = {entry['authorization']['manifest_sha256'] for entry in control['children']}
            manifests.update(auth['manifest_sha256'] for auth in
                             (control.get('daily_retry_extension') or {}).get('authorizations', []))
            if authorization['manifest_sha256'] not in manifests:
                raise LedgerError('Recovery authorization differs from the frozen original manifest')
        root_rows, root_summary = self._poll(root, root, paths, deadline, interval, queue_budget, 0, done_verifier)
        if self.daily_retry_limit is not None and (control is not None or
                (self._terminal(root_rows, root['files']) and any(str(row['state']).lower() in FAILED for row in root_rows.values()))):
            self._extend_daily(root, paths_and_sources, authorization)
        resolved = {source_id: row for source_id, row in root_rows.items() if str(row['state']).lower() in DONE}
        lineage = {source_id: root['key'] for source_id in resolved}
        predecessor, latest_rows = root, root_rows
        child_summaries = []
        interrupted = {}
        index = 0
        while self._terminal(latest_rows, predecessor['files']):
            controller_key, control, version = self._read_control(root)
            entries = control['children'] if control is not None else []
            if index == len(entries):
                if len(resolved) == len(root['files']):
                    break
                if index >= (self.daily_retry_limit or MAX_CHILDREN):
                    break
                control = self._reserve(root, controller_key, control, version, predecessor, latest_rows, authorization)
                entries = control['children']
            entry = entries[index]
            # Fresh terminal GET must still account for exactly the reserved failures.
            current_failed = [item['id'] for item in predecessor['files']
                              if str(latest_rows[item['id']]['state']).lower() in FAILED]
            if (entry['proof']['value']['task_identity_sha256'] != task_identity(predecessor)
                    or current_failed != entry['file_ids']):
                raise LedgerError('Fresh terminal membership differs from the saved recovery reservation')
            if not exact_json(self._proof_for_entry(predecessor, latest_rows, control, entry), entry['proof']):
                raise LedgerError('Fresh terminal failure proof differs from the saved recovery reservation')
            child, child_version = self._child(root, controller_key, entry, create=True)
            if child['state'] == 'submitting':
                if not partial:
                    raise LedgerError('Ambiguous recovery child blocks new submissions; saved task retained')
                interrupted = {item['id']: ('submission_unknown', child['key']) for item in child['files']}
                break
            if child['state'] in {'claiming', 'auth_rejected'}:
                self._assert_bytes(root['files'], paths)
                try:
                    self.ledger._submit_claimed(child, child_version, paths, deadline)
                except Exception:
                    if not partial:
                        raise
                    saved, _ = self._child(root, controller_key, entry)
                    if saved['state'] == 'submitting':
                        interrupted = {item['id']: ('submission_unknown', saved['key']) for item in saved['files']}
                    elif saved['state'] in {'accepted', 'uploaded', 'terminal'}:
                        interrupted = {item['id']: ('pending', saved['key']) for item in saved['files']}
                    else:
                        raise
                    break
                child, _ = self._child(root, controller_key, entry)
            elif child['state'] not in {'accepted', 'uploaded', 'terminal'}:
                raise LedgerError('Unrecognized recovery child state')
            latest_rows, child_summary = self._poll(child, root, paths, deadline, interval, queue_budget,
                                                  entry['ordinal'], done_verifier)
            child_summaries.append(child_summary)
            for source_id, row in latest_rows.items():
                if str(row['state']).lower() in DONE:
                    if source_id in resolved:
                        raise LedgerError('Recovery returned duplicate successful source coverage')
                    resolved[source_id] = row
                    lineage[source_id] = child['key']
            predecessor = child
            index += 1
        self._assert_bytes(root['files'], paths)
        ready = (len(resolved) == len(root['files'])
                 and self._terminal(latest_rows, predecessor['files']))
        unresolved = {item['id'] for item in root['files']} - set(resolved)
        _, final_control, _ = self._read_control(root)
        entries = final_control['children'] if final_control else []
        outcomes = []
        for item in root['files']:
            source_id = item['id']
            retries = [entry for entry in entries if source_id in entry['file_ids']]
            last_key = retries[-1]['key'] if retries else root['key']
            if source_id in resolved:
                status, last_key = 'done', lineage[source_id]
            elif source_id in interrupted:
                status, last_key = interrupted[source_id]
            elif str(latest_rows.get(source_id, {}).get('state', '')).lower() in FAILED:
                status = 'retry_exhausted' if len(retries) >= (self.daily_retry_limit or MAX_CHILDREN) else 'failed'
            else:
                status = 'pending'
            outcomes.append({'data_id': source_id, 'status': status, 'retry_count': len(retries), 'last_task_key': last_key})
        failed = sum(row['status'] in {'failed', 'retry_exhausted'} for row in outcomes)
        summary = {'policy': self.policy['name'], 'root_key': root['key'], 'requested': len(root['files']),
                   'completed': len(resolved), 'failed': failed,
                   'pending': len(unresolved) - failed, 'provider_posts': self.ledger.submission_posts,
                   'original_batch': root_summary, 'recovery_children': child_summaries,
                   'source_task_keys': lineage, 'ready_for_generation': ready,
                   'partial': not ready, 'source_outcomes': outcomes}
        rows = [(Path(paths[item['id']]), resolved[item['id']]) for item in root['files']
                if item['id'] in resolved] if (ready or partial) else []
        return rows, summary
