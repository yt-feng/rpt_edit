"""One synthetic-page MinerU smoke test, run only on reviewed main in Actions."""
from __future__ import annotations
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tempfile

from consume_legacy_mineru import ConsumerError, NetworkStop, download_once, safe_unzip
from mineru_task_ledger import Ledger, LedgerError, Provider, R2Store, encoded, exact_json, validate_s3_model
from mineru_result_cache import ResultCache, ResultCacheError, MAX_RECEIPT

SCOPE = 'mineru-api-smoke'
ENDPOINT = 'https://mineru.net'
OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}
MARKER = 'MINERU_SMOKE_CANARY_V1'
NUMBERS = ('42.75', '125.50', '168.25')
MAX_RESULT = 16 * 1024 * 1024
CACHE_PREFIX = '_workflow-cache/mineru-results/v1/mineru-api-smoke'
CACHE_POLICY = 'complete-synthetic-smoke-result-v1'
WORKFLOW = '.github/workflows/mineru-api-smoke.yml'


class SmokeError(ValueError):
    pass


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def synthetic_pdf():
    from reportlab.pdfgen.canvas import Canvas
    buffer = io.BytesIO()
    canvas = Canvas(buffer, pagesize=(612, 792), invariant=1, pageCompression=0)
    canvas.setTitle('Synthetic MinerU API smoke test')
    canvas.setAuthor('')
    canvas.setCreator('Synthetic API smoke fixture v1')
    canvas.setFont('Helvetica', 16)
    canvas.drawString(54, 730, MARKER)
    canvas.setFont('Helvetica', 12)
    canvas.drawString(54, 697, 'Synthetic research fixture. No personal report or customer data.')
    canvas.drawString(54, 670, 'Known values: revenue 125.50, cost 42.75, combined total 168.25.')
    canvas.drawString(54, 630, 'Item')
    canvas.drawString(300, 630, 'Value')
    for y, (name, value) in zip((603, 576, 549), zip(('Cost', 'Revenue', 'Combined total'), NUMBERS)):
        canvas.drawString(54, y, name)
        canvas.drawString(300, y, value)
    for y in (646, 618, 590, 562, 536):
        canvas.line(50, y, 450, y)
    canvas.line(50, 536, 50, 646)
    canvas.line(285, 536, 285, 646)
    canvas.line(450, 536, 450, 646)
    canvas.showPage()
    canvas.save()
    return buffer.getvalue()


def credentials(env):
    result, seen = [], set()
    for slot in ('MINER_U', 'MINER_U_2', 'MINER_U_3', 'MINER_U_4'):
        value = env.get(slot, '').strip()
        if value and value not in seen:
            seen.add(value)
            result.append((slot, value))
    if not result:
        raise SmokeError('credentials_missing')
    return result


class NoRedirectHTTP:
    """Keep the existing Provider contract without following API/upload redirects."""
    def __init__(self, request):
        self.request = request
    def call(self, method, *args, **kwargs):
        response = self.request(method, *args, allow_redirects=False, **kwargs)
        if 300 <= response.status_code <= 399:
            response.close()
            raise LedgerError('MinerU redirect refused; saved task retained')
        return response
    def post(self, *a, **kw): return self.call('POST', *a, **kw)
    def put(self, *a, **kw): return self.call('PUT', *a, **kw)
    def get(self, *a, **kw): return self.call('GET', *a, **kw)


def verify_markdown(raw):
    try:
        text = raw.decode('utf-8')
    except UnicodeError:
        raise SmokeError('markdown_encoding') from None
    normalized = re.sub(r'[^a-z0-9]', '', text.lower())
    if re.sub(r'[^a-z0-9]', '', MARKER.lower()) not in normalized:
        raise SmokeError('marker_missing')
    if any(not re.search(r'(?<![\d.])' + re.escape(number) + r'(?![\d.])', text) for number in NUMBERS):
        raise SmokeError('numeric_evidence_missing')


