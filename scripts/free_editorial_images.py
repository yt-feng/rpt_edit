"""Bounded, licensed Commons photos with an original offline editorial fallback.

Only fixed public topic words leave this module. Titles are classified locally;
neither titles nor article bodies are sent to the image search service.
"""
from __future__ import annotations

import hashlib
import html
from html.parser import HTMLParser
import io
import json
import math
from pathlib import Path
import random
import re
import tempfile
import time
from urllib.parse import urlsplit

from PIL import Image, ImageDraw, ImageOps
import requests
from requests.exceptions import RequestException, SSLError

API_URL = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "PortalSuiteEditorialImages/1.0"
MAX_IMAGE_BYTES = 8 * 1024 * 1024
MAX_JSON_BYTES = 512 * 1024
MAX_PIXELS = 20_000_000
CACHE_TTL = 24 * 60 * 60
_SEARCH_CACHE: dict[str, tuple[float, list[dict]]] = {}
_USED: dict[str, set[str]] = {}
_COOLDOWN_UNTIL = 0.0
_COOLDOWN_REASON = ""
OUTAGE_COOLDOWN_SECONDS = 300
_TOPICS = (
    ("technology", "semiconductor microchip", r"芯片|半导体|存储|晶圆|tdk|marvell|samsung|三星|科技|人工智能|数据中心|\bai\b|semiconductor|memory|technology|data cent|software|软件|电子"),
    ("energy", "solar panels wind turbines", r"能源|电力|电网|电池|太阳能|石油|天然气|核电|energy|power|solar|wind|oil|gas|battery"),
    ("industry", "industrial factory automation", r"工业|制造|机械|金属|矿|铜|钢|铝|机器人|工业|industry|industrial|mining|metal|factory|manufactur"),
    ("transport", "container cargo port", r"运输|物流|货运|航运|航空|汽车|rail|transport|cargo|shipping|port|airline|automotive"),
    ("health", "medical laboratory equipment", r"医疗|医药|药物|生物|医院|health|medical|pharma|biotech|medicine"),
    ("consumer", "retail shopping storefront", r"消费|零售|电商|酒店|旅行|旅游|食品|餐饮|consumer|retail|shopping|hotel|travel|food"),
    ("finance", "city financial district skyline", r"银行|金融|利率|宏观|基金|股|投资|市场|经济|bank|financ|market|econom|equity|invest|yield"),
)


def _topic(title: str) -> tuple[str, str]:
    for name, query, pattern in _TOPICS:
        if re.search(pattern, str(title), re.I):
            return name, query
    return "finance", "city financial district skyline"


class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def _plain(value: object) -> str:
    parser = _Text()
    parser.feed(str(value or "")[:8000])
    return " ".join(" ".join(parser.parts).split())[:240]


def _allowed_url(url: str, hosts: set[str]) -> bool:
    try:
        parsed = urlsplit(str(url))
        return (parsed.scheme == "https" and parsed.hostname in hosts
                and parsed.port in (None, 443) and not parsed.username
                and not parsed.password and not parsed.fragment
                and "\\" not in url and not any(ord(c) < 33 for c in url))
    except (ValueError, TypeError):
        return False


def _license(info: dict) -> dict | None:
    raw = info.get("extmetadata")
    if not isinstance(raw, dict):
        return None

    def field(key):
        item = raw.get(key, {})
        return _plain(item.get("value", "")) if isinstance(item, dict) else ""

    url = field("LicenseUrl")
    if url.startswith("//"):
        url = "https:" + url
    elif url.startswith("http://"):
        url = "https://" + url[len("http://"):]
    if not _allowed_url(url, {"creativecommons.org", "www.creativecommons.org"}):
        return None
    parsed = urlsplit(url)
    if parsed.query:
        return None
    path = parsed.path.rstrip("/")
    short = field("LicenseShortName").lower().replace("-", " ")
    if path == "/publicdomain/zero/1.0" and short in ("cc0", "cc0 1.0", "cc0 1.0 universal"):
        name = "CC0 1.0"
    else:
        match = re.fullmatch(r"/licenses/by/(2\.0|2\.5|3\.0|4\.0)", path)
        if not match or short != "cc by " + match[1]:
            return None
        name = "CC BY " + match[1]
    # Do not silently pick the permissive URL when the other metadata fields
    # say something different. Commons may omit License, so the explicit URL
    # and ShortName remain the minimum required pair.
    canonical = field("License").lower().replace("_", "-")
    allowed_codes = {"", "cc0", "cc-zero", "cc0-1.0", "cc-zero-1.0"} if name == "CC0 1.0" else {
        "", "cc-by", "cc-by-" + name.removeprefix("CC BY ")}
    usage = field("UsageTerms").lower()
    if canonical not in allowed_codes or re.search(r"non[ -]?commercial|no[ -]?deriv|share[ -]?alike|\bby[ -](?:nc|nd|sa)\b", usage):
        return None
    author = field("Artist")
    if not author and name != "CC0 1.0":
        return None
    source = str(info.get("descriptionurl", ""))
    if not _allowed_url(source, {"commons.wikimedia.org"}) or not urlsplit(source).path.startswith("/wiki/File:"):
        return None
    return {"author": author or "Unknown creator", "source_url": source,
            "license": name, "license_url": "https://creativecommons.org" + path + "/"}


