(function (root) {
  "use strict";

  const VISITOR_ID_KEY = "portal_visitor_id";
  const FIRST_SEEN_KEY = "portal_analytics_first_seen";
  const SESSION_KEY = "portal_analytics_session";
  const AUTH_SESSION_KEY = "portal_auth_session";
  const SESSION_IDLE_MS = 30 * 60 * 1000;
  const MAX_BATCH_EVENTS = 20;
  const MAX_BODY_BYTES = 24 * 1024;
  const MAX_PENDING_EVENTS = 100;
  const MAX_PENDING_BYTES = 48 * 1024;
  // Keep the public ingestion contract separate from server-only audit events.
  // An unsupported caller must not poison valid events in the same batch.
  const PUBLIC_EVENT_TYPES = new Set([
    "account_auth", "course_material_request", "daily_file_download",
    "delivery_link_generate", "download_attempt", "download_error",
    "download_pending", "download_success", "newsfeed_interaction",
    "newsfeed_topic_request", "page_view", "report_open", "report_request",
    "report_chat_interaction", "report_text_view", "reward_checkin",
    "reward_claim", "search",
  ]);
  const sentPageViews = new Set();
  let configPromise = null;
  let resolvedWorkerUrl = "";
  let flushScheduled = false;
  let pendingEvents = 0;
  let pendingBytes = 0;
  let queue = [];

  function randomId(prefix) {
    if (root.crypto && typeof root.crypto.randomUUID === "function") return root.crypto.randomUUID();
    return `${prefix}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 12)}`;
  }

  function storageGet(key) {
    try {
      return root.localStorage && root.localStorage.getItem(key) || "";
    } catch (_error) {
      return "";
    }
  }

  function storageSet(key, value) {
    try {
      if (root.localStorage) root.localStorage.setItem(key, value);
    } catch (_error) {
      // Storage may be disabled; analytics remains best effort.
    }
  }

  function visitorId() {
    let value = storageGet(VISITOR_ID_KEY);
    if (!value) {
      value = randomId("visitor");
      storageSet(VISITOR_ID_KEY, value);
    }
    return value;
  }

  function firstSeen() {
    const existing = storageGet(FIRST_SEEN_KEY);
    if (existing) return { value: existing, returning: true };
    const value = new Date().toISOString();
    storageSet(FIRST_SEEN_KEY, value);
    return { value, returning: false };
  }

  function cleanPath() {
    return String(root.location.pathname || "/").slice(0, 240);
  }

  function cleanReferrer(value) {
    if (!String(value || "").trim()) return "";
    try {
      const url = new URL(String(value || ""), root.location.origin);
      if (!/^https?:$/.test(url.protocol)) return "";
      return `${url.origin}${url.pathname}`.slice(0, 320);
    } catch (_error) {
      return "";
    }
  }

  function campaignFromLocation() {
    const params = new URLSearchParams(root.location.search || "");
    const read = (name) => String(params.get(name) || "").slice(0, 180);
    return {
      utm_source: read("utm_source"),
      utm_medium: read("utm_medium"),
      utm_campaign: read("utm_campaign"),
      utm_term: read("utm_term"),
      utm_content: read("utm_content"),
    };
  }

  function currentSession(seen = firstSeen()) {
    const now = Date.now();
    let existing = null;
    try {
      existing = JSON.parse(storageGet(SESSION_KEY) || "null");
    } catch (_error) {
      existing = null;
    }
    if (!existing || !existing.id || now - Number(existing.last_at || 0) > SESSION_IDLE_MS) {
      existing = {
        id: randomId("session"),
        started_at: new Date(now).toISOString(),
        last_at: now,
        landing_path: cleanPath(),
        referrer: cleanReferrer(root.document && root.document.referrer || ""),
        first_seen_at: seen.value,
        is_returning: seen.returning,
        ...campaignFromLocation(),
      };
    } else {
      existing.last_at = now;
    }
    storageSet(SESSION_KEY, JSON.stringify(existing));
    return existing;
  }

  function authHeaders() {
    try {
      const session = JSON.parse(storageGet(AUTH_SESSION_KEY) || "null");
      return session && session.token ? { "Authorization": `Bearer ${session.token}` } : {};
    } catch (_error) {
      return {};
    }
  }

  function workerBaseUrl(config) {
    return String(config && config.worker_base_url || "/api").replace(/\/$/, "");
  }

  function loadWorkerBaseUrl() {
    if (!configPromise) {
      configPromise = root.fetch("/data/config.json", { cache: "no-store" })
        .then((response) => response.ok ? response.json() : {})
        .catch(() => ({}))
        .then((config) => {
          resolvedWorkerUrl = workerBaseUrl(config);
          return resolvedWorkerUrl;
        });
    }
    return configPromise;
  }

  function navigationType() {
    try {
      const entries = root.performance && root.performance.getEntriesByType("navigation");
      return entries && entries[0] && entries[0].type || "navigate";
    } catch (_error) {
      return "navigate";
    }
  }

  function deviceType() {
    const ua = String(root.navigator && root.navigator.userAgent || "").toLowerCase();
    if (/bot|spider|crawl|slurp|headless|lighthouse/.test(ua)) return "bot";
    if (/ipad|tablet|kindle|silk|playbook/.test(ua)) return "tablet";
    if (/mobile|iphone|ipod|android.*mobile|windows phone/.test(ua)) return "mobile";
    return "desktop";
  }

  function botHint() {
    return deviceType() === "bot" ? "likely_bot" : "unknown";
  }

  function baseContext() {
    const seen = firstSeen();
    const session = currentSession(seen);
    const screen = root.screen ? `${Number(root.screen.width) || 0}x${Number(root.screen.height) || 0}` : "";
    return {
      page: root.document && root.document.body && root.document.body.dataset.page || "static",
      referrer: session.referrer || "",
      session_id: session.id,
      session_started_at: session.started_at || "",
      first_seen_at: session.first_seen_at || seen.value,
      is_returning: Boolean(session.is_returning),
      landing_path: session.landing_path || "",
      utm_source: session.utm_source || "",
      utm_medium: session.utm_medium || "",
      utm_campaign: session.utm_campaign || "",
      utm_term: session.utm_term || "",
      utm_content: session.utm_content || "",
      language: root.navigator && root.navigator.language || "",
      screen,
      navigation_type: navigationType(),
      device_type: deviceType(),
      bot_hint: botHint(),
    };
  }

  function sendBatch(workerUrl, entries) {
    const body = entries.length === 1
      ? entries[0].body
      : `{"events":[${entries.map((entry) => entry.body).join(",")}]}`;
    const finish = (ok) => {
      for (const entry of entries) {
        pendingEvents -= 1;
        pendingBytes -= entry.bytes;
        entry.resolve(ok);
      }
    };
    try {
      Promise.resolve(root.fetch(`${workerUrl}/analytics`, {
        method: "POST",
        cache: "no-store",
        keepalive: true,
        headers: { "Content-Type": "application/json", ...entries[0].headers },
        body,
      })).then((response) => finish(Boolean(response.ok)), () => finish(false));
    } catch (_error) {
      finish(false);
    }
  }

  function flush(workerUrl) {
    const entries = queue;
    queue = [];
    let batch = [];
    let bytes = 13; // The UTF-8 size of {"events":[]} before adding event bodies.
    for (const entry of entries) {
      if (batch.length && (batch.length >= MAX_BATCH_EVENTS
        || batch[0].headers.Authorization !== entry.headers.Authorization
        || bytes + entry.bytes + 1 > MAX_BODY_BYTES)) {
        sendBatch(workerUrl, batch);
        batch = [];
        bytes = 13;
      }
      bytes += entry.bytes + (batch.length ? 1 : 0);
      batch.push(entry);
    }
    if (batch.length) sendBatch(workerUrl, batch);
  }

  function scheduleFlush() {
    if (flushScheduled) return;
    flushScheduled = true;
    // A single microtask combines synchronous bursts such as popular-card
    // impressions without adding a timer to page views or navigation events.
    Promise.resolve().then(loadWorkerBaseUrl).then((workerUrl) => {
      flushScheduled = false;
      flush(workerUrl);
    }).catch(() => {
      flushScheduled = false;
      flush(resolvedWorkerUrl || "/api");
    });
  }

  function flushBeforeLeaving() {
    // Start keepalive requests synchronously, even if config is still loading.
    // The usual scheduled flush will see an empty queue and cannot resend it.
    if (queue.length) flush(resolvedWorkerUrl || "/api");
  }

  async function track(type, data) {
    const eventType = String(type || "event").toLowerCase();
    if (!PUBLIC_EVENT_TYPES.has(eventType)) return false;
    const path = cleanPath();
    let pageViewKey = "";
    if (eventType === "page_view") {
      pageViewKey = `${path}\u001f${String(data && data.page || root.document.body && root.document.body.dataset.page || "")}`;
      if (sentPageViews.has(pageViewKey)) return false;
    }
    const context = { ...baseContext(), ...(data || {}) };
    const payload = {
      type: eventType,
      visitor_id: visitorId(),
      session_id: context.session_id,
      client_ts: new Date().toISOString(),
      path,
      data: context,
    };
    try {
      const body = JSON.stringify(payload);
      const bytes = new TextEncoder().encode(body).byteLength;
      if (bytes > MAX_BODY_BYTES || pendingEvents >= MAX_PENDING_EVENTS
        || pendingBytes + bytes > MAX_PENDING_BYTES) return false;
      // Capture identity now: a login/logout while config loads must not assign
      // earlier events to the next account or merge the two accounts' batches.
      const headers = authHeaders();
      if (pageViewKey) sentPageViews.add(pageViewKey);
      pendingEvents += 1;
      pendingBytes += bytes;
      return await new Promise((resolve) => {
        queue.push({ body, bytes, headers, resolve });
        scheduleFlush();
      });
    } catch (_error) {
      return false;
    }
  }

  function autoPageView() {
    const body = root.document && root.document.body;
    if (body && body.dataset && body.dataset.analyticsAuto === "manual") return;
    track("page_view", {
      page: body && body.dataset.page || "static",
      report_id: body && body.dataset.reportId || "",
      report_title: body && body.dataset.reportTitle || "",
      source: body && body.dataset.source || "",
    });
  }

  root.PortalSuiteAnalytics = {
    track,
    visitorId,
    currentSession,
    loadWorkerBaseUrl,
  };

  if (typeof root.addEventListener === "function") {
    root.addEventListener("pagehide", flushBeforeLeaving);
  }
  root.document.addEventListener("visibilitychange", () => {
    if (root.document.visibilityState === "hidden") flushBeforeLeaving();
  });

  if (root.document.readyState === "loading") {
    root.document.addEventListener("DOMContentLoaded", autoPageView, { once: true });
  } else {
    autoPageView();
  }
}(window));
