(() => {
  "use strict";

  const root = document.querySelector("[data-api-docs]");
  const navigation = root?.querySelector("[data-api-tabs]");
  if (!root || !navigation) return;

  const panels = [...root.querySelectorAll("[data-api-panel]")];
  const entries = [...navigation.querySelectorAll("a[data-api-tab]")].map((tab) => {
    const href = tab.getAttribute("href") || "";
    const panel = href.startsWith("#") && panels.find((item) => `#${item.id}` === href);
    return panel && tab.id ? { tab, panel } : null;
  }).filter(Boolean);
  // Leave the readable HTML unchanged if its tab/panel contract is incomplete.
  if (!entries.length || entries.length !== panels.length
    || new Set(entries.map(({ panel }) => panel)).size !== panels.length) return;

  navigation.setAttribute("role", "tablist");
  navigation.setAttribute("aria-orientation", "horizontal");
  if (!navigation.hasAttribute("aria-label")) navigation.setAttribute("aria-label", "API 文档");
  for (const { tab, panel } of entries) {
    tab.setAttribute("role", "tab");
    tab.setAttribute("aria-controls", panel.id);
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("aria-labelledby", tab.id);
    panel.tabIndex = 0;
  }

  const header = document.querySelector("body > .topbar");
  const tabWrap = root.querySelector(".api-tab-wrap") || navigation;
  let activeEntry = null;
  let contentOffset = 16;

  function revealTab(tab) {
    const bounds = navigation.getBoundingClientRect();
    const target = tab.getBoundingClientRect();
    const left = bounds.left + navigation.clientLeft + 4;
    const right = bounds.left + navigation.clientLeft + navigation.clientWidth - 4;
    // Adjust this horizontal scroller only; never scroll the page to focus a tab.
    if (target.left < left) navigation.scrollLeft += target.left - left;
    else if (target.right > right) navigation.scrollLeft += target.right - right;
  }

  function measureLayout() {
    const headerHeight = header?.getBoundingClientRect().height || 0;
    const tabsHeight = tabWrap.getBoundingClientRect().height;
    root.style.setProperty("--api-header-height", `${headerHeight}px`);
    root.style.setProperty("--api-tabs-height", `${tabsHeight}px`);
    root.dataset.apiLayout = "measured";
    contentOffset = headerHeight + tabsHeight + 16;
    if (activeEntry) revealTab(activeEntry.tab);
  }

  function activate(selected) {
    activeEntry = selected;
    for (const entry of entries) {
      const active = entry === selected;
      entry.tab.setAttribute("aria-selected", String(active));
      entry.tab.tabIndex = active ? 0 : -1;
      entry.panel.hidden = !active;
    }
    revealTab(selected.tab);
  }

  function resolve(hash) {
    if (!hash || !hash.startsWith("#")) return null;
    let id;
    try { id = decodeURIComponent(hash.slice(1)); } catch { return null; }
    const target = document.getElementById(id);
    if (!target || !root.contains(target)) return null;
    const entry = entries.find(({ tab, panel }) => tab === target || panel === target || panel.contains(target));
    return entry ? { entry, target } : null;
  }

  let handledHash;
  function readLocation() {
    if (handledHash === window.location.hash) return;
    handledHash = window.location.hash;
    const match = resolve(handledHash);
    activate(match?.entry || entries[0]);
    if (match) match.target.scrollIntoView({ block: "start" });
  }

  function setHash(target) {
    const hash = `#${encodeURIComponent(target.id)}`;
    if (window.location.hash === hash) return;
    try {
      window.history.pushState(window.history.state, "", hash);
      handledHash = window.location.hash;
    } catch {
      window.location.hash = hash;
    }
  }

  function selectTab(entry) {
    activate(entry);
    setHash(entry.panel);
    entry.tab.focus({ preventScroll: true });
    if (entry.panel.getBoundingClientRect().top < contentOffset) {
      entry.panel.scrollIntoView({ block: "start", inline: "nearest" });
    }
  }

  function focusContent(target) {
    const temporary = !target.hasAttribute("tabindex") && !target.matches("a[href], button, input, select, textarea");
    if (temporary) {
      target.setAttribute("tabindex", "-1");
      target.addEventListener("blur", () => target.removeAttribute("tabindex"), { once: true });
    }
    target.focus({ preventScroll: true });
    target.scrollIntoView({ block: "start" });
  }

  let copySequence = 0;
  async function copyCode(button) {
    const status = document.getElementById("api-copy-status");
    const code = document.getElementById(button.getAttribute("data-api-copy") || "");
    const ticket = ++copySequence;
    const announce = (message) => {
      if (status && ticket === copySequence) status.textContent = message;
    };
    if (!code || code.tagName !== "CODE" || !root.contains(code)) {
      announce("未找到代码，请手动选择复制。");
      return;
    }
    button.disabled = true;
    announce("正在复制…");
    try {
      if (!navigator.clipboard?.writeText) throw new Error("clipboard_unavailable");
      await navigator.clipboard.writeText(code.textContent || "");
      announce("代码已复制。");
    } catch {
      announce("复制未完成，请手动选择代码复制。");
    } finally {
      button.disabled = false;
    }
  }

  root.addEventListener("click", (event) => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.altKey || event.shiftKey) return;
    const target = event.target;
    const copy = target.closest?.("button[data-api-copy]");
    if (copy && root.contains(copy)) {
      event.preventDefault();
      if (!copy.disabled) void copyCode(copy);
      return;
    }
    const link = target.closest?.("a[data-api-tab], a[data-api-link]");
    if (!link || !root.contains(link)) return;
    const tab = entries.find((entry) => entry.tab === link);
    const match = resolve(link.getAttribute("href"));
    if (!match || (!tab && !link.hasAttribute("data-api-link"))) return;
    event.preventDefault();
    if (tab) selectTab(tab);
    else {
      activate(match.entry);
      setHash(match.target);
      focusContent(match.target);
    }
  });

  navigation.addEventListener("keydown", (event) => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    const index = entries.findIndex(({ tab }) => tab === event.target);
    if (index < 0) return;
    let next;
    if (event.key === "ArrowRight") next = (index + 1) % entries.length;
    else if (event.key === "ArrowLeft") next = (index + entries.length - 1) % entries.length;
    else if (event.key === "Home") next = 0;
    else if (event.key === "End") next = entries.length - 1;
    else if (event.key === " " || event.key === "Enter") next = index;
    else return;
    event.preventDefault();
    selectTab(entries[next]);
  });

  window.addEventListener("hashchange", readLocation);
  window.addEventListener("popstate", readLocation);
  // Establish anchor offsets before applying an initial deep link. Header
  // wrapping and account controls can change height after the initial render.
  measureLayout();
  if (typeof ResizeObserver === "function") {
    const layoutObserver = new ResizeObserver(measureLayout);
    if (header) layoutObserver.observe(header);
    layoutObserver.observe(tabWrap);
  } else {
    window.addEventListener("resize", measureLayout, { passive: true });
  }
  readLocation();
})();
