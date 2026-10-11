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
_SELECTIONS: dict[str, tuple[bytes, dict]] = {}
_BATCH_URL_OWNERS: dict[str, str] = {}
_BATCH_CONTENT_OWNERS: dict[str, str] = {}
_LOADED_SELECTION_CACHES: set[str] = set()
_COOLDOWN_UNTIL = 0.0
_COOLDOWN_REASON = ""
OUTAGE_COOLDOWN_SECONDS = 300
# Category union is a single filter. Boolean OR between separate incategory
# keywords is not supported reliably by CirrusSearch:
# https://phabricator.wikimedia.org/T164589
# These categories narrow discovery only; _license still validates each file.
COMMONS_LICENSE_FILTER = 'incategory:"CC-Zero|CC-BY-2.0|CC-BY-2.5|CC-BY-3.0|CC-BY-4.0"'
_REJECTION_REASONS = {
    "metadata", "license", "format", "url", "duplicate_url", "duplicate_content",
    "response_type", "image_validation", "download_limit", "time_budget", "declared_geometry",
}
_VALIDATION_REASONS = {
    "declared_small", "declared_aspect", "declared_pixels", "declared_bytes",
    "declared_dimensions", "image_too_large", "invalid_image_format", "image_too_small",
    "image_too_many_pixels", "invalid_image_aspect", "flat_image", "image_decode",
    "response_too_large", "untrusted_url", "untrusted_response_url", "too_many_redirects",
    "invalid_content_length", "other_validation",
}
_TOPICS = (
    ("technology", "semiconductor", r"芯片|半导体|存储|晶圆|tdk|marvell|samsung|三星|科技|人工智能|数据中心|\bai\b|semiconductor|memory|technology|data cent|software|软件|电子"),
    ("energy", "solar panels", r"能源|电力|电网|电池|太阳能|石油|天然气|核电|energy|power|solar|wind|oil|gas|battery"),
    ("industry", "factory", r"工业|制造|机械|金属|矿|铜|钢|铝|机器人|工业|industry|industrial|mining|metal|factory|manufactur"),
    ("transport", "container port", r"运输|物流|货运|航运|航空|汽车|rail|transport|cargo|shipping|port|airline|automotive"),
    ("health", "laboratory", r"医疗|医药|药物|生物|医院|health|medical|pharma|biotech|medicine"),
    ("consumer", "retail", r"消费|零售|电商|酒店|旅行|旅游|食品|餐饮|consumer|retail|shopping|hotel|travel|food"),
    ("finance", "city skyline", r"银行|金融|利率|宏观|基金|股|投资|市场|经济|bank|financ|market|econom|equity|invest|yield"),
)


def _topic(title: str) -> tuple[str, str]:
    for name, query, pattern in _TOPICS:
        if re.search(pattern, str(title), re.I):
            return name, query
    return "finance", "city skyline"


def _search_query(query: str) -> str:
    # Fixed one/two-word topic terms avoid inadvertently requiring a single
    # photo description to mention several different objects at once.
    return query + " filetype:bitmap " + COMMONS_LICENSE_FILTER


def _safe_diagnostics(value: object) -> dict:
    """Only bounded counters and fixed rejection codes may enter CI logs."""
    value = value if isinstance(value, dict) else {}
    def number(value):
        return value if type(value) is int and 0 <= value <= 8 else 0
    rejections = value.get("rejections", {})
    rejections = rejections if isinstance(rejections, dict) else {}
    failures = value.get("validation_failures", {})
    failures = failures if isinstance(failures, dict) else {}
    return {"search_results": number(value.get("search_results")),
            "admitted": number(value.get("admitted")),
            "rejections": {key: number(rejections[key]) for key in sorted(_REJECTION_REASONS)
                           if key in rejections and number(rejections[key])},
            "validation_failures": {key: number(failures[key]) for key in sorted(_VALIDATION_REASONS)
                                    if key in failures and number(failures[key])},
            **{key: number(value.get(key)) for key in (
                "thumbnail_candidates", "original_candidates", "thumbnail_attempts", "original_attempts")}}


