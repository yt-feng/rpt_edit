import io
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
import urllib.error
from unittest.mock import patch

import inspect_legacy_mineru as target

BATCH='12345678-1234-4234-8234-123456789abc'
BATCH2='22345678-1234-4234-8234-123456789abc'
TOKEN='private-token-sentinel'


def batch(ids=None, identity=BATCH):
    return {'batch_id':identity,'credential_slot':'MINER_U','expected_data_ids':ids if ids is not None else ['file-a','file-b'],'run_id':'12345','job_id':'23456'}


def request(rows=None):
    return {'schema_version':1,'batches':rows if rows is not None else [batch()]}


def response(rows=None, **overrides):
    payload={'code':0,'data':{'batch_id':BATCH,'extract_result':rows if rows is not None else [
        {'data_id':'file-a','state':'done','full_zip_url':'https://provider.invalid/private-a?secret=value'},
        {'data_id':'file-b','state':'done','full_zip_url':'https://provider.invalid/private-b?secret=value'}]}}
    payload.update(overrides)
    return json.dumps(payload).encode()


class FakeResponse(io.BytesIO):
    status=200
    def __init__(self, body, headers=None):
        super().__init__(body);self.headers=headers or {}


class ReadOnlyTests(unittest.TestCase):
    def test_completed_batch_is_not_original_byte_or_token_proof(self):
        public, private=target.classify_response(200,response(),batch())
        self.assertTrue(public['identified_complete']);self.assertTrue(public['all_succeeded'])
        self.assertFalse(public['original_source_bytes_proven'])
        self.assertFalse(public['historical_token_fingerprint_proven'])
        self.assertEqual(private['input'],batch())
        output=json.dumps(public)
        for text in ('private-a','secret=value','file-a','MINER_U',TOKEN):self.assertNotIn(text,output)

    def test_pending_batch_retains_complete_membership_without_accepting_completion(self):
        rows=[{'data_id':'file-a','state':'pending'},{'data_id':'file-b','state':'running'}]
        public,_=target.classify_response(200,response(rows),batch())
        self.assertTrue(public['membership_proven']);self.assertFalse(public['identified_complete'])
        self.assertEqual(public['state_counts'],{'pending':1,'running':1})

    def test_failed_terminal_member_is_complete_but_not_success(self):
        rows=[{'data_id':'file-a','state':'done','full_zip_url':'https://provider.invalid/x'}, {'data_id':'file-b','state':'failed','err_msg':TOKEN}]
        public,_=target.classify_response(200,response(rows),batch())
        self.assertTrue(public['identified_complete']);self.assertFalse(public['all_succeeded'])
        self.assertNotIn(TOKEN,json.dumps(public))

    def test_unknown_original_membership_is_never_inferred_from_response(self):
        public,_=target.classify_response(200,response(),batch([]))
        self.assertEqual(public['category'],'membership_unknown')
        self.assertFalse(public['membership_proven']);self.assertFalse(public['all_succeeded'])

    def test_missing_unexpected_duplicate_and_invalid_members_reject_membership(self):
        cases=[([{'data_id':'file-a','state':'pending'}],'missing_member_count',1),
               ([{'data_id':'file-a','state':'pending'},{'data_id':'other','state':'pending'}],'unknown_member_count',1),
               ([{'data_id':'file-a','state':'pending'},{'data_id':'file-a','state':'pending'}],'duplicate_member_count',1),
               ([{'data_id':'file-a','state':['done']}],'invalid_row_count',1)]
        for rows,metric,expected in cases:
            with self.subTest(metric=metric):
                public,_=target.classify_response(200,response(rows),batch())
                self.assertFalse(public['membership_proven']);self.assertEqual(public[metric],expected)

    def test_done_without_result_url_is_not_success(self):
        public,_=target.classify_response(200,response([{'data_id':'file-a','state':'done'}]),batch(['file-a']))
        self.assertTrue(public['identified_complete']);self.assertFalse(public['all_succeeded'])
        self.assertEqual(public['completed_result_url_missing_count'],1)

    def test_malformed_provider_contract_does_not_become_completion(self):
        samples=[b'not-json',json.dumps({'data':{'extract_result':[]}}).encode(),response(code=False),
                 response(data={'batch_id':BATCH2,'extract_result':[]}),response(data={'extract_result':[]})]
        for raw in samples:
            with self.subTest(raw=raw[:30]):
                public,_=target.classify_response(200,raw,batch())
                self.assertFalse(public['all_succeeded']);self.assertFalse(public['identified_complete'])

    def test_http_status_is_fixed_and_raw_errors_stay_private(self):
        for status,category in [(401,'http_unauthorized'),(403,'http_forbidden'),(404,'http_not_found'),(302,'http_redirect_blocked'),(500,'http_application_error')]:
            public,_=target.classify_response(status,TOKEN.encode(),batch())
            self.assertEqual(public['category'],category);self.assertNotIn(TOKEN,json.dumps(public))

    def test_input_identity_and_membership_validation_precedes_any_get(self):
        values=[]
        for field,value in [('batch_id','https://attacker.invalid'),('credential_slot',[]),('run_id',True),('expected_data_ids',['same','same']),('expected_data_ids',['../invalid'])]:
            row=batch();row[field]=value;values.append(request([row]))
        values.append(request([batch(),batch()]))
        values.append({'schema_version':True,'batches':[batch()]})
        for value in values:
            getter=lambda *args: self.fail('invalid input caused a provider request')
            with self.subTest(value=value),self.assertRaises(target.InputError):
                target.inspect_batches(value,{'MINER_U':TOKEN},getter=getter)

    def test_network_stop_prevents_next_batch_and_preserves_no_submission_receipt(self):
        calls=[]
        def getter(*args):
            calls.append(args);raise target.NetworkStop(TOKEN)
        public,private=target.inspect_batches(request([batch(),batch(identity=BATCH2)]),{'MINER_U':TOKEN},getter=getter)
        self.assertEqual(len(calls),1);self.assertTrue(public['network_stop'])
        self.assertEqual(public['uninspected_count'],1)
        for key in ('provider_posts','paid_requests','new_submissions'):self.assertEqual(public[key],0)
        self.assertNotIn(TOKEN,json.dumps(public));self.assertEqual(private['batches'],[])

    def test_missing_or_invalid_credential_causes_zero_requests(self):
        for value in (None,'','bad\ncredential',[]):
            public,_=target.inspect_batches(request(),{'MINER_U':value},getter=lambda *args:self.fail('unexpected GET'))
            self.assertEqual(public['provider_gets'],0);self.assertEqual(public['batches'][0]['category'],'credential_unavailable')

    def test_get_once_is_fixed_get_with_no_redirect_handler_or_retry(self):
        calls=[]
        class Opener:
            def open(self,req,timeout):
                calls.append(req)
                return FakeResponse(b'{}',{'Content-Length':'2'})
        with patch.object(target.urllib.request,'build_opener',return_value=Opener()) as build:
            status,raw=target.get_once(target.ENDPOINT+BATCH,TOKEN,20)
        self.assertEqual((status,raw),(200,b'{}'));self.assertEqual(len(calls),1)
        self.assertEqual(calls[0].get_method(),'GET');self.assertIsNone(calls[0].data)
        self.assertEqual(calls[0].full_url,target.ENDPOINT+BATCH)
        self.assertIsInstance(build.call_args.args[0],target.NoRedirect)
        self.assertIsNone(target.NoRedirect().redirect_request(None,None,302,'',{},'https://attacker.invalid'))

    def test_network_error_is_sanitized_and_never_retried(self):
        with patch.object(target.urllib.request,'build_opener') as build:
            build.return_value.open.side_effect=urllib.error.URLError(TOKEN)
            with self.assertRaises(target.NetworkStop) as caught:target.get_once(target.ENDPOINT+BATCH,TOKEN,20)
            self.assertEqual(build.return_value.open.call_count,1)
        self.assertNotIn(TOKEN,str(caught.exception))

    def test_oversized_and_truncated_reads_stop_without_raw_public_body(self):
        for body,headers,error in [(b'{}',{'Content-Length':str(target.MAX_BODY+1)},target.ResponseBounds),
                                   (b'x'*(target.MAX_BODY+1),{},target.ResponseBounds),
                                   (b'{}',{'Content-Length':'10'},target.NetworkStop)]:
            with patch.object(target.urllib.request,'build_opener') as build:
                build.return_value.open.return_value=FakeResponse(body,headers)
                with self.assertRaises(error):target.get_once(target.ENDPOINT+BATCH,TOKEN,20)
        public,private=target.classify_response(200,b'x'*(target.MAX_BODY+1),batch())
        self.assertEqual(public['category'],'response_size');self.assertNotIn('raw_response_base64',private)

    def test_private_receipt_permissions_are_restricted_even_if_file_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'receipt.json';p.write_text('old');p.chmod(0o644)
            target.write_private(p,{'secret':TOKEN})
            self.assertEqual(stat.S_IMODE(p.stat().st_mode),0o600)
            linked=Path(tmp)/'link.json';linked.symlink_to(p)
            with self.assertRaises(OSError):target.write_private(linked,{'changed':True})
            self.assertEqual(json.loads(p.read_text()),{'secret':TOKEN})

    def test_main_cannot_contact_provider_outside_actions(self):
        with patch.dict(os.environ,{'GITHUB_ACTIONS':'false'}),patch.object(target,'inspect_batches') as inspect:
            self.assertEqual(target.main(),1);inspect.assert_not_called()

    def test_main_cannot_use_secrets_from_an_unreviewed_actions_branch(self):
        with patch.dict(os.environ, {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/feature',
                                   'GITHUB_EVENT_NAME': 'workflow_dispatch'}), patch.object(target, 'inspect_batches') as inspect:
            self.assertEqual(target.main(), 1)
            inspect.assert_not_called()


if __name__=='__main__':unittest.main()
