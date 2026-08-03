const ALLOWED_PREFIX = /^edge-static\/releases\/[0-9a-f]{32}\/$/;

function safeRelativePath(pathname) {
  let decoded;
  try {
    decoded = decodeURIComponent(pathname);
  } catch {
    return null;
  }
  if (decoded.includes("\0") || decoded.includes("\\") || decoded.includes("//")) return null;
  const relative = decoded.replace(/^\/+/, "");
  const parts = relative.split("/");
  if (parts.some((part) => part === "." || part === "..")) return null;
  if (!relative || relative.endsWith("/")) return relative + "index.html";
  return relative;
}

function candidatePaths(relative) {
  const values = [relative];
  const last = relative.split("/").pop() || "";
  if (last && !last.includes(".")) {
    values.push(relative + ".html");
    values.push(relative + "/index.html");
  }
  return [...new Set(values)];
}

function fallbackContentType(path) {
  const extension = (path.match(/\.([a-z0-9]+)$/i) || [])[1] || "";
  const types = {
    html: "text/html; charset=utf-8",
    css: "text/css; charset=utf-8",
    js: "text/javascript; charset=utf-8",
    json: "application/json; charset=utf-8",
    xml: "application/xml; charset=utf-8",
    txt: "text/plain; charset=utf-8",
    svg: "image/svg+xml",
    jpg: "image/jpeg",
    jpeg: "image/jpeg",
    png: "image/png",
    webp: "image/webp",
    ico: "image/x-icon",
    pdf: "application/pdf",
    wasm: "application/wasm",
    woff: "font/woff",
    woff2: "font/woff2",
  };
  return types[extension.toLowerCase()] || "application/octet-stream";
}

function cacheControlFor(path) {
  if (/\.(html|json|xml|txt)$/i.test(path)) return "public, max-age=0, must-revalidate";
  return "public, max-age=3600";
}

function responseHeaders(object, path) {
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("content-type", headers.get("content-type") || fallbackContentType(path));
  headers.set("cache-control", headers.get("cache-control") || cacheControlFor(path));
  headers.set("etag", object.httpEtag);
  headers.set("last-modified", object.uploaded.toUTCString());
  headers.set("accept-ranges", "bytes");
  headers.set("access-control-allow-origin", "*");
  headers.set("x-content-type-options", "nosniff");
  headers.set("referrer-policy", "strict-origin-when-cross-origin");
  headers.set("x-frame-options", "SAMEORIGIN");
  headers.set("x-origin-class", "edge-static");
  return headers;
}

async function resolveObject(env, prefix, relative, headOnly, request) {
  for (const candidate of candidatePaths(relative)) {
    const key = prefix + candidate;
    try {
      const object = headOnly
        ? await env.STATIC_BUCKET.head(key)
        : await env.STATIC_BUCKET.get(
            key,
            request.headers.has("Range") ? { range: request.headers } : undefined,
          );
      if (object) return { object, candidate };
    } catch {
      if (request.headers.has("Range")) return { rangeError: true };
      throw new Error("object read failed");
    }
  }
  return null;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api" || url.pathname.startsWith("/api/")) {
      if (!env.API || typeof env.API.fetch !== "function") {
        return new Response("Service Unavailable", { status: 503 });
      }
      return env.API.fetch(request);
    }

    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "access-control-allow-origin": "*",
          "access-control-allow-methods": "GET, HEAD, OPTIONS",
          "access-control-allow-headers": "Range, If-None-Match, If-Modified-Since",
          "x-origin-class": "edge-static",
        },
      });
    }
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method Not Allowed", {
        status: 405,
        headers: { allow: "GET, HEAD, OPTIONS", "x-origin-class": "edge-static" },
      });
    }

    const prefix = String(env.STATIC_PREFIX || "");
    if (!ALLOWED_PREFIX.test(prefix)) {
      return new Response("Service Unavailable", {
        status: 503,
        headers: { "x-origin-class": "edge-static" },
      });
    }
    const relative = safeRelativePath(url.pathname);
    if (relative === null) {
      return new Response("Bad Request", {
        status: 400,
        headers: { "x-origin-class": "edge-static" },
      });
    }

    const headOnly = request.method === "HEAD";
    let resolved = await resolveObject(env, prefix, relative, headOnly, request);
    if (resolved && resolved.rangeError) {
      return new Response(null, {
        status: 416,
        headers: { "content-range": "bytes */*", "x-origin-class": "edge-static" },
      });
    }

    let status = 200;
    if (!resolved) {
      resolved = await resolveObject(env, prefix, "404.html", headOnly, request);
      status = 404;
    }
    if (!resolved) {
      return new Response(headOnly ? null : "Not Found", {
        status: 404,
        headers: {
          "content-type": "text/plain; charset=utf-8",
          "x-origin-class": "edge-static",
        },
      });
    }

    const { object, candidate } = resolved;
    const headers = responseHeaders(object, candidate);
    if (!headOnly && request.headers.has("Range") && object.range && typeof object.range.offset === "number") {
      const start = object.range.offset;
      const length = object.range.length;
      headers.set("content-range", "bytes " + start + "-" + (start + length - 1) + "/" + object.size);
      headers.set("content-length", String(length));
      status = 206;
    } else {
      headers.set("content-length", String(object.size));
    }
    return new Response(headOnly ? null : object.body, { status, headers });
  },
};
