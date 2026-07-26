const XML_DECLARATION = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>';

export const XLSX_MIME_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

const MAX_COLUMNS = 16384;
const MAX_ROWS = 1048576;
const MAX_CELL_TEXT_LENGTH = 32767;
const DEFAULT_COLUMN_WIDTH = 16;
const FORMULA_LIKE_PREFIX = /^[\s\uFEFF]*[=+\-@]/u;
const CRC32_TABLE = buildCrc32Table();

function buildCrc32Table() {
  const table = new Uint32Array(256);
  for (let index = 0; index < table.length; index += 1) {
    let value = index;
    for (let bit = 0; bit < 8; bit += 1) {
      value = value & 1 ? 0xEDB88320 ^ (value >>> 1) : value >>> 1;
    }
    table[index] = value >>> 0;
  }
  return table;
}

function crc32(bytes) {
  let value = 0xFFFFFFFF;
  for (const byte of bytes) {
    value = CRC32_TABLE[(value ^ byte) & 0xFF] ^ (value >>> 8);
  }
  return (value ^ 0xFFFFFFFF) >>> 0;
}

function toXmlText(value) {
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
    ) {
      result += character;
    }
  }
  return result;
}

/**
 * Convert an arbitrary value into safe worksheet text.
 *
 * Every worksheet cell is also emitted as OOXML `inlineStr`, so Excel cannot
 * interpret it as a formula. The apostrophe is defense in depth for consumers
 * that later copy or convert the cell to CSV.
 */
export function sanitizeXlsxText(value) {
  const text = toXmlText(value);
  if (text === "-") return text;
  if (/^[\t\r\n]/u.test(text) || FORMULA_LIKE_PREFIX.test(text)) return `'${text}`;
  return text;
}

