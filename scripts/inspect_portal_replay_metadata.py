"""Bounded metadata comparison; no publication, inference, or remote writes.

Candidate HTML/body hashes describe the immutable approved candidate, not a
claim about semantic translation quality. Missing chronology stays unknown.
"""
from __future__ import annotations

from collections import Counter
import json
import re

import requests

from inspect_portal_handoff_replay import replay_identity, unique_object
from portal_extended_incremental import content_key as extended_content_key
from portal_extended_locales import (ORIGIN, daily_corpus_day, digest, file_for_url,
                                     publication_day, stable_bytes, validate_corpus)
from portal_extended_publication import LEDGER, checked_batches
from portal_extended_r2 import (DEFAULT_PREFIX, MAX_CANDIDATE_MANIFEST_BYTES,
                               MAX_SOURCE_BYTES, R2Store, partial_manifest_is_valid)
from portal_english_commentary import PREFIX, POLICY, exact
from portal_english_handoff import read_handoff
from portal_english_pipeline import (MAX_MANIFEST, batch_admission, checked_cpu_producer,
                                    content_key as english_content_key, hash_value, verify_manifest)
from portal_english_publication import (ASSEMBLY, checked_assembly, checked_batches as english_batches,
                                       read_ledger)
from publish_static_slot import slot_prefix
from resume_portal_locale_candidate import read_pinned_manifest
from verify_prepared_static_slot import read_verified_candidate_body

MAX_BATCHES = 80
MAX_CANDIDATES = 160
MAX_READS = 1600
MAX_CACHED_BYTES = 128 * 1024 * 1024


def require(condition):
    if not condition:
        raise ValueError("Replay metadata integrity check failed")


class ReadOnlyClient:
    """Helpers cannot acquire a storage mutation/listing capability."""
    def __init__(self, client):
        self._client = client
        self.reads = 0

    def __getattr__(self, name):
        if name not in {"get_object", "head_object"}:
            raise ValueError("Storage operation is forbidden")
        def read(**kwargs):
            self.reads += 1
            require(self.reads <= MAX_READS)
            return getattr(self._client, name)(**kwargs)
        return read


class MetadataStore(R2Store):
    def __init__(self, client, bucket, prefix):
        super().__init__(client, bucket, prefix)
        self._cache = {}
        self._bytes = 0

    def _get(self, key, *, maximum):
        if key not in self._cache:
            body = super()._get(key, maximum=maximum)
            self._bytes += len(body)
            require(self._bytes <= MAX_CACHED_BYTES)
            self._cache[key] = body
        require(len(self._cache[key]) <= maximum)
        return self._cache[key]


def read_identity():
    with requests.get(ORIGIN + "/.well-known/edge-state", timeout=(10, 30),
                      allow_redirects=False, stream=True) as response:
        response.raise_for_status()
        raw = response.raw.read(4097, decode_content=True)
    require(len(raw) <= 4096)
    value = json.loads(raw, object_pairs_hook=unique_object)
    require(set(value) == {"schema_version", "slot", "release_id", "tree_sha256"}
            and type(value["schema_version"]) is int and value["schema_version"] == 1
            and value["slot"] in {"a", "b"}
            and re.fullmatch(r"[0-9a-f]{32}", value["release_id"]))
    hash_value(value["tree_sha256"])
    return value


def producer_projection(value):
    # Extended and English producers have different input schemas; neither
    # arbitrary receipt fields nor a repository string enter the output.
    require(isinstance(value, dict)
            and all(re.fullmatch(r"[1-9][0-9]{0,19}", str(value.get(k, ""))) for k in ("run_id", "attempt"))
            and isinstance(value.get("sha"), str) and re.fullmatch(r"[0-9a-f]{40}", value["sha"]))
    return {"run_id": str(value["run_id"]), "attempt": str(value["attempt"]), "sha": value["sha"]}


def page_projection(generation, candidate, day, source_hash, translation_hash):
    hash_value(generation); hash_value(candidate); hash_value(source_hash); hash_value(translation_hash)
    require(publication_day(day) == day)
    return {"generation": generation, "candidate_id": candidate, "source_day": day,
            "source_content_sha256": source_hash, "translation_sha256": translation_hash}


