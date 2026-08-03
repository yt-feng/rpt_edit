import assert from "node:assert/strict";
import { Buffer } from "node:buffer";
import { readFile } from "node:fs/promises";
import test from "node:test";

const moduleUrl = new URL("../site_src/assets/xlsx-export.js", import.meta.url);
const moduleSource = await readFile(moduleUrl, "utf8");
const xlsx = await import(`data:text/javascript;base64,${Buffer.from(moduleSource).toString("base64")}`);

const COLUMNS = [
  { header: "用户名", key: "username", width: 16 },
  { header: "邮箱", key: "email", width: 28 },
  { header: "状态", key: "status", width: 10 },
  { header: "账号", key: "account", width: 12 },
  { header: "下载权限", key: "access", width: 22 },
  { header: "到期", key: "expires", width: 12 },
  { header: "注册", key: "created", width: 12 },
  { header: "最近登录", key: "lastLogin", width: 18 },
  { header: "操作", key: "actions", width: 14 },
];
const OPTIONS = {
  columns: COLUMNS,
  rows: [
    {
      username: "小一",
      email: "17372527191@163.com",
      status: "正常",
      account: "free",
      access: "机构 1",
      expires: "2027-07-22",
      created: "2026-07-06",
      lastLogin: "2026-07-22 07:35",
      actions: "编辑；禁用",
    },
    {
      username: "=1+1",
      email: "  +cmd@example.com",
      status: "\u0000正常\u000B",
      account: "@SUM(A1:A2)",
      access: "\t=cmd|' /C calc'!A0",
      expires: "<长期&\"'>",
      created: "2026-07-22",
      lastLogin: "2026-07-22 15:30",
      actions: "-HYPERLINK(\"https://example.test\")",
    },
  ],
  sheetName: "用户状态",
  creator: "Portal Suite",
  createdAt: "2026-07-22T07:30:00.000Z",
};

function readUint16(bytes, offset) {
  return new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength).getUint16(offset, true);
}

function readUint32(bytes, offset) {
  return new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength).getUint32(offset, true);
}

function crc32(bytes) {
  let value = 0xFFFFFFFF;
  for (const byte of bytes) {
    value ^= byte;
    for (let bit = 0; bit < 8; bit += 1) {
      value = value & 1 ? 0xEDB88320 ^ (value >>> 1) : value >>> 1;
    }
  }
  return (value ^ 0xFFFFFFFF) >>> 0;
}

function findEndOfCentralDirectory(bytes) {
  const minimum = Math.max(0, bytes.length - 0xFFFF - 22);
  for (let offset = bytes.length - 22; offset >= minimum; offset -= 1) {
    if (readUint32(bytes, offset) === 0x06054B50) return offset;
  }
  throw new Error("ZIP end-of-central-directory record not found");
}

function readStoredZip(bytes) {
  const decoder = new TextDecoder();
  const endOffset = findEndOfCentralDirectory(bytes);
  assert.equal(readUint16(bytes, endOffset + 4), 0, "single-disk ZIP expected");
  assert.equal(readUint16(bytes, endOffset + 6), 0, "central directory must be on disk zero");
  const entryCount = readUint16(bytes, endOffset + 10);
  const centralSize = readUint32(bytes, endOffset + 12);
  const centralOffset = readUint32(bytes, endOffset + 16);
  const result = new Map();
  let offset = centralOffset;

  for (let index = 0; index < entryCount; index += 1) {
    assert.equal(readUint32(bytes, offset), 0x02014B50, `central record ${index + 1} signature`);
    const method = readUint16(bytes, offset + 10);
    const expectedCrc = readUint32(bytes, offset + 16);
    const compressedSize = readUint32(bytes, offset + 20);
    const uncompressedSize = readUint32(bytes, offset + 24);
    const nameLength = readUint16(bytes, offset + 28);
    const extraLength = readUint16(bytes, offset + 30);
    const commentLength = readUint16(bytes, offset + 32);
    const localOffset = readUint32(bytes, offset + 42);
    const name = decoder.decode(bytes.subarray(offset + 46, offset + 46 + nameLength));

    assert.equal(method, 0, `${name} must use dependency-free ZIP STORE mode`);
    assert.equal(compressedSize, uncompressedSize, `${name} stored size`);
    assert.equal(readUint32(bytes, localOffset), 0x04034B50, `${name} local signature`);
    assert.equal(readUint16(bytes, localOffset + 8), 0, `${name} local compression method`);
    const localNameLength = readUint16(bytes, localOffset + 26);
    const localExtraLength = readUint16(bytes, localOffset + 28);
    const localName = decoder.decode(bytes.subarray(localOffset + 30, localOffset + 30 + localNameLength));
    assert.equal(localName, name, `${name} local and central names`);
    const dataStart = localOffset + 30 + localNameLength + localExtraLength;
    const data = bytes.slice(dataStart, dataStart + compressedSize);
    assert.equal(crc32(data), expectedCrc, `${name} CRC-32`);
    result.set(name, data);
    offset += 46 + nameLength + extraLength + commentLength;
  }

  assert.equal(offset, centralOffset + centralSize, "central directory size");
  return result;
}

