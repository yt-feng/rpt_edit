import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../..");
const { default: worker } = await import(path.join(root, "workers/edge-static-host/src/index.js"));

const PREFIX = "edge-static/slots/a/";
const RELEASE = "0123456789abcdef0123456789abcdef";
const TREE_SHA256 = "a".repeat(64);
const UPLOADED = new Date("2026-08-12T04:05:06.789Z");

class MemoryR2 {
  constructor() {
    this.rows = new Map();
  }

  seed(relative, body, options = {}) {
    this.rows.set(PREFIX + relative, {
      body: new TextEncoder().encode(body),
      contentType: options.contentType || "",
      etag: options.etag || `"${relative}-v1"`,
      uploaded: options.uploaded || UPLOADED,
    });
  }

  object(row, range = null) {
    const body = range
      ? row.body.slice(range.offset, range.offset + range.length)
      : row.body;
    return {
      body,
      size: row.body.byteLength,
      range,
      httpEtag: row.etag,
      uploaded: row.uploaded,
      writeHttpMetadata(headers) {
        if (row.contentType) headers.set("content-type", row.contentType);
        // The Worker must replace stale upload-time cache metadata.
        headers.set("cache-control", "public, max-age=0, must-revalidate");
      },
    };
  }

  async head(key) {
    const row = this.rows.get(key);
    return row ? this.object(row) : null;
  }

  async get(key, options = {}) {
    const row = this.rows.get(key);
    if (!row) return null;
    if (!options.range) return this.object(row);
    const start = Number(options.range.offset);
    const length = Number(options.range.length);
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(length)
      || start < 0 || start >= row.body.byteLength || length <= 0) {
      throw new RangeError("unsatisfiable range");
    }
    return this.object(row, { offset: start, length });
  }
}

function fixture() {
  const bucket = new MemoryR2();
  bucket.seed("index.html", "home", { contentType: "text/html; charset=utf-8", etag: '"home-v1"' });
  bucket.seed("404.html", "missing", { contentType: "text/html; charset=utf-8", etag: '"missing-v1"' });
  bucket.seed("data/catalog.json", '{"items":[]}', { etag: '"catalog-v1"' });
  bucket.seed("data/catalog_preview.json", '{"items":[]}', { etag: '"catalog-preview-v1"' });
  bucket.seed("assets/app.js", "0123456789", { etag: '"app-v1"' });
  bucket.seed("assets/report-chat.js", "chat", { etag: '"chat-v1"' });
  bucket.seed("assets/styles.abcdef12.css", "body{}", { etag: '"css-v1"' });
  return {
    STATIC_PREFIX: PREFIX,
    STATIC_RELEASE: RELEASE,
    STATIC_TREE_SHA256: TREE_SHA256,
    STATIC_BUCKET: bucket,
  };
}

async function request(pathname, init = {}) {
  return worker.fetch(new Request(`https://static.example.invalid${pathname}`, init), fixture());
}

test("HTML keeps browser freshness while the canonical gateway bypasses CDN storage", async () => {
  const response = await request("/");
  assert.equal(response.status, 200);
  assert.equal(await response.text(), "home");
  assert.equal(response.headers.get("cache-control"), "public, max-age=60");
  assert.equal(response.headers.get("cloudflare-cdn-cache-control"), "no-store");
  assert.doesNotMatch(response.headers.get("cache-control"), /s-maxage|stale-/i);
  assert.doesNotMatch(response.headers.get("cloudflare-cdn-cache-control"), /s-maxage/i);
  assert.equal(response.headers.get("etag"), '"home-v1"');
  assert.equal(response.headers.get("last-modified"), "Wed, 12 Aug 2026 04:05:06 GMT");
});

test("legacy HTML paths and alias hosts redirect to one canonical URL", async () => {
  const env = fixture();
  env.CANONICAL_HOST = "static.example.invalid";
  const legacy = await worker.fetch(new Request("https://static.example.invalid/reports/index.html?q=ai"), env);
  assert.equal(legacy.status, 301);
  assert.equal(legacy.headers.get("location"), "https://static.example.invalid/reports/?q=ai");

  const alias = await worker.fetch(new Request("https://www.static.example.invalid/charts.html"), env);
  assert.equal(alias.status, 301);
  assert.equal(alias.headers.get("location"), "https://static.example.invalid/charts");
  assert.equal(alias.headers.get("cache-control"), "no-store");
  assert.equal(alias.headers.get("cloudflare-cdn-cache-control"), "no-store");

  const slash = await worker.fetch(new Request("https://static.example.invalid/reports/institutions/bernstein"), env);
  assert.equal(slash.status, 301);
  assert.equal(slash.headers.get("location"), "https://static.example.invalid/reports/institutions/bernstein/");
});

