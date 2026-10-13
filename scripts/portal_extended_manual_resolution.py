"""One explicit child attempt; original unknown claims are never reset."""
from __future__ import annotations
import copy
import json
import time

from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import HEX64, R2NotFound, R2TransportError, error_code
from portal_extended_continuation import producer_identity
from build_portal_extended_locales import validate_text, safe_failure_code
from offline_translation import OfflineTranslationValidationError
from portal_extended_repair_contract import MANUAL_STRICT_RETRY

POLICY = 'exact-failed-owner-child-v1'
WORKFLOW = '.github/workflows/portal-extended-locales-r2.yml'
MAX_BYTES = 1024 * 1024


def require(ok, code):
    if not ok: raise ExpansionError(code)


def request(value):
    base = {'policy','claim_sha256','producer','source_job_id','locale_job_id'}
    require(isinstance(value,dict) and set(value) in (base,base|{'completion_sha256'})
        and value.get('policy')==POLICY,'resolution_request_invalid')
    for field in ('claim_sha256','completion_sha256'):
        if field in value: require(isinstance(value[field],str) and HEX64.fullmatch(value[field]),'resolution_identity_invalid')
    producer_identity(value['producer'])
    require(all(type(value[k]) is int and value[k]>0 for k in ('source_job_id','locale_job_id')),
            'resolution_jobs_invalid')
    return value


def normalized(repair):
    value=copy.deepcopy(repair)
    value['resolution_evidence'].pop('completion_sha256',None)
    return value


def key(store, parent, *parts):
    require(isinstance(parent,str) and HEX64.fullmatch(parent),'resolution_parent_invalid')
    return store.key('manual-unit-resolution',parent,*parts)


def read(store, name):
    try: raw=store._get(name,maximum=MAX_BYTES)
    except R2NotFound: return None
    value=json.loads(raw)
    require(isinstance(value,dict) and raw==stable_bytes(value),'resolution_record_not_canonical')
    return value


def require_absent(store,name):
    try: store._get(name,maximum=MAX_BYTES)
    except R2NotFound: return
    raise ExpansionError('resolution_parent_already_resolved')


def immutable(store,name,value):
    """Retry only identical bytes after a typed missing read, never inference."""
    raw=stable_bytes(value)
    require(0<len(raw)<=MAX_BYTES,'resolution_record_oversized')
    for attempt in range(2):
        try:
            store.client.put_object(Bucket=store.bucket,Key=name,Body=raw,ContentType='application/json',
                CacheControl='private, no-store',Metadata={'sha256':digest(raw),'kind':POLICY},IfNoneMatch='*')
        except Exception as error:
            if error_code(error) not in {'preconditionfailed','412','conditionalrequestconflict','409'}:
                existing=read(store,name)
                if existing is None:
                    if attempt==0: continue
                    raise R2TransportError('resolution_write_unresolved') from None
                require(stable_bytes(existing)==raw,'resolution_immutable_conflict')
                return
        require(read(store,name)==value,'resolution_readback_differs')
        return


def jobs(repository,owner,locale,api,*,failed=False):
    owner=producer_identity(owner)
    path=f'repos/{repository}/actions/runs/{owner["run_id"]}/attempts/{owner["attempt"]}'
    run=api(path); inventory=api(path+'/jobs?per_page=100')
    require(run.get('id')==int(owner['run_id']) and run.get('run_attempt')==int(owner['attempt'])
        and run.get('head_sha')==owner['sha'] and run.get('status')=='completed'
        and run.get('conclusion') in ({'failure'} if failed else {'success','failure'})
        and run.get('path')==WORKFLOW and run.get('head_branch')=='main' and run.get('event')=='workflow_dispatch'
        and all((run.get(k) or {}).get('full_name')==repository for k in ('repository','head_repository'))
        and (run.get('repository') or {}).get('private') is False,'resolution_owner_unproved')
    rows=inventory.get('jobs')
    require(type(inventory.get('total_count')) is int and isinstance(rows,list)
        and 0<len(rows)==inventory['total_count']<=100,'resolution_jobs_incomplete')
    found=[]
    for name, conclusion in (('source','success'),(f'locale ({locale})','failure' if failed else 'success')):
        matching=[r for r in rows if r.get('name')==name]
        require(len(matching)==1,'resolution_job_not_unique')
        row=matching[0]
        require(row.get('status')=='completed' and row.get('conclusion')==conclusion
            and row.get('run_id')==int(owner['run_id']) and row.get('head_sha')==owner['sha']
            and type(row.get('id')) is int and row['id']>0,'resolution_job_unproved')
        found.append(row['id'])
    return found


def parent(store,engine,repair,source):
    engine.request(repair)
    require(engine.contract.automatic and repair.get('retry_policy')==MANUAL_STRICT_RETRY
        and len(repair['units'])==1,'resolution_manual_contract_required')
    evidence=request(repair['resolution_evidence']); unit=repair['units'][0]
    claim=engine.read_optional(store,engine.ledger_key(store,unit,'started.json'))
    require(claim is not None and digest(stable_bytes(claim))==evidence['claim_sha256']
        and set(claim)==set(engine.claim_contract(unit,source))|{'producer'}
        and claim['producer']==evidence['producer']
        and {k:claim[k] for k in engine.claim_contract(unit,source)}==engine.claim_contract(unit,source),
        'resolution_original_claim_differs')
    return claim


