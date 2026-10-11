#!/usr/bin/env python3
"""Read one exact cached result and diagnose original/provider figure gates.

This probe never downloads provider ZIP URLs, submits jobs, writes caches, or
creates a source handoff. Its public output contains only counts and hashes.
"""
from __future__ import annotations
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import tempfile
import time

from mineru_task_ledger import DONE, Ledger, LedgerError, digest, encoded, exact_json
from mineru_completed_child_reuse import read_completed_batch
from mineru_result_cache import identity as cache_identity
from recover_durable_mineru_sources import (MANIFEST, OPTIONS, check_producer, exact_date,
                                          frozen_inputs, original_groups)

WORKFLOW = '.github/workflows/mineru-figure-binding-probe.yml'
MAX_PROVIDER_GETS = 4
MAX_PROBE_SECONDS = 480
MAX_VISUALS = 100
MAX_OBJECTS_PER_PAGE = 10000


class ProbeError(ValueError):
    pass


def require(value, category):
    if not value:
        raise ProbeError(category)


def validate_request(metadata, source_run_id, date_folder, expected_articles, source_ordinal, repository):
    require(isinstance(source_run_id,str) and re.fullmatch(r'[1-9][0-9]{0,19}',source_run_id), 'source_run_id_invalid')
    exact_date(date_folder)
    require(type(expected_articles) is int and 1 <= expected_articles <= 1000, 'expected_count_invalid')
    require(type(source_ordinal) is int and 1 <= source_ordinal <= expected_articles, 'source_ordinal_invalid')
    sha = check_producer(metadata,source_run_id,repository)
    require(metadata.get('status') == 'completed', 'producer_not_completed')
    return sha


class ReadOnlyStore:
    def __init__(self,store):
        self.store,self.snapshots = store,{}
    def get(self,key):
        value,version = self.store.get(key)
        raw = encoded(value)
        require(key not in self.snapshots or self.snapshots[key] == raw,'stored_snapshot_changed')
        self.snapshots[key] = raw
        return value,version
    def put(self,*_args,**_kwargs):
        raise ProbeError('canonical_write_forbidden')
    def verify(self):
        for key in list(self.snapshots): self.get(key)


class ReadOnlyProvider:
    def __init__(self,provider,clock=time.monotonic,deadline=None):
        self.provider,self.clock,self.deadline = provider,clock,deadline
        self.gets = 0
    def poll(self,batch_id,token,timeout):
        require(self.gets < MAX_PROVIDER_GETS,'provider_get_bound')
        remaining = MAX_PROBE_SECONDS if self.deadline is None else self.deadline-self.clock()
        require(remaining > 0,'probe_deadline')
        self.gets += 1
        return self.provider.poll(batch_id,token,min(timeout,remaining,60))
    def submit(self,*_args,**_kwargs): raise ProbeError('provider_post_forbidden')
    def upload(self,*_args,**_kwargs): raise ProbeError('provider_upload_forbidden')


class ReadOnlyR2Client:
    def __init__(self,client): self.client = client
    def get_object(self,**kwargs): return self.client.get_object(**kwargs)
    def put_object(self,**_kwargs): raise ProbeError('private_write_forbidden')


def _page_objects(page):
    annotations = list(itertools.islice(page.annots() or (),MAX_OBJECTS_PER_PAGE+1))
    widgets = list(itertools.islice(page.widgets() or (),MAX_OBJECTS_PER_PAGE+1))
    images = page.get_images(full=True)
    require(max(len(annotations),len(widgets),len(images)) <= MAX_OBJECTS_PER_PAGE,'page_objects_bound')
    return {'image_count':len(images),'annotation_count':len(annotations),'widget_count':len(widgets),
            'annotation_types':dict(sorted(Counter(str(item.type[0]) for item in annotations).items())),
            'widget_types':dict(sorted(Counter(str(item.field_type) for item in widgets).items()))}


def _difference(left,right):
    from PIL import ImageChops
    if left.size != right.size:
        return {'same_size':False,'original_pixels':list(left.size),'embedded_pixels':list(right.size),
                'original_rgb_sha256':digest(left.tobytes()),'embedded_rgb_sha256':digest(right.tobytes())}
    difference = ImageChops.difference(left,right)
    channels = difference.split()
    maximum = ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2])
    histogram = maximum.histogram()
    changed = left.width*left.height-histogram[0]
    result = {'same_size':True,'pixel_size':list(left.size),'diff_bbox':list(maximum.getbbox()) if changed else None,
        'diff_pixel_count':changed,'diff_pixel_ratio':changed/(left.width*left.height),
        'max_channel_delta':max(index for index,value in enumerate(histogram) if value),
        'original_rgb_sha256':digest(left.tobytes()),'embedded_rgb_sha256':digest(right.tobytes())}
    difference.close(); maximum.close()
    for channel in channels: channel.close()
    return result


MAX_SEMANTIC_BYTES = 64 * 1024 * 1024
MAX_GLYPHS = 200000
MAX_IMAGE_PLACEMENTS = 1000
MAX_FONTS = 256
MAX_PDFIUM_REWRITE_BYTES = 512 * 1024 * 1024


def _semantic_canonical(value):
    """Canonicalize internal PDF data for hashing; never return its raw text."""
    if value is None or type(value) in {bool,int,str}:
        return value
    if type(value) is float:
        require(math.isfinite(value),'semantic_nonfinite_number')
        return value
    if isinstance(value,bytes):
        return {'bytes':len(value),'sha256':digest(value)}
    if isinstance(value,dict):
        require(all(isinstance(key,str) for key in value),'semantic_mapping_key')
        return {key:_semantic_canonical(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)) or type(value).__name__ in {'Rect','IRect','Point','Quad','Matrix'}:
        return [_semantic_canonical(item) for item in value]
    raise ProbeError('semantic_value_type')


def _semantic_hash(value):
    raw=encoded(_semantic_canonical(value))
    require(len(raw)<=MAX_SEMANTIC_BYTES,'semantic_bytes_bound')
    return digest(raw)


