# KC桌面 agent toolkit

Read authorized reports and existing processed artifacts through the KC桌面 customer content API. This folder is a portable AgentSkills package, a dependency-free Python CLI, and an optional stdio MCP server. It creates no account, grant, or key and performs no model generation.

## Requirements and credentials

The CLI requires Python 3.10+. Obtain a customer content API grant and create a key in the KC桌面 account interface. The administrator determines the corpus, scopes and expiry. Supply the key through the host's secret/environment settings as `KCD_API_KEY`; do not put a real key in chat, command arguments, this folder or a committed configuration file.

| Environment variable | Purpose |
| --- | --- |
| `KCD_API_KEY` | Bearer customer API key; needed only for content calls |
| `CONTENT_API_BASE_URL` | HTTPS origin only; defaults to `https://kcdesk.com`. No path, credentials, query, fragment or nonstandard port. Set only to a trusted deployment that should receive this key. |
| `CONTENT_DOWNLOAD_DIR` | Local output directory, default `./content-downloads` relative to the executing process. Use an absolute directory for an MCP host. |

All requests are GETs. No key is needed to inspect the CLI or MCP tool catalog. The five API route families are `/api/content/v1/reports`, `/reports/{id}`, `/reports/{id}/download`, `/reports/{id}/artifacts`, and `/reports/{id}/artifacts/{artifactId}` under the same version prefix.

## CLI and portable skill

Run these from this folder, with the environment supplied by your host:

```sh
python3 scripts/content_client.py capabilities
python3 scripts/content_client.py search-reports --q "AI" --limit 10
python3 scripts/content_client.py search-reports --date 2026-10-17 --limit 25
python3 scripts/content_client.py get-report --report-id REPORT_ID
python3 scripts/content_client.py list-artifacts --report-id REPORT_ID --kind translation
python3 scripts/content_client.py read-artifact --report-id REPORT_ID --artifact-id ARTIFACT_ID
python3 scripts/content_client.py get-metadata --report-id REPORT_ID
python3 scripts/content_client.py download --report-id REPORT_ID
python3 scripts/content_client.py download --report-id REPORT_ID --artifact-id ARTIFACT_ID
```

Replace example IDs with IDs returned by the API. Search matches authorized titles and institution names, not full PDF bodies. An empty `--q` lists reports. Pass a returned `next_cursor` with `--cursor` and unchanged query/date filters to continue; clear it when changing the search. Each page has at most 100 items. Inspect `text_scope`, `language`, availability and truncation before describing coverage.

Copy this **entire folder**, including `scripts/`, into your agent's skill directory as `content-agent`. The skill refers to its own scripts, so copying only `SKILL.md` is insufficient. No package installation is required for the skill/CLI route.

## MCP

