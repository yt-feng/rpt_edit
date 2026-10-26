import hashlib
import json
import unittest
from verify_portal_ui_hotfix_live import identity, verify, verify_english_account_session

ORIGIN = 'https://portal.example.invalid'

class Response:
    def __init__(self, value, status=200, headers=None):
        self.content = value if isinstance(value, bytes) else json.dumps(value).encode()
        self.status_code = status
        self.headers = headers or {}
    def json(self):
        return json.loads(self.content)

class Acceptance(unittest.TestCase):
    def fixture(self, english_key='tenant_auth_session'):
        pages = {'charts.html': b'charts-with-new-analytics-hash', 'report.html': b'report-with-new-app-hash',
                 'assets/app.js': b'const AUTH_SESSION_KEY = "tenant_auth_session";',
                 'assets/english-commentary.js': f'const SESSION = "{english_key}";'.encode()}
        scripts = ''.join('<script defer src="/'+name+'?v='+hashlib.sha256(body).hexdigest()[:12]+'"></script>'
                          for name, body in pages.items() if name.startswith('assets/')).encode()
        pages.update({'en/index.html': scripts+b'public-preview-index',
                      'en/blog/20261024-aaaaaaaaaaaaaaaa.html': scripts+b'public-preview-only'})
        receipt = {'slot': 'b', 'release_id': '2'*32, 'tree_sha256': '3'*64,
                   'previous': {'schema_version': 1, 'slot': 'a', 'release_id': '1'*32, 'tree_sha256': '4'*64},
                   'changed_files': {name: {'size': len(body), 'sha256': hashlib.sha256(body).hexdigest()} for name, body in pages.items()}}
        class Session:
            def __init__(self): self.calls = []; self.mutate = False; self.corrupt = False; self.private = False; self.pages = pages
            def get(self, url, **kwargs):
                self.calls.append(url)
                assert kwargs['allow_redirects'] is False
                path = url[len(ORIGIN):].split('?')[0]
                if path == '/.well-known/edge-state':
                    state = identity(receipt)
                    if self.mutate and len(self.calls) > 1: state['release_id'] = '5'*32
                    return Response(state)
                if path == '/api/health': return Response({'ok': True})
                if path == '/api/course/full/access': return Response({}, 401)
                if path == '/charts.html': return Response(b'', 301, {'Location': '/charts'})
                name = 'charts.html' if path == '/charts' else 'en/index.html' if path == '/en/' else path[1:]
                raw = pages[name] + (b'corrupt' if self.corrupt else b'')
                return Response(raw)
            def post(self, url, **kwargs):
                self.calls.append(url)
                assert kwargs['json'] == {'id': '20261024-aaaaaaaaaaaaaaaa'}
                return Response({'error': 'login_required'} if not self.private else {'blocks': ['private']}, 401 if not self.private else 200, {'Cache-Control': 'private, no-store'})
        return receipt, Session()

    def test_exact_candidate_and_anonymous_boundaries(self):
        receipt, session = self.fixture()
        result = verify(ORIGIN, receipt, session)
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(result['english_account_session'], 'matched')
        self.assertTrue(any('/assets/app.js?v=' in call for call in session.calls))
        self.assertIn(ORIGIN+'/charts', session.calls)
        self.assertNotIn(ORIGIN+'/charts.html', session.calls)
        self.assertFalse(any('/download' in call for call in session.calls))

    def test_exact_fingerprints_do_not_hide_a_deployed_session_key_mismatch(self):
        receipt, session = self.fixture(english_key='portal_auth_session')
        with self.assertRaisesRegex(ValueError, 'session keys differ'):
            verify(ORIGIN, receipt, session)

    def test_unchanged_account_asset_is_checked_from_the_preview_script_reference(self):
        receipt, session = self.fixture()
        del receipt['changed_files']['assets/app.js']
        result = verify(ORIGIN, receipt, session)
        self.assertEqual(result['english_account_session'], 'matched')
        self.assertTrue(any('/assets/app.js?v=' in call for call in session.calls))

    def test_missing_duplicate_or_external_account_script_references_are_rejected(self):
        receipt, session = self.fixture()
        page = session.pages['en/index.html']
        app_ref = page.split(b'</script>', 1)[0]+b'</script>'
        for broken in (page.replace(app_ref, b''), page+app_ref,
                       page.replace(b'src="/assets/app.js', b'src="https://other.invalid/assets/app.js')):
            with self.assertRaisesRegex(ValueError, 'reference is missing or ambiguous'):
                verify_english_account_session(ORIGIN, broken, session)

    def test_referenced_asset_must_match_its_version_fingerprint(self):
        receipt, session = self.fixture()
        page = session.pages['en/index.html']
        session.pages['assets/app.js'] += b'changed'
        with self.assertRaisesRegex(ValueError, 'fingerprint differs'):
            verify_english_account_session(ORIGIN, page, session)

    def test_stale_bytes_wrong_state_and_exposed_body_fail(self):
        for flag in ('corrupt', 'mutate', 'private'):
            receipt, session = self.fixture(); setattr(session, flag, True)
            with self.assertRaises(ValueError): verify(ORIGIN, receipt, session)

    def test_previous_check_only_reads_state_and_rejects_changed_release(self):
        receipt, session = self.fixture()
        with self.assertRaises(ValueError): verify(ORIGIN, receipt, session, expect_previous=True)
        self.assertEqual(len(session.calls), 1)
        session.get = lambda *a, **k: Response(receipt['previous'])
        self.assertTrue(verify(ORIGIN, receipt, session, expect_previous=True)['previous_unchanged'])

    def test_non_https_or_injected_origins_rejected_before_network(self):
        for origin in ('http://portal.example.invalid', ORIGIN+'/private', 'https://user:pass@portal.example.invalid', ORIGIN+'?target=x'):
            receipt, session = self.fixture()
            with self.assertRaises(ValueError): verify(origin, receipt, session)
            self.assertEqual(session.calls, [])

if __name__ == '__main__': unittest.main()
