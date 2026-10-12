#!/usr/bin/env python3
"""Repair media in receipt-bound existing drafts; never add, delete or publish."""
from __future__ import annotations
import argparse
from collections import Counter
import copy
import hashlib
import html
import json
import os
from pathlib import Path
import re
from urllib.parse import urlsplit
import requests
from PIL import Image
from free_editorial_images import download_editorial_image, attribution_html
from wechat_image_quality import article_image_rejection
from verify_existing_wechat_drafts import load_drafts
from push_portal_translated_to_wechat_drafts import (
    get_stable_access_token, get_draft, draft_news_items, wechat_content_images,
    materialize_private_article_payload, article_prose_text, generated_image_credit_signature,
    legacy_stripped_commons_credit, generated_image_credits, IMAGE_CREDIT_PARAGRAPH_RE,
    visible_wechat_content_text, managed_image_annotation_kind, strip_managed_image_annotations,
    MANAGED_IMAGE_ANNOTATION_RE,
    post_wechat_json, parse_wechat_json, prepare_cover_upload_image,
    upload_article_image, upload_cover_material, image_html, summarize_draft_get_response,
    wechat_image_url_identity, wechat_editorial_contract_check, WeChatError,
)

MAX_IMAGE_BYTES = 12 * 1024 * 1024
CREDIT_RE = MANAGED_IMAGE_ANNOTATION_RE
IMG_RE = re.compile(r'<img\b[^>]*>', re.I | re.S)
MANAGED_IMG_RE = re.compile(r'''<img\b(?:[^>"']|"[^"]*"|'[^']*')*>''', re.I | re.S)
IMAGE_ATTRIBUTE_RE = re.compile(
    r'''\s+(?P<name>[^\s=/>]+)\s*=\s*(?P<value>"[^"]*"|'[^']*'|[^\s>]+)''', re.S)
IMAGE_BLOCK_RE = re.compile(r'<p\b[^>]*>\s*<img\b[^>]*>\s*</p>|<img\b[^>]*>', re.I | re.S)
STRUCTURAL_TAG_RE = re.compile(r'<\s*(/?)\s*([a-z][\w:-]*)\b[^>]*>', re.I | re.S)
TRANSPARENT_IMAGE_TAGS = frozenset({'p','div','section','span','strong','em','b','i','u','a','br'})
MAX_DRAFT_CATALOG = 1000
WECHAT_DRAFT_WRITABLE_FIELDS = ('title','author','digest','content','content_source_url',
                                'thumb_media_id','need_open_comment','only_fans_can_comment')


class DraftCatalogError(ValueError):
    """Safe category only; do not include draft IDs, URLs or article text."""


def strict_draft_group_match(actual, expected):
    if not actual or len(actual) != len(expected):
        return False
    return all(prose_identity(a) == prose_identity(b)
               and html.unescape(str(a.get('content_source_url') or '')).strip()
               == html.unescape(str(b.get('content_source_url') or '')).strip()
               for a, b in zip(actual, expected))


def saved_receipt_author_change_only(actual, expected):
    """Allow a live author edit only after the original receipt ID still resolves.

    This is not a catalog matching rule. Count, order, titles, prose and source
    URLs retain the strict identity contract; the caller keeps live authors as
    the update/readback baseline instead of restoring receipt authors.
    """
    if not actual or len(actual) != len(expected):
        return False
    if not any(prose_identity(a)[1] != prose_identity(b)[1] for a, b in zip(actual, expected)):
        return False
    with_receipt_authors = [dict(a, author=b.get('author')) for a, b in zip(actual, expected)]
    return strict_draft_group_match(with_receipt_authors, expected)


def saved_receipt_single_removed_index(actual, expected):
    """Identify one uniquely deleted member; never use this to find another ID."""
    if not actual or len(actual) != len(expected) - 1:
        return None
    matches = []
    for removed in range(len(expected)):
        retained = expected[:removed] + expected[removed + 1:]
        with_receipt_authors = [dict(a, author=b.get('author')) for a, b in zip(actual, retained)]
        if strict_draft_group_match(with_receipt_authors, retained):
            matches.append(removed)
    return matches[0] if len(matches) == 1 else None


def group_identity_diagnostics(actual, expected):
    """Field-level evidence without article text, titles, source URLs or IDs."""
    def fields(article):
        title, author, prose = prose_identity(article)
        return {'title':title, 'author':author, 'prose':prose,
                'source_url':html.unescape(str(article.get('content_source_url') or '')).strip()}
    rows = []
    for index in range(max(len(actual), len(expected))):
        a = fields(actual[index]) if index < len(actual) else fields({})
        b = fields(expected[index]) if index < len(expected) else fields({})
        matches = {key:a[key] == b[key] for key in b}
        differences = {key:{'actual_sha256':hashlib.sha256(a[key].encode()).hexdigest(),
                            'expected_sha256':hashlib.sha256(b[key].encode()).hexdigest()}
                       for key in b if not matches[key]}
        rows.append({'index':index, 'matches':matches, 'differences':differences})
    return {'actual_article_count':len(actual), 'expected_article_count':len(expected),
            'article_count_matches':len(actual) == len(expected), 'articles':rows}


def returned_article_diagnostics(actual, expected):
    # Returned URL/thumbnail fields can change independently of prose. Keep
    # evidence for a later narrow fix; do not assume a difference is harmless.
    known = {'title','author','content','digest','content_source_url','thumb_media_id',
             'thumb_url','url','show_cover_pic','need_open_comment','only_fans_can_comment',
             'article_type','is_deleted','copyright_stat'}
    changed = {key for key in set(actual) | set(expected) if actual.get(key) != expected.get(key)}
    def digest(value):
        return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    return {'changed_fields':{key:{'matches':False, 'writable':key in WECHAT_DRAFT_WRITABLE_FIELDS,
                                  'actual_sha256':digest(actual.get(key)),
                                  'expected_sha256':digest(expected.get(key))} for key in sorted(changed & known)},
            'unrecognized_changed_field_count':len(changed-known)}


def writable_group_unchanged(actual, expected):
    return len(actual) == len(expected) and all(
        all(a.get(field) == b.get(field) for field in WECHAT_DRAFT_WRITABLE_FIELDS)
        for a, b in zip(actual, expected))


