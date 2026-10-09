"""Strict, bounded PDF drawing-graph binding for optional-content repair.

This proves the existing objects correspond; it never changes either document.
Only unparameterized Flate transport encoding is normalized. Image codecs are
never decoded, and no object names, strings, stream data, or xrefs enter receipts.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
import hashlib
import io
import json
import logging
import re
from types import SimpleNamespace
import zlib

MAX_PAGES = 1000
MAX_OBJECTS = 50000
MAX_NODES = 500000
MAX_DEPTH = 128
MAX_HEADER_BYTES = 2 * 1024 * 1024
MAX_STREAM_BYTES = 64 * 1024 * 1024
MAX_TOTAL_BYTES = 256 * 1024 * 1024
MAX_CONTAINER_ITEMS = 20000
MAX_DIAGNOSTIC_KEYS = 64
MAX_DIAGNOSTIC_UNKNOWN_KEYS = 16
MAX_DIAGNOSTIC_NODES = 10000
# Only these literal PDF specification keys can be exposed in diagnostics.
# Resource identifiers and all dictionary values are always hashed.
DIAGNOSTIC_STANDARD_KEYS = frozenset("""
/Type /Subtype /Length /Length1 /Length2 /Length3 /DL /Filter /DecodeParms
/F /FFilter /FDecodeParms /Metadata /PieceInfo /LastModified /StructParent /StructParents
/Width /Height /ColorSpace /CS /BitsPerComponent /Decode /Interpolate /ImageMask
/Mask /SMask /Matte /SMaskInData /Intent /Alternates /OC /OPI
/Predictor /Columns /Colors /EarlyChange /K /EndOfLine /EncodedByteAlign /Rows
/EndOfBlock /BlackIs1 /DamagedRowsBeforeError /ColorTransform /JBIG2Globals
/Resources /Contents /Group /Annots /XObject /ExtGState /Font /Pattern /Shading /Properties /ProcSet
/S /I /N /C /BC /TR /TR2 /G /BBox /Matrix /FormType /Ref
/LW /LC /LJ /ML /D /RI /OP /op /OPM /BG /BG2 /UCR /UCR2 /HT /FL /SM /SA /BM /CA /ca /AIS /TK
/BaseFont /FirstChar /LastChar /Widths /FontDescriptor /Encoding /ToUnicode /DescendantFonts
/CIDSystemInfo /CIDToGIDMap /DW /W /DW2 /W2 /FontFile /FontFile2 /FontFile3
/FontName /FontFamily /FontStretch /FontWeight /Flags /FontBBox /ItalicAngle /Ascent /Descent
/Leading /CapHeight /XHeight /StemV /StemH /AvgWidth /MaxWidth /MissingWidth /CharSet
/FontMatrix /CharProcs /Differences /BaseEncoding /Registry /Ordering /Supplement
/OCGs /VE /P /Name /Usage /CreatorInfo /Creator /View /ViewState /Print /PrintState /Export /ExportState
/OCProperties /Configs /BaseState /ON /OFF /AS /Order /ListMode /RBGroups /Locked
/OutputIntents /DestOutputProfile /OutputCondition /OutputConditionIdentifier /Info
/MediaBox /CropBox /BleedBox /TrimBox /ArtBox /Rotate /UserUnit
/Rect /AP /AS /Border /BS /A /AA /Dest /QuadPoints /Parent /Kids /T /V /DA /DR /AcroForm /NeedsRendering /XFA
/ShadingType /Function /FunctionType /Domain /Range /Coords /Extend /Background /AntiAlias
/Size /BitsPerSample /Encode /Bounds /Functions /C0 /C1 /PatternType /PaintType /TilingType /XStep /YStep
""".split())
_PARSER = SimpleNamespace(strict=True)
_PARSER_LOADED = False


def _load_parser():
    """Receipt validation is standard-library-only on lightweight consumers."""
    global _PARSER_LOADED
    if not _PARSER_LOADED:
        from pypdf import generic
        for name in ("ArrayObject", "BooleanObject", "ByteStringObject", "DictionaryObject", "FloatObject",
                     "IndirectObject", "NameObject", "NullObject", "NumberObject", "TextStringObject", "read_object"):
            globals()[name] = getattr(generic, name)
        _PARSER_LOADED = True


class PdfGraphError(ValueError):
    """A fixed, non-private rejection category."""
    def __init__(self, category):
        self.category = category
        self.path_sha256 = None
        self.sanitized_details = None
        super().__init__(category)


def _require(condition, category):
    if not condition:
        raise PdfGraphError(category)


def parse_pdf_value(header):
    """Parse a PyMuPDF normalized object header without resolving references."""
    _load_parser()
    if isinstance(header, str):
        header = header.encode("utf-8")
    _require(isinstance(header, bytes) and 0 < len(header) <= MAX_HEADER_BYTES,
             "pdf_graph_header_bound")
    # Parser diagnostics can quote original object strings. Suppress these and
    # replace exceptions with a fixed category, including malformed input.
    logger = logging.getLogger("pypdf")
    previous = logger.disabled, logger.propagate, logger.handlers[:]
    logger.disabled, logger.propagate, logger.handlers = True, False, [logging.NullHandler()]
    try:
        stream = io.BytesIO(header)
        result = read_object(stream, _PARSER)
        _require(not stream.read().strip(), "pdf_graph_parse_trailing_data")
        return result
    except PdfGraphError:
        raise
    except Exception:
        raise PdfGraphError("pdf_graph_parse_failed") from None
    finally:
        logger.disabled, logger.propagate, logger.handlers = previous


def _raw(dictionary, key):
    return dictionary.raw_get(key) if key in dictionary else NullObject()


def _is_null(value):
    return isinstance(value, NullObject)


def _reference(value):
    _require(isinstance(value, IndirectObject), "pdf_graph_reference_required")
    # PyMuPDF's xref accessor takes only the object number. Until a generation
    # aware accessor is used, accepting nonzero generations would be guessing.
    _require(value.generation == 0 and value.idnum > 0, "pdf_graph_reference_generation")
    return value.idnum, value.generation


def _value_kind(value):
    for kind, classes in (("dictionary", (DictionaryObject, dict)), ("array", (ArrayObject,)),
                          ("reference", (IndirectObject,)), ("boolean", (BooleanObject,)),
                          ("null", (NullObject,)), ("number", (NumberObject, FloatObject)),
                          ("name", (NameObject,)), ("string", (TextStringObject,)),
                          ("bytes", (ByteStringObject,))):
        if isinstance(value, classes):
            return kind
    return "unsupported"


def _key_hash(key):
    return hashlib.sha256(str(key).encode("utf-8")).hexdigest()


def _value_summary(value):
    """Summarize typed values without resolving references or exposing strings."""
    kind = _value_kind(value)
    result = {"type": kind, "empty": kind == "null" or (
        kind in {"dictionary", "array", "name", "string", "bytes"} and len(value) == 0)}
    hasher = hashlib.sha256()
    nodes, size = 0, 0

    def visit(item, depth=0):
        nonlocal nodes, size
        nodes += 1
        if nodes > MAX_DIAGNOSTIC_NODES or depth > MAX_DEPTH:
            raise ValueError
        item_kind = _value_kind(item)
        payload = item_kind.encode("ascii")
        if item_kind in {"name", "string", "number"}:
            payload += str(item).encode("utf-8")
        elif item_kind == "bytes":
            payload += bytes(item)
        elif item_kind == "boolean":
            payload += b"true" if item.value else b"false"
        # Normalize xref numbers: this describes value shape, not an additional
        # graph-binding proof. Indirect target content is checked by the binder.
        size += len(payload)
        if size > MAX_HEADER_BYTES:
            raise ValueError
        hasher.update(len(payload).to_bytes(8, "big")); hasher.update(payload)
        if item_kind == "dictionary":
            for key in sorted(item, key=str):
                raw_key = str(key).encode("utf-8")
                size += len(raw_key)
                if size > MAX_HEADER_BYTES:
                    raise ValueError
                hasher.update(len(raw_key).to_bytes(8, "big")); hasher.update(raw_key)
                visit(item.raw_get(key) if isinstance(item, DictionaryObject) else item[key], depth + 1)
        elif item_kind == "array":
            for member in item:
                visit(member, depth + 1)
    try:
        visit(value)
        result.update(sha256=hasher.hexdigest(), hash_status="complete")
    except Exception:
        result.update(sha256=None, hash_status="bounded")
    if kind == "dictionary":
        keys = {str(key) for key in value}
        unknown = sorted(_key_hash(key) for key in keys - DIAGNOSTIC_STANDARD_KEYS)
        result.update(key_count=len(keys), known_keys=sorted(keys & DIAGNOSTIC_STANDARD_KEYS),
                      unknown_key_count=len(unknown), unknown_key_sha256=unknown[:MAX_DIAGNOSTIC_UNKNOWN_KEYS],
                      unknown_keys_truncated=len(unknown) > MAX_DIAGNOSTIC_UNKNOWN_KEYS)
    return result


def _sanitized_details(a, b, path, path_sha256):
    """Expose standard key names only; private path components stay hashed."""
    standard_path_keys = [part for part in path if isinstance(part, str) and part in DIAGNOSTIC_STANDARD_KEYS]
    result = {"schema": 1, "path_sha256": path_sha256,
              "scope": "page" if path and path[0] == "page" else "catalog" if path and path[0] == "catalog" else "graph",
              "last_standard_key": standard_path_keys[-1] if standard_path_keys else None,
              "original": _value_summary(a), "embedded": _value_summary(b)}
    if len(path) >= 2 and path[0] == "page" and type(path[1]) is int:
        result["page_index"] = path[1]
    if isinstance(a, (DictionaryObject, dict)) and isinstance(b, (DictionaryObject, dict)):
        original_only = set(a) - set(b)
        embedded_only = set(b) - set(a)
        def keys(values):
            known = sorted(str(key) for key in values if str(key) in DIAGNOSTIC_STANDARD_KEYS)
            unknown = sorted(_key_hash(key) for key in values if str(key) not in DIAGNOSTIC_STANDARD_KEYS)
            return {"known": known, "unknown_count": len(unknown),
                    "unknown_sha256": unknown[:MAX_DIAGNOSTIC_UNKNOWN_KEYS],
                    "unknown_truncated": len(unknown) > MAX_DIAGNOSTIC_UNKNOWN_KEYS}
        changed = sorted(original_only | embedded_only,
                         key=lambda key: (str(key) not in DIAGNOSTIC_STANDARD_KEYS, str(key)))
        values = []
        for key in changed[:MAX_DIAGNOSTIC_KEYS]:
            row = {"key": str(key)} if str(key) in DIAGNOSTIC_STANDARD_KEYS else {"key_sha256": _key_hash(key)}
            for label, value in (("original", a), ("embedded", b)):
                row[label] = _value_summary(value.raw_get(key) if isinstance(value, DictionaryObject) else value[key]) \
                    if key in value else {"type": "missing", "empty": True, "sha256": None, "hash_status": "missing"}
            values.append(row)
        result["dictionary_difference"] = {"original_only": keys(original_only), "embedded_only": keys(embedded_only),
                                           "values": values, "values_truncated": len(changed) > MAX_DIAGNOSTIC_KEYS}
    return result


@dataclass(frozen=True)
class GraphBinding:
    mapping: dict[tuple[int, int], tuple[int, int]]
    ocg_mapping: dict[tuple[int, int], tuple[int, int]]
    receipt: dict


def validate_graph_receipt(value):
    keys = {"schema", "policy", "sha256", "pages", "objects", "streams", "nodes",
            "mapped_references", "ocg_count", "original_inspected_bytes", "embedded_inspected_bytes"}
    _require(isinstance(value, dict) and set(value) == keys, "pdf_graph_receipt_invalid")
    _require(type(value["schema"]) is int and value["schema"] == 1
             and value["policy"] == "mineru-render-object-graph-v1"
             and isinstance(value["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", value["sha256"]),
             "pdf_graph_receipt_invalid")
    bounds = {"pages": (1, MAX_PAGES), "objects": (0, MAX_OBJECTS), "streams": (0, MAX_OBJECTS),
              "nodes": (1, MAX_NODES), "mapped_references": (1, MAX_OBJECTS), "ocg_count": (0, MAX_OBJECTS),
              "original_inspected_bytes": (1, MAX_TOTAL_BYTES), "embedded_inspected_bytes": (1, MAX_TOTAL_BYTES)}
    for key, (low, high) in bounds.items():
        _require(type(value[key]) is int and low <= value[key] <= high, "pdf_graph_receipt_invalid")
    _require(value["streams"] <= value["objects"]
             and value["ocg_count"] <= value["objects"]
             and value["mapped_references"] == value["pages"] + value["objects"],
             "pdf_graph_receipt_invalid")
    return dict(value)


class _Document:
    def __init__(self, document, budget):
        self.document, self.budget = document, budget
        self.headers, self.streams = {}, {}
        self.bytes = 0
        _require(not document.is_encrypted and 0 < len(document) <= MAX_PAGES,
                 "pdf_graph_document_bound")
        _require(0 < document.xref_length() <= MAX_OBJECTS, "pdf_graph_object_bound")

    def charge(self, size):
        self.bytes += size
        _require(self.bytes <= MAX_TOTAL_BYTES, "pdf_graph_total_bytes_bound")

    def header(self, reference):
        self.budget()
        number, generation = reference
        _require(generation == 0 and 0 < number < self.document.xref_length(),
                 "pdf_graph_reference_invalid")
        if reference not in self.headers:
            try:
                raw = self.document.xref_object(number, compressed=True)
            except Exception:
                raise PdfGraphError("pdf_graph_object_unavailable") from None
            self.charge(len(raw.encode("utf-8")))
            self.headers[reference] = parse_pdf_value(raw)
        return self.headers[reference]

    def dictionary(self, reference):
        result = self.header(reference)
        _require(isinstance(result, DictionaryObject), "pdf_graph_dictionary_required")
        return result

    def resolve(self, value):
        return self.header(_reference(value)) if isinstance(value, IndirectObject) else value

    def page_references(self):
        catalog = self.dictionary((self.document.pdf_catalog(), 0))
        root = _reference(_raw(catalog, "/Pages"))
        result, seen = [], set()

        def walk(reference, depth):
            _require(depth <= MAX_DEPTH and reference not in seen, "pdf_graph_page_tree_invalid")
            seen.add(reference)
            obj = self.dictionary(reference)
            kind = _raw(obj, "/Type")
            if kind == "/Page":
                result.append(reference)
                _require(len(result) <= MAX_PAGES, "pdf_graph_page_count_bound")
                return
            _require(kind == "/Pages", "pdf_graph_page_tree_invalid")
            children = self.resolve(_raw(obj, "/Kids"))
            _require(isinstance(children, ArrayObject) and len(children) <= MAX_PAGES,
                     "pdf_graph_page_tree_invalid")
            for child in children:
                walk(_reference(child), depth + 1)

        walk(root, 0)
        _require([ref[0] for ref in result] == [self.document.page_xref(i) for i in range(len(self.document))],
                 "pdf_graph_page_tree_mismatch")
        return result

    def inherited(self, reference, key):
        seen = set()
        while True:
            _require(reference not in seen and len(seen) <= MAX_DEPTH, "pdf_graph_inheritance_cycle")
            seen.add(reference)
            obj = self.dictionary(reference)
            value = _raw(obj, key)
            if not _is_null(value):
                return value
            parent = _raw(obj, "/Parent")
            if _is_null(parent):
                return NullObject()
            reference = _reference(parent)

    def stream(self, reference):
        if reference in self.streams:
            return self.streams[reference]
        number, _ = reference
        if not self.document.xref_is_stream(number):
            result = None
        else:
            try:
                raw = self.document.xref_stream_raw(number)
            except Exception:
                raise PdfGraphError("pdf_graph_stream_unavailable") from None
            _require(isinstance(raw, bytes) and len(raw) <= MAX_STREAM_BYTES,
                     "pdf_graph_stream_bytes_bound")
            self.charge(len(raw))
            header = self.dictionary(reference)
            result_header = {str(key): value for key, value in header.items() if key != "/Length"}
            filter_value = self.resolve(_raw(header, "/Filter"))
            if isinstance(filter_value, ArrayObject) and len(filter_value) == 1:
                filter_value = self.resolve(filter_value[0])
            parameters = self.resolve(_raw(header, "/DecodeParms"))
            if isinstance(parameters, ArrayObject) and len(parameters) == 1:
                parameters = self.resolve(parameters[0])
            # An empty parameter dictionary supplies no parameters. PyMuPDF
            # writes this on unfiltered PNG pixels; PDFium omits it when adding
            # Flate transport. Nonempty dictionaries remain strictly compared.
            if isinstance(parameters, DictionaryObject) and not parameters:
                parameters = NullObject()
            if filter_value in ("/FlateDecode", "/Fl") and _is_null(parameters):
                try:
                    decoder = zlib.decompressobj()
                    decoded = decoder.decompress(raw, MAX_STREAM_BYTES + 1)
                    _require(len(decoded) <= MAX_STREAM_BYTES and not decoder.unconsumed_tail,
                             "pdf_graph_stream_bytes_bound")
                    _require(decoder.eof and not decoder.unused_data, "pdf_graph_flate_invalid")
                except PdfGraphError:
                    raise
                except Exception:
                    raise PdfGraphError("pdf_graph_flate_invalid") from None
                self.charge(len(decoded))
                raw = decoded
                result_header.pop("/Filter", None)
                result_header.pop("/DecodeParms", None)
            elif _is_null(filter_value):
                result_header.pop("/Filter", None)
                if _is_null(parameters):
                    result_header.pop("/DecodeParms", None)
            # DCT/JPX/etc retain exact encoded bytes and every codec parameter.
            # No xref_stream() / Pixmap() call is used here.
            result = result_header, len(raw), hashlib.sha256(raw).hexdigest()
        self.streams[reference] = result
        return result

    def ocg_inventory(self):
        result = set()
        for number in range(1, self.document.xref_length()):
            self.budget()
            try:
                kind, value = self.document.xref_get_key(number, "Type")
            except Exception:
                raise PdfGraphError("pdf_graph_inventory_unavailable") from None
            if kind == "name" and value == "/OCG":
                result.add(number)
        return result


def bind_pdf_render_graph(original_doc, embedded_doc, *, budget=lambda: None):
    """Bind all pages and reachable drawing objects, including hidden objects.

    Caller owns the open PyMuPDF documents. The returned mapping includes only
    proved object correspondences, with explicit generation numbers. A repeated
    original reference must target the same embedded reference and vice versa.
    """
    _load_parser()
    left, right = _Document(original_doc, budget), _Document(embedded_doc, budget)
    left_pages, right_pages = left.page_references(), right.page_references()
    _require(len(left_pages) == len(right_pages), "pdf_graph_page_count_mismatch")
    mapping, reverse, ordinals, ocgs, visited, compared_pairs = {}, {}, {}, {}, set(), set()
    fingerprint = hashlib.sha256()
    counts = {"pages": len(left_pages), "objects": 0, "streams": 0, "nodes": 0}

    def note(tag, value):
        encoded = json.dumps([tag, value], ensure_ascii=True, separators=(",", ":")).encode("ascii")
        fingerprint.update(len(encoded).to_bytes(8, "big")); fingerprint.update(encoded)

    def bind(a, b):
        _require(a not in mapping or mapping[a] == b, "pdf_graph_alias_mismatch")
        _require(b not in reverse or reverse[b] == a, "pdf_graph_alias_mismatch")
        if a not in mapping:
            ordinals[a] = len(mapping)
            mapping[a], reverse[b] = b, a
        return a, b

    # Annotation /P links back to an already paired page, not its full Pages
    # parent tree. Every page's drawing roots are checked separately below.
    for a, b in zip(left_pages, right_pages):
        bind(a, b); visited.add((a, b, False)); compared_pairs.add((a, b))

    def annotation_root(path):
        return (len(path) == 5 and path[0] == "page" and type(path[1]) is int
                and path[2:4] == ("/Annots", "index") and type(path[4]) is int)

    def checked_link_destination(document, page_references, value):
        """Validate navigation syntax only; it is not a drawing dependency."""
        def resolved(item):
            seen = set()
            while isinstance(item, IndirectObject):
                reference = _reference(item)
                _require(reference not in seen and len(seen) < MAX_DEPTH,
                         "pdf_graph_link_destination_invalid")
                seen.add(reference); item = document.header(reference)
            return item
        value = resolved(value)
        if isinstance(value, (NameObject, TextStringObject, ByteStringObject)):
            _require(0 < len(value) <= MAX_HEADER_BYTES, "pdf_graph_link_destination_invalid")
            return
        _require(isinstance(value, ArrayObject) and 2 <= len(value) <= 6,
                 "pdf_graph_link_destination_invalid")
        _require(isinstance(value[0], IndirectObject) and _reference(value[0]) in page_references,
                 "pdf_graph_link_destination_invalid")
        mode = resolved(value[1])
        arities = {"/XYZ": 5, "/Fit": 2, "/FitH": 3, "/FitV": 3, "/FitR": 6,
                   "/FitB": 2, "/FitBH": 3, "/FitBV": 3}
        _require(isinstance(mode, NameObject) and str(mode) in arities and len(value) == arities[str(mode)],
                 "pdf_graph_link_destination_invalid")
        numbers = [resolved(item) for item in value[2:]]
        for item in numbers:
            _require(isinstance(item, (NumberObject, FloatObject)) and Decimal(str(item)).is_finite()
                     or isinstance(item, NullObject) and mode != "/FitR",
                     "pdf_graph_link_destination_invalid")
        if mode == "/XYZ" and not isinstance(numbers[2], NullObject):
            _require(Decimal(str(numbers[2])) >= 0, "pdf_graph_link_destination_invalid")

    def drawing_annotation(a, b, path):
        if not annotation_root(path):
            return a, b
        def raw(item, key):
            return item.raw_get(key) if isinstance(item, DictionaryObject) and key in item else item.get(key, NullObject())
        if not all(raw(item, "/Subtype") == "/Link" and
                   (isinstance(raw(item, "/Type"), NullObject) or raw(item, "/Type") == "/Annot")
                   for item in (a, b)):
            return a, b
        for item, document, pages in ((a, left, left_pages), (b, right, right_pages)):
            if "/Dest" in item:
                _require(isinstance(raw(item, "/A"), NullObject), "pdf_graph_link_destination_invalid")
                checked_link_destination(document, pages, raw(item, "/Dest"))
        # /Dest controls interactive navigation, not Link appearance. PDFium
        # removes forward-page destinations during import (CPDF_PageOrganizer
        # UpdateReference/GetNewObjId). This exception applies only to a page's
        # actual annotation entry: every AP/OC/Border/Rect and nested dictionary
        # remains subject to the full typed graph comparison.
        # https://pdfium.googlesource.com/pdfium/+/refs/heads/main/core/fpdfapi/edit/cpdf_pageorganizer.cpp
        return ({key: raw(a, key) for key in a if key != "/Dest"},
                {key: raw(b, key) for key in b if key != "/Dest"})

    def compare(a, b, depth=0, path=()):
        try:
            return compare_value(a, b, depth, path)
        except PdfGraphError as error:
            if error.path_sha256 is None:
                error.path_sha256 = hashlib.sha256(json.dumps(path, ensure_ascii=True,
                    separators=(",", ":")).encode("ascii")).hexdigest()
            if error.sanitized_details is None:
                try:
                    error.sanitized_details = _sanitized_details(a, b, path, error.path_sha256)
                except Exception:
                    # Diagnostics never replace the original rejection or
                    # report parser exceptions containing source material.
                    error.sanitized_details = {"schema": 1, "path_sha256": error.path_sha256,
                                               "status": "unavailable"}
            raise

    def compare_value(a, b, depth, path):
        budget()
        counts["nodes"] += 1
        _require(depth <= MAX_DEPTH and counts["nodes"] <= MAX_NODES, "pdf_graph_traversal_bound")
        if isinstance(a, IndirectObject) or isinstance(b, IndirectObject):
            _require(isinstance(a, IndirectObject) and isinstance(b, IndirectObject),
                     "pdf_graph_reference_shape_mismatch")
            ar, br = _reference(a), _reference(b)
            pair = bind(ar, br)
            scoped_pair = (*pair, annotation_root(path))
            # Stable traversal ordinal preserves alias topology without xrefs.
            note("reference", ordinals[ar])
            if scoped_pair in visited:
                return
            visited.add(scoped_pair)
            if pair not in compared_pairs:
                compared_pairs.add(pair); counts["objects"] += 1
            ah, bh = left.header(ar), right.header(br)
            ast, bst = left.stream(ar), right.stream(br)
            _require((ast is None) == (bst is None), "pdf_graph_stream_kind_mismatch")
            if ast is not None:
                _require(ast[1:] == bst[1:], "pdf_graph_stream_content_mismatch")
                counts["streams"] += 1; note("stream", ast[1:])
                compare(ast[0], bst[0], depth + 1, path)
            else:
                compare(ah, bh, depth + 1, path)
            if isinstance(ah, DictionaryObject) and _raw(ah, "/Type") == "/OCG":
                _require(isinstance(bh, DictionaryObject) and _raw(bh, "/Type") == "/OCG",
                         "pdf_graph_ocg_kind_mismatch")
                ocgs[ar] = br
            return
        if isinstance(a, (DictionaryObject, dict)) or isinstance(b, (DictionaryObject, dict)):
            _require(isinstance(a, (DictionaryObject, dict)) and isinstance(b, (DictionaryObject, dict)),
                     "pdf_graph_value_type_mismatch")
            _require(len(a) <= MAX_CONTAINER_ITEMS and len(b) <= MAX_CONTAINER_ITEMS,
                     "pdf_graph_container_bound")
            a, b = drawing_annotation(a, b, path)
            _require(set(a) == set(b), "pdf_graph_dictionary_keys_mismatch")
            note("dictionary", sorted(str(key) for key in a))
            for key in sorted(a, key=str):
                compare(a.raw_get(key) if isinstance(a, DictionaryObject) else a[key],
                        b.raw_get(key) if isinstance(b, DictionaryObject) else b[key], depth + 1,
                        path + ("key", str(key)))
            return
        if isinstance(a, ArrayObject) or isinstance(b, ArrayObject):
            _require(isinstance(a, ArrayObject) and isinstance(b, ArrayObject), "pdf_graph_value_type_mismatch")
            _require(len(a) == len(b), "pdf_graph_array_length_mismatch")
            _require(len(a) <= MAX_CONTAINER_ITEMS, "pdf_graph_container_bound")
            note("array", len(a))
            for index, (av, bv) in enumerate(zip(a, b)):
                compare(av, bv, depth + 1, path + ("index", index))
            return
        if isinstance(a, (NumberObject, FloatObject)) or isinstance(b, (NumberObject, FloatObject)):
            _require(isinstance(a, (NumberObject, FloatObject)) and isinstance(b, (NumberObject, FloatObject)),
                     "pdf_graph_value_type_mismatch")
            av, bv = Decimal(str(a)), Decimal(str(b))
            _require(av.is_finite() and bv.is_finite() and av == bv, "pdf_graph_scalar_mismatch")
            note("number", str(av.normalize())); return
        _require(type(a) is type(b), "pdf_graph_value_type_mismatch")
        if isinstance(a, NullObject):
            note("null", None); return
        if isinstance(a, BooleanObject):
            _require(a.value == b.value, "pdf_graph_scalar_mismatch")
            note("boolean", a.value); return
        if isinstance(a, ByteStringObject):
            _require(bytes(a) == bytes(b), "pdf_graph_scalar_mismatch")
            note("bytes", [len(a), hashlib.sha256(a).hexdigest()]); return
        if isinstance(a, (NameObject, TextStringObject)):
            _require(str(a) == str(b), "pdf_graph_scalar_mismatch")
            note(type(a).__name__, str(a)); return
        raise PdfGraphError("pdf_graph_value_unsupported")

    inherited = ("/Resources",)
    direct = ("/Contents", "/Group", "/Annots")
    for index, (ar, br) in enumerate(zip(left_pages, right_pages)):
        note("page", index)
        ah, bh = left.dictionary(ar), right.dictionary(br)
        def geometry(page):
            return {"rect": list(page.rect), "cropbox": list(page.cropbox), "mediabox": list(page.mediabox),
                    "bleedbox": list(page.bleedbox), "trimbox": list(page.trimbox), "artbox": list(page.artbox),
                    "rotation": page.rotation}
        ag, bg = geometry(original_doc[index]), geometry(embedded_doc[index])
        _require(ag == bg, "pdf_graph_page_geometry_mismatch")
        note("geometry", ag)
        for key in inherited + direct:
            av = left.inherited(ar, key) if key in inherited else _raw(ah, key)
            bv = right.inherited(br, key) if key in inherited else _raw(bh, key)
            note("root", key); compare(av, bv, path=("page", index, key))
    ac = left.dictionary((original_doc.pdf_catalog(), 0))
    bc = right.dictionary((embedded_doc.pdf_catalog(), 0))
    for key in ("/AcroForm", "/NeedsRendering", "/XFA"):
        _require(_is_null(_raw(ac, key)) and _is_null(_raw(bc, key)), "pdf_graph_dynamic_document_unsupported")
    note("catalog", "/OutputIntents"); compare(_raw(ac, "/OutputIntents"), _raw(bc, "/OutputIntents"),
                                              path=("catalog", "/OutputIntents"))
    _require({ref[0] for ref in ocgs} == left.ocg_inventory()
             and {ref[0] for ref in ocgs.values()} == right.ocg_inventory(),
             "pdf_graph_ocg_inventory_mismatch")
    receipt = {"schema": 1, "policy": "mineru-render-object-graph-v1", "sha256": fingerprint.hexdigest(),
               **counts, "mapped_references": len(mapping), "ocg_count": len(ocgs),
               "original_inspected_bytes": left.bytes, "embedded_inspected_bytes": right.bytes}
    return GraphBinding(dict(mapping), dict(ocgs), validate_graph_receipt(receipt))
