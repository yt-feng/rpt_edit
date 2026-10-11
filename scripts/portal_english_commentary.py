"""English editorial-only inputs and private, resumable CPU candidates.

Never translate a whole report/Blog page into English. Only explicit KC comment
sections inside the canonical site's own Chinese BlogPosting are admitted.
Generated bodies, sources and checkpoints remain private R2 build inputs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import tempfile
import time
from urllib.parse import urlsplit

from build_portal_extended_locales import (Memo, SEO_QUANTITY_POLICY, extended_source_language, reject_symlinks,
                                          safe_failure_code, validate_budget)
from compare_hymt_translation import require_actions
from offline_translation import MODEL_ID, PROVIDER, OfflineTranslator, TranslationBudgetExceeded
from portal_extended_locales import (ExpansionError, INCREMENTAL_START, MAX_DOCUMENT_BYTES,
                                    ORIGIN, VOID, digest, publication_day, stable_bytes, walk_ld)
from portal_extended_r2 import (HEX64, MAX_SOURCE_BYTES, R2IntegrityError, R2NotFound,
                               R2Store, require_staging_prefix)

POLICY = 'english-secondary-commentary-v1'
SCOPE = 'daily-editorial-comments-v1'
PREFIX = '_english-commentary/v1'
ID = re.compile(r'\d{8}-[a-f0-9]{16}')
MARKERS = {'KC评论：', 'KC评论:', '编辑评论：', '编辑评论:'}
SOURCE_TAGS = {'section', 'span', 'strong', 'b', 'i', 'em', 'u', 'p', 'br',
               'ol', 'ul', 'li', 'h2', 'h3', 'h4'}
TEXT_TAGS = {'p', 'li', 'h2', 'h3', 'h4'}


def require(condition, message='English editorial validation failed'):
    if not condition:
        raise ExpansionError(message)


def exact(value, keys):
    require(isinstance(value, dict) and set(value) == set(keys), 'English payload fields differ')


def text(value, maximum=12000, *, english=False):
    require(isinstance(value, str) and 0 < len(value.strip()) <= maximum, 'Empty/oversized English editorial text')
    require(not re.search(r'[<>\ufffd\ud800-\udfff]|!\[|https?://|(?:data|javascript):|\[\[PORTAL_', value, re.I),
            'Embedded/original asset reference is forbidden')
    require(not re.search(r'original\s+report\s*:|原文[：:]|原始报告[：:]', value, re.I),
            'Original report field is forbidden')
    if english:
        require(not re.search(r'[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]', value), 'Non-English source fallback is forbidden')
    return value


@dataclass
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


class EditorialHTML(HTMLParser):
    """Bounded tree retaining section boundaries, unlike whole-page extraction."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('document')
        self.stack = [self.root]
        self.count = 0

    def handle_starttag(self, tag, attrs):
        self.count += 1
        require(self.count <= 50000 and len(self.stack) <= 128, 'English source HTML exceeds structural bound')
        require(len({key for key, _ in attrs}) == len(attrs), 'Duplicate HTML attributes')
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        require(len(self.stack) > 1 and self.stack[-1].tag == tag, 'Malformed English source HTML')
        self.stack.pop()

    def handle_data(self, value):
        self.stack[-1].children.append(value)

    def close(self):
        super().close()
        require(len(self.stack) == 1, 'Unclosed English source HTML')


def nodes(node):
    yield node
    for child in node.children:
        if isinstance(child, Node):
            yield from nodes(child)


def plain(node):
    return re.sub(r'\s+', ' ', ''.join(child if isinstance(child, str) else
                   (' ' if child.tag == 'br' else plain(child)) for child in node.children)).strip()


def classes(node):
    return set((node.attrs.get('class') or '').split())


def visible(node):
    return ('hidden' not in node.attrs and node.attrs.get('aria-hidden') != 'true'
            and not re.search(r'display\s*:\s*none|visibility\s*:\s*hidden', node.attrs.get('style') or '', re.I))


