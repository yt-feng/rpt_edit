"""Self-created color-profile PDFs; no private content or production inputs."""
import copy
import io
import json
from pathlib import Path
import struct
import subprocess
import sys
import unittest
from unittest.mock import patch

import fitz
import mineru_pdf_output_intents as color
from mineru_pdf_graph import PdfGraphError


def output_intent_fixture(*,pages=2,plain_first=False):
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
        for index in range(pages):
            page=document.new_page(width=400,height=500)
            page.insert_text((20,30),'Synthetic color-managed source',fontsize=12)
            if not plain_first or index != 0:
                page.draw_rect(fitz.Rect(35,100,185,260),fill=(.3,.5,.7))
        xref=document.get_new_xref();document.update_object(xref,'<</N 3>>')
        document.update_stream(xref,bytes(profile),compress=True)
        document.xref_set_key(document.pdf_catalog(),'OutputIntents',
            f'[<</Type/OutputIntent/S/GTS_PDFX/DestOutputProfile {xref} 0 R'
            '/OutputConditionIdentifier(SYNTHETIC_PRIVATE_PROFILE)>>]')
        return document.tobytes(no_new_id=True)



def pdfium_copy(raw):
    import pypdfium2 as pdfium
    source=pdfium.PdfDocument(raw);target=pdfium.PdfDocument.new()
    try:
        target.import_pages(source,list(range(len(source))))
        output=io.BytesIO();target.save(output);return output.getvalue()
    finally:target.close();source.close()


def changed(raw,operation):
    with fitz.open(stream=raw,filetype='pdf') as document:
        operation(document)
        return document.tobytes(no_new_id=True)


def restore(original,embedded):
    return color.restore_missing_output_intents(original,embedded,
        original_sha256=color.digest(original),embedded_sha256=color.digest(embedded))


