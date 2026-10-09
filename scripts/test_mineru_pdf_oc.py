"""Self-created optional-content PDFs; hidden edits cannot be repaired away."""
import io
import json
import unittest

import fitz
from PIL import Image

import mineru_pdf_oc as oc


def optional_content_fixture(*,pages=1,size=(400,500),plain_first=False):
    with fitz.open() as document:
        first=document.add_ocg('fixture-hidden-A',on=False)
        second=document.add_ocg('fixture-hidden-B',on=False)
        for index in range(pages):
            page=document.new_page(width=size[0],height=size[1])
            page.insert_text((20,30),'Synthetic original page',fontsize=12)
            page.draw_rect(fitz.Rect(35,100,185,260),fill=(.8,.9,1))
            if plain_first and index==0: continue
            for group,y,color,word in [(first,140,(240,30,20),'Hidden_A'),(second,200,(20,40,230),'Hidden_B')]:
                page.insert_text((45,y),word,fontsize=12,oc=group)
                image=io.BytesIO();Image.new('RGB',(8,8),color).save(image,'PNG')
                page.insert_image(fitz.Rect(50,y+2,100,y+40),stream=image.getvalue(),oc=group)
        original=document.tobytes(no_new_id=True)
        document.xref_set_key(document.pdf_catalog(),'OCProperties','null')
        embedded=document.tobytes(no_new_id=True)
    return original,embedded


def changed_provider(raw,kind):
    with fitz.open(stream=raw,filetype='pdf') as document:
        page=document[0]
        if kind=='image':
            document.update_stream(page.get_images()[0][0],bytes([0,255,0])*64)
        elif kind=='text':
            for xref in page.get_contents():
                data=document.xref_stream(xref)
                revised=data.replace(b'48696464656e5f41',b'48696464656e5f5a')
                if data!=revised:
                    document.update_stream(xref,revised);break
            else: raise AssertionError('Fixture text missing')
        elif kind=='swap':
            left,right=[row[0] for row in page.get_images()[:2]]
            a,b=document.xref_get_key(left,'OC')[1],document.xref_get_key(right,'OC')[1]
            document.xref_set_key(left,'OC',b);document.xref_set_key(right,'OC',a)
        elif kind=='extra':
            xref=document.get_new_xref();document.update_object(xref,'<</Type/OCG/Name(extra-hidden)>>')
        elif kind=='existing':
            document.xref_set_key(document.pdf_catalog(),'OCProperties','<</OCGs[]/D<</BaseState/ON>>>>')
        else: raise AssertionError(kind)
        return document.tobytes(no_new_id=True)


def render(document,index=0):
    pix=document[index].get_pixmap(matrix=fitz.Matrix(300/72,300/72),colorspace=fitz.csRGB,alpha=False)
    return pix.width,pix.height,oc.digest(pix.samples)