Install the optional official Python MCP SDK in a dedicated virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-mcp.txt
.venv/bin/python scripts/content_mcp.py
```

On Windows use `.venv\Scripts\python.exe`. The MCP process waits for JSON-RPC on stdin; stdout contains only protocol messages. Use the absolute interpreter and script paths in the host configuration. No `npx`, browser, remote shell or global install is required.

Generic MCP host configuration (adapt the outer configuration key to your host):

```json
{
  "mcpServers": {
    "content-api": {
      "command": "/absolute/path/content-agent/.venv/bin/python",
      "args": ["/absolute/path/content-agent/scripts/content_mcp.py"],
      "env": {
        "KCD_API_KEY": "REPLACE_IN_YOUR_HOST_SECRET_CONFIGURATION",
        "CONTENT_DOWNLOAD_DIR": "/absolute/path/content-downloads"
      }
    }
  }
}
```

The placeholder is not a working credential. If your host supports secret references or secure environment injection, use that mechanism. Environment expansion syntax differs between hosts; this toolkit does not interpolate `${...}` itself.

| MCP tool | Input |
| --- | --- |
| `content_search_reports` | Optional `q`, `date`, `cursor`, `limit` |
| `content_get_report` | `report_id` |
| `content_list_artifacts` | `report_id`; optional `kind`, `language`, `cursor`, `limit` |
| `content_read_artifact` | `report_id`, `artifact_id`; optional `max_chars` (1–80,000; default 20,000) |
| `content_get_metadata` | `report_id` |
| `content_download` | `report_id`; optional `artifact_id` (omit for original PDF) |

Each tool result includes `api_requests: {attempted, http_200}` for that tool call. These count physical HTTP attempts and received HTTP 200 responses, including a 200 whose body later fails validation; they are not an invoice or proof of completed transfer. Each current tool makes at most one REST attempt and does not automatically follow pagination.

Tool schemas contain bounds and reject unknown arguments. Tool failures return `isError: true` with fixed error codes and, when available, HTTP status and numeric retry-after. The download tool is marked as a local write; other tools do not write local files. API reads can consume existing request/download allowances.

The adapter uses the **official `mcp>=1.28,<2` supported maintenance line**, rather than a handwritten protocol. The SDK handles lifecycle, version negotiation, request validation and stdio. Protocol versions **2025-06-18** and **2025-11-25** are covered by the offline handshake tests. It does not claim support for draft protocol extensions or native remote HTTP MCP hosting.

## OpenClaw

OpenClaw supports AgentSkills folders. Place this folder at `<workspace>/skills/content-agent` (or a local skill root that your OpenClaw installation already uses). Supply `KCD_API_KEY` to the actual execution environment and ask the agent to use the `content-agent` skill. A sandbox needs the scripts, Python and secret in that sandbox; host environment injection alone may not reach it. This route uses the standard-library CLI and does not require MCP.

The current official documentation also describes `openclaw skills install /absolute/path/content-agent --as content-agent`. Choose either your existing folder-copy workflow or your installed version's local installer. This repository does not execute either installation or alter OpenClaw configuration. [Official OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills).

## Hermes Agent

Hermes accepts local skills under `~/.hermes/skills/`; copy this folder there as `content-agent` to use the CLI skill. For MCP, merge a server entry into the configuration you manage (`~/.hermes/config.yaml` by default):

```yaml
mcp_servers:
  content-api:
    command: /absolute/path/content-agent/.venv/bin/python
    args: ["/absolute/path/content-agent/scripts/content_mcp.py"]
    env:
      KCD_API_KEY: "REPLACE_IN_YOUR_HOST_SECRET_CONFIGURATION"
      CONTENT_DOWNLOAD_DIR: /absolute/path/content-downloads
```

The example follows the official `mcp_servers` → `command` / `args` / `env` format; do not replace unrelated settings. Prefer your installation's supported secret storage. Reload the host according to its instructions after adding the server. [Official Hermes quickstart: skills and MCP](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart).

## Delivery behavior and validation

- HTTPS only, 30-second socket timeout plus an elapsed-time check between reads; normal TLS verification remains enabled. All redirects, including same-host redirects, are refused. The configured bearer key is sent only to the configured origin.
- JSON responses are bounded to 2 MiB. Text reads consume at most 256 KiB plus one byte to detect truncation and return `truncated`, `returned_chars`, `source_bytes` and the exact `api_source_url` called. That API URL requires authorization; no public webpage URL is inferred. Only UTF-8 plain text, Markdown and JSON can be read into tool context. `extracted-text` is explicitly labeled as an excerpt; other artifacts retain their descriptor's meaning.
- File downloads are capped at 64 MiB, check the declared length, and use generated exclusive filenames with private permissions in the operator-configured directory. Remote filenames never control paths. Partial files are removed on failure. The returned `computed_sha256` describes received bytes, and `manifest_hash_verified: false` explicitly indicates that it was not compared against the publisher's manifest.
- No automatic retries: a failed or interrupted request may already consume API allowance. Error text never includes raw upstream bodies, headers, credentials or transport exception text. Retrieved source text is untrusted and must not be executed or treated as agent instructions.

Run offline tests from the repository root:

```sh
python3 -m unittest discover -s integrations/content-agent/tests -v
integrations/content-agent/.venv/bin/python -m unittest discover -s integrations/content-agent/tests -v
```

The standard-library run covers a fake upstream, query/pagination encoding, authorization headers, ID validation, redirects, secret reflection, response bounds, truncation and file cleanup. With the SDK installed, tests exercise real stdio initialization for the two protocol versions, tool discovery without a key, `isError` responses and a real SDK client calling the adapter against a fake upstream. Tested with Python 3.14 and official MCP SDK 1.30.0. Python 3.10 is the source-language minimum, not a claim of every-platform testing.

OpenClaw and Hermes instructions were checked against their official documentation; their installed applications were not launched or tested here. Offline tests do not prove a customer's grant, key, production content availability or live search deployment. Those require a separately supplied valid customer key and a successful authorized content read.

[Official Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk/tree/v1.x) · [MCP 2025-06-18 lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
