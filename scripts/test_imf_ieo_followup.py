"""Offline IEO source binding, section discovery, bounded HTTP and real PDF checks."""
import copy
from dataclasses import replace
import hashlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

import imf_ieo_followup as f
from imf_elibrary_resolver import SourceIdentity

EVALUATION = "IMF Advice on Fiscal Policy"
TITLE = "Implementation Plan in Response to the Board-Endorsed Recommendations from the IEO Evaluation on " + EVALUATION
LANDING = "https://ieo.imf.org/en/evaluations/completed/2025-1216-imf-advice-on-fiscal-policy"
PDF_URL = "https://ieo.imf.org/-/media/ieo/files/evaluations/follow-up/fp-mip.pdf"
IDENTITY = SourceIdentity(guid="synthetic-guid", source_url="https://www.imf.org/en/publications/policy-papers/issues/2026/10/08/synthetic-plan",
                         title=TITLE, published="2026-10-09T04:00:00+00:00", doi="10.5089/9798229064200.007",
                         isbn="9798229064200", series=("Policy Papers",), year="2026", issue="047",
                         original_language=None, source_binding_sha256="1"*64, preview_sha256="2"*64)


def directory():
    return f'<html><a href="{LANDING}">{EVALUATION}</a></html>'.encode()


def landing(*, title=TITLE, pdf_url=PDF_URL, section="Follow-up by the IMF"):
    # Matches the official streamed accordion structure, including icon links.
    return (f'<html><h1>{EVALUATION}</h1><li class="doc-view-section panel">'
            f'<h2><button>{section}<img alt=""/></button></h2><a href="{pdf_url}"><img alt=""/></a>'
            f'<a href="{pdf_url}"><span>{title}</span></a></li></html>').encode()


def pdf_bytes(title=TITLE, *, encrypted=False):
    writer = PdfWriter(); page = writer.add_blank_page(width=612, height=792)
    font = DictionaryObject({NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"),
                             NameObject("/BaseFont"): NameObject("/Helvetica")})
    page[NameObject("/Resources")] = DictionaryObject({NameObject("/Font"): DictionaryObject({NameObject("/F1"): writer._add_object(font)})})
    stream = DecodedStreamObject()
    safe = title.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    stream.set_data(("BT /F1 8 Tf 20 700 Td (" + safe + ") Tj ET").encode())
    page[NameObject("/Contents")] = writer._add_object(stream)
    if encrypted:
        writer.encrypt("test-only-password")
    output = io.BytesIO(); writer.write(output)
    return output.getvalue()


class Response:
    def __init__(self, url, data, status=200):
        self.url, self.data, self.status_code, self.closed = url, data, status, False
    def iter_content(self, size):
        for offset in range(0, len(self.data), size):
            yield self.data[offset:offset+size]
    def close(self): self.closed = True