def _text_semantics(page):
    import fitz
    raw=page.get_text('rawdict',flags=fitz.TEXTFLAGS_RAWDICT & ~fitz.TEXT_PRESERVE_IMAGES)
    blocks,lines,spans,glyphs,geometry,characters=0,0,[],[],[],[]
    for block in raw['blocks']:
        if block.get('type')!=0: continue
        blocks+=1
        for line in block['lines']:
            lines+=1
            for span in line['spans']:
                span_index=len(spans)
                chars=span.get('chars',[])
                require(len(glyphs)+len(chars)<=MAX_GLYPHS,'glyph_count_bound')
                spans.append({'line':lines-1,'line_dir':line.get('dir'),'wmode':line.get('wmode'),
                    **{key:span.get(key) for key in ('size','flags','font','color','alpha','ascender','descender','origin','bbox')}})
                for char in chars:
                    entry={'span':span_index,**{key:char.get(key) for key in ('c','origin','bbox','synthetic')}}
                    glyphs.append(entry)
                    characters.append(char.get('c'))
                    geometry.append({key:item for key,item in entry.items() if key!='c'})
    trace=page.get_texttrace()
    require(len(trace)<=MAX_OBJECTS_PER_PAGE,'text_trace_count_bound')
    trace_chars=[]
    for span in trace:
        chars=span.get('chars',[])
        require(len(trace_chars)+len(chars)<=MAX_GLYPHS,'text_trace_glyph_count_bound')
        trace_chars.extend(chars)
    rawdict_sha=_semantic_hash({'spans':spans,'glyphs':glyphs})
    trace_sha=_semantic_hash(trace)
    return {'status':'checked','block_count':blocks,'line_count':lines,'span_count':len(spans),
        'glyph_count':len(glyphs),'sha256':_semantic_hash([rawdict_sha,trace_sha]),
        'rawdict_sha256':rawdict_sha,'texttrace_sha256':trace_sha,
        'glyph_ids_sha256':_semantic_hash([char[1] for char in trace_chars]),
        'unicode_sha256':_semantic_hash([char[0] for char in trace_chars]),
        'characters_sha256':_semantic_hash(characters),'glyph_geometry_sha256':_semantic_hash(geometry),
        'span_style_sha256':_semantic_hash(spans)}


def _drawings_semantics(page):
    rows=page.get_drawings(extended=True)
    require(len(rows)<=MAX_OBJECTS_PER_PAGE,'drawing_count_bound')
    item_count=sum(len(row.get('items',[])) for row in rows)
    require(item_count<=MAX_GLYPHS,'drawing_item_count_bound')
    return {'status':'checked','path_count':len(rows),'item_count':item_count,'sha256':_semantic_hash(rows)}


def _font_semantics(page):
    fonts=page.get_fonts(full=True)
    require(len(fonts)<=MAX_FONTS,'font_count_bound')
    rows,total=[],0
    for value in fonts:
        xref=value[0]
        basename,extension,kind,program=page.parent.extract_font(xref)
        total+=len(program)
        require(total<=MAX_SEMANTIC_BYTES,'font_program_bytes_bound')
        rows.append({'embedded':bool(program),'program_bytes':len(program),'program_sha256':digest(program),
            'font_type_sha256':_semantic_hash(kind),'encoding_sha256':_semantic_hash(value[5]),
            'font_identity_sha256':_semantic_hash([basename,extension,kind])})
    rows.sort(key=lambda row:encoded(row))
    return {'status':'checked','resource_count':len(fonts),'embedded_program_bytes':total,
        'sha256':_semantic_hash(rows),'programs':rows}


def _stream_semantics(page):
    refs=page.get_contents()
    require(len(refs)<=MAX_OBJECTS_PER_PAGE,'content_stream_count_bound')
    rows,total=[],0
    combined=hashlib.sha256()
    for ref in refs:
        raw=page.parent.xref_stream(ref)
        require(isinstance(raw,bytes),'content_stream_missing')
        total+=len(raw); require(total<=MAX_SEMANTIC_BYTES,'content_stream_bytes_bound')
        combined.update(raw)
        rows.append({'bytes':len(raw),'sha256':digest(raw)})
    return {'status':'checked','stream_count':len(rows),'decoded_bytes':total,
            'sha256':combined.hexdigest(),'stream_inventory_sha256':_semantic_hash(rows)}


def _bboxlog_semantics(page):
    rows=page.get_bboxlog()
    require(len(rows)<=MAX_GLYPHS,'bboxlog_count_bound')
    return {'status':'checked','entry_count':len(rows),'sha256':_semantic_hash(rows)}


def _pdf_key_fingerprint(document,xref,key):
    """Hash typed metadata with reference numbers removed; no image decoding."""
    kind,value=document.xref_get_key(xref,key)
    references=re.findall(r'(?<![0-9])([0-9]+) [0-9]+ R',value)
    require(len(references)<=MAX_OBJECTS_PER_PAGE,'resource_reference_count_bound')
    def normalized(raw):
        return re.sub(r'(?<![0-9])[0-9]+ [0-9]+ R','<reference>',raw)
    # One-level target dictionary hashes are enough to expose changed known
    # entries without walking shared image resources or disclosing xref IDs.
    targets=[]; total=len(value)
    for reference in references:
        raw=document.xref_object(int(reference),compressed=True)
        total+=len(raw)
        require(total<=MAX_SEMANTIC_BYTES,'resource_metadata_bytes_bound')
        targets.append(_semantic_hash(normalized(raw)))
    return {'type':kind,'present':kind!='null','sha256':_semantic_hash([kind,normalized(value),targets])}


def _render_resource_context(page):
    document=page.parent
    def group(xref,path):
        return {key:_pdf_key_fingerprint(document,xref,path+'/'+key) for key in ('S','I','K','CS')}
    def transparency(xref):
        root=_pdf_key_fingerprint(document,xref,'Resources/ExtGState')
        kind,value=document.xref_get_key(xref,'Resources/ExtGState')
        if kind=='xref':
            value=document.xref_object(int(value.split()[0]),compressed=True)
        refs=re.findall(r'/[^\s/<>()\[\]]+\s+([0-9]+) [0-9]+ R',value)
        require(len(refs)<=256,'extgstate_count_bound')
        entries=[]
        for ref in refs:
            ref=int(ref)
            entries.append({'fields':{key:_pdf_key_fingerprint(document,ref,key) for key in ('ca','CA','BM','SMask')},
                'soft_mask_fields':{key:_pdf_key_fingerprint(document,ref,'SMask/'+key) for key in ('S','BC','TR')},
                'soft_mask_group':group(ref,'SMask/G/Group')})
        entries.sort(key=encoded)
        return {'dictionary':root,'entry_count':len(entries),'entries':entries}
    forms=page.get_xobjects()
    require(len(forms)<=MAX_OBJECTS_PER_PAGE,'form_count_bound')
    form_rows=[{'group':group(row[0],'Group'),'transparency':transparency(row[0]),
                'colorspace':_pdf_key_fingerprint(document,row[0],'Resources/ColorSpace')} for row in forms]
    form_rows.sort(key=encoded)
    catalog=document.pdf_catalog()
    data={'page_group':group(page.xref,'Group'),'page_transparency':transparency(page.xref),
        'page_colorspace':_pdf_key_fingerprint(document,page.xref,'Resources/ColorSpace'),
        'form_count':len(forms),'forms':form_rows,
        'catalog':{key:_pdf_key_fingerprint(document,catalog,key) for key in ('OutputIntents','OCProperties')}}
    return {'status':'checked','sha256':_semantic_hash(data),**data}


