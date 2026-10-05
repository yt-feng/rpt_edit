"""Offline strict-first delivery, exact identity, active lease and cloud scopes."""
from datetime import datetime, timedelta, timezone
import json
import ssl
import subprocess
import unittest
from unittest.mock import Mock, patch

from consume_legacy_mineru import NetworkStop, ResultHTTPError
import mineru_daily_result_transport as d
import mineru_pinned_result_transport as p
import test_mineru_pinned_result_transport as fixtures
from test_mineru_pinned_result_transport import Pool, Response
from test_probe_mineru_result_tls import metadata_output

NOW = datetime(2026, 10, 6, 12, 0, tzinfo=timezone.utc)
WORKFLOW = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
ENV = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'schedule',
       'GITHUB_REF': 'refs/heads/main', 'GITHUB_REPOSITORY': 'example/research',
       'GITHUB_WORKFLOW_REF': 'example/research/' + WORKFLOW + '@refs/heads/main'}
URL = 'https://' + p.HOST + '/result.zip?signature=PRIVATE'


def authentication(now=NOW, workflow=WORKFLOW, event='schedule'):
    return {'schema_version': 1, 'policy': d.POLICY, 'auth_mode': p.AUTH_MODE,
            'pki_verified_now': False, 'historical_chain_verified': True, 'historical_ca_checks': 2,
            'leaf_sha256': p.LEAF_SHA256, 'leaf_not_after_utc': p.LEAF_EXPIRY.isoformat(),
            'peer_chain_sha256': [p.LEAF_SHA256, 'a' * 64], 'preflight_tls_connections': 1,
            'preflight_http_requests': 0, 'issued_at_utc': now.isoformat(),
            'expires_at_utc': (now + timedelta(minutes=15)).isoformat(),
            'repository': 'example/research', 'workflow_path': workflow, 'event': event}


