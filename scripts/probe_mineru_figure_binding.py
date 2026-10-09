#!/usr/bin/env python3
"""Read one exact cached result and diagnose original/provider figure gates.

This probe never downloads provider ZIP URLs, submits jobs, writes caches, or
creates a source handoff. Its public output contains only counts and hashes.
"""
from __future__ import annotations
import argparse
from collections import Counter
import copy
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
                try: difference = _difference(left,right)
                finally: left.close(); right.close()
                default_equal = difference['same_size'] and difference.get('diff_pixel_count') == 0
                page['default_rgb_equal'] = default_equal
                if not geometry_equal or not provider_size_equal or not default_equal:
                    page['annots_true'] = difference
                    result.update(status='mismatch',stage='page_geometry' if not geometry_equal else
                                  'provider_page_size' if not provider_size_equal else 'rgb_pixels')
                    budget()
                    def without_annotations(value):
                        pix = value.get_pixmap(matrix=fitz.Matrix(300/72,300/72),alpha=False,
                                               colorspace=fitz.csRGB,annots=False)
                        return Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
                    left,right = without_annotations(actual),without_annotations(other)
                    try: page['annots_false'] = _difference(left,right)
                    finally: left.close(); right.close()
                    page['annots_false_equal'] = (page['annots_false']['same_size']
                        and page['annots_false'].get('diff_pixel_count') == 0)
                    require(digest(original_path.read_bytes())==original_sha256,'original_bytes_changed')
                    return result
                page['rgb_sha256'] = difference['original_rgb_sha256']
            result['all_selected_pages_equal'] = True
        require(digest(original_path.read_bytes())==original_sha256,'original_bytes_changed')
        return result


def probe(ledger,result_cache,input_dir,expected_articles,date_folder,source_ordinal):
    require(type(source_ordinal) is int and 1<=source_ordinal<=expected_articles,'source_ordinal_invalid')
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
    return {'schema':1,'diagnostic_only':True,'production_acceptance':False,'complete_source_handoff':False,
        'provider_posts':0,'provider_uploads':0,'provider_zip_downloads':0,'canonical_ledger_writes':0,
        'cache_writes':0,'provider_gets':readonly.provider.gets,'source_ordinal':source_ordinal,
        'original_report_count':expected_articles,'manifest_sha256':digest(raw_manifest),
        'source_binding_sha256':binding['id'],'cache_identity_sha256':identity,
        'selected_root_members':counts['admitted'],'selected_root_completed':counts['completed'],
        'selected_child_ordinal':lineage['child_ordinal'],'comparison':result}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir',required=True); parser.add_argument('--output',required=True)
    parser.add_argument('--source-run-id',required=True); parser.add_argument('--producer-json',required=True)
    parser.add_argument('--date-folder',required=True); parser.add_argument('--expected-articles',required=True,type=int)
    parser.add_argument('--source-ordinal',required=True,type=int)
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
        result = probe(ledger,ResultCache(client,bucket),args.input_dir,args.expected_articles,args.date_folder,args.source_ordinal)
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
