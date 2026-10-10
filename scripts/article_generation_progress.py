"""Durable private body/title results; ambiguous requests are never resubmitted."""
from __future__ import annotations

from contextlib import contextmanager
import copy
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

RECEIPT = 'article_generation_progress.json'
POLICY = 'durable-article-generation-v1'
MAX_TITLES = 4
MAX_STATE_BYTES = 256 * 1024
MAX_RESPONSE_BYTES = 4 * 1024 * 1024
MAX_PROMPT_BYTES = 2 * 1024 * 1024
RESPONSE_PREFIX = 'article_generation_response_'
HASH = re.compile(r'[a-f0-9]{64}')


class ProgressError(ValueError):
    """Only fixed categories, never provider text or private paths."""
    def __init__(self, category):
        self.category = category
        super().__init__(category)


def require(condition, code):
    if not condition:
        raise ProgressError(code)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    try:
        return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':'), allow_nan=False).encode()
    except (TypeError, ValueError, UnicodeError, RecursionError):
        raise ProgressError('article_progress_json_invalid') from None


def decoded(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'article_progress_json_invalid')
            result[key] = value
        return result
    try:
        return json.loads(raw, object_pairs_hook=pairs,
                          parse_constant=lambda _: require(False, 'article_progress_json_invalid'))
    except (ValueError, UnicodeError, RecursionError):
        raise ProgressError('article_progress_json_invalid') from None


def dictionary(value, limit):
    require(isinstance(value, dict) and all(isinstance(key, str) for key in value),
            'article_progress_dictionary_invalid')
    raw = encoded(value)
    require(len(raw) <= limit, 'article_progress_dictionary_oversized')
    return decoded(raw)


def response_bytes(value):
    require(isinstance(value, str) and bool(value.strip()), 'article_progress_response_invalid')
    try:
        raw = value.encode('utf-8')
    except UnicodeError:
        raise ProgressError('article_progress_response_invalid') from None
    require(len(raw) <= MAX_RESPONSE_BYTES, 'article_progress_response_oversized')
    return raw


def request_id(kind, prompt_sha, options_sha):
    return digest(encoded({'kind': kind, 'prompt_sha256': prompt_sha, 'options_sha256': options_sha}))


