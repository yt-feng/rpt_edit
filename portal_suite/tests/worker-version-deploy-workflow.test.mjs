import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const workflowUrl = new URL("../../.github/workflows/portal-worker-emergency-deploy.yml", import.meta.url);
const workflow = await readFile(workflowUrl, "utf8");

test("Worker emergency release preserves Cron triggers through versioned deployment", () => {
  assert.match(workflow, /uses:\s*cloudflare\/wrangler-action@v4/gu);
  assert.match(workflow, /wranglerVersion:\s*"4\.125\.0"/gu);
  assert.match(workflow, /versions upload --keep-vars/gu);
  assert.match(workflow, /--tag "git-\$\{\{ github\.sha \}\}"/gu);
  assert.match(workflow, /versions deploy[\s\S]*?--version-tag "git-\$\{\{ github\.sha \}\}"/gu);
  assert.match(workflow, /--percentage 100[\s\S]*?--yes/gu);
  assert.doesNotMatch(workflow, /^\s*command:\s*deploy\s*$/gmu);
  assert.doesNotMatch(workflow, /wrangler triggers deploy/gu);
});
