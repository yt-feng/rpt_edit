#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import io
import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

import upload_market_view_to_r2 as uploader


class FakeR2Client:
    def __init__(self, head_overrides: dict | None = None) -> None:
        self.calls: list[tuple[str, str]] = []
        self.objects: dict[str, dict] = {}
        self.head_overrides = head_overrides or {}

    def put_object(self, **kwargs):
        key = kwargs["Key"]
        body = kwargs["Body"]
        if hasattr(body, "read"):
            body = body.read()
        kwargs = {**kwargs, "Body": bytes(body)}
        self.calls.append(("put", key))
        self.objects[key] = kwargs
        return {"ETag": '"fake"'}

    def head_object(self, **kwargs):
        key = kwargs["Key"]
        self.calls.append(("head", key))
        stored = self.objects[key]
        response = {
            "ContentLength": len(stored["Body"]),
            "ContentType": stored.get("ContentType"),
            "Metadata": stored.get("Metadata", {}),
        }
        response.update(self.head_overrides)
        return response

    def get_object(self, **kwargs):
        key = kwargs["Key"]
        self.calls.append(("get", key))
        body = self.objects[key]["Body"]
        if kwargs.get("Range") == "bytes=0-4":
            body = body[:5]
        return {"Body": io.BytesIO(body)}


def write_pdf(directory: str, payload_size: int = 1400, magic: bytes = b"%PDF-1.7\n") -> Path:
    path = Path(directory) / "market_views_260802.pdf"
    path.write_bytes(magic + (b"x" * payload_size))
    return path


