"""Content-free observations of saved title gates; never authorize publication."""
from __future__ import annotations

import re

import wechat_title_optimizer as titles
from inspect_recovered_article_generation import TITLE_REJECTION_REASONS

POLICY = 'saved-title-evidence-diagnostic-v1'


def title_excerpt(body):
    """The production revalidation selector's unchanged evidence window."""
    excerpt = re.sub(r'[ \t]+', ' ', re.sub(r'[#>*`!\\[\\]()]+', ' ', body))
    return re.sub(r'\n{2,}', '\n', excerpt).strip()[:2200]


def quality_counts(value, institution, source):
    issues = titles.title_quality_issues(value, institution, source)
    return {'codes': sorted({code for code in issues if code in TITLE_REJECTION_REASONS}),
            'unknown_code_count': sum(code not in TITLE_REJECTION_REASONS for code in issues)}


def hook_support(candidate, faithful, source, evidence):
    """Count the existing gate's exact tokens/rules, without disclosing tokens."""
    signals = titles._title_hook_signals(candidate, faithful)
    combined = f'{titles.strip_source_filename_noise(source)}\n{evidence}'
    numbers = signals['added_numbers']
    names = signals['added_big_names']
    contrasts = signals['added_contrarian_terms']
    supported = {
        'numbers': sum(token in titles._numeric_title_tokens(combined) for token in numbers),
        'big_names': sum(token.lower() in combined.lower() for token in names),
        'contrarian': sum(titles._contrarian_additions_supported(token, '', combined) for token in contrasts),
    }
    result = {kind: {'added_count': len(tokens), 'supported_count': supported[kind],
                     'unsupported_count': len(tokens) - supported[kind]}
              for kind, tokens in (('numbers', numbers), ('big_names', names), ('contrarian', contrasts))}
    result['passes_existing_hook_gate'] = titles.filename_title_additions_are_supported(
        candidate, faithful, source, evidence)
    return result