def _image_semantics(page):
    import fitz
    import io
    from PIL import Image
    # xrefs=True would hash every resource image, including unrelated pages.
    # Read actual placements without hashes, bound their decoded size first,
    # then obtain only displayed image blocks. No resource image is decoded.
    images=page.get_image_info(hashes=False,xrefs=False)
    require(len(images)<=MAX_IMAGE_PLACEMENTS,'image_placement_count_bound')
    def dimensions(width,height):
        require(type(width) is int and type(height) is int and 1<=width<=20000 and 1<=height<=20000,
                'displayed_image_dimensions_bound')
        # Allow source channels, mask, RGB conversion and copied samples.
        estimate=width*height*16
        require(estimate<=MAX_SEMANTIC_BYTES,'displayed_image_pixels_bound')
        return estimate
    estimate=0
    for item in images:
        estimate+=dimensions(item.get('width'),item.get('height'))
        require(estimate<=MAX_SEMANTIC_BYTES,'displayed_image_decoded_bytes_bound')
    if not images:
        return {'status':'checked','placement_count':0,'sha256':_semantic_hash([]),
            'content_sha256':_semantic_hash([]),'placements_sha256':_semantic_hash([]),'images':[]}
    # Resource dictionaries can be shared with other pages. Inspect only their
    # headers / dictionary hashes; do not claim they were actually displayed.
    resources=page.get_images(full=True)
    require(len(resources)<=MAX_OBJECTS_PER_PAGE,'page_objects_bound')
    resource_rows=[]
    metadata_keys=('ColorSpace','SMask','Matte','Interpolate','Decode','DecodeParms',
                   'Filter','Intent','ImageMask','Mask','BitsPerComponent','SMaskInData')
    for resource in resources:
        xref,mask_ref,width,height=resource[:4]
        row={'width':width,'height':height,'has_soft_mask':bool(mask_ref),
             'dictionary_fields_sha256':{key:_pdf_key_fingerprint(page.parent,xref,key)['sha256'] for key in metadata_keys}}
        if mask_ref:
            width_kind,mask_width=page.parent.xref_get_key(mask_ref,'Width')
            height_kind,mask_height=page.parent.xref_get_key(mask_ref,'Height')
            require(width_kind==height_kind=='int','image_mask_dimensions_missing')
            dimensions(int(mask_width),int(mask_height))
            row['mask_dimensions']=[int(mask_width),int(mask_height)]
            row['mask_dictionary_fields_sha256']={key:_pdf_key_fingerprint(page.parent,mask_ref,key)['sha256'] for key in metadata_keys}
        resource_rows.append(row)
    # Before block extraction, conservatively reserve the largest candidate
    # mask for each displayed placement. Candidate dictionaries are not proof
    # of which resource was drawn; actual mask evidence comes from its block.
    for item in images:
        candidates=[row for row in resource_rows if (row['width'],row['height'])==(item['width'],item['height'])]
        estimate+=max([dimensions(*row['mask_dimensions']) for row in candidates if row['has_soft_mask']] or [0])
        require(estimate<=MAX_SEMANTIC_BYTES,'displayed_image_decoded_bytes_bound')
    blocks=[block for block in page.get_text('dict')['blocks'] if block.get('type')==1]
    require(len(blocks)==len(images),'displayed_image_inventory_mismatch')
    rows,total=[],0
    def decode_metadata(raw,expected=None):
        nonlocal total
        require(isinstance(raw,bytes),'displayed_image_content_missing')
        total+=len(raw)
        require(total<=MAX_SEMANTIC_BYTES,'displayed_image_bytes_bound')
        # Pillow reads extracted PNG/JPEG headers without allocating pixels.
        with Image.open(io.BytesIO(raw)) as header:
            dimensions(*header.size)
            size=header.size
            require(expected is None or size==expected,'displayed_image_header_mismatch')
        pix=fitz.Pixmap(raw)
        try:
            if pix.colorspace is not None and pix.colorspace.n not in (1,3):
                pix=fitz.Pixmap(fitz.csRGB,pix)
            require((pix.width,pix.height)==size and pix.n<=4,'displayed_image_decoded_geometry_mismatch')
            require(total+pix.width*pix.height*pix.n<=MAX_SEMANTIC_BYTES,'displayed_image_bytes_bound')
            pixels=pix.samples
            total+=len(pixels)
            return {'width':pix.width,'height':pix.height,'channels':pix.n,'alpha':bool(pix.alpha),
                'content_bytes':len(raw),'content_sha256':digest(raw),
                'pixel_sha256':digest(encoded([pix.width,pix.height,pix.n,pix.alpha])+pixels)}
        finally: del pix
    for item in images:
        matches=[block for block in blocks if block.get('number')==item.get('number')
                 and exact_json(list(block['bbox']),list(item['bbox']))
                 and block.get('width')==item['width'] and block.get('height')==item['height']]
        require(len(matches)==1,'displayed_image_ambiguous')
        block=matches[0]; expected=(item['width'],item['height'])
        base=decode_metadata(block['image'],expected)
        # Different-size masks are legal PDF objects. Keep independent decoded
        # hashes and geometry; never rescale or compose them in this diagnostic.
        mask=decode_metadata(block['mask']) if block.get('mask') else None
        candidates=sorted([row for row in resource_rows if (row['width'],row['height'])==expected],key=encoded)
        row={'bbox':list(item['bbox']),'transform':list(item['transform']),
            'width':item['width'],'height':item['height'],'bpc':item.get('bpc'),
            'colorspace':item.get('colorspace'),'content_bytes':base['content_bytes'],
            'content_sha256':base['content_sha256'],'pixel_sha256':base['pixel_sha256'],
            'base_image':base,'displayed_block_mask':mask,
            'resource_candidates_are_exact_binding':False,'resource_candidate_count':len(candidates),
            'resource_candidates_sha256':_semantic_hash(candidates),'resource_candidate_metadata':candidates[:8],
            'resource_candidates_truncated':len(candidates)>8}
        rows.append(row)
    content=sorted([{key:row[key] for key in ('content_bytes','content_sha256','pixel_sha256','displayed_block_mask')} for row in rows],key=encoded)
    placements=[{key:row[key] for key in ('bbox','transform','width','height','bpc','colorspace')} for row in rows]
    return {'status':'checked','placement_count':len(rows),'sha256':_semantic_hash(rows),
        'content_sha256':_semantic_hash(content),'placements_sha256':_semantic_hash(placements),'images':rows,
        'resource_inventory_count':len(resource_rows),'resource_inventory_sha256':_semantic_hash(sorted(resource_rows,key=encoded))}