class DateValidationTests(unittest.TestCase):
    def test_accepts_real_six_and_eight_digit_dates(self):
        issue_date, date_key = uploader.parse_issue_date("260802")
        self.assertEqual(issue_date.isoformat(), "2026-08-02")
        self.assertEqual(date_key, "260802")

        issue_date, date_key = uploader.parse_issue_date("20240229")
        self.assertEqual(issue_date.isoformat(), "2024-02-29")
        self.assertEqual(date_key, "240229")

    def test_rejects_wrong_shape_and_impossible_dates(self):
        for value in ("", "26082", "2026-08-02", " 260802", "260802 ", "260229", "20261301"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                uploader.parse_issue_date(value)


class PdfValidationTests(unittest.TestCase):
    def test_rejects_small_or_non_pdf_files(self):
        with tempfile.TemporaryDirectory() as directory:
            exact_limit = Path(directory) / "small.pdf"
            exact_limit.write_bytes(b"%PDF-" + (b"x" * (uploader.MIN_PDF_BYTES - 5)))
            with self.assertRaisesRegex(ValueError, "larger than"):
                uploader.read_valid_pdf(exact_limit)

            non_pdf = write_pdf(directory, magic=b"not-pdf\n")
            with self.assertRaisesRegex(ValueError, "PDF magic"):
                uploader.read_valid_pdf(non_pdf)


class UploadTests(unittest.TestCase):
    def test_if_absent_keeps_an_existing_private_pdf_and_item(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf_path = write_pdf(directory)
            client = FakeR2Client()
            existing_pdf = b"%PDF-1.7\n" + (b"existing" * 200)
            pdf_path.write_bytes(existing_pdf)
            existing_sha = hashlib.sha256(existing_pdf).hexdigest()
            client.objects["_market-views/pdfs/260802.pdf"] = {
                "Body": existing_pdf,
                "ContentType": "application/pdf",
                "Metadata": {"date-key": "260802", "sha256": existing_sha},
            }
            existing_item = {
                "schema_version": 1,
                "id": "market-view:260802",
                "date_key": "260802",
                "date": "2026-08-02",
                "title": "Market Views · 2026-08-02",
                "filename": "market_views_260802.pdf",
                "pdf_key": "_market-views/pdfs/260802.pdf",
                "size_bytes": len(existing_pdf),
                "sha256": existing_sha,
                "content_type": "application/pdf",
                "updated_at": "2026-08-02T00:00:00Z",
                "uploaded_at": "2026-08-02T00:00:00Z",
            }
            client.objects["_market-views/items/260802.json"] = {
                "Body": json.dumps(existing_item).encode("utf-8"),
                "ContentType": "application/json; charset=utf-8",
                "Metadata": {},
            }
            item = uploader.upload_market_view(
                pdf_path,
                "260802",
                client=client,
                bucket="test-bucket",
                if_absent=True,
            )

        self.assertTrue(item["skipped_existing"])
        self.assertEqual(
            client.calls,
            [
                ("head", "_market-views/pdfs/260802.pdf"),
                ("head", "_market-views/items/260802.json"),
                ("get", "_market-views/pdfs/260802.pdf"),
                ("get", "_market-views/items/260802.json"),
            ],
        )

    def test_if_absent_preserves_a_different_same_date_version_privately(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf_path = write_pdf(directory)
            source_data = pdf_path.read_bytes()
            source_sha = hashlib.sha256(source_data).hexdigest()
            existing_pdf = b"%PDF-1.7\n" + (b"existing" * 200)
            existing_sha = hashlib.sha256(existing_pdf).hexdigest()
            client = FakeR2Client()
            client.objects["_market-views/pdfs/260802.pdf"] = {
                "Body": existing_pdf,
                "ContentType": "application/pdf",
                "Metadata": {"date-key": "260802", "sha256": existing_sha},
            }
            existing_item = {
                "schema_version": 1,
                "id": "market-view:260802",
                "date_key": "260802",
                "date": "2026-08-02",
                "title": "Market Views · 2026-08-02",
                "filename": "market_views_260802.pdf",
                "pdf_key": "_market-views/pdfs/260802.pdf",
                "size_bytes": len(existing_pdf),
                "sha256": existing_sha,
                "content_type": "application/pdf",
                "updated_at": "2026-08-02T00:00:00Z",
                "uploaded_at": "2026-08-02T00:00:00Z",
            }
            client.objects["_market-views/items/260802.json"] = {
                "Body": json.dumps(existing_item).encode("utf-8"),
                "ContentType": "application/json; charset=utf-8",
                "Metadata": {},
            }

            item = uploader.upload_market_view(
                pdf_path,
                "260802",
                client=client,
                bucket="test-bucket",
                if_absent=True,
            )

        variant_key = f"_market-views/legacy-variants/260802/{source_sha}.pdf"
        self.assertTrue(item["archived_variant"])
        self.assertEqual(item["variant_pdf_key"], variant_key)
        self.assertIn(variant_key, client.objects)
        self.assertEqual(client.objects[variant_key]["Body"], source_data)

    def test_if_absent_rejects_an_unverified_existing_pair(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf_path = write_pdf(directory)
            client = FakeR2Client()
            client.objects["_market-views/pdfs/260802.pdf"] = {
                "Body": b"%PDF-fake",
                "ContentType": "application/pdf",
                "Metadata": {},
            }
            client.objects["_market-views/items/260802.json"] = {
                "Body": b"{}",
                "ContentType": "application/json; charset=utf-8",
                "Metadata": {},
            }
            with self.assertRaisesRegex(RuntimeError, "too small"):
                uploader.upload_market_view(
                    pdf_path,
                    "260802",
                    client=client,
                    bucket="test-bucket",
                    if_absent=True,
                )

        self.assertNotIn(("put", "_market-views/pdfs/260802.pdf"), client.calls)

    def test_uploads_pdf_verifies_head_then_publishes_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf_path = write_pdf(directory)
            client = FakeR2Client()
            item = uploader.upload_market_view(
                pdf_path,
                "20260802",
                client=client,
                bucket="test-bucket",
                updated_at="2026-08-02T01:02:03Z",
            )

        pdf_key = "_market-views/pdfs/260802.pdf"
        item_key = "_market-views/items/260802.json"
        self.assertEqual(
            client.calls,
            [("put", pdf_key), ("head", pdf_key), ("get", pdf_key), ("put", item_key)],
        )
        pdf_object = client.objects[pdf_key]
        self.assertEqual(pdf_object["ContentType"], "application/pdf")
        self.assertEqual(pdf_object["Metadata"]["sha256"], item["sha256"])
        self.assertEqual(pdf_object["Metadata"]["date-key"], "260802")

        stored_item = json.loads(client.objects[item_key]["Body"].decode("utf-8"))
        self.assertEqual(stored_item, item)
        self.assertEqual(item["schema_version"], 1)
        self.assertEqual(item["id"], "market-view:260802")
        self.assertEqual(item["date"], "2026-08-02")
        self.assertEqual(item["filename"], "market_views_260802.pdf")
        self.assertEqual(item["pdf_key"], pdf_key)
        self.assertEqual(item["size_bytes"], len(pdf_object["Body"]))
        self.assertEqual(item["updated_at"], "2026-08-02T01:02:03Z")

    def test_does_not_publish_metadata_when_head_verification_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf_path = write_pdf(directory)
            client = FakeR2Client({"ContentLength": 7})
            with self.assertRaisesRegex(RuntimeError, "too small"):
                uploader.upload_market_view(
                    pdf_path,
                    "260802",
                    client=client,
                    bucket="test-bucket",
                )

        self.assertEqual(
            client.calls,
            [("put", "_market-views/pdfs/260802.pdf"), ("head", "_market-views/pdfs/260802.pdf")],
        )
        self.assertNotIn("_market-views/items/260802.json", client.objects)

    def test_build_client_uses_cloudflare_r2_endpoint_without_network(self):
        captured: dict = {}

        def fake_client(service_name, **kwargs):
            captured.update({"service_name": service_name, **kwargs})
            return object()

        fake_boto3 = types.SimpleNamespace(client=fake_client)
        env = {
            "R2_ACCOUNT_ID": "account123",
            "R2_ACCESS_KEY_ID": "access123",
            "R2_SECRET_ACCESS_KEY": "secret123",
        }
        with mock.patch.dict(os.environ, env, clear=True), mock.patch.dict(
            sys.modules, {"boto3": fake_boto3}
        ):
            uploader.build_r2_client()

        self.assertEqual(captured["service_name"], "s3")
        self.assertEqual(
            captured["endpoint_url"], "https://account123.r2.cloudflarestorage.com"
        )
        self.assertEqual(captured["region_name"], "auto")


if __name__ == "__main__":
    unittest.main()