def checked_result(raw):
    if not isinstance(raw, bytes) or not 1 <= len(raw) <= MAX_RESULT:
        raise SmokeError('result_size')
    with tempfile.TemporaryDirectory(prefix='mineru-smoke-zip-') as temporary:
        markdown = safe_unzip(raw, Path(temporary) / 'result')
        verify_markdown(markdown)
        return markdown


def checked_authentication(authentication, *, stored=False):
    if authentication is None:
        return None
    from mineru_daily_result_transport import validate_daily_authentication, validate_stored_daily_authentication
    checked = (validate_stored_daily_authentication(authentication) if stored
               else validate_daily_authentication(authentication))
    if checked['workflow_path'] != WORKFLOW:
        raise SmokeError('result_authentication_scope')
    return checked


def result_identity(binding, lineage):
    if (not isinstance(binding, dict) or set(binding) != {'source', 'sha256', 'size', 'scope', 'endpoint', 'options', 'id'}
            or binding['scope'] != SCOPE or binding['endpoint'] != ENDPOINT or not exact_json(binding['options'], OPTIONS)
            or not isinstance(binding['source'], str) or not re.fullmatch(r'mineru-api-smoke-[1-9][0-9]{0,19}\.pdf', binding['source'])
            or type(binding['size']) is not int or binding['size'] < 1
            or not isinstance(binding['sha256'], str) or not re.fullmatch('[a-f0-9]{64}', binding['sha256'])
            or binding['id'] != sha256(encoded({k: v for k, v in binding.items() if k != 'id'}))):
        raise SmokeError('result_cache_source')
    if (not isinstance(lineage, dict) or set(lineage) != {'batch_key', 'batch_id', 'data_id'}
            or not isinstance(lineage['batch_key'], str) or not re.fullmatch('batches/[a-f0-9]{32}', lineage['batch_key'])
            or not isinstance(lineage['batch_id'], str) or not re.fullmatch('[A-Za-z0-9_-]{1,128}', lineage['batch_id'])
            or lineage['data_id'] != binding['id']):
        raise SmokeError('result_cache_task')
    return sha256(encoded({'policy': CACHE_POLICY, 'source_binding': binding, 'lineage': lineage}))


