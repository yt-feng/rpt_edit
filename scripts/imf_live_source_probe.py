"""Read-only cloud acceptance of the three IMF originals from run 38658714099.

Resolve fresh official source metadata and download through the production
adapter. Only the isolated artifact directory is written; this probe never
calls the intake, original cache, MinerU, models, publication or seen writers.
"""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path

from imf_cloud_browser import BrowserDownloadError, CloudImfBrowser, require_cloud

FIXTURE = Path('scripts/fixtures/institution_sources/imf_live_exact_20261015.json')
FIXTURE_SHA = '4d5f324a8e079dd3a448f778175df69d5af4f268d057e9711910181b495d3a51'
PROTECTED = ('institution_feeds/pending_intake/imf.json', 'institution_feeds/seen_state.json',
             'institution_feeds/institution_pdf_archive.jsonl')
OUT = Path('_fetch_test')


class ProbeError(ValueError):
    pass


def require(condition, category):
    if not condition:
        raise ProbeError(category)


def digest(path):
    require(path.is_file() and not path.is_symlink(), 'regular_file_required')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def targets(root):
    require(digest(root / FIXTURE) == FIXTURE_SHA, 'frozen_sources_changed')
    data = json.loads((root / FIXTURE).read_text())
    rows = data['records']
    require(data['schema'] == 1 and data['source_run_id'] == '38658714099' and len(rows) == 3,
            'source_scope_changed')
    require(len({row['item']['guid'] for row in rows}) == 3, 'source_scope_changed')
    return rows


def probe(root, producer, *, browser_factory=CloudImfBrowser):
    require_cloud()
    require(os.environ.get('IMF_CLOUD_BROWSER_ENABLED') == 'true', 'cloud_browser_required')
    from institution_source_health import validate_live_download

    rows = targets(root)
    output = root / OUT
    require(not output.exists(), 'probe_output_must_be_fresh')
    before = {path: digest(root / path) for path in PROTECTED}
    output.mkdir()
    result = {'schema': 1, 'scope': 'imf-live-exact-20261015', 'accepted': False,
              'source_run_id': '38658714099', 'expected_count': 3, 'reports': []}
    cfg = deepcopy(producer.INSTITUTIONS['imf'])
    with producer.requests.Session() as session, browser_factory(
            fetch_subscription=producer._fetch_subscription, decode_subscription=producer._b64_text) as browser:
        session.trust_env = False
        session.headers.update(producer.source_request_headers())
        for source in rows:
            item = deepcopy(source['item'])
            report = {'source_guid': item['guid'], 'source_url': item['source_url'], 'title': item['title'],
                      'published': item['date'], 'expected_sha256': source['sha256'],
                      'expected_bytes': source['bytes'], 'accepted': False}
            started = False
            try:
                # Fresh preview/Crossref resolution is the normal production
                # identity path. Frozen URLs are never accepted as live proof.
                publication = producer.resolve_imf_browser_publication(cfg, session, item, 30)
                require(publication['source_guid'] == item['guid'] and publication['source_url'] == item['source_url']
                        and publication['source_title'] == item['title'], 'resolved_source_changed')
                started = True
                destination = output / source['local_filename']
                proof = browser.download(publication, destination, 128 * 1024 * 1024,
                                         expected_sha256=source['sha256'])
                require(proof['source_guid'] == item['guid'] and proof['source_url'] == item['source_url'],
                        'downloaded_source_changed')
                require(digest(destination) == proof['sha256'] == source['sha256']
                        and destination.stat().st_size == proof['bytes'] == source['bytes'], 'original_bytes_changed')
                receipt_row = {'institution': 'imf', 'title': item['title'], 'source_page_url': item['source_url'],
                               'local_filename': source['local_filename'], 'pdf_url': proof['pdf_url'],
                               'sha256': proof['sha256'], 'bytes': proof['bytes'], 'imf_live_download': proof}
                validate_live_download(receipt_row)
                report.update(accepted=True, sha256=proof['sha256'], bytes=proof['bytes'],
                              pages=proof['pages'], imf_live_download=proof)
            except Exception as error:
                report['error'] = (str(error) if isinstance(error, (ProbeError, BrowserDownloadError))
                                   else type(error).__name__)
            finally:
                report['source_attempts'] = deepcopy(browser.last_source_attempts) if started else []
                result['reports'].append(report)
    result['production_state_unchanged'] = before == {path: digest(root / path) for path in PROTECTED}
    result['verified_count'] = sum(row['accepted'] for row in result['reports'])
    result['accepted'] = result['verified_count'] == 3 and result['production_state_unchanged']
    (output / 'exact-scope-acceptance.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    require_cloud()
    import fetch_institution_latest_pdfs as producer
    result = probe(Path.cwd(), producer)
    # The artifact contains official source proofs; stdout stays compact and
    # excludes raw HTTP, runtime configuration and remote provider values.
    print(json.dumps({key: result[key] for key in ('scope', 'accepted', 'expected_count',
                                                  'verified_count', 'production_state_unchanged')}))
    return 0 if result['accepted'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
