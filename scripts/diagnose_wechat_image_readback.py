#!/usr/bin/env python3
"""Read-only, text-free diagnostics for two uncertain historical image updates.

No write payload is reconstructed. Comparisons explicitly distinguish the saved
original receipt from the unavailable post-repair request. Candidate credit
normalization is diagnostic evidence only and never grants draft acceptance.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import hashlib
from html.parser import HTMLParser
import io
import json
import os
from pathlib import Path
import re
from urllib.parse import parse_qs, urlsplit

from free_editorial_images import attribution_caption
from push_portal_translated_to_wechat_drafts import (
    article_prose_text, draft_news_items, generated_image_credits, generated_image_credit_signature, get_draft,
    IMAGE_CREDIT_PARAGRAPH_RE, materialize_private_article_payload, normalize_space, parse_wechat_json,
    post_wechat_json, visible_wechat_content_text, wechat_content_images,
    wechat_image_url_identity, wechat_media_contract_check, WeChatError,
)
import restore_wechat_image_repair_receipts as receipts
from verify_existing_wechat_drafts import load_drafts

WORKFLOW = '.github/workflows/wechat-image-readback-diagnostics.yml'
REPAIR_RUN_ID = '38120919897'
TARGETS = {
    1: {'count': 8, 'article_index': 1,
        'receipt_id_sha256': 'a743dbb6c8aa3b345fa44147a2a8c7a28c7410f376f3bf37d4ee133223a23b4b',
        'repair_expected_prose_sha256': 'ad67bb7f9c35a8b79bf65aab41b21efa80b5c6f9654444efc1a2b9cb0fa6d37b'},
    6: {'count': 4, 'article_index': 1,
        'receipt_id_sha256': 'af9e8bd8053af47b990e7cdf4ef53aa1b0dda241f75a2195b03935387950deab',
        'repair_expected_prose_sha256': '3eb41822a4a6e266651f6fa0a1db99dc3b56f069e4dc8aaa559c4db91a1a1aa5'},
}
MAX_CONTENT_BYTES = 128 * 1024
MAX_NODES = 4096
MAX_CREDIT_CANDIDATES = 32
LOCAL_CAPTION = attribution_caption({'source': 'local_editorial'})
BLOCKS = {'p', 'div', 'section'}
KNOWN_TAGS = BLOCKS | {'span', 'strong', 'em', 'b', 'i', 'a', 'img', 'br'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
COMMONS_CAPTION_RE = re.compile(r'主题配图：(.{1,240}) / Wikimedia Commons / (CC0 1\.0|CC BY (2\.0|2\.5|3\.0|4\.0))；已裁剪与缩放，非报告原图。( 图片来源 · 许可)?')


class DiagnosticError(ValueError):
    pass


def require(value, category):
    if not value:
        raise DiagnosticError(category)


def digest(value):
    if isinstance(value, str):
        value = value.encode('utf-8')
    return hashlib.sha256(value).hexdigest()


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()


class CreditShapeParser(HTMLParser):
    """Capture bounded source spans without exporting arbitrary HTML or attrs."""
    def __init__(self, content):
        super().__init__(convert_charrefs=True)
        self.content = content
        self.lines = [0]
        for index, char in enumerate(content):
            if char == '\n':
                self.lines.append(index + 1)
        self.stack = []
        self.nodes = []
        self.malformed = False

    def character_offset(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        require(len(self.nodes) < MAX_NODES and len(self.stack) < 64, 'html_structure_bound')
        start = self.character_offset()
        node = {'tag': tag, 'attrs': dict(attrs), 'start': start,
                'end': start + len(self.get_starttag_text()), 'children': [], 'comment': False}
        self.nodes.append(node)
        for parent in self.stack:
            parent['children'].append(tag)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1]['tag'] != tag:
            self.malformed = True
            return
        node = self.stack.pop()
        close = self.content.find('>', self.character_offset())
        node['end'] = close + 1 if close >= 0 else len(self.content)

    def handle_comment(self, _value):
        for parent in self.stack:
            parent['comment'] = True


def known_credit_shapes(content):
    """Identify exact fixed captions; stripped output must stay diagnostic-only."""
    require(isinstance(content, str) and len(content.encode()) <= MAX_CONTENT_BYTES, 'content_bound')
    parser = CreditShapeParser(content)
    parser.feed(content)
    parser.close()
    # Smallest complete matching block wins; a wrapping section is not a second
    # credit. Comments, links or images are never stripped by this experiment.
    found = []
    for node in parser.nodes:
        if node['tag'] not in BLOCKS or node in parser.stack:
            continue
        fragment = content[node['start']:node['end']]
        if visible_wechat_content_text(fragment) == LOCAL_CAPTION:
            found.append(node)
    selected = []
    for node in sorted(found, key=lambda n: n['end'] - n['start']):
        if not any(node['start'] <= other['start'] and node['end'] >= other['end'] for other in selected):
            selected.append(node)
    selected.sort(key=lambda n: n['start'])
    require(len(selected) <= MAX_CREDIT_CANDIDATES, 'credit_candidate_bound')
    shapes = []
    removable = []
    for node in selected:
        attrs = node['attrs']
        eligible = not node['comment'] and all(tag in {'span', 'strong', 'em', 'b', 'i', 'br'} for tag in node['children'])
        fragment = content[node['start']:node['end']]
        shapes.append({'tag': node['tag'], 'has_data_marker': 'data-editorial-credit' in attrs,
            'data_marker_equals_one': attrs.get('data-editorial-credit') == '1',
            'has_image_credit_class': 'image-credit' in str(attrs.get('class') or '').split(),
            'child_tags': sorted({tag if tag in KNOWN_TAGS else 'other' for tag in node['children']}),
            'has_comment': node['comment'], 'has_link': 'a' in node['children'],
            'recognized_by_current_contract': bool(generated_image_credits(fragment)),
            'diagnostic_removal_eligible': eligible})
        if eligible:
            removable.append((node['start'], node['end']))
    normalized = content
    for start, end in reversed(removable):
        normalized = normalized[:start] + normalized[end:]
    return {'candidate_count': len(selected), 'diagnostic_removed_count': len(removable),
            'current_contract_credit_count': len(generated_image_credits(content)),
            'unbalanced_markup': parser.malformed or bool(parser.stack), 'shapes': shapes}, normalized


def known_credit_text(text):
    """Classify exact complete known captions; never return captured authors."""
    result = {'kind': 'unknown', 'commons_prefix': text.startswith('主题配图：'),
              'commons_credit_suffix_present': '；已裁剪与缩放，非报告原图。' in text,
              'text_sha256': digest(text), 'text_char_count': len(text)}
    if text == LOCAL_CAPTION:
        result['kind'] = 'local_editorial'
    elif match := COMMONS_CAPTION_RE.fullmatch(text):
        result.update(kind='commons', license=match[2], author_sha256=digest(match[1]),
                      author_char_count=len(match[1]), link_labels_present=bool(match[4]))
    return result


def safe_link_shape(attrs, license_name):
    """Only fixed host/path classes, booleans and hashes leave this function."""
    url = str(attrs.get('href') or '')
    result = {'href_present': bool(url), 'data_href_present': bool(attrs.get('data-href')),
              'href_sha256': digest(url), 'valid_url': False}
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError:
        return result
    license_path = '/publicdomain/zero/1.0/' if license_name == 'CC0 1.0' else '/licenses/by/' + license_name.removeprefix('CC BY ') + '/'
    result.update(valid_url=bool(parsed.scheme and parsed.netloc),
        scheme=parsed.scheme if parsed.scheme in {'https', 'http'} else 'other_or_missing',
        source_host_allowed=parsed.hostname == 'commons.wikimedia.org',
        license_host_allowed=parsed.hostname == 'creativecommons.org',
        wechat_redirect_host=parsed.hostname == 'mp.weixin.qq.com',
        source_file_path=parsed.path.startswith('/wiki/File:'),
        license_path_matches=bool(license_name) and parsed.path == license_path,
        has_query=bool(parsed.query), has_fragment=bool(parsed.fragment),
        has_credentials=bool(parsed.username or parsed.password), port_allowed=port in (None, 443))
    return result


class CreditDetailParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = {}; self.p_count = 0; self.parts = []; self.links = []
        self.tags = []; self.comment = False

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == 'p':
            self.p_count += 1; self.root = dict(attrs)
        elif tag == 'a':
            self.links.append(dict(attrs))

    def handle_data(self, value):
        self.parts.append(value)

    def handle_comment(self, _value):
        self.comment = True


def credit_paragraph_diagnostics(fragment):
    parsed = CreditDetailParser(); parsed.feed(fragment); parsed.close()
    joined = normalize_space(''.join(parsed.parts))
    text = known_credit_text(joined)
    visible = known_credit_text(visible_wechat_content_text(fragment))
    links = [safe_link_shape(attrs, text.get('license', '')) for attrs in parsed.links[:8]]
    accepted = generated_image_credit_signature(fragment) is not None
    marker = parsed.root.get('data-editorial-credit') == '1'
    marked_class = 'image-credit' in str(parsed.root.get('class') or '').split()
    if accepted:
        reason = 'accepted'
    elif parsed.comment or any(tag not in {'p', 'a'} for tag in parsed.tags):
        reason = 'extra_tag_or_comment'
    elif parsed.p_count != 1:
        reason = 'paragraph_count'
    elif not marker:
        reason = 'missing_data_marker'
    elif not marked_class:
        reason = 'missing_credit_class'
    elif text['kind'] == 'local_editorial':
        reason = 'unexpected_local_links'
    elif text['kind'] != 'commons' or not text.get('link_labels_present'):
        reason = 'prefix_or_spacing_or_text_mismatch'
    elif len(parsed.links) != 2:
        reason = 'link_count'
    elif any(not row['href_present'] for row in links):
        reason = 'missing_href'
    elif any(not row['valid_url'] for row in links):
        reason = 'invalid_link_url'
    elif any(row['scheme'] != 'https' for row in links):
        reason = 'non_https'
    elif any(row['has_query'] or row['has_fragment'] for row in links):
        reason = 'query_or_fragment'
    elif any(row['has_credentials'] or not row['port_allowed'] for row in links):
        reason = 'credentials_or_port'
    elif not links[0]['source_host_allowed'] or not links[1]['license_host_allowed']:
        reason = 'disallowed_host'
    elif not links[0]['source_file_path']:
        reason = 'source_path'
    elif not links[1]['license_path_matches']:
        reason = 'license_path'
    else:
        reason = 'unclassified_contract_rejection'
    # Diagnostic removal depends on a whole known text block, never arbitrary
    # prose. Link validation remains separately visible and is NOT waived.
    eligible = (parsed.p_count == 1 and not parsed.comment
                and all(tag in {'p', 'a', 'span', 'strong', 'em', 'b', 'i', 'br'} for tag in parsed.tags)
                and text['kind'] in {'local_editorial', 'commons'})
    return {'has_data_marker': 'data-editorial-credit' in parsed.root, 'data_marker_equals_one': marker,
        'has_image_credit_class': marked_class, 'paragraph_count': parsed.p_count,
        'child_tags': sorted({tag if tag in KNOWN_TAGS else 'other' for tag in parsed.tags if tag != 'p'}),
        'has_comment': parsed.comment, 'link_count': len(parsed.links), 'links': links,
        'links_truncated': len(parsed.links) > len(links),
        'joined_text': text, 'visible_text': visible,
        'joined_and_visible_text_equal': joined == visible_wechat_content_text(fragment),
        'current_signature_accepted': accepted, 'current_signature_rejection': reason,
        'diagnostic_whole_known_credit_removal_eligible': eligible}


def all_credit_diagnostics(content):
    require(isinstance(content, str) and len(content.encode()) <= MAX_CONTENT_BYTES, 'content_bound')
    paragraphs = []; spans = []; rejection_counts = {}
    for match in IMAGE_CREDIT_PARAGRAPH_RE.finditer(content):
        fragment = match.group(0)
        # Inspect all marked credits, plus known prefixes when a marker was
        # stripped. No arbitrary paragraph content is emitted by the parser.
        if not any(marker in fragment for marker in ('data-editorial-credit', 'image-credit', '主题配图：', '主题示意图：')):
            continue
        require(len(paragraphs) < MAX_CREDIT_CANDIDATES, 'credit_candidate_bound')
        row = credit_paragraph_diagnostics(fragment)
        paragraphs.append(row)
        reason = row['current_signature_rejection']
        rejection_counts[reason] = rejection_counts.get(reason, 0) + 1
        if row['diagnostic_whole_known_credit_removal_eligible']:
            spans.append((match.start(), match.end()))
    normalized = content
    for start, end in reversed(spans):
        normalized = normalized[:start] + normalized[end:]
    return {'diagnostic_only': True, 'production_acceptance': False,
            'paragraph_count': len(paragraphs), 'diagnostic_removed_count': len(spans),
            'rejection_counts': rejection_counts, 'paragraphs': paragraphs}, normalized


def media_inventory(article):
    images = wechat_content_images(article.get('content'))
    identities = [wechat_image_url_identity(url) for url, _ in images]
    return {'inline_image_count': len(images), 'distinct_image_count': len(set(identities)),
        'valid_image_identity_count': sum(bool(item) for item in identities),
        'ordered_image_identity_sha256': digest(encoded(identities)),
        'cover_present': bool(article.get('thumb_media_id')),
        'cover_identity_sha256': digest(str(article.get('thumb_media_id') or ''))}


def compare_article(actual, expected, target):
    actual_content = str(actual.get('content') or '')
    expected_content = str(expected.get('content') or '')
    actual_shapes, normalized_actual = known_credit_shapes(actual_content)
    expected_shapes, normalized_expected = known_credit_shapes(expected_content)
    actual_credit_details, normalized_all_actual = all_credit_diagnostics(actual_content)
    expected_credit_details, normalized_all_expected = all_credit_diagnostics(expected_content)
    actual_prose, expected_prose = article_prose_text(actual_content), article_prose_text(expected_content)
    actual_visible, expected_visible = visible_wechat_content_text(actual_content), visible_wechat_content_text(expected_content)
    # Unlike the production prose helper, this experiment removes only the
    # selected fixed local caption blocks. Other credits remain visible text.
    normalized_actual_text = visible_wechat_content_text(normalized_actual)
    normalized_expected_text = visible_wechat_content_text(normalized_expected)
    normalized_all_actual_text = visible_wechat_content_text(normalized_all_actual)
    normalized_all_expected_text = visible_wechat_content_text(normalized_all_expected)
    # This reference is the original saved receipt, NOT the last update request.
    # Changed cover/inline fields against that older receipt are expected after
    # repair and cannot by themselves diagnose a write/readback discrepancy.
    media = wechat_media_contract_check(actual, expected)
    return {'article_index': target['article_index'], 'comparison_reference': 'saved_original_receipt',
        'post_repair_request_available': False, 'repair_acceptance': False,
        'title_equal': str(actual.get('title') or '') == str(expected.get('title') or ''),
        'author_equal': str(actual.get('author') or '') == str(expected.get('author') or ''),
        'source_url_equal': str(actual.get('content_source_url') or '') == str(expected.get('content_source_url') or ''),
        'saved_prose_matches_recorded_repair_expected_hash': digest(expected_prose) == target['repair_expected_prose_sha256'],
        'strict_prose_equal': actual_prose == expected_prose,
        'strict_prose_sha256': {'actual': digest(actual_prose), 'saved': digest(expected_prose)},
        'visible_text_equal': actual_visible == expected_visible,
        'visible_text_sha256': {'actual': digest(actual_visible), 'saved': digest(expected_visible)},
        'diagnostic_known_caption_removal_equal': normalized_actual_text == normalized_expected_text,
        'diagnostic_known_caption_removal_sha256': {'actual': digest(normalized_actual_text), 'saved': digest(normalized_expected_text)},
        'diagnostic_all_known_credit_removal_equal': normalized_all_actual_text == normalized_all_expected_text,
        'diagnostic_all_known_credit_removal_sha256': {'actual': digest(normalized_all_actual_text), 'saved': digest(normalized_all_expected_text)},
        'actual_all_credit_diagnostics': actual_credit_details, 'saved_all_credit_diagnostics': expected_credit_details,
        'saved_receipt_media_checks': {key: value for key, value in media.items() if isinstance(value, (bool, int))},
        'actual_media_inventory': media_inventory(actual), 'saved_media_inventory': media_inventory(expected),
        'actual_known_local_credits': actual_shapes, 'saved_known_local_credits': expected_shapes}


class ReadOnlyWeChat:
    """Reject every operation except one token request and two exact draft reads."""
    def __init__(self, session, draft_ids):
        self.session = session
        self.draft_ids = set(draft_ids)
        self.read_ids = set()
        self.token_requests = 0

    def post(self, url, **kwargs):
        parsed = urlsplit(url)
        require(parsed.scheme == 'https' and parsed.netloc == 'api.weixin.qq.com'
                and not parsed.fragment and not kwargs.get('files'), 'readonly_endpoint_required')
        payload = json.loads(kwargs.get('data', b'{}'))
        if parsed.path == '/cgi-bin/stable_token':
            require(not parsed.query and self.token_requests == 0
                and set(payload) == {'grant_type', 'appid', 'secret', 'force_refresh'}
                and payload.get('grant_type') == 'client_credential' and payload.get('force_refresh') is False,
                'readonly_token_request_required')
            self.token_requests += 1
        else:
            require(parsed.path == '/cgi-bin/draft/get' and set(parse_qs(parsed.query)) == {'access_token'}
                    and set(payload) == {'media_id'} and payload['media_id'] in self.draft_ids
                    and payload['media_id'] not in self.read_ids, 'readonly_exact_draft_get_required')
            self.read_ids.add(payload['media_id'])
        return self.session.post(url, **kwargs, allow_redirects=False)


def diagnose(drafts, session, token, timeout=30, *, targets=TARGETS):
    require(len(drafts) == 6 and [len(d['articles']) for d in drafts] == [8, 8, 8, 8, 8, 4], 'historical_inventory_mismatch')
    rows = []
    for group_index, target in targets.items():
        require(group_index in {1, 6} and target['article_index'] == 1, 'diagnostic_target_invalid')
        draft = drafts[group_index - 1]
        require(digest(draft['media_id']) == target['receipt_id_sha256'], 'historical_target_receipt_mismatch')
        expected = materialize_private_article_payload(draft['articles'], os.environ.get('PORTAL_SITE_URL', ''))
        try:
            data = get_draft(session, token, draft['media_id'], timeout)
        except WeChatError as error:
            if error.errcode != 40007:
                raise
            rows.append({'draft_index': group_index, 'status': 'original_receipt_unavailable', 'wechat_errcode': 40007})
            continue
        actual = draft_news_items(data)
        row = {'draft_index': group_index, 'actual_article_count': len(actual),
               'saved_article_count': len(expected), 'article_count_equal': len(actual) == len(expected)}
        # Never guess a shifted ordinal, relink another ID or scan the catalog.
        if len(actual) != len(expected):
            row['status'] = 'count_changed_no_article_comparison'
        else:
            index = target['article_index']
            row.update(status='diagnosed', article=compare_article(actual[index], expected[index], target))
        rows.append(row)
    return {'schema_version': 1, 'read_only': True, 'diagnostic_only': True,
        'production_acceptance': False, 'full_repair_verified': False,
        'source_run_id': receipts.ACCEPTED_RUN_ID, 'observed_repair_run_id': REPAIR_RUN_ID,
        'draft_reads': len(rows), 'catalog_reads': 0, 'image_downloads': 0, 'wechat_writes': 0,
        'model_calls': 0, 'cache_writes': 0, 'drafts': rows, 'status': 'diagnostics_complete'}


def require_main_workflow():
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    require(bool(repository) and os.environ.get('GITHUB_ACTIONS') == 'true'
        and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
        and os.environ.get('GITHUB_REF') == 'refs/heads/main'
        and os.environ.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main',
        'read_only_main_workflow_required')
    return repository


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', required=True, choices=['restore', 'inspect'])
    parser.add_argument('--artifact-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    code = 1
    try:
        repository = require_main_workflow()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            if args.mode == 'restore':
                result = receipts.restore(args.artifact_root, receipts.ACCEPTED_RUN_ID, repository,
                                          receipts.build_client(), receipts.r2_bucket())
                result['success'] = True
            else:
                import requests
                drafts = load_drafts(args.artifact_root)
                selected_ids = [drafts[index - 1]['media_id'] for index in TARGETS]
                with requests.Session() as transport:
                    session = ReadOnlyWeChat(transport, selected_ids)
                    response = post_wechat_json(session, 'https://api.weixin.qq.com/cgi-bin/stable_token',
                        {'grant_type': 'client_credential', 'appid': os.environ['WECHAT_MP_APPID'],
                         'secret': os.environ['WECHAT_MP_APPSECRET'], 'force_refresh': False}, 30, max_attempts=1)
                    token = parse_wechat_json(response, 'read-only stable token').get('access_token')
                    require(isinstance(token, str) and bool(token), 'read_only_token_missing')
                    result = diagnose(drafts, session, token)
            code = 0
    except Exception as error:
        result = {'read_only': True, 'diagnostic_only': True, 'status': 'stopped',
            'wechat_writes': 0, 'model_calls': 0, 'cache_writes': 0,
            'category': str(error) if isinstance(error, (DiagnosticError, receipts.RestoreError)) else 'diagnostic_operation_failed'}
        if isinstance(error, WeChatError) and type(error.errcode) is int:
            result['wechat_errcode'] = error.errcode
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded(result) + b'\n')
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