def record_unresolved_group(report, output, index, media_id, expected, category, *,
                            diagnostics=None, changed=None, errcode=None, remaining_articles=None,
                            uncertain_articles=0, preserved_removal=None):
    remaining = len(expected) if remaining_articles is None else remaining_articles
    report['unresolved_draft_count'] += 1
    report['unresolved_article_count'] += remaining
    report['uncertain_article_count'] += uncertain_articles
    report.update(partial=True, fully_repaired=False, ok=False, status='partial')
    row = {'index':index, 'identity':hashlib.sha256(media_id.encode()).hexdigest(),
           'articles':len(expected), 'remaining_articles':remaining,
           'processed_articles':len(expected)-remaining, 'uncertain_articles':uncertain_articles,
           'verified':False, 'resolution':category,
           'status':'unresolved', 'changed':changed or []}
    if diagnostics is not None:row['identity_diagnostics'] = diagnostics
    if errcode is not None:row['wechat_errcode'] = errcode
    if preserved_removal:row.update(preserved_removal)
    report['drafts'].append(row)
    (output/'progress.json').write_text(json.dumps(report,indent=2))
    safe = {'draft_index':index, 'status':'unresolved', 'category':category,
            'unresolved_article_count':report['unresolved_article_count']}
    if diagnostics is not None:safe['identity_diagnostics'] = diagnostics
    print(json.dumps(safe), flush=True)


def pending_legacy_media_matches(actual, expected, media_checks):
    """Defer only an unchanged future member's known missing-credit failure."""
    def legacy_captions(article):
        return [visible_wechat_content_text(match.group(0))
                for match in IMAGE_CREDIT_PARAGRAPH_RE.finditer(str(article.get('content') or ''))
                if legacy_stripped_commons_credit(match.group(0))]
    original = legacy_captions(expected)
    return (bool(original) and original == legacy_captions(actual)
            and writable_group_unchanged([actual], [expected])
            and media_checks.get('matches_cover') is True
            and media_checks.get('matches_inline_images') is True
            and generated_image_credits(actual.get('content')) == generated_image_credits(expected.get('content'))
            and media_checks.get('incomplete_image_credit_count') == len(original)
            and media_checks.get('expected_incomplete_image_credit_count') == len(original))


def verify_repair_readback(session, token, media_id, timeout, expected, *, processed_count=None):
    """Validate a returned representation and retain its canonical write fields.

    Do not use the uploader's logging wrapper here: its messages include raw
    media IDs. Only sanitized counts/diagnostics leave the repair workflow.
    """
    if processed_count is None:
        processed_count = len(expected)
    if type(processed_count) is not int or not 1 <= processed_count <= len(expected):
        raise ValueError('Invalid processed article count')
    data = get_draft(session, token, media_id, timeout)
    articles = draft_news_items(data)
    checks = summarize_draft_get_response(data, len(expected), expected)
    checks['matches_prose_and_source'] = strict_draft_group_match(articles, expected)
    pending = []
    media_checks = checks.get('media_contract', [])
    processed_media_matches = len(articles) == len(expected) == len(media_checks)
    if processed_media_matches:
        for index, media_check in enumerate(media_checks):
            if media_check.get('matches'):
                continue
            if index >= processed_count and pending_legacy_media_matches(articles[index], expected[index], media_check):
                pending.append(index)
            else:
                processed_media_matches = False
    # Keep the full-group result truthful while processing an earlier member.
    # At the last member there are no deferred indices: full media must pass.
    checks['pending_legacy_media_indices'] = pending
    checks['matches_processed_media_contract'] = processed_media_matches
    checks['ok'] = bool(processed_media_matches and checks['matches_prose_and_source']
                        and checks.get('matches_expected_article_count')
                        and checks.get('matches_expected_titles')
                        and checks.get('matches_editorial_contract'))
    return checks, articles


def read_complete_draft_catalog(session, token, timeout):
    """Read a bounded complete catalog; never infer uniqueness from a prefix."""
    rows = []; seen = set(); total = None
    while total is None or len(rows) < total:
        response = post_wechat_json(session,
            f'https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token={token}',
            {'offset':len(rows), 'count':20, 'no_content':0}, timeout, max_attempts=1)
        data = parse_wechat_json(response, 'draft/batchget receipt recovery')
        reported = data.get('total_count')
        if type(reported) is not int or reported < 0:
            raise DraftCatalogError('catalog_invalid_count')
        if reported > MAX_DRAFT_CATALOG:
            raise DraftCatalogError('catalog_exceeds_scan_bound')
        if total is not None and reported != total:
            raise DraftCatalogError('catalog_changed_during_scan')
        total = reported
        items = data.get('item', [] if total == 0 else None)
        if not isinstance(items, list) or (not items and len(rows) < total) or len(rows) + len(items) > total:
            raise DraftCatalogError('catalog_incomplete_page')
        for item in items:
            if not isinstance(item, dict):
                raise DraftCatalogError('catalog_invalid_item')
            media_id = item.get('media_id')
            container = item.get('content') if isinstance(item.get('content'), dict) else item
            raw_articles = container.get('news_item', container.get('articles'))
            articles = draft_news_items(item)
            if (not isinstance(media_id, str) or not media_id.strip() or media_id in seen
                    or not isinstance(raw_articles, list) or any(not isinstance(a, dict) for a in raw_articles)
                    or not articles or any(not isinstance(a.get('title'), str) or not a['title']
                                          or not isinstance(a.get('content'), str) or not a['content'] for a in articles)):
                raise DraftCatalogError('catalog_invalid_or_duplicate_item')
            seen.add(media_id); rows.append(item)
        if total == 0:
            break
    return rows


def resolve_unique_receipt_candidate(catalog, expected, reserved_ids):
    matches = [item for item in catalog if strict_draft_group_match(draft_news_items(item), expected)]
    if not matches:
        return None, 'invalid_receipt_no_current_match'
    if len(matches) != 1:
        return None, 'invalid_receipt_ambiguous_match'
    if matches[0]['media_id'] in reserved_ids:
        return None, 'invalid_receipt_target_already_bound'
    return matches[0], 'unique_exact_group_match'


