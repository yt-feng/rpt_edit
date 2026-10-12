"""Temporary single-book GHA observation. Never download PDFs or update intake."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

import imf_cloud_browser as b
import imf_elibrary_resolver as r

BRANCH = 'codex/imf-fiscal-book-observation-20261013'
OUTPUT = Path('_imf_fiscal_observation')
FIXTURE = 'fiscal_book_observed_crossref.json'
FIXTURE_SHA = '4d212b5110f4b220596d483b93694dae99050d2d59280f8feee4f20223f63dd4'


def require_approval():
    b.require_cloud()
    if (os.environ.get('GITHUB_REPOSITORY') != 'yt-feng/rpt_edit'
            or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or os.environ.get('GITHUB_WORKFLOW_REF') !=
            f'yt-feng/rpt_edit/.github/workflows/institution-fetch-test.yml@refs/heads/{BRANCH}'):
        raise b.BrowserDownloadError('imf_browser_cloud_approval_required')


def source_and_candidate(fixture):
    """Use the exact observed Crossref book resource; never construct a URL."""
    message = fixture['message']
    doi, isbns = message['DOI'], message['ISBN']
    if (fixture['status'] != 'ok' or message['type'] != 'edited-book'
            or not isinstance(isbns, list) or len(isbns) != 1
            or not r.isbn_valid(isbns[0]) or doi != '10.5089/' + isbns[0] + '.089'):
        raise ValueError('book_identity_invalid')
    title, subtitle = message['title'], message['subtitle']
    if (not isinstance(title, list) or len(title) != 1 or not isinstance(title[0], str) or not title[0]
            or not isinstance(subtitle, list) or len(subtitle) != 1 or not isinstance(subtitle[0], str) or not subtitle[0]):
        raise ValueError('book_title_invalid')
    candidate = message['resource']['primary']['URL']
    locator = r.validate_publication_url(candidate)
    if locator['kind'] != 'book' or locator['isbn'] != isbns[0]:
        raise ValueError('book_resource_invalid')
    publication = dict(doi=doi, isbn=isbns[0], title=title[0], subtitle=subtitle[0],
                       full_title=title[0] + ': ' + subtitle[0], landing_url=candidate,
                       crossref_sha256=FIXTURE_SHA, pdf_verified=False)
    return publication, candidate


def load_sources():
    path = Path(__file__).parent / 'fixtures/imf_elibrary' / FIXTURE
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != FIXTURE_SHA:
        raise ValueError('book_fixture_changed')
    return [source_and_candidate(json.loads(raw))]


def observe(candidate, proxy):
    require_approval()
    with tempfile.TemporaryDirectory(prefix='imf-fiscal-observe-', dir=os.environ.get('RUNNER_TEMP')) as folder:
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
    report = {'schema': 1, 'accepted': False, 'purpose': 'official_crossref_book_observation_only',
              'expected_sources': 1, 'pdf_downloads': 0, 'rows': []}
    try:
        with b.CloudImfBrowser(fetch_subscription=f._fetch_subscription, decode_subscription=f._b64_text) as browser:
            if not browser.enabled:
                raise b.BrowserDownloadError('imf_browser_not_enabled')
            browser._start()
            for publication, candidate in rows:
                page = observe(candidate, browser._proxy)
                name = hashlib.sha256(publication['doi'].encode()).hexdigest() + '.json'
                record = {'schema': 1, 'accepted': False, 'book_publication': publication,
                          'candidate_url': candidate, 'page': page, 'pdf_downloads': 0}
                (OUTPUT / name).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
                report['rows'].append({'book_doi': publication['doi'], 'file': name,
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