def semantic_diagnostics(original,embedded,budget=lambda:None):
    """Emit only hashes, typed geometry and counts from the first failed page."""
    result={}
    for name,inspect in [('text',_text_semantics),('images',_image_semantics),
                         ('drawings',_drawings_semantics),('fonts',_font_semantics),('content_streams',_stream_semantics),
                         ('display_operations',_bboxlog_semantics),('render_resources',_render_resource_context)]:
        values=[]
        for page in (original,embedded):
            budget()
            try: values.append(inspect(page))
            except Exception as error:
                values.append({'status':'unavailable','category':str(error) if isinstance(error,ProbeError) else type(error).__name__})
        result[name]={'original':values[0],'embedded':values[1],
            'equal':values[0].get('sha256')==values[1].get('sha256') if all(row['status']=='checked' for row in values) else None}
    return result


def selected_visual_differences(left,right,metadata,decisions,page_index,page_size):
    import mineru_figure_sources as figures
    from PIL import ImageChops
    same_size=left.size==right.size
    mask=None
    if same_size:
        difference=ImageChops.difference(left,right)
        channels=difference.split()
        mask=ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2])
        difference.close()
        for channel in channels: channel.close()
    results=[]
    try:
        for record,decision in zip(metadata['records'],decisions):
            if record['page_idx']!=page_index or not decision['selected']: continue
            crop=figures._crop(record,metadata['records'],page_size,list(left.size))
            body=record['body_bbox']; scale=crop['point_to_pixel'][0]
            body_pixels=[max(0,math.floor(body[0]*scale)),max(0,math.floor(body[1]*scale)),
                         min(left.width,math.ceil(body[2]*scale)),min(left.height,math.ceil(body[3]*scale))]
            row={'record_index':record['index'],'kind':record['kind'],'body_bbox':body,
                'union_bbox':crop['union_bbox'],'body_pixel_box':body_pixels,'crop_pixel_box':crop['pixel_box'],
                'source_rect_size':crop['source_rect_size'],'point_to_pixel':crop['point_to_pixel'],
                'caption_count':len(record['captions']),'footnote_count':len(record['footnotes']),
                'included_attachment_count':sum(bool(item['include']) for item in crop['attachments']),
                'same_pixel_size':same_size}
            if same_size:
                for name,box in [('body',body_pixels),('union_crop',crop['pixel_box'])]:
                    part=mask.crop(box)
                    count=part.width*part.height-part.histogram()[0]
                    row[name+'_diff_pixel_count']=count
                    row[name+'_diff_pixel_ratio']=count/(part.width*part.height) if part.width*part.height else 0
                    row[name+'_diff_bbox']=list(part.getbbox()) if count else None
                    part.close()
                    for label,image in [('original',left),('embedded',right)]:
                        cropped=image.crop(box)
                        row[name+'_'+label+'_rgb_sha256']=digest(cropped.tobytes())
                        cropped.close()
            results.append(row)
    finally:
        if mask is not None: mask.close()
    return results


def _pdfium_rewrite(original,budget=lambda:None):
    """Reproduce upstream whole-document import/save; diagnostic only."""
    import io
    import pypdfium2 as pdfium
    require(len(original)<=512*1024*1024,'pdfium_source_bytes_bound')
    class BoundedBuffer(io.BytesIO):
        failure=None
        def write(self,data):
            # The SDK writes through a ctypes callback, which cannot propagate
            # Python exceptions. Stop retaining bytes and fail after save returns.
            if self.failure is not None: return len(data)
            if self.tell()+len(data)>MAX_PDFIUM_REWRITE_BYTES:
                self.failure='pdfium_rewritten_bytes_bound'
                return len(data)
            try: budget()
            except Exception:
                self.failure='probe_deadline'
                return len(data)
            return super().write(data)
    budget()
    source=pdfium.PdfDocument(original)
    destination=None
    try:
        require(1<=len(source)<=1000,'pdfium_page_count_bound')
        destination=pdfium.PdfDocument.new()
        budget()
        destination.import_pages(source,list(range(len(source))))
        require(len(destination)==len(source),'pdfium_import_page_count_mismatch')
        budget()
        with BoundedBuffer() as buffer:
            destination.save(buffer)
            require(buffer.failure is None,buffer.failure or 'pdfium_save_failed')
            rewritten=buffer.getvalue()
        budget()
        return rewritten,{'pypdfium2':str(pdfium.PYPDFIUM_INFO),'pdfium':str(pdfium.PDFIUM_INFO)}
    finally:
        if destination is not None: destination.close()
        source.close()


def pdfium_rewrite_diagnostics(original,authentic,supplied,page_index,metadata,decisions,budget=lambda:None):
    """Compare reproducible derived bytes; equality does not accept content loss."""
    import fitz
    import mineru_figure_sources as figures
    result={'diagnostic_only':True,'production_acceptance':False,
        'recipe':'mineru-3.4.4-whole-document-pdfium-import-save',
        'upstream_commit':'0dfc9460cd9ab693b9af60ae3fbffd7bc111b062',
        'page_index':page_index,'render_dpi':300}
    try:
        rewritten,runtime=_pdfium_rewrite(original,budget)
        result.update(runtime=runtime,rewritten_pdf_sha256=digest(rewritten),rewritten_pdf_bytes=len(rewritten),
            original_pdf_sha256=digest(original),original_pages=len(authentic),embedded_pages=len(supplied))
        budget()
        with fitz.open(stream=rewritten,filetype='pdf') as document:
            result.update(rewritten_pages=len(document),rewritten_encrypted=bool(document.is_encrypted),
                original_page_count_equal=len(document)==len(authentic),embedded_page_count_equal=len(document)==len(supplied))
            require(len(document)==len(authentic),'pdfium_rewritten_page_count_mismatch')
            require(not document.is_encrypted and page_index<len(document),'pdfium_rewritten_page_missing')
            actual,derived,embedded=authentic[page_index],document[page_index],supplied[page_index]
            geometry=figures._geometry(derived)
            result.update(rewritten_geometry=geometry,
                original_geometry_equal=exact_json(figures._geometry(actual),geometry),
                embedded_geometry_equal=exact_json(figures._geometry(embedded),geometry))
            budget()
            transformed=figures._render(derived)
            try:
                budget()
                left=figures._render(actual)
                try:
                    result['original_vs_rewritten']=_difference(left,transformed)
                    result['original_vs_rewritten']['selected_visual_differences']=selected_visual_differences(
                        left,transformed,metadata,decisions,page_index,figures._geometry(actual)['rect'][2:])
                finally: left.close()
                budget()
                right=figures._render(embedded)
                try:
                    result['rewritten_vs_embedded']=_difference(transformed,right)
                    result['rewritten_vs_embedded']['selected_visual_differences']=selected_visual_differences(
                        transformed,right,metadata,decisions,page_index,geometry['rect'][2:])
                finally: right.close()
            finally: transformed.close()
            for label in ('original_vs_rewritten','rewritten_vs_embedded'):
                comparison=result[label]
                comparison['rgb_equal']=comparison['same_size'] and comparison.get('diff_pixel_count')==0
            result['status']='checked'
            budget()
    except Exception as error:
        result.update(status='unavailable',category=str(error) if isinstance(error,ProbeError) else type(error).__name__)
    return result


