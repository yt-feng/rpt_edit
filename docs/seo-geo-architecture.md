# SEO / GEO architecture for KC桌面

This document defines the public discovery contract for the generated report site. It is intentionally written against the neutral build origin `https://portal.example.invalid`; production identity and routing are materialized outside the public source tree.

## Goals and non-goals

The site should be discoverable by global Simplified-Chinese readers searching for investment-bank research, macro strategy, industry research, company research, filings, think-tank reports, and charts. English institution names, company names, tickers, and source titles remain searchable because those are often the terms a Chinese reader actually uses.

The site does not claim authorship, ownership, or publication rights over an underlying report. It publishes a free metadata and discovery page. Report access is a separate, dynamic capability whose current state must not be inferred from an old search snippet.

“GEO” does not have a special Google markup or shortcut. The implementation therefore uses the same crawlability, text quality, structured data, internal linking, page experience, and attribution fundamentals used for conventional search. `llms.txt` is a secondary machine-readable aid, not a substitute for crawlable HTML or a Google ranking signal.

## Public URL contract

| Content | Canonical URL | Build behavior |
| --- | --- | --- |
| Search home | `/` | Canonical, `zh-Hans`, WebSite + Organization entity graph |
| Report collection | `/reports/` | First 200 records, self-canonical |
| Report collection pages | `/reports/page-N.html` | 200 records per page, self-canonical, crawlable previous/next and numbered links |
| Institution/topic hub | `/reports/topics.html` | Every institution and topic gets a stable fragment target; each section shows its newest records |
| Report metadata | `/reports/{opaque-id}.html` | One canonical page per report, visible source-bounded summary and Report/WebPage/Breadcrumb data |
| Blog collection | `/blog/` | First 30 posts, self-canonical |
| Blog collection pages | `/blog/page-N.html` | 30 posts per page, self-canonical, crawlable pagination |
| Blog article | `/blog/{date-fingerprint}.html` | Canonical BlogPosting/WebPage/Breadcrumb data |
| Chart discovery | `/charts` | Canonical chart-search landing page |
| Methodology | `/about.html` | Entity definition, scope, attribution boundary, and discovery routes |

Each paginated page is independently canonical. Do not canonicalize every page to page 1. Pagination must remain ordinary `<a href>` navigation; buttons or JavaScript-only state are not a crawl path.

Dynamic report, document, delivery, and personalized newsfeed pages stay `noindex`. Their query parameters can contain transient application state and should not become canonical discovery URLs.

## Language and entity signals

- Public pages use `lang="zh-Hans"`, `hreflang="zh-Hans"`, and a same-page `x-default` alternate.
- Do not add `hreflang="en"` until a real English page exists at a distinct URL. English keywords inside a Chinese page are not an English localization.
- The only public entity name is `KC桌面`; historical English deployment identities are not emitted as aliases.
- Titles and descriptions cover both Chinese intent and high-value English query vocabulary such as “Chinese financial research”, “investment bank research”, “equity research”, “macro research”, institution names, companies, and tickers.
- Legacy neutral editorial labels are normalized to `KC桌面` only at the public rendering edge. Immutable source archives and their fingerprints do not change.

## Report attribution and structured data

The static metadata page and the underlying report are different entities:

- `WebPage` describes the free KC桌面 metadata page and uses `isAccessibleForFree: true`.
- `Report` describes the indexed report, uses the catalog institution as `publisher`, and uses KC桌面 only as `sdPublisher` for the structured-data record.
- `Report.abstract` exactly matches the visible “核心信息（可引用）” paragraph. It includes only catalog-backed facts: institution, index date, display title, topic, page count, and current index availability.
- `datePublished` is emitted only from an explicit valid `published_at` field; the Dropbox/date-folder index date is never promoted into a publication claim. `pagination` is emitted only when the catalog contains a valid page count.
- Do not synthesize `author`, `copyrightHolder`, analyst names, investment conclusions, or ownership claims.
- A visible attribution boundary explains that KC桌面 is the metadata/discovery index and that original author, copyright, and usage conditions come from the source report.
- Related reports and institution/topic links are static HTML links. Every fragment link emitted by a report page must exist on the topic hub.

Blog article JSON-LD follows the same visibility rule: headline, description, author, image, and dates must match the public article. A neutral legacy author becomes KC桌面; a known source author remains that author.

## First-paint catalog preview

The build writes `data/catalog_preview.json` alongside the full public catalog. Its contract is:

```json
{
  "schema_version": 1,
  "updated_at_bjt": "build timestamp",
  "item_count": 40,
  "total_item_count": 12838,
  "items": ["newest 40 records, using the existing public catalog field whitelist"]
}
```

The preview is sorted newest-first by report date and server-modified timestamp. It contains no storage quota, ingest path, pruning reason, private archive state, or other operational metadata.

The browser should request and render the preview immediately, then fetch the full catalog in the background and atomically replace/merge the list. During this phase it should state “正在加载完整索引” rather than presenting an empty result. A search submitted before the full catalog arrives should remain visibly pending and re-run once the full catalog is ready; it must not imply that the preview is the complete result set.

Preview and full catalog share the same schema/update version. The browser only
promotes a full catalog that is at least as new as the preview; a cache mismatch
causes a reload instead of making newly visible reports disappear. Full-catalog
derived maps are built cooperatively in chunks and swapped atomically, keeping
the input event loop responsive while the larger payload arrives.

