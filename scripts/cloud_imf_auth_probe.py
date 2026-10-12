"""Cloud-only structured diagnostics. Never emit route identities or raw errors."""
import base64
import io
import json
import hashlib
import os
from pathlib import Path
from urllib.parse import urlsplit, unquote, quote
import requests
from curl_cffi import requests as cffi
from pypdf import PdfReader
import fetch_institution_latest_pdfs as f
assert os.getenv('GITHUB_ACTIONS')=='true'
out=Path('_imf_auth_probe'); out.mkdir(exist_ok=True)
rows=[]
seed=json.loads(Path('institution_feeds/pending_intake/imf.json').read_text())
item=next(iter(seed['items'].values()))['item']

def probe(label,url,proxy=None,auth=None):
    row={'label':label}
    try:
        kw={'timeout':12,'impersonate':'chrome','headers':f.source_request_headers()}
        if proxy:
            kw['proxy']=proxy
        if auth:
            kw['proxy_auth']=auth
        r=cffi.get(url,**kw)
        row.update(status=r.status_code,bytes=len(r.content),pdf=f.is_pdf_bytes(r.content),content_type=r.headers.get('content-type',''))
        if row['pdf']:
            reader=PdfReader(io.BytesIO(r.content));row.update(sha256=hashlib.sha256(r.content).hexdigest(),pages=len(reader.pages),title=(reader.pages[0].extract_text() or '')[:400]);(out/(row['sha256']+'.pdf')).write_bytes(r.content)
    except Exception as e:
        row.update(error_type=type(e).__name__,error_code=getattr(e,'code',None))
        message=str(e).lower()
        patterns={'auth_method_rejected':'no authentication method','user_rejected':'user was rejected','socks_connection_denied':'cannot complete socks5 connection','connection_refused':'connection refused','connect_failed':'could not connect','hostname_resolution':'could not resolve'}
        row['error_categories']=[key for key,value in patterns.items() if value in message]
    rows.append(row)

subscription=os.getenv('PROXY_SUBSCRIPTION_URL','')
structure=[]
if subscription:
    try:
        r=requests.get(subscription,timeout=15);r.raise_for_status();body=r.text.strip()
        if '://' not in body.splitlines()[0]:body=f._b64_text(body) or body
        socks=[f._normalize_proxy_node(x) for x in body.splitlines() if x.startswith('socks5://') or x.startswith('socks5h://')]
        for index,node in enumerate(socks[:1]):
            p=urlsplit(node); username=unquote(p.username or '');password=unquote(p.password or '')
            meta={'index':index,'username_present':bool(p.username),'password_present':p.password is not None,'username_over_255':len(username)>255,'password_over_255':len(password)>255}
            decoded=None
            if p.username and p.password is None:
                try:
                    decoded=base64.b64decode(username+'='*(-len(username)%4),validate=True).decode('utf-8')
                except Exception:pass
            meta['encoded_userinfo_pair']=bool(decoded and ':' in decoded and all(decoded.split(':',1)))
            structure.append(meta)
            probe('socks_current_connectivity','https://www.gstatic.com/generate_204',node)
            if meta['encoded_userinfo_pair']:
                user,pwd=decoded.split(':',1)
                clean=f'{p.scheme}://{p.hostname}:{p.port}'
                probe('socks_decoded_connectivity','https://www.gstatic.com/generate_204',clean,(user,pwd))
                probe('socks_decoded_official_pdf',item['pdf_candidates'][0],clean,(user,pwd))
            elif username and password:
                clean=f'{p.scheme}://{p.hostname}:{p.port}'
                probe('socks_explicit_auth_connectivity','https://www.gstatic.com/generate_204',clean,(username,password))
                probe('socks_explicit_auth_official_pdf',item['pdf_candidates'][0],clean,(username,password))
    except Exception as e:
        structure.append({'error_type':type(e).__name__})
probe('observed_crossref_elibrary','https://elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml?cid=580315-com-dsp-crossref')
probe('elibrary_series_pdf','https://elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf')
probe('elibrary_article_pdf','https://elibrary.imf.org/downloadpdf/view/journals/019/2026/082/article-A001-en.pdf')
result={'structure':structure,'probes':rows};(out/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