def result(store,engine,repair,source):
    claim=parent(store,engine,repair,source); identity=digest(stable_bytes(claim))
    started=read(store,key(store,identity,'started.json'))
    accepted=read(store,key(store,identity,'accepted.json'))
    terminal=read(store,key(store,identity,'terminal.json'))
    if started is None:
        require(accepted is None and terminal is None,'resolution_orphan_result')
        return None,None
    expected={'schema_version':1,'policy':POLICY,'parent_claim_sha256':identity,
        'unit_contract':engine.claim_contract(repair['units'][0],source),
        'request_sha256':digest(stable_bytes(normalized(repair)))}
    require(set(started)==set(expected)|{'producer'} and all(started[k]==v for k,v in expected.items()),
        'resolution_child_claim_differs')
    producer_identity(started['producer'])
    if terminal is not None:
        from repair_portal_french_source_fallback import TERMINAL_CODES
        require(set(terminal)=={'schema_version','policy','child_claim_sha256','failure_code'}
            and terminal['schema_version']==1 and terminal['policy']==POLICY
            and terminal['child_claim_sha256']==digest(stable_bytes(started))
            and terminal['failure_code'] in TERMINAL_CODES,'resolution_terminal_binding_invalid')
        require(accepted is None,'resolution_terminal_result_conflict')
        raise ExpansionError('resolution_child_terminal')
    if accepted is None: return started,None
    require(set(accepted)=={'schema_version','policy','child_claim_sha256','parent_claim_sha256','producer','row','row_sha256'}
        and accepted['schema_version']==1 and accepted['policy']==POLICY
        and accepted['parent_claim_sha256']==identity and accepted['child_claim_sha256']==digest(stable_bytes(started))
        and accepted['producer']==started['producer'],'resolution_result_binding_invalid')
    row=accepted['row']
    require(isinstance(row,dict) and set(row)=={'source','language','text'}
        and row['source']==source['source'] and row['language']==source['language']
        and accepted['row_sha256']==digest(stable_bytes(row)),'resolution_result_row_differs')
    validate_text(source['source'],row['text'],engine.locale,source['language'])
    return started,accepted


def preflight(store,engine,repair,source,repository,api):
    claim=parent(store,engine,repair,source)
    evidence=repair['resolution_evidence']
    require(jobs(repository,claim['producer'],engine.locale,api,failed=True)
        ==[evidence['source_job_id'],evidence['locale_job_id']],'resolution_failed_jobs_differ')
    require_absent(store,engine.ledger_key(store,repair['units'][0],'outcome.json'))
    started,accepted=result(store,engine,repair,source)
    require(started is None or accepted is not None,'resolution_child_started_unresolved')
    return accepted is None


def stage(store,engine,repair,source,owner,translator,seconds):
    require(1<=seconds<=900,'resolution_budget_invalid')
    claim=parent(store,engine,repair,source); identity=digest(stable_bytes(claim))
    started,accepted=result(store,engine,repair,source)
    if accepted is not None: return accepted
    require(started is None,'resolution_child_started_unresolved')
    require_absent(store,engine.ledger_key(store,repair['units'][0],'outcome.json'))
    started={'schema_version':1,'policy':POLICY,'parent_claim_sha256':identity,
        'unit_contract':engine.claim_contract(repair['units'][0],source),
        'request_sha256':digest(stable_bytes(normalized(repair))),'producer':producer_identity(owner)}
    # A competing creator cannot inherit permission to infer from an equal record.
    require(engine.create_record(store,key(store,identity,'started.json'),started),'resolution_child_already_claimed')
    setter=getattr(translator,'set_deadline',None)
    if callable(setter): setter(time.monotonic()+seconds)
    try:
        value=translator.cached_translation(source['source'],engine.locale,source['language'],markdown=source['markdown'])
        if value is None:
            value=translator.translate(source['source'],target=engine.locale,source=source['language'],markdown=source['markdown'])
        validate_text(source['source'],value,engine.locale,source['language'])
    except (OfflineTranslationValidationError,ExpansionError) as error:
        immutable(store,key(store,identity,'terminal.json'),{'schema_version':1,'policy':POLICY,
            'child_claim_sha256':digest(stable_bytes(started)),'failure_code':safe_failure_code(error)})
        raise
    row={'source':source['source'],'language':source['language'],'text':value}
    accepted={'schema_version':1,'policy':POLICY,'child_claim_sha256':digest(stable_bytes(started)),
        'parent_claim_sha256':identity,'producer':producer_identity(owner),'row':row,'row_sha256':digest(stable_bytes(row))}
    # Private durable validated bytes precede every candidate/parent-ledger write.
    immutable(store,key(store,identity,'accepted.json'),accepted)
    return result(store,engine,repair,source)[1]


