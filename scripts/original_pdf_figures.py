"""Source-bound original PDF crops for OCR article continuations.

Text remains explicitly OCR. These images are rendered from the authenticated
original, never from model-generated chart specifications or editorial art.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import re

SIDECAR = 'source_original_figures.json'
LEGACY_POLICY = 'original-pdf-figures-v1'
POLICY = 'original-pdf-figures-v2'
DPI = 180
MAX_IMAGES = 3
MAX_PIXELS = 40_000_000
MAX_PDF_BYTES = 128 * 1024 * 1024
CAPTION = re.compile(r'(?im)^\s*(?:exhibit|figure|fig\.?|chart|table|图表?|表)\s*(?:\d+|[一二三四五六七八九十]+)(?!\d)')
FURNITURE = re.compile(r'(?im)^\s*(?:table of contents|contents|免责声明|分析师声明|目录|disclosures?|disclaimer)\s*[:：]?\s*$')


def _scanned_data_page(page, text):
    """Recognize unnumbered plot grids and financial snapshots in scans.

    The result authorizes original page context only. It does not reconstruct
    chart values or treat prose/phone numbers as a data table.
    """
    import fitz
    images = page.get_image_info()
    if not any((fitz.Rect(row['bbox']) & page.rect).get_area() >= .7 * page.rect.get_area()
               and row.get('width', 0) >= 500 and row.get('height', 0) >= 500 for row in images):
        return False
    numbers = re.findall(r'(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*', text)
    if len(numbers) < 12:
        return False
    # Only standalone appendix headings qualify; a research page's short
    # footer pointing to disclosures must not hide its financial tables.
    heading = re.search(r'(?im)^\s*(?:analyst certification|issuer specific regulatory disclosures|'
                        r'important disclosures|other disclosures|disclosure appendix|disclosure section)\s*[:：]?\s*$', text[:1200])
    if heading:
        from mineru_figure_sources import _cues
        if sum(bool(value) for name, value in _cues(text).items() if name != 'banking_clients') >= 2:
            return False
    financial = bool(re.search(r'(?i)\b(?:EPS|EBITDA|net\s+income|revenue)\b', text))
    fiscal = bool(re.search(r'(?i)\bfiscal\s*year(?:\s+ending)?\b|\byear\s+ending\b', text))
    snapshot = sum(bool(re.search(pattern, text, re.I)) for pattern in
        (r'\b(?:mkt|market)\s*cap\b', r'52[ -]*week', r'\bavg\.?\s*daily\s*trading',
         r'\bEV\s*/\s*(?:revenue|EBITDA)', r'\bsh\s+out\b', r'\bindustry\s+view\b'))
    if financial and (fiscal or snapshot >= 2):
        return True
    sources = len(re.findall(r'(?i)\bsources?\s*[:：]|来源\s*[:：]', text))
    units = bool(re.search(r'(?i)%|\b(?:index|yoy|qoq|mom|3mma|percent)\b|同比|环比|指数', text))
    numeric_lines = sum(len(line) <= 85 and bool(re.search(r'\d', line))
                        for line in text.splitlines() if line.strip())
    density = sum(char.isdigit() for char in text) / max(1, len(re.sub(r'\s', '', text)))
    return units and sources > 0 and (sources >= 2 or numeric_lines >= 5 or density >= .12)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(',', ':')).encode() + b'\n'


def require(condition):
    if not condition:
        raise ValueError('original_figure_evidence_invalid')


def extract(pdf, pages, *, source_sha256, maximum=MAX_IMAGES, policy=POLICY):
    import fitz
    from mineru_figure_sources import _silent_mupdf
    from market_views_source_digest import _chart_regions
    require(isinstance(pdf, bytes) and pdf.startswith(b'%PDF-') and len(pdf) <= MAX_PDF_BYTES
            and isinstance(source_sha256, str) and re.fullmatch(r'[a-f0-9]{64}', source_sha256)
            and type(maximum) is int and 1 <= maximum <= MAX_IMAGES and policy in {POLICY, LEGACY_POLICY})
    candidates, files = [], {}
    with _silent_mupdf(), fitz.open(stream=pdf, filetype='pdf') as document:
        require(not document.needs_pass and 0 < len(document) <= 1000 and len(pages) == len(document))
        for index, page in enumerate(document):
            text = pages[index]['text']
            require(isinstance(text, str) and pages[index]['page'] == index + 1)
            if FURNITURE.search(text[:500]):
                continue
            regions = _chart_regions(page)
            # A scanned/table page can have one full-page bitmap or no vector
            # plot at all. Preserve its original chart context only when the
            # verified page text identifies a numbered exhibit with data.
            mode = 'original_pdf_crop'
            if not regions and ((CAPTION.search(text) and len(re.findall(r'\d+(?:\.\d+)?', text)) >= 4)
                    or (policy == POLICY and _scanned_data_page(page, text))):
                regions = [page.rect]
                mode = 'original_pdf_chart_page'
            for region in regions:
                region = (region + (-16, -24, 16, 20)) & page.rect
                require(not region.is_empty and not region.is_infinite)
                candidates.append({'page': index + 1, 'bbox': list(region),
                                   'page_size': [page.rect.width, page.rect.height], 'kind': mode})
        # Spread the bounded article selection over chart pages rather than
        # choosing multiple pieces of the first page's same plot.
        first_per_page = list({row['page']: row for row in reversed(candidates)}.values())
        first_per_page.sort(key=lambda row: row['page'])
        chosen = first_per_page[:maximum]
        if len(chosen) < maximum:
            chosen += [row for row in candidates if row not in chosen][:maximum - len(chosen)]
        chosen.sort(key=lambda row: (row['page'], row['bbox'][1], row['bbox'][0]))
        assets, pixels = [], 0
        for number, candidate in enumerate(chosen, 1):
            region = fitz.Rect(candidate['bbox'])
            pixels += math.ceil(region.width * DPI / 72) * math.ceil(region.height * DPI / 72)
            require(pixels <= MAX_PIXELS)
            pixmap = document[candidate['page'] - 1].get_pixmap(
                dpi=DPI, clip=region, colorspace=fitz.csRGB, alpha=False)
            raw = pixmap.tobytes('png')
            path = f'assets/source_image_{number:02d}.png'
            files[path] = raw
            assets.append({**candidate, 'path': path, 'sha256': digest(raw), 'bytes': len(raw),
                           'width': pixmap.width, 'height': pixmap.height,
                           'rgb_sha256': digest(pixmap.samples)})
        evidence = {'schema': 1, 'policy': policy, 'original_pdf_sha256': digest(pdf),
                    'source_sha256': source_sha256, 'page_count': len(document), 'dpi': DPI, 'max_images': maximum,
                    'candidate_count': len(candidates), 'candidate_pages': sorted({r['page'] for r in candidates}),
                    'assets': assets}
    return evidence, files


def validate(evidence, loader, *, original_pdf_sha256, source_sha256, pdf=None, pages=None):
    from PIL import Image
    import io
    require(isinstance(evidence, dict) and set(evidence) == {'schema', 'policy', 'original_pdf_sha256',
            'source_sha256', 'page_count', 'dpi', 'max_images', 'candidate_count', 'candidate_pages', 'assets'}
            and evidence['schema'] == 1 and evidence['policy'] in {POLICY, LEGACY_POLICY} and evidence['dpi'] == DPI
            and evidence['original_pdf_sha256'] == original_pdf_sha256
            and evidence['source_sha256'] == source_sha256
            and type(evidence['max_images']) is int and 1 <= evidence['max_images'] <= MAX_IMAGES
            and type(evidence['page_count']) is int and 1 <= evidence['page_count'] <= 1000
            and type(evidence['candidate_count']) is int and 0 <= evidence['candidate_count'] <= 2000
            and isinstance(evidence['candidate_pages'], list)
            and evidence['candidate_pages'] == sorted(set(evidence['candidate_pages']))
            and all(type(p) is int and 1 <= p <= evidence['page_count'] for p in evidence['candidate_pages'])
            and len(evidence['candidate_pages']) <= evidence['candidate_count']
            and isinstance(evidence['assets'], list)
            and len(evidence['assets']) == min(evidence['max_images'], evidence['candidate_count']))
    seen = set()
    for index, asset in enumerate(evidence['assets'], 1):
        require(isinstance(asset, dict) and asset.get('path') == f'assets/source_image_{index:02d}.png'
                and asset.get('kind') in {'original_pdf_crop', 'original_pdf_chart_page'}
                and type(asset.get('page')) is int and asset.get('page') in evidence['candidate_pages'] and asset['path'] not in seen
                and type(asset.get('bytes')) is int and 0 < asset['bytes'] <= 64 * 1024 * 1024
                and isinstance(asset.get('bbox'), list) and len(asset['bbox']) == 4
                and isinstance(asset.get('page_size'), list) and len(asset['page_size']) == 2
                and all(type(v) in (float, int) and math.isfinite(v)
                        for v in asset['bbox'] + asset['page_size']))
        x0, y0, x1, y1 = asset['bbox']; width, height = asset['page_size']
        require(0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height)
        raw = loader(asset['path'])
        require(len(raw) == asset.get('bytes') and digest(raw) == asset.get('sha256'))
        with Image.open(io.BytesIO(raw)) as image:
            require(image.size == (asset.get('width'), asset.get('height'))
                    and image.width * image.height <= MAX_PIXELS
                    and digest(image.convert('RGB').tobytes()) == asset.get('rgb_sha256'))
        seen.add(asset['path'])
    if pdf is not None:
        require(digest(pdf) == original_pdf_sha256 and pages is not None)
        rebuilt, rendered = extract(pdf, pages, source_sha256=source_sha256,
                                    maximum=evidence['max_images'], policy=evidence['policy'])
        require(rebuilt == evidence and all(loader(path) == raw for path, raw in rendered.items()))
    return [asset['path'] for asset in evidence['assets']]


def write(directory, evidence, files):
    directory = Path(directory)
    require(not directory.is_symlink())
    for name, raw in {**files, SIDECAR: encode(evidence)}.items():
        target = directory / name
        require(not target.is_symlink() and not target.parent.is_symlink())
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    mapping = {'version': 1, 'source_sha256': evidence['source_sha256'],
               'images': {asset['path']: asset['path'] for asset in evidence['assets']}}
    (directory / 'source_image_map.json').write_bytes(encode(mapping))


def admitted(directory):
    from report_extraction_source import resolve_extraction_source
    directory = Path(directory)
    source = resolve_extraction_source(directory)
    status = json.loads((directory / 'status.json').read_bytes())
    sidecar = directory / SIDECAR
    require(not sidecar.is_symlink() and sidecar.is_file())
    raw = sidecar.read_bytes()
    require(len(raw) <= 2 * 1024 * 1024 and digest(raw) == status.get('original_figures_sha256'))
    evidence = json.loads(raw)
    def load(name):
        path = directory / name
        require(not path.is_symlink() and not path.parent.is_symlink() and path.is_file()
                and path.stat().st_size <= 64 * 1024 * 1024)
        return path.read_bytes()
    refs = validate(evidence, load, original_pdf_sha256=status.get('original_pdf_sha256'), source_sha256=source.sha256)
    require(status.get('images') == refs and status.get('chart_source_image_count') == len(refs))
    mapping = directory / 'source_image_map.json'
    require(not mapping.is_symlink() and json.loads(mapping.read_bytes()) == {
        'version': 1, 'source_sha256': source.sha256, 'images': {ref: ref for ref in refs}})
    return [directory / ref for ref in refs]
