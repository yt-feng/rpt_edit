"""Temporary header-only checks of the three already observed official IEO URLs."""
from cloud_imf_fiscal_observation import require_approval

TARGETS = (
    ('directory', 'https://ieo.imf.org/en/evaluations'),
    ('evaluation', 'https://ieo.imf.org/en/evaluations/completed/2025-1216-imf-advice-on-fiscal-policy'),
    ('pdf', 'https://ieo.imf.org/-/media/ieo/files/evaluations/follow-up/fp-mip.pdf'),
)


def observe_headers(cloud_proxy):
    require_approval()  # Before requests import, environment access or sessions.
    import requests
    results = []
    for route, proxy in (('direct', None), ('cloud_client', cloud_proxy)):
        with requests.Session() as session:
            session.trust_env = False
            session.proxies = {} if proxy is None else {'http': proxy, 'https': proxy}
            for stage, url in TARGETS:
                row = dict(route=route, stage=stage, method='GET', status=None,
                           final_official_url=None, redirected=None, category='request_failed', body_read=False)
                response = None
                try:
                    response = session.get(url, stream=True, allow_redirects=False, timeout=(10, 20))
                    status = response.status_code
                    if type(status) is int and 100 <= status <= 599:
                        row.update(status=status, redirected=300 <= status < 400,
                                   final_official_url=response.url if response.url == url else None,
                                   category='http_response')
                except requests.exceptions.ProxyError:
                    row['category'] = 'proxy_connection_failed'
                except requests.exceptions.ConnectTimeout:
                    row['category'] = 'connect_timeout'
                except requests.exceptions.ReadTimeout:
                    row['category'] = 'read_timeout'
                except requests.exceptions.SSLError:
                    row['category'] = 'tls_failed'
                except requests.exceptions.ConnectionError:
                    row['category'] = 'connection_failed'
                except Exception:
                    pass  # Never serialize exception text, chain, endpoint or headers.
                finally:
                    if response is not None:
                        try:
                            response.close()  # Never access content, text, iter_content or raw.
                        except Exception:
                            row['category'] = 'response_close_failed'
                results.append(row)
    return dict(schema=1, accepted=False, purpose='official_ieo_response_headers_only',
                expected_requests=6, body_reads=0, rows=results)
