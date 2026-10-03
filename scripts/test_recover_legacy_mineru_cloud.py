"""Offline origin, private persistence and resume checks; no provider/model calls."""
import base64
from copy import deepcopy
import io
import json
from pathlib import Path
import tempfile
import ssl
import unittest
from unittest.mock import patch
import urllib.error

import consume_legacy_mineru as c
import recover_legacy_mineru_cloud as r
from inspect_legacy_mineru import canonical
from portal_extended_r2 import R2NotFound, R2TransportError
from test_consume_legacy_mineru import fixture, prepare_fixture, zip_bytes, fake_asset_writer


class Store:
    def __init__(self):self.objects={};self.writes=[]
    def key(self,*parts):return '/'.join((r.PREFIX,*parts))
    def _get(self,key,maximum):
        if key not in self.objects:raise R2NotFound('missing')
        body=self.objects[key]
        if len(body)>maximum:raise ValueError('bound')
        return body
    def _put(self,key,body,metadata):self.writes.append(key);self.objects[key]=body


def origin_fixture():
    receipt,objects,log,manifest,context=fixture()
    p=json.loads(receipt)['producer']; sha='b'*40
    log=b'2026-10-03T00:00:00Z HEAD is now at '+sha[:7].encode()+b' Original source\n'+log
    archive=zip_bytes([('institution_run_manifest.json',manifest),('progress.log',b'private log')])
    value={'run_id':context['run_id'],'job_id':context['job_id'],'artifact_id':'11262148107',
        'artifact_digest':c.digest(archive),'inspection_receipt_sha256':c.digest(receipt),
        'inspection_input_sha256':json.loads(receipt)['input_canonical_sha256'],'inspection_producer':p}
    def run(identity,path,sha,conclusion):
        return {'id':int(identity),'repository':{'full_name':r.REPOSITORY},'head_repository':{'full_name':r.REPOSITORY},
            'head_branch':'main','path':path,'status':'completed','event':'workflow_dispatch','head_sha':sha,
            'run_attempt':1,'conclusion':conclusion}
    root='repos/'+r.REPOSITORY+'/'
    responses={root+f'actions/runs/{p["run_id"]}/attempts/1':run(p['run_id'],'.github/workflows/mineru-legacy-inspect.yml',p['sha'],'success'),
        root+f'actions/runs/{value["run_id"]}':run(value['run_id'],c.WORKFLOW,'d'*40,'failure'),
        root+f'actions/jobs/{value["job_id"]}':{'id':int(value['job_id']),'run_id':int(value['run_id']),
           'name':'fetch-and-build','status':'completed','conclusion':'failure'},
        root+'commits/'+sha[:7]:{'sha':sha},root+f'actions/artifacts/{value["artifact_id"]}':{
            'id':int(value['artifact_id']),'expired':False,'workflow_run':{'id':int(value['run_id'])},
            'digest':'sha256:'+c.digest(archive),'size_in_bytes':len(archive)}}
    code={}
    for path in r.ORIGINAL_CODE:
        raw=('reviewed '+path).encode();code[path]=c.digest(raw)
        responses[root+f'contents/{path}?ref={sha}']={'path':path,'encoding':'base64','content':base64.b64encode(raw).decode()}
    class API:
        def get(self,endpoint):return deepcopy(responses[endpoint])
        def raw(self,endpoint,maximum,redirect=False):
            if endpoint.endswith('/logs'):return log
            if endpoint.endswith('/zip'):return archive
            raise AssertionError(endpoint)
    return value,receipt,objects,API(),responses,code,log,manifest,context


