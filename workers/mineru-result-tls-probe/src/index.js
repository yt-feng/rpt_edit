// Fixed-target, authenticated diagnostic. It never returns upstream content.
const TARGET = "https://cdn-mineru.openxlab.org.cn/";
const TIMEOUT_MS = 8000;

function json(value, status = 200) {
  return new Response(JSON.stringify(value), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "x-content-type-options": "nosniff",
    },
  });
}

async function authorized(request, expected) {
  if (typeof expected !== "string" || !/^[a-f0-9]{64}$/.test(expected)) return false;
  const supplied = request.headers.get("authorization") || "";
  if (!/^Bearer [a-f0-9]{64}$/.test(supplied)) return false;
  const encoder = new TextEncoder();
  const left = new Uint8Array(await crypto.subtle.digest("SHA-256", encoder.encode(supplied.slice(7))));
  const right = new Uint8Array(await crypto.subtle.digest("SHA-256", encoder.encode(expected)));
  let difference = 0;
  for (let index = 0; index < left.length; index += 1) difference |= left[index] ^ right[index];
  return difference === 0;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method !== "GET" || url.pathname !== "/probe" || url.search) {
      return json({ category: "not_found" }, 404);
    }
    if (!await authorized(request, env.PROBE_TOKEN)) {
      return json({ category: "unauthorized" }, 401);
    }
    const started = Date.now();
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), TIMEOUT_MS);
    const colo = /^[A-Z]{3}$/.test(request.cf?.colo || "") ? request.cf.colo : "unknown";
    const result = {
      schema_version: 1,
      provider_host: "cdn-mineru.openxlab.org.cn",
      request_method: "HEAD",
      request_count: 1,
      redirects_followed: 0,
      zip_downloads: 0,
      provider_posts: 0,
      category: "fetch_failed",
      upstream_http_status: null,
      colo,
      elapsed_ms: 0,
    };
    try {
      const response = await fetch(TARGET, {
        method: "HEAD",
        redirect: "manual",
        cache: "no-store",
        signal: controller.signal,
      });
      result.upstream_http_status = response.status;
      result.category = response.status === 526 ? "tls_invalid_certificate"
        : response.status === 525 ? "tls_handshake_failed"
        : response.status >= 500 ? "upstream_http_error"
        : response.status >= 300 && response.status < 400 ? "https_redirect_received"
        : "https_response_received";
      if (response.body) await response.body.cancel();
    } catch {
      result.category = controller.signal.aborted ? "fetch_timeout" : "fetch_failed";
    } finally {
      clearTimeout(timeout);
      result.elapsed_ms = Math.max(0, Math.min(60000, Date.now() - started));
    }
    return json(result);
  },
};
