"""Explicit repair of exact rejected legacy units in the serialized CPU queue."""
from __future__ import annotations
import argparse
import copy
import json
import os
from pathlib import Path
import re

from build_portal_extended_locales import (CHECKPOINT_VERSION, SOURCE_FALLBACK_VERSION,
    build, translate_document, validate_text)
from financial_quantity_integrity import NUMBER
from offline_translation import MODEL_ID, OfflineTranslationValidationError
from portal_extended_continuation import (checkpoint_evidence, producer_identity, queue,
    read_origin, record_result, register, verify_origin_run)
from portal_extended_daily_queue import immutable_record, write_verified
from portal_extended_locales import ExpansionError, daily_corpus_day, digest, stable_bytes
from portal_extended_r2 import (DEFAULT_PREFIX, HEX64, MAX_CHECKPOINT_BYTES,
    MAX_CANDIDATE_PAGE_BYTES, R2NotFound, R2Store, R2TransportError, checkpoint_is_valid, require_env)
from portal_extended_recovery_intent import (acknowledged, key, read_index, read_receipt,
    source, POLICY as INTENT_POLICY)

POLICY = 'explicit-rejected-legacy-unit-repair-v1'
WORKFLOW = '.github/workflows/portal-extended-locales-r2.yml'
BP = re.compile(rf'({NUMBER})\s*(?:个基点|個基點|基点|基點|basis\s+points?|bps?\b)', re.I)


def once_store():
    import boto3
    from botocore.config import Config
    client = boto3.client('s3', endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
        region_name='auto', config=Config(retries={'total_max_attempts': 1, 'mode': 'standard'},
                                        connect_timeout=10, read_timeout=30))
    return R2Store(client, require_env('R2_BUCKET'), DEFAULT_PREFIX)


def request(value):
    if (not isinstance(value, dict) or set(value) != {'intent', 'units'}
        or not isinstance(value['intent'], str) or not HEX64.fullmatch(value['intent'])
        or not isinstance(value['units'], list) or not 1 <= len(value['units']) <= 20
        or any(not isinstance(v, str) or not HEX64.fullmatch(v) for v in value['units'])
        or value['units'] != sorted(set(value['units']))):
        raise ExpansionError('Invalid exact rejected-unit repair request')
    return value


def unit_key(locale, row, markdown=False):
    return digest(stable_bytes([CHECKPOINT_VERSION, MODEL_ID, locale, row['language'], row['source']] +
                              (['markdown'] if markdown else [])))


def required_units(corpus,locale):
    required=set()
    class Collect:
        def get(self,text,language='zh',*,markdown=False):
            required.add(unit_key(locale,{'source':text,'language':language},markdown));return text
    for doc in corpus['documents']:translate_document(doc,Collect())
    return required


def validate_units(value, locale, generation):
    checkpoint_is_valid(value, locale, generation)
    if value.get('source_generation') != generation or not isinstance(value.get('source_fallbacks', {}), dict):
        raise ExpansionError('Repair checkpoint lacks exact source generation')
    bad = []
    for kind in ('rows', 'source_fallbacks'):
        for identity, row in value.get(kind, {}).items():
            if (not isinstance(row, dict) or not isinstance(row.get('source'), str)
                or not isinstance(row.get('language'), str) or identity not in
                {unit_key(locale, row), unit_key(locale, row, True)}):
                raise ExpansionError('Repair checkpoint unit differs from exact source')
            if kind == 'source_fallbacks':
                if row.get('policy') != SOURCE_FALLBACK_VERSION or not isinstance(row.get('code'), str):
                    raise ExpansionError('Repair source fallback policy differs')
                continue
            try:
                validate_text(row['source'], row.get('text'), locale, row['language'])
            except ExpansionError as error:
                if str(error) != 'Financial quantity validation failed' or not BP.search(row['source']):
                    raise ExpansionError('Repair may only replace rejected basis-point units') from None
                bad.append(identity)
    return sorted(bad)