def prose_identity(article):
    return (str(article.get('title') or ''), str(article.get('author') or ''), article_prose_text(article.get('content')))


def article_body_images(content):
    # One downloaded image may occur more than once in an old fallback article.
    # Replace all occurrences together, and do not count it as three pictures.
    images = {}
    for url, alt in wechat_content_images(content):
        if alt != 'KC桌面':
            images.setdefault(wechat_image_url_identity(url) or url, (url, alt))
    return list(images.values())


def fetch_wechat_image(session, url, target, timeout):
    """Bounded direct download from the existing WeChat CDN, no redirects."""
    try:
        parts = urlsplit(html.unescape(url))
        allowed = parts.scheme in {'http', 'https'} and parts.hostname in {'mmbiz.qpic.cn', 'mmbiz.qlogo.cn'} and not (parts.username or parts.password or parts.port or parts.fragment)
    except (ValueError, TypeError):
        allowed = False
    if not allowed:
        return 'untrusted_image_url'
    try:
        with session.get(url, timeout=min(timeout, 20), stream=True, allow_redirects=False) as response:
            if response.status_code != 200:
                return f'image_http_{response.status_code}'
            if int(response.headers.get('Content-Length', '0') or 0) > MAX_IMAGE_BYTES:
                return 'oversized_image'
            target.parent.mkdir(parents=True, exist_ok=True)
            size = 0
            with target.open('wb') as output:
                for chunk in response.iter_content(65536):
                    size += len(chunk)
                    if size > MAX_IMAGE_BYTES:
                        return 'oversized_image'
                    output.write(chunk)
        return article_image_rejection(target)
    except (requests.RequestException, OSError, ValueError, Image.DecompressionBombError):
        return 'image_download_or_decode_failed'


def replace_image(content, old_url, new_url, credit, *, managed_annotations=False):
    if managed_annotations:
        # Preserve the editor's surrounding markup exactly. Caption cleanup
        # removes the separately recognized notes after every photo is rebound;
        # consuming wrapper closing tags here would corrupt the document tree.
        if not new_url or credit:
            raise ValueError('managed_photo_replacement_requires_caption_free_url')
        old_identity = wechat_image_url_identity(old_url)
        replaced = 0
        def update_tag(match):
            nonlocal replaced
            refs = wechat_content_images(match.group(0))
            if not refs or refs[0][1] == 'KC桌面':
                return match.group(0)
            same = (wechat_image_url_identity(refs[0][0]) == old_identity if old_identity
                    else html.unescape(refs[0][0]) == html.unescape(old_url))
            if not same:
                return match.group(0)
            def update_attribute(attribute):
                if attribute.group('name').lower() not in {'src', 'data-src'}:
                    return attribute.group(0)
                value = attribute.group('value')
                quote = value[0] if value[0] in {'"', "'"} else '"'
                prefix = attribute.group(0)[:attribute.start('value')-attribute.start()]
                return prefix+quote+html.escape(new_url,quote=True)+quote
            # Consume every complete attribute value before considering the
            # next name. A src-like word inside alt/title is ordinary text.
            result = IMAGE_ATTRIBUTE_RE.sub(update_attribute, match.group(0))
            rewritten = wechat_content_images(result)
            if (not rewritten or wechat_image_url_identity(rewritten[0][0])
                    != wechat_image_url_identity(new_url)):
                raise ValueError('managed_photo_url_not_rewritten')
            replaced += 1
            return result
        result = MANAGED_IMG_RE.sub(update_tag, content)
        if not replaced:
            raise ValueError('Expected image element was not found')
        return result
    replaced = 0
    pieces = []
    cursor = 0
    for match in IMAGE_BLOCK_RE.finditer(content):
        if match.start() < cursor:
            continue
        block = match.group(0)
        refs = wechat_content_images(block)
        if not refs or refs[0][1] == 'KC桌面':
            continue
        old_identity = wechat_image_url_identity(old_url)
        same_image = (wechat_image_url_identity(refs[0][0]) == old_identity if old_identity
                      else html.unescape(refs[0][0]) == html.unescape(old_url))
        if not same_image:
            continue
        if not block.lower().startswith('<p'):
            # Generated images occupy their own paragraph. Do not inject a
            # paragraph credit into a manually rearranged text paragraph.
            prefix = content[:match.start()].lower()
            if prefix.rfind('<p') > prefix.rfind('</p>'):
                raise ValueError('Image is inside an unsupported text paragraph')
        # Rewrite only src/data-src attributes of the matched image element.
        result = IMG_RE.sub(lambda image: re.sub(r'\b(?:src|data-src)\s*=\s*([\"\']).*?\1', lambda m: m.group(0).split('=', 1)[0] + '="' + html.escape(new_url, quote=True) + '"', image.group(0), flags=re.I | re.S), block) if new_url else ''
        end = match.end()
        # Replace the managed credit together with its image, including any
        # duplicate adjacent credits left by an interrupted historical repair.
        while True:
            tail = content[end:]
            whitespace = len(tail) - len(tail.lstrip())
            previous_credit = CREDIT_RE.match(tail, whitespace)
            if not previous_credit or not ((managed_annotations and managed_image_annotation_kind(previous_credit.group(0)))
                                           or generated_image_credit_signature(previous_credit.group(0)) is not None
                                           or legacy_stripped_commons_credit(previous_credit.group(0))):
                break
            end += previous_credit.end()
        pieces.append(content[cursor:match.start()])
        pieces.append(result + credit)
        cursor = end
        replaced += 1
    if not replaced:
        raise ValueError('Expected image element was not found')
    pieces.append(content[cursor:])
    return ''.join(pieces)


def next_managed_image_credit(content, offset):
    """Cross only empty presentation markup between an image and its note.

    Never cross visible text, comments, a new image or another semantic tag.
    HTML entities are decoded solely to decide whether a text gap is blank.
    """
    while offset < len(content):
        end = content.find('<', offset)
        if end < 0:
            return None
        if html.unescape(content[offset:end]).strip():
            return None
        offset = end
        credit = CREDIT_RE.match(content, offset)
        if credit and managed_image_annotation_kind(credit.group(0)):
            return credit
        tag = STRUCTURAL_TAG_RE.match(content, offset)
        if not tag or tag.group(2).lower() not in TRANSPARENT_IMAGE_TAGS:
            return None
        offset = tag.end()
    return None