def optional_content_restoration_diagnostics(original,embedded_bytes,authentic,supplied,metadata,decisions,used_pages,budget=lambda:None):
    """Test the production restoration with all selected pages; never hand off."""
    import mineru_figure_sources as figures
    from mineru_pdf_oc import (has_missing_optional_content,restore_missing_optional_content,
                               validate_restoration_receipt,OptionalContentError)
    from mineru_pdf_graph import PdfGraphError
    result={'diagnostic_only':True,'production_acceptance':False,'complete_source_handoff':False,
        'selected_page_count':len(used_pages),'checked_page_count':0,'all_selected_pages_equal':False,'pages':[]}
    if not has_missing_optional_content(authentic,supplied):
        result['status']='not_applicable'
        return result
    restored=None
    try:
        budget()
        restored,proof=restore_missing_optional_content(authentic,supplied,
            original_sha256=digest(original),embedded_sha256=digest(embedded_bytes),budget=budget)
        total=0
        for index in used_pages:
            budget()
            actual,other=authentic[index],restored[index]
            geometry=figures._geometry(actual)
            equal=exact_json(geometry,figures._geometry(other))
            size=metadata['pages'][index]['provider_size']
            provider_size_equal=not any(abs(a-b)>=1.1 for a,b in zip(size,[actual.rect.width,actual.rect.height]))
            page={'page_index':index,'geometry_equal':equal,'provider_size_equal':provider_size_equal}
            result['pages'].append(page);result['checked_page_count']+=1
            if not equal or not provider_size_equal:
                result.update(status='mismatch',stage='geometry')
                return result
            total+=math.ceil(actual.rect.width*300/72)*math.ceil(actual.rect.height*300/72)
            require(total<=figures.MAX_CARRIED_PAGE_PIXELS,'render_pixels_bound')
            left,right=figures._render(actual),figures._render(other)
            try:
                page['comparison']=_difference(left,right)
                if not page['comparison']['same_size'] or page['comparison'].get('diff_pixel_count'):
                    page['selected_visual_differences']=selected_visual_differences(left,right,metadata,decisions,index,geometry['rect'][2:])
                    result.update(status='mismatch',stage='rgb_pixels')
                    return result
            finally:left.close();right.close()
        proof['verified_page_indices']=used_pages
        validate_restoration_receipt(proof,original_sha256=digest(original),embedded_sha256=proof['embedded_pdf_sha256'],page_indices=used_pages)
        result.update(status='verified',all_selected_pages_equal=True,restoration_proof=proof)
        budget()
    except Exception as error:
        result.update(status='rejected',category=str(error) if isinstance(error,(OptionalContentError,PdfGraphError,ProbeError)) else type(error).__name__)
        path=getattr(error,'path_sha256',None)
        if isinstance(path,str) and re.fullmatch(r'[0-9a-f]{64}',path):result['path_sha256']=path
        details=getattr(error,'sanitized_details',None)
        if isinstance(error,PdfGraphError) and isinstance(details,dict):result['graph_details']=details
    finally:
        if restored is not None:restored.close()
    return result


def _restore_output_intents_diagnostic(original,embedded,budget=lambda:None):
    """Copy only the admitted catalog color profile into an in-memory copy.

    Diagnostic serialization is not a production repair. The caller compares
    the complete drawing graph and every selected page before reporting proof.
    No original/provider file or cache is overwritten.
    """
    import io
    import logging
    from pypdf import PdfReader,PdfWriter
    from pypdf.generic import ArrayObject,DictionaryObject,NameObject,StreamObject
    require(0<len(original)<=16*1024*1024 and 0<len(embedded)<=16*1024*1024,
            'output_intent_probe_input_bound')
    logger=logging.getLogger('pypdf')
    previous=logger.disabled,logger.propagate,logger.handlers[:]
    logger.disabled,logger.propagate,logger.handlers=True,False,[logging.NullHandler()]
    try:
        budget()
        source=PdfReader(io.BytesIO(original));provider=PdfReader(io.BytesIO(embedded))
        source_root=source.trailer['/Root'];provider_root=provider.trailer['/Root']
        require('/OutputIntents' in source_root and not provider_root.get('/OutputIntents'),
                'output_intent_probe_missing_required')
        intents=source_root['/OutputIntents']
        require(isinstance(intents,ArrayObject) and 1<=len(intents)<=8,'output_intent_probe_array_bound')
        total_profiles=0
        for item in intents:
            budget();intent=item.get_object()
            require(isinstance(intent,DictionaryObject) and set(intent)<={
                '/Type','/S','/OutputCondition','/OutputConditionIdentifier','/RegistryName','/Info','/DestOutputProfile'},
                'output_intent_probe_keys')
            profile=intent.get('/DestOutputProfile')
            profile=profile.get_object() if profile is not None else None
            require(isinstance(profile,StreamObject),'output_intent_probe_profile_required')
            require(set(profile)<={'/N','/Alternate','/Range','/Length','/Filter','/DecodeParms'},
                    'output_intent_probe_profile_keys')
            profile_bytes=profile.get_data();total_profiles+=len(profile_bytes)
            require(128<=len(profile_bytes)<=8*1024*1024 and total_profiles<=16*1024*1024
                    and profile_bytes[36:40]==b'acsp','output_intent_probe_profile_bound')
        writer=PdfWriter();writer.clone_document_from_reader(provider)
        writer._root_object[NameObject('/OutputIntents')]=source_root.raw_get('/OutputIntents').clone(writer)
        output=io.BytesIO();writer.write(output);restored=output.getvalue()
        require(0<len(restored)<=32*1024*1024,'output_intent_probe_output_bound')
        budget()
        return restored
    finally:
        logger.disabled,logger.propagate,logger.handlers=previous


