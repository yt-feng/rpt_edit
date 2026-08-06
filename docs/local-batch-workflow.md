# Local Batch Workflow

This document describes the generic repo-local PDF processing path. It is kept intentionally channel-neutral because the public repository should not explain destination-specific operations.

## Inputs

Place PDF files in the configured input directory. Nested folders are supported by the processing scripts.

```text
pdfs/
  sample-a.pdf
  sample-b.pdf
```

## Required Credentials

- PDF extraction provider token.
- Text generation provider token.

Optional delivery, storage, or account credentials are only needed for workflows that publish, cache, or serve artifacts.

## Running In GitHub Actions

1. Open the repository in GitHub.
2. Go to **Actions**.
3. Choose the relevant batch-processing workflow.
4. Keep the default parameters for a first run unless you need a custom input folder, output folder, language, OCR mode, or commit behavior.

## Output Shape

A successful batch creates one folder per input document, plus a summary file for the run. The generated folder usually contains:

- normalized source text;
- generated draft files;
- extracted and normalized figures;
- status metadata;
- optional packaged artifacts.

Prompt files, raw extraction archives, provider logs, and temporary status files are intermediate materials. Review packages should exclude those files unless an operator explicitly needs them.

## Local Runs

The same pipeline can run locally when the required Python dependencies and provider credentials are available. Prefer the repository's existing scripts and workflow defaults rather than copying long commands into public docs.

For local debugging, keep credentials in environment variables and write outputs to a disposable folder.

## Maintenance

- Keep this document generic.
- Do not name destination platforms, upstream source brands, contact handles, or pricing copy here.
- If workflow parameters still contain historical names, treat them as compatibility labels rather than public documentation terms.
