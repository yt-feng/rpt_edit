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


def result_zip(raw, *, label='part', profile='3.4.4', metadata=True, inline_table=False):
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
    picture = io.BytesIO(); Image.new('RGB', (700, 500), (40, 100, 160)).save(picture, 'PNG')
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('result/full.md', label+'\n![](images/same.png)\n<img src="images/same.png">\n')
        archive.writestr('result/images/same.png', picture.getvalue())
        if inline_table:
            archive.writestr('result/images/'+'a'*64+'.jpg', picture.getvalue())
        archive.writestr('result/source.pdf', raw)
        if metadata:
            archive.writestr('result/content_list.json', json.dumps([content]))
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
