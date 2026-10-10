#!/usr/bin/env python3
from __future__ import annotations
import json
import unittest
from unittest.mock import Mock, patch

import diagnose_chart_vision_config as diagnostic


class VisionConfigTests(unittest.TestCase):
    def test_fixed_classification_never_copies_provider_detail(self):
        for message, expected in (
            ("model_not_found PRIVATE_SECRET", "model_unavailable"),
            ("No available channel PRIVATE_SECRET", "model_unavailable"),
            ("Cannot POST /PRIVATE_SECRET", "route_not_found"),
            ("PRIVATE_SECRET", "configuration"),
        ):
            with self.subTest(message=message):
                response = Mock(status_code=404)
                response.json.return_value = {"error": {"message": message}}
                exc = diagnostic.chart.classify_http_error(response)
                self.assertEqual(exc.reason, expected)
                self.assertEqual(exc.status, 404)
                self.assertNotIn("PRIVATE", str(exc))

    def test_real_client_posts_once_to_exact_configured_destination(self):
        response = Mock(status_code=404)
        response.json.return_value = {"error": {"code": "ModelNotFound", "message": "PRIVATE"}}
        session = Mock()
        session.post.return_value = response
        env = {"VISION_INDEX_API_BASE_URL": "https://private.example.invalid/compatible-mode/v1",
               "VISION_INDEX_API_KEY": "PRIVATE_KEY", "VISION_INDEX_MODEL": "PRIVATE_MODEL"}
        with patch.dict(diagnostic.os.environ, env, clear=True), patch.object(diagnostic.chart.requests, "Session", return_value=session):
            report = diagnostic.inspect_configuration()
        self.assertEqual(report["reason"], "model_unavailable")
        self.assertEqual(report["provider_posts"], 1)
        self.assertEqual(report["endpoint_path_kind"], "versioned_chat_completions")
        session.post.assert_called_once()
        self.assertEqual(session.post.call_args.args[0], env["VISION_INDEX_API_BASE_URL"] + "/chat/completions")
        self.assertEqual(session.post.call_args.kwargs["json"]["model"], "PRIVATE_MODEL")
        self.assertIs(session.post.call_args.kwargs["allow_redirects"], False)
        session.close.assert_called_once()
        self.assertNotIn("PRIVATE", json.dumps(report))
        self.assertNotIn("private.example", json.dumps(report))

    def test_transport_failure_is_not_configuration_rejection(self):
        session = Mock()
        session.post.side_effect = diagnostic.chart.requests.ReadTimeout("PRIVATE_ENDPOINT")
        env = {"VISION_INDEX_API_BASE_URL": "https://private.example.invalid", "VISION_INDEX_API_KEY": "PRIVATE", "VISION_INDEX_MODEL": "PRIVATE"}
        with patch.dict(diagnostic.os.environ, env, clear=True), patch.object(diagnostic.chart.requests, "Session", return_value=session):
            report = diagnostic.inspect_configuration()
        self.assertEqual(report["probe_status"], "service_or_response_failure")
        self.assertEqual(report["reason"], "read_timeout")
        self.assertEqual(report["endpoint_path_kind"], "root_chat_completions")
        session.post.assert_called_once()
        self.assertNotIn("PRIVATE", json.dumps(report))

    def test_missing_configuration_makes_no_call(self):
        with patch.dict(diagnostic.os.environ, {}, clear=True), patch.object(diagnostic.chart.requests, "Session") as session:
            report = diagnostic.inspect_configuration()
        session.assert_not_called()
        self.assertEqual(report["provider_posts"], 0)
        self.assertEqual(report["probe_status"], "configuration_invalid")

    def test_redirects_cannot_create_a_second_post_or_change_destination(self):
        for status in (307, 308):
            with self.subTest(status=status):
                session = Mock()
                session.post.return_value = Mock(status_code=status, headers={"Location": "https://OTHER_PRIVATE.invalid"})
                env = {"VISION_INDEX_API_BASE_URL": "https://private.example.invalid/v1", "VISION_INDEX_API_KEY": "PRIVATE", "VISION_INDEX_MODEL": "PRIVATE"}
                with patch.dict(diagnostic.os.environ, env, clear=True), patch.object(diagnostic.chart.requests, "Session", return_value=session):
                    report = diagnostic.inspect_configuration()
                session.post.assert_called_once()
                self.assertIs(session.post.call_args.kwargs["allow_redirects"], False)
                self.assertEqual(report["reason"], "http_unexpected")
                self.assertFalse(report["endpoint_changed"])
                self.assertNotIn("PRIVATE", json.dumps(report))

    def test_success_retains_no_generated_model_content(self):
        env = {"VISION_INDEX_API_BASE_URL": "https://private.example.invalid/v1", "VISION_INDEX_API_KEY": "PRIVATE", "VISION_INDEX_MODEL": "PRIVATE"}
        with patch.dict(diagnostic.os.environ, env, clear=True), patch.object(diagnostic.chart.VisionClient, "analyze", return_value={"description": "PRIVATE"}):
            report = diagnostic.inspect_configuration()
        self.assertEqual(report["probe_status"], "accepted")
        self.assertNotIn("PRIVATE", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
