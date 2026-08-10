import assert from "node:assert/strict";
import { createDecipheriv, randomBytes } from "node:crypto";
import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { gunzipSync } from "node:zlib";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const script = path.join(root, "scripts", "encrypt_member_course_directory.mjs");

test("course directory bundle is AES-256-GCM authenticated and round-trips flat JSON", async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), "course-directory-encryption-"));
  const input = path.join(temp, "directory.json");
  const output = path.join(temp, "directory.aesgcm");
  const outputFromKeyFile = path.join(temp, "directory-key-file.aesgcm");
  const keyFile = path.join(temp, "bundle-key.txt");
  const payload = {
    schema_version: 1,
    generated_at: "2026-08-10T00:00:00Z",
    items: [{
      id: "file-00000001",
      course_id: "cap-03",
      name: "Market Authority listing review",
      folders: ["Listing practice"],
      extension: "pdf",
      size_label: "2 MB",
      date: "2026-08-10",
      entities: ["Market Authority"],
    }],
  };
  await writeFile(input, JSON.stringify(payload));
  const key = randomBytes(32);
  await writeFile(keyFile, key.toString("base64"), { mode: 0o600 });
  const run = spawnSync(process.execPath, [script, "--input", input, "--output", output], {
    encoding: "utf8",
    env: { ...process.env, COURSE_DIRECTORY_BUNDLE_KEY_B64: key.toString("base64") },
  });
  assert.equal(run.status, 0, run.stderr);
  assert.equal(run.stdout.includes(input), false, "the private plaintext path must not be logged");

  const envelope = JSON.parse(await readFile(output, "utf8"));
  assert.equal(envelope.format, "course-directory-aes-256-gcm-v1");
  const nonce = Buffer.from(envelope.nonce, "base64");
  const sealed = Buffer.from(envelope.ciphertext, "base64");
  const decipher = createDecipheriv("aes-256-gcm", key, nonce);
  decipher.setAAD(Buffer.from("course-directory-v1", "utf8"));
  decipher.setAuthTag(sealed.subarray(-16));
  const compressed = Buffer.concat([decipher.update(sealed.subarray(0, -16)), decipher.final()]);
  assert.deepEqual(JSON.parse(gunzipSync(compressed).toString("utf8")), payload);

  const tampered = Buffer.from(sealed);
  tampered[0] ^= 1;
  const rejected = createDecipheriv("aes-256-gcm", key, nonce);
  rejected.setAAD(Buffer.from("course-directory-v1", "utf8"));
  rejected.setAuthTag(tampered.subarray(-16));
  assert.throws(() => Buffer.concat([rejected.update(tampered.subarray(0, -16)), rejected.final()]));

  const keyFileRun = spawnSync(process.execPath, [
    script,
    "--input", input,
    "--output", outputFromKeyFile,
    "--key-file", keyFile,
  ], { encoding: "utf8", env: { ...process.env, COURSE_DIRECTORY_BUNDLE_KEY_B64: "" } });
  assert.equal(keyFileRun.status, 0, keyFileRun.stderr);
  assert.equal(keyFileRun.stdout.includes(keyFile), false, "the private key path must not be logged");
});

test("course directory encryption refuses a legacy tree payload", async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), "course-directory-encryption-"));
  const input = path.join(temp, "directory.json");
  const output = path.join(temp, "directory.aesgcm");
  await writeFile(input, JSON.stringify({ schema_version: 1, directories: [], files: [{}] }));
  const run = spawnSync(process.execPath, [script, "--input", input, "--output", output], {
    encoding: "utf8",
    env: { ...process.env, COURSE_DIRECTORY_BUNDLE_KEY_B64: randomBytes(32).toString("base64") },
  });
  assert.equal(run.status, 2);
  assert.match(run.stderr, /flat items/u);
});

test("course directory encryption enforces the publish byte and item caps", async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), "course-directory-encryption-"));
  const input = path.join(temp, "directory.json");
  const output = path.join(temp, "directory.aesgcm");
  const env = { ...process.env, COURSE_DIRECTORY_BUNDLE_KEY_B64: randomBytes(32).toString("base64") };
  await writeFile(input, JSON.stringify({
    schema_version: 1,
    generated_at: "2026-08-10T00:00:00Z",
    items: Array.from({ length: 45001 }, () => ({})),
  }));
  const tooMany = spawnSync(process.execPath, [script, "--input", input, "--output", output], { encoding: "utf8", env });
  assert.equal(tooMany.status, 2);
  assert.match(tooMany.stderr, /item.*count/u);

  await writeFile(input, Buffer.alloc(16 * 1024 * 1024 + 1, 0x20));
  const tooLarge = spawnSync(process.execPath, [script, "--input", input, "--output", output], { encoding: "utf8", env });
  assert.equal(tooLarge.status, 2);
  assert.match(tooLarge.stderr, /input size/u);
});

test("private publish validator is syntactically valid and rejects contact-shaped display text", async () => {
  const workflow = await readFile(path.join(root, ".github", "workflows", "course-directory-private-publish.yml"), "utf8");
  const blocks = [...workflow.matchAll(/python - <<'PY'\n([\s\S]*?)\n {10}PY/gu)]
    .map((match) => match[1].split("\n").map((line) => line.startsWith("          ") ? line.slice(10) : line).join("\n"));
  const source = blocks.find((block) => block.includes("MAX_PLAINTEXT_BYTES"));
  assert.ok(source, "publish workflow Python validator must remain extractable");
  const syntax = spawnSync("python3", ["-c", [
    "import ast,re,sys",
    "source=sys.stdin.read()",
    "tree=ast.parse(source)",
    "assignment=next(node for node in tree.body if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == 'CONTACT_PATTERNS' for target in node.targets))",
    "patterns=eval(compile(ast.Expression(assignment.value), '<validator>', 'eval'), {'re': re})",
    "cases=('联系abc@example.com资料','网址private.example.edu资料','ftp : / /private.example.edu','www . private.example.edu','13800138000','微信 abc123')",
    "assert all(any(pattern.search(value) for pattern in patterns) for value in cases)",
  ].join("; ")], {
    encoding: "utf8",
    input: source,
  });
  assert.equal(syntax.status, 0, syntax.stderr);
  assert.match(source, /MAX_PLAINTEXT_BYTES = 16 \* 1024 \* 1024/u);
  assert.match(source, /MAX_ITEMS = 45_000/u);
  assert.match(source, /CONTACT_PATTERNS/u);
  assert.match(source, /private contact information/u);
  assert.equal(source.includes("A-Z0-9._%+-]+@"), true);
  assert.equal(source.includes("1[3-9]\\d{9}"), true);
  assert.equal(source.includes("(?:https?|ftp)\\s*:\\s*/\\s*/"), true);
  assert.equal(source.includes("www\\s*\\.\\s*"), true);
  assert.equal(source.includes("com|cn|net|org|io|co|edu|gov|info|biz|me"), true);
});