class OptionalContentTests(unittest.TestCase):
    def test_restoration_changes_only_catalog_and_preserves_exact_original_pixels(self):
        original,embedded=optional_content_fixture(pages=2)
        with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=embedded,filetype='pdf') as e:
            self.assertNotEqual(render(a),render(e))
            before=oc._provider_inventory(e,lambda:None)
            restored,receipt=oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))
            try:
                self.assertEqual(oc._provider_inventory(restored,lambda:None),before)
                self.assertEqual(oc._provider_inventory(e,lambda:None),before)
                self.assertEqual(e.xref_get_key(e.pdf_catalog(),'OCProperties')[0],'null')
                for index in range(2): self.assertEqual(render(a,index),render(restored,index))
                receipt['verified_page_indices']=[0,1]
                oc.validate_restoration_receipt(receipt,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded),page_indices=[0,1])
            finally: restored.close()
        for private in ('fixture-hidden','Hidden_A','Synthetic original','/OCGs','/Type'):
            self.assertNotIn(private,json.dumps(receipt))

    def test_hidden_provider_edits_or_extra_groups_never_become_repair_authority(self):
        original,embedded=optional_content_fixture()
        for kind in ('image','text','swap','extra','existing'):
            with self.subTest(kind=kind):
                bad=changed_provider(embedded,kind)
                with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=bad,filetype='pdf') as e:
                    with self.assertRaises(ValueError):
                        oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(bad))

    def test_cyclic_original_configuration_is_rejected(self):
        original,embedded=optional_content_fixture()
        with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=embedded,filetype='pdf') as e:
            cycle=a.get_new_xref();a.update_object(cycle,'['+str(cycle)+' 0 R]')
            a.xref_set_key(a.pdf_catalog(),'OCProperties/D/Order',str(cycle)+' 0 R')
            with self.assertRaisesRegex(oc.OptionalContentError,'oc_configuration_cycle'):
                oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))

    def test_ocmd_not_and_off_policies_are_bound_without_all_on_substitution(self):
        for policy in ('Not','AnyOff','AllOff'):
            with self.subTest(policy=policy),fitz.open() as source:
                page=source.new_page(width=200,height=200)
                first=source.add_ocg('membership-one',on=False)
                if policy=='Not': membership=source.set_ocmd(ve=['not',first])
                else:
                    second=source.add_ocg('membership-two',on=False)
                    membership=source.set_ocmd(ocgs=[first,second],policy=policy)
                page.insert_text((20,50),'Controlled membership text',oc=membership)
                original=source.tobytes(no_new_id=True)
                source.xref_set_key(source.pdf_catalog(),'OCProperties','null')
                embedded=source.tobytes(no_new_id=True)
            with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=embedded,filetype='pdf') as e:
                restored,_=oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))
                try:self.assertEqual(render(a),render(restored))
                finally:restored.close()
                membership=next(xref for xref in range(1,e.xref_length()) if e.xref_get_key(xref,'Type')==('name','/OCMD'))
                e.xref_set_key(membership,'P','/AnyOn')
                with self.assertRaises(ValueError):
                    oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))

    def test_nonzero_configuration_reference_generation_is_rejected(self):
        original,embedded=optional_content_fixture()
        with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=embedded,filetype='pdf') as e:
            config=a.get_new_xref();a.update_object(config,'<</BaseState/ON>>')
            a.xref_set_key(a.pdf_catalog(),'OCProperties/D',str(config)+' 7 R')
            with self.assertRaisesRegex(oc.OptionalContentError,'oc_configuration_reference_invalid'):
                oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))

    def test_non_ascii_configuration_names_are_safely_serialized(self):
        original,embedded=optional_content_fixture()
        with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=embedded,filetype='pdf') as e:
            a.xref_set_key(a.pdf_catalog(),'OCProperties/D/Name',fitz.get_pdf_str('中文图层设置'))
            restored,receipt=oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))
            try:
                self.assertEqual(restored.xref_get_key(restored.pdf_catalog(),'OCProperties/D/Name')[1],'中文图层设置')
                self.assertEqual(render(a),render(restored))
                self.assertNotIn('中文',json.dumps(receipt,ensure_ascii=False))
            finally:restored.close()

    def test_bound_context_must_not_be_accepted_as_raw_provider_equivalence(self):
        original,embedded=optional_content_fixture()
        with fitz.open(stream=original,filetype='pdf') as a,fitz.open(stream=embedded,filetype='pdf') as e:
            restored,receipt=oc.restore_missing_optional_content(a,e,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded))
            restored.close()
        self.assertEqual(receipt['embedded_pdf_sha256'],oc.digest(embedded))
        self.assertNotEqual(receipt['restored_pdf_sha256'],receipt['embedded_pdf_sha256'])
        self.assertEqual(receipt['verified_page_indices'],[])
        with self.assertRaises(oc.OptionalContentError):
            oc.validate_restoration_receipt(receipt,original_sha256=oc.digest(original),embedded_sha256=oc.digest(embedded),page_indices=[0])


if __name__=='__main__': unittest.main(verbosity=2)
