"""Frozen quantity grammar for already authenticated active reading pages.

This contract cannot approve a new candidate. Publication independently proves
byte-identical approved HTML and unchanged source content before carrying it.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import approved_financial_quantity_v1 as parser
from portal_extended_locales import ExpansionError

CONTRACT_ID = 'approved-financial-quantities-pre204-v1'
PARSER_SHA256 = 'ff7790f5535378c6e3ca0d9ba3bb1f31a4e581704c38e840e6c1db8e64b682be'
PARSER_SOURCE_COMMIT = 'ae18c2b83bda8cd526116a888df6885c6add3a9f'

if hashlib.sha256(Path(parser.__file__).read_bytes()).hexdigest() != PARSER_SHA256:
    raise ExpansionError('Frozen approved quantity parser bytes changed')


def quantity_issues(source, translated, source_language='', target_language=''):
    return parser.quantity_issues(source, translated, source_language, target_language)


def bindings(batches):
    return {(row['generation'], locale, candidate) for row in batches for locale, candidate in row['candidates'].items()}
