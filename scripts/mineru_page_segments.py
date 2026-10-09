"""Exact physical PDF segments with independent durable MinerU identities.

An assembled result is a derived delivery, never an original provider success.
Existing original claims and recovery budgets are read but never changed here.
Each segment has one permanent Ledger source claim: ambiguous or failed tasks
cannot turn into another submission merely by restarting this adapter.
"""
from __future__ import annotations

import copy
import io
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile

from consume_legacy_mineru import safe_unzip
from mineru_result_cache import identity as cache_identity, missing, conflict
from mineru_task_ledger import LedgerError, digest, encoded, exact_json, schema_v1
from mineru_terminal_recovery import task_identity

POLICY = 'physical-page-segments-v1'
PAGE_LIMIT = 200
# The existing figure proof parser accepts at most 1,000 original pages.
MAX_PAGES = 1000
MAX_PDF_BYTES = 200 * 1024 * 1024
HASH = re.compile(r'[a-f0-9]{64}')
PROFILE = ('_backend', '_version_name', '_ocr_enable', '_effort')
ARCHIVE_PREFIX = '_workflow-cache/mineru-page-segments/v1/'


def require(test, category):
    if not test:
        raise LedgerError('Page segments: ' + category)


def page_count(path):
    """Inspect the actual PDF, without a provider call or a new source claim."""
    import fitz
    with fitz.open(path) as document:
        require(not document.is_encrypted and 0 < document.page_count <= MAX_PAGES,
                'unsupported original PDF')
        return document.page_count


def plan_key(binding):
    return 'recoveries/' + digest(encoded([POLICY, binding['id']]))[:32]


def _binding_valid(binding):
    # Reuse exactly the existing source binding contract, without changing it.
    cache_identity(binding, {'batch_id': 'validation', 'batch_key': 'batches/'+'0'*32,
        'parent_batch_key': 'batches/'+'0'*32, 'data_id': binding['id'], 'child_ordinal': 0})


class SegmentArchive:
    """Exact private derived PDFs, separate from all provider-result caches."""
    def __init__(self, client, bucket):
        self.client, self.bucket = client, bucket

    @staticmethod
    def key(original, binding):
        return ARCHIVE_PREFIX+original['id']+'/'+binding['id']+'.pdf'

    @staticmethod
    def metadata(original, binding):
        return {'sha256': binding['sha256'], 'original-id': original['id'], 'binding-id': binding['id']}

    def get(self, original, binding):
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=self.key(original, binding))
        except Exception as error:
            if missing(error): return None
            raise LedgerError('Page segments: archive read failed') from None
        body = response.get('Body')
        try:
            require(body is not None and response.get('ContentLength') == binding['size']
                    and 0 < binding['size'] <= MAX_PDF_BYTES and response.get('ContentType') == 'application/pdf'
                    and response.get('Metadata') == self.metadata(original, binding), 'archive metadata differs')
            raw = body.read(MAX_PDF_BYTES+1)
            require(len(raw) == binding['size'] and digest(raw) == binding['sha256'] and raw.startswith(b'%PDF-'),
                    'archive PDF differs')
            return raw
        finally:
            if callable(getattr(body, 'close', None)): body.close()

    def preserve(self, original, binding, payload):
        require(isinstance(payload, bytes) and len(payload) == binding['size'] <= MAX_PDF_BYTES
                and digest(payload) == binding['sha256'] and payload.startswith(b'%PDF-'), 'archive input differs')
        existing = self.get(original, binding)
        if existing is not None:
            require(existing == payload, 'archive PDF differs')
            return
        try:
            self.client.put_object(Bucket=self.bucket, Key=self.key(original, binding), Body=payload,
                ContentType='application/pdf', Metadata=self.metadata(original, binding),
                CacheControl='private, no-store', IfNoneMatch='*')
        except Exception as error:
            if not conflict(error):
                raise LedgerError('Page segments: archive write unresolved') from None
        require(self.get(original, binding) == payload, 'archive readback differs')


