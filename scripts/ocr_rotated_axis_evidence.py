"""Bounded rotated date-axis recognition with replayable source geometry.

The selected transcript retains every unchanged character. Original recognition
and every replacement remain private proof data. New rotated numbers never gain
numeric acceptance from this recognition alone.
"""
from __future__ import annotations

import hashlib
from collections import Counter
import json
import math
from pathlib import Path
import re
import statistics
import time
from typing import Any

import fitz
from PIL import Image, ImageChops, ImageDraw

POLICY = "rotated-axis-regions-v1"
ENGINE = "tesseract-cli-rotated-axis"
LABELS = ("geometric-sorted", "source-flow", "full-page-psm11")
MAX_REGIONS = 4
MAX_READS = 8
TIME_BUDGET = 180
READ_TIMEOUT = 30
MAX_PIXELS = 80_000_000
MAX_WORDS = 20_000
MAX_SEEDS = 32
MAX_REGION_WORDS = 256
MAX_EXPANSION_PASSES = 8
MAX_PROFILE_COLUMNS = 20_000
MAX_TEXT_BYTES = 1_000_000
MAX_PROOF_BYTES = 8_000_000
LONG = re.compile(r"[A-Za-z0-9]{25,}")
DATE = re.compile(r"(?:[12][0-9]{3})[/.-](?:0?[1-9]|1[0-2])(?:[/.-](?:0?[1-9]|[12][0-9]|3[01]))?")
HASH = re.compile(r"[a-f0-9]{64}")


class RotatedAxisError(ValueError):
    """Fixed categories only; callers must never publish source text."""

    def __init__(self, message, *, guard=None, source_pixel_box=None, source_word_box=None):
        super().__init__(message)
        self.guard = guard
        self.source_pixel_box = source_pixel_box
        self.source_word_box = source_word_box


DIAGNOSTIC_STAGES = {"candidate_validation", "region_planning", "region_recognition", "composed_readability"}
DIAGNOSTIC_REASONS = {"invalid_candidate_evidence", "not_eligible", "no_valid_direction", "ambiguous_directions",
    "page_readability_rejected", "seed_count", "region_count", "expansion_bound", "word_assignment",
    "region_geometry", "grown_word_membership", "horizontal_word_intersection", "partial_word_intersection",
    "crop_bounds", "crop_area", "total_crop_area", "overlapping_regions", "geometric-sorted_words",
    "source-flow_words", "full-page-psm11_words", "geometric-sorted_glyphs", "source-flow_glyphs",
    "full-page-psm11_glyphs", "candidate_readability", "candidate_same_glyphs", "cli_transcript_order",
    "source_transcript_spans", "fragment_pixel_support", "uncovered_source_ink"}


def safe_rotated_axis_diagnostics(value):
    """Only fixed stages and bounded pixel/count data may leave private OCR."""
    if (not isinstance(value, dict) or type(value.get("schema")) is not int or value["schema"] != 1
            or not isinstance(value.get("stage"), str) or not isinstance(value.get("reason"), str)
            or value.get("stage") not in DIAGNOSTIC_STAGES or value.get("reason") not in DIAGNOSTIC_REASONS):
        return None
    result = {key: value[key] for key in ("schema", "stage", "reason")}
    for key in ("region", "planned_region_count"):
        if key in value:
            if type(value[key]) is not int or not 1 <= value[key] <= MAX_REGIONS:
                return None
            result[key] = value[key]
    for key in ("source_pixel_box", "source_word_box"):
        if key in value:
            box = value[key]
            if (not isinstance(box, list) or len(box) != 4
                    or any(not _number(v) or not 0 <= v <= MAX_PIXELS or (key == "source_pixel_box" and type(v) is not int) for v in box)
                    or box[0] >= box[2] or box[1] >= box[3]):
                return None
            result[key] = list(box)
    if "reads" in value:
        if not isinstance(value["reads"], list) or len(value["reads"]) != 2:
            return None
        result["reads"] = []
        for read, angle in zip(value["reads"], (90, 270)):
            if (not isinstance(read, dict) or type(read.get("angle")) is not int or read["angle"] != angle
                    or type(read.get("accepted")) is not bool
                    or any(type(read.get(key)) is not int or not 0 <= read[key] <= MAX_WORDS for key in ("words", "date_words"))
                    or read["date_words"] > read["words"]):
                return None
            result["reads"].append({key: read[key] for key in ("angle", "words", "date_words", "accepted")})
    return result


def _record_diagnostic(diagnostics, stage, reason, **values):
    if diagnostics is not None:
        diagnostics.clear()
        diagnostics.update(safe_rotated_axis_diagnostics({"schema": 1, "stage": stage, "reason": reason, **values}) or {})


def _fail(guard=None):
    raise RotatedAxisError("rotated_axis_proof_invalid", guard=guard)


def _canonical(value):
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    except (ValueError, TypeError, OverflowError):
        _fail()


def _hash(value):
    return hashlib.sha256(value).hexdigest()


def proof_sha256(proof):
    return _hash(_canonical(proof))


def _number(value):
    try:
        return type(value) in (int, float) and math.isfinite(value)
    except OverflowError:
        return False


def _size(value, *, integer=False):
    if (not isinstance(value, list) or len(value) != 2
            or any(not _number(v) or v <= 0 or (integer and type(v) is not int) for v in value)):
        _fail()
    if integer and value[0] * value[1] > MAX_PIXELS:
        _fail()
    return value


def _words(values, size, *, pixels=False):
    if not isinstance(values, list) or len(values) > MAX_WORDS:
        _fail()
    result = []
    for original in values:
        if isinstance(original, (tuple, list)) and len(original) >= 5:
            original = {"bbox": list(original[:4]), "text": original[4],
                        "block": original[5] if len(original) > 5 else 0,
                        "paragraph": 0, "line": original[6] if len(original) > 6 else 0}
        if (not isinstance(original, dict) or set(original) != {"bbox", "text", "block", "paragraph", "line"}
                or not isinstance(original["text"], str) or not original["text"]
                or any(c.isspace() for c in original["text"])
                or len(original["text"].encode()) > MAX_TEXT_BYTES
                or any(type(original[k]) is not int or not 0 <= original[k] <= 10_000_000
                       for k in ("block", "paragraph", "line"))):
            _fail()
        box = original["bbox"]
        if (not isinstance(box, list) or len(box) != 4 or any(not _number(v) for v in box)
                or (pixels and any(type(v) is not int for v in box))
                or not (0 <= box[0] < box[2] <= size[0] and 0 <= box[1] < box[3] <= size[1])):
            _fail()
        result.append({**original, "bbox": list(box)})
    if sum(len(w["text"].encode()) for w in result) > MAX_TEXT_BYTES:
        _fail()
    return result


