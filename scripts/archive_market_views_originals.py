"""Private, immutable original-PDF archive; never a completed source handoff.

Upload verifies the complete original date/count/hash inventory before preserving
any bytes. Restore performs only R2 GETs and publishes a new local directory only
after every archived original passes the same checks. Seven-day expiry is an
application read limit; physical deletion is a separate cloud lifecycle policy.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import gzip
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tarfile
import tempfile

from recover_durable_mineru_sources import MANIFEST, decode, exact_date, frozen_inputs
from mineru_task_ledger import digest, encoded, exact_json

PREFIX = '_private-workflow-originals/native-pdf'
WORKFLOW = '.github/workflows/market-views-native-recovery.yml'
KIND = 'original-pdf-archive'
RECEIPT = 'originals-receipt.json'
MAX_ARCHIVE = 512 * 1024 * 1024
MAX_RECEIPT = 16 * 1024 * 1024
TTL_DAYS = 7
RUN = re.compile(r'[1-9][0-9]{0,19}')
SHA = re.compile(r'[a-f0-9]{40}')
HASH = re.compile(r'[a-f0-9]{64}')


class OriginalsError(ValueError):
    pass


def now_utc():
    return datetime.now(timezone.utc)


def context(run_id, date_folder, execution_sha, original_source_run_id=''):
    exact_date(date_folder)
    if (not isinstance(run_id, str) or not RUN.fullmatch(run_id)
            or not isinstance(execution_sha, str) or not SHA.fullmatch(execution_sha)
            or not isinstance(original_source_run_id, str)
            or original_source_run_id and not RUN.fullmatch(original_source_run_id)):
        raise OriginalsError('producer_context_invalid')
    return {'producer_run_id': run_id, 'date_folder': date_folder, 'execution_sha': execution_sha,
            'original_source_run_id': original_source_run_id, 'producer_workflow': WORKFLOW}


def require_manual_main(env):
    repository = env.get('GITHUB_REPOSITORY', '')
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or env.get('GITHUB_REF') != 'refs/heads/main'
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            or env.get('GITHUB_WORKFLOW_REF') != repository + '/' + WORKFLOW + '@refs/heads/main'):
        raise OriginalsError('manual_main_producer_required')


def checked_inputs(source, expected_reports, date_folder):
    if type(expected_reports) is not int or not 1 <= expected_reports <= 1000:
        raise OriginalsError('original_count_invalid')
    raw, bindings, pairs = frozen_inputs(source, Path(source) / MANIFEST, expected_reports, date_folder)
    rows = decode(raw)
    if any(PurePosixPath(row['dropbox_path']).parts[:3] != ('/', 'zip_backup', date_folder) for row in rows):
        raise OriginalsError('original_date_invalid')
    if len(raw) + sum(path.stat().st_size for path, _ in pairs) > MAX_ARCHIVE:
        raise OriginalsError('original_bytes_exceed_bound')
    return raw, bindings, pairs


def packed_originals(raw, pairs):
    output = io.BytesIO()
    with gzip.GzipFile(fileobj=output, mode='wb', mtime=0) as compressed:
        with tarfile.open(fileobj=compressed, mode='w|', format=tarfile.PAX_FORMAT) as archive:
            entries = [(MANIFEST, io.BytesIO(raw), len(raw))]
            for path, source in pairs:
                entries.append((source, path, path.stat().st_size))
            for name, stream, size in entries:
                info = tarfile.TarInfo(name)
                info.mode, info.size, info.mtime = 0o600, size, 0
                if isinstance(stream, Path):
                    with stream.open('rb') as opened:
                        archive.addfile(info, opened)
                else:
                    archive.addfile(info, stream)
    payload = output.getvalue()
    if not 1 <= len(payload) <= MAX_ARCHIVE:
        raise OriginalsError('archive_size_invalid')
    return payload


def unpack_checked(payload, destination, expected_reports, date_folder, manifest_sha, expected_bindings):
    # Bound the entire decoded tar, including PAX/GNU extension headers, before
    # tarfile can read an oversized hidden header internally.
    with gzip.GzipFile(fileobj=io.BytesIO(payload), mode='rb') as compressed:
        decoded = compressed.read(MAX_ARCHIVE + 1)
    if len(decoded) > MAX_ARCHIVE:
        raise OriginalsError('decoded_archive_exceeds_bound')
    expected = {item['source_pdf'] for item in expected_bindings} | {MANIFEST}
    with tarfile.open(fileobj=io.BytesIO(decoded), mode='r|') as archive:
        seen, total = set(), 0
        for member in archive:
            total += member.size
            if (member.name not in expected or member.name in seen or len(seen) >= len(expected)
                    or not member.isfile() or member.size < 1 or total > MAX_ARCHIVE
                    or member.name != PurePosixPath(member.name).name or '..' in PurePosixPath(member.name).parts):
                raise OriginalsError('original_archive_members_invalid')
            seen.add(member.name)
            stream = archive.extractfile(member)
            if stream is None:
                raise OriginalsError('original_archive_member_missing')
            data = stream.read(member.size + 1)
            if len(data) != member.size:
                raise OriginalsError('original_archive_member_truncated')
            path = Path(destination) / member.name
            path.write_bytes(data)
            path.chmod(0o600)
        if seen != expected:
            raise OriginalsError('original_archive_members_invalid')
    raw, bindings, _ = checked_inputs(destination, expected_reports, date_folder)
    if digest(raw) != manifest_sha or not exact_json(bindings, expected_bindings):
        raise OriginalsError('restored_original_binding_mismatch')


def read_object(client, bucket, key, maximum, *, missing_ok=False):
    try:
        response = client.get_object(Bucket=bucket, Key=key)
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        if missing_ok and code in {'NoSuchKey', '404', 'NotFound'}:
            return None
        raise OriginalsError('private_archive_read_failed') from None
    size = response.get('ContentLength')
    metadata = response.get('Metadata', {})
    if (type(size) is not int or not 1 <= size <= maximum or not isinstance(metadata, dict)
            or metadata.get('kind') != KIND or not HASH.fullmatch(str(metadata.get('sha256', '')))):
        raise OriginalsError('private_archive_metadata_invalid')
    body = response['Body']
    try:
        payload = body.read(maximum + 1)
    finally:
        body.close()
    if not isinstance(payload, bytes) or len(payload) != size or digest(payload) != metadata['sha256']:
        raise OriginalsError('private_archive_hash_mismatch')
    return payload


def immutable_put(client, bucket, key, payload, content_type, maximum):
    try:
        client.put_object(Bucket=bucket, Key=key, Body=payload, ContentType=content_type,
                          Metadata={'sha256': digest(payload), 'kind': KIND}, IfNoneMatch='*')
    except Exception:
        # A conditional conflict or a lost ACK never triggers another PUT.
        # Only exact immutable full-byte readback establishes persistence.
        pass
    if read_object(client, bucket, key, maximum) != payload:
        raise OriginalsError('private_archive_immutable_conflict')


def checked_receipt(value, expected_context, expected_reports, *, now=now_utc):
    keys = {'schema_version', 'kind', 'source_ready', 'source_context', 'report_count', 'manifest_sha256',
            'original_inventory', 'archive_sha256', 'archive_bytes', 'created_at_utc', 'expires_at_utc',
            'expiry_policy', 'physical_deletion_guaranteed'}
    if (not isinstance(value, dict) or set(value) != keys or type(value.get('schema_version')) is not int
            or value['schema_version'] != 1 or value['kind'] != KIND or value['source_ready'] is not False
            or value['physical_deletion_guaranteed'] is not False or value['expiry_policy'] != 'restore-disabled-after-7-days'
            or not exact_json(value['source_context'], expected_context)
            or type(value['report_count']) is not int or value['report_count'] != expected_reports
            or not HASH.fullmatch(str(value['manifest_sha256'])) or not HASH.fullmatch(str(value['archive_sha256']))
            or type(value['archive_bytes']) is not int or not 1 <= value['archive_bytes'] <= MAX_ARCHIVE
            or not isinstance(value['original_inventory'], list)):
        raise OriginalsError('original_receipt_invalid')
    try:
        created, expires = datetime.fromisoformat(value['created_at_utc']), datetime.fromisoformat(value['expires_at_utc'])
        current = now()
        if (created.tzinfo is None or expires.tzinfo is None or current.tzinfo is None
                or created.utcoffset() != timedelta(0) or expires.utcoffset() != timedelta(0)
                or expires - created != timedelta(days=TTL_DAYS) or not created <= current < expires):
            raise ValueError('expiry')
    except (ValueError, TypeError, AttributeError):
        raise OriginalsError('original_archive_expired_or_time_invalid') from None
    return value


def upload_originals(source, expected_reports, source_context, client, bucket, *, now=now_utc):
    source_context = context(source_context['producer_run_id'], source_context['date_folder'],
                             source_context['execution_sha'], source_context['original_source_run_id'])
    raw, bindings, pairs = checked_inputs(source, expected_reports, source_context['date_folder'])
    payload = packed_originals(raw, pairs)
    # Packing must not preserve a partial/raced version of the frozen originals.
    raw_after, bindings_after, _ = checked_inputs(source, expected_reports, source_context['date_folder'])
    if raw_after != raw or not exact_json(bindings_after, bindings):
        raise OriginalsError('original_input_changed')
    # Source snapshots cannot alone exclude a temporary change while packing.
    # Prove the exact sealed payload is independently fully recoverable before
    # its first R2 publication.
    with tempfile.TemporaryDirectory(prefix='originals-packed-check-') as checked:
        unpack_checked(payload, checked, expected_reports, source_context['date_folder'], digest(raw), bindings)
    prefix = f"{PREFIX}/{source_context['producer_run_id']}/{source_context['date_folder']}"
    archive_key, receipt_key = prefix + '/originals.tar.gz', prefix + '/' + RECEIPT
    existing = read_object(client, bucket, receipt_key, MAX_RECEIPT, missing_ok=True)
    if existing is None:
        created = now()
        value = {'schema_version': 1, 'kind': KIND, 'source_ready': False, 'source_context': source_context,
                 'report_count': expected_reports, 'manifest_sha256': digest(raw), 'original_inventory': bindings,
                 'archive_sha256': digest(payload), 'archive_bytes': len(payload), 'created_at_utc': created.isoformat(),
                 'expires_at_utc': (created + timedelta(days=TTL_DAYS)).isoformat(),
                 'expiry_policy': 'restore-disabled-after-7-days', 'physical_deletion_guaranteed': False}
    else:
        value = decode(existing)
    checked_receipt(value, source_context, expected_reports, now=now)
    if (value['manifest_sha256'] != digest(raw) or value['archive_sha256'] != digest(payload)
            or value['archive_bytes'] != len(payload) or not exact_json(value['original_inventory'], bindings)):
        raise OriginalsError('original_archive_binding_conflict')
    immutable_put(client, bucket, archive_key, payload, 'application/gzip', MAX_ARCHIVE)
    immutable_put(client, bucket, receipt_key, encoded(value), 'application/json', MAX_RECEIPT)
    return value


def restore_originals(destination, expected_reports, source_context, client, bucket, *, now=now_utc):
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        raise OriginalsError('restore_destination_must_be_new')
    source_context = context(source_context['producer_run_id'], source_context['date_folder'],
                             source_context['execution_sha'], source_context['original_source_run_id'])
    prefix = f"{PREFIX}/{source_context['producer_run_id']}/{source_context['date_folder']}"
    receipt = checked_receipt(decode(read_object(client, bucket, prefix + '/' + RECEIPT, MAX_RECEIPT)),
                              source_context, expected_reports, now=now)
    payload = read_object(client, bucket, prefix + '/originals.tar.gz', MAX_ARCHIVE)
    if digest(payload) != receipt['archive_sha256'] or len(payload) != receipt['archive_bytes']:
        raise OriginalsError('original_archive_binding_conflict')
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix='.originals-restore-', dir=destination.parent))
    try:
        unpack_checked(payload, temporary, expected_reports, source_context['date_folder'],
                       receipt['manifest_sha256'], receipt['original_inventory'])
        (temporary / RECEIPT).write_bytes(encoded(receipt))
        (temporary / RECEIPT).chmod(0o600)
        checked_receipt(receipt, source_context, expected_reports, now=now)
        temporary.rename(destination)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return receipt


def check_restore_producer(value, run_id, repository, execution_sha):
    if (not isinstance(value, dict) or type(value.get('id')) is not int or value['id'] != int(run_id)
            or value.get('path') != WORKFLOW or value.get('event') != 'workflow_dispatch'
            or value.get('head_branch') != 'main' or value.get('head_sha') != execution_sha
            or value.get('repository', {}).get('full_name') != repository
            or value.get('status') != 'completed' or value.get('conclusion') not in {'success', 'failure'}):
        raise OriginalsError('restore_producer_invalid')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('upload', 'restore'))
    parser.add_argument('--source', type=Path)
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--run-id', required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--execution-sha', required=True)
    parser.add_argument('--original-source-run-id', default='')
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--producer-json', type=Path)
    parser.add_argument('--repository')
    args = parser.parse_args(argv)
    try:
        source_context = context(args.run_id, args.date_folder, args.execution_sha, args.original_source_run_id)
        if args.command == 'upload':
            require_manual_main(os.environ)
            if (args.run_id != os.environ.get('GITHUB_RUN_ID') or args.execution_sha != os.environ.get('GITHUB_SHA')
                    or args.source is None or args.destination is not None):
                raise OriginalsError('upload_context_invalid')
        else:
            if (args.destination is None or args.source is not None or not args.repository
                    or args.producer_json is None or args.producer_json.is_symlink()):
                raise OriginalsError('restore_context_invalid')
            check_restore_producer(decode(args.producer_json.read_bytes()), args.run_id, args.repository, args.execution_sha)
        from private_workflow_handoff import require_env
        import boto3
        from botocore.config import Config
        client = boto3.client('s3', endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                             aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
                             region_name='auto', config=Config(connect_timeout=20, read_timeout=180,
                                                              retries={'total_max_attempts': 1, 'mode': 'standard'}))
        bucket = require_env('R2_BUCKET')
        if args.command == 'upload':
            receipt = upload_originals(args.source, args.expected_reports, source_context, client, bucket)
        else:
            receipt = restore_originals(args.destination, args.expected_reports, source_context, client, bucket)
        print(json.dumps({'kind': KIND, 'source_ready': False, 'report_count': receipt['report_count'],
                          'manifest_sha256': receipt['manifest_sha256'], 'archive_sha256': receipt['archive_sha256'],
                          'archive_bytes': receipt['archive_bytes'], 'expires_at_utc': receipt['expires_at_utc'],
                          'physical_deletion_guaranteed': False}, sort_keys=True))
        return 0
    except Exception as error:
        category = str(error) if type(error) is OriginalsError else 'original_archive_failed'
        print('Original PDF archive stopped: ' + category, file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
