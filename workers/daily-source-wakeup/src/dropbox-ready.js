// Authenticate Dropbox readiness and dispatch only the Daily source wake.
const ROUTE = "/dropbox-report-batch-ready";
const WORKFLOW = "daily-report-source-wakeup.yml";
const BODY_LIMIT = 1024;
const SIGNATURE_MAX_AGE_MS = 5 * 60 * 1000;
const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: true });

async function verifySignature(timestamp, signature, body, signingKey) {
  const prefix = encoder.encode(`${timestamp}\n`);
  const signed = new Uint8Array(prefix.length + body.length);
  signed.set(prefix);
  signed.set(body, prefix.length);
  const signatureBytes = Uint8Array.from(signature.match(/../g), (byte) => parseInt(byte, 16));
  const key = await crypto.subtle.importKey("raw", encoder.encode(signingKey),
    { name: "HMAC", hash: "SHA-256" }, false, ["verify"]);
  return crypto.subtle.verify("HMAC", key, signatureBytes, signed);
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
    const body = bytes.subarray(0, end);
    const inputs = JSON.parse(decoder.decode(body));
    const fields = {
      date_folder: /^[0-9]{6}$/,
      upstream_run_id: /^[1-9][0-9]{0,15}$/,
      pdf_count: /^[1-9][0-9]{0,7}$/,
      manifest_sha256: /^[0-9a-f]{64}$/,
    };
    if (!inputs || Object.keys(inputs).length !== Object.keys(fields).length) return null;
    for (const [name, pattern] of Object.entries(fields)) {
      if (typeof inputs[name] !== "string" || !pattern.test(inputs[name])) return null;
    }
    return { inputs, body };
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
  const authorization = /^ReportHMAC ([1-9][0-9]{9,10})\.([0-9a-f]{64})$/.exec(request.headers.get("Authorization") || "");
  if (!authorization) return respond("unauthorized", 401);
  const [, timestamp, signature] = authorization;
  if (Math.abs(now() - Number(timestamp) * 1000) > SIGNATURE_MAX_AGE_MS) {
    return respond("unauthorized", 401);
  }
  const signingKey = String(env.REPORT_HANDOFF_SIGNING_KEY || "").trim();
  if (!/^[0-9a-f]{64}$/.test(signingKey)) return respond("dispatch_unconfigured", 503);
  const proof = await readInputs(request);
  if (!proof) return respond("invalid_batch_proof", 400);
  const { body, inputs } = proof;
  if (!await verifySignature(timestamp, signature, body, signingKey)) return respond("unauthorized", 401);

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
      // Workers returns 3xx directly in manual mode. Reject it without
      // forwarding credentials, just like other unaccepted responses.
      redirect: "manual",
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
