# Search-engine submission matrix

This runbook separates independent indexes from downstream result providers and AI search crawlers. It uses the neutral origin `https://portal.example.invalid`; the scheduled workflow receives the deployed HTTPS origin through `PORTAL_SITE_URL`. A row marked “automated” describes repository capability, not proof that a third-party account accepted a submission. Acceptance must come from the relevant deployment log or webmaster console.

## Live Cloudflare robots boundary

Production `robots.txt` is currently emitted by Cloudflare Managed robots before the application Worker. The managed block explicitly permits ordinary search indexing with `Content-Signal: search=yes` and separately controls model-training agents, but it may omit a `Sitemap:` line. Both canonical-host and `www` requests for this managed file can therefore return HTTP 200 at the platform layer (a `Location` header alone is not a redirect status); the application Worker cannot turn that managed-file response into a path-level 301.

The repository still publishes the canonical `/sitemap.xml` and all engine-specific discovery files independently. The daily audit recognizes only the explicit `BEGIN/END Cloudflare Managed Content` block with wildcard `search=yes` before treating a missing robots Sitemap line as a named warning. It continues to fetch and fully validate `/sitemap.xml`; `search=no`, wildcard `Disallow: /`, malformed discovery XML, missing shards, off-origin URLs, duplicates, or non-indexable samples remain failures. A self-managed robots file must still advertise the canonical Sitemap.

Account action: keep a private record of the Cloudflare Managed robots setting and its last review date, verify that `search=yes` remains enabled, and determine in the Cloudflare dashboard whether a canonical Sitemap directive can be preserved alongside managed content. If the platform cannot preserve it, submit `/sitemap.xml` directly in each webmaster console and retain the console/API acceptance evidence. Do not change the model-training choices as part of this SEO check.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| Automated | A release can notify the service without an interactive webmaster session. The live proof file and response still have to pass. |
| Account action | The engine requires site ownership, a signed-in console, an API token, or an invitation. Credentials are never committed to public source. |
| Manual review | A public form exists, but acceptance is reviewed by the engine and is not an API guarantee. |
| Passive/downstream | There is no useful independent site-submission action. Keep the site crawlable and maintain the upstream indexes named in the row. |

## Independent indexes and submission roots