def adjacent_image_credits(content, url, *, managed_annotations=False):
    """Yield only managed credits immediately following this non-contact image."""
    identity = wechat_image_url_identity(url)
    for match in IMAGE_BLOCK_RE.finditer(content):
        refs = wechat_content_images(match.group(0))
        if refs and refs[0][1] != 'KC桌面' and wechat_image_url_identity(refs[0][0]) == identity:
            end = match.end()
            while True:
                tail = content[end:]
                credit = (next_managed_image_credit(content, end) if managed_annotations
                          else CREDIT_RE.match(tail, len(tail)-len(tail.lstrip())))
                if not credit or not ((managed_annotations and managed_image_annotation_kind(credit.group(0)))
                                      or generated_image_credit_signature(credit.group(0)) is not None
                                      or legacy_stripped_commons_credit(credit.group(0))):
                    break
                yield credit.group(0)
                end = credit.end() if managed_annotations else end+credit.end()


def has_editorial_credit(content, url):
    return any(adjacent_image_credits(content, url))


def has_incomplete_editorial_credit(content, url):
    return any(legacy_stripped_commons_credit(credit) for credit in adjacent_image_credits(content, url))


def has_source_image_reference(alt):
    # Historical renderer labels such as "研报原图 1" and contextual prose were
    # also assigned to Pollinations images. Only an explicit retained-asset
    # reference supplies source provenance in a receipt without inline metadata.
    return bool(re.fullmatch(r'(?:assets/)?source_image_\d+\.(?:png|jpe?g|webp|gif|bmp|tiff?)', str(alt or '').strip(), re.I))


def build_media_repair(session, token, article, directory, timeout, min_images=3):
    result = copy.deepcopy(article)
    content = str(article.get('content') or '')
    body = article_body_images(content)
    replacements = []; candidates = []; sources = []; inspected = []
    for index, (url, alt) in enumerate(body, 1):
        local = directory / f'body_{index:02d}.jpg'
        rejection = fetch_wechat_image(session, url, local, timeout)
        if re.search(r'(?:^|/)xhs_card_\d+\.(?:png|jpe?g)$', alt, re.I):
            rejection = 'generated_title_or_chart_card'
        if has_incomplete_editorial_credit(content, url):
            rejection = 'legacy_commons_credit_missing_source'
        inspected.append((index, url, alt, local, rejection))
    # Absence of a credit is not evidence of an original chart: legacy generated
    # photos were uncredited too. Keep good legacy images, without relabeling
    # them as source figures or inventing access to missing original PDF assets.
    usable_existing = [local for _, _, _, local, reason in inspected if not reason]
    original_candidates = [local for _, url, alt, local, reason in inspected
                           if not reason and has_source_image_reference(alt) and not has_editorial_credit(content, url)]
    for index, url, _alt, local, rejection in inspected:
        if rejection:
            if original_candidates:
                content = replace_image(content, url, '', '')
                replacements.append({'index': index, 'reason': rejection, 'action': 'remove_invalid_image'})
                continue
            local, metadata = download_editorial_image(session, str(article.get('title') or ''), local, min(timeout, 15), index=index, cache_dir=directory.parent / 'licensed_cache')
            new_url = upload_article_image(session, token, local, timeout)
            content = replace_image(content, url, new_url, attribution_html(metadata))
            replacements.append({'index': index, 'reason': rejection});sources.append(metadata['source'])
        candidates.append(local)
    added = 0
    minimum = len(candidates) if usable_existing else min_images
    while len(candidates) < minimum:
        index = len(candidates) + 1
        local, metadata = download_editorial_image(session, str(article.get('title') or ''), directory / f'fill_{index:02d}.jpg', min(timeout, 15), index=index, cache_dir=directory.parent / 'licensed_cache')
        new_url = upload_article_image(session, token, local, timeout)
        illustration = image_html(new_url, alt='主题配图') + attribution_html(metadata)
        # Insert before the trailing contact card, leaving its exact content intact.
        footer = next((m for m in IMG_RE.finditer(content) if any(alt == 'KC桌面' for _, alt in wechat_content_images(m.group(0)))), None)
        insertion = content.rfind('<p', 0, footer.start()) if footer else -1
        if insertion < 0: insertion = content.rfind('</section>')
        if insertion < 0: insertion = len(content)
        content = content[:insertion] + illustration + content[insertion:]
        candidates.append(local);sources.append(metadata['source']);added += 1
    cover = directory / 'old_cover.jpg'
    cover_issue = fetch_wechat_image(session, str(article.get('thumb_url') or ''), cover, timeout)
    if any(reason == 'legacy_commons_credit_missing_source' for _, _, _, _, reason in inspected):
        # The previous cover may be a rendition of the now-unattributable
        # Commons image. Bind it to a retained source/credited candidate rather
        # than claiming the old picture was visually defective.
        cover_issue = 'license_source_lost'
    if cover_issue:
        if not candidates:
            raise ValueError('No usable image available for cover')
        normalized = prepare_cover_upload_image((original_candidates or usable_existing or candidates)[0], directory, 'replacement')
        result['thumb_media_id'] = upload_cover_material(session, token, normalized, timeout)
        result.pop('pic_crop_235_1', None);result.pop('pic_crop_1_1', None)
    result['content'] = content
    if prose_identity(result) != prose_identity(article):
        raise ValueError('Media repair changed article prose')
    if len(content.encode('utf-8')) > 20000:
        raise ValueError('Media repair exceeds article byte budget')
    cover_source = ('retained_source_reference' if original_candidates else 'retained_body_image' if usable_existing else 'editorial_fallback') if cover_issue else 'unchanged'
    return result, {'cover_replaced': bool(cover_issue), 'cover_reason': cover_issue, 'cover_source': cover_source, 'body_replacements': replacements, 'body_added': added, 'sources': sources}