def output_intent_restoration_diagnostics(original,embedded_bytes,authentic,supplied,metadata,decisions,used_pages,budget=lambda:None):
    """Test the observed PDFium catalog loss without relaxing production gates."""
    import fitz
    import mineru_figure_sources as figures
    from mineru_pdf_graph import bind_pdf_render_graph,PdfGraphError
    result={'diagnostic_only':True,'production_acceptance':False,'complete_source_handoff':False,
        'selected_page_count':len(used_pages),'checked_page_count':0,'all_selected_pages_equal':False,'pages':[]}
    if (authentic.xref_get_key(authentic.pdf_catalog(),'OutputIntents')[0]=='null'
            or supplied.xref_get_key(supplied.pdf_catalog(),'OutputIntents')[0]!='null'):
        result['status']='not_applicable'
        return result
    try:
        restored_bytes=_restore_output_intents_diagnostic(original,embedded_bytes,budget)
        result.update(original_pdf_sha256=digest(original),embedded_pdf_sha256=digest(embedded_bytes),
                      restored_pdf_sha256=digest(restored_bytes),restored_pdf_bytes=len(restored_bytes))
        with fitz.open(stream=restored_bytes,filetype='pdf') as restored:
            require(len(restored)==len(authentic)==len(supplied),'output_intent_probe_page_count')
            # The graph includes the original ICC stream and all existing page
            # drawing objects. A body/annotation change cannot be repaired away.
            try:
                binding=bind_pdf_render_graph(authentic,restored,budget=budget)
                result.update(graph_binding_status='verified',graph_binding=binding.receipt)
            except PdfGraphError as error:
                # Pixels remain useful diagnostic evidence when an independent
                # structural check rejects. This cannot become acceptance.
                graph={'category':str(error)}
                if getattr(error,'path_sha256',None):graph['path_sha256']=error.path_sha256
                if isinstance(getattr(error,'sanitized_details',None),dict):graph['details']=error.sanitized_details
                result.update(graph_binding_status='rejected',graph_failure=graph)
            total=0
            for index in used_pages:
                budget();actual,other=authentic[index],restored[index]
                geometry=figures._geometry(actual)
                equal=exact_json(geometry,figures._geometry(other))
                size=metadata['pages'][index]['provider_size']
                provider_size_equal=not any(abs(a-b)>=1.1 for a,b in zip(size,[actual.rect.width,actual.rect.height]))
                page={'page_index':index,'geometry_equal':equal,'provider_size_equal':provider_size_equal}
                result['pages'].append(page);result['checked_page_count']+=1
                if not equal or not provider_size_equal:
                    result.update(status='mismatch',stage='geometry');return result
                total+=math.ceil(actual.rect.width*300/72)*math.ceil(actual.rect.height*300/72)
                require(total<=figures.MAX_CARRIED_PAGE_PIXELS,'render_pixels_bound')
                left,right=figures._render(actual),figures._render(other)
                try:
                    page['comparison']=_difference(left,right)
                    if not page['comparison']['same_size'] or page['comparison'].get('diff_pixel_count'):
                        page['selected_visual_differences']=selected_visual_differences(left,right,metadata,decisions,index,geometry['rect'][2:])
                        result.update(status='mismatch',stage='rgb_pixels');return result
                finally:left.close();right.close()
            result.update(status='verified' if result['graph_binding_status']=='verified' else
                          'pixels_verified_graph_rejected',all_selected_pages_equal=True)
    except Exception as error:
        result.update(status='rejected',category=str(error) if isinstance(error,(PdfGraphError,ProbeError)) else type(error).__name__)
        path=getattr(error,'path_sha256',None)
        if isinstance(path,str) and re.fullmatch(r'[0-9a-f]{64}',path):result['path_sha256']=path
        details=getattr(error,'sanitized_details',None)
        if isinstance(error,PdfGraphError) and isinstance(details,dict):result['graph_details']=details
    return result


