# SEO / GEO architecture for KC桌面

This document defines the public discovery contract for the generated report site. It is intentionally written against the neutral build origin `https://portal.example.invalid`; production identity and routing are materialized outside the public source tree.

This is the implementation architecture, not a future-state proposal. When code and this document disagree, the release must stop until the generator, tests, and this document describe the same public contract.

## Goals and non-goals

The site should be discoverable by global Simplified-Chinese readers searching for investment-bank research, macro strategy, industry research, company research, filings, think-tank reports, and charts. English institution names, company names, tickers, and source titles remain searchable because those are often the terms a Chinese reader actually uses.

The site does not claim authorship, ownership, or publication rights over an underlying report. It publishes a free metadata and discovery page. Report access is a separate, dynamic capability whose current state must not be inferred from an old search snippet.

“GEO” does not have a special Google markup or shortcut. The implementation therefore uses the same crawlability, text quality, structured data, internal linking, page experience, and attribution fundamentals used for conventional search. `llms.txt` is a secondary machine-readable aid, not a substitute for crawlable HTML or a Google ranking signal.

## Implementation map and sources of truth

| Responsibility | Current source of truth |
| --- | --- |
| Hand-authored page shells and first-paint metadata | `portal_suite/site_src/*.html` and `portal_suite/site_src/assets/` |
| Catalog filtering, static HTML, canonical metadata, JSON-LD, sitemaps, robots, feeds, `llms*`, and asset versioning | `scripts/build_portal_suite_site.py` |
| Report and search inputs retained between builds | `portal_suite/data/catalog*.json`, `portal_suite/data/search_index.json`, and the configured Blog archive |
| Static release build, validation, slot selection, upload, edge activation, live checks, and IndexNow ordering | `.github/workflows/neutral-edge-cutover.yml` |
| Incremental inactive-slot upload and manifest/tree digest | `scripts/publish_static_slot.py` |
| Canonical redirects, clean-path resolution, R2 reads, cache headers, API forwarding, and release probes | `workers/edge-static-host/src/index.js` |
| Changed-URL selection and IndexNow submission | `scripts/submit_portal_indexnow.py` |
| Regression contracts | `scripts/test_portal_seo.py`, `scripts/test_portal_blog_build.py`, `portal_suite/tests/*.test.mjs`, `workers/edge-static-host/test/index.test.mjs`, `scripts/test_publish_static_slot.py`, and `scripts/test_edge_route_cutover.py` |

The generated `_neutral_site/` directory is an ephemeral release artifact. Never hand-edit it or treat it as source. Durable SEO changes start in the page shells or generator, are asserted in tests, and are then rebuilt through the workflow.

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
| Legal policies | `/terms.html`, `/privacy.html` | Static source documents retained in `sitemap-pages.xml`; outside the generated structured-discovery graph |

Each paginated page is independently canonical. Do not canonicalize every page to page 1. Pagination must remain ordinary `<a href>` navigation; buttons or JavaScript-only state are not a crawl path.

Dynamic report, document, delivery, and personalized newsfeed pages stay `noindex`. Their query parameters can contain transient application state and should not become canonical discovery URLs.

## Language and entity signals

- Public pages use `lang="zh-Hans"`, `hreflang="zh-Hans"`, and a same-page `x-default` alternate.
- Do not add `hreflang="en"` until a real English page exists at a distinct URL. English keywords inside a Chinese page are not an English localization.
- The only public entity name is `KC桌面`; historical English deployment identities are not emitted as aliases.
- Titles and descriptions cover both Chinese intent and high-value English query vocabulary such as “Chinese financial research”, “investment bank research”, “equity research”, “macro research”, institution names, companies, and tickers.
- Legacy neutral editorial labels are normalized to `KC桌面` only at the public rendering edge. Immutable source archives and their fingerprints do not change.

## Metadata, canonical, social, and JSON-LD contract

The SEO-generated discovery pages are server-readable HTML and carry a single production-origin canonical URL. They also carry `index,follow`, a title and description, and `zh-Hans` plus `x-default` alternates. Open Graph metadata is emitted for home, report collections/details, the Bernstein hub, Blog, and Charts; the topic and About pages currently rely on their standard title, description, canonical, alternates, and JSON-LD. Home, report details, and Blog pages use the configured 1200×630 social card; Blog pages also expose a large-image Twitter card. The build rewrites production identity before these pages are generated and asset URLs are content-versioned after generation.

