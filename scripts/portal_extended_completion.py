"""Exact completed locale provenance, including bounded legacy log adoption."""
from __future__ import annotations
import json
import re

from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import HEX64, R2NotFound, R2TransportError, error_code

POLICY = 'exact-locale-completion-v1'
WORKFLOW = '.github/workflows/portal-extended-locales-r2.yml'
MAX_LOG_BYTES = 1024 * 1024


def require(ok, code):
    if not ok: raise ExpansionError(code)


def receipt_key(store, identity):
    require(isinstance(identity,str) and HEX64.fullmatch(identity), 'completion_identity_invalid')
    return store.key('incremental','locale-completions',identity,'receipt.json')


def adoption_key(store, origin, locale):
    from portal_extended_locales import select_locales
    require(select_locales(locale)==(locale,), 'completion_locale_invalid')
    return store.key('incremental','completion-adoptions',origin['generation'],locale,
                     digest(stable_bytes(origin))+'.json')


def optional(store, key):
    try: raw=store._get(key,maximum=65536)
    except R2NotFound:return None
    value=json.loads(raw)
    require(raw==stable_bytes(value),'completion_record_not_canonical')
    return value


def immutable(store, key, value):
    raw=stable_bytes(value)
    require(len(raw)<=65536,'completion_record_oversized')
    try:
        store.client.put_object(Bucket=store.bucket,Key=key,Body=raw,ContentType='application/json',
            CacheControl='private, no-store',Metadata={'sha256':digest(raw),'kind':POLICY},IfNoneMatch='*')
    except Exception as error:
        if error_code(error) not in {'preconditionfailed','412','conditionalrequestconflict','409'}:
            raise R2TransportError('completion_write_unresolved') from None
    require(store._get(key,maximum=65536)==raw,'completion_immutable_conflict')


def record(store, origin, locale, snapshot, producer, *, evidence=None):
    from portal_extended_continuation import producer_identity
    value={'schema_version':1,'policy':POLICY,'generation':origin['generation'],'locale':locale,
        'origin_sha256':digest(stable_bytes(origin)),'source_sha256':origin['source_sha256'],
        'snapshot':snapshot,'producer':producer_identity(producer),
        'evidence':evidence or {'kind':'native-result'}}
    from portal_extended_daily_queue import immutable_record
    identity=digest(stable_bytes(value))
    immutable_record(store,receipt_key(store,identity),value,kind=POLICY)
    return identity


def request(value):
    from portal_extended_continuation import producer_identity
    require(isinstance(value,dict) and set(value)=={'producer','source_job_id','locale_job_id',
        'source_log_sha256','locale_log_sha256','previous_checkpoint_sha256'},'completion_request_invalid')
    producer_identity(value['producer'])
    require(all(type(value[k]) is int and value[k]>0 for k in ('source_job_id','locale_job_id'))
            and value['source_job_id']!=value['locale_job_id'],'completion_job_identity_invalid')
    require(all(isinstance(value[k],str) and HEX64.fullmatch(value[k]) for k in
        ('source_log_sha256','locale_log_sha256','previous_checkpoint_sha256')),'completion_hash_invalid')
    return value


def completed_jobs(repository, producer, locale, api):
    from portal_extended_continuation import producer_identity
    producer=producer_identity(producer)
    path=f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
    run=api(path);response=api(path+'/jobs?per_page=100')
    require(run.get('id')==int(producer['run_id']) and run.get('run_attempt')==int(producer['attempt'])
        and run.get('head_sha')==producer['sha'] and run.get('status')=='completed'
        and run.get('conclusion') in {'success','failure'} and run.get('path')==WORKFLOW
        and run.get('head_branch')=='main' and run.get('event') in {'workflow_dispatch','workflow_run'}
        and all((run.get(k)or{}).get('full_name')==repository for k in ('repository','head_repository'))
        and (run.get('repository')or{}).get('private') is False,'completion_run_unproved')
    jobs=response.get('jobs')
    require(type(response.get('total_count')) is int and isinstance(jobs,list)
        and 0<len(jobs)==response['total_count']<=100,'completion_job_inventory_incomplete')
    selected=[]
    for name in ('source',f'locale ({locale})'):
        matches=[j for j in jobs if j.get('name')==name]
        require(len(matches)==1,'completion_job_not_unique')
        job=matches[0]
        require(job.get('status')=='completed' and job.get('conclusion')=='success'
            and job.get('run_id')==int(producer['run_id']) and job.get('head_sha')==producer['sha']
            and type(job.get('id')) is int and job['id']>0,'completion_job_unproved')
        selected.append(job)
    return selected


