"""Local image admission for article media, separate from trailing contact art."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import re

from PIL import Image, ImageChops, ImageDraw, ImageOps, ImageStat

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTACT_IMAGE_NAMES = re.compile(r"(?:zsxq[_-]?img|(?:member[_-]?)?contact[_-]?card|(?:wechat[_-]?)?qr[_-]?code)", re.I)


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
    try:
        with Image.open(path) as image:
            image.load()
            if min(image.size) < 64:
                return "undersized"
            preview = _preview(image)
    except (OSError, ValueError, Image.DecompressionBombError):
        return "unreadable"
    for contact in _contact_previews():
        if max(ImageStat.Stat(ImageChops.difference(preview, contact)).mean) < 6:
            return "contact_card"
    for placeholder in _placeholder_previews():
        if max(ImageStat.Stat(ImageChops.difference(preview, placeholder)).mean) < 6:
            return "legacy_placeholder"
    return ""


def is_article_image_candidate(path: Path) -> bool:
    return not article_image_rejection(path)