def load(store, generation, locale, repair, repository, api, *, allow_ack=False):
    repair = request(repair)
    entries = [row for row in read_index(store) if row == {'intent': repair['intent'], 'generation': generation}]
    if len(entries) != 1 or (acknowledged(store, repair['intent']) and not allow_ack):
        raise ExpansionError('Repair requires an unconsumed exact registered legacy intent')
    value = read_receipt(store, entries[0]); corpus = source(store, value)
    if set(value['evidence']['locales']) != {locale}:
        raise ExpansionError('Repair is limited to the exact single legacy locale')
    producer = producer_identity(value['evidence']['producer'])
    path = f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
    jobs = api(path+'/jobs?per_page=100')
    if type(jobs.get('total_count')) is not int or jobs['total_count'] > 100 or len(jobs.get('jobs', [])) != jobs['total_count']:
        raise ExpansionError('Repair original job inventory is incomplete')
    verify_origin_run({'producer': producer, 'source_day': daily_corpus_day(corpus)}, api(path), jobs['jobs'], repository)
    locale_jobs = [j for j in jobs['jobs'] if j.get('name') == f'locale ({locale})']
    if len(locale_jobs) != 1 or locale_jobs[0].get('status') != 'completed' or locale_jobs[0].get('conclusion') not in {'success','failure'}:
        raise ExpansionError('Repair original locale producer is unproved')
    proof = value['evidence']['locales'][locale]
    from inspect_portal_extended_continuation import inspect
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        output = Path(tmp)/'frozen'
        summary = inspect(store, generation, locale, proof['checkpoint_sha256'], proof['candidate_id'], output)
        old = json.loads((output/'checkpoint.json').read_bytes())
        manifest = json.loads((output/'candidate-manifest.json').read_bytes())
    if (summary['manifest_sha256'] != proof['manifest_sha256'] or summary['status'] != 'incomplete-candidate'
        or summary['budget_exhausted'] is not True or summary['failure_count'] != 0):
        raise ExpansionError('Repair original candidate is not a checkpointed budget result')
    docs = {d['url']: d for d in corpus['documents']}
    from portal_extended_locales import file_for_url
    for row in manifest['pages']:
        doc = docs[row['source_url']]
        if (row['path'] != (Path(locale)/file_for_url(doc['url'])).as_posix()
            or row.get('source_content_sha256') != doc['content_sha256']
            or row.get('source_html_sha256') != doc['source_html_sha256']):
            raise ExpansionError('Repair frozen page source descriptors differ')
        raw = store._get(store.candidate_key(locale, generation, proof['candidate_id'], row['path']), maximum=MAX_CANDIDATE_PAGE_BYTES)
        if len(raw) != row['bytes'] or digest(raw) != row['sha256']:
            raise ExpansionError('Repair frozen page bytes differ')
    rejected=validate_units(old, locale, generation)
    if rejected != repair['units']:
        print(json.dumps({'status':'rejected-unit-set-differs','failed_unit_count':len(rejected),
                          'failed_unit_sha256':rejected[:20],'maximum_reported_units':20},sort_keys=True))
        raise ExpansionError('Repair requested units differ from current rejected units')
    if not set(repair['units']) <= required_units(corpus,locale):
        raise ExpansionError('Repair requested unit is absent from frozen source documents')
    return value, corpus, old


def claim_key(store, repair):
    return key(store, repair['intent'], 'repair-'+digest(stable_bytes(repair))+'.json')


def repair_key(store, repair, *parts):
    return key(store, repair['intent'], 'repair', digest(stable_bytes(repair)), *parts)


def read_optional(store, name):
    try:raw=store._get(name,maximum=65536)
    except R2NotFound:return None
    value=json.loads(raw)
    if raw!=stable_bytes(value):raise ExpansionError('Repair metadata is not canonical')
    return value


def attempts(store, repair):
    value=read_optional(store,repair_key(store,repair,'attempts.json'))
    if value is None:return []
    if (set(value)!={'schema_version','policy','request','producers'} or type(value['schema_version']) is not int
        or value['schema_version']!=1 or value['policy']!=POLICY or value['request']!=repair
        or not isinstance(value['producers'],list) or not 1<=len(value['producers'])<=3):
        raise ExpansionError('Repair attempt ledger is invalid')
    producers=[producer_identity(p) for p in value['producers']]
    if len({digest(stable_bytes(p)) for p in producers})!=len(producers):raise ExpansionError('Repair attempt ledger repeats an attempt')
    return producers


