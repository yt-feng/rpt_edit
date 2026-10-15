#!/usr/bin/env python3
"""Restore the three saved complete IMF titles from producer run 38698155880.

This intentionally has no arbitrary draft/run/title selector. Audit first, then
apply only a reviewed plan hash. Never create/publish/delete a draft or call a
model. The producer's private artifact remains immutable.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import time

import requests

from build_portal_suite_site import (
    BLOG_START_DATE, blog_archive_record, blog_article_fingerprint,
    blog_public_slug, load_blog_draft_articles, parse_blog_start_date,
    validate_blog_archive_record,
)
from push_portal_translated_to_wechat_drafts import (
    draft_group_key, get_draft, get_stable_access_token,
    materialize_private_article_payload, parse_wechat_json, post_wechat_json,
    summarize_draft_get_response,
)
from update_blog_archive_from_wechat_drafts import assert_public_archive_identity
from wechat_title_optimizer import title_quality_issues
from wechat_html_diagnostics import article_content_diagnostics, all_field_read_diagnostics

PINS = json.loads((Path(__file__).parent / 'fixtures/wechat_institution_title_repair_38698155880.json').read_text())
WRITABLE = ('title', 'author', 'digest', 'content', 'content_source_url',
            'thumb_media_id', 'need_open_comment', 'only_fans_can_comment')
UPLOAD_ONLY = {'pic_crop_1_1', 'pic_crop_235_1'}


class RepairError(ValueError):
    """Only fixed categories, never API responses, private IDs, or body text."""


def require(condition, category):
    if not condition:
        raise RepairError(category)


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def html_binding_matches(content, pin, prefix):
    return (isinstance(content, str) and len(content.encode()) == pin.get(prefix + '_html_bytes')
            and hashlib.sha256(content.encode()).hexdigest() == pin.get(prefix + '_html_sha256'))


def reviewed_content_matches(actual, expected, pin):
    """Allow only the exact producer bytes or this article's reviewed live bytes.

    Diagnostic run 38703812822 proved that the three returned bodies differ
    only at their four img events: src becomes data-src, the same qpic image
    uses its HTTPS /640 rendition, and the void tag is no longer self-closing.
    No generic HTML normalization or prose/media-only equivalence is accepted.
    """
    return (actual == expected or
            (html_binding_matches(expected, pin, 'producer') and html_binding_matches(actual, pin, 'live')))


def read_json(path, expected_sha=None):
    require(path.is_file() and not path.is_symlink(), 'input_not_regular_file')
    require(0 < path.stat().st_size <= 1024 * 1024, 'input_size_bound')
    raw = path.read_bytes()
    require(expected_sha is None or hashlib.sha256(raw).hexdigest() == expected_sha,
            'producer_artifact_hash_mismatch')
    return json.loads(raw)


def load_source(artifact_root, pins=PINS):
    receipt_dir = artifact_root / pins['receipt_dir']
    values = {name: read_json(receipt_dir / name, sha) for name, sha in pins['files'].items()}
    summary, payload, log = (values[name] for name in
                            ('wechat_draft_summary.json', 'draft_payload_01.json', 'wechat_title_log.json'))
    require(summary.get('status') == 'verified' and summary.get('dry_run') is False
            and summary.get('publish') is False and summary.get('draft_count') == 1
            and len(summary.get('drafts', [])) == 1 and summary.get('selected_count') == 3,
            'producer_summary_mismatch')
    draft = summary['drafts'][0]
    require(draft.get('status') == 'verified' and draft.get('published') is False
            and not draft.get('publish_id') and draft.get('article_count') == 3
            and draft.get('draft_index') == 1 and draft.get('draft_get', {}).get('ok') is True
            and draft.get('payload') == pins['receipt_dir'] + '/draft_payload_01.json'
            and isinstance(draft.get('media_id'), str) and bool(draft['media_id']),
            'producer_draft_mismatch')
    articles = payload.get('articles', [])
    require(len(articles) == len(summary.get('articles', [])) == len(log.get('articles', [])) == 3,
            'producer_article_count_mismatch')
    require(len(list((artifact_root / 'wechat_drafts').rglob('draft_payload_*.json'))) == 1,
            'producer_payload_not_unique')
    for article, meta, logged, pin in zip(articles, summary['articles'], log['articles'], pins['articles']):
        decision = logged.get('generation_decision', {})
        require(article.get('title') == meta.get('title') == logged.get('final_wechat_title') == pin['old_title']
                and meta.get('report_dir') == logged.get('report_dir') == pin['report_dir']
                and meta.get('source_report_name') == logged.get('source_report_name') == pin['source_report_name']
                and decision.get('selected_title') == decision.get('final_title_after_wording_guard') == pin['selected_title']
                and not title_quality_issues(pin['selected_title'], 'IMF', pin['source_report_name'])
                and len(pin['selected_title']) <= 35, 'producer_title_binding_mismatch')
        require(not article.get('content_source_url') and not re.search(r'<a\b', article.get('content', ''), re.I),
                'producer_link_contract_changed')
    records = {row['fingerprint']: blog_archive_record(row) for row in
               load_blog_draft_articles(artifact_root / 'wechat_drafts', parse_blog_start_date(BLOG_START_DATE))}
    require(set(records) == {row['old_blog_fingerprint'] for row in pins['articles']},
            'producer_blog_binding_mismatch')
    materialized = materialize_private_article_payload(articles, '')
    for article, pin in zip(materialized, pins['articles']):
        require(html_binding_matches(article['content'], pin, 'producer'), 'producer_html_binding_mismatch')
    return {'media_id': draft['media_id'], 'articles': materialized,
            'payload': payload, 'summary': summary, 'title_log': log, 'pins': pins,
            'old_records': records}


def live_articles(data):
    # Reject malformed/filtered rows rather than silently shortening the group.
    rows = data.get('news_item')
    require(isinstance(rows, list) and len(rows) == 3 and all(isinstance(row, dict) for row in rows),
            'live_draft_count_or_shape_mismatch')
    return rows


def validate_live(data, source):
    actual = live_articles(data)
    for current, expected, pin in zip(actual, source['articles'], source['pins']['articles']):
        require(current.get('is_deleted', 0) in (0, False), 'live_article_deleted')
        require(current.get('title') in {pin['old_title'], pin['selected_title']}, 'live_title_changed')
        for key, value in expected.items():
            if key == 'title':
                continue
            if key in UPLOAD_ONLY and key not in current:
                continue  # These upload-only crop inputs are never sent by this repair.
            if key == 'article_type' and value == 'news' and key not in current:
                continue  # Older draft/get responses omit the default article type.
            if key == 'content':
                require(reviewed_content_matches(current.get(key), value, pin), 'live_payload_changed_content')
                continue
            require(key in current and current[key] == value, 'live_payload_changed_' + key)
        require(not current.get('content_source_url'), 'live_source_url_changed')
    checks = summarize_draft_get_response(data, 3, [dict(row, title=a['title'])
                                                for row, a in zip(source['articles'], actual)])
    require(checks['ok'] is True, 'live_media_or_editorial_contract_mismatch')
    return actual


def blog_changes(archive_root, source):
    changes = []
    for pin in source['pins']['articles']:
        old = source['old_records'][pin['old_blog_fingerprint']]
        new = copy.deepcopy(old)
        new['title'] = pin['selected_title']
        new['fingerprint'] = blog_article_fingerprint(new['title'], new['content'])
        new['slug'] = blog_public_slug(new['date'], new['fingerprint'])
        new['legacy_slugs'] = sorted(set(old.get('legacy_slugs', [])) | {old['slug']})
        old_path = archive_root / old['date'].replace('-', '') / (old['fingerprint'] + '.json')
        new_path = old_path.with_name(new['fingerprint'] + '.json')
        require(old_path != new_path and old_path.exists() != new_path.exists(), 'blog_state_ambiguous')
        current_path, expected = (old_path, old) if old_path.exists() else (new_path, new)
        require(read_json(current_path) == expected, 'blog_record_changed')
        validate_blog_archive_record(new, new_path, parse_blog_start_date(BLOG_START_DATE))
        assert_public_archive_identity([new])
        changes.append({'old_path': old_path, 'new_path': new_path, 'old': old, 'new': new,
                        'already_updated': current_path == new_path})
    return changes


def plan_for(data, source, changes):
    actual = validate_live(data, source)
    return {'source_run_id': source['pins']['source_run_id'], 'article_count': 3,
            'draft_identity_sha256': digest(source['media_id']),
            'full_live_articles_sha256': digest(actual),
            'reviewed_live_html': source['pins']['reviewed_live_html'],
            'unreturned_upload_only_fields': sorted({key for row in actual for key in UPLOAD_ONLY if key not in row}),
            'articles': [{'index': index, 'current_title': current['title'], 'selected_title': pin['selected_title'],
                          'old_blog_fingerprint': change['old']['fingerprint'],
                          'new_blog_fingerprint': change['new']['fingerprint'],
                          'blog_already_updated': change['already_updated'],
                          'blog_before_sha256': digest(change['new'] if change['already_updated'] else change['old']),
                          'blog_after_sha256': digest(change['new'])}
                         for index, (current, pin, change) in enumerate(zip(actual, source['pins']['articles'], changes))]}


def unchanged_articles(data, expected):
    return live_articles(data) == expected


def protected_live_facts(articles):
    """Hash every returned field except the sole authorized title change."""
    protected = [{key: value for key, value in row.items() if key != 'title'} for row in articles]
    return {'article_count': len(articles), 'all_non_title_fields_sha256': digest(protected),
            'article_non_title_fields_sha256': [digest(row) for row in protected],
            'html_sha256': [hashlib.sha256(row['content'].encode()).hexdigest() for row in articles]}


def repair_titles(session, token, source, initial, progress, save, timeout=30):
    baseline = copy.deepcopy(validate_live(initial, source))
    progress['live_before'] = protected_live_facts(baseline)
    for index, pin in enumerate(source['pins']['articles']):
        # Recheck every field of all three articles immediately before a write.
        before = get_draft(session, token, source['media_id'], timeout)
        require(unchanged_articles(before, baseline), 'live_group_changed_before_update')
        if baseline[index]['title'] == pin['selected_title']:
            progress['verified_indices'].append(index)
            save()
            continue
        update = {key: baseline[index][key] for key in WRITABLE if key in baseline[index]}
        update['title'] = pin['selected_title']
        wanted = copy.deepcopy(baseline)
        wanted[index]['title'] = pin['selected_title']
        progress['attempted_indices'].append(index)
        save()
        acknowledged = False
        try:
            response = post_wechat_json(session,
                f'https://api.weixin.qq.com/cgi-bin/draft/update?access_token={token}',
                {'media_id': source['media_id'], 'index': index, 'articles': update}, timeout, max_attempts=1)
            acknowledged = parse_wechat_json(response, 'draft/update title').get('errcode') == 0
        except Exception:
            pass  # The outcome is unknown: read back, never repeat this POST.
        verified = None
        for attempt in range(3):
            try:
                candidate = get_draft(session, token, source['media_id'], timeout)
                if unchanged_articles(candidate, wanted):
                    verified = candidate
                    break
                require(unchanged_articles(candidate, baseline), 'live_group_changed_after_update')
            except RepairError:
                raise
            except Exception:
                pass
            if attempt < 2:
                time.sleep(2)
        require(verified is not None, 'title_update_not_verified_stop_without_retry')
        baseline = wanted
        progress['verified_indices'].append(index)
        progress['updates'].append({'index': index, 'acknowledged': acknowledged, 'readback_verified': True})
        save()
    final = get_draft(session, token, source['media_id'], timeout)
    require(unchanged_articles(final, baseline), 'final_full_payload_mismatch')
    validate_live(final, source)
    progress['live_after'] = protected_live_facts(live_articles(final))
    require(progress['live_after'] == progress['live_before'], 'non_title_fields_changed')
    save()
    return final


def replace_blog_records(archive_root, source):
    changes = blog_changes(archive_root, source)  # Recheck before any filesystem mutation.
    count_before = len(list(archive_root.glob('*/*.json')))
    for change in changes:
        if change['already_updated']:
            continue
        temporary = change['new_path'].with_suffix('.json.tmp')
        temporary.write_text(json.dumps(change['new'], ensure_ascii=False, indent=2) + '\n')
        temporary.replace(change['new_path'])
        change['old_path'].unlink()
    require(all(row['already_updated'] for row in blog_changes(archive_root, source)), 'blog_replacement_not_verified')
    require(len(list(archive_root.glob('*/*.json'))) == count_before, 'blog_archive_count_changed')
    return {'changed_records': sum(not row['already_updated'] for row in changes),
            'article_count_before': count_before, 'article_count_after': count_before,
            'old_links_preserved': True}


def write_corrected_receipts(output, source, final):
    """A new receipt points to the same draft with the corrected group identity."""
    target = output / source['pins']['receipt_dir']
    target.mkdir(parents=True, exist_ok=True)
    payload, summary, log = (copy.deepcopy(source[key]) for key in ('payload', 'summary', 'title_log'))
    titles = [pin['selected_title'] for pin in source['pins']['articles']]
    for index, title in enumerate(titles):
        payload['articles'][index]['title'] = title
        summary['articles'][index].update(title=title, wechat_title=title)
        log['articles'][index].update(final_wechat_title=title, title_before_upload=title)
    draft = summary['drafts'][0]
    draft.update(titles=titles, wechat_titles=titles, group_key=draft_group_key(payload['articles']),
                 payload_bytes=len(json.dumps({'articles': payload['articles']}, ensure_ascii=False,
                                              separators=(',', ':')).encode()),
                 draft_get=summarize_draft_get_response(final, 3, materialize_private_article_payload(payload['articles'], '')))
    summary['title_repair_source_run_id'] = source['pins']['source_run_id']
    for name, value in [('draft_payload_01.json', payload), ('wechat_draft_summary.json', summary), ('wechat_title_log.json', log)]:
        (target / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact-root', type=Path, required=True)
    parser.add_argument('--archive-root', type=Path, default=Path('portal_suite/data/blog_archive'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--expected-plan-sha256', default='')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result = {'ok': False, 'apply': args.apply, 'source_run_id': PINS['source_run_id'],
              'attempted_indices': [], 'verified_indices': [], 'updates': []}
    def save():
        (args.output / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    try:
        source = load_source(args.artifact_root)
        changes = blog_changes(args.archive_root, source)
        with requests.Session() as session:
            token = get_stable_access_token(session, os.environ['WECHAT_MP_APPID'], os.environ['WECHAT_MP_APPSECRET'], 30)
            initial = get_draft(session, token, source['media_id'], 30)
            # Preserve bounded, content-free evidence even when strict byte
            # binding rejects a server-returned representation. Diagnostics
            # never weaken validate_live or authorize a write.
            result['content_diagnostics'] = article_content_diagnostics(initial, source)
            save()
            if not args.apply:
                # Audit only: compare a second independent read to locate
                # server-returned field drift. The plan remains bound to the
                # first read and the apply/write path is unchanged.
                second_read = get_draft(session, token, source['media_id'], 30)
                result['live_field_diagnostics'] = all_field_read_diagnostics(initial, second_read, WRITABLE)
                save()
            plan = plan_for(initial, source, changes)
            result.update(plan=plan, plan_sha256=digest(plan))
            save()
            if args.apply:
                require(bool(re.fullmatch(r'[a-f0-9]{64}', args.expected_plan_sha256))
                        and args.expected_plan_sha256 == result['plan_sha256'], 'reviewed_plan_changed')
                final = repair_titles(session, token, source, initial, result, save)
                write_corrected_receipts(args.output, source, final)
                result['blog'] = replace_blog_records(args.archive_root, source)
                result['full_payload_preserved'] = True
            result['ok'] = True
    except Exception as exc:
        result['error_category'] = str(exc) if isinstance(exc, RepairError) else 'repair_contract_or_transport_stop'
    save()
    print(json.dumps({key: result[key] for key in ('ok', 'apply', 'source_run_id', 'plan_sha256', 'error_category') if key in result}))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