def _spans(text, words):
    if not isinstance(text, str) or len(text.encode()) > MAX_TEXT_BYTES:
        _fail()
    spans, cursor = [], 0
    for word in words:
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        start, end = cursor, cursor + len(word["text"])
        if text[start:end] != word["text"] or (end < len(text) and not text[end].isspace()):
            _fail()
        spans.append((start, end))
        cursor = end
    if text[cursor:].strip():
        _fail()
    return spans


def _readability(text):
    from extract_native_market_sources import page_readability
    return page_readability(text, allow_sparse_ocr=True)


def _candidates(values, size):
    if not isinstance(values, dict) or set(values) != set(LABELS):
        _fail()
    result = {}
    for key in LABELS:
        value = values[key]
        if not isinstance(value, dict) or set(value) != {"text", "words"}:
            _fail()
        text = value["text"]
        if not isinstance(text, str) or len(text.encode()) > MAX_TEXT_BYTES:
            _fail()
        try:
            result[key] = {"text": text, "words": _words(value["words"], size)}
        except RotatedAxisError as exc:
            exc.guard = key + "_words"
            raise
        glyphs = Counter(c for c in text if not c.isspace())
        if glyphs != Counter(c for word in result[key]["words"] for c in word["text"]):
            _fail(key + "_glyphs")
        if _readability(text)["reason"] != "opaque_ascii_runs":
            raise RotatedAxisError("rotated_axis_not_eligible", guard="candidate_readability")
    if sorted(c for c in result[LABELS[0]]["text"] if not c.isspace()) != sorted(
            c for c in result[LABELS[1]]["text"] if not c.isspace()):
        _fail("candidate_same_glyphs")
    prior_cli_text = _region_text(result["full-page-psm11"]["words"])[0]
    if prior_cli_text != result["full-page-psm11"]["text"]:
        _fail("cli_transcript_order")
    return result


def _intersects(a, b):
    return min(a[2], b[2]) > max(a[0], b[0]) and min(a[3], b[3]) > max(a[1], b[1])


def _union(boxes):
    return [min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes)]


def _ink_profile(image, image_size, rows, gap):
    if image_size[0] > MAX_PROFILE_COLUMNS:
        raise RotatedAxisError("rotated_axis_not_eligible")
    counts = [0] * image_size[0]
    if image is not None:
        mask = image.crop((0, rows[0], image_size[0], rows[1])).convert("L").point(lambda value: 255 if value < 96 else 0)
        counts = [mask.crop((x, 0, x + 1, mask.height)).histogram()[255] for x in range(mask.width)]
    return {"rows": rows, "threshold": 96, "max_gap": gap, "dark_counts": counts}


def _grow_columns(box, profile):
    counts, gap = profile["dark_counts"], profile["max_gap"]
    left, right = box[0], box[2]
    cursor, last = left - 1, left
    while cursor >= 0 and last - cursor <= gap:
        if counts[cursor]:
            last = cursor; left = min(left, cursor)
        cursor -= 1
    cursor, last = right, right - 1
    while cursor < len(counts) and cursor - last <= gap:
        if counts[cursor]:
            last = cursor; right = max(right, cursor + 1)
        cursor += 1
    # Keep source white margin at the terminal labels. A crop stopping at
    # the last dark column would otherwise look clipped to region admission.
    return [left - 3, box[1], right + 3, box[3]]


def _axis_word(word, glyph_height):
    box = word["bbox"]
    return (LONG.search(word["text"]) is not None or
            (re.fullmatch(r"[0-9/.,+\-()]+", word["text"]) is not None
             and box[3] - box[1] >= 1.2 * glyph_height
             and box[3] - box[1] >= 1.5 * (box[2] - box[0])))