def prepare(store, generation, locale, repair, repository, api, owner):
    prepared=read_optional(store,repair_key(store,repair,'prepared.json'))
    value, corpus, old = load(store, generation, locale, repair, repository, api,allow_ack=prepared is not None)
    if prepared is not None:
        resume_prepared(store,value,corpus,old,repair,locale,prepared)
        return {'has_work':False,'generation':generation,'locales_json':'[]','locale_jobs_json':'[]',
                'day':daily_corpus_day(corpus),'requested_locales':locale,'source_admission':'',
                'english_admission':'','stopped_locales_json':'[]','resumed_prepared_without_cpu':True}
    if read_origin(store, generation) is not None or generation in queue(store, locale):
        raise ExpansionError('Repair cannot reset registered or advanced generation')
    claim = {'schema_version':1,'policy':POLICY,'request':repair,'generation':generation,
             'locale':locale,'source_sha256':value['source_sha256'],'producer':producer_identity(owner)}
    existing=read_optional(store,claim_key(store,repair))
    if existing is None:
        immutable_record(store, claim_key(store, repair), claim, kind='legacy-unit-repair-claim')
    elif {k:v for k,v in existing.items() if k!='producer'}!={k:v for k,v in claim.items() if k!='producer'}:
        raise ExpansionError('Repair claim differs from exact frozen request')
    producers=attempts(store,repair)
    current=producer_identity(owner)
    if not producers or producers[-1]!=current:
        if len(producers)>=3:raise ExpansionError('Repair attempt bound reached without resetting original continuation')
        if producers:
            previous=producers[-1]
            prior=api(f'repos/{repository}/actions/runs/{previous["run_id"]}/attempts/{previous["attempt"]}')
            if (prior.get('id')!=int(previous['run_id']) or prior.get('run_attempt')!=int(previous['attempt'])
                or prior.get('head_sha')!=previous['sha'] or prior.get('status')!='completed'
                or prior.get('path')!=WORKFLOW or prior.get('head_branch')!='main'
                or prior.get('event')!='workflow_dispatch'
                or any((prior.get(k)or{}).get('full_name')!=repository for k in ('repository','head_repository'))):
                raise ExpansionError('Previous repair attempt is not a completed exact main producer')
        producers.append(current)
        write_verified(store,repair_key(store,repair,'attempts.json'),
            {'schema_version':1,'policy':POLICY,'request':repair,'producers':producers},kind='legacy-unit-repair-attempts')
    return {'has_work':True,'generation':generation,'locales_json':json.dumps([locale]),
            'locale_jobs_json':json.dumps([{'locale':locale,'generation':generation,'day':daily_corpus_day(corpus)}]),
            'day':daily_corpus_day(corpus),'requested_locales':locale,'source_admission':'',
            'english_admission':'','selected_page_count':len(corpus['documents']),'stopped_locales_json':'[]'}


def check_claim(store, generation, locale, repair, owner):
    raw = store._get(claim_key(store, repair), maximum=65536); value = json.loads(raw)
    if (raw != stable_bytes(value) or value.get('schema_version') != 1 or value.get('policy') != POLICY
        or value.get('request') != repair or value.get('generation') != generation or value.get('locale') != locale
        or not attempts(store,repair) or attempts(store,repair)[-1]!=producer_identity(owner)):
        raise ExpansionError('Repair requires the exact serialized source-job claim')
    return value


def preserve(old, new, locale, generation, units, *, allowed_new_units=None):
    if validate_units(new, locale, generation): raise ExpansionError('Repaired checkpoint still fails its financial gate')
    extra=(set(new['rows'])|set(new.get('source_fallbacks',{})))-(set(old['rows'])|set(old.get('source_fallbacks',{})))
    if allowed_new_units is not None and not extra<=allowed_new_units:
        raise ExpansionError('Repair added a unit outside the frozen source corpus')
    unaffected = {k:v for k,v in old['rows'].items() if k not in units}
    if (any(new['rows'].get(k) != v for k,v in unaffected.items())
        or any(new.get('source_fallbacks',{}).get(k) != v for k,v in old.get('source_fallbacks',{}).items())
        or any(k not in new['rows'] or k in new.get('source_fallbacks',{}) for k in units)):
        raise ExpansionError('Repair changed preserved cache or replaced rejected units with source fallback')
    changed = [{'unit_sha256':k,'source_sha256':digest(old['rows'][k]['source'].encode()),
                'previous_translated_sha256':digest(old['rows'][k]['text'].encode()),
                'translated_sha256':digest(new['rows'][k]['text'].encode())} for k in units]
    if any(new['rows'][k]['source'] != old['rows'][k]['source'] or new['rows'][k]['language'] != old['rows'][k]['language'] for k in units):
        raise ExpansionError('Repair changed the source identity')
    return {'repaired_units':changed,'unchanged_translation_rows':len(unaffected),
            'unchanged_rows_sha256':digest(stable_bytes(unaffected)),
            'unchanged_source_fallback_rows':len(old.get('source_fallbacks',{})),
            'unchanged_source_fallbacks_sha256':digest(stable_bytes(old.get('source_fallbacks',{})))}


