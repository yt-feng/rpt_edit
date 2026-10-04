"""Read-only encrypted original-page visual QA; never a source admission.

Only one authenticated original page is rendered. Its PDF, PNG and private hash
receipt are encrypted together using a bounded RSA recipient certificate. The
published files contain only CMS ciphertext and a sanitized hash/count summary.
"""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
import io
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

import fitz

import archive_market_views_originals as archive
from mineru_task_ledger import digest, encoded, exact_json
from recover_durable_mineru_sources import decode

WORKFLOW = '.github/workflows/market-views-original-page-qa.yml'
OPENSSL = '/usr/bin/openssl'
MAX_CERTIFICATE = 16 * 1024
MAX_PAGE_PIXELS = 40_000_000
MAX_PAGE_BYTES = 64 * 1024 * 1024
MAX_PAYLOAD = 128 * 1024 * 1024
MAX_PAGE_POINTS = 2000
DPI = 300
SAFE_ERRORS = frozenset({'reviewed_visual_qa_workflow_required', 'recipient_certificate_invalid',
    'recipient_rsa_size_invalid', 'visual_qa_request_invalid', 'visual_qa_originals_invalid',
    'visual_qa_page_invalid', 'visual_qa_page_size_invalid', 'visual_qa_output_invalid',
    'visual_qa_encryption_failed', 'visual_qa_crypto_unavailable'})


class QAError(ValueError):
    pass


def fail(category):
    raise QAError(category)


@contextmanager
def _silent_mupdf():
    """Suppress C-level document diagnostics for the complete PDF lifetime."""
    old_errors = fitz.TOOLS.mupdf_display_errors()
    old_warnings = fitz.TOOLS.mupdf_display_warnings()
    try:
        fitz.TOOLS.mupdf_display_errors(False)
        fitz.TOOLS.mupdf_display_warnings(False)
        yield
    finally:
        # Python stream redirection cannot catch MuPDF's native diagnostics.
        # Restore both global switches on success and every failure path.
        try:
            fitz.TOOLS.mupdf_display_errors(old_errors)
        finally:
            fitz.TOOLS.mupdf_display_warnings(old_warnings)


def require_cloud_main(env):
    repository = env.get('GITHUB_REPOSITORY', '')
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or env.get('GITHUB_REF') != 'refs/heads/main'
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            or env.get('GITHUB_WORKFLOW_REF') != repository + '/' + WORKFLOW + '@refs/heads/main'
            or not archive.RUN.fullmatch(env.get('GITHUB_RUN_ID', ''))
            or not archive.SHA.fullmatch(env.get('GITHUB_SHA', ''))):
        fail('reviewed_visual_qa_workflow_required')


def _openssl(args, payload=None, *, maximum=MAX_CERTIFICATE * 4):
    try:
        result = subprocess.run([OPENSSL, *args], input=payload, capture_output=True, timeout=120, check=False)
    except (OSError, subprocess.SubprocessError):
        fail('visual_qa_crypto_unavailable')
    if result.returncode or len(result.stdout) > maximum:
        fail('recipient_certificate_invalid')
    return result.stdout


def checked_recipient(pem):
    if not isinstance(pem, str) or not 1 <= len(pem.encode('utf-8')) <= MAX_CERTIFICATE:
        fail('recipient_certificate_invalid')
    match = re.fullmatch(r'\s*-----BEGIN CERTIFICATE-----\r?\n([A-Za-z0-9+/=\r\n]+)'
                         r'-----END CERTIFICATE-----\s*', pem)
    if match is None:
        fail('recipient_certificate_invalid')
    try:
        supplied_der = base64.b64decode(re.sub(r'\s', '', match[1]), validate=True)
        canonical = ('-----BEGIN CERTIFICATE-----\n' + '\n'.join(
            base64.b64encode(supplied_der).decode('ascii')[offset:offset + 64]
            for offset in range(0, len(base64.b64encode(supplied_der)), 64))
            + '\n-----END CERTIFICATE-----\n').encode('ascii')
    except (ValueError, UnicodeError):
        fail('recipient_certificate_invalid')
    with tempfile.TemporaryDirectory(prefix='original-page-recipient-') as directory:
        path = Path(directory) / 'recipient.pem'; path.write_bytes(canonical); path.chmod(0o600)
        actual_der = _openssl(['x509', '-in', str(path), '-outform', 'DER'])
        if not supplied_der or actual_der != supplied_der:
            fail('recipient_certificate_invalid')
        _openssl(['x509', '-in', str(path), '-checkend', '0', '-noout'])
        public_key = _openssl(['x509', '-in', str(path), '-pubkey', '-noout'])
        description = _openssl(['rsa', '-pubin', '-text', '-noout'], public_key).decode('ascii')
        size = re.search(r'(?:RSA )?Public-Key:\s*\(([0-9]+) bit\)', description)
        if size is None or not 3072 <= int(size[1]) <= 8192:
            fail('recipient_rsa_size_invalid')
    return canonical, {'recipient_certificate_sha256': digest(actual_der), 'recipient_rsa_bits': int(size[1])}