def _separate_chart_top(image, pixel_box, earliest_axis_top, glyph_height_pixels):
    """Separate a chart baseline only at a bounded source-pixel near-white gap.

    Read only the upper third of the bounded proposed axis band. A long
    horizontal stroke must precede the first full-width near-white gap. One
    isolated gray pixel per row is retained as noise in the recorded profile.
    The new
    boundary cannot cut any known axis word. Horizontal scale/body words are
    checked afterwards and remain outside the replacement ledger.
    """
    left, top, right, bottom = pixel_box
    scan_end = top + max(1, (bottom - top) // 3)
    minimum_gap = max(6, math.ceil(glyph_height_pixels * .15))
    counts, longest = [], []
    if image is not None:
        gray = image.crop((left, top, right, scan_end)).convert("L")
        pixels = gray.tobytes()
        for row in range(gray.height):
            values = pixels[row * gray.width:(row + 1) * gray.width]
            counts.append(sum(value < 245 for value in values))
            run = best = 0
            for value in values:
                run = run + 1 if value < 245 else 0
                best = max(best, run)
            longest.append(best)
    profile = {"policy": "chart-baseline-white-gap-v1", "input_pixel_box": list(pixel_box),
               "scan_rows": [top, scan_end], "threshold": 245, "maximum_gap_row_ink": 1, "minimum_gap": minimum_gap,
               "row_dark_counts": counts, "row_longest_dark_runs": longest,
               "separator_row": None, "white_gap": None, "selected_top": top}
    baselines = [top + i for i, run in enumerate(longest) if run >= math.ceil((right - left) * .6)]
    if not baselines:
        return list(pixel_box), profile
    separator = baselines[-1]
    cursor = separator + 1
    while cursor < scan_end:
        if counts[cursor - top] > 1:
            cursor += 1
            continue
        begin = cursor
        while cursor < scan_end and counts[cursor - top] <= 1:
            cursor += 1
        # Require pixels below the entire gap, rather than accepting a gap
        # cut by the scan boundary. Keep at least two white pixels above ink.
        if cursor - begin >= minimum_gap and cursor < scan_end:
            chosen = begin + (cursor - begin) // 2
            if (begin - separator <= math.ceil(glyph_height_pixels)
                    and cursor - chosen >= 2 and chosen <= earliest_axis_top):
                profile.update(separator_row=separator, white_gap=[begin, cursor], selected_top=chosen)
                return [left, chosen, right, bottom], profile
            break
    return list(pixel_box), profile


def _select_axis_regions(candidates, page_size, image_size, source_image=None, *, seeds_only=False):
    base = candidates["source-flow"]
    try:
        spans = _spans(base["text"], base["words"])
    except RotatedAxisError as exc:
        exc.guard = "source_transcript_spans"
        raise
    runs = list(LONG.finditer(base["text"]))
    if not runs or len(runs) > MAX_SEEDS:
        raise RotatedAxisError("rotated_axis_not_eligible", guard="seed_count")
    targets = []
    for run in runs:
        ids = [i for i, (start, end) in enumerate(spans) if start < run.end() and end > run.start()]
        if not ids:
            _fail()
        targets.append(_union([base["words"][i]["bbox"] for i in ids]))
    padding = min(4.0, max(1.0, statistics.median(b[3] - b[1] for b in targets) * .35))
    clusters = [[b[0] - padding, b[1] - padding, b[2] + padding, b[3] + padding] for b in targets]
    changed = True
    while changed:
        changed = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if _intersects(clusters[i], clusters[j]):
                    clusters[i] = _union([clusters[i], clusters[j]])
                    clusters.pop(j); changed = True; break
            if changed:
                break
    if not 1 <= len(clusters) <= MAX_REGIONS:
        raise RotatedAxisError("rotated_axis_not_eligible", guard="region_count")
    regions, assigned = [], set()
    def axis_word(word, height):
        return bool(LONG.search(word["text"])) if seeds_only else _axis_word(word, height)
    glyph_height = statistics.median(b[3] - b[1] for b in targets)
    for box in sorted(clusters, key=lambda b: (b[1], b[0])):
        # A long horizontal garbage row can be only one slice of vertical
        # dates. Expand upwards to the bounded full label height, then include
        # adjacent tall date words. Never use document-specific coordinates.
        box[1] = min(box[1], box[3] - 4 * glyph_height - padding)
        grew, passes = True, 0
        while grew:
            passes += 1
            if passes > MAX_EXPANSION_PASSES:
                raise RotatedAxisError("rotated_axis_not_eligible", guard="expansion_bound")
            grew = False
            for word in base["words"]:
                wb = word["bbox"]
                gap = max(0, wb[0] - box[2], box[0] - wb[2])
                if axis_word(word, glyph_height) and gap <= 2 * glyph_height and min(wb[3], box[3]) > max(wb[1], box[1]):
                    expanded = _union([box, wb])
                    if expanded != box:
                        box = expanded; grew = True
        ids = {i for i, word in enumerate(base["words"])
               if axis_word(word, glyph_height) and _intersects(word["bbox"], box)}
        if ids & assigned:
            raise RotatedAxisError("rotated_axis_not_eligible", guard="word_assignment")
        assigned |= ids
        box = _union([box, *[base["words"][i]["bbox"] for i in ids]])
        w, h = box[2] - box[0], box[3] - box[1]
        if (not ids or len(ids) > MAX_REGION_WORDS or min(box) <= 0 or box[2] >= page_size[0] or box[3] >= page_size[1]
                or w < 4 * h or h > page_size[1] * .08 or w < page_size[0] * .08
                or w * h > page_size[0] * page_size[1] * .04):
            raise RotatedAxisError("rotated_axis_not_eligible", guard="region_geometry")
        pixel_box = [math.floor(box[0] * image_size[0] / page_size[0]),
                     math.floor(box[1] * image_size[1] / page_size[1]),
                     math.ceil(box[2] * image_size[0] / page_size[0]),
                     math.ceil(box[3] * image_size[1] / page_size[1])]
        seed_box = list(pixel_box)
        earliest = min(math.floor(base["words"][i]["bbox"][1] * image_size[1] / page_size[1]) for i in ids)
        pixel_box, separation = _separate_chart_top(source_image, pixel_box, earliest,
                                                   glyph_height * image_size[1] / page_size[1])
        # OCR word boxes use fractional points while a crop starts at an
        # integer pixel. A retained horizontal word may therefore extend by
        # less than one pixel into the chosen blank row. Align to its ceiling
        # only inside the proven white gap; genuine body/axis overlap still
        # fails the unchanged whole-word checks below.
        if separation["white_gap"] is not None:
            top = pixel_box[1]
            scale_x, scale_y = image_size[0] / page_size[0], image_size[1] / page_size[1]
            edges = [math.ceil(word["bbox"][3] * scale_y) for word in base["words"]
                     if not axis_word(word, glyph_height)
                     and word["bbox"][0] * scale_x < pixel_box[2]
                     and word["bbox"][2] * scale_x > pixel_box[0]
                     and word["bbox"][1] * scale_y < top < word["bbox"][3] * scale_y <= top + 1]
            aligned_top = max(edges, default=top)
            blank_rows = separation["row_dark_counts"][top - separation["scan_rows"][0]:aligned_top - separation["scan_rows"][0]]
            if (aligned_top > top and aligned_top <= earliest
                    and aligned_top <= separation["white_gap"][1] - 2
                    and len(blank_rows) == aligned_top - top and not any(blank_rows)):
                pixel_box[1] = aligned_top
                separation["selected_top"] = aligned_top
        profile = _ink_profile(source_image, image_size, pixel_box[1::2],
                               max(1, math.ceil(2 * glyph_height * image_size[0] / page_size[0])))
        pixel_box = _grow_columns(pixel_box, profile)
        # Pixel growth may encounter words absent from a seed garbage row.
        # Include every whole word, and refuse horizontal chart scales/prose.
        grown = [pixel_box[0] * page_size[0] / image_size[0], pixel_box[1] * page_size[1] / image_size[1],
                 pixel_box[2] * page_size[0] / image_size[0], pixel_box[3] * page_size[1] / image_size[1]]
        if seeds_only:
            all_ids = ids
        else:
            all_ids = {i for i, word in enumerate(base["words"]) if _intersects(word["bbox"], grown)}
            if (not ids <= all_ids or len(all_ids) > MAX_REGION_WORDS
                    or any(i not in ids and i in assigned for i in all_ids)):
                raise RotatedAxisError("rotated_axis_not_eligible", guard="grown_word_membership")
            for i in all_ids:
                word = base["words"][i]; wb = word["bbox"]
                if not axis_word(word, glyph_height):
                    raise RotatedAxisError("rotated_axis_not_eligible", guard="horizontal_word_intersection",
                                           source_pixel_box=pixel_box, source_word_box=wb)
                if not (grown[0] <= wb[0] and grown[1] <= wb[1] and wb[2] <= grown[2] and wb[3] <= grown[3]):
                    raise RotatedAxisError("rotated_axis_not_eligible", guard="partial_word_intersection",
                                           source_pixel_box=pixel_box, source_word_box=wb)
            assigned |= all_ids
        if min(pixel_box) < 2 or pixel_box[2] > image_size[0] - 2 or pixel_box[3] > image_size[1] - 2:
            raise RotatedAxisError("rotated_axis_not_eligible", guard="crop_bounds")
        if (pixel_box[2] - pixel_box[0]) * (pixel_box[3] - pixel_box[1]) > image_size[0] * image_size[1] * .04:
            raise RotatedAxisError("rotated_axis_not_eligible", guard="crop_area")
        regions.append({"id": len(regions) + 1, "seed_pixel_box": seed_box, "source_pixel_box": pixel_box,
                        "source_word_indices": sorted(all_ids), "top_separation": separation, "ink_profile": profile})
    if sum((r["source_pixel_box"][2] - r["source_pixel_box"][0]) *
           (r["source_pixel_box"][3] - r["source_pixel_box"][1]) for r in regions) > image_size[0] * image_size[1] * .12:
        raise RotatedAxisError("rotated_axis_not_eligible", guard="total_crop_area")
    for i, a in enumerate(regions):
        if any(_intersects(a["source_pixel_box"], b["source_pixel_box"]) for b in regions[i + 1:]):
            raise RotatedAxisError("rotated_axis_not_eligible", guard="overlapping_regions")
    return regions


def _pixel_word_box(word, page_size, image_size):
    return [operation(word["bbox"][i] * image_size[i % 2] / page_size[i % 2])
            for i, operation in enumerate((math.floor, math.floor, math.ceil, math.ceil))]


def _select_fragment_regions(candidates, page_size, image_size, source_image):
    """Close complete source-word ink over independently separated date bands.

    Whole-page OCR can assign one word to slices of several vertical labels,
    even across adjacent charts. Character shape is not ownership evidence.
    Every non-white source pixel must instead belong to a planned band, or to
    its independently detected final gray baseline row. Acceptance remains
    pending until complete rotated date words cover every band pixel.
    """
    plans = _select_axis_regions(candidates, page_size, image_size, source_image, seeds_only=True)
    if any(p["top_separation"]["white_gap"] is None for p in plans):
        raise RotatedAxisError("rotated_axis_not_eligible", guard="fragment_pixel_support")
    gray = source_image.convert("L")
    for plan in plans:
        left, _, right, _ = plan["seed_pixel_box"]
        separator = plan["top_separation"]["separator_row"]
        row = gray.crop((left, separator, right, separator + 1)).tobytes()
        runs, begin = [], None
        for x, value in enumerate((*row, 255)):
            if value < 245 and begin is None:
                begin = x
            elif value >= 245 and begin is not None:
                if x - begin >= math.ceil((right - left) * .6):
                    runs.append([left + begin, left + x])
                begin = None
        if len(runs) != 1:
            raise RotatedAxisError("rotated_axis_not_eligible", guard="fragment_pixel_support")
        plan["fragment_separator_run"] = runs[0]
        plan["fragment_support"] = []
        plan["source_word_indices"] = []
    base = candidates["source-flow"]
    scanned_pixels = 0
    for index, word in enumerate(base["words"]):
        box = _pixel_word_box(word, page_size, image_size)
        touching = [p for p in plans if _intersects(box, p["source_pixel_box"])]
        if not touching:
            continue
        scanned_pixels += (box[2] - box[0]) * (box[3] - box[1])
        if scanned_pixels > MAX_PIXELS:
            raise RotatedAxisError("rotated_axis_not_eligible", guard="fragment_pixel_support")
        crop = gray.crop(tuple(box))
        pixels = crop.tobytes()
        support, separators, outside = {}, {}, 0
        for offset, value in enumerate(pixels):
            if value >= 245:
                continue
            x, y = box[0] + offset % crop.width, box[1] + offset // crop.width
            owners = [p for p in touching if p["source_pixel_box"][0] <= x < p["source_pixel_box"][2]
                      and p["source_pixel_box"][1] <= y < p["source_pixel_box"][3]]
            if len(owners) == 1:
                support.setdefault(owners[0]["id"], []).append((offset, value))
                continue
            # The word box may include the chart's gray baseline, separated
            # from the labels by a proved white gap. Only that exact detected
            # row is admissible; dark strokes or any other row stay outside.
            owners = [p for p in touching if value >= 96
                      and y == p["top_separation"]["separator_row"]
                      and p["fragment_separator_run"][0] <= x < p["fragment_separator_run"][1]]
            if len(owners) == 1:
                separators.setdefault(owners[0]["id"], []).append((offset, value))
            else:
                outside += 1
        if not support and outside:
            continue  # The original word's actual ink is entirely retained.
        if (outside or not support or not any(value < 96 for rows in support.values() for _, value in rows)):
            raise RotatedAxisError("rotated_axis_not_eligible", guard="fragment_pixel_support",
                                   source_pixel_box=touching[0]["source_pixel_box"], source_word_box=word["bbox"])
        supported = [p for p in touching if p["id"] in support]
        # A cross-chart word must lie in the same independently proved blank
        # separator band. Vertically unrelated regions cannot absorb it.
        if len(supported) > 1 and max(p["top_separation"]["white_gap"][0] for p in supported) >= min(
                p["top_separation"]["white_gap"][1] for p in supported):
            raise RotatedAxisError("rotated_axis_not_eligible", guard="fragment_pixel_support")
        def evidence(groups):
            return [{"region_id": region_id, "pixels": len(rows),
                     "core_pixels": sum(value < 96 for _, value in rows),
                     "pixel_support_sha256": _hash(_canonical(rows))} for region_id, rows in sorted(groups.items())]
        owner = supported[0]
        owner["source_word_indices"].append(index)
        owner["fragment_support"].append({"word_index": index, "word_pixel_box": box,
            "support": evidence(support), "separator_support": evidence(separators)})
    assigned = {index for p in plans for index in p["source_word_indices"]}
    seed_ids = {i for i, word in enumerate(base["words"]) if LONG.search(word["text"])}
    if (not seed_ids <= assigned or any(not p["source_word_indices"] or len(p["source_word_indices"]) > MAX_REGION_WORDS for p in plans)):
        raise RotatedAxisError("rotated_axis_not_eligible", guard="fragment_pixel_support")
    return plans


def _select_regions(candidates, page_size, image_size, source_image=None):
    try:
        return _select_axis_regions(candidates, page_size, image_size, source_image)
    except RotatedAxisError as original:
        if source_image is None or original.guard not in {
                "horizontal_word_intersection", "partial_word_intersection", "grown_word_membership"}:
            raise
        try:
            return _select_fragment_regions(candidates, page_size, image_size, source_image)
        except RotatedAxisError:
            raise original


def _date_component_coverage(gray, words):
    """Account for a one-pixel light edge without expanding any OCR box.

    Each connected component has one original date-word owner. Every core
    pixel stays in that unmodified box; an outside pixel needs a directly
    adjacent darker pixel inside it. A gray chain to a distant dark core,
    another word, a detached mark or a second outside row is not sufficient.
    """
    width, height = gray.size
    pixels, visited = gray.tobytes(), bytearray(width * height)
    row_owners = [-1] * height
    for index, word in enumerate(words):
        for y in range(word["bbox"][1], word["bbox"][3]):
            row_owners[y] = index
    def owner_at(x, y):
        owner = row_owners[y]
        return owner if owner >= 0 and words[owner]["bbox"][0] <= x < words[owner]["bbox"][2] else -1
    components, totals = [], [0] * len(words)
    for start, value in enumerate(pixels):
        if value >= 245 or visited[start]:
            continue
        queue, visited[start] = [start], 1
        owners, core_owners, fringe = set(), set(), []
        count = core_count = 0
        bounds = [width, height, 0, 0]
        digest = hashlib.sha256()
        while queue:
            offset = queue.pop()
            x, y, value = offset % width, offset // width, pixels[offset]
            count += 1
            bounds = [min(bounds[0], x), min(bounds[1], y), max(bounds[2], x + 1), max(bounds[3], y + 1)]
            digest.update(offset.to_bytes(4, "big") + bytes((value,)))
            owner = owner_at(x, y)
            if owner < 0:
                fringe.append(offset)
            else:
                owners.add(owner)
            if value < 96:
                if owner < 0:
                    _fail("uncovered_source_ink")
                core_count += 1
                core_owners.add(owner)
            if len(owners) > 1 or len(core_owners) > 1:
                _fail("uncovered_source_ink")
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    neighbor = ny * width + nx
                    if not visited[neighbor] and pixels[neighbor] < 245:
                        visited[neighbor] = 1
                        queue.append(neighbor)
        if len(owners) != 1 or (fringe and core_owners != owners):
            _fail("uncovered_source_ink")
        owner = next(iter(owners))
        box = words[owner]["bbox"]
        for offset in fringe:
            x, y, value = offset % width, offset // width, pixels[offset]
            if not (box[0] - 1 <= x < box[2] + 1 and box[1] - 1 <= y < box[3] + 1):
                _fail("uncovered_source_ink")
            supported = False
            for ny in range(max(0, y - 1), min(height, y + 2)):
                for nx in range(max(0, x - 1), min(width, x + 2)):
                    adjacent_owner = owner_at(nx, ny)
                    if adjacent_owner not in (-1, owner):
                        _fail("uncovered_source_ink")
                    if adjacent_owner == owner and pixels[ny * width + nx] < value:
                        supported = True
            if not supported:
                _fail("uncovered_source_ink")
        totals[owner] += count
        components.append({"word_index": owner, "bbox": bounds, "pixels": count, "core_pixels": core_count,
                           "fringe_pixels": len(fringe), "pixel_support_sha256": digest.hexdigest()})
        if len(components) > MAX_WORDS:
            _fail("uncovered_source_ink")
    return {"core_threshold": 96, "maximum_edge_pixels": 1, "components": components}, totals


def _date_pixel_coverage(crop, read):
    """Require all source ink in a new fragment band to belong to full dates.

    No box dilation, omitted words, threshold relaxation or inferred date
    values are used. The existing exact-box proof is unchanged when it
    succeeds. Only a pixel-proved light component edge may extend one pixel
    beyond an original word box. The consumer recomputes this from pixels.
    """
    rotated = crop.transpose(Image.Transpose.ROTATE_90 if read["angle"] == 90 else Image.Transpose.ROTATE_270)
    ink = rotated.convert("L").point(lambda value: 255 if value < 245 else 0)
    words = sorted(read["words"], key=lambda word: (word["bbox"][1], word["bbox"][0]))
    if not 3 <= len(words) <= MAX_REGION_WORDS or any(a["bbox"][3] >= b["bbox"][1] for a, b in zip(words, words[1:])):
        _fail("uncovered_source_ink")
    covered, counts = Image.new("L", rotated.size), []
    for word in words:
        box = word["bbox"]
        count = ink.crop(tuple(box)).histogram()[255]
        if not count:
            _fail("uncovered_source_ink")
        ImageDraw.Draw(covered).rectangle((box[0], box[1], box[2] - 1, box[3] - 1), fill=255)
        counts.append({"bbox": box, "pixels": count})
    result = {"policy": "complete-date-source-ink-v1", "threshold": 245,
            "source_ink_sha256": _hash(ink.tobytes()), "pixels": ink.histogram()[255], "words": counts}
    if ImageChops.subtract(ink, covered).getbbox() is not None:
        support, totals = _date_component_coverage(rotated.convert("L"), words)
        result.update(policy="complete-date-source-ink-components-v1", component_support=support,
                      words=[{**row, "box_pixels": row["pixels"], "pixels": total} for row, total in zip(counts, totals)])
    return result


def _transform(box, angle):
    left, top, right, bottom = box
    # Coordinate boundaries, not pixel centres; transposition is lossless.
    return ([0, -1, right, 1, 0, top], [0, 1, -top, -1, 0, right]) if angle == 90 else (
        [0, 1, left, -1, 0, bottom], [0, -1, bottom, 1, 0, -left])


def _point(point, matrix):
    x, y = point
    a, b, c, d, e, f = matrix
    return [a * x + b * y + c, d * x + e * y + f]


def _quad(box, matrix, image_size, page_size):
    x0, y0, x1, y1 = box
    pixels = [_point(p, matrix) for p in ([x0, y0], [x1, y0], [x1, y1], [x0, y1])]
    points = [[p[0] * page_size[0] / image_size[0], p[1] * page_size[1] / image_size[1]] for p in pixels]
    return {"source_pixel_quad": pixels, "source_quad": points}


def _region_text(words, image_size=None):
    lines = {}
    for i, word in enumerate(words):
        lines.setdefault((word["block"], word["paragraph"], word["line"]), []).append((i, word))
    ordered = sorted(lines.values(), key=lambda row: (min(w["bbox"][1] for _, w in row), min(w["bbox"][0] for _, w in row)))
    text, token_spans = "", []
    for row in ordered:
        if text:
            text += "\n"
        first = True
        for i, word in sorted(row, key=lambda pair: pair[1]["bbox"][0]):
            if not first:
                text += " "
            first = False
            start = len(text); text += word["text"]
            token_spans.append((start, len(text), i))
    # No invented separators or omitted recognition words are permitted.
    labels = [line.replace(" ", "") for line in text.splitlines()]
    # The numeric proof maps substrings within one word. Split sign/month
    # words would need a multiword quad protocol and are refused beforehand.
    eligible = (len(labels) >= 3 and len(set(labels)) >= 3 and all(len(row) == 1 for row in ordered)
                and all(DATE.fullmatch(line) for line in labels))
    if image_size is not None and any(min(word["bbox"]) < 2 or word["bbox"][2] > image_size[0] - 2
                                     or word["bbox"][3] > image_size[1] - 2 for word in words):
        eligible = False
    return text, token_spans, eligible


def _runtime(language, version, models):
    if (not isinstance(language, str) or not re.fullmatch(r"[a-z_]+(?:\+[a-z_]+)*", language)
            or not isinstance(version, str) or not re.fullmatch(r"[0-9][0-9A-Za-z.+_-]{0,63}", version)
            or not isinstance(models, list) or len(models) != len(language.split("+"))):
        _fail()
    for model, lang in zip(models, language.split("+")):
        if (not isinstance(model, dict) or set(model) != {"language", "filename", "sha256"}
                or model["language"] != lang or model["filename"] != lang + ".traineddata"
                or not isinstance(model["sha256"], str) or not HASH.fullmatch(model["sha256"])):
            _fail()
    return {"engine": ENGINE, "languages": language, "tesseract_version": version, "traineddata": models,
            "dpi": 300, "psm": 6, "output": "tsv", "angles": [90, 270], "max_regions": MAX_REGIONS,
            "max_reads": MAX_READS, "budget_seconds": TIME_BUDGET, "read_timeout_seconds": READ_TIMEOUT}


def _compose(candidates, regions):
    base = candidates["source-flow"]
    spans = _spans(base["text"], base["words"])
    edits = []
    for region in regions:
        selected = next(r for r in region["reads"] if r["angle"] == region["selected_angle"])
        text, _, _ = _region_text(selected["words"])
        for n, i in enumerate(region["source_word_indices"]):
            start, end = spans[i]
            edits.append({"begin": start, "end": end, "word_index": i, "region_id": region["id"],
                          "replacement": "\n" + text + "\n" if n == 0 else ""})
    edits.sort(key=lambda e: e["begin"])
    chunks, retained, inserted, cursor, out = [], [], {}, 0, 0
    for edit in edits:
        start, end = edit["begin"], edit["end"]
        if start < cursor:
            _fail()
        original = base["text"][cursor:start]
        retained.append({"old_begin": cursor, "old_end": start, "new_begin": out, "new_end": out + len(original)})
        chunks.append(original); out += len(original)
        if edit["replacement"]:
            inserted[edit["region_id"]] = out + 1
        chunks.append(edit["replacement"]); out += len(edit["replacement"]); cursor = end
    tail = base["text"][cursor:]
    retained.append({"old_begin": cursor, "old_end": len(base["text"]), "new_begin": out, "new_end": out + len(tail)})
    chunks.append(tail)
    return "".join(chunks), {"edits": edits, "retained": retained}, inserted


def recover_rotated_axes(page, candidates, *, language, tessdata, tesseract_command,
                         tesseract_version, traineddata, reader=None, clock=None, diagnostics=None, private_trace=None):
    from ocr_numeric_evidence import _read_tesseract
    reader, clock = reader or _read_tesseract, clock or time.monotonic
    started = clock()
    size = [float(page.rect.width), float(page.rect.height)]
    pixmap = page.get_pixmap(dpi=300, colorspace=fitz.csRGB, alpha=False)
    image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
    _size(list(image.size), integer=True)
    if private_trace is not None:
        private_trace.clear()
        private_trace.update(schema=1, stage="candidate_validation", input_pixel_sha256=_hash(image.tobytes()),
                             plans=[], regions=[])
    try:
        candidates = _candidates(candidates, size)
    except RotatedAxisError as exc:
        _record_diagnostic(diagnostics, "candidate_validation", exc.guard or "invalid_candidate_evidence")
        return None
    try:
        if private_trace is not None:
            private_trace["stage"] = "region_planning"
        plans = _select_regions(candidates, size, list(image.size), source_image=image)
    except RotatedAxisError as exc:
        geometry = {key: getattr(exc, key) for key in ("source_pixel_box", "source_word_box") if getattr(exc, key) is not None}
        _record_diagnostic(diagnostics, "region_planning", exc.guard or "not_eligible", **geometry)
        return None  # Preserve the original page rejection for ineligible input.
    runtime = _runtime(language, tesseract_version, traineddata)
    if private_trace is not None:
        private_trace.update(stage="region_recognition", plans=plans, runtime=runtime)
    regions = []
    for plan in plans:
        crop = image.crop(tuple(plan["source_pixel_box"]))
        region = {**plan, "source_crop_sha256": _hash(crop.tobytes()), "reads": []}
        if private_trace is not None:
            private_trace["regions"].append(region)
        for angle, operation in ((90, Image.Transpose.ROTATE_90), (270, Image.Transpose.ROTATE_270)):
            remaining = TIME_BUDGET - (clock() - started)
            if remaining <= 0:
                raise RotatedAxisError("rotated_axis_time_budget_exhausted")
            rotated = crop.transpose(operation)
            words = reader(rotated, language=language, tessdata=tessdata, command=tesseract_command,
                           psm=6, dpi=300, timeout_seconds=min(READ_TIMEOUT, remaining))
            exhausted = clock() - started >= TIME_BUDGET
            if exhausted and private_trace is None:
                raise RotatedAxisError("rotated_axis_time_budget_exhausted")
            try:
                words = _words(words, list(rotated.size), pixels=True)
                matrix, inverse = _transform(plan["source_pixel_box"], angle)
                region["reads"].append({"angle": angle, "image_size": list(rotated.size),
                    "input_pixel_sha256": _hash(rotated.tobytes()), "affine": matrix, "inverse_affine": inverse,
                    "words": words})
            finally:
                # Opt-in diagnostics may retain an already completed read,
                # but cannot change the original timeout exception priority.
                if exhausted:
                    raise RotatedAxisError("rotated_axis_time_budget_exhausted")
        accepted = [r for r in region["reads"] if _region_text(r["words"], r["image_size"])[2]]
        if len(accepted) != 1:
            _record_diagnostic(diagnostics, "region_recognition",
                "no_valid_direction" if not accepted else "ambiguous_directions", region=plan["id"],
                planned_region_count=len(plans), source_pixel_box=plan["source_pixel_box"],
                reads=[{"angle": r["angle"], "words": len(r["words"]),
                        "date_words": sum(bool(DATE.fullmatch(w["text"])) for w in r["words"]),
                        "accepted": _region_text(r["words"], r["image_size"])[2]} for r in region["reads"]])
            return None  # Both valid directions are ambiguous, including equal dates.
        region["selected_angle"] = accepted[0]["angle"]
        if "fragment_support" in plan:
            try:
                region["date_pixel_coverage"] = _date_pixel_coverage(crop, accepted[0])
            except RotatedAxisError:
                _record_diagnostic(diagnostics, "region_recognition", "uncovered_source_ink", region=plan["id"],
                                   planned_region_count=len(plans), source_pixel_box=plan["source_pixel_box"])
                return None
        regions.append(region)
    if private_trace is not None:
        private_trace["stage"] = "composed_readability"
    text, ledger, _ = _compose(candidates, regions)
    if not _readability(text)["accepted"]:
        _record_diagnostic(diagnostics, "composed_readability", "page_readability_rejected", planned_region_count=len(plans))
        return None
    proof = {"schema": 1, "policy": POLICY, "input_pixel_sha256": _hash(image.tobytes()),
             "page_size_points": size, "source_image_size": list(image.size), "runtime": runtime,
             "candidates": candidates, "regions": regions, "ledger": ledger,
             "primary_text_sha256": _hash(text.encode())}
    derived = replay_rotated_axis_proof(proof, text, input_pixel_sha256=proof["input_pixel_sha256"],
                page_size_points=size, source_image=image, language=language, traineddata=traineddata)
    if clock() - started >= TIME_BUDGET:
        raise RotatedAxisError("rotated_axis_time_budget_exhausted")
    if private_trace is not None:
        private_trace["stage"] = "complete"
    return {"primary_text": text, "primary_words": derived["primary_words"], "proof": proof}


def replay_rotated_axis_proof(proof, primary_text, *, input_pixel_sha256, page_size_points,
                              source_image=None, image_path=None, language=None, traineddata=None):
    from ocr_numeric_evidence import _align_mentions, _word_mentions, numeric_mentions
    keys = {"schema", "policy", "input_pixel_sha256", "page_size_points", "source_image_size", "runtime",
            "candidates", "regions", "ledger", "primary_text_sha256"}
    if (not isinstance(proof, dict) or set(proof) != keys or type(proof["schema"]) is not int or proof["schema"] != 1
            or proof["policy"] != POLICY or len(_canonical(proof)) > MAX_PROOF_BYTES
            or not isinstance(input_pixel_sha256, str) or not HASH.fullmatch(input_pixel_sha256)
            or proof["input_pixel_sha256"] != input_pixel_sha256
            or _canonical(proof["page_size_points"]) != _canonical(page_size_points)):
        _fail()
    size, image_size = _size(proof["page_size_points"]), _size(proof["source_image_size"], integer=True)
    runtime = proof["runtime"]
    if not isinstance(runtime, dict):
        _fail()
    expected_runtime = _runtime(runtime.get("languages"), runtime.get("tesseract_version"), runtime.get("traineddata"))
    if (_canonical(runtime) != _canonical(expected_runtime) or (language is not None and runtime["languages"] != language)
            or (traineddata is not None and _canonical(runtime["traineddata"]) != _canonical(traineddata))):
        _fail()
    candidates = _candidates(proof["candidates"], size)
    if _canonical(candidates) != _canonical(proof["candidates"]):
        _fail()
    if image_path is not None and source_image is None:
        path = Path(image_path)
        if path.is_symlink() or not path.is_file():
            _fail()
        with Image.open(path) as loaded:
            if loaded.width * loaded.height > MAX_PIXELS:
                _fail()
            source_image = loaded.convert("RGB")
    if source_image is None or not isinstance(source_image, Image.Image) or (source_image.mode != "RGB" or list(source_image.size) != image_size
                                    or _hash(source_image.tobytes()) != input_pixel_sha256):
        _fail()
    plans = _select_regions(candidates, size, image_size, source_image=source_image)
    regions = proof["regions"]
    if not isinstance(regions, list) or len(regions) != len(plans):
        _fail()
    for region, plan in zip(regions, plans):
        coverage_keys = {"date_pixel_coverage"} if "fragment_support" in plan else set()
        if (not isinstance(region, dict) or set(region) != set(plan) | {"source_crop_sha256", "reads", "selected_angle"} | coverage_keys
                or any(_canonical(region[k]) != _canonical(v) for k, v in plan.items())
                or not isinstance(region["source_crop_sha256"], str) or not HASH.fullmatch(region["source_crop_sha256"])
                or type(region["selected_angle"]) is not int or region["selected_angle"] not in (90, 270)
                or not isinstance(region["reads"], list) or len(region["reads"]) != 2):
            _fail()
        crop = source_image.crop(tuple(plan["source_pixel_box"])) if source_image is not None else None
        if crop is not None and _hash(crop.tobytes()) != region["source_crop_sha256"]:
            _fail()
        accepted = []
        for read, angle in zip(region["reads"], (90, 270)):
            matrix, inverse = _transform(plan["source_pixel_box"], angle)
            expected_size = [plan["source_pixel_box"][3] - plan["source_pixel_box"][1],
                             plan["source_pixel_box"][2] - plan["source_pixel_box"][0]]
            if (not isinstance(read, dict) or set(read) != {"angle", "image_size", "input_pixel_sha256", "affine", "inverse_affine", "words"}
                    or type(read["angle"]) is not int or read["angle"] != angle or _canonical(read["image_size"]) != _canonical(expected_size)
                    or _canonical(read["affine"]) != _canonical(matrix) or _canonical(read["inverse_affine"]) != _canonical(inverse)
                    or not isinstance(read["input_pixel_sha256"], str) or not HASH.fullmatch(read["input_pixel_sha256"])):
                _fail()
            words = _words(read["words"], expected_size, pixels=True)
            if _canonical(words) != _canonical(read["words"]):
                _fail()
            if crop is not None:
                rotated = crop.transpose(Image.Transpose.ROTATE_90 if angle == 90 else Image.Transpose.ROTATE_270)
                if _hash(rotated.tobytes()) != read["input_pixel_sha256"]:
                    _fail()
            if _region_text(words, expected_size)[2]:
                accepted.append(angle)
        if accepted != [region["selected_angle"]]:
            _fail()
        if coverage_keys:
            selected_read = next(read for read in region["reads"] if read["angle"] == region["selected_angle"])
            if _canonical(region["date_pixel_coverage"]) != _canonical(_date_pixel_coverage(crop, selected_read)):
                _fail()
    selected, ledger, inserted = _compose(candidates, regions)
    if (selected != primary_text or _canonical(proof["ledger"]) != _canonical(ledger)
            or proof["primary_text_sha256"] != _hash(selected.encode()) or not _readability(selected)["accepted"]):
        _fail()
    base = candidates["source-flow"]
    base_mentions = numeric_mentions(base["text"])
    original = _align_mentions(base_mentions, _word_mentions(base["words"]))
    mentions = numeric_mentions(selected)
    by_span = {(row["begin"], row["end"]): i for i, row in enumerate(mentions)}
    positioned, rotated_mentions = {}, {}
    for index, row in original.items():
        # The positioned mention's offsets belong to its reconstructed line.
        # Only primary occurrences have global transcript offsets for ledger
        # migration; the independent alignment supplies just the source box.
        original_mention = base_mentions[index]
        for retained in ledger["retained"]:
            if retained["old_begin"] <= original_mention["begin"] and original_mention["end"] <= retained["old_end"]:
                delta = retained["new_begin"] - retained["old_begin"]
                new_index = by_span.get((original_mention["begin"] + delta, original_mention["end"] + delta))
                if new_index is not None and not any(_intersects(row["bbox"], [r["source_pixel_box"][0] * size[0] / image_size[0],
                        r["source_pixel_box"][1] * size[1] / image_size[1], r["source_pixel_box"][2] * size[0] / image_size[0],
                        r["source_pixel_box"][3] * size[1] / image_size[1]]) for r in regions):
                    positioned[new_index] = {**mentions[new_index], "bbox": row["bbox"]}
                break
    removed = {i for r in regions for i in r["source_word_indices"]}
    primary_words = [w for i, w in enumerate(base["words"]) if i not in removed]
    for region in regions:
        read = next(r for r in region["reads"] if r["angle"] == region["selected_angle"])
        text, spans, _ = _region_text(read["words"])
        for start, end, i in spans:
            word = read["words"][i]
            whole = _quad(word["bbox"], read["affine"], image_size, size)
            q = whole["source_quad"]
            primary_words.append({**word, "bbox": [min(p[0] for p in q), min(p[1] for p in q), max(p[0] for p in q), max(p[1] for p in q)]})
            for local in numeric_mentions(text[start:end]):
                begin, finish = start + local["begin"], start + local["end"]
                index = by_span.get((inserted[region["id"]] + begin, inserted[region["id"]] + finish))
                if index is None:
                    _fail()
                x0, y0, x1, y1 = word["bbox"]
                width = x1 - x0
                field_box = [x0 + width * local["begin"] / len(word["text"]), y0,
                             x0 + width * local["end"] / len(word["text"]), y1]
                rotated_mentions[index] = {"policy": POLICY, "region_id": region["id"], "word_index": i,
                    "word_begin": local["begin"], "word_end": local["end"],
                    **_quad(field_box, read["affine"], image_size, size)}
    if set(positioned) & set(rotated_mentions):
        _fail()
    return {"positioned": positioned, "rotated_mentions": rotated_mentions, "primary_words": primary_words}
