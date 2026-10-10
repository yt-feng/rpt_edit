"""French fallback repair: real cache/render contracts, synthetic model and R2 only."""
from __future__ import annotations
import copy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import repair_portal_french_source_fallback as repair
from build_portal_extended_locales import build, SOURCE_FALLBACK_VERSION, public_translation_diagnostics
from hymt_offline_translation import quantity_failure_diagnostics
from offline_translation import OfflineTranslationValidationError
from portal_extended_locales import document_from_html, make_corpus, stable_bytes, digest, ExpansionError
from portal_extended_r2 import R2Store, R2TransportError
from test_portal_extended_locales import FakeTranslator, HOME, BLOG, html
from test_portal_extended_r2 import FakeR2

OWNER = {'run_id': '2', 'attempt': '1', 'sha': 'b' * 40}
OTHER_OWNER = {'run_id': '3', 'attempt': '1', 'sha': 'c' * 40}


class Precondition(Exception):
    response = {'Error': {'Code': 'PreconditionFailed'}}


class AtomicR2(FakeR2):
    def __init__(self):
        super().__init__()
        self.writes = 0
        self.lose_ack = None
        self.race = False

    def put_object(self, *, IfNoneMatch=None, **kwargs):
        assert IfNoneMatch == '*'
        if kwargs['Key'] in self.objects or self.race:
            raise Precondition()
        super().put_object(**kwargs)
        self.writes += 1
        if self.lose_ack and kwargs['Key'].endswith(self.lose_ack):
            raise TimeoutError('synthetic PRIVATE transport body')


class OriginalRejected(FakeTranslator):
    def translate(self, text, target, source=None, *, markdown=True):
        if 'USD' in text:
            self.calls += 1
            raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed')
        return super().translate(text, target, source, markdown=markdown)


class RepairTranslator:
    def __init__(self, terminal=None, crash=None, unchanged=False):
        self.calls = []
        self.terminal, self.crash, self.unchanged = terminal, crash, unchanged

    def translate(self, text, target, source=None, *, markdown=True):
        self.calls.append((text, target, source, markdown))
        if self.crash and self.crash in text:
            raise TimeoutError('PRIVATE unknown outcome')
        if self.terminal and self.terminal in text:
            raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed PRIVATE')
        if self.unchanged: return text
        return text.replace('Revenue', 'Chiffre d’affaires').replace('Profit', 'Bénéfice')


class RepairTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.corpus = make_corpus([document_from_html(url, html(url, body=
            '<h1>Public research</h1><p>Revenue USD10m.</p><p>Profit USD2m.</p><p>Further research.</p>'))
            for url in (HOME, BLOG)])
        self.oldcandidate = self.root / 'old'
        self.oldcheckpoint = self.root / 'old.json'
        self.manifest = build(self.corpus, 'fr', self.oldcandidate, self.oldcheckpoint,
                              OriginalRejected(), allow_source_fallback=True, budget_seconds=30)
        self.oldraw = self.oldcheckpoint.read_bytes()
        self.old = json.loads(self.oldraw)
        self.units = sorted(self.old['source_fallbacks'])
        self.request = {'policy': repair.POLICY, 'validator_revision': repair.REVISION,
            'source_sha256': digest(stable_bytes(self.corpus)), 'origin_sha256': 'd' * 64,
            'producer': {'run_id': '1', 'attempt': '1', 'sha': 'a' * 40},
            'checkpoint_sha256': digest(self.oldraw), 'candidate_id': self.manifest['files_sha256'],
            'manifest_sha256': digest((self.oldcandidate / 'candidate-manifest.json').read_bytes()),
            'units': self.units}
        self.client = AtomicR2()
        self.store = R2Store(self.client, 'private-bucket', '_extended-locales/staging/test')

    def rebuild(self, translator, *, name='new', request=None, raw=None, owner=OWNER):
        return repair.rebuild(self.store, self.corpus, self.oldraw if raw is None else raw,
            self.oldcandidate, self.root/name, self.root/(name+'.json'), request or self.request,
            owner, translator, seconds=30)

    def refresh_checkpoint(self, value):
        self.old = value
        self.oldraw = stable_bytes(value)
        self.oldcheckpoint.write_bytes(self.oldraw)
        self.request['checkpoint_sha256'] = digest(self.oldraw)

    def refresh_candidate_pins(self):
        manifest_path = self.oldcandidate / 'candidate-manifest.json'
        value = json.loads(manifest_path.read_bytes())
        for row in value['pages']:
            raw = (self.oldcandidate / row['path']).read_bytes()
            row['sha256'], row['bytes'] = digest(raw), len(raw)
        value['files_sha256'] = digest(stable_bytes(value['pages']))
        manifest_path.write_bytes(stable_bytes(value))
        self.request['candidate_id'] = value['files_sha256']
        self.request['manifest_sha256'] = digest(manifest_path.read_bytes())

    def assert_no_effect(self, translator):
        self.assertEqual(translator.calls, [])
        self.assertEqual(self.client.writes, 0)

    def test_inspector_emits_exact_eligible_hashes_only(self):
        req = {**self.request, 'units': []}
        result = repair.inspect_frozen(self.corpus, self.oldraw, self.oldcandidate, req)
        self.assertEqual(result['eligible_units'], self.units)
        self.assertEqual((result['page_count'], result['fallback_count'], result['model_calls'], result['storage_writes']), (2, 2, 0, 0))
        for word in ('Revenue', 'Profit', 'USD', '10000000', '2000000'):
            self.assertNotIn(word, json.dumps(result))
        self.assertEqual(self.client.writes, 0)

    def test_strict_request_rejects_widening_before_model(self):
        variants = [dict(self.request, policy='legacy'), dict(self.request, validator_revision='new'),
                    dict(self.request, units=[]), dict(self.request, units=self.units[::-1]),
                    dict(self.request, units=[self.units[0]]*2), dict(self.request, locale='de'),
                    dict(self.request, units=sorted(f'{n:064x}' for n in range(21))),
                    dict(self.request, units=['f'*64])]
        for req in variants:
            translator = RepairTranslator()
            with self.subTest(req=list(req)), self.assertRaises(Exception): self.rebuild(translator, request=req)
            self.assert_no_effect(translator)

    def test_all_frozen_identities_required_before_model(self):
        for field in ('source_sha256', 'checkpoint_sha256', 'manifest_sha256', 'candidate_id'):
            translator = RepairTranslator()
            with self.subTest(field=field), self.assertRaises(Exception):
                self.rebuild(translator, request={**self.request, field:'e'*64})
            self.assert_no_effect(translator)

    def test_required_unselected_cache_miss_is_preflight_failure(self):
        value = copy.deepcopy(self.old)
        del value['rows'][next(iter(value['rows']))]
        self.refresh_checkpoint(value)
        translator = RepairTranslator()
        with self.assertRaises(Exception): self.rebuild(translator)
        self.assert_no_effect(translator)

    def test_all_preserved_rows_current_validation_preflight_even_unused(self):
        value = copy.deepcopy(self.old)
        text = 'Earlier revenue USD50m.'
        value['rows'][repair.unit_key(text,'en')] = {'source':text,'language':'en','text':''}
        self.refresh_checkpoint(value)
        translator = RepairTranslator()
        with self.assertRaisesRegex(Exception, 'Empty translated'): self.rebuild(translator)
        self.assert_no_effect(translator)

    def test_row_fallback_conflict_and_unknown_schema_rejected_before_model(self):
        for conflict in (True, False):
            value = copy.deepcopy(self.old)
            if conflict:
                fallback = value['source_fallbacks'][self.units[0]]
                value['rows'][self.units[0]] = {k: fallback[k] for k in ('source','language')}
                value['rows'][self.units[0]]['text'] = 'Texte'
            else: value['unexpected_metadata'] = {'private': 'PRIVATE'}
            self.refresh_checkpoint(value)
            translator = RepairTranslator()
            with self.assertRaises(Exception): self.rebuild(translator)
            self.assert_no_effect(translator)
            self.old.pop('unexpected_metadata', None)
            self.old['rows'].pop(self.units[0], None)

    def test_nonquantity_fallback_is_not_eligible(self):
        value = copy.deepcopy(self.old)
        value['source_fallbacks'][self.units[0]]['code'] = 'offline-placeholder-validation'
        self.refresh_checkpoint(value)
        translator = RepairTranslator()
        with self.assertRaises(Exception): self.rebuild(translator)
        self.assert_no_effect(translator)

    def test_plain_and_markdown_unit_identities_do_not_alias(self):
        text, language = self.old['source_fallbacks'][self.units[0]]['source'], 'en'
        self.assertNotEqual(repair.unit_key(text,language),repair.unit_key(text,language,True))
        value = copy.deepcopy(self.old)
        row = value['source_fallbacks'].pop(repair.unit_key(text,language))
        value['source_fallbacks'][repair.unit_key(text,language,True)] = row
        self.refresh_checkpoint(value)
        translator = RepairTranslator()
        with self.assertRaises(Exception): self.rebuild(translator)
        self.assert_no_effect(translator)

    def test_frozen_candidate_must_reproduce_from_exact_checkpoint_before_calls(self):
        page = self.oldcandidate/'fr/index.html'
        page.write_text(page.read_text().replace('Revenue USD10m.', 'Unrelated USD10m.'))
        self.refresh_candidate_pins()  # A self-consistent but cache-unbound old candidate.
        translator = RepairTranslator()
        with self.assertRaisesRegex(Exception,'candidate_cache_binding'): self.rebuild(translator)
        self.assert_no_effect(translator)

    def test_manifest_fallback_counts_must_match_actual_cache_uses(self):
        manifest = self.oldcandidate/'candidate-manifest.json'
        value = json.loads(manifest.read_bytes()); value['source_fallback_occurrences'] = 1
        manifest.write_bytes(stable_bytes(value)); self.refresh_candidate_pins()
        translator = RepairTranslator()
        with self.assertRaisesRegex(Exception,'fallback_counts'): self.rebuild(translator)
        self.assert_no_effect(translator)

    def test_success_and_terminal_preserve_unselected_rows_and_remaining_fallback(self):
        terminal_source = self.old['source_fallbacks'][self.units[-1]]['source']
        translator = RepairTranslator(terminal=terminal_source)
        proof = self.rebuild(translator)
        self.assertEqual(len(translator.calls), 2)
        self.assertEqual((proof['accepted_units'], proof['terminal_units']), (self.units[:1],self.units[1:]))
        self.assertEqual((proof['fallbacks_before'], proof['fallbacks_after'], proof['changed']), (2,1,True))
        new = json.loads((self.root/'new.json').read_bytes())
        self.assertEqual({k:new['rows'][k] for k in self.old['rows']},self.old['rows'])
        self.assertEqual(new['source_fallbacks'],{self.units[-1]:self.old['source_fallbacks'][self.units[-1]]})
        manifest = json.loads((self.root/'new/candidate-manifest.json').read_bytes())
        self.assertEqual((manifest['completed_page_count'], manifest['translation_calls_this_run'],
                          manifest['source_fallback_unit_count'],manifest['source_fallback_occurrences']), (2,0,1,2))

    def test_selected_subset_and_unused_fallback_are_byte_preserved(self):
        value = copy.deepcopy(self.old)
        text = 'Unselected historical revenue USD3m.'
        key = repair.unit_key(text,'en')
        value['source_fallbacks'][key] = {'source':text,'language':'en','policy':SOURCE_FALLBACK_VERSION,'code':'offline-quantity-validation'}
        self.refresh_checkpoint(value)
        proof = self.rebuild(RepairTranslator(), request={**self.request, 'units':self.units[:1]})
        new = json.loads((self.root/'new.json').read_bytes())
        untouched = {k:v for k,v in value['source_fallbacks'].items() if k != self.units[0]}
        self.assertEqual(stable_bytes(new['source_fallbacks']),stable_bytes(untouched))
        self.assertEqual((proof['fallbacks_before'],proof['fallbacks_after']), (2,1))

    def test_durable_accepted_and_terminal_reuse_across_new_owner_and_request_subset(self):
        terminal_source = self.old['source_fallbacks'][self.units[-1]]['source']
        first = self.rebuild(RepairTranslator(terminal=terminal_source))
        translator = RepairTranslator()
        second = self.rebuild(translator, name='second', owner=OTHER_OWNER)
        self.assertEqual(translator.calls, [])
        self.assertEqual(first,second)
        subset = {**self.request, 'units':self.units[:1]}
        self.rebuild(translator,name='third',request=subset,owner=OTHER_OWNER)
        self.assertEqual(translator.calls, [])
        self.assertEqual(self.client.writes,4)

    def test_imported_new_checkpoint_or_request_cannot_reset_unit_ledger(self):
        self.rebuild(RepairTranslator())
        # A new seed imports unrelated memo rows, but the unit/revision identity
        # must reuse the completed logical attempt, regardless of request hash.
        value=copy.deepcopy(self.old)
        text='An older research heading'
        value['rows'][repair.unit_key(text,'en')]={'source':text,'language':'en','text':'Ancienne analyse de référence.'}
        self.refresh_checkpoint(value)
        self.request['producer']=OTHER_OWNER
        self.request['origin_sha256']='e'*64
        retry=RepairTranslator()
        self.rebuild(retry,name='new-seed',owner=OTHER_OWNER)
        self.assertEqual(retry.calls,[])
        self.assertEqual(self.client.writes,4)

    def test_pending_claim_cannot_be_reopened_by_new_owner(self):
        first_source = self.old['source_fallbacks'][self.units[0]]['source']
        translator = RepairTranslator(crash=first_source)
        with self.assertRaises(TimeoutError): self.rebuild(translator)
        self.assertEqual(len(translator.calls),1)
        retry = RepairTranslator()
        with self.assertRaisesRegex(Exception,'started_unresolved'): self.rebuild(retry,name='retry',owner=OTHER_OWNER)
        self.assertEqual(retry.calls,[])
        self.assertEqual(self.client.writes,1)

    def test_partial_success_survives_later_unknown_outcome(self):
        last_source = self.old['source_fallbacks'][self.units[-1]]['source']
        translator = RepairTranslator(crash=last_source)
        with self.assertRaises(TimeoutError): self.rebuild(translator)
        self.assertEqual(len(translator.calls),2)
        retry = RepairTranslator()
        with self.assertRaisesRegex(Exception,'started_unresolved'): self.rebuild(retry,name='retry',owner=OTHER_OWNER)
        self.assertEqual(retry.calls,[])
        unit = self.units[0]
        _, outcome = repair.ledger_outcome(self.store,unit,repair.required_units(self.corpus)[unit])
        self.assertEqual(outcome['status'],'accepted')

    def test_later_preexisting_pending_stops_before_fresh_selected_unit(self):
        unit=self.units[-1]; source=repair.required_units(self.corpus)[unit]
        claim={**repair.claim_contract(unit,source),'producer':OWNER}
        repair.create_record(self.store,repair.ledger_key(self.store,unit,'started.json'),claim)
        translator=RepairTranslator()
        with self.assertRaisesRegex(Exception,'started_unresolved'): self.rebuild(translator)
        self.assertEqual(translator.calls,[])
        self.assertEqual(self.client.writes,1)

    def test_lost_claim_ack_or_conditional_race_never_calls_model(self):
        for race in (False,True):
            with self.subTest(race=race):
                self.client.objects.clear(); self.client.writes=0
                self.client.lose_ack='started.json'; self.client.race=race
                translator = RepairTranslator()
                with self.assertRaises(Exception): self.rebuild(translator)
                self.assertEqual(translator.calls,[])

    def test_claim_readback_failure_never_calls_model(self):
        original = self.store._get
        def read(key, **kwargs):
            if key.endswith('started.json') and key in self.client.objects:
                raise R2TransportError('synthetic readback failure')
            return original(key,**kwargs)
        translator = RepairTranslator()
        with patch.object(self.store,'_get',side_effect=read), self.assertRaises(R2TransportError): self.rebuild(translator)
        self.assertEqual(translator.calls,[])

    def test_lost_outcome_ack_is_reused_without_second_call(self):
        self.client.lose_ack='outcome.json'
        translator = RepairTranslator()
        with self.assertRaises(R2TransportError): self.rebuild(translator)
        self.assertEqual(len(translator.calls),1)
        self.client.lose_ack=None
        retry = RepairTranslator()
        self.rebuild(retry,name='retry',owner=OTHER_OWNER)
        self.assertEqual(len(retry.calls),1)
        self.assertNotEqual(retry.calls[0][0],translator.calls[0][0])

    def test_ledger_content_tamper_is_rejected_without_model(self):
        self.rebuild(RepairTranslator())
        key = repair.ledger_key(self.store,self.units[0],'outcome.json')
        value = json.loads(self.client.objects[key]['body'])
        value['row']['text'] = ''
        raw = stable_bytes(value)
        self.client.objects[key].update(body=raw,ContentLength=len(raw),Metadata={'sha256':digest(raw)})
        retry = RepairTranslator()
        with self.assertRaises(Exception): self.rebuild(retry,name='retry')
        self.assertEqual(retry.calls,[])

    def test_wrong_revision_source_or_markdown_claim_is_rejected(self):
        unit=self.units[0]; source=repair.required_units(self.corpus)[unit]
        original={**repair.claim_contract(unit,source),'producer':OWNER}
        for field,value in (('validator_revision','different'),('source_sha256','0'*64),('markdown',True)):
            self.client.objects.clear()
            repair.create_record(self.store,repair.ledger_key(self.store,unit,'started.json'),{**original,field:value})
            translator=RepairTranslator()
            with self.subTest(field=field),self.assertRaisesRegex(Exception,'ledger_claim_invalid'): self.rebuild(translator)
            self.assertEqual(translator.calls,[])

    def test_missing_outcome_write_leaves_pending_without_retry(self):
        original=self.client.put_object
        def write(**kwargs):
            if kwargs['Key'].endswith('outcome.json'): raise TimeoutError('PRIVATE no write acknowledgement')
            return original(**kwargs)
        translator=RepairTranslator()
        with patch.object(self.client,'put_object',side_effect=write),self.assertRaises(R2TransportError): self.rebuild(translator)
        self.assertEqual(len(translator.calls),1)
        retry=RepairTranslator()
        with self.assertRaisesRegex(Exception,'started_unresolved'): self.rebuild(retry,name='retry')
        self.assertEqual(retry.calls,[])

    def test_selected_terminal_diagnostics_keep_hashes_and_fixed_category_only(self):
        class Diagnostic(RepairTranslator):
            def __init__(self):
                super().__init__(); self.failure_diagnostics=[]; self.validation_failure_count=0
            def translate(self,text,target,source=None,*,markdown=True):
                self.calls.append(text); self.validation_failure_count+=1
                self.failure_diagnostics.append({'source_sha256':digest(text.encode()),'response_sha256':digest(b'PRIVATE USD999m'),
                    'target_language':target,'quantities':quantity_failure_diagnostics(text,'PRIVATE USD999m'),
                    'raw_text':'PRIVATE USD999m'})
                raise OfflineTranslationValidationError('quantity failure PRIVATE USD999m')
        translator=Diagnostic(); self.rebuild(translator)
        summary=public_translation_diagnostics(translator,'fr')
        self.assertEqual(summary['terminal_validation_failure_count'],2)
        self.assertEqual({row['failure_type'] for row in summary['terminal_translation_diagnostics']},{'offline-quantity-validation'})
        for value in ('PRIVATE','USD','Revenue','Profit','999000000'):
            self.assertNotIn(value,json.dumps(summary))
        self.assertEqual(len(translator.calls),2)

    def test_existing_output_overlap_symlink_and_budget_fail_before_calls(self):
        translator=RepairTranslator()
        for output,checkpoint in ((self.oldcandidate/'new',self.root/'x.json'),
                                  (self.root/'new',self.oldcandidate/'new.json'),
                                  (self.root/'new',self.root/'new/memo.json')):
            with self.subTest(output=output),self.assertRaises(Exception):
                repair.rebuild(self.store,self.corpus,self.oldraw,self.oldcandidate,output,checkpoint,self.request,OWNER,translator,seconds=30)
            self.assert_no_effect(translator)
        link=self.root/'linked'; link.symlink_to(self.oldcandidate)
        with self.assertRaises(Exception):
            repair.rebuild(self.store,self.corpus,self.oldraw,self.oldcandidate,link,self.root/'x.json',self.request,OWNER,translator,seconds=30)
        with self.assertRaises(Exception):
            repair.rebuild(self.store,self.corpus,self.oldraw,self.oldcandidate,self.root/'new',self.root/'new.json',self.request,OWNER,translator,seconds=0)
        self.assert_no_effect(translator)

    def test_terminal_and_outer_display_failure_preserve_original_candidate_bytes(self):
        class Invalid(RepairTranslator):
            def translate(self,*args,**kwargs):
                self.calls.append(args[0]); return 'Texte __KC_PH_000__'
        translator=Invalid(); proof=self.rebuild(translator)
        self.assertFalse(proof['changed']); self.assertEqual(proof['new'],proof['old'])
        self.assertEqual(proof['fallbacks_after'],2)
        self.assertEqual((self.root/'new.json').read_bytes(),self.oldraw)
        self.assertEqual((self.root/'new/candidate-manifest.json').read_bytes(),(self.oldcandidate/'candidate-manifest.json').read_bytes())
        retry=RepairTranslator(); self.rebuild(retry,name='retry'); self.assertEqual(retry.calls,[])

    def test_successful_ledger_without_page_change_keeps_old_counts(self):
        # Numeric-only content can pass unchanged and must not overwrite a candidate
        # with identical file ID but different metadata or claim public repair.
        source='USD10m'
        corpus=make_corpus([document_from_html(url,html(url,body=f'<h1>Public research</h1><p>{source}</p>')) for url in(HOME,BLOG)])
        self.corpus=corpus
        self.oldcandidate=self.root/'numeric-old'; self.oldcheckpoint=self.root/'numeric-old.json'
        self.manifest=build(corpus,'fr',self.oldcandidate,self.oldcheckpoint,OriginalRejected(),allow_source_fallback=True,budget_seconds=30)
        self.oldraw=self.oldcheckpoint.read_bytes(); self.old=json.loads(self.oldraw)
        self.units=sorted(self.old['source_fallbacks'])
        self.request.update(source_sha256=digest(stable_bytes(corpus)),checkpoint_sha256=digest(self.oldraw),units=self.units)
        self.refresh_candidate_pins()
        proof=self.rebuild(RepairTranslator(unchanged=True))
        self.assertEqual(proof['accepted_units'],self.units)
        self.assertEqual((proof['changed'],proof['fallbacks_after']), (False,1))
        self.assertEqual((self.root/'new.json').read_bytes(),self.oldraw)

    def test_proof_checkpoint_and_page_tampering_rejected(self):
        proof=self.rebuild(RepairTranslator()); newraw=(self.root/'new.json').read_bytes()
        forged={**proof,'fallbacks_after':99}
        with self.assertRaises(Exception): repair.verify_rebuild(self.store,self.corpus,self.oldraw,newraw,self.oldcandidate,self.root/'new',self.request,forged)
        value=json.loads(newraw); value['rows'].pop(next(iter(self.old['rows'])))
        with self.assertRaises(Exception): repair.verify_rebuild(self.store,self.corpus,self.oldraw,stable_bytes(value),self.oldcandidate,self.root/'new',self.request,proof)
        page=self.root/'new/fr/index.html'; page.write_bytes(page.read_bytes()+b'changed')
        with self.assertRaises(Exception): repair.verify_rebuild(self.store,self.corpus,self.oldraw,newraw,self.oldcandidate,self.root/'new',self.request,proof)

    def test_cli_failure_and_success_are_private_text_free(self):
        for name,value in (('corpus',self.corpus),('request',{**self.request,'units':[]})):
            (self.root/(name+'.json')).write_bytes(stable_bytes(value))
        args=['inspect','--corpus',str(self.root/'corpus.json'),'--checkpoint',str(self.oldcheckpoint),
              '--candidate',str(self.oldcandidate),'--request',str(self.root/'request.json'),'--output',str(self.root/'inspection.json')]
        with redirect_stdout(io.StringIO()) as stream: self.assertEqual(repair.main(args),0)
        self.assertNotIn('USD',stream.getvalue())
        self.oldcheckpoint.write_text('PRIVATE invalid JSON USD10m')
        with redirect_stdout(io.StringIO()) as stream: self.assertEqual(repair.main(args),1)
        self.assertEqual(json.loads(stream.getvalue()),{'status':'rejected','code':'fr_fallback_inspection_failed'})


if __name__=='__main__': unittest.main()
