"""Authenticate old Actions evidence and preserve complete legacy output privately.

Runs only in reviewed main workflows. Every remote read/write has one attempt;
provider result ZIPs remain on the cloud runner and private R2. No PDF/source
hash is invented and canonical MinerU admission is never modified.
"""
from __future__ import annotations
import argparse
import base64
import io
import http.client
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import urllib.error
import urllib.request
import zipfile

import consume_legacy_mineru as consumer
from inspect_legacy_mineru import canonical
from persist_legacy_mineru_inspection import PREFIX as INSPECTION_PREFIX, single_attempt_store
from portal_extended_r2 import R2NotFound, R2Store, R2TransportError

REPOSITORY = 'yt-feng/rpt_edit'
WORKFLOW = '.github/workflows/mineru-legacy-consume.yml'
PREFIX = '_workflow-cache/mineru-legacy-outputs/v1'
MAX_ARTIFACT = 16 * 1024 * 1024
MAX_FILE = 128 * 1024 * 1024
MAX_TOTAL = 1024 * 1024 * 1024
# These two exact old source implementations establish the copied-filename and
# retry-group contract; a different producer implementation requires review.
ORIGINAL_CODE = {
    'scripts/run_pdf_to_xhs_in_batches.py': 'f0c32f8939e7f2cc9ed62ee15933b94204c1e23f66c2902162975f4ad6ecf5a5',
    'scripts/pdf_to_xhs_batch.py': '0b4335b767ea78e21cf8093b728b38d75637ccda2f906753dc34690c6f744c38',
}


def request(value):
    keys = {'run_id', 'job_id', 'artifact_id', 'artifact_digest',
            'inspection_receipt_sha256', 'inspection_input_sha256', 'inspection_producer'}
    if (not isinstance(value, dict) or set(value) != keys
        or any(not isinstance(value[k], str) or not consumer.DECIMAL_ID.fullmatch(value[k])
               for k in ('run_id', 'job_id', 'artifact_id'))
        or any(not isinstance(value[k], str) or not consumer.SHA.fullmatch(value[k])
               for k in ('artifact_digest', 'inspection_receipt_sha256', 'inspection_input_sha256'))):
        consumer.fail('recovery_request')
    producer = value['inspection_producer']
    if (not isinstance(producer, dict) or set(producer) != {'run_id', 'attempt', 'sha'}
        or any(not isinstance(producer[k], str) or not consumer.DECIMAL_ID.fullmatch(producer[k])
               for k in ('run_id', 'attempt'))
        or not isinstance(producer['sha'], str) or not re.fullmatch(r'[a-f0-9]{40}', producer['sha'])):
        consumer.fail('recovery_request')
    return value


def read_response(response, maximum):
    chunks = []; size = 0
    length = response.headers.get('Content-Length')
    if length is not None and (not re.fullmatch(r'[0-9]{1,12}', length) or int(length) > maximum):
        consumer.fail('github_size')
    while True:
        chunk = response.read(min(65536, maximum + 1 - size))
        if not chunk: break
        chunks.append(chunk); size += len(chunk)
        if size > maximum: consumer.fail('github_size')
    if length is not None and size != int(length): raise consumer.NetworkStop('network_stop')
    return b''.join(chunks)