def extract_editorial(url, body, day):
    """None means no explicit KC commentary, never permission to take the body."""
    require(publication_day(day) == day and day >= INCREMENTAL_START, 'Invalid English source day')
    identifier = urlsplit(url).path.removeprefix('/blog/').removesuffix('.html')
    require(url == f'{ORIGIN}/blog/{identifier}.html' and ID.fullmatch(identifier)
            and identifier[:8] == day.replace('-', ''), 'English accepts only same-day canonical Blog IDs')
    require(isinstance(body, bytes) and 0 < len(body) <= MAX_DOCUMENT_BYTES, 'Empty/oversized English source')
    reader = EditorialHTML(); reader.feed(body.decode('utf-8', errors='strict')); reader.close()
    all_nodes = list(nodes(reader.root))
    canonical = [n.attrs.get('href') for n in all_nodes if n.tag == 'link' and n.attrs.get('rel') == 'canonical']
    require(canonical == [url], 'English source canonical differs')
    require(not any(n.tag == 'meta' and n.attrs.get('name', '').lower() == 'robots'
                    and 'noindex' in n.attrs.get('content', '').lower() for n in all_nodes), 'English source is noindex')
    owned = []
    for node in all_nodes:
        if node.tag == 'script' and node.attrs.get('type') == 'application/ld+json':
            try:
                value = json.loads(plain(node))
            except (ValueError, TypeError):
                raise ExpansionError('Invalid English source provenance JSON') from None
            owned.extend(n for n in walk_ld(value) if n.get('@type') == 'BlogPosting' and n.get('url') == url)
    require(len(owned) == 1, 'English source must own one BlogPosting')
    own = owned[0]
    require(own.get('inLanguage') == 'zh-Hans' and isinstance(own.get('author'), dict)
            and own['author'].get('name') == 'KC桌面'
            and publication_day(own.get('datePublished', '')) == day, 'English source author/language/date differs')
    articles = [n for n in all_nodes if n.tag == 'article' and 'blog-article' in classes(n)]
    require(len(articles) == 1 and visible(articles[0]), 'English source article shell differs')
    contents = [n for n in nodes(articles[0]) if n.tag == 'div' and 'blog-article-content' in classes(n)]
    headers = [n for n in nodes(articles[0]) if n.tag == 'header' and 'blog-article-header' in classes(n)]
    require(len(contents) == len(headers) == 1 and visible(contents[0]), 'English source content boundary differs')
    headings = [n for n in nodes(headers[0]) if n.tag == 'h1' and visible(n)]
    require(len(headings) == 1, 'English editorial title is missing')
    title = re.sub(r'\s*\|\s*KC桌面\s*$', '', plain(headings[0]))
    text(title, 500)
    require(re.search(r'[\u3400-\u9fff]', title), 'An original English report title is not an editorial title')
    blocks = []

    def collect(container, ancestors_visible=True):
        for child in container.children:
            if not isinstance(child, Node):
                continue
            shown = ancestors_visible and visible(child)
            meaningful = [part for part in child.children if not isinstance(part, str) or part.strip()]
            marker = meaningful[0] if meaningful else None
            marked = (child.tag == 'section' and isinstance(marker, Node)
                      and marker.tag == 'strong' and plain(marker) in MARKERS)
            if marked:
                require(shown, 'Hidden English commentary is forbidden')
                require(all(n.tag in SOURCE_TAGS and visible(n) for n in nodes(child)),
                        'Quotes/charts/embeds or hidden content inside a KC comment are forbidden')
                # The label authorizes only this section, not surrounding source
                # paragraphs, neighbouring headings, chart captions or digest.
                prose = Node('section', children=meaningful[1:])
                paragraphs = [n for n in nodes(prose) if n.tag in TEXT_TAGS]
                if paragraphs:
                    require(not any(isinstance(part, str) and part.strip() for part in prose.children),
                            'Mixed commentary paragraph structure')
                    require(not any(n.tag in TEXT_TAGS and any(c.tag in TEXT_TAGS for c in nodes(n) if c is not n)
                                    for n in paragraphs), 'Nested commentary blocks')
                    blocks.extend({'tag': n.tag, 'text': text(plain(n))} for n in paragraphs)
                else:
                    blocks.append({'tag': 'p', 'text': text(plain(prose))})
            else:
                collect(child, shown)

    collect(contents[0])
    if not blocks:
        return None
    require(len(blocks) <= 500, 'Too many editorial blocks')
    result = {'id': identifier, 'source_url': url, 'source_html_sha256': digest(body),
              'datePublished': day, 'title': title, 'blocks': blocks}
    result['editorial_sha256'] = digest(stable_bytes(result))
    validate_editorial(result, day)
    return result


