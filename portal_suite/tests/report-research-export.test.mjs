import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const source = await readFile(path.join(root, "portal_suite/site_src/assets/report-research-export.js"), "utf8");
const jpeg = Buffer.from(
  "/9j/4AAQSkZJRgABAgAAAQABAAD//gAQTGF2YzYyLjI4LjEwMQD/2wBDAAgEBAQEBAUFBQUFBQYGBgYGBgYGBgYGBgYGBwcHCAgHBwcGBgcHCAgICAkJCQgICAgJCQoKCgwMCwsODg4RERT/xABLAAEBAAAAAAAAAAAAAAAAAAAABwEBAAAAAAAAAAAAAAAAAAAAABABAAAAAAAAAAAAAAAAAAAAABEBAAAAAAAAAAAAAAAAAAAAAP/AABEIABAAEAMBIgACEQADEQD/2gAMAwEAAhEDEQA/AL+AD//Z",
  "base64",
);

function loadExporter() {
  const window = {};
  vm.runInNewContext(source, {
    Blob,
    Date,
    Intl,
    Promise,
    TextEncoder,
    Uint8Array,
    URL,
    btoa,
    console,
    setTimeout,
    clearTimeout,
    window,
  }, { filename: "report-research-export.js" });
  return window.PortalReportResearchExport;
}

function zipEntries(bytes) {
  const decoder = new TextDecoder();
  const entries = new Map();
  let offset = 0;
  while (offset + 4 <= bytes.length) {
    const view = new DataView(bytes.buffer, bytes.byteOffset + offset, bytes.byteLength - offset);
    const signature = view.getUint32(0, true);
    if (signature !== 0x04034B50) break;
    const compressedSize = view.getUint32(18, true);
    const nameLength = view.getUint16(26, true);
    const extraLength = view.getUint16(28, true);
    const nameStart = offset + 30;
    const dataStart = nameStart + nameLength + extraLength;
    const name = decoder.decode(bytes.subarray(nameStart, nameStart + nameLength));
    entries.set(name, bytes.subarray(dataStart, dataStart + compressedSize));
    offset = dataStart + compressedSize;
  }
  return entries;
}

function fixture() {
  return {
    question: "AI 数据中心 <电力> 与资本开支？",
    question_hash: "fixture-hash-01",
    response: {
      mode: "research",
      research_title: "AI 数据中心：电力与资本开支研究",
      research_scope: ["最近半年", "投行报告 & Charts"],
      generated_at: "2026-08-30T12:00:00Z",
      executive_summary: "多份报告显示 <供电> 是主要约束。",
      summary_source_ids: ["report-1"],
      findings: [{ title: "电力约束", summary: "并网与供电容量决定扩张速度。", source_ids: ["report-1"] }],
      data_points: [{ label: "资本开支", value: "+25%", context: "2026E", source_ids: ["report-1"] }],
      sources: [
        { id: "report-1", title: "摩根大通 AI 电力报告", institution: "摩根大通", industry: "科技" },
        { id: "report-2", title: "高盛电网报告", institution: "高盛", industry: "公用事业" },
      ],
      charts: [
        { image_id: "a".repeat(64), report_id: "report-1", title: "匹配图表", description: "只属于来源一致的发现", metrics: ["TWh"] },
        { image_id: "b".repeat(64), report_id: "report-2", title: "补充图表", description: "不得硬塞进发现", metrics: ["GW"] },
      ],
      follow_up_questions: ["电网投资由谁承担？"],
    },
  };
}

test("historical excerpts retain their boundary in export data and Word even with old cached scope", async () => {
  const exporter = loadExporter();
  const payload = fixture();
  payload.response.sources[0].partial_excerpt = true;
  const model = exporter.normalizePayload(payload);
  assert.equal(model.sources[0].partial_excerpt, true);
  assert.match(model.research_scope.join(" "), /含 1 份历史正文节选，不代表完整报告正文/u);
  const document = await exporter.buildDocx(payload, { fetch: imageFetch([]) });
  const xml = new TextDecoder().decode(zipEntries(document.bytes).get("word/document.xml"));
  assert.match(xml, /历史正文节选，不代表完整报告正文/u);
});

function imageFetch(log, contentType = "image/jpeg") {
  return async (url) => {
    log.push(url);
    return {
      ok: true,
      headers: { get: (name) => name.toLowerCase() === "content-type" ? contentType : null },
      arrayBuffer: async () => jpeg.buffer.slice(jpeg.byteOffset, jpeg.byteOffset + jpeg.byteLength),
    };
  };
}

