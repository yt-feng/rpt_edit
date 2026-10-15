#!/usr/bin/env python3
from __future__ import annotations

import copy
from datetime import date
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import repair_wechat_institution_titles as repair
from build_portal_suite_site import (
    blog_article_fingerprint, blog_public_slug,
    render_blog_legacy_redirect, sanitize_blog_html, validate_blog_archive_record,
)
from push_portal_translated_to_wechat_drafts import draft_group_key, translated_article_title_metadata


class CompleteGeneratedTitleTests(unittest.TestCase):
    def metadata(self, pin, *, heading=None, selected=None):
        markdown = f"# {heading or pin['selected_title']}\n\n## {pin['subtitle']}\n\n正文摘要。\n"
        status = {'title': pin['source_report_name'], 'wechat_title_decision': {
            'selected_title': pin['selected_title'] if selected is None else selected}}
        return translated_article_title_metadata(Path(pin['report_dir']), markdown, status)

    def test_actual_three_titles_remain_complete_and_body_headers_do_not_change(self):
        for pin in repair.PINS['articles']:
            with self.subTest(source=pin['source_report_name']):
                result = self.metadata(pin)
                self.assertEqual(result['wechat_title'], pin['selected_title'])
                self.assertEqual(result['header_title'], pin['subtitle'])
                self.assertNotEqual(result['wechat_title'], pin['old_title'])
                self.assertLess(len(result['wechat_title']), 20)

    def test_manually_edited_first_heading_wins_over_stale_saved_title(self):
        pin = repair.PINS['articles'][0]
        heading = 'IMF：美国短期国债占比上升与政策传导'
        with_stale = self.metadata(pin, heading=heading)
        without_saved = self.metadata(pin, heading=heading, selected='')
        self.assertEqual(with_stale['wechat_title'], without_saved['wechat_title'])
        self.assertNotEqual(with_stale['wechat_title'], pin['selected_title'])

    def test_mismatched_or_bad_saved_title_does_not_override_current_heading(self):
        pin = repair.PINS['articles'][0]
        for selected in ['IMF：完全不相关的其他报告主题', 'IMF：研究主题与行业变化观察', 'IMF：' + '标题' * 25]:
            self.assertEqual(self.metadata(pin, selected=selected)['wechat_title'],
                             self.metadata(pin, selected='')['wechat_title'])


class BoundedTitleRepairTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.archive = self.root / 'archive'
        self.pins = copy.deepcopy(repair.PINS)
        articles, records = [], {}
        for index, pin in enumerate(self.pins['articles']):
            article = {'title': pin['old_title'], 'author': 'KC桌面', 'digest': '完整摘要',
                       'content': f'<p>原文正文{index}。</p><img src="https://example.com/{index}.png" alt="chart">',
                       'thumb_media_id': f'cover-{index}', 'need_open_comment': 0, 'only_fans_can_comment': 0,
                       'article_type': 'news', 'pic_crop_1_1': '0_0_1_1', 'pic_crop_235_1': '0_0_1_1'}
            articles.append(article)
            stored_content = sanitize_blog_html(article['content'])
            fingerprint = blog_article_fingerprint(article['title'], stored_content)
            pin['old_blog_fingerprint'] = fingerprint
            record = {'schema_version': 1, 'fingerprint': fingerprint,
                      'slug': blog_public_slug('2026-10-15', fingerprint), 'legacy_slugs': ['legacy-test-' + str(index)],
                      'title': article['title'], 'author': article['author'], 'digest': article['digest'],
                      'content': stored_content, 'date': '2026-10-15', 'last_date': '2026-10-15',
                      'source': 'institutions', 'origins': [{'source': 'institutions', 'date': '2026-10-15'}]}
            records[fingerprint] = record
            path = self.archive / '20261015' / (fingerprint + '.json')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(record, ensure_ascii=False))
        self.source = {'media_id': 'test-only-draft', 'articles': articles, 'old_records': records, 'pins': self.pins}
        self.actual = copy.deepcopy(articles)
        for article in self.actual:
            for field in repair.UPLOAD_ONLY:
                article.pop(field)
            article['url'] = 'https://example.com/existing-draft'
        self.data = {'news_item': self.actual}
        self.progress = {'attempted_indices': [], 'verified_indices': [], 'updates': []}
        self.contract = patch.object(repair, 'summarize_draft_get_response', return_value={'ok': True})
        self.contract.start()
        self.addCleanup(self.contract.stop)

    def run_repair(self, *, unknown=False, apply_post=True, mutate=None):
        state = copy.deepcopy(self.data)
        posts = []
        def get(*args):
            return copy.deepcopy(state)
        def post(session, url, payload, timeout, *, max_attempts):
            self.assertIn('/draft/update?', url)
            self.assertEqual(max_attempts, 1)
            self.assertEqual(payload['media_id'], self.source['media_id'])
            index = payload['index']
            wanted = {key: state['news_item'][index][key] for key in repair.WRITABLE if key in state['news_item'][index]}
            wanted['title'] = self.pins['articles'][index]['selected_title']
            self.assertEqual(payload['articles'], wanted)
            self.assertFalse(set(payload['articles']) & repair.UPLOAD_ONLY)
            posts.append(index)
            if apply_post:
                state['news_item'][index]['title'] = wanted['title']
            if mutate:
                mutate(state)
            if unknown:
                raise TimeoutError('unknown request outcome')
            return object()
        with patch.object(repair, 'get_draft', side_effect=get), patch.object(repair, 'post_wechat_json', side_effect=post), \
                patch.object(repair, 'parse_wechat_json', return_value={'errcode': 0}), patch.object(repair.time, 'sleep'):
            result = repair.repair_titles(None, 'test-token', self.source, self.data, self.progress, lambda: None)
        return result, posts

    def test_three_single_attempt_updates_keep_full_existing_payload(self):
        result, posts = self.run_repair()
        self.assertEqual(posts, [0, 1, 2])
        self.assertEqual(self.progress['verified_indices'], [0, 1, 2])
        for old, new, pin in zip(self.actual, result['news_item'], self.pins['articles']):
            self.assertEqual(new, dict(old, title=pin['selected_title']))

    def test_unknown_success_is_read_back_without_repeat_post(self):
        _, posts = self.run_repair(unknown=True)
        self.assertEqual(posts, [0, 1, 2])
        self.assertTrue(all(not row['acknowledged'] and row['readback_verified'] for row in self.progress['updates']))

    def test_unknown_unapplied_write_stops_before_next_article_and_never_retries(self):
        with self.assertRaisesRegex(repair.RepairError, 'title_update_not_verified'):
            self.run_repair(unknown=True, apply_post=False)
        self.assertEqual(self.progress['attempted_indices'], [0])
        self.assertEqual(self.progress['verified_indices'], [])

    def test_full_readback_detects_non_title_metadata_change(self):
        with self.assertRaisesRegex(repair.RepairError, 'live_group_changed_after_update'):
            self.run_repair(mutate=lambda state: state['news_item'][2].update(digest='changed'))
        self.assertEqual(self.progress['attempted_indices'], [0])

    def test_partial_previous_run_only_updates_remaining_exact_indices(self):
        self.data['news_item'][0]['title'] = self.pins['articles'][0]['selected_title']
        _, posts = self.run_repair()
        self.assertEqual(posts, [1, 2])

    def test_completed_replay_is_read_only(self):
        for row, pin in zip(self.data['news_item'], self.pins['articles']):
            row['title'] = pin['selected_title']
        _, posts = self.run_repair()
        self.assertEqual(posts, [])

    def test_changed_body_cover_author_digest_source_order_or_count_rejected(self):
        for field in ('content', 'thumb_media_id', 'author', 'digest', 'content_source_url'):
            data = copy.deepcopy(self.data)
            data['news_item'][2][field] = 'user edited'
            with self.subTest(field=field), self.assertRaises(repair.RepairError):
                repair.validate_live(data, self.source)
        for rows in (list(reversed(self.actual)), self.actual[:2], [*self.actual, {}]):
            with self.assertRaises(repair.RepairError):
                repair.validate_live({'news_item': rows}, self.source)

    def test_review_plan_hash_binds_all_live_fields_and_blog_state(self):
        changes = repair.blog_changes(self.archive, self.source)
        plan = repair.plan_for(self.data, self.source, changes)
        modified = copy.deepcopy(self.data)
        modified['news_item'][0]['server_field'] = 'changed'
        self.assertNotEqual(repair.digest(plan), repair.digest(repair.plan_for(modified, self.source, changes)))
        self.assertNotIn(self.source['media_id'], json.dumps(plan))

    def test_blog_replacement_is_canonical_count_preserving_with_old_links_and_noop(self):
        changes = repair.blog_changes(self.archive, self.source)
        result = repair.replace_blog_records(self.archive, self.source)
        self.assertEqual(result['changed_records'], 3)
        self.assertEqual(result['article_count_before'], result['article_count_after'])
        for change in changes:
            self.assertFalse(change['old_path'].exists())
            actual = json.loads(change['new_path'].read_text())
            self.assertEqual(actual, change['new'])
            validate_blog_archive_record(actual, change['new_path'], date(2026, 1, 1))
            self.assertIn(change['old']['slug'], actual['legacy_slugs'])
            self.assertIn(actual['slug'] + '.html', render_blog_legacy_redirect(actual, 'https://example.com'))
            self.assertEqual({key: value for key, value in actual.items() if key not in {'title', 'fingerprint', 'slug', 'legacy_slugs'}},
                             {key: value for key, value in change['old'].items() if key not in {'title', 'fingerprint', 'slug', 'legacy_slugs'}})
        self.assertEqual(repair.replace_blog_records(self.archive, self.source)['changed_records'], 0)

    def test_blog_preflight_checks_all_records_before_any_replacement(self):
        before = {path: path.read_bytes() for path in self.archive.glob('*/*.json')}
        path = next(reversed(before))
        altered = json.loads(path.read_text()); altered['digest'] = 'edited'
        path.write_text(json.dumps(altered))
        with self.assertRaisesRegex(repair.RepairError, 'blog_record_changed'):
            repair.replace_blog_records(self.archive, self.source)
        self.assertEqual(set(self.archive.glob('*/*.json')), set(before))
        for other in set(before) - {path}:
            self.assertEqual(other.read_bytes(), before[other])

    def test_original_and_new_blog_shards_together_are_rejected(self):
        change = repair.blog_changes(self.archive, self.source)[0]
        change['new_path'].write_text(json.dumps(change['new']))
        with self.assertRaisesRegex(repair.RepairError, 'blog_state_ambiguous'):
            repair.blog_changes(self.archive, self.source)

    def test_receipt_hash_mismatch_fails_without_api_calls(self):
        path = self.root / 'receipt.json'; path.write_text('{}')
        with self.assertRaisesRegex(repair.RepairError, 'producer_artifact_hash_mismatch'):
            repair.read_json(path, '0' * 64)

    def test_corrected_receipt_preserves_id_bodies_and_updates_all_title_identities(self):
        source = copy.deepcopy(self.source)
        source['payload'] = {'articles': copy.deepcopy(source['articles'])}
        source['summary'] = {'articles': [{'title': row['title'], 'wechat_title': row['title'], 'header_title': pin['subtitle']}
                                        for row, pin in zip(source['articles'], self.pins['articles'])],
                             'drafts': [{'media_id': source['media_id'], 'group_key': draft_group_key(source['articles'])}]}
        source['title_log'] = {'articles': [{'final_wechat_title': row['title'], 'generation_decision': {'selected_title': pin['selected_title']}}
                                          for row, pin in zip(source['articles'], self.pins['articles'])]}
        old_source = copy.deepcopy(source)
        final, _ = self.run_repair()
        repair.write_corrected_receipts(self.root / 'output', source, final)
        target = self.root / 'output' / self.pins['receipt_dir']
        summary = json.loads((target / 'wechat_draft_summary.json').read_text())
        payload = json.loads((target / 'draft_payload_01.json').read_text())
        self.assertEqual(source, old_source)
        titles = [pin['selected_title'] for pin in self.pins['articles']]
        self.assertEqual(summary['drafts'][0]['media_id'], source['media_id'])
        self.assertEqual(summary['drafts'][0]['titles'], titles)
        self.assertEqual(summary['drafts'][0]['wechat_titles'], titles)
        self.assertEqual(summary['drafts'][0]['group_key'], draft_group_key(payload['articles']))
        self.assertNotEqual(summary['drafts'][0]['group_key'], source['summary']['drafts'][0]['group_key'])
        for old, new, pin in zip(source['articles'], payload['articles'], self.pins['articles']):
            self.assertEqual(new, dict(old, title=pin['selected_title']))

    def test_live_deleted_article_is_never_repaired(self):
        self.data['news_item'][1]['is_deleted'] = 1
        with self.assertRaisesRegex(repair.RepairError, 'live_article_deleted'):
            repair.validate_live(self.data, self.source)


class WorkflowContractTests(unittest.TestCase):
    def test_manual_workflow_is_pinned_and_defaults_to_audit(self):
        text = (Path(__file__).parents[1] / '.github/workflows/wechat-institution-title-repair.yml').read_text()
        self.assertIn('default: false', text)
        self.assertIn('run-id: 38698155880', text)
        self.assertIn('name: institution-wechat-drafts-261015-38698155880', text)
        self.assertIn("run.get('head_sha') == PINS['source_head']", text)
        self.assertIn('expected-plan-sha256 "$EXPECTED_PLAN"', text)
        self.assertIn("if: inputs.apply", text)
        self.assertNotIn('source_run_id:', text)

    def test_pinned_artifact_and_test_suite_are_in_pr_ci(self):
        self.assertEqual(repair.PINS['source_run_id'], 38698155880)
        self.assertEqual(len(repair.PINS['files']), 3)
        self.assertEqual(len(repair.PINS['articles']), 3)
        text = (Path(__file__).parents[1] / '.github/workflows/wechat-pipeline-regression.yml').read_text()
        self.assertIn('python scripts/test_repair_wechat_institution_titles.py', text)


if __name__ == '__main__':
    unittest.main()
