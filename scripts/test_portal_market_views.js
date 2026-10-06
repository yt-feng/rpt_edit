const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const workflow = fs.readFileSync(path.join(root, ".github/workflows/market-views-latex-pdf.yml"), "utf8");
const gitignore = fs.readFileSync(path.join(root, ".gitignore"), "utf8");

function extractFunction(source, name) {
  const starts = [`async function ${name}(`, `function ${name}(`]
    .map((needle) => source.indexOf(needle))
    .filter((index) => index >= 0);
  assert.ok(starts.length, `${name} must exist`);
  const start = Math.min(...starts);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  assert.ok(bodyStart >= 0, `${name} must have a body`);
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

const planDefinitions = worker.match(/const VID2PPT_PORTAL_GIFT_PLANS = \{[\s\S]*?\n\};/);
assert.ok(planDefinitions, "membership plan definitions must exist");

const sandbox = { api: null };
vm.runInNewContext(`
  const TRIAL_3D_DOWNLOAD_LIMIT = 10;
  ${planDefinitions[0]}
  const TRIAL_3D_DURATION_VALUE = "trial_3d";
  const MARKET_VIEW_ID_PATTERN = /^market-view:(\\d{6})$/;
  const MARKET_VIEW_MIN_MONTHS = 1;
  const MARKET_VIEW_REQUIRED_PLAN = "至少1个月会员";
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  function accountDisabled(user) { return Boolean(user && user.disabled); }
  function isPrivilegedAccount(user) { return Boolean(user && user.privileged); }
  function publicAccessGrant(row) { return row && typeof row === "object" ? { ...row } : { active: false, source: "none" }; }
  function publicEntitlement(row) { return row && typeof row === "object" ? { ...row } : { active: false, plan: "free" }; }
  function roleAccessForUser() { return { active: true, lifetime: true, source: "role", access_mode: "all" }; }
  function superEntitlement() { return { active: true, plan: "super" }; }
  async function findEntitlement(env) { return env.entitlement || null; }
  async function findAccessGrant(env) { return env.access || null; }
  async function findVid2PptTrialAccess(env) { return env.trial || null; }
  function effectiveAccessChoiceForUser(_user, entitlement, access) {
    const choices = [];
    if (access && access.active) choices.push({ kind: "admin", access });
    if (entitlement && entitlement.active) choices.push({
      kind: "entitlement",
      access: {
        active: true,
        source: entitlement.source || "entitlement",
        source_plan_code: entitlement.source_plan_code || "",
        duration_value: entitlement.duration_value || "",
        access_mode: "all",
      },
    });
    return { choices };
  }
  function broaderCurrentAccessChoice(left, right) { return right || left; }
  ${extractFunction(worker, "hotReportPlanMonths")}
  ${extractFunction(worker, "hotReportAccessMonths")}
  ${extractFunction(worker, "reportTextAccessQualifies")}
  ${extractFunction(worker, "marketViewMembershipAccessForUser")}
  ${extractFunction(worker, "marketViewDateKeyFromId")}
  ${extractFunction(worker, "marketViewDateIso")}
  api = { marketViewMembershipAccessForUser, marketViewDateKeyFromId, marketViewDateIso };
`, sandbox);

const api = sandbox.api;
const reader = { email: "reader@example.com" };

(async () => {
  const cases = {
    filteredMonth: await api.marketViewMembershipAccessForUser({
      access: { active: true, access_mode: "filters", duration_value: "1", source: "stored" },
    }, reader),
    novaMonth: await api.marketViewMembershipAccessForUser({
      entitlement: { active: true, plan: "annual", source: "vid2ppt_nova", source_plan_code: "NOVA-M" },
    }, reader),
    annual: await api.marketViewMembershipAccessForUser({
      entitlement: { active: true, plan: "annual", source: "entitlement" },
    }, reader),
    lifetime: await api.marketViewMembershipAccessForUser({
      access: { active: true, access_mode: "filters", lifetime: true, source: "stored" },
    }, reader),
    trial: await api.marketViewMembershipAccessForUser({
      access: { active: true, access_mode: "all", duration_value: "trial_3d", source: "stored" },
    }, reader),
    free: await api.marketViewMembershipAccessForUser({}, reader),
    disabled: await api.marketViewMembershipAccessForUser({}, { ...reader, disabled: true }),
    privileged: await api.marketViewMembershipAccessForUser({}, { ...reader, privileged: true }),
  };

  assert.equal(cases.filteredMonth.can_download, true, "a one-month institution-filtered member qualifies");
  assert.equal(cases.novaMonth.can_download, true, "NOVA-M qualifies for Market Views");
  assert.equal(cases.annual.can_download, true, "annual membership qualifies");
  assert.equal(cases.lifetime.can_download, true, "lifetime membership qualifies");
  assert.equal(cases.trial.can_download, false, "the three-day trial does not qualify");
  assert.equal(cases.free.can_download, false, "a free registered account does not qualify");
  assert.equal(cases.disabled.can_download, false, "a disabled account does not qualify");
  assert.equal(cases.privileged.can_download, true, "the administrator qualifies");

  assert.equal(api.marketViewDateKeyFromId("market-view:260801"), "260801");
  assert.equal(api.marketViewDateIso("260229"), "", "invalid calendar dates are rejected");
  assert.equal(api.marketViewDateKeyFromId("market-view:../../secret"), "", "path injection is rejected at the id parser");

  const pdfHandler = extractFunction(worker, "handleMarketViewsPdf");
  assert.match(pdfHandler, /marketViewMembershipAccessForUser\(env, user\)/);
  assert.match(pdfHandler, /env\.REPORT_BUCKET\.get\(key\)/, "paid PDFs must come from private R2");
  assert.doesNotMatch(pdfHandler, /fetchGithubRawFile|market_view_summaries/, "the paid endpoint must not fall back to the public repository");
  assert.doesNotMatch(pdfHandler, /searchParams\.get\("path"\)/, "clients cannot submit a repository or R2 path");
  assert.match(worker, /pathname === "\/market-views\/pdf"[\s\S]*?handleMarketViewsPdf\(request, env\)/);
  assert.doesNotMatch(extractFunction(worker, "listMarketViewItems"), /latestMarketViewFiles|github/i, "the public list must only describe private R2 objects");
  assert.doesNotMatch(worker, /function latestMarketViewFiles/, "the old repository Market Views listing must stay removed");
  for (const functionName of [
    "latestAdminGithubFiles",
    "adminGithubArtifact",
    "isAllowedAdminGithubFile",
    "prepareAdminGithubFileCache",
    "handleAccountAdminGithubArtifact",
  ]) {
    const source = extractFunction(worker, functionName);
    assert.doesNotMatch(source, /market_view_summaries|market-views-pdf/i, `${functionName} must not restore a legacy paid-PDF path`);
  }
  assert.match(extractFunction(worker, "handleAccountAdminGithubArtifact"), /requireSuperUser\(request, env\)/);
  assert.equal((worker.match(/market_view_summaries/g) || []).length, 1, "the only legacy repository token must be the stale-snapshot filter");
  assert.equal((worker.match(/market-views-pdf/gi) || []).length, 1, "the only legacy artifact token must be the stale-snapshot filter");

  const snapshotSandbox = { result: null };
  vm.runInNewContext(`
    function applyAdminVideoContinuityMajority(files) { return files; }
    ${extractFunction(worker, "adminFileGroup")}
    ${extractFunction(worker, "adminFileKey")}
    ${extractFunction(worker, "isLegacyMarketViewAdminFile")}
    ${extractFunction(worker, "groupAdminFiles")}
    ${extractFunction(worker, "mergeAdminFilesWithSnapshot")}
    result = mergeAdminFilesWithSnapshot([], [
      { type: "file", kind: "market-views", path: "market_view_summaries/260801/market_views_260801.pdf" },
      { type: "artifact", kind: "artifact", name: "market-views-pdf-123" },
      { type: "file", kind: "bbg-show", path: "rendered-clips/show/example.mp4" },
    ]);
  `, snapshotSandbox);
  const snapshotResult = JSON.parse(JSON.stringify(snapshotSandbox.result));
  assert.equal(snapshotResult.files.some((file) => /market/i.test(JSON.stringify(file))), false, "legacy Market Views snapshot rows must be discarded");
  assert.equal(snapshotResult.stale_groups.includes("market-views"), false, "legacy Market Views must not survive as a stale group");

  const artifactSteps = workflow.split(/\n      - name: /).filter((step) => /actions\/upload-artifact/.test(step) && !/path: \$\{\{ runner\.temp \}\}\/market-views-native-source-audit\.json/.test(step));
  assert.equal(artifactSteps.length, 1, "only the public-safe acceptance PDF has an artifact step");
  assert.match(artifactSteps[0], /inputs\.acceptance_only == true.*steps\.public_pdf\.conclusion == 'success'/);
  assert.match(artifactSteps[0], /path: market_view_summaries\/\$\{\{ env\.DATE_FOLDER \}\}\/market_views_\$\{\{ env\.DATE_FOLDER \}\}\.pdf/);
  assert.match(workflow, /prepare_public_market_view_pdf\.py/, "the public copy must remove the private ending page");
  assert.match(workflow, /force_rebuild:[\s\S]*?type: boolean[\s\S]*?default: false/, "same-date rebuilds must require an explicit opt-in");
  assert.match(workflow, /force_rebuild=os\.environ\['FORCE_REBUILD'\] == 'true'[\s\S]*?should_build = plan\['should_build'\][\s\S]*?"SHOULD_BUILD": str\(should_build\)\.lower\(\)/, "the validated publication plan must control same-date reuse");
  assert.match(workflow, /Archive exact Market Views PDF in private R2\n\s*if: \$\{\{ env\.SHOULD_BUILD != 'false' && inputs\.acceptance_only != true \}\}/, "an idempotent rerun must not replace the private R2 original with the public copy");
  assert.match(
    workflow,
    /PDF_PATH="market_view_summaries\/\$DATE_FOLDER\/market_views_\$DATE_FOLDER\.pdf"[\s\S]*?commit_output_dir\.sh[\s\\]*\n\s*"\$PDF_PATH"[\s\S]*?8[\s\\]*\n\s*true[\s\\]*\n\s*true/,
    "only the exact public-safe PDF may be force-added",
  );
  assert.doesNotMatch(workflow, /commit_output_dir\.sh\s+"market_view_summaries"/, "the synthesis root must never be committed wholesale");
  assert.match(workflow, /git restore --source=HEAD --worktree -- prompts\/zsxq_img\.jpg/, "the private publishing image must be restored before the public identity scan");
  assert.match(workflow, /git add -f "\$PDF_PATH"[\s\S]*?check_public_identity\.py[\s\S]*?git reset -- "\$PDF_PATH"/, "the exact public PDF must pass the identity guard before commit");
  assert.doesNotMatch(workflow, /actions:\s*write|migrate_legacy_artifacts|archive_existing_only|commit_results/, "one-time migration privileges must not remain in the daily workflow");
  assert.match(workflow, /permissions:\s*\n\s*contents: write\s*\n\s*actions: read/, "the generator needs narrowly scoped repository write permission");
  assert.match(gitignore, /^market_view_summaries\/$/m, "Market Views synthesis output must remain ignored by git");
  assert.match(app, /data-market-view-id/);
  assert.match(app, /\/market-views\/access/);
  assert.match(app, /\/market-views\/pdf\?id=/);
  assert.match(app, /id="accountAdminMarketViewsSection"/, "the operations dashboard must expose a dedicated Market Views section");
  assert.match(app, /loadAccountAdminMarketViews\(workerUrl, targets\)/, "the operations dashboard must load private-R2 Market Views metadata");

  const transfer = { Blob, AbortController, setTimeout, clearTimeout, fetch: null, api: null };
  vm.runInNewContext(`${extractFunction(app, "fetchBlogMarketView")} api = fetchBlogMarketView;`, transfer);
  const bytes = new TextEncoder().encode("%PDF-1.7\nactual streamed content");
  function responseFor(length, options = {}) {
    const headers = { "Content-Type": "application/pdf", ...options.headers };
    if (length !== null) headers["Content-Length"] = String(length);
    return new Response(new ReadableStream({ start(controller) {
      controller.enqueue(bytes.slice(0, 8));
      controller.enqueue(bytes.slice(8));
      controller.close();
    } }), { headers });
  }
  for (const length of [bytes.length, null]) {
    transfer.fetch = async () => responseFor(length);
    const progress = [];
    const result = await transfer.api("/api/market-views/pdf?id=market-view:261005", { Authorization: "Bearer fixture" }, new AbortController(), (received, total) => progress.push([received, total]));
    assert.equal(result.blob.size, bytes.length);
    assert.equal(await result.blob.text(), new TextDecoder().decode(bytes));
    assert.deepEqual(progress[0], [0, length || 0]);
    assert.ok(progress.some(([received]) => received === 8), "real intermediate chunk size must be visible");
    assert.deepEqual(progress.at(-1), [bytes.length, length || 0]);
  }
  transfer.fetch = async () => responseFor(bytes.length + 1);
  await assert.rejects(transfer.api("/api/pdf", {}, new AbortController(), () => {}), /传输不完整/);
  transfer.fetch = async () => responseFor(bytes.length, { headers: { "Content-Encoding": "gzip" } });
  await transfer.api("/api/pdf", {}, new AbortController(), (_, total) => assert.equal(total, 0, "compressed Content-Length is not decoded stream length"));
  transfer.fetch = async () => new Response("login required", { headers: { "Content-Type": "text/html" } });
  await assert.rejects(transfer.api("/api/pdf", {}, new AbortController(), () => {}), /有效 PDF/);
  for (const code of [401, 402, 503]) {
    transfer.fetch = async () => new Response(JSON.stringify({ detail: `server gate ${code}` }), { status: code });
    await assert.rejects(transfer.api("/api/pdf", {}, new AbortController(), () => {}), new RegExp(`server gate ${code}`));
  }
  const cancelled = new AbortController();
  transfer.fetch = async (_url, options) => {
    assert.equal(options.headers.Authorization, "Bearer fixture");
    return new Response(new ReadableStream({ start(controller) {
      options.signal.addEventListener("abort", () => controller.error(new DOMException("aborted", "AbortError")));
    } }), { headers: { "Content-Type": "application/pdf" } });
  };
  const cancelling = transfer.api("/api/pdf", { Authorization: "Bearer fixture" }, cancelled, () => cancelled.abort());
  await assert.rejects(cancelling, /已取消/);
  let timeout;
  transfer.setTimeout = (callback, delay) => { assert.equal(delay, 60000); timeout = callback; return 1; };
  transfer.clearTimeout = () => {};
  transfer.fetch = (_url, options) => new Promise((_resolve, reject) => options.signal.addEventListener("abort", () => reject(new DOMException("aborted", "AbortError"))));
  const timed = transfer.api("/api/pdf", {}, new AbortController(), () => {});
  timeout();
  await assert.rejects(timed, /60 秒未收到数据/);

  const historySandbox = { api: null };
  vm.runInNewContext(`${extractFunction(app, "blogMarketViewHistory")} api = blogMarketViewHistory;`, historySandbox);
  const dated = Array.from({ length: 19 }, (_, i) => ({ id: String(i), date: `2026-09-${String(30 - i).padStart(2, "0")}` }));
  assert.equal(historySandbox.api(dated, "", 1).items.length, 6);
  assert.equal(historySandbox.api(dated, "", 2).items[0].id, "6");
  assert.equal(historySandbox.api(dated, "", 99).page, 4);
  assert.equal(historySandbox.api(dated, "", 0).page, 1);
  assert.equal(historySandbox.api(dated, "2026-09-27", 3).items[0].id, "3");
  assert.equal(historySandbox.api(dated, "2026-01-01", 1).items.length, 0);

  const cardStatus = { textContent: "", className: "" };
  const progressElement = { hidden: true, removeAttribute() {} };
  const cancelButton = { hidden: true };
  const card = { querySelector(selector) { return selector === "progress" ? progressElement : selector === ".blog-download-cancel" ? cancelButton : cardStatus; } };
  const downloadButton = { disabled: false, dataset: { marketViewId: "market-view:261005" }, closest() { return card; } };
  const handlers = {};
  const list = { innerHTML: "", addEventListener(name, callback) { handlers[name] = callback; }, querySelector() { return null; }, querySelectorAll() { return [downloadButton]; } };
  let loggedIn = false, modal = 0, downloads = 0, starts = 0, finish;
  const listRequests = [];
  const ui = { api: null, AbortController, Date, formatSize: (size) => `${size} B`, escapeHtml: String,
    document: { getElementById(id) { return id === "blogMarketViewsList" ? list : { textContent: "", className: "" }; }, addEventListener() {} },
    window: { addEventListener() {} }, initAccountGate() {}, loadAuthSession: () => loggedIn,
    authHeaders: () => ({ Authorization: "Bearer fixture" }), showAccountModal() { modal += 1; },
    blogMarketViewCard: () => "latest PDF", blogMarketViewHistory: historySandbox.api,
    fetch: async (url, options) => { listRequests.push({ url, ...options }); return { ok: true, json: async () => ({ items: [{ id: "market-view:261005", date: "2026-10-05" }] }) }; },
    fetchBlogMarketView: async (_url, headers, _controller, progress) => { starts += 1; assert.equal(headers.Authorization, "Bearer fixture"); progress(8, bytes.length); return new Promise((resolve) => { finish = resolve; }); },
    triggerBlobDownload() { downloads += 1; },
  };
  vm.runInNewContext(`${extractFunction(app, "initBlog")} api = initBlog;`, ui);
  await ui.api();
  assert.equal(listRequests[0].url, "/api/market-views");
  assert.equal(listRequests[0].cache, "default");
  assert.equal(listRequests[0].credentials, "omit", "public metadata must not carry same-origin login cookies");
  assert.equal(listRequests[0].headers, undefined, "public metadata must not carry the bearer token");
  await handlers.click({ target: { closest(selector) { return selector === "[data-market-reload]" ? {} : null; } } });
  assert.equal(listRequests[1].cache, "no-store", "explicit retry bypasses the public directory cache");
  assert.equal(listRequests[1].credentials, "omit");
  const click = { target: { closest(selector) { return selector === "button[data-market-view-id]" ? downloadButton : null; } } };
  await handlers.click(click);
  assert.equal(modal, 1, "anonymous download prompts login");
  assert.equal(starts, 0, "anonymous users cannot start a PDF request");
  loggedIn = true;
  const firstClick = handlers.click(click);
  assert.equal(downloadButton.disabled, true);
  assert.equal(cancelButton.hidden, false);
  assert.match(cardStatus.textContent, /正在接收/);
  await handlers.click(click);
  assert.equal(starts, 1, "repeated clicks cannot create a concurrent download");
  finish({ blob: new Blob([bytes]), disposition: "" });
  await firstClick;
  assert.equal(downloads, 1);
  assert.equal(downloadButton.disabled, false);
  assert.equal(cancelButton.hidden, true);
  assert.match(cardStatus.textContent, /交给浏览器保存/);
  ui.fetchBlogMarketView = async () => { throw new Error("fixture interrupted"); };
  await handlers.click(click);
  assert.equal(downloads, 1, "a failed transfer cannot save a PDF");
  assert.equal(downloadButton.textContent, "重试下载");
  assert.equal(downloadButton.disabled, false);
  ui.fetchBlogMarketView = async (_url, _headers, controller) => new Promise((_resolve, reject) => {
    controller.signal.addEventListener("abort", () => reject(new Error("下载已取消，可重新下载。")));
  });
  const cancelledClick = handlers.click(click);
  await handlers.click({ target: { closest(selector) { return selector === ".blog-download-cancel" ? cancelButton : null; } } });
  await cancelledClick;
  assert.match(cardStatus.textContent, /已取消/);
  assert.equal(downloadButton.textContent, "重新下载");
  assert.equal(downloadButton.disabled, false);
  assert.equal(downloads, 1, "cancel cannot save a partial PDF");

  console.log("portal Market Views membership and private-download checks passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
