// Scope the public relay to one GitHub Actions workflow and one destination.
const ISSUER = "https://token.actions.githubusercontent.com";
const AUDIENCE = "rpt-edit-dropbox-ready";
const REF = "refs/heads/main";
const ROUTE = "/dropbox-report-batch-ready";
const WORKFLOW = "daily-report-source-wakeup.yml";
const BODY_LIMIT = 1024;
const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: true });

function decodeBase64Url(value) {
  if (!/^[A-Za-z0-9_-]+$/.test(value)) throw new Error("invalid_token");
  return Uint8Array.from(atob(value.replace(/-/g, "+").replace(/_/g, "/")), (char) => char.charCodeAt(0));
}

function tokenForRun(authorization, runId, now, env) {
  const jwt = authorization?.startsWith("Bearer ") ? authorization.slice(7) : "";
  if (jwt.length > 8192) return null;
  try {
    const parts = jwt.split(".");
    if (parts.length !== 3) return null;
    const [header, claims] = parts.slice(0, 2).map((part) => JSON.parse(decoder.decode(decodeBase64Url(part))));
    const seconds = Math.floor(now / 1000);
    if (header.alg !== "RS256" || typeof header.kid !== "string" || !/^[A-Za-z0-9_:-]{1,128}$/.test(header.kid)
        || claims.iss !== ISSUER || claims.aud !== AUDIENCE
        || !env.DROPBOX_SOURCE_REPO || !env.DROPBOX_SOURCE_REPO_ID || !env.DROPBOX_SOURCE_OWNER_ID
        || claims.repository !== env.DROPBOX_SOURCE_REPO || claims.repository_id !== env.DROPBOX_SOURCE_REPO_ID
        || claims.repository_owner_id !== env.DROPBOX_SOURCE_OWNER_ID
        || claims.ref !== REF
        || claims.workflow_ref !== `${env.DROPBOX_SOURCE_REPO}/.github/workflows/sync.yml@${REF}`
        || !["schedule", "workflow_dispatch"].includes(claims.event_name)
        || claims.run_id !== runId
        || ![claims.iat, claims.nbf, claims.exp].every(Number.isSafeInteger)
        || claims.iat < seconds - 600 || claims.iat > seconds + 30 || claims.nbf > seconds + 30
        || claims.exp <= seconds || claims.exp - claims.iat > 600) return null;
    return {
      kid: header.kid,
      signature: decodeBase64Url(parts[2]),
      signed: encoder.encode(parts.slice(0, 2).join(".")),
    };
  } catch {
    return null;
  }
}

async function verifyToken(token, fetchWithTimeout) {
  const response = await fetchWithTimeout(`${ISSUER}/.well-known/jwks`, { redirect: "error" }, 5000);
  if (!response.ok) throw new Error("issuer_unavailable");
  const { keys } = await response.json();
  const key = keys.find((entry) => entry.kid === token.kid && entry.kty === "RSA"
    && entry.use === "sig" && (!entry.alg || entry.alg === "RS256"));
  if (!key) return false;
  const algorithm = { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" };
  const verificationKey = await crypto.subtle.importKey("jwk", key, algorithm, false, ["verify"]);
  return crypto.subtle.verify(algorithm, verificationKey, token.signature, token.signed);
}

async function readInputs(request) {
  if (!request.body || Number(request.headers.get("Content-Length")) > BODY_LIMIT
      || request.headers.get("Content-Type")?.split(";")[0].trim() !== "application/json") return null;
  const reader = request.body.getReader();
  try {
    const bytes = new Uint8Array(BODY_LIMIT);
    let end = 0;
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      if (end + value.length > BODY_LIMIT) {
        await reader.cancel();
        return null;
      }
      bytes.set(value, end);
      end += value.length;
    }
    const input = JSON.parse(decoder.decode(bytes.subarray(0, end)));
    const fields = {
      date_folder: /^[0-9]{6}$/,
      upstream_run_id: /^[1-9][0-9]{0,15}$/,
      pdf_count: /^[1-9][0-9]{0,7}$/,
      manifest_sha256: /^[0-9a-f]{64}$/,
    };
    if (!input || Object.keys(input).length !== Object.keys(fields).length) return null;
    for (const [name, pattern] of Object.entries(fields)) {
      if (typeof input[name] !== "string" || !pattern.test(input[name])) return null;
    }
    return input;
  } catch {
    return null;
  } finally {
    reader.releaseLock();
  }
}

export async function handleDropboxReady(request, env, { fetchWithTimeout, now = Date.now }) {
  const respond = (state, status) => Response.json({ state }, {
    status, headers: { "Cache-Control": "no-store" },
  });
  if (new URL(request.url).pathname !== ROUTE) return respond("not_found", 404);
  if (request.method !== "POST") return respond("method_not_allowed", 405);
  const authorization = request.headers.get("Authorization");
  if (!authorization) return respond("unauthorized", 401);
  const inputs = await readInputs(request);
  if (!inputs) return respond("invalid_batch_proof", 400);
  const token = tokenForRun(authorization, inputs.upstream_run_id, now(), env);
  if (!token) return respond("unauthorized", 401);
  try {
    if (!await verifyToken(token, fetchWithTimeout)) return respond("unauthorized", 401);
  } catch {
    return respond("issuer_unavailable", 503);
  }

  const repository = String(env.GH_REPO || "").trim();
  const credential = String(env.GH_DISPATCH_TOKEN || "").trim();
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository) || !credential || credential === "unconfigured") {
    return respond("dispatch_unconfigured", 503);
  }
  try {
    // The wake workflow independently verifies the Dropbox proof and serializes
    // with the polling wake. One POST is enough even on a lost acknowledgement.
    const response = await fetchWithTimeout(`https://api.github.com/repos/${repository}/actions/workflows/${WORKFLOW}/dispatches`, {
      method: "POST",
      redirect: "error",
      headers: {
        Authorization: `Bearer ${credential}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "portal-daily-source-clock",
        "X-GitHub-Api-Version": "2022-11-28",
      },
      body: JSON.stringify({ ref: "main", inputs }),
    }, 8000);
    await response.body?.cancel().catch(() => {});
    if (response.ok) return respond("wake_accepted", 202);
    return respond(response.status >= 500 ? "wake_outcome_unknown" : "wake_rejected", 502);
  } catch {
    return respond("wake_outcome_unknown", 502);
  }
}