def read_segment_plan(ledger, original_binding):
    """Read a frozen plan without writing, regenerating PDFs or provider calls."""
    _binding_valid(original_binding)
    plan, _ = ledger.store.get(plan_key(original_binding))
    if plan is None:
        return None
    require(isinstance(plan, dict) and set(plan) == {'schema', 'policy', 'original_binding',
            'page_count', 'page_limit', 'segments'} and type(plan['schema']) is int and plan['schema'] == 1
            and plan['policy'] == POLICY and exact_json(plan['original_binding'], original_binding), 'frozen plan identity')
    count = plan['page_count']
    require(type(count) is int and PAGE_LIMIT < count <= MAX_PAGES and type(plan['page_limit']) is int
            and plan['page_limit'] == PAGE_LIMIT and isinstance(plan['segments'], list)
            and len(plan['segments']) == (count+PAGE_LIMIT-1)//PAGE_LIMIT, 'frozen plan coverage')
    for index, segment in enumerate(plan['segments']):
        require(isinstance(segment, dict) and set(segment) == {'page_start', 'page_end', 'binding'}, 'frozen segment fields')
        start, end = index*PAGE_LIMIT+1, min((index+1)*PAGE_LIMIT, count)
        require(type(segment['page_start']) is int and segment['page_start'] == start
                and type(segment['page_end']) is int and segment['page_end'] == end, 'frozen segment span')
        binding = segment['binding']; _binding_valid(binding)
        require(all(exact_json(binding[key], original_binding[key]) for key in ('scope', 'endpoint', 'options'))
                and binding['source'] == f'_mineru-page-segments/v1/{original_binding["id"]}/p{start:04d}-{end:04d}.pdf'
                and binding['id'] != original_binding['id'], 'frozen segment binding')
    return plan


def prepare_segments(ledger, original_pdf, source, directory, *, allow_plan_write=True, archive=None):
    """Freeze a deterministic plan and segment bytes; return None at <=200 pages.

    Physical splitting has no provider side effects. The first plan is immutable;
    changed splitter bytes on a future runtime stop instead of creating new tasks.
    Page spans in all public interfaces are inclusive, one-based.
    """
    import fitz
    original_pdf, directory = Path(original_pdf), Path(directory)
    require(not original_pdf.is_symlink(), 'original symlink')
    original = ledger.bind(original_pdf, source)
    raw = original_pdf.read_bytes()
    with fitz.open(stream=raw, filetype='pdf') as document:
        require(not document.is_encrypted and 0 < document.page_count <= MAX_PAGES,
                'unsupported original PDF')
        if document.page_count <= PAGE_LIMIT:
            return None
        _binding_valid(original)
        existing = read_segment_plan(ledger, original)
        directory.mkdir(parents=True, exist_ok=True)
        require(not directory.is_symlink(), 'segment directory symlink')
        segments = []
        for index, start in enumerate(range(0, document.page_count, PAGE_LIMIT)):
            end = min(start+PAGE_LIMIT, document.page_count)
            name = f'p{start+1:04d}-{end:04d}.pdf'
            target = directory/name
            require(not target.is_symlink(), 'segment symlink')
            prior = existing['segments'][index] if existing is not None else None
            payload = archive.get(original, prior['binding']) if archive is not None and prior is not None else None
            if payload is None:
                with fitz.open() as part:
                    part.insert_pdf(document, from_page=start, to_page=end-1)
                    payload = part.tobytes(garbage=4, deflate=True, no_new_id=True)
            require(len(payload) <= MAX_PDF_BYTES, 'segment PDF exceeds size limit')
            with fitz.open(stream=payload, filetype='pdf') as part:
                require(part.page_count == end-start, 'archived segment page count differs')
            if target.exists():
                require(target.read_bytes() == payload, 'local segment bytes changed')
            else:
                target.write_bytes(payload)
            derived_source = f'_mineru-page-segments/v1/{original["id"]}/{name}'
            segments.append({'page_start': start+1, 'page_end': end,
                'binding': ledger.bind(target, derived_source)})
        plan = {'schema': 1, 'policy': POLICY, 'original_binding': original,
                'page_count': document.page_count, 'page_limit': PAGE_LIMIT, 'segments': segments}
    require(exact_json(ledger.bind(original_pdf, source), original), 'original bytes changed')
    if existing is None:
        require(allow_plan_write, 'missing frozen segment plan')
        ledger.store.put(plan_key(original), plan)
        existing, _ = ledger.store.get(plan_key(original))
    require(exact_json(existing, plan), 'frozen segment plan differs')
    return plan


def _segment_path(directory, segment):
    return Path(directory)/Path(segment['binding']['source']).name


def _claim(ledger, binding, *, required):
    claim, _ = ledger.store.get('sources/'+binding['id'])
    if claim is None:
        require(not required, 'segment claim missing')
        return None
    require(schema_v1(claim) and exact_json(claim.get('binding'), binding), 'segment claim mismatch')
    batch, _ = ledger._read_batch(claim['batch_key'])
    require(exact_json(batch['files'], [binding]) and 'recovery_parent' not in batch,
            'segment task is not its exact singleton')
    require(batch['state'] in {'accepted', 'uploaded', 'terminal', 'auth_rejected'},
            'ambiguous segment submission')
    if required:
        require(batch['state'] != 'auth_rejected' and bool(batch['batch_id']), 'segment task unaccepted')
    return batch


def preflight_segment_claims(ledger, plan, *, required=False):
    require(exact_json(read_segment_plan(ledger, plan['original_binding']), plan), 'frozen plan differs')
    return [_claim(ledger, segment['binding'], required=required) for segment in plan['segments']]


def _rewrite_resource(value, resources, *, middle=False):
    require(isinstance(value, str) and value, 'invalid resource reference')
    path = unquote(value)
    if middle and not path.startswith('images/'):
        path = 'images/'+path
    matches = [target for source, target in resources.items()
               if source == path or source.endswith('/'+path)]
    require(len(matches) == 1, 'resource reference missing or ambiguous')
    target = matches[0]
    return target.removeprefix('images/') if middle else target


def _rewrite_json(value, resources, offset, pages):
    if isinstance(value, list):
        return [_rewrite_json(item, resources, offset, pages) for item in value]
    if not isinstance(value, dict):
        return value
    result = {}
    for key, item in value.items():
        if key == 'page_idx':
            require(type(item) is int and 0 <= item < pages, 'segment page index outside span')
            result[key] = item+offset
        elif key in {'img_path', 'image_path'} and item:
            result[key] = _rewrite_resource(item, resources, middle=key == 'image_path')
        elif key in {'html', 'table_body'} and isinstance(item, str):
            result[key] = _rewrite_markdown(item, resources)
        else:
            result[key] = _rewrite_json(item, resources, offset, pages)
    return result


def _rewrite_markdown(text, resources):
    def mapped(value):
        enclosed = value.startswith('<') and value.endswith('>')
        path = value[1:-1] if enclosed else value
        if urlsplit(path).scheme or path.startswith('#'):
            return value
        new = _rewrite_resource(path.removeprefix('./'), resources)
        return '<'+new+'>' if enclosed else new
    # Image/ordinary inline links, HTML img sources, and reference definitions.
    text = re.sub(r'(!?\[[^\]\n]*\]\(\s*)(<[^>\n]+>|[^\s)]+)',
                  lambda m: m[1]+mapped(m[2]), text)
    text = re.sub(r'(<img\b[^>]*\bsrc\s*=\s*)(?:([\"\x27])(.*?)\2|([^\s>]+))',
                  lambda m: m[1]+(m[2] or '')+mapped(m[3] if m[2] else m[4])+(m[2] or ''), text, flags=re.I)
    text = re.sub(r'^(\s{0,3}\[[^\]\n]+\]:\s*)(<[^>\n]+>|\S+)',
                  lambda m: m[1]+mapped(m[2]), text, flags=re.M)
    return text


def merge_segments(plan, segment_zips, original_pdf):
    """Merge validated metadata with global page indexes and collision-free assets.

    The synthetic ZIP is accompanied by a distinct segmented receipt; callers
    must never put it in ResultCache under the original provider task identity.
    """
    import fitz
    from mineru_figure_sources import _metadata_files, _normalise, _geometry
    require(len(segment_zips) == len(plan['segments']), 'result coverage differs')
    original_pdf = Path(original_pdf)
    require(digest(original_pdf.read_bytes()) == plan['original_binding']['sha256'], 'original bytes changed')
    files, markdowns, content, pages, profile = {}, [], [], [], None
    with fitz.open(original_pdf) as original, fitz.open() as joined, tempfile.TemporaryDirectory(prefix='mineru-segment-merge-') as temporary:
        require(original.page_count == plan['page_count'], 'original page count differs')
        for index, (segment, payload) in enumerate(zip(plan['segments'], segment_zips), 1):
            root = Path(temporary)/str(index)
            markdown = safe_unzip(payload, root).decode('utf-8')
            found = _metadata_files(root)
            require(found is not None, 'complete segment metadata required')
            (_, segment_content), (_, middle), paths = found
            normalized = _normalise(segment_content, middle)
            count, offset = segment['page_end']-segment['page_start']+1, segment['page_start']-1
            require(len(normalized['pages']) == count, 'segment page coverage differs')
            embedded = [path for path in paths if path.is_file() and path.suffix.lower() == '.pdf']
            require(len(embedded) == 1, 'segment embedded PDF missing or ambiguous')
            with fitz.open(embedded[0]) as provider_pdf:
                require(not provider_pdf.is_encrypted and provider_pdf.page_count == count, 'embedded PDF coverage differs')
                for pi in range(count):
                    require(exact_json(_geometry(provider_pdf[pi]), _geometry(original[offset+pi])),
                            'embedded PDF geometry differs')
                joined.insert_pdf(provider_pdf)
            current_profile = {key: middle.get(key) for key in PROFILE}
            require(profile is None or exact_json(profile, current_profile), 'segment parser profiles differ')
            profile = current_profile
            for pi, page in enumerate(middle['pdf_info']):
                rect = original[offset+pi].rect
                require(abs(page['page_size'][0]-rect.width) <= 2 and abs(page['page_size'][1]-rect.height) <= 2,
                        'segment geometry differs from original')
            resources = {}
            for path in paths:
                if not path.is_file() or path.suffix.lower() in {'.md', '.json', '.pdf'}:
                    continue
                relative = path.relative_to(root).as_posix()
                target = f'images/segment{index:04d}/'+relative
                require(target not in files, 'resource name collision')
                resources[relative] = target
                files[target] = path.read_bytes()
            markdowns.append(_rewrite_markdown(markdown, resources))
            content.extend(_rewrite_json(segment_content, resources, offset, count))
            pages.extend(_rewrite_json(middle['pdf_info'], resources, offset, count))
        # Preserve the provider's actual returned pages. Existing figure proofs
        # compare these pages pixel-for-pixel against the authentic original.
        files['source.pdf'] = joined.tobytes(garbage=4, deflate=True, no_new_id=True)
    merged_middle = {**profile, 'pdf_info': pages}
    _normalise(content, merged_middle)
    files.update({'full.md': ('\n\n'.join(markdowns)+'\n').encode(),
                  'content_list.json': encoded(content), 'middle.json': encoded(merged_middle)})
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[name])
    payload = output.getvalue()
    with tempfile.TemporaryDirectory(prefix='mineru-segment-check-') as temporary:
        safe_unzip(payload, Path(temporary)/'raw')
    return payload