def repair_drafts(drafts, session, token, output, timeout, apply):
    output.mkdir(parents=True, exist_ok=True)
    report = {'applied': apply, 'drafts': [], 'article_count': 0, 'expected_article_count':sum(len(d['articles']) for d in drafts),
              'changed_articles': 0, 'cover_replacements': 0, 'body_replacements': 0, 'body_added': 0, 'sources': {},
              'updated_articles':0, 'recovered_receipt_groups':0, 'unresolved_draft_count':0, 'unresolved_article_count':0,
              'preserved_removed_article_count':0,
              'uncertain_article_count':0,
              'partial':False, 'fully_repaired':False, 'ok':False, 'status':'in_progress'}
    catalog = None; catalog_error = None
    reserved_ids = {draft['media_id'] for draft in drafts}
    for draft_index, draft in enumerate(drafts, 1):
        media_id = draft['media_id']
        expected = materialize_private_article_payload(draft['articles'], os.environ.get('PORTAL_SITE_URL', ''))
        resolution = 'saved_receipt_id'
        resolution_diagnostics = None
        preserved_removal = None
        saved_receipt_id_valid = False
        try:
            data = get_draft(session, token, media_id, timeout)
            saved_receipt_id_valid = True
        except WeChatError as exc:
            if exc.errcode != 40007:
                raise
            if catalog is None and catalog_error is None:
                try:
                    catalog = read_complete_draft_catalog(session, token, timeout)
                except DraftCatalogError as scan_error:
                    catalog_error = str(scan_error)
            candidate, resolution = (None, catalog_error) if catalog_error else resolve_unique_receipt_candidate(catalog, expected, reserved_ids)
            if candidate is not None:
                candidate_id = candidate['media_id']
                try:
                    data = get_draft(session, token, candidate_id, timeout)
                except WeChatError as confirmation_error:
                    if confirmation_error.errcode != 40007:
                        raise
                    candidate = None; resolution = 'matched_candidate_no_longer_available'
                if candidate is not None and not strict_draft_group_match(draft_news_items(data), expected):
                    resolution_diagnostics = group_identity_diagnostics(draft_news_items(data), expected)
                    candidate = None; resolution = 'matched_candidate_changed_before_use'
                if candidate is not None:
                    media_id = candidate_id; reserved_ids.add(media_id)
                    report['recovered_receipt_groups'] += 1
            if candidate is None:
                record_unresolved_group(report, output, draft_index, media_id, expected, resolution,
                                        diagnostics=resolution_diagnostics, errcode=40007)
                continue
        actual = draft_news_items(data)
        if not strict_draft_group_match(actual, expected):
            if saved_receipt_id_valid and saved_receipt_author_change_only(actual, expected):
                resolution = 'author_change_preserved'
                print(json.dumps({'draft_index':draft_index, 'resolution':resolution}), flush=True)
            else:
                removed = saved_receipt_single_removed_index(actual, expected) if saved_receipt_id_valid else None
                if removed is None:
                    record_unresolved_group(report, output, draft_index, media_id, expected, 'saved_receipt_identity_mismatch',
                                            diagnostics=group_identity_diagnostics(actual, expected))
                    continue
                preserved_removal = {'original_articles':len(expected), 'current_articles':len(actual),
                                     'preserved_removed_original_index':removed}
                expected = expected[:removed] + expected[removed + 1:]
                report['preserved_removed_article_count'] += 1
                resolution = 'single_removed_article_preserved'
                print(json.dumps({'draft_index':draft_index, 'resolution':resolution, **preserved_removal}), flush=True)
        changed = []; interrupted = False
        for index, article in enumerate(actual):
            directory = output / 'assets' / f'{draft_index:02d}_{index:02d}'
            if not apply:
                # Audit downloads only, with no provider calls, uploads or writes.
                body = article_body_images(article.get('content'))
                issues = [fetch_wechat_image(session,u,directory/f'body_{i}.jpg',timeout) for i,(u,a) in enumerate(body)]
                cover_issue = fetch_wechat_image(session,str(article.get('thumb_url') or ''),directory/'cover.jpg',timeout)
                for i, (_url, alt) in enumerate(body):
                    if re.search(r'(?:^|/)xhs_card_\d+\.(?:png|jpe?g)$', alt, re.I):
                        issues[i] = 'generated_title_or_chart_card'
                    if has_incomplete_editorial_credit(article.get('content') or '', _url):
                        issues[i] = 'legacy_commons_credit_missing_source'
                if 'legacy_commons_credit_missing_source' in issues:
                    cover_issue = 'license_source_lost'
                has_usable_existing = any(not issue for issue in issues)
                facts = {'cover_replaced':bool(cover_issue),'cover_reason':cover_issue,'body_replacements':[{'index':i+1,'reason':v} for i,v in enumerate(issues) if v], 'body_added':0 if has_usable_existing else max(0,3-len(body)),'sources':[]}
            else:
                updated_this_article = False
                repaired, facts = build_media_repair(session, token, article, directory, timeout)
                if facts['cover_replaced'] or facts['body_replacements'] or facts['body_added']:
                    try:
                        fresh = draft_news_items(get_draft(session, token, media_id, timeout))
                    except WeChatError as preparation_error:
                        if preparation_error.errcode != 40007:raise
                        record_unresolved_group(report, output, draft_index, media_id, expected,
                                                'draft_unavailable_during_image_preparation', changed=changed, errcode=40007,
                                                remaining_articles=len(actual)-index, preserved_removal=preserved_removal)
                        interrupted = True; break
                    if not strict_draft_group_match(fresh, actual) or not writable_group_unchanged(fresh, actual):
                        diagnostics = group_identity_diagnostics(fresh, actual)
                        diagnostics['target_article_fields_unchanged'] = index < len(fresh) and fresh[index] == article
                        diagnostics['protected_group_identity_matches'] = strict_draft_group_match(fresh, actual)
                        diagnostics['writable_group_unchanged'] = writable_group_unchanged(fresh, actual)
                        diagnostics['target_returned_fields'] = returned_article_diagnostics(fresh[index] if index < len(fresh) else {}, article)
                        record_unresolved_group(report, output, draft_index, media_id, expected,
                                                'draft_changed_during_image_preparation', diagnostics=diagnostics, changed=changed,
                                                remaining_articles=len(actual)-index, preserved_removal=preserved_removal)
                        interrupted = True; break
                    if fresh[index] != article:
                        facts['response_only_field_changes'] = returned_article_diagnostics(fresh[index], article)
                        print(json.dumps({'draft_index':draft_index, 'article_index':index,
                                          'response_only_field_changes':facts['response_only_field_changes']}), flush=True)
                    payload = {key: repaired[key] for key in WECHAT_DRAFT_WRITABLE_FIELDS if key in repaired}
                    try:
                        response = post_wechat_json(session, f'https://api.weixin.qq.com/cgi-bin/draft/update?access_token={token}', {'media_id':media_id,'index':index,'articles':payload}, timeout, max_attempts=1)
                        if parse_wechat_json(response,'draft/update image repair').get('errcode') != 0:
                            raise ValueError('Draft media update not confirmed')
                    except WeChatError as update_error:
                        # Observed server refusal: the existing draft is queued
                        # for scheduled publication. Preserve that schedule and
                        # do not retry or cancel it; other groups are independent.
                        if update_error.errcode != 53407 or not update_error.errmsg.startswith('定时发布中，无法删除或修改'):
                            raise
                        record_unresolved_group(report, output, draft_index, media_id, expected,
                                                'scheduled_publish_locked', changed=changed, errcode=53407,
                                                remaining_articles=len(actual)-index, preserved_removal=preserved_removal)
                        interrupted = True; break
                    report['updated_articles'] += 1
                    updated_this_article = True
                    (output/'progress.json').write_text(json.dumps(report,indent=2))
                    print(json.dumps({'draft_index':draft_index, 'article_index':index,
                                      'updated_articles':report['updated_articles']}), flush=True)
                    actual[index] = repaired
                try:
                    verification, readback_articles = verify_repair_readback(session, token, media_id, timeout, actual, processed_count=index+1)
                except WeChatError as readback_error:
                    record_unresolved_group(report, output, draft_index, media_id, expected,
                                            'draft_readback_unavailable', changed=changed, errcode=readback_error.errcode,
                                            remaining_articles=len(actual)-index, uncertain_articles=int(updated_this_article),
                                            preserved_removal=preserved_removal)
                    interrupted = True; break
                if not verification['ok']:
                    diagnostics = group_identity_diagnostics(readback_articles, actual)
                    diagnostics['readback_checks'] = {key:bool(verification.get(key)) for key in (
                        'matches_expected_article_count','matches_expected_titles','matches_editorial_contract',
                        'matches_media_contract','matches_processed_media_contract','matches_prose_and_source')}
                    diagnostics['pending_legacy_media_indices'] = verification.get('pending_legacy_media_indices', [])
                    record_unresolved_group(report, output, draft_index, media_id, expected,
                                            'draft_image_readback_failed', diagnostics=diagnostics, changed=changed,
                                            remaining_articles=len(actual)-index, uncertain_articles=int(updated_this_article),
                                            preserved_removal=preserved_removal)
                    interrupted = True; break
                if updated_this_article:
                    # Only our just-written member gains a new concurrency
                    # baseline, after both prose/source and media validation.
                    actual[index] = copy.deepcopy(readback_articles[index])
            report['article_count'] += 1
            if facts['cover_replaced'] or facts['body_replacements'] or facts['body_added']:
                report['changed_articles'] += 1;changed.append({'index':index,**facts})
            report['cover_replacements'] += int(facts['cover_replaced'])
            report['body_replacements'] += len(facts['body_replacements']);report['body_added'] += facts['body_added']
            for source in facts['sources']: report['sources'][source] = report['sources'].get(source,0)+1
            (output/'progress.json').write_text(json.dumps(report,indent=2))
            print(json.dumps({key: report[key] for key in ('article_count','changed_articles','cover_replacements','body_replacements','body_added')}), flush=True)
        if not interrupted:
            report['drafts'].append({'index':draft_index, 'identity':hashlib.sha256(media_id.encode()).hexdigest(), 'articles':len(actual),'changed':changed,'verified':apply,'resolution':resolution, **(preserved_removal or {})})
    report['ok'] = report['unresolved_draft_count'] == 0
    report['partial'] = not report['ok']
    report['fully_repaired'] = bool(apply and report['ok'])
    report['status'] = 'complete' if report['ok'] else 'partial'
    (output/'progress.json').write_text(json.dumps(report,indent=2))
    return report