def compare_cached_pdf(original_path,payload,*,original_sha256,clock=time.monotonic,deadline=None):
    """Match the four production gates; alternate annotation renders are diagnostic only."""
    import fitz
    from PIL import Image
    import mineru_figure_sources as figures
    from consume_legacy_mineru import safe_unzip
    original_path = Path(original_path)
    original = original_path.read_bytes()
    require(digest(original) == original_sha256,'original_bytes_changed')
    deadline = clock()+MAX_PROBE_SECONDS if deadline is None else deadline
    def budget(): require(clock()<deadline,'probe_deadline')
    with tempfile.TemporaryDirectory(prefix='mineru-figure-binding-probe-') as temporary:
        root = Path(temporary)/'raw'; safe_unzip(payload,root)
        found = figures._metadata_files(root)
        require(found is not None,'provider_metadata_missing')
        (cp,content),(mp,middle),paths = found
        metadata = figures._normalise(content,middle)
        embedded = [path for path in paths if path.is_file() and path.suffix.lower() == '.pdf']
        require(len(embedded)==1,'embedded_pdf_ambiguous')
        embedded_raw = figures._regular(embedded[0],root,512*1024*1024)
        decisions = figures._decisions(metadata,MAX_VISUALS)
        used_pages = sorted({record['page_idx'] for record,decision in zip(metadata['records'],decisions)
                             if decision['selected']})
        require(len(used_pages)<=MAX_VISUALS,'selected_pages_bound')
        result = {'status':'checked','stage':'complete','original_pdf_sha256':digest(original),
            'original_pdf_bytes':len(original),'embedded_pdf_sha256':digest(embedded_raw),
            'embedded_pdf_bytes':len(embedded_raw),'result_zip_sha256':digest(payload),'result_zip_bytes':len(payload),
            'metadata_pages':len(metadata['pages']),'selected_visual_count':sum(row['selected'] for row in decisions),
            'selected_page_count':len(used_pages),'checked_page_count':0,'pages':[],
            'runtime':{'pymupdf':fitz.VersionBind,'mupdf':fitz.VersionFitz},
            'all_selected_pages_equal':False}
        with figures._silent_mupdf(), fitz.open(stream=original,filetype='pdf') as authentic, \
                fitz.open(stream=embedded_raw,filetype='pdf') as supplied:
            result.update(original_pages=len(authentic),embedded_pages=len(supplied),
                original_encrypted=bool(authentic.is_encrypted),embedded_encrypted=bool(supplied.is_encrypted))
            if (authentic.is_encrypted or supplied.is_encrypted or len(authentic)!=len(metadata['pages'])
                    or len(supplied)!=len(authentic)):
                result.update(status='mismatch',stage='page_count_or_encryption')
                return result
            total_pixels = 0
            for index in used_pages:
                budget()
                actual,other = authentic[index],supplied[index]
                left_geometry,right_geometry = figures._geometry(actual),figures._geometry(other)
                page = {'page_index':index,'original_geometry':left_geometry,'embedded_geometry':right_geometry,
                        'original_objects':_page_objects(actual),'embedded_objects':_page_objects(other)}
                result['pages'].append(page); result['checked_page_count'] += 1
                geometry_equal = exact_json(left_geometry,right_geometry)
                page['viewport_equal'] = exact_json(left_geometry['rect'],right_geometry['rect'])
                size = metadata['pages'][index]['provider_size']; page['provider_size'] = size
                provider_size_equal = not any(abs(a-b)>=1.1 for a,b in zip(size,[actual.rect.width,actual.rect.height]))
                page['geometry_equal'] = geometry_equal
                page['provider_size_equal'] = provider_size_equal
                pixels = math.ceil(actual.rect.width*300/72)*math.ceil(actual.rect.height*300/72)
                total_pixels += pixels
                require(total_pixels<=figures.MAX_CARRIED_PAGE_PIXELS,'render_pixels_bound')
                budget()
                left,right = figures._render(actual),figures._render(other)
                try:
                    difference = _difference(left,right)
                    if not difference['same_size'] or difference.get('diff_pixel_count'):
                        page['selected_visual_differences'] = selected_visual_differences(
                            left,right,metadata,decisions,index,left_geometry['rect'][2:])
                finally: left.close(); right.close()
                default_equal = difference['same_size'] and difference.get('diff_pixel_count') == 0
                page['default_rgb_equal'] = default_equal
                if not geometry_equal or not provider_size_equal or not default_equal:
                    page['annots_true'] = difference
                    result.update(status='mismatch',stage='page_geometry' if not geometry_equal else
                                  'provider_page_size' if not provider_size_equal else 'rgb_pixels')
                    budget()
                    def without_annotations(value):
                        return figures._render(value,annots=False)
                    left,right = without_annotations(actual),without_annotations(other)
                    try: page['annots_false'] = _difference(left,right)
                    finally: left.close(); right.close()
                    page['annots_false_equal'] = (page['annots_false']['same_size']
                        and page['annots_false'].get('diff_pixel_count') == 0)
                    if not default_equal:
                        page['semantic_diagnostics'] = semantic_diagnostics(actual,other,budget)
                    page['pdfium_rewrite'] = pdfium_rewrite_diagnostics(
                        original,authentic,supplied,index,metadata,decisions,budget)
                    page['optional_content_restoration'] = optional_content_restoration_diagnostics(
                        original,embedded_raw,authentic,supplied,metadata,decisions,used_pages,budget)
                    page['output_intent_restoration'] = output_intent_restoration_diagnostics(
                        original,embedded_raw,authentic,supplied,metadata,decisions,used_pages,budget)
                    require(digest(original_path.read_bytes())==original_sha256,'original_bytes_changed')
                    return result
                page['rgb_sha256'] = difference['original_rgb_sha256']
            result['all_selected_pages_equal'] = True
        require(digest(original_path.read_bytes())==original_sha256,'original_bytes_changed')
        return result


ENCRYPTED_EXPORT_NAME='mineru-figure-binding-export.cms'
MAX_EXPORT_BYTES=128*1024*1024


def _prepare_encrypted_export(recipient_cert_pem,encrypted_output,input_dir):
    if not recipient_cert_pem:
        require(encrypted_output is None,'export_recipient_required')
        return None
    from export_market_views_original_page_qa import checked_recipient
    recipient,certificate=checked_recipient(recipient_cert_pem)
    require(encrypted_output is not None,'encrypted_export_output_required')
    target=Path(encrypted_output)
    require(target.name==ENCRYPTED_EXPORT_NAME and not target.exists() and not target.is_symlink()
            and target.parent.is_dir() and not target.parent.is_symlink(),'encrypted_export_output_invalid')
    require(Path(input_dir).resolve() not in (target.resolve(),*target.resolve().parents),'encrypted_export_output_invalid')
    return recipient,certificate,target


