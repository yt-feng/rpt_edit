import base64
import json
import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import check_mineru_key_expiry as monitor


NOW = datetime(2026, 8, 29, 1, 17, tzinfo=timezone.utc)


def fake_probe(state="valid", code="A0204", status=400):
    def probe(_token, **_kwargs):
        return monitor.ProbeResult(state, code, status)

    return probe


def jwt_with_exp(expiry):
    def encode(value):
        raw = json.dumps(value, separators=(",", ":")).encode("utf-8")
        return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")

    return f"{encode({'alg': 'none'})}.{encode({'exp': int(expiry.timestamp())})}.signature"


class FakeResponse:
    def __init__(self, status, payload):
        self.status = status
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def getcode(self):
        return self.status

    def read(self, _limit=-1):
        return json.dumps(self.payload).encode("utf-8")


class ExpiryTests(unittest.TestCase):
    def test_threshold_boundaries_are_inclusive(self):
        cases = (
            (NOW, "expired"),
            (NOW + timedelta(days=3), "expiring_3d"),
            (NOW + timedelta(days=3, seconds=1), "expiring_14d"),
            (NOW + timedelta(days=14), "expiring_14d"),
            (NOW + timedelta(days=14, seconds=1), "healthy"),
        )
        for expiry, expected_stage in cases:
            with self.subTest(expiry=expiry):
                _state, stage, _days = monitor.expiry_evaluation(expiry, now=NOW)
                self.assertEqual(stage, expected_stage)

    def test_date_only_expiry_is_beijing_end_of_day(self):
        parsed = monitor.parse_explicit_expiry("2026-08-29")
        self.assertEqual(parsed.isoformat(), "2026-08-29T23:59:59+08:00")

    def test_explicit_expiry_overrides_jwt_exp(self):
        slot = monitor.ConfiguredSlot(
            env_name="MINER_U",
            display_name="Key 1",
            token=jwt_with_exp(NOW + timedelta(days=60)),
            explicit_expiry="2026-09-01T09:17:00+08:00",
        )
        expiry, source, malformed = monitor.resolve_expiry(slot)
        self.assertEqual(source, "GitHub Variable（预计值）")
        self.assertFalse(malformed)
        self.assertEqual(expiry, NOW + timedelta(days=3))

    def test_jwt_exp_is_used_when_explicit_variable_is_absent(self):
        expected = NOW + timedelta(days=45)
        slot = monitor.ConfiguredSlot(
            env_name="MINER_U",
            display_name="Key 1",
            token=jwt_with_exp(expected),
            explicit_expiry="",
        )
        expiry, source, malformed = monitor.resolve_expiry(slot)
        self.assertEqual(expiry, expected)
        self.assertEqual(source, "JWT exp")
        self.assertFalse(malformed)

    def test_malformed_explicit_variable_does_not_fall_back_silently(self):
        slot = monitor.ConfiguredSlot(
            env_name="MINER_U",
            display_name="Key 1",
            token=jwt_with_exp(NOW + timedelta(days=45)),
            explicit_expiry="ninety days",
        )
        expiry, source, malformed = monitor.resolve_expiry(slot)
        self.assertIsNone(expiry)
        self.assertIn("格式无效", source)
        self.assertTrue(malformed)