def caption_binding_diagnostics(article):
    """Bounded structural evidence only: no titles, prose, image URLs or IDs."""
    content = str(article.get('content') or '')
    captions = [match for match in CREDIT_RE.finditer(content)
                if managed_image_annotation_kind(match.group(0))]
    commons = [match for match in captions if managed_image_annotation_kind(match.group(0)) == 'commons']
    blocks = list(IMAGE_BLOCK_RE.finditer(content))
    images = wechat_content_images(content)
    records = []
    for ordinal, caption in enumerate(commons[:16], 1):
        before = [(index, block) for index, block in enumerate(blocks, 1) if block.end() <= caption.start()]
        previous = before[-1] if before else None
        gap = content[previous[1].end():caption.start()] if previous else content[:caption.start()]
        stripped_gap = strip_managed_image_annotations(gap)
        tags = [('end:' if match.group(1) else 'start:')+
                (match.group(2).lower() if match.group(2).lower() in TRANSPARENT_IMAGE_TAGS | {'img'} else 'other')
                for match in STRUCTURAL_TAG_RE.finditer(stripped_gap)]
        direct = not html.unescape(stripped_gap).strip()
        bound = False
        nearest = None
        if previous:
            index, block = previous
            refs = wechat_content_images(block.group(0))
            if refs:
                url, alt = refs[0]
                alt_kind = ('contact' if alt == 'KC桌面' else 'source_reference' if has_source_image_reference(alt)
                            else 'editorial' if alt in {'主题配图','主题示意图'} else 'other')
                nearest = {'ordinal':index, 'block_kind':'paragraph' if block.group(0).lower().startswith('<p') else 'image',
                           'alt_kind':alt_kind, 'identity_sha256':hashlib.sha256(wechat_image_url_identity(url).encode()).hexdigest(),
                           'has_src':bool(re.search(r'\ssrc\s*=',block.group(0),re.I)),
                           'has_data_src':bool(re.search(r'\sdata-src\s*=',block.group(0),re.I))}
                offset = block.end()
                while alt != 'KC桌面':
                    next_credit = next_managed_image_credit(content, offset)
                    if next_credit is None or next_credit.start() > caption.start():
                        break
                    if next_credit.start() == caption.start():
                        bound = True; break
                    offset = next_credit.end()
        signature = generated_image_credit_signature(caption.group(0))
        records.append({'ordinal':ordinal,
            'caption_sha256':hashlib.sha256(caption.group(0).encode()).hexdigest(),
            'wrapper':caption.group('tag').lower(),
            'has_managed_marker':bool(re.search(r'data-editorial-credit\s*=\s*[\"\']1[\"\']',caption.group(0),re.I)),
            'has_credit_class':bool(re.search(r'class\s*=\s*[\"\'][^\"\']*\bimage-credit\b',caption.group(0),re.I)),
            'signature_kind':'complete' if signature else 'legacy_stripped' if legacy_stripped_commons_credit(caption.group(0)) else 'unknown',
            'nearest_image':nearest, 'direct_adjacency':direct, 'transparent_adjacency':bound,
            'gap_tags':tags[:24], 'gap_tags_truncated':len(tags)>24,
            'gap_has_comment':'<!--' in stripped_gap,
            'gap_text_chars':len(visible_wechat_content_text(gap)),
            'gap_without_managed_notes_text_chars':len(visible_wechat_content_text(stripped_gap))})
    return {'managed_caption_counts':dict(Counter(managed_image_annotation_kind(match.group(0)) for match in captions)),
            'image_count':len(images), 'unique_body_image_count':len(article_body_images(content)),
            'commons_caption_count':len(commons), 'caption_records':records,
            'caption_records_truncated':len(commons)>16}


