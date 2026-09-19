# DeepSeek usage attribution

Each production stage uses its own provider key. GitHub Actions keeps the process variable `DEEPSEEK_API_KEY` for script compatibility and maps it to the stage-specific repository secret below. Provider key names identify this repository and stage in the DeepSeek usage console.

| Provider key name | Repository secret | Consumers |
| --- | --- | --- |
| `gha-rpt-edit-selection` | `DEEPSEEK_SELECTION_API_KEY` | Dropbox and bilingual-video report selection |
| `gha-rpt-edit-report-notes` | `DEEPSEEK_REPORT_NOTES_API_KEY` | Dropbox, institution, consulting and bilingual-video PDF-to-notes generation |
| `gha-rpt-edit-podcast` | `DEEPSEEK_PODCAST_API_KEY` | Dropbox article/podcast postprocessing and bilingual podcast/video scripts |
| `gha-rpt-edit-finalize` | `DEEPSEEK_FINALIZE_API_KEY` | Dropbox final content and downstream social copy |
| `gha-rpt-edit-report-translation` | `DEEPSEEK_REPORT_TRANSLATION_API_KEY` | Dropbox, institution, consulting and ARK translated reports; translated-report test; static locale translation and its bounded preflight |
| `gha-rpt-edit-market-views` | `DEEPSEEK_MARKET_VIEWS_API_KEY` | Market Views synthesis and coverage validation |
| `gha-rpt-edit-catalog-titles` | `DEEPSEEK_CATALOG_TITLES_API_KEY` | Chinese catalog-title translation during the edge release |
| `gha-rpt-edit-portal-runtime` | `DEEPSEEK_PORTAL_RUNTIME_API_KEY` | Portal Worker Report Chat, Newsfeed and research calls |

The report-translation bucket includes editorial rewrites and title refinement performed inside the report translation script. The catalog-titles bucket is the separate catalog-maintenance stage. MinerU, DeepL and ElevenLabs usage is unaffected by this mapping.

## Key provisioning and activation

1. Create the named keys in the DeepSeek account and set the corresponding Actions repository secrets before deploying these workflow changes. Keep credential values out of files, source control, logs and artifacts.
2. The workflows intentionally do not fall back to `DEEPSEEK_API_KEY`, `DEEPSEEK_API_KEY_BACKUP`, `DEEPSEEK_API_KEY_2` or `DEEPSEEK_API_KEYS` repository secrets. Existing backup environment entries are empty to prevent shared-key consumption. If a backup is added later, give it the same stage attribution and a separate stage-specific secret.
3. Update the running portal Worker's `DEEPSEEK_API_KEY` binding with the portal-runtime key, or deploy a Worker version through `portal-worker-emergency-deploy.yml`, which materializes it from `DEEPSEEK_PORTAL_RUNTIME_API_KEY`. Changing a GitHub secret alone does not update an already-running Worker. The emergency deployment now fails materialization if this stage secret is absent.
4. Confirm the deployed workflow revision, then check subsequent stage runs and the corresponding provider usage entries. A `/models` or balance check verifies key acceptance without running a generation pipeline; it does not establish that every stage has executed.
5. Retain the former shared key until other repositories and non-Actions consumers have migrated. Usage accrued before activation remains assigned to that original key.

Runtime code continues reading `env.DEEPSEEK_API_KEY`; its process variable name is independent of the Actions secret name. The existing retry and key-pool logic remains available to local callers.

## Offline verification

Run the existing workflow contract tests after changing mappings:

```sh
python3 -B scripts/test_neutral_edge_cutover_workflow.py
python3 -B scripts/test_portal_locale_translation_preflight_workflow.py
python3 -B scripts/test_portal_worker_emergency_deploy_workflow.py
python3 -B scripts/test_market_views_workflow_contract.py
python3 -B scripts/test_ark_workflow_contract.py
python3 -B scripts/test_deepseek_http.py
```

Also parse changed workflow YAML and confirm no shared DeepSeek secret references remain in `.github/workflows/`.
