"""Restore an admitted PDF's lost catalog color profile in a temporary copy.

The raw provider and original bytes remain immutable. A complete drawing-graph
binding is mandatory, including the restored ICC stream; callers still require
exact geometry and 300-dpi RGB equality for every selected source page.
"""
from __future__ import annotations

import hashlib
import io
import logging
import re

POLICY = 'authenticated-outputintents-restoration-v1'
MAX_PDF_BYTES = 512 * 1024 * 1024
MAX_PROFILE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_PROFILE_BYTES = 16 * 1024 * 1024
MAX_PROFILES = 8


class OutputIntentError(ValueError):
    pass


def require(value, category):
    if not value:
        raise OutputIntentError(category)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def has_missing_output_intents(original, embedded):
    return (original.xref_get_key(original.pdf_catalog(), 'OutputIntents')[0] != 'null'
            and embedded.xref_get_key(embedded.pdf_catalog(), 'OutputIntents')[0] == 'null')


def copy_output_intents(original, embedded, budget=lambda: None):
    """Return temporary bytes and hashes; this alone grants no acceptance.

    This is the same pypdf catalog copy used by the exact six-page cloud probe.
    No callback can replace source bytes, insert page content or select a profile.
    """
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, DictionaryObject, NameObject, NullObject, StreamObject
    require(isinstance(original, bytes) and isinstance(embedded, bytes)
            and 0 < len(original) <= MAX_PDF_BYTES and 0 < len(embedded) <= MAX_PDF_BYTES,
            'output_intent_input_bound')
    logger = logging.getLogger('pypdf')
    previous = logger.disabled, logger.propagate, logger.handlers[:]
    logger.disabled, logger.propagate, logger.handlers = True, False, [logging.NullHandler()]
    try:
        budget()
        source = PdfReader(io.BytesIO(original)); provider = PdfReader(io.BytesIO(embedded))
        for reader in (source, provider):
            # is_encrypted remains true for permission-protected PDFs that
            # open normally without a password. Confirm empty-password access;
            # never request or try a nonempty password, or change source bytes.
            if reader.is_encrypted:
                require(reader.decrypt('') != 0, 'output_intent_password_required')
        source_root = source.trailer['/Root']; provider_root = provider.trailer['/Root']
        provider_intents = provider_root.get('/OutputIntents')
        require('/OutputIntents' in source_root and (provider_intents is None or isinstance(provider_intents, NullObject)),
                'output_intent_missing_required')
        # Optional-content catalog semantics use a separate graph-bound policy.
        # Do not combine two catalog repairs or silently ignore their interaction.
        require(all(root.get('/OCProperties') is None or isinstance(root.get('/OCProperties'), NullObject)
                    for root in (source_root, provider_root)),
                'output_intent_optional_content_unsupported')
        intents = source_root['/OutputIntents']
        require(isinstance(intents, ArrayObject) and 1 <= len(intents) <= MAX_PROFILES,
                'output_intent_array_bound')
        total_profiles = 0; profiles = []
        for item in intents:
            budget(); intent = item.get_object()
            require(isinstance(intent, DictionaryObject) and set(intent) <= {
                '/Type', '/S', '/OutputCondition', '/OutputConditionIdentifier', '/RegistryName', '/Info', '/DestOutputProfile'},
                'output_intent_keys')
            profile = intent.get('/DestOutputProfile')
            profile = profile.get_object() if profile is not None else None
            require(isinstance(profile, StreamObject), 'output_intent_profile_required')
            require(set(profile) <= {'/N', '/Alternate', '/Range', '/Length', '/Filter', '/DecodeParms'},
                    'output_intent_profile_keys')
            profile_bytes = profile.get_data(); total_profiles += len(profile_bytes)
            require(128 <= len(profile_bytes) <= MAX_PROFILE_BYTES and total_profiles <= MAX_TOTAL_PROFILE_BYTES
                    and profile_bytes[36:40] == b'acsp', 'output_intent_profile_bound')
            profiles.append(digest(profile_bytes))
        descriptor = io.BytesIO(); intents.write_to_stream(descriptor)
        writer = PdfWriter(); writer.clone_document_from_reader(provider)
        writer._root_object[NameObject('/OutputIntents')] = source_root.raw_get('/OutputIntents').clone(writer)
        output = io.BytesIO(); writer.write(output); restored = output.getvalue()
        require(0 < len(restored) <= MAX_PDF_BYTES, 'output_intent_output_bound')
        budget()
        return restored, {'original_output_intents_sha256': digest(descriptor.getvalue()),
                          'profile_sha256': profiles, 'profile_bytes': total_profiles}
    finally:
        logger.disabled, logger.propagate, logger.handlers = previous


