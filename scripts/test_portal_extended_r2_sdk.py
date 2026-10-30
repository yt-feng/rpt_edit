#!/usr/bin/env python3
"""Exercise R2 retries through botocore's real parser, endpoint and handlers.

Only the HTTP transport and waits are replaced.  No R2 credentials, sockets or
live requests are used; Stubber would bypass the retry lifecycle under test.
"""
from __future__ import annotations

from contextlib import contextmanager
import io
import os
import unittest
from unittest.mock import patch

from botocore.awsrequest import AWSResponse
from botocore.exceptions import ClientError

from portal_extended_r2 import (
    R2NotFound,
    R2PermissionError,
    R2Store,
    R2TransportError,
    build_r2_client,
    sha256_bytes,
)


class RawBody(io.BytesIO):
    def stream(self, amt=1024, decode_content=False):
        while chunk := self.read(amt):
            yield chunk


def http_response(status, body=b"", *, metadata=False, head=False, write_metadata=None):
    headers = {"content-length": str(len(body))}
    if metadata:
        headers["x-amz-meta-sha256"] = sha256_bytes(body)
    if write_metadata is not None:
        headers.update({f"x-amz-meta-{key}": value for key, value in write_metadata.items()})
        headers.update({"content-type": "application/octet-stream", "cache-control": "private, no-store"})
    return AWSResponse("https://test.invalid/object", status, headers, RawBody(b"" if head else body))


