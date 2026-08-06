# rpt_edit

Private document automation utilities for batch PDF processing, draft generation, review packaging, summary artifacts, media rendering, and protected document search.

This public README intentionally describes the repository at a system level. Some scripts and workflows still carry historical internal names for compatibility; those names are implementation details rather than public product or channel labels.

## What It Does

- Ingest PDF batches from a cloud folder or a repo-local input folder.
- Extract text and figures, normalize visual assets, and prepare structured intermediate files.
- Generate target-specific drafts and review packages from the extracted material.
- Build optional summary PDFs, audio/video explainers, and static search indexes.
- Serve private source files through a serverless gateway backed by object storage.
- Keep raw inputs, prompts, logs, and publish-ready artifacts separated.

## Typical Operation

1. Configure the required provider and storage credentials in repository secrets.
2. Open GitHub Actions and run the relevant scheduled or manual workflow.
3. Review generated packages before using them outside the repository.
4. Treat generated outputs as transient artifacts unless a workflow explicitly commits them.

## Configuration

The baseline PDF extraction and generation workflows require:

- `MINER_U`
- `DEEPSEEK_API_KEY`

Additional workflows may require cloud-folder access, object-storage credentials, account-store credentials, serverless deployment credentials, alerting credentials, or delivery-adapter credentials. Secrets should stay in GitHub Actions, Cloudflare, or the relevant managed service; they should not be committed to the repository.

## Public Source And Deployment Config

Public names, domains, account labels, external repositories, and storage identifiers in this repository should be treated as aliases. Production mappings, verification files, brand assets, and operator-only configuration belong in encrypted secrets or encrypted asset bundles that are materialized by runners in temporary workspaces.

Automation should remain disabled by default until the required private deployment profile and asset keys are configured. Generated packages, drafts, media, and caches should go to private storage or temporary workspaces unless a workflow explicitly commits a public-safe artifact.

## Public Docs

- `docs/pipeline-overview-v2.md`: neutral overview of the automation pipeline.
- `docs/local-batch-workflow.md`: generic repo-local PDF batch workflow notes.
- `docs/service-architecture.md`: protected document service architecture and access-code derivation model.
- `docs/document-portal-architecture.md`: neutral architecture notes for the protected document portal.
- `docs/delivery-adapter-architecture.md`: neutral delivery-adapter boundaries and recovery notes.

## Notes

- Public-facing documentation should use neutral names such as "content package", "document portal", "external adapter", and "delivery artifact".
- Destination channels, upstream source brands, customer contact handles, and pricing copy belong in private operational notes, not in public repository docs.
- Historical file names are not renamed in this cleanup because the workflows depend on them.
