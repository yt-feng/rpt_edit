# Delivery Adapter Architecture

Last updated: 2026-08-10

This document describes the delivery-adapter side of the repository.

## Scope

The delivery pipeline is responsible for:

1. Discovering PDF inputs.
2. Extracting text and figures.
3. Generating short-form and long-form draft material.
4. Applying deterministic title and wording controls.
5. Rendering optional compiled documents.
6. Passing approved payloads to a delivery adapter from a controlled runner.
7. Verifying remote creation through the adapter's read-back API.

## Runner Boundary

General hosted runners handle discovery, extraction, generation, packaging, and public-safe artifacts.

Controlled self-hosted runners handle adapters that require fixed network identity or provider-specific upload pacing. Inputs to those runners should come from artifacts or commits already pushed to the remote default branch, not from a developer's local working tree.

## Component Roles

| Component Type | Role |
| --- | --- |
| Source discovery | Finds candidate PDFs and records seen state. |
| Batch extraction | Produces source text, figures, and per-item status. |
| Generation | Produces drafts, titles, summaries, and image placement hints. |
| Guard layer | Applies wording, title, and compliance controls. |
| Commit handoff | Ensures downstream jobs consume the remote source of truth. |
| Delivery adapter | Converts approved content to provider-specific payloads. |
| Read-back verifier | Confirms that the remote provider has the expected item count and identifiers. |

## Timing And Idempotency

- Only confirmed downloads or confirmed empty source states should update seen-state files.
- Network errors should remain retryable and must not be recorded as successful empty states.
- Completed item folders can be reused only when required outputs and run parameters match.
- A delivery adapter is successful only after the read-back verifier confirms the expected remote state.
- Partial successes should preserve successfully verified remote items and retry only unfinished work when possible.

## Content Controls

- Titles should be factual, complete, and understandable without private context.
- The source filename is the highest-weight title anchor. Preserve its company,
  product, technical term, geography, and report subject before adding a
  source-backed number, date, comparison, or factual hook.
- Sensitivity controls should target inflammatory, adversarial,
  political/military, and advice-like wording. They must not erase ordinary
  research facts such as growth, profit, records, guidance, or concrete data.
- Generic observation templates are failed by the deterministic quality gate;
  the gate retries the source anchor and article evidence before using a safe
  fallback.
- Title rewrites must not drop an otherwise valid item.
- Sensitive wording should trigger rewrite or cooling, not silent deletion.
- Generated content should follow the adapter's formatting and review rules.
- All WeChat generation paths share one reference-tone contract: present a
  source fact, explain its causal mechanism in plain language, then identify
  the next variable worth watching. This contract is attached in code rather
  than left to model-specific style interpretation.
- `KC评论` should be a two- or three-sentence mini-argument grounded in adjacent
  evidence. Restrained editorial first person is allowed; fabricated personal
  experience, reader interaction, and generic observation boilerplate are not.
- The public editorial label is exactly `KC评论`; upload and archive renderers
  normalize the historical label.
- WeChat body budgeting preserves complete source sentences and never invents
  a period after a hard character cut.
- Repository-at-rest templates keep the final information line on the neutral
  public placeholder. The fixed `PUBLIC_SITE_HOST` footer and validated private
  source URL materialize only in the in-memory WeChat submission clone.

## Retry Semantics

| Boundary | Expected Behavior |
| --- | --- |
| Source HTTP requests | Bounded retries for connection errors and retryable status codes. |
| Extraction provider | Bounded attempts across available provider slots. |
| Generation provider | Bounded retries with controlled fallback behavior where available. |
| Single item failure | Record status and continue the batch when possible. |
| Empty batch | Fail when inputs existed but no usable output was produced. |
| Commit handoff | Fail downstream delivery when required artifacts did not reach the remote branch. |
| Destination adapter | Bounded retries and read-back verification before declaring success. |

Permanent authentication, quota, or parameter errors should fail clearly instead of looping indefinitely.

## Observability

Each run should preserve:

- source manifests and source health;
- extraction attempt summaries;
- batch summaries and per-item status;
- delivery payload summaries;
- read-back verification summaries;
- title and wording-control audit logs;
- operational alert records when alerts are enabled.

Do not rely only on a green workflow icon. Compare input counts, generated counts, delivered counts, and remote read-back counts.

## Change Checklist

When changing this pipeline, confirm:

1. New network calls have timeout, retry, and permanent-error behavior.
2. Single-item failures do not erase successful siblings.
3. Failed source discovery does not write false seen state.
4. Title and wording controls run before delivery.
5. Downstream runners consume remote artifacts or commits.
6. Destination adapters perform read-back verification.
7. Targeted tests or dry-run payload checks were updated.