| Service | Independent index | Current repository coverage | Official submission or control point | Operator action and evidence |
| --- | --- | --- | --- | --- |
| [IndexNow](https://www.indexnow.org/faq) | Protocol shared by participating engines | Automated changed-URL selection exists; the daily audit verifies the root key file. One global endpoint can share notifications with Amazon, Bing, Naver, Seznam, Yandex, and Yep. | [Protocol documentation](https://www.indexnow.org/documentation) | Send only new, materially updated, redirected, or deleted canonical URLs after a successful public release. Retain response status and submitted/reason counts in the release log. Do not repeatedly submit unchanged sitemap contents. |
| [Google Search](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | Yes | Crawlable HTML, a canonical sitemap index, and structured data are generated. Cloudflare Managed robots currently permits search but may omit robots-level Sitemap discovery. There is no anonymous sitemap-ping fallback. | [Search Console sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps/submit) or the Search Console UI | Account action: verify the exact canonical property, submit `/sitemap.xml`, and record the property plus last accepted date privately. The [Indexing API](https://developers.google.com/search/apis/indexing-api/v3/quota-pricing) is limited to qualifying `JobPosting` and livestream pages and must not be used for ordinary reports. Google retired its old unauthenticated sitemap ping endpoint. |
| [Bing](https://learn.microsoft.com/en-us/bingwebmaster/) | Yes | IndexNow provides release notifications; the canonical sitemap remains available for console monitoring. | Bing Webmaster Tools and its current REST API | Account action: verify the site and submit `/sitemap.xml`; retain indexed/crawl-error counts. Do not build against the retiring SOAP/POX interfaces. |
| [Baidu](https://ziyuan.baidu.com/college/articleinfo?id=3217) | Yes | A flat `/sitemap-baidu.xml` is generated because this intake does not consume a sitemap index. | Baidu Search Resource Platform | Account action: verify the site and submit the flat file or use the authenticated push token. Keep each file within 50,000 URLs and 10 MB. Store the token only as an encrypted workflow secret. |
| [Sogou](https://zhanzhang.sogou.com/index.php/sitelink/index) | Yes | A flat `/sitemap-sogou.xml` is generated independently of the Cloudflare Managed robots response. | [URL submission](https://help.sogou.com/submit.html); [sitemap help](https://zhanzhang.sogou.com/index.php/help/sitemap) | Manual/account action: submit the canonical home URL; sitemap access is invitation-controlled. Record the console state without claiming acceptance from a form submission alone. |
| [360 Search](https://info.so.360.cn/site_submit.html) | Yes | Standard crawl discovery is available; there is no repository credential. | Public one-time site form; [verified sitemap guidance](https://www.so.com/help/help_3_3.html) | Manual review for the canonical home URL, then account action for sitemap management if offered. Retain the submitted date and visible console result. |
| [Shenma](https://zhanzhang.sm.cn/open/helpsitemap) | Yes, mobile focused | Standard crawl discovery and a flat Chinese sitemap are available. | Shenma Webmaster Platform | Account action: verify ownership and submit the supported sitemap/feed in the console. Keep mobile rendering and canonical parity under observation. |
| [Yandex](https://yandex.com/support/webmaster/en/indexing-options/sitemap) | Yes | IndexNow can notify Yandex; the canonical sitemap is also available. | Yandex Webmaster; [recrawl API](https://yandex.com/dev/webmaster/doc/en/reference/host-recrawl-post) | Account action: verify the host and register `/sitemap.xml`. Use recrawl requests only for bounded important changes and retain API results. |
| [Naver](https://searchadvisor.naver.com/guide/request-feed) | Yes | IndexNow can notify Naver; sitemap and RSS discovery files are generated. | Naver Search Advisor: [crawl requests](https://searchadvisor.naver.com/guide/request-crawl) and feed/sitemap UI | Account action: verify the site, register sitemap/RSS, and monitor collection status. Its [crawl-request API](https://searchadvisor.naver.com/guide/crawl-request-api) is partner-scoped, so do not assume general API access. |
| [Brave Search](https://search.brave.com/help/brave-search-crawler) | Yes | Normal crawl access is available through robots; no account token is stored. | [Public URL submission form](https://search.brave.com/submit-url) | Manual review: submit the canonical root once and retain the visible confirmation. Ongoing discovery should come from crawlable links and sitemaps, not repeated form entries. |
| [Daum](https://register.search.daum.net/info.daum?act=info) | Yes | Normal crawl discovery is available. | Daum Search Registration | Manual review: submit the canonical site entry and record the review outcome. Do not label the site indexed until a Daum result or console state confirms it. |
| [Seznam](https://o-seznam.cz/napoveda/odkazy/nejcastejsi-otazky-k-odkazum/jak-pridam-odkaz/) | Yes | Covered by IndexNow and ordinary crawling. | IndexNow; Seznam directory is intended for Czech/Slovak sites | No separate directory action for an unrelated-language site. Verify IndexNow delivery and crawler access. |
| [Yep](https://yep.com/yepbot/) | Yes | Covered by IndexNow; Ahrefs/Yep crawling is not blocked by the committed robots policy. | IndexNow and YepBot documentation | No account submission needed. Watch server logs and public search presence. |
| [Mojeek](https://blog.mojeek.com/2020/12/frequently-asked-questions-about-mojeek-search-engines-technology-stack.html) | Yes | Standard links, sitemaps, and default crawler access. | No add-URL service | Passive discovery only; do not invent a submission endpoint. |
| [Qwant](https://help.qwant.com/bot/) | Mixed own crawl and external sources | Standard crawler access and upstream Bing coverage. | [Missing-site support guidance](https://help.qwant.com/en/docs/qwant-search/survey-monkey/how-to-get-my-website-listed-on-qwant) | Passive first. Contact support only after the canonical site remains absent, and retain the case response. |

## Downstream result providers

These services do not expose a distinct webmaster action that adds value beyond keeping their upstream indexes healthy.

| Service | Result source / official guidance | Action |
| --- | --- | --- |
| [DuckDuckGo](https://duckduckgo.com/duckduckgo-help-pages/results/sources) | Combines multiple sources, prominently including Bing | Maintain Bing, IndexNow, crawlability, and canonical consistency. |
| [Yahoo Search](https://help.yahoo.com/kb/search-for-mobile-web/submit-website-yahoo-search-sln2217.html) and AOL | Web results are supplied through Bing | Maintain the verified Bing property; no second submission. |
| [Ecosia](https://support.ecosia.org/article/579-search-results-providers) | Uses external search providers by market | Maintain the relevant upstream index; no separate site submission. |
| [Startpage](https://support.startpage.com/hc/en-us/articles/5138782571796-Why-isn-t-a-particular-site-appearing-in-the-results) | Privacy layer over upstream results | Resolve absence in the upstream engine; no separate webmaster console. |

## AI search and answer crawlers

AI discovery is a crawler-access and source-quality problem, not a separate mass-submission queue. Public HTML, self-canonicals, visible attribution, internal links, and source-grounded structured data remain the primary contract.

| Service | Search crawler / source | Current action |
| --- | --- | --- |
| [OpenAI search](https://developers.openai.com/api/docs/bots) | `OAI-SearchBot`; user-triggered retrieval may use `ChatGPT-User` | Both search/retrieval agents are explicitly allowed for public pages. `GPTBot` remains separately blocked for training. There is no webmaster submission form to automate. |
| [Perplexity](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) | `PerplexityBot` and user retrieval agent | Public-page access is explicitly allowed. Maintain canonical citation URLs and clear source attribution. |
| [Claude search](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | `Claude-SearchBot` and user retrieval agent | Search/retrieval access is explicitly allowed; training controls remain separate. |
| [Google AI experiences](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Google Search index | No special submission or AI-only markup. Maintain Google indexing fundamentals and Search Console evidence. |
| [Applebot](https://support.apple.com/en-ie/119829) | Apple search, Siri, and Spotlight discovery | Default public crawl access is available. Maintain ordinary robots, sitemap, canonical, and structured-data health; no generic URL submission is claimed. |

## Daily health and account handoff

`.github/workflows/portal-seo-health.yml` runs a read-only check every day and on manual dispatch. It receives the production origin and public IndexNow key at runtime, then checks:

1. `robots.txt` HTTP 200 and wildcard crawlability; Cloudflare Managed `search=yes` is recorded, while a missing robots Sitemap directive becomes an explicit warning only for that managed response. The canonical `/sitemap.xml`, every declared shard, URL counts, duplicate and off-origin entries are always validated independently.
2. A deterministic cross-shard HTML sample for HTTP 200, indexability, one self-canonical, and basic JSON-LD.
3. The public IndexNow proof file, favicon/brand icon, and an unqualified `www` root request returning HTTP 301 to the canonical root.
4. A one-day aggregate artifact and GitHub step summary. Any failed category fails the job and invokes the existing operations-alert workflow.

The workflow does not sign in to webmaster consoles and does not claim third-party acceptance. For every account/manual row above, keep a private ledger with: engine, verified property, owner account, submission mechanism, submitted discovery file, last attempted time, accepted/failed state, and a console screenshot or API response identifier. Never put console tokens, verification secrets, private account addresses, or production identity in this public document.