def _declared_geometry_rejection(info: dict, thumbnail: bool) -> str:
    """Reject only dimensions of the chosen asset, not its larger original."""
    prefix = "thumb" if thumbnail else ""
    width, height = info.get(prefix + "width"), info.get(prefix + "height")
    if width is not None or height is not None:
        if type(width) is not int or type(height) is not int or width <= 0 or height <= 0:
            return "declared_dimensions"
        if min(width, height) < 320:
            return "declared_small"
        if not .6 <= width / height <= 3.5:
            return "declared_aspect"
        if width * height > MAX_PIXELS:
            return "declared_pixels"
    # API size describes the original, not the generated thumbnail.
    if not thumbnail and type(info.get("size")) is int and info["size"] > MAX_IMAGE_BYTES:
        return "declared_bytes"
    return ""


def _validation_reason(exc: Exception) -> str:
    if isinstance(exc, Image.DecompressionBombError):
        return "image_too_many_pixels"
    if isinstance(exc, OSError):
        return "image_decode"
    return str(exc) if str(exc) in _VALIDATION_REASONS else "other_validation"


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
            if size:
                try:
                    declared_size = int(size)
                except (ValueError, TypeError):
                    raise ValueError("invalid_content_length") from None
                if declared_size > limit:
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
    query = _search_query(query)
    # Change identity with thumbnail parameters so old API metadata lacking
    # bounded thumbnail dimensions does not survive this request upgrade.
    cache_key = "thumbnail-box-1200-v2:" + query
    cached = _SEARCH_CACHE.get(cache_key)
    if cached and time.time() - cached[0] < CACHE_TTL:
        return cached[1]
    cache_path = cache_dir / (hashlib.sha256(cache_key.encode()).hexdigest() + ".json") if cache_dir else None
    if cache_path and cache_path.is_file() and cache_path.stat().st_size <= MAX_JSON_BYTES:
        try:
            data = json.loads(cache_path.read_text())
            if time.time() - float(data["time"]) < CACHE_TTL and isinstance(data["results"], list):
                _SEARCH_CACHE[cache_key] = (float(data["time"]), data["results"][:8])
                return data["results"][:8]
        except (ValueError, KeyError, OSError, TypeError):
            pass
    params = {"action": "query", "format": "json", "formatversion": 2,
              "generator": "search", "gsrnamespace": 6, "gsrlimit": 8,
              "gsrsearch": query, "prop": "imageinfo",
              "iiprop": "url|size|mime|thumbmime|extmetadata", "iiurlwidth": 1200, "iiurlheight": 1200,
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
    _SEARCH_CACHE[cache_key] = (time.time(), results)
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
        if image.format not in ("JPEG", "PNG"):
            raise ValueError("invalid_image_format")
        if min(image.size) < 320:
            raise ValueError("image_too_small")
        if image.width * image.height > MAX_PIXELS:
            raise ValueError("image_too_many_pixels")
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


def _valid_selection_record(record: dict) -> bool:
    if not isinstance(record, dict) or record.get('schema') != 1:
        return False
    metadata = record.get('metadata', {})
    if (not isinstance(metadata, dict) or not re.fullmatch(r'[a-f0-9]{64}', str(record.get('slot', '')))
            or not re.fullmatch(r'[a-f0-9]{64}', str(metadata.get('sha256', '')))):
        return False
    if metadata.get('source') == 'local_editorial':
        return metadata.get('license') == 'original' and not metadata.get('license_url')
    if metadata.get('source') != 'wikimedia_commons':
        return False
    return _license({'descriptionurl': metadata.get('source_url'), 'extmetadata': {
        'Artist': {'value': metadata.get('author')}, 'LicenseShortName': {'value': metadata.get('license')},
        'LicenseUrl': {'value': metadata.get('license_url')}}}) is not None


def _read_selection(path: Path):
    try:
        if path.is_file() and not path.is_symlink() and path.stat().st_size <= 16 * 1024:
            value = json.loads(path.read_text())
            return value if _valid_selection_record(value) else None
    except (ValueError, OSError):
        pass
    return None


def _load_batch_claims(cache_dir: Path | None) -> None:
    if cache_dir is None or str(cache_dir.resolve()) in _LOADED_SELECTION_CACHES:
        return
    _LOADED_SELECTION_CACHES.add(str(cache_dir.resolve()))
    for path in sorted(cache_dir.glob('selection-*.json'))[:512]:
        record = _read_selection(path)
        if not record:
            continue
        metadata, slot = record['metadata'], record['slot']
        if metadata['source'] == 'wikimedia_commons':
            _BATCH_CONTENT_OWNERS.setdefault(metadata['sha256'], slot)
            url_key = str(metadata.get('asset_url_sha256', ''))
            if re.fullmatch(r'[a-f0-9]{64}', url_key):
                _BATCH_URL_OWNERS.setdefault(url_key, slot)


def _selected_image(slot: str, target: Path, cache_dir: Path | None):
    selected = _SELECTIONS.get(slot)
    if selected is None and cache_dir is not None:
        record = _read_selection(cache_dir / ('selection-' + slot + '.json'))
        image_path = cache_dir / ('selection-' + slot + '.jpg')
        try:
            if record and record['slot'] == slot and image_path.is_file() and not image_path.is_symlink() and image_path.stat().st_size <= MAX_IMAGE_BYTES:
                data = image_path.read_bytes()
                if hashlib.sha256(data).hexdigest() == record['metadata']['sha256']:
                    with Image.open(io.BytesIO(data)) as image:
                        if image.format == 'JPEG' and image.size == (1200, 675):
                            image.verify()
                            selected = (data, record['metadata'])
        except (ValueError, OSError, Image.DecompressionBombError):
            pass
    if selected is None:
        return None
    data, metadata = selected
    _atomic(target, data)
    _SELECTIONS[slot] = (data, dict(metadata))
    return target, dict(metadata)


def _remember_selection(slot: str, path: Path, metadata: dict, cache_dir: Path | None):
    data = path.read_bytes()
    if len(_SELECTIONS) >= 512:
        _SELECTIONS.pop(next(iter(_SELECTIONS)))
    _SELECTIONS[slot] = (data, dict(metadata))
    if metadata['source'] == 'wikimedia_commons':
        _BATCH_CONTENT_OWNERS[metadata['sha256']] = slot
        _BATCH_URL_OWNERS[metadata['asset_url_sha256']] = slot
    if cache_dir is not None:
        try:
            _atomic(cache_dir / ('selection-' + slot + '.jpg'), data)
            _atomic(cache_dir / ('selection-' + slot + '.json'),
                    json.dumps({'schema': 1, 'slot': slot, 'metadata': metadata}).encode())
        except OSError:
            pass
    return path, metadata


def download_editorial_image(session, title, target, timeout, index=1, cache_dir=None):
    """Return (JPEG Path, credit metadata); network failures use local artwork.

    One search (cached per topic/day), at most three candidate downloads, at
    most two redirects per request, and a shared 30-second maximum budget.
    Shared cache_dir preserves article/slot selections and batch image claims:
    retries retain the same choice; different articles never share a photo.
    """
    target = Path(target)
    cache_dir = Path(cache_dir) if cache_dir is not None else None
    topic, query = _topic(title)
    article_key = hashlib.sha256(str(title).encode()).hexdigest()
    slot = hashlib.sha256((str(title) + '\0' + str(index)).encode()).hexdigest()
    _load_batch_claims(cache_dir)
    selected = _selected_image(slot, target, cache_dir)
    if selected is not None:
        return selected
    used = _USED.setdefault(article_key, set())
    if len(_USED) > 512:
        _USED.pop(next(iter(_USED)))
    diagnostics = _safe_diagnostics({})

    def reject(reason):
        rejected = diagnostics["rejections"]
        rejected[reason] = rejected.get(reason, 0) + 1

    def validation_failure(reason):
        failures = diagnostics["validation_failures"]
        failures[reason] = failures.get(reason, 0) + 1

    try:
        deadline = time.monotonic() + max(0.0, min(30.0, float(timeout)))
        results = _search(session, query, deadline, cache_dir)
        diagnostics["search_results"] = len(results)
        offset = max(0, int(index) - 1) % max(1, len(results))
        results = results[offset:] + results[:offset]
        candidates = []
        for page in results:
            infos = page.get("imageinfo", [])
            if not isinstance(infos, list) or not infos or not isinstance(infos[0], dict):
                reject("metadata")
                continue
            info = infos[0]
            credit = _license(info)
            thumbnail = bool(info.get("thumburl"))
            url = str(info.get("thumburl") or info.get("url", ""))
            if not credit:
                reject("license")
                continue
            if (info.get("mime") not in ("image/jpeg", "image/png")
                    or (thumbnail and info.get("thumbmime", info["mime"]) not in ("image/jpeg", "image/png"))):
                reject("format")
                continue
            if not _allowed_url(url, {"upload.wikimedia.org", "thumb.wikimedia.org"}):
                reject("url")
                continue
            geometry_rejection = _declared_geometry_rejection(info, thumbnail)
            if geometry_rejection:
                reject("declared_geometry")
                validation_failure(geometry_rejection)
                continue
            diagnostics["thumbnail_candidates" if thumbnail else "original_candidates"] += 1
            candidates.append((page, credit, url, thumbnail))
        diagnostics["admitted"] = len(candidates)
        attempted = 0
        for page, credit, url, thumbnail in candidates:
            key = hashlib.sha256(url.encode()).hexdigest()
            if key in used or _BATCH_URL_OWNERS.get(key, slot) != slot:
                reject("duplicate_url")
                continue
            if attempted >= 3:
                reject("download_limit")
                break
            if time.monotonic() >= deadline:
                reject("time_budget")
                break
            attempted += 1
            diagnostics["thumbnail_attempts" if thumbnail else "original_attempts"] += 1
            image_cache = cache_dir / (key + ".jpg") if cache_dir else None
            try:
                if image_cache and image_cache.is_file() and image_cache.stat().st_size <= MAX_IMAGE_BYTES:
                    raw = image_cache.read_bytes()
                else:
                    raw, mime = _read_response(session, url, deadline=deadline, limit=MAX_IMAGE_BYTES,
                                               hosts={"upload.wikimedia.org", "thumb.wikimedia.org"})
                    if mime not in ("image/jpeg", "image/png"):
                        reject("response_type")
                        continue
                image = _normalized_image(raw)
            except RequestException:
                raise
            except (ValueError, OSError, Image.DecompressionBombError) as exc:
                reject("image_validation")
                validation_failure(_validation_reason(exc))
                continue
            sha = hashlib.sha256(image).hexdigest()
            if sha in used or _BATCH_CONTENT_OWNERS.get(sha, slot) != slot:
                # Alias URLs returning the same image must not be tried again
                # for every subsequent article in the batch.
                _BATCH_URL_OWNERS[key] = _BATCH_CONTENT_OWNERS.get(sha, 'duplicate')
                reject("duplicate_content")
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
                            sha256=sha, asset_id=str(page.get("pageid", key)), asset_url_sha256=key, modified=True)
            metadata["download_variant"] = "thumbnail" if thumbnail else "original"
            metadata["caption"] = attribution_caption(metadata)
            metadata["search_diagnostics"] = _safe_diagnostics(diagnostics)
            return _remember_selection(slot, target, metadata, cache_dir)
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
    metadata["search_diagnostics"] = _safe_diagnostics(diagnostics)
    return _remember_selection(slot, path, metadata, cache_dir)


