import json
import unittest
from unittest.mock import Mock, patch

import inspect_market_views_live as live


class LiveInspectionTests(unittest.TestCase):
    def setUp(self):
        self.item = {"id": "market-view:261004", "date": "2026-10-04", "filename": "market_views_261004.pdf",
                     "size_bytes": 4000, "sha256": "a" * 64}
        self.client = Mock()
        self.fetch = Mock(side_effect=[(200, "application/json", json.dumps({"items": [self.item], "total": 1}).encode()),
                                      (401, "application/json", b"{}")])

    def test_full_pair_and_public_match_do_not_claim_authenticated_download(self):
        with patch.object(live, "validate_existing_private_pair", return_value=self.item) as verify:
            result = live.inspect(self.client, "PRIVATE-bucket", ["261004"], self.fetch)
        self.assertTrue(result["success"])
        self.assertFalse(result["authenticated_download_verified"])
        self.assertEqual(result["dates"][0]["private_pdf_sha256"], "a" * 64)
        self.assertNotIn("PRIVATE", json.dumps(result))
        self.assertEqual(verify.call_args.kwargs["pdf_key"], "_market-views/pdfs/261004.pdf")
        self.client.put_object.assert_not_called()

    def test_wrong_or_duplicate_public_date_fails(self):
        for rows in ([], [dict(self.item, size_bytes=1)], [self.item, self.item]):
            with self.subTest(rows=rows), patch.object(live, "validate_existing_private_pair", return_value=self.item):
                self.fetch.side_effect = [(200, "application/json", json.dumps({"items": rows, "total": len(rows)}).encode())]
                with self.assertRaises(live.InspectionError):
                    live.inspect(self.client, "bucket", ["261004"], self.fetch)

    def test_anonymous_pdf_success_is_rejected(self):
        self.fetch.side_effect = [(200, "application/json", json.dumps({"items": [self.item], "total": 1}).encode()),
                                 (200, "application/pdf", b"%PDF-")]
        with patch.object(live, "validate_existing_private_pair", return_value=self.item), self.assertRaises(live.InspectionError):
            live.inspect(self.client, "bucket", ["261004"], self.fetch)

    def test_private_pair_failure_cannot_pass_public_match(self):
        with patch.object(live, "validate_existing_private_pair", side_effect=RuntimeError("private-invalid")), self.assertRaises(RuntimeError):
            live.inspect(self.client, "bucket", ["261004"], self.fetch)

    def test_invalid_dates_fail_before_access(self):
        for dates in ([], ["20261004"], ["261032"], ["261004", "261004"], ["261001"] * 5):
            with self.subTest(dates=dates), self.assertRaises(ValueError):
                live.inspect(self.client, "bucket", dates, self.fetch)
        self.fetch.assert_not_called()
        self.client.head_object.assert_not_called()

    def test_redirect_is_rejected(self):
        with self.assertRaises(live.InspectionError):
            live.NoRedirect().redirect_request(None, None, None, None, None, None)

    def test_invalid_configured_origin_cannot_send_a_request(self):
        for origin in ("", "http://example.invalid", "https://user:secret@example.invalid", "https://example.invalid/path"):
            with self.subTest(origin=origin), patch.dict(live.os.environ, {"PORTAL_SITE_URL": origin}), \
                    patch.object(live.urllib.request, "build_opener") as opener, self.assertRaises(live.InspectionError):
                live.get_public("/api/market-views")
            opener.assert_not_called()


if __name__ == "__main__":
    unittest.main()
