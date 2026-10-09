"""Separate OCR provenance from MinerU through report translation inputs."""
from argparse import Namespace
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import build_portal_translated_reports as builder
from report_extraction_source import digest, ocr_markdown_from_pages, resolve_extraction_source


class ExtractionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / 'report'
        self.directory.mkdir()
        text = 'Revenue was 10 million. Output expanded.'
        self.pages = [{'page': 1, 'text': text, 'text_sha256': digest(text.encode()), 'empty_text': False, 'method': 'ocr'}]
        self.raw_pages = json.dumps(self.pages).encode()
        self.content = ocr_markdown_from_pages(self.pages, 1)
        self.status = {'source_method': 'ocr', 'source_markdown': 'source_ocr.md', 'source_pdf': 'fixture.pdf',
          'wechat_source_provenance': {'source_kind': 'ocr-synthesis', 'source_pdf': 'fixture.pdf',
             'content_sha256': 'a' * 64, 'source_receipt_sha256': 'b' * 64,
             'source_pages_sha256': digest(self.raw_pages), 'source_report_id': 'R001'}}

    def ocr(self):
        (self.directory / 'source_ocr.md').write_bytes(self.content)
        (self.directory / 'source_ocr_pages.json').write_bytes(self.raw_pages)
        self.save_status()

    def save_status(self):
        (self.directory / 'status.json').write_text(json.dumps(self.status))

    def test_original_mineru_status_remains_optional_and_cache_path_unchanged(self):
        (self.directory / 'source_mineru.md').write_bytes(self.content)
        source = resolve_extraction_source(self.directory)
        self.assertEqual(source.method, 'mineru')
        self.assertEqual(source.cache_namespace(), '')
        self.assertIsNone(source.provenance_sha256)

    def test_ocr_requires_independent_provenance_and_page_derived_text(self):
        self.ocr()
        source = resolve_extraction_source(self.directory)
        self.assertEqual(source.method, 'ocr')
        self.assertEqual(source.path.name, 'source_ocr.md')
        self.assertEqual(source.sha256, digest(self.content))
        self.assertTrue(source.cache_namespace().startswith('ocr-'))
        clean, figures = builder.prepare_clean_markdown(self.directory, self.root / 'clean', 0)
        self.assertIn('Revenue was 10 million.', clean)
        self.assertEqual(figures, [])

    def test_ocr_without_status_or_provenance_is_never_inferred_as_mineru(self):
        self.ocr()
        for status in ({}, {'source_method': 'ocr', 'source_markdown': 'source_ocr.md'}):
            with self.subTest(status=status):
                (self.directory / 'status.json').write_text(json.dumps(status))
                with self.assertRaises(ValueError):
                    resolve_extraction_source(self.directory)

    def test_unknown_method_and_traversal_or_wrong_file_paths_are_rejected(self):
        self.ocr()
        original = copy.deepcopy(self.status)
        for key, value in [('source_method', 'unknown'), ('source_markdown', '../source_ocr.md'),
                           ('source_markdown', '/tmp/source_ocr.md'), ('source_markdown', 'source_mineru.md')]:
            with self.subTest(key=key, value=value):
                self.status = {**original, key: value}
                self.save_status()
                with self.assertRaises(ValueError):
                    resolve_extraction_source(self.directory)

    def test_dual_sources_fail_discovery_instead_of_silent_preference(self):
        self.ocr()
        (self.directory / 'source_mineru.md').write_bytes(self.content)
        with self.assertRaisesRegex(ValueError, 'conflicting'):
            builder.find_report_dirs(self.root)

    def test_symlink_source_status_and_page_evidence_are_rejected(self):
        self.ocr()
        for name in ('source_ocr.md', 'source_ocr_pages.json', 'status.json'):
            with self.subTest(name=name):
                path = self.directory / name
                raw = path.read_bytes()
                external = self.root / ('other-' + name)
                external.write_bytes(raw)
                path.unlink()
                path.symlink_to(external)
                with self.assertRaises(ValueError):
                    resolve_extraction_source(self.directory)
                path.unlink()
                path.write_bytes(raw)

    def test_modified_page_evidence_and_markdown_fail_independently(self):
        self.ocr()
        (self.directory / 'source_ocr.md').write_bytes(self.content + b'Invented content')
        with self.assertRaisesRegex(ValueError, 'does not match'):
            resolve_extraction_source(self.directory)
        (self.directory / 'source_ocr.md').write_bytes(self.content)
        (self.directory / 'source_ocr_pages.json').write_bytes(self.raw_pages + b' ')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            resolve_extraction_source(self.directory)

    def test_page_gaps_reordered_text_method_and_hash_evidence_fail(self):
        for key, value in [('page', 2), ('text_sha256', 'a' * 64), ('empty_text', True), ('method', 'unknown')]:
            with self.subTest(key=key):
                pages = copy.deepcopy(self.pages)
                pages[0][key] = value
                with self.assertRaises(ValueError):
                    ocr_markdown_from_pages(pages, 1)
        with self.assertRaises(ValueError):
            ocr_markdown_from_pages(self.pages, 2)

    def test_provenance_source_kind_and_pdf_identity_cannot_be_relabelled(self):
        self.ocr()
        for key, value in [('source_kind', 'mineru-recovery'), ('source_pdf', 'different.pdf'),
                           ('source_receipt_sha256', 'invalid'), ('source_report_id', '../R001')]:
            with self.subTest(key=key):
                changed = copy.deepcopy(self.status)
                changed['wechat_source_provenance'][key] = value
                (self.directory / 'status.json').write_text(json.dumps(changed))
                with self.assertRaises(ValueError):
                    resolve_extraction_source(self.directory)

    def test_ocr_process_uses_offline_translation_and_separate_cache(self):
        self.ocr()
        engine = Mock(model_id='offline-test')
        engine.translate_markdown.return_value = '# 收入\n\n收入为1000万。'
        engine.translate.return_value = '收入'
        args = Namespace(max_images_per_report=0, title_refine=True)
        with patch('offline_translation.OfflineTranslator', return_value=engine) as factory, \
             patch.object(builder, 'is_public_or_consulting_report', return_value=False), \
             patch.object(builder, 'render_pdf'), \
             patch.object(builder, 'call_deepseek', side_effect=AssertionError('Paid translation forbidden')) as paid:
            row = builder.process_report(self.directory, self.root / 'out', 1, args)
        self.assertEqual(row['source_method'], 'ocr')
        self.assertEqual(row['source_markdown'], 'source_ocr.md')
        self.assertEqual(row['source_sha256'], digest(self.content))
        self.assertEqual(row['body_provider'], 'hymt')
        cache_dir = factory.call_args.kwargs['cache_dir']
        self.assertTrue(cache_dir.parent.name.startswith('ocr-'))
        paid.assert_not_called()


if __name__ == '__main__':
    unittest.main()
