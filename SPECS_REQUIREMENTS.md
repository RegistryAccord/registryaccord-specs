# Registry Accord Specs Requirements

Purpose
- This document defines how to author, version, validate, and release protocol specifications (schemas, federation drafts, payments design) for Registry Accord. It also provides precise, automatable instructions for assistants and CI to build, test, and debug specifications.

Scope
- Applies to /lexicons, /governance, /federation, /payments-design, /fixtures, /conformance, /security, /docs-index, and the root CHANGELOG.md.

Repository Structure (authoritative)
- /lexicons/{namespace}/{name}/{version}.json
- /governance/SCHEMA_GOVERNANCE.md
- /federation/GATEWAY_FEDERATION_v0.md
- /payments-design/{doc}.md (Phase 1: design-only)
- /fixtures/{namespace}/{name}/{version}/valid/*.json
- /fixtures/{namespace}/{name}/{version}/invalid/*.json
- /conformance/manifest.yaml
- /security/{doc}.md
- /docs-index/{doc}.md
- /CHANGELOG.md
- /ADR_INDEX.md
- /API_REFERENCES.md

Authoring Rules for JSON Schemas (Lexicons)
- File path: /lexicons/{namespace}/{name}/{version}.json where {version} is semver (e.g., 1.0.0).
- Required top-level fields: $schema, $id, title, description, type, properties, required, additionalProperties.
- Namespaces: lowercase dot-delimited (e.g., ra.social.profile), names: kebab-case (e.g., post), versions: semver.
- Backward-compatible changes: additive only; breaking changes require major bump and deprecation plan in /governance.
- Each schema must include invariants (e.g., string length bounds, enum domains, regex for IDs/URIs) and cross-field constraints when applicable.
- Every schema must ship fixtures: ≥3 valid and ≥3 invalid examples in /fixtures; invalid cases must prove constraint enforcement.

Initial Schema Set (Phase 1)
- profile: { displayName, bio, avatar, links[], createdAt }
- post: { text, facets[], mentions[], embeds[], createdAt }
- follow: { actorDid, subjectDid, createdAt }
- like: { actorDid, subjectUri, createdAt }
- comment: { postUri, text, mentions[], createdAt }
- repost: { postUri, createdAt }
- moderationFlag: { subjectUri, type, reason, createdAt }
- mediaAsset: { assetId, did, mimeType, size, checksum, uri, createdAt }

Federation Draft v0
- Document endpoints, auth (DID/JWT), pagination, rate limits, abuse controls, SLAs, and error taxonomy in /federation/GATEWAY_FEDERATION_v0.md.
- Provide sequence diagrams (Mermaid accepted) and sample payloads referencing /lexicons types.

Payments Design (Phase 1: design-only)
- Include flows: donate, subscribe, unlock, ad campaigns; ERD for credits ledger; webhooks and signature verification.
- Mark all endpoints as non-implementing stubs for Phase 1; provide NFRs (latency, availability) and error codes.

Conformance Manifest
- /conformance/manifest.yaml must map schema versions to golden fixtures and reference conformance cases in the conformance repo.
- Include minimum pass thresholds and deviation reporting fields.

Governance & Versioning
- Follow /governance/SCHEMA_GOVERNANCE.md for namespaces, compatibility policy, deprecation windows, and release cadence.
- Each release requires: tagged version, CHANGELOG entry, and fixture validation passing in CI.

Security & Privacy Summaries
- Include Identity Key Lifecycle summary, JWT claims guidance, CDV write-path validation note, and webhook signing expectations under /security.

AI Assistant Execution Guidance
- When asked to add or change a schema:
  1) Locate /lexicons/{namespace}/{name}/{version}.json; if adding, create a new version respecting semver.
  2) Update /fixtures with ≥3 valid and ≥3 invalid examples; ensure coverage of invariants and cross-field constraints.
  3) Run validation: npm run validate-schemas or make validate-schemas.
  4) Update /CHANGELOG.md with a precise, human-readable summary and semver impact.
  5) If the change alters federation payloads, update /federation/GATEWAY_FEDERATION_v0.md samples and error taxonomy.
  6) If the change impacts conformance, update /conformance/manifest.yaml version mappings.

- When asked to propose payments design updates (Phase 1):
  1) Edit /payments-design docs only; do not introduce runnable endpoints.
  2) Keep sequence diagrams and ERD in sync; update error codes/NFRs.

- When asked to prepare a release:
  1) Verify CI passes on schema validation and fixtures.
  2) Confirm governance checklist: backward compatibility or documented deprecation path.
  3) Tag version and update /CHANGELOG.md.

Acceptance Criteria (per PR)
- All modified schemas validate against their fixtures; invalid fixtures fail as expected.
- CHANGELOG updated and semver justification included.
- Governance checklist satisfied; status labels updated (draft → stable) where applicable.
- If federation or payments design affected, corresponding docs updated with diagrams and examples.

Commands (reference)
- make validate-schemas: validate all JSON Schemas against fixtures.
- make lint-docs: basic link and Markdown checks for docs.
- make diff-schemas: compare schema versions and detect breaking changes.

Lifecycle Status
- draft: subject to change; not required for external conformance.
- stable: frozen except for additive changes; external conformance applies.
- deprecated: scheduled for removal; replacement documented.

Glossary
- DID: Decentralized Identifier
- CDV: Creator Data Vault
- Lexicon: Versioned JSON Schema for protocol data types
- Fixture: Concrete example used to validate schemas and conformance
