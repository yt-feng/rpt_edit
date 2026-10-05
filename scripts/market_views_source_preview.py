#!/usr/bin/env python3
"""Bounded, explicitly degraded original-page edition; no OCR or model calls."""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

import fitz

from extract_native_market_sources import read_manifest, _original_inventory


TITLE = "Market Views 备用来源版（解析服务异常）"
SCHEMA = "market-views-source-preview-v1"
MAX_PAGES = 120
MAX_BYTES = 64 * 1024 * 1024
MAX_SCAN_PAGES = 20
MARKET_WORDS = re.compile(r"market|outlook|investment|econom|equity|bond|rate|inflation|valuation|forecast|市场|展望|投资|经济|利率|估值|预测", re.I)
TEXT_FONT_NAME = "SourcePreviewCJK"


@lru_cache(maxsize=1)
def _text_font_buffer():
    # MuPDF ships this font. Embed its bytes instead of relying on a reader's
    # optional Adobe-GB1 CJK package (the built-in china-s alias is unembedded).
    return fitz.Font("cjk").buffer


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def context(date, run_id, sha):
    if not re.fullmatch(r"[0-9]{6,8}", date) or not re.fullmatch(r"[1-9][0-9]*", run_id) or not re.fullmatch(r"[a-f0-9]{40}", sha):
        raise ValueError("Invalid source preview provenance")
    return {"date": date, "producer_run_id": run_id, "execution_sha": sha}


def _selected_pages(document, limit):
    candidates = []
    for index in range(min(len(document), MAX_SCAN_PAGES)):
        page = document[index]
        if min(page.rect.width, page.rect.height) <= 0 or max(page.rect.width, page.rect.height) > 3000:
            continue
        thumbnail = page.get_pixmap(matrix=fitz.Matrix(.3, .3), colorspace=fitz.csGRAY, alpha=False)
        # Reject genuinely blank pages without requiring a recognized text layer.
        if sum(value < 245 for value in thumbnail.samples) < 20:
            continue
        score = min(30, len(MARKET_WORDS.findall(page.get_text())))
        candidates.append((-score, index))
    return sorted(index for _, index in sorted(candidates)[:limit])


