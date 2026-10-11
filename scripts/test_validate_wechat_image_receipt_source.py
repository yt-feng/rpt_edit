import copy
import io
import json
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
import validate_wechat_image_receipt_source as source

REPO = 'example/reports'
NAME = 'wechat-drafts-123'


class ReceiptSourceTests(unittest.TestCase):
    def setUp(self):
        self.run = dict(id=123, status='completed', conclusion='success', head_repository={'full_name': REPO})
        self.rows = [dict(id=456, name=NAME, expired=False)]

    def api(self, path):
        if path == 'actions/runs/123':
            return self.run
        return dict(total_count=len(self.rows), artifacts=self.rows)

    def test_cli_unavailable_does_not_matter(self):
        with patch('subprocess.run', side_effect=FileNotFoundError('gh')):
            self.assertTrue(source.validate(REPO, '123', NAME, self.api)['artifact_verified'])

    def test_failed_incomplete_or_foreign_run_not_admitted(self):
        for change in ({'conclusion':'failure'}, {'status':'in_progress'}, {'id':124},
                       {'head_repository':{'full_name':'other/reports'}}):
            original = copy.deepcopy(self.run)
            self.run.update(change)
            with self.assertRaises(source.ReceiptSourceError):
                source.validate(REPO, '123', NAME, self.api)
            self.run = original

    def test_expired_duplicate_or_missing_artifact_not_admitted(self):
        for rows in ([], [dict(id=456,name=NAME,expired=True)],
                     [dict(id=456,name=NAME,expired=False),dict(id=457,name=NAME,expired=False)]):
            self.rows = rows
            with self.assertRaises(source.ReceiptSourceError):
                source.validate(REPO, '123', NAME, self.api)

    def test_complete_pagination_is_required(self):
        calls = []
        def api(path):
            calls.append(path)
            if path == 'actions/runs/123': return self.run
            if 'page=2' in path: return dict(total_count=101,artifacts=self.rows)
            return dict(total_count=101,artifacts=[dict(id=1000+i,name='other-'+str(i),expired=False) for i in range(100)])
        self.assertEqual(source.validate(REPO,'123',NAME,api)['artifact_id'],456)
        self.assertEqual(len(calls),3)
        def incomplete(path):
            if path == 'actions/runs/123': return self.run
            return dict(total_count=101,artifacts=self.rows)
        with self.assertRaises(source.ReceiptSourceError): source.validate(REPO,'123',NAME,incomplete)

    def test_invalid_inputs_never_call_api(self):
        for repo, run, name in ((REPO,'1/../../bad',NAME),('example/reports/extra','123',NAME),(REPO,'123','other')):
            with self.assertRaises(source.ReceiptSourceError):
                source.validate(repo,run,name,lambda _:self.fail('API must not run'))

    def test_rest_get_is_authenticated_bounded_and_does_not_use_cli(self):
        response = io.BytesIO(json.dumps(self.run).encode())
        with patch.object(source,'urlopen',return_value=response) as opening:
            self.assertEqual(source.github_json(REPO,'actions/runs/123','private-test-token'),self.run)
        request = opening.call_args.args[0]
        self.assertEqual(request.get_method(),'GET')
        self.assertEqual(request.get_header('Authorization'),'Bearer private-test-token')
        self.assertEqual(opening.call_args.kwargs['timeout'],30)

    def test_network_or_auth_error_is_sanitized_and_never_retried(self):
        for error, category in ((URLError('private details'),'github_network_stop'),
                                (HTTPError('private-url',403,'private-body',{},None),'github_http_403')):
            with patch.object(source,'urlopen',side_effect=error) as opening:
                with self.assertRaisesRegex(source.ReceiptSourceError,category):
                    source.github_json(REPO,'actions/runs/123','private-test-token')
                self.assertEqual(opening.call_count,1)

    def test_authorization_is_never_followed_to_a_redirect_target(self):
        self.assertIsNone(source.NoRedirect().redirect_request(None,None,302,'Found',{},'https://elsewhere.invalid/'))


if __name__ == '__main__': unittest.main()