test("sanitizeXlsxText removes illegal XML controls and neutralizes formula-like prefixes", () => {
  assert.equal(xlsx.sanitizeXlsxText("安全中文😀"), "安全中文😀");
  assert.equal(xlsx.sanitizeXlsxText("A\u0000B\u000BC"), "ABC");
  assert.equal(xlsx.sanitizeXlsxText("=1+1"), "'=1+1");
  assert.equal(xlsx.sanitizeXlsxText("  @SUM(A1:A2)"), "'  @SUM(A1:A2)");
  assert.equal(xlsx.sanitizeXlsxText("\tcommand"), "'\tcommand");
  assert.equal(xlsx.sanitizeXlsxText("-"), "-");
  assert.equal(xlsx.sanitizeXlsxText("-1"), "'-1");
  assert.equal(xlsx.sanitizeXlsxText("safe+value"), "safe+value");
});

test("buildXlsxWorkbook emits a complete OOXML ZIP with text-only safe cells", async () => {
  const blob = xlsx.buildXlsxWorkbook(OPTIONS);
  assert.equal(blob.type, xlsx.XLSX_MIME_TYPE);
  const bytes = new Uint8Array(await blob.arrayBuffer());
  assert.deepEqual([...bytes.subarray(0, 4)], [0x50, 0x4B, 0x03, 0x04], "XLSX starts with a ZIP local-file header");

  const files = readStoredZip(bytes);
  const requiredFiles = [
    "[Content_Types].xml",
    "_rels/.rels",
    "docProps/app.xml",
    "docProps/core.xml",
    "xl/workbook.xml",
    "xl/_rels/workbook.xml.rels",
    "xl/styles.xml",
    "xl/worksheets/sheet1.xml",
  ];
  for (const name of requiredFiles) assert.ok(files.has(name), `contains ${name}`);

  const decoder = new TextDecoder();
  const workbook = decoder.decode(files.get("xl/workbook.xml"));
  const worksheet = decoder.decode(files.get("xl/worksheets/sheet1.xml"));
  const styles = decoder.decode(files.get("xl/styles.xml"));

  assert.match(workbook, /<sheet name="用户状态" sheetId="1" r:id="rId1"\/>/u);
  assert.match(worksheet, /<dimension ref="A1:I3"\/>/u);
  assert.match(worksheet, /<pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"\/>/u);
  assert.match(worksheet, /<autoFilter ref="A1:I3"\/>/u);
  assert.match(worksheet, /<col min="1" max="1" width="16" customWidth="1"\/>/u);
  assert.match(worksheet, /<col min="2" max="2" width="28" customWidth="1"\/>/u);
  assert.match(styles, /<xf numFmtId="49"/u, "cell style uses Excel's text number format");

  const cells = worksheet.match(/<c\b[^>]*>/gu) || [];
  assert.equal(cells.length, 27, "nine headers and eighteen data cells are present");
  assert.ok(cells.every((cell) => /\bt="inlineStr"/u.test(cell)), "every worksheet cell is explicitly text");
  assert.doesNotMatch(worksheet, /<f(?:\s|>)/u, "worksheet contains no formula elements");
  assert.match(worksheet, /小一/u, "Chinese text survives UTF-8 OOXML encoding");
  assert.match(worksheet, /正常/u, "ordinary Chinese cell text is retained");
  assert.match(worksheet, /&apos;=1\+1/u, "equals-prefixed input is neutralized");
  assert.match(worksheet, /&apos;  \+cmd@example\.com/u, "leading-space plus input is neutralized");
  assert.match(worksheet, /&apos;@SUM\(A1:A2\)/u, "at-sign formula input is neutralized");
  assert.match(worksheet, /&apos;\t=cmd\|&apos; \/C calc&apos;!A0/u, "tab-prefixed input is neutralized and XML escaped");
  assert.match(worksheet, /&lt;长期&amp;&quot;&apos;&gt;/u, "XML metacharacters are escaped");
  assert.ok(!worksheet.includes("\u0000") && !worksheet.includes("\u000B"), "illegal XML controls are removed");
});

test("buildXlsxWorkbook handles an empty table and normalizes a truncated sheet name", async () => {
  const requestedName = `${"甲".repeat(30)}'尾`;
  const blob = xlsx.buildXlsxWorkbook({
    sheetName: requestedName,
    columns: [{ header: "用户名", key: "username", width: 16 }],
    rows: [],
    createdAt: "2026-07-22T00:00:00.000Z",
  });
  const files = readStoredZip(new Uint8Array(await blob.arrayBuffer()));
  const decoder = new TextDecoder();
  const workbook = decoder.decode(files.get("xl/workbook.xml"));
  const worksheet = decoder.decode(files.get("xl/worksheets/sheet1.xml"));
  assert.match(workbook, new RegExp(`<sheet name="${"甲".repeat(30)}" sheetId="1"`, "u"));
  assert.match(worksheet, /<dimension ref="A1:A1"\/>/u);
  assert.match(worksheet, /<autoFilter ref="A1:A1"\/>/u);

  assert.throws(() => xlsx.buildXlsxWorkbook({
    columns: [
      { header: "A", key: "same" },
      { header: "B", key: "same" },
    ],
    rows: [],
  }), /duplicated/u);
});

test("downloadXlsx creates the correct Blob and uses a revocable object URL", async () => {
  const events = [];
  const anchor = {
    style: {},
    click() { events.push("click"); },
    remove() { events.push("remove"); },
  };
  const document = {
    body: {
      appendChild(node) {
        assert.equal(node, anchor);
        events.push("append");
      },
    },
    createElement(tag) {
      assert.equal(tag, "a");
      return anchor;
    },
  };
  let capturedBlob;
  const URL = {
    createObjectURL(blob) {
      capturedBlob = blob;
      events.push("create-url");
      return "blob:test-xlsx";
    },
    revokeObjectURL(url) {
      assert.equal(url, "blob:test-xlsx");
      events.push("revoke-url");
    },
  };
  const setTimeout = (callback, delay) => {
    assert.equal(delay, 1000);
    events.push("schedule-revoke");
    callback();
  };

  const blob = xlsx.buildXlsxWorkbook(OPTIONS);
  const downloadedAs = xlsx.downloadXlsx(blob, "用户/状态", { document, URL, setTimeout });
  assert.equal(downloadedAs, "用户_状态.xlsx");
  assert.equal(anchor.download, "用户_状态.xlsx");
  assert.equal(anchor.href, "blob:test-xlsx");
  assert.equal(blob.type, xlsx.XLSX_MIME_TYPE);
  assert.equal(capturedBlob, blob);
  assert.deepEqual(events, ["create-url", "append", "click", "remove", "schedule-revoke", "revoke-url"]);
  const downloadedBytes = new Uint8Array(await blob.arrayBuffer());
  assert.deepEqual([...downloadedBytes.subarray(0, 4)], [0x50, 0x4B, 0x03, 0x04]);
});
