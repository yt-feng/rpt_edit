#!/usr/bin/env python3
"""Offline real-SDK throttling and bounded interrupted-stream contracts."""
from contextlib import contextmanager
import io
import os
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import boto3
from botocore.awsrequest import AWSResponse
from botocore.config import Config
from botocore.exceptions import ClientError, IncompleteReadError
from botocore.response import StreamingBody

import r2_transport as transport


class RawBody(io.BytesIO):
    def stream(self, amt=1024, decode_content=False):
        while chunk := self.read(amt):
            yield chunk


def response(status, body=b""):
    return AWSResponse("https://test.invalid/object", status,
                       {"content-length": str(len(body))}, RawBody(body))


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.client = transport.install_r2_retry_handler(boto3.client(
            "s3", endpoint_url="https://test.invalid", region_name="auto",
            aws_access_key_id="test", aws_secret_access_key="test",
            config=Config(retries={"total_max_attempts": 9, "mode": "adaptive"}),
        ))
        self.addCleanup(self.client.close)

    @contextmanager
    def http(self, responses):
        with patch.object(self.client._endpoint.http_session, "send", side_effect=responses) as send, \
             patch("botocore.endpoint.time.sleep") as sleep, \
             patch("botocore.retries.bucket.TokenBucket.acquire", return_value=True) as acquire:
            yield send, sleep, acquire

    def test_historical_simultaneous_read_response_uses_native_adaptive_budget(self):
        body = (b"<Error><Code>ServiceUnavailable</Code><Message>"
                b"Reduce your rate of simultaneous reads on the same object.</Message></Error>")
        for status in (429, 503):
            with self.subTest(status=status), self.http([response(status, body), response(200, b"abc")]) as (send, sleep, acquire):
                self.assertEqual(transport.read_r2_bytes(self.client, "bucket", "object", maximum=10), b"abc")
                self.assertEqual(send.call_count, 2)
                self.assertEqual(sleep.call_count, 1)
                self.assertGreaterEqual(acquire.call_count, 1)

    def test_persistent_native_throttle_stops_after_nine_gets(self):
        with self.http([response(429) for _ in range(9)]) as (send, sleep, acquire):
            with self.assertRaises(ClientError) as raised:
                transport.read_r2_bytes(self.client, "bucket", "object", maximum=10)
        self.assertEqual(send.call_count, 9)
        self.assertEqual(sleep.call_count, 8)
        self.assertEqual(raised.exception.response["ResponseMetadata"]["RetryAttempts"], 8)

    def test_named_permission_error_is_not_normalized(self):
        body = b"<Error><Code>AccessDenied</Code><Message>Denied</Message></Error>"
        with self.http([response(429, body)]) as (send, sleep, acquire):
            with self.assertRaises(ClientError) as raised:
                transport.read_r2_bytes(self.client, "bucket", "object", maximum=10)
        self.assertEqual(raised.exception.response["Error"]["Code"], "AccessDenied")
        self.assertEqual(send.call_count, 1)
        sleep.assert_not_called()
        acquire.assert_not_called()

    def test_publisher_does_not_multiply_real_sdk_head_or_upload_budgets(self):
        import publish_static_slot
        with self.http([response(429) for _ in range(9)]) as (send, sleep, acquire):
            with self.assertRaises(ClientError):
                publish_static_slot.head_object_with_retry(self.client, "bucket", "object")
            self.assertEqual(send.call_count, 9)
            self.assertEqual(sleep.call_count, 8)
        with tempfile.NamedTemporaryFile() as source:
            source.write(b"abc")
            source.flush()
            with self.http([response(429) for _ in range(9)]) as (send, sleep, acquire):
                with self.assertRaises(boto3.exceptions.S3UploadFailedError):
                    publish_static_slot.upload_file_with_retry(self.client, source.name, "bucket", "object")
                self.assertEqual(send.call_count, 9)
                self.assertEqual(sleep.call_count, 8)

    def test_release_clients_share_native_policy_and_bounded_timeouts(self):
        import chart_search_r2
        import portal_extended_r2
        import portal_suite_catalog
        import publish_static_slot
        env = {"R2_ACCOUNT_ID": "test", "R2_ACCESS_KEY_ID": "test",
               "R2_SECRET_ACCESS_KEY": "test", "R2_BUCKET": "bucket"}
        with patch.dict(os.environ, env):
            clients = [chart_search_r2.client_and_bucket()[0], portal_extended_r2.build_r2_client(),
                       portal_suite_catalog.build_r2_client(), publish_static_slot.build_r2_client()[0]]
        for client in clients:
            self.addCleanup(client.close)
            self.assertTrue(transport.native_retry_handler_installed(client))
            self.assertEqual(client.meta.config.retries["total_max_attempts"], 9)
            self.assertEqual(client.meta.config.connect_timeout, 10)
            self.assertEqual(client.meta.config.read_timeout, 60)


