import assert from 'node:assert/strict';
import test from 'node:test';
import pdfLib from '../site_src/assets/vendor/research-pdf/pdf-lib-1.17.1.min.js';
import {createExternalPreviewPdf} from '../../workers/portal-suite-worker/src/external-preview-pdf.mjs';
const {PDFDocument, PDFName, PDFString, PDFDict, PDFRawStream, decodePDFRawStream, degrees} = pdfLib;
const name = PDFName.of;
function allObjectsText(doc) {
  return doc.context.enumerateIndirectObjects().map(([, obj]) => {
    if (obj instanceof PDFRawStream) return `${obj.dict.toString()} ${new TextDecoder().decode(decodePDFRawStream(obj).decode())}`;
    return obj.toString();
  }).join('\n');
}
async function source() {
  const doc = await PDFDocument.create();
  const first = doc.addPage([360, 500]);
  const other = doc.addPage([600, 700]);
  first.node.set(name('Contents'), doc.context.register(doc.context.stream('FIRST_PAGE_CONTENT')));
  other.node.set(name('Contents'), doc.context.register(doc.context.stream('PRIVATE_SECOND_PAGE_CONTENT')));
  return {doc, first, other, ctx:doc.context};
}
test('copies only first-page drawing objects, stripping article beads, annotations, actions, attachments and unknown page associations before copy', async () => {
  const {doc,first,other,ctx} = await source();
  const embedded = ctx.register(ctx.flateStream('PRIVATE_ATTACHMENT_CONTENT', {Type:'EmbeddedFile'}));
  const file = ctx.register(ctx.obj({Type:'Filespec', F:PDFString.of('PRIVATE_ATTACHMENT.txt'), EF:{F:embedded}}));
  const js = ctx.obj({S:'JavaScript', JS:PDFString.of('PRIVATE_JAVASCRIPT')});
  first.node.set(name('Annots'),ctx.obj([{Type:'Annot', Subtype:'Link', Dest:[other.ref,'Fit']},{Type:'Annot', Subtype:'FileAttachment',FS:file}]));
  first.node.set(name('B'),ctx.obj([ctx.register(ctx.obj({P:other.ref}))]));
  first.node.set(name('AA'),ctx.obj({O:js}));
  first.node.set(name('ArbitraryCustomAssociation'),other.ref);
  first.node.set(name('Resources'),ctx.obj({XObject:{Cover:ctx.register(ctx.stream('VISIBLE_FORM',{Type:'XObject',Subtype:'Form',BBox:[0,0,10,10],Resources:{},AF:[file],AA:{O:js},Metadata:ctx.register(ctx.stream('PRIVATE_METADATA')),HiddenPage:other.ref}))}}));
  const result = await createExternalPreviewPdf(await doc.save(),2);
  const output = await PDFDocument.load(result);
  const text = allObjectsText(output);
  assert.equal(output.getPageCount(),1);
  assert.equal(output.context.enumerateIndirectObjects().filter(([,obj])=>obj instanceof PDFDict && obj.get(name('Type'))===name('Page')).length,1);
  assert.match(text,/FIRST_PAGE_CONTENT/);
  assert.match(text,/VISIBLE_FORM/);
  assert.doesNotMatch(text,/PRIVATE_|\/Annots\b|\/Filespec\b|\/EmbeddedFile\b|\/JavaScript\b/);
});
test('retains inherited resources, page boxes, rotation and arbitrary rendering resource or Type 3 glyph names',async()=>{
  const {doc,first,ctx}=await source();
  first.setRotation(degrees(90)); first.setCropBox(5,10,300,400);
  const font=ctx.obj({Type:'Font',Subtype:'Type3',FontBBox:[0,0,10,10],FontMatrix:[1,0,0,1,0,0],CharProcs:{A:ctx.register(ctx.stream('VISIBLE_GLYPH_A')),B:ctx.register(ctx.stream('VISIBLE_GLYPH_B'))}});
  const resources=ctx.obj({Font:{A:ctx.register(font)}, XObject:{B:ctx.register(ctx.stream('VISIBLE_FORM_B',{Type:'XObject',Subtype:'Form',BBox:[0,0,10,10],Resources:{}}))}});
  const parent=first.node.lookup(name('Parent'));
  parent.set(name('Resources'),resources);
  parent.set(name('Rotate'),first.node.get(name('Rotate')));
  first.node.delete(name('Resources'));first.node.delete(name('Rotate'));
  const output=await PDFDocument.load(await createExternalPreviewPdf(await doc.save(),2));
  assert.deepEqual(output.getPage(0).getSize(),{width:360,height:500});
  assert.deepEqual(output.getPage(0).getCropBox(),{x:5,y:10,width:300,height:400});
  assert.equal(output.getPage(0).getRotation().angle,90);
  assert.match(allObjectsText(output),/VISIBLE_GLYPH_A/);
  assert.match(allObjectsText(output),/VISIBLE_GLYPH_B/);
  assert.match(allObjectsText(output),/VISIBLE_FORM_B/);
});
test('rejects invalid page metadata and invalid or oversized documents',async()=>{
 const {doc}=await source();const bytes=await doc.save();
 for(const count of [0,-1,1,3,2001,NaN,2.5,'2']) await assert.rejects(createExternalPreviewPdf(bytes,count));
 await assert.rejects(createExternalPreviewPdf(new TextEncoder().encode('<html>not pdf</html>'),2));
 const oversized=new Uint8Array(25*1024*1024+1);oversized.set(new TextEncoder().encode('%PDF-'));
 await assert.rejects(createExternalPreviewPdf(oversized,2));
});