class DailyDeliveryTests(unittest.TestCase):
    def make(self, response=None, **runner_options):
        leaf_hash, runner, calls = fixtures.AuthenticationTests().setup_runner(**runner_options)
        response = response or Response()
        pool = Pool(response)
        factory = Mock(return_value=pool)
        strict = Mock(side_effect=NetworkStop('tls_certificate_expired'))
        return leaf_hash, runner, calls, response, pool, factory, strict

    def test_strict_success_never_reads_cloud_context_clock_or_pin_even_for_new_certificate(self):
        runner, factory, now = Mock(), Mock(), Mock(side_effect=AssertionError('no lease needed'))
        strict = Mock(return_value=b'strict verified bytes')
        self.assertEqual(d.download_result('https://new-official-result.invalid/result',
                         strict_downloader=strict, env={}, now=now, runner=runner, pool_factory=factory),
                         (b'strict verified bytes', None))
        runner.assert_not_called(); factory.assert_not_called(); now.assert_not_called()

    def test_only_exact_expired_certificate_category_can_start_preflight(self):
        errors = [NetworkStop('network_stop'), NetworkStop('tls_certificate_expired', 'extra'),
                  ResultHTTPError(403), TimeoutError('PRIVATE'), ssl.SSLError('PRIVATE')]
        for error in errors:
            runner, factory = Mock(), Mock()
            with self.subTest(error=type(error).__name__), self.assertRaises(type(error)) as raised:
                d.download_result(URL, strict_downloader=Mock(side_effect=error), env=ENV,
                                  runner=runner, pool_factory=factory)
            self.assertIs(raised.exception, error)
            runner.assert_not_called(); factory.assert_not_called()

    def test_only_allowlisted_main_cloud_workflows_can_recover(self):
        for change in ({'GITHUB_ACTIONS': 'false'}, {'GITHUB_REF': 'refs/heads/topic'},
                       {'GITHUB_EVENT_NAME': 'pull_request'}, {'GITHUB_WORKFLOW_REF': 'other'},
                       {'GITHUB_REPOSITORY': ''}, {'GITHUB_EVENT_NAME': []}):
            runner, factory = Mock(), Mock()
            with self.subTest(change=change), self.assertRaisesRegex(NetworkStop, '^daily_cloud_context_required$'):
                d.download_result(URL, strict_downloader=Mock(side_effect=NetworkStop('tls_certificate_expired')),
                                  env=ENV | change, now=lambda: NOW, runner=runner, pool_factory=factory)
            runner.assert_not_called(); factory.assert_not_called()
        for workflow, events in d.WORKFLOWS.items():
            for event in events:
                env = ENV | {'GITHUB_WORKFLOW_REF': 'example/research/' + workflow + '@refs/heads/main',
                             'GITHUB_EVENT_NAME': event}
                self.assertEqual(d._cloud_context(env)['workflow_path'], workflow)
        for workflow in ('.github/workflows/mineru-api-smoke.yml',
                         '.github/workflows/market-views-mineru-recovery.yml'):
            with self.assertRaises(NetworkStop):
                d._cloud_context(ENV | {'GITHUB_WORKFLOW_REF': 'example/research/' + workflow + '@refs/heads/main'})

    def test_other_host_url_credentials_port_or_redirect_origin_never_start_preflight(self):
        for url in ('https://other.invalid/a', 'https://' + p.HOST + '.attacker.invalid/a',
                    'https://token@' + p.HOST + '/a', 'http://' + p.HOST + '/a',
                    'https://' + p.HOST + ':8443/a', 'https://127.0.0.1/a'):
            runner, factory = Mock(), Mock()
            with self.subTest(url=url), self.assertRaises(NetworkStop):
                d.download_result(url, strict_downloader=Mock(side_effect=NetworkStop('tls_certificate_expired')),
                                  env=ENV, now=lambda: NOW, runner=runner, pool_factory=factory)
            runner.assert_not_called(); factory.assert_not_called()

    def test_fresh_daily_lease_after_old_manual_cutoff_reuses_full_identity_checks(self):
        leaf_hash, runner, calls, response, pool, factory, strict = self.make()
        with patch.object(p, 'LEAF_SHA256', leaf_hash):
            payload, auth = d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                                            runner=runner, pool_factory=factory)
            self.assertEqual(d.validate_daily_authentication(auth, now=lambda: NOW, env=ENV), auth)
        self.assertEqual(payload, b'complete bytes')
        self.assertEqual(auth['policy'], d.POLICY)
        self.assertEqual(datetime.fromisoformat(auth['expires_at_utc']) - NOW, timedelta(minutes=15))
        self.assertNotIn('cutoff_utc', auth)
        self.assertNotIn('PRIVATE', json.dumps(auth))
        commands = [row[0] for row in calls]
        self.assertEqual(sum(command[1] == 's_client' for command in commands), 1)
        verifies = [command for command in commands if command[1] == 'verify']
        self.assertEqual(len(verifies), 2)
        self.assertNotIn('-CAfile', verifies[0]); self.assertIn('-CAfile', verifies[1])
        for command in verifies:
            self.assertIn('-verify_hostname', command)
            self.assertEqual(command[command.index('-attime') + 1], str(int(p.LEAF_EXPIRY.timestamp()) - 1))
        options = factory.call_args.kwargs
        self.assertEqual(options['assert_fingerprint'], leaf_hash)
        self.assertEqual(options['ssl_minimum_version'], ssl.TLSVersion.TLSv1_2)
        self.assertIs(options['retries'], False)
        self.assertEqual(pool.calls[0][1]['headers'], {'Accept-Encoding': 'identity'})
        self.assertFalse(pool.calls[0][1]['redirect'])
        self.assertEqual(len(pool.calls), 1)
        strict.assert_called_once_with(URL)
        self.assertTrue(response.closed); self.assertTrue(pool.closed)
        manual_runner = Mock()
        manual_env = ENV | {'GITHUB_EVENT_NAME': 'workflow_dispatch',
                           'GITHUB_WORKFLOW_REF': 'example/research/' + p.WORKFLOW + '@refs/heads/main'}
        with self.assertRaisesRegex(p.PinnedTransportError, 'pinned_auth_window_closed'):
            p.prepare_authentication(env=manual_env, now=lambda: NOW, runner=manual_runner)
        manual_runner.assert_not_called()

    def test_valid_pki_other_chain_error_or_unknown_leaf_never_gets_pinned(self):
        for values in ({'code': 0, 'exit_code': 0}, {'code': 62}, {'depth': 1}, {'historical_exit': 1}):
            leaf_hash, runner, _, _, _, factory, strict = self.make(**values)
            with self.subTest(values=values), patch.object(p, 'LEAF_SHA256', leaf_hash), self.assertRaises(NetworkStop):
                d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                                  runner=runner, pool_factory=factory)
            factory.assert_not_called()
        _, runner, _, _, _, factory, strict = self.make()
        with self.assertRaisesRegex(NetworkStop, '^fixed_leaf_fingerprint_mismatch$'):
            d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                              runner=runner, pool_factory=factory)
        factory.assert_not_called()

    def test_current_intermediate_and_its_expiry_bound_the_lease(self):
        for expiry, succeeds in (('Oct  6 12:03:00 2026 GMT', True), ('Oct  6 11:59:59 2026 GMT', False)):
            leaf_hash, base_runner, _, _, _, factory, strict = self.make()
            # The fixture is PEM/base64, so identify intermediate by DER hash.
            def wrapped(command, **kwargs):
                if command[:2] == ['openssl', 'x509']:
                    import hashlib
                    actual = hashlib.sha256(ssl.PEM_cert_to_DER_cert(kwargs['input'].decode())).hexdigest()
                    if actual != leaf_hash:
                        return subprocess.CompletedProcess(command, 0, metadata_output(kwargs['input'], not_after=expiry), b'')
                return base_runner(command, **kwargs)
            with self.subTest(expiry=expiry), patch.object(p, 'LEAF_SHA256', leaf_hash):
                if succeeds:
                    _, auth = d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                                              runner=wrapped, pool_factory=factory)
                    self.assertEqual(datetime.fromisoformat(auth['expires_at_utc']) - NOW, timedelta(minutes=3))
                else:
                    with self.assertRaisesRegex(NetworkStop, '^peer_intermediate_not_current$'):
                        d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                                          runner=wrapped, pool_factory=factory)
                    factory.assert_not_called()

    def test_redirect_truncation_http_or_fingerprint_failure_never_retries_or_returns_bytes(self):
        for response in (Response(status=302), Response(status=403), Response(headers={'Content-Length': '999'})):
            leaf_hash, runner, _, _, pool, factory, strict = self.make(response=response)
            with patch.object(p, 'LEAF_SHA256', leaf_hash), self.assertRaises(NetworkStop):
                d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                                  runner=runner, pool_factory=factory)
            self.assertEqual(len(pool.calls), 1)
        leaf_hash, runner, _, response, pool, factory, strict = self.make()
        pool.request = Mock(side_effect=ssl.SSLError('PRIVATE signature secret'))
        with patch.object(p, 'LEAF_SHA256', leaf_hash), self.assertRaisesRegex(NetworkStop, '^pinned_result_transport_failed$'):
            d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: NOW,
                              runner=runner, pool_factory=factory)
        self.assertEqual(pool.request.call_count, 1)

    def test_expiry_during_preflight_and_after_read_never_releases_payload(self):
        for stage in ('preflight', 'read'):
            leaf_hash, base_runner, _, response, pool, factory, strict = self.make()
            clock = [NOW]
            def runner(command, **kwargs):
                result = base_runner(command, **kwargs)
                if stage == 'preflight' and command[:2] == ['openssl', 's_client']:
                    clock[0] += timedelta(minutes=15)
                return result
            real_read = response.read
            def read(*args, **kwargs):
                result = real_read(*args, **kwargs)
                clock[0] += timedelta(minutes=15)
                return result
            if stage == 'read':
                response.read = read
            with self.subTest(stage=stage), patch.object(p, 'LEAF_SHA256', leaf_hash), self.assertRaises(NetworkStop):
                d.download_result(URL, strict_downloader=strict, env=ENV, now=lambda: clock[0],
                                  runner=runner, pool_factory=factory)
            if stage == 'preflight':
                factory.assert_not_called()
            else:
                self.assertEqual(len(pool.calls), 1)
                self.assertTrue(response.closed)