class ProbeTests(unittest.TestCase):
    def test_live_gateway_msg_code_shape_is_supported(self):
        body = json.dumps(
            {
                "traceId": "opaque",
                "msgCode": "A0211",
                "msg": "token expired",
                "success": False,
            }
        ).encode("utf-8")
        self.assertEqual(monitor._response_code(body), "A0211")

    def test_official_auth_codes_and_transient_responses(self):
        cases = (
            (401, "A0211", "expired"),
            (401, "a0202", "invalid"),
            (400, "A0204", "valid"),
            (404, "A0301", "valid"),
            (200, "", "valid"),
            (401, "", "unknown"),
            (429, "A0204", "unknown"),
            (503, "A0204", "unknown"),
            (401, "-60012", "unknown"),
        )
        for status, code, expected in cases:
            with self.subTest(status=status, code=code):
                result = monitor.classify_probe_response(status, code)
                self.assertEqual(result.state, expected)

    def test_probe_is_get_only_and_sends_token_only_in_authorization_header(self):
        secret = "mineru-secret-value"
        calls = []

        def opener(request, **kwargs):
            calls.append((request, kwargs))
            return FakeResponse(400, {"code": "A0204", "msg": "task not found"})

        result = monitor.probe_token(secret, opener=opener)
        self.assertEqual(result.state, "valid")
        request, kwargs = calls[0]
        self.assertEqual(request.method, "GET")
        self.assertIsNone(request.data)
        self.assertTrue(request.full_url.endswith(monitor.PROBE_BATCH_ID))
        self.assertEqual(request.get_header("Authorization"), f"Bearer {secret}")
        self.assertNotIn(secret, request.full_url)
        self.assertEqual(kwargs["timeout"], 20)

    @mock.patch("check_mineru_key_expiry.urllib.request.urlopen")
    def test_network_failure_is_unknown_without_exception_text(self, urlopen):
        urlopen.side_effect = monitor.urllib.error.URLError("token=must-not-leak")
        result = monitor.probe_token("must-not-leak")
        self.assertEqual(result, monitor.ProbeResult("unknown", "", None))


class ReportTests(unittest.TestCase):
    def test_only_nonempty_secret_slots_are_monitored(self):
        env = {
            "MINER_U": "key-one",
            "MINER_U_2": "  ",
            "MINER_U_3": "key-three",
            "MINER_U_4": "",
        }
        slots = monitor.collect_configured_slots(env)
        self.assertEqual([slot.env_name for slot in slots], ["MINER_U", "MINER_U_3"])

    def test_no_configured_secrets_produces_an_actionable_alert(self):
        report = monitor.run_monitor({}, now=NOW, probe_func=fake_probe())
        self.assertTrue(report.should_alert)
        self.assertEqual(report.alert_stage, "no_keys")
        self.assertEqual(report.configured_count, 0)
        self.assertEqual(report.severity, "critical")

    def test_force_email_sends_healthy_test_with_stable_key(self):
        env = {
            "MINER_U": "opaque-key",
            "MINER_U_EXPIRES_AT": (NOW + timedelta(days=30)).isoformat(),
        }
        first = monitor.run_monitor(env, now=NOW, force_email=True, probe_func=fake_probe())
        later = monitor.run_monitor(
            env,
            now=NOW + timedelta(hours=2),
            force_email=True,
            probe_func=fake_probe(),
        )
        self.assertEqual(first.alert_stage, "healthy_forced")
        self.assertEqual(first.severity, "info")
        self.assertEqual(first.dedupe_key, later.dedupe_key)
        self.assertTrue(first.should_alert)

    def test_dedupe_key_changes_when_key_moves_to_a_new_stage(self):
        expiry = NOW + timedelta(days=13)
        env = {"MINER_U": "opaque-key", "MINER_U_EXPIRES_AT": expiry.isoformat()}
        warning = monitor.run_monitor(env, now=NOW, probe_func=fake_probe())
        critical = monitor.run_monitor(
            env,
            now=expiry - timedelta(days=2),
            probe_func=fake_probe(),
        )
        self.assertEqual(warning.alert_stage, "expiring_14d")
        self.assertEqual(critical.alert_stage, "expiring_3d")
        self.assertNotEqual(warning.dedupe_key, critical.dedupe_key)

    def test_dedupe_key_changes_when_expected_expiry_is_updated(self):
        first_env = {
            "MINER_U": "opaque-key",
            "MINER_U_EXPIRES_AT": (NOW + timedelta(days=9)).isoformat(),
        }
        second_env = {
            "MINER_U": "replacement-key",
            "MINER_U_EXPIRES_AT": (NOW + timedelta(days=12)).isoformat(),
        }
        first = monitor.run_monitor(first_env, now=NOW, probe_func=fake_probe())
        second = monitor.run_monitor(second_env, now=NOW, probe_func=fake_probe())
        self.assertEqual(first.alert_stage, second.alert_stage)
        self.assertNotEqual(first.dedupe_key, second.dedupe_key)

    def test_token_never_reaches_email_json_github_output_or_console_summary(self):
        secrets = ("token-super-secret-one", "token-super-secret-two")
        env = {
            "MINER_U": secrets[0],
            "MINER_U_2": secrets[1],
            "MINER_U_EXPIRES_AT": (NOW + timedelta(days=7)).isoformat(),
            "MINER_U_2_EXPIRES_AT": (NOW + timedelta(days=40)).isoformat(),
            "GITHUB_SERVER_URL": "https://github.com",
            "GITHUB_REPOSITORY": "owner/repo",
            "GITHUB_RUN_ID": "1234",
        }
        report = monitor.run_monitor(env, now=NOW, probe_func=fake_probe())
        rendered = monitor.render_email(report, env)
        payload = json.dumps(monitor.report_payload(report), ensure_ascii=False)
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            output = tmp_path / "github-output.txt"
            email = tmp_path / "email.txt"
            report_json = tmp_path / "report.json"
            monitor.write_github_output(output, report, email, report_json)
            combined = rendered + payload + output.read_text(encoding="utf-8")
        for secret in secrets:
            self.assertNotIn(secret, combined)
        self.assertIn("MINER_U", combined)
        self.assertNotIn("msg", combined)

    def test_invalid_and_expiring_keys_are_aggregated_in_one_email(self):
        env = {
            "MINER_U": "bad-key",
            "MINER_U_EXPIRES_AT": (NOW + timedelta(days=40)).isoformat(),
            "MINER_U_2": "short-key",
            "MINER_U_2_EXPIRES_AT": (NOW + timedelta(days=9)).isoformat(),
        }

        def probe(token, **_kwargs):
            if token == "bad-key":
                return monitor.ProbeResult("invalid", "A0202", 401)
            return monitor.ProbeResult("valid", "A0204", 400)

        report = monitor.run_monitor(env, now=NOW, probe_func=probe)
        email = monitor.render_email(report, env)
        self.assertEqual(report.issue_count, 2)
        self.assertEqual(report.alert_stage, "invalid")
        self.assertEqual(report.severity, "critical")
        self.assertIn("Key 1", email)
        self.assertIn("Key 2", email)
        self.assertIn("A0202", email)