class SmokeResultCache(ResultCache):
    """Use conditional R2 primitives with an isolated synthetic-source contract."""
    @staticmethod
    def receipt_key(identity_sha):
        return f'{CACHE_PREFIX}/{identity_sha}/receipt.json'

    @staticmethod
    def blob_key(identity_sha, zip_sha):
        return f'{CACHE_PREFIX}/{identity_sha}/{zip_sha}.zip'

    def get(self, binding, lineage):
        identity_sha = result_identity(binding, lineage)
        raw = self._read(self.receipt_key(identity_sha), maximum=MAX_RECEIPT, content_type='application/json',
                         identity_sha=identity_sha, allow_missing=True)
        if raw is None:
            return None
        def unique_pairs(pairs):
            value = {}
            for key, item in pairs:
                if key in value:
                    raise SmokeError('result_cache_receipt')
                value[key] = item
            return value
        try:
            receipt = json.loads(raw, object_pairs_hook=unique_pairs)
        except (ValueError, UnicodeError):
            raise SmokeError('result_cache_receipt') from None
        if (not isinstance(receipt, dict) or set(receipt) != {'schema_version', 'policy', 'identity_sha256',
                'source_binding', 'lineage', 'zip_sha256', 'zip_bytes', 'markdown_sha256', 'blob_key', 'authentication'}
                or type(receipt['schema_version']) is not int or receipt['schema_version'] != 1
                or receipt['policy'] != CACHE_POLICY or receipt['identity_sha256'] != identity_sha
                or not exact_json(receipt['source_binding'], binding) or not exact_json(receipt['lineage'], lineage)
                or any(not isinstance(receipt[k], str) or not re.fullmatch('[a-f0-9]{64}', receipt[k])
                       for k in ('zip_sha256', 'markdown_sha256'))
                or type(receipt['zip_bytes']) is not int or not 1 <= receipt['zip_bytes'] <= MAX_RESULT
                or receipt['blob_key'] != self.blob_key(identity_sha, receipt['zip_sha256'])):
            raise SmokeError('result_cache_receipt')
        authentication = checked_authentication(receipt['authentication'], stored=True)
        payload = self._read(receipt['blob_key'], maximum=MAX_RESULT, content_type='application/zip', identity_sha=identity_sha)
        if len(payload) != receipt['zip_bytes'] or sha256(payload) != receipt['zip_sha256']:
            raise SmokeError('result_cache_payload')
        if sha256(checked_result(payload)) != receipt['markdown_sha256']:
            raise SmokeError('result_cache_markdown')
        return payload, authentication

    def put(self, binding, lineage, payload, authentication):
        identity_sha = result_identity(binding, lineage)
        markdown = checked_result(payload)
        authentication = checked_authentication(authentication)
        existing = self.get(binding, lineage)
        if existing is not None:
            if existing[0] != payload:
                raise SmokeError('result_cache_changed')
            return existing
        zip_sha = sha256(payload)
        key = self.blob_key(identity_sha, zip_sha)
        checked_authentication(authentication)
        self._immutable(key, payload, content_type='application/zip', identity_sha=identity_sha, maximum=MAX_RESULT)
        receipt = encoded({'schema_version': 1, 'policy': CACHE_POLICY, 'identity_sha256': identity_sha,
            'source_binding': binding, 'lineage': lineage, 'zip_sha256': zip_sha, 'zip_bytes': len(payload),
            'markdown_sha256': sha256(markdown), 'blob_key': key, 'authentication': authentication})
        checked_authentication(authentication)
        self._immutable(self.receipt_key(identity_sha), receipt, content_type='application/json',
                        identity_sha=identity_sha, maximum=MAX_RECEIPT)
        restored = self.get(binding, lineage)
        if restored is None or restored[0] != payload:
            raise SmokeError('result_cache_readback')
        return restored


def original_lineage(ledger, binding, row):
    claim, _ = ledger.store.get('sources/' + binding['id'])
    if not isinstance(claim, dict) or not exact_json(claim.get('binding'), binding):
        raise SmokeError('result_cache_claim')
    batch, _ = ledger._read_batch(claim.get('batch_key'))
    if ('recovery_parent' in batch or batch.get('state') != 'terminal'
            or not exact_json(batch.get('files'), [binding]) or row.get('data_id') != binding['id']):
        raise SmokeError('result_cache_original_task')
    lineage = {'batch_key': batch['key'], 'batch_id': batch['batch_id'], 'data_id': binding['id']}
    result_identity(binding, lineage)
    return lineage


def restore_result(url, binding, lineage, cache, downloader, result_downloader):
    cached = cache.get(binding, lineage) if cache is not None else None
    if cached is not None:
        return cached[0], cached[1], True
    payload, authentication = (result_downloader(url, strict_downloader=downloader) if result_downloader is not None
                               else (downloader(url), None))
    checked_result(payload)
    authentication = checked_authentication(authentication)
    if cache is not None:
        payload, authentication = cache.put(binding, lineage, payload, authentication)
    return payload, authentication, False


