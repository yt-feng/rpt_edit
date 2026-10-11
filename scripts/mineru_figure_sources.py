#!/usr/bin/env python3
"""Source-bound MinerU visual selection and lossless original-page crops.

The private sidecar is evidence, not an original-PDF authentication mechanism.
Consumers must obtain expected source/Markdown hashes from the trusted producer
and its immutable outer receipt.  A carried PNG proves crop replay only; it does
not independently establish that the producer rendered the admitted PDF.
"""
from __future__ import annotations

import hashlib
import html
import io
import json
import math
import re
import struct
from contextlib import ExitStack, contextmanager
from pathlib import Path, PurePosixPath
from typing import Any

POLICY = "mineru-source-figures-v1"
RESTORED_POLICY = "mineru-source-figures-v2"
SIDECAR = "source_figure_map.json"
MAX_JSON = 32 * 1024 * 1024
MAX_ITEMS = 20000
MAX_PAGES = 1000
MAX_VISUALS = 1000
MAX_IMAGE_BYTES = 64 * 1024 * 1024
MAX_PIXELS = 80_000_000
MAX_DIMENSION = 20000
MAX_TEXT = 100000
# Carriers are streamed to disk and replayed one page at a time. This aggregate
# bounds a long report's work without treating 31 ordinary 300-dpi pages as a
# source mismatch. Per-page dimensions/pixels remain independently bounded.
MAX_CARRIED_PAGE_PIXELS = 1_000_000_000
MAX_PROVIDER_BYTES = 512 * 1024 * 1024
MARGIN_PIXELS = 3
KINDS = {"table", "chart", "image"}
ERRORS = {"figure_metadata_invalid", "figure_metadata_ambiguous",
          "figure_source_binding_mismatch", "figure_source_pixels_mismatch",
          "figure_asset_mismatch", "figure_proof_invalid", "figure_page_budget_exceeded",
          "figure_render_cache_isolation_failed"}


class FigureSourceError(ValueError):
    def __init__(self, category: str):
        self.category = category if category in ERRORS else "figure_proof_invalid"
        super().__init__(self.category)


def _fail(category="figure_metadata_invalid"):
    raise FigureSourceError(category)


def _sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _hash(value: Any, *, optional=False) -> str | None:
    if optional and value is None:
        return None
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        _fail("figure_source_binding_mismatch")
    return value


def _canonical(value) -> bytes:
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False).encode("utf-8")
    except (ValueError, TypeError):
        _fail()


def _keys(value, keys):
    if not isinstance(value, dict) or set(value) != set(keys):
        _fail("figure_proof_invalid")


def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            _fail()
        result[key] = value
    return result


def _json(data: bytes):
    if len(data) > MAX_JSON:
        _fail()
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=_pairs,
                          parse_constant=lambda _: _fail())
    except FigureSourceError:
        raise
    except (ValueError, UnicodeError, RecursionError):
        _fail()


def _int(value, low, high):
    if type(value) is not int or not low <= value <= high:
        _fail()
    return value


def _text(value):
    if not isinstance(value, str) or len(value) > MAX_TEXT or "\x00" in value:
        _fail()
    return value


def _bbox(value, width, height):
    if not isinstance(value, list) or len(value) != 4:
        _fail()
    if any(type(v) not in (int, float) or not math.isfinite(v) for v in value):
        _fail()
    x0, y0, x1, y1 = value
    if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
        _fail()
    return [float(v) for v in value]


def _relative(value):
    if not isinstance(value, str) or not value or len(value) > 512 or "\\" in value:
        _fail()
    p = PurePosixPath(value)
    if p.is_absolute() or any(q in ("", ".", "..") for q in value.split("/")):
        _fail()
    return value


def _regular(path: Path, root: Path, maximum=MAX_IMAGE_BYTES) -> bytes:
    try:
        path.relative_to(root)
        if any(p.is_symlink() for p in (path, *path.parents) if p == root or root in p.parents):
            _fail("figure_asset_mismatch")
        if not path.is_file() or path.stat().st_size > maximum:
            _fail("figure_asset_mismatch")
        return path.read_bytes()
    except FigureSourceError:
        raise
    except (OSError, ValueError):
        _fail("figure_asset_mismatch")


def _png_size(data):
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        _fail("figure_asset_mismatch")
    return struct.unpack(">II", data[16:24])


def _image(data, *, png=False):
    if len(data) > MAX_IMAGE_BYTES:
        _fail("figure_asset_mismatch")
    if png:
        width, height = _png_size(data)
        if not (1 <= width <= MAX_DIMENSION and 1 <= height <= MAX_DIMENSION and width * height <= MAX_PIXELS):
            _fail("figure_asset_mismatch")
    try:
        from PIL import Image

        with Image.open(io.BytesIO(data)) as im:
            if not (1 <= im.width <= MAX_DIMENSION and 1 <= im.height <= MAX_DIMENSION and im.width * im.height <= MAX_PIXELS):
                _fail("figure_asset_mismatch")
            if png and (im.format != "PNG" or im.mode != "RGB"):
                _fail("figure_asset_mismatch")
            im.load()
            return im.convert("RGB")
    except FigureSourceError:
        raise
    except Exception:
        _fail("figure_asset_mismatch")


def _rgb_hash(image):
    return _sha(image.tobytes())


def _plain(value):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]{0,4096}>", " ", value))).strip()


def _block_text(block):
    lines = block.get("lines", [])
    if not isinstance(lines, list) or len(lines) > 2000:
        _fail()
    result = []
    for line in lines:
        if (not isinstance(line, dict) or not isinstance(line.get("spans", []), list)
                or len(line.get("spans", [])) > 2000
                or any(not isinstance(s, dict) or not isinstance(s.get("type"), str) for s in line.get("spans", []))):
            _fail()
        result.append(" ".join(_text(s.get("content", "")) for s in line.get("spans", [])
                               if s.get("type") == "text"))
    return _text("\n".join(result))


