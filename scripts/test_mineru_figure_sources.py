#!/usr/bin/env python3
"""Actual-shape provider fixtures plus real PDF/pixel crop replay, without OCR."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import subprocess
import sys
import tempfile
import unittest
import weakref
from pathlib import Path
from unittest.mock import patch

import fitz
from PIL import Image

import mineru_figure_sources as figures


def digest(data):
    return hashlib.sha256(data).hexdigest()


def text_block(box, text, kind="text", level=0):
    return {"type": kind, "bbox": box, "level": level,
            "lines": [{"bbox": box, "spans": [{"type": "text", "bbox": box, "content": text}]}]}


def visual(index, box, *, kind="table", body="", captions=(), footnotes=(), page_idx=0, size=(400, 500), ref=None):
    ref = ref or f"images/image-{index}.jpg"
    children = [{"type": kind + "_body", "bbox": box,
                 "lines": [{"spans": [{"type": kind, "bbox": box, "image_path": ref[7:], "html": body}]}]}]
    for label, entries in (("caption", captions), ("footnote", footnotes)):
        children.extend({**text_block(b, t), "type": kind + "_" + label} for b, t in entries)
    parent = {"type": kind, "bbox": box, "blocks": children, "index": index}
    content = {"type": kind, "page_idx": page_idx,
               "bbox": [round(box[0] * 1000 / size[0]), round(box[1] * 1000 / size[1]),
                        round(box[2] * 1000 / size[0]), round(box[3] * 1000 / size[1])],
               "img_path": ref, kind + "_caption": [t for _, t in captions], kind + "_footnote": [t for _, t in footnotes],
               "table_body" if kind == "table" else "content": body}
    return content, parent


class Fixture:
    def __init__(self, root, visuals=None, text_blocks=(), size=(400, 500), actual_size=None, pages=1):
        self.root = root
        self.raw = root / "report" / "mineru_raw"
        self.report = self.raw.parent
        self.assets = self.report / "assets"
        self.raw.mkdir(parents=True)
        self.size = size
        self.actual_size = actual_size or size
        self.content = []
        self.middle = {"_backend": "hybrid", "_version_name": "3.4.4", "_ocr_enable": True, "_effort": "medium", "pdf_info": []}
        visuals = visuals if visuals is not None else [visual(0, [35, 100, 185, 260], kind="chart",
                    captions=[([35, 80, 180, 99], "Figure 1: Growth")], size=size)]
        # Inputs use lists of (bbox,text); convenient single-tuples are normalised.
        for pi in range(pages):
            self.middle["pdf_info"].append({"page_idx": pi, "page_size": list(size), "para_blocks": list(text_blocks) if pi == 0 else []})
        for content, parent in visuals:
            self.content.append(content)
            self.middle["pdf_info"][content["page_idx"]]["para_blocks"].append(parent)
            ref = content["img_path"]
            if ref:
                path = self.raw / ref
                path.parent.mkdir(parents=True, exist_ok=True)
                Image.new("RGB", (700, 500), (40, 100, 160)).save(path, "JPEG")
        self.original = root / "original.pdf"
        doc = fitz.open()
        for pi in range(pages):
            page = doc.new_page(width=self.actual_size[0], height=self.actual_size[1])
            page.insert_text((20, 30), "Verified source page", fontsize=12)
            for c, p in visuals:
                if c["page_idx"] != pi:
                    continue
                page.draw_rect(fitz.Rect(p["bbox"]), color=(.2, .4, .6), fill=(.8, .9, 1))
                for child in p["blocks"]:
                    if child["type"].endswith(("_caption", "_footnote")):
                        b = child["bbox"]
                        page.draw_rect(fitz.Rect(b), color=(.7, .1, .1), fill=(.9, .5, .5))
        doc.save(self.original)
        doc.close()
        (self.raw / "source.pdf").write_bytes(self.original.read_bytes())
        self.original_sha = digest(self.original.read_bytes())
        (self.report / "source_mineru.md").write_text("\n".join("![](" + c["img_path"] + ")" for c, _ in visuals))
        self.md_sha = digest((self.report / "source_mineru.md").read_bytes())
        self.write_metadata()

    def write_metadata(self):
        (self.raw / "content_list.json").write_text(json.dumps(self.content))
        (self.raw / "middle.json").write_text(json.dumps(self.middle))

    def create(self, *, auth=True, admitted=True, maximum=100):
        self.selection = figures.create_figure_sources(self.raw, self.assets,
            original_pdf_sha256=self.original_sha if admitted else None,
            markdown_sha256=self.md_sha, auth_original_pdf=self.original if auth else None, max_images=maximum)
        self.admitted = admitted
        return self.selection

    def status(self):
        value = {"source_markdown": "source_mineru.md", "original_pdf_sha256": self.original_sha if self.admitted else None,
                 "images": self.selection["images"], "source_figure_map": figures.SIDECAR,
                 "source_figure_map_sha256": digest((self.report / figures.SIDECAR).read_bytes())}
        (self.report / "status.json").write_text(json.dumps(value))

    def validate(self):
        return figures.validate_figure_sources(self.report,
            expected_original_sha256=self.original_sha if self.admitted else None,
            expected_markdown_sha256=self.md_sha, expected_images=self.selection["images"])

    def proof(self):
        return json.loads((self.report / figures.SIDECAR).read_bytes())

    def mutate(self, callback, *, reseal=True):
        value = self.proof()
        callback(value)
        if reseal:
            value["metadata_sha256"] = digest(figures._canonical(value["metadata"]))
        (self.report / figures.SIDECAR).write_bytes(figures._canonical(value))


class FigureSourceTests(unittest.TestCase):
    def test_fractional_page_dimensions_create_status_and_replay_with_exact_mupdf_raster(self):
        for actual, provider, expected in (((595.2, 500), (595, 500), [2480, 2084]),
                                          ((400.08001, 500.16), (400, 500), [1667, 2084])):
            with self.subTest(size=actual):
                fixture = self.fixture(size=provider, actual_size=actual)
                fixture.create(); fixture.status()
                page = fixture.proof()["pages"][0]
                self.assertEqual(page["pixel_size"], expected)
                self.assertNotEqual(expected, [math.ceil(value * 300 / 72) for value in page["geometry"]["rect"][2:]])
                self.assertEqual(figures._raster_size(page["geometry"]["rect"]), expected)
                import shutil
                shutil.rmtree(fixture.raw)
                self.assertEqual(len(fixture.validate()), 1)

    def test_fractional_carrier_cannot_gain_a_pixel_even_if_hashes_are_resealed(self):
        for axis in (0, 1):
            with self.subTest(axis=axis):
                fixture = self.fixture(size=(595, 500), actual_size=(595.2, 500.16))
                fixture.create()
                proof = fixture.proof(); page = proof["pages"][0]
                path = fixture.report / page["path"]
                with Image.open(path) as image:
                    size = list(image.size); size[axis] += 1
                    forged = Image.new("RGB", tuple(size), (255, 255, 255))
                    forged.paste(image, (0, 0))
                page.update(figures._save(forged, path)); forged.close()
                (fixture.report / figures.SIDECAR).write_bytes(figures._canonical(proof))
                fixture.status()
                with self.assertRaisesRegex(figures.FigureSourceError, "figure_source_pixels_mismatch"):
                    fixture.validate()

    def test_renderer_pixel_dimensions_must_equal_its_bounded_raster_rectangle(self):
        with fitz.open() as document:
            page = document.new_page(width=20, height=20)
            width, height = figures._raster_size(list(page.rect))
            wrong = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, width + 1, height), False)
            with patch.object(fitz.Page, "get_pixmap", return_value=wrong):
                with self.assertRaisesRegex(figures.FigureSourceError, "figure_source_pixels_mismatch"):
                    figures._render(page)
        for rect in ([0, 0, float("inf"), 1], [0, 0, 20000, 20000], [1, 0, 10, 10], [0, 0, 0, 10]):
            with self.subTest(rect=rect), self.assertRaisesRegex(figures.FigureSourceError, "figure_source_pixels_mismatch"):
                figures._raster_size(rect)

    def test_interleaved_document_cache_cannot_change_carried_source_or_provider_pixels(self):
        # Model the observed cross-document warmed-store corruption without
        # publishing the private 42-page regression report. All PDF inputs here
        # are generated; the real renderer still produces and replays carriers.
        with tempfile.TemporaryDirectory() as temporary:
            visuals = [
                visual(0, [35, 100, 185, 260], kind="chart", page_idx=0),
                visual(1, [35, 100, 185, 260], kind="chart", page_idx=1)]
            fixture = Fixture(Path(temporary) / "isolated", pages=2, visuals=visuals)
            native_render, native_clear = fitz.Page.get_pixmap, fitz.TOOLS.store_shrink
            warmed = {"document": None}
            events = []

            def clear(percent):
                self.assertEqual(percent, 100)
                native_clear(percent)
                warmed["document"] = None
                events.append("clear")

            def render(page, **kwargs):
                image = native_render(page, **kwargs)
                if warmed["document"] is not None and warmed["document"] != id(page.parent):
                    image.set_pixel(0, 0, (17, 23, 41))
                warmed["document"] = id(page.parent)
                events.append("render")
                return image

            unisolated = Fixture(Path(temporary) / "warmed", pages=2, visuals=visuals)
            with patch.object(fitz.TOOLS, "store_shrink", return_value=0), \
                    patch.object(fitz.Page, "get_pixmap", render):
                with self.assertRaisesRegex(figures.FigureSourceError, "figure_source_pixels_mismatch"):
                    unisolated.create()
            events.clear()
            with patch.object(fitz.TOOLS, "store_shrink", side_effect=clear), \
                    patch.object(fitz.Page, "get_pixmap", render):
                fixture.create()
            self.assertEqual(events, ["clear", "render"] * 4)
            self.assertEqual(fixture.proof()["schema"], 1)
            self.assertEqual(len(fixture.proof()["pages"]), 2)
            self.assertIsNotNone(fixture.validate())

    def test_cache_isolation_failure_stops_before_any_render(self):
        with fitz.open() as document:
            page = document.new_page(width=20, height=20)
            with patch.object(fitz.TOOLS, "store_shrink", side_effect=RuntimeError("private detail")), \
                    patch.object(fitz.Page, "get_pixmap") as render:
                with self.assertRaises(figures.FigureSourceError) as caught:
                    figures._render(page)
            self.assertEqual(caught.exception.category, "figure_render_cache_isolation_failed")
            self.assertNotIn("private detail", str(caught.exception))
            render.assert_not_called()

    def fixture(self, **kwargs):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        return Fixture(Path(tmp.name), **kwargs)

    def test_authority_helpers_import_in_true_stdlib_only_subprocess(self):
        # GitHub's authorization step runs before PyMuPDF/Pillow installation.
        # -S removes site-packages rather than mocking successful library loads.
        program = r'''
import sys, tempfile
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import mineru_figure_sources as figures
import consume_legacy_mineru as consumer
import recover_durable_mineru_sources as recovery
assert not any(name.split('.')[0] in {'PIL','fitz','pymupdf'} for name in sys.modules)
producer={'id':123,'path':recovery.PRODUCER,'head_branch':'main',
          'repository':{'full_name':'owner/repo'},'head_sha':'a'*40}
assert recovery.check_producer(producer,'123','owner/repo')=='a'*40
consumer.valid_url('https://example.invalid/result.zip')
assert figures._cues('Statistical distribution of returns')['disclosures']==0
with tempfile.TemporaryDirectory() as temp:
 root=Path(temp);raw=root/'raw';raw.mkdir()
 assert figures.create_figure_sources(raw,root/'assets',original_pdf_sha256=None,markdown_sha256='') is None
 assert figures.validate_figure_sources(root,expected_original_sha256=None,expected_markdown_sha256='',expected_images=[]) is None
assert not any(name.split('.')[0] in {'PIL','fitz','pymupdf'} for name in sys.modules)
print('stdlib_authority_import_ready')
'''
        result = subprocess.run([sys.executable, "-S", "-B", "-c", program, str(Path(figures.__file__).parent)],
                                capture_output=True, timeout=30, check=False)
        self.assertEqual(result.returncode, 0, "Pre-install source authority imports failed")
        self.assertIn(b"stdlib_authority_import_ready", result.stdout)

    def test_tls_cache_and_auth_imports_do_not_attempt_image_libraries(self):
        # TLS already requires requests/certifi/urllib3. Keep those real modules,
        # but fail every attempt to import either new source-image dependency.
        program = r'''
import sys, importlib.abc, socket
sys.path.insert(0, sys.argv[1])
attempted=[]
class NoImageDependencies(importlib.abc.MetaPathFinder):
 def find_spec(self, fullname, path=None, target=None):
  if fullname.split('.')[0] in {'PIL','fitz','pymupdf'}:
   attempted.append(fullname)
   raise ImportError('image_dependencies_not_installed')
sys.meta_path.insert(0,NoImageDependencies())
def no_network(*args,**kwargs): raise AssertionError('No network allowed')
socket.create_connection=no_network
import consume_legacy_mineru
import recover_durable_mineru_sources
import probe_mineru_result_tls
import mineru_result_cache
import mineru_pinned_result_transport
import seed_mineru_result_cache
assert not attempted
assert not any(name.split('.')[0] in {'PIL','fitz','pymupdf'} for name in sys.modules)
assert probe_mineru_result_tls.cloud_manual_execution_allowed({}) is False
assert callable(seed_mineru_result_cache.check_producer)
print('tls_cache_authority_import_ready')
'''
        result = subprocess.run([sys.executable, "-B", "-c", program, str(Path(figures.__file__).parent)],
                                capture_output=True, timeout=30, check=False)
        self.assertEqual(result.returncode, 0, "Existing TLS/cache imports attempted image dependencies")
        self.assertIn(b"tls_cache_authority_import_ready", result.stdout)

    def test_missing_metadata_is_only_legacy_none_and_missing_hashes_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "raw"
            raw.mkdir()
            self.assertIsNone(figures.create_figure_sources(raw, Path(tmp) / "assets", original_pdf_sha256=None, markdown_sha256=""))
            (raw / "middle.json").write_text("{}")
            with self.assertRaises(figures.FigureSourceError):
                figures.create_figure_sources(raw, Path(tmp) / "assets", original_pdf_sha256=None, markdown_sha256="")

    def test_missing_oc_configuration_restores_exact_all_selected_pages_and_v2_replay(self):
        from test_mineru_pdf_oc import optional_content_fixture
        fixture=self.fixture(pages=2,visuals=[visual(0,[35,100,185,260],kind='chart',page_idx=0),
                                              visual(1,[35,100,185,260],kind='chart',page_idx=1)])
        original,embedded=optional_content_fixture(pages=2,plain_first=True)
        fixture.original.write_bytes(original);fixture.original_sha=digest(original)
        (fixture.raw/'source.pdf').write_bytes(embedded)
        fixture.create();fixture.status()
        proof=fixture.proof()
        self.assertEqual(proof['schema'],2)
        self.assertEqual(proof['embedded_pdf_sha256'],digest(embedded))
        repair=proof['embedded_pdf_render_restoration']
        self.assertEqual(repair['verified_page_indices'],[0,1])
        self.assertEqual(repair['original_pdf_sha256'],digest(original))
        self.assertEqual((fixture.raw/'source.pdf').read_bytes(),embedded)
        self.assertTrue(all(asset['mode']=='authenticated_original_crop' for asset in proof['assets']))
        import shutil
        shutil.rmtree(fixture.raw)
        self.assertEqual(len(fixture.validate()),2)

    def test_oc_repair_refuses_hidden_content_changes_or_existing_provider_config(self):
        from test_mineru_pdf_oc import optional_content_fixture,changed_provider
        for change in ('image','text','swap','extra','existing'):
            with self.subTest(change=change):
                fixture=self.fixture()
                original,embedded=optional_content_fixture()
                fixture.original.write_bytes(original);fixture.original_sha=digest(original)
                (fixture.raw/'source.pdf').write_bytes(changed_provider(embedded,change))
                with self.assertRaises(figures.FigureSourceError): fixture.create()
                self.assertFalse((fixture.report/figures.SIDECAR).exists())

    def test_v2_oc_proof_binding_and_verified_page_tampering_are_rejected(self):
        from test_mineru_pdf_oc import optional_content_fixture
        for key,value in [('embedded_pdf_sha256','0'*64),('verified_page_indices',[]),('verified_page_indices',[False]),('schema',True)]:
            with self.subTest(key=key):
                fixture=self.fixture();original,embedded=optional_content_fixture()
                fixture.original.write_bytes(original);fixture.original_sha=digest(original)
                (fixture.raw/'source.pdf').write_bytes(embedded)
                fixture.create()
                fixture.mutate(lambda proof:proof['embedded_pdf_render_restoration'].__setitem__(key,value))
                with self.assertRaises(figures.FigureSourceError):fixture.validate()

    def test_authenticated_crop_preserves_caption_pixels_and_replays_after_raw_removed(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 185, 260], kind="chart",
            captions=[([35, 80, 180, 99], "Figure 1: Growth")], footnotes=[([35, 264, 180, 276], "Source data")])])
        selection = fixture.create()
        fixture.status()
        value = fixture.proof()
        self.assertEqual(value["assets"][0]["crop"]["union_bbox"], [35, 80, 185, 276])
        self.assertEqual(len(value["pages"]), 1)
        import shutil
        shutil.rmtree(fixture.raw)
        self.assertEqual(fixture.validate(), {"images/image-0.jpg": selection["images"][0]})

    def test_missing_output_intents_restores_all_selected_pages_and_v2_replay(self):
        from test_mineru_pdf_output_intents import output_intent_fixture,pdfium_copy
        from mineru_pdf_output_intents import POLICY
        fixture=self.fixture(pages=2,visuals=[visual(0,[35,100,185,260],kind='chart',page_idx=0),
                                              visual(1,[35,100,185,260],kind='chart',page_idx=1)])
        original=output_intent_fixture(plain_first=True);embedded=pdfium_copy(original)
        fixture.original.write_bytes(original);fixture.original_sha=digest(original)
        (fixture.raw/'source.pdf').write_bytes(embedded)
        fixture.create();fixture.status();proof=fixture.proof()
        self.assertEqual(proof['schema'],2)
        repair=proof['embedded_pdf_render_restoration']
        self.assertEqual(repair['policy'],POLICY);self.assertEqual(repair['verified_page_indices'],[0,1])
        self.assertEqual(repair['original_pdf_sha256'],digest(original))
        self.assertEqual(repair['embedded_pdf_sha256'],digest(embedded))
        self.assertEqual(fixture.original.read_bytes(),original)
        self.assertEqual((fixture.raw/'source.pdf').read_bytes(),embedded)
        self.assertTrue(all(asset['mode']=='authenticated_original_crop' for asset in proof['assets']))
        import shutil
        shutil.rmtree(fixture.raw)
        self.assertEqual(len(fixture.validate()),2)

    def test_color_restoration_never_accepts_changed_provider_body_or_changed_pixels(self):
        from test_mineru_pdf_output_intents import output_intent_fixture,pdfium_copy,changed
        import mineru_pdf_output_intents as color
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        fixture=self.fixture();fixture.original.write_bytes(original);fixture.original_sha=digest(original)
        modified=changed(embedded,lambda doc:doc[0].insert_text((30,80),'ALTERED',fontsize=9))
        (fixture.raw/'source.pdf').write_bytes(modified)
        with self.assertRaises(figures.FigureSourceError):fixture.create()
        self.assertFalse((fixture.report/figures.SIDECAR).exists())
        fixture=self.fixture();fixture.original.write_bytes(original);fixture.original_sha=digest(original)
        (fixture.raw/'source.pdf').write_bytes(embedded)
        real_restore=color.restore_missing_output_intents
        def bad_restore(*args,**kwargs):
            restored,proof=real_restore(*args,**kwargs)
            restored[0].draw_rect((35,100,185,260),fill=(0,1,0))
            return restored,proof
        with patch.object(color,'restore_missing_output_intents',side_effect=bad_restore),self.assertRaises(figures.FigureSourceError):
            fixture.create()
        self.assertFalse((fixture.report/figures.SIDECAR).exists())

    def test_color_restoration_receipt_cannot_change_policy_or_verified_pages(self):
        from test_mineru_pdf_output_intents import output_intent_fixture,pdfium_copy
        original=output_intent_fixture(pages=1);embedded=pdfium_copy(original)
        for key,value in [('policy','unknown'),('policy','authenticated-ocproperties-restoration-v1'),
                          ('embedded_pdf_sha256','0'*64),('verified_page_indices',[]),('verified_page_indices',[False])]:
            with self.subTest(key=key,value=value):
                fixture=self.fixture();fixture.original.write_bytes(original);fixture.original_sha=digest(original)
                (fixture.raw/'source.pdf').write_bytes(embedded);fixture.create()
                fixture.mutate(lambda proof:proof['embedded_pdf_render_restoration'].__setitem__(key,value))
                with self.assertRaises(figures.FigureSourceError):fixture.validate()

    def test_no_auth_preserves_provider_bytes_and_explicit_unproven_identity(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 185, 260])])
        original_bytes = (fixture.raw / "images/image-0.jpg").read_bytes()
        fixture.create(auth=False, admitted=False)
        fixture.status()
        value = fixture.proof()
        self.assertEqual(value["original_identity"], "unproven")
        self.assertFalse(value["authenticated_original_render"])
        self.assertEqual(value["pages"], [])
        self.assertEqual((fixture.report / fixture.selection["images"][0]).read_bytes(), original_bytes)
        self.assertEqual(len(fixture.validate()), 1)

    def test_table_equation_serialization_preserves_exact_formula_and_source_proof(self):
        body = "<table><tr><td><eq>x_1</eq></td><td>27</td><td><eq>y^2</eq></td></tr></table>"
        fixture = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body=body)])
        content_body = body.replace("<eq>", " $").replace("</eq>", "$ ")
        fixture.content[0]["table_body"] = content_body
        fixture.write_metadata()
        content_hash = digest((fixture.raw / "content_list.json").read_bytes())
        middle_hash = digest((fixture.raw / "middle.json").read_bytes())
        fixture.create()
        fixture.status()
        proof = fixture.proof()
        self.assertEqual(proof["metadata"]["records"][0]["body_text"], content_body)
        self.assertEqual(proof["provider_json_sha256"],
                         {"content_list": content_hash, "middle": middle_hash})
        self.assertEqual(proof["assets"][0]["mode"], "authenticated_original_crop")
        import shutil
        shutil.rmtree(fixture.raw)
        self.assertEqual(len(fixture.validate()), 1)

    def test_equation_wrapper_compatibility_does_not_clean_or_change_table_content(self):
        middle = "<table><tr><td><eq>x_1</eq></td><td>27</td></tr></table>"
        valid = middle.replace("<eq>", " $").replace("</eq>", "$ ")
        for changed in (valid.replace("x_1", "x_2"), valid.replace(">27<", ">28<"),
                        valid.replace("<td>", "<th>", 1), valid.replace(" $", "$", 1)):
            with self.subTest(changed=changed):
                fixture = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body=middle)])
                fixture.content[0]["table_body"] = changed
                fixture.write_metadata()
                with self.assertRaisesRegex(figures.FigureSourceError, "figure_metadata_invalid"):
                    fixture.create()
                self.assertFalse((fixture.report / figures.SIDECAR).exists())
        for malformed in ("<eq>x", "x</eq>", "<eq>x</eq></eq>", "<eq><eq>x</eq></eq>"):
            self.assertFalse(figures._table_html_matches(" $x$ ", malformed))

    def test_table_image_directory_serialization_preserves_source_and_pixel_proof(self):
        # Real provider shape: the content list prefixes images/ on an inline
        # hashed JPEG. The middle JSON keeps that same image's bare basename.
        filename = "a" * 64 + ".jpg"
        for equation, prefix_image in (("", True), ("<eq>x_1</eq>", True), ("<eq>x_1</eq>", False)):
            with self.subTest(equation=bool(equation), prefix_image=prefix_image):
                middle = f'<table><tr><td><img src="{filename}"/></td><td>27{equation}</td></tr></table>'
                # Keep accepting the pre-existing eq-only serialization too:
                # adding a new path form must not require it in old results.
                content = middle.replace(f'src="{filename}"', f'src="images/{filename}"') if prefix_image else middle
                content = content.replace("<eq>", " $").replace("</eq>", "$ ")
                fixture = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body=middle)])
                fixture.content[0]["table_body"] = content
                fixture.write_metadata()
                raw_hashes = {"content_list": digest((fixture.raw / "content_list.json").read_bytes()),
                              "middle": digest((fixture.raw / "middle.json").read_bytes())}
                fixture.create()
                fixture.status()
                proof = fixture.proof()
                self.assertEqual(proof["provider_json_sha256"], raw_hashes)
                self.assertEqual(proof["metadata"]["records"][0]["body_text"], content)
                self.assertEqual(proof["assets"][0]["mode"], "authenticated_original_crop")
                import shutil
                shutil.rmtree(fixture.raw)
                self.assertEqual(len(fixture.validate()), 1)

    def test_table_image_directory_compatibility_rejects_content_or_path_changes(self):
        filename = "a" * 64 + ".jpg"
        middle = f'<table><tr><td><img src="{filename}"/></td><td>27<eq>x_1</eq></td></tr></table>'
        valid = middle.replace(f'src="{filename}"', f'src="images/{filename}"')
        valid = valid.replace("<eq>", " $").replace("</eq>", "$ ")
        changed_values = (valid.replace(filename, "b" * 64 + ".jpg"),
                          valid.replace("images/", "images/../"),
                          valid.replace("images/", "other/"), valid.replace(".jpg", ".png"),
                          valid.replace(">27", ">28"), valid.replace("x_1", "x_2"),
                          valid.replace("<td>", "<th>", 1), valid.replace("/>", " />"),
                          valid.replace("src=", "data-src="), valid.replace("</tr>", "<td></td></tr>"))
        for index, changed in enumerate(changed_values):
            with self.subTest(change=index):
                fixture = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body=middle)])
                fixture.content[0]["table_body"] = changed
                fixture.write_metadata()
                with self.assertRaisesRegex(figures.FigureSourceError, "figure_metadata_invalid"):
                    fixture.create()
                self.assertFalse((fixture.report / figures.SIDECAR).exists())
        for ref in ("../" + filename, "https://example.invalid/" + filename, "unhashed.jpg"):
            raw = f'<table><tr><td><img src="{ref}"/></td></tr></table>'
            self.assertFalse(figures._table_html_matches(raw.replace('src="', 'src="images/'), raw))

    def test_page_carriers_are_streamed_and_replayed_without_retaining_all_page_pixels(self):
        fixture = self.fixture(pages=3, visuals=[visual(pi, [35, 100, 185, 260], page_idx=pi)
                                               for pi in (2, 0, 1)])
        live_renders, live_carriers = [], []
        actual_render, actual_image = figures._render, figures._image

        def render(page):
            image = actual_render(page)
            live_renders.append(weakref.ref(image))
            self.assertLessEqual(sum(ref() is not None for ref in live_renders), 2)
            return image

        def decode(data, *, png=False):
            image = actual_image(data, png=png)
            if png and image.size == (1667, 2084):
                live_carriers.append(weakref.ref(image))
                self.assertLessEqual(sum(ref() is not None for ref in live_carriers), 1)
            return image

        with patch.object(figures, "_render", side_effect=render), patch.object(figures, "_image", side_effect=decode):
            fixture.create()
            fixture.status()
            self.assertEqual(len(fixture.proof()["pages"]), 3)
            self.assertEqual(len(fixture.validate()), 3)
        self.assertEqual(sum(ref() is not None for ref in live_renders), 0)
        self.assertEqual(sum(ref() is not None for ref in live_carriers), 0)

    def test_streamed_page_work_remains_bounded_in_producer_and_replay(self):
        fixture = self.fixture(pages=2, visuals=[visual(pi, [35, 100, 185, 260], page_idx=pi)
                                               for pi in range(2)])
        one_page = 1667 * 2084
        with patch.object(figures, "MAX_CARRIED_PAGE_PIXELS", one_page):
            with self.assertRaisesRegex(figures.FigureSourceError, "figure_page_budget_exceeded"):
                fixture.create()
        self.assertFalse((fixture.report / figures.SIDECAR).exists())
        complete = self.fixture(pages=2, visuals=[visual(pi, [35, 100, 185, 260], page_idx=pi)
                                                for pi in range(2)])
        complete.create()
        with patch.object(figures, "MAX_CARRIED_PAGE_PIXELS", one_page):
            with self.assertRaisesRegex(figures.FigureSourceError, "figure_page_budget_exceeded"):
                complete.validate()

    def test_all_legal_records_audited_and_zero_images_is_valid(self):
        body = "<table><tr><td>Important disclosures. Analyst compensation. Legal/compliance. " + "Explanation. " * 30 + "</td></tr></table>"
        fixture = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body=body)])
        fixture.create()
        fixture.status()
        self.assertEqual(fixture.selection["images"], [])
        self.assertTrue(fixture.proof()["decisions"][0]["legal"]["exclude"])
        self.assertEqual(fixture.validate(), {})

    def test_near_legal_heading_plus_body_cue_excludes_but_footer_does_not(self):
        heading = text_block([35, 80, 180, 98], "OTHER DISCLOSURES", "title", 2)
        body = "<table><tr><td>Conflicts of interest. " + "Explanatory terms. " * 20 + "</td></tr></table>"
        fixture = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body=body)], text_blocks=[heading])
        fixture.create(auth=False)
        self.assertEqual(fixture.proof()["decisions"][0]["reason"], "exclude_nearby_legal_scope")
        normal = self.fixture(visuals=[visual(0, [35, 100, 350, 360], body="Distribution of returns. Compensation expenses. " * 8)],
                              text_blocks=[text_block([35, 480, 390, 493], "Copyright. Important disclosures. Legal/compliance.")])
        normal.create()
        self.assertEqual(len(normal.selection["images"]), 1)

    def test_generic_images_and_tables_are_not_blacklisted_and_limit_keeps_all_decisions(self):
        data = [visual(i, [35, 100, 180, 200], kind=kind, page_idx=i) for i, kind in enumerate(("table", "image", "chart"))]
        fixture = self.fixture(visuals=data, pages=3)
        fixture.create(maximum=1)
        self.assertEqual(len(fixture.proof()["decisions"]), 3)
        self.assertEqual([d["reason"] for d in fixture.proof()["decisions"]], ["selected_source_visual", "selection_limit", "selection_limit"])
        self.assertEqual(len(fixture.validate()), 1)

    def test_parent_wrong_column_footnote_excluded_nearest_other_parent_note_included(self):
        # Shape of the actual Cash Flow defect: the note attached to the right
        # table belongs left, while its real source line is attached left.
        left = visual(0, [35, 290, 180, 460], captions=[([35, 275, 180, 289], "Income")],
                      footnotes=[([230, 322, 375, 336], "Cash Flow source")])
        right = visual(1, [230, 180, 375, 320], captions=[([232, 174, 300, 187], "Cash Flow")],
                       footnotes=[([35, 264, 180, 276], "Left source")])
        fixture = self.fixture(visuals=[left, right])
        fixture.create()
        crop = fixture.proof()["assets"][1]["crop"]
        self.assertEqual(crop["union_bbox"], [230, 174, 375, 336])
        self.assertTrue(any(a["owner"] == 0 and a["kind"] == "footnotes" and a["include"] for a in crop["attachments"]))
        self.assertFalse(any(a["owner"] == 1 and a["kind"] == "footnotes" and a["include"] for a in crop["attachments"]))
        self.assertEqual(len(fixture.validate()), 2)

    def test_title_misattached_as_previous_table_note_is_uniquely_recovered(self):
        previous = visual(0, [220, 100, 375, 220], footnotes=[([225, 221, 280, 233], "Factor Profile")])
        chart = visual(1, [220, 230, 375, 370], kind="chart", footnotes=[([230, 376, 375, 392], "Source explanation")])
        fixture = self.fixture(visuals=[previous, chart])
        fixture.create()
        self.assertEqual(fixture.proof()["assets"][1]["crop"]["union_bbox"], [220, 221, 375, 392])
        fixture.validate()

    def test_actual_factor_profile_metadata_shape_recovers_only_misattached_title_and_own_note(self):
        # Sanitised, source-verified provider coordinates; no private report
        # transcript, original bytes, or provider credentials are in the test.
        size = (604, 776)
        previous = visual(0, [358, 370, 555, 495], size=size,
                          footnotes=[([359, 497, 429, 508], "Factor Profile")])
        chart = visual(1, [358, 504, 554, 625], size=size, kind="chart",
                       footnotes=[([370, 631, 554, 649], "Source: synthetic measurements")])
        left = visual(2, [40, 504, 320, 625], size=size,
                      footnotes=[([40, 631, 320, 649], "Left source")])
        fixture = self.fixture(visuals=[previous, chart, left], size=size, actual_size=(604.3864746, 776.0369873))
        fixture.create()
        crop = fixture.proof()["assets"][1]["crop"]
        self.assertEqual(crop["union_bbox"], [358, 497, 554, 649])
        self.assertEqual(crop["pixel_box"], [1488, 2067, 2312, 2708])
        self.assertFalse(any(a["owner"] == 2 and a["include"] for a in crop["attachments"]))
        self.assertEqual(fixture.validate(), fixture.selection["reference_images"])

    def test_actual_adjacent_chart_shape_preserves_caption_and_lower_legend_without_right_column(self):
        size = (595, 826)
        left = visual(0, [46, 212, 293, 329], size=size, kind="chart",
                      captions=[([48, 188, 277, 212], "Figure 9: Synthetic growth")],
                      footnotes=[([49, 333, 202, 343], "Source: synthetic data")])
        right = visual(1, [302, 213, 549, 327], size=size, kind="chart",
                       captions=[([301, 188, 549, 213], "Right figure")],
                       footnotes=[([302, 333, 530, 343], "Right source")])
        fixture = self.fixture(visuals=[left, right], size=size, actual_size=(595, 826.2036743))
        # The real provider body stops before the third legend. Insert the same
        # class of source ink, then prove the crop uses original pixels below it.
        with fitz.open(fixture.original) as doc:
            doc[0].draw_rect(fitz.Rect(70, 329.2, 210, 330.24), color=(0, 0, 0), fill=(0, 0, 0))
            data = doc.tobytes()
        fixture.original.write_bytes(data)
        (fixture.raw / "source.pdf").write_bytes(data)
        fixture.original_sha = digest(data)
        fixture.create()
        crop = fixture.proof()["assets"][0]["crop"]
        self.assertEqual(crop["union_bbox"], [46, 188, 293, 343])
        self.assertEqual(crop["pixel_box"], [188, 780, 1224, 1433])
        self.assertFalse(any(a["owner"] == 1 and a["include"] for a in crop["attachments"]))
        with Image.open(fixture.report / fixture.selection["images"][0]) as im:
            self.assertEqual(im.getpixel((400 - 188, 1374 - 780)), (0, 0, 0))
        fixture.validate()

    def test_ambiguous_and_cross_column_notes_cannot_expand_crop(self):
        first = visual(0, [35, 100, 180, 260], footnotes=[([35, 264, 180, 276], "Ambiguous"), ([230, 264, 375, 276], "Different column")])
        second = visual(1, [35, 100, 180, 260])
        # Ref mapping is unique although overlapping source figures make note
        # ownership genuinely ambiguous. Neither candidate gets the note.
        fixture = self.fixture(visuals=[first, second])
        fixture.create()
        for asset in fixture.proof()["assets"]:
            self.assertEqual(asset["crop"]["union_bbox"], [35, 100, 180, 260])
        fixture.validate()

    def test_multiple_images_on_page_share_one_original_carrier(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260]), visual(1, [230, 100, 375, 260])])
        fixture.create()
        self.assertEqual(len(fixture.proof()["pages"]), 1)
        self.assertEqual(len(fixture.validate()), 2)

    def test_fractional_auth_rect_is_recorded_separately_from_provider_frame(self):
        fixture = self.fixture(visuals=[visual(0, [230, 180, 375, 320], captions=[([232, 174, 300, 187], "Cash Flow")])], actual_size=(400.386, 500.504))
        fixture.create()
        page = fixture.proof()["pages"][0]
        self.assertEqual(page["provider_size"], [400, 500])
        self.assertGreater(page["geometry"]["rect"][2], 400)
        self.assertEqual(page["pixel_size"], [1669, 2086])
        crop = fixture.proof()["assets"][0]["crop"]
        # Integer provider height must not stretch 320pt into 1337px; actual
        # 300dpi matrix gives ceil(320*300/72)+3 == 1337 including margin.
        self.assertEqual(crop["pixel_box"], [955, 722, 1566, 1337])
        self.assertEqual(crop["point_to_pixel"], [300/72, 0, 0, 300/72, 0, 0])
        fixture.validate()

    def test_wide_note_crossing_adjacent_columns_never_expands_left_crop(self):
        left = visual(0, [46, 212, 293, 329], footnotes=[([49, 333, 463, 343], "Cross-column note")], size=(600, 700))
        right = visual(1, [301, 213, 549, 327], size=(600, 700))
        fixture = self.fixture(visuals=[left, right], size=(600, 700))
        fixture.create()
        self.assertEqual(fixture.proof()["assets"][0]["crop"]["union_bbox"], [46, 212, 293, 329])
        self.assertEqual(fixture.proof()["assets"][1]["crop"]["union_bbox"], [301, 213, 549, 327])
        fixture.validate()

    def test_conflicting_title_and_footnote_roles_are_globally_ambiguous(self):
        previous = visual(0, [220, 100, 375, 220], footnotes=[([225, 222, 280, 227], "Short note")])
        chart = visual(1, [220, 229, 375, 370], kind="chart")
        fixture = self.fixture(visuals=[previous, chart])
        fixture.create()
        for asset in fixture.proof()["assets"]:
            note = asset["crop"]["attachments"][0]
            self.assertEqual(note["reason"], "ambiguous_same_column")
            self.assertIsNone(note["winner"])
            self.assertFalse(note["include"])
        fixture.validate()

    def test_wrong_source_hash_and_embedded_pixel_mutation_fail_before_writes(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
        with self.assertRaisesRegex(figures.FigureSourceError, "source_binding"):
            figures.create_figure_sources(fixture.raw, fixture.assets, original_pdf_sha256="0" * 64,
                markdown_sha256=fixture.md_sha, auth_original_pdf=fixture.original)
        self.assertFalse((fixture.report / "figure_source_evidence").exists())
        path = fixture.raw / "source.pdf"
        with fitz.open(path) as doc:
            doc[0].insert_text((30, 70), "Changed", fontsize=15)
            data = doc.tobytes()
        path.write_bytes(data)
        with self.assertRaisesRegex(figures.FigureSourceError, "source_pixels"):
            fixture.create()
        self.assertFalse((fixture.report / "figure_source_evidence").exists())

    def test_duplicate_metadata_ref_unsafe_path_and_profile_change_never_fallback(self):
        for case in ("duplicate", "unsafe", "profile", "bool_bbox", "bad_span"):
            fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
            if case == "duplicate":
                fixture.content.append(copy.deepcopy(fixture.content[0]))
            elif case == "unsafe":
                fixture.content[0]["img_path"] = "../private.jpg"
            elif case == "profile":
                fixture.middle["_version_name"] = "unknown"
            elif case == "bool_bbox":
                fixture.content[0]["bbox"][0] = True
            else:
                fixture.middle["pdf_info"][0]["para_blocks"].insert(0, text_block([35, 30, 180, 50], "Title"))
                fixture.middle["pdf_info"][0]["para_blocks"][0]["lines"][0]["spans"] = [None]
            fixture.write_metadata()
            with self.assertRaises(figures.FigureSourceError):
                fixture.create()

    def test_asset_pixel_and_original_or_markdown_binding_tamper_rejected(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
        fixture.create()
        asset = fixture.report / fixture.selection["images"][0]
        with Image.open(asset) as im:
            value = im.copy()
        value.putpixel((0, 0), (1, 2, 3))
        value.save(asset)
        fixture.mutate(lambda p: p["assets"][0].update(sha256=digest(asset.read_bytes()), rgb_sha256=digest(value.tobytes())))
        with self.assertRaises(figures.FigureSourceError):
            fixture.validate()
        original = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
        original.create()
        with self.assertRaises(figures.FigureSourceError):
            figures.validate_figure_sources(original.report, expected_original_sha256="0" * 64,
                expected_markdown_sha256=original.md_sha, expected_images=original.selection["images"])
        (original.report / "source_mineru.md").write_text("altered")
        with self.assertRaises(figures.FigureSourceError):
            original.validate()

    def test_legal_decision_profile_and_crop_proof_tamper_rejected_even_rehashed(self):
        for case in ("legal", "profile", "crop", "bool_index", "extra"):
            fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
            fixture.create()
            def mutate(p):
                if case == "legal": p["decisions"][0]["legal"]["exclude"] = True
                elif case == "profile": p["metadata"]["profile"]["_backend"] = "other"
                elif case == "crop": p["assets"][0]["crop"]["pixel_box"][1] += 10
                elif case == "bool_index": p["assets"][0]["index"] = False
                else: p["assets"][0]["private_extra"] = "not accepted"
            fixture.mutate(mutate)
            with self.assertRaises(figures.FigureSourceError):
                fixture.validate()

    def test_deleted_sidecar_and_partial_or_changed_status_marker_fail_closed(self):
        for case in ("delete", "partial", "path", "sha", "evidence_only", "null", "dangling"):
            fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
            fixture.create()
            fixture.status()
            if case in ("delete", "evidence_only", "dangling"):
                (fixture.report / figures.SIDECAR).unlink()
                if case == "evidence_only": (fixture.report / "status.json").unlink()
                if case == "dangling":
                    (fixture.report / figures.SIDECAR).symlink_to("missing.json")
                    (fixture.report / "status.json").unlink()
            else:
                path = fixture.report / "status.json"
                value = json.loads(path.read_bytes())
                if case == "partial": del value["source_figure_map_sha256"]
                elif case == "path": value["source_figure_map"] = "other.json"
                elif case == "null": value.update(source_figure_map=None, source_figure_map_sha256=None)
                else: value["source_figure_map_sha256"] = True
                path.write_text(json.dumps(value))
            with self.assertRaises(figures.FigureSourceError):
                fixture.validate()

    def test_duplicate_json_keys_and_symlink_source_image_rejected(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
        middle = fixture.raw / "middle.json"
        data = middle.read_text()
        middle.write_text(data.replace('"_backend": "hybrid"', '"_backend": "hybrid", "_backend": "hybrid"'))
        with self.assertRaises(figures.FigureSourceError): fixture.create()
        fixture.write_metadata()
        image = fixture.raw / "images/image-0.jpg"
        existing = image.read_bytes()
        outside = fixture.root / "outside.jpg"
        outside.write_bytes(existing)
        image.unlink()
        image.symlink_to(outside)
        with self.assertRaises(figures.FigureSourceError): fixture.create()

    def test_png_dimensions_are_bounded_before_decode(self):
        fixture = self.fixture(visuals=[visual(0, [35, 100, 180, 260])])
        fixture.create()
        value = fixture.proof()
        carrier = fixture.report / value["pages"][0]["path"]
        data = bytearray(carrier.read_bytes())
        data[16:24] = (100000).to_bytes(4, "big") * 2
        carrier.write_bytes(data)
        with self.assertRaises(figures.FigureSourceError): fixture.validate()

    def test_native_pdf_diagnostics_suppressed_and_switches_restored_on_success_and_failure(self):
        program = r'''
import sys, tempfile
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, sys.argv[1])
import fitz
import mineru_figure_sources as f
from test_mineru_figure_sources import Fixture, digest, visual
for desired in (True, False):
 for failure in (False, True):
  with tempfile.TemporaryDirectory() as tmp:
   fixture = Fixture(Path(tmp), visuals=[visual(0,[35,100,180,260])])
   with fitz.open(fixture.original) as doc:
    xref=doc[0].get_contents()[0]
    doc.update_stream(xref,doc.xref_stream(xref)+b'\nq PRIVATE_SYNTHETIC_OPERATOR Q\n')
    data=doc.tobytes()
   fixture.original.write_bytes(data)
   (fixture.raw/'source.pdf').write_bytes(data)
   fixture.original_sha=digest(data)
   fitz.TOOLS.mupdf_display_errors(desired)
   fitz.TOOLS.mupdf_display_warnings(desired)
   render=f._render
   def fail_after_render(page):
    render(page)
    raise RuntimeError('PRIVATE_SYNTHETIC_OPERATOR')
   try:
    if failure:
     with patch.object(f,'_render',side_effect=fail_after_render): fixture.create()
    else: fixture.create()
    assert not failure
   except f.FigureSourceError as exc:
    assert failure and exc.category=='figure_metadata_invalid'
   assert fitz.TOOLS.mupdf_display_errors() is desired
   assert fitz.TOOLS.mupdf_display_warnings() is desired
print('native_diagnostics_suppressed')
'''
        result = subprocess.run([sys.executable, "-B", "-c", program, str(Path(figures.__file__).parent)],
                                capture_output=True, timeout=60, check=False)
        self.assertEqual(result.returncode, 0, "Native PDF diagnostic regression failed")
        self.assertNotIn(b"PRIVATE_SYNTHETIC_OPERATOR", result.stdout)
        self.assertNotIn(b"PRIVATE_SYNTHETIC_OPERATOR", result.stderr)
        self.assertIn(b"native_diagnostics_suppressed", result.stdout)

    def test_empty_provider_table_is_audited_without_inventing_image(self):
        content, parent = visual(0, [35, 100, 180, 260])
        content["img_path"] = ""
        content.pop("table_body")
        parent["blocks"][0]["lines"] = []
        parent["blocks"][0]["lines_deleted"] = True
        fixture = self.fixture(visuals=[(content, parent)])
        fixture.create()
        self.assertEqual(fixture.proof()["decisions"][0]["reason"], "no_provider_image")
        self.assertEqual(fixture.validate(), {})


if __name__ == "__main__":
    unittest.main()