class ReadOnlyClient:
    def __init__(self, client):
        self.client = client

    def get_object(self, **kwargs):
        return self.client.get_object(**kwargs)

    def put_object(self, **kwargs):
        raise AssertionError('Visual QA never publishes private source objects')

    def delete_object(self, **kwargs):
        raise AssertionError('Visual QA never deletes private source objects')


def checked_originals(source, producer, archive_run_id, repository, expected_reports, date_folder,
                      original_source_run_id=''):
    try:
        sha = producer.get('head_sha') if isinstance(producer, dict) else None
        context = archive.context(archive_run_id, date_folder, sha, original_source_run_id)
        archive.check_restore_producer(producer, archive_run_id, repository, sha)
        path = Path(source) / archive.RECEIPT
        if path.is_symlink() or not path.is_file() or not 1 <= path.stat().st_size <= archive.MAX_RECEIPT:
            raise ValueError('receipt')
        receipt_raw = path.read_bytes()
        receipt = archive.checked_receipt(decode(receipt_raw), context, expected_reports)
        raw, inventory, pairs = archive.checked_inputs(source, expected_reports, date_folder)
        if (receipt['manifest_sha256'] != digest(raw) or not exact_json(receipt['original_inventory'], inventory)
                or path.read_bytes() != receipt_raw):
            raise ValueError('inventory')
    except (ValueError, TypeError, KeyError, AttributeError, OSError):
        fail('visual_qa_originals_invalid')
    return context, receipt_raw, raw, inventory, pairs


def _zip_payload(pdf, png, private_receipt):
    result = io.BytesIO()
    with zipfile.ZipFile(result, 'w', compression=zipfile.ZIP_DEFLATED) as output:
        for name, raw in (('original-page.pdf', pdf), ('original-page.png', png), ('page-receipt.json', encoded(private_receipt))):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0)); info.external_attr = 0o600 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            output.writestr(info, raw)
    payload = result.getvalue()
    if not 1 <= len(payload) <= MAX_PAYLOAD:
        fail('visual_qa_page_size_invalid')
    return payload


def encrypt_payload(payload, recipient):
    if not isinstance(payload, bytes) or not 1 <= len(payload) <= MAX_PAYLOAD:
        fail('visual_qa_page_size_invalid')
    with tempfile.TemporaryDirectory(prefix='original-page-cms-') as directory:
        path = Path(directory) / 'recipient.pem'; path.write_bytes(recipient); path.chmod(0o600)
        try:
            result = subprocess.run([OPENSSL, 'cms', '-encrypt', '-aes256', '-binary', '-outform', 'DER', str(path)],
                                    input=payload, capture_output=True, timeout=120, check=False)
        except (OSError, subprocess.SubprocessError):
            fail('visual_qa_encryption_failed')
    if result.returncode or not 1 <= len(result.stdout) <= MAX_PAYLOAD + MAX_CERTIFICATE:
        fail('visual_qa_encryption_failed')
    return result.stdout


