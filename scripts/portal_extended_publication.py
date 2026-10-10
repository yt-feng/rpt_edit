"""Compose approved reading pages after the established locale build.

Only previously approved, byte-identical translations may be replayed against
current source HTML. Missing units are errors, never new source fallbacks. The
complete current candidate is stored privately and checked by the unchanged
exact-HTML assembler. No inference or deployment occurs in this module.
"""
from __future__ import annotations

import json
from pathlib import Path
import xml.etree.ElementTree as ET

from assemble_portal_extended_locales import (
    assemble, head_alternates, locale_home_alternates,
    verified_candidate, NS, XHTML,
)
from build_portal_extended_locales import build
from offline_translation import OfflineTranslationError
from portal_extended_incremental import content_key
from portal_extended_locales import (
    ORIGIN, HREFLANG, ExpansionError, PublicParser, daily_corpus_day, digest,
    document_from_html, file_for_url, locale_url, make_corpus, select_locales,
    stable_bytes, validate_corpus,
)
from portal_extended_r2 import HEX64, MAX_CHECKPOINT_BYTES, checkpoint_is_valid, safe_part
from portal_extended_ui import UI_VERSION, standard_detail, standard_homepage, ui_assets
from portal_approved_quantity_contract import CONTRACT_ID, PARSER_SHA256, bindings, quantity_issues as approved_quantity_issues

LEDGER = 'data/extended-locales/assembly.json'


class CacheOnly:
    def translate(self, *args, **kwargs):
        # Not a validation exception: source-fallback must NOT catch this.
        raise OfflineTranslationError('Approved publication unit is absent', code='offline-approval-cache-miss')


def current_document(root: Path, original: dict) -> dict:
    path = root / file_for_url(original['url'])
    if not path.is_file() or path.is_symlink():
        raise ExpansionError('Approved source is missing from the current inactive tree')
    current = document_from_html(original['url'], path.read_bytes(), exclude_related=True)
    allowed_links = {row['url'] for row in original['links']}
    current['links'] = [row for row in current['links'] if row['url'] in allowed_links]
    for key in ('selection_scope', 'selection_day'):
        current[key] = original[key]
    current['content_sha256'] = digest(stable_bytes({k: v for k, v in current.items() if k != 'content_sha256'}))
    if content_key(current) != content_key(original):
        raise ExpansionError('Approved source content changed; a new translated candidate is required')
    return current


def read_active_ledger(store, identity: dict | None) -> dict:
    if identity is None:
        return {'batches': []}
    from resume_portal_locale_candidate import read_pinned_manifest
    from publish_static_slot import slot_prefix
    from verify_prepared_static_slot import read_verified_candidate_body
    manifest = read_pinned_manifest(store.client, store.bucket, identity)
    descriptor = manifest['files'].get(LEDGER)
    if descriptor is None:
        return {'batches': []}
    raw = read_verified_candidate_body(store.client, store.bucket,
        slot_prefix(identity['slot']) + LEDGER, descriptor, maximum=1024 * 1024)
    value = json.loads(raw)
    if value.get('schema_version') != 2 or value.get('status') != 'assembled' or not value.get('batches'):
        raise ExpansionError('Active extended release has no verified carry-forward ledger')
    return value


def read_active_batches(store, identity: dict | None) -> list[dict]:
    return read_active_ledger(store, identity)['batches']


def active_checkpoint_sha(ledger, locale, generation, candidate):
    """Find one seed receipt for the original approval, not its replay output."""
    rows = ledger.get('replays')
    if not isinstance(rows, list) or len(rows) > 20000:
        raise ExpansionError('Active approval checkpoint receipts are absent or unbounded')
    matches = [row for row in rows if isinstance(row, dict)
        and (row.get('locale'), row.get('approved_generation'), row.get('approved_candidate'))
        == (locale, generation, candidate)]
    if len(matches) != 1:
        raise ExpansionError('Active approval requires one exact checkpoint receipt')
    checksum = matches[0].get('checkpoint_sha256')
    if not isinstance(checksum, str) or HEX64.fullmatch(checksum) is None:
        raise ExpansionError('Active approved checkpoint checksum is invalid')
    return checksum


