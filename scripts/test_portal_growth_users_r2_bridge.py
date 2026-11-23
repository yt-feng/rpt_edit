import ast
import io
from pathlib import Path
import unittest
from unittest.mock import Mock, call

from portal_growth_users_r2_bridge import MAX_BYTES, read_request, request_shape


class ReadOnlyBridgeTests(unittest.TestCase):
    def test_read_projection_does_not_expose_sdk_credentials_or_metadata(self):
        client = Mock()
        body = io.BytesIO(b'{"id":"fixture"}')
        client.get_object.return_value = {"Body": body, "ETag": '"version"', "private": "never-return"}
        result = read_request(client, "fixture-bucket", {"id": 1, "op": "get", "key": "_account/users/id/fixture"})
        self.assertEqual(set(result), {"etag", "body_b64"})
        self.assertEqual(result["etag"], "version")
        self.assertTrue(body.closed)
        client.get_object.assert_called_once_with(Bucket="fixture-bucket", Key="_account/users/id/fixture")
        self.assertEqual(client.mock_calls, [call.get_object(Bucket="fixture-bucket", Key="_account/users/id/fixture")])

    def test_writes_and_broad_or_unrelated_reads_never_reach_storage(self):
        client = Mock()
        for value in [
            {"id": 1, "op": "put", "key": "_account/access/x"},
            {"id": 1, "op": "delete", "key": "_account/access/x"},
            {"id": 1, "op": "list", "prefix": "_account/"},
            {"id": 1, "op": "get", "key": "_analytics/events/private"},
            {"id": 1, "op": "get", "key": "_account/access_backup/latest/fixture"},
            {"id": 1, "op": "get", "key": "_account/access/../other"},
            {"id": 1, "op": "get", "key": "_account/access/fixture/nested"},
            {"id": 1, "op": "list", "prefix": "_account/users/id/", "limit": 1001},
            {"id": 1, "op": "get", "key": "_account/access/fixture", "Body": "mutation"},
            {"id": True, "op": "get", "key": "_account/access/fixture"},
        ]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                read_request(client, "fixture-bucket", value)
        self.assertEqual(client.mock_calls, [])

    def test_sdk_surface_contains_only_three_storage_reads(self):
        source = Path(__file__).with_name("portal_growth_users_r2_bridge.py").read_text()
        operations = {node.func.attr for node in ast.walk(ast.parse(source))
                      if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                      and isinstance(node.func.value, ast.Name) and node.func.value.id == "client"}
        self.assertEqual(operations, {"get_object", "head_object", "list_objects_v2"})

    def test_pagination_preserves_cursor_even_for_short_truncated_pages(self):
        client = Mock()
        client.list_objects_v2.return_value = {"Contents": [{"Key": "_account/users/id/a"}], "IsTruncated": True, "NextContinuationToken": "next"}
        value = read_request(client, "fixture", {"id": 1, "op": "list", "prefix": "_account/users/id/", "limit": 500, "cursor": "before"})
        self.assertEqual(value, {"objects": [{"key": "_account/users/id/a"}], "truncated": True, "cursor": "next"})
        client.list_objects_v2.assert_called_once_with(Bucket="fixture", Prefix="_account/users/id/", MaxKeys=500, ContinuationToken="before")

    def test_missing_objects_are_distinct_from_permission_and_oversize_failures(self):
        client = Mock()
        class StorageError(Exception):
            response = {"Error": {"Code": "NoSuchKey"}}
        client.get_object.side_effect = StorageError()
        request = {"id": 1, "op": "get", "key": "_account/access/fixture"}
        self.assertIsNone(read_request(client, "fixture", request))
        StorageError.response = {"Error": {"Code": "AccessDenied"}}
        with self.assertRaises(StorageError): read_request(client, "fixture", request)
        client.get_object.side_effect = None
        body = io.BytesIO(b"x" * (MAX_BYTES + 1))
        client.get_object.return_value = {"Body": body, "ETag": '"v"'}
        with self.assertRaises(ValueError): read_request(client, "fixture", request)
        self.assertTrue(body.closed)


if __name__ == "__main__": unittest.main()
