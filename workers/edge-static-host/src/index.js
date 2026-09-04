const ALLOWED_PREFIX = /^(?:edge-static\/slots\/([ab])|edge-static\/releases\/([0-9a-f]{32}))\/$/;
const RELEASE_ID = /^[0-9a-f]{32}$/;
const TREE_SHA256 = /^[0-9a-f]{64}$/;
const RELEASE_CHECK_PATH = /^\/\.well-known\/edge-release\/([0-9a-f]{32})(?:\/(.*))?$/;
const EDGE_STATE_PATH = "/.well-known/edge-state";
const SHADOW_ROBOTS_POLICY = "noindex, nofollow, noarchive";
const SHADOW_ROBOTS_BODY = "User-agent: *\nDisallow: /\n";

const CACHE_POLICY = Object.freeze({
  html: Object.freeze({
    browser: "public, max-age=60",
    edge: "public, max-age=900, stale-while-revalidate=3600, stale-if-error=86400",
  }),
  runtimeJson: Object.freeze({
    browser: "public, max-age=300",
    edge: "public, max-age=300, stale-while-revalidate=300, stale-if-error=86400",
  }),
  seo: Object.freeze({
    browser: "public, max-age=300",
    edge: "public, max-age=900, stale-while-revalidate=3600, stale-if-error=86400",
  }),
  immutable: Object.freeze({
    browser: "public, max-age=31536000, immutable",
    edge: "public, max-age=31536000, immutable",
  }),
  shortAsset: Object.freeze({
    browser: "public, max-age=300",
    edge: "public, max-age=900, stale-while-revalidate=3600, stale-if-error=86400",
  }),
});

const VERSIONABLE_ASSET = /\.(?:avif|css|gif|ico|jpe?g|js|mjs|png|svg|ttf|wasm|webp|woff2?)$/i;
const CONTENT_HASH = /^[0-9a-f]{8,64}$/i;
const LOCALE_CONTENT_LANGUAGES = Object.freeze({
  ko: "ko",
  ja: "ja",
  ar: "ar",
});
const CANONICAL_PATHS = Object.freeze({
  "/index": "/",
  "/index.html": "/",
  "/reports": "/reports/",
  "/reports/index.html": "/reports/",
  "/blog": "/blog/",
  "/blog/index.html": "/blog/",
  "/reports/institutions/bernstein": "/reports/institutions/bernstein/",
  "/reports/institutions/bernstein/index.html": "/reports/institutions/bernstein/",
  "/charts.html": "/charts",
});

function localePath(pathname) {
  const match = /^\/(ko|ja|ar)(?=\/|$)/.exec(String(pathname || ""));
  if (!match) return { prefix: "", pathname: String(pathname || "") };
  const prefix = `/${match[1]}`;
  return {
    prefix,
    pathname: String(pathname || "").slice(prefix.length) || "/",
  };
}

function canonicalPath(pathname) {
  const localized = localePath(pathname);
  if (localized.prefix && pathname === localized.prefix) return `${localized.prefix}/`;
  const target = CANONICAL_PATHS[localized.pathname] || "";
  return target && localized.prefix ? `${localized.prefix}${target}` : target;
}

function contentLanguage(pathname) {
  const releaseCheck = RELEASE_CHECK_PATH.exec(String(pathname || ""));
  const contentPath = releaseCheck ? `/${releaseCheck[2] || ""}` : pathname;
  const localizedData = /^\/data\/i18n\/(ko|ja|ar)(?=\/|$)/.exec(contentPath);
  if (localizedData) return LOCALE_CONTENT_LANGUAGES[localizedData[1]];
  const localizedSitemap = /^\/sitemap-(ko|ja|ar)\.xml$/.exec(contentPath);
  if (localizedSitemap) return LOCALE_CONTENT_LANGUAGES[localizedSitemap[1]];
  const localized = localePath(contentPath);
  return localized.prefix
    ? LOCALE_CONTENT_LANGUAGES[localized.prefix.slice(1)]
    : "zh-Hans";
}

