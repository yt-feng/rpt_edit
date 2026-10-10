"""Version-bound English previews and private commentary, with zero inference.

Only an exact protected release approval may create a NEW version binding.
An ordinary refresh may carry forward the verified active ledger unchanged.
The public tree never receives original material or private commentary bodies.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

from build_portal_extended_locales import reject_symlinks
from portal_english_commentary import PREFIX, POLICY, extract_editorial, exact, require, text
from portal_english_pipeline import (MAX_BODY, MAX_MANIFEST, content_key, hash_value,
                                     put_verified, read_json, restore_candidate, verify_body)
from portal_english_ui import PUBLIC_ASSET_NAMES, detail, homepage, preview_item, ui_assets
from portal_extended_locales import ORIGIN, digest, stable_bytes
from portal_extended_r2 import DEFAULT_PREFIX, R2NotFound, R2Store, safe_relative

ASSEMBLY = 'data/english-commentary/assembly.json'
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
RELEASE = re.compile(r'[0-9a-f]{32}')


def checked_batches(rows):
    require(isinstance(rows, list) and 1 <= len(rows) <= 500, 'English batch ledger exceeds bound')
    result = []
    for row in rows:
        exact(row, ['generation', 'candidate_id'])
        hash_value(row['generation']); hash_value(row['candidate_id'])
        require(row not in result, 'Duplicate English approved batch')
        result.append(dict(row))
    return result


def checked_ledger(value):
    exact(value, ['schema_version', 'policy', 'locale', 'status', 'release_id', 'items'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY and value['locale'] == 'en'
            and value['status'] == 'approved', 'English ledger policy differs')
    hash_value(value['release_id'])
    require(isinstance(value['items'], list) and 1 <= len(value['items']) <= 5000, 'English ledger page bound differs')
    seen = set()
    for item in value['items']:
        exact(item, ['id', 'title', 'preview', 'datePublished', 'editorial_sha256', 'body_sha256'])
        preview_item(item); hash_value(item['editorial_sha256']); hash_value(item['body_sha256'])
        require(item['id'] not in seen, 'Duplicate English ledger ID'); seen.add(item['id'])
    require(value['release_id'] == digest(stable_bytes(value['items'])), 'English ledger content identity differs')
    return value


def read_ledger(store, identity):
    hash_value(identity)
    raw = store._get(store.key('ledgers', identity+'.json'), maximum=MAX_MANIFEST)
    require(digest(raw) == identity, 'English private ledger checksum differs')
    return checked_ledger(json.loads(raw))


def checked_assembly(value):
    exact(value, ['schema_version', 'policy', 'status', 'batches', 'ledger_sha256', 'page_count', 'public_files'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY and value['status'] == 'assembled')
    checked_batches(value['batches']); hash_value(value['ledger_sha256'])
    require(type(value['page_count']) is int and 1 <= value['page_count'] <= 5000)
    require(isinstance(value['public_files'], dict) and len(value['public_files']) == value['page_count']+2,
            'English public preview inventory differs')
    for relative, row in value['public_files'].items():
        safe_relative(relative); exact(row, ['sha256', 'bytes']); hash_value(row['sha256'])
        require(relative in {'en/index.html', 'sitemap-en.xml'} or
                re.fullmatch(r'en/blog/\d{8}-[0-9a-f]{16}\.html', relative), 'Original/private English static route is forbidden')
        require(type(row['bytes']) is int and 0 < row['bytes'] <= MAX_MANIFEST)
    require({'en/index.html', 'sitemap-en.xml'} <= set(value['public_files']))
    return value


def read_static_assembly(store, identity):
    from resume_portal_locale_candidate import read_pinned_manifest
    from publish_static_slot import slot_prefix
    from verify_prepared_static_slot import read_verified_candidate_body
    manifest = read_pinned_manifest(store.client, store.bucket, identity)
    descriptor = manifest['files'].get(ASSEMBLY)
    if descriptor is None:
        require(not any(relative.startswith('en/') for relative in manifest['files']),
                'Untracked English pages exist in the pinned release')
        return None
    raw = read_verified_candidate_body(store.client, store.bucket, slot_prefix(identity['slot'])+ASSEMBLY,
                                       descriptor, maximum=MAX_MANIFEST)
    value = checked_assembly(json.loads(raw))
    expected = set(value['public_files'])-{'sitemap-en.xml'}
    require({relative for relative in manifest['files'] if relative.startswith('en/')} == expected,
            'Pinned release has extra/missing English pages')
    for relative, row in value['public_files'].items():
        descriptor = manifest['files'].get(relative)
        require(descriptor is not None and descriptor['sha256'] == row['sha256'] and descriptor['size'] == row['bytes'],
                'English preview differs from the pinned static descriptor')
        read_verified_candidate_body(store.client, store.bucket, slot_prefix(identity['slot'])+relative,
                                     descriptor, maximum=MAX_MANIFEST)
    return value


def read_active(store, identity):
    if identity is None: return None
    value = read_static_assembly(store, identity)
    if value is None: return None
    release = identity['release_id']; require(RELEASE.fullmatch(release))
    binding = read_json(store, store.key('releases', release, 'manifest.json'))
    exact(binding, ['schema_version', 'policy', 'status', 'site_release', 'ledger_sha256'])
    require(binding == {'schema_version': 1, 'policy': POLICY, 'status': 'approved',
                        'site_release': release, 'ledger_sha256': value['ledger_sha256']},
            'Active English private/public version binding differs')
    ledger = read_ledger(store, value['ledger_sha256'])
    require(len(ledger['items']) == value['page_count'])
    require({'en/index.html', 'sitemap-en.xml', *(f'en/blog/{item["id"]}.html' for item in ledger['items'])}
            == set(value['public_files']), 'Active English ledger/preview routes differ')
    return value


def put_immutable_bytes(store, key, raw, kind, maximum):
    require(0 < len(raw) <= maximum)
    try:
        previous = store._get(key, maximum=maximum)
    except R2NotFound:
        previous = None
    require(previous is None or previous == raw, 'Immutable English publication object differs')
    if previous is None: store._put(key, raw, metadata={'kind': kind})
    require(store._get(key, maximum=maximum) == raw, 'English publication readback differs')


def verify_prepared_ledger(store, source_store, identity, workspace):
    """Prove uploaded previews/private ledger reproduce only admitted KC units."""
    from publish_static_slot import slot_prefix
    from resume_portal_locale_candidate import read_pinned_manifest
    from verify_prepared_static_slot import read_verified_candidate_body
    assembly = read_static_assembly(store, identity); require(assembly is not None)
    ledger = read_ledger(store, assembly['ledger_sha256'])
    items = {}
    for index, row in enumerate(assembly['batches']):
        directory = workspace/str(index)
        _, candidate, source = restore_candidate(store, source_store, row['generation'], row['candidate_id'], directory)
        docs = {doc['id']: doc for doc in source['documents']}
        for item in candidate['items']:
            raw = (directory/'private'/'bodies'/f'{item["body_sha256"]}.json').read_bytes()
            verify_body(raw, item, docs[item['id']])
            require(store._get(store.key('bodies', item['body_sha256']+'.json'), maximum=MAX_BODY) == raw,
                    'Prepared private commentary differs from its admitted candidate')
            items[item['id']] = item
    ordered = sorted(items.values(), key=lambda item: item['id'], reverse=True)
    require(ordered == ledger['items'] and len(ordered) == assembly['page_count'],
            'Prepared ledger does not reproduce the exact admitted candidates')
    pinned = read_pinned_manifest(store.client, store.bucket, identity)
    # prepare_release materializes deployment-specific assets; this reviewer
    # runs in a clean checkout. Reproduce URLs from the exact uploaded tree,
    # never from this runner's source-file hashes.
    asset_hashes = {}
    for name in PUBLIC_ASSET_NAMES:
        descriptor = pinned['files'].get('assets/'+name)
        require(isinstance(descriptor, dict), 'Prepared English public asset is missing')
        hash_value(descriptor['sha256'])
        asset_hashes[name] = descriptor['sha256']
    expected = {'en/index.html': homepage(ordered, approved=True, asset_hashes=asset_hashes)}
    expected.update({f'en/blog/{item["id"]}.html': detail(item, approved=True, asset_hashes=asset_hashes)
                     for item in ordered})
    for relative, raw in expected.items():
        actual = read_verified_candidate_body(store.client, store.bucket, slot_prefix(identity['slot'])+relative,
                                             pinned['files'][relative], maximum=MAX_MANIFEST)
        require(actual == raw, 'Prepared English public HTML is not a preview-only projection')
    return assembly


def compose(root, store, source_store, active, batches, workspace):
    """Re-render previews only; never copy candidate HTML into the release."""
    if not batches: return {'ready': False, 'page_count': 0, 'translation_calls': 0}
    batches = checked_batches(batches)
    require((root/'index.html').is_file() and (root/'sitemap.xml').is_file() and (root/'robots.txt').is_file(),
            'English assembly needs a complete fresh inactive tree')
    require(not (root/'en').exists() and not (root/ASSEMBLY).exists(), 'English assembly must not overwrite an existing namespace')
    old_batches = checked_batches(active['batches']) if active else []
    require(batches[:len(old_batches)] == old_batches, 'Previously approved English batches must be retained')
    previous = read_ledger(store, active['ledger_sha256']) if active else None
    items, bodies = {}, {}
    for index, row in enumerate(batches):
        directory = workspace/f'candidate-{index}'
        _, manifest, source = restore_candidate(store, source_store, row['generation'], row['candidate_id'], directory)
        docs = {doc['id']: doc for doc in source['documents']}
        for item in manifest['items']:
            doc = docs[item['id']]
            # New approval is against the CURRENT inactive Chinese editorial
            # section. Previously approved dated commentary is not re-inferred.
            if row not in old_batches:
                path = root/'blog'/f'{doc["id"]}.html'; reject_symlinks(path)
                require(path.is_file() and path.stat().st_size <= 2*1024*1024, 'New English commentary source is missing')
                current = extract_editorial(doc['source_url'], path.read_bytes(), source['day'])
                require(current is not None and content_key(current) == content_key(doc),
                        'KC secondary interpretation changed after the English candidate')
            raw = (directory/'private'/'bodies'/f'{item["body_sha256"]}.json').read_bytes()
            verify_body(raw, item, doc)
            items[item['id']] = item; bodies[item['body_sha256']] = raw
    ordered = sorted(items.values(), key=lambda item: item['id'], reverse=True)
    require(1 <= len(ordered) <= 5000, 'English approved page bound differs')
    if previous and batches == old_batches:
        require(previous['items'] == ordered, 'Carry-forward cannot change the approved English ledger')
    assets = ui_assets()
    asset_hashes = {}
    for name in PUBLIC_ASSET_NAMES:
        relative = 'assets/'+name
        if relative in assets:
            raw = assets[relative]
        else:
            path = root/relative; reject_symlinks(path)
            require(path.is_file(), 'English assembly needs the final shared public assets')
            raw = path.read_bytes()
        asset_hashes[name] = digest(raw)
    ledger = checked_ledger({'schema_version': 1, 'policy': POLICY, 'locale': 'en', 'status': 'approved',
                             'release_id': digest(stable_bytes(ordered)), 'items': ordered})
    raw_ledger = stable_bytes(ledger); ledger_hash = digest(raw_ledger)
    planned = {'en/index.html': homepage(ordered, approved=True, asset_hashes=asset_hashes)}
    for item in ordered:
        planned[f'en/blog/{item["id"]}.html'] = detail(item, approved=True, asset_hashes=asset_hashes)
    xml = ET.Element(f'{{{NS}}}urlset')
    for url in [ORIGIN+'/en/', *(f'{ORIGIN}/en/blog/{item["id"]}.html' for item in ordered)]:
        node = ET.SubElement(xml, f'{{{NS}}}url'); ET.SubElement(node, f'{{{NS}}}loc').text = url
    planned['sitemap-en.xml'] = ET.tostring(xml, encoding='utf-8', xml_declaration=True)
    public_files = {relative: {'sha256': digest(raw), 'bytes': len(raw)} for relative, raw in planned.items()}
    assembly = checked_assembly({'schema_version': 1, 'policy': POLICY, 'status': 'assembled',
                                 'batches': batches, 'ledger_sha256': ledger_hash,
                                 'page_count': len(ordered), 'public_files': public_files})
    planned[ASSEMBLY] = stable_bytes(assembly); planned.update(assets)
    sitemap = ET.fromstring((root/'sitemap.xml').read_bytes())
    require(sitemap.tag == f'{{{NS}}}sitemapindex', 'Root sitemap must retain its established index')
    for node in list(sitemap):
        if node.findtext(f'{{{NS}}}loc') == ORIGIN+'/sitemap-en.xml': sitemap.remove(node)
    node = ET.SubElement(sitemap, f'{{{NS}}}sitemap'); ET.SubElement(node, f'{{{NS}}}loc').text = ORIGIN+'/sitemap-en.xml'
    planned['sitemap.xml'] = ET.tostring(sitemap, encoding='utf-8', xml_declaration=True)
    # Commentary is a DIFFERENT product, not a full translation of the source.
    # Do not fabricate reciprocal original-report hreflang equivalence.
    root_html = (root/'index.html').read_text()
    anchor = '<a class="topbar-link" data-english-commentary-link href="/en/">English commentary</a>'
    if 'data-english-commentary-link' not in root_html:
        # The established Chinese homepage uses a div; localized shells also
        # use nav. Identify the exact class token instead of assuming one tag.
        boundaries = []
        for match in re.finditer(r'<(?:nav|div)\b[^>]*>', root_html, re.IGNORECASE):
            # Consume complete attributes so data-class or class-like text in
            # another quoted attribute cannot masquerade as the class itself.
            attributes = re.findall(r'''\s+([^\s=/>]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))''',
                                    match.group(), re.DOTALL)
            classes = [double or single or bare for name, double, single, bare in attributes if name.lower() == 'class']
            if any('topbar-actions' in value.split() for value in classes):
                require(len(classes) == 1, 'Established portal navigation boundary is missing or ambiguous')
                boundaries.append(match.end())
        require(len(boundaries) == 1, 'Established portal navigation boundary is missing or ambiguous')
        boundary = boundaries[0]
        planned['index.html'] = (root_html[:boundary]+anchor+root_html[boundary:]).encode()
    for relative in planned: reject_symlinks(root/safe_relative(relative))
    for checksum, raw in bodies.items():
        put_immutable_bytes(store, store.key('bodies', checksum+'.json'), raw, 'english-private-body', MAX_BODY)
    put_immutable_bytes(store, store.key('ledgers', ledger_hash+'.json'), raw_ledger, 'english-private-ledger', MAX_MANIFEST)
    # The ledger is unselected: there is NO site-release manifest until the
    # normal protected job approves/binds the exact uploaded static version.
    for relative, raw in planned.items():
        path = root/relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
    return {'ready': True, 'page_count': len(ordered), 'ledger_sha256': ledger_hash,
            'batches': batches, 'translation_calls': 0, 'deployed': False}


def bind_release(store, identity, previous, *, approved_ledger=''):
    """Called after protected approval and static verification, before cutover."""
    value = read_static_assembly(store, identity); require(value is not None, 'Prepared English assembly is absent')
    if approved_ledger:
        hash_value(approved_ledger); require(value['ledger_sha256'] == approved_ledger, 'English exact-version approval differs')
    else:
        active = read_active(store, previous)
        require(active is not None and value['ledger_sha256'] == active['ledger_sha256']
                and value['batches'] == active['batches'], 'Unapproved new English content cannot bind a site version')
    ledger = read_ledger(store, value['ledger_sha256']); require(len(ledger['items']) == value['page_count'])
    for item in ledger['items']:
        raw = store._get(store.key('bodies', item['body_sha256']+'.json'), maximum=MAX_BODY)
        require(digest(raw) == item['body_sha256'], 'Private English body checksum differs before version binding')
        body = json.loads(raw)
        exact(body, ['schema_version', 'policy', 'locale', 'content_kind', 'id', 'title', 'preview', 'datePublished', 'editorial_sha256', 'blocks'])
        require(body['schema_version'] == 1 and body['policy'] == POLICY and body['locale'] == 'en'
                and body['content_kind'] == 'secondary-commentary'
                and all(body[key] == item[key] for key in ('id', 'title', 'preview', 'datePublished', 'editorial_sha256')))
        require(isinstance(body['blocks'], list) and 1 <= len(body['blocks']) <= 500)
        for block in body['blocks']:
            exact(block, ['tag', 'text']); require(block['tag'] in {'p', 'li', 'h2', 'h3', 'h4'}); text(block['text'], english=True)
    release = identity['release_id']; require(isinstance(release, str) and RELEASE.fullmatch(release))
    binding = {'schema_version': 1, 'policy': POLICY, 'status': 'approved', 'site_release': release,
               'ledger_sha256': value['ledger_sha256']}
    put_verified(store, store.key('releases', release, 'manifest.json'), binding, 'english-site-version-binding', immutable=True)
    return {'site_release': release, 'ledger_sha256': value['ledger_sha256'], 'page_count': value['page_count'], 'deployed': False}


def recover_prepared(store, source_store, identity, workspace):
    """Recover exact uploaded previews; fresh approval, no public rewrite/inference."""
    from portal_english_handoff import save_handoff
    assembly = read_static_assembly(store, identity)
    if assembly is None: return {'ready': False, 'page_count': 0, 'translation_calls': 0, 'handoff': ''}
    verify_prepared_ledger(store, source_store, identity, workspace/'verify')
    batch = assembly['batches'][-1]
    ready, manifest, _ = restore_candidate(store, source_store, batch['generation'], batch['candidate_id'], workspace/'handoff')
    handoff = save_handoff(store, batch, ready, manifest)
    return {'ready': True, 'page_count': assembly['page_count'], 'ledger_sha256': assembly['ledger_sha256'],
            'handoff': handoff, 'translation_calls': 0, 'deployed': False}


def preflight_api(session):
    response = session.get(ORIGIN+'/api/english/commentary?page=1', timeout=(10, 30), allow_redirects=False)
    require(len(response.content) <= MAX_MANIFEST, 'English API response exceeds bound')
    value = response.json()
    require((response.status_code == 404 and value == {'error': 'commentary_not_published'})
            or (response.status_code == 200 and value.get('policy') == POLICY and isinstance(value.get('items'), list)),
            'Live API does not expose the English access boundary')


def audit_live(store, identity, session):
    response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False)
    require(response.status_code == 200 and len(response.content) <= 65536
            and all(response.json().get(key) == value for key, value in identity.items()), 'Live English site version differs')
    active = read_active(store, identity)
    if active is None:
        response = session.get(ORIGIN+'/en/', timeout=(10, 30), allow_redirects=False)
        require(response.status_code == 404, 'Rollback without English must not keep English public pages')
        response = session.get(ORIGIN+'/api/english/commentary', timeout=(10, 30), allow_redirects=False)
        require(response.status_code == 404 and len(response.content) <= 4096
                and response.json() == {'error': 'commentary_not_published'}, 'Rollback kept an independently selected English API ledger')
        return {'site_release': identity['release_id'], 'page_count': 0, 'english_absent': True, 'status': 'passed'}
    ledger = read_ledger(store, active['ledger_sha256']); items = ledger['items']
    samples = {'en/index.html', f'en/blog/{items[0]["id"]}.html', f'en/blog/{items[-1]["id"]}.html', 'sitemap-en.xml'}
    for relative in sorted(samples):
        url = ORIGIN+'/en/' if relative == 'en/index.html' else ORIGIN+'/'+relative
        response = session.get(url, timeout=(10, 30), allow_redirects=False); expected = active['public_files'][relative]
        require(response.status_code == 200 and len(response.content) == expected['bytes']
                and digest(response.content) == expected['sha256'], 'Live English preview/sitemap bytes differ')
        if relative.startswith('en/'):
            require(response.headers.get('Content-Language') == 'en', 'Live English language header differs')
    response = session.get(ORIGIN+'/api/english/commentary?page=1', timeout=(10, 30), allow_redirects=False)
    require(response.status_code == 200 and len(response.content) <= MAX_MANIFEST, 'Live English public preview API failed')
    value = response.json()
    require(value.get('policy') == POLICY and value.get('total') == len(items)
            and value.get('items') == [preview_item(item) for item in items[:24]], 'Live English API/static preview versions differ')
    response = session.post(ORIGIN+'/api/english/commentary/read', json={'id': items[0]['id']},
                            timeout=(10, 30), allow_redirects=False)
    require(response.status_code == 401 and len(response.content) <= 4096
            and response.json() == {'error': 'login_required'}, 'Anonymous English reader received private commentary')
    require('no-store' in response.headers.get('Cache-Control', '')
            and 'noindex' in response.headers.get('X-Robots-Tag', ''), 'Private English API response headers differ')
    return {'site_release': identity['release_id'], 'ledger_sha256': active['ledger_sha256'],
            'page_count': len(items), 'public_samples': len(samples), 'anonymous_full_read': 'denied', 'status': 'passed'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['assemble', 'recover', 'bind', 'identity', 'approve', 'preflight', 'audit'])
    parser.add_argument('--root', type=Path); parser.add_argument('--active-state', type=Path, required=True)
    parser.add_argument('--candidate-state', type=Path); parser.add_argument('--handoff', default='')
    parser.add_argument('--slot'); parser.add_argument('--release'); parser.add_argument('--tree')
    parser.add_argument('--identity', type=Path)
    parser.add_argument('--approved-ledger', default=''); parser.add_argument('--evidence-out', type=Path)
    parser.add_argument('--github-output', type=Path)
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('KC_PUBLIC_REPOSITORY') == 'true', 'English publication requires reviewed main public Actions')
    store = R2Store.from_env(PREFIX); source_store = R2Store(store.client, store.bucket, DEFAULT_PREFIX)
    previous = json.loads(args.active_state.read_bytes())
    if args.operation == 'assemble':
        from portal_english_handoff import verify_handoff
        active = read_active(store, previous); batches = list(active['batches']) if active else []
        require(args.root is not None)
        with tempfile.TemporaryDirectory(prefix='english-approved-restore-') as temporary:
            if args.handoff:
                handoff, _ = verify_handoff(store, source_store, args.handoff, Path(temporary)/'handoff')
                row = handoff['batch']
                if row not in batches: batches.append(row)
            result = compose(args.root, store, source_store, active, batches, Path(temporary))
            result['handoff'] = args.handoff
    elif args.operation == 'approve':
        from review_portal_english_handoff import approval_is_valid
        require(args.identity is not None)
        identity = json.loads(args.identity.read_bytes())
        expected = {'schema_version': 1, 'policy': POLICY, 'operation': 'migrate',
                    'commit_sha': os.environ['CANDIDATE_COMMIT_SHA'], 'static_tree_sha256': args.tree,
                    'site_release': args.release, 'ledger_sha256': args.approved_ledger,
                    'page_count': int(os.environ['CANDIDATE_ENGLISH_PAGES']), 'handoff': args.handoff}
        approval_is_valid(identity, expected, os.environ)
        result = {'approval_verified': True, 'ledger_sha256': args.approved_ledger, 'deployed': False}
    elif args.operation == 'preflight':
        import requests
        with requests.Session() as session: preflight_api(session)
        result = {'english_api_boundary': 'available', 'deployed': False}
    else:
        if args.candidate_state:
            candidate = json.loads(args.candidate_state.read_bytes())
        else:
            candidate = {'slot': args.slot, 'release_id': args.release, 'tree_sha256': args.tree}
            require(args.slot in {'a', 'b'} and isinstance(args.release, str) and RELEASE.fullmatch(args.release)); hash_value(args.tree)
        if args.operation == 'identity':
            require(args.handoff)
            value = read_static_assembly(store, candidate); require(value is not None)
            commit = os.environ.get('CANDIDATE_COMMIT_SHA') or os.environ['GITHUB_SHA']
            require(re.fullmatch(r'[0-9a-f]{40}', commit))
            result = {'schema_version': 1, 'policy': POLICY, 'operation': 'migrate', 'commit_sha': commit,
                      'static_tree_sha256': candidate['tree_sha256'], 'site_release': candidate['release_id'],
                      'ledger_sha256': value['ledger_sha256'], 'page_count': value['page_count'], 'handoff': args.handoff}
        elif args.operation == 'recover':
            with tempfile.TemporaryDirectory(prefix='english-prepared-recovery-') as temporary:
                result = recover_prepared(store, source_store, candidate, Path(temporary))
        elif args.operation == 'audit':
            import requests
            with requests.Session() as session: result = audit_live(store, candidate, session)
        else:
            require(args.operation == 'bind')
            if args.approved_ledger:
                require(os.environ.get('KC_ENGLISH_APPROVAL_VERIFIED') == 'true', 'English protected approval receipt is required')
            with tempfile.TemporaryDirectory(prefix='english-bind-verify-') as temporary:
                verify_prepared_ledger(store, source_store, candidate, Path(temporary))
            result = bind_release(store, candidate, previous, approved_ledger=args.approved_ledger)
    if args.evidence_out: args.evidence_out.write_bytes(stable_bytes(result))
    if args.github_output:
        with args.github_output.open('a') as stream:
            for key in ('ready', 'page_count', 'ledger_sha256', 'handoff'):
                value = result.get(key, '')
                stream.write(key+'='+str(value).lower()+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__': main()
