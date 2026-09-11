import copy
import contextlib
import io
import json
import pathlib
import sys
import tempfile
import types
import unittest
import urllib.error
from unittest import mock

import replay_course_owner_notification as replay


REQUEST_ID = "a" * 64
ATTEMPTED_AT = "2026-09-10T18:29:01.328Z"
OWNER = "owner@example.invalid"
APPLICANT = "private-applicant@example.invalid"
SENDER = {"email": "sender@example.invalid", "name": "Test Sender"}
RECORD = {
    "request_id": REQUEST_ID, "material_id": "material-02", "material_title": "原始材料标题",
    "attempted_at": ATTEMPTED_AT, "requester_email": APPLICANT,
    "message_id": "<original@provider.invalid>", "provider": "brevo", "status": "sent",
}


class S3Error(Exception):
    def __init__(self, code):
        self.response = {"Error": {"Code": code}}


class FakeS3:
    def __init__(self):
        self.objects = {f"{replay.REQUEST_PREFIX}{REQUEST_ID}.json": replay.json_bytes(RECORD)}
        self.writes = []
        self.truncated = False
        self.race = False
        self.fail_final_write = False

    def get_object(self, *, Bucket, Key):
        if Key not in self.objects:
            raise S3Error("NoSuchKey")
        return {"Body": io.BytesIO(self.objects[Key])}

    def list_objects_v2(self, *, Bucket, Prefix, MaxKeys):
        return {"Contents": [{"Key": key} for key in self.objects if key.startswith(Prefix)][:MaxKeys], "IsTruncated": self.truncated}

    def put_object(self, **kwargs):
        if kwargs.get("IfNoneMatch") == "*" and (kwargs["Key"] in self.objects or self.race):
            raise S3Error("PreconditionFailed")
        if self.fail_final_write and not kwargs.get("IfNoneMatch"):
            raise S3Error("ServiceUnavailable")
        self.writes.append(copy.deepcopy(kwargs))
        self.objects[kwargs["Key"]] = kwargs["Body"]


class FakeBrevo:
    def __init__(self, s3):
        self.s3 = s3
        self.sent = []
        self.content_reads = 0
        self.ambiguous = False
        self.events_calls = []

    def events(self, **kwargs):
        self.events_calls.append(kwargs)
        return [{"event": "delivered", "date": "2026-09-10T18:30:00Z", "email": OWNER,
                 "messageId": kwargs.get("message_id", ""), "reason": "private SMTP detail"}]

    def original_content(self, record):
        self.content_reads += 1
        return {"subject": "原始材料标题", "htmlContent": "<p>" + APPLICANT + "</p>"}

    def request(self, method, path, payload=None, **query):
        if method != "POST":
            raise AssertionError("Unexpected provider operation")
        markers = [json.loads(body) for key, body in self.s3.objects.items() if key.startswith(replay.REPLAY_PREFIX)]
        assert len(markers) == 1 and markers[0]["state"] == "sending", "Must reserve before sending"
        self.sent.append(copy.deepcopy(payload))
        if self.ambiguous:
            raise TimeoutError("private provider error and secret values")
        return {"messageId": "<new-owner-reminder@provider.invalid>"}


