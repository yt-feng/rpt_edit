#!/usr/bin/env python3
"""Bounded R2 handoff for offline locales; never a production activation API.

Only the private portal-global-locales/v1 prefix is accessed. Source snapshots,
checkpoints and complete candidates replace their own latest object; no run-ID
archives, public URLs, model-provider calls, or destructive cleanup are used.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import tarfile
import tempfile
from typing import Any
from portal_language_registry import selected_locales
from offline_translation import MODEL_ID, atomic_json

PREFIX = 'portal-global-locales/v1/'
MAX_ARCHIVE = 256 * 1024 * 1024
MAX_TREE = 2 * 1024 * 1024 * 1024
MAX_CHECKPOINT = 8 * 1024 * 1024
MAX_CACHE_JSON = 64 * 1024 * 1024
MAX_FILES = 100_000


def namespace() -> str:
    root=Path(__file__).parent
    digest=hashlib.sha256(MODEL_ID.encode())
    for name in ('hymt_offline_translation.py','portal_chinese_script.py','build_portal_locales.py','financial_quantity_integrity.py'):
        digest.update((root/name).read_bytes())
    return digest.hexdigest()[:24]


def object_key(kind: str, locale: str | None = None) -> str:
    if kind == 'source': return PREFIX+'sources/current.tar.gz'
    if kind not in {'checkpoint','candidate','readiness'}: raise ValueError('Unknown R2 handoff kind')
    codes=selected_locales(locale)
    if len(codes)!=1 or codes[0]!=locale: raise ValueError('One canonical locale is required')
    suffix={'checkpoint':'cache.json.gz','candidate':'site.tar.gz','readiness':'readiness.json'}[kind]
    return PREFIX+namespace()+'/'+locale+'/'+suffix


def client_from_env():
    import boto3
    from botocore.config import Config
    names=('R2_ACCOUNT_ID','R2_ACCESS_KEY_ID','R2_SECRET_ACCESS_KEY','R2_BUCKET')
    if any(not os.environ.get(name) for name in names):
        raise RuntimeError('Existing R2 account, bucket and storage credentials are required')
    account=os.environ['R2_ACCOUNT_ID']
    if not re.fullmatch(r'[0-9a-f]{32}',account): raise ValueError('Invalid R2 account identifier')
    return boto3.client('s3',endpoint_url=f'https://{account}.r2.cloudflarestorage.com',
                       aws_access_key_id=os.environ['R2_ACCESS_KEY_ID'],
                       aws_secret_access_key=os.environ['R2_SECRET_ACCESS_KEY'],region_name='auto',
                       config=Config(connect_timeout=15,read_timeout=120,retries={'max_attempts':2})),os.environ['R2_BUCKET']


def put(client: Any, bucket: str, key: str, body: bytes, limit: int) -> str:
    if not key.startswith(PREFIX) or '..' in key: raise ValueError('Outside locale R2 namespace')
    if not 0 < len(body) <= limit: raise ValueError('R2 handoff exceeds its size bound')
    checksum=hashlib.sha256(body).hexdigest()
    client.put_object(Bucket=bucket,Key=key,Body=body,
                      ContentType='application/gzip' if key.endswith('.gz') else 'application/json',
                      CacheControl='private, no-store',Metadata={'sha256':checksum,'scope':'offline-locale-candidate'})
    metadata=client.head_object(Bucket=bucket,Key=key)
    if metadata.get('Metadata',{}).get('sha256')!=checksum or metadata.get('ContentLength')!=len(body):
        raise RuntimeError('R2 upload readback did not match')
    return checksum


def get(client: Any, bucket: str, key: str, limit: int, *, missing_ok: bool=False) -> bytes | None:
    if not key.startswith(PREFIX) or '..' in key: raise ValueError('Outside locale R2 namespace')
    try: obj=client.get_object(Bucket=bucket,Key=key)
    except Exception as error:
        code=str(getattr(error,'response',{}).get('Error',{}).get('Code',''))
        if missing_ok and code in {'NoSuchKey','404','NotFound'}: return None
        raise RuntimeError('R2 handoff read failed; permissions and service errors are not cache misses') from error
    stream=obj['Body']
    try:
        if not 0 < obj.get('ContentLength',0) <= limit: raise ValueError('Oversized R2 handoff')
        body=stream.read(limit+1)
        if len(body)>limit or len(body)!=obj['ContentLength']: raise ValueError('Truncated or oversized R2 handoff')
        if hashlib.sha256(body).hexdigest()!=obj.get('Metadata',{}).get('sha256'):
            raise ValueError('R2 handoff checksum mismatch')
        return body
    finally: stream.close()


def pack_tree(root: Path) -> bytes:
    if not root.is_dir() or root.is_symlink(): raise ValueError('A real source directory is required')
    output=io.BytesIO();total=0;count=0
    with tarfile.open(fileobj=output,mode='w:gz') as archive:
        for path in sorted(root.rglob('*')):
            if path.is_symlink(): raise ValueError('Symlinks are forbidden in locale handoffs')
            if not path.is_file(): continue
            count+=1;total+=path.stat().st_size
            if count>MAX_FILES or total>MAX_TREE: raise ValueError('Locale tree exceeds its bound')
            archive.add(path,arcname=path.relative_to(root).as_posix(),recursive=False)
            if output.tell()>MAX_ARCHIVE: raise ValueError('Locale package exceeds its bound')
    body=output.getvalue()
    if len(body)>MAX_ARCHIVE: raise ValueError('Locale package exceeds its bound')
    return body


def unpack_tree(body: bytes, output: Path) -> None:
    if output.exists(): raise ValueError('R2 input must unpack into a new directory')
    if len(body)>MAX_ARCHIVE: raise ValueError('Locale package exceeds its bound')
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=output.name+'-',dir=output.parent) as temporary:
        root=Path(temporary);total=0;seen=set()
        with tarfile.open(fileobj=io.BytesIO(body),mode='r:gz') as archive:
            for item in archive:
                name=PurePosixPath(item.name)
                if (not item.isfile() or name.is_absolute() or not name.parts or
                    any(part in {'..','.'} for part in name.parts) or name.as_posix()!=item.name or '\\' in item.name or
                    item.name in seen or item.size<0): raise ValueError('Unsafe locale archive member')
                total+=item.size;seen.add(item.name)
                if len(seen)>MAX_FILES or total>MAX_TREE: raise ValueError('Locale archive expands beyond bound')
                target=root.joinpath(*name.parts);target.parent.mkdir(parents=True,exist_ok=True)
                with archive.extractfile(item) as source, target.open('wb') as destination:
                    remaining=item.size
                    while remaining:
                        block=source.read(min(1024*1024,remaining))
                        if not block: raise ValueError('Truncated locale archive member')
                        destination.write(block);remaining-=len(block)
        root.rename(output)


def validate_checkpoint(body: bytes, locale: str) -> None:
    if not 0<len(body)<=MAX_CHECKPOINT: raise ValueError('Translation checkpoint exceeds 8 MiB')
    with gzip.GzipFile(fileobj=io.BytesIO(body)) as stream: decoded=stream.read(MAX_CACHE_JSON+1)
    if len(decoded)>MAX_CACHE_JSON: raise ValueError('Translation checkpoint expands beyond bound')
    data=json.loads(decoded)
    if data.get('provider')!='hymt' or data.get('model')!=MODEL_ID:
        raise ValueError('Checkpoint provider or pinned model mismatch')
    if set(data.get('locales',{}))!={locale} or not isinstance(data['locales'][locale],dict):
        raise ValueError('Checkpoint must contain exactly its own locale')
    if data.get('_source_fallbacks'): raise ValueError('Source fallbacks are not translated checkpoints')


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['push-source','pull-source','push-checkpoint','pull-checkpoint','push-candidate','push-readiness'])
    parser.add_argument('--path',type=Path,required=True)
    parser.add_argument('--locale')
    parser.add_argument('--expected-source')
    parser.add_argument('--readiness',type=Path)
    args=parser.parse_args()
    from compare_hymt_translation import require_actions
    require_actions();client,bucket=client_from_env()
    kind=args.operation.split('-',1)[1];key=object_key(kind,args.locale)
    if args.operation=='push-source':
        from prepare_portal_global_locales import source_identity
        identity=source_identity(args.path)
        put(client,bucket,key,pack_tree(args.path),MAX_ARCHIVE)
        print(json.dumps({'source_sha256':identity,'storage':'cloudflare-r2'}))
        if os.environ.get('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'],'a') as stream:stream.write('source_sha256='+identity+'\n')
    elif args.operation=='pull-source':
        if not re.fullmatch(r'[0-9a-f]{64}',args.expected_source or ''):raise ValueError('Source identity is required')
        unpack_tree(get(client,bucket,key,MAX_ARCHIVE),args.path)
        from prepare_portal_global_locales import source_identity
        if source_identity(args.path)!=args.expected_source:raise ValueError('Source was superseded; restart from the current snapshot')
    elif args.operation=='push-checkpoint':
        if not args.path.is_file() or args.path.is_symlink():raise ValueError('Checkpoint missing or unsafe')
        body=args.path.read_bytes();validate_checkpoint(body,args.locale)
        put(client,bucket,key,body,MAX_CHECKPOINT)
    elif args.operation=='pull-checkpoint':
        if args.path.exists():raise ValueError('Checkpoint destination already exists')
        body=get(client,bucket,key,MAX_CHECKPOINT,missing_ok=True)
        if body is not None:
            validate_checkpoint(body,args.locale);args.path.parent.mkdir(parents=True,exist_ok=True);args.path.write_bytes(body)
        print(json.dumps({'checkpoint_restored':body is not None,'storage':'cloudflare-r2'}))
    elif args.operation=='push-candidate':
        if args.readiness is None:raise ValueError('Candidate readiness evidence is required')
        ready=json.loads(args.readiness.read_text())
        if (ready.get('candidate_complete') is not True or ready.get('production_ready') is not False or
            ready.get('targets')!=[args.locale] or ready.get('provider')!='hymt' or
            ready.get('model')!=MODEL_ID or ready.get('paid_provider_requests')!=0):
            raise ValueError('Only a complete offline candidate can be retained; activation is separate')
        from portal_locale_manifest import load_locale_manifest,validate_translation_resolution
        from portal_language_registry import manifest_locales
        manifest=load_locale_manifest(args.path/'data/i18n/manifest.json')
        if manifest_locales(manifest)!=(args.locale,):raise ValueError('Candidate language identity mismatch')
        validate_translation_resolution(manifest,[args.locale])
        checksum=put(client,bucket,key,pack_tree(args.path),MAX_ARCHIVE)
        ready['candidate_archive_sha256']=checksum;ready['storage']='cloudflare-r2'
        put(client,bucket,object_key('readiness',args.locale),json.dumps(ready,ensure_ascii=False).encode(),1024*1024)
    else:
        ready=json.loads(args.path.read_text())
        if ready.get('production_ready') is not False:raise ValueError('Preparation cannot claim activation')
        put(client,bucket,key,json.dumps(ready,ensure_ascii=False).encode(),1024*1024)
    return 0

if __name__=='__main__':raise SystemExit(main())
