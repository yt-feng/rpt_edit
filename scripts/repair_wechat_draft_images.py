#!/usr/bin/env python3
"""Repair media in receipt-bound existing drafts; never add, delete or publish."""
from __future__ import annotations
import argparse
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
    post_wechat_json, parse_wechat_json, prepare_cover_upload_image,
    upload_article_image, upload_cover_material, image_html, verify_draft_get,
    wechat_image_url_identity, WeChatError,
)

MAX_IMAGE_BYTES = 12 * 1024 * 1024
CREDIT_RE = re.compile(r'<p\b[^>]*\bdata-editorial-credit\s*=\s*(["\'])1\1[^>]*>.*?</p>', re.I | re.S)
IMG_RE = re.compile(r'<img\b[^>]*>', re.I | re.S)
IMAGE_BLOCK_RE = re.compile(r'<p\b[^>]*>\s*<img\b[^>]*>\s*</p>|<img\b[^>]*>', re.I | re.S)
MAX_DRAFT_CATALOG = 1000


class DraftCatalogError(ValueError):
    """Safe category only; do not include draft IDs, URLs or article text."""


def strict_draft_group_match(actual, expected):
    if not actual or len(actual) != len(expected):
        return False
    return all(prose_identity(a) == prose_identity(b)
               and html.unescape(str(a.get('content_source_url') or '')).strip()
               == html.unescape(str(b.get('content_source_url') or '')).strip()
               for a, b in zip(actual, expected))


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


def replace_image(content, old_url, new_url, credit):
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
            if not previous_credit or generated_image_credit_signature(previous_credit.group(0)) is None:
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


def has_editorial_credit(content, url):
    identity = wechat_image_url_identity(url)
    for match in IMAGE_BLOCK_RE.finditer(content):
        refs = wechat_content_images(match.group(0))
        if refs and wechat_image_url_identity(refs[0][0]) == identity:
            tail = content[match.end():].lstrip()
            credit = CREDIT_RE.match(tail)
            if credit and generated_image_credit_signature(credit.group(0)) is not None:
                return True
    return False


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
              'recovered_receipt_groups':0, 'unresolved_draft_count':0, 'unresolved_article_count':0}
    catalog = None; catalog_error = None
    reserved_ids = {draft['media_id'] for draft in drafts}
    for draft_index, draft in enumerate(drafts, 1):
        media_id = draft['media_id']
        expected = materialize_private_article_payload(draft['articles'], os.environ.get('PORTAL_SITE_URL', ''))
        resolution = 'saved_receipt_id'
        try:
            data = get_draft(session, token, media_id, timeout)
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
                    candidate = None; resolution = 'matched_candidate_changed_before_use'
                if candidate is not None:
                    media_id = candidate_id; reserved_ids.add(media_id)
                    report['recovered_receipt_groups'] += 1
            if candidate is None:
                report['unresolved_draft_count'] += 1; report['unresolved_article_count'] += len(expected)
                report['drafts'].append({'index':draft_index, 'identity':hashlib.sha256(media_id.encode()).hexdigest(),
                                        'articles':len(expected), 'verified':False, 'resolution':resolution,
                                        'status':'unresolved', 'wechat_errcode':40007, 'changed':[]})
                (output/'progress.json').write_text(json.dumps(report,indent=2))
                print(json.dumps({'draft_index':draft_index, 'status':'unresolved', 'category':resolution,
                                  'unresolved_article_count':report['unresolved_article_count']}), flush=True)
                continue
        actual = draft_news_items(data)
        if not strict_draft_group_match(actual, expected):
            raise ValueError(f'Draft {draft_index} prose differs from original receipt; no overwrite')
        changed = []
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
                has_usable_existing = any(not issue for issue in issues)
                facts = {'cover_replaced':bool(cover_issue),'cover_reason':cover_issue,'body_replacements':[{'index':i+1,'reason':v} for i,v in enumerate(issues) if v], 'body_added':0 if has_usable_existing else max(0,3-len(body)),'sources':[]}
            else:
                repaired, facts = build_media_repair(session, token, article, directory, timeout)
                if facts['cover_replaced'] or facts['body_replacements'] or facts['body_added']:
                    fresh = draft_news_items(get_draft(session, token, media_id, timeout))
                    if len(fresh) != len(actual) or fresh[index] != article:
                        raise ValueError('Draft changed during image preparation; no overwrite')
                    allowed = ('title','author','digest','content','content_source_url','thumb_media_id','need_open_comment','only_fans_can_comment')
                    payload = {key: repaired[key] for key in allowed if key in repaired}
                    response = post_wechat_json(session, f'https://api.weixin.qq.com/cgi-bin/draft/update?access_token={token}', {'media_id':media_id,'index':index,'articles':payload}, timeout, max_attempts=1)
                    if parse_wechat_json(response,'draft/update image repair').get('errcode') != 0:
                        raise ValueError('Draft media update not confirmed')
                    actual[index] = repaired
                verification = verify_draft_get(session, token, media_id, timeout, len(actual), actual)
                if not verification['ok']:
                    raise ValueError('Draft image readback failed')
            report['article_count'] += 1
            if facts['cover_replaced'] or facts['body_replacements'] or facts['body_added']:
                report['changed_articles'] += 1;changed.append({'index':index,**facts})
            report['cover_replacements'] += int(facts['cover_replaced'])
            report['body_replacements'] += len(facts['body_replacements']);report['body_added'] += facts['body_added']
            for source in facts['sources']: report['sources'][source] = report['sources'].get(source,0)+1
            (output/'progress.json').write_text(json.dumps(report,indent=2))
            print(json.dumps({key: report[key] for key in ('article_count','changed_articles','cover_replacements','body_replacements','body_added')}), flush=True)
        report['drafts'].append({'index':draft_index, 'identity':hashlib.sha256(media_id.encode()).hexdigest(), 'articles':len(actual),'changed':changed,'verified':apply,'resolution':resolution})
    report['ok'] = report['unresolved_draft_count'] == 0
    report['partial'] = not report['ok']
    report['fully_repaired'] = bool(apply and report['ok'])
    report['status'] = 'complete' if report['ok'] else 'partial'
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact-root', type=Path, required=True);parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--apply', action='store_true');parser.add_argument('--timeout',type=int,default=60)
    args = parser.parse_args();drafts=load_drafts(args.artifact_root)
    with requests.Session() as session:
        token=get_stable_access_token(session,os.environ['WECHAT_MP_APPID'],os.environ['WECHAT_MP_APPSECRET'],args.timeout)
        report=repair_drafts(drafts,session,token,args.output,args.timeout,args.apply)
    (args.output/'result.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='drafts'}))
    return 0
if __name__=='__main__':
    raise SystemExit(main())
