import assert from "node:assert/strict";
import { randomBytes } from "node:crypto";
import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const script = path.join(root, "scripts", "social_receipt_crypto.mjs");

function receipt() {
  return {
    schema_version: 1,
    content_id: "2026-09-01-private-receipt",
    manifest_sha256: "a".repeat(64),
    state: "published",
    completed_at: "2026-09-01T02:00:00Z",
    results: {
      youtube: {
        state: "published",
        video_id: "private-video-id",
        published_at: "2026-09-01T02:00:00Z",
      },
      linkedin: {
        state: "published",
        post_id: "urn:li:share:private-post-id",
        published_at: "2026-09-01T02:00:00Z",
      },
    },
    failure: null,
  };
}

test("private receipt is authenticated, opaque, and round-trips", async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), "social-receipt-"));
  const input = path.join(temp, "private.json");
  const encrypted = path.join(temp, "private.json.enc");
  const output = path.join(temp, "opened.json");
  const key = randomBytes(32).toString("base64");
  await writeFile(input, JSON.stringify(receipt()));
  const seal = spawnSync(process.execPath, [script, "seal", "--input", input, "--output", encrypted], {
    encoding: "utf8",
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: key },
  });
  assert.equal(seal.status, 0, seal.stderr);
  assert.equal(seal.stdout.includes("private-video-id"), false);
  const encryptedText = await readFile(encrypted, "utf8");
  assert.equal(encryptedText.includes("private-video-id"), false);
  assert.equal(encryptedText.includes("private-post-id"), false);

  const open = spawnSync(process.execPath, [script, "open", "--input", encrypted, "--output", output], {
    encoding: "utf8",
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: key },
  });
  assert.equal(open.status, 0, open.stderr);
  assert.deepEqual(JSON.parse(await readFile(output, "utf8")), receipt());
});

test("wrong key and tampering are rejected without provider identifiers", async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), "social-receipt-"));
  const input = path.join(temp, "private.json");
  const encrypted = path.join(temp, "private.json.enc");
  const output = path.join(temp, "opened.json");
  const key = randomBytes(32).toString("base64");
  await writeFile(input, JSON.stringify(receipt()));
  assert.equal(spawnSync(process.execPath, [script, "seal", "--input", input, "--output", encrypted], {
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: key },
  }).status, 0);

  const wrongKey = spawnSync(process.execPath, [script, "open", "--input", encrypted, "--output", output], {
    encoding: "utf8",
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: randomBytes(32).toString("base64") },
  });
  assert.equal(wrongKey.status, 2);
  assert.equal(wrongKey.stderr.includes("private-video-id"), false);

  const envelope = JSON.parse(await readFile(encrypted, "utf8"));
  const ciphertext = Buffer.from(envelope.ciphertext, "base64");
  ciphertext[0] ^= 1;
  envelope.ciphertext = ciphertext.toString("base64");
  await writeFile(encrypted, JSON.stringify(envelope));
  const tampered = spawnSync(process.execPath, [script, "open", "--input", encrypted, "--output", output], {
    encoding: "utf8",
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: key },
  });
  assert.equal(tampered.status, 2);
  assert.match(tampered.stderr, /authentication failed/u);
});

test("receipt schema rejects credential-shaped fields", async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), "social-receipt-"));
  const input = path.join(temp, "private.json");
  const encrypted = path.join(temp, "private.json.enc");
  const payload = receipt();
  payload.results.youtube.access_token = "must-not-be-stored";
  await writeFile(input, JSON.stringify(payload));
  const run = spawnSync(process.execPath, [script, "seal", "--input", input, "--output", encrypted], {
    encoding: "utf8",
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: randomBytes(32).toString("base64") },
  });
  assert.equal(run.status, 2);
  assert.equal(run.stderr.includes("must-not-be-stored"), false);
});

test("key preflight uses the same strict canonical base64 validation", () => {
  const key = randomBytes(32).toString("base64");
  const valid = spawnSync(process.execPath, [script, "check-key"], {
    encoding: "utf8",
    env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: key },
  });
  assert.equal(valid.status, 0, valid.stderr);
  for (const invalid of [`${key}\n`, key.slice(0, -1), "not-base64"] ) {
    const rejected = spawnSync(process.execPath, [script, "check-key"], {
      encoding: "utf8",
      env: { ...process.env, SOCIAL_RECEIPT_KEY_B64: invalid },
    });
    assert.equal(rejected.status, 2);
  }
});