def validate_segment_receipt(receipt, original_binding, zip_bytes=None):
    """Validate a carried derived-delivery receipt, never a provider done claim."""
    _binding_valid(original_binding)
    require(isinstance(receipt, dict) and set(receipt) == {'schema', 'policy', 'original_binding',
        'page_count', 'page_limit', 'plan_sha256', 'segments', 'merged_zip_sha256', 'merged_zip_bytes'},
        'receipt fields')
    require(type(receipt['schema']) is int and receipt['schema'] == 1 and receipt['policy'] == POLICY
            and exact_json(receipt['original_binding'], original_binding), 'receipt identity')
    count, segments = receipt['page_count'], receipt['segments']
    require(type(count) is int and PAGE_LIMIT < count <= MAX_PAGES
            and type(receipt['page_limit']) is int and receipt['page_limit'] == PAGE_LIMIT
            and isinstance(segments, list) and len(segments) == (count+PAGE_LIMIT-1)//PAGE_LIMIT,
            'receipt segment count')
    plans, ids, tasks = [], set(), set()
    for index, segment in enumerate(segments):
        require(isinstance(segment, dict) and set(segment) == {'page_start', 'page_end', 'binding',
            'lineage', 'task_identity_sha256', 'result_zip_sha256'}, 'receipt segment fields')
        start, end = index*PAGE_LIMIT+1, min((index+1)*PAGE_LIMIT, count)
        require(type(segment['page_start']) is int and segment['page_start'] == start
                and type(segment['page_end']) is int and segment['page_end'] == end, 'receipt page coverage')
        binding, lineage = segment['binding'], segment['lineage']
        cache_identity(binding, lineage)
        require(all(exact_json(binding[key], original_binding[key]) for key in ('scope', 'endpoint', 'options'))
                and binding['source'] == f'_mineru-page-segments/v1/{original_binding["id"]}/p{start:04d}-{end:04d}.pdf'
                and binding['id'] != original_binding['id'] and binding['id'] not in ids
                and lineage['child_ordinal'] == 0 and lineage['batch_key'] not in tasks,
                'receipt derived identity')
        require(all(isinstance(segment[key], str) and HASH.fullmatch(segment[key])
                    for key in ('task_identity_sha256', 'result_zip_sha256')), 'receipt task hashes')
        ids.add(binding['id']); tasks.add(lineage['batch_key'])
        plans.append({key: segment[key] for key in ('page_start', 'page_end', 'binding')})
    plan = {key: receipt[key] for key in ('schema', 'policy', 'original_binding', 'page_count', 'page_limit')}
    plan['segments'] = plans
    require(receipt['plan_sha256'] == digest(encoded(plan))
            and isinstance(receipt['merged_zip_sha256'], str) and HASH.fullmatch(receipt['merged_zip_sha256'])
            and type(receipt['merged_zip_bytes']) is int and receipt['merged_zip_bytes'] > 0,
            'receipt aggregate hashes')
    if zip_bytes is not None:
        require(isinstance(zip_bytes, bytes) and len(zip_bytes) == receipt['merged_zip_bytes']
                and digest(zip_bytes) == receipt['merged_zip_sha256'], 'merged ZIP differs')
        with tempfile.TemporaryDirectory(prefix='mineru-segment-receipt-') as temporary:
            root = Path(temporary)/'raw'; safe_unzip(zip_bytes, root)
            from mineru_figure_sources import _metadata_files, _normalise
            found = _metadata_files(root)
            require(found is not None, 'merged metadata missing')
            require(len(_normalise(found[0][1], found[1][1])['pages']) == count, 'merged page coverage differs')
    return receipt