def log_records(raw):
    require(isinstance(raw,bytes) and 0<len(raw)<=MAX_LOG_BYTES,'completion_log_size_invalid')
    records=[]
    for line in raw.decode('utf-8').splitlines():
        match=re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z (\{.*\})',line)
        if match:
            try:value=json.loads(match[1])
            except ValueError:continue
            if isinstance(value,dict):records.append(value)
    return records


def verify_log_evidence(store, origin, locale, snapshot, value, repository, api, raw):
    from portal_extended_continuation import checkpoint_evidence
    value=request(value)
    source_job,locale_job=completed_jobs(repository,value['producer'],locale,api)
    require(source_job['id']==value['source_job_id'] and locale_job['id']==value['locale_job_id'],
            'completion_requested_jobs_differ')
    comparison=api(f'repos/{repository}/compare/{origin["producer"]["sha"]}...{value["producer"]["sha"]}')
    require(comparison.get('status') in {'identical','ahead'}
        and (comparison.get('merge_base_commit')or{}).get('sha')==origin['producer']['sha'],
        'completion_source_lineage_unproved')
    logs={kind:raw(f'actions/jobs/{value[kind+"_job_id"]}/logs',MAX_LOG_BYTES) for kind in ('source','locale')}
    require(all(digest(logs[kind])==value[kind+'_log_sha256'] for kind in logs),'completion_log_hash_differs')
    source,translated=(log_records(logs[kind]) for kind in ('source','locale'))
    claims=[v for v in source if v.get('continuation') is True and v.get('generation')==origin['generation']
            and v.get('day')==origin['source_day']]
    claimed=json.loads(claims[0].get('locales_json','null')) if len(claims)==1 else None
    require(isinstance(claimed,list) and locale in claimed,'completion_source_claim_unproved')
    require(any(v.get('generation')==origin['generation'] and v.get('sha256')==origin['source_sha256']
                and 'locale' not in v for v in translated),'completion_source_hash_unproved')
    require(any(v.get('generation')==origin['generation'] and v.get('locale')==locale
                and v.get('present') is True and v.get('sha256')==value['previous_checkpoint_sha256']
                for v in translated),'completion_previous_checkpoint_unproved')
    require(any(v.get('generation')==origin['generation'] and v.get('locale')==locale
                and v.get('sha256')==snapshot['checkpoint_sha256'] and 'pointer_key' in v
                for v in translated),'completion_checkpoint_unproved')
    require(any(v.get('source_generation')==origin['generation'] and v.get('locale')==locale
                and v.get('candidate_id')==snapshot['candidate_id'] and v.get('manifest_sha256')==snapshot['manifest_sha256']
                and v.get('status')=='complete-candidate' and v.get('ready') is True
                and v.get('completed_page_count')==origin['pages'] for v in translated),
                'completion_candidate_unproved')
    before=checkpoint_evidence(store,locale,origin['generation'],value['previous_checkpoint_sha256'])
    after=checkpoint_evidence(store,locale,origin['generation'],snapshot['checkpoint_sha256'])
    require(before<=after,'completion_checkpoint_regressed')
    return {'kind':'github-log-adoption','repository':repository,**value}