class TargetedRepairError(RuntimeError):
    pass


class ProtectedBasisPointTranslator:
    def __init__(self, base, sources): self.base, self.sources = base, sources
    def set_deadline(self, value):
        method = getattr(self.base, 'set_deadline', None)
        if callable(method): method(value)
    def translate(self, text, *, target, source, markdown=True):
        if text not in self.sources: return self.base.translate(text,target=target,source=source,markdown=markdown)
        terms = {}
        def protect(match):
            token = f'__HYMTPH_{9000+len(terms):04d}__'; terms[token] = match[1]+' bps'; return token
        masked = BP.sub(protect, text)
        if not terms or len(terms)>64: raise ExpansionError('Repair basis-point protection is outside its bound')
        try:
            translated = self.base.translate(masked,target=target,source=source,markdown=markdown)
            for token, value in terms.items():
                if translated.count(token)!=1: raise ExpansionError('Repair changed protected basis-point placeholder')
                translated = translated.replace(token,value)
            validate_text(text, translated, target, source)
            return translated
        except (ExpansionError, OfflineTranslationValidationError):
            # A selected failed row must become a validated translation. It
            # cannot be silently converted into the ordinary source fallback.
            raise TargetedRepairError('Targeted basis-point repair failed its original quality gate') from None


class PrivateUnitTranslator:
    """Persist each validated new unit before returning it to the local memo."""
    def __init__(self,base,store,repair,generation,locale,owner):
        self.base,self.store,self.repair,self.generation,self.locale,self.owner=base,store,repair,generation,locale,owner
        self.cache_hits=0
    def set_deadline(self,value):self.base.set_deadline(value)
    def translate(self,text,*,target,source,markdown=True):
        identity=unit_key(target,{'source':text,'language':source},markdown)
        name=repair_key(self.store,self.repair,'units',identity+'.json')
        value=read_optional(self.store,name)
        if value is not None:
            if (set(value)!={'schema_version','policy','request_sha256','generation','locale','unit_sha256','markdown','producer','row'}
                or type(value['schema_version'])is not int or value['schema_version']!=1 or value['policy']!=POLICY
                or value['request_sha256']!=digest(stable_bytes(self.repair)) or value['generation']!=self.generation
                or value['locale']!=target or value['unit_sha256']!=identity or value['markdown']is not markdown
                or value['row'].get('source')!=text or value['row'].get('language')!=source
                or producer_identity(value['producer']) not in attempts(self.store,self.repair)):
                raise ExpansionError('Private repaired unit differs from exact source identity')
            validate_text(text,value['row']['text'],target,source)
            self.cache_hits+=1;return value['row']['text']
        translated=self.base.translate(text,target=target,source=source,markdown=markdown)
        validate_text(text,translated,target,source)
        value={'schema_version':1,'policy':POLICY,'request_sha256':digest(stable_bytes(self.repair)),
               'generation':self.generation,'locale':target,'unit_sha256':identity,'markdown':markdown,
               'producer':self.owner,'row':{'source':text,'language':source,'text':translated}}
        immutable_record(self.store,name,value,kind='validated-private-repaired-unit')
        return translated