_MOTIFS = {
    "technology": ("chip", "servers", "network", "board"),
    "energy": ("wind", "solar", "battery", "grid"),
    "industry": ("factory", "robot", "gear", "conveyor"),
    "transport": ("ship", "train", "container", "route"),
    "health": ("medicine", "molecule", "cross", "lab"),
    "consumer": ("phone", "boxes", "shop", "cart"),
    "finance": ("tower", "globe", "bank", "coins"),
}


def _scene_plan(title: str, index: int) -> tuple[str, dict]:
    """Geometry only: no color/noise/metadata enters the geometry fingerprint."""
    seed_hex = hashlib.sha256(("editorial-scene-v2\0" + str(title) + "\0" + str(index)).encode()).hexdigest()
    rng = random.Random(int(seed_hex[:16], 16))
    topic, _ = _topic(title)
    variant = rng.choice(("hero", "cascade", "constellation", "panorama", "duet"))
    if variant == "hero":
        anchors = [(770, 345, 505), (255, 205, 260), (260, 510, 250)]
    elif variant == "cascade":
        anchors = [(220, 485, 330), (565, 320, 425), (970, 195, 310)]
    elif variant == "constellation":
        anchors = [(600, 330, 375), (185, 180, 235), (190, 520, 225), (1020, 180, 225), (1000, 520, 230)]
    elif variant == "panorama":
        count = rng.choice((3, 4))
        anchors = [(int((i + .5) * 1200 / count), rng.randint(275, 410), 360 if count == 3 else 290) for i in range(count)]
    else:
        anchors = [(335, 350, 480), (865, 335, 450)]
    motifs = list(_MOTIFS[topic])
    rng.shuffle(motifs)
    objects = []
    mirror = rng.choice((False, True))
    for i, (cx, cy, size) in enumerate(anchors):
        cx = (1200 - cx if mirror else cx) + rng.randint(-30, 30)
        cy += rng.randint(-28, 28)
        size = round(size * rng.uniform(.86, 1.06))
        objects.append({"motif": motifs[i % len(motifs)], "cx": cx, "cy": cy,
                        "size": size, "angle": rng.choice((-12, -7, 0, 5, 10)),
                        "columns": rng.randint(3, 6), "rows": rng.randint(3, 6),
                        "detail": rng.randint(0, 9999)})
    return seed_hex, {"schema": 2, "topic": topic, "variant": variant, "objects": objects}