class WorkflowContractTests(unittest.TestCase):
    def test_workflow_schedule_inputs_and_secret_separation(self):
        workflow = (REPO_ROOT / ".github/workflows/mineru-key-expiry-monitor.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("17 1 * * *", workflow)
        self.assertIn("force_email:", workflow)
        self.assertIn("scripts/check_mineru_key_expiry.py", workflow)
        self.assertIn("scripts/test_check_mineru_key_expiry.py", workflow)
        self.assertIn("--dedupe-hours", workflow)
        self.assertIn("inputs.force_email && '1' || '168'", workflow)
        self.assertIn("if: vars.PORTAL_AUTOMATION_ENABLED == 'true'", workflow)
        self.assertIn("scripts/test_send_portal_ops_alert.py", workflow)
        for suffix in ("", "_2", "_3", "_4"):
            self.assertIn(f"MINER_U{suffix}: ${{{{ secrets.MINER_U{suffix} }}}}", workflow)
            self.assertIn(
                f"MINER_U{suffix}_EXPIRES_AT: ${{{{ vars.MINER_U{suffix}_EXPIRES_AT }}}}",
                workflow,
            )

        probe_block = workflow.split("- name: Probe MinerU key pool", 1)[1].split("\n      - name:", 1)[0]
        self.assertIn("MINER_U:", probe_block)
        self.assertNotIn("OPS_ALERT_SIGNING_KEY", probe_block)
        self.assertNotIn("PORTAL_PRIVATE_CONFIG_B64", probe_block)

        send_block = workflow.split("- name: Send deduplicated expiry email", 1)[1]
        self.assertIn("OPS_ALERT_SIGNING_KEY", send_block)
        self.assertNotIn("secrets.MINER_U", send_block)


if __name__ == "__main__":
    unittest.main()
