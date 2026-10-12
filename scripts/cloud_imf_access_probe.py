"""Cloud-only, bounded public-source diagnostic; never prints proxy identities."""
import base64
import concurrent.futures
import hashlib
import io
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

import requests
from curl_cffi import requests as cffi
from pypdf import PdfReader
import fetch_institution_latest_pdfs as f

assert os.environ.get('GITHUB_ACTIONS') == 'true', 'Run only in GitHub Actions'
out = Path('_imf_access_probe')
out.mkdir(exist_ok=True)
seed = json.loads(Path('institution_feeds/pending_intake/imf.json').read_text())
item = next(iter(seed['items'].values()))['item']
pdf = item['pdf_candidates'][0]
targets = [('connectivity', 'https://www.gstatic.com/generate_204'), ('landing', item['source_url']), ('pdf', pdf)]
result = {'source':item, 'subscription':{}, 'probes':[]}
subscription = os.environ.get('PROXY_SUBSCRIPTION_URL', '')
nodes = []
if subscription:
    try:
        r = requests.get(subscription, timeout=15, headers={'User-Agent':f.DEFAULT_USER_AGENT})
        result['subscription']['status'] = r.status_code
        if r.ok:
            body = r.text.strip()
            if '://' not in body.splitlines()[0]:
                body = f._b64_text(body) or body
            nodes = [p for p in (f._normalize_proxy_node(x) for x in body.splitlines() if x.strip()) if p][:12]
            result['subscription']['compatible_nodes'] = len(nodes)
    except Exception as e:
        result['subscription']['error_type'] = type(e).__name__

def probe(index, proxy, kind, url, client='cffi'):
    row = {'route_index':index, 'route_scheme':urlsplit(proxy).scheme if proxy else 'direct', 'target':kind, 'client':client}
    try:
        kwargs = {'timeout':10, 'headers':f.source_request_headers()}
        if proxy:
            kwargs['proxies'] = {'http':proxy,'https':proxy}
        if client == 'cffi':
            kwargs['impersonate'] = 'chrome'
            r = cffi.get(url, **kwargs)
        else:
            r = requests.get(url, **kwargs)
        row.update(status=r.status_code, content_type=r.headers.get('content-type',''), bytes=len(r.content), pdf=f.is_pdf_bytes(r.content))
        if row['pdf'] and len(r.content)<32*1024*1024:
            reader=PdfReader(io.BytesIO(r.content))
            row.update(sha256=hashlib.sha256(r.content).hexdigest(), pages=len(reader.pages), first_page_text=(reader.pages[0].extract_text() or '')[:500])
            (out/f'{index}-{kind}-{client}.pdf').write_bytes(r.content)
    except Exception as e:
        row['error_type']=type(e).__name__
        code=getattr(e,'code',None)
        if isinstance(code,(int,str)) and len(str(code))<10:
            row['error_code']=code
    return row

jobs=[]
for index,proxy in enumerate([None]+nodes):
    for kind,url in targets:
        jobs.append((index,proxy,kind,url,'cffi'))
# Confirm official origin URL observed in the public discovery result independently.
jobs.append((0,None,'observed_origin_pdf',pdf.replace('://www.imf.org/', '://origin-www.imf.org/'),'cffi'))
jobs.append((0,None,'pdf',pdf,'requests'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for row in pool.map(lambda args:probe(*args),jobs):
        result['probes'].append(row)
        print(json.dumps(row,ensure_ascii=False),flush=True)
(out/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'subscription':result['subscription'],'valid_pdf_probes':sum(p.get('pdf',False) for p in result['probes'])}))