def _motif_image(obj: dict, colors: tuple, geometry_only: bool = False) -> Image.Image:
    """Draw a varied thematic object in a square transparent coordinate space."""
    dark, mid, light, accent = colors
    if geometry_only:
        dark, mid, light, accent = "#888888", "#aaaaaa", "#ffffff", "#dddddd"
    image = Image.new("RGBA", (480, 480))
    d = ImageDraw.Draw(image)
    kind, cols, rows = obj["motif"], obj["columns"], obj["rows"]
    rng = random.Random(obj["detail"])

    def rect(box, fill=mid, radius=0, outline=light, width=5):
        if radius:
            d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
        else:
            d.rectangle(box, fill=fill, outline=outline, width=width)

    def line(points, fill=light, width=6):
        d.line(points, fill=fill, width=width, joint="curve")

    def circle(cx, cy, r, fill=accent, outline=light, width=4):
        d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=fill, outline=outline, width=width)

    if kind in ("chip", "board"):
        rect((95, 95, 385, 385), dark, 22)
        for i in range(cols + 2):
            p = 125 + i * 230 / (cols + 1)
            for box in ((p, 45, p+13, 95), (p, 385, p+13, 435), (45, p, 95, p+13), (385, p, 435, p+13)):
                rect(box, accent, width=0)
        if kind == "chip":
            rect((140, 140, 340, 340), mid, 12, width=3)
            for row in range(rows):
                for col in range(cols):
                    x, y = 153 + col * 174 / cols, 153 + row * 174 / rows
                    rect((x, y, x + 110 / cols, y + 110 / rows), accent if (row+col) % 3 == 0 else light, width=0)
        else:
            for i in range(3):
                x, y = rng.randint(125, 285), 140 + i * 75
                rect((x, y, x+55, y+45), accent, 4, width=2)
                line([(x+55, y+23), (350, y+23), (350, y+55)], light, 3)
                circle(350, y+55, 5, light, width=0)
    elif kind == "servers":
        count = 2 + cols % 3
        w = 360 / count
        for col in range(count):
            x = 55 + col * (w + 7)
            rect((x, 60 + col*9, x+w-10, 415), dark, 12)
            for row in range(rows):
                y = 83 + row * (300 / rows)
                rect((x+10, y, x+w-20, y+220/rows), mid, 4, width=2)
                circle(x+25, y+100/rows, 4, accent, width=0)
                line([(x+38,y+100/rows),(x+w-27,y+100/rows)], light, 2)
    elif kind in ("network", "molecule", "route"):
        count = cols + 1
        points = [(240 + math.cos(2*math.pi*i/count)*rng.randint(140,185),
                   240 + math.sin(2*math.pi*i/count)*rng.randint(140,185)) for i in range(count)]
        for i, point in enumerate(points):
            line([point, points[(i+1)%count]], mid, 8)
            if kind != "route":
                line([point, (240,240)], light, 4)
        for i,(x,y) in enumerate(points):
            circle(x,y,16 + (i % 3)*7, light if i%2 else accent)
        if kind == "network":
            rect((193,193,287,287), dark, 15)
            rect((217,217,263,263), accent, width=0)
        elif kind == "molecule":
            circle(240,240,40,accent)
        else:
            line([points[0], (240,240), points[-1]], accent, 12)
            circle(240,240,22,accent)
    elif kind == "wind":
        for i in range(2 + cols % 2):
            x, y = 105 + i * 140, 155 + i * 40
            line([(x,y),(x,425)], light, 13)
            rotation = rng.randint(0,90)
            for angle in (rotation, rotation+120, rotation+240):
                a=math.radians(angle)
                tip=(x+math.cos(a)*95,y+math.sin(a)*95)
                d.polygon([(x-7,y-7),tip,(x+7,y+7)],fill=light)
            circle(x,y,13,accent,width=0)
    elif kind == "solar":
        for row in range(2 + rows % 2):
            y=105+row*105
            for col in range(2 + cols % 2):
                x=30+col*145
                d.polygon([(x,y),(x+110,y),(x+140,y+80),(x+10,y+80)],fill=mid,outline=light,width=4)
                for dx in (30,60,90): line([(x+dx,y+5),(x+dx+20,y+75)],light,2)
                line([(x+8,y+40),(x+125,y+40)],light,2)
        circle(375,50,28,accent,width=0)
    elif kind == "battery":
        count=2+cols%3
        for i in range(count):
            x=50+i*360/count
            rect((x+20,65,x+55,93),accent,width=0)
            rect((x,95,x+76,398),dark,12)
            for row in range(2+((rows+i)%4)):
                y=345-row*46
                rect((x+12,y,x+64,y+29),light if row%2 else accent,width=0)
    elif kind == "grid":
        for x,h in ((140,335),(335,275)):
            y=425-h
            line([(x-65,425),(x,y),(x+65,425)],light,8)
            for off in (60,120,185):
                line([(x-70,y+off),(x+70,y+off)],accent,6)
                line([(x-45,y+off+50),(x+45,y+off)],mid,4)
        for y in (140,205,270): line([(70,y),(335,y+60),(430,y+70)],light,3)
    elif kind in ("factory", "shop", "bank"):
        if kind == "bank":
            d.polygon([(40,150),(240,45),(440,150)],fill=accent,outline=light,width=5)
            for i in range(cols):
                x=75+i*340/cols
                rect((x,175,x+190/cols,385),mid)
            rect((40,405,440,437),accent)
        else:
            roof=[(45,190),(435,190),(435,420),(45,420)]
            if kind == "factory": roof=[(45,190),(165,100),(165,190),(295,100),(295,190),(435,100),(435,420),(45,420)]
            d.polygon(roof,fill=dark,outline=light,width=5)
            for i in range(cols):
                x=65+i*350/cols
                rect((x,260,x+220/cols,355),accent,width=0)
            if kind=="shop":
                for i in range(cols+2):
                    x=45+i*390/(cols+2)
                    rect((x,140,x+390/(cols+2),220),accent if i%2 else light,width=0)
    elif kind == "robot":
        joints=[(245,400),(245,310),(rng.randint(105,160),220),(rng.randint(230,300),90)]
        line(joints,light,35)
        for x,y in joints: circle(x,y,23,accent,outline=dark)
        rect((155,405,335,440),dark,10)
        x,y=joints[-1]
        line([(x-20,y-15),(x-35,y-55),(x-10,y-75)],light,10)
        line([(x+20,y-15),(x+35,y-55),(x+10,y-75)],light,10)
    elif kind == "gear":
        for cx,cy,r in ((175,185,120),(340,325,80)):
            teeth=cols+6
            for i in range(teeth):
                a=2*math.pi*i/teeth
                x,y=cx+math.cos(a)*r,cy+math.sin(a)*r
                rect((x-14,y-14,x+14,y+14),accent,width=0)
            circle(cx,cy,r,mid)
            circle(cx,cy,r*.43,dark)
    elif kind == "conveyor":
        rect((35,325,445,420),dark,45)
        for i in range(cols+3): circle(65+i*350/(cols+2),372,15,mid)
        for i in range(2+rows%3):
            x=55+i*350/(2+rows%3)
            rect((x,215,x+65,323),accent)
            line([(x+32,220),(x+32,255)],dark,5)
    elif kind in ("ship", "container", "train"):
        count=3+cols%3
        for row in range(1+rows%3):
            for col in range(count):
                x,y=40+col*400/count,155+row*60
                rect((x,y,x+380/count,y+52),accent if (col+row)%2 else mid,width=3)
                for dx in range(12,int(380/count)-5,16): line([(x+dx,y+6),(x+dx,y+45)],dark,2)
        if kind=="ship":
            d.polygon([(15,355),(465,355),(415,420),(85,420)],fill=dark,outline=light,width=5)
            rect((55,95,130,155),light)
            line([(240,150),(240,55),(355,55)],light,5)
        elif kind=="train":
            for x in (85,185,285,385): circle(x,375,25,dark)
            line([(30,415),(455,415)],light,7)
        else:
            line([(40,355),(435,355)],light,6)
    elif kind in ("medicine", "cross", "lab"):
        if kind=="cross":
            rect((85,85,395,395),dark,45)
            rect((195,145,285,335),accent,width=0)
            rect((145,195,335,285),accent,width=0)
        elif kind=="medicine":
            rect((130,120,350,425),light,35,outline=dark)
            rect((175,65,305,132),accent)
            rect((170,255,310,295),mid,width=0)
            rect((220,205,260,345),mid,width=0)
        else:
            line([(190,50),(190,180),(70,375),(90,425),(390,425),(410,375),(290,180),(290,50)],light,8)
            line([(175,50),(305,50)],accent,12)
            d.polygon([(123,320),(357,320),(390,390),(90,390)],fill=mid)
            for i in range(cols): circle(rng.randint(145,335),rng.randint(240,380),rng.randint(7,17),accent,width=0)
    elif kind in ("phone", "cart", "boxes"):
        if kind=="phone":
            rect((130,35,350,445),dark,30)
            rect((150,85,330,382),mid,10,width=2)
            line([(205,58),(275,58)],light,5)
            circle(240,413,12,dark)
            line([(175,175),(195,175),(215,270),(285,270),(305,195),(200,195)],accent,8)
        elif kind=="cart":
            line([(45,95),(95,95),(155,325),(380,325),(430,150),(115,150)],light,12)
            for i in range(cols): line([(140+i*240/cols,165),(165+i*210/cols,295)],mid,5)
            for x in (185,355): circle(x,385,30,accent)
        else:
            for x,y,w in ((65,150,165),(235,245,170),(240,60,150)):
                d.polygon([(x,y),(x+w/2,y-45),(x+w,y),(x+w,y+125),(x,y+125)],fill=accent,outline=dark,width=5)
                line([(x,y),(x+w/2,y+35),(x+w,y)],dark,4)
                line([(x+w/2,y+35),(x+w/2,y+125)],dark,4)
    elif kind == "tower":
        count=2+cols%3
        for i in range(count):
            x=45+i*390/count
            height=rng.randint(200,355)
            rect((x,425-height,x+330/count,425),dark)
            for row in range(rows):
                for col in range(2):
                    y=445-height+row*(height-45)/rows
                    rect((x+15+col*110/count,y,x+25+col*110/count,y+14),accent,width=0)
    elif kind == "globe":
        circle(240,240,185,dark)
        d.ellipse((150,55,330,425),outline=accent,width=4)
        for y in (125,200,280,355): line([(90,y),(390,y)],light,3)
        line([(240,55),(240,425)],light,3)
    elif kind == "coins":
        for i in range(3):
            x=65+i*150
            count=2+(rows+i)%5
            for j in range(count):
                y=380-j*45
                rect((x,y-25,x+115,y),mid,outline=light,width=3)
                d.ellipse((x,y-45,x+115,y-10),fill=accent,outline=light,width=3)
    return image


