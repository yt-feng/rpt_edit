import pdfLib from "../../../portal_suite/site_src/assets/vendor/research-pdf/pdf-lib-1.17.1.min.js";

const { PDFDocument, PDFArray, PDFDict, PDFName, PDFStream } = pdfLib;
const PAGE_RENDER_KEYS = new Set([
  "Type", "Parent", "Resources", "Contents", "MediaBox", "CropBox", "BleedBox",
  "TrimBox", "ArtBox", "Rotate", "UserUnit", "Group",
]);
const NON_RENDER_KEYS = new Set([
  "Annots", "AA", "A", "AF", "Names", "OpenAction", "Metadata", "PieceInfo",
  "PresSteps", "Thumb", "B", "StructTreeRoot", "AcroForm", "Outlines", "Threads",
  "EmbeddedFiles", "JavaScript", "JS", "XFA", "Parent",
]);
const NON_RENDER_TYPES = new Set(["Page", "Pages", "Catalog", "Filespec", "EmbeddedFile", "Action", "Annot", "Sig"]);
const NON_RENDER_ACTIONS = new Set([
  "JavaScript", "Launch", "GoTo", "GoToR", "GoToE", "SubmitForm", "ImportData",
  "URI", "Named", "ResetForm", "SetOCGState", "Rendition", "Thread", "Hide",
]);
const RESOURCE_MAP_KEYS = new Set(["Font", "XObject", "ExtGState", "ColorSpace", "Pattern", "Shading", "Properties", "CharProcs"]);

function pdfName(value) {
  return value instanceof PDFName ? value.decodeText() : "";
}

// Resources can themselves contain associated files, metadata, or references
// back to pages. Remove those edges before copying: removing them afterwards
// leaves the already copied objects in the serialized document.
function prunePreviewResources(source, first) {
  const visited = new Set();
  const pending = [];
  const keep = (value, namedEntries = false) => {
    const object = source.context.lookup(value);
    const dict = object instanceof PDFStream ? object.dict : object;
    if (dict instanceof PDFDict
      && (NON_RENDER_TYPES.has(pdfName(dict.get(PDFName.of("Type"))))
        || NON_RENDER_ACTIONS.has(pdfName(dict.get(PDFName.of("S")))))) return false;
    if ((object instanceof PDFArray || dict instanceof PDFDict) && !visited.has(object)) {
      visited.add(object);
      if (visited.size > 50000) throw new Error("Preview PDF is too complex.");
      pending.push({ object, namedEntries });
    }
    return true;
  };
  // copyPages materializes these inherited fields. Materialize them first so
  // sanitization also visits resources inherited through the page tree.
  for (const key of ["Resources", "MediaBox", "CropBox", "Rotate"]) {
    const name = PDFName.of(key);
    const inherited = first.node.getInheritableAttribute(name);
    if (!first.node.has(name) && inherited) first.node.set(name, inherited);
  }
  for (const [key, value] of first.node.entries()) {
    if (key.decodeText() !== "Parent" && !keep(value)) first.node.delete(key);
  }
  while (pending.length) {
    const { object, namedEntries } = pending.pop();
    if (object instanceof PDFArray) {
      for (let i = object.size() - 1; i >= 0; i -= 1) {
        if (!keep(object.get(i))) object.remove(i);
      }
    } else {
      const dict = object instanceof PDFStream ? object.dict : object;
      for (const [key, value] of dict.entries()) {
        const name = key.decodeText();
        // Resource names and Type 3 glyph names are arbitrary: a visible glyph
        // called "A" or an XObject called "B" must not be treated as an action.
        if ((!namedEntries && NON_RENDER_KEYS.has(name))
          || !keep(value, !namedEntries && RESOURCE_MAP_KEYS.has(name))) dict.delete(key);
      }
    }
  }
}

// The browser must never receive the source document for a one-page preview.
export async function createExternalPreviewPdf(bytes, expectedPages) {
  if (!Number.isSafeInteger(expectedPages) || expectedPages < 1 || expectedPages > 2000
    || bytes.length > 25 * 1024 * 1024
    || String.fromCharCode(...bytes.subarray(0, 5)) !== "%PDF-") {
    throw new Error("Preview PDF is unavailable.");
  }
  const source = await PDFDocument.load(bytes, { updateMetadata: false, throwOnInvalidObject: true });
  if (source.isEncrypted || source.getPageCount() !== expectedPages) {
    throw new Error("Preview PDF page count is invalid.");
  }
  const first = source.getPage(0);
  // Link destinations, attachments and page actions can reference other pages.
  // Keep only the first page's drawing state before recursively copying it.
  for (const key of first.node.keys()) {
    if (!PAGE_RENDER_KEYS.has(key.decodeText())) first.node.delete(key);
  }
  prunePreviewResources(source, first);
  const preview = await PDFDocument.create();
  const [page] = await preview.copyPages(source, [0]);
  preview.addPage(page);
  preview.setTitle("Report first-page preview");
  preview.setSubject("One-page preview, not the complete report");
  const copiedPages = preview.context.enumerateIndirectObjects().filter(([, object]) =>
    object instanceof PDFDict && pdfName(object.get(PDFName.of("Type"))) === "Page");
  if (copiedPages.length !== 1) throw new Error("Preview PDF page isolation failed.");
  const result = await preview.save();
  if (result.length > 10 * 1024 * 1024) throw new Error("Preview PDF is too large.");
  return result;
}
