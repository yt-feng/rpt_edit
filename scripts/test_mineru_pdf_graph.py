"""Real PDFium round trips and adversarial hidden drawing-graph changes."""
import io
import json
import pathlib
import subprocess
import sys
import unittest
from unittest.mock import patch

import fitz
from PIL import Image
import pypdfium2 as pdfium

import mineru_pdf_graph as graph
from mineru_pdf_graph import (PdfGraphError, bind_pdf_render_graph,
                             parse_pdf_value, validate_graph_receipt)


def rewrite(raw):
    source = pdfium.PdfDocument(raw)
    target = pdfium.PdfDocument.new()
    try:
        target.import_pages(source, list(range(len(source))))
        output = io.BytesIO(); target.save(output)
        return output.getvalue()
    finally:
        target.close(); source.close()


def fixture(pages=1, *, images=True, same_names=False):
    with fitz.open() as document:
        one = document.add_ocg("PRIVATE SAME" if same_names else "PRIVATE FIRST", on=False)
        two = document.add_ocg("PRIVATE SAME" if same_names else "PRIVATE SECOND", on=False)
        encoded = []
        for color in ((200, 20, 30), (30, 40, 200)):
            output = io.BytesIO(); Image.new("RGB", (12, 13), color).save(output, "JPEG")
            encoded.append(output.getvalue())
        for index in range(pages):
            page = document.new_page(width=200, height=200)
            page.insert_text((10, 25), "PRIVATE HIDDEN TEXT", oc=one)
            page.insert_text((10, 45), "SECOND HIDDEN TEXT", oc=two)
            if images:
                page.insert_image(fitz.Rect(10, 60, 80, 140), stream=encoded[0], oc=one)
                page.insert_image(fitz.Rect(110, 60, 180, 140), stream=encoded[1], oc=two)
        return document.tobytes(no_new_id=True)


def changed(raw, operation):
    with fitz.open(stream=raw, filetype="pdf") as document:
        operation(document)
        return document.tobytes(no_new_id=True)


def link_fixture():
    def forward_link(document):
        link = document.get_new_xref()
        document.update_object(link, f"<</Type/Annot/Subtype/Link/Rect[10 10 40 30]/Border[0 0 0]"
                               f"/Dest[{document.page_xref(1)} 0 R /XYZ 10 180 0]>>")
        document.xref_set_key(document.page_xref(0), "Annots", f"[{link} 0 R]")
    return changed(fixture(pages=2), forward_link)


def link_reference(document):
    return parse_pdf_value(document.xref_get_key(document.page_xref(0), "Annots")[1])[0].idnum