function canonicalPathForResolved(pathname, relative, candidate) {
  const sourcePath = String(pathname || "");
  if (!sourcePath || sourcePath.endsWith("/")) return "";
  const localized = localePath(sourcePath);
  // Dynamic canonicalization belongs to the new locale namespaces only.  The
  // established Chinese routes keep their existing behavior until they are
  // reviewed as a separate release.
  if (!localized.prefix) return "";
  const contentPath = localized.pathname;
  if (/^\/(?:api|assets|data|\.well-known)(?:\/|$)/i.test(contentPath)
    || /^\/favicon(?:\.|$)/i.test(contentPath)) {
    return "";
  }

  const lowerRelative = String(relative || "").toLowerCase();
  const lowerCandidate = String(candidate || "").toLowerCase();
  if (/\/index\.html$/i.test(contentPath)
    && lowerCandidate === lowerRelative
    && lowerCandidate.endsWith("/index.html")) {
    return sourcePath.replace(/index\.html$/i, "");
  }
  const lastSegment = lowerRelative.split("/").pop() || "";
  if (!lowerCandidate || !lastSegment || lastSegment.includes(".")) return "";
  if (lowerCandidate === `${lowerRelative}/index.html`) return `${sourcePath}/`;
  if (lowerCandidate !== `${lowerRelative}.html`) return "";
  // /charts is already the explicit pretty canonical for charts.html.
  if (Object.values(CANONICAL_PATHS).includes(contentPath)) return "";
  return `${sourcePath}.html`;
}

function canonicalRedirect(url, canonicalHostValue = "", targetPath = canonicalPath(url.pathname)) {
  const canonicalHost = String(canonicalHostValue || "").trim().toLowerCase();
  const hostNeedsRedirect = Boolean(canonicalHost && url.hostname.toLowerCase() !== canonicalHost);
  if (!targetPath && !hostNeedsRedirect) return null;
  const target = new URL(url);
  if (canonicalHost) {
    target.protocol = "https:";
    target.host = canonicalHost;
  }
  if (targetPath) target.pathname = targetPath;
  const headers = new Headers({
    location: target.toString(),
    "cache-control": "no-store",
    "cloudflare-cdn-cache-control": "no-store",
    "content-language": contentLanguage(target.pathname),
    "x-origin-class": "edge-static",
  });
  return new Response(null, { status: 301, headers });
}

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

function isVersionedAsset(path, url) {
  if (!VERSIONABLE_ASSET.test(path)) return false;
  const segments = path.split("/");
  const filename = segments.pop() || "";
  const stem = filename.replace(/\.[^.]+$/, "");
  if (segments.some((segment) => CONTENT_HASH.test(segment))) return true;
  if (stem.split(/[._-]/).some((part) => CONTENT_HASH.test(part))) return true;
  const versions = url.searchParams.getAll("v");
  return versions.length === 1 && CONTENT_HASH.test(versions[0]);
}

function cachePolicyFor(path, url) {
  const lower = path.toLowerCase();
  if (lower.endsWith(".html")) return CACHE_POLICY.html;
  if (lower.endsWith(".json")) return CACHE_POLICY.runtimeJson;
  if (lower.endsWith(".xml") || lower.endsWith(".txt")) return CACHE_POLICY.seo;
  if (isVersionedAsset(path, url)) return CACHE_POLICY.immutable;
  return CACHE_POLICY.shortAsset;
}

function responseHeaders(object, path, url, releaseCheck = false) {
  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set("content-type", headers.get("content-type") || fallbackContentType(path));
  headers.set("content-language", contentLanguage(url.pathname));
  // The active Worker binding changes between immutable releases, so edge policy
  // is authoritative even when an older object carries legacy upload metadata.
  const cachePolicy = cachePolicyFor(path, url);
  headers.set("cache-control", releaseCheck ? "no-store" : cachePolicy.browser);
  // This Worker is the canonical-host gateway.  Its entrypoint must run before
  // any reusable representation is selected, otherwise an alias response can
  // be replayed to the canonical host by a shared Workers Cache key.
  headers.set("cloudflare-cdn-cache-control", "no-store");
  if (object.httpEtag) headers.set("etag", object.httpEtag);
  if (object.uploaded instanceof Date && Number.isFinite(object.uploaded.getTime())) {
    headers.set("last-modified", object.uploaded.toUTCString());
  }
  headers.set("accept-ranges", "bytes");
  headers.set("access-control-allow-origin", "*");
  headers.set("x-content-type-options", "nosniff");
  headers.set("referrer-policy", "strict-origin-when-cross-origin");
  headers.set("x-frame-options", "SAMEORIGIN");
  headers.set("x-origin-class", "edge-static");
  return headers;
}

function splitEtags(value) {
  const values = [];
  let start = 0;
  let quoted = false;
  for (let index = 0; index < value.length; index += 1) {
    const character = value[index];
    if (character === '"') quoted = !quoted;
    if (character === "," && !quoted) {
      values.push(value.slice(start, index).trim());
      start = index + 1;
    }
  }
  values.push(value.slice(start).trim());
  return values.filter(Boolean);
}

function weakEtag(value) {
  const trimmed = String(value || "").trim();
  return /^W\//i.test(trimmed) ? trimmed.slice(2).trim() : trimmed;
}

