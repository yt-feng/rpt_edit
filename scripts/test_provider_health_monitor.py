import copy
from datetime import datetime, timedelta, timezone
import io
import json
import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import zipfile

from provider_health_monitor import classify, probe, thresholds, validate_report, NoRedirect
from notify_provider_health import GitHubReader, read_consumer, incident_groups, send_groups, send_activation_test, ReportUnavailable

NOW = datetime(2026, 10, 5, 12, tzinfo=timezone.utc)
LIMITS = thresholds({})
ENV = {'GITHUB_REPOSITORY': 'example/media', 'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '1',
       'GITHUB_SHA': 'a' * 40, 'TIKHUB_API_KEY': 'private-sentinel', 'DEEPSEEK_API_KEY': 'private-sentinel-2'}
KEYS = ['tikhub:TIKHUB_API_KEY', 'deepseek:DEEPSEEK_API_KEY']


def tikhub(balance=10, free=0):
    return {'code': 200, 'api_key_data': {'api_key_status': 1, 'expires_at': None},
            'user_data': {'balance': balance, 'free_credit': free, 'account_disabled': False, 'is_active': True}}


def deepseek(balance='25', currency='CNY', available=True):
    return {'is_available': available, 'balance_infos': [{'currency': currency, 'total_balance': balance}]}


def report():
    return probe(KEYS, ENV, getter=lambda p, k: (200, tikhub() if p == 'tikhub' else deepseek()), now=NOW)


def validate(value, now=NOW):
    return validate_report(value, now=now, repository=ENV['GITHUB_REPOSITORY'], run_id='123',
                           run_attempt=1, commit='a' * 40, workflow='.github/workflows/provider-api-health.yml')