def _render_scene(plan: dict, seed_hex: str, *, geometry_only=False) -> Image.Image:
    import colorsys
    rng=random.Random(int(seed_hex[16:32],16))
    hue=rng.random()
    def color(h,s,l):
        return tuple(round(v*255) for v in colorsys.hls_to_rgb(h%1,l,s))
    colors=(color(hue,.55,.13),color(hue,.45,.30),color(hue+.05,.63,.80),color(hue+.48,.85,.73))
    dark,mid,light,accent=colors
    image=Image.new("RGB",(1200,675),"black" if geometry_only else dark)
    d=ImageDraw.Draw(image)
    if not geometry_only:
        for y in range(675):
            ratio=y/674
            d.line((0,y,1200,y),fill=tuple(round(a*(1-ratio)+b*ratio) for a,b in zip(dark,mid)))
        # Broad composition accents differ independently; there is no noise
        # texture that could artificially satisfy image-diversity checks.
        x,y=rng.randint(-180,900),rng.randint(-180,250)
        diameter=rng.randint(350,750)
        d.ellipse((x,y,x+diameter,y+diameter),outline=mid,width=3)
        d.line((0,rng.randint(450,600),1200,rng.randint(420,600)),fill=mid,width=3)
    objects=plan["objects"]
    for previous,current in zip(objects,objects[1:]):
        d.line((previous["cx"],previous["cy"],current["cx"],current["cy"]),fill="#555555" if geometry_only else mid,width=4)
    for obj in objects:
        motif=_motif_image(obj,colors,geometry_only)
        size=obj["size"]
        motif=motif.resize((size,size),Image.Resampling.LANCZOS).rotate(obj["angle"],resample=Image.Resampling.BICUBIC,expand=True)
        image.paste(motif,(round(obj["cx"]-motif.width/2),round(obj["cy"]-motif.height/2)),motif)
    return image