def validate_editorial(doc, day):
    exact(doc, ['id', 'source_url', 'source_html_sha256', 'datePublished', 'title', 'blocks', 'editorial_sha256'])
    require(isinstance(doc['id'], str) and ID.fullmatch(doc['id']) and doc['id'][:8] == day.replace('-', '')
            and doc['source_url'] == f'{ORIGIN}/blog/{doc["id"]}.html' and doc['datePublished'] == day,
            'Editorial source identity differs')
    require(isinstance(doc['source_html_sha256'], str) and HEX64.fullmatch(doc['source_html_sha256']))
    text(doc['title'], 500)
    require(isinstance(doc['blocks'], list) and 1 <= len(doc['blocks']) <= 500)
    for block in doc['blocks']:
        exact(block, ['tag', 'text']); require(block['tag'] in TEXT_TAGS); text(block['text'])
    require(doc['editorial_sha256'] == digest(stable_bytes({k: v for k, v in doc.items() if k != 'editorial_sha256'})),
            'Editorial checksum differs')


def make_source(docs, day):
    source = {'schema_version': 1, 'policy': POLICY, 'locale': 'en', 'scope': SCOPE,
              'origin': ORIGIN, 'day': day, 'documents': sorted(docs, key=lambda doc: doc['id'])}
    source['generation'] = digest(stable_bytes(source))
    validate_source(source)
    return source


def validate_source(source):
    exact(source, ['schema_version', 'policy', 'locale', 'scope', 'origin', 'day', 'documents', 'generation'])
    require(source['schema_version'] == 1 and source['policy'] == POLICY and source['locale'] == 'en'
            and source['scope'] == SCOPE and source['origin'] == ORIGIN, 'English corpus policy differs')
    require(publication_day(source['day']) == source['day'] and source['day'] >= INCREMENTAL_START)
    require(isinstance(source['documents'], list) and 1 <= len(source['documents']) <= 500)
    for doc in source['documents']:
        validate_editorial(doc, source['day'])
    require(len({doc['id'] for doc in source['documents']}) == len(source['documents']), 'Duplicate editorial ID')
    require(source['generation'] == digest(stable_bytes({k: v for k, v in source.items() if k != 'generation'})),
            'English source generation differs')
    require(len(stable_bytes(source)) <= MAX_SOURCE_BYTES)
    return source['documents']


def put_source(store, source):
    validate_source(source)
    raw = stable_bytes(source)
    key = store.key('sources', source['generation'], 'editorial.json')
    try:
        previous = store._get(key, maximum=MAX_SOURCE_BYTES)
    except R2NotFound:
        previous = None
    require(previous is None or previous == raw, 'Immutable English source differs')
    if previous is None:
        store._put(key, raw, metadata={'kind': 'english-editorial-source', 'generation': source['generation']})
    if store._get(key, maximum=MAX_SOURCE_BYTES) != raw:
        raise R2IntegrityError('English source readback differs')
    return {'generation': source['generation'], 'pages': len(source['documents']), 'sha256': digest(raw)}


def read_source(store, generation):
    require(isinstance(generation, str) and HEX64.fullmatch(generation))
    value = json.loads(store._get(store.key('sources', generation, 'editorial.json'), maximum=MAX_SOURCE_BYTES))
    validate_source(value)
    require(value['generation'] == generation, 'English restored generation differs')
    return value


