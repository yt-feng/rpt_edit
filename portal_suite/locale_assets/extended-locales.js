(function () {
  "use strict";
  const normalize = value => String(value || "").normalize("NFKD").replace(/\p{M}/gu, "").toLocaleLowerCase().replace(/[^\p{L}\p{N}]+/gu, " ").trim();
  function selectRows(rows, { query = "", kind = "", from = "", to = "", sort = "newest" } = {}) {
    const terms = normalize(query).split(/\s+/).filter(Boolean);
    return rows.filter(row => (!kind || row.kind === kind) && (!from || row.date >= from) && (!to || (row.date && row.date <= to)) && terms.every(term => normalize(row.text).includes(term)))
      .sort((a, b) => (sort === "oldest" ? 1 : -1) * a.date.localeCompare(b.date) || a.position - b.position);
  }
  if (typeof module !== "undefined" && module.exports) module.exports = { normalize, selectRows };
  if (typeof document === "undefined") return;
  const el = id => document.getElementById(id);
  const list = el("extendedResults");
  if (!list) return;
  const rows = Array.from(list.querySelectorAll(".extended-result"), (node, position) => ({ node, position, kind: node.dataset.kind, date: node.dataset.date, text: node.textContent }));
  const controls = [el("extendedSearch") || el("searchInput"), el("extendedType"), el("extendedFrom") || el("startDate"), el("extendedTo") || el("endDate"), el("extendedSort")];
  let page = 1;
  const pageSize = 24;
  const params = new URLSearchParams(location.search);
  controls[0].value = params.get("q") || "";
  controls[1].value = ["blog", "reports"].includes(params.get("type")) ? params.get("type") : "";
  function render() {
    const selected = selectRows(rows, { query: controls[0].value, kind: controls[1].value, from: controls[2].value, to: controls[3].value, sort: controls[4].value });
    const pages = Math.max(1, Math.ceil(selected.length / pageSize));
    page = Math.max(1, Math.min(page, pages));
    rows.forEach(row => { row.node.hidden = true; });
    selected.slice((page - 1) * pageSize, page * pageSize).forEach(row => { row.node.hidden = false; list.append(row.node); });
    el("extendedCount").textContent = `${selected.length} / ${rows.length}`;
    el("extendedPage").textContent = `${page} / ${pages}`;
    el("extendedPrev").disabled = page <= 1;
    el("extendedNext").disabled = page >= pages;
    el("extendedEmpty").hidden = selected.length > 0;
  }
  controls.forEach(control => control.addEventListener("input", () => { page = 1; render(); }));
  (el("extendedClear") || el("clearFilters")).addEventListener("click", () => { controls.forEach(control => { control.value = ""; }); controls[4].value = "newest"; page = 1; render(); });
  el("extendedPrev").addEventListener("click", () => { page -= 1; render(); });
  el("extendedNext").addEventListener("click", () => { page += 1; render(); });
  render();
}());