class Progress:
    def __init__(self, directory, *, identity, persist):
        self.directory = Path(directory)
        require(not self.directory.is_symlink(), 'article_progress_directory_invalid')
        try:
            self.directory.mkdir(parents=True, exist_ok=True)
        except OSError:
            raise ProgressError('article_progress_directory_invalid') from None
        require(self.directory.is_dir(), 'article_progress_directory_invalid')
        self.identity = dictionary(identity, 64 * 1024)
        require(bool(self.identity) and callable(persist), 'article_progress_identity_invalid')
        self.persist = persist
        self.path = self.directory / RECEIPT
        with self._locked():
            self._load()

    @contextmanager
    def _locked(self):
        path = self.directory / '.article_generation_progress.lock'
        require(not path.is_symlink(), 'article_progress_lock_invalid')
        try:
            fd = os.open(path, os.O_RDWR | os.O_CREAT | getattr(os, 'O_NOFOLLOW', 0), 0o600)
        except OSError:
            raise ProgressError('article_progress_lock_invalid') from None
        with os.fdopen(fd, 'a+b') as stream:
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)

    def _atomic(self, path, raw):
        require(not path.is_symlink(), 'article_progress_file_invalid')
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(prefix='.article-progress-', dir=self.directory, delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(path)
        except OSError:
            raise ProgressError('article_progress_write_failed') from None
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)

    def _write(self, state):
        raw = encoded(state)
        require(len(raw) <= MAX_STATE_BYTES, 'article_progress_state_oversized')
        self._atomic(self.path, raw + b'\n')

    def _persist(self):
        require(self.persist() is not False, 'article_progress_persistence_rejected')

    def _response(self, entry):
        path = self.directory / entry['response_path']
        require(path.is_file() and not path.is_symlink()
                and path.stat().st_size == entry['response_bytes'], 'article_progress_response_changed')
        raw = path.read_bytes()
        require(digest(raw) == entry['response_sha256'], 'article_progress_response_changed')
        try:
            value = raw.decode('utf-8')
        except UnicodeError:
            raise ProgressError('article_progress_response_changed') from None
        response_bytes(value)
        return value

    def _load(self):
        require(not self.path.is_symlink(), 'article_progress_file_invalid')
        if not self.path.exists():
            require(not list(self.directory.glob(RESPONSE_PREFIX + '*')), 'article_progress_state_missing')
            return {'schema_version': 1, 'policy': POLICY, 'identity': copy.deepcopy(self.identity), 'requests': []}
        require(self.path.is_file() and 0 < self.path.stat().st_size <= MAX_STATE_BYTES,
                'article_progress_state_invalid')
        state = decoded(self.path.read_bytes())
        require(isinstance(state, dict) and set(state) == {'schema_version', 'policy', 'identity', 'requests'}
                and type(state['schema_version']) is int and state['schema_version'] == 1
                and state['policy'] == POLICY and encoded(state['identity']) == encoded(self.identity),
                'article_progress_identity_mismatch')
        entries = state['requests']
        require(isinstance(entries, list) and len(entries) <= MAX_TITLES + 1, 'article_progress_state_invalid')
        ids, body, titles, pending = set(), 0, 0, 0
        keys = {'id', 'kind', 'origin', 'prompt_sha256', 'options_sha256', 'state',
                'response_path', 'response_sha256', 'response_bytes', 'proof'}
        for index, entry in enumerate(entries):
            require(isinstance(entry, dict) and set(entry) == keys
                    and isinstance(entry['kind'], str) and entry['kind'] in {'body', 'title'}
                    and isinstance(entry['origin'], str) and entry['origin'] in {'request', 'legacy'}
                    and isinstance(entry['id'], str) and HASH.fullmatch(entry['id'])
                    and entry['id'] not in ids and isinstance(entry['state'], str) and entry['state'] in {'pending', 'complete'},
                    'article_progress_state_invalid')
            ids.add(entry['id'])
            if entry['kind'] == 'body':
                body += 1
                require(index == 0 and body == 1, 'article_progress_body_mismatch')
            else:
                titles += 1
                require(body == 1 and entries[0]['state'] == 'complete' and titles <= MAX_TITLES,
                        'article_progress_title_budget')
            if entry['origin'] == 'legacy':
                proof = dictionary(entry['proof'], 64 * 1024)
                require(entry['kind'] == 'body' and bool(proof) and entry['state'] == 'complete'
                        and entry['prompt_sha256'] is None and entry['options_sha256'] is None
                        and entry['id'] == digest(encoded({'kind': 'legacy-body', 'body_sha256': entry['response_sha256'],
                                                          'proof_sha256': digest(encoded(proof))})),
                        'article_progress_legacy_invalid')
            else:
                require(entry['proof'] is None and all(isinstance(entry[key], str) and HASH.fullmatch(entry[key])
                        for key in ('prompt_sha256', 'options_sha256'))
                        and entry['id'] == request_id(entry['kind'], entry['prompt_sha256'], entry['options_sha256']),
                        'article_progress_request_mismatch')
            require(entry['response_path'] == RESPONSE_PREFIX + entry['id'] + '.txt', 'article_progress_response_changed')
            if entry['state'] == 'pending':
                pending += 1
                require(pending == 1 and index == len(entries) - 1 and entry['response_sha256'] is None
                        and entry['response_bytes'] is None, 'article_progress_pending_invalid')
            else:
                require(isinstance(entry['response_sha256'], str) and HASH.fullmatch(entry['response_sha256'])
                        and type(entry['response_bytes']) is int and 0 < entry['response_bytes'] <= MAX_RESPONSE_BYTES,
                        'article_progress_response_changed')
                self._response(entry)
        require({path.name for path in self.directory.glob(RESPONSE_PREFIX + '*')}
                <= {entry['response_path'] for entry in entries}, 'article_progress_response_unbound')
        return state

    def saved_body(self):
        with self._locked():
            state = self._load()
            if not state['requests']:
                return None
            body = state['requests'][0]
            require(body['state'] == 'complete', 'article_progress_pending')
            return self._response(body)

    def request(self, kind, prompt, options, call):
        require(isinstance(kind, str) and kind in {'body', 'title'} and isinstance(prompt, str) and callable(call),
                'article_progress_request_invalid')
        try:
            raw_prompt = prompt.encode('utf-8')
        except UnicodeError:
            raise ProgressError('article_progress_request_invalid') from None
        require(0 < len(raw_prompt) <= MAX_PROMPT_BYTES, 'article_progress_prompt_invalid')
        options = dictionary(options, 64 * 1024)
        prompt_sha, options_sha = digest(raw_prompt), digest(encoded(options))
        identity = request_id(kind, prompt_sha, options_sha)
        with self._locked():
            state = self._load()
            matching = [entry for entry in state['requests'] if entry['id'] == identity]
            if matching:
                require(matching[0]['state'] == 'complete', 'article_progress_pending')
                return self._response(matching[0])
            require(not any(entry['state'] == 'pending' for entry in state['requests']), 'article_progress_pending')
            if kind == 'body':
                require(not state['requests'], 'article_progress_body_mismatch')
            else:
                require(state['requests'] and state['requests'][0]['kind'] == 'body', 'article_progress_body_missing')
                require(sum(entry['kind'] == 'title' for entry in state['requests']) < MAX_TITLES,
                        'article_progress_title_budget')
            entry = {'id': identity, 'kind': kind, 'origin': 'request', 'prompt_sha256': prompt_sha,
                     'options_sha256': options_sha, 'state': 'pending', 'response_path': RESPONSE_PREFIX + identity + '.txt',
                     'response_sha256': None, 'response_bytes': None, 'proof': None}
            state['requests'].append(entry)
            self._write(state)
            try:
                self._persist()
            except Exception as error:
                raise ProgressError('article_progress_intent_persistence_failed') from error
            try:
                raw = response_bytes(call())
            except Exception as error:
                raise ProgressError('article_progress_request_pending') from error
            self._atomic(self.directory / entry['response_path'], raw)
            pending = copy.deepcopy(state)
            entry.update(state='complete', response_sha256=digest(raw), response_bytes=len(raw))
            self._write(state)
            try:
                self._persist()
            except Exception as error:
                self._write(pending)
                raise ProgressError('article_progress_result_persistence_failed') from error
            return raw.decode('utf-8')

    def seed_body(self, body, *, proof):
        """Caller must authenticate legacy bytes/proof before invoking this API."""
        raw = response_bytes(body)
        proof = dictionary(proof, 64 * 1024)
        require(bool(proof), 'article_progress_legacy_invalid')
        identity = digest(encoded({'kind': 'legacy-body', 'body_sha256': digest(raw), 'proof_sha256': digest(encoded(proof))}))
        with self._locked():
            state = self._load()
            if state['requests']:
                entry = state['requests'][0]
                require(entry['origin'] == 'legacy' and entry['id'] == identity and entry['state'] == 'complete'
                        and encoded(entry['proof']) == encoded(proof) and self._response(entry) == body,
                        'article_progress_legacy_mismatch')
                return
            entry = {'id': identity, 'kind': 'body', 'origin': 'legacy', 'prompt_sha256': None,
                     'options_sha256': None, 'state': 'complete', 'response_path': RESPONSE_PREFIX + identity + '.txt',
                     'response_sha256': digest(raw), 'response_bytes': len(raw), 'proof': proof}
            self._atomic(self.directory / entry['response_path'], raw)
            state['requests'].append(entry)
            self._write(state)
            try:
                self._persist()
            except Exception as error:
                # Seeding submits nothing; preserve exact local proof/result for
                # the caller to persist explicitly before any title submission.
                raise ProgressError('article_progress_legacy_persistence_failed') from error