def freeze_editorial(store, docs, day, producer, source_admission):
    """Same-fetch editorial snapshot, bound to the reviewed source-day capture.

    Does not approve/publish, mark completion or initiate inference. The private
    queue retains admitted new days; no subsequent crawler can backfill history.
    """
    from portal_extended_daily_queue import checked_producer
    checked_producer(producer)
    require(isinstance(source_admission, str) and HEX64.fullmatch(source_admission), 'English source admission required')
    if not docs:
        return {'admitted': False, 'pages': 0, 'day': day}
    source = make_source(docs, day)
    key = store.key('admitted-source-days', 'queue.json')
    try:
        queue = json.loads(store._get(key, maximum=65536))
    except R2NotFound:
        queue = {'schema_version': 1, 'policy': POLICY, 'entries': []}
    exact(queue, ['schema_version', 'policy', 'entries'])
    require(queue['schema_version'] == 1 and queue['policy'] == POLICY and isinstance(queue['entries'], list),
            'English source queue differs')
    require(len(queue['entries']) <= 32, 'English source queue exceeds bound')
    seen = set()
    for entry in queue['entries']:
        exact(entry, ['day', 'receipt'])
        require(publication_day(entry['day']) == entry['day'] and entry['day'] not in seen
                and isinstance(entry['receipt'], str) and HEX64.fullmatch(entry['receipt']), 'English queue entry differs')
        seen.add(entry['day'])
    from portal_english_pipeline import completed_day_is_durable
    retained = [entry for entry in queue['entries'] if entry['day'] != day
                and not completed_day_is_durable(store, entry)]
    require(len(retained) < 32, 'Unfinished English admission days exceed bound; nothing discarded')
    saved = put_source(store, source)
    receipt = {'schema_version': 1, 'policy': POLICY, 'scope': SCOPE, 'day': day,
               'generation': source['generation'], 'pages': len(docs), 'source_admission': source_admission,
               'producer': producer}
    raw = stable_bytes(receipt); identity = digest(raw)
    receipt_key = store.key('source-admissions', identity, 'receipt.json')
    try:
        previous = store._get(receipt_key, maximum=65536)
    except R2NotFound:
        previous = None
    require(previous is None or previous == raw, 'Immutable English admission receipt differs')
    if previous is None:
        store._put(receipt_key, raw, metadata={'kind': 'english-source-admission'})
    require(store._get(receipt_key, maximum=65536) == raw, 'English admission readback differs')
    queue_raw = stable_bytes({**queue, 'entries': sorted(retained + [{'day': day, 'receipt': identity}],
                                                       key=lambda row: row['day'], reverse=True)})
    store._put(key, queue_raw, metadata={'kind': 'english-source-day-queue'})
    require(store._get(key, maximum=65536) == queue_raw, 'English queue readback differs')
    return {'admitted': True, 'day': day, 'receipt': identity, **saved}


def preview_text(blocks):
    # One complete sentence from our own translated comment, not a report digest
    # and not an invented model summary. No clipped financial claims.
    first = blocks[0]['text']
    sentence = re.split(r'(?<=[.!?])\s+', first, maxsplit=1)[0]
    return text(sentence, 640, english=True)


PUBLIC_FAILURE_CODES = frozenset({
    'time-budget', 'offline-request-timeout', 'offline-runtime', 'offline-context-limit',
    'offline-response-invalid', 'offline-model-incomplete', 'offline-transport',
    'offline-quantity-validation', 'offline-placeholder-validation', 'offline-markdown-validation',
    'offline-target-script-validation', 'offline-empty-validation', 'offline-token-limit',
    'offline-unicode-validation', 'offline-validation', 'financial-quantity-validation',
    'table-structure-validation', 'untranslated-source-validation', 'chinese-residue-validation',
    'target-script-validation', 'placeholder-validation', 'empty-translation-validation',
    'translation-size-validation', 'expansion-validation', 'translation-error',
    'english-language-validation', 'english-asset-validation', 'english-size-validation',
})


def english_failure_code(error):
    if isinstance(error, ExpansionError):
        code = {
            'Non-English source fallback is forbidden': 'english-language-validation',
            'Embedded/original asset reference is forbidden': 'english-asset-validation',
            'Original report field is forbidden': 'english-asset-validation',
            'Empty/oversized English editorial text': 'english-size-validation',
        }.get(str(error))
        if code:
            return code
    return safe_failure_code(error)