The current structured-data graph is page-specific:

| Page family | Structured data generated today |
| --- | --- |
| Home | `WebSite` + `Organization`, including the title-search `SearchAction` |
| Report collection and topic/institution hubs | `CollectionPage`/`ItemList` as applicable + `BreadcrumbList` |
| Static report detail | `WebPage` + `Report` + `BreadcrumbList` |
| Blog collection | `Blog` with visible-page `BlogPosting` entries |
| Blog article | `BlogPosting` + `WebPage` + `BreadcrumbList` |
| Charts | `CollectionPage` + `BreadcrumbList` |
| About/methodology | `Organization` + `WebSite` + `AboutPage` + `BreadcrumbList` |

Canonical and structured URLs must use the configured HTTPS origin, never the neutral placeholder, an alias host, a query-string detail URL, or a release-probe URL. The edge redirects `/reports/index.html` to `/reports/`, `/blog/index.html` to `/blog/`, `/charts.html` to `/charts`, and configured alias hosts to the canonical host while preserving the query string. Dynamic application pages remain followable but are not canonical discovery documents.

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

## Text-only report SEO and user guidance

A Text-only state means the catalog does not currently expose a directly downloadable, non-archived PDF (`available` is false, or `pdf_archived` is true). That access state does not remove the catalog record from search discovery:

- `/reports/{opaque-id}.html` remains the indexable, self-canonical metadata page with catalog-backed title, description, availability label, citable summary, attribution, related reports, and JSON-LD.
- `report.html?...` remains `noindex,follow`; it is the interactive access/detail view and must not compete with the static canonical page.
- Both the static page and the dynamic detail first paint tell the reader that about 90% of Text-only reports can be found by searching the complete title on the home page, including in “其他报告”等板块.
- The call to action links directly to `/?q=<complete-title>` (bounded to 200 characters), so the user reaches a prefilled home search instead of having to copy the title manually.
- Hydration repeats the same guidance; it must not replace it with a blank loading state or an email-only dead end.
- This guidance does not claim that a PDF exists, change the canonical URL, synthesize report authorship, or turn access state into publication metadata.

The behavior is covered at three layers: `scripts/test_portal_seo.py` checks generated static HTML, `portal_suite/tests/report-detail-performance.test.mjs` checks the inline first paint, and `portal_suite/tests/text-only-frontend.test.mjs` checks hydrated behavior, direct search links, and mobile presentation.

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

- `sitemap.xml` is a sitemap index referencing `sitemap-pages.xml`, sharded `sitemap-reports-N.xml` files, and sharded `sitemap-blog-N.xml` files.
- `sitemap-baidu.xml` and `sitemap-sogou.xml` are flat China-focused variants containing the same canonical public page families while remaining below sitemap size limits.
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

## Build order

The production workflow owns the order because the public repository intentionally contains a neutral origin and neutral deployment placeholders:

1. Validate the neutral public source and run the full source-level regression suite.
2. Materialize the private deployment profile, production origin, verification values, and public assets in the runner. `SITE_BASE_URL` is therefore production-correct before the generator executes.
3. Refresh and translate the catalog while preserving the previous live/archive/history catalogs for change detection.
4. `scripts/build_portal_suite_site.py` copies `portal_suite/site_src` into `_neutral_site`, replacing any previous output.
5. The generator public-filters the live catalog, merges history and archive records, builds the full-text indexes, and writes current/history search shards.
6. It writes public runtime JSON: full/preview/recommendation catalogs, search index, public password rules, and worker configuration; retained archive/search state is persisted separately from the release output.
7. It builds Blog collection/article pages from current drafts plus the configured archive.
8. It generates static report pages, paginated collections, hubs, About, report-detail shards, sitemaps, feed, IndexNow proof file, `robots.txt`, `llms.txt`, and `llms-full.txt`; the same pass enhances home and Charts metadata/entity graphs.
9. It materializes the public contact alias in generated crawlable content and appends content hashes to JavaScript and stylesheet references.
10. The workflow merges the private chart-search index into the release and checks required files, bounded file count/size, symlink absence, and placeholder removal before upload.

Changing this order can produce mixed-origin canonicals, stale discovery files, mismatched schemas, or unhashed assets. The generator and workflow order are therefore part of the SEO contract.