class FollowupTests(unittest.TestCase):
    def run_download(self, folder, *, identity=IDENTITY, pages=None, max_bytes=f.MAX_PDF, timeout=20):
        responses = pages or [Response(f.DIRECTORY_URL, directory()), Response(LANDING, landing()), Response(PDF_URL, pdf_bytes())]
        session = Mock(); session.get.side_effect = responses
        proof = f.download_followup(identity, session, folder/'original.pdf', max_bytes, timeout)
        return proof, session, responses

    def test_exact_official_chain_has_three_gets_full_proof_and_real_pdf(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); proof, session, responses = self.run_download(root)
            f.validate_receipt(proof)
            self.assertEqual(set(proof), f.PROOF_FIELDS)
            self.assertEqual(proof['sha256'], hashlib.sha256((root/'original.pdf').read_bytes()).hexdigest())
            self.assertEqual((proof['pages'], proof['title'], proof['doi']), (1, TITLE, IDENTITY.doi))
            self.assertEqual([call.args[0] for call in session.get.call_args_list], [f.DIRECTORY_URL, LANDING, PDF_URL])
            self.assertTrue(all(r.closed for r in responses))
            self.assertTrue(all(call.kwargs == dict(timeout=(10, 20), allow_redirects=False, stream=True)
                                for call in session.get.call_args_list))
            self.assertFalse(list(root.glob('.imf-ieo-original-*')))
            self.assertNotIn('crossref_sha256', proof)

    def test_different_or_ambiguous_evaluation_is_rejected(self):
        for raw in (b'<a href="/en/evaluations/completed/other">Different evaluation</a>',
                    directory()+directory().replace(b'2025-1216', b'2025-1217'),
                    directory().replace(b'https://ieo.imf.org', b'https://ieo.imf.org.evil.invalid')):
            with self.subTest(raw=raw), self.assertRaises(f.FollowupError):
                f.select_evaluation(raw, TITLE)
        self.assertEqual(f.select_evaluation(directory()+directory(), TITLE), LANDING)

    def test_only_same_full_title_in_followup_section_is_selected(self):
        self.assertEqual(f.select_followup(landing(), LANDING, TITLE), PDF_URL)
        for raw in (landing(title=EVALUATION), landing(title=TITLE+' Annex'), landing(section='Full Report by Sections'),
                    landing(section='Background Papers'), landing().replace(b'<h1>', b'<h1>Different '),
                    landing()+landing(), landing(pdf_url=PDF_URL.replace('fp-mip', 'other'))+landing()):
            with self.subTest(raw=raw), self.assertRaises(f.FollowupError):
                f.select_followup(raw, LANDING, TITLE)
        # A matching citation outside the official follow-up section cannot admit it.
        with self.assertRaises(f.FollowupError):
            f.select_followup(landing(title='Different paper')+f'<a href="{PDF_URL}">{TITLE}</a>'.encode(), LANDING, TITLE)

    def test_url_scope_rejects_credentials_redirect_hosts_paths_and_non_followup_assets(self):
        for value in (PDF_URL.replace('https:', 'http:'), PDF_URL.replace('ieo.imf.org', 'ieo.imf.org.evil.invalid'),
                      PDF_URL.replace('ieo.imf.org', 'u@ieo.imf.org'), PDF_URL.replace('ieo.imf.org', '@ieo.imf.org'),
                      PDF_URL+'?download=1', PDF_URL+'#part', PDF_URL.replace('follow-up', 'background'),
                      PDF_URL.replace('fp-mip', '../fp-mip'), PDF_URL.replace('fp-mip', '%66p-mip')):
            with self.subTest(value=value), self.assertRaises(f.FollowupError):
                f.select_followup(landing(pdf_url=value), LANDING, TITLE)

    def test_invalid_or_unrelated_source_stops_before_http(self):
        invalid = [replace(IDENTITY, title=EVALUATION), replace(IDENTITY, title='IEO report '+TITLE),
                   replace(IDENTITY, source_url='https://www.imf.org/en/publications/wp/report'),
                   replace(IDENTITY, published='2026-10-09'), replace(IDENTITY, doi=IDENTITY.doi.replace('.007','.019')),
                   replace(IDENTITY, source_binding_sha256='bad'), replace(IDENTITY, preview_sha256='bad')]
        with tempfile.TemporaryDirectory() as folder:
            for identity in invalid:
                session=Mock()
                with self.subTest(identity=identity), self.assertRaises(f.FollowupError):
                    f.download_followup(identity, session, Path(folder)/'original.pdf', f.MAX_PDF, 20)
                session.get.assert_not_called()

    def test_no_retry_and_no_file_for_non200_redirect_network_or_oversize(self):
        for stage in range(3):
            for error in ('http', 'redirect', 'oversize', 'network'):
                responses=[Response(f.DIRECTORY_URL,directory()), Response(LANDING,landing()), Response(PDF_URL,pdf_bytes())]
                if error=='http': responses[stage].status_code=404
                elif error=='redirect': responses[stage].url='https://evil.invalid/secret'
                elif error=='oversize': responses[stage].data=b'x'*(f.MAX_HTML+1)
                else:responses[stage]=TimeoutError('SECRET credential URL')
                session=Mock();session.get.side_effect=responses
                with self.subTest(stage=stage,error=error), tempfile.TemporaryDirectory() as folder:
                    with self.assertRaises(f.FollowupError) as failure:
                        f.download_followup(IDENTITY,session,Path(folder)/'original.pdf',f.MAX_HTML,20)
                    self.assertNotIn('SECRET',str(failure.exception))
                    self.assertEqual(session.get.call_count,stage+1)
                    self.assertFalse(list(Path(folder).iterdir()))

    def test_pdf_requires_signature_real_pages_and_complete_contiguous_title(self):
        for data in (b'<html>'+TITLE.encode(), b'%PDF-not-a-real-pdf', pdf_bytes(EVALUATION),
                     pdf_bytes(TITLE.replace('Fiscal','Monetary')), pdf_bytes(TITLE,encrypted=True)):
            with self.subTest(digest=hashlib.sha256(data).hexdigest()), self.assertRaises(f.FollowupError):
                f.verify_pdf(data,TITLE,f.MAX_PDF)
        with self.assertRaises(f.FollowupError):f.verify_pdf(pdf_bytes(),TITLE,5)

    def test_http_status_is_strict_public_metadata_without_request_retry(self):
        for stage in range(3):
            for status in (403, 401, 429, 500, 302, True, "403", 403.0, None, 99, 600):
                responses = [Response(f.DIRECTORY_URL, directory()), Response(LANDING, landing()),
                             Response(PDF_URL, pdf_bytes())]
                responses[stage].status_code = status
                session = Mock(); session.get.side_effect = responses
                with self.subTest(stage=stage, status=status), tempfile.TemporaryDirectory() as folder:
                    with self.assertRaises(f.FollowupError) as caught:
                        f.download_followup(IDENTITY, session, Path(folder)/'original.pdf', f.MAX_PDF, 20)
                    error = caught.exception
                    expected = status if type(status) is int and 100 <= status <= 599 else None
                    self.assertEqual(error.http_status, expected)
                    self.assertEqual(str(error), 'ieo_followup_http_rejected')
                    self.assertEqual(session.get.call_count, stage + 1)
                    self.assertTrue(all(response.closed for response in responses[:stage+1]))
                    self.assertFalse(list(Path(folder).iterdir()))

    def test_non_http_failures_cannot_claim_a_status_or_expose_exception_text(self):
        for category in ('ieo_followup_request_failed', 'ieo_followup_redirect_rejected',
                         'ieo_followup_pdf_title_mismatch', 'SECRET unexpected category'):
            error = f.FollowupError(category, http_status=403)
            self.assertIsNone(error.http_status)
            self.assertNotIn('SECRET', str(error))
        session = Mock(); session.get.side_effect = TimeoutError('SECRET HTTP 403 endpoint')
        with self.assertRaises(f.FollowupError) as caught:
            f._read(session, f.DIRECTORY_URL, f.MAX_HTML, 20)
        self.assertIsNone(caught.exception.http_status)
        self.assertEqual(str(caught.exception), 'ieo_followup_request_failed')
        session.get.assert_called_once()

    def test_receipt_requires_every_field_strict_types_and_no_unknown_claims(self):
        with tempfile.TemporaryDirectory() as folder:proof,_,_=self.run_download(Path(folder))
        for field in proof:
            bad=copy.deepcopy(proof);del bad[field]
            with self.subTest(missing=field), self.assertRaises(f.FollowupError):f.validate_receipt(bad)
        changes=[('schema',True),('bytes',True),('pages',0),('pdf_status',True),('landing_status',302),
                 ('directory_status',403),('source_identity_verified',1),('sha256','X'*64),
                 ('transport','existing_subscription_vless_browser'),('crossref_sha256','1'*64)]
        for key,value in changes:
            with self.subTest(key=key),self.assertRaises(f.FollowupError):f.validate_receipt(dict(proof,**{key:value}))

    def test_destination_and_atomic_write_preserve_existing_original(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);dest=root/'original.pdf';dest.write_bytes(b'prior')
            session=Mock()
            with self.assertRaises(f.FollowupError):f.download_followup(IDENTITY,session,dest,f.MAX_PDF,20)
            session.get.assert_not_called();self.assertEqual(dest.read_bytes(),b'prior')
            dest.unlink()
            with patch.object(f.os,'link',side_effect=OSError('SECRET')):
                with self.assertRaisesRegex(f.FollowupError,'ieo_followup_write_failed'):self.run_download(root)
            self.assertFalse(list(root.iterdir()))

    def test_midstream_expiry_closes_response_and_rejects_before_publication(self):
        response=Response(f.DIRECTORY_URL,directory());session=Mock();session.get.return_value=response
        with patch.object(f.time,'monotonic',side_effect=[0,31]):
            with self.assertRaisesRegex(f.FollowupError,'ieo_followup_request_timeout'):f._read(session,f.DIRECTORY_URL,f.MAX_HTML,30)
        self.assertTrue(response.closed);self.assertEqual(session.get.call_count,1)


if __name__ == '__main__':unittest.main()
