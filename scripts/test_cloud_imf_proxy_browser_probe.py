"""Offline-only contract tests: no socket, browser, subprocess or HTTP starts."""
import base64
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import cloud_imf_proxy_browser_probe as p

NODE = ("vless://00000000-0000-0000-0000-000000000001@example.invalid:443"
        "?encryption=none&type=tcp&security=reality&sni=example.invalid&fp=chrome&pbk=" + "A" * 43)


class ProbeTests(unittest.TestCase):
    def test_cloud_approval_and_workflow_are_required_before_subprocess(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(p.subprocess, "Popen") as start:
            with self.assertRaises(RuntimeError):
                p.require_approval()
            start.assert_not_called()
        env = {"GITHUB_ACTIONS": "true", "EXPLICIT_CLOUD_BROWSER_APPROVAL": "true",
               "GITHUB_REPOSITORY": "yt-feng/rpt_edit", "GITHUB_EVENT_NAME": "workflow_dispatch",
               "GITHUB_WORKFLOW_REF": f"yt-feng/rpt_edit/.github/workflows/institution-fetch-test.yml@refs/heads/{p.BRANCH}"}
        with patch.object(p.sys, "platform", "linux"), patch.dict(os.environ, env, clear=True):
            p.require_approval()
            for key in env:
                with patch.dict(os.environ, {key: "wrong"}):
                    with self.assertRaises((RuntimeError, p.ProbeFailure)):
                        p.require_approval()

    def test_unique_valid_vless_and_base64(self):
        result = p.select_outbound(NODE, lambda _: None)
        self.assertEqual((result["type"], result["network"], result["tls"]["enabled"]), ("vless", "tcp", True))
        encoded = base64.b64encode(NODE.encode()).decode()
        self.assertEqual(result, p.select_outbound(encoded, lambda x: base64.b64decode(x).decode()))

    def test_multiple_valid_or_no_supported_node_rejected(self):
        for body in (NODE + "\n" + NODE, "https://example.invalid:443", "", None):
            with self.subTest(body=bool(body)), self.assertRaises(p.ProbeFailure):
                p.select_outbound(body, lambda _: None)

    def test_unsupported_and_insecure_vless_fail_closed(self):
        for bad in (NODE + "&unknown=value", NODE + "&allowInsecure=1",
                    NODE.replace("type=tcp", "type=ws"), NODE.replace("security=reality", "security=tls")):
            with self.assertRaises(p.ProbeFailure):
                p.select_outbound(bad, lambda _: None)

    def test_node_credential_and_proxy_env_never_reach_browser(self):
        with patch.dict(os.environ, {"PATH": "/test/path", "PROXY_SUBSCRIPTION_URL": "SECRET",
                                    "HTTPS_PROXY": "SECRET", "TOKEN": "SECRET"}, clear=True):
            env = p.browser_environment("socks5h://127.0.0.1:54321")
        self.assertEqual(env["IMF_CLOUD_SOCKS_PORT"], "54321")
        self.assertEqual(set(env), {"PATH", "GITHUB_ACTIONS", "EXPLICIT_CLOUD_BROWSER_APPROVAL", "IMF_CLOUD_SOCKS_PORT"})
        self.assertNotIn("SECRET", repr(env))

    def test_listener_must_be_unauthenticated_exact_loopback(self):
        for value in ("socks5h://localhost:1234", "http://127.0.0.1:1234", "socks5h://u:p@127.0.0.1:1234",
                      "socks5h://127.0.0.1:1234/path", "socks5h://127.0.0.1:0"):
            with self.assertRaises(p.ProbeFailure):
                p.browser_environment(value)

    def test_connectivity_one_explicit_request_no_redirect_and_close(self):
        response = Mock(status_code=204)
        cffi = SimpleNamespace(get=Mock(return_value=response))
        report = p.connectivity("socks5h://127.0.0.1:5555", cffi, 10177)
        self.assertTrue(report["accepted"])
        cffi.get.assert_called_once()
        kw = cffi.get.call_args.kwargs
        self.assertEqual(kw["curl_options"], {10177: ""})
        self.assertFalse(kw["allow_redirects"])
        self.assertEqual(kw["timeout"], 8)
        self.assertEqual(set(kw["proxies"]), {"http", "https"})
        response.close.assert_called_once()

    def test_connectivity_http_and_exception_are_redacted(self):
        for error in (None, RuntimeError("SECRET URL and credentials")):
            cffi = SimpleNamespace(get=Mock(side_effect=error, return_value=Mock(status_code=403)))
            report = p.connectivity("socks5h://127.0.0.1:5555", cffi, 10177)
            self.assertFalse(report["accepted"])
            self.assertEqual(report["status"], None if error else 403)
            self.assertNotIn("SECRET", repr(report))
            cffi.get.assert_called_once()

    def test_browser_timeout_stops_group_before_return(self):
        proc = Mock(pid=123, poll=Mock(return_value=None))
        proc.wait.side_effect = [subprocess.TimeoutExpired("not printed", 150), 143]
        with patch.object(p.subprocess, "Popen", return_value=proc), patch.object(p.os, "killpg") as stop:
            with self.assertRaisesRegex(p.ProbeFailure, "browser_process_timeout"):
                p.run_browser("socks5h://127.0.0.1:5555")
        stop.assert_called_once_with(123, p.signal.SIGTERM)

    def test_browser_interruption_escalates_cleanup_without_retry(self):
        proc = Mock(pid=123, poll=Mock(return_value=None))
        proc.wait.side_effect = [KeyboardInterrupt(), subprocess.TimeoutExpired("private", 8), -9]
        with patch.object(p.subprocess, "Popen", return_value=proc) as spawn, patch.object(p.os, "killpg") as stop:
            with self.assertRaises(KeyboardInterrupt):
                p.run_browser("socks5h://127.0.0.1:5555")
        self.assertEqual([call.args[1] for call in stop.call_args_list], [p.signal.SIGTERM, p.signal.SIGKILL])
        spawn.assert_called_once()

    def test_pdf_requires_exact_bytes_pages_and_identity(self):
        data = b"%PDF-test-fixture"
        digest = hashlib.sha256(data).hexdigest()
        good_page = SimpleNamespace(extract_text=lambda: "Estonia Consumer Price Index 2026")
        good = SimpleNamespace(is_encrypted=False, pages=[good_page] * 14)
        with tempfile.TemporaryDirectory() as folder, patch.object(p, "SHA", digest), patch.object(p, "SIZE", len(data)):
            path = Path(folder) / f"{digest}.pdf"
            path.write_bytes(data)
            self.assertTrue(p.verify_pdf(Path(folder), lambda _: good)["source_identity_match"])
            for bad in (SimpleNamespace(is_encrypted=True, pages=good.pages),
                        SimpleNamespace(is_encrypted=False, pages=good.pages[:13]),
                        SimpleNamespace(is_encrypted=False, pages=[SimpleNamespace(extract_text=lambda: "Other report")] * 14)):
                with self.assertRaises(p.ProbeFailure):
                    p.verify_pdf(Path(folder), lambda _: bad)
            path.write_bytes(data[:-1] + b"x")
            with self.assertRaisesRegex(p.ProbeFailure, "pdf_bytes_mismatch"):
                p.verify_pdf(Path(folder), lambda _: good)

    def test_browser_source_has_no_stealth_or_session_export_and_forces_proxy(self):
        code = (Path(__file__).parent / "cloud_imf_browser_probe.cjs").read_text()
        self.assertIn("proxy: {server: `socks5://127.0.0.1:${port}`}" , code)
        self.assertIn("headless: false", code)
        self.assertIn("download.url() !== PDF", code)
        for forbidden in ("executablePath:", "userAgent:", "storageState(", "addInitScript(", "newCDPSession("):
            self.assertNotIn(forbidden, code)

    def test_async_render_wait_stays_within_single_navigation(self):
        code = (Path(__file__).parent / "cloud_imf_browser_probe.cjs").read_text()
        self.assertEqual(code.count("page.goto("), 1)
        self.assertNotIn("page.reload(", code)
        self.assertEqual(code.count('waitFor({state: "visible", timeout: 15000})'), 2)
        self.assertIn('report.initial_human_verification_title =', code)
        self.assertIn('report.final_human_verification_title =', code)
        self.assertNotIn('throw new Error("human_verification_required")', code)
        self.assertIn('report.final_navigation_status = response.status()', code)


if __name__ == "__main__":
    unittest.main()
