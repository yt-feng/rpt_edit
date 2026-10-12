"""Read only nonsensitive subscription renewal metadata in Actions."""
import json
import os
from pathlib import Path
from urllib.parse import urlsplit
import requests
assert os.getenv('GITHUB_ACTIONS')=='true'
out=Path('_imf_provider_metadata');out.mkdir(exist_ok=True)
summary={}
try:
    address=os.environ['PROXY_SUBSCRIPTION_URL']
    r=requests.get(address,timeout=15)
    summary['status']=r.status_code
    webpage=r.headers.get('profile-web-page-url','')
    candidate=urlsplit(webpage if webpage.startswith('https://') else address)
    if candidate.scheme=='https' and candidate.hostname and not candidate.username:
        summary['provider_origin']='https://'+candidate.hostname
        summary['origin_basis']='subscription_account_homepage_header' if webpage.startswith('https://') else 'subscription_host'
except Exception as e:
    summary['error_type']=type(e).__name__
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
