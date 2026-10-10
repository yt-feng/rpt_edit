"""Text-only public previews: never serialize private commentary or originals."""
from html import escape
from pathlib import Path
import re
from portal_english_commentary import ID, text, require
from portal_extended_locales import ORIGIN, digest, publication_day, stable_bytes

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT/'portal_suite/locale_assets'
PUBLIC_KEYS = ('id', 'title', 'preview', 'datePublished')
PUBLIC_ASSET_NAMES = ('styles.css', 'blog.css', 'extended-locales.css', 'english-commentary.css',
                      'app.js', 'english-commentary.js', 'extended-locales.js')


def preview_item(item):
    require(isinstance(item, dict) and all(key in item for key in PUBLIC_KEYS))
    value = {key: item[key] for key in PUBLIC_KEYS}
    require(isinstance(value['id'], str) and ID.fullmatch(value['id']))
    require(publication_day(value['datePublished']) == value['datePublished']
            and value['id'][:8] == value['datePublished'].replace('-', ''))
    text(value['title'], 500, english=True); text(value['preview'], 640, english=True)
    return value


def ui_assets():
    return {'assets/'+name: (ASSETS/name).read_bytes()
            for name in ('english-commentary.js', 'english-commentary.css', 'extended-locales.js', 'extended-locales.css')}


def head(title, preview, canonical, *, approved=False, article=None, asset_hashes=None):
    if asset_hashes is not None:
        require(isinstance(asset_hashes, dict) and set(asset_hashes) == set(PUBLIC_ASSET_NAMES)
                and all(isinstance(value, str) and re.fullmatch(r'[a-f0-9]{64}', value)
                        for value in asset_hashes.values()), 'English public asset identity differs')
    def version(name):
        if asset_hashes is not None:
            return asset_hashes[name][:12]
        base = ASSETS if name in {'english-commentary.js', 'english-commentary.css', 'extended-locales.js', 'extended-locales.css'} \
            else ROOT/'portal_suite/site_src/assets'
        return digest((base/name).read_bytes())[:12]
    css = ''.join(f'<link rel="stylesheet" href="/assets/{name}?v={version(name)}">'
                  for name in ('styles.css', 'blog.css', 'extended-locales.css', 'english-commentary.css'))
    scripts = ''.join(f'<script defer src="/assets/{name}?v={version(name)}"></script>'
                      for name in ('app.js', 'english-commentary.js', 'extended-locales.js'))
    schema = {'@context': 'https://schema.org', '@type': 'BlogPosting' if article else 'CollectionPage',
              'url': canonical, 'headline': title, 'description': preview, 'inLanguage': 'en'}
    if article:
        schema.update(datePublished=article['datePublished'], isAccessibleForFree=False,
                      author={'@type': 'Organization', 'name': 'KC Commentary'},
                      hasPart={'@type': 'WebPageElement', 'isAccessibleForFree': False, 'cssSelector': '#englishFullCommentary'})
    # No articleBody, image, original URL, source digest, embedded chart or body
    # JSON is permitted in structured data, JS state, HTML comments or cards.
    jsonld = stable_bytes(schema).decode().replace('<', '\\u003c')
    robots = 'index,follow' if approved else 'noindex,follow'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title><meta name="description" content="{escape(preview, quote=True)}">
<meta name="robots" content="{robots}"><link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">{css}{scripts}
<script type="application/ld+json">{jsonld}</script></head>'''


def chrome():
    return '''<header class="topbar blog-topbar"><a class="brand compact" href="/en/">KC Commentary</a>
<nav class="topbar-actions" aria-label="Navigation"><a class="topbar-link" href="/en/">Commentary</a>
<button id="accountGate" class="account-button" type="button">Sign in</button>
<button class="account-button signup-button" type="button" data-auth-open="register" data-auth-placement="english_commentary" data-guest-only>Register</button>
</nav></header>'''


def footer():
    return '''<footer class="legal-footer blog-footer"><a href="/en/">English commentary</a>