def complete(store,engine,repair,source,owner):
    started,accepted=result(store,engine,repair,source)
    require(accepted is not None,'resolution_accepted_result_missing')
    value={'schema_version':1,'policy':POLICY,'parent_claim_sha256':accepted['parent_claim_sha256'],
        'accepted_sha256':digest(stable_bytes(accepted)),'request_sha256':digest(stable_bytes(normalized(repair))),
        'producer':producer_identity(owner)}
    identity=digest(stable_bytes(value))
    immutable(store,key(store,value['parent_claim_sha256'],'completions',identity+'.json'),value)
    return identity


def completion_binding(store,engine,repair,accepted,identity):
    parent_id=repair['resolution_evidence']['claim_sha256']
    completion=read(store,key(store,parent_id,'completions',identity+'.json'))
    require(completion is not None and digest(stable_bytes(completion))==identity
        and set(completion)=={'schema_version','policy','parent_claim_sha256','accepted_sha256','request_sha256','producer'}
        and completion['schema_version']==1 and completion['policy']==POLICY
        and completion['parent_claim_sha256']==parent_id
        and completion['accepted_sha256']==digest(stable_bytes(accepted))
        and completion['request_sha256']==digest(stable_bytes(normalized(repair))),
        'resolution_completion_binding_invalid')
    producer_identity(completion['producer'])
    from portal_extended_french_repair import RepairPipeline
    pipeline=RepairPipeline(engine.contract)
    for owner in (accepted['producer'],completion['producer']):
        source_claim=pipeline.read_optional(store,pipeline.claim_key(store,normalized(repair),owner))
        require(source_claim is not None and source_claim.get('request')==normalized(repair)
            and source_claim.get('producer')==owner
            and source_claim.get('before_row',{}).get('status')=='complete'
            and all(source_claim['before_row']['snapshot'][k]==repair[k] for k in
                ('checkpoint_sha256','candidate_id','manifest_sha256')),'resolution_source_claim_missing')
    return completion


def verify_admission(store,engine,unit,source,claim,identity):
    require(isinstance(identity,str) and HEX64.fullmatch(identity),'resolution_admission_identity_invalid')
    parent_id=digest(stable_bytes(claim))
    record=read(store,key(store,parent_id,'admissions',identity+'.json'))
    require(record is not None and digest(stable_bytes(record))==identity
        and set(record)=={'schema_version','policy','request','completion_sha256','jobs','row_sha256'}
        and record['schema_version']==1 and record['policy']==POLICY,'resolution_admission_invalid')
    repair=engine.request(record['request'])
    require(repair['units']==[unit] and repair['resolution_evidence']['claim_sha256']==parent_id,
        'resolution_admission_unit_differs')
    require(record['completion_sha256']==repair['resolution_evidence'].get('completion_sha256'),
            'resolution_admission_completion_differs')
    _,accepted=result(store,engine,repair,source)
    require(accepted is not None and accepted['row_sha256']==record['row_sha256'],'resolution_admission_row_differs')
    completion=completion_binding(store,engine,repair,accepted,record['completion_sha256'])
    require(isinstance(record['jobs'],list) and len(record['jobs'])==2
        and all(type(v) is int and v>0 for v in record['jobs']),'resolution_completion_jobs_invalid')
    return accepted,completion,record


def adopt(store,engine,repair,source,repository,api):
    claim=parent(store,engine,repair,source); parent_id=digest(stable_bytes(claim))
    identity=repair['resolution_evidence'].get('completion_sha256')
    require(identity is not None,'resolution_completion_required')
    _,accepted=result(store,engine,repair,source)
    require(accepted is not None,'resolution_accepted_result_missing')
    completion=completion_binding(store,engine,repair,accepted,identity)
    evidence=repair['resolution_evidence']
    require(jobs(repository,claim['producer'],engine.locale,api,failed=True)
        ==[evidence['source_job_id'],evidence['locale_job_id']],'resolution_failed_jobs_differ')
    verified_jobs=jobs(repository,completion['producer'],engine.locale,api)
    admission={'schema_version':1,'policy':POLICY,'request':repair,'completion_sha256':identity,
        'jobs':verified_jobs,'row_sha256':accepted['row_sha256']}
    admission_id=digest(stable_bytes(admission))
    immutable(store,key(store,parent_id,'admissions',admission_id+'.json'),admission)
    verify_admission(store,engine,repair['units'][0],source,claim,admission_id)
    outcome={'schema_version':1,'policy':engine.policy,'validator_revision':engine.revision,
        'unit_sha256':repair['units'][0],'claim_sha256':parent_id,'status':'accepted',
        'row':accepted['row'],'mode':'accepted-ledger','manual_resolution_sha256':admission_id}
    immutable(store,engine.ledger_key(store,repair['units'][0],'outcome.json'),outcome)
    return engine.ledger_outcome(store,repair['units'][0],source)