def commit_prepared(store,value,corpus,locale,prepared):
    generation=corpus['documents_sha256'];repair=prepared['request']
    original=value['evidence']['producer']
    origin=read_origin(store,generation);current=queue(store,locale).get(generation)
    if origin is not None and (origin['producer']!=original or origin['source_sha256']!=value['source_sha256']
                              or origin['locales']!=[locale]):
        raise ExpansionError('Prepared repair cannot replace generation ownership')
    if current is not None and (current['continuations']!=0 or current['status'] not in {'started','complete'}
        or current['status']=='started' and current.get('owner')!=original):
        raise ExpansionError('Prepared repair cannot reset advanced continuation')
    if origin is None:
        if current is not None:raise ExpansionError('Prepared repair found unowned continuation')
        register(store,corpus,(locale,),original)
    elif current is None:
        if acknowledged(store,repair['intent']):raise ExpansionError('Prepared repair cannot recreate a dropped generation')
        # The immutable prepared identity preceded origin registration; an
        # unacknowledged missing row proves only that its initial write stopped.
        register(store,corpus,(locale,),original)
    result={k:prepared[k] for k in ('candidate_id','manifest_sha256')}
    if current is None or current['status']=='started':
        record_result(store,locale,corpus,result,checkpoint_sha=prepared['checkpoint_sha256'],owner=original)
    else:
        expected={'checkpoint_sha256':prepared['checkpoint_sha256'],'candidate_id':prepared['candidate_id'],
                  'manifest_sha256':prepared['manifest_sha256'],'completed_pages':len(corpus['documents']),
                  'resolved_units':len(checkpoint_evidence(store,locale,generation,prepared['checkpoint_sha256']))}
        if current['snapshot']!=expected:raise ExpansionError('Prepared repair completed snapshot differs')
    from portal_extended_incremental import content_key,read_state,write_state
    day=daily_corpus_day(corpus);pages=read_state(store,'completed',locale,day).get('pages',{})
    if not isinstance(pages,dict):raise ExpansionError('Repair completed-page receipt is invalid')
    for doc in corpus['documents']:
        pages[doc['url']]={'content_key':content_key(doc),'generation':generation,'candidate_id':prepared['candidate_id']}
    write_state(store,'completed',locale,{'pages':pages},day)
    immutable_record(store,key(store,repair['intent'],'ack.json'),
        {'schema_version':1,'policy':INTENT_POLICY,'intent':repair['intent'],'status':'adopted'},kind='legacy-recovery-intent-ack')