class BoundedBodyTests(unittest.TestCase):
    def setUp(self):
        self.sleep_patch = patch("r2_transport.time.sleep")
        self.sleep = self.sleep_patch.start()
        self.addCleanup(self.sleep_patch.stop)
        jitter = patch("r2_transport.random.uniform", return_value=0)
        jitter.start()
        self.addCleanup(jitter.stop)

    def test_reads_in_chunks_closes_and_forwards_pinned_get_arguments(self):
        raw = b"x" * (transport.READ_CHUNK_BYTES + 3)
        stream = io.BytesIO(raw)
        client = SimpleNamespace(get_object=Mock(return_value={"Body": stream, "ContentLength": len(raw)}))
        self.assertEqual(transport.read_r2_bytes(client, "bucket", "key", maximum=len(raw), IfMatch="etag"), raw)
        client.get_object.assert_called_once_with(Bucket="bucket", Key="key", IfMatch="etag")
        self.assertTrue(stream.closed)

    def test_incomplete_native_stream_recovers_without_reusing_partial_bytes(self):
        partial_raw, full_raw = io.BytesIO(b"ab"), io.BytesIO(b"complete")
        partial = StreamingBody(partial_raw, 8)
        complete = StreamingBody(full_raw, 8)
        client = SimpleNamespace(get_object=Mock(side_effect=[
            {"Body": partial, "ContentLength": 8}, {"Body": complete, "ContentLength": 8},
        ]))
        self.assertEqual(transport.read_r2_bytes(client, "bucket", "key", maximum=8), b"complete")
        self.assertEqual(client.get_object.call_count, 2)
        self.assertTrue(partial_raw.closed and full_raw.closed)
        self.sleep.assert_called_once_with(2)

    def test_stream_after_native_retries_does_not_start_another_sdk_chain(self):
        raw = io.BytesIO(b"ab")
        client = SimpleNamespace(get_object=Mock(return_value={
            "Body": StreamingBody(raw, 8), "ContentLength": 8,
            "ResponseMetadata": {"RetryAttempts": 1},
        }))
        with self.assertRaises(IncompleteReadError):
            transport.read_r2_bytes(client, "bucket", "key", maximum=8)
        self.assertEqual(client.get_object.call_count, 1)
        self.assertTrue(raw.closed)
        self.sleep.assert_not_called()

    def test_request_transport_failure_has_no_extra_chain(self):
        client = SimpleNamespace(get_object=Mock(side_effect=TimeoutError("SDK exhausted")))
        with self.assertRaises(TimeoutError):
            transport.read_r2_bytes(client, "bucket", "key", maximum=8)
        self.assertEqual(client.get_object.call_count, 1)
        self.sleep.assert_not_called()

    def test_stream_recovery_is_bounded_and_closes_all_responses(self):
        streams = [io.BytesIO(b"a") for _ in range(4)]
        client = SimpleNamespace(get_object=Mock(side_effect=[
            {"Body": StreamingBody(stream, 8), "ContentLength": 8} for stream in streams
        ]))
        with self.assertRaises(IncompleteReadError):
            transport.read_r2_bytes(client, "bucket", "key", maximum=8)
        self.assertEqual(client.get_object.call_count, 4)
        self.assertEqual([call.args[0] for call in self.sleep.call_args_list], [2, 4, 8])
        self.assertTrue(all(stream.closed for stream in streams))

    def test_invalid_or_oversized_headers_close_without_retry(self):
        for length in (-1, "3", 9, None, 0):
            with self.subTest(length=length):
                stream = io.BytesIO(b"abc")
                client = SimpleNamespace(get_object=Mock(return_value={"Body": stream, "ContentLength": length}))
                with self.assertRaises(transport.R2BodyError) as raised:
                    transport.read_r2_bytes(client, "bucket", "key", maximum=8, require_content_length=True)
                self.assertEqual(raised.exception.category, "size_invalid")
                self.assertTrue(stream.closed)
                self.assertEqual(client.get_object.call_count, 1)
        self.sleep.assert_not_called()

    def test_body_overflow_or_declared_length_mismatch_does_not_retry(self):
        for raw, length, category in ((b"123456789", None, "size_invalid"), (b"abc", 4, "size_mismatch")):
            with self.subTest(category=category):
                stream = io.BytesIO(raw)
                client = SimpleNamespace(get_object=Mock(return_value={"Body": stream, "ContentLength": length}))
                with self.assertRaises(transport.R2BodyError) as raised:
                    transport.read_r2_bytes(client, "bucket", "key", maximum=8)
                self.assertEqual(raised.exception.category, category)
                self.assertTrue(stream.closed)
                self.assertEqual(client.get_object.call_count, 1)
        self.sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
