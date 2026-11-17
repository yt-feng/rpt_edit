"""Exercise incremental source admission, durable fixed groups and edit-safe resume."""
import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import shutil
import unittest
from unittest.mock import patch

import progressive_wechat_delivery as progressive
import push_xhs_notes_to_wechat_drafts as uploader
import push_portal_translated_to_wechat_drafts as api


class StorageError(Exception):
    def __init__(self, code):
        self.response = {'Error': {'Code': code}, 'ResponseMetadata': {'HTTPStatusCode': 412 if code == 'PreconditionFailed' else 404}}


class Store:
    def __init__(self):
        self.rows, self.counter = {}, 0
    def get_object(self, Bucket, Key):
        if Key not in self.rows:
            raise StorageError('NoSuchKey')
        data, version, metadata = self.rows[Key]
        return {'Body': io.BytesIO(data), 'ETag': version, 'Metadata': metadata}
    def put_object(self, Bucket, Key, Body, IfMatch=None, IfNoneMatch=None, **kwargs):
        old = self.rows.get(Key)
        if (IfNoneMatch == '*' and old) or (IfMatch is not None and (not old or old[1] != IfMatch)):
            raise StorageError('PreconditionFailed')
        self.counter += 1
        self.rows[Key] = (Body, str(self.counter), kwargs.get('Metadata', {}))
        return {'ETag': str(self.counter)}
    def upload_file(self, Filename, Bucket, Key, ExtraArgs):
        self.put_object(Bucket=Bucket, Key=Key, Body=Path(Filename).read_bytes(), **ExtraArgs)
    def download_file(self, Bucket, Key, Filename):
        Path(Filename).write_bytes(self.get_object(Bucket, Key)['Body'].read())
    def head_object(self, Bucket, Key):
        row = self.get_object(Bucket, Key)
        return {'ContentLength': len(row['Body'].read()), 'Metadata': row['Metadata']}


class ProgressiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.manifest = self.root / 'manifest.json'
        self.rows = [{'process_local_path': f'_selected/{index:02d}-Report-{index}.pdf', 'content_sha256': hashlib.sha256(str(index).encode()).hexdigest()} for index in range(1, 13)]
        progressive.write_json(self.manifest, self.rows)
        self.store = Store()
        self.env = patch.dict(os.environ, {'WECHAT_ROUTING_START_DATE': '2026-11-08', 'WECHAT_ROUTING_SCOPE': 'dropbox', 'GITHUB_RUN_ID': '2345', 'GITHUB_RUN_ATTEMPT': '1'})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.quiet = redirect_stdout(io.StringIO())
        self.quiet.__enter__()
        self.addCleanup(self.quiet.__exit__, None, None, None)
        self.plan = self.make_plan()
        self.source_root = self.root / 'xhs' / '261116'
        self.output = self.root / 'wechat' / '261116'
        self.uploaded = []
    def make_plan(self, **kwargs):
        defaults = dict(source_run_id='1234', date_folder='261116', source_execution_sha='a' * 40, reports_per_shard=2, articles_per_draft=3, max_articles='all', client=self.store, bucket='private')
        defaults.update(kwargs)
        return progressive.create_plan(self.manifest, **defaults)
    def materialize(self, sources=None):
        for row in sources or self.plan['sources']:
            directory = self.source_root / row['report_relative']
            directory.mkdir(parents=True, exist_ok=True)
            progressive.write_json(directory / 'status.json', {'source_pdf': row['staged_name'], 'original_pdf_sha256': row['content_sha256'], 'wechat_article': 'wechat_article.md'})
            (directory / 'wechat_article.md').write_text('# A report\nA complete generated article.')
        return progressive.source_directories(self.plan, self.source_root)
    def fake_upload(self, plan, group, directories, output, client, bucket, args):
        self.uploaded.append(group['group_id'])
        output.mkdir(parents=True, exist_ok=True)
        sources = group['source_ids']
        articles = [{'title': f'Title-{source[:8]}', 'author': 'Author', 'content': '<p>Original article</p>'} for source in sources]
        payload = {'account': group['account'], 'articles': articles}
        progressive.write_json(output / 'draft_payload_01.json', payload)
        drafts = [{'draft_index': 1, 'media_id': 'media-' + group['group_id'], 'article_count': len(sources), 'account': group['account'],
                   'report_dirs': [str(directories[source]) for source in sources], 'payload': str(output / 'draft_payload_01.json'),
                   'group_key': api.draft_group_key(articles, account=group['account']), 'status': 'verified',
                   'draft_get': {'ok': True, 'article_count': len(sources), 'expected_article_count': len(sources), 'matches_editorial_contract': True, 'matches_expected_article_count': True, 'matches_expected_titles': True, 'matches_media_contract': True}}]
        summaries = [{'report_dir': str(directories[source]), 'wechat_title': item['title'], 'source_image_count': 0, 'source_image_sha256': [], 'account': group['account']} for source, item in zip(sources, articles)]
        progressive.write_json(output / 'wechat_draft_summary.json', {'drafts': drafts, 'articles': summaries, 'skipped_title_policy': []})
        audits = {}
        records = {row['source_id']: row for row in plan['sources']}
        for source in sources:
            audit = {'source_id': source, 'content_sha256': records[source]['content_sha256'], 'source_image_sha256': []}
            audits[source] = {**audit, 'audit_sha256': progressive.digest(progressive.encoded(audit))}
        progressive.write_json(output / 'progressive_figures.json', audits)
        progressive.save_group(plan, group, output, client, bucket, True)
    def send(self, directories):
        with patch.object(progressive, 'upload_group', side_effect=self.fake_upload):
            return progressive.upload_ready_groups(self.plan, directories, self.output, self.root, self.store, 'private', [])
    def presence(self, edited=False):
        summary = progressive.read_json(self.output / 'wechat_draft_summary.json')
        progressive.write_json(self.output / 'progressive_presence.json', {'plan_sha256': self.plan['plan_sha256'], 'drafts': [{'account': row['account'], 'media_id': row['media_id'], 'article_count': row['article_count'], 'id_exists': True, 'editorial_changes_preserved': edited} for row in summary['drafts']]})
    def test_plan_reserves_all_routes_and_balances_before_completion_order_is_known(self):
        self.assertEqual(self.make_plan(), self.plan)
        for account in ('kc', 'tt', 'pankou'):
            sizes = [len(group['source_ids']) for group in self.plan['groups'] if group['account'] == account]
            self.assertEqual(sizes, [2, 1, 1])
        mutated = copy.deepcopy(self.plan)
        mutated['groups'][0]['source_ids'].reverse()
        with self.assertRaisesRegex(ValueError, 'digest'):
            progressive.validate_plan(mutated)
    def test_first_ready_group_does_not_wait_for_earlier_or_other_shards(self):
        group = self.plan['groups'][-1]
        directories = self.materialize([row for row in self.plan['sources'] if row['source_id'] in group['source_ids']])
        summary = self.send(directories)
        self.assertEqual(self.uploaded, [group['group_id']])
        self.assertEqual(summary['selected_count'], len(group['source_ids']))
        self.assertEqual(summary['status'], 'in_progress')
        self.send(directories)
        self.assertEqual(self.uploaded, [group['group_id']])
    def test_accepted_groups_survive_recovery_directory_changes_and_preserve_all_counts(self):
        first = self.plan['groups'][0]
        sources = [row for row in self.plan['sources'] if row['source_id'] in first['source_ids']]
        self.send(self.materialize(sources))
        original_media = progressive.read_json(self.output / 'wechat_draft_summary.json')['drafts'][0]['media_id']
        recovery = self.root / 'recovered'
        for index, source in enumerate(self.plan['sources']):
            directory = recovery / f'report_{index:04d}_recovered'
            directory.mkdir(parents=True)
            progressive.write_json(directory / 'status.json', {'original_filename': source['source_pdf'], 'original_pdf_sha256': source['content_sha256']})
            (directory / 'wechat_article.md').write_text('# Regenerated\nDifferent generated content')
        directories = progressive.recovery_source_dirs(self.plan, recovery)
        self.send(directories)
        self.presence(edited=True)
        result = progressive.validate_progressive_delivery(self.output, self.plan, directories)
        self.assertEqual(result['article_count'], 12)
        self.assertTrue(result['editorial_changes_preserved'])
        self.assertEqual(len(self.uploaded), len(self.plan['groups']))
        self.assertEqual(progressive.read_json(self.output / 'wechat_draft_summary.json')['drafts'][0]['media_id'], original_media)
    def test_matching_filename_with_changed_pdf_bytes_is_rejected(self):
        self.materialize()
        source = self.plan['sources'][0]
        status_path = self.source_root / source['report_relative'] / 'status.json'
        status = progressive.read_json(status_path)
        status['original_pdf_sha256'] = 'b' * 64
        progressive.write_json(status_path, status)
        with self.assertRaisesRegex(ValueError, 'binding_mismatch'):
            progressive.source_directories(self.plan, self.source_root)
    def test_changed_manifest_cannot_resume_or_add_a_second_plan(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['content_sha256'] = 'b' * 64
        progressive.write_json(self.manifest, rows)
        with self.assertRaisesRegex(ValueError, 'manifest_changed'):
            self.make_plan()
    def test_one_article_mode_and_eight_digit_dates_remain_supported(self):
        plan = self.make_plan(source_run_id='3456', date_folder='20261116', articles_per_draft=1)
        self.assertTrue(all(len(group['source_ids']) == 1 for group in plan['groups']))
    def test_fake_policy_or_missing_first_figure_audit_cannot_establish_completion(self):
        directories = self.materialize()
        self.send(directories)
        self.presence()
        summary = progressive.read_json(self.output / 'wechat_draft_summary.json')
        summary['articles'][0]['progressive_initial_figure_audit']['content_sha256'] = 'b' * 64
        progressive.write_json(self.output / 'wechat_draft_summary.json', summary)
        with self.assertRaisesRegex(ValueError, 'figure_audit'):
            progressive.validate_progressive_delivery(self.output, self.plan, directories)
    @patch.object(progressive, "publisher_owner", return_value={"run_id": "2345", "run_attempt": 1, "job_id": 12, "job_name": "deliver"})
    def test_lease_never_takes_over_an_active_owner_and_terminal_owner_is_checked(self, _owner):
        with progressive.publisher_lease(self.plan, self.store, 'private'):
            with patch.object(progressive, 'github_run_completed', return_value=False):
                with self.assertRaisesRegex(ValueError, 'publisher_busy'):
                    with progressive.publisher_lease(self.plan, self.store, 'private'):
                        self.fail('second publisher entered')
        with progressive.publisher_lease(self.plan, self.store, 'private'):
            pass
    def test_global_group_capacity_and_contiguous_first_group(self):
        for total, expected_counts, expected_groups in ((60, [20, 20, 20], [3, 3, 3]), (80, [32, 24, 24], [4, 3, 3])):
            rows = [{'process_local_path': f'_selected/{index:03d}-report.pdf', 'content_sha256': hashlib.sha256(str(index).encode()).hexdigest()} for index in range(total)]
            progressive.write_json(self.manifest, rows)
            plan = self.make_plan(source_run_id=str(3000 + total), articles_per_draft=8, client=Store())
            accounts = tuple(progressive.ACCOUNT_NAMES)
            self.assertEqual([sum(source['account'] == account for source in plan['sources']) for account in accounts], expected_counts)
            self.assertEqual([sum(group['account'] == account for group in plan['groups']) for account in accounts], expected_groups)
            self.assertEqual(set(plan['groups'][0]['source_ids']), {source['source_id'] for source in plan['sources'][:len(plan['groups'][0]['source_ids'])]})
            self.assertTrue(all(len(group['source_ids']) <= 8 for group in plan['groups']))
        self.assertEqual([len(group['source_ids']) for group in plan['groups']], [8] * 10)

    def test_existing_route_assignments_are_never_moved(self):
        routes = [hashlib.sha256(str(index).encode()).hexdigest() for index in range(80)]
        original = {source: tuple(progressive.ACCOUNT_NAMES)[index % 3] for index, source in enumerate(routes[:60])}
        self.store.put_object(Bucket='private', Key=progressive.ROUTING_KEY, Body=progressive.encoded({'version': 1, 'assigned': original}))
        assigned, counts = progressive.balanced_route_reservation(self.store, 'private', routes, 8)
        self.assertTrue(all(assigned[source] == account for source, account in original.items()))
        self.assertEqual(sum(counts.values()), 10)

    def test_pacing_is_durable_per_account_and_unknown_attempt_is_not_reset(self):
        clock = [100.0]
        waits = []
        def sleep(delay):
            waits.append(delay)
            clock[0] += delay
        def submit():
            return 'accepted'
        prefix = progressive.progressive_prefix('1234', '261116')
        progressive.paced_submission(self.store, 'private', prefix, 'kc', 90, submit, now=lambda: clock[0], sleep=sleep)
        self.assertEqual(waits, [90])
        clock[0] += 20
        progressive.paced_submission(self.store, 'private', prefix, 'tt', 0, submit, now=lambda: clock[0], sleep=sleep)
        progressive.paced_submission(self.store, 'private', prefix, 'kc', 90, submit, now=lambda: clock[0], sleep=sleep)
        self.assertEqual(waits, [90, 70])
        with self.assertRaisesRegex(RuntimeError, 'lost ACK'):
            progressive.paced_submission(self.store, 'private', prefix, 'kc', 90, lambda: (_ for _ in ()).throw(RuntimeError('lost ACK')), now=lambda: clock[0], sleep=sleep)
        clock[0] += 10
        progressive.paced_submission(self.store, 'private', prefix, 'kc', 90, submit, now=lambda: clock[0], sleep=sleep)
        self.assertEqual(waits, [90, 70, 90, 80])

    def test_crashed_final_job_can_release_lease_while_daily_waits_for_recovery(self):
        owner = {'run_id': '2345', 'run_attempt': 1, 'job_id': 12, 'job_name': 'push-xhs-wechat-drafts'}
        run = {'id': 2345, 'run_attempt': 1, 'status': 'in_progress', 'head_repository': {'full_name': 'fixture/repo'}}
        with patch.dict(os.environ, {'GITHUB_REPOSITORY': 'fixture/repo'}), patch.object(progressive, 'github_json', return_value=run), patch.object(progressive, 'owner_jobs', return_value=[{'id': 12, 'name': owner['job_name'], 'status': 'completed'}]):
            self.assertTrue(progressive.github_run_completed(owner))
        with patch.dict(os.environ, {'GITHUB_REPOSITORY': 'fixture/repo'}), patch.object(progressive, 'github_json', return_value=run), patch.object(progressive, 'owner_jobs', return_value=[{'id': 12, 'name': owner['job_name'], 'status': 'in_progress'}]):
            self.assertFalse(progressive.github_run_completed(owner))

    def test_individual_ready_archive_is_bound_to_manifest_bytes(self):
        source = self.plan['sources'][0]
        directories = self.materialize([source])
        directory = directories[source['source_id']]
        receipt = {key: self.plan[key] for key in ('source_run_id', 'source_execution_sha', 'date_folder', 'manifest_sha256')}
        receipt.update(schema_version=1, source_pdf=source['source_pdf'], content_sha256=source['content_sha256'])
        progressive.write_json(directory / 'progressive_source.json', receipt)
        key = f"_private-workflow-handoff/xhs-ready/1234/261116/source_{source['source_id']}.tar.gz"
        progressive.upload_directory(directory, key, client=self.store, bucket='private')
        shutil.rmtree(self.source_root)
        self.assertEqual(set(progressive.restore_ready_sources(self.plan, self.source_root, self.store, 'private')), {source['source_id']})
        receipt['manifest_sha256'] = '0' * 64
        progressive.write_json(directory / 'progressive_source.json', receipt)
        progressive.upload_directory(directory, key, client=self.store, bucket='private')
        shutil.rmtree(self.source_root)
        with self.assertRaisesRegex(ValueError, 'ready_owner_changed'):
            progressive.restore_ready_sources(self.plan, self.source_root, self.store, 'private')

    def test_complete_final_retains_sources_after_transient_handoff_cleanup(self):
        directories = self.materialize()
        self.send(directories)
        self.presence()
        progressive.save_complete(self.plan, self.output, self.store, 'private', directories)
        shutil.rmtree(self.source_root)
        prefix = progressive.progressive_prefix('1234', '261116')
        progressive.download_directory(prefix + '/sources.tar.gz', self.source_root, client=self.store, bucket='private')
        self.assertEqual(len(progressive.source_directories(self.plan, self.source_root)), 12)

    def test_full_inventory_is_required_even_with_selection_limit(self):
        self.plan = self.make_plan(source_run_id='4567', max_articles='2')
        directories = self.materialize(self.plan['sources'][:2])
        self.send(directories)
        self.presence()
        with self.assertRaisesRegex(ValueError, 'inventory_incomplete'):
            progressive.validate_progressive_delivery(self.output, self.plan, directories)

    def test_actual_uploader_crash_after_verified_ack_preserves_payload_on_recovery(self):
        first = self.plan['groups'][0]
        sources = [row for row in self.plan['sources'] if row['source_id'] in first['source_ids']]
        directories = self.materialize(sources)
        target = api.DraftDestination(first['account'], 'fixture-app', 'fixture-token', '')
        original_metadata = uploader.xhs_article_title_metadata
        def build(report, index, *args):
            metadata = original_metadata(report)
            return {**metadata, 'article': {'title': metadata['wechat_title'], 'author': 'Author', 'content': '<p>Original prepared prose</p>', 'thumb_media_id': 'fixture-cover'}, 'content_chars': 30, 'content_bytes': 30, 'visible_text_chars': 25, 'inline_images': [], 'body_image_count': 0, 'cover_image': 'fixture.jpg', 'source_image_count': 0, 'source_image_sha256': []}
        verification = {'ok': True, 'article_count': len(sources), 'expected_article_count': len(sources), 'matches_editorial_contract': True, 'matches_expected_article_count': True, 'matches_expected_titles': True, 'matches_media_contract': True}
        save = progressive.save_group
        crashed = [False]
        def crash_after_verified(plan, group, directory, client, bucket, complete=False):
            save(plan, group, directory, client, bucket, complete)
            summary = directory / 'wechat_draft_summary.json'
            if summary.exists() and any(row.get('status') == 'verified' for row in progressive.read_json(summary).get('drafts', [])) and not crashed[0]:
                crashed[0] = True
                raise RuntimeError('runner crashed after verified ACK')
        args = ['--dropbox-output-root', str(self.source_root.parent), '--wechat-appid', 'fixture-app', '--wechat-secret', 'fixture-secret', '--site-url', 'https://portal.example.invalid', '--article-delay-seconds', '0', '--draft-delay-seconds', '0', '--draft-verify-delay-seconds', '0']
        with patch.object(uploader, 'prepare_draft_destinations', side_effect=lambda args, date, reports, *a, **kw: ({path: first['account'] for path in reports}, {first['account']: target}, None)), patch.object(uploader, 'build_article', side_effect=build) as built, patch.object(uploader, 'find_recent_draft_by_titles', return_value=''), patch.object(api, 'post_wechat_json', return_value=object()) as post, patch.object(api, 'parse_wechat_json', return_value={'media_id': 'accepted-first'}), patch.object(uploader, 'verify_draft_get', return_value=verification) as verify:
            with patch.object(progressive, 'save_group', side_effect=crash_after_verified), self.assertRaisesRegex(RuntimeError, 'runner crashed'):
                progressive.upload_ready_groups(self.plan, directories, self.output, self.root, self.store, 'private', args)
            self.assertEqual(post.call_count, 1)
            prepared_count = built.call_count
            recovery = self.root / 'recovery' / '261116'
            changed = {}
            for index, source in enumerate(sources):
                report = recovery / f'report_{index:04d}_changed'
                report.mkdir(parents=True)
                progressive.write_json(report / 'status.json', {'source_pdf': source['source_pdf'], 'original_pdf_sha256': source['content_sha256']})
                (report / 'wechat_article.md').write_text('# Goldman Sachs: changed and now policy blocked\nCompletely different generation')
                changed[source['source_id']] = report
            progressive.upload_ready_groups(self.plan, changed, self.output, self.root, self.store, 'private', args)
            self.assertEqual(post.call_count, 1)
            self.assertEqual(built.call_count, prepared_count)
            self.assertEqual(verify.call_count, 1)
            self.assertEqual(progressive.read_json(self.output / 'wechat_draft_summary.json')['drafts'][0]['media_id'], 'accepted-first')


    def test_live_identity_validation_preserves_editorial_changes(self):
        directories = self.materialize()
        self.send(directories)
        summaries = progressive.read_json(self.output / 'wechat_draft_summary.json')['drafts']
        counts = {row['media_id']: row['article_count'] for row in summaries}
        with patch('wechat_accounts.draft_tokens', return_value={account: 'fixture-token' for account in progressive.ACCOUNT_NAMES}), patch.object(api, 'get_draft', side_effect=lambda session, token, media, timeout: {'news_item': [{'title': 'Manually edited title', 'author': 'Human editor', 'content': '<p>Manually edited body</p>'} for _ in range(counts[media])]}), patch.object(api, 'post_wechat_json') as post:
            result = progressive.validate_progressive_delivery(self.output, self.plan, directories, live=True)
            self.assertTrue(result['editorial_changes_preserved'])
            self.assertTrue(result['figure_verification_complete'])
            post.assert_not_called()
        # Local recovery admission uses the same bound presence proof.
        self.assertTrue(progressive.validate_progressive_delivery(self.output, self.plan, directories)['complete'])

    def test_unknown_post_cannot_be_replayed_with_regenerated_payload(self):
        from recovered_article_delivery import guarded_add_draft
        prefix = progressive.progressive_prefix('1234', '261116')
        articles = [{'title': 'Original title', 'content': '<p>Original immutable body</p>'}]
        with patch.object(api, 'post_wechat_json', side_effect=api.WeChatError('lost ACK')) as post, patch.object(api, 'recover_draft_after_ambiguous_add', return_value=''):
            with self.assertRaisesRegex(ValueError, 'intent_unresolved'):
                guarded_add_draft(self.store, 'private', prefix, None, 'fixture-token', articles, 30, account='kc')
            self.assertEqual(post.call_count, 1)
        with patch.object(api, 'post_wechat_json') as post, patch.object(api, 'recover_draft_after_ambiguous_add', return_value='original-media'):
            self.assertEqual(guarded_add_draft(self.store, 'private', prefix, None, 'fixture-token', articles, 30, account='kc'), 'original-media')
            post.assert_not_called()


    def test_corrupt_inventory_does_not_become_empty_input(self):
        self.store.rows[progressive.progressive_prefix('1234', '261116') + '/plan.json'] = (b'{}', '999', {})
        with self.assertRaisesRegex(ValueError, 'plan_invalid'):
            self.make_plan()


if __name__ == '__main__':
    unittest.main()
