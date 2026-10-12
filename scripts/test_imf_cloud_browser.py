"""Offline transport contracts. All HTTP, clients and browser processes are mocks."""
import base64
import contextlib
from copy import deepcopy
import hashlib
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import imf_cloud_browser as b
import imf_cloud_client as c

NODE = ('vless://00000000-0000-0000-0000-000000000001@example.invalid:443'
        '?encryption=none&type=tcp&security=reality&sni=example.invalid&fp=chrome&pbk=' + 'A' * 43)
LANDING = 'https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml'
PDF = 'https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf'
TITLE = 'Republic of Estonia: Consumer Price Index'
PUBLICATION = dict(source_guid='test-guid', source_url='https://www.imf.org/en/publications/test',
                   source_title=TITLE, title='Republic of Estonia', full_title=TITLE,
                   title_variants=['Republic of Estonia', TITLE], doi='10.5089/9798229063937.019',
                   isbn='9798229063937', landing_url=LANDING, identity_sha256='a' * 64,
                   crossref_sha256='b' * 64)
PAGE = dict(stage='metadata', final_url=LANDING, landing_status=200, ready=True, metadata={'citation_doi': [PUBLICATION['doi']],
            'citation_title': [TITLE]}, h1s=[TITLE], download_hrefs=[PDF])
RESULT = dict(stage='download', pdf_url=PDF, landing_status=200, pdf_status=200)
ENV = dict(GITHUB_ACTIONS='true', EXPLICIT_CLOUD_BROWSER_APPROVAL='true', IMF_CLOUD_BROWSER_ENABLED='true')


