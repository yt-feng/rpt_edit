"""Restore only missing optional-content configuration after strict graph binding.

The provider PDF bytes are never changed. A temporary in-memory document gets
only the authenticated original's mapped catalog OCProperties, and callers must
still require exact page geometry and RGB equality before accepting any output.
"""
from __future__ import annotations

import hashlib
import io
import json
import re

POLICY = 'authenticated-ocproperties-restoration-v1'
MAX_BYTES = 512 * 1024 * 1024
MAX_CONFIG_BYTES = 4 * 1024 * 1024
MAX_OBJECTS = 100000
MAX_CONFIG_NODES = 20000
MAX_DEPTH = 64


class OptionalContentError(ValueError):
    pass


def require(value, category):
    if not value:
        raise OptionalContentError(category)


def encoded(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def has_missing_optional_content(original,embedded):
    return (original.xref_get_key(original.pdf_catalog(),'OCProperties')[0] != 'null'
            and embedded.xref_get_key(embedded.pdf_catalog(),'OCProperties')[0] == 'null')


def _provider_inventory(document,budget):
    """Bind every existing object, ignoring only the one allowed catalog key."""
    count=document.xref_length()
    require(1<count<=MAX_OBJECTS,'oc_provider_object_bound')
    catalog=document.pdf_catalog()
    hasher=hashlib.sha256();total=0
    for xref in range(1,count):
        budget()
        if xref==catalog:
            value={key:document.xref_get_key(xref,key) for key in document.xref_get_keys(xref)
                   if key!='OCProperties'}
            header=encoded(value)
        else:
            header=document.xref_object(xref,compressed=True).encode()
        raw=document.xref_stream_raw(xref) if document.xref_is_stream(xref) else b''
        total+=len(header)+len(raw)
        require(total<=MAX_BYTES,'oc_provider_bytes_bound')
        hasher.update(encoded([xref,len(header),digest(header),len(raw),digest(raw)]))
    return {'object_count':count-1,'sha256':hasher.hexdigest()}


def _groups(document,budget):
    require(document.xref_length()<=MAX_OBJECTS,'oc_provider_object_bound')
    result=set()
    for xref in range(1,document.xref_length()):
        budget()
        if document.xref_get_key(xref,'Type')==('name','/OCG'):
            result.add(xref)
    return result


def _mapped_configuration(original,binding,budget):
    from pypdf.generic import (ArrayObject,DictionaryObject,IndirectObject,NameObject,
                              NullObject,BooleanObject,NumberObject,FloatObject,
                              TextStringObject,ByteStringObject)
    from mineru_pdf_graph import parse_pdf_value
    kind,value=original.xref_get_key(original.pdf_catalog(),'OCProperties')
    require(kind in {'dict','xref'},'oc_original_configuration_invalid')
    root=parse_pdf_value(value)
    nodes=0;original_group_refs=[]
    def reference_key(value):
        require(value.generation==0 and 0<value.idnum<original.xref_length(),'oc_configuration_reference_invalid')
        return value.idnum,value.generation
    def resolve(value,seen=frozenset()):
        if not isinstance(value,IndirectObject): return value
        key=reference_key(value)
        require(key not in seen and len(seen)<MAX_DEPTH,'oc_configuration_cycle')
        require(not original.xref_is_stream(value.idnum),'oc_configuration_stream')
        return resolve(parse_pdf_value(original.xref_object(value.idnum)),seen|{key})
    root=resolve(root)
    require(isinstance(root,DictionaryObject),'oc_original_configuration_invalid')
    require(set(root)<= {'/OCGs','/D','/Configs'} and {'/OCGs','/D'}<=set(root),'oc_configuration_keys')
    groups=resolve(root.raw_get('/OCGs'))
    require(isinstance(groups,ArrayObject) and 0<len(groups)<=1000,'oc_configuration_groups')
    for group in groups:
        require(isinstance(group,IndirectObject),'oc_configuration_group_reference')
        key=reference_key(group)
        require(key in binding.ocg_mapping,'oc_configuration_unbound_group')
        original_group_refs.append(key)
    require(len(set(original_group_refs))==len(original_group_refs),'oc_configuration_duplicate_group')
    require(set(original_group_refs)==set(binding.ocg_mapping),'oc_configuration_group_coverage')
    config_keys={'/Name','/Creator','/BaseState','/ON','/OFF','/Intent','/AS','/Order','/ListMode','/RBGroups','/Locked'}
    configs=[resolve(root.raw_get('/D'))]
    if '/Configs' in root:
        others=resolve(root.raw_get('/Configs'))
        require(isinstance(others,ArrayObject) and len(others)<=100,'oc_configuration_count')
        configs.extend(resolve(item) for item in others)
    require(all(isinstance(item,DictionaryObject) and set(item)<=config_keys for item in configs),'oc_configuration_default_keys')
    def clone(value,stack=frozenset(),depth=0):
        nonlocal nodes
        budget();nodes+=1
        require(nodes<=MAX_CONFIG_NODES and depth<=MAX_DEPTH,'oc_configuration_bound')
        if isinstance(value,IndirectObject):
            key=reference_key(value)
            if key in binding.ocg_mapping:
                target=binding.ocg_mapping[key]
                return IndirectObject(target[0],target[1],None)
            require(key not in stack,'oc_configuration_cycle')
            require(not original.xref_is_stream(value.idnum),'oc_configuration_stream')
            resolved=parse_pdf_value(original.xref_object(value.idnum))
            if isinstance(resolved,DictionaryObject):
                require(resolved.get('/Type') not in {'/OCG','/OCMD'},'oc_configuration_unbound_group')
            return clone(resolved,stack|{key},depth+1)
        if isinstance(value,DictionaryObject):
            require(value.get('/Type') not in {'/OCG','/OCMD'},'oc_configuration_inline_group')
            result=DictionaryObject()
            for key in sorted(value):
                require(isinstance(key,NameObject),'oc_configuration_key_type')
                result[key]=clone(value.raw_get(key),stack,depth+1)
            return result
        if isinstance(value,ArrayObject):
            return ArrayObject([clone(item,stack,depth+1) for item in value])
        require(isinstance(value,(NameObject,NullObject,BooleanObject,NumberObject,FloatObject,TextStringObject,ByteStringObject)),
                'oc_configuration_value_type')
        return value
    result=clone(root)
    buffer=io.BytesIO();result.write_to_stream(buffer)
    raw=buffer.getvalue()
    require(len(raw)<=MAX_CONFIG_BYTES,'oc_configuration_bytes_bound')
    source_buffer=io.BytesIO();root.write_to_stream(source_buffer)
    source=source_buffer.getvalue()
    require(len(source)<=MAX_CONFIG_BYTES,'oc_configuration_bytes_bound')
    return raw,{'original_oc_properties_sha256':digest(source),'mapped_oc_properties_sha256':digest(raw),
                'ocg_count':len(original_group_refs),'configuration_nodes':nodes}


def restore_missing_optional_content(original,embedded,*,original_sha256,embedded_sha256,budget=lambda:None):
    """Return (owned temporary document, proof); never accept page pixels here."""
    import fitz
    from mineru_pdf_graph import bind_pdf_render_graph
    require(all(isinstance(value,str) and re.fullmatch(r'[0-9a-f]{64}',value)
                for value in (original_sha256,embedded_sha256)),'oc_source_binding_invalid')
    require(has_missing_optional_content(original,embedded),'oc_missing_configuration_required')
    binding=bind_pdf_render_graph(original,embedded,budget=budget)
    require(_groups(original,budget)=={key[0] for key in binding.ocg_mapping},'oc_original_group_coverage')
    require(_groups(embedded,budget)=={key[0] for key in binding.ocg_mapping.values()},'oc_provider_group_coverage')
    configuration,config_proof=_mapped_configuration(original,binding,budget)
    before=_provider_inventory(embedded,budget)
    raw=embedded.tobytes(no_new_id=True)
    require(len(raw)<=MAX_BYTES,'oc_provider_bytes_bound')
    with fitz.open(stream=raw,filetype='pdf') as working:
        require(_provider_inventory(working,budget)==before,'oc_provider_clone_changed')
        working.xref_set_key(working.pdf_catalog(),'OCProperties',configuration.decode('ascii'))
        require(_provider_inventory(working,budget)==before,'oc_provider_content_changed')
        restored_bytes=working.tobytes(no_new_id=True)
    require(len(restored_bytes)<=MAX_BYTES,'oc_provider_bytes_bound')
    restored=fitz.open(stream=restored_bytes,filetype='pdf')
    try:
        require(_provider_inventory(restored,budget)==before,'oc_provider_content_changed')
        require(len(restored)==len(embedded),'oc_provider_pages_changed')
        proof={'schema':1,'policy':POLICY,'original_pdf_sha256':original_sha256,
            'embedded_pdf_sha256':embedded_sha256,'provider_catalog_was_missing':True,
            'restored_pdf_sha256':digest(restored_bytes),'restored_pdf_bytes':len(restored_bytes),
            'preserved_provider_objects':before,'graph_binding':binding.receipt,
            'verified_page_indices':[],**config_proof}
        return restored,proof
    except Exception:
        restored.close()
        raise


def validate_restoration_receipt(value,*,original_sha256,embedded_sha256,page_indices):
    from mineru_pdf_graph import validate_graph_receipt
    required={'schema','policy','original_pdf_sha256','embedded_pdf_sha256','provider_catalog_was_missing',
        'restored_pdf_sha256','restored_pdf_bytes','preserved_provider_objects','graph_binding','verified_page_indices',
        'original_oc_properties_sha256','mapped_oc_properties_sha256','ocg_count','configuration_nodes'}
    require(isinstance(value,dict) and set(value)==required,'oc_receipt_keys')
    require(type(value['schema']) is int and value['schema']==1 and value['policy']==POLICY,'oc_receipt_policy')
    require(value['original_pdf_sha256']==original_sha256 and value['embedded_pdf_sha256']==embedded_sha256,
            'oc_receipt_binding')
    require(value['provider_catalog_was_missing'] is True and isinstance(value['verified_page_indices'],list)
            and all(type(index) is int for index in value['verified_page_indices'])
            and value['verified_page_indices']==page_indices,'oc_receipt_pages')
    for key in ('original_pdf_sha256','embedded_pdf_sha256','restored_pdf_sha256','original_oc_properties_sha256','mapped_oc_properties_sha256'):
        require(isinstance(value[key],str) and re.fullmatch(r'[0-9a-f]{64}',value[key]),'oc_receipt_hash')
    for key,limit in [('restored_pdf_bytes',MAX_BYTES),('ocg_count',1000),('configuration_nodes',MAX_CONFIG_NODES)]:
        require(type(value[key]) is int and 1<=value[key]<=limit,'oc_receipt_count')
    inventory=value['preserved_provider_objects']
    require(isinstance(inventory,dict) and set(inventory)=={'object_count','sha256'},'oc_receipt_inventory')
    require(type(inventory['object_count']) is int and 1<=inventory['object_count']<MAX_OBJECTS,'oc_receipt_count')
    require(isinstance(inventory['sha256'],str) and re.fullmatch(r'[0-9a-f]{64}',inventory['sha256']),'oc_receipt_hash')
    graph=validate_graph_receipt(value['graph_binding'])
    require(value['ocg_count']==graph['ocg_count'],'oc_receipt_group_count')
    require(all(0<=index<graph['pages'] for index in page_indices) and page_indices==sorted(set(page_indices)),
            'oc_receipt_pages')
    return value