def _table_html_matches(content_html, middle_html):
    """Allow only MinerU's exact equation and image-path serialization.

    The hybrid content list emits `` $...$ `` where middle JSON retains
    ``<eq>...</eq>`` and prefixes ``images/`` on its bare hashed JPEG img src.
    Every formula character, image basename, table cell and other HTML byte
    must remain identical. Unbalanced or nested equation wrappers reject;
    this does not parse, clean or otherwise normalise arbitrary HTML.
    """
    if content_html == middle_html:
        return True
    parts = middle_html.split("<eq>")
    if "</eq>" in parts[0]:
        return False
    converted = [parts[0]]
    for part in parts[1:]:
        equation, closing, tail = part.partition("</eq>")
        if not closing or "</eq>" in tail:
            return False
        converted.extend((" $", equation, "$ ", tail))
    equation_html = "".join(converted)
    if content_html == equation_html:
        return True
    image_html = re.sub(r'<img src="([0-9a-f]{64}\.jpg)"/>',
                        r'<img src="images/\1"/>', equation_html)
    return content_html == image_html


def _metadata_files(root):
    contents, middles = [], []
    paths = list(root.rglob("*"))
    if len(paths) > 50000 or root.is_symlink() or any(p.is_symlink() for p in paths):
        _fail()
    for path in paths:
        if not path.is_file() or path.suffix.lower() != ".json":
            continue
        named_content = path.name == "content_list.json" or path.name.endswith("_content_list.json")
        named_middle = path.name == "middle.json" or path.name.endswith("_middle.json")
        value = _json(_regular(path, root, MAX_JSON))
        is_content = isinstance(value, list) and bool(value) and isinstance(value[0], dict) and "page_idx" in value[0] and "type" in value[0]
        if named_content or is_content:
            contents.append((path, value))
        if named_middle or isinstance(value, dict) and "pdf_info" in value:
            middles.append((path, value))
    if not contents and not middles:
        return None
    if len(contents) != 1 or len(middles) != 1:
        _fail("figure_metadata_ambiguous")
    return contents[0], middles[0], paths


def _normalise(content, middle):
    """Project only the typed fields actually used in deterministic selection."""
    if not isinstance(content, list) or len(content) > MAX_ITEMS or not isinstance(middle, dict):
        _fail()
    profile = {k: middle.get(k) for k in ("_backend", "_version_name", "_ocr_enable", "_effort")}
    if (profile["_backend"] != "hybrid" or profile["_version_name"] != "3.4.4"
            or type(profile["_ocr_enable"]) is not bool or profile["_effort"] != "medium"):
        _fail()
    pdf_info = middle.get("pdf_info")
    if not isinstance(pdf_info, list) or not 1 <= len(pdf_info) <= MAX_PAGES:
        _fail()
    pages, parents = [], []
    for ordinal, page in enumerate(pdf_info):
        if not isinstance(page, dict) or _int(page.get("page_idx"), 0, MAX_PAGES - 1) != ordinal:
            _fail()
        size = page.get("page_size")
        if not isinstance(size, list) or len(size) != 2:
            _fail()
        w, h = [_int(v, 1, 10000) for v in size]
        blocks = page.get("para_blocks")
        if not isinstance(blocks, list) or len(blocks) > MAX_ITEMS:
            _fail()
        text_blocks = []
        for bi, block in enumerate(blocks):
            if not isinstance(block, dict):
                _fail()
            kind = block.get("type")
            if kind in ("text", "title"):
                text_blocks.append({"index": bi, "kind": kind,
                                    "level": _int(block.get("level", 0), 0, 10),
                                    "bbox": _bbox(block.get("bbox"), w, h),
                                    "text": _block_text(block)})
            if kind not in KINDS:
                continue
            body = _bbox(block.get("bbox"), w, h)
            children = block.get("blocks")
            if not isinstance(children, list) or len(children) > 1000:
                _fail()
            refs, bodies, captions, notes = [], [], [], []
            for child in children:
                if not isinstance(child, dict) or child.get("type") not in {kind + "_body", kind + "_caption", kind + "_footnote"}:
                    _fail()
                box = _bbox(child.get("bbox"), w, h)
                if child["type"] == kind + "_body":
                    bodies.append(box)
                    for line in child.get("lines", []):
                        if not isinstance(line, dict) or not isinstance(line.get("spans", []), list):
                            _fail()
                        for span in line.get("spans", []):
                            if not isinstance(span, dict):
                                _fail()
                            if span.get("image_path"):
                                refs.append({"ref": "images/" + _relative(span["image_path"]),
                                             "html": _text(span.get("html", "")),
                                             "bbox": _bbox(span.get("bbox"), w, h)})
                else:
                    target = captions if child["type"].endswith("_caption") else notes
                    target.append({"bbox": box, "text": _block_text(child)})
            if len(bodies) != 1 or len(refs) > 1 or bodies[0] != body:
                _fail()
            if refs and refs[0]["bbox"] != body:
                _fail()
            parents.append({"page_idx": ordinal, "block_index": bi, "kind": kind,
                            "body_bbox": body, "refs": refs, "captions": captions, "footnotes": notes})
        pages.append({"page_idx": ordinal, "provider_size": size, "text_blocks": text_blocks})
    records, used = [], set()
    for index, item in enumerate(content):
        if not isinstance(item, dict) or not isinstance(item.get("type"), str):
            _fail()
        pi = _int(item.get("page_idx"), 0, len(pages) - 1)
        kind = item["type"]
        if kind not in KINDS:
            continue
        ref = item.get("img_path", "")
        if not isinstance(ref, str):
            _fail()
        if ref:
            _relative(ref)
        box = _bbox(item.get("bbox"), 1000, 1000)
        w, h = pages[pi]["provider_size"]
        points = [box[0] * w / 1000, box[1] * h / 1000, box[2] * w / 1000, box[3] * h / 1000]
        matches = [p for p in parents if p["page_idx"] == pi and p["kind"] == kind
                   and (p["refs"] and p["refs"][0]["ref"] == ref or not p["refs"] and not ref)
                   and max(abs(a - b) for a, b in zip(p["body_bbox"], points)) <= 2]
        if len(matches) != 1:
            _fail("figure_metadata_ambiguous")
        parent = matches[0]
        identity = (pi, parent["block_index"])
        if identity in used or ref and any(r["ref"] == ref for r in records):
            _fail("figure_metadata_ambiguous")
        used.add(identity)
        captions = item.get(kind + "_caption", [])
        notes = item.get(kind + "_footnote", [])
        if any(not isinstance(v, list) or len(v) > 1000 for v in (captions, notes)):
            _fail()
        captions = [_text(v) for v in captions]
        notes = [_text(v) for v in notes]
        body_text = _text(item.get("table_body", "") if kind == "table" else item.get("content", ""))
        if (kind == "table" and parent["refs"]
                and not _table_html_matches(body_text, parent["refs"][0]["html"])):
            _fail()
        records.append({"index": index, "kind": kind, "page_idx": pi, "ref": ref,
                        "content_bbox": box, "body_bbox": parent["body_bbox"],
                        "body_text": body_text, "content_captions": captions, "content_footnotes": notes,
                        "captions": parent["captions"], "footnotes": parent["footnotes"],
                        "block_index": parent["block_index"]})
    if len(records) > MAX_VISUALS or used != {(p["page_idx"], p["block_index"]) for p in parents}:
        _fail("figure_metadata_ambiguous")
    return {"profile": profile, "pages": pages, "records": records}


