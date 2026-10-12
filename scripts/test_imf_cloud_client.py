"""Pure config/runtime mocks: never bind a real socket or start sing-box."""
import contextlib
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import imf_cloud_client as c

NODE = ('vless://00000000-0000-0000-0000-000000000001@example.invalid:443'
        '?encryption=none&type=tcp&security=reality&sni=example.invalid&fp=chrome&pbk=' + 'A' * 43)


class ClientTests(unittest.TestCase):
    def test_strict_supported_config_has_no_global_network_settings(self):
        outbound = c.build_outbound(NODE)
        self.assertEqual(outbound['type'], 'vless')
        self.assertEqual(outbound['network'], 'tcp')
        self.assertTrue(outbound['tls']['enabled'])
        self.assertNotIn('insecure', outbound['tls'])
        config = c.client_config(outbound, 54321)
        self.assertEqual(set(config), {'log', 'inbounds', 'outbounds'})
        self.assertEqual(config['inbounds'][0]['listen'], '127.0.0.1')
        self.assertEqual(config['inbounds'][0]['type'], 'socks')
        self.assertEqual(config['log'], {'disabled': True})

    def test_unsupported_credentials_and_tls_settings_are_fixed_errors(self):
        bad = [NODE + '&unknown=SECRET', NODE + '&fp=chrome', NODE + '&insecure=1',
               NODE.replace('type=tcp', 'type=ws'), NODE.replace('security=reality', 'security=tls'),
               NODE.replace(':443?', '?'), NODE.replace('000000000001@', '000000000001:SECRET@'),
               NODE + '&sid=xyz', NODE.replace('pbk=' + 'A' * 43, 'pbk=SECRET'), NODE + '&flow=unknown']
        for value in bad:
            with self.assertRaises(c.UnsupportedNode) as error:
                c.build_outbound(value)
            self.assertIn(error.exception.code, c.ERROR_CODES)
            self.assertNotIn('SECRET', str(error.exception))

    @contextlib.contextmanager
    def mocked_runtime(self, check_return=0):
        reserved = Mock()
        reserved.__enter__ = Mock(return_value=reserved); reserved.__exit__ = Mock(return_value=False)
        reserved.getsockname.return_value = ('127.0.0.1', 5555)
        connection = Mock(); connection.__enter__ = Mock(); connection.__exit__ = Mock(return_value=False)
        process = Mock(poll=Mock(return_value=None))
        paths = []
        def check(args, **kwargs):
            path = Path(args[-1]); paths.append(path)
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
            self.assertEqual(stat.S_IMODE(path.parent.stat().st_mode), 0o700)
            self.assertEqual(json.loads(path.read_text())['inbounds'][0]['listen'], '127.0.0.1')
            self.assertEqual(kwargs['timeout'], 8)
            self.assertEqual(kwargs['stderr'], subprocess.DEVNULL)
            return SimpleNamespace(returncode=check_return)
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {
                'GITHUB_ACTIONS': 'true', 'EXPLICIT_CLOUD_BROWSER_APPROVAL': 'true', 'RUNNER_TEMP': folder}, clear=True), \
             patch.object(c.sys, 'platform', 'linux'), patch.object(c.socket, 'socket', return_value=reserved), \
             patch.object(c.socket, 'create_connection', return_value=connection) as connect, \
             patch.object(c.subprocess, 'run', side_effect=check), \
             patch.object(c.subprocess, 'Popen', return_value=process) as spawn:
            yield process, paths, connect, spawn
        for path in paths:
            self.assertFalse(path.exists()); self.assertFalse(path.parent.exists())

    def test_config_permissions_and_cleanup_on_interruption(self):
        with self.mocked_runtime() as (process, paths, connect, spawn):
            with self.assertRaises(KeyboardInterrupt):
                with c.running_client('/mock/binary', c.build_outbound(NODE)) as proxy:
                    self.assertEqual(proxy, 'socks5h://127.0.0.1:5555')
                    self.assertTrue(paths[0].exists())
                    raise KeyboardInterrupt()
            process.terminate.assert_called_once(); process.wait.assert_called_once_with(timeout=3)
            connect.assert_called_once_with(('127.0.0.1', 5555), timeout=0.2)
            spawn.assert_called_once()
            self.assertFalse(paths[0].exists())

    def test_check_failure_never_starts_client_and_removes_config(self):
        with self.mocked_runtime(check_return=1) as (_, paths, connect, spawn):
            with self.assertRaisesRegex(c.UnsupportedNode, '^runtime_check_failed$'):
                with c.running_client('/mock/binary', c.build_outbound(NODE)):
                    self.fail('client started')
            connect.assert_not_called(); spawn.assert_not_called()
            self.assertFalse(paths[0].exists())

    def test_stop_timeout_escalates_without_restart(self):
        with self.mocked_runtime() as (process, _, _, spawn):
            process.wait.side_effect = [subprocess.TimeoutExpired('private', 3), -9]
            with c.running_client('/mock/binary', c.build_outbound(NODE)):
                pass
            process.terminate.assert_called_once(); process.kill.assert_called_once(); spawn.assert_called_once()


if __name__ == '__main__':
    unittest.main()
