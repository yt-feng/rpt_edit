import assert from "node:assert/strict";
import { generateKeyPairSync, sign } from "node:crypto";
import test from "node:test";

import { handleDropboxReady } from "../../workers/daily-source-wakeup/src/dropbox-ready.js";

const URL = "https://clock.example/dropbox-report-batch-ready";
const ISSUER = "https://token.actions.githubusercontent.com";
const NOW = Date.parse("2026-11-24T02:00:00Z");
const seconds = NOW / 1000;
const { privateKey, publicKey } = generateKeyPairSync("rsa", { modulusLength: 2048 });
const jwk = { ...publicKey.export({ format: "jwk" }), kid: "issuer-key", use: "sig", alg: "RS256" };
const proof = {
  date_folder: "261123", upstream_run_id: "45305004834", pdf_count: "48", manifest_sha256: "f".repeat(64),
};
const env = { GH_REPO: "yt-feng/rpt_edit", GH_DISPATCH_TOKEN: "test-destination-credential" };

function jwt(overrides = {}, headerOverrides = {}) {
  const claims = {
    iss: ISSUER, aud: "rpt-edit-dropbox-ready", repository: "yf2-stack/rpt_gdrive",
    repository_id: "1191522935", repository_owner_id: "270917424", ref: "refs/heads/main",
    workflow_ref: "yf2-stack/rpt_gdrive/.github/workflows/sync.yml@refs/heads/main",
    event_name: "schedule", run_id: proof.upstream_run_id, iat: seconds - 40, nbf: seconds - 40,
    exp: seconds + 260, ...overrides,
  };
  const unsigned = [{ alg: "RS256", kid: jwk.kid, ...headerOverrides }, claims]
    .map((object) => Buffer.from(JSON.stringify(object)).toString("base64url")).join(".");
  return `${unsigned}.${sign("sha256", Buffer.from(unsigned), privateKey).toString("base64url")}`;
}

function request({ token = jwt(), inputs = proof, url = URL, method = "POST" } = {}) {
  return new Request(url, {
    method,
    headers: { "Content-Type": "application/json", ...(token ? { Authorization: `Bearer ${token}` } : {}) },
    ...(method === "POST" ? { body: JSON.stringify(inputs) } : {}),
  });
}

function fixture({ githubStatus = 204, issuerStatus = 200, lost = false } = {}) {
  const calls = [];
  return {
    calls,
    call(req, settings = env) {
      return handleDropboxReady(req, settings, {
        now: () => NOW,
        async fetchWithTimeout(url, options) {
          calls.push([url, options]);
          if (url.startsWith(ISSUER)) return Response.json({ keys: [jwk] }, { status: issuerStatus });
          if (lost) throw new Error("transport timeout");
          return new Response(null, { status: githubStatus });
        },
      });
    },
  };
}

test("one authenticated run signals the fixed wake workflow with only its exact proof", async () => {
  const f = fixture();
  const response = await f.call(request());
  assert.equal(response.status, 202);
  assert.deepEqual(await response.json(), { state: "wake_accepted" });
  const [[jwks, jwksOptions], [dispatch, options]] = f.calls;
  assert.equal(jwks, `${ISSUER}/.well-known/jwks`);
  assert.equal(jwksOptions.headers, undefined);
  assert.equal(dispatch, "https://api.github.com/repos/yt-feng/rpt_edit/actions/workflows/daily-report-source-wakeup.yml/dispatches");
  assert.equal(options.method, "POST");
  assert.equal(options.headers.Authorization, `Bearer ${env.GH_DISPATCH_TOKEN}`);
  assert.deepEqual(JSON.parse(options.body), { ref: "main", inputs: proof });
});

test("missing authorization, other routes, malformed proof and oversized requests never call a provider", async () => {
  const f = fixture();
  for (const [options, code] of [
    [{ url: "https://clock.example/" }, 404], [{ method: "GET" }, 405], [{ token: "" }, 401],
    [{ inputs: { ...proof, pdf_count: 48 } }, 400],
    [{ inputs: { ...proof, destination: "another/repo" } }, 400],
    [{ inputs: { ...proof, manifest_sha256: "a".repeat(1100) } }, 400],
  ]) assert.equal((await f.call(request(options))).status, code);
  assert.deepEqual(f.calls, []);
});

test("signed tokens from the wrong workflow, branch, repository, event, or time window cannot signal", async () => {
  const f = fixture();
  for (const claims of [
    { iss: "https://issuer.example" }, { aud: "other" }, { repository_id: "7" }, { repository_owner_id: "8" },
    { repository: "another/repo" }, { ref: "refs/heads/preview" }, { workflow_ref: "untrusted" },
    { event_name: "pull_request" }, { run_id: "5" }, { nbf: seconds + 120 }, { exp: seconds },
    { iat: seconds - 1200 },
  ]) assert.equal((await f.call(request({ token: jwt(claims) }))).status, 401);
  assert.equal((await f.call(request({ token: jwt({}, { alg: "none" }) }))).status, 401);
  assert.deepEqual(f.calls, []);
});

test("an invalid signature cannot signal even for otherwise allowed claims", async () => {
  const f = fixture();
  const [header, claims, signature] = jwt().split(".");
  const changed = (signature[0] === "a" ? "b" : "a") + signature.slice(1);
  assert.equal((await f.call(request({ token: [header, claims, changed].join(".") }))).status, 401);
  assert.equal(f.calls.length, 1);
});

test("issuer unavailability and uncertain dispatch never cause a second POST", async () => {
  for (const [options, status, state, calls] of [
    [{ issuerStatus: 503 }, 503, "issuer_unavailable", 1],
    [{ githubStatus: 403 }, 502, "wake_rejected", 2],
    [{ githubStatus: 503 }, 502, "wake_outcome_unknown", 2],
    [{ lost: true }, 502, "wake_outcome_unknown", 2],
  ]) {
    const f = fixture(options);
    const response = await f.call(request({ token: jwt({ event_name: "workflow_dispatch" }) }));
    assert.equal(response.status, status);
    assert.deepEqual(await response.json(), { state });
    assert.equal(f.calls.length, calls);
  }
});