def prepare(input_dir, manifest, output_dir, expected_reports, *, date, run_id, sha):
    """Bind exact PDFs, then retain at most two readable page images per report."""
    provenance = context(date, run_id, sha)
    raw_manifest, bindings = read_manifest(Path(manifest), expected_reports)
    originals = _original_inventory(Path(input_dir))
    if set(originals) != {row["source_pdf"] for row in bindings}:
        raise ValueError("Original PDF inventory differs from the selected manifest")
    output = Path(output_dir)
    if output.exists() or output.is_symlink():
        raise ValueError("Preview destination must be new")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent, prefix=".source-preview-") as temporary:
        root = Path(temporary) / "preview"
        root.mkdir()
        (root / "selected_to_process_manifest.json").write_bytes(raw_manifest)
        rows, page_count, total_bytes = [], 0, 0
        limit = max(1, min(2, MAX_PAGES // expected_reports))
        for index, binding in enumerate(bindings, 1):
            original = originals[binding["source_pdf"]]
            if digest(original) != binding["content_sha256"]:
                raise ValueError("Original PDF SHA-256 differs from the selected manifest")
            row = {**binding, "pages": [], "source_page_count": 0, "status": "not_rendered"}
            if page_count >= MAX_PAGES:
                row["status"] = "page_budget"
                rows.append(row)
                continue
            try:
                document = fitz.open(original)
            except Exception:
                row["status"] = "unreadable_pdf"
                rows.append(row)
                continue
            with document:
                row["source_page_count"] = len(document)
                if document.is_encrypted or document.needs_pass or document.is_repaired or not len(document):
                    row["status"] = "unreadable_pdf"
                    rows.append(row)
                    continue
                for number in _selected_pages(document, min(limit, MAX_PAGES - page_count)):
                    page = document[number]
                    # Full page at up to 150 dpi; a bounded long edge avoids huge diagrams.
                    scale = min(150 / 72, 2400 / max(page.rect.width, page.rect.height))
                    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csRGB, alpha=False)
                    raw = pixmap.tobytes("jpeg", jpg_quality=85)
                    if total_bytes + len(raw) > MAX_BYTES:
                        row["status"] = "byte_budget"
                        break
                    name = f"report_{index:04d}_page_{number + 1:04d}.jpg"
                    (root / name).write_bytes(raw)
                    row["pages"].append({"page": number + 1, "image": name,
                        "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
                        "width": pixmap.width, "height": pixmap.height})
                    total_bytes += len(raw)
                    page_count += 1
                if row["pages"]:
                    row["status"] = "selected_pages"
                elif row["status"] == "not_rendered":
                    row["status"] = "no_nonblank_page_in_scan_window"
            rows.append(row)
        if not page_count:
            raise ValueError("No readable original pages available for a source edition")
        receipt = {"schema": SCHEMA, "status": "degraded", "title": TITLE,
            "source_context": provenance, "manifest_sha256": hashlib.sha256(raw_manifest).hexdigest(),
            "report_count": expected_reports, "selected_page_count": page_count,
            "selected_image_bytes": total_bytes, "scan_pages_per_report": MAX_SCAN_PAGES,
            "max_pages": MAX_PAGES, "max_bytes": MAX_BYTES, "reports": rows}
        (root / "source_preview_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
        validate(root, expected_reports, date=date, run_id=run_id, sha=sha)
        os.replace(root, output)
    return receipt


def validate(root, expected_reports, *, date, run_id, sha):
    root = Path(root)
    value = json.loads((root / "source_preview_receipt.json").read_text())
    manifest, bindings = read_manifest(root / "selected_to_process_manifest.json", expected_reports)
    if (value.get("schema") != SCHEMA or value.get("status") != "degraded" or value.get("title") != TITLE
            or value.get("source_context") != context(date, run_id, sha)
            or value.get("manifest_sha256") != hashlib.sha256(manifest).hexdigest()
            or value.get("report_count") != expected_reports or len(value.get("reports", [])) != expected_reports):
        raise ValueError("Source edition provenance differs")
    pages, size, images = 0, 0, set()
    for index, (row, binding) in enumerate(zip(value["reports"], bindings), 1):
        if any(row.get(key) != item for key, item in binding.items()) or len(row.get("pages", [])) > 2:
            raise ValueError("Source edition report binding differs")
        for page in row["pages"]:
            number = page.get("page")
            if type(number) is not int or not 1 <= number <= min(MAX_SCAN_PAGES, row["source_page_count"]):
                raise ValueError("Source edition page position differs")
            expected_name = f"report_{index:04d}_page_{number:04d}.jpg"
            if page.get("image") != expected_name or expected_name in images:
                raise ValueError("Source edition image path differs")
            image = root / expected_name
            if image.is_symlink() or not image.is_file() or digest(image) != page.get("sha256") or image.stat().st_size != page.get("bytes"):
                raise ValueError("Source edition image integrity differs")
            pix = fitz.Pixmap(str(image))
            if [pix.width, pix.height] != [page.get("width"), page.get("height")] or max(pix.width, pix.height) > 2401:
                raise ValueError("Source edition image geometry differs")
            pages += 1
            size += image.stat().st_size
            images.add(expected_name)
    if not 0 < pages <= MAX_PAGES or size > MAX_BYTES or pages != value.get("selected_page_count") or size != value.get("selected_image_bytes"):
        raise ValueError("Source edition coverage or size differs")
    return value


def _text(page, rect, text, size=11, color=(.12, .16, .22)):
    page.insert_font(fontname=TEXT_FONT_NAME, fontbuffer=_text_font_buffer())
    if page.insert_textbox(fitz.Rect(rect), text, fontname=TEXT_FONT_NAME, fontsize=size, color=color) < 0:
        raise ValueError("Source edition text does not fit")


def render(root, output, expected_reports, *, date, run_id, sha):
    from prepare_public_market_view_pdf import ENDING_PAGE_MARKER
    receipt = validate(root, expected_reports, date=date, run_id=run_id, sha=sha)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with fitz.open() as document:
        cover = document.new_page(width=595, height=842)
        _text(cover, (42, 62, 553, 170), TITLE, 24)
        _text(cover, (42, 190, 553, 450),
            f"报告批次：{date}\n\n主解析或摘要流程未完成。本版仅保留来源目录和原报告页面图片，"
            "没有生成或验证投资观点、OCR 数值或摘要。请直接阅读原页，并以原始报告为准。\n\n"
            f"覆盖：{expected_reports} 份选定来源中，{sum(bool(r['pages']) for r in receipt['reports'])} 份提供了页图，"
            f"共 {receipt['selected_page_count']} 页。每份最多 2 页；只从前 {MAX_SCAN_PAGES} 页中优先选择有市场相关文字的非空页。"
            "扫描件按原页次序选取，未覆盖全文，不代表完整研判。", 12)
        _text(cover, (42, 620, 553, 765), f"来源运行：{run_id}\n代码版本：{sha}\n原文件 SHA-256 和原页位置见下页目录。\n状态：degraded / source pages only", 10)
        for start in range(0, len(receipt["reports"]), 7):
            page = document.new_page(width=595, height=842)
            _text(page, (35, 25, 560, 65), "备用来源版 - 来源与覆盖目录", 17)
            for offset, row in enumerate(receipt["reports"][start:start + 7]):
                top = 82 + offset * 101
                name = row["source_pdf"]
                # Full names remain in the private receipt; the printed identity is the complete hash.
                label = name if len(name) <= 110 else name[:107] + "..."
                selected = ", ".join(str(p["page"]) for p in row["pages"]) or "未选入"
                _text(page, (35, top, 560, top + 96),
                    f"{start + offset + 1}. {label}\nSHA-256: {row['content_sha256']}\n"
                    f"原报告页数：{row['source_page_count'] or '未读取'}；选入页：{selected}；状态：{row['status']}", 9)
        for index, row in enumerate(receipt["reports"], 1):
            for selected in row["pages"]:
                page = document.new_page(width=595, height=842)
                _text(page, (26, 14, 569, 53), "备用来源版（解析服务异常）- 原页图片，非已验证摘要", 10)
                page.insert_image(fitz.Rect(22, 61, 573, 770), filename=str(Path(root) / selected["image"]), keep_proportion=True)
                _text(page, (26, 783, 569, 831),
                    f"来源 {index} / 原报告第 {selected['page']} 页；仅部分覆盖\nSHA-256: {row['content_sha256']}", 8)
        end = document.new_page(width=595, height=842)
        _text(end, (40, 80, 550, 140), "备用来源版", 16)
        end.insert_text((40, 180), ENDING_PAGE_MARKER, fontname="helv", fontsize=16)
        document.set_metadata({"title": f"{TITLE} {date}", "author": "", "subject": "degraded source-page edition"})
        temporary = output.with_name(output.name + ".tmp")
        document.subset_fonts()
        document.save(temporary, garbage=4, deflate=True)
    verify_pdf(temporary, receipt["selected_page_count"])
    os.replace(temporary, output)
    return {"status": "degraded", "source_pages": receipt["selected_page_count"], "pdf_bytes": output.stat().st_size, "pdf_sha256": digest(output)}


def verify_pdf(path, minimum_source_pages=1):
    if not 1024 < Path(path).stat().st_size <= MAX_BYTES + 2 * 1024 * 1024:
        raise ValueError("Source edition PDF size outside bounds")
    with fitz.open(path) as document:
        if document.is_repaired or document.is_encrypted or len(document) < minimum_source_pages + 2:
            raise ValueError("Source edition PDF cannot be opened completely")
        if "备用来源版" not in document[0].get_text():
            raise ValueError("Source edition label is missing")
        if sum(bool(page.get_images()) for page in document) < minimum_source_pages:
            raise ValueError("Source edition original images are missing")
        embedded_fonts = set()
        for page in document:
            text_fonts = [font for font in page.get_fonts() if font[4] == TEXT_FONT_NAME]
            if len(text_fonts) != 1:
                raise ValueError("Source edition portable label font is missing")
            xref = text_fonts[0][0]
            if xref not in embedded_fonts:
                if not document.extract_font(xref)[3]:
                    raise ValueError("Source edition label font is not embedded")
                embedded_fonts.add(xref)
            pixmap = page.get_pixmap(matrix=fitz.Matrix(.2, .2), alpha=False)
            if not pixmap.samples:
                raise ValueError("Source edition contains an unrenderable page")


def readable_pdf(path):
    try:
        if Path(path).stat().st_size <= 1024:
            return False
        with fitz.open(path) as document:
            if not len(document) or document.is_repaired or document.needs_pass:
                return False
            return all(page.get_pixmap(matrix=fitz.Matrix(.2, .2), alpha=False).samples for page in document)
    except (OSError, RuntimeError, ValueError):
        return False


def degraded_pdf(path):
    try:
        with fitz.open(path) as document:
            return "degraded source-page edition" in document.metadata.get("subject", "") or "备用来源版" in document[0].get_text()
    except (OSError, RuntimeError, ValueError):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "validate", "render"))
    parser.add_argument("--input-dir", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--expected-reports", type=int, required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--producer-run-id", required=True)
    parser.add_argument("--execution-sha", required=True)
    args = parser.parse_args()
    kwargs = {"date": args.date, "run_id": args.producer_run_id, "sha": args.execution_sha}
    if args.mode == "prepare":
        result = prepare(args.input_dir, args.manifest, args.source_dir, args.expected_reports, **kwargs)
    elif args.mode == "render":
        result = render(args.source_dir, args.pdf, args.expected_reports, **kwargs)
    else:
        result = validate(args.source_dir, args.expected_reports, **kwargs)
    print(json.dumps({key: result[key] for key in ("status", "report_count", "selected_page_count", "pdf_bytes", "pdf_sha256") if key in result}))


if __name__ == "__main__":
    main()