<a href="/terms.html">Terms</a><a href="/privacy.html">Privacy</a>
<button type="button" class="inline-request-button" data-membership-request-open="access">Membership request</button></footer>'''


def detail(item, *, approved=False, asset_hashes=None):
    value = preview_item(item)
    canonical = f'{ORIGIN}/en/blog/{value["id"]}.html'
    return (head(value['title'], value['preview'], canonical, approved=approved, article=value,
                 asset_hashes=asset_hashes) +
            f'''<body class="blog-page blog-article-page extended-page english-commentary-page" data-page="english-commentary">
{chrome()}<main class="blog-article-shell"><a class="blog-back" href="/en/">← Commentary</a>
<article class="blog-article"><header class="blog-article-header"><time datetime="{value['datePublished']}">{value['datePublished']}</time>
<h1>{escape(value['title'])}</h1><p class="blog-digest">{escape(value['preview'])}</p></header>
<aside class="notice"><p>Our secondary interpretation only. No original report text, charts or document downloads.</p>
<p>Sign in for 3 free full commentary reads per account. Re-reading an unlocked comment does not use another read.
After the allowance, join as a website member to continue.</p></aside>
<section class="english-read-gate" aria-label="Read commentary">
<button id="englishRead" class="account-button" type="button" data-commentary-id="{value['id']}">Read full commentary</button>
<p id="englishReadStatus" role="status" aria-live="polite">Only the preview is public.</p>
<button id="englishMembership" class="account-button" type="button" data-membership-request-open="access" hidden>Join as a member</button>
</section><div id="englishFullCommentary" class="blog-article-content" data-nosnippet hidden></div>
<noscript><p>JavaScript and sign-in are required to read full commentary. The preview remains available.</p></noscript>
</article></main>{footer()}</body></html>\n''').encode()


def homepage(items, *, approved=False, asset_hashes=None):
    require(isinstance(items, list) and 1 <= len(items) <= 5000, 'English collection needs real completed previews')
    values = [preview_item(item) for item in items]
    require(len({item['id'] for item in values}) == len(values), 'Duplicate English preview ID')
    values.sort(key=lambda row: row['id'], reverse=True)
    cards = ''.join(f'''<article class="blog-card extended-result" data-kind="blog" data-date="{row['datePublished']}">
<div class="blog-card-meta"><time datetime="{row['datePublished']}">{row['datePublished']}</time><span>KC commentary</span></div>
<h2><a href="/en/blog/{row['id']}.html">{escape(row['title'])}</a></h2><p>{escape(row['preview'])}</p></article>'''
                    for row in values)
    return (head('English commentary | KC Commentary', 'Our latest secondary interpretations. Public previews; member full reading.',
                 ORIGIN+'/en/', approved=approved, asset_hashes=asset_hashes) +
            f'''<body class="blog-page extended-page english-commentary-page" data-page="english-commentary">
{chrome()}<main class="blog-shell"><h1>English commentary</h1>
<aside class="notice">Public summaries of our secondary interpretation, not original reports. No charts or original document downloads.</aside>
<section class="search-panel" aria-label="Search commentary previews">
<label>Search<input id="extendedSearch" type="search" placeholder="Keywords or a phrase" autocomplete="off"></label>
<label>Type<select id="extendedType"><option value="">Commentary only</option><option value="blog">Commentary</option></select></label>
<label>From<input id="extendedFrom" type="date"></label><label>To<input id="extendedTo" type="date"></label>
<label>Sort<select id="extendedSort"><option value="newest">Newest</option><option value="oldest">Oldest</option></select></label>
<button id="extendedClear" class="account-button" type="button">Clear</button></section>
<p id="extendedCount" role="status" aria-live="polite">{len(values)} previews</p>
<section id="extendedResults" class="blog-card-grid">{cards}</section><p id="extendedEmpty" hidden>No matching commentary.</p>
<nav class="pagination-bar" aria-label="Commentary pages"><button id="extendedPrev" type="button">Previous</button>
<span id="extendedPage">1</span><button id="extendedNext" type="button">Next</button></nav>
</main>{footer()}</body></html>\n''').encode()
