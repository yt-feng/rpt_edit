#!/usr/bin/env node

import { createCipheriv, createHash, randomBytes } from "node:crypto";
import { mkdir, readFile, rename, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { gzipSync } from "node:zlib";

const FORMAT = "course-directory-aes-256-gcm-v1";
const AAD = Buffer.from("course-directory-v1", "utf8");
const MAX_PLAINTEXT_BYTES = 16 * 1024 * 1024;
const MAX_ITEMS = 45000;

function argument(name) {
  const index = process.argv.indexOf(name);
  return index >= 0 ? String(process.argv[index + 1] || "") : "";
}

function fail(message) {
  process.stderr.write(`course-directory encryption failed: ${message}\n`);
  process.exit(2);
}

const inputPath = argument("--input");
const outputPath = argument("--output");
const keyEnv = argument("--key-env") || "COURSE_DIRECTORY_BUNDLE_KEY_B64";
const keyFile = argument("--key-file");
if (!inputPath || !outputPath) fail("--input and --output are required");

let key;
try {
  if (keyFile) {
    const stored = await readFile(keyFile);
    key = stored.length === 32 ? stored : Buffer.from(stored.toString("utf8").trim(), "base64");
  } else {
    key = Buffer.from(String(process.env[keyEnv] || ""), "base64");
  }
} catch (_error) {
  fail("bundle key is unavailable or invalid");
}
if (key.length !== 32) fail("bundle key must decode to exactly 32 bytes");

let plaintext;
try {
  plaintext = await readFile(inputPath);
} catch (_error) {
  fail("sanitized input is unavailable");
}
if (!plaintext.length || plaintext.length > MAX_PLAINTEXT_BYTES) fail("sanitized input size is invalid");
try {
  const payload = JSON.parse(plaintext.toString("utf8"));
  if (!payload || typeof payload !== "object" || Array.isArray(payload) || Number(payload.schema_version) !== 1) {
    fail("sanitized input schema is invalid");
  }
  if (!Array.isArray(payload.items) || !payload.items.length || payload.items.length > MAX_ITEMS) {
    fail("sanitized input flat items count is invalid");
  }
} catch (error) {
  if (error && error.code === 2) throw error;
  fail("sanitized input is not valid JSON");
}

const nonce = randomBytes(12);
const cipher = createCipheriv("aes-256-gcm", key, nonce);
cipher.setAAD(AAD);
const compressed = gzipSync(plaintext, { level: 9 });
const encrypted = Buffer.concat([cipher.update(compressed), cipher.final(), cipher.getAuthTag()]);
const envelope = Buffer.from(`${JSON.stringify({
  format: FORMAT,
  nonce: nonce.toString("base64"),
  ciphertext: encrypted.toString("base64"),
})}\n`, "utf8");
const temporaryPath = `${outputPath}.tmp-${process.pid}`;
await mkdir(path.dirname(outputPath), { recursive: true });
await writeFile(temporaryPath, envelope, { mode: 0o600 });
await rename(temporaryPath, outputPath);
process.stdout.write(`${JSON.stringify({
  output: path.basename(outputPath),
  format: FORMAT,
  encrypted_bytes: envelope.length,
  sha256: createHash("sha256").update(envelope).digest("hex"),
})}\n`);