def _check_excerpt(value):
    """Reparse the sidecar projection using the same typed provider contract."""
    _keys(value, {"profile", "pages", "records"})
    pages = value["pages"]
    records = value["records"]
    if not isinstance(pages, list) or not isinstance(records, list):
        _fail()
    middle = dict(value["profile"])
    middle["pdf_info"] = []
    for page in pages:
        _keys(page, {"page_idx", "provider_size", "text_blocks"})
        blocks = []
        for text in page["text_blocks"]:
            _keys(text, {"index", "kind", "level", "bbox", "text"})
            blocks.append((text["index"], {"type": text["kind"], "level": text["level"], "bbox": text["bbox"],
                                         "lines": [{"spans": [{"type": "text", "content": text["text"]}]}]}))
        for record in records:
            _keys(record, {"index", "kind", "page_idx", "ref", "content_bbox", "body_bbox", "body_text",
                           "content_captions", "content_footnotes", "captions", "footnotes", "block_index"})
            if record["page_idx"] != page["page_idx"]:
                continue
            kind = record["kind"]
            children = [{"type": kind + "_body", "bbox": record["body_bbox"], "lines": []}]
            if record["ref"]:
                if not record["ref"].startswith("images/"):
                    _fail()
                children[0]["lines"] = [{"spans": [{"type": kind, "bbox": record["body_bbox"],
                                                    "image_path": record["ref"][7:], "html": record["body_text"] if kind == "table" else ""}]}]
            for label, entries in (("caption", record["captions"]), ("footnote", record["footnotes"])):
                for entry in entries:
                    _keys(entry, {"bbox", "text"})
                    children.append({"type": kind + "_" + label, "bbox": entry["bbox"],
                                     "lines": [{"spans": [{"type": "text", "content": entry["text"]}]}]})
            blocks.append((record["block_index"], {"type": kind, "bbox": record["body_bbox"], "blocks": children}))
        # Retain source block indices without inventing text in discarded gaps.
        if len({i for i, _ in blocks}) != len(blocks):
            _fail()
        last = max((i for i, _ in blocks), default=-1)
        _int(last + 1, 0, MAX_ITEMS)
        ordered = [{"type": "unused"} for _ in range(last + 1)]
        for index, block in blocks:
            ordered[_int(index, 0, MAX_ITEMS - 1)] = block
        middle["pdf_info"].append({"page_idx": page["page_idx"], "page_size": page["provider_size"], "para_blocks": ordered})
    if len(records) > MAX_VISUALS:
        _fail()
    last = max((r["index"] for r in records), default=-1)
    _int(last + 1, 0, MAX_ITEMS)
    if len({r["index"] for r in records}) != len(records):
        _fail()
    content = [{"type": "unused", "page_idx": 0} for _ in range(last + 1)]
    for r in records:
        content[_int(r["index"], 0, MAX_ITEMS - 1)] = {"type": r["kind"], "page_idx": r["page_idx"], "bbox": r["content_bbox"],
            "img_path": r["ref"], r["kind"] + "_caption": r["content_captions"], r["kind"] + "_footnote": r["content_footnotes"],
            "table_body" if r["kind"] == "table" else "content": r["body_text"]}
    normalised = _normalise(content, middle)
    if _canonical(normalised) != _canonical(value):
        _fail("figure_proof_invalid")
    return normalised


LEGAL_PATTERNS = {
    "disclosures": r"\b(?:important|other) disclosures\b|\bdisclosure for investors\b",
    "certification": r"\banalyst certification\b|\bresearch analyst affiliations\b|\bnon[- ]u\.?s\.? research analyst disclosures\b",
    "compliance": r"\blegal(?: and|/) ?compliance\b|\bcompliance department\b",
    "conflicts": r"\bconflicts? of interest\b",
    "compensation": r"\banalysts?['’]? compensation\b|\bcompensation for (?:products|services)\b|\bnon[- ]investment banking services\b",
    "regulated": r"\b(?:authori[sz]ed|regulated) by\b",
    "availability": r"\b(?:this |the )?product is made available\b",
    "not_offer": r"\bnot (?:an? )?offer\b|\bdoes not constitute (?:an? )?offer\b",
    "banking_clients": r"\binvestment banking clients\b",
}


def _cues(text):
    plain = _plain(text).lower()
    return {name: len(re.findall(pattern, plain)) for name, pattern in LEGAL_PATTERNS.items()}


def _overlap(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) / min(a[2] - a[0], b[2] - b[0])


