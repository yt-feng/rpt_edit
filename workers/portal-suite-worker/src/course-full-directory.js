export const COURSE_FULL_DIRECTORY_KEY = "_course-directory/full-v1/directory.json";
const MAX_BYTES = 32 * 1024 * 1024;
const MAX_ITEMS = 100000;
const CACHE_MS = 5 * 60 * 1000;
const CACHE = new WeakMap();
const FIELDS = ["id", "name", "folders", "extension", "size_label", "date"];
const TOP_FIELDS = ["schema_version", "variant", "complete", "item_count", "generated_at", "items"];

function exactFields(value, fields) {
  return value && typeof value === "object" && !Array.isArray(value)
    && Object.keys(value).length === fields.length && fields.every((field) => Object.hasOwn(value, field));
}

function label(value) {
  return typeof value === "string" && value.trim() && [...value].length <= 500
    && !/[\u0000-\u001f\u007f/\\]/u.test(value);
}

export function fullDirectoryFileType(extension) {
  if (extension === "pdf") return "pdf";
  if (["mp4", "mov", "mkv", "avi", "webm", "m4v"].includes(extension)) return "video";
  if (["mp3", "m4a", "wav", "flac", "aac", "ogg"].includes(extension)) return "audio";
  if (["doc", "docx", "txt", "rtf", "md"].includes(extension)) return "document";
  if (["ppt", "pptx", "key"].includes(extension)) return "presentation";
  if (["xls", "xlsx", "csv", "tsv", "numbers"].includes(extension)) return "spreadsheet";
  if (["zip", "rar", "7z", "tar", "gz"].includes(extension)) return "archive";
  if (["jpg", "jpeg", "png", "gif", "webp", "svg"].includes(extension)) return "image";
  return "other";
}

export function validateCourseFullDirectory(payload) {
  if (!exactFields(payload, TOP_FIELDS) || payload.schema_version !== 1 || payload.variant !== "original_names"
    || payload.complete !== true || !Array.isArray(payload.items) || !Number.isSafeInteger(payload.item_count)
    || payload.item_count !== payload.items.length || payload.item_count < 1 || payload.item_count > MAX_ITEMS
    || typeof payload.generated_at !== "string" || !/^\d{4}-\d{2}-\d{2}T[0-9:.]+Z$/u.test(payload.generated_at)
    || !Number.isFinite(Date.parse(payload.generated_at))) throw new Error("Original-name directory is unavailable.");
  const seen = new Set();
  const folderCounts = new Map();
  const typeCounts = new Map();
  for (const row of payload.items) {
    if (!exactFields(row, FIELDS) || typeof row.id !== "string" || !/^[a-z0-9][a-z0-9_-]{7,79}$/u.test(row.id)
      || seen.has(row.id) || !label(row.name) || !Array.isArray(row.folders) || row.folders.length > 32
      || !row.folders.every(label) || typeof row.extension !== "string" || !/^[a-z0-9]{0,12}$/u.test(row.extension)
      || typeof row.size_label !== "string" || (row.size_label && !/^\d+(?:\.\d+)?\s*(?:B|KB|MB|GB|TB)$/u.test(row.size_label))
      || typeof row.date !== "string" || (row.date && !/^\d{4}-\d{2}-\d{2}$/u.test(row.date))) {
      throw new Error("Original-name directory is unavailable.");
    }
    seen.add(row.id);
    const folder = row.folders[0] || "";
    if (folder) folderCounts.set(folder, (folderCounts.get(folder) || 0) + 1);
    const type = fullDirectoryFileType(row.extension);
    typeCounts.set(type, (typeCounts.get(type) || 0) + 1);
  }
  const facets = (counts) => [...counts].map(([name, count]) => ({ name, count })).sort((a, b) => a.name.localeCompare(b.name));
  // Keep only metadata. No original storage locator or download endpoint is
  // accepted, even as an ignored extension field in an otherwise valid row.
  return { items: payload.items, generated_at: payload.generated_at, facets: { folders: facets(folderCounts), file_types: facets(typeCounts) } };
}

export async function loadCourseFullDirectory(bucket) {
  const cached = CACHE.get(bucket);
  if (cached?.value && Date.now() - cached.loaded_at < CACHE_MS) return cached.value;
  if (cached?.promise) return cached.promise;
  const promise = (async () => {
    const object = await bucket.get(COURSE_FULL_DIRECTORY_KEY);
    if (!object || Number(object.size) > MAX_BYTES) throw new Error("Original-name directory is unavailable.");
    const text = await object.text();
    if (new TextEncoder().encode(text).byteLength > MAX_BYTES) throw new Error("Original-name directory is unavailable.");
    return validateCourseFullDirectory(JSON.parse(text));
  })();
  CACHE.set(bucket, { promise });
  try {
    const value = await promise;
    CACHE.set(bucket, { value, loaded_at: Date.now() });
    return value;
  } catch (error) {
    CACHE.delete(bucket);
    throw error;
  }
}

function searchText(value, limit) {
  return String(value || "").slice(0, limit).normalize("NFKC").toLowerCase();
}

export function queryCourseFullDirectory(directory, params) {
  const terms = searchText(params.get("q"), 160).trim().split(/\s+/u).filter(Boolean).slice(0, 12);
  const folder = String(params.get("folder") || "").slice(0, 1000);
  const type = String(params.get("file_type") || "").slice(0, 24);
  const page = Math.max(1, Math.min(100000, Math.trunc(Number(params.get("page")) || 1)));
  const pageSize = Math.max(1, Math.min(100, Math.trunc(Number(params.get("page_size")) || 50)));
  const start = (page - 1) * pageSize;
  const items = [];
  let total = 0;
  for (const row of directory.items) {
    if (folder && (row.folders[0] || "") !== folder) continue;
    if (type && fullDirectoryFileType(row.extension) !== type) continue;
    if (terms.length) {
      const haystack = searchText([row.name, ...row.folders].join("\n"), 17000);
      if (!terms.every((term) => haystack.includes(term))) continue;
    }
    if (total >= start && items.length < pageSize) items.push({ ...row, folders: [...row.folders] });
    total += 1;
  }
  return { items, total, page, page_size: pageSize, has_more: start + items.length < total, facets: directory.facets, generated_at: directory.generated_at };
}