def restore_active_checkpoint(store, ledger, locale, generation, candidate, destination):
    """Restore the seed bound by the authenticated active publication ledger.

    This selects no new approval: the ordinary byte-identical baseline proof
    still follows. A mutable latest pointer is never authority for old approval.
    """
    checksum = active_checkpoint_sha(ledger, locale, generation, candidate)
    key = store.checkpoint_object_key(locale, generation, checksum)
    raw = store._get(key, maximum=MAX_CHECKPOINT_BYTES)
    if digest(raw) != checksum:
        raise ExpansionError('Active approved checkpoint checksum differs')
    checkpoint_is_valid(json.loads(raw), locale, generation)
    destination.write_bytes(raw)
    return {'present': True, 'sha256': checksum, 'bytes': len(raw), 'object_key': key,
            'binding': 'authenticated-active-ledger'}


def checked_batches(batches: list[dict]) -> list[dict]:
    if not isinstance(batches, list) or len(batches) > 500:
        raise ExpansionError('Publication batch ledger exceeds its bound')
    result = []
    for row in batches:
        generation = safe_part(row['generation'], label='source generation', pattern=HEX64)
        candidates = row['candidates']
        if not isinstance(candidates, dict) or not candidates:
            raise ExpansionError('Approved batch needs exact candidate identities')
        select_locales(','.join(candidates))
        for value in candidates.values():
            safe_part(value, label='candidate id', pattern=HEX64)
        normalized = {'generation': generation, 'candidates': dict(candidates)}
        if normalized not in result:
            result.append(normalized)
    return result


def prove_approved_baseline(corpus, locale, work, seed, approved_manifest, *, allow_frozen=False, require_match=True):
    """Try today's gate first; only authenticated active bytes may use v1.

    Both attempts are isolated and read-only. A validator is selected only when
    every page reproduces the complete approved file inventory with zero cache
    misses. The returned checkpoint contains only these demonstrated units.
    """
    policies = [('current', None, None)]
    if allow_frozen: policies.append((CONTRACT_ID, approved_quantity_issues, PARSER_SHA256))
    attempts = []
    for index, (contract, validator, parser_sha) in enumerate(policies):
        checkpoint = work/f'baseline-{index}.json'
        replay = build(corpus, locale, work/f'baseline-{index}', checkpoint, CacheOnly(),
                       allow_source_fallback=True, seed_checkpoint=seed, quantity_validator=validator)
        matches = (replay['status'] == 'complete-candidate' and replay['translation_calls_this_run'] == 0
                   and replay['files_sha256'] == approved_manifest['files_sha256'])
        attempts.append({'contract': contract, 'parser_sha256': parser_sha, 'matches': matches,
                         'status': replay['status'], 'cache_miss_attempts': replay['translation_calls_this_run'],
                         'files_sha256': replay['files_sha256']})
        proof = {'manifest': replay, 'checkpoint': checkpoint, 'quantity_validator': validator,
                 'quantity_contract': contract, 'quantity_parser_sha256': parser_sha,
                 'matches': matches, 'attempts': attempts}
        if matches: return proof
    if require_match: raise ExpansionError('Checkpoint does not reproduce the approved candidate bytes')
    return proof