def export_page(source, producer, *, archive_run_id, repository, expected_reports, date_folder,
                source_ordinal, page_number, recipient_pem, output_dir, original_source_run_id=''):
    recipient, certificate = checked_recipient(recipient_pem)
    if (type(source_ordinal) is not int or type(expected_reports) is not int
            or not 1 <= source_ordinal <= expected_reports <= 1000
            or type(page_number) is not int or not 1 <= page_number <= 10000):
        fail('visual_qa_request_invalid')
    output_dir = Path(output_dir)
    if (output_dir.exists() or output_dir.is_symlink() or Path(source).resolve() == output_dir.resolve()
            or Path(source).resolve() in output_dir.resolve().parents):
        fail('visual_qa_output_invalid')
    context, receipt_raw, raw, inventory, pairs = checked_originals(source, producer, archive_run_id, repository,
                                                                 expected_reports, date_folder, original_source_run_id)
    path = pairs[source_ordinal - 1][0]
    original = path.read_bytes(); source_sha = digest(original)
    if source_sha != inventory[source_ordinal - 1]['content_sha256']:
        fail('visual_qa_originals_invalid')
    try:
        with _silent_mupdf(), fitz.open(stream=original, filetype='pdf') as document:
            if document.needs_pass or not 1 <= page_number <= document.page_count <= 10000:
                fail('visual_qa_page_invalid')
            source_page = document[page_number - 1]
            size = [float(source_page.rect.width), float(source_page.rect.height)]
            if (not all(math.isfinite(value) and 0 < value <= MAX_PAGE_POINTS for value in size)
                    or math.ceil(size[0] * DPI / 72) * math.ceil(size[1] * DPI / 72) > MAX_PAGE_PIXELS):
                fail('visual_qa_page_size_invalid')
            pixels = source_page.get_pixmap(dpi=DPI, colorspace=fitz.csRGB, alpha=False)
            if pixels.width * pixels.height > MAX_PAGE_PIXELS:
                fail('visual_qa_page_size_invalid')
            png = pixels.tobytes('png')
            with fitz.open() as selected:
                selected.insert_pdf(document, from_page=page_number - 1, to_page=page_number - 1)
                selected.set_metadata({})
                pdf = selected.tobytes(garbage=4, deflate=True)
            page_count = document.page_count
    except QAError:
        raise
    except Exception:
        fail('visual_qa_page_invalid')
    if not 1 <= len(pdf) <= MAX_PAGE_BYTES or not 1 <= len(png) <= MAX_PAGE_BYTES:
        fail('visual_qa_page_size_invalid')
    private = {'schema_version': 1, 'source_context': context, 'manifest_sha256': digest(raw),
               'archive_receipt_sha256': digest(receipt_raw), 'source_pdf_sha256': source_sha,
               'source_pdf_bytes': len(original), 'source_ordinal': source_ordinal, 'page': page_number,
               'source_page_count': page_count, 'page_size_points': size, 'render_dpi': DPI,
               'render_pixel_size': [pixels.width, pixels.height], 'render_pixel_sha256': digest(pixels.samples),
               'page_pdf_sha256': digest(pdf), 'page_png_sha256': digest(png)}
    payload = _zip_payload(pdf, png, private)
    ciphertext = encrypt_payload(payload, recipient)
    check = checked_originals(source, producer, archive_run_id, repository, expected_reports, date_folder,
                              original_source_run_id)
    if check[1] != receipt_raw or check[2] != raw or path.read_bytes() != original:
        fail('visual_qa_originals_invalid')
    summary = {'schema_version': 1, 'success': True, 'status': 'encrypted_visual_qa_only',
               'source_ready': False, 'production_acceptance': False, 'complete_source_handoff': False,
               'archive_run_id': archive_run_id, 'date_folder': date_folder,
               'original_source_run_id': original_source_run_id, 'original_members_verified': expected_reports,
               'source_ordinal': source_ordinal, 'page': page_number, 'source_page_count': page_count,
               'source_pdf_sha256': source_sha, 'source_pdf_bytes': len(original),
               'manifest_sha256': digest(raw), 'archive_receipt_sha256': digest(receipt_raw),
               'page_size_points': size, 'render_dpi': DPI, 'render_pixel_size': [pixels.width, pixels.height],
               'plaintext_payload_sha256': digest(payload), 'ciphertext_sha256': digest(ciphertext),
               'ciphertext_bytes': len(ciphertext), 'cipher': 'CMS-EnvelopedData-AES-256-CBC',
               'model_calls': 0, 'provider_posts': 0, 'canonical_ledger_writes': 0, 'private_source_writes': 0,
               'ocr_calls': 0, **certificate}
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix='.original-page-qa-', dir=output_dir.parent)); temporary.chmod(0o700)
    try:
        for name, contents in (('original-page.cms', ciphertext), ('visual-qa-summary.json', encoded(summary))):
            output = temporary / name; output.write_bytes(contents); output.chmod(0o600)
        temporary.rename(output_dir)
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--producer-json', type=Path, required=True)
    parser.add_argument('--archive-run-id', required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--source-ordinal', type=int, required=True)
    parser.add_argument('--page', type=int, required=True)
    parser.add_argument('--original-source-run-id', default='')
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        require_cloud_main(os.environ)
        pem = os.environ.get('RECIPIENT_CERT_PEM', '')
        checked_recipient(pem)
        if args.producer_json.is_symlink() or not args.producer_json.is_file() or args.producer_json.stat().st_size > 1_000_000:
            fail('visual_qa_originals_invalid')
        producer = decode(args.producer_json.read_bytes())
        sha = producer.get('head_sha') if isinstance(producer, dict) else None
        context = archive.context(args.archive_run_id, args.date_folder, sha, args.original_source_run_id)
        archive.check_restore_producer(producer, args.archive_run_id, os.environ['GITHUB_REPOSITORY'], sha)
        if (not 1 <= args.source_ordinal <= args.expected_reports <= 1000 or not 1 <= args.page <= 10000):
            fail('visual_qa_request_invalid')
        import boto3
        from botocore.config import Config
        from private_workflow_handoff import require_env
        client = boto3.client('s3', endpoint_url=f'https://{require_env("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com',
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
            region_name='auto', config=Config(connect_timeout=20, read_timeout=180,
            retries={'total_max_attempts': 1, 'mode': 'standard'}))
        with tempfile.TemporaryDirectory(prefix='private-original-visual-qa-') as directory:
            source = Path(directory) / 'originals'
            archive.restore_originals(source, args.expected_reports, context, ReadOnlyClient(client), require_env('R2_BUCKET'))
            summary = export_page(source, producer, archive_run_id=args.archive_run_id,
                repository=os.environ['GITHUB_REPOSITORY'], expected_reports=args.expected_reports,
                date_folder=args.date_folder, source_ordinal=args.source_ordinal, page_number=args.page,
                recipient_pem=pem, output_dir=args.output_dir, original_source_run_id=args.original_source_run_id)
        print(json.dumps(summary, sort_keys=True))
        return 0
    except Exception as error:
        category = str(error) if type(error) is QAError and str(error) in SAFE_ERRORS else 'encrypted_visual_qa_failed'
        print('Encrypted original page QA stopped: ' + category, file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