class LeaseTests(unittest.TestCase):
    def test_historical_receipt_can_be_read_after_lease_but_cannot_authorize_new_write_or_connection(self):
        auth = authentication()
        self.assertEqual(d.validate_stored_daily_authentication(auth), auth)
        for now in (NOW - timedelta(seconds=1), NOW + timedelta(minutes=15)):
            with self.subTest(now=now), self.assertRaisesRegex(NetworkStop, '^daily_auth_lease_expired$'):
                d.validate_daily_authentication(auth, now=lambda: now, env=ENV)
        self.assertEqual(d.validate_daily_authentication(auth, now=lambda: NOW, env=ENV), auth)

    def test_receipt_fields_policy_identity_context_and_duration_are_closed(self):
        auth = authentication()
        for change in ({'url': 'PRIVATE'}, {'cutoff_utc': p.CUTOFF.isoformat()}, {'policy': 'manual'},
                       {'pki_verified_now': True}, {'historical_ca_checks': True}, {'leaf_sha256': 'a' * 64},
                       {'expires_at_utc': (NOW + timedelta(minutes=16)).isoformat()}, {'event': []},
                       {'issued_at_utc': NOW.replace(tzinfo=None).isoformat()}, {'schema_version': True}):
            with self.subTest(change=change), self.assertRaises(NetworkStop):
                d.validate_stored_daily_authentication(auth | change)
        for key in auth:
            incomplete = dict(auth); incomplete.pop(key)
            with self.subTest(missing=key), self.assertRaises(NetworkStop):
                d.validate_stored_daily_authentication(incomplete)
        with self.assertRaisesRegex(NetworkStop, '^daily_authentication_context_mismatch$'):
            d.validate_daily_authentication(auth | {'event': 'workflow_dispatch'}, now=lambda: NOW, env=ENV)

    def test_real_connection_hook_checks_before_and_after_handshake(self):
        response = Response(); pool = Pool(response)
        clock = [NOW]
        transport = d.DailyPinnedResultTransport(authentication(), now=lambda: clock[0], env=ENV,
                                                 pool_factory=Mock(return_value=pool))
        transport(URL)
        connection = pool.ConnectionCls(p.HOST)
        clock[0] = NOW + timedelta(minutes=15)
        with patch.object(p.HTTPSConnection, 'connect') as connect, self.assertRaises(NetworkStop):
            connection.connect()
        connect.assert_not_called()
        clock[0] = NOW
        def expire():
            clock[0] += timedelta(minutes=15)
        with patch.object(p.HTTPSConnection, 'connect', side_effect=expire) as connect, self.assertRaises(NetworkStop):
            connection.connect()
        connect.assert_called_once()


if __name__ == '__main__':
    unittest.main()
