"""Authorized API/R2 acquisition regression tests; no browser or live service."""
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from io import BytesIO, StringIO
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
from urllib.error import HTTPError, URLError

from pypdf import PdfWriter
import reportify_pdf_grabber as grab
from reportify_result import read_result, ready_metadata, status_fields


class MissingObject(Exception):
    response = {"Error": {"Code": "NoSuchKey"}}


def pdf(pages):
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=595, height=842)
    buffer = BytesIO()
    writer.write(buffer)
    return buffer.getvalue()


def detail(pages=5, readable=True, url="https://s.reportify.cn/reports/actual.pdf?signature=secret"):
    return {"readable": readable, "resource_limit": 0,
            "main": {"render_type": "image", "url_pdf": url,
                     "meta_data": {"document_total_page": pages}}}


class ReportifyApiGrabTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.output = self.root / "report.pdf"

    def test_exact_gated_reports_stop_without_asset_or_browser_requests(self):
        for report_id, pages in (("1294129388408934400", 5), ("1256239582803005440", 6)):
            for token, code in (("", "upstream_login_required"), ("runtime-secret", "upstream_access_required")):
                with self.subTest(report_id=report_id, authenticated=bool(token)):
                    fetch = mock.Mock(return_value=json.dumps(detail(pages, False, "")).encode())
                    with self.assertRaises(grab.ReportifyUnavailable) as caught:
                        grab.grab_report(report_id, self.output, token=token, fetch=fetch)
                    self.assertEqual(caught.exception.reason, code)
                    self.assertEqual(caught.exception.metrics["expected_page_count"], pages)
                    self.assertEqual(fetch.call_count, 1)
                    self.assertFalse(self.output.exists())

    def test_top_level_denial_overrides_nested_true_and_pdf_url(self):
        value = detail(readable=False)
        value["main"].update(readable=True, resource_limit=99)
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.authorized_pdf(value, authenticated=True)
        self.assertEqual(caught.exception.reason, "upstream_access_required")

    def test_explicit_readable_full_pdf_is_not_denied_by_separate_zero_quota(self):
        data = pdf(5)
        fetch = mock.Mock(side_effect=[json.dumps(detail()).encode(), data])
        result = grab.grab_report("1294129388408934400", self.output, token="runtime-secret", fetch=fetch)
        self.assertEqual(result["page_count"], 5)
        self.assertLess(len(data), 256 * 1024)
        self.assertEqual(self.output.read_bytes(), data)
        self.assertEqual(result["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(ready_metadata(result, data)["validated"], "true")
        self.assertNotIn("signature", json.dumps(result))
        self.assertNotIn("runtime-secret", json.dumps(result))

    def test_observed_public_pdf_minus_one_limit_requires_explicit_permission(self):
        value = detail(pages=21)
        value.update(resource_limit=-1)
        value["main"].update(render_type="pdf", preview_image=None)
        self.assertEqual(grab.authorized_pdf(value, authenticated=False),
                         (value["main"]["url_pdf"], 21))
        legacy = {"main": {**value["main"], "readable": True, "resource_limit": -1}}
        self.assertEqual(grab.authorized_pdf(legacy, authenticated=False)[1], 21)
        for readable in (False, None, "true", 1):
            with self.subTest(readable=readable), self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.authorized_pdf({**value, "readable": readable}, authenticated=False)
            self.assertEqual(caught.exception.detail_code, "invalid_resource_limit")

    def test_public_pdf_minus_one_limit_still_validates_exact_full_page_count(self):
        value = detail(pages=21)
        value.update(resource_limit=-1)
        value["main"].update(render_type="pdf", preview_image=None)
        for actual in (1, 21):
            with self.subTest(actual=actual):
                data = pdf(actual)
                fetch = mock.Mock(side_effect=[json.dumps(value).encode(), data])
                if actual == 21:
                    result = grab.grab_report("1283195192727441408", self.output, fetch=fetch)
                    self.assertEqual(result["page_count"], 21)
                    self.assertEqual(self.output.read_bytes(), data)
                else:
                    with self.assertRaises(grab.ReportifyUnavailable) as caught:
                        grab.grab_report("1283195192727441408", self.output, fetch=fetch)
                    self.assertEqual(caught.exception.detail_code, "page_count_mismatch")
                    self.assertFalse(self.output.exists())

    def test_legacy_main_permission_supported_but_unknown_permission_is_not(self):
        value = detail()
        value.pop("readable")
        value.pop("resource_limit")
        value["main"]["readable"] = True
        self.assertEqual(grab.authorized_pdf(value, authenticated=True)[1], 5)
        value["main"].pop("readable")
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.authorized_pdf(value, authenticated=True)
        self.assertEqual(caught.exception.detail_code, "read_permission_unknown")

    def test_mixed_envelope_never_recovers_permission_from_main(self):
        value = detail()
        value.pop("readable")
        value["main"]["readable"] = True
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.authorized_pdf(value, authenticated=True)
        self.assertEqual(caught.exception.detail_code, "read_permission_unknown")
        for invalid in (None, "0", "-1", {}, [], True, -2, -0.5, float("inf"), float("nan")):
            with self.subTest(limit=invalid), self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.authorized_pdf({**detail(), "resource_limit": invalid}, authenticated=True)
            self.assertEqual(caught.exception.detail_code, "invalid_resource_limit")

    def test_document_metadata_page_count_outranks_legacy_main(self):
        value = detail(5)
        value["main"]["document_total_page"] = 6
        value["main"]["page_count"] = 7
        self.assertEqual(grab.expected_page_count(value), 5)
        value["main"]["meta_data"]["document_total_page"] = 5.0
        self.assertEqual(grab.expected_page_count(value), 5)

    def test_readable_image_without_full_pdf_is_unavailable_not_converted(self):
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.authorized_pdf(detail(url=""), authenticated=True)
        self.assertEqual(caught.exception.detail_code, "full_pdf_not_exposed")

    def test_authorized_missing_inline_url_uses_official_download_route(self):
        url = "https://files.reportify.cn/report/full.pdf?signature=private"
        for response in (url, {"url": url}, {"url_pdf": url}, {"download_url": url},
                         {"data": {"url": url}}, {"data": url}):
            with self.subTest(response_type=type(response).__name__):
                data = pdf(6)
                fetch = mock.Mock(side_effect=[json.dumps(detail(6, url="")).encode(),
                                              json.dumps(response).encode(), data])
                result = grab.grab_report("1256239582803005440", self.output,
                                          token="runtime-secret", fetch=fetch)
                self.assertEqual(result["page_count"], 6)
                self.assertEqual(self.output.read_bytes(), data)
                self.assertEqual(fetch.call_args_list[1].args[0],
                                 "https://api.reportify.cn/reports/1256239582803005440/download")
                self.assertEqual(fetch.call_args_list[2].args[0], url)
                self.assertNotIn("private", json.dumps(result))
                self.assertNotIn("runtime-secret", json.dumps(result))

    def test_official_download_can_return_pdf_bytes_but_preview_still_fails(self):
        for pages in (1, 5):
            with self.subTest(pages=pages):
                fetch = mock.Mock(side_effect=[json.dumps(detail(url="")).encode(), pdf(pages)])
                if pages == 5:
                    result = grab.grab_report("1294129388408934400", self.output,
                                              token="runtime-secret", fetch=fetch)
                    self.assertEqual(result["page_count"], 5)
                else:
                    with self.assertRaises(grab.ReportifyUnavailable) as caught:
                        grab.grab_report("1294129388408934400", self.output,
                                         token="runtime-secret", fetch=fetch)
                    self.assertEqual(caught.exception.detail_code, "page_count_mismatch")
                    self.assertFalse(self.output.exists())
                self.assertEqual(fetch.call_count, 2)

    def test_official_download_requires_session_and_known_page_count(self):
        for token, pages, code in (("", 5, "download_session_required"),
                                   ("runtime-secret", 0, "expected_page_count_missing")):
            with self.subTest(code=code):
                fetch = mock.Mock(return_value=json.dumps(detail(pages, url="")).encode())
                with self.assertRaises(grab.ReportifyUnavailable) as caught:
                    grab.grab_report("1294129388408934400", self.output, token=token, fetch=fetch)
                self.assertEqual(caught.exception.detail_code, code)
                self.assertEqual(fetch.call_count, 1)

    def test_official_download_rejects_unknown_ambiguous_error_or_external_urls(self):
        url = "https://files.reportify.cn/report/full.pdf"
        for payload in ({}, {"href": url}, {"url": url, "download_url": url + "?other"},
                        {"success": False, "url": url}, {"url": "https://evil.example/file.pdf"},
                        {"code": 401000, "url": url},
                        {"code": 401000, "data": {"url": url}},
                        {"readable": False, "url": url},
                        {"url": url, "data": {"status": "error", "message": "denied"}},
                        {"code": 200, "url": url}, {"status": "success", "url": url},
                        {"readable": "true", "url": url}, {"ok": 1, "url": url},
                        {"url": url, "error": {}}, {"url": url, "data": []},
                        {"data": {"url": None}}, {"url": "data:application/pdf;base64,anything"}):
            with self.subTest(payload_type=type(payload).__name__):
                fetch = mock.Mock(side_effect=[json.dumps(detail(url="")).encode(), json.dumps(payload).encode()])
                with self.assertRaises(grab.ReportifyUnavailable):
                    grab.grab_report("1294129388408934400", self.output,
                                     token="runtime-secret", fetch=fetch)
                self.assertEqual(fetch.call_count, 2)
                self.assertFalse(self.output.exists())

    def test_official_download_denial_preserves_typed_failure_without_fallback(self):
        for reason, code in (("upstream_login_required", "http_401"),
                             ("upstream_access_required", "http_403"),
                             ("upstream_unavailable", "http_429")):
            with self.subTest(code=code):
                fetch = mock.Mock(side_effect=[json.dumps(detail(url="")).encode(),
                                              grab.ReportifyUnavailable(reason, code)])
                with self.assertRaises(grab.ReportifyUnavailable) as caught:
                    grab.grab_report("1294129388408934400", self.output,
                                     token="runtime-secret", fetch=fetch)
                self.assertEqual(caught.exception.reason, reason)
                self.assertEqual(fetch.call_count, 2)
                self.assertFalse(self.output.exists())

    def test_one_page_preview_cannot_satisfy_five_or_six_page_report(self):
        for expected in (5, 6):
            fetch = mock.Mock(side_effect=[json.dumps(detail(expected)).encode(), pdf(1)])
            with self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.grab_report("1294129388408934400", self.output, fetch=fetch)
            self.assertEqual(caught.exception.reason, "invalid_pdf")
            self.assertEqual(caught.exception.metrics["page_count"], 1)
            self.assertFalse(self.output.exists())

    def test_missing_page_count_untrusted_host_and_nonpdf_fail_closed(self):
        # The current source detail uses this first-party asset host for previews;
        # a full-file URL still requires explicit API permission and parsed pages.
        first_party = detail(url="https://files.reportify.cn/report/full.pdf")
        self.assertEqual(grab.authorized_pdf(first_party, authenticated=True)[1], 5)
        for value, code in ((detail(pages=0), "expected_page_count_missing"),
                            (detail(url="https://evil.example/secret.pdf"), "invalid_asset_url"),
                            (detail(url="http://s.reportify.cn/file.pdf"), "invalid_asset_url")):
            with self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.authorized_pdf(value, authenticated=True)
            self.assertEqual(caught.exception.detail_code, code)
        for data in (b"<html>login</html>", b"%PDF-broken"):
            with self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.validate_pdf(data, 5)
            self.assertEqual(caught.exception.reason, "invalid_pdf")

    def test_current_r2_session_only_and_no_store_body_in_errors(self):
        now = datetime(2026, 9, 17, tzinfo=timezone.utc)
        for hours, expected in ((0, "runtime-secret"), (11, "runtime-secret"), (13, ""), (-1, "")):
            client = mock.Mock()
            client.get_object.return_value = {"Body": BytesIO(json.dumps({
                "token": "runtime-secret", "updated_at": (now - timedelta(hours=hours)).isoformat()}).encode())}
            self.assertEqual(grab.stored_session_token(client, "bucket", now=now), expected)
            client.get_object.assert_called_once_with(Bucket="bucket", Key="reportify-auth/session.json")
        client.get_object.side_effect = MissingObject()
        self.assertEqual(grab.stored_session_token(client, "bucket"), "")
        client.get_object.side_effect = RuntimeError("do not log runtime-secret")
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.stored_session_token(client, "bucket")
        self.assertNotIn("runtime-secret", str(caught.exception))
        self.assertEqual(caught.exception.detail_code, "credential_store_unavailable")

    def test_cached_complete_pdf_is_validated_without_fetching_gated_source(self):
        client, fetch = mock.Mock(), mock.Mock(return_value=json.dumps(detail(6, False, "")).encode())
        client.get_object.return_value = {"Body": BytesIO(pdf(6))}
        result = grab.grab_report("1256239582803005440", self.output, fetch=fetch, cache_client=client)
        self.assertTrue(result["cached"])
        self.assertTrue(result["validated"])
        self.assertEqual(result["page_count"], 6)
        self.assertEqual(fetch.call_count, 1)
        client.get_object.assert_called_once_with(Bucket="portal-suite-pdfs", Key="reportify/1256239582803005440.pdf")
        client.delete_object.assert_not_called()

    def test_cached_preview_is_neither_approved_nor_deleted(self):
        client, fetch = mock.Mock(), mock.Mock(return_value=json.dumps(detail(6, False, "")).encode())
        client.get_object.return_value = {"Body": BytesIO(pdf(1))}
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.grab_report("1256239582803005440", self.output, fetch=fetch, cache_client=client)
        self.assertEqual(caught.exception.reason, "invalid_pdf")
        self.assertEqual(fetch.call_count, 1)
        client.delete_object.assert_not_called()
        self.assertFalse(self.output.exists())

    def test_missing_cache_still_obeys_upstream_permission(self):
        client, fetch = mock.Mock(), mock.Mock(return_value=json.dumps(detail(5, False, "")).encode())
        client.get_object.side_effect = MissingObject()
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.grab_report("1294129388408934400", self.output, fetch=fetch, cache_client=client)
        self.assertEqual(caught.exception.reason, "upstream_login_required")
        self.assertEqual(fetch.call_count, 1)

    def test_credentials_not_forwarded_to_cdn_or_redirect_destination(self):
        opener = mock.Mock()
        opener.open.side_effect = [HTTPError("https://api.reportify.cn/start", 302, "redirect", {
            "Location": "https://s.reportify.cn/report.pdf?signature=secret"}, BytesIO()), BytesIO(pdf(1))]
        with mock.patch.object(grab, "build_opener", return_value=opener):
            grab.fetch_bytes("https://api.reportify.cn/start", token="runtime-secret", cookie="session=cookie-secret",
                             maximum=10000, accept="application/pdf")
        first, second = [call.args[0] for call in opener.open.call_args_list]
        self.assertEqual(first.get_header("Authorization"), "Bearer runtime-secret")
        self.assertIsNone(second.get_header("Authorization"))
        self.assertIsNone(second.get_header("Cookie"))

    def test_redirect_to_untrusted_host_and_provider_failure_have_safe_codes(self):
        opener = mock.Mock()
        opener.open.side_effect = HTTPError("https://api.reportify.cn/start", 302, "redirect", {
            "Location": "https://evil.example/runtime-secret"}, BytesIO())
        with mock.patch.object(grab, "build_opener", return_value=opener):
            with self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.fetch_bytes("https://api.reportify.cn/start", token="runtime-secret", maximum=100, accept="application/json")
        self.assertEqual(caught.exception.detail_code, "invalid_asset_url")
        self.assertEqual(opener.open.call_count, 1)
        opener.open.side_effect = URLError("signed-url-and-token-secret")
        with mock.patch.object(grab, "build_opener", return_value=opener):
            with self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.fetch_bytes("https://api.reportify.cn/start", maximum=100, accept="application/json")
        self.assertNotIn("secret", str(caught.exception))

    def test_result_binding_and_typed_failure_status(self):
        data = pdf(5)
        fetch = mock.Mock(side_effect=[json.dumps(detail()).encode(), data])
        result = grab.grab_report("1294129388408934400", self.output, fetch=fetch)
        path = self.root / "result.json"
        grab.write_result(path, result)
        self.assertEqual(read_result(path, result["id"]), result)
        with self.assertRaises(ValueError):
            read_result(path, "1256239582803005440")
        with self.assertRaises(ValueError):
            ready_metadata(result, pdf(1))
        self.assertEqual(status_fields("ready", result)["page_count"], 5)
        with self.assertRaises(ValueError):
            status_fields("ready", None)
        failed = {"status": "failed", "reason": "upstream_access_required", "message": "private secret",
                  "detail_code": "full_report_not_authorized", "expected_page_count": 5}
        fields = status_fields("failed", failed)
        self.assertEqual(fields["reason"], "upstream_access_required")
        self.assertNotIn("private secret", json.dumps(fields))
        self.assertEqual(status_fields("failed", result)["reason"], "upstream_unavailable")

    def test_cli_failure_sidecar_is_typed_and_contains_no_secret(self):
        path = self.root / "result.json"
        args = ["grab", "--url", "https://reportify.cn/reports/1294129388408934400", "--output", str(self.output),
                "--result-json", str(path), "--auth-token", "runtime-secret", "--headless"]
        stdout = StringIO()
        with mock.patch("sys.argv", args), redirect_stdout(stdout), mock.patch.object(grab, "grab_report", side_effect=
                grab.ReportifyUnavailable("upstream_access_required", "full_report_not_authorized", expected_page_count=5)):
            self.assertEqual(grab.main(), 2)
        self.assertEqual(json.loads(path.read_text())["error_code"], "upstream_access_required")
        self.assertNotIn("runtime-secret", stdout.getvalue() + path.read_text())

    def test_upload_reads_back_verified_metadata_and_size(self):
        import upload_reportify_pdf_to_r2 as upload
        data = pdf(5)
        result = grab.grab_report("1294129388408934400", self.output,
                                 fetch=mock.Mock(side_effect=[json.dumps(detail()).encode(), data]))
        sidecar = self.root / "result.json"
        grab.write_result(sidecar, result)
        metadata = {**ready_metadata(result, data), "sha256": result["sha256"]}
        client = mock.Mock()
        client.head_object.return_value = {"ContentLength": len(data), "Metadata": metadata}
        args = ["upload", "--id", result["id"], "--pdf", str(self.output), "--result-json", str(sidecar)]
        with mock.patch("sys.argv", args), mock.patch.object(upload, "build_r2_client", return_value=client), redirect_stdout(StringIO()):
            self.assertEqual(upload.main(), 0)
        self.assertEqual(client.upload_fileobj.call_args.kwargs["ExtraArgs"]["Metadata"], metadata)
        client.head_object.assert_called_once()
        client.head_object.return_value["ContentLength"] = 1
        with mock.patch("sys.argv", args), mock.patch.object(upload, "build_r2_client", return_value=client):
            with self.assertRaisesRegex(RuntimeError, "readback"):
                upload.main()

    def test_transport_escaped_first_party_urls_are_normalized(self):
        url = "https://files.reportify.cn/report/full.pdf?first=1&signature=private"
        variants = [url, json.dumps(url), json.dumps(json.dumps(url)),
                    url.replace("/", "\\/"), url.replace("&", "&amp;"),
                    url.replace("&", "\\u0026").replace("=", "\\u003d")]
        for variant in variants:
            with self.subTest(encoding=variants.index(variant)):
                self.assertEqual(grab.authorized_pdf(detail(url=variant), authenticated=True)[0], url)
                opener = mock.Mock()
                opener.open.return_value = BytesIO(pdf(5))
                with mock.patch.object(grab, "build_opener", return_value=opener):
                    grab.fetch_bytes(variant, maximum=10000, accept="application/pdf")
                self.assertEqual(opener.open.call_args.args[0].full_url, url)

    def test_asset_failure_diagnostics_never_include_path_query_or_userinfo(self):
        value = detail(url="https://user:private@cdn.example.test/private-path/report.pdf?signature=secret")
        with self.assertRaises(grab.ReportifyUnavailable) as caught:
            grab.authorized_pdf(value, authenticated=True)
        metrics = caught.exception.metrics
        self.assertEqual(metrics["asset_host"], "cdn.example.test")
        self.assertEqual(metrics["asset_stage"], "detail_pdf")
        self.assertEqual(metrics["asset_scheme"], "https")
        safe = json.dumps(metrics)
        for secret in ("private", "signature", "secret", "report.pdf", "user"):
            self.assertNotIn(secret, safe)
        fields = status_fields("failed", {"status": "failed", "reason": "upstream_unavailable", **metrics})
        self.assertEqual(fields["asset_host"], "cdn.example.test")
        self.assertNotIn("asset_host", status_fields("failed", {"asset_host": "private/path?secret"}))

    def test_transient_http_and_connection_failures_retry_with_bounds(self):
        for failure in (lambda: HTTPError("https://api.reportify.cn/report", 429, "private", {}, BytesIO()),
                        lambda: URLError("private signed query")):
            opener = mock.Mock()
            opener.open.side_effect = [failure(), failure(), BytesIO(pdf(1))]
            with mock.patch.object(grab, "build_opener", return_value=opener), mock.patch.object(grab.time, "sleep") as sleep:
                self.assertTrue(grab.fetch_bytes("https://api.reportify.cn/report", maximum=10000,
                                               accept="application/pdf").startswith(b"%PDF-"))
            self.assertEqual(opener.open.call_count, 3)
            self.assertEqual([call.args[0] for call in sleep.call_args_list], list(grab.RETRY_DELAYS))
        opener.open.side_effect = URLError("private")
        with mock.patch.object(grab, "build_opener", return_value=opener), mock.patch.object(grab.time, "sleep"):
            opener.open.reset_mock()
            with self.assertRaises(grab.ReportifyUnavailable) as caught:
                grab.fetch_bytes("https://api.reportify.cn/report", maximum=100, accept="application/json")
        self.assertEqual(caught.exception.detail_code, "request_failed")
        self.assertEqual(opener.open.call_count, 3)

    def test_auth_denial_is_not_retried_and_token_excludes_historical_cookie(self):
        opener = mock.Mock()
        opener.open.side_effect = HTTPError("https://api.reportify.cn/report", 403, "private", {}, BytesIO())
        with mock.patch.object(grab, "build_opener", return_value=opener), mock.patch.object(grab.time, "sleep") as sleep:
            with self.assertRaises(grab.ReportifyUnavailable):
                grab.fetch_bytes("https://api.reportify.cn/report", token="current-token", cookie="old-cookie",
                                 maximum=100, accept="application/json")
        self.assertEqual(opener.open.call_count, 1)
        sleep.assert_not_called()
        request = opener.open.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer current-token")
        self.assertIsNone(request.get_header("Cookie"))

    def test_detail_and_official_download_use_same_new_account_without_old_cookie(self):
        for inline_url in ("https://files.reportify.cn/report/full.pdf", ""):
            opener = mock.Mock()
            opener.open.side_effect = [BytesIO(json.dumps(detail(56, url=inline_url)).encode()), BytesIO(pdf(56))]
            with mock.patch.object(grab, "build_opener", return_value=opener):
                result = grab.grab_report("1300546606747226112", self.output, token="new-token",
                                          cookie="old-cookie", fetch=grab.fetch_bytes)
            self.assertEqual(result["page_count"], 56)
            requests = [call.args[0] for call in opener.open.call_args_list]
            for request in requests:
                self.assertIsNone(request.get_header("Cookie"))
                expected_auth = "Bearer new-token" if request.host == "api.reportify.cn" else None
                self.assertEqual(request.get_header("Authorization"), expected_auth)
            if not inline_url:
                self.assertTrue(requests[1].full_url.endswith("/reports/1300546606747226112/download"))

    def test_observed_official_cos_download_returns_all_56_pages_without_credentials(self):
        url = "https://reportify-1252068037.cos.ap-beijing.myqcloud.com/reports/full.pdf?signature=private"
        opener = mock.Mock()
        opener.open.side_effect = [BytesIO(json.dumps(detail(56, url="")).encode()),
                                  BytesIO(json.dumps({"url": url}).encode()), BytesIO(pdf(56))]
        with mock.patch.object(grab, "build_opener", return_value=opener):
            result = grab.grab_report("1300546606747226112", self.output, token="new-token",
                                      cookie="old-cookie", fetch=grab.fetch_bytes)
        self.assertEqual(result["page_count"], 56)
        self.assertEqual(grab.validate_pdf(self.output.read_bytes(), 56), 56)
        requests = [call.args[0] for call in opener.open.call_args_list]
        self.assertEqual(requests[-1].full_url, url)
        self.assertIsNone(requests[-1].get_header("Authorization"))
        self.assertIsNone(requests[-1].get_header("Cookie"))
        self.assertNotIn("signature", json.dumps(result))
        for host in ("other-1252068037.cos.ap-beijing.myqcloud.com", "cos.ap-beijing.myqcloud.com",
                     "reportify-1252068037.cos.ap-beijing.myqcloud.com.evil.example"):
            self.assertFalse(grab.allowed_asset_url("https://" + host + "/full.pdf"))

    def test_new_r2_session_does_not_mix_in_historical_cookie(self):
        args = ["grab", "--url", "https://reportify.cn/reports/1300546606747226112", "--output", str(self.output),
                "--session-from-r2", "--cookie-header", "old-cookie"]
        result = {"id": "1300546606747226112", "status": "ready", "reason": ""}
        with mock.patch("sys.argv", args), redirect_stdout(StringIO()), mock.patch.object(grab, "runtime_r2_client"), \
                mock.patch.object(grab, "stored_session_token", return_value="new-token"), \
                mock.patch.object(grab, "grab_report", return_value=result) as acquire:
            self.assertEqual(grab.main(), 0)
        self.assertEqual(acquire.call_args.kwargs["token"], "new-token")
        self.assertEqual(acquire.call_args.kwargs["cookie"], "")

    def test_workflow_reads_r2_session_and_never_dispatches_or_launches_browser(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/reportify-grab.yml").read_text()
        self.assertIn("--session-from-r2", workflow)
        self.assertNotIn("client_payload.reportify_token", workflow)
        self.assertNotIn("playwright", workflow)
        self.assertNotIn("chromium", workflow)
        self.assertIn("--result-json", workflow)
        source = Path(grab.__file__).read_text()
        self.assertNotIn("sync_playwright", source)
        self.assertNotIn("page.pdf(", source)


if __name__ == "__main__":
    unittest.main()