class R2SDKTests(unittest.TestCase):
    def setUp(self):
        with patch.dict(os.environ, {
            "R2_ACCOUNT_ID": "test-account",
            "R2_ACCESS_KEY_ID": "test-access-key",
            "R2_SECRET_ACCESS_KEY": "test-secret-key",
        }):
            self.client = build_r2_client()
        self.addCleanup(self.client.close)
        self.store = R2Store(self.client, "private-bucket", "_extended-locales/staging/sdk")

    @contextmanager
    def transport(self, responses):
        # Keep real standard/adaptive handlers, but do not wait for either the
        # exponential backoff or the adaptive token bucket during offline tests.
        with patch.object(self.client._endpoint.http_session, "send", side_effect=responses) as send, \
                patch("botocore.endpoint.time.sleep") as sleep, \
                patch("botocore.retries.bucket.TokenBucket.acquire", return_value=True) as acquire:
            yield send, sleep, acquire

    def test_head_bare_429_reaches_native_retry_and_adaptive_rate_limiter(self):
        with self.transport([http_response(429), http_response(200, b"abc", head=True)]) as (send, sleep, acquire):
            response = self.client.head_object(Bucket="private-bucket", Key="object")
        self.assertEqual(response["ResponseMetadata"]["RetryAttempts"], 1)
        self.assertEqual(send.call_count, 2)
        self.assertEqual(sleep.call_count, 1)
        # The limiter starts disabled; acquisition proves it saw the normalized
        # throttle and gated the next request, not just an added retry loop.
        self.assertEqual(acquire.call_count, 1)

    def test_get_bare_429_recovers_through_native_sdk_retry(self):
        with self.transport([
            http_response(200, b"abc", metadata=True, head=True),
            http_response(429),
            http_response(200, b"abc"),
        ]) as (send, sleep, acquire):
            self.assertEqual(self.store._get("object", maximum=16), b"abc")
        self.assertEqual([call.args[0].method for call in send.call_args_list], ["HEAD", "GET", "GET"])
        self.assertEqual(sleep.call_count, 1)
        self.assertEqual(acquire.call_count, 1)

    def test_post_put_head_throttles_do_not_replay_the_put(self):
        with self.transport([
            http_response(200),
            http_response(429),
            http_response(429),
            http_response(200, b"abc", metadata=True, head=True),
        ]) as (send, sleep, acquire):
            result = self.store._put("object", b"abc", metadata={"kind": "test"})
        self.assertEqual(result["sha256"], sha256_bytes(b"abc"))
        self.assertEqual([call.args[0].method for call in send.call_args_list], ["PUT", "HEAD", "HEAD", "HEAD"])
        self.assertEqual(sleep.call_count, 2)
        self.assertEqual(acquire.call_count, 2)

    def test_put_bare_429_recovers_through_native_sdk_retry(self):
        with self.transport([
            http_response(429),
            http_response(200),
            http_response(200, b"abc", metadata=True, head=True),
        ]) as (send, sleep, acquire):
            result = self.store._put("object", b"abc", metadata={"kind": "test"})
        self.assertEqual(result["sha256"], sha256_bytes(b"abc"))
        self.assertEqual([call.args[0].method for call in send.call_args_list], ["PUT", "PUT", "HEAD"])
        self.assertEqual(sleep.call_count, 1)
        self.assertEqual(acquire.call_count, 2)

    def test_same_object_serviceunavailable_reaches_native_adaptive_retry(self):
        body = (b"<Error><Code>ServiceUnavailable</Code><Message>"
                b"Reduce your concurrent request rate for the same object.</Message></Error>")
        for status in (429, 503):
            with self.subTest(status=status), self.transport([
                http_response(status, body), http_response(200),
            ]) as (send, sleep, acquire):
                response = self.client.put_object(Bucket="private-bucket", Key="object", Body=b"abc")
                self.assertEqual(response["ResponseMetadata"]["RetryAttempts"], 1)
                self.assertEqual([call.args[0].method for call in send.call_args_list], ["PUT", "PUT"])
                self.assertEqual(sleep.call_count, 1)
                self.assertGreaterEqual(acquire.call_count, 1)

    def test_put_throttling_exhaustion_has_one_native_budget_and_one_reconciliation(self):
        body = (b"<Error><Code>ServiceUnavailable</Code><Message>"
                b"Reduce your concurrent request rate for the same object.</Message></Error>")
        with self.transport([http_response(429, body) for _ in range(9)] + [http_response(404)]) as (send, sleep, acquire):
            with self.assertRaises(R2TransportError) as raised:
                self.store._put("object", b"abc", metadata={"kind": "test"})
        self.assertEqual([call.args[0].method for call in send.call_args_list], ["PUT"] * 9 + ["HEAD"])
        self.assertEqual(sleep.call_count, 8)
        self.assertEqual(acquire.call_count, 9)
        cause = raised.exception.__cause__
        self.assertIsInstance(cause, ClientError)
        self.assertEqual(cause.response["Error"]["Code"], "SlowDown")
        self.assertEqual(cause.response["ResponseMetadata"]["RetryAttempts"], 8)

    def test_exhausted_put_accepts_only_the_verified_committed_object(self):
        with self.transport([http_response(429) for _ in range(9)] + [
            http_response(200, b"abc", metadata=True, head=True, write_metadata={"kind": "test"}),
        ]) as (send, sleep, acquire):
            result = self.store._put("object", b"abc", metadata={"kind": "test"})
        self.assertEqual(result["sha256"], sha256_bytes(b"abc"))
        self.assertEqual([call.args[0].method for call in send.call_args_list], ["PUT"] * 9 + ["HEAD"])
        self.assertEqual(sleep.call_count, 8)

    def test_identical_put_is_verified_without_sending_a_write(self):
        with self.transport([
            http_response(200, b"abc", metadata=True, head=True, write_metadata={"kind": "test"}),
        ]) as (send, sleep, acquire):
            result = self.store._put("object", b"abc", metadata={"kind": "test"}, reuse_identical=True)
        self.assertEqual(result["sha256"], sha256_bytes(b"abc"))
        self.assertEqual([call.args[0].method for call in send.call_args_list], ["HEAD"])
        sleep.assert_not_called()

    def test_named_put_failures_are_not_normalized_retried_or_reconciled(self):
        cases = [(429, "AccessDenied", R2PermissionError), (403, "AccessDenied", R2PermissionError),
                 (400, "InvalidArgument", R2TransportError)]
        for status, code, expected in cases:
            body = f"<Error><Code>{code}</Code><Message>Rejected</Message></Error>".encode()
            with self.subTest(status=status, code=code), self.transport([http_response(status, body)]) as (send, sleep, acquire):
                with self.assertRaises(expected) as raised:
                    self.store._put("object", b"abc", metadata={})
                self.assertEqual(raised.exception.__cause__.response["Error"]["Code"], code)
                self.assertEqual([call.args[0].method for call in send.call_args_list], ["PUT"])
                sleep.assert_not_called()
                acquire.assert_not_called()

    def test_persistent_429_stops_at_one_native_nine_attempt_budget(self):
        self.assertEqual(self.client.meta.config.retries["total_max_attempts"], 9)
        with self.transport([http_response(429) for _ in range(9)]) as (send, sleep, acquire):
            with self.assertRaises(R2TransportError) as raised:
                self.store._get("object", maximum=16)
        self.assertEqual(send.call_count, 9)
        self.assertEqual(sleep.call_count, 8)
        self.assertEqual(acquire.call_count, 8)
        cause = raised.exception.__cause__
        self.assertIsInstance(cause, ClientError)
        self.assertEqual(cause.response["ResponseMetadata"]["RetryAttempts"], 8)

    def test_permission_and_missing_responses_are_not_retried(self):
        for status, expected in [(403, R2PermissionError), (404, R2NotFound)]:
            with self.subTest(status=status), self.transport([http_response(status)]) as (send, sleep, acquire):
                with self.assertRaises(expected):
                    self.store._get("object", maximum=16)
                self.assertEqual(send.call_count, 1)
                sleep.assert_not_called()
                acquire.assert_not_called()

    def test_named_service_error_on_429_is_preserved(self):
        body = b"<Error><Code>AccessDenied</Code><Message>Denied</Message></Error>"
        with self.transport([http_response(429, body)]) as (send, sleep, acquire):
            with self.assertRaises(ClientError) as raised:
                self.client.get_object(Bucket="private-bucket", Key="object")
        self.assertEqual(raised.exception.response["Error"]["Code"], "AccessDenied")
        self.assertEqual(send.call_count, 1)
        sleep.assert_not_called()
        acquire.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
