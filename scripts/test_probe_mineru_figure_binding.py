"""Exact real PDF gate classification and cache-only read boundaries."""
import copy
import io
import json
import subprocess
import struct
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock,patch
import zipfile

import fitz
from test_mineru_figure_sources import Fixture,visual
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


def output_intent_fixture(*,pages=2):
    """Self-created ICC gamma profile; PDFium drops its catalog reference."""
    from PIL import ImageCms
    profile=bytearray(ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes())
    for index in range(struct.unpack('>I',profile[128:132])[0]):
        position=132+index*12;tag=profile[position:position+4]
        offset,_=struct.unpack('>II',profile[position+4:position+12])
        if tag in (b'rTRC',b'gTRC',b'bTRC'):
            if profile[offset:offset+4]!=b'para':raise AssertionError('Synthetic ICC parametric TRC expected')
            profile[offset+12:offset+16]=struct.pack('>i',int(1.5*65536))
    with fitz.open() as document:
        for _ in range(pages):
            page=document.new_page(width=400,height=500)
            page.insert_text((20,30),'Synthetic color-managed source',fontsize=12)
            page.draw_rect(fitz.Rect(35,100,185,260),fill=(.3,.5,.7))
        xref=document.get_new_xref();document.update_object(xref,'<</N 3>>')
        document.update_stream(xref,bytes(profile),compress=True)
        document.xref_set_key(document.pdf_catalog(),'OutputIntents',
            f'[<</Type/OutputIntent/S/GTS_PDFX/DestOutputProfile {xref} 0 R'
            '/OutputConditionIdentifier(SYNTHETIC_PRIVATE_PROFILE)>>]')
        return document.tobytes(no_new_id=True)


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
    def test_semantic_text_change_is_distinguished_without_plaintext(self):
        self.change_embedded(lambda doc:doc[0].insert_text((50,150),'CHANGED SECRET',fontsize=10))
        result=self.compare(); page=result['pages'][0]; semantic=page['semantic_diagnostics']
        self.assertFalse(semantic['text']['equal'])
        self.assertTrue(semantic['images']['equal']); self.assertTrue(semantic['drawings']['equal'])
        self.assertNotEqual(semantic['text']['original']['characters_sha256'],semantic['text']['embedded']['characters_sha256'])
        self.assertFalse(semantic['content_streams']['equal'])
        self.assertNotIn('CHANGED',json.dumps(result)); self.assertNotIn('Helvetica',json.dumps(result))
        selected=page['selected_visual_differences'][0]
        self.assertGreater(selected['body_diff_pixel_count'],0)
        self.assertNotEqual(selected['union_crop_original_rgb_sha256'],selected['union_crop_embedded_rgb_sha256'])

    def test_semantic_displayed_image_change_ignores_unrelated_resource_inventory(self):
        from PIL import Image
        image=io.BytesIO(); Image.new('RGB',(20,20),(255,0,0)).save(image,'PNG')
        self.change_embedded(lambda doc:doc[0].insert_image(fitz.Rect(50,120,100,170),stream=image.getvalue()))
        result=self.compare(); semantic=result['pages'][0]['semantic_diagnostics']
        self.assertTrue(semantic['text']['equal']); self.assertTrue(semantic['drawings']['equal'])
        self.assertFalse(semantic['images']['equal'])
        self.assertEqual(semantic['images']['embedded']['placement_count'],1)
        self.assertEqual(semantic['images']['original']['placement_count'],0)
        displayed=semantic['images']['embedded']['images'][0]
        self.assertEqual((displayed['width'],displayed['height']),(20,20))
        self.assertEqual(len(displayed['content_sha256']),64); self.assertEqual(len(displayed['pixel_sha256']),64)
        self.assertFalse(semantic['content_streams']['equal'])

    def test_semantic_vector_change_and_diff_outside_selected_crop(self):
        self.change_embedded(lambda doc:doc[0].draw_rect(fitz.Rect(5,40,15,50),fill=(1,0,0)))
        result=self.compare(); page=result['pages'][0]; semantic=page['semantic_diagnostics']
        self.assertTrue(semantic['text']['equal']); self.assertTrue(semantic['images']['equal'])
        self.assertFalse(semantic['drawings']['equal']); self.assertFalse(semantic['content_streams']['equal'])
        selected=page['selected_visual_differences'][0]
        self.assertEqual(selected['body_diff_pixel_count'],0)
        self.assertEqual(selected['union_crop_diff_pixel_count'],0)
        self.assertEqual(selected['union_crop_original_rgb_sha256'],selected['union_crop_embedded_rgb_sha256'])
        self.assertFalse(result['all_selected_pages_equal'])

    def test_image_dimensions_are_bounded_before_hashing_or_decoding(self):
        page=Mock()
        page.get_image_info.return_value=[{'width':20001,'height':1}]
        with patch('fitz.Pixmap',side_effect=AssertionError('Pixel decode before bounds')):
            with self.assertRaisesRegex(probe.ProbeError,'displayed_image_dimensions_bound'):
                probe._image_semantics(page)
        page.get_image_info.assert_called_once_with(hashes=False,xrefs=False)
        page.get_images.assert_not_called(); page.get_text.assert_not_called()

    def test_image_aggregate_and_mask_bounds_precede_extraction(self):
        page=Mock()
        page.get_image_info.return_value=[{'width':2000,'height':2000}]*2
        with self.assertRaisesRegex(probe.ProbeError,'displayed_image_decoded_bytes_bound'):
            probe._image_semantics(page)
        page.get_text.assert_not_called()
        page.get_image_info.return_value=[{'width':20,'height':20}]
        page.get_images.return_value=[(1,2,20,20)]
        page.parent.xref_get_key.side_effect=lambda _ref,key:('int','999999') if key in {'Width','Height'} else ('null','null')
        with patch('fitz.Pixmap',side_effect=AssertionError('Mask decode before bounds')):
            with self.assertRaisesRegex(probe.ProbeError,'displayed_image_dimensions_bound'):
                probe._image_semantics(page)
        page.get_text.assert_not_called()

    def test_displayed_image_and_different_size_softmask_are_independently_hashed(self):
        from PIL import Image
        image=io.BytesIO(); Image.new('RGB',(20,20),(255,0,0)).save(image,'PNG')
        with fitz.open() as document:
            page=document.new_page()
            xref=page.insert_image(fitz.Rect(20,20,120,120),stream=image.getvalue())
            mask=document.get_new_xref()
            document.update_object(mask,'<</Type/XObject/Subtype/Image/Width 9/Height 13/ColorSpace/DeviceGray/BitsPerComponent 8>>')
            document.update_stream(mask,bytes([128])*(9*13))
            document.xref_set_key(xref,'SMask',str(mask)+' 0 R')
            result=probe._image_semantics(page)
        self.assertEqual(result['status'],'checked')
        displayed=result['images'][0]
        self.assertEqual((displayed['base_image']['width'],displayed['base_image']['height']),(20,20))
        self.assertEqual((displayed['displayed_block_mask']['width'],displayed['displayed_block_mask']['height']),(9,13))
        self.assertEqual(len(displayed['displayed_block_mask']['pixel_sha256']),64)
        self.assertFalse(displayed['resource_candidates_are_exact_binding'])
        self.assertIn('Matte',displayed['resource_candidate_metadata'][0]['mask_dictionary_fields_sha256'])
        self.assertNotIn('DeviceGray',json.dumps(result))

    def test_unused_resource_softmask_is_not_claimed_as_displayed_mask(self):
        from PIL import Image
        def png(size):
            stream=io.BytesIO(); Image.new('RGB',size,(255,0,0)).save(stream,'PNG'); return stream.getvalue()
        with fitz.open() as document:
            page=document.new_page()
            page.insert_image(fitz.Rect(20,20,120,120),stream=png((20,20)))
            original_contents=page.get_contents()
            unused=page.insert_image(fitz.Rect(130,20,230,120),stream=png((40,40)))
            mask=document.get_new_xref()
            document.update_object(mask,'<</Type/XObject/Subtype/Image/Width 9/Height 13/ColorSpace/DeviceGray/BitsPerComponent 8>>')
            document.update_stream(mask,bytes([128])*(9*13))
            document.xref_set_key(unused,'SMask',str(mask)+' 0 R')
            document.xref_set_key(page.xref,'Contents','['+' '.join(str(ref)+' 0 R' for ref in original_contents)+']')
            result=probe._image_semantics(page)
        self.assertEqual(result['placement_count'],1)
        self.assertEqual(result['resource_inventory_count'],2)
        self.assertIsNone(result['images'][0]['displayed_block_mask'])
        self.assertFalse(result['images'][0]['resource_candidate_metadata'][0]['has_soft_mask'])

    def test_render_context_detects_group_and_transparency_without_private_values(self):
        with fitz.open(self.fixture.original) as document:
            page=document[0]
            before=probe._render_resource_context(page)
            document.xref_set_key(page.xref,'Group','<</S/Transparency/I true/K false/CS/DeviceRGB>>')
            state=document.get_new_xref()
            document.update_object(state,'<</Type/ExtGState/ca 0.5/CA 0.7/BM/Multiply>>')
            resources=int(document.xref_get_key(page.xref,'Resources')[1].split()[0])
            document.xref_set_key(resources,'ExtGState','<</SECRET_RESOURCE '+str(state)+' 0 R>>')
            document.xref_set_key(document.pdf_catalog(),'OCProperties','<</PRIVATE_LABEL(SECRET_TEXT)>>')
            after=probe._render_resource_context(page)
        self.assertNotEqual(before['sha256'],after['sha256'])
        self.assertTrue(after['page_group']['I']['present'])
        self.assertEqual(after['page_transparency']['entry_count'],1)
        self.assertTrue(after['page_transparency']['entries'][0]['fields']['ca']['present'])
        self.assertTrue(after['catalog']['OCProperties']['present'])
        for private in ('SECRET_RESOURCE','SECRET_TEXT','PRIVATE_LABEL','Multiply','DeviceRGB'):
            self.assertNotIn(private,json.dumps(after))

    def test_resource_fingerprint_does_not_treat_xref_renumbering_as_difference(self):
        with fitz.open(self.fixture.original) as document:
            first,second=document.get_new_xref(),document.get_new_xref()
            for reference in (first,second):
                document.update_object(reference,'<</S/Transparency/I true/CS/DeviceRGB>>')
            document.xref_set_key(document[0].xref,'Group',str(first)+' 0 R')
            before=probe._pdf_key_fingerprint(document,document[0].xref,'Group')
            document.xref_set_key(document[0].xref,'Group',str(second)+' 0 R')
            after=probe._pdf_key_fingerprint(document,document[0].xref,'Group')
        self.assertEqual(before,after)

    def test_selected_crop_uses_exact_fractional_source_viewport(self):
        self.fixture=Fixture(self.root/'fractional',actual_size=(400.3,500.8))
        self.change_embedded(lambda doc:doc[0].insert_text((50,150),'CHANGED',fontsize=10))
        page=self.compare()['pages'][0]
        selected=page['selected_visual_differences'][0]
        self.assertEqual(selected['source_rect_size'],page['original_geometry']['rect'][2:])
        self.assertNotEqual(selected['source_rect_size'],page['provider_size'])
        self.assertEqual(selected['point_to_pixel'],[300/72,0,0,300/72,0,0])
        self.assertGreater(selected['union_crop_diff_pixel_count'],0)

    def test_pdfium_rewrite_imports_all_real_pages_with_recorded_runtime(self):
        with fitz.open(self.fixture.original) as original:
            original.new_page().insert_text((30,50),'SECOND PAGE CONTENT')
            raw=original.tobytes(no_new_id=True)
        rewritten,runtime=probe._pdfium_rewrite(raw)
        self.assertEqual(runtime['pypdfium2'],'5.13.0')
        self.assertTrue(runtime['pdfium'])
        import mineru_figure_sources as figures
        with fitz.open(stream=raw,filetype='pdf') as original, fitz.open(stream=rewritten,filetype='pdf') as derived:
            self.assertEqual((len(original),len(derived)),(2,2))
            for index in range(2):
                left,right=figures._render(original[index]),figures._render(derived[index])
                try: self.assertEqual(probe._difference(left,right)['diff_pixel_count'],0)
                finally: left.close(); right.close()

    def test_pdfium_rewrite_rejects_incomplete_whole_document_import(self):
        import pypdfium2 as pdfium
        with fitz.open(self.fixture.original) as original:
            original.new_page()
            raw=original.tobytes(no_new_id=True)
        importer=pdfium.PdfDocument.import_pages
        with patch.object(pdfium.PdfDocument,'import_pages',
                          lambda target,source,pages:importer(target,source,pages[:1])):
            with self.assertRaisesRegex(probe.ProbeError,'pdfium_import_page_count_mismatch'):
                probe._pdfium_rewrite(raw)

    def test_pdfium_save_bound_fails_after_callback_without_retaining_overflow(self):
        with patch.object(probe,'MAX_PDFIUM_REWRITE_BYTES',100):
            with self.assertRaisesRegex(probe.ProbeError,'pdfium_rewritten_bytes_bound'):
                probe._pdfium_rewrite(self.fixture.original.read_bytes())

    def test_pdfium_derived_provider_is_reproducible_but_diagnostic_only(self):
        import mineru_figure_sources as figures
        raw=self.fixture.original.read_bytes()
        rewritten,_=probe._pdfium_rewrite(raw)
        (self.fixture.raw/'source.pdf').write_bytes(rewritten)
        (_,content),(_,middle),_=figures._metadata_files(self.fixture.raw)
        metadata=figures._normalise(content,middle)
        with fitz.open(stream=raw,filetype='pdf') as original, fitz.open(stream=rewritten,filetype='pdf') as supplied:
            result=probe.pdfium_rewrite_diagnostics(raw,original,supplied,0,metadata,figures._decisions(metadata,100))
        self.assertEqual(result['status'],'checked')
        self.assertTrue(result['rewritten_vs_embedded']['rgb_equal'])
        self.assertTrue(result['original_page_count_equal']); self.assertTrue(result['embedded_page_count_equal'])
        self.assertEqual(len(result['rewritten_pdf_sha256']),64)
        self.assertTrue(result['diagnostic_only']); self.assertFalse(result['production_acceptance'])
        self.assertNotIn('Verified source page',json.dumps(result))
        self.assertNotIn('Figure 1',json.dumps(result))

    def test_pdfium_rewrite_does_not_explain_modified_provider_body(self):
        self.change_embedded(lambda doc:doc[0].insert_text((50,150),'CHANGED SECRET',fontsize=10))
        result=self.compare(); derived=result['pages'][0]['pdfium_rewrite']
        self.assertEqual(derived['status'],'checked')
        self.assertTrue(derived['original_vs_rewritten']['rgb_equal'])
        self.assertFalse(derived['rewritten_vs_embedded']['rgb_equal'])
        self.assertGreater(derived['rewritten_vs_embedded']['selected_visual_differences'][0]['body_diff_pixel_count'],0)
        self.assertEqual(result['status'],'mismatch'); self.assertFalse(result['all_selected_pages_equal'])
        self.assertFalse(derived['production_acceptance'])
        self.assertNotIn('CHANGED',json.dumps(derived))

    def test_actual_pdfium_oc_loss_has_graph_bound_all_selected_page_restoration(self):
        from test_mineru_pdf_oc import optional_content_fixture
        self.fixture=Fixture(self.root/'oc-pdfium',pages=2,visuals=[
            visual(0,[35,100,185,260],kind='chart',page_idx=0),
            visual(1,[35,100,185,260],kind='chart',page_idx=1)])
        original,_=optional_content_fixture(pages=2,plain_first=True)
        embedded,_=probe._pdfium_rewrite(original)
        self.fixture.original.write_bytes(original);(self.fixture.raw/'source.pdf').write_bytes(embedded)
        result=self.compare()
        self.assertEqual(result['status'],'mismatch')
        restored=result['pages'][-1]['optional_content_restoration']
        self.assertEqual(restored['status'],'verified')
        self.assertEqual(restored['checked_page_count'],2)
        self.assertTrue(restored['all_selected_pages_equal'])
        self.assertEqual(restored['restoration_proof']['verified_page_indices'],[0,1])
        self.assertEqual(restored['restoration_proof']['embedded_pdf_sha256'],digest(embedded))
        self.assertFalse(restored['production_acceptance']);self.assertFalse(restored['complete_source_handoff'])
        self.assertNotIn('fixture-hidden',json.dumps(restored))

    def test_actual_pdfium_output_intent_loss_restores_all_selected_page_pixels(self):
        self.fixture=Fixture(self.root/'icc-pdfium',pages=2,visuals=[
            visual(0,[35,100,185,260],kind='chart',page_idx=0),
            visual(1,[35,100,185,260],kind='chart',page_idx=1)])
        original=output_intent_fixture();embedded,_=probe._pdfium_rewrite(original)
        self.fixture.original.write_bytes(original);(self.fixture.raw/'source.pdf').write_bytes(embedded)
        result=self.compare();page=result['pages'][0]
        self.assertEqual(result['status'],'mismatch');self.assertFalse(result['all_selected_pages_equal'])
        self.assertTrue(page['pdfium_rewrite']['rewritten_vs_embedded']['rgb_equal'])
        restored=page['output_intent_restoration']
        self.assertEqual(restored['status'],'verified',restored)
        self.assertEqual(restored['checked_page_count'],2);self.assertTrue(restored['all_selected_pages_equal'])
        self.assertEqual([row['comparison']['diff_pixel_count'] for row in restored['pages']],[0,0])
        self.assertEqual(restored['graph_binding']['pages'],2)
        self.assertEqual(restored['original_pdf_sha256'],digest(original))
        self.assertEqual(restored['embedded_pdf_sha256'],digest(embedded))
        self.assertFalse(restored['production_acceptance']);self.assertFalse(restored['complete_source_handoff'])
        self.assertEqual(self.fixture.original.read_bytes(),original)
        self.assertEqual((self.fixture.raw/'source.pdf').read_bytes(),embedded)
        for private in ('SYNTHETIC_PRIVATE_PROFILE','Synthetic color-managed','DestOutputProfile'):
            self.assertNotIn(private,json.dumps(restored))

    def test_output_intent_probe_rejects_changed_provider_content(self):
        self.fixture=Fixture(self.root/'icc-edited')
        original=output_intent_fixture(pages=1);embedded,_=probe._pdfium_rewrite(original)
        self.fixture.original.write_bytes(original);(self.fixture.raw/'source.pdf').write_bytes(embedded)
        self.change_embedded(lambda doc:doc[0].insert_text((50,150),'CHANGED PRIVATE',fontsize=10))
        result=self.compare()['pages'][0]['output_intent_restoration']
        self.assertEqual(result['status'],'mismatch');self.assertFalse(result['all_selected_pages_equal'])
        self.assertEqual(result['graph_binding_status'],'rejected')
        self.assertFalse(result['production_acceptance']);self.assertNotIn('CHANGED PRIVATE',json.dumps(result))

    def test_output_intent_probe_never_overwrites_existing_provider_configuration(self):
        self.change_embedded(lambda doc:doc[0].insert_text((50,150),'CHANGED PRIVATE',fontsize=10))
        result=self.compare()['pages'][0]['output_intent_restoration']
        self.assertEqual(result['status'],'not_applicable')
        original=output_intent_fixture(pages=1)
        self.fixture.original.write_bytes(original);(self.fixture.raw/'source.pdf').write_bytes(original)
        self.change_embedded(lambda doc:doc[0].insert_text((50,150),'CHANGED PRIVATE',fontsize=10))
        result=self.compare()['pages'][0]['output_intent_restoration']
        self.assertEqual(result['status'],'not_applicable');self.assertFalse(result['all_selected_pages_equal'])

    def test_output_intent_equal_pixels_do_not_hide_independent_graph_rejection(self):
        self.fixture=Fixture(self.root/'icc-graph')
        original=output_intent_fixture(pages=1);embedded,_=probe._pdfium_rewrite(original)
        self.fixture.original.write_bytes(original);(self.fixture.raw/'source.pdf').write_bytes(embedded)
        def change_resources(document):
            kind,value=document.xref_get_key(document[0].xref,'Resources')
            self.assertEqual(kind,'xref')
            document.xref_set_key(int(value.split()[0]),'PRIVATE_RESOURCE','(NEVER_PUBLIC)')
        self.change_embedded(change_resources)
        result=self.compare()['pages'][0]['output_intent_restoration']
        self.assertEqual(result['status'],'pixels_verified_graph_rejected')
        self.assertTrue(result['all_selected_pages_equal'])
        self.assertEqual(result['graph_binding_status'],'rejected')
        self.assertFalse(result['production_acceptance'])
        for private in ('PRIVATE_RESOURCE','NEVER_PUBLIC'):
            self.assertNotIn(private,json.dumps(result))

    def test_oc_restoration_probe_rejects_provider_hidden_changes_and_ref_swaps(self):
        from test_mineru_pdf_oc import optional_content_fixture,changed_provider
        original,_=optional_content_fixture()
        embedded,_=probe._pdfium_rewrite(original)
        self.fixture.original.write_bytes(original)
        for change in ('image','text','swap','extra'):
            with self.subTest(change=change):
                (self.fixture.raw/'source.pdf').write_bytes(changed_provider(embedded,change))
                result=self.compare()
                restored=result['pages'][-1]['optional_content_restoration']
                self.assertEqual(restored['status'],'rejected')
                self.assertFalse(restored['all_selected_pages_equal'])
                self.assertFalse(restored['production_acceptance'])

    def test_graph_failure_details_expose_no_unknown_resource_names_or_values(self):
        from test_mineru_pdf_oc import optional_content_fixture
        original,embedded=optional_content_fixture()
        self.fixture.original.write_bytes(original)
        with fitz.open(stream=embedded,filetype='pdf') as document:
            image=document[0].get_images()[0][0]
            document.xref_set_key(image,'CONFIDENTIAL_PRIVATE_RESOURCE','(PRIVATE_SOURCE_TEXT)')
            embedded=document.tobytes(no_new_id=True)
        (self.fixture.raw/'source.pdf').write_bytes(embedded)
        result=self.compare()['pages'][-1]['optional_content_restoration']
        self.assertEqual(result['status'],'rejected')
        self.assertEqual(result['category'],'pdf_graph_dictionary_keys_mismatch')
        self.assertIsInstance(result['graph_details'],dict)
        self.assertTrue(result['graph_details'])
        encoded_result=json.dumps(result)
        for private in ('CONFIDENTIAL_PRIVATE_RESOURCE','PRIVATE_SOURCE_TEXT','fixture-hidden','Hidden_A'):
            self.assertNotIn(private,encoded_result)
        self.assertEqual(len(result['path_sha256']),64)
        self.assertFalse(result['production_acceptance'])

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


class EncryptedExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from export_market_views_original_page_qa import OPENSSL
        cls.crypto=tempfile.TemporaryDirectory();cls.addClassCleanup(cls.crypto.cleanup)
        cls.key=Path(cls.crypto.name)/'key.pem';cls.cert=Path(cls.crypto.name)/'cert.pem'
        created=subprocess.run([OPENSSL,'req','-x509','-newkey','rsa:3072','-nodes','-days','1',
            '-subj','/CN=offline-mineru-binding','-keyout',str(cls.key),'-out',str(cls.cert)],
            capture_output=True,timeout=120,check=False)
        if created.returncode:raise AssertionError('System OpenSSL fixture creation required')
        cls.key.chmod(0o600);cls.cert.chmod(0o600);cls.pem=cls.cert.read_text()
    def setUp(self):
        self.fixture=ProbeTests();self.fixture.setUp();self.addCleanup(self.fixture.doCleanups)
        self.input,self.ledger,self.cache,self.binding=self.fixture.prepared()
        self.output=self.fixture.root/probe.ENCRYPTED_EXPORT_NAME
    def test_invalid_certificate_fails_before_original_ledger_provider_or_cache_reads(self):
        for pem in ('https://PRIVATE.invalid/cert',self.key.read_text(),self.pem+self.pem,'invalid'):
            with self.subTest(length=len(pem)),patch.object(self.cache,'get',side_effect=AssertionError('No cache read')),\
                    patch.object(self.ledger.store,'get',side_effect=AssertionError('No ledger read')),\
                    patch.object(probe,'frozen_inputs',side_effect=AssertionError('No original read')):
                with self.assertRaises(ValueError):
                    probe.probe(self.ledger,self.cache,self.input,1,'261009',1,
                                recipient_cert_pem=pem,encrypted_output=self.output)
        self.assertEqual(self.ledger.provider.gets,0);self.assertFalse(self.output.exists())
    def test_real_cms_export_contains_exact_original_cache_zip_and_private_binding_only(self):
        from export_market_views_original_page_qa import OPENSSL
        before=copy.deepcopy(self.cache.client.objects)
        with patch.object(self.cache,'put',side_effect=AssertionError('No cache write')),\
                patch.object(self.ledger.store,'put',side_effect=AssertionError('No ledger write')):
            result=probe.probe(self.ledger,self.cache,self.input,1,'261009',1,
                recipient_cert_pem=self.pem,encrypted_output=self.output,
                export_context={'source_run_id':'123','source_execution_sha':'a'*40,'probe_execution_sha':'b'*40})
        ciphertext=self.output.read_bytes()
        decrypted=subprocess.run([OPENSSL,'cms','-decrypt','-binary','-inform','DER',
            '-recip',str(self.cert),'-inkey',str(self.key)],input=ciphertext,capture_output=True,timeout=120,check=False)
        self.assertEqual(decrypted.returncode,0)
        summary=result['encrypted_export']
        self.assertEqual(summary['ciphertext_sha256'],digest(ciphertext))
        self.assertEqual(summary['plaintext_payload_sha256'],digest(decrypted.stdout))
        self.assertEqual(self.output.stat().st_mode&0o777,0o600)
        self.assertEqual(result['provider_gets'],1);self.assertEqual(before,self.cache.client.objects)
        with zipfile.ZipFile(io.BytesIO(decrypted.stdout)) as archive:
            self.assertEqual(set(archive.namelist()),{'original.pdf','result.zip','binding-manifest.json'})
            original=archive.read('original.pdf');payload=archive.read('result.zip')
            manifest=json.loads(archive.read('binding-manifest.json'))
            self.assertEqual(original,(self.input/'selected.pdf').read_bytes())
            self.assertEqual(digest(payload),result['comparison']['result_zip_sha256'])
            self.assertEqual(manifest['source_binding'],self.binding)
            self.assertEqual(manifest['files']['original.pdf'],{'sha256':digest(original),'bytes':len(original)})
            self.assertEqual(manifest['source_context']['source_run_id'],'123')
        for private in ('PRIVATE','selected.pdf','SECRET_TOKEN','Verified source page','https://'):
            self.assertNotIn(private,json.dumps(result))
        self.assertFalse(summary['production_acceptance'])
    def test_plaintext_and_zip_size_bound_precedes_encryption_and_output(self):
        with patch.object(probe,'MAX_EXPORT_BYTES',100),\
                patch('export_market_views_original_page_qa.encrypt_payload',side_effect=AssertionError('No oversized encryption')):
            with self.assertRaisesRegex(probe.ProbeError,'encrypted_export_size_bound'):
                probe.probe(self.ledger,self.cache,self.input,1,'261009',1,
                    recipient_cert_pem=self.pem,encrypted_output=self.output)
        self.assertFalse(self.output.exists())
    def test_omitted_recipient_produces_no_encrypted_artifact(self):
        result=probe.probe(self.ledger,self.cache,self.input,1,'261009',1)
        self.assertNotIn('encrypted_export',result);self.assertFalse(self.output.exists())


if __name__=='__main__': unittest.main(verbosity=2)
