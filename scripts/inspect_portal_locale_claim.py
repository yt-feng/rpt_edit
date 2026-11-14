"""Read one stopped locale claim and expose only its exact Actions identities."""
import argparse
import json
import os
import re

from portal_extended_continuation import producer_identity, queue, read_origin
from portal_extended_locales import ExpansionError, select_locales
from portal_extended_r2 import R2Store


def inspect(store, locale, generation, *, api=None, owner=None, repository=None):
    if select_locales(locale) != (locale,) or not re.fullmatch(r'[0-9a-f]{64}', generation):
        raise ExpansionError('An exact locale and source generation are required')
    row = queue(store, locale).get(generation)
    if row is None:
        return {'locale': locale, 'generation': generation, 'status': 'absent'}
    origin = read_origin(store, generation)
    if origin is None:
        raise ExpansionError('The immutable claim origin is absent')
    result = {'locale': locale, 'generation': generation, 'status': row['status'],
            'continuations': row['continuations'], 'has_snapshot': 'snapshot' in row,
            'owner': producer_identity(row['owner']) if row.get('owner') else None,
            'source_producer': producer_identity(origin['producer']), 'source_day': origin['source_day']}
    if api is not None and row['status'] in {'started', 'claimed'}:
        from portal_extended_unstarted_claims import UnstartedClaims
        scan = UnstartedClaims(store, repository, owner, api)
        result['recovery_eligible'] = scan.eligible(locale, generation, row, origin)
        result['recovery_code'] = scan.reasons.get((locale, generation), '')
        result['proof_api_reads'] = scan.api_reads
        result['r2_writes'] = 0
        result['model_calls'] = 0
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--locale', required=True)
    parser.add_argument('--generation', required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
            or os.environ.get('KC_PUBLIC_REPOSITORY') != 'true'):
        raise ExpansionError('Claim inspection requires public main Actions')
    from review_portal_extended_handoff import api
    owner = producer_identity({'run_id':os.environ['GITHUB_RUN_ID'],
        'attempt':os.environ['GITHUB_RUN_ATTEMPT'], 'sha':os.environ['GITHUB_SHA']})
    print(json.dumps(inspect(R2Store.from_env('_extended-locales/v1'), args.locale, args.generation,
        api=api, owner=owner, repository=os.environ['GITHUB_REPOSITORY']), sort_keys=True))


if __name__ == '__main__':
    main()