function isNotModified(request, object) {
  const ifNoneMatch = request.headers.get("if-none-match");
  if (ifNoneMatch !== null) {
    const candidates = splitEtags(ifNoneMatch);
    if (candidates.includes("*")) return true;
    if (!object.httpEtag) return false;
    const current = weakEtag(object.httpEtag);
    return candidates.some((candidate) => weakEtag(candidate) === current);
  }

  const ifModifiedSince = request.headers.get("if-modified-since");
  if (!ifModifiedSince || !(object.uploaded instanceof Date)) return false;
  const requestedTime = Date.parse(ifModifiedSince);
  const uploadedTime = object.uploaded.getTime();
  if (!Number.isFinite(requestedTime) || !Number.isFinite(uploadedTime)) return false;
  // HTTP dates have one-second precision. Compare the same value advertised in
  // Last-Modified instead of treating sub-second storage metadata as newer.
  return Math.floor(uploadedTime / 1000) <= Math.floor(requestedTime / 1000);
}

function isIfRangeMatch(request, object) {
  const value = String(request.headers.get("if-range") || "").trim();
  if (!value) return true;

  // If-Range uses strong entity-tag comparison. A weak validator must fall
  // back to the complete representation even if its opaque value matches.
  if (value.startsWith('"') || /^W\//i.test(value)) {
    const current = String(object.httpEtag || "").trim();
    return Boolean(current) && !/^W\//i.test(value) && !/^W\//i.test(current) && value === current;
  }

  if (!(object.uploaded instanceof Date)) return false;
  const requestedTime = Date.parse(value);
  const uploadedTime = object.uploaded.getTime();
  if (!Number.isFinite(requestedTime) || !Number.isFinite(uploadedTime)) return false;
  return Math.floor(uploadedTime / 1000) <= Math.floor(requestedTime / 1000);
}

function parseByteRange(value, size) {
  if (!Number.isSafeInteger(size) || size < 0) return null;
  const match = /^bytes=(\d*)-(\d*)$/i.exec(String(value || "").trim());
  if (!match || (!match[1] && !match[2]) || size === 0) return null;

  let start;
  let end;
  if (!match[1]) {
    const suffix = Number(match[2]);
    if (!Number.isSafeInteger(suffix) || suffix <= 0) return null;
    start = Math.max(0, size - suffix);
    end = size - 1;
  } else {
    start = Number(match[1]);
    end = match[2] ? Number(match[2]) : size - 1;
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start < 0 || end < start || start >= size) {
      return null;
    }
    end = Math.min(end, size - 1);
  }
  return { offset: start, length: end - start + 1 };
}

async function resolveObject(env, prefix, relative, headOnly, request, allowRange = true) {
  for (const candidate of candidatePaths(relative)) {
    const key = prefix + candidate;
    const rangeRequested = allowRange && !headOnly && request.headers.has("Range");
    if (headOnly) {
      const object = await env.STATIC_BUCKET.head(key);
      if (object) return { object, candidate };
      continue;
    }
    if (!rangeRequested) {
      const object = await env.STATIC_BUCKET.get(key);
      if (object) return { object, candidate };
      continue;
    }

    // R2 does not evaluate If-Range. Read metadata first so a stale validator
    // yields the complete 200 representation and only a genuinely invalid byte
    // range becomes 416. Storage errors are deliberately not rewritten as 416.
    const metadata = await env.STATIC_BUCKET.head(key);
    if (!metadata) continue;
    if (request.headers.has("If-Range") && !isIfRangeMatch(request, metadata)) {
      const object = await env.STATIC_BUCKET.get(key);
      if (object) return { object, candidate };
      continue;
    }
    const range = parseByteRange(request.headers.get("Range"), metadata.size);
    if (!range) return { rangeError: true, object: metadata, candidate };
    const object = await env.STATIC_BUCKET.get(key, { range });
    if (object) return { object, candidate };
  }
  return null;
}

function isShadowMode(env) {
  return env.SHADOW_MODE === "true";
}

