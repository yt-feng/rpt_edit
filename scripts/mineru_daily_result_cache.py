"""Private authentication evidence for automatic MinerU result recovery.

The normal result-cache schema remains unchanged. Each recovery attempt records
its own immutable evidence before the complete ZIP can be released to generation.
"""
from mineru_daily_result_transport import validate_daily_authentication
from mineru_result_cache import MAX_RECEIPT, ResultCacheError, identity
from mineru_task_ledger import digest, encoded

AUTH_PREFIX = '_workflow-cache/mineru-result-auth/v1/daily'


def persist_authentication(cache, binding, lineage, payload, authentication):
    authentication = validate_daily_authentication(authentication)
    identity_sha = identity(binding, lineage)
    zip_sha = digest(payload)
    receipt = {'schema_version': 1, 'policy': 'daily-exact-leaf-result-cache-v1',
               'identity_sha256': identity_sha, 'source_binding': binding, 'lineage': lineage,
               'zip_sha256': zip_sha, 'zip_bytes': len(payload), 'authentication': authentication}
    raw = encoded(receipt)
    if len(raw) > MAX_RECEIPT:
        raise ResultCacheError('cache_authentication_size')
    # Fresh preflights have fresh leases. A prior interrupted attempt must not
    # prevent this attempt's evidence from being persisted and read back.
    receipt_sha = digest(raw)
    cache._immutable(f'{AUTH_PREFIX}/{identity_sha}/{zip_sha}/{receipt_sha}.json', raw,
                     content_type='application/json', identity_sha=identity_sha, maximum=MAX_RECEIPT)
    return receipt_sha