class BrowserTests(unittest.TestCase):
    def test_exception_category_never_exposes_raw_runtime_text(self):
        self.assertEqual(b.BrowserDownloadError('imf_browser_pdf_title_mismatch').category, 'imf_browser_pdf_title_mismatch')
        self.assertEqual(b.BrowserDownloadError('SECRET https://private.invalid').category, 'imf_browser_download_failed')

    def test_observed_alphabetic_compound_join_requires_exact_word_and_all_other_words(self):
        title = 'Foreign Currency Stablecoins: Initial Considerations on Policies to Manage and Enhance Macro-Financial Stability'
        observed = title.replace('Macro-Financial', 'Macrofinancial')
        self.assertTrue(b.title_words_present(title, observed))
        for bad in (observed.replace('Macrofinancial', 'Microfinancial'),
                    observed.replace('Macrofinancial', 'Macrofinancially'),
                    observed.replace('Foreign Currency', ''), 'Macrofinancial Stability'):
            self.assertFalse(b.title_words_present(title, bad))
        self.assertFalse(b.title_words_present('Mission January 12-16 2026', 'Mission January 1216 2026'))
        self.assertFalse(b.title_words_present('Macro-Financial Policies and Macro Measures',
                                              'Macrofinancial Policies and Measures'))

    def spanish_fixture(self, series):
        issue, isbn, name = (('083', '9798229064521', 'Technical Assistance Reports') if series == '019' else
                            ('071', '9798229062657', 'High-Level Summary Technical Assistance Reports'))
        publication = {**PUBLICATION, 'language': 'en', 'original_language': 'es', 'year': '2026', 'issue': issue, 'series': [name],
                       'source_title': 'Chile: English official report title', 'doi': f'10.5089/{isbn}.{series}',
                       'landing_url': f'https://www.elibrary.imf.org/view/journals/{series}/2026/{issue}/{series}.2026.issue-{issue}-en.xml'}
        if series == '029':
            title = ('Chile – Reporte sobre la misión de asistencia técnica en estadísticas de finanzas públicas; '
                     'Informe del FMI sobre asistencia técnica: Resumen de alto nivel n.º 2026/071; 18 al 29 de mayo de 2026')
            body = ('©2026 Fondo Monetario Internacional HLS/26/71 Resumen de alto nivel sobre informe de asistencia técnica '
                    'Departamento de Estadística Chile – Reporte sobre la misión de asistencia técnica en estadísticas de finanzas públicas')
        else:
            title = ('Chile: Informe de asistencia técnica — Informe sobre la misión de asistencia técnica en estadísticas de las finanzas públicas '
                     '(18 al 29 de mayo de 2026); Informe de asistencia técnica del FMI n.º 26/83; septiembre de 2026')
            body = ('INFORME DE ASISTENCIA TÉCNICA CHILE Informe sobre la misión de asistencia técnica en estadísticas de las finanzas públicas '
                    '(18 al 29 de mayo de 2026) SEPTIEMBRE DE 2026 ©2026 Fondo Monetario Internacional')
        return publication, title, body

    def test_two_observed_spanish_edition_formats_require_full_substantive_title(self):
        for series in ('019', '029'):
            publication, title, body = self.spanish_fixture(series)
            self.assertTrue(b.spanish_series_identity(publication, title, body))
            self.assertFalse(b.title_words_present(publication['source_title'], body))
            for bad in (body.replace('estadísticas', 'inflación'), body.replace('Fondo Monetario Internacional', ''),
                        'Chile 2026 Fondo Monetario Internacional HLS/26/71'):
                self.assertFalse(b.spanish_series_identity(publication, title, bad))

    def test_same_country_wrong_edition_series_or_language_never_accept(self):
        for series in ('019', '029'):
            publication, title, body = self.spanish_fixture(series)
            for change in ({'issue': '082'}, {'year': '2025'}, {'language': 'fr'}, {'series': ['Working Papers']},
                           {'original_language': None}, {'original_language': 'Spanish'},
                           {'series': []}, {'doi': publication['doi'][:-3] + '001'}, {'source_title': 'Peru: Report'}):
                self.assertFalse(b.spanish_series_identity({**publication, **change}, title, body), change)
            for bad in (title.replace('/83', '/82').replace('/071', '/072'), title.replace('2026', '2025').replace('26/83', '25/83'),
                        title.replace('Chile', 'Peru'), title.replace('asistencia técnica del FMI', 'Working Papers del FMI')
                        .replace('Resumen de alto nivel n.', 'Working Paper n.')):
                self.assertFalse(b.spanish_series_identity(publication, bad, body), bad)

    def test_hls_needs_corresponding_unambiguous_body_number_and_country(self):
        publication, title, body = self.spanish_fixture('029')
        for bad in (body.replace('HLS/26/71', ''), body.replace('HLS/26/71', 'HLS/26/72'),
                    body + ' HLS/25/71', body.replace('Chile', 'Chileland')):
            self.assertFalse(b.spanish_series_identity(publication, title, bad))

    def test_spanish_type_label_without_substantive_topic_never_accepts(self):
        publication, title, body = self.spanish_fixture('019')
        generic = 'Chile: Informe de asistencia técnica; ' + title.split('; ', 1)[1]
        self.assertFalse(b.spanish_series_identity(publication, generic, body))

    def test_spanish_pdf_path_still_needs_real_pdf_hash_pages_and_edition(self):
        publication, title, body = self.spanish_fixture('019')
        publication['full_title'] = publication['source_title']
        data = b'%PDF-spanish'; digest = hashlib.sha256(data).hexdigest()
        reader = SimpleNamespace(is_encrypted=False, metadata={'/Title': title}, pages=[SimpleNamespace(extract_text=lambda: body)])
        with tempfile.TemporaryDirectory() as folder, patch.dict(sys.modules, {'pypdf': SimpleNamespace(PdfReader=lambda _: reader)}):
            file = Path(folder) / 'test.pdf'; file.write_bytes(data)
            self.assertEqual(b.verify_pdf(file, publication, 1024, digest)['pages'], 1)
            reader.metadata = {'/Title': title.replace('26/83', '26/82')}
            with self.assertRaisesRegex(b.BrowserDownloadError, 'pdf_title_mismatch'):
                b.verify_pdf(file, publication, 1024, digest)

    def test_optional_evidence_disabled_has_no_filesystem_work(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(b.tempfile, 'mkstemp') as write:
            b.write_public_evidence(PUBLICATION, PAGE)
            write.assert_not_called()

    def test_public_evidence_uses_fixed_bounded_fields_and_redacts_private_urls(self):
        publication = {**PUBLICATION, 'subscription': 'SECRET', 'headers': {'Authorization': 'SECRET'}}
        page = deepcopy(PAGE)
        page.update(cookie='SECRET', stdout='SECRET', final_url='https://user:SECRET@www.elibrary.imf.org/x')
        page['metadata_keys'] = ['citation_title', 'og:description', 'citation_title']
        page['metadata'].update(cookie=['SECRET'], description=['SECRET'], citation_pdf_url=['https://user:SECRET@evil.invalid/x.pdf'])
        page['h1s'] = ['x' * 5000] * 33
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {**ENV, 'IMF_PUBLIC_EVIDENCE_DIR': folder}, clear=True), \
             patch.object(b.sys, 'platform', 'linux'):
            b.write_public_evidence(publication, page)
            files = list(Path(folder).iterdir()); self.assertEqual(len(files), 1)
            self.assertEqual(files[0].name, hashlib.sha256(PUBLICATION['source_guid'].encode()).hexdigest() + '.json')
            encoded = files[0].read_text(); self.assertNotIn('SECRET', encoded)
            record = json.loads(encoded)
            self.assertEqual(set(record), {'schema', 'accepted', 'kind', 'publication', 'page'})
            self.assertFalse(record['accepted'])
            self.assertEqual(len(record['page']['h1s']), 32)
            self.assertEqual(record['page']['final_url'], '[invalid_official_url]')
            self.assertNotIn('cookie', record['page']['metadata'])
            self.assertEqual(record['page']['metadata_keys'], ['citation_title', 'og:description'])

    def test_failed_metadata_is_retained_but_never_accepted(self):
        page = deepcopy(PAGE); page['metadata']['citation_doi'] = ['10.5089/9798229063074.029']
        with self.download_mocks([page]) as (instance, dest, proc, _, _), \
             patch.dict(os.environ, {'IMF_PUBLIC_EVIDENCE_DIR': str(dest.parent / 'evidence')}):
            with self.assertRaisesRegex(b.BrowserDownloadError, 'page_identity_mismatch'):
                instance.download(PUBLICATION, dest, 1024)
            record = json.loads(next((dest.parent / 'evidence').glob('*.json')).read_text())
            self.assertEqual(record['page']['metadata']['citation_doi'], ['10.5089/9798229063074.029'])
            self.assertFalse(record['accepted']); proc.stdin.write.assert_not_called()

    def test_unready_observation_saved_and_never_sends_click_decision(self):
        for status, code in ((200, 'page_not_ready'), (405, 'landing_http_rejected')):
            page = {**PAGE, 'ready': False, 'landing_status': status, 'h1s': [], 'download_hrefs': []}
            with self.download_mocks([page]) as (instance, dest, proc, _, _), \
                 patch.dict(os.environ, {'IMF_PUBLIC_EVIDENCE_DIR': str(dest.parent / 'evidence')}):
                with self.assertRaisesRegex(b.BrowserDownloadError, code):
                    instance.download(PUBLICATION, dest, 1024)
                record = json.loads(next((dest.parent / 'evidence').glob('*.json')).read_text())
                self.assertFalse(record['page']['ready'])
                self.assertEqual(record['page']['landing_status'], status)
                self.assertIn('citation_doi', record['page']['metadata'])
                proc.stdin.write.assert_not_called(); self.assertFalse(dest.exists())

    def test_disabled_enter_is_zero_launch_zero_credentials(self):
        fetch = Mock()
        with patch.dict(os.environ, {}, clear=True), patch.object(b.subprocess, 'Popen') as spawn:
            with b.CloudImfBrowser(fetch_subscription=fetch, decode_subscription=Mock()) as instance:
                self.assertFalse(instance.enabled)
                with self.assertRaisesRegex(b.BrowserDownloadError, 'not_enabled'):
                    instance.download(PUBLICATION, 'unused', 1024)
            fetch.assert_not_called()
            spawn.assert_not_called()

    def test_approval_and_linux_guard_precede_secret_fetch_and_start(self):
        for changes in ({'GITHUB_ACTIONS': ''}, {'EXPLICIT_CLOUD_BROWSER_APPROVAL': ''}, {'platform': 'darwin'}):
            env = {**ENV, **{k: v for k, v in changes.items() if k != 'platform'}}
            with patch.dict(os.environ, env, clear=True), patch.object(b.sys, 'platform', changes.get('platform', 'linux')):
                with b.CloudImfBrowser(fetch_subscription=Mock(), decode_subscription=Mock()) as instance:
                    with patch.object(instance, '_start') as start:
                        with self.assertRaisesRegex(b.BrowserDownloadError, 'cloud_approval_required'):
                            instance.download(PUBLICATION, 'unused', 1024)
                        start.assert_not_called()
                with patch.object(c.socket, 'socket') as socket:
                    with self.assertRaisesRegex(RuntimeError, 'cloud_only'):
                        with c.running_client('unused', {}):
                            self.fail('client started')
                    socket.assert_not_called()

    def test_candidate_order_three_cap_and_base64(self):
        nodes = [NODE.replace('example.invalid:443', f'node{i}.invalid:443') for i in range(5)]
        body = '\n'.join([NODE + '&insecure=1', 'https://other.invalid:443', *nodes])
        selected = b.select_outbounds(body, Mock())
        self.assertEqual([x['server'] for x in selected], ['node0.invalid', 'node1.invalid', 'node2.invalid'])
        encoded = base64.b64encode(nodes[0].encode()).decode()
        self.assertEqual(b.select_outbounds(encoded, lambda x: base64.b64decode(x).decode())[0], selected[0])
        for bad in (NODE + '&unknown=x', NODE + '&fp=chrome', NODE.replace('type=tcp', 'type=ws'),
                    NODE.replace('security=reality', 'security=tls'), NODE + '&allowInsecure=true'):
            with self.assertRaises(b.BrowserDownloadError):
                b.select_outbounds(bad, lambda _: '')

    def test_child_environment_contains_no_credential_or_proxy_settings(self):
        with patch.dict(os.environ, {'PATH': '/bin', 'PROXY_SUBSCRIPTION_URL': 'SECRET',
                                    'HTTPS_PROXY': 'SECRET', 'GH_TOKEN': 'SECRET'}, clear=True):
            env = b.child_environment('socks5h://127.0.0.1:54321')
        self.assertEqual(set(env), {'PATH', 'GITHUB_ACTIONS', 'EXPLICIT_CLOUD_BROWSER_APPROVAL', 'IMF_CLOUD_SOCKS_PORT'})
        self.assertNotIn('SECRET', repr(env))
        for bad in ('socks5h://localhost:42', 'http://127.0.0.1:42', 'socks5h://u:p@127.0.0.1:42',
                    'socks5h://127.0.0.1:42/path', 'socks5h://127.0.0.1:0', 'socks5h://@127.0.0.1:42'):
            with self.assertRaises(b.BrowserDownloadError):
                b.child_environment(bad)

    @contextlib.contextmanager
    def startup(self, statuses):
        events, fetch = [], Mock(return_value='\n'.join([NODE] * 4))
        @contextlib.contextmanager
        def client(*_):
            number = sum(x[0] == 'open' for x in events) + 1
            events.append(('open', number))
            try:
                yield f'socks5h://127.0.0.1:{5000 + number}'
            finally:
                events.append(('close', number))
        responses = [Mock(status_code=x) if isinstance(x, int) else x for x in statuses]
        get = Mock(side_effect=responses)
        with tempfile.TemporaryDirectory() as folder:
            binary = Path(folder) / 'sing-box'; binary.touch()
            env = {**ENV, 'IMF_SING_BOX_BINARY': str(binary), 'PROXY_SUBSCRIPTION_URL': 'SECRET'}
            with patch.dict(os.environ, env, clear=True), patch.object(b.sys, 'platform', 'linux'), \
                 patch.object(b.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout='sing-box version 1.14.3\n')), \
                 patch.object(c, 'running_client', client), \
                 patch.dict(sys.modules, {'curl_cffi': SimpleNamespace(requests=SimpleNamespace(get=get), CurlOpt=SimpleNamespace(NOPROXY=10177))}):
                with b.CloudImfBrowser(fetch_subscription=fetch, decode_subscription=Mock()) as instance:
                    yield instance, get, fetch, events

    def test_one_subscription_bounded_failover_and_batch_reuse(self):
        with self.startup([RuntimeError('SECRET'), 403, 204]) as (instance, get, fetch, events):
            instance._start(); instance._start()
            self.assertEqual(events, [('open', 1), ('close', 1), ('open', 2), ('close', 2), ('open', 3)])
            fetch.assert_called_once_with('SECRET', 8)
            self.assertEqual(get.call_count, 3)
            for call in get.call_args_list:
                self.assertEqual(call.kwargs['curl_options'], {10177: ''})
                self.assertFalse(call.kwargs['allow_redirects'])
                self.assertEqual(call.kwargs['timeout'], 8)
                self.assertTrue(call.kwargs['stream'])
        self.assertEqual(events[-1], ('close', 3))

    def test_all_connectivity_failed_is_cached_no_second_subscription(self):
        with self.startup([403, 403, 403]) as (instance, get, fetch, events):
            for _ in range(2):
                with self.assertRaisesRegex(b.BrowserDownloadError, '^imf_browser_connectivity_rejected$'):
                    instance._start()
            self.assertEqual(get.call_count, 3)
            fetch.assert_called_once()
            self.assertEqual(events[-1], ('close', 3))

    def test_sigterm_restores_handler_and_closes_selected_client(self):
        previous = signal.getsignal(signal.SIGTERM)
        with self.assertRaises(KeyboardInterrupt):
            with self.startup([204]) as (instance, _, _, events):
                instance._start()
                signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
        self.assertEqual(events[-1], ('close', 1))
        self.assertIs(signal.getsignal(signal.SIGTERM), previous)

    def test_ipc_timeout_size_eof_and_invalid_json_are_fixed_codes(self):
        selector = Mock(); selector.__enter__ = Mock(return_value=selector); selector.__exit__ = Mock(return_value=False)
        proc = Mock(); proc.stdout.fileno.return_value = 9
        for chunk, matches, expected in [(b'', [1], 'process_stopped'), (b'[]\n', [1], 'protocol_invalid'),
                  (b'not-json SECRET\n', [1], 'protocol_invalid'), (b'{}\n{}\n', [1], 'protocol_invalid'),
                  (b'x' * (b.MAX_MESSAGE + 1), [1], 'message_limit'), (b'', [], 'phase_timeout')]:
            selector.select.return_value = matches
            with self.subTest(code=expected), patch.object(b.selectors, 'DefaultSelector', return_value=selector), \
                 patch.object(b.os, 'set_blocking'), patch.object(b.os, 'read', return_value=chunk):
                with self.assertRaisesRegex(b.BrowserDownloadError, expected) as error:
                    b.read_message(proc, 1)
                self.assertNotIn('SECRET', str(error.exception))

    @contextlib.contextmanager
    def download_mocks(self, messages):
        proc = Mock(pid=123, poll=Mock(return_value=None), wait=Mock(return_value=0))
        proc.stdin = Mock(); proc.stdout = Mock()
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {**ENV, 'RUNNER_TEMP': folder}, clear=True), \
             patch.object(b.sys, 'platform', 'linux'), patch.object(b.subprocess, 'Popen', return_value=proc) as spawn, \
             patch.object(b, 'read_message', side_effect=messages), patch.object(b.os, 'killpg') as stop:
            with b.CloudImfBrowser(fetch_subscription=Mock(), decode_subscription=Mock()) as instance:
                instance._proxy = 'socks5h://127.0.0.1:5555'
                with patch.object(instance, '_start'):
                    yield instance, Path(folder) / 'result.pdf', proc, spawn, stop

    def test_metadata_timeout_kills_child_before_return(self):
        with self.download_mocks([b.BrowserDownloadError('imf_browser_phase_timeout')]) as (instance, dest, proc, spawn, stop):
            with self.assertRaisesRegex(b.BrowserDownloadError, 'phase_timeout'):
                instance.download(PUBLICATION, dest, 1024)
            stop.assert_called_once_with(123, signal.SIGTERM)
            proc.stdin.write.assert_not_called()
            self.assertFalse(dest.exists()); spawn.assert_called_once()

    def test_historical_source_path_case_is_accepted_by_shared_resolver(self):
        publication = {**PUBLICATION, 'source_url': 'https://www.imf.org/en/Publications/CR/Issues/2026/report'}
        with self.download_mocks([b.BrowserDownloadError('imf_browser_phase_timeout')]) as (instance, dest, _, spawn, _):
            with self.assertRaisesRegex(b.BrowserDownloadError, 'phase_timeout'):
                instance.download(publication, dest, 1024)
            spawn.assert_called_once()  # Passed source validation; no real browser.

    def test_bad_metadata_never_sends_download_command(self):
        page = deepcopy(PAGE); page['metadata']['citation_doi'] = ['10.5089/9798229063074.029']
        with self.download_mocks([page]) as (instance, dest, proc, _, stop):
            with self.assertRaisesRegex(b.BrowserDownloadError, 'page_identity_mismatch'):
                instance.download(PUBLICATION, dest, 1024)
            proc.stdin.write.assert_not_called(); stop.assert_called_once()

    def test_landing_rejected_before_decision_even_if_following_pdf_is_200(self):
        for status in (405, 202, True, '200', None):
            with self.download_mocks([{**PAGE, 'landing_status': status}, RESULT]) as (instance, dest, proc, _, _):
                with self.assertRaisesRegex(b.BrowserDownloadError, 'landing_http_rejected'):
                    instance.download(PUBLICATION, dest, 1024)
                proc.stdin.write.assert_not_called()
                self.assertFalse(dest.exists())

    def test_decision_timeout_and_sigterm_interrupt_clean_child(self):
        for error in (b.BrowserDownloadError('imf_browser_phase_timeout'), KeyboardInterrupt()):
            with self.download_mocks([PAGE, error]) as (instance, dest, proc, _, stop):
                with self.assertRaises(type(error)):
                    instance.download(PUBLICATION, dest, 1024)
                proc.stdin.write.assert_called_once()
                self.assertEqual(json.loads(proc.stdin.write.call_args.args[0]), {'pdf_url': PDF})
                stop.assert_called_once_with(123, signal.SIGTERM)
                self.assertFalse(dest.exists())

    def test_completed_download_returns_exact_proof_and_atomic_file(self):
        data = b'%PDF-mock'; digest = hashlib.sha256(data).hexdigest()
        def verify(path, *_):
            path.write_bytes(data)
            return dict(sha256=digest, bytes=len(data), pages=14)
        with self.download_mocks([PAGE, RESULT]) as (instance, dest, proc, _, _), patch.object(b, 'verify_pdf', verify):
            proof = instance.download(PUBLICATION, dest, 1024)
            self.assertEqual(set(proof), b.PROOF_FIELDS)
            self.assertEqual(proof['title'], TITLE)
            self.assertEqual(proof['sha256'], digest)
            self.assertEqual(dest.read_bytes(), data)
            self.assertEqual(list(dest.parent.glob('.imf-original-*')), [])

    def test_status_downgrade_and_changed_download_never_accept(self):
        for changes in (dict(pdf_status=202), dict(landing_status=403), dict(pdf_url='https://evil.invalid/a.pdf')):
            with self.download_mocks([PAGE, {**RESULT, **changes}]) as (instance, dest, _, _, _):
                with self.assertRaisesRegex(b.BrowserDownloadError, 'download_not_verified'):
                    instance.download(PUBLICATION, dest, 1024)
                self.assertFalse(dest.exists())

    def test_stop_timeout_escalates_and_closes_streams(self):
        proc = Mock(pid=123, poll=Mock(return_value=None))
        proc.wait.side_effect = [subprocess.TimeoutExpired('secret', 8), -9]
        with patch.object(b.os, 'killpg') as stop:
            b.stop_browser(proc)
        self.assertEqual([x.args[1] for x in stop.call_args_list], [signal.SIGTERM, signal.SIGKILL])
        proc.stdin.close.assert_called_once(); proc.stdout.close.assert_called_once()

    def test_atomic_original_rejects_tampering_and_never_overwrites(self):
        with tempfile.TemporaryDirectory() as folder:
            source, dest = Path(folder) / 'src', Path(folder) / 'dest'
            data = b'%PDF-mock'; source.write_bytes(data)
            proof = dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
            dest.write_bytes(b'existing')
            with self.assertRaises(FileExistsError):
                b.publish_original(source, dest, proof)
            self.assertEqual(dest.read_bytes(), b'existing')
            dest.unlink(); source.write_bytes(b'%PDF-evil')
            with self.assertRaisesRegex(b.BrowserDownloadError, 'bytes_changed'):
                b.publish_original(source, dest, proof)
            self.assertFalse(dest.exists())
            self.assertEqual(list(Path(folder).glob('.imf-original-*')), [])

    def test_atomic_original_failed_write_exposes_no_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            source, dest = Path(folder) / 'src', Path(folder) / 'dest'
            data = b'%PDF-mock'; source.write_bytes(data)
            with patch.object(b.os, 'fsync', side_effect=OSError('private')):
                with self.assertRaises(OSError):
                    b.publish_original(source, dest, dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
            self.assertFalse(dest.exists())
            self.assertEqual(list(Path(folder).glob('.imf-original-*')), [])

    def test_pdf_signature_hash_parse_pages_and_full_title_identity(self):
        data = b'%PDF-fixture'; digest = hashlib.sha256(data).hexdigest()
        page = SimpleNamespace(extract_text=lambda: TITLE)
        good = SimpleNamespace(is_encrypted=False, pages=[page] * 14)
        reader = Mock(return_value=good)
        with tempfile.TemporaryDirectory() as folder, patch.dict(sys.modules, {'pypdf': SimpleNamespace(PdfReader=reader)}):
            file = Path(folder) / 'test.pdf'; file.write_bytes(data)
            self.assertEqual(b.verify_pdf(file, PUBLICATION, 1024, digest)['pages'], 14)
            for bad in (SimpleNamespace(is_encrypted=True, pages=[page]), SimpleNamespace(is_encrypted=False, pages=[]),
                        SimpleNamespace(is_encrypted=False, pages=[SimpleNamespace(extract_text=lambda: 'Republic of Estonia Unrelated Report')])):
                reader.return_value = bad
                with self.assertRaises(b.BrowserDownloadError):
                    b.verify_pdf(file, PUBLICATION, 1024)
            reader.side_effect = RuntimeError('SECRET')
            with self.assertRaisesRegex(b.BrowserDownloadError, '^imf_browser_pdf_parse_failed$'):
                b.verify_pdf(file, PUBLICATION, 1024)
            file.write_bytes(b'<!DOCTYPE html>not PDF')
            with self.assertRaisesRegex(b.BrowserDownloadError, 'pdf_bytes_invalid'):
                b.verify_pdf(file, PUBLICATION, 1024)
            file.write_bytes(data)
            with self.assertRaisesRegex(b.BrowserDownloadError, 'pdf_bytes_invalid'):
                b.verify_pdf(file, PUBLICATION, 1024, '0' * 64)


if __name__ == '__main__':
    unittest.main()