def attribution_caption(metadata: dict) -> str:
    if metadata.get("source") == "local_editorial":
        return "主题示意图：Portal Suite 原创插画，非实拍或数据图。"
    author = _plain(metadata.get("author", ""))
    license_name = _plain(metadata.get("license", ""))
    return f"主题配图：{author} / Wikimedia Commons / {license_name}；已裁剪与缩放，非报告原图。"


def attribution_html(metadata: dict) -> str:
    """A small safe credit line; untrusted metadata HTML is never preserved."""
    caption = html.escape(attribution_caption(metadata))
    if metadata.get("source") == "local_editorial":
        return f'<p class="image-credit" data-editorial-credit="1">{caption}</p>'
    source = str(metadata.get("source_url", ""))
    license_url = str(metadata.get("license_url", ""))
    links = []
    if _allowed_url(source, {"commons.wikimedia.org"}):
        links.append(f'<a href="{html.escape(source, quote=True)}">图片来源</a>')
    if _allowed_url(license_url, {"creativecommons.org"}):
        links.append(f'<a href="{html.escape(license_url, quote=True)}">许可</a>')
    suffix = " · ".join(links)
    return f'<p class="image-credit" data-editorial-credit="1">{caption}{" " + suffix if suffix else ""}</p>'


def _atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".editorial-", delete=False) as f:
        temporary = Path(f.name)
        f.write(data)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


class _ProviderCooldown(RuntimeError):
    pass


class _DeadlineExceeded(TimeoutError):
    pass


def _record_outage(exc: Exception) -> None:
    global _COOLDOWN_UNTIL, _COOLDOWN_REASON
    _COOLDOWN_REASON = "commons_tls_failed" if isinstance(exc, SSLError) else "commons_unavailable"
    _COOLDOWN_UNTIL = time.monotonic() + OUTAGE_COOLDOWN_SECONDS


def _read_response(session, url: str, *, deadline: float, limit: int,
                   hosts: set[str], params: dict | None = None) -> tuple[bytes, str]:
    if time.monotonic() < _COOLDOWN_UNTIL:
        raise _ProviderCooldown(_COOLDOWN_REASON)
    for _ in range(3):
        if not _allowed_url(url, hosts):
            raise ValueError("untrusted_url")
        left = deadline - time.monotonic()
        if left <= 0:
            raise _DeadlineExceeded("deadline_exceeded")
        response = session.get(url, params=params, headers={"User-Agent": USER_AGENT,
                               "Authorization": None, "Cookie": None},
                               timeout=min(10.0, left), stream=True, allow_redirects=False)
        try:
            if response.status_code in (301, 302, 303, 307, 308):
                url = response.headers.get("Location", "")
                params = None
                continue
            response.raise_for_status()
            final = getattr(response, "url", url)
            if not _allowed_url(final, hosts):
                raise ValueError("untrusted_response_url")
            size = response.headers.get("Content-Length")
            if size and int(size) > limit:
                raise ValueError("response_too_large")
            chunks, total = [], 0
            for chunk in response.iter_content(chunk_size=65536):
                if time.monotonic() >= deadline:
                    raise _DeadlineExceeded("deadline_exceeded")
                total += len(chunk)
                if total > limit:
                    raise ValueError("response_too_large")
                chunks.append(chunk)
            return b"".join(chunks), response.headers.get("Content-Type", "").split(";", 1)[0].lower()
        finally:
            response.close()
    raise ValueError("too_many_redirects")


