# Schemas Authoring Guide

Format
- Lexicon v1 JSON under schemas/lexicons with one primary NSID per file (reverse-DNS), e.g., com.registryaccord.feed.post.
  - The file name MUST equal the NSID plus .json, e.g., `com.registryaccord.feed.post.json`.

Shapes
- Use defs: record (with required fields minimal), query (parameters + output), procedure (input + output), and refs for reuse.

Evolution
- Prefer additive changes; never rename/remove fields in place; publish breaking changes under new NSIDs; document in INDEX.

Validation
- Local: run `npm ci && npm run validate` before PRs; CI enforces the same.
  - Provide validating examples for each schema under `examples/<nsid-last-component>/` and link them from `schemas/INDEX.md`.
