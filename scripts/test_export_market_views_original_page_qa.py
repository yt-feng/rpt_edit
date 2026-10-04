"""Offline real CMS encryption and exact complete original-page contracts."""
import base64
from datetime import timedelta
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import fitz

import export_market_views_original_page_qa as qa
import archive_market_views_originals as archive
from mineru_task_ledger import digest, encoded


class QATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.crypto = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.crypto.cleanup)
        cls.key = Path(cls.crypto.name) / 'key.pem'; cls.cert = Path(cls.crypto.name) / 'cert.pem'
        result = subprocess.run([qa.OPENSSL, 'req', '-x509', '-newkey', 'rsa:3072', '-nodes', '-days', '1',
            '-subj', '/CN=offline-original-page-qa', '-keyout', str(cls.key), '-out', str(cls.cert)],
            capture_output=True, timeout=120, check=False)
        if result.returncode:
            raise AssertionError('System OpenSSL real encryption fixture is required')
        cls.key.chmod(0o600); cls.pem = cls.cert.read_text()

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(); self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name); self.source = self.root / 'originals'; self.source.mkdir()
        self.producer = {'id': 12345, 'head_sha': 'a' * 40, 'path': archive.WORKFLOW,
            'head_branch': 'main', 'event': 'workflow_dispatch', 'status': 'completed', 'conclusion': 'success',
            'repository': {'full_name': 'owner/repo'}}
        self.rows = []
        for index in range(2):
            name = f'PRIVATE-{index}.pdf'
            with fitz.open() as document:
                for number in range(2):
                    page = document.new_page(width=300, height=400)
                    page.insert_text((30, 50), f'Synthetic page {number + 1}; 4.8 (3.1)%')
                raw = document.tobytes()
            (self.source / name).write_bytes(raw)
            self.rows.append({'process_local_path': '/private/' + name, 'content_sha256': digest(raw),
                              'dropbox_path': '/zip_backup/261002/' + name})
        (self.source / archive.MANIFEST).write_bytes(encoded(self.rows))
        raw, inventory, _ = archive.checked_inputs(self.source, 2, '261002')
        now = archive.now_utc()
        self.receipt = {'schema_version': 1, 'kind': archive.KIND, 'source_ready': False,
            'source_context': archive.context('12345', '261002', 'a' * 40), 'report_count': 2,
            'manifest_sha256': digest(raw), 'original_inventory': inventory, 'archive_sha256': 'b' * 64,
            'archive_bytes': 100, 'created_at_utc': now.isoformat(),
            'expires_at_utc': (now + timedelta(days=7)).isoformat(),
            'expiry_policy': 'restore-disabled-after-7-days', 'physical_deletion_guaranteed': False}
        (self.source / archive.RECEIPT).write_bytes(encoded(self.receipt))

    def export(self, **kwargs):
        values = dict(archive_run_id='12345', repository='owner/repo', expected_reports=2, date_folder='261002',
            source_ordinal=1, page_number=2, recipient_pem=self.pem, output_dir=self.root / 'encrypted')
        values.update(kwargs)
        with patch('socket.create_connection', side_effect=AssertionError('No network in QA tests')):
            return qa.export_page(self.source, self.producer, **values)

    def decrypt(self, ciphertext):
        result = subprocess.run([qa.OPENSSL, 'cms', '-decrypt', '-binary', '-inform', 'DER',
            '-recip', str(self.cert), '-inkey', str(self.key)], input=ciphertext,
            capture_output=True, timeout=120, check=False)
        self.assertEqual(result.returncode, 0)
        return result.stdout

    def test_real_cms_recipient_decrypts_only_requested_pdf_png_hash_receipt(self):
        summary = self.export()
        output = self.root / 'encrypted'
        self.assertEqual({path.name for path in output.iterdir()}, {'original-page.cms', 'visual-qa-summary.json'})
        ciphertext = (output / 'original-page.cms').read_bytes()
        payload = self.decrypt(ciphertext)
        self.assertEqual(summary['ciphertext_sha256'], digest(ciphertext))
        self.assertEqual(summary['plaintext_payload_sha256'], digest(payload))
        self.assertEqual(summary['recipient_rsa_bits'], 3072)
        self.assertEqual(summary['source_pdf_sha256'], self.rows[0]['content_sha256'])
        self.assertFalse(summary['source_ready']); self.assertFalse(summary['production_acceptance'])
        for count in ('model_calls', 'ocr_calls', 'provider_posts', 'canonical_ledger_writes', 'private_source_writes'):
            self.assertEqual(summary[count], 0)
        self.assertNotIn('PRIVATE', json.dumps(summary)); self.assertNotIn('Synthetic', json.dumps(summary))
        self.assertNotIn(b'Synthetic', ciphertext)
        with zipfile.ZipFile(io.BytesIO(payload)) as decrypted:
            self.assertEqual(set(decrypted.namelist()), {'original-page.pdf', 'original-page.png', 'page-receipt.json'})
            receipt = json.loads(decrypted.read('page-receipt.json'))
            self.assertEqual(receipt['page'], 2)
            self.assertEqual(receipt['source_pdf_sha256'], self.rows[0]['content_sha256'])
            pdf = decrypted.read('original-page.pdf'); png = decrypted.read('original-page.png')
            self.assertEqual(receipt['page_pdf_sha256'], digest(pdf)); self.assertEqual(receipt['page_png_sha256'], digest(png))
            with fitz.open(stream=pdf, filetype='pdf') as document:
                self.assertEqual(document.page_count, 1)
                self.assertIn('Synthetic page 2', document[0].get_text())
                self.assertNotIn('Synthetic page 1', document[0].get_text())
            self.assertTrue(png.startswith(b'\x89PNG'))
        self.assertEqual(output.stat().st_mode & 0o777, 0o700)
        self.assertTrue(all(path.stat().st_mode & 0o777 == 0o600 for path in output.iterdir()))

    def test_recipient_rejects_url_private_key_multiple_certificates_and_oversize_before_source_read(self):
        for pem in ('https://PRIVATE.invalid/cert', self.key.read_text(), self.pem + self.pem,
                    ' ' * (qa.MAX_CERTIFICATE + 1), '-----BEGIN CERTIFICATE-----\nPRIVATE\n-----END CERTIFICATE-----'):
            with self.subTest(kind=len(pem)), patch.object(qa, 'checked_originals', side_effect=AssertionError('No source read')), \
                    self.assertRaises(qa.QAError):
                self.export(recipient_pem=pem)

    def test_actual_small_rsa_and_ec_certificates_are_rejected(self):
        for kind in ('rsa:2048', 'ec'):
            key = self.root / 'other-key.pem'; cert = self.root / 'other-cert.pem'
            command = [qa.OPENSSL, 'req', '-x509', '-newkey', kind]
            if kind == 'ec': command += ['-pkeyopt', 'ec_paramgen_curve:prime256v1']
            result = subprocess.run(command + ['-nodes', '-days', '1', '-subj', '/CN=offline-invalid',
                '-keyout', str(key), '-out', str(cert)], capture_output=True, timeout=120, check=False)
            self.assertEqual(result.returncode, 0)
            with self.subTest(kind=kind), self.assertRaises(qa.QAError):
                qa.checked_recipient(cert.read_text())

    def test_complete_other_pdf_hash_producer_context_and_expiry_required_before_render(self):
        with patch.object(fitz.Page, 'get_pixmap', side_effect=AssertionError('No partial source render')):
            self.producer['event'] = 'push'
            with self.assertRaises(qa.QAError): self.export()
            self.producer['event'] = 'workflow_dispatch'
            path = self.source / 'PRIVATE-1.pdf'; original = path.read_bytes(); path.write_bytes(original + b'changed')
            with self.assertRaises(qa.QAError): self.export()
            path.write_bytes(original)
            self.receipt['source_context']['original_source_run_id'] = '99999'
            (self.source / archive.RECEIPT).write_bytes(encoded(self.receipt))
            with self.assertRaises(qa.QAError): self.export()
            self.receipt['source_context']['original_source_run_id'] = ''
            self.receipt['expires_at_utc'] = self.receipt['created_at_utc']
            (self.source / archive.RECEIPT).write_bytes(encoded(self.receipt))
            with self.assertRaises(qa.QAError): self.export()
        self.assertFalse((self.root / 'encrypted').exists())

    def test_page_ordinal_geometry_pixel_and_byte_bounds_emit_no_output(self):
        for values in ({'source_ordinal': True}, {'source_ordinal': 3}, {'page_number': 3}, {'page_number': 0}):
            with self.subTest(values=values), self.assertRaises(qa.QAError): self.export(**values)
        with patch.object(qa, 'MAX_PAGE_PIXELS', 10), self.assertRaises(qa.QAError): self.export()
        with patch.object(qa, 'MAX_PAGE_BYTES', 10), self.assertRaises(qa.QAError): self.export()
        self.assertFalse((self.root / 'encrypted').exists())

    def test_archive_changes_during_encryption_block_ciphertext_publication(self):
        encrypt = qa.encrypt_payload
        def mutate(payload, recipient):
            result = encrypt(payload, recipient)
            (self.source / 'PRIVATE-1.pdf').write_bytes(b'%PDF-1.7 changed original')
            return result
        with patch.object(qa, 'encrypt_payload', side_effect=mutate), self.assertRaises(qa.QAError): self.export()
        self.assertFalse((self.root / 'encrypted').exists())

    def test_r2_client_explicitly_prohibits_mutation(self):
        class Client:
            def get_object(self, **kwargs): return kwargs
        client = qa.ReadOnlyClient(Client())
        self.assertEqual(client.get_object(Key='fixed'), {'Key': 'fixed'})
        for operation in (client.put_object, client.delete_object):
            with self.assertRaises(AssertionError): operation(Key='fixed')

    def test_manual_main_guard_and_invalid_certificate_precede_archive_restore(self):
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main',
            'GITHUB_REPOSITORY': 'owner/repo', 'GITHUB_RUN_ID': '45678', 'GITHUB_SHA': 'c' * 40,
            'GITHUB_WORKFLOW_REF': 'owner/repo/' + qa.WORKFLOW + '@refs/heads/main'}
        qa.require_cloud_main(env)
        for key in ('GITHUB_EVENT_NAME', 'GITHUB_WORKFLOW_REF', 'GITHUB_REF'):
            with self.assertRaises(qa.QAError): qa.require_cloud_main({**env, key: 'PRIVATE'})
        args = ['--producer-json', str(self.root / 'PRIVATE.json'), '--archive-run-id', '12345',
            '--date-folder', '261002', '--expected-reports', '2', '--source-ordinal', '1', '--page', '2',
            '--output-dir', str(self.root / 'encrypted')]
        with patch.dict('os.environ', {**env, 'RECIPIENT_CERT_PEM': 'https://PRIVATE.invalid'}, clear=True), \
                patch.object(archive, 'restore_originals', side_effect=AssertionError('No R2 GET')) as restore, \
                patch('builtins.print') as printed:
            self.assertEqual(qa.main(args), 2)
        restore.assert_not_called(); self.assertNotIn('PRIVATE', str(printed.call_args_list))

    def test_workflow_exports_only_ciphertext_and_sanitized_summary(self):
        text = (Path(__file__).resolve().parents[1] / qa.WORKFLOW).read_text()
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", text)
        self.assertIn('recipient_cert_pem:', text)
        self.assertIn('original_source_run_id:', text)
        self.assertIn('actions: read', text)
        self.assertEqual(text.count('actions/upload-artifact@v4'), 1)
        self.assertIn('original-page.cms', text); self.assertIn('visual-qa-summary.json', text)
        for forbidden in ('DROPBOX_REFRESH_TOKEN', 'MINER_U:', 'tesseract', 'build_market_views', 'upload-dir', '**', 'PRIVATE KEY'):
            self.assertNotIn(forbidden, text)


if __name__ == '__main__':
    unittest.main()