def caption_cleanup_plan(article):
    """Identify only deployed managed annotations and their adjacent photos."""
    content = str(article.get('content') or '')
    captions = [match.group(0) for match in CREDIT_RE.finditer(content)
                if managed_image_annotation_kind(match.group(0))]
    replace = []
    bound = []
    for index, (url, _alt) in enumerate(article_body_images(content), 1):
        credits = list(adjacent_image_credits(content, url, managed_annotations=True))
        commons = [credit for credit in credits if managed_image_annotation_kind(credit) == 'commons']
        bound.extend(commons)
        # An intact CC0 signature proves no display attribution is needed.
        # All CC BY or unknown/link-stripped Commons media must be replaced.
        if any(not (generated_image_credit_signature(credit)
                    and '/ Wikimedia Commons / CC0 1.0' in generated_image_credit_signature(credit)[0])
               for credit in commons):
            replace.append({'index':index, 'url':url, 'reason':'attributed_editorial_photo'})
    orphan = (Counter(credit for credit in captions if managed_image_annotation_kind(credit) == 'commons')
              - Counter(bound))
    if orphan:
        raise ValueError('unbound_commons_annotation')
    thumb = wechat_image_url_identity(str(article.get('thumb_url') or ''))
    cover_is_retained = bool(thumb and any(wechat_image_url_identity(url) == thumb
        and all(wechat_image_url_identity(item['url']) != thumb for item in replace)
        for url, _alt in article_body_images(content)))
    return {'captions_removed':len(captions), 'body_replacements':replace,
            'cover_replaced':bool(replace) and not cover_is_retained, 'body_added':0, 'sources':[]}


def build_caption_cleanup(session, token, article, directory, timeout, plan=None):
    """Remove known notes; replace only photos whose attribution would be lost."""
    facts = copy.deepcopy(plan if plan is not None else caption_cleanup_plan(article))
    result = copy.deepcopy(article)
    content = str(article.get('content') or '')
    replacement_cover = None
    for replacement in facts['body_replacements']:
        index = replacement['index']
        path, metadata = download_editorial_image(
            session, str(article.get('title') or ''), directory/f'photo_{index:02d}.jpg',
            min(timeout, 15), index=index, cache_dir=directory.parent/'photo_cache')
        # Provider metadata is retained privately, never rendered in the body.
        source = metadata.get('source')
        if source in {'commons', 'wikimedia_commons'} and metadata.get('license') != 'CC0 1.0':
            raise ValueError('replacement_photo_requires_attribution')
        if metadata.get('attribution_required') is True:
            raise ValueError('replacement_photo_requires_attribution')
        new_url = upload_article_image(session, token, path, timeout)
        content = replace_image(content, replacement.pop('url'), new_url, '', managed_annotations=True)
        replacement_cover = replacement_cover or path
        facts['sources'].append(str(source or 'unknown'))
    content = strip_managed_image_annotations(content)
    if replacement_cover is not None and facts['cover_replaced']:
        # Historic covers may be alternate renditions of any replaced photo;
        # bind the cover to the same approved replacement deterministically.
        normalized = prepare_cover_upload_image(replacement_cover, directory, 'caption_cleanup')
        result['thumb_media_id'] = upload_cover_material(session, token, normalized, timeout)
        result.pop('pic_crop_235_1', None);result.pop('pic_crop_1_1', None)
    result['content'] = content
    if visible_wechat_content_text(strip_managed_image_annotations(article.get('content'))) != visible_wechat_content_text(content):
        raise ValueError('caption_cleanup_changed_prose')
    if len(content.encode('utf-8')) > 20000:
        raise ValueError('caption_cleanup_exceeds_byte_budget')
    return result, facts