def failure_code_counts(failures):
    """Expose enumerated diagnostics, never exception text or document content."""
    require(isinstance(failures, list) and len(failures) <= 24, 'Invalid English failure inventory')
    counts = Counter(); seen = set()
    for row in failures:
        exact(row, ['id', 'code'])
        identifier, code = row['id'], row['code']
        require(isinstance(identifier, str) and ID.fullmatch(identifier) and identifier not in seen,
                'Invalid English failure identity')
        seen.add(identifier)
        require(isinstance(code, str) and (code in PUBLIC_FAILURE_CODES or re.fullmatch(
            r'offline-http-[1-5][0-9]{2}(?:-(?:context-limit|invalid-utf8|chat-parser|memory|decode|slot-unavailable))?', code)),
            'Unrecognized English failure code')
        counts[code] += 1
    return dict(sorted(counts.items()))


def build(source, output, checkpoint, translator, *, seconds=14400, seed_checkpoint=None,
          quantity_diagnostics=None):
    docs = validate_source(source)
    require(1 <= len(docs) <= 24, 'English CPU batch must be 1..24 new editorial pages')
    validate_budget(seconds); reject_symlinks(output); reject_symlinks(checkpoint)
    require(not output.exists() or not any(output.iterdir()), 'English candidate output must be empty')
    output.mkdir(parents=True, exist_ok=True)
    memo = Memo(checkpoint, 'en', translator, time.monotonic() + seconds,
                source_generation=source['generation'], allow_source_fallback=False, seed_checkpoint=seed_checkpoint,
                quantity_policy='advisory')
    deadline = getattr(translator, 'set_deadline', None)
    if callable(deadline): deadline(memo.deadline)
    memo.save()
    items, failures, timeout = [], [], False
    for doc in docs:
        try:
            # Enforce the editorial-only contract before saving or reusing a
            # memo row. The general locale validator permits some legal-name
            # source residue which cannot appear in English commentary.
            title = memo.get(doc['title'], extended_source_language(doc['title']),
                             validate_result=lambda value: text(value, 500, english=True))
            blocks = [{'tag': row['tag'], 'text': memo.get(row['text'], extended_source_language(row['text']),
                      validate_result=lambda value: text(value, english=True))} for row in doc['blocks']]
            body = {'schema_version': 1, 'policy': POLICY, 'locale': 'en', 'content_kind': 'secondary-commentary',
                    'id': doc['id'], 'title': title, 'preview': preview_text(blocks),
                    'datePublished': doc['datePublished'], 'editorial_sha256': doc['editorial_sha256'], 'blocks': blocks}
            raw = stable_bytes(body); require(len(raw) <= 512 * 1024, 'English body exceeds gateway bound')
            body_hash = digest(raw)
            body_dir = output/'private'/'bodies'; body_dir.mkdir(parents=True, exist_ok=True)
            (body_dir/f'{body_hash}.json').write_bytes(raw)
            items.append({k: body[k] for k in ('id', 'title', 'preview', 'datePublished', 'editorial_sha256')}
                         | {'body_sha256': body_hash})
        except TranslationBudgetExceeded:
            timeout = True; break
        except Exception as error:
            failures.append({'id': doc['id'], 'code': english_failure_code(error)})
    memo.save()
    # Public candidate files contain only projected previews, never private body
    # JSON. Even complete candidates remain noindex until normal approval.
    public_files = {}
    if items:
        from portal_english_ui import detail, homepage
        public_files = {f'public/en/blog/{item["id"]}.html': detail(item) for item in items}
        public_files['public/en/index.html'] = homepage(items)
        for relative, raw in public_files.items():
            path = output/relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
    # The manifest is the immutable candidate identity. Include rendered preview
    # bytes so asset/template changes cannot collide with a previous candidate
    # that has identical translations and inference counters.
    public_files_sha256 = digest(stable_bytes({relative: {'sha256': digest(raw), 'bytes': len(raw)}
                                               for relative, raw in public_files.items()}))
    result = {'schema_version': 2, 'public_files_sha256': public_files_sha256,
              'policy': POLICY, 'locale': 'en', 'scope': SCOPE, 'day': source['day'],
              'provider': PROVIDER, 'model': MODEL_ID, 'paid_provider_requests': 0,
              'generation': source['generation'], 'source_document_count': len(docs),
              'completed_page_count': len(items), 'items': items, 'failures': failures,
              'budget_exhausted': timeout, 'translation_calls': memo.calls, 'cache_hits': memo.hits,
              'indexable': False, 'status': 'complete-candidate' if len(items) == len(docs) and not failures and not timeout
              else 'incomplete-candidate'}
    # This manifest is private review evidence, NOT a public search/SEO asset.
    (output/'candidate-manifest.json').write_bytes(stable_bytes(result))
    if quantity_diagnostics is not None:
        # Do not extend the exact immutable manifest schema for an advisory.
        # Counts also include revalidated memo hits; no source facts leave here.
        quantity_diagnostics.update(quantity_validation_policy=SEO_QUANTITY_POLICY,
            quantity_warning_unit_count=len(memo.quantity_warning_keys),
            quantity_warning_occurrences=memo.quantity_warning_occurrences)
    return result


