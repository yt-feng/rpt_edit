"""Pure, narrowly scoped discovery of an explicitly named Fiscal Monitor chapter.

The source has no DOI. A complete bounded Crossref book search must identify one
publisher record by series, month, chapter number and exact chapter title; an
independent exact-DOI response must then agree. Returned URLs still need live
publisher-page and PDF identity verification. This module performs no I/O.
"""
from calendar import month_abbr, month_name, monthrange
from datetime import datetime
from functools import wraps
import hashlib
import html
import re
from urllib.parse import urlsplit

from imf_elibrary_resolver import (_Document, digest, isbn_valid, source_url,
                                  title_key, validate_landing_metadata, validate_official_pair, validate_publication_url)

METADATA_FIELDS = {'method', 'preview_sha256', 'search_sha256', 'search_total_results',
                   'exact_crossref_sha256', 'chapter', 'year', 'month', 'book_title', 'book_subtitle'}
SOURCE_FIELDS = {'source_guid', 'source_url', 'source_title', 'published', 'year', 'month',
                 'chapter', 'preview_sha256', 'identity_sha256', 'query_params'}


class FiscalChapterError(ValueError):
    category = 'imf_fiscal_chapter_invalid'
    def __init__(self):
        super().__init__(self.category)


def require(value):
    if not value:
        raise FiscalChapterError()