class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.s3 = FakeS3()
        self.provider = FakeBrevo(self.s3)

    def run_operation(self, mode="audit", **kwargs):
        return replay.run(self.s3, "private-bucket", self.provider, mode=mode, owner=OWNER, sender=SENDER,
                          material_id="material-02", attempted_at=ATTEMPTED_AT, **kwargs)

    def test_audit_reads_without_content_send_or_mutation(self):
        before = copy.deepcopy(self.s3.objects)
        summary = self.run_operation()
        self.assertTrue(summary["original_delivery"]["delivered"])
        self.assertEqual(summary["replay_state"], "not_attempted")
        self.assertEqual(self.provider.content_reads, 0)
        self.assertEqual(self.provider.sent, [])
        self.assertEqual(self.s3.objects, before)

    def test_resend_reserves_first_and_preserves_original(self):
        original = self.s3.objects[f"{replay.REQUEST_PREFIX}{REQUEST_ID}.json"]
        summary = self.run_operation("resend")
        self.assertEqual(summary["replay_state"], "accepted")
        self.assertTrue(summary["send_attempted_this_run"])
        self.assertEqual(self.s3.objects[f"{replay.REQUEST_PREFIX}{REQUEST_ID}.json"], original)
        self.assertEqual(len(self.provider.sent), 1)
        sent = self.provider.sent[0]
        self.assertEqual(sent["to"], [{"email": OWNER}])
        self.assertEqual(sent["sender"], SENDER)
        self.assertEqual(sent["subject"], "原始材料标题")
        self.assertEqual(sent["htmlContent"], "<p>" + APPLICANT + "</p>")
        self.assertNotIn("cc", sent)
        self.assertNotIn("bcc", sent)
        self.assertEqual(self.s3.writes[0]["IfNoneMatch"], "*")
        self.assertTrue(all(write["Key"].startswith(replay.REPLAY_PREFIX) for write in self.s3.writes))

    def test_repeat_is_suppressed_and_audits_original_provider_message(self):
        self.run_operation("resend")
        summary = self.run_operation("resend")
        self.assertTrue(summary["repeat_suppressed"])
        self.assertFalse(summary["send_attempted_this_run"])
        self.assertEqual(len(self.provider.sent), 1)
        self.assertEqual(self.provider.events_calls[-1]["message_id"], "<new-owner-reminder@provider.invalid>")

    def test_timeout_marks_unknown_and_repeat_never_sends_again(self):
        self.provider.ambiguous = True
        summary = self.run_operation("resend")
        self.assertEqual(summary["replay_state"], "unknown_requires_audit")
        summary = self.run_operation("resend")
        self.assertTrue(summary["repeat_suppressed"])
        self.assertEqual(len(self.provider.sent), 1)
        self.assertTrue(self.provider.events_calls[-1]["tag"].startswith("owner-replay-"))
        self.assertEqual(self.provider.events_calls[-1]["recipient"], OWNER)

    def test_failed_final_marker_write_keeps_reservation_and_prevents_duplicate(self):
        self.s3.fail_final_write = True
        with self.assertRaisesRegex(replay.ReplayError, "persist"):
            self.run_operation("resend")
        self.s3.fail_final_write = False
        summary = self.run_operation("resend")
        self.assertTrue(summary["repeat_suppressed"])
        self.assertEqual(len(self.provider.sent), 1)

    def test_concurrent_reservation_does_not_send(self):
        self.s3.race = True
        summary = self.run_operation("resend")
        self.assertEqual(summary["replay_state"], "concurrent_operation_suppressed")
        self.assertEqual(self.provider.sent, [])

    def test_refuses_applicant_as_destination(self):
        with self.assertRaisesRegex(replay.ReplayError, "differ from the applicant"):
            replay.run(self.s3, "bucket", self.provider, mode="resend", owner=APPLICANT, sender=SENDER,
                       request_id=REQUEST_ID)
        self.assertEqual(self.s3.writes, [])

    def test_rejects_recipient_lists_and_display_addresses(self):
        for invalid in ("owner@example.invalid,evil.com", "owner@example.invalid;other@example.invalid",
                        "Owner <owner@example.invalid>", "owner@example.invalid\nBcc:other@example.invalid",
                        "owner@example.invalid:secret"):
            with self.subTest(invalid=invalid), self.assertRaises(replay.ReplayError):
                replay.normalized_email(invalid)

    def test_malformed_marker_state_is_never_printed(self):
        self.run_operation("resend")
        key = next(key for key in self.s3.objects if key.startswith(replay.REPLAY_PREFIX))
        marker = json.loads(self.s3.objects[key])
        marker["state"] = APPLICANT
        self.s3.objects[key] = replay.json_bytes(marker)
        summary = self.run_operation("audit")
        self.assertEqual(summary["replay_state"], "unknown")
        self.assertNotIn(APPLICANT, json.dumps(summary))

    def test_truncated_scan_requires_exact_id(self):
        self.s3.truncated = True
        with self.assertRaisesRegex(replay.ReplayError, "scan limit"):
            self.run_operation("resend")
        record = replay.find_request(self.s3, "bucket", REQUEST_ID, "", "")
        self.assertEqual(record["request_id"], REQUEST_ID)

    def test_ambiguous_or_wrong_timestamp_selection_fails(self):
        second_id = "b" * 64
        second = {**RECORD, "request_id": second_id}
        self.s3.objects[f"{replay.REQUEST_PREFIX}{second_id}.json"] = replay.json_bytes(second)
        with self.assertRaisesRegex(replay.ReplayError, "exactly one"):
            self.run_operation("resend")
        with self.assertRaisesRegex(replay.ReplayError, "exactly one"):
            replay.find_request(self.s3, "bucket", REQUEST_ID, "material-02", "2026-09-10T18:29:01.329Z")
        self.assertEqual(self.provider.sent, [])

    def test_summary_withholds_addresses_content_ids_and_provider_errors(self):
        summary = self.run_operation("resend")
        rendered = json.dumps(summary)
        for private in (OWNER, APPLICANT, SENDER["email"], RECORD["message_id"], REQUEST_ID,
                        RECORD["material_title"], "private SMTP detail"):
            self.assertNotIn(private, rendered)

    def test_original_provider_content_checked_against_record(self):
        provider = replay.Brevo("unused")
        calls = []

        def response(method, path, payload=None, **query):
            calls.append((method, path, query))
            if path == "/smtp/emails":
                return {"transactionalEmails": [{"messageId": RECORD["message_id"], "uuid": "valid-uuid-123"}]}
            return {"subject": "材料索取：" + RECORD["material_title"],
                    "body": "<p>" + APPLICANT + "</p>", "date": ATTEMPTED_AT}

        provider.request = response
        content = provider.original_content(RECORD)
        self.assertIn(APPLICANT, content["htmlContent"])
        self.assertEqual(calls[0][2]["messageId"], RECORD["message_id"])
        with self.assertRaisesRegex(replay.ReplayError, "does not match"):
            provider.original_content({**RECORD, "requester_email": "another@example.invalid"})

    def test_provider_event_filter_keeps_only_selected_owner_and_message(self):
        provider = replay.Brevo("unused")
        provider.request = lambda *_args, **_kwargs: {"events": [
            {"messageId": RECORD["message_id"], "email": OWNER, "event": "delivered"},
            {"messageId": RECORD["message_id"], "email": APPLICANT, "event": "blocked"},
            {"messageId": "another", "email": OWNER, "event": "blocked"},
        ]}
        self.assertEqual(len(provider.events(message_id=RECORD["message_id"], recipient=OWNER)), 1)

    def test_http_errors_expose_only_allowlisted_classification(self):
        cases = [
            (401, {"code": "unauthorized", "message": "We have detected an unrecognised IP address 203.0.113.67 PRIVATE-KEY"}, "ip_not_authorized"),
            (401, {"code": "unauthorized", "message": "IP not authorized: 203.0.113.67 PRIVATE-KEY"}, "ip_not_authorized"),
            (401, {"code": "unauthorized", "message": "API Key is not enabled: PRIVATE-KEY"}, "key_invalid_or_disabled"),
            (403, {"code": "permission_denied", "message": "PRIVATE-KEY " + APPLICANT}, "permission_denied"),
            (401, {"code": "PRIVATE-KEY", "message": APPLICANT}, "authentication_failed"),
            (503, {"code": "PRIVATE-KEY", "message": APPLICANT}, "http_error"),
        ]
        for status, body, expected in cases:
            with self.subTest(status=status, expected=expected):
                provider = replay.Brevo("PRIVATE-KEY")
                error = urllib.error.HTTPError("https://api.brevo.com/v3/smtp/statistics/events", status, APPLICANT, {}, io.BytesIO(replay.json_bytes(body)))
                provider.opener.open = mock.Mock(side_effect=error)
                with self.assertRaises(replay.BrevoHTTPError) as caught:
                    provider.events(message_id=RECORD["message_id"])
                self.assertEqual(caught.exception.category, expected)
                self.assertEqual(caught.exception.status, status)
                rendered = str(caught.exception) + json.dumps(replay.safe_failure(caught.exception))
                for private in ("203.0.113.67", "PRIVATE-KEY", APPLICANT, RECORD["message_id"]):
                    self.assertNotIn(private, rendered)

    def test_http_error_body_read_is_bounded_and_invalid_payload_is_withheld(self):
        class RecordedBody(io.BytesIO):
            def __init__(self, raw):
                super().__init__(raw)
                self.sizes = []

            def read(self, size=-1):
                self.sizes.append(size)
                return super().read(size)

        for raw in (b"PRIVATE-KEY invalid-json", b"PRIVATE-KEY " * replay.MAX_ERROR_BYTES):
            body = RecordedBody(raw)
            provider = replay.Brevo("PRIVATE-KEY")
            error = urllib.error.HTTPError("https://api.brevo.com/v3/smtp/statistics/events", 401, "private", {}, body)
            provider.opener.open = mock.Mock(side_effect=error)
            with self.assertRaises(replay.BrevoHTTPError) as caught:
                provider.events(message_id=RECORD["message_id"])
            self.assertEqual(body.sizes, [replay.MAX_ERROR_BYTES + 1])
            self.assertTrue(body.closed)
            self.assertEqual(caught.exception.category, "authentication_failed")
            self.assertNotIn("PRIVATE-KEY", str(caught.exception))

    def test_cli_publishes_inventory_before_provider_401_and_exits_nonzero(self):
        environment = {
            "R2_ACCOUNT_ID": "private-account", "R2_ACCESS_KEY_ID": "private-key", "R2_SECRET_ACCESS_KEY": "private-secret",
            "R2_BUCKET": "private-bucket", "OWNER_NOTIFICATION_EMAIL": OWNER,
            "BREVO_API_KEY": "PRIVATE-KEY", "BREVO_SENDER_EMAIL": SENDER["email"], "BREVO_SENDER_NAME": SENDER["name"],
        }
        boto3 = types.SimpleNamespace(client=lambda *_args, **_kwargs: self.s3)
        config_module = types.SimpleNamespace(Config=lambda **kwargs: kwargs)
        arguments = ["replay", "--mode", "audit", "--material-id", "material-02", "--attempted-at", ATTEMPTED_AT,
                     "--inventory-start", "2026-09-03T16:00:00Z", "--inventory-end", "2026-09-11T04:00:00Z"]
        with tempfile.TemporaryDirectory() as directory:
            summary_path = pathlib.Path(directory) / "step-summary.md"
            environment["GITHUB_STEP_SUMMARY"] = str(summary_path)
            with contextlib.redirect_stdout(output := io.StringIO()), contextlib.redirect_stderr(errors := io.StringIO()):
                def blocked_request(*_args, **_kwargs):
                    # Both outputs must exist before the first provider request.
                    self.assertIn('"total_requests": 1', output.getvalue())
                    self.assertIn('"owner_request_inventory"', summary_path.read_text())
                    body = replay.json_bytes({"code": "unauthorized", "message": "Unrecognised IP address 203.0.113.67 PRIVATE-KEY " + APPLICANT})
                    raise urllib.error.HTTPError("https://api.brevo.com/v3/smtp/statistics/events", 401, "private", {}, io.BytesIO(body))

                opener = types.SimpleNamespace(open=blocked_request)
                with mock.patch.dict(sys.modules, {"boto3": boto3, "botocore.config": config_module}), \
                     mock.patch.dict(replay.os.environ, environment), \
                     mock.patch.object(sys, "argv", arguments), \
                     mock.patch.object(replay.urllib.request, "build_opener", return_value=opener):
                    self.assertEqual(replay.main(), 1)
            decoder = json.JSONDecoder()
            first, end = decoder.raw_decode(output.getvalue())
            second = json.loads(output.getvalue()[end:].strip())
            self.assertEqual(first["phase"], "inventory")
            self.assertTrue(first["owner_request_inventory"]["complete"])
            self.assertEqual(first["owner_request_inventory"]["total_requests"], 1)
            self.assertEqual(second["provider_error"], {"status": "unavailable", "http_status": 401, "category": "ip_not_authorized"})
            rendered = output.getvalue() + errors.getvalue() + summary_path.read_text()
            for private in ("203.0.113.67", "PRIVATE-KEY", "private-account", "private-key", "private-secret", "private-bucket",
                            OWNER, APPLICANT, REQUEST_ID, RECORD["message_id"], RECORD["material_title"]):
                self.assertNotIn(private, rendered)
            self.assertEqual(self.s3.writes, [])


if __name__ == "__main__":
    unittest.main()
