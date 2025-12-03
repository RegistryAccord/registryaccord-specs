# ADR-012: Content-Addressed Storage with SHA-256 Hashing

- **Status:** Accepted
- **Author:** RegistryAccord Team
- **Created:** 2025-11-18
- **Updated:** 2025-11-18

## Summary
RegistryAccord stores media assets using content-addressed identifiers derived from SHA-256 hashes. Objects are addressed as `hash:<sha256-hex>` regardless of physical backend (S3, GCS, IPFS, etc.). This guarantees integrity, enables automatic deduplication, ensures immutability, and keeps identifiers verifiable across the decentralized ecosystem.

## Context
The platform ingests large media files from many participants. Location- or UUID-based addressing duplicates data, lacks tamper detection, and allows silent mutation. A cryptographic hash provides a deterministic identifier based solely on content, supporting deduplication and integrity guarantees crucial for provenance, moderation, and inter-operator replication.

## Decision
- Use SHA-256 to compute a 64-hex-character identifier for every object.
- Storage URLs take the form `https://storage.registryaccord.com/objects/hash:<sha256>`.
- Upload flow: client computes hash, checks existence via `HEAD`, uploads only if missing, and server verifies hash before committing.
- Content Registry references storage objects via their hash IDs; metadata/versions track additional info.

## Rationale
- **Integrity:** Any consumer can recompute SHA-256 to verify the file matches the advertised content.
- **Deduplication:** Identical files share the same hash; uploads can be skipped if the object already exists.
- **Immutability:** Changing file bytes alters the hash, making tampering detectable.
- **Ecosystem portability:** SHA-256 is ubiquitous and independent of any specific storage backend.

## Consequences
**Positive:** Reduced storage/bandwidth through deduplication, tamper-evident content, verifiable exchange between operators, and backend agnosticism.

**Negative:** Hash reveals when two parties store identical content (privacy consideration), metadata is stored separately, and mutable content requires new hashes for every change.

## Alternatives Considered
1. **UUID addressing:** Simple but lacks deduplication/integrity and can silently mutate.
2. **Location-based paths:** Human-readable but mutable and non-verifiable.
3. **IPFS-only CIDs:** Strong guarantees but imposes IPFS infrastructure requirements; SHA-256 can still underpin optional IPFS backends.
4. **Weaker hashes (MD5/SHA-1):** Faster but cryptographically broken; rejected for security reasons.

## Implementation
- Storage Gateway enforces hash verification on upload/finalize operations and exposes HEAD/GET endpoints by hash.
- Content service stores the hash alongside version metadata and integrity manifests.
- Examples in `openapi/storage/v1/openapi.yaml` document request/response shapes referencing hash IDs.
- SDKs provide helper utilities to compute SHA-256 before upload.

## References
- `SPECS_REQUIREMENTS.md` §§2.2, 5.4
- Storage OpenAPI specification
- ADR-004 (Content Integrity Hashing)

_Last updated: 2025-11-18_