class AuthenticationTests(unittest.TestCase):
    def test_original_execution_sha_and_archive_digest_are_authenticated(self):
        value,receipt,_,api,_,code,log,manifest,_=origin_fixture()
        with patch.object(r,'ORIGINAL_CODE',code):
            got_log,got_manifest,context,authority=r.authenticate(api,value,receipt)
        self.assertEqual(got_log,log);self.assertEqual(got_manifest,manifest)
        self.assertEqual(context['execution_source_sha'],'b'*40)
        self.assertEqual(authority['original_run_head_sha'],'d'*40)
        self.assertEqual(authority['manifest_artifact_zip_sha256'],value['artifact_digest'])
        plan=c.prepare(receipt,origin_fixture()[2].__getitem__,log,manifest,context)
        self.assertEqual(len(plan['members']),5)

    def test_cross_run_job_artifact_and_inspection_producer_are_rejected(self):
        for what in ['job','artifact','producer']:
            value,receipt,_,api,responses,code,*_=origin_fixture()
            if what=='job':responses[f'repos/{r.REPOSITORY}/actions/jobs/{value["job_id"]}']['run_id']=9
            elif what=='artifact':responses[f'repos/{r.REPOSITORY}/actions/artifacts/{value["artifact_id"]}']['workflow_run']['id']=9
            else:responses[f'repos/{r.REPOSITORY}/actions/runs/{value["inspection_producer"]["run_id"]}/attempts/1']['head_sha']='f'*40
            with self.subTest(what=what),patch.object(r,'ORIGINAL_CODE',code),self.assertRaises(c.ConsumerError):
                r.authenticate(api,value,receipt)

    def test_unknown_actual_execution_code_and_archive_bytes_cannot_be_used(self):
        value,receipt,_,api,_,code,*_=origin_fixture()
        with self.assertRaisesRegex(c.ConsumerError,'execution_code'):r.authenticate(api,value,receipt)
        value['artifact_digest']='f'*64
        with patch.object(r,'ORIGINAL_CODE',code),self.assertRaisesRegex(c.ConsumerError,'manifest_artifact'):
            r.authenticate(api,value,receipt)

    def test_manifest_zip_ambiguity_paths_symlinks_and_crc_are_rejected(self):
        for raw in [zip_bytes([('a/institution_run_manifest.json',b'{}'),('b/institution_run_manifest.json',b'{}')]),
                    zip_bytes([('../institution_run_manifest.json',b'{}')]),b'not a zip']:
            with self.assertRaisesRegex(c.ConsumerError,'manifest_archive'):r.manifest_member(raw)

    def test_malformed_request_rejected_without_remote_calls(self):
        value,*_=origin_fixture();value['inspection_producer']['run_id']=1
        with self.assertRaisesRegex(c.ConsumerError,'recovery_request'):r.request(value)


class PersistenceTests(unittest.TestCase):
    def setUp(self):
        t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.temp=Path(t.name)
        self.root=self.temp/'source';self.store=Store()
        raw=zip_bytes([('full.md',b'# Original source\n\nActual report body.')])
        c.materialize(prepare_fixture(),self.root,downloader=lambda _:raw,asset_writer=fake_asset_writer)
        self.value=origin_fixture()[0]
        self.authority={'original_run_head_sha':'d'*40,'execution_code_sha256':r.ORIGINAL_CODE,
            'manifest_artifact_id':self.value['artifact_id'],'manifest_artifact_zip_sha256':self.value['artifact_digest'],
            'inspection_producer':self.value['inspection_producer'],
            'original_context':json.loads((self.root/'_legacy_output_receipt.json').read_bytes())['context']}
        self.owner={'run_id':'37160000000','attempt':'1','sha':'e'*40}

    def test_private_ready_written_after_all_verified_content_and_restores_without_provider(self):
        ready=r.preserve(self.store,self.value,self.root,self.authority,self.owner)
        self.assertTrue(self.store.writes[-1].endswith('/ready.json'))
        self.assertFalse(ready['canonical_task_admission']);self.assertFalse(ready['original_source_bytes_proven'])
        new=self.temp/'restored';restored,receipt=r.restore(self.store,self.value,new)
        self.assertEqual(ready,restored);self.assertEqual(receipt['source_count'],5)
        self.assertEqual(sorted(p.relative_to(new).as_posix() for p in new.rglob('*') if p.is_file()),
                         sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob('*') if p.is_file()))
        c.verify_materialized_output(new,(new/'_legacy_output_receipt.json').read_bytes())

    def test_modified_source_cannot_write_any_private_output(self):
        source=next(self.root.rglob('source_mineru.md'));source.write_bytes(b'changed')
        with self.assertRaises(c.ConsumerError):r.preserve(self.store,self.value,self.root,self.authority,self.owner)
        self.assertEqual(self.store.writes,[])

    def test_write_failure_never_creates_ready_receipt(self):
        original=self.store._put
        def put(key,body,metadata):
            if len(self.store.writes)==2:raise R2TransportError('stop')
            original(key,body,metadata)
        self.store._put=put
        with self.assertRaises(R2TransportError):r.preserve(self.store,self.value,self.root,self.authority,self.owner)
        self.assertFalse(any(k.endswith('/ready.json') for k in self.store.objects))

    def test_changed_private_file_hash_and_unproven_flags_fail_restore(self):
        r.preserve(self.store,self.value,self.root,self.authority,self.owner)
        key=next(k for k in self.store.objects if '/files/' in k);self.store.objects[key]+=b'bad'
        with self.assertRaises(c.ConsumerError):r.restore(self.store,self.value,self.temp/'bad')
        self.assertFalse((self.temp/'bad').exists())

    def test_immutable_existing_object_cannot_be_overwritten(self):
        self.store.objects['private']=b'first'
        with self.assertRaisesRegex(c.ConsumerError,'immutable_output_differs'):r.immutable(self.store,'private',b'other')
        self.assertEqual(self.store.writes,[])


