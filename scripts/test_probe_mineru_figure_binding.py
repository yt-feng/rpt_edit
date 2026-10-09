"""Exact real PDF gate classification and cache-only read boundaries."""
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import fitz
from test_mineru_figure_sources import Fixture
from test_mineru_result_cache import MemoryR2
from mineru_task_ledger import Ledger,FileStore,digest,encoded
from mineru_result_cache import ResultCache
import probe_mineru_figure_binding as probe
from recover_durable_mineru_sources import MANIFEST,OPTIONS,PRODUCER


def pack(root):
    output=io.BytesIO()
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('full.md',(root.parent/'source_mineru.md').read_bytes())
        for path in root.rglob('*'):
            if path.is_file(): archive.writestr(path.relative_to(root).as_posix(),path.read_bytes())
    return output.getvalue()


class Provider:
    def __init__(self,binding): self.binding=binding; self.gets=0
    def poll(self,*_):
        self.gets+=1
        return [{'data_id':self.binding['id'],'state':'done','full_zip_url':'https://PRIVATE.invalid/DO_NOT_DOWNLOAD'}]
    def submit(self,*_): raise AssertionError('No provider POST')
    def upload(self,*_): raise AssertionError('No provider upload')


class ProbeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.fixture=Fixture(self.root/'fixture')
    def compare(self):
        return probe.compare_cached_pdf(self.fixture.original,pack(self.fixture.raw),
                                        original_sha256=digest(self.fixture.original.read_bytes()))
    def change_embedded(self,operation):
        path=self.fixture.raw/'source.pdf'
        with fitz.open(path) as document:
            operation(document)
            raw=document.tobytes(no_new_id=True)
        path.write_bytes(raw)
    def test_equal_original_has_no_text_paths_pixels_or_source_handoff(self):
        result=self.compare()
        self.assertEqual((result['stage'],result['status'],result['checked_page_count']),('complete','checked',1))
        self.assertTrue(result['all_selected_pages_equal'])
        encoded_result=json.dumps(result)
        for value in ('Verified source page','Figure 1','original.pdf','source.pdf','images/','PRIVATE'):
            self.assertNotIn(value,encoded_result)
    def test_page_count_gate_is_distinct(self):
        self.change_embedded(lambda doc:doc.new_page())
        result=self.compare()
        self.assertEqual((result['stage'],result['checked_page_count']),('page_count_or_encryption',0))
        self.assertEqual((result['original_pages'],result['embedded_pages']),(1,2))
    def test_geometry_gate_still_renders_both_annotation_modes(self):
        self.change_embedded(lambda doc:doc[0].set_rotation(90))
        result=self.compare(); page=result['pages'][0]
        self.assertEqual(result['stage'],'page_geometry')
        self.assertFalse(page['geometry_equal'])
        self.assertFalse(page['viewport_equal'])
        self.assertIn('annots_true',page); self.assertIn('annots_false',page)
    def test_rotation_normalization_is_diagnosed_without_weakening_original_gate(self):
        original=self.fixture.original
        with fitz.open(original) as doc:
            doc[0].set_rotation(90); raw=doc.tobytes(no_new_id=True)
        original.write_bytes(raw)
        with fitz.open(stream=raw,filetype='pdf') as doc:
            doc[0].remove_rotation(); normalized=doc.tobytes(no_new_id=True)
        (self.fixture.raw/'source.pdf').write_bytes(normalized)
        result=self.compare(); page=result['pages'][0]
        self.assertEqual(result['stage'],'page_geometry')
        self.assertTrue(page['viewport_equal'])
        self.assertTrue(page['default_rgb_equal'])
        self.assertTrue(page['annots_false_equal'])
        self.assertFalse(result['all_selected_pages_equal'])
    def test_provider_page_size_gate_keeps_default_pixel_comparison(self):
        self.fixture=Fixture(self.root/'size',actual_size=(398,500))
        result=self.compare(); page=result['pages'][0]
        self.assertEqual(result['stage'],'provider_page_size')
        self.assertTrue(page['geometry_equal']); self.assertFalse(page['provider_size_equal'])
        self.assertTrue(page['default_rgb_equal'])
    def test_actual_content_change_differs_with_and_without_annotations(self):
        self.change_embedded(lambda doc:doc[0].draw_rect(fitz.Rect(10,40,30,60),fill=(1,0,0)))
        result=self.compare(); page=result['pages'][0]
        self.assertEqual(result['stage'],'rgb_pixels')
        self.assertFalse(page['default_rgb_equal']); self.assertFalse(page['annots_false_equal'])
        self.assertGreater(page['annots_true']['diff_pixel_ratio'],0)
        self.assertIsNotNone(page['annots_true']['diff_bbox'])
    def test_annotation_change_is_classified_but_never_accepted(self):
        def annotate(doc):
            annotation=doc[0].add_rect_annot(fitz.Rect(20,40,100,100))
            annotation.set_colors(stroke=(1,0,0),fill=(1,1,0)); annotation.update()
        self.change_embedded(annotate)
        result=self.compare(); page=result['pages'][0]
        self.assertEqual(result['stage'],'rgb_pixels')
        self.assertFalse(page['default_rgb_equal']); self.assertTrue(page['annots_false_equal'])
        self.assertEqual((page['original_objects']['annotation_count'],page['embedded_objects']['annotation_count']),(0,1))
        self.assertFalse(result['all_selected_pages_equal'])
    def prepared(self):
        input_dir=self.root/'input'; input_dir.mkdir()
        original=input_dir/'selected.pdf'; original.write_bytes(self.fixture.original.read_bytes())
        raw_manifest=encoded([{'process_local_path':'selected.pdf','content_sha256':digest(original.read_bytes()),
            'dropbox_path':'/zip_backup/261009/selected.pdf','name':'PRIVATE.pdf'}])
        (input_dir/MANIFEST).write_bytes(raw_manifest)
        store=FileStore(self.root/'ledger')
        ledger=Ledger(store,None,'dropbox','https://mineru.net',OPTIONS,[('MINER_U','SECRET_TOKEN')])
        binding=ledger.bind(original,original.name); ledger.provider=Provider(binding)
        key='batches/'+'1'*32
        task={'schema':1,'key':key,'scope':'dropbox','endpoint':'https://mineru.net','options':OPTIONS,
              'token_identity':next(iter(ledger.tokens)),'files':[binding],'state':'accepted','batch_id':'fixed-root'}
        store.put(key,task); store.put('sources/'+binding['id'],{'schema':1,'binding':binding,'batch_key':key})
        cache=ResultCache(MemoryR2(),'private')
        lineage={'batch_key':key,'parent_batch_key':key,'batch_id':'fixed-root','data_id':binding['id'],'child_ordinal':0}
        cache.put(binding,lineage,pack(self.fixture.raw))
        return input_dir,ledger,cache,binding
    def test_entire_probe_reads_exact_cache_without_any_writes_or_result_url_download(self):
        input_dir,ledger,cache,binding=self.prepared()
        before={p:p.read_bytes() for p in ledger.store.root.rglob('*.json')}
        r2_before=copy.deepcopy(cache.client.objects)
        with patch.object(ledger.store,'put',side_effect=AssertionError('Ledger write')), \
             patch.object(cache,'put',side_effect=AssertionError('Cache write')), \
             patch('consume_legacy_mineru.download_once',side_effect=AssertionError('Provider result GET')):
            result=probe.probe(ledger,cache,input_dir,1,'261009',1)
        self.assertEqual(result['provider_gets'],1)
        self.assertEqual(result['source_binding_sha256'],binding['id'])
        self.assertEqual(result['comparison']['stage'],'complete')
        self.assertFalse(result['production_acceptance'])
        for key in ('provider_posts','provider_uploads','provider_zip_downloads','canonical_ledger_writes','cache_writes'):
            self.assertEqual(result[key],0)
        self.assertEqual(before,{p:p.read_bytes() for p in ledger.store.root.rglob('*.json')})
        self.assertEqual(r2_before,cache.client.objects)
        for private in ('PRIVATE','SECRET_TOKEN','https://','selected.pdf'):
            self.assertNotIn(private,json.dumps(result))
    def test_missing_cache_stops_without_cdn_fallback(self):
        input_dir,ledger,cache,_=self.prepared(); cache.client.objects.clear()
        with self.assertRaisesRegex(probe.ProbeError,'selected_cache_missing'):
            probe.probe(ledger,cache,input_dir,1,'261009',1)
        self.assertEqual(ledger.provider.gets,1)
    def test_changed_frozen_original_stops_before_provider_get(self):
        input_dir,ledger,cache,_=self.prepared(); (input_dir/'selected.pdf').write_bytes(b'%PDF changed')
        with self.assertRaises(ValueError): probe.probe(ledger,cache,input_dir,1,'261009',1)
        self.assertEqual(ledger.provider.gets,0)
    def test_corrupted_claim_stops_before_provider_get(self):
        input_dir,ledger,cache,binding=self.prepared()
        claim,version=ledger.store.get('sources/'+binding['id']); claim['binding']['size']+=1
        ledger.store.put('sources/'+binding['id'],claim,version)
        with self.assertRaises(ValueError): probe.probe(ledger,cache,input_dir,1,'261009',1)
        self.assertEqual(ledger.provider.gets,0)
    def test_provider_get_bound_and_write_denials(self):
        provider=probe.ReadOnlyProvider(Provider({'id':'a'*64}))
        for _ in range(4): provider.poll('root','token',20)
        with self.assertRaisesRegex(probe.ProbeError,'provider_get_bound'): provider.poll('root','token',20)
        with self.assertRaisesRegex(probe.ProbeError,'provider_post_forbidden'): provider.submit()
        with self.assertRaisesRegex(probe.ProbeError,'provider_upload_forbidden'): provider.upload()
        with self.assertRaisesRegex(probe.ProbeError,'private_write_forbidden'): probe.ReadOnlyR2Client(None).put_object()
    def test_producer_context_requires_complete_original_main_and_exact_bounded_ordinal(self):
        metadata={'id':123,'status':'completed','path':PRODUCER,'head_branch':'main',
                  'repository':{'full_name':'owner/repo'},'head_sha':'a'*40}
        self.assertEqual(probe.validate_request(metadata,'123','261009',40,39,'owner/repo'),'a'*40)
        for change in ({'status':'in_progress'},{'head_branch':'feature'},{'path':'other.yml'}):
            with self.assertRaises(ValueError):
                probe.validate_request(dict(metadata,**change),'123','261009',40,39,'owner/repo')
        with self.assertRaises(probe.ProbeError): probe.validate_request(metadata,'123','261009',40,41,'owner/repo')
    def test_bounded_time_stops_rendering(self):
        with self.assertRaisesRegex(probe.ProbeError,'probe_deadline'):
            probe.compare_cached_pdf(self.fixture.original,pack(self.fixture.raw),
                original_sha256=digest(self.fixture.original.read_bytes()),clock=lambda:10,deadline=9)


if __name__=='__main__': unittest.main(verbosity=2)