def binding(original, embedded):
    with fitz.open(stream=original, filetype="pdf") as left, fitz.open(stream=embedded, filetype="pdf") as right:
        return bind_pdf_render_graph(left, right)


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.original = fixture()
        self.embedded = rewrite(self.original)

    def test_real_42_page_pdfium_round_trip_binds_every_page_and_shared_ocg(self):
        original = fixture(42)
        result = binding(original, rewrite(original))
        self.assertEqual(result.receipt["pages"], 42)
        self.assertEqual(result.receipt["ocg_count"], 2)
        self.assertGreater(result.receipt["streams"], 84)
        self.assertTrue(all(a[1] == b[1] == 0 for a, b in result.mapping.items()))
        self.assertEqual(validate_graph_receipt(result.receipt), result.receipt)
        for private in ("PRIVATE", "HIDDEN", "FIRST", "SECOND", "Helvetica"):
            self.assertNotIn(private, json.dumps(result.receipt))

    def test_same_name_ocgs_are_matched_by_graph_position(self):
        original = fixture(same_names=True)
        result = binding(original, rewrite(original))
        self.assertEqual(len(result.ocg_mapping), 2)
        self.assertEqual(len(set(result.ocg_mapping.values())), 2)

    def test_dictionary_order_and_flate_transport_are_semantically_normalized(self):
        def uncompressed(document):
            for stream in document[0].get_contents():
                document.update_stream(stream, document.xref_stream(stream), compress=False)
        original = changed(self.original, uncompressed)
        embedded = rewrite(original)
        with fitz.open(stream=original, filetype="pdf") as a, fitz.open(stream=embedded, filetype="pdf") as e:
            self.assertNotEqual(a.xref_get_key(a[0].get_contents()[0], "Filter"),
                                e.xref_get_key(e[0].get_contents()[0], "Filter"))
            result = bind_pdf_render_graph(a, e)
        self.assertEqual(result.receipt["ocg_count"], 2)

    def test_hidden_text_stream_change_is_rejected(self):
        def operation(document):
            stream = document[0].get_contents()[0]
            document.update_stream(stream, document.xref_stream(stream).replace(b"20", b"21", 1))
        with self.assertRaises(PdfGraphError) as caught:
            binding(self.original, changed(self.embedded, operation))
        self.assertEqual(caught.exception.category, "pdf_graph_stream_content_mismatch")
        self.assertRegex(caught.exception.path_sha256, "^[0-9a-f]{64}$")
        self.assertNotIn("PRIVATE", str(caught.exception))

    def test_hidden_image_bytes_change_is_rejected_without_image_decode(self):
        def operation(document):
            image = document[0].get_images()[0][0]
            raw = bytearray(document.xref_stream_raw(image)); raw[-10] ^= 1
            document.update_stream(image, bytes(raw), compress=False)
            document.xref_set_key(image, "Filter", "/DCTDecode")
        changed_embedded = changed(self.embedded, operation)
        with patch.object(fitz.Document, "xref_stream", side_effect=AssertionError("No decoded image stream")), \
             patch("fitz.Pixmap", side_effect=AssertionError("No image decode")):
            with self.assertRaisesRegex(PdfGraphError, "pdf_graph_stream_content_mismatch"):
                binding(self.original, changed_embedded)

    def test_two_off_layer_image_oc_references_cannot_be_swapped(self):
        def operation(document):
            images = document[0].get_images()
            first, second = images[0][0], images[1][0]
            a, b = document.xref_get_key(first, "OC")[1], document.xref_get_key(second, "OC")[1]
            document.xref_set_key(first, "OC", b); document.xref_set_key(second, "OC", a)
        with self.assertRaises(PdfGraphError):
            binding(self.original, changed(self.embedded, operation))

    def test_extra_reachable_resource_is_rejected(self):
        def operation(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            document.xref_set_key(resources, "PRIVATE_EXTRA_KEY", "42")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_dictionary_keys_mismatch"):
            binding(self.original, changed(self.embedded, operation))

    def test_dictionary_failure_details_expose_only_known_pdf_keys(self):
        def operation(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            document.xref_set_key(resources, "DL", "123")
            document.xref_set_key(resources, "CONFIDENTIAL_RESOURCE", "(PRIVATE_SOURCE_TEXT)")
            document.xref_set_key(resources, "CONFIDENTIAL_NAME", "/PRIVATE_NAME_VALUE")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_dictionary_keys_mismatch") as caught:
            binding(self.original, changed(self.embedded, operation))
        details = caught.exception.sanitized_details
        self.assertEqual((details["page_index"], details["last_standard_key"]), (0, "/Resources"))
        self.assertEqual(details["path_sha256"], caught.exception.path_sha256)
        difference = details["dictionary_difference"]
        self.assertEqual(difference["embedded_only"]["known"], ["/DL"])
        self.assertEqual(difference["embedded_only"]["unknown_count"], 2)
        dl = next(value for value in difference["values"] if value.get("key") == "/DL")
        self.assertEqual(dl["original"]["type"], "missing")
        self.assertEqual(dl["embedded"]["type"], "number")
        self.assertFalse(dl["embedded"]["empty"])
        self.assertRegex(dl["embedded"]["sha256"], "^[0-9a-f]{64}$")
        serialized = json.dumps(details)
        for private in ("CONFIDENTIAL_RESOURCE", "CONFIDENTIAL_NAME", "PRIVATE_SOURCE_TEXT", "PRIVATE_NAME_VALUE", "PRIVATE FIRST"):
            self.assertNotIn(private, serialized)

    def test_scalar_failure_details_never_expose_pdf_name_or_string_values(self):
        def operation(document):
            group = next(x for x in range(1, document.xref_length()) if document.xref_get_key(x, "Type") == ("name", "/OCG"))
            document.xref_set_key(group, "Name", "(CHANGED_SECRET_NAME)")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_scalar_mismatch") as caught:
            binding(self.original, changed(self.embedded, operation))
        details = caught.exception.sanitized_details
        self.assertEqual(details["last_standard_key"], "/Name")
        self.assertEqual(details["original"]["type"], "string")
        self.assertNotEqual(details["original"]["sha256"], details["embedded"]["sha256"])
        for private in ("CHANGED_SECRET_NAME", "PRIVATE FIRST", "PRIVATE SECOND"):
            self.assertNotIn(private, json.dumps(details))

    def test_diagnostic_unknown_keys_and_value_hash_work_are_bounded(self):
        private = parse_pdf_value("<<" + " ".join(f"/SECRET_RESOURCE_{i}(SECRET_VALUE_{i})" for i in range(200)) + ">>")
        with patch("mineru_pdf_graph.MAX_DIAGNOSTIC_NODES", 1):
            details = graph._sanitized_details(private, parse_pdf_value("<<>>"),
                ("page", 3, "/Resources", "key", "/SECRET_RESOURCE_199"), "a" * 64)
        self.assertEqual(details["original"]["hash_status"], "bounded")
        self.assertEqual(details["last_standard_key"], "/Resources")
        difference = details["dictionary_difference"]
        self.assertEqual(len(difference["original_only"]["unknown_sha256"]), graph.MAX_DIAGNOSTIC_UNKNOWN_KEYS)
        self.assertEqual(len(difference["values"]), graph.MAX_DIAGNOSTIC_KEYS)
        self.assertTrue(difference["values_truncated"])
        self.assertNotIn("SECRET_RESOURCE", json.dumps(details))
        self.assertNotIn("SECRET_VALUE", json.dumps(details))

    def test_extra_unreferenced_ocg_is_rejected_by_inventory(self):
        def operation(document):
            obj = document.get_new_xref(); document.update_object(obj, "<</Type/OCG/Name(PRIVATE EXTRA)>>")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_ocg_inventory_mismatch"):
            binding(self.original, changed(self.embedded, operation))

    def test_one_original_alias_cannot_split_into_two_provider_objects(self):
        def add_alias(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            group = next(x for x in range(1, document.xref_length()) if document.xref_get_key(x, "Type") == ("name", "/OCG"))
            document.xref_set_key(resources, "PRIVATE_ALIAS", f"{group} 0 R")
        original = changed(self.original, add_alias)
        embedded = rewrite(original)
        def split(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            group = int(document.xref_get_key(resources, "PRIVATE_ALIAS")[1].split()[0])
            new = document.get_new_xref(); document.update_object(new, document.xref_object(group))
            document.xref_set_key(resources, "PRIVATE_ALIAS", f"{new} 0 R")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_alias_mismatch"):
            binding(original, changed(embedded, split))

    def test_two_original_objects_cannot_merge_into_one_provider_alias(self):
        original = fixture(same_names=True)
        def merge(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            first = document.xref_get_key(resources, "Properties/MC0")[1]
            document.xref_set_key(resources, "Properties/MC1", first)
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_alias_mismatch"):
            binding(original, changed(rewrite(original), merge))

    def test_image_codec_parameters_are_never_ignored(self):
        def parameter(document):
            image = document[0].get_images()[0][0]
            document.xref_set_key(image, "DecodeParms", "<</ColorTransform 0>>")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_dictionary_keys_mismatch"):
            binding(self.original, changed(self.embedded, parameter))

    def test_real_png_empty_decode_parameters_survive_pdfium_flate_transport(self):
        def png(document):
            output = io.BytesIO(); Image.new("RGB", (8, 8), (200, 40, 30)).save(output, "PNG")
            document[0].insert_image(fitz.Rect(20, 150, 40, 170), stream=output.getvalue())
        original = changed(fixture(images=False), png)
        with fitz.open(stream=original, filetype="pdf") as document:
            image = document[0].get_images()[0][0]
            self.assertEqual(document.xref_get_key(image, "DecodeParms"), ("dict", "<<>>"))
        result = binding(original, rewrite(original))
        self.assertEqual(result.receipt["ocg_count"], 2)

    def test_fractional_cropbox_uses_exact_render_geometry_not_raw_number_precision(self):
        def crop(document):
            document.xref_set_key(document[0].xref, "CropBox", "[3.80676007270813 2.142857193946838 197.19047546386719 196.22857666015625]")
        original = changed(self.original, crop)
        result = binding(original, rewrite(original))
        self.assertEqual(result.receipt["pages"], 1)

    def test_geometry_change_is_rejected_on_unselected_pages_too(self):
        original = fixture(pages=2)
        embedded = changed(rewrite(original), lambda document: document[1].set_rotation(90))
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_page_geometry_mismatch"):
            binding(original, embedded)

    def test_form_matrix_numbers_remain_strict(self):
        def form(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            obj = document.get_new_xref()
            document.update_object(obj, "<</Type/XObject/Subtype/Form/BBox[0 0 10 10]/Matrix[1 0 0 1 3.80676007270813 0]>>")
            document.update_stream(obj, b"q Q")
            document.xref_set_key(resources, "XObject/PRIVATE_FORM", f"{obj} 0 R")
        original = changed(self.original, form)
        def alter(document):
            xref = int(document.xref_get_key(document[0].xref, "Resources/XObject/PRIVATE_FORM")[1].split()[0])
            document.xref_set_key(xref, "Matrix", "[1 0 0 1 3.8068601 0]")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_scalar_mismatch"):
            binding(original, changed(original, alter))

    def test_reference_cycle_is_compared_without_unbounded_recursion(self):
        def cycle(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            obj = document.get_new_xref(); document.update_object(obj, f"<</Cycle {obj} 0 R>>")
            document.xref_set_key(resources, "PRIVATE_CYCLE", f"{obj} 0 R")
        original = changed(self.original, cycle)
        # Self-copy preserves arbitrary private resource keys exactly.
        result = binding(original, original)
        self.assertEqual(result.receipt["ocg_count"], 2)

    def test_inherited_resources_are_compared_to_pdfium_materialized_resources(self):
        def inherit(document):
            page = document[0]
            parent = int(document.xref_get_key(page.xref, "Parent")[1].split()[0])
            resources = document.xref_get_key(page.xref, "Resources")[1]
            document.xref_set_key(parent, "Resources", resources)
            document.xref_set_key(page.xref, "Resources", "null")
        original = changed(self.original, inherit)
        # Keep PDF syntax absence rather than explicit null for inherited keys.
        def remove_null(document):
            xref = document[0].xref
            document.update_object(xref, document.xref_object(xref).replace("/Resources null", ""))
        original = changed(original, remove_null)
        result = binding(original, rewrite(original))
        self.assertEqual(result.receipt["ocg_count"], 2)

    def test_annotation_page_back_reference_does_not_traverse_catalog(self):
        def annotation(document):
            document[0].add_rect_annot(fitz.Rect(10, 10, 20, 20))
        original = changed(self.original, annotation)
        result = binding(original, rewrite(original))
        self.assertEqual(result.receipt["pages"], 1)

    def test_pdfium_forward_link_destination_is_ignored_only_for_static_annotation_binding(self):
        original = link_fixture(); embedded = rewrite(original)
        with fitz.open(stream=original, filetype="pdf") as a, fitz.open(stream=embedded, filetype="pdf") as e:
            self.assertEqual(a.xref_get_key(link_reference(a), "Dest")[0], "array")
            self.assertEqual(e.xref_get_key(link_reference(e), "Dest")[0], "null")
        result = binding(original, embedded)
        self.assertEqual(result.receipt["pages"], 2)
        self.assertEqual(result.receipt["ocg_count"], 2)

    def test_link_border_appearance_and_optional_content_changes_are_rejected(self):
        original = link_fixture(); embedded = rewrite(original)
        def alter(document, kind):
            link = link_reference(document)
            if kind == "border":
                document.xref_set_key(link, "Border", "[0 0 1]")
            elif kind == "appearance":
                form = document.get_new_xref()
                document.update_object(form, "<</Type/XObject/Subtype/Form/BBox[0 0 30 20]>>")
                document.update_stream(form, b"q 1 0 0 rg 0 0 30 20 re f Q")
                document.xref_set_key(link, "AP", f"<</N {form} 0 R>>")
            elif kind == "oc":
                group = next(x for x in range(1, document.xref_length()) if document.xref_get_key(x, "Type") == ("name", "/OCG"))
                document.xref_set_key(link, "OC", f"{group} 0 R")
            else:
                document.xref_set_key(link, "Rect", "[10 10 45 35]")
        for kind in ("border", "appearance", "oc", "rect"):
            with self.subTest(kind=kind), self.assertRaises(PdfGraphError):
                binding(original, changed(embedded, lambda doc: alter(doc, kind)))

    def test_nested_link_dictionary_has_no_destination_exception(self):
        def insert(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            document.xref_set_key(resources, "PRIVATE_NESTED", f"<</Subtype/Link/Dest[{document.page_xref(0)} 0 R /Fit]>>")
        original = changed(self.original, insert)
        def drop(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            document.xref_set_key(resources, "PRIVATE_NESTED", "<</Subtype/Link>>")
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_dictionary_keys_mismatch"):
            binding(original, changed(original, drop))

    def test_malformed_or_action_conflicting_link_destination_is_not_ignored(self):
        original = link_fixture()
        for value in ("[42 /XYZ 10 180 0]", "[42 0 R /Unknown 10]", "<< /PRIVATE(SECRET) >>"):
            with self.subTest(case=len(value)):
                invalid = changed(original, lambda doc: doc.xref_set_key(link_reference(doc), "Dest", value))
                with self.assertRaisesRegex(PdfGraphError, "pdf_graph_link_destination_invalid"):
                    binding(invalid, invalid)
        conflicted = changed(original, lambda doc: doc.xref_set_key(link_reference(doc), "A", "<</S/GoTo/D(named)>>"))
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_link_destination_invalid"):
            binding(conflicted, conflicted)

    def test_shared_link_object_in_resources_still_gets_full_non_annotation_comparison(self):
        def alias(document):
            resources = int(document.xref_get_key(document[0].xref, "Resources")[1].split()[0])
            document.xref_set_key(resources, "PRIVATE_ALIAS", f"{link_reference(document)} 0 R")
        original = changed(link_fixture(), alias)
        embedded = rewrite(original)
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_dictionary_keys_mismatch"):
            binding(original, embedded)

    def test_dynamic_forms_are_not_admitted(self):
        original = changed(self.original, lambda document: document.xref_set_key(document.pdf_catalog(), "AcroForm", "<<>>"))
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_dynamic_document_unsupported"):
            binding(original, original)

    def test_flate_expansion_is_bounded(self):
        def large_compressed_stream(document):
            document.update_stream(document[0].get_contents()[0], b"q\n" + b" " * 2048 + b"Q\n", compress=True)
        original = changed(fixture(images=False), large_compressed_stream)
        with fitz.open(stream=original, filetype="pdf") as document:
            self.assertLess(len(document.xref_stream_raw(document[0].get_contents()[0])), 128)
        with patch("mineru_pdf_graph.MAX_STREAM_BYTES", 128):
            with self.assertRaisesRegex(PdfGraphError, "pdf_graph_stream_bytes_bound"):
                binding(original, original)

    def test_parser_preserves_reference_generation_and_rejects_invalid_text_privately(self):
        value = parse_pdf_value("<</A 9 2 R>>").raw_get("/A")
        self.assertEqual((value.idnum, value.generation), (9, 2))
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_parse_failed"):
            parse_pdf_value("<</PRIVATE(SECRET) /B BROKEN>>")

    def test_receipt_rejects_unknown_private_values_and_invalid_counts(self):
        receipt = binding(self.original, self.embedded).receipt
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_receipt_invalid"):
            validate_graph_receipt({**receipt, "private": "SECRET"})
        with self.assertRaisesRegex(PdfGraphError, "pdf_graph_receipt_invalid"):
            validate_graph_receipt({**receipt, "streams": receipt["objects"] + 1})

    def test_receipt_validator_import_needs_no_third_party_packages(self):
        script = "import mineru_pdf_graph, mineru_pdf_oc, sys; assert 'pypdf' not in sys.modules; assert 'fitz' not in sys.modules"
        result = subprocess.run([sys.executable, "-S", "-c", script],
            cwd=pathlib.Path(__file__).parent, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