def compare_pages(pages, owners):
    result = []
    for identity, page in sorted(pages.items()):
        owner = owners.get(identity)
        if owner is None:
            status = "novel"
        elif page["generation"] == owner["generation"] and page["candidate_id"] == owner["candidate_id"]:
            require(page == owner)
            status = "same_version"
        elif page["source_content_sha256"] != owner["source_content_sha256"]:
            status = "overlap_source_changed"
        elif page["translation_sha256"] == owner["translation_sha256"]:
            status = "same_approved_bytes"
        else:
            status = "overlap_translation_changed"
        result.append({"public_page": identity, **page, "active_owner": owner, "comparison": status})
    counts = Counter(row["comparison"] for row in result)
    return result, {key: counts[key] for key in ("novel", "same_version", "same_approved_bytes",
                                               "overlap_source_changed", "overlap_translation_changed")}


class Reader:
    def __init__(self, original, english, identity):
        self.original, self.english, self.identity = original, english, identity
        self.manifest = read_pinned_manifest(original.client, original.bucket, identity)
        self.sources, self.candidates, self.english_candidates = {}, {}, {}

    def static_json(self, relative):
        descriptor = self.manifest["files"].get(relative)
        if descriptor is None:
            return None
        raw = read_verified_candidate_body(self.original.client, self.original.bucket,
            slot_prefix(self.identity["slot"]) + relative, descriptor, maximum=MAX_MANIFEST)
        return json.loads(raw, object_pairs_hook=unique_object)

    def source(self, generation):
        hash_value(generation)
        if generation not in self.sources:
            require(len(self.sources) < MAX_BATCHES + 20)
            value = json.loads(self.original._get(self.original.source_key(generation), maximum=MAX_SOURCE_BYTES),
                               object_pairs_hook=unique_object)
            docs = validate_corpus(value)
            require(value["documents_sha256"] == generation and len(docs) <= 24 and daily_corpus_day(value))
            self.sources[generation] = value
        return self.sources[generation]

    def extended_candidate(self, generation, locale, candidate):
        key = (generation, locale, candidate)
        if key in self.candidates:
            return self.candidates[key]
        require(len(self.candidates) < MAX_CANDIDATES)
        source = self.source(generation)
        ready = json.loads(self.original._get(self.original.candidate_ready_key(locale, generation, candidate), maximum=512*1024),
                           object_pairs_hook=unique_object)
        require(ready.get("schema_version") == 1 and ready.get("ready") is True
                and ready.get("locale") == locale and ready.get("source_generation") == generation
                and ready.get("candidate_id") == candidate and ready.get("indexable") is False)
        raw = self.original._get(self.original.candidate_manifest_key(locale, generation, candidate), maximum=MAX_CANDIDATE_MANIFEST_BYTES)
        require(ready.get("manifest_sha256") == digest(raw))
        manifest = partial_manifest_is_valid(json.loads(raw, object_pairs_hook=unique_object), locale, generation)
        require(manifest["status"] == "complete-candidate" and manifest["files_sha256"] == candidate)
        docs = {doc["url"]: doc for doc in source["documents"]}
        require(len(manifest["pages"]) == len(docs)
                and {row["source_url"] for row in manifest["pages"]} == set(docs))
        pages = {}
        for row in manifest["pages"]:
            url = row["source_url"]
            require(row["path"] == locale + "/" + file_for_url(url).as_posix())
            pages[url] = page_projection(generation, candidate, daily_corpus_day(source),
                                        extended_content_key(docs[url]), row["sha256"])
        self.candidates[key] = pages
        return pages

    def english_candidate(self, generation, candidate):
        key = (generation, candidate)
        if key in self.english_candidates:
            return self.english_candidates[key]
        require(len(self.english_candidates) < MAX_BATCHES + 20)
        hash_value(generation); hash_value(candidate)
        base = self.english.key("candidates", generation, candidate)
        ready = json.loads(self.english._get(base + "/candidate-ready.json", maximum=MAX_MANIFEST), object_pairs_hook=unique_object)
        exact(ready, ["schema_version", "policy", "locale", "generation", "candidate_id", "files", "files_sha256",
                      "producer", "admission", "indexable", "ready"])
        checked_cpu_producer(ready["producer"])
        require(ready.get("schema_version") == 1 and ready.get("policy") == POLICY and ready.get("locale") == "en"
                and ready.get("generation") == generation and ready.get("candidate_id") == candidate
                and ready.get("ready") is True and ready.get("indexable") is False
                and isinstance(ready.get("files"), dict) and 1 <= len(ready["files"]) <= 50
                and ready.get("files_sha256") == digest(stable_bytes(ready["files"])))
        proof, _, source = batch_admission(self.english, self.original, generation)
        require(ready.get("admission") == proof["admission"])
        raw = self.english._get(base + "/candidate-manifest.json", maximum=MAX_MANIFEST)
        require(digest(raw) == candidate and ready["files"].get("candidate-manifest.json") == {"sha256": candidate, "bytes": len(raw)})
        manifest = verify_manifest(json.loads(raw, object_pairs_hook=unique_object), source)
        require(manifest["status"] == "complete-candidate")
        expected = {"candidate-manifest.json", "public/en/index.html"}
        for item in manifest["items"]:
            expected.add(f'private/bodies/{item["body_sha256"]}.json')
            expected.add(f'public/en/blog/{item["id"]}.html')
        require(set(ready["files"]) == expected)
        for descriptor in ready["files"].values():
            exact(descriptor, ["sha256", "bytes"])
            hash_value(descriptor["sha256"])
            require(type(descriptor["bytes"]) is int and 0 < descriptor["bytes"] <= MAX_MANIFEST)
        for item in manifest["items"]:
            require(ready["files"][f'private/bodies/{item["body_sha256"]}.json']["sha256"] == item["body_sha256"])
        if manifest["schema_version"] == 2:
            public_files = {path: descriptor for path, descriptor in ready["files"].items() if path.startswith("public/")}
            require(manifest["public_files_sha256"] == digest(stable_bytes(public_files)))
        docs = {doc["id"]: doc for doc in source["documents"]}
        pages = {item["id"]: page_projection(generation, candidate, source["day"],
            english_content_key(docs[item["id"]]), item["body_sha256"]) for item in manifest["items"]}
        self.english_candidates[key] = (ready, manifest, pages)
        return ready, manifest, pages

    def active(self):
        extended = self.static_json(LEDGER)
        batches = checked_batches(extended["batches"]) if extended else []
        require(len(batches) <= MAX_BATCHES)
        if extended:
            require(extended.get("schema_version") == 2 and extended.get("status") == "assembled")
        # Mirror the publisher's last-batch owner rule without replaying content.
        owners = {}
        for batch in batches:
            for locale, candidate in batch["candidates"].items():
                for doc in self.source(batch["generation"])["documents"]:
                    owners[(locale, doc["url"])] = (batch["generation"], candidate)
        assembly = self.static_json(ASSEMBLY)
        english = []
        ledger = None
        if assembly is None:
            require(not any(path.startswith("en/") for path in self.manifest["files"]))
        if assembly:
            checked_assembly(assembly)
            english = english_batches(assembly["batches"])
            require(len(english) <= MAX_BATCHES)
            binding = json.loads(self.english._get(self.english.key("releases", self.identity["release_id"], "manifest.json"), maximum=65536))
            require(binding == {"schema_version": 1, "policy": POLICY, "status": "approved",
                "site_release": self.identity["release_id"], "ledger_sha256": assembly["ledger_sha256"]})
            ledger = read_ledger(self.english, assembly["ledger_sha256"])
            require(len(ledger["items"]) == assembly["page_count"])
            require(set(assembly["public_files"]) == {"en/index.html", "sitemap-en.xml",
                *(f'en/blog/{item["id"]}.html' for item in ledger["items"])})
            require({path for path in self.manifest["files"] if path.startswith("en/")}
                    == set(assembly["public_files"]) - {"sitemap-en.xml"})
            for path, descriptor in assembly["public_files"].items():
                actual = self.manifest["files"].get(path)
                require(actual is not None and actual["sha256"] == descriptor["sha256"] and actual["size"] == descriptor["bytes"])
        return batches, owners, english, ledger


