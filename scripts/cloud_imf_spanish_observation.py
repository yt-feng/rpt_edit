"""Temporary two-source GHA observation. Never download PDFs or update intake."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit, urlunsplit

import imf_cloud_browser as b
import imf_elibrary_resolver as r

BRANCH = 'codex/imf-spanish-edition-observation-20261013'
OUTPUT = Path('_imf_spanish_observation')
FIXTURES = ('chile_hls_observed_metadata.json', 'chile_tar_observed_metadata.json')


def require_approval():
    b.require_cloud()
    if (os.environ.get('GITHUB_REPOSITORY') != 'yt-feng/rpt_edit'
            or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or os.environ.get('GITHUB_WORKFLOW_REF') !=
            f'yt-feng/rpt_edit/.github/workflows/institution-fetch-test.yml@refs/heads/{BRANCH}'):
        raise b.BrowserDownloadError('imf_browser_cloud_approval_required')


def source_and_candidate(fixture):
    """Candidate only: strict source DOI chain stays immutable and distinct."""
    identity = r.bind_source(fixture['item'], {}, fixture['preview_excerpt'], fixture['item']['source_url'])
    publication = r.resolve_crossref(identity, fixture['crossref'])
    loc = r.validate_publication_url(publication['landing_url'])
    if (publication.get('original_language') != 'es' or loc['kind'] != 'journal'
            or loc['series'] not in {'019', '029'} or loc['language'] != 'en'
            or loc['year'] != publication['year'] or loc['issue'] != publication['issue']):
        raise ValueError('candidate_not_supported')
    original = urlsplit(publication['landing_url'])
    # This is the one source-declared language of the same exact issue. No
    # publication/DOI is guessed or replaced; a URL is not evidence of success.
    path = loc['document_path'].removesuffix('-en') + '-es.xml'
    candidate = urlunsplit((original.scheme, original.netloc, path, '', ''))
    result = r.validate_publication_url(candidate)
    if any(result[key] != loc[key] for key in ('kind', 'series', 'year', 'issue', 'document')) or result['language'] != 'es':
        raise ValueError('candidate_not_supported')
    return publication, candidate


def load_sources():
    folder = Path(__file__).parent / 'fixtures/imf_elibrary'
    rows = [source_and_candidate(json.loads((folder / name).read_text())) for name in FIXTURES]
    if len({row[0]['source_guid'] for row in rows}) != 2:
        raise ValueError('fixture_identity_invalid')
    return rows


def observe(candidate, proxy):
    require_approval()
    with tempfile.TemporaryDirectory(prefix='imf-spanish-observe-', dir=os.environ.get('RUNNER_TEMP')) as folder:
        os.chmod(folder, 0o700)
        request = Path(folder) / 'request.json'
        with os.fdopen(os.open(request, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600), 'w') as stream:
            json.dump({'candidate_url': candidate}, stream)
        proc = None
        try:
            proc = subprocess.Popen(['node', str(Path(__file__).with_suffix('.cjs')), str(request)],
                                    env=b.child_environment(proxy), start_new_session=True,
                                    stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            page = b.read_message(proc, 110)
            if proc.wait(timeout=10) != 0 and page.get('stage') != 'error':
                return {'stage': 'error', 'category': 'observer_process_failed'}
            return page
        except b.BrowserDownloadError as error:
            return {'stage': 'error', 'category': error.category}
        except Exception:
            return {'stage': 'error', 'category': 'observer_failed'}
        finally:
            if proc is not None:
                b.stop_browser(proc)


def main():
    require_approval()  # Before subscription import/access, sockets or processes.
    rows = load_sources()
    import fetch_institution_latest_pdfs as f
    OUTPUT.mkdir(parents=True, exist_ok=True)
    report = {'schema': 1, 'accepted': False, 'purpose': 'public_language_candidate_observation_only',
              'expected_sources': 2, 'pdf_downloads': 0, 'rows': []}
    try:
        with b.CloudImfBrowser(fetch_subscription=f._fetch_subscription, decode_subscription=f._b64_text) as browser:
            if not browser.enabled:
                raise b.BrowserDownloadError('imf_browser_not_enabled')
            browser._start()
            for publication, candidate in rows:
                page = observe(candidate, browser._proxy)
                name = hashlib.sha256(publication['source_guid'].encode()).hexdigest() + '.json'
                record = {'schema': 1, 'accepted': False, 'source_publication': publication,
                          'candidate_url': candidate, 'page': page, 'pdf_downloads': 0}
                (OUTPUT / name).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
                report['rows'].append({'source_guid': publication['source_guid'], 'file': name,
                                       'status': page.get('landing_status'), 'stage': page.get('stage')})
    except b.BrowserDownloadError as error:
        report['error'] = error.category
    except KeyboardInterrupt:
        report['error'] = 'interrupted'
    except Exception:
        report['error'] = 'observation_stopped'
    finally:
        (OUTPUT / 'summary.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'observed_sources': len(report['rows']), 'pdf_downloads': 0,
                      'accepted': False, 'error': report.get('error')}))
    return 1 if report.get('error') else 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except b.BrowserDownloadError as error:
        print(json.dumps({'accepted': False, 'error': error.category}))
        raise SystemExit(1) from None
    except Exception:
        print(json.dumps({'accepted': False, 'error': 'observation_setup_failed'}))
        raise SystemExit(1) from None