def _search(session, query: str, deadline: float, cache_dir: Path | None) -> list[dict]:
    cached = _SEARCH_CACHE.get(query)
    if cached and time.time() - cached[0] < CACHE_TTL:
        return cached[1]
    cache_path = cache_dir / (hashlib.sha256(query.encode()).hexdigest() + ".json") if cache_dir else None
    if cache_path and cache_path.is_file() and cache_path.stat().st_size <= MAX_JSON_BYTES:
        try:
            data = json.loads(cache_path.read_text())
            if time.time() - float(data["time"]) < CACHE_TTL and isinstance(data["results"], list):
                _SEARCH_CACHE[query] = (float(data["time"]), data["results"][:8])
                return data["results"][:8]
        except (ValueError, KeyError, OSError, TypeError):
            pass
    params = {"action": "query", "format": "json", "formatversion": 2,
              "generator": "search", "gsrnamespace": 6, "gsrlimit": 8,
              "gsrsearch": query + " filetype:bitmap", "prop": "imageinfo",
              "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1200,
              "iiextmetadatafilter": "Artist|Credit|License|LicenseShortName|LicenseUrl|UsageTerms|Copyrighted|AttributionRequired"}
    try:
        body, content_type = _read_response(session, API_URL, deadline=deadline, limit=MAX_JSON_BYTES,
                                           hosts={"commons.wikimedia.org"}, params=params)
        if content_type != "application/json":
            raise ValueError("not_json")
        data = json.loads(body)
        if "error" in data:
            raise ValueError("api_error")
        pages = data.get("query", {}).get("pages", [])
        if not isinstance(pages, list):
            raise ValueError("invalid_search_results")
    except (_ProviderCooldown, _DeadlineExceeded):
        raise
    except Exception as exc:
        _record_outage(exc)
        raise
    results = [p for p in pages[:8] if isinstance(p, dict)]
    _SEARCH_CACHE[query] = (time.time(), results)
    if cache_path:
        try:
            _atomic(cache_path, json.dumps({"time": time.time(), "results": results}).encode())
        except OSError:
            pass
    return results


def _normalized_image(data: bytes) -> bytes:
    if len(data) > MAX_IMAGE_BYTES:
        raise ValueError("image_too_large")
    with Image.open(io.BytesIO(data)) as image:
        if image.format not in ("JPEG", "PNG") or min(image.size) < 320 or image.width * image.height > MAX_PIXELS:
            raise ValueError("invalid_image_dimensions_or_format")
        if not 0.6 <= image.width / image.height <= 3.5:
            raise ValueError("invalid_image_aspect")
        image.verify()
    with Image.open(io.BytesIO(data)) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image = ImageOps.fit(image, (1200, 675), method=Image.Resampling.LANCZOS)
        # Flat responses and tiny service error badges are not article artwork.
        gray = image.convert("L").resize((96, 54))
        if gray.entropy() < 2.0:
            raise ValueError("flat_image")
        output = io.BytesIO()
        image.save(output, "JPEG", quality=89, optimize=True)
        return output.getvalue()


