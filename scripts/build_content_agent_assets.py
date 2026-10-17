#!/usr/bin/env python3
"""Build deterministic public Agent download and the read-only OpenAPI contract."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "portal_suite/site_src"
PACKAGE = ROOT / "integrations/content-agent"
FILES = ["SKILL.md", "README.md", "requirements-mcp.txt", "scripts/content_client.py", "scripts/content_mcp.py"]


def parameter(name, description, location="query", **schema):
    return dict(name=name, description=description, **{"in": location},
                required=location == "path", schema=schema or {"type": "string"})


def contract():
    page = [parameter("cursor", "Opaque cursor; preserve filters.", type="string", maxLength=512),
            parameter("limit", "Rows per page.", type="integer", minimum=1, maximum=100, default=25)]
    rid = parameter("id", "Report ID from the directory.", "path", type="string", pattern="^[a-f0-9]{24}$")
    aid = parameter("artifactId", "Artifact ID returned by this report's material list.", "path",
                    type="string", pattern="^[A-Za-z0-9][A-Za-z0-9_-]{0,159}$")
    kinds = ["text", "image", "chart", "metadata", "translation", "article", "pdf"]
    report_fields = {key: {"type": "string"} for key in ["id", "title", "title_zh", "title_en", "institution", "date", "processed_updated_at"]}
    report_fields.update(page_count={"type": "integer", "minimum": 0}, pdf_listed={"type": "boolean"},
                         pdf_available={"type": "boolean"}, source={"enum": ["catalog", "processed"]})
    report = dict(type="object", required=["id", "title", "title_zh", "title_en", "institution", "date", "pdf_listed", "source"], properties=report_fields)
    artifact_fields = {key: {"type": "string"} for key in ["id", "report_id", "language", "mime_type", "filename", "text_scope"]}
    artifact_fields.update(kind={"enum": kinds}, size={"type": ["integer", "null"], "minimum": 0},
                           sha256={"type": "string", "pattern": "^[a-f0-9]{64}$"}, page_number={"type": "integer"})
    artifact = dict(type="object", required=["id", "report_id", "kind", "language", "mime_type", "size"], properties=artifact_fields)
    error = {"type": "object", "required": ["ok", "error"], "properties": {"ok": {"const": False}, "error": {"type": "string"}}}

    def listing(name):
        return {"type": "object", "required": ["ok", "items", "next_cursor"], "properties": {
            "ok": {"const": True}, "items": {"type": "array", "items": {"$ref": "#/components/schemas/" + name}},
            "next_cursor": {"type": ["string", "null"]}}}

    def operation(name, summary, params, scope, response=None, binary=False):
        success = {"description": "Success", "content": {"application/json": {"schema": response}}}
        if binary:
            media_types = ["application/pdf"] if name == "downloadReport" else [
                "application/pdf", "text/plain", "text/markdown", "application/json", "image/jpeg", "image/png", "image/webp"]
            media = {}
            for mime in media_types:
                # Artifact JSON is the material itself, not an {ok: ...} envelope.
                schema = {"type": "object", "additionalProperties": True} if mime == "application/json" else {"type": "string"}
                if not mime.startswith("text/") and mime != "application/json":
                    schema["format"] = "binary"
                media[mime] = {"schema": schema}
            success = {"description": "Authorized file bytes (maximum 256 MiB), not a URL. Actual MIME is PDF, text/Markdown, JSON, JPEG, PNG or WebP.",
                       "headers": {"Content-Length": {"schema": {"type": "integer"}}, "Content-Type": {"schema": {"type": "string"}}},
                       "content": media}
        return {"get": {"operationId": name, "summary": summary,
                        "description": "Requires " + scope + ". Reads existing published content only; no new generation.",
                        "x-required-scope": scope, "parameters": params,
                        "responses": {"200": success, "default": {"description": "Authorization, input, content or quota error; Retry-After may be present.",
                                                                    "content": {"application/json": {"schema": error}}}}}}

    paths = {
        "/reports": operation("searchReports", "List or search authorized titles and institutions", page + [
            parameter("q", "NFKC, whitespace and case normalized; at most 200 normalized Unicode characters. Not full-text/semantic search.", type="string", maxLength=800),
            parameter("date", "Exact source date, not update time.", type="string", format="date")], "reports:read", listing("Report")),
        "/reports/{id}": operation("getReport", "Get report metadata", [rid], "reports:read", {
            "type": "object", "required": ["ok", "report"], "properties": {"ok": {"const": True}, "report": {"$ref": "#/components/schemas/Report"}}}),
        "/reports/{id}/download": operation("downloadReport", "Download original PDF", [rid], "reports:download", binary=True),
        "/reports/{id}/artifacts": operation("listArtifacts", "List available published materials", [rid] + page + [
            parameter("kind", "Artifact category.", type="string", enum=kinds),
            parameter("language", "Language identifier, for example zh, en or und.", type="string")], "artifacts:read", listing("Artifact")),
        "/reports/{id}/artifacts/{artifactId}": operation("downloadArtifact", "Read or download material", [rid, aid], "artifacts:read", binary=True),
    }
    return {"openapi": "3.1.0", "info": {"title": "KC桌面 Content API", "version": "1.1.0",
            "description": "Read-only authorized content. Account-wide daily request/byte limits are operational limits, not billing meters. Each scope can be granted independently. Not every report has all materials."},
            "servers": [{"url": "https://kcdesk.com/api/content/v1"}], "security": [{"ApiKey": []}], "paths": paths,
            "components": {"securitySchemes": {"ApiKey": {"type": "http", "scheme": "bearer", "description": "KCD_API_KEY goes in Authorization, never in a URL."}},
                           "schemas": {"Report": report, "Artifact": artifact}}}


def outputs():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            info = zipfile.ZipInfo("content-agent/" + name, date_time=(2026, 10, 17, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (PACKAGE / name).read_bytes())
    data = buffer.getvalue()
    return {
        SITE / "downloads/content-agent.zip": data,
        SITE / "downloads/content-agent.zip.sha256": (hashlib.sha256(data).hexdigest() + "  content-agent.zip\n").encode(),
        SITE / "content-api.openapi.json": (json.dumps(contract(), ensure_ascii=False, indent=2) + "\n").encode(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when generated assets differ.")
    args = parser.parse_args()
    stale = []
    for path, data in outputs().items():
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    if stale:
        raise SystemExit("Regenerate Agent assets: " + ", ".join(stale))
    print("Agent assets match sources." if args.check else "Built Agent download and OpenAPI contract.")


if __name__ == "__main__":
    main()