def run_smoke(run_id, store, provider, tokens, *, downloader=download_once, result_downloader=None,
              result_cache=None, clock=None, sleep=None):
    if not isinstance(run_id, str) or not re.fullmatch(r'[1-9][0-9]{0,19}', run_id):
        raise SmokeError('run_identity')
    summary = {'schema_version': 1, 'status': 'failed', 'stage': 'source',
               'authentication': {'configured_slots': len(tokens), 'accepted': None},
               'parse': {'requested': 1, 'completed': 0, 'failed': 0, 'pending': 1},
               'download': {'complete_zip_verified': False, 'bytes': 0},
               'marker_verified': False, 'provider_posts': 0, 'accepted_parse_limit': 1,
               'network_stop': False, 'hashes': {},
               'result_cache': {'enabled': False, 'durable_readback': False, 'initial_hit': False,
                                'replay_hit': False, 'replay_provider_posts': None, 'replay_result_downloads': None}}
    kwargs = {}
    if clock is not None: kwargs['clock'] = clock
    if sleep is not None: kwargs['sleep'] = sleep
    ledger = Ledger(store, provider, SCOPE, ENDPOINT, OPTIONS, tokens, **kwargs)
    replay_ledger = None
    cache = result_cache
    if cache is None and isinstance(store, R2Store):
        cache = SmokeResultCache.single_attempt(store.client, store.bucket)
    summary['result_cache']['enabled'] = cache is not None
    try:
        with tempfile.TemporaryDirectory(prefix='mineru-smoke-private-') as temporary:
            root = Path(temporary)
            source = f'mineru-api-smoke-{run_id}.pdf'
            pdf = root / source
            raw = synthetic_pdf()
            pdf.write_bytes(raw)
            summary['hashes']['pdf_sha256'] = sha256(raw)
            binding = ledger.bind(pdf, source)
            # Independent immutable per-run guard: changed fixture/options cannot
            # create a second accepted task under a different source hash on rerun.
            guard_key = 'sources/' + sha256(('smoke-run-v1:' + run_id).encode())
            guard = {'schema': 1, 'policy': 'single-source-smoke-v1', 'binding': binding}
            saved, version = store.get(guard_key)
            if saved is None:
                store.put(guard_key, guard)
            elif not exact_json(saved, guard) or not version:
                raise SmokeError('run_source_binding_changed')
            summary['stage'] = 'parse'
            rows, task = ledger.run([(pdf, source)], timeout=600, interval=10, queue_budget=180)
            summary['authentication']['accepted'] = True
            summary['parse'] = {key: task[key] for key in ('requested', 'completed', 'failed', 'pending')}
            if not task['ready_for_generation'] or len(rows) != 1:
                summary['status'] = 'pending' if task['pending'] else 'failed'
                return summary
            summary['stage'] = 'download'
            lineage = original_lineage(ledger, binding, rows[0][1]) if cache is not None else None
            zipped, authentication, cache_hit = restore_result(rows[0][1]['full_zip_url'], binding, lineage,
                                                               cache, downloader, result_downloader)
            markdown = checked_result(zipped)
            summary['download'] = {'complete_zip_verified': True, 'bytes': len(zipped)}
            summary['hashes'].update(zip_sha256=sha256(zipped), markdown_sha256=sha256(markdown))
            summary['stage'] = 'marker'
            summary['result_authentication'] = authentication or {'auth_mode': 'normal_pki', 'pki_verified_now': True}
            if cache is not None:
                summary['stage'] = 'cache_replay'
                summary['result_cache'].update(durable_readback=True, initial_hit=cache_hit)
                replay_ledger = Ledger(store, provider, SCOPE, ENDPOINT, OPTIONS, tokens, **kwargs)
                again, replay_task = replay_ledger.run([(pdf, source)], timeout=120, interval=10, queue_budget=60)
                if (not replay_task['ready_for_generation'] or len(again) != 1 or replay_ledger.submission_posts != 0
                        or not exact_json(original_lineage(replay_ledger, binding, again[0][1]), lineage)):
                    raise SmokeError('result_cache_replay_task')
                replay_downloads = []
                def forbidden_download(*args, **kwargs):
                    replay_downloads.append(True)
                    raise SmokeError('result_cache_replay_download')
                restored, stored_auth, hit = restore_result(again[0][1]['full_zip_url'], binding, lineage, cache,
                    forbidden_download, forbidden_download)
                if (not hit or restored != zipped or not exact_json(stored_auth, authentication)
                        or checked_result(restored) != markdown):
                    raise SmokeError('result_cache_replay_mismatch')
                summary['result_cache'].update(replay_hit=True, replay_provider_posts=replay_ledger.submission_posts,
                                               replay_result_downloads=len(replay_downloads))
            summary.update(status='passed', stage='complete', marker_verified=True)
    except NetworkStop as error:
        category = 'tls_certificate_expired' if str(error) == 'tls_certificate_expired' else 'result_network_stop'
        summary.update(category=category, network_stop=True)
    except ConsumerError as error:
        # Consumer helpers use fixed categories; never include URLs/provider text.
        allowed = {'result_http', 'result_url', 'timeout', 'zip_size', 'zip_member_count',
                   'zip_path', 'zip_expansion', 'zip_integrity', 'markdown_ambiguous',
                   'markdown_size', 'markdown_empty', 'markdown_encoding'}
        summary['category'] = str(error) if str(error) in allowed else 'result_contract'
    except SmokeError as error:
        summary['category'] = str(error)
    except ResultCacheError:
        summary['category'] = 'result_cache_contract'
    except LedgerError as error:
        summary['category'] = 'durable_task_stopped'
        if str(error).startswith('All configured MinerU credentials were definitively rejected;'):
            summary['authentication']['accepted'] = False
            summary['category'] = 'authentication_rejected'
        elif 'transport outcome unknown; saved task retained' in str(error):
            summary['network_stop'] = True
    except Exception as error:
        summary.update(category='smoke_stopped', exception_class=type(error).__name__)
    finally:
        summary['provider_posts'] = ledger.submission_posts + (replay_ledger.submission_posts if replay_ledger is not None else 0)
    return summary