def _write_encrypted_export(prepared,original,payload,private_receipt):
    import io
    import zipfile
    from export_market_views_original_page_qa import encrypt_payload
    recipient,certificate,target=prepared
    manifest=encoded(private_receipt)
    require(0<len(original)+len(payload)+len(manifest)<=MAX_EXPORT_BYTES,'encrypted_export_size_bound')
    buffer=io.BytesIO()
    with zipfile.ZipFile(buffer,'w',compression=zipfile.ZIP_STORED) as archive:
        for name,raw in [('original.pdf',original),('result.zip',payload),('binding-manifest.json',manifest)]:
            item=zipfile.ZipInfo(name,(1980,1,1,0,0,0));item.external_attr=0o600<<16
            archive.writestr(item,raw)
    plaintext=buffer.getvalue()
    require(len(plaintext)<=MAX_EXPORT_BYTES,'encrypted_export_size_bound')
    ciphertext=encrypt_payload(plaintext,recipient)
    descriptor=os.open(target,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    try:
        with os.fdopen(descriptor,'wb') as output:output.write(ciphertext)
    except Exception:
        target.unlink(missing_ok=True)
        raise
    return {'schema':1,'status':'encrypted_exact_source_export','diagnostic_only':True,
        'production_acceptance':False,'cipher':'CMS-EnvelopedData-AES-256-CBC',
        'plaintext_payload_sha256':digest(plaintext),'ciphertext_sha256':digest(ciphertext),
        'ciphertext_bytes':len(ciphertext),'original_pdf_sha256':digest(original),'result_zip_sha256':digest(payload),
        **certificate}


def probe(ledger,result_cache,input_dir,expected_articles,date_folder,source_ordinal,*,
          recipient_cert_pem='',encrypted_output=None,export_context=None):
    require(type(source_ordinal) is int and 1<=source_ordinal<=expected_articles,'source_ordinal_invalid')
    export=_prepare_encrypted_export(recipient_cert_pem,encrypted_output,input_dir)
    deadline = ledger.clock()+MAX_PROBE_SECONDS
    raw_manifest,bindings,pairs = frozen_inputs(input_dir,Path(input_dir)/MANIFEST,expected_articles,date_folder)
    readonly = copy.copy(ledger); readonly.store = ReadOnlyStore(ledger.store)
    readonly.provider = ReadOnlyProvider(ledger.provider,ledger.clock,deadline)
    readonly.forbid_new_submissions = True
    groups,_ = original_groups(readonly,pairs,source_run_id='',allow_fresh=False)
    selected_path,selected_source = pairs[source_ordinal-1]
    binding = readonly.bind(selected_path,selected_source)
    roots = [root for root,_ in groups if any(item['id']==binding['id'] for item in root['files'])]
    require(len(roots)==1,'selected_root_identity')
    rows,counts = read_completed_batch(readonly,roots[0])
    row = rows.get(binding['id'])
    require(isinstance(row,dict) and str(row.get('state','')).lower() in DONE,'selected_result_not_complete')
    lineage = row['_recovery_lineage']
    identity = cache_identity(binding,lineage)
    payload = result_cache.get(binding,lineage)
    require(payload is not None,'selected_cache_missing')
    result = compare_cached_pdf(selected_path,payload,original_sha256=binding['sha256'],
                                clock=ledger.clock,deadline=deadline)
    readonly.store.verify()
    raw_after,bindings_after,pairs_after = frozen_inputs(input_dir,Path(input_dir)/MANIFEST,expected_articles,date_folder)
    require(raw_after==raw_manifest and exact_json(bindings_after,bindings),'original_inventory_changed')
    response = {'schema':1,'diagnostic_only':True,'production_acceptance':False,'complete_source_handoff':False,
        'provider_posts':0,'provider_uploads':0,'provider_zip_downloads':0,'canonical_ledger_writes':0,
        'cache_writes':0,'provider_gets':readonly.provider.gets,'source_ordinal':source_ordinal,
        'original_report_count':expected_articles,'manifest_sha256':digest(raw_manifest),
        'source_binding_sha256':binding['id'],'cache_identity_sha256':identity,
        'selected_root_members':counts['admitted'],'selected_root_completed':counts['completed'],
        'selected_child_ordinal':lineage['child_ordinal'],'comparison':result}
    if export is not None:
        original=selected_path.read_bytes()
        require(digest(original)==binding['sha256'],'original_bytes_changed')
        private={'schema':1,'kind':'exact_mineru_figure_binding_export','source_context':export_context or {},
            'date_folder':date_folder,'source_ordinal':source_ordinal,'expected_articles':expected_articles,
            'manifest_sha256':digest(raw_manifest),'source_binding':binding,'cache_lineage':lineage,
            'cache_identity_sha256':identity,'files':{
                'original.pdf':{'sha256':digest(original),'bytes':len(original)},
                'result.zip':{'sha256':digest(payload),'bytes':len(payload)}}}
        response['encrypted_export']=_write_encrypted_export(export,original,payload,private)
    return response


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir',required=True); parser.add_argument('--output',required=True)
    parser.add_argument('--source-run-id',required=True); parser.add_argument('--producer-json',required=True)
    parser.add_argument('--date-folder',required=True); parser.add_argument('--expected-articles',required=True,type=int)
    parser.add_argument('--source-ordinal',required=True,type=int)
    parser.add_argument('--recipient-cert-pem',default=os.environ.get('RECIPIENT_CERT_PEM',''))
    args = parser.parse_args(argv)
    result = {'schema':1,'diagnostic_only':True,'production_acceptance':False,'complete_source_handoff':False,
        'provider_posts':0,'provider_uploads':0,'provider_zip_downloads':0,'canonical_ledger_writes':0,'cache_writes':0}
    code = 2
    try:
        env = os.environ; repo = env.get('GITHUB_REPOSITORY','')
        require(env.get('GITHUB_ACTIONS')=='true' and env.get('GITHUB_EVENT_NAME')=='workflow_dispatch'
            and env.get('GITHUB_REF')=='refs/heads/main'
            and env.get('GITHUB_WORKFLOW_REF')==repo+'/'+WORKFLOW+'@refs/heads/main','reviewed_main_probe_required')
        metadata = json.loads(Path(args.producer_json).read_bytes())
        source_sha = validate_request(metadata,args.source_run_id,args.date_folder,args.expected_articles,args.source_ordinal,repo)
        require(re.fullmatch(r'[a-f0-9]{40}',env.get('GITHUB_SHA','')),'probe_execution_sha_invalid')
        import boto3
        from botocore.config import Config
        import requests
        from private_workflow_handoff import require_env
        from mineru_task_ledger import R2Store,Provider
        from mineru_result_cache import ResultCache
        from smoke_mineru_api import credentials,NoRedirectHTTP
        client = ReadOnlyR2Client(boto3.client('s3',
            endpoint_url='https://'+require_env('R2_ACCOUNT_ID')+'.r2.cloudflarestorage.com',
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'),aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
            region_name='auto',config=Config(connect_timeout=20,read_timeout=30,
                retries={'total_max_attempts':1,'mode':'standard'})))
        bucket = require_env('R2_BUCKET')
        ledger = Ledger(R2Store('dropbox',client=client,bucket=bucket),
            Provider(NoRedirectHTTP(requests.request),'https://mineru.net'),'dropbox','https://mineru.net',
            OPTIONS,credentials(env))
        result = probe(ledger,ResultCache(client,bucket),args.input_dir,args.expected_articles,args.date_folder,args.source_ordinal,
            recipient_cert_pem=args.recipient_cert_pem,
            encrypted_output=Path(args.output).with_name(ENCRYPTED_EXPORT_NAME) if args.recipient_cert_pem else None,
            export_context={'source_run_id':args.source_run_id,'source_execution_sha':source_sha,'probe_execution_sha':env['GITHUB_SHA']})
        result.update(source_run_id=args.source_run_id,date_folder=args.date_folder,
            source_execution_sha=source_sha,probe_execution_sha=env['GITHUB_SHA'])
        code = 0
    except Exception as error:
        category = str(error) if isinstance(error,ProbeError) else type(error).__name__
        result.update(status='stopped',category=category)
    Path(args.output).write_bytes(encoded(result)+b'\n')
    print(json.dumps(result,sort_keys=True))
    return code


if __name__=='__main__': raise SystemExit(main())