def _legal(record, page):
    cues = _cues(record["body_text"])
    strong = sum(bool(cues[k]) for k in LEGAL_PATTERNS if k != "banking_clients")
    if len(_plain(record["body_text"])) >= 180 and strong >= 2:
        return {"exclude": True, "reason": "exclude_legal_body", "body_cues": cues, "nearby_index": None, "nearby_cues": None}
    nearby = []
    box = record["body_bbox"]
    for block in page["text_blocks"]:
        gap = box[1] - block["bbox"][3]
        if 0 <= gap <= 24 and _overlap(box, block["bbox"]) >= .8:
            nearby.append((gap, block))
    nearby.sort(key=lambda pair: (pair[0], pair[1]["index"]))
    if nearby and not record["content_captions"] and not record["captions"]:
        gap, block = nearby[0]
        scope = _cues(block["text"])
        # A nearby heading alone, or any contact/footer alone, cannot exclude.
        own = any(cues.values())
        heading = len(_plain(block["text"])) <= 180 and (block["level"] > 0 or block["kind"] == "title")
        legal_heading = heading and any(scope[k] for k in ("disclosures", "certification", "compliance"))
        dense_local_scope = sum(bool(v) for k, v in scope.items() if k != "banking_clients") >= 2
        if own and (legal_heading or dense_local_scope):
            return {"exclude": True, "reason": "exclude_nearby_legal_scope", "body_cues": cues,
                    "nearby_index": block["index"], "nearby_cues": scope}
    return {"exclude": False, "reason": "retain_source_visual", "body_cues": cues, "nearby_index": None, "nearby_cues": None}


def _same_column(box, body):
    intersection = max(0, min(box[2], body[2]) - max(box[0], body[0]))
    return (intersection / (box[2] - box[0]) >= .8
            and box[0] >= body[0] - 24 and box[2] <= body[2] + 24)


def _attachment_decisions(records, page_idx):
    """Each note has one global ownership decision, independent of its target."""
    decisions = []
    notes = [(r["index"], kind, ordinal, entry) for r in records if r["page_idx"] == page_idx
             for kind in ("captions", "footnotes") for ordinal, entry in enumerate(r[kind])]
    for owner, kind, ordinal, entry in notes:
        box = entry["bbox"]
        candidates = []
        for r in records:
            if r["page_idx"] != page_idx or not r["ref"]:
                continue
            rb = r["body_bbox"]
            if not _same_column(box, rb):
                continue
            # A note crossing a neighbouring column is not a same-column note,
            # even if its short vertical distance would otherwise win.
            if any(other["index"] != r["index"] and other["page_idx"] == page_idx
                   and (other["body_bbox"][0] >= rb[2] - 2 or other["body_bbox"][2] <= rb[0] + 2)
                   and min(box[2], other["body_bbox"][2]) - max(box[0], other["body_bbox"][0]) > 2
                   for other in records):
                continue
            # Text must not overlap a different visual interior in the same column.
            if any(other["index"] != r["index"] and other["page_idx"] == r["page_idx"]
                   and _overlap(box, other["body_bbox"]) >= .8
                   and min(box[3], other["body_bbox"][3]) - max(box[1], other["body_bbox"][1]) > 2
                   for other in records):
                continue
            caption_gap = rb[1] - box[3]
            note_gap = box[1] - rb[3]
            if box[1] <= rb[1] and -12 <= caption_gap <= 24 and (kind == "captions" or len(_plain(entry["text"])) <= 180):
                candidates.append((abs(caption_gap), r["index"], "caption"))
            if kind == "footnotes" and -2 <= note_gap <= 24:
                candidates.append((abs(note_gap), r["index"], "footnote"))
        candidates.sort()
        reason = "outside_same_column_scope"
        winner = None
        role = None
        if candidates:
            if len(candidates) == 1 or candidates[1][0] - candidates[0][0] > .5:
                winner = candidates[0][1]
                role = candidates[0][2]
                reason = "unique_nearest_same_column"
            else:
                reason = "ambiguous_same_column"
        decisions.append({"owner": owner, "kind": kind, "ordinal": ordinal, "role": role,
                          "reason": reason, "winner": winner, "bbox": box})
    return decisions


def _attachments(record, records):
    selected, decisions = [], []
    for item in _attachment_decisions(records, record["page_idx"]):
        include = item["winner"] == record["index"]
        if include:
            selected.append(item["bbox"])
        decisions.append({**item, "include": include})
    return selected, decisions


def _crop(record, records, page_size, pixel_size):
    boxes, decisions = _attachments(record, records)
    boxes = [record["body_bbox"], *boxes]
    union = [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]
    pw, ph = pixel_size
    # Middle bboxes are viewport points, not a normalised integer-page frame.
    # Use the exact rendering matrix; ceil(raster size)/integer_size would
    # stretch fractions and shift the crop on real cropped source PDFs.
    scale = 300 / 72
    pixels = [max(0, math.floor(union[0] * scale) - MARGIN_PIXELS),
              max(0, math.floor(union[1] * scale) - MARGIN_PIXELS),
              min(pw, math.ceil(union[2] * scale) + MARGIN_PIXELS),
              min(ph, math.ceil(union[3] * scale) + MARGIN_PIXELS)]
    return {"union_bbox": union, "pixel_box": pixels, "margin_pixels": MARGIN_PIXELS,
            "source_rect_size": page_size, "point_to_pixel": [scale, 0, 0, scale, 0, 0],
            "attachments": decisions}


def _decisions(metadata, maximum):
    result, selected = [], 0
    for record in metadata["records"]:
        legal = _legal(record, metadata["pages"][record["page_idx"]])
        if not record["ref"]:
            reason, choose = "no_provider_image", False
        elif legal["exclude"]:
            reason, choose = legal["reason"], False
        elif selected >= maximum:
            reason, choose = "selection_limit", False
        else:
            reason, choose = "selected_source_visual", True
            selected += 1
        result.append({"index": record["index"], "selected": choose, "reason": reason, "legal": legal})
    return result


def _geometry(page):
    return {"rect": list(page.rect), "cropbox": list(page.cropbox), "mediabox": list(page.mediabox),
            "rotation": page.rotation}


