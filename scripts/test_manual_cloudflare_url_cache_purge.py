#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import json
import os
import sys
import unittest
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/manual_cloudflare_url_cache_purge.py"
SPEC = importlib.util.spec_from_file_location("manual_cloudflare_url_cache_purge", SCRIPT)
assert SPEC and SPEC.loader
purge = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = purge
SPEC.loader.exec_module(purge)


class FakeResponse:
    def __init__(self, payload: dict, status: int = 200) -> None:
        self.payload = json.dumps(payload).encode("utf-8")
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self, _limit: int = -1) -> bytes:
        return self.payload


class ManualCloudflareUrlCachePurgeTests(unittest.TestCase):
    def test_allowlist_is_fixed_to_canonical_host_and_priority_order(self) -> None:
        self.assertEqual(purge.CANONICAL_URLS[:2], ("https://kcdesk.com/", "https://kcdesk.com/reports/"))
        self.assertEqual(len(purge.CANONICAL_URLS), len(set(purge.CANONICAL_URLS)))
        self.assertTrue(all(url.startswith("https://kcdesk.com/") for url in purge.CANONICAL_URLS))
        self.assertTrue(all("?" not in url and "#" not in url for url in purge.CANONICAL_URLS))

    def test_default_mode_is_dry_run_and_never_opens_network(self) -> None:
        output = io.StringIO()
        with patch.object(purge.urllib.request, "urlopen") as urlopen, redirect_stdout(output):
            self.assertEqual(purge.main([]), 0)
        urlopen.assert_not_called()
        self.assertIn("mode=dry-run", output.getvalue())
        self.assertIn("No Cloudflare API request was sent.", output.getvalue())

    def test_apply_posts_only_files_after_exact_zone_lookup(self) -> None:
        requests = []

        def fake_urlopen(request, timeout):
            self.assertEqual(timeout, 30)
            requests.append(request)
            if request.get_method() == "GET":
                return FakeResponse({"success": True, "result": [{"id": "zone-123", "name": "kcdesk.com"}]})
            return FakeResponse({"success": True, "result": {"id": "purge-123"}})

        with patch.object(purge.urllib.request, "urlopen", side_effect=fake_urlopen):
            count = purge.purge_urls("secret-token")

        self.assertEqual(count, len(purge.CANONICAL_URLS))
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0].get_method(), "GET")
        self.assertIn("name=kcdesk.com", requests[0].full_url)
        self.assertEqual(requests[1].get_method(), "POST")
        self.assertTrue(requests[1].full_url.endswith("/zones/zone-123/purge_cache"))
        self.assertEqual(json.loads(requests[1].data), {"files": list(purge.CANONICAL_URLS)})
        self.assertEqual(requests[1].headers["Authorization"], "Bearer secret-token")

    def test_http_failure_reports_status_codes_and_messages_without_body_or_token(self) -> None:
        body = json.dumps(
            {"success": False, "errors": [{"code": 10000, "message": "Authentication error\nretry"}], "secret": "do-not-print"}
        ).encode("utf-8")
        error = urllib.error.HTTPError("https://api.cloudflare.invalid", 403, "Forbidden", {}, io.BytesIO(body))
        with patch.object(purge.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(purge.CloudflareFailure) as caught:
                purge.find_zone_id("secret-token")
        message = purge.format_failure(caught.exception)
        self.assertEqual(
            message,
            "cloudflare_error stage=zone_lookup http_status=403 errors=10000:Authentication error retry",
        )
        self.assertNotIn("do-not-print", message)
        self.assertNotIn("secret-token", message)
        self.assertNotIn("{", message)

    def test_apply_requires_token_before_network(self) -> None:
        stderr = io.StringIO()
        with patch.dict(os.environ, {}, clear=True), patch.object(purge.urllib.request, "urlopen") as urlopen, redirect_stderr(stderr), redirect_stdout(io.StringIO()):
            self.assertEqual(purge.main(["--mode", "apply"]), 2)
        urlopen.assert_not_called()
        self.assertEqual(stderr.getvalue().strip(), "configuration_error missing=CLOUDFLARE_API_TOKEN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
