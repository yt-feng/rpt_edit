import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const workflowUrl = new URL("../../.github/workflows/portal-worker-emergency-deploy.yml", import.meta.url);
const workflow = await readFile(workflowUrl, "utf8");

test("Worker emergency release preserves Cron triggers through versioned deployment", () => {
  assert.match(workflow, /uses:\s*cloudflare\/wrangler-action@v4/gu);
  assert.match(workflow, /wranglerVersion:\s*"4\.125\.0"/gu);
  assert.match(workflow, /versions upload --keep-vars/gu);
  assert.match(workflow, /--secrets-file "\$\{\{ runner\.temp \}\}\/portal-worker-version-secrets\.json"/gu);
  assert.match(workflow, /--tag "run-\$\{\{ github\.run_id \}\}-\$\{\{ github\.run_attempt \}\}"/gu);
  assert.match(workflow, /versions deploy[\s\S]*?--version-tag "run-\$\{\{ github\.run_id \}\}-\$\{\{ github\.run_attempt \}\}"/gu);
  assert.match(workflow, /--percentage 100[\s\S]*?--yes/gu);
  assert.doesNotMatch(workflow, /^\s*command:\s*deploy\s*$/gmu);
  assert.doesNotMatch(workflow, /^\s*secrets:\s*\|\s*$/gmu);
  assert.match(workflow, /portal-worker-version-secrets\.json[\s\S]*?os\.O_EXCL, 0o600/gu);
  assert.match(workflow, /Remove temporary Worker version secrets[\s\S]*?unlink\(missing_ok=True\)/gu);
  assert.doesNotMatch(workflow, /wrangler triggers deploy/gu);
  assert.match(workflow, /HOT_REPORT_CLEANUP_ENABLED:\s*\$\{\{ vars\.HOT_REPORT_CLEANUP_ENABLED \|\| 'false' \}\}/gu);
  assert.match(workflow, /HOT_REPORT_CLEANUP_ENABLED = "\$HOT_REPORT_CLEANUP_ENABLED"/gu);
});
