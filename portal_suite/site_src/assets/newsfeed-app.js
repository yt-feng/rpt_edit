// Loaded only by the Newsfeed page; shared account/session helpers stay in app.js.
export async function initNewsfeedApp(dependencies) {
  const {
    CONTENT_INTL_LOCALE,
    CONTENT_LOCALE,
    authHeaders,
    authUserLabel,
    currentAnalyticsPath,
    escapeHtml,
    initAccountGate,
    initAdminGate,
    initNewsfeedNav,
    isLocalizedContentPage,
    isNewsfeedSession,
    isSuperSession,
    loadAuthSession,
    loadOptionalJson,
    localizedServiceMessage,
    refreshAuthSession,
    showAccountModal,
    trackEvent,
    workerBaseUrl,
  } = dependencies;
  const NEWSFEED_SYSTEM_TOPIC_IDS = new Set([
    "global-daily",
    "tech-ai",
    "global-politics",
    "industries",
    "investment",
  ]);

  function newsfeedLogoUrl(item) {
    if (item && item.logo_url) return item.logo_url;
    const domain = String(item && (item.domain || item.source_domain) || "").trim();
    return domain ? `https://www.google.com/s2/favicons?domain=${encodeURIComponent(domain)}&sz=64` : "";
  }

  function newsfeedTimeLabel(value) {
    const timestamp = Date.parse(value || "");
    if (!Number.isFinite(timestamp)) return "";
    const diff = Date.now() - timestamp;
    const minute = 60 * 1000;
    const hour = 60 * minute;
    const day = 24 * hour;
    if (!isLocalizedContentPage()) {
      if (diff >= 0 && diff < hour) return `${Math.max(1, Math.round(diff / minute))}m ago`;
      if (diff >= 0 && diff < day) return `${Math.max(1, Math.round(diff / hour))}h ago`;
      if (diff >= 0 && diff < 3 * day) return `${Math.max(1, Math.round(diff / day))}d ago`;
      return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" }).format(new Date(timestamp));
    }
    const relative = new Intl.RelativeTimeFormat(CONTENT_INTL_LOCALE, { numeric: "always" });
    if (diff >= 0 && diff < hour) return relative.format(-Math.max(1, Math.round(diff / minute)), "minute");
    if (diff >= 0 && diff < day) return relative.format(-Math.max(1, Math.round(diff / hour)), "hour");
    if (diff >= 0 && diff < 3 * day) return relative.format(-Math.max(1, Math.round(diff / day)), "day");
    return new Intl.DateTimeFormat(CONTENT_INTL_LOCALE, { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" }).format(new Date(timestamp));
  }

  function newsfeedSourceName(item) {
    return String(item && (item.source || item.source_name || item.domain) || "News")
      .replace(/^[^/]{1,48}\s*\/\s*/u, "")
      .trim() || "News";
  }

  const NEWSFEED_UI_COPY = {
    en: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      newsletterTopic: "Newsletter",
      noNewsletter: "Not subscribed",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    "zh-CN": {
      myFeed: "我的新闻",
      explore: "探索",
      addTopics: "添加话题",
      digestEmail: "邮件摘要",
      dailyDigest: "每日摘要",
      topHeadlines: "重点新闻",
      regions: "区域",
      language: "语言",
      outputLanguage: "输出语言",
      suggestedTopics: "热门话题",
      sendDailyDigest: "发送每日摘要",
      saveEmail: "保存邮箱",
      sendTestNow: "发送测试邮件",
      sendNewsletterNow: "立即发送 newsletter",
      newsletterTopic: "Newsletter 主题",
      noNewsletter: "不订阅",
      email: "邮箱",
      sendTime: "发送时间",
      timezone: "时区",
      noHeadlines: "暂无新闻。",
      loadingLatest: "正在加载最新新闻...",
      updating: "正在补全新闻流...",
      playBriefing: "播放简报",
      nowPlaying: "正在播放",
      playlist: "播放列表",
      readStory: "阅读新闻",
      addRegion: "添加区域",
      customRegion: "其他区域",
    },
    ja: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      newsletterTopic: "Newsletter",
      noNewsletter: "Not subscribed",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    ko: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      newsletterTopic: "Newsletter",
      noNewsletter: "Not subscribed",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    ar: {
      myFeed: "موجزك",
      explore: "استكشاف",
      addTopics: "إضافة مواضيع",
      digestEmail: "ملخص البريد",
      dailyDigest: "الملخص اليومي",
      topHeadlines: "أبرز الأخبار",
      regions: "المناطق",
      language: "اللغة",
      outputLanguage: "لغة المخرجات",
      suggestedTopics: "مواضيع مقترحة",
      sendDailyDigest: "إرسال الملخص اليومي",
      saveEmail: "حفظ البريد",
      sendTestNow: "إرسال اختبار الآن",
      sendNewsletterNow: "إرسال النشرة الآن",
      newsletterTopic: "النشرة",
      noNewsletter: "غير مشترك",
      email: "البريد الإلكتروني",
      sendTime: "وقت الإرسال",
      timezone: "المنطقة الزمنية",
      noHeadlines: "لا توجد أخبار بعد.",
      loadingLatest: "جارٍ تحميل أحدث الأخبار...",
      updating: "جارٍ تحديث الموجز الكامل...",
      playBriefing: "تشغيل الموجز الصوتي",
      nowPlaying: "يُشغّل الآن",
      playlist: "قائمة التشغيل",
      readStory: "قراءة الخبر",
      addRegion: "إضافة منطقة",
      customRegion: "منطقة أخرى",
    },
  };

  function newsfeedLanguageCode(value) {
    return ["en", "zh-CN", "ja", "ko", "ar"].includes(value) ? value : "en";
  }

  function newsfeedDefaultLanguage() {
    const contentLocale = window.PortalLocale && window.PortalLocale.contentLocale;
    return newsfeedLanguageCode(contentLocale);
  }

  function newsfeedFixedInterfaceLanguage() {
    return isLocalizedContentPage() ? newsfeedLanguageCode(CONTENT_LOCALE) : "";
  }

  function newsfeedInterfaceLocaleCode(value) {
    const language = newsfeedLanguageCode(value);
    return language === "zh-CN" || language === "en" ? "zh-Hans" : language;
  }

  function newsfeedInterfaceNavigationUrl(value) {
    const localeUrl = window.PortalLocale && window.PortalLocale.localeUrl;
    return typeof localeUrl === "function" ? localeUrl(newsfeedInterfaceLocaleCode(value)) : "";
  }

  function newsfeedText(state, key) {
    const language = newsfeedLanguageCode(state && state.interfaceLanguage || "en");
    return (NEWSFEED_UI_COPY[language] && NEWSFEED_UI_COPY[language][key]) || NEWSFEED_UI_COPY.en[key] || key;
  }

  // Built-in topic/region/category values are stable API identifiers and stay
  // in English on the wire. Keep presentation labels separate so locale builds
  // can translate visible copy without changing request/filter semantics.
  const NEWSFEED_SYSTEM_TOPIC_COPY = {
    "global-daily": {
      title: "Global Daily",
      description: "A broad feed across markets, policy, technology, and global affairs.",
    },
    "tech-ai": {
      title: "Technology news",
      description: "AI, robotics, semiconductors, software, and platform shifts.",
    },
    "global-politics": {
      title: "Politics news",
      description: "Elections, policy, geopolitics, defense, sanctions, and trade.",
    },
    industries: {
      title: "Industry news",
      description: "Energy, manufacturing, transport, healthcare, and industrial supply chains.",
    },
    investment: {
      title: "Investment news",
      description: "Capital markets, IPOs, private equity, M&A, funding, and asset flows.",
    },
  };

  const NEWSFEED_CATEGORY_COPY = {
    Investment: "Investment news",
    Tech: "Technology news",
    Politics: "Politics news",
    Industries: "Industry news",
  };

  const NEWSFEED_REGION_COPY = {
    global: "Global coverage",
    mena: "MENA",
    china: "China coverage",
    usa: "United States",
  };

  const NEWSFEED_SUGGESTED_TOPIC_COPY = {
    "Self-driving snow groomers for ski resorts": "Self-driving snow groomers for ski resorts",
    "Satellite-based wildfire early-warning apps": "Satellite-based wildfire early-warning apps",
    "Robotic kitchen systems for home chefs": "Robotic kitchen systems for home chefs",
    "Zero-gravity manufacturing on the ISS": "Zero-gravity manufacturing on the ISS",
    "Middle East capital investing in China": "Middle East capital investing in China",
    "Humanoid robot supply chains": "Humanoid robot supply chains",
  };

  function newsfeedTopicText(topic, field = "title") {
    if (!isLocalizedContentPage()) return String(topic && topic[field] || "");
    const id = String(topic && topic.id || "");
    const builtIn = NEWSFEED_SYSTEM_TOPIC_COPY[id];
    return String(builtIn && builtIn[field] || topic && topic[field] || "");
  }

  function newsfeedCategoryText(value) {
    const clean = String(value || "");
    return isLocalizedContentPage() ? NEWSFEED_CATEGORY_COPY[clean] || clean : clean;
  }

  function newsfeedSuggestedTopicText(value) {
    const clean = String(value || "");
    return isLocalizedContentPage() ? NEWSFEED_SUGGESTED_TOPIC_COPY[clean] || clean : clean;
  }

  function newsfeedTopicUpdatedText(topic) {
    const label = String(topic && (topic.last_updated_label || topic.updated_label) || "");
    if (!isLocalizedContentPage()) return label || String(topic && topic.description || "");
    if (newsfeedSystemTopic(topic) || label === "Latest") return "Latest updates";
    return label ? "Recently updated" : newsfeedTopicText(topic, "description");
  }

  function newsfeedImageMarkup(item) {
    const image = String(item && item.image_url || "").trim();
    if (!image) return "";
    return `<img class="news-story-image" src="${escapeHtml(image)}" alt="">`;
  }

  function newsfeedLogoMarkup(item) {
    const logo = newsfeedLogoUrl(item);
    const label = newsfeedSourceName(item).slice(0, 1).toUpperCase() || "N";
    return logo
      ? `<img class="news-source-logo" src="${escapeHtml(logo)}" alt="">`
      : `<span class="news-source-logo news-source-fallback">${escapeHtml(label)}</span>`;
  }

  function newsfeedSourceStack(items = []) {
    const unique = [];
    const seen = new Set();
    for (const item of items) {
      const key = String(item.domain || item.source || item.source_name || item.id || "");
      if (!key || seen.has(key)) continue;
      seen.add(key);
      unique.push(item);
      if (unique.length >= 5) break;
    }
    if (!unique.length) return "";
    return `
      <div class="news-source-stack" aria-label="Sources">
        ${unique.map(newsfeedLogoMarkup).join("")}
      </div>
    `;
  }

  function newsfeedStoryMeta(item) {
    return [newsfeedTimeLabel(item && item.published_at), newsfeedSourceName(item), newsfeedCategoryText(item && item.category)]
      .filter(Boolean)
      .join(" · ");
  }

  function newsfeedStoryCard(item, index = 0, options = {}) {
    if (!item) return "";
    const id = String(item.id || "");
    const image = newsfeedImageMarkup(item);
    const summary = item.summary ? `<p>${escapeHtml(item.summary)}</p>` : "";
    const className = options.featured ? "news-story is-featured" : "news-story";
    return `
      <button class="${className}" type="button" data-action="open-article" data-id="${escapeHtml(id)}">
        <span class="news-story-rank">${index ? escapeHtml(index) : ""}</span>
        <span class="news-story-main">
          <strong>${escapeHtml(item.title || "Untitled")}</strong>
          ${summary}
          <span class="news-story-meta">${escapeHtml(newsfeedStoryMeta(item))}</span>
        </span>
        ${image}
        <span class="news-story-actions">${newsfeedLogoMarkup(item)}<span>···</span></span>
      </button>
    `;
  }

  function newsfeedSpinnerMarkup(label = "Loading") {
    return `
      <div class="newsfeed-loader" role="status" aria-live="polite">
        <span></span>
        <strong>${escapeHtml(label)}</strong>
      </div>
    `;
  }

  function newsfeedSkeletonMarkup(kind = "home", label = "Preparing Newsfeed") {
    const rows = Array.from({ length: kind === "article" ? 5 : 4 }).map(() => `
      <div class="news-skeleton-row">
        <span></span>
        <span></span>
      </div>
    `).join("");
    return `
      <section class="newsfeed-loading-panel">
        ${newsfeedSpinnerMarkup(label)}
        <div class="news-skeleton-block">
          ${rows}
        </div>
      </section>
    `;
  }

  function newsfeedDigestMarkup(digest = []) {
    const rows = digest.slice(0, 4).map((line) => `<li>${escapeHtml(line)}</li>`).join("");
    return rows || "<li>Fresh digest is loading.</li>";
  }

  function newsfeedTopicIcon(topic) {
    if (topic && topic.pinned) return "◆";
    if (topic && topic.kind === "custom") return "“";
    return "◇";
  }

  function newsfeedTopicRow(topic, state) {
    const id = String(topic && topic.id || "");
    const pin = newsfeedCanCustomize(state)
      ? `<button class="news-topic-pin" type="button" data-action="pin-topic" data-id="${escapeHtml(id)}" aria-label="Pin topic">${topic && topic.pinned ? "●" : "○"}</button>`
      : "";
    return `
      <div class="news-topic-row${pin ? "" : " is-readonly"}" data-topic-id="${escapeHtml(id)}">
        <button class="news-topic-open" type="button" data-action="open-topic" data-id="${escapeHtml(id)}">
          <span>${escapeHtml(newsfeedTopicIcon(topic))}</span>
          <strong>${escapeHtml(newsfeedTopicText(topic) || "Topic")}</strong>
          <small>${escapeHtml(newsfeedTopicUpdatedText(topic))}</small>
        </button>
        ${pin}
      </div>
    `;
  }

  function newsfeedShellMarkup(state) {
    return `
      <section class="newsfeed-layout">
        <aside class="newsfeed-sidebar" id="newsfeedSidebar">
          <div class="newsfeed-profile">
            <span class="newsfeed-avatar">KC</span>
            <strong>${escapeHtml(authUserLabel(loadAuthSession()))}</strong>
          </div>
          <div class="newsfeed-side-actions">
            <button type="button" data-action="show-feed">My feed</button>
            <button type="button" data-action="show-explore">Explore</button>
            <button type="button" data-action="show-email" data-newsfeed-capability="subscribe" hidden>Digest Email</button>
          </div>
          <div id="newsfeedPolicyNotice" class="newsfeed-policy-notice"></div>
          <div class="newsfeed-following">
            <div class="newsfeed-sidebar-heading">
              <span>Following</span>
              <strong id="newsfeedTopicCount">0 topics</strong>
            </div>
            <div id="newsfeedTopicList" class="newsfeed-topic-list"></div>
          </div>
          <button class="newsfeed-add-wide" type="button" data-action="show-add" data-newsfeed-capability="customize" hidden>+ Add Topics</button>
        </aside>
        <section class="newsfeed-main">
          <div class="newsfeed-command">
            <button class="news-icon-button" type="button" data-action="toggle-sidebar" aria-label="Topics">☰</button>
            <h1 id="newsfeedTitle">Daily Digest</h1>
            <div class="newsfeed-audio-actions">
              <button id="newsBriefingButton" class="news-icon-button is-wide" type="button" data-action="play-briefing" aria-label="Audio">▥ ▶</button>
            </div>
          </div>
          <div id="newsfeedPreferences" class="news-preference-bar" hidden></div>
          <div id="newsfeedStatus" class="newsfeed-status" aria-live="polite"></div>
          <div id="newsfeedContent" class="newsfeed-content"></div>
          <div id="newsBriefingPanel" class="news-briefing-panel" hidden></div>
          <nav class="newsfeed-bottom-tabs" aria-label="Newsfeed sections">
            <button type="button" data-action="show-feed" class="is-active"><span>▯</span>My feed</button>
            <button type="button" data-action="show-add" data-newsfeed-capability="customize" hidden><span>＋</span>Add topics</button>
            <button type="button" data-action="show-explore"><span>◇</span>Explore</button>
          </nav>
        </section>
      </section>
    `;
  }

  function renderNewsfeedBoot(app, message = "Checking Newsfeed access...") {
    app.innerHTML = `
      <section class="newsfeed-access is-loading">
        ${newsfeedSpinnerMarkup(message)}
        <p>We are preparing your private Newsfeed workspace.</p>
      </section>
    `;
  }

  async function newsfeedJson(workerUrl, path, options = {}) {
    const response = await fetch(`${workerUrl}${path}`, {
      cache: "no-store",
      ...options,
      headers: {
        ...(options.body ? { "Content-Type": "application/json" } : {}),
        ...authHeaders(),
        ...(options.headers || {}),
      },
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const error = new Error(localizedServiceMessage(data.detail || data.error, "Newsfeed request failed."));
      error.status = response.status;
      error.code = String(data.code || data.stage_code || "");
      error.data = data;
      throw error;
    }
    return data;
  }

  function newsfeedSystemTopic(topic) {
    return NEWSFEED_SYSTEM_TOPIC_IDS.has(String(topic && topic.id || topic || ""));
  }

  function newsfeedCustomTopics(value) {
    return (Array.isArray(value) ? value : []).filter((topic) => topic && !newsfeedSystemTopic(topic));
  }

  function normalizeNewsfeedPolicy(raw = {}, session = null, topics = []) {
    const source = raw && typeof raw === "object" && !Array.isArray(raw) ? raw : {};
    const authenticated = Object.prototype.hasOwnProperty.call(source, "authenticated")
      ? Boolean(source.authenticated)
      : isNewsfeedSession(session);
    const tier = String(source.tier || (isSuperSession(session) ? "super" : authenticated ? "registered" : "anonymous"))
      .trim()
      .toLowerCase();
    const hasExplicitNullLimit = Object.prototype.hasOwnProperty.call(source, "custom_topic_limit")
      && source.custom_topic_limit === null;
    const unlimited = authenticated && (
      isSuperSession(session)
      || tier === "super"
      || tier === "admin"
      || source.custom_topic_limit === "unlimited"
      || hasExplicitNullLimit
    );
    const observedCount = newsfeedCustomTopics(topics).length;
    const rawCount = Number(source.custom_topic_count);
    const customTopicCount = Number.isFinite(rawCount) ? Math.max(0, Math.floor(rawCount)) : observedCount;
    const rawLimit = Number(source.custom_topic_limit);
    const customTopicLimit = unlimited ? null : Number.isFinite(rawLimit) ? Math.max(0, Math.floor(rawLimit)) : 0;
    const rawRemaining = Number(source.custom_topic_remaining);
    const customTopicRemaining = unlimited
      ? null
      : Number.isFinite(rawRemaining)
        ? Math.max(0, Math.floor(rawRemaining))
        : Math.max(0, customTopicLimit - customTopicCount);
    const hasMemberFeatures = authenticated && (unlimited || customTopicLimit > 0);
    return {
      tier,
      authenticated,
      can_customize: authenticated && (hasMemberFeatures || source.can_customize === true || source.can_create_custom === true),
      can_subscribe: authenticated && (hasMemberFeatures || source.can_subscribe === true),
      custom_topic_limit: customTopicLimit,
      custom_topic_count: customTopicCount,
      custom_topic_remaining: customTopicRemaining,
      request_allowed: authenticated && source.request_allowed === true,
      unlimited,
    };
  }

  function applyNewsfeedPolicy(state, payload = {}) {
    const declared = payload && (payload.policy || payload.topic_policy);
    const usage = payload && payload.custom_topics && typeof payload.custom_topics === "object"
      ? payload.custom_topics
      : {};
    const raw = declared && typeof declared === "object" ? { ...declared } : {};
    if (raw.can_customize === undefined && raw.can_create_custom !== undefined) raw.can_customize = raw.can_create_custom;
    if (raw.custom_topic_count === undefined) {
      raw.custom_topic_count = Object.prototype.hasOwnProperty.call(payload, "custom_topic_count")
        ? payload.custom_topic_count
        : usage.count;
    }
    if (raw.custom_topic_limit === undefined) {
      raw.custom_topic_limit = Object.prototype.hasOwnProperty.call(payload, "custom_topic_limit")
        ? payload.custom_topic_limit
        : usage.limit;
    }
    if (raw.custom_topic_remaining === undefined) {
      raw.custom_topic_remaining = Object.prototype.hasOwnProperty.call(payload, "custom_topic_remaining")
        ? payload.custom_topic_remaining
        : usage.remaining;
    }
    if (raw.request_allowed === undefined) raw.request_allowed = payload.request_available;
    const hasPolicyFields = Object.values(raw).some((value) => value !== undefined);
    if (!hasPolicyFields && state.policy) return state.policy;
    state.policy = normalizeNewsfeedPolicy(raw, state.session, state.topics);
    return state.policy;
  }

  function newsfeedCanCustomize(state) {
    return Boolean(state && state.policy && state.policy.can_customize);
  }

  function newsfeedCanSubscribe(state) {
    return Boolean(state && state.policy && state.policy.can_subscribe);
  }

  function newsfeedCanOpenAdd(state) {
    return Boolean(state && state.policy && (state.policy.can_customize || state.policy.request_allowed));
  }

  function newsfeedCanCreateTopic(state) {
    if (!newsfeedCanCustomize(state)) return false;
    return Boolean(state.policy.unlimited || Number(state.policy.custom_topic_remaining) > 0);
  }

  function newsfeedShouldShowRequest(state) {
    return Boolean(
      state
      && state.policy
      && state.policy.authenticated
      && state.policy.request_allowed
      && !newsfeedCanCreateTopic(state)
    );
  }

  function newsfeedVisibleTopics(state, topics = state && state.topics || []) {
    const rows = Array.isArray(topics) ? topics : [];
    if (state && state.policy && state.policy.authenticated && newsfeedCanCustomize(state)) return rows;
    return rows.filter(newsfeedSystemTopic).slice(0, NEWSFEED_SYSTEM_TOPIC_IDS.size);
  }

  function newsfeedTopicAnalyticsKey(value) {
    let hash = 2166136261;
    const text = String(value || "");
    for (let index = 0; index < text.length; index += 1) {
      hash ^= text.charCodeAt(index);
      hash = Math.imul(hash, 16777619);
    }
    return `topic-${(hash >>> 0).toString(36)}`;
  }

  function newsfeedTopicAnalyticsFields(topic) {
    const id = String(topic && topic.id || topic || "").trim();
    if (NEWSFEED_SYSTEM_TOPIC_IDS.has(id)) return { topic_kind: "system", topic_id: id };
    return id ? { topic_kind: "custom", topic_hash: newsfeedTopicAnalyticsKey(id) } : {};
  }

  function trackNewsfeedInteraction(state, action, details = {}) {
    const policy = state && state.policy || {};
    const safe = {
      action: String(action || "interaction").slice(0, 64),
      access_state: policy.authenticated ? "authenticated" : "anonymous",
      view: String(details.view || state && state.currentView || "feed").slice(0, 32),
      tier: String(policy.tier || (policy.authenticated ? "registered" : "anonymous")).slice(0, 32),
      count: Math.max(0, Math.floor(Number(policy.custom_topic_count) || 0)),
      limit: policy.unlimited || policy.custom_topic_limit === null
        ? null
        : Math.max(0, Math.floor(Number(policy.custom_topic_limit) || 0)),
      custom_topic_remaining: policy.unlimited || policy.custom_topic_remaining === null
        ? null
        : Math.max(0, Math.floor(Number(policy.custom_topic_remaining) || 0)),
    };
    for (const key of ["outcome", "category", "language", "provider", "reason", "latency_bucket"]) {
      if (details[key] !== undefined && details[key] !== null) safe[key] = String(details[key]).slice(0, 80);
    }
    for (const key of ["region_count", "item_count", "custom_topic_remaining"]) {
      if (details[key] !== undefined && details[key] !== null && Number.isFinite(Number(details[key]))) {
        safe[key] = Math.max(0, Math.floor(Number(details[key])));
      }
    }
    if (details.topic !== undefined) Object.assign(safe, newsfeedTopicAnalyticsFields(details.topic));
    if (details.requested_topic !== undefined) {
      safe.topic_kind = "custom";
      safe.topic_hash = newsfeedTopicAnalyticsKey(details.requested_topic);
      delete safe.topic_id;
    }
    trackEvent(state && state.workerUrl || "", "newsfeed_interaction", safe);
  }

  function newsfeedPolicyNoticeMarkup(state) {
    const policy = state && state.policy || normalizeNewsfeedPolicy();
    const count = policy.custom_topic_count || 0;
    if (!policy.authenticated) {
      return `
        <strong>General · 公开浏览</strong>
        <span>当前可浏览 5 个内置话题；自定义话题 0 个。</span>
        <button type="button" data-action="show-login">登录 / 查看会员权益</button>
      `;
    }
    if (policy.unlimited) return `<strong>自定义话题不限量</strong><span>已创建 ${escapeHtml(count)} 个。</span>`;
    if (newsfeedCanCustomize(state)) {
      return `<strong>自定义话题 ${escapeHtml(count)}/${escapeHtml(policy.custom_topic_limit || 0)}</strong><span>还可创建 ${escapeHtml(policy.custom_topic_remaining || 0)} 个。</span>`;
    }
    return `
      <strong>General · 会员功能未开启</strong>
      <span>当前自定义话题 0 个；升级后可创建话题并订阅邮件。</span>
      <button type="button" data-action="show-account">查看会员权益</button>
    `;
  }

  function renderNewsfeedAccess(app, workerUrl, message = "请登录已注册且状态正常的账号继续。") {
    app.innerHTML = `
      <section class="newsfeed-access">
        <h1>Newsfeed</h1>
        <p>${escapeHtml(message)}</p>
        <button id="newsfeedLogin" class="primary" type="button">登录 / 账号</button>
      </section>
    `;
    const login = document.getElementById("newsfeedLogin");
    if (login) login.addEventListener("click", () => showAccountModal(workerUrl));
  }

  function setNewsfeedStatus(text, kind) {
    const status = document.getElementById("newsfeedStatus");
    if (!status) return;
    status.className = kind ? `newsfeed-status ${kind}` : "newsfeed-status";
    status.textContent = text || "";
  }

  function renderNewsfeedContentLoading(label, kind = "home") {
    const content = document.getElementById("newsfeedContent");
    if (content) content.innerHTML = newsfeedSkeletonMarkup(kind, label);
    setNewsfeedStatus(label, "loading");
  }

  function setNewsfeedTitle(text) {
    const title = document.getElementById("newsfeedTitle");
    if (title) title.textContent = text || "Newsfeed";
  }

  function refreshNewsfeedChrome(state) {
    const sideFeed = document.querySelector(".newsfeed-side-actions [data-action='show-feed']");
    const sideExplore = document.querySelector(".newsfeed-side-actions [data-action='show-explore']");
    const sideEmail = document.querySelector(".newsfeed-side-actions [data-action='show-email']");
    if (sideFeed) sideFeed.textContent = newsfeedText(state, "myFeed");
    if (sideExplore) sideExplore.textContent = newsfeedText(state, "explore");
    if (sideEmail) sideEmail.textContent = newsfeedText(state, "digestEmail");
    const bottomFeed = document.querySelector(".newsfeed-bottom-tabs [data-action='show-feed']");
    const bottomAdd = document.querySelector(".newsfeed-bottom-tabs [data-action='show-add']");
    const bottomExplore = document.querySelector(".newsfeed-bottom-tabs [data-action='show-explore']");
    const addWide = document.querySelector(".newsfeed-add-wide[data-action='show-add']");
    const preferences = document.getElementById("newsfeedPreferences");
    const policyNotice = document.getElementById("newsfeedPolicyNotice");
    const bottomTabs = document.querySelector(".newsfeed-bottom-tabs");
    const sideActions = document.querySelector(".newsfeed-side-actions");
    const canOpenAdd = newsfeedCanOpenAdd(state);
    const canSubscribe = newsfeedCanSubscribe(state);
    if (bottomFeed) bottomFeed.innerHTML = `<span>▯</span>${escapeHtml(newsfeedText(state, "myFeed"))}`;
    if (bottomAdd) bottomAdd.innerHTML = `<span>＋</span>${escapeHtml(newsfeedText(state, "addTopics"))}`;
    if (bottomExplore) bottomExplore.innerHTML = `<span>◇</span>${escapeHtml(newsfeedText(state, "explore"))}`;
    if (sideEmail) sideEmail.hidden = !canSubscribe;
    if (bottomAdd) bottomAdd.hidden = !canOpenAdd;
    if (addWide) addWide.hidden = !canOpenAdd;
    if (bottomTabs) bottomTabs.classList.toggle("is-public", !canOpenAdd);
    if (sideActions) sideActions.classList.toggle("is-public", !canSubscribe);
    if (preferences) preferences.hidden = !(newsfeedCanCustomize(state) || canSubscribe);
    if (policyNotice) policyNotice.innerHTML = newsfeedPolicyNoticeMarkup(state);
    const audio = document.getElementById("newsBriefingButton");
    if (audio) {
      audio.setAttribute("aria-label", newsfeedText(state, "playBriefing"));
      audio.hidden = !(state.policy && state.policy.authenticated);
    }
    renderNewsfeedPreferences(state);
  }

  function updateNewsfeedTabs(view) {
    document.querySelectorAll(".newsfeed-bottom-tabs button").forEach((button) => {
      const action = button.dataset.action || "";
      button.classList.toggle(
        "is-active",
        (view === "feed" && action === "show-feed") ||
          (view === "add" && action === "show-add") ||
          (view === "explore" && action === "show-explore") ||
          (view === "email" && action === "show-email"),
      );
    });
  }

  function normalizeNewsfeedRegionsClient(value) {
    const raw = Array.isArray(value) ? value : String(value || "").split(",");
    const out = [];
    const seen = new Set();
    for (const item of raw) {
      const clean = String(item && (item.value || item) || "").trim().slice(0, 54);
      const key = clean.toLowerCase();
      if (!clean || seen.has(key)) continue;
      seen.add(key);
      out.push(clean);
      if (out.length >= 8) break;
    }
    return out.length ? out : ["global"];
  }

  function newsfeedRegionOptions(state) {
    const defaults = [
      { value: "global", label: "Global" },
      { value: "mena", label: "MENA" },
      { value: "china", label: "China" },
      { value: "usa", label: "USA" },
    ];
    const options = (Array.isArray(state.regionOptions) && state.regionOptions.length ? state.regionOptions : defaults)
      .map((item) => ({
        ...item,
        label: isLocalizedContentPage()
          ? NEWSFEED_REGION_COPY[String(item && item.value || "")] || item.label
          : item.label,
      }));
    const selected = normalizeNewsfeedRegionsClient(state.preferredRegions);
    const custom = selected
      .filter((value) => !options.some((item) => item.value === value))
      .map((value) => ({ value, label: value }));
    return [...options, ...custom];
  }

  function newsfeedRegionLabel(state, value) {
    const option = newsfeedRegionOptions(state).find((item) => item.value === value);
    return option ? option.label : value;
  }

  function newsfeedPreferenceQuery(state, options = {}) {
    const params = new URLSearchParams();
    if (options.force || state.preferencesReady) {
      normalizeNewsfeedRegionsClient(state.preferredRegions).forEach((region) => params.append("regions", region));
      params.set("language", newsfeedFixedInterfaceLanguage()
        || newsfeedLanguageCode(state.interfaceLanguage || state.outputLanguage || "en"));
      const regions = params.getAll("regions");
      params.delete("regions");
      params.set("regions", regions.join(","));
    }
    return params.toString();
  }

  function applyNewsfeedSettings(state, settings = {}) {
    state.settings = settings || state.settings || {};
    const fixedInterfaceLanguage = newsfeedFixedInterfaceLanguage();
    if (fixedInterfaceLanguage) {
      state.interfaceLanguage = fixedInterfaceLanguage;
      state.outputLanguage = newsfeedLanguageCode(settings.digest_language || state.outputLanguage || fixedInterfaceLanguage);
    } else {
      state.interfaceLanguage = newsfeedLanguageCode(settings.interface_language || state.interfaceLanguage || "en");
      state.outputLanguage = newsfeedLanguageCode(settings.interface_language || state.outputLanguage || settings.digest_language || "en");
    }
    state.preferredRegions = normalizeNewsfeedRegionsClient(settings.preferred_regions || state.preferredRegions || ["global"]);
    state.preferencesReady = true;
  }

  function newsfeedLanguageOptions(selected = "en") {
    const languages = [
      ["en", "English"],
      ["zh-CN", "中文"],
      ["ja", "日本語"],
      ["ko", "한국어"],
    ];
    if (isLocalizedContentPage()) languages.push(["ar", "العربية"]);
    return languages.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedInterfaceLanguageOptions(selected = "en") {
    if (!newsfeedFixedInterfaceLanguage()) return newsfeedLanguageOptions(selected);
    const languages = [
      ["zh-CN", "中文"],
      ["ja", "日本語"],
      ["ko", "한국어"],
      ["ar", "العربية"],
    ];
    return languages.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedTimezoneOptions(selected = "Asia/Shanghai") {
    const timezones = [
      ["Asia/Shanghai", "China / Singapore"],
      ["America/New_York", "New York"],
      ["Europe/London", "London"],
      ["UTC", "UTC"],
    ];
    return timezones.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedNewsletterOptions(state, selected = "") {
    const topics = Array.isArray(state.topics) ? state.topics : [];
    const options = [`<option value="">${escapeHtml(newsfeedText(state, "noNewsletter"))}</option>`];
    const seen = new Set();
    for (const topic of topics) {
      const id = String(topic && topic.id || "").trim();
      if (!id || seen.has(id)) continue;
      seen.add(id);
      options.push(`<option value="${escapeHtml(id)}" ${id === selected ? "selected" : ""}>${escapeHtml(newsfeedTopicText(topic) || id)}</option>`);
    }
    return options.join("");
  }

  function newsfeedEmailPayloadFromForm(state) {
    const newsletterTopicId = document.getElementById("newsNewsletterTopic")?.value || "";
    return {
      digest_email_enabled: Boolean(newsletterTopicId && document.getElementById("newsEmailEnabled")?.checked),
      newsletter_topic_id: newsletterTopicId,
      digest_send_time: document.getElementById("newsEmailTime")?.value || "09:00",
      digest_timezone: document.getElementById("newsEmailTimezone")?.value || "Asia/Shanghai",
      digest_language: document.getElementById("newsEmailLanguage")?.value || state.outputLanguage || "en",
      interface_language: newsfeedFixedInterfaceLanguage() || state.interfaceLanguage || "en",
      preferred_regions: state.preferredRegions || ["global"],
    };
  }

  function newsfeedEmailLastStatus(settings = {}) {
    const result = String(settings.digest_last_send_result || "").trim();
    if (!result) return "";
    const at = settings.digest_last_attempt_at || settings.digest_last_sent_at || "";
    const when = at ? newsfeedTimeLabel(at) : "";
    const visibleResult = localizedServiceMessage(result, "Email delivery status updated.");
    const detail = settings.digest_last_send_detail
      ? ` · ${localizedServiceMessage(settings.digest_last_send_detail, "Email delivery details are unavailable.")}`
      : "";
    return `Last email attempt: ${visibleResult}${when ? ` · ${when}` : ""}${detail}`;
  }

  function renderNewsfeedPreferences(state) {
    const mount = document.getElementById("newsfeedPreferences");
    if (!mount) return;
    if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) {
      mount.hidden = true;
      mount.innerHTML = "";
      return;
    }
    mount.hidden = false;
    const selected = normalizeNewsfeedRegionsClient(state.preferredRegions);
    const selectedLabels = selected.map((value) => newsfeedRegionLabel(state, value)).join(", ");
    const options = newsfeedRegionOptions(state);
    mount.innerHTML = `
      <div class="news-region-picker">
        <button id="newsRegionToggle" type="button" data-action="toggle-region-menu" aria-expanded="false">
          <span>${escapeHtml(newsfeedText(state, "regions"))}</span>
          <strong>${escapeHtml(selectedLabels || "Global")}</strong>
          <span>▾</span>
        </button>
        <div id="newsRegionMenu" class="news-region-menu" hidden>
          ${options.map((item) => `
            <label>
              <input type="checkbox" data-action="region-checkbox" value="${escapeHtml(item.value)}" ${selected.includes(item.value) ? "checked" : ""}>
              <span>${escapeHtml(item.label)}</span>
            </label>
          `).join("")}
          <form id="newsCustomRegionForm" class="news-custom-region-form">
            <input id="newsCustomRegionInput" type="text" placeholder="${escapeHtml(newsfeedText(state, "customRegion"))}">
            <button type="submit">${escapeHtml(newsfeedText(state, "addRegion"))}</button>
          </form>
        </div>
      </div>
      <label class="news-inline-select">
        <span>${escapeHtml(newsfeedText(state, "language"))}</span>
        <select id="newsInterfaceLanguage">${newsfeedInterfaceLanguageOptions(state.interfaceLanguage || "en")}</select>
      </label>
    `;
  }

  function renderNewsfeedEmailSettings(state) {
    if (!newsfeedCanSubscribe(state)) {
      return `<section class="newsfeed-policy-card">${newsfeedPolicyNoticeMarkup(state)}</section>`;
    }
    const settings = state.settings || {};
    const session = loadAuthSession();
    const fallbackEmail = session && session.user && !session.user.email_is_generated ? session.user.email : "";
    const email = settings.digest_email || fallbackEmail || "";
    const enabled = Boolean(settings.digest_email_enabled);
    const newsletterTopicId = enabled ? String(settings.newsletter_topic_id || "global-daily") : "";
    const providerNote = settings.email_provider_configured === false
      ? (state.interfaceLanguage === "zh-CN"
        ? "邮件服务还没配置好，请先配置 Brevo API key。"
        : "Email sender is not configured yet. Add the Brevo API key first.")
      : (settings.email_provider === "brevo"
        ? (state.interfaceLanguage === "zh-CN"
          ? "Brevo 邮件服务已连接；保存后可立即发送 newsletter。"
          : "Brevo email is connected. Save, then send a newsletter now.")
        : (state.interfaceLanguage === "zh-CN"
          ? "Cloudflare 邮件服务已连接；保存后可立即发送 newsletter。"
          : "Cloudflare email is connected. Save, then send a newsletter now."));
    const lastStatus = newsfeedEmailLastStatus(settings);
    return `
      <section class="news-email-settings">
        <div class="news-email-copy">
          <h2>${escapeHtml(newsfeedText(state, "digestEmail"))}</h2>
          <p>${state.interfaceLanguage === "zh-CN" ? "每天定点发送最新摘要到邮箱。" : "Send the latest Daily Digest to your inbox once a day."}</p>
        </div>
        <form id="newsEmailForm" class="news-email-form">
          <label>${escapeHtml(newsfeedText(state, "email"))}
            <input id="newsEmailInput" type="email" autocomplete="email" value="${escapeHtml(email)}" readonly aria-readonly="true">
          </label>
          <label>${escapeHtml(newsfeedText(state, "newsletterTopic"))}
            <select id="newsNewsletterTopic">${newsfeedNewsletterOptions(state, newsletterTopicId)}</select>
          </label>
          <label>${escapeHtml(newsfeedText(state, "sendTime"))}
            <input id="newsEmailTime" type="time" value="${escapeHtml(settings.digest_send_time || "09:00")}">
          </label>
          <label>${escapeHtml(newsfeedText(state, "timezone"))}
            <select id="newsEmailTimezone">${newsfeedTimezoneOptions(settings.digest_timezone || "Asia/Shanghai")}</select>
          </label>
          <label>${escapeHtml(newsfeedText(state, "language"))}
            <select id="newsEmailLanguage">${newsfeedLanguageOptions(settings.digest_language || state.outputLanguage || "en")}</select>
          </label>
          <label class="news-toggle-row">
            <input id="newsEmailEnabled" type="checkbox" ${enabled ? "checked" : ""}>
            <span>${escapeHtml(newsfeedText(state, "sendDailyDigest"))} · ${state.interfaceLanguage === "zh-CN" ? "每个账号最多订阅一个，可随时取消或替换" : "one newsletter per account; cancel or replace it anytime"}</span>
          </label>
          <button id="newsEmailSubmit" class="primary" type="submit">${escapeHtml(newsfeedText(state, "saveEmail"))}</button>
          <button id="newsEmailSend" class="primary news-email-test" type="button" data-action="send-email-now">${escapeHtml(newsfeedText(state, "sendNewsletterNow"))}</button>
          <button id="newsEmailTest" class="secondary-button news-email-test" type="button" data-action="send-email-test">${escapeHtml(newsfeedText(state, "sendTestNow"))}</button>
        </form>
        <div id="newsEmailStatus" class="status-line" aria-live="polite">${escapeHtml(lastStatus || providerNote)}</div>
      </section>
    `;
  }

  function rememberNewsfeedArticles(state, items = [], topic = null) {
    for (const item of items || []) {
      if (!item || !item.id) continue;
      const id = String(item.id);
      const outputLanguage = item.output_language || topic && topic.output_language || state.outputLanguage || "en";
      state.articles.set(id, item);
      if (state.articleLanguages) state.articleLanguages.set(id, outputLanguage);
    }
  }

  function renderNewsfeedSidebar(state) {
    const list = document.getElementById("newsfeedTopicList");
    const count = document.getElementById("newsfeedTopicCount");
    if (!list) return;
    const topics = [...newsfeedVisibleTopics(state)].sort((a, b) => Number(Boolean(b.pinned)) - Number(Boolean(a.pinned)));
    list.innerHTML = topics.map((topic) => newsfeedTopicRow(topic, state)).join("") || '<div class="newsfeed-empty">No topics yet.</div>';
    if (count) {
      const policy = state.policy || normalizeNewsfeedPolicy();
      count.textContent = policy.unlimited
        ? `${policy.custom_topic_count || 0} custom · unlimited`
        : `${policy.custom_topic_count || 0}/${policy.custom_topic_limit || 0} custom`;
    }
  }

  function renderNewsfeedHome(state) {
    const home = state.home || {};
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    setNewsfeedTitle(newsfeedText(state, "dailyDigest"));
    updateNewsfeedTabs("feed");
    state.currentView = "feed";
    state.topics = newsfeedVisibleTopics(state, home.topics || state.topics || []);
    rememberNewsfeedArticles(state, home.highlights || []);
    rememberNewsfeedArticles(state, home.headlines || []);
    renderNewsfeedSidebar(state);
    const category = state.homeCategory || "Investment";
    const categories = home.categories || ["Investment", "Tech", "Politics", "Industries"];
    const filtered = (home.headlines || []).filter((item) => !category || item.category === category);
    const visible = filtered.length ? filtered : (home.headlines || []);
    content.innerHTML = `
      <section class="news-digest-panel">
        <div>
          <div class="news-section-kicker">${escapeHtml(newsfeedText(state, "dailyDigest"))} <span>${escapeHtml(String(home.digest_count || 0).padStart(2, "0"))}</span></div>
          <ul>${newsfeedDigestMarkup(home.daily_digest)}</ul>
        </div>
        ${newsfeedSourceStack(home.highlights || [])}
      </section>
      <section class="newsfeed-section">
        <div class="newsfeed-section-heading">
          <h2>${escapeHtml(newsfeedText(state, "topHeadlines"))}</h2>
          <span>${escapeHtml(isLocalizedContentPage() ? newsfeedTimeLabel(home.updated_at) : home.updated_label || "")}</span>
        </div>
        <div class="news-category-tabs">
          ${categories.map((item) => `
            <button type="button" data-action="home-category" data-category="${escapeHtml(item)}" class="${item === category ? "is-active" : ""}">${escapeHtml(newsfeedCategoryText(item))}</button>
          `).join("")}
        </div>
        <div class="news-story-list">
          ${visible.slice(0, 12).map((item, index) => newsfeedStoryCard(item, index + 1)).join("") || `<div class="newsfeed-empty">${escapeHtml(newsfeedText(state, "noHeadlines"))}</div>`}
        </div>
      </section>
    `;
  }

  function renderNewsfeedAdd(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    const home = state.home || {};
    const policy = state.policy || normalizeNewsfeedPolicy();
    const suggestions = home.suggested_topics || [];
    setNewsfeedTitle(newsfeedText(state, "addTopics"));
    updateNewsfeedTabs("add");
    state.currentView = "add";
    if (!newsfeedCanCreateTopic(state)) {
      const requestedTopic = String(state.pendingRequestedTopic || "").trim().slice(0, 600);
      const requestForm = policy.request_allowed ? `
        <form id="newsTopicRequestForm" class="news-topic-request-form">
          <label for="newsTopicRequestInput">希望继续追踪的话题</label>
          <textarea id="newsTopicRequestInput" rows="4" maxlength="600" required>${escapeHtml(requestedTopic)}</textarea>
          <label for="newsTopicRequestLanguage">输出语言</label>
          <select id="newsTopicRequestLanguage">${newsfeedLanguageOptions(state.outputLanguage || "en")}</select>
          <label class="news-topic-request-honeypot" aria-hidden="true">请勿填写<input id="newsTopicRequestHoneypot" type="text" tabindex="-1" autocomplete="off"></label>
          <label class="news-topic-request-confirm"><input id="newsTopicRequestConfirm" type="checkbox" required> 我确认提交此话题申请，由团队人工审核后处理。</label>
          <button id="newsTopicRequestSubmit" class="primary" type="submit">确认提交申请</button>
          <p id="newsTopicRequestStatus" class="status-line" role="status" aria-live="polite"></p>
        </form>
      ` : `<button class="primary" type="button" data-action="show-account">查看会员权益</button>`;
      content.innerHTML = `
        <section class="news-add-panel news-topic-limit-panel">
          <div class="news-add-meta">
            <strong>自定义话题额度已用完</strong>
            <span>已创建 ${escapeHtml(policy.custom_topic_count || 0)}/${escapeHtml(policy.custom_topic_limit || 0)} 个；不会自动提交申请。</span>
          </div>
          <p>如需继续创建，请确认具体话题后提交申请。</p>
          ${requestForm}
        </section>
      `;
      return;
    }
    content.innerHTML = `
      <section class="news-add-panel">
        <div class="news-add-meta">
          <strong>${policy.unlimited ? `${escapeHtml(policy.custom_topic_count || 0)} custom · unlimited` : `${escapeHtml(policy.custom_topic_count || 0)}/${escapeHtml(policy.custom_topic_limit || 0)} custom topics`}</strong>
          <span>${policy.unlimited ? escapeHtml(newsfeedText(state, "suggestedTopics")) : `还可创建 ${escapeHtml(policy.custom_topic_remaining || 0)} 个`}</span>
        </div>
        <div class="news-suggested-list">
          ${suggestions.map((topic) => `<button type="button" data-action="suggest-topic" data-topic="${escapeHtml(topic)}">${escapeHtml(newsfeedSuggestedTopicText(topic))}</button>`).join("")}
        </div>
        <div class="news-language-row">
          <label for="newsTopicLanguage">${escapeHtml(newsfeedText(state, "outputLanguage"))}</label>
          <select id="newsTopicLanguage">
            ${newsfeedLanguageOptions(state.outputLanguage || "en")}
          </select>
        </div>
        <div id="newsTopicStatus" class="status-line" aria-live="polite"></div>
        <form id="newsTopicForm" class="news-topic-form">
          <textarea id="newsTopicInput" rows="4" placeholder="Type any topic you want to follow"></textarea>
          <button id="newsTopicSubmit" class="primary" type="submit" aria-label="Create topic">↑</button>
        </form>
        ${newsfeedCanSubscribe(state) ? renderNewsfeedEmailSettings(state) : ""}
      </section>
    `;
  }

  function renderNewsfeedExplore(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    const explore = state.explore || {};
    const categories = explore.categories || ["Tech", "Industries", "Investment", "Politics"];
    const category = state.exploreCategory || categories[0] || "";
    const items = (explore.items || []).filter((item) => !category || item.category === category);
    rememberNewsfeedArticles(state, explore.items || []);
    setNewsfeedTitle(newsfeedText(state, "explore"));
    updateNewsfeedTabs("explore");
    state.currentView = "explore";
    content.innerHTML = `
      <section class="newsfeed-section">
        <div class="news-category-tabs news-category-tabs-large">
          ${categories.map((item) => `
            <button type="button" data-action="explore-category" data-category="${escapeHtml(item)}" class="${item === category ? "is-active" : ""}">${escapeHtml(newsfeedCategoryText(item))}</button>
          `).join("")}
        </div>
        <div class="news-story-list news-story-list-cards">
          ${items.slice(0, 24).map((item, index) => newsfeedStoryCard(item, index + 1)).join("") || '<div class="newsfeed-empty">No stories yet.</div>'}
        </div>
      </section>
    `;
  }

  function renderNewsfeedEmailView(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    setNewsfeedTitle(newsfeedText(state, "digestEmail"));
    updateNewsfeedTabs("email");
    state.currentView = "email";
    content.innerHTML = renderNewsfeedEmailSettings(state);
  }

  function renderNewsfeedTopic(state, topic, items) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    rememberNewsfeedArticles(state, items || [], topic);
    const topicTitle = newsfeedTopicText(topic) || "Topic";
    const topicDescription = newsfeedTopicText(topic, "description");
    setNewsfeedTitle(topicTitle);
    updateNewsfeedTabs("topic");
    state.currentView = "topic";
    state.currentTopic = topic;
    state.currentTopicItems = items || [];
    content.innerHTML = `
      <section class="news-topic-hero">
        <div>
          <span class="news-topic-mark">“</span>
          <h2>${escapeHtml(topicTitle)}</h2>
          <p>${escapeHtml(topicDescription)}</p>
        </div>
        <div class="news-topic-source-line">
          <span>Sources</span>
          ${newsfeedSourceStack(items || [])}
        </div>
      </section>
      <section class="newsfeed-section">
        <div class="newsfeed-section-heading">
          <h2>Top Stories</h2>
          <span>${escapeHtml(newsfeedTopicUpdatedText(topic))}</span>
        </div>
        <div class="news-story-list news-story-list-cards">
          ${(items || []).slice(0, 24).map((item, index) => newsfeedStoryCard(item, index + 1, { featured: index === 0 })).join("") || '<div class="newsfeed-empty">No stories yet.</div>'}
        </div>
      </section>
    `;
  }

  async function renderNewsfeedArticle(state, article) {
    const content = document.getElementById("newsfeedContent");
    if (!content || !article) return;
    state.currentView = "article";
    setNewsfeedTitle("Story");
    updateNewsfeedTabs("article");
    content.innerHTML = `
      <article class="news-article-detail">
        <button class="news-icon-button" type="button" data-action="article-back" aria-label="Back">‹</button>
        <header>
          <div>
            <h2>${escapeHtml(article.title || "Untitled")}</h2>
            <p>${escapeHtml(newsfeedStoryMeta(article))}</p>
          </div>
          ${article.image_url ? `<img src="${escapeHtml(article.image_url)}" alt="">` : newsfeedLogoMarkup(article)}
        </header>
        <div class="news-article-source">
          ${newsfeedLogoMarkup(article)}
          <span>${escapeHtml(newsfeedSourceName(article))}</span>
          ${article.url ? `<a href="${escapeHtml(article.url)}" target="_blank" rel="noopener noreferrer">Source</a>` : ""}
        </div>
        <div class="news-article-tabs">
          <button type="button" class="is-active">Narrative</button>
          <button type="button">Structured</button>
        </div>
        <section class="news-article-stream">
          <h3>Summary</h3>
          <div id="newsArticleSummary" class="news-stream-text"></div>
          <h3>Narrative</h3>
          <div id="newsArticleNarrative" class="news-stream-text"></div>
        </section>
      </article>
    `;
    await streamNewsfeedArticle(state, article);
  }

  async function streamNewsfeedArticle(state, article) {
    const summary = document.getElementById("newsArticleSummary");
    const narrative = document.getElementById("newsArticleNarrative");
    if (!summary || !narrative) return;
    if (!(state.policy && state.policy.authenticated)) {
      summary.textContent = article.summary || "打开原始来源查看完整报道。";
      narrative.textContent = "登录并开通会员后，可生成结构化摘要与语音简报。";
      return;
    }
    summary.textContent = "Generating summary...";
    narrative.textContent = "Writing narrative...";
    try {
      const response = await fetch(`${state.workerUrl}/newsfeed/article`, {
        method: "POST",
        cache: "no-store",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ article }),
      });
      if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(localizedServiceMessage(data.detail, "Could not load story."));
      }
      if (!response.body) {
        const data = await response.json();
        summary.textContent = data.summary || "";
        narrative.textContent = data.narrative || "";
        return;
      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      summary.textContent = "";
      narrative.textContent = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";
        for (const line of lines) {
          if (!line.trim()) continue;
          const event = JSON.parse(line);
          if (event.type === "summary") summary.textContent += event.text || "";
          if (event.type === "narrative") narrative.textContent += event.text || "";
        }
      }
    } catch (error) {
      narrative.textContent = localizedServiceMessage(error.message, "Could not load story.");
    }
  }

  function newsfeedBriefingItems(state) {
    if (state.currentView === "topic") return state.currentTopicItems || [];
    if (state.currentView === "explore") return state.explore && state.explore.items || [];
    return state.home && state.home.headlines || [];
  }

  function renderNewsfeedBriefingPanel(state, options = {}) {
    const panel = document.getElementById("newsBriefingPanel");
    if (!panel) return;
    const items = newsfeedBriefingItems(state).slice(0, 5);
    const first = items[0] || {};
    const progress = Math.max(0, Math.min(100, options.progress || 0));
    panel.hidden = false;
    panel.innerHTML = `
      <div class="news-briefing-head">
        <div>
          <strong>${escapeHtml(options.countText || "0/5 stories listened today")}</strong>
          <span>${escapeHtml(options.status || newsfeedText(state, "playBriefing"))}</span>
        </div>
        <button class="news-icon-button" type="button" data-action="close-briefing" aria-label="Close">×</button>
      </div>
      <div class="news-briefing-now">
        <div>
          <span>${escapeHtml(newsfeedText(state, "nowPlaying"))}</span>
          <h2>${escapeHtml(first.title || newsfeedText(state, "dailyDigest"))}</h2>
          ${first.id ? `<button type="button" data-action="open-article" data-id="${escapeHtml(first.id)}">${escapeHtml(newsfeedText(state, "readStory"))}</button>` : ""}
        </div>
        ${first.image_url ? `<img src="${escapeHtml(first.image_url)}" alt="">` : newsfeedLogoMarkup(first)}
      </div>
      <div class="news-briefing-playlist">
        <h3>${escapeHtml(newsfeedText(state, "playlist"))}</h3>
        ${items.slice(0, 4).map((item) => `
          <button type="button" data-action="open-article" data-id="${escapeHtml(item.id || "")}">
            <span>${escapeHtml(item.title || "Story")}</span>
            ${item.image_url ? `<img src="${escapeHtml(item.image_url)}" alt="">` : ""}
          </button>
        `).join("")}
      </div>
      <div class="news-briefing-player">
        <div class="news-briefing-progress"><span style="width:${progress}%"></span></div>
        <div class="news-briefing-controls">
          <button type="button" data-action="briefing-prev">‹</button>
          <button type="button" data-action="play-briefing" class="is-primary">${options.playing ? "❚❚" : "▶"}</button>
          <button type="button" data-action="briefing-next">›</button>
        </div>
        <small>${escapeHtml(options.voiceLabel || "browser speech")}</small>
      </div>
    `;
  }

  function stopNewsfeedBriefing(state) {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (state.briefingTimer) window.clearInterval(state.briefingTimer);
    state.briefingTimer = null;
    state.briefingPlaying = false;
    const button = document.getElementById("newsBriefingButton");
    if (button) {
      button.classList.remove("is-playing", "is-loading");
      button.innerHTML = "▥ ▶";
    }
  }

  async function playNewsfeedBriefing(state) {
    const button = document.getElementById("newsBriefingButton");
    if (state.briefingPlaying) {
      stopNewsfeedBriefing(state);
      renderNewsfeedBriefingPanel(state, { status: "Paused", progress: state.briefingProgress || 0 });
      return;
    }
    const items = newsfeedBriefingItems(state).slice(0, 8);
    if (!items.length) {
      renderNewsfeedBriefingPanel(state, { status: "No stories ready yet" });
      return;
    }
    if (button) {
      button.classList.add("is-loading");
      button.innerHTML = "▥ …";
    }
    renderNewsfeedBriefingPanel(state, { status: "Preparing audio briefing...", playing: true });
    try {
      const data = await newsfeedJson(state.workerUrl, "/newsfeed/briefing", {
        method: "POST",
        body: JSON.stringify({
          language: state.interfaceLanguage || state.outputLanguage || "en",
          digest: state.home && state.home.daily_digest || [],
          items,
        }),
      });
      const script = data.script || "";
      state.briefingScript = script;
      state.briefingProgress = 0;
      if (!("speechSynthesis" in window) || !script) {
        renderNewsfeedBriefingPanel(state, { status: script || "Audio is not available in this browser.", progress: 100 });
        return;
      }
      stopNewsfeedBriefing(state);
      const utterance = new SpeechSynthesisUtterance(script);
      utterance.lang = state.interfaceLanguage === "zh-CN" ? "zh-CN" : state.interfaceLanguage || "en-US";
      utterance.rate = state.interfaceLanguage === "zh-CN" ? 1.05 : 1.08;
      state.briefingPlaying = true;
      if (button) {
        button.classList.remove("is-loading");
        button.classList.add("is-playing");
        button.innerHTML = "▥ ❚❚";
      }
      const started = Date.now();
      state.briefingTimer = window.setInterval(() => {
        state.briefingProgress = Math.min(100, ((Date.now() - started) / 30000) * 100);
        renderNewsfeedBriefingPanel(state, {
          status: "Playing 30 sec briefing",
          progress: state.briefingProgress,
          playing: true,
          voiceLabel: data.provider || "browser speech",
        });
      }, 800);
      utterance.onend = () => {
        stopNewsfeedBriefing(state);
        state.briefingProgress = 100;
        renderNewsfeedBriefingPanel(state, { status: "Briefing complete", progress: 100 });
      };
      utterance.onerror = () => {
        stopNewsfeedBriefing(state);
        renderNewsfeedBriefingPanel(state, { status: script, progress: 100 });
      };
      window.speechSynthesis.speak(utterance);
    } catch (error) {
      stopNewsfeedBriefing(state);
      renderNewsfeedBriefingPanel(state, { status: localizedServiceMessage(error.message, "Could not prepare briefing.") });
    }
  }

  async function initNewsfeed() {
    const app = document.getElementById("newsfeedApp");
    if (app) renderNewsfeedBoot(app, "Checking account...");
    const config = await loadOptionalJson("data/config.json", {});
    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    initNewsfeedNav();

    if (!app) return;
    let session = loadAuthSession();
    renderNewsfeedBoot(app, "Preparing General Newsfeed...");
    session = await refreshAuthSession(workerUrl);
    const defaultLanguage = newsfeedDefaultLanguage();

    const state = {
      workerUrl,
      session,
      home: null,
      explore: null,
      settings: null,
      policy: normalizeNewsfeedPolicy({}, session, []),
      topics: [],
      articles: new Map(),
      articleLanguages: new Map(),
      currentView: "feed",
      lastListView: "feed",
      homeCategory: "Investment",
      exploreCategory: "Tech",
      outputLanguage: defaultLanguage,
      interfaceLanguage: defaultLanguage,
      preferredRegions: ["global"],
      preferencesReady: defaultLanguage !== "en",
      regionOptions: [],
      briefingPlaying: false,
      briefingProgress: 0,
      briefingTimer: null,
      requestEpoch: 0,
      pendingRequestedTopic: "",
      limitRequestExposed: false,
    };

    document.addEventListener("portal-auth-change", () => window.location.reload());
    app.innerHTML = newsfeedShellMarkup(state);
    refreshNewsfeedChrome(state);
    renderNewsfeedSidebar(state);
    trackEvent(workerUrl, "page_view", {
      page: "newsfeed",
      access_state: state.policy.authenticated ? "authenticated" : "anonymous",
    });

    function latencyBucket(startedAt) {
      const elapsed = Date.now() - startedAt;
      if (elapsed < 1000) return "lt_1s";
      if (elapsed < 4000) return "1_4s";
      if (elapsed < 15000) return "4_15s";
      return "gte_15s";
    }

    function nextRequestEpoch() {
      state.requestEpoch += 1;
      return state.requestEpoch;
    }

    function applyNewsfeedResponse(data = {}) {
      state.regionOptions = data.regions || state.regionOptions || [];
      state.topics = data.topics || state.topics || [];
      applyNewsfeedPolicy(state, data);
      state.topics = newsfeedVisibleTopics(state, state.topics);
      if (data.settings || state.settings) applyNewsfeedSettings(state, data.settings || state.settings || {});
      refreshNewsfeedChrome(state);
      renderNewsfeedSidebar(state);
    }

    async function loadHome() {
      const epoch = nextRequestEpoch();
      const startedAt = Date.now();
      renderNewsfeedContentLoading(newsfeedText(state, "loadingLatest"), "home");
      const query = newsfeedPreferenceQuery(state);
      const fast = await newsfeedJson(workerUrl, `/newsfeed/home?fast=1&${query}`);
      if (epoch !== state.requestEpoch) return null;
      state.home = fast;
      applyNewsfeedResponse(fast);
      if (newsfeedShouldShowRequest(state)) {
        renderNewsfeedAdd(state);
        state.limitRequestExposed = true;
        trackNewsfeedInteraction(state, "topic_limit_exposure", { outcome: "initial" });
      } else {
        renderNewsfeedHome(state);
      }
      setNewsfeedStatus(fast.pending ? newsfeedText(state, "updating") : "", fast.pending ? "loading" : "");
      trackNewsfeedInteraction(state, "feed_load", {
        outcome: "success",
        item_count: (fast.headlines || []).length,
        latency_bucket: latencyBucket(startedAt),
      });
      newsfeedJson(workerUrl, `/newsfeed/home?${newsfeedPreferenceQuery(state)}`)
        .then((data) => {
          if (epoch !== state.requestEpoch) return;
          state.home = data;
          applyNewsfeedResponse(data);
          setNewsfeedStatus("");
          if (state.currentView === "feed") {
            if (newsfeedShouldShowRequest(state)) {
              renderNewsfeedAdd(state);
              if (!state.limitRequestExposed) {
                state.limitRequestExposed = true;
                trackNewsfeedInteraction(state, "topic_limit_exposure", { outcome: "initial" });
              }
            } else {
              renderNewsfeedHome(state);
            }
          }
        })
        .catch((error) => {
          if (epoch === state.requestEpoch) {
            setNewsfeedStatus(localizedServiceMessage(error.message, "Newsfeed request failed."), "error");
          }
        });
      return fast;
    }

    async function loadExplore(category = state.exploreCategory) {
      const epoch = nextRequestEpoch();
      const startedAt = Date.now();
      renderNewsfeedContentLoading("Loading explore...", "explore");
      const data = await newsfeedJson(workerUrl, `/newsfeed/explore?category=${encodeURIComponent(category || "")}&${newsfeedPreferenceQuery(state)}`);
      if (epoch !== state.requestEpoch) return null;
      state.explore = data;
      state.exploreCategory = category || (data.categories && data.categories[0]) || "";
      applyNewsfeedResponse(data);
      setNewsfeedStatus("");
      renderNewsfeedExplore(state);
      trackNewsfeedInteraction(state, "explore_load", {
        outcome: "success",
        category: state.exploreCategory,
        item_count: (data.items || []).length,
        latency_bucket: latencyBucket(startedAt),
      });
      return data;
    }

    async function loadTopic(id) {
      const cleanId = String(id || "").trim();
      if (!newsfeedSystemTopic(cleanId) && !newsfeedCanCustomize(state)) {
        setNewsfeedStatus("登录并开通会员后可查看自定义话题。", "error");
        return null;
      }
      const epoch = nextRequestEpoch();
      const startedAt = Date.now();
      renderNewsfeedContentLoading("Preparing topic package...", "topic");
      const data = await newsfeedJson(workerUrl, `/newsfeed/topic?id=${encodeURIComponent(cleanId)}&${newsfeedPreferenceQuery(state)}`);
      if (epoch !== state.requestEpoch) return null;
      applyNewsfeedResponse(data);
      setNewsfeedStatus("");
      renderNewsfeedTopic(state, data.topic, data.items || []);
      trackNewsfeedInteraction(state, "topic_load", {
        outcome: "success",
        topic: data.topic || cleanId,
        item_count: (data.items || []).length,
        latency_bucket: latencyBucket(startedAt),
      });
      return data;
    }

    async function reloadCurrentNewsfeed() {
      if (state.currentView === "explore") return loadExplore(state.exploreCategory);
      if (state.currentView === "topic" && state.currentTopic) return loadTopic(state.currentTopic.id);
      if (state.currentView === "email" && newsfeedCanSubscribe(state)) {
        nextRequestEpoch();
        renderNewsfeedEmailView(state);
        return null;
      }
      return loadHome();
    }

    async function saveNewsfeedPreferences(reload = true) {
      if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return null;
      state.preferencesReady = true;
      refreshNewsfeedChrome(state);
      const data = await newsfeedJson(workerUrl, "/newsfeed/settings", {
        method: "POST",
        body: JSON.stringify({
          preferred_regions: state.preferredRegions,
          interface_language: state.interfaceLanguage,
        }),
      });
      applyNewsfeedPolicy(state, data);
      applyNewsfeedSettings(state, data.settings || state.settings || {});
      refreshNewsfeedChrome(state);
      trackNewsfeedInteraction(state, "preferences_save", {
        outcome: "success",
        language: state.interfaceLanguage,
        region_count: (state.preferredRegions || []).length,
      });
      if (reload) await reloadCurrentNewsfeed();
      return data;
    }

    function closeSidebar() {
      const sidebar = document.getElementById("newsfeedSidebar");
      if (sidebar) sidebar.classList.remove("is-open");
    }

    app.addEventListener("click", async (event) => {
      const control = event.target.closest("[data-action]");
      if (!control) return;
      const action = control.dataset.action;
      try {
        if (action === "show-login" || action === "show-account") {
          trackNewsfeedInteraction(state, "membership_cta", { outcome: "open" });
          showAccountModal(workerUrl);
          return;
        }
        if (action === "toggle-sidebar") {
          document.getElementById("newsfeedSidebar")?.classList.toggle("is-open");
          return;
        }
        if (action === "show-feed") {
          closeSidebar();
          trackNewsfeedInteraction(state, "view_feed");
          if (!state.home) await loadHome();
          else {
            nextRequestEpoch();
            renderNewsfeedHome(state);
          }
          return;
        }
        if (action === "show-add") {
          if (!newsfeedCanOpenAdd(state)) return;
          closeSidebar();
          nextRequestEpoch();
          renderNewsfeedAdd(state);
          trackNewsfeedInteraction(state, "view_add", { custom_topic_remaining: state.policy.custom_topic_remaining });
          return;
        }
        if (action === "show-explore") {
          closeSidebar();
          await loadExplore();
          return;
        }
        if (action === "show-email") {
          if (!newsfeedCanSubscribe(state)) return;
          closeSidebar();
          nextRequestEpoch();
          renderNewsfeedEmailView(state);
          trackNewsfeedInteraction(state, "view_email");
          return;
        }
        if (action === "send-email-test" || action === "send-email-now") {
          if (!newsfeedCanSubscribe(state)) return;
          const isTest = action === "send-email-test";
          const status = document.getElementById("newsEmailStatus");
          const button = document.getElementById(isTest ? "newsEmailTest" : "newsEmailSend");
          if (status) {
            status.className = "status-line";
            status.textContent = isTest ? "Sending test digest email..." : "Sending newsletter digest...";
          }
          if (button) {
            button.disabled = true;
            button.classList.add("is-loading");
            button.textContent = "Sending...";
          }
          trackNewsfeedInteraction(state, isTest ? "email_test" : "email_send", { outcome: "submit" });
          const data = await newsfeedJson(workerUrl, isTest ? "/newsfeed/email-test" : "/newsfeed/email-send", {
            method: "POST",
            body: JSON.stringify(newsfeedEmailPayloadFromForm(state)),
          });
          applyNewsfeedPolicy(state, data);
          applyNewsfeedSettings(state, data.settings || state.settings || {});
          renderNewsfeedEmailView(state);
          const nextStatus = document.getElementById("newsEmailStatus");
          if (nextStatus) {
            nextStatus.className = data.sent ? "status-line ok" : "status-line error";
            const idSuffix = data.message_id ? ` (${data.message_id})` : "";
            nextStatus.textContent = data.sent
              ? (isTest
                ? `Test digest accepted by ${data.provider || "email provider"}.${idSuffix}`
                : `Newsletter accepted by ${data.provider || "email provider"}.${idSuffix}`)
              : localizedServiceMessage(
                data.detail || state.settings.digest_last_send_detail,
                isTest ? "Test email was not sent." : "Newsletter email was not sent.",
              );
          }
          trackNewsfeedInteraction(state, isTest ? "email_test" : "email_send", {
            outcome: data.sent ? "success" : "error",
            provider: data.provider || "",
          });
          return;
        }
        if (action === "toggle-region-menu") {
          if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
          const menu = document.getElementById("newsRegionMenu");
          const toggle = document.getElementById("newsRegionToggle");
          if (menu) {
            const nextHidden = !menu.hidden;
            menu.hidden = nextHidden;
            if (toggle) toggle.setAttribute("aria-expanded", String(!nextHidden));
          }
          return;
        }
        if (action === "play-briefing") {
          if (!(state.policy && state.policy.authenticated)) return;
          trackNewsfeedInteraction(state, "briefing_toggle");
          await playNewsfeedBriefing(state);
          return;
        }
        if (action === "close-briefing") {
          stopNewsfeedBriefing(state);
          const panel = document.getElementById("newsBriefingPanel");
          if (panel) panel.hidden = true;
          return;
        }
        if (action === "briefing-prev" || action === "briefing-next") {
          renderNewsfeedBriefingPanel(state, {
            status: state.briefingScript || newsfeedText(state, "playBriefing"),
            progress: state.briefingProgress || 0,
            playing: state.briefingPlaying,
          });
          return;
        }
        if (action === "home-category") {
          state.homeCategory = control.dataset.category || "";
          renderNewsfeedHome(state);
          trackNewsfeedInteraction(state, "category_select", { category: state.homeCategory, view: "feed" });
          return;
        }
        if (action === "explore-category") {
          state.exploreCategory = control.dataset.category || "";
          renderNewsfeedExplore(state);
          trackNewsfeedInteraction(state, "category_select", { category: state.exploreCategory, view: "explore" });
          return;
        }
        if (action === "suggest-topic") {
          const input = document.getElementById("newsTopicInput");
          if (input) input.value = control.dataset.topic || "";
          trackNewsfeedInteraction(state, "topic_suggestion_select");
          return;
        }
        if (action === "open-topic") {
          const id = String(control.dataset.id || "");
          if (!newsfeedSystemTopic(id) && !newsfeedCanCustomize(state)) return;
          closeSidebar();
          trackNewsfeedInteraction(state, "topic_open", { topic: id });
          await loadTopic(id);
          return;
        }
        if (action === "pin-topic") {
          if (!newsfeedCanCustomize(state)) return;
          const id = control.dataset.id || "";
          const topic = (state.topics || []).find((item) => String(item.id) === id);
          const pinned = !(topic && topic.pinned);
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics/pin", {
            method: "POST",
            body: JSON.stringify({ id, pinned }),
          });
          applyNewsfeedPolicy(state, data);
          if (topic) topic.pinned = pinned;
          renderNewsfeedSidebar(state);
          trackNewsfeedInteraction(state, "topic_pin", { topic: id, outcome: pinned ? "pinned" : "unpinned" });
          return;
        }
        if (action === "open-article") {
          const id = String(control.dataset.id || "");
          const article = state.articles.get(id);
          state.lastListView = state.currentView === "article" ? state.lastListView : state.currentView;
          trackNewsfeedInteraction(state, "article_open", { topic: id });
          await renderNewsfeedArticle(state, article ? { ...article, output_language: state.articleLanguages.get(id) || state.outputLanguage || "en" } : article);
          return;
        }
        if (action === "article-back") {
          if (state.lastListView === "explore") renderNewsfeedExplore(state);
          else if (state.lastListView === "topic") renderNewsfeedTopic(state, state.currentTopic, state.currentTopicItems);
          else renderNewsfeedHome(state);
        }
      } catch (error) {
        trackNewsfeedInteraction(state, "ui_error", { outcome: "error", reason: error.code || "request_failed" });
        setNewsfeedStatus(localizedServiceMessage(error.message, "Newsfeed request failed."), "error");
      }
    });

    app.addEventListener("submit", async (event) => {
      if (event.target && event.target.id === "newsTopicForm") {
        event.preventDefault();
        if (!newsfeedCanCreateTopic(state)) {
          renderNewsfeedAdd(state);
          return;
        }
        const input = document.getElementById("newsTopicInput");
        const language = document.getElementById("newsTopicLanguage");
        const status = document.getElementById("newsTopicStatus");
        const submit = document.getElementById("newsTopicSubmit");
        const topic = input ? input.value.trim() : "";
        if (!topic) return;
        const outputLanguage = language ? language.value : "en";
        state.outputLanguage = outputLanguage || "en";
        if (status) {
          status.className = "status-line";
          status.textContent = "Creating topic package...";
        }
        if (submit) {
          submit.disabled = true;
          submit.classList.add("is-loading");
          submit.textContent = "…";
        }
        trackNewsfeedInteraction(state, "topic_create", { outcome: "submit", requested_topic: topic, language: outputLanguage });
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics", {
            method: "POST",
            body: JSON.stringify({ topic, output_language: outputLanguage, preferred_regions: state.preferredRegions }),
          });
          state.topics = data.topics || state.topics || [];
          applyNewsfeedPolicy(state, data);
          state.topics = newsfeedVisibleTopics(state, state.topics);
          refreshNewsfeedChrome(state);
          renderNewsfeedSidebar(state);
          renderNewsfeedTopic(state, data.topic, data.items || []);
          setNewsfeedStatus(data.pending ? "Topic created. Stories are loading; open it again in a moment." : "", data.pending ? "ok" : "");
          trackNewsfeedInteraction(state, "topic_create", { outcome: "success", topic: data.topic || topic, language: outputLanguage });
        } catch (error) {
          if (error.status === 409 && error.code === "NEWSFEED_TOPIC_LIMIT") {
            state.pendingRequestedTopic = String(error.data && error.data.requested_topic || topic).trim().slice(0, 600);
            applyNewsfeedPolicy(state, error.data || {});
            refreshNewsfeedChrome(state);
            renderNewsfeedAdd(state);
            trackNewsfeedInteraction(state, "topic_create", { outcome: "limit", requested_topic: topic });
          } else if (status) {
            status.className = "status-line error";
            status.textContent = localizedServiceMessage(error.message, "Could not create topic.");
            trackNewsfeedInteraction(state, "topic_create", { outcome: "error", requested_topic: topic, reason: error.code || "request_failed" });
          }
        } finally {
          if (submit && submit.isConnected) {
            submit.disabled = false;
            submit.classList.remove("is-loading");
            submit.textContent = "↑";
          }
        }
      }
      if (event.target && event.target.id === "newsTopicRequestForm") {
        event.preventDefault();
        if (!(state.policy && state.policy.request_allowed)) return;
        const topicInput = document.getElementById("newsTopicRequestInput");
        const language = document.getElementById("newsTopicRequestLanguage");
        const confirm = document.getElementById("newsTopicRequestConfirm");
        const honeypot = document.getElementById("newsTopicRequestHoneypot");
        const status = document.getElementById("newsTopicRequestStatus");
        const submit = document.getElementById("newsTopicRequestSubmit");
        const topic = topicInput ? topicInput.value.trim() : "";
        if (!topic || !confirm || !confirm.checked) {
          if (status) {
            status.className = "status-line error";
            status.textContent = "请填写话题并勾选确认后再提交。";
          }
          return;
        }
        const outputLanguage = language ? language.value : state.outputLanguage || "en";
        const body = {
          topic,
          output_language: outputLanguage,
          preferred_regions: state.preferredRegions || ["global"],
          page_path: currentAnalyticsPath(),
          honeypot: honeypot ? honeypot.value : "",
        };
        if (submit) {
          submit.disabled = true;
          submit.textContent = "提交中…";
        }
        if (status) {
          status.className = "status-line";
          status.textContent = "正在提交申请…";
        }
        trackNewsfeedInteraction(state, "topic_request", { outcome: "submit", requested_topic: topic, language: outputLanguage });
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics/request", {
            method: "POST",
            body: JSON.stringify(body),
          });
          applyNewsfeedPolicy(state, data);
          if (status) {
            status.className = "status-line ok";
            status.textContent = localizedServiceMessage(data.detail, "申请已提交，我们会后续处理。");
          }
          if (submit) submit.textContent = "已提交";
          trackNewsfeedInteraction(state, "topic_request", { outcome: "success", requested_topic: topic });
        } catch (error) {
          if (status) {
            status.className = "status-line error";
            status.textContent = localizedServiceMessage(error.message, "申请提交失败，请稍后重试。");
          }
          if (submit) {
            submit.disabled = false;
            submit.textContent = "确认提交申请";
          }
          trackNewsfeedInteraction(state, "topic_request", { outcome: "error", requested_topic: topic, reason: error.code || "request_failed" });
        }
      }
      if (event.target && event.target.id === "newsCustomRegionForm") {
        event.preventDefault();
        if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
        const input = document.getElementById("newsCustomRegionInput");
        const value = input ? input.value.trim() : "";
        if (!value) return;
        state.preferredRegions = normalizeNewsfeedRegionsClient([...(state.preferredRegions || []), value]);
        if (input) input.value = "";
        await saveNewsfeedPreferences(true);
      }
      if (event.target && event.target.id === "newsEmailForm") {
        event.preventDefault();
        if (!newsfeedCanSubscribe(state)) return;
        const status = document.getElementById("newsEmailStatus");
        const submit = document.getElementById("newsEmailSubmit");
        const payload = newsfeedEmailPayloadFromForm(state);
        if (status) {
          status.className = "status-line";
          status.textContent = "Saving digest email settings...";
        }
        if (submit) {
          submit.disabled = true;
          submit.classList.add("is-loading");
          submit.textContent = "Saving...";
        }
        trackNewsfeedInteraction(state, "email_subscription", { outcome: "submit" });
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/settings", {
            method: "POST",
            body: JSON.stringify(payload),
          });
          state.settings = data.settings || state.settings || {};
          applyNewsfeedPolicy(state, data);
          if (status) {
            status.className = "status-line ok";
            status.textContent = state.settings.email_provider_configured === false
              ? "Settings saved. Email delivery starts after the email sender is configured."
              : (state.settings.digest_email_enabled
                ? "Newsletter subscription saved. It will be sent at the selected time."
                : "Newsletter subscription canceled.");
          }
          trackNewsfeedInteraction(state, "email_subscription", { outcome: state.settings.digest_email_enabled ? "enabled" : "disabled" });
        } catch (error) {
          if (status) {
            status.className = "status-line error";
            status.textContent = localizedServiceMessage(error.message, "Could not save email settings.");
          }
          trackNewsfeedInteraction(state, "email_subscription", { outcome: "error", reason: error.code || "request_failed" });
        } finally {
          if (submit) {
            submit.disabled = false;
            submit.classList.remove("is-loading");
            submit.textContent = newsfeedText(state, "saveEmail");
          }
        }
      }
    });

    app.addEventListener("change", async (event) => {
      const target = event.target;
      try {
        if (target && target.dataset && target.dataset.action === "region-checkbox") {
          if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
          const selected = Array.from(document.querySelectorAll("[data-action='region-checkbox']:checked"))
            .map((item) => item.value);
          state.preferredRegions = normalizeNewsfeedRegionsClient(selected);
          await saveNewsfeedPreferences(true);
        }
        if (target && target.id === "newsInterfaceLanguage") {
          if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
          const fixedInterfaceLanguage = newsfeedFixedInterfaceLanguage();
          if (fixedInterfaceLanguage) {
            const nextUrl = newsfeedInterfaceNavigationUrl(target.value || fixedInterfaceLanguage);
            if (nextUrl) window.location.href = nextUrl;
            return;
          }
          state.interfaceLanguage = newsfeedLanguageCode(target.value || "en");
          state.outputLanguage = state.interfaceLanguage;
          await saveNewsfeedPreferences(true);
        }
        if (target && target.id === "newsTopicLanguage") {
          state.outputLanguage = newsfeedLanguageCode(target.value || "en");
        }
        if (target && target.id === "newsNewsletterTopic") {
          const enabled = document.getElementById("newsEmailEnabled");
          if (enabled) enabled.checked = Boolean(target.value);
        }
        if (target && target.id === "newsEmailEnabled" && target.checked) {
          const topic = document.getElementById("newsNewsletterTopic");
          if (topic && !topic.value) topic.value = "global-daily";
        }
      } catch (error) {
        trackNewsfeedInteraction(state, "preferences_save", { outcome: "error", reason: error.code || "request_failed" });
        setNewsfeedStatus(localizedServiceMessage(error.message, "Could not save preferences."), "error");
      }
    });

    await loadHome();
  }

  return initNewsfeed();
}