def run_segments(ledger, original_pdf, source, directory, *, result_cache, downloader,
                 timeout=1800, interval=15, allow_new=True):
    """Parse/reuse each bounded singleton and return an independently bound ZIP.

    downloader returns bytes, or (bytes, authentication). The latter supports the
    existing strict-first downloader and its immutable cache authentication.
    allow_new=False requires all accepted segment claims before any provider I/O.
    """
    require(type(allow_new) is bool and type(timeout) in {int, float} and 0 < timeout <= 3600,
            'execution policy')
    reader = copy.copy(ledger)
    reader.forbid_new_submissions = ledger.forbid_new_submissions or not allow_new
    archive = SegmentArchive(result_cache.client, result_cache.bucket)
    plan = prepare_segments(reader, original_pdf, source, directory,
                            allow_plan_write=not reader.forbid_new_submissions, archive=archive)
    require(plan is not None, 'segmentation not required')
    original = plan['original_binding']
    original_claim, _ = reader.store.get('sources/'+original['id'])
    preflight_segment_claims(reader, plan, required=reader.forbid_new_submissions)
    # Every physical original is immutable and read back before the first POST.
    # GET-only replay does not introduce a cache write.
    if not reader.forbid_new_submissions:
        for segment in plan['segments']:
            archive.preserve(original, segment['binding'], _segment_path(directory, segment).read_bytes())
    deadline, payloads, receipts, posts = reader.clock()+timeout, [], [], 0
    for segment in plan['segments']:
        require(exact_json(reader.bind(original_pdf, source), original), 'original bytes changed')
        path = _segment_path(directory, segment)
        require(exact_json(reader.bind(path, segment['binding']['source']), segment['binding']), 'segment bytes changed')
        remaining = deadline-reader.clock()
        require(remaining > 0, 'execution deadline reached')
        rows, summary = reader.run([(path, segment['binding']['source'])], timeout=remaining, interval=interval, queue_budget=0)
        posts += summary['provider_posts']
        require(summary['ready_for_generation'] and len(rows) == 1, 'segment parsing incomplete')
        batch = _claim(reader, segment['binding'], required=True)
        row = rows[0][1]
        require(row.get('data_id') == segment['binding']['id'], 'segment result identity differs')
        lineage = {'batch_id': batch['batch_id'], 'batch_key': batch['key'], 'parent_batch_key': batch['key'],
                   'data_id': segment['binding']['id'], 'child_ordinal': 0}
        payload = result_cache.get(segment['binding'], lineage)
        if payload is None:
            require(reader.clock() < deadline, 'execution deadline reached')
            result = downloader(row['full_zip_url'])
            if isinstance(result, tuple):
                payload, authentication = result
            else:
                payload, authentication = result, None
            if authentication is not None:
                from mineru_daily_result_cache import persist_authentication
                persist_authentication(result_cache, segment['binding'], lineage, payload, authentication)
            result_cache.put(segment['binding'], lineage, payload)
        payloads.append(payload)
        receipts.append({**segment, 'lineage': lineage, 'task_identity_sha256': task_identity(batch),
                         'result_zip_sha256': digest(payload)})
    require(exact_json(reader.bind(original_pdf, source), original), 'original bytes changed')
    current_claim, _ = reader.store.get('sources/'+original['id'])
    require(exact_json(current_claim, original_claim), 'original claim changed')
    payload = merge_segments(plan, payloads, original_pdf)
    receipt = {**plan, 'segments': receipts, 'plan_sha256': digest(encoded(plan)),
               'merged_zip_sha256': digest(payload), 'merged_zip_bytes': len(payload)}
    validate_segment_receipt(receipt, original, payload)
    return {'receipt': receipt, 'zip_bytes': payload, 'provider_posts': posts}
