"""Original vector/table crops survive the real OCR-to-article boundary."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import fitz
import original_pdf_figures as figures
from report_extraction_source import ocr_markdown_from_pages
from wechat_image_quality import source_chart_images


def chart_pdf(count=4):
    document = fitz.open()
    pages = []
    for index in range(count):
        page = document.new_page(width=600, height=800)
        text = f'Figure {index + 1}: revenue 10 20 30 40. Research growth and valuation evidence.'
        page.insert_text((50, 80), text)
        page.draw_rect(fitz.Rect(70, 150, 510, 420), color=(0, 0, 0))
        for number in range(4):
            page.draw_rect(fitz.Rect(100 + number * 95, 380 - number * 45, 150 + number * 95, 400),
                           color=(0, .3, .8), fill=(0, .3, .8))
        pages.append({'page': index + 1, 'text': text, 'method': 'native',
                      'text_sha256': figures.digest(text.encode()), 'empty_text': False})
    raw = document.tobytes(); document.close()
    return raw, pages


def scanned_pdf(text):
    with fitz.open() as template:
        page = template.new_page(width=600, height=800)
        page.insert_textbox(fitz.Rect(45, 40, 555, 740), text, fontsize=11)
        page.draw_rect(fitz.Rect(70, 520, 500, 700), color=(.1, .3, .8))
        pixels = page.get_pixmap(dpi=120, alpha=False).tobytes('png')
    with fitz.open() as document:
        page = document.new_page(width=600, height=800)
        page.insert_image(page.rect, stream=pixels)
        raw = document.tobytes()
    return raw, [{'page': 1, 'text': text, 'method': 'ocr',
                  'text_sha256': figures.digest(text.encode()), 'empty_text': False}]


class OriginalFiguresTests(unittest.TestCase):
    def test_unnumbered_banking_rating_appendix_is_excluded_and_previous_proof_replays(self):
        text = ('Global research\nRating Distribution\nInvestment Banking Relationships\n'
                'Buy Hold Sell\n50% 34% 16% 65% 58% 43%\n2026 2025 2024 2023 2022 2021\n'
                'Source: Research\nSource: Rating definitions')
        pdf, pages = scanned_pdf(text); sha = figures.digest(text.encode())
        previous, retained = figures.extract(pdf, pages, source_sha256=sha, policy=figures.PREVIOUS_POLICY)
        self.assertEqual(len(retained), 1)
        figures.validate(previous, retained.__getitem__, original_pdf_sha256=figures.digest(pdf),
                         source_sha256=sha, pdf=pdf, pages=pages)
        current, files = figures.extract(pdf, pages, source_sha256=sha)
        self.assertEqual(files, {})
        self.assertEqual(current['candidate_count'], 0)

    def test_unnumbered_scanned_plot_grids_and_financial_snapshots_keep_original_pixels(self):
        examples = [
            'China imports\nIndex, sa, 3mma\n0 20 40 60 80 100\n2019 2020 2021 2022 2023 2024\nSource: Customs\n'
            'China export prices\n% yoy\n0 10 20 30 40\nSource: Research',
            'Company snapshot\nFiscal Year Ending 2025 2026 2027 2028\nEPS 3.13 2.36 4.88 7.17\n'
            'Revenue 3028 3709 4884 6205\nMkt cap 13983\n52-Week Range 29.35 12.00\n'
            'For analyst certification and other important disclosures, please refer to the end of this report.',
        ]
        for text in examples:
            with self.subTest(snapshot='Fiscal Year' in text):
                pdf, pages = scanned_pdf(text); sha = figures.digest(text.encode())
                legacy, old_files = figures.extract(pdf, pages, source_sha256=sha, policy=figures.LEGACY_POLICY)
                self.assertEqual(old_files, {})
                figures.validate(legacy, old_files.__getitem__, original_pdf_sha256=figures.digest(pdf),
                                 source_sha256=sha, pdf=pdf, pages=pages)
                proof, files = figures.extract(pdf, pages, source_sha256=sha)
                self.assertEqual(len(files), 1)
                self.assertEqual(proof['assets'][0]['kind'], 'original_pdf_chart_page')
                figures.validate(proof, files.__getitem__, original_pdf_sha256=figures.digest(pdf),
                                 source_sha256=sha, pdf=pdf, pages=pages)

    def test_scanned_legal_appendix_and_numeric_prose_do_not_become_charts(self):
        examples = [
            'Analyst Certification\nImportant Disclosures\nRating Distribution\n% Buy Hold Sell\n'
            '10 20 30 40 50 60 70 80 90 100 110 120\nSource: Bank\nSource: Ratings\nInvestment banking clients',
            ('Revenue and EPS expanded across the operations described in this report with growth measured at '
             '1% 2% 3% 4% 5% 6% 7% 8% 9% 10% 11% 12% and the following long narrative discusses how '
             'management expects demand to develop across its markets during the coming quarters.\nSource: Company'),
        ]
        for text in examples:
            pdf, pages = scanned_pdf(text)
            proof, files = figures.extract(pdf, pages, source_sha256=figures.digest(text.encode()))
            self.assertEqual(files, {})
            self.assertEqual(proof['candidate_count'], 0)

    def test_real_vector_crops_are_replayed_and_admitted_as_ocr_originals(self):
        pdf, pages = chart_pdf()
        markdown = ocr_markdown_from_pages(pages, len(pages))
        proof, files = figures.extract(pdf, pages, source_sha256=figures.digest(markdown))
        self.assertEqual(len(files), 3)
        self.assertGreaterEqual(proof['candidate_count'], 4)
        self.assertEqual([r['page'] for r in proof['assets']], [1, 2, 3])
        figures.validate(proof, files.__getitem__, original_pdf_sha256=figures.digest(pdf),
                         source_sha256=figures.digest(markdown), pdf=pdf, pages=pages)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            figures.write(root, proof, files)
            pages_raw = json.dumps(pages).encode()
            (root / 'source_ocr_pages.json').write_bytes(pages_raw)
            (root / 'source_ocr.md').write_bytes(markdown)
            (root / 'status.json').write_text(json.dumps({'source_pdf': 'report.pdf', 'source_method': 'ocr',
                'source_markdown': 'source_ocr.md', 'original_pdf_sha256': figures.digest(pdf),
                'original_figures_sha256': figures.digest(figures.encode(proof)),
                'images': list(files), 'chart_source_image_count': len(files),
                'wechat_source_provenance': {'source_kind': 'ocr-pages', 'source_pdf': 'report.pdf',
                    'content_sha256': figures.digest(pdf), 'source_receipt_sha256': 'a' * 64,
                    'source_report_id': 'R001', 'source_pages_sha256': figures.digest(pages_raw)}}))
            self.assertEqual(source_chart_images(root, require_verified=True), [root / ref for ref in files])
            (root / next(iter(files))).write_bytes(b'not the original chart')
            with self.assertRaisesRegex(ValueError, 'original_figure'):
                source_chart_images(root, require_verified=True)

    def test_wrong_original_text_or_crop_pixels_are_rejected(self):
        pdf, pages = chart_pdf(1)
        proof, files = figures.extract(pdf, pages, source_sha256='b' * 64)
        for sha, text in (('a' * 64, 'b' * 64), (figures.digest(pdf), 'c' * 64)):
            with self.assertRaises(ValueError):
                figures.validate(proof, files.__getitem__, original_pdf_sha256=sha, source_sha256=text)
        changed = copy.deepcopy(proof)
        changed['assets'][0]['bbox'][0] += 10
        with self.assertRaises(ValueError):
            figures.validate(changed, files.__getitem__, original_pdf_sha256=figures.digest(pdf),
                             source_sha256='b' * 64, pdf=pdf, pages=pages)

    def test_text_only_ocr_cannot_silently_become_editorial_illustrations(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'status.json').write_text(json.dumps({'source_method': 'ocr', 'images': [],
                                                        'image_source_kind': 'ocr_pages_text_only'}))
            with self.assertRaisesRegex(ValueError, 'source_figure_audit_missing'):
                source_chart_images(root, require_verified=True)


if __name__ == '__main__':
    unittest.main()