def cloud_store(env):
    import boto3
    from botocore.config import Config
    required = ('R2_ACCOUNT_ID', 'R2_ACCESS_KEY_ID', 'R2_SECRET_ACCESS_KEY', 'R2_BUCKET')
    if any(not env.get(key, '').strip() for key in required):
        raise SmokeError('private_store_configuration')
    client = boto3.client('s3', endpoint_url=f"https://{env['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
                          aws_access_key_id=env['R2_ACCESS_KEY_ID'], aws_secret_access_key=env['R2_SECRET_ACCESS_KEY'],
                          region_name='auto', config=Config(retries={'total_max_attempts': 1, 'mode': 'standard'},
                                                          connect_timeout=10, read_timeout=30))
    validate_s3_model(client.meta.service_model)
    return R2Store(SCOPE, client=client, bucket=env['R2_BUCKET'])


def main():
    env = os.environ
    expected = env.get('GITHUB_REPOSITORY', '') + '/.github/workflows/mineru-api-smoke.yml@refs/heads/main'
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_REF') != 'refs/heads/main'
            or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch' or env.get('GITHUB_WORKFLOW_REF') != expected):
        raise SystemExit('Reviewed main cloud smoke workflow required')
    try:
        import requests
        from mineru_daily_result_transport import download_result
        result = run_smoke(env.get('GITHUB_RUN_ID'), cloud_store(env), Provider(NoRedirectHTTP(requests.request), ENDPOINT),
                           credentials(env), result_downloader=download_result)
    except Exception as error:
        result = {'schema_version': 1, 'status': 'failed', 'stage': 'configuration',
                  'exception_class': type(error).__name__, 'provider_posts': 0, 'marker_verified': False}
    output = Path(env['RUNNER_TEMP']) / 'mineru-api-smoke-summary.json'
    output.write_text(json.dumps(result, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, sort_keys=True))
    return 0 if result['status'] == 'passed' else 75 if result['status'] == 'pending' else 2


if __name__ == '__main__':
    raise SystemExit(main())