class ProviderTests(unittest.TestCase):
    def test_payment_permission_and_rate_limit_are_distinct(self):
        for code, expected in [(401, 'invalid_key'), (402, 'payment_required'), (403, 'permission_denied'),
                               (429, 'rate_limited'), (503, 'service_unavailable'), (0, 'transport_error')]:
            for provider in ('tikhub', 'deepseek'):
                with self.subTest(code=code, provider=provider):
                    self.assertEqual(classify(provider, code, None, LIMITS, NOW), [expected])

    def test_tikhub_free_credit_does_not_hide_paid_wallet_exhaustion(self):
        self.assertEqual(classify('tikhub', 200, tikhub(0, 999), LIMITS, NOW), ['exhausted'])
        self.assertEqual(classify('tikhub', 200, tikhub('4.99'), LIMITS, NOW), ['low_balance'])
        self.assertEqual(classify('tikhub', 200, tikhub('5.01'), LIMITS, NOW), ['healthy'])

    def test_tikhub_key_expiry_disabled_and_inactive_account(self):
        for delta, expected in [(-1, 'expired_key'), (86400, 'expiring_key')]:
            item = tikhub()
            item['api_key_data']['expires_at'] = (NOW + timedelta(seconds=delta)).isoformat()
            self.assertIn(expected, classify('tikhub', 200, item, LIMITS, NOW))
        item = tikhub()
        item['api_key_data']['api_key_status'] = 0
        self.assertEqual(classify('tikhub', 200, item, LIMITS, NOW), ['invalid_key'])
        item['user_data']['account_disabled'] = True
        self.assertEqual(classify('tikhub', 200, item, LIMITS, NOW), ['account_disabled'])

    def test_tikhub_embedded_error_is_not_healthy(self):
        self.assertEqual(classify('tikhub', 200, {'code': 402}, LIMITS, NOW), ['payment_required'])

    def test_deepseek_availability_currencies_and_thresholds(self):
        for data, expected in [(deepseek('0'), 'exhausted'), (deepseek('1', available=False), 'exhausted'),
                               (deepseek('20'), 'low_balance'), (deepseek('5', 'USD'), 'low_balance'),
                               (deepseek('21'), 'healthy')]:
            self.assertEqual(classify('deepseek', 200, data, LIMITS, NOW), [expected])
        data = deepseek('0')
        data['balance_infos'].append({'currency': 'USD', 'total_balance': '50'})
        self.assertEqual(classify('deepseek', 200, data, LIMITS, NOW), ['healthy'])

    def test_missing_nonfinite_or_malformed_balances_never_become_zero(self):
        for value in (None, True, '', 'NaN', 'Infinity', [], {}):
            for provider, data in [('tikhub', tikhub(value)), ('deepseek', deepseek(value))]:
                self.assertEqual(classify(provider, 200, data, LIMITS, NOW), ['malformed_response'])
        self.assertEqual(classify('deepseek', 200, deepseek('40', 'EUR'), LIMITS, NOW), ['malformed_response'])

    def test_all_current_slots_checked_and_only_safe_fields_emitted(self):
        calls = []
        def getter(provider, key):
            calls.append((provider, key))
            return 200, tikhub() if provider == 'tikhub' else deepseek()
        value = probe(KEYS, ENV, getter=getter, now=NOW)
        self.assertEqual(len(calls), 2)
        self.assertEqual(validate(value), value)
        raw = json.dumps(value)
        self.assertNotIn('private-sentinel', raw)
        self.assertNotIn('total_balance', raw)
        self.assertNotIn('user_data', raw)

    def test_empty_keys_emit_missing_key_without_network(self):
        value = probe(KEYS, {}, getter=lambda *_: self.fail('network'), now=NOW)
        self.assertEqual([x['status'] for x in value['checks']], ['missing_key'] * 2)

    def test_redirect_is_never_followed_with_provider_key(self):
        self.assertIsNone(NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.invalid'))

    def test_freshness_provenance_and_field_allowlist(self):
        for field, value in [('commit', 'b' * 40), ('run_id', '124'), ('run_attempt', 2),
                             ('repository', 'other/repo'), ('email', 'private@example.invalid')]:
            altered = report(); altered[field] = value
            with self.assertRaises(ValueError): validate(altered)
        with self.assertRaises(ValueError): validate(report(), NOW + timedelta(hours=4))
        with self.assertRaises(ValueError): validate(report(), NOW - timedelta(minutes=6))
        altered = report(); altered['checks'][0]['key'] = 'must-not-leak'
        with self.assertRaises(ValueError): validate(altered)
        altered = report(); altered['checks'][0]['signals'] = ['healthy', 'exhausted']
        with self.assertRaises(ValueError): validate(altered)


class Reader:
    def __init__(self, *, value=None, conclusion='success', path='provider-health-report.json'):
        self.value = value or report(); self.conclusion = conclusion; self.path = path
    def request(self, path, archive=False):
        if archive:
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, 'w') as out: out.writestr(self.path, json.dumps(self.value))
            return buf.getvalue()
        if 'artifacts?' in path:
            return {'total_count': 1, 'artifacts': [{'id': 44, 'name': 'provider-health-report', 'expired': False, 'size_in_bytes': 1024}]}
        if '/runs?' in path:
            return {'workflow_runs': [{'id': 123, 'run_attempt': 1, 'head_sha': 'a' * 40, 'head_branch': 'main',
                'head_repository': {'full_name': 'example/media'}, 'path': '.github/workflows/provider-api-health.yml',
                'status': 'completed', 'conclusion': self.conclusion, 'event': 'schedule'}]}
        return {'default_branch': 'main'}