def download_editorial_image(session, title, target, timeout, index=1, cache_dir=None):
    """Return (JPEG Path, credit metadata); network failures use local artwork.

    One search (cached per topic/day), at most three candidate downloads, at
    most two redirects per request, and a shared 30-second maximum budget.
    """
    target = Path(target)
    cache_dir = Path(cache_dir) if cache_dir is not None else None
    topic, query = _topic(title)
    article_key = hashlib.sha256(str(title).encode()).hexdigest()
    used = _USED.setdefault(article_key, set())
    if len(_USED) > 512:
        _USED.pop(next(iter(_USED)))
    try:
        deadline = time.monotonic() + max(0.0, min(30.0, float(timeout)))
        results = _search(session, query, deadline, cache_dir)
        offset = max(0, int(index) - 1) % max(1, len(results))
        results = results[offset:] + results[:offset]
        attempted = 0
        for page in results:
            infos = page.get("imageinfo", [])
            if not infos or not isinstance(infos[0], dict):
                continue
            info = infos[0]
            credit = _license(info)
            url = str(info.get("thumburl") or info.get("url", ""))
            if (not credit or info.get("mime") not in ("image/jpeg", "image/png")
                    or not _allowed_url(url, {"upload.wikimedia.org", "thumb.wikimedia.org"})):
                continue
            key = hashlib.sha256(url.encode()).hexdigest()
            if key in used:
                continue
            attempted += 1
            if attempted > 3 or time.monotonic() >= deadline:
                break
            image_cache = cache_dir / (key + ".jpg") if cache_dir else None
            try:
                if image_cache and image_cache.is_file() and image_cache.stat().st_size <= MAX_IMAGE_BYTES:
                    raw = image_cache.read_bytes()
                else:
                    raw, mime = _read_response(session, url, deadline=deadline, limit=MAX_IMAGE_BYTES,
                                               hosts={"upload.wikimedia.org", "thumb.wikimedia.org"})
                    if mime not in ("image/jpeg", "image/png"):
                        continue
                image = _normalized_image(raw)
            except RequestException:
                raise
            except (ValueError, OSError, Image.DecompressionBombError):
                continue
            sha = hashlib.sha256(image).hexdigest()
            if sha in used:
                continue
            _atomic(target, image)
            if image_cache:
                try:
                    # Keep the admitted source bytes, avoiding lossy re-encoding
                    # on every cache hit and keeping content dedupe stable.
                    _atomic(image_cache, raw)
                except OSError:
                    pass
            used.update((key, sha))
            metadata = dict(credit, source="wikimedia_commons", topic=topic,
                            sha256=sha, asset_id=str(page.get("pageid", key)), modified=True)
            metadata["caption"] = attribution_caption(metadata)
            return target, metadata
    except (_ProviderCooldown, _DeadlineExceeded):
        pass
    except (RequestException, TimeoutError) as exc:
        # One provider outage must not turn a 43-article batch into 43 failed
        # searches. Successful cached source bytes remain usable during this
        # short circuit; future batches can probe again after the cooldown.
        _record_outage(exc)
    except Exception:
        # No retry loops, auth workarounds, or raw provider details in articles.
        pass
    path, metadata = bundled_fallback_image(target, str(title), index)
    metadata["fallback_reason"] = _COOLDOWN_REASON if time.monotonic() < _COOLDOWN_UNTIL else "no_eligible_image"
    return path, metadata


