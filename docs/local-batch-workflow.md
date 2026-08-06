# Local Batch Workflow

This document describes the repo-local PDF processing path.

## Inputs

Place PDF files in the input directory. Nested folders are supported by the processing scripts.

```text
pdfs/
  sample-a.pdf
  sample-b.pdf
```

## Running In GitHub Actions

1. Open the repository in GitHub.
2. Go to **Actions**.
3. Choose the relevant batch-processing workflow.
4. Use workflow parameters appropriate for the input folder, output folder, language, OCR mode, and commit behavior.

## Output Shape

A successful batch creates one folder per input document, plus a summary file for the run. The generated folder usually contains:

- normalized source text;
- generated draft files;
- extracted and normalized figures;
- status metadata;
- optional packaged artifacts.

Prompt files, raw extraction archives, provider logs, and temporary status files are intermediate materials. Review packages should exclude those files unless an operator explicitly needs them.

## Local Runs

The same pipeline can run locally when the required Python dependencies are available. Prefer the repository's existing scripts and workflow defaults for local debugging.

Write experimental outputs to a disposable folder.

## Maintenance

- Keep this document focused on the local batch shape.
- If workflow parameters still contain historical names, treat them as compatibility labels.
