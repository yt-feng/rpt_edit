#!/usr/bin/env python3
"""Offline public-route acceptance tests; every HTTP response is simulated."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import threading
import unittest
from unittest.mock import patch

import verify_portal_locale_routes as audit


ORIGIN = "https://portal.example.invalid"


def describe(path: str, body: bytes) -> dict:
    return {"path": path, "byte_size": len(body), "sha256": hashlib.sha256(body).hexdigest()}


def fixture() -> tuple[dict, dict]:
    manifest = {"schema_version": 1, "application_routes": {}}
    responses = {}
    for locale, direction in audit.LOCALES.items():
        manifest["application_routes"][locale] = {}
        for filename, page in audit.APPLICATION_PAGES.items():
            path = f"{locale}/{filename}"
            body = (
                f'<!doctype html><html lang="{locale}" dir="{direction}"><head>'
                '<meta name="robots" content="noindex,follow"></head>'
                f'<body data-page="{page}"><header>Navigation</header>'
                '<aside data-kc-locale-help>'
                f'<a data-kc-chinese-entry data-kc-chinese-equivalent hreflang="zh-Hans" href="{ORIGIN}/{filename}">中文</a>'
                f'<a data-kc-chinese-entry hreflang="zh-Hans" href="{ORIGIN}/">Chinese home</a>'
                '<span data-kc-public-account-contact>Account contact '
                '<a href="mailto:info@kcdesk.com" dir="ltr">info@kcdesk.com</a></span>'
                '<p data-kc-locale-error hidden></p></aside>'
                '<main><section>Application</section></main></body></html>'
            ).encode()
            manifest["application_routes"][locale][filename] = describe(path, body)
            responses[ORIGIN + "/" + path] = (200, {"Content-Language": locale}, body)
    asset = b'(() => { "use strict"; })();\n'
    manifest["recovery_asset"] = describe(audit.RECOVERY_PATH, asset)
    responses[ORIGIN + "/" + audit.RECOVERY_PATH] = (200, {}, asset)
    return manifest, responses


class PublicLocaleRouteTests(unittest.TestCase):
    def setUp(self):
        self.manifest, self.responses = fixture()
        self.calls = []

    def fetch(self, url, timeout):
        self.calls.append((url, timeout))
        self.assertIn(url, self.responses, "Only declared exact public routes may be fetched")
        self.assertEqual(timeout, 20)
        response = self.responses[url]
        if isinstance(response, Exception):
            raise response
        return response

    def verify(self):
        return audit.verify_locale_routes(self.manifest, ORIGIN, fetcher=self.fetch)

    def replace_body(self, locale, filename, transform):
        url = f"{ORIGIN}/{locale}/{filename}"
        status, headers, body = self.responses[url]
        body = transform(body.decode()).encode()
        self.responses[url] = (status, headers, body)
        self.manifest["application_routes"][locale][filename] = describe(f"{locale}/{filename}", body)

    def test_all_fifteen_shells_and_asset_pass_once(self):
        report = self.verify()
        self.assertEqual(report["status"], "passed")
        self.assertEqual((report["route_count"], report["asset_count"], report["request_count"]), (15, 1, 16))
        self.assertEqual(len(self.calls), 16)
        self.assertEqual(len(set(url for url, _ in self.calls)), 16)
        self.assertTrue(all(row["status"] == "passed" for row in report["checks"]))

    def test_declared_detail_module_is_verified_as_one_additional_exact_asset(self):
        body = b'(() => { "use strict"; /* locale detail */ })();\n'
        self.manifest["detail_asset"] = describe(audit.DETAIL_PATH, body)
        self.responses[ORIGIN + "/" + audit.DETAIL_PATH] = (200, {}, body)
        report = self.verify()
        self.assertEqual(report["status"], "passed")
        self.assertEqual((report["route_count"], report["asset_count"], report["request_count"]), (15, 2, 17))
        self.responses[ORIGIN + "/" + audit.DETAIL_PATH] = (404, {}, b"Not Found")
        self.assertEqual(self.verify()["status"], "failed")

    def test_declared_detail_module_cannot_be_null_or_an_arbitrary_url(self):
        for value in (None, describe("https://other.invalid/code.js", b"code")):
            with self.subTest(value=value):
                self.manifest["detail_asset"] = value
                with self.assertRaises(audit.RouteVerificationError):
                    self.verify()
                self.assertEqual(self.calls, [])

    def test_legacy_manifest_explicitly_skips_without_claims_or_requests(self):
        report = audit.verify_locale_routes({"schema_version": 1}, ORIGIN, fetcher=self.fetch)
        self.assertEqual(report["status"], "skipped")
        self.assertEqual(report["reason"], "legacy-manifest-without-application-routes")
        self.assertEqual((report["route_count"], report["asset_count"], report["request_count"]), (0, 0, 0))
        self.assertEqual(self.calls, [])

    def test_404_redirect_and_timeout_fail_without_retry(self):
        target = ORIGIN + "/ja/report.html"
        for response in ((404, {}, b"Not found"), (302, {"location": "https://other.invalid/"}, b""), TimeoutError()):
            with self.subTest(response=response):
                self.calls = []
                self.responses[target] = response
                report = self.verify()
                self.assertEqual(report["status"], "failed")
                self.assertEqual([url for url, _ in self.calls].count(target), 1)
                self.assertEqual(len(self.calls), 16)

    def test_200_not_found_with_matching_hash_is_not_a_valid_application(self):
        self.replace_body("ja", "report.html", lambda text: text.replace('data-page="report"', 'data-page="404"'))
        report = self.verify()
        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("page identity" in row.get("error", "") for row in report["checks"]))

    def test_wrong_hash_or_size_cannot_pass(self):
        for key, value in (("sha256", "0" * 64), ("byte_size", 5)):
            with self.subTest(key=key):
                self.manifest, self.responses = fixture()
                self.manifest["application_routes"]["ko"]["doc.html"][key] = value
                report = self.verify()
                self.assertEqual(report["status"], "failed")
                self.assertTrue(any("size/SHA-256" in row.get("error", "") for row in report["checks"]))

    def test_invalid_or_cross_origin_manifest_paths_fail_before_any_request(self):
        for path in ("https://other.invalid/ja/doc.html", "//other.invalid/doc.html", "ja/../doc.html", "ja/doc.html?token=x", "ko/doc.html"):
            with self.subTest(path=path):
                self.manifest, self.responses = fixture()
                self.manifest["application_routes"]["ja"]["doc.html"]["path"] = path
                with self.assertRaises(audit.RouteVerificationError):
                    self.verify()
                self.assertEqual(self.calls, [])

    def test_missing_doc_or_extra_shell_cannot_silently_skip(self):
        for mutation in ("missing-doc", "extra-shell", "missing-locale", "empty-routes", "null-routes", "missing-asset"):
            with self.subTest(mutation=mutation):
                self.manifest, self.responses = fixture()
                if mutation == "missing-doc": del self.manifest["application_routes"]["ar"]["doc.html"]
                if mutation == "extra-shell": self.manifest["application_routes"]["ar"]["external.html"] = {}
                if mutation == "missing-locale": del self.manifest["application_routes"]["ko"]
                if mutation == "empty-routes": self.manifest["application_routes"] = {}
                if mutation == "null-routes": self.manifest["application_routes"] = None
                if mutation == "missing-asset": del self.manifest["recovery_asset"]
                with self.assertRaises(audit.RouteVerificationError):
                    self.verify()
                self.assertEqual(self.calls, [])

    def test_chinese_equivalent_must_not_be_relocalized_or_cross_origin(self):
        for target in (ORIGIN + "/ja/doc.html", "https://other.invalid/doc.html", ORIGIN + "/doc.html?token=hidden"):
            with self.subTest(target=target):
                self.manifest, self.responses = fixture()
                self.replace_body("ja", "doc.html", lambda text: text.replace(f'href="{ORIGIN}/doc.html"', f'href="{target}"'))
                report = self.verify()
                self.assertEqual(report["status"], "failed")
                self.assertTrue(any("real non-locale root route" in row.get("error", "") for row in report["checks"]))

    def test_language_direction_noindex_and_static_help_are_required(self):
        replacements = (
            ('lang="ar"', 'lang="zh-Hans"'), ('dir="rtl"', 'dir="ltr"'),
            ('content="noindex,follow"', 'content="index,follow"'),
            ('data-kc-locale-help', 'data-unrelated-help'),
            ('mailto:info@kcdesk.com', 'mailto:other@example.invalid'),
            (f'href="{ORIGIN}/"', f'href="{ORIGIN}/ar/"'),
        )
        for before, after in replacements:
            with self.subTest(before=before):
                self.manifest, self.responses = fixture()
                self.replace_body("ar", "courses.html", lambda text: text.replace(before, after))
                self.assertEqual(self.verify()["status"], "failed")

    def test_wrong_response_language_and_recovery_asset_failure_are_detected(self):
        url = ORIGIN + "/ko/newsfeed.html"
        status, _, body = self.responses[url]
        self.responses[url] = (status, {"Content-Language": "zh-Hans"}, body)
        self.responses[ORIGIN + "/" + audit.RECOVERY_PATH] = (404, {}, b"")
        report = self.verify()
        self.assertEqual(report["status"], "failed")
        self.assertEqual(sum(row["status"] == "failed" for row in report["checks"]), 2)

    def test_footer_must_not_duplicate_the_static_help_contact(self):
        self.replace_body("ja", "report.html", lambda text: text.replace(
            "</body>", '<footer><span data-kc-public-account-contact>Duplicate contact</span></footer></body>',
        ))
        report = self.verify()
        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("email must appear once" in row.get("error", "") for row in report["checks"]))

    def test_origin_must_be_bare_https_before_any_request(self):
        for origin in ("http://portal.example.invalid", "https://name:secret@portal.example.invalid", "https://portal.example.invalid/api", "https://portal.example.invalid?x=1", "https://portal.example.invalid:443", "https://portal.example.invalid\\other"):
            with self.subTest(origin=origin), self.assertRaises(audit.RouteVerificationError):
                audit.verify_locale_routes(self.manifest, origin, fetcher=self.fetch)
        self.assertEqual(self.calls, [])

    def test_worker_count_is_bounded_to_four(self):
        lock = threading.Lock()
        ready = threading.Event()
        active = maximum = 0

        def fetcher(url, timeout):
            nonlocal active, maximum
            with lock:
                active += 1
                maximum = max(maximum, active)
                if active == 4: ready.set()
            self.assertTrue(ready.wait(timeout=2))
            with lock: active -= 1
            return self.fetch(url, timeout)

        report = audit.verify_locale_routes(self.manifest, ORIGIN, fetcher=fetcher)
        self.assertEqual(report["status"], "passed")
        self.assertEqual(maximum, 4)

    def test_fetch_wrapper_has_hard_deadline_no_redirects_and_no_retry(self):
        body = b"test"
        result = subprocess.CompletedProcess([], 0, b"HTTP/2 200\r\nContent-Language: ja\r\n\r\n" + body + b"\nKC_ROUTE_STATUS:200", b"")
        with patch.object(audit.subprocess, "run", return_value=result) as run:
            self.assertEqual(audit.fetch_public(ORIGIN + "/ja/report.html", 20), (200, {"content-language": "ja"}, body))
        args = run.call_args.args[0]
        self.assertEqual(args[args.index("--max-time") + 1], "20")
        self.assertEqual(args[args.index("--max-redirs") + 1], "0")
        self.assertNotIn("--location", args)
        self.assertNotIn("--retry", args)
        self.assertEqual(run.call_args.kwargs["timeout"], 20)
        self.assertEqual(run.call_count, 1)

    def test_cli_writes_report_and_returns_failure_without_real_requests(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = directory / "manifest.json"
            output = directory / "result.json"
            manifest.write_text(json.dumps(self.manifest))
            args = ["verify_portal_locale_routes.py", "--manifest", str(manifest), "--origin", ORIGIN, "--output", str(output)]
            with patch("sys.argv", args), patch.object(audit, "verify_locale_routes", return_value={"schema_version": 1, "status": "failed", "checks": []}), patch("builtins.print"):
                self.assertEqual(audit.main(), 1)
            self.assertEqual(json.loads(output.read_text())["status"], "failed")


if __name__ == "__main__":
    unittest.main()