def resume_prepared(store,value,corpus,old,repair,locale,prepared):
    generation=corpus['documents_sha256']
    if (prepared.get('policy')!=POLICY or prepared.get('request')!=repair or prepared.get('generation')!=generation
        or prepared.get('locale')!=locale or prepared.get('source_sha256')!=value['source_sha256']
        or prepared.get('original_producer')!=value['evidence']['producer']
        or producer_identity(prepared.get('producer')) not in attempts(store,repair)):
        raise ExpansionError('Prepared repair identity differs')
    raw=store._get(store.checkpoint_object_key(locale,generation,prepared['checkpoint_sha256']),maximum=MAX_CHECKPOINT_BYTES)
    if digest(raw)!=prepared['checkpoint_sha256']:raise ExpansionError('Prepared repair checkpoint bytes differ')
    evidence=preserve(old,json.loads(raw),locale,generation,repair['units'],allowed_new_units=required_units(corpus,locale))
    if any(prepared.get(k)!=v for k,v in evidence.items()):raise ExpansionError('Prepared repair preserved-row evidence differs')
    checkpoint_evidence(store,locale,generation,prepared['checkpoint_sha256'])
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        destination=Path(tmp)/'candidate';store.restore_candidate(locale,generation,prepared['candidate_id'],destination)
        from assemble_portal_extended_locales import verified_candidate
        verified_candidate(destination,corpus)
        if digest((destination/'candidate-manifest.json').read_bytes())!=prepared['manifest_sha256']:
            raise ExpansionError('Prepared repair manifest bytes differ')
    commit_prepared(store,value,corpus,locale,prepared)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['prepare','restore','build','persist'])
    parser.add_argument('--generation',required=True);parser.add_argument('--locale',required=True)
    parser.add_argument('--request',required=True);parser.add_argument('--corpus',type=Path)
    parser.add_argument('--checkpoint',type=Path);parser.add_argument('--output',type=Path)
    parser.add_argument('--github-output',type=Path);parser.add_argument('--seconds',type=int,default=14400)
    args=parser.parse_args()
    from build_portal_extended_locales import validate_budget
    validate_budget(args.seconds)
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REF')!='refs/heads/main'
        or os.environ.get('GITHUB_EVENT_NAME')!='workflow_dispatch' or os.environ.get('KC_PUBLIC_REPOSITORY')!='true'
        or os.environ.get('GITHUB_WORKFLOW_REF')!=os.environ.get('GITHUB_REPOSITORY','')+'/'+WORKFLOW+'@refs/heads/main'):
        raise ExpansionError('Exact checkpoint repair requires reviewed-main public dispatch')
    owner=producer_identity({k:os.environ[v] for k,v in {'run_id':'GITHUB_RUN_ID','attempt':'GITHUB_RUN_ATTEMPT','sha':'GITHUB_SHA'}.items()})
    repair=request(json.loads(args.request));store=once_store()
    from review_portal_extended_handoff import api
    repository=os.environ['GITHUB_REPOSITORY']
    if args.operation=='prepare':
        result=prepare(store,args.generation,args.locale,repair,repository,api,owner)
        if args.github_output:
            with args.github_output.open('a') as file:
                for k,v in result.items():file.write(f'{k}={str(v).lower() if isinstance(v,bool) else v}\n')
        print(json.dumps(result,sort_keys=True));return 0
    check_claim(store,args.generation,args.locale,repair,owner)
    value,corpus,old=load(store,args.generation,args.locale,repair,repository,api)
    if args.operation=='restore':
        cloned=copy.deepcopy(old)
        for identity in repair['units']:del cloned['rows'][identity]
        args.checkpoint.write_bytes(stable_bytes(cloned))
        args.corpus.write_bytes(stable_bytes(corpus))
        print(json.dumps({'present':True,'removed_rejected_units':len(repair['units']),'unchanged_rows':len(cloned['rows'])}));return 0
    if args.operation=='build':
        from offline_translation import OfflineTranslator
        translator=OfflineTranslator()
        protected=ProtectedBasisPointTranslator(translator,{old['rows'][k]['source'] for k in repair['units']})
        wrapped=PrivateUnitTranslator(protected,store,repair,args.generation,args.locale,owner)
        result=build(corpus,args.locale,args.output,args.checkpoint,wrapped,budget_seconds=args.seconds,allow_source_fallback=True)
        result['repair_private_unit_cache_hits']=wrapped.cache_hits
        result['free_cpu_translation_fragments']=translator.stats['batch_requests']
        (args.output/'candidate-manifest.json').write_bytes(stable_bytes(result))
        print(json.dumps({k:result[k] for k in ('status','source_document_count','completed_page_count',
            'translation_calls_this_run','cache_hits','paid_provider_requests','budget_exhausted','failures',
            'repair_private_unit_cache_hits','free_cpu_translation_fragments')},sort_keys=True))
        return 0 if result['status']=='complete-candidate' else 75
    if args.checkpoint.stat().st_size>MAX_CHECKPOINT_BYTES:raise ExpansionError('Repair checkpoint exceeds bound')
    new=json.loads(args.checkpoint.read_bytes());evidence=preserve(old,new,args.locale,args.generation,repair['units'],
                                                               allowed_new_units=required_units(corpus,args.locale))
    from assemble_portal_extended_locales import verified_candidate
    verified_candidate(args.output,corpus)
    manifest=json.loads((args.output/'candidate-manifest.json').read_bytes())
    if (manifest['status']!='complete-candidate' or manifest['failures'] or manifest['budget_exhausted']
        or manifest['completed_page_count']!=len(corpus['documents']) or manifest['paid_provider_requests']!=0):
        raise ExpansionError('Repair requires a complete zero-paid quality-gated result')
    if read_origin(store,args.generation) is not None or args.generation in queue(store,args.locale):
        raise ExpansionError('Repair cannot replace a registered or advanced generation')
    checkpoint=store.put_checkpoint(args.locale,args.generation,args.checkpoint)
    result=store.upload_candidate(args.output,args.locale,args.generation)
    if result['status']!='complete-candidate':raise ExpansionError('Repair candidate is incomplete')
    checkpoint_evidence(store,args.locale,args.generation,checkpoint['sha256'])
    summary={'schema_version':1,'policy':POLICY,'generation':args.generation,'locale':args.locale,'intent':repair['intent'],
             'producer':owner,'original_producer':value['evidence']['producer'],'source_sha256':value['source_sha256'],
             'request':repair,'checkpoint_sha256':checkpoint['sha256'],'candidate_id':result['candidate_id'],
             'manifest_sha256':result['manifest_sha256'],'paid_provider_requests':0,
             'translation_calls_this_run':manifest['translation_calls_this_run'],'cache_hits':manifest['cache_hits'],
             'repair_private_unit_cache_hits':manifest.get('repair_private_unit_cache_hits',0),
             'free_cpu_translation_fragments':manifest.get('free_cpu_translation_fragments',0),**evidence}
    immutable_record(store,key(store,repair['intent'],'repair-result-'+digest(stable_bytes(summary))+'.json'),summary,kind='legacy-unit-repair-result')
    immutable_record(store,repair_key(store,repair,'prepared.json'),summary,kind='legacy-unit-repair-prepared')
    commit_prepared(store,value,corpus,args.locale,summary)
    print(json.dumps(summary,sort_keys=True));return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except R2TransportError:
        print(json.dumps({'status':'rejected','code':'exact-checkpoint-repair-remote-stop','remote_stop':True}));raise SystemExit(1) from None
    except Exception:
        print(json.dumps({'status':'rejected','code':'exact-checkpoint-repair-failed'}));raise SystemExit(1) from None