def audit(reader, extended_hashes, english_hashes):
    batches, extended_owners, english_active, active_ledger = reader.active()
    groups = {}
    for identity in extended_hashes:
        raw = reader.original._get(reader.original.key("publication-handoffs", identity, "receipt.json"), maximum=65536)
        projected = replay_identity(identity, raw)
        receipt = json.loads(raw, object_pairs_hook=unique_object)
        batch = {"generation": projected["generation"], "candidates": projected["candidates"]}
        day = daily_corpus_day(reader.source(batch["generation"]))
        require(receipt.get("source_day") == day)
        key = digest(stable_bytes(batch))
        if key not in groups:
            candidates = []
            for locale, candidate in sorted(batch["candidates"].items()):
                pages = reader.extended_candidate(batch["generation"], locale, candidate)
                active = {}
                for url in pages:
                    owner = extended_owners.get((locale, url))
                    if owner:
                        active[url] = reader.extended_candidate(owner[0], locale, owner[1])[url]
                comparisons, counts = compare_pages(pages, active)
                candidates.append({"locale": locale, "candidate_id": candidate, "pages": comparisons, "counts": counts})
            groups[key] = {"generation": batch["generation"], "source_day": day, "generated_at": None,
                "approved_at": None, "exact_batch_active": batch in batches, "receipts": [], "candidates": candidates}
        groups[key]["receipts"].append({"handoff_sha256": identity, "producer": producer_projection(projected["producer"])})

    english_owners = {}
    if english_hashes:
        for batch in english_active:
            _, _, pages = reader.english_candidate(batch["generation"], batch["candidate_id"])
            english_owners.update(pages)
        require({key: row["translation_sha256"] for key, row in english_owners.items()}
                == {item["id"]: item["body_sha256"] for item in (active_ledger or {}).get("items", [])})
    english_results = {}
    for identity in english_hashes:
        receipt = read_handoff(reader.english, identity)
        batch = receipt["batch"]
        ready, manifest, pages = reader.english_candidate(batch["generation"], batch["candidate_id"])
        require(ready["producer"] == receipt["producer"] and ready["admission"] == receipt["source_admission"]
                and manifest["day"] == receipt["day"] and len(pages) == receipt["page_count"])
        key = (batch["generation"], batch["candidate_id"])
        if key not in english_results:
            comparisons, counts = compare_pages(pages, english_owners)
            english_results[key] = {"locale": "en", **batch, "source_day": manifest["day"], "generated_at": None,
                "approved_at": None, "exact_batch_active": batch in english_active,
                "receipts": [], "pages": comparisons, "counts": counts}
        english_results[key]["receipts"].append({"handoff_sha256": identity, "producer": producer_projection(receipt["producer"])})
    return {"schema_version": 2, "mode": "metadata", "active_release": reader.identity["release_id"],
            "active_tree_sha256": reader.identity["tree_sha256"], "active_extended_batches": len(batches),
            "active_english_batches": len(english_active), "receipt_count": len(extended_hashes) + len(english_hashes),
            "extended": list(groups.values()), "english": list(english_results.values()),
            "generated_at_source": "unavailable_in_candidate_schema", "approved_at_source": "unavailable_in_active_ledger",
            "comparison_basis": "immutable_candidate_html_or_body_sha256",
            "publication_authorized": False, "production_writes": 0, "inference_calls": 0}


def inspect_metadata(store, extended_hashes, english_hashes, expected_release):
    identity = read_identity()
    require(identity["release_id"] == expected_release)
    client = ReadOnlyClient(store.client)
    original = MetadataStore(client, store.bucket, DEFAULT_PREFIX)
    english = MetadataStore(client, store.bucket, PREFIX)
    result = audit(Reader(original, english, identity), extended_hashes, english_hashes)
    require(read_identity() == identity)
    result["storage_reads"] = client.reads
    return result