@contextmanager
def _silent_mupdf():
    """Python stdout redirection does not suppress native PDF diagnostics."""
    import fitz

    errors = fitz.TOOLS.mupdf_display_errors()
    warnings = fitz.TOOLS.mupdf_display_warnings()
    try:
        fitz.TOOLS.mupdf_display_errors(False)
        fitz.TOOLS.mupdf_display_warnings(False)
        yield
    finally:
        try:
            fitz.TOOLS.mupdf_display_errors(errors)
        finally:
            fitz.TOOLS.mupdf_display_warnings(warnings)


def _raster_size(rect):
    """Match MuPDF's transformed integer rectangle, including float rounding."""
    import fitz

    if (not isinstance(rect, (list, tuple)) or len(rect) != 4
            or any(type(value) not in (int, float) or not math.isfinite(value) for value in rect)
            or list(rect[:2]) != [0, 0] or rect[2] <= 0 or rect[3] <= 0
            or any(value > MAX_DIMENSION * 72 / 300 + 1 for value in rect[2:])):
        _fail("figure_source_pixels_mismatch")
    # Rect/Matrix multiplication uses the renderer's float precision and
    # endpoint rounding. ceil(width * dpi / 72) differs for legitimate pages
    # such as 595.2 pt: MuPDF emits 2480 pixels, while double-precision ceil
    # applied to the stored 595.200012... point width yields 2481.
    raster = (fitz.Rect(rect) * fitz.Matrix(300 / 72, 300 / 72)).irect
    w, h = raster.width, raster.height
    if not (1 <= w <= MAX_DIMENSION and 1 <= h <= MAX_DIMENSION and w * h <= MAX_PIXELS):
        _fail("figure_source_pixels_mismatch")
    return [w, h]


