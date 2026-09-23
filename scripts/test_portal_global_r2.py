"""Offline storage regressions; never access R2 or model providers."""
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest import mock
import portal_global_r2 as s

class MemoryR2:
    def __init__(self):self.objects={}
    def put_object(self,**kw):self.objects[kw['Key']]=kw
    def head_object(self,**kw):
        row=self.objects[kw['Key']]
        return {'ContentLength':len(row['Body']),'Metadata':row['Metadata']}
    def get_object(self,**kw):
        if kw['Key'] not in self.objects:
            error=RuntimeError('missing');error.response={'Error':{'Code':'NoSuchKey'}};raise error
        row=self.objects[kw['Key']]
        return {**self.head_object(**kw),'Body':io.BytesIO(row['Body'])}

class StorageTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.client=MemoryR2()
    def cache(self,**changes):
        data={'provider':'hymt','model':s.MODEL_ID,'locales':{'fr':{}}};data.update(changes)
        return gzip.compress(json.dumps(data).encode())
    def test_roundtrip_checks_object_hash_size_and_private_policy(self):
        key=s.object_key('checkpoint','fr');data=self.cache();checksum=s.put(self.client,'b',key,data,s.MAX_CHECKPOINT)
        self.assertEqual(s.get(self.client,'b',key,s.MAX_CHECKPOINT),data)
        self.assertEqual(checksum,hashlib.sha256(data).hexdigest())
        self.assertEqual(self.client.objects[key]['CacheControl'],'private, no-store')
        self.assertEqual(s.object_key('checkpoint','fr'),key)
    def test_only_own_namespace_and_canonical_single_locale(self):
        for kind,code in [('checkpoint','fr,es'),('candidate','zh'),('candidate','../fr'),('candidate','zh-hant'),('state','fr')]:
            with self.assertRaises(ValueError):s.object_key(kind,code)
        with self.assertRaises(ValueError):s.put(self.client,'b','edge-static/state.json',b'x',99)
    def test_404_is_a_cache_miss_but_auth_or_service_errors_are_not(self):
        self.assertIsNone(s.get(self.client,'b',s.object_key('checkpoint','fr'),99,missing_ok=True))
        for code in ('403','AccessDenied','SlowDown'):
            error=RuntimeError('private detail');error.response={'Error':{'Code':code}}
            with mock.patch.object(self.client,'get_object',side_effect=error),self.assertRaises(RuntimeError):
                s.get(self.client,'b',s.object_key('checkpoint','fr'),99,missing_ok=True)
    def test_hash_corruption_is_not_returned(self):
        key=s.object_key('source');s.put(self.client,'b',key,b'abc',99)
        self.client.objects[key]['Body']=b'bad'
        with self.assertRaises(ValueError):s.get(self.client,'b',key,99)
    def test_upload_requires_matching_readback(self):
        with mock.patch.object(self.client,'head_object',return_value={}),self.assertRaises(RuntimeError):
            s.put(self.client,'b',s.object_key('source'),b'x',99)
    def test_archive_roundtrip_and_new_directory_only(self):
        root=self.root/'source';root.mkdir();(root/'index.html').write_text('公开研究')
        (root/'data').mkdir();(root/'data/catalog.json').write_text('{"items":[]}')
        data=s.pack_tree(root);s.unpack_tree(data,self.root/'target')
        self.assertEqual((self.root/'target/index.html').read_bytes(),(root/'index.html').read_bytes())
        with self.assertRaises(ValueError):s.unpack_tree(data,self.root/'target')
    def test_symlink_and_tar_traversal_rejected_before_destination_commit(self):
        root=self.root/'source';root.mkdir();(root/'link').symlink_to('/etc/passwd')
        with self.assertRaises(ValueError):s.pack_tree(root)
        for name,kind in [('../escape',tarfile.REGTYPE),('/escape',tarfile.REGTYPE),('link',tarfile.SYMTYPE),('a//b',tarfile.REGTYPE)]:
            out=io.BytesIO()
            with tarfile.open(fileobj=out,mode='w:gz') as archive:
                member=tarfile.TarInfo(name);member.type=kind;member.size=1 if kind==tarfile.REGTYPE else 0
                archive.addfile(member,io.BytesIO(b'x'))
            with self.assertRaises(ValueError):s.unpack_tree(out.getvalue(),self.root/'bad')
            self.assertFalse((self.root/'bad').exists())
    def test_cache_must_match_model_language_provider_and_bounds(self):
        s.validate_checkpoint(self.cache(),'fr')
        for values in ({'provider':'deepseek'},{'model':'other'},{'locales':{'fr':{},'es':{}}},{'_source_fallbacks':{'fr':1}}):
            with self.assertRaises(ValueError):s.validate_checkpoint(self.cache(**values),'fr')
        with mock.patch.object(s,'MAX_CACHE_JSON',4),self.assertRaises(ValueError):s.validate_checkpoint(self.cache(),'fr')
    def test_workflow_does_not_store_site_or_translation_checkpoint_on_github(self):
        workflow=Path(__file__).parents[1]/'.github/workflows/portal-global-locale-prepare.yml'
        text=workflow.read_text()
        self.assertNotIn('actions/cache',text);self.assertNotIn('actions/upload-artifact',text);self.assertNotIn('actions/download-artifact',text)
        self.assertIn('push-candidate',text);self.assertIn('push-checkpoint',text)
        self.assertNotIn('DEEPSEEK',text);self.assertNotIn('DEEPL',text)
        self.assertIn('max-parallel: 2',text);self.assertIn('runs-on: ubuntu-24.04',text)

if __name__=='__main__':unittest.main()
