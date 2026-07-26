const CACHE_TTL_MS = 5 * 60 * 1000;
const DEFAULT_R2_PREFIX = "reports";
const CONTACT_WECHAT = "MacroGate";
const ADMIN_TOKEN_TTL_SECONDS = 180 * 24 * 60 * 60;
const USER_TOKEN_TTL_SECONDS = 30 * 24 * 60 * 60;
const CAPTCHA_TTL_SECONDS = 10 * 60;
const PASSWORD_ITERATIONS = 120000;
const GENERATED_EMAIL_DOMAIN = "users.kcdesk.com";
const SITE_ORIGIN = "kcdesk";
const VID2PPT_SOURCE_SITE = "vid2ppt";
const USERNAME_PATTERN = /^[a-z0-9][a-z0-9_.-]{2,31}$/;
const EMAIL_PATTERN = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const ACTIVE_STATUSES = new Set(["active", "trialing"]);
const SUPER_ACCOUNT_USERNAMES = new Set(["twotigers"]);
const SUPER_ACCOUNT_EMAILS = new Set(["twotigers@users.kcdesk.com"]);
const OPERATOR_ACCOUNT_USERNAMES = new Set(["liuxin"]);
const OPERATOR_ACCOUNT_EMAILS = new Set(["liuxin@users.kcdesk.com"]);
const ACCESS_MODES = new Set(["none", "all", "filters"]);
const TRIAL_3D_DURATION_VALUE = "trial_3d";
const TRIAL_3D_DOWNLOAD_LIMIT = 10;
const TRIAL_LIMIT_MESSAGE = `3天体验下载已满 ${TRIAL_3D_DOWNLOAD_LIMIT} 篇，请联系微信 ${CONTACT_WECHAT}。`;
const ACCESS_PAGE_RANGE_OPTIONS = [
  { value: "under5", label: "5页以下" },
  { value: "5_10", label: "5-10页" },
  { value: "10_20", label: "10-20页" },
  { value: "over20", label: "20页以上" },
];
const ACCESS_DURATION_OPTIONS = [
  { value: TRIAL_3D_DURATION_VALUE, label: "3天体验（10篇）", days: 3, download_limit: TRIAL_3D_DOWNLOAD_LIMIT },
  { value: "1", label: "1个月", months: 1 },
  { value: "2", label: "2个月", months: 2 },
  { value: "3", label: "3个月", months: 3 },
  { value: "6", label: "6个月", months: 6 },
  { value: "12", label: "1年", months: 12 },
  { value: "24", label: "2年", months: 24 },
  { value: "lifetime", label: "长期", months: 0 },
];
const REPORT_INDUSTRY_RULES = [
  ["Macro / FX / Rates", /\b(macro|fx|foreign exchange|currency|cny|yuan|dollar|usd|rate|rates|yield|fed|ecb|boj|inflation|cpi|pmi|gdp|economy|economic|recession|treasury|bond|nominal|real rate)\b/],
  ["Equity Strategy", /\b(strategy|equity strategy|market strategy|asset allocation|portfolio|index|earnings revision|valuation|eps|target price)\b/],
  ["Tech / AI / Semis", /\b(ai|artificial intelligence|semiconductor|semis|chip|chips|memory|dram|nand|hbm|gpu|server|software|cloud|data center|datacenter|robot|robotics)\b/],
  ["Internet / Media", /\b(internet|media|gaming|game|music|streaming|advertising|ecommerce|e-commerce|platform|social|takeaway|food delivery|new media)\b/],
  ["Autos / EV / Batteries", /\b(auto|autos|automotive|vehicle|ev|bev|battery|batteries|lithium|ess|adas|mobility|tesla|byd)\b/],
  ["Energy / Utilities", /\b(energy|oil|gas|lng|solar|wind|power|utility|utilities|renewable|coal|electricity|grid)\b/],
  ["Metals / Mining", /\b(metal|metals|mining|copper|aluminum|aluminium|steel|iron ore|gold|silver|nickel|commodity|commodities)\b/],
  ["Healthcare / Biotech", /\b(healthcare|health care|biotech|pharma|pharmaceutical|drug|medical|hospital|medtech|vaccine|therapy)\b/],
  ["Consumer / Retail", /\b(consumer|retail|apparel|luxury|brand|restaurant|food|beverage|travel retail|staples|discretionary)\b/],
  ["Banks / Financials", /\b(bank|banks|banking|insurance|broker|brokerage|asset manager|fintech|exchange|financials|payment)\b/],
  ["Real Estate", /\b(real estate|property|housing|developer|reit|mortgage|homebuilder|construction)\b/],
  ["Industrials / Capex", /\b(industrial|industrials|machinery|automation|capex|capital goods|aerospace|defense|rail|shipping|logistics|transport)\b/],
  ["Policy / Geopolitics", /\b(policy|politics|geopolitic|geopolitical|tariff|trade war|election|sanction|iran|russia|taiwan|strait|security)\b/],
];
const NEWSFEED_ACCOUNT_USERNAMES = new Set(["jacob"]);
const NEWSFEED_ACCOUNT_EMAILS = new Set(["jacob@bo-axis.com"]);
const DEFAULT_GITHUB_REPO = "yt-feng/rpt_edit";
const DEFAULT_GITHUB_REF = "main";
const BBG_SHOW_REPO = "yt-feng/bbg-show";
const BBG_SHOW_PREFIX = "rendered-clips";
const ENTERTAIN_CUT_REPO = "yt-feng/entertain_cut";
const KC_ENTERTAIN_PREFIX = "outputs/kc_entertain";
const RPT2VID_REPO = "yt-feng/rpt2vid";
const RPT2VID_PDF_KC_PREFIX = "videos/pdf_kc";
const GITHUB_CACHE_PREFIX = "_account/github-cache";
const GITHUB_CACHE_RETENTION_MS = 3 * 24 * 60 * 60 * 1000;
const WECHAT_DRAFT_SOURCES = [
  { root: "wechat_drafts/xhs_notes", label: "投行文章" },
  { root: "wechat_drafts/institutions", label: "机构文章" },
  { root: "wechat_drafts/consulting", label: "咨询文章" },
  { root: "wechat_drafts", label: "公众号文章", legacy: true },
];
const PADDLE_HANDLED_EVENTS = new Set([
  "transaction.completed",
  "subscription.created",
  "subscription.updated",
  "subscription.canceled",
  "subscription.past_due",
  "subscription.paused",
  "subscription.resumed",
]);
const VID2PPT_KCDESK_GIFT_PLANS = {
  "NOVA-3D": { days: 3, download_limit: TRIAL_3D_DOWNLOAD_LIMIT, label: "NOVA three-day trial" },
  "NOVA-M": { months: 1, label: "NOVA monthly" },
  "NOVA-Q": { months: 3, label: "NOVA quarter" },
  "NOVA-Y": { months: 12, label: "NOVA year" },
  "NOVA-2Y": { months: 24, label: "NOVA two years" },
  // Keep already-issued ATLAS codes redeemable after the NOVA migration.
  "ATLAS-M": { months: 1, label: "ATLAS monthly (legacy)" },
  "ATLAS-Q": { months: 3, label: "ATLAS quarter (legacy)" },
  "ATLAS-Y": { months: 12, label: "ATLAS year (legacy)" },
  "ATLAS-2Y": { months: 24, label: "ATLAS two years (legacy)" },
};
const VID2PPT_GIFT_SOURCES = new Set(["vid2ppt_nova", "vid2ppt_atlas"]);
const VID2PPT_REDEEM_URL = "https://vid2ppt.com/api/usage";
const VID2PPT_CODE_PATTERN = /^[A-Z0-9][A-Z0-9-]{7,39}$/;

// External report integration. Search/detail endpoints are public; PDF access
// still requires a password.
const EXTERNAL_HOST = "report" + "ify.cn";
const EXTERNAL_API = `https://api.${EXTERNAL_HOST}`;
const EXTERNAL_SITE = `https://${EXTERNAL_HOST}`;
const EXTERNAL_R2_PREFIX = "report" + "ify";
const EXTERNAL_STATUS_PREFIX = "report" + "ify-status";
const EXTERNAL_SEARCH_PAGE_SIZE = 20;
const EXTERNAL_UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36";

// High-authority foreign-report metadata. Search endpoints are public; this
// integration intentionally does not download PDFs.
const AUTHORITY_HOST = ["www", "na" + "sh-ai", "cn"].join(".");
const AUTHORITY_ORIGIN = `https://${AUTHORITY_HOST}`;
const AUTHORITY_SOURCE = "authority";
const AUTHORITY_SEARCH_PAGE_SIZE = 20;
const AUTHORITY_UA = "KCDeskAuthoritySearch/1.0";
const AUTHORITY_KINDS = {
  "foreign": {
    endpoint: "/reports/foreign/search",
    referer: `${AUTHORITY_ORIGIN}/foreign.html`,
    price_cents: 2600,
    label: "普通外文",
  },
  "foreign-rt": {
    endpoint: "/reports/foreign-rt/search",
    referer: `${AUTHORITY_ORIGIN}/foreign-rt.html`,
    price_cents: 4600,
    label: "实时外文",
  },
};

const HIBOR_ORIGIN = "https://www.hibor.com.cn";
const HIBOR_SOURCE = "report-a";
const HIBOR_SEARCH_PAGE_SIZE = 30;
const HIBOR_UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/137.0 Safari/537.36";
const THINKTANK_SOURCE = "thinktank";
const THINKTANK_ARCHIVE_PATH = "institution_feeds/institution_pdf_archive.jsonl";
const THINKTANK_WECHAT_DRAFT_ROOT = "wechat_drafts/institutions";
const THINKTANK_SEARCH_PAGE_SIZE = 30;
const THINKTANK_WECHAT_DATE_LIMIT = 45;
const THINKTANK_WARM_PDF_LIMIT = 90;
const THINKTANK_SEARCH_WARM_LIMIT = 8;
const THINKTANK_WARM_CONCURRENCY = 3;
const THINKTANK_R2_PREFIX = "thinktank";
const THINKTANK_UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/137.0 Safari/537.36";
const UPSTREAM_SEARCH_TIMEOUT_MS = 28000;
const UPSTREAM_PDF_TIMEOUT_MS = 15000;
const SEARCH_CACHE_PREFIX = "_search-cache";
const SEARCH_CACHE_FRESH_MS = 6 * 60 * 60 * 1000;
const SEARCH_MIRROR_PREFIX = "_search-mirror";
const SEARCH_MIRROR_STALE_MS = 36 * 60 * 60 * 1000;
const ANALYTICS_PREFIX = "_analytics/events";
const ANALYTICS_BACKUP_PREFIX = "_analytics_backup/events";
const ANALYTICS_DASHBOARD_DAYS = 7;
const ANALYTICS_DASHBOARD_LIMIT = 50;
const ANALYTICS_DASHBOARD_R2_READ_BUDGET = 60;
const ANALYTICS_DASHBOARD_TIMEOUT_MS = 9000;
const ANALYTICS_HISTORY_DEFAULT_PAGE_SIZE = 100;
const ANALYTICS_HISTORY_MAX_PAGE_SIZE = 200;
const ANALYTICS_HISTORY_FILTER_SCAN_LIMIT = 100;
const ANALYTICS_HISTORY_READ_BATCH = 30;
const ADMIN_GITHUB_FILES_TIMEOUT_MS = 12000;
const ADMIN_GITHUB_SOURCE_TIMEOUT_MS = 8500;
const ADMIN_GITHUB_ARTIFACT_TIMEOUT_MS = 2500;
const GITHUB_API_TIMEOUT_MS = 5500;
const ADMIN_CATALOG_TIMEOUT_MS = 3500;
const ADMIN_WECHAT_TIMEOUT_MS = 3500;
const INTERNAL_JSON_TIMEOUT_MS = 10000;
const SUPABASE_TIMEOUT_MS = 6500;
const SUPABASE_WRITE_TIMEOUT_MS = 15000;
const ADMIN_SNAPSHOT_PREFIX = "_account/admin-snapshots";
const ADMIN_FILES_SNAPSHOT_KEY = `${ADMIN_SNAPSHOT_PREFIX}/files.json`;
const ADMIN_PICKS_SNAPSHOT_KEY = `${ADMIN_SNAPSHOT_PREFIX}/picks.json`;
const ADMIN_WECHAT_SNAPSHOT_KEY = `${ADMIN_SNAPSHOT_PREFIX}/wechat.json`;
const ADMIN_ANALYTICS_SNAPSHOT_KEY = `${ADMIN_SNAPSHOT_PREFIX}/analytics.json`;
const ADMIN_USERS_SNAPSHOT_KEY = `${ADMIN_SNAPSHOT_PREFIX}/users.json`;
const ADMIN_OPS_MIRROR_STATE_KEY = `${ADMIN_SNAPSHOT_PREFIX}/ops-mirror.json`;
const ADMIN_SNAPSHOT_FRESH_MS = 30 * 60 * 1000;
const ADMIN_FILES_SNAPSHOT_FRESH_MS = 10 * 60 * 1000;
const ADMIN_ANALYTICS_SNAPSHOT_FRESH_MS = 15 * 60 * 1000;
const ADMIN_SNAPSHOT_VERSION = 1;
const OPS_MIRROR_EVENT_TYPE = "kcdesk-ops-files-changed";
const OPS_MIRROR_RETRY_MS = 5 * 60 * 1000;
const OPS_ALERT_PREFIX = "_ops/alerts";
const OPS_ALERT_SIGNATURE_MAX_AGE_SECONDS = 5 * 60;
const OPS_ALERT_DEDUPE_MS = 24 * 60 * 60 * 1000;
const NEWSFEED_CACHE_PREFIX = "_newsfeed/cache";
const NEWSFEED_TOPICS_PREFIX = "_newsfeed/topics";
const NEWSFEED_SETTINGS_PREFIX = "_newsfeed/settings";
const NEWSFEED_CACHE_FRESH_MS = 30 * 60 * 1000;
const NEWSFEED_CACHE_STALE_MS = 6 * 60 * 60 * 1000;
const NEWSFEED_CACHE_VERSION = 3;
const NEWSFEED_MAX_USER_TOPICS = 10000;
const NEWSFEED_EMAIL_DEFAULT_TIME = "09:00";
const NEWSFEED_EMAIL_DEFAULT_TIMEZONE = "Asia/Shanghai";
const NEWSFEED_EMAIL_WINDOW_MINUTES = 35;
const CLOUDFLARE_API_BASE = "https://api.cloudflare.com/client/v4";
const CLOUDFLARE_EMAIL_TIMEOUT_MS = 10000;
const NEWSFEED_CATEGORIES = ["Investment", "Tech", "Politics", "Industries"];
const NEWSFEED_UA = "KCDeskNewsfeed/0.1";
const NEWSFEED_OUTPUT_LANGUAGES = [
  { code: "en", label: "English", instruction: "English" },
  { code: "zh-CN", label: "中文", instruction: "Simplified Chinese" },
  { code: "ja", label: "日本語", instruction: "Japanese" },
  { code: "ko", label: "한국어", instruction: "Korean" },
];
const NEWSFEED_REGIONS = [
  {
    code: "global",
    label: "Global",
    query: "",
    google: { hl: "en-US", gl: "US", ceid: "US:en" },
  },
  {
    code: "mena",
    label: "MENA",
    query: "\"Middle East\" OR MENA OR GCC OR Saudi Arabia OR UAE OR Qatar OR Egypt OR Turkey OR Israel",
    google: { hl: "en-AE", gl: "AE", ceid: "AE:en" },
  },
  {
    code: "china",
    label: "China",
    query: "China OR Chinese OR Beijing OR Shanghai OR Shenzhen OR Hong Kong",
    google: { hl: "zh-CN", gl: "CN", ceid: "CN:zh-Hans" },
  },
  {
    code: "usa",
    label: "USA",
    query: "\"United States\" OR USA OR US OR Washington",
    google: { hl: "en-US", gl: "US", ceid: "US:en" },
  },
];
const NEWSFEED_PUBLIC_RSS_FEEDS = [
  { url: "https://feeds.bbci.co.uk/news/world/rss.xml", source: "BBC World", category: "Politics" },
  { url: "https://www.theguardian.com/world/rss", source: "The Guardian World", category: "Politics" },
  { url: "https://feeds.bbci.co.uk/news/business/rss.xml", source: "BBC Business", category: "Investment" },
  { url: "https://www.theguardian.com/business/rss", source: "The Guardian Business", category: "Investment" },
  { url: "https://feeds.bbci.co.uk/news/technology/rss.xml", source: "BBC Technology", category: "Tech" },
  { url: "https://www.theguardian.com/technology/rss", source: "The Guardian Technology", category: "Tech" },
  { url: "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml", source: "BBC Science", category: "Industries" },
  { url: "https://feeds.bbci.co.uk/news/business/rss.xml", source: "BBC Business", category: "Industries" },
];
const NEWSFEED_DEFAULT_TOPICS = [
  {
    id: "global-daily",
    title: "Global Daily",
    description: "A broad feed across markets, policy, technology, and global affairs.",
    kind: "system",
    pinned: true,
    category: "Investment",
    queries: [
      "global economy OR markets OR central banks OR geopolitics",
      "major world news economy politics technology",
    ],
  },
  {
    id: "tech-ai",
    title: "Tech",
    description: "AI, robotics, semiconductors, software, and platform shifts.",
    kind: "system",
    category: "Tech",
    queries: [
      "artificial intelligence OR robotics OR semiconductors OR data centers",
      "AI startup funding OR humanoid robots OR chips",
    ],
  },
  {
    id: "global-politics",
    title: "Politics",
    description: "Elections, policy, geopolitics, defense, sanctions, and trade.",
    kind: "system",
    category: "Politics",
    queries: [
      "election OR sanctions OR trade policy OR defense OR diplomacy",
      "geopolitics OR tariff OR security council OR government policy",
    ],
  },
  {
    id: "industries",
    title: "Industries",
    description: "Energy, manufacturing, transport, healthcare, and industrial supply chains.",
    kind: "system",
    category: "Industries",
    queries: [
      "manufacturing OR energy OR logistics OR healthcare OR supply chain",
      "industrial automation OR renewable energy OR aerospace OR biotech",
    ],
  },
  {
    id: "investment",
    title: "Investment",
    description: "Capital markets, IPOs, private equity, M&A, funding, and asset flows.",
    kind: "system",
    category: "Investment",
    queries: [
      "IPO OR funding round OR merger acquisition OR private equity",
      "investment flows OR asset management OR venture capital OR markets",
    ],
  },
];
const NEWSFEED_SUGGESTED_TOPICS = [
  "Self-driving snow groomers for ski resorts",
  "Satellite-based wildfire early-warning apps",
  "Robotic kitchen systems for home chefs",
  "Zero-gravity manufacturing on the ISS",
  "Middle East capital investing in China",
  "Humanoid robot supply chains",
];

let catalogCache = null;
let catalogFetchedAt = 0;
let rulesCache = null;
let rulesFetchedAt = 0;
let searchIndexCache = null;
let searchIndexFetchedAt = 0;
let adminFilesRefreshPromise = null;
let adminPicksRefreshPromise = null;
let adminWechatRefreshPromise = null;
let adminAnalyticsRefreshPromise = null;
let adminUsersRefreshPromise = null;

function allowedOrigin(request, env) {
  const requestOrigin = request.headers.get("Origin") || "";
  const configured = String(env.ALLOWED_ORIGIN || "")
    .split(",")
    .map((origin) => {
      const trimmed = origin.trim();
      try {
        return new URL(trimmed).origin;
      } catch (_error) {
        return trimmed;
      }
    })
    .filter(Boolean);

  if (!configured.length) return requestOrigin || "*";
  if (configured.includes(requestOrigin)) return requestOrigin;
  return configured[0];
}

function corsHeaders(request, env) {
  return {
    "Access-Control-Allow-Origin": allowedOrigin(request, env),
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, Paddle-Signature, X-Vid2PPT-Signature, Range, X-KC-Timestamp, X-KC-Signature",
    "Access-Control-Expose-Headers": "Content-Disposition, Content-Length, Content-Range, Accept-Ranges",
    "Vary": "Origin",
  };
}

function jsonResponse(request, env, status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

async function fetchJson(url) {
  const response = await fetchWithTimeout(url, { headers: { "Accept": "application/json" } }, INTERNAL_JSON_TIMEOUT_MS);
  if (!response.ok) {
    throw new Error(`Could not fetch ${url}: ${response.status}`);
  }
  return response.json();
}

async function loadCatalog(env) {
  const now = Date.now();
  if (catalogCache && now - catalogFetchedAt < CACHE_TTL_MS) return catalogCache;
  if (!env.CATALOG_URL) throw new Error("CATALOG_URL is not configured");
  catalogCache = await fetchJson(env.CATALOG_URL);
  catalogFetchedAt = now;
  return catalogCache;
}

function searchIndexUrl(env) {
  const configured = String(env.SEARCH_INDEX_URL || "").trim();
  if (configured) return configured;
  const catalogUrl = String(env.CATALOG_URL || "").trim();
  if (!catalogUrl) return "";
  try {
    const url = new URL(catalogUrl);
    url.pathname = url.pathname.replace(/\/catalog\.json$/i, "/search_index.json");
    return url.toString();
  } catch (_error) {
    return catalogUrl.replace(/\/catalog\.json(?:\?.*)?$/i, "/search_index.json");
  }
}

async function loadSearchIndex(env) {
  const now = Date.now();
  if (searchIndexCache && now - searchIndexFetchedAt < CACHE_TTL_MS) return searchIndexCache;
  const url = searchIndexUrl(env);
  if (!url) throw new Error("SEARCH_INDEX_URL is not configured");
  searchIndexCache = await fetchJson(url);
  searchIndexFetchedAt = now;
  return searchIndexCache;
}

async function loadRules(env) {
  const now = Date.now();
  if (rulesCache && now - rulesFetchedAt < CACHE_TTL_MS) return rulesCache;
  if (!env.PASSWORD_RULES_URL) throw new Error("PASSWORD_RULES_URL is not configured");
  rulesCache = await fetchJson(env.PASSWORD_RULES_URL);
  rulesFetchedAt = now;
  return rulesCache;
}

function findReport(catalog, id) {
  return (catalog.items || []).find((item) => item.id === id);
}

function findPasswordGroup(rules, groupId) {
  const target = groupId || rules.default_group || "default";
  return (rules.groups || []).find((group) => group.id === target && group.active !== false);
}

function normalizePassword(value) {
  return String(value || "").trim().toLowerCase();
}

function base32NoPadding(bytes) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
  let output = "";
  let buffer = 0;
  let bitsLeft = 0;
  for (const byte of bytes) {
    buffer = (buffer << 8) | byte;
    bitsLeft += 8;
    while (bitsLeft >= 5) {
      output += alphabet[(buffer >> (bitsLeft - 5)) & 31];
      bitsLeft -= 5;
    }
  }
  if (bitsLeft > 0) {
    output += alphabet[(buffer << (5 - bitsLeft)) & 31];
  }
  return output;
}

function base64UrlEncodeBytes(bytes) {
  let binary = "";
  for (const byte of bytes) {
    binary += String.fromCharCode(byte);
  }
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64UrlEncodeText(value) {
  return base64UrlEncodeBytes(new TextEncoder().encode(value));
}

function base64UrlDecodeText(value) {
  const base64 = String(value || "").replace(/-/g, "+").replace(/_/g, "/");
  const padded = base64 + "=".repeat((4 - base64.length % 4) % 4);
  const binary = atob(padded);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }
  return new TextDecoder().decode(bytes);
}

function constantTimeEqual(left, right) {
  const a = String(left || "");
  const b = String(right || "");
  const length = Math.max(a.length, b.length);
  let diff = a.length ^ b.length;
  for (let index = 0; index < length; index += 1) {
    diff |= (a.charCodeAt(index) || 0) ^ (b.charCodeAt(index) || 0);
  }
  return diff === 0;
}

async function hmacSha256Bytes(secret, message) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = await crypto.subtle.sign("HMAC", key, encoder.encode(message));
  return new Uint8Array(signature);
}

function adminTokenSecret(env) {
  return String(env.PASSWORD_SECRET || env.MASTER_KEY || "");
}

async function adminTokenSignature(env, body) {
  const secret = adminTokenSecret(env);
  if (!secret) throw new Error("Admin token secret is not configured");
  return base64UrlEncodeBytes(await hmacSha256Bytes(secret, `kcdesk:admin-token:v1:${body}`));
}

async function signAdminToken(env, payload) {
  const claims = { ...payload, kind: "admin", aud: "kcdesk-private-tools", v: 1 };
  const body = base64UrlEncodeText(JSON.stringify(claims));
  const signature = await adminTokenSignature(env, body);
  return `${body}.${signature}`;
}

async function verifyAdminToken(env, token) {
  const parts = String(token || "").split(".");
  if (parts.length !== 2) throw new Error("Admin session is invalid");
  const [body, signature] = parts;
  if (!body || !signature) throw new Error("Admin session is invalid");
  const expected = await adminTokenSignature(env, body);
  if (!constantTimeEqual(signature, expected)) throw new Error("Admin session is invalid");

  let payload;
  try {
    payload = JSON.parse(base64UrlDecodeText(body));
  } catch (_error) {
    throw new Error("Admin session is invalid");
  }
  const now = Math.floor(Date.now() / 1000);
  if (
    !payload
    || payload.kind !== "admin"
    || payload.aud !== "kcdesk-private-tools"
    || payload.v !== 1
    || !Number.isFinite(Number(payload.iat))
    || Number(payload.iat) > now + 60
  ) {
    throw new Error("Admin session is invalid");
  }
  if (Number(payload.exp || 0) < now) throw new Error("Admin session has expired");
  return payload;
}

async function derivedReportPassword(env, id) {
  if (!env.PASSWORD_SECRET) throw new Error("PASSWORD_SECRET is not configured");
  const cleanId = String(id || "").trim().toLowerCase();
  const digest = await hmacSha256Bytes(env.PASSWORD_SECRET, `kc-desk-notes:${cleanId}`);
  const code = base32NoPadding(digest).slice(0, 12);
  return `KC-${code.slice(0, 4)}-${code.slice(4, 8)}-${code.slice(8, 12)}`;
}

async function derivedPasswordMatches(env, id, password) {
  return normalizePassword(password) === normalizePassword(await derivedReportPassword(env, id));
}

async function sha256Hex(value) {
  const data = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(digest))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

async function hmacSha256Hex(secret, message) {
  const digest = await hmacSha256Bytes(secret, message);
  return Array.from(digest).map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function verifyOpsAlertSignature(request, env, rawBody) {
  const secret = cleanEnv(env.OPS_ALERT_SIGNING_KEY);
  if (!secret) throw new Error("Operations alert signing key is not configured.");
  const timestamp = String(request.headers.get("X-KC-Timestamp") || "").trim();
  const supplied = String(request.headers.get("X-KC-Signature") || "")
    .trim()
    .replace(/^sha256=/i, "")
    .toLowerCase();
  if (!/^\d{10}$/.test(timestamp) || !/^[a-f0-9]{64}$/.test(supplied)) {
    throw new Error("Operations alert signature is invalid.");
  }
  const age = Math.abs(Math.floor(Date.now() / 1000) - Number(timestamp));
  if (age > OPS_ALERT_SIGNATURE_MAX_AGE_SECONDS) {
    throw new Error("Operations alert signature has expired.");
  }
  const expected = await hmacSha256Hex(secret, `${timestamp}.${rawBody}`);
  if (!constantTimeEqual(supplied, expected)) {
    throw new Error("Operations alert signature is invalid.");
  }
}

function randomInt(min, max) {
  const span = max - min + 1;
  const buffer = new Uint32Array(1);
  crypto.getRandomValues(buffer);
  return min + (buffer[0] % span);
}

function randomHex(byteLength) {
  const bytes = new Uint8Array(byteLength);
  crypto.getRandomValues(bytes);
  return Array.from(bytes).map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function pbkdf2Digest(password, salt, iterations) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(password),
    "PBKDF2",
    false,
    ["deriveBits"],
  );
  const bits = await crypto.subtle.deriveBits(
    {
      name: "PBKDF2",
      salt: encoder.encode(salt),
      iterations,
      hash: "SHA-256",
    },
    key,
    256,
  );
  return base64UrlEncodeBytes(new Uint8Array(bits));
}

async function hashUserPassword(env, password) {
  const salt = randomHex(16);
  const digest = await hmacSha256Hex(accountSecret(env), `user-password:${salt}:${password}`);
  return {
    password_salt: salt,
    password_hash: `hmac_sha256$${digest}`,
  };
}

async function verifyUserPassword(env, password, salt, storedHash) {
  let algorithm = "pbkdf2_sha256";
  let iterations = PASSWORD_ITERATIONS;
  let digest = String(storedHash || "");
  const parts = digest.split("$");
  if (parts.length === 2) {
    [algorithm, digest] = [parts[0], parts[1]];
  }
  if (parts.length === 3) {
    [algorithm, iterations, digest] = [parts[0], Number(parts[1]), parts[2]];
  }
  if (algorithm === "hmac_sha256") {
    if (!digest) return false;
    const actual = await hmacSha256Hex(accountSecret(env), `user-password:${salt}:${password}`);
    return constantTimeEqual(actual, digest);
  }
  if (algorithm !== "pbkdf2_sha256" || !Number.isFinite(iterations) || !digest) return false;
  const actual = await pbkdf2Digest(password, salt, iterations);
  return constantTimeEqual(actual, digest);
}

function normalizeUsername(value) {
  return String(value || "").trim().toLowerCase().replace(/^@+/, "");
}

function normalizeEmail(value) {
  const email = String(value || "").trim().toLowerCase();
  return EMAIL_PATTERN.test(email) ? email : "";
}

function isSuperAccount(user) {
  if (!user) return false;
  const username = normalizeUsername(user.username);
  const email = normalizeEmail(user.email);
  return SUPER_ACCOUNT_USERNAMES.has(username) && SUPER_ACCOUNT_EMAILS.has(email);
}

function isOperatorAccount(user) {
  if (!user) return false;
  const username = normalizeUsername(user.username);
  const email = normalizeEmail(user.email);
  return OPERATOR_ACCOUNT_USERNAMES.has(username) && OPERATOR_ACCOUNT_EMAILS.has(email);
}

function isReservedPrivilegedIdentity(username, email) {
  const normalizedUsername = normalizeUsername(username);
  const normalizedEmail = normalizeEmail(email);
  return SUPER_ACCOUNT_USERNAMES.has(normalizedUsername)
    || SUPER_ACCOUNT_EMAILS.has(normalizedEmail)
    || OPERATOR_ACCOUNT_USERNAMES.has(normalizedUsername)
    || OPERATOR_ACCOUNT_EMAILS.has(normalizedEmail)
    || NEWSFEED_ACCOUNT_USERNAMES.has(normalizedUsername)
    || NEWSFEED_ACCOUNT_EMAILS.has(normalizedEmail);
}

function accountRole(user) {
  if (isSuperAccount(user)) return "super";
  if (isOperatorAccount(user)) return "operator";
  return "user";
}

function isPrivilegedAccount(user) {
  return accountRole(user) !== "user";
}

function isNewsfeedAccount(user) {
  if (!user) return false;
  const username = normalizeUsername(user.username);
  const email = normalizeEmail(user.email);
  return isSuperAccount(user) || (
    NEWSFEED_ACCOUNT_USERNAMES.has(username)
    && NEWSFEED_ACCOUNT_EMAILS.has(email)
  );
}

function accessErrorStatus(error) {
  const message = String(error && error.message || "");
  if (/disabled|禁用|access denied|not enabled|only .*admin/i.test(message)) return 403;
  if (/log in|session|account not found/i.test(message)) return 401;
  return 503;
}

function generatedEmailForUsername(username) {
  return `${username}@${GENERATED_EMAIL_DOMAIN}`;
}

function isGeneratedEmail(email) {
  return String(email || "").trim().toLowerCase().endsWith(`@${GENERATED_EMAIL_DOMAIN}`);
}

function accountSecret(env) {
  // AUTH_SECRET historically also peppers stored password hashes. Keep the
  // fallback until those hashes are migrated; token protocols are separated
  // cryptographically below so sharing this base secret cannot cross domains.
  const secret = String(env.AUTH_SECRET || env.PASSWORD_SECRET || env.MASTER_KEY || "").trim();
  if (!secret || secret === "unconfigured") throw new Error("Account service is temporarily unavailable.");
  return secret;
}

async function accountTokenSignature(env, body) {
  return base64UrlEncodeBytes(await hmacSha256Bytes(
    accountSecret(env),
    `kcdesk:account-token:v1:${body}`,
  ));
}

async function signAccountPayload(env, payload) {
  const body = base64UrlEncodeText(JSON.stringify(payload));
  const signature = await accountTokenSignature(env, body);
  return `${body}.${signature}`;
}

async function verifyAccountPayload(env, token, expectedKind) {
  const parts = String(token || "").split(".");
  if (parts.length !== 2) throw new Error("Session is invalid.");
  const [body, signature] = parts;
  if (!body || !signature) throw new Error("Session is invalid.");
  const expected = await accountTokenSignature(env, body);
  if (!constantTimeEqual(signature, expected)) throw new Error("Session is invalid.");
  let payload;
  try {
    payload = JSON.parse(base64UrlDecodeText(body));
  } catch (_error) {
    throw new Error("Session is invalid.");
  }
  if (payload.kind !== expectedKind) throw new Error("Session is invalid.");
  const now = Math.floor(Date.now() / 1000);
  if (Number(payload.exp || 0) < now) throw new Error("Session has expired.");
  return payload;
}

async function createUserToken(env, user) {
  const now = Math.floor(Date.now() / 1000);
  return signAccountPayload(env, {
    kind: "user",
    sub: String(user.id || ""),
    username: String(user.username || ""),
    email: String(user.email || ""),
    iat: now,
    exp: now + USER_TOKEN_TTL_SECONDS,
  });
}

function publicUser(user) {
  const email = String(user.email || "");
  const role = accountRole(user);
  return {
    id: user.id || "",
    username: user.username || "",
    email,
    email_is_generated: Boolean(user.email_is_generated) || isGeneratedEmail(email),
    site_origin: user.site_origin || SITE_ORIGIN,
    registered_site: user.registered_site || user.site_origin || SITE_ORIGIN,
    source_site: user.source_site || user.site_origin || SITE_ORIGIN,
    created_at: user.created_at || "",
    updated_at: user.updated_at || "",
    disabled: accountDisabled(user),
    disabled_at: user.disabled_at || "",
    role,
    is_super: role === "super",
    is_operator: role === "operator",
  };
}

function bearerToken(request) {
  const header = request.headers.get("Authorization") || request.headers.get("authorization") || "";
  if (header.toLowerCase().startsWith("bearer ")) return header.slice(7).trim();
  try {
    const url = new URL(request.url);
    const path = url.pathname.replace(/^\/api(?=\/)/, "");
    const downloadToken = String(url.searchParams.get("download_token") || "").trim();
    if (downloadToken && /^\/account-admin\/github-(file|artifact)$/.test(path)) return downloadToken;
  } catch (_error) {
    // Header-based auth remains the default path.
  }
  return "";
}

function supabaseBaseUrl(env) {
  const url = String(env.SUPABASE_URL || "").trim().replace(/\/+$/, "");
  if (!url || url === "unconfigured") throw new Error("Account database is not configured.");
  return url;
}

function supabaseServiceKey(env) {
  const key = String(env.SUPABASE_SERVICE_ROLE_KEY || "").trim();
  if (!key || key === "unconfigured") throw new Error("Account database is not configured.");
  return key;
}

async function supabaseRequest(env, method, path, payload = null, options = {}) {
  const key = supabaseServiceKey(env);
  const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": `Bearer ${key}`,
    "apikey": key,
  };
  if (options.prefer) headers.Prefer = options.prefer;
  else if (options.preferReturn) headers.Prefer = "return=representation";
  const timeoutMs = String(method || "GET").toUpperCase() === "GET" ? SUPABASE_TIMEOUT_MS : SUPABASE_WRITE_TIMEOUT_MS;
  const response = await fetchWithTimeout(`${supabaseBaseUrl(env)}${path}`, {
    method,
    headers,
    body: payload === null ? undefined : JSON.stringify(payload),
  }, timeoutMs);
  const text = await response.text();
  if (!response.ok) {
    throw new Error(`Account database error ${response.status}: ${text.slice(0, 300)}`);
  }
  return text ? JSON.parse(text) : null;
}

function hasSupabaseConfig(env) {
  const mode = String(env.ACCOUNT_STORE_MODE || "").trim().toLowerCase();
  const url = cleanEnv(env.SUPABASE_URL);
  const serviceKey = cleanEnv(env.SUPABASE_SERVICE_ROLE_KEY);
  if (!["supabase", "r2"].includes(mode)) {
    throw new Error("Account storage mode is not configured.");
  }
  if (mode === "supabase") {
    if (!url || !serviceKey) throw new Error("Account database configuration is incomplete.");
    return true;
  }
  if (url || serviceKey) {
    throw new Error("R2 account mode cannot be combined with Supabase credentials.");
  }
  return false;
}

function accountBucket(env) {
  if (!env.REPORT_BUCKET) throw new Error("Account storage is temporarily unavailable.");
  return env.REPORT_BUCKET;
}

async function r2GetJson(env, key) {
  const object = await accountBucket(env).get(key);
  if (!object) return null;
  try {
    return JSON.parse(await object.text());
  } catch (_error) {
    return null;
  }
}

async function r2GetJsonStrict(env, key) {
  const object = await accountBucket(env).get(key);
  if (!object) return null;
  return JSON.parse(await object.text());
}

async function r2GetJsonObjectStrict(env, key) {
  const object = await accountBucket(env).get(key);
  if (!object) return null;
  return { object, value: JSON.parse(await object.text()) };
}

async function safeR2GetJson(env, key) {
  try {
    return await r2GetJson(env, key);
  } catch (_error) {
    return null;
  }
}

async function r2PutJson(env, key, payload) {
  await accountBucket(env).put(key, JSON.stringify(payload), {
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
  return payload;
}

async function safeR2PutJson(env, key, payload) {
  try {
    await r2PutJson(env, key, payload);
    return true;
  } catch (_error) {
    return false;
  }
}

function accountKey(...parts) {
  return ["_account", ...parts.map((part) => encodeURIComponent(String(part || "")))].join("/");
}

function queryString(params) {
  const search = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => search.set(key, value));
  return search.toString();
}

async function createSiteUserInR2(env, fields) {
  const id = crypto.randomUUID ? crypto.randomUUID() : randomHex(16);
  const user = { ...fields, id };
  return writeSiteUserIndexesInR2(env, user);
}

async function writeSiteUserIndexesInR2(env, user) {
  const now = new Date().toISOString();
  const normalized = {
    ...user,
    id: user.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    updated_at: user.updated_at || now,
  };
  const keys = [accountKey("users", "id", normalized.id)];
  if (normalized.username) keys.push(accountKey("users", "username", normalized.username));
  if (normalized.email) keys.push(accountKey("users", "email", normalized.email));
  await Promise.all(keys.map((key) => r2PutJson(env, key, normalized)));
  const verified = await Promise.all(keys.map((key) => r2GetJsonStrict(env, key)));
  if (verified.some((row) => {
    try {
      return validateSiteUserRow(row, {
        id: normalized.id,
        username: normalized.username,
        email: normalized.email,
      }) !== row;
    } catch (_error) {
      return true;
    }
  })) {
    throw new Error("Account identity verification failed.");
  }
  return normalized;
}

async function repairSiteUserIndexesInR2(env, user) {
  if (!user) return null;
  // Supabase is the sole identity authority in production. Never mirror its
  // password hashes into the legacy R2 identity namespace.
  if (hasSupabaseConfig(env)) return user;
  try {
    return await writeSiteUserIndexesInR2(env, user);
  } catch (_error) {
    return user;
  }
}

async function updateSiteUserInR2(env, userId, fields) {
  const existing = await r2GetJsonStrict(env, accountKey("users", "id", userId));
  const user = { ...(existing || {}), ...fields, id: userId, updated_at: new Date().toISOString() };
  validateSiteUserRow(user, { id: userId });
  return writeSiteUserIndexesInR2(env, user);
}

function validateSiteUserRow(row, expected = {}) {
  if (row === null || row === undefined) return null;
  if (!row || typeof row !== "object" || Array.isArray(row)) {
    throw new Error("Account identity verification failed.");
  }
  const username = normalizeUsername(row.username);
  const email = normalizeEmail(row.email);
  const id = String(row.id || "").trim();
  if (!USERNAME_PATTERN.test(username) || !email || !id) {
    throw new Error("Account identity verification failed.");
  }
  if (expected.username && username !== normalizeUsername(expected.username)) {
    throw new Error("Account identity verification failed.");
  }
  if (expected.email && email !== normalizeEmail(expected.email)) {
    throw new Error("Account identity verification failed.");
  }
  if (expected.id && id !== String(expected.id)) {
    throw new Error("Account identity verification failed.");
  }
  return row;
}

async function findSiteUserByUsername(env, username) {
  const normalized = normalizeUsername(username);
  if (!USERNAME_PATTERN.test(normalized)) return null;
  if (hasSupabaseConfig(env)) {
    const query = queryString({ username: `eq.${normalized}`, site_origin: `eq.${SITE_ORIGIN}`, limit: "1" });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
    let row = Array.isArray(rows) && rows.length ? rows[0] : null;
    if (!row) {
      const fallback = queryString({ username: `eq.${normalized}`, limit: "1" });
      const fallbackRows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${fallback}`);
      row = Array.isArray(fallbackRows) && fallbackRows.length ? fallbackRows[0] : null;
    }
    return validateSiteUserRow(row, { username: normalized });
  }
  const row = await r2GetJsonStrict(env, accountKey("users", "username", normalized));
  return repairSiteUserIndexesInR2(env, validateSiteUserRow(row, { username: normalized }));
}

async function findSiteUserByEmail(env, email) {
  const normalized = normalizeEmail(email);
  if (!normalized) return null;
  if (hasSupabaseConfig(env)) {
    const query = queryString({ email: `eq.${normalized}`, site_origin: `eq.${SITE_ORIGIN}`, limit: "1" });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
    let row = Array.isArray(rows) && rows.length ? rows[0] : null;
    if (!row) {
      const fallback = queryString({ email: `eq.${normalized}`, limit: "1" });
      const fallbackRows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${fallback}`);
      row = Array.isArray(fallbackRows) && fallbackRows.length ? fallbackRows[0] : null;
    }
    return validateSiteUserRow(row, { email: normalized });
  }
  const row = await r2GetJsonStrict(env, accountKey("users", "email", normalized));
  return repairSiteUserIndexesInR2(env, validateSiteUserRow(row, { email: normalized }));
}

async function createSiteUser(env, fields) {
  if (!hasSupabaseConfig(env)) return createSiteUserInR2(env, fields);
  const rows = await supabaseRequest(env, "POST", "/rest/v1/site_users?select=*", {
    site_origin: SITE_ORIGIN,
    registered_site: SITE_ORIGIN,
    source_site: SITE_ORIGIN,
    ...fields,
  }, { preferReturn: true });
  const row = Array.isArray(rows) && rows.length ? rows[0] : fields;
  return validateSiteUserRow(row, { username: fields.username, email: fields.email });
}

async function updateSiteUser(env, userId, fields) {
  if (!hasSupabaseConfig(env)) return updateSiteUserInR2(env, userId, fields);
  const query = queryString({ id: `eq.${userId}`, select: "*" });
  const rows = await supabaseRequest(env, "PATCH", `/rest/v1/site_users?${query}`, {
    ...fields,
    updated_at: new Date().toISOString(),
  }, { preferReturn: true });
  const row = Array.isArray(rows) && rows.length ? rows[0] : null;
  return validateSiteUserRow(row, { id: userId });
}

function accountDisabled(user) {
  return Boolean(user && (user.disabled || user.account_status === "disabled" || user.status === "disabled"));
}

function disabledAccountMessage() {
  return `账号已禁用，请联系微信 ${CONTACT_WECHAT}。`;
}

function userAdminStateKeys(user = {}) {
  const keys = [];
  const email = normalizeEmail(user.email);
  const id = String(user.id || "").trim();
  if (email) keys.push(accountKey("user-state", "email", email));
  if (id) keys.push(accountKey("user-state", "id", id));
  return keys;
}

async function findUserAdminState(env, user = {}) {
  const keys = userAdminStateKeys(user);
  if (!keys.length) return {};
  const expectedEmail = normalizeEmail(user.email);
  const expectedId = String(user.id || "").trim();
  const rows = (await Promise.all(keys.map(async (key) => {
    const row = await r2GetJsonStrict(env, key);
    if (!row) return null;
    if (typeof row !== "object" || Array.isArray(row) || typeof row.disabled !== "boolean") {
      throw new Error("Account status verification failed.");
    }
    if (key.includes("/email/") && normalizeEmail(row.email) !== expectedEmail) {
      throw new Error("Account status verification failed.");
    }
    if (key.includes("/id/") && String(row.user_id || "") !== expectedId) {
      throw new Error("Account status verification failed.");
    }
    if (row.email && expectedEmail && normalizeEmail(row.email) !== expectedEmail) {
      throw new Error("Account status verification failed.");
    }
    if (row.user_id && expectedId && String(row.user_id) !== expectedId) {
      throw new Error("Account status verification failed.");
    }
    return row;
  }))).filter(Boolean);
  if (!rows.length) return {};
  rows.sort((a, b) => String(a.updated_at || "").localeCompare(String(b.updated_at || "")));
  const merged = rows.reduce((result, row) => ({ ...result, ...row }), {});
  const disabledRow = rows.find((row) => row.disabled);
  return {
    ...merged,
    disabled: rows.some((row) => row.disabled),
    disabled_at: disabledRow && disabledRow.disabled_at || merged.disabled_at || "",
    disabled_by: disabledRow && disabledRow.disabled_by || merged.disabled_by || "",
  };
}

async function mergeSiteUserAdminState(env, user) {
  if (!user) return null;
  const state = await findUserAdminState(env, user);
  return {
    ...user,
    disabled: Boolean(state.disabled),
    account_status: state.disabled ? "disabled" : "active",
    disabled_at: state.disabled_at || "",
    disabled_by: state.disabled_by || "",
  };
}

async function saveUserAdminState(env, user, fields, adminUser) {
  const now = new Date().toISOString();
  const existing = await findUserAdminState(env, user);
  const disabled = Boolean(fields.disabled);
  const payload = {
    ...existing,
    user_id: String(user.id || existing.user_id || ""),
    username: normalizeUsername(user.username || existing.username || ""),
    email: normalizeEmail(user.email || existing.email || ""),
    disabled,
    account_status: disabled ? "disabled" : "active",
    disabled_at: disabled ? (existing.disabled_at || now) : "",
    disabled_by: disabled ? (normalizeEmail(adminUser && adminUser.email) || String(adminUser && adminUser.username || "")) : "",
    updated_at: now,
    updated_by: normalizeEmail(adminUser && adminUser.email) || String(adminUser && adminUser.username || ""),
  };
  const keys = userAdminStateKeys({ ...user, ...payload });
  if (!keys.length) throw new Error("User identity is required.");
  await Promise.all(keys.map((key) => r2PutJson(env, key, payload)));
  return payload;
}

async function currentUserFromRequest(env, request) {
  const token = bearerToken(request);
  if (!token) throw new Error("Please log in.");
  const payload = await verifyAccountPayload(env, token, "user");
  const username = normalizeUsername(payload.username);
  const user = await findSiteUserByUsername(env, username);
  if (!user) throw new Error("Account not found.");
  if (
    String(payload.sub || "") !== String(user.id || "")
    || normalizeUsername(payload.username) !== normalizeUsername(user.username)
    || normalizeEmail(payload.email) !== normalizeEmail(user.email)
  ) {
    throw new Error("Session is invalid.");
  }
  const merged = await mergeSiteUserAdminState(env, user);
  if (accountDisabled(merged)) throw new Error(disabledAccountMessage());
  return merged;
}

async function siteUserPasswordMatches(env, user, password) {
  if (!user) return false;
  return verifyUserPassword(
    env,
    password,
    String(user.password_salt || ""),
    String(user.password_hash || ""),
  );
}

async function authSuccessResponse(request, env, status, user, extra = {}) {
  const repaired = await repairSiteUserIndexesInR2(env, user);
  const merged = await mergeSiteUserAdminState(env, repaired);
  if (accountDisabled(merged)) {
    return jsonResponse(request, env, 403, { detail: disabledAccountMessage() });
  }
  return jsonResponse(request, env, status, {
    token: await createUserToken(env, merged),
    user: publicUser(merged),
    ...extra,
  });
}

async function recoverExistingUserResponse(request, env, user, password) {
  const merged = await mergeSiteUserAdminState(env, user);
  if (!await siteUserPasswordMatches(env, merged, password)) return null;
  if (accountDisabled(merged)) {
    return jsonResponse(request, env, 403, { detail: disabledAccountMessage() });
  }
  return authSuccessResponse(request, env, 200, merged, { recovered: true });
}

function validateEntitlementRow(row, expectedEmail) {
  if (row === null || row === undefined) return null;
  if (!row || typeof row !== "object" || Array.isArray(row)) {
    throw new Error("Entitlement verification failed.");
  }
  const email = normalizeEmail(row.email);
  const status = String(row.status || "");
  const plan = String(row.plan || "");
  const periodEnd = row.current_period_end;
  const lastEventId = String(row.paddle_last_event_id || "").trim();
  const lastOccurredAt = String(row.paddle_last_occurred_at || "").trim();
  const paddleEventVersionValid = !lastEventId && !lastOccurredAt
    || Boolean(validPaddleEventIdentity({ event_id: lastEventId, occurred_at: lastOccurredAt }));
  if (
    !email
    || email !== normalizeEmail(expectedEmail)
    || !status
    || !plan
    || typeof row.lifetime !== "boolean"
    || !paddleEventVersionValid
    || !(periodEnd === null || (typeof periodEnd === "string" && Number.isFinite(Date.parse(periodEnd))))
  ) {
    throw new Error("Entitlement verification failed.");
  }
  return row;
}

async function findEntitlement(env, email) {
  const normalized = normalizeEmail(email);
  if (!normalized) return null;
  if (hasSupabaseConfig(env)) {
    const query = queryString({ email: `eq.${normalized}`, order: "updated_at.desc", limit: "1" });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
    const row = Array.isArray(rows) && rows.length ? rows[0] : null;
    return validateEntitlementRow(row, normalized);
  }
  return validateEntitlementRow(
    await r2GetJsonStrict(env, accountKey("entitlements", normalized)),
    normalized,
  );
}

async function saveEntitlementInR2(env, email, fields, now = new Date().toISOString()) {
  const existing = validateEntitlementRow(
    await r2GetJsonStrict(env, accountKey("entitlements", email)),
    email,
  );
  const key = accountKey("entitlements", email);
  const payload = {
    ...(existing || {}),
    ...fields,
    email,
    id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    updated_at: now,
    created_at: existing && existing.created_at || now,
  };
  validateEntitlementRow(payload, email);
  await r2PutJson(env, key, payload);
  return validateEntitlementRow(await r2GetJsonStrict(env, key), email);
}

async function saveEntitlement(env, email, fields) {
  const now = new Date().toISOString();
  if (!hasSupabaseConfig(env)) return saveEntitlementInR2(env, email, fields, now);
  const query = queryString({ email: `eq.${email}`, order: "updated_at.desc", limit: "1" });
  const existingRows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
  const existing = Array.isArray(existingRows) && existingRows.length
    ? validateEntitlementRow(existingRows[0], email)
    : null;
  const payload = {
    site_origin: SITE_ORIGIN,
    source_site: fields.source_site || SITE_ORIGIN,
    grant_source: fields.grant_source || "kcdesk",
    ...fields,
    email,
    updated_at: now,
  };
  if (existing && existing.id) {
    const patchQuery = queryString({ id: `eq.${existing.id}`, select: "*" });
    const rows = await supabaseRequest(env, "PATCH", `/rest/v1/user_entitlements?${patchQuery}`, payload, { preferReturn: true });
    return validateEntitlementRow(Array.isArray(rows) && rows.length ? rows[0] : payload, email);
  }
  const rows = await supabaseRequest(env, "POST", "/rest/v1/user_entitlements?select=*", {
    ...payload,
    created_at: now,
  }, { preferReturn: true });
  return validateEntitlementRow(Array.isArray(rows) && rows.length ? rows[0] : payload, email);
}

function validateReportPurchaseRow(row, expected = {}) {
  if (row === null || row === undefined) return null;
  if (!row || typeof row !== "object" || Array.isArray(row)) {
    throw new Error("Purchase verification failed.");
  }
  const email = normalizeEmail(row.email);
  const reportId = String(row.report_id || "");
  const source = String(row.source || "");
  const status = String(row.status || "");
  if (
    !email
    || email !== normalizeEmail(expected.email)
    || !reportId
    || reportId !== String(expected.report_id || "")
    || !source
    || source !== String(expected.source || "")
    || !status
  ) {
    throw new Error("Purchase verification failed.");
  }
  return row;
}

async function findReportPurchase(env, email, reportId, source) {
  const expected = {
    email: normalizeEmail(email),
    report_id: String(reportId || ""),
    source: String(source || ""),
  };
  if (!expected.email || !expected.report_id || !expected.source) return null;
  if (hasSupabaseConfig(env)) {
    const query = queryString({
      email: `eq.${email}`,
      report_id: `eq.${reportId}`,
      source: `eq.${source}`,
      order: "updated_at.desc",
      limit: "1",
    });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/report_purchases?${query}`);
    const row = Array.isArray(rows) && rows.length ? rows[0] : null;
    return validateReportPurchaseRow(row, expected);
  }
  return validateReportPurchaseRow(
    await r2GetJsonStrict(env, accountKey("purchases", source, reportId, email)),
    expected,
  );
}

async function saveReportPurchaseInR2(env, fields, now = new Date().toISOString()) {
  const expected = { email: fields.email, report_id: fields.report_id, source: fields.source };
  const existing = validateReportPurchaseRow(
    await r2GetJsonStrict(env, accountKey("purchases", fields.source, fields.report_id, fields.email)),
    expected,
  );
  const key = accountKey("purchases", fields.source, fields.report_id, fields.email);
  const payload = {
    ...(existing || {}),
    ...fields,
    id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    purchased_at: existing && existing.purchased_at || now,
    created_at: existing && existing.created_at || now,
    updated_at: now,
  };
  validateReportPurchaseRow(payload, expected);
  await r2PutJson(env, key, payload);
  return validateReportPurchaseRow(await r2GetJsonStrict(env, key), expected);
}

async function saveReportPurchase(env, fields) {
  const now = new Date().toISOString();
  if (!hasSupabaseConfig(env)) return saveReportPurchaseInR2(env, fields, now);
  const expected = { email: fields.email, report_id: fields.report_id, source: fields.source };
  const query = queryString({
    email: `eq.${fields.email}`,
    report_id: `eq.${fields.report_id}`,
    source: `eq.${fields.source}`,
    order: "updated_at.desc",
    limit: "1",
  });
  const existingRows = await supabaseRequest(env, "GET", `/rest/v1/report_purchases?${query}`);
  const existing = Array.isArray(existingRows) && existingRows.length
    ? validateReportPurchaseRow(existingRows[0], expected)
    : null;
  const payload = { ...fields, updated_at: now };
  if (existing && existing.id) {
    const patchQuery = queryString({ id: `eq.${existing.id}`, select: "*" });
    const rows = await supabaseRequest(env, "PATCH", `/rest/v1/report_purchases?${patchQuery}`, payload, { preferReturn: true });
    return validateReportPurchaseRow(Array.isArray(rows) && rows.length ? rows[0] : payload, expected);
  }
  const rows = await supabaseRequest(env, "POST", "/rest/v1/report_purchases?select=*", {
    ...payload,
    purchased_at: now,
    created_at: now,
  }, { preferReturn: true });
  return validateReportPurchaseRow(Array.isArray(rows) && rows.length ? rows[0] : payload, expected);
}

async function insertUsageEventInR2(env, email, eventType, metadata = {}) {
  const key = accountKey("usage", email, `${Date.now()}-${randomHex(4)}.json`);
  await r2PutJson(env, key, {
    id: crypto.randomUUID ? crypto.randomUUID() : randomHex(16),
    email,
    event_type: eventType,
    units: 1,
    metadata,
    created_at: new Date().toISOString(),
  });
}

async function insertUsageEvent(env, email, eventType, metadata = {}) {
  if (!hasSupabaseConfig(env)) return insertUsageEventInR2(env, email, eventType, metadata);
  const siteOrigin = cleanAnalyticsText(metadata && metadata.site_origin || SITE_ORIGIN, 80) || SITE_ORIGIN;
  try {
    await supabaseRequest(env, "POST", "/rest/v1/usage_events", {
      email,
      site_origin: siteOrigin,
      event_type: eventType,
      units: 1,
      metadata: { site_origin: siteOrigin, ...metadata },
    });
  } catch (_error) {
    await insertUsageEventInR2(env, email, eventType, metadata);
  }
}

function periodIsCurrent(value) {
  if (!value || typeof value !== "string") return false;
  const time = Date.parse(value);
  return Number.isFinite(time) && time > Date.now();
}

function publicEntitlement(row) {
  if (!row) {
    return {
      plan: "free",
      status: "inactive",
      lifetime: false,
      current_period_end: null,
      active: false,
    };
  }
  const status = String(row.status || "inactive");
  const lifetime = Boolean(row.lifetime);
  const currentPeriodEnd = row.current_period_end || null;
  const active = ACTIVE_STATUSES.has(status) && (lifetime || periodIsCurrent(currentPeriodEnd));
  return {
    email: row.email || "",
    plan: row.plan || "free",
    status,
    lifetime,
    current_period_end: currentPeriodEnd,
    active,
    site_origin: row.site_origin || SITE_ORIGIN,
    source_site: row.source_site || "",
    grant_source: row.grant_source || "",
    source_plan_code: row.source_plan_code || "",
    source_reference: row.source_reference || "",
    updated_at: row.updated_at || "",
  };
}

function normalizeAccessList(values, limit = 60) {
  const raw = Array.isArray(values) ? values : String(values || "").split(/[,\n，;；]+/);
  const seen = new Set();
  const items = [];
  for (const value of raw) {
    const text = String(value || "").replace(/\s+/g, " ").trim();
    if (!text) continue;
    const key = normalizeText(text);
    if (!key || seen.has(key)) continue;
    seen.add(key);
    items.push(text.slice(0, 120));
    if (items.length >= limit) break;
  }
  return items;
}

function accessGrantActive(row) {
  if (!row || typeof row !== "object") return false;
  const status = String(row.status || "inactive");
  return ACTIVE_STATUSES.has(status) && (Boolean(row.lifetime) || periodIsCurrent(row.current_period_end));
}

function cleanAccessCount(value) {
  const number = Number(value);
  return Number.isFinite(number) && number > 0 ? Math.floor(number) : 0;
}

function accessDurationSpec(value) {
  const text = String(value || "").trim();
  return ACCESS_DURATION_OPTIONS.find((option) => String(option.value) === text) || null;
}

function accessGrantDownloadLimit(row) {
  return cleanAccessCount(row && row.download_limit);
}

function accessGrantDownloadCount(row) {
  const items = Array.isArray(row && row.download_items) ? row.download_items.filter(Boolean).length : 0;
  return Math.max(cleanAccessCount(row && row.download_count), items);
}

function publicAccessGrant(row) {
  const source = row && row.source || "";
  const mode = ACCESS_MODES.has(String(row && row.access_mode || "")) ? String(row.access_mode) : "none";
  const lifetime = Boolean(row && row.lifetime);
  const currentPeriodEnd = row && row.current_period_end || null;
  const status = row && row.status || "inactive";
  const downloadLimit = accessGrantDownloadLimit(row);
  const downloadCount = accessGrantDownloadCount(row);
  return {
    email: row && row.email || "",
    access_mode: mode,
    status,
    lifetime,
    current_period_end: currentPeriodEnd,
    active: accessGrantActive(row),
    duration_value: String(row && row.duration_value || (lifetime ? "lifetime" : "")),
    download_limit: downloadLimit,
    download_count: downloadCount,
    downloads_remaining: downloadLimit ? Math.max(0, downloadLimit - downloadCount) : null,
    institutions: normalizeAccessList(row && row.institutions),
    industries: normalizeAccessList(row && row.industries),
    page_ranges: normalizeAccessList(row && row.page_ranges, ACCESS_PAGE_RANGE_OPTIONS.length)
      .filter((value) => ACCESS_PAGE_RANGE_OPTIONS.some((option) => option.value === value)),
    note: String(row && row.note || "").slice(0, 240),
    source,
    source_site: String(row && row.source_site || ""),
    grant_source: String(row && row.grant_source || ""),
    source_plan_code: String(row && row.source_plan_code || ""),
    source_reference: String(row && row.source_reference || ""),
    change_id: String(row && row.change_id || ""),
    updated_at: row && row.updated_at || "",
    updated_by: row && row.updated_by || "",
  };
}

function accessGrantBackupLatestKey(email) {
  return accountKey("access_backup", "latest", email);
}

function accessGrantBackupHistoryKey(email, timestamp, changeId = "") {
  const suffix = `${timestamp || ""}-${changeId || ""}`.replace(/[^0-9A-Za-z_-]+/g, "-");
  return accountKey("access_backup", "history", email, suffix);
}

function accessGrantAuditKey(email, timestamp, changeId = "") {
  const suffix = `${timestamp || ""}-${changeId || ""}`.replace(/[^0-9A-Za-z_-]+/g, "-");
  return accountKey("access_audit", email, suffix);
}

function accessGrantComparable(row) {
  const access = publicAccessGrant(row);
  return {
    email: normalizeEmail(access.email),
    access_mode: access.access_mode,
    status: access.status,
    lifetime: Boolean(access.lifetime),
    current_period_end: access.current_period_end || null,
    duration_value: access.duration_value || "",
    download_limit: access.download_limit || 0,
    download_count: access.download_count || 0,
    download_items: access.download_items,
    institutions: access.institutions,
    industries: access.industries,
    page_ranges: access.page_ranges,
    note: access.note || "",
    change_id: access.change_id || "",
  };
}

function accessGrantMatchesExpected(actual, expected) {
  return JSON.stringify(accessGrantComparable(actual)) === JSON.stringify(accessGrantComparable(expected));
}

function validateAccessGrantRow(row, expectedEmail) {
  if (row === null || row === undefined) return null;
  if (!row || typeof row !== "object" || Array.isArray(row)) {
    throw new Error("Access record verification failed.");
  }
  const email = normalizeEmail(row.email);
  const mode = String(row.access_mode || "");
  const status = String(row.status || "");
  const periodEnd = row.current_period_end;
  const listFieldsValid = [row.institutions, row.industries, row.page_ranges, row.download_items]
    .every((value) => Array.isArray(value) && value.every((item) => typeof item === "string"));
  const downloadLimit = row.download_limit;
  const downloadCount = row.download_count;
  const uniqueDownloadItems = Array.isArray(row.download_items)
    ? [...new Set(row.download_items.filter(Boolean))]
    : [];
  const quotaValid = Number.isInteger(downloadLimit)
    && downloadLimit >= 0
    && Number.isInteger(downloadCount)
    && downloadCount >= 0
    && downloadCount === uniqueDownloadItems.length
    && uniqueDownloadItems.length === (Array.isArray(row.download_items) ? row.download_items.length : 0)
    && (String(row.duration_value || "") === TRIAL_3D_DURATION_VALUE
      ? downloadLimit === TRIAL_3D_DOWNLOAD_LIMIT
      : downloadLimit === 0)
    && (downloadLimit === 0 || downloadCount <= downloadLimit);
  if (
    !email
    || email !== normalizeEmail(expectedEmail)
    || !String(row.id || "").trim()
    || !ACCESS_MODES.has(mode)
    || !["active", "inactive"].includes(status)
    || typeof row.lifetime !== "boolean"
    || !listFieldsValid
    || !quotaValid
    || !(periodEnd === null || (typeof periodEnd === "string" && Number.isFinite(Date.parse(periodEnd))))
    || (mode === "none") !== (status === "inactive")
    || (row.lifetime && periodEnd !== null)
    || (!row.lifetime && status === "active" && !periodEnd)
  ) {
    throw new Error("Access record verification failed.");
  }
  return row;
}

async function findStoredAccessGrantSnapshot(env, email) {
  const normalized = normalizeEmail(email);
  if (!normalized) return { record: null, etag: "" };
  // The primary record is the only authorization source. Backups are retained
  // for audit/recovery by an administrator, but an older or partially written
  // backup must never silently restore broader access.
  const snapshot = await r2GetJsonObjectStrict(env, accountKey("access", normalized));
  const record = validateAccessGrantRow(snapshot && snapshot.value, normalized);
  const etag = String(snapshot && snapshot.object && snapshot.object.etag || "");
  if (snapshot && !etag) throw new Error("Access record version verification failed.");
  return { record, etag };
}

async function findStoredAccessGrant(env, email) {
  return (await findStoredAccessGrantSnapshot(env, email)).record;
}

function vid2PptTrialAccessKey(email) {
  return accountKey("vid2ppt_trial", normalizeEmail(email));
}

function vid2PptTrialAccessBackupLatestKey(email) {
  return accountKey("vid2ppt_trial_backup", "latest", normalizeEmail(email));
}

function vid2PptTrialAccessBackupHistoryKey(email, timestamp, changeId = "") {
  const suffix = `${timestamp || ""}-${changeId || ""}`.replace(/[^0-9A-Za-z_-]+/g, "-");
  return accountKey("vid2ppt_trial_backup", "history", normalizeEmail(email), suffix);
}

async function findStoredVid2PptTrialAccessSnapshot(env, email) {
  const normalized = normalizeEmail(email);
  if (!normalized) return { record: null, etag: "" };
  const snapshot = await r2GetJsonObjectStrict(env, vid2PptTrialAccessKey(normalized));
  const record = validateAccessGrantRow(snapshot && snapshot.value, normalized);
  const etag = String(snapshot && snapshot.object && snapshot.object.etag || "");
  if (snapshot && !etag) throw new Error("Trial access record version verification failed.");
  return { record, etag };
}

async function writeVid2PptTrialAccessRecoveryCopies(env, email, payload) {
  const normalized = normalizeEmail(email);
  const timestamp = payload.quota_updated_at || payload.updated_at || new Date().toISOString();
  const keys = [
    vid2PptTrialAccessBackupLatestKey(normalized),
    vid2PptTrialAccessBackupHistoryKey(normalized, timestamp, payload.change_id),
  ];
  const results = await Promise.allSettled(keys.map(async (key) => {
    await r2PutJson(env, key, payload);
    const saved = validateAccessGrantRow(await r2GetJsonStrict(env, key), normalized);
    if (!accessGrantMatchesExpected(saved, payload)) throw new Error("Trial access backup verification failed.");
  }));
  return {
    backup_count: results.filter((result) => result.status === "fulfilled").length,
    backup_error: results.some((result) => result.status === "rejected"),
  };
}

async function writeVid2PptTrialAccessDurably(env, email, payload, expectedEtag) {
  const normalized = normalizeEmail(email);
  const key = vid2PptTrialAccessKey(normalized);
  validateAccessGrantRow(payload, normalized);
  const onlyIf = expectedEtag
    ? { etagMatches: String(expectedEtag) }
    : { etagDoesNotMatch: "*" };
  const written = await accountBucket(env).put(key, JSON.stringify(payload), {
    onlyIf,
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
  if (written === null) {
    const error = new Error("体验权益已被其他操作更新，请重试。");
    error.code = "ACCESS_CONFLICT";
    throw error;
  }
  const saved = validateAccessGrantRow(await r2GetJsonStrict(env, key), normalized);
  if (!accessGrantMatchesExpected(saved, payload)) throw new Error("Trial access save verification failed.");
  const backups = await writeVid2PptTrialAccessRecoveryCopies(env, normalized, payload);
  return { record: saved, ...backups };
}

async function findVid2PptTrialAccess(env, email) {
  const normalized = normalizeEmail(email);
  if (!normalized) return publicAccessGrant(null);
  const snapshot = await findStoredVid2PptTrialAccessSnapshot(env, normalized);
  if (snapshot.record) {
    return publicAccessGrant({ ...snapshot.record, email: normalized, source: "vid2ppt_trial" });
  }
  return publicAccessGrant({ email: normalized, source: "none" });
}

async function writeAccessGrantRecoveryCopies(env, email, payload) {
  const normalized = normalizeEmail(email);
  const timestamp = payload.quota_updated_at || payload.updated_at || new Date().toISOString();
  const latestKey = accessGrantBackupLatestKey(normalized);
  const historyKey = accessGrantBackupHistoryKey(normalized, timestamp, payload.change_id);
  const backupResults = await Promise.allSettled([
    (async () => {
      await r2PutJson(env, latestKey, payload);
      const saved = validateAccessGrantRow(await r2GetJsonStrict(env, latestKey), normalized);
      if (!accessGrantMatchesExpected(saved, payload)) throw new Error("Latest backup verification failed.");
    })(),
    (async () => {
      await r2PutJson(env, historyKey, payload);
      const saved = validateAccessGrantRow(await r2GetJsonStrict(env, historyKey), normalized);
      if (!accessGrantMatchesExpected(saved, payload)) throw new Error("History backup verification failed.");
    })(),
  ]);
  return {
    backup_count: backupResults.filter((result) => result.status === "fulfilled").length,
    backup_error: backupResults.some((result) => result.status === "rejected"),
  };
}

async function writeAccessGrantDurably(env, email, payload, expectedEtag) {
  const normalized = normalizeEmail(email);
  const primaryKey = accountKey("access", normalized);
  validateAccessGrantRow(payload, normalized);
  // The primary record is the sole authorization commit point. In particular,
  // narrowing or revoking access must not be held back by a backup failure.
  const onlyIf = expectedEtag
    ? { etagMatches: String(expectedEtag) }
    : { etagDoesNotMatch: "*" };
  const written = await accountBucket(env).put(primaryKey, JSON.stringify(payload), {
    onlyIf,
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
  if (written === null) {
    const error = new Error("权限记录已被其他操作更新，请刷新后重试。");
    error.code = "ACCESS_CONFLICT";
    throw error;
  }
  const primary = validateAccessGrantRow(await r2GetJsonStrict(env, primaryKey), normalized);
  if (!accessGrantMatchesExpected(primary, payload)) {
    throw new Error("Access save verification failed. Please retry.");
  }
  const backups = await writeAccessGrantRecoveryCopies(env, normalized, payload);
  return { record: primary, ...backups };
}

async function writeAccessGrantAudit(env, email, previous, next, adminUser) {
  const normalized = normalizeEmail(email);
  const timestamp = next && next.updated_at || new Date().toISOString();
  const audit = {
    type: "user_access_update",
    email: normalized,
    updated_at: timestamp,
    updated_by: normalizeEmail(adminUser && adminUser.email) || String(adminUser && adminUser.username || ""),
    previous: previous ? publicAccessGrant(previous) : publicAccessGrant(null),
    next: next ? publicAccessGrant(next) : publicAccessGrant(null),
  };
  await r2PutJson(env, accessGrantAuditKey(normalized, timestamp, next && next.change_id), audit);
  return audit;
}

async function findAccessGrant(env, email) {
  const normalized = normalizeEmail(email);
  if (!normalized) return publicAccessGrant(null);
  const stored = await findStoredAccessGrant(env, normalized);
  if (stored && typeof stored === "object") {
    return publicAccessGrant({ ...stored, email: normalized, source: "stored" });
  }
  return publicAccessGrant({ email: normalized, source: "none" });
}

function accessDurationEndIso(durationMonths) {
  const text = String(durationMonths || "").trim();
  if (text === "lifetime") return null;
  const spec = accessDurationSpec(text);
  if (spec && Number(spec.days || 0) > 0) {
    const date = new Date();
    date.setUTCDate(date.getUTCDate() + Math.min(365, Math.round(Number(spec.days))));
    return date.toISOString();
  }
  const months = Number(text);
  if (!Number.isFinite(months) || months <= 0) return null;
  const date = new Date();
  date.setUTCMonth(date.getUTCMonth() + Math.min(120, Math.round(months)));
  return date.toISOString();
}

function accessDurationDownloadLimit(durationValue) {
  const spec = accessDurationSpec(durationValue);
  return cleanAccessCount(spec && spec.download_limit);
}

function explicitAccessEndIso(value) {
  const date = String(value || "").trim();
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return null;
  // Admin dates are Beijing business dates. End them at 23:59:59.999
  // Asia/Shanghai (UTC+08:00), not eight hours into the following day.
  const parsed = new Date(`${date}T15:59:59.999Z`);
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === date
    ? parsed.toISOString()
    : null;
}

async function saveAccessGrant(env, email, fields, adminUser) {
  const normalized = normalizeEmail(email);
  if (!normalized) throw new Error("Email is required.");
  const snapshot = await findStoredAccessGrantSnapshot(env, normalized);
  const existing = snapshot.record;
  const expectedChangeId = String(fields.expected_change_id || "");
  const expectedUpdatedAt = String(fields.expected_updated_at || "");
  if (existing) {
    const versionMatches = existing.change_id
      ? expectedChangeId === String(existing.change_id)
      : expectedUpdatedAt === String(existing.updated_at || "");
    if (!versionMatches) {
      const error = new Error("权限记录已变化，请刷新后再保存。");
      error.code = "ACCESS_CONFLICT";
      throw error;
    }
  } else if (expectedChangeId || expectedUpdatedAt) {
    const error = new Error("权限记录已变化，请刷新后再保存。");
    error.code = "ACCESS_CONFLICT";
    throw error;
  }
  const mode = ACCESS_MODES.has(String(fields.access_mode || "")) ? String(fields.access_mode) : "none";
  const activeMode = mode !== "none";
  const duration = String(fields.duration_months || "").trim();
  const lifetime = activeMode && duration === "lifetime";
  const durationValue = activeMode ? (duration || "1") : "";
  const renew = Boolean(fields.renew);
  const expiresOn = String(fields.expires_on || "").trim();
  const explicitEnd = activeMode && !lifetime && !renew ? explicitAccessEndIso(expiresOn) : null;
  if (activeMode && !lifetime && !renew && expiresOn && !explicitEnd) {
    throw new Error("到期日期格式无效。");
  }
  const preserveExistingExpiry = Boolean(
    activeMode
    && existing
    && !renew
    && String(existing.duration_value || "") === durationValue,
  );
  const currentPeriodEnd = activeMode
    ? (lifetime
      ? null
      : explicitEnd
        ? (existing && String(existing.current_period_end || "").slice(0, 10) === expiresOn ? existing.current_period_end : explicitEnd)
        : preserveExistingExpiry
          ? existing.current_period_end
          : accessDurationEndIso(durationValue))
    : null;
  const now = new Date().toISOString();
  const downloadLimit = activeMode ? accessDurationDownloadLimit(duration) : 0;
  const sameLimitedGrant = Boolean(
    downloadLimit &&
    existing &&
    String(existing.duration_value || "") === duration &&
    accessGrantActive(existing),
  );
  const existingItems = Array.isArray(existing && existing.download_items) ? existing.download_items.map(String).filter(Boolean) : [];
  const downloadItems = sameLimitedGrant ? [...new Set(existingItems)].slice(0, downloadLimit) : [];
  const payload = {
    ...(existing || {}),
    email: normalized,
    access_mode: mode,
    status: activeMode ? "active" : "inactive",
    lifetime,
    current_period_end: currentPeriodEnd,
    duration_value: durationValue,
    download_limit: downloadLimit,
    download_count: downloadLimit ? downloadItems.length : 0,
    download_items: downloadLimit ? downloadItems : [],
    institutions: mode === "filters" ? normalizeAccessList(fields.institutions) : [],
    industries: mode === "filters" ? normalizeAccessList(fields.industries) : [],
    page_ranges: mode === "filters"
      ? normalizeAccessList(fields.page_ranges, ACCESS_PAGE_RANGE_OPTIONS.length)
        .filter((value) => ACCESS_PAGE_RANGE_OPTIONS.some((option) => option.value === value))
      : [],
    note: String(fields.note || "").slice(0, 240),
    id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    change_id: crypto.randomUUID ? crypto.randomUUID() : randomHex(16),
    created_at: existing && existing.created_at || now,
    updated_at: now,
    updated_by: normalizeEmail(adminUser && adminUser.email) || String(adminUser && adminUser.username || ""),
  };
  const writeResult = await writeAccessGrantDurably(env, normalized, payload, snapshot.etag);
  let auditSaved = true;
  try {
    await writeAccessGrantAudit(env, normalized, existing, writeResult.record, adminUser);
  } catch (_error) {
    auditSaved = false;
  }
  return {
    access: publicAccessGrant({ ...writeResult.record, source: "stored" }),
    durability: {
      primary_verified: true,
      backup_count: writeResult.backup_count,
      audit_saved: auditSaved,
      warning: Boolean(writeResult.backup_error || !auditSaved),
    },
  };
}

function accessPageRangeMatches(range, pages) {
  if (!pages) return false;
  if (range === "under5") return pages <= 5;
  if (range === "5_10") return pages >= 5 && pages <= 10;
  if (range === "10_20") return pages >= 10 && pages <= 20;
  if (range === "over20") return pages >= 20;
  return false;
}

function accessGrantMatchesReport(grant, report, source) {
  const access = publicAccessGrant(grant);
  if (!access.active) return false;
  if (access.access_mode === "all") return true;
  if (access.access_mode !== "filters" || source !== "catalog" || !report) return false;
  const institutionFilters = access.institutions.map(normalizeText).filter(Boolean);
  const industryFilters = access.industries.map(normalizeText).filter(Boolean);
  const pageFilters = access.page_ranges;

  if (institutionFilters.length) {
    const reportInstitutions = [
      report.bank_code,
      report.bank_name,
      reportBankLabel(report),
    ].map(normalizeText).filter(Boolean);
    if (!institutionFilters.some((filter) => reportInstitutions.includes(filter))) {
      return false;
    }
  }

  if (industryFilters.length) {
    const industry = normalizeText(inferReportIndustry(report));
    if (!industryFilters.includes(industry)) {
      return false;
    }
  }

  if (pageFilters.length) {
    const pages = reportPageCount(report);
    if (!pageFilters.some((range) => accessPageRangeMatches(range, pages))) return false;
  }

  return Boolean(institutionFilters.length || industryFilters.length || pageFilters.length);
}

function accessGrantDownloadItemKey(reportId, source) {
  return `${String(source || "catalog")}:${String(reportId || "").trim()}`;
}

function limitedAccessNeedsConsumption(access) {
  const grant = publicAccessGrant(access);
  return grant.active && grant.download_limit > 0;
}

async function consumeLimitedAccessDownload(env, email, reportId, source, expectedChangeId = "", storageKind = "access") {
  const normalized = normalizeEmail(email);
  if (!normalized) return { ok: true, access: publicAccessGrant(null) };
  const itemKey = accessGrantDownloadItemKey(reportId, source);
  const trialStorage = storageKind === "vid2ppt_trial";
  const key = trialStorage ? vid2PptTrialAccessKey(normalized) : accountKey("access", normalized);
  for (let attempt = 0; attempt < 5; attempt += 1) {
    const snapshot = await r2GetJsonObjectStrict(env, key);
    const stored = validateAccessGrantRow(snapshot && snapshot.value, normalized);
    const access = publicAccessGrant(stored);
    if (!snapshot || !stored || !limitedAccessNeedsConsumption(access)) {
      return {
        ok: false,
        status: 409,
        limit_exceeded: false,
        access,
        error: "Download access could not be verified. Please retry.",
        contact: CONTACT_WECHAT,
      };
    }
    if (String(stored.change_id || "") !== String(expectedChangeId || "")) {
      return {
        ok: false,
        status: 409,
        limit_exceeded: false,
        access,
        error: "下载权限刚刚发生变化，请刷新后重试。",
        contact: CONTACT_WECHAT,
      };
    }
    const etag = String(snapshot.object && snapshot.object.etag || "");
    if (!etag) {
      return {
        ok: false,
        status: 503,
        limit_exceeded: false,
        access,
        error: "Download quota could not be verified. Please retry.",
        contact: CONTACT_WECHAT,
      };
    }
    const existingItems = Array.isArray(stored.download_items) ? stored.download_items.map(String) : [];
    const uniqueItems = [...new Set(existingItems.filter(Boolean))];
    if (uniqueItems.includes(itemKey)) return { ok: true, access };
    if (uniqueItems.length >= access.download_limit) {
      return {
        ok: false,
        status: 403,
        limit_exceeded: true,
        access,
        error: TRIAL_LIMIT_MESSAGE,
        contact: CONTACT_WECHAT,
      };
    }
    const updatedItems = [...uniqueItems, itemKey];
    const updated = {
      ...stored,
      email: normalized,
      download_items: updatedItems,
      download_count: updatedItems.length,
      // Quota consumption is not a permission-policy edit. Keep the editor
      // version stable while the R2 ETag protects the quota counter itself.
      change_id: String(stored.change_id || ""),
      updated_at: stored.updated_at || new Date().toISOString(),
      quota_updated_at: new Date().toISOString(),
    };
    validateAccessGrantRow(updated, normalized);
    const written = await accountBucket(env).put(key, JSON.stringify(updated), {
      onlyIf: { etagMatches: etag },
      httpMetadata: { contentType: "application/json; charset=utf-8" },
    });
    if (written === null) continue;
    const verified = validateAccessGrantRow(await r2GetJsonStrict(env, key), normalized);
    if (!accessGrantMatchesExpected(verified, updated)) continue;
    if (trialStorage) {
      await writeVid2PptTrialAccessRecoveryCopies(env, normalized, updated);
    } else {
      await writeAccessGrantRecoveryCopies(env, normalized, updated);
    }
    return {
      ok: true,
      access: publicAccessGrant({ ...verified, source: trialStorage ? "vid2ppt_trial" : "stored" }),
      storage_kind: storageKind,
    };
  }
  return {
    ok: false,
    status: 409,
    limit_exceeded: false,
    access: publicAccessGrant({ email: normalized, source: "error" }),
    error: "Download quota changed concurrently. Please retry.",
    contact: CONTACT_WECHAT,
  };
}

function superEntitlement(user) {
  return {
    email: normalizeEmail(user && user.email) || "",
    plan: accountRole(user),
    status: "active",
    lifetime: true,
    current_period_end: null,
    active: true,
    updated_at: new Date().toISOString(),
  };
}

function roleAccessForUser(user) {
  return publicAccessGrant({
    email: normalizeEmail(user && user.email),
    access_mode: "all",
    status: "active",
    lifetime: true,
    source: "role",
    updated_at: "",
  });
}

function effectiveAccessForUser(user, entitlementRow, accessRow, trialAccessRow = null) {
  if (accountDisabled(user)) {
    return publicAccessGrant({
      email: normalizeEmail(user && user.email),
      source: "disabled",
    });
  }
  if (isPrivilegedAccount(user)) return roleAccessForUser(user);
  const access = publicAccessGrant(accessRow);
  const trialAccess = publicAccessGrant(trialAccessRow);
  if (access.source === "error") return access;
  if (trialAccess.source === "error") return trialAccess;
  const entitlement = publicEntitlement(entitlementRow);
  if (entitlement.active && entitlement.plan === "annual") {
    const entitlementSource = VID2PPT_GIFT_SOURCES.has(entitlement.grant_source)
      ? entitlement.grant_source
      : (access.active ? "entitlement+stored" : "entitlement");
    const entitlementAccess = publicAccessGrant({
      email: normalizeEmail(user && user.email),
      access_mode: "all",
      status: "active",
      lifetime: entitlement.lifetime,
      current_period_end: entitlement.current_period_end,
      source: entitlementSource,
      grant_source: entitlement.grant_source,
      source_site: entitlement.source_site,
      source_plan_code: entitlement.source_plan_code,
      source_reference: entitlement.source_reference,
      updated_at: entitlement.updated_at,
    });
    if (access.active && access.access_mode === "all") {
      const accessEnd = access.lifetime ? Number.POSITIVE_INFINITY : Date.parse(access.current_period_end || "");
      const entitlementEnd = entitlementAccess.lifetime
        ? Number.POSITIVE_INFINITY
        : Date.parse(entitlementAccess.current_period_end || "");
      if (accessEnd > entitlementEnd) return publicAccessGrant({ ...access, source: "entitlement+stored" });
    }
    return entitlementAccess;
  }
  if (access.active && access.access_mode === "all" && access.download_limit === 0) return access;
  if (trialAccess.active && trialAccess.access_mode === "all") return trialAccess;
  return access.active ? access : trialAccess;
}

function shouldConsumeAccessGrantDownload(accessResult) {
  if (!accessResult) return null;
  const entitlementProvidesAccess = accessResult.effective_access
    && String(accessResult.effective_access.source || "").includes("entitlement");
  const purchased = Boolean(accessResult.purchase);
  if (entitlementProvidesAccess || purchased) return null;
  if (accessResult.custom_access_matched) {
    return limitedAccessNeedsConsumption(accessResult.access)
      ? { storage_kind: "access", grant: accessResult.access }
      : null;
  }
  if (accessResult.trial_access_matched && limitedAccessNeedsConsumption(accessResult.trial_access)) {
    return { storage_kind: "vid2ppt_trial", grant: accessResult.trial_access };
  }
  return null;
}

async function reportAccessForUser(env, user, reportId, source) {
  const email = normalizeEmail(user.email);
  if (!email) {
    const noAccess = publicAccessGrant({ source: "none" });
    return {
      can_download: false,
      entitlement: publicEntitlement(null),
      access: noAccess,
      trial_access: noAccess,
      effective_access: noAccess,
      purchase: null,
    };
  }
  if (isPrivilegedAccount(user)) {
    const roleAccess = roleAccessForUser(user);
    return {
      can_download: true,
      entitlement: superEntitlement(user),
      access: roleAccess,
      trial_access: publicAccessGrant(null),
      effective_access: roleAccess,
      purchase: null,
    };
  }
  const [entitlementRow, purchase, accessRow, trialAccessRow] = await Promise.all([
    findEntitlement(env, email),
    reportId ? findReportPurchase(env, email, reportId, source) : Promise.resolve(null),
    findAccessGrant(env, email),
    findVid2PptTrialAccess(env, email),
  ]);
  const entitlement = publicEntitlement(entitlementRow);
  const access = publicAccessGrant(accessRow);
  const trialAccess = publicAccessGrant(trialAccessRow);
  // Existing business policy is additive: annual, a custom grant, an exact
  // report purchase, or a privileged role can independently allow a download.
  const annual = entitlement.active && entitlement.plan === "annual";
  const purchased = purchase && ACTIVE_STATUSES.has(String(purchase.status || ""));
  let customAccess = false;
  if (access.active) {
    if (access.access_mode === "all") {
      customAccess = true;
    } else if (reportId && source === "catalog") {
      const catalog = await loadCatalog(env);
      customAccess = accessGrantMatchesReport(access, findReport(catalog, reportId), source);
    }
  }
  const trialAccessMatched = trialAccess.active && trialAccess.access_mode === "all";
  const effectiveAccess = effectiveAccessForUser(user, entitlementRow, accessRow, trialAccessRow);
  return {
    can_download: Boolean(annual || customAccess || trialAccessMatched || purchased),
    entitlement,
    access,
    trial_access: trialAccess,
    effective_access: effectiveAccess,
    purchase: purchased ? purchase : null,
    custom_access_matched: customAccess,
    trial_access_matched: trialAccessMatched,
  };
}

async function accountDownloadDecision(env, request, reportId, source) {
  try {
    const user = await currentUserFromRequest(env, request);
    const access = await reportAccessForUser(env, user, reportId, source);
    if (!access.can_download) {
      return {
        allowed: false,
        user,
        access,
        status: 402,
        error: "Please log in, purchase this report, or enter the report password.",
      };
    }
    const limitedAccess = shouldConsumeAccessGrantDownload(access);
    return {
      allowed: true,
      user,
      access,
      consume_limited_access: Boolean(limitedAccess),
      limited_access: limitedAccess,
    };
  } catch (error) {
    const status = accessErrorStatus(error);
    return {
      allowed: false,
      status,
      error: status === 503
        ? "下载权限暂时无法核验，请稍后重试。"
        : error && error.message || "Please log in.",
    };
  }
}

async function finalizeAccountDownloadDecision(env, request, decision, reportId, source) {
  if (!decision || !decision.allowed) return { ok: true };
  try {
    const user = await currentUserFromRequest(env, request);
    if (String(user.id || "") !== String(decision.user && decision.user.id || "")) {
      return { ok: false, status: 409, limit_exceeded: false, error: "下载权限已发生变化，请重试。", contact: CONTACT_WECHAT };
    }
    const refreshedAccess = await reportAccessForUser(env, user, reportId, source);
    if (!refreshedAccess.can_download) {
      return { ok: false, status: 403, limit_exceeded: false, error: "下载权限已失效，请刷新后重试。", contact: CONTACT_WECHAT };
    }
    decision.user = user;
    decision.access = refreshedAccess;
    decision.limited_access = shouldConsumeAccessGrantDownload(refreshedAccess);
    decision.consume_limited_access = Boolean(decision.limited_access);
  } catch (_error) {
    return { ok: false, status: 503, limit_exceeded: false, error: "下载权限暂时无法核验，请稍后重试。", contact: CONTACT_WECHAT };
  }
  if (!decision.consume_limited_access) return { ok: true };
  const email = normalizeEmail(decision.user && decision.user.email);
  let consumed;
  try {
    consumed = await consumeLimitedAccessDownload(
      env,
      email,
      reportId,
      source,
      decision.limited_access && decision.limited_access.grant && decision.limited_access.grant.change_id,
      decision.limited_access && decision.limited_access.storage_kind || "access",
    );
  } catch (_error) {
    return { ok: false, status: 503, limit_exceeded: false, error: "下载权限暂时无法核验，请稍后重试。", contact: CONTACT_WECHAT };
  }
  if (!consumed.ok) return consumed;
  decision.access = {
    ...(decision.access || {}),
    [consumed.storage_kind === "vid2ppt_trial" ? "trial_access" : "access"]: consumed.access,
    effective_access: consumed.access,
  };
  return { ok: true, access: consumed.access };
}

async function accountCanDownload(env, request, reportId, source) {
  const decision = await accountDownloadDecision(env, request, reportId, source);
  return Boolean(decision.allowed);
}

async function captchaAnswerHash(env, answer, nonce) {
  return hmacSha256Hex(accountSecret(env), `captcha:${nonce}:${answer}`);
}

function captchaSvg(question) {
  const rotate = randomInt(-5, 5);
  const lineA = randomInt(12, 28);
  const lineB = randomInt(84, 108);
  const dotA = randomInt(24, 132);
  const dotB = randomInt(18, 50);
  return `<svg xmlns="http://www.w3.org/2000/svg" width="180" height="64" viewBox="0 0 180 64" role="img" aria-label="captcha">
  <rect width="180" height="64" rx="14" fill="#f8fafc"/>
  <path d="M8 ${lineA} C52 2, 92 68, 172 ${lineB}" fill="none" stroke="#99f6e4" stroke-width="3" opacity=".8"/>
  <path d="M4 ${lineB} C48 70, 118 -4, 176 ${lineA}" fill="none" stroke="#bfdbfe" stroke-width="3" opacity=".8"/>
  <circle cx="${dotA}" cy="${dotB}" r="4" fill="#fbbf24" opacity=".75"/>
  <text x="90" y="42" text-anchor="middle" transform="rotate(${rotate} 90 32)" fill="#111827" font-size="28" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-weight="900">${question}</text>
</svg>`;
}

async function createCaptchaChallenge(env) {
  const left = randomInt(2, 9);
  const right = randomInt(1, 9);
  const answer = String(left + right);
  const nonce = randomHex(12);
  const now = Math.floor(Date.now() / 1000);
  const token = await signAccountPayload(env, {
    kind: "captcha",
    nonce,
    answer_hash: await captchaAnswerHash(env, answer, nonce),
    iat: now,
    exp: now + CAPTCHA_TTL_SECONDS,
  });
  const svg = captchaSvg(`${left} + ${right} = ?`);
  return {
    token,
    image: `data:image/svg+xml;base64,${btoa(svg)}`,
    expires_in: CAPTCHA_TTL_SECONDS,
  };
}

async function verifyCaptchaResponse(env, token, answer) {
  try {
    const payload = await verifyAccountPayload(env, token, "captcha");
    const clean = String(answer || "").replace(/\D+/g, "");
    if (!clean || !payload.nonce || !payload.answer_hash) return false;
    const actual = await captchaAnswerHash(env, clean, payload.nonce);
    return constantTimeEqual(actual, payload.answer_hash);
  } catch (_error) {
    return false;
  }
}

async function passwordMatches(env, group, password) {
  const expected = String(group.password_sha256 || "");
  if (!expected || expected === "REPLACE_WITH_SHA256_HASH") {
    throw new Error(`Password hash is not configured for group: ${group.id}`);
  }
  if (!env.PASSWORD_SECRET) throw new Error("PASSWORD_SECRET is not configured");
  const actual = await sha256Hex(`${env.PASSWORD_SECRET}:${password}`);
  return actual === expected.toLowerCase();
}

async function defaultPasswordMatches(env, password) {
  const master = String(env.MASTER_KEY || "").trim();
  if (master && normalizePassword(password) === normalizePassword(master)) return true;

  try {
    const rules = await loadRules(env);
    const group = findPasswordGroup(rules, rules.default_group);
    return group ? await passwordMatches(env, group, password) : false;
  } catch (_error) {
    return false;
  }
}

async function sharedReportPasswordMatches(env, id, password) {
  if (!password) return false;
  try {
    if (await derivedPasswordMatches(env, id, password)) return true;
  } catch (_error) {
    // Fall through to the shared password.
  }
  return defaultPasswordMatches(env, password);
}

async function handleCaptcha(request, env) {
  try {
    return jsonResponse(request, env, 200, await createCaptchaChallenge(env));
  } catch (_error) {
    return jsonResponse(request, env, 503, { detail: "Account service is temporarily unavailable." });
  }
}

async function handleAuth(request, env) {
  if (request.method === "GET") {
    try {
      const user = await currentUserFromRequest(env, request);
      return jsonResponse(request, env, 200, {
        token: await createUserToken(env, user),
        user: publicUser(user),
      });
    } catch (error) {
      return jsonResponse(request, env, 401, { detail: error.message || "Please log in." });
    }
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const action = String(payload.action || "login").trim().toLowerCase();
  const username = normalizeUsername(payload.username);
  const password = String(payload.password || "");
  if (!["login", "register"].includes(action)) {
    return jsonResponse(request, env, 400, { detail: "Unsupported auth action." });
  }
  if (!(await verifyCaptchaResponse(env, String(payload.captcha_token || ""), String(payload.captcha_answer || "")))) {
    return jsonResponse(request, env, 400, { detail: "验证码不正确或已过期。" });
  }
  if (!USERNAME_PATTERN.test(username)) {
    return jsonResponse(request, env, 400, { detail: "用户名需为 3-32 位小写字母、数字、点、短横线或下划线。" });
  }
  if (password.length < 4 || password.length > 128) {
    return jsonResponse(request, env, 400, { detail: "密码需为 4-128 位。" });
  }

  try {
    if (action === "register") {
      const existing = await findSiteUserByUsername(env, username);
      if (existing) {
        const recovered = await recoverExistingUserResponse(request, env, existing, password);
        if (recovered) return recovered;
        return jsonResponse(request, env, 409, { detail: "用户名已被注册。" });
      }
      const rawEmail = String(payload.email || "");
      const email = normalizeEmail(rawEmail);
      if (!email) {
        return jsonResponse(request, env, 400, { detail: "注册必须填写有效邮箱。" });
      }
      if (isReservedPrivilegedIdentity(username, email)) {
        return jsonResponse(request, env, 403, { detail: "该用户名或邮箱为系统保留身份。" });
      }
      const existingEmail = await findSiteUserByEmail(env, email);
      if (existingEmail) {
        const recovered = await recoverExistingUserResponse(request, env, existingEmail, password);
        if (recovered) return recovered;
        return jsonResponse(request, env, 409, { detail: "用户名或邮箱已被注册。" });
      }
      const now = new Date().toISOString();
      const passwordFields = await hashUserPassword(env, password);
      const fields = {
        username,
        email,
        email_is_generated: false,
        ...passwordFields,
        created_at: now,
        updated_at: now,
        last_login_at: now,
      };
      let user;
      try {
        user = await createSiteUser(env, fields);
      } catch (error) {
        const recovered = await recoverExistingUserResponse(request, env, await findSiteUserByUsername(env, username), password);
        if (recovered) return recovered;
        throw error;
      }
      const emailDestination = await requestCloudflareDestinationVerification(env, email);
      return authSuccessResponse(request, env, 201, user, { email_destination: emailDestination });
    }

    const user = await findSiteUserByUsername(env, username);
    const ok = await siteUserPasswordMatches(env, user, password);
    if (!ok) return jsonResponse(request, env, 401, { detail: "用户名或密码不正确。" });
    const repaired = await repairSiteUserIndexesInR2(env, user);
    const updated = repaired.id ? await updateSiteUser(env, repaired.id, { last_login_at: new Date().toISOString() }) : repaired;
    const merged = { ...repaired, ...updated };
    return authSuccessResponse(request, env, 200, merged);
  } catch (error) {
    const text = String(error && error.message || "");
    if (/duplicate|409|unique/i.test(text)) {
      return jsonResponse(request, env, 409, { detail: "用户名或邮箱已被注册。" });
    }
    return jsonResponse(request, env, 503, { detail: "Account service is temporarily unavailable." });
  }
}

async function handleAccountPasswordChange(request, env) {
  let user;
  try {
    user = await currentUserFromRequest(env, request);
  } catch (error) {
    return jsonResponse(request, env, 401, { detail: error.message || "Please log in." });
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const currentPassword = String(payload.current_password || "");
  const newPassword = String(payload.new_password || "");
  if (newPassword.length < 4 || newPassword.length > 128) {
    return jsonResponse(request, env, 400, { detail: "新密码需为 4-128 位。" });
  }
  if (currentPassword === newPassword) {
    return jsonResponse(request, env, 400, { detail: "新密码不能和当前密码相同。" });
  }
  if (!await siteUserPasswordMatches(env, user, currentPassword)) {
    return jsonResponse(request, env, 401, { detail: "当前密码不正确。" });
  }
  if (!user.id) {
    return jsonResponse(request, env, 503, { detail: "Account service is temporarily unavailable." });
  }

  try {
    const passwordFields = await hashUserPassword(env, newPassword);
    const updated = await updateSiteUser(env, user.id, {
      ...passwordFields,
      last_login_at: new Date().toISOString(),
    });
    return authSuccessResponse(request, env, 200, { ...user, ...updated });
  } catch (_error) {
    return jsonResponse(request, env, 503, { detail: "密码更新失败，请稍后重试。" });
  }
}

async function handleEntitlement(request, env) {
  const url = new URL(request.url);
  try {
    const user = await currentUserFromRequest(env, request);
    const reportId = String(url.searchParams.get("report_id") || "").trim();
    const source = String(url.searchParams.get("source") || "catalog").trim() || "catalog";
    const access = await reportAccessForUser(env, user, reportId, source);
    return jsonResponse(request, env, 200, {
      user: publicUser(user),
      ...access,
    });
  } catch (error) {
    const status = accessErrorStatus(error);
    return jsonResponse(request, env, status, {
      detail: status === 503 ? "下载权限暂时无法核验，请稍后重试。" : error.message || "Please log in.",
    });
  }
}

function cleanEnv(value) {
  const text = String(value || "").trim();
  return text === "unconfigured" ? "" : text;
}

function cloudflareEmailRoutingConfig(env) {
  const accountId = cleanEnv(env.CLOUDFLARE_EMAIL_ROUTING_ACCOUNT_ID || env.CLOUDFLARE_ACCOUNT_ID);
  const token = cleanEnv(env.CLOUDFLARE_EMAIL_ROUTING_API_TOKEN || env.CLOUDFLARE_API_TOKEN);
  return {
    accountId,
    token,
    configured: Boolean(accountId && token),
  };
}

async function cloudflareEmailRoutingJson(env, path, init = {}) {
  const config = cloudflareEmailRoutingConfig(env);
  if (!config.configured) throw new Error("Cloudflare Email Routing API is not configured.");
  const headers = {
    "Accept": "application/json",
    "Authorization": `Bearer ${config.token}`,
    ...(init.body ? { "Content-Type": "application/json" } : {}),
    ...(init.headers || {}),
  };
  const response = await fetchWithTimeout(`${CLOUDFLARE_API_BASE}${path}`, {
    ...init,
    headers,
  }, CLOUDFLARE_EMAIL_TIMEOUT_MS);
  const data = await response.json().catch(() => ({}));
  if (!response.ok || data.success === false) {
    const detail = Array.isArray(data.errors) && data.errors[0] && data.errors[0].message
      ? data.errors[0].message
      : `Cloudflare API returned HTTP ${response.status}.`;
    throw new Error(detail);
  }
  return data.result;
}

async function requestCloudflareDestinationVerification(env, email) {
  const cleanEmail = normalizeEmail(email);
  if (!cleanEmail) return { status: "invalid", configured: false };
  const config = cloudflareEmailRoutingConfig(env);
  if (!config.configured) return { status: "not_configured", configured: false };
  const basePath = `/accounts/${encodeURIComponent(config.accountId)}/email/routing/addresses`;
  try {
    const existing = await cloudflareEmailRoutingJson(env, `${basePath}?per_page=200`, { method: "GET" });
    const match = (Array.isArray(existing) ? existing : [])
      .find((address) => normalizeEmail(address && address.email) === cleanEmail);
    if (match) {
      return {
        status: match.verified ? "verified" : "pending",
        configured: true,
        requested: false,
        id: String(match.id || ""),
      };
    }
  } catch (_error) {
    // A write-only token can still create the address and trigger Cloudflare's email.
  }
  try {
    const created = await cloudflareEmailRoutingJson(env, basePath, {
      method: "POST",
      body: JSON.stringify({ email: cleanEmail }),
    });
    return {
      status: created && created.verified ? "verified" : "pending",
      configured: true,
      requested: true,
      id: String(created && created.id || ""),
    };
  } catch (error) {
    const detail = String(error && error.message || "Cloudflare destination verification failed.").slice(0, 300);
    const status = /already exists|duplicate|exists/i.test(detail) ? "pending" : "failed";
    return {
      status,
      configured: true,
      requested: false,
      detail,
    };
  }
}

function paddleClientToken(env) {
  const token = cleanEnv(env.PADDLE_CLIENT_TOKEN);
  return /^(live|test)_[A-Za-z0-9_-]+$/.test(token) ? token : "";
}

function paddleEnv(env, clientToken) {
  const configured = cleanEnv(env.PADDLE_ENV);
  if (clientToken.startsWith("test_")) return "sandbox";
  if (clientToken.startsWith("live_")) return "production";
  return configured || "production";
}

function paddleConfig(env) {
  const cnyCentPrice = cleanEnv(env.PADDLE_PRICE_CNY_CENT);
  const clientToken = paddleClientToken(env);
  return {
    PADDLE_ENV: paddleEnv(env, clientToken),
    PADDLE_CLIENT_TOKEN: clientToken,
    PADDLE_PRICE_CNY_CENT: cnyCentPrice,
    PADDLE_PRICE_REPORT_CNY_CENT: cleanEnv(env.PADDLE_PRICE_REPORT_CNY_CENT) || cnyCentPrice,
    PADDLE_PRICE_YEARLY: cleanEnv(env.PADDLE_PRICE_YEARLY) || cnyCentPrice,
  };
}

function handlePaddleConfig(request, env) {
  return jsonResponse(request, env, 200, {
    config: {},
    missing: ["ACCESS_CHANNEL_DISABLED"],
    disabled: true,
    message: `Self-serve access is paused. Contact WeChat: ${CONTACT_WECHAT}.`,
  });
}

function parsePaddleSignature(header) {
  let timestamp = "";
  const signatures = [];
  for (const part of String(header || "").split(";")) {
    const [key, value] = part.split("=");
    if (!key || !value) continue;
    if (key.trim() === "ts") timestamp = value.trim();
    if (key.trim() === "h1") signatures.push(value.trim());
  }
  return { timestamp, signatures };
}

async function verifyPaddleSignature(env, rawBody, signatureHeader) {
  const secret = cleanEnv(env.PADDLE_WEBHOOK_SECRET);
  if (!secret || !signatureHeader) return false;
  const { timestamp, signatures } = parsePaddleSignature(signatureHeader);
  if (!timestamp || !signatures.length) return false;
  const sentAt = Number(timestamp);
  if (!Number.isFinite(sentAt) || Math.abs(Math.floor(Date.now() / 1000) - sentAt) > 300) return false;
  const expected = await hmacSha256Hex(secret, `${timestamp}:${rawBody}`);
  return signatures.some((signature) => constantTimeEqual(signature, expected));
}

function asObject(value) {
  return value && typeof value === "object" && !Array.isArray(value) ? value : {};
}

function firstText(...values) {
  for (const value of values) {
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  return "";
}

function collectPaddleLineItemPriceIds(data) {
  const details = asObject(data && data.details);
  const items = [
    ...(Array.isArray(data && data.items) ? data.items : []),
    ...(Array.isArray(details.line_items) ? details.line_items : []),
  ];
  const found = [];
  for (const rawItem of items) {
    const item = asObject(rawItem);
    const price = asObject(item.price);
    const priceId = firstText(price.id, item.price_id);
    if (priceId.startsWith("pri_") && !found.includes(priceId)) found.push(priceId);
  }
  return found;
}

function claimedPaddleEmail(data, customData) {
  const customer = asObject(data.customer);
  const billing = asObject(data.billing_details);
  return normalizeEmail(firstText(
    data.customer_email,
    data.email,
    customer.email,
    billing.email,
    customData.email,
    customData.customer_email,
  ));
}

function transactionIdForEvent(eventType, data) {
  return eventType.startsWith("transaction.")
    ? firstText(data.id, data.transaction_id)
    : firstText(data.transaction_id);
}

function subscriptionIdForEvent(eventType, data) {
  return eventType.startsWith("subscription.")
    ? firstText(data.id, data.subscription_id)
    : firstText(data.subscription_id);
}

function validPaddleCustomerId(value) {
  const customerId = String(value || "").trim();
  return /^ctm_[a-z0-9]{26}$/.test(customerId) ? customerId : "";
}

function validPaddleSubscriptionId(value) {
  const subscriptionId = String(value || "").trim();
  return /^sub_[a-z0-9]{26}$/.test(subscriptionId) ? subscriptionId : "";
}

function paddleCustomerBindingKey(customerId) {
  return accountKey("paddle_binding", "customer", customerId);
}

function validatePaddleCustomerBinding(row, customerId) {
  if (row === null || row === undefined) return null;
  if (!row || typeof row !== "object" || Array.isArray(row)) {
    throw new Error("Paddle customer binding verification failed.");
  }
  const email = normalizeEmail(row.email);
  const storedCustomerId = validPaddleCustomerId(row.paddle_customer_id);
  if (!email || !storedCustomerId || storedCustomerId !== customerId) {
    throw new Error("Paddle customer binding verification failed.");
  }
  return { ...row, email, paddle_customer_id: storedCustomerId };
}

async function findPaddleCustomerBinding(env, customerId) {
  const normalized = validPaddleCustomerId(customerId);
  if (!normalized) return null;
  if (hasSupabaseConfig(env)) {
    const query = queryString({
      paddle_customer_id: `eq.${normalized}`,
      select: "id,email,plan,status,lifetime,current_period_end,paddle_customer_id,paddle_subscription_id,paddle_transaction_id,paddle_last_event_id,paddle_last_occurred_at,created_at,updated_at",
      limit: "2",
    });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
    if (!Array.isArray(rows)) throw new Error("Account database response is invalid.");
    if (rows.length > 1) throw new Error("Paddle customer binding is not unique.");
    return validatePaddleCustomerBinding(rows[0] || null, normalized);
  }
  return validatePaddleCustomerBinding(
    await r2GetJsonStrict(env, paddleCustomerBindingKey(normalized)),
    normalized,
  );
}

function resolvePaddleStatus(eventType, data) {
  if (eventType === "subscription.canceled") return "canceled";
  if (eventType === "subscription.paused") return "paused";
  if (eventType === "subscription.past_due") return "past_due";
  if (eventType === "subscription.resumed") return "active";
  if (eventType.startsWith("subscription.")) {
    const status = String(data.status || "unknown").toLowerCase();
    return ACTIVE_STATUSES.has(status) ? "active" : status;
  }
  return "active";
}

function paddlePeriodEnd(data) {
  const period = asObject(data.current_billing_period);
  const value = firstText(period.ends_at, data.next_billed_at, data.billing_period_end);
  return value && Number.isFinite(Date.parse(value)) ? value : null;
}

function validPaddleEventIdentity(event) {
  const eventId = String(event && event.event_id || "").trim();
  const occurredAt = String(event && event.occurred_at || "").trim();
  if (!/^evt_[a-z0-9]{26}$/.test(eventId) || !Number.isFinite(Date.parse(occurredAt))) return null;
  return { eventId, occurredAt, occurredMs: Date.parse(occurredAt) };
}

function legacyPaddleEntitlementStateKey(email) {
  return accountKey("paddle_state", "entitlement", normalizeEmail(email));
}

async function assertNoLegacyPaddleWriteInFlight(env, email) {
  const row = await r2GetJsonStrict(env, legacyPaddleEntitlementStateKey(email));
  if (!row) return;
  const identity = validPaddleEventIdentity({
    event_id: row.event_id,
    occurred_at: row.occurred_at,
  });
  if (
    typeof row !== "object"
    || Array.isArray(row)
    || normalizeEmail(row.email) !== normalizeEmail(email)
    || !identity
    || !["pending", "applied"].includes(String(row.state || ""))
  ) {
    throw new Error("Legacy Paddle event state requires manual reconciliation.");
  }
  if (row.state === "pending") {
    throw new Error("Legacy Paddle entitlement update is still pending.");
  }
}

function paddleEventDisposition(row, identity, baselineUpdatedAt = "") {
  if (!identity) return "invalid";
  const lastEventId = String(row && row.paddle_last_event_id || "").trim();
  const lastOccurredAt = String(row && row.paddle_last_occurred_at || "").trim();
  if (lastEventId || lastOccurredAt) {
    const last = validPaddleEventIdentity({ event_id: lastEventId, occurred_at: lastOccurredAt });
    if (!last) throw new Error("Paddle entitlement event version is invalid.");
    if (last.eventId === identity.eventId) return "duplicate";
    if (identity.occurredMs <= last.occurredMs) return "stale";
    return "apply";
  }
  const baselineMs = Date.parse(String(baselineUpdatedAt || row && row.updated_at || ""));
  return Number.isFinite(baselineMs) && identity.occurredMs <= baselineMs ? "stale" : "apply";
}

function paddleEntitlementUpdateFields(binding, identity, fields) {
  return {
    ...fields,
    email: normalizeEmail(binding.email),
    paddle_customer_id: binding.paddle_customer_id,
    paddle_subscription_id: binding.paddle_subscription_id,
    paddle_last_event_id: identity.eventId,
    paddle_last_occurred_at: identity.occurredAt,
    updated_at: new Date().toISOString(),
  };
}

async function applyPaddleEntitlementEventInSupabase(env, binding, identity, fields) {
  let current = binding;
  for (let attempt = 0; attempt < 5; attempt += 1) {
    const action = paddleEventDisposition(current, identity, binding.updated_at);
    if (action !== "apply") return { action, entitlement: current };
    const id = String(current && current.id || "").trim();
    if (!id) throw new Error("Paddle customer binding is missing its entitlement id.");
    const query = {
      id: `eq.${id}`,
      paddle_customer_id: `eq.${binding.paddle_customer_id}`,
      paddle_subscription_id: `eq.${binding.paddle_subscription_id}`,
      select: "*",
    };
    const lastOccurredAt = String(current.paddle_last_occurred_at || "").trim();
    query.paddle_last_occurred_at = lastOccurredAt ? `eq.${lastOccurredAt}` : "is.null";
    const rows = await supabaseRequest(
      env,
      "PATCH",
      `/rest/v1/user_entitlements?${queryString(query)}`,
      paddleEntitlementUpdateFields(binding, identity, fields),
      { preferReturn: true },
    );
    if (Array.isArray(rows) && rows.length === 1) {
      const saved = validateEntitlementRow(rows[0], binding.email);
      validatePaddleCustomerBinding(saved, binding.paddle_customer_id);
      return { action: "applied", entitlement: saved };
    }
    current = await findPaddleCustomerBinding(env, binding.paddle_customer_id);
    if (!current) throw new Error("Paddle customer binding disappeared during update.");
  }
  throw new Error("Paddle entitlement changed concurrently. Please retry.");
}

async function applyPaddleEntitlementEventInR2(env, binding, identity, fields) {
  const email = normalizeEmail(binding.email);
  const key = accountKey("entitlements", email);
  for (let attempt = 0; attempt < 5; attempt += 1) {
    const snapshot = await r2GetJsonObjectStrict(env, key);
    const current = validateEntitlementRow(snapshot && snapshot.value, email);
    const action = paddleEventDisposition(current, identity, binding.updated_at);
    if (action !== "apply") return { action, entitlement: current };
    const now = new Date().toISOString();
    const payload = {
      ...(current || {}),
      ...paddleEntitlementUpdateFields(binding, identity, fields),
      id: current && current.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
      created_at: current && current.created_at || now,
    };
    validateEntitlementRow(payload, email);
    const etag = String(snapshot && snapshot.object && snapshot.object.etag || "");
    if (snapshot && !etag) throw new Error("Paddle entitlement version could not be verified.");
    const written = await accountBucket(env).put(key, JSON.stringify(payload), {
      onlyIf: snapshot ? { etagMatches: etag } : { etagDoesNotMatch: "*" },
      httpMetadata: { contentType: "application/json; charset=utf-8" },
    });
    if (written === null) continue;
    const saved = validateEntitlementRow(await r2GetJsonStrict(env, key), email);
    if (
      String(saved.paddle_last_event_id || "") !== identity.eventId
      || String(saved.paddle_last_occurred_at || "") !== identity.occurredAt
    ) {
      throw new Error("Paddle entitlement update could not be verified.");
    }
    return { action: "applied", entitlement: saved };
  }
  throw new Error("Paddle entitlement changed concurrently. Please retry.");
}

async function applyPaddleEntitlementEvent(env, binding, event, fields) {
  const identity = validPaddleEventIdentity(event);
  if (!identity) return { action: "invalid", entitlement: binding };
  return hasSupabaseConfig(env)
    ? applyPaddleEntitlementEventInSupabase(env, binding, identity, fields)
    : applyPaddleEntitlementEventInR2(env, binding, identity, fields);
}

async function processPaddleEvent(env, event) {
  const eventType = String(event.event_type || "");
  if (!PADDLE_HANDLED_EVENTS.has(eventType)) return { processed: false, event_type: eventType };

  const data = asObject(event.data);
  const customData = asObject(data.custom_data || data.customData);
  const priceIds = collectPaddleLineItemPriceIds(data);
  const config = paddleConfig(env);
  const reportPrice = config.PADDLE_PRICE_REPORT_CNY_CENT;
  const yearlyPrice = config.PADDLE_PRICE_YEARLY;
  const customerId = validPaddleCustomerId(data.customer_id);
  if (!customerId) return { processed: false, event_type: eventType, detail: "missing customer id" };
  const binding = await findPaddleCustomerBinding(env, customerId);
  if (!binding) return { processed: false, event_type: eventType, detail: "unbound customer" };
  const email = normalizeEmail(binding.email);
  const claimedEmail = claimedPaddleEmail(data, customData);
  if (claimedEmail && claimedEmail !== email) {
    return { processed: false, event_type: eventType, detail: "customer identity mismatch" };
  }
  await assertNoLegacyPaddleWriteInFlight(env, email);

  const isReportPurchase = eventType === "transaction.completed"
    && reportPrice
    && priceIds.includes(reportPrice)
    && reportPrice !== yearlyPrice;
  if (isReportPurchase) {
    // Self-service checkout is disabled. A client-provided report id or email
    // is not an authorization source; re-enable only with a server-signed,
    // single-use checkout intent.
    return { processed: false, event_type: eventType, detail: "checkout intent required" };
  }

  const subscriptionId = validPaddleSubscriptionId(subscriptionIdForEvent(eventType, data));
  const boundSubscriptionId = validPaddleSubscriptionId(binding.paddle_subscription_id);
  const subscriptionMatches = Boolean(
    eventType.startsWith("subscription.")
    && subscriptionId
    && boundSubscriptionId
    && subscriptionId === boundSubscriptionId,
  );
  const status = resolvePaddleStatus(eventType, data);
  const boundRevocation = subscriptionMatches && !ACTIVE_STATUSES.has(status);
  const isAnnualPurchase = boundRevocation || Boolean(
    yearlyPrice
    && priceIds.includes(yearlyPrice)
    && (eventType === "transaction.completed" || eventType.startsWith("subscription.")),
  );
  if (isAnnualPurchase) {
    if (!subscriptionId || !boundSubscriptionId || subscriptionId !== boundSubscriptionId) {
      return { processed: false, event_type: eventType, detail: "unbound subscription" };
    }
    const applied = await applyPaddleEntitlementEvent(env, {
      ...binding,
      paddle_customer_id: customerId,
      paddle_subscription_id: subscriptionId,
    }, event, {
      plan: "annual",
      status,
      lifetime: false,
      paddle_transaction_id: transactionIdForEvent(eventType, data),
      current_period_end: paddlePeriodEnd(data),
    });
    if (applied.action === "invalid") {
      return { processed: false, event_type: eventType, detail: "missing event identity" };
    }
    if (applied.action === "duplicate" || applied.action === "stale") {
      return {
        processed: false,
        event_type: eventType,
        detail: applied.action === "duplicate" ? "duplicate event" : "stale event",
      };
    }
    const saved = applied.entitlement;
    await insertUsageEvent(env, email, eventType, {
      event_id: event.event_id,
      plan: "annual",
      status,
      quantity: Number(customData.quantity || 0) || null,
      price_ids: priceIds,
    });
    return { processed: true, event_type: eventType, email, plan: saved.plan, status: saved.status };
  }

  await insertUsageEvent(env, email, eventType, {
    event_id: event.event_id,
    processed: false,
    reason: "unrecognized price",
    price_ids: priceIds,
  }).catch(() => {});
  return { processed: false, event_type: eventType, detail: "unrecognized price" };
}

async function handlePaddleWebhook(request, env) {
  const rawBody = await request.text();
  const signatureHeader = request.headers.get("Paddle-Signature") || "";
  if (!(await verifyPaddleSignature(env, rawBody, signatureHeader))) {
    return jsonResponse(request, env, 401, { detail: "Invalid Paddle signature." });
  }
  try {
    const event = JSON.parse(rawBody || "{}");
    const result = await processPaddleEvent(env, event);
    return jsonResponse(request, env, 200, { ok: true, ...result });
  } catch (error) {
    return jsonResponse(request, env, 500, { detail: error.message || "Webhook processing failed." });
  }
}

function vid2pptGrantSecret(env) {
  return String(env.VID2PPT_KCDESK_GRANT_SECRET || "").trim();
}

async function verifyVid2PptGrantSignature(env, request, rawBody) {
  const secret = vid2pptGrantSecret(env);
  const submitted = String(request.headers.get("X-Vid2PPT-Signature") || "")
    .trim()
    .replace(/^sha256=/i, "");
  if (!secret || !submitted) return false;
  const expected = await hmacSha256Hex(secret, rawBody);
  return constantTimeEqual(submitted, expected);
}

function cleanGrantText(value, limit = 160) {
  return String(value || "")
    .normalize("NFKC")
    .replace(/[\u0000-\u001f\u007f]+/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, limit);
}

function cleanGiftPlanCode(value) {
  return cleanGrantText(value, 32).toUpperCase();
}

function giftGrantPeriodEnd(planCode, startAt) {
  const spec = VID2PPT_KCDESK_GIFT_PLANS[planCode];
  if (!spec) return null;
  const parsed = Date.parse(String(startAt || ""));
  const date = new Date(Number.isFinite(parsed) ? parsed : Date.now());
  if (Number(spec.days || 0) > 0) {
    date.setUTCDate(date.getUTCDate() + Number(spec.days));
  } else if (Number(spec.months || 0) > 0) {
    date.setUTCMonth(date.getUTCMonth() + Number(spec.months));
  } else {
    return null;
  }
  return date.toISOString();
}

function normalizeVid2PptCode(value) {
  const code = cleanGrantText(value, 40).toUpperCase();
  return VID2PPT_CODE_PATTERN.test(code) ? code : "";
}

function vid2pptRedeemUrl(env) {
  return cleanEnv(env.VID2PPT_REDEEM_URL) || VID2PPT_REDEEM_URL;
}

function giftGrantStartIso(existingEntitlement, completedAt) {
  const completedMs = Date.parse(String(completedAt || ""));
  const baselineMs = Number.isFinite(completedMs) ? completedMs : Date.now();
  const existingMs = existingEntitlement && existingEntitlement.active && existingEntitlement.current_period_end
    ? Date.parse(String(existingEntitlement.current_period_end))
    : NaN;
  return new Date(Math.max(baselineMs, Number.isFinite(existingMs) ? existingMs : 0)).toISOString();
}

function giftGrantSource(planCode) {
  return String(planCode || "").startsWith("NOVA-") ? "vid2ppt_nova" : "vid2ppt_atlas";
}

function sameVid2PptGift(entitlement, planCode, sourceReference) {
  const grantSource = giftGrantSource(planCode);
  return entitlement
    && entitlement.grant_source === grantSource
    && entitlement.source_plan_code === planCode
    && entitlement.source_reference === sourceReference;
}

async function applyVid2PptGift(env, options = {}) {
  const email = normalizeEmail(options.email);
  const planCode = cleanGiftPlanCode(options.planCode || options.plan_code);
  if (!email) throw new Error("Valid email is required.");
  if (!VID2PPT_KCDESK_GIFT_PLANS[planCode]) throw new Error("Unsupported NOVA gift plan.");

  const requestId = cleanGrantText(options.requestId || options.request_id, 96);
  const transactionId = cleanGrantText(options.transactionId || options.paddle_transaction_id || options.transaction_id, 120);
  const eventId = cleanGrantText(options.eventId || options.event_id, 120);
  const code = normalizeVid2PptCode(options.code);
  const sourceReference = requestId || transactionId || eventId || code;
  if (!sourceReference) throw new Error("Grant reference is required.");
  const spec = VID2PPT_KCDESK_GIFT_PLANS[planCode];
  const grantSource = giftGrantSource(planCode);

  if (cleanAccessCount(spec.download_limit) > 0) {
    const snapshot = await findStoredVid2PptTrialAccessSnapshot(env, email);
    const existing = snapshot.record;
    const access = publicAccessGrant(existing && { ...existing, source: "vid2ppt_trial" });
    if (sameVid2PptGift(access, planCode, sourceReference)) {
      return { saved: existing || access, duplicate: true, sourceReference, accessKind: "trial" };
    }

    const startAt = giftGrantStartIso(access, options.completedAt || options.completed_at);
    const currentPeriodEnd = giftGrantPeriodEnd(planCode, startAt);
    if (!currentPeriodEnd) throw new Error("Unsupported NOVA gift plan.");
    const now = new Date().toISOString();
    const payload = {
      ...(existing || {}),
      id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
      email,
      access_mode: "all",
      status: "active",
      lifetime: false,
      current_period_end: currentPeriodEnd,
      duration_value: TRIAL_3D_DURATION_VALUE,
      download_limit: TRIAL_3D_DOWNLOAD_LIMIT,
      download_count: 0,
      download_items: [],
      institutions: [],
      industries: [],
      page_ranges: [],
      note: "Vid2PPT NOVA-3D gift",
      source_site: VID2PPT_SOURCE_SITE,
      grant_source: grantSource,
      source_plan_code: planCode,
      source_reference: sourceReference,
      paddle_transaction_id: transactionId,
      change_id: crypto.randomUUID ? crypto.randomUUID() : randomHex(16),
      created_at: existing && existing.created_at || now,
      updated_at: now,
      updated_by: "vid2ppt.com",
    };
    const writeResult = await writeVid2PptTrialAccessDurably(env, email, payload, snapshot.etag);
    await insertUsageEvent(env, email, options.eventType || `${grantSource}.granted`, {
      site_origin: SITE_ORIGIN,
      source_site: VID2PPT_SOURCE_SITE,
      grant_source: grantSource,
      plan_code: planCode,
      request_id: requestId,
      event_id: eventId,
      code,
      paddle_transaction_id: transactionId,
      amount_cny: cleanGrantText(options.amountCny || options.amount_cny, 40),
      legal_purchase_site: "vid2ppt.com",
      granted_benefit_site: "kcdesk.com",
      source_reference: sourceReference,
      duration_days: Number(spec.days),
      download_limit: TRIAL_3D_DOWNLOAD_LIMIT,
    }).catch(() => {});
    return { saved: writeResult.record, duplicate: false, sourceReference, accessKind: "trial" };
  }

  const existing = await findEntitlement(env, email).catch(() => null);
  const entitlement = publicEntitlement(existing);

  if (sameVid2PptGift(entitlement, planCode, sourceReference)) {
    return { saved: existing || entitlement, duplicate: true, sourceReference, accessKind: "entitlement" };
  }
  if (entitlement.active && entitlement.lifetime) {
    return { saved: existing || entitlement, duplicate: false, lifetime: true, sourceReference, accessKind: "entitlement" };
  }

  const startAt = giftGrantStartIso(entitlement, options.completedAt || options.completed_at);
  const currentPeriodEnd = giftGrantPeriodEnd(planCode, startAt);
  if (!currentPeriodEnd) throw new Error("Unsupported NOVA gift plan.");
  const saved = await saveEntitlement(env, email, {
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: currentPeriodEnd,
    paddle_transaction_id: transactionId,
    site_origin: SITE_ORIGIN,
    source_site: VID2PPT_SOURCE_SITE,
    grant_source: grantSource,
    source_plan_code: planCode,
    source_reference: sourceReference,
  });
  await insertUsageEvent(env, email, options.eventType || `${grantSource}.granted`, {
    site_origin: SITE_ORIGIN,
    source_site: VID2PPT_SOURCE_SITE,
    grant_source: grantSource,
    plan_code: planCode,
    request_id: requestId,
    event_id: eventId,
    code,
    paddle_transaction_id: transactionId,
    amount_cny: cleanGrantText(options.amountCny || options.amount_cny, 40),
    legal_purchase_site: "vid2ppt.com",
    granted_benefit_site: "kcdesk.com",
    source_reference: sourceReference,
  }).catch(() => {});
  return { saved, duplicate: false, sourceReference, accessKind: "entitlement" };
}

async function handleVid2PptGiftGrant(request, env) {
  const rawBody = await request.text();
  if (!(await verifyVid2PptGrantSignature(env, request, rawBody))) {
    return jsonResponse(request, env, 401, { detail: "Invalid grant signature." });
  }

  let payload = {};
  try {
    payload = JSON.parse(rawBody || "{}");
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const email = normalizeEmail(payload.email);
  const planCode = cleanGiftPlanCode(payload.plan_code);
  if (!email) return jsonResponse(request, env, 400, { detail: "Valid email is required." });
  if (!VID2PPT_KCDESK_GIFT_PLANS[planCode]) {
    return jsonResponse(request, env, 200, { ok: true, granted: false, detail: "Not a NOVA gift plan." });
  }

  const requestId = cleanGrantText(payload.request_id, 96);
  const transactionId = cleanGrantText(payload.paddle_transaction_id || payload.transaction_id, 120);
  const eventId = cleanGrantText(payload.event_id, 120);

  try {
    const { saved, duplicate, accessKind } = await applyVid2PptGift(env, {
      email,
      planCode,
      requestId,
      transactionId,
      eventId,
      completedAt: payload.completed_at,
      amountCny: payload.amount_cny,
      eventType: `${giftGrantSource(planCode)}.granted`,
    });
    const grant = accessKind === "trial" ? publicAccessGrant(saved) : publicEntitlement(saved);
    return jsonResponse(request, env, 200, {
      ok: true,
      granted: true,
      duplicate,
      email,
      access_kind: accessKind,
      plan: accessKind === "trial" ? TRIAL_3D_DURATION_VALUE : saved.plan,
      status: grant.status,
      current_period_end: grant.current_period_end,
      download_limit: grant.download_limit || 0,
      downloads_remaining: grant.downloads_remaining,
      source_plan_code: planCode,
    });
  } catch (error) {
    return jsonResponse(request, env, 500, { detail: error.message || "Grant failed." });
  }
}

async function callVid2PptRedeemCode(env, { code, email, username, mode }) {
  const response = await fetchWithTimeout(vid2pptRedeemUrl(env), {
    method: "POST",
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      action: "redeem_code",
      mode: mode || "check",
      code,
      email,
      source: "kcdesk_redeem_fallback",
      metadata: {
        site_origin: SITE_ORIGIN,
        source_site: VID2PPT_SOURCE_SITE,
        username,
        legal_purchase_site: "vid2ppt.com",
        gift_benefit_site: "kcdesk.com",
      },
    }),
  }, 12000);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || `Vid2PPT returned HTTP ${response.status}.`);
  }
  return data;
}

async function handleVid2PptRedeemCode(request, env) {
  let user;
  try {
    user = await currentUserFromRequest(env, request);
  } catch (error) {
    return jsonResponse(request, env, 401, { detail: error.message || "Please log in." });
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const code = normalizeVid2PptCode(payload.code);
  if (!code) return jsonResponse(request, env, 400, { detail: "请输入有效的 Vid2PPT 兑换代码。" });

  const email = normalizeEmail(user.email);
  const username = normalizeUsername(user.username);
  try {
    const checked = await callVid2PptRedeemCode(env, { code, email, username, mode: "check" });
    const order = checked && checked.order || {};
    const orderEmail = normalizeEmail(order.email);
    const planCode = cleanGiftPlanCode(order.plan_code);
    if (!checked.valid) return jsonResponse(request, env, 404, { detail: checked.detail || "代码未找到或未支付完成。" });
    if (checked.redeemed) return jsonResponse(request, env, 409, { detail: "这串代码已经兑换过。", order });
    if (!VID2PPT_KCDESK_GIFT_PLANS[planCode] || (order.benefit_site && order.benefit_site !== "kcdesk")) {
      return jsonResponse(request, env, 400, { detail: "这串代码不是 NOVA 赠送权益代码。", order });
    }
    if (orderEmail && orderEmail !== email) {
      return jsonResponse(request, env, 403, { detail: "这串代码对应的支付邮箱与当前 KCdesk 账号邮箱不一致。", order });
    }

    const { saved, duplicate, accessKind } = await applyVid2PptGift(env, {
      email,
      planCode,
      requestId: order.request_id,
      code,
      completedAt: order.completed_at || new Date().toISOString(),
      amountCny: order.amount_cny,
      eventType: `${giftGrantSource(planCode)}.code_redeemed`,
    });
    const redeemed = await callVid2PptRedeemCode(env, { code, email, username, mode: "redeem" });
    return jsonResponse(request, env, 200, {
      ok: true,
      redeemed: Boolean(redeemed.redeemed || redeemed.valid),
      granted: true,
      duplicate,
      user: publicUser(user),
      entitlement: accessKind === "trial" ? publicAccessGrant(saved) : publicEntitlement(saved),
      order: redeemed.order || order,
    });
  } catch (error) {
    return jsonResponse(request, env, 502, { detail: error.message || "兑换代码校验失败，请稍后重试。" });
  }
}

function safeFilename(value) {
  const filename = String(value || "report.pdf")
    .replace(/[\r\n"\\/:*?<>|]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
  return filename || "report.pdf";
}

function asciiFilename(value) {
  return safeFilename(value).replace(/[^\x20-\x7e]+/g, "_");
}

function contentDisposition(filename) {
  const safe = safeFilename(filename);
  return `attachment; filename="${asciiFilename(safe)}"; filename*=UTF-8''${encodeURIComponent(safe)}`;
}

function objectKeyForReport(env, id) {
  const prefix = String(env.R2_OBJECT_PREFIX || DEFAULT_R2_PREFIX).replace(/^\/+|\/+$/g, "");
  return prefix ? `${prefix}/${id}.pdf` : `${id}.pdf`;
}

async function handleDownload(request, env) {
  let payload;
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
  }

  const id = String(payload.id || "").trim();
  const password = String(payload.password || "");
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const accountDecision = await accountDownloadDecision(env, request, id, "catalog");
  const accountAllowed = Boolean(accountDecision.allowed);
  if (!password && !accountAllowed) {
    return jsonResponse(request, env, accountDecision.status || 402, {
      error: accountDecision.error || "Please log in, purchase this report, or enter the report password.",
      contact: accountDecision.contact || undefined,
      limit_exceeded: Boolean(accountDecision.limit_exceeded),
    });
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Download service is temporarily unavailable." });
  }

  const report = findReport(catalog, id);
  if (!report) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }
  if (report.available === false) {
    return jsonResponse(request, env, 404, {
      error: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.`,
      archived: true,
      contact: CONTACT_WECHAT,
    });
  }

  if (!accountAllowed) {
    let derivedOk = false;
    try {
      derivedOk = await derivedPasswordMatches(env, id, password);
    } catch (_error) {
      derivedOk = false;
    }

    if (!derivedOk) {
      try {
        const rules = await loadRules(env);
        const group = findPasswordGroup(rules, report.password_group || rules.default_group);
        if (!group) {
          return jsonResponse(request, env, 503, { error: "Password validation failed." });
        }
        const ok = await passwordMatches(env, group, password);
        if (!ok) return jsonResponse(request, env, 401, { error: "Password is incorrect." });
      } catch (_error) {
        return jsonResponse(request, env, 503, { error: "Password validation failed." });
      }
    }
  }

  if (!env.REPORT_BUCKET) {
    return jsonResponse(request, env, 503, { error: "Download service is temporarily unavailable." });
  }

  const key = objectKeyForReport(env, id);
  const object = await env.REPORT_BUCKET.get(key);
  if (!object) {
    return jsonResponse(request, env, 404, {
      error: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.`,
      archived: true,
      contact: CONTACT_WECHAT,
    });
  }

  const consumed = await finalizeAccountDownloadDecision(env, request, accountDecision, id, "catalog");
  if (!consumed.ok) {
    return jsonResponse(request, env, consumed.status || 403, {
      error: consumed.error || TRIAL_LIMIT_MESSAGE,
      contact: consumed.contact || CONTACT_WECHAT,
      limit_exceeded: Boolean(consumed.limit_exceeded),
    });
  }

  return new Response(object.body, {
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/pdf",
      "Content-Disposition": contentDisposition(report.filename || `${id}.pdf`),
      "Cache-Control": "no-store, private",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

async function handleCalculator(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  const key = String(url.searchParams.get("key") || "");
  if (!env.CALC_KEY) {
    return jsonResponse(request, env, 503, { error: "Calculator key is not configured." });
  }
  if (key !== env.CALC_KEY) {
    return jsonResponse(request, env, 401, { error: "Calculator key is incorrect." });
  }
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  try {
    return jsonResponse(request, env, 200, {
      id,
      password: await derivedReportPassword(env, id),
      rule: "KC-" + "base32(hmac_sha256(PASSWORD_SECRET, 'kc-desk-notes:' + report_id))[0:12] grouped 4-4-4",
    });
  } catch (error) {
    return jsonResponse(request, env, 503, { error: error.message || "Could not calculate password." });
  }
}

async function handleAdminLogin(request, env) {
  let payload;
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
  }

  const submitted = String(payload.key || "").trim();
  const expected = String(env.MASTER_KEY || "").trim();
  if (!expected) {
    return jsonResponse(request, env, 503, { error: "Private tools are not configured." });
  }
  if (!submitted || !constantTimeEqual(submitted, expected)) {
    return jsonResponse(request, env, 401, { error: "Private key is incorrect." });
  }

  try {
    const now = Math.floor(Date.now() / 1000);
    const expires = now + ADMIN_TOKEN_TTL_SECONDS;
    const token = await signAdminToken(env, { v: 1, iat: now, exp: expires });
    return jsonResponse(request, env, 200, {
      ok: true,
      token,
      expires_in: ADMIN_TOKEN_TTL_SECONDS,
      expires_at: new Date(expires * 1000).toISOString(),
    });
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Private tools are not configured." });
  }
}

async function requireAdminOrSuperUser(request, env, token) {
  let tokenError = null;
  if (token) {
    try {
      await verifyAdminToken(env, token);
      return { kind: "master" };
    } catch (error) {
      tokenError = error;
    }
  }
  try {
    const user = await currentUserFromRequest(env, request);
    if (isPrivilegedAccount(user)) return { kind: accountRole(user), user };
  } catch (_error) {
    // Use the token error below when an admin token was supplied.
  }
  if (tokenError) throw tokenError;
  throw new Error("Admin session is invalid.");
}

async function handleAdminReportPassword(request, env) {
  let payload;
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
  }

  const id = String(payload.id || "").trim();
  const token = String(payload.token || "");
  const source = String(payload.source || "catalog").trim().toLowerCase();
  if (source === "external") {
    if (!isExternalId(id)) {
      return jsonResponse(request, env, 400, { error: "Invalid report id." });
    }
  } else if (source === THINKTANK_SOURCE) {
    if (!parseThinkTankId(id)) {
      return jsonResponse(request, env, 400, { error: "Invalid report id." });
    }
  } else if (source === AUTHORITY_SOURCE) {
    if (!parseAuthorityId(id)) {
      return jsonResponse(request, env, 400, { error: "Invalid report id." });
    }
  } else if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }

  try {
    await requireAdminOrSuperUser(request, env, token);
  } catch (error) {
    return jsonResponse(request, env, 401, { error: error.message || "Admin session is invalid." });
  }

  if (source === AUTHORITY_SOURCE) {
    return jsonResponse(request, env, 403, {
      error: `高权报告仅提供检索线索，无法生成下载发货链接。请联系 WeChat: ${CONTACT_WECHAT}。`,
      contact: CONTACT_WECHAT,
    });
  }

  if (source === "external") {
    try {
      return jsonResponse(request, env, 200, {
        id,
        source,
        password: await derivedReportPassword(env, id),
      });
    } catch (_error) {
      return jsonResponse(request, env, 503, { error: "Could not calculate report password." });
    }
  }

  if (source === THINKTANK_SOURCE) {
    const row = await findThinkTankRow(env, id);
    if (!row) return jsonResponse(request, env, 404, { error: "Report not found." });
    const canonicalId = thinkTankId(row);
    try {
      return jsonResponse(request, env, 200, {
        id: canonicalId,
        source,
        title: row.title || "",
        password: await derivedReportPassword(env, canonicalId),
      });
    } catch (_error) {
      return jsonResponse(request, env, 503, { error: "Could not calculate report password." });
    }
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Catalog is not configured." });
  }

  const report = findReport(catalog, id);
  if (!report) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }

  try {
    return jsonResponse(request, env, 200, {
      id,
      title: report.title || "",
      title_zh: report.title_zh || "",
      available: report.available !== false,
      password: await derivedReportPassword(env, id),
    });
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Could not calculate report password." });
  }
}

async function requireSuperUser(request, env) {
  const user = await currentUserFromRequest(env, request);
  if (!isSuperAccount(user)) throw new Error("Only the admin account can access this area.");
  return user;
}

async function requireOperationsUser(request, env) {
  const user = await currentUserFromRequest(env, request);
  if (!isPrivilegedAccount(user)) throw new Error("Only an admin account can access this area.");
  return user;
}

function adminVisibleUser(user, entitlementRow, accessRow) {
  const publicInfo = publicUser(user);
  const entitlement = isPrivilegedAccount(user) ? superEntitlement(user) : publicEntitlement(entitlementRow);
  const access = publicAccessGrant(accessRow);
  return {
    ...publicInfo,
    last_login_at: user.last_login_at || "",
    entitlement,
    access,
    effective_access: effectiveAccessForUser(user, entitlementRow, accessRow),
  };
}

function cleanAnalyticsText(value, limit = 240) {
  return String(value || "")
    .normalize("NFKC")
    .replace(/[\u0000-\u001f\u007f]+/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, limit);
}

function cleanAnalyticsNumber(value) {
  const number = Number(value);
  return Number.isFinite(number) ? number : 0;
}

function analyticsBjtDateKey(ms = Date.now()) {
  return new Date(ms + 8 * 60 * 60 * 1000).toISOString().slice(0, 10);
}

function analyticsRecentDateKeys(days = ANALYTICS_DASHBOARD_DAYS) {
  const now = Date.now();
  const keys = [];
  for (let index = 0; index < days; index += 1) {
    keys.push(analyticsBjtDateKey(now - index * 24 * 60 * 60 * 1000));
  }
  return keys;
}

function analyticsClientIp(request) {
  return String(
    request.headers.get("CF-Connecting-IP") ||
    request.headers.get("X-Forwarded-For") ||
    "",
  ).split(",")[0].trim();
}

async function analyticsIpHash(request, env) {
  const ip = analyticsClientIp(request);
  if (!ip) return "";
  let secret = "kcdesk";
  try {
    secret = accountSecret(env);
  } catch (_error) {
    // Hashing without the account secret is still enough to avoid storing the raw IP.
  }
  return (await sha256Hex(`${secret}:analytics-ip:${ip}`)).slice(0, 24);
}

async function optionalAnalyticsUser(request, env) {
  try {
    const user = await currentUserFromRequest(env, request);
    return {
      id: cleanAnalyticsText(user.id, 80),
      username: cleanAnalyticsText(user.username, 80),
      email: cleanAnalyticsText(user.email, 160),
      role: accountRole(user),
    };
  } catch (_error) {
    return null;
  }
}

function analyticsEventFromPayload(request, payload, user, ipHash) {
  const now = new Date();
  const cf = request.cf || {};
  const data = payload && typeof payload.data === "object" && payload.data ? payload.data : {};
  const pathFromPayload = cleanAnalyticsText(payload.path || data.path, 240);
  const path = pathFromPayload || cleanAnalyticsText(new URL(request.url).pathname, 240);
  const type = cleanAnalyticsText(payload.type || data.type || "event", 60).toLowerCase() || "event";
  return {
    id: crypto.randomUUID ? crypto.randomUUID() : randomHex(16),
    ts: now.toISOString(),
    date: analyticsBjtDateKey(now.getTime()),
    type,
    visitor_id: cleanAnalyticsText(payload.visitor_id || data.visitor_id, 96),
    path,
    page: cleanAnalyticsText(data.page || payload.page, 80),
    source: cleanAnalyticsText(data.source || payload.source, 80),
    query: cleanAnalyticsText(data.query || payload.query, 240),
    bank: cleanAnalyticsText(data.bank || payload.bank, 160),
    industry: cleanAnalyticsText(data.industry || payload.industry, 160),
    start_date: cleanAnalyticsText(data.start_date || payload.start_date, 32),
    end_date: cleanAnalyticsText(data.end_date || payload.end_date, 32),
    scope: cleanAnalyticsText(data.scope || payload.scope, 40),
    availability: cleanAnalyticsText(data.availability || payload.availability, 40),
    page_ranges: cleanAnalyticsText(data.page_ranges || payload.page_ranges, 120),
    page_range_labels: cleanAnalyticsText(data.page_range_labels || payload.page_range_labels, 160),
    result_count: cleanAnalyticsNumber(data.result_count),
    total_count: cleanAnalyticsNumber(data.total_count),
    cache_status: cleanAnalyticsText(data.cache_status, 60),
    report_id: cleanAnalyticsText(data.report_id || data.id, 120),
    report_title: cleanAnalyticsText(data.report_title || data.title, 360),
    institution: cleanAnalyticsText(data.institution, 160),
    target: cleanAnalyticsText(data.target, 240),
    action: cleanAnalyticsText(data.action, 80),
    status: cleanAnalyticsText(data.status, 80),
    duration_ms: cleanAnalyticsNumber(data.duration_ms),
    error: cleanAnalyticsText(data.error, 180),
    referrer: cleanAnalyticsText(data.referrer || request.headers.get("Referer"), 320),
    user,
    ip_hash: ipHash,
    country: cleanAnalyticsText(cf.country || request.headers.get("CF-IPCountry"), 16),
    colo: cleanAnalyticsText(cf.colo, 16),
    user_agent: cleanAnalyticsText(request.headers.get("User-Agent"), 240),
  };
}

function analyticsUserSnapshot(user) {
  if (!user) return null;
  return {
    id: cleanAnalyticsText(user.id, 80),
    username: cleanAnalyticsText(user.username, 80),
    email: cleanAnalyticsText(user.email, 160),
    role: accountRole(user),
  };
}

async function persistAnalyticsEvent(request, env, payload, userOverride = undefined) {
  if (!env.REPORT_BUCKET || !payload || typeof payload !== "object") return null;
  const [user, ipHash] = await Promise.all([
    userOverride === undefined
      ? optionalAnalyticsUser(request, env)
      : Promise.resolve(analyticsUserSnapshot(userOverride)),
    analyticsIpHash(request, env),
  ]);
  const event = analyticsEventFromPayload(request, payload, user, ipHash);
  const suffix = `${event.date}/${event.ts.replace(/[:.]/g, "-")}-${event.id}.json`;
  const body = JSON.stringify(event);
  const metadata = {
    httpMetadata: {
      contentType: "application/json; charset=utf-8",
      cacheControl: "no-store",
    },
  };
  await Promise.all([
    env.REPORT_BUCKET.put(`${ANALYTICS_PREFIX}/${suffix}`, body, metadata),
    env.REPORT_BUCKET.put(`${ANALYTICS_BACKUP_PREFIX}/${suffix}`, body, metadata),
  ]);
  return event;
}

async function handleAnalyticsEvent(request, env, ctx = null) {
  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }
  const write = persistAnalyticsEvent(request, env, payload).catch(() => null);
  if (ctx && typeof ctx.waitUntil === "function") {
    ctx.waitUntil(write);
  } else {
    await write;
  }
  return new Response(null, { status: 204, headers: corsHeaders(request, env) });
}

async function listAnalyticsEvents(env, days = ANALYTICS_DASHBOARD_DAYS, limit = ANALYTICS_DASHBOARD_LIMIT) {
  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") return [];
  const rowsById = new Map();
  let readBudget = Math.min(Math.max(1, Number(limit) || ANALYTICS_DASHBOARD_LIMIT), ANALYTICS_DASHBOARD_R2_READ_BUDGET);
  for (const prefixRoot of [ANALYTICS_PREFIX, ANALYTICS_BACKUP_PREFIX]) {
    if (prefixRoot === ANALYTICS_BACKUP_PREFIX && rowsById.size > 0) break;
    for (const date of analyticsRecentDateKeys(days)) {
      let cursor = undefined;
      do {
        if (readBudget <= 0 || rowsById.size >= limit) break;
        const listLimit = Math.min(200, Math.max(1, limit - rowsById.size), Math.max(1, readBudget));
        const listed = await env.REPORT_BUCKET.list({
          prefix: `${prefixRoot}/${date}/`,
          limit: listLimit,
          cursor,
        });
        const objects = (Array.isArray(listed && listed.objects) ? listed.objects : [])
          .slice(0, Math.min(readBudget, Math.max(0, limit - rowsById.size)));
        readBudget -= objects.length;
        const batch = await Promise.all(objects.map(async (object) => {
          try {
            const stored = await env.REPORT_BUCKET.get(object.key);
            return stored ? JSON.parse(await stored.text()) : null;
          } catch (_error) {
            return null;
          }
        }));
        for (const event of batch) {
          if (event && typeof event === "object") {
            const id = String(event.id || `${event.ts || ""}:${event.type || ""}:${event.visitor_id || event.ip_hash || ""}`);
            if (id && !rowsById.has(id)) rowsById.set(id, event);
          }
          if (rowsById.size >= limit) break;
        }
        if (rowsById.size >= limit || !listed || !listed.truncated || !listed.cursor) break;
        cursor = listed.cursor;
      } while (rowsById.size < limit);
      if (rowsById.size >= limit) break;
    }
    if (rowsById.size >= limit) break;
  }
  return [...rowsById.values()].sort((a, b) => String(b.ts || "").localeCompare(String(a.ts || "")));
}

function analyticsDateFromPrefix(prefixRoot, value) {
  const prefix = `${prefixRoot}/`;
  const date = String(value || "").startsWith(prefix)
    ? String(value).slice(prefix.length).replace(/\/$/, "")
    : "";
  return /^\d{4}-\d{2}-\d{2}$/.test(date) ? date : "";
}

async function listAnalyticsEventDatesForRoot(env, prefixRoot) {
  const dates = new Set();
  let cursor = undefined;
  do {
    const listed = await env.REPORT_BUCKET.list({
      prefix: `${prefixRoot}/`,
      delimiter: "/",
      limit: 1000,
      cursor,
    });
    for (const value of Array.isArray(listed && listed.delimitedPrefixes) ? listed.delimitedPrefixes : []) {
      const date = analyticsDateFromPrefix(prefixRoot, value);
      if (date) dates.add(date);
    }
    if (!listed || !listed.truncated || !listed.cursor) break;
    cursor = listed.cursor;
  } while (cursor);
  return [...dates];
}

async function listAnalyticsEventDateRows(env) {
  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") return [];
  const [primaryDates, backupDates] = await Promise.all([
    listAnalyticsEventDatesForRoot(env, ANALYTICS_PREFIX),
    listAnalyticsEventDatesForRoot(env, ANALYTICS_BACKUP_PREFIX),
  ]);
  const primary = new Set(primaryDates);
  const backup = new Set(backupDates);
  return [...new Set([...primaryDates, ...backupDates])]
    .sort((a, b) => b.localeCompare(a))
    .map((date) => ({
      date,
      prefix_roots: [
        primary.has(date) ? ANALYTICS_PREFIX : "",
        backup.has(date) ? ANALYTICS_BACKUP_PREFIX : "",
      ].filter(Boolean),
    }));
}

async function listAnalyticsEventKeysForRoot(env, prefixRoot, date) {
  const rows = [];
  let cursor = undefined;
  do {
    const listed = await env.REPORT_BUCKET.list({
      prefix: `${prefixRoot}/${date}/`,
      limit: 1000,
      cursor,
    });
    for (const object of Array.isArray(listed && listed.objects) ? listed.objects : []) {
      if (!object || !object.key) continue;
      const key = String(object.key);
      rows.push({
        key,
        suffix: key.slice(`${prefixRoot}/${date}/`.length),
      });
    }
    if (!listed || !listed.truncated || !listed.cursor) break;
    cursor = listed.cursor;
  } while (cursor);
  return rows;
}

async function listAnalyticsEventKeysForDate(env, prefixRoots, date) {
  const batches = await Promise.all((Array.isArray(prefixRoots) ? prefixRoots : [])
    .map((prefixRoot) => listAnalyticsEventKeysForRoot(env, prefixRoot, date)));
  const rowsBySuffix = new Map();
  for (const rows of batches) {
    for (const row of rows) {
      if (!row.suffix) continue;
      const existing = rowsBySuffix.get(row.suffix);
      if (existing) {
        existing.keys.push(row.key);
      } else {
        rowsBySuffix.set(row.suffix, { suffix: row.suffix, keys: [row.key] });
      }
    }
  }
  return [...rowsBySuffix.values()].sort((a, b) => b.suffix.localeCompare(a.suffix));
}

async function readAnalyticsEventsByRows(env, rows) {
  return Promise.all((Array.isArray(rows) ? rows : []).map(async (row) => {
    for (const key of Array.isArray(row && row.keys) ? row.keys : []) {
      try {
        const stored = await env.REPORT_BUCKET.get(key);
        if (stored) return JSON.parse(await stored.text());
      } catch (_error) {
        // Try the mirrored analytics object next.
      }
    }
    return null;
  }));
}

function publicAnalyticsEvent(event) {
  return {
    id: event.id || "",
    ts: event.ts || "",
    date: event.date || "",
    type: event.type || "",
    visitor_id: event.visitor_id || "",
    ip_hash: event.ip_hash || "",
    user: event.user ? {
      username: event.user.username || "",
      email: event.user.email || "",
      role: event.user.role || "",
    } : null,
    country: event.country || "",
    colo: event.colo || "",
    page: event.page || "",
    path: event.path || "",
    source: event.source || "",
    query: event.query || "",
    bank: event.bank || "",
    industry: event.industry || "",
    start_date: event.start_date || "",
    end_date: event.end_date || "",
    scope: event.scope || "",
    availability: event.availability || "",
    page_ranges: event.page_ranges || "",
    page_range_labels: event.page_range_labels || "",
    result_count: event.result_count || 0,
    total_count: event.total_count || 0,
    cache_status: event.cache_status || "",
    report_id: event.report_id || "",
    report_title: event.report_title || "",
    institution: event.institution || "",
    target: event.target || "",
    action: event.action || "",
    status: event.status || "",
    duration_ms: event.duration_ms || 0,
    error: event.error || "",
    referrer: event.referrer || "",
    user_agent: event.user_agent || "",
  };
}

function cleanAnalyticsHistoryDate(value) {
  const date = cleanAnalyticsText(value, 10);
  return /^\d{4}-\d{2}-\d{2}$/.test(date) ? date : "";
}

function analyticsHistoryFilterSignature(filters) {
  return [filters.type, filters.query, filters.startDate, filters.endDate].join("\u001f");
}

function encodeAnalyticsHistoryCursor(value) {
  return base64UrlEncodeText(JSON.stringify(value || {}));
}

function decodeAnalyticsHistoryCursor(value) {
  try {
    const parsed = JSON.parse(base64UrlDecodeText(value));
    return parsed && typeof parsed === "object" ? parsed : null;
  } catch (_error) {
    return null;
  }
}

function analyticsHistoryEventMatches(event, filters) {
  if (!event || typeof event !== "object") return false;
  if (filters.type && String(event.type || "").toLowerCase() !== filters.type) return false;
  if (!filters.query) return true;
  const user = event.user && typeof event.user === "object" ? event.user : {};
  const haystack = normalizeText([
    event.type,
    event.visitor_id,
    event.ip_hash,
    user.username,
    user.email,
    event.country,
    event.colo,
    event.page,
    event.path,
    event.source,
    event.query,
    event.bank,
    event.industry,
    event.report_id,
    event.report_title,
    event.institution,
    event.target,
    event.action,
    event.status,
    event.error,
    event.referrer,
    event.user_agent,
  ].filter(Boolean).join(" "));
  return normalizeText(filters.query).split(" ").filter(Boolean).every((token) => haystack.includes(token));
}

async function handleAccountAdminAnalyticsEvents(request, env) {
  try {
    await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }

  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") {
    return jsonResponse(request, env, 503, { detail: "Analytics storage is unavailable." });
  }

  const url = new URL(request.url);
  const pageSize = Math.min(
    ANALYTICS_HISTORY_MAX_PAGE_SIZE,
    Math.max(1, Number(url.searchParams.get("page_size")) || ANALYTICS_HISTORY_DEFAULT_PAGE_SIZE),
  );
  const filters = {
    type: cleanAnalyticsText(url.searchParams.get("type"), 60).toLowerCase(),
    query: cleanAnalyticsText(url.searchParams.get("q"), 240),
    startDate: cleanAnalyticsHistoryDate(url.searchParams.get("start_date")),
    endDate: cleanAnalyticsHistoryDate(url.searchParams.get("end_date")),
  };
  const scanLimit = filters.type || filters.query
    ? ANALYTICS_HISTORY_FILTER_SCAN_LIMIT
    : pageSize;
  if (filters.startDate && filters.endDate && filters.startDate > filters.endDate) {
    return jsonResponse(request, env, 400, { detail: "Start date must not be after end date." });
  }

  const signature = analyticsHistoryFilterSignature(filters);
  const requestedCursor = decodeAnalyticsHistoryCursor(url.searchParams.get("cursor"));
  const cursor = requestedCursor && requestedCursor.signature === signature ? requestedCursor : null;

  try {
    const allDateRows = await listAnalyticsEventDateRows(env);
    const dateRows = allDateRows.filter((row) => {
      if (filters.startDate && row.date < filters.startDate) return false;
      if (filters.endDate && row.date > filters.endDate) return false;
      return true;
    });
    let dateIndex = 0;
    let afterKey = "";
    if (cursor && cursor.date) {
      const index = dateRows.findIndex((row) => row.date === cursor.date);
      if (index >= 0) {
        dateIndex = index;
        afterKey = cleanAnalyticsText(cursor.after_key, 500);
      }
    }

    const events = [];
    let scannedCount = 0;
    let nextCursor = "";
    let hasMore = false;
    let stop = false;

    for (; dateIndex < dateRows.length && !stop; dateIndex += 1) {
      const dateRow = dateRows[dateIndex];
      const keys = await listAnalyticsEventKeysForDate(env, dateRow.prefix_roots, dateRow.date);
      let keyIndex = 0;
      if (afterKey) {
        const exactIndex = keys.findIndex((row) => row.suffix === afterKey);
        if (exactIndex >= 0) {
          keyIndex = exactIndex + 1;
        } else {
          const nextIndex = keys.findIndex((row) => row.suffix.localeCompare(afterKey) < 0);
          keyIndex = nextIndex >= 0 ? nextIndex : keys.length;
        }
      }
      afterKey = "";
      let lastProcessedKey = "";

      while (keyIndex < keys.length && !stop) {
        const remainingScan = scanLimit - scannedCount;
        if (remainingScan <= 0) {
          stop = true;
          break;
        }
        const batchRows = keys.slice(
          keyIndex,
          Math.min(keys.length, keyIndex + ANALYTICS_HISTORY_READ_BATCH, keyIndex + remainingScan),
        );
        const batch = await readAnalyticsEventsByRows(env, batchRows);
        for (let index = 0; index < batchRows.length; index += 1) {
          lastProcessedKey = batchRows[index].suffix;
          keyIndex += 1;
          scannedCount += 1;
          if (analyticsHistoryEventMatches(batch[index], filters)) {
            events.push(publicAnalyticsEvent(batch[index]));
          }
          if (events.length >= pageSize || scannedCount >= scanLimit) {
            stop = true;
            break;
          }
        }
      }

      if (stop) {
        hasMore = keyIndex < keys.length || dateIndex < dateRows.length - 1;
        if (hasMore && lastProcessedKey) {
          nextCursor = encodeAnalyticsHistoryCursor({
            date: dateRow.date,
            after_key: lastProcessedKey,
            signature,
          });
        }
      }
    }

    return jsonResponse(request, env, 200, {
      events,
      next_cursor: nextCursor,
      has_more: hasMore,
      page_size: pageSize,
      scanned_count: scannedCount,
      available_dates: allDateRows.map((row) => row.date),
      newest_date: allDateRows.length ? allDateRows[0].date : "",
      oldest_date: allDateRows.length ? allDateRows[allDateRows.length - 1].date : "",
      generated_at: new Date().toISOString(),
    });
  } catch (error) {
    return jsonResponse(request, env, 503, { detail: error.message || "Analytics history is unavailable." });
  }
}

function analyticsEventVisitorKey(event) {
  return String(event && (event.visitor_id || event.ip_hash || (event.user && event.user.email)) || "");
}

function analyticsTopSearches(events, limit = 20) {
  const grouped = new Map();
  for (const event of events || []) {
    if (String(event.type || "") !== "search") continue;
    const query = cleanAnalyticsText(event.query, 240);
    if (!query) continue;
    const key = query.toLowerCase();
    const row = grouped.get(key) || {
      query,
      count: 0,
      visitors: new Set(),
      sources: {},
      last_at: "",
      total_result_count: 0,
    };
    row.count += 1;
    const visitor = analyticsEventVisitorKey(event);
    if (visitor) row.visitors.add(visitor);
    const source = cleanAnalyticsText(event.source || "unknown", 80) || "unknown";
    row.sources[source] = (row.sources[source] || 0) + 1;
    row.total_result_count += cleanAnalyticsNumber(event.result_count);
    if (String(event.ts || "") > row.last_at) row.last_at = String(event.ts || "");
    grouped.set(key, row);
  }
  return [...grouped.values()]
    .sort((a, b) => b.count - a.count || String(b.last_at).localeCompare(String(a.last_at)))
    .slice(0, limit)
    .map((row) => ({
      query: row.query,
      count: row.count,
      visitor_count: row.visitors.size,
      sources: row.sources,
      avg_result_count: row.count ? Math.round(row.total_result_count / row.count) : 0,
      last_at: row.last_at,
    }));
}

function analyticsTopReports(events, limit = 16) {
  const grouped = new Map();
  for (const event of events || []) {
    const type = String(event.type || "");
    if (type !== "report_open" && type !== "download_success") continue;
    const id = cleanAnalyticsText(event.report_id, 120);
    if (!id) continue;
    const row = grouped.get(id) || {
      report_id: id,
      title: cleanAnalyticsText(event.report_title, 260),
      source: cleanAnalyticsText(event.source, 80),
      opens: 0,
      downloads: 0,
      last_at: "",
    };
    if (type === "report_open") row.opens += 1;
    if (type === "download_success") row.downloads += 1;
    if (!row.title && event.report_title) row.title = cleanAnalyticsText(event.report_title, 260);
    if (String(event.ts || "") > row.last_at) row.last_at = String(event.ts || "");
    grouped.set(id, row);
  }
  return [...grouped.values()]
    .sort((a, b) => (b.opens + b.downloads * 2) - (a.opens + a.downloads * 2) || String(b.last_at).localeCompare(String(a.last_at)))
    .slice(0, limit);
}

function analyticsDailySeries(events) {
  const grouped = new Map();
  for (const event of events || []) {
    const date = cleanAnalyticsText(event.date || String(event.ts || "").slice(0, 10), 20);
    if (!date) continue;
    const row = grouped.get(date) || { date, events: 0, searches: 0, opens: 0, downloads: 0, visitors: new Set() };
    row.events += 1;
    if (event.type === "search") row.searches += 1;
    if (event.type === "report_open") row.opens += 1;
    if (event.type === "download_success") row.downloads += 1;
    const visitor = analyticsEventVisitorKey(event);
    if (visitor) row.visitors.add(visitor);
    grouped.set(date, row);
  }
  return [...grouped.values()]
    .sort((a, b) => String(a.date).localeCompare(String(b.date)))
    .map((row) => ({
      date: row.date,
      events: row.events,
      searches: row.searches,
      opens: row.opens,
      downloads: row.downloads,
      visitor_count: row.visitors.size,
    }));
}

async function buildAnalyticsDashboard(env) {
  const events = await listAnalyticsEvents(env);
  const visitorSet = new Set();
  const userSet = new Set();
  for (const event of events) {
    const visitor = analyticsEventVisitorKey(event);
    if (visitor) visitorSet.add(visitor);
    const userEmail = event.user && event.user.email;
    if (userEmail) userSet.add(userEmail);
  }
  return {
    range_days: ANALYTICS_DASHBOARD_DAYS,
    event_count: events.length,
    visitor_count: visitorSet.size,
    signed_in_user_count: userSet.size,
    search_count: events.filter((event) => event.type === "search").length,
    report_open_count: events.filter((event) => event.type === "report_open").length,
    download_success_count: events.filter((event) => event.type === "download_success").length,
    delivery_link_count: events.filter((event) => event.type === "delivery_link_generate").length,
    top_searches: analyticsTopSearches(events),
    top_reports: analyticsTopReports(events),
    daily: analyticsDailySeries(events),
    recent_events: events.slice(0, 120).map(publicAnalyticsEvent),
  };
}

function normalizeText(value) {
  return String(value || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function reportBankLabel(item) {
  const code = String(item.bank_code || "").trim();
  const name = String(item.bank_name || "").trim();
  return code && name && normalizeText(code) !== normalizeText(name) ? `${code} · ${name}` : (code || name || "Other");
}

function inferReportIndustry(item) {
  const explicit = item && (item.industry || item.sector || item.category);
  if (explicit) return String(explicit);
  const text = normalizeText([
    item && item.title,
    item && item.title_zh,
    item && item.filename,
  ].join(" "));
  for (const [label, pattern] of REPORT_INDUSTRY_RULES) {
    if (pattern.test(text)) return label;
  }
  return "Other";
}

function reportDisplayTitle(item) {
  return String(item.title_zh || item.title || item.filename || "Untitled report").trim();
}

function reportEnglishTitle(item) {
  return String(item.title || item.filename || "Untitled report").replace(/\.pdf$/i, "").trim();
}

function reportPageCount(item) {
  const pages = Number(item.page_count || 0);
  return Number.isFinite(pages) && pages > 0 ? pages : 0;
}

function reportIsLandscape(item) {
  if (item.first_page_landscape === true) return true;
  return String(item.first_page_orientation || "").toLowerCase() === "landscape";
}

function latestCatalogDateFolder(items) {
  return (items || [])
    .map((item) => String(item.date_folder || ""))
    .filter(Boolean)
    .sort((a, b) => dateScore(b) - dateScore(a) || b.localeCompare(a))[0] || "";
}

function recentCatalogDateFolders(items, maxDates = 14) {
  const seen = new Set();
  for (const item of items || []) {
    const date = String(item && item.date_folder || "");
    if (date) seen.add(date);
  }
  return Array.from(seen)
    .sort((a, b) => dateScore(b) - dateScore(a) || b.localeCompare(a))
    .slice(0, maxDates);
}

const DAILY_PICK_MACRO_KEYWORDS = [
  "macro", "global views", "global economics", "economics", "economic", "economy",
  "strategy", "asset allocation", "rates", "fx", "currency", "currencies", "cny",
  "dollar", "treasury", "bond", "yield", "central bank", "fed", "fomc", "ecb",
  "boj", "boe", "pboc", "inflation", "cpi", "pce", "pmi", "gdp", "recession",
  "policy", "fiscal", "monetary", "liquidity", "commodities", "commodity",
  "oil", "crude", "gold", "geopolitics", "tariff", "trade", "china economy",
  "asia insights", "global markets", "market outlook", "weekly", "monthly",
  "宏观", "央行", "货币政策", "财政", "利率", "汇率", "通胀", "经济", "增长",
  "衰退", "流动性", "大类资产", "资产配置", "地缘", "油价", "黄金", "贸易",
];

const DAILY_PICK_STOCK_PATTERNS = [
  /[（(][0-9]{4,6}\s*\.(?:hk|ss|sz|ch|us|jp|ks|tw|t)[）)]/i,
  /[（(][a-z]{1,6}\s*\.(?:us|o|n|ln|fp|gr|sw|ks|jp|t)[）)]/i,
  /\b(?:upgrade|downgrade|initiat(?:e|ion)|target price|price target|buy|sell|neutral|overweight|underweight)\b/i,
  /\b(?:results|earnings|investor day|valuation|eps|ebitda|revenue)\b/i,
  /公司|个股|目标价|评级|买入|卖出|增持|减持|业绩|财报|估值/,
];

const DAILY_PICK_SECTOR_PATTERN = /\b(?:shipbuilding|semiconductor|internet|media|technology|software|hardware|healthcare|property|real estate|autos?|automobile|retail|consumer|gaming|banks?|insurance|utilities|materials|chemicals?|pharma|biotech|airlines?|restaurants?|power equipment|capital goods|machinery)\b|造船|半导体|互联网|传媒|科技|地产|汽车|零售|消费|银行|保险|医药|航空|机械|电力设备/iu;

const DAILY_PICK_MACRO_ANCHOR_PATTERN = /\b(?:global views|global economics|economic outlook|economics|economy|macro|rates strategy|rates|fx|currency|currencies|central bank|fed|fomc|ecb|boj|boe|pboc|inflation|cpi|pce|pmi|gdp|recession|monetary|fiscal|asset allocation|global markets|market outlook)\b|宏观|央行|货币政策|财政|利率|汇率|通胀|经济展望|大类资产|资产配置|衰退|流动性/iu;

function dailyPickSourceText(item, bodyText = "") {
  return normalizeText(`${item.title || ""} ${item.title_zh || ""} ${item.filename || ""} ${String(bodyText || "").slice(0, 30000)}`);
}

function textMatches(text, patterns) {
  return patterns.some((pattern) => {
    if (pattern instanceof RegExp) return pattern.test(text);
    return text.includes(normalizeText(pattern));
  });
}

function addUnique(list, value) {
  const clean = String(value || "").trim();
  if (clean && !list.includes(clean)) list.push(clean);
}

function dailyPickTopicTags(item, bodyText = "") {
  const text = dailyPickSourceText(item, bodyText);
  const tags = [];
  const add = (tag) => {
    if (tag && !tags.includes(tag)) tags.push(tag);
  };
  if (/fed|fomc|ecb|boj|boe|pboc|central bank|央行|货币政策/.test(text)) add("央行政策");
  if (/oil|crude|commodity|commodities|gold|energy|油价|原油|黄金|大宗/.test(text)) add("大宗商品");
  if (/china|cny|pboc|中国|人民币/.test(text)) add("中国宏观");
  if (/fx|currency|dollar|usd|汇率|美元|外汇/.test(text)) add("汇率");
  if (/rates|treasury|bond|yield|利率|债券|国债/.test(text)) add("利率");
  if (/strategy|asset allocation|market outlook|global markets|大类资产|资产配置/.test(text)) add("资产配置");
  if (/inflation|cpi|pce|通胀/.test(text)) add("通胀");
  add("宏观趋势");
  const bank = String(item.bank_name || item.bank_code || "").replace(/\s+/g, "").trim();
  if (bank && bank.length <= 12) add(bank);
  return tags.slice(0, 4);
}

function dailyPickThemes(item, tags, bodyText = "") {
  const titleText = normalizeText(`${item.title || ""} ${item.title_zh || ""} ${item.filename || ""}`);
  const text = dailyPickSourceText(item, bodyText).slice(0, 16000);
  const focusedText = `${titleText} ${text}`;
  const indiaStrong = textMatches(titleText, [/\bindia\b|\binr\b|\brbi\b|印度|印度央行/]);
  const globalAggStrong = textMatches(titleText, [/\bglobal agg\b|\bglobal aggregate\b|index inclusion|指数纳入/]) ||
    textMatches(text, [/\bglobal aggregate index\b|bloomberg global aggregate|index inclusion/]);
  const themes = [];
  if (indiaStrong) addUnique(themes, "印度宏观与亚洲外汇利率");
  if (globalAggStrong) addUnique(themes, "全球综合债券指数纳入预期");
  if (indiaStrong && textMatches(focusedText, [/\bfx\b|currency|currencies|\bdollar\b|\busd\b|汇率|外汇|美元/])) addUnique(themes, "汇率市场");
  if (indiaStrong && textMatches(focusedText, [/\brates\b|treasury|\bbond\b|\byield\b|curve|债券|国债|收益率|利率/])) addUnique(themes, "利率与债券市场");
  if (textMatches(focusedText, [/\bfed\b|\bfomc\b|core pce|core cpi|rate hikes|on hold|美联储|加息/])) addUnique(themes, "美联储政策路径与美国通胀数据");
  if (textMatches(focusedText, [/payroll|unemployment|labor market|就业|失业率/])) addUnique(themes, "就业市场");
  if (textMatches(focusedText, [/\boil\b|crude|energy|middle east|iran|油价|原油|中东/])) addUnique(themes, "油价与地缘冲突");
  if (textMatches(focusedText, [/\bchina\b|\bcny\b|\bpboc\b|人民币|中国宏观/])) addUnique(themes, "中国宏观与人民币");
  if (textMatches(focusedText, [/inflation|\bcpi\b|\bpce\b|通胀/])) addUnique(themes, "通胀路径");
  if (textMatches(focusedText, [/fiscal|deficit|subsidy|财政|补贴/])) addUnique(themes, "财政压力");
  if (textMatches(focusedText, [/asset allocation|global markets|portfolio|资产配置|大类资产/])) addUnique(themes, "大类资产配置");
  if (textMatches(focusedText, [/\bgdp\b|growth|recession|经济增长|衰退/])) addUnique(themes, "经济增长与衰退概率");
  if (textMatches(focusedText, [/\bfx\b|currency|currencies|\bdollar\b|\busd\b|汇率|外汇|美元/])) addUnique(themes, "汇率市场");
  if (textMatches(focusedText, [/\brates\b|treasury|\bbond\b|\byield\b|curve|债券|国债|收益率|利率/])) addUnique(themes, "利率与债券市场");
  for (const tag of tags || []) {
    if (tag !== "宏观趋势" && tag !== item.bank_name && tag !== item.bank_code) addUnique(themes, tag);
  }
  return themes.slice(0, 4);
}

function dailyPickBodyInsights(item, bodyText = "") {
  const titleText = normalizeText(`${item.title || ""} ${item.title_zh || ""} ${item.filename || ""}`);
  const text = dailyPickSourceText(item, bodyText).slice(0, 22000);
  const focusedText = `${titleText} ${text}`;
  const indiaContext = textMatches(titleText, [/\bindia\b|\binr\b|\brbi\b|印度|印度央行/]);
  const fedContext = textMatches(focusedText, [/\bfed\b|\bfomc\b|core pce|core cpi|rate hikes|on hold|payroll|unemployment|labor market|美联储|加息|失业率|就业/]);
  const insights = [];
  const add = (value) => addUnique(insights, value);

  if (indiaContext && textMatches(text, [/q1 real gdp growth.*7\s*8.*yoy|7\s*8 yoy.*gdp|q1.*gdp.*above.*forecast/])) {
    add("印度一季度实际 GDP 同比约 7.8%，增长动能好于此前预期");
  }
  if (indiaContext && textMatches(text, [/raised.*cy26.*real gdp|raised.*fy27.*forecast|growth.*tracking above|gdp forecast.*raised/])) {
    add("增长预测被上修，反映投资、服务业和低油价带来的宏观改善");
  }
  if (indiaContext && textMatches(text, [/lower oil prices|oil forecasts.*revised lower|lower inflation trajectory|fertilizer subsidy|urea prices|油价/])) {
    add("油价下调和化肥价格回落缓解通胀与财政补贴压力");
  }
  if (indiaContext && textMatches(text, [/capital flow measures|foreign inflows|full fx hedging support|concessional fx swap|domestic equities.*limits|\brbi\b.*\bfx\b/])) {
    add("RBI 与印度政府通过外汇对冲、美元融资和投资额度等措施吸引资本流入");
  }
  if (indiaContext && textMatches(text, [/removed interest and capital gains tax|capital gains tax.*fii|local tax consultant|foreign investors/])) {
    add("取消 FII 投资政府债利息与资本利得税，降低外资进入本地债市的操作摩擦");
  }
  if (indiaContext && textMatches(text, [/fully accessible route|far universe|15 year 30 y|index eligibility|global aggregate index/])) {
    add("FAR 债券范围扩展至更长期限，改善进入 Bloomberg Global Aggregate Index 的条件");
  }
  if (textMatches(text, [/recommend going long|going long.*bond|long inr|做多/])) {
    add("配置结论指向做多相关长期债券或利率品种");
  }
  if (!indiaContext && textMatches(text, [/lower oil prices|oil prices.*came down|\boil\b|crude|middle east|iran|能源价格|油价/])) {
    add("油价和地缘局势变化会影响通胀预期、增长判断和政策路径");
  }

  if (fedContext && textMatches(text, [/\bfed\b.*stays on hold|fed on hold|on hold through year end|no rate hikes|美联储.*观望/])) {
    add("基准判断是美联储年内维持观望，是否重新加息取决于后续数据");
  }
  if (fedContext && textMatches(text, [/core pce.*0\s*2|core cpi.*0\s*2|monthly rates.*0\s*2|inflation.*0\s*2/])) {
    add("若核心 PCE/CPI 月率维持在 0.2% 或以下，加息压力相对有限");
  }
  if (fedContext && textMatches(text, [/core inflation.*0\s*3|0\s*3 m m|inflation remain.*0\s*3/])) {
    add("若核心通胀持续 0.3% 或更高，政策判断可能重新转鹰");
  }
  if (fedContext && textMatches(text, [/unemployment rate falls below 4\s*0|unemployment.*4\s*0|overheating labor market/])) {
    add("失业率若跌破 4.0%，劳动力市场过热会重新支撑加息风险");
  }
  if (fedContext && textMatches(text, [/payroll growth slows|employment growth|labor market data|就业增长/])) {
    add("就业增长放缓是其基准路径的重要前提");
  }

  if (textMatches(text, [/recession risk|recession probability|衰退/])) {
    add("衰退风险评估是资产市场定价的重要约束");
  }
  if (textMatches(text, [/ecb|boe|boj|pboc|central banks|央行/])) {
    add("主要央行的政策分化会影响利率、汇率和风险资产定价");
  }
  if (textMatches(text, [/tariff|trade|exports|imports|贸易|出口|进口/])) {
    add("贸易和出口变化会影响增长结构与市场预期");
  }
  if (textMatches(text, [/ai|artificial intelligence|估值|valuation/])) {
    add("AI 与估值变化仍是风险资产需要跟踪的变量");
  }

  return insights.slice(0, 5);
}

function chineseJoin(values, fallback = "") {
  const clean = values.map((value) => String(value || "").trim()).filter(Boolean);
  if (!clean.length) return fallback;
  if (clean.length === 1) return clean[0];
  return clean.join("、");
}

function dailyPickMacroScore(item) {
  const raw = `${item.title || ""} ${item.title_zh || ""} ${item.filename || ""}`;
  const text = normalizeText(raw);
  let score = 0;
  for (const keyword of DAILY_PICK_MACRO_KEYWORDS) {
    if (text.includes(normalizeText(keyword))) score += keyword.length > 8 ? 12 : 8;
  }
  if (/\b(?:global views|asia insights|economic|economics|macro|strategy)\b/i.test(raw)) score += 22;
  if (/宏观|经济|策略|大类资产|央行/.test(raw)) score += 18;
  if (DAILY_PICK_SECTOR_PATTERN.test(raw) && !DAILY_PICK_MACRO_ANCHOR_PATTERN.test(raw)) score -= 42;
  if (reportIsLandscape(item)) score += 120;
  const pages = reportPageCount(item);
  if (pages > 5) score += Math.min(28, pages);
  if (!pages) score -= 8;
  return score;
}

function isLikelySingleStockReport(item) {
  const text = `${item.title || ""} ${item.title_zh || ""} ${item.filename || ""}`;
  return DAILY_PICK_STOCK_PATTERNS.some((pattern) => pattern.test(text));
}

function dailyPickIntro(item, tags, bodyText = "") {
  const bank = String(item.bank_name || item.bank_code || "机构").trim();
  const title = reportEnglishTitle(item);
  const themes = dailyPickThemes(item, tags, bodyText);
  const insights = dailyPickBodyInsights(item, bodyText);
  const topicText = chineseJoin(themes.slice(0, 3), "全球宏观趋势、政策变化与资产市场");
  const landscapeText = reportIsLandscape(item) ? "这份 PDF 为横屏呈现，适合直接做会议讨论或素材摘图。" : "";
  const pageText = reportPageCount(item) ? `报告共 ${reportPageCount(item)} 页，` : "";
  const detailText = insights.length
    ? `核心围绕${chineseJoin(insights.slice(0, 3))}。${insights[3] ? `同时，报告也提示：${insights.slice(3, 5).join("，")}。` : ""}`
    : "核心适合关注宏观主线、政策预期和市场定价变化的读者快速把握当日信息。";
  const tagText = tags
    .map((tag) => String(tag || "").trim())
    .filter(Boolean)
    .map((tag) => `#${tag}`)
    .join("  ");
  return `${bank}报告《${title}》是对${topicText}的全面更新。${pageText}${detailText}${landscapeText}\n${tagText}`.trim();
}

function searchTextMapFromIndex(searchIndex) {
  const map = new Map();
  const entries = Array.isArray(searchIndex && searchIndex.items) ? searchIndex.items : [];
  for (const entry of entries) {
    if (entry && entry.id && entry.text) map.set(String(entry.id), String(entry.text));
  }
  return map;
}

function selectDailyPicks(catalog, maxItems = 5, searchIndex = null) {
  const items = Array.isArray(catalog && catalog.items) ? catalog.items : [];
  const searchTextById = searchIndex instanceof Map ? searchIndex : searchTextMapFromIndex(searchIndex);
  const dates = recentCatalogDateFolders(items);
  if (!dates.length) return [];

  const selected = [];
  const seenIds = new Set();
  const fallback = [];
  const addCandidate = (entry) => {
    const id = String(entry.item && entry.item.id || "");
    if (!id || seenIds.has(id) || selected.length >= maxItems) return;
    seenIds.add(id);
    selected.push(entry);
  };
  const sortEntries = (entries) => entries.sort((a, b) => {
    if (a.landscape !== b.landscape) return a.landscape ? -1 : 1;
    if (b.score !== a.score) return b.score - a.score;
    if (dateScore(b.date) !== dateScore(a.date)) return dateScore(b.date) - dateScore(a.date);
    if (b.pages !== a.pages) return b.pages - a.pages;
    return String(b.item.client_modified || b.item.server_modified || "").localeCompare(String(a.item.client_modified || a.item.server_modified || ""));
  });

  for (const date of dates) {
    const entries = items
      .filter((item) => String(item.date_folder || "") === date)
      .filter((item) => item && item.available !== false)
      .filter((item) => !isLikelySingleStockReport(item))
      .map((item) => {
        const score = dailyPickMacroScore(item);
        const pages = reportPageCount(item);
        const landscape = reportIsLandscape(item);
        const pageEligible = pages > 5 || pages === 0 || landscape;
        return { item, score, pages, landscape, pageEligible, date };
      })
      .filter((entry) => entry.pageEligible);
    const strict = sortEntries(entries.filter((entry) => entry.landscape || entry.score > 0));
    for (const entry of strict) addCandidate(entry);
    fallback.push(...entries);
    if (selected.length >= maxItems) break;
  }

  if (selected.length < maxItems) {
    for (const entry of sortEntries(fallback)) addCandidate(entry);
  }

  return selected.slice(0, maxItems).map(({ item, score, pages, landscape, date }) => {
    const bodyText = searchTextById.get(String(item.id || "")) || "";
    const tags = dailyPickTopicTags(item, bodyText);
    return {
      id: String(item.id || ""),
      title: reportEnglishTitle(item),
      title_zh: String(item.title_zh || ""),
      display_title: reportDisplayTitle(item),
      filename: item.filename || `${reportEnglishTitle(item)}.pdf`,
      bank: reportBankLabel(item),
      date_folder: date || String(item.date_folder || ""),
      page_count: pages,
      first_page_orientation: String(item.first_page_orientation || ""),
      first_page_landscape: landscape,
      size_bytes: Number(item.size_bytes || 0) || 0,
      score,
      tags,
      intro: dailyPickIntro(item, tags, bodyText),
    };
  });
}

async function listR2JsonObjects(env, prefix, limit = 500) {
  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") return [];
  const rows = [];
  let cursor = undefined;
  while (rows.length < limit) {
    const listed = await env.REPORT_BUCKET.list({
      prefix,
      limit: Math.min(1000, Math.max(1, limit - rows.length)),
      cursor,
    });
    const objects = Array.isArray(listed && listed.objects) ? listed.objects : [];
    const batch = await Promise.all(objects.map(async (object) => safeR2GetJson(env, object.key)));
    for (const row of batch) {
      if (row && typeof row === "object") rows.push(row);
      if (rows.length >= limit) break;
    }
    if (!listed || !listed.truncated || !listed.cursor) break;
    cursor = listed.cursor;
  }
  return rows;
}

async function listSiteUsers(env) {
  if (hasSupabaseConfig(env)) {
    const query = queryString({
      select: "id,username,email,email_is_generated,site_origin,registered_site,source_site,created_at,updated_at,last_login_at",
      order: "updated_at.desc",
      limit: "500",
    });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
    if (!Array.isArray(rows)) throw new Error("Account database response is invalid.");
    return Promise.all(rows.map((row) => mergeSiteUserAdminState(env, validateSiteUserRow(row))));
  }
  const rows = await listR2JsonObjects(env, accountKey("users", "id", ""), 500);
  const merged = await Promise.all(rows.map((row) => mergeSiteUserAdminState(env, validateSiteUserRow(row))));
  return merged.sort((a, b) => String(b.updated_at || "").localeCompare(String(a.updated_at || "")));
}

async function listEntitlementRows(env) {
  if (hasSupabaseConfig(env)) {
    const query = queryString({
      select: "email,site_origin,source_site,grant_source,source_plan_code,source_reference,plan,status,lifetime,current_period_end,updated_at",
      order: "updated_at.desc",
      limit: "1000",
    });
    const rows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
    if (!Array.isArray(rows)) throw new Error("Account database response is invalid.");
    return rows.map((row) => validateEntitlementRow(row, row && row.email));
  }
  const rows = await listR2JsonObjects(env, accountKey("entitlements", ""), 1000);
  return rows.map((row) => validateEntitlementRow(row, row && row.email));
}

function entitlementMap(rows) {
  const mapped = new Map();
  for (const row of rows || []) {
    const email = normalizeEmail(row && row.email);
    if (email && !mapped.has(email)) mapped.set(email, row);
  }
  return mapped;
}

function accessOptionRowsFromCatalog(catalog) {
  const items = Array.isArray(catalog && catalog.items) ? catalog.items : [];
  const institutions = new Map();
  const industries = new Map();
  for (const item of items) {
    const bank = reportBankLabel(item);
    if (bank) institutions.set(bank, (institutions.get(bank) || 0) + 1);
    const industry = inferReportIndustry(item);
    if (industry) industries.set(industry, (industries.get(industry) || 0) + 1);
  }
  const optionRows = (map) => [...map.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, 120)
    .map(([value, count]) => ({ value, label: `${value} (${count})` }));
  return {
    modes: [
      { value: "none", label: "关闭下载权限" },
      { value: "all", label: "全站报告" },
      { value: "filters", label: "按条件筛选" },
    ],
    institutions: optionRows(institutions),
    industries: optionRows(industries),
    page_ranges: ACCESS_PAGE_RANGE_OPTIONS,
    durations: ACCESS_DURATION_OPTIONS,
  };
}

function githubRepo(env) {
  return cleanEnv(env.GH_REPO) || cleanEnv(env.GITHUB_REPO) || DEFAULT_GITHUB_REPO;
}

function githubRef(env, repo = githubRepo(env)) {
  if (repo === BBG_SHOW_REPO) return DEFAULT_GITHUB_REF;
  if (repo === ENTERTAIN_CUT_REPO) return DEFAULT_GITHUB_REF;
  if (repo === RPT2VID_REPO) return DEFAULT_GITHUB_REF;
  const configured = cleanEnv(env.GH_REF) || cleanEnv(env.GITHUB_BRANCH) || cleanEnv(env.GITHUB_REF);
  if (!configured) return DEFAULT_GITHUB_REF;
  return configured.startsWith("refs/heads/") ? configured.slice("refs/heads/".length) : configured;
}

function githubToken(env, repo = githubRepo(env)) {
  const readToken = cleanEnv(env.GH_READ_TOKEN) || cleanEnv(env.GITHUB_TOKEN) || cleanEnv(env.GH_TOKEN);
  if (readToken) return readToken;
  return cleanEnv(env.GH_DISPATCH_TOKEN);
}

function githubHeaders(env, extra = {}, repo = githubRepo(env)) {
  const token = githubToken(env, repo);
  const headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "kc-desk-notes-worker",
    "X-GitHub-Api-Version": "2022-11-28",
    ...extra,
  };
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

function encodeGithubPath(path) {
  return String(path || "").split("/").filter(Boolean).map(encodeURIComponent).join("/");
}

async function githubApiFetch(env, path, init = {}, repo = githubRepo(env)) {
  const { timeoutMs, ...requestInit } = init || {};
  const response = await fetchWithTimeout(`https://api.github.com/repos/${repo}${path}`, {
    ...requestInit,
    headers: githubHeaders(env, requestInit.headers || {}, repo),
    redirect: requestInit.redirect || "follow",
  }, Number(timeoutMs) || GITHUB_API_TIMEOUT_MS);
  if (!response.ok) {
    const text = await response.text().catch(() => "");
    throw new Error(`GitHub API ${response.status}: ${text.slice(0, 200)}`);
  }
  return response;
}

async function githubApiJson(env, path, init = {}, repo = githubRepo(env)) {
  return (await githubApiFetch(env, path, init, repo)).json();
}

async function githubContents(env, path, repo = githubRepo(env), ref = githubRef(env, repo)) {
  const encoded = encodeGithubPath(path);
  const suffix = encoded ? `/contents/${encoded}` : "/contents";
  const query = `?ref=${encodeURIComponent(ref)}`;
  const data = await githubApiJson(env, `${suffix}${query}`, {}, repo);
  return Array.isArray(data) ? data : [];
}

async function githubContentJson(env, path, repo = githubRepo(env), ref = githubRef(env, repo)) {
  const encoded = encodeGithubPath(path);
  const data = await githubApiJson(env, `/contents/${encoded}?ref=${encodeURIComponent(ref)}`, {}, repo);
  const content = String(data && data.content || "").replace(/\s/g, "");
  if (!content) return null;
  const binary = atob(content);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }
  return JSON.parse(new TextDecoder().decode(bytes));
}

async function githubContentText(env, path, repo = githubRepo(env), ref = githubRef(env, repo)) {
  const encoded = encodeGithubPath(path);
  const data = await githubApiJson(env, `/contents/${encoded}?ref=${encodeURIComponent(ref)}`, {}, repo);
  const content = String(data && data.content || "").replace(/\s/g, "");
  if (!content) return "";
  const binary = atob(content);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }
  return new TextDecoder().decode(bytes);
}

async function fetchWithTimeout(resource, init = {}, timeoutMs = UPSTREAM_SEARCH_TIMEOUT_MS) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort("timeout"), timeoutMs);
  try {
    return await fetch(resource, {
      ...init,
      signal: controller.signal,
    });
  } finally {
    clearTimeout(timer);
  }
}

function newsfeedUserKey(user) {
  return encodeURIComponent(normalizeEmail(user && user.email) || normalizeUsername(user && user.username) || String(user && user.id || "user"));
}

function newsfeedTopicPrefix(user) {
  return `${NEWSFEED_TOPICS_PREFIX}/${newsfeedUserKey(user)}/`;
}

function newsfeedTopicKey(user, id) {
  return `${newsfeedTopicPrefix(user)}${encodeURIComponent(String(id || ""))}.json`;
}

function newsfeedSettingsKey(user) {
  return `${NEWSFEED_SETTINGS_PREFIX}/${newsfeedUserKey(user)}.json`;
}

function defaultNewsfeedSettings(user = null) {
  return {
    pinned: ["global-daily"],
    user_key: user ? newsfeedUserKey(user) : "",
    username: user && user.username || "",
    user_email: normalizeEmail(user && user.email) || "",
    digest_email_enabled: false,
    digest_email: normalizeEmail(user && user.email) || "",
    digest_send_time: NEWSFEED_EMAIL_DEFAULT_TIME,
    digest_timezone: NEWSFEED_EMAIL_DEFAULT_TIMEZONE,
    digest_language: "en",
    digest_last_sent_date: "",
    preferred_regions: ["global"],
    interface_language: "en",
  };
}

function normalizeNewsfeedTime(value) {
  const match = String(value || "").trim().match(/^([01]?\d|2[0-3]):([0-5]\d)$/);
  if (!match) return NEWSFEED_EMAIL_DEFAULT_TIME;
  return `${match[1].padStart(2, "0")}:${match[2]}`;
}

function normalizeNewsfeedTimezone(value) {
  const timezone = String(value || "").trim() || NEWSFEED_EMAIL_DEFAULT_TIMEZONE;
  try {
    new Intl.DateTimeFormat("en", { timeZone: timezone }).format(new Date());
    return timezone;
  } catch (_error) {
    return NEWSFEED_EMAIL_DEFAULT_TIMEZONE;
  }
}

function normalizeNewsfeedLanguage(value) {
  const code = String(value || "").trim();
  return NEWSFEED_OUTPUT_LANGUAGES.some((item) => item.code === code) ? code : "en";
}

function newsfeedLanguageInstruction(value) {
  const code = normalizeNewsfeedLanguage(value);
  return (NEWSFEED_OUTPUT_LANGUAGES.find((item) => item.code === code) || NEWSFEED_OUTPUT_LANGUAGES[0]).instruction;
}

function newsfeedLanguageLabel(value) {
  const code = normalizeNewsfeedLanguage(value);
  return (NEWSFEED_OUTPUT_LANGUAGES.find((item) => item.code === code) || NEWSFEED_OUTPUT_LANGUAGES[0]).label;
}

function normalizeNewsfeedRegionValue(value) {
  const clean = stripNewsfeedHtml(value).replace(/\s+/g, " ").trim().slice(0, 54);
  if (!clean) return "";
  const normalized = clean.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  const builtIn = NEWSFEED_REGIONS.find((region) => region.code === normalized || region.label.toLowerCase() === clean.toLowerCase());
  return builtIn ? builtIn.code : clean;
}

function normalizeNewsfeedRegions(value) {
  const raw = Array.isArray(value)
    ? value
    : String(value || "").split(",").map((item) => item.trim());
  const out = [];
  const seen = new Set();
  for (const item of raw) {
    const clean = normalizeNewsfeedRegionValue(item);
    const key = clean.toLowerCase();
    if (!clean || seen.has(key)) continue;
    seen.add(key);
    out.push(clean);
    if (out.length >= 8) break;
  }
  return out.length ? out : ["global"];
}

function newsfeedRegionLabel(value) {
  const clean = normalizeNewsfeedRegionValue(value);
  const builtIn = NEWSFEED_REGIONS.find((region) => region.code === clean);
  return builtIn ? builtIn.label : clean;
}

function publicNewsfeedRegions(values) {
  return normalizeNewsfeedRegions(values).map((value) => ({
    value,
    label: newsfeedRegionLabel(value),
    custom: !NEWSFEED_REGIONS.some((region) => region.code === value),
  }));
}

function newsfeedRegionQueryTerms(values) {
  return normalizeNewsfeedRegions(values)
    .map((value) => {
      const builtIn = NEWSFEED_REGIONS.find((region) => region.code === value);
      return builtIn ? builtIn.query : value;
    })
    .map(compactNewsfeedQuery)
    .filter(Boolean);
}

function applyNewsfeedRegionsToQuery(query, regions) {
  const cleanQuery = compactNewsfeedQuery(query);
  const regionTerms = newsfeedRegionQueryTerms(regions);
  if (!cleanQuery || !regionTerms.length) return cleanQuery;
  const regionClause = regionTerms.length === 1 ? regionTerms[0] : `(${regionTerms.join(" OR ")})`;
  return compactNewsfeedQuery(`${cleanQuery} ${regionClause}`);
}

function newsfeedGoogleLocale(regions, language) {
  const values = normalizeNewsfeedRegions(regions);
  const region = values
    .map((value) => NEWSFEED_REGIONS.find((item) => item.code === value))
    .find((item) => item && item.code !== "global");
  if (region && region.google) return region.google;
  const code = normalizeNewsfeedLanguage(language);
  if (code === "zh-CN") return { hl: "zh-CN", gl: "CN", ceid: "CN:zh-Hans" };
  if (code === "ja") return { hl: "ja", gl: "JP", ceid: "JP:ja" };
  if (code === "ko") return { hl: "ko", gl: "KR", ceid: "KR:ko" };
  return NEWSFEED_REGIONS[0].google;
}

function hasCloudflareEmailBinding(env) {
  return Boolean(env.EMAIL && typeof env.EMAIL.send === "function");
}

function hasBrevoEmailConfig(env) {
  return Boolean(cleanEnv(env.BREVO_API_KEY));
}

function newsfeedEmailProvider(env) {
  const configured = cleanEnv(env.NEWSFEED_EMAIL_PROVIDER).toLowerCase();
  if (configured === "brevo") return hasBrevoEmailConfig(env) ? "brevo" : "none";
  if (configured === "cloudflare") return hasCloudflareEmailBinding(env) ? "cloudflare" : "none";
  if (hasBrevoEmailConfig(env)) return "brevo";
  if (hasCloudflareEmailBinding(env)) return "cloudflare";
  return "none";
}

function newsfeedEmailFrom(env) {
  return cleanEnv(env.NEWSFEED_EMAIL_FROM) || "KC Desk Newsfeed <newsfeed@kcdesk.com>";
}

function newsfeedSender(env) {
  const fallback = newsfeedEmailFrom(env);
  const configuredEmail = normalizeEmail(env.BREVO_SENDER_EMAIL);
  const configuredName = cleanEnv(env.BREVO_SENDER_NAME);
  if (configuredEmail) return { email: configuredEmail, name: configuredName || "KC Desk Newsfeed" };
  const match = fallback.match(/^(.*?)<([^>]+)>$/);
  if (match) {
    return {
      name: match[1].trim().replace(/^"|"$/g, "") || "KC Desk Newsfeed",
      email: normalizeEmail(match[2]) || "newsfeed@kcdesk.com",
    };
  }
  return { name: "KC Desk Newsfeed", email: normalizeEmail(fallback) || "newsfeed@kcdesk.com" };
}

function publicNewsfeedSettings(settings, user, env) {
  const merged = { ...defaultNewsfeedSettings(user), ...(settings || {}) };
  const interfaceLanguage = normalizeNewsfeedLanguage(merged.interface_language || merged.digest_language || "en");
  const preferredRegions = normalizeNewsfeedRegions(merged.preferred_regions);
  return {
    digest_email_enabled: Boolean(merged.digest_email_enabled),
    digest_email: normalizeEmail(merged.digest_email),
    digest_send_time: normalizeNewsfeedTime(merged.digest_send_time),
    digest_timezone: normalizeNewsfeedTimezone(merged.digest_timezone),
    digest_language: normalizeNewsfeedLanguage(merged.digest_language),
    digest_last_sent_date: String(merged.digest_last_sent_date || ""),
    digest_last_sent_at: String(merged.digest_last_sent_at || ""),
    digest_last_attempt_at: String(merged.digest_last_attempt_at || ""),
    digest_last_send_result: String(merged.digest_last_send_result || ""),
    digest_last_send_detail: String(merged.digest_last_send_detail || ""),
    interface_language: interfaceLanguage,
    interface_language_label: newsfeedLanguageLabel(interfaceLanguage),
    preferred_regions: preferredRegions,
    preferred_region_labels: publicNewsfeedRegions(preferredRegions),
    email_provider_configured: newsfeedEmailProvider(env) !== "none",
    email_provider: newsfeedEmailProvider(env),
  };
}

function simpleNewsfeedId(value) {
  let hash = 2166136261;
  const text = String(value || "");
  for (let index = 0; index < text.length; index += 1) {
    hash ^= text.charCodeAt(index);
    hash = Math.imul(hash, 16777619);
  }
  return (hash >>> 0).toString(36);
}

function slugifyNewsfeed(value) {
  const cleaned = String(value || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 54);
  return cleaned || `topic-${simpleNewsfeedId(value)}`;
}

function decodeNewsfeedEntities(value) {
  const named = {
    amp: "&",
    lt: "<",
    gt: ">",
    quot: "\"",
    apos: "'",
    nbsp: " ",
  };
  return String(value || "").replace(/&(#x?[0-9a-f]+|[a-z]+);/gi, (match, entity) => {
    const key = String(entity || "").toLowerCase();
    if (named[key]) return named[key];
    if (key.startsWith("#x")) {
      const code = Number.parseInt(key.slice(2), 16);
      return Number.isFinite(code) ? String.fromCodePoint(code) : match;
    }
    if (key.startsWith("#")) {
      const code = Number.parseInt(key.slice(1), 10);
      return Number.isFinite(code) ? String.fromCodePoint(code) : match;
    }
    return match;
  });
}

function stripNewsfeedHtml(value) {
  return decodeNewsfeedEntities(String(value || "")
    .replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, "$1")
    .replace(/<[^>]+>/g, " "))
    .replace(/\s+/g, " ")
    .trim();
}

function compactNewsfeedQuery(value) {
  return String(value || "").normalize("NFKC").replace(/\s+/g, " ").trim().slice(0, 220);
}

function newsfeedUtcStamp(date) {
  const pad = (number) => String(number).padStart(2, "0");
  return [
    date.getUTCFullYear(),
    pad(date.getUTCMonth() + 1),
    pad(date.getUTCDate()),
    pad(date.getUTCHours()),
    pad(date.getUTCMinutes()),
    pad(date.getUTCSeconds()),
  ].join("");
}

function parseGdeltDate(value) {
  const text = String(value || "").trim();
  const match = text.match(/^(\d{4})(\d{2})(\d{2})T?(\d{2})(\d{2})(\d{2})Z?$/);
  if (!match) return text;
  return `${match[1]}-${match[2]}-${match[3]}T${match[4]}:${match[5]}:${match[6]}Z`;
}

function cleanNewsfeedUrl(value) {
  const raw = String(value || "").trim();
  if (!raw) return "";
  try {
    const url = new URL(raw);
    [...url.searchParams.keys()].forEach((key) => {
      if (/^utm_/i.test(key) || ["fbclid", "gclid", "mc_cid", "mc_eid"].includes(key.toLowerCase())) {
        url.searchParams.delete(key);
      }
    });
    url.hash = "";
    return url.toString();
  } catch (_error) {
    return raw;
  }
}

function domainFromUrl(value) {
  try {
    return new URL(value).hostname.replace(/^www\./i, "").toLowerCase();
  } catch (_error) {
    return "";
  }
}

function inferNewsfeedCategory(text, fallback = "Investment") {
  const haystack = String(text || "").toLowerCase();
  if (/(ai|robot|semiconductor|chip|software|data center|cloud|startup|technology|tech)/.test(haystack)) return "Tech";
  if (/(election|government|policy|sanction|tariff|war|defense|diplomacy|geopolitic|minister|president)/.test(haystack)) return "Politics";
  if (/(energy|manufactur|supply chain|healthcare|biotech|aerospace|logistics|industrial|factory|mining|transport)/.test(haystack)) return "Industries";
  if (/(ipo|funding|market|stock|bond|private equity|venture|investment|merger|acquisition|deal|bank)/.test(haystack)) return "Investment";
  return fallback || "Investment";
}

function newsfeedItem(input, defaults = {}) {
  const url = cleanNewsfeedUrl(input.url);
  const domain = input.domain || domainFromUrl(url);
  const source = input.source || input.source_name || domain || defaults.source || "News";
  const title = stripNewsfeedHtml(input.title || "");
  const summary = stripNewsfeedHtml(input.summary || input.description || "");
  const category = input.category || inferNewsfeedCategory(`${title} ${summary} ${source}`, defaults.category);
  const id = simpleNewsfeedId(`${title}|${url}|${source}`);
  return {
    id,
    title,
    url,
    source,
    domain,
    source_url: input.source_url || (domain ? `https://${domain}` : ""),
    logo_url: domain ? `https://www.google.com/s2/favicons?domain=${encodeURIComponent(domain)}&sz=64` : "",
    image_url: input.image_url || "",
    published_at: input.published_at || "",
    summary,
    category,
    query: input.query || defaults.query || "",
    provider: input.provider || defaults.provider || "",
  };
}

function dedupeNewsfeedItems(items) {
  const seen = new Set();
  const out = [];
  for (const item of items || []) {
    if (!item || !item.title) continue;
    const key = item.url ? cleanNewsfeedUrl(item.url).toLowerCase() : stripNewsfeedHtml(item.title).toLowerCase();
    if (!key || seen.has(key)) continue;
    seen.add(key);
    out.push(item);
  }
  return out;
}

function newsfeedSortValue(item) {
  const time = Date.parse(item && item.published_at || "");
  const base = Number.isFinite(time) ? time : 0;
  return base + (item && item.image_url ? 90 * 60 * 1000 : 0);
}

function newsfeedUpdatedLabel(value) {
  const timestamp = Date.parse(value || "");
  if (!Number.isFinite(timestamp)) return "";
  return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit", timeZone: "Asia/Shanghai" }).format(new Date(timestamp));
}

function googleNewsRssUrl(query, locale = "en-US", region = "US", ceid = "US:en") {
  const params = new URLSearchParams({ q: query, hl: locale, gl: region, ceid });
  return `https://news.google.com/rss/search?${params.toString()}`;
}

function rssAttribute(block, tagPattern, attribute) {
  const pattern = new RegExp(`<(?:${tagPattern})\\b[^>]*\\s${attribute}=["']([^"']+)["'][^>]*>`, "i");
  const match = String(block || "").match(pattern);
  return match ? decodeNewsfeedEntities(match[1]) : "";
}

function rssImageUrl(block) {
  return cleanNewsfeedUrl(
    rssAttribute(block, "media:content|media:thumbnail|enclosure", "url") ||
      rssAttribute(block, "image", "url"),
  );
}

function rssTag(block, tag) {
  const pattern = new RegExp(`<${tag}(?:\\s[^>]*)?>([\\s\\S]*?)<\\/${tag}>`, "i");
  const match = String(block || "").match(pattern);
  return match ? stripNewsfeedHtml(match[1]) : "";
}

function rssSource(block) {
  const match = String(block || "").match(/<source(?:\s+url="([^"]*)")?[^>]*>([\s\S]*?)<\/source>/i);
  if (!match) return { name: "", url: "" };
  return {
    name: stripNewsfeedHtml(match[2]),
    url: cleanNewsfeedUrl(decodeNewsfeedEntities(match[1] || "")),
  };
}

function parseGoogleNewsRss(xml, query, defaults = {}) {
  const out = [];
  const blocks = String(xml || "").match(/<item\b[\s\S]*?<\/item>/gi) || [];
  for (const block of blocks) {
    const source = rssSource(block);
    const link = cleanNewsfeedUrl(rssTag(block, "link"));
    const sourceDomain = domainFromUrl(source.url);
    const pubDate = rssTag(block, "pubDate");
    const parsedDate = Date.parse(pubDate);
    const item = newsfeedItem({
      title: rssTag(block, "title"),
      url: link,
      source: source.name || sourceDomain || "Google News",
      source_url: source.url || "https://news.google.com/",
      domain: sourceDomain || domainFromUrl(link),
      published_at: Number.isFinite(parsedDate) ? new Date(parsedDate).toISOString() : "",
      summary: rssTag(block, "description"),
      query,
      provider: "google-news-rss",
    }, defaults);
    if (item.title) out.push(item);
  }
  return out;
}

function parseGenericNewsRss(xml, defaults = {}) {
  const out = [];
  const blocks = String(xml || "").match(/<item\b[\s\S]*?<\/item>/gi) || [];
  const fallbackDomain = domainFromUrl(defaults.feed_url || defaults.url || "");
  for (const block of blocks) {
    const link = cleanNewsfeedUrl(rssTag(block, "link") || rssTag(block, "guid"));
    const pubDate = rssTag(block, "pubDate") || rssTag(block, "updated") || rssTag(block, "published");
    const parsedDate = Date.parse(pubDate);
    const item = newsfeedItem({
      title: rssTag(block, "title"),
      url: link,
      source: defaults.source || fallbackDomain || "RSS",
      source_url: defaults.feed_url || defaults.url || "",
      domain: fallbackDomain || domainFromUrl(link),
      published_at: Number.isFinite(parsedDate) ? new Date(parsedDate).toISOString() : "",
      summary: rssTag(block, "description") || rssTag(block, "content:encoded"),
      image_url: rssImageUrl(block),
      query: defaults.query || "",
      provider: "public-rss",
    }, defaults);
    if (item.title) out.push(item);
  }
  return out;
}

function newsfeedRssFeedsForSpec(spec) {
  const category = spec && spec.category || "";
  const feeds = NEWSFEED_PUBLIC_RSS_FEEDS.filter((feed) => !category || feed.category === category);
  if (category !== "Politics") {
    feeds.push(...NEWSFEED_PUBLIC_RSS_FEEDS.filter((feed) => feed.category === "Politics").slice(0, 1));
  }
  return feeds.slice(0, 3);
}

async function fetchGdeltNews(query, options = {}) {
  const cleanQuery = compactNewsfeedQuery(query);
  if (!cleanQuery) return [];
  const end = options.end || new Date();
  const start = options.start || new Date(end.getTime() - 36 * 60 * 60 * 1000);
  const params = new URLSearchParams({
    query: cleanQuery,
    mode: "artlist",
    format: "json",
    maxrecords: String(options.maxrecords || 50),
    sort: "hybridrel",
    startdatetime: newsfeedUtcStamp(start),
    enddatetime: newsfeedUtcStamp(end),
  });
  const response = await fetchWithTimeout(`https://api.gdeltproject.org/api/v2/doc/doc?${params.toString()}`, {
    headers: { "Accept": "application/json", "User-Agent": NEWSFEED_UA },
  }, options.timeout || 14000);
  if (!response.ok) return [];
  const payload = await response.json();
  return (payload.articles || []).map((article) => newsfeedItem({
    title: article.title || "",
    url: article.url || "",
    source: article.domain || "",
    domain: article.domain || domainFromUrl(article.url || ""),
    published_at: parseGdeltDate(article.seendate || ""),
    summary: article.domain || article.language || "",
    image_url: article.socialimage || "",
    query: cleanQuery,
    provider: "gdelt",
  }, options)).filter((item) => item.title && item.url);
}

async function fetchGoogleNews(query, options = {}) {
  const days = Math.max(1, Math.round((options.days || 2)));
  const regionalQuery = applyNewsfeedRegionsToQuery(query, options.regions || ["global"]);
  const cleanQuery = `${regionalQuery} when:${days}d`;
  const locale = newsfeedGoogleLocale(options.regions || ["global"], options.language || "en");
  const response = await fetchWithTimeout(googleNewsRssUrl(
    cleanQuery,
    options.locale || locale.hl,
    options.region || locale.gl,
    options.ceid || locale.ceid,
  ), {
    headers: { "Accept": "application/rss+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent": NEWSFEED_UA },
  }, options.timeout || 14000);
  if (!response.ok) return [];
  return parseGoogleNewsRss(await response.text(), query, options);
}

async function fetchPublicRssFeed(feed, spec = {}, options = {}) {
  const response = await fetchWithTimeout(feed.url, {
    headers: { "Accept": "application/rss+xml,application/xml;q=0.9,*/*;q=0.8", "User-Agent": NEWSFEED_UA },
  }, options.timeout || 10000);
  if (!response.ok) return [];
  return parseGenericNewsRss(await response.text(), {
    category: feed.category || spec.category,
    source: feed.source,
    feed_url: feed.url,
    query: (spec.queries && spec.queries[0]) || spec.query || spec.title || "",
    ...options,
  });
}

function newsfeedCacheKey(scope, key) {
  return `${NEWSFEED_CACHE_PREFIX}/${scope}/${simpleNewsfeedId(key)}.json`;
}

async function getNewsfeedCache(env, scope, key) {
  if (!env.REPORT_BUCKET) return null;
  try {
    const object = await env.REPORT_BUCKET.get(newsfeedCacheKey(scope, key));
    if (!object) return null;
    const data = JSON.parse(await object.text());
    return data && typeof data === "object" ? data : null;
  } catch (_error) {
    return null;
  }
}

async function putNewsfeedCache(env, scope, key, payload) {
  if (!env.REPORT_BUCKET) return;
  try {
    await env.REPORT_BUCKET.put(newsfeedCacheKey(scope, key), JSON.stringify({
      cached_at: new Date().toISOString(),
      payload,
    }), {
      httpMetadata: {
        contentType: "application/json; charset=utf-8",
        cacheControl: "public, max-age=1800",
      },
    });
  } catch (_error) {
    // Cache misses only make the next request fetch upstream again.
  }
}

function newsfeedCacheIsFresh(cache) {
  const cachedAt = Date.parse(cache && cache.cached_at || "");
  return Number.isFinite(cachedAt) && Date.now() - cachedAt < NEWSFEED_CACHE_FRESH_MS;
}

function newsfeedCacheIsUsable(cache, maxAgeMs) {
  const cachedAt = Date.parse(cache && cache.cached_at || "");
  return Number.isFinite(cachedAt) && Date.now() - cachedAt < maxAgeMs;
}

async function fetchNewsfeedItems(env, spec, options = {}) {
  const queries = (Array.isArray(spec && spec.queries) ? spec.queries : [spec && spec.query || spec && spec.title])
    .map(compactNewsfeedQuery)
    .filter(Boolean)
    .slice(0, options.queryLimit || 4);
  const regions = normalizeNewsfeedRegions(options.regions || spec && spec.regions || ["global"]);
  const language = normalizeNewsfeedLanguage(options.language || spec && spec.output_language || "en");
  const cacheKey = JSON.stringify({
    version: NEWSFEED_CACHE_VERSION,
    id: spec && spec.id,
    queries,
    category: spec && spec.category,
    regions,
    language,
    limit: options.limit || 30,
  });
  const fullCached = options.skipCache ? null : await getNewsfeedCache(env, "items", cacheKey);
  if (fullCached && fullCached.payload && newsfeedCacheIsFresh(fullCached)) {
    return { ...fullCached.payload, cached: true, cache_status: "fresh", cached_at: fullCached.cached_at };
  }
  if (options.allowStale && fullCached && fullCached.payload && newsfeedCacheIsUsable(fullCached, NEWSFEED_CACHE_STALE_MS)) {
    return { ...fullCached.payload, cached: true, cache_status: "stale", cached_at: fullCached.cached_at };
  }
  const cacheScope = options.fast ? "items-fast" : "items";
  const fastCached = options.fast || options.allowStale ? await getNewsfeedCache(env, cacheScope, cacheKey) : null;
  if (fastCached && fastCached.payload && newsfeedCacheIsUsable(fastCached, options.allowStale ? NEWSFEED_CACHE_STALE_MS : NEWSFEED_CACHE_FRESH_MS)) {
    return { ...fastCached.payload, cached: true, cache_status: options.allowStale && !newsfeedCacheIsFresh(fastCached) ? "stale" : "fresh", cached_at: fastCached.cached_at };
  }

  const tasks = [];
  if (options.includeGdelt && queries[0]) {
    const gdeltQuery = applyNewsfeedRegionsToQuery(queries[0], regions);
    tasks.push(fetchGdeltNews(gdeltQuery, {
      category: spec.category,
      query: queries[0],
      regions,
      language,
      timeout: options.sourceTimeout,
    }));
  }
  for (const query of queries) {
    tasks.push(fetchGoogleNews(query, {
      category: spec.category,
      query,
      regions,
      language,
      timeout: options.sourceTimeout,
    }));
  }
  const rssLimit = Number.isFinite(options.rssLimit) ? options.rssLimit : 3;
  for (const feed of newsfeedRssFeedsForSpec(spec).slice(0, rssLimit)) {
    tasks.push(fetchPublicRssFeed(feed, spec, {
      regions,
      language,
      timeout: options.sourceTimeout,
    }));
  }
  const settled = await Promise.allSettled(tasks);
  const items = [];
  for (const result of settled) {
    if (result.status === "fulfilled") items.push(...result.value);
  }
  const deduped = dedupeNewsfeedItems(items)
    .sort((a, b) => newsfeedSortValue(b) - newsfeedSortValue(a))
    .slice(0, options.limit || 30);
  const payload = {
    topic_id: spec && spec.id || "",
    items: deduped,
    updated_at: new Date().toISOString(),
    updated_label: newsfeedUpdatedLabel(new Date().toISOString()),
    regions,
    language,
  };
  await putNewsfeedCache(env, cacheScope, cacheKey, payload);
  if (!options.fast) await putNewsfeedCache(env, "items", cacheKey, payload);
  return { ...payload, cached: false, cache_status: "refreshed" };
}

async function requireNewsfeedUser(request, env) {
  const user = await currentUserFromRequest(env, request);
  if (!isNewsfeedAccount(user)) throw new Error("Newsfeed is not enabled for this account.");
  return user;
}

async function loadNewsfeedSettings(env, user) {
  return {
    ...defaultNewsfeedSettings(user),
    ...(await safeR2GetJson(env, newsfeedSettingsKey(user)) || {}),
  };
}

async function saveNewsfeedSettings(env, user, settings) {
  if (!env.REPORT_BUCKET) return settings;
  return r2PutJson(env, newsfeedSettingsKey(user), {
    ...(settings || {}),
    updated_at: new Date().toISOString(),
  });
}

function hasOwnField(object, field) {
  return Object.prototype.hasOwnProperty.call(object || {}, field);
}

function nextNewsfeedSettingsFromPayload(settings, user, payload = {}) {
  const hasDigestEnabled = hasOwnField(payload, "digest_email_enabled") || hasOwnField(payload, "enabled");
  const hasDigestEmail = hasOwnField(payload, "digest_email") || hasOwnField(payload, "email");
  const hasRegions = hasOwnField(payload, "preferred_regions") || hasOwnField(payload, "regions");
  const hasInterfaceLanguage = hasOwnField(payload, "interface_language") || hasOwnField(payload, "language");
  return {
    ...settings,
    user_key: newsfeedUserKey(user),
    username: String(user.username || ""),
    user_email: normalizeEmail(user.email) || "",
    digest_email_enabled: hasDigestEnabled ? Boolean(payload.digest_email_enabled || payload.enabled) : Boolean(settings.digest_email_enabled),
    digest_email: hasDigestEmail
      ? normalizeEmail(payload.digest_email || payload.email)
      : normalizeEmail(settings.digest_email || user.email),
    digest_send_time: normalizeNewsfeedTime(payload.digest_send_time || payload.send_time || settings.digest_send_time),
    digest_timezone: normalizeNewsfeedTimezone(payload.digest_timezone || payload.timezone || settings.digest_timezone),
    digest_language: normalizeNewsfeedLanguage(payload.digest_language || payload.output_language || settings.digest_language),
    interface_language: normalizeNewsfeedLanguage(hasInterfaceLanguage
      ? (payload.interface_language || payload.language)
      : (settings.interface_language || settings.digest_language)),
    preferred_regions: normalizeNewsfeedRegions(hasRegions
      ? (payload.preferred_regions || payload.regions)
      : settings.preferred_regions),
  };
}

async function loadNewsfeedCustomTopics(env, user) {
  const topics = await listR2JsonObjects(env, newsfeedTopicPrefix(user), NEWSFEED_MAX_USER_TOPICS + 20);
  return topics.filter(Boolean).sort((a, b) => Date.parse(b.created_at || "") - Date.parse(a.created_at || ""));
}

async function loadNewsfeedTopics(env, user) {
  const [settings, customTopics] = await Promise.all([
    loadNewsfeedSettings(env, user),
    loadNewsfeedCustomTopics(env, user),
  ]);
  const pinned = new Set(settings.pinned || []);
  return [
    ...NEWSFEED_DEFAULT_TOPICS.map((topic) => ({ ...topic, pinned: pinned.has(topic.id) })),
    ...customTopics.map((topic) => ({ ...topic, kind: "custom", pinned: pinned.has(topic.id) })),
  ];
}

function findNewsfeedTopic(topics, id) {
  return (topics || []).find((topic) => String(topic.id || "") === String(id || ""));
}

function digestFromNewsItems(items) {
  return (items || [])
    .slice(0, 4)
    .map((item) => {
      const source = item.source ? `${item.source}: ` : "";
      return `${source}${item.title}`.slice(0, 180);
    });
}

function topicCountLabel(topic) {
  if (topic.kind === "system") return "Latest";
  return topic.created_at ? newsfeedUpdatedLabel(topic.created_at) : "Custom";
}

function publicNewsfeedTopic(topic) {
  return {
    id: topic.id,
    title: topic.title,
    description: topic.description || "",
    kind: topic.kind || "custom",
    category: topic.category || "Investment",
    pinned: Boolean(topic.pinned),
    output_language: normalizeNewsfeedLanguage(topic.output_language),
    output_language_label: newsfeedLanguageLabel(topic.output_language),
    regions: publicNewsfeedRegions(topic.regions || ["global"]),
    last_updated_label: topicCountLabel(topic),
    query_plan: topic.query_plan || null,
  };
}

function fallbackNewsfeedTopicPackage(input, outputLanguage = "en") {
  const clean = compactNewsfeedQuery(input);
  const title = clean.length > 58 ? `${clean.slice(0, 55)}...` : clean;
  const words = clean.split(/\s+/).filter(Boolean);
  const compact = words.length > 1 ? `"${clean}"` : clean;
  return {
    title: title || "Custom Topic",
    description: `Latest reporting around ${title || "this topic"}.`,
    category: inferNewsfeedCategory(clean, "Investment"),
    queries: [
      compact,
      `${clean} news OR analysis`,
      `${clean} funding OR policy OR market`,
    ].filter(Boolean),
    query_plan: {
      source_mix: ["GDELT DOC", "Google News RSS"],
      include_terms: words.slice(0, 8),
      exclude_terms: ["advertisement", "coupon", "job posting"],
      refresh: "30 minutes",
    },
    output_language: normalizeNewsfeedLanguage(outputLanguage),
  };
}

function extractJsonObject(text) {
  const cleaned = String(text || "").trim().replace(/^```(?:json)?\s*/i, "").replace(/\s*```$/i, "");
  const start = cleaned.indexOf("{");
  const end = cleaned.lastIndexOf("}");
  if (start < 0 || end <= start) throw new Error("No JSON object returned.");
  return JSON.parse(cleaned.slice(start, end + 1));
}

async function deepseekJson(env, messages, options = {}) {
  const apiKey = cleanEnv(env.DEEPSEEK_API_KEY);
  if (!apiKey) return null;
  const baseUrl = cleanEnv(env.DEEPSEEK_BASE_URL) || "https://api.deepseek.com";
  const model = cleanEnv(env.DEEPSEEK_MODEL) || "deepseek-v4-flash";
  const response = await fetchWithTimeout(`${baseUrl.replace(/\/+$/, "")}/chat/completions`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model,
      thinking: { type: "disabled" },
      messages,
      temperature: options.temperature ?? 0.2,
      stream: false,
      response_format: { type: "json_object" },
    }),
  }, options.timeout || 45000);
  if (!response.ok) return null;
  const payload = await response.json();
  const content = payload && payload.choices && payload.choices[0] && payload.choices[0].message && payload.choices[0].message.content;
  if (!content) return null;
  try {
    return extractJsonObject(content);
  } catch (_error) {
    return null;
  }
}

async function generateNewsfeedTopicPackage(env, input, outputLanguage = "en") {
  const language = normalizeNewsfeedLanguage(outputLanguage);
  const fallback = fallbackNewsfeedTopicPackage(input, language);
  const generated = await deepseekJson(env, [
    {
      role: "system",
      content: "You create machine-readable newsfeed topic packages. Output strict JSON only. Do not invent specific news facts.",
    },
    {
      role: "user",
      content: JSON.stringify({
        task: "Turn the user's interest into a reusable global news grabbing plan.",
        user_topic: input,
        output_language: newsfeedLanguageInstruction(language),
        schema: {
          title: "short topic title",
          description: "one sentence",
          category: "Investment | Tech | Politics | Industries",
          queries: ["2-4 concise GDELT/Google News search queries"],
          query_plan: {
            source_mix: ["GDELT DOC", "Google News RSS"],
            include_terms: ["important terms"],
            exclude_terms: ["terms to avoid"],
            refresh: "30 minutes",
          },
        },
      }),
    },
  ], { temperature: 0.1, timeout: 12000 });
  if (!generated) return fallback;
  const queries = Array.isArray(generated.queries) ? generated.queries.map(compactNewsfeedQuery).filter(Boolean).slice(0, 4) : fallback.queries;
  return {
    title: stripNewsfeedHtml(generated.title || fallback.title).slice(0, 90),
    description: stripNewsfeedHtml(generated.description || fallback.description).slice(0, 220),
    category: NEWSFEED_CATEGORIES.includes(generated.category) ? generated.category : fallback.category,
    queries: queries.length ? queries : fallback.queries,
    query_plan: generated.query_plan || fallback.query_plan,
    output_language: language,
  };
}

function newsfeedPreferencesFromRequest(request, settings = {}) {
  const url = new URL(request.url);
  const regionsParam = url.searchParams.get("regions");
  const languageParam = url.searchParams.get("language");
  const regions = normalizeNewsfeedRegions(regionsParam ? regionsParam.split(",") : settings.preferred_regions);
  const language = normalizeNewsfeedLanguage(languageParam || settings.interface_language || settings.digest_language || "en");
  return { regions, language };
}

function newsfeedRegionOptionsPayload() {
  return NEWSFEED_REGIONS.map((region) => ({
    value: region.code,
    label: region.label,
  }));
}

async function handleNewsfeedHome(request, env) {
  try {
    const user = await requireNewsfeedUser(request, env);
    const [topics, settings] = await Promise.all([
      loadNewsfeedTopics(env, user),
      loadNewsfeedSettings(env, user),
    ]);
    const preferences = newsfeedPreferencesFromRequest(request, settings);
    const globalSpec = NEWSFEED_DEFAULT_TOPICS.find((topic) => topic.id === "global-daily") || NEWSFEED_DEFAULT_TOPICS[0];
    const defaultSpecs = NEWSFEED_DEFAULT_TOPICS.filter((topic) => topic.id !== "global-daily");
    const url = new URL(request.url);
    if (url.searchParams.get("fast") === "1") {
      const fastPromise = fetchNewsfeedItems(env, globalSpec, {
        limit: 24,
        includeGdelt: false,
        queryLimit: 2,
        rssLimit: 1,
        sourceTimeout: 2600,
        fast: true,
        allowStale: true,
        regions: preferences.regions,
        language: preferences.language,
      });
      const fastPayload = await Promise.race([fastPromise, sleep(3200).then(() => null)]);
      const headlines = fastPayload && fastPayload.items || [];
      return jsonResponse(request, env, 200, {
        partial: true,
        pending: !fastPayload || fastPayload.cache_status === "stale",
        updated_at: new Date().toISOString(),
        updated_label: fastPayload && fastPayload.updated_label || "Loading",
        digest_count: Math.min(99, headlines.length),
        daily_digest: digestFromNewsItems(headlines),
        highlights: headlines.filter((item) => item.image_url).slice(0, 5),
        headlines,
        categories: NEWSFEED_CATEGORIES,
        regions: newsfeedRegionOptionsPayload(),
        languages: NEWSFEED_OUTPUT_LANGUAGES.map(({ code, label }) => ({ code, label })),
        topics: topics.map(publicNewsfeedTopic),
        suggested_topics: NEWSFEED_SUGGESTED_TOPICS,
        settings: publicNewsfeedSettings({ ...settings, preferred_regions: preferences.regions, interface_language: preferences.language }, user, env),
      });
    }
    const fetched = await Promise.all([
      fetchNewsfeedItems(env, globalSpec, { limit: 20, includeGdelt: true, regions: preferences.regions, language: preferences.language }),
      ...defaultSpecs.map((topic) => fetchNewsfeedItems(env, topic, { limit: 14, regions: preferences.regions, language: preferences.language })),
    ]);
    const headlines = dedupeNewsfeedItems(fetched.flatMap((row) => row.items || []))
      .sort((a, b) => newsfeedSortValue(b) - newsfeedSortValue(a))
      .slice(0, 42);
    const highlights = headlines.filter((item) => item.image_url).slice(0, 5);
    return jsonResponse(request, env, 200, {
      updated_at: new Date().toISOString(),
      updated_label: newsfeedUpdatedLabel(new Date().toISOString()),
      digest_count: Math.min(99, headlines.length),
      daily_digest: digestFromNewsItems(headlines),
      highlights: highlights.length ? highlights : headlines.slice(0, 5),
      headlines,
      categories: NEWSFEED_CATEGORIES,
      regions: newsfeedRegionOptionsPayload(),
      languages: NEWSFEED_OUTPUT_LANGUAGES.map(({ code, label }) => ({ code, label })),
      topics: topics.map(publicNewsfeedTopic),
      suggested_topics: NEWSFEED_SUGGESTED_TOPICS,
      settings: publicNewsfeedSettings({ ...settings, preferred_regions: preferences.regions, interface_language: preferences.language }, user, env),
    });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Newsfeed unavailable." });
  }
}

async function handleNewsfeedExplore(request, env) {
  try {
    const user = await requireNewsfeedUser(request, env);
    const url = new URL(request.url);
    const settings = await loadNewsfeedSettings(env, user);
    const preferences = newsfeedPreferencesFromRequest(request, settings);
    const requested = url.searchParams.get("category") || "Tech";
    const spec = NEWSFEED_DEFAULT_TOPICS.find((topic) => topic.category === requested) || NEWSFEED_DEFAULT_TOPICS[1];
    const [topics, payload] = await Promise.all([
      loadNewsfeedTopics(env, user),
      fetchNewsfeedItems(env, spec, { limit: 34, includeGdelt: true, regions: preferences.regions, language: preferences.language }),
    ]);
    return jsonResponse(request, env, 200, {
      categories: NEWSFEED_CATEGORIES,
      regions: newsfeedRegionOptionsPayload(),
      languages: NEWSFEED_OUTPUT_LANGUAGES.map(({ code, label }) => ({ code, label })),
      category: spec.category,
      items: payload.items || [],
      updated_at: payload.updated_at,
      updated_label: payload.updated_label,
      cache_status: payload.cache_status,
      topics: topics.map(publicNewsfeedTopic),
    });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Newsfeed unavailable." });
  }
}

async function handleNewsfeedTopic(request, env) {
  try {
    const user = await requireNewsfeedUser(request, env);
    const url = new URL(request.url);
    const id = url.searchParams.get("id") || "global-daily";
    const [topics, settings] = await Promise.all([
      loadNewsfeedTopics(env, user),
      loadNewsfeedSettings(env, user),
    ]);
    const preferences = newsfeedPreferencesFromRequest(request, settings);
    const topic = findNewsfeedTopic(topics, id);
    if (!topic) return jsonResponse(request, env, 404, { detail: "Topic not found." });
    const payload = await fetchNewsfeedItems(env, topic, { limit: 34, includeGdelt: true, regions: preferences.regions, language: preferences.language });
    return jsonResponse(request, env, 200, {
      topic: { ...publicNewsfeedTopic(topic), updated_label: payload.updated_label },
      items: payload.items || [],
      topics: topics.map(publicNewsfeedTopic),
      cache_status: payload.cache_status,
    });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Newsfeed unavailable." });
  }
}

async function handleNewsfeedCreateTopic(request, env, ctx) {
  try {
    const user = await requireNewsfeedUser(request, env);
    const existing = await loadNewsfeedCustomTopics(env, user);
    if (existing.length >= NEWSFEED_MAX_USER_TOPICS) {
      return jsonResponse(request, env, 400, { detail: "Topic limit reached." });
    }
    const payload = await request.json().catch(() => ({}));
    const input = compactNewsfeedQuery(payload.topic || payload.query || "");
    if (input.length < 2) return jsonResponse(request, env, 400, { detail: "Topic is required." });
    const outputLanguage = normalizeNewsfeedLanguage(payload.output_language || payload.language || "en");
    const regions = normalizeNewsfeedRegions(payload.preferred_regions || payload.regions || ["global"]);
    const plan = await generateNewsfeedTopicPackage(env, input, outputLanguage);
    const id = `${slugifyNewsfeed(plan.title)}-${randomHex(3)}`;
    const topic = {
      id,
      kind: "custom",
      title: plan.title,
      description: plan.description,
      category: plan.category,
      output_language: outputLanguage,
      regions,
      queries: plan.queries,
      query_plan: plan.query_plan,
      created_from: input,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
    };
    await r2PutJson(env, newsfeedTopicKey(user, id), topic);
    const itemsPromise = fetchNewsfeedItems(env, topic, { limit: 34, skipCache: true, includeGdelt: true, regions, language: outputLanguage }).catch(() => null);
    const [topics, fastItems] = await Promise.all([
      loadNewsfeedTopics(env, user),
      Promise.race([itemsPromise, sleep(3500).then(() => null)]),
    ]);
    if (!fastItems && ctx && typeof ctx.waitUntil === "function") ctx.waitUntil(itemsPromise);
    const items = fastItems || { items: [], updated_label: "Preparing stories" };
    return jsonResponse(request, env, 201, {
      topic: { ...publicNewsfeedTopic(topic), updated_label: items.updated_label },
      items: items.items || [],
      topics: topics.map(publicNewsfeedTopic),
      pending: !fastItems,
    });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Could not create topic." });
  }
}

async function handleNewsfeedPinTopic(request, env) {
  try {
    const user = await requireNewsfeedUser(request, env);
    const payload = await request.json().catch(() => ({}));
    const id = String(payload.id || "").trim();
    const pinned = Boolean(payload.pinned);
    if (!id) return jsonResponse(request, env, 400, { detail: "Topic id is required." });
    const settings = await loadNewsfeedSettings(env, user);
    const next = new Set(settings.pinned || []);
    if (pinned) next.add(id);
    else next.delete(id);
    await saveNewsfeedSettings(env, user, { ...settings, pinned: [...next] });
    const topics = await loadNewsfeedTopics(env, user);
    return jsonResponse(request, env, 200, { topics: topics.map(publicNewsfeedTopic) });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Could not update topic." });
  }
}

async function handleNewsfeedSettings(request, env) {
  try {
    const user = await requireNewsfeedUser(request, env);
    const settings = await loadNewsfeedSettings(env, user);
    if (request.method === "GET") {
      return jsonResponse(request, env, 200, { settings: publicNewsfeedSettings(settings, user, env) });
    }
    const payload = await request.json().catch(() => ({}));
    const next = nextNewsfeedSettingsFromPayload(settings, user, payload);
    if (next.digest_email_enabled && !normalizeEmail(next.digest_email)) return jsonResponse(request, env, 400, { detail: "A valid email is required." });
    await saveNewsfeedSettings(env, user, next);
    return jsonResponse(request, env, 200, { settings: publicNewsfeedSettings(next, user, env) });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Could not save settings." });
  }
}

async function handleNewsfeedEmailSend(request, env, options = {}) {
  const isTest = Boolean(options.test);
  try {
    const user = await requireNewsfeedUser(request, env);
    const settings = await loadNewsfeedSettings(env, user);
    const payload = await request.json().catch(() => ({}));
    const next = nextNewsfeedSettingsFromPayload(settings, user, payload);
    const email = normalizeEmail(next.digest_email);
    if (!email) return jsonResponse(request, env, 400, { detail: "A valid email is required." });
    await saveNewsfeedSettings(env, user, next);
    const parts = newsfeedLocalParts(new Date(), next.digest_timezone);
    const due = { dateKey: newsfeedDateKey(parts), parts };
    let result;
    let recorded;
    try {
      ({ result } = await attemptNewsfeedDigestEmail(env, next, due, isTest
        ? { subject: `${newsfeedEmailSubject(next, due)} · Test` }
        : {}));
      recorded = await recordNewsfeedEmailAttempt(env, newsfeedUserKey(user), next, result, due, { test: isTest });
    } catch (error) {
      result = { sent: false, detail: error.message || "Email send failed." };
      recorded = await recordNewsfeedEmailAttempt(env, newsfeedUserKey(user), next, result, due, { test: isTest });
    }
    return jsonResponse(request, env, 200, {
      sent: Boolean(result && result.sent),
      detail: result && (result.detail || result.message) || "",
      provider: result && result.provider || newsfeedEmailProvider(env),
      message_id: result && result.messageId || "",
      test: isTest,
      settings: publicNewsfeedSettings(recorded || next, user, env),
    });
  } catch (error) {
    const fallback = isTest ? "Could not send test email." : "Could not send newsletter email.";
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || fallback });
  }
}

function fallbackArticleNarrative(article) {
  const title = stripNewsfeedHtml(article && article.title || "This story");
  const source = stripNewsfeedHtml(article && (article.source || article.domain) || "the source");
  const summary = stripNewsfeedHtml(article && article.summary || "");
  const language = normalizeNewsfeedLanguage(article && article.output_language);
  if (language === "zh-CN") {
    return {
      summary: summary ? `${source} 报道：${summary}` : `${source} 报道了这条新闻：${title}。`,
      narrative: [
        `${source} 正在报道「${title}」。`,
        summary ? `核心信息是：${summary}` : "这条标题显示事件仍在发展，后续需要结合更多原始来源继续跟踪。",
        "当前新闻流保留了原始来源链接，方便你打开原文核对细节和语境。",
      ].join("\n\n"),
    };
  }
  return {
    summary: summary || `${source} is reporting: ${title}.`,
    narrative: [
      `${source} is carrying a new story on ${title}.`,
      summary ? `The core read-through is ${summary}` : "The headline points to a developing story that is worth monitoring alongside follow-up coverage from primary sources.",
      "For now, the feed keeps the original source attached so the user can open the underlying article and compare the narrative against the reported facts.",
    ].join("\n\n"),
  };
}

async function generateArticleNarrative(env, article) {
  const outputLanguage = normalizeNewsfeedLanguage(article && article.output_language);
  const generated = await deepseekJson(env, [
    {
      role: "system",
      content: `You write concise news summaries in ${newsfeedLanguageInstruction(outputLanguage)}. Output strict JSON with summary and narrative. Base everything only on the provided article metadata.`,
    },
    {
      role: "user",
      content: JSON.stringify({
        title: article.title || "",
        source: article.source || article.domain || "",
        published_at: article.published_at || "",
        summary: article.summary || "",
        url: article.url || "",
        output_language: newsfeedLanguageInstruction(outputLanguage),
        required_json: { summary: "2 short sentences", narrative: "3 concise paragraphs" },
      }),
    },
  ], { temperature: 0.25, timeout: 45000 });
  const fallback = fallbackArticleNarrative(article);
  if (!generated) return fallback;
  return {
    summary: stripNewsfeedHtml(generated.summary || fallback.summary),
    narrative: stripNewsfeedHtml(generated.narrative || fallback.narrative),
  };
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function streamNewsfeedText(controller, encoder, type, text) {
  const chunks = String(text || "").match(/.{1,42}(\s|$)|.{1,42}/g) || [String(text || "")];
  for (const chunk of chunks) {
    controller.enqueue(encoder.encode(`${JSON.stringify({ type, text: chunk })}\n`));
    await sleep(18);
  }
}

async function handleNewsfeedArticle(request, env) {
  try {
    await requireNewsfeedUser(request, env);
    const payload = await request.json().catch(() => ({}));
    const article = payload.article || {};
    const result = await generateArticleNarrative(env, article);
    const encoder = new TextEncoder();
    const stream = new ReadableStream({
      async start(controller) {
        try {
          await streamNewsfeedText(controller, encoder, "summary", result.summary);
          await streamNewsfeedText(controller, encoder, "narrative", result.narrative);
          controller.enqueue(encoder.encode(`${JSON.stringify({ type: "done" })}\n`));
        } finally {
          controller.close();
        }
      },
    });
    return new Response(stream, {
      status: 200,
      headers: {
        ...corsHeaders(request, env),
        "Content-Type": "application/x-ndjson; charset=utf-8",
        "Cache-Control": "no-store",
      },
    });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Could not load story." });
  }
}

function newsfeedBriefingLimit(language) {
  const code = normalizeNewsfeedLanguage(language);
  return code === "zh-CN" || code === "ja" || code === "ko" ? 260 : 680;
}

function buildNewsfeedBriefingScript(input = {}) {
  const language = normalizeNewsfeedLanguage(input.language || input.output_language || "en");
  const digest = Array.isArray(input.digest) ? input.digest : [];
  const items = Array.isArray(input.items) ? input.items : [];
  const lines = digest.length
    ? digest
    : items.slice(0, 5).map((item) => `${item.source ? `${item.source}: ` : ""}${item.title || ""}`);
  const cleaned = lines.map(stripNewsfeedHtml).filter(Boolean).slice(0, 5);
  let text = "";
  if (language === "zh-CN") {
    text = [
      "这里是 KC Desk 三十秒新闻简报。",
      ...cleaned.map((line, index) => `第 ${index + 1} 条，${line}。`),
      "以上是当前新闻流重点。",
    ].join("");
  } else if (language === "ja") {
    text = [
      "KC Deskの30秒ニュースブリーフです。",
      ...cleaned.map((line, index) => `${index + 1}本目、${line}。`),
      "以上が現在のニュースフィードの要点です。",
    ].join("");
  } else if (language === "ko") {
    text = [
      "KC Desk 30초 뉴스 브리핑입니다.",
      ...cleaned.map((line, index) => `${index + 1}번째, ${line}.`),
      "이상 현재 뉴스피드 핵심입니다.",
    ].join(" ");
  } else {
    text = [
      "This is your KC Desk thirty second news briefing.",
      ...cleaned.map((line, index) => `Story ${index + 1}: ${line}.`),
      "That is the current read from your Newsfeed.",
    ].join(" ");
  }
  return text.slice(0, newsfeedBriefingLimit(language));
}

async function handleNewsfeedBriefing(request, env) {
  try {
    await requireNewsfeedUser(request, env);
    const payload = await request.json().catch(() => ({}));
    const script = buildNewsfeedBriefingScript(payload);
    return jsonResponse(request, env, 200, {
      script,
      provider: "browser-speech",
      audio_seconds_target: 30,
    });
  } catch (error) {
    return jsonResponse(request, env, accessErrorStatus(error), { detail: error.message || "Could not prepare briefing." });
  }
}

function escapeNewsfeedHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function newsfeedLocalParts(date, timezone) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: normalizeNewsfeedTimezone(timezone),
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hourCycle: "h23",
  }).formatToParts(date);
  const value = (type) => Number(parts.find((part) => part.type === type)?.value || 0);
  return {
    year: value("year"),
    month: value("month"),
    day: value("day"),
    hour: value("hour"),
    minute: value("minute"),
  };
}

function newsfeedDateKey(parts) {
  return `${String(parts.year).padStart(4, "0")}-${String(parts.month).padStart(2, "0")}-${String(parts.day).padStart(2, "0")}`;
}

function newsfeedEmailDue(settings, now = new Date()) {
  if (!settings || !settings.digest_email_enabled || !normalizeEmail(settings.digest_email)) return null;
  const parts = newsfeedLocalParts(now, settings.digest_timezone);
  const dateKey = newsfeedDateKey(parts);
  if (String(settings.digest_last_sent_date || "") === dateKey) return null;
  const [scheduledHour, scheduledMinute] = normalizeNewsfeedTime(settings.digest_send_time).split(":").map(Number);
  const scheduled = scheduledHour * 60 + scheduledMinute;
  const current = parts.hour * 60 + parts.minute;
  if (current < scheduled || current >= scheduled + NEWSFEED_EMAIL_WINDOW_MINUTES) return null;
  return { dateKey, parts };
}

async function fetchNewsfeedDigestPayload(env, settings = {}) {
  const globalSpec = NEWSFEED_DEFAULT_TOPICS.find((topic) => topic.id === "global-daily") || NEWSFEED_DEFAULT_TOPICS[0];
  const defaultSpecs = NEWSFEED_DEFAULT_TOPICS.filter((topic) => topic.id !== "global-daily");
  const regions = normalizeNewsfeedRegions(settings.preferred_regions);
  const language = normalizeNewsfeedLanguage(settings.digest_language || settings.interface_language || "en");
  const fetched = await Promise.all([
    fetchNewsfeedItems(env, globalSpec, { limit: 20, includeGdelt: true, regions, language }),
    ...defaultSpecs.map((topic) => fetchNewsfeedItems(env, topic, { limit: 10, regions, language })),
  ]);
  const headlines = dedupeNewsfeedItems(fetched.flatMap((row) => row.items || []))
    .sort((a, b) => newsfeedSortValue(b) - newsfeedSortValue(a))
    .slice(0, 24);
  return {
    updated_at: new Date().toISOString(),
    daily_digest: digestFromNewsItems(headlines),
    headlines,
    regions,
    language,
  };
}

function newsfeedEmailSubject(settings, due) {
  const dateText = due && due.dateKey || new Date().toISOString().slice(0, 10);
  if (normalizeNewsfeedLanguage(settings.digest_language) === "zh-CN") return `KC Desk Daily Digest · ${dateText}`;
  return `KC Desk Daily Digest · ${dateText}`;
}

function newsfeedEmailText(payload) {
  const lines = [
    "KC Desk Daily Digest",
    "",
    ...((payload.daily_digest || []).map((line) => `- ${line}`)),
    "",
    "Top headlines:",
    ...((payload.headlines || []).slice(0, 10).map((item, index) => `${index + 1}. ${item.title} (${item.source || item.domain || "News"})${item.url ? `\n   ${item.url}` : ""}`)),
  ];
  return lines.join("\n");
}

function newsfeedEmailHtml(payload) {
  const digest = (payload.daily_digest || []).map((line) => `<li>${escapeNewsfeedHtml(line)}</li>`).join("");
  const rows = (payload.headlines || []).slice(0, 12).map((item) => `
    <tr>
      <td style="padding:14px 0;border-top:1px solid #e5e7eb;">
        <a href="${escapeNewsfeedHtml(item.url || "https://kcdesk.com/newsfeed.html")}" style="color:#111827;font-size:17px;font-weight:700;text-decoration:none;">${escapeNewsfeedHtml(item.title)}</a>
        <div style="margin-top:6px;color:#6b7280;font-size:13px;">${escapeNewsfeedHtml([item.source || item.domain || "News", item.category].filter(Boolean).join(" · "))}</div>
      </td>
    </tr>
  `).join("");
  return `
    <div style="margin:0;padding:24px;background:#f6f7fb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#111827;">
      <div style="max-width:680px;margin:0 auto;background:#ffffff;border-radius:12px;padding:28px;">
        <h1 style="margin:0 0 18px;font-size:24px;">KC Desk Daily Digest</h1>
        <ul style="margin:0 0 24px;padding-left:20px;color:#374151;line-height:1.6;">${digest}</ul>
        <h2 style="margin:0 0 10px;font-size:18px;">Top headlines</h2>
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0">${rows}</table>
        <p style="margin:24px 0 0;color:#6b7280;font-size:13px;">Manage your Newsfeed email settings at <a href="https://kcdesk.com/newsfeed.html">kcdesk.com/newsfeed.html</a>.</p>
      </div>
    </div>
  `;
}

async function sendNewsfeedEmail(env, { to, subject, html, text }) {
  if (newsfeedEmailProvider(env) === "brevo") {
    const response = await fetchWithTimeout("https://api.brevo.com/v3/smtp/email", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "api-key": cleanEnv(env.BREVO_API_KEY),
      },
      body: JSON.stringify({
        sender: newsfeedSender(env),
        to: [{ email: to }],
        subject,
        htmlContent: html,
        textContent: text,
        tags: ["kcdesk-newsfeed"],
      }),
    }, 15000);
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const detail = data && (data.message || data.code)
        ? `${data.message || data.code}`
        : `Brevo returned HTTP ${response.status}.`;
      return { sent: false, provider: "brevo", detail };
    }
    return { sent: true, provider: "brevo", messageId: String(data.messageId || "") };
  }
  if (hasCloudflareEmailBinding(env)) {
    const response = await env.EMAIL.send({
      to,
      from: newsfeedEmailFrom(env),
      subject,
      html,
      text,
    });
    return { sent: true, provider: "cloudflare", response };
  }
  return { sent: false, detail: "Cloudflare Email binding is not configured." };
}

function opsAlertEmailHtml(subject, text, severity) {
  const color = severity === "critical" ? "#b42318" : severity === "warning" ? "#b54708" : "#175cd3";
  const paragraphs = String(text || "")
    .split(/\n{2,}/)
    .map((value) => `<p style="margin:0 0 14px;line-height:1.65;">${escapeNewsfeedHtml(value).replace(/\n/g, "<br>")}</p>`)
    .join("");
  return `
    <div style="margin:0;padding:24px;background:#f6f7fb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#111827;">
      <div style="max-width:680px;margin:0 auto;background:#ffffff;border-radius:8px;padding:28px;border-top:4px solid ${color};">
        <div style="margin:0 0 10px;color:${color};font-size:13px;font-weight:700;text-transform:uppercase;">KC Desk Operations</div>
        <h1 style="margin:0 0 20px;font-size:22px;line-height:1.35;">${escapeNewsfeedHtml(subject)}</h1>
        <div style="font-size:15px;color:#344054;">${paragraphs}</div>
      </div>
    </div>
  `;
}

async function handleOpsAlertEmail(request, env) {
  const rawBody = await request.text();
  try {
    await verifyOpsAlertSignature(request, env, rawBody);
  } catch (error) {
    return jsonResponse(request, env, 401, { detail: error.message || "Unauthorized." });
  }

  let payload;
  try {
    payload = JSON.parse(rawBody);
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Request body must be valid JSON." });
  }

  const recipient = normalizeEmail(env.OPS_ALERT_EMAIL);
  const subject = String(payload && payload.subject || "").replace(/\s+/g, " ").trim().slice(0, 160);
  const text = String(payload && payload.text || "").trim().slice(0, 6000);
  const dedupeKey = String(payload && payload.dedupe_key || "").trim().slice(0, 240);
  const severityValue = String(payload && payload.severity || "warning").trim().toLowerCase();
  const severity = ["info", "warning", "critical"].includes(severityValue) ? severityValue : "warning";
  if (!recipient) return jsonResponse(request, env, 503, { detail: "Operations alert recipient is not configured." });
  if (!subject || !text || !dedupeKey) {
    return jsonResponse(request, env, 400, { detail: "subject, text, and dedupe_key are required." });
  }

  const stateKey = `${OPS_ALERT_PREFIX}/${await sha256Hex(dedupeKey)}.json`;
  const previous = await safeR2GetJson(env, stateKey);
  const previousSentAt = Date.parse(String(previous && previous.sent_at || ""));
  if (previous && previous.sent && Number.isFinite(previousSentAt) && Date.now() - previousSentAt < OPS_ALERT_DEDUPE_MS) {
    return jsonResponse(request, env, 200, {
      sent: true,
      deduplicated: true,
      provider: String(previous.provider || ""),
      sent_at: String(previous.sent_at || ""),
    });
  }

  const result = await sendNewsfeedEmail(env, {
    to: recipient,
    subject,
    text,
    html: opsAlertEmailHtml(subject, text, severity),
  });
  const state = {
    sent: Boolean(result && result.sent),
    dedupe_key: dedupeKey,
    severity,
    subject,
    provider: String(result && result.provider || newsfeedEmailProvider(env)),
    message_id: String(result && result.messageId || ""),
    detail: String(result && result.detail || "").slice(0, 500),
    attempted_at: new Date().toISOString(),
    sent_at: result && result.sent ? new Date().toISOString() : "",
  };
  await r2PutJson(env, stateKey, state);
  return jsonResponse(request, env, state.sent ? 200 : 502, state);
}

async function attemptNewsfeedDigestEmail(env, settings, due, options = {}) {
  const email = normalizeEmail(settings.digest_email);
  if (!email) return { result: { sent: false, detail: "No digest email is configured." }, payload: null };
  const payload = await fetchNewsfeedDigestPayload(env, settings);
  const result = await sendNewsfeedEmail(env, {
    to: email,
    subject: options.subject || newsfeedEmailSubject(settings, due),
    html: newsfeedEmailHtml(payload),
    text: newsfeedEmailText(payload),
  });
  return { result, payload };
}

async function recordNewsfeedEmailAttempt(env, userKey, settings, result, due = null, options = {}) {
  const sent = Boolean(result && result.sent);
  const now = new Date().toISOString();
  const next = {
    ...settings,
    user_key: userKey,
    digest_last_attempt_at: now,
    digest_last_send_result: sent ? "sent" : "failed",
    digest_last_send_detail: sent ? "" : String(result && result.detail || result && result.message || "Email send failed.").slice(0, 500),
  };
  if (sent) {
    next.digest_last_sent_at = now;
    if (!options.test && due && due.dateKey) next.digest_last_sent_date = due.dateKey;
  }
  await r2PutJson(env, `${NEWSFEED_SETTINGS_PREFIX}/${userKey}.json`, next);
  return next;
}

async function sendDueNewsfeedDigestEmails(env) {
  if (!env.REPORT_BUCKET || newsfeedEmailProvider(env) === "none") return [];
  const settingsRows = await listR2JsonObjects(env, `${NEWSFEED_SETTINGS_PREFIX}/`, 10000);
  const dueRows = [];
  const now = new Date();
  for (const row of settingsRows) {
    const settings = { ...defaultNewsfeedSettings(), ...(row || {}) };
    const due = newsfeedEmailDue(settings, now);
    if (due) dueRows.push({ settings, due });
  }
  if (!dueRows.length) return [];
  const results = [];
  for (const { settings, due } of dueRows) {
    const email = normalizeEmail(settings.digest_email);
    if (!email) continue;
    const userKey = settings.user_key || newsfeedUserKey({ email: settings.user_email || email, username: settings.username || "" });
    let result;
    let next;
    try {
      ({ result } = await attemptNewsfeedDigestEmail(env, settings, due));
      next = await recordNewsfeedEmailAttempt(env, userKey, settings, result, due);
    } catch (error) {
      result = { sent: false, detail: error.message || "Email send failed." };
      next = await recordNewsfeedEmailAttempt(env, userKey, settings, result, due);
    }
    results.push({ email, result: next.digest_last_send_result });
  }
  return results;
}

async function warmNewsfeedCaches(env) {
  await Promise.all(NEWSFEED_DEFAULT_TOPICS.map((topic) => fetchNewsfeedItems(env, topic, { limit: 24 }).catch(() => null)));
}

function compactSearchQuery(value) {
  return String(value || "").normalize("NFKC").replace(/\s+/g, " ").trim().slice(0, 160);
}

async function searchCacheKey(source, query, page) {
  const digest = await sha256Hex(`${source}:${page}:${compactSearchQuery(query).toLowerCase()}`);
  return `${SEARCH_CACHE_PREFIX}/${source}/${digest}.json`;
}

async function getSearchCache(env, source, query, page) {
  if (!env.REPORT_BUCKET) return null;
  try {
    const object = await env.REPORT_BUCKET.get(await searchCacheKey(source, query, page));
    if (!object) return null;
    const data = JSON.parse(await object.text());
    return data && typeof data === "object" ? data : null;
  } catch (_error) {
    return null;
  }
}

async function putSearchCache(env, source, query, page, payload) {
  if (!env.REPORT_BUCKET) return;
  try {
    await env.REPORT_BUCKET.put(await searchCacheKey(source, query, page), JSON.stringify({
      source,
      query: compactSearchQuery(query),
      page,
      cached_at: new Date().toISOString(),
      payload,
    }), {
      httpMetadata: {
        contentType: "application/json; charset=utf-8",
        cacheControl: "public, max-age=21600",
      },
    });
  } catch (_error) {
    // Search cache is an acceleration layer only.
  }
}

function cachedPayloadIsFresh(cache) {
  const cachedAt = Date.parse(cache && cache.cached_at || "");
  return Number.isFinite(cachedAt) && Date.now() - cachedAt < SEARCH_CACHE_FRESH_MS;
}

function searchPayloadHasItems(payload) {
  return Boolean(payload && Array.isArray(payload.items) && payload.items.length > 0);
}

async function handleCachedSearch(request, env, source, query, page, emptyPayload, fetcher, fallbackFetcher = null, options = {}) {
  const cached = await getSearchCache(env, source, query, page);
  if (!options.skipFreshCache && cached && cached.payload && cachedPayloadIsFresh(cached)) {
    return jsonResponse(request, env, 200, {
      ...cached.payload,
      cached: true,
      cache_status: "fresh",
      cached_at: cached.cached_at || "",
    });
  }
  if (fallbackFetcher && options.preferFallback) {
    const fallback = await fallbackFetcher(null);
    if (searchPayloadHasItems(fallback)) {
      return jsonResponse(request, env, 200, {
        ...fallback,
        cached: true,
        cache_status: "mirror",
        warning: "已返回站内镜像结果。",
      });
    }
  }
  try {
    const payload = await fetcher();
    await putSearchCache(env, source, query, page, payload);
    return jsonResponse(request, env, 200, {
      ...payload,
      cached: false,
      cache_status: "refreshed",
    });
  } catch (error) {
    if (cached && cached.payload) {
      const fallback = fallbackFetcher ? await fallbackFetcher(error) : null;
      if (!searchPayloadHasItems(cached.payload) && searchPayloadHasItems(fallback)) {
        return jsonResponse(request, env, 200, {
          ...fallback,
          cached: true,
          cache_status: "mirror",
          warning: "已返回站内镜像结果。",
        });
      }
      return jsonResponse(request, env, 200, {
        ...cached.payload,
        cached: true,
        cache_status: "stale",
        cached_at: cached.cached_at || "",
        warning: "上游暂时不可用，已返回最近缓存结果。",
      });
    }
    if (fallbackFetcher) {
      const fallback = await fallbackFetcher(error);
      if (fallback) {
        return jsonResponse(request, env, 200, {
          ...fallback,
          cached: true,
          cache_status: "mirror",
          warning: "已返回站内镜像结果。",
        });
      }
    }
    return jsonResponse(request, env, 200, {
      ...emptyPayload,
      cached: false,
      cache_status: "miss",
      warning: "上游暂时不可用，暂无缓存结果。",
      upstream_error: String(error && error.message || error || "unavailable").slice(0, 160),
    });
  }
}

function searchMirrorKey(source) {
  return `${SEARCH_MIRROR_PREFIX}/${source}/latest.json`;
}

async function getSearchMirror(env, source) {
  if (!env.REPORT_BUCKET) return null;
  try {
    const object = await env.REPORT_BUCKET.get(searchMirrorKey(source));
    if (!object) return null;
    const data = JSON.parse(await object.text());
    return data && typeof data === "object" ? data : null;
  } catch (_error) {
    return null;
  }
}

function searchMirrorText(item) {
  return [
    item && item.title,
    item && item.title_cn,
    item && item.institution,
    item && item.date,
    item && item.summary,
    item && item.report_type,
    item && item.file_type,
    item && item.kind_label,
    item && item.author,
    item && item.stock_code,
    item && item.stock_name,
  ].filter(Boolean).join(" ").normalize("NFKC").toLowerCase();
}

function searchMirrorTerms(query) {
  const compact = compactSearchQuery(query).toLowerCase();
  if (!compact) return [];
  const tokens = compact.split(/[\s,，;；|/]+/).map((term) => term.trim()).filter((term) => term.length >= 2);
  return tokens.length ? tokens : [compact];
}

function scoreSearchMirrorItem(item, query, terms) {
  const title = String(item && (item.title || item.title_cn) || "").normalize("NFKC").toLowerCase();
  const institution = String(item && item.institution || "").normalize("NFKC").toLowerCase();
  const summary = String(item && item.summary || "").normalize("NFKC").toLowerCase();
  const haystack = searchMirrorText(item);
  const compact = compactSearchQuery(query).toLowerCase();
  let score = 0;
  if (compact && title.includes(compact)) score += 80;
  if (compact && institution.includes(compact)) score += 60;
  if (compact && summary.includes(compact)) score += 25;
  for (const term of terms) {
    if (title.includes(term)) score += 18;
    else if (institution.includes(term)) score += 14;
    else if (summary.includes(term)) score += 6;
    else if (haystack.includes(term)) score += 3;
    else return 0;
  }
  return score || (compact && haystack.includes(compact) ? 2 : 0);
}

function searchMirrorPayloadFromItems(items, query, page, pageSize) {
  const terms = searchMirrorTerms(query);
  const scored = (Array.isArray(items) ? items : [])
    .map((item) => ({ item, score: terms.length ? scoreSearchMirrorItem(item, query, terms) : 1 }))
    .filter((entry) => entry.score > 0)
    .sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      return dateScore(b.item && b.item.date) - dateScore(a.item && a.item.date);
    })
    .map((entry) => entry.item);
  const start = Math.max(0, (page - 1) * pageSize);
  return {
    items: scored.slice(start, start + pageSize),
    total: scored.length,
  };
}

async function searchMirrorFallback(env, source, query, page, pageSize, formatter) {
  const mirror = await getSearchMirror(env, source);
  const generatedAt = String(mirror && mirror.generated_at || "");
  const generatedMs = Date.parse(generatedAt);
  const stale = Number.isFinite(generatedMs) && Date.now() - generatedMs > SEARCH_MIRROR_STALE_MS;
  if (!mirror || !Array.isArray(mirror.items)) return null;
  const result = searchMirrorPayloadFromItems(mirror.items, query, page, pageSize);
  return formatter({
    ...result,
    generated_at: generatedAt,
    mirror_stale: Boolean(stale),
  });
}

function dateScore(value) {
  const text = String(value || "");
  const iso = text.match(/(20\d{2})-(\d{2})-(\d{2})/);
  if (iso) return Number(`${iso[1]}${iso[2]}${iso[3]}`);
  const match = text.match(/(\d{8}|\d{6})/);
  if (!match) return 0;
  const digits = match[1];
  return digits.length === 6 ? Number(`20${digits}`) : Number(digits);
}

function sortGithubDirsDesc(items) {
  return (items || [])
    .filter((item) => item && item.type === "dir")
    .sort((a, b) => {
      const score = dateScore(b.name || b.path) - dateScore(a.name || a.path);
      if (score) return score;
      return String(b.name || "").localeCompare(String(a.name || ""));
    });
}

function pad2(value) {
  return String(value).padStart(2, "0");
}

function bjtTodayFolder(now = Date.now()) {
  const shifted = new Date(now + 8 * 60 * 60 * 1000);
  const year = shifted.getUTCFullYear();
  const month = shifted.getUTCMonth() + 1;
  const day = shifted.getUTCDate();
  return `${String(year).slice(2)}${pad2(month)}${pad2(day)}`;
}

function dateFolderParts(folder) {
  const digits = String(folder || "").match(/^(\d{6}|\d{8})$/);
  if (!digits) return null;
  const value = digits[1];
  const year = value.length === 6 ? 2000 + Number(value.slice(0, 2)) : Number(value.slice(0, 4));
  const month = Number(value.slice(value.length - 4, value.length - 2));
  const day = Number(value.slice(value.length - 2));
  if (!year || !month || !day) return null;
  return { year, month, day };
}

function dateFolderIso(folder) {
  const parts = dateFolderParts(folder);
  if (!parts) return String(folder || "");
  return `${parts.year}-${pad2(parts.month)}-${pad2(parts.day)}`;
}

function dateFolderShortLabel(folder) {
  const parts = dateFolderParts(folder);
  if (!parts) return String(folder || "");
  return `${pad2(parts.month)}-${pad2(parts.day)}`;
}

function isWechatDateDirName(name) {
  return /^(\d{6}|\d{8})$/.test(String(name || ""));
}

function wechatArticleLabel(index) {
  const labels = ["头条", "二条", "三条", "四条", "五条", "六条", "七条", "八条", "九条"];
  return labels[index] || `${index + 1}条`;
}

function cleanWechatTitle(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function wechatArticlesFromTitles(titles) {
  return (Array.isArray(titles) ? titles : [])
    .map(cleanWechatTitle)
    .filter(Boolean)
    .map((title, index) => ({
      position: index + 1,
      label: wechatArticleLabel(index),
      title,
    }));
}

function wechatDraftTitles(draft) {
  if (!draft || typeof draft !== "object") return [];
  if (Array.isArray(draft.wechat_titles) && draft.wechat_titles.length) return draft.wechat_titles;
  if (Array.isArray(draft.titles) && draft.titles.length) return draft.titles;
  if (Array.isArray(draft.articles)) return draft.articles.map((article) => article && article.title);
  return [];
}

function wechatBatchFromDraft(entry, draft, fallbackIndex) {
  const draftIndex = Number(draft && draft.draft_index || fallbackIndex + 1) || fallbackIndex + 1;
  const articles = wechatArticlesFromTitles(wechatDraftTitles(draft));
  const articleCount = Number(draft && draft.article_count || articles.length) || articles.length;
  return {
    source_label: entry.source.label,
    source_date_folder: entry.name || "",
    source_date_iso: dateFolderIso(entry.name || ""),
    source_is_today: Boolean(entry.is_today),
    batch_no: draftIndex,
    batch_label: `${entry.source.label} ${draftIndex}`,
    article_count: articleCount,
    articles,
  };
}

function wechatBatchesFromSummary(entry, summary) {
  const drafts = Array.isArray(summary && summary.drafts) ? summary.drafts : [];
  if (drafts.length) return drafts.map((draft, index) => wechatBatchFromDraft(entry, draft, index));

  const articles = Array.isArray(summary && summary.articles) ? summary.articles : [];
  const perDraft = Math.min(9, Math.max(1, Number(summary && summary.articles_per_draft || 8) || 8));
  const batches = [];
  for (let index = 0; index < articles.length; index += perDraft) {
    const group = articles.slice(index, index + perDraft);
    batches.push(wechatBatchFromDraft(entry, {
      draft_index: batches.length + 1,
      article_count: group.length,
      articles: group,
    }, batches.length));
  }
  return batches;
}

async function wechatBatchesFromPayloads(env, entry) {
  const files = await githubContents(env, entry.path);
  const payloads = files
    .filter((item) => item && item.type === "file" && /^draft_payload_\d+\.json$/i.test(item.name || ""))
    .sort((a, b) => String(a.name || "").localeCompare(String(b.name || "")))
    .slice(0, 50);
  const batches = [];
  for (const file of payloads) {
    try {
      const payload = await githubContentJson(env, file.path);
      const match = String(file.name || "").match(/(\d+)/);
      batches.push(wechatBatchFromDraft(entry, {
        draft_index: match ? Number(match[1]) : batches.length + 1,
        articles: Array.isArray(payload && payload.articles) ? payload.articles : [],
      }, batches.length));
    } catch (_error) {
      // Keep the admin page usable even if one payload is malformed.
    }
  }
  return batches;
}

async function wechatDateDirs(env) {
  const entries = [];
  for (const source of WECHAT_DRAFT_SOURCES) {
    let dirs = [];
    try {
      dirs = await githubContents(env, source.root);
    } catch (_error) {
      continue;
    }
    for (const dir of dirs) {
      if (!dir || dir.type !== "dir" || !isWechatDateDirName(dir.name)) continue;
      entries.push({
        source,
        name: dir.name,
        path: dir.path,
      });
    }
  }
  return entries;
}

function selectWechatDateEntries(dirs, todayFolder) {
  const selected = [];
  for (const source of WECHAT_DRAFT_SOURCES) {
    const sourceDirs = dirs
      .filter((dir) => dir.source.root === source.root)
      .sort((a, b) => dateScore(b.name) - dateScore(a.name) || String(b.name || "").localeCompare(String(a.name || "")));
    if (!sourceDirs.length) continue;
    const today = sourceDirs.find((dir) => dir.name === todayFolder);
    if (source.legacy && !today) continue;
    const entry = today || sourceDirs[0];
    selected.push({
      ...entry,
      is_today: entry.name === todayFolder,
    });
  }
  if (!selected.length) {
    const latest = dirs
      .slice()
      .sort((a, b) => dateScore(b.name) - dateScore(a.name) || String(b.name || "").localeCompare(String(a.name || "")))[0];
    if (latest) selected.push({ ...latest, is_today: latest.name === todayFolder });
  }
  return selected;
}

async function wechatBatchesForEntries(env, dateEntries) {
  const batches = [];
  for (const entry of dateEntries) {
    let entryBatches = [];
    try {
      const summary = await githubContentJson(env, `${entry.path}/wechat_draft_summary.json`);
      entryBatches = wechatBatchesFromSummary(entry, summary);
    } catch (_error) {
      try {
        entryBatches = await wechatBatchesFromPayloads(env, entry);
      } catch (_fallbackError) {
        entryBatches = [];
      }
    }
    batches.push(...entryBatches.filter((batch) => batch.article_count > 0 || batch.articles.length));
  }
  return batches;
}

function wechatScheduleSlot(dateFolder, index, total) {
  const parts = dateFolderParts(dateFolder);
  const offsetMinutes = total <= 1 ? 0 : Math.round((990 * index) / (total - 1));
  const minuteOfDay = 8 * 60 + offsetMinutes;
  if (parts && minuteOfDay === 24 * 60) {
    return {
      scheduled_at_bjt: `${parts.year}-${pad2(parts.month)}-${pad2(parts.day)} 24:00`,
      scheduled_time: `${pad2(parts.month)}-${pad2(parts.day)} 24:00`,
      day_label: "当天",
    };
  }
  const dayOffset = Math.floor(minuteOfDay / (24 * 60));
  const localMinutes = minuteOfDay % (24 * 60);
  const hour = Math.floor(localMinutes / 60);
  const minute = localMinutes % 60;
  if (!parts) {
    return {
      scheduled_at_bjt: `${dateFolder} ${pad2(hour)}:${pad2(minute)}`,
      scheduled_time: `${pad2(hour)}:${pad2(minute)}`,
      day_label: dayOffset ? "次日" : "当天",
    };
  }
  const date = new Date(Date.UTC(parts.year, parts.month - 1, parts.day + dayOffset));
  const year = date.getUTCFullYear();
  const month = date.getUTCMonth() + 1;
  const day = date.getUTCDate();
  return {
    scheduled_at_bjt: `${year}-${pad2(month)}-${pad2(day)} ${pad2(hour)}:${pad2(minute)}`,
    scheduled_time: `${pad2(month)}-${pad2(day)} ${pad2(hour)}:${pad2(minute)}`,
    day_label: dayOffset ? "次日" : "当天",
  };
}

function applyWechatSchedule(dateFolder, batches) {
  const total = batches.length;
  return batches.map((batch, index) => ({
    ...batch,
    schedule_index: index + 1,
    total_batches: total,
    ...wechatScheduleSlot(dateFolder, index, total),
  }));
}

async function buildWechatDraftSchedule(env) {
  const todayFolder = bjtTodayFolder();
  const dirs = await wechatDateDirs(env);
  if (!dirs.length) {
    return {
      today_folder: todayFolder,
      date_folder: "",
      date_label: "",
      is_today: false,
      window: "08:00 - 次日 00:30",
      source_dates: [],
      total_batches: 0,
      total_articles: 0,
      batches: [],
    };
  }
  const dateEntries = selectWechatDateEntries(dirs, todayFolder);
  const batches = await wechatBatchesForEntries(env, dateEntries);
  const scheduled = applyWechatSchedule(todayFolder, batches);
  const sourceDates = dateEntries.map((entry) => ({
    source_label: entry.source.label,
    date_folder: entry.name,
    date_iso: dateFolderIso(entry.name),
    is_today: entry.name === todayFolder,
  }));
  const allSourcesToday = sourceDates.length > 0 && sourceDates.every((entry) => entry.is_today);
  return {
    today_folder: todayFolder,
    date_folder: todayFolder,
    date_iso: dateFolderIso(todayFolder),
    date_label: dateFolderShortLabel(todayFolder),
    is_today: allSourcesToday,
    window: "08:00 - 次日 00:30",
    source_dates: sourceDates,
    total_batches: scheduled.length,
    total_articles: scheduled.reduce((sum, batch) => sum + Number(batch.article_count || batch.articles.length || 0), 0),
    batches: scheduled,
  };
}

function adminGithubFile(kind, label, item, date, note = "", repo = "", extra = {}) {
  return {
    type: "file",
    kind,
    label,
    name: item.name || item.path.split("/").pop(),
    path: item.path,
    size_bytes: Number(item.size || 0),
    date: date || "",
    note,
    repo,
    ...extra,
  };
}

async function githubRecursiveTree(env, repo, ref = githubRef(env, repo)) {
  const data = await githubApiJson(env, `/git/trees/${encodeURIComponent(ref)}?recursive=1`, {}, repo);
  return Array.isArray(data && data.tree) ? data.tree : [];
}

async function latestMarketViewFiles(env, maxItems = 3) {
  const results = [];
  const dateDirs = sortGithubDirsDesc(await githubContents(env, "market_view_summaries"));
  for (const dateDir of dateDirs.slice(0, 20)) {
    const files = await githubContents(env, dateDir.path);
    const pdfs = files
      .filter((item) => item.type === "file" && /^market_views_.*\.pdf$/i.test(item.name || ""))
      .sort((a, b) => String(b.name || "").localeCompare(String(a.name || "")));
    for (const pdf of pdfs) {
      results.push(adminGithubFile("market-views", "Market Views PDF", pdf, dateDir.name));
      if (results.length >= maxItems) return results;
    }
  }
  return results;
}

function preferredVideoItem(items) {
  const files = (items || []).filter((item) => item.type === "file" && /\.mp4$/i.test(item.name || ""));
  const preferred = [
    "podcast_mixed_bilingual_explainer.mp4",
    "podcast_en_explainer.mp4",
    "podcast_zh_explainer.mp4",
  ];
  for (const name of preferred) {
    const item = files.find((file) => String(file.name || "").toLowerCase() === name);
    if (item) return item;
  }
  return files[0] || null;
}

function titleFromGeneratedPath(path) {
  const parts = String(path || "").split("/");
  const folder = parts.length >= 4 ? parts[3] : parts[parts.length - 2] || "";
  return folder.replace(/^\d{4}-/, "").replace(/[-_]+/g, " ").slice(0, 120);
}

function renderedClipDate(path) {
  const match = String(path || "").match(/^rendered-clips\/(?:[^/]*\/)*[^/]*(20\d{2}-\d{2}-\d{2})[^/]*\//);
  return match ? match[1] : "";
}

function isoDateAddDays(value, days) {
  const match = String(value || "").match(/^(20\d{2})-(\d{2})-(\d{2})$/);
  if (!match) return "";
  const date = new Date(Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3]) + Number(days || 0)));
  if (Number.isNaN(date.getTime())) return "";
  return date.toISOString().slice(0, 10);
}

function bbgRenderedClipInfo(path) {
  const clean = String(path || "").replace(/^\/+/, "");
  const parts = clean.split("/");
  const firstDate = renderedClipDate(clean);
  const source = parts[1] || "";
  if (source === "top-videos") {
    return {
      source: "top-videos",
      label: "BBG Top Videos",
      generatedDate: firstDate,
      contentDate: firstDate,
      sourceOrder: 1,
      notePrefix: "top-videos",
    };
  }
  if (source === "ark-invest") {
    return {
      source: "ark-invest",
      label: "ARK Invest 视频",
      generatedDate: firstDate,
      contentDate: firstDate,
      sourceOrder: 2,
      notePrefix: "ark-invest",
    };
  }
  const sourceDate = (source.match(/^(20\d{2}-\d{2}-\d{2})(?:$|[-_])/) || [])[1] || "";
  if (sourceDate) {
    const generatedDate = source === sourceDate ? isoDateAddDays(sourceDate, 1) : sourceDate;
    return {
      source: "daily-clips",
      label: "BBG Show 视频",
      generatedDate: generatedDate || sourceDate,
      contentDate: sourceDate,
      sourceOrder: 0,
      notePrefix: "普通 clips",
    };
  }
  return {
    source: "other",
    label: "BBG Show 视频",
    generatedDate: firstDate,
    contentDate: firstDate,
    sourceOrder: 3,
    notePrefix: "",
  };
}

function renderedClipNote(path, info = bbgRenderedClipInfo(path)) {
  const parts = String(path || "").split("/");
  const dateIndex = parts.findIndex((part) => /^20\d{2}-\d{2}-\d{2}$/.test(part));
  const noteParts = dateIndex >= 0 ? parts.slice(dateIndex + 1, -1) : parts.slice(1, -1);
  const detail = noteParts.length ? noteParts.join(" / ").replace(/[-_]+/g, " ") : "";
  const notes = [];
  if (info.notePrefix) notes.push(info.notePrefix);
  if (info.generatedDate) notes.push(`生成日期 ${info.generatedDate}`);
  if (info.contentDate && info.contentDate !== info.generatedDate) notes.push(`内容日期 ${info.contentDate}`);
  if (detail && detail !== info.notePrefix) notes.push(detail);
  return notes.join(" · ");
}

function bbgVideoTitleText(path) {
  const fileName = String(path || "").split("/").pop() || "";
  const folderParts = String(path || "").split("/").slice(0, -1);
  const folderHint = folderParts[folderParts.length - 1] || "";
  const cleanFile = fileName
    .replace(/\.mp4$/i, "")
    .replace(/^\d+[_-]+/, "")
    .replace(/[_-]+/g, " ")
    .trim();
  const cleanFolder = folderHint
    .replace(/^\d+[_-]+/, "")
    .replace(/[_-]+/g, " ")
    .trim();
  return `${cleanFile} ${cleanFolder}`.trim().toLowerCase();
}

function normalizeBbgGroupText(value) {
  return String(value || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, "");
}

function bbgVideoShareGroupKey(path, info = bbgRenderedClipInfo(path)) {
  const fileName = String(path || "").split("/").pop() || "";
  const stem = fileName
    .replace(/\.mp4$/i, "")
    .replace(/^\d+[_\-＿-]+/, "")
    .trim();
  const parts = stem.split(/[_＿]+/).map((part) => part.trim()).filter(Boolean);
  const shareSource = parts.length >= 2 ? parts[0] : "";
  const normalized = normalizeBbgGroupText(shareSource);
  if (normalized.length < 4) return "";
  return [
    info && info.source || "",
    info && (info.contentDate || info.generatedDate) || "",
    normalized.slice(0, 120),
  ].join("|");
}

function accountLabelMatch(text, rules) {
  let score = 0;
  const reasons = [];
  for (const [label, weight, pattern] of rules) {
    if (pattern.test(text)) {
      score += weight;
      reasons.push(label);
    }
  }
  return { score, reasons };
}

const DESKTOP_VIDEO_RULES = [
  ["机构/分析师/报告型内容", 4.0, /高盛|野村|clsa|中银|瀚亚|花旗|汇丰|瑞银|美银|巴克莱|伯恩斯坦|bernstein|pimco|摩根士丹利|分析师|策略师|完整版|报告|解读|lagarde|拉加德|央行|fed|fomc|美联储|通胀/i],
  ["中国宏观/楼市/政策/信贷消费", 3.2, /楼市|房价|城市更新|地产|住房|信贷|消费|k型|k型分化|价值陷阱|财富效应|政策转向|复苏路径|人民币|中国经济/i],
  ["投研结构化主题", 2.0, /路径|展望|周期|定价|估值|复苏|转向|策略|配置|预测|三大方向|十五五|低估值|阿里腾讯|半导体|泡沫/i],
  ["行业政策/产业研究", 1.6, /绿色电力|能源预测|产业|行业|电力|半导体|银行体系|通胀回落|欧洲银行|能源局/i],
];

const BIAS_VIDEO_RULES = [
  ["地缘/历史/公共议题叙事", 3.5, /特朗普|伊朗|美伊|巴基斯坦|巴拿马|运河|中美博弈|俄罗斯|乌克兰|美军|白宫|共和制|罗斯福|克拉苏|格林斯潘|最高法院|world cup|世界杯|法院|election|选票|burnham|伯纳姆/i],
  ["科技趋势/个人观点感", 2.8, /deepseek|token|人形机器人|机器人|ai资本开支|数据中心|aidc|苹果|科技股|ai叙事|催化剂|云收入|经验工人|中国科技股|rocket lab|space.?x|ark|cathie|wood|tesla|bitcoin|芯片|人工智能/i],
  ["市场叙事/反直觉标题", 1.9, /悖论|被低估|低估|爆发|暗藏|扛住|教训|言论|回调掩盖|机会|可期|走强|油价下跌|黄金|日元贬值|mania|warning|surge/i],
  ["泛商业/生活化新闻", 1.4, /汽水|票房|温网|球迷|索尼|康卡斯特|创始人|收购|comcast|sony|tennis|wimbledon|soda|box office|nbcuniversal/i],
];

function bbgVideoAccountRecommendation(path, info) {
  const text = `${bbgVideoTitleText(path)} ${info && info.source || ""}`.toLowerCase();
  const desktop = accountLabelMatch(text, DESKTOP_VIDEO_RULES);
  const bias = accountLabelMatch(text, BIAS_VIDEO_RULES);
  if (info && info.source === "ark-invest") {
    bias.score += 1.4;
    bias.reasons.push("ARK/创新投资更贴近 KC偏见");
  }
  if (info && info.source === "top-videos" && desktop.score === 0 && bias.score === 0) {
    bias.score += 0.7;
    bias.reasons.push("top-videos 默认偏新闻/观点流");
  }
  if (info && info.source === "daily-clips" && desktop.score === 0 && bias.score === 0) {
    bias.score += 0.5;
    bias.reasons.push("普通 clips 默认偏观点短评");
  }
  const account = desktop.score > bias.score ? "KC桌面" : "KC偏见";
  const diff = Math.abs(desktop.score - bias.score);
  const confidence = diff >= 3.5 ? "高" : (diff >= 1.5 ? "中" : "低");
  const reasons = account === "KC桌面" ? desktop.reasons : bias.reasons;
  return {
    recommended_account: account,
    account_label_confidence: confidence,
    account_label_reason: reasons.slice(0, 3).join("；") || "两边接近，按默认内容风格推荐",
    kc_bias_score: Number(bias.score.toFixed(2)),
    kc_desktop_score: Number(desktop.score.toFixed(2)),
  };
}

function explicitKcVideoAccountLabel(value) {
  const text = String(value || "");
  if (/KC桌面/i.test(text)) return "KC桌面";
  if (/KC偏见/i.test(text)) return "KC偏见";
  return "";
}

function rpt2vidAccountRecommendation(path) {
  const fileName = String(path || "").split("/").pop() || "";
  const explicit = explicitKcVideoAccountLabel(fileName);
  const text = bbgVideoTitleText(path);
  const desktop = accountLabelMatch(text, DESKTOP_VIDEO_RULES);
  const bias = accountLabelMatch(text, BIAS_VIDEO_RULES);
  if (explicit) {
    if (explicit === "KC桌面") desktop.score += 6;
    if (explicit === "KC偏见") bias.score += 6;
    return {
      recommended_account: explicit,
      account_label_confidence: "高",
      account_label_reason: "文件名显式标注",
      kc_bias_score: Number(bias.score.toFixed(2)),
      kc_desktop_score: Number(desktop.score.toFixed(2)),
    };
  }
  if (desktop.score === 0 && bias.score === 0) {
    desktop.score += 0.8;
    desktop.reasons.push("报告视频默认偏投研/报告解读");
  }
  const account = desktop.score > bias.score ? "KC桌面" : "KC偏见";
  const diff = Math.abs(desktop.score - bias.score);
  const confidence = diff >= 3.5 ? "高" : (diff >= 1.5 ? "中" : "低");
  const reasons = account === "KC桌面" ? desktop.reasons : bias.reasons;
  return {
    recommended_account: account,
    account_label_confidence: confidence,
    account_label_reason: reasons.slice(0, 3).join("；") || "两边接近，按默认内容风格推荐",
    kc_bias_score: Number(bias.score.toFixed(2)),
    kc_desktop_score: Number(desktop.score.toFixed(2)),
  };
}

function applyBbgVideoGroupMajority(files) {
  const groups = new Map();
  for (const file of files || []) {
    const key = String(file && file._bbg_group_key || "");
    if (!key) continue;
    const rows = groups.get(key) || [];
    rows.push(file);
    groups.set(key, rows);
  }
  for (const rows of groups.values()) {
    if (rows.length < 2) continue;
    const desktopCount = rows.filter((row) => row.recommended_account === "KC桌面").length;
    const biasCount = rows.filter((row) => row.recommended_account === "KC偏见").length;
    const desktopScore = rows.reduce((sum, row) => sum + Number(row.kc_desktop_score || 0), 0);
    const biasScore = rows.reduce((sum, row) => sum + Number(row.kc_bias_score || 0), 0);
    const chosen = desktopCount > biasCount
      ? "KC桌面"
      : (biasCount > desktopCount ? "KC偏见" : (desktopScore >= biasScore ? "KC桌面" : "KC偏见"));
    const chosenCount = chosen === "KC桌面" ? desktopCount : biasCount;
    const confidence = chosenCount === rows.length ? "高" : "中";
    for (const row of rows) {
      const previousReason = String(row.account_label_reason || "");
      row.recommended_account = chosen;
      row.account_label_confidence = confidence;
      row.account_label_reason = `同源视频多数原则：${rows.length}条同组视频统一为${chosen}（${chosenCount}/${rows.length}）；${previousReason}`;
    }
  }
  applyBbgVideoAccountBalance(files);
  return (files || []).map((file) => {
    if (file && Object.prototype.hasOwnProperty.call(file, "_bbg_group_key")) delete file._bbg_group_key;
    return file;
  });
}

function applyBbgVideoAccountBalance(files) {
  const groups = new Map();
  (files || []).forEach((file, index) => {
    const account = String(file && file.recommended_account || "");
    if (account !== "KC桌面" && account !== "KC偏见") return;
    const key = String(file && file._bbg_group_key || `single:${index}`);
    const rows = groups.get(key) || [];
    rows.push(file);
    groups.set(key, rows);
  });
  const blocks = [...groups.values()].map((rows) => {
    const desktopScore = rows.reduce((sum, row) => sum + Number(row.kc_desktop_score || 0), 0);
    const biasScore = rows.reduce((sum, row) => sum + Number(row.kc_bias_score || 0), 0);
    const desktopRows = rows.filter((row) => row.recommended_account === "KC桌面").length;
    const biasRows = rows.filter((row) => row.recommended_account === "KC偏见").length;
    const account = desktopRows >= biasRows ? "KC桌面" : "KC偏见";
    return {
      rows,
      account,
      size: rows.length,
      margin: Math.abs(desktopScore - biasScore) / Math.max(1, rows.length),
    };
  });
  let desktopTotal = blocks.reduce((sum, block) => sum + (block.account === "KC桌面" ? block.size : 0), 0);
  let biasTotal = blocks.reduce((sum, block) => sum + (block.account === "KC偏见" ? block.size : 0), 0);
  for (let guard = 0; guard < blocks.length && Math.abs(desktopTotal - biasTotal) > 1; guard += 1) {
    const majority = desktopTotal > biasTotal ? "KC桌面" : "KC偏见";
    const minority = majority === "KC桌面" ? "KC偏见" : "KC桌面";
    const currentDiff = Math.abs(desktopTotal - biasTotal);
    const candidate = blocks
      .filter((block) => block.account === majority)
      .map((block) => {
        const nextDesktop = majority === "KC桌面" ? desktopTotal - block.size : desktopTotal + block.size;
        const nextBias = majority === "KC偏见" ? biasTotal - block.size : biasTotal + block.size;
        return { block, nextDiff: Math.abs(nextDesktop - nextBias) };
      })
      .filter((entry) => entry.nextDiff < currentDiff)
      .sort((a, b) => a.nextDiff - b.nextDiff || a.block.margin - b.block.margin || a.block.size - b.block.size)[0];
    if (!candidate) break;
    candidate.block.account = minority;
    if (majority === "KC桌面") {
      desktopTotal -= candidate.block.size;
      biasTotal += candidate.block.size;
    } else {
      biasTotal -= candidate.block.size;
      desktopTotal += candidate.block.size;
    }
    for (const row of candidate.block.rows) {
      const previousReason = String(row.account_label_reason || "");
      row.recommended_account = minority;
      row.account_label_confidence = row.account_label_confidence === "低" ? "低" : "中";
      row.account_label_reason = `数量均衡：后台列表 KC桌面/KC偏见 数量偏差，整组调整为${minority}；${previousReason}`;
    }
  }
}

function adminVideoDecodeText(value) {
  const raw = String(value || "");
  try {
    return decodeURIComponent(raw);
  } catch (_error) {
    return raw;
  }
}

function adminVideoFileStem(file) {
  const source = adminVideoDecodeText(file && (file.path || file.name) || "");
  const fileName = source.split(/[?#]/)[0].split("/").pop() || source;
  return fileName
    .normalize("NFKC")
    .replace(/\.(?:mp4|mov|m4v|webm)$/i, "")
    .replace(/[_\-\s]*(?:KC桌面|KC偏见)$/i, "")
    .replace(/^\d{4}-\d{2}-\d{2}[_\-\s]+/, "")
    .replace(/^\d{6,8}[_\-\s]+/, "")
    .replace(/^\d{1,3}[_\-.\s:：]+/, "")
    .trim();
}

function cleanAdminVideoGroupSegment(value) {
  return String(value || "")
    .normalize("NFKC")
    .replace(/\s+/g, "")
    .replace(/^(?:分享|访谈|采访|专访|完整版|片段|视频|观点|解读)+/i, "")
    .replace(/(?:第?\d+[条段集期]|上集|下集|上|下)$/i, "")
    .replace(/^[\s_\-:：|｜]+|[\s_\-:：|｜]+$/g, "")
    .trim();
}

function adminVideoLeadingPersonSegment(stem) {
  const text = String(stem || "").trim();
  if (!text) return "";
  const known = text.match(/^(特朗普|拜登|鲍威尔|拉加德|马斯克|黄仁勋|奥特曼|泽连斯基|普京|黑田东彦|植田和男)/);
  if (known) return known[1];
  const englishName = text.match(/^([A-Z][A-Za-z]+(?:[A-Z][a-z]+|[ -][A-Z][a-z]+){1,3})\b/);
  if (englishName) return englishName[1];
  const cjkWithRole = text.match(/^([\p{Script=Han}A-Za-z0-9·.\s-]{2,36}?(?:基金经理|分析师|策略师|经济学家|首席|CEO|CFO|创始人|主席|总统|总理|行长|主管))/u);
  if (cjkWithRole) return cjkWithRole[1];
  const cjkName = text.match(/^([\p{Script=Han}·]{2,4})(?:称|说|表示|认为|警告|分享|解读|谈|看好|看空)/u);
  return cjkName ? cjkName[1] : "";
}

function adminVideoContinuitySegment(file) {
  const stem = adminVideoFileStem(file);
  if (!stem) return "";
  const underscoreParts = stem.split(/[_＿]+/).map(cleanAdminVideoGroupSegment).filter(Boolean);
  if (underscoreParts.length >= 2) return underscoreParts[0];
  const pipeParts = stem.split(/[|｜]+/).map(cleanAdminVideoGroupSegment).filter(Boolean);
  if (pipeParts.length >= 2) return pipeParts[0];
  const dashParts = stem.split(/\s[-–—]\s/).map(cleanAdminVideoGroupSegment).filter(Boolean);
  if (dashParts.length >= 2) return dashParts[0];
  return adminVideoLeadingPersonSegment(stem);
}

function adminVideoContinuityKey(file) {
  const account = String(file && file.recommended_account || "");
  if (account !== "KC桌面" && account !== "KC偏见") return "";
  const name = String(file && (file.name || file.path || "") || "");
  const kind = String(file && file.kind || "");
  const label = String(file && file.label || "");
  if (!/\.mp4(?:$|\?)/i.test(name) && !/视频|video/i.test(`${kind} ${label}`)) return "";
  const segment = cleanAdminVideoGroupSegment(adminVideoContinuitySegment(file));
  const normalized = normalizeBbgGroupText(segment);
  const genericSegments = new Set(["中国", "美国", "市场", "科技", "行业", "公司", "报告", "新闻", "普通clips", "topvideos"]);
  if (!normalized || normalized.length < 3 || genericSegments.has(normalized)) return "";
  const date = String(file && file.date || "").slice(0, 10);
  return [
    kind || label || "video",
    label || "",
    date,
    normalized.slice(0, 120),
  ].join("|");
}

function applyAdminVideoContinuityMajority(files) {
  const list = Array.isArray(files) ? files : [];
  const groups = new Map();
  for (const file of list) {
    const key = adminVideoContinuityKey(file);
    if (!key) continue;
    const rows = groups.get(key) || [];
    rows.push(file);
    groups.set(key, rows);
  }
  for (const rows of groups.values()) {
    if (rows.length < 2) continue;
    const desktopCount = rows.filter((row) => row.recommended_account === "KC桌面").length;
    const biasCount = rows.filter((row) => row.recommended_account === "KC偏见").length;
    if (!desktopCount || !biasCount) continue;
    const desktopScore = rows.reduce((sum, row) => sum + Number(row.kc_desktop_score || 0), 0);
    const biasScore = rows.reduce((sum, row) => sum + Number(row.kc_bias_score || 0), 0);
    const chosen = desktopCount > biasCount
      ? "KC桌面"
      : (biasCount > desktopCount ? "KC偏见" : (desktopScore >= biasScore ? "KC桌面" : "KC偏见"));
    const chosenCount = chosen === "KC桌面" ? desktopCount : biasCount;
    for (const row of rows) {
      const previousReason = String(row.account_label_reason || "");
      row.recommended_account = chosen;
      row.account_label_confidence = chosenCount === rows.length ? "高" : "中";
      const prefix = `同一人物连续视频统一为${chosen}（${chosenCount}/${rows.length}）`;
      row.account_label_reason = previousReason.includes("同一人物连续视频统一")
        ? previousReason
        : `${prefix}；${previousReason}`.replace(/；$/, "");
    }
  }
  return list;
}

function bbgClipTakeLimit(source) {
  if (source === "daily-clips") return 8;
  if (source === "top-videos") return 10;
  if (source === "ark-invest") return 8;
  return 4;
}

function isGithubMp4File(item) {
  return item && item.type === "file" && /\.mp4$/i.test(String(item.name || item.path || ""));
}

function sortGithubEntriesDesc(items) {
  return (items || [])
    .slice()
    .sort((a, b) => {
      const score = dateScore(b && (b.name || b.path)) - dateScore(a && (a.name || a.path));
      if (score) return score;
      return String(b && (b.name || b.path) || "").localeCompare(String(a && (a.name || a.path) || ""));
    });
}

async function githubContentsOrEmpty(env, path, repo, timeoutMs = GITHUB_API_TIMEOUT_MS) {
  return resolveWithin(githubContents(env, path, repo), timeoutMs, []);
}

async function collectGithubMp4Files(env, repo, dirPath, options = {}) {
  const maxFiles = Math.max(1, Number(options.maxFiles || 20));
  const nestedDirLimit = Math.max(0, Number(options.nestedDirLimit || 0));
  const entries = await githubContentsOrEmpty(env, dirPath, repo, options.timeoutMs || GITHUB_API_TIMEOUT_MS);
  const files = sortGithubEntriesDesc(entries.filter(isGithubMp4File));
  if (files.length >= maxFiles || nestedDirLimit <= 0) return files.slice(0, maxFiles);

  const nestedDirs = sortGithubEntriesDesc(entries.filter((item) => item && item.type === "dir")).slice(0, nestedDirLimit);
  const nested = await Promise.all(nestedDirs.map((dir) => collectGithubMp4Files(env, repo, dir.path, {
    maxFiles,
    nestedDirLimit: 0,
    timeoutMs: options.timeoutMs || GITHUB_API_TIMEOUT_MS,
  })));
  return [...files, ...nested.flat()].slice(0, maxFiles);
}

async function bbgNestedSourceFiles(env, sourceDir, maxDateDirs, maxFilesPerDir) {
  const children = await githubContentsOrEmpty(env, sourceDir.path, BBG_SHOW_REPO, GITHUB_API_TIMEOUT_MS);
  const dateDirs = sortGithubEntriesDesc(children.filter((item) => item && item.type === "dir")).slice(0, maxDateDirs);
  const dirs = dateDirs.length ? dateDirs : [sourceDir];
  const groups = await Promise.all(dirs.map((dir) => collectGithubMp4Files(env, BBG_SHOW_REPO, dir.path, {
    maxFiles: maxFilesPerDir,
    nestedDirLimit: maxFilesPerDir,
    timeoutMs: GITHUB_API_TIMEOUT_MS,
  })));
  return groups.flat();
}

async function bbgRenderedClipFilesFromContents(env) {
  const roots = await githubContentsOrEmpty(env, BBG_SHOW_PREFIX, BBG_SHOW_REPO, ADMIN_GITHUB_SOURCE_TIMEOUT_MS);
  const rootFiles = roots.filter(isGithubMp4File);
  const rootDirs = roots.filter((item) => item && item.type === "dir");
  const sourceTasks = [];
  const topVideos = rootDirs.find((dir) => String(dir.name || "") === "top-videos");
  const arkInvest = rootDirs.find((dir) => String(dir.name || "") === "ark-invest");
  if (topVideos) sourceTasks.push(bbgNestedSourceFiles(env, topVideos, 1, 12));
  if (arkInvest) sourceTasks.push(bbgNestedSourceFiles(env, arkInvest, 2, 10));
  for (const dir of sortGithubEntriesDesc(rootDirs.filter((item) => !["top-videos", "ark-invest"].includes(String(item.name || "")))).slice(0, 14)) {
    sourceTasks.push(collectGithubMp4Files(env, BBG_SHOW_REPO, dir.path, {
      maxFiles: 10,
      nestedDirLimit: 1,
      timeoutMs: GITHUB_API_TIMEOUT_MS,
    }));
  }
  return [
    ...rootFiles,
    ...(await Promise.all(sourceTasks.map((task) => resolveWithin(task, ADMIN_GITHUB_SOURCE_TIMEOUT_MS - 1000, [])))).flat(),
  ];
}

async function latestBbgRenderedClipFiles(env, maxItems = 26) {
  const tree = await resolveWithin(githubRecursiveTree(env, BBG_SHOW_REPO), ADMIN_GITHUB_SOURCE_TIMEOUT_MS - 500, []);
  const treeFiles = (Array.isArray(tree) ? tree : [])
    .filter((item) => item && item.type === "blob" && /^rendered-clips\/.+\.mp4$/i.test(String(item.path || "")))
    .map((item) => ({
      type: "file",
      name: String(item.path || "").split("/").pop(),
      path: item.path,
      size: Number(item.size || 0),
    }));
  const listedFiles = treeFiles.length ? treeFiles : await bbgRenderedClipFilesFromContents(env);
  const seen = new Set();
  const grouped = new Map();
  for (const item of listedFiles || []) {
    if (!isGithubMp4File(item) || !/^rendered-clips\/.+\.mp4$/i.test(item.path || "")) continue;
    const path = String(item.path || "");
    if (seen.has(path)) continue;
    seen.add(path);
    const info = bbgRenderedClipInfo(item.path);
    if (!info.generatedDate) continue;
    const rows = grouped.get(info.source) || [];
    rows.push({ item, info });
    grouped.set(info.source, rows);
  }
  const picked = [];
  for (const [source, rows] of grouped.entries()) {
    rows.sort((a, b) => {
      const score = dateScore(b.info.generatedDate) - dateScore(a.info.generatedDate);
      if (score) return score;
      return String(b.item.path || "").localeCompare(String(a.item.path || ""));
    });
    picked.push(...rows.slice(0, bbgClipTakeLimit(source)));
  }
  const dated = picked
    .sort((a, b) => {
      const score = dateScore(b.info.generatedDate) - dateScore(a.info.generatedDate);
      if (score) return score;
      if (a.info.sourceOrder !== b.info.sourceOrder) return a.info.sourceOrder - b.info.sourceOrder;
      return String(b.item.path || "").localeCompare(String(a.item.path || ""));
    })
    .slice(0, maxItems);
  const files = dated.map(({ item, info }) => {
    const path = String(item.path || "");
    return {
      ...adminGithubFile(
        info.source === "ark-invest" ? "bbg-ark-invest" : "bbg-show",
        info.label,
        {
          name: path.split("/").pop(),
          path,
          size: item.size,
        },
        info.generatedDate,
        renderedClipNote(path, info),
        BBG_SHOW_REPO,
        bbgVideoAccountRecommendation(path, info),
      ),
      _bbg_group_key: bbgVideoShareGroupKey(path, info),
    };
  });
  return applyBbgVideoGroupMajority(files);
}

function kcEntertainmentDateFromPath(path) {
  const clean = String(path || "").replace(/^\/+/, "");
  const match = clean.match(/^outputs\/kc_entertain\/(20\d{2}-\d{2}-\d{2})\//);
  return match ? match[1] : "";
}

function kcEntertainmentNote(path, date) {
  const clean = String(path || "").replace(/^\/+/, "");
  const parts = clean.split("/");
  const folder = parts.length >= 3 ? parts[2] : "";
  const notes = [];
  if (date) notes.push(`生成日期 ${date}`);
  if (folder && folder !== date) notes.push(folder.replace(/[-_]+/g, " "));
  return notes.join(" · ");
}

async function latestKcEntertainmentFiles(env, maxItems = 12) {
  const tree = await resolveWithin(githubRecursiveTree(env, ENTERTAIN_CUT_REPO), ADMIN_GITHUB_SOURCE_TIMEOUT_MS - 500, []);
  const treeVideos = (Array.isArray(tree) ? tree : [])
    .filter((item) => item && item.type === "blob" && /^outputs\/kc_entertain\/20\d{2}-\d{2}-\d{2}\/.+\.mp4$/i.test(String(item.path || "")))
    .sort((a, b) => dateScore(b.path) - dateScore(a.path) || String(a.path || "").localeCompare(String(b.path || "")));
  if (treeVideos.length) {
    return treeVideos.slice(0, maxItems).map((video) => {
      const path = String(video.path || "");
      const date = kcEntertainmentDateFromPath(path);
      return adminGithubFile(
        "kc-entertain",
        "KC 娱乐视频",
        { name: path.split("/").pop(), path, size: video.size },
        date,
        kcEntertainmentNote(path, date),
        ENTERTAIN_CUT_REPO,
        {
          recommended_account: "KC娱乐",
          account_label_confidence: "高",
          account_label_reason: "KC娱乐专属内容",
        },
      );
    });
  }
  let entries = [];
  try {
    entries = await githubContents(env, KC_ENTERTAIN_PREFIX, ENTERTAIN_CUT_REPO);
  } catch (_error) {
    return [];
  }
  const dateDirs = sortGithubDirsDesc(entries)
    .filter((item) => /^20\d{2}-\d{2}-\d{2}$/.test(String(item.name || "")));
  const results = [];
  for (const dateDir of dateDirs.slice(0, 8)) {
    let files = [];
    try {
      files = await githubContents(env, dateDir.path, ENTERTAIN_CUT_REPO);
    } catch (_error) {
      continue;
    }
    const videos = files
      .filter((item) => item && item.type === "file" && /\.mp4$/i.test(item.name || ""))
      .sort((a, b) => String(a.name || "").localeCompare(String(b.name || "")));
    for (const video of videos) {
      const path = String(video.path || "");
      const date = kcEntertainmentDateFromPath(path) || dateDir.name;
      results.push(adminGithubFile(
        "kc-entertain",
        "KC 娱乐视频",
        video,
        date,
        kcEntertainmentNote(path, date),
        ENTERTAIN_CUT_REPO,
        {
          recommended_account: "KC娱乐",
          account_label_confidence: "高",
          account_label_reason: "KC娱乐专属内容",
        },
      ));
      if (results.length >= maxItems) return results;
    }
  }
  return results;
}

function rpt2vidDateFromPath(path) {
  const clean = String(path || "").replace(/^\/+/, "");
  const escapedPrefix = RPT2VID_PDF_KC_PREFIX.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const match = clean.match(new RegExp(`^${escapedPrefix}/(\\d{6}|\\d{8})/`));
  return match ? dateFolderIso(match[1]) : "";
}

function rpt2vidNote(path, date) {
  const fileName = String(path || "").split("/").pop() || "";
  const stem = fileName
    .replace(/\.mp4$/i, "")
    .replace(/_KC(?:桌面|偏见)$/i, "")
    .replace(/[-_]+/g, " ")
    .trim();
  const notes = [];
  if (date) notes.push(`生成日期 ${date}`);
  if (stem) notes.push(stem.slice(0, 120));
  return notes.join(" · ");
}

async function latestRpt2vidPdfKcFiles(env, maxItems = 20) {
  const tree = await resolveWithin(githubRecursiveTree(env, RPT2VID_REPO), ADMIN_GITHUB_SOURCE_TIMEOUT_MS - 500, []);
  const escapedPrefix = RPT2VID_PDF_KC_PREFIX.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const treePattern = new RegExp(`^${escapedPrefix}/(?:\\d{6}|20\\d{6})/.+\\.mp4$`, "i");
  const treeVideos = (Array.isArray(tree) ? tree : [])
    .filter((item) => item && item.type === "blob" && treePattern.test(String(item.path || "")))
    .sort((a, b) => dateScore(b.path) - dateScore(a.path) || String(a.path || "").localeCompare(String(b.path || "")));
  if (treeVideos.length) {
    return treeVideos.slice(0, maxItems).map((video) => {
      const path = String(video.path || "");
      const date = rpt2vidDateFromPath(path);
      return adminGithubFile(
        "rpt2vid-pdf-kc",
        "报告视频",
        { name: path.split("/").pop(), path, size: video.size },
        date,
        rpt2vidNote(path, date),
        RPT2VID_REPO,
        rpt2vidAccountRecommendation(path),
      );
    });
  }
  let entries = [];
  try {
    entries = await githubContents(env, RPT2VID_PDF_KC_PREFIX, RPT2VID_REPO);
  } catch (_error) {
    return [];
  }
  const dateDirs = sortGithubDirsDesc(entries)
    .filter((item) => /^(?:\d{6}|20\d{6})$/.test(String(item.name || "")));
  const results = [];
  for (const dateDir of dateDirs.slice(0, 8)) {
    let files = [];
    try {
      files = await githubContents(env, dateDir.path, RPT2VID_REPO);
    } catch (_error) {
      continue;
    }
    const videos = files
      .filter((item) => item && item.type === "file" && /\.mp4$/i.test(item.name || ""))
      .sort((a, b) => String(a.name || "").localeCompare(String(b.name || "")));
    for (const video of videos) {
      const path = String(video.path || "");
      const date = rpt2vidDateFromPath(path) || dateFolderIso(dateDir.name);
      results.push(adminGithubFile(
        "rpt2vid-pdf-kc",
        "报告视频",
        video,
        date,
        rpt2vidNote(path, date),
        RPT2VID_REPO,
        rpt2vidAccountRecommendation(path),
      ));
      if (results.length >= maxItems) return results;
    }
  }
  return results;
}

async function latestSiteVideoFiles(env, maxItems = 6) {
  const results = [];
  const dateDirs = sortGithubDirsDesc(await githubContents(env, "bilingual_podcast_videos"));
  for (const dateDir of dateDirs.slice(0, 12)) {
    const runDirs = sortGithubDirsDesc(await githubContents(env, dateDir.path))
      .sort((a, b) => Number(b.name || 0) - Number(a.name || 0));
    for (const runDir of runDirs.slice(0, 8)) {
      const reportDirs = sortGithubDirsDesc(await githubContents(env, runDir.path));
      for (const reportDir of reportDirs) {
        const files = await githubContents(env, reportDir.path);
        const video = preferredVideoItem(files);
        if (!video) continue;
        results.push(adminGithubFile("site-video", "站内视频", video, dateDir.name, titleFromGeneratedPath(video.path), githubRepo(env)));
        if (results.length >= maxItems) return results;
      }
    }
  }
  return results;
}

function adminGithubArtifact(artifact) {
  const name = String(artifact.name || "");
  let kind = "artifact";
  let label = "GitHub Artifact";
  if (/bilingual-podcast-videos/i.test(name)) {
    kind = "site-video";
    label = "站内视频 artifact";
  } else if (/market-views-pdf/i.test(name)) {
    kind = "market-views";
    label = "Market Views PDF artifact";
  }
  return {
    type: "artifact",
    kind,
    label,
    id: String(artifact.id || ""),
    name,
    size_bytes: Number(artifact.size_in_bytes || 0),
    date: String(artifact.created_at || "").slice(0, 10),
    note: "artifact zip",
  };
}

async function latestGithubArtifacts(env) {
  try {
    const data = await githubApiJson(env, "/actions/artifacts?per_page=60");
    const artifacts = Array.isArray(data && data.artifacts) ? data.artifacts : [];
    return artifacts
      .filter((artifact) => !artifact.expired && /bilingual-podcast-videos|market-views-pdf/i.test(String(artifact.name || "")))
      .map(adminGithubArtifact);
  } catch (_error) {
    return [];
  }
}

async function latestAdminGithubFiles(env) {
  const [bbg, market, entertainVideos, rpt2vidVideos, siteVideos, artifacts] = await Promise.all([
    resolveWithin(latestBbgRenderedClipFiles(env), ADMIN_GITHUB_SOURCE_TIMEOUT_MS, []),
    resolveWithin(latestMarketViewFiles(env), ADMIN_GITHUB_SOURCE_TIMEOUT_MS, []),
    resolveWithin(latestKcEntertainmentFiles(env), ADMIN_GITHUB_SOURCE_TIMEOUT_MS, []),
    resolveWithin(latestRpt2vidPdfKcFiles(env), ADMIN_GITHUB_SOURCE_TIMEOUT_MS, []),
    resolveWithin(latestSiteVideoFiles(env), ADMIN_GITHUB_SOURCE_TIMEOUT_MS, []),
    resolveWithin(latestGithubArtifacts(env), ADMIN_GITHUB_ARTIFACT_TIMEOUT_MS, []),
  ]);
  const fallback = [];
  if (!market.length) fallback.push(...artifacts.filter((item) => item.kind === "market-views").slice(0, 3));
  if (!siteVideos.length) fallback.push(...artifacts.filter((item) => item.kind === "site-video").slice(0, 3));
  return applyAdminVideoContinuityMajority([...bbg, ...market, ...fallback, ...entertainVideos, ...rpt2vidVideos, ...siteVideos]);
}

async function resolveWithin(promise, timeoutMs, fallbackValue) {
  return Promise.race([
    promise,
    sleep(timeoutMs).then(() => fallbackValue),
  ]).catch(() => fallbackValue);
}

function hasAdminSnapshot(snapshot) {
  return Boolean(
    snapshot &&
    typeof snapshot === "object" &&
    Object.prototype.hasOwnProperty.call(snapshot, "data"),
  );
}

function adminSnapshotStatus(snapshot, freshMs = ADMIN_SNAPSHOT_FRESH_MS) {
  if (!hasAdminSnapshot(snapshot)) {
    return {
      state: "updating",
      has_data: false,
      updated_at: "",
      retry_after_minutes: 30,
    };
  }
  const updatedMs = Date.parse(String(snapshot.updated_at || ""));
  const ageMs = Number.isFinite(updatedMs) ? Math.max(0, Date.now() - updatedMs) : Number.POSITIVE_INFINITY;
  const partial = Boolean(snapshot.partial);
  let state = !partial && ageMs <= freshMs ? "fresh" : "updating";
  if (ageMs > freshMs * 4) state = "degraded";
  return {
    state,
    has_data: true,
    partial,
    updated_at: String(snapshot.updated_at || ""),
    attempted_at: String(snapshot.attempted_at || snapshot.updated_at || ""),
    age_seconds: Number.isFinite(ageMs) ? Math.round(ageMs / 1000) : null,
    retry_after_minutes: 30,
  };
}

async function writeAdminSnapshot(env, key, data, extra = {}) {
  const snapshot = {
    version: ADMIN_SNAPSHOT_VERSION,
    updated_at: new Date().toISOString(),
    data,
    ...extra,
  };
  await r2PutJson(env, key, snapshot);
  return snapshot;
}

async function loadAdminSnapshotModule(env, key, options = {}) {
  let snapshot = await safeR2GetJson(env, key);
  const refresh = options.refresh;
  const freshMs = Number(options.freshMs || ADMIN_SNAPSHOT_FRESH_MS);
  const timeoutMs = Number(options.timeoutMs || ADMIN_GITHUB_FILES_TIMEOUT_MS);
  if (!hasAdminSnapshot(snapshot) && typeof refresh === "function") {
    const refreshPromise = refresh();
    const refreshed = await resolveWithin(refreshPromise, timeoutMs, null);
    if (hasAdminSnapshot(refreshed)) snapshot = refreshed;
    else if (options.ctx && typeof options.ctx.waitUntil === "function") {
      options.ctx.waitUntil(refreshPromise.catch(() => null));
    }
  }
  const status = adminSnapshotStatus(snapshot, freshMs);
  if (status.has_data && status.state !== "fresh" && typeof refresh === "function" && options.ctx && typeof options.ctx.waitUntil === "function") {
    options.ctx.waitUntil(refresh().catch(() => null));
  }
  return {
    data: status.has_data ? snapshot.data : options.fallback,
    status,
    snapshot,
  };
}

function adminFileGroup(file) {
  const path = String(file && file.path || "");
  const kind = String(file && file.kind || "");
  if (/^rendered-clips\/top-videos\//i.test(path)) return "bbg-top";
  if (kind === "bbg-ark-invest" || /^rendered-clips\/ark-invest\//i.test(path)) return "bbg-ark";
  if (kind === "bbg-show") return "bbg-show";
  if (kind === "market-views") return "market-views";
  if (kind === "kc-entertain") return "kc-entertain";
  if (kind === "rpt2vid-pdf-kc") return "report-videos";
  if (kind === "site-video") return "site-videos";
  return kind || String(file && file.type || "other");
}

function adminFileKey(file) {
  return [file && file.type, file && file.repo, file && (file.path || file.id || file.name)].map((part) => String(part || "")).join(":");
}

function opsMirrorVideoFiles(files) {
  const allowedGroups = new Set(["bbg-top", "bbg-show", "bbg-ark", "kc-entertain", "report-videos"]);
  return (Array.isArray(files) ? files : []).filter((file) => {
    const path = String(file && (file.path || file.name) || "");
    return file && file.type === "file" && /\.mp4$/i.test(path) && allowedGroups.has(adminFileGroup(file));
  });
}

async function opsMirrorFingerprint(files) {
  const rows = opsMirrorVideoFiles(files)
    .map((file) => [adminFileKey(file), Number(file.size_bytes || 0), String(file.date || "")].join(":"))
    .sort();
  return rows.length ? sha256Hex(rows.join("\n")) : "";
}

function opsMirrorStateAgeMs(state) {
  const attempted = Date.parse(String(state && state.attempted_at || ""));
  return Number.isFinite(attempted) ? Math.max(0, Date.now() - attempted) : Number.POSITIVE_INFINITY;
}

async function triggerOpsMirrorIfChanged(env, files) {
  const token = cleanEnv(env.GH_DISPATCH_TOKEN);
  const repo = githubRepo(env);
  if (!token || token === "unconfigured" || !repo) return { status: "disabled" };
  const videos = opsMirrorVideoFiles(files);
  const fingerprint = await opsMirrorFingerprint(videos);
  if (!fingerprint) return { status: "empty" };

  const previous = await safeR2GetJson(env, ADMIN_OPS_MIRROR_STATE_KEY);
  const sameFingerprint = String(previous && previous.fingerprint || "") === fingerprint;
  if (sameFingerprint && String(previous && previous.status || "") === "dispatched") {
    return { status: "unchanged", fingerprint, file_count: videos.length };
  }
  if (sameFingerprint && opsMirrorStateAgeMs(previous) < OPS_MIRROR_RETRY_MS) {
    return { status: "cooldown", fingerprint, file_count: videos.length };
  }

  const attemptedAt = new Date().toISOString();
  const pending = {
    version: 1,
    status: "dispatching",
    fingerprint,
    file_count: videos.length,
    attempted_at: attemptedAt,
    dispatched_at: String(previous && previous.dispatched_at || ""),
  };
  await r2PutJson(env, ADMIN_OPS_MIRROR_STATE_KEY, pending);

  try {
    const response = await fetchWithTimeout(`https://api.github.com/repos/${repo}/dispatches`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "kc-desk-notes-worker",
        "X-GitHub-Api-Version": "2022-11-28",
      },
      body: JSON.stringify({
        event_type: OPS_MIRROR_EVENT_TYPE,
        client_payload: {
          fingerprint,
          file_count: videos.length,
          detected_at: attemptedAt,
        },
      }),
    }, GITHUB_API_TIMEOUT_MS);
    if (!response.ok) {
      const detail = await response.text().catch(() => "");
      throw new Error(`GitHub dispatch ${response.status}: ${detail.slice(0, 160)}`);
    }
    const dispatched = {
      ...pending,
      status: "dispatched",
      dispatched_at: new Date().toISOString(),
    };
    await r2PutJson(env, ADMIN_OPS_MIRROR_STATE_KEY, dispatched);
    return dispatched;
  } catch (error) {
    await r2PutJson(env, ADMIN_OPS_MIRROR_STATE_KEY, {
      ...pending,
      status: "failed",
      error: String(error && error.message || "Dispatch failed.").slice(0, 240),
    }).catch(() => null);
    throw error;
  }
}

function groupAdminFiles(files) {
  const grouped = new Map();
  for (const file of Array.isArray(files) ? files : []) {
    const group = adminFileGroup(file);
    const rows = grouped.get(group) || [];
    rows.push(file);
    grouped.set(group, rows);
  }
  return grouped;
}

function mergeAdminFilesWithSnapshot(liveFiles, previousFiles) {
  const live = groupAdminFiles(liveFiles);
  const previous = groupAdminFiles(previousFiles);
  const orderedGroups = [
    "bbg-top",
    "bbg-show",
    "bbg-ark",
    "market-views",
    "kc-entertain",
    "report-videos",
    "site-videos",
  ];
  const groups = [...new Set([...orderedGroups, ...live.keys(), ...previous.keys()])];
  const staleGroups = [];
  const merged = [];
  const seen = new Set();
  for (const group of groups) {
    const current = live.get(group) || [];
    const fallback = previous.get(group) || [];
    const rows = current.length ? current : fallback;
    if (!current.length && fallback.length) staleGroups.push(group);
    for (const file of rows) {
      const key = adminFileKey(file);
      if (!key || seen.has(key)) continue;
      seen.add(key);
      merged.push(file);
    }
  }
  const expectedGroups = ["bbg-top", "bbg-show"];
  for (const group of expectedGroups) {
    if (!live.has(group) && !staleGroups.includes(group)) staleGroups.push(group);
  }
  return {
    files: applyAdminVideoContinuityMajority(merged),
    stale_groups: staleGroups,
  };
}

async function refreshAdminFilesSnapshot(env) {
  const previous = await safeR2GetJson(env, ADMIN_FILES_SNAPSHOT_KEY);
  const previousFiles = hasAdminSnapshot(previous) && Array.isArray(previous.data && previous.data.files)
    ? previous.data.files
    : [];
  const liveFiles = await latestAdminGithubFiles(env);
  const merged = mergeAdminFilesWithSnapshot(liveFiles, previousFiles);
  if (!merged.files.length) throw new Error("No daily files are currently available.");
  if (!liveFiles.length && previousFiles.length) {
    const retained = {
      ...previous,
      attempted_at: new Date().toISOString(),
      partial: true,
    };
    await r2PutJson(env, ADMIN_FILES_SNAPSHOT_KEY, retained);
    return retained;
  }
  const snapshot = await writeAdminSnapshot(env, ADMIN_FILES_SNAPSHOT_KEY, { files: merged.files }, {
    attempted_at: new Date().toISOString(),
    partial: merged.stale_groups.length > 0,
    stale_groups: merged.stale_groups,
  });
  await triggerOpsMirrorIfChanged(env, merged.files).catch(() => null);
  return snapshot;
}

function refreshAdminFilesSnapshotOnce(env) {
  if (!adminFilesRefreshPromise) {
    adminFilesRefreshPromise = refreshAdminFilesSnapshot(env).finally(() => {
      adminFilesRefreshPromise = null;
    });
  }
  return adminFilesRefreshPromise;
}

async function refreshAdminPicksSnapshot(env) {
  const [catalog, searchIndex] = await Promise.all([loadCatalog(env), loadSearchIndex(env)]);
  if (!catalog || !Array.isArray(catalog.items) || !catalog.items.length) {
    throw new Error("Catalog is not ready.");
  }
  return writeAdminSnapshot(env, ADMIN_PICKS_SNAPSHOT_KEY, {
    daily_picks: selectDailyPicks(catalog, 5, searchIndex),
    access_options: accessOptionRowsFromCatalog(catalog),
  });
}

function refreshAdminPicksSnapshotOnce(env) {
  if (!adminPicksRefreshPromise) {
    adminPicksRefreshPromise = refreshAdminPicksSnapshot(env).finally(() => {
      adminPicksRefreshPromise = null;
    });
  }
  return adminPicksRefreshPromise;
}

async function refreshAdminWechatSnapshot(env) {
  return writeAdminSnapshot(env, ADMIN_WECHAT_SNAPSHOT_KEY, await buildWechatDraftSchedule(env));
}

function refreshAdminWechatSnapshotOnce(env) {
  if (!adminWechatRefreshPromise) {
    adminWechatRefreshPromise = refreshAdminWechatSnapshot(env).finally(() => {
      adminWechatRefreshPromise = null;
    });
  }
  return adminWechatRefreshPromise;
}

async function refreshAdminAnalyticsSnapshot(env) {
  return writeAdminSnapshot(env, ADMIN_ANALYTICS_SNAPSHOT_KEY, await buildAnalyticsDashboard(env));
}

function refreshAdminAnalyticsSnapshotOnce(env) {
  if (!adminAnalyticsRefreshPromise) {
    adminAnalyticsRefreshPromise = refreshAdminAnalyticsSnapshot(env).finally(() => {
      adminAnalyticsRefreshPromise = null;
    });
  }
  return adminAnalyticsRefreshPromise;
}

async function refreshAdminUsersSnapshot(env) {
  const [userRows, entitlementRows] = await Promise.all([listSiteUsers(env), listEntitlementRows(env)]);
  if (!Array.isArray(userRows) || !userRows.length) throw new Error("User list is not ready.");
  const entitlementsByEmail = entitlementMap(entitlementRows);
  const accessRows = await Promise.all(userRows.map((user) => findAccessGrant(env, user.email).catch(() => publicAccessGrant(null))));
  const users = userRows.map((user, index) => adminVisibleUser(
    user,
    entitlementsByEmail.get(normalizeEmail(user.email)),
    accessRows[index],
  ));
  return writeAdminSnapshot(env, ADMIN_USERS_SNAPSHOT_KEY, { users });
}

function refreshAdminUsersSnapshotOnce(env) {
  if (!adminUsersRefreshPromise) {
    adminUsersRefreshPromise = refreshAdminUsersSnapshot(env).finally(() => {
      adminUsersRefreshPromise = null;
    });
  }
  return adminUsersRefreshPromise;
}

async function patchAdminUsersSnapshotUser(env, user) {
  if (!user || !user.email) return false;
  const previous = await safeR2GetJson(env, ADMIN_USERS_SNAPSHOT_KEY);
  const hasPreviousUsers = hasAdminSnapshot(previous) && Array.isArray(previous.data && previous.data.users);
  const users = hasPreviousUsers
    ? previous.data.users.slice()
    : [];
  const email = normalizeEmail(user.email);
  const index = users.findIndex((row) => normalizeEmail(row && row.email) === email);
  if (index >= 0) users[index] = user;
  else users.unshift(user);
  await writeAdminSnapshot(env, ADMIN_USERS_SNAPSHOT_KEY, { users }, { partial: !hasPreviousUsers });
  return true;
}

async function refreshAdminDashboardSnapshots(env) {
  const filesResult = await refreshAdminFilesSnapshotOnce(env).catch(() => null);
  await refreshAdminWechatSnapshotOnce(env).catch(() => null);
  await Promise.allSettled([
    refreshAdminPicksSnapshotOnce(env),
    refreshAdminAnalyticsSnapshotOnce(env),
    refreshAdminUsersSnapshotOnce(env),
  ]);
  const filesSnapshot = hasAdminSnapshot(filesResult)
    ? filesResult
    : await safeR2GetJson(env, ADMIN_FILES_SNAPSHOT_KEY);
  const files = hasAdminSnapshot(filesSnapshot) && Array.isArray(filesSnapshot.data && filesSnapshot.data.files)
    ? filesSnapshot.data.files
    : [];
  if (files.length) await warmAdminGithubCache(env, files).catch(() => null);
  return { ok: true, generated_at: new Date().toISOString() };
}

function operatorVisibleAdminFiles(files) {
  return (Array.isArray(files) ? files : []).filter((file) => {
    const kind = String(file && file.kind || "");
    const label = String(file && file.label || "");
    return kind !== "site-video" && !/站内视频/i.test(label);
  });
}

function adminFilesForUser(files, user) {
  return isSuperAccount(user) ? files : operatorVisibleAdminFiles(files);
}

async function handleAccountAdminSummary(request, env, ctx = null) {
  let adminUser;
  try {
    adminUser = await requireOperationsUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
  try {
    const isSuper = isSuperAccount(adminUser);
    const forceRefresh = new URL(request.url).searchParams.get("refresh") === "1";
    if (forceRefresh && ctx && typeof ctx.waitUntil === "function") {
      ctx.waitUntil(refreshAdminDashboardSnapshots(env).catch(() => null));
    }
    const emptyWechatSchedule = {
      today_folder: bjtTodayFolder(),
      date_folder: "",
      date_label: "",
      is_today: false,
      window: "08:00 - 次日 00:30",
      source_dates: [],
      total_batches: 0,
      total_articles: 0,
      batches: [],
    };
    const [filesModule, picksModule, wechatModule, analyticsModule, usersModule] = await Promise.all([
      loadAdminSnapshotModule(env, ADMIN_FILES_SNAPSHOT_KEY, {
        refresh: () => refreshAdminFilesSnapshotOnce(env),
        timeoutMs: ADMIN_GITHUB_FILES_TIMEOUT_MS,
        freshMs: ADMIN_FILES_SNAPSHOT_FRESH_MS,
        fallback: { files: [] },
        ctx,
      }),
      loadAdminSnapshotModule(env, ADMIN_PICKS_SNAPSHOT_KEY, {
        refresh: () => refreshAdminPicksSnapshotOnce(env),
        timeoutMs: Math.max(ADMIN_CATALOG_TIMEOUT_MS * 2, 8000),
        fallback: { daily_picks: [], access_options: null },
        ctx,
      }),
      isSuper ? loadAdminSnapshotModule(env, ADMIN_WECHAT_SNAPSHOT_KEY, {
        refresh: () => refreshAdminWechatSnapshotOnce(env),
        timeoutMs: Math.max(ADMIN_WECHAT_TIMEOUT_MS * 2, 8000),
        fallback: emptyWechatSchedule,
        ctx,
      }) : Promise.resolve({ data: null, status: null }),
      isSuper ? loadAdminSnapshotModule(env, ADMIN_ANALYTICS_SNAPSHOT_KEY, {
        refresh: () => refreshAdminAnalyticsSnapshotOnce(env),
        timeoutMs: Math.max(ANALYTICS_DASHBOARD_TIMEOUT_MS, 10000),
        freshMs: ADMIN_ANALYTICS_SNAPSHOT_FRESH_MS,
        fallback: null,
        ctx,
      }) : Promise.resolve({ data: null, status: null }),
      isSuper ? loadAdminSnapshotModule(env, ADMIN_USERS_SNAPSHOT_KEY, {
        refresh: () => refreshAdminUsersSnapshotOnce(env),
        timeoutMs: 15000,
        fallback: { users: [] },
        ctx,
      }) : Promise.resolve({ data: { users: [] }, status: null }),
    ]);
    const filesData = filesModule.data && typeof filesModule.data === "object" ? filesModule.data : { files: [] };
    const picksData = picksModule.data && typeof picksModule.data === "object" ? picksModule.data : { daily_picks: [], access_options: null };
    const usersData = usersModule.data && typeof usersModule.data === "object" ? usersModule.data : { users: [] };
    const allFiles = Array.isArray(filesData.files) ? filesData.files : [];
    const files = adminFilesForUser(allFiles, adminUser);
    const dailyPicks = Array.isArray(picksData.daily_picks) ? picksData.daily_picks : [];
    const userRows = Array.isArray(usersData.users) ? usersData.users : [];
    return jsonResponse(request, env, 200, {
      user: publicUser(adminUser),
      dashboard_title: isSuper ? "管理后台" : "运营后台",
      can_view_users: isSuper,
      can_view_wechat: isSuper,
      can_view_analytics: isSuper,
      users: isSuper ? userRows : [],
      access_options: isSuper ? picksData.access_options || null : null,
      files,
      daily_picks: dailyPicks,
      wechat_schedule: isSuper ? wechatModule.data || emptyWechatSchedule : null,
      analytics: isSuper ? analyticsModule.data || null : null,
      analytics_error: "",
      module_status: {
        files: forceRefresh ? { ...filesModule.status, state: "updating" } : filesModule.status,
        picks: forceRefresh ? { ...picksModule.status, state: "updating" } : picksModule.status,
        wechat: isSuper ? (forceRefresh ? { ...wechatModule.status, state: "updating" } : wechatModule.status) : null,
        analytics: isSuper ? (forceRefresh ? { ...analyticsModule.status, state: "updating" } : analyticsModule.status) : null,
        users: isSuper ? (forceRefresh ? { ...usersModule.status, state: "updating" } : usersModule.status) : null,
      },
      repo: githubRepo(env),
      ref: githubRef(env),
      generated_at: new Date().toISOString(),
    });
  } catch (error) {
    return jsonResponse(request, env, 503, {
      detail: "后台数据正在更新，请稍后重试。",
      code: "dashboard_updating",
    });
  }
}

async function handleAccountAdminUserAccess(request, env) {
  let adminUser;
  try {
    adminUser = await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const email = normalizeEmail(payload.email);
  if (!email) return jsonResponse(request, env, 400, { detail: "Email is required." });

  try {
    const user = await findSiteUserByEmail(env, email);
    if (!user) return jsonResponse(request, env, 404, { detail: "User not found." });
    if (isPrivilegedAccount(user)) {
      return jsonResponse(request, env, 400, { detail: "系统角色账号不能写入普通用户授权。" });
    }
    const saveResult = await saveAccessGrant(env, email, payload, adminUser);
    const access = saveResult.access;
    const verifiedAccess = await findAccessGrant(env, email);
    if (!accessGrantMatchesExpected(verifiedAccess, access)) {
      throw new Error("Access save verification failed. Please retry.");
    }
    const visibleUser = adminVisibleUser(user, await findEntitlement(env, email).catch(() => null), access);
    if (visibleUser) await patchAdminUsersSnapshotUser(env, visibleUser).catch(() => false);
    await persistAnalyticsEvent(request, env, {
      type: "admin_user_update",
      path: "/account-admin/user-access",
      data: {
        target: email,
        action: `access_${access.access_mode || "none"}`,
        status: "success",
      },
    }, adminUser).catch(() => null);
    return jsonResponse(request, env, 200, {
      ok: true,
      verified: true,
      backup_count: 3,
      user: visibleUser,
      access,
    });
  } catch (error) {
    if (error && error.code === "ACCESS_CONFLICT") {
      return jsonResponse(request, env, 409, {
        detail: error.message || "权限记录已变化，请刷新后重试。",
      });
    }
    const status = accessErrorStatus(error);
    return jsonResponse(request, env, status === 503 ? 503 : 400, {
      detail: status === 503 ? "权限保存或核验失败，请稍后重试。" : error.message || "Could not save access.",
    });
  }
}

async function handleAccountAdminUserCreate(request, env) {
  let adminUser;
  try {
    adminUser = await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const username = normalizeUsername(payload.username);
  const email = normalizeEmail(payload.email);
  const password = String(payload.password || "");
  if (!USERNAME_PATTERN.test(username)) {
    return jsonResponse(request, env, 400, { detail: "用户名需为 3-32 位小写字母、数字、点、短横线或下划线。" });
  }
  if (!email) {
    return jsonResponse(request, env, 400, { detail: "请输入有效邮箱。" });
  }
  if (password.length < 4 || password.length > 128) {
    return jsonResponse(request, env, 400, { detail: "密码需为 4-128 位。" });
  }
  if (isReservedPrivilegedIdentity(username, email)) {
    return jsonResponse(request, env, 403, { detail: "该用户名或邮箱为系统保留身份，不能通过通用入口创建。" });
  }

  try {
    if (await findSiteUserByUsername(env, username)) {
      return jsonResponse(request, env, 409, { detail: "用户名已被注册。" });
    }
    if (await findSiteUserByEmail(env, email)) {
      return jsonResponse(request, env, 409, { detail: "邮箱已被注册。" });
    }
    const now = new Date().toISOString();
    const passwordFields = await hashUserPassword(env, password);
    const user = await createSiteUser(env, {
      username,
      email,
      email_is_generated: false,
      ...passwordFields,
      created_at: now,
      updated_at: now,
    });
    const merged = await mergeSiteUserAdminState(env, user);
    const visibleUser = adminVisibleUser(merged, await findEntitlement(env, email).catch(() => null), await findAccessGrant(env, email).catch(() => publicAccessGrant(null)));
    await patchAdminUsersSnapshotUser(env, visibleUser).catch(() => false);
    await persistAnalyticsEvent(request, env, {
      type: "admin_user_update",
      path: "/account-admin/user",
      data: {
        target: email,
        action: "create",
        status: "success",
      },
    }, adminUser).catch(() => null);
    return jsonResponse(request, env, 201, {
      ok: true,
      user: visibleUser,
    });
  } catch (error) {
    const text = String(error && error.message || "");
    if (/duplicate|409|unique/i.test(text)) {
      return jsonResponse(request, env, 409, { detail: "用户名或邮箱已被注册。" });
    }
    return jsonResponse(request, env, 503, { detail: "用户创建或权限核验失败，请稍后重试。" });
  }
}

async function handleAccountAdminUserStatus(request, env) {
  let adminUser;
  try {
    adminUser = await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const email = normalizeEmail(payload.email);
  if (!email) return jsonResponse(request, env, 400, { detail: "Email is required." });

  try {
    const user = await findSiteUserByEmail(env, email);
    if (!user) return jsonResponse(request, env, 404, { detail: "User not found." });
    if (isSuperAccount(user)) return jsonResponse(request, env, 400, { detail: "管理员账号不能禁用。" });
    const state = await saveUserAdminState(env, user, { disabled: Boolean(payload.disabled) }, adminUser);
    const merged = await mergeSiteUserAdminState(env, { ...user, ...state });
    const visibleUser = adminVisibleUser(merged, await findEntitlement(env, email).catch(() => null), await findAccessGrant(env, email).catch(() => publicAccessGrant(null)));
    await patchAdminUsersSnapshotUser(env, visibleUser).catch(() => false);
    await persistAnalyticsEvent(request, env, {
      type: "admin_user_update",
      path: "/account-admin/user-status",
      data: {
        target: email,
        action: payload.disabled ? "disable" : "enable",
        status: "success",
      },
    }, adminUser).catch(() => null);
    return jsonResponse(request, env, 200, {
      ok: true,
      user: visibleUser,
    });
  } catch (error) {
    return jsonResponse(request, env, 503, { detail: "用户状态保存或核验失败，请稍后重试。" });
  }
}

async function handleAccountAdminReportPdf(request, env) {
  try {
    await requireOperationsUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }

  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { detail: "Report id is invalid." });
  }
  if (!env.REPORT_BUCKET) {
    return jsonResponse(request, env, 503, { detail: "Report storage is unavailable." });
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { detail: "Catalog is unavailable." });
  }
  const report = findReport(catalog, id);
  if (!report) return jsonResponse(request, env, 404, { detail: "Report not found." });
  if (report.available === false) {
    return jsonResponse(request, env, 404, { detail: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.` });
  }

  const object = await env.REPORT_BUCKET.get(objectKeyForReport(env, id));
  if (!object) return jsonResponse(request, env, 404, { detail: "Report PDF was not found in storage." });
  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": "application/pdf",
    "Content-Disposition": contentDisposition(report.filename || `${id}.pdf`),
    "Content-Length": String(object.size || ""),
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
  };
  return new Response(object.body, { headers });
}

function githubFileRepo(env, file) {
  return normalizeGithubRepoParam(env, file && file.repo || "");
}

function fileDateScoreFromPath(path) {
  return dateScore(path);
}

function retentionCutoffDateScore(now = Date.now()) {
  return Number(new Date(now - GITHUB_CACHE_RETENTION_MS).toISOString().slice(0, 10).replace(/-/g, ""));
}

function normalizeGithubRepoParam(env, value) {
  const repo = String(value || githubRepo(env)).trim();
  if (repo === githubRepo(env) || repo === DEFAULT_GITHUB_REPO) return githubRepo(env);
  if (repo === BBG_SHOW_REPO) return BBG_SHOW_REPO;
  if (repo === ENTERTAIN_CUT_REPO) return ENTERTAIN_CUT_REPO;
  if (repo === RPT2VID_REPO) return RPT2VID_REPO;
  return "";
}

function isAllowedAdminGithubFile(env, repo, path) {
  const clean = String(path || "").replace(/^\/+/, "");
  if (clean.includes("..")) return false;
  if (repo === BBG_SHOW_REPO) return /^rendered-clips\/.+\.mp4$/i.test(clean);
  if (repo === ENTERTAIN_CUT_REPO) return /^outputs\/kc_entertain\/20\d{2}-\d{2}-\d{2}\/.+\.mp4$/i.test(clean);
  if (repo === RPT2VID_REPO) return /^videos\/pdf_kc\/(?:\d{6}|20\d{6})\/[^/]+\.mp4$/i.test(clean);
  if (/^bilingual_podcast_videos\/.+\.mp4$/i.test(clean)) return true;
  if (/^market_view_summaries\/.+\.pdf$/i.test(clean)) return true;
  return false;
}

function operatorBlockedGithubFile(path) {
  const clean = String(path || "").replace(/^\/+/, "");
  return /^bilingual_podcast_videos\/.+\.mp4$/i.test(clean);
}

function contentTypeForGithubPath(path) {
  if (/\.mp4$/i.test(path)) return "video/mp4";
  if (/\.pdf$/i.test(path)) return "application/pdf";
  return "application/octet-stream";
}

async function githubCacheKey(repo, ref, path) {
  const digest = await sha256Hex(`github-file:${repo}:${ref}:${path}`);
  const filename = String(path || "").split("/").pop() || "download";
  return `${GITHUB_CACHE_PREFIX}/${digest}/${filename}`;
}

function githubArtifactCacheKey(id) {
  return `${GITHUB_CACHE_PREFIX}/artifacts/${encodeURIComponent(String(id || ""))}.zip`;
}

async function githubCacheExists(env, cacheKey) {
  if (!env.REPORT_BUCKET) return false;
  try {
    if (typeof env.REPORT_BUCKET.head === "function") {
      return Boolean(await env.REPORT_BUCKET.head(cacheKey));
    }
    return Boolean(await env.REPORT_BUCKET.get(cacheKey));
  } catch (_error) {
    return false;
  }
}

async function cacheGithubFile(env, file) {
  if (!env.REPORT_BUCKET || !file || file.type !== "file") return { ok: false, skipped: true };
  const repo = githubFileRepo(env, file);
  const path = String(file.path || "").replace(/^\/+/, "");
  if (!repo || !isAllowedAdminGithubFile(env, repo, path)) return { ok: false, skipped: true };
  const ref = githubRef(env, repo);
  const cacheKey = await githubCacheKey(repo, ref, path);
  if (await githubCacheExists(env, cacheKey)) return { ok: true, cached: true, key: cacheKey };

  const encodedPath = encodeGithubPath(path);
  const rawUrl = `https://raw.githubusercontent.com/${repo}/${encodeURIComponent(ref)}/${encodedPath}`;
  let response = await fetch(rawUrl, {
    headers: githubHeaders(env, { "Accept": "*/*" }, repo),
    redirect: "follow",
  });
  if (response.status === 404 && githubToken(env, repo)) {
    const metadata = await githubApiJson(env, `/contents/${encodedPath}?ref=${encodeURIComponent(ref)}`, {}, repo);
    const downloadUrl = String(metadata && metadata.download_url || "");
    if (downloadUrl) {
      response = await fetch(downloadUrl, {
        headers: githubHeaders(env, { "Accept": "*/*" }, repo),
        redirect: "follow",
      });
    }
  }
  if (!response.ok || !response.body) return { ok: false, status: response.status };

  await env.REPORT_BUCKET.put(cacheKey, response.body, {
    httpMetadata: {
      contentType: response.headers.get("Content-Type") || contentTypeForGithubPath(path),
      contentDisposition: contentDisposition(path.split("/").pop() || "download"),
    },
    customMetadata: {
      repo,
      ref,
      path: path.slice(0, 900),
      cached_at: new Date().toISOString(),
      file_date: String(file.date || renderedClipDate(path) || "").slice(0, 40),
    },
  });
  return { ok: true, cached: false, key: cacheKey };
}

async function cacheGithubArtifact(env, file) {
  if (!env.REPORT_BUCKET || !file || file.type !== "artifact") return { ok: false, skipped: true };
  const id = String(file.id || "").trim();
  if (!/^\d+$/.test(id)) return { ok: false, skipped: true };
  const cacheKey = githubArtifactCacheKey(id);
  if (await githubCacheExists(env, cacheKey)) return { ok: true, cached: true, key: cacheKey };
  const response = await githubApiFetch(env, `/actions/artifacts/${encodeURIComponent(id)}/zip`, {
    headers: { "Accept": "application/vnd.github+json" },
    redirect: "follow",
  });
  if (!response.ok || !response.body) return { ok: false, status: response.status };
  const filename = /\.zip$/i.test(String(file.name || "")) ? String(file.name || "") : `${file.name || `github-artifact-${id}`}.zip`;
  await env.REPORT_BUCKET.put(cacheKey, response.body, {
    httpMetadata: {
      contentType: "application/zip",
      contentDisposition: contentDisposition(filename),
    },
    customMetadata: {
      artifact_id: id,
      path: filename.slice(0, 900),
      cached_at: new Date().toISOString(),
      file_date: String(file.date || "").slice(0, 40),
    },
  });
  return { ok: true, cached: false, key: cacheKey };
}

async function cacheAdminGithubFilesWithConcurrency(env, files, concurrency = 4) {
  const results = [];
  let cursor = 0;
  async function worker() {
    while (cursor < files.length) {
      const index = cursor;
      cursor += 1;
      const file = files[index];
      try {
        results[index] = file.type === "artifact" ? await cacheGithubArtifact(env, file) : await cacheGithubFile(env, file);
      } catch (error) {
        results[index] = { ok: false, error: String(error && error.message || error || "cache failed").slice(0, 200) };
      }
    }
  }
  await Promise.all(Array.from({ length: Math.min(concurrency, files.length) }, () => worker()));
  return results.filter(Boolean);
}

function adminGithubWarmPriority(file) {
  if (!file || file.type === "artifact") return 4;
  const name = String(file.name || file.path || "");
  if (/\.mp4$/i.test(name)) return 0;
  if (/\.pdf$/i.test(name)) return 1;
  if (/\.zip$/i.test(name)) return 2;
  return 3;
}

function sortAdminGithubWarmTargets(files) {
  return [...(files || [])].sort((a, b) => {
    const priority = adminGithubWarmPriority(a) - adminGithubWarmPriority(b);
    if (priority) return priority;
    const date = dateScore(b.date || b.path || b.name) - dateScore(a.date || a.path || a.name);
    if (date) return date;
    return Number(b.size_bytes || 0) - Number(a.size_bytes || 0);
  });
}

async function pruneGithubCache(env, now = Date.now()) {
  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") return { deleted: 0 };
  const cutoffTime = now - GITHUB_CACHE_RETENTION_MS;
  const cutoffDate = retentionCutoffDateScore(now);
  let cursor = undefined;
  let deleted = 0;
  do {
    const listed = await env.REPORT_BUCKET.list({
      prefix: `${GITHUB_CACHE_PREFIX}/`,
      limit: 1000,
      cursor,
      include: ["customMetadata"],
    });
    const objects = Array.isArray(listed && listed.objects) ? listed.objects : [];
    for (const object of objects) {
      const metadata = object.customMetadata || {};
      const pathScore = dateScore(metadata.file_date || "") || fileDateScoreFromPath(metadata.path || object.key || "");
      const cachedAt = Date.parse(metadata.cached_at || object.uploaded || "");
      const tooOldByFileDate = pathScore && pathScore < cutoffDate;
      const tooOldByCacheDate = Number.isFinite(cachedAt) && cachedAt < cutoffTime;
      if (tooOldByFileDate || tooOldByCacheDate) {
        try {
          await env.REPORT_BUCKET.delete(object.key);
          deleted += 1;
        } catch (_error) {
          // Best-effort cleanup.
        }
      }
    }
    cursor = listed && listed.truncated ? listed.cursor : undefined;
  } while (cursor);
  return { deleted };
}

async function warmAdminGithubCache(env, files = null) {
  const targetFiles = Array.isArray(files) ? files : await latestAdminGithubFiles(env);
  const warmTargets = sortAdminGithubWarmTargets(targetFiles.filter((item) => item && (item.type === "file" || item.type === "artifact"))).slice(0, 96);
  const warmed = await cacheAdminGithubFilesWithConcurrency(env, warmTargets, 4);
  const cleanup = await pruneGithubCache(env).catch((error) => ({ deleted: 0, error: String(error && error.message || error || "") }));
  return {
    warmed,
    cleanup,
    generated_at: new Date().toISOString(),
  };
}

async function prepareAdminGithubFileCache(request, env) {
  let adminUser;
  try {
    adminUser = await requireOperationsUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
  const url = new URL(request.url);
  const kind = String(url.searchParams.get("kind") || "file").trim();
  if (kind === "artifact") {
    const id = String(url.searchParams.get("id") || "").trim();
    if (!/^\d+$/.test(id)) return jsonResponse(request, env, 400, { detail: "Artifact id is invalid." });
    if (!isSuperAccount(adminUser)) {
      try {
        const artifact = await githubApiJson(env, `/actions/artifacts/${encodeURIComponent(id)}`);
        if (!/market-views-pdf/i.test(String(artifact && artifact.name || ""))) {
          return jsonResponse(request, env, 403, { detail: "Artifact is not allowed for this account." });
        }
      } catch (_error) {
        return jsonResponse(request, env, 403, { detail: "Artifact is not allowed for this account." });
      }
    }
    const result = await cacheGithubArtifact(env, { type: "artifact", id, name: url.searchParams.get("name") || "" });
    return jsonResponse(request, env, result.ok ? 200 : 502, result.ok
      ? { ok: true, cached: Boolean(result.cached), key: result.key || "" }
      : { ok: false, detail: "文件缓存准备失败，请稍后重试。" });
  }

  const path = String(url.searchParams.get("path") || "").replace(/^\/+/, "");
  const repo = normalizeGithubRepoParam(env, url.searchParams.get("repo") || "");
  if (!repo || !isAllowedAdminGithubFile(env, repo, path)) {
    return jsonResponse(request, env, 400, { detail: "File path is not allowed." });
  }
  if (!isSuperAccount(adminUser) && operatorBlockedGithubFile(path)) {
    return jsonResponse(request, env, 403, { detail: "File path is not allowed for this account." });
  }
  const result = await cacheGithubFile(env, {
    type: "file",
    path,
    repo,
    name: path.split("/").pop() || "download",
    date: renderedClipDate(path) || kcEntertainmentDateFromPath(path) || rpt2vidDateFromPath(path) || "",
  });
  return jsonResponse(request, env, result.ok ? 200 : 502, result.ok
    ? { ok: true, cached: Boolean(result.cached), key: result.key || "" }
    : { ok: false, detail: "文件缓存准备失败，请稍后重试。" });
}

function parseRangeHeader(rangeHeader, size) {
  const match = String(rangeHeader || "").match(/^bytes=(\d*)-(\d*)$/i);
  if (!match || !Number.isFinite(size) || size <= 0) return null;
  let startText = match[1];
  let endText = match[2];
  let start;
  let end;
  if (!startText && !endText) return null;
  if (!startText) {
    const suffix = Number(endText);
    if (!Number.isFinite(suffix) || suffix <= 0) return null;
    start = Math.max(0, size - suffix);
    end = size - 1;
  } else {
    start = Number(startText);
    end = endText ? Number(endText) : size - 1;
    if (!Number.isFinite(start) || !Number.isFinite(end)) return null;
  }
  if (start < 0 || start >= size || end < start) return null;
  end = Math.min(end, size - 1);
  return {
    offset: start,
    length: end - start + 1,
    start,
    end,
    size,
  };
}

function rangeNotSatisfiableResponse(request, env, size) {
  return new Response(null, {
    status: 416,
    headers: {
      ...corsHeaders(request, env),
      "Content-Range": `bytes */${size || 0}`,
      "Accept-Ranges": "bytes",
      "Cache-Control": "no-store, private",
    },
  });
}

function cachedGithubResponse(request, env, object, path, options = {}) {
  const status = options.status || 200;
  const range = options.range || null;
  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": object.httpMetadata && object.httpMetadata.contentType || contentTypeForGithubPath(path),
    "Content-Disposition": contentDisposition(path.split("/").pop() || "download"),
    "Content-Length": String(range ? range.length : (object.size || "")),
    "Accept-Ranges": "bytes",
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
    "X-KCDesk-Cache": "R2",
  };
  if (range) headers["Content-Range"] = `bytes ${range.start}-${range.end}/${range.size}`;
  return new Response(object.body, { status, headers });
}

async function fetchGithubRawFile(env, path, request, repo = githubRepo(env), ctx = null) {
  const ref = githubRef(env, repo);
  const encodedPath = encodeGithubPath(path);
  const cacheKey = await githubCacheKey(repo, ref, path);
  const range = request.headers.get("Range") || request.headers.get("range") || "";
  if (env.REPORT_BUCKET) {
    try {
      if (range) {
        const head = typeof env.REPORT_BUCKET.head === "function" ? await env.REPORT_BUCKET.head(cacheKey) : null;
        if (head) {
          const parsed = parseRangeHeader(range, Number(head.size || 0));
          if (!parsed) return rangeNotSatisfiableResponse(request, env, Number(head.size || 0));
          const cachedRange = await env.REPORT_BUCKET.get(cacheKey, {
            range: {
              offset: parsed.offset,
              length: parsed.length,
            },
          });
          if (cachedRange) return cachedGithubResponse(request, env, cachedRange, path, { status: 206, range: parsed });
        }
      } else {
        const cached = await env.REPORT_BUCKET.get(cacheKey);
        if (cached) return cachedGithubResponse(request, env, cached, path);
      }
    } catch (_error) {
      // Fall through to GitHub.
    }
  }

  const rawUrl = `https://raw.githubusercontent.com/${repo}/${encodeURIComponent(ref)}/${encodedPath}`;
  const headers = githubHeaders(env, { "Accept": "*/*" }, repo);
  if (range) headers.Range = range;
  let response = await fetch(rawUrl, { headers, redirect: "follow" });
  if (response.status === 404 && githubToken(env, repo)) {
    const metadata = await githubApiJson(env, `/contents/${encodedPath}?ref=${encodeURIComponent(ref)}`, {}, repo);
    const downloadUrl = String(metadata && metadata.download_url || "");
    if (downloadUrl) response = await fetch(downloadUrl, { headers, redirect: "follow" });
  }

  if (!range && response.ok && response.body && env.REPORT_BUCKET && ctx && typeof ctx.waitUntil === "function") {
    const [clientBody, cacheBody] = response.body.tee();
    const contentType = response.headers.get("Content-Type") || contentTypeForGithubPath(path);
    ctx.waitUntil(env.REPORT_BUCKET.put(cacheKey, cacheBody, {
      httpMetadata: {
        contentType,
        contentDisposition: contentDisposition(path.split("/").pop() || "download"),
      },
      customMetadata: {
        repo,
        ref,
        path: path.slice(0, 900),
        cached_at: new Date().toISOString(),
        file_date: String(renderedClipDate(path) || kcEntertainmentDateFromPath(path) || rpt2vidDateFromPath(path) || "").slice(0, 40),
      },
    }).catch(() => null));
    return new Response(clientBody, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers,
    });
  }
  return response;
}

async function handleAccountAdminGithubFile(request, env, ctx = null) {
  let adminUser;
  try {
    adminUser = await requireOperationsUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
  const url = new URL(request.url);
  const path = String(url.searchParams.get("path") || "").replace(/^\/+/, "");
  const repo = normalizeGithubRepoParam(env, url.searchParams.get("repo") || "");
  if (!repo || !isAllowedAdminGithubFile(env, repo, path)) {
    return jsonResponse(request, env, 400, { detail: "File path is not allowed." });
  }
  if (!isSuperAccount(adminUser) && operatorBlockedGithubFile(path)) {
    return jsonResponse(request, env, 403, { detail: "File path is not allowed for this account." });
  }
  let upstream;
  try {
    upstream = await fetchGithubRawFile(env, path, request, repo, ctx);
  } catch (_error) {
    return jsonResponse(request, env, 502, { detail: "GitHub file download is unavailable." });
  }
  if (!upstream.ok && upstream.status !== 206) {
    return jsonResponse(request, env, upstream.status === 404 ? 404 : 502, { detail: "GitHub file was not found." });
  }

  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": upstream.headers.get("Content-Type") || contentTypeForGithubPath(path),
    "Content-Disposition": contentDisposition(path.split("/").pop() || "download"),
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
  };
  for (const name of ["Content-Length", "Content-Range", "Accept-Ranges"]) {
    const value = upstream.headers.get(name);
    if (value) headers[name] = value;
  }
  return new Response(upstream.body, {
    status: upstream.status,
    headers,
  });
}

async function handleAccountAdminGithubArtifact(request, env, ctx = null) {
  let adminUser;
  try {
    adminUser = await requireOperationsUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!/^\d+$/.test(id)) return jsonResponse(request, env, 400, { detail: "Artifact id is invalid." });
  let artifactName = `github-artifact-${id}.zip`;
  if (!isSuperAccount(adminUser)) {
    try {
      const artifact = await githubApiJson(env, `/actions/artifacts/${encodeURIComponent(id)}`);
      const name = String(artifact && artifact.name || "");
      if (!/market-views-pdf/i.test(name)) {
        return jsonResponse(request, env, 403, { detail: "Artifact is not allowed for this account." });
      }
      if (name) artifactName = /\.zip$/i.test(name) ? name : `${name}.zip`;
    } catch (_error) {
      return jsonResponse(request, env, 403, { detail: "Artifact is not allowed for this account." });
    }
  }

  const cacheKey = githubArtifactCacheKey(id);
  const range = request.headers.get("Range") || request.headers.get("range") || "";
  if (env.REPORT_BUCKET) {
    try {
      if (range) {
        const head = typeof env.REPORT_BUCKET.head === "function" ? await env.REPORT_BUCKET.head(cacheKey) : null;
        if (head) {
          const parsed = parseRangeHeader(range, Number(head.size || 0));
          if (!parsed) return rangeNotSatisfiableResponse(request, env, Number(head.size || 0));
          const cachedRange = await env.REPORT_BUCKET.get(cacheKey, {
            range: {
              offset: parsed.offset,
              length: parsed.length,
            },
          });
          if (cachedRange) return cachedGithubResponse(request, env, cachedRange, artifactName, { status: 206, range: parsed });
        }
      } else {
        const cached = await env.REPORT_BUCKET.get(cacheKey);
        if (cached) return cachedGithubResponse(request, env, cached, artifactName);
      }
    } catch (_error) {
      // Fall through to GitHub.
    }
  }

  let upstream;
  try {
    upstream = await githubApiFetch(env, `/actions/artifacts/${encodeURIComponent(id)}/zip`, {
      headers: { "Accept": "application/vnd.github+json" },
      redirect: "follow",
    });
  } catch (_error) {
    return jsonResponse(request, env, 502, { detail: "GitHub artifact download is unavailable." });
  }
  let body = upstream.body;
  if (body && env.REPORT_BUCKET) {
    const [clientBody, cacheBody] = body.tee();
    body = clientBody;
    const cachePromise = env.REPORT_BUCKET.put(cacheKey, cacheBody, {
      httpMetadata: {
        contentType: "application/zip",
        contentDisposition: contentDisposition(artifactName),
      },
      customMetadata: {
        artifact_id: id,
        path: artifactName.slice(0, 900),
        cached_at: new Date().toISOString(),
      },
    }).catch(() => null);
    if (ctx && typeof ctx.waitUntil === "function") ctx.waitUntil(cachePromise);
    else await cachePromise;
  }
  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": "application/zip",
    "Content-Disposition": contentDisposition(artifactName),
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
    "Accept-Ranges": "bytes",
  };
  const length = upstream.headers.get("Content-Length");
  if (length) headers["Content-Length"] = length;
  return new Response(body, {
    headers,
  });
}

// ---------------------------------------------------------------------------
// External report integration
// ---------------------------------------------------------------------------

function externalHeaders() {
  return {
    "User-Agent": EXTERNAL_UA,
    "Referer": `${EXTERNAL_SITE}/`,
    "Accept": "application/json",
  };
}

function externalObjectKey(id) {
  return `${EXTERNAL_R2_PREFIX}/${id}.pdf`;
}

function externalStatusKey(id) {
  return `${EXTERNAL_STATUS_PREFIX}/${id}.json`;
}

function isExternalId(value) {
  return /^[0-9]{6,25}$/.test(String(value || "").trim());
}

async function externalStoredStatus(env, id) {
  if (!env.REPORT_BUCKET) return null;
  try {
    const object = await env.REPORT_BUCKET.get(externalStatusKey(id));
    if (!object) return null;
    const data = JSON.parse(await object.text());
    return data && typeof data === "object" ? data : null;
  } catch (_error) {
    return null;
  }
}

async function externalPutStatus(env, id, status, message = "") {
  if (!env.REPORT_BUCKET) return;
  try {
    await env.REPORT_BUCKET.put(externalStatusKey(id), JSON.stringify({
      id,
      status,
      message: String(message || "").slice(0, 500),
      updated_at: new Date().toISOString(),
    }), {
      httpMetadata: {
        contentType: "application/json; charset=utf-8",
        cacheControl: "no-store",
      },
    });
  } catch (_error) {
    // Status files are best-effort; the PDF path remains the source of truth.
  }
}

function externalStatusAgeMs(stored) {
  const updated = Date.parse(String(stored && stored.updated_at || ""));
  if (!Number.isFinite(updated)) return Number.POSITIVE_INFINITY;
  return Date.now() - updated;
}

function externalStatusIsActive(stored) {
  const status = String(stored && stored.status || "");
  return ["queued", "running"].includes(status) && externalStatusAgeMs(stored) < 30 * 60 * 1000;
}

function externalStatusIsRecentFailure(stored) {
  return String(stored && stored.status || "") === "failed" && externalStatusAgeMs(stored) < 10 * 60 * 1000;
}

function externalPendingResponse(request, env, stored = null) {
  return jsonResponse(request, env, 202, {
    status: stored && stored.status ? String(stored.status) : "pending",
    wait_seconds: 480,
    updated_at: stored && stored.updated_at ? String(stored.updated_at) : "",
  });
}

function externalIsoDate(publishAt) {
  const ms = Number(publishAt || 0);
  if (!ms) return "";
  try {
    return new Date(ms).toISOString().slice(0, 10);
  } catch (_error) {
    return "";
  }
}

// Map a raw upstream report record to the slim shape the frontend renders.
function slimExternalItem(item) {
  const title = String(item.title || item.title_cn || "").trim();
  const summary = String(item.summary || "").replace(/\s+/g, " ").trim();
  return {
    id: String(item.report_id || ""),
    title: title || "Untitled report",
    title_cn: String(item.title_cn || "").trim(),
    institution: String(item.institution_name || item.channel_name || "").trim(),
    date: externalIsoDate(item.publish_at),
    file_type: String(item.file_type || "").trim(),
    summary: summary.length > 220 ? `${summary.slice(0, 220)}…` : summary,
  };
}

function slimExternalDetailItem(main, id) {
  const item = slimExternalItem({
    ...main,
    report_id: id || main.report_id || main.id,
  });
  item.source = "external";
  item.size_bytes = Number(main.size_bytes || main.file_size || main.file_size_bytes || 0) || 0;
  item.page_count = Number(main.document_total_page || main.page_count || main.pages || 0) || 0;
  return item;
}

async function externalDetailItem(id) {
  try {
    const resp = await fetchWithTimeout(`${EXTERNAL_API}/reports/${id}`, { headers: externalHeaders() });
    if (!resp.ok) return null;
    const data = await resp.json();
    const main = data && data.main && typeof data.main === "object" ? data.main : {};
    return {
      item: slimExternalDetailItem(main, id),
      pdf_url: String(main.url_pdf || "").trim(),
    };
  } catch (_error) {
    return null;
  }
}

async function handleExternalItem(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!isExternalId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const detail = await externalDetailItem(id);
  if (!detail || !detail.item || !detail.item.id) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }
  return jsonResponse(request, env, 200, { item: detail.item });
}

async function handleExternalSearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  if (!query) {
    return jsonResponse(request, env, 200, { items: [], page: 1, total_page: 0 });
  }

  return handleCachedSearch(request, env, "external", query, page, {
    items: [],
    page,
    total_page: 0,
  }, async () => {
    const target = new URL(`${EXTERNAL_API}/reports`);
    target.searchParams.set("query", query);
    target.searchParams.set("page_num", String(page));
    target.searchParams.set("page_size", String(EXTERNAL_SEARCH_PAGE_SIZE));
    const upstream = await fetchWithTimeout(target.toString(), { headers: externalHeaders() });
    if (!upstream.ok) {
      throw new Error(`Search unavailable (${upstream.status}).`);
    }
    const data = await upstream.json();
    const items = Array.isArray(data.items) ? data.items.map(slimExternalItem).filter((it) => it.id) : [];
    return {
      items,
      page: Number(data.page_num || page),
      total_page: Number(data.total_page || 0),
    };
  }, (_error) => searchMirrorFallback(env, "external", query, page, EXTERNAL_SEARCH_PAGE_SIZE, (result) => ({
    items: result.items,
    page,
    total_page: Math.ceil(result.total / EXTERNAL_SEARCH_PAGE_SIZE),
    total_count: result.total,
    mirror_generated_at: result.generated_at,
    mirror_stale: result.mirror_stale,
  })), { skipFreshCache: true });
}

// Fetch the upstream detail and, if the report is directly readable, return its
// presigned PDF url. Returns "" when the PDF is gated (needs a browser grab).
async function externalDirectPdfUrl(id) {
  const detail = await externalDetailItem(id);
  const item = detail && detail.item ? detail.item : {};
  return {
    url: detail ? String(detail.pdf_url || "").trim() : "",
    title: String(item.title || item.title_cn || "").trim(),
  };
}

function bytesToBinaryString(bytes) {
  let out = "";
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) {
    out += String.fromCharCode(...bytes.subarray(i, i + chunk));
  }
  return out;
}

function binaryStringToBytes(text) {
  const bytes = new Uint8Array(text.length);
  for (let i = 0; i < text.length; i += 1) bytes[i] = text.charCodeAt(i) & 0xff;
  return bytes;
}

function sanitizePdfExternalLinksBytes(bytes) {
  if (!bytes || bytes.length < 5 || bytesToBinaryString(bytes.subarray(0, 5)) !== "%PDF-") return bytes;
  let text = bytesToBinaryString(bytes);
  text = text.replace(/\/URI\s*\((?:\\[\s\S]|[^\\)])*\)/g, (match) => match.replace(/\(([\s\S]*)\)$/, (_whole, inner) => `(${String(inner).replace(/[^\r\n]/g, " ")})`));
  text = text.replace(/\/URI\s*<[^>]*>/g, (match) => match.replace(/<([^>]*)>$/, (_whole, inner) => `<${String(inner).replace(/[0-9A-Fa-f]/g, "0")}>`));
  text = text.replace(/\/S\s*\/URI/g, (match) => match.replace("/URI", "/XYZ"));
  return binaryStringToBytes(text);
}

async function sanitizePdfExternalLinksBody(body) {
  const bytes = new Uint8Array(await new Response(body).arrayBuffer());
  return sanitizePdfExternalLinksBytes(bytes);
}

function externalPdfResponse(request, env, sanitized, title, id) {
  return new Response(sanitized, {
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/pdf",
      "Content-Disposition": contentDisposition(`${title || id}.pdf`),
      "Cache-Control": "no-store, private",
      "X-Content-Type-Options": "nosniff",
      "X-KCDesk-PDF-Sanitized": "links",
    },
  });
}

// Ask GitHub to run the external grab workflow for a gated report. Returns true
// when the dispatch was accepted (HTTP 204).
async function triggerExternalGrab(env, id) {
  const repo = String(env.GH_REPO || "").trim();
  const token = String(env.GH_DISPATCH_TOKEN || "").trim();
  if (!repo || !token || token === "unconfigured") return false;
  try {
    const resp = await fetch(`https://api.github.com/repos/${repo}/dispatches`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "kc-desk-notes-worker",
        "X-GitHub-Api-Version": "2022-11-28",
      },
      body: JSON.stringify({ event_type: "report" + "ify-grab", client_payload: { id } }),
    });
    return resp.ok;
  } catch (_error) {
    return false;
  }
}

async function handleExternalPdf(request, env) {
  const url = new URL(request.url);
  let payload = {};
  if (request.method === "POST") {
    try {
      payload = await request.json();
    } catch (_error) {
      return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
    }
  }
  const id = String(payload.id || url.searchParams.get("id") || "").trim();
  const password = String(payload.password || url.searchParams.get("password") || "");
  if (!isExternalId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const accountDecision = await accountDownloadDecision(env, request, id, "external");
  const accountAllowed = Boolean(accountDecision.allowed);
  if (!password && !accountAllowed) {
    return jsonResponse(request, env, accountDecision.status || 402, {
      error: accountDecision.error || "Please log in, purchase this report, or enter the report password.",
      contact: accountDecision.contact || undefined,
      limit_exceeded: Boolean(accountDecision.limit_exceeded),
    });
  }
  if (!accountAllowed && !(await sharedReportPasswordMatches(env, id, password))) {
    return jsonResponse(request, env, 401, { error: "Password is incorrect." });
  }

  // 1) Directly readable reports expose a presigned PDF url - stream it (instant).
  const direct = await externalDirectPdfUrl(id);
  if (direct.url) {
    try {
      const pdf = await fetchWithTimeout(direct.url, { headers: { "User-Agent": EXTERNAL_UA } }, UPSTREAM_PDF_TIMEOUT_MS);
      if (pdf.ok) {
        const sanitized = await sanitizePdfExternalLinksBody(pdf.body);
        const consumed = await finalizeAccountDownloadDecision(env, request, accountDecision, id, "external");
        if (!consumed.ok) {
          return jsonResponse(request, env, consumed.status || 403, {
            error: consumed.error || TRIAL_LIMIT_MESSAGE,
            contact: consumed.contact || CONTACT_WECHAT,
            limit_exceeded: Boolean(consumed.limit_exceeded),
          });
        }
        return externalPdfResponse(request, env, sanitized, direct.title, id);
      }
    } catch (_error) {
      // Fall through to the R2 / grab paths below.
    }
  }

  // 2) Already grabbed by the workflow and mirrored to R2.
  if (env.REPORT_BUCKET) {
    const object = await env.REPORT_BUCKET.get(externalObjectKey(id));
    if (object) {
      const sanitized = await sanitizePdfExternalLinksBody(object.body);
      const consumed = await finalizeAccountDownloadDecision(env, request, accountDecision, id, "external");
      if (!consumed.ok) {
        return jsonResponse(request, env, consumed.status || 403, {
          error: consumed.error || TRIAL_LIMIT_MESSAGE,
          contact: consumed.contact || CONTACT_WECHAT,
          limit_exceeded: Boolean(consumed.limit_exceeded),
        });
      }
      return externalPdfResponse(request, env, sanitized, direct.title, id);
    }
  }

  // 3) Gated and not yet mirrored - request preparation and let the page poll.
  const stored = await externalStoredStatus(env, id);
  if (externalStatusIsActive(stored)) {
    return externalPendingResponse(request, env, stored);
  }
  if (externalStatusIsRecentFailure(stored)) {
    return jsonResponse(request, env, 503, {
      error: `报告刚刚准备失败，请稍后重试或联系 WeChat: ${CONTACT_WECHAT}。`,
      updated_at: String(stored.updated_at || ""),
    });
  }

  await externalPutStatus(env, id, "queued");
  const dispatched = await triggerExternalGrab(env, id);
  if (!dispatched) {
    await externalPutStatus(env, id, "failed", "dispatch failed");
    return jsonResponse(request, env, 503, {
      error: `文件准备服务暂时不可用，请联系 WeChat: ${CONTACT_WECHAT}。`,
    });
  }
  return externalPendingResponse(request, env, { status: "queued", updated_at: new Date().toISOString() });
}

async function handleExternalStatus(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!isExternalId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  let ready = false;
  if (env.REPORT_BUCKET) {
    const head = await env.REPORT_BUCKET.head(externalObjectKey(id));
    ready = Boolean(head);
  }
  if (ready) return jsonResponse(request, env, 200, { ready, status: "ready" });

  const stored = await externalStoredStatus(env, id);
  if (stored && stored.status === "failed") {
    return jsonResponse(request, env, 200, {
      ready: false,
      status: "failed",
      message: `报告准备失败，请联系 ${CONTACT_WECHAT}。`,
      updated_at: String(stored.updated_at || ""),
    });
  }
  return jsonResponse(request, env, 200, {
    ready: false,
    status: stored && stored.status ? String(stored.status) : "pending",
    updated_at: stored && stored.updated_at ? String(stored.updated_at) : "",
  });
}

// ---------------------------------------------------------------------------
// Hibor metadata integration
// ---------------------------------------------------------------------------

function decodeHtmlEntities(value) {
  const named = {
    amp: "&",
    lt: "<",
    gt: ">",
    quot: "\"",
    apos: "'",
    nbsp: " ",
    middot: "·",
  };
  return String(value || "")
    .replace(/&#x([0-9a-f]+);/gi, (_all, hex) => {
      const code = Number.parseInt(hex, 16);
      return Number.isFinite(code) ? String.fromCodePoint(code) : "";
    })
    .replace(/&#(\d+);/g, (_all, digits) => {
      const code = Number.parseInt(digits, 10);
      return Number.isFinite(code) ? String.fromCodePoint(code) : "";
    })
    .replace(/&([a-z]+);/gi, (all, name) => named[String(name || "").toLowerCase()] || all);
}

function stripHtml(value) {
  return decodeHtmlEntities(String(value || "").replace(/<[^>]*>/g, " "));
}

function cleanHtmlText(value) {
  return stripHtml(value).replace(/\s+/g, " ").trim();
}

function reportAPublicText(value) {
  return String(value || "").replace(/慧博/g, "报告A").replace(/Hibor/gi, "报告A");
}

function hiborMetaField(block, label) {
  const match = String(block || "").match(new RegExp(`<span>\\s*${label}：([\\s\\S]*?)<\\/span>`, "i"));
  return match ? reportAPublicText(cleanHtmlText(match[1])) : "";
}

function hiborDateFromTitle(title) {
  const match = String(title || "").match(/-(\d{2})(\d{2})(\d{2})$/);
  if (!match) return "";
  return `20${match[1]}-${match[2]}-${match[3]}`;
}

function hiborInstitutionFromTitle(title) {
  const text = String(title || "").trim();
  const index = text.indexOf("-");
  return index > 0 ? text.slice(0, index).trim() : "";
}

function parseHiborItems(html) {
  const items = [];
  const rowRe = /<tr>\s*<td>([\s\S]*?)<\/td>\s*<\/tr>/gi;
  let match;
  while ((match = rowRe.exec(String(html || ""))) && items.length < HIBOR_SEARCH_PAGE_SIZE) {
    const block = match[1];
    if (!/tab_divttl/i.test(block)) continue;
    const link = block.match(/<div class="tab_divttl"[\s\S]*?<a\s+href="([^"]+)"[^>]*title="([^"]*)"[^>]*>([\s\S]*?)<\/a>/i);
    if (!link) continue;
    const href = decodeHtmlEntities(link[1]);
    const idMatch = href.match(/\/data\/([^/.]+)\.html/i);
    if (!idMatch) continue;
    const title = reportAPublicText(cleanHtmlText(link[2] || link[3]));
    if (!title) continue;
    const shareTime = hiborMetaField(block, "分享时间");
    const pageText = hiborMetaField(block, "页数");
    const pageMatch = pageText.match(/\d+/);
    items.push({
      id: `${HIBOR_SOURCE}:${idMatch[1]}`,
      source: HIBOR_SOURCE,
      title,
      institution: hiborInstitutionFromTitle(title),
      date: shareTime.slice(0, 10) || hiborDateFromTitle(title),
      share_time: shareTime,
      category: hiborMetaField(block, "栏目"),
      author: hiborMetaField(block, "作者"),
      rating: hiborMetaField(block, "评级"),
      page_count: pageMatch ? Number(pageMatch[0]) : 0,
      file_type: "pdf",
    });
  }
  return items;
}

async function handleHiborSearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  if (!query) return jsonResponse(request, env, 200, { items: [], page: 1, total: 0 });

  return handleCachedSearch(request, env, HIBOR_SOURCE, query, page, {
    items: [],
    page,
    total: 0,
    source: HIBOR_SOURCE,
  }, async () => {
    const body = new URLSearchParams({
      hy1: "all",
      hy2: "all",
      ybbt: query,
    }).toString();
    const upstream = `${HIBOR_ORIGIN}/newweb/web/hangye?page=${encodeURIComponent(String(page))}`;
    const response = await fetchWithTimeout(upstream, {
      method: "POST",
      headers: {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": HIBOR_ORIGIN,
        "Referer": `${HIBOR_ORIGIN}/newweb/web/hangye?page=1`,
        "User-Agent": HIBOR_UA,
      },
      body,
    });
    if (!response.ok) {
      throw new Error(`Report A search failed (${response.status}).`);
    }
    const html = await response.text();
    const items = parseHiborItems(html);
    return {
      items,
      page,
      total: 0,
      source: HIBOR_SOURCE,
    };
  }, null, { skipFreshCache: true });
}

// ---------------------------------------------------------------------------
// International think-tank / institution PDF archive
// ---------------------------------------------------------------------------

function thinkTankBasename(value) {
  return String(value || "")
    .split(/[?#]/)[0]
    .split("/")
    .pop()
    .replace(/\.pdf$/i, "")
    .trim();
}

function thinkTankSlug(row) {
  const base = thinkTankBasename(row && row.local_filename) ||
    thinkTankBasename(row && row.pdf_url) ||
    compactSearchQuery(row && row.title);
  return String(base || "report")
    .replace(/[^A-Za-z0-9._-]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 180) || "report";
}

function thinkTankId(row) {
  const hash = thinkTankHashFromFilename(row && row.local_filename);
  return `${THINKTANK_SOURCE}:${hash || thinkTankSlug(row)}`;
}

function parseThinkTankId(value) {
  const match = String(value || "").trim().match(/^thinktank:([A-Za-z0-9._-]{3,220})$/);
  return match ? { id: `thinktank:${match[1]}`, slug: match[1] } : null;
}

function thinkTankHashFromFilename(value) {
  const match = String(value || "").match(/_([0-9a-f]{6,12})(?:\.pdf)?$/i);
  return match ? match[1].toLowerCase() : "";
}

function thinkTankRowMatchesId(row, parsed) {
  if (!row || !parsed) return false;
  const hash = thinkTankHashFromFilename(row.local_filename);
  return parsed.slug === hash || parsed.slug === thinkTankSlug(row);
}

function thinkTankDate(row) {
  const date = String(row && row.date || "").trim();
  if (/^\d{6}$/.test(date)) return `20${date.slice(0, 2)}-${date.slice(2, 4)}-${date.slice(4, 6)}`;
  if (/^\d{8}$/.test(date)) return `${date.slice(0, 4)}-${date.slice(4, 6)}-${date.slice(6, 8)}`;
  const published = String(row && row.published || "").trim();
  const iso = published.match(/(20\d{2})[-/](\d{2})[-/](\d{2})/);
  if (iso) return `${iso[1]}-${iso[2]}-${iso[3]}`;
  const archived = String(row && row.archived_at || "").slice(0, 10);
  return /^\d{4}-\d{2}-\d{2}$/.test(archived) ? archived : "";
}

function thinkTankInstitution(row) {
  const cn = String(row && row.institution_cn || "").trim();
  const en = String(row && row.institution_en || row && row.institution || "").trim();
  if (cn && en && cn.toLowerCase() !== en.toLowerCase()) return `${en} · ${cn}`;
  return cn || en || "国际智库";
}

function slimThinkTankItem(row, wechatTitleMap = new Map()) {
  const id = thinkTankId(row);
  const hash = thinkTankHashFromFilename(row && row.local_filename);
  const wechatTitle = hash ? String(wechatTitleMap.get(hash) || "").trim() : "";
  const title = String(row && row.title || "").replace(/\s+/g, " ").trim();
  return {
    id,
    source: THINKTANK_SOURCE,
    title: title || "Untitled report",
    title_cn: wechatTitle,
    institution: thinkTankInstitution(row),
    institution_en: String(row && row.institution_en || row && row.institution || "").trim(),
    institution_cn: String(row && row.institution_cn || "").trim(),
    date: thinkTankDate(row),
    page_count: Number(row && row.page_count || 0) || 0,
    size_bytes: Number(row && row.bytes || 0) || 0,
    file_type: "pdf",
  };
}

async function thinkTankArchiveRows(env) {
  const text = await githubContentText(env, THINKTANK_ARCHIVE_PATH);
  return String(text || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      try {
        return JSON.parse(line);
      } catch (_error) {
        return null;
      }
    })
    .filter((row) => row && row.pdf_url && row.title);
}

function thinkTankOriginalHashFromArticle(article) {
  const content = String(article && article.content || article && article.content_html || "");
  const match = content.match(/Original report:\s*[A-Za-z0-9._-]+\s+[\s\S]{0,220}?\s+([0-9a-f]{6,12})(?:\s|<|$)/i);
  return match ? match[1].toLowerCase() : "";
}

async function thinkTankWechatTitleMap(env) {
  const map = new Map();
  let dateDirs = [];
  try {
    dateDirs = await githubContents(env, THINKTANK_WECHAT_DRAFT_ROOT);
  } catch (_error) {
    return map;
  }
  const dirs = dateDirs
    .filter((entry) => entry && entry.type === "dir" && /^\d{6}$/.test(String(entry.name || "")))
    .sort((a, b) => String(b.name || "").localeCompare(String(a.name || "")))
    .slice(0, THINKTANK_WECHAT_DATE_LIMIT);

  await Promise.allSettled(dirs.map(async (dir) => {
    let files = [];
    try {
      files = await githubContents(env, `${THINKTANK_WECHAT_DRAFT_ROOT}/${dir.name}`);
    } catch (_error) {
      return;
    }
    const payloadFiles = files
      .filter((entry) => /^draft_payload_\d+\.json$/i.test(String(entry && entry.name || "")))
      .slice(0, 12);
    await Promise.allSettled(payloadFiles.map(async (file) => {
      let payload = null;
      try {
        payload = await githubContentJson(env, file.path);
      } catch (_error) {
        return;
      }
      const articles = Array.isArray(payload && payload.articles) ? payload.articles : [];
      for (const article of articles) {
        const hash = thinkTankOriginalHashFromArticle(article);
        const title = cleanHtmlText(article && article.title || "");
        if (hash && title && !map.has(hash)) map.set(hash, title);
      }
    }));
  }));
  return map;
}

function thinkTankSearchText(item) {
  return [
    item && item.title,
    item && item.title_cn,
    item && item.institution,
    item && item.institution_en,
    item && item.institution_cn,
    item && item.date,
    item && item.file_type,
  ].filter(Boolean).join(" ").normalize("NFKC").toLowerCase();
}

function scoreThinkTankItem(item, query, terms) {
  const compact = compactSearchQuery(query).toLowerCase();
  const title = String(item && item.title || "").normalize("NFKC").toLowerCase();
  const titleCn = String(item && item.title_cn || "").normalize("NFKC").toLowerCase();
  const institution = String(item && item.institution || "").normalize("NFKC").toLowerCase();
  const haystack = thinkTankSearchText(item);
  let score = 0;
  if (compact && title.includes(compact)) score += 90;
  if (compact && titleCn.includes(compact)) score += 95;
  if (compact && institution.includes(compact)) score += 60;
  for (const term of terms) {
    if (title.includes(term) || titleCn.includes(term)) score += 20;
    else if (institution.includes(term)) score += 12;
    else if (haystack.includes(term)) score += 4;
    else return 0;
  }
  return score || (compact && haystack.includes(compact) ? 2 : 0);
}

async function thinkTankSearchPayload(env, query, page, ctx = null) {
  const [rows, wechatTitles] = await Promise.all([
    thinkTankArchiveRows(env),
    thinkTankWechatTitleMap(env),
  ]);
  const terms = searchMirrorTerms(query);
  const scored = rows
    .map((row) => ({ row, item: slimThinkTankItem(row, wechatTitles) }))
    .filter((entry) => entry.item.id && entry.item.title)
    .map((entry) => ({
      ...entry,
      score: terms.length ? scoreThinkTankItem(entry.item, query, terms) : 1,
    }))
    .filter((entry) => entry.score > 0)
    .sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      return dateScore(b.item && b.item.date) - dateScore(a.item && a.item.date);
    });
  const start = Math.max(0, (page - 1) * THINKTANK_SEARCH_PAGE_SIZE);
  const pageEntries = scored.slice(start, start + THINKTANK_SEARCH_PAGE_SIZE);
  if (ctx && pageEntries.length) {
    ctx.waitUntil(warmThinkTankRows(env, pageEntries.map((entry) => entry.row), THINKTANK_SEARCH_WARM_LIMIT).catch(() => null));
  }
  return {
    items: pageEntries.map((entry) => entry.item),
    page,
    total: scored.length,
    source: THINKTANK_SOURCE,
  };
}

async function handleThinkTankSearch(request, env, ctx = null) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  if (!query) return jsonResponse(request, env, 200, { items: [], page: 1, total: 0, source: THINKTANK_SOURCE });

  return handleCachedSearch(request, env, THINKTANK_SOURCE, query, page, {
    items: [],
    page,
    total: 0,
    source: THINKTANK_SOURCE,
  }, () => thinkTankSearchPayload(env, query, page, ctx), null, { skipFreshCache: true });
}

async function findThinkTankRow(env, id) {
  const parsed = parseThinkTankId(id);
  if (!parsed) return null;
  const rows = await thinkTankArchiveRows(env);
  return rows.find((row) => thinkTankRowMatchesId(row, parsed)) || null;
}

function thinkTankObjectKey(id) {
  const parsed = parseThinkTankId(id);
  const slug = parsed ? parsed.slug : String(id || "").replace(/[^A-Za-z0-9._-]+/g, "-");
  return `${THINKTANK_R2_PREFIX}/${slug}.pdf`;
}

function thinkTankObjectKeyForRow(row) {
  return thinkTankObjectKey(thinkTankId(row));
}

async function handleThinkTankItem(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!parseThinkTankId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const row = await findThinkTankRow(env, id);
  if (!row) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }
  const wechatTitles = await thinkTankWechatTitleMap(env).catch(() => new Map());
  return jsonResponse(request, env, 200, {
    item: slimThinkTankItem(row, wechatTitles),
  });
}

async function cacheThinkTankPdf(env, row) {
  if (!env.REPORT_BUCKET || !row) return { ok: false, reason: "bucket-unavailable" };
  const id = thinkTankId(row);
  const key = thinkTankObjectKeyForRow(row);
  const existing = await env.REPORT_BUCKET.head(key).catch(() => null);
  if (existing) return { ok: true, cached: true, key };

  const pdfUrl = String(row.pdf_url || "").trim();
  if (!/^https?:\/\//i.test(pdfUrl)) return { ok: false, reason: "missing-url" };
  const pdf = await fetchWithTimeout(pdfUrl, {
    headers: {
      "Accept": "application/pdf,*/*",
      "User-Agent": THINKTANK_UA,
    },
    redirect: "follow",
  }, Math.max(UPSTREAM_PDF_TIMEOUT_MS, 45000));
  if (!pdf.ok) return { ok: false, reason: `http-${pdf.status}` };

  const bytes = sanitizePdfExternalLinksBytes(new Uint8Array(await pdf.arrayBuffer()));
  await env.REPORT_BUCKET.put(key, bytes, {
    httpMetadata: {
      contentType: "application/pdf",
      contentDisposition: contentDisposition(`${row.title || id}.pdf`),
      cacheControl: "public, max-age=2592000, immutable",
    },
    customMetadata: {
      source: THINKTANK_SOURCE,
      id,
      cached_at: new Date().toISOString(),
    },
  });
  return { ok: true, cached: false, key };
}

async function warmThinkTankRows(env, rows, limit = THINKTANK_WARM_PDF_LIMIT) {
  if (!env.REPORT_BUCKET) return { ok: false, warmed: 0, reason: "bucket-unavailable" };
  const queue = (Array.isArray(rows) ? rows : [])
    .filter((row) => row && row.pdf_url)
    .slice(0, Math.max(0, limit));
  let warmed = 0;
  let index = 0;
  const workers = Array.from({ length: Math.min(THINKTANK_WARM_CONCURRENCY, Math.max(1, queue.length)) }, async () => {
    while (index < queue.length) {
      const row = queue[index];
      index += 1;
      try {
        const result = await cacheThinkTankPdf(env, row);
        if (result.ok) warmed += 1;
      } catch (_error) {
        // Best-effort cache warming; download path can still fetch on demand.
      }
    }
  });
  await Promise.allSettled(workers);
  return { ok: true, warmed };
}

async function warmThinkTankPdfCache(env) {
  const rows = await thinkTankArchiveRows(env);
  const sorted = rows
    .slice()
    .sort((a, b) => {
      const dateCompare = dateScore(thinkTankDate(b)) - dateScore(thinkTankDate(a));
      if (dateCompare) return dateCompare;
      return String(b.archived_at || "").localeCompare(String(a.archived_at || ""));
    });
  return warmThinkTankRows(env, sorted, THINKTANK_WARM_PDF_LIMIT);
}

async function handleThinkTankPdf(request, env) {
  const url = new URL(request.url);
  let payload = {};
  if (request.method === "POST") {
    try {
      payload = await request.json();
    } catch (_error) {
      return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
    }
  }
  const id = String(payload.id || url.searchParams.get("id") || "").trim();
  const password = String(payload.password || url.searchParams.get("password") || "");
  if (!parseThinkTankId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const row = await findThinkTankRow(env, id);
  if (!row) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }
  const canonicalId = thinkTankId(row);
  const cacheKey = thinkTankObjectKeyForRow(row);

  const accountDecision = await accountDownloadDecision(env, request, canonicalId, THINKTANK_SOURCE);
  const accountAllowed = Boolean(accountDecision.allowed);
  if (!password && !accountAllowed) {
    return jsonResponse(request, env, accountDecision.status || 402, {
      error: accountDecision.error || "Please log in, purchase this report, or enter the report password.",
      contact: accountDecision.contact || undefined,
      limit_exceeded: Boolean(accountDecision.limit_exceeded),
    });
  }
  if (!accountAllowed && !(await sharedReportPasswordMatches(env, canonicalId, password)) && !(id !== canonicalId && await sharedReportPasswordMatches(env, id, password))) {
    return jsonResponse(request, env, 401, { error: "Password is incorrect." });
  }

  if (env.REPORT_BUCKET) {
    const object = await env.REPORT_BUCKET.get(cacheKey);
    if (object) {
      const sanitized = await sanitizePdfExternalLinksBody(object.body);
      const consumed = await finalizeAccountDownloadDecision(env, request, accountDecision, canonicalId, THINKTANK_SOURCE);
      if (!consumed.ok) {
        return jsonResponse(request, env, consumed.status || 403, {
          error: consumed.error || TRIAL_LIMIT_MESSAGE,
          contact: consumed.contact || CONTACT_WECHAT,
          limit_exceeded: Boolean(consumed.limit_exceeded),
        });
      }
      return externalPdfResponse(request, env, sanitized, row.title, id);
    }
  }

  let cached = null;
  try {
    await cacheThinkTankPdf(env, row);
    cached = env.REPORT_BUCKET ? await env.REPORT_BUCKET.get(cacheKey) : null;
  } catch (_error) {
    cached = null;
  }
  if (!cached) {
    return jsonResponse(request, env, 502, {
      error: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.`,
      contact: CONTACT_WECHAT,
    });
  }
  const sanitized = await sanitizePdfExternalLinksBody(cached.body);
  const consumed = await finalizeAccountDownloadDecision(env, request, accountDecision, canonicalId, THINKTANK_SOURCE);
  if (!consumed.ok) {
    return jsonResponse(request, env, consumed.status || 403, {
      error: consumed.error || TRIAL_LIMIT_MESSAGE,
      contact: consumed.contact || CONTACT_WECHAT,
      limit_exceeded: Boolean(consumed.limit_exceeded),
    });
  }
  return externalPdfResponse(request, env, sanitized, row.title, id);
}

// ---------------------------------------------------------------------------
// Authority report integration
// ---------------------------------------------------------------------------

function parseAuthorityId(value) {
  const match = String(value || "").trim().match(/^(foreign|foreign-rt):([0-9]{1,25})$/);
  if (!match || !AUTHORITY_KINDS[match[1]]) return null;
  return {
    kind: match[1],
    upstreamId: match[2],
    compoundId: `${match[1]}:${match[2]}`,
    config: AUTHORITY_KINDS[match[1]],
  };
}

function authoritySearchPayload(query, page) {
  return {
    releaseDate: 0,
    startDate: "",
    endDate: "",
    minPages: 0,
    keyword: query,
    reportTypes: [],
    industries: [],
    pageNum: page,
    pageSize: AUTHORITY_SEARCH_PAGE_SIZE,
  };
}

function authoritySearchHeaders(kindConfig) {
  return {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": AUTHORITY_ORIGIN,
    "Referer": kindConfig.referer,
    "User-Agent": AUTHORITY_UA,
  };
}

function slimAuthorityItem(kind, record) {
  const config = AUTHORITY_KINDS[kind];
  const id = String(record.id || "").trim();
  const title = String(record.title || "").replace(/\s+/g, " ").trim();
  const institution = String(record.securities || record.companyName || "").trim();
  if (!id) return { id: "" };
  return {
    id: `${kind}:${id}`,
    source: AUTHORITY_SOURCE,
    kind,
    kind_label: config.label,
    title: title || "Untitled report",
    institution,
    date: String(record.reDate || "").trim(),
    report_type: String(record.reportType || "").trim(),
    page_count: Number(record.page || record.pages || 0) || 0,
    language: String(record.lang || "").trim(),
    stock_code: String(record.stockCode || record.companycode || "").trim(),
    stock_name: String(record.stockName || record.companyName || "").trim(),
    author: String(record.author || record.authors || "").trim(),
    file_type: "pdf",
  };
}

async function authoritySearchOne(kind, query, page) {
  const config = AUTHORITY_KINDS[kind];
  const response = await fetchWithTimeout(`${AUTHORITY_ORIGIN}${config.endpoint}`, {
    method: "POST",
    headers: authoritySearchHeaders(config),
    body: JSON.stringify(authoritySearchPayload(query, page)),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const raw = await response.json();
  const data = raw && raw.data && typeof raw.data === "object" ? raw.data : null;
  if (raw.code !== 200 || !data || !Array.isArray(data.records)) throw new Error("bad response");
  return {
    kind,
    page: Number(data.pageNum || page),
    total: Number(data.total || 0),
    items: data.records.map((record) => slimAuthorityItem(kind, record)).filter((item) => item.id && item.title),
  };
}

async function handleAuthoritySearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  const requestedKind = String(url.searchParams.get("kind") || "both").trim();
  if (!query) {
    return jsonResponse(request, env, 200, { items: [], page: 1, total: 0 });
  }

  return handleCachedSearch(request, env, AUTHORITY_SOURCE, `${requestedKind}:${query}`, page, {
    items: [],
    page,
    total: 0,
    sources: [],
  }, async () => {
    const kinds = AUTHORITY_KINDS[requestedKind] ? [requestedKind] : Object.keys(AUTHORITY_KINDS);
    const results = await Promise.allSettled(kinds.map((kind) => authoritySearchOne(kind, query, page)));
    const fulfilled = results
      .filter((result) => result.status === "fulfilled")
      .map((result) => result.value);
    const items = fulfilled.flatMap((result) => result.items)
      .sort((a, b) => String(b.date || "").localeCompare(String(a.date || "")));
    if (!fulfilled.length && results.length) {
      throw new Error("Authority search is unavailable.");
    }
    return {
      items,
      page,
      total: fulfilled.reduce((sum, result) => sum + result.total, 0),
      sources: fulfilled.map((result) => ({ kind: result.kind, total: result.total })),
    };
  }, (_error) => searchMirrorFallback(env, AUTHORITY_SOURCE, query, page, AUTHORITY_SEARCH_PAGE_SIZE, (result) => {
    const items = result.items.filter((item) => requestedKind === "both" || item.kind === requestedKind);
    return {
      items,
      page,
      total: result.total,
      sources: Object.keys(AUTHORITY_KINDS).map((kind) => ({
        kind,
        total: items.filter((item) => item.kind === kind).length,
      })),
      mirror_generated_at: result.generated_at,
      mirror_stale: result.mirror_stale,
    };
  }), { skipFreshCache: true });
}

async function handleAuthorityPdf(request, env) {
  return jsonResponse(request, env, 403, {
    error: `高权报告仅提供检索线索，无法直接下载。请联系 WeChat: ${CONTACT_WECHAT}。`,
    contact: CONTACT_WECHAT,
  });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const pathname = url.pathname.startsWith("/api/")
      ? url.pathname.slice(4) || "/"
      : url.pathname;

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(request, env) });
    }

    if (pathname === "/health") {
      const [filesSnapshot, analyticsSnapshot, opsMirrorState] = await Promise.all([
        safeR2GetJson(env, ADMIN_FILES_SNAPSHOT_KEY),
        safeR2GetJson(env, ADMIN_ANALYTICS_SNAPSHOT_KEY),
        safeR2GetJson(env, ADMIN_OPS_MIRROR_STATE_KEY),
      ]);
      return jsonResponse(request, env, 200, {
        ok: true,
        dashboard_cache: {
          files: adminSnapshotStatus(filesSnapshot, ADMIN_FILES_SNAPSHOT_FRESH_MS),
          analytics: adminSnapshotStatus(analyticsSnapshot, ADMIN_ANALYTICS_SNAPSHOT_FRESH_MS),
        },
        ops_mirror: opsMirrorState ? {
          status: String(opsMirrorState.status || "unknown"),
          file_count: Number(opsMirrorState.file_count || 0),
          attempted_at: String(opsMirrorState.attempted_at || ""),
          dispatched_at: String(opsMirrorState.dispatched_at || ""),
        } : {
          status: "waiting",
          file_count: 0,
          attempted_at: "",
          dispatched_at: "",
        },
      });
    }

    if (pathname === "/analytics" && request.method === "POST") {
      return handleAnalyticsEvent(request, env, ctx);
    }

    if (pathname === "/calc" && request.method === "GET") {
      return handleCalculator(request, env);
    }

    if (pathname === "/download" && request.method === "POST") {
      return handleDownload(request, env);
    }

    if (pathname === "/captcha" && request.method === "GET") {
      return handleCaptcha(request, env);
    }

    if (pathname === "/auth" && (request.method === "GET" || request.method === "POST")) {
      return handleAuth(request, env);
    }

    if (pathname === "/account/password" && request.method === "POST") {
      return handleAccountPasswordChange(request, env);
    }

    if (pathname === "/entitlement" && request.method === "GET") {
      return handleEntitlement(request, env);
    }

    if (pathname === "/ops/alerts/email" && request.method === "POST") {
      return handleOpsAlertEmail(request, env);
    }

    if (pathname === "/vid2ppt/redeem-code" && request.method === "POST") {
      return handleVid2PptRedeemCode(request, env);
    }

    if (pathname === "/newsfeed/home" && request.method === "GET") {
      return handleNewsfeedHome(request, env);
    }

    if (pathname === "/newsfeed/explore" && request.method === "GET") {
      return handleNewsfeedExplore(request, env);
    }

    if (pathname === "/newsfeed/topic" && request.method === "GET") {
      return handleNewsfeedTopic(request, env);
    }

    if (pathname === "/newsfeed/topics" && request.method === "POST") {
      return handleNewsfeedCreateTopic(request, env, ctx);
    }

    if (pathname === "/newsfeed/topics/pin" && request.method === "POST") {
      return handleNewsfeedPinTopic(request, env);
    }

    if (pathname === "/newsfeed/settings" && (request.method === "GET" || request.method === "POST")) {
      return handleNewsfeedSettings(request, env);
    }

    if (pathname === "/newsfeed/email-test" && request.method === "POST") {
      return handleNewsfeedEmailSend(request, env, { test: true });
    }

    if (pathname === "/newsfeed/email-send" && request.method === "POST") {
      return handleNewsfeedEmailSend(request, env);
    }

    if (pathname === "/newsfeed/article" && request.method === "POST") {
      return handleNewsfeedArticle(request, env);
    }

    if (pathname === "/newsfeed/briefing" && request.method === "POST") {
      return handleNewsfeedBriefing(request, env);
    }

    if (pathname === "/paddle-config" && request.method === "GET") {
      return jsonResponse(request, env, 410, {
        detail: "KCdesk checkout is closed. Vid2PPT NOVA sponsor checkout handles payment and may gift KCdesk.com membership time.",
      });
    }

    if (pathname === "/paddle-webhook" && request.method === "POST") {
      return jsonResponse(request, env, 410, {
        detail: "KCdesk Paddle webhook is closed. Payment events are handled by Vid2PPT.",
      });
    }

    if (["/vid2ppt/nova-grant", "/vid2ppt/atlas-grant"].includes(pathname) && request.method === "POST") {
      return handleVid2PptGiftGrant(request, env);
    }

    if (pathname === "/admin/login" && request.method === "POST") {
      return handleAdminLogin(request, env);
    }

    if (pathname === "/admin/report-password" && request.method === "POST") {
      return handleAdminReportPassword(request, env);
    }

    if (pathname === "/account-admin/summary" && request.method === "GET") {
      return handleAccountAdminSummary(request, env, ctx);
    }

    if (pathname === "/account-admin/analytics-events" && request.method === "GET") {
      return handleAccountAdminAnalyticsEvents(request, env);
    }

    if (pathname === "/account-admin/user-access" && request.method === "POST") {
      return handleAccountAdminUserAccess(request, env);
    }

    if (pathname === "/account-admin/user" && request.method === "POST") {
      return handleAccountAdminUserCreate(request, env);
    }

    if (pathname === "/account-admin/user-status" && request.method === "POST") {
      return handleAccountAdminUserStatus(request, env);
    }

    if (pathname === "/account-admin/github-file" && request.method === "GET") {
      return handleAccountAdminGithubFile(request, env, ctx);
    }

    if (pathname === "/account-admin/github-artifact" && request.method === "GET") {
      return handleAccountAdminGithubArtifact(request, env, ctx);
    }

    if (pathname === "/account-admin/prepare-github-download" && request.method === "GET") {
      return prepareAdminGithubFileCache(request, env);
    }

    if (pathname === "/account-admin/report-pdf" && request.method === "GET") {
      return handleAccountAdminReportPdf(request, env);
    }

    if (pathname === "/external/search" && request.method === "GET") {
      return handleExternalSearch(request, env);
    }

    if (pathname === "/external/pdf" && (request.method === "GET" || request.method === "POST")) {
      return handleExternalPdf(request, env);
    }

    if (pathname === "/external/status" && request.method === "GET") {
      return handleExternalStatus(request, env);
    }

    if (pathname === "/external/item" && request.method === "GET") {
      return handleExternalItem(request, env);
    }

    if (pathname === "/report-a/search" && request.method === "GET") {
      return handleHiborSearch(request, env);
    }

    if (pathname === "/thinktank/search" && request.method === "GET") {
      return handleThinkTankSearch(request, env, ctx);
    }

    if (pathname === "/thinktank/item" && request.method === "GET") {
      return handleThinkTankItem(request, env);
    }

    if (pathname === "/thinktank/pdf" && (request.method === "GET" || request.method === "POST")) {
      return handleThinkTankPdf(request, env);
    }

    if (pathname === "/authority/search" && request.method === "GET") {
      return handleAuthoritySearch(request, env);
    }

    if (pathname === "/authority/pdf" && (request.method === "GET" || request.method === "POST")) {
      return handleAuthorityPdf(request, env);
    }

    return jsonResponse(request, env, 404, { error: "Not found." });
  },

  async scheduled(event, env, ctx) {
    const cron = String(event && event.cron || "");
    const tasks = [];
    if (!cron || cron === "*/30 * * * *") {
      tasks.push(refreshAdminDashboardSnapshots(env));
      tasks.push(warmThinkTankPdfCache(env));
    }
    if (!cron || cron !== "*/30 * * * *") {
      tasks.push(warmNewsfeedCaches(env));
      tasks.push(sendDueNewsfeedDigestEmails(env));
    }
    ctx.waitUntil(Promise.allSettled(tasks));
  },
};
