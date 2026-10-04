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
from mineru_task_ledger import Ledger, LedgerError, Provider, R2Store, exact_json, validate_s3_model

SCOPE = 'mineru-api-smoke'
ENDPOINT = 'https://mineru.net'
OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}
MARKER = 'MINERU_SMOKE_CANARY_V1'
NUMBERS = ('42.75', '125.50', '168.25')
MAX_RESULT = 16 * 1024 * 1024


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


def run_smoke(run_id, store, provider, tokens, *, downloader=download_once, clock=None, sleep=None):
    if not isinstance(run_id, str) or not re.fullmatch(r'[1-9][0-9]{0,19}', run_id):
        raise SmokeError('run_identity')
    summary = {'schema_version': 1, 'status': 'failed', 'stage': 'source',
               'authentication': {'configured_slots': len(tokens), 'accepted': None},
               'parse': {'requested': 1, 'completed': 0, 'failed': 0, 'pending': 1},
               'download': {'complete_zip_verified': False, 'bytes': 0},
               'marker_verified': False, 'provider_posts': 0, 'accepted_parse_limit': 1,
               'network_stop': False, 'hashes': {}}
    kwargs = {}
    if clock is not None: kwargs['clock'] = clock
    if sleep is not None: kwargs['sleep'] = sleep
    ledger = Ledger(store, provider, SCOPE, ENDPOINT, OPTIONS, tokens, **kwargs)
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
            zipped = downloader(rows[0][1]['full_zip_url'])
            if not isinstance(zipped, bytes) or not 1 <= len(zipped) <= MAX_RESULT:
                raise SmokeError('result_size')
            markdown = safe_unzip(zipped, root / 'result')
            summary['download'] = {'complete_zip_verified': True, 'bytes': len(zipped)}
            summary['hashes'].update(zip_sha256=sha256(zipped), markdown_sha256=sha256(markdown))
            summary['stage'] = 'marker'
            verify_markdown(markdown)
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
        summary['provider_posts'] = ledger.submission_posts
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
        result = run_smoke(env.get('GITHUB_RUN_ID'), cloud_store(env), Provider(NoRedirectHTTP(requests.request), ENDPOINT), credentials(env))
    except Exception as error:
        result = {'schema_version': 1, 'status': 'failed', 'stage': 'configuration',
                  'exception_class': type(error).__name__, 'provider_posts': 0, 'marker_verified': False}
    output = Path(env['RUNNER_TEMP']) / 'mineru-api-smoke-summary.json'
    output.write_text(json.dumps(result, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, sort_keys=True))
    return 0 if result['status'] == 'passed' else 75 if result['status'] == 'pending' else 2


if __name__ == '__main__':
    raise SystemExit(main())
