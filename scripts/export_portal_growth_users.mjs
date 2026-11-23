#!/usr/bin/env node
// Reuse production account/permission rules without changing the Worker module.
import { spawn } from "node:child_process";
import { cp, mkdtemp, readFile, rm, writeFile, open, mkdir } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { createInterface } from "node:readline";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ACCESS_FIELDS = ["active", "access_mode", "download_limit", "downloads_remaining", "source", "status", "current_period_end", "lifetime"];
const fail = () => new Error("Canonical account snapshot failed; private details omitted.");

export function readOnlySupabaseFetch(base, transport = globalThis.fetch) {
  let allowed;
  if (base) {
    allowed = new URL(base);
    if (allowed.protocol !== "https:" || allowed.username || allowed.password || allowed.search || allowed.hash
      || !["", "/"].includes(allowed.pathname)) throw fail();
  }
  return async (input, options = {}) => {
    const request = new Request(input, options);
    const url = new URL(request.url);
    if (!allowed || request.method !== "GET" || request.body || url.origin !== allowed.origin
      || url.username || url.password || url.hash
      || !["/rest/v1/site_users", "/rest/v1/user_entitlements"].includes(url.pathname)) throw fail();
    const response = await transport(new Request(request, { redirect: "error" }));
    if (response.redirected) throw fail();
    return response;
  };
}

export function readOnlyBucket(send) {
  const deny = async () => { throw fail(); };
  return Object.freeze({
    async get(key, options) {
      if (options !== undefined) throw fail();
      const result = await send({ op: "get", key });
      return result === null ? null : Object.freeze({
        etag: result.etag,
        text: async () => Buffer.from(result.body_b64, "base64").toString("utf8"),
      });
    },
    head: (key) => send({ op: "head", key }),
    list: ({ prefix, limit = 1000, cursor } = {}) => send({ op: "list", prefix, limit, ...(cursor ? { cursor } : {}) }),
    put: deny, delete: deny, createMultipartUpload: deny, resumeMultipartUpload: deny,
  });
}

export function startReadOnlyBridge(env) {
  const names = ["PATH", "R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET"];
  const child = spawn("python3", ["-B", path.join(ROOT, "scripts/portal_growth_users_r2_bridge.py")], {
    env: Object.fromEntries(names.filter((key) => env[key]).map((key) => [key, env[key]])),
    stdio: ["pipe", "pipe", "ignore"],
  });
  const pending = new Map();
  let sequence = 0;
  let stopped = false;
  const stop = () => {
    stopped = true;
    for (const { reject, timeout } of pending.values()) { clearTimeout(timeout); reject(fail()); }
    pending.clear();
    child.kill();
  };
  const lines = createInterface({ input: child.stdout });
  lines.on("line", (line) => {
    try {
      if (line.length > 1024 * 1024) throw fail();
      const value = JSON.parse(line);
      const entry = pending.get(value.id);
      if (!entry) throw fail();
      pending.delete(value.id);
      clearTimeout(entry.timeout);
      if (value.ok === true) entry.resolve(value.result);
      else entry.reject(fail());
    } catch { stop(); }
  });
  child.on("error", stop);
  child.on("exit", stop);
  child.stdin.on("error", stop);
  return {
    bucket: readOnlyBucket((value) => new Promise((resolve, reject) => {
      if (stopped || sequence >= 40000) return reject(fail());
      const id = ++sequence;
      const timeout = setTimeout(stop, 90000);
      pending.set(id, { resolve, reject, timeout });
      child.stdin.write(JSON.stringify({ id, ...value }) + "\n");
    })),
    close: stop,
  };
}

export async function withCanonicalLoader(callback, source = path.join(ROOT, "workers/portal-suite-worker/src")) {
  const directory = await mkdtemp(path.join(os.tmpdir(), "portal-growth-users-"));
  try {
    await cp(source, path.join(directory, "src"), { recursive: true });
    await writeFile(path.join(directory, "package.json"), '{"type":"module"}\n', { mode: 0o600 });
    const entry = path.join(directory, "src/index.js");
    const worker = await readFile(entry, "utf8");
    await writeFile(entry, worker + "\nexport { loadAllAdminUsersForExport };\n", { mode: 0o600 });
    const module = await import(pathToFileURL(entry).href);
    return await callback(module.loadAllAdminUsersForExport);
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
}

export function currentUserSnapshot(rows, sourceMode, generatedAt = new Date().toISOString()) {
  if (!Array.isArray(rows) || rows.length > 5000 || !["supabase", "r2"].includes(sourceMode)) throw fail();
  const seen = new Set();
  const users = rows.map((row) => {
    if (!row || typeof row.id !== "string" || !row.id || seen.has(row.id) || typeof row.email !== "string"
      || typeof row.disabled !== "boolean" || !["user", "super", "operator"].includes(row.role)
      || !row.effective_access || typeof row.effective_access.active !== "boolean"
      || !["all", "filters", "none"].includes(row.effective_access.access_mode)
      || !Number.isInteger(row.effective_access.download_limit) || row.effective_access.download_limit < 0) throw fail();
    seen.add(row.id);
    return {
      id: row.id, email: row.email, created_at: row.created_at || "", last_login_at: row.last_login_at || "",
      disabled: row.disabled, role: row.role,
      effective_access: Object.fromEntries(ACCESS_FIELDS.map((key) => [key, row.effective_access[key]])),
    };
  });
  return { schema: "portal-growth-current-users-v1", generated_at: generatedAt, complete: true,
    source_mode: sourceMode, user_count: users.length, users };
}

export async function writePrivateSnapshot(output, snapshot) {
  await mkdir(path.dirname(output), { recursive: true, mode: 0o700 });
  // Never follow or overwrite an existing path (including symlinks).
  const file = await open(output, "wx", 0o600);
  try { await file.writeFile(JSON.stringify(snapshot) + "\n"); }
  catch (error) { await file.close(); await rm(output, { force: true }); throw error; }
  await file.close();
}

export async function main(args = process.argv.slice(2), env = process.env) {
  if (args.length !== 2 || args[0] !== "--output" || !args[1]) throw fail();
  const mode = String(env.ACCOUNT_STORE_MODE || "supabase").trim();
  const supabase = String(env.SUPABASE_URL || "").trim();
  const serviceKey = String(env.SUPABASE_SERVICE_ROLE_KEY || "").trim();
  if (!["supabase", "r2"].includes(mode) || (mode === "supabase" && (!supabase || !serviceKey))
    || (mode === "r2" && (supabase || serviceKey))) throw fail();
  const originalFetch = globalThis.fetch;
  globalThis.fetch = readOnlySupabaseFetch(supabase, originalFetch);
  const bridge = startReadOnlyBridge(env);
  try {
    const snapshot = await withCanonicalLoader(async (load) => currentUserSnapshot(await load({
      ACCOUNT_STORE_MODE: mode, SUPABASE_URL: supabase, SUPABASE_SERVICE_ROLE_KEY: serviceKey,
      REPORT_BUCKET: bridge.bucket,
    }), mode));
    await writePrivateSnapshot(path.resolve(args[1]), snapshot);
    console.log(JSON.stringify({ ok: true, user_count: snapshot.user_count, complete: true }));
  } finally {
    bridge.close();
    globalThis.fetch = originalFetch;
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(() => { console.error(JSON.stringify({ ok: false, error: "canonical_user_snapshot_failed" })); process.exitCode = 1; });
}