def cleanup_current_drafts(session, token, output, timeout, apply):
    """Audit/apply the complete live catalog without historical receipt guesses."""
    output.mkdir(parents=True, exist_ok=True)
    catalog = read_complete_draft_catalog(session, token, timeout)
    report = {'mode':'current_drafts_caption_cleanup', 'applied':apply, 'drafts':[],
              'article_count':0, 'expected_article_count':sum(len(draft_news_items(row)) for row in catalog),
              'changed_articles':0, 'updated_articles':0, 'captions_removed':0,
              'body_replacements':0, 'cover_replacements':0, 'body_added':0, 'sources':{},
              'unresolved_draft_count':0, 'unresolved_article_count':0, 'uncertain_article_count':0,
              'partial':False, 'fully_repaired':False, 'ok':False, 'status':'in_progress'}
    for draft_index, row in enumerate(catalog, 1):
        media_id = row['media_id']
        baseline = copy.deepcopy(draft_news_items(row))
        changed = []; interrupted = False
        if apply and any(managed_image_annotation_kind(match.group(0))
                         for article in baseline for match in CREDIT_RE.finditer(article.get('content') or '')):
            if any(not wechat_editorial_contract_check(article, article)['matches'] for article in baseline):
                record_unresolved_group(report, output, draft_index, media_id, baseline,
                                        'existing_editorial_contract_failed')
                continue
        for index, article in enumerate(baseline):
            updated = False
            try:
                facts = caption_cleanup_plan(article)
                if apply and facts['captions_removed']:
                    repaired, facts = build_caption_cleanup(session, token, article,
                        output/'assets'/f'{draft_index:04d}_{index:02d}', timeout, facts)
                    fresh = draft_news_items(get_draft(session, token, media_id, timeout))
                    if not writable_group_unchanged(fresh, baseline):
                        raise ValueError('draft_changed_during_caption_preparation')
                    payload = {key:repaired[key] for key in WECHAT_DRAFT_WRITABLE_FIELDS if key in repaired}
                    update_error = None
                    try:
                        response = post_wechat_json(session,
                            f'https://api.weixin.qq.com/cgi-bin/draft/update?access_token={token}',
                            {'media_id':media_id, 'index':index, 'articles':payload}, timeout, max_attempts=1)
                        if parse_wechat_json(response, 'draft/update caption cleanup').get('errcode') != 0:
                            raise ValueError('caption_update_not_confirmed')
                        report['updated_articles'] += 1
                    except (WeChatError, requests.RequestException) as exc:
                        # Read an uncertain result once. Never retry the write.
                        if isinstance(exc, WeChatError) and exc.errcode in {40007, 53407}:
                            raise
                        update_error = exc
                    updated = True
                    expected = copy.deepcopy(baseline); expected[index] = repaired
                    checks, returned = verify_repair_readback(session, token, media_id, timeout,
                                                              expected, processed_count=index+1)
                    if not checks['ok']:
                        raise ValueError('caption_readback_contract_failed')
                    if caption_cleanup_plan(returned[index])['captions_removed']:
                        raise ValueError('caption_readback_still_present')
                    # The provider can normalize media URLs, but all other write
                    # fields and untouched group members must remain unchanged.
                    protected = [key for key in WECHAT_DRAFT_WRITABLE_FIELDS if key not in {'content','thumb_media_id'}]
                    if (any(returned[index].get(key) != repaired.get(key) for key in protected)
                            or not writable_group_unchanged(returned[:index]+returned[index+1:],
                                                            baseline[:index]+baseline[index+1:])):
                        raise ValueError('caption_readback_protected_fields_changed')
                    if update_error is not None:
                        report['updated_articles'] += 1
                    baseline[index] = copy.deepcopy(returned[index])
                report['article_count'] += 1
                if facts['captions_removed']:
                    safe_facts = copy.deepcopy(facts)
                    for replacement in safe_facts['body_replacements']:
                        replacement.pop('url', None)
                    changed.append({'index':index, **safe_facts})
                    report['changed_articles'] += 1
                    report['captions_removed'] += facts['captions_removed']
                    report['body_replacements'] += len(facts['body_replacements'])
                    report['cover_replacements'] += int(facts['cover_replaced'])
                    for source in facts['sources']:
                        report['sources'][source] = report['sources'].get(source, 0)+1
            except (WeChatError, requests.RequestException, ValueError, OSError) as exc:
                category = ('scheduled_publish_locked' if isinstance(exc, WeChatError) and exc.errcode == 53407
                            else 'draft_unavailable' if isinstance(exc, WeChatError) and exc.errcode == 40007
                            else str(exc) if isinstance(exc, ValueError) and re.fullmatch(r'[a-z_]{1,100}', str(exc))
                            else 'caption_cleanup_failed')
                record_unresolved_group(report, output, draft_index, media_id, baseline, category,
                    changed=changed, remaining_articles=len(baseline)-index, uncertain_articles=int(updated),
                    errcode=exc.errcode if isinstance(exc, WeChatError) else None,
                    diagnostics=caption_binding_diagnostics(article) if category == 'unbound_commons_annotation' else None)
                interrupted = True; break
            (output/'progress.json').write_text(json.dumps(report, indent=2))
            print(json.dumps({key:report[key] for key in ('article_count','changed_articles','captions_removed','updated_articles')}), flush=True)
        if not interrupted:
            report['drafts'].append({'index':draft_index, 'identity':hashlib.sha256(media_id.encode()).hexdigest(),
                                    'articles':len(baseline), 'changed':changed, 'verified':apply,
                                    'resolution':'current_catalog'})
    report['ok'] = report['unresolved_draft_count'] == 0
    report['partial'] = not report['ok']
    report['fully_repaired'] = bool(apply and report['ok'])
    report['status'] = 'complete' if report['ok'] else 'partial'
    (output/'progress.json').write_text(json.dumps(report, indent=2))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--artifact-root', type=Path)
    source.add_argument('--current-drafts', action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--apply', action='store_true');parser.add_argument('--timeout',type=int,default=60)
    args = parser.parse_args()
    with requests.Session() as session:
        token=get_stable_access_token(session,os.environ['WECHAT_MP_APPID'],os.environ['WECHAT_MP_APPSECRET'],args.timeout)
        report=(cleanup_current_drafts(session,token,args.output,args.timeout,args.apply) if args.current_drafts
                else repair_drafts(load_drafts(args.artifact_root),session,token,args.output,args.timeout,args.apply))
    (args.output/'result.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='drafts'}))
    return 1 if args.current_drafts and not report['ok'] else 0
if __name__=='__main__':
    raise SystemExit(main())
