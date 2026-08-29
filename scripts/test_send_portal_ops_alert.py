import hashlib
import hmac
import json
import unittest
from unittest import mock

import send_portal_ops_alert as alerts


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class PortalOpsAlertTests(unittest.TestCase):
    def test_relative_worker_url_uses_portal_api(self):
        self.assertEqual(
            alerts.normalize_worker_url("/api"),
            "https://portal.example.invalid/api/ops/alerts/email",
        )

    def test_signature_covers_timestamp_and_exact_body(self):
        body = b'{"subject":"test"}'
        headers = alerts.signed_headers("secret", body, 1234567890)
        expected = hmac.new(
            b"secret",
            b"1234567890." + body,
            hashlib.sha256,
        ).hexdigest()
        self.assertEqual(headers["X-Portal-Timestamp"], "1234567890")
        self.assertEqual(headers["X-Portal-Signature"], f"sha256={expected}")

    def test_payload_uses_default_and_custom_dedupe_windows(self):
        default_payload = json.loads(
            alerts.payload_bytes("Subject", "Body", "key", "warning")
        )
        custom_payload = json.loads(
            alerts.payload_bytes("Subject", "Body", "key", "warning", 168)
        )
        self.assertEqual(default_payload["dedupe_window_hours"], 24)
        self.assertEqual(custom_payload["dedupe_window_hours"], 168)

    def test_payload_rejects_out_of_range_dedupe_windows(self):
        for value in (0, 721):
            with self.subTest(value=value), self.assertRaisesRegex(
                ValueError,
                "dedupe hours must be between 1 and 720",
            ):
                alerts.payload_bytes("Subject", "Body", "key", "warning", value)

    @mock.patch("send_portal_ops_alert.urllib.request.urlopen")
    def test_send_alert_accepts_confirmed_deduplicated_response(self, urlopen):
        urlopen.return_value = FakeResponse(
            {"sent": True, "deduplicated": True, "provider": "brevo"}
        )
        result = alerts.send_alert(
            worker_base_url="https://worker.example/api",
            signing_key="secret",
            subject="Workflow failed",
            text="Open the run log.",
            dedupe_key="run:123",
            attempts=1,
        )
        self.assertTrue(result["sent"])
        request = urlopen.call_args.args[0]
        self.assertEqual(
            request.full_url,
            "https://worker.example/api/ops/alerts/email",
        )
        self.assertNotIn("secret", request.data.decode("utf-8"))
        self.assertEqual(json.loads(request.data)["dedupe_window_hours"], 24)


if __name__ == "__main__":
    unittest.main()
