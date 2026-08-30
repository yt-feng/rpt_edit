import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const source = await readFile(path.join(root, "portal_suite/site_src/assets/report-research-export.js"), "utf8");
const jpeg = await readFile(path.join(root, "prompts/zsxq_img.jpg"));

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
  assert.match(documentXml, /w:pgSz w:w="12240" w:h="15840"/u);
  assert.match(documentXml, /w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/u);
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

test("export stops visibly when a chart response is not JPEG", async () => {
  const exporter = loadExporter();
  await assert.rejects(
    exporter.buildDocx(fixture(), { fetch: imageFetch([], "text/html") }),
    /暂时无法导出/u,
  );
});