## Cloudflare release and discovery publication path

The site is published as an immutable, double-buffered R2 static tree behind `workers/edge-static-host`:

1. The workflow reads `/.well-known/edge-state` to identify the active `a` or `b` slot.
2. `scripts/publish_static_slot.py` uploads the generated tree incrementally to the inactive slot, then records the release ID and tree SHA-256.
3. The edge Worker is deployed with `STATIC_PREFIX`, `STATIC_RELEASE`, `STATIC_TREE_SHA256`, the canonical host, the R2 `STATIC_BUCKET` binding, and the `API` service binding.
4. The workflow verifies the new state, canonical routes, refreshed catalog, and generated discovery/report-detail assets. Release-specific `/.well-known/edge-release/{release}/...` probes are current-release-only and `no-store`, so they can validate the exact artifact without becoming canonical URLs.
5. Only after public and release-specific discovery checks pass does `scripts/submit_portal_indexnow.py` verify the public key file and submit changed canonical URLs. It compares current and previous catalogs, adds generated public Blog/hub pages, deduplicates URLs, and chunks requests at 10,000 URLs.
6. The runner reverses private materialization before any retained data is committed. Old releases are pruned only after upload, Worker deployment, state, catalog, and discovery checks all succeed.

The edge serves HTML with short freshness, runtime JSON with its own freshness policy, XML/TXT discovery files with an SEO cache policy, and content-versioned assets as immutable. A successful build alone is not a published SEO release; edge activation and recipient-visible discovery checks are separate gates.

## Regression and production acceptance

The repository-level regression set is executable without a production origin:

```sh
python3 -B scripts/check_public_identity.py
node --check portal_suite/site_src/assets/app.js
node --test portal_suite/tests/*.test.mjs
python3 -B scripts/test_portal_seo.py
python3 -B scripts/test_portal_blog_build.py
node --test workers/edge-static-host/test/index.test.mjs
python3 -B scripts/test_publish_static_slot.py
python3 -B scripts/test_edge_route_cutover.py
```

The GitHub Action is the authoritative full build because it materializes the configured origin and private runtime inputs. After activation, its live acceptance must cover these independently:

1. `/.well-known/edge-state` equals the prepared slot, release ID, and tree digest.
2. `/`, `/reports/`, one static report, `/blog/`, one Blog article, `/charts`, `/about.html`, `robots.txt`, `sitemap.xml`, a report sitemap shard, `llms.txt`, and `llms-full.txt` resolve through `edge-static`.
3. Each sampled indexable HTML page has one production-origin self-canonical, is not `noindex`, and has visible text matching its description and JSON-LD.
4. `report.html?...` is still `noindex,follow`, while the corresponding static report remains in the report sitemap. A Text-only sample has the visible 90% guidance and a correctly encoded, prefilled home-search link.
5. Legacy HTML paths and any alias host return the expected permanent canonical redirect.
6. `robots.txt` names every generated sitemap and preserves the intended search-versus-training crawler policy; sitemap counts and pagination totals agree with the generated catalog and Blog archive.
7. The release-specific discovery files match the public files, the IndexNow proof file is live, and IndexNow runs only after those checks.

A read-only operator can reproduce the core live discovery check without embedding the production origin in source:

```sh
portal_site_url="https://configured-production-origin"
curl --fail --silent --show-error "$portal_site_url/.well-known/edge-state"
curl --fail --silent --show-error "$portal_site_url/robots.txt"
curl --fail --silent --show-error "$portal_site_url/sitemap.xml"
curl --fail --silent --show-error "$portal_site_url/llms.txt"
curl --fail --silent --show-error "$portal_site_url/reports/"
curl --fail --silent --show-error "$portal_site_url/blog/"
```

For a pre-submission URL audit against a built release, use IndexNow dry-run mode; it prints the count, public key location, and a sample without sending a request:

```sh
python3 -B scripts/submit_portal_indexnow.py \
  --catalog _neutral_site/data/catalog.json \
  --site-dir _neutral_site \
  --base-url "$portal_site_url" \
  --dry-run
```

## Measurement and operating checklist

At each production release:

1. Run the repository regression set above before materialization and retain the generated-artifact checks before upload.
2. Confirm every generated discovery URL in the sitemaps resolves, has one self-canonical, and is not `noindex`; separately confirm the retained legal-policy URLs resolve.
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
