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
    def test_recovered_wechat_success_is_separate_from_translation_runner_failure(self):
        text = alerts.workflow_alert_text("Daily report articles and translations",
            "shards=failure, recovered_articles=success, recovered_article_count=54, "
            "wechat_enabled=true, wechat_source=xhs_notes, wechat=skipped, "
            "delivery_gate=success, market_source_recovery=success, recovery_source_kind=mineru-recovery, "
            "ocr_page_source_recovery=skipped, translation_requested=all, translation_shards=failure, translated=skipped", {})
        self.assertIn("已通过恢复链路完成草稿投递与回读验证（54 篇）", text)
        self.assertIn("Market Views：已验证交付", text)
        self.assertIn("报告全文翻译：分片未全部完成", text)
        self.assertIn("本次恢复未使用 OCR", text)
        self.assertNotIn("已经依次尝试", text)

    def test_generated_recovery_without_enabled_upload_is_not_delivery(self):
        for extra in ("wechat_enabled=false", "", "wechat_enabled=true, wechat_source=portal_translated"):
            with self.subTest(extra=extra):
                text = alerts.workflow_alert_text("Daily report articles and translations",
                    "recovered_articles=success, recovered_article_count=54, " + extra, {})
                self.assertNotIn("已通过恢复链路完成草稿投递", text)

    def test_ocr_source_success_does_not_claim_articles_delivered(self):
        text = alerts.workflow_alert_text("Daily report articles and translations",
            "market_source_recovery=success, recovery_source_kind=ocr-synthesis, "
            "recovered_articles=failure, wechat_enabled=true, wechat_source=xhs_notes, translation_requested=0", {})
        self.assertIn("OCR 来源已就绪", text)
        self.assertIn("尚未确认完成草稿交付", text)
        self.assertIn("报告全文翻译：本次未启用", text)

    def test_unrelated_workflow_does_not_claim_wechat_or_api_failure(self):
        text = alerts.workflow_alert_text("Institution latest PDF to WeChat", "build=failure, wechat=skipped", {})
        self.assertIn("未完成的步骤：build", text)
        self.assertNotIn("微信文章自动任务未成功", text)
        self.assertNotIn("已经依次尝试", text)

    def test_empty_selection_does_not_claim_new_delivery(self):
        text = alerts.workflow_alert_text("Daily report articles and translations",
            "no_work=true, selected_count=0, delivery_gate=success, wechat_enabled=true", {})
        self.assertIn("本次无新增来源", text)
        self.assertNotIn("已验证交付", text)

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
