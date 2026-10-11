"""Local image admission for article media, separate from trailing contact art."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import hashlib
import json
import re

from PIL import Image, ImageChops, ImageDraw, ImageOps, ImageStat

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTACT_IMAGE_NAMES = re.compile(r"(?:zsxq[_-]?img|(?:member[_-]?)?contact[_-]?card|(?:wechat[_-]?)?qr[_-]?code)", re.I)
SOURCE_IMAGE_NAME = re.compile(r"source_image_\d{2,}\.(?:png|jpe?g|webp|gif|bmp|tiff?)", re.I)
FURNITURE_ROLES = {"cover", "cover_page", "title_page", "title_card", "generated_cover", "table_of_contents", "toc", "contact_card", "qr_code", "page_render", "pdf_page"}


def is_publication_furniture_metadata(record: dict) -> bool:
    for key in ("role", "kind", "type", "media_role", "source_kind"):
        value = str(record.get(key) or "").strip().lower().replace("-", "_")
        if value in FURNITURE_ROLES:
            return True
    # Exact producer labels only; ordinary chart captions mentioning a report
    # page or company contact must not become exclusion heuristics.
    for key in ("title", "label", "caption", "body_text"):
        if str(record.get(key) or "").strip().lower() in {"contents", "table of contents", "目录", "目錄", "contact information"}:
            return True
    for key in ("source_path", "relative_path", "path"):
        path = Path(str(record.get(key) or ""))
        if path.parent.name == "assets" and (path.stem.lower() == "cover" or re.fullmatch(r"xhs_card_\d+", path.stem, re.I)):
            return True
    return False


def source_chart_images(report_dir: Path) -> list[Path]:
    """Read retained MinerU exhibits, never generated page/title/card artwork.

    A present source map limits the set to its source-bound assets, so stale
    files left by an earlier generation cannot silently become article art.
    Authentication of the original handoff remains the producer's contract.
    """
    report_dir = Path(report_dir)
    assets = report_dir / "assets"
    if assets.is_symlink() or not assets.is_dir():
        return []
    paths = sorted(assets.glob("source_image_*"))
    mapping_path = report_dir / "source_image_map.json"
    if mapping_path.exists() or mapping_path.is_symlink():
        try:
            mapping = json.loads(mapping_path.read_text())
            source = report_dir / "source_mineru.md"
            if (mapping_path.is_symlink() or source.is_symlink() or mapping.get("version") != 1
                    or mapping.get("source_sha256") != hashlib.sha256(source.read_bytes()).hexdigest()
                    or not isinstance(mapping.get("images"), dict)):
                return []
            refs = list(dict.fromkeys(mapping["images"].values()))
            if not all(isinstance(ref, str) and re.fullmatch(r"assets/source_image_\d{2,}\.(?:png|jpe?g|webp|gif|bmp|tiff?)", ref, re.I) for ref in refs):
                return []
            paths = [report_dir / ref for ref in refs]
        except (OSError, ValueError, AttributeError, TypeError):
            return []
    figure_map = report_dir / "source_figure_map.json"
    bindings = None
    if figure_map.exists() or figure_map.is_symlink():
        try:
            mapping = json.loads(figure_map.read_text())
            if figure_map.is_symlink() or not isinstance(mapping.get("assets"), list):
                return []
            records = {item["index"]: item for item in mapping.get("metadata", {}).get("records", [])}
            bindings = {item["path"]: item for item in mapping["assets"]
                        if not is_publication_furniture_metadata(item)
                        and not is_publication_furniture_metadata(records.get(item.get("index"), {}))}
        except (OSError, ValueError, TypeError, AttributeError, KeyError):
            return []
    selected = []; seen = set()
    for path in paths:
        if (not SOURCE_IMAGE_NAME.fullmatch(path.name) or path.is_symlink() or not path.is_file()
                or path.resolve().parent != assets.resolve() or not is_article_image_candidate(path)):
            continue
        identity = hashlib.sha256(path.read_bytes()).hexdigest()
        if bindings is not None:
            binding = bindings.get(path.relative_to(report_dir).as_posix())
            if not binding or binding.get("sha256") != identity:
                continue
        if identity not in seen:
            seen.add(identity); selected.append(path)
    return selected


def _generated_title_panel(image: Image.Image) -> bool:
    """Recognize the exact old make_cover geometry, including WeChat crops.

    This is deliberately not a white-area/entropy test. Require the renderer's
    four specific borders and its fixed empty interior bands simultaneously.
    Titles and PDF backgrounds are variable and never inspected as text.
    """
    width, height = image.size
    if not .73 <= width / height <= 2.40:
        return False
    rgb = image.convert("RGB")
    scale = width / 1080
    offset = (1440 * scale - height) / 2
    def light(x, y, *, border=False):
        px, py = round(x * scale), round(y * scale - offset)
        if not (1 <= px < width - 1 and 1 <= py < height - 1):
            return -1
        values = [sum(rgb.getpixel((px + dx, py + dy))) / 3
                  for dx, dy in ([(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] if border else [(0, 0)])]
        return min(values)
    white = [light(x, y) for x in (180, 320, 760, 900) for y in (535, 570, 835, 870)]
    if min(white) < 245:
        return False
    groups = [([light(x, y, border=True) for x in (220, 400, 700, 860)]) for y in (501, 899)]
    groups += [([light(x, y, border=True) for y in (550, 580, 840, 870)]) for x in (111, 969)]
    return all(min(values) >= 0 and sum(values) / len(values) < 145 for values in groups)


def _preview(image: Image.Image) -> Image.Image:
    return image.convert("RGB").resize((64, 64), Image.Resampling.LANCZOS)


@lru_cache(maxsize=1)
def _contact_previews() -> tuple[Image.Image, ...]:
    previews = []
    for path in (REPO_ROOT / "prompts/zsxq_img.jpg", REPO_ROOT / "portal_suite/site_src/assets/contact-card.jpg"):
        if not path.is_file():
            continue
        with Image.open(path) as image:
            image = image.convert("RGB")
            previews.append(_preview(image))
            for size in ((1200, 675), (940, 400), (640, 640)):
                previews.append(_preview(ImageOps.fit(image, size, method=Image.Resampling.LANCZOS)))
    return tuple(previews)


@lru_cache(maxsize=1)
def _placeholder_previews() -> tuple[Image.Image, ...]:
    """Reference pixels of the two historical fallback writers, including crops."""
    ink, gold, cream = (20, 32, 51), (201, 162, 39), (247, 243, 232)
    originals = []
    for width, height in ((1200, 675), (940, 400)):
        canvas = Image.new("RGB", (width, height), cream)
        draw = ImageDraw.Draw(canvas)
        draw.rectangle((0, 0, width, 91), fill=ink)
        draw.rectangle((0, 92, width, 113), fill=gold)
        draw.rectangle((0, 0, 33, height), fill=gold)
        originals.append(canvas)
    canvas = Image.new("RGB", (960, 640), cream)
    draw = ImageDraw.Draw(canvas, "RGBA")
    for y in range(640):
        shade = int(18 * y / 640)
        draw.line((0, y, 960, y), fill=tuple(value - shade for value in cream))
    draw.rectangle((0, 0, 960, 92), fill=(*ink, 245))
    draw.rectangle((0, 92, 960, 110), fill=(*gold, 230))
    for index in range(7):
        x, top = 95 + index * 122, 220 + (index % 3) * 34
        draw.rounded_rectangle((x, top, x + 54, 470), radius=12, outline=(*gold, 155), width=4)
        draw.ellipse((x + 12, top - 58, x + 42, top - 28), fill=(*ink, 90))
    for index in range(5):
        draw.line((110, 535 + index * 18, 850, 535 + index * 18), fill=(*ink, 48), width=4)
    originals.append(canvas)
    return tuple(_preview(candidate) for original in originals for candidate in (
        original, ImageOps.fit(original, (1200, 675)), ImageOps.fit(original, (940, 400))))


def article_image_rejection(path: Path) -> str:
    """Reject known publication furniture and synthetic placeholders, not charts.

    Contact-card copies are detected by pixels as well as filenames, including
    the cover crops produced by older uploaders. This deliberately does not use
    a generic white-space/entropy threshold: real research charts are often
    mostly white and remain valid article illustrations.
    """
    path = Path(path)
    if CONTACT_IMAGE_NAMES.search(path.stem):
        return "contact_card"
    # These reserved asset names are generated by pdf_to_xhs_batch, not PDF
    # exhibits. In particular cover.png is a blurred PDF page plus title box.
    if path.parent.name == "assets" and (path.stem.lower() == "cover" or re.fullmatch(r"xhs_card_\d+", path.stem, re.I)):
        return "generated_title_or_chart_card"
    try:
        with Image.open(path) as image:
            image.load()
            if min(image.size) < 64:
                return "undersized"
            preview = _preview(image)
            generated_title = _generated_title_panel(image)
    except (OSError, ValueError, Image.DecompressionBombError):
        return "unreadable"
    if generated_title:
        return "generated_pdf_title_card"
    for contact in _contact_previews():
        if max(ImageStat.Stat(ImageChops.difference(preview, contact)).mean) < 6:
            return "contact_card"
    for placeholder in _placeholder_previews():
        if max(ImageStat.Stat(ImageChops.difference(preview, placeholder)).mean) < 6:
            return "legacy_placeholder"
    return ""


def is_article_image_candidate(path: Path) -> bool:
    return not article_image_rejection(path)
