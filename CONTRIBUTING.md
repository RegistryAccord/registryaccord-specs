# Contributing to RegistryAccord Specs

Thanks for helping improve the protocol specifications.

Principles
- Protocol-first, developer-ready specs with strong governance, portability, and repeatability. 
- Backward-compatible evolution by default; major bumps only for explicit breaking changes.
- All schema and example changes must be validated in CI and reflected in the changelog.

What lives here
- Versioned Lexicons (JSON Schemas)
- Governance and versioning policy
- Federation draft (gateway)
- Payments design (Phase 1 design-only)
- Fixtures and conformance manifest
- Security and privacy summaries
- Style and authoring guides, templates

Workflow
1) Fork and branch from main with a descriptive name (e.g., feat/post-mentions-v1-1-0). 
2) Make changes and update fixtures: ≥3 valid and ≥3 invalid examples per schema. 
3) Run local checks: make validate-schemas, make lint-docs, make diff-schemas. 
4) Update CHANGELOG.md with semver impact and migration notes if applicable. 
5) Open a PR; fill the checklist; pass CI; request CODEOWNERS review. 
6) For draft→stable promotions, attach governance checklist and conformance status.

Governance gates
- Draft: open iteration; not required for external conformance.
- Stable: frozen except additive changes; requires conformance-ready fixtures.
- Deprecated: scheduled removal with migration guidance and timelines.

Semver for schemas
- Patch: clarifications, doc typos, non-normative notes.
- Minor: additive fields/enum values with no breaking invariants.
- Major: removals/renames/behavioral changes; requires deprecation plan and migration.

PR checklist
- [ ] Schemas validate; fixtures cover edge cases and negative cases.
- [ ] CHANGELOG updated with semver and rationale.
- [ ] SPEC_INDEX.json and SPEC_VERSION_MATRIX.md updated if needed.
- [ ] Federation samples or payments design updated if payloads change.
- [ ] Governance checklist attached for status changes.
- [ ] Links validated; docs lint passes.

Local commands
- make validate-schemas
- make lint-docs
- make diff-schemas

Community norms
- Respectful and constructive collaboration.
- Security-sensitive issues use private disclosure channels (see SECURITY.md).

Licensing
- Schemas and docs are released under a permissive license for maximum interoperability.
