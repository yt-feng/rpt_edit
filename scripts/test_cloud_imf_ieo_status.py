"""Mock-only IEO headers; no HTTP/session is opened in these tests."""
import json
import unittest
from unittest.mock import Mock, patch
import cloud_imf_ieo_status as p


class StatusTests(unittest.TestCase):
    def sessions(self):
        sessions, responses = [], []
        for _ in range(2):
            session = Mock(); session.__enter__ = Mock(return_value=session); session.__exit__ = Mock()
            current = [Mock(status_code=200, url=url) for _, url in p.TARGETS]
            session.get.side_effect = current
            sessions.append(session); responses.extend(current)
        return sessions, responses

    def test_six_header_only_gets_in_direct_then_cloud_order_no_body_read(self):
        sessions, responses = self.sessions()
        with patch.object(p,'require_approval'), patch('requests.Session',side_effect=sessions):
            result=p.observe_headers('socks5h://127.0.0.1:12345')
        self.assertEqual([row['route'] for row in result['rows']],['direct']*3+['cloud_client']*3)
        self.assertEqual(len(result['rows']),6);self.assertFalse(result['accepted'])
        for session in sessions:
            self.assertIs(session.trust_env,False)
            self.assertEqual([call.args[0] for call in session.get.call_args_list],[url for _,url in p.TARGETS])
            self.assertTrue(all(call.kwargs==dict(stream=True,allow_redirects=False,timeout=(10,20))
                                for call in session.get.call_args_list))
            session.__exit__.assert_called_once()
        self.assertEqual(sessions[0].proxies,{})
        self.assertEqual(sessions[1].proxies,{'http':'socks5h://127.0.0.1:12345','https':'socks5h://127.0.0.1:12345'})
        for response in responses:
            response.close.assert_called_once()
            self.assertEqual(set(response._mock_children),{'close'})
        self.assertNotIn('12345',json.dumps(result))

    def test_failures_and_redirects_never_expose_exception_text_or_request_headers(self):
        import requests
        sessions,responses=self.sessions()
        responses[1].status_code=302;responses[1].url='https://user:SECRET@bad.invalid/'
        sessions[1].get.side_effect=[requests.exceptions.ProxyError('SECRET endpoint'),
                                   requests.exceptions.ReadTimeout('SECRET token'),RuntimeError('SECRET')]
        with patch.object(p,'require_approval'),patch('requests.Session',side_effect=sessions):result=p.observe_headers('private')
        self.assertTrue(result['rows'][1]['redirected']);self.assertIsNone(result['rows'][1]['final_official_url'])
        self.assertEqual([row['category'] for row in result['rows'][3:]],['proxy_connection_failed','read_timeout','request_failed'])
        self.assertNotIn('SECRET',json.dumps(result));self.assertNotIn('private',json.dumps(result))

    def test_guard_precedes_sessions(self):
        with patch.object(p,'require_approval',side_effect=ValueError('guard')),patch('requests.Session') as session:
            with self.assertRaises(ValueError):p.observe_headers('unused')
            session.assert_not_called()


if __name__ == '__main__':unittest.main()