test("canonical host root path is served without redirect", async () => {
  const env = fixture();
  env.CANONICAL_HOST = "static.example.invalid";
  const response = await worker.fetch(new Request("https://static.example.invalid/"), env);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("location"), null);
  assert.equal(await response.text(), "home");
});

test("catalog JSON keeps browser freshness without gateway CDN storage", async () => {
  const response = await request("/data/catalog.json");
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("cache-control"), "public, max-age=300");
  assert.equal(response.headers.get("cloudflare-cdn-cache-control"), "no-store");
  assert.equal(response.headers.get("content-type"), "application/json; charset=utf-8");
});

test("release-specific checks bypass stale edge caches and only expose the active release", async () => {
  const active = await request(
    "/.well-known/edge-release/0123456789abcdef0123456789abcdef/data/catalog.json",
  );
  assert.equal(active.status, 200);
  assert.equal(await active.text(), '{"items":[]}');
  assert.equal(active.headers.get("cache-control"), "no-store");
  assert.equal(active.headers.get("cloudflare-cdn-cache-control"), "no-store");

  const stale = await request(
    "/.well-known/edge-release/ffffffffffffffffffffffffffffffff/data/catalog.json",
  );
  assert.equal(stale.status, 404);
  assert.equal(await stale.text(), "Not Found");
  assert.equal(stale.headers.get("cache-control"), "no-store");
});

test("edge state exposes the independently versioned active slot without caching", async () => {
  const response = await request("/.well-known/edge-state");
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), {
    schema_version: 1,
    slot: "a",
    release_id: RELEASE,
    tree_sha256: TREE_SHA256,
  });
  assert.equal(response.headers.get("cache-control"), "no-store");
  assert.equal(response.headers.get("cloudflare-cdn-cache-control"), "no-store");
});

test("content-versioned assets are immutable while unversioned assets stay short-lived", async () => {
  const queryVersioned = await request("/assets/app.js?v=deadbeef");
  assert.equal(queryVersioned.headers.get("cache-control"), "public, max-age=31536000, immutable");
  assert.equal(queryVersioned.headers.get("cloudflare-cdn-cache-control"), "no-store");

  const filenameVersioned = await request("/assets/styles.abcdef12.css");
  assert.equal(filenameVersioned.headers.get("cache-control"), "public, max-age=31536000, immutable");

  const unversioned = await request("/assets/report-chat.js");
  assert.equal(unversioned.headers.get("cache-control"), "public, max-age=300");
  assert.equal(unversioned.headers.get("cloudflare-cdn-cache-control"), "no-store");

  const fakeVersion = await request("/assets/app.js?v=latest");
  assert.equal(fakeVersion.headers.get("cache-control"), "public, max-age=300");
  assert.equal(fakeVersion.headers.get("cloudflare-cdn-cache-control"), "no-store");
});

test("API service-binding responses pass through without static cache mutation", async () => {
  const upstream = new Response('{"ok":true}', {
    headers: {
      "cache-control": "private, no-store",
      "content-type": "application/json",
      "x-upstream": "preserved",
    },
  });
  const env = fixture();
  env.API = { fetch: async () => upstream };
  const response = await worker.fetch(new Request("https://static.example.invalid/api/session"), env);
  assert.equal(response, upstream);
  assert.equal(response.headers.get("cache-control"), "private, no-store");
  assert.equal(response.headers.get("cloudflare-cdn-cache-control"), null);
  assert.equal(response.headers.get("x-upstream"), "preserved");
});

test("If-None-Match supports wildcard, lists, and weak comparison", async () => {
  for (const value of ["*", '"other", W/"home-v1"']) {
    const response = await request("/", { headers: { "if-none-match": value } });
    assert.equal(response.status, 304);
    assert.equal(await response.text(), "");
    assert.equal(response.headers.get("etag"), '"home-v1"');
    assert.equal(response.headers.get("content-length"), null);
  }
});