def bundled_fallback_image(target: Path, title: str, index: int = 1):
    """Render original subject illustration, never a QR/contact/header card."""
    target = Path(target)
    topic, _ = _topic(title)
    seed = int(hashlib.sha256((str(title) + ":" + str(index)).encode()).hexdigest()[:16], 16)
    rng = random.Random(seed)
    palettes = [("#102e4b", "#30717e", "#7fe4d5", "#ffcb75"),
                ("#241d46", "#514a8b", "#a7baff", "#ffae8f"),
                ("#163936", "#376c64", "#98e1c3", "#edbd65")]
    dark, mid, light, accent = palettes[seed % len(palettes)]
    image = Image.new("RGB", (1200, 675))
    draw = ImageDraw.Draw(image)
    from PIL import ImageColor
    top, bottom = ImageColor.getrgb(dark), ImageColor.getrgb(mid)
    for y in range(675):
        ratio = y / 674
        color = tuple(round(a * (1 - ratio) + b * ratio) for a, b in zip(top, bottom))
        draw.line((0, y, 1200, y), fill=color)
    for _ in range(170):
        x, y = rng.randrange(1200), rng.randrange(675)
        draw.ellipse((x, y, x + 2, y + 2), fill=mid)
    draw.ellipse((880, -190, 1390, 320), outline=light, width=3)
    draw.ellipse((-240, 390, 330, 960), outline=mid, width=3)

    def line(points, fill=light, width=5):
        draw.line(points, fill=fill, width=width, joint="curve")

    if topic == "technology":
        for i in range(10):
            y = 175 + i * 36
            for side in (-1, 1):
                edge, far = (390, 85 + (i % 3) * 55) if side < 0 else (810, 1115 - (i % 3) * 55)
                shift = rng.randint(-65, 65)
                line([(edge, y), (edge + side * 80, y), (edge + side * 130, y + shift), (far, y + shift)], mid, 7)
                draw.ellipse((far - 7, y + shift - 7, far + 7, y + shift + 7), fill=accent)
        for x in range(430, 800, 40):
            draw.rectangle((x, 100, x + 17, 160), fill=accent)
            draw.rectangle((x, 520, x + 17, 580), fill=accent)
        draw.rounded_rectangle((365, 140, 845, 540), radius=30, fill=dark, outline=light, width=6)
        draw.rounded_rectangle((425, 195, 785, 485), radius=20, fill=mid, outline=light, width=3)
        for row in range(4):
            for col in range(5):
                x, y = 458 + col * 60, 228 + row * 60
                draw.rectangle((x, y, x + 31, y + 31), fill=light if (col + row) % 3 else accent)
    elif topic == "energy":
        draw.ellipse((760, 65, 910, 215), fill=accent)
        draw.polygon([(0, 445), (270, 345), (480, 440), (830, 360), (1200, 470), (1200, 675), (0, 675)], fill=dark)
        for x, y, scale in [(275, 240, 1), (540, 285, .78), (940, 330, .65)]:
            line([(x, y), (x + 12, 535)], light, 9)
            for angle in (20, 140, 260):
                a = math.radians(angle + seed % 25)
                tip = (x + math.cos(a) * 120 * scale, y + math.sin(a) * 120 * scale)
                draw.polygon([(x - 8, y - 8), tip, (x + 8, y + 8)], fill=light)
            draw.ellipse((x - 11, y - 11, x + 11, y + 11), fill=accent)
        for col in range(4):
            x = 350 + col * 145
            draw.polygon([(x, 505), (x + 118, 505), (x + 165, 595), (x + 15, 595)], fill=mid, outline=light, width=3)
            for offset in (35, 70, 105):
                line([(x + offset, 510), (x + offset + 25, 590)], light, 2)
            line([(x + 8, 548), (x + 137, 548)], light, 2)
    elif topic == "transport":
        for y in range(490, 650, 25):
            line([(0, y), (1200, y - 25)], mid, 3)
        draw.polygon([(125, 400), (1030, 400), (950, 520), (220, 520)], fill=dark, outline=light, width=4)
        for row in range(3):
            for col in range(6):
                x, y = 280 + col * 105, 230 + row * 56
                draw.rectangle((x, y, x + 100, y + 50), fill=mid if (col + row) % 2 else accent, outline=dark, width=3)
                for dx in range(10, 95, 18):
                    line([(x + dx, y + 8), (x + dx, y + 43)], dark, 2)
        draw.rectangle((170, 255, 265, 400), fill=light)
        for x in (175, 207, 239):
            draw.rectangle((x, 272, x + 20, 299), fill=mid)
        for x in (650, 1000):
            line([(x, 390), (x, 100), (x - 235, 100)], light, 10)
            line([(x, 135), (x - 235, 100)], light, 3)
            line([(x - 210, 103), (x - 210, 200)], accent, 3)
    elif topic == "industry":
        draw.polygon([(115, 450), (115, 300), (295, 210), (295, 300), (475, 210), (475, 300), (655, 210), (655, 450)], fill=dark, outline=light, width=4)
        for x in range(155, 625, 85):
            draw.rectangle((x, 340, x + 45, 399), fill=accent)
        draw.rectangle((170, 120, 218, 275), fill=mid, outline=light, width=3)
        draw.rounded_rectangle((125, 480, 1090, 566), 40, fill=dark, outline=light, width=5)
        for x in range(155, 1080, 53):
            draw.ellipse((x, 509, x + 26, 535), fill=mid, outline=light, width=2)
        for x in (320, 520, 720):
            draw.rectangle((x, 425, x + 90, 480), fill=accent, outline=dark, width=4)
        line([(925, 475), (925, 370), (770, 275), (830, 180)], light, 34)
        for x, y in ((925, 370), (770, 275), (830, 180)):
            draw.ellipse((x - 24, y - 24, x + 24, y + 24), fill=accent, outline=dark, width=5)
        line([(827, 167), (815, 125), (850, 105)], light, 12)
    elif topic == "health":
        draw.rounded_rectangle((465, 125, 780, 535), radius=45, fill=light, outline=dark, width=6)
        draw.rectangle((555, 70, 690, 145), fill=accent, outline=dark, width=6)
        draw.rectangle((555, 260, 680, 315), fill=mid)
        draw.rectangle((590, 225, 645, 350), fill=mid)
        nodes = [(180, 210), (280, 140), (370, 240), (325, 370), (165, 390), (965, 205), (1040, 340), (910, 440)]
        for group in (nodes[:5], nodes[5:]):
            line(group + [group[0]], light, 6)
        for x, y in nodes:
            draw.ellipse((x - 27, y - 27, x + 27, y + 27), fill=accent, outline=dark, width=3)
        draw.rounded_rectangle((130, 505, 370, 565), 30, fill=accent)
        draw.pieslice((130, 505, 190, 565), 90, 270, fill=light)
        draw.rectangle((160, 505, 250, 565), fill=light)
    elif topic == "consumer":
        draw.rounded_rectangle((420, 85, 755, 580), 40, fill=dark, outline=light, width=7)
        draw.rounded_rectangle((445, 130, 730, 525), 15, fill=mid)
        draw.rounded_rectangle((540, 106, 635, 115), 4, fill=light)
        draw.ellipse((575, 544, 601, 570), outline=light, width=3)
        for x, y, scale in ((175, 340, 1), (820, 280, 1.15), (705, 440, .75)):
            w, h = 190 * scale, 145 * scale
            draw.polygon([(x, y), (x + w / 2, y - 45), (x + w, y), (x + w, y + h), (x, y + h)], fill=accent, outline=dark, width=5)
            line([(x, y), (x + w / 2, y + 40), (x + w, y)], dark, 4)
            line([(x + w / 2, y + 40), (x + w / 2, y + h)], dark, 4)
        line([(490, 240), (520, 240), (544, 342), (665, 342), (690, 270), (530, 270)], light, 9)
        for x in (550, 650):
            draw.ellipse((x - 12, 357, x + 12, 381), fill=light)
    else:
        draw.ellipse((750, 95, 1070, 415), outline=accent, width=4)
        draw.ellipse((830, 95, 990, 415), outline=accent, width=3)
        for y in (175, 255, 335):
            line([(770, y), (1050, y)], accent, 3)
        for i, (x, height) in enumerate([(110, 220), (260, 335), (425, 420), (610, 270), (770, 180), (925, 245)]):
            y = 580 - height
            draw.polygon([(x, y), (x + 108, y), (x + 145, y + 32), (x + 145, 590), (x, 590)], fill=dark, outline=light, width=3)
            draw.polygon([(x + 108, y), (x + 145, y + 32), (x + 145, 590), (x + 108, 590)], fill=mid)
            for wx in range(x + 18, x + 103, 29):
                for wy in range(y + 25, 563, 40):
                    draw.rectangle((wx, wy, wx + 10, wy + 18), fill=accent if (wx + wy + i) % 3 else light)
        line([(80, 605), (1110, 605)], light, 5)
    output = io.BytesIO()
    image.save(output, "JPEG", quality=91, optimize=True)
    data = output.getvalue()
    _atomic(target, data)
    metadata = {"source": "local_editorial", "author": "Portal Suite", "source_url": "",
                "license": "original", "license_url": "", "topic": topic,
                "sha256": hashlib.sha256(data).hexdigest(), "modified": False}
    metadata["caption"] = attribution_caption(metadata)
    return target, metadata