def observe_saved_title_gates(status, body, source_markdown, batches, decision):
    """Inputs are pinned by the caller. Output contains only fixed codes/counts."""
    source, institution = status.get('original_filename'), status.get('institution_name', '')
    if not (isinstance(source, str) and 0 < len(source) <= 2048 and isinstance(institution, str)
            and len(institution) <= 200 and isinstance(body, str) and isinstance(source_markdown, str)
            and isinstance(batches, list) and 1 <= len(batches) <= 4
            and all(isinstance(batch, list) and len(batch) <= 12
                    and all(isinstance(value, str) and len(value) <= 1000 for value in batch) for batch in batches)
            and isinstance(decision, dict)):
        raise ValueError('saved_title_diagnostic_input_invalid')
    excerpt = title_excerpt(body)
    required = titles.required_filename_terms(source, institution)
    # Keep the selector's newest-response-first order; observing another evidence
    # window does not select a title or replace the decision returned to callers.
    entries = [(response + 1, index + 1, raw) for response in reversed(range(len(batches)))
               for index, raw in enumerate(batches[response])]
    candidates = [raw for _, _, raw in entries]
    if decision.get('raw_candidates') != candidates or decision.get('source_filename') != source:
        raise ValueError('saved_title_diagnostic_decision_invalid')
    fallback = titles.ensure_required_filename_terms(titles.filename_title_fallback(source, institution),
                                                    required, institution)
    faithful = titles.finalize_filename_wechat_title(candidates[0] if candidates else fallback, source, institution)
    generated = list(dict.fromkeys(titles.finalize_filename_wechat_title(raw, source, institution) for raw in candidates))

    def base_valid(value):
        return not titles.missing_required_filename_terms(value, required) and not titles.title_quality_issues(value, institution, source)

    valid = [value for value in generated if base_valid(value)]
    generic = titles.source_uses_generic_series_title(source, institution)
    concrete = [value for value in valid if not titles.title_is_generic_series(value)
                and titles.CONCRETE_TITLE_SIGNAL_RE.search(value)] if generic else []
    emergency = titles.evidence_title_fallback(excerpt, source, institution)
    anchor = (concrete or valid or [fallback if base_valid(fallback) else emergency])[0]
    saved_clean = {titles.clean_filename_wechat_title(raw, institution) for raw in candidates
                   if len(titles.clean_filename_wechat_title(raw, institution).split('：', 1)[-1]) >= 4}
    anchor_origin = ('saved_candidate' if anchor in saved_clean else
                     'filename_fallback' if anchor == fallback else 'evidence_fallback')
    evidence = {'filename_only': '', 'selector_excerpt': excerpt,
                'complete_article': body, 'verified_source_markdown': source_markdown}
    rows = []
    for response, ordinal, raw in entries:
        full = titles.clean_filename_wechat_title(raw, institution, max_chars=10000)
        cleaned = titles.clean_filename_wechat_title(raw, institution)
        finalized = titles.finalize_filename_wechat_title(raw, source, institution)
        raw_missing = set(titles.missing_required_filename_terms(raw, required))
        full_missing = set(titles.missing_required_filename_terms(full, required))
        clean_missing = set(titles.missing_required_filename_terms(cleaned, required))
        raw_numbers, full_numbers, clean_numbers = (titles._numeric_title_tokens(value) for value in (raw, full, cleaned))
        hooks = {name: hook_support(finalized, faithful, source, value) for name, value in evidence.items()}
        rows.append({'response_ordinal': response, 'candidate_ordinal': ordinal,
            'raw_character_count': len(raw), 'full_clean_character_count': len(full),
            'clean_character_count': len(cleaned), 'length_limit_changed_candidate': full != cleaned,
            'short_candidate_replaced_by_fallback': finalized != cleaned,
            'raw_quality': quality_counts(raw, institution, source),
            'full_clean_quality': quality_counts(full, institution, source),
            'clean_quality': quality_counts(cleaned, institution, source),
            'raw_missing_required_count': len(raw_missing),
            'full_clean_missing_required_count': len(full_missing),
            'clean_missing_required_count': len(clean_missing),
            'normalization_removed_required_count': len(full_missing - raw_missing),
            'length_limit_removed_required_count': len(clean_missing - full_missing),
            'normalization_removed_numeric_token_count': len(raw_numbers - full_numbers),
            'length_limit_removed_numeric_token_count': len(full_numbers - clean_numbers),
            'raw_to_clean_removed_numeric_token_count': len(raw_numbers - clean_numbers),
            'base_valid_after_finalize': base_valid(finalized),
            'is_selected_anchor': finalized == anchor,
            'meets_existing_anchor_coverage': titles.filename_anchor_coverage(finalized, anchor) >= (0.62 if required else 0.72),
            'hook_support': hooks})
    blocked = {value for value in valid if not titles.filename_title_additions_are_supported(value, faithful, source, excerpt)}
    return {'policy': POLICY, 'observational_only': True, 'response_count': len(batches),
        'candidate_count': len(entries), 'unique_generated_candidate_count': len(generated),
        'required_term_count': len(required), 'generic_series_source': generic,
        'complete_article_missing_required_count': len(titles.missing_required_filename_terms(body, required)),
        'verified_source_missing_required_count': len(titles.missing_required_filename_terms(source_markdown, required)),
        'base_valid_unique_candidate_count': len(valid),
        'base_valid_saved_candidate_count': sum(value in saved_clean for value in valid),
        'base_valid_fallback_substitution_count': sum(value not in saved_clean for value in valid),
        'anchor_origin': anchor_origin,
        'base_valid_hook_rejected_unique_count': len(blocked),
        'hook_rejection_cleared_by_complete_article_count': sum(titles.filename_title_additions_are_supported(
            value, faithful, source, body) for value in blocked),
        'hook_rejection_cleared_by_verified_source_count': sum(titles.filename_title_additions_are_supported(
            value, faithful, source, source_markdown) for value in blocked),
        'candidates': rows, 'provider_posts': 0, 'object_writes': 0}
