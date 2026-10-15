"""Real PDF split/merge plus durable crash/restart boundaries, without network."""
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import fitz
from PIL import Image

from consume_legacy_mineru import safe_unzip
from mineru_result_cache import ResultCache
from mineru_task_ledger import FileStore, Ledger, LedgerError, digest, encoded
import mineru_page_segments as segments
from test_mineru_result_cache import MemoryR2
from test_mineru_figure_sources import visual


def pdf(path, count):
    with fitz.open() as doc:
        for pi in range(count):
            page = doc.new_page(width=400, height=500)
            page.insert_text((20, 30), 'Original page '+str(pi+1))
            page.draw_rect(fitz.Rect(35, 100, 185, 260), color=(.2, .4, .6), fill=(.8, .9, 1))
        doc.save(path)


def result_zip(raw, *, label='part', profile='3.4.4', metadata=True, inline_table=False, visual_count=1):
    with fitz.open(stream=raw, filetype='pdf') as doc:
        count = len(doc)
    html = '<table><tr><td><img src="'+'a'*64+'.jpg"/></td></tr></table>' if inline_table else ''
    content, parent = visual(0, [35, 100, 185, 260], kind='table' if inline_table else 'chart',
                             ref='images/same.png', body=html)
    if inline_table:
        content['table_body'] = html.replace('src="', 'src="images/')
    middle = {'_backend': 'hybrid', '_version_name': profile, '_ocr_enable': True, '_effort': 'medium',
              'pdf_info': [{'page_idx': i, 'page_size': [400, 500], 'para_blocks': [parent] if i == 0 else []}
                           for i in range(count)]}
    content_rows, extra_images = [content], []
    for index in range(1, visual_count):
        pi = index * count // visual_count
        name = f'images/dense-{index}.png'
        item, block = visual(index, [35, 100, 185, 260], kind='chart', ref=name, page_idx=pi)
        content_rows.append(item); middle['pdf_info'][pi]['para_blocks'].append(block)
        extra_images.append(name)
    picture = io.BytesIO(); Image.new('RGB', (700, 500), (40, 100, 160)).save(picture, 'PNG')
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('result/full.md', label+'\n![](images/same.png)\n<img src="images/same.png">\n')
        archive.writestr('result/images/same.png', picture.getvalue())
        for name in extra_images:
            archive.writestr('result/' + name, picture.getvalue())
        if inline_table:
            archive.writestr('result/images/'+'a'*64+'.jpg', picture.getvalue())
        archive.writestr('result/source.pdf', raw)
        if metadata:
            archive.writestr('result/content_list.json', json.dumps(content_rows))
            archive.writestr('result/middle.json', json.dumps(middle))
    return output.getvalue()


class Provider:
    def __init__(self):
        self.posts, self.uploads, self.polls, self.tasks = [], {}, [], {}
        self.crash_submit = None
        self.failed_segment = None

    def submit(self, items, options, token, timeout):
        key = str(len(self.posts)+1)
        self.posts.append(copy.deepcopy(items))
        if self.crash_submit == len(self.posts):
            raise LedgerError('MinerU POST transport outcome unknown; saved task retained')
        self.tasks[key] = copy.deepcopy(items)
        return key, ['https://upload.invalid/'+key]

    def upload(self, url, raw, timeout):
        self.uploads[url.rsplit('/', 1)[-1]] = raw

    def poll(self, key, token, timeout):
        self.polls.append(key)
        item = self.tasks[key][0]
        failed = not item['source'].startswith('_mineru-page-segments/') or self.failed_segment == item['source']
        return [{'data_id': item['id'], 'state': 'failed' if failed else 'done',
                 **({'err_msg': 'page limit'} if failed else {'full_zip_url': 'https://results.invalid/'+key})}]

    def download(self, url):
        key = url.rsplit('/', 1)[-1]
        return result_zip(self.uploads[key], label='Segment '+key)


class SegmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.original = self.root/'original.pdf'; pdf(self.original, 202)
        self.provider = Provider()
        self.ledger = Ledger(FileStore(self.root/'ledger'), self.provider, 'dropbox', 'https://mineru.net',
            {'model': 'vlm', 'language': 'en', 'ocr': True}, [('MINER_U', 'test-secret')])
        self.cache = ResultCache(MemoryR2(), 'private')
        self.directory = self.root/'parts'

    def run_parts(self, **kwargs):
        return segments.run_segments(self.ledger, self.original, 'original.pdf', self.directory,
            result_cache=self.cache, downloader=kwargs.pop('downloader', self.provider.download), **kwargs)

    def test_frozen_legacy_segments_restore_static_groups_and_replay_original_crops(self):
        from probe_consulting_mineru_figure_binding import verify_production_figures
        with fitz.open(self.original) as document:
            for index in (0, 200):
                page = document[index]
                page.draw_rect(fitz.Rect(35, 100, 185, 260), fill=(.7, .2, .5), fill_opacity=.4)
                document.xref_set_key(page.xref, 'Group', '<</S/Transparency/CS/DeviceRGB>>')
            raw = document.tobytes(no_new_id=True)
        self.original.write_bytes(raw)
        # Reproduce the pre-fix frozen uploads: physical imports dropped Group.
        with patch.object(segments, '_preserve_page_groups', return_value=[]):
            plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        self.assertEqual(segments.prepare_segments(self.ledger, self.original, 'original.pdf',
                                                    self.root/'prearchive-replay'), plan)
        archive = segments.SegmentArchive(self.cache.client, 'private')
        physical, payloads = [], []
        for part in plan['segments']:
            raw_part = (self.directory/Path(part['binding']['source']).name).read_bytes()
            physical.append(raw_part); payloads.append(result_zip(raw_part))
            archive.preserve(plan['original_binding'], part['binding'], raw_part)
        with patch.object(segments, '_preserve_page_groups', side_effect=AssertionError('must reuse frozen bytes')):
            replay_plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf',
                                                    self.root/'replayed', archive=archive)
        self.assertEqual(plan, replay_plan)
        merged = segments.merge_segments(plan, payloads, self.original)
        with zipfile.ZipFile(io.BytesIO(merged)) as result:
            receipt = json.loads(result.read('segment_render_context.json'))
        self.assertEqual([row['page_index'] for row in receipt['pages']], [0, 200])
        self.assertTrue(all(row['provider_group_was_missing'] for row in receipt['pages']))
        self.assertEqual(receipt['original_pdf_sha256'], digest(self.original.read_bytes()))
        proof = verify_production_figures(self.original, merged, digest(self.original.read_bytes()), lambda: None)
        self.assertEqual(proof['status'], 'verified', proof)
        self.assertEqual(proof['image_count'], 2)
        self.assertTrue(proof['private_handoff_replay_verified'])
        for part, before in zip(plan['segments'], physical):
            self.assertEqual(archive.get(plan['original_binding'], part['binding']), before)
        # A real body change survives restoration and remains rejected by the
        # original full-page pixel gate, including after a source Group repair.
        with fitz.open(stream=physical[1], filetype='pdf') as changed:
            changed[0].draw_rect(fitz.Rect(40, 110, 80, 150), fill=(1, 0, 0))
            tampered = changed.tobytes(no_new_id=True)
        altered = segments.merge_segments(plan, [payloads[0], result_zip(tampered)], self.original)
        rejection = verify_production_figures(self.original, altered, digest(self.original.read_bytes()), lambda: None)
        self.assertEqual(rejection.get('category'), 'figure_source_pixels_mismatch')
        self.assertFalse(rejection['production_consumer_verified'])

    def test_new_physical_segments_preserve_group_across_page_200(self):
        with fitz.open(self.original) as document:
            for index in (0, 200):
                document.xref_set_key(document.page_xref(index), 'Group', '<</S/Transparency/CS/DeviceRGB>>')
            raw = document.tobytes(no_new_id=True)
        self.original.write_bytes(raw)
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        for part in plan['segments']:
            with fitz.open(self.directory/Path(part['binding']['source']).name) as split:
                self.assertEqual(segments._static_page_group(split, 0)[1],
                                 {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': False, '/K': False})

    def test_static_group_conflicts_reject_and_unsupported_source_keeps_existing_behavior(self):
        with fitz.open() as source, fitz.open() as provider, fitz.open() as target:
            for document in (source, provider, target):
                document.new_page(width=40, height=40)
            source.xref_set_key(source.page_xref(0), 'Group', '<</S/Transparency/CS/DeviceRGB>>')
            provider.xref_set_key(provider.page_xref(0), 'Group',
                                 '<</Type/Group/S/Transparency/CS/DeviceRGB/I false/K false>>')
            self.assertEqual(len(segments._preserve_page_groups(source, provider, target, 0, 0, 0, 1)), 1)
            target.xref_set_key(target.page_xref(0), 'Group', 'null')
            for setting in ('<</S/Transparency/CS/DeviceCMYK>>', '<</S/Transparency>>'):
                provider.xref_set_key(provider.page_xref(0), 'Group', setting)
                with self.assertRaisesRegex(LedgerError, 'provider page group differs'):
                    segments._preserve_page_groups(source, provider, target, 0, 0, 0, 1)
                self.assertEqual(target.xref_get_key(target.page_xref(0), 'Group')[0], 'null')
            # Missing CS is legal but outside this observed static repair. It
            # must not add a new failure on a previously unselected page.
            source.xref_set_key(source.page_xref(0), 'Group', '<</S/Transparency>>')
            self.assertEqual(segments._preserve_page_groups(source, provider, target, 0, 0, 0, 1), [])

    def test_boundary_and_deterministic_frozen_bytes(self):
        for count in (199, 200):
            target = self.root/f'{count}.pdf'; pdf(target, count)
            self.assertIsNone(segments.prepare_segments(self.ledger, target, target.name, self.root/str(count)))
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        self.assertEqual([(row['page_start'], row['page_end']) for row in plan['segments']], [(1, 200), (201, 202)])
        for row in plan['segments']:
            with fitz.open(self.directory/Path(row['binding']['source']).name) as part:
                self.assertLessEqual(len(part), 200)
                self.assertIn(str(row['page_start']), part[0].get_text())
        second = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.root/'regenerated')
        self.assertEqual(plan, second)
        self.assertEqual(segments.read_segment_plan(self.ledger, plan['original_binding']), plan)
        self.assertFalse(self.provider.posts)

    def test_short_local_scope_does_not_require_remote_cache_binding(self):
        target = self.root/'short.pdf'; pdf(target, 1)
        local = Ledger(FileStore(self.root/'local'), self.provider, 'local', 'https://mineru.net',
            {'model': 'vlm', 'language': 'en', 'ocr': True}, [('MINER_U', 'test-secret')])
        self.assertIsNone(segments.prepare_segments(local, target, target.name, self.root/'short'))
        self.assertFalse(self.provider.posts)

    def test_table_inline_images_rewritten_in_content_and_middle_html(self):
        result = self.run_parts(downloader=lambda url: result_zip(
            self.provider.uploads[url.rsplit('/', 1)[-1]], inline_table=True))
        root = self.root/'inline'; safe_unzip(result['zip_bytes'], root)
        content = json.loads((root/'content_list.json').read_bytes())
        middle = json.loads((root/'middle.json').read_bytes())
        for ordinal, page in enumerate((0, 200), 1):
            chtml = content[ordinal-1]['table_body']
            mhtml = middle['pdf_info'][page]['para_blocks'][0]['blocks'][0]['lines'][0]['spans'][0]['html']
            self.assertEqual(chtml, mhtml)
            expected = f'images/segment{ordinal:04d}/result/images/'+('a'*64)+'.jpg'
            self.assertIn(expected, chtml)
            self.assertTrue((root/expected).is_file())

    def test_original_failed_claim_retained_and_restart_reuses_every_task_and_zip(self):
        self.ledger.run([(self.original, 'original.pdf')], timeout=10)
        binding = self.ledger.bind(self.original, 'original.pdf')
        original_claim = self.ledger.store.get('sources/'+binding['id'])
        original_batch = self.ledger.store.get(original_claim[0]['batch_key'])
        result = self.run_parts()
        self.assertEqual(result['provider_posts'], 2)
        self.assertEqual(len(self.provider.posts), 3)
        self.assertEqual(original_claim, self.ledger.store.get('sources/'+binding['id']))
        self.assertEqual(original_batch, self.ledger.store.get(original_claim[0]['batch_key']))
        again = self.run_parts(allow_new=False, downloader=lambda url: self.fail('cached result downloaded again'))
        self.assertEqual(again['provider_posts'], 0)
        self.assertEqual(result['receipt'], again['receipt'])
        self.assertEqual(result['zip_bytes'], again['zip_bytes'])
        self.assertEqual(len(self.provider.posts), 3)

    def test_mid_result_failure_resumes_without_reposting_or_redownloading_completed_segment(self):
        def interrupt(url):
            if url.endswith('/2'): raise RuntimeError('download interrupted')
            return self.provider.download(url)
        with self.assertRaisesRegex(RuntimeError, 'interrupted'):
            self.run_parts(downloader=interrupt)
        downloads = []
        def resumed(url):
            downloads.append(url)
            return self.provider.download(url)
        self.assertEqual(self.run_parts(downloader=resumed)['provider_posts'], 0)
        self.assertEqual(downloads, ['https://results.invalid/2'])
        self.assertEqual(len(self.provider.posts), 2)

    def test_ambiguous_second_submission_blocks_all_replay_provider_calls(self):
        self.provider.crash_submit = 2
        with self.assertRaises(LedgerError): self.run_parts()
        before = len(self.provider.polls)
        with self.assertRaisesRegex(LedgerError, 'ambiguous segment submission'): self.run_parts()
        self.assertEqual(len(self.provider.polls), before)
        self.assertEqual(len(self.provider.posts), 2)

    def test_get_only_missing_plan_does_not_write_or_submit(self):
        with self.assertRaisesRegex(LedgerError, 'missing frozen segment plan'):
            self.run_parts(allow_new=False)
        self.assertEqual(list((self.root/'ledger').rglob('*.json')), [])
        self.assertFalse(self.provider.posts)

    def test_get_only_requires_all_claims_before_any_provider_get(self):
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        part = plan['segments'][0]
        self.ledger.run([(self.directory/Path(part['binding']['source']).name, part['binding']['source'])], timeout=10)
        before = len(self.provider.polls)
        with self.assertRaisesRegex(LedgerError, 'segment claim missing'): self.run_parts(allow_new=False)
        self.assertEqual(len(self.provider.polls), before)

    def test_failed_segment_has_one_permanent_claim(self):
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        self.provider.failed_segment = plan['segments'][1]['binding']['source']
        for _ in range(2):
            with self.assertRaisesRegex(LedgerError, 'segment parsing incomplete'): self.run_parts()
        self.assertEqual(len(self.provider.posts), 2)

    def test_frozen_plan_mutation_stops_before_provider(self):
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        value, version = self.ledger.store.get(segments.plan_key(plan['original_binding']))
        value['segments'][1]['page_start'] = 200
        self.ledger.store.put(segments.plan_key(plan['original_binding']), value, version)
        with self.assertRaisesRegex(LedgerError, 'frozen segment span'): self.run_parts()
        self.assertFalse(self.provider.posts)

    def test_merge_preserves_1432_visuals_from_independent_complete_segments(self):
        import mineru_figure_sources as figures
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        payloads = [result_zip((self.directory / Path(part['binding']['source']).name).read_bytes(),
                              visual_count=count)
                    for part, count in zip(plan['segments'], (1330, 102))]
        merged = segments.merge_segments(plan, payloads, self.original)
        root = self.root / 'dense-merged'
        safe_unzip(merged, root)
        found = figures._metadata_files(root)
        metadata = figures._normalise(found[0][1], found[1][1])
        self.assertEqual(len(metadata['records']), 1432)
        self.assertEqual(len(metadata['pages']), 202)
        self.assertEqual(metadata['records'][1330]['page_idx'], 200)
        self.assertEqual(len({row['ref'] for row in metadata['records']}), 1432)
        self.assertEqual(figures._check_excerpt(metadata), metadata)
        self.assertEqual(sum(row['selected'] for row in figures._decisions(metadata, 8)), 8)
        self.assertFalse(self.provider.posts)

    def test_merge_resource_names_and_global_metadata_then_real_original_figure_proof(self):
        result = self.run_parts()
        receipt, payload = result['receipt'], result['zip_bytes']
        segments.validate_segment_receipt(receipt, self.ledger.bind(self.original, 'original.pdf'), payload)
        report = self.root/'report'; report.mkdir()
        markdown = safe_unzip(payload, report/'raw')
        (report/'source_mineru.md').write_bytes(markdown)
        self.assertIn(b'images/segment0001/result/images/same.png', markdown)
        self.assertIn(b'images/segment0002/result/images/same.png', markdown)
        content = json.loads((report/'raw/content_list.json').read_bytes())
        self.assertEqual([row['page_idx'] for row in content], [0, 200])
        from mineru_figure_sources import create_figure_sources, validate_figure_sources
        selection = create_figure_sources(report/'raw', report/'assets',
            original_pdf_sha256=digest(self.original.read_bytes()), markdown_sha256=digest(markdown),
            auth_original_pdf=self.original)
        proof = json.loads((report/'source_figure_map.json').read_bytes())
        self.assertEqual([row['page_idx'] for row in proof['metadata']['records']], [0, 200])
        validate_figure_sources(report, expected_original_sha256=digest(self.original.read_bytes()),
            expected_markdown_sha256=digest(markdown), expected_images=selection['images'])

    def test_missing_metadata_never_releases_merged_delivery(self):
        with self.assertRaisesRegex(LedgerError, 'complete segment metadata required'):
            self.run_parts(downloader=lambda url: result_zip(self.provider.uploads[url.rsplit('/',1)[-1]], metadata=False))

    def test_bad_receipt_coverage_and_original_hash_rejected(self):
        result = self.run_parts(); receipt = result['receipt']
        for mutate in (lambda r: r['segments'][1].update(page_start=200),
                       lambda r: r['segments'][1]['lineage'].update(data_id='a'*64),
                       lambda r: r.update(merged_zip_sha256='a'*64),
                       lambda r: r['original_binding'].update(sha256='a'*64)):
            value = copy.deepcopy(receipt); mutate(value)
            with self.assertRaises((LedgerError, ValueError)):
                segments.validate_segment_receipt(value, self.ledger.bind(self.original, 'original.pdf'), result['zip_bytes'])

    def test_provider_embedded_pixels_remain_subject_to_original_proof(self):
        result = self.run_parts()
        report = self.root/'tamper'; report.mkdir()
        markdown = safe_unzip(result['zip_bytes'], report/'raw')
        (report/'source_mineru.md').write_bytes(markdown)
        changed = report/'changed.pdf'
        with fitz.open(report/'raw/source.pdf') as doc:
            doc[200].insert_text((20, 70), 'Provider mismatch')
            doc.save(changed)
        (report/'raw/source.pdf').write_bytes(changed.read_bytes())
        from mineru_figure_sources import create_figure_sources, FigureSourceError
        with self.assertRaises(FigureSourceError):
            create_figure_sources(report/'raw', report/'assets', original_pdf_sha256=digest(self.original.read_bytes()),
                markdown_sha256=digest(markdown), auth_original_pdf=self.original)

    def test_exact_segment_archives_exist_before_any_provider_submission(self):
        original_submit = self.provider.submit
        def submit(*args):
            frozen = segments.read_segment_plan(self.ledger, self.ledger.bind(self.original, 'original.pdf'))
            archive = segments.SegmentArchive(self.cache.client, self.cache.bucket)
            for row in frozen['segments']:
                self.assertIsNotNone(archive.get(frozen['original_binding'], row['binding']))
            return original_submit(*args)
        self.provider.submit = submit
        self.run_parts()

    def test_archive_restores_exact_segment_bytes_without_rerunning_splitter(self):
        self.run_parts()
        with patch.object(fitz.Document, 'tobytes', side_effect=AssertionError('splitter must not run')):
            plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.root/'restored',
                allow_plan_write=False, archive=segments.SegmentArchive(self.cache.client, self.cache.bucket))
        self.assertEqual(plan['page_count'], 202)

    def test_archive_lost_ack_stops_before_any_provider_submission(self):
        def fail(key, kwargs):
            if key.startswith(segments.ARCHIVE_PREFIX): raise RuntimeError('lost ACK')
        self.cache.client.after_put = fail
        with self.assertRaisesRegex(LedgerError, 'archive write unresolved'):
            self.run_parts()
        self.assertFalse(self.provider.posts)

    def test_explicit_source_bytes_change_stops_without_new_identity_admission(self):
        plan = segments.prepare_segments(self.ledger, self.original, 'original.pdf', self.directory)
        self.directory.joinpath(Path(plan['segments'][0]['binding']['source']).name).write_bytes(b'changed')
        with self.assertRaisesRegex(LedgerError, 'local segment bytes changed'): self.run_parts()
        self.assertFalse(self.provider.posts)


if __name__ == '__main__':
    unittest.main()
