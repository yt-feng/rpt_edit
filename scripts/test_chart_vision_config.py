#!/usr/bin/env python3
from __future__ import annotations
import json
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import diagnose_chart_vision_config as diagnostic

ENV = {'VISION_INDEX_API_BASE_URL': 'https://private.example.invalid/compatible-mode/v1',
       'VISION_INDEX_API_KEY': 'PRIVATE_KEY', 'VISION_INDEX_MODEL': 'PRIVATE_MODEL'}


def response_fixture(status=200, payload=None, raw=None, headers=None):
    response = Mock(status_code=status, headers=headers or {})
    body = raw if raw is not None else json.dumps(payload).encode()
    response.iter_content.return_value = [body]
    return response


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
        response = response_fixture(404, {"error": {"code": "ModelNotFound", "message": "PRIVATE"}})
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
                session.post.return_value = response_fixture(status, {}, headers={"Location": "https://OTHER_PRIVATE.invalid"})
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

    def test_override_is_allowlisted_single_probe_only_and_default_model_unchanged(self):
        for model in diagnostic.MODEL_ALLOWLIST:
            with self.subTest(model=model):
                session = Mock()
                session.post.return_value = response_fixture(404, {'error': {'code': 'ModelNotFound'}})
                with patch.dict(diagnostic.os.environ, ENV, clear=True), \
                     patch.object(diagnostic.chart.requests, 'Session', return_value=session):
                    report = diagnostic.inspect_configuration(model)
                    self.assertEqual(diagnostic.os.environ['VISION_INDEX_MODEL'], 'PRIVATE_MODEL')
                session.post.assert_called_once(); session.get.assert_not_called()
                self.assertEqual(session.post.call_args.kwargs['json']['model'], model)
                self.assertTrue(session.post.call_args.kwargs['stream'])
                self.assertFalse(session.post.call_args.kwargs['allow_redirects'])
                self.assertEqual(report['model_override'], model)
                self.assertEqual(report['model_selection'], 'allowlisted_override')
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_invalid_override_makes_no_session_or_request(self):
        for value in ('other-model', 'qwen3-vl-flash\n', ' qwen-vl-max', 'https://PRIVATE.invalid'):
            with self.subTest(value=value), patch.dict(diagnostic.os.environ, ENV, clear=True), \
                 patch.object(diagnostic.chart.requests, 'Session') as session:
                report = diagnostic.inspect_configuration(value)
                session.assert_not_called()
                self.assertEqual(report['reason'], 'model_override_invalid')
                self.assertEqual(report['provider_posts'], 0)
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_probe_body_limit_is_enforced_before_json_or_model_content(self):
        for response in (
            response_fixture(200, {}, headers={'Content-Length': str(diagnostic.MAX_RESPONSE_BYTES + 1)}),
            response_fixture(200, raw=b'x' * (diagnostic.MAX_RESPONSE_BYTES + 1)),
        ):
            session = Mock(); session.post.return_value = response
            with patch.dict(diagnostic.os.environ, ENV, clear=True), \
                 patch.object(diagnostic.chart.requests, 'Session', return_value=session):
                report = diagnostic.inspect_configuration()
            self.assertEqual(report['reason'], 'response_too_large')
            self.assertEqual(report['probe_status'], 'service_or_response_failure')
            session.post.assert_called_once(); response.close.assert_called_once()

    def test_probe_non_200_success_status_cannot_be_accepted(self):
        response = response_fixture(201, {'choices': [{'message': {'content': '{}'}}]})
        session = Mock(); session.post.return_value = response
        with patch.dict(diagnostic.os.environ, ENV, clear=True), \
             patch.object(diagnostic.chart.requests, 'Session', return_value=session):
            report = diagnostic.inspect_configuration()
        self.assertEqual(report['reason'], 'http_unexpected')
        self.assertNotEqual(report['probe_status'], 'accepted')