function protectShadowResponse(response, shadowMode) {
  if (!shadowMode) return response;
  const headers = new Headers(response.headers);
  headers.set("x-robots-tag", SHADOW_ROBOTS_POLICY);
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

function shadowRobotsResponse(request) {
  const headers = new Headers({
    "content-type": "text/plain; charset=utf-8",
    "content-language": "zh-Hans",
    "content-length": String(new TextEncoder().encode(SHADOW_ROBOTS_BODY).byteLength),
    "cache-control": "no-store",
    "cloudflare-cdn-cache-control": "no-store",
    "x-origin-class": "edge-static",
    "x-robots-tag": SHADOW_ROBOTS_POLICY,
  });
  return new Response(request.method === "HEAD" ? null : SHADOW_ROBOTS_BODY, {
    status: 200,
    headers,
  });
}

const productionWorker = {
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
          "access-control-allow-headers": "Range, If-Range, If-None-Match, If-Modified-Since",
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

    if (!RELEASE_CHECK_PATH.test(url.pathname)) {
      const redirect = canonicalRedirect(url, env.CANONICAL_HOST, canonicalPath(url.pathname));
      if (redirect) return redirect;
    }

    const prefix = String(env.STATIC_PREFIX || "");
    const prefixMatch = ALLOWED_PREFIX.exec(prefix);
    if (!prefixMatch) {
      return new Response("Service Unavailable", {
        status: 503,
        headers: { "x-origin-class": "edge-static" },
      });
    }
    const slot = prefixMatch[1] || "legacy";
    const legacyRelease = prefixMatch[2] || "";
    const configuredRelease = String(env.STATIC_RELEASE || "").trim().toLowerCase();
    const activeRelease = RELEASE_ID.test(configuredRelease) ? configuredRelease : legacyRelease;
    if (!activeRelease) {
      return new Response("Service Unavailable", {
        status: 503,
        headers: { "x-origin-class": "edge-static" },
      });
    }
    if (url.pathname === EDGE_STATE_PATH) {
      const treeSha256 = String(env.STATIC_TREE_SHA256 || "").trim().toLowerCase();
      return new Response(JSON.stringify({
        schema_version: 1,
        slot,
        release_id: activeRelease,
        ...(TREE_SHA256.test(treeSha256) ? { tree_sha256: treeSha256 } : {}),
      }) + "\n", {
        status: 200,
        headers: {
          "content-type": "application/json; charset=utf-8",
          "cache-control": "no-store",
          "cloudflare-cdn-cache-control": "no-store",
          "x-origin-class": "edge-static",
        },
      });
    }
    const releaseCheckMatch = RELEASE_CHECK_PATH.exec(url.pathname);
    const releaseCheck = Boolean(releaseCheckMatch);
    if (releaseCheckMatch && releaseCheckMatch[1] !== activeRelease) {
      return new Response("Not Found", {
        status: 404,
        headers: {
          "cache-control": "no-store",
          "cloudflare-cdn-cache-control": "no-store",
          "x-origin-class": "edge-static",
        },
      });
    }
    const requestedPath = releaseCheckMatch ? `/${releaseCheckMatch[2] || ""}` : url.pathname;
    const relative = safeRelativePath(requestedPath);
    if (relative === null) {
      return new Response("Bad Request", {
        status: 400,
        headers: { "x-origin-class": "edge-static" },
      });
    }

    const headOnly = request.method === "HEAD";
    let resolved = await resolveObject(env, prefix, relative, headOnly, request);
    if (!releaseCheck) {
      const resolvedTargetPath = resolved
        ? canonicalPathForResolved(requestedPath, relative, resolved.candidate)
        : "";
      const redirect = canonicalRedirect(url, env.CANONICAL_HOST, resolvedTargetPath);
      if (redirect) return redirect;
    }
    if (resolved && resolved.rangeError) {
      const headers = resolved.object
        ? responseHeaders(resolved.object, resolved.candidate, url)
        : new Headers({ "x-origin-class": "edge-static" });
      headers.set("content-range", `bytes */${resolved.object ? resolved.object.size : "*"}`);
      headers.delete("content-length");
      return new Response(null, {
        status: 416,
        headers,
      });
    }

    let status = 200;
    if (!resolved) {
      // A Range for a missing URL applies to the missing resource, not to the
      // site's fallback page. Return the complete 404 representation.
      resolved = await resolveObject(env, prefix, "404.html", headOnly, request, false);
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
    const headers = responseHeaders(object, candidate, url, releaseCheck);
    if (status === 200 && isNotModified(request, object)) {
      headers.delete("content-length");
      return new Response(null, { status: 304, headers });
    }
    if (status === 200 && !headOnly && request.headers.has("Range") && object.range && typeof object.range.offset === "number") {
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

export default {
  async fetch(request, env) {
    const shadowMode = isShadowMode(env);
    const url = new URL(request.url);
    if (shadowMode
      && url.pathname === "/robots.txt"
      && (request.method === "GET" || request.method === "HEAD")) {
      return shadowRobotsResponse(request);
    }
    return protectShadowResponse(await productionWorker.fetch(request, env), shadowMode);
  },
};