def checked(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except (ValueError, TypeError, KeyError, IndexError, AttributeError, OverflowError):
            raise FiscalChapterError() from None
    return wrapped


def sha(value):
    return isinstance(value, str) and re.fullmatch(r'[a-f0-9]{64}', value) is not None


def query_params(title, year, month):
    last = monthrange(int(year), int(month))[1]
    return {'query.bibliographic': f'{title} Fiscal Monitor {month_name[int(month)]} {year}',
            'filter': f'prefix:10.5089,type:edited-book,from-pub-date:{year}-{month}-01,until-pub-date:{year}-{month}-{last:02}',
            'rows': 100, 'offset': 0}


def validate_source(source):
    require(type(source) is dict and set(source) == SOURCE_FIELDS)
    require(isinstance(source['source_title'], str) and 0 < len(source['source_title']) <= 4096
            and len(title_key(source['source_title']).split()) >= 4
            and not re.search(r'[\x00-\x1f\x7f\ud800-\udfff]', source['source_title'])
            and isinstance(source['source_guid'], str) and 0 < len(source['source_guid']) <= 4096
            and not re.search(r'[\x00-\x1f\x7f\ud800-\udfff]', source['source_guid'])
            and type(source['chapter']) is int and 1 <= source['chapter'] <= 99
            and isinstance(source['year'], str) and re.fullmatch(r'20\d{2}', source['year'])
            and isinstance(source['month'], str) and re.fullmatch(r'0[1-9]|1[0-2]', source['month'])
            and sha(source['preview_sha256']) and sha(source['identity_sha256']))
    value = source_url(source['source_url'])
    published = datetime.fromisoformat(source['published'].replace('Z', '+00:00'))
    require(published.tzinfo is not None and published.strftime('%Y') == source['year']
            and published.strftime('%m') == source['month'])
    expected_path = (f"/en/publications/fm/issues/{source['year']}/{source['month']}/{published.day:02}/"
                     f"fiscal-monitor-{month_name[int(source['month'])].lower()}-{source['year']}")
    require(urlsplit(value).path == expected_path and source['query_params'] ==
            query_params(source['source_title'], source['year'], source['month']))
    require(source['identity_sha256'] == digest({k: v for k, v in source.items()
                                               if k not in {'identity_sha256', 'query_params'}}))


@checked
def prepare_fiscal_chapter(item, preview_html, preview_url):
    require(isinstance(item, dict) and isinstance(preview_html, str))
    url = source_url(item['source_url'])
    require(source_url(preview_url) == url and re.search(r'\b10\.\d{4,9}/[^\s<>"\x27]+',
            html.unescape(preview_html).replace('\\/', '/'), re.I) is None)
    doc = _Document(preview_html)
    require(doc.h1s and {title_key(x) for x in doc.h1s} == {'fiscal monitor'})
    for values in (doc.titles, doc.metadata.get('og:title', []), doc.metadata.get('parsely-title', [])):
        require(values and all(title_key(x) == title_key(item['title']) for x in values))
    for key in ('canonical_url', 'og:url', 'parsely-link'):
        require(doc.metadata.get(key) and all(source_url(x) == url for x in doc.metadata[key]))
    require(set(doc.metadata.get('language', [])) == {'ENG'}
            and set(doc.metadata.get('creator', [])) == {'International Monetary Fund'})
    published = datetime.fromisoformat(item['date'].replace('Z', '+00:00'))
    require(published.tzinfo is not None and set(doc.metadata.get('date', [])) == {published.date().isoformat()})
    descriptions = doc.metadata.get('description', [])
    require(descriptions)
    chapters = []
    for description in descriptions:
        match = re.match(r'^Chapter ([1-9]\d?) Fiscal Monitor\b', description)
        require(match is not None)
        chapters.append(int(match[1]))
    require(len(set(chapters)) == 1)
    source = {'source_guid': item['guid'], 'source_url': url, 'source_title': item['title'],
              'published': item['date'], 'year': published.strftime('%Y'), 'month': published.strftime('%m'),
              'chapter': chapters[0], 'preview_sha256': hashlib.sha256(preview_html.encode()).hexdigest()}
    source['identity_sha256'] = digest(source)
    source['query_params'] = query_params(source['source_title'], source['year'], source['month'])
    validate_source(source)
    return source


def book_fields(source, message):
    require(isinstance(message, dict) and message.get('type') == 'edited-book'
            and message.get('publisher') == 'International Monetary Fund' and message.get('language') == 'en')
    doi = message['DOI']
    match = re.fullmatch(r'10\.5089/(97[89]\d{10})\.089', doi)
    require(match is not None and isbn_valid(match[1]) and message.get('ISBN') == [match[1]])
    titles, subtitles = message['title'], message['subtitle']
    require(isinstance(titles, list) and len(titles) == 1 and isinstance(titles[0], str)
            and isinstance(subtitles, list) and len(subtitles) == 1 and isinstance(subtitles[0], str))
    expected_title = f"Fiscal Monitor, {month_name[int(source['month'])]} {source['year']}: Special Edition"
    require(title_key(titles[0]) == title_key(expected_title)
            and title_key(subtitles[0]) == title_key(f"Chapter {source['chapter']}: {source['source_title']}"))
    require('published' in message)
    for key in ('published', 'published-print', 'published-online'):
        if key in message:
            parts = message[key]['date-parts']
            require(isinstance(parts, list) and len(parts) == 1 and isinstance(parts[0], list)
                    and len(parts[0]) in {2, 3} and all(type(x) is int for x in parts[0])
                    and parts[0][:2] == [int(source['year']), int(source['month'])])
            if len(parts[0]) == 3:
                datetime(*parts[0])
    landing = message['resource']['primary']['URL']
    locator = validate_publication_url(landing)
    require(locator['kind'] == 'book' and locator['isbn'] == match[1])
    return {'doi': doi, 'isbn': match[1], 'title': titles[0], 'subtitle': subtitles[0], 'landing_url': landing}


def search_selection(source, payload):
    validate_source(source)
    require(type(payload) is dict and payload.get('status') == 'ok' and payload.get('message-type') == 'work-list')
    message = payload['message']; items = message['items']; total = message['total-results']
    require(type(total) is int and 1 <= total <= 100 and isinstance(items, list) and len(items) == total
            and type(message['items-per-page']) is int and message['items-per-page'] == 100
            and type(message['query']['start-index']) is int and message['query']['start-index'] == 0)
    matches = []
    for item in items:
        try:
            matches.append(book_fields(source, item))
        except (ValueError, TypeError, KeyError, AttributeError, IndexError):
            pass
    require(len(matches) == 1)
    return matches[0], total


@checked
def select_fiscal_chapter(source, search_payload):
    return search_selection(source, search_payload)[0]['doi']


@checked
def resolve_fiscal_chapter(source, search_payload, exact_payload):
    selected, total = search_selection(source, search_payload)
    require(type(exact_payload) is dict and exact_payload.get('status') == 'ok'
            and exact_payload.get('message-type') == 'work')
    exact = book_fields(source, exact_payload['message'])
    require(exact == selected)
    metadata = {'method': 'official_fiscal_chapter', 'preview_sha256': source['preview_sha256'],
                'search_sha256': digest(search_payload), 'search_total_results': total,
                'exact_crossref_sha256': digest(exact_payload), 'chapter': source['chapter'],
                'year': source['year'], 'month': source['month'],
                'book_title': exact['title'], 'book_subtitle': exact['subtitle']}
    validate_fiscal_chapter_metadata(metadata, source['source_title'], exact['doi'], exact['landing_url'])
    full = exact['title'] + ': ' + exact['subtitle']
    return {'source_guid': source['source_guid'], 'source_url': source['source_url'],
            'source_title': source['source_title'], **exact, 'full_title': full,
            'title_variants': [exact['title'], full], 'series': ['Fiscal Monitor'],
            'year': source['year'], 'issue': None, 'language': 'en', 'original_language': None,
            'pdf_url_candidates': [], 'identity_sha256': source['identity_sha256'],
            'preview_sha256': source['preview_sha256'], 'crossref_sha256': None,
            'metadata': metadata, 'pdf_verified': False}


@checked
def validate_fiscal_chapter_metadata(metadata, source_title, doi, landing_url, pdf_url=None):
    fields = METADATA_FIELDS | ({'publisher_page'} if pdf_url is not None else set())
    require(type(metadata) is dict and set(metadata) == fields and metadata['method'] == 'official_fiscal_chapter')
    require(all(sha(metadata[k]) for k in ('preview_sha256', 'search_sha256', 'exact_crossref_sha256'))
            and type(metadata['search_total_results']) is int and 1 <= metadata['search_total_results'] <= 100
            and type(metadata['chapter']) is int and 1 <= metadata['chapter'] <= 99
            and isinstance(metadata['year'], str) and re.fullmatch(r'20\d{2}', metadata['year'])
            and isinstance(metadata['month'], str) and re.fullmatch(r'0[1-9]|1[0-2]', metadata['month'])
            and isinstance(source_title, str) and 0 < len(source_title) <= 4096
            and len(title_key(source_title).split()) >= 4)
    require(all(isinstance(value, str) and 0 < len(value) <= 4096
                and not re.search(r'[\x00-\x1f\x7f\ud800-\udfff]', value)
                for value in (source_title, metadata['book_title'], metadata['book_subtitle'])))
    require(title_key(metadata['book_title']) == title_key(
                f"Fiscal Monitor, {month_name[int(metadata['month'])]} {metadata['year']}: Special Edition")
            and title_key(metadata['book_subtitle']) == title_key(f"Chapter {metadata['chapter']}: {source_title}"))
    match = re.fullmatch(r'10\.5089/(97[89]\d{10})\.089', doi)
    require(match is not None and isbn_valid(match[1]))
    locator = validate_publication_url(landing_url)
    require(locator['kind'] == 'book' and locator['isbn'] == match[1])
    if pdf_url is not None:
        validate_official_pair(landing_url, pdf_url, doi)
        page = metadata['publisher_page']
        require(type(page) is dict and set(page) == {'pages', 'page_sha256'}
                and type(page['pages']) is int and 1 <= page['pages'] <= 5000 and sha(page['page_sha256']))
    return dict(metadata)


def one_label(lines, label):
    values = [line[len(label) + 1:].strip() for line in lines if line.startswith(label + ':')]
    require(len(values) == 1 and values[0])
    return values[0]


@checked
def resolve_fiscal_landing(publication, page):
    """Verify the observed book's main H1 and independently complete chapter title."""
    metadata = validate_fiscal_chapter_metadata(publication['metadata'], publication['source_title'],
                                               publication['doi'], publication['landing_url'])
    require(publication.get('crossref_sha256') is None and 'crossref_sha256' in publication
            and publication.get('preview_sha256') == metadata['preview_sha256']
            and publication.get('year') == metadata['year'] and publication.get('language') == 'en')
    title, subtitle = metadata['book_title'], metadata['book_subtitle']
    full = title + ': ' + subtitle
    require(publication['title'] == title and publication['subtitle'] == subtitle
            and publication['full_title'] == full
            and publication['isbn'] == publication['doi'].split('/')[1].split('.')[0])
    require(type(page) is dict and type(page['landing_status']) is int and page['landing_status'] == 200
            and page['ready'] is True and page['body_truncated'] is False)
    body = page['visible_body']
    require(isinstance(body, str) and 0 < len(body.encode()) <= 80 * 1024)
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    require(one_label(lines, 'Series') == 'Flagships, Fiscal Monitor'
            and one_label(lines, 'Publisher') == 'International Monetary Fund'
            and one_label(lines, 'Language') == 'English'
            and one_label(lines, 'ISBN') == publication['isbn'])
    require(sum(title_key(line) == title_key(title) for line in lines) == 1
            and sum(title_key(line) == title_key(subtitle) for line in lines) == 1)
    date = re.fullmatch(r'([0-3]?\d) ([A-Z][a-z]{2}) (20\d{2})', one_label(lines, 'Publication Date'))
    require(date is not None and date[2] == month_abbr[int(metadata['month'])] and date[3] == metadata['year'])
    datetime(int(date[3]), int(metadata['month']), int(date[1]))
    pages = one_label(lines, 'Pages')
    require(re.fullmatch(r'[1-9]\d{0,3}', pages) is not None and int(pages) <= 5000)
    doi_url = 'https://doi.org/' + publication['doi']
    require(one_label(lines, 'DOI') == doi_url)
    links, hrefs = page['doi_links'], page['download_hrefs']
    require(isinstance(links, list) and 1 <= len(links) <= 16
            and all(isinstance(link, str) for link in links) and set(links) == {doi_url}
            and isinstance(hrefs, list) and 1 <= len(hrefs) <= 16
            and all(isinstance(link, str) for link in hrefs) and len(set(hrefs)) == 1)
    tags = page['metadata']
    require(type(tags) is dict)
    normalized = {}
    for key, values in tags.items():
        require(isinstance(key, str) and isinstance(values, list))
        normalized.setdefault(key.lower(), []).extend(values)
    require(normalized.get('citation_title') and all(isinstance(value, str) and title_key(value) == title_key(full)
                                                   for value in normalized['citation_title']))
    require(normalized.get('citation_isbn') and all(isinstance(value, str) and re.sub(r'[\s-]', '', value) == publication['isbn']
                                                  for value in normalized['citation_isbn']))
    # The live book uses a main-title H1, unlike journal issue pages. Its complete
    # chapter title was required independently above; every optional DOI/title/
    # ISBN/canonical/PDF tag still passes the ordinary conflict checks below.
    page_publication = {**publication, 'full_title': title, 'title_variants': [title, full]}
    pdf_url = validate_landing_metadata(page_publication, final_url=page['final_url'], metadata=tags,
                                       h1s=page['h1s'], download_hrefs=hrefs)
    require(pdf_url == hrefs[0])
    final_metadata = {**metadata, 'publisher_page': {
        'pages': int(pages), 'page_sha256': digest({key: page[key] for key in (
            'final_url', 'landing_status', 'h1s', 'metadata', 'doi_links',
            'download_hrefs', 'visible_body', 'body_truncated')})}}
    validate_fiscal_chapter_metadata(final_metadata, publication['source_title'], publication['doi'],
                                    page['final_url'], pdf_url)
    return pdf_url, final_metadata
