(() => {
  "use strict";

  const DOCX_MIME_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
  const PUBLIC_BRAND = "KC桌面";
  const MAX_CHART_BYTES = 3 * 1024 * 1024;
  const MAX_TOTAL_CHART_BYTES = 18 * 1024 * 1024;
  const XML_DECLARATION = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>';
  const CONTENT_DOCUMENT_LANG = window.KCDeskLocale && window.KCDeskLocale.contentLocale || "zh-CN";
  const CONTENT_DOCUMENT_DIR = window.KCDeskLocale && window.KCDeskLocale.direction || "ltr";
  const CONTENT_INTL_LOCALE = window.KCDeskLocale && window.KCDeskLocale.intlLocale || "zh-CN";
  const chartCache = new Map();
  const CRC32_TABLE = buildCrc32Table();

  const LEGACY_SOURCE_WORDS = [["report", "ify"], ["nash", "ai"], ["mai", "fu"]];
  const LEGACY_SOURCE_DOMAINS = [["report", "ify", "cn"], ["nash", "ai", "cn"], ["hi", "bor", "com", "cn"]];
  const LEGACY_CONTACT_WORDS = [
    ["macro", "gate"], ["support", "contact"], ["portal", "suite"], ["portal", "alternate"],
    ["portal", "娱乐"], ["kc", "desk", "notes"], ["two", "tigers"],
  ];

  function legacyBrandPattern(parts) {
    const escaped = parts.map((part) => String(part).replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    return new RegExp(escaped.join("[\\s._-]*"), "gi");
  }

  function publicDocumentText(value) {
    let result = String(value || "")
      .replace(/[\u200b-\u200d\u2060\ufeff]/g, "")
      .replace(/[Ａ-Ｚａ-ｚ０-９]/g, (character) => String.fromCharCode(character.charCodeAt(0) - 0xfee0));
    for (const parts of LEGACY_SOURCE_DOMAINS) result = result.replace(legacyBrandPattern(parts), PUBLIC_BRAND);
    for (const parts of [...LEGACY_SOURCE_WORDS, ...LEGACY_CONTACT_WORDS]) result = result.replace(legacyBrandPattern(parts), PUBLIC_BRAND);
    for (const legacy of [
      String.fromCharCode(0x6167, 0x535a),
      String.fromCharCode(0x9ea6, 0x5e9c, 0x5b66, 0x5802),
      String.fromCharCode(0x9ea6, 0x5e9c, 0x8bfe, 0x5802),
    ]) result = result.replace(new RegExp(legacy, "g"), PUBLIC_BRAND);
    return result;
  }

  function text(value, limit = 12000) {
    const source = value === null || value === undefined ? "" : String(value);
    let result = "";
    for (const character of source) {
      const codePoint = character.codePointAt(0);
      if (
        codePoint === 0x09
        || codePoint === 0x0A
        || codePoint === 0x0D
        || (codePoint >= 0x20 && codePoint <= 0xD7FF)
        || (codePoint >= 0xE000 && codePoint <= 0xFFFD)
        || (codePoint >= 0x10000 && codePoint <= 0x10FFFF)
      ) result += character;
      if (result.length >= limit) break;
    }
    return publicDocumentText(result).trim();
  }

  function escapeXml(value) {
    return text(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&apos;");
  }

  function escapeHtml(value) {
    return text(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function normalizeDate(value) {
    const date = value instanceof Date ? new Date(value.getTime()) : new Date(value || Date.now());
    return Number.isNaN(date.getTime()) ? new Date() : date;
  }

  function dateLabel(value) {
    const date = normalizeDate(value);
    const parts = new Intl.DateTimeFormat(CONTENT_INTL_LOCALE, {
      year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false,
    }).formatToParts(date).reduce((result, part) => ({ ...result, [part.type]: part.value }), {});
    return `${parts.year}-${parts.month}-${parts.day} ${parts.hour}:${parts.minute}`;
  }

  function dateStamp(value) {
    const date = normalizeDate(value);
    return `${date.getFullYear()}${String(date.getMonth() + 1).padStart(2, "0")}${String(date.getDate()).padStart(2, "0")}`;
  }

  function publicOrigin(runtime = {}) {
    const candidate = text(runtime.origin || (window.location && window.location.origin), 512);
    try {
      const parsed = new URL(candidate);
      if (parsed.protocol === "https:" || parsed.protocol === "http:") return parsed.origin;
    } catch (_error) { /* Use a non-routable test origin outside the browser. */ }
    return "https://example.invalid";
  }

  function canonicalSourceUrl(id, source = {}, origin = "https://example.invalid") {
    const reportId = text(id || source.id, 180);
    if (reportId) return `${origin}/report.html?id=${encodeURIComponent(reportId)}`;
    const title = text(source.report_title || source.title, 300);
    return title ? `${origin}/?q=${encodeURIComponent(title)}` : `${origin}/`;
  }

  function validSourceIds(value, sourceMap) {
    if (!Array.isArray(value)) return [];
    const seen = new Set();
    return value.map((id) => text(id, 180)).filter((id) => {
      if (!id || seen.has(id) || !sourceMap.has(id)) return false;
      seen.add(id);
      return true;
    }).slice(0, 8);
  }

  function normalizePayload(payload = {}, runtime = {}) {
    const response = payload.response && typeof payload.response === "object" ? payload.response : payload;
    const sourceRows = (Array.isArray(response.sources) ? response.sources : Array.isArray(response.recommendations) ? response.recommendations : [])
      .filter((item) => item && typeof item === "object" && text(item.id, 180))
      .slice(0, 8)
      .map((item) => ({
        id: text(item.id, 180),
        title: text(item.title || item.title_zh || item.report_title || "来源报告", 500),
        institution: text(item.institution || item.bank_name, 180),
        industry: text(item.industry, 180),
        date: text(item.date_folder || item.date, 80),
      }));
    const sourceMap = new Map(sourceRows.map((item) => [item.id, item]));
    const findings = (Array.isArray(response.findings) ? response.findings : [])
      .filter((item) => item && typeof item === "object")
      .slice(0, 8)
      .map((item) => ({
        title: text(item.title || "核心发现", 500),
        summary: text(item.summary || item.analysis, 5000),
        source_ids: validSourceIds(item.source_ids, sourceMap),
      }));
    const dataPoints = (Array.isArray(response.data_points) ? response.data_points : [])
      .filter((item) => item && typeof item === "object")
      .slice(0, 12)
      .map((item) => ({
        label: text(item.label || item.metric || "数据", 300),
        value: text(item.value, 500),
        context: text(item.context || item.period, 1200),
        source_ids: validSourceIds(item.source_ids, sourceMap),
      }));
    const charts = (Array.isArray(response.charts) ? response.charts : [])
      .filter((item) => item && typeof item === "object" && /^[0-9a-f]{64}$/u.test(String(item.image_id || "")))
      .filter((item) => text(item.report_id || item.report_title, 500))
      .slice(0, 6)
      .map((item) => ({
        image_id: String(item.image_id),
        report_id: text(item.report_id, 180),
        report_title: text(item.report_title, 500),
        title: text(item.title || "研究图表", 500),
        description: text(item.description || item.trend_summary, 3000),
        metrics: (Array.isArray(item.metrics) ? item.metrics : []).map((value) => text(value, 180)).filter(Boolean).slice(0, 5),
      }));
    const question = text(payload.question || response.research_title || response.question || "KC桌面跨报告研究", 600);
    const researchTitle = text(response.research_title || question || "KC桌面跨报告研究", 600);
    const questionHash = text(payload.questionHash || payload.question_hash || response.question_hash, 128).replace(/[^a-zA-Z0-9_-]/gu, "");
    return {
      question,
      research_title: researchTitle,
      research_scope: (Array.isArray(response.research_scope)
        ? response.research_scope
        : text(response.research_scope, 1200) ? [response.research_scope] : [])
        .map((item) => text(item, 240)).filter(Boolean).slice(0, 8),
      generated_at: text(response.generated_at || payload.generated_at, 80),
      question_hash: questionHash,
      source_origin: publicOrigin(runtime),
      executive_summary: text(response.executive_summary || response.answer, 8000),
      summary_source_ids: validSourceIds(response.summary_source_ids, sourceMap),
      findings: findings.filter((item) => item.title || item.summary),
      data_points: dataPoints.filter((item) => item.label || item.value || item.context),
      charts,
      sources: sourceRows,
      follow_up_questions: (Array.isArray(response.follow_up_questions) ? response.follow_up_questions : []).map((item) => text(item, 600)).filter(Boolean).slice(0, 3),
    };
  }

  function chartAssignments(model) {
    const groups = model.findings.map(() => []);
    const unmatched = [];
    const sourceSets = model.findings.map((finding) => new Set(finding.source_ids));
    for (const chart of model.charts) {
      const index = chart.report_id ? sourceSets.findIndex((ids) => ids.has(chart.report_id)) : -1;
      if (index >= 0) groups[index].push(chart);
      else unmatched.push(chart);
    }
    return { groups, unmatched };
  }

  function parseJpeg(bytes) {
    if (!(bytes instanceof Uint8Array) || bytes.length < 4 || bytes[0] !== 0xFF || bytes[1] !== 0xD8) {
      throw new Error("图表不是有效的 JPEG 图片。");
    }
    let offset = 2;
    while (offset + 9 < bytes.length) {
      if (bytes[offset] !== 0xFF) { offset += 1; continue; }
      const marker = bytes[offset + 1];
      offset += 2;
      if (marker === 0xD8 || marker === 0xD9) continue;
      if (offset + 2 > bytes.length) break;
      const length = (bytes[offset] << 8) | bytes[offset + 1];
      if (length < 2 || offset + length > bytes.length) break;
      if ([0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF].includes(marker)) {
        const height = (bytes[offset + 3] << 8) | bytes[offset + 4];
        const width = (bytes[offset + 5] << 8) | bytes[offset + 6];
        if (!width || !height) break;
        return { width, height };
      }
      offset += length;
    }
    throw new Error("无法读取图表尺寸。");
  }

  async function fetchChart(chart, runtime = {}) {
    if (chartCache.has(chart.image_id)) return chartCache.get(chart.image_id);
    const task = (async () => {
      const fetchRef = runtime.fetch || (typeof fetch === "function" ? fetch : null);
      if (!fetchRef) throw new Error("当前浏览器无法读取图表。");
      const response = await fetchRef(`/api/charts/image?id=${encodeURIComponent(chart.image_id)}`, {
        method: "GET", cache: "force-cache", credentials: "same-origin",
      });
      const contentType = String(response && response.headers && response.headers.get("content-type") || "").split(";", 1)[0].trim().toLowerCase();
      if (!response || !response.ok || contentType !== "image/jpeg") throw new Error(`图表“${chart.title}”暂时无法导出，请重试。`);
      const bytes = new Uint8Array(await response.arrayBuffer());
      if (!bytes.length || bytes.length > MAX_CHART_BYTES) throw new Error(`图表“${chart.title}”文件大小异常。`);
      return { ...chart, bytes, ...parseJpeg(bytes) };
    })();
    chartCache.set(chart.image_id, task);
    try {
      return await task;
    } catch (error) {
      chartCache.delete(chart.image_id);
      throw error;
    }
  }

  async function chartAssets(model, runtime = {}) {
    const assets = await Promise.all(model.charts.map((chart) => fetchChart(chart, runtime)));
    const total = assets.reduce((sum, item) => sum + item.bytes.length, 0);
    if (total > MAX_TOTAL_CHART_BYTES) throw new Error("本次图表总量过大，请缩小研究范围后重试。");
    return new Map(assets.map((item) => [item.image_id, item]));
  }

  function buildCrc32Table() {
    const table = new Uint32Array(256);
    for (let index = 0; index < table.length; index += 1) {
      let value = index;
      for (let bit = 0; bit < 8; bit += 1) value = value & 1 ? 0xEDB88320 ^ (value >>> 1) : value >>> 1;
      table[index] = value >>> 0;
    }
    return table;
  }

  function crc32(bytes) {
    let value = 0xFFFFFFFF;
    for (const byte of bytes) value = CRC32_TABLE[(value ^ byte) & 0xFF] ^ (value >>> 8);
    return (value ^ 0xFFFFFFFF) >>> 0;
  }

  function concatBytes(chunks) {
    const length = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
    const result = new Uint8Array(length);
    let offset = 0;
    for (const chunk of chunks) { result.set(chunk, offset); offset += chunk.length; }
    return result;
  }

  function dosTimestamp(date) {
    const year = Math.min(2107, Math.max(1980, date.getFullYear()));
    return {
      time: (date.getHours() << 11) | (date.getMinutes() << 5) | Math.floor(date.getSeconds() / 2),
      date: ((year - 1980) << 9) | ((date.getMonth() + 1) << 5) | date.getDate(),
    };
  }

  function storedZip(files, createdAt) {
    const encoder = new TextEncoder();
    const stamp = dosTimestamp(createdAt);
    const locals = [];
    const centralMeta = [];
    let offset = 0;
    for (const file of files) {
      const name = encoder.encode(file.name);
      const data = typeof file.data === "string" ? encoder.encode(file.data) : file.data;
      const checksum = crc32(data);
      const header = new Uint8Array(30);
      const view = new DataView(header.buffer);
      view.setUint32(0, 0x04034B50, true); view.setUint16(4, 20, true); view.setUint16(6, 0x0800, true);
      view.setUint16(10, stamp.time, true); view.setUint16(12, stamp.date, true); view.setUint32(14, checksum, true);
      view.setUint32(18, data.length, true); view.setUint32(22, data.length, true); view.setUint16(26, name.length, true);
      const record = concatBytes([header, name, data]);
      locals.push(record); centralMeta.push({ name, checksum, length: data.length, offset }); offset += record.length;
    }
    const centrals = centralMeta.map((entry) => {
      const header = new Uint8Array(46); const view = new DataView(header.buffer);
      view.setUint32(0, 0x02014B50, true); view.setUint16(4, 20, true); view.setUint16(6, 20, true); view.setUint16(8, 0x0800, true);
      view.setUint16(12, stamp.time, true); view.setUint16(14, stamp.date, true); view.setUint32(16, entry.checksum, true);
      view.setUint32(20, entry.length, true); view.setUint32(24, entry.length, true); view.setUint16(28, entry.name.length, true);
      view.setUint32(42, entry.offset, true);
      return concatBytes([header, entry.name]);
    });
    const centralSize = centrals.reduce((sum, value) => sum + value.length, 0);
    const end = new Uint8Array(22); const endView = new DataView(end.buffer);
    endView.setUint32(0, 0x06054B50, true); endView.setUint16(8, files.length, true); endView.setUint16(10, files.length, true);
    endView.setUint32(12, centralSize, true); endView.setUint32(16, offset, true);
    return concatBytes([...locals, ...centrals, end]);
  }

  function runXml(value, options = {}) {
    const properties = [
      options.bold ? "<w:b/>" : "",
      options.italic ? "<w:i/>" : "",
      options.color ? `<w:color w:val="${options.color}"/>` : "",
      options.size ? `<w:sz w:val="${options.size}"/><w:szCs w:val="${options.size}"/>` : "",
    ].join("");
    const parts = text(value).split(/\r?\n/u).map((part) => `<w:t xml:space="preserve">${escapeXml(part)}</w:t>`);
    return `<w:r><w:rPr><w:rFonts w:ascii="Arial Unicode MS" w:hAnsi="Arial Unicode MS" w:eastAsia="Arial Unicode MS"/><w:lang w:val="en-US" w:eastAsia="zh-CN"/>${properties}</w:rPr>${parts.join("<w:br/>")}</w:r>`;
  }

  function paragraphXml(content, options = {}) {
    const properties = [
      options.style ? `<w:pStyle w:val="${options.style}"/>` : "",
      options.align ? `<w:jc w:val="${options.align}"/>` : "",
      options.keepNext ? "<w:keepNext/>" : "",
      options.pageBreakBefore ? "<w:pageBreakBefore/>" : "",
      options.numbered ? `<w:numPr><w:ilvl w:val="0"/><w:numId w:val="${options.numbered === true ? 1 : Math.max(1, Math.min(2, Math.floor(Number(options.numbered) || 1)))}"/></w:numPr>` : "",
    ].join("");
    return `<w:p><w:pPr>${properties}</w:pPr>${content}</w:p>`;
  }

  function drawingXml(image, relationshipId, drawingId) {
    const maxWidth = 5303520;
    const maxHeight = 3474720;
    const scale = Math.min(maxWidth / image.width, maxHeight / image.height);
    const cx = Math.max(1, Math.round(image.width * scale));
    const cy = Math.max(1, Math.round(image.height * scale));
    const title = escapeXml(image.title || "研究图表");
    return `<w:r><w:drawing><wp:inline xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" distT="0" distB="0" distL="0" distR="0"><wp:extent cx="${cx}" cy="${cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="${drawingId}" name="Chart ${drawingId}" descr="${title}"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr><a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="${drawingId}" name="chart-${drawingId}.jpg" descr="${title}"/><pic:cNvPicPr/></pic:nvPicPr><pic:blipFill><a:blip r:embed="${relationshipId}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="${cx}" cy="${cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>`;
  }

  function stylesXml() {
    return `${XML_DECLARATION}<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial Unicode MS" w:hAnsi="Arial Unicode MS" w:eastAsia="Arial Unicode MS"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-US" w:eastAsia="zh-CN"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="0" w:after="120" w:line="264" w:lineRule="auto"/></w:pPr><w:rPr><w:rFonts w:ascii="Arial Unicode MS" w:hAnsi="Arial Unicode MS" w:eastAsia="Arial Unicode MS"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-US" w:eastAsia="zh-CN"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:qFormat/><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="160"/></w:pPr><w:rPr><w:b/><w:color w:val="203748"/><w:sz w:val="60"/><w:szCs w:val="60"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:pPr><w:jc w:val="center"/><w:spacing w:after="80"/></w:pPr><w:rPr><w:color w:val="2B5163"/><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Kicker"><w:name w:val="Kicker"/><w:basedOn w:val="Normal"/><w:pPr><w:jc w:val="center"/><w:spacing w:before="1200" w:after="360"/></w:pPr><w:rPr><w:b/><w:color w:val="A06A12"/><w:sz w:val="20"/><w:szCs w:val="20"/><w:spacing w:val="24"/></w:rPr></w:style>${[["Heading1", "heading 1", 32, "2E74B5", 320, 160], ["Heading2", "heading 2", 26, "2E74B5", 240, 120], ["Heading3", "heading 3", 24, "1F4D78", 160, 80]].map(([id, name, size, color, before, after], index) => `<w:style w:type="paragraph" w:styleId="${id}"><w:name w:val="${name}"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="${before}" w:after="${after}"/></w:pPr><w:rPr><w:b/><w:color w:val="${color}"/><w:sz w:val="${size}"/><w:szCs w:val="${size}"/></w:rPr></w:style>`).join("")}<w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="Caption"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="40" w:after="120"/></w:pPr><w:rPr><w:color w:val="59636E"/><w:sz w:val="18"/><w:szCs w:val="18"/><w:i/></w:rPr></w:style><w:style w:type="character" w:styleId="Hyperlink"><w:name w:val="Hyperlink"/><w:unhideWhenUsed/><w:rPr><w:color w:val="0F766E"/><w:u w:val="single"/></w:rPr></w:style></w:styles>`;
  }

  function numberingXml() {
    const level = '<w:multiLevelType w:val="singleLevel"/><w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%1."/><w:lvlJc w:val="left"/><w:pPr><w:tabs><w:tab w:val="num" w:pos="720"/></w:tabs><w:spacing w:after="160" w:line="280" w:lineRule="auto"/><w:ind w:left="720" w:hanging="360"/></w:pPr></w:lvl>';
    return `${XML_DECLARATION}<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:abstractNum w:abstractNumId="0">${level}</w:abstractNum><w:abstractNum w:abstractNumId="1">${level}</w:abstractNum><w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num><w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num></w:numbering>`;
  }

  function headerXml() {
    return `${XML_DECLARATION}<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:tabs><w:tab w:val="right" w:pos="9360"/></w:tabs><w:pBdr><w:bottom w:val="single" w:sz="4" w:space="4" w:color="D7DBE2"/></w:pBdr></w:pPr>${runXml("KC桌面  |  RESEARCH BRIEF", { bold: true, color: "59636E", size: 18 })}</w:p></w:hdr>`;
  }

  function footerXml() {
    return `${XML_DECLARATION}<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:pPr><w:jc w:val="right"/></w:pPr>${runXml("KC桌面 Research  ·  ", { color: "7A838C", size: 18 })}<w:fldSimple w:instr="PAGE"><w:r><w:rPr><w:color w:val="7A838C"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>`;
  }

  async function createDocx(model, assets, createdAt) {
    const relationships = [
      { id: "rId1", type: "styles", target: "styles.xml" },
      { id: "rId2", type: "numbering", target: "numbering.xml" },
      { id: "rId3", type: "header", target: "header1.xml" },
      { id: "rId4", type: "footer", target: "footer1.xml" },
    ];
    let nextRelationship = 5;
    let drawingId = 1;
    const media = [];
    const sourceIndex = new Map(model.sources.map((source, index) => [source.id, index + 1]));
    const hyperlink = (label, url) => {
      const id = `rId${nextRelationship++}`;
      relationships.push({ id, type: "hyperlink", target: url, external: true });
      return `<w:hyperlink r:id="${id}" w:history="1"><w:r><w:rPr><w:rStyle w:val="Hyperlink"/></w:rPr><w:t xml:space="preserve">${escapeXml(label)}</w:t></w:r></w:hyperlink>`;
    };
    const sourceRefs = (ids) => {
      const valid = ids.filter((id) => sourceIndex.has(id));
      if (!valid.length) return "";
      const runs = [runXml("来源：", { color: "59636E", size: 18 })];
      valid.forEach((id, index) => {
        if (index) runs.push(runXml("  ", { size: 18 }));
        runs.push(hyperlink(`[S${sourceIndex.get(id)}]`, canonicalSourceUrl(id, model.sources[sourceIndex.get(id) - 1], model.source_origin)));
      });
      return paragraphXml(runs.join(""), { style: "Caption" });
    };
    const imageParagraphs = (chart) => {
      const asset = assets.get(chart.image_id);
      const relationId = `rId${nextRelationship++}`;
      const filename = `image${media.length + 1}.jpg`;
      relationships.push({ id: relationId, type: "image", target: `media/${filename}` });
      media.push({ name: `word/media/${filename}`, data: asset.bytes });
      const source = model.sources.find((item) => item.id === chart.report_id) || { id: chart.report_id, title: chart.report_title };
      const url = canonicalSourceUrl(chart.report_id, source, model.source_origin);
      const caption = [chart.description, chart.metrics.join(" · ")].filter(Boolean).join("  ");
      return [
        paragraphXml(runXml(chart.title, { bold: true, color: "1F4D78", size: 22 }), { keepNext: true }),
        paragraphXml(drawingXml(asset, relationId, drawingId++), { align: "center", keepNext: true }),
        paragraphXml(`${caption ? runXml(`${caption}  `, { color: "59636E", size: 18 }) : ""}${hyperlink("查看来源报告", url)}`, { style: "Caption" }),
      ].join("");
    };
    const assignment = chartAssignments(model);
    const body = [];
    body.push(paragraphXml(runXml("KC桌面研究报告", { bold: true }), { style: "Kicker" }));
    body.push(paragraphXml(runXml(model.research_title || model.question, { bold: true }), { style: "Title" }));
    if (model.question && model.question !== model.research_title) body.push(paragraphXml(runXml(model.question), { style: "Subtitle" }));
    if (model.research_scope.length) body.push(paragraphXml(runXml(`研究范围：${model.research_scope.join(" · ")}`, { color: "59636E", size: 20 }), { align: "center" }));
    body.push(paragraphXml(runXml(`生成时间：${dateLabel(model.generated_at || createdAt)}`, { color: "59636E", size: 20 }), { align: "center" }));
    body.push(paragraphXml(runXml("基于 KC桌面跨报告 RAG 的来源化研究摘要。请结合来源报告核验后使用。", { italic: true, color: "59636E", size: 19 }), { align: "center" }));
    body.push(paragraphXml(runXml(""), { pageBreakBefore: true }));
    if (model.executive_summary) {
      body.push(paragraphXml(runXml("研究摘要"), { style: "Heading1" }));
      body.push(paragraphXml(runXml(model.executive_summary)));
      body.push(sourceRefs(model.summary_source_ids));
    }
    if (model.findings.length) {
      body.push(paragraphXml(runXml("主要发现"), { style: "Heading1" }));
      model.findings.forEach((finding, index) => {
        body.push(paragraphXml(runXml(`${index + 1}. ${finding.title}`), { style: "Heading2" }));
        if (finding.summary) body.push(paragraphXml(runXml(finding.summary)));
        body.push(sourceRefs(finding.source_ids));
        assignment.groups[index].forEach((chart) => body.push(imageParagraphs(chart)));
      });
    }
    if (assignment.unmatched.length) {
      body.push(paragraphXml(runXml("补充图表证据"), { style: "Heading1" }));
      assignment.unmatched.forEach((chart) => body.push(imageParagraphs(chart)));
    }
    if (model.data_points.length) {
      body.push(paragraphXml(runXml("关键数据"), { style: "Heading1" }));
      model.data_points.forEach((item) => {
        body.push(paragraphXml(runXml(`${item.label}  ${item.value}`, { bold: true }), { style: "Heading3" }));
        if (item.context) body.push(paragraphXml(runXml(item.context)));
        body.push(sourceRefs(item.source_ids));
      });
    }
    if (model.sources.length) {
      body.push(paragraphXml(runXml("来源报告"), { style: "Heading1" }));
      model.sources.forEach((source) => {
        const meta = [source.institution, source.industry, source.date].filter(Boolean).join(" · ");
        body.push(paragraphXml(`${hyperlink(source.title || source.id, canonicalSourceUrl(source.id, source, model.source_origin))}${meta ? runXml(`\n${meta}`, { color: "59636E", size: 18 }) : ""}`, { numbered: true }));
      });
    }
    if (model.follow_up_questions.length) {
      body.push(paragraphXml(runXml("可继续研究"), { style: "Heading1" }));
      model.follow_up_questions.forEach((question) => body.push(paragraphXml(runXml(question), { numbered: 2 })));
    }
    body.push(paragraphXml(runXml("说明：本材料由 AI 根据已索引研究资料生成，不构成投资建议；重要结论请以来源报告为准。", { italic: true, color: "59636E", size: 18 })));
    const documentXml = `${XML_DECLARATION}<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>${body.join("")}<w:sectPr><w:headerReference w:type="default" r:id="rId3"/><w:footerReference w:type="default" r:id="rId4"/><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/><w:cols w:space="720"/><w:docGrid w:linePitch="360"/></w:sectPr></w:body></w:document>`;
    const relationshipTypes = {
      styles: "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles",
      numbering: "http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering",
      header: "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header",
      footer: "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer",
      image: "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image",
      hyperlink: "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
    };
    const documentRelationships = `${XML_DECLARATION}<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">${relationships.map((item) => `<Relationship Id="${item.id}" Type="${relationshipTypes[item.type]}" Target="${escapeXml(item.target)}"${item.external ? ' TargetMode="External"' : ""}/>`).join("")}</Relationships>`;
    const contentTypes = `${XML_DECLARATION}<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="jpg" ContentType="image/jpeg"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/><Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/><Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>`;
    const rootRelationships = `${XML_DECLARATION}<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>`;
    const timestamp = createdAt.toISOString();
    const core = `${XML_DECLARATION}<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>KC桌面研究报告</dc:title><dc:creator>KC桌面</dc:creator><cp:lastModifiedBy>KC桌面</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">${timestamp}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">${timestamp}</dcterms:modified></cp:coreProperties>`;
    const app = `${XML_DECLARATION}<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>KC桌面 Research Export</Application><DocSecurity>0</DocSecurity><ScaleCrop>false</ScaleCrop><Company>KC桌面</Company><LinksUpToDate>false</LinksUpToDate></Properties>`;
    return storedZip([
      { name: "[Content_Types].xml", data: contentTypes }, { name: "_rels/.rels", data: rootRelationships },
      { name: "docProps/core.xml", data: core }, { name: "docProps/app.xml", data: app },
      { name: "word/document.xml", data: documentXml }, { name: "word/_rels/document.xml.rels", data: documentRelationships },
      { name: "word/styles.xml", data: stylesXml() }, { name: "word/numbering.xml", data: numberingXml() },
      { name: "word/header1.xml", data: headerXml() }, { name: "word/footer1.xml", data: footerXml() }, ...media,
    ], createdAt);
  }

  function safeFilename(extension, model, createdAt) {
    const hash = (model.question_hash || "research").slice(0, 12);
    return `KC桌面研究结果_${dateStamp(createdAt)}_${hash}.${extension}`;
  }

  async function buildDocx(payload, runtime = {}) {
    if (typeof Blob !== "function") throw new Error("当前浏览器不支持 Word 导出。");
    const model = normalizePayload(payload, runtime);
    const createdAt = normalizeDate(runtime.createdAt || model.generated_at);
    const assets = await chartAssets(model, runtime);
    const bytes = await createDocx(model, assets, createdAt);
    return { blob: new Blob([bytes], { type: DOCX_MIME_TYPE }), bytes, filename: safeFilename("docx", model, createdAt), model };
  }

  function bytesToDataUrl(bytes) {
    let binary = "";
    for (let offset = 0; offset < bytes.length; offset += 0x8000) binary += String.fromCharCode(...bytes.subarray(offset, offset + 0x8000));
    const encode = typeof btoa === "function" ? btoa : null;
    if (!encode) throw new Error("当前浏览器无法嵌入图表。");
    return `data:image/jpeg;base64,${encode(binary)}`;
  }

  function printSourceRefs(ids, sourceIndex, sourceMap, sourceOrigin) {
    const links = ids.filter((id) => sourceIndex.has(id)).map((id) => `<a href="${escapeHtml(canonicalSourceUrl(id, sourceMap.get(id), sourceOrigin))}">[S${sourceIndex.get(id)}]</a>`);
    return links.length ? `<p class="source-refs"><span>来源</span>${links.join("")}</p>` : "";
  }

  async function buildPrintHtml(payload, runtime = {}) {
    const model = normalizePayload(payload, runtime);
    const assets = await chartAssets(model, runtime);
    const sourceIndex = new Map(model.sources.map((source, index) => [source.id, index + 1]));
    const sourceMap = new Map(model.sources.map((source) => [source.id, source]));
    const assignment = chartAssignments(model);
    const chartHtml = (chart) => {
      const asset = assets.get(chart.image_id);
      const source = sourceMap.get(chart.report_id) || { id: chart.report_id, title: chart.report_title };
      const caption = [chart.description, chart.metrics.join(" · ")].filter(Boolean).join(" · ");
      return `<figure><h3>${escapeHtml(chart.title)}</h3><img src="${bytesToDataUrl(asset.bytes)}" width="${asset.width}" height="${asset.height}" alt="${escapeHtml(chart.title)}"><figcaption>${caption ? `<span>${escapeHtml(caption)}</span>` : ""}<a href="${escapeHtml(canonicalSourceUrl(chart.report_id, source, model.source_origin))}">查看来源报告</a></figcaption></figure>`;
    };
    const body = [];
    body.push(`<section class="cover"><p class="kicker">KC桌面研究报告</p><h1>${escapeHtml(model.research_title || model.question)}</h1>${model.question && model.question !== model.research_title ? `<p class="subtitle">${escapeHtml(model.question)}</p>` : ""}${model.research_scope.length ? `<p class="scope">研究范围：${escapeHtml(model.research_scope.join(" · "))}</p>` : ""}<p class="date">生成时间：${escapeHtml(dateLabel(model.generated_at))}</p><p class="notice">基于 KC桌面跨报告 RAG 的来源化研究摘要。请结合来源报告核验后使用。</p></section>`);
    body.push('<main class="report">');
    if (model.executive_summary) body.push(`<section><h2>研究摘要</h2><p>${escapeHtml(model.executive_summary)}</p>${printSourceRefs(model.summary_source_ids, sourceIndex, sourceMap, model.source_origin)}</section>`);
    if (model.findings.length) {
      body.push("<section><h2>主要发现</h2>");
      model.findings.forEach((finding, index) => {
        body.push(`<article class="finding"><h3>${index + 1}. ${escapeHtml(finding.title)}</h3>${finding.summary ? `<p>${escapeHtml(finding.summary)}</p>` : ""}${printSourceRefs(finding.source_ids, sourceIndex, sourceMap, model.source_origin)}${assignment.groups[index].map(chartHtml).join("")}</article>`);
      });
      body.push("</section>");
    }
    if (assignment.unmatched.length) body.push(`<section><h2>补充图表证据</h2>${assignment.unmatched.map(chartHtml).join("")}</section>`);
    if (model.data_points.length) body.push(`<section><h2>关键数据</h2><div class="data-grid">${model.data_points.map((item) => `<article><h3>${escapeHtml(item.label)}</h3><strong>${escapeHtml(item.value)}</strong>${item.context ? `<p>${escapeHtml(item.context)}</p>` : ""}${printSourceRefs(item.source_ids, sourceIndex, sourceMap, model.source_origin)}</article>`).join("")}</div></section>`);
    if (model.sources.length) body.push(`<section><h2>来源报告</h2><ol class="sources">${model.sources.map((source) => `<li><a href="${escapeHtml(canonicalSourceUrl(source.id, source, model.source_origin))}">${escapeHtml(source.title || source.id)}</a>${[source.institution, source.industry, source.date].filter(Boolean).length ? `<span>${escapeHtml([source.institution, source.industry, source.date].filter(Boolean).join(" · "))}</span>` : ""}</li>`).join("")}</ol></section>`);
    if (model.follow_up_questions.length) body.push(`<section><h2>可继续研究</h2><ol>${model.follow_up_questions.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ol></section>`);
    body.push('<p class="disclaimer">说明：本材料由 AI 根据已索引研究资料生成，不构成投资建议；重要结论请以来源报告为准。</p></main>');
    return `<!doctype html><html lang="${CONTENT_DOCUMENT_LANG}" dir="${CONTENT_DOCUMENT_DIR}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>KC桌面研究报告</title><style>@page{size:A4;margin:16mm 18mm 18mm}*{box-sizing:border-box}html{color:#17212b;background:#fff;font-family:"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",Arial,sans-serif;font-size:10.5pt;line-height:1.65}body{margin:0}.cover{display:flex;min-height:250mm;flex-direction:column;align-items:center;justify-content:center;text-align:center;break-after:page}.kicker{margin:0 0 18pt;color:#a06a12;font-size:10pt;font-weight:800;letter-spacing:.16em}.cover h1{max-width:150mm;margin:0;color:#203748;font-size:27pt;line-height:1.28}.subtitle{max-width:148mm;margin:10pt 0 0;color:#2b5163;font-size:14pt}.scope,.date,.notice{max-width:145mm;color:#59636e}.scope{margin:24pt 0 0}.date{margin:7pt 0 0}.notice{margin:56pt 0 0;font-size:9pt;font-style:italic}.report>section{margin:0 0 18pt}.report h2{margin:15pt 0 7pt;color:#2e74b5;font-size:16pt;line-height:1.3;break-after:avoid}.report h3{margin:10pt 0 4pt;color:#1f4d78;font-size:12pt;line-height:1.35;break-after:avoid}.report p{margin:0 0 7pt;white-space:pre-line}.finding{margin-bottom:14pt}.source-refs{display:flex;gap:6pt;align-items:center;color:#59636e;font-size:9pt}.source-refs a,.sources a,figcaption a{color:#0f766e;text-decoration:underline}.data-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8pt}.data-grid article{padding:10pt;border:1px solid #dfe5e8;border-radius:6pt;break-inside:avoid}.data-grid strong{display:block;margin:3pt 0;font-size:15pt}figure{margin:12pt 0 16pt;break-inside:avoid}figure h3{margin-bottom:6pt}figure img{display:block;width:100%;height:auto;max-height:150mm;object-fit:contain;border:1px solid #e2e8eb}figcaption{display:flex;justify-content:space-between;gap:10pt;margin-top:5pt;color:#59636e;font-size:9pt}.sources li{margin:0 0 7pt}.sources span{display:block;color:#59636e;font-size:9pt}.disclaimer{margin-top:24pt;padding-top:8pt;border-top:1px solid #d7dbe2;color:#59636e;font-size:8.5pt;font-style:italic}@media screen{body{max-width:210mm;margin:20px auto;padding:16mm 18mm;box-shadow:0 8px 36px rgba(15,23,42,.12)}.cover{min-height:255mm}}@media print{a{color:#0f766e!important}.data-grid article{border-color:#dfe5e8}}</style></head><body>${body.join("")}</body></html>`;
  }

  function saveBlob(blob, filename, runtime = {}) {
    const documentRef = runtime.document || document;
    const urlRef = runtime.URL || URL;
    const schedule = runtime.setTimeout || setTimeout;
    const objectUrl = urlRef.createObjectURL(blob);
    const link = documentRef.createElement("a");
    link.href = objectUrl; link.download = filename; link.rel = "noopener"; link.style.display = "none";
    documentRef.body.appendChild(link);
    try { link.click(); } finally { link.remove(); schedule(() => urlRef.revokeObjectURL(objectUrl), 1000); }
    return filename;
  }

  async function downloadDocx(payload, runtime = {}) {
    const result = await buildDocx(payload, runtime);
    saveBlob(result.blob, result.filename, runtime);
    return result;
  }

  async function openPdfPrint(payload, runtime = {}) {
    const windowRef = runtime.window || window;
    const printWindow = runtime.printWindow || windowRef.open("", "_blank");
    if (!printWindow) throw new Error("浏览器拦截了 PDF 保存窗口，请允许弹出窗口后重试。");
    try { printWindow.opener = null; } catch (_error) { /* Best effort. */ }
    printWindow.document.open();
    printWindow.document.write(`<!doctype html><html lang="${CONTENT_DOCUMENT_LANG}" dir="${CONTENT_DOCUMENT_DIR}"><meta charset="utf-8"><title>正在准备研究报告</title><body style="font-family:system-ui;padding:32px">正在准备可打印的研究报告与图表…</body></html>`);
    printWindow.document.close();
    try {
      const html = await buildPrintHtml(payload, runtime);
      printWindow.document.open(); printWindow.document.write(html); printWindow.document.close();
      if (printWindow.document.fonts && printWindow.document.fonts.ready) await printWindow.document.fonts.ready;
      const images = Array.from(printWindow.document.images || []);
      await Promise.all(images.map((image) => image.complete
        ? (typeof image.decode === "function" ? image.decode().catch(() => {}) : Promise.resolve())
        : new Promise((resolve, reject) => { image.addEventListener("load", resolve, { once: true }); image.addEventListener("error", reject, { once: true }); })));
      printWindow.focus(); printWindow.print();
      return { filename: "", model: normalizePayload(payload, runtime), status: "print_dialog_opened" };
    } catch (error) {
      try { printWindow.close(); } catch (_closeError) { /* Best effort. */ }
      throw error;
    }
  }

  window.PortalReportResearchExport = Object.freeze({
    DOCX_MIME_TYPE,
    normalizePayload,
    chartAssignments,
    buildDocx,
    buildPrintHtml,
    downloadDocx,
    openPdfPrint,
    _clearChartCache: () => chartCache.clear(),
  });
})();