def restore_missing_output_intents(original, embedded, *, original_sha256, embedded_sha256, budget=lambda: None):
    """Return an owned temporary document plus proof; caller must verify pixels."""
    import fitz
    from mineru_pdf_graph import bind_pdf_render_graph
    require(all(isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value)
                for value in (original_sha256, embedded_sha256)), 'output_intent_source_binding')
    require(digest(original) == original_sha256 and digest(embedded) == embedded_sha256,
            'output_intent_source_binding')
    restored_bytes, configuration = copy_output_intents(original, embedded, budget)
    restored = fitz.open(stream=restored_bytes, filetype='pdf')
    try:
        with fitz.open(stream=original, filetype='pdf') as source:
            binding = bind_pdf_render_graph(source, restored, budget=budget)
        proof = {'schema': 1, 'policy': POLICY, 'original_pdf_sha256': original_sha256,
            'embedded_pdf_sha256': embedded_sha256, 'provider_catalog_was_missing': True,
            'restored_pdf_sha256': digest(restored_bytes), 'restored_pdf_bytes': len(restored_bytes),
            'graph_binding': binding.receipt, 'verified_page_indices': [], **configuration}
        return restored, proof
    except Exception:
        restored.close()
        raise


def validate_restoration_receipt(value, *, original_sha256, embedded_sha256, page_indices):
    from mineru_pdf_graph import validate_graph_receipt
    required = {'schema', 'policy', 'original_pdf_sha256', 'embedded_pdf_sha256', 'provider_catalog_was_missing',
        'restored_pdf_sha256', 'restored_pdf_bytes', 'graph_binding', 'verified_page_indices',
        'original_output_intents_sha256', 'profile_sha256', 'profile_bytes'}
    require(isinstance(value, dict) and set(value) == required, 'output_intent_receipt_keys')
    require(type(value['schema']) is int and value['schema'] == 1 and value['policy'] == POLICY,
            'output_intent_receipt_policy')
    require(value['original_pdf_sha256'] == original_sha256 and value['embedded_pdf_sha256'] == embedded_sha256,
            'output_intent_receipt_binding')
    require(value['provider_catalog_was_missing'] is True, 'output_intent_receipt_missing_required')
    for key in ('original_pdf_sha256', 'embedded_pdf_sha256', 'restored_pdf_sha256', 'original_output_intents_sha256'):
        require(isinstance(value[key], str) and re.fullmatch(r'[0-9a-f]{64}', value[key]), 'output_intent_receipt_hash')
    require(type(value['restored_pdf_bytes']) is int and 0 < value['restored_pdf_bytes'] <= MAX_PDF_BYTES,
            'output_intent_receipt_size')
    profiles = value['profile_sha256']
    require(isinstance(profiles, list) and 1 <= len(profiles) <= MAX_PROFILES
            and all(isinstance(item, str) and re.fullmatch(r'[0-9a-f]{64}', item) for item in profiles),
            'output_intent_receipt_profiles')
    require(type(value['profile_bytes']) is int and 128 * len(profiles) <= value['profile_bytes'] <= MAX_TOTAL_PROFILE_BYTES,
            'output_intent_receipt_size')
    graph = validate_graph_receipt(value['graph_binding'])
    pages = value['verified_page_indices']
    require(isinstance(pages, list) and all(type(index) is int and 0 <= index < graph['pages'] for index in pages)
            and pages == sorted(set(pages)) and pages == page_indices, 'output_intent_receipt_pages')
    return value