class RemoteBoundaryTests(unittest.TestCase):
    def test_provider_expired_certificate_is_reported_without_retry_or_verify_bypass(self):
        error=ssl.SSLCertVerificationError(1,'private TLS details');error.verify_code=10
        opener=unittest.mock.MagicMock();opener.open.side_effect=urllib.error.URLError(error)
        with patch('consume_legacy_mineru.urllib.request.build_opener',return_value=opener):
            with self.assertRaisesRegex(c.NetworkStop,'tls_certificate_expired'):
                c.download_once('https://private.example/result')
        self.assertEqual(opener.open.call_count,1)

    def test_transport_failure_has_one_attempt_and_no_fallback(self):
        api=r.Github('private-token')
        with patch.object(api.opener,'open',side_effect=urllib.error.URLError('private network error')) as call:
            with self.assertRaises(c.NetworkStop):api.raw('repos/'+r.REPOSITORY+'/actions/runs/1',1024)
        self.assertEqual(call.call_count,1)

    def test_github_redirect_storage_get_has_no_authorization_and_no_second_redirect(self):
        api=r.Github('private-token');error=urllib.error.HTTPError('https://api.github.com/private',302,'Found',
             {'Location':'https://private.example/signed?secret=private'},io.BytesIO())
        class Response:
            status=200;headers={'Content-Length':'2'}
            def __enter__(self):return self
            def __exit__(self,*args):pass
            def read(self,n):body=getattr(self,'body',b'{}');self.body=b'';return body
        with patch.object(api.opener,'open',side_effect=[error,Response()]) as call:
            self.assertEqual(api.raw('repos/'+r.REPOSITORY+'/actions/jobs/1/logs',1024,redirect=True),b'{}')
        self.assertEqual(call.call_count,2)
        self.assertIsNone(call.call_args_list[1].args[0].get_header('Authorization'))
        self.assertIn('Authorization',call.call_args_list[0].args[0].headers)

    def test_local_cli_is_rejected_before_private_or_remote_read(self):
        value=origin_fixture()[0]
        with patch.dict('os.environ',{'GITHUB_ACTIONS':'false'}),patch('sys.argv',['recover','recover','--request',json.dumps(value),'--output','/missing']),patch.object(r,'single_attempt_store') as store:
            with self.assertRaisesRegex(c.ConsumerError,'main_workflow_required'):r.main()
        store.assert_not_called()


if __name__=='__main__':unittest.main()