test("If-None-Match takes precedence over If-Modified-Since", async () => {
  const response = await request("/", {
    headers: {
      "if-none-match": '"different"',
      "if-modified-since": "Wed, 12 Aug 2037 04:05:06 GMT",
    },
  });
  assert.equal(response.status, 200);
  assert.equal(await response.text(), "home");
});

test("If-Modified-Since uses HTTP second precision and ignores invalid dates", async () => {
  const unchanged = await request("/", {
    headers: { "if-modified-since": "Wed, 12 Aug 2026 04:05:06 GMT" },
  });
  assert.equal(unchanged.status, 304);

  const older = await request("/", {
    headers: { "if-modified-since": "Wed, 12 Aug 2026 04:05:05 GMT" },
  });
  assert.equal(older.status, 200);

  const invalid = await request("/", { headers: { "if-modified-since": "not-a-date" } });
  assert.equal(invalid.status, 200);
});

test("HEAD returns full metadata without a body and supports validators", async () => {
  const response = await request("/assets/app.js", { method: "HEAD", headers: { range: "bytes=2-4" } });
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("content-length"), "10");
  assert.equal(response.headers.get("content-range"), null);
  assert.equal(await response.text(), "");

  const unchanged = await request("/assets/app.js", {
    method: "HEAD",
    headers: { "if-none-match": '"app-v1"' },
  });
  assert.equal(unchanged.status, 304);
  assert.equal(unchanged.headers.get("content-length"), null);
});

test("GET byte ranges retain 206 metadata and can short-circuit to 304", async () => {
  const response = await request("/assets/app.js", { headers: { range: "bytes=2-5" } });
  assert.equal(response.status, 206);
  assert.equal(await response.text(), "2345");
  assert.equal(response.headers.get("content-range"), "bytes 2-5/10");
  assert.equal(response.headers.get("content-length"), "4");
  assert.equal(response.headers.get("accept-ranges"), "bytes");

  const unchanged = await request("/assets/app.js", {
    headers: { range: "bytes=2-5", "if-none-match": '"app-v1"' },
  });
  assert.equal(unchanged.status, 304);
  assert.equal(unchanged.headers.get("content-range"), null);
  assert.equal(unchanged.headers.get("content-length"), null);
});

test("If-Range only returns 206 for a matching strong ETag", async () => {
  const matching = await request("/assets/app.js", {
    headers: { range: "bytes=2-5", "if-range": '"app-v1"' },
  });
  assert.equal(matching.status, 206);
  assert.equal(await matching.text(), "2345");

  for (const validator of ['"app-v0"', 'W/"app-v1"']) {
    const response = await request("/assets/app.js", {
      headers: { range: "bytes=2-5", "if-range": validator },
    });
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("content-range"), null);
    assert.equal(response.headers.get("content-length"), "10");
    assert.equal(await response.text(), "0123456789");
  }
});

test("If-Range dates use advertised HTTP precision and stale dates return full 200", async () => {
  for (const validator of [
    "Wed, 12 Aug 2026 04:05:06 GMT",
    "Wed, 12 Aug 2027 04:05:06 GMT",
  ]) {
    const response = await request("/assets/app.js", {
      headers: { range: "bytes=6-9", "if-range": validator },
    });
    assert.equal(response.status, 206);
    assert.equal(await response.text(), "6789");
  }

  for (const validator of ["Wed, 12 Aug 2026 04:05:05 GMT", "not-a-validator"]) {
    const response = await request("/assets/app.js", {
      headers: { range: "bytes=99-100", "if-range": validator },
    });
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("content-range"), null);
    assert.equal(await response.text(), "0123456789");
  }
});

test("unsatisfiable ranges include the complete object length", async () => {
  const response = await request("/assets/app.js", { headers: { range: "bytes=99-100" } });
  assert.equal(response.status, 416);
  assert.equal(response.headers.get("content-range"), "bytes */10");
  assert.equal(response.headers.get("content-length"), null);
  assert.equal(await response.text(), "");
});