def authenticate(store, origin, locale, repository, api, *, adoption=None, capture=False, raw=None, expected_snapshot=None, completed_row=None):
    """Called only after the unchanged original source-job verification."""
    from portal_extended_continuation import queue, origin_allows_locale, validate_snapshot
    require(origin_allows_locale(origin,locale),'completion_locale_outside_origin')
    row=queue(store,locale).get(origin['generation'],{})
    if completed_row is not None:
        require(not row or row==completed_row,'completion_current_row_advanced')
        from portal_extended_quality_recovery import exact_result
        row=exact_result(store,locale,origin['generation'],completed_row)
    require(row.get('status')=='complete','completion_requires_current_complete_result')
    validate_snapshot(store,locale,origin['generation'],row)
    identity=row.get('completion_sha256')
    if identity is None:
        adopted=optional(store,adoption_key(store,origin,locale))
        if adopted is not None:
            require(set(adopted)=={'completion_sha256'},'completion_adoption_invalid')
            identity=adopted['completion_sha256']
    if identity is None:
        require(adoption is not None,'completion_producer_evidence_missing')
        require(expected_snapshot is None or row['snapshot']==expected_snapshot,'completion_requested_snapshot_differs')
        if raw is None:
            from portal_extended_recovered_admission import GitHub
            raw=GitHub(repository).raw
        evidence=verify_log_evidence(store,origin,locale,row['snapshot'],adoption,repository,api,raw)
        if not capture:return None
        identity=record(store,origin,locale,row['snapshot'],adoption['producer'],evidence=evidence)
        immutable(store,adoption_key(store,origin,locale),{'completion_sha256':identity})
    value=optional(store,receipt_key(store,identity))
    require(value is not None and digest(stable_bytes(value))==identity
        and set(value)=={'schema_version','policy','generation','locale','origin_sha256','source_sha256',
                         'snapshot','producer','evidence'}
        and value['schema_version']==1 and value['policy']==POLICY
        and value['generation']==origin['generation'] and value['locale']==locale
        and value['origin_sha256']==digest(stable_bytes(origin))
        and value['source_sha256']==origin['source_sha256'],'completion_receipt_binding_invalid')
    evidence=value['evidence']
    require(evidence=={'kind':'native-result'} or (isinstance(evidence,dict)
        and set(evidence)=={'kind','repository','producer','source_job_id','locale_job_id',
                           'source_log_sha256','locale_log_sha256','previous_checkpoint_sha256'}
        and evidence['kind']=='github-log-adoption' and evidence['repository']==repository
        and evidence['producer']==value['producer']),'completion_evidence_invalid')
    source_job,locale_job=completed_jobs(repository,value['producer'],locale,api)
    if evidence['kind']=='github-log-adoption':
        request({key:item for key,item in evidence.items() if key not in {'kind','repository'}})
        require(source_job['id']==evidence['source_job_id'] and locale_job['id']==evidence['locale_job_id'],
                'completion_requested_jobs_differ')
    # Follow verified before/after proofs back to the exact completed snapshot;
    # a receipt for another candidate of the same source is not sufficient.
    current=row
    reachable=[]
    for _ in range(16):
        reachable.append(current.get('snapshot'))
        if current.get('snapshot')==value['snapshot']:break
        repair_id=current.get('source_repair_sha256')
        require(isinstance(repair_id,str) and HEX64.fullmatch(repair_id),'completion_snapshot_lineage_missing')
        from portal_extended_quality_recovery import verify_previous_repair
        verify_previous_repair(store,locale,origin['generation'],current,repository,api)
        from portal_extended_french_repair import read_repair_pipeline
        pipeline=read_repair_pipeline(store,repair_id)
        require(pipeline.locale==locale,'completion_repair_locale_differs')
        proof=pipeline.verify_proof(store,repair_id,origin['generation'])
        expected={**proof['after_row'],'source_repair_sha256':repair_id}
        tail=current.get('source_repair_completion_sha256')
        if tail:
            pipeline.verify_completion(store,tail,proof,repair_id)
            expected['source_repair_completion_sha256']=tail
        require(current==expected,'completion_repair_lineage_differs')
        current=proof['before_row']
    require(current.get('snapshot')==value['snapshot'],'completion_repair_chain_exceeds_bound')
    require(expected_snapshot is None or expected_snapshot in reachable,'completion_requested_snapshot_differs')
    validate_snapshot(store,locale,origin['generation'],{'status':'complete','snapshot':value['snapshot']})
    return identity