test("DOCX export is a real OOXML package with inline charts and canonical source hyperlinks", async () => {
  const exporter = loadExporter();
  const fetches = [];
  const result = await exporter.buildDocx(fixture(), {
    createdAt: new Date("2026-08-30T12:00:00Z"),
    fetch: imageFetch(fetches),
    origin: "https://portal.example",
  });
  assert.equal(result.blob.type, exporter.DOCX_MIME_TYPE);
  assert.equal(result.filename, "KC桌面研究结果_20260830_fixture-hash.docx");
  assert.doesNotMatch(result.filename, /电力|资本/u);
  assert.deepEqual(fetches, [
    `/api/charts/image?id=${"a".repeat(64)}`,
    `/api/charts/image?id=${"b".repeat(64)}`,
  ]);

  const entries = zipEntries(result.bytes);
  for (const name of [
    "[Content_Types].xml", "_rels/.rels", "docProps/core.xml", "word/document.xml",
    "word/_rels/document.xml.rels", "word/styles.xml", "word/numbering.xml",
    "word/header1.xml", "word/footer1.xml", "word/media/image1.jpg", "word/media/image2.jpg",
  ]) assert.ok(entries.has(name), `missing ${name}`);
  const decode = (name) => new TextDecoder().decode(entries.get(name));
  const documentXml = decode("word/document.xml");
  const relationships = decode("word/_rels/document.xml.rels");
  const styles = decode("word/styles.xml");
  assert.match(documentXml, /AI 数据中心：电力与资本开支研究/u);
  assert.match(documentXml, /多份报告显示 &lt;供电&gt; 是主要约束/u);
  assert.match(documentXml, /补充图表证据/u);
  assert.equal((documentXml.match(/<wp:inline\b/gu) || []).length, 2);
  assert.match(documentXml, /w:pgSz w:w="11906" w:h="16838"/u);
  assert.match(documentXml, /w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"/u);
  assert.match(styles, /w:styleId="Normal"[\s\S]*w:spacing w:before="0" w:after="120" w:line="264"/u);
  assert.match(styles, /w:ascii="Arial Unicode MS" w:hAnsi="Arial Unicode MS" w:eastAsia="Arial Unicode MS"/u);
  assert.match(decode("word/numbering.xml"), /w:abstractNumId="0"[\s\S]*w:abstractNumId="1"[\s\S]*w:numId="1"[\s\S]*w:numId="2"/u);
  assert.match(documentXml, /可继续研究[\s\S]*w:numId w:val="2"/u);
  assert.equal((relationships.match(/relationships\/image/gu) || []).length, 2);
  assert.ok((relationships.match(/TargetMode="External"/gu) || []).length >= 4);
  assert.match(relationships, /https:\/\/portal\.example\/report\.html\?id=report-1/u);
  assert.doesNotMatch(relationships, /api\/charts|_report-research|archive_id|visitor_id/u);
});

test("A4 print export embeds charts, preserves links, and reuses chart bytes without another request", async () => {
  const exporter = loadExporter();
  const fetches = [];
  const runtime = { fetch: imageFetch(fetches), createdAt: new Date("2026-08-30T12:00:00Z"), origin: "https://portal.example" };
  await exporter.buildDocx(fixture(), runtime);
  const html = await exporter.buildPrintHtml(fixture(), runtime);
  assert.equal(fetches.length, 2, "print output should reuse the chart cache after DOCX export");
  assert.match(html, /@page\{size:A4/u);
  assert.match(html, /data:image\/jpeg;base64,/u);
  assert.equal((html.match(/data:image\/jpeg;base64,/gu) || []).length, 2);
  assert.match(html, /研究范围：最近半年 · 投行报告 &amp; Charts/u);
  assert.match(html, /<h2>补充图表证据<\/h2>[\s\S]*补充图表/u);
  assert.match(html, /href="https:\/\/portal\.example\/report\.html\?id=report-1"/u);
  assert.doesNotMatch(html, /<script>alert|_report-research|archive_id|visitor_id/u);
});

test("chart placement never assigns an unrelated chart to a finding", () => {
  const exporter = loadExporter();
  const model = exporter.normalizePayload(fixture());
  const placement = exporter.chartAssignments(model);
  assert.deepEqual(Array.from(placement.groups[0], (item) => item.title), ["匹配图表"]);
  assert.deepEqual(Array.from(placement.unmatched, (item) => item.title), ["补充图表"]);
});

test("research_scope accepts the Worker string contract as well as arrays", async () => {
  const exporter = loadExporter();
  const payload = fixture();
  payload.response.research_scope = "最近半年投行报告与历史 Charts";
  const model = exporter.normalizePayload(payload);
  assert.deepEqual(Array.from(model.research_scope), ["最近半年投行报告与历史 Charts"]);
  const html = await exporter.buildPrintHtml(payload, { fetch: imageFetch([]) });
  assert.match(html, /研究范围：最近半年投行报告与历史 Charts/u);
});

test("DOCX and printable PDF exports re-sanitize every user-visible research field", async () => {
  const exporter = loadExporter();
  const payload = fixture();
  payload.question = "Reportify 与 NashAI 怎么看 maifu / 麦府课堂？";
  payload.response.research_title = "MacroGate / Portal Suite 研究";
  payload.response.research_scope = ["Twotigers 范围", "麦府学堂资料"];
  payload.response.executive_summary = "Reportify 汇总 Nash AI 内容";
  payload.response.findings = [{
    title: "MacroGate 结论",
    summary: "Portal Suite 与麦府课堂的旧内容",
    source_ids: ["report-1"],
  }];
  payload.response.data_points = [{
    label: "Twotigers 指标",
    value: "NashAI 42",
    context: "Reportify 2026E",
    source_ids: ["report-1"],
  }];
  payload.response.sources = [{
    id: "report-1",
    title: "Reportify 来源报告",
    institution: "Nash AI",
    industry: "MacroGate",
  }];
  payload.response.charts = [];
  payload.response.follow_up_questions = ["Portal Suite 的下一步是什么？"];

  const forbidden = /Reportify|Nash[\s._-]*AI|Macro[\s._-]*Gate|Portal[\s._-]+Suite|Two[\s._-]*tigers|\bmaifu\b|麦府(?:课堂|学堂)/iu;
  const model = exporter.normalizePayload(payload);
  assert.doesNotMatch(JSON.stringify(model), forbidden);
  assert.match(JSON.stringify(model), /KC桌面/u);

  const result = await exporter.buildDocx(payload, { createdAt: new Date("2026-08-31T12:00:00Z") });
  const entries = zipEntries(result.bytes);
  const documentXml = new TextDecoder().decode(entries.get("word/document.xml"));
  const html = await exporter.buildPrintHtml(payload, { createdAt: new Date("2026-08-31T12:00:00Z") });
  assert.doesNotMatch(documentXml, forbidden);
  assert.doesNotMatch(html, forbidden);
  assert.match(documentXml, /KC桌面/u);
  assert.match(html, /KC桌面/u);
});

test("export stops visibly when a chart response is not JPEG", async () => {
  const exporter = loadExporter();
  await assert.rejects(
    exporter.buildDocx(fixture(), { fetch: imageFetch([], "text/html") }),
    /暂时无法导出/u,
  );
});

async function pdfHarness() {
  const vendor = path.join(root, "portal_suite/site_src/assets/vendor/research-pdf");
  const context = vm.createContext({ Blob, Date, Intl, Promise, TextEncoder, Uint8Array, URL, btoa, setTimeout, clearTimeout, console, window: {} });
  vm.runInContext(await readFile(path.join(vendor, "pdf-lib-1.17.1.min.js"), "utf8"), context);
  vm.runInContext(await readFile(path.join(vendor, "fontkit-1.1.1.min.js"), "utf8"), context);
  vm.runInContext(source, context);
  const fontFilename = source.match(/ResearchSans-Regular-[0-9a-f]+\.ttf/u)[0];
  return { exporter: context.window.PortalReportResearchExport, PDFLib: context.PDFLib, runtime: {
    PDFLib: context.PDFLib, fontkit: context.fontkit,
    fontBytes: new Uint8Array(await readFile(path.join(vendor, fontFilename))),
    fetch: imageFetch([]), origin: "https://portal.example",
  } };
}

test("PDF export produces an A4 binary with embedded Chinese font, chart images and clickable source links", async () => {
  const { exporter, PDFLib, runtime } = await pdfHarness();
  const result = await exporter.buildPdf(fixture(), runtime);
  assert.equal(result.blob.type, "application/pdf");
  assert.match(result.filename, /\.pdf$/u);
  assert.equal(new TextDecoder().decode(result.bytes.subarray(0, 5)), "%PDF-");
  const pdf = await PDFLib.PDFDocument.load(result.bytes);
  assert.ok(pdf.getPageCount() >= 1);
  let images = 0, links = 0;
  for (const page of pdf.getPages()) {
    assert.ok(Math.abs(page.getWidth() - 595.28) < 0.01);
    assert.ok(Math.abs(page.getHeight() - 841.89) < 0.01);
    const resources = page.node.Resources();
    const fonts = resources.lookup(PDFLib.PDFName.of("Font"), PDFLib.PDFDict);
    const font = fonts.lookup(fonts.keys()[0], PDFLib.PDFDict);
    assert.ok(font.has(PDFLib.PDFName.of("ToUnicode")), "Chinese text must remain searchable/copyable");
    const objects = resources.lookup(PDFLib.PDFName.of("XObject"), PDFLib.PDFDict);
    images += objects.keys().length;
    const annots = page.node.Annots();
    for (let i = 0; annots && i < annots.size(); i += 1) {
      const annotation = annots.lookup(i, PDFLib.PDFDict);
      const action = annotation.lookup(PDFLib.PDFName.of("A"), PDFLib.PDFDict);
      const url = action.lookup(PDFLib.PDFName.of("URI"), PDFLib.PDFString).decodeText();
      assert.match(url, /^https:\/\/portal\.example\/report\.html\?id=report-/u);
      links += 1;
    }
  }
  assert.equal(images, 2);
  assert.ok(links >= 6);
  assert.ok(result.bytes.length < 10 * 1024 * 1024, "embedded CJK text and chart files remain bounded");
});

test("PDF download uses the blob download boundary without opening a window or print dialog", async () => {
  const { exporter, runtime } = await pdfHarness();
  const links = [];
  let clicked = 0;
  const document = { body: { appendChild(link) { links.push(link); } }, createElement() { return { style: {}, click() { clicked += 1; }, remove() {} }; } };
  const result = await exporter.downloadPdf(fixture(), { ...runtime, document,
    URL: { createObjectURL(blob) { assert.equal(blob.type, "application/pdf"); return "blob:pdf"; }, revokeObjectURL() {} },
    setTimeout(fn) { fn(); }, window: { open() { throw new Error("unexpected popup"); }, print() { throw new Error("unexpected print"); } },
  });
  assert.equal(clicked, 1);
  assert.equal(result.status, "downloaded");
  assert.match(links[0].download, /\.pdf$/u);
});

test("chart permission failure is actionable and a subsequent export retries the failed image", async () => {
  const exporter = loadExporter();
  await assert.rejects(exporter.buildDocx(fixture(), { fetch: async () => ({ ok: false, status: 403, headers: { get: () => "application/json" } }) }), /重新登录/u);
  const result = await exporter.buildDocx(fixture(), { fetch: imageFetch([]) });
  assert.ok(result.bytes.length > 1000);
});

test("text-only exports explicitly describe the missing chart evidence", async () => {
  const exporter = loadExporter();
  const payload = fixture(); payload.response.charts = [];
  const result = await exporter.buildDocx(payload);
  const xml = new TextDecoder().decode(zipEntries(result.bytes).get("word/document.xml"));
  assert.match(xml, /没有匹配到可引用图表/u);
});

test("news citations retain external URLs and observation dates in DOCX and PDF", async () => {
  const { exporter, PDFLib, runtime } = await pdfHarness();
  const payload = fixture(), id = `news:${"9".repeat(64)}`, url = "https://www.eia.gov/todayinenergy/detail.php?id=123";
  payload.response.charts = [];
  payload.response.sources = [{ id, title: "Power demand update", institution: "EIA", source_url: url, observed_at: "2026-09-08T01:00:00Z", evidence_kind: "news_description" }];
  payload.response.executive_summary = "报告解释供电约束。\n\n新闻补充近期进展。";
  payload.response.summary_source_ids = [id];
  payload.response.findings = [{ title: "近期进展", summary: "新闻简介与报告相互补充。\n\n投产节奏仍取决于并网条件。", source_ids: [id] }];
  payload.response.data_points = [{ label: "并网容量", value: "53 GW", source_ids: [id] }];
  const docx = await exporter.buildDocx(payload, runtime);
  const entries = zipEntries(docx.bytes), decoder = new TextDecoder();
  assert.equal(docx.model.executive_summary, payload.response.executive_summary);
  assert.equal(docx.model.findings[0].summary, payload.response.findings[0].summary);
  assert.match(decoder.decode(entries.get("word/document.xml")), /监测时间 2026-09-08/u);
  assert.match(decoder.decode(entries.get("word/document.xml")), /新闻简介 · GDELT/u);
  assert.match(decoder.decode(entries.get("word/document.xml")), /新闻简介与报告相互补充。<\/w:t><w:br\/><w:t xml:space="preserve"><\/w:t><w:br\/><w:t xml:space="preserve">投产节奏仍取决于并网条件。/u);
  assert.equal(decoder.decode(entries.get("word/_rels/document.xml.rels")).split(url).length - 1, 4, "summary, finding, data point and bibliography must cite the original article");
  assert.doesNotMatch(decoder.decode(entries.get("word/_rels/document.xml.rels")), /report\.html\?id=news/u);
  const pdf = await exporter.buildPdf(payload, runtime);
  const document = await PDFLib.PDFDocument.load(pdf.bytes);
  const urls = document.getPages().flatMap((page) => {
    const annotations = page.node.Annots();
    return Array.from({ length: annotations ? annotations.size() : 0 }, (_, index) => annotations.lookup(index, PDFLib.PDFDict).lookup(PDFLib.PDFName.of("A"), PDFLib.PDFDict).lookup(PDFLib.PDFName.of("URI"), PDFLib.PDFString).decodeText());
  });
  assert.equal(urls.filter((candidate) => candidate === url).length, 4, "all inline references and the bibliography must cite the original article");
  assert.ok(urls.every((candidate) => candidate === url || candidate === "https://www.gdeltproject.org/"), JSON.stringify(urls));
  payload.response.sources[0].source_url = "javascript:alert(1)";
  const invalid = await exporter.buildDocx(payload, runtime);
  assert.doesNotMatch(decoder.decode(zipEntries(invalid.bytes).get("word/_rels/document.xml.rels")), /javascript:/u);
});

test("exports retain twelve available sources and up to eight citations per analytical section", () => {
  const exporter = loadExporter();
  const sources = Array.from({ length: 12 }, (_, index) => ({ id: `report-${index}`, title: `Source ${index}` }));
  const ids = sources.map((source) => source.id);
  const model = exporter.normalizePayload({ sources, executive_summary: "综合分析。", summary_source_ids: ids,
    findings: [{ title: "共同约束", summary: "比较证据。", source_ids: ids }],
    data_points: [{ label: "容量", value: "53 GW", source_ids: ids }],
  });
  assert.equal(model.sources.length, 12);
  assert.deepEqual(Array.from(model.summary_source_ids), ids.slice(0, 8));
  assert.deepEqual(Array.from(model.findings[0].source_ids), ids.slice(0, 8));
  assert.deepEqual(Array.from(model.data_points[0].source_ids), ids.slice(0, 8));
});

test("unlinked chart evidence stays inline and cites its exact chart permalink in DOCX and PDF", async () => {
  const { exporter, PDFLib, runtime } = await pdfHarness();
  const payload = fixture(), imageId = "c".repeat(64), sourceId = `chart:${imageId}`;
  payload.response.sources = [{ id: sourceId, title: "尚未关联全文的图表", evidence_kind: "chart_metadata" }];
  payload.response.summary_source_ids = [sourceId];
  payload.response.findings = [{ title: "图表证据", summary: "根据图表提取内容生成。", source_ids: [sourceId] }];
  payload.response.charts = [{ image_id: imageId, source_id: sourceId, report_id: "", report_title: "图表所在报告", title: "独立图表" }];
  const model = exporter.normalizePayload(payload);
  assert.equal(exporter.chartAssignments(model).groups[0].length, 1);
  const docx = await exporter.buildDocx(payload, runtime);
  const rels = new TextDecoder().decode(zipEntries(docx.bytes).get("word/_rels/document.xml.rels"));
  assert.match(rels, new RegExp(`/charts\\.html\\?image=${imageId}`, "u"));
  assert.doesNotMatch(rels, /report\.html\?id=chart/u);
  const pdf = await exporter.buildPdf(payload, runtime);
  const document = await PDFLib.PDFDocument.load(pdf.bytes);
  const urls = [];
  for (const page of document.getPages()) {
    const annotations = page.node.Annots();
    for (let i = 0; annotations && i < annotations.size(); i += 1) {
      const action = annotations.lookup(i, PDFLib.PDFDict).lookup(PDFLib.PDFName.of("A"), PDFLib.PDFDict);
      urls.push(action.lookup(PDFLib.PDFName.of("URI"), PDFLib.PDFString).decodeText());
    }
  }
  assert.ok(urls.length >= 2);
  assert.ok(urls.every((url) => url === `https://portal.example/charts.html?image=${imageId}`));
});