def staging_probe(store):
    require_staging_prefix(store.prefix)
    day = '2026-09-25'; identifier = '20260925-' + 'a'*16
    doc = {'id': identifier, 'source_url': f'{ORIGIN}/blog/{identifier}.html',
           'source_html_sha256': 'b'*64, 'datePublished': day, 'title': '合成测试评论',
           'blocks': [{'tag': 'p', 'text': '这是隔离的合成评论，仅用于存储测试。'}]}
    doc['editorial_sha256'] = digest(stable_bytes(doc))
    source = make_source([doc], day)
    saved = put_source(store, source)
    require(read_source(store, source['generation']) == source, 'English staging source restore differs')
    with tempfile.TemporaryDirectory() as temporary:
        checkpoint, restored = Path(temporary)/'checkpoint.json', Path(temporary)/'restored.json'
        # Empty English memo only: no synthetic/production translation output.
        memo = Memo(checkpoint, 'en', None, time.monotonic()+5, source_generation=source['generation'])
        memo.save()
        written = store.put_checkpoint('en', source['generation'], checkpoint)
        recovered = store.restore_checkpoint('en', source['generation'], restored)
        require(recovered['present'] and written['sha256'] == recovered['sha256']
                and restored.read_bytes() == checkpoint.read_bytes(), 'English staging checkpoint restore differs')
    return {'staging_only': True, 'english_editorial_restore': 'passed', **saved,
            'english_checkpoint_restore': 'passed', 'checkpoint_sha256': written['sha256'],
            'ready_candidates': 0, 'translation_calls': 0, 'paid_provider_requests': 0, 'deployed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path); parser.add_argument('--output', type=Path)
    parser.add_argument('--checkpoint', type=Path); parser.add_argument('--seed-checkpoint', type=Path)
    parser.add_argument('--seconds', type=int, default=14400)
    parser.add_argument('--staging-prefix')
    args = parser.parse_args()
    require_actions(); require(os.environ.get('KC_PUBLIC_REPOSITORY') == 'true', 'English production translation requires public Actions')
    if args.staging_prefix:
        print(json.dumps(staging_probe(R2Store.from_env(args.staging_prefix)), sort_keys=True)); return 0
    require(os.environ.get('GITHUB_REF') == 'refs/heads/main', 'English production inference requires reviewed main')
    require(all((args.corpus, args.output, args.checkpoint)), 'English corpus/output/checkpoint required')
    require(args.corpus.stat().st_size <= MAX_SOURCE_BYTES, 'English corpus too large')
    translator = OfflineTranslator(validation_attempts=3, quantity_policy='advisory')
    quantity_diagnostics = {}
    result = build(json.loads(args.corpus.read_text()), args.output, args.checkpoint,
                   translator, seconds=args.seconds, seed_checkpoint=args.seed_checkpoint,
                   quantity_diagnostics=quantity_diagnostics)
    summary = {k: result[k] for k in ('status', 'source_document_count', 'completed_page_count',
                                    'budget_exhausted', 'translation_calls', 'cache_hits', 'paid_provider_requests')}
    summary['failure_code_counts'] = failure_code_counts(result['failures'])
    summary.update(quantity_diagnostics)
    summary['terminal_translation_diagnostics'] = getattr(translator, 'failure_diagnostics', [])
    summary['terminal_validation_failure_count'] = getattr(translator, 'validation_failure_count', 0)
    summary['maximum_reported_translation_diagnostics'] = 20
    print(json.dumps(summary))
    return 0 if result['status'] == 'complete-candidate' else 75 if result['budget_exhausted'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
