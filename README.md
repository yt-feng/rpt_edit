# rpt_edit

Document workflow utilities for batch PDF processing, draft generation, review packaging, summary artifacts, media rendering, and searchable static outputs.

## Overview

This repository contains scripts and workflow glue for turning document batches into structured working artifacts. The project favors reproducible command-line steps, predictable output folders, and small reviewable packages.

## Capabilities

- Batch PDF intake from source folders.
- Text, table, and figure extraction.
- Structured draft and asset generation.
- Review package assembly.
- Optional summary and media artifact rendering.
- Static catalog and search artifact generation.

## Repository Notes

- `docs/pipeline-overview-v2.md` gives a high-level pipeline map.
- `docs/local-batch-workflow.md` describes local batch processing.
- `docs/service-architecture.md` describes the file gateway and access-code model.
- `docs/document-portal-architecture.md` describes the document portal shape.
- `docs/delivery-adapter-architecture.md` describes delivery-adapter boundaries.
- `docs/blog-seo-wechat-output.md` describes Blog persistence, SEO, and WeChat output.
- `docs/engagement-analytics-course-architecture.md` describes rewards, attribution, and Course access.
- `docs/chart-search-architecture.md` describes incremental chart-text indexing.
- `docs/source-lead-adapter.md` describes the neutral metadata-only search adapter.