def _smoke_main() -> int:
    """Manual CI-only public provider canary, with no publishing or secrets."""
    import argparse
    from datetime import datetime, timezone

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke-dir", type=Path, required=True)
    parser.add_argument("--require-commons", action="store_true")
    args = parser.parse_args()
    args.smoke_dir.mkdir(parents=True, exist_ok=True)

    class CountedSession(requests.Session):
        count = 0

        def get(self, *a, **kw):
            self.count += 1
            return super().get(*a, **kw)

    with CountedSession() as session:
        path, metadata = download_editorial_image(session, "financial district skyline", args.smoke_dir / "sample.jpg", 30)
        with Image.open(path) as image:
            image.load()
            dimensions = list(image.size)
        report = {"schema_version": 1, "checked_at": datetime.now(timezone.utc).isoformat(),
                  "source": metadata["source"], "commons_download_verified": metadata["source"] == "wikimedia_commons",
                  "network_requests": session.count, "image_count": 1, "dimensions": dimensions,
                  "image_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                  "license": metadata["license"], "license_url": metadata["license_url"],
                  "author": metadata["author"], "source_url": metadata["source_url"],
                  "fallback_reason": metadata.get("fallback_reason", ""),
                  "model_calls": 0, "wechat_writes": 0, "publication_writes": 0}
    _atomic(args.smoke_dir / "provider-report.json", json.dumps(report, indent=2).encode())
    _atomic(args.smoke_dir / "caption.html", attribution_html(metadata).encode())
    print(json.dumps(report))
    return int(args.require_commons and not report["commons_download_verified"])


if __name__ == "__main__":
    raise SystemExit(_smoke_main())