class AggregationTests(unittest.TestCase):
    def test_activation_mail_is_explicit_and_uses_its_own_dedupe_key(self):
        calls = []
        result = send_activation_test(worker='https://example.invalid', signing_key='x',
                                     mailer=lambda **kwargs: calls.append(kwargs) or {'sent': True})
        self.assertTrue(result['sent'])
        self.assertEqual(calls[0]['severity'], 'info')
        self.assertEqual(calls[0]['dedupe_key'], 'provider-health:activation-test')
        self.assertIn('测试', calls[0]['subject'])
        self.assertIn('不代表供应商发生故障', calls[0]['text'])

    def test_archive_redirect_strips_auth_and_rejects_unknown_hosts(self):
        for location, accepted in [('https://objects.example.blob.core.windows.net/object?sig=opaque', True),
                                    ('https://evil.invalid/object', False),
                                    ('https://blob.core.windows.net.evil.invalid/object', False),
                                    ('http://objects.blob.core.windows.net/object', False)]:
            first, second = MagicMock(), MagicMock()
            first.open.side_effect = urllib.error.HTTPError('https://api.github.com/artifact', 302, '',
                                                            {'Location': location}, io.BytesIO())
            second.open.return_value.read.return_value = b'zip-bytes'
            with patch('urllib.request.build_opener', side_effect=[first, second]):
                if accepted:
                    self.assertEqual(GitHubReader('private-token').request('artifact', archive=True), b'zip-bytes')
                    self.assertEqual(second.open.call_args.args, (location,))
                else:
                    with self.assertRaises(ReportUnavailable): GitHubReader('private-token').request('artifact', archive=True)
                    second.open.assert_not_called()

    def test_oversized_report_is_rejected_before_json_read(self):
        value = report(); value['extra'] = 'x' * 40000
        with self.assertRaises(ReportUnavailable): read_consumer('example/media', Reader(value=value), NOW)

    def test_current_report_identity_and_exact_archive(self):
        self.assertEqual(read_consumer('example/media', Reader(), NOW), report())
        for reader in [Reader(conclusion='failure'), Reader(path='../secret.json')]:
            with self.assertRaises(ReportUnavailable): read_consumer('example/media', reader, NOW)
        value = report(); value['checks'].pop()
        with self.assertRaises(ReportUnavailable): read_consumer('example/media', Reader(value=value), NOW)

    def test_incident_fingerprint_ignores_run_and_balance_movement(self):
        first = report(); first['checks'][0].update(status='low_balance', signals=['low_balance'])
        second = copy.deepcopy(first); second['run_id'] = '456'; second['checked_at'] = (NOW + timedelta(hours=1)).isoformat()
        self.assertEqual(incident_groups([first])[0]['dedupe_key'], incident_groups([second])[0]['dedupe_key'])
        second['checks'][0].update(status='exhausted', signals=['exhausted'])
        self.assertNotEqual(incident_groups([first])[0]['dedupe_key'], incident_groups([second])[0]['dedupe_key'])

    def test_healthy_silent_and_real_issue_uses_existing_mailer(self):
        self.assertEqual(send_groups([report()], worker='https://example.invalid', signing_key='x',
                                      mailer=lambda **_: self.fail('healthy mail')), [])
        value = report(); value['checks'][0].update(status='exhausted', signals=['exhausted'])
        calls = []
        def mailer(**kwargs):
            calls.append(kwargs); return {'sent': True, 'deduplicated': True}
        results = send_groups([value], worker='https://example.invalid', signing_key='secret', mailer=mailer)
        self.assertTrue(results[0]['sent']); self.assertTrue(results[0]['deduplicated'])
        self.assertEqual(calls[0]['dedupe_hours'], 24)
        self.assertEqual(calls[0]['severity'], 'critical')
        self.assertNotIn('private-sentinel', calls[0]['text'])

    def test_missing_report_links_to_consumer_workflow(self):
        value = {'repository': 'example/media', 'run_id': '', 'checked_at': NOW.isoformat(),
                 'checks': [{'provider': 'monitor', 'slot': 'PROVIDER_HEALTH_REPORT',
                             'status': 'report_unavailable', 'signals': ['report_unavailable']}]}
        calls = []
        send_groups([value], worker='https://example.invalid', signing_key='x',
                    mailer=lambda **kwargs: calls.append(kwargs) or {'sent': True})
        self.assertIn('https://github.com/example/media/actions/workflows/provider-api-health.yml', calls[0]['text'])
        self.assertNotIn('/actions/runs/', calls[0]['text'])


if __name__ == '__main__':
    unittest.main()
