import assert from "node:assert/strict";
import { webcrypto } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appUrl = new URL("../site_src/assets/app.js", import.meta.url);
const stylesUrl = new URL("../site_src/assets/styles.css", import.meta.url);
const [app, styles] = await Promise.all([readFile(appUrl, "utf8"), readFile(stylesUrl, "utf8")]);

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const markerIndex = source.indexOf(marker);
  assert.notEqual(markerIndex, -1, `${name} must exist`);
  const start = source.slice(Math.max(0, markerIndex - 6), markerIndex) === "async "
    ? markerIndex - 6
    : markerIndex;
  const bodyStart = source.indexOf("{", source.indexOf(")", markerIndex));
  let depth = 0;
  let quote = "";
  let escaped = false;
  for (let index = bodyStart; index < source.length; index += 1) {
    const char = source[index];
    if (escaped) {
      escaped = false;
      continue;
    }
    if (quote && char === "\\") {
      escaped = true;
      continue;
    }
    if (quote) {
      if (char === quote) quote = "";
      continue;
    }
    if (["'", '"', "`"].includes(char)) {
      quote = char;
      continue;
    }
    if (char === "{") depth += 1;
    else if (char === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function eventTarget() {
  const listeners = new Map();
  return {
    addEventListener(type, listener) {
      const values = listeners.get(type) || [];
      values.push(listener);
      listeners.set(type, values);
    },
    emit(type, event = {}) {
      for (const listener of listeners.get(type) || []) listener(event);
    },
  };
}

test("admin PDF transport reports real progress, sets idempotency headers, and has a five-minute bound", async () => {
  let request;
  class FakeXhr {
    constructor() {
      request = this;
      this.upload = eventTarget();
      this.events = eventTarget();
      this.headers = {};
      this.status = 0;
      this.response = null;
      this.responseText = "";
    }
    open(method, url) { this.method = method; this.url = url; }
    setRequestHeader(name, value) { this.headers[name] = value; }
    addEventListener(type, listener) { this.events.addEventListener(type, listener); }
    send(body) { this.body = body; }
    abort() { this.events.emit("abort"); }
  }
  const progress = [];
  let transportComplete = 0;
  const sandbox = {
    XMLHttpRequest: FakeXhr,
    ADMIN_PDF_UPLOAD_XHR_TIMEOUT_MS: 300000,
  };
  const upload = vm.runInNewContext(`(${extractFunction(app, "xhrAdminPdfUpload")})`, sandbox);
  const transfer = upload("/api/account-admin/hot-report", { form: true }, {
    headers: { "X-Upload-ID": "uuid", "X-Upload-Fingerprint": "a".repeat(64) },
    onProgress(loaded, total) { progress.push([loaded, total]); },
    onTransportComplete() { transportComplete += 1; },
  });

  assert.equal(request.method, "POST");
  assert.equal(request.timeout, 300000);
  assert.equal(request.headers["X-Upload-ID"], "uuid");
  assert.equal(request.headers["X-Upload-Fingerprint"], "a".repeat(64));
  request.upload.emit("progress", { loaded: 5, total: 10, lengthComputable: true });
  request.upload.emit("load");
  request.status = 201;
  request.response = { ok: true, item: { id: "hot:test" } };
  request.events.emit("load");
  assert.deepEqual(progress, [[5, 10]]);
  assert.equal(transportComplete, 1);
  assert.equal((await transfer.promise).item.id, "hot:test");
});

test("upload status lookup aborts a hung request instead of freezing polling", async () => {
  const sandbox = {
    AbortController,
    ADMIN_PDF_UPLOAD_STATUS_TIMEOUT_MS: 1,
    authHeaders() { return { Authorization: "Bearer admin" }; },
    window: { setTimeout, clearTimeout },
    fetch(_url, options) {
      return new Promise((_resolve, reject) => {
        options.signal.addEventListener("abort", () => reject(new DOMException("aborted", "AbortError")));
      });
    },
  };
  const check = vm.runInNewContext(`(${extractFunction(app, "fetchAdminPdfUploadStatus")})`, sandbox);
  await assert.rejects(check("/api", "123e4567-e89b-42d3-a456-426614174000"), (error) => {
    assert.equal(error.name, "TimeoutError");
    assert.match(error.message, /不要重复上传/u);
    return true;
  });
});

test("upload fingerprints are deterministic SHA-256 values bound to target and file metadata", async () => {
  const fingerprint = vm.runInNewContext(`(${extractFunction(app, "adminPdfUploadFingerprint")})`, {
    crypto: webcrypto,
    TextEncoder,
    Uint8Array,
  });
  const file = { name: "report.pdf", size: 1024, lastModified: 1234 };
  const first = await fingerprint("hot-report", "", "", file);
  const same = await fingerprint("hot-report", "", "", file);
  const other = await fingerprint("text-only-pdf", "catalog", "42", file);
  assert.match(first, /^[a-f0-9]{64}$/u);
  assert.equal(first, same);
  assert.notEqual(first, other);
});

test("session recovery persists only upload id and non-sensitive metadata", () => {
  const values = new Map();
  const sandbox = {
    ADMIN_PDF_UPLOAD_SESSION_KEY: "pending",
    ADMIN_PDF_UPLOAD_SESSION_VERSION: 1,
    sessionStorage: {
      getItem(key) { return values.get(key) || null; },
      setItem(key, value) { values.set(key, value); },
      removeItem(key) { values.delete(key); },
    },
  };
  vm.runInNewContext([
    extractFunction(app, "isAdminPdfUploadId"),
    extractFunction(app, "normalizeAdminPdfUploadSession"),
    extractFunction(app, "readAdminPdfUploadSession"),
    extractFunction(app, "writeAdminPdfUploadSession"),
  ].join("\n"), sandbox);
  sandbox.writeAdminPdfUploadSession({
    upload_id: "123e4567-e89b-42d3-a456-426614174000",
    mode: "request",
    state: "processing",
    started_at: 1000,
    file_size: 2048,
    source: "authority",
    target_id: "foreign:42",
    requester_email: "private@example.com",
    title: "private title",
    filename: "private.pdf",
  });
  const persisted = JSON.parse(values.get("pending"));
  assert.deepEqual(Object.keys(persisted).sort(), [
    "file_size", "mode", "source", "started_at", "state", "target_id", "upload_id", "version",
  ]);
  assert.equal(persisted.requester_email, undefined);
  assert.equal(persisted.filename, undefined);
  assert.equal(sandbox.readAdminPdfUploadSession().target_id, "foreign:42");
});

test("a server-declared failed upload clears recovery and assigns a fresh file upload id", async () => {
  let cleared = 0;
  let reset = 0;
  let statusText = "";
  const sandbox = {
    normalizeAdminPdfUploadSession(value) { return value; },
    renderAdminPdfUploadUi() {},
    async fetchAdminPdfUploadStatus() {
      return { upload: { status: "failed", detail: "PDF 校验失败" } };
    },
    completedAdminPdfUploadPayload() { return null; },
    clearAdminPdfUploadSession() { cleared += 1; },
    resetAdminPdfUploadId() { reset += 1; },
    writeAdminPdfUploadSession() {},
    adminPdfUploadStageText() { return "processing"; },
    adminPdfUploadElapsedText() { return "1 秒"; },
  };
  const check = vm.runInNewContext(`(${extractFunction(app, "checkAdminPdfUploadResult")})`, sandbox);
  await check("/api", {
    upload_id: "123e4567-e89b-42d3-a456-426614174000",
    mode: "hot-report",
    state: "processing",
    started_at: 1,
  }, {
    prefix: "upload",
    fileInput: {},
    setStatus(message) { statusText = message; },
  });
  assert.equal(cleared, 1);
  assert.equal(reset, 1);
  assert.match(statusText, /新的上传编号/u);
});

test("request queue uses one mixed-source cursor request and fetches later pages only on demand", async () => {
  const calls = [];
  const sandbox = {
    URLSearchParams,
    authHeaders() { return { Authorization: "Bearer admin" }; },
    async fetch(url) {
      calls.push(String(url));
      return {
        ok: true,
        async json() {
          return {
            items: [{ request_id: "r-2", report_id: "foreign:2", source: "authority" }],
            total: 41,
            has_more: true,
            next_cursor: "request:40",
            index_rebuilding: true,
            migration_complete: false,
            repair_pending: true,
          };
        },
      };
    },
  };
  const load = vm.runInNewContext(`(${extractFunction(app, "fetchAdminReportRequestQueue")})`, sandbox);
  const first = await load("/api", "robotics");
  assert.equal(calls.length, 1);
  assert.doesNotMatch(calls[0], /[?&]source=/u, "mixed queue must not issue one full request per source");
  assert.doesNotMatch(calls[0], /cursor=/u, "first page must not invent a cursor");
  assert.equal(first.next_cursor, "request:40");
  assert.equal(first.partial_index, true, "an unfinished request index must be exposed to the UI");
  assert.equal(first.index_rebuilding, true);
  assert.equal(first.migration_complete, false);
  assert.equal(first.repair_pending, true);
  await load("/api", "robotics", { cursor: first.next_cursor });
  assert.equal(calls.length, 2, "the next page is fetched only after an explicit second call");
  assert.match(calls[1], /cursor=request%3A40/u);

  const identity = vm.runInNewContext(`(${extractFunction(app, "requestIntakeIdentity")})`);
  const queueItem = { source: "authority", report_id: "foreign:2", request_id: "r-2" };
  const searchItem = { source: "authority", id: "foreign:2", target_token: "signed" };
  assert.equal(identity(queueItem), identity(searchItem), "queue and active-search variants share one dedupe identity");
});

test("Twotigers storage metadata shows contact count and quota only when the backend provides it", () => {
  const storageText = vm.runInNewContext(`(() => {
    ${extractFunction(app, "formatSize")}
    ${extractFunction(app, "contactReportStorageMetaText")}
    return contactReportStorageMetaText;
  })()`);
  assert.equal(storageText({}), "", "legacy storage responses must not gain an empty contact segment");
  assert.equal(storageText({ total_size_bytes: 1024 }), "", "unrelated storage fields stay compatible");
  assert.equal(
    storageText({
      contact_report_size_bytes: 12 * 1024 * 1024,
      contact_report_limit_bytes: 2 * 1024 * 1024 * 1024,
      contact_report_count: 7,
    }),
    "7 contact reports · 12.0 MB / 2.0 GB contact archive",
  );
  assert.equal(
    storageText({
      contact_report_size_bytes: 0,
      contact_report_limit_bytes: 2 * 1024 * 1024 * 1024,
      contact_report_count: 0,
    }),
    "0 contact reports · 0 B / 2.0 GB contact archive",
    "provided zero values are real metadata rather than missing fields",
  );
});

test("catalog/contact intake search forwards the requested page and legacy queue uploads keep both proofs", async () => {
  const calls = [];
  const search = vm.runInNewContext(`(${extractFunction(app, "fetchAdminPdfIntakeCandidates")})`, {
    URLSearchParams,
    authHeaders() { return { Authorization: "Bearer admin" }; },
    async fetch(url) {
      calls.push(String(url));
      return {
        ok: true,
        async json() { return { items: [], page: 2, has_more: false }; },
      };
    },
  });
  await search("/api", "authority", "robotics", { page: 2 });
  assert.match(calls[0], /source=authority/u);
  assert.match(calls[0], /page=2/u);

  const build = vm.runInNewContext(`(${extractFunction(app, "buildContactReportUploadFormData")})`, { FormData });
  const pdf = new File(["%PDF-1.7"], "legacy.pdf", { type: "application/pdf" });
  const legacy = build({
    source: "authority",
    report_id: "foreign:42",
    request_id: "legacy-request",
    target_token: "legacy-target-proof",
    title: "Legacy request",
  }, pdf).formData;
  assert.equal(legacy.get("request_id"), "legacy-request");
  assert.equal(legacy.get("target_token"), "legacy-target-proof");
  assert.equal(legacy.get("origin_id"), "foreign:42");

  const verified = build({
    source: "report-a",
    report_id: "report-a:verified_row",
    request_id: "verified-request",
  }, pdf).formData;
  assert.equal(verified.get("request_id"), "verified-request");
  assert.equal(verified.get("target_token"), null, "new verified requests do not require a redundant token");
});

test("contact request token survives search link, new page parsing, detail fetch, and report request POST", async () => {
  const elements = new Map();
  const calls = [];
  function control(id, value = "") {
    const listeners = new Map();
    return {
      id,
      value,
      disabled: false,
      readOnly: false,
      textContent: "",
      className: "",
      addEventListener(type, listener) { listeners.set(type, listener); },
      focus() {},
      async submit() {
        const listener = listeners.get("submit");
        assert.ok(listener, "report request submit listener must be installed");
        await listener({ preventDefault() {} });
      },
    };
  }
  elements.set("reportRequestForm", control("reportRequestForm"));
  elements.set("reportRequesterEmail", control("reportRequesterEmail", "reader@example.com"));
  elements.set("reportRequestWebsite", control("reportRequestWebsite"));
  elements.set("reportRequestSubmit", control("reportRequestSubmit"));
  elements.set("reportRequestStatus", control("reportRequestStatus"));

  const context = vm.createContext({
    URL,
    URLSearchParams,
    window: { location: { href: "https://portal.example.invalid/" } },
    document: { getElementById(id) { return elements.get(id) || null; } },
    AUTHORITY_SOURCE: "authority",
    REPORT_A_SOURCE: "report-a",
    THINKTANK_SOURCE: "thinktank",
    HOT_REPORT_SOURCE: "hot",
    EXTERNAL_SOURCE: "external",
    CONTACT_EMAIL: "support@portal.example.invalid",
    publicBrandText(value) { return String(value || ""); },
    publicDocItem(item) { return item; },
    cachedDocItem() { return null; },
    validDocId() { return true; },
    isHotReportItem() { return false; },
    isThinkTankItem() { return false; },
    isAuthorityItem(item) { return item && item.source === "authority"; },
    isReportAItem(item) { return item && item.source === "report-a"; },
    isContactOnlyItem(item) { return ["authority", "report-a"].includes(item && item.source); },
    rememberDocItem() {},
    loadAuthSession() { return null; },
    authHeaders() { return { Authorization: "Bearer member" }; },
    currentAnalyticsPath() { return "/doc.html"; },
    analyticsReportPayload() { return {}; },
    trackEvent() {},
    async fetch(url, init = {}) {
      calls.push({ url: String(url), init });
      if (String(url).includes("/contact-report/item?")) {
        return {
          ok: true,
          status: 200,
          async json() {
            return { item: { id: "report-a:robotics_2026", title: "Robotics report", availability: "contact_only" } };
          },
        };
      }
      return {
        ok: true,
        status: 200,
        async json() { return { ok: true, detail: "申请已提交。", deduplicated: false }; },
      };
    },
  });
  vm.runInContext(`
    ${extractFunction(app, "hasMeaningfulDocTitle")}
    ${extractFunction(app, "mergeDocItemMetadata")}
    ${extractFunction(app, "reportRequestTitle")}
    ${extractFunction(app, "externalPageUrl")}
    ${extractFunction(app, "externalItemFromParams")}
    ${extractFunction(app, "fetchDocDetailItem")}
    ${extractFunction(app, "initReportRequest")}
    globalThis.buildUrl = externalPageUrl;
    globalThis.fromParams = externalItemFromParams;
    globalThis.fetchDetail = fetchDocDetailItem;
    globalThis.initRequest = initReportRequest;
  `, context);

  const searchItem = {
    id: "report-a:robotics_2026",
    source: "report-a",
    title: "Robotics report",
    request_token: "signed-search-request-token",
  };
  const resultUrl = new URL(context.buildUrl(searchItem, ""));
  assert.equal(resultUrl.searchParams.get("rt"), "signed-search-request-token");
  const pageItem = context.fromParams(resultUrl.searchParams);
  assert.equal(pageItem.request_token, "signed-search-request-token");

  const detailItem = await context.fetchDetail("/api", pageItem);
  assert.match(calls[0].url, /request_token=signed-search-request-token/u);
  assert.equal(detailItem.request_token, "signed-search-request-token", "detail merge must retain the in-memory token");
  assert.equal(detailItem.__detail_fetched, true);
  const canonicalUrl = new URL(context.buildUrl(detailItem, "", { compact: true }));
  assert.equal(canonicalUrl.searchParams.has("rt"), false, "the verified short URL must no longer expose the token");

  context.initRequest("/api", detailItem);
  await elements.get("reportRequestForm").submit();
  assert.equal(calls[1].url, "/api/report-request");
  assert.equal(JSON.parse(calls[1].init.body).request_token, "signed-search-request-token");
});

function fakeElement(id = "") {
  const element = {
    id,
    dataset: {},
    hidden: false,
    disabled: false,
    required: false,
    value: "",
    textContent: "",
    className: "",
    tabIndex: 0,
    validity: { valid: true },
    style: {},
    addEventListener() {},
    setAttribute() {},
    remove() {},
    focus() {},
    querySelector() { return fakeElement(`${id}-child`); },
    querySelectorAll() { return []; },
    closest() { return null; },
  };
  element.classList = {
    add() {}, remove() {}, toggle() {}, contains() { return false; },
  };
  return element;
}

test("account popup and Twotigers admin initialize in their own runtime scopes", async () => {
  const elements = new Map();
  const get = (id) => {
    if (!elements.has(id)) elements.set(id, fakeElement(id));
    return elements.get(id);
  };
  const tabs = ["new", "catalog", "request"].map((mode) => {
    const tab = fakeElement(`tab-${mode}`);
    tab.dataset.adminIntakeMode = mode;
    return tab;
  });
  get("accountAdminModal").querySelectorAll = (selector) => selector === "[data-admin-intake-mode]" ? tabs : [];
  const document = {
    body: { insertAdjacentHTML() {} },
    getElementById: get,
    addEventListener() {},
  };
  const common = {
    document,
    window: { alert() {}, clearInterval, setInterval },
    accountModalMarkup() { return ""; },
    loadAuthSession() { return null; },
    loadAccountCaptcha() { return Promise.resolve("captcha"); },
    localizedContactText(value) { return String(value || ""); },
  };
  const showAccount = vm.runInNewContext(`(${extractFunction(app, "showAccountModal")})`, common);
  await assert.doesNotReject(showAccount("/api"));

  const adminSandbox = {
    document,
    Map,
    Promise,
    clearTimeout,
    accountAdminLastSummaryOwner: "",
    accountAdminLastSummary: null,
    accountAdminRefreshTimer: null,
    accountAdminListModalCleanup: null,
    accountAdminHotReports: [],
    accountAdminMarketViews: new Map(),
    accountAdminDailyPicks: new Map(),
    canOpenOperationsPanel() { return true; },
    loadAuthSession() { return { user: { email: "admin@example.com" } }; },
    isOperatorSession() { return false; },
    isSuperSession() { return true; },
    accountAdminModalMarkup() { return ""; },
    readAdminPdfUploadSession() { return null; },
    shanghaiDateInputValue() { return "2026-08-27"; },
    loadAccountAdminSummary() { return Promise.resolve({}); },
    loadAccountAdminMarketViews() { return Promise.resolve([]); },
    loadAdminHotReports() { return Promise.resolve([]); },
    loadAdminReportChatHistory() { return Promise.resolve([]); },
    renderAdminUsersVerificationState() {},
    loadFreshAdminUsers() { return Promise.resolve({ users: [] }); },
  };
  const showAdmin = vm.runInNewContext(`(${extractFunction(app, "showAccountAdminModal")})`, adminSandbox);
  assert.doesNotThrow(() => showAdmin("/api"));
  await new Promise((resolve) => setImmediate(resolve));
});

test("unified intake and contact availability UI cover every supported source without exposing a naked PDF link", () => {
  assert.match(app, /PDF 入库中心/u);
  assert.match(app, /Text only、已声明有 PDF 但对象缺失或归档失效的 Catalog 报告、报告A、高权报告/u);
  assert.match(app, /External 与国际智库的临时准备失败不会被当作永久缺失/u);
  assert.match(app, /account-admin\/pdf-intake-search/u);
  assert.match(app, /account-admin\/report-requests/u);
  assert.match(app, /account-admin\/contact-report-pdf/u);
  assert.match(app, /data-admin-intake-more="catalog"/u);
  assert.match(app, /data-admin-intake-more="request"/u);
  assert.match(app, /data-admin-intake-search-more=/u);
  assert.match(app, /申请队列正在后台建立索引，已展示部分结果，请稍后刷新\/加载。/u);
  assert.match(app, /contactReportStorageMetaText\(internalStorageMetadata\)/u);
  assert.match(app, /requestIntakeByIdentity\.has\(identity\)/u);
  assert.match(app, /上一笔 PDF 上传结果尚未确认/u);
  assert.match(app, /formData\.set\("target_token", targetToken\)/u);
  assert.match(app, /request_token: requestToken/u);
  assert.match(app, /url\.searchParams\.set\("rt", requestToken/u);
  assert.match(app, /params\.set\("request_token", merged\.request_token\)/u);
  assert.match(app, /compact: isContactOnlyItem\(item\) && item\.__detail_fetched === true/u);
  assert.match(app, /contact-report\/item/u);
  assert.match(app, /contact-report\/pdf\?/u);
  assert.match(app, /3个月及以上会员登录后可直接下载全文/u);
  assert.doesNotMatch(app, /href="\$\{[^}]*download_url/u);
  assert.match(app, /\^report-a:\[A-Za-z0-9_-\]\{1,180\}\$/u);
  assert.match(styles, /\.account-admin-upload-progress/u);
  assert.match(styles, /@keyframes account-admin-upload-processing/u);
  assert.match(styles, /\.account-admin-intake-more/u);
  assert.match(styles, /@media\s*\(prefers-color-scheme:\s*dark\)/u);
});