class VisionModelsTests(unittest.TestCase):
    def inspect(self, response=None, *, env=None, error=None, override=''):
        session = Mock()
        session.get.return_value = response or response_fixture(200, {'data': []})
        if error: session.get.side_effect = error
        with patch.dict(diagnostic.os.environ, env or ENV, clear=True), \
             patch.object(diagnostic.chart.requests, 'Session', return_value=session):
            report = diagnostic.inspect_models(override)
        session.post.assert_not_called()
        return report, session

    def test_models_get_exact_same_origin_and_base_once_only(self):
        for base, expected in (
            ('https://private.invalid', 'https://private.invalid/models'),
            ('https://private.invalid/v1/', 'https://private.invalid/v1/models'),
            ('https://private.invalid/compatible-mode/v1/chat/completions', 'https://private.invalid/compatible-mode/v1/models'),
            ('https://private.invalid:8443/api/v1', 'https://private.invalid:8443/api/v1/models'),
        ):
            with self.subTest(base=base):
                response = response_fixture(200, {'data': [{'id': 'qwen-vl-plus'}]})
                report, session = self.inspect(response, env={**ENV, 'VISION_INDEX_API_BASE_URL': base})
                session.get.assert_called_once_with(expected, timeout=(15, 60), allow_redirects=False, stream=True)
                self.assertEqual((report['provider_gets'], report['provider_posts']), (1, 0))
                self.assertEqual(report['probe_status'], 'accepted')
                self.assertEqual(report['available_models'], ['qwen-vl-plus'])
                self.assertFalse(report['endpoint_changed'])
                response.close.assert_called_once(); session.close.assert_called_once()
                self.assertNotIn('private.invalid', json.dumps(report))

    def test_output_contains_only_allowlist_intersection_in_fixed_order(self):
        payload = {'object': 'list', 'PRIVATE_FIELD': 'PRIVATE_BODY', 'data': [
            {'id': 'PRIVATE_MODEL', 'owned_by': 'PRIVATE_OWNER'},
            {'id': 'qwen-vl-max'}, {'id': 'qwen3-vl-flash'}, {'id': 'qwen-vl-max'},
            {'id': 'qwen2.5-vl-72b-instruct'}, {'id': 'qwen3-vl-plus'}]}
        report, _ = self.inspect(response_fixture(200, payload))
        self.assertEqual(report['available_models'], ['qwen3-vl-flash', 'qwen3-vl-plus', 'qwen-vl-max', 'qwen2.5-vl-72b-instruct'])
        self.assertNotIn('PRIVATE', json.dumps(report))
        self.assertNotIn('inventory_count', report)

    def test_empty_intersection_is_explicit_and_does_not_choose_any_model(self):
        report, _ = self.inspect(response_fixture(200, {'data': [{'id': 'PRIVATE_MODEL'}]}))
        self.assertEqual(report['probe_status'], 'accepted')
        self.assertEqual(report['available_models'], [])
        self.assertNotIn('model_override', report)

    def test_inventory_does_not_require_a_configured_model(self):
        report, session = self.inspect(env={k: v for k, v in ENV.items() if k != 'VISION_INDEX_MODEL'})
        self.assertEqual(report['probe_status'], 'accepted')
        self.assertNotIn('params', session.get.call_args.kwargs)
        self.assertNotIn('json', session.get.call_args.kwargs)

    def test_override_on_inventory_is_rejected_without_any_request(self):
        report, session = self.inspect(override='qwen-vl-max')
        session.get.assert_not_called()
        self.assertEqual(report['reason'], 'model_override_not_applicable')
        self.assertEqual(report['provider_gets'], 0)

    def test_invalid_endpoint_or_missing_key_performs_no_get(self):
        for env in ({**ENV, 'VISION_INDEX_API_KEY': ''}, {**ENV, 'VISION_INDEX_API_BASE_URL': 'http://PRIVATE.invalid'},
                    {**ENV, 'VISION_INDEX_API_BASE_URL': 'https://user:PRIVATE@private.invalid'},
                    {**ENV, 'VISION_INDEX_API_BASE_URL': 'https://private.invalid/?key=PRIVATE'}):
            with self.subTest(env=env):
                report, session = self.inspect(env=env)
                session.get.assert_not_called()
                self.assertEqual(report['probe_status'], 'configuration_invalid')
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_http_failure_and_redirect_never_parse_or_accept_body(self):
        for status in [201, 204, 301, 302, 307, 308, 400, 401, 403, 404, 405, 429, 500, 503]:
            with self.subTest(status=status):
                response = response_fixture(status, {'data': [{'id': 'qwen-vl-max'}], 'secret': 'PRIVATE'})
                report, session = self.inspect(response)
                self.assertNotEqual(report['probe_status'], 'accepted')
                self.assertEqual(report['http_status'], status)
                self.assertEqual(report['available_models'], [])
                response.iter_content.assert_not_called()
                session.get.assert_called_once()
                self.assertFalse(session.get.call_args.kwargs['allow_redirects'])
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_invalid_json_and_duplicate_keys_fail_closed(self):
        for raw in (b'PRIVATE', b'\xff', b'{"data":[],"data":[{"id":"qwen-vl-max"}]}', b'{"data":[],"extra":NaN}', b'{} trailing'):
            with self.subTest(raw=raw):
                report, _ = self.inspect(response_fixture(200, raw=raw))
                self.assertEqual(report['reason'], 'response_json')
                self.assertEqual(report['available_models'], [])
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_invalid_or_partial_inventory_never_returns_early_matches(self):
        for payload in ([], {}, {'data': {}}, {'data': [{'id': 'qwen-vl-max'}, 'PRIVATE']},
                        {'data': [{'id': 'qwen-vl-max'}, {'id': 12}]}, {'data': [], 'error': 'PRIVATE'},
                        {'data': [{'id': 'qwen-vl-max'}], 'has_more': True}, {'data': [], 'next': 'PRIVATE'},
                        {'data': [{'id': 'qwen-vl-max'}] * (diagnostic.MAX_MODEL_ROWS + 1)}):
            with self.subTest(payload_type=type(payload).__name__):
                report, _ = self.inspect(response_fixture(200, payload))
                self.assertNotEqual(report['probe_status'], 'accepted')
                self.assertEqual(report['available_models'], [])
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_response_size_truncation_and_invalid_length_are_rejected(self):
        cases = [
            (response_fixture(200, {}, headers={'Content-Length': str(diagnostic.MAX_RESPONSE_BYTES + 1)}), 'response_too_large'),
            (response_fixture(200, raw=b'x' * (diagnostic.MAX_RESPONSE_BYTES + 1)), 'response_too_large'),
            (response_fixture(200, {}, headers={'Content-Length': '-1'}), 'response_length_invalid'),
            (response_fixture(200, {}, headers={'Content-Length': 'PRIVATE'}), 'response_length_invalid'),
            (response_fixture(200, {}, headers={'Content-Length': '999'}), 'response_length_mismatch')]
        for response, reason in cases:
            with self.subTest(reason=reason):
                report, session = self.inspect(response)
                self.assertEqual(report['reason'], reason)
                self.assertEqual(report['available_models'], [])
                session.get.assert_called_once(); response.close.assert_called_once()

    def test_transport_error_does_not_retry_or_leak_endpoint(self):
        for error, reason in ((diagnostic.chart.requests.ReadTimeout('PRIVATE_HOST'), 'read_timeout'),
                              (diagnostic.chart.requests.ConnectTimeout('PRIVATE_KEY'), 'connect_timeout')):
            report, session = self.inspect(error=error)
            self.assertEqual(report['reason'], reason)
            session.get.assert_called_once(); session.close.assert_called_once()
            self.assertNotIn('PRIVATE', json.dumps(report))

    def test_cli_writes_only_filtered_report_and_workflow_preserves_checkpoint_default(self):
        response = response_fixture(200, {'data': [{'id': 'PRIVATE'}, {'id': 'qwen-vl-plus'}]})
        session = Mock(); session.get.return_value = response
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'report.json'
            with patch.dict(diagnostic.os.environ, ENV, clear=True), \
                 patch.object(diagnostic.chart.requests, 'Session', return_value=session), \
                 patch('sys.argv', ['diagnostic', '--operation', 'vision-models', '--output', str(output)]), \
                 contextlib.redirect_stdout(io.StringIO()) as log:
                self.assertEqual(diagnostic.main(), 0)
            self.assertEqual([path.name for path in Path(directory).iterdir()], ['report.json'])
            self.assertNotIn('PRIVATE', output.read_text() + log.getvalue())
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/portal-chart-search-diagnostic.yml').read_text()
        self.assertIn('default: checkpoint', workflow)
        self.assertIn('options: [checkpoint, vision-models, vision-config]', workflow)
        self.assertIn('inputs.operation != \'vision-models\'', workflow.split('- name: Probe', 1)[0])
        self.assertIn('--model-override "$VISION_MODEL_OVERRIDE"', workflow)
        self.assertNotIn('gh variable', workflow)


if __name__ == "__main__":
    unittest.main()
