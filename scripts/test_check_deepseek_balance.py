#!/usr/bin/env python3
"""Offline balance-check tests; every HTTP call is mocked."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_deepseek_balance as balance


class BalanceCheckTests(unittest.TestCase):
    def setUp(self):
        self.environment = mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "test-primary-secret"}, clear=True)
        self.environment.start()
        self.addCleanup(self.environment.stop)

    @staticmethod
    def response(payload=None, status=200):
        response = mock.Mock(status_code=status)
        response.json.return_value = payload if payload is not None else {
            "is_available": True,
            "balance_infos": [{"currency": "CNY", "total_balance": "123.4500",
                               "granted_balance": "3.45", "topped_up_balance": "120.00"}],
            "unexpected_private_field": "test-primary-secret",
        }
        return response

    def test_single_get_uses_first_key_and_outputs_only_whitelisted_balance_values(self):
        get = mock.Mock(return_value=self.response())
        with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY_BACKUP": "backup-secret"}):
            report = balance.read_balance(transport=get)
        get.assert_called_once_with(
            "https://api.deepseek.com/user/balance", headers={"Authorization": "Bearer test-primary-secret"},
            timeout=30, allow_redirects=False,
        )
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["mode"], "balance")
        self.assertEqual(report["provider_requests"], 0)
        self.assertEqual(report["balance_requests"], 1)
        self.assertEqual(report["balance_infos"][0]["total_balance"], "123.4500")
        self.assertNotIn("secret", json.dumps(report))
        self.assertNotIn("unexpected_private_field", json.dumps(report))

    def test_key_list_uses_first_nonempty_configured_value_without_fallback_requests(self):
        get = mock.Mock(return_value=self.response())
        with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": " ; first ,second", "DEEPSEEK_API_KEY_BACKUP": "backup"}):
            balance.read_balance(transport=get)
        self.assertEqual(get.call_args.kwargs["headers"], {"Authorization": "Bearer first"})
        self.assertEqual(get.call_count, 1)

    def test_missing_key_makes_no_request(self):
        get = mock.Mock()
        with mock.patch.dict("os.environ", {}, clear=True):
            report = balance.read_balance(transport=get)
        get.assert_not_called()
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["balance_requests"], 0)

    def test_http_errors_do_not_read_or_echo_body_and_never_retry(self):
        for status in (301, 401, 402, 403, 429, 500):
            with self.subTest(status=status):
                response = self.response({"error": "Authorization Bearer test-primary-secret"}, status)
                get = mock.Mock(return_value=response)
                report = balance.read_balance(transport=get)
                response.json.assert_not_called()
                self.assertEqual(get.call_count, 1)
                self.assertEqual(report["status"], "failed")
                self.assertNotIn("secret", json.dumps(report))

    def test_transport_and_json_errors_never_echo_credentials(self):
        get = mock.Mock(side_effect=OSError("Authorization Bearer test-primary-secret"))
        report = balance.read_balance(transport=get)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(report["balance_requests"], 1)
        self.assertNotIn("secret", json.dumps(report))
        response = self.response()
        response.json.side_effect = ValueError("test-primary-secret")
        report = balance.read_balance(transport=mock.Mock(return_value=response))
        self.assertEqual(report["status"], "failed")
        self.assertNotIn("secret", json.dumps(report))

    def test_invalid_currency_or_decimal_fails_without_echoing_source_value(self):
        base = {"currency": "CNY", "total_balance": "1.00", "granted_balance": "0", "topped_up_balance": "1"}
        for field, value in (
            ("currency", "test-primary-secret"), ("currency", "EUR"),
            ("total_balance", "NaN"), ("total_balance", "sNaN"), ("total_balance", "Infinity"),
            ("total_balance", "1E1000000"), ("total_balance", "1E-1000000"),
            ("total_balance", "test-primary-secret"), ("total_balance", 1.0),
            ("granted_balance", None),
        ):
            with self.subTest(field=field, value=value):
                response = self.response({"is_available": True, "balance_infos": [{**base, field: value}]})
                report = balance.read_balance(transport=mock.Mock(return_value=response))
                self.assertEqual(report["status"], "failed")
                self.assertNotIn("balance_infos", report)
                self.assertNotIn("secret", json.dumps(report))

    def test_unavailable_account_and_negative_balances_are_valid_read_only_results(self):
        report = balance.read_balance(transport=mock.Mock(return_value=self.response({
            "is_available": False, "balance_infos": [{"currency": "USD", "total_balance": "-0.05",
                                                       "granted_balance": "0", "topped_up_balance": "-0.05"}],
        })))
        self.assertEqual(report["status"], "passed")
        self.assertFalse(report["is_available"])
        self.assertEqual(report["balance_infos"][0]["total_balance"], "-0.05")

    def test_missing_schema_fields_and_duplicate_currency_are_rejected(self):
        for payload in ({}, {"is_available": "true", "balance_infos": []}, {"is_available": True}):
            report = balance.read_balance(transport=mock.Mock(return_value=self.response(payload)))
            self.assertEqual(report["status"], "failed")
        response = self.response()
        response.json.return_value["balance_infos"] *= 2
        report = balance.read_balance(transport=mock.Mock(return_value=response))
        self.assertEqual(report["status"], "failed")

    def test_diagnostics_file_contains_safe_report_on_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "balance" / "diagnostics.json"
            report = balance.read_balance(diagnostics_out=path, transport=mock.Mock(side_effect=OSError("test-primary-secret")))
            self.assertEqual(json.loads(path.read_text()), report)
            self.assertNotIn("secret", path.read_text())


if __name__ == "__main__":
    unittest.main(verbosity=2)
