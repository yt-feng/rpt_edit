#!/usr/bin/env node

import { createCipheriv, createDecipheriv, randomBytes } from "node:crypto";
import { mkdir, readFile, rename, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const FORMAT = "social-receipt-aes-256-gcm-v1";
const AAD = Buffer.from("social-receipt-v1", "utf8");
const MAX_PLAINTEXT_BYTES = 512 * 1024;
const MAX_ENVELOPE_BYTES = 1024 * 1024;
const CONTENT_ID_RE = /^[a-z0-9][a-z0-9._-]{7,79}$/u;
const PROVIDERS = new Set(["youtube", "linkedin", "x"]);

function fail(message) {
  process.stderr.write(`social receipt operation failed: ${message}\n`);
  process.exit(2);
}

function argument(name) {
  const index = process.argv.indexOf(name);
  return index >= 0 ? String(process.argv[index + 1] || "") : "";
}

function decodeBase64(value, field) {
  if (!value || !/^[A-Za-z0-9+/]+={0,2}$/u.test(value) || value.length % 4 !== 0) {
    fail(`${field} is invalid`);
  }
  const decoded = Buffer.from(value, "base64");
  if (decoded.toString("base64") !== value) fail(`${field} is invalid`);
  return decoded;
}

function validateReceipt(payload) {
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    fail("receipt must be a JSON object");
  }
  const allowedTop = new Set([
    "schema_version", "content_id", "manifest_sha256", "state",
    "completed_at", "results", "failure",
  ]);
  if (Object.keys(payload).some((key) => !allowedTop.has(key))) {
    fail("receipt contains unsupported fields");
  }
  if (payload.schema_version !== 1 || !CONTENT_ID_RE.test(String(payload.content_id || ""))) {
    fail("receipt schema or content ID is invalid");
  }
  if (!["reserved", "partial", "published", "failed"].includes(payload.state)) {
    fail("receipt state is invalid");
  }
  if (!payload.results || typeof payload.results !== "object" || Array.isArray(payload.results)) {
    fail("receipt results are invalid");
  }
  for (const [provider, result] of Object.entries(payload.results)) {
    if (!PROVIDERS.has(provider) || !result || typeof result !== "object" || Array.isArray(result)) {
      fail("receipt provider result is invalid");
    }
    const idField = provider === "youtube" ? "video_id" : "post_id";
    const allowedResult = new Set(["state", idField, "published_at"]);
    if (provider === "youtube") allowedResult.add("publish_at");
    if (Object.keys(result).some((key) => !allowedResult.has(key))) {
      fail("receipt provider result contains unsupported fields");
    }
    if (result.state !== "published" || typeof result[idField] !== "string" || !result[idField]) {
      fail("receipt provider locator is invalid");
    }
    if (typeof result.published_at !== "string" || !result.published_at) {
      fail("receipt publication timestamp is invalid");
    }
  }
  if (payload.failure !== null) {
    const failure = payload.failure;
    if (!failure || typeof failure !== "object" || Array.isArray(failure)) {
      fail("receipt failure is invalid");
    }
    const keys = Object.keys(failure);
    if (keys.some((key) => !new Set(["platform", "code"]).has(key))) {
      fail("receipt failure contains unsupported fields");
    }
  }
  return payload;
}

async function atomicWrite(outputPath, data) {
  await mkdir(path.dirname(outputPath), { recursive: true });
  const temporary = `${outputPath}.tmp-${process.pid}`;
  await writeFile(temporary, data, { mode: 0o600 });
  await rename(temporary, outputPath);
}

const mode = String(process.argv[2] || "");
const inputPath = argument("--input");
const outputPath = argument("--output");
if (!new Set(["check-key", "seal", "open"]).has(mode)) {
  fail("use check-key, seal, or open");
}
if (mode !== "check-key" && (!inputPath || !outputPath)) {
  fail("seal and open require --input and --output");
}

const key = decodeBase64(String(process.env.SOCIAL_RECEIPT_KEY_B64 || ""), "receipt key");
if (key.length !== 32) fail("receipt key must decode to exactly 32 bytes");

if (mode === "check-key") {
  process.stdout.write(`${JSON.stringify({ mode, format: FORMAT })}\n`);
  process.exit(0);
}

try {
  if (mode === "seal") {
    const plaintext = await readFile(inputPath);
    if (!plaintext.length || plaintext.length > MAX_PLAINTEXT_BYTES) {
      fail("receipt plaintext size is invalid");
    }
    let payload;
    try {
      payload = JSON.parse(plaintext.toString("utf8"));
    } catch (_error) {
      fail("receipt plaintext is not valid JSON");
    }
    validateReceipt(payload);
    const nonce = randomBytes(12);
    const cipher = createCipheriv("aes-256-gcm", key, nonce);
    cipher.setAAD(AAD);
    const ciphertext = Buffer.concat([cipher.update(plaintext), cipher.final()]);
    const envelope = Buffer.from(`${JSON.stringify({
      format: FORMAT,
      nonce: nonce.toString("base64"),
      ciphertext: ciphertext.toString("base64"),
      tag: cipher.getAuthTag().toString("base64"),
    })}\n`, "utf8");
    await atomicWrite(outputPath, envelope);
    process.stdout.write(`${JSON.stringify({ mode, format: FORMAT, bytes: envelope.length })}\n`);
  } else {
    const envelopeBytes = await readFile(inputPath);
    if (!envelopeBytes.length || envelopeBytes.length > MAX_ENVELOPE_BYTES) {
      fail("encrypted receipt size is invalid");
    }
    let envelope;
    try {
      envelope = JSON.parse(envelopeBytes.toString("utf8"));
    } catch (_error) {
      fail("encrypted receipt is not valid JSON");
    }
    const keys = Object.keys(envelope || {}).sort().join(",");
    if (keys !== "ciphertext,format,nonce,tag" || envelope.format !== FORMAT) {
      fail("encrypted receipt format is invalid");
    }
    const nonce = decodeBase64(envelope.nonce, "nonce");
    const ciphertext = decodeBase64(envelope.ciphertext, "ciphertext");
    const tag = decodeBase64(envelope.tag, "authentication tag");
    if (nonce.length !== 12 || tag.length !== 16 || ciphertext.length > MAX_PLAINTEXT_BYTES) {
      fail("encrypted receipt fields are invalid");
    }
    let plaintext;
    try {
      const decipher = createDecipheriv("aes-256-gcm", key, nonce);
      decipher.setAAD(AAD);
      decipher.setAuthTag(tag);
      plaintext = Buffer.concat([decipher.update(ciphertext), decipher.final()]);
    } catch (_error) {
      fail("encrypted receipt authentication failed");
    }
    let payload;
    try {
      payload = JSON.parse(plaintext.toString("utf8"));
    } catch (_error) {
      fail("decrypted receipt is not valid JSON");
    }
    validateReceipt(payload);
    await atomicWrite(outputPath, Buffer.from(`${JSON.stringify(payload, null, 2)}\n`, "utf8"));
    process.stdout.write(`${JSON.stringify({ mode, format: FORMAT, bytes: plaintext.length })}\n`);
  }
} catch (error) {
  if (error && error.code === 2) throw error;
  fail("input or output is unavailable");
}