function escapeXml(value) {
  return toXmlText(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

function normalizeSheetName(value) {
  const cleaned = toXmlText(value || "Sheet1")
    .replace(/[\\/*?:[\]]/g, " ")
    .trim()
    .slice(0, 31)
    .replace(/^'+|'+$/g, "")
    .trim();
  return cleaned || "Sheet1";
}

function normalizeDate(value) {
  const date = value === undefined
    ? new Date()
    : (value instanceof Date ? new Date(value.getTime()) : new Date(value));
  if (Number.isNaN(date.getTime())) throw new TypeError("createdAt must be a valid date");
  return date;
}

function excelColumnName(columnIndex) {
  let index = columnIndex;
  let result = "";
  do {
    result = String.fromCharCode(65 + (index % 26)) + result;
    index = Math.floor(index / 26) - 1;
  } while (index >= 0);
  return result;
}

function normalizeColumnWidth(value) {
  const width = Number(value);
  if (!Number.isFinite(width)) return DEFAULT_COLUMN_WIDTH;
  return Math.min(255, Math.max(1, width));
}

function decimal(value) {
  return Number(value.toFixed(2)).toString();
}

function worksheetCellXml(reference, value, styleId) {
  const text = sanitizeXlsxText(value);
  if (text.length > MAX_CELL_TEXT_LENGTH) {
    throw new RangeError(`Cell ${reference} exceeds Excel's ${MAX_CELL_TEXT_LENGTH}-character limit`);
  }
  return `<c r="${reference}" s="${styleId}" t="inlineStr"><is><t xml:space="preserve">${escapeXml(text)}</t></is></c>`;
}

function worksheetXml(headers, rows, columnWidths) {
  const columnCount = headers.length;
  const lastColumn = excelColumnName(columnCount - 1);
  const lastRow = rows.length + 1;
  const range = `A1:${lastColumn}${lastRow}`;
  const widths = Array.from({ length: columnCount }, (_, index) => normalizeColumnWidth(columnWidths[index]));

  const columns = widths.map((width, index) => (
    `<col min="${index + 1}" max="${index + 1}" width="${decimal(width)}" customWidth="1"/>`
  )).join("");

  const rowXml = [headers, ...rows].map((row, rowIndex) => {
    const rowNumber = rowIndex + 1;
    const cells = Array.from({ length: columnCount }, (_, columnIndex) => {
      const reference = `${excelColumnName(columnIndex)}${rowNumber}`;
      return worksheetCellXml(reference, row[columnIndex], rowIndex === 0 ? 1 : 0);
    }).join("");
    const headerHeight = rowIndex === 0 ? ' ht="22" customHeight="1"' : "";
    return `<row r="${rowNumber}" spans="1:${columnCount}"${headerHeight}>${cells}</row>`;
  }).join("");

  return `${XML_DECLARATION}
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <dimension ref="${range}"/>
  <sheetViews>
    <sheetView tabSelected="1" workbookViewId="0">
      <pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/>
      <selection pane="bottomLeft" activeCell="A2" sqref="A2"/>
    </sheetView>
  </sheetViews>
  <sheetFormatPr defaultRowHeight="15"/>
  <cols>${columns}</cols>
  <sheetData>${rowXml}</sheetData>
  <autoFilter ref="${range}"/>
  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3"/>
</worksheet>`;
}

function workbookXml(sheetName) {
  return `${XML_DECLARATION}
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <bookViews><workbookView xWindow="0" yWindow="0" windowWidth="24000" windowHeight="12000"/></bookViews>
  <sheets><sheet name="${escapeXml(sheetName)}" sheetId="1" r:id="rId1"/></sheets>
</workbook>`;
}

function stylesXml() {
  return `${XML_DECLARATION}
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="2">
    <font><sz val="11"/><color rgb="FF000000"/><name val="Arial"/><family val="2"/></font>
    <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Arial"/><family val="2"/></font>
  </fonts>
  <fills count="3">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color rgb="FFD9E2F3"/></left>
      <right style="thin"><color rgb="FFD9E2F3"/></right>
      <top style="thin"><color rgb="FFD9E2F3"/></top>
      <bottom style="thin"><color rgb="FFD9E2F3"/></bottom>
      <diagonal/>
    </border>
  </borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="2">
    <xf numFmtId="49" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"><alignment vertical="center"/></xf>
    <xf numFmtId="49" fontId="1" fillId="2" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center"/></xf>
  </cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
  <dxfs count="0"/>
  <tableStyles count="0" defaultTableStyle="TableStyleMedium2" defaultPivotStyle="PivotStyleLight16"/>
</styleSheet>`;
}

function corePropertiesXml(creator, createdAt) {
  const escapedCreator = escapeXml(creator || "KC Desk Notes");
  const timestamp = createdAt.toISOString();
  return `${XML_DECLARATION}
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:creator>${escapedCreator}</dc:creator>
  <cp:lastModifiedBy>${escapedCreator}</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">${timestamp}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">${timestamp}</dcterms:modified>
</cp:coreProperties>`;
}

function appPropertiesXml(sheetName) {
  return `${XML_DECLARATION}
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>KC Desk Notes XLSX Export</Application>
  <DocSecurity>0</DocSecurity>
  <ScaleCrop>false</ScaleCrop>
  <HeadingPairs><vt:vector size="2" baseType="variant"><vt:variant><vt:lpstr>Worksheets</vt:lpstr></vt:variant><vt:variant><vt:i4>1</vt:i4></vt:variant></vt:vector></HeadingPairs>
  <TitlesOfParts><vt:vector size="1" baseType="lpstr"><vt:lpstr>${escapeXml(sheetName)}</vt:lpstr></vt:vector></TitlesOfParts>
  <Company></Company>
  <LinksUpToDate>false</LinksUpToDate>
  <SharedDoc>false</SharedDoc>
  <HyperlinksChanged>false</HyperlinksChanged>
  <AppVersion>1.0</AppVersion>
</Properties>`;
}

function contentTypesXml() {
  return `${XML_DECLARATION}
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>`;
}

function rootRelationshipsXml() {
  return `${XML_DECLARATION}
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>`;
}

function workbookRelationshipsXml() {
  return `${XML_DECLARATION}
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>`;
}

function concatBytes(parts) {
  const length = parts.reduce((total, part) => total + part.length, 0);
  const result = new Uint8Array(length);
  let offset = 0;
  for (const part of parts) {
    result.set(part, offset);
    offset += part.length;
  }
  return result;
}

function dosTimestamp(date) {
  let year = date.getUTCFullYear();
  let month = date.getUTCMonth() + 1;
  let day = date.getUTCDate();
  let hours = date.getUTCHours();
  let minutes = date.getUTCMinutes();
  let seconds = date.getUTCSeconds();
  if (year < 1980) {
    year = 1980;
    month = 1;
    day = 1;
    hours = 0;
    minutes = 0;
    seconds = 0;
  } else if (year > 2107) {
    year = 2107;
    month = 12;
    day = 31;
    hours = 23;
    minutes = 59;
    seconds = 58;
  }
  return {
    time: (hours << 11) | (minutes << 5) | Math.floor(seconds / 2),
    date: ((year - 1980) << 9) | (month << 5) | day,
  };
}

function storedZip(files, createdAt) {
  if (files.length > 0xFFFF) throw new RangeError("ZIP contains too many files");
  const encoder = new TextEncoder();
  const timestamp = dosTimestamp(createdAt);
  const localRecords = [];
  const centralMetadata = [];
  let localOffset = 0;

  for (const file of files) {
    const name = encoder.encode(file.name);
    const data = typeof file.data === "string" ? encoder.encode(file.data) : file.data;
    if (!(data instanceof Uint8Array)) throw new TypeError(`ZIP entry ${file.name} must be text or Uint8Array`);
    if (data.length > 0xFFFFFFFF || localOffset > 0xFFFFFFFF) throw new RangeError("ZIP64 is not supported");
    const checksum = crc32(data);
    const header = new Uint8Array(30);
    const view = new DataView(header.buffer);
    view.setUint32(0, 0x04034B50, true);
    view.setUint16(4, 20, true);
    view.setUint16(6, 0x0800, true);
    view.setUint16(8, 0, true);
    view.setUint16(10, timestamp.time, true);
    view.setUint16(12, timestamp.date, true);
    view.setUint32(14, checksum, true);
    view.setUint32(18, data.length, true);
    view.setUint32(22, data.length, true);
    view.setUint16(26, name.length, true);
    view.setUint16(28, 0, true);
    const record = concatBytes([header, name, data]);
    localRecords.push(record);
    centralMetadata.push({ name, dataLength: data.length, checksum, localOffset });
    localOffset += record.length;
  }

  const centralRecords = centralMetadata.map((entry) => {
    const header = new Uint8Array(46);
    const view = new DataView(header.buffer);
    view.setUint32(0, 0x02014B50, true);
    view.setUint16(4, 20, true);
    view.setUint16(6, 20, true);
    view.setUint16(8, 0x0800, true);
    view.setUint16(10, 0, true);
    view.setUint16(12, timestamp.time, true);
    view.setUint16(14, timestamp.date, true);
    view.setUint32(16, entry.checksum, true);
    view.setUint32(20, entry.dataLength, true);
    view.setUint32(24, entry.dataLength, true);
    view.setUint16(28, entry.name.length, true);
    view.setUint16(30, 0, true);
    view.setUint16(32, 0, true);
    view.setUint16(34, 0, true);
    view.setUint16(36, 0, true);
    view.setUint32(38, 0, true);
    view.setUint32(42, entry.localOffset, true);
    return concatBytes([header, entry.name]);
  });

  const centralSize = centralRecords.reduce((total, record) => total + record.length, 0);
  if (centralSize > 0xFFFFFFFF || localOffset + centralSize > 0xFFFFFFFF) {
    throw new RangeError("ZIP64 is not supported");
  }
  const end = new Uint8Array(22);
  const endView = new DataView(end.buffer);
  endView.setUint32(0, 0x06054B50, true);
  endView.setUint16(4, 0, true);
  endView.setUint16(6, 0, true);
  endView.setUint16(8, files.length, true);
  endView.setUint16(10, files.length, true);
  endView.setUint32(12, centralSize, true);
  endView.setUint32(16, localOffset, true);
  endView.setUint16(20, 0, true);
  return concatBytes([...localRecords, ...centralRecords, end]);
}

function normalizeTable(options) {
  if (!options || !Array.isArray(options.columns) || options.columns.length === 0) {
    throw new TypeError("columns must be a non-empty array");
  }
  if (options.columns.length > MAX_COLUMNS) throw new RangeError(`Excel supports at most ${MAX_COLUMNS} columns`);
  const seenKeys = new Set();
  const columns = options.columns.map((column, index) => {
    if (!column || typeof column !== "object" || Array.isArray(column)) {
      throw new TypeError(`Column ${index + 1} must be an object`);
    }
    const key = String(column.key || "").trim();
    if (!key) throw new TypeError(`Column ${index + 1} must have a key`);
    if (seenKeys.has(key)) throw new TypeError(`Column key ${key} is duplicated`);
    seenKeys.add(key);
    return {
      header: column.header === null || column.header === undefined ? "" : String(column.header),
      key,
      width: normalizeColumnWidth(column.width),
    };
  });
  const rows = options.rows === undefined ? [] : options.rows;
  if (!Array.isArray(rows)) throw new TypeError("rows must be an array");
  if (rows.length + 1 > MAX_ROWS) throw new RangeError(`Excel supports at most ${MAX_ROWS} rows`);
  rows.forEach((row, index) => {
    if (!row || typeof row !== "object" || Array.isArray(row)) {
      throw new TypeError(`Row ${index + 1} must be an object`);
    }
  });
  return {
    headers: columns.map((column) => column.header),
    rows: rows.map((row) => columns.map((column) => row[column.key])),
    columnWidths: columns.map((column) => column.width),
  };
}

function createXlsxBytes(options) {
  const { headers, rows, columnWidths } = normalizeTable(options);
  const sheetName = normalizeSheetName(options.sheetName || "用户状态");
  const createdAt = normalizeDate(options.createdAt);
  const files = [
    { name: "[Content_Types].xml", data: contentTypesXml() },
    { name: "_rels/.rels", data: rootRelationshipsXml() },
    { name: "docProps/app.xml", data: appPropertiesXml(sheetName) },
    { name: "docProps/core.xml", data: corePropertiesXml(options.creator, createdAt) },
    { name: "xl/workbook.xml", data: workbookXml(sheetName) },
    { name: "xl/_rels/workbook.xml.rels", data: workbookRelationshipsXml() },
    { name: "xl/styles.xml", data: stylesXml() },
    { name: "xl/worksheets/sheet1.xml", data: worksheetXml(headers, rows, columnWidths) },
  ];
  return storedZip(files, createdAt);
}

/** Build a standards-based, dependency-free XLSX workbook as a Blob. */
export function buildXlsxWorkbook(options) {
  if (typeof Blob !== "function") throw new Error("Blob is not available in this environment");
  return new Blob([createXlsxBytes(options)], { type: XLSX_MIME_TYPE });
}

function normalizeFilename(value) {
  let filename = toXmlText(value || "export.xlsx")
    .replace(/[<>:"/\\|?*]/g, "_")
    .replace(/[. ]+$/g, "")
    .trim();
  if (!filename) filename = "export";
  if (!/\.xlsx$/i.test(filename)) filename += ".xlsx";
  if (filename.length > 180) filename = `${filename.slice(0, 175)}.xlsx`;
  return filename;
}

/** Trigger a browser download for an XLSX Blob. */
export function downloadXlsx(blob, filename = "export.xlsx", runtime = {}) {
  if (!blob || typeof blob.arrayBuffer !== "function") {
    throw new TypeError("blob must be a Blob");
  }
  const documentRef = runtime.document || globalThis.document;
  const urlRef = runtime.URL || globalThis.URL;
  const schedule = runtime.setTimeout || globalThis.setTimeout;
  if (!documentRef || !documentRef.body || typeof documentRef.createElement !== "function") {
    throw new Error("A browser document is required to download XLSX files");
  }
  if (!urlRef || typeof urlRef.createObjectURL !== "function" || typeof urlRef.revokeObjectURL !== "function") {
    throw new Error("Browser object URL support is required to download XLSX files");
  }
  const safeFilename = normalizeFilename(filename);
  const objectUrl = urlRef.createObjectURL(blob);
  const link = documentRef.createElement("a");
  link.href = objectUrl;
  link.download = safeFilename;
  link.rel = "noopener";
  if (link.style) link.style.display = "none";
  documentRef.body.appendChild(link);
  try {
    link.click();
  } finally {
    if (typeof link.remove === "function") link.remove();
    else if (typeof documentRef.body.removeChild === "function") documentRef.body.removeChild(link);
    const revoke = () => urlRef.revokeObjectURL(objectUrl);
    if (typeof schedule === "function") schedule(revoke, 1000);
    else revoke();
  }
  return safeFilename;
}