def compose(root: Path, store, batches: list[dict], workspace: Path, *, active_identity: dict | None = None) -> dict:
    batches = checked_batches(batches)
    active_ledger = read_active_ledger(store, active_identity) if active_identity is not None else {'batches': []}
    active = checked_batches(active_ledger['batches'])
    if batches[:len(active)] != active:
        raise ExpansionError('Authenticated active approval batches must be retained exactly')
    active_approvals = bindings(active)
    if not batches:
        return {'ready': False, 'locales': [], 'paid_provider_requests': 0}
    if not (root/'index.html').is_file() or not (root/'robots.txt').is_file() or (root/LEDGER).exists():
        raise ExpansionError('Publication requires a fresh complete inactive tree')
    corpora, owners = [], {}
    for index, row in enumerate(batches):
        path = workspace/f'source-{index}.json'
        store.restore_source(row['generation'], path)
        corpus = json.loads(path.read_text())
        docs = validate_corpus(corpus)
        if not daily_corpus_day(corpus) or len(docs) > 24:
            raise ExpansionError('Publication accepts only bounded daily detail batches')
        corpora.append(corpus)
        for locale in row['candidates']:
            for doc in docs:
                owners[locale, doc['url']] = index
    if len(owners) > 20000:
        raise ExpansionError('Extended publication exceeds its page bound')
    pages, sources, candidate_ids, replays = {}, {}, {}, []
    for index, (row, corpus) in enumerate(zip(batches, corpora, strict=True)):
        for locale, candidate_id in row['candidates'].items():
            docs = [doc for doc in corpus['documents'] if owners[locale, doc['url']] == index]
            if not docs:
                continue
            work = workspace/f'{index}-{locale}'
            work.mkdir()
            original_dir = work/'approved'
            store.restore_candidate(locale, row['generation'], candidate_id, original_dir)
            approved_manifest, _approved_files = verified_candidate(original_dir, corpus)
            frozen = (row['generation'], locale, candidate_id) in active_approvals
            seed = work/'seed.json'
            restored = (restore_active_checkpoint(store, active_ledger, locale, row['generation'], candidate_id, seed)
                        if frozen else store.restore_checkpoint(locale, row['generation'], seed))
            if not restored.get('present'):
                raise ExpansionError('Approved checkpoint is absent')
            # Prove the checkpoint reproduces the actual approved HTML, not
            # merely a new plausible translation with the same model name.
            proof = prove_approved_baseline(corpus, locale, work, seed, approved_manifest, allow_frozen=frozen)
            validator = proof['quantity_validator']
            # Extra or newer latest-cache rows never enter current-source
            # replay; this seed only contains units proven against approval.
            approved_seed = proof['checkpoint']
            current_docs = [current_document(root, doc) for doc in docs]
            current = make_corpus(current_docs)
            directory = work/'current'
            checkpoint = work/'current.json'
            replay = build(current, locale, directory, checkpoint, CacheOnly(),
                allow_source_fallback=True, seed_checkpoint=approved_seed, quantity_validator=validator)
            if replay['status'] != 'complete-candidate' or replay['translation_calls_this_run'] != 0:
                raise ExpansionError('Current-source replay requires unapproved translation units')
            generation = current['documents_sha256']
            store.put_source(current)
            store.put_checkpoint(locale, generation, checkpoint)
            saved = store.upload_candidate(directory, locale, generation)
            if not saved['ready']:
                raise ExpansionError('Replayed candidate has not been persisted completely')
            staging = work/'tree'
            staging.mkdir()
            (staging/'index.html').write_bytes((root/'index.html').read_bytes())
            (staging/'robots.txt').write_bytes((root/'robots.txt').read_bytes())
            for doc in current_docs:
                relative = file_for_url(doc['url'])
                for prefix in ('', 'ko', 'ja', 'ar'):
                    source = root/prefix/relative
                    if source.is_file() and not source.is_symlink():
                        target = staging/prefix/relative
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_bytes(source.read_bytes())
                sources[doc['url']] = doc
            # The existing exact source-HTML SHA and complete-candidate gates
            # operate on the freshly rendered generation without exceptions.
            assemble(staging, current, [directory], (locale,), apply=True,
                     existing_locales=('ko', 'ja', 'ar'), presentation=False)
            for doc in current_docs:
                pages[locale, doc['url']] = (staging/locale/file_for_url(doc['url'])).read_bytes()
            candidate_ids[locale] = candidate_id
            replays.append({'locale': locale, 'approved_generation': row['generation'],
                'approved_candidate': candidate_id, 'source_generation': generation,
                'candidate_id': saved['candidate_id'], 'quantity_contract': proof['quantity_contract'],
                'quantity_parser_sha256': proof['quantity_parser_sha256'], 'checkpoint_sha256': restored['sha256'],
                'checkpoint_binding': restored.get('binding', 'incoming-exact-byte-replay'),
                'pages': len(current_docs), 'translation_calls': 0})
    planned, clusters = {}, {}
    locales = tuple(locale for locale in select_locales('all-supported') if any(k[0] == locale for k in pages))
    home_alternates = locale_home_alternates(
        root, locales, existing_locales=('ko', 'ja', 'ar'), origin=ORIGIN,
    )
    planned['index.html'] = head_alternates((root/'index.html').read_text(), home_alternates).encode()
    for url in sorted(sources):
        relative = file_for_url(url)
        cluster = {'zh-Hans': url, 'x-default': url}
        established = {}
        for locale in ('ko', 'ja', 'ar'):
            path = root/locale/relative
            if not path.is_file() or path.is_symlink():
                continue
            html = path.read_text()
            parsed = PublicParser(); parsed.feed(html); parsed.close()
            canonical = ORIGIN+'/'+locale+url[len(ORIGIN):]
            if parsed.canonical == canonical and parsed.content_lang == locale and 'noindex' not in parsed.metadata.get('robots', ''):
                cluster[locale] = canonical
                established[locale] = html
        for locale in locales:
            if (locale, url) in pages and locale in HREFLANG:
                cluster[HREFLANG[locale]] = locale_url(url, locale)
        clusters[url] = cluster
        original = (root/relative).read_text()
        planned[relative.as_posix()] = head_alternates(original, cluster).encode()
        for locale, html in established.items():
            planned[(Path(locale)/relative).as_posix()] = head_alternates(html, cluster).encode()
        for locale in locales:
            if (locale, url) in pages:
                html = standard_detail(pages[locale, url], locale, url, alternates=cluster).decode()
                planned[(Path(locale)/relative).as_posix()] = (head_alternates(html, cluster) if locale in HREFLANG else html).encode()
    index = ET.Element(f'{{{NS}}}sitemapindex')
    counts = {}
    for locale in locales:
        urls = sorted(url for code, url in pages if code == locale)
        counts[locale] = len(urls)
        planned[f'{locale}/index.html'] = standard_homepage(
            locale, [(url, pages[locale, url]) for url in urls], origin=ORIGIN,
            alternates=home_alternates,
            portal_home=(root/'index.html').read_text(),
        )
        planned[f'{locale}/index.html'] = head_alternates(
            planned[f'{locale}/index.html'].decode(), home_alternates,
        ).encode()
        xml = ET.Element(f'{{{NS}}}urlset')
        for url in urls:
            node = ET.SubElement(xml, f'{{{NS}}}url')
            ET.SubElement(node, f'{{{NS}}}loc').text = locale_url(url, locale)
            if locale in HREFLANG:
                for language, href in clusters[url].items():
                    ET.SubElement(node, f'{{{XHTML}}}link', {'rel':'alternate','hreflang':language,'href':href})
        planned[f'sitemap-extended-{locale}.xml'] = ET.tostring(xml, encoding='utf-8', xml_declaration=True)
        child = ET.SubElement(index, f'{{{NS}}}sitemap')
        ET.SubElement(child, f'{{{NS}}}loc').text = ORIGIN+f'/sitemap-extended-{locale}.xml'
        planned[f'{locale}/llms.txt'] = ('# KC桌面\n\n'+'\n'.join('- '+locale_url(url, locale) for url in urls)+'\n').encode()
    planned['sitemap-extended.xml'] = ET.tostring(index, encoding='utf-8', xml_declaration=True)
    robots = (root/'robots.txt').read_text()
    declaration = 'Sitemap: '+ORIGIN+'/sitemap-extended.xml'
    planned['robots.txt'] = (robots if declaration in robots.splitlines() else robots.rstrip()+'\n'+declaration+'\n').encode()
    sitemap_path = root/'sitemap.xml'
    sitemap = sitemap_path.read_text()
    sitemap_root = ET.fromstring(sitemap)
    if sitemap_root.tag != f'{{{NS}}}sitemapindex':
        raise ExpansionError('Existing root sitemap is not an index')
    # Each child of the root index must be a URL-set sitemap. Keep the
    # standalone extended index advertised in robots, but do not nest it here.
    # Replace this publication's namespace to repair older nested indexes and
    # remove stale/duplicate locale entries when approved batches change.
    for child in list(sitemap_root):
        location = child.find(f'{{{NS}}}loc')
        if location is not None and (
            location.text == ORIGIN+'/sitemap-extended.xml'
            or str(location.text).startswith(ORIGIN+'/sitemap-extended-')
        ):
            sitemap_root.remove(child)
    for locale in locales:
        child = ET.SubElement(sitemap_root, f'{{{NS}}}sitemap')
        ET.SubElement(child, f'{{{NS}}}loc').text = ORIGIN+f'/sitemap-extended-{locale}.xml'
    planned['sitemap.xml'] = ET.tostring(sitemap_root, encoding='utf-8', xml_declaration=True)
    receipt = {'schema_version': 2, 'status': 'assembled', 'locales': list(locales),
        'batches': batches, 'page_counts': counts, 'pages_per_locale': min(counts.values()),
        'source_urls_by_locale': {locale: sorted(url for code, url in pages if code == locale) for locale in locales},
        'replays': replays, 'paid_provider_requests': 0, 'deployment_performed': False,
        'detail_only': True, 'locale_homepages': True, 'ui_version': UI_VERSION}
    planned.update(ui_assets())
    planned[LEDGER] = stable_bytes(receipt)
    if len(planned[LEDGER]) > 1024 * 1024:
        raise ExpansionError('Extended approval ledger exceeds its storage bound')
    # Reject all escaping/symlink writes before touching the inactive release.
    for relative in planned:
        path = root/relative
        if not path.resolve().is_relative_to(root.resolve()) or any(p.is_symlink() for p in [path, *path.parents] if p == root or root in p.parents):
            raise ExpansionError('Unsafe publication output')
    for relative, body in planned.items():
        path = root/relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    return {**receipt, 'ready': True, 'candidate_ids': candidate_ids,
            'source_generation': batches[-1]['generation']}