class Github:
    def __init__(self, token):
        if not token: consumer.fail('github_credentials')
        self.token = token
        self.opener = urllib.request.build_opener(consumer.NoRedirect)

    def raw(self, endpoint, maximum, *, redirect=False):
        if not endpoint.startswith(f'repos/{REPOSITORY}/') or any(c in endpoint for c in ('\\', '#', '\n')):
            consumer.fail('github_endpoint')
        req = urllib.request.Request('https://api.github.com/'+endpoint,
            headers={'Authorization': 'Bearer '+self.token, 'Accept': 'application/vnd.github+json',
                     'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'rpt-legacy-recovery'}, method='GET')
        try:
            with self.opener.open(req, timeout=30) as response:
                if response.status != 200: consumer.fail('github_http')
                return read_response(response, maximum)
        except urllib.error.HTTPError as error:
            if redirect and error.code == 302:
                url = error.headers.get('Location', ''); error.close(); consumer.valid_url(url)
                # Signed Actions storage URL receives no GitHub token and is
                # allowed exactly one GET without subsequent redirects.
                try:
                    with self.opener.open(urllib.request.Request(url, method='GET'), timeout=30) as response:
                        if response.status != 200: consumer.fail('github_archive_http')
                        return read_response(response, maximum)
                except urllib.error.HTTPError: consumer.fail('github_archive_http')
                except (urllib.error.URLError, OSError, TimeoutError, http.client.HTTPException): raise consumer.NetworkStop('network_stop') from None
            error.close(); consumer.fail('github_http')
        except (urllib.error.URLError, OSError, TimeoutError, http.client.HTTPException): raise consumer.NetworkStop('network_stop') from None

    def get(self, endpoint): return consumer.decode(self.raw(endpoint, MAX_ARTIFACT), MAX_ARTIFACT)


def check_run(run, identity, path, *, sha=None, attempt=None):
    if (not isinstance(run, dict) or str(run.get('id')) != identity
        or run.get('repository', {}).get('full_name') != REPOSITORY
        or run.get('head_repository', {}).get('full_name') != REPOSITORY
        or run.get('head_branch') != 'main' or run.get('path') != path
        or run.get('status') != 'completed' or run.get('event') not in {'schedule', 'workflow_dispatch'}
        or (sha is not None and run.get('head_sha') != sha)
        or (attempt is not None and str(run.get('run_attempt')) != attempt)):
        consumer.fail('github_origin')


def manifest_member(raw):
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            infos = archive.infolist()
            if not infos or len(infos) > 20 or sum(i.file_size for i in infos) > MAX_ARTIFACT:
                consumer.fail('manifest_archive')
            names = set(); selected = []
            for info in infos:
                name = info.orig_filename; path = PurePosixPath(name)
                if (path.is_absolute() or '\\' in name or ':' in name or any(ord(c)<32 for c in name)
                    or any(p in {'', '.', '..'} for p in name.rstrip('/').split('/'))
                    or name.casefold() in names or info.flag_bits & 1
                    or info.file_size > MAX_ARTIFACT or info.file_size > max(1, info.compress_size)*1000
                    or ((info.external_attr >> 16) & 0o170000) not in (0, 0o100000, 0o040000)):
                    consumer.fail('manifest_archive')
                names.add(name.casefold())
                if not info.is_dir():
                    payload = archive.read(info)  # validates CRC for every member
                    if path.name == 'institution_run_manifest.json': selected.append(payload)
            if len(selected) != 1: consumer.fail('manifest_archive')
            return selected[0]
    except (zipfile.BadZipFile, RuntimeError, OSError): consumer.fail('manifest_archive')


def authenticate(api, value, receipt_raw):
    value = request(value); p = value['inspection_producer']
    inspection = consumer.decode(receipt_raw, 256*1024)
    if (consumer.digest(receipt_raw) != value['inspection_receipt_sha256']
        or inspection.get('producer') != p
        or inspection.get('input_canonical_sha256') != value['inspection_input_sha256']):
        consumer.fail('inspection_identity')
    producer = api.get(f'repos/{REPOSITORY}/actions/runs/{p["run_id"]}/attempts/{p["attempt"]}')
    check_run(producer, p['run_id'], '.github/workflows/mineru-legacy-inspect.yml', sha=p['sha'], attempt=p['attempt'])
    if producer.get('conclusion') != 'success': consumer.fail('inspection_producer')
    run = api.get(f'repos/{REPOSITORY}/actions/runs/{value["run_id"]}')
    check_run(run, value['run_id'], consumer.WORKFLOW)
    job = api.get(f'repos/{REPOSITORY}/actions/jobs/{value["job_id"]}')
    if (str(job.get('id')) != value['job_id'] or str(job.get('run_id')) != value['run_id']
        or job.get('name') != 'fetch-and-build' or job.get('status') != 'completed'
        or job.get('conclusion') not in {'failure', 'cancelled'}): consumer.fail('original_job')
    log = api.raw(f'repos/{REPOSITORY}/actions/jobs/{value["job_id"]}/logs', consumer.MAX_LOG, redirect=True)
    lines = log.decode('utf-8').splitlines()
    reset = [re.search(r'HEAD is now at ([a-f0-9]{7,40})\b', x) for x in lines]
    reset = [x[1] for x in reset if x]
    if len(reset) != 1: consumer.fail('execution_source')
    commit = api.get(f'repos/{REPOSITORY}/commits/{reset[0]}'); sha = commit.get('sha')
    if not isinstance(sha, str) or not re.fullmatch(r'[a-f0-9]{40}', sha) or not sha.startswith(reset[0]):
        consumer.fail('execution_source')
    code_hashes = {}
    for path, expected in ORIGINAL_CODE.items():
        source = api.get(f'repos/{REPOSITORY}/contents/{path}?ref={sha}')
        if source.get('encoding') != 'base64' or source.get('path') != path: consumer.fail('execution_code')
        raw = base64.b64decode(source['content'], validate=False)
        code_hashes[path] = consumer.digest(raw)
        if code_hashes[path] != expected: consumer.fail('execution_code')
    artifact = api.get(f'repos/{REPOSITORY}/actions/artifacts/{value["artifact_id"]}')
    if (str(artifact.get('id')) != value['artifact_id'] or artifact.get('expired') is not False
        or str(artifact.get('workflow_run', {}).get('id')) != value['run_id']
        or artifact.get('digest') != 'sha256:'+value['artifact_digest']
        or type(artifact.get('size_in_bytes')) is not int or not 1 <= artifact['size_in_bytes'] <= MAX_ARTIFACT):
        consumer.fail('manifest_artifact')
    archive = api.raw(f'repos/{REPOSITORY}/actions/artifacts/{value["artifact_id"]}/zip', MAX_ARTIFACT, redirect=True)
    if consumer.digest(archive) != value['artifact_digest'] or len(archive) != artifact['size_in_bytes']:
        consumer.fail('manifest_artifact_digest')
    manifest = manifest_member(archive)
    context = {'schema_version': 1, 'repository': REPOSITORY, 'workflow_path': consumer.WORKFLOW,
        'run_id': value['run_id'], 'job_id': value['job_id'], 'execution_source_sha': sha,
        'job_log_sha256': consumer.digest(log), 'manifest_sha256': consumer.digest(manifest),
        'inspection_receipt_sha256': value['inspection_receipt_sha256']}
    authority = {'original_run_head_sha': run['head_sha'], 'execution_code_sha256': code_hashes,
        'manifest_artifact_id': value['artifact_id'], 'manifest_artifact_zip_sha256': value['artifact_digest'],
        'inspection_producer': p, 'original_context': context}
    return log, manifest, context, authority


def output_store(store): return R2Store(store.client, store.bucket, PREFIX)


def check_ready(ready, value, receipt):
    producer=ready.get('producer');authority=ready.get('authority');context=receipt.get('context')
    if (not isinstance(producer,dict) or set(producer)!={'run_id','attempt','sha'}
        or any(not isinstance(producer[k],str) or not consumer.DECIMAL_ID.fullmatch(producer[k])
               for k in ('run_id','attempt'))
        or not isinstance(producer['sha'],str) or not re.fullmatch(r'[a-f0-9]{40}',producer['sha'])
        or not isinstance(authority,dict) or set(authority)!={'original_run_head_sha','execution_code_sha256',
            'manifest_artifact_id','manifest_artifact_zip_sha256','inspection_producer','original_context'}
        or not isinstance(authority['original_run_head_sha'],str)
        or not re.fullmatch(r'[a-f0-9]{40}',authority['original_run_head_sha'])
        or authority['execution_code_sha256']!=ORIGINAL_CODE
        or authority['manifest_artifact_id']!=value['artifact_id']
        or authority['manifest_artifact_zip_sha256']!=value['artifact_digest']
        or authority['inspection_producer']!=value['inspection_producer']
        or authority['original_context']!=context or not isinstance(context,dict)
        or context.get('run_id')!=value['run_id'] or context.get('job_id')!=value['job_id']
        or context.get('inspection_receipt_sha256')!=value['inspection_receipt_sha256']):
        consumer.fail('ready_authority')


def immutable(store, key, raw, *, maximum=MAX_FILE):
    try: old = store._get(key, maximum=maximum)
    except R2NotFound: old = None
    if old is not None:
        if old != raw: consumer.fail('immutable_output_differs')
        return
    store._put(key, raw, metadata={'kind': 'legacy-source-only-private-output'})
    if store._get(key, maximum=maximum) != raw: consumer.fail('output_readback')


def preserve(store, value, root, authority, owner):
    receipt_raw = (root/'_legacy_output_receipt.json').read_bytes()
    consumer.verify_materialized_output(root, receipt_raw)
    receipt = consumer.decode(receipt_raw, MAX_ARTIFACT)
    identity = consumer.digest(canonical(value)); total = 0
    ready = {'schema_version': 1, 'policy': 'authenticated-legacy-source-ready-v1', 'request': value,
        'producer': owner, 'authority': authority, 'source_receipt_sha256': consumer.digest(receipt_raw),
        'original_source_bytes_proven': False, 'canonical_task_admission': False}
    check_ready(ready,value,receipt)
    if any(row['bytes']>MAX_FILE for row in receipt['files']) or sum(row['bytes'] for row in receipt['files'])>MAX_TOTAL:
        consumer.fail('output_size')
    for row in receipt['files']:
        body = (root/row['path']).read_bytes(); total += len(body)
        if total > MAX_TOTAL or len(body)>MAX_FILE: consumer.fail('output_size')
        immutable(store, store.key(identity, 'files', row['sha256']), body)
    checksum = consumer.digest(receipt_raw)
    immutable(store, store.key(identity, 'source-receipt-'+checksum+'.json'), receipt_raw, maximum=MAX_ARTIFACT)
    immutable(store, store.key(identity, 'ready.json'), canonical(ready), maximum=MAX_ARTIFACT)
    return ready


def restore(store, value, destination):
    identity = consumer.digest(canonical(request(value)))
    ready = consumer.decode(store._get(store.key(identity, 'ready.json'), maximum=MAX_ARTIFACT), MAX_ARTIFACT)
    if (set(ready) != {'schema_version','policy','request','producer','authority','source_receipt_sha256',
                      'original_source_bytes_proven','canonical_task_admission'}
        or ready['schema_version'] != 1 or ready['policy'] != 'authenticated-legacy-source-ready-v1'
        or ready['request'] != value or any(ready[k] is not False for k in
            ('original_source_bytes_proven','canonical_task_admission'))
        or not consumer.SHA.fullmatch(str(ready['source_receipt_sha256']))): consumer.fail('ready_contract')
    raw = store._get(store.key(identity, 'source-receipt-'+ready['source_receipt_sha256']+'.json'), maximum=MAX_ARTIFACT)
    if consumer.digest(raw) != ready['source_receipt_sha256']: consumer.fail('ready_receipt_hash')
    receipt = consumer.decode(raw, MAX_ARTIFACT)
    check_ready(ready,value,receipt)
    # File paths are checked before any directories are created. The final
    # verifier also rejects extra files, symlinks and inconsistent provenance.
    files = receipt.get('files'); total = 0
    if not isinstance(files, list) or not 1 <= len(files)<=10000: consumer.fail('output_files')
    destination = Path(destination)
    if destination.exists() or destination.is_symlink(): consumer.fail('destination_exists')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.legacy-restore-', dir=destination.parent) as tmp:
        stage = Path(tmp)/'source'; stage.mkdir()
        for row in files:
            if not isinstance(row,dict) or set(row)!={'path','sha256','bytes'}: consumer.fail('output_files')
            relative=row['path']; path=PurePosixPath(relative) if isinstance(relative,str) else PurePosixPath('/')
            if (path.is_absolute() or path.as_posix()!=relative or '\\' in relative or ':' in relative
                or any(p in {'','.','..'} for p in relative.split('/'))
                or not consumer.SHA.fullmatch(str(row['sha256'])) or type(row['bytes']) is not int
                or not 0<=row['bytes']<=MAX_FILE): consumer.fail('output_files')
            total += row['bytes']
            if total>MAX_TOTAL: consumer.fail('output_size')
            body=store._get(store.key(identity,'files',row['sha256']),maximum=MAX_FILE)
            if len(body)!=row['bytes'] or consumer.digest(body)!=row['sha256']: consumer.fail('output_file_hash')
            target=stage/relative; target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(body)
        (stage/'_legacy_output_receipt.json').write_bytes(raw)
        consumer.verify_materialized_output(stage,raw)
        os.replace(stage,destination)
    return ready, receipt


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['recover','restore-output'])
    parser.add_argument('--request',required=True);parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--github-output',type=Path);args=parser.parse_args()
    allowed=WORKFLOW if args.operation=='recover' else consumer.WORKFLOW
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REF')!='refs/heads/main'
        or os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY or os.environ.get('GITHUB_EVENT_NAME')!='workflow_dispatch'
        or os.environ.get('GITHUB_WORKFLOW_REF')!=REPOSITORY+'/'+allowed+'@refs/heads/main'):
        consumer.fail('main_workflow_required')
    value=request(consumer.decode(args.request.encode(),65536)); api=Github(os.environ.get('GITHUB_TOKEN'))
    inspection_store=single_attempt_store(); store=output_store(inspection_store)
    identity=consumer.digest(canonical(value))
    try:
        ready, receipt=restore(store,value,args.output)
        p=ready['producer']
        producer=api.get(f'repos/{REPOSITORY}/actions/runs/{p["run_id"]}/attempts/{p["attempt"]}')
        # The producer may be this still-running recovery job on a resumed tail;
        # downstream consumers require a completed successful exact attempt.
        same_owner=all(p[k]==os.environ.get(v) for k,v in
            {'run_id':'GITHUB_RUN_ID','attempt':'GITHUB_RUN_ATTEMPT','sha':'GITHUB_SHA'}.items())
        if args.operation=='restore-output' or not same_owner:
            check_run(producer,p['run_id'],WORKFLOW,sha=p['sha'],attempt=p['attempt'])
            if producer.get('conclusion')!='success':consumer.fail('output_producer')
        resumed=True
    except R2NotFound:
        if args.operation!='recover':raise
        p=value['inspection_producer']
        receipt_key=inspection_store.key(p['run_id']+'-'+p['attempt'],value['inspection_input_sha256'],
                                       'receipt-'+value['inspection_receipt_sha256']+'.json')
        raw=inspection_store._get(receipt_key,maximum=256*1024)
        log,manifest,context,authority=authenticate(api,value,raw)
        def load_object(relative):
            return inspection_store._get(inspection_store.key(*relative.split('/')),maximum=consumer.MAX_METADATA)
        plan=consumer.prepare(raw,load_object,log,manifest,context)
        owner={k:os.environ[v] for k,v in {'run_id':'GITHUB_RUN_ID','attempt':'GITHUB_RUN_ATTEMPT','sha':'GITHUB_SHA'}.items()}
        # Serialize the workflow and claim before signed ZIP reads. An unknown
        # interrupted attempt needs a new authenticated inspection request,
        # never an automatic repeat of the same download set.
        claim_key=store.key(identity,'claim.json')
        try: store._get(claim_key,maximum=65536)
        except R2NotFound: immutable(store,claim_key,canonical({'request':value,'producer':owner}),maximum=65536)
        else: consumer.fail('already_claimed_without_ready_output')
        public=consumer.materialize(plan,args.output)
        ready=preserve(store,value,args.output,authority,owner)
        receipt=consumer.decode((args.output/'_legacy_output_receipt.json').read_bytes(),MAX_ARTIFACT)
        consumer.verify_materialized_output(args.output,(args.output/'_legacy_output_receipt.json').read_bytes())
        resumed=False
    public={'status':'authenticated-legacy-source-ready','source_count':receipt['source_count'],
        'date_folder':receipt['date_folder'],'original_run':value['run_id'],
        'request_sha256':identity,'source_receipt_sha256':ready['source_receipt_sha256'],
        'resumed_private_output':resumed,'original_source_bytes_proven':False,
        'canonical_task_admission':False,'provider_posts':0,'paid_requests':0,'new_submissions':0}
    if args.github_output:
        with args.github_output.open('a') as out:
            for k,v in {'date_folder':receipt['date_folder'],'pdf_count':receipt['source_count'],
                        'legacy_source_receipt_sha256':ready['source_receipt_sha256']}.items():out.write(f'{k}={v}\n')
    print(json.dumps(public,sort_keys=True));return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except (consumer.NetworkStop,R2TransportError) as error:
        category='tls_certificate_expired' if str(error)=='tls_certificate_expired' else 'network_stop'
        print(json.dumps({'status':'legacy-recovery-stopped','category':category,'network_stop':True,'provider_posts':0}));raise SystemExit(75) from None
    except consumer.ResultHTTPError as error:
        print(json.dumps({'status':'legacy-recovery-rejected','category':'result_http','http_status':error.http_status,
                          'provider_posts':0,'paid_requests':0,'new_submissions':0}));raise SystemExit(2) from None
    except Exception as error:
        print(json.dumps({'status':'legacy-recovery-rejected','category':str(error) if isinstance(error,consumer.ConsumerError) else 'contract',
                          'provider_posts':0,'paid_requests':0,'new_submissions':0}));raise SystemExit(2) from None