Document-body search is opt-in. The build writes a manifest plus current text
shards capped at roughly 3 MiB each; the browser loads and merges them
progressively, yielding between shards. It never parses the legacy monolithic
text index during ordinary title/catalog search or merely by opening a report
detail page.

## Sitemaps, robots, and AI discovery

- `sitemap.xml` is a sitemap index for pages, sharded report URLs, and sharded Blog URLs.
- The China-focused flat sitemaps contain the same canonical public pages while remaining below sitemap size limits.
- `lastmod` reflects a meaningful catalog/article update. `priority` is retained only for compatibility; Google ignores `priority` and `changefreq`.
- IndexNow submissions point only to canonical public URLs and never include passwords, delivery tokens, or internal query state.
- `OAI-SearchBot` and `PerplexityBot` are allowed to discover public pages. `GPTBot` and `Google-Extended` are blocked so search visibility remains separate from bulk model-training controls.
- `/api/`, private data, delivery pages, and personalized newsfeed pages remain disallowed. The public full catalog can be allowed deliberately; the small preview does not need to be indexed.
- `llms.txt` gives a short site map and attribution rules. `llms-full.txt` exposes bounded report metadata, canonical citation URLs, citable summaries, and only the latest Blog metadata. Neither file should expose report bodies, access tokens, repository identity, runtime secrets, or private storage paths.

## Internal linking and content hierarchy

Discovery should work without client JavaScript:

1. Home links to report index, Blog, charts, courses when present, and About.
2. Report index pages link to report details and the institution/topic hub.
3. Report details link back to the collection, their exact institution/topic fragments, related reports, and the dynamic access page.
4. Blog collection pages link to every article in that page and to adjacent collection pages.
5. About links to the primary discovery routes and explains the metadata methodology in visible text.

The topic hub groups every current institution and research topic. Large names naturally rank first by record count, while one-report groups still receive a working fragment target. The hub is a navigation aid, not a claim that all included reports are endorsed or equally important.

## Page experience targets

Target the Core Web Vitals thresholds Google recommends for a good experience at the 75th percentile:

- LCP at or below 2.5 seconds.
- INP below 200 milliseconds.
- CLS at or below 0.1.

The static collection pagination prevents a multi-megabyte 12,000-record HTML response. The catalog preview prevents a blank first paint while the full search catalog loads. Search input should be debounced, expensive indexing work should stay off the input event, and all asynchronous actions should expose an immediate status, skeleton, or determinate phase before waiting on the network.

Measure real-user p75 mobile and desktop performance rather than relying only on a local synthetic run. Track LCP element, resource timing for preview/full catalog/search shards, INP interaction name, JS exceptions, and the percentage of sessions that ever see an empty report state.

## Measurement and operating checklist

At each production release:

1. Run `python3 scripts/test_portal_seo.py` and `python3 scripts/test_portal_blog_build.py`.
2. Confirm every sitemap URL resolves, has one self-canonical, and is not `noindex`.
3. Validate a report and Blog article JSON-LD graph; compare structured fields to visible text.
4. Confirm report pagination page counts and Blog pagination page counts match their collection totals.
5. Confirm `catalog_preview.json` has at most 40 items and only public-whitelisted item keys.
6. Confirm preview/full schema and update versions, total count, and latest index date agree.
7. Confirm OAI-SearchBot remains allowed while GPTBot remains blocked.
8. Submit/monitor sitemaps in Google Search Console and Bing Webmaster Tools; inspect index coverage, discovered-vs-indexed URLs, crawl errors, canonical selection, search queries by country/device, and Core Web Vitals.
9. Use IndexNow only for newly added, updated, or deleted canonical pages.

For analytics, collect only the minimum aggregate events needed to improve discovery and interaction: landing path, referrer/search campaign, country/language at coarse resolution, search started/completed, result count, preview/full-catalog readiness, report-detail open, and latency bucket. Do not emit raw account identifiers, email addresses, access tokens, full private queries, or repository/build identity.

## Public-source privacy boundary

Public source and generated artifacts may contain the KC桌面 brand and neutral placeholders. They must not contain the production origin, repository owner or repository URL, personal email addresses, secret names that reveal infrastructure, private storage paths, or credentials. Production origin, support contact, worker route, and verification tokens are materialized by the deployment environment and must not be written back to source, logs, or public artifacts beyond the intended public values.

## Primary references

- Google Search Central, [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- Google Search Central, [Top ways to ensure your content performs well in Google's AI experiences](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Google Search Central, [Managing multi-regional and multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
- Google Search Central, [Tell Google about localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- Google Search Central, [Pagination, incremental page loading, and Search](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
- Google Search Central, [Consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- Google Search Central, [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- Google Search Central, [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Google Search Central, [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals)
- Google Search Central, [Structured data general guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- Google Search Central, [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article)
- Google Search Central, [Breadcrumb structured data](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)
- Schema.org, [`Report`](https://schema.org/Report)
- Bing Webmaster Tools, [Sitemaps](https://www.bing.com/webmasters/help/Sitemaps-3b5cf6ed)
- Bing Webmaster Tools, [IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby)
- IndexNow, [protocol documentation](https://www.indexnow.org/documentation)
- OpenAI, [guidance for allowing OpenAI web crawlers](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers)