def _render(page, *, annots=True):
    import fitz
    from PIL import Image

    expected_size = _raster_size(list(page.rect))
    # MuPDF's process-wide resource store can make interleaved source/provider
    # renders depend on previous pages, even when each PDF renders identically
    # in a fresh process. Isolate every comparison and carried source image;
    # never accept a warmed-cache mismatch or relax the exact RGB comparison.
    try:
        fitz.TOOLS.store_shrink(100)
    except Exception:
        _fail("figure_render_cache_isolation_failed")
    pix = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False,
                          colorspace=fitz.csRGB, annots=annots)
    if [pix.width, pix.height] != expected_size:
        _fail("figure_source_pixels_mismatch")
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def _save(image, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG")
    return {"sha256": _sha(path.read_bytes()), "rgb_sha256": _rgb_hash(image), "pixel_size": list(image.size)}


def _read_carried_page(report, page):
    data = _regular(report / page["path"], report)
    if _sha(data) != page["sha256"]:
        _fail("figure_source_pixels_mismatch")
    image = _image(data, png=True)
    if _canonical({"pixel_size": list(image.size), "rgb_sha256": _rgb_hash(image)}) != _canonical(
            {key: page[key] for key in ("pixel_size", "rgb_sha256")}):
        _fail("figure_source_pixels_mismatch")
    return image


def create_figure_sources(result_dir: Path, assets_dir: Path, *, original_pdf_sha256: str | None,
                          markdown_sha256: str, auth_original_pdf: Path | None = None,
                          max_images: int = 100):
    """Return None only when both provider metadata families are absent."""
    result_dir, assets_dir = Path(result_dir), Path(assets_dir)
    found = _metadata_files(result_dir)
    if found is None:
        return None
    try:
        return _create(result_dir, assets_dir, found, original_pdf_sha256,
                       markdown_sha256, auth_original_pdf, max_images)
    except FigureSourceError:
        raise
    except Exception:
        _fail()


def _create(result_dir, assets_dir, found, original_sha, markdown_sha, original, maximum):
    original_sha = _hash(original_sha, optional=True)
    markdown_sha = _hash(markdown_sha)
    maximum = _int(maximum, 0, MAX_VISUALS)
    if original is not None and original_sha is None:
        _fail("figure_source_binding_mismatch")
    (cp, content), (mp, middle), paths = found
    content_raw = _regular(cp, result_dir, MAX_JSON)
    middle_raw = _regular(mp, result_dir, MAX_JSON)
    if _canonical(_json(content_raw)) != _canonical(content) or _canonical(_json(middle_raw)) != _canonical(middle):
        _fail("figure_source_binding_mismatch")
    metadata = _normalise(content, middle)
    report = assets_dir.parent
    if assets_dir.is_symlink() or report.is_symlink():
        _fail("figure_asset_mismatch")
    source = report / "source_mineru.md"
    if _sha(_regular(source, report, MAX_JSON)) != markdown_sha:
        _fail("figure_source_binding_mismatch")
    decisions = _decisions(metadata, maximum)
    evidence_dir = report / "figure_source_evidence"
    if evidence_dir.exists() or (report / SIDECAR).exists() or list(assets_dir.glob("source_image_*")):
        _fail("figure_asset_mismatch")
    assets_dir.mkdir(parents=True, exist_ok=True)
    provider = {}
    for record in metadata["records"]:
        ref = record["ref"]
        if not ref:
            continue
        matches = [p for p in paths if p.is_file() and (p.relative_to(result_dir).as_posix() == ref
                   or p.relative_to(result_dir).as_posix().endswith("/" + ref))]
        if len(matches) != 1:
            _fail("figure_metadata_ambiguous")
        path = matches[0]
        data = _regular(path, result_dir)
        image = _image(data)
        suffix = path.suffix.lower()
        if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
            _fail()
        target = evidence_dir / "provider_images" / (_sha(data) + suffix)
        provider[ref] = {"path": target.relative_to(report).as_posix(), "sha256": _sha(data),
                         "rgb_sha256": _rgb_hash(image), "pixel_size": list(image.size),
                         "original_path": path, "data": data}
        if sum(len(p["data"]) for p in provider.values()) > MAX_PROVIDER_BYTES:
            _fail()
    # All inventory/ref checks happen before any asset or evidence write.
    pages, carried_pixels = [], 0
    original_bytes = None
    embedded_bytes = None
    restoration_proof = None
    if original is not None:
        original = Path(original)
        original_bytes = _regular(original, original.parent, 512 * 1024 * 1024)
        if _sha(original_bytes) != original_sha:
            _fail("figure_source_binding_mismatch")
        embedded = [p for p in paths if p.is_file() and p.suffix.lower() == ".pdf"]
        if len(embedded) != 1:
            _fail("figure_metadata_ambiguous")
        embedded_bytes = _regular(embedded[0], result_dir, 512 * 1024 * 1024)
        import fitz

        with _silent_mupdf(), fitz.open(stream=original_bytes, filetype="pdf") as authentic, fitz.open(stream=embedded_bytes, filetype="pdf") as rewritten, ExitStack() as restoration_stack:
            if authentic.is_encrypted or rewritten.is_encrypted or len(authentic) != len(metadata["pages"]) or len(rewritten) != len(authentic):
                _fail("figure_source_pixels_mismatch")
            used_pages = sorted({r["page_idx"] for r, d in zip(metadata["records"], decisions) if d["selected"]})
            render_document = rewritten
            for pi in used_pages:
                actual, supplied = authentic[pi], render_document[pi]
                geometry = _geometry(actual)
                if _canonical(geometry) != _canonical(_geometry(supplied)):
                    _fail("figure_source_pixels_mismatch")
                integer_size = metadata["pages"][pi]["provider_size"]
                if any(abs(a - b) >= 1.1 for a, b in zip(integer_size, [actual.rect.width, actual.rect.height])):
                    _fail("figure_source_pixels_mismatch")
                image, other = _render(actual), _render(supplied)
                if image.size != other.size or image.tobytes() != other.tobytes():
                    # Repair only a missing catalog configuration after binding
                    # every existing page drawing object to the admitted source.
                    # The cache / raw provider file and original crop stay intact.
                    from mineru_pdf_oc import has_missing_optional_content, restore_missing_optional_content
                    from mineru_pdf_output_intents import has_missing_output_intents, restore_missing_output_intents
                    missing_oc = has_missing_optional_content(authentic, rewritten)
                    missing_output_intents = has_missing_output_intents(authentic, rewritten)
                    if restoration_proof is not None or missing_oc == missing_output_intents:
                        image.close(); other.close()
                        _fail("figure_source_pixels_mismatch")
                    try:
                        if missing_oc:
                            restored, restoration_proof = restore_missing_optional_content(authentic, rewritten,
                                original_sha256=original_sha, embedded_sha256=_sha(embedded_bytes))
                        else:
                            restored, restoration_proof = restore_missing_output_intents(original_bytes, embedded_bytes,
                                original_sha256=original_sha, embedded_sha256=_sha(embedded_bytes))
                        restoration_stack.callback(restored.close)
                        for prior in pages:
                            previous = restored[prior["page_idx"]]
                            if _canonical(_geometry(previous)) != _canonical(prior["geometry"]):
                                _fail("figure_source_pixels_mismatch")
                            carried = _read_carried_page(report, prior)
                            candidate = _render(previous)
                            try:
                                if carried.size != candidate.size or carried.tobytes() != candidate.tobytes():
                                    _fail("figure_source_pixels_mismatch")
                            finally:
                                carried.close(); candidate.close()
                        render_document = restored
                        other.close(); other = _render(restored[pi])
                        if _canonical(_geometry(restored[pi])) != _canonical(geometry):
                            _fail("figure_source_pixels_mismatch")
                        if image.size != other.size or image.tobytes() != other.tobytes():
                            _fail("figure_source_pixels_mismatch")
                    except Exception:
                        image.close(); other.close()
                        _fail("figure_source_pixels_mismatch")
                carried_pixels += image.width * image.height
                if carried_pixels > MAX_CARRIED_PAGE_PIXELS:
                    _fail("figure_page_budget_exceeded")
                page = {"page_idx": pi, "path": f"figure_source_evidence/pages/page_{pi + 1:04}.png",
                        "provider_size": integer_size, "geometry": geometry, "dpi": 300}
                page.update(_save(image, report / page["path"]))
                pages.append(page)
                image.close()
                other.close()
                del image, other
            if restoration_proof is not None:
                restoration_proof["verified_page_indices"] = used_pages
                _validate_render_restoration(restoration_proof, original_sha256=original_sha,
                    embedded_sha256=_sha(embedded_bytes), page_indices=used_pages)
    for item in provider.values():
        target = report / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(item["data"])
    assets, copied = [], []
    image, image_page = None, None
    for record, decision in zip(metadata["records"], decisions):
        if not decision["selected"]:
            continue
        source_info = provider[record["ref"]]
        ordinal = len(assets) + 1
        if original is not None:
            page_record = next(p for p in pages if p["page_idx"] == record["page_idx"])
            if image_page != record["page_idx"]:
                if image is not None:
                    image.close()
                    del image
                image = _read_carried_page(report, page_record)
                image_page = record["page_idx"]
            crop = _crop(record, metadata["records"], page_record["geometry"]["rect"][2:], list(image.size))
            asset_path = assets_dir / f"source_image_{ordinal:02}.png"
            pixel = image.crop(crop["pixel_box"])
            binding = _save(pixel, asset_path)
            mode = "authenticated_original_crop"
        else:
            asset_path = assets_dir / f"source_image_{ordinal:02}{source_info['original_path'].suffix.lower()}"
            asset_path.write_bytes(source_info["data"])
            binding = {k: source_info[k] for k in ("sha256", "rgb_sha256", "pixel_size")}
            crop, mode = None, "provider_image_only"
        assets.append({"index": record["index"], "ref": record["ref"], "path": asset_path.relative_to(report).as_posix(),
                       "page_idx": record["page_idx"], "provider_image_sha256": source_info["sha256"],
                       "mode": mode, "crop": crop, **binding})
        copied.append((source_info["original_path"], asset_path))
    if image is not None:
        image.close()
    payload = {"schema": 2 if restoration_proof is not None else 1,
               "policy": RESTORED_POLICY if restoration_proof is not None else POLICY,
               "authority": "trusted-producer-and-outer-receipt",
               "original_pdf_sha256": original_sha,
               "original_identity": "unproven" if original_sha is None else "admitted_sha256",
               "markdown_sha256": markdown_sha,
               "authenticated_original_render": original is not None,
               "embedded_pdf_sha256": _sha(embedded_bytes) if embedded_bytes is not None else None,
               "metadata": metadata, "metadata_sha256": _sha(_canonical(metadata)),
               "provider_json_sha256": {"content_list": _sha(content_raw), "middle": _sha(middle_raw)},
               "max_images": maximum, "decisions": decisions,
               "provider_images": {ref: {k: v for k, v in p.items() if k not in {"original_path", "data"}} for ref, p in provider.items()},
               "pages": pages, "assets": assets}
    if restoration_proof is not None:
        payload["embedded_pdf_render_restoration"] = restoration_proof
    # Detect source mutation before sealing. Outer inventory independently binds
    # this sidecar and its private carriers after the producer returns.
    if original is not None and _sha(_regular(original, original.parent, 512 * 1024 * 1024)) != original_sha:
        _fail("figure_source_binding_mismatch")
    if embedded_bytes is not None and _sha(_regular(embedded[0], result_dir, 512 * 1024 * 1024)) != _sha(embedded_bytes):
        _fail("figure_source_binding_mismatch")
    if _sha(_regular(source, report, MAX_JSON)) != markdown_sha:
        _fail("figure_source_binding_mismatch")
    if (_sha(_regular(cp, result_dir, MAX_JSON)) != _sha(content_raw)
            or _sha(_regular(mp, result_dir, MAX_JSON)) != _sha(middle_raw)
            or any(_sha(_regular(p["original_path"], result_dir)) != p["sha256"] for p in provider.values())):
        _fail("figure_source_binding_mismatch")
    sidecar = report / SIDECAR
    sealed = _canonical(payload)
    if len(sealed) > MAX_JSON:
        _fail()
    sidecar.write_bytes(sealed)
    return {"images": [a["path"] for a in assets], "copied_images": copied, "sidecar_path": sidecar,
            "reference_images": {a["ref"]: a["path"] for a in assets}}


def validate_figure_sources(report_dir: Path, *, expected_original_sha256: str | None,
                            expected_markdown_sha256: str, expected_images: list[str]):
    """Validate private carriers and return exact provider reference -> asset.

    None means this is a legacy report without a sidecar, not a failed proof.
    New source producers must ensure the outer receipt requires this sidecar.
    """
    report = Path(report_dir)
    sidecar = report / SIDECAR
    if not sidecar.exists():
        if sidecar.is_symlink() or (report / "figure_source_evidence").exists() or (report / "figure_source_evidence").is_symlink():
            _fail("figure_source_binding_mismatch")
        status = report / "status.json"
        if status.exists() or status.is_symlink():
            value = _json(_regular(status, report, MAX_JSON))
            if isinstance(value, dict) and {"source_figure_map", "source_figure_map_sha256"} & set(value):
                _fail("figure_source_binding_mismatch")
        return None
    try:
        return _validate(report, expected_original_sha256, expected_markdown_sha256, expected_images)
    except FigureSourceError:
        raise
    except Exception:
        _fail("figure_proof_invalid")


def _validate_render_restoration(value, **bindings):
    from mineru_pdf_oc import POLICY as OC_POLICY, validate_restoration_receipt as validate_oc
    from mineru_pdf_output_intents import POLICY as COLOR_POLICY, validate_restoration_receipt as validate_color
    if not isinstance(value, dict):
        _fail("figure_proof_invalid")
    if value.get("policy") == OC_POLICY:
        return validate_oc(value, **bindings)
    if value.get("policy") == COLOR_POLICY:
        return validate_color(value, **bindings)
    _fail("figure_proof_invalid")


def _validate(report, original_sha, markdown_sha, images):
    original_sha = _hash(original_sha, optional=True)
    markdown_sha = _hash(markdown_sha)
    value = _json(_regular(report / SIDECAR, report, MAX_JSON))
    restored = isinstance(value, dict) and type(value.get("schema")) is int and value["schema"] == 2
    fields = {"schema", "policy", "authority", "original_pdf_sha256", "original_identity", "markdown_sha256",
              "authenticated_original_render", "embedded_pdf_sha256", "metadata", "metadata_sha256", "provider_json_sha256",
              "max_images", "decisions", "provider_images", "pages", "assets"}
    _keys(value, fields | ({"embedded_pdf_render_restoration"} if restored else set()))
    if (type(value["schema"]) is not int or value["schema"] not in (1, 2)
            or value["policy"] != (RESTORED_POLICY if restored else POLICY)
            or value["authority"] != "trusted-producer-and-outer-receipt"
            or value["original_pdf_sha256"] != original_sha or value["markdown_sha256"] != markdown_sha
            or value["original_identity"] != ("unproven" if original_sha is None else "admitted_sha256")
            or type(value["authenticated_original_render"]) is not bool):
        _fail("figure_source_binding_mismatch")
    auth = value["authenticated_original_render"]
    if (auth and original_sha is None) or (restored and not auth):
        _fail("figure_source_binding_mismatch")
    if auth:
        _hash(value["embedded_pdf_sha256"])
    elif value["embedded_pdf_sha256"] is not None:
        _fail()
    _keys(value["provider_json_sha256"], {"content_list", "middle"})
    for sha in value["provider_json_sha256"].values():
        _hash(sha)
    metadata = _check_excerpt(value["metadata"])
    if _sha(_canonical(metadata)) != value["metadata_sha256"]:
        _fail("figure_proof_invalid")
    maximum = _int(value["max_images"], 0, MAX_VISUALS)
    decisions = _decisions(metadata, maximum)
    if _canonical(decisions) != _canonical(value["decisions"]):
        _fail("figure_proof_invalid")
    if not isinstance(images, list) or any(not isinstance(v, str) for v in images):
        _fail("figure_source_binding_mismatch")
    if _sha(_regular(report / "source_mineru.md", report, MAX_JSON)) != markdown_sha:
        _fail("figure_source_binding_mismatch")
    status_path = report / "status.json"
    if status_path.exists() or status_path.is_symlink():
        status = _json(_regular(status_path, report, MAX_JSON))
        if (not isinstance(status, dict) or status.get("images") != images
                or status.get("source_markdown") != "source_mineru.md"
                or status.get("original_pdf_sha256") != original_sha):
            _fail("figure_source_binding_mismatch")
        markers = {"source_figure_map", "source_figure_map_sha256"}
        if markers & set(status):
            if (not markers <= set(status) or status["source_figure_map"] != SIDECAR
                    or status["source_figure_map_sha256"] != _sha(_regular(report / SIDECAR, report, MAX_JSON))):
                _fail("figure_source_binding_mismatch")
    providers = value["provider_images"]
    refs = {r["ref"] for r in metadata["records"] if r["ref"]}
    if not isinstance(providers, dict) or set(providers) != refs:
        _fail("figure_proof_invalid")
    for ref, info in providers.items():
        _relative(ref)
        _keys(info, {"path", "sha256", "rgb_sha256", "pixel_size"})
        _relative(info["path"])
        if not info["path"].startswith("figure_source_evidence/provider_images/"):
            _fail()
        data = _regular(report / info["path"], report)
        im = _image(data)
        if _canonical({"sha256": _sha(data), "rgb_sha256": _rgb_hash(im), "pixel_size": list(im.size)}) != _canonical({k: info[k] for k in ("sha256", "rgb_sha256", "pixel_size")}):
            _fail("figure_asset_mismatch")
    if sum((report / p["path"]).stat().st_size for p in providers.values()) > MAX_PROVIDER_BYTES:
        _fail()
    carried_pixels = 0
    expected_pages = sorted({r["page_idx"] for r, d in zip(metadata["records"], decisions) if d["selected"]}) if auth else []
    if restored:
        _validate_render_restoration(value["embedded_pdf_render_restoration"], original_sha256=original_sha,
            embedded_sha256=value["embedded_pdf_sha256"], page_indices=expected_pages)
    if not isinstance(value["pages"], list) or [p.get("page_idx") for p in value["pages"]] != expected_pages:
        _fail()
    for page in value["pages"]:
        _keys(page, {"page_idx", "path", "provider_size", "geometry", "dpi", "pixel_size", "rgb_sha256", "sha256"})
        pi = _int(page["page_idx"], 0, len(metadata["pages"]) - 1)
        if page["path"] != f"figure_source_evidence/pages/page_{pi + 1:04}.png" or type(page["dpi"]) is not int or page["dpi"] != 300:
            _fail()
        geometry = page["geometry"]
        _keys(geometry, {"rect", "cropbox", "mediabox", "rotation"})
        if type(geometry["rotation"]) is not int or geometry["rotation"] not in (0, 90, 180, 270):
            _fail()
        for box in (geometry["rect"], geometry["cropbox"], geometry["mediabox"]):
            if not isinstance(box, list) or len(box) != 4 or any(type(v) not in (int, float) or not math.isfinite(v) for v in box) or box[2] <= box[0] or box[3] <= box[1]:
                _fail()
        if geometry["rect"][:2] != [0, 0] or page["provider_size"] != metadata["pages"][pi]["provider_size"]:
            _fail()
        rect_size = [geometry["rect"][2], geometry["rect"][3]]
        if any(abs(a - b) >= 1.1 for a, b in zip(page["provider_size"], rect_size)):
            _fail()
        im = _read_carried_page(report, page)
        if list(im.size) != _raster_size(geometry["rect"]):
            _fail("figure_source_pixels_mismatch")
        carried_pixels += im.width * im.height
        if carried_pixels > MAX_CARRIED_PAGE_PIXELS:
            _fail("figure_page_budget_exceeded")
        im.close()
        del im
    selected = [(r, d) for r, d in zip(metadata["records"], decisions) if d["selected"]]
    if not isinstance(value["assets"], list) or len(value["assets"]) != len(selected) or [a.get("path") for a in value["assets"]] != images:
        _fail("figure_source_binding_mismatch")
    result = {}
    page_image, image_page = None, None
    for ordinal, ((record, _), asset) in enumerate(zip(selected, value["assets"]), 1):
        _keys(asset, {"index", "ref", "path", "page_idx", "provider_image_sha256", "mode", "crop", "sha256", "rgb_sha256", "pixel_size"})
        if (type(asset["index"]) is not int or asset["index"] != record["index"] or type(asset["page_idx"]) is not int
                or asset["page_idx"] != record["page_idx"] or asset["ref"] != record["ref"]
                or asset["provider_image_sha256"] != providers[record["ref"]]["sha256"]):
            _fail()
        _relative(asset["path"])
        if not re.fullmatch(rf"assets/source_image_{ordinal:02}\.(?:png|jpg|jpeg|webp)", asset["path"]):
            _fail()
        data = _regular(report / asset["path"], report)
        im = _image(data, png=auth)
        if auth:
            page_record = next(p for p in value["pages"] if p["page_idx"] == record["page_idx"])
            if image_page != record["page_idx"]:
                if page_image is not None:
                    page_image.close()
                    del page_image
                page_image = _read_carried_page(report, page_record)
                image_page = record["page_idx"]
            crop = _crop(record, metadata["records"], page_record["geometry"]["rect"][2:], list(page_image.size))
            if asset["mode"] != "authenticated_original_crop" or _canonical(crop) != _canonical(asset["crop"]):
                _fail("figure_proof_invalid")
            expected = page_image.crop(crop["pixel_box"])
            if im.size != expected.size or im.tobytes() != expected.tobytes():
                _fail("figure_asset_mismatch")
        elif asset["mode"] != "provider_image_only" or asset["crop"] is not None or _sha(data) != providers[record["ref"]]["sha256"]:
            _fail("figure_proof_invalid")
        if _canonical({"sha256": _sha(data), "rgb_sha256": _rgb_hash(im), "pixel_size": list(im.size)}) != _canonical({k: asset[k] for k in ("sha256", "rgb_sha256", "pixel_size")}):
            _fail("figure_asset_mismatch")
        result[record["ref"]] = asset["path"]
    if page_image is not None:
        page_image.close()
    return result