def bundled_fallback_image(target: Path, title: str, index: int = 1):
    """Original, visibly varied geometry; a stable article/slot keeps its image."""
    target=Path(target)
    seed_hex,plan=_scene_plan(title,index)
    image=_render_scene(plan,seed_hex)
    output=io.BytesIO()
    image.save(output,"JPEG",quality=91,optimize=True)
    data=output.getvalue()
    _atomic(target,data)
    geometry=hashlib.sha256(json.dumps(plan,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    metadata={"source":"local_editorial","author":"Portal Suite","source_url":"",
              "license":"original","license_url":"","topic":plan["topic"],
              "sha256":hashlib.sha256(data).hexdigest(),"modified":False,
              "variant":plan["variant"],"seed":seed_hex[:16],"geometry_signature":geometry,
              "object_count":len(plan["objects"])}
    metadata["caption"]=attribution_caption(metadata)
    return target,metadata


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
        report.update(_safe_diagnostics(metadata.get("search_diagnostics")))
    _atomic(args.smoke_dir / "provider-report.json", json.dumps(report, indent=2).encode())
    _atomic(args.smoke_dir / "caption.html", attribution_html(metadata).encode())
    print(json.dumps(report))
    return int(args.require_commons and not report["commons_download_verified"])


if __name__ == "__main__":
    raise SystemExit(_smoke_main())