test("R2 read failures are not disguised as invalid byte ranges", async () => {
  const env = fixture();
  env.STATIC_BUCKET.get = async () => { throw new Error("storage unavailable"); };
  await assert.rejects(
    worker.fetch(new Request("https://static.example.invalid/assets/app.js", {
      headers: { range: "bytes=2-5" },
    }), env),
    /storage unavailable/,
  );
});

test("a Range for a missing URL does not turn the fallback page into a 206", async () => {
  const response = await request("/does-not-exist", { headers: { range: "bytes=0-2" } });
  assert.equal(response.status, 404);
  assert.equal(response.headers.get("content-range"), null);
  assert.equal(response.headers.get("content-length"), "7");
  assert.equal(await response.text(), "missing");
});

test("the fallback representation never answers 304 for a missing URL", async () => {
  const response = await request("/does-not-exist", {
    headers: { "if-none-match": '"missing-v1"' },
  });
  assert.equal(response.status, 404);
  assert.equal(await response.text(), "missing");
});

test("neutral deployment keeps the canonical gateway cache disabled and verifies catalog parity", () => {
  const workflow = readFileSync(path.join(root, ".github/workflows/neutral-edge-cutover.yml"), "utf8");
  assert.match(workflow, /\[cache\]\s+enabled = false/);
  assert.match(workflow, /wranglerVersion: ["']4\.69\.0["']/);
  assert.match(workflow, /compatibility_date = ["']2026-08-12["']/);
  assert.match(workflow, /group: edge-static-hosting-production/);
  assert.match(workflow, /test -s _neutral_site\/data\/catalog_preview\.json/);
  assert.match(workflow, /live-catalog-preview\.json/);
  assert.match(workflow, /\.well-known\/edge-release\/\$STATIC_RELEASE/);
  assert.match(workflow, /STATIC_PREFIX = "\$STATIC_PREFIX"/);
  assert.match(workflow, /STATIC_RELEASE = "\$STATIC_RELEASE"/);
  assert.match(workflow, /STATIC_TREE_SHA256 = "\$STATIC_TREE_SHA256"/);
  const refreshStep = workflow.match(
    /- name: Verify refreshed catalog is live[\s\S]*?- name: Remove private values from persistent source/,
  )?.[0] || "";
  assert.match(refreshStep, /\$release_check\/data\/catalog\.json/);
  assert.match(refreshStep, /\$release_check\/data\/catalog_preview\.json/);
  assert.doesNotMatch(refreshStep, /\?release=/);
  assert.match(workflow, /assert_aligned\("local", expected, expected_preview\)/);
  assert.match(workflow, /assert_aligned\("live", actual, actual_preview\)/);
  const verifyRouteStep = workflow.match(
    /- name: Verify active edge routes[\s\S]*?- name: Verify refreshed catalog is live/,
  )?.[0] || "";
  assert.match(verifyRouteStep, /scripts\/edge_route_cutover\.py verify/);
  assert.doesNotMatch(verifyRouteStep, /CLOUDFLARE_API_TOKEN/);
  assert.doesNotMatch(verifyRouteStep, /exit 0/);
  assert.ok(
    workflow.indexOf("- name: Roll back failed edge release")
      > workflow.indexOf("- name: Verify hot-report pagination UI and API are live"),
  );
  const preflightStep = workflow.match(
    /- name: Gate refresh on stable live routes[\s\S]*?- name: Capture previous public discovery state/,
  )?.[0] || "";
  assert.match(preflightStep, /scripts\/edge_route_cutover\.py verify/);
  assert.match(preflightStep, /EDGE_VERIFY_ATTEMPTS: ["']3["']/);
  assert.match(preflightStep, /EDGE_VERIFY_CONSECUTIVE: ["']3["']/);
  assert.ok(
    workflow.indexOf("- name: Gate refresh on stable live routes")
      < workflow.indexOf("- name: Upload inactive static slot incrementally"),
    "live cache isolation must pass before an inactive slot is uploaded",
  );
  const rollbackStep = workflow.match(
    /- name: Roll back failed edge release[\s\S]*?- name: Verify automated edge rollback/,
  )?.[0] || "";
  assert.match(rollbackStep, /steps\.edge_deploy\.outcome != 'skipped'/);
  assert.match(rollbackStep, /steps\.edge_state_verify\.outcome != 'success'/);
  assert.match(rollbackStep, /steps\.edge_routes_verify\.outcome != 'success'/);
  assert.match(rollbackStep, /steps\.live_catalog\.outcome != 'success'/);
  assert.match(rollbackStep, /steps\.live_discovery\.outcome != 'success'/);
  assert.match(rollbackStep, /steps\.live_hot_reports\.outcome != 'success'/);
  assert.match(rollbackStep, /command: rollback \$\{\{ env\.EDGE_PREVIOUS_VERSION_ID \}\} --message/);
  assert.doesNotMatch(workflow, /- name: Switch active edge routes/);
  assert.doesNotMatch(workflow, /scripts\/edge_route_cutover\.py migrate/);
  assert.doesNotMatch(workflow, /scripts\/edge_route_cutover\.py rollback/);
  assert.doesNotMatch(workflow, /Purge previous public edge cache/);
  assert.doesNotMatch(workflow, /edge_route_cutover\.py purge/);
  assert.ok(
    workflow.indexOf("- name: Deploy neutral edge runtime")
      < workflow.indexOf("- name: Verify active edge routes"),
    "bare alias verification must gate the release after the edge runtime deploys",
  );
  const discoveryStep = workflow.match(
    /- name: Verify discovery and report-detail assets are live[\s\S]*?- name: Submit changed public URLs to IndexNow/,
  )?.[0] || "";
  assert.match(discoveryStep, /curl --fail --location --silent --show-error[\s\\]+--connect-timeout 10 --max-time 30/);
  assert.match(discoveryStep, /fetch_asset\(\)/);
  assert.match(discoveryStep, /for attempt in \$\(seq 1 18\)/);
  assert.match(discoveryStep, /asset_check=%s http_status=%s/);
  assert.match(discoveryStep, /Waiting for discovery assets to become active/);
  assert.match(discoveryStep, /Discovery assets did not become active in time/);
  assert.match(discoveryStep, /live-report-detail-release\.json/);
  assert.doesNotMatch(discoveryStep, /continue-on-error/);
  assert.doesNotMatch(discoveryStep, /urlopen/);

  const activeSlotStep = workflow.match(
    /- name: Discover active static slot[\s\S]*?- name: Upload inactive static slot incrementally/,
  )?.[0] || "";
  assert.match(activeSlotStep, /\.well-known\/edge-state\?before=\$STATIC_RELEASE/);
  assert.match(activeSlotStep, /ACTIVE_STATIC_SLOT/);
  assert.match(activeSlotStep, /legacy-bootstrap/);

  const uploadStep = workflow.match(
    /- name: Upload inactive static slot incrementally[\s\S]*?- name: Prepare neutral edge runtime/,
  )?.[0] || "";
  assert.match(uploadStep, /id: static_upload/);
  assert.match(uploadStep, /scripts\/publish_static_slot\.py/);
  assert.match(uploadStep, /--active-slot "\$\{ACTIVE_STATIC_SLOT:-\}"/);
  assert.doesNotMatch(uploadStep, /client\.upload_file/);

  const stateVerifyStep = workflow.match(
    /- name: Verify active static slot switch[\s\S]*?- name: Verify active edge routes/,
  )?.[0] || "";
  assert.match(stateVerifyStep, /id: edge_state_verify/);
  assert.match(stateVerifyStep, /\.well-known\/edge-state\?after=\$STATIC_RELEASE/);
  assert.match(stateVerifyStep, /state != expected/);

  const pruneStep = workflow.match(
    /- name: Prune obsolete legacy static releases[\s\S]*$/,
  )?.[0] || "";
  assert.match(pruneStep, /always\(\)/);
  assert.match(pruneStep, /steps\.static_upload\.outcome == 'success'/);
  assert.match(pruneStep, /steps\.edge_deploy\.outcome == 'success'/);
  assert.match(pruneStep, /steps\.edge_state_verify\.outcome == 'success'/);
  assert.match(pruneStep, /steps\.live_catalog\.outcome == 'success'/);
  assert.match(pruneStep, /steps\.live_discovery\.outcome == 'success'/);
  assert.match(pruneStep, /complete_slots < 2/);
  assert.match(pruneStep, /continue-on-error: true/);
});
