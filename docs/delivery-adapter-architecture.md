# Delivery Adapter Architecture

Last updated: 2026-08-06

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
- Title rewrites must not drop an otherwise valid item.
- Sensitive wording should trigger rewrite or cooling, not silent deletion.
- Generated content should follow the adapter's formatting and review rules.

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