class OutputIntentTests(unittest.TestCase):
    def test_actual_pdfium_loss_is_restored_without_changing_any_input_bytes(self):
        from mineru_figure_sources import _render
        original=output_intent_fixture();embedded=pdfium_copy(original)
        raw_pair=(original,embedded)
        restored,proof=restore(original,embedded)
        try:
            with fitz.open(stream=original,filetype='pdf') as authentic,fitz.open(stream=embedded,filetype='pdf') as provider:
                self.assertTrue(color.has_missing_output_intents(authentic,provider))
                for index in range(2):
                    source_image,provider_image,restored_image=(_render(doc[index]) for doc in (authentic,provider,restored))
                    try:
                        self.assertNotEqual(source_image.tobytes(),provider_image.tobytes())
                        self.assertEqual(source_image.size,restored_image.size)
                        self.assertEqual(source_image.tobytes(),restored_image.tobytes())
                    finally:source_image.close();provider_image.close();restored_image.close()
                self.assertTrue(color.has_missing_output_intents(authentic,provider))
            self.assertEqual((original,embedded),raw_pair)
            self.assertEqual(proof['graph_binding']['pages'],2)
            self.assertEqual(proof['policy'],color.POLICY)
            proof['verified_page_indices']=[0,1]
            color.validate_restoration_receipt(proof,original_sha256=color.digest(original),
                embedded_sha256=color.digest(embedded),page_indices=[0,1])
            for private in ('Synthetic','PRIVATE_PROFILE','DestOutputProfile'):
                self.assertNotIn(private,json.dumps(proof))
        finally:restored.close()

    def test_changed_text_drawing_and_nonrendering_resources_remain_rejected(self):
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        def private_resource(document):
            kind,value=document.xref_get_key(document[0].xref,'Resources')
            self.assertEqual(kind,'xref')
            document.xref_set_key(int(value.split()[0]),'PRIVATE_RESOURCE','(PRIVATE_VALUE)')
        for operation in [lambda doc:doc[0].insert_text((30,80),'ALTERED',fontsize=9),
                          lambda doc:doc[0].draw_rect((40,100,180,150),fill=(1,0,0)),private_resource]:
            with self.subTest(operation=operation),self.assertRaises(PdfGraphError):
                restore(original,changed(embedded,operation))

    def test_existing_empty_or_nonempty_provider_catalog_is_not_replaced(self):
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        for provider in (original,changed(embedded,lambda doc:doc.xref_set_key(doc.pdf_catalog(),'OutputIntents','[]'))):
            with self.subTest(provider_hash=color.digest(provider)),self.assertRaisesRegex(color.OutputIntentError,'output_intent_missing_required'):
                restore(original,provider)
        with self.assertRaisesRegex(color.OutputIntentError,'output_intent_missing_required'):
            restore(embedded,embedded)

    def test_combined_optional_content_configuration_is_not_silently_repaired(self):
        original=changed(output_intent_fixture(pages=1),lambda doc:doc.add_ocg('HIDDEN_PRIVATE',on=False))
        embedded=pdfium_copy(original)
        with self.assertRaisesRegex(color.OutputIntentError,'output_intent_optional_content_unsupported'):
            restore(original,embedded)

    def test_original_and_embedded_hashes_are_verified_before_copy(self):
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        for original_hash,embedded_hash in [('0'*64,color.digest(embedded)),(color.digest(original),'0'*64)]:
            with self.subTest(original_hash=original_hash),patch.object(color,'copy_output_intents',side_effect=AssertionError('copy forbidden')):
                with self.assertRaisesRegex(color.OutputIntentError,'output_intent_source_binding'):
                    color.restore_missing_output_intents(original,embedded,original_sha256=original_hash,embedded_sha256=embedded_hash)

    def test_malformed_profile_and_unrecognized_catalog_keys_are_rejected(self):
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        def invalid_profile(document):
            profile=next(x for x in range(1,document.xref_length()) if document.xref_is_stream(x)
                         and document.xref_get_key(x,'N')==('int','3'))
            document.update_stream(profile,b'not an ICC profile')
        invalid=changed(original,invalid_profile)
        with self.assertRaisesRegex(color.OutputIntentError,'output_intent_profile_bound'):
            restore(invalid,embedded)
        unknown=changed(original,lambda doc:doc.xref_set_key(doc.pdf_catalog(),'OutputIntents',
            '[<</Type/OutputIntent/S/GTS_PDFX/PRIVATE_KEY(PRIVATE_VALUE)>>]'))
        with self.assertRaisesRegex(color.OutputIntentError,'output_intent_keys'):
            restore(unknown,embedded)

    def test_input_size_and_budget_stop_before_acceptance(self):
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        with patch.object(color,'MAX_PDF_BYTES',10),self.assertRaisesRegex(color.OutputIntentError,'output_intent_input_bound'):
            restore(original,embedded)
        def stop():raise TimeoutError('test deadline')
        with self.assertRaises(TimeoutError):
            color.restore_missing_output_intents(original,embedded,original_sha256=color.digest(original),
                embedded_sha256=color.digest(embedded),budget=stop)

    def test_receipt_binding_pages_and_types_are_strict(self):
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        restored,proof=restore(original,embedded);restored.close();proof['verified_page_indices']=[0]
        for key,value in [('schema',True),('policy','unknown'),('embedded_pdf_sha256','0'*64),
                          ('verified_page_indices',[]),('verified_page_indices',[False]),('profile_sha256',[]),
                          ('restored_pdf_bytes',True),('provider_catalog_was_missing',False)]:
            candidate=copy.deepcopy(proof);candidate[key]=value
            with self.subTest(key=key),self.assertRaises(color.OutputIntentError):
                color.validate_restoration_receipt(candidate,original_sha256=color.digest(original),
                    embedded_sha256=color.digest(embedded),page_indices=[0])

    def test_lightweight_receipt_import_does_not_load_pdf_engines(self):
        result=subprocess.run([sys.executable,'-c',
            "import mineru_pdf_output_intents,sys; assert 'fitz' not in sys.modules and 'pypdf' not in sys.modules"],
            capture_output=True,text=True,cwd=Path(__file__).resolve().parent)
        self.assertEqual(result.returncode,0,result.stderr)


if __name__=='__main__':unittest.main(verbosity=2)
